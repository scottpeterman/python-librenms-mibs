# SNMP MIB module (UBIQUOSS-EPON-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBIQUOSS-EPON-TC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:00 2025
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



class PortList(TextualConvention, Integer32):
    status = "current"


class OnuType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              30,
              31,
              41,
              42,
              61,
              62,
              63,
              64,
              113,
              116,
              117,
              118,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
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
              170,
              171,
              250,
              251)
        )
    )
    namedValues = NamedValues(
        *(("og1100", 1),
          ("u9024a", 2),
          ("hybridOnu", 19),
          ("hybridOnu2", 20),
          ("hybridOnu2b", 21),
          ("hybridOnu2e", 22),
          ("hybridOnuSfp", 23),
          ("hybridPmc", 24),
          ("hybridPmc2b", 25),
          ("hybrid10gOnu", 30),
          ("hybrid10gOnub", 31),
          ("ctc-tk", 41),
          ("ctc-tk4", 42),
          ("c1004", 61),
          ("c1001a", 62),
          ("c1010at", 63),
          ("c1010ax", 64),
          ("og3410ab", 113),
          ("og3500ab", 116),
          ("og3400aa", 117),
          ("og3500db", 118),
          ("og3500ec", 121),
          ("og3500jc", 122),
          ("og3500kc", 123),
          ("cc3802tg", 124),
          ("corecess3801t", 125),
          ("corecess3804tn", 126),
          ("corecess3801tn", 127),
          ("dongwon204d", 128),
          ("dongwon201d", 129),
          ("c501m", 131),
          ("c501a", 132),
          ("c501b", 133),
          ("c501g", 134),
          ("c501l", 135),
          ("c502j", 136),
          ("c504a", 137),
          ("c504b", 138),
          ("c501n", 139),
          ("c504n", 140),
          ("c504k", 141),
          ("c504j", 142),
          ("dongwon301d", 143),
          ("dongwon304d", 144),
          ("IOP_TK", 145),
          ("IOP_TK4", 146),
          ("IOP_PMC", 148),
          ("IOP_CTN", 149),
          ("IOP_CTN4", 150),
          ("c504e", 151),
          ("c501f", 152),
          ("c504g", 153),
          ("c504w", 154),
          ("c504l", 155),
          ("IOP_TK4N", 156),
          ("IOP_CTN4N", 157),
          ("c502ep", 158),
          ("c501v", 159),
          ("c504gr", 160),
          ("c502p", 161),
          ("c502d", 162),
          ("c524a", 170),
          ("c514k", 171),
          ("filter", 250),
          ("Unknown", 251))
    )



class PonFilterRuleField(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              10,
              11,
              16)
        )
    )
    namedValues = NamedValues(
        *(("layer2DstAddr", 0),
          ("layer2SrcAddr", 1),
          ("logicalLinkId", 2),
          ("etherType", 3),
          ("vlanId", 4),
          ("ipV4Protocol", 6),
          ("dscp", 10),
          ("cos", 11),
          ("noExist", 16))
    )



class PonFilterRuleOperator(TextualConvention, Integer32):
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
        *(("neverMatch", 0),
          ("equalTo", 1),
          ("notEqualTo", 2),
          ("lessThanOrEqualTo", 3),
          ("greaterThanOrEqualTo", 4),
          ("matchWhenFieldExists", 5),
          ("matchWhenFieldNotExists", 6),
          ("alwaysMatch", 7),
          ("noExist", 8),
          ("mask", 9))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBIQUOSS-EPON-TC-MIB",
    **{"PortList": PortList,
       "OnuType": OnuType,
       "PonFilterRuleField": PonFilterRuleField,
       "PonFilterRuleOperator": PonFilterRuleOperator}
)
