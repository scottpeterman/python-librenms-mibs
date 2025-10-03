# SNMP MIB module (CIENA-WS-TYPEDEFS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-TYPEDEFS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:02 2025
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

(cienaWsConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsConfig")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaWsTypedefsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 13)
)
if mibBuilder.loadTexts:
    cienaWsTypedefsMIB.setRevisions(
        ("2017-06-14 00:00",
         "2017-02-28 00:00",
         "2016-12-12 00:00",
         "2016-03-03 00:00",
         "2015-02-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ChannelsNumber(TextualConvention, Unsigned32):
    status = "current"


class ConnectorTypeDescEnum(TextualConvention, Integer32):
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
              36)
        )
    )
    namedValues = NamedValues(
        *(("unknownorunspecified", 0),
          ("sc", 1),
          ("fibrechannelstyle1copperconnector", 2),
          ("fibrechannelstyle2copperconnector", 3),
          ("bnc", 4),
          ("fibrechannelcoaxheaders", 5),
          ("fiberjack", 6),
          ("lc", 7),
          ("mtrj", 8),
          ("mu", 9),
          ("sg", 10),
          ("opticalpigtail", 11),
          ("mpo1x12", 12),
          ("mpo2x16", 13),
          ("hssdcii", 32),
          ("copperpigtail", 33),
          ("rj45", 34),
          ("noseparableconnector", 35),
          ("mxc2x16", 36))
    )



class Decimal1Dig(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483640, 2147483640),
    )



class Decimal2Dig(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483600, 2147483600),
    )



class Decimal2DigSmall(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3000000, 3000000),
    )



class Decimal3Dig(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483000, 2147483000),
    )



class DescriptionString(TextualConvention, OctetString):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class EnabledDisabledEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class EnabledDisabledNaEnum(TextualConvention, Integer32):
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
        *(("disabled", 0),
          ("enabled", 1),
          ("na", 2))
    )



class EnhancedOptsEnum(TextualConvention, Integer32):
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
        *(("na", 0),
          ("yes", 1),
          ("no", 2))
    )



class LicenseStatusEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notcompliant", 0),
          ("compliant", 1))
    )



class LineModuleTypeBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("wl3eline", 0)
    )


class LineSysEnum(TextualConvention, Integer32):
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
        *(("coloured", 0),
          ("colourless", 1),
          ("contentionless", 2),
          ("cscolored", 3),
          ("cscolorless", 4))
    )



class MacString(TextualConvention, OctetString):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



class ModemChannel(TextualConvention, Integer32):
    status = "current"


class ModemFrequency(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483640, 2147483640),
    )



class ModuleTypeBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("integrated", 0),
          ("fieldreplaceable", 1))
    )


class ModuleTypeEnum(TextualConvention, Integer32):
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
          ("integrated", 1),
          ("fieldreplaceable", 2))
    )



class NameString(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class OnOffEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )



class PortId(TextualConvention, Unsigned32):
    status = "current"


class PortName(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class PtpId(TextualConvention, Unsigned32):
    status = "current"


class RecoverLinkDispersionType(TextualConvention, Integer32):
    status = "current"


class ServiceDomainIdx(TextualConvention, Unsigned32):
    status = "current"


class ServiceIdx(TextualConvention, Unsigned32):
    status = "current"


class StringMaxl128(TextualConvention, OctetString):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class StringMaxl15(TextualConvention, OctetString):
    status = "current"
    displayHint = "15a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )



class StringMaxl16(TextualConvention, OctetString):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class StringMaxl254(TextualConvention, OctetString):
    status = "current"
    displayHint = "254a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )



class StringMaxl256(TextualConvention, OctetString):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class StringMaxl32(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class StringMaxl44(TextualConvention, OctetString):
    status = "current"
    displayHint = "44a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )



class StringMaxl50(TextualConvention, OctetString):
    status = "current"
    displayHint = "50a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )



class StringMaxl64(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class StringSci(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TraceMismatchFailMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarmoff", 0),
          ("alarmon", 1))
    )



class TraceMismatchMode(TextualConvention, Integer32):
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
        *(("operatoronly", 1),
          ("sapi", 2),
          ("dapi", 3),
          ("sapianddapi", 4))
    )



class TraceTxOperMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("manual", 0),
          ("auto", 1))
    )



class TxPowerLvl(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483640, 2147483640),
    )



class UpDownEnum(TextualConvention, Integer32):
    status = "current"
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



class VendorDateString(TextualConvention, OctetString):
    status = "current"
    displayHint = "9a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )



class VendorRvString(TextualConvention, OctetString):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class WlSpacing(TextualConvention, Integer32):
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
        *(("fixed50ghz", 0),
          ("fixed100ghz", 1),
          ("fixed200ghz", 2),
          ("flexgrid", 3))
    )



class XcvrId(TextualConvention, Unsigned32):
    status = "current"


class XcvrMode(TextualConvention, Integer32):
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
        *(("blank", 0),
          ("mode10gig", 1),
          ("mode40gig", 2),
          ("mode100gig", 3),
          ("mode16qam", 4),
          ("modeqpsk", 5),
          ("mode8qam", 6))
    )



class XcvrProfileId(TextualConvention, Unsigned32):
    status = "current"


class XcvrSerdesRxAmplitude(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ampUnspecified", -1),
          ("amp0", 0),
          ("amp1", 1),
          ("amp2", 2),
          ("amp3", 3))
    )



class XcvrSerdesRxEmphasis(TextualConvention, Integer32):
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
        *(("empUnspecified", -1),
          ("emp0", 0),
          ("emp1", 1),
          ("emp2", 2),
          ("emp3", 3),
          ("emp4", 4),
          ("emp5", 5),
          ("emp6", 6),
          ("emp7", 7))
    )



class XcvrSerdesTxEq(TextualConvention, Integer32):
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("eqUnspecified", -1),
          ("eq0", 0),
          ("eq1", 1),
          ("eq2", 2),
          ("eq3", 3),
          ("eq4", 4),
          ("eq5", 5),
          ("eq6", 6),
          ("eq7", 7),
          ("eq8", 8),
          ("eq9", 9),
          ("eq10", 10))
    )



class XcvrType(TextualConvention, Integer32):
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
        *(("notavailable", 0),
          ("unsupported", 1),
          ("qsfpplus", 2),
          ("qsfp28", 3),
          ("wavelogic3extreme", 4))
    )



class YesNoEnum(TextualConvention, Integer32):
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



class YesNoNaEnum(TextualConvention, Integer32):
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
        *(("no", 0),
          ("yes", 1),
          ("na", 2))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    **{"ChannelsNumber": ChannelsNumber,
       "ConnectorTypeDescEnum": ConnectorTypeDescEnum,
       "Decimal1Dig": Decimal1Dig,
       "Decimal2Dig": Decimal2Dig,
       "Decimal2DigSmall": Decimal2DigSmall,
       "Decimal3Dig": Decimal3Dig,
       "DescriptionString": DescriptionString,
       "EnabledDisabledEnum": EnabledDisabledEnum,
       "EnabledDisabledNaEnum": EnabledDisabledNaEnum,
       "EnhancedOptsEnum": EnhancedOptsEnum,
       "LicenseStatusEnum": LicenseStatusEnum,
       "LineModuleTypeBits": LineModuleTypeBits,
       "LineSysEnum": LineSysEnum,
       "MacString": MacString,
       "ModemChannel": ModemChannel,
       "ModemFrequency": ModemFrequency,
       "ModuleTypeBits": ModuleTypeBits,
       "ModuleTypeEnum": ModuleTypeEnum,
       "NameString": NameString,
       "OnOffEnum": OnOffEnum,
       "PortId": PortId,
       "PortName": PortName,
       "PtpId": PtpId,
       "RecoverLinkDispersionType": RecoverLinkDispersionType,
       "ServiceDomainIdx": ServiceDomainIdx,
       "ServiceIdx": ServiceIdx,
       "StringMaxl128": StringMaxl128,
       "StringMaxl15": StringMaxl15,
       "StringMaxl16": StringMaxl16,
       "StringMaxl254": StringMaxl254,
       "StringMaxl256": StringMaxl256,
       "StringMaxl32": StringMaxl32,
       "StringMaxl44": StringMaxl44,
       "StringMaxl50": StringMaxl50,
       "StringMaxl64": StringMaxl64,
       "StringSci": StringSci,
       "TraceMismatchFailMode": TraceMismatchFailMode,
       "TraceMismatchMode": TraceMismatchMode,
       "TraceTxOperMode": TraceTxOperMode,
       "TxPowerLvl": TxPowerLvl,
       "UpDownEnum": UpDownEnum,
       "VendorDateString": VendorDateString,
       "VendorRvString": VendorRvString,
       "WlSpacing": WlSpacing,
       "XcvrId": XcvrId,
       "XcvrMode": XcvrMode,
       "XcvrProfileId": XcvrProfileId,
       "XcvrSerdesRxAmplitude": XcvrSerdesRxAmplitude,
       "XcvrSerdesRxEmphasis": XcvrSerdesRxEmphasis,
       "XcvrSerdesTxEq": XcvrSerdesTxEq,
       "XcvrType": XcvrType,
       "YesNoEnum": YesNoEnum,
       "YesNoNaEnum": YesNoNaEnum,
       "cienaWsTypedefsMIB": cienaWsTypedefsMIB}
)
