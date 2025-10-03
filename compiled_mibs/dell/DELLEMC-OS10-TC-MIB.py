# SNMP MIB module (DELLEMC-OS10-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\DELLEMC-OS10-TC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:58 2025
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

(os10,) = mibBuilder.importSymbols(
    "DELLEMC-OS10-SMI-MIB",
    "os10")

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

os10TextualConventionsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 1)
)
if mibBuilder.loadTexts:
    os10TextualConventionsMib.setRevisions(
        ("2019-07-03 12:00",
         "2019-03-07 12:00",
         "2018-05-15 12:00",
         "2018-01-26 12:00",
         "2017-10-27 12:00",
         "2017-10-11 12:00",
         "2017-09-06 12:00",
         "2017-06-21 12:00",
         "2017-01-25 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Os10ChassisDefType(TextualConvention, Integer32):
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
              9999)
        )
    )
    namedValues = NamedValues(
        *(("s6000on", 1),
          ("s4048on", 2),
          ("s4048Ton", 3),
          ("s3048on", 4),
          ("s6010on", 5),
          ("s4148Fon", 6),
          ("s4128Fon", 7),
          ("s4148Ton", 8),
          ("s4128Ton", 9),
          ("s4148FEon", 10),
          ("s4148Uon", 11),
          ("s4200on", 12),
          ("mx5108Non", 13),
          ("mx9116Non", 14),
          ("s5148Fon", 15),
          ("z9100on", 16),
          ("s4248FBon", 17),
          ("s4248FBLon", 18),
          ("s4112Fon", 19),
          ("s4112Ton", 20),
          ("z9264Fon", 21),
          ("z9224Fon", 22),
          ("s5212Fon", 23),
          ("s5224Fon", 24),
          ("s5232Fon", 25),
          ("s5248Fon", 26),
          ("s5296Fon", 27),
          ("z9332Fon", 28),
          ("n3248TEon", 29),
          ("unknown", 9999))
    )



class Os10InterfaceType(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("ethernetManagement", 1),
          ("ethernet100M", 2),
          ("ethernet1GB", 3),
          ("ethernet1GBCopper", 4),
          ("ethernet10GB", 5),
          ("ethernet10GBCopper", 6),
          ("ethernet25GB", 7),
          ("ethernet50GB", 8),
          ("ethernet40GB", 9),
          ("ethernet100GB", 10),
          ("fc", 11))
    )



class Os10SystemCardType(TextualConvention, Integer32):
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
              24,
              25,
              26,
              27,
              28,
              29,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("s6000on", 1),
          ("s4048on", 2),
          ("s4048Ton", 3),
          ("s3048on", 4),
          ("s6010on", 5),
          ("s4148Fon", 6),
          ("s4128Fon", 7),
          ("s4148Ton", 8),
          ("s4128Ton", 9),
          ("s4148FEon", 10),
          ("s4148Uon", 11),
          ("s4200on", 12),
          ("mx5108Non", 13),
          ("mx9116Non", 14),
          ("s5148Fon", 15),
          ("z9100on", 16),
          ("s4248FBon", 17),
          ("s4248FBLon", 18),
          ("s4112Fon", 19),
          ("s4112Ton", 20),
          ("z9264Fon", 21),
          ("z9232Fon", 22),
          ("s5212Fon", 23),
          ("s5224Fon", 24),
          ("s5232Fon", 25),
          ("s5248Fon", 26),
          ("s5296Fon", 27),
          ("z9332Fon", 28),
          ("n3248TEon", 29),
          ("unknown", 9999))
    )



class Os10CardOperStatus(TextualConvention, Integer32):
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
        *(("ready", 1),
          ("cardMisMatch", 2),
          ("cardProblem", 3),
          ("diagMode", 4),
          ("cardAbsent", 5),
          ("offline", 6))
    )



class Os10DeviceType(TextualConvention, Integer32):
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
        *(("chassis", 1),
          ("stack", 2),
          ("rpm", 3),
          ("supervisor", 4),
          ("linecard", 5))
    )



class Os10CmnOperStatus(TextualConvention, Integer32):
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7),
          ("failed", 8))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELLEMC-OS10-TC-MIB",
    **{"Os10ChassisDefType": Os10ChassisDefType,
       "Os10InterfaceType": Os10InterfaceType,
       "Os10SystemCardType": Os10SystemCardType,
       "Os10CardOperStatus": Os10CardOperStatus,
       "Os10DeviceType": Os10DeviceType,
       "Os10CmnOperStatus": Os10CmnOperStatus,
       "os10TextualConventionsMib": os10TextualConventionsMib}
)
