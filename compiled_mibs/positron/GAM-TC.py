# SNMP MIB module (GAM-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\positron\GAM-TC
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:52 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class GAMInteger8(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )



class GAMInteger16(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )



class GAMInteger64(TextualConvention, OctetString):
    status = "current"
    displayHint = "8x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class GAMUnsigned8(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class GAMUnsigned16(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class GAMUnsigned64(TextualConvention, OctetString):
    status = "current"
    displayHint = "8x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class GAMInteger32e_9(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class GAMTimeStamp(TextualConvention, OctetString):
    status = "current"
    displayHint = "8x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class GAMEtherType(TextualConvention, Gauge32):
    status = "current"
    displayHint = "2x"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class GAMPsecUserBitmaskType(TextualConvention, Gauge32):
    status = "current"
    displayHint = "2x"


class GAMInterfaceIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class GAMRowEditorState(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"


class GAMPercent(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class GAMPortList(TextualConvention, OctetString):
    status = "current"
    displayHint = "128x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class GAMVlan(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )



class GAMVlanOrZero(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class GAMVlanListQuarter(TextualConvention, OctetString):
    status = "current"
    displayHint = "128x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128



class GAMDisplayString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class GAMMacStringList(TextualConvention, OctetString):
    status = "current"
    displayHint = "4095a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4095),
    )



class GAMInetAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )



class GAMIpAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 46),
    )



class GAMVclProtoEncap(TextualConvention, OctetString):
    status = "current"
    displayHint = "6x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 6),
    )



class GAMBitType(TextualConvention, Integer32):
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
        *(("any", 0),
          ("zero", 1),
          ("one", 2))
    )



class GAMDestMacType(TextualConvention, Integer32):
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
        *(("any", 0),
          ("unicast", 1),
          ("multicast", 2),
          ("broadcast", 3))
    )



class GAMVcapKeyType(TextualConvention, Integer32):
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
          ("doubleTag", 1),
          ("ipAddr", 2),
          ("macIpAddr", 3))
    )



class GAMVlanTagPriority(TextualConvention, Integer32):
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
        *(("any", 0),
          ("value0", 1),
          ("value1", 2),
          ("value2", 3),
          ("value3", 4),
          ("value4", 5),
          ("value5", 6),
          ("value6", 7),
          ("value7", 8),
          ("range0to1", 9),
          ("range2to3", 10),
          ("range4to5", 11),
          ("range6to7", 12),
          ("range0to3", 13),
          ("range4to7", 14))
    )



class GAMVlanTagType(TextualConvention, Integer32):
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
        *(("any", 0),
          ("untagged", 1),
          ("tagged", 2),
          ("cTagged", 3),
          ("sTagged", 4))
    )



class GAMASRType(TextualConvention, Integer32):
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
        *(("any", 0),
          ("specific", 1),
          ("range", 2))
    )



class GAMAdvDestMacType(TextualConvention, Integer32):
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
        *(("any", 0),
          ("unicast", 1),
          ("multicast", 2),
          ("broadcast", 3),
          ("specific", 4))
    )



class GAMASType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("specific", 1))
    )



class GAMSfpTransceiver(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
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
          ("notSupported", 1),
          ("sfp100FX", 2),
          ("sfp1000BaseT", 7),
          ("sfp1000BaseCx", 8),
          ("sfp1000BaseSx", 9),
          ("sfp1000BaseLx", 10),
          ("sfp1000BaseX", 11),
          ("sfp2G5", 12),
          ("sfp5G", 13),
          ("sfp10G", 14))
    )



class GAMMepDmTimeUnit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("microSeconds", 0),
          ("nanoSeconds", 1))
    )



class GAMMepInstanceDirection(TextualConvention, Integer32):
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



class GAMMepTxRate(TextualConvention, Integer32):
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
          ("frames300PerSecond", 1),
          ("frames100PerSecond", 2),
          ("frames10PerSecond", 3),
          ("frames1PerSecond", 4),
          ("frames6PerMinute", 5),
          ("frames1PerMinute", 6),
          ("frames6PerHour", 7))
    )



class GAMPortStatusSpeed(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("speed10M", 1),
          ("speed100M", 2),
          ("speed1G", 3),
          ("speed2G5", 4),
          ("speed5G", 5),
          ("speed10G", 6),
          ("speed12G", 7))
    )



class GAMQosShaperRateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("line", 0),
          ("data", 1))
    )



class GAMRfc5517Mode(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("isolated", 1),
          ("community", 2),
          ("uplink", 3),
          ("stacking", 4),
          ("stacking-isolated", 5))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GAM-TC",
    **{"GAMInteger8": GAMInteger8,
       "GAMInteger16": GAMInteger16,
       "GAMInteger64": GAMInteger64,
       "GAMUnsigned8": GAMUnsigned8,
       "GAMUnsigned16": GAMUnsigned16,
       "GAMUnsigned64": GAMUnsigned64,
       "GAMInteger32e-9": GAMInteger32e_9,
       "GAMTimeStamp": GAMTimeStamp,
       "GAMEtherType": GAMEtherType,
       "GAMPsecUserBitmaskType": GAMPsecUserBitmaskType,
       "GAMInterfaceIndex": GAMInterfaceIndex,
       "GAMRowEditorState": GAMRowEditorState,
       "GAMPercent": GAMPercent,
       "GAMPortList": GAMPortList,
       "GAMVlan": GAMVlan,
       "GAMVlanOrZero": GAMVlanOrZero,
       "GAMVlanListQuarter": GAMVlanListQuarter,
       "GAMDisplayString": GAMDisplayString,
       "GAMMacStringList": GAMMacStringList,
       "GAMInetAddress": GAMInetAddress,
       "GAMIpAddress": GAMIpAddress,
       "GAMVclProtoEncap": GAMVclProtoEncap,
       "GAMBitType": GAMBitType,
       "GAMDestMacType": GAMDestMacType,
       "GAMVcapKeyType": GAMVcapKeyType,
       "GAMVlanTagPriority": GAMVlanTagPriority,
       "GAMVlanTagType": GAMVlanTagType,
       "GAMASRType": GAMASRType,
       "GAMAdvDestMacType": GAMAdvDestMacType,
       "GAMASType": GAMASType,
       "GAMSfpTransceiver": GAMSfpTransceiver,
       "GAMMepDmTimeUnit": GAMMepDmTimeUnit,
       "GAMMepInstanceDirection": GAMMepInstanceDirection,
       "GAMMepTxRate": GAMMepTxRate,
       "GAMPortStatusSpeed": GAMPortStatusSpeed,
       "GAMQosShaperRateType": GAMQosShaperRateType,
       "GAMRfc5517Mode": GAMRfc5517Mode}
)
