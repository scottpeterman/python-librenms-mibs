# SNMP MIB module (VIPTELA-OPER-VPN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-OPER-VPN
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:07 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

viptela_oper_vpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12)
)
if mibBuilder.loadTexts:
    viptela_oper_vpn.setRevisions(
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



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Ipv4Prefix(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d.1d.1d.1d/1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5



class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class IpPrefix(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(17, 17),
    )



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class HexList(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"


class IfAddressTypeEnum(TextualConvention, Integer32):
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
        *(("ifaddrEnumInvalid", 0),
          ("ifaddrEnumIpv4Static", 1),
          ("ifaddrEnumIpv4Dhcp", 2),
          ("ifaddrEnumIpv6Static", 3),
          ("ifaddrEnumIpv6Dhcp", 4),
          ("ifaddrEnumIpv6Ra", 5),
          ("ifaddrEnumIpv6LinkLocal", 6))
    )



class SfpPowerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sfpPowerTypeAverageInputPower", 0),
          ("sfpPowerTypeOma", 1))
    )



class SfpPhysicalIdentifierEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              256)
        )
    )
    namedValues = NamedValues(
        *(("sfpPiUnknownUnspecified", 0),
          ("sfpPiGbic", 1),
          ("sfpPiSff", 2),
          ("sfpPiSfpSfpPlus", 3),
          ("sfpPiUnknown", 256))
    )



class SfpConnectorTypeEnum(TextualConvention, Integer32):
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
              32,
              33,
              34,
              35,
              36,
              256)
        )
    )
    namedValues = NamedValues(
        *(("sfpConnectorTypeUnknownUnspecified", 0),
          ("sfpConnectorTypeSc", 1),
          ("sfpConnectorTypeFcStyle1Cu", 2),
          ("sfpConnectorTypeFcStyle2Cu", 3),
          ("sfpConnectorTypeBncTnc", 4),
          ("sfpConnectorTypeCoax", 5),
          ("sfpConnectorTypeFiberJack", 6),
          ("sfpConnectorTypeLc", 7),
          ("sfpConnectorTypeRj", 8),
          ("sfpConnectorTypeMu", 9),
          ("sfpConnectorTypeSg", 10),
          ("sfpConnectorTypeOpticalPigtail", 11),
          ("sfpConnectorTypeMpo1x12", 12),
          ("sfpConnectorTypeMpo2x16", 13),
          ("sfpConnectorTypeHssdcIi", 32),
          ("sfpConnectorTypeCopperPigtail", 33),
          ("sfpConnectorTypeRj45", 34),
          ("sfpConnectorTypeNoSeparableConnector", 35),
          ("sfpConnectorTypeMxc2x16", 36),
          ("sfpConnectorTypeUnknown", 256))
    )



class SfpCalibrationType(TextualConvention, Integer32):
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
        *(("sfpCalibrationTypeNone", 0),
          ("sfpCalibrationTypeInternal", 1),
          ("sfpCalibrationTypeExternal", 2))
    )



class SfpRateSelectEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8,
              10,
              12,
              14,
              256,
              257)
        )
    )
    namedValues = NamedValues(
        *(("sfpRateSelectUnspecified", 0),
          ("sfpRateSelect4-2-1G-RateSelectAndAs0As1", 1),
          ("sfpRateSelect8-4-2G-RxRateSelect", 2),
          ("sfpRateSelect8-4-2G-TxRateSelect", 4),
          ("sfpRateSelect8-4-2G-RxAndTxRateSelect", 6),
          ("sfpRateSelect16-8-4G-RxRateSelect", 8),
          ("sfpRateSelect16-8-4G-RxAndTxRateSelect", 10),
          ("sfpRateSelect32-16-8G-RxAndTxRateSelect", 12),
          ("sfpRateSelect10-8G-RxAndTxRateSelect", 14),
          ("sfpRateSelectReserved", 256),
          ("sfpRateSelectUnallocated", 257))
    )



class SfpTransceiverComplianceEnum(TextualConvention, Integer32):
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
        *(("sfpTransceiverComplianceUnexpected", 0),
          ("sfpTransceiverCompliance10gBaseEr", 1),
          ("sfpTransceiverCompliance10gBaseLrm", 2),
          ("sfpTransceiverCompliance10gBaseSr", 3),
          ("sfpTransceiverCompliance10gBaseLr", 4),
          ("sfpTransceiverCompliance1gBaseT", 5),
          ("sfpTransceiverCompliance1gBaseCx", 6),
          ("sfpTransceiverCompliance1gBaseLx", 7),
          ("sfpTransceiverCompliance1gBaseSx", 8))
    )



class Yesno(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )



class VpnIfFlagsType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("inactive", 0),
          ("detect", 1),
          ("pseudo", 2))
    )


class SfpTimingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sfpTimingTypeInternalRetimer", 0),
          ("sfpTimingTypeCdr", 1))
    )



class SfpEncodingEnum(TextualConvention, Integer32):
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("sfpEncodingUnspecified", 0),
          ("sfpEncoding8b-10b", 1),
          ("sfpEncoding4b-5b", 2),
          ("sfpEncodingNrz", 3),
          ("sfpEncodingManchester", 4),
          ("sfpEncodingScrambled", 5),
          ("sfpEncoding64b-66b", 6),
          ("sfpEncoding256b-257b", 7),
          ("sfpEncodingPam4", 8),
          ("sfpEncodingReserved", 255))
    )



class SfpHexBytes(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class T3(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("dhcp", 0),
          ("dns", 1),
          ("icmp", 2),
          ("sshd", 3),
          ("ntp", 4),
          ("stun", 5),
          ("all", 6),
          ("bgp", 7),
          ("ospf", 8),
          ("netconf", 9),
          ("https", 10))
    )


class RouteStatusType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("b", 0),
          ("f", 1),
          ("i", 2),
          ("s", 3),
          ("r", 4),
          ("l", 5))
    )


class VpnIfPauseType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("txPause", 0),
          ("rxPause", 1))
    )


class PppInterfaceAuthEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("chap", 0),
          ("pap", 1))
    )



class CloudExpressAppType(TextualConvention, Integer32):
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



class TlocColorEnum(TextualConvention, Integer32):
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



# MIB Managed Objects in the order of their OIDs

_ArpTable_Object = MibTable
arpTable = _ArpTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 1)
)
if mibBuilder.loadTexts:
    arpTable.setStatus("current")
_ArpEntry_Object = MibTableRow
arpEntry = _ArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 1, 1)
)
arpEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "arpVpnId"),
    (0, "VIPTELA-OPER-VPN", "arpIfName"),
    (0, "VIPTELA-OPER-VPN", "arpIp"),
)
if mibBuilder.loadTexts:
    arpEntry.setStatus("current")


class _ArpVpnId_Type(Unsigned32):
    """Custom type arpVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_ArpVpnId_Type.__name__ = "Unsigned32"
_ArpVpnId_Object = MibTableColumn
arpVpnId = _ArpVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 1, 1, 1),
    _ArpVpnId_Type()
)
arpVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arpVpnId.setStatus("current")


class _ArpIfName_Type(String):
    """Custom type arpIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ArpIfName_Type.__name__ = "String"
_ArpIfName_Object = MibTableColumn
arpIfName = _ArpIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 1, 1, 2),
    _ArpIfName_Type()
)
arpIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arpIfName.setStatus("current")
_ArpIp_Type = InetAddressIP
_ArpIp_Object = MibTableColumn
arpIp = _ArpIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 1, 1, 3),
    _ArpIp_Type()
)
arpIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arpIp.setStatus("current")
_ArpMac_Type = String
_ArpMac_Object = MibTableColumn
arpMac = _ArpMac_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 1, 1, 4),
    _ArpMac_Type()
)
arpMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMac.setStatus("current")


class _ArpState_Type(Integer32):
    """Custom type arpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1),
          ("invalid", 2))
    )


_ArpState_Type.__name__ = "Integer32"
_ArpState_Object = MibTableColumn
arpState = _ArpState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 1, 1, 5),
    _ArpState_Type()
)
arpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpState.setStatus("current")
_ArpIdleTimer_Type = String
_ArpIdleTimer_Object = MibTableColumn
arpIdleTimer = _ArpIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 1, 1, 6),
    _ArpIdleTimer_Type()
)
arpIdleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIdleTimer.setStatus("current")
_ArpUptime_Type = String
_ArpUptime_Object = MibTableColumn
arpUptime = _ArpUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 1, 1, 7),
    _ArpUptime_Type()
)
arpUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpUptime.setStatus("current")
_InterfaceTable_Object = MibTable
interfaceTable = _InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2)
)
if mibBuilder.loadTexts:
    interfaceTable.setStatus("current")
_InterfaceEntry_Object = MibTableRow
interfaceEntry = _InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1)
)
interfaceEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "interfaceVpnId"),
    (0, "VIPTELA-OPER-VPN", "interfaceIfname"),
    (0, "VIPTELA-OPER-VPN", "interfaceAfType"),
)
if mibBuilder.loadTexts:
    interfaceEntry.setStatus("current")


class _InterfaceVpnId_Type(Unsigned32):
    """Custom type interfaceVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_InterfaceVpnId_Type.__name__ = "Unsigned32"
_InterfaceVpnId_Object = MibTableColumn
interfaceVpnId = _InterfaceVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 1),
    _InterfaceVpnId_Type()
)
interfaceVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceVpnId.setStatus("current")


class _InterfaceIfname_Type(String):
    """Custom type interfaceIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_InterfaceIfname_Type.__name__ = "String"
_InterfaceIfname_Object = MibTableColumn
interfaceIfname = _InterfaceIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 2),
    _InterfaceIfname_Type()
)
interfaceIfname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceIfname.setStatus("current")


class _InterfaceIpAddress_Type(String):
    """Custom type interfaceIpAddress based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_InterfaceIpAddress_Type.__name__ = "String"
_InterfaceIpAddress_Object = MibTableColumn
interfaceIpAddress = _InterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 3),
    _InterfaceIpAddress_Type()
)
interfaceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIpAddress.setStatus("current")
_InterfaceIpv6Address_Type = String
_InterfaceIpv6Address_Object = MibTableColumn
interfaceIpv6Address = _InterfaceIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 4),
    _InterfaceIpv6Address_Type()
)
interfaceIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIpv6Address.setStatus("current")


class _InterfaceIfAdminStatus_Type(String):
    """Custom type interfaceIfAdminStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_InterfaceIfAdminStatus_Type.__name__ = "String"
_InterfaceIfAdminStatus_Object = MibTableColumn
interfaceIfAdminStatus = _InterfaceIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 5),
    _InterfaceIfAdminStatus_Type()
)
interfaceIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIfAdminStatus.setStatus("current")


class _InterfaceIfOperStatus_Type(String):
    """Custom type interfaceIfOperStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_InterfaceIfOperStatus_Type.__name__ = "String"
_InterfaceIfOperStatus_Object = MibTableColumn
interfaceIfOperStatus = _InterfaceIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 6),
    _InterfaceIfOperStatus_Type()
)
interfaceIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIfOperStatus.setStatus("current")


class _InterfaceDesc_Type(String):
    """Custom type interfaceDesc based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_InterfaceDesc_Type.__name__ = "String"
_InterfaceDesc_Object = MibTableColumn
interfaceDesc = _InterfaceDesc_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 7),
    _InterfaceDesc_Type()
)
interfaceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceDesc.setStatus("current")


class _InterfaceEncapType_Type(Integer32):
    """Custom type interfaceEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("vlan", 1),
          ("ppp", 2))
    )


_InterfaceEncapType_Type.__name__ = "Integer32"
_InterfaceEncapType_Object = MibTableColumn
interfaceEncapType = _InterfaceEncapType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 9),
    _InterfaceEncapType_Type()
)
interfaceEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceEncapType.setStatus("current")


class _InterfacePortType_Type(Integer32):
    """Custom type interfacePortType based on Integer32"""
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
        *(("service", 0),
          ("transport", 1),
          ("loopback", 2),
          ("mgmt", 3))
    )


_InterfacePortType_Type.__name__ = "Integer32"
_InterfacePortType_Object = MibTableColumn
interfacePortType = _InterfacePortType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 10),
    _InterfacePortType_Type()
)
interfacePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfacePortType.setStatus("current")
_InterfaceIfindex_Type = Unsigned32
_InterfaceIfindex_Object = MibTableColumn
interfaceIfindex = _InterfaceIfindex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 11),
    _InterfaceIfindex_Type()
)
interfaceIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIfindex.setStatus("current")
_InterfaceMtu_Type = Unsigned32
_InterfaceMtu_Object = MibTableColumn
interfaceMtu = _InterfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 12),
    _InterfaceMtu_Type()
)
interfaceMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceMtu.setStatus("current")


class _InterfaceHwaddr_Type(String):
    """Custom type interfaceHwaddr based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_InterfaceHwaddr_Type.__name__ = "String"
_InterfaceHwaddr_Object = MibTableColumn
interfaceHwaddr = _InterfaceHwaddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 13),
    _InterfaceHwaddr_Type()
)
interfaceHwaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceHwaddr.setStatus("current")
_InterfaceSpeedMbps_Type = Unsigned32
_InterfaceSpeedMbps_Object = MibTableColumn
interfaceSpeedMbps = _InterfaceSpeedMbps_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 14),
    _InterfaceSpeedMbps_Type()
)
interfaceSpeedMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceSpeedMbps.setStatus("current")


class _InterfaceDuplex_Type(Integer32):
    """Custom type interfaceDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 0),
          ("half", 1),
          ("nA", 2))
    )


_InterfaceDuplex_Type.__name__ = "Integer32"
_InterfaceDuplex_Object = MibTableColumn
interfaceDuplex = _InterfaceDuplex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 15),
    _InterfaceDuplex_Type()
)
interfaceDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceDuplex.setStatus("current")
_InterfaceAutoNeg_Type = TruthValue
_InterfaceAutoNeg_Object = MibTableColumn
interfaceAutoNeg = _InterfaceAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 16),
    _InterfaceAutoNeg_Type()
)
interfaceAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceAutoNeg.setStatus("current")
_InterfacePauseType_Type = VpnIfPauseType
_InterfacePauseType_Object = MibTableColumn
interfacePauseType = _InterfacePauseType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 17),
    _InterfacePauseType_Type()
)
interfacePauseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfacePauseType.setStatus("current")
_InterfaceTcpMssAdjust_Type = UnsignedShort
_InterfaceTcpMssAdjust_Object = MibTableColumn
interfaceTcpMssAdjust = _InterfaceTcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 18),
    _InterfaceTcpMssAdjust_Type()
)
interfaceTcpMssAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTcpMssAdjust.setStatus("current")
_InterfaceUptime_Type = String
_InterfaceUptime_Object = MibTableColumn
interfaceUptime = _InterfaceUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 19),
    _InterfaceUptime_Type()
)
interfaceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceUptime.setStatus("current")
_InterfaceAllowService_Type = T3
_InterfaceAllowService_Object = MibTableColumn
interfaceAllowService = _InterfaceAllowService_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 20),
    _InterfaceAllowService_Type()
)
interfaceAllowService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceAllowService.setStatus("current")
_InterfaceRxPackets_Type = Counter64
_InterfaceRxPackets_Object = MibTableColumn
interfaceRxPackets = _InterfaceRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 21),
    _InterfaceRxPackets_Type()
)
interfaceRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPackets.setStatus("current")
_InterfaceRxOctets_Type = Counter64
_InterfaceRxOctets_Object = MibTableColumn
interfaceRxOctets = _InterfaceRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 22),
    _InterfaceRxOctets_Type()
)
interfaceRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxOctets.setStatus("current")
_InterfaceRxErrors_Type = Counter64
_InterfaceRxErrors_Object = MibTableColumn
interfaceRxErrors = _InterfaceRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 23),
    _InterfaceRxErrors_Type()
)
interfaceRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxErrors.setStatus("current")
_InterfaceRxDrops_Type = Counter64
_InterfaceRxDrops_Object = MibTableColumn
interfaceRxDrops = _InterfaceRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 24),
    _InterfaceRxDrops_Type()
)
interfaceRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxDrops.setStatus("current")
_InterfaceTxPackets_Type = Counter64
_InterfaceTxPackets_Object = MibTableColumn
interfaceTxPackets = _InterfaceTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 25),
    _InterfaceTxPackets_Type()
)
interfaceTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxPackets.setStatus("current")
_InterfaceTxOctets_Type = Counter64
_InterfaceTxOctets_Object = MibTableColumn
interfaceTxOctets = _InterfaceTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 26),
    _InterfaceTxOctets_Type()
)
interfaceTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxOctets.setStatus("current")
_InterfaceTxErrors_Type = Counter64
_InterfaceTxErrors_Object = MibTableColumn
interfaceTxErrors = _InterfaceTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 27),
    _InterfaceTxErrors_Type()
)
interfaceTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxErrors.setStatus("current")
_InterfaceTxDrops_Type = Counter64
_InterfaceTxDrops_Object = MibTableColumn
interfaceTxDrops = _InterfaceTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 28),
    _InterfaceTxDrops_Type()
)
interfaceTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxDrops.setStatus("current")
_InterfaceRxPps_Type = Counter64
_InterfaceRxPps_Object = MibTableColumn
interfaceRxPps = _InterfaceRxPps_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 29),
    _InterfaceRxPps_Type()
)
interfaceRxPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPps.setStatus("current")
_InterfaceRxKbps_Type = Counter64
_InterfaceRxKbps_Object = MibTableColumn
interfaceRxKbps = _InterfaceRxKbps_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 30),
    _InterfaceRxKbps_Type()
)
interfaceRxKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxKbps.setStatus("current")
_InterfaceTxPps_Type = Counter64
_InterfaceTxPps_Object = MibTableColumn
interfaceTxPps = _InterfaceTxPps_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 31),
    _InterfaceTxPps_Type()
)
interfaceTxPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxPps.setStatus("current")
_InterfaceTxKbps_Type = Counter64
_InterfaceTxKbps_Object = MibTableColumn
interfaceTxKbps = _InterfaceTxKbps_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 32),
    _InterfaceTxKbps_Type()
)
interfaceTxKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxKbps.setStatus("current")
_InterfaceRxArpRequests_Type = Counter64
_InterfaceRxArpRequests_Object = MibTableColumn
interfaceRxArpRequests = _InterfaceRxArpRequests_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 33),
    _InterfaceRxArpRequests_Type()
)
interfaceRxArpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxArpRequests.setStatus("current")
_InterfaceTxArpReplies_Type = Counter64
_InterfaceTxArpReplies_Object = MibTableColumn
interfaceTxArpReplies = _InterfaceTxArpReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 34),
    _InterfaceTxArpReplies_Type()
)
interfaceTxArpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxArpReplies.setStatus("current")
_InterfaceTxArpRequests_Type = Counter64
_InterfaceTxArpRequests_Object = MibTableColumn
interfaceTxArpRequests = _InterfaceTxArpRequests_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 35),
    _InterfaceTxArpRequests_Type()
)
interfaceTxArpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxArpRequests.setStatus("current")
_InterfaceRxArpReplies_Type = Counter64
_InterfaceRxArpReplies_Object = MibTableColumn
interfaceRxArpReplies = _InterfaceRxArpReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 36),
    _InterfaceRxArpReplies_Type()
)
interfaceRxArpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxArpReplies.setStatus("current")
_InterfaceArpAddFails_Type = Counter64
_InterfaceArpAddFails_Object = MibTableColumn
interfaceArpAddFails = _InterfaceArpAddFails_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 37),
    _InterfaceArpAddFails_Type()
)
interfaceArpAddFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceArpAddFails.setStatus("current")
_InterfaceRxArpReplyDrops_Type = Counter64
_InterfaceRxArpReplyDrops_Object = MibTableColumn
interfaceRxArpReplyDrops = _InterfaceRxArpReplyDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 38),
    _InterfaceRxArpReplyDrops_Type()
)
interfaceRxArpReplyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxArpReplyDrops.setStatus("current")
_InterfaceRxArpRateLimitDrops_Type = Counter64
_InterfaceRxArpRateLimitDrops_Object = MibTableColumn
interfaceRxArpRateLimitDrops = _InterfaceRxArpRateLimitDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 39),
    _InterfaceRxArpRateLimitDrops_Type()
)
interfaceRxArpRateLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxArpRateLimitDrops.setStatus("current")
_InterfaceTxArpRateLimitDrops_Type = Counter64
_InterfaceTxArpRateLimitDrops_Object = MibTableColumn
interfaceTxArpRateLimitDrops = _InterfaceTxArpRateLimitDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 40),
    _InterfaceTxArpRateLimitDrops_Type()
)
interfaceTxArpRateLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxArpRateLimitDrops.setStatus("current")
_InterfaceRxArpNonLocalDrops_Type = Counter64
_InterfaceRxArpNonLocalDrops_Object = MibTableColumn
interfaceRxArpNonLocalDrops = _InterfaceRxArpNonLocalDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 41),
    _InterfaceRxArpNonLocalDrops_Type()
)
interfaceRxArpNonLocalDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxArpNonLocalDrops.setStatus("current")
_InterfaceTxArpRequestFail_Type = Counter64
_InterfaceTxArpRequestFail_Object = MibTableColumn
interfaceTxArpRequestFail = _InterfaceTxArpRequestFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 42),
    _InterfaceTxArpRequestFail_Type()
)
interfaceTxArpRequestFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxArpRequestFail.setStatus("current")
_InterfaceTxNoArpDrops_Type = Counter64
_InterfaceTxNoArpDrops_Object = MibTableColumn
interfaceTxNoArpDrops = _InterfaceTxNoArpDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 43),
    _InterfaceTxNoArpDrops_Type()
)
interfaceTxNoArpDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxNoArpDrops.setStatus("current")
_InterfaceRxIpTtlExpired_Type = Counter64
_InterfaceRxIpTtlExpired_Object = MibTableColumn
interfaceRxIpTtlExpired = _InterfaceRxIpTtlExpired_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 44),
    _InterfaceRxIpTtlExpired_Type()
)
interfaceRxIpTtlExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxIpTtlExpired.setStatus("current")
_InterfaceRxIpErrors_Type = Counter64
_InterfaceRxIpErrors_Object = MibTableColumn
interfaceRxIpErrors = _InterfaceRxIpErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 45),
    _InterfaceRxIpErrors_Type()
)
interfaceRxIpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxIpErrors.setStatus("current")
_InterfaceInterfaceDisabled_Type = Counter64
_InterfaceInterfaceDisabled_Object = MibTableColumn
interfaceInterfaceDisabled = _InterfaceInterfaceDisabled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 46),
    _InterfaceInterfaceDisabled_Type()
)
interfaceInterfaceDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceInterfaceDisabled.setStatus("current")
_InterfaceRxPolicerDrops_Type = Counter64
_InterfaceRxPolicerDrops_Object = MibTableColumn
interfaceRxPolicerDrops = _InterfaceRxPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 47),
    _InterfaceRxPolicerDrops_Type()
)
interfaceRxPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPolicerDrops.setStatus("current")
_InterfaceRxNonIpDrops_Type = Counter64
_InterfaceRxNonIpDrops_Object = MibTableColumn
interfaceRxNonIpDrops = _InterfaceRxNonIpDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 48),
    _InterfaceRxNonIpDrops_Type()
)
interfaceRxNonIpDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxNonIpDrops.setStatus("current")
_InterfaceFilterDrops_Type = Counter64
_InterfaceFilterDrops_Object = MibTableColumn
interfaceFilterDrops = _InterfaceFilterDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 49),
    _InterfaceFilterDrops_Type()
)
interfaceFilterDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFilterDrops.setStatus("current")
_InterfaceMirrorDrops_Type = Counter64
_InterfaceMirrorDrops_Object = MibTableColumn
interfaceMirrorDrops = _InterfaceMirrorDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 50),
    _InterfaceMirrorDrops_Type()
)
interfaceMirrorDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceMirrorDrops.setStatus("current")
_InterfaceCpuPolicerDrops_Type = Counter64
_InterfaceCpuPolicerDrops_Object = MibTableColumn
interfaceCpuPolicerDrops = _InterfaceCpuPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 51),
    _InterfaceCpuPolicerDrops_Type()
)
interfaceCpuPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceCpuPolicerDrops.setStatus("current")
_InterfaceTxIcmpPolicerDrops_Type = Counter64
_InterfaceTxIcmpPolicerDrops_Object = MibTableColumn
interfaceTxIcmpPolicerDrops = _InterfaceTxIcmpPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 52),
    _InterfaceTxIcmpPolicerDrops_Type()
)
interfaceTxIcmpPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxIcmpPolicerDrops.setStatus("current")
_InterfaceTxIcmpMirroredDrops_Type = Counter64
_InterfaceTxIcmpMirroredDrops_Object = MibTableColumn
interfaceTxIcmpMirroredDrops = _InterfaceTxIcmpMirroredDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 53),
    _InterfaceTxIcmpMirroredDrops_Type()
)
interfaceTxIcmpMirroredDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxIcmpMirroredDrops.setStatus("current")
_InterfaceSplitHorizonDrops_Type = Counter64
_InterfaceSplitHorizonDrops_Object = MibTableColumn
interfaceSplitHorizonDrops = _InterfaceSplitHorizonDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 54),
    _InterfaceSplitHorizonDrops_Type()
)
interfaceSplitHorizonDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceSplitHorizonDrops.setStatus("current")
_InterfaceRouteLookupFail_Type = Counter64
_InterfaceRouteLookupFail_Object = MibTableColumn
interfaceRouteLookupFail = _InterfaceRouteLookupFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 55),
    _InterfaceRouteLookupFail_Type()
)
interfaceRouteLookupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRouteLookupFail.setStatus("current")
_InterfaceBadLabel_Type = Counter64
_InterfaceBadLabel_Object = MibTableColumn
interfaceBadLabel = _InterfaceBadLabel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 56),
    _InterfaceBadLabel_Type()
)
interfaceBadLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceBadLabel.setStatus("current")
_InterfaceTxInterfaceDisabled_Type = Counter64
_InterfaceTxInterfaceDisabled_Object = MibTableColumn
interfaceTxInterfaceDisabled = _InterfaceTxInterfaceDisabled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 57),
    _InterfaceTxInterfaceDisabled_Type()
)
interfaceTxInterfaceDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxInterfaceDisabled.setStatus("current")
_InterfaceRxMulticastPkts_Type = Counter64
_InterfaceRxMulticastPkts_Object = MibTableColumn
interfaceRxMulticastPkts = _InterfaceRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 58),
    _InterfaceRxMulticastPkts_Type()
)
interfaceRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxMulticastPkts.setStatus("current")
_InterfaceRxBroadcastPkts_Type = Counter64
_InterfaceRxBroadcastPkts_Object = MibTableColumn
interfaceRxBroadcastPkts = _InterfaceRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 59),
    _InterfaceRxBroadcastPkts_Type()
)
interfaceRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxBroadcastPkts.setStatus("current")
_InterfaceTxMulticastPkts_Type = Counter64
_InterfaceTxMulticastPkts_Object = MibTableColumn
interfaceTxMulticastPkts = _InterfaceTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 60),
    _InterfaceTxMulticastPkts_Type()
)
interfaceTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxMulticastPkts.setStatus("current")
_InterfaceTxBroadcastPkts_Type = Counter64
_InterfaceTxBroadcastPkts_Object = MibTableColumn
interfaceTxBroadcastPkts = _InterfaceTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 61),
    _InterfaceTxBroadcastPkts_Type()
)
interfaceTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxBroadcastPkts.setStatus("current")
_InterfaceRxPausePkts_Type = Counter64
_InterfaceRxPausePkts_Object = MibTableColumn
interfaceRxPausePkts = _InterfaceRxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 62),
    _InterfaceRxPausePkts_Type()
)
interfaceRxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPausePkts.setStatus("current")
_InterfaceRxDmacFilterDrops_Type = Counter64
_InterfaceRxDmacFilterDrops_Object = MibTableColumn
interfaceRxDmacFilterDrops = _InterfaceRxDmacFilterDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 63),
    _InterfaceRxDmacFilterDrops_Type()
)
interfaceRxDmacFilterDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxDmacFilterDrops.setStatus("current")
_InterfaceRxWredDrops_Type = Counter64
_InterfaceRxWredDrops_Object = MibTableColumn
interfaceRxWredDrops = _InterfaceRxWredDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 64),
    _InterfaceRxWredDrops_Type()
)
interfaceRxWredDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxWredDrops.setStatus("current")
_InterfaceRxInterfaceNotFound_Type = Counter64
_InterfaceRxInterfaceNotFound_Object = MibTableColumn
interfaceRxInterfaceNotFound = _InterfaceRxInterfaceNotFound_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 65),
    _InterfaceRxInterfaceNotFound_Type()
)
interfaceRxInterfaceNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxInterfaceNotFound.setStatus("current")
_InterfaceRxInbErrors_Type = Counter64
_InterfaceRxInbErrors_Object = MibTableColumn
interfaceRxInbErrors = _InterfaceRxInbErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 66),
    _InterfaceRxInbErrors_Type()
)
interfaceRxInbErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxInbErrors.setStatus("current")
_InterfaceRxOversizeErrors_Type = Counter64
_InterfaceRxOversizeErrors_Object = MibTableColumn
interfaceRxOversizeErrors = _InterfaceRxOversizeErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 67),
    _InterfaceRxOversizeErrors_Type()
)
interfaceRxOversizeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxOversizeErrors.setStatus("current")
_InterfaceRxFcsAlignErrors_Type = Counter64
_InterfaceRxFcsAlignErrors_Object = MibTableColumn
interfaceRxFcsAlignErrors = _InterfaceRxFcsAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 68),
    _InterfaceRxFcsAlignErrors_Type()
)
interfaceRxFcsAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxFcsAlignErrors.setStatus("current")
_InterfaceRxUndersizeErrors_Type = Counter64
_InterfaceRxUndersizeErrors_Object = MibTableColumn
interfaceRxUndersizeErrors = _InterfaceRxUndersizeErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 69),
    _InterfaceRxUndersizeErrors_Type()
)
interfaceRxUndersizeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxUndersizeErrors.setStatus("current")
_InterfaceTxUnderflowPkts_Type = Counter64
_InterfaceTxUnderflowPkts_Object = MibTableColumn
interfaceTxUnderflowPkts = _InterfaceTxUnderflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 70),
    _InterfaceTxUnderflowPkts_Type()
)
interfaceTxUnderflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxUnderflowPkts.setStatus("current")
_InterfaceTxCollisionDrops_Type = Counter64
_InterfaceTxCollisionDrops_Object = MibTableColumn
interfaceTxCollisionDrops = _InterfaceTxCollisionDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 71),
    _InterfaceTxCollisionDrops_Type()
)
interfaceTxCollisionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxCollisionDrops.setStatus("current")
_InterfaceTxPausePkts_Type = Counter64
_InterfaceTxPausePkts_Object = MibTableColumn
interfaceTxPausePkts = _InterfaceTxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 72),
    _InterfaceTxPausePkts_Type()
)
interfaceTxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxPausePkts.setStatus("current")
_InterfaceTxFragmentsNeeded_Type = Counter64
_InterfaceTxFragmentsNeeded_Object = MibTableColumn
interfaceTxFragmentsNeeded = _InterfaceTxFragmentsNeeded_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 73),
    _InterfaceTxFragmentsNeeded_Type()
)
interfaceTxFragmentsNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxFragmentsNeeded.setStatus("current")
_InterfaceTxFragments_Type = Counter64
_InterfaceTxFragments_Object = MibTableColumn
interfaceTxFragments = _InterfaceTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 74),
    _InterfaceTxFragments_Type()
)
interfaceTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxFragments.setStatus("current")
_InterfaceTxFragmentDrops_Type = Counter64
_InterfaceTxFragmentDrops_Object = MibTableColumn
interfaceTxFragmentDrops = _InterfaceTxFragmentDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 75),
    _InterfaceTxFragmentDrops_Type()
)
interfaceTxFragmentDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxFragmentDrops.setStatus("current")
_InterfaceTxTailRedDrops_Type = Counter64
_InterfaceTxTailRedDrops_Object = MibTableColumn
interfaceTxTailRedDrops = _InterfaceTxTailRedDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 76),
    _InterfaceTxTailRedDrops_Type()
)
interfaceTxTailRedDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxTailRedDrops.setStatus("current")
_InterfaceLlqDrops_Type = Counter64
_InterfaceLlqDrops_Object = MibTableColumn
interfaceLlqDrops = _InterfaceLlqDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 77),
    _InterfaceLlqDrops_Type()
)
interfaceLlqDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceLlqDrops.setStatus("current")
_InterfaceRxPktSize64_Type = Counter64
_InterfaceRxPktSize64_Object = MibTableColumn
interfaceRxPktSize64 = _InterfaceRxPktSize64_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 78),
    _InterfaceRxPktSize64_Type()
)
interfaceRxPktSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPktSize64.setStatus("current")
_InterfaceRxPktSizeLt64_Type = Counter64
_InterfaceRxPktSizeLt64_Object = MibTableColumn
interfaceRxPktSizeLt64 = _InterfaceRxPktSizeLt64_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 79),
    _InterfaceRxPktSizeLt64_Type()
)
interfaceRxPktSizeLt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPktSizeLt64.setStatus("current")
_InterfaceRxPktSize65127_Type = Counter64
_InterfaceRxPktSize65127_Object = MibTableColumn
interfaceRxPktSize65127 = _InterfaceRxPktSize65127_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 80),
    _InterfaceRxPktSize65127_Type()
)
interfaceRxPktSize65127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPktSize65127.setStatus("current")
_InterfaceRxPktSize128255_Type = Counter64
_InterfaceRxPktSize128255_Object = MibTableColumn
interfaceRxPktSize128255 = _InterfaceRxPktSize128255_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 81),
    _InterfaceRxPktSize128255_Type()
)
interfaceRxPktSize128255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPktSize128255.setStatus("current")
_InterfaceRxPktSize256511_Type = Counter64
_InterfaceRxPktSize256511_Object = MibTableColumn
interfaceRxPktSize256511 = _InterfaceRxPktSize256511_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 82),
    _InterfaceRxPktSize256511_Type()
)
interfaceRxPktSize256511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPktSize256511.setStatus("current")
_InterfaceRxPktSize5121023_Type = Counter64
_InterfaceRxPktSize5121023_Object = MibTableColumn
interfaceRxPktSize5121023 = _InterfaceRxPktSize5121023_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 83),
    _InterfaceRxPktSize5121023_Type()
)
interfaceRxPktSize5121023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPktSize5121023.setStatus("current")
_InterfaceRxPktSize10241518_Type = Counter64
_InterfaceRxPktSize10241518_Object = MibTableColumn
interfaceRxPktSize10241518 = _InterfaceRxPktSize10241518_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 84),
    _InterfaceRxPktSize10241518_Type()
)
interfaceRxPktSize10241518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPktSize10241518.setStatus("current")
_InterfaceRxPktSizeGt1518_Type = Counter64
_InterfaceRxPktSizeGt1518_Object = MibTableColumn
interfaceRxPktSizeGt1518 = _InterfaceRxPktSizeGt1518_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 85),
    _InterfaceRxPktSizeGt1518_Type()
)
interfaceRxPktSizeGt1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPktSizeGt1518.setStatus("current")
_InterfaceTxPktSize64_Type = Counter64
_InterfaceTxPktSize64_Object = MibTableColumn
interfaceTxPktSize64 = _InterfaceTxPktSize64_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 86),
    _InterfaceTxPktSize64_Type()
)
interfaceTxPktSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxPktSize64.setStatus("current")
_InterfaceTxPktSizeLt64_Type = Counter64
_InterfaceTxPktSizeLt64_Object = MibTableColumn
interfaceTxPktSizeLt64 = _InterfaceTxPktSizeLt64_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 87),
    _InterfaceTxPktSizeLt64_Type()
)
interfaceTxPktSizeLt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxPktSizeLt64.setStatus("current")
_InterfaceTxPktSize65127_Type = Counter64
_InterfaceTxPktSize65127_Object = MibTableColumn
interfaceTxPktSize65127 = _InterfaceTxPktSize65127_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 88),
    _InterfaceTxPktSize65127_Type()
)
interfaceTxPktSize65127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxPktSize65127.setStatus("current")
_InterfaceTxPktSize128255_Type = Counter64
_InterfaceTxPktSize128255_Object = MibTableColumn
interfaceTxPktSize128255 = _InterfaceTxPktSize128255_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 89),
    _InterfaceTxPktSize128255_Type()
)
interfaceTxPktSize128255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxPktSize128255.setStatus("current")
_InterfaceTxPktSize256511_Type = Counter64
_InterfaceTxPktSize256511_Object = MibTableColumn
interfaceTxPktSize256511 = _InterfaceTxPktSize256511_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 90),
    _InterfaceTxPktSize256511_Type()
)
interfaceTxPktSize256511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxPktSize256511.setStatus("current")
_InterfaceTxPktSize5121023_Type = Counter64
_InterfaceTxPktSize5121023_Object = MibTableColumn
interfaceTxPktSize5121023 = _InterfaceTxPktSize5121023_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 91),
    _InterfaceTxPktSize5121023_Type()
)
interfaceTxPktSize5121023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxPktSize5121023.setStatus("current")
_InterfaceTxPktSize10241518_Type = Counter64
_InterfaceTxPktSize10241518_Object = MibTableColumn
interfaceTxPktSize10241518 = _InterfaceTxPktSize10241518_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 92),
    _InterfaceTxPktSize10241518_Type()
)
interfaceTxPktSize10241518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxPktSize10241518.setStatus("current")
_InterfaceTxPktSizeGt1518_Type = Counter64
_InterfaceTxPktSizeGt1518_Object = MibTableColumn
interfaceTxPktSizeGt1518 = _InterfaceTxPktSizeGt1518_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 93),
    _InterfaceTxPktSizeGt1518_Type()
)
interfaceTxPktSizeGt1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTxPktSizeGt1518.setStatus("current")
_InterfaceNumFlaps_Type = Unsigned32
_InterfaceNumFlaps_Object = MibTableColumn
interfaceNumFlaps = _InterfaceNumFlaps_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 94),
    _InterfaceNumFlaps_Type()
)
interfaceNumFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceNumFlaps.setStatus("current")


class _InterfacePppoeEnabledInterface_Type(String):
    """Custom type interfacePppoeEnabledInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_InterfacePppoeEnabledInterface_Type.__name__ = "String"
_InterfacePppoeEnabledInterface_Object = MibTableColumn
interfacePppoeEnabledInterface = _InterfacePppoeEnabledInterface_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 95),
    _InterfacePppoeEnabledInterface_Type()
)
interfacePppoeEnabledInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfacePppoeEnabledInterface.setStatus("current")
_InterfacePppoeTxPkts_Type = Counter64
_InterfacePppoeTxPkts_Object = MibTableColumn
interfacePppoeTxPkts = _InterfacePppoeTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 96),
    _InterfacePppoeTxPkts_Type()
)
interfacePppoeTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfacePppoeTxPkts.setStatus("current")
_InterfacePppoeRxPkts_Type = Counter64
_InterfacePppoeRxPkts_Object = MibTableColumn
interfacePppoeRxPkts = _InterfacePppoeRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 97),
    _InterfacePppoeRxPkts_Type()
)
interfacePppoeRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfacePppoeRxPkts.setStatus("current")
_InterfaceBandwidthUpstream_Type = Unsigned32
_InterfaceBandwidthUpstream_Object = MibTableColumn
interfaceBandwidthUpstream = _InterfaceBandwidthUpstream_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 98),
    _InterfaceBandwidthUpstream_Type()
)
interfaceBandwidthUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceBandwidthUpstream.setStatus("current")
_InterfaceBandwidthDownstream_Type = Unsigned32
_InterfaceBandwidthDownstream_Object = MibTableColumn
interfaceBandwidthDownstream = _InterfaceBandwidthDownstream_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 99),
    _InterfaceBandwidthDownstream_Type()
)
interfaceBandwidthDownstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceBandwidthDownstream.setStatus("current")


class _InterfaceAfType_Type(Integer32):
    """Custom type interfaceAfType based on Integer32"""
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


_InterfaceAfType_Type.__name__ = "Integer32"
_InterfaceAfType_Object = MibTableColumn
interfaceAfType = _InterfaceAfType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 100),
    _InterfaceAfType_Type()
)
interfaceAfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceAfType.setStatus("current")
_InterfaceLinkLocalAddress_Type = String
_InterfaceLinkLocalAddress_Object = MibTableColumn
interfaceLinkLocalAddress = _InterfaceLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 101),
    _InterfaceLinkLocalAddress_Type()
)
interfaceLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceLinkLocalAddress.setStatus("current")
_InterfaceShapingRate_Type = Counter64
_InterfaceShapingRate_Object = MibTableColumn
interfaceShapingRate = _InterfaceShapingRate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 102),
    _InterfaceShapingRate_Type()
)
interfaceShapingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceShapingRate.setStatus("current")
_InterfaceDot1xTxPkts_Type = Counter64
_InterfaceDot1xTxPkts_Object = MibTableColumn
interfaceDot1xTxPkts = _InterfaceDot1xTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 103),
    _InterfaceDot1xTxPkts_Type()
)
interfaceDot1xTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceDot1xTxPkts.setStatus("current")
_InterfaceDot1xRxPkts_Type = Counter64
_InterfaceDot1xRxPkts_Object = MibTableColumn
interfaceDot1xRxPkts = _InterfaceDot1xRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 104),
    _InterfaceDot1xRxPkts_Type()
)
interfaceDot1xRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceDot1xRxPkts.setStatus("current")
_InterfaceRxPolicerRemark_Type = Counter64
_InterfaceRxPolicerRemark_Object = MibTableColumn
interfaceRxPolicerRemark = _InterfaceRxPolicerRemark_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 105),
    _InterfaceRxPolicerRemark_Type()
)
interfaceRxPolicerRemark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceRxPolicerRemark.setStatus("current")


class _InterfaceIfTrackerStatus_Type(String):
    """Custom type interfaceIfTrackerStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_InterfaceIfTrackerStatus_Type.__name__ = "String"
_InterfaceIfTrackerStatus_Object = MibTableColumn
interfaceIfTrackerStatus = _InterfaceIfTrackerStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 106),
    _InterfaceIfTrackerStatus_Type()
)
interfaceIfTrackerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIfTrackerStatus.setStatus("current")
_InterfaceAddrType_Type = IfAddressTypeEnum
_InterfaceAddrType_Object = MibTableColumn
interfaceAddrType = _InterfaceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 107),
    _InterfaceAddrType_Type()
)
interfaceAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceAddrType.setStatus("current")
_InterfaceIcmpRedirectTxDrops_Type = Counter64
_InterfaceIcmpRedirectTxDrops_Object = MibTableColumn
interfaceIcmpRedirectTxDrops = _InterfaceIcmpRedirectTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 108),
    _InterfaceIcmpRedirectTxDrops_Type()
)
interfaceIcmpRedirectTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIcmpRedirectTxDrops.setStatus("current")
_InterfaceIcmpRedirectRxDrops_Type = Counter64
_InterfaceIcmpRedirectRxDrops_Object = MibTableColumn
interfaceIcmpRedirectRxDrops = _InterfaceIcmpRedirectRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 109),
    _InterfaceIcmpRedirectRxDrops_Type()
)
interfaceIcmpRedirectRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIcmpRedirectRxDrops.setStatus("current")
_InterfaceDevicePolicyDrops_Type = Counter64
_InterfaceDevicePolicyDrops_Object = MibTableColumn
interfaceDevicePolicyDrops = _InterfaceDevicePolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 2, 1, 110),
    _InterfaceDevicePolicyDrops_Type()
)
interfaceDevicePolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceDevicePolicyDrops.setStatus("current")
_Nd6Table_Object = MibTable
nd6Table = _Nd6Table_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 3)
)
if mibBuilder.loadTexts:
    nd6Table.setStatus("current")
_Nd6Entry_Object = MibTableRow
nd6Entry = _Nd6Entry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 3, 1)
)
nd6Entry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "nd6VpnId"),
    (0, "VIPTELA-OPER-VPN", "nd6IfName"),
    (0, "VIPTELA-OPER-VPN", "nd6Ip"),
)
if mibBuilder.loadTexts:
    nd6Entry.setStatus("current")


class _Nd6VpnId_Type(Unsigned32):
    """Custom type nd6VpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_Nd6VpnId_Type.__name__ = "Unsigned32"
_Nd6VpnId_Object = MibTableColumn
nd6VpnId = _Nd6VpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 3, 1, 1),
    _Nd6VpnId_Type()
)
nd6VpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nd6VpnId.setStatus("current")


class _Nd6IfName_Type(String):
    """Custom type nd6IfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Nd6IfName_Type.__name__ = "String"
_Nd6IfName_Object = MibTableColumn
nd6IfName = _Nd6IfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 3, 1, 2),
    _Nd6IfName_Type()
)
nd6IfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nd6IfName.setStatus("current")
_Nd6Ip_Type = InetAddressIP
_Nd6Ip_Object = MibTableColumn
nd6Ip = _Nd6Ip_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 3, 1, 3),
    _Nd6Ip_Type()
)
nd6Ip.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nd6Ip.setStatus("current")
_Nd6Mac_Type = String
_Nd6Mac_Object = MibTableColumn
nd6Mac = _Nd6Mac_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 3, 1, 4),
    _Nd6Mac_Type()
)
nd6Mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nd6Mac.setStatus("current")


class _Nd6State_Type(Integer32):
    """Custom type nd6State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1),
          ("invalid", 2))
    )


_Nd6State_Type.__name__ = "Integer32"
_Nd6State_Object = MibTableColumn
nd6State = _Nd6State_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 3, 1, 5),
    _Nd6State_Type()
)
nd6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nd6State.setStatus("current")
_Nd6IdleTimer_Type = String
_Nd6IdleTimer_Object = MibTableColumn
nd6IdleTimer = _Nd6IdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 3, 1, 6),
    _Nd6IdleTimer_Type()
)
nd6IdleTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nd6IdleTimer.setStatus("current")
_Nd6Uptime_Type = String
_Nd6Uptime_Object = MibTableColumn
nd6Uptime = _Nd6Uptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 3, 1, 7),
    _Nd6Uptime_Type()
)
nd6Uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nd6Uptime.setStatus("current")
_InterfaceIfAddrTable_Object = MibTable
interfaceIfAddrTable = _InterfaceIfAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 4)
)
if mibBuilder.loadTexts:
    interfaceIfAddrTable.setStatus("current")
_InterfaceIfAddrEntry_Object = MibTableRow
interfaceIfAddrEntry = _InterfaceIfAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 4, 1)
)
interfaceIfAddrEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "interfaceVpnId"),
    (0, "VIPTELA-OPER-VPN", "interfaceIfname"),
    (0, "VIPTELA-OPER-VPN", "interfaceAfType"),
    (0, "VIPTELA-OPER-VPN", "interfaceIfAddrAddrId"),
)
if mibBuilder.loadTexts:
    interfaceIfAddrEntry.setStatus("current")
_InterfaceIfAddrAddrId_Type = Unsigned32
_InterfaceIfAddrAddrId_Object = MibTableColumn
interfaceIfAddrAddrId = _InterfaceIfAddrAddrId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 4, 1, 1),
    _InterfaceIfAddrAddrId_Type()
)
interfaceIfAddrAddrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceIfAddrAddrId.setStatus("current")


class _InterfaceIfAddrIpAddress_Type(String):
    """Custom type interfaceIfAddrIpAddress based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_InterfaceIfAddrIpAddress_Type.__name__ = "String"
_InterfaceIfAddrIpAddress_Object = MibTableColumn
interfaceIfAddrIpAddress = _InterfaceIfAddrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 4, 1, 2),
    _InterfaceIfAddrIpAddress_Type()
)
interfaceIfAddrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIfAddrIpAddress.setStatus("current")
_InterfaceIfAddrBroadcastAddr_Type = IpAddress
_InterfaceIfAddrBroadcastAddr_Object = MibTableColumn
interfaceIfAddrBroadcastAddr = _InterfaceIfAddrBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 4, 1, 3),
    _InterfaceIfAddrBroadcastAddr_Type()
)
interfaceIfAddrBroadcastAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceIfAddrBroadcastAddr.setStatus("current")
_InterfaceIfAddrSecondary_Type = TruthValue
_InterfaceIfAddrSecondary_Object = MibTableColumn
interfaceIfAddrSecondary = _InterfaceIfAddrSecondary_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 4, 1, 4),
    _InterfaceIfAddrSecondary_Type()
)
interfaceIfAddrSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIfAddrSecondary.setStatus("current")
_InterfaceQueueTable_Object = MibTable
interfaceQueueTable = _InterfaceQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5)
)
if mibBuilder.loadTexts:
    interfaceQueueTable.setStatus("current")
_InterfaceQueueEntry_Object = MibTableRow
interfaceQueueEntry = _InterfaceQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5, 1)
)
interfaceQueueEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "interfaceVpnId"),
    (0, "VIPTELA-OPER-VPN", "interfaceIfname"),
    (0, "VIPTELA-OPER-VPN", "interfaceAfType"),
    (0, "VIPTELA-OPER-VPN", "interfaceQueueQnum"),
)
if mibBuilder.loadTexts:
    interfaceQueueEntry.setStatus("current")


class _InterfaceQueueQnum_Type(UnsignedByte):
    """Custom type interfaceQueueQnum based on UnsignedByte"""
    subtypeSpec = UnsignedByte.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_InterfaceQueueQnum_Type.__name__ = "UnsignedByte"
_InterfaceQueueQnum_Object = MibTableColumn
interfaceQueueQnum = _InterfaceQueueQnum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5, 1, 1),
    _InterfaceQueueQnum_Type()
)
interfaceQueueQnum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceQueueQnum.setStatus("current")
_InterfaceQueueQueuedPackets_Type = Counter64
_InterfaceQueueQueuedPackets_Object = MibTableColumn
interfaceQueueQueuedPackets = _InterfaceQueueQueuedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5, 1, 2),
    _InterfaceQueueQueuedPackets_Type()
)
interfaceQueueQueuedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceQueueQueuedPackets.setStatus("current")
_InterfaceQueueQueuedBytes_Type = Counter64
_InterfaceQueueQueuedBytes_Object = MibTableColumn
interfaceQueueQueuedBytes = _InterfaceQueueQueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5, 1, 3),
    _InterfaceQueueQueuedBytes_Type()
)
interfaceQueueQueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceQueueQueuedBytes.setStatus("current")
_InterfaceQueueTailDropPackets_Type = Counter64
_InterfaceQueueTailDropPackets_Object = MibTableColumn
interfaceQueueTailDropPackets = _InterfaceQueueTailDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5, 1, 4),
    _InterfaceQueueTailDropPackets_Type()
)
interfaceQueueTailDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceQueueTailDropPackets.setStatus("current")
_InterfaceQueueTailDropBytes_Type = Counter64
_InterfaceQueueTailDropBytes_Object = MibTableColumn
interfaceQueueTailDropBytes = _InterfaceQueueTailDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5, 1, 5),
    _InterfaceQueueTailDropBytes_Type()
)
interfaceQueueTailDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceQueueTailDropBytes.setStatus("current")
_InterfaceQueueRedDropPackets_Type = Counter64
_InterfaceQueueRedDropPackets_Object = MibTableColumn
interfaceQueueRedDropPackets = _InterfaceQueueRedDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5, 1, 6),
    _InterfaceQueueRedDropPackets_Type()
)
interfaceQueueRedDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceQueueRedDropPackets.setStatus("current")
_InterfaceQueueRedDropBytes_Type = Counter64
_InterfaceQueueRedDropBytes_Object = MibTableColumn
interfaceQueueRedDropBytes = _InterfaceQueueRedDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5, 1, 7),
    _InterfaceQueueRedDropBytes_Type()
)
interfaceQueueRedDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceQueueRedDropBytes.setStatus("current")
_InterfaceQueueTxPackets_Type = Counter64
_InterfaceQueueTxPackets_Object = MibTableColumn
interfaceQueueTxPackets = _InterfaceQueueTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5, 1, 8),
    _InterfaceQueueTxPackets_Type()
)
interfaceQueueTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceQueueTxPackets.setStatus("current")
_InterfaceQueueTxBytes_Type = Counter64
_InterfaceQueueTxBytes_Object = MibTableColumn
interfaceQueueTxBytes = _InterfaceQueueTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5, 1, 9),
    _InterfaceQueueTxBytes_Type()
)
interfaceQueueTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceQueueTxBytes.setStatus("current")
_InterfaceQueueQueueDepth_Type = Counter64
_InterfaceQueueQueueDepth_Object = MibTableColumn
interfaceQueueQueueDepth = _InterfaceQueueQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5, 1, 10),
    _InterfaceQueueQueueDepth_Type()
)
interfaceQueueQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceQueueQueueDepth.setStatus("current")
_InterfaceQueueMaxDepth_Type = Counter64
_InterfaceQueueMaxDepth_Object = MibTableColumn
interfaceQueueMaxDepth = _InterfaceQueueMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5, 1, 11),
    _InterfaceQueueMaxDepth_Type()
)
interfaceQueueMaxDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceQueueMaxDepth.setStatus("current")
_InterfaceQueueAvgQueue_Type = Counter64
_InterfaceQueueAvgQueue_Object = MibTableColumn
interfaceQueueAvgQueue = _InterfaceQueueAvgQueue_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5, 1, 12),
    _InterfaceQueueAvgQueue_Type()
)
interfaceQueueAvgQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceQueueAvgQueue.setStatus("current")
_InterfaceQueueQueuePps_Type = Counter64
_InterfaceQueueQueuePps_Object = MibTableColumn
interfaceQueueQueuePps = _InterfaceQueueQueuePps_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5, 1, 13),
    _InterfaceQueueQueuePps_Type()
)
interfaceQueueQueuePps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceQueueQueuePps.setStatus("current")
_InterfaceQueueQueueDropPps_Type = Counter64
_InterfaceQueueQueueDropPps_Object = MibTableColumn
interfaceQueueQueueDropPps = _InterfaceQueueQueueDropPps_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 5, 1, 14),
    _InterfaceQueueQueueDropPps_Type()
)
interfaceQueueQueueDropPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceQueueQueueDropPps.setStatus("current")
_App_ObjectIdentity = ObjectIdentity
app = _App_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6)
)
_AppCflowd_ObjectIdentity = ObjectIdentity
appCflowd = _AppCflowd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1)
)
_AppCflowdFlowsTable_Object = MibTable
appCflowdFlowsTable = _AppCflowdFlowsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1)
)
if mibBuilder.loadTexts:
    appCflowdFlowsTable.setStatus("current")
_AppCflowdFlowsEntry_Object = MibTableRow
appCflowdFlowsEntry = _AppCflowdFlowsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1)
)
appCflowdFlowsEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "appCflowdFlowsVpnId"),
    (0, "VIPTELA-OPER-VPN", "appCflowdFlowsSrcIp"),
    (0, "VIPTELA-OPER-VPN", "appCflowdFlowsDestIp"),
    (0, "VIPTELA-OPER-VPN", "appCflowdFlowsSrcPort"),
    (0, "VIPTELA-OPER-VPN", "appCflowdFlowsDestPort"),
    (0, "VIPTELA-OPER-VPN", "appCflowdFlowsDscp"),
    (0, "VIPTELA-OPER-VPN", "appCflowdFlowsIpProto"),
)
if mibBuilder.loadTexts:
    appCflowdFlowsEntry.setStatus("current")


class _AppCflowdFlowsVpnId_Type(Unsigned32):
    """Custom type appCflowdFlowsVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_AppCflowdFlowsVpnId_Type.__name__ = "Unsigned32"
_AppCflowdFlowsVpnId_Object = MibTableColumn
appCflowdFlowsVpnId = _AppCflowdFlowsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 1),
    _AppCflowdFlowsVpnId_Type()
)
appCflowdFlowsVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appCflowdFlowsVpnId.setStatus("current")
_AppCflowdFlowsSrcIp_Type = InetAddressIP
_AppCflowdFlowsSrcIp_Object = MibTableColumn
appCflowdFlowsSrcIp = _AppCflowdFlowsSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 2),
    _AppCflowdFlowsSrcIp_Type()
)
appCflowdFlowsSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appCflowdFlowsSrcIp.setStatus("current")
_AppCflowdFlowsDestIp_Type = InetAddressIP
_AppCflowdFlowsDestIp_Object = MibTableColumn
appCflowdFlowsDestIp = _AppCflowdFlowsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 3),
    _AppCflowdFlowsDestIp_Type()
)
appCflowdFlowsDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appCflowdFlowsDestIp.setStatus("current")
_AppCflowdFlowsSrcPort_Type = UnsignedShort
_AppCflowdFlowsSrcPort_Object = MibTableColumn
appCflowdFlowsSrcPort = _AppCflowdFlowsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 4),
    _AppCflowdFlowsSrcPort_Type()
)
appCflowdFlowsSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appCflowdFlowsSrcPort.setStatus("current")
_AppCflowdFlowsDestPort_Type = UnsignedShort
_AppCflowdFlowsDestPort_Object = MibTableColumn
appCflowdFlowsDestPort = _AppCflowdFlowsDestPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 5),
    _AppCflowdFlowsDestPort_Type()
)
appCflowdFlowsDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appCflowdFlowsDestPort.setStatus("current")
_AppCflowdFlowsDscp_Type = UnsignedByte
_AppCflowdFlowsDscp_Object = MibTableColumn
appCflowdFlowsDscp = _AppCflowdFlowsDscp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 6),
    _AppCflowdFlowsDscp_Type()
)
appCflowdFlowsDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appCflowdFlowsDscp.setStatus("current")
_AppCflowdFlowsIpProto_Type = UnsignedByte
_AppCflowdFlowsIpProto_Object = MibTableColumn
appCflowdFlowsIpProto = _AppCflowdFlowsIpProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 7),
    _AppCflowdFlowsIpProto_Type()
)
appCflowdFlowsIpProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appCflowdFlowsIpProto.setStatus("current")
_AppCflowdFlowsTcpCntrlBits_Type = UnsignedByte
_AppCflowdFlowsTcpCntrlBits_Object = MibTableColumn
appCflowdFlowsTcpCntrlBits = _AppCflowdFlowsTcpCntrlBits_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 8),
    _AppCflowdFlowsTcpCntrlBits_Type()
)
appCflowdFlowsTcpCntrlBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdFlowsTcpCntrlBits.setStatus("current")
_AppCflowdFlowsIcmpOpcode_Type = UnsignedShort
_AppCflowdFlowsIcmpOpcode_Object = MibTableColumn
appCflowdFlowsIcmpOpcode = _AppCflowdFlowsIcmpOpcode_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 9),
    _AppCflowdFlowsIcmpOpcode_Type()
)
appCflowdFlowsIcmpOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdFlowsIcmpOpcode.setStatus("current")
_AppCflowdFlowsNhopIp_Type = InetAddressIP
_AppCflowdFlowsNhopIp_Object = MibTableColumn
appCflowdFlowsNhopIp = _AppCflowdFlowsNhopIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 10),
    _AppCflowdFlowsNhopIp_Type()
)
appCflowdFlowsNhopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdFlowsNhopIp.setStatus("current")
_AppCflowdFlowsEgressIntf_Type = Unsigned32
_AppCflowdFlowsEgressIntf_Object = MibTableColumn
appCflowdFlowsEgressIntf = _AppCflowdFlowsEgressIntf_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 11),
    _AppCflowdFlowsEgressIntf_Type()
)
appCflowdFlowsEgressIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdFlowsEgressIntf.setStatus("deprecated")
_AppCflowdFlowsIngressIntf_Type = Unsigned32
_AppCflowdFlowsIngressIntf_Object = MibTableColumn
appCflowdFlowsIngressIntf = _AppCflowdFlowsIngressIntf_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 12),
    _AppCflowdFlowsIngressIntf_Type()
)
appCflowdFlowsIngressIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdFlowsIngressIntf.setStatus("deprecated")
_AppCflowdFlowsTotalPkts_Type = Counter64
_AppCflowdFlowsTotalPkts_Object = MibTableColumn
appCflowdFlowsTotalPkts = _AppCflowdFlowsTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 13),
    _AppCflowdFlowsTotalPkts_Type()
)
appCflowdFlowsTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdFlowsTotalPkts.setStatus("current")
_AppCflowdFlowsTotalBytes_Type = Counter64
_AppCflowdFlowsTotalBytes_Object = MibTableColumn
appCflowdFlowsTotalBytes = _AppCflowdFlowsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 14),
    _AppCflowdFlowsTotalBytes_Type()
)
appCflowdFlowsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdFlowsTotalBytes.setStatus("current")
_AppCflowdFlowsMinLen_Type = UnsignedShort
_AppCflowdFlowsMinLen_Object = MibTableColumn
appCflowdFlowsMinLen = _AppCflowdFlowsMinLen_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 15),
    _AppCflowdFlowsMinLen_Type()
)
appCflowdFlowsMinLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdFlowsMinLen.setStatus("current")
_AppCflowdFlowsMaxLen_Type = UnsignedShort
_AppCflowdFlowsMaxLen_Object = MibTableColumn
appCflowdFlowsMaxLen = _AppCflowdFlowsMaxLen_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 16),
    _AppCflowdFlowsMaxLen_Type()
)
appCflowdFlowsMaxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdFlowsMaxLen.setStatus("current")
_AppCflowdFlowsStartTime_Type = String
_AppCflowdFlowsStartTime_Object = MibTableColumn
appCflowdFlowsStartTime = _AppCflowdFlowsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 17),
    _AppCflowdFlowsStartTime_Type()
)
appCflowdFlowsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdFlowsStartTime.setStatus("current")
_AppCflowdFlowsTimeToExpire_Type = Unsigned32
_AppCflowdFlowsTimeToExpire_Object = MibTableColumn
appCflowdFlowsTimeToExpire = _AppCflowdFlowsTimeToExpire_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 18),
    _AppCflowdFlowsTimeToExpire_Type()
)
appCflowdFlowsTimeToExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdFlowsTimeToExpire.setStatus("current")


class _AppCflowdFlowsEgressIntfName_Type(String):
    """Custom type appCflowdFlowsEgressIntfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppCflowdFlowsEgressIntfName_Type.__name__ = "String"
_AppCflowdFlowsEgressIntfName_Object = MibTableColumn
appCflowdFlowsEgressIntfName = _AppCflowdFlowsEgressIntfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 19),
    _AppCflowdFlowsEgressIntfName_Type()
)
appCflowdFlowsEgressIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdFlowsEgressIntfName.setStatus("current")


class _AppCflowdFlowsIngressIntfName_Type(String):
    """Custom type appCflowdFlowsIngressIntfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppCflowdFlowsIngressIntfName_Type.__name__ = "String"
_AppCflowdFlowsIngressIntfName_Object = MibTableColumn
appCflowdFlowsIngressIntfName = _AppCflowdFlowsIngressIntfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 20),
    _AppCflowdFlowsIngressIntfName_Type()
)
appCflowdFlowsIngressIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdFlowsIngressIntfName.setStatus("current")
_AppCflowdFlowsAppID_Type = Unsigned32
_AppCflowdFlowsAppID_Object = MibTableColumn
appCflowdFlowsAppID = _AppCflowdFlowsAppID_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 1, 1, 21),
    _AppCflowdFlowsAppID_Type()
)
appCflowdFlowsAppID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdFlowsAppID.setStatus("current")
_AppCflowdCollectorTable_Object = MibTable
appCflowdCollectorTable = _AppCflowdCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 2)
)
if mibBuilder.loadTexts:
    appCflowdCollectorTable.setStatus("current")
_AppCflowdCollectorEntry_Object = MibTableRow
appCflowdCollectorEntry = _AppCflowdCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 2, 1)
)
appCflowdCollectorEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "appCflowdCollectorVpnId"),
    (0, "VIPTELA-OPER-VPN", "appCflowdCollectorIpAddress"),
    (0, "VIPTELA-OPER-VPN", "appCflowdCollectorPort"),
    (0, "VIPTELA-OPER-VPN", "appCflowdCollectorProto"),
)
if mibBuilder.loadTexts:
    appCflowdCollectorEntry.setStatus("current")


class _AppCflowdCollectorVpnId_Type(Unsigned32):
    """Custom type appCflowdCollectorVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_AppCflowdCollectorVpnId_Type.__name__ = "Unsigned32"
_AppCflowdCollectorVpnId_Object = MibTableColumn
appCflowdCollectorVpnId = _AppCflowdCollectorVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 2, 1, 1),
    _AppCflowdCollectorVpnId_Type()
)
appCflowdCollectorVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appCflowdCollectorVpnId.setStatus("current")
_AppCflowdCollectorIpAddress_Type = InetAddressIP
_AppCflowdCollectorIpAddress_Object = MibTableColumn
appCflowdCollectorIpAddress = _AppCflowdCollectorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 2, 1, 2),
    _AppCflowdCollectorIpAddress_Type()
)
appCflowdCollectorIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appCflowdCollectorIpAddress.setStatus("current")
_AppCflowdCollectorPort_Type = UnsignedShort
_AppCflowdCollectorPort_Object = MibTableColumn
appCflowdCollectorPort = _AppCflowdCollectorPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 2, 1, 3),
    _AppCflowdCollectorPort_Type()
)
appCflowdCollectorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appCflowdCollectorPort.setStatus("current")


class _AppCflowdCollectorProto_Type(Integer32):
    """Custom type appCflowdCollectorProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("tcp", 6),
          ("udp", 17))
    )


_AppCflowdCollectorProto_Type.__name__ = "Integer32"
_AppCflowdCollectorProto_Object = MibTableColumn
appCflowdCollectorProto = _AppCflowdCollectorProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 2, 1, 4),
    _AppCflowdCollectorProto_Type()
)
appCflowdCollectorProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appCflowdCollectorProto.setStatus("current")
_AppCflowdCollectorConnectionUp_Type = TruthValue
_AppCflowdCollectorConnectionUp_Object = MibTableColumn
appCflowdCollectorConnectionUp = _AppCflowdCollectorConnectionUp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 2, 1, 5),
    _AppCflowdCollectorConnectionUp_Type()
)
appCflowdCollectorConnectionUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdCollectorConnectionUp.setStatus("current")
_AppCflowdCollectorIpfix_Type = UnsignedByte
_AppCflowdCollectorIpfix_Object = MibTableColumn
appCflowdCollectorIpfix = _AppCflowdCollectorIpfix_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 2, 1, 6),
    _AppCflowdCollectorIpfix_Type()
)
appCflowdCollectorIpfix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdCollectorIpfix.setStatus("current")
_AppCflowdCollectorConnectionRetry_Type = UnsignedShort
_AppCflowdCollectorConnectionRetry_Object = MibTableColumn
appCflowdCollectorConnectionRetry = _AppCflowdCollectorConnectionRetry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 2, 1, 7),
    _AppCflowdCollectorConnectionRetry_Type()
)
appCflowdCollectorConnectionRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdCollectorConnectionRetry.setStatus("current")
_AppCflowdCollectorTemplatePackets_Type = Counter64
_AppCflowdCollectorTemplatePackets_Object = MibTableColumn
appCflowdCollectorTemplatePackets = _AppCflowdCollectorTemplatePackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 2, 1, 8),
    _AppCflowdCollectorTemplatePackets_Type()
)
appCflowdCollectorTemplatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdCollectorTemplatePackets.setStatus("current")
_AppCflowdCollectorDataPackets_Type = Counter64
_AppCflowdCollectorDataPackets_Object = MibTableColumn
appCflowdCollectorDataPackets = _AppCflowdCollectorDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 2, 1, 9),
    _AppCflowdCollectorDataPackets_Type()
)
appCflowdCollectorDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdCollectorDataPackets.setStatus("current")
_AppCflowdCollectorDroppedPackets_Type = Counter64
_AppCflowdCollectorDroppedPackets_Object = MibTableColumn
appCflowdCollectorDroppedPackets = _AppCflowdCollectorDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 2, 1, 10),
    _AppCflowdCollectorDroppedPackets_Type()
)
appCflowdCollectorDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdCollectorDroppedPackets.setStatus("current")


class _AppCflowdCollectorSourceInterface_Type(String):
    """Custom type appCflowdCollectorSourceInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppCflowdCollectorSourceInterface_Type.__name__ = "String"
_AppCflowdCollectorSourceInterface_Object = MibTableColumn
appCflowdCollectorSourceInterface = _AppCflowdCollectorSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 2, 1, 11),
    _AppCflowdCollectorSourceInterface_Type()
)
appCflowdCollectorSourceInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdCollectorSourceInterface.setStatus("current")
_AppCflowdStatistics_ObjectIdentity = ObjectIdentity
appCflowdStatistics = _AppCflowdStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 3)
)
_AppCflowdStatisticsDataPackets_Type = Counter64
_AppCflowdStatisticsDataPackets_Object = MibScalar
appCflowdStatisticsDataPackets = _AppCflowdStatisticsDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 3, 1),
    _AppCflowdStatisticsDataPackets_Type()
)
appCflowdStatisticsDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdStatisticsDataPackets.setStatus("current")
_AppCflowdStatisticsTemplatePackets_Type = Counter64
_AppCflowdStatisticsTemplatePackets_Object = MibScalar
appCflowdStatisticsTemplatePackets = _AppCflowdStatisticsTemplatePackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 3, 2),
    _AppCflowdStatisticsTemplatePackets_Type()
)
appCflowdStatisticsTemplatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdStatisticsTemplatePackets.setStatus("current")
_AppCflowdStatisticsTotalPackets_Type = Counter64
_AppCflowdStatisticsTotalPackets_Object = MibScalar
appCflowdStatisticsTotalPackets = _AppCflowdStatisticsTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 3, 3),
    _AppCflowdStatisticsTotalPackets_Type()
)
appCflowdStatisticsTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdStatisticsTotalPackets.setStatus("current")
_AppCflowdStatisticsFlowRefresh_Type = Counter64
_AppCflowdStatisticsFlowRefresh_Object = MibScalar
appCflowdStatisticsFlowRefresh = _AppCflowdStatisticsFlowRefresh_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 3, 4),
    _AppCflowdStatisticsFlowRefresh_Type()
)
appCflowdStatisticsFlowRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdStatisticsFlowRefresh.setStatus("current")
_AppCflowdStatisticsFlowAgeout_Type = Counter64
_AppCflowdStatisticsFlowAgeout_Object = MibScalar
appCflowdStatisticsFlowAgeout = _AppCflowdStatisticsFlowAgeout_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 3, 5),
    _AppCflowdStatisticsFlowAgeout_Type()
)
appCflowdStatisticsFlowAgeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdStatisticsFlowAgeout.setStatus("current")
_AppCflowdStatisticsFlowEndDetected_Type = Counter64
_AppCflowdStatisticsFlowEndDetected_Object = MibScalar
appCflowdStatisticsFlowEndDetected = _AppCflowdStatisticsFlowEndDetected_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 3, 6),
    _AppCflowdStatisticsFlowEndDetected_Type()
)
appCflowdStatisticsFlowEndDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdStatisticsFlowEndDetected.setStatus("current")
_AppCflowdStatisticsFlowEndForced_Type = Counter64
_AppCflowdStatisticsFlowEndForced_Object = MibScalar
appCflowdStatisticsFlowEndForced = _AppCflowdStatisticsFlowEndForced_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 3, 7),
    _AppCflowdStatisticsFlowEndForced_Type()
)
appCflowdStatisticsFlowEndForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdStatisticsFlowEndForced.setStatus("current")
_AppCflowdTemplate_ObjectIdentity = ObjectIdentity
appCflowdTemplate = _AppCflowdTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 4)
)
_AppCflowdTemplateName_Type = String
_AppCflowdTemplateName_Object = MibScalar
appCflowdTemplateName = _AppCflowdTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 4, 1),
    _AppCflowdTemplateName_Type()
)
appCflowdTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdTemplateName.setStatus("current")
_AppCflowdTemplateFlowActiveTimeout_Type = Unsigned32
_AppCflowdTemplateFlowActiveTimeout_Object = MibScalar
appCflowdTemplateFlowActiveTimeout = _AppCflowdTemplateFlowActiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 4, 2),
    _AppCflowdTemplateFlowActiveTimeout_Type()
)
appCflowdTemplateFlowActiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdTemplateFlowActiveTimeout.setStatus("current")
_AppCflowdTemplateFlowInactiveTimeout_Type = Unsigned32
_AppCflowdTemplateFlowInactiveTimeout_Object = MibScalar
appCflowdTemplateFlowInactiveTimeout = _AppCflowdTemplateFlowInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 4, 3),
    _AppCflowdTemplateFlowInactiveTimeout_Type()
)
appCflowdTemplateFlowInactiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdTemplateFlowInactiveTimeout.setStatus("current")
_AppCflowdTemplateTemplateRefresh_Type = Unsigned32
_AppCflowdTemplateTemplateRefresh_Object = MibScalar
appCflowdTemplateTemplateRefresh = _AppCflowdTemplateTemplateRefresh_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 4, 4),
    _AppCflowdTemplateTemplateRefresh_Type()
)
appCflowdTemplateTemplateRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdTemplateTemplateRefresh.setStatus("current")
_AppCflowdFlowCountTable_Object = MibTable
appCflowdFlowCountTable = _AppCflowdFlowCountTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 5)
)
if mibBuilder.loadTexts:
    appCflowdFlowCountTable.setStatus("current")
_AppCflowdFlowCountEntry_Object = MibTableRow
appCflowdFlowCountEntry = _AppCflowdFlowCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 5, 1)
)
appCflowdFlowCountEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "appCflowdFlowCountVpnId"),
)
if mibBuilder.loadTexts:
    appCflowdFlowCountEntry.setStatus("current")


class _AppCflowdFlowCountVpnId_Type(Unsigned32):
    """Custom type appCflowdFlowCountVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_AppCflowdFlowCountVpnId_Type.__name__ = "Unsigned32"
_AppCflowdFlowCountVpnId_Object = MibTableColumn
appCflowdFlowCountVpnId = _AppCflowdFlowCountVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 5, 1, 1),
    _AppCflowdFlowCountVpnId_Type()
)
appCflowdFlowCountVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appCflowdFlowCountVpnId.setStatus("current")
_AppCflowdFlowCountCount_Type = Unsigned32
_AppCflowdFlowCountCount_Object = MibTableColumn
appCflowdFlowCountCount = _AppCflowdFlowCountCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 1, 5, 1, 2),
    _AppCflowdFlowCountCount_Type()
)
appCflowdFlowCountCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appCflowdFlowCountCount.setStatus("current")
_AppDpi_ObjectIdentity = ObjectIdentity
appDpi = _AppDpi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2)
)
_AppDpiApplicationsTable_Object = MibTable
appDpiApplicationsTable = _AppDpiApplicationsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 1)
)
if mibBuilder.loadTexts:
    appDpiApplicationsTable.setStatus("current")
_AppDpiApplicationsEntry_Object = MibTableRow
appDpiApplicationsEntry = _AppDpiApplicationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 1, 1)
)
appDpiApplicationsEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "appDpiApplicationsVpnId"),
    (1, "VIPTELA-OPER-VPN", "appDpiApplicationsApplication"),
)
if mibBuilder.loadTexts:
    appDpiApplicationsEntry.setStatus("current")


class _AppDpiApplicationsVpnId_Type(Unsigned32):
    """Custom type appDpiApplicationsVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_AppDpiApplicationsVpnId_Type.__name__ = "Unsigned32"
_AppDpiApplicationsVpnId_Object = MibTableColumn
appDpiApplicationsVpnId = _AppDpiApplicationsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 1, 1, 1),
    _AppDpiApplicationsVpnId_Type()
)
appDpiApplicationsVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appDpiApplicationsVpnId.setStatus("current")
_AppDpiApplicationsSrcIp_Type = InetAddressIP
_AppDpiApplicationsSrcIp_Object = MibTableColumn
appDpiApplicationsSrcIp = _AppDpiApplicationsSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 1, 1, 2),
    _AppDpiApplicationsSrcIp_Type()
)
appDpiApplicationsSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appDpiApplicationsSrcIp.setStatus("deprecated")


class _AppDpiApplicationsApplication_Type(String):
    """Custom type appDpiApplicationsApplication based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AppDpiApplicationsApplication_Type.__name__ = "String"
_AppDpiApplicationsApplication_Object = MibTableColumn
appDpiApplicationsApplication = _AppDpiApplicationsApplication_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 1, 1, 3),
    _AppDpiApplicationsApplication_Type()
)
appDpiApplicationsApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appDpiApplicationsApplication.setStatus("current")
_AppDpiApplicationsFamily_Type = String
_AppDpiApplicationsFamily_Object = MibTableColumn
appDpiApplicationsFamily = _AppDpiApplicationsFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 1, 1, 4),
    _AppDpiApplicationsFamily_Type()
)
appDpiApplicationsFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiApplicationsFamily.setStatus("current")
_AppDpiApplicationsTotalFlows_Type = Unsigned32
_AppDpiApplicationsTotalFlows_Object = MibTableColumn
appDpiApplicationsTotalFlows = _AppDpiApplicationsTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 1, 1, 5),
    _AppDpiApplicationsTotalFlows_Type()
)
appDpiApplicationsTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiApplicationsTotalFlows.setStatus("deprecated")
_AppDpiApplicationsExpiredFlows_Type = Unsigned32
_AppDpiApplicationsExpiredFlows_Object = MibTableColumn
appDpiApplicationsExpiredFlows = _AppDpiApplicationsExpiredFlows_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 1, 1, 6),
    _AppDpiApplicationsExpiredFlows_Type()
)
appDpiApplicationsExpiredFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiApplicationsExpiredFlows.setStatus("current")
_AppDpiApplicationsLastSeen_Type = DateAndTime
_AppDpiApplicationsLastSeen_Object = MibTableColumn
appDpiApplicationsLastSeen = _AppDpiApplicationsLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 1, 1, 7),
    _AppDpiApplicationsLastSeen_Type()
)
appDpiApplicationsLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiApplicationsLastSeen.setStatus("current")
_AppDpiApplicationsPackets_Type = Unsigned32
_AppDpiApplicationsPackets_Object = MibTableColumn
appDpiApplicationsPackets = _AppDpiApplicationsPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 1, 1, 8),
    _AppDpiApplicationsPackets_Type()
)
appDpiApplicationsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiApplicationsPackets.setStatus("current")
_AppDpiApplicationsOctets_Type = Counter64
_AppDpiApplicationsOctets_Object = MibTableColumn
appDpiApplicationsOctets = _AppDpiApplicationsOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 1, 1, 9),
    _AppDpiApplicationsOctets_Type()
)
appDpiApplicationsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiApplicationsOctets.setStatus("current")
_AppDpiFlowsTable_Object = MibTable
appDpiFlowsTable = _AppDpiFlowsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 2)
)
if mibBuilder.loadTexts:
    appDpiFlowsTable.setStatus("current")
_AppDpiFlowsEntry_Object = MibTableRow
appDpiFlowsEntry = _AppDpiFlowsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 2, 1)
)
appDpiFlowsEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsVpnId"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsSrcIp"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsDstIp"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsSrcPort"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsDstPort"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsProto"),
)
if mibBuilder.loadTexts:
    appDpiFlowsEntry.setStatus("current")


class _AppDpiFlowsVpnId_Type(Unsigned32):
    """Custom type appDpiFlowsVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_AppDpiFlowsVpnId_Type.__name__ = "Unsigned32"
_AppDpiFlowsVpnId_Object = MibTableColumn
appDpiFlowsVpnId = _AppDpiFlowsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 2, 1, 1),
    _AppDpiFlowsVpnId_Type()
)
appDpiFlowsVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appDpiFlowsVpnId.setStatus("current")
_AppDpiFlowsSrcIp_Type = InetAddressIP
_AppDpiFlowsSrcIp_Object = MibTableColumn
appDpiFlowsSrcIp = _AppDpiFlowsSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 2, 1, 2),
    _AppDpiFlowsSrcIp_Type()
)
appDpiFlowsSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appDpiFlowsSrcIp.setStatus("current")
_AppDpiFlowsDstIp_Type = InetAddressIP
_AppDpiFlowsDstIp_Object = MibTableColumn
appDpiFlowsDstIp = _AppDpiFlowsDstIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 2, 1, 3),
    _AppDpiFlowsDstIp_Type()
)
appDpiFlowsDstIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appDpiFlowsDstIp.setStatus("current")
_AppDpiFlowsSrcPort_Type = UnsignedShort
_AppDpiFlowsSrcPort_Object = MibTableColumn
appDpiFlowsSrcPort = _AppDpiFlowsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 2, 1, 4),
    _AppDpiFlowsSrcPort_Type()
)
appDpiFlowsSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appDpiFlowsSrcPort.setStatus("current")
_AppDpiFlowsDstPort_Type = UnsignedShort
_AppDpiFlowsDstPort_Object = MibTableColumn
appDpiFlowsDstPort = _AppDpiFlowsDstPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 2, 1, 5),
    _AppDpiFlowsDstPort_Type()
)
appDpiFlowsDstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appDpiFlowsDstPort.setStatus("current")


class _AppDpiFlowsProto_Type(Integer32):
    """Custom type appDpiFlowsProto based on Integer32"""
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
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hopopt", 0),
          ("icmp", 1),
          ("igmp", 2),
          ("ggp", 3),
          ("ipv4", 4),
          ("st", 5),
          ("tcp", 6),
          ("cbt", 7),
          ("egp", 8),
          ("igp", 9),
          ("bbn-rcc-mon", 10),
          ("nvp-ii", 11),
          ("pup", 12),
          ("argus", 13),
          ("emcon", 14),
          ("xnet", 15),
          ("chaos", 16),
          ("udp", 17),
          ("mux", 18),
          ("dcn-meas", 19),
          ("hmp", 20),
          ("prm", 21),
          ("xns-idp", 22),
          ("trunk-1", 23),
          ("trunk-2", 24),
          ("leaf-1", 25),
          ("leaf-2", 26),
          ("rdp", 27),
          ("irtp", 28),
          ("iso-tp4", 29),
          ("netblt", 30),
          ("mfe-nsp", 31),
          ("merit-inp", 32),
          ("dccp", 33),
          ("a3pc", 34),
          ("idpr", 35),
          ("xtp", 36),
          ("ddp", 37),
          ("idpr-cmtp", 38),
          ("tp", 39),
          ("il", 40),
          ("ipv6", 41),
          ("sdrp", 42),
          ("ipv6-route", 43),
          ("ipv6-frag", 44),
          ("idrp", 45),
          ("rsvp", 46),
          ("gre", 47),
          ("dsr", 48),
          ("bna", 49),
          ("esp", 50),
          ("ah", 51),
          ("i-nlsp", 52),
          ("swipe", 53),
          ("narp", 54),
          ("mobile", 55),
          ("tlsp", 56),
          ("skip", 57),
          ("ipv6-icmp", 58),
          ("ipv6-nonxt", 59),
          ("ipv6-opts", 60),
          ("any-host", 61),
          ("cftp", 62),
          ("any-local", 63),
          ("sat-expak", 64),
          ("kryptolan", 65),
          ("rvd", 66),
          ("ippc", 67),
          ("dist-fs", 68),
          ("sat-mon", 69),
          ("visa", 70),
          ("ipcv", 71),
          ("cpnx", 72),
          ("cphb", 73),
          ("wsn", 74),
          ("pvp", 75),
          ("br-sat-mon", 76),
          ("sun-nd", 77),
          ("wb-mon", 78),
          ("wb-expak", 79),
          ("iso-ip", 80),
          ("vmtp", 81),
          ("secure-vmtp", 82),
          ("vines", 83),
          ("ttp", 84),
          ("nsfnet-igp", 85),
          ("dgp", 86),
          ("tcf", 87),
          ("eigrp", 88),
          ("ospf", 89),
          ("sprite-rpc", 90),
          ("larp", 91),
          ("mtp", 92),
          ("ax-25", 93),
          ("ipip", 94),
          ("micp", 95),
          ("scc-sp", 96),
          ("etherip", 97),
          ("encap", 98),
          ("priv-encypt", 99),
          ("gmtp", 100),
          ("ifmp", 101),
          ("pnni", 102),
          ("pim", 103),
          ("aris", 104),
          ("scps", 105),
          ("qnx", 106),
          ("a-n", 107),
          ("ipcomp", 108),
          ("snp", 109),
          ("compaq-peer", 110),
          ("ipx-in-ip", 111),
          ("vrrp", 112),
          ("pgm", 113),
          ("any-0-hop", 114),
          ("l2tp", 115),
          ("ddx", 116),
          ("iatp", 117),
          ("stp", 118),
          ("srp", 119),
          ("uti", 120),
          ("smp", 121),
          ("sm", 122),
          ("ptp", 123),
          ("isis-o-ipv4", 124),
          ("fire", 125),
          ("crtp", 126),
          ("crudp", 127),
          ("sscopmce", 128),
          ("iplt", 129),
          ("sps", 130),
          ("pipe", 131),
          ("sctp", 132),
          ("fc", 133),
          ("rsvp-e2e-ignore", 134),
          ("mobility-header", 135),
          ("udplite", 136),
          ("mpls-in-ip", 137),
          ("manet", 138),
          ("hip", 139),
          ("shim6", 140),
          ("wesp", 141),
          ("rohc", 142),
          ("exp-1", 253),
          ("exp-2", 254),
          ("reserved", 255))
    )


_AppDpiFlowsProto_Type.__name__ = "Integer32"
_AppDpiFlowsProto_Object = MibTableColumn
appDpiFlowsProto = _AppDpiFlowsProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 2, 1, 6),
    _AppDpiFlowsProto_Type()
)
appDpiFlowsProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appDpiFlowsProto.setStatus("current")
_AppDpiFlowsApplication_Type = String
_AppDpiFlowsApplication_Object = MibTableColumn
appDpiFlowsApplication = _AppDpiFlowsApplication_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 2, 1, 7),
    _AppDpiFlowsApplication_Type()
)
appDpiFlowsApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsApplication.setStatus("current")
_AppDpiFlowsFamily_Type = String
_AppDpiFlowsFamily_Object = MibTableColumn
appDpiFlowsFamily = _AppDpiFlowsFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 2, 1, 8),
    _AppDpiFlowsFamily_Type()
)
appDpiFlowsFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsFamily.setStatus("current")
_AppDpiFlowsActiveSince_Type = DateAndTime
_AppDpiFlowsActiveSince_Object = MibTableColumn
appDpiFlowsActiveSince = _AppDpiFlowsActiveSince_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 2, 1, 9),
    _AppDpiFlowsActiveSince_Type()
)
appDpiFlowsActiveSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsActiveSince.setStatus("current")
_AppDpiFlowsPackets_Type = Unsigned32
_AppDpiFlowsPackets_Object = MibTableColumn
appDpiFlowsPackets = _AppDpiFlowsPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 2, 1, 10),
    _AppDpiFlowsPackets_Type()
)
appDpiFlowsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsPackets.setStatus("current")
_AppDpiFlowsOctets_Type = Counter64
_AppDpiFlowsOctets_Object = MibTableColumn
appDpiFlowsOctets = _AppDpiFlowsOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 2, 1, 11),
    _AppDpiFlowsOctets_Type()
)
appDpiFlowsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsOctets.setStatus("current")
_AppDpiSupportedApplicationsTable_Object = MibTable
appDpiSupportedApplicationsTable = _AppDpiSupportedApplicationsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 3)
)
if mibBuilder.loadTexts:
    appDpiSupportedApplicationsTable.setStatus("current")
_AppDpiSupportedApplicationsEntry_Object = MibTableRow
appDpiSupportedApplicationsEntry = _AppDpiSupportedApplicationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 3, 1)
)
appDpiSupportedApplicationsEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "appDpiSupportedApplicationsApplication"),
)
if mibBuilder.loadTexts:
    appDpiSupportedApplicationsEntry.setStatus("current")


class _AppDpiSupportedApplicationsApplication_Type(String):
    """Custom type appDpiSupportedApplicationsApplication based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AppDpiSupportedApplicationsApplication_Type.__name__ = "String"
_AppDpiSupportedApplicationsApplication_Object = MibTableColumn
appDpiSupportedApplicationsApplication = _AppDpiSupportedApplicationsApplication_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 3, 1, 1),
    _AppDpiSupportedApplicationsApplication_Type()
)
appDpiSupportedApplicationsApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiSupportedApplicationsApplication.setStatus("current")
_AppDpiSupportedApplicationsFamily_Type = String
_AppDpiSupportedApplicationsFamily_Object = MibTableColumn
appDpiSupportedApplicationsFamily = _AppDpiSupportedApplicationsFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 3, 1, 2),
    _AppDpiSupportedApplicationsFamily_Type()
)
appDpiSupportedApplicationsFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiSupportedApplicationsFamily.setStatus("current")
_AppDpiSupportedApplicationsAppLongName_Type = String
_AppDpiSupportedApplicationsAppLongName_Object = MibTableColumn
appDpiSupportedApplicationsAppLongName = _AppDpiSupportedApplicationsAppLongName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 3, 1, 3),
    _AppDpiSupportedApplicationsAppLongName_Type()
)
appDpiSupportedApplicationsAppLongName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiSupportedApplicationsAppLongName.setStatus("current")
_AppDpiSupportedApplicationsFamilyLongName_Type = String
_AppDpiSupportedApplicationsFamilyLongName_Object = MibTableColumn
appDpiSupportedApplicationsFamilyLongName = _AppDpiSupportedApplicationsFamilyLongName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 3, 1, 4),
    _AppDpiSupportedApplicationsFamilyLongName_Type()
)
appDpiSupportedApplicationsFamilyLongName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiSupportedApplicationsFamilyLongName.setStatus("current")
_AppDpiSupportedApplicationsAppId_Type = Unsigned32
_AppDpiSupportedApplicationsAppId_Object = MibTableColumn
appDpiSupportedApplicationsAppId = _AppDpiSupportedApplicationsAppId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 3, 1, 5),
    _AppDpiSupportedApplicationsAppId_Type()
)
appDpiSupportedApplicationsAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiSupportedApplicationsAppId.setStatus("current")
_AppDpiSummary_ObjectIdentity = ObjectIdentity
appDpiSummary = _AppDpiSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 4)
)


class _AppDpiSummaryStatus_Type(Integer32):
    """Custom type appDpiSummaryStatus based on Integer32"""
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


_AppDpiSummaryStatus_Type.__name__ = "Integer32"
_AppDpiSummaryStatus_Object = MibScalar
appDpiSummaryStatus = _AppDpiSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 4, 1),
    _AppDpiSummaryStatus_Type()
)
appDpiSummaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiSummaryStatus.setStatus("current")
_AppDpiSummaryFlowsCreated_Type = ConfdString
_AppDpiSummaryFlowsCreated_Object = MibScalar
appDpiSummaryFlowsCreated = _AppDpiSummaryFlowsCreated_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 4, 2),
    _AppDpiSummaryFlowsCreated_Type()
)
appDpiSummaryFlowsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiSummaryFlowsCreated.setStatus("current")
_AppDpiSummaryFlowsExpired_Type = ConfdString
_AppDpiSummaryFlowsExpired_Object = MibScalar
appDpiSummaryFlowsExpired = _AppDpiSummaryFlowsExpired_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 4, 3),
    _AppDpiSummaryFlowsExpired_Type()
)
appDpiSummaryFlowsExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiSummaryFlowsExpired.setStatus("current")
_AppDpiSummaryCurrentFlows_Type = ConfdString
_AppDpiSummaryCurrentFlows_Object = MibScalar
appDpiSummaryCurrentFlows = _AppDpiSummaryCurrentFlows_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 4, 4),
    _AppDpiSummaryCurrentFlows_Type()
)
appDpiSummaryCurrentFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiSummaryCurrentFlows.setStatus("current")
_AppDpiSummaryPeakFlows_Type = ConfdString
_AppDpiSummaryPeakFlows_Object = MibScalar
appDpiSummaryPeakFlows = _AppDpiSummaryPeakFlows_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 4, 5),
    _AppDpiSummaryPeakFlows_Type()
)
appDpiSummaryPeakFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiSummaryPeakFlows.setStatus("current")
_AppDpiSummaryCurrentRate_Type = Unsigned32
_AppDpiSummaryCurrentRate_Object = MibScalar
appDpiSummaryCurrentRate = _AppDpiSummaryCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 4, 6),
    _AppDpiSummaryCurrentRate_Type()
)
appDpiSummaryCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiSummaryCurrentRate.setStatus("current")
_AppDpiSummaryPeakRate_Type = Unsigned32
_AppDpiSummaryPeakRate_Object = MibScalar
appDpiSummaryPeakRate = _AppDpiSummaryPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 4, 7),
    _AppDpiSummaryPeakRate_Type()
)
appDpiSummaryPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiSummaryPeakRate.setStatus("current")
_AppDpiFlowsTunnelsInTable_Object = MibTable
appDpiFlowsTunnelsInTable = _AppDpiFlowsTunnelsInTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 5)
)
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsInTable.setStatus("current")
_AppDpiFlowsTunnelsInEntry_Object = MibTableRow
appDpiFlowsTunnelsInEntry = _AppDpiFlowsTunnelsInEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 5, 1)
)
appDpiFlowsTunnelsInEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsVpnId"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsSrcIp"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsDstIp"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsSrcPort"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsDstPort"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsProto"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsTunnelsInIndex"),
)
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsInEntry.setStatus("current")
_AppDpiFlowsTunnelsInIndex_Type = Unsigned32
_AppDpiFlowsTunnelsInIndex_Object = MibTableColumn
appDpiFlowsTunnelsInIndex = _AppDpiFlowsTunnelsInIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 5, 1, 1),
    _AppDpiFlowsTunnelsInIndex_Type()
)
appDpiFlowsTunnelsInIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsInIndex.setStatus("current")
_AppDpiFlowsTunnelsInLocalTlocIp_Type = InetAddressIP
_AppDpiFlowsTunnelsInLocalTlocIp_Object = MibTableColumn
appDpiFlowsTunnelsInLocalTlocIp = _AppDpiFlowsTunnelsInLocalTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 5, 1, 2),
    _AppDpiFlowsTunnelsInLocalTlocIp_Type()
)
appDpiFlowsTunnelsInLocalTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsInLocalTlocIp.setStatus("current")


class _AppDpiFlowsTunnelsInLocalTlocColor_Type(Integer32):
    """Custom type appDpiFlowsTunnelsInLocalTlocColor based on Integer32"""
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


_AppDpiFlowsTunnelsInLocalTlocColor_Type.__name__ = "Integer32"
_AppDpiFlowsTunnelsInLocalTlocColor_Object = MibTableColumn
appDpiFlowsTunnelsInLocalTlocColor = _AppDpiFlowsTunnelsInLocalTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 5, 1, 3),
    _AppDpiFlowsTunnelsInLocalTlocColor_Type()
)
appDpiFlowsTunnelsInLocalTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsInLocalTlocColor.setStatus("current")


class _AppDpiFlowsTunnelsInLocalTlocEncap_Type(Integer32):
    """Custom type appDpiFlowsTunnelsInLocalTlocEncap based on Integer32"""
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


_AppDpiFlowsTunnelsInLocalTlocEncap_Type.__name__ = "Integer32"
_AppDpiFlowsTunnelsInLocalTlocEncap_Object = MibTableColumn
appDpiFlowsTunnelsInLocalTlocEncap = _AppDpiFlowsTunnelsInLocalTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 5, 1, 4),
    _AppDpiFlowsTunnelsInLocalTlocEncap_Type()
)
appDpiFlowsTunnelsInLocalTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsInLocalTlocEncap.setStatus("current")
_AppDpiFlowsTunnelsInRemoteTlocIp_Type = InetAddressIP
_AppDpiFlowsTunnelsInRemoteTlocIp_Object = MibTableColumn
appDpiFlowsTunnelsInRemoteTlocIp = _AppDpiFlowsTunnelsInRemoteTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 5, 1, 5),
    _AppDpiFlowsTunnelsInRemoteTlocIp_Type()
)
appDpiFlowsTunnelsInRemoteTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsInRemoteTlocIp.setStatus("current")


class _AppDpiFlowsTunnelsInRemoteTlocColor_Type(Integer32):
    """Custom type appDpiFlowsTunnelsInRemoteTlocColor based on Integer32"""
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


_AppDpiFlowsTunnelsInRemoteTlocColor_Type.__name__ = "Integer32"
_AppDpiFlowsTunnelsInRemoteTlocColor_Object = MibTableColumn
appDpiFlowsTunnelsInRemoteTlocColor = _AppDpiFlowsTunnelsInRemoteTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 5, 1, 6),
    _AppDpiFlowsTunnelsInRemoteTlocColor_Type()
)
appDpiFlowsTunnelsInRemoteTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsInRemoteTlocColor.setStatus("current")


class _AppDpiFlowsTunnelsInRemoteTlocEncap_Type(Integer32):
    """Custom type appDpiFlowsTunnelsInRemoteTlocEncap based on Integer32"""
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


_AppDpiFlowsTunnelsInRemoteTlocEncap_Type.__name__ = "Integer32"
_AppDpiFlowsTunnelsInRemoteTlocEncap_Object = MibTableColumn
appDpiFlowsTunnelsInRemoteTlocEncap = _AppDpiFlowsTunnelsInRemoteTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 5, 1, 7),
    _AppDpiFlowsTunnelsInRemoteTlocEncap_Type()
)
appDpiFlowsTunnelsInRemoteTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsInRemoteTlocEncap.setStatus("current")
_AppDpiFlowsTunnelsInPackets_Type = Unsigned32
_AppDpiFlowsTunnelsInPackets_Object = MibTableColumn
appDpiFlowsTunnelsInPackets = _AppDpiFlowsTunnelsInPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 5, 1, 8),
    _AppDpiFlowsTunnelsInPackets_Type()
)
appDpiFlowsTunnelsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsInPackets.setStatus("current")
_AppDpiFlowsTunnelsInOctets_Type = Counter64
_AppDpiFlowsTunnelsInOctets_Object = MibTableColumn
appDpiFlowsTunnelsInOctets = _AppDpiFlowsTunnelsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 5, 1, 9),
    _AppDpiFlowsTunnelsInOctets_Type()
)
appDpiFlowsTunnelsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsInOctets.setStatus("current")
_AppDpiFlowsTunnelsInStartTime_Type = DateAndTime
_AppDpiFlowsTunnelsInStartTime_Object = MibTableColumn
appDpiFlowsTunnelsInStartTime = _AppDpiFlowsTunnelsInStartTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 5, 1, 10),
    _AppDpiFlowsTunnelsInStartTime_Type()
)
appDpiFlowsTunnelsInStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsInStartTime.setStatus("current")
_AppDpiFlowsTunnelsOutTable_Object = MibTable
appDpiFlowsTunnelsOutTable = _AppDpiFlowsTunnelsOutTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 6)
)
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsOutTable.setStatus("current")
_AppDpiFlowsTunnelsOutEntry_Object = MibTableRow
appDpiFlowsTunnelsOutEntry = _AppDpiFlowsTunnelsOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 6, 1)
)
appDpiFlowsTunnelsOutEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsVpnId"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsSrcIp"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsDstIp"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsSrcPort"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsDstPort"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsProto"),
    (0, "VIPTELA-OPER-VPN", "appDpiFlowsTunnelsOutIndex"),
)
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsOutEntry.setStatus("current")
_AppDpiFlowsTunnelsOutIndex_Type = Unsigned32
_AppDpiFlowsTunnelsOutIndex_Object = MibTableColumn
appDpiFlowsTunnelsOutIndex = _AppDpiFlowsTunnelsOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 6, 1, 1),
    _AppDpiFlowsTunnelsOutIndex_Type()
)
appDpiFlowsTunnelsOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsOutIndex.setStatus("current")
_AppDpiFlowsTunnelsOutLocalTlocIp_Type = InetAddressIP
_AppDpiFlowsTunnelsOutLocalTlocIp_Object = MibTableColumn
appDpiFlowsTunnelsOutLocalTlocIp = _AppDpiFlowsTunnelsOutLocalTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 6, 1, 2),
    _AppDpiFlowsTunnelsOutLocalTlocIp_Type()
)
appDpiFlowsTunnelsOutLocalTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsOutLocalTlocIp.setStatus("current")


class _AppDpiFlowsTunnelsOutLocalTlocColor_Type(Integer32):
    """Custom type appDpiFlowsTunnelsOutLocalTlocColor based on Integer32"""
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


_AppDpiFlowsTunnelsOutLocalTlocColor_Type.__name__ = "Integer32"
_AppDpiFlowsTunnelsOutLocalTlocColor_Object = MibTableColumn
appDpiFlowsTunnelsOutLocalTlocColor = _AppDpiFlowsTunnelsOutLocalTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 6, 1, 3),
    _AppDpiFlowsTunnelsOutLocalTlocColor_Type()
)
appDpiFlowsTunnelsOutLocalTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsOutLocalTlocColor.setStatus("current")


class _AppDpiFlowsTunnelsOutLocalTlocEncap_Type(Integer32):
    """Custom type appDpiFlowsTunnelsOutLocalTlocEncap based on Integer32"""
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


_AppDpiFlowsTunnelsOutLocalTlocEncap_Type.__name__ = "Integer32"
_AppDpiFlowsTunnelsOutLocalTlocEncap_Object = MibTableColumn
appDpiFlowsTunnelsOutLocalTlocEncap = _AppDpiFlowsTunnelsOutLocalTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 6, 1, 4),
    _AppDpiFlowsTunnelsOutLocalTlocEncap_Type()
)
appDpiFlowsTunnelsOutLocalTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsOutLocalTlocEncap.setStatus("current")
_AppDpiFlowsTunnelsOutRemoteTlocIp_Type = InetAddressIP
_AppDpiFlowsTunnelsOutRemoteTlocIp_Object = MibTableColumn
appDpiFlowsTunnelsOutRemoteTlocIp = _AppDpiFlowsTunnelsOutRemoteTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 6, 1, 5),
    _AppDpiFlowsTunnelsOutRemoteTlocIp_Type()
)
appDpiFlowsTunnelsOutRemoteTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsOutRemoteTlocIp.setStatus("current")


class _AppDpiFlowsTunnelsOutRemoteTlocColor_Type(Integer32):
    """Custom type appDpiFlowsTunnelsOutRemoteTlocColor based on Integer32"""
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


_AppDpiFlowsTunnelsOutRemoteTlocColor_Type.__name__ = "Integer32"
_AppDpiFlowsTunnelsOutRemoteTlocColor_Object = MibTableColumn
appDpiFlowsTunnelsOutRemoteTlocColor = _AppDpiFlowsTunnelsOutRemoteTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 6, 1, 6),
    _AppDpiFlowsTunnelsOutRemoteTlocColor_Type()
)
appDpiFlowsTunnelsOutRemoteTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsOutRemoteTlocColor.setStatus("current")


class _AppDpiFlowsTunnelsOutRemoteTlocEncap_Type(Integer32):
    """Custom type appDpiFlowsTunnelsOutRemoteTlocEncap based on Integer32"""
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


_AppDpiFlowsTunnelsOutRemoteTlocEncap_Type.__name__ = "Integer32"
_AppDpiFlowsTunnelsOutRemoteTlocEncap_Object = MibTableColumn
appDpiFlowsTunnelsOutRemoteTlocEncap = _AppDpiFlowsTunnelsOutRemoteTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 6, 1, 7),
    _AppDpiFlowsTunnelsOutRemoteTlocEncap_Type()
)
appDpiFlowsTunnelsOutRemoteTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsOutRemoteTlocEncap.setStatus("current")
_AppDpiFlowsTunnelsOutPackets_Type = Unsigned32
_AppDpiFlowsTunnelsOutPackets_Object = MibTableColumn
appDpiFlowsTunnelsOutPackets = _AppDpiFlowsTunnelsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 6, 1, 8),
    _AppDpiFlowsTunnelsOutPackets_Type()
)
appDpiFlowsTunnelsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsOutPackets.setStatus("current")
_AppDpiFlowsTunnelsOutOctets_Type = Counter64
_AppDpiFlowsTunnelsOutOctets_Object = MibTableColumn
appDpiFlowsTunnelsOutOctets = _AppDpiFlowsTunnelsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 6, 1, 9),
    _AppDpiFlowsTunnelsOutOctets_Type()
)
appDpiFlowsTunnelsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsOutOctets.setStatus("current")
_AppDpiFlowsTunnelsOutStartTime_Type = DateAndTime
_AppDpiFlowsTunnelsOutStartTime_Object = MibTableColumn
appDpiFlowsTunnelsOutStartTime = _AppDpiFlowsTunnelsOutStartTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 2, 6, 1, 10),
    _AppDpiFlowsTunnelsOutStartTime_Type()
)
appDpiFlowsTunnelsOutStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDpiFlowsTunnelsOutStartTime.setStatus("current")
_AppLog_ObjectIdentity = ObjectIdentity
appLog = _AppLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3)
)
_AppLogFlowsTable_Object = MibTable
appLogFlowsTable = _AppLogFlowsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1)
)
if mibBuilder.loadTexts:
    appLogFlowsTable.setStatus("current")
_AppLogFlowsEntry_Object = MibTableRow
appLogFlowsEntry = _AppLogFlowsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1)
)
appLogFlowsEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "appLogFlowsVpnId"),
    (0, "VIPTELA-OPER-VPN", "appLogFlowsSrcIp"),
    (0, "VIPTELA-OPER-VPN", "appLogFlowsDestIp"),
    (0, "VIPTELA-OPER-VPN", "appLogFlowsSrcPort"),
    (0, "VIPTELA-OPER-VPN", "appLogFlowsDestPort"),
    (0, "VIPTELA-OPER-VPN", "appLogFlowsDscp"),
    (0, "VIPTELA-OPER-VPN", "appLogFlowsIpProto"),
)
if mibBuilder.loadTexts:
    appLogFlowsEntry.setStatus("current")


class _AppLogFlowsVpnId_Type(Unsigned32):
    """Custom type appLogFlowsVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_AppLogFlowsVpnId_Type.__name__ = "Unsigned32"
_AppLogFlowsVpnId_Object = MibTableColumn
appLogFlowsVpnId = _AppLogFlowsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 1),
    _AppLogFlowsVpnId_Type()
)
appLogFlowsVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appLogFlowsVpnId.setStatus("current")
_AppLogFlowsSrcIp_Type = InetAddressIP
_AppLogFlowsSrcIp_Object = MibTableColumn
appLogFlowsSrcIp = _AppLogFlowsSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 2),
    _AppLogFlowsSrcIp_Type()
)
appLogFlowsSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appLogFlowsSrcIp.setStatus("current")
_AppLogFlowsDestIp_Type = InetAddressIP
_AppLogFlowsDestIp_Object = MibTableColumn
appLogFlowsDestIp = _AppLogFlowsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 3),
    _AppLogFlowsDestIp_Type()
)
appLogFlowsDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appLogFlowsDestIp.setStatus("current")
_AppLogFlowsSrcPort_Type = UnsignedShort
_AppLogFlowsSrcPort_Object = MibTableColumn
appLogFlowsSrcPort = _AppLogFlowsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 4),
    _AppLogFlowsSrcPort_Type()
)
appLogFlowsSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appLogFlowsSrcPort.setStatus("current")
_AppLogFlowsDestPort_Type = UnsignedShort
_AppLogFlowsDestPort_Object = MibTableColumn
appLogFlowsDestPort = _AppLogFlowsDestPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 5),
    _AppLogFlowsDestPort_Type()
)
appLogFlowsDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appLogFlowsDestPort.setStatus("current")
_AppLogFlowsDscp_Type = UnsignedByte
_AppLogFlowsDscp_Object = MibTableColumn
appLogFlowsDscp = _AppLogFlowsDscp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 6),
    _AppLogFlowsDscp_Type()
)
appLogFlowsDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appLogFlowsDscp.setStatus("current")
_AppLogFlowsIpProto_Type = UnsignedByte
_AppLogFlowsIpProto_Object = MibTableColumn
appLogFlowsIpProto = _AppLogFlowsIpProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 7),
    _AppLogFlowsIpProto_Type()
)
appLogFlowsIpProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appLogFlowsIpProto.setStatus("current")
_AppLogFlowsTcpCntrlBits_Type = UnsignedByte
_AppLogFlowsTcpCntrlBits_Object = MibTableColumn
appLogFlowsTcpCntrlBits = _AppLogFlowsTcpCntrlBits_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 8),
    _AppLogFlowsTcpCntrlBits_Type()
)
appLogFlowsTcpCntrlBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLogFlowsTcpCntrlBits.setStatus("current")
_AppLogFlowsIcmpOpcode_Type = UnsignedShort
_AppLogFlowsIcmpOpcode_Object = MibTableColumn
appLogFlowsIcmpOpcode = _AppLogFlowsIcmpOpcode_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 9),
    _AppLogFlowsIcmpOpcode_Type()
)
appLogFlowsIcmpOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLogFlowsIcmpOpcode.setStatus("current")
_AppLogFlowsNhopIp_Type = InetAddressIP
_AppLogFlowsNhopIp_Object = MibTableColumn
appLogFlowsNhopIp = _AppLogFlowsNhopIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 10),
    _AppLogFlowsNhopIp_Type()
)
appLogFlowsNhopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLogFlowsNhopIp.setStatus("current")
_AppLogFlowsTotalPkts_Type = Counter64
_AppLogFlowsTotalPkts_Object = MibTableColumn
appLogFlowsTotalPkts = _AppLogFlowsTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 11),
    _AppLogFlowsTotalPkts_Type()
)
appLogFlowsTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLogFlowsTotalPkts.setStatus("current")
_AppLogFlowsTotalBytes_Type = Counter64
_AppLogFlowsTotalBytes_Object = MibTableColumn
appLogFlowsTotalBytes = _AppLogFlowsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 12),
    _AppLogFlowsTotalBytes_Type()
)
appLogFlowsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLogFlowsTotalBytes.setStatus("current")
_AppLogFlowsStartTime_Type = String
_AppLogFlowsStartTime_Object = MibTableColumn
appLogFlowsStartTime = _AppLogFlowsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 13),
    _AppLogFlowsStartTime_Type()
)
appLogFlowsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLogFlowsStartTime.setStatus("current")
_AppLogFlowsTimeToExpire_Type = Unsigned32
_AppLogFlowsTimeToExpire_Object = MibTableColumn
appLogFlowsTimeToExpire = _AppLogFlowsTimeToExpire_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 14),
    _AppLogFlowsTimeToExpire_Type()
)
appLogFlowsTimeToExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLogFlowsTimeToExpire.setStatus("current")


class _AppLogFlowsEgressIntfName_Type(String):
    """Custom type appLogFlowsEgressIntfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppLogFlowsEgressIntfName_Type.__name__ = "String"
_AppLogFlowsEgressIntfName_Object = MibTableColumn
appLogFlowsEgressIntfName = _AppLogFlowsEgressIntfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 15),
    _AppLogFlowsEgressIntfName_Type()
)
appLogFlowsEgressIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLogFlowsEgressIntfName.setStatus("current")


class _AppLogFlowsIngressIntfName_Type(String):
    """Custom type appLogFlowsIngressIntfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppLogFlowsIngressIntfName_Type.__name__ = "String"
_AppLogFlowsIngressIntfName_Object = MibTableColumn
appLogFlowsIngressIntfName = _AppLogFlowsIngressIntfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 16),
    _AppLogFlowsIngressIntfName_Type()
)
appLogFlowsIngressIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLogFlowsIngressIntfName.setStatus("current")


class _AppLogFlowsPolicyName_Type(String):
    """Custom type appLogFlowsPolicyName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppLogFlowsPolicyName_Type.__name__ = "String"
_AppLogFlowsPolicyName_Object = MibTableColumn
appLogFlowsPolicyName = _AppLogFlowsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 17),
    _AppLogFlowsPolicyName_Type()
)
appLogFlowsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLogFlowsPolicyName.setStatus("current")


class _AppLogFlowsPolicyAction_Type(String):
    """Custom type appLogFlowsPolicyAction based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppLogFlowsPolicyAction_Type.__name__ = "String"
_AppLogFlowsPolicyAction_Object = MibTableColumn
appLogFlowsPolicyAction = _AppLogFlowsPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 18),
    _AppLogFlowsPolicyAction_Type()
)
appLogFlowsPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLogFlowsPolicyAction.setStatus("current")


class _AppLogFlowsPolicyDirection_Type(String):
    """Custom type appLogFlowsPolicyDirection based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppLogFlowsPolicyDirection_Type.__name__ = "String"
_AppLogFlowsPolicyDirection_Object = MibTableColumn
appLogFlowsPolicyDirection = _AppLogFlowsPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 1, 1, 19),
    _AppLogFlowsPolicyDirection_Type()
)
appLogFlowsPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLogFlowsPolicyDirection.setStatus("current")
_AppLogFlowCountTable_Object = MibTable
appLogFlowCountTable = _AppLogFlowCountTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 2)
)
if mibBuilder.loadTexts:
    appLogFlowCountTable.setStatus("current")
_AppLogFlowCountEntry_Object = MibTableRow
appLogFlowCountEntry = _AppLogFlowCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 2, 1)
)
appLogFlowCountEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "appLogFlowCountVpnId"),
)
if mibBuilder.loadTexts:
    appLogFlowCountEntry.setStatus("current")


class _AppLogFlowCountVpnId_Type(Unsigned32):
    """Custom type appLogFlowCountVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_AppLogFlowCountVpnId_Type.__name__ = "Unsigned32"
_AppLogFlowCountVpnId_Object = MibTableColumn
appLogFlowCountVpnId = _AppLogFlowCountVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 2, 1, 1),
    _AppLogFlowCountVpnId_Type()
)
appLogFlowCountVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appLogFlowCountVpnId.setStatus("current")
_AppLogFlowCountCount_Type = Unsigned32
_AppLogFlowCountCount_Object = MibTableColumn
appLogFlowCountCount = _AppLogFlowCountCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 3, 2, 1, 2),
    _AppLogFlowCountCount_Type()
)
appLogFlowCountCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appLogFlowCountCount.setStatus("current")
_AppTcpOpt_ObjectIdentity = ObjectIdentity
appTcpOpt = _AppTcpOpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4)
)
_AppTcpOptActiveFlowsTable_Object = MibTable
appTcpOptActiveFlowsTable = _AppTcpOptActiveFlowsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 1)
)
if mibBuilder.loadTexts:
    appTcpOptActiveFlowsTable.setStatus("current")
_AppTcpOptActiveFlowsEntry_Object = MibTableRow
appTcpOptActiveFlowsEntry = _AppTcpOptActiveFlowsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 1, 1)
)
appTcpOptActiveFlowsEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "appTcpOptActiveFlowsVpnId"),
    (0, "VIPTELA-OPER-VPN", "appTcpOptActiveFlowsSrcIp"),
    (0, "VIPTELA-OPER-VPN", "appTcpOptActiveFlowsDestIp"),
    (0, "VIPTELA-OPER-VPN", "appTcpOptActiveFlowsSrcPort"),
    (0, "VIPTELA-OPER-VPN", "appTcpOptActiveFlowsDestPort"),
)
if mibBuilder.loadTexts:
    appTcpOptActiveFlowsEntry.setStatus("current")


class _AppTcpOptActiveFlowsVpnId_Type(Unsigned32):
    """Custom type appTcpOptActiveFlowsVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_AppTcpOptActiveFlowsVpnId_Type.__name__ = "Unsigned32"
_AppTcpOptActiveFlowsVpnId_Object = MibTableColumn
appTcpOptActiveFlowsVpnId = _AppTcpOptActiveFlowsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 1, 1, 1),
    _AppTcpOptActiveFlowsVpnId_Type()
)
appTcpOptActiveFlowsVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appTcpOptActiveFlowsVpnId.setStatus("current")
_AppTcpOptActiveFlowsSrcIp_Type = InetAddressIP
_AppTcpOptActiveFlowsSrcIp_Object = MibTableColumn
appTcpOptActiveFlowsSrcIp = _AppTcpOptActiveFlowsSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 1, 1, 2),
    _AppTcpOptActiveFlowsSrcIp_Type()
)
appTcpOptActiveFlowsSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appTcpOptActiveFlowsSrcIp.setStatus("current")
_AppTcpOptActiveFlowsDestIp_Type = InetAddressIP
_AppTcpOptActiveFlowsDestIp_Object = MibTableColumn
appTcpOptActiveFlowsDestIp = _AppTcpOptActiveFlowsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 1, 1, 3),
    _AppTcpOptActiveFlowsDestIp_Type()
)
appTcpOptActiveFlowsDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appTcpOptActiveFlowsDestIp.setStatus("current")
_AppTcpOptActiveFlowsSrcPort_Type = UnsignedShort
_AppTcpOptActiveFlowsSrcPort_Object = MibTableColumn
appTcpOptActiveFlowsSrcPort = _AppTcpOptActiveFlowsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 1, 1, 4),
    _AppTcpOptActiveFlowsSrcPort_Type()
)
appTcpOptActiveFlowsSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appTcpOptActiveFlowsSrcPort.setStatus("current")
_AppTcpOptActiveFlowsDestPort_Type = UnsignedShort
_AppTcpOptActiveFlowsDestPort_Object = MibTableColumn
appTcpOptActiveFlowsDestPort = _AppTcpOptActiveFlowsDestPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 1, 1, 5),
    _AppTcpOptActiveFlowsDestPort_Type()
)
appTcpOptActiveFlowsDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appTcpOptActiveFlowsDestPort.setStatus("current")


class _AppTcpOptActiveFlowsStartTime_Type(String):
    """Custom type appTcpOptActiveFlowsStartTime based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppTcpOptActiveFlowsStartTime_Type.__name__ = "String"
_AppTcpOptActiveFlowsStartTime_Object = MibTableColumn
appTcpOptActiveFlowsStartTime = _AppTcpOptActiveFlowsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 1, 1, 6),
    _AppTcpOptActiveFlowsStartTime_Type()
)
appTcpOptActiveFlowsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptActiveFlowsStartTime.setStatus("current")


class _AppTcpOptActiveFlowsEgressIntfName_Type(String):
    """Custom type appTcpOptActiveFlowsEgressIntfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppTcpOptActiveFlowsEgressIntfName_Type.__name__ = "String"
_AppTcpOptActiveFlowsEgressIntfName_Object = MibTableColumn
appTcpOptActiveFlowsEgressIntfName = _AppTcpOptActiveFlowsEgressIntfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 1, 1, 7),
    _AppTcpOptActiveFlowsEgressIntfName_Type()
)
appTcpOptActiveFlowsEgressIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptActiveFlowsEgressIntfName.setStatus("current")


class _AppTcpOptActiveFlowsIngressIntfName_Type(String):
    """Custom type appTcpOptActiveFlowsIngressIntfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppTcpOptActiveFlowsIngressIntfName_Type.__name__ = "String"
_AppTcpOptActiveFlowsIngressIntfName_Object = MibTableColumn
appTcpOptActiveFlowsIngressIntfName = _AppTcpOptActiveFlowsIngressIntfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 1, 1, 8),
    _AppTcpOptActiveFlowsIngressIntfName_Type()
)
appTcpOptActiveFlowsIngressIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptActiveFlowsIngressIntfName.setStatus("current")
_AppTcpOptActiveFlowsTxBytes_Type = Counter64
_AppTcpOptActiveFlowsTxBytes_Object = MibTableColumn
appTcpOptActiveFlowsTxBytes = _AppTcpOptActiveFlowsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 1, 1, 9),
    _AppTcpOptActiveFlowsTxBytes_Type()
)
appTcpOptActiveFlowsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptActiveFlowsTxBytes.setStatus("current")
_AppTcpOptActiveFlowsRxBytes_Type = Counter64
_AppTcpOptActiveFlowsRxBytes_Object = MibTableColumn
appTcpOptActiveFlowsRxBytes = _AppTcpOptActiveFlowsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 1, 1, 10),
    _AppTcpOptActiveFlowsRxBytes_Type()
)
appTcpOptActiveFlowsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptActiveFlowsRxBytes.setStatus("current")


class _AppTcpOptActiveFlowsTcpState_Type(String):
    """Custom type appTcpOptActiveFlowsTcpState based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppTcpOptActiveFlowsTcpState_Type.__name__ = "String"
_AppTcpOptActiveFlowsTcpState_Object = MibTableColumn
appTcpOptActiveFlowsTcpState = _AppTcpOptActiveFlowsTcpState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 1, 1, 11),
    _AppTcpOptActiveFlowsTcpState_Type()
)
appTcpOptActiveFlowsTcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptActiveFlowsTcpState.setStatus("current")


class _AppTcpOptActiveFlowsUnoptReason_Type(String):
    """Custom type appTcpOptActiveFlowsUnoptReason based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppTcpOptActiveFlowsUnoptReason_Type.__name__ = "String"
_AppTcpOptActiveFlowsUnoptReason_Object = MibTableColumn
appTcpOptActiveFlowsUnoptReason = _AppTcpOptActiveFlowsUnoptReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 1, 1, 12),
    _AppTcpOptActiveFlowsUnoptReason_Type()
)
appTcpOptActiveFlowsUnoptReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptActiveFlowsUnoptReason.setStatus("current")


class _AppTcpOptActiveFlowsProxyIdentity_Type(String):
    """Custom type appTcpOptActiveFlowsProxyIdentity based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppTcpOptActiveFlowsProxyIdentity_Type.__name__ = "String"
_AppTcpOptActiveFlowsProxyIdentity_Object = MibTableColumn
appTcpOptActiveFlowsProxyIdentity = _AppTcpOptActiveFlowsProxyIdentity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 1, 1, 13),
    _AppTcpOptActiveFlowsProxyIdentity_Type()
)
appTcpOptActiveFlowsProxyIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptActiveFlowsProxyIdentity.setStatus("current")
_AppTcpOptExpiredFlowsTable_Object = MibTable
appTcpOptExpiredFlowsTable = _AppTcpOptExpiredFlowsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2)
)
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsTable.setStatus("current")
_AppTcpOptExpiredFlowsEntry_Object = MibTableRow
appTcpOptExpiredFlowsEntry = _AppTcpOptExpiredFlowsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2, 1)
)
appTcpOptExpiredFlowsEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "appTcpOptExpiredFlowsTimestamp"),
    (0, "VIPTELA-OPER-VPN", "appTcpOptExpiredFlowsVpnId"),
    (0, "VIPTELA-OPER-VPN", "appTcpOptExpiredFlowsSrcIp"),
    (0, "VIPTELA-OPER-VPN", "appTcpOptExpiredFlowsDestIp"),
    (0, "VIPTELA-OPER-VPN", "appTcpOptExpiredFlowsSrcPort"),
    (0, "VIPTELA-OPER-VPN", "appTcpOptExpiredFlowsDestPort"),
)
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsEntry.setStatus("current")
_AppTcpOptExpiredFlowsTimestamp_Type = ConfdString
_AppTcpOptExpiredFlowsTimestamp_Object = MibTableColumn
appTcpOptExpiredFlowsTimestamp = _AppTcpOptExpiredFlowsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2, 1, 1),
    _AppTcpOptExpiredFlowsTimestamp_Type()
)
appTcpOptExpiredFlowsTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsTimestamp.setStatus("current")


class _AppTcpOptExpiredFlowsVpnId_Type(Unsigned32):
    """Custom type appTcpOptExpiredFlowsVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_AppTcpOptExpiredFlowsVpnId_Type.__name__ = "Unsigned32"
_AppTcpOptExpiredFlowsVpnId_Object = MibTableColumn
appTcpOptExpiredFlowsVpnId = _AppTcpOptExpiredFlowsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2, 1, 2),
    _AppTcpOptExpiredFlowsVpnId_Type()
)
appTcpOptExpiredFlowsVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsVpnId.setStatus("current")
_AppTcpOptExpiredFlowsSrcIp_Type = InetAddressIP
_AppTcpOptExpiredFlowsSrcIp_Object = MibTableColumn
appTcpOptExpiredFlowsSrcIp = _AppTcpOptExpiredFlowsSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2, 1, 3),
    _AppTcpOptExpiredFlowsSrcIp_Type()
)
appTcpOptExpiredFlowsSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsSrcIp.setStatus("current")
_AppTcpOptExpiredFlowsDestIp_Type = InetAddressIP
_AppTcpOptExpiredFlowsDestIp_Object = MibTableColumn
appTcpOptExpiredFlowsDestIp = _AppTcpOptExpiredFlowsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2, 1, 4),
    _AppTcpOptExpiredFlowsDestIp_Type()
)
appTcpOptExpiredFlowsDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsDestIp.setStatus("current")
_AppTcpOptExpiredFlowsSrcPort_Type = UnsignedShort
_AppTcpOptExpiredFlowsSrcPort_Object = MibTableColumn
appTcpOptExpiredFlowsSrcPort = _AppTcpOptExpiredFlowsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2, 1, 5),
    _AppTcpOptExpiredFlowsSrcPort_Type()
)
appTcpOptExpiredFlowsSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsSrcPort.setStatus("current")
_AppTcpOptExpiredFlowsDestPort_Type = UnsignedShort
_AppTcpOptExpiredFlowsDestPort_Object = MibTableColumn
appTcpOptExpiredFlowsDestPort = _AppTcpOptExpiredFlowsDestPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2, 1, 6),
    _AppTcpOptExpiredFlowsDestPort_Type()
)
appTcpOptExpiredFlowsDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsDestPort.setStatus("current")


class _AppTcpOptExpiredFlowsStartTime_Type(String):
    """Custom type appTcpOptExpiredFlowsStartTime based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppTcpOptExpiredFlowsStartTime_Type.__name__ = "String"
_AppTcpOptExpiredFlowsStartTime_Object = MibTableColumn
appTcpOptExpiredFlowsStartTime = _AppTcpOptExpiredFlowsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2, 1, 7),
    _AppTcpOptExpiredFlowsStartTime_Type()
)
appTcpOptExpiredFlowsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsStartTime.setStatus("current")


class _AppTcpOptExpiredFlowsEndTime_Type(String):
    """Custom type appTcpOptExpiredFlowsEndTime based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppTcpOptExpiredFlowsEndTime_Type.__name__ = "String"
_AppTcpOptExpiredFlowsEndTime_Object = MibTableColumn
appTcpOptExpiredFlowsEndTime = _AppTcpOptExpiredFlowsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2, 1, 8),
    _AppTcpOptExpiredFlowsEndTime_Type()
)
appTcpOptExpiredFlowsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsEndTime.setStatus("current")
_AppTcpOptExpiredFlowsTxBytes_Type = Counter64
_AppTcpOptExpiredFlowsTxBytes_Object = MibTableColumn
appTcpOptExpiredFlowsTxBytes = _AppTcpOptExpiredFlowsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2, 1, 9),
    _AppTcpOptExpiredFlowsTxBytes_Type()
)
appTcpOptExpiredFlowsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsTxBytes.setStatus("current")
_AppTcpOptExpiredFlowsRxBytes_Type = Counter64
_AppTcpOptExpiredFlowsRxBytes_Object = MibTableColumn
appTcpOptExpiredFlowsRxBytes = _AppTcpOptExpiredFlowsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2, 1, 10),
    _AppTcpOptExpiredFlowsRxBytes_Type()
)
appTcpOptExpiredFlowsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsRxBytes.setStatus("current")


class _AppTcpOptExpiredFlowsTcpState_Type(String):
    """Custom type appTcpOptExpiredFlowsTcpState based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppTcpOptExpiredFlowsTcpState_Type.__name__ = "String"
_AppTcpOptExpiredFlowsTcpState_Object = MibTableColumn
appTcpOptExpiredFlowsTcpState = _AppTcpOptExpiredFlowsTcpState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2, 1, 11),
    _AppTcpOptExpiredFlowsTcpState_Type()
)
appTcpOptExpiredFlowsTcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsTcpState.setStatus("current")


class _AppTcpOptExpiredFlowsUnoptReason_Type(String):
    """Custom type appTcpOptExpiredFlowsUnoptReason based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppTcpOptExpiredFlowsUnoptReason_Type.__name__ = "String"
_AppTcpOptExpiredFlowsUnoptReason_Object = MibTableColumn
appTcpOptExpiredFlowsUnoptReason = _AppTcpOptExpiredFlowsUnoptReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2, 1, 12),
    _AppTcpOptExpiredFlowsUnoptReason_Type()
)
appTcpOptExpiredFlowsUnoptReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsUnoptReason.setStatus("current")


class _AppTcpOptExpiredFlowsProxyIdentity_Type(String):
    """Custom type appTcpOptExpiredFlowsProxyIdentity based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppTcpOptExpiredFlowsProxyIdentity_Type.__name__ = "String"
_AppTcpOptExpiredFlowsProxyIdentity_Object = MibTableColumn
appTcpOptExpiredFlowsProxyIdentity = _AppTcpOptExpiredFlowsProxyIdentity_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2, 1, 13),
    _AppTcpOptExpiredFlowsProxyIdentity_Type()
)
appTcpOptExpiredFlowsProxyIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsProxyIdentity.setStatus("current")


class _AppTcpOptExpiredFlowsDeleteReason_Type(String):
    """Custom type appTcpOptExpiredFlowsDeleteReason based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AppTcpOptExpiredFlowsDeleteReason_Type.__name__ = "String"
_AppTcpOptExpiredFlowsDeleteReason_Object = MibTableColumn
appTcpOptExpiredFlowsDeleteReason = _AppTcpOptExpiredFlowsDeleteReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 2, 1, 14),
    _AppTcpOptExpiredFlowsDeleteReason_Type()
)
appTcpOptExpiredFlowsDeleteReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptExpiredFlowsDeleteReason.setStatus("current")
_AppTcpOptSummary_ObjectIdentity = ObjectIdentity
appTcpOptSummary = _AppTcpOptSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 3)
)
_AppTcpOptSummaryFlowsOptimized_Type = Unsigned32
_AppTcpOptSummaryFlowsOptimized_Object = MibScalar
appTcpOptSummaryFlowsOptimized = _AppTcpOptSummaryFlowsOptimized_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 3, 1),
    _AppTcpOptSummaryFlowsOptimized_Type()
)
appTcpOptSummaryFlowsOptimized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptSummaryFlowsOptimized.setStatus("current")
_AppTcpOptSummaryFlowsPassthrough_Type = Unsigned32
_AppTcpOptSummaryFlowsPassthrough_Object = MibScalar
appTcpOptSummaryFlowsPassthrough = _AppTcpOptSummaryFlowsPassthrough_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 3, 2),
    _AppTcpOptSummaryFlowsPassthrough_Type()
)
appTcpOptSummaryFlowsPassthrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptSummaryFlowsPassthrough.setStatus("current")
_AppTcpOptSummaryFlowsInProgress_Type = Unsigned32
_AppTcpOptSummaryFlowsInProgress_Object = MibScalar
appTcpOptSummaryFlowsInProgress = _AppTcpOptSummaryFlowsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 3, 3),
    _AppTcpOptSummaryFlowsInProgress_Type()
)
appTcpOptSummaryFlowsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptSummaryFlowsInProgress.setStatus("current")
_AppTcpOptSummaryFlowsExpired_Type = Unsigned32
_AppTcpOptSummaryFlowsExpired_Object = MibScalar
appTcpOptSummaryFlowsExpired = _AppTcpOptSummaryFlowsExpired_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 3, 4),
    _AppTcpOptSummaryFlowsExpired_Type()
)
appTcpOptSummaryFlowsExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptSummaryFlowsExpired.setStatus("current")
_AppTcpOptSummaryFlowsCloseWait_Type = Unsigned32
_AppTcpOptSummaryFlowsCloseWait_Object = MibScalar
appTcpOptSummaryFlowsCloseWait = _AppTcpOptSummaryFlowsCloseWait_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 3, 5),
    _AppTcpOptSummaryFlowsCloseWait_Type()
)
appTcpOptSummaryFlowsCloseWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptSummaryFlowsCloseWait.setStatus("current")
_AppTcpOptSummaryFlowsUntracked_Type = Unsigned32
_AppTcpOptSummaryFlowsUntracked_Object = MibScalar
appTcpOptSummaryFlowsUntracked = _AppTcpOptSummaryFlowsUntracked_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 6, 4, 3, 6),
    _AppTcpOptSummaryFlowsUntracked_Type()
)
appTcpOptSummaryFlowsUntracked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appTcpOptSummaryFlowsUntracked.setStatus("current")
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7)
)
_IpRoutesTableTable_Object = MibTable
ipRoutesTableTable = _IpRoutesTableTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1)
)
if mibBuilder.loadTexts:
    ipRoutesTableTable.setStatus("current")
_IpRoutesTableEntry_Object = MibTableRow
ipRoutesTableEntry = _IpRoutesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1)
)
ipRoutesTableEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "ipRoutesTableVpnId"),
    (0, "VIPTELA-OPER-VPN", "ipRoutesTableAddressFamily"),
    (0, "VIPTELA-OPER-VPN", "ipRoutesTablePrefix"),
    (0, "VIPTELA-OPER-VPN", "ipRoutesTablePathId"),
)
if mibBuilder.loadTexts:
    ipRoutesTableEntry.setStatus("current")


class _IpRoutesTableVpnId_Type(Unsigned32):
    """Custom type ipRoutesTableVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IpRoutesTableVpnId_Type.__name__ = "Unsigned32"
_IpRoutesTableVpnId_Object = MibTableColumn
ipRoutesTableVpnId = _IpRoutesTableVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 1),
    _IpRoutesTableVpnId_Type()
)
ipRoutesTableVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipRoutesTableVpnId.setStatus("current")


class _IpRoutesTableAddressFamily_Type(Integer32):
    """Custom type ipRoutesTableAddressFamily based on Integer32"""
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


_IpRoutesTableAddressFamily_Type.__name__ = "Integer32"
_IpRoutesTableAddressFamily_Object = MibTableColumn
ipRoutesTableAddressFamily = _IpRoutesTableAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 2),
    _IpRoutesTableAddressFamily_Type()
)
ipRoutesTableAddressFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipRoutesTableAddressFamily.setStatus("current")
_IpRoutesTablePrefix_Type = IpPrefix
_IpRoutesTablePrefix_Object = MibTableColumn
ipRoutesTablePrefix = _IpRoutesTablePrefix_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 3),
    _IpRoutesTablePrefix_Type()
)
ipRoutesTablePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipRoutesTablePrefix.setStatus("current")
_IpRoutesTablePathId_Type = Unsigned32
_IpRoutesTablePathId_Object = MibTableColumn
ipRoutesTablePathId = _IpRoutesTablePathId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 4),
    _IpRoutesTablePathId_Type()
)
ipRoutesTablePathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipRoutesTablePathId.setStatus("current")


class _IpRoutesTableProtocol_Type(Integer32):
    """Custom type ipRoutesTableProtocol based on Integer32"""
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
        *(("connected", 0),
          ("static", 1),
          ("ospf", 2),
          ("bgp", 3),
          ("omp", 4),
          ("nat", 5),
          ("gre", 6),
          ("natpoolOmp", 7),
          ("natpoolService", 8),
          ("stdIpsec", 9))
    )


_IpRoutesTableProtocol_Type.__name__ = "Integer32"
_IpRoutesTableProtocol_Object = MibTableColumn
ipRoutesTableProtocol = _IpRoutesTableProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 5),
    _IpRoutesTableProtocol_Type()
)
ipRoutesTableProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableProtocol.setStatus("current")


class _IpRoutesTableProtocolSubType_Type(Integer32):
    """Custom type ipRoutesTableProtocolSubType based on Integer32"""
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
        *(("intraArea", 1),
          ("interArea", 2),
          ("external1", 3),
          ("external2", 4),
          ("nssaExternal1", 5),
          ("nssaExternal2", 6),
          ("bgpExternal", 7),
          ("bgpInternal", 8))
    )


_IpRoutesTableProtocolSubType_Type.__name__ = "Integer32"
_IpRoutesTableProtocolSubType_Object = MibTableColumn
ipRoutesTableProtocolSubType = _IpRoutesTableProtocolSubType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 6),
    _IpRoutesTableProtocolSubType_Type()
)
ipRoutesTableProtocolSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableProtocolSubType.setStatus("current")
_IpRoutesTableDistance_Type = Unsigned32
_IpRoutesTableDistance_Object = MibTableColumn
ipRoutesTableDistance = _IpRoutesTableDistance_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 7),
    _IpRoutesTableDistance_Type()
)
ipRoutesTableDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableDistance.setStatus("current")
_IpRoutesTableMetric_Type = Unsigned32
_IpRoutesTableMetric_Object = MibTableColumn
ipRoutesTableMetric = _IpRoutesTableMetric_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 8),
    _IpRoutesTableMetric_Type()
)
ipRoutesTableMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableMetric.setStatus("current")
_IpRoutesTableUptime_Type = String
_IpRoutesTableUptime_Object = MibTableColumn
ipRoutesTableUptime = _IpRoutesTableUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 9),
    _IpRoutesTableUptime_Type()
)
ipRoutesTableUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableUptime.setStatus("current")
_IpRoutesTablePathFlags_Type = Unsigned32
_IpRoutesTablePathFlags_Object = MibTableColumn
ipRoutesTablePathFlags = _IpRoutesTablePathFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 10),
    _IpRoutesTablePathFlags_Type()
)
ipRoutesTablePathFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTablePathFlags.setStatus("current")
_IpRoutesTableNexthopFlags_Type = Unsigned32
_IpRoutesTableNexthopFlags_Object = MibTableColumn
ipRoutesTableNexthopFlags = _IpRoutesTableNexthopFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 11),
    _IpRoutesTableNexthopFlags_Type()
)
ipRoutesTableNexthopFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableNexthopFlags.setStatus("current")


class _IpRoutesTableNexthopType_Type(Integer32):
    """Custom type ipRoutesTableNexthopType based on Integer32"""
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
        *(("if-connected", 0),
          ("interface", 1),
          ("ipv4", 2),
          ("ipv4-with-ifindex", 3),
          ("ipv4-with-ifname", 4),
          ("ipv4-indirect", 5),
          ("ipv6", 6),
          ("ipv6-with-ifindex", 7),
          ("ipv6-with-ifname", 8),
          ("ipv6-indirect", 9),
          ("blackhole", 10),
          ("extranet", 11))
    )


_IpRoutesTableNexthopType_Type.__name__ = "Integer32"
_IpRoutesTableNexthopType_Object = MibTableColumn
ipRoutesTableNexthopType = _IpRoutesTableNexthopType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 12),
    _IpRoutesTableNexthopType_Type()
)
ipRoutesTableNexthopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableNexthopType.setStatus("current")


class _IpRoutesTableNexthopIfname_Type(String):
    """Custom type ipRoutesTableNexthopIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpRoutesTableNexthopIfname_Type.__name__ = "String"
_IpRoutesTableNexthopIfname_Object = MibTableColumn
ipRoutesTableNexthopIfname = _IpRoutesTableNexthopIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 13),
    _IpRoutesTableNexthopIfname_Type()
)
ipRoutesTableNexthopIfname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableNexthopIfname.setStatus("current")
_IpRoutesTableNexthopAddr_Type = InetAddressIP
_IpRoutesTableNexthopAddr_Object = MibTableColumn
ipRoutesTableNexthopAddr = _IpRoutesTableNexthopAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 14),
    _IpRoutesTableNexthopAddr_Type()
)
ipRoutesTableNexthopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableNexthopAddr.setStatus("current")


class _IpRoutesTableNexthopRtype_Type(Integer32):
    """Custom type ipRoutesTableNexthopRtype based on Integer32"""
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
        *(("if-connected", 0),
          ("interface", 1),
          ("ipv4", 2),
          ("ipv4-with-ifindex", 3),
          ("ipv4-with-ifname", 4),
          ("ipv4-indirect", 5),
          ("ipv6", 6),
          ("ipv6-with-ifindex", 7),
          ("ipv6-with-ifname", 8),
          ("ipv6-indirect", 9),
          ("blackhole", 10),
          ("extranet", 11))
    )


_IpRoutesTableNexthopRtype_Type.__name__ = "Integer32"
_IpRoutesTableNexthopRtype_Object = MibTableColumn
ipRoutesTableNexthopRtype = _IpRoutesTableNexthopRtype_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 15),
    _IpRoutesTableNexthopRtype_Type()
)
ipRoutesTableNexthopRtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableNexthopRtype.setStatus("current")


class _IpRoutesTableNexthopRifname_Type(String):
    """Custom type ipRoutesTableNexthopRifname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpRoutesTableNexthopRifname_Type.__name__ = "String"
_IpRoutesTableNexthopRifname_Object = MibTableColumn
ipRoutesTableNexthopRifname = _IpRoutesTableNexthopRifname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 16),
    _IpRoutesTableNexthopRifname_Type()
)
ipRoutesTableNexthopRifname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableNexthopRifname.setStatus("current")
_IpRoutesTableNexthopRaddr_Type = InetAddressIP
_IpRoutesTableNexthopRaddr_Object = MibTableColumn
ipRoutesTableNexthopRaddr = _IpRoutesTableNexthopRaddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 17),
    _IpRoutesTableNexthopRaddr_Type()
)
ipRoutesTableNexthopRaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableNexthopRaddr.setStatus("current")
_IpRoutesTableNexthopRsrc_Type = InetAddressIP
_IpRoutesTableNexthopRsrc_Object = MibTableColumn
ipRoutesTableNexthopRsrc = _IpRoutesTableNexthopRsrc_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 18),
    _IpRoutesTableNexthopRsrc_Type()
)
ipRoutesTableNexthopRsrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableNexthopRsrc.setStatus("current")
_IpRoutesTableIp_Type = InetAddressIP
_IpRoutesTableIp_Object = MibTableColumn
ipRoutesTableIp = _IpRoutesTableIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 19),
    _IpRoutesTableIp_Type()
)
ipRoutesTableIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableIp.setStatus("current")


class _IpRoutesTableColor_Type(Integer32):
    """Custom type ipRoutesTableColor based on Integer32"""
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


_IpRoutesTableColor_Type.__name__ = "Integer32"
_IpRoutesTableColor_Object = MibTableColumn
ipRoutesTableColor = _IpRoutesTableColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 20),
    _IpRoutesTableColor_Type()
)
ipRoutesTableColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableColor.setStatus("current")


class _IpRoutesTableEncap_Type(Integer32):
    """Custom type ipRoutesTableEncap based on Integer32"""
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


_IpRoutesTableEncap_Type.__name__ = "Integer32"
_IpRoutesTableEncap_Object = MibTableColumn
ipRoutesTableEncap = _IpRoutesTableEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 21),
    _IpRoutesTableEncap_Type()
)
ipRoutesTableEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableEncap.setStatus("current")


class _IpRoutesTableNexthopVpn_Type(Unsigned32):
    """Custom type ipRoutesTableNexthopVpn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IpRoutesTableNexthopVpn_Type.__name__ = "Unsigned32"
_IpRoutesTableNexthopVpn_Object = MibTableColumn
ipRoutesTableNexthopVpn = _IpRoutesTableNexthopVpn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 22),
    _IpRoutesTableNexthopVpn_Type()
)
ipRoutesTableNexthopVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableNexthopVpn.setStatus("current")
_IpRoutesTableNexthopLabel_Type = Unsigned32
_IpRoutesTableNexthopLabel_Object = MibTableColumn
ipRoutesTableNexthopLabel = _IpRoutesTableNexthopLabel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 23),
    _IpRoutesTableNexthopLabel_Type()
)
ipRoutesTableNexthopLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableNexthopLabel.setStatus("current")
_IpRoutesTableRstatus_Type = RouteStatusType
_IpRoutesTableRstatus_Object = MibTableColumn
ipRoutesTableRstatus = _IpRoutesTableRstatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 24),
    _IpRoutesTableRstatus_Type()
)
ipRoutesTableRstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableRstatus.setStatus("current")
_IpRoutesTableOmpTag_Type = Unsigned32
_IpRoutesTableOmpTag_Object = MibTableColumn
ipRoutesTableOmpTag = _IpRoutesTableOmpTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 25),
    _IpRoutesTableOmpTag_Type()
)
ipRoutesTableOmpTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableOmpTag.setStatus("current")
_IpRoutesTableOspfTag_Type = Unsigned32
_IpRoutesTableOspfTag_Object = MibTableColumn
ipRoutesTableOspfTag = _IpRoutesTableOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 1, 1, 26),
    _IpRoutesTableOspfTag_Type()
)
ipRoutesTableOspfTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesTableOspfTag.setStatus("current")
_IpLongerRoutesTableTable_Object = MibTable
ipLongerRoutesTableTable = _IpLongerRoutesTableTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5)
)
if mibBuilder.loadTexts:
    ipLongerRoutesTableTable.setStatus("current")
_IpLongerRoutesTableEntry_Object = MibTableRow
ipLongerRoutesTableEntry = _IpLongerRoutesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1)
)
ipLongerRoutesTableEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "ipLongerRoutesTableVpnId"),
    (0, "VIPTELA-OPER-VPN", "ipLongerRoutesTableAddressFamily"),
    (0, "VIPTELA-OPER-VPN", "ipLongerRoutesTablePrefix"),
    (0, "VIPTELA-OPER-VPN", "ipLongerRoutesTableLongerPrefix"),
    (0, "VIPTELA-OPER-VPN", "ipLongerRoutesTablePathId"),
)
if mibBuilder.loadTexts:
    ipLongerRoutesTableEntry.setStatus("current")


class _IpLongerRoutesTableVpnId_Type(Unsigned32):
    """Custom type ipLongerRoutesTableVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IpLongerRoutesTableVpnId_Type.__name__ = "Unsigned32"
_IpLongerRoutesTableVpnId_Object = MibTableColumn
ipLongerRoutesTableVpnId = _IpLongerRoutesTableVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 1),
    _IpLongerRoutesTableVpnId_Type()
)
ipLongerRoutesTableVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipLongerRoutesTableVpnId.setStatus("current")


class _IpLongerRoutesTableAddressFamily_Type(Integer32):
    """Custom type ipLongerRoutesTableAddressFamily based on Integer32"""
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


_IpLongerRoutesTableAddressFamily_Type.__name__ = "Integer32"
_IpLongerRoutesTableAddressFamily_Object = MibTableColumn
ipLongerRoutesTableAddressFamily = _IpLongerRoutesTableAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 2),
    _IpLongerRoutesTableAddressFamily_Type()
)
ipLongerRoutesTableAddressFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipLongerRoutesTableAddressFamily.setStatus("current")
_IpLongerRoutesTablePrefix_Type = IpPrefix
_IpLongerRoutesTablePrefix_Object = MibTableColumn
ipLongerRoutesTablePrefix = _IpLongerRoutesTablePrefix_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 3),
    _IpLongerRoutesTablePrefix_Type()
)
ipLongerRoutesTablePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipLongerRoutesTablePrefix.setStatus("current")
_IpLongerRoutesTableLongerPrefix_Type = IpPrefix
_IpLongerRoutesTableLongerPrefix_Object = MibTableColumn
ipLongerRoutesTableLongerPrefix = _IpLongerRoutesTableLongerPrefix_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 4),
    _IpLongerRoutesTableLongerPrefix_Type()
)
ipLongerRoutesTableLongerPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipLongerRoutesTableLongerPrefix.setStatus("current")
_IpLongerRoutesTablePathId_Type = Unsigned32
_IpLongerRoutesTablePathId_Object = MibTableColumn
ipLongerRoutesTablePathId = _IpLongerRoutesTablePathId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 5),
    _IpLongerRoutesTablePathId_Type()
)
ipLongerRoutesTablePathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipLongerRoutesTablePathId.setStatus("current")


class _IpLongerRoutesTableProtocol_Type(Integer32):
    """Custom type ipLongerRoutesTableProtocol based on Integer32"""
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
        *(("connected", 0),
          ("static", 1),
          ("ospf", 2),
          ("bgp", 3),
          ("omp", 4),
          ("nat", 5),
          ("gre", 6),
          ("natpoolOmp", 7),
          ("natpoolService", 8))
    )


_IpLongerRoutesTableProtocol_Type.__name__ = "Integer32"
_IpLongerRoutesTableProtocol_Object = MibTableColumn
ipLongerRoutesTableProtocol = _IpLongerRoutesTableProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 6),
    _IpLongerRoutesTableProtocol_Type()
)
ipLongerRoutesTableProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableProtocol.setStatus("current")


class _IpLongerRoutesTableProtocolSubType_Type(Integer32):
    """Custom type ipLongerRoutesTableProtocolSubType based on Integer32"""
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
        *(("intraArea", 1),
          ("interArea", 2),
          ("external1", 3),
          ("external2", 4),
          ("nssaExternal1", 5),
          ("nssaExternal2", 6),
          ("bgpExternal", 7),
          ("bgpInternal", 8))
    )


_IpLongerRoutesTableProtocolSubType_Type.__name__ = "Integer32"
_IpLongerRoutesTableProtocolSubType_Object = MibTableColumn
ipLongerRoutesTableProtocolSubType = _IpLongerRoutesTableProtocolSubType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 7),
    _IpLongerRoutesTableProtocolSubType_Type()
)
ipLongerRoutesTableProtocolSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableProtocolSubType.setStatus("current")
_IpLongerRoutesTableDistance_Type = Unsigned32
_IpLongerRoutesTableDistance_Object = MibTableColumn
ipLongerRoutesTableDistance = _IpLongerRoutesTableDistance_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 8),
    _IpLongerRoutesTableDistance_Type()
)
ipLongerRoutesTableDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableDistance.setStatus("current")
_IpLongerRoutesTableMetric_Type = Unsigned32
_IpLongerRoutesTableMetric_Object = MibTableColumn
ipLongerRoutesTableMetric = _IpLongerRoutesTableMetric_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 9),
    _IpLongerRoutesTableMetric_Type()
)
ipLongerRoutesTableMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableMetric.setStatus("current")
_IpLongerRoutesTableUptime_Type = String
_IpLongerRoutesTableUptime_Object = MibTableColumn
ipLongerRoutesTableUptime = _IpLongerRoutesTableUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 10),
    _IpLongerRoutesTableUptime_Type()
)
ipLongerRoutesTableUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableUptime.setStatus("current")
_IpLongerRoutesTablePathFlags_Type = Unsigned32
_IpLongerRoutesTablePathFlags_Object = MibTableColumn
ipLongerRoutesTablePathFlags = _IpLongerRoutesTablePathFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 11),
    _IpLongerRoutesTablePathFlags_Type()
)
ipLongerRoutesTablePathFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTablePathFlags.setStatus("current")
_IpLongerRoutesTableNexthopFlags_Type = Unsigned32
_IpLongerRoutesTableNexthopFlags_Object = MibTableColumn
ipLongerRoutesTableNexthopFlags = _IpLongerRoutesTableNexthopFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 12),
    _IpLongerRoutesTableNexthopFlags_Type()
)
ipLongerRoutesTableNexthopFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableNexthopFlags.setStatus("current")


class _IpLongerRoutesTableNexthopType_Type(Integer32):
    """Custom type ipLongerRoutesTableNexthopType based on Integer32"""
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
        *(("if-connected", 0),
          ("interface", 1),
          ("ipv4", 2),
          ("ipv4-with-ifindex", 3),
          ("ipv4-with-ifname", 4),
          ("ipv4-indirect", 5),
          ("ipv6", 6),
          ("ipv6-with-ifindex", 7),
          ("ipv6-with-ifname", 8),
          ("ipv6-indirect", 9),
          ("blackhole", 10),
          ("extranet", 11))
    )


_IpLongerRoutesTableNexthopType_Type.__name__ = "Integer32"
_IpLongerRoutesTableNexthopType_Object = MibTableColumn
ipLongerRoutesTableNexthopType = _IpLongerRoutesTableNexthopType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 13),
    _IpLongerRoutesTableNexthopType_Type()
)
ipLongerRoutesTableNexthopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableNexthopType.setStatus("current")


class _IpLongerRoutesTableNexthopIfname_Type(String):
    """Custom type ipLongerRoutesTableNexthopIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpLongerRoutesTableNexthopIfname_Type.__name__ = "String"
_IpLongerRoutesTableNexthopIfname_Object = MibTableColumn
ipLongerRoutesTableNexthopIfname = _IpLongerRoutesTableNexthopIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 14),
    _IpLongerRoutesTableNexthopIfname_Type()
)
ipLongerRoutesTableNexthopIfname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableNexthopIfname.setStatus("current")
_IpLongerRoutesTableNexthopAddr_Type = InetAddressIP
_IpLongerRoutesTableNexthopAddr_Object = MibTableColumn
ipLongerRoutesTableNexthopAddr = _IpLongerRoutesTableNexthopAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 15),
    _IpLongerRoutesTableNexthopAddr_Type()
)
ipLongerRoutesTableNexthopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableNexthopAddr.setStatus("current")


class _IpLongerRoutesTableNexthopRtype_Type(Integer32):
    """Custom type ipLongerRoutesTableNexthopRtype based on Integer32"""
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
        *(("if-connected", 0),
          ("interface", 1),
          ("ipv4", 2),
          ("ipv4-with-ifindex", 3),
          ("ipv4-with-ifname", 4),
          ("ipv4-indirect", 5),
          ("ipv6", 6),
          ("ipv6-with-ifindex", 7),
          ("ipv6-with-ifname", 8),
          ("ipv6-indirect", 9),
          ("blackhole", 10),
          ("extranet", 11))
    )


_IpLongerRoutesTableNexthopRtype_Type.__name__ = "Integer32"
_IpLongerRoutesTableNexthopRtype_Object = MibTableColumn
ipLongerRoutesTableNexthopRtype = _IpLongerRoutesTableNexthopRtype_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 16),
    _IpLongerRoutesTableNexthopRtype_Type()
)
ipLongerRoutesTableNexthopRtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableNexthopRtype.setStatus("current")


class _IpLongerRoutesTableNexthopRifname_Type(String):
    """Custom type ipLongerRoutesTableNexthopRifname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpLongerRoutesTableNexthopRifname_Type.__name__ = "String"
_IpLongerRoutesTableNexthopRifname_Object = MibTableColumn
ipLongerRoutesTableNexthopRifname = _IpLongerRoutesTableNexthopRifname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 17),
    _IpLongerRoutesTableNexthopRifname_Type()
)
ipLongerRoutesTableNexthopRifname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableNexthopRifname.setStatus("current")
_IpLongerRoutesTableNexthopRaddr_Type = InetAddressIP
_IpLongerRoutesTableNexthopRaddr_Object = MibTableColumn
ipLongerRoutesTableNexthopRaddr = _IpLongerRoutesTableNexthopRaddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 18),
    _IpLongerRoutesTableNexthopRaddr_Type()
)
ipLongerRoutesTableNexthopRaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableNexthopRaddr.setStatus("current")
_IpLongerRoutesTableNexthopRsrc_Type = InetAddressIP
_IpLongerRoutesTableNexthopRsrc_Object = MibTableColumn
ipLongerRoutesTableNexthopRsrc = _IpLongerRoutesTableNexthopRsrc_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 19),
    _IpLongerRoutesTableNexthopRsrc_Type()
)
ipLongerRoutesTableNexthopRsrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableNexthopRsrc.setStatus("current")
_IpLongerRoutesTableTlocIp_Type = InetAddressIP
_IpLongerRoutesTableTlocIp_Object = MibTableColumn
ipLongerRoutesTableTlocIp = _IpLongerRoutesTableTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 20),
    _IpLongerRoutesTableTlocIp_Type()
)
ipLongerRoutesTableTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableTlocIp.setStatus("current")


class _IpLongerRoutesTableTlocColor_Type(Integer32):
    """Custom type ipLongerRoutesTableTlocColor based on Integer32"""
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


_IpLongerRoutesTableTlocColor_Type.__name__ = "Integer32"
_IpLongerRoutesTableTlocColor_Object = MibTableColumn
ipLongerRoutesTableTlocColor = _IpLongerRoutesTableTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 21),
    _IpLongerRoutesTableTlocColor_Type()
)
ipLongerRoutesTableTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableTlocColor.setStatus("current")


class _IpLongerRoutesTableTlocEncap_Type(Integer32):
    """Custom type ipLongerRoutesTableTlocEncap based on Integer32"""
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


_IpLongerRoutesTableTlocEncap_Type.__name__ = "Integer32"
_IpLongerRoutesTableTlocEncap_Object = MibTableColumn
ipLongerRoutesTableTlocEncap = _IpLongerRoutesTableTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 22),
    _IpLongerRoutesTableTlocEncap_Type()
)
ipLongerRoutesTableTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableTlocEncap.setStatus("current")


class _IpLongerRoutesTableNexthopVpn_Type(Unsigned32):
    """Custom type ipLongerRoutesTableNexthopVpn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IpLongerRoutesTableNexthopVpn_Type.__name__ = "Unsigned32"
_IpLongerRoutesTableNexthopVpn_Object = MibTableColumn
ipLongerRoutesTableNexthopVpn = _IpLongerRoutesTableNexthopVpn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 23),
    _IpLongerRoutesTableNexthopVpn_Type()
)
ipLongerRoutesTableNexthopVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableNexthopVpn.setStatus("current")
_IpLongerRoutesTableNexthopLabel_Type = Unsigned32
_IpLongerRoutesTableNexthopLabel_Object = MibTableColumn
ipLongerRoutesTableNexthopLabel = _IpLongerRoutesTableNexthopLabel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 24),
    _IpLongerRoutesTableNexthopLabel_Type()
)
ipLongerRoutesTableNexthopLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableNexthopLabel.setStatus("current")
_IpLongerRoutesTableRstatus_Type = RouteStatusType
_IpLongerRoutesTableRstatus_Object = MibTableColumn
ipLongerRoutesTableRstatus = _IpLongerRoutesTableRstatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 25),
    _IpLongerRoutesTableRstatus_Type()
)
ipLongerRoutesTableRstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableRstatus.setStatus("current")
_IpLongerRoutesTableOmpTag_Type = Unsigned32
_IpLongerRoutesTableOmpTag_Object = MibTableColumn
ipLongerRoutesTableOmpTag = _IpLongerRoutesTableOmpTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 26),
    _IpLongerRoutesTableOmpTag_Type()
)
ipLongerRoutesTableOmpTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableOmpTag.setStatus("current")
_IpLongerRoutesTableOspfTag_Type = Unsigned32
_IpLongerRoutesTableOspfTag_Object = MibTableColumn
ipLongerRoutesTableOspfTag = _IpLongerRoutesTableOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 5, 1, 27),
    _IpLongerRoutesTableOspfTag_Type()
)
ipLongerRoutesTableOspfTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipLongerRoutesTableOspfTag.setStatus("current")
_IpBestMatchRouteTable_Object = MibTable
ipBestMatchRouteTable = _IpBestMatchRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6)
)
if mibBuilder.loadTexts:
    ipBestMatchRouteTable.setStatus("current")
_IpBestMatchRouteEntry_Object = MibTableRow
ipBestMatchRouteEntry = _IpBestMatchRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1)
)
ipBestMatchRouteEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "ipBestMatchRouteVpnId"),
    (0, "VIPTELA-OPER-VPN", "ipBestMatchRouteAddressFamily"),
    (0, "VIPTELA-OPER-VPN", "ipBestMatchRouteDestination"),
    (0, "VIPTELA-OPER-VPN", "ipBestMatchRoutePathId"),
)
if mibBuilder.loadTexts:
    ipBestMatchRouteEntry.setStatus("current")


class _IpBestMatchRouteVpnId_Type(Unsigned32):
    """Custom type ipBestMatchRouteVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IpBestMatchRouteVpnId_Type.__name__ = "Unsigned32"
_IpBestMatchRouteVpnId_Object = MibTableColumn
ipBestMatchRouteVpnId = _IpBestMatchRouteVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 1),
    _IpBestMatchRouteVpnId_Type()
)
ipBestMatchRouteVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipBestMatchRouteVpnId.setStatus("current")


class _IpBestMatchRouteAddressFamily_Type(Integer32):
    """Custom type ipBestMatchRouteAddressFamily based on Integer32"""
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


_IpBestMatchRouteAddressFamily_Type.__name__ = "Integer32"
_IpBestMatchRouteAddressFamily_Object = MibTableColumn
ipBestMatchRouteAddressFamily = _IpBestMatchRouteAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 2),
    _IpBestMatchRouteAddressFamily_Type()
)
ipBestMatchRouteAddressFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipBestMatchRouteAddressFamily.setStatus("current")
_IpBestMatchRouteDestination_Type = InetAddressIP
_IpBestMatchRouteDestination_Object = MibTableColumn
ipBestMatchRouteDestination = _IpBestMatchRouteDestination_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 3),
    _IpBestMatchRouteDestination_Type()
)
ipBestMatchRouteDestination.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipBestMatchRouteDestination.setStatus("current")
_IpBestMatchRoutePathId_Type = Unsigned32
_IpBestMatchRoutePathId_Object = MibTableColumn
ipBestMatchRoutePathId = _IpBestMatchRoutePathId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 4),
    _IpBestMatchRoutePathId_Type()
)
ipBestMatchRoutePathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipBestMatchRoutePathId.setStatus("current")
_IpBestMatchRoutePrefix_Type = IpPrefix
_IpBestMatchRoutePrefix_Object = MibTableColumn
ipBestMatchRoutePrefix = _IpBestMatchRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 5),
    _IpBestMatchRoutePrefix_Type()
)
ipBestMatchRoutePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRoutePrefix.setStatus("current")


class _IpBestMatchRouteProtocol_Type(Integer32):
    """Custom type ipBestMatchRouteProtocol based on Integer32"""
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
        *(("connected", 0),
          ("static", 1),
          ("ospf", 2),
          ("bgp", 3),
          ("omp", 4),
          ("nat", 5),
          ("gre", 6),
          ("natpoolOmp", 7),
          ("natpoolService", 8))
    )


_IpBestMatchRouteProtocol_Type.__name__ = "Integer32"
_IpBestMatchRouteProtocol_Object = MibTableColumn
ipBestMatchRouteProtocol = _IpBestMatchRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 6),
    _IpBestMatchRouteProtocol_Type()
)
ipBestMatchRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteProtocol.setStatus("current")


class _IpBestMatchRouteProtocolSubType_Type(Integer32):
    """Custom type ipBestMatchRouteProtocolSubType based on Integer32"""
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
        *(("intraArea", 1),
          ("interArea", 2),
          ("external1", 3),
          ("external2", 4),
          ("nssaExternal1", 5),
          ("nssaExternal2", 6),
          ("bgpExternal", 7),
          ("bgpInternal", 8))
    )


_IpBestMatchRouteProtocolSubType_Type.__name__ = "Integer32"
_IpBestMatchRouteProtocolSubType_Object = MibTableColumn
ipBestMatchRouteProtocolSubType = _IpBestMatchRouteProtocolSubType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 7),
    _IpBestMatchRouteProtocolSubType_Type()
)
ipBestMatchRouteProtocolSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteProtocolSubType.setStatus("current")
_IpBestMatchRouteDistance_Type = Unsigned32
_IpBestMatchRouteDistance_Object = MibTableColumn
ipBestMatchRouteDistance = _IpBestMatchRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 8),
    _IpBestMatchRouteDistance_Type()
)
ipBestMatchRouteDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteDistance.setStatus("current")
_IpBestMatchRouteMetric_Type = Unsigned32
_IpBestMatchRouteMetric_Object = MibTableColumn
ipBestMatchRouteMetric = _IpBestMatchRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 9),
    _IpBestMatchRouteMetric_Type()
)
ipBestMatchRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteMetric.setStatus("current")
_IpBestMatchRouteUptime_Type = String
_IpBestMatchRouteUptime_Object = MibTableColumn
ipBestMatchRouteUptime = _IpBestMatchRouteUptime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 10),
    _IpBestMatchRouteUptime_Type()
)
ipBestMatchRouteUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteUptime.setStatus("current")
_IpBestMatchRoutePathFlags_Type = Unsigned32
_IpBestMatchRoutePathFlags_Object = MibTableColumn
ipBestMatchRoutePathFlags = _IpBestMatchRoutePathFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 11),
    _IpBestMatchRoutePathFlags_Type()
)
ipBestMatchRoutePathFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRoutePathFlags.setStatus("current")
_IpBestMatchRouteNexthopFlags_Type = Unsigned32
_IpBestMatchRouteNexthopFlags_Object = MibTableColumn
ipBestMatchRouteNexthopFlags = _IpBestMatchRouteNexthopFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 12),
    _IpBestMatchRouteNexthopFlags_Type()
)
ipBestMatchRouteNexthopFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteNexthopFlags.setStatus("current")


class _IpBestMatchRouteNexthopType_Type(Integer32):
    """Custom type ipBestMatchRouteNexthopType based on Integer32"""
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
        *(("if-connected", 0),
          ("interface", 1),
          ("ipv4", 2),
          ("ipv4-with-ifindex", 3),
          ("ipv4-with-ifname", 4),
          ("ipv4-indirect", 5),
          ("ipv6", 6),
          ("ipv6-with-ifindex", 7),
          ("ipv6-with-ifname", 8),
          ("ipv6-indirect", 9),
          ("blackhole", 10),
          ("extranet", 11))
    )


_IpBestMatchRouteNexthopType_Type.__name__ = "Integer32"
_IpBestMatchRouteNexthopType_Object = MibTableColumn
ipBestMatchRouteNexthopType = _IpBestMatchRouteNexthopType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 13),
    _IpBestMatchRouteNexthopType_Type()
)
ipBestMatchRouteNexthopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteNexthopType.setStatus("current")


class _IpBestMatchRouteNexthopIfname_Type(String):
    """Custom type ipBestMatchRouteNexthopIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpBestMatchRouteNexthopIfname_Type.__name__ = "String"
_IpBestMatchRouteNexthopIfname_Object = MibTableColumn
ipBestMatchRouteNexthopIfname = _IpBestMatchRouteNexthopIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 14),
    _IpBestMatchRouteNexthopIfname_Type()
)
ipBestMatchRouteNexthopIfname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteNexthopIfname.setStatus("current")
_IpBestMatchRouteNexthopAddr_Type = InetAddressIP
_IpBestMatchRouteNexthopAddr_Object = MibTableColumn
ipBestMatchRouteNexthopAddr = _IpBestMatchRouteNexthopAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 15),
    _IpBestMatchRouteNexthopAddr_Type()
)
ipBestMatchRouteNexthopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteNexthopAddr.setStatus("current")


class _IpBestMatchRouteNexthopRtype_Type(Integer32):
    """Custom type ipBestMatchRouteNexthopRtype based on Integer32"""
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
        *(("if-connected", 0),
          ("interface", 1),
          ("ipv4", 2),
          ("ipv4-with-ifindex", 3),
          ("ipv4-with-ifname", 4),
          ("ipv4-indirect", 5),
          ("ipv6", 6),
          ("ipv6-with-ifindex", 7),
          ("ipv6-with-ifname", 8),
          ("ipv6-indirect", 9),
          ("blackhole", 10),
          ("extranet", 11))
    )


_IpBestMatchRouteNexthopRtype_Type.__name__ = "Integer32"
_IpBestMatchRouteNexthopRtype_Object = MibTableColumn
ipBestMatchRouteNexthopRtype = _IpBestMatchRouteNexthopRtype_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 16),
    _IpBestMatchRouteNexthopRtype_Type()
)
ipBestMatchRouteNexthopRtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteNexthopRtype.setStatus("current")


class _IpBestMatchRouteNexthopRifname_Type(String):
    """Custom type ipBestMatchRouteNexthopRifname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpBestMatchRouteNexthopRifname_Type.__name__ = "String"
_IpBestMatchRouteNexthopRifname_Object = MibTableColumn
ipBestMatchRouteNexthopRifname = _IpBestMatchRouteNexthopRifname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 17),
    _IpBestMatchRouteNexthopRifname_Type()
)
ipBestMatchRouteNexthopRifname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteNexthopRifname.setStatus("current")
_IpBestMatchRouteNexthopRaddr_Type = InetAddressIP
_IpBestMatchRouteNexthopRaddr_Object = MibTableColumn
ipBestMatchRouteNexthopRaddr = _IpBestMatchRouteNexthopRaddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 18),
    _IpBestMatchRouteNexthopRaddr_Type()
)
ipBestMatchRouteNexthopRaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteNexthopRaddr.setStatus("current")
_IpBestMatchRouteNexthopRsrc_Type = InetAddressIP
_IpBestMatchRouteNexthopRsrc_Object = MibTableColumn
ipBestMatchRouteNexthopRsrc = _IpBestMatchRouteNexthopRsrc_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 19),
    _IpBestMatchRouteNexthopRsrc_Type()
)
ipBestMatchRouteNexthopRsrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteNexthopRsrc.setStatus("current")
_IpBestMatchRouteTlocIp_Type = InetAddressIP
_IpBestMatchRouteTlocIp_Object = MibTableColumn
ipBestMatchRouteTlocIp = _IpBestMatchRouteTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 20),
    _IpBestMatchRouteTlocIp_Type()
)
ipBestMatchRouteTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteTlocIp.setStatus("current")


class _IpBestMatchRouteTlocColor_Type(Integer32):
    """Custom type ipBestMatchRouteTlocColor based on Integer32"""
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


_IpBestMatchRouteTlocColor_Type.__name__ = "Integer32"
_IpBestMatchRouteTlocColor_Object = MibTableColumn
ipBestMatchRouteTlocColor = _IpBestMatchRouteTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 21),
    _IpBestMatchRouteTlocColor_Type()
)
ipBestMatchRouteTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteTlocColor.setStatus("current")


class _IpBestMatchRouteTlocEncap_Type(Integer32):
    """Custom type ipBestMatchRouteTlocEncap based on Integer32"""
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


_IpBestMatchRouteTlocEncap_Type.__name__ = "Integer32"
_IpBestMatchRouteTlocEncap_Object = MibTableColumn
ipBestMatchRouteTlocEncap = _IpBestMatchRouteTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 22),
    _IpBestMatchRouteTlocEncap_Type()
)
ipBestMatchRouteTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteTlocEncap.setStatus("current")
_IpBestMatchRouteNexthopLabel_Type = Unsigned32
_IpBestMatchRouteNexthopLabel_Object = MibTableColumn
ipBestMatchRouteNexthopLabel = _IpBestMatchRouteNexthopLabel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 23),
    _IpBestMatchRouteNexthopLabel_Type()
)
ipBestMatchRouteNexthopLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteNexthopLabel.setStatus("current")
_IpBestMatchRouteRstatus_Type = RouteStatusType
_IpBestMatchRouteRstatus_Object = MibTableColumn
ipBestMatchRouteRstatus = _IpBestMatchRouteRstatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 24),
    _IpBestMatchRouteRstatus_Type()
)
ipBestMatchRouteRstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteRstatus.setStatus("current")
_IpBestMatchRouteOmpTag_Type = Unsigned32
_IpBestMatchRouteOmpTag_Object = MibTableColumn
ipBestMatchRouteOmpTag = _IpBestMatchRouteOmpTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 25),
    _IpBestMatchRouteOmpTag_Type()
)
ipBestMatchRouteOmpTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteOmpTag.setStatus("current")
_IpBestMatchRouteNexthopVpn_Type = Unsigned32
_IpBestMatchRouteNexthopVpn_Object = MibTableColumn
ipBestMatchRouteNexthopVpn = _IpBestMatchRouteNexthopVpn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 26),
    _IpBestMatchRouteNexthopVpn_Type()
)
ipBestMatchRouteNexthopVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteNexthopVpn.setStatus("current")
_IpBestMatchRouteOspfTag_Type = Unsigned32
_IpBestMatchRouteOspfTag_Object = MibTableColumn
ipBestMatchRouteOspfTag = _IpBestMatchRouteOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 6, 1, 27),
    _IpBestMatchRouteOspfTag_Type()
)
ipBestMatchRouteOspfTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBestMatchRouteOspfTag.setStatus("current")
_IpMfib_ObjectIdentity = ObjectIdentity
ipMfib = _IpMfib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7)
)
_IpMfibSummaryTable_Object = MibTable
ipMfibSummaryTable = _IpMfibSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 1)
)
if mibBuilder.loadTexts:
    ipMfibSummaryTable.setStatus("current")
_IpMfibSummaryEntry_Object = MibTableRow
ipMfibSummaryEntry = _IpMfibSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 1, 1)
)
ipMfibSummaryEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "ipMfibSummaryVpnId"),
    (0, "VIPTELA-OPER-VPN", "ipMfibSummaryGroup"),
    (0, "VIPTELA-OPER-VPN", "ipMfibSummarySource"),
)
if mibBuilder.loadTexts:
    ipMfibSummaryEntry.setStatus("current")


class _IpMfibSummaryVpnId_Type(Unsigned32):
    """Custom type ipMfibSummaryVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IpMfibSummaryVpnId_Type.__name__ = "Unsigned32"
_IpMfibSummaryVpnId_Object = MibTableColumn
ipMfibSummaryVpnId = _IpMfibSummaryVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 1, 1, 1),
    _IpMfibSummaryVpnId_Type()
)
ipMfibSummaryVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMfibSummaryVpnId.setStatus("current")
_IpMfibSummaryGroup_Type = InetAddressIP
_IpMfibSummaryGroup_Object = MibTableColumn
ipMfibSummaryGroup = _IpMfibSummaryGroup_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 1, 1, 2),
    _IpMfibSummaryGroup_Type()
)
ipMfibSummaryGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMfibSummaryGroup.setStatus("current")
_IpMfibSummarySource_Type = InetAddressIP
_IpMfibSummarySource_Object = MibTableColumn
ipMfibSummarySource = _IpMfibSummarySource_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 1, 1, 3),
    _IpMfibSummarySource_Type()
)
ipMfibSummarySource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMfibSummarySource.setStatus("current")


class _IpMfibSummaryUpstreamIf_Type(String):
    """Custom type ipMfibSummaryUpstreamIf based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpMfibSummaryUpstreamIf_Type.__name__ = "String"
_IpMfibSummaryUpstreamIf_Object = MibTableColumn
ipMfibSummaryUpstreamIf = _IpMfibSummaryUpstreamIf_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 1, 1, 4),
    _IpMfibSummaryUpstreamIf_Type()
)
ipMfibSummaryUpstreamIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibSummaryUpstreamIf.setStatus("current")
_IpMfibSummaryUpstreamTunnel_Type = InetAddressIP
_IpMfibSummaryUpstreamTunnel_Object = MibTableColumn
ipMfibSummaryUpstreamTunnel = _IpMfibSummaryUpstreamTunnel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 1, 1, 5),
    _IpMfibSummaryUpstreamTunnel_Type()
)
ipMfibSummaryUpstreamTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibSummaryUpstreamTunnel.setStatus("current")
_IpMfibSummaryNumServiceOils_Type = Unsigned32
_IpMfibSummaryNumServiceOils_Object = MibTableColumn
ipMfibSummaryNumServiceOils = _IpMfibSummaryNumServiceOils_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 1, 1, 6),
    _IpMfibSummaryNumServiceOils_Type()
)
ipMfibSummaryNumServiceOils.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibSummaryNumServiceOils.setStatus("current")
_IpMfibSummaryNumTunnelOils_Type = Unsigned32
_IpMfibSummaryNumTunnelOils_Object = MibTableColumn
ipMfibSummaryNumTunnelOils = _IpMfibSummaryNumTunnelOils_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 1, 1, 7),
    _IpMfibSummaryNumTunnelOils_Type()
)
ipMfibSummaryNumTunnelOils.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibSummaryNumTunnelOils.setStatus("current")
_IpMfibOilTable_Object = MibTable
ipMfibOilTable = _IpMfibOilTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 2)
)
if mibBuilder.loadTexts:
    ipMfibOilTable.setStatus("current")
_IpMfibOilEntry_Object = MibTableRow
ipMfibOilEntry = _IpMfibOilEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 2, 1)
)
ipMfibOilEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "ipMfibOilVpnId"),
    (0, "VIPTELA-OPER-VPN", "ipMfibOilGroup"),
    (0, "VIPTELA-OPER-VPN", "ipMfibOilSource"),
)
if mibBuilder.loadTexts:
    ipMfibOilEntry.setStatus("current")


class _IpMfibOilVpnId_Type(Unsigned32):
    """Custom type ipMfibOilVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IpMfibOilVpnId_Type.__name__ = "Unsigned32"
_IpMfibOilVpnId_Object = MibTableColumn
ipMfibOilVpnId = _IpMfibOilVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 2, 1, 1),
    _IpMfibOilVpnId_Type()
)
ipMfibOilVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMfibOilVpnId.setStatus("current")
_IpMfibOilGroup_Type = InetAddressIP
_IpMfibOilGroup_Object = MibTableColumn
ipMfibOilGroup = _IpMfibOilGroup_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 2, 1, 2),
    _IpMfibOilGroup_Type()
)
ipMfibOilGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMfibOilGroup.setStatus("current")
_IpMfibOilSource_Type = InetAddressIP
_IpMfibOilSource_Object = MibTableColumn
ipMfibOilSource = _IpMfibOilSource_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 2, 1, 3),
    _IpMfibOilSource_Type()
)
ipMfibOilSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibOilSource.setStatus("current")
_IpMfibStatsTable_Object = MibTable
ipMfibStatsTable = _IpMfibStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3)
)
if mibBuilder.loadTexts:
    ipMfibStatsTable.setStatus("current")
_IpMfibStatsEntry_Object = MibTableRow
ipMfibStatsEntry = _IpMfibStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1)
)
ipMfibStatsEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "ipMfibStatsVpnId"),
    (0, "VIPTELA-OPER-VPN", "ipMfibStatsGroup"),
    (0, "VIPTELA-OPER-VPN", "ipMfibStatsSource"),
)
if mibBuilder.loadTexts:
    ipMfibStatsEntry.setStatus("current")


class _IpMfibStatsVpnId_Type(Unsigned32):
    """Custom type ipMfibStatsVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IpMfibStatsVpnId_Type.__name__ = "Unsigned32"
_IpMfibStatsVpnId_Object = MibTableColumn
ipMfibStatsVpnId = _IpMfibStatsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 1),
    _IpMfibStatsVpnId_Type()
)
ipMfibStatsVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMfibStatsVpnId.setStatus("current")
_IpMfibStatsGroup_Type = InetAddressIP
_IpMfibStatsGroup_Object = MibTableColumn
ipMfibStatsGroup = _IpMfibStatsGroup_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 2),
    _IpMfibStatsGroup_Type()
)
ipMfibStatsGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMfibStatsGroup.setStatus("current")
_IpMfibStatsSource_Type = InetAddressIP
_IpMfibStatsSource_Object = MibTableColumn
ipMfibStatsSource = _IpMfibStatsSource_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 3),
    _IpMfibStatsSource_Type()
)
ipMfibStatsSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMfibStatsSource.setStatus("current")
_IpMfibStatsRxPkts_Type = Counter64
_IpMfibStatsRxPkts_Object = MibTableColumn
ipMfibStatsRxPkts = _IpMfibStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 4),
    _IpMfibStatsRxPkts_Type()
)
ipMfibStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibStatsRxPkts.setStatus("current")
_IpMfibStatsRxOctets_Type = Counter64
_IpMfibStatsRxOctets_Object = MibTableColumn
ipMfibStatsRxOctets = _IpMfibStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 5),
    _IpMfibStatsRxOctets_Type()
)
ipMfibStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibStatsRxOctets.setStatus("current")
_IpMfibStatsTxPkts_Type = Counter64
_IpMfibStatsTxPkts_Object = MibTableColumn
ipMfibStatsTxPkts = _IpMfibStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 6),
    _IpMfibStatsTxPkts_Type()
)
ipMfibStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibStatsTxPkts.setStatus("current")
_IpMfibStatsTxOctets_Type = Counter64
_IpMfibStatsTxOctets_Object = MibTableColumn
ipMfibStatsTxOctets = _IpMfibStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 7),
    _IpMfibStatsTxOctets_Type()
)
ipMfibStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibStatsTxOctets.setStatus("current")
_IpMfibStatsTxToPimPkts_Type = Counter64
_IpMfibStatsTxToPimPkts_Object = MibTableColumn
ipMfibStatsTxToPimPkts = _IpMfibStatsTxToPimPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 8),
    _IpMfibStatsTxToPimPkts_Type()
)
ipMfibStatsTxToPimPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibStatsTxToPimPkts.setStatus("current")
_IpMfibStatsRxPacketRate_Type = Counter64
_IpMfibStatsRxPacketRate_Object = MibTableColumn
ipMfibStatsRxPacketRate = _IpMfibStatsRxPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 9),
    _IpMfibStatsRxPacketRate_Type()
)
ipMfibStatsRxPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibStatsRxPacketRate.setStatus("current")
_IpMfibStatsRxOctetRate_Type = Counter64
_IpMfibStatsRxOctetRate_Object = MibTableColumn
ipMfibStatsRxOctetRate = _IpMfibStatsRxOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 10),
    _IpMfibStatsRxOctetRate_Type()
)
ipMfibStatsRxOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibStatsRxOctetRate.setStatus("current")
_IpMfibStatsTxPacketRate_Type = Counter64
_IpMfibStatsTxPacketRate_Object = MibTableColumn
ipMfibStatsTxPacketRate = _IpMfibStatsTxPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 11),
    _IpMfibStatsTxPacketRate_Type()
)
ipMfibStatsTxPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibStatsTxPacketRate.setStatus("current")
_IpMfibStatsTxOctetRate_Type = Counter64
_IpMfibStatsTxOctetRate_Object = MibTableColumn
ipMfibStatsTxOctetRate = _IpMfibStatsTxOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 12),
    _IpMfibStatsTxOctetRate_Type()
)
ipMfibStatsTxOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibStatsTxOctetRate.setStatus("current")


class _IpMfibStatsAvgReplication_Type(String):
    """Custom type ipMfibStatsAvgReplication based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpMfibStatsAvgReplication_Type.__name__ = "String"
_IpMfibStatsAvgReplication_Object = MibTableColumn
ipMfibStatsAvgReplication = _IpMfibStatsAvgReplication_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 13),
    _IpMfibStatsAvgReplication_Type()
)
ipMfibStatsAvgReplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibStatsAvgReplication.setStatus("current")
_IpMfibStatsRpfFailure_Type = Unsigned32
_IpMfibStatsRpfFailure_Object = MibTableColumn
ipMfibStatsRpfFailure = _IpMfibStatsRpfFailure_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 14),
    _IpMfibStatsRpfFailure_Type()
)
ipMfibStatsRpfFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibStatsRpfFailure.setStatus("current")
_IpMfibStatsTxInvalidOilFailure_Type = Unsigned32
_IpMfibStatsTxInvalidOilFailure_Object = MibTableColumn
ipMfibStatsTxInvalidOilFailure = _IpMfibStatsTxInvalidOilFailure_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 15),
    _IpMfibStatsTxInvalidOilFailure_Type()
)
ipMfibStatsTxInvalidOilFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibStatsTxInvalidOilFailure.setStatus("current")
_IpMfibStatsTxFailure_Type = Unsigned32
_IpMfibStatsTxFailure_Object = MibTableColumn
ipMfibStatsTxFailure = _IpMfibStatsTxFailure_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 16),
    _IpMfibStatsTxFailure_Type()
)
ipMfibStatsTxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibStatsTxFailure.setStatus("current")
_IpMfibStatsRxPolicyDrop_Type = Unsigned32
_IpMfibStatsRxPolicyDrop_Object = MibTableColumn
ipMfibStatsRxPolicyDrop = _IpMfibStatsRxPolicyDrop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 17),
    _IpMfibStatsRxPolicyDrop_Type()
)
ipMfibStatsRxPolicyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibStatsRxPolicyDrop.setStatus("current")
_IpMfibStatsTxPolicyDrop_Type = Unsigned32
_IpMfibStatsTxPolicyDrop_Object = MibTableColumn
ipMfibStatsTxPolicyDrop = _IpMfibStatsTxPolicyDrop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 7, 3, 1, 18),
    _IpMfibStatsTxPolicyDrop_Type()
)
ipMfibStatsTxPolicyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibStatsTxPolicyDrop.setStatus("current")
_IpFibTable_Object = MibTable
ipFibTable = _IpFibTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 8)
)
if mibBuilder.loadTexts:
    ipFibTable.setStatus("current")
_IpFibEntry_Object = MibTableRow
ipFibEntry = _IpFibEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 8, 1)
)
ipFibEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "ipFibVpnId"),
    (0, "VIPTELA-OPER-VPN", "ipFibAddressFamily"),
    (0, "VIPTELA-OPER-VPN", "ipFibPrefix"),
    (0, "VIPTELA-OPER-VPN", "ipFibPathId"),
)
if mibBuilder.loadTexts:
    ipFibEntry.setStatus("current")


class _IpFibVpnId_Type(Unsigned32):
    """Custom type ipFibVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IpFibVpnId_Type.__name__ = "Unsigned32"
_IpFibVpnId_Object = MibTableColumn
ipFibVpnId = _IpFibVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 8, 1, 1),
    _IpFibVpnId_Type()
)
ipFibVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFibVpnId.setStatus("current")
_IpFibPrefix_Type = IpPrefix
_IpFibPrefix_Object = MibTableColumn
ipFibPrefix = _IpFibPrefix_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 8, 1, 2),
    _IpFibPrefix_Type()
)
ipFibPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFibPrefix.setStatus("current")
_IpFibPathId_Type = Unsigned32
_IpFibPathId_Object = MibTableColumn
ipFibPathId = _IpFibPathId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 8, 1, 3),
    _IpFibPathId_Type()
)
ipFibPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFibPathId.setStatus("current")


class _IpFibOutIfname_Type(String):
    """Custom type ipFibOutIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpFibOutIfname_Type.__name__ = "String"
_IpFibOutIfname_Object = MibTableColumn
ipFibOutIfname = _IpFibOutIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 8, 1, 4),
    _IpFibOutIfname_Type()
)
ipFibOutIfname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFibOutIfname.setStatus("current")
_IpFibNexthopAddress_Type = InetAddressIP
_IpFibNexthopAddress_Object = MibTableColumn
ipFibNexthopAddress = _IpFibNexthopAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 8, 1, 5),
    _IpFibNexthopAddress_Type()
)
ipFibNexthopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFibNexthopAddress.setStatus("current")
_IpFibNexthopLabel_Type = Unsigned32
_IpFibNexthopLabel_Object = MibTableColumn
ipFibNexthopLabel = _IpFibNexthopLabel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 8, 1, 6),
    _IpFibNexthopLabel_Type()
)
ipFibNexthopLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFibNexthopLabel.setStatus("current")
_IpFibSaIndex_Type = Unsigned32
_IpFibSaIndex_Object = MibTableColumn
ipFibSaIndex = _IpFibSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 8, 1, 7),
    _IpFibSaIndex_Type()
)
ipFibSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFibSaIndex.setStatus("current")
_IpFibIp_Type = InetAddressIP
_IpFibIp_Object = MibTableColumn
ipFibIp = _IpFibIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 8, 1, 8),
    _IpFibIp_Type()
)
ipFibIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFibIp.setStatus("current")


class _IpFibColor_Type(Integer32):
    """Custom type ipFibColor based on Integer32"""
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


_IpFibColor_Type.__name__ = "Integer32"
_IpFibColor_Object = MibTableColumn
ipFibColor = _IpFibColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 8, 1, 9),
    _IpFibColor_Type()
)
ipFibColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFibColor.setStatus("current")


class _IpFibAddressFamily_Type(Integer32):
    """Custom type ipFibAddressFamily based on Integer32"""
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


_IpFibAddressFamily_Type.__name__ = "Integer32"
_IpFibAddressFamily_Object = MibTableColumn
ipFibAddressFamily = _IpFibAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 8, 1, 10),
    _IpFibAddressFamily_Type()
)
ipFibAddressFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFibAddressFamily.setStatus("current")
_IpFibNexthopVpn_Type = Unsigned32
_IpFibNexthopVpn_Object = MibTableColumn
ipFibNexthopVpn = _IpFibNexthopVpn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 8, 1, 11),
    _IpFibNexthopVpn_Type()
)
ipFibNexthopVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFibNexthopVpn.setStatus("current")
_IpNat_ObjectIdentity = ObjectIdentity
ipNat = _IpNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9)
)
_IpNatInterfaceTable_Object = MibTable
ipNatInterfaceTable = _IpNatInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 1)
)
if mibBuilder.loadTexts:
    ipNatInterfaceTable.setStatus("current")
_IpNatInterfaceEntry_Object = MibTableRow
ipNatInterfaceEntry = _IpNatInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 1, 1)
)
ipNatInterfaceEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "ipNatInterfaceVpnId"),
    (0, "VIPTELA-OPER-VPN", "ipNatInterfaceIfname"),
)
if mibBuilder.loadTexts:
    ipNatInterfaceEntry.setStatus("current")


class _IpNatInterfaceVpnId_Type(Unsigned32):
    """Custom type ipNatInterfaceVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IpNatInterfaceVpnId_Type.__name__ = "Unsigned32"
_IpNatInterfaceVpnId_Object = MibTableColumn
ipNatInterfaceVpnId = _IpNatInterfaceVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 1, 1, 1),
    _IpNatInterfaceVpnId_Type()
)
ipNatInterfaceVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNatInterfaceVpnId.setStatus("current")


class _IpNatInterfaceIfname_Type(String):
    """Custom type ipNatInterfaceIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpNatInterfaceIfname_Type.__name__ = "String"
_IpNatInterfaceIfname_Object = MibTableColumn
ipNatInterfaceIfname = _IpNatInterfaceIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 1, 1, 2),
    _IpNatInterfaceIfname_Type()
)
ipNatInterfaceIfname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNatInterfaceIfname.setStatus("current")


class _IpNatInterfaceMappingType_Type(Integer32):
    """Custom type ipNatInterfaceMappingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endpoint-independent", 0),
          ("address-port-dependent", 1),
          ("null-translation", 2))
    )


_IpNatInterfaceMappingType_Type.__name__ = "Integer32"
_IpNatInterfaceMappingType_Object = MibTableColumn
ipNatInterfaceMappingType = _IpNatInterfaceMappingType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 1, 1, 3),
    _IpNatInterfaceMappingType_Type()
)
ipNatInterfaceMappingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceMappingType.setStatus("current")


class _IpNatInterfaceFilterType_Type(Integer32):
    """Custom type ipNatInterfaceFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("address-port-restricted", 0)
    )


_IpNatInterfaceFilterType_Type.__name__ = "Integer32"
_IpNatInterfaceFilterType_Object = MibTableColumn
ipNatInterfaceFilterType = _IpNatInterfaceFilterType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 1, 1, 4),
    _IpNatInterfaceFilterType_Type()
)
ipNatInterfaceFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceFilterType.setStatus("current")
_IpNatInterfaceFilterCount_Type = Unsigned32
_IpNatInterfaceFilterCount_Object = MibTableColumn
ipNatInterfaceFilterCount = _IpNatInterfaceFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 1, 1, 5),
    _IpNatInterfaceFilterCount_Type()
)
ipNatInterfaceFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceFilterCount.setStatus("current")
_IpNatInterfaceFibFilterCount_Type = Unsigned32
_IpNatInterfaceFibFilterCount_Object = MibTableColumn
ipNatInterfaceFibFilterCount = _IpNatInterfaceFibFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 1, 1, 6),
    _IpNatInterfaceFibFilterCount_Type()
)
ipNatInterfaceFibFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceFibFilterCount.setStatus("current")
_IpNatInterfaceIp_Type = IpPrefix
_IpNatInterfaceIp_Object = MibTableColumn
ipNatInterfaceIp = _IpNatInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 1, 1, 7),
    _IpNatInterfaceIp_Type()
)
ipNatInterfaceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceIp.setStatus("current")
_IpNatInterfaceNumberIpPools_Type = Unsigned32
_IpNatInterfaceNumberIpPools_Object = MibTableColumn
ipNatInterfaceNumberIpPools = _IpNatInterfaceNumberIpPools_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 1, 1, 8),
    _IpNatInterfaceNumberIpPools_Type()
)
ipNatInterfaceNumberIpPools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceNumberIpPools.setStatus("current")
_IpNatInterfaceStatisticsTable_Object = MibTable
ipNatInterfaceStatisticsTable = _IpNatInterfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2)
)
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsTable.setStatus("current")
_IpNatInterfaceStatisticsEntry_Object = MibTableRow
ipNatInterfaceStatisticsEntry = _IpNatInterfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1)
)
ipNatInterfaceStatisticsEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "ipNatInterfaceStatisticsVpnId"),
    (0, "VIPTELA-OPER-VPN", "ipNatInterfaceStatisticsIfname"),
)
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsEntry.setStatus("current")


class _IpNatInterfaceStatisticsVpnId_Type(Unsigned32):
    """Custom type ipNatInterfaceStatisticsVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IpNatInterfaceStatisticsVpnId_Type.__name__ = "Unsigned32"
_IpNatInterfaceStatisticsVpnId_Object = MibTableColumn
ipNatInterfaceStatisticsVpnId = _IpNatInterfaceStatisticsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 1),
    _IpNatInterfaceStatisticsVpnId_Type()
)
ipNatInterfaceStatisticsVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsVpnId.setStatus("current")


class _IpNatInterfaceStatisticsIfname_Type(String):
    """Custom type ipNatInterfaceStatisticsIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpNatInterfaceStatisticsIfname_Type.__name__ = "String"
_IpNatInterfaceStatisticsIfname_Object = MibTableColumn
ipNatInterfaceStatisticsIfname = _IpNatInterfaceStatisticsIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 2),
    _IpNatInterfaceStatisticsIfname_Type()
)
ipNatInterfaceStatisticsIfname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsIfname.setStatus("current")
_IpNatInterfaceStatisticsNatOutboundPackets_Type = Counter64
_IpNatInterfaceStatisticsNatOutboundPackets_Object = MibTableColumn
ipNatInterfaceStatisticsNatOutboundPackets = _IpNatInterfaceStatisticsNatOutboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 3),
    _IpNatInterfaceStatisticsNatOutboundPackets_Type()
)
ipNatInterfaceStatisticsNatOutboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatOutboundPackets.setStatus("current")
_IpNatInterfaceStatisticsNatInboundPackets_Type = Counter64
_IpNatInterfaceStatisticsNatInboundPackets_Object = MibTableColumn
ipNatInterfaceStatisticsNatInboundPackets = _IpNatInterfaceStatisticsNatInboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 4),
    _IpNatInterfaceStatisticsNatInboundPackets_Type()
)
ipNatInterfaceStatisticsNatInboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatInboundPackets.setStatus("current")
_IpNatInterfaceStatisticsNatEncodeFail_Type = Counter64
_IpNatInterfaceStatisticsNatEncodeFail_Object = MibTableColumn
ipNatInterfaceStatisticsNatEncodeFail = _IpNatInterfaceStatisticsNatEncodeFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 5),
    _IpNatInterfaceStatisticsNatEncodeFail_Type()
)
ipNatInterfaceStatisticsNatEncodeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatEncodeFail.setStatus("current")
_IpNatInterfaceStatisticsNatDecodeFail_Type = Counter64
_IpNatInterfaceStatisticsNatDecodeFail_Object = MibTableColumn
ipNatInterfaceStatisticsNatDecodeFail = _IpNatInterfaceStatisticsNatDecodeFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 6),
    _IpNatInterfaceStatisticsNatDecodeFail_Type()
)
ipNatInterfaceStatisticsNatDecodeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatDecodeFail.setStatus("current")
_IpNatInterfaceStatisticsNatMapAddFail_Type = Counter64
_IpNatInterfaceStatisticsNatMapAddFail_Object = MibTableColumn
ipNatInterfaceStatisticsNatMapAddFail = _IpNatInterfaceStatisticsNatMapAddFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 7),
    _IpNatInterfaceStatisticsNatMapAddFail_Type()
)
ipNatInterfaceStatisticsNatMapAddFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatMapAddFail.setStatus("current")
_IpNatInterfaceStatisticsNatFilterAddFail_Type = Counter64
_IpNatInterfaceStatisticsNatFilterAddFail_Object = MibTableColumn
ipNatInterfaceStatisticsNatFilterAddFail = _IpNatInterfaceStatisticsNatFilterAddFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 8),
    _IpNatInterfaceStatisticsNatFilterAddFail_Type()
)
ipNatInterfaceStatisticsNatFilterAddFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatFilterAddFail.setStatus("current")
_IpNatInterfaceStatisticsNatFilterLookupFail_Type = Counter64
_IpNatInterfaceStatisticsNatFilterLookupFail_Object = MibTableColumn
ipNatInterfaceStatisticsNatFilterLookupFail = _IpNatInterfaceStatisticsNatFilterLookupFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 9),
    _IpNatInterfaceStatisticsNatFilterLookupFail_Type()
)
ipNatInterfaceStatisticsNatFilterLookupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatFilterLookupFail.setStatus("current")
_IpNatInterfaceStatisticsNatStateCheckFail_Type = Counter64
_IpNatInterfaceStatisticsNatStateCheckFail_Object = MibTableColumn
ipNatInterfaceStatisticsNatStateCheckFail = _IpNatInterfaceStatisticsNatStateCheckFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 10),
    _IpNatInterfaceStatisticsNatStateCheckFail_Type()
)
ipNatInterfaceStatisticsNatStateCheckFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatStateCheckFail.setStatus("current")
_IpNatInterfaceStatisticsNatPolicerDrops_Type = Counter64
_IpNatInterfaceStatisticsNatPolicerDrops_Object = MibTableColumn
ipNatInterfaceStatisticsNatPolicerDrops = _IpNatInterfaceStatisticsNatPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 11),
    _IpNatInterfaceStatisticsNatPolicerDrops_Type()
)
ipNatInterfaceStatisticsNatPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatPolicerDrops.setStatus("current")
_IpNatInterfaceStatisticsOutboundIcmpError_Type = Counter64
_IpNatInterfaceStatisticsOutboundIcmpError_Object = MibTableColumn
ipNatInterfaceStatisticsOutboundIcmpError = _IpNatInterfaceStatisticsOutboundIcmpError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 12),
    _IpNatInterfaceStatisticsOutboundIcmpError_Type()
)
ipNatInterfaceStatisticsOutboundIcmpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsOutboundIcmpError.setStatus("current")
_IpNatInterfaceStatisticsInboundIcmpError_Type = Counter64
_IpNatInterfaceStatisticsInboundIcmpError_Object = MibTableColumn
ipNatInterfaceStatisticsInboundIcmpError = _IpNatInterfaceStatisticsInboundIcmpError_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 13),
    _IpNatInterfaceStatisticsInboundIcmpError_Type()
)
ipNatInterfaceStatisticsInboundIcmpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsInboundIcmpError.setStatus("current")
_IpNatInterfaceStatisticsInboundIcmpErrorDrops_Type = Counter64
_IpNatInterfaceStatisticsInboundIcmpErrorDrops_Object = MibTableColumn
ipNatInterfaceStatisticsInboundIcmpErrorDrops = _IpNatInterfaceStatisticsInboundIcmpErrorDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 14),
    _IpNatInterfaceStatisticsInboundIcmpErrorDrops_Type()
)
ipNatInterfaceStatisticsInboundIcmpErrorDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsInboundIcmpErrorDrops.setStatus("current")
_IpNatInterfaceStatisticsNatFragments_Type = Counter64
_IpNatInterfaceStatisticsNatFragments_Object = MibTableColumn
ipNatInterfaceStatisticsNatFragments = _IpNatInterfaceStatisticsNatFragments_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 15),
    _IpNatInterfaceStatisticsNatFragments_Type()
)
ipNatInterfaceStatisticsNatFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatFragments.setStatus("current")
_IpNatInterfaceStatisticsNatFragmentsFail_Type = Counter64
_IpNatInterfaceStatisticsNatFragmentsFail_Object = MibTableColumn
ipNatInterfaceStatisticsNatFragmentsFail = _IpNatInterfaceStatisticsNatFragmentsFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 16),
    _IpNatInterfaceStatisticsNatFragmentsFail_Type()
)
ipNatInterfaceStatisticsNatFragmentsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatFragmentsFail.setStatus("current")
_IpNatInterfaceStatisticsNatUnsupportedProto_Type = Counter64
_IpNatInterfaceStatisticsNatUnsupportedProto_Object = MibTableColumn
ipNatInterfaceStatisticsNatUnsupportedProto = _IpNatInterfaceStatisticsNatUnsupportedProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 17),
    _IpNatInterfaceStatisticsNatUnsupportedProto_Type()
)
ipNatInterfaceStatisticsNatUnsupportedProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatUnsupportedProto.setStatus("current")
_IpNatInterfaceStatisticsNatMapNoPorts_Type = Counter64
_IpNatInterfaceStatisticsNatMapNoPorts_Object = MibTableColumn
ipNatInterfaceStatisticsNatMapNoPorts = _IpNatInterfaceStatisticsNatMapNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 18),
    _IpNatInterfaceStatisticsNatMapNoPorts_Type()
)
ipNatInterfaceStatisticsNatMapNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatMapNoPorts.setStatus("current")
_IpNatInterfaceStatisticsNatMapCannotXlate_Type = Counter64
_IpNatInterfaceStatisticsNatMapCannotXlate_Object = MibTableColumn
ipNatInterfaceStatisticsNatMapCannotXlate = _IpNatInterfaceStatisticsNatMapCannotXlate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 19),
    _IpNatInterfaceStatisticsNatMapCannotXlate_Type()
)
ipNatInterfaceStatisticsNatMapCannotXlate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatMapCannotXlate.setStatus("current")
_IpNatInterfaceStatisticsNatFilterMapMismatch_Type = Counter64
_IpNatInterfaceStatisticsNatFilterMapMismatch_Object = MibTableColumn
ipNatInterfaceStatisticsNatFilterMapMismatch = _IpNatInterfaceStatisticsNatFilterMapMismatch_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 20),
    _IpNatInterfaceStatisticsNatFilterMapMismatch_Type()
)
ipNatInterfaceStatisticsNatFilterMapMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatFilterMapMismatch.setStatus("current")
_IpNatInterfaceStatisticsNatMapIpPoolExhausted_Type = Counter64
_IpNatInterfaceStatisticsNatMapIpPoolExhausted_Object = MibTableColumn
ipNatInterfaceStatisticsNatMapIpPoolExhausted = _IpNatInterfaceStatisticsNatMapIpPoolExhausted_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 2, 1, 21),
    _IpNatInterfaceStatisticsNatMapIpPoolExhausted_Type()
)
ipNatInterfaceStatisticsNatMapIpPoolExhausted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatInterfaceStatisticsNatMapIpPoolExhausted.setStatus("current")
_IpNatFilterTable_Object = MibTable
ipNatFilterTable = _IpNatFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3)
)
if mibBuilder.loadTexts:
    ipNatFilterTable.setStatus("current")
_IpNatFilterEntry_Object = MibTableRow
ipNatFilterEntry = _IpNatFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1)
)
ipNatFilterEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "ipNatFilterNatVpnId"),
    (0, "VIPTELA-OPER-VPN", "ipNatFilterNatIfname"),
    (0, "VIPTELA-OPER-VPN", "ipNatFilterPrivateVpnId"),
    (0, "VIPTELA-OPER-VPN", "ipNatFilterProto"),
    (0, "VIPTELA-OPER-VPN", "ipNatFilterPrivateSourceAddress"),
    (0, "VIPTELA-OPER-VPN", "ipNatFilterPrivateDestAddress"),
    (0, "VIPTELA-OPER-VPN", "ipNatFilterPrivateSourcePort"),
    (0, "VIPTELA-OPER-VPN", "ipNatFilterPrivateDestPort"),
)
if mibBuilder.loadTexts:
    ipNatFilterEntry.setStatus("current")


class _IpNatFilterNatVpnId_Type(Unsigned32):
    """Custom type ipNatFilterNatVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IpNatFilterNatVpnId_Type.__name__ = "Unsigned32"
_IpNatFilterNatVpnId_Object = MibTableColumn
ipNatFilterNatVpnId = _IpNatFilterNatVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 1),
    _IpNatFilterNatVpnId_Type()
)
ipNatFilterNatVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNatFilterNatVpnId.setStatus("current")


class _IpNatFilterNatIfname_Type(String):
    """Custom type ipNatFilterNatIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpNatFilterNatIfname_Type.__name__ = "String"
_IpNatFilterNatIfname_Object = MibTableColumn
ipNatFilterNatIfname = _IpNatFilterNatIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 2),
    _IpNatFilterNatIfname_Type()
)
ipNatFilterNatIfname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNatFilterNatIfname.setStatus("current")


class _IpNatFilterPrivateVpnId_Type(Unsigned32):
    """Custom type ipNatFilterPrivateVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IpNatFilterPrivateVpnId_Type.__name__ = "Unsigned32"
_IpNatFilterPrivateVpnId_Object = MibTableColumn
ipNatFilterPrivateVpnId = _IpNatFilterPrivateVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 3),
    _IpNatFilterPrivateVpnId_Type()
)
ipNatFilterPrivateVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNatFilterPrivateVpnId.setStatus("current")


class _IpNatFilterProto_Type(Integer32):
    """Custom type ipNatFilterProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("tcp", 6),
          ("udp", 17))
    )


_IpNatFilterProto_Type.__name__ = "Integer32"
_IpNatFilterProto_Object = MibTableColumn
ipNatFilterProto = _IpNatFilterProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 4),
    _IpNatFilterProto_Type()
)
ipNatFilterProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNatFilterProto.setStatus("current")
_IpNatFilterPrivateSourceAddress_Type = IpAddress
_IpNatFilterPrivateSourceAddress_Object = MibTableColumn
ipNatFilterPrivateSourceAddress = _IpNatFilterPrivateSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 5),
    _IpNatFilterPrivateSourceAddress_Type()
)
ipNatFilterPrivateSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNatFilterPrivateSourceAddress.setStatus("current")
_IpNatFilterPrivateDestAddress_Type = IpAddress
_IpNatFilterPrivateDestAddress_Object = MibTableColumn
ipNatFilterPrivateDestAddress = _IpNatFilterPrivateDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 6),
    _IpNatFilterPrivateDestAddress_Type()
)
ipNatFilterPrivateDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNatFilterPrivateDestAddress.setStatus("current")
_IpNatFilterPrivateSourcePort_Type = Unsigned32
_IpNatFilterPrivateSourcePort_Object = MibTableColumn
ipNatFilterPrivateSourcePort = _IpNatFilterPrivateSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 7),
    _IpNatFilterPrivateSourcePort_Type()
)
ipNatFilterPrivateSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNatFilterPrivateSourcePort.setStatus("current")
_IpNatFilterPrivateDestPort_Type = Unsigned32
_IpNatFilterPrivateDestPort_Object = MibTableColumn
ipNatFilterPrivateDestPort = _IpNatFilterPrivateDestPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 8),
    _IpNatFilterPrivateDestPort_Type()
)
ipNatFilterPrivateDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNatFilterPrivateDestPort.setStatus("current")
_IpNatFilterPublicSourceAddress_Type = IpAddress
_IpNatFilterPublicSourceAddress_Object = MibTableColumn
ipNatFilterPublicSourceAddress = _IpNatFilterPublicSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 9),
    _IpNatFilterPublicSourceAddress_Type()
)
ipNatFilterPublicSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatFilterPublicSourceAddress.setStatus("current")
_IpNatFilterPublicDestAddress_Type = IpAddress
_IpNatFilterPublicDestAddress_Object = MibTableColumn
ipNatFilterPublicDestAddress = _IpNatFilterPublicDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 10),
    _IpNatFilterPublicDestAddress_Type()
)
ipNatFilterPublicDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatFilterPublicDestAddress.setStatus("current")
_IpNatFilterPublicSourcePort_Type = Unsigned32
_IpNatFilterPublicSourcePort_Object = MibTableColumn
ipNatFilterPublicSourcePort = _IpNatFilterPublicSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 11),
    _IpNatFilterPublicSourcePort_Type()
)
ipNatFilterPublicSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatFilterPublicSourcePort.setStatus("current")
_IpNatFilterPublicDestPort_Type = Unsigned32
_IpNatFilterPublicDestPort_Object = MibTableColumn
ipNatFilterPublicDestPort = _IpNatFilterPublicDestPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 12),
    _IpNatFilterPublicDestPort_Type()
)
ipNatFilterPublicDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatFilterPublicDestPort.setStatus("current")


class _IpNatFilterFilterState_Type(Integer32):
    """Custom type ipNatFilterFilterState based on Integer32"""
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
        *(("initial", 0),
          ("syn-sent", 1),
          ("syn-ack", 2),
          ("syn-received", 3),
          ("established", 4),
          ("fin-sent", 5),
          ("fin-received", 6),
          ("fin-acked", 7),
          ("closed", 8),
          ("reset", 9))
    )


_IpNatFilterFilterState_Type.__name__ = "Integer32"
_IpNatFilterFilterState_Object = MibTableColumn
ipNatFilterFilterState = _IpNatFilterFilterState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 13),
    _IpNatFilterFilterState_Type()
)
ipNatFilterFilterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatFilterFilterState.setStatus("current")
_IpNatFilterIdleTimeout_Type = String
_IpNatFilterIdleTimeout_Object = MibTableColumn
ipNatFilterIdleTimeout = _IpNatFilterIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 14),
    _IpNatFilterIdleTimeout_Type()
)
ipNatFilterIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatFilterIdleTimeout.setStatus("current")
_IpNatFilterOutboundPackets_Type = Counter64
_IpNatFilterOutboundPackets_Object = MibTableColumn
ipNatFilterOutboundPackets = _IpNatFilterOutboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 15),
    _IpNatFilterOutboundPackets_Type()
)
ipNatFilterOutboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatFilterOutboundPackets.setStatus("current")
_IpNatFilterOutboundOctets_Type = Counter64
_IpNatFilterOutboundOctets_Object = MibTableColumn
ipNatFilterOutboundOctets = _IpNatFilterOutboundOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 16),
    _IpNatFilterOutboundOctets_Type()
)
ipNatFilterOutboundOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatFilterOutboundOctets.setStatus("current")
_IpNatFilterInboundPackets_Type = Counter64
_IpNatFilterInboundPackets_Object = MibTableColumn
ipNatFilterInboundPackets = _IpNatFilterInboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 17),
    _IpNatFilterInboundPackets_Type()
)
ipNatFilterInboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatFilterInboundPackets.setStatus("current")
_IpNatFilterInboundOctets_Type = Counter64
_IpNatFilterInboundOctets_Object = MibTableColumn
ipNatFilterInboundOctets = _IpNatFilterInboundOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 18),
    _IpNatFilterInboundOctets_Type()
)
ipNatFilterInboundOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatFilterInboundOctets.setStatus("current")


class _IpNatFilterDirection_Type(Integer32):
    """Custom type ipNatFilterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inside", 0),
          ("outside", 1))
    )


_IpNatFilterDirection_Type.__name__ = "Integer32"
_IpNatFilterDirection_Object = MibTableColumn
ipNatFilterDirection = _IpNatFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 9, 3, 1, 19),
    _IpNatFilterDirection_Type()
)
ipNatFilterDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatFilterDirection.setStatus("current")
_IpRoutesSummaryTable_Object = MibTable
ipRoutesSummaryTable = _IpRoutesSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 10)
)
if mibBuilder.loadTexts:
    ipRoutesSummaryTable.setStatus("current")
_IpRoutesSummaryEntry_Object = MibTableRow
ipRoutesSummaryEntry = _IpRoutesSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 10, 1)
)
ipRoutesSummaryEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "ipRoutesSummaryVpnId"),
    (0, "VIPTELA-OPER-VPN", "ipRoutesSummaryAddressFamily"),
    (0, "VIPTELA-OPER-VPN", "ipRoutesSummaryRouteProtocol"),
)
if mibBuilder.loadTexts:
    ipRoutesSummaryEntry.setStatus("current")


class _IpRoutesSummaryVpnId_Type(Unsigned32):
    """Custom type ipRoutesSummaryVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_IpRoutesSummaryVpnId_Type.__name__ = "Unsigned32"
_IpRoutesSummaryVpnId_Object = MibTableColumn
ipRoutesSummaryVpnId = _IpRoutesSummaryVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 10, 1, 1),
    _IpRoutesSummaryVpnId_Type()
)
ipRoutesSummaryVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipRoutesSummaryVpnId.setStatus("current")


class _IpRoutesSummaryAddressFamily_Type(Integer32):
    """Custom type ipRoutesSummaryAddressFamily based on Integer32"""
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


_IpRoutesSummaryAddressFamily_Type.__name__ = "Integer32"
_IpRoutesSummaryAddressFamily_Object = MibTableColumn
ipRoutesSummaryAddressFamily = _IpRoutesSummaryAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 10, 1, 2),
    _IpRoutesSummaryAddressFamily_Type()
)
ipRoutesSummaryAddressFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipRoutesSummaryAddressFamily.setStatus("current")


class _IpRoutesSummaryRouteProtocol_Type(Integer32):
    """Custom type ipRoutesSummaryRouteProtocol based on Integer32"""
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
        *(("connected", 0),
          ("static", 1),
          ("ospf", 2),
          ("bgp", 3),
          ("omp", 4),
          ("nat", 5),
          ("gre", 6),
          ("natpoolOmp", 7),
          ("natpoolService", 8))
    )


_IpRoutesSummaryRouteProtocol_Type.__name__ = "Integer32"
_IpRoutesSummaryRouteProtocol_Object = MibTableColumn
ipRoutesSummaryRouteProtocol = _IpRoutesSummaryRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 10, 1, 3),
    _IpRoutesSummaryRouteProtocol_Type()
)
ipRoutesSummaryRouteProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipRoutesSummaryRouteProtocol.setStatus("current")
_IpRoutesSummaryReceived_Type = Unsigned32
_IpRoutesSummaryReceived_Object = MibTableColumn
ipRoutesSummaryReceived = _IpRoutesSummaryReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 10, 1, 4),
    _IpRoutesSummaryReceived_Type()
)
ipRoutesSummaryReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesSummaryReceived.setStatus("current")
_IpRoutesSummaryInstalled_Type = Unsigned32
_IpRoutesSummaryInstalled_Object = MibTableColumn
ipRoutesSummaryInstalled = _IpRoutesSummaryInstalled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 7, 10, 1, 5),
    _IpRoutesSummaryInstalled_Type()
)
ipRoutesSummaryInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesSummaryInstalled.setStatus("current")
_IpMfibOilMcastOilListTable_Object = MibTable
ipMfibOilMcastOilListTable = _IpMfibOilMcastOilListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 8)
)
if mibBuilder.loadTexts:
    ipMfibOilMcastOilListTable.setStatus("current")
_IpMfibOilMcastOilListEntry_Object = MibTableRow
ipMfibOilMcastOilListEntry = _IpMfibOilMcastOilListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 8, 1)
)
ipMfibOilMcastOilListEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "ipMfibOilVpnId"),
    (0, "VIPTELA-OPER-VPN", "ipMfibOilGroup"),
    (0, "VIPTELA-OPER-VPN", "ipMfibOilSource"),
    (0, "VIPTELA-OPER-VPN", "ipMfibOilMcastOilListIndex"),
)
if mibBuilder.loadTexts:
    ipMfibOilMcastOilListEntry.setStatus("current")
_IpMfibOilMcastOilListIndex_Type = Unsigned32
_IpMfibOilMcastOilListIndex_Object = MibTableColumn
ipMfibOilMcastOilListIndex = _IpMfibOilMcastOilListIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 8, 1, 1),
    _IpMfibOilMcastOilListIndex_Type()
)
ipMfibOilMcastOilListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMfibOilMcastOilListIndex.setStatus("current")


class _IpMfibOilMcastOilListOilInterface_Type(String):
    """Custom type ipMfibOilMcastOilListOilInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpMfibOilMcastOilListOilInterface_Type.__name__ = "String"
_IpMfibOilMcastOilListOilInterface_Object = MibTableColumn
ipMfibOilMcastOilListOilInterface = _IpMfibOilMcastOilListOilInterface_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 8, 1, 2),
    _IpMfibOilMcastOilListOilInterface_Type()
)
ipMfibOilMcastOilListOilInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibOilMcastOilListOilInterface.setStatus("current")
_IpMfibOilMcastOilListOilRemoteSystem_Type = InetAddressIP
_IpMfibOilMcastOilListOilRemoteSystem_Object = MibTableColumn
ipMfibOilMcastOilListOilRemoteSystem = _IpMfibOilMcastOilListOilRemoteSystem_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 8, 1, 3),
    _IpMfibOilMcastOilListOilRemoteSystem_Type()
)
ipMfibOilMcastOilListOilRemoteSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMfibOilMcastOilListOilRemoteSystem.setStatus("current")
_VrrpTable_Object = MibTable
vrrpTable = _VrrpTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 9)
)
if mibBuilder.loadTexts:
    vrrpTable.setStatus("current")
_VrrpEntry_Object = MibTableRow
vrrpEntry = _VrrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 9, 1)
)
vrrpEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "vrrpVpnId"),
)
if mibBuilder.loadTexts:
    vrrpEntry.setStatus("current")


class _VrrpVpnId_Type(Unsigned32):
    """Custom type vrrpVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_VrrpVpnId_Type.__name__ = "Unsigned32"
_VrrpVpnId_Object = MibTableColumn
vrrpVpnId = _VrrpVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 9, 1, 1),
    _VrrpVpnId_Type()
)
vrrpVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpVpnId.setStatus("current")
_VrrpInterfacesTable_Object = MibTable
vrrpInterfacesTable = _VrrpInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 10)
)
if mibBuilder.loadTexts:
    vrrpInterfacesTable.setStatus("current")
_VrrpInterfacesEntry_Object = MibTableRow
vrrpInterfacesEntry = _VrrpInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 10, 1)
)
vrrpInterfacesEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "vrrpVpnId"),
    (0, "VIPTELA-OPER-VPN", "vrrpInterfacesIfName"),
)
if mibBuilder.loadTexts:
    vrrpInterfacesEntry.setStatus("current")


class _VrrpInterfacesIfName_Type(String):
    """Custom type vrrpInterfacesIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VrrpInterfacesIfName_Type.__name__ = "String"
_VrrpInterfacesIfName_Object = MibTableColumn
vrrpInterfacesIfName = _VrrpInterfacesIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 10, 1, 1),
    _VrrpInterfacesIfName_Type()
)
vrrpInterfacesIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInterfacesIfName.setStatus("current")
_VrrpInterfacesGroupsTable_Object = MibTable
vrrpInterfacesGroupsTable = _VrrpInterfacesGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 11)
)
if mibBuilder.loadTexts:
    vrrpInterfacesGroupsTable.setStatus("current")
_VrrpInterfacesGroupsEntry_Object = MibTableRow
vrrpInterfacesGroupsEntry = _VrrpInterfacesGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 11, 1)
)
vrrpInterfacesGroupsEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "vrrpVpnId"),
    (0, "VIPTELA-OPER-VPN", "vrrpInterfacesIfName"),
    (0, "VIPTELA-OPER-VPN", "vrrpInterfacesGroupsGroupId"),
)
if mibBuilder.loadTexts:
    vrrpInterfacesGroupsEntry.setStatus("current")


class _VrrpInterfacesGroupsGroupId_Type(UnsignedByte):
    """Custom type vrrpInterfacesGroupsGroupId based on UnsignedByte"""
    subtypeSpec = UnsignedByte.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpInterfacesGroupsGroupId_Type.__name__ = "UnsignedByte"
_VrrpInterfacesGroupsGroupId_Object = MibTableColumn
vrrpInterfacesGroupsGroupId = _VrrpInterfacesGroupsGroupId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 11, 1, 1),
    _VrrpInterfacesGroupsGroupId_Type()
)
vrrpInterfacesGroupsGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpInterfacesGroupsGroupId.setStatus("current")
_VrrpInterfacesGroupsVirtualIp_Type = InetAddressIP
_VrrpInterfacesGroupsVirtualIp_Object = MibTableColumn
vrrpInterfacesGroupsVirtualIp = _VrrpInterfacesGroupsVirtualIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 11, 1, 2),
    _VrrpInterfacesGroupsVirtualIp_Type()
)
vrrpInterfacesGroupsVirtualIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInterfacesGroupsVirtualIp.setStatus("current")
_VrrpInterfacesGroupsVirtualMac_Type = String
_VrrpInterfacesGroupsVirtualMac_Object = MibTableColumn
vrrpInterfacesGroupsVirtualMac = _VrrpInterfacesGroupsVirtualMac_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 11, 1, 3),
    _VrrpInterfacesGroupsVirtualMac_Type()
)
vrrpInterfacesGroupsVirtualMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInterfacesGroupsVirtualMac.setStatus("current")
_VrrpInterfacesGroupsPriority_Type = UnsignedByte
_VrrpInterfacesGroupsPriority_Object = MibTableColumn
vrrpInterfacesGroupsPriority = _VrrpInterfacesGroupsPriority_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 11, 1, 4),
    _VrrpInterfacesGroupsPriority_Type()
)
vrrpInterfacesGroupsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInterfacesGroupsPriority.setStatus("current")


class _VrrpInterfacesGroupsVrrpState_Type(Integer32):
    """Custom type vrrpInterfacesGroupsVrrpState based on Integer32"""
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


_VrrpInterfacesGroupsVrrpState_Type.__name__ = "Integer32"
_VrrpInterfacesGroupsVrrpState_Object = MibTableColumn
vrrpInterfacesGroupsVrrpState = _VrrpInterfacesGroupsVrrpState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 11, 1, 5),
    _VrrpInterfacesGroupsVrrpState_Type()
)
vrrpInterfacesGroupsVrrpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInterfacesGroupsVrrpState.setStatus("current")


class _VrrpInterfacesGroupsOmpState_Type(Integer32):
    """Custom type vrrpInterfacesGroupsOmpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_VrrpInterfacesGroupsOmpState_Type.__name__ = "Integer32"
_VrrpInterfacesGroupsOmpState_Object = MibTableColumn
vrrpInterfacesGroupsOmpState = _VrrpInterfacesGroupsOmpState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 11, 1, 6),
    _VrrpInterfacesGroupsOmpState_Type()
)
vrrpInterfacesGroupsOmpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInterfacesGroupsOmpState.setStatus("current")
_VrrpInterfacesGroupsAdvertisementTimer_Type = Integer32
_VrrpInterfacesGroupsAdvertisementTimer_Object = MibTableColumn
vrrpInterfacesGroupsAdvertisementTimer = _VrrpInterfacesGroupsAdvertisementTimer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 11, 1, 7),
    _VrrpInterfacesGroupsAdvertisementTimer_Type()
)
vrrpInterfacesGroupsAdvertisementTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInterfacesGroupsAdvertisementTimer.setStatus("current")
_VrrpInterfacesGroupsMasterDownTimer_Type = Integer32
_VrrpInterfacesGroupsMasterDownTimer_Object = MibTableColumn
vrrpInterfacesGroupsMasterDownTimer = _VrrpInterfacesGroupsMasterDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 11, 1, 8),
    _VrrpInterfacesGroupsMasterDownTimer_Type()
)
vrrpInterfacesGroupsMasterDownTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInterfacesGroupsMasterDownTimer.setStatus("current")
_VrrpInterfacesGroupsLastStateChangeTime_Type = DateAndTime
_VrrpInterfacesGroupsLastStateChangeTime_Object = MibTableColumn
vrrpInterfacesGroupsLastStateChangeTime = _VrrpInterfacesGroupsLastStateChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 11, 1, 9),
    _VrrpInterfacesGroupsLastStateChangeTime_Type()
)
vrrpInterfacesGroupsLastStateChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInterfacesGroupsLastStateChangeTime.setStatus("current")


class _VrrpInterfacesGroupsTrackPrefixList_Type(String):
    """Custom type vrrpInterfacesGroupsTrackPrefixList based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VrrpInterfacesGroupsTrackPrefixList_Type.__name__ = "String"
_VrrpInterfacesGroupsTrackPrefixList_Object = MibTableColumn
vrrpInterfacesGroupsTrackPrefixList = _VrrpInterfacesGroupsTrackPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 11, 1, 10),
    _VrrpInterfacesGroupsTrackPrefixList_Type()
)
vrrpInterfacesGroupsTrackPrefixList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInterfacesGroupsTrackPrefixList.setStatus("current")


class _VrrpInterfacesGroupsPrefixListState_Type(Integer32):
    """Custom type vrrpInterfacesGroupsPrefixListState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("resolved", 0),
          ("unresolved", 1))
    )


_VrrpInterfacesGroupsPrefixListState_Type.__name__ = "Integer32"
_VrrpInterfacesGroupsPrefixListState_Object = MibTableColumn
vrrpInterfacesGroupsPrefixListState = _VrrpInterfacesGroupsPrefixListState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 11, 1, 11),
    _VrrpInterfacesGroupsPrefixListState_Type()
)
vrrpInterfacesGroupsPrefixListState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInterfacesGroupsPrefixListState.setStatus("current")
_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 12)
)
_DhcpInterfaceTable_Object = MibTable
dhcpInterfaceTable = _DhcpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 12, 1)
)
if mibBuilder.loadTexts:
    dhcpInterfaceTable.setStatus("current")
_DhcpInterfaceEntry_Object = MibTableRow
dhcpInterfaceEntry = _DhcpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 12, 1, 1)
)
dhcpInterfaceEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "dhcpInterfaceVpnId"),
    (0, "VIPTELA-OPER-VPN", "dhcpInterfaceIfname"),
)
if mibBuilder.loadTexts:
    dhcpInterfaceEntry.setStatus("current")


class _DhcpInterfaceVpnId_Type(Unsigned32):
    """Custom type dhcpInterfaceVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_DhcpInterfaceVpnId_Type.__name__ = "Unsigned32"
_DhcpInterfaceVpnId_Object = MibTableColumn
dhcpInterfaceVpnId = _DhcpInterfaceVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 12, 1, 1, 1),
    _DhcpInterfaceVpnId_Type()
)
dhcpInterfaceVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpInterfaceVpnId.setStatus("current")


class _DhcpInterfaceIfname_Type(String):
    """Custom type dhcpInterfaceIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DhcpInterfaceIfname_Type.__name__ = "String"
_DhcpInterfaceIfname_Object = MibTableColumn
dhcpInterfaceIfname = _DhcpInterfaceIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 12, 1, 1, 2),
    _DhcpInterfaceIfname_Type()
)
dhcpInterfaceIfname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpInterfaceIfname.setStatus("current")


class _DhcpInterfaceState_Type(Integer32):
    """Custom type dhcpInterfaceState based on Integer32"""
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
        *(("init", 0),
          ("request", 1),
          ("bound", 2),
          ("renew", 3),
          ("rebind", 4),
          ("release", 5),
          ("dynamic-ip", 6))
    )


_DhcpInterfaceState_Type.__name__ = "Integer32"
_DhcpInterfaceState_Object = MibTableColumn
dhcpInterfaceState = _DhcpInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 12, 1, 1, 3),
    _DhcpInterfaceState_Type()
)
dhcpInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpInterfaceState.setStatus("current")
_DhcpInterfaceAcquiredIp_Type = Ipv4Prefix
_DhcpInterfaceAcquiredIp_Object = MibTableColumn
dhcpInterfaceAcquiredIp = _DhcpInterfaceAcquiredIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 12, 1, 1, 4),
    _DhcpInterfaceAcquiredIp_Type()
)
dhcpInterfaceAcquiredIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpInterfaceAcquiredIp.setStatus("current")
_DhcpInterfaceServer_Type = IpAddress
_DhcpInterfaceServer_Object = MibTableColumn
dhcpInterfaceServer = _DhcpInterfaceServer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 12, 1, 1, 5),
    _DhcpInterfaceServer_Type()
)
dhcpInterfaceServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpInterfaceServer.setStatus("current")
_DhcpInterfaceLeaseTime_Type = String
_DhcpInterfaceLeaseTime_Object = MibTableColumn
dhcpInterfaceLeaseTime = _DhcpInterfaceLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 12, 1, 1, 6),
    _DhcpInterfaceLeaseTime_Type()
)
dhcpInterfaceLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpInterfaceLeaseTime.setStatus("current")
_DhcpInterfaceTimeRemaining_Type = String
_DhcpInterfaceTimeRemaining_Object = MibTableColumn
dhcpInterfaceTimeRemaining = _DhcpInterfaceTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 12, 1, 1, 7),
    _DhcpInterfaceTimeRemaining_Type()
)
dhcpInterfaceTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpInterfaceTimeRemaining.setStatus("current")
_DhcpInterfaceGateway_Type = IpAddress
_DhcpInterfaceGateway_Object = MibTableColumn
dhcpInterfaceGateway = _DhcpInterfaceGateway_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 12, 1, 1, 8),
    _DhcpInterfaceGateway_Type()
)
dhcpInterfaceGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpInterfaceGateway.setStatus("current")
_DhcpServerTable_Object = MibTable
dhcpServerTable = _DhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 12, 2)
)
if mibBuilder.loadTexts:
    dhcpServerTable.setStatus("current")
_DhcpServerEntry_Object = MibTableRow
dhcpServerEntry = _DhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 12, 2, 1)
)
dhcpServerEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "dhcpServerVpnId"),
    (0, "VIPTELA-OPER-VPN", "dhcpServerIfname"),
)
if mibBuilder.loadTexts:
    dhcpServerEntry.setStatus("current")


class _DhcpServerVpnId_Type(Unsigned32):
    """Custom type dhcpServerVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_DhcpServerVpnId_Type.__name__ = "Unsigned32"
_DhcpServerVpnId_Object = MibTableColumn
dhcpServerVpnId = _DhcpServerVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 12, 2, 1, 1),
    _DhcpServerVpnId_Type()
)
dhcpServerVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpServerVpnId.setStatus("current")


class _DhcpServerIfname_Type(String):
    """Custom type dhcpServerIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DhcpServerIfname_Type.__name__ = "String"
_DhcpServerIfname_Object = MibTableColumn
dhcpServerIfname = _DhcpServerIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 12, 2, 1, 2),
    _DhcpServerIfname_Type()
)
dhcpServerIfname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerIfname.setStatus("current")
_DhcpInterfaceDnsListTable_Object = MibTable
dhcpInterfaceDnsListTable = _DhcpInterfaceDnsListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 13)
)
if mibBuilder.loadTexts:
    dhcpInterfaceDnsListTable.setStatus("current")
_DhcpInterfaceDnsListEntry_Object = MibTableRow
dhcpInterfaceDnsListEntry = _DhcpInterfaceDnsListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 13, 1)
)
dhcpInterfaceDnsListEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "dhcpInterfaceVpnId"),
    (0, "VIPTELA-OPER-VPN", "dhcpInterfaceIfname"),
    (0, "VIPTELA-OPER-VPN", "dhcpInterfaceDnsListIndex"),
)
if mibBuilder.loadTexts:
    dhcpInterfaceDnsListEntry.setStatus("current")
_DhcpInterfaceDnsListIndex_Type = Unsigned32
_DhcpInterfaceDnsListIndex_Object = MibTableColumn
dhcpInterfaceDnsListIndex = _DhcpInterfaceDnsListIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 13, 1, 1),
    _DhcpInterfaceDnsListIndex_Type()
)
dhcpInterfaceDnsListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpInterfaceDnsListIndex.setStatus("current")
_DhcpInterfaceDnsListDns_Type = IpAddress
_DhcpInterfaceDnsListDns_Object = MibTableColumn
dhcpInterfaceDnsListDns = _DhcpInterfaceDnsListDns_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 13, 1, 2),
    _DhcpInterfaceDnsListDns_Type()
)
dhcpInterfaceDnsListDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpInterfaceDnsListDns.setStatus("current")
_DhcpServerBindingsTable_Object = MibTable
dhcpServerBindingsTable = _DhcpServerBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 14)
)
if mibBuilder.loadTexts:
    dhcpServerBindingsTable.setStatus("current")
_DhcpServerBindingsEntry_Object = MibTableRow
dhcpServerBindingsEntry = _DhcpServerBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 14, 1)
)
dhcpServerBindingsEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "dhcpServerVpnId"),
    (0, "VIPTELA-OPER-VPN", "dhcpServerIfname"),
    (1, "VIPTELA-OPER-VPN", "dhcpServerBindingsClientMac"),
)
if mibBuilder.loadTexts:
    dhcpServerBindingsEntry.setStatus("current")


class _DhcpServerBindingsClientMac_Type(String):
    """Custom type dhcpServerBindingsClientMac based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DhcpServerBindingsClientMac_Type.__name__ = "String"
_DhcpServerBindingsClientMac_Object = MibTableColumn
dhcpServerBindingsClientMac = _DhcpServerBindingsClientMac_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 14, 1, 1),
    _DhcpServerBindingsClientMac_Type()
)
dhcpServerBindingsClientMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpServerBindingsClientMac.setStatus("current")
_DhcpServerBindingsClientIp_Type = IpAddress
_DhcpServerBindingsClientIp_Object = MibTableColumn
dhcpServerBindingsClientIp = _DhcpServerBindingsClientIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 14, 1, 2),
    _DhcpServerBindingsClientIp_Type()
)
dhcpServerBindingsClientIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerBindingsClientIp.setStatus("current")
_DhcpServerBindingsLeaseTime_Type = String
_DhcpServerBindingsLeaseTime_Object = MibTableColumn
dhcpServerBindingsLeaseTime = _DhcpServerBindingsLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 14, 1, 3),
    _DhcpServerBindingsLeaseTime_Type()
)
dhcpServerBindingsLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerBindingsLeaseTime.setStatus("current")
_DhcpServerBindingsLeaseTimeRemaining_Type = String
_DhcpServerBindingsLeaseTimeRemaining_Object = MibTableColumn
dhcpServerBindingsLeaseTimeRemaining = _DhcpServerBindingsLeaseTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 14, 1, 4),
    _DhcpServerBindingsLeaseTimeRemaining_Type()
)
dhcpServerBindingsLeaseTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerBindingsLeaseTimeRemaining.setStatus("current")
_DhcpServerBindingsStaticBinding_Type = TruthValue
_DhcpServerBindingsStaticBinding_Object = MibTableColumn
dhcpServerBindingsStaticBinding = _DhcpServerBindingsStaticBinding_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 14, 1, 5),
    _DhcpServerBindingsStaticBinding_Type()
)
dhcpServerBindingsStaticBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerBindingsStaticBinding.setStatus("current")
_DhcpServerBindingsHostName_Type = String
_DhcpServerBindingsHostName_Object = MibTableColumn
dhcpServerBindingsHostName = _DhcpServerBindingsHostName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 14, 1, 6),
    _DhcpServerBindingsHostName_Type()
)
dhcpServerBindingsHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerBindingsHostName.setStatus("current")
_Pppoe_ObjectIdentity = ObjectIdentity
pppoe = _Pppoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15)
)
_PppoeSessionTable_Object = MibTable
pppoeSessionTable = _PppoeSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 1)
)
if mibBuilder.loadTexts:
    pppoeSessionTable.setStatus("current")
_PppoeSessionEntry_Object = MibTableRow
pppoeSessionEntry = _PppoeSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 1, 1)
)
pppoeSessionEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "pppoeSessionVpnId"),
    (0, "VIPTELA-OPER-VPN", "pppoeSessionIfname"),
)
if mibBuilder.loadTexts:
    pppoeSessionEntry.setStatus("current")


class _PppoeSessionVpnId_Type(Unsigned32):
    """Custom type pppoeSessionVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_PppoeSessionVpnId_Type.__name__ = "Unsigned32"
_PppoeSessionVpnId_Object = MibTableColumn
pppoeSessionVpnId = _PppoeSessionVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 1, 1, 2),
    _PppoeSessionVpnId_Type()
)
pppoeSessionVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppoeSessionVpnId.setStatus("current")


class _PppoeSessionIfname_Type(String):
    """Custom type pppoeSessionIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PppoeSessionIfname_Type.__name__ = "String"
_PppoeSessionIfname_Object = MibTableColumn
pppoeSessionIfname = _PppoeSessionIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 1, 1, 3),
    _PppoeSessionIfname_Type()
)
pppoeSessionIfname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppoeSessionIfname.setStatus("current")
_PppoeSessionSessionId_Type = Unsigned32
_PppoeSessionSessionId_Object = MibTableColumn
pppoeSessionSessionId = _PppoeSessionSessionId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 1, 1, 4),
    _PppoeSessionSessionId_Type()
)
pppoeSessionSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeSessionSessionId.setStatus("current")
_PppoeSessionServerMac_Type = String
_PppoeSessionServerMac_Object = MibTableColumn
pppoeSessionServerMac = _PppoeSessionServerMac_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 1, 1, 5),
    _PppoeSessionServerMac_Type()
)
pppoeSessionServerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeSessionServerMac.setStatus("current")
_PppoeSessionLocalMac_Type = String
_PppoeSessionLocalMac_Object = MibTableColumn
pppoeSessionLocalMac = _PppoeSessionLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 1, 1, 6),
    _PppoeSessionLocalMac_Type()
)
pppoeSessionLocalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeSessionLocalMac.setStatus("current")


class _PppoeSessionPppInterface_Type(String):
    """Custom type pppoeSessionPppInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PppoeSessionPppInterface_Type.__name__ = "String"
_PppoeSessionPppInterface_Object = MibTableColumn
pppoeSessionPppInterface = _PppoeSessionPppInterface_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 1, 1, 7),
    _PppoeSessionPppInterface_Type()
)
pppoeSessionPppInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeSessionPppInterface.setStatus("current")


class _PppoeSessionAcName_Type(String):
    """Custom type pppoeSessionAcName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PppoeSessionAcName_Type.__name__ = "String"
_PppoeSessionAcName_Object = MibTableColumn
pppoeSessionAcName = _PppoeSessionAcName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 1, 1, 8),
    _PppoeSessionAcName_Type()
)
pppoeSessionAcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeSessionAcName.setStatus("current")


class _PppoeSessionServiceName_Type(String):
    """Custom type pppoeSessionServiceName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PppoeSessionServiceName_Type.__name__ = "String"
_PppoeSessionServiceName_Object = MibTableColumn
pppoeSessionServiceName = _PppoeSessionServiceName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 1, 1, 9),
    _PppoeSessionServiceName_Type()
)
pppoeSessionServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeSessionServiceName.setStatus("current")
_PppoeStatistics_ObjectIdentity = ObjectIdentity
pppoeStatistics = _PppoeStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 10)
)
_PppoeStatisticsPppoeTxPkts_Type = ConfdString
_PppoeStatisticsPppoeTxPkts_Object = MibScalar
pppoeStatisticsPppoeTxPkts = _PppoeStatisticsPppoeTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 10, 1),
    _PppoeStatisticsPppoeTxPkts_Type()
)
pppoeStatisticsPppoeTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeStatisticsPppoeTxPkts.setStatus("current")
_PppoeStatisticsPppoeRxPkts_Type = ConfdString
_PppoeStatisticsPppoeRxPkts_Object = MibScalar
pppoeStatisticsPppoeRxPkts = _PppoeStatisticsPppoeRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 10, 2),
    _PppoeStatisticsPppoeRxPkts_Type()
)
pppoeStatisticsPppoeRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeStatisticsPppoeRxPkts.setStatus("current")
_PppoeStatisticsPppoeTxSessionDrops_Type = Unsigned32
_PppoeStatisticsPppoeTxSessionDrops_Object = MibScalar
pppoeStatisticsPppoeTxSessionDrops = _PppoeStatisticsPppoeTxSessionDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 10, 3),
    _PppoeStatisticsPppoeTxSessionDrops_Type()
)
pppoeStatisticsPppoeTxSessionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeStatisticsPppoeTxSessionDrops.setStatus("current")
_PppoeStatisticsPppoeRxSessionDrops_Type = Unsigned32
_PppoeStatisticsPppoeRxSessionDrops_Object = MibScalar
pppoeStatisticsPppoeRxSessionDrops = _PppoeStatisticsPppoeRxSessionDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 10, 4),
    _PppoeStatisticsPppoeRxSessionDrops_Type()
)
pppoeStatisticsPppoeRxSessionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeStatisticsPppoeRxSessionDrops.setStatus("current")
_PppoeStatisticsPppoeLcpPkts_Type = Unsigned32
_PppoeStatisticsPppoeLcpPkts_Object = MibScalar
pppoeStatisticsPppoeLcpPkts = _PppoeStatisticsPppoeLcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 10, 5),
    _PppoeStatisticsPppoeLcpPkts_Type()
)
pppoeStatisticsPppoeLcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeStatisticsPppoeLcpPkts.setStatus("current")
_PppoeStatisticsPppoeIpcpPkts_Type = Unsigned32
_PppoeStatisticsPppoeIpcpPkts_Object = MibScalar
pppoeStatisticsPppoeIpcpPkts = _PppoeStatisticsPppoeIpcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 10, 6),
    _PppoeStatisticsPppoeIpcpPkts_Type()
)
pppoeStatisticsPppoeIpcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeStatisticsPppoeIpcpPkts.setStatus("current")
_PppoeStatisticsPppoeCcpPkts_Type = Unsigned32
_PppoeStatisticsPppoeCcpPkts_Object = MibScalar
pppoeStatisticsPppoeCcpPkts = _PppoeStatisticsPppoeCcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 10, 7),
    _PppoeStatisticsPppoeCcpPkts_Type()
)
pppoeStatisticsPppoeCcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeStatisticsPppoeCcpPkts.setStatus("current")
_PppoeStatisticsPppoeInvDiscoveryPkts_Type = Unsigned32
_PppoeStatisticsPppoeInvDiscoveryPkts_Object = MibScalar
pppoeStatisticsPppoeInvDiscoveryPkts = _PppoeStatisticsPppoeInvDiscoveryPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 10, 8),
    _PppoeStatisticsPppoeInvDiscoveryPkts_Type()
)
pppoeStatisticsPppoeInvDiscoveryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeStatisticsPppoeInvDiscoveryPkts.setStatus("current")
_PppoeStatisticsPppoePadiPkts_Type = Unsigned32
_PppoeStatisticsPppoePadiPkts_Object = MibScalar
pppoeStatisticsPppoePadiPkts = _PppoeStatisticsPppoePadiPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 10, 9),
    _PppoeStatisticsPppoePadiPkts_Type()
)
pppoeStatisticsPppoePadiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeStatisticsPppoePadiPkts.setStatus("current")
_PppoeStatisticsPppoePadoPkts_Type = Unsigned32
_PppoeStatisticsPppoePadoPkts_Object = MibScalar
pppoeStatisticsPppoePadoPkts = _PppoeStatisticsPppoePadoPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 10, 10),
    _PppoeStatisticsPppoePadoPkts_Type()
)
pppoeStatisticsPppoePadoPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeStatisticsPppoePadoPkts.setStatus("current")
_PppoeStatisticsPppoePadrPkts_Type = Unsigned32
_PppoeStatisticsPppoePadrPkts_Object = MibScalar
pppoeStatisticsPppoePadrPkts = _PppoeStatisticsPppoePadrPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 10, 11),
    _PppoeStatisticsPppoePadrPkts_Type()
)
pppoeStatisticsPppoePadrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeStatisticsPppoePadrPkts.setStatus("current")
_PppoeStatisticsPppoePadsPkts_Type = Unsigned32
_PppoeStatisticsPppoePadsPkts_Object = MibScalar
pppoeStatisticsPppoePadsPkts = _PppoeStatisticsPppoePadsPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 10, 12),
    _PppoeStatisticsPppoePadsPkts_Type()
)
pppoeStatisticsPppoePadsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeStatisticsPppoePadsPkts.setStatus("current")
_PppoeStatisticsPppoePadtPkts_Type = Unsigned32
_PppoeStatisticsPppoePadtPkts_Object = MibScalar
pppoeStatisticsPppoePadtPkts = _PppoeStatisticsPppoePadtPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 15, 10, 13),
    _PppoeStatisticsPppoePadtPkts_Type()
)
pppoeStatisticsPppoePadtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeStatisticsPppoePadtPkts.setStatus("current")
_Ppp_ObjectIdentity = ObjectIdentity
ppp = _Ppp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 16)
)
_PppInterfaceTable_Object = MibTable
pppInterfaceTable = _PppInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 16, 1)
)
if mibBuilder.loadTexts:
    pppInterfaceTable.setStatus("current")
_PppInterfaceEntry_Object = MibTableRow
pppInterfaceEntry = _PppInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 16, 1, 1)
)
pppInterfaceEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "pppInterfaceVpnId"),
    (0, "VIPTELA-OPER-VPN", "pppInterfaceIfname"),
)
if mibBuilder.loadTexts:
    pppInterfaceEntry.setStatus("current")


class _PppInterfaceVpnId_Type(Unsigned32):
    """Custom type pppInterfaceVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_PppInterfaceVpnId_Type.__name__ = "Unsigned32"
_PppInterfaceVpnId_Object = MibTableColumn
pppInterfaceVpnId = _PppInterfaceVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 16, 1, 1, 2),
    _PppInterfaceVpnId_Type()
)
pppInterfaceVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppInterfaceVpnId.setStatus("current")


class _PppInterfaceIfname_Type(String):
    """Custom type pppInterfaceIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PppInterfaceIfname_Type.__name__ = "String"
_PppInterfaceIfname_Object = MibTableColumn
pppInterfaceIfname = _PppInterfaceIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 16, 1, 1, 3),
    _PppInterfaceIfname_Type()
)
pppInterfaceIfname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppInterfaceIfname.setStatus("current")


class _PppInterfacePppoeInterface_Type(String):
    """Custom type pppInterfacePppoeInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PppInterfacePppoeInterface_Type.__name__ = "String"
_PppInterfacePppoeInterface_Object = MibTableColumn
pppInterfacePppoeInterface = _PppInterfacePppoeInterface_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 16, 1, 1, 4),
    _PppInterfacePppoeInterface_Type()
)
pppInterfacePppoeInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppInterfacePppoeInterface.setStatus("current")


class _PppInterfaceInterfaceIp_Type(String):
    """Custom type pppInterfaceInterfaceIp based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PppInterfaceInterfaceIp_Type.__name__ = "String"
_PppInterfaceInterfaceIp_Object = MibTableColumn
pppInterfaceInterfaceIp = _PppInterfaceInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 16, 1, 1, 5),
    _PppInterfaceInterfaceIp_Type()
)
pppInterfaceInterfaceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppInterfaceInterfaceIp.setStatus("current")


class _PppInterfaceGatewayIp_Type(String):
    """Custom type pppInterfaceGatewayIp based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PppInterfaceGatewayIp_Type.__name__ = "String"
_PppInterfaceGatewayIp_Object = MibTableColumn
pppInterfaceGatewayIp = _PppInterfaceGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 16, 1, 1, 6),
    _PppInterfaceGatewayIp_Type()
)
pppInterfaceGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppInterfaceGatewayIp.setStatus("current")


class _PppInterfacePrimaryDns_Type(String):
    """Custom type pppInterfacePrimaryDns based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PppInterfacePrimaryDns_Type.__name__ = "String"
_PppInterfacePrimaryDns_Object = MibTableColumn
pppInterfacePrimaryDns = _PppInterfacePrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 16, 1, 1, 7),
    _PppInterfacePrimaryDns_Type()
)
pppInterfacePrimaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppInterfacePrimaryDns.setStatus("current")


class _PppInterfaceSecondaryDns_Type(String):
    """Custom type pppInterfaceSecondaryDns based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PppInterfaceSecondaryDns_Type.__name__ = "String"
_PppInterfaceSecondaryDns_Object = MibTableColumn
pppInterfaceSecondaryDns = _PppInterfaceSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 16, 1, 1, 8),
    _PppInterfaceSecondaryDns_Type()
)
pppInterfaceSecondaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppInterfaceSecondaryDns.setStatus("current")
_PppInterfaceMtu_Type = Integer32
_PppInterfaceMtu_Object = MibTableColumn
pppInterfaceMtu = _PppInterfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 16, 1, 1, 9),
    _PppInterfaceMtu_Type()
)
pppInterfaceMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppInterfaceMtu.setStatus("current")
_PppInterfaceAuthType_Type = PppInterfaceAuthEnum
_PppInterfaceAuthType_Object = MibTableColumn
pppInterfaceAuthType = _PppInterfaceAuthType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 16, 1, 1, 10),
    _PppInterfaceAuthType_Type()
)
pppInterfaceAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppInterfaceAuthType.setStatus("current")
_Sfp_ObjectIdentity = ObjectIdentity
sfp = _Sfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17)
)
_SfpDetailTable_Object = MibTable
sfpDetailTable = _SfpDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1)
)
if mibBuilder.loadTexts:
    sfpDetailTable.setStatus("current")
_SfpDetailEntry_Object = MibTableRow
sfpDetailEntry = _SfpDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1)
)
sfpDetailEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "sfpDetailIfname"),
)
if mibBuilder.loadTexts:
    sfpDetailEntry.setStatus("current")


class _SfpDetailIfname_Type(String):
    """Custom type sfpDetailIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SfpDetailIfname_Type.__name__ = "String"
_SfpDetailIfname_Object = MibTableColumn
sfpDetailIfname = _SfpDetailIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 1),
    _SfpDetailIfname_Type()
)
sfpDetailIfname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sfpDetailIfname.setStatus("current")
_SfpDetailPresent_Type = Yesno
_SfpDetailPresent_Object = MibTableColumn
sfpDetailPresent = _SfpDetailPresent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 2),
    _SfpDetailPresent_Type()
)
sfpDetailPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailPresent.setStatus("current")
_SfpDetailPhysicalIdentifier_Type = SfpPhysicalIdentifierEnum
_SfpDetailPhysicalIdentifier_Object = MibTableColumn
sfpDetailPhysicalIdentifier = _SfpDetailPhysicalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 3),
    _SfpDetailPhysicalIdentifier_Type()
)
sfpDetailPhysicalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailPhysicalIdentifier.setStatus("current")
_SfpDetailConnectorType_Type = SfpConnectorTypeEnum
_SfpDetailConnectorType_Object = MibTableColumn
sfpDetailConnectorType = _SfpDetailConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 4),
    _SfpDetailConnectorType_Type()
)
sfpDetailConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailConnectorType.setStatus("current")
_SfpDetailTransceiverCompliancePri_Type = SfpTransceiverComplianceEnum
_SfpDetailTransceiverCompliancePri_Object = MibTableColumn
sfpDetailTransceiverCompliancePri = _SfpDetailTransceiverCompliancePri_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 5),
    _SfpDetailTransceiverCompliancePri_Type()
)
sfpDetailTransceiverCompliancePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailTransceiverCompliancePri.setStatus("current")
_SfpDetailTransceiverComplianceSec_Type = SfpTransceiverComplianceEnum
_SfpDetailTransceiverComplianceSec_Object = MibTableColumn
sfpDetailTransceiverComplianceSec = _SfpDetailTransceiverComplianceSec_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 6),
    _SfpDetailTransceiverComplianceSec_Type()
)
sfpDetailTransceiverComplianceSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailTransceiverComplianceSec.setStatus("current")
_SfpDetailEncoding_Type = SfpEncodingEnum
_SfpDetailEncoding_Object = MibTableColumn
sfpDetailEncoding = _SfpDetailEncoding_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 7),
    _SfpDetailEncoding_Type()
)
sfpDetailEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailEncoding.setStatus("current")
_SfpDetailNominalSpeed_Type = ConfdString
_SfpDetailNominalSpeed_Object = MibTableColumn
sfpDetailNominalSpeed = _SfpDetailNominalSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 8),
    _SfpDetailNominalSpeed_Type()
)
sfpDetailNominalSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailNominalSpeed.setStatus("current")
_SfpDetailRateSelectOptions_Type = SfpRateSelectEnum
_SfpDetailRateSelectOptions_Object = MibTableColumn
sfpDetailRateSelectOptions = _SfpDetailRateSelectOptions_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 9),
    _SfpDetailRateSelectOptions_Type()
)
sfpDetailRateSelectOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailRateSelectOptions.setStatus("current")
_SfpDetailLengthSingleModeKm_Type = Unsigned32
_SfpDetailLengthSingleModeKm_Object = MibTableColumn
sfpDetailLengthSingleModeKm = _SfpDetailLengthSingleModeKm_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 10),
    _SfpDetailLengthSingleModeKm_Type()
)
sfpDetailLengthSingleModeKm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailLengthSingleModeKm.setStatus("current")
_SfpDetailLength625umOm1_Type = Unsigned32
_SfpDetailLength625umOm1_Object = MibTableColumn
sfpDetailLength625umOm1 = _SfpDetailLength625umOm1_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 11),
    _SfpDetailLength625umOm1_Type()
)
sfpDetailLength625umOm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailLength625umOm1.setStatus("current")
_SfpDetailLength50umOm2_Type = Unsigned32
_SfpDetailLength50umOm2_Object = MibTableColumn
sfpDetailLength50umOm2 = _SfpDetailLength50umOm2_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 12),
    _SfpDetailLength50umOm2_Type()
)
sfpDetailLength50umOm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailLength50umOm2.setStatus("current")
_SfpDetailCopperMinLength_Type = Unsigned32
_SfpDetailCopperMinLength_Object = MibTableColumn
sfpDetailCopperMinLength = _SfpDetailCopperMinLength_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 13),
    _SfpDetailCopperMinLength_Type()
)
sfpDetailCopperMinLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailCopperMinLength.setStatus("current")
_SfpDetailLength50umOm3_Type = Unsigned32
_SfpDetailLength50umOm3_Object = MibTableColumn
sfpDetailLength50umOm3 = _SfpDetailLength50umOm3_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 14),
    _SfpDetailLength50umOm3_Type()
)
sfpDetailLength50umOm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailLength50umOm3.setStatus("current")
_SfpDetailLength50umOm4_Type = Unsigned32
_SfpDetailLength50umOm4_Object = MibTableColumn
sfpDetailLength50umOm4 = _SfpDetailLength50umOm4_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 15),
    _SfpDetailLength50umOm4_Type()
)
sfpDetailLength50umOm4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailLength50umOm4.setStatus("current")
_SfpDetailLaserWavelength_Type = Unsigned32
_SfpDetailLaserWavelength_Object = MibTableColumn
sfpDetailLaserWavelength = _SfpDetailLaserWavelength_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 16),
    _SfpDetailLaserWavelength_Type()
)
sfpDetailLaserWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailLaserWavelength.setStatus("current")
_SfpDetailVendorName_Type = String
_SfpDetailVendorName_Object = MibTableColumn
sfpDetailVendorName = _SfpDetailVendorName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 17),
    _SfpDetailVendorName_Type()
)
sfpDetailVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailVendorName.setStatus("current")
_SfpDetailVendorOui_Type = HexList
_SfpDetailVendorOui_Object = MibTableColumn
sfpDetailVendorOui = _SfpDetailVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 18),
    _SfpDetailVendorOui_Type()
)
sfpDetailVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailVendorOui.setStatus("current")
_SfpDetailVendorPartNumber_Type = String
_SfpDetailVendorPartNumber_Object = MibTableColumn
sfpDetailVendorPartNumber = _SfpDetailVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 19),
    _SfpDetailVendorPartNumber_Type()
)
sfpDetailVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailVendorPartNumber.setStatus("current")
_SfpDetailVendorRevision_Type = String
_SfpDetailVendorRevision_Object = MibTableColumn
sfpDetailVendorRevision = _SfpDetailVendorRevision_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 20),
    _SfpDetailVendorRevision_Type()
)
sfpDetailVendorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailVendorRevision.setStatus("current")
_SfpDetailVendorSerialNumber_Type = String
_SfpDetailVendorSerialNumber_Object = MibTableColumn
sfpDetailVendorSerialNumber = _SfpDetailVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 21),
    _SfpDetailVendorSerialNumber_Type()
)
sfpDetailVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailVendorSerialNumber.setStatus("current")
_SfpDetailDateCode_Type = String
_SfpDetailDateCode_Object = MibTableColumn
sfpDetailDateCode = _SfpDetailDateCode_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 22),
    _SfpDetailDateCode_Type()
)
sfpDetailDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailDateCode.setStatus("current")
_SfpDetailFeatureOptionsLossOfSignal_Type = Yesno
_SfpDetailFeatureOptionsLossOfSignal_Object = MibTableColumn
sfpDetailFeatureOptionsLossOfSignal = _SfpDetailFeatureOptionsLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 23),
    _SfpDetailFeatureOptionsLossOfSignal_Type()
)
sfpDetailFeatureOptionsLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailFeatureOptionsLossOfSignal.setStatus("current")
_SfpDetailFeatureOptionsSignalDetect_Type = Yesno
_SfpDetailFeatureOptionsSignalDetect_Object = MibTableColumn
sfpDetailFeatureOptionsSignalDetect = _SfpDetailFeatureOptionsSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 24),
    _SfpDetailFeatureOptionsSignalDetect_Type()
)
sfpDetailFeatureOptionsSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailFeatureOptionsSignalDetect.setStatus("current")
_SfpDetailFeatureOptionsTxFault_Type = Yesno
_SfpDetailFeatureOptionsTxFault_Object = MibTableColumn
sfpDetailFeatureOptionsTxFault = _SfpDetailFeatureOptionsTxFault_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 25),
    _SfpDetailFeatureOptionsTxFault_Type()
)
sfpDetailFeatureOptionsTxFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailFeatureOptionsTxFault.setStatus("current")
_SfpDetailFeatureOptionsTxDisable_Type = Yesno
_SfpDetailFeatureOptionsTxDisable_Object = MibTableColumn
sfpDetailFeatureOptionsTxDisable = _SfpDetailFeatureOptionsTxDisable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 26),
    _SfpDetailFeatureOptionsTxDisable_Type()
)
sfpDetailFeatureOptionsTxDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailFeatureOptionsTxDisable.setStatus("current")
_SfpDetailFeatureOptionsRateSelect_Type = Yesno
_SfpDetailFeatureOptionsRateSelect_Object = MibTableColumn
sfpDetailFeatureOptionsRateSelect = _SfpDetailFeatureOptionsRateSelect_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 27),
    _SfpDetailFeatureOptionsRateSelect_Type()
)
sfpDetailFeatureOptionsRateSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailFeatureOptionsRateSelect.setStatus("current")
_SfpDetailFeatureOptionsTuneableWavelength_Type = Yesno
_SfpDetailFeatureOptionsTuneableWavelength_Object = MibTableColumn
sfpDetailFeatureOptionsTuneableWavelength = _SfpDetailFeatureOptionsTuneableWavelength_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 28),
    _SfpDetailFeatureOptionsTuneableWavelength_Type()
)
sfpDetailFeatureOptionsTuneableWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailFeatureOptionsTuneableWavelength.setStatus("current")
_SfpDetailFeatureOptionsRdt_Type = Yesno
_SfpDetailFeatureOptionsRdt_Object = MibTableColumn
sfpDetailFeatureOptionsRdt = _SfpDetailFeatureOptionsRdt_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 29),
    _SfpDetailFeatureOptionsRdt_Type()
)
sfpDetailFeatureOptionsRdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailFeatureOptionsRdt.setStatus("current")
_SfpDetailFeatureOptionsLro_Type = Yesno
_SfpDetailFeatureOptionsLro_Object = MibTableColumn
sfpDetailFeatureOptionsLro = _SfpDetailFeatureOptionsLro_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 30),
    _SfpDetailFeatureOptionsLro_Type()
)
sfpDetailFeatureOptionsLro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailFeatureOptionsLro.setStatus("current")
_SfpDetailFeatureOptionsPowerLevel_Type = Unsigned32
_SfpDetailFeatureOptionsPowerLevel_Object = MibTableColumn
sfpDetailFeatureOptionsPowerLevel = _SfpDetailFeatureOptionsPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 31),
    _SfpDetailFeatureOptionsPowerLevel_Type()
)
sfpDetailFeatureOptionsPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailFeatureOptionsPowerLevel.setStatus("current")
_SfpDetailFeatureOptionsCooledLaser_Type = Yesno
_SfpDetailFeatureOptionsCooledLaser_Object = MibTableColumn
sfpDetailFeatureOptionsCooledLaser = _SfpDetailFeatureOptionsCooledLaser_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 32),
    _SfpDetailFeatureOptionsCooledLaser_Type()
)
sfpDetailFeatureOptionsCooledLaser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailFeatureOptionsCooledLaser.setStatus("current")
_SfpDetailFeatureOptionsTimingType_Type = SfpTimingType
_SfpDetailFeatureOptionsTimingType_Object = MibTableColumn
sfpDetailFeatureOptionsTimingType = _SfpDetailFeatureOptionsTimingType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 33),
    _SfpDetailFeatureOptionsTimingType_Type()
)
sfpDetailFeatureOptionsTimingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailFeatureOptionsTimingType.setStatus("current")
_SfpDetailFeatureOptionsPagedA2_Type = Yesno
_SfpDetailFeatureOptionsPagedA2_Object = MibTableColumn
sfpDetailFeatureOptionsPagedA2 = _SfpDetailFeatureOptionsPagedA2_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 34),
    _SfpDetailFeatureOptionsPagedA2_Type()
)
sfpDetailFeatureOptionsPagedA2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailFeatureOptionsPagedA2.setStatus("current")
_SfpDetailDigitalDiagnosticsSupported_Type = Yesno
_SfpDetailDigitalDiagnosticsSupported_Object = MibTableColumn
sfpDetailDigitalDiagnosticsSupported = _SfpDetailDigitalDiagnosticsSupported_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 35),
    _SfpDetailDigitalDiagnosticsSupported_Type()
)
sfpDetailDigitalDiagnosticsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailDigitalDiagnosticsSupported.setStatus("current")
_SfpDetailDigitalDiagnosticsCalibrationType_Type = SfpCalibrationType
_SfpDetailDigitalDiagnosticsCalibrationType_Object = MibTableColumn
sfpDetailDigitalDiagnosticsCalibrationType = _SfpDetailDigitalDiagnosticsCalibrationType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 36),
    _SfpDetailDigitalDiagnosticsCalibrationType_Type()
)
sfpDetailDigitalDiagnosticsCalibrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailDigitalDiagnosticsCalibrationType.setStatus("current")
_SfpDetailDigitalDiagnosticsPowerType_Type = SfpPowerType
_SfpDetailDigitalDiagnosticsPowerType_Object = MibTableColumn
sfpDetailDigitalDiagnosticsPowerType = _SfpDetailDigitalDiagnosticsPowerType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 37),
    _SfpDetailDigitalDiagnosticsPowerType_Type()
)
sfpDetailDigitalDiagnosticsPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailDigitalDiagnosticsPowerType.setStatus("current")
_SfpDetailEnhancedOptionsSoftRateSelectControl_Type = Yesno
_SfpDetailEnhancedOptionsSoftRateSelectControl_Object = MibTableColumn
sfpDetailEnhancedOptionsSoftRateSelectControl = _SfpDetailEnhancedOptionsSoftRateSelectControl_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 38),
    _SfpDetailEnhancedOptionsSoftRateSelectControl_Type()
)
sfpDetailEnhancedOptionsSoftRateSelectControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailEnhancedOptionsSoftRateSelectControl.setStatus("current")
_SfpDetailEnhancedOptionsAppSelectControl_Type = Yesno
_SfpDetailEnhancedOptionsAppSelectControl_Object = MibTableColumn
sfpDetailEnhancedOptionsAppSelectControl = _SfpDetailEnhancedOptionsAppSelectControl_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 39),
    _SfpDetailEnhancedOptionsAppSelectControl_Type()
)
sfpDetailEnhancedOptionsAppSelectControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailEnhancedOptionsAppSelectControl.setStatus("current")
_SfpDetailEnhancedOptionsSoftRateSelectControlMonitor_Type = Yesno
_SfpDetailEnhancedOptionsSoftRateSelectControlMonitor_Object = MibTableColumn
sfpDetailEnhancedOptionsSoftRateSelectControlMonitor = _SfpDetailEnhancedOptionsSoftRateSelectControlMonitor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 40),
    _SfpDetailEnhancedOptionsSoftRateSelectControlMonitor_Type()
)
sfpDetailEnhancedOptionsSoftRateSelectControlMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailEnhancedOptionsSoftRateSelectControlMonitor.setStatus("current")
_SfpDetailEnhancedOptionsSoftRxLosMonitor_Type = Yesno
_SfpDetailEnhancedOptionsSoftRxLosMonitor_Object = MibTableColumn
sfpDetailEnhancedOptionsSoftRxLosMonitor = _SfpDetailEnhancedOptionsSoftRxLosMonitor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 41),
    _SfpDetailEnhancedOptionsSoftRxLosMonitor_Type()
)
sfpDetailEnhancedOptionsSoftRxLosMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailEnhancedOptionsSoftRxLosMonitor.setStatus("current")
_SfpDetailEnhancedOptionsSoftTxFaultMonitor_Type = Yesno
_SfpDetailEnhancedOptionsSoftTxFaultMonitor_Object = MibTableColumn
sfpDetailEnhancedOptionsSoftTxFaultMonitor = _SfpDetailEnhancedOptionsSoftTxFaultMonitor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 42),
    _SfpDetailEnhancedOptionsSoftTxFaultMonitor_Type()
)
sfpDetailEnhancedOptionsSoftTxFaultMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailEnhancedOptionsSoftTxFaultMonitor.setStatus("current")
_SfpDetailEnhancedOptionsSoftTxDisableControlMonitor_Type = Yesno
_SfpDetailEnhancedOptionsSoftTxDisableControlMonitor_Object = MibTableColumn
sfpDetailEnhancedOptionsSoftTxDisableControlMonitor = _SfpDetailEnhancedOptionsSoftTxDisableControlMonitor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 43),
    _SfpDetailEnhancedOptionsSoftTxDisableControlMonitor_Type()
)
sfpDetailEnhancedOptionsSoftTxDisableControlMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailEnhancedOptionsSoftTxDisableControlMonitor.setStatus("current")
_SfpDetailEnhancedOptionsAllAlarmWarningFlags_Type = Yesno
_SfpDetailEnhancedOptionsAllAlarmWarningFlags_Object = MibTableColumn
sfpDetailEnhancedOptionsAllAlarmWarningFlags = _SfpDetailEnhancedOptionsAllAlarmWarningFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 1, 1, 44),
    _SfpDetailEnhancedOptionsAllAlarmWarningFlags_Type()
)
sfpDetailEnhancedOptionsAllAlarmWarningFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDetailEnhancedOptionsAllAlarmWarningFlags.setStatus("current")
_SfpDiagnosticTable_Object = MibTable
sfpDiagnosticTable = _SfpDiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 2)
)
if mibBuilder.loadTexts:
    sfpDiagnosticTable.setStatus("current")
_SfpDiagnosticEntry_Object = MibTableRow
sfpDiagnosticEntry = _SfpDiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 2, 1)
)
sfpDiagnosticEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "sfpDiagnosticIfname"),
)
if mibBuilder.loadTexts:
    sfpDiagnosticEntry.setStatus("current")


class _SfpDiagnosticIfname_Type(String):
    """Custom type sfpDiagnosticIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SfpDiagnosticIfname_Type.__name__ = "String"
_SfpDiagnosticIfname_Object = MibTableColumn
sfpDiagnosticIfname = _SfpDiagnosticIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 2, 1, 1),
    _SfpDiagnosticIfname_Type()
)
sfpDiagnosticIfname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sfpDiagnosticIfname.setStatus("current")
_SfpDiagnosticPresent_Type = Yesno
_SfpDiagnosticPresent_Object = MibTableColumn
sfpDiagnosticPresent = _SfpDiagnosticPresent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 2, 1, 2),
    _SfpDiagnosticPresent_Type()
)
sfpDiagnosticPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticPresent.setStatus("current")
_SfpDiagnosticSupported_Type = Yesno
_SfpDiagnosticSupported_Object = MibTableColumn
sfpDiagnosticSupported = _SfpDiagnosticSupported_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 2, 1, 3),
    _SfpDiagnosticSupported_Type()
)
sfpDiagnosticSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticSupported.setStatus("current")
_SfpDiagnosticControlStatusDataReadyState_Type = Yesno
_SfpDiagnosticControlStatusDataReadyState_Object = MibTableColumn
sfpDiagnosticControlStatusDataReadyState = _SfpDiagnosticControlStatusDataReadyState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 2, 1, 4),
    _SfpDiagnosticControlStatusDataReadyState_Type()
)
sfpDiagnosticControlStatusDataReadyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticControlStatusDataReadyState.setStatus("current")
_SfpDiagnosticControlStatusRxLosState_Type = Yesno
_SfpDiagnosticControlStatusRxLosState_Object = MibTableColumn
sfpDiagnosticControlStatusRxLosState = _SfpDiagnosticControlStatusRxLosState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 2, 1, 5),
    _SfpDiagnosticControlStatusRxLosState_Type()
)
sfpDiagnosticControlStatusRxLosState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticControlStatusRxLosState.setStatus("current")
_SfpDiagnosticControlStatusTxFaultState_Type = Yesno
_SfpDiagnosticControlStatusTxFaultState_Object = MibTableColumn
sfpDiagnosticControlStatusTxFaultState = _SfpDiagnosticControlStatusTxFaultState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 2, 1, 6),
    _SfpDiagnosticControlStatusTxFaultState_Type()
)
sfpDiagnosticControlStatusTxFaultState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticControlStatusTxFaultState.setStatus("current")
_SfpDiagnosticControlStatusSoftRateSelect0State_Type = Yesno
_SfpDiagnosticControlStatusSoftRateSelect0State_Object = MibTableColumn
sfpDiagnosticControlStatusSoftRateSelect0State = _SfpDiagnosticControlStatusSoftRateSelect0State_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 2, 1, 7),
    _SfpDiagnosticControlStatusSoftRateSelect0State_Type()
)
sfpDiagnosticControlStatusSoftRateSelect0State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticControlStatusSoftRateSelect0State.setStatus("current")
_SfpDiagnosticControlStatusSoftRateSelect1State_Type = Yesno
_SfpDiagnosticControlStatusSoftRateSelect1State_Object = MibTableColumn
sfpDiagnosticControlStatusSoftRateSelect1State = _SfpDiagnosticControlStatusSoftRateSelect1State_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 2, 1, 8),
    _SfpDiagnosticControlStatusSoftRateSelect1State_Type()
)
sfpDiagnosticControlStatusSoftRateSelect1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticControlStatusSoftRateSelect1State.setStatus("current")
_SfpDiagnosticControlStatusRateSelect0State_Type = Yesno
_SfpDiagnosticControlStatusRateSelect0State_Object = MibTableColumn
sfpDiagnosticControlStatusRateSelect0State = _SfpDiagnosticControlStatusRateSelect0State_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 2, 1, 9),
    _SfpDiagnosticControlStatusRateSelect0State_Type()
)
sfpDiagnosticControlStatusRateSelect0State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticControlStatusRateSelect0State.setStatus("current")
_SfpDiagnosticControlStatusRateSelect1State_Type = Yesno
_SfpDiagnosticControlStatusRateSelect1State_Object = MibTableColumn
sfpDiagnosticControlStatusRateSelect1State = _SfpDiagnosticControlStatusRateSelect1State_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 2, 1, 10),
    _SfpDiagnosticControlStatusRateSelect1State_Type()
)
sfpDiagnosticControlStatusRateSelect1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticControlStatusRateSelect1State.setStatus("current")
_SfpDiagnosticControlStatusSoftTxDisableState_Type = Yesno
_SfpDiagnosticControlStatusSoftTxDisableState_Object = MibTableColumn
sfpDiagnosticControlStatusSoftTxDisableState = _SfpDiagnosticControlStatusSoftTxDisableState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 2, 1, 11),
    _SfpDiagnosticControlStatusSoftTxDisableState_Type()
)
sfpDiagnosticControlStatusSoftTxDisableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticControlStatusSoftTxDisableState.setStatus("current")
_SfpDiagnosticControlStatusTxDisableState_Type = Yesno
_SfpDiagnosticControlStatusTxDisableState_Object = MibTableColumn
sfpDiagnosticControlStatusTxDisableState = _SfpDiagnosticControlStatusTxDisableState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 2, 1, 12),
    _SfpDiagnosticControlStatusTxDisableState_Type()
)
sfpDiagnosticControlStatusTxDisableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticControlStatusTxDisableState.setStatus("current")
_SfpDiagnosticMeasurementValueTable_Object = MibTable
sfpDiagnosticMeasurementValueTable = _SfpDiagnosticMeasurementValueTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 3)
)
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementValueTable.setStatus("current")
_SfpDiagnosticMeasurementValueEntry_Object = MibTableRow
sfpDiagnosticMeasurementValueEntry = _SfpDiagnosticMeasurementValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 3, 1)
)
sfpDiagnosticMeasurementValueEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "sfpDiagnosticIfname"),
    (1, "VIPTELA-OPER-VPN", "sfpDiagnosticMeasurementValueMeasurement"),
)
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementValueEntry.setStatus("current")
_SfpDiagnosticMeasurementValueMeasurement_Type = String
_SfpDiagnosticMeasurementValueMeasurement_Object = MibTableColumn
sfpDiagnosticMeasurementValueMeasurement = _SfpDiagnosticMeasurementValueMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 3, 1, 1),
    _SfpDiagnosticMeasurementValueMeasurement_Type()
)
sfpDiagnosticMeasurementValueMeasurement.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementValueMeasurement.setStatus("current")
_SfpDiagnosticMeasurementValueUnitValue_Type = String
_SfpDiagnosticMeasurementValueUnitValue_Object = MibTableColumn
sfpDiagnosticMeasurementValueUnitValue = _SfpDiagnosticMeasurementValueUnitValue_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 3, 1, 2),
    _SfpDiagnosticMeasurementValueUnitValue_Type()
)
sfpDiagnosticMeasurementValueUnitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementValueUnitValue.setStatus("current")
_SfpDiagnosticMeasurementValueLowAlarmValue_Type = ConfdString
_SfpDiagnosticMeasurementValueLowAlarmValue_Object = MibTableColumn
sfpDiagnosticMeasurementValueLowAlarmValue = _SfpDiagnosticMeasurementValueLowAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 3, 1, 3),
    _SfpDiagnosticMeasurementValueLowAlarmValue_Type()
)
sfpDiagnosticMeasurementValueLowAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementValueLowAlarmValue.setStatus("current")
_SfpDiagnosticMeasurementValueLowWarningValue_Type = ConfdString
_SfpDiagnosticMeasurementValueLowWarningValue_Object = MibTableColumn
sfpDiagnosticMeasurementValueLowWarningValue = _SfpDiagnosticMeasurementValueLowWarningValue_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 3, 1, 4),
    _SfpDiagnosticMeasurementValueLowWarningValue_Type()
)
sfpDiagnosticMeasurementValueLowWarningValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementValueLowWarningValue.setStatus("current")
_SfpDiagnosticMeasurementValueHighWarningValue_Type = ConfdString
_SfpDiagnosticMeasurementValueHighWarningValue_Object = MibTableColumn
sfpDiagnosticMeasurementValueHighWarningValue = _SfpDiagnosticMeasurementValueHighWarningValue_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 3, 1, 5),
    _SfpDiagnosticMeasurementValueHighWarningValue_Type()
)
sfpDiagnosticMeasurementValueHighWarningValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementValueHighWarningValue.setStatus("current")
_SfpDiagnosticMeasurementValueHighAlarmValue_Type = ConfdString
_SfpDiagnosticMeasurementValueHighAlarmValue_Object = MibTableColumn
sfpDiagnosticMeasurementValueHighAlarmValue = _SfpDiagnosticMeasurementValueHighAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 3, 1, 6),
    _SfpDiagnosticMeasurementValueHighAlarmValue_Type()
)
sfpDiagnosticMeasurementValueHighAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementValueHighAlarmValue.setStatus("current")
_SfpDiagnosticMeasurementValueCurrentValue_Type = ConfdString
_SfpDiagnosticMeasurementValueCurrentValue_Object = MibTableColumn
sfpDiagnosticMeasurementValueCurrentValue = _SfpDiagnosticMeasurementValueCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 3, 1, 7),
    _SfpDiagnosticMeasurementValueCurrentValue_Type()
)
sfpDiagnosticMeasurementValueCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementValueCurrentValue.setStatus("current")
_SfpDiagnosticMeasurementAlarmTable_Object = MibTable
sfpDiagnosticMeasurementAlarmTable = _SfpDiagnosticMeasurementAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 4)
)
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementAlarmTable.setStatus("current")
_SfpDiagnosticMeasurementAlarmEntry_Object = MibTableRow
sfpDiagnosticMeasurementAlarmEntry = _SfpDiagnosticMeasurementAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 4, 1)
)
sfpDiagnosticMeasurementAlarmEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "sfpDiagnosticIfname"),
    (1, "VIPTELA-OPER-VPN", "sfpDiagnosticMeasurementAlarmMeasurement"),
)
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementAlarmEntry.setStatus("current")
_SfpDiagnosticMeasurementAlarmMeasurement_Type = String
_SfpDiagnosticMeasurementAlarmMeasurement_Object = MibTableColumn
sfpDiagnosticMeasurementAlarmMeasurement = _SfpDiagnosticMeasurementAlarmMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 4, 1, 1),
    _SfpDiagnosticMeasurementAlarmMeasurement_Type()
)
sfpDiagnosticMeasurementAlarmMeasurement.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementAlarmMeasurement.setStatus("current")
_SfpDiagnosticMeasurementAlarmLowAlarmAlarm_Type = String
_SfpDiagnosticMeasurementAlarmLowAlarmAlarm_Object = MibTableColumn
sfpDiagnosticMeasurementAlarmLowAlarmAlarm = _SfpDiagnosticMeasurementAlarmLowAlarmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 4, 1, 2),
    _SfpDiagnosticMeasurementAlarmLowAlarmAlarm_Type()
)
sfpDiagnosticMeasurementAlarmLowAlarmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementAlarmLowAlarmAlarm.setStatus("current")
_SfpDiagnosticMeasurementAlarmLowWarningAlarm_Type = String
_SfpDiagnosticMeasurementAlarmLowWarningAlarm_Object = MibTableColumn
sfpDiagnosticMeasurementAlarmLowWarningAlarm = _SfpDiagnosticMeasurementAlarmLowWarningAlarm_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 4, 1, 3),
    _SfpDiagnosticMeasurementAlarmLowWarningAlarm_Type()
)
sfpDiagnosticMeasurementAlarmLowWarningAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementAlarmLowWarningAlarm.setStatus("current")
_SfpDiagnosticMeasurementAlarmHighWarningAlarm_Type = String
_SfpDiagnosticMeasurementAlarmHighWarningAlarm_Object = MibTableColumn
sfpDiagnosticMeasurementAlarmHighWarningAlarm = _SfpDiagnosticMeasurementAlarmHighWarningAlarm_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 4, 1, 4),
    _SfpDiagnosticMeasurementAlarmHighWarningAlarm_Type()
)
sfpDiagnosticMeasurementAlarmHighWarningAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementAlarmHighWarningAlarm.setStatus("current")
_SfpDiagnosticMeasurementAlarmHighAlarmAlarm_Type = String
_SfpDiagnosticMeasurementAlarmHighAlarmAlarm_Object = MibTableColumn
sfpDiagnosticMeasurementAlarmHighAlarmAlarm = _SfpDiagnosticMeasurementAlarmHighAlarmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 4, 1, 5),
    _SfpDiagnosticMeasurementAlarmHighAlarmAlarm_Type()
)
sfpDiagnosticMeasurementAlarmHighAlarmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticMeasurementAlarmHighAlarmAlarm.setStatus("current")
_SfpRawA0Table_Object = MibTable
sfpRawA0Table = _SfpRawA0Table_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5)
)
if mibBuilder.loadTexts:
    sfpRawA0Table.setStatus("current")
_SfpRawA0Entry_Object = MibTableRow
sfpRawA0Entry = _SfpRawA0Entry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1)
)
sfpRawA0Entry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "sfpRawA0Ifname"),
)
if mibBuilder.loadTexts:
    sfpRawA0Entry.setStatus("current")


class _SfpRawA0Ifname_Type(String):
    """Custom type sfpRawA0Ifname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SfpRawA0Ifname_Type.__name__ = "String"
_SfpRawA0Ifname_Object = MibTableColumn
sfpRawA0Ifname = _SfpRawA0Ifname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 1),
    _SfpRawA0Ifname_Type()
)
sfpRawA0Ifname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sfpRawA0Ifname.setStatus("current")
_SfpRawA0Present_Type = Yesno
_SfpRawA0Present_Object = MibTableColumn
sfpRawA0Present = _SfpRawA0Present_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 2),
    _SfpRawA0Present_Type()
)
sfpRawA0Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0Present.setStatus("current")
_SfpRawA0Row0_Type = SfpHexBytes
_SfpRawA0Row0_Object = MibTableColumn
sfpRawA0Row0 = _SfpRawA0Row0_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 3),
    _SfpRawA0Row0_Type()
)
sfpRawA0Row0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0Row0.setStatus("current")
_SfpRawA0Row1_Type = SfpHexBytes
_SfpRawA0Row1_Object = MibTableColumn
sfpRawA0Row1 = _SfpRawA0Row1_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 4),
    _SfpRawA0Row1_Type()
)
sfpRawA0Row1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0Row1.setStatus("current")
_SfpRawA0Row2_Type = SfpHexBytes
_SfpRawA0Row2_Object = MibTableColumn
sfpRawA0Row2 = _SfpRawA0Row2_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 5),
    _SfpRawA0Row2_Type()
)
sfpRawA0Row2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0Row2.setStatus("current")
_SfpRawA0Row3_Type = SfpHexBytes
_SfpRawA0Row3_Object = MibTableColumn
sfpRawA0Row3 = _SfpRawA0Row3_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 6),
    _SfpRawA0Row3_Type()
)
sfpRawA0Row3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0Row3.setStatus("current")
_SfpRawA0Row4_Type = SfpHexBytes
_SfpRawA0Row4_Object = MibTableColumn
sfpRawA0Row4 = _SfpRawA0Row4_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 7),
    _SfpRawA0Row4_Type()
)
sfpRawA0Row4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0Row4.setStatus("current")
_SfpRawA0Row5_Type = SfpHexBytes
_SfpRawA0Row5_Object = MibTableColumn
sfpRawA0Row5 = _SfpRawA0Row5_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 8),
    _SfpRawA0Row5_Type()
)
sfpRawA0Row5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0Row5.setStatus("current")
_SfpRawA0Row6_Type = SfpHexBytes
_SfpRawA0Row6_Object = MibTableColumn
sfpRawA0Row6 = _SfpRawA0Row6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 9),
    _SfpRawA0Row6_Type()
)
sfpRawA0Row6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0Row6.setStatus("current")
_SfpRawA0Row7_Type = SfpHexBytes
_SfpRawA0Row7_Object = MibTableColumn
sfpRawA0Row7 = _SfpRawA0Row7_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 10),
    _SfpRawA0Row7_Type()
)
sfpRawA0Row7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0Row7.setStatus("current")
_SfpRawA0Row8_Type = SfpHexBytes
_SfpRawA0Row8_Object = MibTableColumn
sfpRawA0Row8 = _SfpRawA0Row8_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 11),
    _SfpRawA0Row8_Type()
)
sfpRawA0Row8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0Row8.setStatus("current")
_SfpRawA0Row9_Type = SfpHexBytes
_SfpRawA0Row9_Object = MibTableColumn
sfpRawA0Row9 = _SfpRawA0Row9_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 12),
    _SfpRawA0Row9_Type()
)
sfpRawA0Row9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0Row9.setStatus("current")
_SfpRawA0RowA_Type = SfpHexBytes
_SfpRawA0RowA_Object = MibTableColumn
sfpRawA0RowA = _SfpRawA0RowA_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 13),
    _SfpRawA0RowA_Type()
)
sfpRawA0RowA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0RowA.setStatus("current")
_SfpRawA0RowB_Type = SfpHexBytes
_SfpRawA0RowB_Object = MibTableColumn
sfpRawA0RowB = _SfpRawA0RowB_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 14),
    _SfpRawA0RowB_Type()
)
sfpRawA0RowB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0RowB.setStatus("current")
_SfpRawA0RowC_Type = SfpHexBytes
_SfpRawA0RowC_Object = MibTableColumn
sfpRawA0RowC = _SfpRawA0RowC_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 15),
    _SfpRawA0RowC_Type()
)
sfpRawA0RowC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0RowC.setStatus("current")
_SfpRawA0RowD_Type = SfpHexBytes
_SfpRawA0RowD_Object = MibTableColumn
sfpRawA0RowD = _SfpRawA0RowD_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 16),
    _SfpRawA0RowD_Type()
)
sfpRawA0RowD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0RowD.setStatus("current")
_SfpRawA0RowE_Type = SfpHexBytes
_SfpRawA0RowE_Object = MibTableColumn
sfpRawA0RowE = _SfpRawA0RowE_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 17),
    _SfpRawA0RowE_Type()
)
sfpRawA0RowE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0RowE.setStatus("current")
_SfpRawA0RowF_Type = SfpHexBytes
_SfpRawA0RowF_Object = MibTableColumn
sfpRawA0RowF = _SfpRawA0RowF_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 5, 1, 18),
    _SfpRawA0RowF_Type()
)
sfpRawA0RowF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA0RowF.setStatus("current")
_SfpRawA2Table_Object = MibTable
sfpRawA2Table = _SfpRawA2Table_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6)
)
if mibBuilder.loadTexts:
    sfpRawA2Table.setStatus("current")
_SfpRawA2Entry_Object = MibTableRow
sfpRawA2Entry = _SfpRawA2Entry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1)
)
sfpRawA2Entry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "sfpRawA2Ifname"),
)
if mibBuilder.loadTexts:
    sfpRawA2Entry.setStatus("current")


class _SfpRawA2Ifname_Type(String):
    """Custom type sfpRawA2Ifname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SfpRawA2Ifname_Type.__name__ = "String"
_SfpRawA2Ifname_Object = MibTableColumn
sfpRawA2Ifname = _SfpRawA2Ifname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 1),
    _SfpRawA2Ifname_Type()
)
sfpRawA2Ifname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sfpRawA2Ifname.setStatus("current")
_SfpRawA2Present_Type = Yesno
_SfpRawA2Present_Object = MibTableColumn
sfpRawA2Present = _SfpRawA2Present_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 2),
    _SfpRawA2Present_Type()
)
sfpRawA2Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2Present.setStatus("current")
_SfpRawA2Supported_Type = Yesno
_SfpRawA2Supported_Object = MibTableColumn
sfpRawA2Supported = _SfpRawA2Supported_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 3),
    _SfpRawA2Supported_Type()
)
sfpRawA2Supported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2Supported.setStatus("current")
_SfpRawA2Row0_Type = SfpHexBytes
_SfpRawA2Row0_Object = MibTableColumn
sfpRawA2Row0 = _SfpRawA2Row0_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 4),
    _SfpRawA2Row0_Type()
)
sfpRawA2Row0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2Row0.setStatus("current")
_SfpRawA2Row1_Type = SfpHexBytes
_SfpRawA2Row1_Object = MibTableColumn
sfpRawA2Row1 = _SfpRawA2Row1_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 5),
    _SfpRawA2Row1_Type()
)
sfpRawA2Row1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2Row1.setStatus("current")
_SfpRawA2Row2_Type = SfpHexBytes
_SfpRawA2Row2_Object = MibTableColumn
sfpRawA2Row2 = _SfpRawA2Row2_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 6),
    _SfpRawA2Row2_Type()
)
sfpRawA2Row2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2Row2.setStatus("current")
_SfpRawA2Row3_Type = SfpHexBytes
_SfpRawA2Row3_Object = MibTableColumn
sfpRawA2Row3 = _SfpRawA2Row3_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 7),
    _SfpRawA2Row3_Type()
)
sfpRawA2Row3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2Row3.setStatus("current")
_SfpRawA2Row4_Type = SfpHexBytes
_SfpRawA2Row4_Object = MibTableColumn
sfpRawA2Row4 = _SfpRawA2Row4_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 8),
    _SfpRawA2Row4_Type()
)
sfpRawA2Row4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2Row4.setStatus("current")
_SfpRawA2Row5_Type = SfpHexBytes
_SfpRawA2Row5_Object = MibTableColumn
sfpRawA2Row5 = _SfpRawA2Row5_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 9),
    _SfpRawA2Row5_Type()
)
sfpRawA2Row5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2Row5.setStatus("current")
_SfpRawA2Row6_Type = SfpHexBytes
_SfpRawA2Row6_Object = MibTableColumn
sfpRawA2Row6 = _SfpRawA2Row6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 10),
    _SfpRawA2Row6_Type()
)
sfpRawA2Row6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2Row6.setStatus("current")
_SfpRawA2Row7_Type = SfpHexBytes
_SfpRawA2Row7_Object = MibTableColumn
sfpRawA2Row7 = _SfpRawA2Row7_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 11),
    _SfpRawA2Row7_Type()
)
sfpRawA2Row7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2Row7.setStatus("current")
_SfpRawA2Row8_Type = SfpHexBytes
_SfpRawA2Row8_Object = MibTableColumn
sfpRawA2Row8 = _SfpRawA2Row8_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 12),
    _SfpRawA2Row8_Type()
)
sfpRawA2Row8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2Row8.setStatus("current")
_SfpRawA2Row9_Type = SfpHexBytes
_SfpRawA2Row9_Object = MibTableColumn
sfpRawA2Row9 = _SfpRawA2Row9_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 13),
    _SfpRawA2Row9_Type()
)
sfpRawA2Row9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2Row9.setStatus("current")
_SfpRawA2RowA_Type = SfpHexBytes
_SfpRawA2RowA_Object = MibTableColumn
sfpRawA2RowA = _SfpRawA2RowA_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 14),
    _SfpRawA2RowA_Type()
)
sfpRawA2RowA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2RowA.setStatus("current")
_SfpRawA2RowB_Type = SfpHexBytes
_SfpRawA2RowB_Object = MibTableColumn
sfpRawA2RowB = _SfpRawA2RowB_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 15),
    _SfpRawA2RowB_Type()
)
sfpRawA2RowB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2RowB.setStatus("current")
_SfpRawA2RowC_Type = SfpHexBytes
_SfpRawA2RowC_Object = MibTableColumn
sfpRawA2RowC = _SfpRawA2RowC_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 16),
    _SfpRawA2RowC_Type()
)
sfpRawA2RowC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2RowC.setStatus("current")
_SfpRawA2RowD_Type = SfpHexBytes
_SfpRawA2RowD_Object = MibTableColumn
sfpRawA2RowD = _SfpRawA2RowD_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 17),
    _SfpRawA2RowD_Type()
)
sfpRawA2RowD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2RowD.setStatus("current")
_SfpRawA2RowE_Type = SfpHexBytes
_SfpRawA2RowE_Object = MibTableColumn
sfpRawA2RowE = _SfpRawA2RowE_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 18),
    _SfpRawA2RowE_Type()
)
sfpRawA2RowE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2RowE.setStatus("current")
_SfpRawA2RowF_Type = SfpHexBytes
_SfpRawA2RowF_Object = MibTableColumn
sfpRawA2RowF = _SfpRawA2RowF_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 17, 6, 1, 19),
    _SfpRawA2RowF_Type()
)
sfpRawA2RowF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRawA2RowF.setStatus("current")
_Dhcpv6_ObjectIdentity = ObjectIdentity
dhcpv6 = _Dhcpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 18)
)
_Dhcpv6InterfaceTable_Object = MibTable
dhcpv6InterfaceTable = _Dhcpv6InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 18, 1)
)
if mibBuilder.loadTexts:
    dhcpv6InterfaceTable.setStatus("current")
_Dhcpv6InterfaceEntry_Object = MibTableRow
dhcpv6InterfaceEntry = _Dhcpv6InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 18, 1, 1)
)
dhcpv6InterfaceEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "dhcpv6InterfaceVpnId"),
    (0, "VIPTELA-OPER-VPN", "dhcpv6InterfaceIfname"),
)
if mibBuilder.loadTexts:
    dhcpv6InterfaceEntry.setStatus("current")


class _Dhcpv6InterfaceVpnId_Type(Unsigned32):
    """Custom type dhcpv6InterfaceVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_Dhcpv6InterfaceVpnId_Type.__name__ = "Unsigned32"
_Dhcpv6InterfaceVpnId_Object = MibTableColumn
dhcpv6InterfaceVpnId = _Dhcpv6InterfaceVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 18, 1, 1, 1),
    _Dhcpv6InterfaceVpnId_Type()
)
dhcpv6InterfaceVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpv6InterfaceVpnId.setStatus("current")


class _Dhcpv6InterfaceIfname_Type(String):
    """Custom type dhcpv6InterfaceIfname based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Dhcpv6InterfaceIfname_Type.__name__ = "String"
_Dhcpv6InterfaceIfname_Object = MibTableColumn
dhcpv6InterfaceIfname = _Dhcpv6InterfaceIfname_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 18, 1, 1, 2),
    _Dhcpv6InterfaceIfname_Type()
)
dhcpv6InterfaceIfname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpv6InterfaceIfname.setStatus("current")


class _Dhcpv6InterfaceState_Type(Integer32):
    """Custom type dhcpv6InterfaceState based on Integer32"""
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
        *(("init", 0),
          ("request", 1),
          ("bound", 2),
          ("renew", 3),
          ("rebind", 4),
          ("release", 5))
    )


_Dhcpv6InterfaceState_Type.__name__ = "Integer32"
_Dhcpv6InterfaceState_Object = MibTableColumn
dhcpv6InterfaceState = _Dhcpv6InterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 18, 1, 1, 3),
    _Dhcpv6InterfaceState_Type()
)
dhcpv6InterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6InterfaceState.setStatus("current")
_Dhcpv6InterfaceAcquiredIp_Type = IpPrefix
_Dhcpv6InterfaceAcquiredIp_Object = MibTableColumn
dhcpv6InterfaceAcquiredIp = _Dhcpv6InterfaceAcquiredIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 18, 1, 1, 4),
    _Dhcpv6InterfaceAcquiredIp_Type()
)
dhcpv6InterfaceAcquiredIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6InterfaceAcquiredIp.setStatus("current")
_Dhcpv6InterfaceServer_Type = String
_Dhcpv6InterfaceServer_Object = MibTableColumn
dhcpv6InterfaceServer = _Dhcpv6InterfaceServer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 18, 1, 1, 5),
    _Dhcpv6InterfaceServer_Type()
)
dhcpv6InterfaceServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6InterfaceServer.setStatus("current")
_Dhcpv6InterfaceLeaseTime_Type = String
_Dhcpv6InterfaceLeaseTime_Object = MibTableColumn
dhcpv6InterfaceLeaseTime = _Dhcpv6InterfaceLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 18, 1, 1, 6),
    _Dhcpv6InterfaceLeaseTime_Type()
)
dhcpv6InterfaceLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6InterfaceLeaseTime.setStatus("current")
_Dhcpv6InterfaceTimeRemaining_Type = String
_Dhcpv6InterfaceTimeRemaining_Object = MibTableColumn
dhcpv6InterfaceTimeRemaining = _Dhcpv6InterfaceTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 18, 1, 1, 7),
    _Dhcpv6InterfaceTimeRemaining_Type()
)
dhcpv6InterfaceTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6InterfaceTimeRemaining.setStatus("current")
_Dhcpv6InterfaceGateway_Type = Ipv6Address
_Dhcpv6InterfaceGateway_Object = MibTableColumn
dhcpv6InterfaceGateway = _Dhcpv6InterfaceGateway_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 18, 1, 1, 8),
    _Dhcpv6InterfaceGateway_Type()
)
dhcpv6InterfaceGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6InterfaceGateway.setStatus("current")
_Dhcpv6InterfaceDnsListTable_Object = MibTable
dhcpv6InterfaceDnsListTable = _Dhcpv6InterfaceDnsListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 19)
)
if mibBuilder.loadTexts:
    dhcpv6InterfaceDnsListTable.setStatus("current")
_Dhcpv6InterfaceDnsListEntry_Object = MibTableRow
dhcpv6InterfaceDnsListEntry = _Dhcpv6InterfaceDnsListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 19, 1)
)
dhcpv6InterfaceDnsListEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "dhcpv6InterfaceVpnId"),
    (0, "VIPTELA-OPER-VPN", "dhcpv6InterfaceIfname"),
    (0, "VIPTELA-OPER-VPN", "dhcpv6InterfaceDnsListIndex"),
)
if mibBuilder.loadTexts:
    dhcpv6InterfaceDnsListEntry.setStatus("current")
_Dhcpv6InterfaceDnsListIndex_Type = Unsigned32
_Dhcpv6InterfaceDnsListIndex_Object = MibTableColumn
dhcpv6InterfaceDnsListIndex = _Dhcpv6InterfaceDnsListIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 19, 1, 1),
    _Dhcpv6InterfaceDnsListIndex_Type()
)
dhcpv6InterfaceDnsListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpv6InterfaceDnsListIndex.setStatus("current")
_Dhcpv6InterfaceDnsListDns_Type = Ipv6Address
_Dhcpv6InterfaceDnsListDns_Object = MibTableColumn
dhcpv6InterfaceDnsListDns = _Dhcpv6InterfaceDnsListDns_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 19, 1, 2),
    _Dhcpv6InterfaceDnsListDns_Type()
)
dhcpv6InterfaceDnsListDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpv6InterfaceDnsListDns.setStatus("current")
_Cloudexpress_ObjectIdentity = ObjectIdentity
cloudexpress = _Cloudexpress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20)
)
_CloudAppTable_Object = MibTable
cloudAppTable = _CloudAppTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 1)
)
if mibBuilder.loadTexts:
    cloudAppTable.setStatus("current")
_CloudAppEntry_Object = MibTableRow
cloudAppEntry = _CloudAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 1, 1)
)
cloudAppEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "cloudAppVpnId"),
    (0, "VIPTELA-OPER-VPN", "cloudAppName"),
)
if mibBuilder.loadTexts:
    cloudAppEntry.setStatus("current")


class _CloudAppVpnId_Type(Unsigned32):
    """Custom type cloudAppVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_CloudAppVpnId_Type.__name__ = "Unsigned32"
_CloudAppVpnId_Object = MibTableColumn
cloudAppVpnId = _CloudAppVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 1, 1, 1),
    _CloudAppVpnId_Type()
)
cloudAppVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cloudAppVpnId.setStatus("current")
_CloudAppName_Type = CloudExpressAppType
_CloudAppName_Object = MibTableColumn
cloudAppName = _CloudAppName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 1, 1, 2),
    _CloudAppName_Type()
)
cloudAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cloudAppName.setStatus("current")


class _CloudAppExitType_Type(Integer32):
    """Custom type cloudAppExitType based on Integer32"""
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


_CloudAppExitType_Type.__name__ = "Integer32"
_CloudAppExitType_Object = MibTableColumn
cloudAppExitType = _CloudAppExitType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 1, 1, 3),
    _CloudAppExitType_Type()
)
cloudAppExitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudAppExitType.setStatus("current")
_CloudAppGatewayIp_Type = InetAddressIP
_CloudAppGatewayIp_Object = MibTableColumn
cloudAppGatewayIp = _CloudAppGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 1, 1, 4),
    _CloudAppGatewayIp_Type()
)
cloudAppGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudAppGatewayIp.setStatus("current")


class _CloudAppIfName_Type(String):
    """Custom type cloudAppIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CloudAppIfName_Type.__name__ = "String"
_CloudAppIfName_Object = MibTableColumn
cloudAppIfName = _CloudAppIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 1, 1, 5),
    _CloudAppIfName_Type()
)
cloudAppIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudAppIfName.setStatus("current")
_CloudAppLatency_Type = Unsigned32
_CloudAppLatency_Object = MibTableColumn
cloudAppLatency = _CloudAppLatency_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 1, 1, 6),
    _CloudAppLatency_Type()
)
cloudAppLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudAppLatency.setStatus("current")
_CloudAppLoss_Type = Unsigned32
_CloudAppLoss_Object = MibTableColumn
cloudAppLoss = _CloudAppLoss_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 1, 1, 7),
    _CloudAppLoss_Type()
)
cloudAppLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudAppLoss.setStatus("current")
_CloudAppLocalColor_Type = TlocColorEnum
_CloudAppLocalColor_Object = MibTableColumn
cloudAppLocalColor = _CloudAppLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 1, 1, 8),
    _CloudAppLocalColor_Type()
)
cloudAppLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudAppLocalColor.setStatus("current")
_CloudAppRemoteColor_Type = TlocColorEnum
_CloudAppRemoteColor_Object = MibTableColumn
cloudAppRemoteColor = _CloudAppRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 1, 1, 9),
    _CloudAppRemoteColor_Type()
)
cloudAppRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudAppRemoteColor.setStatus("current")
_CloudLocalExitTable_Object = MibTable
cloudLocalExitTable = _CloudLocalExitTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 2)
)
if mibBuilder.loadTexts:
    cloudLocalExitTable.setStatus("current")
_CloudLocalExitEntry_Object = MibTableRow
cloudLocalExitEntry = _CloudLocalExitEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 2, 1)
)
cloudLocalExitEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "cloudLocalExitVpnId"),
    (0, "VIPTELA-OPER-VPN", "cloudLocalExitAppName"),
    (0, "VIPTELA-OPER-VPN", "cloudLocalExitIfName"),
)
if mibBuilder.loadTexts:
    cloudLocalExitEntry.setStatus("current")


class _CloudLocalExitVpnId_Type(Unsigned32):
    """Custom type cloudLocalExitVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_CloudLocalExitVpnId_Type.__name__ = "Unsigned32"
_CloudLocalExitVpnId_Object = MibTableColumn
cloudLocalExitVpnId = _CloudLocalExitVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 2, 1, 1),
    _CloudLocalExitVpnId_Type()
)
cloudLocalExitVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cloudLocalExitVpnId.setStatus("current")
_CloudLocalExitAppName_Type = CloudExpressAppType
_CloudLocalExitAppName_Object = MibTableColumn
cloudLocalExitAppName = _CloudLocalExitAppName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 2, 1, 2),
    _CloudLocalExitAppName_Type()
)
cloudLocalExitAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cloudLocalExitAppName.setStatus("current")


class _CloudLocalExitIfName_Type(String):
    """Custom type cloudLocalExitIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CloudLocalExitIfName_Type.__name__ = "String"
_CloudLocalExitIfName_Object = MibTableColumn
cloudLocalExitIfName = _CloudLocalExitIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 2, 1, 3),
    _CloudLocalExitIfName_Type()
)
cloudLocalExitIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cloudLocalExitIfName.setStatus("current")
_CloudLocalExitLatency_Type = Unsigned32
_CloudLocalExitLatency_Object = MibTableColumn
cloudLocalExitLatency = _CloudLocalExitLatency_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 2, 1, 4),
    _CloudLocalExitLatency_Type()
)
cloudLocalExitLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudLocalExitLatency.setStatus("current")
_CloudLocalExitLoss_Type = Unsigned32
_CloudLocalExitLoss_Object = MibTableColumn
cloudLocalExitLoss = _CloudLocalExitLoss_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 2, 1, 5),
    _CloudLocalExitLoss_Type()
)
cloudLocalExitLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudLocalExitLoss.setStatus("current")
_CloudGatewayExitTable_Object = MibTable
cloudGatewayExitTable = _CloudGatewayExitTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 3)
)
if mibBuilder.loadTexts:
    cloudGatewayExitTable.setStatus("current")
_CloudGatewayExitEntry_Object = MibTableRow
cloudGatewayExitEntry = _CloudGatewayExitEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 3, 1)
)
cloudGatewayExitEntry.setIndexNames(
    (0, "VIPTELA-OPER-VPN", "cloudGatewayExitVpnId"),
    (0, "VIPTELA-OPER-VPN", "cloudGatewayExitAppName"),
    (0, "VIPTELA-OPER-VPN", "cloudGatewayExitIP"),
)
if mibBuilder.loadTexts:
    cloudGatewayExitEntry.setStatus("current")


class _CloudGatewayExitVpnId_Type(Unsigned32):
    """Custom type cloudGatewayExitVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_CloudGatewayExitVpnId_Type.__name__ = "Unsigned32"
_CloudGatewayExitVpnId_Object = MibTableColumn
cloudGatewayExitVpnId = _CloudGatewayExitVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 3, 1, 1),
    _CloudGatewayExitVpnId_Type()
)
cloudGatewayExitVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cloudGatewayExitVpnId.setStatus("current")
_CloudGatewayExitAppName_Type = CloudExpressAppType
_CloudGatewayExitAppName_Object = MibTableColumn
cloudGatewayExitAppName = _CloudGatewayExitAppName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 3, 1, 2),
    _CloudGatewayExitAppName_Type()
)
cloudGatewayExitAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cloudGatewayExitAppName.setStatus("current")
_CloudGatewayExitIP_Type = InetAddressIP
_CloudGatewayExitIP_Object = MibTableColumn
cloudGatewayExitIP = _CloudGatewayExitIP_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 3, 1, 3),
    _CloudGatewayExitIP_Type()
)
cloudGatewayExitIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cloudGatewayExitIP.setStatus("current")
_CloudGatewayExitLatency_Type = Unsigned32
_CloudGatewayExitLatency_Object = MibTableColumn
cloudGatewayExitLatency = _CloudGatewayExitLatency_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 3, 1, 4),
    _CloudGatewayExitLatency_Type()
)
cloudGatewayExitLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudGatewayExitLatency.setStatus("current")
_CloudGatewayExitLoss_Type = Unsigned32
_CloudGatewayExitLoss_Object = MibTableColumn
cloudGatewayExitLoss = _CloudGatewayExitLoss_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 3, 1, 5),
    _CloudGatewayExitLoss_Type()
)
cloudGatewayExitLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudGatewayExitLoss.setStatus("current")
_CloudGatewayExitLocalColor_Type = TlocColorEnum
_CloudGatewayExitLocalColor_Object = MibTableColumn
cloudGatewayExitLocalColor = _CloudGatewayExitLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 3, 1, 6),
    _CloudGatewayExitLocalColor_Type()
)
cloudGatewayExitLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudGatewayExitLocalColor.setStatus("current")
_CloudGatewayExitRemoteColor_Type = TlocColorEnum
_CloudGatewayExitRemoteColor_Object = MibTableColumn
cloudGatewayExitRemoteColor = _CloudGatewayExitRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 12, 20, 3, 1, 7),
    _CloudGatewayExitRemoteColor_Type()
)
cloudGatewayExitRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cloudGatewayExitRemoteColor.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-OPER-VPN",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
       "Ipv4Prefix": Ipv4Prefix,
       "InetAddressIP": InetAddressIP,
       "IpPrefix": IpPrefix,
       "String": String,
       "HexList": HexList,
       "IfAddressTypeEnum": IfAddressTypeEnum,
       "SfpPowerType": SfpPowerType,
       "SfpPhysicalIdentifierEnum": SfpPhysicalIdentifierEnum,
       "SfpConnectorTypeEnum": SfpConnectorTypeEnum,
       "SfpCalibrationType": SfpCalibrationType,
       "SfpRateSelectEnum": SfpRateSelectEnum,
       "SfpTransceiverComplianceEnum": SfpTransceiverComplianceEnum,
       "Yesno": Yesno,
       "VpnIfFlagsType": VpnIfFlagsType,
       "SfpTimingType": SfpTimingType,
       "SfpEncodingEnum": SfpEncodingEnum,
       "SfpHexBytes": SfpHexBytes,
       "T3": T3,
       "RouteStatusType": RouteStatusType,
       "VpnIfPauseType": VpnIfPauseType,
       "PppInterfaceAuthEnum": PppInterfaceAuthEnum,
       "CloudExpressAppType": CloudExpressAppType,
       "TlocColorEnum": TlocColorEnum,
       "viptela-oper-vpn": viptela_oper_vpn,
       "arpTable": arpTable,
       "arpEntry": arpEntry,
       "arpVpnId": arpVpnId,
       "arpIfName": arpIfName,
       "arpIp": arpIp,
       "arpMac": arpMac,
       "arpState": arpState,
       "arpIdleTimer": arpIdleTimer,
       "arpUptime": arpUptime,
       "interfaceTable": interfaceTable,
       "interfaceEntry": interfaceEntry,
       "interfaceVpnId": interfaceVpnId,
       "interfaceIfname": interfaceIfname,
       "interfaceIpAddress": interfaceIpAddress,
       "interfaceIpv6Address": interfaceIpv6Address,
       "interfaceIfAdminStatus": interfaceIfAdminStatus,
       "interfaceIfOperStatus": interfaceIfOperStatus,
       "interfaceDesc": interfaceDesc,
       "interfaceEncapType": interfaceEncapType,
       "interfacePortType": interfacePortType,
       "interfaceIfindex": interfaceIfindex,
       "interfaceMtu": interfaceMtu,
       "interfaceHwaddr": interfaceHwaddr,
       "interfaceSpeedMbps": interfaceSpeedMbps,
       "interfaceDuplex": interfaceDuplex,
       "interfaceAutoNeg": interfaceAutoNeg,
       "interfacePauseType": interfacePauseType,
       "interfaceTcpMssAdjust": interfaceTcpMssAdjust,
       "interfaceUptime": interfaceUptime,
       "interfaceAllowService": interfaceAllowService,
       "interfaceRxPackets": interfaceRxPackets,
       "interfaceRxOctets": interfaceRxOctets,
       "interfaceRxErrors": interfaceRxErrors,
       "interfaceRxDrops": interfaceRxDrops,
       "interfaceTxPackets": interfaceTxPackets,
       "interfaceTxOctets": interfaceTxOctets,
       "interfaceTxErrors": interfaceTxErrors,
       "interfaceTxDrops": interfaceTxDrops,
       "interfaceRxPps": interfaceRxPps,
       "interfaceRxKbps": interfaceRxKbps,
       "interfaceTxPps": interfaceTxPps,
       "interfaceTxKbps": interfaceTxKbps,
       "interfaceRxArpRequests": interfaceRxArpRequests,
       "interfaceTxArpReplies": interfaceTxArpReplies,
       "interfaceTxArpRequests": interfaceTxArpRequests,
       "interfaceRxArpReplies": interfaceRxArpReplies,
       "interfaceArpAddFails": interfaceArpAddFails,
       "interfaceRxArpReplyDrops": interfaceRxArpReplyDrops,
       "interfaceRxArpRateLimitDrops": interfaceRxArpRateLimitDrops,
       "interfaceTxArpRateLimitDrops": interfaceTxArpRateLimitDrops,
       "interfaceRxArpNonLocalDrops": interfaceRxArpNonLocalDrops,
       "interfaceTxArpRequestFail": interfaceTxArpRequestFail,
       "interfaceTxNoArpDrops": interfaceTxNoArpDrops,
       "interfaceRxIpTtlExpired": interfaceRxIpTtlExpired,
       "interfaceRxIpErrors": interfaceRxIpErrors,
       "interfaceInterfaceDisabled": interfaceInterfaceDisabled,
       "interfaceRxPolicerDrops": interfaceRxPolicerDrops,
       "interfaceRxNonIpDrops": interfaceRxNonIpDrops,
       "interfaceFilterDrops": interfaceFilterDrops,
       "interfaceMirrorDrops": interfaceMirrorDrops,
       "interfaceCpuPolicerDrops": interfaceCpuPolicerDrops,
       "interfaceTxIcmpPolicerDrops": interfaceTxIcmpPolicerDrops,
       "interfaceTxIcmpMirroredDrops": interfaceTxIcmpMirroredDrops,
       "interfaceSplitHorizonDrops": interfaceSplitHorizonDrops,
       "interfaceRouteLookupFail": interfaceRouteLookupFail,
       "interfaceBadLabel": interfaceBadLabel,
       "interfaceTxInterfaceDisabled": interfaceTxInterfaceDisabled,
       "interfaceRxMulticastPkts": interfaceRxMulticastPkts,
       "interfaceRxBroadcastPkts": interfaceRxBroadcastPkts,
       "interfaceTxMulticastPkts": interfaceTxMulticastPkts,
       "interfaceTxBroadcastPkts": interfaceTxBroadcastPkts,
       "interfaceRxPausePkts": interfaceRxPausePkts,
       "interfaceRxDmacFilterDrops": interfaceRxDmacFilterDrops,
       "interfaceRxWredDrops": interfaceRxWredDrops,
       "interfaceRxInterfaceNotFound": interfaceRxInterfaceNotFound,
       "interfaceRxInbErrors": interfaceRxInbErrors,
       "interfaceRxOversizeErrors": interfaceRxOversizeErrors,
       "interfaceRxFcsAlignErrors": interfaceRxFcsAlignErrors,
       "interfaceRxUndersizeErrors": interfaceRxUndersizeErrors,
       "interfaceTxUnderflowPkts": interfaceTxUnderflowPkts,
       "interfaceTxCollisionDrops": interfaceTxCollisionDrops,
       "interfaceTxPausePkts": interfaceTxPausePkts,
       "interfaceTxFragmentsNeeded": interfaceTxFragmentsNeeded,
       "interfaceTxFragments": interfaceTxFragments,
       "interfaceTxFragmentDrops": interfaceTxFragmentDrops,
       "interfaceTxTailRedDrops": interfaceTxTailRedDrops,
       "interfaceLlqDrops": interfaceLlqDrops,
       "interfaceRxPktSize64": interfaceRxPktSize64,
       "interfaceRxPktSizeLt64": interfaceRxPktSizeLt64,
       "interfaceRxPktSize65127": interfaceRxPktSize65127,
       "interfaceRxPktSize128255": interfaceRxPktSize128255,
       "interfaceRxPktSize256511": interfaceRxPktSize256511,
       "interfaceRxPktSize5121023": interfaceRxPktSize5121023,
       "interfaceRxPktSize10241518": interfaceRxPktSize10241518,
       "interfaceRxPktSizeGt1518": interfaceRxPktSizeGt1518,
       "interfaceTxPktSize64": interfaceTxPktSize64,
       "interfaceTxPktSizeLt64": interfaceTxPktSizeLt64,
       "interfaceTxPktSize65127": interfaceTxPktSize65127,
       "interfaceTxPktSize128255": interfaceTxPktSize128255,
       "interfaceTxPktSize256511": interfaceTxPktSize256511,
       "interfaceTxPktSize5121023": interfaceTxPktSize5121023,
       "interfaceTxPktSize10241518": interfaceTxPktSize10241518,
       "interfaceTxPktSizeGt1518": interfaceTxPktSizeGt1518,
       "interfaceNumFlaps": interfaceNumFlaps,
       "interfacePppoeEnabledInterface": interfacePppoeEnabledInterface,
       "interfacePppoeTxPkts": interfacePppoeTxPkts,
       "interfacePppoeRxPkts": interfacePppoeRxPkts,
       "interfaceBandwidthUpstream": interfaceBandwidthUpstream,
       "interfaceBandwidthDownstream": interfaceBandwidthDownstream,
       "interfaceAfType": interfaceAfType,
       "interfaceLinkLocalAddress": interfaceLinkLocalAddress,
       "interfaceShapingRate": interfaceShapingRate,
       "interfaceDot1xTxPkts": interfaceDot1xTxPkts,
       "interfaceDot1xRxPkts": interfaceDot1xRxPkts,
       "interfaceRxPolicerRemark": interfaceRxPolicerRemark,
       "interfaceIfTrackerStatus": interfaceIfTrackerStatus,
       "interfaceAddrType": interfaceAddrType,
       "interfaceIcmpRedirectTxDrops": interfaceIcmpRedirectTxDrops,
       "interfaceIcmpRedirectRxDrops": interfaceIcmpRedirectRxDrops,
       "interfaceDevicePolicyDrops": interfaceDevicePolicyDrops,
       "nd6Table": nd6Table,
       "nd6Entry": nd6Entry,
       "nd6VpnId": nd6VpnId,
       "nd6IfName": nd6IfName,
       "nd6Ip": nd6Ip,
       "nd6Mac": nd6Mac,
       "nd6State": nd6State,
       "nd6IdleTimer": nd6IdleTimer,
       "nd6Uptime": nd6Uptime,
       "interfaceIfAddrTable": interfaceIfAddrTable,
       "interfaceIfAddrEntry": interfaceIfAddrEntry,
       "interfaceIfAddrAddrId": interfaceIfAddrAddrId,
       "interfaceIfAddrIpAddress": interfaceIfAddrIpAddress,
       "interfaceIfAddrBroadcastAddr": interfaceIfAddrBroadcastAddr,
       "interfaceIfAddrSecondary": interfaceIfAddrSecondary,
       "interfaceQueueTable": interfaceQueueTable,
       "interfaceQueueEntry": interfaceQueueEntry,
       "interfaceQueueQnum": interfaceQueueQnum,
       "interfaceQueueQueuedPackets": interfaceQueueQueuedPackets,
       "interfaceQueueQueuedBytes": interfaceQueueQueuedBytes,
       "interfaceQueueTailDropPackets": interfaceQueueTailDropPackets,
       "interfaceQueueTailDropBytes": interfaceQueueTailDropBytes,
       "interfaceQueueRedDropPackets": interfaceQueueRedDropPackets,
       "interfaceQueueRedDropBytes": interfaceQueueRedDropBytes,
       "interfaceQueueTxPackets": interfaceQueueTxPackets,
       "interfaceQueueTxBytes": interfaceQueueTxBytes,
       "interfaceQueueQueueDepth": interfaceQueueQueueDepth,
       "interfaceQueueMaxDepth": interfaceQueueMaxDepth,
       "interfaceQueueAvgQueue": interfaceQueueAvgQueue,
       "interfaceQueueQueuePps": interfaceQueueQueuePps,
       "interfaceQueueQueueDropPps": interfaceQueueQueueDropPps,
       "app": app,
       "appCflowd": appCflowd,
       "appCflowdFlowsTable": appCflowdFlowsTable,
       "appCflowdFlowsEntry": appCflowdFlowsEntry,
       "appCflowdFlowsVpnId": appCflowdFlowsVpnId,
       "appCflowdFlowsSrcIp": appCflowdFlowsSrcIp,
       "appCflowdFlowsDestIp": appCflowdFlowsDestIp,
       "appCflowdFlowsSrcPort": appCflowdFlowsSrcPort,
       "appCflowdFlowsDestPort": appCflowdFlowsDestPort,
       "appCflowdFlowsDscp": appCflowdFlowsDscp,
       "appCflowdFlowsIpProto": appCflowdFlowsIpProto,
       "appCflowdFlowsTcpCntrlBits": appCflowdFlowsTcpCntrlBits,
       "appCflowdFlowsIcmpOpcode": appCflowdFlowsIcmpOpcode,
       "appCflowdFlowsNhopIp": appCflowdFlowsNhopIp,
       "appCflowdFlowsEgressIntf": appCflowdFlowsEgressIntf,
       "appCflowdFlowsIngressIntf": appCflowdFlowsIngressIntf,
       "appCflowdFlowsTotalPkts": appCflowdFlowsTotalPkts,
       "appCflowdFlowsTotalBytes": appCflowdFlowsTotalBytes,
       "appCflowdFlowsMinLen": appCflowdFlowsMinLen,
       "appCflowdFlowsMaxLen": appCflowdFlowsMaxLen,
       "appCflowdFlowsStartTime": appCflowdFlowsStartTime,
       "appCflowdFlowsTimeToExpire": appCflowdFlowsTimeToExpire,
       "appCflowdFlowsEgressIntfName": appCflowdFlowsEgressIntfName,
       "appCflowdFlowsIngressIntfName": appCflowdFlowsIngressIntfName,
       "appCflowdFlowsAppID": appCflowdFlowsAppID,
       "appCflowdCollectorTable": appCflowdCollectorTable,
       "appCflowdCollectorEntry": appCflowdCollectorEntry,
       "appCflowdCollectorVpnId": appCflowdCollectorVpnId,
       "appCflowdCollectorIpAddress": appCflowdCollectorIpAddress,
       "appCflowdCollectorPort": appCflowdCollectorPort,
       "appCflowdCollectorProto": appCflowdCollectorProto,
       "appCflowdCollectorConnectionUp": appCflowdCollectorConnectionUp,
       "appCflowdCollectorIpfix": appCflowdCollectorIpfix,
       "appCflowdCollectorConnectionRetry": appCflowdCollectorConnectionRetry,
       "appCflowdCollectorTemplatePackets": appCflowdCollectorTemplatePackets,
       "appCflowdCollectorDataPackets": appCflowdCollectorDataPackets,
       "appCflowdCollectorDroppedPackets": appCflowdCollectorDroppedPackets,
       "appCflowdCollectorSourceInterface": appCflowdCollectorSourceInterface,
       "appCflowdStatistics": appCflowdStatistics,
       "appCflowdStatisticsDataPackets": appCflowdStatisticsDataPackets,
       "appCflowdStatisticsTemplatePackets": appCflowdStatisticsTemplatePackets,
       "appCflowdStatisticsTotalPackets": appCflowdStatisticsTotalPackets,
       "appCflowdStatisticsFlowRefresh": appCflowdStatisticsFlowRefresh,
       "appCflowdStatisticsFlowAgeout": appCflowdStatisticsFlowAgeout,
       "appCflowdStatisticsFlowEndDetected": appCflowdStatisticsFlowEndDetected,
       "appCflowdStatisticsFlowEndForced": appCflowdStatisticsFlowEndForced,
       "appCflowdTemplate": appCflowdTemplate,
       "appCflowdTemplateName": appCflowdTemplateName,
       "appCflowdTemplateFlowActiveTimeout": appCflowdTemplateFlowActiveTimeout,
       "appCflowdTemplateFlowInactiveTimeout": appCflowdTemplateFlowInactiveTimeout,
       "appCflowdTemplateTemplateRefresh": appCflowdTemplateTemplateRefresh,
       "appCflowdFlowCountTable": appCflowdFlowCountTable,
       "appCflowdFlowCountEntry": appCflowdFlowCountEntry,
       "appCflowdFlowCountVpnId": appCflowdFlowCountVpnId,
       "appCflowdFlowCountCount": appCflowdFlowCountCount,
       "appDpi": appDpi,
       "appDpiApplicationsTable": appDpiApplicationsTable,
       "appDpiApplicationsEntry": appDpiApplicationsEntry,
       "appDpiApplicationsVpnId": appDpiApplicationsVpnId,
       "appDpiApplicationsSrcIp": appDpiApplicationsSrcIp,
       "appDpiApplicationsApplication": appDpiApplicationsApplication,
       "appDpiApplicationsFamily": appDpiApplicationsFamily,
       "appDpiApplicationsTotalFlows": appDpiApplicationsTotalFlows,
       "appDpiApplicationsExpiredFlows": appDpiApplicationsExpiredFlows,
       "appDpiApplicationsLastSeen": appDpiApplicationsLastSeen,
       "appDpiApplicationsPackets": appDpiApplicationsPackets,
       "appDpiApplicationsOctets": appDpiApplicationsOctets,
       "appDpiFlowsTable": appDpiFlowsTable,
       "appDpiFlowsEntry": appDpiFlowsEntry,
       "appDpiFlowsVpnId": appDpiFlowsVpnId,
       "appDpiFlowsSrcIp": appDpiFlowsSrcIp,
       "appDpiFlowsDstIp": appDpiFlowsDstIp,
       "appDpiFlowsSrcPort": appDpiFlowsSrcPort,
       "appDpiFlowsDstPort": appDpiFlowsDstPort,
       "appDpiFlowsProto": appDpiFlowsProto,
       "appDpiFlowsApplication": appDpiFlowsApplication,
       "appDpiFlowsFamily": appDpiFlowsFamily,
       "appDpiFlowsActiveSince": appDpiFlowsActiveSince,
       "appDpiFlowsPackets": appDpiFlowsPackets,
       "appDpiFlowsOctets": appDpiFlowsOctets,
       "appDpiSupportedApplicationsTable": appDpiSupportedApplicationsTable,
       "appDpiSupportedApplicationsEntry": appDpiSupportedApplicationsEntry,
       "appDpiSupportedApplicationsApplication": appDpiSupportedApplicationsApplication,
       "appDpiSupportedApplicationsFamily": appDpiSupportedApplicationsFamily,
       "appDpiSupportedApplicationsAppLongName": appDpiSupportedApplicationsAppLongName,
       "appDpiSupportedApplicationsFamilyLongName": appDpiSupportedApplicationsFamilyLongName,
       "appDpiSupportedApplicationsAppId": appDpiSupportedApplicationsAppId,
       "appDpiSummary": appDpiSummary,
       "appDpiSummaryStatus": appDpiSummaryStatus,
       "appDpiSummaryFlowsCreated": appDpiSummaryFlowsCreated,
       "appDpiSummaryFlowsExpired": appDpiSummaryFlowsExpired,
       "appDpiSummaryCurrentFlows": appDpiSummaryCurrentFlows,
       "appDpiSummaryPeakFlows": appDpiSummaryPeakFlows,
       "appDpiSummaryCurrentRate": appDpiSummaryCurrentRate,
       "appDpiSummaryPeakRate": appDpiSummaryPeakRate,
       "appDpiFlowsTunnelsInTable": appDpiFlowsTunnelsInTable,
       "appDpiFlowsTunnelsInEntry": appDpiFlowsTunnelsInEntry,
       "appDpiFlowsTunnelsInIndex": appDpiFlowsTunnelsInIndex,
       "appDpiFlowsTunnelsInLocalTlocIp": appDpiFlowsTunnelsInLocalTlocIp,
       "appDpiFlowsTunnelsInLocalTlocColor": appDpiFlowsTunnelsInLocalTlocColor,
       "appDpiFlowsTunnelsInLocalTlocEncap": appDpiFlowsTunnelsInLocalTlocEncap,
       "appDpiFlowsTunnelsInRemoteTlocIp": appDpiFlowsTunnelsInRemoteTlocIp,
       "appDpiFlowsTunnelsInRemoteTlocColor": appDpiFlowsTunnelsInRemoteTlocColor,
       "appDpiFlowsTunnelsInRemoteTlocEncap": appDpiFlowsTunnelsInRemoteTlocEncap,
       "appDpiFlowsTunnelsInPackets": appDpiFlowsTunnelsInPackets,
       "appDpiFlowsTunnelsInOctets": appDpiFlowsTunnelsInOctets,
       "appDpiFlowsTunnelsInStartTime": appDpiFlowsTunnelsInStartTime,
       "appDpiFlowsTunnelsOutTable": appDpiFlowsTunnelsOutTable,
       "appDpiFlowsTunnelsOutEntry": appDpiFlowsTunnelsOutEntry,
       "appDpiFlowsTunnelsOutIndex": appDpiFlowsTunnelsOutIndex,
       "appDpiFlowsTunnelsOutLocalTlocIp": appDpiFlowsTunnelsOutLocalTlocIp,
       "appDpiFlowsTunnelsOutLocalTlocColor": appDpiFlowsTunnelsOutLocalTlocColor,
       "appDpiFlowsTunnelsOutLocalTlocEncap": appDpiFlowsTunnelsOutLocalTlocEncap,
       "appDpiFlowsTunnelsOutRemoteTlocIp": appDpiFlowsTunnelsOutRemoteTlocIp,
       "appDpiFlowsTunnelsOutRemoteTlocColor": appDpiFlowsTunnelsOutRemoteTlocColor,
       "appDpiFlowsTunnelsOutRemoteTlocEncap": appDpiFlowsTunnelsOutRemoteTlocEncap,
       "appDpiFlowsTunnelsOutPackets": appDpiFlowsTunnelsOutPackets,
       "appDpiFlowsTunnelsOutOctets": appDpiFlowsTunnelsOutOctets,
       "appDpiFlowsTunnelsOutStartTime": appDpiFlowsTunnelsOutStartTime,
       "appLog": appLog,
       "appLogFlowsTable": appLogFlowsTable,
       "appLogFlowsEntry": appLogFlowsEntry,
       "appLogFlowsVpnId": appLogFlowsVpnId,
       "appLogFlowsSrcIp": appLogFlowsSrcIp,
       "appLogFlowsDestIp": appLogFlowsDestIp,
       "appLogFlowsSrcPort": appLogFlowsSrcPort,
       "appLogFlowsDestPort": appLogFlowsDestPort,
       "appLogFlowsDscp": appLogFlowsDscp,
       "appLogFlowsIpProto": appLogFlowsIpProto,
       "appLogFlowsTcpCntrlBits": appLogFlowsTcpCntrlBits,
       "appLogFlowsIcmpOpcode": appLogFlowsIcmpOpcode,
       "appLogFlowsNhopIp": appLogFlowsNhopIp,
       "appLogFlowsTotalPkts": appLogFlowsTotalPkts,
       "appLogFlowsTotalBytes": appLogFlowsTotalBytes,
       "appLogFlowsStartTime": appLogFlowsStartTime,
       "appLogFlowsTimeToExpire": appLogFlowsTimeToExpire,
       "appLogFlowsEgressIntfName": appLogFlowsEgressIntfName,
       "appLogFlowsIngressIntfName": appLogFlowsIngressIntfName,
       "appLogFlowsPolicyName": appLogFlowsPolicyName,
       "appLogFlowsPolicyAction": appLogFlowsPolicyAction,
       "appLogFlowsPolicyDirection": appLogFlowsPolicyDirection,
       "appLogFlowCountTable": appLogFlowCountTable,
       "appLogFlowCountEntry": appLogFlowCountEntry,
       "appLogFlowCountVpnId": appLogFlowCountVpnId,
       "appLogFlowCountCount": appLogFlowCountCount,
       "appTcpOpt": appTcpOpt,
       "appTcpOptActiveFlowsTable": appTcpOptActiveFlowsTable,
       "appTcpOptActiveFlowsEntry": appTcpOptActiveFlowsEntry,
       "appTcpOptActiveFlowsVpnId": appTcpOptActiveFlowsVpnId,
       "appTcpOptActiveFlowsSrcIp": appTcpOptActiveFlowsSrcIp,
       "appTcpOptActiveFlowsDestIp": appTcpOptActiveFlowsDestIp,
       "appTcpOptActiveFlowsSrcPort": appTcpOptActiveFlowsSrcPort,
       "appTcpOptActiveFlowsDestPort": appTcpOptActiveFlowsDestPort,
       "appTcpOptActiveFlowsStartTime": appTcpOptActiveFlowsStartTime,
       "appTcpOptActiveFlowsEgressIntfName": appTcpOptActiveFlowsEgressIntfName,
       "appTcpOptActiveFlowsIngressIntfName": appTcpOptActiveFlowsIngressIntfName,
       "appTcpOptActiveFlowsTxBytes": appTcpOptActiveFlowsTxBytes,
       "appTcpOptActiveFlowsRxBytes": appTcpOptActiveFlowsRxBytes,
       "appTcpOptActiveFlowsTcpState": appTcpOptActiveFlowsTcpState,
       "appTcpOptActiveFlowsUnoptReason": appTcpOptActiveFlowsUnoptReason,
       "appTcpOptActiveFlowsProxyIdentity": appTcpOptActiveFlowsProxyIdentity,
       "appTcpOptExpiredFlowsTable": appTcpOptExpiredFlowsTable,
       "appTcpOptExpiredFlowsEntry": appTcpOptExpiredFlowsEntry,
       "appTcpOptExpiredFlowsTimestamp": appTcpOptExpiredFlowsTimestamp,
       "appTcpOptExpiredFlowsVpnId": appTcpOptExpiredFlowsVpnId,
       "appTcpOptExpiredFlowsSrcIp": appTcpOptExpiredFlowsSrcIp,
       "appTcpOptExpiredFlowsDestIp": appTcpOptExpiredFlowsDestIp,
       "appTcpOptExpiredFlowsSrcPort": appTcpOptExpiredFlowsSrcPort,
       "appTcpOptExpiredFlowsDestPort": appTcpOptExpiredFlowsDestPort,
       "appTcpOptExpiredFlowsStartTime": appTcpOptExpiredFlowsStartTime,
       "appTcpOptExpiredFlowsEndTime": appTcpOptExpiredFlowsEndTime,
       "appTcpOptExpiredFlowsTxBytes": appTcpOptExpiredFlowsTxBytes,
       "appTcpOptExpiredFlowsRxBytes": appTcpOptExpiredFlowsRxBytes,
       "appTcpOptExpiredFlowsTcpState": appTcpOptExpiredFlowsTcpState,
       "appTcpOptExpiredFlowsUnoptReason": appTcpOptExpiredFlowsUnoptReason,
       "appTcpOptExpiredFlowsProxyIdentity": appTcpOptExpiredFlowsProxyIdentity,
       "appTcpOptExpiredFlowsDeleteReason": appTcpOptExpiredFlowsDeleteReason,
       "appTcpOptSummary": appTcpOptSummary,
       "appTcpOptSummaryFlowsOptimized": appTcpOptSummaryFlowsOptimized,
       "appTcpOptSummaryFlowsPassthrough": appTcpOptSummaryFlowsPassthrough,
       "appTcpOptSummaryFlowsInProgress": appTcpOptSummaryFlowsInProgress,
       "appTcpOptSummaryFlowsExpired": appTcpOptSummaryFlowsExpired,
       "appTcpOptSummaryFlowsCloseWait": appTcpOptSummaryFlowsCloseWait,
       "appTcpOptSummaryFlowsUntracked": appTcpOptSummaryFlowsUntracked,
       "ip": ip,
       "ipRoutesTableTable": ipRoutesTableTable,
       "ipRoutesTableEntry": ipRoutesTableEntry,
       "ipRoutesTableVpnId": ipRoutesTableVpnId,
       "ipRoutesTableAddressFamily": ipRoutesTableAddressFamily,
       "ipRoutesTablePrefix": ipRoutesTablePrefix,
       "ipRoutesTablePathId": ipRoutesTablePathId,
       "ipRoutesTableProtocol": ipRoutesTableProtocol,
       "ipRoutesTableProtocolSubType": ipRoutesTableProtocolSubType,
       "ipRoutesTableDistance": ipRoutesTableDistance,
       "ipRoutesTableMetric": ipRoutesTableMetric,
       "ipRoutesTableUptime": ipRoutesTableUptime,
       "ipRoutesTablePathFlags": ipRoutesTablePathFlags,
       "ipRoutesTableNexthopFlags": ipRoutesTableNexthopFlags,
       "ipRoutesTableNexthopType": ipRoutesTableNexthopType,
       "ipRoutesTableNexthopIfname": ipRoutesTableNexthopIfname,
       "ipRoutesTableNexthopAddr": ipRoutesTableNexthopAddr,
       "ipRoutesTableNexthopRtype": ipRoutesTableNexthopRtype,
       "ipRoutesTableNexthopRifname": ipRoutesTableNexthopRifname,
       "ipRoutesTableNexthopRaddr": ipRoutesTableNexthopRaddr,
       "ipRoutesTableNexthopRsrc": ipRoutesTableNexthopRsrc,
       "ipRoutesTableIp": ipRoutesTableIp,
       "ipRoutesTableColor": ipRoutesTableColor,
       "ipRoutesTableEncap": ipRoutesTableEncap,
       "ipRoutesTableNexthopVpn": ipRoutesTableNexthopVpn,
       "ipRoutesTableNexthopLabel": ipRoutesTableNexthopLabel,
       "ipRoutesTableRstatus": ipRoutesTableRstatus,
       "ipRoutesTableOmpTag": ipRoutesTableOmpTag,
       "ipRoutesTableOspfTag": ipRoutesTableOspfTag,
       "ipLongerRoutesTableTable": ipLongerRoutesTableTable,
       "ipLongerRoutesTableEntry": ipLongerRoutesTableEntry,
       "ipLongerRoutesTableVpnId": ipLongerRoutesTableVpnId,
       "ipLongerRoutesTableAddressFamily": ipLongerRoutesTableAddressFamily,
       "ipLongerRoutesTablePrefix": ipLongerRoutesTablePrefix,
       "ipLongerRoutesTableLongerPrefix": ipLongerRoutesTableLongerPrefix,
       "ipLongerRoutesTablePathId": ipLongerRoutesTablePathId,
       "ipLongerRoutesTableProtocol": ipLongerRoutesTableProtocol,
       "ipLongerRoutesTableProtocolSubType": ipLongerRoutesTableProtocolSubType,
       "ipLongerRoutesTableDistance": ipLongerRoutesTableDistance,
       "ipLongerRoutesTableMetric": ipLongerRoutesTableMetric,
       "ipLongerRoutesTableUptime": ipLongerRoutesTableUptime,
       "ipLongerRoutesTablePathFlags": ipLongerRoutesTablePathFlags,
       "ipLongerRoutesTableNexthopFlags": ipLongerRoutesTableNexthopFlags,
       "ipLongerRoutesTableNexthopType": ipLongerRoutesTableNexthopType,
       "ipLongerRoutesTableNexthopIfname": ipLongerRoutesTableNexthopIfname,
       "ipLongerRoutesTableNexthopAddr": ipLongerRoutesTableNexthopAddr,
       "ipLongerRoutesTableNexthopRtype": ipLongerRoutesTableNexthopRtype,
       "ipLongerRoutesTableNexthopRifname": ipLongerRoutesTableNexthopRifname,
       "ipLongerRoutesTableNexthopRaddr": ipLongerRoutesTableNexthopRaddr,
       "ipLongerRoutesTableNexthopRsrc": ipLongerRoutesTableNexthopRsrc,
       "ipLongerRoutesTableTlocIp": ipLongerRoutesTableTlocIp,
       "ipLongerRoutesTableTlocColor": ipLongerRoutesTableTlocColor,
       "ipLongerRoutesTableTlocEncap": ipLongerRoutesTableTlocEncap,
       "ipLongerRoutesTableNexthopVpn": ipLongerRoutesTableNexthopVpn,
       "ipLongerRoutesTableNexthopLabel": ipLongerRoutesTableNexthopLabel,
       "ipLongerRoutesTableRstatus": ipLongerRoutesTableRstatus,
       "ipLongerRoutesTableOmpTag": ipLongerRoutesTableOmpTag,
       "ipLongerRoutesTableOspfTag": ipLongerRoutesTableOspfTag,
       "ipBestMatchRouteTable": ipBestMatchRouteTable,
       "ipBestMatchRouteEntry": ipBestMatchRouteEntry,
       "ipBestMatchRouteVpnId": ipBestMatchRouteVpnId,
       "ipBestMatchRouteAddressFamily": ipBestMatchRouteAddressFamily,
       "ipBestMatchRouteDestination": ipBestMatchRouteDestination,
       "ipBestMatchRoutePathId": ipBestMatchRoutePathId,
       "ipBestMatchRoutePrefix": ipBestMatchRoutePrefix,
       "ipBestMatchRouteProtocol": ipBestMatchRouteProtocol,
       "ipBestMatchRouteProtocolSubType": ipBestMatchRouteProtocolSubType,
       "ipBestMatchRouteDistance": ipBestMatchRouteDistance,
       "ipBestMatchRouteMetric": ipBestMatchRouteMetric,
       "ipBestMatchRouteUptime": ipBestMatchRouteUptime,
       "ipBestMatchRoutePathFlags": ipBestMatchRoutePathFlags,
       "ipBestMatchRouteNexthopFlags": ipBestMatchRouteNexthopFlags,
       "ipBestMatchRouteNexthopType": ipBestMatchRouteNexthopType,
       "ipBestMatchRouteNexthopIfname": ipBestMatchRouteNexthopIfname,
       "ipBestMatchRouteNexthopAddr": ipBestMatchRouteNexthopAddr,
       "ipBestMatchRouteNexthopRtype": ipBestMatchRouteNexthopRtype,
       "ipBestMatchRouteNexthopRifname": ipBestMatchRouteNexthopRifname,
       "ipBestMatchRouteNexthopRaddr": ipBestMatchRouteNexthopRaddr,
       "ipBestMatchRouteNexthopRsrc": ipBestMatchRouteNexthopRsrc,
       "ipBestMatchRouteTlocIp": ipBestMatchRouteTlocIp,
       "ipBestMatchRouteTlocColor": ipBestMatchRouteTlocColor,
       "ipBestMatchRouteTlocEncap": ipBestMatchRouteTlocEncap,
       "ipBestMatchRouteNexthopLabel": ipBestMatchRouteNexthopLabel,
       "ipBestMatchRouteRstatus": ipBestMatchRouteRstatus,
       "ipBestMatchRouteOmpTag": ipBestMatchRouteOmpTag,
       "ipBestMatchRouteNexthopVpn": ipBestMatchRouteNexthopVpn,
       "ipBestMatchRouteOspfTag": ipBestMatchRouteOspfTag,
       "ipMfib": ipMfib,
       "ipMfibSummaryTable": ipMfibSummaryTable,
       "ipMfibSummaryEntry": ipMfibSummaryEntry,
       "ipMfibSummaryVpnId": ipMfibSummaryVpnId,
       "ipMfibSummaryGroup": ipMfibSummaryGroup,
       "ipMfibSummarySource": ipMfibSummarySource,
       "ipMfibSummaryUpstreamIf": ipMfibSummaryUpstreamIf,
       "ipMfibSummaryUpstreamTunnel": ipMfibSummaryUpstreamTunnel,
       "ipMfibSummaryNumServiceOils": ipMfibSummaryNumServiceOils,
       "ipMfibSummaryNumTunnelOils": ipMfibSummaryNumTunnelOils,
       "ipMfibOilTable": ipMfibOilTable,
       "ipMfibOilEntry": ipMfibOilEntry,
       "ipMfibOilVpnId": ipMfibOilVpnId,
       "ipMfibOilGroup": ipMfibOilGroup,
       "ipMfibOilSource": ipMfibOilSource,
       "ipMfibStatsTable": ipMfibStatsTable,
       "ipMfibStatsEntry": ipMfibStatsEntry,
       "ipMfibStatsVpnId": ipMfibStatsVpnId,
       "ipMfibStatsGroup": ipMfibStatsGroup,
       "ipMfibStatsSource": ipMfibStatsSource,
       "ipMfibStatsRxPkts": ipMfibStatsRxPkts,
       "ipMfibStatsRxOctets": ipMfibStatsRxOctets,
       "ipMfibStatsTxPkts": ipMfibStatsTxPkts,
       "ipMfibStatsTxOctets": ipMfibStatsTxOctets,
       "ipMfibStatsTxToPimPkts": ipMfibStatsTxToPimPkts,
       "ipMfibStatsRxPacketRate": ipMfibStatsRxPacketRate,
       "ipMfibStatsRxOctetRate": ipMfibStatsRxOctetRate,
       "ipMfibStatsTxPacketRate": ipMfibStatsTxPacketRate,
       "ipMfibStatsTxOctetRate": ipMfibStatsTxOctetRate,
       "ipMfibStatsAvgReplication": ipMfibStatsAvgReplication,
       "ipMfibStatsRpfFailure": ipMfibStatsRpfFailure,
       "ipMfibStatsTxInvalidOilFailure": ipMfibStatsTxInvalidOilFailure,
       "ipMfibStatsTxFailure": ipMfibStatsTxFailure,
       "ipMfibStatsRxPolicyDrop": ipMfibStatsRxPolicyDrop,
       "ipMfibStatsTxPolicyDrop": ipMfibStatsTxPolicyDrop,
       "ipFibTable": ipFibTable,
       "ipFibEntry": ipFibEntry,
       "ipFibVpnId": ipFibVpnId,
       "ipFibPrefix": ipFibPrefix,
       "ipFibPathId": ipFibPathId,
       "ipFibOutIfname": ipFibOutIfname,
       "ipFibNexthopAddress": ipFibNexthopAddress,
       "ipFibNexthopLabel": ipFibNexthopLabel,
       "ipFibSaIndex": ipFibSaIndex,
       "ipFibIp": ipFibIp,
       "ipFibColor": ipFibColor,
       "ipFibAddressFamily": ipFibAddressFamily,
       "ipFibNexthopVpn": ipFibNexthopVpn,
       "ipNat": ipNat,
       "ipNatInterfaceTable": ipNatInterfaceTable,
       "ipNatInterfaceEntry": ipNatInterfaceEntry,
       "ipNatInterfaceVpnId": ipNatInterfaceVpnId,
       "ipNatInterfaceIfname": ipNatInterfaceIfname,
       "ipNatInterfaceMappingType": ipNatInterfaceMappingType,
       "ipNatInterfaceFilterType": ipNatInterfaceFilterType,
       "ipNatInterfaceFilterCount": ipNatInterfaceFilterCount,
       "ipNatInterfaceFibFilterCount": ipNatInterfaceFibFilterCount,
       "ipNatInterfaceIp": ipNatInterfaceIp,
       "ipNatInterfaceNumberIpPools": ipNatInterfaceNumberIpPools,
       "ipNatInterfaceStatisticsTable": ipNatInterfaceStatisticsTable,
       "ipNatInterfaceStatisticsEntry": ipNatInterfaceStatisticsEntry,
       "ipNatInterfaceStatisticsVpnId": ipNatInterfaceStatisticsVpnId,
       "ipNatInterfaceStatisticsIfname": ipNatInterfaceStatisticsIfname,
       "ipNatInterfaceStatisticsNatOutboundPackets": ipNatInterfaceStatisticsNatOutboundPackets,
       "ipNatInterfaceStatisticsNatInboundPackets": ipNatInterfaceStatisticsNatInboundPackets,
       "ipNatInterfaceStatisticsNatEncodeFail": ipNatInterfaceStatisticsNatEncodeFail,
       "ipNatInterfaceStatisticsNatDecodeFail": ipNatInterfaceStatisticsNatDecodeFail,
       "ipNatInterfaceStatisticsNatMapAddFail": ipNatInterfaceStatisticsNatMapAddFail,
       "ipNatInterfaceStatisticsNatFilterAddFail": ipNatInterfaceStatisticsNatFilterAddFail,
       "ipNatInterfaceStatisticsNatFilterLookupFail": ipNatInterfaceStatisticsNatFilterLookupFail,
       "ipNatInterfaceStatisticsNatStateCheckFail": ipNatInterfaceStatisticsNatStateCheckFail,
       "ipNatInterfaceStatisticsNatPolicerDrops": ipNatInterfaceStatisticsNatPolicerDrops,
       "ipNatInterfaceStatisticsOutboundIcmpError": ipNatInterfaceStatisticsOutboundIcmpError,
       "ipNatInterfaceStatisticsInboundIcmpError": ipNatInterfaceStatisticsInboundIcmpError,
       "ipNatInterfaceStatisticsInboundIcmpErrorDrops": ipNatInterfaceStatisticsInboundIcmpErrorDrops,
       "ipNatInterfaceStatisticsNatFragments": ipNatInterfaceStatisticsNatFragments,
       "ipNatInterfaceStatisticsNatFragmentsFail": ipNatInterfaceStatisticsNatFragmentsFail,
       "ipNatInterfaceStatisticsNatUnsupportedProto": ipNatInterfaceStatisticsNatUnsupportedProto,
       "ipNatInterfaceStatisticsNatMapNoPorts": ipNatInterfaceStatisticsNatMapNoPorts,
       "ipNatInterfaceStatisticsNatMapCannotXlate": ipNatInterfaceStatisticsNatMapCannotXlate,
       "ipNatInterfaceStatisticsNatFilterMapMismatch": ipNatInterfaceStatisticsNatFilterMapMismatch,
       "ipNatInterfaceStatisticsNatMapIpPoolExhausted": ipNatInterfaceStatisticsNatMapIpPoolExhausted,
       "ipNatFilterTable": ipNatFilterTable,
       "ipNatFilterEntry": ipNatFilterEntry,
       "ipNatFilterNatVpnId": ipNatFilterNatVpnId,
       "ipNatFilterNatIfname": ipNatFilterNatIfname,
       "ipNatFilterPrivateVpnId": ipNatFilterPrivateVpnId,
       "ipNatFilterProto": ipNatFilterProto,
       "ipNatFilterPrivateSourceAddress": ipNatFilterPrivateSourceAddress,
       "ipNatFilterPrivateDestAddress": ipNatFilterPrivateDestAddress,
       "ipNatFilterPrivateSourcePort": ipNatFilterPrivateSourcePort,
       "ipNatFilterPrivateDestPort": ipNatFilterPrivateDestPort,
       "ipNatFilterPublicSourceAddress": ipNatFilterPublicSourceAddress,
       "ipNatFilterPublicDestAddress": ipNatFilterPublicDestAddress,
       "ipNatFilterPublicSourcePort": ipNatFilterPublicSourcePort,
       "ipNatFilterPublicDestPort": ipNatFilterPublicDestPort,
       "ipNatFilterFilterState": ipNatFilterFilterState,
       "ipNatFilterIdleTimeout": ipNatFilterIdleTimeout,
       "ipNatFilterOutboundPackets": ipNatFilterOutboundPackets,
       "ipNatFilterOutboundOctets": ipNatFilterOutboundOctets,
       "ipNatFilterInboundPackets": ipNatFilterInboundPackets,
       "ipNatFilterInboundOctets": ipNatFilterInboundOctets,
       "ipNatFilterDirection": ipNatFilterDirection,
       "ipRoutesSummaryTable": ipRoutesSummaryTable,
       "ipRoutesSummaryEntry": ipRoutesSummaryEntry,
       "ipRoutesSummaryVpnId": ipRoutesSummaryVpnId,
       "ipRoutesSummaryAddressFamily": ipRoutesSummaryAddressFamily,
       "ipRoutesSummaryRouteProtocol": ipRoutesSummaryRouteProtocol,
       "ipRoutesSummaryReceived": ipRoutesSummaryReceived,
       "ipRoutesSummaryInstalled": ipRoutesSummaryInstalled,
       "ipMfibOilMcastOilListTable": ipMfibOilMcastOilListTable,
       "ipMfibOilMcastOilListEntry": ipMfibOilMcastOilListEntry,
       "ipMfibOilMcastOilListIndex": ipMfibOilMcastOilListIndex,
       "ipMfibOilMcastOilListOilInterface": ipMfibOilMcastOilListOilInterface,
       "ipMfibOilMcastOilListOilRemoteSystem": ipMfibOilMcastOilListOilRemoteSystem,
       "vrrpTable": vrrpTable,
       "vrrpEntry": vrrpEntry,
       "vrrpVpnId": vrrpVpnId,
       "vrrpInterfacesTable": vrrpInterfacesTable,
       "vrrpInterfacesEntry": vrrpInterfacesEntry,
       "vrrpInterfacesIfName": vrrpInterfacesIfName,
       "vrrpInterfacesGroupsTable": vrrpInterfacesGroupsTable,
       "vrrpInterfacesGroupsEntry": vrrpInterfacesGroupsEntry,
       "vrrpInterfacesGroupsGroupId": vrrpInterfacesGroupsGroupId,
       "vrrpInterfacesGroupsVirtualIp": vrrpInterfacesGroupsVirtualIp,
       "vrrpInterfacesGroupsVirtualMac": vrrpInterfacesGroupsVirtualMac,
       "vrrpInterfacesGroupsPriority": vrrpInterfacesGroupsPriority,
       "vrrpInterfacesGroupsVrrpState": vrrpInterfacesGroupsVrrpState,
       "vrrpInterfacesGroupsOmpState": vrrpInterfacesGroupsOmpState,
       "vrrpInterfacesGroupsAdvertisementTimer": vrrpInterfacesGroupsAdvertisementTimer,
       "vrrpInterfacesGroupsMasterDownTimer": vrrpInterfacesGroupsMasterDownTimer,
       "vrrpInterfacesGroupsLastStateChangeTime": vrrpInterfacesGroupsLastStateChangeTime,
       "vrrpInterfacesGroupsTrackPrefixList": vrrpInterfacesGroupsTrackPrefixList,
       "vrrpInterfacesGroupsPrefixListState": vrrpInterfacesGroupsPrefixListState,
       "dhcp": dhcp,
       "dhcpInterfaceTable": dhcpInterfaceTable,
       "dhcpInterfaceEntry": dhcpInterfaceEntry,
       "dhcpInterfaceVpnId": dhcpInterfaceVpnId,
       "dhcpInterfaceIfname": dhcpInterfaceIfname,
       "dhcpInterfaceState": dhcpInterfaceState,
       "dhcpInterfaceAcquiredIp": dhcpInterfaceAcquiredIp,
       "dhcpInterfaceServer": dhcpInterfaceServer,
       "dhcpInterfaceLeaseTime": dhcpInterfaceLeaseTime,
       "dhcpInterfaceTimeRemaining": dhcpInterfaceTimeRemaining,
       "dhcpInterfaceGateway": dhcpInterfaceGateway,
       "dhcpServerTable": dhcpServerTable,
       "dhcpServerEntry": dhcpServerEntry,
       "dhcpServerVpnId": dhcpServerVpnId,
       "dhcpServerIfname": dhcpServerIfname,
       "dhcpInterfaceDnsListTable": dhcpInterfaceDnsListTable,
       "dhcpInterfaceDnsListEntry": dhcpInterfaceDnsListEntry,
       "dhcpInterfaceDnsListIndex": dhcpInterfaceDnsListIndex,
       "dhcpInterfaceDnsListDns": dhcpInterfaceDnsListDns,
       "dhcpServerBindingsTable": dhcpServerBindingsTable,
       "dhcpServerBindingsEntry": dhcpServerBindingsEntry,
       "dhcpServerBindingsClientMac": dhcpServerBindingsClientMac,
       "dhcpServerBindingsClientIp": dhcpServerBindingsClientIp,
       "dhcpServerBindingsLeaseTime": dhcpServerBindingsLeaseTime,
       "dhcpServerBindingsLeaseTimeRemaining": dhcpServerBindingsLeaseTimeRemaining,
       "dhcpServerBindingsStaticBinding": dhcpServerBindingsStaticBinding,
       "dhcpServerBindingsHostName": dhcpServerBindingsHostName,
       "pppoe": pppoe,
       "pppoeSessionTable": pppoeSessionTable,
       "pppoeSessionEntry": pppoeSessionEntry,
       "pppoeSessionVpnId": pppoeSessionVpnId,
       "pppoeSessionIfname": pppoeSessionIfname,
       "pppoeSessionSessionId": pppoeSessionSessionId,
       "pppoeSessionServerMac": pppoeSessionServerMac,
       "pppoeSessionLocalMac": pppoeSessionLocalMac,
       "pppoeSessionPppInterface": pppoeSessionPppInterface,
       "pppoeSessionAcName": pppoeSessionAcName,
       "pppoeSessionServiceName": pppoeSessionServiceName,
       "pppoeStatistics": pppoeStatistics,
       "pppoeStatisticsPppoeTxPkts": pppoeStatisticsPppoeTxPkts,
       "pppoeStatisticsPppoeRxPkts": pppoeStatisticsPppoeRxPkts,
       "pppoeStatisticsPppoeTxSessionDrops": pppoeStatisticsPppoeTxSessionDrops,
       "pppoeStatisticsPppoeRxSessionDrops": pppoeStatisticsPppoeRxSessionDrops,
       "pppoeStatisticsPppoeLcpPkts": pppoeStatisticsPppoeLcpPkts,
       "pppoeStatisticsPppoeIpcpPkts": pppoeStatisticsPppoeIpcpPkts,
       "pppoeStatisticsPppoeCcpPkts": pppoeStatisticsPppoeCcpPkts,
       "pppoeStatisticsPppoeInvDiscoveryPkts": pppoeStatisticsPppoeInvDiscoveryPkts,
       "pppoeStatisticsPppoePadiPkts": pppoeStatisticsPppoePadiPkts,
       "pppoeStatisticsPppoePadoPkts": pppoeStatisticsPppoePadoPkts,
       "pppoeStatisticsPppoePadrPkts": pppoeStatisticsPppoePadrPkts,
       "pppoeStatisticsPppoePadsPkts": pppoeStatisticsPppoePadsPkts,
       "pppoeStatisticsPppoePadtPkts": pppoeStatisticsPppoePadtPkts,
       "ppp": ppp,
       "pppInterfaceTable": pppInterfaceTable,
       "pppInterfaceEntry": pppInterfaceEntry,
       "pppInterfaceVpnId": pppInterfaceVpnId,
       "pppInterfaceIfname": pppInterfaceIfname,
       "pppInterfacePppoeInterface": pppInterfacePppoeInterface,
       "pppInterfaceInterfaceIp": pppInterfaceInterfaceIp,
       "pppInterfaceGatewayIp": pppInterfaceGatewayIp,
       "pppInterfacePrimaryDns": pppInterfacePrimaryDns,
       "pppInterfaceSecondaryDns": pppInterfaceSecondaryDns,
       "pppInterfaceMtu": pppInterfaceMtu,
       "pppInterfaceAuthType": pppInterfaceAuthType,
       "sfp": sfp,
       "sfpDetailTable": sfpDetailTable,
       "sfpDetailEntry": sfpDetailEntry,
       "sfpDetailIfname": sfpDetailIfname,
       "sfpDetailPresent": sfpDetailPresent,
       "sfpDetailPhysicalIdentifier": sfpDetailPhysicalIdentifier,
       "sfpDetailConnectorType": sfpDetailConnectorType,
       "sfpDetailTransceiverCompliancePri": sfpDetailTransceiverCompliancePri,
       "sfpDetailTransceiverComplianceSec": sfpDetailTransceiverComplianceSec,
       "sfpDetailEncoding": sfpDetailEncoding,
       "sfpDetailNominalSpeed": sfpDetailNominalSpeed,
       "sfpDetailRateSelectOptions": sfpDetailRateSelectOptions,
       "sfpDetailLengthSingleModeKm": sfpDetailLengthSingleModeKm,
       "sfpDetailLength625umOm1": sfpDetailLength625umOm1,
       "sfpDetailLength50umOm2": sfpDetailLength50umOm2,
       "sfpDetailCopperMinLength": sfpDetailCopperMinLength,
       "sfpDetailLength50umOm3": sfpDetailLength50umOm3,
       "sfpDetailLength50umOm4": sfpDetailLength50umOm4,
       "sfpDetailLaserWavelength": sfpDetailLaserWavelength,
       "sfpDetailVendorName": sfpDetailVendorName,
       "sfpDetailVendorOui": sfpDetailVendorOui,
       "sfpDetailVendorPartNumber": sfpDetailVendorPartNumber,
       "sfpDetailVendorRevision": sfpDetailVendorRevision,
       "sfpDetailVendorSerialNumber": sfpDetailVendorSerialNumber,
       "sfpDetailDateCode": sfpDetailDateCode,
       "sfpDetailFeatureOptionsLossOfSignal": sfpDetailFeatureOptionsLossOfSignal,
       "sfpDetailFeatureOptionsSignalDetect": sfpDetailFeatureOptionsSignalDetect,
       "sfpDetailFeatureOptionsTxFault": sfpDetailFeatureOptionsTxFault,
       "sfpDetailFeatureOptionsTxDisable": sfpDetailFeatureOptionsTxDisable,
       "sfpDetailFeatureOptionsRateSelect": sfpDetailFeatureOptionsRateSelect,
       "sfpDetailFeatureOptionsTuneableWavelength": sfpDetailFeatureOptionsTuneableWavelength,
       "sfpDetailFeatureOptionsRdt": sfpDetailFeatureOptionsRdt,
       "sfpDetailFeatureOptionsLro": sfpDetailFeatureOptionsLro,
       "sfpDetailFeatureOptionsPowerLevel": sfpDetailFeatureOptionsPowerLevel,
       "sfpDetailFeatureOptionsCooledLaser": sfpDetailFeatureOptionsCooledLaser,
       "sfpDetailFeatureOptionsTimingType": sfpDetailFeatureOptionsTimingType,
       "sfpDetailFeatureOptionsPagedA2": sfpDetailFeatureOptionsPagedA2,
       "sfpDetailDigitalDiagnosticsSupported": sfpDetailDigitalDiagnosticsSupported,
       "sfpDetailDigitalDiagnosticsCalibrationType": sfpDetailDigitalDiagnosticsCalibrationType,
       "sfpDetailDigitalDiagnosticsPowerType": sfpDetailDigitalDiagnosticsPowerType,
       "sfpDetailEnhancedOptionsSoftRateSelectControl": sfpDetailEnhancedOptionsSoftRateSelectControl,
       "sfpDetailEnhancedOptionsAppSelectControl": sfpDetailEnhancedOptionsAppSelectControl,
       "sfpDetailEnhancedOptionsSoftRateSelectControlMonitor": sfpDetailEnhancedOptionsSoftRateSelectControlMonitor,
       "sfpDetailEnhancedOptionsSoftRxLosMonitor": sfpDetailEnhancedOptionsSoftRxLosMonitor,
       "sfpDetailEnhancedOptionsSoftTxFaultMonitor": sfpDetailEnhancedOptionsSoftTxFaultMonitor,
       "sfpDetailEnhancedOptionsSoftTxDisableControlMonitor": sfpDetailEnhancedOptionsSoftTxDisableControlMonitor,
       "sfpDetailEnhancedOptionsAllAlarmWarningFlags": sfpDetailEnhancedOptionsAllAlarmWarningFlags,
       "sfpDiagnosticTable": sfpDiagnosticTable,
       "sfpDiagnosticEntry": sfpDiagnosticEntry,
       "sfpDiagnosticIfname": sfpDiagnosticIfname,
       "sfpDiagnosticPresent": sfpDiagnosticPresent,
       "sfpDiagnosticSupported": sfpDiagnosticSupported,
       "sfpDiagnosticControlStatusDataReadyState": sfpDiagnosticControlStatusDataReadyState,
       "sfpDiagnosticControlStatusRxLosState": sfpDiagnosticControlStatusRxLosState,
       "sfpDiagnosticControlStatusTxFaultState": sfpDiagnosticControlStatusTxFaultState,
       "sfpDiagnosticControlStatusSoftRateSelect0State": sfpDiagnosticControlStatusSoftRateSelect0State,
       "sfpDiagnosticControlStatusSoftRateSelect1State": sfpDiagnosticControlStatusSoftRateSelect1State,
       "sfpDiagnosticControlStatusRateSelect0State": sfpDiagnosticControlStatusRateSelect0State,
       "sfpDiagnosticControlStatusRateSelect1State": sfpDiagnosticControlStatusRateSelect1State,
       "sfpDiagnosticControlStatusSoftTxDisableState": sfpDiagnosticControlStatusSoftTxDisableState,
       "sfpDiagnosticControlStatusTxDisableState": sfpDiagnosticControlStatusTxDisableState,
       "sfpDiagnosticMeasurementValueTable": sfpDiagnosticMeasurementValueTable,
       "sfpDiagnosticMeasurementValueEntry": sfpDiagnosticMeasurementValueEntry,
       "sfpDiagnosticMeasurementValueMeasurement": sfpDiagnosticMeasurementValueMeasurement,
       "sfpDiagnosticMeasurementValueUnitValue": sfpDiagnosticMeasurementValueUnitValue,
       "sfpDiagnosticMeasurementValueLowAlarmValue": sfpDiagnosticMeasurementValueLowAlarmValue,
       "sfpDiagnosticMeasurementValueLowWarningValue": sfpDiagnosticMeasurementValueLowWarningValue,
       "sfpDiagnosticMeasurementValueHighWarningValue": sfpDiagnosticMeasurementValueHighWarningValue,
       "sfpDiagnosticMeasurementValueHighAlarmValue": sfpDiagnosticMeasurementValueHighAlarmValue,
       "sfpDiagnosticMeasurementValueCurrentValue": sfpDiagnosticMeasurementValueCurrentValue,
       "sfpDiagnosticMeasurementAlarmTable": sfpDiagnosticMeasurementAlarmTable,
       "sfpDiagnosticMeasurementAlarmEntry": sfpDiagnosticMeasurementAlarmEntry,
       "sfpDiagnosticMeasurementAlarmMeasurement": sfpDiagnosticMeasurementAlarmMeasurement,
       "sfpDiagnosticMeasurementAlarmLowAlarmAlarm": sfpDiagnosticMeasurementAlarmLowAlarmAlarm,
       "sfpDiagnosticMeasurementAlarmLowWarningAlarm": sfpDiagnosticMeasurementAlarmLowWarningAlarm,
       "sfpDiagnosticMeasurementAlarmHighWarningAlarm": sfpDiagnosticMeasurementAlarmHighWarningAlarm,
       "sfpDiagnosticMeasurementAlarmHighAlarmAlarm": sfpDiagnosticMeasurementAlarmHighAlarmAlarm,
       "sfpRawA0Table": sfpRawA0Table,
       "sfpRawA0Entry": sfpRawA0Entry,
       "sfpRawA0Ifname": sfpRawA0Ifname,
       "sfpRawA0Present": sfpRawA0Present,
       "sfpRawA0Row0": sfpRawA0Row0,
       "sfpRawA0Row1": sfpRawA0Row1,
       "sfpRawA0Row2": sfpRawA0Row2,
       "sfpRawA0Row3": sfpRawA0Row3,
       "sfpRawA0Row4": sfpRawA0Row4,
       "sfpRawA0Row5": sfpRawA0Row5,
       "sfpRawA0Row6": sfpRawA0Row6,
       "sfpRawA0Row7": sfpRawA0Row7,
       "sfpRawA0Row8": sfpRawA0Row8,
       "sfpRawA0Row9": sfpRawA0Row9,
       "sfpRawA0RowA": sfpRawA0RowA,
       "sfpRawA0RowB": sfpRawA0RowB,
       "sfpRawA0RowC": sfpRawA0RowC,
       "sfpRawA0RowD": sfpRawA0RowD,
       "sfpRawA0RowE": sfpRawA0RowE,
       "sfpRawA0RowF": sfpRawA0RowF,
       "sfpRawA2Table": sfpRawA2Table,
       "sfpRawA2Entry": sfpRawA2Entry,
       "sfpRawA2Ifname": sfpRawA2Ifname,
       "sfpRawA2Present": sfpRawA2Present,
       "sfpRawA2Supported": sfpRawA2Supported,
       "sfpRawA2Row0": sfpRawA2Row0,
       "sfpRawA2Row1": sfpRawA2Row1,
       "sfpRawA2Row2": sfpRawA2Row2,
       "sfpRawA2Row3": sfpRawA2Row3,
       "sfpRawA2Row4": sfpRawA2Row4,
       "sfpRawA2Row5": sfpRawA2Row5,
       "sfpRawA2Row6": sfpRawA2Row6,
       "sfpRawA2Row7": sfpRawA2Row7,
       "sfpRawA2Row8": sfpRawA2Row8,
       "sfpRawA2Row9": sfpRawA2Row9,
       "sfpRawA2RowA": sfpRawA2RowA,
       "sfpRawA2RowB": sfpRawA2RowB,
       "sfpRawA2RowC": sfpRawA2RowC,
       "sfpRawA2RowD": sfpRawA2RowD,
       "sfpRawA2RowE": sfpRawA2RowE,
       "sfpRawA2RowF": sfpRawA2RowF,
       "dhcpv6": dhcpv6,
       "dhcpv6InterfaceTable": dhcpv6InterfaceTable,
       "dhcpv6InterfaceEntry": dhcpv6InterfaceEntry,
       "dhcpv6InterfaceVpnId": dhcpv6InterfaceVpnId,
       "dhcpv6InterfaceIfname": dhcpv6InterfaceIfname,
       "dhcpv6InterfaceState": dhcpv6InterfaceState,
       "dhcpv6InterfaceAcquiredIp": dhcpv6InterfaceAcquiredIp,
       "dhcpv6InterfaceServer": dhcpv6InterfaceServer,
       "dhcpv6InterfaceLeaseTime": dhcpv6InterfaceLeaseTime,
       "dhcpv6InterfaceTimeRemaining": dhcpv6InterfaceTimeRemaining,
       "dhcpv6InterfaceGateway": dhcpv6InterfaceGateway,
       "dhcpv6InterfaceDnsListTable": dhcpv6InterfaceDnsListTable,
       "dhcpv6InterfaceDnsListEntry": dhcpv6InterfaceDnsListEntry,
       "dhcpv6InterfaceDnsListIndex": dhcpv6InterfaceDnsListIndex,
       "dhcpv6InterfaceDnsListDns": dhcpv6InterfaceDnsListDns,
       "cloudexpress": cloudexpress,
       "cloudAppTable": cloudAppTable,
       "cloudAppEntry": cloudAppEntry,
       "cloudAppVpnId": cloudAppVpnId,
       "cloudAppName": cloudAppName,
       "cloudAppExitType": cloudAppExitType,
       "cloudAppGatewayIp": cloudAppGatewayIp,
       "cloudAppIfName": cloudAppIfName,
       "cloudAppLatency": cloudAppLatency,
       "cloudAppLoss": cloudAppLoss,
       "cloudAppLocalColor": cloudAppLocalColor,
       "cloudAppRemoteColor": cloudAppRemoteColor,
       "cloudLocalExitTable": cloudLocalExitTable,
       "cloudLocalExitEntry": cloudLocalExitEntry,
       "cloudLocalExitVpnId": cloudLocalExitVpnId,
       "cloudLocalExitAppName": cloudLocalExitAppName,
       "cloudLocalExitIfName": cloudLocalExitIfName,
       "cloudLocalExitLatency": cloudLocalExitLatency,
       "cloudLocalExitLoss": cloudLocalExitLoss,
       "cloudGatewayExitTable": cloudGatewayExitTable,
       "cloudGatewayExitEntry": cloudGatewayExitEntry,
       "cloudGatewayExitVpnId": cloudGatewayExitVpnId,
       "cloudGatewayExitAppName": cloudGatewayExitAppName,
       "cloudGatewayExitIP": cloudGatewayExitIP,
       "cloudGatewayExitLatency": cloudGatewayExitLatency,
       "cloudGatewayExitLoss": cloudGatewayExitLoss,
       "cloudGatewayExitLocalColor": cloudGatewayExitLocalColor,
       "cloudGatewayExitRemoteColor": cloudGatewayExitRemoteColor}
)
