# SNMP MIB module (FORCE10-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\FORCE10-TC
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:02 2025
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

(f10Modules,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Modules")

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

f10TextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 4, 2)
)
if mibBuilder.loadTexts:
    f10TextualConventions.setRevisions(
        ("2009-04-07 12:00",
         "2008-09-16 12:00",
         "2008-09-02 12:00",
         "2007-06-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class F10ChassisType(TextualConvention, Integer32):
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
              39)
        )
    )
    namedValues = NamedValues(
        *(("e1200", 1),
          ("e600", 2),
          ("e300", 3),
          ("e150", 4),
          ("e610", 5),
          ("c150", 6),
          ("c300", 7),
          ("e1200i", 8),
          ("s2410cp", 9),
          ("s2410p", 10),
          ("s50", 11),
          ("s50e", 12),
          ("s50v", 13),
          ("s50nac", 14),
          ("s50ndc", 15),
          ("s25pdc", 16),
          ("s25pac", 17),
          ("s25v", 18),
          ("s25n", 19),
          ("s60", 20),
          ("s55", 21),
          ("s4810", 22),
          ("s6410", 23),
          ("z9000", 24),
          ("m-MXL", 25),
          ("m-IOA", 26),
          ("s4820", 27),
          ("s6000", 28),
          ("s5000", 29),
          ("s-FN410S-IOA", 30),
          ("s-FN410T-IOA", 31),
          ("s-FN2210S-IOA", 32),
          ("z9500", 33),
          ("s4810on", 34),
          ("s6000on", 35),
          ("s4000", 36),
          ("c9000", 37),
          ("c1048p", 38),
          ("s3000", 39))
    )



class F10InterfaceType(TextualConvention, Integer32):
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
        *(("ethernetManagement", 1),
          ("ethernet100M", 2),
          ("ethernet1GB", 3),
          ("ethernet1GBCopper", 4),
          ("ethernet10GB", 5),
          ("ethernet10GBCopper", 6),
          ("sonetOC3OC12", 7),
          ("sonetOC48OC96", 8),
          ("sonetOC192", 9),
          ("ethernet40GB", 10))
    )



class F10SystemPortType(TextualConvention, Integer32):
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("portSerial", 1),
          ("portAux", 2),
          ("portFastEther", 3),
          ("port0210E2TV", 4),
          ("port0210E2TE", 5),
          ("port2401E24S", 6),
          ("port2401E24L", 7),
          ("port12OC12OC3", 8),
          ("port01OC192", 9),
          ("port2401E24SEC", 10),
          ("port2401E24LEC", 11),
          ("port0210E2TY", 12),
          ("port0210E2TU", 13),
          ("port0110EW1YB", 14),
          ("port0110EW1YC", 15),
          ("port02S48YC2", 16),
          ("port0110EX1YB", 17),
          ("port0110EX1YC", 18),
          ("port1201F12PB", 19),
          ("port1201F12PC", 20),
          ("port0110EX1EB", 21),
          ("port0110EX1EC", 22),
          ("port0110EX1YBL", 23),
          ("port0210EX2YD", 24),
          ("port0210EX2ED", 25),
          ("port0210EX2ZD-DEP", 26),
          ("port0210EW2YD", 27),
          ("port0110EX1YD", 28),
          ("port0110EX1ED", 29),
          ("port0110EX1ZD", 30),
          ("port0110EW1YD", 31),
          ("port2401E24PD", 32),
          ("port0210EX2YD2", 33),
          ("port0210EX2YE", 34),
          ("port0110EX1YD2", 35),
          ("port0110EX1YE", 36),
          ("port0210EW2YD2", 37),
          ("port0210EW2YE", 38),
          ("port0110EW1YE", 39),
          ("port01OC192SE", 40),
          ("port2401E24TD", 41),
          ("port2401E24PE", 42),
          ("port1201F12PC2", 43),
          ("port0210EX2ZD", 44),
          ("port0210EW2YD3", 45),
          ("port0210EX2ZE", 46),
          ("port1201F12PE", 47),
          ("port2401E24PD2", 48),
          ("port1201E12TD3", 49),
          ("port0210EX2YD3", 50),
          ("port0110EX1YD3", 51),
          ("port1201E12PD3", 52),
          ("port02S48YE2", 53),
          ("port0110EX1YE3", 54),
          ("port1201E12PE3", 55),
          ("port4801E48PF", 56),
          ("port2401E24PF3", 57),
          ("port4801E48TF3", 58),
          ("port4801E48TF", 59),
          ("port0410EXW4PF", 60),
          ("port0210EXW2PF3", 61),
          ("port9001E90MF", 62),
          ("port4801E48T1F", 63),
          ("port1610EXW16PF", 64),
          ("port0810EXW8PF", 65),
          ("port0410EXW4PG", 66),
          ("port4801E48PG", 67),
          ("port4801E48TG", 68),
          ("port0210EXW2PG3", 69),
          ("port2401E24PG3", 70),
          ("port2401E24TG3", 71),
          ("port04S48P4G", 72),
          ("port04S48P4G3", 73),
          ("port1610EXW16PG", 74),
          ("port0810EXW8PG3", 75),
          ("port9001E90MH", 76),
          ("port1010EXW10SH", 77),
          ("port1010EXW10SJ", 78),
          ("port9001E90MJ", 79),
          ("port5001E50PH", 80),
          ("port5001E50PJ", 81),
          ("port1010EXW10PH", 82),
          ("port1010EXW10PJ", 83),
          ("port4010EXW40SH", 84),
          ("port4010EXW40SJ", 85),
          ("portUnknown", 99))
    )



class F10SystemCardType(TextualConvention, Integer32):
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
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              250,
              259)
        )
    )
    namedValues = NamedValues(
        *(("notPresented", 0),
          ("lc0210E2TV", 1),
          ("lc0210E2TE", 2),
          ("lc2401E24S", 3),
          ("lc2401E24L", 4),
          ("lc12OC12OC3", 5),
          ("lc01OC192", 6),
          ("lcReserve", 7),
          ("lc2401E24SEC", 8),
          ("lc2401E24lEc", 9),
          ("lc0210E2TY", 10),
          ("lc0210E2TU", 11),
          ("lc0110EW1YB", 12),
          ("lc0110EW1YC", 13),
          ("lc02S48YC2", 14),
          ("lc0110EX1YB", 15),
          ("lc0110EX1YC", 16),
          ("lc1201F12PB", 17),
          ("lc1201F12PC", 18),
          ("lc0110EX1EB", 19),
          ("lc0110EX1EC", 20),
          ("lc0110EX1YBL", 21),
          ("lc0210EX2YD", 22),
          ("lc0210EX2ED", 23),
          ("lc0210EX2ZDdep", 24),
          ("lc0210EW2YD", 25),
          ("lc0110EX1YD", 26),
          ("lc0110EX1ED", 27),
          ("lc0110EX1ZD", 28),
          ("lc0110EW1YD", 29),
          ("lc2401E24PD", 30),
          ("lc0210EX2YD2", 31),
          ("lc0210EX2YE", 32),
          ("lc0110EX1YD2", 33),
          ("lc0110EX1YE", 34),
          ("lc0210EW2YD2", 35),
          ("lc0210EW2YE", 36),
          ("lc0110EW1YE", 37),
          ("lc01OC192SE", 38),
          ("lc2401E24TD", 39),
          ("lc2401E24PE", 40),
          ("lc1201F12PC2", 41),
          ("lc0210EX2ZD", 42),
          ("lc0210EW2YD3", 43),
          ("lc0210EX2ZE", 44),
          ("lc1201F12PE", 45),
          ("lc2401E24PD2", 46),
          ("lc0210EX2ZD2", 47),
          ("lc1201E12TD3", 48),
          ("lc0210EX2YD3", 49),
          ("lc0110EX1YD3", 50),
          ("lc1201E12PD3", 51),
          ("lc02S48YE2", 52),
          ("lc0110EX1YE3", 53),
          ("lc1201E12PE3", 54),
          ("lc4801E48PF", 55),
          ("lc2401E24PF3", 56),
          ("lc4801E48TF3", 57),
          ("lc4801E48TF", 58),
          ("lc0410EXW4PF", 59),
          ("lc0210EXW2PF3", 60),
          ("lc9001E90MF", 61),
          ("lc4801E48T1F", 62),
          ("lc1610EXW16PF", 63),
          ("lc0810EXW8PF", 64),
          ("lc0410EXW4PG", 65),
          ("lc4801E48PG", 66),
          ("lc4801E48TG", 67),
          ("lc0210EXW2PG3", 68),
          ("lc2401E24PG3", 69),
          ("lc2401E24TG3", 70),
          ("lc04S48P4G", 71),
          ("lc04S48P4G3", 72),
          ("lc1610EXW16PG", 73),
          ("lc0810EXW8PG3", 74),
          ("lc9001E90MH", 75),
          ("lc1010EXW10SH", 76),
          ("lc1010EXW10SJ", 77),
          ("lc9001E90MJ", 78),
          ("lc5001E50PH", 79),
          ("lc5001E50PJ", 80),
          ("lc1010EXW10PH", 81),
          ("lc1010EXW10PJ", 82),
          ("lc4010EXW40SH", 83),
          ("lc4010EXW40SJ", 84),
          ("z9500LC12", 85),
          ("z9500LC36", 86),
          ("z9500LC48", 87),
          ("c9000LC24X10GCu", 88),
          ("c9000LC24X10GOptics", 89),
          ("c9000LC6X40G", 90),
          ("rpmCard", 200),
          ("rpmCardEB", 201),
          ("rpmCardED", 202),
          ("rpmCardEE", 203),
          ("rpmCardEE3", 204),
          ("rpmCardEF", 205),
          ("rpmCardEF3", 206),
          ("rpmCardEH", 207),
          ("supCard", 208),
          ("sfmCard", 250),
          ("cardUnknown", 259))
    )



class F10CardOperStatus(TextualConvention, Integer32):
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
          ("cardNotmatch", 2),
          ("cardProblem", 3),
          ("diagMode", 4),
          ("cardAbsent", 5),
          ("offline", 6))
    )



class F10CSeriesPortType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("portSerial", 1),
          ("portAux", 2),
          ("portFastEther", 3),
          ("portGigEther", 4),
          ("port10GigEther", 5),
          ("portUnknown", 99))
    )



class F10SSeriesPortType(TextualConvention, Integer32):
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("portSerial", 1),
          ("portFastEther", 2),
          ("portGigEther", 3),
          ("port10GigEther", 4),
          ("port40GigEther", 5),
          ("portFibreChannel", 6),
          ("portUnknown", 99))
    )



class F10MSeriesPortType(TextualConvention, Integer32):
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("portSerial", 1),
          ("portFastEther", 2),
          ("portGigEther", 3),
          ("port10GigEther", 4),
          ("port40GigEther", 5),
          ("portFC", 6),
          ("portUnknown", 99))
    )



class F10CSeriesCardType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              99,
              200,
              1024,
              1026,
              1027,
              1028,
              1280,
              1284,
              2049)
        )
    )
    namedValues = NamedValues(
        *(("notPresented", 0),
          ("cardUnknown", 99),
          ("rpmCard", 200),
          ("lc4802E48TB", 1024),
          ("lc0410EX4PB", 1026),
          ("lc4801E48PB", 1027),
          ("lc4610E46TB", 1028),
          ("lc4802E48VB", 1280),
          ("lc4610E46VB", 1284),
          ("lc0810EX8PB", 2049))
    )



class F10ProcessorModuleType(TextualConvention, Integer32):
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
        *(("controlProcessor", 1),
          ("routingProcessor1", 2),
          ("routingProcessor2", 3),
          ("linecardProcessor", 4),
          ("rpmProcessor", 5),
          ("routingProcessor", 6))
    )



class F10SlotState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class F10SlotID(TextualConvention, Integer32):
    status = "current"


class F10SwDate(DisplayString):
    status = "current"


class F10MfgDate(DisplayString):
    status = "current"


class PortList(TextualConvention, OctetString):
    status = "current"


class F10VlanID(TextualConvention, Integer32):
    status = "current"


class F10ChassisMode(TextualConvention, Integer32):
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
        *(("nonJumbo", 0),
          ("etherScale", 1),
          ("mixed", 2),
          ("teraScale", 3),
          ("cseries1", 4),
          ("sseries1", 5),
          ("exaScale", 6))
    )



class F10QueueID(TextualConvention, Integer32):
    status = "current"


class F10PortPipeID(TextualConvention, Integer32):
    status = "current"


class F10CycloneVersion(TextualConvention, Integer32):
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
        *(("onePointFive", 1),
          ("twoPointZero", 2),
          ("threePointZero", 3))
    )



class F10CamPartitionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              31,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              91,
              121,
              122)
        )
    )
    namedValues = NamedValues(
        *(("layer2AclIngress", 1),
          ("layer2AclPvstIngress", 2),
          ("layer2FibIngress", 3),
          ("layer2FibEgress", 31),
          ("layer3AclIngress", 61),
          ("layer3FibIngress", 62),
          ("layer3SysFlowIngress", 63),
          ("layer3TrcListIngress", 64),
          ("layer3McastFibIngress", 65),
          ("layer3QosIngress", 66),
          ("layer3PbrIngress", 67),
          ("layer3AclEgress", 91),
          ("layer3ExtHost", 121),
          ("layer3ExtLPM", 122))
    )



class F10HundredthdB(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"


class DellNetDeviceType(TextualConvention, Integer32):
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
        *(("chassis", 1),
          ("stack", 2),
          ("rpm", 3),
          ("supervisor", 4),
          ("linecard", 5),
          ("port-extender", 6))
    )



class DellNetPEOperStatus(TextualConvention, Integer32):
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



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORCE10-TC",
    **{"F10ChassisType": F10ChassisType,
       "F10InterfaceType": F10InterfaceType,
       "F10SystemPortType": F10SystemPortType,
       "F10SystemCardType": F10SystemCardType,
       "F10CardOperStatus": F10CardOperStatus,
       "F10CSeriesPortType": F10CSeriesPortType,
       "F10SSeriesPortType": F10SSeriesPortType,
       "F10MSeriesPortType": F10MSeriesPortType,
       "F10CSeriesCardType": F10CSeriesCardType,
       "F10ProcessorModuleType": F10ProcessorModuleType,
       "F10SlotState": F10SlotState,
       "F10SlotID": F10SlotID,
       "F10SwDate": F10SwDate,
       "F10MfgDate": F10MfgDate,
       "PortList": PortList,
       "F10VlanID": F10VlanID,
       "F10ChassisMode": F10ChassisMode,
       "F10QueueID": F10QueueID,
       "F10PortPipeID": F10PortPipeID,
       "F10CycloneVersion": F10CycloneVersion,
       "F10CamPartitionType": F10CamPartitionType,
       "F10HundredthdB": F10HundredthdB,
       "DellNetDeviceType": DellNetDeviceType,
       "DellNetPEOperStatus": DellNetPEOperStatus,
       "f10TextualConventions": f10TextualConventions}
)
