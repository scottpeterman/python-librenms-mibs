# SNMP MIB module (PDU2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\raritan\PDU2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:13 2025
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
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

raritan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13742)
)
if mibBuilder.loadTexts:
    raritan.setRevisions(
        ("2024-10-07 00:00",
         "2023-11-28 00:00",
         "2023-05-26 00:00",
         "2022-09-21 00:00",
         "2022-06-01 00:00",
         "2022-01-05 00:00",
         "2021-08-03 00:00",
         "2020-12-11 00:00",
         "2020-10-22 00:00",
         "2020-07-06 00:00",
         "2019-11-29 00:00",
         "2019-05-20 00:00",
         "2018-10-16 00:00",
         "2018-05-07 00:00",
         "2018-03-05 00:00",
         "2017-11-13 00:00",
         "2016-12-02 00:00",
         "2016-02-16 00:00",
         "2016-02-09 00:00",
         "2015-10-26 00:00",
         "2015-09-30 00:00",
         "2015-02-18 00:00",
         "2014-06-04 00:00",
         "2014-01-09 00:00",
         "2014-01-07 00:00",
         "2013-11-21 00:00",
         "2013-09-18 00:00",
         "2013-08-01 00:00",
         "2013-07-10 00:00",
         "2013-07-02 00:00",
         "2013-05-21 00:00",
         "2013-04-26 00:00",
         "2013-03-27 00:00",
         "2013-03-25 10:00",
         "2013-03-25 00:00",
         "2013-03-18 00:00",
         "2013-02-25 00:00",
         "2013-02-04 00:00",
         "2013-01-24 00:00",
         "2012-11-20 00:00",
         "2012-11-15 00:00",
         "2012-10-05 00:00",
         "2012-10-04 00:00",
         "2012-09-28 00:00",
         "2012-09-21 00:00",
         "2012-09-20 00:00",
         "2012-09-17 00:00",
         "2012-09-04 00:00",
         "2012-06-22 00:00",
         "2012-06-18 00:00",
         "2012-06-06 00:00",
         "2012-05-25 00:00",
         "2012-05-15 00:00",
         "2012-03-26 00:00",
         "2011-12-13 00:00",
         "2011-11-29 00:00",
         "2011-10-25 00:00",
         "2011-06-16 00:00",
         "2011-03-22 00:00",
         "2011-02-21 00:00",
         "2011-02-14 00:00",
         "2011-02-08 00:00",
         "2011-02-03 00:00",
         "2011-01-31 00:00",
         "2010-12-15 00:00",
         "2010-12-13 11:31",
         "2010-12-13 00:00",
         "2010-12-07 00:00",
         "2010-10-07 00:00",
         "2010-10-04 00:00",
         "2010-09-01 00:00",
         "2010-08-05 00:00",
         "2010-07-23 00:00",
         "2010-07-22 00:00",
         "2010-07-21 00:00",
         "2010-07-14 00:00",
         "2010-07-06 00:00",
         "2010-07-01 00:00",
         "2010-06-30 00:00",
         "2010-06-21 00:00",
         "2010-06-03 00:00",
         "2010-05-27 00:00",
         "2010-05-24 00:00",
         "2010-04-19 00:00",
         "2010-04-15 00:00",
         "2010-04-08 00:00",
         "2010-03-29 00:00",
         "2010-03-25 00:00",
         "2010-03-16 00:00",
         "2010-03-01 00:00",
         "2010-01-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SensorTypeEnumeration(TextualConvention, Integer32):
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
              81)
        )
    )
    namedValues = NamedValues(
        *(("rmsCurrent", 1),
          ("peakCurrent", 2),
          ("unbalancedCurrent", 3),
          ("rmsVoltage", 4),
          ("activePower", 5),
          ("apparentPower", 6),
          ("powerFactor", 7),
          ("activeEnergy", 8),
          ("apparentEnergy", 9),
          ("temperature", 10),
          ("humidity", 11),
          ("airFlow", 12),
          ("airPressure", 13),
          ("onOff", 14),
          ("trip", 15),
          ("vibration", 16),
          ("waterDetection", 17),
          ("smokeDetection", 18),
          ("binary", 19),
          ("contact", 20),
          ("fanSpeed", 21),
          ("surgeProtectorStatus", 22),
          ("frequency", 23),
          ("phaseAngle", 24),
          ("rmsVoltageLN", 25),
          ("residualCurrent", 26),
          ("rcmState", 27),
          ("absoluteHumidity", 28),
          ("reactivePower", 29),
          ("other", 30),
          ("none", 31),
          ("powerQuality", 32),
          ("overloadStatus", 33),
          ("overheatStatus", 34),
          ("displacementPowerFactor", 35),
          ("residualDcCurrent", 36),
          ("fanStatus", 37),
          ("inletPhaseSyncAngle", 38),
          ("inletPhaseSync", 39),
          ("operatingState", 40),
          ("activeInlet", 41),
          ("illuminance", 42),
          ("doorContact", 43),
          ("tamperDetection", 44),
          ("motionDetection", 45),
          ("i1smpsStatus", 46),
          ("i2smpsStatus", 47),
          ("switchStatus", 48),
          ("doorLockState", 49),
          ("doorHandleLock", 50),
          ("crestFactor", 51),
          ("length", 52),
          ("distance", 53),
          ("activePowerDemand", 54),
          ("residualAcCurrent", 55),
          ("particleDensity", 56),
          ("voltageThd", 57),
          ("currentThd", 58),
          ("inrushCurrent", 59),
          ("unbalancedVoltage", 60),
          ("unbalancedLineLineCurrent", 61),
          ("unbalancedLineLineVoltage", 62),
          ("dewPoint", 63),
          ("mass", 64),
          ("flux", 65),
          ("luminousIntensity", 66),
          ("luminousEnergy", 67),
          ("luminousFlux", 68),
          ("luminousEmittance", 69),
          ("electricalResistance", 70),
          ("electricalImpedance", 71),
          ("totalHarmonicDistortion", 72),
          ("magneticFieldStrength", 73),
          ("magneticFluxDensity", 74),
          ("electricFieldStrength", 75),
          ("selection", 76),
          ("rotationalSpeed", 77),
          ("transferSwitchBypassState", 78),
          ("batteryLevel", 79),
          ("installFaultStatus", 80),
          ("transferSwitchOutputStatus", 81))
    )



class SensorStateEnumeration(TextualConvention, Integer32):
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
              36)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", -1),
          ("open", 0),
          ("closed", 1),
          ("belowLowerCritical", 2),
          ("belowLowerWarning", 3),
          ("normal", 4),
          ("aboveUpperWarning", 5),
          ("aboveUpperCritical", 6),
          ("on", 7),
          ("off", 8),
          ("detected", 9),
          ("notDetected", 10),
          ("alarmed", 11),
          ("ok", 12),
          ("fail", 14),
          ("yes", 15),
          ("no", 16),
          ("standby", 17),
          ("one", 18),
          ("two", 19),
          ("inSync", 20),
          ("outOfSync", 21),
          ("i1OpenFault", 22),
          ("i1ShortFault", 23),
          ("i2OpenFault", 24),
          ("i2ShortFault", 25),
          ("fault", 26),
          ("warning", 27),
          ("critical", 28),
          ("selfTest", 29),
          ("nonRedundant", 30),
          ("inactive", 31),
          ("i1Selected", 32),
          ("i2Selected", 33),
          ("i1SelectedAndActive", 34),
          ("i2SelectedAndActive", 35),
          ("bypassActive", 36))
    )



class PlugTypeEnumeration(TextualConvention, Integer32):
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
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
              49)
        )
    )
    namedValues = NamedValues(
        *(("plugOTHER", -1),
          ("plugNONE", 0),
          ("plug56P320", 1),
          ("plug56P520", 2),
          ("plug56P532", 3),
          ("plugCS8365C", 4),
          ("plugIEC320C14", 5),
          ("plugIEC320C20", 6),
          ("plugIEC603093WIRE250V16A", 7),
          ("plugIEC603093WIRE250V20A", 8),
          ("plugIEC603093WIRE250V30A", 9),
          ("plugIEC603093WIRE250V32A", 10),
          ("plugIEC603093WIRE250V60A", 11),
          ("plugIEC603093WIRE250V63A", 12),
          ("plugIEC603093WIRE250V100A", 13),
          ("plugIEC603093WIRE250V125A", 14),
          ("plugIEC603094WIRE250V20A", 15),
          ("plugIEC603094WIRE250V30A", 16),
          ("plugIEC603094WIRE250V60A", 17),
          ("plugIEC603094WIRE250V100A", 18),
          ("plugIEC603095WIRE208V20A", 23),
          ("plugIEC603095WIRE208V30A", 24),
          ("plugIEC603095WIRE208V60A", 25),
          ("plugIEC603095WIRE208V100A", 26),
          ("plugIEC603095WIRE415V16A", 27),
          ("plugIEC603095WIRE415V32A", 28),
          ("plugIEC603095WIRE415V63A", 29),
          ("plugIEC603095WIRE415V125A", 30),
          ("plugIEC603095WIRE480V20A", 31),
          ("plugIEC603095WIRE480V30A", 32),
          ("plugIEC603095WIRE480V60A", 33),
          ("plugIEC603095WIRE480V100A", 34),
          ("plugNEMA515P", 35),
          ("plugNEMAL515P", 36),
          ("plugNEMA520P", 37),
          ("plugNEMAL520P", 38),
          ("plugNEMAL530P", 39),
          ("plugNEMAL615P", 40),
          ("plugNEMAL620P", 41),
          ("plugNEMAL630P", 42),
          ("plugNEMAL1520P", 43),
          ("plugNEMAL1530P", 44),
          ("plugNEMAL2120P", 45),
          ("plugNEMAL2130P", 46),
          ("plugNEMAL2230P", 47),
          ("plug56P320F", 48),
          ("plug56PA320", 49))
    )



class ReceptacleTypeEnumeration(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
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
              48)
        )
    )
    namedValues = NamedValues(
        *(("receptacleOTHER", -1),
          ("receptacleNONE", 0),
          ("receptacleBS1363", 1),
          ("receptacle56P532", 3),
          ("receptacleCS8364C", 4),
          ("receptacleIEC320C13", 5),
          ("receptacleIEC320C19", 6),
          ("receptacleIEC603093WIRE250V16A", 7),
          ("receptacleIEC603093WIRE250V20A", 8),
          ("receptacleIEC603093WIRE250V30A", 9),
          ("receptacleIEC603093WIRE250V32A", 10),
          ("receptacleIEC603093WIRE250V60A", 11),
          ("receptacleIEC603093WIRE250V63A", 12),
          ("receptacleIEC603093WIRE250V100A", 13),
          ("receptacleIEC603093WIRE250V125A", 14),
          ("receptacleIEC603094WIRE250V20A", 15),
          ("receptacleIEC603094WIRE250V30A", 16),
          ("receptacleIEC603094WIRE250V60A", 17),
          ("receptacleIEC603094WIRE250V100A", 18),
          ("receptacleIEC603095WIRE208V20A", 23),
          ("receptacleIEC603095WIRE208V30A", 24),
          ("receptacleIEC603095WIRE208V60A", 25),
          ("receptacleIEC603095WIRE208V100A", 26),
          ("receptacleIEC603095WIRE415V16A", 27),
          ("receptacleIEC603095WIRE415V32A", 28),
          ("receptacleIEC603095WIRE415V63A", 29),
          ("receptacleIEC603095WIRE415V125A", 30),
          ("receptacleIEC603095WIRE480V20A", 31),
          ("receptacleIEC603095WIRE480V30A", 32),
          ("receptacleIEC603095WIRE480V60A", 33),
          ("receptacleIEC603095WIRE480V100A", 34),
          ("receptacleNEMA515R", 35),
          ("receptacleNEMAL515R", 36),
          ("receptacleNEMA520R", 37),
          ("receptacleNEMAL520R", 38),
          ("receptacleNEMAL530R", 39),
          ("receptacleNEMAL615R", 40),
          ("receptacleNEMAL620R", 41),
          ("receptacleNEMAL630R", 42),
          ("receptacleNEMAL1520R", 43),
          ("receptacleNEMAL1530R", 44),
          ("receptacleNEMAL2120RP", 45),
          ("receptacleNEMAL2130R", 46),
          ("receptacleSCHUKOTYPEE", 47),
          ("receptacleSCHUKOTYPEF", 48))
    )



class OverCurrentProtectorTypeEnumeration(TextualConvention, Integer32):
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
        *(("ocpBREAKER1POLE", 1),
          ("ocpBREAKER2POLE", 2),
          ("ocpBREAKER3POLE", 3),
          ("ocpFUSE", 4),
          ("ocpFUSEPAIR", 5),
          ("ocpRCBO2POLE", 6),
          ("ocpRCBO3POLE", 7),
          ("ocpRCBO4POLE", 8))
    )



class BoardTypeEnumeration(TextualConvention, Integer32):
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
        *(("mainController", 1),
          ("inletController", 2),
          ("outletController", 3),
          ("meteringController", 4))
    )



class OutletSwitchingOperationsEnumeration(TextualConvention, Integer32):
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
        *(("off", 0),
          ("on", 1),
          ("cycle", 2))
    )



class SensorUnitsEnumeration(TextualConvention, Integer32):
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
              54)
        )
    )
    namedValues = NamedValues(
        *(("none", -1),
          ("other", 0),
          ("volt", 1),
          ("amp", 2),
          ("watt", 3),
          ("voltamp", 4),
          ("wattHour", 5),
          ("voltampHour", 6),
          ("degreeC", 7),
          ("hertz", 8),
          ("percent", 9),
          ("meterpersec", 10),
          ("pascal", 11),
          ("psi", 12),
          ("g", 13),
          ("degreeF", 14),
          ("feet", 15),
          ("inches", 16),
          ("cm", 17),
          ("meters", 18),
          ("rpm", 19),
          ("degrees", 20),
          ("lux", 21),
          ("grampercubicmeter", 22),
          ("var", 23),
          ("feetpersec", 24),
          ("lbspercubicfoot", 25),
          ("microgrampercubicmeter", 26),
          ("hour", 27),
          ("minute", 28),
          ("second", 29),
          ("coulomb", 30),
          ("kelvin", 31),
          ("voltAmpReactiveHour", 32),
          ("voltPerAmpere", 33),
          ("voltPerMeter", 34),
          ("gram", 35),
          ("meterPerSquareSec", 36),
          ("litersPerHour", 37),
          ("nit", 38),
          ("candela", 39),
          ("lumen", 40),
          ("lumenSecond", 41),
          ("cubicMeter", 42),
          ("radiant", 43),
          ("steradiant", 44),
          ("newton", 45),
          ("joule", 46),
          ("ohm", 47),
          ("tesla", 48),
          ("henry", 49),
          ("farad", 50),
          ("mol", 51),
          ("becquerel", 52),
          ("gray", 53),
          ("sievert", 54))
    )



class DaisychainMemberTypeEnumeration(TextualConvention, Integer32):
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
        *(("standalone", 0),
          ("primaryUnit", 1),
          ("expansionUnit", 2))
    )



class URL(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class GlobalOutletStateOnStartupEnumeration(TextualConvention, Integer32):
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
        *(("off", 0),
          ("on", 1),
          ("lastKnownState", 2))
    )



class OutletStateOnStartupEnumeration(TextualConvention, Integer32):
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
        *(("off", 0),
          ("on", 1),
          ("lastKnownState", 2),
          ("globalOutletStateOnStartup", 3))
    )



class ExternalSensorsZCoordinateUnitsEnumeration(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rackUnits", 0),
          ("text", 1))
    )



class HundredthsOfAPercentage(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



class DeviceIdentificationParameterEnumeration(TextualConvention, Integer32):
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
        *(("pduName", 0),
          ("sysContact", 1),
          ("sysName", 2),
          ("sysLocation", 3))
    )



class TransferSwitchTransferReasonEnumeration(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("startup", 1),
          ("manualTransfer", 2),
          ("automaticReTransfer", 3),
          ("powerFailure", 4),
          ("powerQuality", 5),
          ("overloadAlarm", 6),
          ("overheatAlarm", 7),
          ("internalFailure", 8),
          ("bypassActive", 9))
    )



class ProductTypeEnumeration(TextualConvention, Integer32):
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
        *(("rackPdu", 0),
          ("bcm", 1),
          ("transferSwitch", 2),
          ("powerMeter", 3))
    )



class RelayPowerLossBehaviorEnumeration(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonLatching", 0),
          ("latching", 1))
    )



class TripCauseOutletHandlingEnumeration(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("keepUnchanged", 0),
          ("suspend", 1))
    )



class DeviceCascadeTypeEnumeration(TextualConvention, Integer32):
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
        *(("bridging", 0),
          ("portForwarding", 1),
          ("none", 2))
    )



class PeripheralDeviceFirmwareUpdateStateEnumeration(TextualConvention, Integer32):
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
        *(("started", 1),
          ("successful", 2),
          ("failed", 3))
    )



class PanelLayoutEnumeration(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -1),
          ("oneColumn", 1),
          ("twoColumns", 2))
    )



class PanelNumberingEnumeration(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", -1),
          ("oddEven", 1),
          ("sequential", 2))
    )



class CircuitTypeEnumeration(TextualConvention, Integer32):
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
        *(("onePhaseLL", 1),
          ("onePhaseLN", 2),
          ("onePhaseLLN", 3),
          ("threePhase", 4))
    )



class PhaseEnumeration(TextualConvention, Integer32):
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
        *(("phaseA", 1),
          ("phaseB", 2),
          ("phaseC", 3),
          ("neutral", 4),
          ("earth", 5))
    )



class LineEnumeration(TextualConvention, Integer32):
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
        *(("lineL1", 1),
          ("lineL2", 2),
          ("lineL3", 3),
          ("lineNeutral", 4),
          ("lineDcPositive", 5),
          ("lineDcNegative", 6))
    )



class PowerMeterTypeEnumeration(TextualConvention, Integer32):
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
        *(("singlePhase", 1),
          ("splitPhase", 2),
          ("threePhase", 3))
    )



class NetworkInterfaceTypeEnumeration(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wired", 0),
          ("wireless", 1))
    )



class AddressSourceEnumeration(TextualConvention, Integer32):
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
        *(("static", 1),
          ("dhcp", 2),
          ("dhcpv6", 3))
    )



class HwFailureTypeEnumeration(TextualConvention, Integer32):
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
        *(("networkDeviceNotDetected", 1),
          ("i2cBusStuck", 2),
          ("subCtrlNotReachable", 3),
          ("subCtrlMalfunction", 4),
          ("outletPowerStateInconsistent", 5))
    )



class ServerPowerStateEnumeration(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("on", 1),
          ("off", 2),
          ("shuttingDown", 3))
    )



class ServerPowerControlResultEnumeration(TextualConvention, Integer32):
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
        *(("noError", 0),
          ("shutdownCmdFailed", 1),
          ("switchingOffFailed", 2),
          ("switchingOnFailed", 3),
          ("powerCheckTimeout", 4))
    )



class PduOrientationEnumeration(TextualConvention, Integer32):
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
          ("bottomFeed", 1),
          ("topFeed", 2))
    )



class PortFuseStateEnumeration(TextualConvention, Integer32):
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
          ("good", 1),
          ("tripped", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Pdu2_ObjectIdentity = ObjectIdentity
pdu2 = _Pdu2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0)
)
_TrapInformation_ObjectIdentity = ObjectIdentity
trapInformation = _TrapInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0)
)
_TrapInformationTable_Object = MibTable
trapInformationTable = _TrapInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 1)
)
if mibBuilder.loadTexts:
    trapInformationTable.setStatus("current")
_TrapInformationEntry_Object = MibTableRow
trapInformationEntry = _TrapInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 1, 1)
)
trapInformationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
)
if mibBuilder.loadTexts:
    trapInformationEntry.setStatus("current")
_UserName_Type = DisplayString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 1, 1, 2),
    _UserName_Type()
)
userName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_TargetUser_Type = DisplayString
_TargetUser_Object = MibTableColumn
targetUser = _TargetUser_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 1, 1, 3),
    _TargetUser_Type()
)
targetUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    targetUser.setStatus("current")
_ImageVersion_Type = DisplayString
_ImageVersion_Object = MibTableColumn
imageVersion = _ImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 1, 1, 5),
    _ImageVersion_Type()
)
imageVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    imageVersion.setStatus("current")
_RoleName_Type = DisplayString
_RoleName_Object = MibTableColumn
roleName = _RoleName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 1, 1, 6),
    _RoleName_Type()
)
roleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    roleName.setStatus("current")
_SmtpMessageRecipients_Type = DisplayString
_SmtpMessageRecipients_Object = MibTableColumn
smtpMessageRecipients = _SmtpMessageRecipients_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 1, 1, 7),
    _SmtpMessageRecipients_Type()
)
smtpMessageRecipients.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smtpMessageRecipients.setStatus("current")
_SmtpServer_Type = DisplayString
_SmtpServer_Object = MibTableColumn
smtpServer = _SmtpServer_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 1, 1, 8),
    _SmtpServer_Type()
)
smtpServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smtpServer.setStatus("current")
_NewTargetUser_Type = DisplayString
_NewTargetUser_Object = MibTableColumn
newTargetUser = _NewTargetUser_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 1, 1, 9),
    _NewTargetUser_Type()
)
newTargetUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    newTargetUser.setStatus("current")
_OldSensorState_Type = SensorStateEnumeration
_OldSensorState_Object = MibScalar
oldSensorState = _OldSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 2),
    _OldSensorState_Type()
)
oldSensorState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    oldSensorState.setStatus("current")


class _PduNumber_Type(Integer32):
    """Custom type pduNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduNumber_Type.__name__ = "Integer32"
_PduNumber_Object = MibScalar
pduNumber = _PduNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 3),
    _PduNumber_Type()
)
pduNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pduNumber.setStatus("current")


class _InletPoleNumber_Type(Integer32):
    """Custom type inletPoleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_InletPoleNumber_Type.__name__ = "Integer32"
_InletPoleNumber_Object = MibScalar
inletPoleNumber = _InletPoleNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 5),
    _InletPoleNumber_Type()
)
inletPoleNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    inletPoleNumber.setStatus("current")


class _OutletPoleNumber_Type(Integer32):
    """Custom type outletPoleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_OutletPoleNumber_Type.__name__ = "Integer32"
_OutletPoleNumber_Object = MibScalar
outletPoleNumber = _OutletPoleNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 7),
    _OutletPoleNumber_Type()
)
outletPoleNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    outletPoleNumber.setStatus("current")


class _ExternalSensorNumber_Type(Integer32):
    """Custom type externalSensorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ExternalSensorNumber_Type.__name__ = "Integer32"
_ExternalSensorNumber_Object = MibScalar
externalSensorNumber = _ExternalSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 8),
    _ExternalSensorNumber_Type()
)
externalSensorNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    externalSensorNumber.setStatus("current")
_TypeOfSensor_Type = SensorTypeEnumeration
_TypeOfSensor_Object = MibScalar
typeOfSensor = _TypeOfSensor_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 10),
    _TypeOfSensor_Type()
)
typeOfSensor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    typeOfSensor.setStatus("current")
_ErrorDescription_Type = DisplayString
_ErrorDescription_Object = MibScalar
errorDescription = _ErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 11),
    _ErrorDescription_Type()
)
errorDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    errorDescription.setStatus("current")
_DeviceChangedParameter_Type = DeviceIdentificationParameterEnumeration
_DeviceChangedParameter_Object = MibScalar
deviceChangedParameter = _DeviceChangedParameter_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 12),
    _DeviceChangedParameter_Type()
)
deviceChangedParameter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    deviceChangedParameter.setStatus("current")
_ChangedParameterNewValue_Type = DisplayString
_ChangedParameterNewValue_Object = MibScalar
changedParameterNewValue = _ChangedParameterNewValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 13),
    _ChangedParameterNewValue_Type()
)
changedParameterNewValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    changedParameterNewValue.setStatus("current")
_LhxSupportEnabled_Type = TruthValue
_LhxSupportEnabled_Object = MibScalar
lhxSupportEnabled = _LhxSupportEnabled_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 14),
    _LhxSupportEnabled_Type()
)
lhxSupportEnabled.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lhxSupportEnabled.setStatus("deprecated")
_WebcamModel_Type = DisplayString
_WebcamModel_Object = MibScalar
webcamModel = _WebcamModel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 15),
    _WebcamModel_Type()
)
webcamModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    webcamModel.setStatus("current")
_WebcamConnectionPort_Type = DisplayString
_WebcamConnectionPort_Object = MibScalar
webcamConnectionPort = _WebcamConnectionPort_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 16),
    _WebcamConnectionPort_Type()
)
webcamConnectionPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    webcamConnectionPort.setStatus("current")
_AgentInetPortNumber_Type = InetPortNumber
_AgentInetPortNumber_Object = MibScalar
agentInetPortNumber = _AgentInetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 18),
    _AgentInetPortNumber_Type()
)
agentInetPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentInetPortNumber.setStatus("current")
_PeripheralDeviceRomcode_Type = DisplayString
_PeripheralDeviceRomcode_Object = MibScalar
peripheralDeviceRomcode = _PeripheralDeviceRomcode_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 19),
    _PeripheralDeviceRomcode_Type()
)
peripheralDeviceRomcode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    peripheralDeviceRomcode.setStatus("current")
_PeripheralDeviceFirmwareUpdateState_Type = PeripheralDeviceFirmwareUpdateStateEnumeration
_PeripheralDeviceFirmwareUpdateState_Object = MibScalar
peripheralDeviceFirmwareUpdateState = _PeripheralDeviceFirmwareUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 20),
    _PeripheralDeviceFirmwareUpdateState_Type()
)
peripheralDeviceFirmwareUpdateState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    peripheralDeviceFirmwareUpdateState.setStatus("current")


class _CircuitNumber_Type(Integer32):
    """Custom type circuitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33000),
    )


_CircuitNumber_Type.__name__ = "Integer32"
_CircuitNumber_Object = MibScalar
circuitNumber = _CircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 21),
    _CircuitNumber_Type()
)
circuitNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    circuitNumber.setStatus("current")


class _CircuitPoleNumber_Type(Integer32):
    """Custom type circuitPoleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CircuitPoleNumber_Type.__name__ = "Integer32"
_CircuitPoleNumber_Object = MibScalar
circuitPoleNumber = _CircuitPoleNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 22),
    _CircuitPoleNumber_Type()
)
circuitPoleNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    circuitPoleNumber.setStatus("current")
_PhoneNumber_Type = DisplayString
_PhoneNumber_Object = MibScalar
phoneNumber = _PhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 23),
    _PhoneNumber_Type()
)
phoneNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    phoneNumber.setStatus("current")
_SmartCardReaderId_Type = DisplayString
_SmartCardReaderId_Object = MibScalar
smartCardReaderId = _SmartCardReaderId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 24),
    _SmartCardReaderId_Type()
)
smartCardReaderId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartCardReaderId.setStatus("current")
_SmartCardTimestamp_Type = Unsigned32
_SmartCardTimestamp_Object = MibScalar
smartCardTimestamp = _SmartCardTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 25),
    _SmartCardTimestamp_Type()
)
smartCardTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartCardTimestamp.setStatus("current")
_SmartCardType_Type = DisplayString
_SmartCardType_Object = MibScalar
smartCardType = _SmartCardType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 26),
    _SmartCardType_Type()
)
smartCardType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartCardType.setStatus("current")
_SmartCardId_Type = DisplayString
_SmartCardId_Object = MibScalar
smartCardId = _SmartCardId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 27),
    _SmartCardId_Type()
)
smartCardId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartCardId.setStatus("current")
_SuspectedTripCauseLabel_Type = DisplayString
_SuspectedTripCauseLabel_Object = MibScalar
suspectedTripCauseLabel = _SuspectedTripCauseLabel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 28),
    _SuspectedTripCauseLabel_Type()
)
suspectedTripCauseLabel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    suspectedTripCauseLabel.setStatus("current")
_SmartCardReaderManufacturer_Type = DisplayString
_SmartCardReaderManufacturer_Object = MibScalar
smartCardReaderManufacturer = _SmartCardReaderManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 29),
    _SmartCardReaderManufacturer_Type()
)
smartCardReaderManufacturer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartCardReaderManufacturer.setStatus("current")
_SmartCardReaderProduct_Type = DisplayString
_SmartCardReaderProduct_Object = MibScalar
smartCardReaderProduct = _SmartCardReaderProduct_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 30),
    _SmartCardReaderProduct_Type()
)
smartCardReaderProduct.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartCardReaderProduct.setStatus("current")
_SmartCardReaderSerialNumber_Type = DisplayString
_SmartCardReaderSerialNumber_Object = MibScalar
smartCardReaderSerialNumber = _SmartCardReaderSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 31),
    _SmartCardReaderSerialNumber_Type()
)
smartCardReaderSerialNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartCardReaderSerialNumber.setStatus("current")


class _SmartCardReaderChannel_Type(Integer32):
    """Custom type smartCardReaderChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 256),
    )


_SmartCardReaderChannel_Type.__name__ = "Integer32"
_SmartCardReaderChannel_Object = MibScalar
smartCardReaderChannel = _SmartCardReaderChannel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 32),
    _SmartCardReaderChannel_Type()
)
smartCardReaderChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartCardReaderChannel.setStatus("current")


class _OutletGroupNumber_Type(Integer32):
    """Custom type outletGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_OutletGroupNumber_Type.__name__ = "Integer32"
_OutletGroupNumber_Object = MibScalar
outletGroupNumber = _OutletGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 33),
    _OutletGroupNumber_Type()
)
outletGroupNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    outletGroupNumber.setStatus("current")
_ServerPowerOperation_Type = DisplayString
_ServerPowerOperation_Object = MibScalar
serverPowerOperation = _ServerPowerOperation_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 34),
    _ServerPowerOperation_Type()
)
serverPowerOperation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    serverPowerOperation.setStatus("current")
_ServerPowerResult_Type = ServerPowerControlResultEnumeration
_ServerPowerResult_Object = MibScalar
serverPowerResult = _ServerPowerResult_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 35),
    _ServerPowerResult_Type()
)
serverPowerResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    serverPowerResult.setStatus("current")
_WebcamName_Type = DisplayString
_WebcamName_Object = MibScalar
webcamName = _WebcamName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 36),
    _WebcamName_Type()
)
webcamName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    webcamName.setStatus("current")
_WebcamFolderUrl_Type = DisplayString
_WebcamFolderUrl_Object = MibScalar
webcamFolderUrl = _WebcamFolderUrl_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 37),
    _WebcamFolderUrl_Type()
)
webcamFolderUrl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    webcamFolderUrl.setStatus("current")
_KeypadId_Type = DisplayString
_KeypadId_Object = MibScalar
keypadId = _KeypadId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 38),
    _KeypadId_Type()
)
keypadId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    keypadId.setStatus("current")
_KeypadPinTimestamp_Type = Unsigned32
_KeypadPinTimestamp_Object = MibScalar
keypadPinTimestamp = _KeypadPinTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 39),
    _KeypadPinTimestamp_Type()
)
keypadPinTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    keypadPinTimestamp.setStatus("current")
_KeypadPin_Type = DisplayString
_KeypadPin_Object = MibScalar
keypadPin = _KeypadPin_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 40),
    _KeypadPin_Type()
)
keypadPin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    keypadPin.setStatus("current")
_KeypadManufacturer_Type = DisplayString
_KeypadManufacturer_Object = MibScalar
keypadManufacturer = _KeypadManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 41),
    _KeypadManufacturer_Type()
)
keypadManufacturer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    keypadManufacturer.setStatus("current")
_KeypadProduct_Type = DisplayString
_KeypadProduct_Object = MibScalar
keypadProduct = _KeypadProduct_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 42),
    _KeypadProduct_Type()
)
keypadProduct.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    keypadProduct.setStatus("current")
_KeypadSerialNumber_Type = DisplayString
_KeypadSerialNumber_Object = MibScalar
keypadSerialNumber = _KeypadSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 43),
    _KeypadSerialNumber_Type()
)
keypadSerialNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    keypadSerialNumber.setStatus("current")


class _KeypadChannel_Type(Integer32):
    """Custom type keypadChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 256),
    )


_KeypadChannel_Type.__name__ = "Integer32"
_KeypadChannel_Object = MibScalar
keypadChannel = _KeypadChannel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 44),
    _KeypadChannel_Type()
)
keypadChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    keypadChannel.setStatus("current")


class _DoorAccessRuleId_Type(Integer32):
    """Custom type doorAccessRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 256),
    )


_DoorAccessRuleId_Type.__name__ = "Integer32"
_DoorAccessRuleId_Object = MibScalar
doorAccessRuleId = _DoorAccessRuleId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 45),
    _DoorAccessRuleId_Type()
)
doorAccessRuleId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    doorAccessRuleId.setStatus("current")
_DoorAccessDenialReason_Type = DisplayString
_DoorAccessDenialReason_Object = MibScalar
doorAccessDenialReason = _DoorAccessDenialReason_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 46),
    _DoorAccessDenialReason_Type()
)
doorAccessDenialReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    doorAccessDenialReason.setStatus("current")
_DoorAccessRuleName_Type = DisplayString
_DoorAccessRuleName_Object = MibScalar
doorAccessRuleName = _DoorAccessRuleName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 47),
    _DoorAccessRuleName_Type()
)
doorAccessRuleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    doorAccessRuleName.setStatus("current")
_SmartCardReaderPosition_Type = DisplayString
_SmartCardReaderPosition_Object = MibScalar
smartCardReaderPosition = _SmartCardReaderPosition_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 48),
    _SmartCardReaderPosition_Type()
)
smartCardReaderPosition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartCardReaderPosition.setStatus("current")
_KeypadPosition_Type = DisplayString
_KeypadPosition_Object = MibScalar
keypadPosition = _KeypadPosition_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 49),
    _KeypadPosition_Type()
)
keypadPosition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    keypadPosition.setStatus("current")
_KeypadDescription_Type = DisplayString
_KeypadDescription_Object = MibScalar
keypadDescription = _KeypadDescription_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 50),
    _KeypadDescription_Type()
)
keypadDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    keypadDescription.setStatus("current")
_KeypadName_Type = DisplayString
_KeypadName_Object = MibScalar
keypadName = _KeypadName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 51),
    _KeypadName_Type()
)
keypadName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    keypadName.setStatus("current")
_SmartCardReaderDescription_Type = DisplayString
_SmartCardReaderDescription_Object = MibScalar
smartCardReaderDescription = _SmartCardReaderDescription_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 52),
    _SmartCardReaderDescription_Type()
)
smartCardReaderDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartCardReaderDescription.setStatus("current")
_SmartCardReaderName_Type = DisplayString
_SmartCardReaderName_Object = MibScalar
smartCardReaderName = _SmartCardReaderName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 53),
    _SmartCardReaderName_Type()
)
smartCardReaderName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartCardReaderName.setStatus("current")


class _InletLinePairNumber_Type(Integer32):
    """Custom type inletLinePairNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_InletLinePairNumber_Type.__name__ = "Integer32"
_InletLinePairNumber_Object = MibScalar
inletLinePairNumber = _InletLinePairNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 54),
    _InletLinePairNumber_Type()
)
inletLinePairNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    inletLinePairNumber.setStatus("current")
_DipSwellEventVoltage_Type = Unsigned32
_DipSwellEventVoltage_Object = MibScalar
dipSwellEventVoltage = _DipSwellEventVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 55),
    _DipSwellEventVoltage_Type()
)
dipSwellEventVoltage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dipSwellEventVoltage.setStatus("current")
_DipSwellEventTimeStamp_Type = Unsigned32
_DipSwellEventTimeStamp_Object = MibScalar
dipSwellEventTimeStamp = _DipSwellEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 56),
    _DipSwellEventTimeStamp_Type()
)
dipSwellEventTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dipSwellEventTimeStamp.setStatus("current")
_DipSwellEventDuration_Type = Unsigned32
_DipSwellEventDuration_Object = MibScalar
dipSwellEventDuration = _DipSwellEventDuration_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 57),
    _DipSwellEventDuration_Type()
)
dipSwellEventDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dipSwellEventDuration.setStatus("current")
_PortFuseState_Type = PortFuseStateEnumeration
_PortFuseState_Object = MibScalar
portFuseState = _PortFuseState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 58),
    _PortFuseState_Type()
)
portFuseState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    portFuseState.setStatus("current")
_ExternalPortFuseId_Type = DisplayString
_ExternalPortFuseId_Object = MibScalar
externalPortFuseId = _ExternalPortFuseId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 59),
    _ExternalPortFuseId_Type()
)
externalPortFuseId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    externalPortFuseId.setStatus("current")
_ExternalPortName_Type = DisplayString
_ExternalPortName_Object = MibScalar
externalPortName = _ExternalPortName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 60),
    _ExternalPortName_Type()
)
externalPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    externalPortName.setStatus("current")


class _LinkUnitId_Type(Integer32):
    """Custom type linkUnitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 256),
    )


_LinkUnitId_Type.__name__ = "Integer32"
_LinkUnitId_Object = MibScalar
linkUnitId = _LinkUnitId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 61),
    _LinkUnitId_Type()
)
linkUnitId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    linkUnitId.setStatus("current")
_LinkUnitAddress_Type = DisplayString
_LinkUnitAddress_Object = MibScalar
linkUnitAddress = _LinkUnitAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 62),
    _LinkUnitAddress_Type()
)
linkUnitAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    linkUnitAddress.setStatus("current")
_DoorHandleName_Type = DisplayString
_DoorHandleName_Object = MibScalar
doorHandleName = _DoorHandleName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 63),
    _DoorHandleName_Type()
)
doorHandleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    doorHandleName.setStatus("current")
_DoorLockName_Type = DisplayString
_DoorLockName_Object = MibScalar
doorLockName = _DoorLockName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 64),
    _DoorLockName_Type()
)
doorLockName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    doorLockName.setStatus("current")
_DoorStateName_Type = DisplayString
_DoorStateName_Object = MibScalar
doorStateName = _DoorStateName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 0, 65),
    _DoorStateName_Type()
)
doorStateName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    doorStateName.setStatus("current")
_Board_ObjectIdentity = ObjectIdentity
board = _Board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 1)
)
_Environmental_ObjectIdentity = ObjectIdentity
environmental = _Environmental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 2)
)
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3)
)
_PduCount_Type = Integer32
_PduCount_Object = MibScalar
pduCount = _PduCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 1),
    _PduCount_Type()
)
pduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCount.setStatus("current")
_Unit_ObjectIdentity = ObjectIdentity
unit = _Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2)
)
_NameplateTable_Object = MibTable
nameplateTable = _NameplateTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    nameplateTable.setStatus("current")
_NameplateEntry_Object = MibTableRow
nameplateEntry = _NameplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 1, 1)
)
nameplateEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
)
if mibBuilder.loadTexts:
    nameplateEntry.setStatus("current")


class _PduId_Type(Integer32):
    """Custom type pduId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_PduId_Type.__name__ = "Integer32"
_PduId_Object = MibTableColumn
pduId = _PduId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 1, 1, 1),
    _PduId_Type()
)
pduId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduId.setStatus("current")
_PduManufacturer_Type = DisplayString
_PduManufacturer_Object = MibTableColumn
pduManufacturer = _PduManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 1, 1, 2),
    _PduManufacturer_Type()
)
pduManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduManufacturer.setStatus("current")
_PduModel_Type = DisplayString
_PduModel_Object = MibTableColumn
pduModel = _PduModel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 1, 1, 3),
    _PduModel_Type()
)
pduModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduModel.setStatus("current")
_PduSerialNumber_Type = DisplayString
_PduSerialNumber_Object = MibTableColumn
pduSerialNumber = _PduSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 1, 1, 4),
    _PduSerialNumber_Type()
)
pduSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduSerialNumber.setStatus("current")
_PduRatedVoltage_Type = DisplayString
_PduRatedVoltage_Object = MibTableColumn
pduRatedVoltage = _PduRatedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 1, 1, 5),
    _PduRatedVoltage_Type()
)
pduRatedVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduRatedVoltage.setStatus("current")
_PduRatedCurrent_Type = DisplayString
_PduRatedCurrent_Object = MibTableColumn
pduRatedCurrent = _PduRatedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 1, 1, 6),
    _PduRatedCurrent_Type()
)
pduRatedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduRatedCurrent.setStatus("current")
_PduRatedFrequency_Type = DisplayString
_PduRatedFrequency_Object = MibTableColumn
pduRatedFrequency = _PduRatedFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 1, 1, 7),
    _PduRatedFrequency_Type()
)
pduRatedFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduRatedFrequency.setStatus("current")
_PduRatedVA_Type = DisplayString
_PduRatedVA_Object = MibTableColumn
pduRatedVA = _PduRatedVA_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 1, 1, 8),
    _PduRatedVA_Type()
)
pduRatedVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduRatedVA.setStatus("current")
_PduImage_Type = URL
_PduImage_Object = MibTableColumn
pduImage = _PduImage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 1, 1, 9),
    _PduImage_Type()
)
pduImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduImage.setStatus("current")
_UnitConfigurationTable_Object = MibTable
unitConfigurationTable = _UnitConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2)
)
if mibBuilder.loadTexts:
    unitConfigurationTable.setStatus("current")
_UnitConfigurationEntry_Object = MibTableRow
unitConfigurationEntry = _UnitConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1)
)
unitConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
)
if mibBuilder.loadTexts:
    unitConfigurationEntry.setStatus("current")


class _InletCount_Type(Integer32):
    """Custom type inletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_InletCount_Type.__name__ = "Integer32"
_InletCount_Object = MibTableColumn
inletCount = _InletCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 2),
    _InletCount_Type()
)
inletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletCount.setStatus("current")


class _OverCurrentProtectorCount_Type(Integer32):
    """Custom type overCurrentProtectorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OverCurrentProtectorCount_Type.__name__ = "Integer32"
_OverCurrentProtectorCount_Object = MibTableColumn
overCurrentProtectorCount = _OverCurrentProtectorCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 3),
    _OverCurrentProtectorCount_Type()
)
overCurrentProtectorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorCount.setStatus("current")


class _OutletCount_Type(Integer32):
    """Custom type outletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_OutletCount_Type.__name__ = "Integer32"
_OutletCount_Object = MibTableColumn
outletCount = _OutletCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 4),
    _OutletCount_Type()
)
outletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletCount.setStatus("current")


class _InletControllerCount_Type(Integer32):
    """Custom type inletControllerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_InletControllerCount_Type.__name__ = "Integer32"
_InletControllerCount_Object = MibTableColumn
inletControllerCount = _InletControllerCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 5),
    _InletControllerCount_Type()
)
inletControllerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletControllerCount.setStatus("current")


class _OutletControllerCount_Type(Integer32):
    """Custom type outletControllerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OutletControllerCount_Type.__name__ = "Integer32"
_OutletControllerCount_Object = MibTableColumn
outletControllerCount = _OutletControllerCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 6),
    _OutletControllerCount_Type()
)
outletControllerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletControllerCount.setStatus("current")


class _ExternalSensorCount_Type(Integer32):
    """Custom type externalSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExternalSensorCount_Type.__name__ = "Integer32"
_ExternalSensorCount_Object = MibTableColumn
externalSensorCount = _ExternalSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 7),
    _ExternalSensorCount_Type()
)
externalSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorCount.setStatus("current")
_PxIPAddress_Type = IpAddress
_PxIPAddress_Object = MibTableColumn
pxIPAddress = _PxIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 8),
    _PxIPAddress_Type()
)
pxIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxIPAddress.setStatus("deprecated")
_Netmask_Type = IpAddress
_Netmask_Object = MibTableColumn
netmask = _Netmask_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 9),
    _Netmask_Type()
)
netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netmask.setStatus("deprecated")
_Gateway_Type = IpAddress
_Gateway_Object = MibTableColumn
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 10),
    _Gateway_Type()
)
gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gateway.setStatus("deprecated")
_PxMACAddress_Type = MacAddress
_PxMACAddress_Object = MibTableColumn
pxMACAddress = _PxMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 11),
    _PxMACAddress_Type()
)
pxMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxMACAddress.setStatus("deprecated")
_UtcOffset_Type = DisplayString
_UtcOffset_Object = MibTableColumn
utcOffset = _UtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 12),
    _UtcOffset_Type()
)
utcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utcOffset.setStatus("current")
_PduName_Type = DisplayString
_PduName_Object = MibTableColumn
pduName = _PduName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 13),
    _PduName_Type()
)
pduName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduName.setStatus("current")
_NetworkInterfaceType_Type = NetworkInterfaceTypeEnumeration
_NetworkInterfaceType_Object = MibTableColumn
networkInterfaceType = _NetworkInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 14),
    _NetworkInterfaceType_Type()
)
networkInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkInterfaceType.setStatus("deprecated")
_ExternalSensorsZCoordinateUnits_Type = ExternalSensorsZCoordinateUnitsEnumeration
_ExternalSensorsZCoordinateUnits_Object = MibTableColumn
externalSensorsZCoordinateUnits = _ExternalSensorsZCoordinateUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 34),
    _ExternalSensorsZCoordinateUnits_Type()
)
externalSensorsZCoordinateUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorsZCoordinateUnits.setStatus("current")


class _UnitDeviceCapabilities_Type(Bits):
    """Custom type unitDeviceCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("activePower", 4),
          ("apparentPower", 5),
          ("activeEnergy", 7),
          ("apparentEnergy", 8),
          ("i1smpsStatus", 45),
          ("i2smpsStatus", 46))
    )

_UnitDeviceCapabilities_Type.__name__ = "Bits"
_UnitDeviceCapabilities_Object = MibTableColumn
unitDeviceCapabilities = _UnitDeviceCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 35),
    _UnitDeviceCapabilities_Type()
)
unitDeviceCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitDeviceCapabilities.setStatus("current")


class _OutletSequencingDelay_Type(Unsigned32):
    """Custom type outletSequencingDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_OutletSequencingDelay_Type.__name__ = "Unsigned32"
_OutletSequencingDelay_Object = MibTableColumn
outletSequencingDelay = _OutletSequencingDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 36),
    _OutletSequencingDelay_Type()
)
outletSequencingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSequencingDelay.setStatus("deprecated")


class _GlobalOutletPowerCyclingPowerOffPeriod_Type(Unsigned32):
    """Custom type globalOutletPowerCyclingPowerOffPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_GlobalOutletPowerCyclingPowerOffPeriod_Type.__name__ = "Unsigned32"
_GlobalOutletPowerCyclingPowerOffPeriod_Object = MibTableColumn
globalOutletPowerCyclingPowerOffPeriod = _GlobalOutletPowerCyclingPowerOffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 37),
    _GlobalOutletPowerCyclingPowerOffPeriod_Type()
)
globalOutletPowerCyclingPowerOffPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalOutletPowerCyclingPowerOffPeriod.setStatus("current")
_GlobalOutletStateOnStartup_Type = GlobalOutletStateOnStartupEnumeration
_GlobalOutletStateOnStartup_Object = MibTableColumn
globalOutletStateOnStartup = _GlobalOutletStateOnStartup_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 38),
    _GlobalOutletStateOnStartup_Type()
)
globalOutletStateOnStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalOutletStateOnStartup.setStatus("current")
_OutletPowerupSequence_Type = DisplayString
_OutletPowerupSequence_Object = MibTableColumn
outletPowerupSequence = _OutletPowerupSequence_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 39),
    _OutletPowerupSequence_Type()
)
outletPowerupSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPowerupSequence.setStatus("current")


class _PduPowerCyclingPowerOffPeriod_Type(Unsigned32):
    """Custom type pduPowerCyclingPowerOffPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_PduPowerCyclingPowerOffPeriod_Type.__name__ = "Unsigned32"
_PduPowerCyclingPowerOffPeriod_Object = MibTableColumn
pduPowerCyclingPowerOffPeriod = _PduPowerCyclingPowerOffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 40),
    _PduPowerCyclingPowerOffPeriod_Type()
)
pduPowerCyclingPowerOffPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduPowerCyclingPowerOffPeriod.setStatus("current")
_PduDaisychainMemberType_Type = DaisychainMemberTypeEnumeration
_PduDaisychainMemberType_Object = MibTableColumn
pduDaisychainMemberType = _PduDaisychainMemberType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 41),
    _PduDaisychainMemberType_Type()
)
pduDaisychainMemberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduDaisychainMemberType.setStatus("current")


class _ManagedExternalSensorCount_Type(Integer32):
    """Custom type managedExternalSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ManagedExternalSensorCount_Type.__name__ = "Integer32"
_ManagedExternalSensorCount_Object = MibTableColumn
managedExternalSensorCount = _ManagedExternalSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 42),
    _ManagedExternalSensorCount_Type()
)
managedExternalSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedExternalSensorCount.setStatus("current")
_PxInetAddressType_Type = InetAddressType
_PxInetAddressType_Object = MibTableColumn
pxInetAddressType = _PxInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 50),
    _PxInetAddressType_Type()
)
pxInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxInetAddressType.setStatus("deprecated")
_PxInetIPAddress_Type = InetAddress
_PxInetIPAddress_Object = MibTableColumn
pxInetIPAddress = _PxInetIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 51),
    _PxInetIPAddress_Type()
)
pxInetIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxInetIPAddress.setStatus("deprecated")
_PxInetNetmask_Type = InetAddress
_PxInetNetmask_Object = MibTableColumn
pxInetNetmask = _PxInetNetmask_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 52),
    _PxInetNetmask_Type()
)
pxInetNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxInetNetmask.setStatus("deprecated")
_PxInetGateway_Type = InetAddress
_PxInetGateway_Object = MibTableColumn
pxInetGateway = _PxInetGateway_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 53),
    _PxInetGateway_Type()
)
pxInetGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxInetGateway.setStatus("deprecated")
_LoadShedding_Type = TruthValue
_LoadShedding_Object = MibTableColumn
loadShedding = _LoadShedding_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 55),
    _LoadShedding_Type()
)
loadShedding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadShedding.setStatus("current")


class _ServerCount_Type(Integer32):
    """Custom type serverCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ServerCount_Type.__name__ = "Integer32"
_ServerCount_Object = MibTableColumn
serverCount = _ServerCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 56),
    _ServerCount_Type()
)
serverCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCount.setStatus("current")


class _InrushGuardDelay_Type(Unsigned32):
    """Custom type inrushGuardDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_InrushGuardDelay_Type.__name__ = "Unsigned32"
_InrushGuardDelay_Object = MibTableColumn
inrushGuardDelay = _InrushGuardDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 57),
    _InrushGuardDelay_Type()
)
inrushGuardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inrushGuardDelay.setStatus("current")
_CascadedDeviceConnected_Type = TruthValue
_CascadedDeviceConnected_Object = MibTableColumn
cascadedDeviceConnected = _CascadedDeviceConnected_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 58),
    _CascadedDeviceConnected_Type()
)
cascadedDeviceConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cascadedDeviceConnected.setStatus("current")
_SynchronizeWithNTPServer_Type = TruthValue
_SynchronizeWithNTPServer_Object = MibTableColumn
synchronizeWithNTPServer = _SynchronizeWithNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 59),
    _SynchronizeWithNTPServer_Type()
)
synchronizeWithNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    synchronizeWithNTPServer.setStatus("current")
_UseDHCPProvidedNTPServer_Type = TruthValue
_UseDHCPProvidedNTPServer_Object = MibTableColumn
useDHCPProvidedNTPServer = _UseDHCPProvidedNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 60),
    _UseDHCPProvidedNTPServer_Type()
)
useDHCPProvidedNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useDHCPProvidedNTPServer.setStatus("obsolete")


class _FirstNTPServerAddressType_Type(InetAddressType):
    """Custom type firstNTPServerAddressType based on InetAddressType"""
    defaultValue = 1


_FirstNTPServerAddressType_Type.__name__ = "InetAddressType"
_FirstNTPServerAddressType_Object = MibTableColumn
firstNTPServerAddressType = _FirstNTPServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 61),
    _FirstNTPServerAddressType_Type()
)
firstNTPServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstNTPServerAddressType.setStatus("current")
_FirstNTPServerAddress_Type = InetAddress
_FirstNTPServerAddress_Object = MibTableColumn
firstNTPServerAddress = _FirstNTPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 62),
    _FirstNTPServerAddress_Type()
)
firstNTPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firstNTPServerAddress.setStatus("current")
_SecondNTPServerAddressType_Type = InetAddressType
_SecondNTPServerAddressType_Object = MibTableColumn
secondNTPServerAddressType = _SecondNTPServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 63),
    _SecondNTPServerAddressType_Type()
)
secondNTPServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondNTPServerAddressType.setStatus("current")
_SecondNTPServerAddress_Type = InetAddress
_SecondNTPServerAddress_Object = MibTableColumn
secondNTPServerAddress = _SecondNTPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 64),
    _SecondNTPServerAddress_Type()
)
secondNTPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondNTPServerAddress.setStatus("current")


class _WireCount_Type(Integer32):
    """Custom type wireCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WireCount_Type.__name__ = "Integer32"
_WireCount_Object = MibTableColumn
wireCount = _WireCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 65),
    _WireCount_Type()
)
wireCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wireCount.setStatus("obsolete")


class _TransferSwitchCount_Type(Integer32):
    """Custom type transferSwitchCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TransferSwitchCount_Type.__name__ = "Integer32"
_TransferSwitchCount_Object = MibTableColumn
transferSwitchCount = _TransferSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 66),
    _TransferSwitchCount_Type()
)
transferSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchCount.setStatus("current")
_ProductType_Type = ProductTypeEnumeration
_ProductType_Object = MibTableColumn
productType = _ProductType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 67),
    _ProductType_Type()
)
productType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productType.setStatus("current")


class _MeteringControllerCount_Type(Integer32):
    """Custom type meteringControllerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MeteringControllerCount_Type.__name__ = "Integer32"
_MeteringControllerCount_Object = MibTableColumn
meteringControllerCount = _MeteringControllerCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 68),
    _MeteringControllerCount_Type()
)
meteringControllerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meteringControllerCount.setStatus("current")
_RelayBehaviorOnPowerLoss_Type = RelayPowerLossBehaviorEnumeration
_RelayBehaviorOnPowerLoss_Object = MibTableColumn
relayBehaviorOnPowerLoss = _RelayBehaviorOnPowerLoss_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 69),
    _RelayBehaviorOnPowerLoss_Type()
)
relayBehaviorOnPowerLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayBehaviorOnPowerLoss.setStatus("current")
_DeviceCascadeType_Type = DeviceCascadeTypeEnumeration
_DeviceCascadeType_Object = MibTableColumn
deviceCascadeType = _DeviceCascadeType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 70),
    _DeviceCascadeType_Type()
)
deviceCascadeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCascadeType.setStatus("current")


class _DeviceCascadePosition_Type(Integer32):
    """Custom type deviceCascadePosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_DeviceCascadePosition_Type.__name__ = "Integer32"
_DeviceCascadePosition_Object = MibTableColumn
deviceCascadePosition = _DeviceCascadePosition_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 71),
    _DeviceCascadePosition_Type()
)
deviceCascadePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCascadePosition.setStatus("current")
_PeripheralDevicesAutoManagement_Type = TruthValue
_PeripheralDevicesAutoManagement_Object = MibTableColumn
peripheralDevicesAutoManagement = _PeripheralDevicesAutoManagement_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 72),
    _PeripheralDevicesAutoManagement_Type()
)
peripheralDevicesAutoManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peripheralDevicesAutoManagement.setStatus("current")
_FrontPanelOutletSwitching_Type = TruthValue
_FrontPanelOutletSwitching_Object = MibTableColumn
frontPanelOutletSwitching = _FrontPanelOutletSwitching_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 73),
    _FrontPanelOutletSwitching_Type()
)
frontPanelOutletSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frontPanelOutletSwitching.setStatus("current")
_FrontPanelRCMSelfTest_Type = TruthValue
_FrontPanelRCMSelfTest_Object = MibTableColumn
frontPanelRCMSelfTest = _FrontPanelRCMSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 74),
    _FrontPanelRCMSelfTest_Type()
)
frontPanelRCMSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frontPanelRCMSelfTest.setStatus("current")
_FrontPanelActuatorControl_Type = TruthValue
_FrontPanelActuatorControl_Object = MibTableColumn
frontPanelActuatorControl = _FrontPanelActuatorControl_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 75),
    _FrontPanelActuatorControl_Type()
)
frontPanelActuatorControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frontPanelActuatorControl.setStatus("current")


class _CircuitCount_Type(Integer32):
    """Custom type circuitCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CircuitCount_Type.__name__ = "Integer32"
_CircuitCount_Object = MibTableColumn
circuitCount = _CircuitCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 76),
    _CircuitCount_Type()
)
circuitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitCount.setStatus("current")


class _ActiveDNSServerCount_Type(Integer32):
    """Custom type activeDNSServerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ActiveDNSServerCount_Type.__name__ = "Integer32"
_ActiveDNSServerCount_Object = MibTableColumn
activeDNSServerCount = _ActiveDNSServerCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 77),
    _ActiveDNSServerCount_Type()
)
activeDNSServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeDNSServerCount.setStatus("current")


class _ActiveNTPServerCount_Type(Integer32):
    """Custom type activeNTPServerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ActiveNTPServerCount_Type.__name__ = "Integer32"
_ActiveNTPServerCount_Object = MibTableColumn
activeNTPServerCount = _ActiveNTPServerCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 78),
    _ActiveNTPServerCount_Type()
)
activeNTPServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeNTPServerCount.setStatus("current")


class _PeripheralDevicePackageCount_Type(Integer32):
    """Custom type peripheralDevicePackageCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_PeripheralDevicePackageCount_Type.__name__ = "Integer32"
_PeripheralDevicePackageCount_Object = MibTableColumn
peripheralDevicePackageCount = _PeripheralDevicePackageCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 79),
    _PeripheralDevicePackageCount_Type()
)
peripheralDevicePackageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peripheralDevicePackageCount.setStatus("current")


class _OutletGroupCount_Type(Integer32):
    """Custom type outletGroupCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_OutletGroupCount_Type.__name__ = "Integer32"
_OutletGroupCount_Object = MibTableColumn
outletGroupCount = _OutletGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 80),
    _OutletGroupCount_Type()
)
outletGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletGroupCount.setStatus("current")


class _DemandUpdateInterval_Type(Unsigned32):
    """Custom type demandUpdateInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 300),
    )


_DemandUpdateInterval_Type.__name__ = "Unsigned32"
_DemandUpdateInterval_Object = MibTableColumn
demandUpdateInterval = _DemandUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 81),
    _DemandUpdateInterval_Type()
)
demandUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    demandUpdateInterval.setStatus("current")


class _DemandAveragingIntervals_Type(Unsigned32):
    """Custom type demandAveragingIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_DemandAveragingIntervals_Type.__name__ = "Unsigned32"
_DemandAveragingIntervals_Object = MibTableColumn
demandAveragingIntervals = _DemandAveragingIntervals_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 82),
    _DemandAveragingIntervals_Type()
)
demandAveragingIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    demandAveragingIntervals.setStatus("current")
_HasDCInlets_Type = TruthValue
_HasDCInlets_Object = MibTableColumn
hasDCInlets = _HasDCInlets_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 83),
    _HasDCInlets_Type()
)
hasDCInlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hasDCInlets.setStatus("current")
_PduOrientation_Type = PduOrientationEnumeration
_PduOrientation_Object = MibTableColumn
pduOrientation = _PduOrientation_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 84),
    _PduOrientation_Type()
)
pduOrientation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOrientation.setStatus("current")


class _PduUptime_Type(Unsigned32):
    """Custom type pduUptime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PduUptime_Type.__name__ = "Unsigned32"
_PduUptime_Object = MibTableColumn
pduUptime = _PduUptime_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 85),
    _PduUptime_Type()
)
pduUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUptime.setStatus("current")
_TripCauseOutletHandling_Type = TripCauseOutletHandlingEnumeration
_TripCauseOutletHandling_Object = MibTableColumn
tripCauseOutletHandling = _TripCauseOutletHandling_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 2, 1, 86),
    _TripCauseOutletHandling_Type()
)
tripCauseOutletHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tripCauseOutletHandling.setStatus("current")
_ControllerConfigurationTable_Object = MibTable
controllerConfigurationTable = _ControllerConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 3)
)
if mibBuilder.loadTexts:
    controllerConfigurationTable.setStatus("current")
_ControllerConfigurationEntry_Object = MibTableRow
controllerConfigurationEntry = _ControllerConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 3, 1)
)
controllerConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "boardType"),
    (0, "PDU2-MIB", "boardIndex"),
)
if mibBuilder.loadTexts:
    controllerConfigurationEntry.setStatus("current")
_BoardType_Type = BoardTypeEnumeration
_BoardType_Object = MibTableColumn
boardType = _BoardType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 3, 1, 1),
    _BoardType_Type()
)
boardType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    boardType.setStatus("current")


class _BoardIndex_Type(Integer32):
    """Custom type boardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_BoardIndex_Type.__name__ = "Integer32"
_BoardIndex_Object = MibTableColumn
boardIndex = _BoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 3, 1, 2),
    _BoardIndex_Type()
)
boardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    boardIndex.setStatus("current")
_BoardVersion_Type = DisplayString
_BoardVersion_Object = MibTableColumn
boardVersion = _BoardVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 3, 1, 4),
    _BoardVersion_Type()
)
boardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardVersion.setStatus("current")
_BoardFirmwareVersion_Type = DisplayString
_BoardFirmwareVersion_Object = MibTableColumn
boardFirmwareVersion = _BoardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 3, 1, 6),
    _BoardFirmwareVersion_Type()
)
boardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardFirmwareVersion.setStatus("current")
_BoardFirmwareTimeStamp_Type = Unsigned32
_BoardFirmwareTimeStamp_Object = MibTableColumn
boardFirmwareTimeStamp = _BoardFirmwareTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 3, 1, 8),
    _BoardFirmwareTimeStamp_Type()
)
boardFirmwareTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardFirmwareTimeStamp.setStatus("current")
_LogConfigurationTable_Object = MibTable
logConfigurationTable = _LogConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 4)
)
if mibBuilder.loadTexts:
    logConfigurationTable.setStatus("current")
_LogConfigurationEntry_Object = MibTableRow
logConfigurationEntry = _LogConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 4, 1)
)
logConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
)
if mibBuilder.loadTexts:
    logConfigurationEntry.setStatus("current")
_DataLogging_Type = TruthValue
_DataLogging_Object = MibTableColumn
dataLogging = _DataLogging_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 4, 1, 1),
    _DataLogging_Type()
)
dataLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataLogging.setStatus("current")
_MeasurementPeriod_Type = Integer32
_MeasurementPeriod_Object = MibTableColumn
measurementPeriod = _MeasurementPeriod_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 4, 1, 2),
    _MeasurementPeriod_Type()
)
measurementPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementPeriod.setStatus("current")


class _MeasurementsPerLogEntry_Type(Integer32):
    """Custom type measurementsPerLogEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_MeasurementsPerLogEntry_Type.__name__ = "Integer32"
_MeasurementsPerLogEntry_Object = MibTableColumn
measurementsPerLogEntry = _MeasurementsPerLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 4, 1, 3),
    _MeasurementsPerLogEntry_Type()
)
measurementsPerLogEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measurementsPerLogEntry.setStatus("current")


class _LogSize_Type(Integer32):
    """Custom type logSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 20000),
    )


_LogSize_Type.__name__ = "Integer32"
_LogSize_Object = MibTableColumn
logSize = _LogSize_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 4, 1, 4),
    _LogSize_Type()
)
logSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logSize.setStatus("current")
_DataLoggingEnableForAllSensors_Type = TruthValue
_DataLoggingEnableForAllSensors_Object = MibTableColumn
dataLoggingEnableForAllSensors = _DataLoggingEnableForAllSensors_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 4, 1, 5),
    _DataLoggingEnableForAllSensors_Type()
)
dataLoggingEnableForAllSensors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataLoggingEnableForAllSensors.setStatus("current")
_UnitSensorConfigurationTable_Object = MibTable
unitSensorConfigurationTable = _UnitSensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5)
)
if mibBuilder.loadTexts:
    unitSensorConfigurationTable.setStatus("current")
_UnitSensorConfigurationEntry_Object = MibTableRow
unitSensorConfigurationEntry = _UnitSensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1)
)
unitSensorConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    unitSensorConfigurationEntry.setStatus("current")
_SensorType_Type = SensorTypeEnumeration
_SensorType_Object = MibTableColumn
sensorType = _SensorType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 1),
    _SensorType_Type()
)
sensorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensorType.setStatus("current")
_UnitSensorLogAvailable_Type = TruthValue
_UnitSensorLogAvailable_Object = MibTableColumn
unitSensorLogAvailable = _UnitSensorLogAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 4),
    _UnitSensorLogAvailable_Type()
)
unitSensorLogAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSensorLogAvailable.setStatus("current")
_UnitSensorUnits_Type = SensorUnitsEnumeration
_UnitSensorUnits_Object = MibTableColumn
unitSensorUnits = _UnitSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 6),
    _UnitSensorUnits_Type()
)
unitSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSensorUnits.setStatus("current")
_UnitSensorDecimalDigits_Type = Unsigned32
_UnitSensorDecimalDigits_Object = MibTableColumn
unitSensorDecimalDigits = _UnitSensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 7),
    _UnitSensorDecimalDigits_Type()
)
unitSensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSensorDecimalDigits.setStatus("current")
_UnitSensorAccuracy_Type = HundredthsOfAPercentage
_UnitSensorAccuracy_Object = MibTableColumn
unitSensorAccuracy = _UnitSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 8),
    _UnitSensorAccuracy_Type()
)
unitSensorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSensorAccuracy.setStatus("deprecated")
_UnitSensorResolution_Type = Unsigned32
_UnitSensorResolution_Object = MibTableColumn
unitSensorResolution = _UnitSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 9),
    _UnitSensorResolution_Type()
)
unitSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSensorResolution.setStatus("current")
_UnitSensorTolerance_Type = Unsigned32
_UnitSensorTolerance_Object = MibTableColumn
unitSensorTolerance = _UnitSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 10),
    _UnitSensorTolerance_Type()
)
unitSensorTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSensorTolerance.setStatus("deprecated")
_UnitSensorMaximum_Type = Unsigned32
_UnitSensorMaximum_Object = MibTableColumn
unitSensorMaximum = _UnitSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 11),
    _UnitSensorMaximum_Type()
)
unitSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSensorMaximum.setStatus("current")
_UnitSensorMinimum_Type = Unsigned32
_UnitSensorMinimum_Object = MibTableColumn
unitSensorMinimum = _UnitSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 12),
    _UnitSensorMinimum_Type()
)
unitSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSensorMinimum.setStatus("current")
_UnitSensorHysteresis_Type = Unsigned32
_UnitSensorHysteresis_Object = MibTableColumn
unitSensorHysteresis = _UnitSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 13),
    _UnitSensorHysteresis_Type()
)
unitSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSensorHysteresis.setStatus("current")


class _UnitSensorStateChangeDelay_Type(Unsigned32):
    """Custom type unitSensorStateChangeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_UnitSensorStateChangeDelay_Type.__name__ = "Unsigned32"
_UnitSensorStateChangeDelay_Object = MibTableColumn
unitSensorStateChangeDelay = _UnitSensorStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 14),
    _UnitSensorStateChangeDelay_Type()
)
unitSensorStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSensorStateChangeDelay.setStatus("current")
_UnitSensorLowerCriticalThreshold_Type = Unsigned32
_UnitSensorLowerCriticalThreshold_Object = MibTableColumn
unitSensorLowerCriticalThreshold = _UnitSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 21),
    _UnitSensorLowerCriticalThreshold_Type()
)
unitSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSensorLowerCriticalThreshold.setStatus("current")
_UnitSensorLowerWarningThreshold_Type = Unsigned32
_UnitSensorLowerWarningThreshold_Object = MibTableColumn
unitSensorLowerWarningThreshold = _UnitSensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 22),
    _UnitSensorLowerWarningThreshold_Type()
)
unitSensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSensorLowerWarningThreshold.setStatus("current")
_UnitSensorUpperCriticalThreshold_Type = Unsigned32
_UnitSensorUpperCriticalThreshold_Object = MibTableColumn
unitSensorUpperCriticalThreshold = _UnitSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 23),
    _UnitSensorUpperCriticalThreshold_Type()
)
unitSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSensorUpperCriticalThreshold.setStatus("current")
_UnitSensorUpperWarningThreshold_Type = Unsigned32
_UnitSensorUpperWarningThreshold_Object = MibTableColumn
unitSensorUpperWarningThreshold = _UnitSensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 24),
    _UnitSensorUpperWarningThreshold_Type()
)
unitSensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSensorUpperWarningThreshold.setStatus("current")


class _UnitSensorEnabledThresholds_Type(Bits):
    """Custom type unitSensorEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_UnitSensorEnabledThresholds_Type.__name__ = "Bits"
_UnitSensorEnabledThresholds_Object = MibTableColumn
unitSensorEnabledThresholds = _UnitSensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 25),
    _UnitSensorEnabledThresholds_Type()
)
unitSensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSensorEnabledThresholds.setStatus("current")
_UnitSensorSignedMaximum_Type = Integer32
_UnitSensorSignedMaximum_Object = MibTableColumn
unitSensorSignedMaximum = _UnitSensorSignedMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 26),
    _UnitSensorSignedMaximum_Type()
)
unitSensorSignedMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSensorSignedMaximum.setStatus("current")
_UnitSensorSignedMinimum_Type = Integer32
_UnitSensorSignedMinimum_Object = MibTableColumn
unitSensorSignedMinimum = _UnitSensorSignedMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 27),
    _UnitSensorSignedMinimum_Type()
)
unitSensorSignedMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSensorSignedMinimum.setStatus("current")
_UnitSensorSignedLowerCriticalThreshold_Type = Integer32
_UnitSensorSignedLowerCriticalThreshold_Object = MibTableColumn
unitSensorSignedLowerCriticalThreshold = _UnitSensorSignedLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 28),
    _UnitSensorSignedLowerCriticalThreshold_Type()
)
unitSensorSignedLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSensorSignedLowerCriticalThreshold.setStatus("current")
_UnitSensorSignedLowerWarningThreshold_Type = Integer32
_UnitSensorSignedLowerWarningThreshold_Object = MibTableColumn
unitSensorSignedLowerWarningThreshold = _UnitSensorSignedLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 29),
    _UnitSensorSignedLowerWarningThreshold_Type()
)
unitSensorSignedLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSensorSignedLowerWarningThreshold.setStatus("current")
_UnitSensorSignedUpperCriticalThreshold_Type = Integer32
_UnitSensorSignedUpperCriticalThreshold_Object = MibTableColumn
unitSensorSignedUpperCriticalThreshold = _UnitSensorSignedUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 30),
    _UnitSensorSignedUpperCriticalThreshold_Type()
)
unitSensorSignedUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSensorSignedUpperCriticalThreshold.setStatus("current")
_UnitSensorSignedUpperWarningThreshold_Type = Integer32
_UnitSensorSignedUpperWarningThreshold_Object = MibTableColumn
unitSensorSignedUpperWarningThreshold = _UnitSensorSignedUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 5, 1, 31),
    _UnitSensorSignedUpperWarningThreshold_Type()
)
unitSensorSignedUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSensorSignedUpperWarningThreshold.setStatus("current")
_ActiveDNSServerTable_Object = MibTable
activeDNSServerTable = _ActiveDNSServerTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 6)
)
if mibBuilder.loadTexts:
    activeDNSServerTable.setStatus("current")
_ActiveDNSServerEntry_Object = MibTableRow
activeDNSServerEntry = _ActiveDNSServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 6, 1)
)
activeDNSServerEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "activeDNSServerIndex"),
)
if mibBuilder.loadTexts:
    activeDNSServerEntry.setStatus("current")


class _ActiveDNSServerIndex_Type(Integer32):
    """Custom type activeDNSServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ActiveDNSServerIndex_Type.__name__ = "Integer32"
_ActiveDNSServerIndex_Object = MibTableColumn
activeDNSServerIndex = _ActiveDNSServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 6, 1, 2),
    _ActiveDNSServerIndex_Type()
)
activeDNSServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    activeDNSServerIndex.setStatus("current")
_ActiveDNSServerAddressType_Type = InetAddressType
_ActiveDNSServerAddressType_Object = MibTableColumn
activeDNSServerAddressType = _ActiveDNSServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 6, 1, 3),
    _ActiveDNSServerAddressType_Type()
)
activeDNSServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeDNSServerAddressType.setStatus("current")
_ActiveDNSServerAddress_Type = InetAddress
_ActiveDNSServerAddress_Object = MibTableColumn
activeDNSServerAddress = _ActiveDNSServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 6, 1, 4),
    _ActiveDNSServerAddress_Type()
)
activeDNSServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeDNSServerAddress.setStatus("current")
_ActiveDNSServerAddressSource_Type = AddressSourceEnumeration
_ActiveDNSServerAddressSource_Object = MibTableColumn
activeDNSServerAddressSource = _ActiveDNSServerAddressSource_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 6, 1, 5),
    _ActiveDNSServerAddressSource_Type()
)
activeDNSServerAddressSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeDNSServerAddressSource.setStatus("deprecated")
_ActiveNTPServerTable_Object = MibTable
activeNTPServerTable = _ActiveNTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 7)
)
if mibBuilder.loadTexts:
    activeNTPServerTable.setStatus("current")
_ActiveNTPServerEntry_Object = MibTableRow
activeNTPServerEntry = _ActiveNTPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 7, 1)
)
activeNTPServerEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "activeNTPServerIndex"),
)
if mibBuilder.loadTexts:
    activeNTPServerEntry.setStatus("current")


class _ActiveNTPServerIndex_Type(Integer32):
    """Custom type activeNTPServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ActiveNTPServerIndex_Type.__name__ = "Integer32"
_ActiveNTPServerIndex_Object = MibTableColumn
activeNTPServerIndex = _ActiveNTPServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 7, 1, 2),
    _ActiveNTPServerIndex_Type()
)
activeNTPServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    activeNTPServerIndex.setStatus("current")
_ActiveNTPServerAddressType_Type = InetAddressType
_ActiveNTPServerAddressType_Object = MibTableColumn
activeNTPServerAddressType = _ActiveNTPServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 7, 1, 3),
    _ActiveNTPServerAddressType_Type()
)
activeNTPServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeNTPServerAddressType.setStatus("current")
_ActiveNTPServerAddress_Type = InetAddress
_ActiveNTPServerAddress_Object = MibTableColumn
activeNTPServerAddress = _ActiveNTPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 7, 1, 4),
    _ActiveNTPServerAddress_Type()
)
activeNTPServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeNTPServerAddress.setStatus("current")
_ActiveNTPServerAddressSource_Type = AddressSourceEnumeration
_ActiveNTPServerAddressSource_Object = MibTableColumn
activeNTPServerAddressSource = _ActiveNTPServerAddressSource_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 2, 7, 1, 5),
    _ActiveNTPServerAddressSource_Type()
)
activeNTPServerAddressSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeNTPServerAddressSource.setStatus("deprecated")
_Inlets_ObjectIdentity = ObjectIdentity
inlets = _Inlets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3)
)
_InletConfigurationTable_Object = MibTable
inletConfigurationTable = _InletConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3)
)
if mibBuilder.loadTexts:
    inletConfigurationTable.setStatus("current")
_InletConfigurationEntry_Object = MibTableRow
inletConfigurationEntry = _InletConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1)
)
inletConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
)
if mibBuilder.loadTexts:
    inletConfigurationEntry.setStatus("current")


class _InletId_Type(Integer32):
    """Custom type inletId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_InletId_Type.__name__ = "Integer32"
_InletId_Object = MibTableColumn
inletId = _InletId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 1),
    _InletId_Type()
)
inletId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inletId.setStatus("current")
_InletLabel_Type = DisplayString
_InletLabel_Object = MibTableColumn
inletLabel = _InletLabel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 2),
    _InletLabel_Type()
)
inletLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLabel.setStatus("current")
_InletName_Type = DisplayString
_InletName_Object = MibTableColumn
inletName = _InletName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 3),
    _InletName_Type()
)
inletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletName.setStatus("current")
_InletPlug_Type = PlugTypeEnumeration
_InletPlug_Object = MibTableColumn
inletPlug = _InletPlug_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 4),
    _InletPlug_Type()
)
inletPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPlug.setStatus("deprecated")


class _InletPoleCount_Type(Integer32):
    """Custom type inletPoleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_InletPoleCount_Type.__name__ = "Integer32"
_InletPoleCount_Object = MibTableColumn
inletPoleCount = _InletPoleCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 5),
    _InletPoleCount_Type()
)
inletPoleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleCount.setStatus("current")
_InletRatedVoltage_Type = DisplayString
_InletRatedVoltage_Object = MibTableColumn
inletRatedVoltage = _InletRatedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 6),
    _InletRatedVoltage_Type()
)
inletRatedVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletRatedVoltage.setStatus("current")
_InletRatedCurrent_Type = DisplayString
_InletRatedCurrent_Object = MibTableColumn
inletRatedCurrent = _InletRatedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 7),
    _InletRatedCurrent_Type()
)
inletRatedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletRatedCurrent.setStatus("current")
_InletRatedFrequency_Type = DisplayString
_InletRatedFrequency_Object = MibTableColumn
inletRatedFrequency = _InletRatedFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 8),
    _InletRatedFrequency_Type()
)
inletRatedFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletRatedFrequency.setStatus("deprecated")
_InletRatedVA_Type = DisplayString
_InletRatedVA_Object = MibTableColumn
inletRatedVA = _InletRatedVA_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 9),
    _InletRatedVA_Type()
)
inletRatedVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletRatedVA.setStatus("deprecated")


class _InletDeviceCapabilities_Type(Bits):
    """Custom type inletDeviceCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("rmsCurrent", 0),
          ("peakCurrent", 1),
          ("unbalancedCurrent", 2),
          ("rmsVoltage", 3),
          ("activePower", 4),
          ("apparentPower", 5),
          ("powerFactor", 6),
          ("activeEnergy", 7),
          ("apparentEnergy", 8),
          ("surgeProtectorStatus", 21),
          ("frequency", 22),
          ("phaseAngle", 23),
          ("residualCurrent", 25),
          ("rcmState", 26),
          ("reactivePower", 28),
          ("powerQuality", 31),
          ("displacementPowerFactor", 34),
          ("residualDcCurrent", 35),
          ("crestFactor", 50),
          ("activePowerDemand", 53),
          ("residualAcCurrent", 54),
          ("voltageThd", 56),
          ("currentThd", 57),
          ("unbalancedVoltage", 59),
          ("unbalancedLineLineCurrent", 60),
          ("unbalancedLineLineVoltage", 61))
    )

_InletDeviceCapabilities_Type.__name__ = "Bits"
_InletDeviceCapabilities_Object = MibTableColumn
inletDeviceCapabilities = _InletDeviceCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 10),
    _InletDeviceCapabilities_Type()
)
inletDeviceCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletDeviceCapabilities.setStatus("current")


class _InletPoleCapabilities_Type(Bits):
    """Custom type inletPoleCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("rmsCurrent", 0),
          ("peakCurrent", 1),
          ("rmsVoltage", 3),
          ("activePower", 4),
          ("apparentPower", 5),
          ("powerFactor", 6),
          ("activeEnergy", 7),
          ("apparentEnergy", 8),
          ("phaseAngle", 23),
          ("rmsVoltageLN", 24),
          ("residualCurrent", 25),
          ("rcmState", 26),
          ("reactivePower", 28),
          ("displacementPowerFactor", 34),
          ("residualDcCurrent", 35),
          ("crestFactor", 50),
          ("residualAcCurrent", 54),
          ("voltageThd", 56),
          ("currentThd", 57))
    )

_InletPoleCapabilities_Type.__name__ = "Bits"
_InletPoleCapabilities_Object = MibTableColumn
inletPoleCapabilities = _InletPoleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 11),
    _InletPoleCapabilities_Type()
)
inletPoleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleCapabilities.setStatus("current")
_InletPlugDescriptor_Type = DisplayString
_InletPlugDescriptor_Object = MibTableColumn
inletPlugDescriptor = _InletPlugDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 12),
    _InletPlugDescriptor_Type()
)
inletPlugDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPlugDescriptor.setStatus("current")
_InletEnableState_Type = TruthValue
_InletEnableState_Object = MibTableColumn
inletEnableState = _InletEnableState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 13),
    _InletEnableState_Type()
)
inletEnableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletEnableState.setStatus("current")
_InletRCMResidualOperatingCurrent_Type = Unsigned32
_InletRCMResidualOperatingCurrent_Object = MibTableColumn
inletRCMResidualOperatingCurrent = _InletRCMResidualOperatingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 14),
    _InletRCMResidualOperatingCurrent_Type()
)
inletRCMResidualOperatingCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletRCMResidualOperatingCurrent.setStatus("obsolete")
_InletIsDC_Type = TruthValue
_InletIsDC_Object = MibTableColumn
inletIsDC = _InletIsDC_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 15),
    _InletIsDC_Type()
)
inletIsDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletIsDC.setStatus("current")


class _InletLinePairCount_Type(Integer32):
    """Custom type inletLinePairCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_InletLinePairCount_Type.__name__ = "Integer32"
_InletLinePairCount_Object = MibTableColumn
inletLinePairCount = _InletLinePairCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 16),
    _InletLinePairCount_Type()
)
inletLinePairCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLinePairCount.setStatus("current")


class _InletLinePairCapabilities_Type(Bits):
    """Custom type inletLinePairCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("rmsCurrent", 0),
          ("peakCurrent", 1),
          ("rmsVoltage", 3),
          ("activePower", 4),
          ("apparentPower", 5),
          ("powerFactor", 6),
          ("activeEnergy", 7),
          ("apparentEnergy", 8),
          ("phaseAngle", 23),
          ("reactivePower", 28),
          ("displacementPowerFactor", 34),
          ("crestFactor", 50),
          ("voltageThd", 56),
          ("currentThd", 57))
    )

_InletLinePairCapabilities_Type.__name__ = "Bits"
_InletLinePairCapabilities_Object = MibTableColumn
inletLinePairCapabilities = _InletLinePairCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 3, 1, 17),
    _InletLinePairCapabilities_Type()
)
inletLinePairCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLinePairCapabilities.setStatus("current")
_InletSensorConfigurationTable_Object = MibTable
inletSensorConfigurationTable = _InletSensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4)
)
if mibBuilder.loadTexts:
    inletSensorConfigurationTable.setStatus("current")
_InletSensorConfigurationEntry_Object = MibTableRow
inletSensorConfigurationEntry = _InletSensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1)
)
inletSensorConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    inletSensorConfigurationEntry.setStatus("current")
_InletSensorLogAvailable_Type = TruthValue
_InletSensorLogAvailable_Object = MibTableColumn
inletSensorLogAvailable = _InletSensorLogAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 4),
    _InletSensorLogAvailable_Type()
)
inletSensorLogAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletSensorLogAvailable.setStatus("current")
_InletSensorUnits_Type = SensorUnitsEnumeration
_InletSensorUnits_Object = MibTableColumn
inletSensorUnits = _InletSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 6),
    _InletSensorUnits_Type()
)
inletSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSensorUnits.setStatus("current")
_InletSensorDecimalDigits_Type = Unsigned32
_InletSensorDecimalDigits_Object = MibTableColumn
inletSensorDecimalDigits = _InletSensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 7),
    _InletSensorDecimalDigits_Type()
)
inletSensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSensorDecimalDigits.setStatus("current")
_InletSensorAccuracy_Type = HundredthsOfAPercentage
_InletSensorAccuracy_Object = MibTableColumn
inletSensorAccuracy = _InletSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 8),
    _InletSensorAccuracy_Type()
)
inletSensorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSensorAccuracy.setStatus("deprecated")
_InletSensorResolution_Type = Unsigned32
_InletSensorResolution_Object = MibTableColumn
inletSensorResolution = _InletSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 9),
    _InletSensorResolution_Type()
)
inletSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSensorResolution.setStatus("current")
_InletSensorTolerance_Type = Unsigned32
_InletSensorTolerance_Object = MibTableColumn
inletSensorTolerance = _InletSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 10),
    _InletSensorTolerance_Type()
)
inletSensorTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSensorTolerance.setStatus("deprecated")
_InletSensorMaximum_Type = Unsigned32
_InletSensorMaximum_Object = MibTableColumn
inletSensorMaximum = _InletSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 11),
    _InletSensorMaximum_Type()
)
inletSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSensorMaximum.setStatus("current")
_InletSensorMinimum_Type = Unsigned32
_InletSensorMinimum_Object = MibTableColumn
inletSensorMinimum = _InletSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 12),
    _InletSensorMinimum_Type()
)
inletSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSensorMinimum.setStatus("current")
_InletSensorHysteresis_Type = Unsigned32
_InletSensorHysteresis_Object = MibTableColumn
inletSensorHysteresis = _InletSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 13),
    _InletSensorHysteresis_Type()
)
inletSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletSensorHysteresis.setStatus("current")


class _InletSensorStateChangeDelay_Type(Unsigned32):
    """Custom type inletSensorStateChangeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_InletSensorStateChangeDelay_Type.__name__ = "Unsigned32"
_InletSensorStateChangeDelay_Object = MibTableColumn
inletSensorStateChangeDelay = _InletSensorStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 14),
    _InletSensorStateChangeDelay_Type()
)
inletSensorStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletSensorStateChangeDelay.setStatus("current")
_InletSensorLowerCriticalThreshold_Type = Unsigned32
_InletSensorLowerCriticalThreshold_Object = MibTableColumn
inletSensorLowerCriticalThreshold = _InletSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 21),
    _InletSensorLowerCriticalThreshold_Type()
)
inletSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletSensorLowerCriticalThreshold.setStatus("current")
_InletSensorLowerWarningThreshold_Type = Unsigned32
_InletSensorLowerWarningThreshold_Object = MibTableColumn
inletSensorLowerWarningThreshold = _InletSensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 22),
    _InletSensorLowerWarningThreshold_Type()
)
inletSensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletSensorLowerWarningThreshold.setStatus("current")
_InletSensorUpperCriticalThreshold_Type = Unsigned32
_InletSensorUpperCriticalThreshold_Object = MibTableColumn
inletSensorUpperCriticalThreshold = _InletSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 23),
    _InletSensorUpperCriticalThreshold_Type()
)
inletSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletSensorUpperCriticalThreshold.setStatus("current")
_InletSensorUpperWarningThreshold_Type = Unsigned32
_InletSensorUpperWarningThreshold_Object = MibTableColumn
inletSensorUpperWarningThreshold = _InletSensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 24),
    _InletSensorUpperWarningThreshold_Type()
)
inletSensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletSensorUpperWarningThreshold.setStatus("current")


class _InletSensorEnabledThresholds_Type(Bits):
    """Custom type inletSensorEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_InletSensorEnabledThresholds_Type.__name__ = "Bits"
_InletSensorEnabledThresholds_Object = MibTableColumn
inletSensorEnabledThresholds = _InletSensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 25),
    _InletSensorEnabledThresholds_Type()
)
inletSensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletSensorEnabledThresholds.setStatus("current")
_InletSensorSignedMaximum_Type = Integer32
_InletSensorSignedMaximum_Object = MibTableColumn
inletSensorSignedMaximum = _InletSensorSignedMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 26),
    _InletSensorSignedMaximum_Type()
)
inletSensorSignedMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSensorSignedMaximum.setStatus("current")
_InletSensorSignedMinimum_Type = Integer32
_InletSensorSignedMinimum_Object = MibTableColumn
inletSensorSignedMinimum = _InletSensorSignedMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 27),
    _InletSensorSignedMinimum_Type()
)
inletSensorSignedMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSensorSignedMinimum.setStatus("current")
_InletSensorSignedLowerCriticalThreshold_Type = Integer32
_InletSensorSignedLowerCriticalThreshold_Object = MibTableColumn
inletSensorSignedLowerCriticalThreshold = _InletSensorSignedLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 28),
    _InletSensorSignedLowerCriticalThreshold_Type()
)
inletSensorSignedLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletSensorSignedLowerCriticalThreshold.setStatus("current")
_InletSensorSignedLowerWarningThreshold_Type = Integer32
_InletSensorSignedLowerWarningThreshold_Object = MibTableColumn
inletSensorSignedLowerWarningThreshold = _InletSensorSignedLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 29),
    _InletSensorSignedLowerWarningThreshold_Type()
)
inletSensorSignedLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletSensorSignedLowerWarningThreshold.setStatus("current")
_InletSensorSignedUpperCriticalThreshold_Type = Integer32
_InletSensorSignedUpperCriticalThreshold_Object = MibTableColumn
inletSensorSignedUpperCriticalThreshold = _InletSensorSignedUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 30),
    _InletSensorSignedUpperCriticalThreshold_Type()
)
inletSensorSignedUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletSensorSignedUpperCriticalThreshold.setStatus("current")
_InletSensorSignedUpperWarningThreshold_Type = Integer32
_InletSensorSignedUpperWarningThreshold_Object = MibTableColumn
inletSensorSignedUpperWarningThreshold = _InletSensorSignedUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 4, 1, 31),
    _InletSensorSignedUpperWarningThreshold_Type()
)
inletSensorSignedUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletSensorSignedUpperWarningThreshold.setStatus("current")
_InletPoleConfigurationTable_Object = MibTable
inletPoleConfigurationTable = _InletPoleConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 5)
)
if mibBuilder.loadTexts:
    inletPoleConfigurationTable.setStatus("current")
_InletPoleConfigurationEntry_Object = MibTableRow
inletPoleConfigurationEntry = _InletPoleConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 5, 1)
)
inletPoleConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
    (0, "PDU2-MIB", "inletPoleIndex"),
)
if mibBuilder.loadTexts:
    inletPoleConfigurationEntry.setStatus("current")
_InletPoleLine_Type = LineEnumeration
_InletPoleLine_Object = MibTableColumn
inletPoleLine = _InletPoleLine_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 5, 1, 1),
    _InletPoleLine_Type()
)
inletPoleLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleLine.setStatus("current")
_InletPoleNode_Type = Integer32
_InletPoleNode_Object = MibTableColumn
inletPoleNode = _InletPoleNode_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 5, 1, 2),
    _InletPoleNode_Type()
)
inletPoleNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleNode.setStatus("current")
_InletPoleSensorConfigurationTable_Object = MibTable
inletPoleSensorConfigurationTable = _InletPoleSensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6)
)
if mibBuilder.loadTexts:
    inletPoleSensorConfigurationTable.setStatus("current")
_InletPoleSensorConfigurationEntry_Object = MibTableRow
inletPoleSensorConfigurationEntry = _InletPoleSensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1)
)
inletPoleSensorConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
    (0, "PDU2-MIB", "inletPoleIndex"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    inletPoleSensorConfigurationEntry.setStatus("current")


class _InletPoleIndex_Type(Integer32):
    """Custom type inletPoleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_InletPoleIndex_Type.__name__ = "Integer32"
_InletPoleIndex_Object = MibTableColumn
inletPoleIndex = _InletPoleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 1),
    _InletPoleIndex_Type()
)
inletPoleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inletPoleIndex.setStatus("current")
_InletPoleSensorLogAvailable_Type = TruthValue
_InletPoleSensorLogAvailable_Object = MibTableColumn
inletPoleSensorLogAvailable = _InletPoleSensorLogAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 4),
    _InletPoleSensorLogAvailable_Type()
)
inletPoleSensorLogAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletPoleSensorLogAvailable.setStatus("current")
_InletPoleSensorUnits_Type = SensorUnitsEnumeration
_InletPoleSensorUnits_Object = MibTableColumn
inletPoleSensorUnits = _InletPoleSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 6),
    _InletPoleSensorUnits_Type()
)
inletPoleSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleSensorUnits.setStatus("current")
_InletPoleSensorDecimalDigits_Type = Unsigned32
_InletPoleSensorDecimalDigits_Object = MibTableColumn
inletPoleSensorDecimalDigits = _InletPoleSensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 7),
    _InletPoleSensorDecimalDigits_Type()
)
inletPoleSensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleSensorDecimalDigits.setStatus("current")
_InletPoleSensorAccuracy_Type = HundredthsOfAPercentage
_InletPoleSensorAccuracy_Object = MibTableColumn
inletPoleSensorAccuracy = _InletPoleSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 8),
    _InletPoleSensorAccuracy_Type()
)
inletPoleSensorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleSensorAccuracy.setStatus("deprecated")
_InletPoleSensorResolution_Type = Unsigned32
_InletPoleSensorResolution_Object = MibTableColumn
inletPoleSensorResolution = _InletPoleSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 9),
    _InletPoleSensorResolution_Type()
)
inletPoleSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleSensorResolution.setStatus("current")
_InletPoleSensorTolerance_Type = Unsigned32
_InletPoleSensorTolerance_Object = MibTableColumn
inletPoleSensorTolerance = _InletPoleSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 10),
    _InletPoleSensorTolerance_Type()
)
inletPoleSensorTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleSensorTolerance.setStatus("deprecated")
_InletPoleSensorMaximum_Type = Unsigned32
_InletPoleSensorMaximum_Object = MibTableColumn
inletPoleSensorMaximum = _InletPoleSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 11),
    _InletPoleSensorMaximum_Type()
)
inletPoleSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleSensorMaximum.setStatus("current")
_InletPoleSensorMinimum_Type = Unsigned32
_InletPoleSensorMinimum_Object = MibTableColumn
inletPoleSensorMinimum = _InletPoleSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 12),
    _InletPoleSensorMinimum_Type()
)
inletPoleSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleSensorMinimum.setStatus("current")
_InletPoleSensorHysteresis_Type = Unsigned32
_InletPoleSensorHysteresis_Object = MibTableColumn
inletPoleSensorHysteresis = _InletPoleSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 13),
    _InletPoleSensorHysteresis_Type()
)
inletPoleSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletPoleSensorHysteresis.setStatus("current")


class _InletPoleSensorStateChangeDelay_Type(Unsigned32):
    """Custom type inletPoleSensorStateChangeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_InletPoleSensorStateChangeDelay_Type.__name__ = "Unsigned32"
_InletPoleSensorStateChangeDelay_Object = MibTableColumn
inletPoleSensorStateChangeDelay = _InletPoleSensorStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 14),
    _InletPoleSensorStateChangeDelay_Type()
)
inletPoleSensorStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletPoleSensorStateChangeDelay.setStatus("current")
_InletPoleSensorLowerCriticalThreshold_Type = Unsigned32
_InletPoleSensorLowerCriticalThreshold_Object = MibTableColumn
inletPoleSensorLowerCriticalThreshold = _InletPoleSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 21),
    _InletPoleSensorLowerCriticalThreshold_Type()
)
inletPoleSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletPoleSensorLowerCriticalThreshold.setStatus("current")
_InletPoleSensorLowerWarningThreshold_Type = Unsigned32
_InletPoleSensorLowerWarningThreshold_Object = MibTableColumn
inletPoleSensorLowerWarningThreshold = _InletPoleSensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 22),
    _InletPoleSensorLowerWarningThreshold_Type()
)
inletPoleSensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletPoleSensorLowerWarningThreshold.setStatus("current")
_InletPoleSensorUpperCriticalThreshold_Type = Unsigned32
_InletPoleSensorUpperCriticalThreshold_Object = MibTableColumn
inletPoleSensorUpperCriticalThreshold = _InletPoleSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 23),
    _InletPoleSensorUpperCriticalThreshold_Type()
)
inletPoleSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletPoleSensorUpperCriticalThreshold.setStatus("current")
_InletPoleSensorUpperWarningThreshold_Type = Unsigned32
_InletPoleSensorUpperWarningThreshold_Object = MibTableColumn
inletPoleSensorUpperWarningThreshold = _InletPoleSensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 24),
    _InletPoleSensorUpperWarningThreshold_Type()
)
inletPoleSensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletPoleSensorUpperWarningThreshold.setStatus("current")


class _InletPoleSensorEnabledThresholds_Type(Bits):
    """Custom type inletPoleSensorEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_InletPoleSensorEnabledThresholds_Type.__name__ = "Bits"
_InletPoleSensorEnabledThresholds_Object = MibTableColumn
inletPoleSensorEnabledThresholds = _InletPoleSensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 25),
    _InletPoleSensorEnabledThresholds_Type()
)
inletPoleSensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletPoleSensorEnabledThresholds.setStatus("current")
_InletPoleSensorSignedMaximum_Type = Integer32
_InletPoleSensorSignedMaximum_Object = MibTableColumn
inletPoleSensorSignedMaximum = _InletPoleSensorSignedMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 26),
    _InletPoleSensorSignedMaximum_Type()
)
inletPoleSensorSignedMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleSensorSignedMaximum.setStatus("current")
_InletPoleSensorSignedMinimum_Type = Integer32
_InletPoleSensorSignedMinimum_Object = MibTableColumn
inletPoleSensorSignedMinimum = _InletPoleSensorSignedMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 27),
    _InletPoleSensorSignedMinimum_Type()
)
inletPoleSensorSignedMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletPoleSensorSignedMinimum.setStatus("current")
_InletPoleSensorSignedLowerCriticalThreshold_Type = Integer32
_InletPoleSensorSignedLowerCriticalThreshold_Object = MibTableColumn
inletPoleSensorSignedLowerCriticalThreshold = _InletPoleSensorSignedLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 28),
    _InletPoleSensorSignedLowerCriticalThreshold_Type()
)
inletPoleSensorSignedLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletPoleSensorSignedLowerCriticalThreshold.setStatus("current")
_InletPoleSensorSignedLowerWarningThreshold_Type = Integer32
_InletPoleSensorSignedLowerWarningThreshold_Object = MibTableColumn
inletPoleSensorSignedLowerWarningThreshold = _InletPoleSensorSignedLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 29),
    _InletPoleSensorSignedLowerWarningThreshold_Type()
)
inletPoleSensorSignedLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletPoleSensorSignedLowerWarningThreshold.setStatus("current")
_InletPoleSensorSignedUpperCriticalThreshold_Type = Integer32
_InletPoleSensorSignedUpperCriticalThreshold_Object = MibTableColumn
inletPoleSensorSignedUpperCriticalThreshold = _InletPoleSensorSignedUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 30),
    _InletPoleSensorSignedUpperCriticalThreshold_Type()
)
inletPoleSensorSignedUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletPoleSensorSignedUpperCriticalThreshold.setStatus("current")
_InletPoleSensorSignedUpperWarningThreshold_Type = Integer32
_InletPoleSensorSignedUpperWarningThreshold_Object = MibTableColumn
inletPoleSensorSignedUpperWarningThreshold = _InletPoleSensorSignedUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 6, 1, 31),
    _InletPoleSensorSignedUpperWarningThreshold_Type()
)
inletPoleSensorSignedUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletPoleSensorSignedUpperWarningThreshold.setStatus("current")
_InletLinePairConfigurationTable_Object = MibTable
inletLinePairConfigurationTable = _InletLinePairConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 7)
)
if mibBuilder.loadTexts:
    inletLinePairConfigurationTable.setStatus("current")
_InletLinePairConfigurationEntry_Object = MibTableRow
inletLinePairConfigurationEntry = _InletLinePairConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 7, 1)
)
inletLinePairConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
    (0, "PDU2-MIB", "inletLinePairIndex"),
)
if mibBuilder.loadTexts:
    inletLinePairConfigurationEntry.setStatus("current")


class _InletLinePairIndex_Type(Integer32):
    """Custom type inletLinePairIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_InletLinePairIndex_Type.__name__ = "Integer32"
_InletLinePairIndex_Object = MibTableColumn
inletLinePairIndex = _InletLinePairIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 7, 1, 1),
    _InletLinePairIndex_Type()
)
inletLinePairIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inletLinePairIndex.setStatus("current")
_InletLinePairLeftLine_Type = LineEnumeration
_InletLinePairLeftLine_Object = MibTableColumn
inletLinePairLeftLine = _InletLinePairLeftLine_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 7, 1, 2),
    _InletLinePairLeftLine_Type()
)
inletLinePairLeftLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLinePairLeftLine.setStatus("current")
_InletLinePairRightLine_Type = LineEnumeration
_InletLinePairRightLine_Object = MibTableColumn
inletLinePairRightLine = _InletLinePairRightLine_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 7, 1, 3),
    _InletLinePairRightLine_Type()
)
inletLinePairRightLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLinePairRightLine.setStatus("current")
_InletLinePairLeftNode_Type = Integer32
_InletLinePairLeftNode_Object = MibTableColumn
inletLinePairLeftNode = _InletLinePairLeftNode_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 7, 1, 4),
    _InletLinePairLeftNode_Type()
)
inletLinePairLeftNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLinePairLeftNode.setStatus("current")
_InletLinePairRightNode_Type = Integer32
_InletLinePairRightNode_Object = MibTableColumn
inletLinePairRightNode = _InletLinePairRightNode_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 7, 1, 5),
    _InletLinePairRightNode_Type()
)
inletLinePairRightNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLinePairRightNode.setStatus("current")
_InletLinePairSensorConfigurationTable_Object = MibTable
inletLinePairSensorConfigurationTable = _InletLinePairSensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8)
)
if mibBuilder.loadTexts:
    inletLinePairSensorConfigurationTable.setStatus("current")
_InletLinePairSensorConfigurationEntry_Object = MibTableRow
inletLinePairSensorConfigurationEntry = _InletLinePairSensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1)
)
inletLinePairSensorConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
    (0, "PDU2-MIB", "inletLinePairIndex"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    inletLinePairSensorConfigurationEntry.setStatus("current")
_InletLinePairSensorLogAvailable_Type = TruthValue
_InletLinePairSensorLogAvailable_Object = MibTableColumn
inletLinePairSensorLogAvailable = _InletLinePairSensorLogAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 4),
    _InletLinePairSensorLogAvailable_Type()
)
inletLinePairSensorLogAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletLinePairSensorLogAvailable.setStatus("current")
_InletLinePairSensorUnits_Type = SensorUnitsEnumeration
_InletLinePairSensorUnits_Object = MibTableColumn
inletLinePairSensorUnits = _InletLinePairSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 6),
    _InletLinePairSensorUnits_Type()
)
inletLinePairSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLinePairSensorUnits.setStatus("current")
_InletLinePairSensorDecimalDigits_Type = Unsigned32
_InletLinePairSensorDecimalDigits_Object = MibTableColumn
inletLinePairSensorDecimalDigits = _InletLinePairSensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 7),
    _InletLinePairSensorDecimalDigits_Type()
)
inletLinePairSensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLinePairSensorDecimalDigits.setStatus("current")
_InletLinePairSensorResolution_Type = Unsigned32
_InletLinePairSensorResolution_Object = MibTableColumn
inletLinePairSensorResolution = _InletLinePairSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 9),
    _InletLinePairSensorResolution_Type()
)
inletLinePairSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLinePairSensorResolution.setStatus("current")
_InletLinePairSensorMaximum_Type = Unsigned32
_InletLinePairSensorMaximum_Object = MibTableColumn
inletLinePairSensorMaximum = _InletLinePairSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 11),
    _InletLinePairSensorMaximum_Type()
)
inletLinePairSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLinePairSensorMaximum.setStatus("current")
_InletLinePairSensorMinimum_Type = Unsigned32
_InletLinePairSensorMinimum_Object = MibTableColumn
inletLinePairSensorMinimum = _InletLinePairSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 12),
    _InletLinePairSensorMinimum_Type()
)
inletLinePairSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLinePairSensorMinimum.setStatus("current")
_InletLinePairSensorHysteresis_Type = Unsigned32
_InletLinePairSensorHysteresis_Object = MibTableColumn
inletLinePairSensorHysteresis = _InletLinePairSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 13),
    _InletLinePairSensorHysteresis_Type()
)
inletLinePairSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletLinePairSensorHysteresis.setStatus("current")


class _InletLinePairSensorStateChangeDelay_Type(Unsigned32):
    """Custom type inletLinePairSensorStateChangeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_InletLinePairSensorStateChangeDelay_Type.__name__ = "Unsigned32"
_InletLinePairSensorStateChangeDelay_Object = MibTableColumn
inletLinePairSensorStateChangeDelay = _InletLinePairSensorStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 14),
    _InletLinePairSensorStateChangeDelay_Type()
)
inletLinePairSensorStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletLinePairSensorStateChangeDelay.setStatus("current")
_InletLinePairSensorLowerCriticalThreshold_Type = Unsigned32
_InletLinePairSensorLowerCriticalThreshold_Object = MibTableColumn
inletLinePairSensorLowerCriticalThreshold = _InletLinePairSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 21),
    _InletLinePairSensorLowerCriticalThreshold_Type()
)
inletLinePairSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletLinePairSensorLowerCriticalThreshold.setStatus("current")
_InletLinePairSensorLowerWarningThreshold_Type = Unsigned32
_InletLinePairSensorLowerWarningThreshold_Object = MibTableColumn
inletLinePairSensorLowerWarningThreshold = _InletLinePairSensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 22),
    _InletLinePairSensorLowerWarningThreshold_Type()
)
inletLinePairSensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletLinePairSensorLowerWarningThreshold.setStatus("current")
_InletLinePairSensorUpperCriticalThreshold_Type = Unsigned32
_InletLinePairSensorUpperCriticalThreshold_Object = MibTableColumn
inletLinePairSensorUpperCriticalThreshold = _InletLinePairSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 23),
    _InletLinePairSensorUpperCriticalThreshold_Type()
)
inletLinePairSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletLinePairSensorUpperCriticalThreshold.setStatus("current")
_InletLinePairSensorUpperWarningThreshold_Type = Unsigned32
_InletLinePairSensorUpperWarningThreshold_Object = MibTableColumn
inletLinePairSensorUpperWarningThreshold = _InletLinePairSensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 24),
    _InletLinePairSensorUpperWarningThreshold_Type()
)
inletLinePairSensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletLinePairSensorUpperWarningThreshold.setStatus("current")


class _InletLinePairSensorEnabledThresholds_Type(Bits):
    """Custom type inletLinePairSensorEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_InletLinePairSensorEnabledThresholds_Type.__name__ = "Bits"
_InletLinePairSensorEnabledThresholds_Object = MibTableColumn
inletLinePairSensorEnabledThresholds = _InletLinePairSensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 25),
    _InletLinePairSensorEnabledThresholds_Type()
)
inletLinePairSensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletLinePairSensorEnabledThresholds.setStatus("current")
_InletLinePairSensorSignedMaximum_Type = Integer32
_InletLinePairSensorSignedMaximum_Object = MibTableColumn
inletLinePairSensorSignedMaximum = _InletLinePairSensorSignedMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 26),
    _InletLinePairSensorSignedMaximum_Type()
)
inletLinePairSensorSignedMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLinePairSensorSignedMaximum.setStatus("current")
_InletLinePairSensorSignedMinimum_Type = Integer32
_InletLinePairSensorSignedMinimum_Object = MibTableColumn
inletLinePairSensorSignedMinimum = _InletLinePairSensorSignedMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 27),
    _InletLinePairSensorSignedMinimum_Type()
)
inletLinePairSensorSignedMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletLinePairSensorSignedMinimum.setStatus("current")
_InletLinePairSensorSignedLowerCriticalThreshold_Type = Integer32
_InletLinePairSensorSignedLowerCriticalThreshold_Object = MibTableColumn
inletLinePairSensorSignedLowerCriticalThreshold = _InletLinePairSensorSignedLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 28),
    _InletLinePairSensorSignedLowerCriticalThreshold_Type()
)
inletLinePairSensorSignedLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletLinePairSensorSignedLowerCriticalThreshold.setStatus("current")
_InletLinePairSensorSignedLowerWarningThreshold_Type = Integer32
_InletLinePairSensorSignedLowerWarningThreshold_Object = MibTableColumn
inletLinePairSensorSignedLowerWarningThreshold = _InletLinePairSensorSignedLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 29),
    _InletLinePairSensorSignedLowerWarningThreshold_Type()
)
inletLinePairSensorSignedLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletLinePairSensorSignedLowerWarningThreshold.setStatus("current")
_InletLinePairSensorSignedUpperCriticalThreshold_Type = Integer32
_InletLinePairSensorSignedUpperCriticalThreshold_Object = MibTableColumn
inletLinePairSensorSignedUpperCriticalThreshold = _InletLinePairSensorSignedUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 30),
    _InletLinePairSensorSignedUpperCriticalThreshold_Type()
)
inletLinePairSensorSignedUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletLinePairSensorSignedUpperCriticalThreshold.setStatus("current")
_InletLinePairSensorSignedUpperWarningThreshold_Type = Integer32
_InletLinePairSensorSignedUpperWarningThreshold_Object = MibTableColumn
inletLinePairSensorSignedUpperWarningThreshold = _InletLinePairSensorSignedUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 3, 8, 1, 31),
    _InletLinePairSensorSignedUpperWarningThreshold_Type()
)
inletLinePairSensorSignedUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletLinePairSensorSignedUpperWarningThreshold.setStatus("current")
_OverCurrentProtector_ObjectIdentity = ObjectIdentity
overCurrentProtector = _OverCurrentProtector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4)
)
_OverCurrentProtectorConfigurationTable_Object = MibTable
overCurrentProtectorConfigurationTable = _OverCurrentProtectorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 3)
)
if mibBuilder.loadTexts:
    overCurrentProtectorConfigurationTable.setStatus("current")
_OverCurrentProtectorConfigurationEntry_Object = MibTableRow
overCurrentProtectorConfigurationEntry = _OverCurrentProtectorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 3, 1)
)
overCurrentProtectorConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "overCurrentProtectorIndex"),
)
if mibBuilder.loadTexts:
    overCurrentProtectorConfigurationEntry.setStatus("current")


class _OverCurrentProtectorIndex_Type(Integer32):
    """Custom type overCurrentProtectorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_OverCurrentProtectorIndex_Type.__name__ = "Integer32"
_OverCurrentProtectorIndex_Object = MibTableColumn
overCurrentProtectorIndex = _OverCurrentProtectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 3, 1, 1),
    _OverCurrentProtectorIndex_Type()
)
overCurrentProtectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    overCurrentProtectorIndex.setStatus("current")
_OverCurrentProtectorLabel_Type = DisplayString
_OverCurrentProtectorLabel_Object = MibTableColumn
overCurrentProtectorLabel = _OverCurrentProtectorLabel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 3, 1, 2),
    _OverCurrentProtectorLabel_Type()
)
overCurrentProtectorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorLabel.setStatus("current")
_OverCurrentProtectorName_Type = DisplayString
_OverCurrentProtectorName_Object = MibTableColumn
overCurrentProtectorName = _OverCurrentProtectorName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 3, 1, 3),
    _OverCurrentProtectorName_Type()
)
overCurrentProtectorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overCurrentProtectorName.setStatus("current")
_OverCurrentProtectorType_Type = OverCurrentProtectorTypeEnumeration
_OverCurrentProtectorType_Object = MibTableColumn
overCurrentProtectorType = _OverCurrentProtectorType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 3, 1, 4),
    _OverCurrentProtectorType_Type()
)
overCurrentProtectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorType.setStatus("current")
_OverCurrentProtectorRatedCurrent_Type = DisplayString
_OverCurrentProtectorRatedCurrent_Object = MibTableColumn
overCurrentProtectorRatedCurrent = _OverCurrentProtectorRatedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 3, 1, 5),
    _OverCurrentProtectorRatedCurrent_Type()
)
overCurrentProtectorRatedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorRatedCurrent.setStatus("current")


class _OverCurrentProtectorPoleCount_Type(Integer32):
    """Custom type overCurrentProtectorPoleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_OverCurrentProtectorPoleCount_Type.__name__ = "Integer32"
_OverCurrentProtectorPoleCount_Object = MibTableColumn
overCurrentProtectorPoleCount = _OverCurrentProtectorPoleCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 3, 1, 6),
    _OverCurrentProtectorPoleCount_Type()
)
overCurrentProtectorPoleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorPoleCount.setStatus("current")


class _OverCurrentProtectorCapabilities_Type(Bits):
    """Custom type overCurrentProtectorCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("rmsCurrent", 0),
          ("peakCurrent", 1),
          ("trip", 14),
          ("residualCurrent", 25),
          ("rcmState", 26),
          ("residualDcCurrent", 35),
          ("residualAcCurrent", 54))
    )

_OverCurrentProtectorCapabilities_Type.__name__ = "Bits"
_OverCurrentProtectorCapabilities_Object = MibTableColumn
overCurrentProtectorCapabilities = _OverCurrentProtectorCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 3, 1, 9),
    _OverCurrentProtectorCapabilities_Type()
)
overCurrentProtectorCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorCapabilities.setStatus("current")
_OverCurrentProtectorPowerSource_Type = RowPointer
_OverCurrentProtectorPowerSource_Object = MibTableColumn
overCurrentProtectorPowerSource = _OverCurrentProtectorPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 3, 1, 10),
    _OverCurrentProtectorPowerSource_Type()
)
overCurrentProtectorPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorPowerSource.setStatus("current")
_OverCurrentProtectorSensorConfigurationTable_Object = MibTable
overCurrentProtectorSensorConfigurationTable = _OverCurrentProtectorSensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4)
)
if mibBuilder.loadTexts:
    overCurrentProtectorSensorConfigurationTable.setStatus("current")
_OverCurrentProtectorSensorConfigurationEntry_Object = MibTableRow
overCurrentProtectorSensorConfigurationEntry = _OverCurrentProtectorSensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1)
)
overCurrentProtectorSensorConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "overCurrentProtectorIndex"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    overCurrentProtectorSensorConfigurationEntry.setStatus("current")
_OverCurrentProtectorSensorLogAvailable_Type = TruthValue
_OverCurrentProtectorSensorLogAvailable_Object = MibTableColumn
overCurrentProtectorSensorLogAvailable = _OverCurrentProtectorSensorLogAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 4),
    _OverCurrentProtectorSensorLogAvailable_Type()
)
overCurrentProtectorSensorLogAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorLogAvailable.setStatus("current")
_OverCurrentProtectorSensorUnits_Type = SensorUnitsEnumeration
_OverCurrentProtectorSensorUnits_Object = MibTableColumn
overCurrentProtectorSensorUnits = _OverCurrentProtectorSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 6),
    _OverCurrentProtectorSensorUnits_Type()
)
overCurrentProtectorSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorUnits.setStatus("current")
_OverCurrentProtectorSensorDecimalDigits_Type = Unsigned32
_OverCurrentProtectorSensorDecimalDigits_Object = MibTableColumn
overCurrentProtectorSensorDecimalDigits = _OverCurrentProtectorSensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 7),
    _OverCurrentProtectorSensorDecimalDigits_Type()
)
overCurrentProtectorSensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorDecimalDigits.setStatus("current")
_OverCurrentProtectorSensorAccuracy_Type = HundredthsOfAPercentage
_OverCurrentProtectorSensorAccuracy_Object = MibTableColumn
overCurrentProtectorSensorAccuracy = _OverCurrentProtectorSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 8),
    _OverCurrentProtectorSensorAccuracy_Type()
)
overCurrentProtectorSensorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorAccuracy.setStatus("deprecated")
_OverCurrentProtectorSensorResolution_Type = Unsigned32
_OverCurrentProtectorSensorResolution_Object = MibTableColumn
overCurrentProtectorSensorResolution = _OverCurrentProtectorSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 9),
    _OverCurrentProtectorSensorResolution_Type()
)
overCurrentProtectorSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorResolution.setStatus("current")
_OverCurrentProtectorSensorTolerance_Type = Unsigned32
_OverCurrentProtectorSensorTolerance_Object = MibTableColumn
overCurrentProtectorSensorTolerance = _OverCurrentProtectorSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 10),
    _OverCurrentProtectorSensorTolerance_Type()
)
overCurrentProtectorSensorTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorTolerance.setStatus("deprecated")
_OverCurrentProtectorSensorMaximum_Type = Unsigned32
_OverCurrentProtectorSensorMaximum_Object = MibTableColumn
overCurrentProtectorSensorMaximum = _OverCurrentProtectorSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 11),
    _OverCurrentProtectorSensorMaximum_Type()
)
overCurrentProtectorSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorMaximum.setStatus("current")
_OverCurrentProtectorSensorMinimum_Type = Unsigned32
_OverCurrentProtectorSensorMinimum_Object = MibTableColumn
overCurrentProtectorSensorMinimum = _OverCurrentProtectorSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 12),
    _OverCurrentProtectorSensorMinimum_Type()
)
overCurrentProtectorSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorMinimum.setStatus("current")
_OverCurrentProtectorSensorHysteresis_Type = Unsigned32
_OverCurrentProtectorSensorHysteresis_Object = MibTableColumn
overCurrentProtectorSensorHysteresis = _OverCurrentProtectorSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 13),
    _OverCurrentProtectorSensorHysteresis_Type()
)
overCurrentProtectorSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorHysteresis.setStatus("current")


class _OverCurrentProtectorSensorStateChangeDelay_Type(Unsigned32):
    """Custom type overCurrentProtectorSensorStateChangeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OverCurrentProtectorSensorStateChangeDelay_Type.__name__ = "Unsigned32"
_OverCurrentProtectorSensorStateChangeDelay_Object = MibTableColumn
overCurrentProtectorSensorStateChangeDelay = _OverCurrentProtectorSensorStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 14),
    _OverCurrentProtectorSensorStateChangeDelay_Type()
)
overCurrentProtectorSensorStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorStateChangeDelay.setStatus("current")
_OverCurrentProtectorSensorLowerCriticalThreshold_Type = Unsigned32
_OverCurrentProtectorSensorLowerCriticalThreshold_Object = MibTableColumn
overCurrentProtectorSensorLowerCriticalThreshold = _OverCurrentProtectorSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 21),
    _OverCurrentProtectorSensorLowerCriticalThreshold_Type()
)
overCurrentProtectorSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorLowerCriticalThreshold.setStatus("current")
_OverCurrentProtectorSensorLowerWarningThreshold_Type = Unsigned32
_OverCurrentProtectorSensorLowerWarningThreshold_Object = MibTableColumn
overCurrentProtectorSensorLowerWarningThreshold = _OverCurrentProtectorSensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 22),
    _OverCurrentProtectorSensorLowerWarningThreshold_Type()
)
overCurrentProtectorSensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorLowerWarningThreshold.setStatus("current")
_OverCurrentProtectorSensorUpperCriticalThreshold_Type = Unsigned32
_OverCurrentProtectorSensorUpperCriticalThreshold_Object = MibTableColumn
overCurrentProtectorSensorUpperCriticalThreshold = _OverCurrentProtectorSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 23),
    _OverCurrentProtectorSensorUpperCriticalThreshold_Type()
)
overCurrentProtectorSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorUpperCriticalThreshold.setStatus("current")
_OverCurrentProtectorSensorUpperWarningThreshold_Type = Unsigned32
_OverCurrentProtectorSensorUpperWarningThreshold_Object = MibTableColumn
overCurrentProtectorSensorUpperWarningThreshold = _OverCurrentProtectorSensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 24),
    _OverCurrentProtectorSensorUpperWarningThreshold_Type()
)
overCurrentProtectorSensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorUpperWarningThreshold.setStatus("current")


class _OverCurrentProtectorSensorEnabledThresholds_Type(Bits):
    """Custom type overCurrentProtectorSensorEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_OverCurrentProtectorSensorEnabledThresholds_Type.__name__ = "Bits"
_OverCurrentProtectorSensorEnabledThresholds_Object = MibTableColumn
overCurrentProtectorSensorEnabledThresholds = _OverCurrentProtectorSensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 25),
    _OverCurrentProtectorSensorEnabledThresholds_Type()
)
overCurrentProtectorSensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorEnabledThresholds.setStatus("current")
_OverCurrentProtectorSensorSignedMaximum_Type = Integer32
_OverCurrentProtectorSensorSignedMaximum_Object = MibTableColumn
overCurrentProtectorSensorSignedMaximum = _OverCurrentProtectorSensorSignedMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 26),
    _OverCurrentProtectorSensorSignedMaximum_Type()
)
overCurrentProtectorSensorSignedMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorSignedMaximum.setStatus("current")
_OverCurrentProtectorSensorSignedMinimum_Type = Integer32
_OverCurrentProtectorSensorSignedMinimum_Object = MibTableColumn
overCurrentProtectorSensorSignedMinimum = _OverCurrentProtectorSensorSignedMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 27),
    _OverCurrentProtectorSensorSignedMinimum_Type()
)
overCurrentProtectorSensorSignedMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorSignedMinimum.setStatus("current")
_OverCurrentProtectorSensorSignedLowerCriticalThreshold_Type = Integer32
_OverCurrentProtectorSensorSignedLowerCriticalThreshold_Object = MibTableColumn
overCurrentProtectorSensorSignedLowerCriticalThreshold = _OverCurrentProtectorSensorSignedLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 28),
    _OverCurrentProtectorSensorSignedLowerCriticalThreshold_Type()
)
overCurrentProtectorSensorSignedLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorSignedLowerCriticalThreshold.setStatus("current")
_OverCurrentProtectorSensorSignedLowerWarningThreshold_Type = Integer32
_OverCurrentProtectorSensorSignedLowerWarningThreshold_Object = MibTableColumn
overCurrentProtectorSensorSignedLowerWarningThreshold = _OverCurrentProtectorSensorSignedLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 29),
    _OverCurrentProtectorSensorSignedLowerWarningThreshold_Type()
)
overCurrentProtectorSensorSignedLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorSignedLowerWarningThreshold.setStatus("current")
_OverCurrentProtectorSensorSignedUpperCriticalThreshold_Type = Integer32
_OverCurrentProtectorSensorSignedUpperCriticalThreshold_Object = MibTableColumn
overCurrentProtectorSensorSignedUpperCriticalThreshold = _OverCurrentProtectorSensorSignedUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 30),
    _OverCurrentProtectorSensorSignedUpperCriticalThreshold_Type()
)
overCurrentProtectorSensorSignedUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorSignedUpperCriticalThreshold.setStatus("current")
_OverCurrentProtectorSensorSignedUpperWarningThreshold_Type = Integer32
_OverCurrentProtectorSensorSignedUpperWarningThreshold_Object = MibTableColumn
overCurrentProtectorSensorSignedUpperWarningThreshold = _OverCurrentProtectorSensorSignedUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 4, 1, 31),
    _OverCurrentProtectorSensorSignedUpperWarningThreshold_Type()
)
overCurrentProtectorSensorSignedUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorSignedUpperWarningThreshold.setStatus("current")
_OverCurrentProtectorPoleConfigurationTable_Object = MibTable
overCurrentProtectorPoleConfigurationTable = _OverCurrentProtectorPoleConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 5)
)
if mibBuilder.loadTexts:
    overCurrentProtectorPoleConfigurationTable.setStatus("current")
_OverCurrentProtectorPoleConfigurationEntry_Object = MibTableRow
overCurrentProtectorPoleConfigurationEntry = _OverCurrentProtectorPoleConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 5, 1)
)
overCurrentProtectorPoleConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "overCurrentProtectorIndex"),
    (0, "PDU2-MIB", "overCurrentProtectorPoleIndex"),
)
if mibBuilder.loadTexts:
    overCurrentProtectorPoleConfigurationEntry.setStatus("current")


class _OverCurrentProtectorPoleIndex_Type(Integer32):
    """Custom type overCurrentProtectorPoleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_OverCurrentProtectorPoleIndex_Type.__name__ = "Integer32"
_OverCurrentProtectorPoleIndex_Object = MibTableColumn
overCurrentProtectorPoleIndex = _OverCurrentProtectorPoleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 5, 1, 1),
    _OverCurrentProtectorPoleIndex_Type()
)
overCurrentProtectorPoleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    overCurrentProtectorPoleIndex.setStatus("current")
_OverCurrentProtectorPoleLine_Type = LineEnumeration
_OverCurrentProtectorPoleLine_Object = MibTableColumn
overCurrentProtectorPoleLine = _OverCurrentProtectorPoleLine_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 5, 1, 2),
    _OverCurrentProtectorPoleLine_Type()
)
overCurrentProtectorPoleLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorPoleLine.setStatus("current")
_OverCurrentProtectorPoleInNode_Type = Integer32
_OverCurrentProtectorPoleInNode_Object = MibTableColumn
overCurrentProtectorPoleInNode = _OverCurrentProtectorPoleInNode_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 5, 1, 3),
    _OverCurrentProtectorPoleInNode_Type()
)
overCurrentProtectorPoleInNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorPoleInNode.setStatus("current")
_OverCurrentProtectorPoleOutNode_Type = Integer32
_OverCurrentProtectorPoleOutNode_Object = MibTableColumn
overCurrentProtectorPoleOutNode = _OverCurrentProtectorPoleOutNode_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 4, 5, 1, 4),
    _OverCurrentProtectorPoleOutNode_Type()
)
overCurrentProtectorPoleOutNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overCurrentProtectorPoleOutNode.setStatus("current")
_Outlets_ObjectIdentity = ObjectIdentity
outlets = _Outlets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5)
)
_OutletConfigurationTable_Object = MibTable
outletConfigurationTable = _OutletConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3)
)
if mibBuilder.loadTexts:
    outletConfigurationTable.setStatus("current")
_OutletConfigurationEntry_Object = MibTableRow
outletConfigurationEntry = _OutletConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1)
)
outletConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "outletId"),
)
if mibBuilder.loadTexts:
    outletConfigurationEntry.setStatus("current")


class _OutletId_Type(Integer32):
    """Custom type outletId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_OutletId_Type.__name__ = "Integer32"
_OutletId_Object = MibTableColumn
outletId = _OutletId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 1),
    _OutletId_Type()
)
outletId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outletId.setStatus("current")
_OutletLabel_Type = DisplayString
_OutletLabel_Object = MibTableColumn
outletLabel = _OutletLabel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 2),
    _OutletLabel_Type()
)
outletLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletLabel.setStatus("current")
_OutletName_Type = DisplayString
_OutletName_Object = MibTableColumn
outletName = _OutletName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 3),
    _OutletName_Type()
)
outletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletName.setStatus("current")
_OutletReceptacle_Type = ReceptacleTypeEnumeration
_OutletReceptacle_Object = MibTableColumn
outletReceptacle = _OutletReceptacle_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 4),
    _OutletReceptacle_Type()
)
outletReceptacle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletReceptacle.setStatus("deprecated")


class _OutletPoleCount_Type(Integer32):
    """Custom type outletPoleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_OutletPoleCount_Type.__name__ = "Integer32"
_OutletPoleCount_Object = MibTableColumn
outletPoleCount = _OutletPoleCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 5),
    _OutletPoleCount_Type()
)
outletPoleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPoleCount.setStatus("current")
_OutletRatedVoltage_Type = DisplayString
_OutletRatedVoltage_Object = MibTableColumn
outletRatedVoltage = _OutletRatedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 6),
    _OutletRatedVoltage_Type()
)
outletRatedVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletRatedVoltage.setStatus("current")
_OutletRatedCurrent_Type = DisplayString
_OutletRatedCurrent_Object = MibTableColumn
outletRatedCurrent = _OutletRatedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 7),
    _OutletRatedCurrent_Type()
)
outletRatedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletRatedCurrent.setStatus("current")
_OutletRatedVA_Type = DisplayString
_OutletRatedVA_Object = MibTableColumn
outletRatedVA = _OutletRatedVA_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 8),
    _OutletRatedVA_Type()
)
outletRatedVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletRatedVA.setStatus("current")


class _OutletDeviceCapabilities_Type(Bits):
    """Custom type outletDeviceCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("rmsCurrent", 0),
          ("peakCurrent", 1),
          ("unbalancedCurrent", 2),
          ("rmsVoltage", 3),
          ("activePower", 4),
          ("apparentPower", 5),
          ("powerFactor", 6),
          ("activeEnergy", 7),
          ("apparentEnergy", 8),
          ("onOff", 13),
          ("frequency", 22),
          ("phaseAngle", 23),
          ("reactivePower", 28),
          ("displacementPowerFactor", 34),
          ("crestFactor", 50),
          ("voltageThd", 56),
          ("currentThd", 57),
          ("inrushCurrent", 58))
    )

_OutletDeviceCapabilities_Type.__name__ = "Bits"
_OutletDeviceCapabilities_Object = MibTableColumn
outletDeviceCapabilities = _OutletDeviceCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 10),
    _OutletDeviceCapabilities_Type()
)
outletDeviceCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletDeviceCapabilities.setStatus("current")


class _OutletPoleCapabilities_Type(Bits):
    """Custom type outletPoleCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("rmsCurrent", 0),
          ("peakCurrent", 1),
          ("rmsVoltage", 3),
          ("activePower", 4),
          ("apparentPower", 5),
          ("powerFactor", 6),
          ("activeEnergy", 7),
          ("apparentEnergy", 8),
          ("phaseAngle", 23),
          ("rmsVoltageLN", 24),
          ("reactivePower", 28),
          ("displacementPowerFactor", 34),
          ("crestFactor", 50),
          ("voltageThd", 56),
          ("currentThd", 57))
    )

_OutletPoleCapabilities_Type.__name__ = "Bits"
_OutletPoleCapabilities_Object = MibTableColumn
outletPoleCapabilities = _OutletPoleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 11),
    _OutletPoleCapabilities_Type()
)
outletPoleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPoleCapabilities.setStatus("current")


class _OutletPowerCyclingPowerOffPeriod_Type(Unsigned32):
    """Custom type outletPowerCyclingPowerOffPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_OutletPowerCyclingPowerOffPeriod_Type.__name__ = "Unsigned32"
_OutletPowerCyclingPowerOffPeriod_Object = MibTableColumn
outletPowerCyclingPowerOffPeriod = _OutletPowerCyclingPowerOffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 12),
    _OutletPowerCyclingPowerOffPeriod_Type()
)
outletPowerCyclingPowerOffPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPowerCyclingPowerOffPeriod.setStatus("current")
_OutletStateOnStartup_Type = OutletStateOnStartupEnumeration
_OutletStateOnStartup_Object = MibTableColumn
outletStateOnStartup = _OutletStateOnStartup_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 13),
    _OutletStateOnStartup_Type()
)
outletStateOnStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletStateOnStartup.setStatus("current")
_OutletUseGlobalPowerCyclingPowerOffPeriod_Type = TruthValue
_OutletUseGlobalPowerCyclingPowerOffPeriod_Object = MibTableColumn
outletUseGlobalPowerCyclingPowerOffPeriod = _OutletUseGlobalPowerCyclingPowerOffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 14),
    _OutletUseGlobalPowerCyclingPowerOffPeriod_Type()
)
outletUseGlobalPowerCyclingPowerOffPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletUseGlobalPowerCyclingPowerOffPeriod.setStatus("current")
_OutletSwitchable_Type = TruthValue
_OutletSwitchable_Object = MibTableColumn
outletSwitchable = _OutletSwitchable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 28),
    _OutletSwitchable_Type()
)
outletSwitchable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSwitchable.setStatus("current")
_OutletReceptacleDescriptor_Type = DisplayString
_OutletReceptacleDescriptor_Object = MibTableColumn
outletReceptacleDescriptor = _OutletReceptacleDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 29),
    _OutletReceptacleDescriptor_Type()
)
outletReceptacleDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletReceptacleDescriptor.setStatus("current")
_OutletNonCritical_Type = TruthValue
_OutletNonCritical_Object = MibTableColumn
outletNonCritical = _OutletNonCritical_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 30),
    _OutletNonCritical_Type()
)
outletNonCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletNonCritical.setStatus("current")


class _OutletSequenceDelay_Type(Unsigned32):
    """Custom type outletSequenceDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_OutletSequenceDelay_Type.__name__ = "Unsigned32"
_OutletSequenceDelay_Object = MibTableColumn
outletSequenceDelay = _OutletSequenceDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 32),
    _OutletSequenceDelay_Type()
)
outletSequenceDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSequenceDelay.setStatus("current")
_OutletPowerSource_Type = RowPointer
_OutletPowerSource_Object = MibTableColumn
outletPowerSource = _OutletPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 33),
    _OutletPowerSource_Type()
)
outletPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPowerSource.setStatus("current")
_OutletServiceMode_Type = TruthValue
_OutletServiceMode_Object = MibTableColumn
outletServiceMode = _OutletServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 3, 1, 34),
    _OutletServiceMode_Type()
)
outletServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletServiceMode.setStatus("current")
_OutletSensorConfigurationTable_Object = MibTable
outletSensorConfigurationTable = _OutletSensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4)
)
if mibBuilder.loadTexts:
    outletSensorConfigurationTable.setStatus("current")
_OutletSensorConfigurationEntry_Object = MibTableRow
outletSensorConfigurationEntry = _OutletSensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1)
)
outletSensorConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "outletId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    outletSensorConfigurationEntry.setStatus("current")
_OutletSensorLogAvailable_Type = TruthValue
_OutletSensorLogAvailable_Object = MibTableColumn
outletSensorLogAvailable = _OutletSensorLogAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 4),
    _OutletSensorLogAvailable_Type()
)
outletSensorLogAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSensorLogAvailable.setStatus("current")
_OutletSensorUnits_Type = SensorUnitsEnumeration
_OutletSensorUnits_Object = MibTableColumn
outletSensorUnits = _OutletSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 6),
    _OutletSensorUnits_Type()
)
outletSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSensorUnits.setStatus("current")
_OutletSensorDecimalDigits_Type = Unsigned32
_OutletSensorDecimalDigits_Object = MibTableColumn
outletSensorDecimalDigits = _OutletSensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 7),
    _OutletSensorDecimalDigits_Type()
)
outletSensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSensorDecimalDigits.setStatus("current")
_OutletSensorAccuracy_Type = HundredthsOfAPercentage
_OutletSensorAccuracy_Object = MibTableColumn
outletSensorAccuracy = _OutletSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 8),
    _OutletSensorAccuracy_Type()
)
outletSensorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSensorAccuracy.setStatus("deprecated")
_OutletSensorResolution_Type = Unsigned32
_OutletSensorResolution_Object = MibTableColumn
outletSensorResolution = _OutletSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 9),
    _OutletSensorResolution_Type()
)
outletSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSensorResolution.setStatus("current")
_OutletSensorTolerance_Type = Unsigned32
_OutletSensorTolerance_Object = MibTableColumn
outletSensorTolerance = _OutletSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 10),
    _OutletSensorTolerance_Type()
)
outletSensorTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSensorTolerance.setStatus("deprecated")
_OutletSensorMaximum_Type = Unsigned32
_OutletSensorMaximum_Object = MibTableColumn
outletSensorMaximum = _OutletSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 11),
    _OutletSensorMaximum_Type()
)
outletSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSensorMaximum.setStatus("current")
_OutletSensorMinimum_Type = Unsigned32
_OutletSensorMinimum_Object = MibTableColumn
outletSensorMinimum = _OutletSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 12),
    _OutletSensorMinimum_Type()
)
outletSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSensorMinimum.setStatus("current")
_OutletSensorHysteresis_Type = Unsigned32
_OutletSensorHysteresis_Object = MibTableColumn
outletSensorHysteresis = _OutletSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 13),
    _OutletSensorHysteresis_Type()
)
outletSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSensorHysteresis.setStatus("current")


class _OutletSensorStateChangeDelay_Type(Unsigned32):
    """Custom type outletSensorStateChangeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OutletSensorStateChangeDelay_Type.__name__ = "Unsigned32"
_OutletSensorStateChangeDelay_Object = MibTableColumn
outletSensorStateChangeDelay = _OutletSensorStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 14),
    _OutletSensorStateChangeDelay_Type()
)
outletSensorStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSensorStateChangeDelay.setStatus("current")
_OutletSensorLowerCriticalThreshold_Type = Unsigned32
_OutletSensorLowerCriticalThreshold_Object = MibTableColumn
outletSensorLowerCriticalThreshold = _OutletSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 21),
    _OutletSensorLowerCriticalThreshold_Type()
)
outletSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSensorLowerCriticalThreshold.setStatus("current")
_OutletSensorLowerWarningThreshold_Type = Unsigned32
_OutletSensorLowerWarningThreshold_Object = MibTableColumn
outletSensorLowerWarningThreshold = _OutletSensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 22),
    _OutletSensorLowerWarningThreshold_Type()
)
outletSensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSensorLowerWarningThreshold.setStatus("current")
_OutletSensorUpperCriticalThreshold_Type = Unsigned32
_OutletSensorUpperCriticalThreshold_Object = MibTableColumn
outletSensorUpperCriticalThreshold = _OutletSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 23),
    _OutletSensorUpperCriticalThreshold_Type()
)
outletSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSensorUpperCriticalThreshold.setStatus("current")
_OutletSensorUpperWarningThreshold_Type = Unsigned32
_OutletSensorUpperWarningThreshold_Object = MibTableColumn
outletSensorUpperWarningThreshold = _OutletSensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 24),
    _OutletSensorUpperWarningThreshold_Type()
)
outletSensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSensorUpperWarningThreshold.setStatus("current")


class _OutletSensorEnabledThresholds_Type(Bits):
    """Custom type outletSensorEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_OutletSensorEnabledThresholds_Type.__name__ = "Bits"
_OutletSensorEnabledThresholds_Object = MibTableColumn
outletSensorEnabledThresholds = _OutletSensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 25),
    _OutletSensorEnabledThresholds_Type()
)
outletSensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSensorEnabledThresholds.setStatus("current")
_OutletSensorSignedMaximum_Type = Integer32
_OutletSensorSignedMaximum_Object = MibTableColumn
outletSensorSignedMaximum = _OutletSensorSignedMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 26),
    _OutletSensorSignedMaximum_Type()
)
outletSensorSignedMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSensorSignedMaximum.setStatus("current")
_OutletSensorSignedMinimum_Type = Integer32
_OutletSensorSignedMinimum_Object = MibTableColumn
outletSensorSignedMinimum = _OutletSensorSignedMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 27),
    _OutletSensorSignedMinimum_Type()
)
outletSensorSignedMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSensorSignedMinimum.setStatus("current")
_OutletSensorSignedLowerCriticalThreshold_Type = Integer32
_OutletSensorSignedLowerCriticalThreshold_Object = MibTableColumn
outletSensorSignedLowerCriticalThreshold = _OutletSensorSignedLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 28),
    _OutletSensorSignedLowerCriticalThreshold_Type()
)
outletSensorSignedLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSensorSignedLowerCriticalThreshold.setStatus("current")
_OutletSensorSignedLowerWarningThreshold_Type = Integer32
_OutletSensorSignedLowerWarningThreshold_Object = MibTableColumn
outletSensorSignedLowerWarningThreshold = _OutletSensorSignedLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 29),
    _OutletSensorSignedLowerWarningThreshold_Type()
)
outletSensorSignedLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSensorSignedLowerWarningThreshold.setStatus("current")
_OutletSensorSignedUpperCriticalThreshold_Type = Integer32
_OutletSensorSignedUpperCriticalThreshold_Object = MibTableColumn
outletSensorSignedUpperCriticalThreshold = _OutletSensorSignedUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 30),
    _OutletSensorSignedUpperCriticalThreshold_Type()
)
outletSensorSignedUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSensorSignedUpperCriticalThreshold.setStatus("current")
_OutletSensorSignedUpperWarningThreshold_Type = Integer32
_OutletSensorSignedUpperWarningThreshold_Object = MibTableColumn
outletSensorSignedUpperWarningThreshold = _OutletSensorSignedUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 4, 1, 31),
    _OutletSensorSignedUpperWarningThreshold_Type()
)
outletSensorSignedUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSensorSignedUpperWarningThreshold.setStatus("current")
_OutletPoleConfigurationTable_Object = MibTable
outletPoleConfigurationTable = _OutletPoleConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 5)
)
if mibBuilder.loadTexts:
    outletPoleConfigurationTable.setStatus("current")
_OutletPoleConfigurationEntry_Object = MibTableRow
outletPoleConfigurationEntry = _OutletPoleConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 5, 1)
)
outletPoleConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "outletId"),
    (0, "PDU2-MIB", "outletPoleIndex"),
)
if mibBuilder.loadTexts:
    outletPoleConfigurationEntry.setStatus("current")
_OutletPoleLine_Type = LineEnumeration
_OutletPoleLine_Object = MibTableColumn
outletPoleLine = _OutletPoleLine_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 5, 1, 1),
    _OutletPoleLine_Type()
)
outletPoleLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPoleLine.setStatus("current")
_OutletPoleNode_Type = Integer32
_OutletPoleNode_Object = MibTableColumn
outletPoleNode = _OutletPoleNode_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 5, 1, 2),
    _OutletPoleNode_Type()
)
outletPoleNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPoleNode.setStatus("current")
_OutletPoleSensorConfigurationTable_Object = MibTable
outletPoleSensorConfigurationTable = _OutletPoleSensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6)
)
if mibBuilder.loadTexts:
    outletPoleSensorConfigurationTable.setStatus("current")
_OutletPoleSensorConfigurationEntry_Object = MibTableRow
outletPoleSensorConfigurationEntry = _OutletPoleSensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1)
)
outletPoleSensorConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "outletId"),
    (0, "PDU2-MIB", "outletPoleIndex"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    outletPoleSensorConfigurationEntry.setStatus("current")


class _OutletPoleIndex_Type(Integer32):
    """Custom type outletPoleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_OutletPoleIndex_Type.__name__ = "Integer32"
_OutletPoleIndex_Object = MibTableColumn
outletPoleIndex = _OutletPoleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 1),
    _OutletPoleIndex_Type()
)
outletPoleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outletPoleIndex.setStatus("current")
_OutletPoleSensorLogAvailable_Type = TruthValue
_OutletPoleSensorLogAvailable_Object = MibTableColumn
outletPoleSensorLogAvailable = _OutletPoleSensorLogAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 4),
    _OutletPoleSensorLogAvailable_Type()
)
outletPoleSensorLogAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPoleSensorLogAvailable.setStatus("current")
_OutletPoleSensorUnits_Type = SensorUnitsEnumeration
_OutletPoleSensorUnits_Object = MibTableColumn
outletPoleSensorUnits = _OutletPoleSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 6),
    _OutletPoleSensorUnits_Type()
)
outletPoleSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPoleSensorUnits.setStatus("current")
_OutletPoleSensorDecimalDigits_Type = Unsigned32
_OutletPoleSensorDecimalDigits_Object = MibTableColumn
outletPoleSensorDecimalDigits = _OutletPoleSensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 7),
    _OutletPoleSensorDecimalDigits_Type()
)
outletPoleSensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPoleSensorDecimalDigits.setStatus("current")
_OutletPoleSensorAccuracy_Type = HundredthsOfAPercentage
_OutletPoleSensorAccuracy_Object = MibTableColumn
outletPoleSensorAccuracy = _OutletPoleSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 8),
    _OutletPoleSensorAccuracy_Type()
)
outletPoleSensorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPoleSensorAccuracy.setStatus("deprecated")
_OutletPoleSensorResolution_Type = Unsigned32
_OutletPoleSensorResolution_Object = MibTableColumn
outletPoleSensorResolution = _OutletPoleSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 9),
    _OutletPoleSensorResolution_Type()
)
outletPoleSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPoleSensorResolution.setStatus("current")
_OutletPoleSensorTolerance_Type = Unsigned32
_OutletPoleSensorTolerance_Object = MibTableColumn
outletPoleSensorTolerance = _OutletPoleSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 10),
    _OutletPoleSensorTolerance_Type()
)
outletPoleSensorTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPoleSensorTolerance.setStatus("deprecated")
_OutletPoleSensorMaximum_Type = Unsigned32
_OutletPoleSensorMaximum_Object = MibTableColumn
outletPoleSensorMaximum = _OutletPoleSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 11),
    _OutletPoleSensorMaximum_Type()
)
outletPoleSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPoleSensorMaximum.setStatus("current")
_OutletPoleSensorMinimum_Type = Unsigned32
_OutletPoleSensorMinimum_Object = MibTableColumn
outletPoleSensorMinimum = _OutletPoleSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 12),
    _OutletPoleSensorMinimum_Type()
)
outletPoleSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPoleSensorMinimum.setStatus("current")
_OutletPoleSensorHysteresis_Type = Unsigned32
_OutletPoleSensorHysteresis_Object = MibTableColumn
outletPoleSensorHysteresis = _OutletPoleSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 13),
    _OutletPoleSensorHysteresis_Type()
)
outletPoleSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPoleSensorHysteresis.setStatus("current")


class _OutletPoleSensorStateChangeDelay_Type(Unsigned32):
    """Custom type outletPoleSensorStateChangeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OutletPoleSensorStateChangeDelay_Type.__name__ = "Unsigned32"
_OutletPoleSensorStateChangeDelay_Object = MibTableColumn
outletPoleSensorStateChangeDelay = _OutletPoleSensorStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 14),
    _OutletPoleSensorStateChangeDelay_Type()
)
outletPoleSensorStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPoleSensorStateChangeDelay.setStatus("current")
_OutletPoleSensorLowerCriticalThreshold_Type = Unsigned32
_OutletPoleSensorLowerCriticalThreshold_Object = MibTableColumn
outletPoleSensorLowerCriticalThreshold = _OutletPoleSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 21),
    _OutletPoleSensorLowerCriticalThreshold_Type()
)
outletPoleSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPoleSensorLowerCriticalThreshold.setStatus("current")
_OutletPoleSensorLowerWarningThreshold_Type = Unsigned32
_OutletPoleSensorLowerWarningThreshold_Object = MibTableColumn
outletPoleSensorLowerWarningThreshold = _OutletPoleSensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 22),
    _OutletPoleSensorLowerWarningThreshold_Type()
)
outletPoleSensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPoleSensorLowerWarningThreshold.setStatus("current")
_OutletPoleSensorUpperCriticalThreshold_Type = Unsigned32
_OutletPoleSensorUpperCriticalThreshold_Object = MibTableColumn
outletPoleSensorUpperCriticalThreshold = _OutletPoleSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 23),
    _OutletPoleSensorUpperCriticalThreshold_Type()
)
outletPoleSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPoleSensorUpperCriticalThreshold.setStatus("current")
_OutletPoleSensorUpperWarningThreshold_Type = Unsigned32
_OutletPoleSensorUpperWarningThreshold_Object = MibTableColumn
outletPoleSensorUpperWarningThreshold = _OutletPoleSensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 24),
    _OutletPoleSensorUpperWarningThreshold_Type()
)
outletPoleSensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPoleSensorUpperWarningThreshold.setStatus("current")


class _OutletPoleSensorEnabledThresholds_Type(Bits):
    """Custom type outletPoleSensorEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_OutletPoleSensorEnabledThresholds_Type.__name__ = "Bits"
_OutletPoleSensorEnabledThresholds_Object = MibTableColumn
outletPoleSensorEnabledThresholds = _OutletPoleSensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 25),
    _OutletPoleSensorEnabledThresholds_Type()
)
outletPoleSensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPoleSensorEnabledThresholds.setStatus("current")
_OutletPoleSensorSignedMaximum_Type = Integer32
_OutletPoleSensorSignedMaximum_Object = MibTableColumn
outletPoleSensorSignedMaximum = _OutletPoleSensorSignedMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 26),
    _OutletPoleSensorSignedMaximum_Type()
)
outletPoleSensorSignedMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPoleSensorSignedMaximum.setStatus("current")
_OutletPoleSensorSignedMinimum_Type = Integer32
_OutletPoleSensorSignedMinimum_Object = MibTableColumn
outletPoleSensorSignedMinimum = _OutletPoleSensorSignedMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 27),
    _OutletPoleSensorSignedMinimum_Type()
)
outletPoleSensorSignedMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletPoleSensorSignedMinimum.setStatus("current")
_OutletPoleSensorSignedLowerCriticalThreshold_Type = Integer32
_OutletPoleSensorSignedLowerCriticalThreshold_Object = MibTableColumn
outletPoleSensorSignedLowerCriticalThreshold = _OutletPoleSensorSignedLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 28),
    _OutletPoleSensorSignedLowerCriticalThreshold_Type()
)
outletPoleSensorSignedLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPoleSensorSignedLowerCriticalThreshold.setStatus("current")
_OutletPoleSensorSignedLowerWarningThreshold_Type = Integer32
_OutletPoleSensorSignedLowerWarningThreshold_Object = MibTableColumn
outletPoleSensorSignedLowerWarningThreshold = _OutletPoleSensorSignedLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 29),
    _OutletPoleSensorSignedLowerWarningThreshold_Type()
)
outletPoleSensorSignedLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPoleSensorSignedLowerWarningThreshold.setStatus("current")
_OutletPoleSensorSignedUpperCriticalThreshold_Type = Integer32
_OutletPoleSensorSignedUpperCriticalThreshold_Object = MibTableColumn
outletPoleSensorSignedUpperCriticalThreshold = _OutletPoleSensorSignedUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 30),
    _OutletPoleSensorSignedUpperCriticalThreshold_Type()
)
outletPoleSensorSignedUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPoleSensorSignedUpperCriticalThreshold.setStatus("current")
_OutletPoleSensorSignedUpperWarningThreshold_Type = Integer32
_OutletPoleSensorSignedUpperWarningThreshold_Object = MibTableColumn
outletPoleSensorSignedUpperWarningThreshold = _OutletPoleSensorSignedUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 5, 6, 1, 31),
    _OutletPoleSensorSignedUpperWarningThreshold_Type()
)
outletPoleSensorSignedUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPoleSensorSignedUpperWarningThreshold.setStatus("current")
_ExternalSensors_ObjectIdentity = ObjectIdentity
externalSensors = _ExternalSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6)
)
_ExternalSensorConfigurationTable_Object = MibTable
externalSensorConfigurationTable = _ExternalSensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3)
)
if mibBuilder.loadTexts:
    externalSensorConfigurationTable.setStatus("current")
_ExternalSensorConfigurationEntry_Object = MibTableRow
externalSensorConfigurationEntry = _ExternalSensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1)
)
externalSensorConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "sensorID"),
)
if mibBuilder.loadTexts:
    externalSensorConfigurationEntry.setStatus("current")


class _SensorID_Type(Integer32):
    """Custom type sensorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SensorID_Type.__name__ = "Integer32"
_SensorID_Object = MibTableColumn
sensorID = _SensorID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 1),
    _SensorID_Type()
)
sensorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sensorID.setStatus("current")
_ExternalSensorType_Type = SensorTypeEnumeration
_ExternalSensorType_Object = MibTableColumn
externalSensorType = _ExternalSensorType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 2),
    _ExternalSensorType_Type()
)
externalSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorType.setStatus("current")
_ExternalSensorSerialNumber_Type = DisplayString
_ExternalSensorSerialNumber_Object = MibTableColumn
externalSensorSerialNumber = _ExternalSensorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 3),
    _ExternalSensorSerialNumber_Type()
)
externalSensorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorSerialNumber.setStatus("current")
_ExternalSensorName_Type = DisplayString
_ExternalSensorName_Object = MibTableColumn
externalSensorName = _ExternalSensorName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 4),
    _ExternalSensorName_Type()
)
externalSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorName.setStatus("current")
_ExternalSensorDescription_Type = DisplayString
_ExternalSensorDescription_Object = MibTableColumn
externalSensorDescription = _ExternalSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 5),
    _ExternalSensorDescription_Type()
)
externalSensorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorDescription.setStatus("current")
_ExternalSensorXCoordinate_Type = DisplayString
_ExternalSensorXCoordinate_Object = MibTableColumn
externalSensorXCoordinate = _ExternalSensorXCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 6),
    _ExternalSensorXCoordinate_Type()
)
externalSensorXCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorXCoordinate.setStatus("current")
_ExternalSensorYCoordinate_Type = DisplayString
_ExternalSensorYCoordinate_Object = MibTableColumn
externalSensorYCoordinate = _ExternalSensorYCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 7),
    _ExternalSensorYCoordinate_Type()
)
externalSensorYCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorYCoordinate.setStatus("current")
_ExternalSensorZCoordinate_Type = DisplayString
_ExternalSensorZCoordinate_Object = MibTableColumn
externalSensorZCoordinate = _ExternalSensorZCoordinate_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 8),
    _ExternalSensorZCoordinate_Type()
)
externalSensorZCoordinate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorZCoordinate.setStatus("current")
_ExternalSensorChannelNumber_Type = Integer32
_ExternalSensorChannelNumber_Object = MibTableColumn
externalSensorChannelNumber = _ExternalSensorChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 9),
    _ExternalSensorChannelNumber_Type()
)
externalSensorChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorChannelNumber.setStatus("current")
_ExternalOnOffSensorSubtype_Type = SensorTypeEnumeration
_ExternalOnOffSensorSubtype_Object = MibTableColumn
externalOnOffSensorSubtype = _ExternalOnOffSensorSubtype_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 10),
    _ExternalOnOffSensorSubtype_Type()
)
externalOnOffSensorSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalOnOffSensorSubtype.setStatus("current")
_ExternalSensorLogAvailable_Type = TruthValue
_ExternalSensorLogAvailable_Object = MibTableColumn
externalSensorLogAvailable = _ExternalSensorLogAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 14),
    _ExternalSensorLogAvailable_Type()
)
externalSensorLogAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorLogAvailable.setStatus("current")
_ExternalSensorUnits_Type = SensorUnitsEnumeration
_ExternalSensorUnits_Object = MibTableColumn
externalSensorUnits = _ExternalSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 16),
    _ExternalSensorUnits_Type()
)
externalSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorUnits.setStatus("current")
_ExternalSensorDecimalDigits_Type = Unsigned32
_ExternalSensorDecimalDigits_Object = MibTableColumn
externalSensorDecimalDigits = _ExternalSensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 17),
    _ExternalSensorDecimalDigits_Type()
)
externalSensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorDecimalDigits.setStatus("current")
_ExternalSensorAccuracy_Type = HundredthsOfAPercentage
_ExternalSensorAccuracy_Object = MibTableColumn
externalSensorAccuracy = _ExternalSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 18),
    _ExternalSensorAccuracy_Type()
)
externalSensorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorAccuracy.setStatus("deprecated")
_ExternalSensorResolution_Type = Unsigned32
_ExternalSensorResolution_Object = MibTableColumn
externalSensorResolution = _ExternalSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 19),
    _ExternalSensorResolution_Type()
)
externalSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorResolution.setStatus("current")
_ExternalSensorTolerance_Type = Unsigned32
_ExternalSensorTolerance_Object = MibTableColumn
externalSensorTolerance = _ExternalSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 20),
    _ExternalSensorTolerance_Type()
)
externalSensorTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorTolerance.setStatus("deprecated")
_ExternalSensorMaximum_Type = Integer32
_ExternalSensorMaximum_Object = MibTableColumn
externalSensorMaximum = _ExternalSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 21),
    _ExternalSensorMaximum_Type()
)
externalSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorMaximum.setStatus("current")
_ExternalSensorMinimum_Type = Integer32
_ExternalSensorMinimum_Object = MibTableColumn
externalSensorMinimum = _ExternalSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 22),
    _ExternalSensorMinimum_Type()
)
externalSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorMinimum.setStatus("current")
_ExternalSensorHysteresis_Type = Unsigned32
_ExternalSensorHysteresis_Object = MibTableColumn
externalSensorHysteresis = _ExternalSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 23),
    _ExternalSensorHysteresis_Type()
)
externalSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorHysteresis.setStatus("current")


class _ExternalSensorStateChangeDelay_Type(Unsigned32):
    """Custom type externalSensorStateChangeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_ExternalSensorStateChangeDelay_Type.__name__ = "Unsigned32"
_ExternalSensorStateChangeDelay_Object = MibTableColumn
externalSensorStateChangeDelay = _ExternalSensorStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 24),
    _ExternalSensorStateChangeDelay_Type()
)
externalSensorStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorStateChangeDelay.setStatus("current")
_ExternalSensorLowerCriticalThreshold_Type = Integer32
_ExternalSensorLowerCriticalThreshold_Object = MibTableColumn
externalSensorLowerCriticalThreshold = _ExternalSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 31),
    _ExternalSensorLowerCriticalThreshold_Type()
)
externalSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorLowerCriticalThreshold.setStatus("current")
_ExternalSensorLowerWarningThreshold_Type = Integer32
_ExternalSensorLowerWarningThreshold_Object = MibTableColumn
externalSensorLowerWarningThreshold = _ExternalSensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 32),
    _ExternalSensorLowerWarningThreshold_Type()
)
externalSensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorLowerWarningThreshold.setStatus("current")
_ExternalSensorUpperCriticalThreshold_Type = Integer32
_ExternalSensorUpperCriticalThreshold_Object = MibTableColumn
externalSensorUpperCriticalThreshold = _ExternalSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 33),
    _ExternalSensorUpperCriticalThreshold_Type()
)
externalSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorUpperCriticalThreshold.setStatus("current")
_ExternalSensorUpperWarningThreshold_Type = Integer32
_ExternalSensorUpperWarningThreshold_Object = MibTableColumn
externalSensorUpperWarningThreshold = _ExternalSensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 34),
    _ExternalSensorUpperWarningThreshold_Type()
)
externalSensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorUpperWarningThreshold.setStatus("current")


class _ExternalSensorEnabledThresholds_Type(Bits):
    """Custom type externalSensorEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_ExternalSensorEnabledThresholds_Type.__name__ = "Bits"
_ExternalSensorEnabledThresholds_Object = MibTableColumn
externalSensorEnabledThresholds = _ExternalSensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 35),
    _ExternalSensorEnabledThresholds_Type()
)
externalSensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorEnabledThresholds.setStatus("current")
_ExternalSensorIsActuator_Type = TruthValue
_ExternalSensorIsActuator_Object = MibTableColumn
externalSensorIsActuator = _ExternalSensorIsActuator_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 36),
    _ExternalSensorIsActuator_Type()
)
externalSensorIsActuator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorIsActuator.setStatus("current")
_ExternalSensorPosition_Type = DisplayString
_ExternalSensorPosition_Object = MibTableColumn
externalSensorPosition = _ExternalSensorPosition_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 37),
    _ExternalSensorPosition_Type()
)
externalSensorPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorPosition.setStatus("current")
_ExternalSensorUseDefaultThresholds_Type = TruthValue
_ExternalSensorUseDefaultThresholds_Object = MibTableColumn
externalSensorUseDefaultThresholds = _ExternalSensorUseDefaultThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 38),
    _ExternalSensorUseDefaultThresholds_Type()
)
externalSensorUseDefaultThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorUseDefaultThresholds.setStatus("current")


class _ExternalSensorAlarmedToNormalDelay_Type(Integer32):
    """Custom type externalSensorAlarmedToNormalDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_ExternalSensorAlarmedToNormalDelay_Type.__name__ = "Integer32"
_ExternalSensorAlarmedToNormalDelay_Object = MibTableColumn
externalSensorAlarmedToNormalDelay = _ExternalSensorAlarmedToNormalDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 3, 1, 39),
    _ExternalSensorAlarmedToNormalDelay_Type()
)
externalSensorAlarmedToNormalDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorAlarmedToNormalDelay.setStatus("current")
_ExternalSensorTypeDefaultThresholdsTable_Object = MibTable
externalSensorTypeDefaultThresholdsTable = _ExternalSensorTypeDefaultThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 4)
)
if mibBuilder.loadTexts:
    externalSensorTypeDefaultThresholdsTable.setStatus("current")
_ExternalSensorTypeDefaultThresholdsEntry_Object = MibTableRow
externalSensorTypeDefaultThresholdsEntry = _ExternalSensorTypeDefaultThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 4, 1)
)
externalSensorTypeDefaultThresholdsEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    externalSensorTypeDefaultThresholdsEntry.setStatus("current")
_ExternalSensorTypeDefaultHysteresis_Type = Unsigned32
_ExternalSensorTypeDefaultHysteresis_Object = MibTableColumn
externalSensorTypeDefaultHysteresis = _ExternalSensorTypeDefaultHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 4, 1, 3),
    _ExternalSensorTypeDefaultHysteresis_Type()
)
externalSensorTypeDefaultHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultHysteresis.setStatus("current")


class _ExternalSensorTypeDefaultStateChangeDelay_Type(Unsigned32):
    """Custom type externalSensorTypeDefaultStateChangeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_ExternalSensorTypeDefaultStateChangeDelay_Type.__name__ = "Unsigned32"
_ExternalSensorTypeDefaultStateChangeDelay_Object = MibTableColumn
externalSensorTypeDefaultStateChangeDelay = _ExternalSensorTypeDefaultStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 4, 1, 4),
    _ExternalSensorTypeDefaultStateChangeDelay_Type()
)
externalSensorTypeDefaultStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultStateChangeDelay.setStatus("current")
_ExternalSensorTypeDefaultLowerCriticalThreshold_Type = Integer32
_ExternalSensorTypeDefaultLowerCriticalThreshold_Object = MibTableColumn
externalSensorTypeDefaultLowerCriticalThreshold = _ExternalSensorTypeDefaultLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 4, 1, 5),
    _ExternalSensorTypeDefaultLowerCriticalThreshold_Type()
)
externalSensorTypeDefaultLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultLowerCriticalThreshold.setStatus("current")
_ExternalSensorTypeDefaultLowerWarningThreshold_Type = Integer32
_ExternalSensorTypeDefaultLowerWarningThreshold_Object = MibTableColumn
externalSensorTypeDefaultLowerWarningThreshold = _ExternalSensorTypeDefaultLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 4, 1, 6),
    _ExternalSensorTypeDefaultLowerWarningThreshold_Type()
)
externalSensorTypeDefaultLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultLowerWarningThreshold.setStatus("current")
_ExternalSensorTypeDefaultUpperCriticalThreshold_Type = Integer32
_ExternalSensorTypeDefaultUpperCriticalThreshold_Object = MibTableColumn
externalSensorTypeDefaultUpperCriticalThreshold = _ExternalSensorTypeDefaultUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 4, 1, 7),
    _ExternalSensorTypeDefaultUpperCriticalThreshold_Type()
)
externalSensorTypeDefaultUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultUpperCriticalThreshold.setStatus("current")
_ExternalSensorTypeDefaultUpperWarningThreshold_Type = Integer32
_ExternalSensorTypeDefaultUpperWarningThreshold_Object = MibTableColumn
externalSensorTypeDefaultUpperWarningThreshold = _ExternalSensorTypeDefaultUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 4, 1, 8),
    _ExternalSensorTypeDefaultUpperWarningThreshold_Type()
)
externalSensorTypeDefaultUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultUpperWarningThreshold.setStatus("current")


class _ExternalSensorTypeDefaultEnabledThresholds_Type(Bits):
    """Custom type externalSensorTypeDefaultEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_ExternalSensorTypeDefaultEnabledThresholds_Type.__name__ = "Bits"
_ExternalSensorTypeDefaultEnabledThresholds_Object = MibTableColumn
externalSensorTypeDefaultEnabledThresholds = _ExternalSensorTypeDefaultEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 4, 1, 9),
    _ExternalSensorTypeDefaultEnabledThresholds_Type()
)
externalSensorTypeDefaultEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultEnabledThresholds.setStatus("current")
_ExternalSensorTypeDefaultUnit_Type = SensorUnitsEnumeration
_ExternalSensorTypeDefaultUnit_Object = MibTableColumn
externalSensorTypeDefaultUnit = _ExternalSensorTypeDefaultUnit_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 4, 1, 10),
    _ExternalSensorTypeDefaultUnit_Type()
)
externalSensorTypeDefaultUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultUnit.setStatus("current")
_ExternalSensorTypeDefaultDecimalDigits_Type = Unsigned32
_ExternalSensorTypeDefaultDecimalDigits_Object = MibTableColumn
externalSensorTypeDefaultDecimalDigits = _ExternalSensorTypeDefaultDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 4, 1, 11),
    _ExternalSensorTypeDefaultDecimalDigits_Type()
)
externalSensorTypeDefaultDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultDecimalDigits.setStatus("current")
_ExternalSensorTypeDefaultMaximum_Type = Integer32
_ExternalSensorTypeDefaultMaximum_Object = MibTableColumn
externalSensorTypeDefaultMaximum = _ExternalSensorTypeDefaultMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 4, 1, 12),
    _ExternalSensorTypeDefaultMaximum_Type()
)
externalSensorTypeDefaultMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultMaximum.setStatus("current")
_ExternalSensorTypeDefaultMinimum_Type = Integer32
_ExternalSensorTypeDefaultMinimum_Object = MibTableColumn
externalSensorTypeDefaultMinimum = _ExternalSensorTypeDefaultMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 4, 1, 13),
    _ExternalSensorTypeDefaultMinimum_Type()
)
externalSensorTypeDefaultMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalSensorTypeDefaultMinimum.setStatus("current")
_PeripheralDevicePackageTable_Object = MibTable
peripheralDevicePackageTable = _PeripheralDevicePackageTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 5)
)
if mibBuilder.loadTexts:
    peripheralDevicePackageTable.setStatus("current")
_PeripheralDevicePackageEntry_Object = MibTableRow
peripheralDevicePackageEntry = _PeripheralDevicePackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 5, 1)
)
peripheralDevicePackageEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "peripheralDevicePackageId"),
)
if mibBuilder.loadTexts:
    peripheralDevicePackageEntry.setStatus("current")


class _PeripheralDevicePackageId_Type(Integer32):
    """Custom type peripheralDevicePackageId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_PeripheralDevicePackageId_Type.__name__ = "Integer32"
_PeripheralDevicePackageId_Object = MibTableColumn
peripheralDevicePackageId = _PeripheralDevicePackageId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 5, 1, 1),
    _PeripheralDevicePackageId_Type()
)
peripheralDevicePackageId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    peripheralDevicePackageId.setStatus("current")
_PeripheralDevicePackageSerialNumber_Type = DisplayString
_PeripheralDevicePackageSerialNumber_Object = MibTableColumn
peripheralDevicePackageSerialNumber = _PeripheralDevicePackageSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 5, 1, 3),
    _PeripheralDevicePackageSerialNumber_Type()
)
peripheralDevicePackageSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peripheralDevicePackageSerialNumber.setStatus("current")
_PeripheralDevicePackageModel_Type = DisplayString
_PeripheralDevicePackageModel_Object = MibTableColumn
peripheralDevicePackageModel = _PeripheralDevicePackageModel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 5, 1, 4),
    _PeripheralDevicePackageModel_Type()
)
peripheralDevicePackageModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peripheralDevicePackageModel.setStatus("current")
_PeripheralDevicePackageFirmwareVersion_Type = DisplayString
_PeripheralDevicePackageFirmwareVersion_Object = MibTableColumn
peripheralDevicePackageFirmwareVersion = _PeripheralDevicePackageFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 5, 1, 5),
    _PeripheralDevicePackageFirmwareVersion_Type()
)
peripheralDevicePackageFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peripheralDevicePackageFirmwareVersion.setStatus("current")
_PeripheralDevicePackageMinFirmwareVersion_Type = DisplayString
_PeripheralDevicePackageMinFirmwareVersion_Object = MibTableColumn
peripheralDevicePackageMinFirmwareVersion = _PeripheralDevicePackageMinFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 5, 1, 6),
    _PeripheralDevicePackageMinFirmwareVersion_Type()
)
peripheralDevicePackageMinFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peripheralDevicePackageMinFirmwareVersion.setStatus("current")
_PeripheralDevicePackageFirmwareTimeStamp_Type = Unsigned32
_PeripheralDevicePackageFirmwareTimeStamp_Object = MibTableColumn
peripheralDevicePackageFirmwareTimeStamp = _PeripheralDevicePackageFirmwareTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 5, 1, 7),
    _PeripheralDevicePackageFirmwareTimeStamp_Type()
)
peripheralDevicePackageFirmwareTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peripheralDevicePackageFirmwareTimeStamp.setStatus("current")
_PeripheralDevicePackagePosition_Type = DisplayString
_PeripheralDevicePackagePosition_Object = MibTableColumn
peripheralDevicePackagePosition = _PeripheralDevicePackagePosition_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 5, 1, 8),
    _PeripheralDevicePackagePosition_Type()
)
peripheralDevicePackagePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peripheralDevicePackagePosition.setStatus("current")
_PeripheralDevicePackageState_Type = DisplayString
_PeripheralDevicePackageState_Object = MibTableColumn
peripheralDevicePackageState = _PeripheralDevicePackageState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 6, 5, 1, 9),
    _PeripheralDevicePackageState_Type()
)
peripheralDevicePackageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peripheralDevicePackageState.setStatus("current")
_ServerReachability_ObjectIdentity = ObjectIdentity
serverReachability = _ServerReachability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 7)
)
_ServerReachabilityTable_Object = MibTable
serverReachabilityTable = _ServerReachabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 7, 3)
)
if mibBuilder.loadTexts:
    serverReachabilityTable.setStatus("current")
_ServerReachabilityEntry_Object = MibTableRow
serverReachabilityEntry = _ServerReachabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 7, 3, 1)
)
serverReachabilityEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "serverID"),
)
if mibBuilder.loadTexts:
    serverReachabilityEntry.setStatus("current")


class _ServerID_Type(Integer32):
    """Custom type serverID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ServerID_Type.__name__ = "Integer32"
_ServerID_Object = MibTableColumn
serverID = _ServerID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 7, 3, 1, 1),
    _ServerID_Type()
)
serverID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serverID.setStatus("current")
_ServerIPAddress_Type = DisplayString
_ServerIPAddress_Object = MibTableColumn
serverIPAddress = _ServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 7, 3, 1, 3),
    _ServerIPAddress_Type()
)
serverIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverIPAddress.setStatus("current")
_ServerPingEnabled_Type = TruthValue
_ServerPingEnabled_Object = MibTableColumn
serverPingEnabled = _ServerPingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 7, 3, 1, 4),
    _ServerPingEnabled_Type()
)
serverPingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverPingEnabled.setStatus("current")
_Wires_ObjectIdentity = ObjectIdentity
wires = _Wires_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8)
)
_WireConfigurationTable_Object = MibTable
wireConfigurationTable = _WireConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 3)
)
if mibBuilder.loadTexts:
    wireConfigurationTable.setStatus("obsolete")
_WireConfigurationEntry_Object = MibTableRow
wireConfigurationEntry = _WireConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 3, 1)
)
wireConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "wireId"),
)
if mibBuilder.loadTexts:
    wireConfigurationEntry.setStatus("obsolete")


class _WireId_Type(Integer32):
    """Custom type wireId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_WireId_Type.__name__ = "Integer32"
_WireId_Object = MibTableColumn
wireId = _WireId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 3, 1, 1),
    _WireId_Type()
)
wireId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wireId.setStatus("obsolete")
_WireLabel_Type = DisplayString
_WireLabel_Object = MibTableColumn
wireLabel = _WireLabel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 3, 1, 2),
    _WireLabel_Type()
)
wireLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wireLabel.setStatus("obsolete")


class _WireCapabilities_Type(Bits):
    """Custom type wireCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("rmsCurrent", 0),
          ("peakCurrent", 1),
          ("unbalancedCurrent", 2),
          ("rmsVoltage", 3),
          ("activePower", 4),
          ("apparentPower", 5),
          ("powerFactor", 6),
          ("activeEnergy", 7),
          ("apparentEnergy", 8))
    )

_WireCapabilities_Type.__name__ = "Bits"
_WireCapabilities_Object = MibTableColumn
wireCapabilities = _WireCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 3, 1, 3),
    _WireCapabilities_Type()
)
wireCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wireCapabilities.setStatus("obsolete")
_WirePowerSource_Type = RowPointer
_WirePowerSource_Object = MibTableColumn
wirePowerSource = _WirePowerSource_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 3, 1, 4),
    _WirePowerSource_Type()
)
wirePowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirePowerSource.setStatus("obsolete")
_WireSensorConfigurationTable_Object = MibTable
wireSensorConfigurationTable = _WireSensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4)
)
if mibBuilder.loadTexts:
    wireSensorConfigurationTable.setStatus("obsolete")
_WireSensorConfigurationEntry_Object = MibTableRow
wireSensorConfigurationEntry = _WireSensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1)
)
wireSensorConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "wireId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    wireSensorConfigurationEntry.setStatus("obsolete")
_WireSensorLogAvailable_Type = TruthValue
_WireSensorLogAvailable_Object = MibTableColumn
wireSensorLogAvailable = _WireSensorLogAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1, 4),
    _WireSensorLogAvailable_Type()
)
wireSensorLogAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wireSensorLogAvailable.setStatus("obsolete")
_WireSensorUnits_Type = SensorUnitsEnumeration
_WireSensorUnits_Object = MibTableColumn
wireSensorUnits = _WireSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1, 6),
    _WireSensorUnits_Type()
)
wireSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wireSensorUnits.setStatus("obsolete")
_WireSensorDecimalDigits_Type = Unsigned32
_WireSensorDecimalDigits_Object = MibTableColumn
wireSensorDecimalDigits = _WireSensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1, 7),
    _WireSensorDecimalDigits_Type()
)
wireSensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wireSensorDecimalDigits.setStatus("obsolete")
_WireSensorAccuracy_Type = HundredthsOfAPercentage
_WireSensorAccuracy_Object = MibTableColumn
wireSensorAccuracy = _WireSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1, 8),
    _WireSensorAccuracy_Type()
)
wireSensorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wireSensorAccuracy.setStatus("obsolete")
_WireSensorResolution_Type = Unsigned32
_WireSensorResolution_Object = MibTableColumn
wireSensorResolution = _WireSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1, 9),
    _WireSensorResolution_Type()
)
wireSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wireSensorResolution.setStatus("obsolete")
_WireSensorTolerance_Type = Unsigned32
_WireSensorTolerance_Object = MibTableColumn
wireSensorTolerance = _WireSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1, 10),
    _WireSensorTolerance_Type()
)
wireSensorTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wireSensorTolerance.setStatus("obsolete")
_WireSensorMaximum_Type = Unsigned32
_WireSensorMaximum_Object = MibTableColumn
wireSensorMaximum = _WireSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1, 11),
    _WireSensorMaximum_Type()
)
wireSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wireSensorMaximum.setStatus("obsolete")
_WireSensorMinimum_Type = Unsigned32
_WireSensorMinimum_Object = MibTableColumn
wireSensorMinimum = _WireSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1, 12),
    _WireSensorMinimum_Type()
)
wireSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wireSensorMinimum.setStatus("obsolete")
_WireSensorHysteresis_Type = Unsigned32
_WireSensorHysteresis_Object = MibTableColumn
wireSensorHysteresis = _WireSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1, 13),
    _WireSensorHysteresis_Type()
)
wireSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wireSensorHysteresis.setStatus("obsolete")


class _WireSensorStateChangeDelay_Type(Unsigned32):
    """Custom type wireSensorStateChangeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_WireSensorStateChangeDelay_Type.__name__ = "Unsigned32"
_WireSensorStateChangeDelay_Object = MibTableColumn
wireSensorStateChangeDelay = _WireSensorStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1, 14),
    _WireSensorStateChangeDelay_Type()
)
wireSensorStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wireSensorStateChangeDelay.setStatus("obsolete")
_WireSensorLowerCriticalThreshold_Type = Unsigned32
_WireSensorLowerCriticalThreshold_Object = MibTableColumn
wireSensorLowerCriticalThreshold = _WireSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1, 21),
    _WireSensorLowerCriticalThreshold_Type()
)
wireSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wireSensorLowerCriticalThreshold.setStatus("obsolete")
_WireSensorLowerWarningThreshold_Type = Unsigned32
_WireSensorLowerWarningThreshold_Object = MibTableColumn
wireSensorLowerWarningThreshold = _WireSensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1, 22),
    _WireSensorLowerWarningThreshold_Type()
)
wireSensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wireSensorLowerWarningThreshold.setStatus("obsolete")
_WireSensorUpperCriticalThreshold_Type = Unsigned32
_WireSensorUpperCriticalThreshold_Object = MibTableColumn
wireSensorUpperCriticalThreshold = _WireSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1, 23),
    _WireSensorUpperCriticalThreshold_Type()
)
wireSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wireSensorUpperCriticalThreshold.setStatus("obsolete")
_WireSensorUpperWarningThreshold_Type = Unsigned32
_WireSensorUpperWarningThreshold_Object = MibTableColumn
wireSensorUpperWarningThreshold = _WireSensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1, 24),
    _WireSensorUpperWarningThreshold_Type()
)
wireSensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wireSensorUpperWarningThreshold.setStatus("obsolete")


class _WireSensorEnabledThresholds_Type(Bits):
    """Custom type wireSensorEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_WireSensorEnabledThresholds_Type.__name__ = "Bits"
_WireSensorEnabledThresholds_Object = MibTableColumn
wireSensorEnabledThresholds = _WireSensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 8, 4, 1, 25),
    _WireSensorEnabledThresholds_Type()
)
wireSensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wireSensorEnabledThresholds.setStatus("obsolete")
_TransferSwitch_ObjectIdentity = ObjectIdentity
transferSwitch = _TransferSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9)
)
_TransferSwitchConfigurationTable_Object = MibTable
transferSwitchConfigurationTable = _TransferSwitchConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 3)
)
if mibBuilder.loadTexts:
    transferSwitchConfigurationTable.setStatus("current")
_TransferSwitchConfigurationEntry_Object = MibTableRow
transferSwitchConfigurationEntry = _TransferSwitchConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 3, 1)
)
transferSwitchConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "transferSwitchId"),
)
if mibBuilder.loadTexts:
    transferSwitchConfigurationEntry.setStatus("current")


class _TransferSwitchId_Type(Integer32):
    """Custom type transferSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TransferSwitchId_Type.__name__ = "Integer32"
_TransferSwitchId_Object = MibTableColumn
transferSwitchId = _TransferSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 3, 1, 1),
    _TransferSwitchId_Type()
)
transferSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    transferSwitchId.setStatus("current")
_TransferSwitchLabel_Type = DisplayString
_TransferSwitchLabel_Object = MibTableColumn
transferSwitchLabel = _TransferSwitchLabel_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 3, 1, 2),
    _TransferSwitchLabel_Type()
)
transferSwitchLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchLabel.setStatus("current")
_TransferSwitchName_Type = DisplayString
_TransferSwitchName_Object = MibTableColumn
transferSwitchName = _TransferSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 3, 1, 3),
    _TransferSwitchName_Type()
)
transferSwitchName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchName.setStatus("current")


class _TransferSwitchPreferredInlet_Type(Integer32):
    """Custom type transferSwitchPreferredInlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TransferSwitchPreferredInlet_Type.__name__ = "Integer32"
_TransferSwitchPreferredInlet_Object = MibTableColumn
transferSwitchPreferredInlet = _TransferSwitchPreferredInlet_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 3, 1, 4),
    _TransferSwitchPreferredInlet_Type()
)
transferSwitchPreferredInlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchPreferredInlet.setStatus("current")


class _TransferSwitchPoleCount_Type(Integer32):
    """Custom type transferSwitchPoleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_TransferSwitchPoleCount_Type.__name__ = "Integer32"
_TransferSwitchPoleCount_Object = MibTableColumn
transferSwitchPoleCount = _TransferSwitchPoleCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 3, 1, 5),
    _TransferSwitchPoleCount_Type()
)
transferSwitchPoleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchPoleCount.setStatus("current")
_TransferSwitchAutoReTransferEnabled_Type = TruthValue
_TransferSwitchAutoReTransferEnabled_Object = MibTableColumn
transferSwitchAutoReTransferEnabled = _TransferSwitchAutoReTransferEnabled_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 3, 1, 20),
    _TransferSwitchAutoReTransferEnabled_Type()
)
transferSwitchAutoReTransferEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchAutoReTransferEnabled.setStatus("current")


class _TransferSwitchAutoReTransferWaitTime_Type(Unsigned32):
    """Custom type transferSwitchAutoReTransferWaitTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_TransferSwitchAutoReTransferWaitTime_Type.__name__ = "Unsigned32"
_TransferSwitchAutoReTransferWaitTime_Object = MibTableColumn
transferSwitchAutoReTransferWaitTime = _TransferSwitchAutoReTransferWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 3, 1, 21),
    _TransferSwitchAutoReTransferWaitTime_Type()
)
transferSwitchAutoReTransferWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchAutoReTransferWaitTime.setStatus("current")
_TransferSwitchAutoReTransferRequiresPhaseSync_Type = TruthValue
_TransferSwitchAutoReTransferRequiresPhaseSync_Object = MibTableColumn
transferSwitchAutoReTransferRequiresPhaseSync = _TransferSwitchAutoReTransferRequiresPhaseSync_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 3, 1, 22),
    _TransferSwitchAutoReTransferRequiresPhaseSync_Type()
)
transferSwitchAutoReTransferRequiresPhaseSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchAutoReTransferRequiresPhaseSync.setStatus("current")
_TransferSwitchFrontPanelManualTransferButtonEnabled_Type = TruthValue
_TransferSwitchFrontPanelManualTransferButtonEnabled_Object = MibTableColumn
transferSwitchFrontPanelManualTransferButtonEnabled = _TransferSwitchFrontPanelManualTransferButtonEnabled_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 3, 1, 23),
    _TransferSwitchFrontPanelManualTransferButtonEnabled_Type()
)
transferSwitchFrontPanelManualTransferButtonEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchFrontPanelManualTransferButtonEnabled.setStatus("current")


class _TransferSwitchCapabilities_Type(Bits):
    """Custom type transferSwitchCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("overloadStatus", 32),
          ("inletPhaseSyncAngle", 37),
          ("inletPhaseSync", 38),
          ("operatingState", 39),
          ("activeInlet", 40),
          ("switchStatus", 47),
          ("transferSwitchBypassState", 77),
          ("installFaultStatus", 79),
          ("transferSwitchOutputStatus", 80))
    )

_TransferSwitchCapabilities_Type.__name__ = "Bits"
_TransferSwitchCapabilities_Object = MibTableColumn
transferSwitchCapabilities = _TransferSwitchCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 3, 1, 24),
    _TransferSwitchCapabilities_Type()
)
transferSwitchCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchCapabilities.setStatus("current")
_TransferSwitchPowerSource1_Type = RowPointer
_TransferSwitchPowerSource1_Object = MibTableColumn
transferSwitchPowerSource1 = _TransferSwitchPowerSource1_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 3, 1, 31),
    _TransferSwitchPowerSource1_Type()
)
transferSwitchPowerSource1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchPowerSource1.setStatus("current")
_TransferSwitchPowerSource2_Type = RowPointer
_TransferSwitchPowerSource2_Object = MibTableColumn
transferSwitchPowerSource2 = _TransferSwitchPowerSource2_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 3, 1, 32),
    _TransferSwitchPowerSource2_Type()
)
transferSwitchPowerSource2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchPowerSource2.setStatus("current")
_TransferSwitchSensorConfigurationTable_Object = MibTable
transferSwitchSensorConfigurationTable = _TransferSwitchSensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4)
)
if mibBuilder.loadTexts:
    transferSwitchSensorConfigurationTable.setStatus("current")
_TransferSwitchSensorConfigurationEntry_Object = MibTableRow
transferSwitchSensorConfigurationEntry = _TransferSwitchSensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1)
)
transferSwitchSensorConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "transferSwitchId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    transferSwitchSensorConfigurationEntry.setStatus("current")
_TransferSwitchSensorLogAvailable_Type = TruthValue
_TransferSwitchSensorLogAvailable_Object = MibTableColumn
transferSwitchSensorLogAvailable = _TransferSwitchSensorLogAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 4),
    _TransferSwitchSensorLogAvailable_Type()
)
transferSwitchSensorLogAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchSensorLogAvailable.setStatus("current")
_TransferSwitchSensorUnits_Type = SensorUnitsEnumeration
_TransferSwitchSensorUnits_Object = MibTableColumn
transferSwitchSensorUnits = _TransferSwitchSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 6),
    _TransferSwitchSensorUnits_Type()
)
transferSwitchSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchSensorUnits.setStatus("current")
_TransferSwitchSensorDecimalDigits_Type = Unsigned32
_TransferSwitchSensorDecimalDigits_Object = MibTableColumn
transferSwitchSensorDecimalDigits = _TransferSwitchSensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 7),
    _TransferSwitchSensorDecimalDigits_Type()
)
transferSwitchSensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchSensorDecimalDigits.setStatus("current")
_TransferSwitchSensorAccuracy_Type = HundredthsOfAPercentage
_TransferSwitchSensorAccuracy_Object = MibTableColumn
transferSwitchSensorAccuracy = _TransferSwitchSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 8),
    _TransferSwitchSensorAccuracy_Type()
)
transferSwitchSensorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchSensorAccuracy.setStatus("deprecated")
_TransferSwitchSensorResolution_Type = Unsigned32
_TransferSwitchSensorResolution_Object = MibTableColumn
transferSwitchSensorResolution = _TransferSwitchSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 9),
    _TransferSwitchSensorResolution_Type()
)
transferSwitchSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchSensorResolution.setStatus("current")
_TransferSwitchSensorTolerance_Type = Unsigned32
_TransferSwitchSensorTolerance_Object = MibTableColumn
transferSwitchSensorTolerance = _TransferSwitchSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 10),
    _TransferSwitchSensorTolerance_Type()
)
transferSwitchSensorTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchSensorTolerance.setStatus("deprecated")
_TransferSwitchSensorMaximum_Type = Unsigned32
_TransferSwitchSensorMaximum_Object = MibTableColumn
transferSwitchSensorMaximum = _TransferSwitchSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 11),
    _TransferSwitchSensorMaximum_Type()
)
transferSwitchSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchSensorMaximum.setStatus("current")
_TransferSwitchSensorMinimum_Type = Unsigned32
_TransferSwitchSensorMinimum_Object = MibTableColumn
transferSwitchSensorMinimum = _TransferSwitchSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 12),
    _TransferSwitchSensorMinimum_Type()
)
transferSwitchSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchSensorMinimum.setStatus("current")
_TransferSwitchSensorHysteresis_Type = Unsigned32
_TransferSwitchSensorHysteresis_Object = MibTableColumn
transferSwitchSensorHysteresis = _TransferSwitchSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 13),
    _TransferSwitchSensorHysteresis_Type()
)
transferSwitchSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchSensorHysteresis.setStatus("current")


class _TransferSwitchSensorStateChangeDelay_Type(Unsigned32):
    """Custom type transferSwitchSensorStateChangeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_TransferSwitchSensorStateChangeDelay_Type.__name__ = "Unsigned32"
_TransferSwitchSensorStateChangeDelay_Object = MibTableColumn
transferSwitchSensorStateChangeDelay = _TransferSwitchSensorStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 14),
    _TransferSwitchSensorStateChangeDelay_Type()
)
transferSwitchSensorStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchSensorStateChangeDelay.setStatus("current")
_TransferSwitchSensorLowerCriticalThreshold_Type = Unsigned32
_TransferSwitchSensorLowerCriticalThreshold_Object = MibTableColumn
transferSwitchSensorLowerCriticalThreshold = _TransferSwitchSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 21),
    _TransferSwitchSensorLowerCriticalThreshold_Type()
)
transferSwitchSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchSensorLowerCriticalThreshold.setStatus("current")
_TransferSwitchSensorLowerWarningThreshold_Type = Unsigned32
_TransferSwitchSensorLowerWarningThreshold_Object = MibTableColumn
transferSwitchSensorLowerWarningThreshold = _TransferSwitchSensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 22),
    _TransferSwitchSensorLowerWarningThreshold_Type()
)
transferSwitchSensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchSensorLowerWarningThreshold.setStatus("current")
_TransferSwitchSensorUpperCriticalThreshold_Type = Unsigned32
_TransferSwitchSensorUpperCriticalThreshold_Object = MibTableColumn
transferSwitchSensorUpperCriticalThreshold = _TransferSwitchSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 23),
    _TransferSwitchSensorUpperCriticalThreshold_Type()
)
transferSwitchSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchSensorUpperCriticalThreshold.setStatus("current")
_TransferSwitchSensorUpperWarningThreshold_Type = Unsigned32
_TransferSwitchSensorUpperWarningThreshold_Object = MibTableColumn
transferSwitchSensorUpperWarningThreshold = _TransferSwitchSensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 24),
    _TransferSwitchSensorUpperWarningThreshold_Type()
)
transferSwitchSensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchSensorUpperWarningThreshold.setStatus("current")


class _TransferSwitchSensorEnabledThresholds_Type(Bits):
    """Custom type transferSwitchSensorEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_TransferSwitchSensorEnabledThresholds_Type.__name__ = "Bits"
_TransferSwitchSensorEnabledThresholds_Object = MibTableColumn
transferSwitchSensorEnabledThresholds = _TransferSwitchSensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 25),
    _TransferSwitchSensorEnabledThresholds_Type()
)
transferSwitchSensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchSensorEnabledThresholds.setStatus("current")
_TransferSwitchSensorSignedMaximum_Type = Integer32
_TransferSwitchSensorSignedMaximum_Object = MibTableColumn
transferSwitchSensorSignedMaximum = _TransferSwitchSensorSignedMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 26),
    _TransferSwitchSensorSignedMaximum_Type()
)
transferSwitchSensorSignedMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchSensorSignedMaximum.setStatus("current")
_TransferSwitchSensorSignedMinimum_Type = Integer32
_TransferSwitchSensorSignedMinimum_Object = MibTableColumn
transferSwitchSensorSignedMinimum = _TransferSwitchSensorSignedMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 27),
    _TransferSwitchSensorSignedMinimum_Type()
)
transferSwitchSensorSignedMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchSensorSignedMinimum.setStatus("current")
_TransferSwitchSensorSignedLowerCriticalThreshold_Type = Integer32
_TransferSwitchSensorSignedLowerCriticalThreshold_Object = MibTableColumn
transferSwitchSensorSignedLowerCriticalThreshold = _TransferSwitchSensorSignedLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 28),
    _TransferSwitchSensorSignedLowerCriticalThreshold_Type()
)
transferSwitchSensorSignedLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchSensorSignedLowerCriticalThreshold.setStatus("current")
_TransferSwitchSensorSignedLowerWarningThreshold_Type = Integer32
_TransferSwitchSensorSignedLowerWarningThreshold_Object = MibTableColumn
transferSwitchSensorSignedLowerWarningThreshold = _TransferSwitchSensorSignedLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 29),
    _TransferSwitchSensorSignedLowerWarningThreshold_Type()
)
transferSwitchSensorSignedLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchSensorSignedLowerWarningThreshold.setStatus("current")
_TransferSwitchSensorSignedUpperCriticalThreshold_Type = Integer32
_TransferSwitchSensorSignedUpperCriticalThreshold_Object = MibTableColumn
transferSwitchSensorSignedUpperCriticalThreshold = _TransferSwitchSensorSignedUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 30),
    _TransferSwitchSensorSignedUpperCriticalThreshold_Type()
)
transferSwitchSensorSignedUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchSensorSignedUpperCriticalThreshold.setStatus("current")
_TransferSwitchSensorSignedUpperWarningThreshold_Type = Integer32
_TransferSwitchSensorSignedUpperWarningThreshold_Object = MibTableColumn
transferSwitchSensorSignedUpperWarningThreshold = _TransferSwitchSensorSignedUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 4, 1, 31),
    _TransferSwitchSensorSignedUpperWarningThreshold_Type()
)
transferSwitchSensorSignedUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchSensorSignedUpperWarningThreshold.setStatus("current")
_TransferSwitchPoleConfigurationTable_Object = MibTable
transferSwitchPoleConfigurationTable = _TransferSwitchPoleConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 5)
)
if mibBuilder.loadTexts:
    transferSwitchPoleConfigurationTable.setStatus("current")
_TransferSwitchPoleConfigurationEntry_Object = MibTableRow
transferSwitchPoleConfigurationEntry = _TransferSwitchPoleConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 5, 1)
)
transferSwitchPoleConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "transferSwitchId"),
    (0, "PDU2-MIB", "transferSwitchPoleIndex"),
)
if mibBuilder.loadTexts:
    transferSwitchPoleConfigurationEntry.setStatus("current")


class _TransferSwitchPoleIndex_Type(Integer32):
    """Custom type transferSwitchPoleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TransferSwitchPoleIndex_Type.__name__ = "Integer32"
_TransferSwitchPoleIndex_Object = MibTableColumn
transferSwitchPoleIndex = _TransferSwitchPoleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 5, 1, 1),
    _TransferSwitchPoleIndex_Type()
)
transferSwitchPoleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    transferSwitchPoleIndex.setStatus("current")
_TransferSwitchPoleLine_Type = LineEnumeration
_TransferSwitchPoleLine_Object = MibTableColumn
transferSwitchPoleLine = _TransferSwitchPoleLine_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 5, 1, 2),
    _TransferSwitchPoleLine_Type()
)
transferSwitchPoleLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchPoleLine.setStatus("current")
_TransferSwitchPoleIn1Node_Type = Integer32
_TransferSwitchPoleIn1Node_Object = MibTableColumn
transferSwitchPoleIn1Node = _TransferSwitchPoleIn1Node_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 5, 1, 3),
    _TransferSwitchPoleIn1Node_Type()
)
transferSwitchPoleIn1Node.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchPoleIn1Node.setStatus("current")
_TransferSwitchPoleIn2Node_Type = Integer32
_TransferSwitchPoleIn2Node_Object = MibTableColumn
transferSwitchPoleIn2Node = _TransferSwitchPoleIn2Node_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 5, 1, 4),
    _TransferSwitchPoleIn2Node_Type()
)
transferSwitchPoleIn2Node.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchPoleIn2Node.setStatus("current")
_TransferSwitchPoleOutNode_Type = Integer32
_TransferSwitchPoleOutNode_Object = MibTableColumn
transferSwitchPoleOutNode = _TransferSwitchPoleOutNode_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 9, 5, 1, 5),
    _TransferSwitchPoleOutNode_Type()
)
transferSwitchPoleOutNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchPoleOutNode.setStatus("current")
_PowerMeter_ObjectIdentity = ObjectIdentity
powerMeter = _PowerMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 10)
)
_PowerMeterConfigurationTable_Object = MibTable
powerMeterConfigurationTable = _PowerMeterConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 10, 2)
)
if mibBuilder.loadTexts:
    powerMeterConfigurationTable.setStatus("current")
_PowerMeterConfigurationEntry_Object = MibTableRow
powerMeterConfigurationEntry = _PowerMeterConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 10, 2, 1)
)
powerMeterConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
)
if mibBuilder.loadTexts:
    powerMeterConfigurationEntry.setStatus("current")
_PowerMeterPhaseCTRating_Type = Unsigned32
_PowerMeterPhaseCTRating_Object = MibTableColumn
powerMeterPhaseCTRating = _PowerMeterPhaseCTRating_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 10, 2, 1, 2),
    _PowerMeterPhaseCTRating_Type()
)
powerMeterPhaseCTRating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMeterPhaseCTRating.setStatus("current")
_PowerMeterNeutralCTRating_Type = Unsigned32
_PowerMeterNeutralCTRating_Object = MibTableColumn
powerMeterNeutralCTRating = _PowerMeterNeutralCTRating_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 10, 2, 1, 3),
    _PowerMeterNeutralCTRating_Type()
)
powerMeterNeutralCTRating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMeterNeutralCTRating.setStatus("current")
_PowerMeterEarthCTRating_Type = Unsigned32
_PowerMeterEarthCTRating_Object = MibTableColumn
powerMeterEarthCTRating = _PowerMeterEarthCTRating_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 10, 2, 1, 4),
    _PowerMeterEarthCTRating_Type()
)
powerMeterEarthCTRating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMeterEarthCTRating.setStatus("current")
_PowerMeterBranchCount_Type = Unsigned32
_PowerMeterBranchCount_Object = MibTableColumn
powerMeterBranchCount = _PowerMeterBranchCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 10, 2, 1, 5),
    _PowerMeterBranchCount_Type()
)
powerMeterBranchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerMeterBranchCount.setStatus("current")


class _PowerMeterPanelPositions_Type(Integer32):
    """Custom type powerMeterPanelPositions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_PowerMeterPanelPositions_Type.__name__ = "Integer32"
_PowerMeterPanelPositions_Object = MibTableColumn
powerMeterPanelPositions = _PowerMeterPanelPositions_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 10, 2, 1, 6),
    _PowerMeterPanelPositions_Type()
)
powerMeterPanelPositions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerMeterPanelPositions.setStatus("current")
_PowerMeterPanelLayout_Type = PanelLayoutEnumeration
_PowerMeterPanelLayout_Object = MibTableColumn
powerMeterPanelLayout = _PowerMeterPanelLayout_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 10, 2, 1, 7),
    _PowerMeterPanelLayout_Type()
)
powerMeterPanelLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerMeterPanelLayout.setStatus("current")
_PowerMeterPanelNumbering_Type = PanelNumberingEnumeration
_PowerMeterPanelNumbering_Object = MibTableColumn
powerMeterPanelNumbering = _PowerMeterPanelNumbering_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 10, 2, 1, 8),
    _PowerMeterPanelNumbering_Type()
)
powerMeterPanelNumbering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerMeterPanelNumbering.setStatus("current")
_PowerMeterType_Type = PowerMeterTypeEnumeration
_PowerMeterType_Object = MibTableColumn
powerMeterType = _PowerMeterType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 10, 2, 1, 9),
    _PowerMeterType_Type()
)
powerMeterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerMeterType.setStatus("current")
_Circuit_ObjectIdentity = ObjectIdentity
circuit = _Circuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11)
)
_CircuitConfigurationTable_Object = MibTable
circuitConfigurationTable = _CircuitConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 2)
)
if mibBuilder.loadTexts:
    circuitConfigurationTable.setStatus("current")
_CircuitConfigurationEntry_Object = MibTableRow
circuitConfigurationEntry = _CircuitConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 2, 1)
)
circuitConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "circuitId"),
)
if mibBuilder.loadTexts:
    circuitConfigurationEntry.setStatus("current")


class _CircuitId_Type(Integer32):
    """Custom type circuitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CircuitId_Type.__name__ = "Integer32"
_CircuitId_Object = MibTableColumn
circuitId = _CircuitId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 2, 1, 1),
    _CircuitId_Type()
)
circuitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    circuitId.setStatus("current")


class _CircuitPoleCount_Type(Integer32):
    """Custom type circuitPoleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CircuitPoleCount_Type.__name__ = "Integer32"
_CircuitPoleCount_Object = MibTableColumn
circuitPoleCount = _CircuitPoleCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 2, 1, 2),
    _CircuitPoleCount_Type()
)
circuitPoleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitPoleCount.setStatus("current")
_CircuitName_Type = DisplayString
_CircuitName_Object = MibTableColumn
circuitName = _CircuitName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 2, 1, 3),
    _CircuitName_Type()
)
circuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitName.setStatus("current")
_CircuitType_Type = CircuitTypeEnumeration
_CircuitType_Object = MibTableColumn
circuitType = _CircuitType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 2, 1, 4),
    _CircuitType_Type()
)
circuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitType.setStatus("current")
_CircuitRatedCurrent_Type = Unsigned32
_CircuitRatedCurrent_Object = MibTableColumn
circuitRatedCurrent = _CircuitRatedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 2, 1, 5),
    _CircuitRatedCurrent_Type()
)
circuitRatedCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitRatedCurrent.setStatus("current")
_CircuitCTRating_Type = Unsigned32
_CircuitCTRating_Object = MibTableColumn
circuitCTRating = _CircuitCTRating_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 2, 1, 6),
    _CircuitCTRating_Type()
)
circuitCTRating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitCTRating.setStatus("current")


class _CircuitCapabilities_Type(Bits):
    """Custom type circuitCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("rmsCurrent", 0),
          ("peakCurrent", 1),
          ("unbalancedCurrent", 2),
          ("rmsVoltage", 3),
          ("activePower", 4),
          ("apparentPower", 5),
          ("powerFactor", 6),
          ("activeEnergy", 7),
          ("apparentEnergy", 8),
          ("surgeProtectorStatus", 21),
          ("frequency", 22),
          ("phaseAngle", 23),
          ("residualCurrent", 25),
          ("rcmState", 26),
          ("reactivePower", 28),
          ("powerQuality", 31),
          ("displacementPowerFactor", 34),
          ("crestFactor", 50),
          ("activePowerDemand", 53))
    )

_CircuitCapabilities_Type.__name__ = "Bits"
_CircuitCapabilities_Object = MibTableColumn
circuitCapabilities = _CircuitCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 2, 1, 7),
    _CircuitCapabilities_Type()
)
circuitCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitCapabilities.setStatus("current")


class _CircuitPoleCapabilities_Type(Bits):
    """Custom type circuitPoleCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("rmsCurrent", 0),
          ("peakCurrent", 1),
          ("rmsVoltage", 3),
          ("activePower", 4),
          ("apparentPower", 5),
          ("powerFactor", 6),
          ("activeEnergy", 7),
          ("apparentEnergy", 8),
          ("phaseAngle", 23),
          ("rmsVoltageLN", 24),
          ("reactivePower", 28),
          ("displacementPowerFactor", 34),
          ("crestFactor", 50))
    )

_CircuitPoleCapabilities_Type.__name__ = "Bits"
_CircuitPoleCapabilities_Object = MibTableColumn
circuitPoleCapabilities = _CircuitPoleCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 2, 1, 8),
    _CircuitPoleCapabilities_Type()
)
circuitPoleCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitPoleCapabilities.setStatus("current")
_CircuitPowerSource_Type = RowPointer
_CircuitPowerSource_Object = MibTableColumn
circuitPowerSource = _CircuitPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 2, 1, 9),
    _CircuitPowerSource_Type()
)
circuitPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitPowerSource.setStatus("current")
_CircuitPoleConfigurationTable_Object = MibTable
circuitPoleConfigurationTable = _CircuitPoleConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 3)
)
if mibBuilder.loadTexts:
    circuitPoleConfigurationTable.setStatus("current")
_CircuitPoleConfigurationEntry_Object = MibTableRow
circuitPoleConfigurationEntry = _CircuitPoleConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 3, 1)
)
circuitPoleConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "circuitId"),
    (0, "PDU2-MIB", "circuitPoleId"),
)
if mibBuilder.loadTexts:
    circuitPoleConfigurationEntry.setStatus("current")


class _CircuitPoleId_Type(Integer32):
    """Custom type circuitPoleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CircuitPoleId_Type.__name__ = "Integer32"
_CircuitPoleId_Object = MibTableColumn
circuitPoleId = _CircuitPoleId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 3, 1, 1),
    _CircuitPoleId_Type()
)
circuitPoleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    circuitPoleId.setStatus("current")


class _CircuitPolePanelPosition_Type(Integer32):
    """Custom type circuitPolePanelPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CircuitPolePanelPosition_Type.__name__ = "Integer32"
_CircuitPolePanelPosition_Object = MibTableColumn
circuitPolePanelPosition = _CircuitPolePanelPosition_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 3, 1, 2),
    _CircuitPolePanelPosition_Type()
)
circuitPolePanelPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitPolePanelPosition.setStatus("current")


class _CircuitPoleCTNumber_Type(Integer32):
    """Custom type circuitPoleCTNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CircuitPoleCTNumber_Type.__name__ = "Integer32"
_CircuitPoleCTNumber_Object = MibTableColumn
circuitPoleCTNumber = _CircuitPoleCTNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 3, 1, 3),
    _CircuitPoleCTNumber_Type()
)
circuitPoleCTNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPoleCTNumber.setStatus("current")
_CircuitPolePhase_Type = PhaseEnumeration
_CircuitPolePhase_Object = MibTableColumn
circuitPolePhase = _CircuitPolePhase_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 3, 1, 4),
    _CircuitPolePhase_Type()
)
circuitPolePhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPolePhase.setStatus("current")
_CircuitSensorConfigurationTable_Object = MibTable
circuitSensorConfigurationTable = _CircuitSensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4)
)
if mibBuilder.loadTexts:
    circuitSensorConfigurationTable.setStatus("current")
_CircuitSensorConfigurationEntry_Object = MibTableRow
circuitSensorConfigurationEntry = _CircuitSensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1)
)
circuitSensorConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "circuitId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    circuitSensorConfigurationEntry.setStatus("current")
_CircuitSensorLogAvailable_Type = TruthValue
_CircuitSensorLogAvailable_Object = MibTableColumn
circuitSensorLogAvailable = _CircuitSensorLogAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 4),
    _CircuitSensorLogAvailable_Type()
)
circuitSensorLogAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSensorLogAvailable.setStatus("current")
_CircuitSensorUnits_Type = SensorUnitsEnumeration
_CircuitSensorUnits_Object = MibTableColumn
circuitSensorUnits = _CircuitSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 6),
    _CircuitSensorUnits_Type()
)
circuitSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitSensorUnits.setStatus("current")
_CircuitSensorDecimalDigits_Type = Unsigned32
_CircuitSensorDecimalDigits_Object = MibTableColumn
circuitSensorDecimalDigits = _CircuitSensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 7),
    _CircuitSensorDecimalDigits_Type()
)
circuitSensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitSensorDecimalDigits.setStatus("current")
_CircuitSensorResolution_Type = Unsigned32
_CircuitSensorResolution_Object = MibTableColumn
circuitSensorResolution = _CircuitSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 9),
    _CircuitSensorResolution_Type()
)
circuitSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitSensorResolution.setStatus("current")
_CircuitSensorMaximum_Type = Unsigned32
_CircuitSensorMaximum_Object = MibTableColumn
circuitSensorMaximum = _CircuitSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 11),
    _CircuitSensorMaximum_Type()
)
circuitSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitSensorMaximum.setStatus("current")
_CircuitSensorMinimum_Type = Unsigned32
_CircuitSensorMinimum_Object = MibTableColumn
circuitSensorMinimum = _CircuitSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 12),
    _CircuitSensorMinimum_Type()
)
circuitSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitSensorMinimum.setStatus("current")
_CircuitSensorHysteresis_Type = Unsigned32
_CircuitSensorHysteresis_Object = MibTableColumn
circuitSensorHysteresis = _CircuitSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 13),
    _CircuitSensorHysteresis_Type()
)
circuitSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSensorHysteresis.setStatus("current")


class _CircuitSensorStateChangeDelay_Type(Unsigned32):
    """Custom type circuitSensorStateChangeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_CircuitSensorStateChangeDelay_Type.__name__ = "Unsigned32"
_CircuitSensorStateChangeDelay_Object = MibTableColumn
circuitSensorStateChangeDelay = _CircuitSensorStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 14),
    _CircuitSensorStateChangeDelay_Type()
)
circuitSensorStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSensorStateChangeDelay.setStatus("current")
_CircuitSensorLowerCriticalThreshold_Type = Unsigned32
_CircuitSensorLowerCriticalThreshold_Object = MibTableColumn
circuitSensorLowerCriticalThreshold = _CircuitSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 21),
    _CircuitSensorLowerCriticalThreshold_Type()
)
circuitSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSensorLowerCriticalThreshold.setStatus("current")
_CircuitSensorLowerWarningThreshold_Type = Unsigned32
_CircuitSensorLowerWarningThreshold_Object = MibTableColumn
circuitSensorLowerWarningThreshold = _CircuitSensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 22),
    _CircuitSensorLowerWarningThreshold_Type()
)
circuitSensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSensorLowerWarningThreshold.setStatus("current")
_CircuitSensorUpperCriticalThreshold_Type = Unsigned32
_CircuitSensorUpperCriticalThreshold_Object = MibTableColumn
circuitSensorUpperCriticalThreshold = _CircuitSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 23),
    _CircuitSensorUpperCriticalThreshold_Type()
)
circuitSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSensorUpperCriticalThreshold.setStatus("current")
_CircuitSensorUpperWarningThreshold_Type = Unsigned32
_CircuitSensorUpperWarningThreshold_Object = MibTableColumn
circuitSensorUpperWarningThreshold = _CircuitSensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 24),
    _CircuitSensorUpperWarningThreshold_Type()
)
circuitSensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSensorUpperWarningThreshold.setStatus("current")


class _CircuitSensorEnabledThresholds_Type(Bits):
    """Custom type circuitSensorEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_CircuitSensorEnabledThresholds_Type.__name__ = "Bits"
_CircuitSensorEnabledThresholds_Object = MibTableColumn
circuitSensorEnabledThresholds = _CircuitSensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 25),
    _CircuitSensorEnabledThresholds_Type()
)
circuitSensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSensorEnabledThresholds.setStatus("current")
_CircuitSensorSignedMaximum_Type = Integer32
_CircuitSensorSignedMaximum_Object = MibTableColumn
circuitSensorSignedMaximum = _CircuitSensorSignedMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 26),
    _CircuitSensorSignedMaximum_Type()
)
circuitSensorSignedMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitSensorSignedMaximum.setStatus("current")
_CircuitSensorSignedMinimum_Type = Integer32
_CircuitSensorSignedMinimum_Object = MibTableColumn
circuitSensorSignedMinimum = _CircuitSensorSignedMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 27),
    _CircuitSensorSignedMinimum_Type()
)
circuitSensorSignedMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitSensorSignedMinimum.setStatus("current")
_CircuitSensorSignedLowerCriticalThreshold_Type = Integer32
_CircuitSensorSignedLowerCriticalThreshold_Object = MibTableColumn
circuitSensorSignedLowerCriticalThreshold = _CircuitSensorSignedLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 28),
    _CircuitSensorSignedLowerCriticalThreshold_Type()
)
circuitSensorSignedLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSensorSignedLowerCriticalThreshold.setStatus("current")
_CircuitSensorSignedLowerWarningThreshold_Type = Integer32
_CircuitSensorSignedLowerWarningThreshold_Object = MibTableColumn
circuitSensorSignedLowerWarningThreshold = _CircuitSensorSignedLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 29),
    _CircuitSensorSignedLowerWarningThreshold_Type()
)
circuitSensorSignedLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSensorSignedLowerWarningThreshold.setStatus("current")
_CircuitSensorSignedUpperCriticalThreshold_Type = Integer32
_CircuitSensorSignedUpperCriticalThreshold_Object = MibTableColumn
circuitSensorSignedUpperCriticalThreshold = _CircuitSensorSignedUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 30),
    _CircuitSensorSignedUpperCriticalThreshold_Type()
)
circuitSensorSignedUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSensorSignedUpperCriticalThreshold.setStatus("current")
_CircuitSensorSignedUpperWarningThreshold_Type = Integer32
_CircuitSensorSignedUpperWarningThreshold_Object = MibTableColumn
circuitSensorSignedUpperWarningThreshold = _CircuitSensorSignedUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 4, 1, 31),
    _CircuitSensorSignedUpperWarningThreshold_Type()
)
circuitSensorSignedUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSensorSignedUpperWarningThreshold.setStatus("current")
_CircuitPoleSensorConfigurationTable_Object = MibTable
circuitPoleSensorConfigurationTable = _CircuitPoleSensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6)
)
if mibBuilder.loadTexts:
    circuitPoleSensorConfigurationTable.setStatus("current")
_CircuitPoleSensorConfigurationEntry_Object = MibTableRow
circuitPoleSensorConfigurationEntry = _CircuitPoleSensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1)
)
circuitPoleSensorConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "circuitId"),
    (0, "PDU2-MIB", "circuitPoleId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    circuitPoleSensorConfigurationEntry.setStatus("current")
_CircuitPoleSensorLogAvailable_Type = TruthValue
_CircuitPoleSensorLogAvailable_Object = MibTableColumn
circuitPoleSensorLogAvailable = _CircuitPoleSensorLogAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 4),
    _CircuitPoleSensorLogAvailable_Type()
)
circuitPoleSensorLogAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPoleSensorLogAvailable.setStatus("current")
_CircuitPoleSensorUnits_Type = SensorUnitsEnumeration
_CircuitPoleSensorUnits_Object = MibTableColumn
circuitPoleSensorUnits = _CircuitPoleSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 6),
    _CircuitPoleSensorUnits_Type()
)
circuitPoleSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitPoleSensorUnits.setStatus("current")
_CircuitPoleSensorDecimalDigits_Type = Unsigned32
_CircuitPoleSensorDecimalDigits_Object = MibTableColumn
circuitPoleSensorDecimalDigits = _CircuitPoleSensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 7),
    _CircuitPoleSensorDecimalDigits_Type()
)
circuitPoleSensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitPoleSensorDecimalDigits.setStatus("current")
_CircuitPoleSensorResolution_Type = Unsigned32
_CircuitPoleSensorResolution_Object = MibTableColumn
circuitPoleSensorResolution = _CircuitPoleSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 9),
    _CircuitPoleSensorResolution_Type()
)
circuitPoleSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitPoleSensorResolution.setStatus("current")
_CircuitPoleSensorMaximum_Type = Unsigned32
_CircuitPoleSensorMaximum_Object = MibTableColumn
circuitPoleSensorMaximum = _CircuitPoleSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 11),
    _CircuitPoleSensorMaximum_Type()
)
circuitPoleSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitPoleSensorMaximum.setStatus("current")
_CircuitPoleSensorMinimum_Type = Unsigned32
_CircuitPoleSensorMinimum_Object = MibTableColumn
circuitPoleSensorMinimum = _CircuitPoleSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 12),
    _CircuitPoleSensorMinimum_Type()
)
circuitPoleSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitPoleSensorMinimum.setStatus("current")
_CircuitPoleSensorHysteresis_Type = Unsigned32
_CircuitPoleSensorHysteresis_Object = MibTableColumn
circuitPoleSensorHysteresis = _CircuitPoleSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 13),
    _CircuitPoleSensorHysteresis_Type()
)
circuitPoleSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPoleSensorHysteresis.setStatus("current")


class _CircuitPoleSensorStateChangeDelay_Type(Unsigned32):
    """Custom type circuitPoleSensorStateChangeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_CircuitPoleSensorStateChangeDelay_Type.__name__ = "Unsigned32"
_CircuitPoleSensorStateChangeDelay_Object = MibTableColumn
circuitPoleSensorStateChangeDelay = _CircuitPoleSensorStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 14),
    _CircuitPoleSensorStateChangeDelay_Type()
)
circuitPoleSensorStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPoleSensorStateChangeDelay.setStatus("current")
_CircuitPoleSensorLowerCriticalThreshold_Type = Unsigned32
_CircuitPoleSensorLowerCriticalThreshold_Object = MibTableColumn
circuitPoleSensorLowerCriticalThreshold = _CircuitPoleSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 21),
    _CircuitPoleSensorLowerCriticalThreshold_Type()
)
circuitPoleSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPoleSensorLowerCriticalThreshold.setStatus("current")
_CircuitPoleSensorLowerWarningThreshold_Type = Unsigned32
_CircuitPoleSensorLowerWarningThreshold_Object = MibTableColumn
circuitPoleSensorLowerWarningThreshold = _CircuitPoleSensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 22),
    _CircuitPoleSensorLowerWarningThreshold_Type()
)
circuitPoleSensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPoleSensorLowerWarningThreshold.setStatus("current")
_CircuitPoleSensorUpperCriticalThreshold_Type = Unsigned32
_CircuitPoleSensorUpperCriticalThreshold_Object = MibTableColumn
circuitPoleSensorUpperCriticalThreshold = _CircuitPoleSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 23),
    _CircuitPoleSensorUpperCriticalThreshold_Type()
)
circuitPoleSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPoleSensorUpperCriticalThreshold.setStatus("current")
_CircuitPoleSensorUpperWarningThreshold_Type = Unsigned32
_CircuitPoleSensorUpperWarningThreshold_Object = MibTableColumn
circuitPoleSensorUpperWarningThreshold = _CircuitPoleSensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 24),
    _CircuitPoleSensorUpperWarningThreshold_Type()
)
circuitPoleSensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPoleSensorUpperWarningThreshold.setStatus("current")


class _CircuitPoleSensorEnabledThresholds_Type(Bits):
    """Custom type circuitPoleSensorEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_CircuitPoleSensorEnabledThresholds_Type.__name__ = "Bits"
_CircuitPoleSensorEnabledThresholds_Object = MibTableColumn
circuitPoleSensorEnabledThresholds = _CircuitPoleSensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 25),
    _CircuitPoleSensorEnabledThresholds_Type()
)
circuitPoleSensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPoleSensorEnabledThresholds.setStatus("current")
_CircuitPoleSensorSignedMaximum_Type = Integer32
_CircuitPoleSensorSignedMaximum_Object = MibTableColumn
circuitPoleSensorSignedMaximum = _CircuitPoleSensorSignedMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 26),
    _CircuitPoleSensorSignedMaximum_Type()
)
circuitPoleSensorSignedMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitPoleSensorSignedMaximum.setStatus("current")
_CircuitPoleSensorSignedMinimum_Type = Integer32
_CircuitPoleSensorSignedMinimum_Object = MibTableColumn
circuitPoleSensorSignedMinimum = _CircuitPoleSensorSignedMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 27),
    _CircuitPoleSensorSignedMinimum_Type()
)
circuitPoleSensorSignedMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitPoleSensorSignedMinimum.setStatus("current")
_CircuitPoleSensorSignedLowerCriticalThreshold_Type = Integer32
_CircuitPoleSensorSignedLowerCriticalThreshold_Object = MibTableColumn
circuitPoleSensorSignedLowerCriticalThreshold = _CircuitPoleSensorSignedLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 28),
    _CircuitPoleSensorSignedLowerCriticalThreshold_Type()
)
circuitPoleSensorSignedLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPoleSensorSignedLowerCriticalThreshold.setStatus("current")
_CircuitPoleSensorSignedLowerWarningThreshold_Type = Integer32
_CircuitPoleSensorSignedLowerWarningThreshold_Object = MibTableColumn
circuitPoleSensorSignedLowerWarningThreshold = _CircuitPoleSensorSignedLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 29),
    _CircuitPoleSensorSignedLowerWarningThreshold_Type()
)
circuitPoleSensorSignedLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPoleSensorSignedLowerWarningThreshold.setStatus("current")
_CircuitPoleSensorSignedUpperCriticalThreshold_Type = Integer32
_CircuitPoleSensorSignedUpperCriticalThreshold_Object = MibTableColumn
circuitPoleSensorSignedUpperCriticalThreshold = _CircuitPoleSensorSignedUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 30),
    _CircuitPoleSensorSignedUpperCriticalThreshold_Type()
)
circuitPoleSensorSignedUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPoleSensorSignedUpperCriticalThreshold.setStatus("current")
_CircuitPoleSensorSignedUpperWarningThreshold_Type = Integer32
_CircuitPoleSensorSignedUpperWarningThreshold_Object = MibTableColumn
circuitPoleSensorSignedUpperWarningThreshold = _CircuitPoleSensorSignedUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 11, 6, 1, 31),
    _CircuitPoleSensorSignedUpperWarningThreshold_Type()
)
circuitPoleSensorSignedUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPoleSensorSignedUpperWarningThreshold.setStatus("current")
_OutletGroups_ObjectIdentity = ObjectIdentity
outletGroups = _OutletGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12)
)
_OutletGroupConfigurationTable_Object = MibTable
outletGroupConfigurationTable = _OutletGroupConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 2)
)
if mibBuilder.loadTexts:
    outletGroupConfigurationTable.setStatus("current")
_OutletGroupConfigurationEntry_Object = MibTableRow
outletGroupConfigurationEntry = _OutletGroupConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 2, 1)
)
outletGroupConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "outletGroupId"),
)
if mibBuilder.loadTexts:
    outletGroupConfigurationEntry.setStatus("current")


class _OutletGroupId_Type(Integer32):
    """Custom type outletGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_OutletGroupId_Type.__name__ = "Integer32"
_OutletGroupId_Object = MibTableColumn
outletGroupId = _OutletGroupId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 2, 1, 1),
    _OutletGroupId_Type()
)
outletGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outletGroupId.setStatus("current")
_OutletGroupName_Type = DisplayString
_OutletGroupName_Object = MibTableColumn
outletGroupName = _OutletGroupName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 2, 1, 2),
    _OutletGroupName_Type()
)
outletGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupName.setStatus("current")


class _OutletGroupCapabilities_Type(Bits):
    """Custom type outletGroupCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("activePower", 4),
          ("apparentPower", 5),
          ("activeEnergy", 7),
          ("apparentEnergy", 8))
    )

_OutletGroupCapabilities_Type.__name__ = "Bits"
_OutletGroupCapabilities_Object = MibTableColumn
outletGroupCapabilities = _OutletGroupCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 2, 1, 3),
    _OutletGroupCapabilities_Type()
)
outletGroupCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletGroupCapabilities.setStatus("current")
_OutletGroupMembers_Type = DisplayString
_OutletGroupMembers_Object = MibTableColumn
outletGroupMembers = _OutletGroupMembers_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 2, 1, 4),
    _OutletGroupMembers_Type()
)
outletGroupMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupMembers.setStatus("current")
_OutletGroupSensorConfigurationTable_Object = MibTable
outletGroupSensorConfigurationTable = _OutletGroupSensorConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3)
)
if mibBuilder.loadTexts:
    outletGroupSensorConfigurationTable.setStatus("current")
_OutletGroupSensorConfigurationEntry_Object = MibTableRow
outletGroupSensorConfigurationEntry = _OutletGroupSensorConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1)
)
outletGroupSensorConfigurationEntry.setIndexNames(
    (0, "PDU2-MIB", "outletGroupId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    outletGroupSensorConfigurationEntry.setStatus("current")
_OutletGroupSensorLogAvailable_Type = TruthValue
_OutletGroupSensorLogAvailable_Object = MibTableColumn
outletGroupSensorLogAvailable = _OutletGroupSensorLogAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 4),
    _OutletGroupSensorLogAvailable_Type()
)
outletGroupSensorLogAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupSensorLogAvailable.setStatus("current")
_OutletGroupSensorUnits_Type = SensorUnitsEnumeration
_OutletGroupSensorUnits_Object = MibTableColumn
outletGroupSensorUnits = _OutletGroupSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 6),
    _OutletGroupSensorUnits_Type()
)
outletGroupSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletGroupSensorUnits.setStatus("current")
_OutletGroupSensorDecimalDigits_Type = Unsigned32
_OutletGroupSensorDecimalDigits_Object = MibTableColumn
outletGroupSensorDecimalDigits = _OutletGroupSensorDecimalDigits_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 7),
    _OutletGroupSensorDecimalDigits_Type()
)
outletGroupSensorDecimalDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletGroupSensorDecimalDigits.setStatus("current")
_OutletGroupSensorResolution_Type = Unsigned32
_OutletGroupSensorResolution_Object = MibTableColumn
outletGroupSensorResolution = _OutletGroupSensorResolution_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 9),
    _OutletGroupSensorResolution_Type()
)
outletGroupSensorResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletGroupSensorResolution.setStatus("current")
_OutletGroupSensorMaximum_Type = Unsigned32
_OutletGroupSensorMaximum_Object = MibTableColumn
outletGroupSensorMaximum = _OutletGroupSensorMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 11),
    _OutletGroupSensorMaximum_Type()
)
outletGroupSensorMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletGroupSensorMaximum.setStatus("current")
_OutletGroupSensorMinimum_Type = Unsigned32
_OutletGroupSensorMinimum_Object = MibTableColumn
outletGroupSensorMinimum = _OutletGroupSensorMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 12),
    _OutletGroupSensorMinimum_Type()
)
outletGroupSensorMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletGroupSensorMinimum.setStatus("current")
_OutletGroupSensorHysteresis_Type = Unsigned32
_OutletGroupSensorHysteresis_Object = MibTableColumn
outletGroupSensorHysteresis = _OutletGroupSensorHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 13),
    _OutletGroupSensorHysteresis_Type()
)
outletGroupSensorHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupSensorHysteresis.setStatus("current")


class _OutletGroupSensorStateChangeDelay_Type(Unsigned32):
    """Custom type outletGroupSensorStateChangeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_OutletGroupSensorStateChangeDelay_Type.__name__ = "Unsigned32"
_OutletGroupSensorStateChangeDelay_Object = MibTableColumn
outletGroupSensorStateChangeDelay = _OutletGroupSensorStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 14),
    _OutletGroupSensorStateChangeDelay_Type()
)
outletGroupSensorStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupSensorStateChangeDelay.setStatus("current")
_OutletGroupSensorLowerCriticalThreshold_Type = Unsigned32
_OutletGroupSensorLowerCriticalThreshold_Object = MibTableColumn
outletGroupSensorLowerCriticalThreshold = _OutletGroupSensorLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 21),
    _OutletGroupSensorLowerCriticalThreshold_Type()
)
outletGroupSensorLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupSensorLowerCriticalThreshold.setStatus("current")
_OutletGroupSensorLowerWarningThreshold_Type = Unsigned32
_OutletGroupSensorLowerWarningThreshold_Object = MibTableColumn
outletGroupSensorLowerWarningThreshold = _OutletGroupSensorLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 22),
    _OutletGroupSensorLowerWarningThreshold_Type()
)
outletGroupSensorLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupSensorLowerWarningThreshold.setStatus("current")
_OutletGroupSensorUpperCriticalThreshold_Type = Unsigned32
_OutletGroupSensorUpperCriticalThreshold_Object = MibTableColumn
outletGroupSensorUpperCriticalThreshold = _OutletGroupSensorUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 23),
    _OutletGroupSensorUpperCriticalThreshold_Type()
)
outletGroupSensorUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupSensorUpperCriticalThreshold.setStatus("current")
_OutletGroupSensorUpperWarningThreshold_Type = Unsigned32
_OutletGroupSensorUpperWarningThreshold_Object = MibTableColumn
outletGroupSensorUpperWarningThreshold = _OutletGroupSensorUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 24),
    _OutletGroupSensorUpperWarningThreshold_Type()
)
outletGroupSensorUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupSensorUpperWarningThreshold.setStatus("current")


class _OutletGroupSensorEnabledThresholds_Type(Bits):
    """Custom type outletGroupSensorEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_OutletGroupSensorEnabledThresholds_Type.__name__ = "Bits"
_OutletGroupSensorEnabledThresholds_Object = MibTableColumn
outletGroupSensorEnabledThresholds = _OutletGroupSensorEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 25),
    _OutletGroupSensorEnabledThresholds_Type()
)
outletGroupSensorEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupSensorEnabledThresholds.setStatus("current")
_OutletGroupSensorSignedMaximum_Type = Integer32
_OutletGroupSensorSignedMaximum_Object = MibTableColumn
outletGroupSensorSignedMaximum = _OutletGroupSensorSignedMaximum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 26),
    _OutletGroupSensorSignedMaximum_Type()
)
outletGroupSensorSignedMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletGroupSensorSignedMaximum.setStatus("current")
_OutletGroupSensorSignedMinimum_Type = Integer32
_OutletGroupSensorSignedMinimum_Object = MibTableColumn
outletGroupSensorSignedMinimum = _OutletGroupSensorSignedMinimum_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 27),
    _OutletGroupSensorSignedMinimum_Type()
)
outletGroupSensorSignedMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletGroupSensorSignedMinimum.setStatus("current")
_OutletGroupSensorSignedLowerCriticalThreshold_Type = Integer32
_OutletGroupSensorSignedLowerCriticalThreshold_Object = MibTableColumn
outletGroupSensorSignedLowerCriticalThreshold = _OutletGroupSensorSignedLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 28),
    _OutletGroupSensorSignedLowerCriticalThreshold_Type()
)
outletGroupSensorSignedLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupSensorSignedLowerCriticalThreshold.setStatus("current")
_OutletGroupSensorSignedLowerWarningThreshold_Type = Integer32
_OutletGroupSensorSignedLowerWarningThreshold_Object = MibTableColumn
outletGroupSensorSignedLowerWarningThreshold = _OutletGroupSensorSignedLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 29),
    _OutletGroupSensorSignedLowerWarningThreshold_Type()
)
outletGroupSensorSignedLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupSensorSignedLowerWarningThreshold.setStatus("current")
_OutletGroupSensorSignedUpperCriticalThreshold_Type = Integer32
_OutletGroupSensorSignedUpperCriticalThreshold_Object = MibTableColumn
outletGroupSensorSignedUpperCriticalThreshold = _OutletGroupSensorSignedUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 30),
    _OutletGroupSensorSignedUpperCriticalThreshold_Type()
)
outletGroupSensorSignedUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupSensorSignedUpperCriticalThreshold.setStatus("current")
_OutletGroupSensorSignedUpperWarningThreshold_Type = Integer32
_OutletGroupSensorSignedUpperWarningThreshold_Object = MibTableColumn
outletGroupSensorSignedUpperWarningThreshold = _OutletGroupSensorSignedUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 3, 12, 3, 1, 31),
    _OutletGroupSensorSignedUpperWarningThreshold_Type()
)
outletGroupSensorSignedUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupSensorSignedUpperWarningThreshold.setStatus("current")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4)
)
_OutletControl_ObjectIdentity = ObjectIdentity
outletControl = _OutletControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 1)
)
_OutletSwitchControlTable_Object = MibTable
outletSwitchControlTable = _OutletSwitchControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    outletSwitchControlTable.setStatus("current")
_OutletSwitchControlEntry_Object = MibTableRow
outletSwitchControlEntry = _OutletSwitchControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 1, 2, 1)
)
outletSwitchControlEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "outletId"),
)
if mibBuilder.loadTexts:
    outletSwitchControlEntry.setStatus("current")
_SwitchingOperation_Type = OutletSwitchingOperationsEnumeration
_SwitchingOperation_Object = MibTableColumn
switchingOperation = _SwitchingOperation_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 1, 2, 1, 2),
    _SwitchingOperation_Type()
)
switchingOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchingOperation.setStatus("current")
_OutletSwitchingState_Type = SensorStateEnumeration
_OutletSwitchingState_Object = MibTableColumn
outletSwitchingState = _OutletSwitchingState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 1, 2, 1, 3),
    _OutletSwitchingState_Type()
)
outletSwitchingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSwitchingState.setStatus("current")
_OutletSwitchingTimeStamp_Type = Unsigned32
_OutletSwitchingTimeStamp_Object = MibTableColumn
outletSwitchingTimeStamp = _OutletSwitchingTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 1, 2, 1, 4),
    _OutletSwitchingTimeStamp_Type()
)
outletSwitchingTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSwitchingTimeStamp.setStatus("current")
_OutletSuspendedState_Type = TruthValue
_OutletSuspendedState_Object = MibTableColumn
outletSuspendedState = _OutletSuspendedState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 1, 2, 1, 5),
    _OutletSuspendedState_Type()
)
outletSuspendedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSuspendedState.setStatus("current")
_ExternalSensorControl_ObjectIdentity = ObjectIdentity
externalSensorControl = _ExternalSensorControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 2)
)
_ExternalSensorControlTable_Object = MibTable
externalSensorControlTable = _ExternalSensorControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    externalSensorControlTable.setStatus("current")
_ExternalSensorControlEntry_Object = MibTableRow
externalSensorControlEntry = _ExternalSensorControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 2, 1, 1)
)
externalSensorControlEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "sensorID"),
)
if mibBuilder.loadTexts:
    externalSensorControlEntry.setStatus("current")
_ExternalSensorResetMinMax_Type = TruthValue
_ExternalSensorResetMinMax_Object = MibTableColumn
externalSensorResetMinMax = _ExternalSensorResetMinMax_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 2, 1, 1, 2),
    _ExternalSensorResetMinMax_Type()
)
externalSensorResetMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalSensorResetMinMax.setStatus("current")
_TransferSwitchControl_ObjectIdentity = ObjectIdentity
transferSwitchControl = _TransferSwitchControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 3)
)
_TransferSwitchControlTable_Object = MibTable
transferSwitchControlTable = _TransferSwitchControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 3, 1)
)
if mibBuilder.loadTexts:
    transferSwitchControlTable.setStatus("current")
_TransferSwitchControlEntry_Object = MibTableRow
transferSwitchControlEntry = _TransferSwitchControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 3, 1, 1)
)
transferSwitchControlEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "transferSwitchId"),
)
if mibBuilder.loadTexts:
    transferSwitchControlEntry.setStatus("current")


class _TransferSwitchActiveInlet_Type(Integer32):
    """Custom type transferSwitchActiveInlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_TransferSwitchActiveInlet_Type.__name__ = "Integer32"
_TransferSwitchActiveInlet_Object = MibTableColumn
transferSwitchActiveInlet = _TransferSwitchActiveInlet_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 3, 1, 1, 1),
    _TransferSwitchActiveInlet_Type()
)
transferSwitchActiveInlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchActiveInlet.setStatus("current")


class _TransferSwitchTransferToInlet_Type(Integer32):
    """Custom type transferSwitchTransferToInlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_TransferSwitchTransferToInlet_Type.__name__ = "Integer32"
_TransferSwitchTransferToInlet_Object = MibTableColumn
transferSwitchTransferToInlet = _TransferSwitchTransferToInlet_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 3, 1, 1, 2),
    _TransferSwitchTransferToInlet_Type()
)
transferSwitchTransferToInlet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchTransferToInlet.setStatus("current")
_TransferSwitchAlarmOverride_Type = TruthValue
_TransferSwitchAlarmOverride_Object = MibTableColumn
transferSwitchAlarmOverride = _TransferSwitchAlarmOverride_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 3, 1, 1, 3),
    _TransferSwitchAlarmOverride_Type()
)
transferSwitchAlarmOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchAlarmOverride.setStatus("current")
_TransferSwitchLastTransferReason_Type = TransferSwitchTransferReasonEnumeration
_TransferSwitchLastTransferReason_Object = MibTableColumn
transferSwitchLastTransferReason = _TransferSwitchLastTransferReason_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 3, 1, 1, 4),
    _TransferSwitchLastTransferReason_Type()
)
transferSwitchLastTransferReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferSwitchLastTransferReason.setStatus("current")
_ActuatorControl_ObjectIdentity = ObjectIdentity
actuatorControl = _ActuatorControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 4)
)
_ActuatorControlTable_Object = MibTable
actuatorControlTable = _ActuatorControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 4, 2)
)
if mibBuilder.loadTexts:
    actuatorControlTable.setStatus("current")
_ActuatorControlEntry_Object = MibTableRow
actuatorControlEntry = _ActuatorControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 4, 2, 1)
)
actuatorControlEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "sensorID"),
)
if mibBuilder.loadTexts:
    actuatorControlEntry.setStatus("current")
_ActuatorState_Type = SensorStateEnumeration
_ActuatorState_Object = MibTableColumn
actuatorState = _ActuatorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 4, 2, 1, 2),
    _ActuatorState_Type()
)
actuatorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actuatorState.setStatus("current")
_RcmControl_ObjectIdentity = ObjectIdentity
rcmControl = _RcmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 5)
)
_RcmSelfTestTable_Object = MibTable
rcmSelfTestTable = _RcmSelfTestTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 5, 2)
)
if mibBuilder.loadTexts:
    rcmSelfTestTable.setStatus("current")
_RcmSelfTestEntry_Object = MibTableRow
rcmSelfTestEntry = _RcmSelfTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 5, 2, 1)
)
rcmSelfTestEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
)
if mibBuilder.loadTexts:
    rcmSelfTestEntry.setStatus("current")
_RcmState_Type = SensorStateEnumeration
_RcmState_Object = MibTableColumn
rcmState = _RcmState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 5, 2, 1, 2),
    _RcmState_Type()
)
rcmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcmState.setStatus("current")
_OverCurrentProtectorRcmSelfTestTable_Object = MibTable
overCurrentProtectorRcmSelfTestTable = _OverCurrentProtectorRcmSelfTestTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 5, 3)
)
if mibBuilder.loadTexts:
    overCurrentProtectorRcmSelfTestTable.setStatus("current")
_OverCurrentProtectorRcmSelfTestEntry_Object = MibTableRow
overCurrentProtectorRcmSelfTestEntry = _OverCurrentProtectorRcmSelfTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 5, 3, 1)
)
overCurrentProtectorRcmSelfTestEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "overCurrentProtectorIndex"),
)
if mibBuilder.loadTexts:
    overCurrentProtectorRcmSelfTestEntry.setStatus("current")
_OverCurrentProtectorRcmState_Type = SensorStateEnumeration
_OverCurrentProtectorRcmState_Object = MibTableColumn
overCurrentProtectorRcmState = _OverCurrentProtectorRcmState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 5, 3, 1, 2),
    _OverCurrentProtectorRcmState_Type()
)
overCurrentProtectorRcmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overCurrentProtectorRcmState.setStatus("current")
_InletSensorControl_ObjectIdentity = ObjectIdentity
inletSensorControl = _InletSensorControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 6)
)
_InletSensorControlTable_Object = MibTable
inletSensorControlTable = _InletSensorControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 6, 1)
)
if mibBuilder.loadTexts:
    inletSensorControlTable.setStatus("current")
_InletSensorControlEntry_Object = MibTableRow
inletSensorControlEntry = _InletSensorControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 6, 1, 1)
)
inletSensorControlEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    inletSensorControlEntry.setStatus("current")
_InletSensorResetValue_Type = Integer32
_InletSensorResetValue_Object = MibTableColumn
inletSensorResetValue = _InletSensorResetValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 6, 1, 1, 1),
    _InletSensorResetValue_Type()
)
inletSensorResetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletSensorResetValue.setStatus("current")
_InletSensorResetMinMax_Type = TruthValue
_InletSensorResetMinMax_Object = MibTableColumn
inletSensorResetMinMax = _InletSensorResetMinMax_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 6, 1, 1, 2),
    _InletSensorResetMinMax_Type()
)
inletSensorResetMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletSensorResetMinMax.setStatus("current")
_InletPoleSensorControlTable_Object = MibTable
inletPoleSensorControlTable = _InletPoleSensorControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 6, 2)
)
if mibBuilder.loadTexts:
    inletPoleSensorControlTable.setStatus("current")
_InletPoleSensorControlEntry_Object = MibTableRow
inletPoleSensorControlEntry = _InletPoleSensorControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 6, 2, 1)
)
inletPoleSensorControlEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
    (0, "PDU2-MIB", "inletPoleIndex"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    inletPoleSensorControlEntry.setStatus("current")
_InletPoleSensorResetMinMax_Type = TruthValue
_InletPoleSensorResetMinMax_Object = MibTableColumn
inletPoleSensorResetMinMax = _InletPoleSensorResetMinMax_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 6, 2, 1, 2),
    _InletPoleSensorResetMinMax_Type()
)
inletPoleSensorResetMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletPoleSensorResetMinMax.setStatus("current")
_InletLinePairSensorControlTable_Object = MibTable
inletLinePairSensorControlTable = _InletLinePairSensorControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 6, 3)
)
if mibBuilder.loadTexts:
    inletLinePairSensorControlTable.setStatus("current")
_InletLinePairSensorControlEntry_Object = MibTableRow
inletLinePairSensorControlEntry = _InletLinePairSensorControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 6, 3, 1)
)
inletLinePairSensorControlEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
    (0, "PDU2-MIB", "inletLinePairIndex"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    inletLinePairSensorControlEntry.setStatus("current")
_InletLinePairSensorResetMinMax_Type = TruthValue
_InletLinePairSensorResetMinMax_Object = MibTableColumn
inletLinePairSensorResetMinMax = _InletLinePairSensorResetMinMax_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 6, 3, 1, 2),
    _InletLinePairSensorResetMinMax_Type()
)
inletLinePairSensorResetMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inletLinePairSensorResetMinMax.setStatus("current")
_OutletSensorControl_ObjectIdentity = ObjectIdentity
outletSensorControl = _OutletSensorControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 7)
)
_OutletSensorControlTable_Object = MibTable
outletSensorControlTable = _OutletSensorControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 7, 1)
)
if mibBuilder.loadTexts:
    outletSensorControlTable.setStatus("current")
_OutletSensorControlEntry_Object = MibTableRow
outletSensorControlEntry = _OutletSensorControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 7, 1, 1)
)
outletSensorControlEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "outletId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    outletSensorControlEntry.setStatus("current")
_OutletSensorResetValue_Type = Integer32
_OutletSensorResetValue_Object = MibTableColumn
outletSensorResetValue = _OutletSensorResetValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 7, 1, 1, 1),
    _OutletSensorResetValue_Type()
)
outletSensorResetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSensorResetValue.setStatus("current")
_OutletSensorResetMinMax_Type = TruthValue
_OutletSensorResetMinMax_Object = MibTableColumn
outletSensorResetMinMax = _OutletSensorResetMinMax_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 7, 1, 1, 2),
    _OutletSensorResetMinMax_Type()
)
outletSensorResetMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletSensorResetMinMax.setStatus("current")
_OutletPoleSensorControlTable_Object = MibTable
outletPoleSensorControlTable = _OutletPoleSensorControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 7, 2)
)
if mibBuilder.loadTexts:
    outletPoleSensorControlTable.setStatus("current")
_OutletPoleSensorControlEntry_Object = MibTableRow
outletPoleSensorControlEntry = _OutletPoleSensorControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 7, 2, 1)
)
outletPoleSensorControlEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "outletId"),
    (0, "PDU2-MIB", "outletPoleIndex"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    outletPoleSensorControlEntry.setStatus("current")
_OutletPoleSensorResetMinMax_Type = TruthValue
_OutletPoleSensorResetMinMax_Object = MibTableColumn
outletPoleSensorResetMinMax = _OutletPoleSensorResetMinMax_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 7, 2, 1, 2),
    _OutletPoleSensorResetMinMax_Type()
)
outletPoleSensorResetMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletPoleSensorResetMinMax.setStatus("current")
_UnitSensorControl_ObjectIdentity = ObjectIdentity
unitSensorControl = _UnitSensorControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 8)
)
_UnitSensorControlTable_Object = MibTable
unitSensorControlTable = _UnitSensorControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 8, 1)
)
if mibBuilder.loadTexts:
    unitSensorControlTable.setStatus("current")
_UnitSensorControlEntry_Object = MibTableRow
unitSensorControlEntry = _UnitSensorControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 8, 1, 1)
)
unitSensorControlEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    unitSensorControlEntry.setStatus("current")
_UnitSensorResetValue_Type = Integer32
_UnitSensorResetValue_Object = MibTableColumn
unitSensorResetValue = _UnitSensorResetValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 8, 1, 1, 1),
    _UnitSensorResetValue_Type()
)
unitSensorResetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSensorResetValue.setStatus("current")
_UnitSensorResetMinMax_Type = TruthValue
_UnitSensorResetMinMax_Object = MibTableColumn
unitSensorResetMinMax = _UnitSensorResetMinMax_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 8, 1, 1, 2),
    _UnitSensorResetMinMax_Type()
)
unitSensorResetMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSensorResetMinMax.setStatus("current")
_CircuitSensorControl_ObjectIdentity = ObjectIdentity
circuitSensorControl = _CircuitSensorControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 9)
)
_CircuitSensorControlTable_Object = MibTable
circuitSensorControlTable = _CircuitSensorControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 9, 1)
)
if mibBuilder.loadTexts:
    circuitSensorControlTable.setStatus("current")
_CircuitSensorControlEntry_Object = MibTableRow
circuitSensorControlEntry = _CircuitSensorControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 9, 1, 1)
)
circuitSensorControlEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "circuitId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    circuitSensorControlEntry.setStatus("current")
_CircuitSensorResetValue_Type = Integer32
_CircuitSensorResetValue_Object = MibTableColumn
circuitSensorResetValue = _CircuitSensorResetValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 9, 1, 1, 1),
    _CircuitSensorResetValue_Type()
)
circuitSensorResetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSensorResetValue.setStatus("current")
_CircuitSensorResetMinMax_Type = TruthValue
_CircuitSensorResetMinMax_Object = MibTableColumn
circuitSensorResetMinMax = _CircuitSensorResetMinMax_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 9, 1, 1, 2),
    _CircuitSensorResetMinMax_Type()
)
circuitSensorResetMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSensorResetMinMax.setStatus("current")
_CircuitPoleSensorControlTable_Object = MibTable
circuitPoleSensorControlTable = _CircuitPoleSensorControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 9, 2)
)
if mibBuilder.loadTexts:
    circuitPoleSensorControlTable.setStatus("current")
_CircuitPoleSensorControlEntry_Object = MibTableRow
circuitPoleSensorControlEntry = _CircuitPoleSensorControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 9, 2, 1)
)
circuitPoleSensorControlEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "circuitId"),
    (0, "PDU2-MIB", "circuitPoleId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    circuitPoleSensorControlEntry.setStatus("current")
_CircuitPoleSensorResetMinMax_Type = TruthValue
_CircuitPoleSensorResetMinMax_Object = MibTableColumn
circuitPoleSensorResetMinMax = _CircuitPoleSensorResetMinMax_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 9, 2, 1, 2),
    _CircuitPoleSensorResetMinMax_Type()
)
circuitPoleSensorResetMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPoleSensorResetMinMax.setStatus("current")
_OutletGroupControl_ObjectIdentity = ObjectIdentity
outletGroupControl = _OutletGroupControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 10)
)
_OutletGroupSwitchControlTable_Object = MibTable
outletGroupSwitchControlTable = _OutletGroupSwitchControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 10, 2)
)
if mibBuilder.loadTexts:
    outletGroupSwitchControlTable.setStatus("current")
_OutletGroupSwitchControlEntry_Object = MibTableRow
outletGroupSwitchControlEntry = _OutletGroupSwitchControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 10, 2, 1)
)
outletGroupSwitchControlEntry.setIndexNames(
    (0, "PDU2-MIB", "outletGroupId"),
)
if mibBuilder.loadTexts:
    outletGroupSwitchControlEntry.setStatus("current")
_OutletGroupSwitchingOperation_Type = OutletSwitchingOperationsEnumeration
_OutletGroupSwitchingOperation_Object = MibTableColumn
outletGroupSwitchingOperation = _OutletGroupSwitchingOperation_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 10, 2, 1, 2),
    _OutletGroupSwitchingOperation_Type()
)
outletGroupSwitchingOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupSwitchingOperation.setStatus("current")
_OutletGroupSensorControl_ObjectIdentity = ObjectIdentity
outletGroupSensorControl = _OutletGroupSensorControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 11)
)
_OutletGroupSensorControlTable_Object = MibTable
outletGroupSensorControlTable = _OutletGroupSensorControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 11, 1)
)
if mibBuilder.loadTexts:
    outletGroupSensorControlTable.setStatus("current")
_OutletGroupSensorControlEntry_Object = MibTableRow
outletGroupSensorControlEntry = _OutletGroupSensorControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 11, 1, 1)
)
outletGroupSensorControlEntry.setIndexNames(
    (0, "PDU2-MIB", "outletGroupId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    outletGroupSensorControlEntry.setStatus("current")
_OutletGroupSensorResetValue_Type = Integer32
_OutletGroupSensorResetValue_Object = MibTableColumn
outletGroupSensorResetValue = _OutletGroupSensorResetValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 11, 1, 1, 1),
    _OutletGroupSensorResetValue_Type()
)
outletGroupSensorResetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupSensorResetValue.setStatus("current")
_OutletGroupSensorResetMinMax_Type = TruthValue
_OutletGroupSensorResetMinMax_Object = MibTableColumn
outletGroupSensorResetMinMax = _OutletGroupSensorResetMinMax_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 11, 1, 1, 2),
    _OutletGroupSensorResetMinMax_Type()
)
outletGroupSensorResetMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletGroupSensorResetMinMax.setStatus("current")
_ServerPowerControl_ObjectIdentity = ObjectIdentity
serverPowerControl = _ServerPowerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 12)
)
_ServerPowerControlTable_Object = MibTable
serverPowerControlTable = _ServerPowerControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 12, 1)
)
if mibBuilder.loadTexts:
    serverPowerControlTable.setStatus("current")
_ServerPowerControlEntry_Object = MibTableRow
serverPowerControlEntry = _ServerPowerControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 12, 1, 1)
)
serverPowerControlEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "serverID"),
)
if mibBuilder.loadTexts:
    serverPowerControlEntry.setStatus("current")
_ServerPowerControlOperation_Type = ServerPowerStateEnumeration
_ServerPowerControlOperation_Object = MibTableColumn
serverPowerControlOperation = _ServerPowerControlOperation_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 12, 1, 1, 1),
    _ServerPowerControlOperation_Type()
)
serverPowerControlOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverPowerControlOperation.setStatus("current")
_OverCurrentProtectorSensorControl_ObjectIdentity = ObjectIdentity
overCurrentProtectorSensorControl = _OverCurrentProtectorSensorControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 13)
)
_OverCurrentProtectorSensorControlTable_Object = MibTable
overCurrentProtectorSensorControlTable = _OverCurrentProtectorSensorControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 13, 1)
)
if mibBuilder.loadTexts:
    overCurrentProtectorSensorControlTable.setStatus("current")
_OverCurrentProtectorSensorControlEntry_Object = MibTableRow
overCurrentProtectorSensorControlEntry = _OverCurrentProtectorSensorControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 13, 1, 1)
)
overCurrentProtectorSensorControlEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "overCurrentProtectorIndex"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    overCurrentProtectorSensorControlEntry.setStatus("current")
_OverCurrentProtectorSensorResetMinMax_Type = TruthValue
_OverCurrentProtectorSensorResetMinMax_Object = MibTableColumn
overCurrentProtectorSensorResetMinMax = _OverCurrentProtectorSensorResetMinMax_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 13, 1, 1, 2),
    _OverCurrentProtectorSensorResetMinMax_Type()
)
overCurrentProtectorSensorResetMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overCurrentProtectorSensorResetMinMax.setStatus("current")
_TransferSwitchSensorControl_ObjectIdentity = ObjectIdentity
transferSwitchSensorControl = _TransferSwitchSensorControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 14)
)
_TransferSwitchSensorControlTable_Object = MibTable
transferSwitchSensorControlTable = _TransferSwitchSensorControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 14, 1)
)
if mibBuilder.loadTexts:
    transferSwitchSensorControlTable.setStatus("current")
_TransferSwitchSensorControlEntry_Object = MibTableRow
transferSwitchSensorControlEntry = _TransferSwitchSensorControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 14, 1, 1)
)
transferSwitchSensorControlEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "transferSwitchId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    transferSwitchSensorControlEntry.setStatus("current")
_TransferSwitchSensorResetMinMax_Type = TruthValue
_TransferSwitchSensorResetMinMax_Object = MibTableColumn
transferSwitchSensorResetMinMax = _TransferSwitchSensorResetMinMax_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 4, 14, 1, 1, 2),
    _TransferSwitchSensorResetMinMax_Type()
)
transferSwitchSensorResetMinMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferSwitchSensorResetMinMax.setStatus("current")
_Measurements_ObjectIdentity = ObjectIdentity
measurements = _Measurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5)
)
_MeasurementsUnit_ObjectIdentity = ObjectIdentity
measurementsUnit = _MeasurementsUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1)
)
_UnitSensorMeasurementsTable_Object = MibTable
unitSensorMeasurementsTable = _UnitSensorMeasurementsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3)
)
if mibBuilder.loadTexts:
    unitSensorMeasurementsTable.setStatus("current")
_UnitSensorMeasurementsEntry_Object = MibTableRow
unitSensorMeasurementsEntry = _UnitSensorMeasurementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3, 1)
)
unitSensorMeasurementsEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    unitSensorMeasurementsEntry.setStatus("current")
_MeasurementsUnitSensorIsAvailable_Type = TruthValue
_MeasurementsUnitSensorIsAvailable_Object = MibTableColumn
measurementsUnitSensorIsAvailable = _MeasurementsUnitSensorIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3, 1, 2),
    _MeasurementsUnitSensorIsAvailable_Type()
)
measurementsUnitSensorIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsUnitSensorIsAvailable.setStatus("current")
_MeasurementsUnitSensorState_Type = SensorStateEnumeration
_MeasurementsUnitSensorState_Object = MibTableColumn
measurementsUnitSensorState = _MeasurementsUnitSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3, 1, 3),
    _MeasurementsUnitSensorState_Type()
)
measurementsUnitSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsUnitSensorState.setStatus("current")
_MeasurementsUnitSensorValue_Type = Unsigned32
_MeasurementsUnitSensorValue_Object = MibTableColumn
measurementsUnitSensorValue = _MeasurementsUnitSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3, 1, 4),
    _MeasurementsUnitSensorValue_Type()
)
measurementsUnitSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsUnitSensorValue.setStatus("current")
_MeasurementsUnitSensorTimeStamp_Type = Unsigned32
_MeasurementsUnitSensorTimeStamp_Object = MibTableColumn
measurementsUnitSensorTimeStamp = _MeasurementsUnitSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3, 1, 5),
    _MeasurementsUnitSensorTimeStamp_Type()
)
measurementsUnitSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsUnitSensorTimeStamp.setStatus("current")
_MeasurementsUnitSensorSignedValue_Type = Integer32
_MeasurementsUnitSensorSignedValue_Object = MibTableColumn
measurementsUnitSensorSignedValue = _MeasurementsUnitSensorSignedValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3, 1, 6),
    _MeasurementsUnitSensorSignedValue_Type()
)
measurementsUnitSensorSignedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsUnitSensorSignedValue.setStatus("current")
_MeasurementsUnitSensorMinMaxValid_Type = TruthValue
_MeasurementsUnitSensorMinMaxValid_Object = MibTableColumn
measurementsUnitSensorMinMaxValid = _MeasurementsUnitSensorMinMaxValid_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3, 1, 7),
    _MeasurementsUnitSensorMinMaxValid_Type()
)
measurementsUnitSensorMinMaxValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsUnitSensorMinMaxValid.setStatus("current")
_MeasurementsUnitSensorMinValue_Type = Unsigned32
_MeasurementsUnitSensorMinValue_Object = MibTableColumn
measurementsUnitSensorMinValue = _MeasurementsUnitSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3, 1, 8),
    _MeasurementsUnitSensorMinValue_Type()
)
measurementsUnitSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsUnitSensorMinValue.setStatus("current")
_MeasurementsUnitSensorSignedMinValue_Type = Integer32
_MeasurementsUnitSensorSignedMinValue_Object = MibTableColumn
measurementsUnitSensorSignedMinValue = _MeasurementsUnitSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3, 1, 9),
    _MeasurementsUnitSensorSignedMinValue_Type()
)
measurementsUnitSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsUnitSensorSignedMinValue.setStatus("current")
_MeasurementsUnitSensorMinTimeStamp_Type = Unsigned32
_MeasurementsUnitSensorMinTimeStamp_Object = MibTableColumn
measurementsUnitSensorMinTimeStamp = _MeasurementsUnitSensorMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3, 1, 10),
    _MeasurementsUnitSensorMinTimeStamp_Type()
)
measurementsUnitSensorMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsUnitSensorMinTimeStamp.setStatus("current")
_MeasurementsUnitSensorMaxValue_Type = Unsigned32
_MeasurementsUnitSensorMaxValue_Object = MibTableColumn
measurementsUnitSensorMaxValue = _MeasurementsUnitSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3, 1, 11),
    _MeasurementsUnitSensorMaxValue_Type()
)
measurementsUnitSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsUnitSensorMaxValue.setStatus("current")
_MeasurementsUnitSensorSignedMaxValue_Type = Integer32
_MeasurementsUnitSensorSignedMaxValue_Object = MibTableColumn
measurementsUnitSensorSignedMaxValue = _MeasurementsUnitSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3, 1, 12),
    _MeasurementsUnitSensorSignedMaxValue_Type()
)
measurementsUnitSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsUnitSensorSignedMaxValue.setStatus("current")
_MeasurementsUnitSensorMaxTimeStamp_Type = Unsigned32
_MeasurementsUnitSensorMaxTimeStamp_Object = MibTableColumn
measurementsUnitSensorMaxTimeStamp = _MeasurementsUnitSensorMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3, 1, 13),
    _MeasurementsUnitSensorMaxTimeStamp_Type()
)
measurementsUnitSensorMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsUnitSensorMaxTimeStamp.setStatus("current")
_MeasurementsUnitSensorMinMaxResetTimeStamp_Type = Unsigned32
_MeasurementsUnitSensorMinMaxResetTimeStamp_Object = MibTableColumn
measurementsUnitSensorMinMaxResetTimeStamp = _MeasurementsUnitSensorMinMaxResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3, 1, 14),
    _MeasurementsUnitSensorMinMaxResetTimeStamp_Type()
)
measurementsUnitSensorMinMaxResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsUnitSensorMinMaxResetTimeStamp.setStatus("current")
_MeasurementsUnitSensorResetTimeStamp_Type = Unsigned32
_MeasurementsUnitSensorResetTimeStamp_Object = MibTableColumn
measurementsUnitSensorResetTimeStamp = _MeasurementsUnitSensorResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 1, 3, 1, 15),
    _MeasurementsUnitSensorResetTimeStamp_Type()
)
measurementsUnitSensorResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsUnitSensorResetTimeStamp.setStatus("current")
_MeasurementsInlet_ObjectIdentity = ObjectIdentity
measurementsInlet = _MeasurementsInlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2)
)
_InletSensorMeasurementsTable_Object = MibTable
inletSensorMeasurementsTable = _InletSensorMeasurementsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3)
)
if mibBuilder.loadTexts:
    inletSensorMeasurementsTable.setStatus("current")
_InletSensorMeasurementsEntry_Object = MibTableRow
inletSensorMeasurementsEntry = _InletSensorMeasurementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3, 1)
)
inletSensorMeasurementsEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    inletSensorMeasurementsEntry.setStatus("current")
_MeasurementsInletSensorIsAvailable_Type = TruthValue
_MeasurementsInletSensorIsAvailable_Object = MibTableColumn
measurementsInletSensorIsAvailable = _MeasurementsInletSensorIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3, 1, 2),
    _MeasurementsInletSensorIsAvailable_Type()
)
measurementsInletSensorIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletSensorIsAvailable.setStatus("current")
_MeasurementsInletSensorState_Type = SensorStateEnumeration
_MeasurementsInletSensorState_Object = MibTableColumn
measurementsInletSensorState = _MeasurementsInletSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3, 1, 3),
    _MeasurementsInletSensorState_Type()
)
measurementsInletSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletSensorState.setStatus("current")
_MeasurementsInletSensorValue_Type = Unsigned32
_MeasurementsInletSensorValue_Object = MibTableColumn
measurementsInletSensorValue = _MeasurementsInletSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3, 1, 4),
    _MeasurementsInletSensorValue_Type()
)
measurementsInletSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletSensorValue.setStatus("current")
_MeasurementsInletSensorTimeStamp_Type = Unsigned32
_MeasurementsInletSensorTimeStamp_Object = MibTableColumn
measurementsInletSensorTimeStamp = _MeasurementsInletSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3, 1, 5),
    _MeasurementsInletSensorTimeStamp_Type()
)
measurementsInletSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletSensorTimeStamp.setStatus("current")
_MeasurementsInletSensorSignedValue_Type = Integer32
_MeasurementsInletSensorSignedValue_Object = MibTableColumn
measurementsInletSensorSignedValue = _MeasurementsInletSensorSignedValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3, 1, 6),
    _MeasurementsInletSensorSignedValue_Type()
)
measurementsInletSensorSignedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletSensorSignedValue.setStatus("current")
_MeasurementsInletSensorMinMaxValid_Type = TruthValue
_MeasurementsInletSensorMinMaxValid_Object = MibTableColumn
measurementsInletSensorMinMaxValid = _MeasurementsInletSensorMinMaxValid_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3, 1, 7),
    _MeasurementsInletSensorMinMaxValid_Type()
)
measurementsInletSensorMinMaxValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletSensorMinMaxValid.setStatus("current")
_MeasurementsInletSensorMinValue_Type = Unsigned32
_MeasurementsInletSensorMinValue_Object = MibTableColumn
measurementsInletSensorMinValue = _MeasurementsInletSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3, 1, 8),
    _MeasurementsInletSensorMinValue_Type()
)
measurementsInletSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletSensorMinValue.setStatus("current")
_MeasurementsInletSensorSignedMinValue_Type = Integer32
_MeasurementsInletSensorSignedMinValue_Object = MibTableColumn
measurementsInletSensorSignedMinValue = _MeasurementsInletSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3, 1, 9),
    _MeasurementsInletSensorSignedMinValue_Type()
)
measurementsInletSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletSensorSignedMinValue.setStatus("current")
_MeasurementsInletSensorMinTimeStamp_Type = Unsigned32
_MeasurementsInletSensorMinTimeStamp_Object = MibTableColumn
measurementsInletSensorMinTimeStamp = _MeasurementsInletSensorMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3, 1, 10),
    _MeasurementsInletSensorMinTimeStamp_Type()
)
measurementsInletSensorMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletSensorMinTimeStamp.setStatus("current")
_MeasurementsInletSensorMaxValue_Type = Unsigned32
_MeasurementsInletSensorMaxValue_Object = MibTableColumn
measurementsInletSensorMaxValue = _MeasurementsInletSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3, 1, 11),
    _MeasurementsInletSensorMaxValue_Type()
)
measurementsInletSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletSensorMaxValue.setStatus("current")
_MeasurementsInletSensorSignedMaxValue_Type = Integer32
_MeasurementsInletSensorSignedMaxValue_Object = MibTableColumn
measurementsInletSensorSignedMaxValue = _MeasurementsInletSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3, 1, 12),
    _MeasurementsInletSensorSignedMaxValue_Type()
)
measurementsInletSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletSensorSignedMaxValue.setStatus("current")
_MeasurementsInletSensorMaxTimeStamp_Type = Unsigned32
_MeasurementsInletSensorMaxTimeStamp_Object = MibTableColumn
measurementsInletSensorMaxTimeStamp = _MeasurementsInletSensorMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3, 1, 13),
    _MeasurementsInletSensorMaxTimeStamp_Type()
)
measurementsInletSensorMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletSensorMaxTimeStamp.setStatus("current")
_MeasurementsInletSensorMinMaxResetTimeStamp_Type = Unsigned32
_MeasurementsInletSensorMinMaxResetTimeStamp_Object = MibTableColumn
measurementsInletSensorMinMaxResetTimeStamp = _MeasurementsInletSensorMinMaxResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3, 1, 14),
    _MeasurementsInletSensorMinMaxResetTimeStamp_Type()
)
measurementsInletSensorMinMaxResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletSensorMinMaxResetTimeStamp.setStatus("current")
_MeasurementsInletSensorResetTimeStamp_Type = Unsigned32
_MeasurementsInletSensorResetTimeStamp_Object = MibTableColumn
measurementsInletSensorResetTimeStamp = _MeasurementsInletSensorResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 3, 1, 15),
    _MeasurementsInletSensorResetTimeStamp_Type()
)
measurementsInletSensorResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletSensorResetTimeStamp.setStatus("current")
_InletPoleSensorMeasurementsTable_Object = MibTable
inletPoleSensorMeasurementsTable = _InletPoleSensorMeasurementsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 4)
)
if mibBuilder.loadTexts:
    inletPoleSensorMeasurementsTable.setStatus("current")
_InletPoleSensorMeasurementsEntry_Object = MibTableRow
inletPoleSensorMeasurementsEntry = _InletPoleSensorMeasurementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 4, 1)
)
inletPoleSensorMeasurementsEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
    (0, "PDU2-MIB", "inletPoleIndex"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    inletPoleSensorMeasurementsEntry.setStatus("current")
_MeasurementsInletPoleSensorIsAvailable_Type = TruthValue
_MeasurementsInletPoleSensorIsAvailable_Object = MibTableColumn
measurementsInletPoleSensorIsAvailable = _MeasurementsInletPoleSensorIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 4, 1, 2),
    _MeasurementsInletPoleSensorIsAvailable_Type()
)
measurementsInletPoleSensorIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletPoleSensorIsAvailable.setStatus("current")
_MeasurementsInletPoleSensorState_Type = SensorStateEnumeration
_MeasurementsInletPoleSensorState_Object = MibTableColumn
measurementsInletPoleSensorState = _MeasurementsInletPoleSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 4, 1, 3),
    _MeasurementsInletPoleSensorState_Type()
)
measurementsInletPoleSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletPoleSensorState.setStatus("current")
_MeasurementsInletPoleSensorValue_Type = Unsigned32
_MeasurementsInletPoleSensorValue_Object = MibTableColumn
measurementsInletPoleSensorValue = _MeasurementsInletPoleSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 4, 1, 4),
    _MeasurementsInletPoleSensorValue_Type()
)
measurementsInletPoleSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletPoleSensorValue.setStatus("current")
_MeasurementsInletPoleSensorTimeStamp_Type = Unsigned32
_MeasurementsInletPoleSensorTimeStamp_Object = MibTableColumn
measurementsInletPoleSensorTimeStamp = _MeasurementsInletPoleSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 4, 1, 5),
    _MeasurementsInletPoleSensorTimeStamp_Type()
)
measurementsInletPoleSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletPoleSensorTimeStamp.setStatus("current")
_MeasurementsInletPoleSensorSignedValue_Type = Integer32
_MeasurementsInletPoleSensorSignedValue_Object = MibTableColumn
measurementsInletPoleSensorSignedValue = _MeasurementsInletPoleSensorSignedValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 4, 1, 6),
    _MeasurementsInletPoleSensorSignedValue_Type()
)
measurementsInletPoleSensorSignedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletPoleSensorSignedValue.setStatus("current")
_MeasurementsInletPoleSensorMinMaxValid_Type = TruthValue
_MeasurementsInletPoleSensorMinMaxValid_Object = MibTableColumn
measurementsInletPoleSensorMinMaxValid = _MeasurementsInletPoleSensorMinMaxValid_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 4, 1, 7),
    _MeasurementsInletPoleSensorMinMaxValid_Type()
)
measurementsInletPoleSensorMinMaxValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletPoleSensorMinMaxValid.setStatus("current")
_MeasurementsInletPoleSensorMinValue_Type = Unsigned32
_MeasurementsInletPoleSensorMinValue_Object = MibTableColumn
measurementsInletPoleSensorMinValue = _MeasurementsInletPoleSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 4, 1, 8),
    _MeasurementsInletPoleSensorMinValue_Type()
)
measurementsInletPoleSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletPoleSensorMinValue.setStatus("current")
_MeasurementsInletPoleSensorSignedMinValue_Type = Integer32
_MeasurementsInletPoleSensorSignedMinValue_Object = MibTableColumn
measurementsInletPoleSensorSignedMinValue = _MeasurementsInletPoleSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 4, 1, 9),
    _MeasurementsInletPoleSensorSignedMinValue_Type()
)
measurementsInletPoleSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletPoleSensorSignedMinValue.setStatus("current")
_MeasurementsInletPoleSensorMinTimeStamp_Type = Unsigned32
_MeasurementsInletPoleSensorMinTimeStamp_Object = MibTableColumn
measurementsInletPoleSensorMinTimeStamp = _MeasurementsInletPoleSensorMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 4, 1, 10),
    _MeasurementsInletPoleSensorMinTimeStamp_Type()
)
measurementsInletPoleSensorMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletPoleSensorMinTimeStamp.setStatus("current")
_MeasurementsInletPoleSensorMaxValue_Type = Unsigned32
_MeasurementsInletPoleSensorMaxValue_Object = MibTableColumn
measurementsInletPoleSensorMaxValue = _MeasurementsInletPoleSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 4, 1, 11),
    _MeasurementsInletPoleSensorMaxValue_Type()
)
measurementsInletPoleSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletPoleSensorMaxValue.setStatus("current")
_MeasurementsInletPoleSensorSignedMaxValue_Type = Integer32
_MeasurementsInletPoleSensorSignedMaxValue_Object = MibTableColumn
measurementsInletPoleSensorSignedMaxValue = _MeasurementsInletPoleSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 4, 1, 12),
    _MeasurementsInletPoleSensorSignedMaxValue_Type()
)
measurementsInletPoleSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletPoleSensorSignedMaxValue.setStatus("current")
_MeasurementsInletPoleSensorMaxTimeStamp_Type = Unsigned32
_MeasurementsInletPoleSensorMaxTimeStamp_Object = MibTableColumn
measurementsInletPoleSensorMaxTimeStamp = _MeasurementsInletPoleSensorMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 4, 1, 13),
    _MeasurementsInletPoleSensorMaxTimeStamp_Type()
)
measurementsInletPoleSensorMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletPoleSensorMaxTimeStamp.setStatus("current")
_MeasurementsInletPoleSensorMinMaxResetTimeStamp_Type = Unsigned32
_MeasurementsInletPoleSensorMinMaxResetTimeStamp_Object = MibTableColumn
measurementsInletPoleSensorMinMaxResetTimeStamp = _MeasurementsInletPoleSensorMinMaxResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 4, 1, 14),
    _MeasurementsInletPoleSensorMinMaxResetTimeStamp_Type()
)
measurementsInletPoleSensorMinMaxResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletPoleSensorMinMaxResetTimeStamp.setStatus("current")
_InletLinePairSensorMeasurementsTable_Object = MibTable
inletLinePairSensorMeasurementsTable = _InletLinePairSensorMeasurementsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 5)
)
if mibBuilder.loadTexts:
    inletLinePairSensorMeasurementsTable.setStatus("current")
_InletLinePairSensorMeasurementsEntry_Object = MibTableRow
inletLinePairSensorMeasurementsEntry = _InletLinePairSensorMeasurementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 5, 1)
)
inletLinePairSensorMeasurementsEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
    (0, "PDU2-MIB", "inletLinePairIndex"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    inletLinePairSensorMeasurementsEntry.setStatus("current")
_MeasurementsInletLinePairSensorIsAvailable_Type = TruthValue
_MeasurementsInletLinePairSensorIsAvailable_Object = MibTableColumn
measurementsInletLinePairSensorIsAvailable = _MeasurementsInletLinePairSensorIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 5, 1, 2),
    _MeasurementsInletLinePairSensorIsAvailable_Type()
)
measurementsInletLinePairSensorIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletLinePairSensorIsAvailable.setStatus("current")
_MeasurementsInletLinePairSensorState_Type = SensorStateEnumeration
_MeasurementsInletLinePairSensorState_Object = MibTableColumn
measurementsInletLinePairSensorState = _MeasurementsInletLinePairSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 5, 1, 3),
    _MeasurementsInletLinePairSensorState_Type()
)
measurementsInletLinePairSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletLinePairSensorState.setStatus("current")
_MeasurementsInletLinePairSensorValue_Type = Unsigned32
_MeasurementsInletLinePairSensorValue_Object = MibTableColumn
measurementsInletLinePairSensorValue = _MeasurementsInletLinePairSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 5, 1, 4),
    _MeasurementsInletLinePairSensorValue_Type()
)
measurementsInletLinePairSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletLinePairSensorValue.setStatus("current")
_MeasurementsInletLinePairSensorTimeStamp_Type = Unsigned32
_MeasurementsInletLinePairSensorTimeStamp_Object = MibTableColumn
measurementsInletLinePairSensorTimeStamp = _MeasurementsInletLinePairSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 5, 1, 5),
    _MeasurementsInletLinePairSensorTimeStamp_Type()
)
measurementsInletLinePairSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletLinePairSensorTimeStamp.setStatus("current")
_MeasurementsInletLinePairSensorSignedValue_Type = Integer32
_MeasurementsInletLinePairSensorSignedValue_Object = MibTableColumn
measurementsInletLinePairSensorSignedValue = _MeasurementsInletLinePairSensorSignedValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 5, 1, 6),
    _MeasurementsInletLinePairSensorSignedValue_Type()
)
measurementsInletLinePairSensorSignedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletLinePairSensorSignedValue.setStatus("current")
_MeasurementsInletLinePairSensorMinMaxValid_Type = TruthValue
_MeasurementsInletLinePairSensorMinMaxValid_Object = MibTableColumn
measurementsInletLinePairSensorMinMaxValid = _MeasurementsInletLinePairSensorMinMaxValid_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 5, 1, 7),
    _MeasurementsInletLinePairSensorMinMaxValid_Type()
)
measurementsInletLinePairSensorMinMaxValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletLinePairSensorMinMaxValid.setStatus("current")
_MeasurementsInletLinePairSensorMinValue_Type = Unsigned32
_MeasurementsInletLinePairSensorMinValue_Object = MibTableColumn
measurementsInletLinePairSensorMinValue = _MeasurementsInletLinePairSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 5, 1, 8),
    _MeasurementsInletLinePairSensorMinValue_Type()
)
measurementsInletLinePairSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletLinePairSensorMinValue.setStatus("current")
_MeasurementsInletLinePairSensorSignedMinValue_Type = Integer32
_MeasurementsInletLinePairSensorSignedMinValue_Object = MibTableColumn
measurementsInletLinePairSensorSignedMinValue = _MeasurementsInletLinePairSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 5, 1, 9),
    _MeasurementsInletLinePairSensorSignedMinValue_Type()
)
measurementsInletLinePairSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletLinePairSensorSignedMinValue.setStatus("current")
_MeasurementsInletLinePairSensorMinTimeStamp_Type = Unsigned32
_MeasurementsInletLinePairSensorMinTimeStamp_Object = MibTableColumn
measurementsInletLinePairSensorMinTimeStamp = _MeasurementsInletLinePairSensorMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 5, 1, 10),
    _MeasurementsInletLinePairSensorMinTimeStamp_Type()
)
measurementsInletLinePairSensorMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletLinePairSensorMinTimeStamp.setStatus("current")
_MeasurementsInletLinePairSensorMaxValue_Type = Unsigned32
_MeasurementsInletLinePairSensorMaxValue_Object = MibTableColumn
measurementsInletLinePairSensorMaxValue = _MeasurementsInletLinePairSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 5, 1, 11),
    _MeasurementsInletLinePairSensorMaxValue_Type()
)
measurementsInletLinePairSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletLinePairSensorMaxValue.setStatus("current")
_MeasurementsInletLinePairSensorSignedMaxValue_Type = Integer32
_MeasurementsInletLinePairSensorSignedMaxValue_Object = MibTableColumn
measurementsInletLinePairSensorSignedMaxValue = _MeasurementsInletLinePairSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 5, 1, 12),
    _MeasurementsInletLinePairSensorSignedMaxValue_Type()
)
measurementsInletLinePairSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletLinePairSensorSignedMaxValue.setStatus("current")
_MeasurementsInletLinePairSensorMaxTimeStamp_Type = Unsigned32
_MeasurementsInletLinePairSensorMaxTimeStamp_Object = MibTableColumn
measurementsInletLinePairSensorMaxTimeStamp = _MeasurementsInletLinePairSensorMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 5, 1, 13),
    _MeasurementsInletLinePairSensorMaxTimeStamp_Type()
)
measurementsInletLinePairSensorMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletLinePairSensorMaxTimeStamp.setStatus("current")
_MeasurementsInletLinePairSensorMinMaxResetTimeStamp_Type = Unsigned32
_MeasurementsInletLinePairSensorMinMaxResetTimeStamp_Object = MibTableColumn
measurementsInletLinePairSensorMinMaxResetTimeStamp = _MeasurementsInletLinePairSensorMinMaxResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 2, 5, 1, 14),
    _MeasurementsInletLinePairSensorMinMaxResetTimeStamp_Type()
)
measurementsInletLinePairSensorMinMaxResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsInletLinePairSensorMinMaxResetTimeStamp.setStatus("current")
_MeasurementsOverCurrentProtector_ObjectIdentity = ObjectIdentity
measurementsOverCurrentProtector = _MeasurementsOverCurrentProtector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3)
)
_OverCurrentProtectorSensorMeasurementsTable_Object = MibTable
overCurrentProtectorSensorMeasurementsTable = _OverCurrentProtectorSensorMeasurementsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3, 3)
)
if mibBuilder.loadTexts:
    overCurrentProtectorSensorMeasurementsTable.setStatus("current")
_OverCurrentProtectorSensorMeasurementsEntry_Object = MibTableRow
overCurrentProtectorSensorMeasurementsEntry = _OverCurrentProtectorSensorMeasurementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3, 3, 1)
)
overCurrentProtectorSensorMeasurementsEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "overCurrentProtectorIndex"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    overCurrentProtectorSensorMeasurementsEntry.setStatus("current")
_MeasurementsOverCurrentProtectorSensorIsAvailable_Type = TruthValue
_MeasurementsOverCurrentProtectorSensorIsAvailable_Object = MibTableColumn
measurementsOverCurrentProtectorSensorIsAvailable = _MeasurementsOverCurrentProtectorSensorIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3, 3, 1, 2),
    _MeasurementsOverCurrentProtectorSensorIsAvailable_Type()
)
measurementsOverCurrentProtectorSensorIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOverCurrentProtectorSensorIsAvailable.setStatus("current")
_MeasurementsOverCurrentProtectorSensorState_Type = SensorStateEnumeration
_MeasurementsOverCurrentProtectorSensorState_Object = MibTableColumn
measurementsOverCurrentProtectorSensorState = _MeasurementsOverCurrentProtectorSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3, 3, 1, 3),
    _MeasurementsOverCurrentProtectorSensorState_Type()
)
measurementsOverCurrentProtectorSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOverCurrentProtectorSensorState.setStatus("current")
_MeasurementsOverCurrentProtectorSensorValue_Type = Unsigned32
_MeasurementsOverCurrentProtectorSensorValue_Object = MibTableColumn
measurementsOverCurrentProtectorSensorValue = _MeasurementsOverCurrentProtectorSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3, 3, 1, 4),
    _MeasurementsOverCurrentProtectorSensorValue_Type()
)
measurementsOverCurrentProtectorSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOverCurrentProtectorSensorValue.setStatus("current")
_MeasurementsOverCurrentProtectorSensorTimeStamp_Type = Unsigned32
_MeasurementsOverCurrentProtectorSensorTimeStamp_Object = MibTableColumn
measurementsOverCurrentProtectorSensorTimeStamp = _MeasurementsOverCurrentProtectorSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3, 3, 1, 5),
    _MeasurementsOverCurrentProtectorSensorTimeStamp_Type()
)
measurementsOverCurrentProtectorSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOverCurrentProtectorSensorTimeStamp.setStatus("current")
_MeasurementsOverCurrentProtectorSensorSignedValue_Type = Integer32
_MeasurementsOverCurrentProtectorSensorSignedValue_Object = MibTableColumn
measurementsOverCurrentProtectorSensorSignedValue = _MeasurementsOverCurrentProtectorSensorSignedValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3, 3, 1, 6),
    _MeasurementsOverCurrentProtectorSensorSignedValue_Type()
)
measurementsOverCurrentProtectorSensorSignedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOverCurrentProtectorSensorSignedValue.setStatus("current")
_MeasurementsOverCurrentProtectorSensorMinMaxValid_Type = TruthValue
_MeasurementsOverCurrentProtectorSensorMinMaxValid_Object = MibTableColumn
measurementsOverCurrentProtectorSensorMinMaxValid = _MeasurementsOverCurrentProtectorSensorMinMaxValid_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3, 3, 1, 7),
    _MeasurementsOverCurrentProtectorSensorMinMaxValid_Type()
)
measurementsOverCurrentProtectorSensorMinMaxValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOverCurrentProtectorSensorMinMaxValid.setStatus("current")
_MeasurementsOverCurrentProtectorSensorMinValue_Type = Unsigned32
_MeasurementsOverCurrentProtectorSensorMinValue_Object = MibTableColumn
measurementsOverCurrentProtectorSensorMinValue = _MeasurementsOverCurrentProtectorSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3, 3, 1, 8),
    _MeasurementsOverCurrentProtectorSensorMinValue_Type()
)
measurementsOverCurrentProtectorSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOverCurrentProtectorSensorMinValue.setStatus("current")
_MeasurementsOverCurrentProtectorSensorSignedMinValue_Type = Integer32
_MeasurementsOverCurrentProtectorSensorSignedMinValue_Object = MibTableColumn
measurementsOverCurrentProtectorSensorSignedMinValue = _MeasurementsOverCurrentProtectorSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3, 3, 1, 9),
    _MeasurementsOverCurrentProtectorSensorSignedMinValue_Type()
)
measurementsOverCurrentProtectorSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOverCurrentProtectorSensorSignedMinValue.setStatus("current")
_MeasurementsOverCurrentProtectorSensorMinTimeStamp_Type = Unsigned32
_MeasurementsOverCurrentProtectorSensorMinTimeStamp_Object = MibTableColumn
measurementsOverCurrentProtectorSensorMinTimeStamp = _MeasurementsOverCurrentProtectorSensorMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3, 3, 1, 10),
    _MeasurementsOverCurrentProtectorSensorMinTimeStamp_Type()
)
measurementsOverCurrentProtectorSensorMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOverCurrentProtectorSensorMinTimeStamp.setStatus("current")
_MeasurementsOverCurrentProtectorSensorMaxValue_Type = Unsigned32
_MeasurementsOverCurrentProtectorSensorMaxValue_Object = MibTableColumn
measurementsOverCurrentProtectorSensorMaxValue = _MeasurementsOverCurrentProtectorSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3, 3, 1, 11),
    _MeasurementsOverCurrentProtectorSensorMaxValue_Type()
)
measurementsOverCurrentProtectorSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOverCurrentProtectorSensorMaxValue.setStatus("current")
_MeasurementsOverCurrentProtectorSensorSignedMaxValue_Type = Integer32
_MeasurementsOverCurrentProtectorSensorSignedMaxValue_Object = MibTableColumn
measurementsOverCurrentProtectorSensorSignedMaxValue = _MeasurementsOverCurrentProtectorSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3, 3, 1, 12),
    _MeasurementsOverCurrentProtectorSensorSignedMaxValue_Type()
)
measurementsOverCurrentProtectorSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOverCurrentProtectorSensorSignedMaxValue.setStatus("current")
_MeasurementsOverCurrentProtectorSensorMaxTimeStamp_Type = Unsigned32
_MeasurementsOverCurrentProtectorSensorMaxTimeStamp_Object = MibTableColumn
measurementsOverCurrentProtectorSensorMaxTimeStamp = _MeasurementsOverCurrentProtectorSensorMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3, 3, 1, 13),
    _MeasurementsOverCurrentProtectorSensorMaxTimeStamp_Type()
)
measurementsOverCurrentProtectorSensorMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOverCurrentProtectorSensorMaxTimeStamp.setStatus("current")
_MeasurementsOverCurrentProtectorSensorMinMaxResetTimeStamp_Type = Unsigned32
_MeasurementsOverCurrentProtectorSensorMinMaxResetTimeStamp_Object = MibTableColumn
measurementsOverCurrentProtectorSensorMinMaxResetTimeStamp = _MeasurementsOverCurrentProtectorSensorMinMaxResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 3, 3, 1, 14),
    _MeasurementsOverCurrentProtectorSensorMinMaxResetTimeStamp_Type()
)
measurementsOverCurrentProtectorSensorMinMaxResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOverCurrentProtectorSensorMinMaxResetTimeStamp.setStatus("current")
_MeasurementsOutlet_ObjectIdentity = ObjectIdentity
measurementsOutlet = _MeasurementsOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4)
)
_OutletSensorMeasurementsTable_Object = MibTable
outletSensorMeasurementsTable = _OutletSensorMeasurementsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3)
)
if mibBuilder.loadTexts:
    outletSensorMeasurementsTable.setStatus("current")
_OutletSensorMeasurementsEntry_Object = MibTableRow
outletSensorMeasurementsEntry = _OutletSensorMeasurementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3, 1)
)
outletSensorMeasurementsEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "outletId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    outletSensorMeasurementsEntry.setStatus("current")
_MeasurementsOutletSensorIsAvailable_Type = TruthValue
_MeasurementsOutletSensorIsAvailable_Object = MibTableColumn
measurementsOutletSensorIsAvailable = _MeasurementsOutletSensorIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3, 1, 2),
    _MeasurementsOutletSensorIsAvailable_Type()
)
measurementsOutletSensorIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletSensorIsAvailable.setStatus("current")
_MeasurementsOutletSensorState_Type = SensorStateEnumeration
_MeasurementsOutletSensorState_Object = MibTableColumn
measurementsOutletSensorState = _MeasurementsOutletSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3, 1, 3),
    _MeasurementsOutletSensorState_Type()
)
measurementsOutletSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletSensorState.setStatus("current")
_MeasurementsOutletSensorValue_Type = Unsigned32
_MeasurementsOutletSensorValue_Object = MibTableColumn
measurementsOutletSensorValue = _MeasurementsOutletSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3, 1, 4),
    _MeasurementsOutletSensorValue_Type()
)
measurementsOutletSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletSensorValue.setStatus("current")
_MeasurementsOutletSensorTimeStamp_Type = Unsigned32
_MeasurementsOutletSensorTimeStamp_Object = MibTableColumn
measurementsOutletSensorTimeStamp = _MeasurementsOutletSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3, 1, 5),
    _MeasurementsOutletSensorTimeStamp_Type()
)
measurementsOutletSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletSensorTimeStamp.setStatus("current")
_MeasurementsOutletSensorSignedValue_Type = Integer32
_MeasurementsOutletSensorSignedValue_Object = MibTableColumn
measurementsOutletSensorSignedValue = _MeasurementsOutletSensorSignedValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3, 1, 6),
    _MeasurementsOutletSensorSignedValue_Type()
)
measurementsOutletSensorSignedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletSensorSignedValue.setStatus("current")
_MeasurementsOutletSensorMinMaxValid_Type = TruthValue
_MeasurementsOutletSensorMinMaxValid_Object = MibTableColumn
measurementsOutletSensorMinMaxValid = _MeasurementsOutletSensorMinMaxValid_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3, 1, 7),
    _MeasurementsOutletSensorMinMaxValid_Type()
)
measurementsOutletSensorMinMaxValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletSensorMinMaxValid.setStatus("current")
_MeasurementsOutletSensorMinValue_Type = Unsigned32
_MeasurementsOutletSensorMinValue_Object = MibTableColumn
measurementsOutletSensorMinValue = _MeasurementsOutletSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3, 1, 8),
    _MeasurementsOutletSensorMinValue_Type()
)
measurementsOutletSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletSensorMinValue.setStatus("current")
_MeasurementsOutletSensorSignedMinValue_Type = Integer32
_MeasurementsOutletSensorSignedMinValue_Object = MibTableColumn
measurementsOutletSensorSignedMinValue = _MeasurementsOutletSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3, 1, 9),
    _MeasurementsOutletSensorSignedMinValue_Type()
)
measurementsOutletSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletSensorSignedMinValue.setStatus("current")
_MeasurementsOutletSensorMinTimeStamp_Type = Unsigned32
_MeasurementsOutletSensorMinTimeStamp_Object = MibTableColumn
measurementsOutletSensorMinTimeStamp = _MeasurementsOutletSensorMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3, 1, 10),
    _MeasurementsOutletSensorMinTimeStamp_Type()
)
measurementsOutletSensorMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletSensorMinTimeStamp.setStatus("current")
_MeasurementsOutletSensorMaxValue_Type = Unsigned32
_MeasurementsOutletSensorMaxValue_Object = MibTableColumn
measurementsOutletSensorMaxValue = _MeasurementsOutletSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3, 1, 11),
    _MeasurementsOutletSensorMaxValue_Type()
)
measurementsOutletSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletSensorMaxValue.setStatus("current")
_MeasurementsOutletSensorSignedMaxValue_Type = Integer32
_MeasurementsOutletSensorSignedMaxValue_Object = MibTableColumn
measurementsOutletSensorSignedMaxValue = _MeasurementsOutletSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3, 1, 12),
    _MeasurementsOutletSensorSignedMaxValue_Type()
)
measurementsOutletSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletSensorSignedMaxValue.setStatus("current")
_MeasurementsOutletSensorMaxTimeStamp_Type = Unsigned32
_MeasurementsOutletSensorMaxTimeStamp_Object = MibTableColumn
measurementsOutletSensorMaxTimeStamp = _MeasurementsOutletSensorMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3, 1, 13),
    _MeasurementsOutletSensorMaxTimeStamp_Type()
)
measurementsOutletSensorMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletSensorMaxTimeStamp.setStatus("current")
_MeasurementsOutletSensorMinMaxResetTimeStamp_Type = Unsigned32
_MeasurementsOutletSensorMinMaxResetTimeStamp_Object = MibTableColumn
measurementsOutletSensorMinMaxResetTimeStamp = _MeasurementsOutletSensorMinMaxResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3, 1, 14),
    _MeasurementsOutletSensorMinMaxResetTimeStamp_Type()
)
measurementsOutletSensorMinMaxResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletSensorMinMaxResetTimeStamp.setStatus("current")
_MeasurementsOutletSensorResetTimeStamp_Type = Unsigned32
_MeasurementsOutletSensorResetTimeStamp_Object = MibTableColumn
measurementsOutletSensorResetTimeStamp = _MeasurementsOutletSensorResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 3, 1, 15),
    _MeasurementsOutletSensorResetTimeStamp_Type()
)
measurementsOutletSensorResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletSensorResetTimeStamp.setStatus("current")
_OutletPoleSensorMeasurementsTable_Object = MibTable
outletPoleSensorMeasurementsTable = _OutletPoleSensorMeasurementsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 4)
)
if mibBuilder.loadTexts:
    outletPoleSensorMeasurementsTable.setStatus("current")
_OutletPoleSensorMeasurementsEntry_Object = MibTableRow
outletPoleSensorMeasurementsEntry = _OutletPoleSensorMeasurementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 4, 1)
)
outletPoleSensorMeasurementsEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "outletId"),
    (0, "PDU2-MIB", "outletPoleIndex"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    outletPoleSensorMeasurementsEntry.setStatus("current")
_MeasurementsOutletPoleSensorIsAvailable_Type = TruthValue
_MeasurementsOutletPoleSensorIsAvailable_Object = MibTableColumn
measurementsOutletPoleSensorIsAvailable = _MeasurementsOutletPoleSensorIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 4, 1, 2),
    _MeasurementsOutletPoleSensorIsAvailable_Type()
)
measurementsOutletPoleSensorIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletPoleSensorIsAvailable.setStatus("current")
_MeasurementsOutletPoleSensorState_Type = SensorStateEnumeration
_MeasurementsOutletPoleSensorState_Object = MibTableColumn
measurementsOutletPoleSensorState = _MeasurementsOutletPoleSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 4, 1, 3),
    _MeasurementsOutletPoleSensorState_Type()
)
measurementsOutletPoleSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletPoleSensorState.setStatus("current")
_MeasurementsOutletPoleSensorValue_Type = Unsigned32
_MeasurementsOutletPoleSensorValue_Object = MibTableColumn
measurementsOutletPoleSensorValue = _MeasurementsOutletPoleSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 4, 1, 4),
    _MeasurementsOutletPoleSensorValue_Type()
)
measurementsOutletPoleSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletPoleSensorValue.setStatus("current")
_MeasurementsOutletPoleSensorTimeStamp_Type = Unsigned32
_MeasurementsOutletPoleSensorTimeStamp_Object = MibTableColumn
measurementsOutletPoleSensorTimeStamp = _MeasurementsOutletPoleSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 4, 1, 5),
    _MeasurementsOutletPoleSensorTimeStamp_Type()
)
measurementsOutletPoleSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletPoleSensorTimeStamp.setStatus("current")
_MeasurementsOutletPoleSensorSignedValue_Type = Integer32
_MeasurementsOutletPoleSensorSignedValue_Object = MibTableColumn
measurementsOutletPoleSensorSignedValue = _MeasurementsOutletPoleSensorSignedValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 4, 1, 6),
    _MeasurementsOutletPoleSensorSignedValue_Type()
)
measurementsOutletPoleSensorSignedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletPoleSensorSignedValue.setStatus("current")
_MeasurementsOutletPoleSensorMinMaxValid_Type = TruthValue
_MeasurementsOutletPoleSensorMinMaxValid_Object = MibTableColumn
measurementsOutletPoleSensorMinMaxValid = _MeasurementsOutletPoleSensorMinMaxValid_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 4, 1, 7),
    _MeasurementsOutletPoleSensorMinMaxValid_Type()
)
measurementsOutletPoleSensorMinMaxValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletPoleSensorMinMaxValid.setStatus("current")
_MeasurementsOutletPoleSensorMinValue_Type = Unsigned32
_MeasurementsOutletPoleSensorMinValue_Object = MibTableColumn
measurementsOutletPoleSensorMinValue = _MeasurementsOutletPoleSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 4, 1, 8),
    _MeasurementsOutletPoleSensorMinValue_Type()
)
measurementsOutletPoleSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletPoleSensorMinValue.setStatus("current")
_MeasurementsOutletPoleSensorSignedMinValue_Type = Integer32
_MeasurementsOutletPoleSensorSignedMinValue_Object = MibTableColumn
measurementsOutletPoleSensorSignedMinValue = _MeasurementsOutletPoleSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 4, 1, 9),
    _MeasurementsOutletPoleSensorSignedMinValue_Type()
)
measurementsOutletPoleSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletPoleSensorSignedMinValue.setStatus("current")
_MeasurementsOutletPoleSensorMinTimeStamp_Type = Unsigned32
_MeasurementsOutletPoleSensorMinTimeStamp_Object = MibTableColumn
measurementsOutletPoleSensorMinTimeStamp = _MeasurementsOutletPoleSensorMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 4, 1, 10),
    _MeasurementsOutletPoleSensorMinTimeStamp_Type()
)
measurementsOutletPoleSensorMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletPoleSensorMinTimeStamp.setStatus("current")
_MeasurementsOutletPoleSensorMaxValue_Type = Unsigned32
_MeasurementsOutletPoleSensorMaxValue_Object = MibTableColumn
measurementsOutletPoleSensorMaxValue = _MeasurementsOutletPoleSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 4, 1, 11),
    _MeasurementsOutletPoleSensorMaxValue_Type()
)
measurementsOutletPoleSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletPoleSensorMaxValue.setStatus("current")
_MeasurementsOutletPoleSensorSignedMaxValue_Type = Integer32
_MeasurementsOutletPoleSensorSignedMaxValue_Object = MibTableColumn
measurementsOutletPoleSensorSignedMaxValue = _MeasurementsOutletPoleSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 4, 1, 12),
    _MeasurementsOutletPoleSensorSignedMaxValue_Type()
)
measurementsOutletPoleSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletPoleSensorSignedMaxValue.setStatus("current")
_MeasurementsOutletPoleSensorMaxTimeStamp_Type = Unsigned32
_MeasurementsOutletPoleSensorMaxTimeStamp_Object = MibTableColumn
measurementsOutletPoleSensorMaxTimeStamp = _MeasurementsOutletPoleSensorMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 4, 1, 13),
    _MeasurementsOutletPoleSensorMaxTimeStamp_Type()
)
measurementsOutletPoleSensorMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletPoleSensorMaxTimeStamp.setStatus("current")
_MeasurementsOutletPoleSensorMinMaxResetTimeStamp_Type = Unsigned32
_MeasurementsOutletPoleSensorMinMaxResetTimeStamp_Object = MibTableColumn
measurementsOutletPoleSensorMinMaxResetTimeStamp = _MeasurementsOutletPoleSensorMinMaxResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 4, 4, 1, 14),
    _MeasurementsOutletPoleSensorMinMaxResetTimeStamp_Type()
)
measurementsOutletPoleSensorMinMaxResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletPoleSensorMinMaxResetTimeStamp.setStatus("current")
_MeasurementsExternalSensor_ObjectIdentity = ObjectIdentity
measurementsExternalSensor = _MeasurementsExternalSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 5)
)
_ExternalSensorMeasurementsTable_Object = MibTable
externalSensorMeasurementsTable = _ExternalSensorMeasurementsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 5, 3)
)
if mibBuilder.loadTexts:
    externalSensorMeasurementsTable.setStatus("current")
_ExternalSensorMeasurementsEntry_Object = MibTableRow
externalSensorMeasurementsEntry = _ExternalSensorMeasurementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 5, 3, 1)
)
externalSensorMeasurementsEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "sensorID"),
)
if mibBuilder.loadTexts:
    externalSensorMeasurementsEntry.setStatus("current")
_MeasurementsExternalSensorIsAvailable_Type = TruthValue
_MeasurementsExternalSensorIsAvailable_Object = MibTableColumn
measurementsExternalSensorIsAvailable = _MeasurementsExternalSensorIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 5, 3, 1, 2),
    _MeasurementsExternalSensorIsAvailable_Type()
)
measurementsExternalSensorIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsExternalSensorIsAvailable.setStatus("current")
_MeasurementsExternalSensorState_Type = SensorStateEnumeration
_MeasurementsExternalSensorState_Object = MibTableColumn
measurementsExternalSensorState = _MeasurementsExternalSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 5, 3, 1, 3),
    _MeasurementsExternalSensorState_Type()
)
measurementsExternalSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsExternalSensorState.setStatus("current")
_MeasurementsExternalSensorValue_Type = Integer32
_MeasurementsExternalSensorValue_Object = MibTableColumn
measurementsExternalSensorValue = _MeasurementsExternalSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 5, 3, 1, 4),
    _MeasurementsExternalSensorValue_Type()
)
measurementsExternalSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsExternalSensorValue.setStatus("current")
_MeasurementsExternalSensorTimeStamp_Type = Unsigned32
_MeasurementsExternalSensorTimeStamp_Object = MibTableColumn
measurementsExternalSensorTimeStamp = _MeasurementsExternalSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 5, 3, 1, 5),
    _MeasurementsExternalSensorTimeStamp_Type()
)
measurementsExternalSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsExternalSensorTimeStamp.setStatus("current")
_MeasurementsExternalSensorMinMaxValid_Type = TruthValue
_MeasurementsExternalSensorMinMaxValid_Object = MibTableColumn
measurementsExternalSensorMinMaxValid = _MeasurementsExternalSensorMinMaxValid_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 5, 3, 1, 7),
    _MeasurementsExternalSensorMinMaxValid_Type()
)
measurementsExternalSensorMinMaxValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsExternalSensorMinMaxValid.setStatus("current")
_MeasurementsExternalSensorMinValue_Type = Integer32
_MeasurementsExternalSensorMinValue_Object = MibTableColumn
measurementsExternalSensorMinValue = _MeasurementsExternalSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 5, 3, 1, 8),
    _MeasurementsExternalSensorMinValue_Type()
)
measurementsExternalSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsExternalSensorMinValue.setStatus("current")
_MeasurementsExternalSensorMinTimeStamp_Type = Unsigned32
_MeasurementsExternalSensorMinTimeStamp_Object = MibTableColumn
measurementsExternalSensorMinTimeStamp = _MeasurementsExternalSensorMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 5, 3, 1, 10),
    _MeasurementsExternalSensorMinTimeStamp_Type()
)
measurementsExternalSensorMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsExternalSensorMinTimeStamp.setStatus("current")
_MeasurementsExternalSensorMaxValue_Type = Integer32
_MeasurementsExternalSensorMaxValue_Object = MibTableColumn
measurementsExternalSensorMaxValue = _MeasurementsExternalSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 5, 3, 1, 11),
    _MeasurementsExternalSensorMaxValue_Type()
)
measurementsExternalSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsExternalSensorMaxValue.setStatus("current")
_MeasurementsExternalSensorMaxTimeStamp_Type = Unsigned32
_MeasurementsExternalSensorMaxTimeStamp_Object = MibTableColumn
measurementsExternalSensorMaxTimeStamp = _MeasurementsExternalSensorMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 5, 3, 1, 13),
    _MeasurementsExternalSensorMaxTimeStamp_Type()
)
measurementsExternalSensorMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsExternalSensorMaxTimeStamp.setStatus("current")
_MeasurementsExternalSensorMinMaxResetTimeStamp_Type = Unsigned32
_MeasurementsExternalSensorMinMaxResetTimeStamp_Object = MibTableColumn
measurementsExternalSensorMinMaxResetTimeStamp = _MeasurementsExternalSensorMinMaxResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 5, 3, 1, 14),
    _MeasurementsExternalSensorMinMaxResetTimeStamp_Type()
)
measurementsExternalSensorMinMaxResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsExternalSensorMinMaxResetTimeStamp.setStatus("current")
_MeasurementsWire_ObjectIdentity = ObjectIdentity
measurementsWire = _MeasurementsWire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 6)
)
_WireSensorMeasurementsTable_Object = MibTable
wireSensorMeasurementsTable = _WireSensorMeasurementsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 6, 3)
)
if mibBuilder.loadTexts:
    wireSensorMeasurementsTable.setStatus("obsolete")
_WireSensorMeasurementsEntry_Object = MibTableRow
wireSensorMeasurementsEntry = _WireSensorMeasurementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 6, 3, 1)
)
wireSensorMeasurementsEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "wireId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    wireSensorMeasurementsEntry.setStatus("obsolete")
_MeasurementsWireSensorIsAvailable_Type = TruthValue
_MeasurementsWireSensorIsAvailable_Object = MibTableColumn
measurementsWireSensorIsAvailable = _MeasurementsWireSensorIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 6, 3, 1, 2),
    _MeasurementsWireSensorIsAvailable_Type()
)
measurementsWireSensorIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsWireSensorIsAvailable.setStatus("obsolete")
_MeasurementsWireSensorState_Type = SensorStateEnumeration
_MeasurementsWireSensorState_Object = MibTableColumn
measurementsWireSensorState = _MeasurementsWireSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 6, 3, 1, 3),
    _MeasurementsWireSensorState_Type()
)
measurementsWireSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsWireSensorState.setStatus("obsolete")
_MeasurementsWireSensorValue_Type = Unsigned32
_MeasurementsWireSensorValue_Object = MibTableColumn
measurementsWireSensorValue = _MeasurementsWireSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 6, 3, 1, 4),
    _MeasurementsWireSensorValue_Type()
)
measurementsWireSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsWireSensorValue.setStatus("obsolete")
_MeasurementsWireSensorTimeStamp_Type = Unsigned32
_MeasurementsWireSensorTimeStamp_Object = MibTableColumn
measurementsWireSensorTimeStamp = _MeasurementsWireSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 6, 3, 1, 5),
    _MeasurementsWireSensorTimeStamp_Type()
)
measurementsWireSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsWireSensorTimeStamp.setStatus("obsolete")
_MeasurementsTransferSwitch_ObjectIdentity = ObjectIdentity
measurementsTransferSwitch = _MeasurementsTransferSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7)
)
_TransferSwitchSensorMeasurementsTable_Object = MibTable
transferSwitchSensorMeasurementsTable = _TransferSwitchSensorMeasurementsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7, 3)
)
if mibBuilder.loadTexts:
    transferSwitchSensorMeasurementsTable.setStatus("current")
_TransferSwitchSensorMeasurementsEntry_Object = MibTableRow
transferSwitchSensorMeasurementsEntry = _TransferSwitchSensorMeasurementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7, 3, 1)
)
transferSwitchSensorMeasurementsEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "transferSwitchId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    transferSwitchSensorMeasurementsEntry.setStatus("current")
_MeasurementsTransferSwitchSensorIsAvailable_Type = TruthValue
_MeasurementsTransferSwitchSensorIsAvailable_Object = MibTableColumn
measurementsTransferSwitchSensorIsAvailable = _MeasurementsTransferSwitchSensorIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7, 3, 1, 2),
    _MeasurementsTransferSwitchSensorIsAvailable_Type()
)
measurementsTransferSwitchSensorIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsTransferSwitchSensorIsAvailable.setStatus("current")
_MeasurementsTransferSwitchSensorState_Type = SensorStateEnumeration
_MeasurementsTransferSwitchSensorState_Object = MibTableColumn
measurementsTransferSwitchSensorState = _MeasurementsTransferSwitchSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7, 3, 1, 3),
    _MeasurementsTransferSwitchSensorState_Type()
)
measurementsTransferSwitchSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsTransferSwitchSensorState.setStatus("current")
_MeasurementsTransferSwitchSensorValue_Type = Unsigned32
_MeasurementsTransferSwitchSensorValue_Object = MibTableColumn
measurementsTransferSwitchSensorValue = _MeasurementsTransferSwitchSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7, 3, 1, 4),
    _MeasurementsTransferSwitchSensorValue_Type()
)
measurementsTransferSwitchSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsTransferSwitchSensorValue.setStatus("current")
_MeasurementsTransferSwitchSensorTimeStamp_Type = Unsigned32
_MeasurementsTransferSwitchSensorTimeStamp_Object = MibTableColumn
measurementsTransferSwitchSensorTimeStamp = _MeasurementsTransferSwitchSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7, 3, 1, 5),
    _MeasurementsTransferSwitchSensorTimeStamp_Type()
)
measurementsTransferSwitchSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsTransferSwitchSensorTimeStamp.setStatus("current")
_MeasurementsTransferSwitchSensorSignedValue_Type = Integer32
_MeasurementsTransferSwitchSensorSignedValue_Object = MibTableColumn
measurementsTransferSwitchSensorSignedValue = _MeasurementsTransferSwitchSensorSignedValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7, 3, 1, 6),
    _MeasurementsTransferSwitchSensorSignedValue_Type()
)
measurementsTransferSwitchSensorSignedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsTransferSwitchSensorSignedValue.setStatus("current")
_MeasurementsTransferSwitchSensorMinMaxValid_Type = TruthValue
_MeasurementsTransferSwitchSensorMinMaxValid_Object = MibTableColumn
measurementsTransferSwitchSensorMinMaxValid = _MeasurementsTransferSwitchSensorMinMaxValid_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7, 3, 1, 7),
    _MeasurementsTransferSwitchSensorMinMaxValid_Type()
)
measurementsTransferSwitchSensorMinMaxValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsTransferSwitchSensorMinMaxValid.setStatus("current")
_MeasurementsTransferSwitchSensorMinValue_Type = Unsigned32
_MeasurementsTransferSwitchSensorMinValue_Object = MibTableColumn
measurementsTransferSwitchSensorMinValue = _MeasurementsTransferSwitchSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7, 3, 1, 8),
    _MeasurementsTransferSwitchSensorMinValue_Type()
)
measurementsTransferSwitchSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsTransferSwitchSensorMinValue.setStatus("current")
_MeasurementsTransferSwitchSensorSignedMinValue_Type = Integer32
_MeasurementsTransferSwitchSensorSignedMinValue_Object = MibTableColumn
measurementsTransferSwitchSensorSignedMinValue = _MeasurementsTransferSwitchSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7, 3, 1, 9),
    _MeasurementsTransferSwitchSensorSignedMinValue_Type()
)
measurementsTransferSwitchSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsTransferSwitchSensorSignedMinValue.setStatus("current")
_MeasurementsTransferSwitchSensorMinTimeStamp_Type = Unsigned32
_MeasurementsTransferSwitchSensorMinTimeStamp_Object = MibTableColumn
measurementsTransferSwitchSensorMinTimeStamp = _MeasurementsTransferSwitchSensorMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7, 3, 1, 10),
    _MeasurementsTransferSwitchSensorMinTimeStamp_Type()
)
measurementsTransferSwitchSensorMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsTransferSwitchSensorMinTimeStamp.setStatus("current")
_MeasurementsTransferSwitchSensorMaxValue_Type = Unsigned32
_MeasurementsTransferSwitchSensorMaxValue_Object = MibTableColumn
measurementsTransferSwitchSensorMaxValue = _MeasurementsTransferSwitchSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7, 3, 1, 11),
    _MeasurementsTransferSwitchSensorMaxValue_Type()
)
measurementsTransferSwitchSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsTransferSwitchSensorMaxValue.setStatus("current")
_MeasurementsTransferSwitchSensorSignedMaxValue_Type = Integer32
_MeasurementsTransferSwitchSensorSignedMaxValue_Object = MibTableColumn
measurementsTransferSwitchSensorSignedMaxValue = _MeasurementsTransferSwitchSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7, 3, 1, 12),
    _MeasurementsTransferSwitchSensorSignedMaxValue_Type()
)
measurementsTransferSwitchSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsTransferSwitchSensorSignedMaxValue.setStatus("current")
_MeasurementsTransferSwitchSensorMaxTimeStamp_Type = Unsigned32
_MeasurementsTransferSwitchSensorMaxTimeStamp_Object = MibTableColumn
measurementsTransferSwitchSensorMaxTimeStamp = _MeasurementsTransferSwitchSensorMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7, 3, 1, 13),
    _MeasurementsTransferSwitchSensorMaxTimeStamp_Type()
)
measurementsTransferSwitchSensorMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsTransferSwitchSensorMaxTimeStamp.setStatus("current")
_MeasurementsTransferSwitchSensorMinMaxResetTimeStamp_Type = Unsigned32
_MeasurementsTransferSwitchSensorMinMaxResetTimeStamp_Object = MibTableColumn
measurementsTransferSwitchSensorMinMaxResetTimeStamp = _MeasurementsTransferSwitchSensorMinMaxResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 7, 3, 1, 14),
    _MeasurementsTransferSwitchSensorMinMaxResetTimeStamp_Type()
)
measurementsTransferSwitchSensorMinMaxResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsTransferSwitchSensorMinMaxResetTimeStamp.setStatus("current")
_MeasurementsCircuit_ObjectIdentity = ObjectIdentity
measurementsCircuit = _MeasurementsCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8)
)
_CircuitSensorMeasurementsTable_Object = MibTable
circuitSensorMeasurementsTable = _CircuitSensorMeasurementsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3)
)
if mibBuilder.loadTexts:
    circuitSensorMeasurementsTable.setStatus("current")
_CircuitSensorMeasurementsEntry_Object = MibTableRow
circuitSensorMeasurementsEntry = _CircuitSensorMeasurementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3, 1)
)
circuitSensorMeasurementsEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "circuitId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    circuitSensorMeasurementsEntry.setStatus("current")
_MeasurementsCircuitSensorIsAvailable_Type = TruthValue
_MeasurementsCircuitSensorIsAvailable_Object = MibTableColumn
measurementsCircuitSensorIsAvailable = _MeasurementsCircuitSensorIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3, 1, 2),
    _MeasurementsCircuitSensorIsAvailable_Type()
)
measurementsCircuitSensorIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitSensorIsAvailable.setStatus("current")
_MeasurementsCircuitSensorState_Type = SensorStateEnumeration
_MeasurementsCircuitSensorState_Object = MibTableColumn
measurementsCircuitSensorState = _MeasurementsCircuitSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3, 1, 3),
    _MeasurementsCircuitSensorState_Type()
)
measurementsCircuitSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitSensorState.setStatus("current")
_MeasurementsCircuitSensorValue_Type = Unsigned32
_MeasurementsCircuitSensorValue_Object = MibTableColumn
measurementsCircuitSensorValue = _MeasurementsCircuitSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3, 1, 4),
    _MeasurementsCircuitSensorValue_Type()
)
measurementsCircuitSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitSensorValue.setStatus("current")
_MeasurementsCircuitSensorTimeStamp_Type = Unsigned32
_MeasurementsCircuitSensorTimeStamp_Object = MibTableColumn
measurementsCircuitSensorTimeStamp = _MeasurementsCircuitSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3, 1, 5),
    _MeasurementsCircuitSensorTimeStamp_Type()
)
measurementsCircuitSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitSensorTimeStamp.setStatus("current")
_MeasurementsCircuitSensorSignedValue_Type = Integer32
_MeasurementsCircuitSensorSignedValue_Object = MibTableColumn
measurementsCircuitSensorSignedValue = _MeasurementsCircuitSensorSignedValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3, 1, 6),
    _MeasurementsCircuitSensorSignedValue_Type()
)
measurementsCircuitSensorSignedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitSensorSignedValue.setStatus("current")
_MeasurementsCircuitSensorMinMaxValid_Type = TruthValue
_MeasurementsCircuitSensorMinMaxValid_Object = MibTableColumn
measurementsCircuitSensorMinMaxValid = _MeasurementsCircuitSensorMinMaxValid_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3, 1, 7),
    _MeasurementsCircuitSensorMinMaxValid_Type()
)
measurementsCircuitSensorMinMaxValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitSensorMinMaxValid.setStatus("current")
_MeasurementsCircuitSensorMinValue_Type = Unsigned32
_MeasurementsCircuitSensorMinValue_Object = MibTableColumn
measurementsCircuitSensorMinValue = _MeasurementsCircuitSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3, 1, 8),
    _MeasurementsCircuitSensorMinValue_Type()
)
measurementsCircuitSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitSensorMinValue.setStatus("current")
_MeasurementsCircuitSensorSignedMinValue_Type = Integer32
_MeasurementsCircuitSensorSignedMinValue_Object = MibTableColumn
measurementsCircuitSensorSignedMinValue = _MeasurementsCircuitSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3, 1, 9),
    _MeasurementsCircuitSensorSignedMinValue_Type()
)
measurementsCircuitSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitSensorSignedMinValue.setStatus("current")
_MeasurementsCircuitSensorMinTimeStamp_Type = Unsigned32
_MeasurementsCircuitSensorMinTimeStamp_Object = MibTableColumn
measurementsCircuitSensorMinTimeStamp = _MeasurementsCircuitSensorMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3, 1, 10),
    _MeasurementsCircuitSensorMinTimeStamp_Type()
)
measurementsCircuitSensorMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitSensorMinTimeStamp.setStatus("current")
_MeasurementsCircuitSensorMaxValue_Type = Unsigned32
_MeasurementsCircuitSensorMaxValue_Object = MibTableColumn
measurementsCircuitSensorMaxValue = _MeasurementsCircuitSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3, 1, 11),
    _MeasurementsCircuitSensorMaxValue_Type()
)
measurementsCircuitSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitSensorMaxValue.setStatus("current")
_MeasurementsCircuitSensorSignedMaxValue_Type = Integer32
_MeasurementsCircuitSensorSignedMaxValue_Object = MibTableColumn
measurementsCircuitSensorSignedMaxValue = _MeasurementsCircuitSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3, 1, 12),
    _MeasurementsCircuitSensorSignedMaxValue_Type()
)
measurementsCircuitSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitSensorSignedMaxValue.setStatus("current")
_MeasurementsCircuitSensorMaxTimeStamp_Type = Unsigned32
_MeasurementsCircuitSensorMaxTimeStamp_Object = MibTableColumn
measurementsCircuitSensorMaxTimeStamp = _MeasurementsCircuitSensorMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3, 1, 13),
    _MeasurementsCircuitSensorMaxTimeStamp_Type()
)
measurementsCircuitSensorMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitSensorMaxTimeStamp.setStatus("current")
_MeasurementsCircuitSensorMinMaxResetTimeStamp_Type = Unsigned32
_MeasurementsCircuitSensorMinMaxResetTimeStamp_Object = MibTableColumn
measurementsCircuitSensorMinMaxResetTimeStamp = _MeasurementsCircuitSensorMinMaxResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3, 1, 14),
    _MeasurementsCircuitSensorMinMaxResetTimeStamp_Type()
)
measurementsCircuitSensorMinMaxResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitSensorMinMaxResetTimeStamp.setStatus("current")
_MeasurementsCircuitSensorResetTimeStamp_Type = Unsigned32
_MeasurementsCircuitSensorResetTimeStamp_Object = MibTableColumn
measurementsCircuitSensorResetTimeStamp = _MeasurementsCircuitSensorResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 3, 1, 15),
    _MeasurementsCircuitSensorResetTimeStamp_Type()
)
measurementsCircuitSensorResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitSensorResetTimeStamp.setStatus("current")
_CircuitPoleSensorMeasurementsTable_Object = MibTable
circuitPoleSensorMeasurementsTable = _CircuitPoleSensorMeasurementsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 4)
)
if mibBuilder.loadTexts:
    circuitPoleSensorMeasurementsTable.setStatus("current")
_CircuitPoleSensorMeasurementsEntry_Object = MibTableRow
circuitPoleSensorMeasurementsEntry = _CircuitPoleSensorMeasurementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 4, 1)
)
circuitPoleSensorMeasurementsEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "circuitId"),
    (0, "PDU2-MIB", "circuitPoleId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    circuitPoleSensorMeasurementsEntry.setStatus("current")
_MeasurementsCircuitPoleSensorIsAvailable_Type = TruthValue
_MeasurementsCircuitPoleSensorIsAvailable_Object = MibTableColumn
measurementsCircuitPoleSensorIsAvailable = _MeasurementsCircuitPoleSensorIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 4, 1, 2),
    _MeasurementsCircuitPoleSensorIsAvailable_Type()
)
measurementsCircuitPoleSensorIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitPoleSensorIsAvailable.setStatus("current")
_MeasurementsCircuitPoleSensorState_Type = SensorStateEnumeration
_MeasurementsCircuitPoleSensorState_Object = MibTableColumn
measurementsCircuitPoleSensorState = _MeasurementsCircuitPoleSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 4, 1, 3),
    _MeasurementsCircuitPoleSensorState_Type()
)
measurementsCircuitPoleSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitPoleSensorState.setStatus("current")
_MeasurementsCircuitPoleSensorValue_Type = Unsigned32
_MeasurementsCircuitPoleSensorValue_Object = MibTableColumn
measurementsCircuitPoleSensorValue = _MeasurementsCircuitPoleSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 4, 1, 4),
    _MeasurementsCircuitPoleSensorValue_Type()
)
measurementsCircuitPoleSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitPoleSensorValue.setStatus("current")
_MeasurementsCircuitPoleSensorTimeStamp_Type = Unsigned32
_MeasurementsCircuitPoleSensorTimeStamp_Object = MibTableColumn
measurementsCircuitPoleSensorTimeStamp = _MeasurementsCircuitPoleSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 4, 1, 5),
    _MeasurementsCircuitPoleSensorTimeStamp_Type()
)
measurementsCircuitPoleSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitPoleSensorTimeStamp.setStatus("current")
_MeasurementsCircuitPoleSensorSignedValue_Type = Integer32
_MeasurementsCircuitPoleSensorSignedValue_Object = MibTableColumn
measurementsCircuitPoleSensorSignedValue = _MeasurementsCircuitPoleSensorSignedValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 4, 1, 6),
    _MeasurementsCircuitPoleSensorSignedValue_Type()
)
measurementsCircuitPoleSensorSignedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitPoleSensorSignedValue.setStatus("current")
_MeasurementsCircuitPoleSensorMinMaxValid_Type = TruthValue
_MeasurementsCircuitPoleSensorMinMaxValid_Object = MibTableColumn
measurementsCircuitPoleSensorMinMaxValid = _MeasurementsCircuitPoleSensorMinMaxValid_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 4, 1, 7),
    _MeasurementsCircuitPoleSensorMinMaxValid_Type()
)
measurementsCircuitPoleSensorMinMaxValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitPoleSensorMinMaxValid.setStatus("current")
_MeasurementsCircuitPoleSensorMinValue_Type = Unsigned32
_MeasurementsCircuitPoleSensorMinValue_Object = MibTableColumn
measurementsCircuitPoleSensorMinValue = _MeasurementsCircuitPoleSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 4, 1, 8),
    _MeasurementsCircuitPoleSensorMinValue_Type()
)
measurementsCircuitPoleSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitPoleSensorMinValue.setStatus("current")
_MeasurementsCircuitPoleSensorSignedMinValue_Type = Integer32
_MeasurementsCircuitPoleSensorSignedMinValue_Object = MibTableColumn
measurementsCircuitPoleSensorSignedMinValue = _MeasurementsCircuitPoleSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 4, 1, 9),
    _MeasurementsCircuitPoleSensorSignedMinValue_Type()
)
measurementsCircuitPoleSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitPoleSensorSignedMinValue.setStatus("current")
_MeasurementsCircuitPoleSensorMinTimeStamp_Type = Unsigned32
_MeasurementsCircuitPoleSensorMinTimeStamp_Object = MibTableColumn
measurementsCircuitPoleSensorMinTimeStamp = _MeasurementsCircuitPoleSensorMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 4, 1, 10),
    _MeasurementsCircuitPoleSensorMinTimeStamp_Type()
)
measurementsCircuitPoleSensorMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitPoleSensorMinTimeStamp.setStatus("current")
_MeasurementsCircuitPoleSensorMaxValue_Type = Unsigned32
_MeasurementsCircuitPoleSensorMaxValue_Object = MibTableColumn
measurementsCircuitPoleSensorMaxValue = _MeasurementsCircuitPoleSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 4, 1, 11),
    _MeasurementsCircuitPoleSensorMaxValue_Type()
)
measurementsCircuitPoleSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitPoleSensorMaxValue.setStatus("current")
_MeasurementsCircuitPoleSensorSignedMaxValue_Type = Integer32
_MeasurementsCircuitPoleSensorSignedMaxValue_Object = MibTableColumn
measurementsCircuitPoleSensorSignedMaxValue = _MeasurementsCircuitPoleSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 4, 1, 12),
    _MeasurementsCircuitPoleSensorSignedMaxValue_Type()
)
measurementsCircuitPoleSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitPoleSensorSignedMaxValue.setStatus("current")
_MeasurementsCircuitPoleSensorMaxTimeStamp_Type = Unsigned32
_MeasurementsCircuitPoleSensorMaxTimeStamp_Object = MibTableColumn
measurementsCircuitPoleSensorMaxTimeStamp = _MeasurementsCircuitPoleSensorMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 4, 1, 13),
    _MeasurementsCircuitPoleSensorMaxTimeStamp_Type()
)
measurementsCircuitPoleSensorMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitPoleSensorMaxTimeStamp.setStatus("current")
_MeasurementsCircuitPoleSensorMinMaxResetTimeStamp_Type = Unsigned32
_MeasurementsCircuitPoleSensorMinMaxResetTimeStamp_Object = MibTableColumn
measurementsCircuitPoleSensorMinMaxResetTimeStamp = _MeasurementsCircuitPoleSensorMinMaxResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 8, 4, 1, 14),
    _MeasurementsCircuitPoleSensorMinMaxResetTimeStamp_Type()
)
measurementsCircuitPoleSensorMinMaxResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsCircuitPoleSensorMinMaxResetTimeStamp.setStatus("current")
_MeasurementsOutletGroup_ObjectIdentity = ObjectIdentity
measurementsOutletGroup = _MeasurementsOutletGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9)
)
_OutletGroupSensorMeasurementsTable_Object = MibTable
outletGroupSensorMeasurementsTable = _OutletGroupSensorMeasurementsTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3)
)
if mibBuilder.loadTexts:
    outletGroupSensorMeasurementsTable.setStatus("current")
_OutletGroupSensorMeasurementsEntry_Object = MibTableRow
outletGroupSensorMeasurementsEntry = _OutletGroupSensorMeasurementsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3, 1)
)
outletGroupSensorMeasurementsEntry.setIndexNames(
    (0, "PDU2-MIB", "outletGroupId"),
    (0, "PDU2-MIB", "sensorType"),
)
if mibBuilder.loadTexts:
    outletGroupSensorMeasurementsEntry.setStatus("current")
_MeasurementsOutletGroupSensorIsAvailable_Type = TruthValue
_MeasurementsOutletGroupSensorIsAvailable_Object = MibTableColumn
measurementsOutletGroupSensorIsAvailable = _MeasurementsOutletGroupSensorIsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3, 1, 2),
    _MeasurementsOutletGroupSensorIsAvailable_Type()
)
measurementsOutletGroupSensorIsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletGroupSensorIsAvailable.setStatus("current")
_MeasurementsOutletGroupSensorState_Type = SensorStateEnumeration
_MeasurementsOutletGroupSensorState_Object = MibTableColumn
measurementsOutletGroupSensorState = _MeasurementsOutletGroupSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3, 1, 3),
    _MeasurementsOutletGroupSensorState_Type()
)
measurementsOutletGroupSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletGroupSensorState.setStatus("current")
_MeasurementsOutletGroupSensorValue_Type = Unsigned32
_MeasurementsOutletGroupSensorValue_Object = MibTableColumn
measurementsOutletGroupSensorValue = _MeasurementsOutletGroupSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3, 1, 4),
    _MeasurementsOutletGroupSensorValue_Type()
)
measurementsOutletGroupSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletGroupSensorValue.setStatus("current")
_MeasurementsOutletGroupSensorTimeStamp_Type = Unsigned32
_MeasurementsOutletGroupSensorTimeStamp_Object = MibTableColumn
measurementsOutletGroupSensorTimeStamp = _MeasurementsOutletGroupSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3, 1, 5),
    _MeasurementsOutletGroupSensorTimeStamp_Type()
)
measurementsOutletGroupSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletGroupSensorTimeStamp.setStatus("current")
_MeasurementsOutletGroupSensorSignedValue_Type = Integer32
_MeasurementsOutletGroupSensorSignedValue_Object = MibTableColumn
measurementsOutletGroupSensorSignedValue = _MeasurementsOutletGroupSensorSignedValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3, 1, 6),
    _MeasurementsOutletGroupSensorSignedValue_Type()
)
measurementsOutletGroupSensorSignedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletGroupSensorSignedValue.setStatus("current")
_MeasurementsOutletGroupSensorMinMaxValid_Type = TruthValue
_MeasurementsOutletGroupSensorMinMaxValid_Object = MibTableColumn
measurementsOutletGroupSensorMinMaxValid = _MeasurementsOutletGroupSensorMinMaxValid_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3, 1, 7),
    _MeasurementsOutletGroupSensorMinMaxValid_Type()
)
measurementsOutletGroupSensorMinMaxValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletGroupSensorMinMaxValid.setStatus("current")
_MeasurementsOutletGroupSensorMinValue_Type = Unsigned32
_MeasurementsOutletGroupSensorMinValue_Object = MibTableColumn
measurementsOutletGroupSensorMinValue = _MeasurementsOutletGroupSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3, 1, 8),
    _MeasurementsOutletGroupSensorMinValue_Type()
)
measurementsOutletGroupSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletGroupSensorMinValue.setStatus("current")
_MeasurementsOutletGroupSensorSignedMinValue_Type = Integer32
_MeasurementsOutletGroupSensorSignedMinValue_Object = MibTableColumn
measurementsOutletGroupSensorSignedMinValue = _MeasurementsOutletGroupSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3, 1, 9),
    _MeasurementsOutletGroupSensorSignedMinValue_Type()
)
measurementsOutletGroupSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletGroupSensorSignedMinValue.setStatus("current")
_MeasurementsOutletGroupSensorMinTimeStamp_Type = Unsigned32
_MeasurementsOutletGroupSensorMinTimeStamp_Object = MibTableColumn
measurementsOutletGroupSensorMinTimeStamp = _MeasurementsOutletGroupSensorMinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3, 1, 10),
    _MeasurementsOutletGroupSensorMinTimeStamp_Type()
)
measurementsOutletGroupSensorMinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletGroupSensorMinTimeStamp.setStatus("current")
_MeasurementsOutletGroupSensorMaxValue_Type = Unsigned32
_MeasurementsOutletGroupSensorMaxValue_Object = MibTableColumn
measurementsOutletGroupSensorMaxValue = _MeasurementsOutletGroupSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3, 1, 11),
    _MeasurementsOutletGroupSensorMaxValue_Type()
)
measurementsOutletGroupSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletGroupSensorMaxValue.setStatus("current")
_MeasurementsOutletGroupSensorSignedMaxValue_Type = Integer32
_MeasurementsOutletGroupSensorSignedMaxValue_Object = MibTableColumn
measurementsOutletGroupSensorSignedMaxValue = _MeasurementsOutletGroupSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3, 1, 12),
    _MeasurementsOutletGroupSensorSignedMaxValue_Type()
)
measurementsOutletGroupSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletGroupSensorSignedMaxValue.setStatus("current")
_MeasurementsOutletGroupSensorMaxTimeStamp_Type = Unsigned32
_MeasurementsOutletGroupSensorMaxTimeStamp_Object = MibTableColumn
measurementsOutletGroupSensorMaxTimeStamp = _MeasurementsOutletGroupSensorMaxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3, 1, 13),
    _MeasurementsOutletGroupSensorMaxTimeStamp_Type()
)
measurementsOutletGroupSensorMaxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletGroupSensorMaxTimeStamp.setStatus("current")
_MeasurementsOutletGroupSensorMinMaxResetTimeStamp_Type = Unsigned32
_MeasurementsOutletGroupSensorMinMaxResetTimeStamp_Object = MibTableColumn
measurementsOutletGroupSensorMinMaxResetTimeStamp = _MeasurementsOutletGroupSensorMinMaxResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3, 1, 14),
    _MeasurementsOutletGroupSensorMinMaxResetTimeStamp_Type()
)
measurementsOutletGroupSensorMinMaxResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletGroupSensorMinMaxResetTimeStamp.setStatus("current")
_MeasurementsOutletGroupSensorResetTimeStamp_Type = Unsigned32
_MeasurementsOutletGroupSensorResetTimeStamp_Object = MibTableColumn
measurementsOutletGroupSensorResetTimeStamp = _MeasurementsOutletGroupSensorResetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 5, 9, 3, 1, 15),
    _MeasurementsOutletGroupSensorResetTimeStamp_Type()
)
measurementsOutletGroupSensorResetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementsOutletGroupSensorResetTimeStamp.setStatus("current")
_Log_ObjectIdentity = ObjectIdentity
log = _Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6)
)
_LogUnit_ObjectIdentity = ObjectIdentity
logUnit = _LogUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1)
)
_LogIndexTable_Object = MibTable
logIndexTable = _LogIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 1)
)
if mibBuilder.loadTexts:
    logIndexTable.setStatus("current")
_LogIndexEntry_Object = MibTableRow
logIndexEntry = _LogIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 1, 1)
)
logIndexEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
)
if mibBuilder.loadTexts:
    logIndexEntry.setStatus("current")
_OldestLogID_Type = Integer32
_OldestLogID_Object = MibTableColumn
oldestLogID = _OldestLogID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 1, 1, 2),
    _OldestLogID_Type()
)
oldestLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oldestLogID.setStatus("current")
_NewestLogID_Type = Integer32
_NewestLogID_Object = MibTableColumn
newestLogID = _NewestLogID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 1, 1, 3),
    _NewestLogID_Type()
)
newestLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newestLogID.setStatus("current")
_LogTimeStampTable_Object = MibTable
logTimeStampTable = _LogTimeStampTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 2)
)
if mibBuilder.loadTexts:
    logTimeStampTable.setStatus("current")
_LogTimeStampEntry_Object = MibTableRow
logTimeStampEntry = _LogTimeStampEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 2, 1)
)
logTimeStampEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    logTimeStampEntry.setStatus("current")


class _LogIndex_Type(Integer32):
    """Custom type logIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_LogIndex_Type.__name__ = "Integer32"
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 2, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    logIndex.setStatus("current")
_LogTimeStamp_Type = Unsigned32
_LogTimeStamp_Object = MibTableColumn
logTimeStamp = _LogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 2, 1, 2),
    _LogTimeStamp_Type()
)
logTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTimeStamp.setStatus("current")
_UnitSensorLogTable_Object = MibTable
unitSensorLogTable = _UnitSensorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 3)
)
if mibBuilder.loadTexts:
    unitSensorLogTable.setStatus("current")
_UnitSensorLogEntry_Object = MibTableRow
unitSensorLogEntry = _UnitSensorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 3, 1)
)
unitSensorLogEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "sensorType"),
    (0, "PDU2-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    unitSensorLogEntry.setStatus("current")
_LogUnitSensorDataAvailable_Type = TruthValue
_LogUnitSensorDataAvailable_Object = MibTableColumn
logUnitSensorDataAvailable = _LogUnitSensorDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 3, 1, 2),
    _LogUnitSensorDataAvailable_Type()
)
logUnitSensorDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logUnitSensorDataAvailable.setStatus("current")
_LogUnitSensorState_Type = SensorStateEnumeration
_LogUnitSensorState_Object = MibTableColumn
logUnitSensorState = _LogUnitSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 3, 1, 3),
    _LogUnitSensorState_Type()
)
logUnitSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logUnitSensorState.setStatus("current")
_LogUnitSensorAvgValue_Type = Unsigned32
_LogUnitSensorAvgValue_Object = MibTableColumn
logUnitSensorAvgValue = _LogUnitSensorAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 3, 1, 4),
    _LogUnitSensorAvgValue_Type()
)
logUnitSensorAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logUnitSensorAvgValue.setStatus("current")
_LogUnitSensorMaxValue_Type = Unsigned32
_LogUnitSensorMaxValue_Object = MibTableColumn
logUnitSensorMaxValue = _LogUnitSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 3, 1, 5),
    _LogUnitSensorMaxValue_Type()
)
logUnitSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logUnitSensorMaxValue.setStatus("current")
_LogUnitSensorMinValue_Type = Unsigned32
_LogUnitSensorMinValue_Object = MibTableColumn
logUnitSensorMinValue = _LogUnitSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 3, 1, 6),
    _LogUnitSensorMinValue_Type()
)
logUnitSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logUnitSensorMinValue.setStatus("current")
_LogUnitSensorSignedAvgValue_Type = Integer32
_LogUnitSensorSignedAvgValue_Object = MibTableColumn
logUnitSensorSignedAvgValue = _LogUnitSensorSignedAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 3, 1, 7),
    _LogUnitSensorSignedAvgValue_Type()
)
logUnitSensorSignedAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logUnitSensorSignedAvgValue.setStatus("current")
_LogUnitSensorSignedMaxValue_Type = Integer32
_LogUnitSensorSignedMaxValue_Object = MibTableColumn
logUnitSensorSignedMaxValue = _LogUnitSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 3, 1, 8),
    _LogUnitSensorSignedMaxValue_Type()
)
logUnitSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logUnitSensorSignedMaxValue.setStatus("current")
_LogUnitSensorSignedMinValue_Type = Integer32
_LogUnitSensorSignedMinValue_Object = MibTableColumn
logUnitSensorSignedMinValue = _LogUnitSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 1, 3, 1, 9),
    _LogUnitSensorSignedMinValue_Type()
)
logUnitSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logUnitSensorSignedMinValue.setStatus("current")
_LogInlet_ObjectIdentity = ObjectIdentity
logInlet = _LogInlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2)
)
_InletSensorLogTable_Object = MibTable
inletSensorLogTable = _InletSensorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 3)
)
if mibBuilder.loadTexts:
    inletSensorLogTable.setStatus("current")
_InletSensorLogEntry_Object = MibTableRow
inletSensorLogEntry = _InletSensorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 3, 1)
)
inletSensorLogEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
    (0, "PDU2-MIB", "sensorType"),
    (0, "PDU2-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    inletSensorLogEntry.setStatus("current")
_LogInletSensorDataAvailable_Type = TruthValue
_LogInletSensorDataAvailable_Object = MibTableColumn
logInletSensorDataAvailable = _LogInletSensorDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 3, 1, 2),
    _LogInletSensorDataAvailable_Type()
)
logInletSensorDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletSensorDataAvailable.setStatus("current")
_LogInletSensorState_Type = SensorStateEnumeration
_LogInletSensorState_Object = MibTableColumn
logInletSensorState = _LogInletSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 3, 1, 3),
    _LogInletSensorState_Type()
)
logInletSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletSensorState.setStatus("current")
_LogInletSensorAvgValue_Type = Unsigned32
_LogInletSensorAvgValue_Object = MibTableColumn
logInletSensorAvgValue = _LogInletSensorAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 3, 1, 4),
    _LogInletSensorAvgValue_Type()
)
logInletSensorAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletSensorAvgValue.setStatus("current")
_LogInletSensorMaxValue_Type = Unsigned32
_LogInletSensorMaxValue_Object = MibTableColumn
logInletSensorMaxValue = _LogInletSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 3, 1, 5),
    _LogInletSensorMaxValue_Type()
)
logInletSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletSensorMaxValue.setStatus("current")
_LogInletSensorMinValue_Type = Unsigned32
_LogInletSensorMinValue_Object = MibTableColumn
logInletSensorMinValue = _LogInletSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 3, 1, 6),
    _LogInletSensorMinValue_Type()
)
logInletSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletSensorMinValue.setStatus("current")
_LogInletSensorSignedAvgValue_Type = Integer32
_LogInletSensorSignedAvgValue_Object = MibTableColumn
logInletSensorSignedAvgValue = _LogInletSensorSignedAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 3, 1, 7),
    _LogInletSensorSignedAvgValue_Type()
)
logInletSensorSignedAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletSensorSignedAvgValue.setStatus("current")
_LogInletSensorSignedMaxValue_Type = Integer32
_LogInletSensorSignedMaxValue_Object = MibTableColumn
logInletSensorSignedMaxValue = _LogInletSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 3, 1, 8),
    _LogInletSensorSignedMaxValue_Type()
)
logInletSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletSensorSignedMaxValue.setStatus("current")
_LogInletSensorSignedMinValue_Type = Integer32
_LogInletSensorSignedMinValue_Object = MibTableColumn
logInletSensorSignedMinValue = _LogInletSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 3, 1, 9),
    _LogInletSensorSignedMinValue_Type()
)
logInletSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletSensorSignedMinValue.setStatus("current")
_InletPoleSensorLogTable_Object = MibTable
inletPoleSensorLogTable = _InletPoleSensorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 4)
)
if mibBuilder.loadTexts:
    inletPoleSensorLogTable.setStatus("current")
_InletPoleSensorLogEntry_Object = MibTableRow
inletPoleSensorLogEntry = _InletPoleSensorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 4, 1)
)
inletPoleSensorLogEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
    (0, "PDU2-MIB", "inletPoleIndex"),
    (0, "PDU2-MIB", "sensorType"),
    (0, "PDU2-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    inletPoleSensorLogEntry.setStatus("current")
_LogInletPoleSensorDataAvailable_Type = TruthValue
_LogInletPoleSensorDataAvailable_Object = MibTableColumn
logInletPoleSensorDataAvailable = _LogInletPoleSensorDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 4, 1, 2),
    _LogInletPoleSensorDataAvailable_Type()
)
logInletPoleSensorDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletPoleSensorDataAvailable.setStatus("current")
_LogInletPoleSensorState_Type = SensorStateEnumeration
_LogInletPoleSensorState_Object = MibTableColumn
logInletPoleSensorState = _LogInletPoleSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 4, 1, 3),
    _LogInletPoleSensorState_Type()
)
logInletPoleSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletPoleSensorState.setStatus("current")
_LogInletPoleSensorAvgValue_Type = Unsigned32
_LogInletPoleSensorAvgValue_Object = MibTableColumn
logInletPoleSensorAvgValue = _LogInletPoleSensorAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 4, 1, 4),
    _LogInletPoleSensorAvgValue_Type()
)
logInletPoleSensorAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletPoleSensorAvgValue.setStatus("current")
_LogInletPoleSensorMaxValue_Type = Unsigned32
_LogInletPoleSensorMaxValue_Object = MibTableColumn
logInletPoleSensorMaxValue = _LogInletPoleSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 4, 1, 5),
    _LogInletPoleSensorMaxValue_Type()
)
logInletPoleSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletPoleSensorMaxValue.setStatus("current")
_LogInletPoleSensorMinValue_Type = Unsigned32
_LogInletPoleSensorMinValue_Object = MibTableColumn
logInletPoleSensorMinValue = _LogInletPoleSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 4, 1, 6),
    _LogInletPoleSensorMinValue_Type()
)
logInletPoleSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletPoleSensorMinValue.setStatus("current")
_LogInletPoleSensorSignedAvgValue_Type = Integer32
_LogInletPoleSensorSignedAvgValue_Object = MibTableColumn
logInletPoleSensorSignedAvgValue = _LogInletPoleSensorSignedAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 4, 1, 7),
    _LogInletPoleSensorSignedAvgValue_Type()
)
logInletPoleSensorSignedAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletPoleSensorSignedAvgValue.setStatus("current")
_LogInletPoleSensorSignedMaxValue_Type = Integer32
_LogInletPoleSensorSignedMaxValue_Object = MibTableColumn
logInletPoleSensorSignedMaxValue = _LogInletPoleSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 4, 1, 8),
    _LogInletPoleSensorSignedMaxValue_Type()
)
logInletPoleSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletPoleSensorSignedMaxValue.setStatus("current")
_LogInletPoleSensorSignedMinValue_Type = Integer32
_LogInletPoleSensorSignedMinValue_Object = MibTableColumn
logInletPoleSensorSignedMinValue = _LogInletPoleSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 4, 1, 9),
    _LogInletPoleSensorSignedMinValue_Type()
)
logInletPoleSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletPoleSensorSignedMinValue.setStatus("current")
_InletLinePairSensorLogTable_Object = MibTable
inletLinePairSensorLogTable = _InletLinePairSensorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 5)
)
if mibBuilder.loadTexts:
    inletLinePairSensorLogTable.setStatus("current")
_InletLinePairSensorLogEntry_Object = MibTableRow
inletLinePairSensorLogEntry = _InletLinePairSensorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 5, 1)
)
inletLinePairSensorLogEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "inletId"),
    (0, "PDU2-MIB", "inletLinePairIndex"),
    (0, "PDU2-MIB", "sensorType"),
    (0, "PDU2-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    inletLinePairSensorLogEntry.setStatus("current")
_LogInletLinePairSensorDataAvailable_Type = TruthValue
_LogInletLinePairSensorDataAvailable_Object = MibTableColumn
logInletLinePairSensorDataAvailable = _LogInletLinePairSensorDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 5, 1, 2),
    _LogInletLinePairSensorDataAvailable_Type()
)
logInletLinePairSensorDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletLinePairSensorDataAvailable.setStatus("current")
_LogInletLinePairSensorState_Type = SensorStateEnumeration
_LogInletLinePairSensorState_Object = MibTableColumn
logInletLinePairSensorState = _LogInletLinePairSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 5, 1, 3),
    _LogInletLinePairSensorState_Type()
)
logInletLinePairSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletLinePairSensorState.setStatus("current")
_LogInletLinePairSensorAvgValue_Type = Unsigned32
_LogInletLinePairSensorAvgValue_Object = MibTableColumn
logInletLinePairSensorAvgValue = _LogInletLinePairSensorAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 5, 1, 4),
    _LogInletLinePairSensorAvgValue_Type()
)
logInletLinePairSensorAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletLinePairSensorAvgValue.setStatus("current")
_LogInletLinePairSensorMaxValue_Type = Unsigned32
_LogInletLinePairSensorMaxValue_Object = MibTableColumn
logInletLinePairSensorMaxValue = _LogInletLinePairSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 5, 1, 5),
    _LogInletLinePairSensorMaxValue_Type()
)
logInletLinePairSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletLinePairSensorMaxValue.setStatus("current")
_LogInletLinePairSensorMinValue_Type = Unsigned32
_LogInletLinePairSensorMinValue_Object = MibTableColumn
logInletLinePairSensorMinValue = _LogInletLinePairSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 5, 1, 6),
    _LogInletLinePairSensorMinValue_Type()
)
logInletLinePairSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletLinePairSensorMinValue.setStatus("current")
_LogInletLinePairSensorSignedAvgValue_Type = Integer32
_LogInletLinePairSensorSignedAvgValue_Object = MibTableColumn
logInletLinePairSensorSignedAvgValue = _LogInletLinePairSensorSignedAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 5, 1, 7),
    _LogInletLinePairSensorSignedAvgValue_Type()
)
logInletLinePairSensorSignedAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletLinePairSensorSignedAvgValue.setStatus("current")
_LogInletLinePairSensorSignedMaxValue_Type = Integer32
_LogInletLinePairSensorSignedMaxValue_Object = MibTableColumn
logInletLinePairSensorSignedMaxValue = _LogInletLinePairSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 5, 1, 8),
    _LogInletLinePairSensorSignedMaxValue_Type()
)
logInletLinePairSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletLinePairSensorSignedMaxValue.setStatus("current")
_LogInletLinePairSensorSignedMinValue_Type = Integer32
_LogInletLinePairSensorSignedMinValue_Object = MibTableColumn
logInletLinePairSensorSignedMinValue = _LogInletLinePairSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 2, 5, 1, 9),
    _LogInletLinePairSensorSignedMinValue_Type()
)
logInletLinePairSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logInletLinePairSensorSignedMinValue.setStatus("current")
_LogOverCurrentProtector_ObjectIdentity = ObjectIdentity
logOverCurrentProtector = _LogOverCurrentProtector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 3)
)
_OverCurrentProtectorSensorLogTable_Object = MibTable
overCurrentProtectorSensorLogTable = _OverCurrentProtectorSensorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 3, 3)
)
if mibBuilder.loadTexts:
    overCurrentProtectorSensorLogTable.setStatus("current")
_OverCurrentProtectorSensorLogEntry_Object = MibTableRow
overCurrentProtectorSensorLogEntry = _OverCurrentProtectorSensorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 3, 3, 1)
)
overCurrentProtectorSensorLogEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "overCurrentProtectorIndex"),
    (0, "PDU2-MIB", "sensorType"),
    (0, "PDU2-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    overCurrentProtectorSensorLogEntry.setStatus("current")
_LogOverCurrentProtectorSensorDataAvailable_Type = TruthValue
_LogOverCurrentProtectorSensorDataAvailable_Object = MibTableColumn
logOverCurrentProtectorSensorDataAvailable = _LogOverCurrentProtectorSensorDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 3, 3, 1, 2),
    _LogOverCurrentProtectorSensorDataAvailable_Type()
)
logOverCurrentProtectorSensorDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOverCurrentProtectorSensorDataAvailable.setStatus("current")
_LogOverCurrentProtectorSensorState_Type = SensorStateEnumeration
_LogOverCurrentProtectorSensorState_Object = MibTableColumn
logOverCurrentProtectorSensorState = _LogOverCurrentProtectorSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 3, 3, 1, 3),
    _LogOverCurrentProtectorSensorState_Type()
)
logOverCurrentProtectorSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOverCurrentProtectorSensorState.setStatus("current")
_LogOverCurrentProtectorSensorAvgValue_Type = Unsigned32
_LogOverCurrentProtectorSensorAvgValue_Object = MibTableColumn
logOverCurrentProtectorSensorAvgValue = _LogOverCurrentProtectorSensorAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 3, 3, 1, 4),
    _LogOverCurrentProtectorSensorAvgValue_Type()
)
logOverCurrentProtectorSensorAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOverCurrentProtectorSensorAvgValue.setStatus("current")
_LogOverCurrentProtectorSensorMaxValue_Type = Unsigned32
_LogOverCurrentProtectorSensorMaxValue_Object = MibTableColumn
logOverCurrentProtectorSensorMaxValue = _LogOverCurrentProtectorSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 3, 3, 1, 5),
    _LogOverCurrentProtectorSensorMaxValue_Type()
)
logOverCurrentProtectorSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOverCurrentProtectorSensorMaxValue.setStatus("current")
_LogOverCurrentProtectorSensorMinValue_Type = Unsigned32
_LogOverCurrentProtectorSensorMinValue_Object = MibTableColumn
logOverCurrentProtectorSensorMinValue = _LogOverCurrentProtectorSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 3, 3, 1, 6),
    _LogOverCurrentProtectorSensorMinValue_Type()
)
logOverCurrentProtectorSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOverCurrentProtectorSensorMinValue.setStatus("current")
_LogOverCurrentProtectorSensorSignedAvgValue_Type = Integer32
_LogOverCurrentProtectorSensorSignedAvgValue_Object = MibTableColumn
logOverCurrentProtectorSensorSignedAvgValue = _LogOverCurrentProtectorSensorSignedAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 3, 3, 1, 7),
    _LogOverCurrentProtectorSensorSignedAvgValue_Type()
)
logOverCurrentProtectorSensorSignedAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOverCurrentProtectorSensorSignedAvgValue.setStatus("current")
_LogOverCurrentProtectorSensorSignedMaxValue_Type = Integer32
_LogOverCurrentProtectorSensorSignedMaxValue_Object = MibTableColumn
logOverCurrentProtectorSensorSignedMaxValue = _LogOverCurrentProtectorSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 3, 3, 1, 8),
    _LogOverCurrentProtectorSensorSignedMaxValue_Type()
)
logOverCurrentProtectorSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOverCurrentProtectorSensorSignedMaxValue.setStatus("current")
_LogOverCurrentProtectorSensorSignedMinValue_Type = Integer32
_LogOverCurrentProtectorSensorSignedMinValue_Object = MibTableColumn
logOverCurrentProtectorSensorSignedMinValue = _LogOverCurrentProtectorSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 3, 3, 1, 9),
    _LogOverCurrentProtectorSensorSignedMinValue_Type()
)
logOverCurrentProtectorSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOverCurrentProtectorSensorSignedMinValue.setStatus("current")
_LogOutlet_ObjectIdentity = ObjectIdentity
logOutlet = _LogOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4)
)
_OutletSensorLogTable_Object = MibTable
outletSensorLogTable = _OutletSensorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 3)
)
if mibBuilder.loadTexts:
    outletSensorLogTable.setStatus("current")
_OutletSensorLogEntry_Object = MibTableRow
outletSensorLogEntry = _OutletSensorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 3, 1)
)
outletSensorLogEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "outletId"),
    (0, "PDU2-MIB", "sensorType"),
    (0, "PDU2-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    outletSensorLogEntry.setStatus("current")
_LogOutletSensorDataAvailable_Type = TruthValue
_LogOutletSensorDataAvailable_Object = MibTableColumn
logOutletSensorDataAvailable = _LogOutletSensorDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 3, 1, 2),
    _LogOutletSensorDataAvailable_Type()
)
logOutletSensorDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletSensorDataAvailable.setStatus("current")
_LogOutletSensorState_Type = SensorStateEnumeration
_LogOutletSensorState_Object = MibTableColumn
logOutletSensorState = _LogOutletSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 3, 1, 3),
    _LogOutletSensorState_Type()
)
logOutletSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletSensorState.setStatus("current")
_LogOutletSensorAvgValue_Type = Unsigned32
_LogOutletSensorAvgValue_Object = MibTableColumn
logOutletSensorAvgValue = _LogOutletSensorAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 3, 1, 4),
    _LogOutletSensorAvgValue_Type()
)
logOutletSensorAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletSensorAvgValue.setStatus("current")
_LogOutletSensorMaxValue_Type = Unsigned32
_LogOutletSensorMaxValue_Object = MibTableColumn
logOutletSensorMaxValue = _LogOutletSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 3, 1, 5),
    _LogOutletSensorMaxValue_Type()
)
logOutletSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletSensorMaxValue.setStatus("current")
_LogOutletSensorMinValue_Type = Unsigned32
_LogOutletSensorMinValue_Object = MibTableColumn
logOutletSensorMinValue = _LogOutletSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 3, 1, 6),
    _LogOutletSensorMinValue_Type()
)
logOutletSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletSensorMinValue.setStatus("current")
_LogOutletSensorSignedAvgValue_Type = Integer32
_LogOutletSensorSignedAvgValue_Object = MibTableColumn
logOutletSensorSignedAvgValue = _LogOutletSensorSignedAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 3, 1, 7),
    _LogOutletSensorSignedAvgValue_Type()
)
logOutletSensorSignedAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletSensorSignedAvgValue.setStatus("current")
_LogOutletSensorSignedMaxValue_Type = Integer32
_LogOutletSensorSignedMaxValue_Object = MibTableColumn
logOutletSensorSignedMaxValue = _LogOutletSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 3, 1, 8),
    _LogOutletSensorSignedMaxValue_Type()
)
logOutletSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletSensorSignedMaxValue.setStatus("current")
_LogOutletSensorSignedMinValue_Type = Integer32
_LogOutletSensorSignedMinValue_Object = MibTableColumn
logOutletSensorSignedMinValue = _LogOutletSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 3, 1, 9),
    _LogOutletSensorSignedMinValue_Type()
)
logOutletSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletSensorSignedMinValue.setStatus("current")
_OutletPoleSensorLogTable_Object = MibTable
outletPoleSensorLogTable = _OutletPoleSensorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 4)
)
if mibBuilder.loadTexts:
    outletPoleSensorLogTable.setStatus("current")
_OutletPoleSensorLogEntry_Object = MibTableRow
outletPoleSensorLogEntry = _OutletPoleSensorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 4, 1)
)
outletPoleSensorLogEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "outletId"),
    (0, "PDU2-MIB", "outletPoleIndex"),
    (0, "PDU2-MIB", "sensorType"),
    (0, "PDU2-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    outletPoleSensorLogEntry.setStatus("current")
_LogOutletPoleSensorDataAvailable_Type = TruthValue
_LogOutletPoleSensorDataAvailable_Object = MibTableColumn
logOutletPoleSensorDataAvailable = _LogOutletPoleSensorDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 4, 1, 2),
    _LogOutletPoleSensorDataAvailable_Type()
)
logOutletPoleSensorDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletPoleSensorDataAvailable.setStatus("current")
_LogOutletPoleSensorState_Type = SensorStateEnumeration
_LogOutletPoleSensorState_Object = MibTableColumn
logOutletPoleSensorState = _LogOutletPoleSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 4, 1, 3),
    _LogOutletPoleSensorState_Type()
)
logOutletPoleSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletPoleSensorState.setStatus("current")
_LogOutletPoleSensorAvgValue_Type = Unsigned32
_LogOutletPoleSensorAvgValue_Object = MibTableColumn
logOutletPoleSensorAvgValue = _LogOutletPoleSensorAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 4, 1, 4),
    _LogOutletPoleSensorAvgValue_Type()
)
logOutletPoleSensorAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletPoleSensorAvgValue.setStatus("current")
_LogOutletPoleSensorMaxValue_Type = Unsigned32
_LogOutletPoleSensorMaxValue_Object = MibTableColumn
logOutletPoleSensorMaxValue = _LogOutletPoleSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 4, 1, 5),
    _LogOutletPoleSensorMaxValue_Type()
)
logOutletPoleSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletPoleSensorMaxValue.setStatus("current")
_LogOutletPoleSensorMinValue_Type = Unsigned32
_LogOutletPoleSensorMinValue_Object = MibTableColumn
logOutletPoleSensorMinValue = _LogOutletPoleSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 4, 1, 6),
    _LogOutletPoleSensorMinValue_Type()
)
logOutletPoleSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletPoleSensorMinValue.setStatus("current")
_LogOutletPoleSensorSignedAvgValue_Type = Integer32
_LogOutletPoleSensorSignedAvgValue_Object = MibTableColumn
logOutletPoleSensorSignedAvgValue = _LogOutletPoleSensorSignedAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 4, 1, 7),
    _LogOutletPoleSensorSignedAvgValue_Type()
)
logOutletPoleSensorSignedAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletPoleSensorSignedAvgValue.setStatus("current")
_LogOutletPoleSensorSignedMaxValue_Type = Integer32
_LogOutletPoleSensorSignedMaxValue_Object = MibTableColumn
logOutletPoleSensorSignedMaxValue = _LogOutletPoleSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 4, 1, 8),
    _LogOutletPoleSensorSignedMaxValue_Type()
)
logOutletPoleSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletPoleSensorSignedMaxValue.setStatus("current")
_LogOutletPoleSensorSignedMinValue_Type = Integer32
_LogOutletPoleSensorSignedMinValue_Object = MibTableColumn
logOutletPoleSensorSignedMinValue = _LogOutletPoleSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 4, 4, 1, 9),
    _LogOutletPoleSensorSignedMinValue_Type()
)
logOutletPoleSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletPoleSensorSignedMinValue.setStatus("current")
_LogExternalSensor_ObjectIdentity = ObjectIdentity
logExternalSensor = _LogExternalSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 5)
)
_ExternalSensorLogTable_Object = MibTable
externalSensorLogTable = _ExternalSensorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 5, 3)
)
if mibBuilder.loadTexts:
    externalSensorLogTable.setStatus("current")
_ExternalSensorLogEntry_Object = MibTableRow
externalSensorLogEntry = _ExternalSensorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 5, 3, 1)
)
externalSensorLogEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "sensorID"),
    (0, "PDU2-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    externalSensorLogEntry.setStatus("current")
_LogExternalSensorDataAvailable_Type = TruthValue
_LogExternalSensorDataAvailable_Object = MibTableColumn
logExternalSensorDataAvailable = _LogExternalSensorDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 5, 3, 1, 2),
    _LogExternalSensorDataAvailable_Type()
)
logExternalSensorDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logExternalSensorDataAvailable.setStatus("current")
_LogExternalSensorState_Type = SensorStateEnumeration
_LogExternalSensorState_Object = MibTableColumn
logExternalSensorState = _LogExternalSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 5, 3, 1, 3),
    _LogExternalSensorState_Type()
)
logExternalSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logExternalSensorState.setStatus("current")
_LogExternalSensorAvgValue_Type = Integer32
_LogExternalSensorAvgValue_Object = MibTableColumn
logExternalSensorAvgValue = _LogExternalSensorAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 5, 3, 1, 4),
    _LogExternalSensorAvgValue_Type()
)
logExternalSensorAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logExternalSensorAvgValue.setStatus("current")
_LogExternalSensorMaxValue_Type = Integer32
_LogExternalSensorMaxValue_Object = MibTableColumn
logExternalSensorMaxValue = _LogExternalSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 5, 3, 1, 5),
    _LogExternalSensorMaxValue_Type()
)
logExternalSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logExternalSensorMaxValue.setStatus("current")
_LogExternalSensorMinValue_Type = Integer32
_LogExternalSensorMinValue_Object = MibTableColumn
logExternalSensorMinValue = _LogExternalSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 5, 3, 1, 6),
    _LogExternalSensorMinValue_Type()
)
logExternalSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logExternalSensorMinValue.setStatus("current")
_LogWire_ObjectIdentity = ObjectIdentity
logWire = _LogWire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 6)
)
_WireSensorLogTable_Object = MibTable
wireSensorLogTable = _WireSensorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 6, 3)
)
if mibBuilder.loadTexts:
    wireSensorLogTable.setStatus("obsolete")
_WireSensorLogEntry_Object = MibTableRow
wireSensorLogEntry = _WireSensorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 6, 3, 1)
)
wireSensorLogEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "wireId"),
    (0, "PDU2-MIB", "sensorType"),
    (0, "PDU2-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    wireSensorLogEntry.setStatus("obsolete")
_LogWireSensorDataAvailable_Type = TruthValue
_LogWireSensorDataAvailable_Object = MibTableColumn
logWireSensorDataAvailable = _LogWireSensorDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 6, 3, 1, 2),
    _LogWireSensorDataAvailable_Type()
)
logWireSensorDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logWireSensorDataAvailable.setStatus("obsolete")
_LogWireSensorState_Type = SensorStateEnumeration
_LogWireSensorState_Object = MibTableColumn
logWireSensorState = _LogWireSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 6, 3, 1, 3),
    _LogWireSensorState_Type()
)
logWireSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logWireSensorState.setStatus("obsolete")
_LogWireSensorAvgValue_Type = Unsigned32
_LogWireSensorAvgValue_Object = MibTableColumn
logWireSensorAvgValue = _LogWireSensorAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 6, 3, 1, 4),
    _LogWireSensorAvgValue_Type()
)
logWireSensorAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logWireSensorAvgValue.setStatus("obsolete")
_LogWireSensorMaxValue_Type = Unsigned32
_LogWireSensorMaxValue_Object = MibTableColumn
logWireSensorMaxValue = _LogWireSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 6, 3, 1, 5),
    _LogWireSensorMaxValue_Type()
)
logWireSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logWireSensorMaxValue.setStatus("obsolete")
_LogWireSensorMinValue_Type = Unsigned32
_LogWireSensorMinValue_Object = MibTableColumn
logWireSensorMinValue = _LogWireSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 6, 3, 1, 6),
    _LogWireSensorMinValue_Type()
)
logWireSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logWireSensorMinValue.setStatus("obsolete")
_LogTransferSwitch_ObjectIdentity = ObjectIdentity
logTransferSwitch = _LogTransferSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 7)
)
_TransferSwitchSensorLogTable_Object = MibTable
transferSwitchSensorLogTable = _TransferSwitchSensorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 7, 3)
)
if mibBuilder.loadTexts:
    transferSwitchSensorLogTable.setStatus("current")
_TransferSwitchSensorLogEntry_Object = MibTableRow
transferSwitchSensorLogEntry = _TransferSwitchSensorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 7, 3, 1)
)
transferSwitchSensorLogEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "transferSwitchId"),
    (0, "PDU2-MIB", "sensorType"),
    (0, "PDU2-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    transferSwitchSensorLogEntry.setStatus("current")
_LogTransferSwitchSensorDataAvailable_Type = TruthValue
_LogTransferSwitchSensorDataAvailable_Object = MibTableColumn
logTransferSwitchSensorDataAvailable = _LogTransferSwitchSensorDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 7, 3, 1, 2),
    _LogTransferSwitchSensorDataAvailable_Type()
)
logTransferSwitchSensorDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTransferSwitchSensorDataAvailable.setStatus("current")
_LogTransferSwitchSensorState_Type = SensorStateEnumeration
_LogTransferSwitchSensorState_Object = MibTableColumn
logTransferSwitchSensorState = _LogTransferSwitchSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 7, 3, 1, 3),
    _LogTransferSwitchSensorState_Type()
)
logTransferSwitchSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTransferSwitchSensorState.setStatus("current")
_LogTransferSwitchSensorAvgValue_Type = Unsigned32
_LogTransferSwitchSensorAvgValue_Object = MibTableColumn
logTransferSwitchSensorAvgValue = _LogTransferSwitchSensorAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 7, 3, 1, 4),
    _LogTransferSwitchSensorAvgValue_Type()
)
logTransferSwitchSensorAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTransferSwitchSensorAvgValue.setStatus("current")
_LogTransferSwitchSensorMaxValue_Type = Unsigned32
_LogTransferSwitchSensorMaxValue_Object = MibTableColumn
logTransferSwitchSensorMaxValue = _LogTransferSwitchSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 7, 3, 1, 5),
    _LogTransferSwitchSensorMaxValue_Type()
)
logTransferSwitchSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTransferSwitchSensorMaxValue.setStatus("current")
_LogTransferSwitchSensorMinValue_Type = Unsigned32
_LogTransferSwitchSensorMinValue_Object = MibTableColumn
logTransferSwitchSensorMinValue = _LogTransferSwitchSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 7, 3, 1, 6),
    _LogTransferSwitchSensorMinValue_Type()
)
logTransferSwitchSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTransferSwitchSensorMinValue.setStatus("current")
_LogTransferSwitchSensorSignedAvgValue_Type = Integer32
_LogTransferSwitchSensorSignedAvgValue_Object = MibTableColumn
logTransferSwitchSensorSignedAvgValue = _LogTransferSwitchSensorSignedAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 7, 3, 1, 7),
    _LogTransferSwitchSensorSignedAvgValue_Type()
)
logTransferSwitchSensorSignedAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTransferSwitchSensorSignedAvgValue.setStatus("current")
_LogTransferSwitchSensorSignedMaxValue_Type = Integer32
_LogTransferSwitchSensorSignedMaxValue_Object = MibTableColumn
logTransferSwitchSensorSignedMaxValue = _LogTransferSwitchSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 7, 3, 1, 8),
    _LogTransferSwitchSensorSignedMaxValue_Type()
)
logTransferSwitchSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTransferSwitchSensorSignedMaxValue.setStatus("current")
_LogTransferSwitchSensorSignedMinValue_Type = Integer32
_LogTransferSwitchSensorSignedMinValue_Object = MibTableColumn
logTransferSwitchSensorSignedMinValue = _LogTransferSwitchSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 7, 3, 1, 9),
    _LogTransferSwitchSensorSignedMinValue_Type()
)
logTransferSwitchSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTransferSwitchSensorSignedMinValue.setStatus("current")
_LogCircuit_ObjectIdentity = ObjectIdentity
logCircuit = _LogCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8)
)
_CircuitSensorLogTable_Object = MibTable
circuitSensorLogTable = _CircuitSensorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 3)
)
if mibBuilder.loadTexts:
    circuitSensorLogTable.setStatus("current")
_CircuitSensorLogEntry_Object = MibTableRow
circuitSensorLogEntry = _CircuitSensorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 3, 1)
)
circuitSensorLogEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "circuitId"),
    (0, "PDU2-MIB", "sensorType"),
    (0, "PDU2-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    circuitSensorLogEntry.setStatus("current")
_LogCircuitSensorDataAvailable_Type = TruthValue
_LogCircuitSensorDataAvailable_Object = MibTableColumn
logCircuitSensorDataAvailable = _LogCircuitSensorDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 3, 1, 2),
    _LogCircuitSensorDataAvailable_Type()
)
logCircuitSensorDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitSensorDataAvailable.setStatus("current")
_LogCircuitSensorState_Type = SensorStateEnumeration
_LogCircuitSensorState_Object = MibTableColumn
logCircuitSensorState = _LogCircuitSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 3, 1, 3),
    _LogCircuitSensorState_Type()
)
logCircuitSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitSensorState.setStatus("current")
_LogCircuitSensorAvgValue_Type = Unsigned32
_LogCircuitSensorAvgValue_Object = MibTableColumn
logCircuitSensorAvgValue = _LogCircuitSensorAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 3, 1, 4),
    _LogCircuitSensorAvgValue_Type()
)
logCircuitSensorAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitSensorAvgValue.setStatus("current")
_LogCircuitSensorMaxValue_Type = Unsigned32
_LogCircuitSensorMaxValue_Object = MibTableColumn
logCircuitSensorMaxValue = _LogCircuitSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 3, 1, 5),
    _LogCircuitSensorMaxValue_Type()
)
logCircuitSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitSensorMaxValue.setStatus("current")
_LogCircuitSensorMinValue_Type = Unsigned32
_LogCircuitSensorMinValue_Object = MibTableColumn
logCircuitSensorMinValue = _LogCircuitSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 3, 1, 6),
    _LogCircuitSensorMinValue_Type()
)
logCircuitSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitSensorMinValue.setStatus("current")
_LogCircuitSensorSignedAvgValue_Type = Integer32
_LogCircuitSensorSignedAvgValue_Object = MibTableColumn
logCircuitSensorSignedAvgValue = _LogCircuitSensorSignedAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 3, 1, 7),
    _LogCircuitSensorSignedAvgValue_Type()
)
logCircuitSensorSignedAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitSensorSignedAvgValue.setStatus("current")
_LogCircuitSensorSignedMaxValue_Type = Integer32
_LogCircuitSensorSignedMaxValue_Object = MibTableColumn
logCircuitSensorSignedMaxValue = _LogCircuitSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 3, 1, 8),
    _LogCircuitSensorSignedMaxValue_Type()
)
logCircuitSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitSensorSignedMaxValue.setStatus("current")
_LogCircuitSensorSignedMinValue_Type = Integer32
_LogCircuitSensorSignedMinValue_Object = MibTableColumn
logCircuitSensorSignedMinValue = _LogCircuitSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 3, 1, 9),
    _LogCircuitSensorSignedMinValue_Type()
)
logCircuitSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitSensorSignedMinValue.setStatus("current")
_CircuitPoleSensorLogTable_Object = MibTable
circuitPoleSensorLogTable = _CircuitPoleSensorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 5)
)
if mibBuilder.loadTexts:
    circuitPoleSensorLogTable.setStatus("current")
_CircuitPoleSensorLogEntry_Object = MibTableRow
circuitPoleSensorLogEntry = _CircuitPoleSensorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 5, 1)
)
circuitPoleSensorLogEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "circuitId"),
    (0, "PDU2-MIB", "circuitPoleId"),
    (0, "PDU2-MIB", "sensorType"),
    (0, "PDU2-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    circuitPoleSensorLogEntry.setStatus("current")
_LogCircuitPoleSensorDataAvailable_Type = TruthValue
_LogCircuitPoleSensorDataAvailable_Object = MibTableColumn
logCircuitPoleSensorDataAvailable = _LogCircuitPoleSensorDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 5, 1, 2),
    _LogCircuitPoleSensorDataAvailable_Type()
)
logCircuitPoleSensorDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitPoleSensorDataAvailable.setStatus("current")
_LogCircuitPoleSensorState_Type = SensorStateEnumeration
_LogCircuitPoleSensorState_Object = MibTableColumn
logCircuitPoleSensorState = _LogCircuitPoleSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 5, 1, 3),
    _LogCircuitPoleSensorState_Type()
)
logCircuitPoleSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitPoleSensorState.setStatus("current")
_LogCircuitPoleSensorAvgValue_Type = Unsigned32
_LogCircuitPoleSensorAvgValue_Object = MibTableColumn
logCircuitPoleSensorAvgValue = _LogCircuitPoleSensorAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 5, 1, 4),
    _LogCircuitPoleSensorAvgValue_Type()
)
logCircuitPoleSensorAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitPoleSensorAvgValue.setStatus("current")
_LogCircuitPoleSensorMaxValue_Type = Unsigned32
_LogCircuitPoleSensorMaxValue_Object = MibTableColumn
logCircuitPoleSensorMaxValue = _LogCircuitPoleSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 5, 1, 5),
    _LogCircuitPoleSensorMaxValue_Type()
)
logCircuitPoleSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitPoleSensorMaxValue.setStatus("current")
_LogCircuitPoleSensorMinValue_Type = Unsigned32
_LogCircuitPoleSensorMinValue_Object = MibTableColumn
logCircuitPoleSensorMinValue = _LogCircuitPoleSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 5, 1, 6),
    _LogCircuitPoleSensorMinValue_Type()
)
logCircuitPoleSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitPoleSensorMinValue.setStatus("current")
_LogCircuitPoleSensorSignedAvgValue_Type = Integer32
_LogCircuitPoleSensorSignedAvgValue_Object = MibTableColumn
logCircuitPoleSensorSignedAvgValue = _LogCircuitPoleSensorSignedAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 5, 1, 7),
    _LogCircuitPoleSensorSignedAvgValue_Type()
)
logCircuitPoleSensorSignedAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitPoleSensorSignedAvgValue.setStatus("current")
_LogCircuitPoleSensorSignedMaxValue_Type = Integer32
_LogCircuitPoleSensorSignedMaxValue_Object = MibTableColumn
logCircuitPoleSensorSignedMaxValue = _LogCircuitPoleSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 5, 1, 8),
    _LogCircuitPoleSensorSignedMaxValue_Type()
)
logCircuitPoleSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitPoleSensorSignedMaxValue.setStatus("current")
_LogCircuitPoleSensorSignedMinValue_Type = Integer32
_LogCircuitPoleSensorSignedMinValue_Object = MibTableColumn
logCircuitPoleSensorSignedMinValue = _LogCircuitPoleSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 8, 5, 1, 9),
    _LogCircuitPoleSensorSignedMinValue_Type()
)
logCircuitPoleSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCircuitPoleSensorSignedMinValue.setStatus("current")
_LogOutletGroup_ObjectIdentity = ObjectIdentity
logOutletGroup = _LogOutletGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 9)
)
_OutletGroupSensorLogTable_Object = MibTable
outletGroupSensorLogTable = _OutletGroupSensorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 9, 3)
)
if mibBuilder.loadTexts:
    outletGroupSensorLogTable.setStatus("current")
_OutletGroupSensorLogEntry_Object = MibTableRow
outletGroupSensorLogEntry = _OutletGroupSensorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 9, 3, 1)
)
outletGroupSensorLogEntry.setIndexNames(
    (0, "PDU2-MIB", "outletGroupId"),
    (0, "PDU2-MIB", "sensorType"),
    (0, "PDU2-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    outletGroupSensorLogEntry.setStatus("current")
_LogOutletGroupSensorDataAvailable_Type = TruthValue
_LogOutletGroupSensorDataAvailable_Object = MibTableColumn
logOutletGroupSensorDataAvailable = _LogOutletGroupSensorDataAvailable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 9, 3, 1, 2),
    _LogOutletGroupSensorDataAvailable_Type()
)
logOutletGroupSensorDataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletGroupSensorDataAvailable.setStatus("current")
_LogOutletGroupSensorState_Type = SensorStateEnumeration
_LogOutletGroupSensorState_Object = MibTableColumn
logOutletGroupSensorState = _LogOutletGroupSensorState_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 9, 3, 1, 3),
    _LogOutletGroupSensorState_Type()
)
logOutletGroupSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletGroupSensorState.setStatus("current")
_LogOutletGroupSensorAvgValue_Type = Unsigned32
_LogOutletGroupSensorAvgValue_Object = MibTableColumn
logOutletGroupSensorAvgValue = _LogOutletGroupSensorAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 9, 3, 1, 4),
    _LogOutletGroupSensorAvgValue_Type()
)
logOutletGroupSensorAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletGroupSensorAvgValue.setStatus("current")
_LogOutletGroupSensorMaxValue_Type = Unsigned32
_LogOutletGroupSensorMaxValue_Object = MibTableColumn
logOutletGroupSensorMaxValue = _LogOutletGroupSensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 9, 3, 1, 5),
    _LogOutletGroupSensorMaxValue_Type()
)
logOutletGroupSensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletGroupSensorMaxValue.setStatus("current")
_LogOutletGroupSensorMinValue_Type = Unsigned32
_LogOutletGroupSensorMinValue_Object = MibTableColumn
logOutletGroupSensorMinValue = _LogOutletGroupSensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 9, 3, 1, 6),
    _LogOutletGroupSensorMinValue_Type()
)
logOutletGroupSensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletGroupSensorMinValue.setStatus("current")
_LogOutletGroupSensorSignedAvgValue_Type = Integer32
_LogOutletGroupSensorSignedAvgValue_Object = MibTableColumn
logOutletGroupSensorSignedAvgValue = _LogOutletGroupSensorSignedAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 9, 3, 1, 7),
    _LogOutletGroupSensorSignedAvgValue_Type()
)
logOutletGroupSensorSignedAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletGroupSensorSignedAvgValue.setStatus("current")
_LogOutletGroupSensorSignedMaxValue_Type = Integer32
_LogOutletGroupSensorSignedMaxValue_Object = MibTableColumn
logOutletGroupSensorSignedMaxValue = _LogOutletGroupSensorSignedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 9, 3, 1, 8),
    _LogOutletGroupSensorSignedMaxValue_Type()
)
logOutletGroupSensorSignedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletGroupSensorSignedMaxValue.setStatus("current")
_LogOutletGroupSensorSignedMinValue_Type = Integer32
_LogOutletGroupSensorSignedMinValue_Object = MibTableColumn
logOutletGroupSensorSignedMinValue = _LogOutletGroupSensorSignedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 6, 9, 3, 1, 9),
    _LogOutletGroupSensorSignedMinValue_Type()
)
logOutletGroupSensorSignedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logOutletGroupSensorSignedMinValue.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 1)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 2)
)
_Reliability_ObjectIdentity = ObjectIdentity
reliability = _Reliability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10)
)
_ReliabilityData_ObjectIdentity = ObjectIdentity
reliabilityData = _ReliabilityData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 1)
)


class _ReliabilityDataTableSequenceNumber_Type(Integer32):
    """Custom type reliabilityDataTableSequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ReliabilityDataTableSequenceNumber_Type.__name__ = "Integer32"
_ReliabilityDataTableSequenceNumber_Object = MibScalar
reliabilityDataTableSequenceNumber = _ReliabilityDataTableSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 1, 1),
    _ReliabilityDataTableSequenceNumber_Type()
)
reliabilityDataTableSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityDataTableSequenceNumber.setStatus("current")
_ReliabilityDataTable_Object = MibTable
reliabilityDataTable = _ReliabilityDataTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 1, 2)
)
if mibBuilder.loadTexts:
    reliabilityDataTable.setStatus("current")
_ReliabilityDataEntry_Object = MibTableRow
reliabilityDataEntry = _ReliabilityDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 1, 2, 1)
)
reliabilityDataEntry.setIndexNames(
    (0, "PDU2-MIB", "reliabilityIndex"),
)
if mibBuilder.loadTexts:
    reliabilityDataEntry.setStatus("current")


class _ReliabilityIndex_Type(Integer32):
    """Custom type reliabilityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_ReliabilityIndex_Type.__name__ = "Integer32"
_ReliabilityIndex_Object = MibTableColumn
reliabilityIndex = _ReliabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 1, 2, 1, 1),
    _ReliabilityIndex_Type()
)
reliabilityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    reliabilityIndex.setStatus("current")
_ReliabilityId_Type = DisplayString
_ReliabilityId_Object = MibTableColumn
reliabilityId = _ReliabilityId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 1, 2, 1, 2),
    _ReliabilityId_Type()
)
reliabilityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityId.setStatus("current")
_ReliabilityDataValue_Type = Unsigned32
_ReliabilityDataValue_Object = MibTableColumn
reliabilityDataValue = _ReliabilityDataValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 1, 2, 1, 3),
    _ReliabilityDataValue_Type()
)
reliabilityDataValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityDataValue.setStatus("current")
_ReliabilityDataMaxPossible_Type = Unsigned32
_ReliabilityDataMaxPossible_Object = MibTableColumn
reliabilityDataMaxPossible = _ReliabilityDataMaxPossible_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 1, 2, 1, 4),
    _ReliabilityDataMaxPossible_Type()
)
reliabilityDataMaxPossible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityDataMaxPossible.setStatus("current")
_ReliabilityDataWorstValue_Type = Unsigned32
_ReliabilityDataWorstValue_Object = MibTableColumn
reliabilityDataWorstValue = _ReliabilityDataWorstValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 1, 2, 1, 5),
    _ReliabilityDataWorstValue_Type()
)
reliabilityDataWorstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityDataWorstValue.setStatus("current")
_ReliabilityDataThreshold_Type = Unsigned32
_ReliabilityDataThreshold_Object = MibTableColumn
reliabilityDataThreshold = _ReliabilityDataThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 1, 2, 1, 6),
    _ReliabilityDataThreshold_Type()
)
reliabilityDataThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityDataThreshold.setStatus("current")
_ReliabilityDataRawUpperBytes_Type = Unsigned32
_ReliabilityDataRawUpperBytes_Object = MibTableColumn
reliabilityDataRawUpperBytes = _ReliabilityDataRawUpperBytes_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 1, 2, 1, 7),
    _ReliabilityDataRawUpperBytes_Type()
)
reliabilityDataRawUpperBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityDataRawUpperBytes.setStatus("current")
_ReliabilityDataRawLowerBytes_Type = Unsigned32
_ReliabilityDataRawLowerBytes_Object = MibTableColumn
reliabilityDataRawLowerBytes = _ReliabilityDataRawLowerBytes_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 1, 2, 1, 8),
    _ReliabilityDataRawLowerBytes_Type()
)
reliabilityDataRawLowerBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityDataRawLowerBytes.setStatus("current")


class _ReliabilityDataFlags_Type(Bits):
    """Custom type reliabilityDataFlags based on Bits"""
    namedValues = NamedValues(
        *(("invalidFlag", 0),
          ("oldValue", 1),
          ("criticalEntry", 2))
    )

_ReliabilityDataFlags_Type.__name__ = "Bits"
_ReliabilityDataFlags_Object = MibTableColumn
reliabilityDataFlags = _ReliabilityDataFlags_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 1, 2, 1, 9),
    _ReliabilityDataFlags_Type()
)
reliabilityDataFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityDataFlags.setStatus("current")
_ReliabilityErrorLog_ObjectIdentity = ObjectIdentity
reliabilityErrorLog = _ReliabilityErrorLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 2)
)
_ReliabilityErrorLogTable_Object = MibTable
reliabilityErrorLogTable = _ReliabilityErrorLogTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 2, 2)
)
if mibBuilder.loadTexts:
    reliabilityErrorLogTable.setStatus("current")
_ReliabilityErrorLogEntry_Object = MibTableRow
reliabilityErrorLogEntry = _ReliabilityErrorLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 2, 2, 1)
)
reliabilityErrorLogEntry.setIndexNames(
    (0, "PDU2-MIB", "reliabilityErrorLogIndex"),
)
if mibBuilder.loadTexts:
    reliabilityErrorLogEntry.setStatus("current")


class _ReliabilityErrorLogIndex_Type(Integer32):
    """Custom type reliabilityErrorLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ReliabilityErrorLogIndex_Type.__name__ = "Integer32"
_ReliabilityErrorLogIndex_Object = MibTableColumn
reliabilityErrorLogIndex = _ReliabilityErrorLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 2, 2, 1, 1),
    _ReliabilityErrorLogIndex_Type()
)
reliabilityErrorLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    reliabilityErrorLogIndex.setStatus("current")
_ReliabilityErrorLogId_Type = DisplayString
_ReliabilityErrorLogId_Object = MibTableColumn
reliabilityErrorLogId = _ReliabilityErrorLogId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 2, 2, 1, 2),
    _ReliabilityErrorLogId_Type()
)
reliabilityErrorLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityErrorLogId.setStatus("current")
_ReliabilityErrorLogValue_Type = Unsigned32
_ReliabilityErrorLogValue_Object = MibTableColumn
reliabilityErrorLogValue = _ReliabilityErrorLogValue_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 2, 2, 1, 3),
    _ReliabilityErrorLogValue_Type()
)
reliabilityErrorLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityErrorLogValue.setStatus("current")
_ReliabilityErrorLogThreshold_Type = Unsigned32
_ReliabilityErrorLogThreshold_Object = MibTableColumn
reliabilityErrorLogThreshold = _ReliabilityErrorLogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 2, 2, 1, 6),
    _ReliabilityErrorLogThreshold_Type()
)
reliabilityErrorLogThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityErrorLogThreshold.setStatus("current")
_ReliabilityErrorLogRawUpperBytes_Type = Unsigned32
_ReliabilityErrorLogRawUpperBytes_Object = MibTableColumn
reliabilityErrorLogRawUpperBytes = _ReliabilityErrorLogRawUpperBytes_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 2, 2, 1, 7),
    _ReliabilityErrorLogRawUpperBytes_Type()
)
reliabilityErrorLogRawUpperBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityErrorLogRawUpperBytes.setStatus("current")
_ReliabilityErrorLogRawLowerBytes_Type = Unsigned32
_ReliabilityErrorLogRawLowerBytes_Object = MibTableColumn
reliabilityErrorLogRawLowerBytes = _ReliabilityErrorLogRawLowerBytes_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 2, 2, 1, 8),
    _ReliabilityErrorLogRawLowerBytes_Type()
)
reliabilityErrorLogRawLowerBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityErrorLogRawLowerBytes.setStatus("current")
_ReliabilityErrorLogPOH_Type = Unsigned32
_ReliabilityErrorLogPOH_Object = MibTableColumn
reliabilityErrorLogPOH = _ReliabilityErrorLogPOH_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 2, 2, 1, 9),
    _ReliabilityErrorLogPOH_Type()
)
reliabilityErrorLogPOH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityErrorLogPOH.setStatus("current")
_ReliabilityErrorLogTime_Type = Unsigned32
_ReliabilityErrorLogTime_Object = MibTableColumn
reliabilityErrorLogTime = _ReliabilityErrorLogTime_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 2, 2, 1, 10),
    _ReliabilityErrorLogTime_Type()
)
reliabilityErrorLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliabilityErrorLogTime.setStatus("current")
_ReliabilityHardwareHealth_ObjectIdentity = ObjectIdentity
reliabilityHardwareHealth = _ReliabilityHardwareHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 3)
)
_HwFailureTable_Object = MibTable
hwFailureTable = _HwFailureTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 3, 1)
)
if mibBuilder.loadTexts:
    hwFailureTable.setStatus("current")
_HwFailureEntry_Object = MibTableRow
hwFailureEntry = _HwFailureEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 3, 1, 1)
)
hwFailureEntry.setIndexNames(
    (0, "PDU2-MIB", "pduId"),
    (0, "PDU2-MIB", "hwFailureIndex"),
)
if mibBuilder.loadTexts:
    hwFailureEntry.setStatus("current")


class _HwFailureIndex_Type(Integer32):
    """Custom type hwFailureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwFailureIndex_Type.__name__ = "Integer32"
_HwFailureIndex_Object = MibTableColumn
hwFailureIndex = _HwFailureIndex_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 3, 1, 1, 1),
    _HwFailureIndex_Type()
)
hwFailureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwFailureIndex.setStatus("current")
_HwFailureComponentId_Type = DisplayString
_HwFailureComponentId_Object = MibTableColumn
hwFailureComponentId = _HwFailureComponentId_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 3, 1, 1, 2),
    _HwFailureComponentId_Type()
)
hwFailureComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFailureComponentId.setStatus("current")
_HwFailureType_Type = HwFailureTypeEnumeration
_HwFailureType_Object = MibTableColumn
hwFailureType = _HwFailureType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 3, 1, 1, 3),
    _HwFailureType_Type()
)
hwFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFailureType.setStatus("current")
_HwFailureAsserted_Type = TruthValue
_HwFailureAsserted_Object = MibTableColumn
hwFailureAsserted = _HwFailureAsserted_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 3, 1, 1, 4),
    _HwFailureAsserted_Type()
)
hwFailureAsserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFailureAsserted.setStatus("current")
_HwFailureLastAssertTimeStamp_Type = Unsigned32
_HwFailureLastAssertTimeStamp_Object = MibTableColumn
hwFailureLastAssertTimeStamp = _HwFailureLastAssertTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 3, 1, 1, 5),
    _HwFailureLastAssertTimeStamp_Type()
)
hwFailureLastAssertTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFailureLastAssertTimeStamp.setStatus("current")
_HwFailureLastDeassertTimeStamp_Type = Unsigned32
_HwFailureLastDeassertTimeStamp_Object = MibTableColumn
hwFailureLastDeassertTimeStamp = _HwFailureLastDeassertTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 3, 1, 1, 6),
    _HwFailureLastDeassertTimeStamp_Type()
)
hwFailureLastDeassertTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFailureLastDeassertTimeStamp.setStatus("current")
_HwFailureAssertCount_Type = Unsigned32
_HwFailureAssertCount_Object = MibTableColumn
hwFailureAssertCount = _HwFailureAssertCount_Object(
    (1, 3, 6, 1, 4, 1, 13742, 6, 10, 3, 1, 1, 7),
    _HwFailureAssertCount_Type()
)
hwFailureAssertCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFailureAssertCount.setStatus("current")

# Managed Objects groups

configGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 2, 1)
)
configGroup.setObjects(
      *(("PDU2-MIB", "pduCount"),
        ("PDU2-MIB", "pduManufacturer"),
        ("PDU2-MIB", "pduModel"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduRatedVoltage"),
        ("PDU2-MIB", "pduRatedCurrent"),
        ("PDU2-MIB", "pduRatedFrequency"),
        ("PDU2-MIB", "pduRatedVA"),
        ("PDU2-MIB", "pduImage"),
        ("PDU2-MIB", "inletCount"),
        ("PDU2-MIB", "transferSwitchCount"),
        ("PDU2-MIB", "productType"),
        ("PDU2-MIB", "overCurrentProtectorCount"),
        ("PDU2-MIB", "outletCount"),
        ("PDU2-MIB", "inletControllerCount"),
        ("PDU2-MIB", "outletControllerCount"),
        ("PDU2-MIB", "meteringControllerCount"),
        ("PDU2-MIB", "externalSensorCount"),
        ("PDU2-MIB", "circuitCount"),
        ("PDU2-MIB", "utcOffset"),
        ("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "boardVersion"),
        ("PDU2-MIB", "boardFirmwareVersion"),
        ("PDU2-MIB", "boardFirmwareTimeStamp"),
        ("PDU2-MIB", "unitSensorLogAvailable"),
        ("PDU2-MIB", "unitSensorUnits"),
        ("PDU2-MIB", "unitSensorDecimalDigits"),
        ("PDU2-MIB", "unitSensorResolution"),
        ("PDU2-MIB", "unitSensorMaximum"),
        ("PDU2-MIB", "unitSensorMinimum"),
        ("PDU2-MIB", "unitSensorHysteresis"),
        ("PDU2-MIB", "unitSensorStateChangeDelay"),
        ("PDU2-MIB", "unitSensorLowerCriticalThreshold"),
        ("PDU2-MIB", "unitSensorLowerWarningThreshold"),
        ("PDU2-MIB", "unitSensorUpperCriticalThreshold"),
        ("PDU2-MIB", "unitSensorUpperWarningThreshold"),
        ("PDU2-MIB", "unitSensorEnabledThresholds"),
        ("PDU2-MIB", "unitSensorSignedMaximum"),
        ("PDU2-MIB", "unitSensorSignedMinimum"),
        ("PDU2-MIB", "unitSensorSignedLowerCriticalThreshold"),
        ("PDU2-MIB", "unitSensorSignedLowerWarningThreshold"),
        ("PDU2-MIB", "unitSensorSignedUpperCriticalThreshold"),
        ("PDU2-MIB", "unitSensorSignedUpperWarningThreshold"),
        ("PDU2-MIB", "inletLabel"),
        ("PDU2-MIB", "inletName"),
        ("PDU2-MIB", "inletPoleCount"),
        ("PDU2-MIB", "inletRatedVoltage"),
        ("PDU2-MIB", "inletRatedCurrent"),
        ("PDU2-MIB", "inletDeviceCapabilities"),
        ("PDU2-MIB", "inletPoleCapabilities"),
        ("PDU2-MIB", "inletPlugDescriptor"),
        ("PDU2-MIB", "inletEnableState"),
        ("PDU2-MIB", "inletIsDC"),
        ("PDU2-MIB", "inletLinePairCount"),
        ("PDU2-MIB", "inletPoleLine"),
        ("PDU2-MIB", "inletPoleNode"),
        ("PDU2-MIB", "inletSensorLogAvailable"),
        ("PDU2-MIB", "inletSensorUnits"),
        ("PDU2-MIB", "inletSensorDecimalDigits"),
        ("PDU2-MIB", "inletSensorResolution"),
        ("PDU2-MIB", "inletSensorMaximum"),
        ("PDU2-MIB", "inletSensorMinimum"),
        ("PDU2-MIB", "inletSensorHysteresis"),
        ("PDU2-MIB", "inletSensorStateChangeDelay"),
        ("PDU2-MIB", "inletSensorLowerCriticalThreshold"),
        ("PDU2-MIB", "inletSensorLowerWarningThreshold"),
        ("PDU2-MIB", "inletSensorUpperCriticalThreshold"),
        ("PDU2-MIB", "inletSensorUpperWarningThreshold"),
        ("PDU2-MIB", "inletSensorEnabledThresholds"),
        ("PDU2-MIB", "inletSensorSignedMaximum"),
        ("PDU2-MIB", "inletSensorSignedMinimum"),
        ("PDU2-MIB", "inletSensorSignedLowerCriticalThreshold"),
        ("PDU2-MIB", "inletSensorSignedLowerWarningThreshold"),
        ("PDU2-MIB", "inletSensorSignedUpperCriticalThreshold"),
        ("PDU2-MIB", "inletSensorSignedUpperWarningThreshold"),
        ("PDU2-MIB", "inletPoleSensorLogAvailable"),
        ("PDU2-MIB", "inletPoleSensorUnits"),
        ("PDU2-MIB", "inletPoleSensorDecimalDigits"),
        ("PDU2-MIB", "inletPoleSensorResolution"),
        ("PDU2-MIB", "inletPoleSensorMaximum"),
        ("PDU2-MIB", "inletPoleSensorMinimum"),
        ("PDU2-MIB", "inletPoleSensorHysteresis"),
        ("PDU2-MIB", "inletPoleSensorStateChangeDelay"),
        ("PDU2-MIB", "inletPoleSensorLowerCriticalThreshold"),
        ("PDU2-MIB", "inletPoleSensorLowerWarningThreshold"),
        ("PDU2-MIB", "inletPoleSensorUpperCriticalThreshold"),
        ("PDU2-MIB", "inletPoleSensorUpperWarningThreshold"),
        ("PDU2-MIB", "inletPoleSensorEnabledThresholds"),
        ("PDU2-MIB", "inletPoleSensorSignedMaximum"),
        ("PDU2-MIB", "inletPoleSensorSignedMinimum"),
        ("PDU2-MIB", "inletPoleSensorSignedLowerCriticalThreshold"),
        ("PDU2-MIB", "inletPoleSensorSignedLowerWarningThreshold"),
        ("PDU2-MIB", "inletPoleSensorSignedUpperCriticalThreshold"),
        ("PDU2-MIB", "inletPoleSensorSignedUpperWarningThreshold"),
        ("PDU2-MIB", "inletLinePairCapabilities"),
        ("PDU2-MIB", "inletLinePairLeftLine"),
        ("PDU2-MIB", "inletLinePairRightLine"),
        ("PDU2-MIB", "inletLinePairLeftNode"),
        ("PDU2-MIB", "inletLinePairRightNode"),
        ("PDU2-MIB", "inletLinePairSensorLogAvailable"),
        ("PDU2-MIB", "inletLinePairSensorUnits"),
        ("PDU2-MIB", "inletLinePairSensorDecimalDigits"),
        ("PDU2-MIB", "inletLinePairSensorResolution"),
        ("PDU2-MIB", "inletLinePairSensorMaximum"),
        ("PDU2-MIB", "inletLinePairSensorMinimum"),
        ("PDU2-MIB", "inletLinePairSensorHysteresis"),
        ("PDU2-MIB", "inletLinePairSensorStateChangeDelay"),
        ("PDU2-MIB", "inletLinePairSensorLowerCriticalThreshold"),
        ("PDU2-MIB", "inletLinePairSensorLowerWarningThreshold"),
        ("PDU2-MIB", "inletLinePairSensorUpperCriticalThreshold"),
        ("PDU2-MIB", "inletLinePairSensorUpperWarningThreshold"),
        ("PDU2-MIB", "inletLinePairSensorEnabledThresholds"),
        ("PDU2-MIB", "inletLinePairSensorSignedMaximum"),
        ("PDU2-MIB", "inletLinePairSensorSignedMinimum"),
        ("PDU2-MIB", "inletLinePairSensorSignedLowerCriticalThreshold"),
        ("PDU2-MIB", "inletLinePairSensorSignedLowerWarningThreshold"),
        ("PDU2-MIB", "inletLinePairSensorSignedUpperCriticalThreshold"),
        ("PDU2-MIB", "inletLinePairSensorSignedUpperWarningThreshold"),
        ("PDU2-MIB", "overCurrentProtectorLabel"),
        ("PDU2-MIB", "overCurrentProtectorName"),
        ("PDU2-MIB", "overCurrentProtectorType"),
        ("PDU2-MIB", "overCurrentProtectorRatedCurrent"),
        ("PDU2-MIB", "overCurrentProtectorCapabilities"),
        ("PDU2-MIB", "overCurrentProtectorPoleCount"),
        ("PDU2-MIB", "overCurrentProtectorPoleLine"),
        ("PDU2-MIB", "overCurrentProtectorPoleInNode"),
        ("PDU2-MIB", "overCurrentProtectorPoleOutNode"),
        ("PDU2-MIB", "overCurrentProtectorSensorLogAvailable"),
        ("PDU2-MIB", "overCurrentProtectorSensorUnits"),
        ("PDU2-MIB", "overCurrentProtectorSensorDecimalDigits"),
        ("PDU2-MIB", "overCurrentProtectorSensorResolution"),
        ("PDU2-MIB", "overCurrentProtectorSensorMaximum"),
        ("PDU2-MIB", "overCurrentProtectorSensorMinimum"),
        ("PDU2-MIB", "overCurrentProtectorSensorHysteresis"),
        ("PDU2-MIB", "overCurrentProtectorSensorStateChangeDelay"),
        ("PDU2-MIB", "overCurrentProtectorSensorLowerCriticalThreshold"),
        ("PDU2-MIB", "overCurrentProtectorSensorLowerWarningThreshold"),
        ("PDU2-MIB", "overCurrentProtectorSensorUpperCriticalThreshold"),
        ("PDU2-MIB", "overCurrentProtectorSensorUpperWarningThreshold"),
        ("PDU2-MIB", "overCurrentProtectorSensorEnabledThresholds"),
        ("PDU2-MIB", "overCurrentProtectorSensorSignedMaximum"),
        ("PDU2-MIB", "overCurrentProtectorSensorSignedMinimum"),
        ("PDU2-MIB", "overCurrentProtectorSensorSignedLowerCriticalThreshold"),
        ("PDU2-MIB", "overCurrentProtectorSensorSignedLowerWarningThreshold"),
        ("PDU2-MIB", "overCurrentProtectorSensorSignedUpperCriticalThreshold"),
        ("PDU2-MIB", "overCurrentProtectorSensorSignedUpperWarningThreshold"),
        ("PDU2-MIB", "overCurrentProtectorPowerSource"),
        ("PDU2-MIB", "outletLabel"),
        ("PDU2-MIB", "outletName"),
        ("PDU2-MIB", "outletPoleCount"),
        ("PDU2-MIB", "outletRatedVoltage"),
        ("PDU2-MIB", "outletRatedCurrent"),
        ("PDU2-MIB", "outletRatedVA"),
        ("PDU2-MIB", "outletDeviceCapabilities"),
        ("PDU2-MIB", "outletPoleCapabilities"),
        ("PDU2-MIB", "outletPowerCyclingPowerOffPeriod"),
        ("PDU2-MIB", "outletStateOnStartup"),
        ("PDU2-MIB", "outletUseGlobalPowerCyclingPowerOffPeriod"),
        ("PDU2-MIB", "outletSwitchable"),
        ("PDU2-MIB", "outletReceptacleDescriptor"),
        ("PDU2-MIB", "outletNonCritical"),
        ("PDU2-MIB", "outletSequenceDelay"),
        ("PDU2-MIB", "outletPoleLine"),
        ("PDU2-MIB", "outletPoleNode"),
        ("PDU2-MIB", "outletSensorLogAvailable"),
        ("PDU2-MIB", "outletSensorUnits"),
        ("PDU2-MIB", "outletSensorDecimalDigits"),
        ("PDU2-MIB", "outletSensorResolution"),
        ("PDU2-MIB", "outletSensorMaximum"),
        ("PDU2-MIB", "outletSensorMinimum"),
        ("PDU2-MIB", "outletSensorHysteresis"),
        ("PDU2-MIB", "outletSensorStateChangeDelay"),
        ("PDU2-MIB", "outletSensorLowerCriticalThreshold"),
        ("PDU2-MIB", "outletSensorLowerWarningThreshold"),
        ("PDU2-MIB", "outletSensorUpperCriticalThreshold"),
        ("PDU2-MIB", "outletSensorUpperWarningThreshold"),
        ("PDU2-MIB", "outletSensorEnabledThresholds"),
        ("PDU2-MIB", "outletSensorSignedMaximum"),
        ("PDU2-MIB", "outletSensorSignedMinimum"),
        ("PDU2-MIB", "outletSensorSignedLowerCriticalThreshold"),
        ("PDU2-MIB", "outletSensorSignedLowerWarningThreshold"),
        ("PDU2-MIB", "outletSensorSignedUpperCriticalThreshold"),
        ("PDU2-MIB", "outletSensorSignedUpperWarningThreshold"),
        ("PDU2-MIB", "outletPoleSensorLogAvailable"),
        ("PDU2-MIB", "outletPoleSensorUnits"),
        ("PDU2-MIB", "outletPoleSensorDecimalDigits"),
        ("PDU2-MIB", "outletPoleSensorResolution"),
        ("PDU2-MIB", "outletPoleSensorMaximum"),
        ("PDU2-MIB", "outletPoleSensorMinimum"),
        ("PDU2-MIB", "outletPoleSensorHysteresis"),
        ("PDU2-MIB", "outletPoleSensorStateChangeDelay"),
        ("PDU2-MIB", "outletPoleSensorLowerCriticalThreshold"),
        ("PDU2-MIB", "outletPoleSensorLowerWarningThreshold"),
        ("PDU2-MIB", "outletPoleSensorUpperCriticalThreshold"),
        ("PDU2-MIB", "outletPoleSensorUpperWarningThreshold"),
        ("PDU2-MIB", "outletPoleSensorEnabledThresholds"),
        ("PDU2-MIB", "outletPoleSensorSignedMaximum"),
        ("PDU2-MIB", "outletPoleSensorSignedMinimum"),
        ("PDU2-MIB", "outletPoleSensorSignedLowerCriticalThreshold"),
        ("PDU2-MIB", "outletPoleSensorSignedLowerWarningThreshold"),
        ("PDU2-MIB", "outletPoleSensorSignedUpperCriticalThreshold"),
        ("PDU2-MIB", "outletPoleSensorSignedUpperWarningThreshold"),
        ("PDU2-MIB", "outletPowerSource"),
        ("PDU2-MIB", "outletServiceMode"),
        ("PDU2-MIB", "externalSensorType"),
        ("PDU2-MIB", "externalSensorSerialNumber"),
        ("PDU2-MIB", "externalSensorName"),
        ("PDU2-MIB", "externalSensorDescription"),
        ("PDU2-MIB", "externalSensorXCoordinate"),
        ("PDU2-MIB", "externalSensorYCoordinate"),
        ("PDU2-MIB", "externalSensorZCoordinate"),
        ("PDU2-MIB", "externalSensorChannelNumber"),
        ("PDU2-MIB", "externalOnOffSensorSubtype"),
        ("PDU2-MIB", "externalSensorLogAvailable"),
        ("PDU2-MIB", "externalSensorUnits"),
        ("PDU2-MIB", "externalSensorDecimalDigits"),
        ("PDU2-MIB", "externalSensorResolution"),
        ("PDU2-MIB", "externalSensorMaximum"),
        ("PDU2-MIB", "externalSensorMinimum"),
        ("PDU2-MIB", "externalSensorHysteresis"),
        ("PDU2-MIB", "externalSensorStateChangeDelay"),
        ("PDU2-MIB", "externalSensorLowerCriticalThreshold"),
        ("PDU2-MIB", "externalSensorLowerWarningThreshold"),
        ("PDU2-MIB", "externalSensorUpperCriticalThreshold"),
        ("PDU2-MIB", "externalSensorUpperWarningThreshold"),
        ("PDU2-MIB", "externalSensorEnabledThresholds"),
        ("PDU2-MIB", "externalSensorsZCoordinateUnits"),
        ("PDU2-MIB", "externalSensorIsActuator"),
        ("PDU2-MIB", "externalSensorPosition"),
        ("PDU2-MIB", "externalSensorUseDefaultThresholds"),
        ("PDU2-MIB", "externalSensorTypeDefaultHysteresis"),
        ("PDU2-MIB", "externalSensorTypeDefaultStateChangeDelay"),
        ("PDU2-MIB", "externalSensorTypeDefaultLowerCriticalThreshold"),
        ("PDU2-MIB", "externalSensorTypeDefaultLowerWarningThreshold"),
        ("PDU2-MIB", "externalSensorTypeDefaultUpperCriticalThreshold"),
        ("PDU2-MIB", "externalSensorTypeDefaultUpperWarningThreshold"),
        ("PDU2-MIB", "externalSensorTypeDefaultEnabledThresholds"),
        ("PDU2-MIB", "externalSensorTypeDefaultUnit"),
        ("PDU2-MIB", "externalSensorTypeDefaultDecimalDigits"),
        ("PDU2-MIB", "externalSensorTypeDefaultMaximum"),
        ("PDU2-MIB", "externalSensorTypeDefaultMinimum"),
        ("PDU2-MIB", "measurementPeriod"),
        ("PDU2-MIB", "measurementsPerLogEntry"),
        ("PDU2-MIB", "logSize"),
        ("PDU2-MIB", "unitDeviceCapabilities"),
        ("PDU2-MIB", "globalOutletPowerCyclingPowerOffPeriod"),
        ("PDU2-MIB", "globalOutletStateOnStartup"),
        ("PDU2-MIB", "relayBehaviorOnPowerLoss"),
        ("PDU2-MIB", "pduPowerCyclingPowerOffPeriod"),
        ("PDU2-MIB", "pduDaisychainMemberType"),
        ("PDU2-MIB", "managedExternalSensorCount"),
        ("PDU2-MIB", "outletPowerupSequence"),
        ("PDU2-MIB", "loadShedding"),
        ("PDU2-MIB", "serverCount"),
        ("PDU2-MIB", "serverIPAddress"),
        ("PDU2-MIB", "serverPingEnabled"),
        ("PDU2-MIB", "inrushGuardDelay"),
        ("PDU2-MIB", "cascadedDeviceConnected"),
        ("PDU2-MIB", "synchronizeWithNTPServer"),
        ("PDU2-MIB", "firstNTPServerAddressType"),
        ("PDU2-MIB", "firstNTPServerAddress"),
        ("PDU2-MIB", "secondNTPServerAddressType"),
        ("PDU2-MIB", "secondNTPServerAddress"),
        ("PDU2-MIB", "transferSwitchLabel"),
        ("PDU2-MIB", "transferSwitchName"),
        ("PDU2-MIB", "transferSwitchPreferredInlet"),
        ("PDU2-MIB", "transferSwitchPoleCount"),
        ("PDU2-MIB", "transferSwitchAutoReTransferEnabled"),
        ("PDU2-MIB", "transferSwitchAutoReTransferWaitTime"),
        ("PDU2-MIB", "transferSwitchAutoReTransferRequiresPhaseSync"),
        ("PDU2-MIB", "transferSwitchFrontPanelManualTransferButtonEnabled"),
        ("PDU2-MIB", "transferSwitchCapabilities"),
        ("PDU2-MIB", "transferSwitchPoleLine"),
        ("PDU2-MIB", "transferSwitchPoleIn1Node"),
        ("PDU2-MIB", "transferSwitchPoleIn2Node"),
        ("PDU2-MIB", "transferSwitchPoleOutNode"),
        ("PDU2-MIB", "transferSwitchSensorLogAvailable"),
        ("PDU2-MIB", "transferSwitchSensorUnits"),
        ("PDU2-MIB", "transferSwitchSensorDecimalDigits"),
        ("PDU2-MIB", "transferSwitchSensorResolution"),
        ("PDU2-MIB", "transferSwitchSensorMaximum"),
        ("PDU2-MIB", "transferSwitchSensorMinimum"),
        ("PDU2-MIB", "transferSwitchSensorHysteresis"),
        ("PDU2-MIB", "transferSwitchSensorStateChangeDelay"),
        ("PDU2-MIB", "transferSwitchSensorLowerCriticalThreshold"),
        ("PDU2-MIB", "transferSwitchSensorLowerWarningThreshold"),
        ("PDU2-MIB", "transferSwitchSensorUpperCriticalThreshold"),
        ("PDU2-MIB", "transferSwitchSensorUpperWarningThreshold"),
        ("PDU2-MIB", "transferSwitchSensorEnabledThresholds"),
        ("PDU2-MIB", "transferSwitchSensorSignedMaximum"),
        ("PDU2-MIB", "transferSwitchSensorSignedMinimum"),
        ("PDU2-MIB", "transferSwitchSensorSignedLowerCriticalThreshold"),
        ("PDU2-MIB", "transferSwitchSensorSignedLowerWarningThreshold"),
        ("PDU2-MIB", "transferSwitchSensorSignedUpperCriticalThreshold"),
        ("PDU2-MIB", "transferSwitchSensorSignedUpperWarningThreshold"),
        ("PDU2-MIB", "transferSwitchPowerSource1"),
        ("PDU2-MIB", "transferSwitchPowerSource2"),
        ("PDU2-MIB", "peripheralDevicePackageSerialNumber"),
        ("PDU2-MIB", "peripheralDevicePackageModel"),
        ("PDU2-MIB", "peripheralDevicePackageFirmwareVersion"),
        ("PDU2-MIB", "peripheralDevicePackageMinFirmwareVersion"),
        ("PDU2-MIB", "peripheralDevicePackageFirmwareTimeStamp"),
        ("PDU2-MIB", "peripheralDevicePackagePosition"),
        ("PDU2-MIB", "peripheralDevicePackageState"),
        ("PDU2-MIB", "deviceCascadeType"),
        ("PDU2-MIB", "deviceCascadePosition"),
        ("PDU2-MIB", "peripheralDevicesAutoManagement"),
        ("PDU2-MIB", "externalSensorAlarmedToNormalDelay"),
        ("PDU2-MIB", "frontPanelOutletSwitching"),
        ("PDU2-MIB", "frontPanelRCMSelfTest"),
        ("PDU2-MIB", "frontPanelActuatorControl"),
        ("PDU2-MIB", "powerMeterPanelPositions"),
        ("PDU2-MIB", "powerMeterPanelLayout"),
        ("PDU2-MIB", "powerMeterPanelNumbering"),
        ("PDU2-MIB", "powerMeterPhaseCTRating"),
        ("PDU2-MIB", "powerMeterNeutralCTRating"),
        ("PDU2-MIB", "powerMeterEarthCTRating"),
        ("PDU2-MIB", "powerMeterBranchCount"),
        ("PDU2-MIB", "powerMeterType"),
        ("PDU2-MIB", "circuitPoleCount"),
        ("PDU2-MIB", "circuitName"),
        ("PDU2-MIB", "circuitType"),
        ("PDU2-MIB", "circuitRatedCurrent"),
        ("PDU2-MIB", "circuitCTRating"),
        ("PDU2-MIB", "circuitCapabilities"),
        ("PDU2-MIB", "circuitPoleCapabilities"),
        ("PDU2-MIB", "circuitPowerSource"),
        ("PDU2-MIB", "circuitPolePanelPosition"),
        ("PDU2-MIB", "circuitPoleCTNumber"),
        ("PDU2-MIB", "circuitPolePhase"),
        ("PDU2-MIB", "circuitSensorLogAvailable"),
        ("PDU2-MIB", "circuitSensorUnits"),
        ("PDU2-MIB", "circuitSensorDecimalDigits"),
        ("PDU2-MIB", "circuitSensorResolution"),
        ("PDU2-MIB", "circuitSensorMaximum"),
        ("PDU2-MIB", "circuitSensorMinimum"),
        ("PDU2-MIB", "circuitSensorHysteresis"),
        ("PDU2-MIB", "circuitSensorStateChangeDelay"),
        ("PDU2-MIB", "circuitSensorLowerCriticalThreshold"),
        ("PDU2-MIB", "circuitSensorLowerWarningThreshold"),
        ("PDU2-MIB", "circuitSensorUpperCriticalThreshold"),
        ("PDU2-MIB", "circuitSensorUpperWarningThreshold"),
        ("PDU2-MIB", "circuitSensorEnabledThresholds"),
        ("PDU2-MIB", "circuitSensorSignedMaximum"),
        ("PDU2-MIB", "circuitSensorSignedMinimum"),
        ("PDU2-MIB", "circuitSensorSignedLowerCriticalThreshold"),
        ("PDU2-MIB", "circuitSensorSignedLowerWarningThreshold"),
        ("PDU2-MIB", "circuitSensorSignedUpperCriticalThreshold"),
        ("PDU2-MIB", "circuitSensorSignedUpperWarningThreshold"),
        ("PDU2-MIB", "circuitPoleSensorLogAvailable"),
        ("PDU2-MIB", "circuitPoleSensorUnits"),
        ("PDU2-MIB", "circuitPoleSensorDecimalDigits"),
        ("PDU2-MIB", "circuitPoleSensorResolution"),
        ("PDU2-MIB", "circuitPoleSensorMaximum"),
        ("PDU2-MIB", "circuitPoleSensorMinimum"),
        ("PDU2-MIB", "circuitPoleSensorHysteresis"),
        ("PDU2-MIB", "circuitPoleSensorStateChangeDelay"),
        ("PDU2-MIB", "circuitPoleSensorLowerCriticalThreshold"),
        ("PDU2-MIB", "circuitPoleSensorLowerWarningThreshold"),
        ("PDU2-MIB", "circuitPoleSensorUpperCriticalThreshold"),
        ("PDU2-MIB", "circuitPoleSensorUpperWarningThreshold"),
        ("PDU2-MIB", "circuitPoleSensorEnabledThresholds"),
        ("PDU2-MIB", "circuitPoleSensorSignedMaximum"),
        ("PDU2-MIB", "circuitPoleSensorSignedMinimum"),
        ("PDU2-MIB", "circuitPoleSensorSignedLowerCriticalThreshold"),
        ("PDU2-MIB", "circuitPoleSensorSignedLowerWarningThreshold"),
        ("PDU2-MIB", "circuitPoleSensorSignedUpperCriticalThreshold"),
        ("PDU2-MIB", "circuitPoleSensorSignedUpperWarningThreshold"),
        ("PDU2-MIB", "activeDNSServerAddressType"),
        ("PDU2-MIB", "activeDNSServerAddress"),
        ("PDU2-MIB", "activeDNSServerCount"),
        ("PDU2-MIB", "activeNTPServerAddressType"),
        ("PDU2-MIB", "activeNTPServerAddress"),
        ("PDU2-MIB", "activeNTPServerCount"),
        ("PDU2-MIB", "peripheralDevicePackageCount"),
        ("PDU2-MIB", "outletGroupCount"),
        ("PDU2-MIB", "outletGroupName"),
        ("PDU2-MIB", "outletGroupCapabilities"),
        ("PDU2-MIB", "outletGroupMembers"),
        ("PDU2-MIB", "outletGroupSensorLogAvailable"),
        ("PDU2-MIB", "outletGroupSensorUnits"),
        ("PDU2-MIB", "outletGroupSensorDecimalDigits"),
        ("PDU2-MIB", "outletGroupSensorResolution"),
        ("PDU2-MIB", "outletGroupSensorMaximum"),
        ("PDU2-MIB", "outletGroupSensorMinimum"),
        ("PDU2-MIB", "outletGroupSensorHysteresis"),
        ("PDU2-MIB", "outletGroupSensorStateChangeDelay"),
        ("PDU2-MIB", "outletGroupSensorLowerCriticalThreshold"),
        ("PDU2-MIB", "outletGroupSensorLowerWarningThreshold"),
        ("PDU2-MIB", "outletGroupSensorUpperCriticalThreshold"),
        ("PDU2-MIB", "outletGroupSensorUpperWarningThreshold"),
        ("PDU2-MIB", "outletGroupSensorEnabledThresholds"),
        ("PDU2-MIB", "outletGroupSensorSignedMaximum"),
        ("PDU2-MIB", "outletGroupSensorSignedMinimum"),
        ("PDU2-MIB", "outletGroupSensorSignedLowerCriticalThreshold"),
        ("PDU2-MIB", "outletGroupSensorSignedLowerWarningThreshold"),
        ("PDU2-MIB", "outletGroupSensorSignedUpperCriticalThreshold"),
        ("PDU2-MIB", "outletGroupSensorSignedUpperWarningThreshold"),
        ("PDU2-MIB", "demandUpdateInterval"),
        ("PDU2-MIB", "demandAveragingIntervals"),
        ("PDU2-MIB", "hasDCInlets"),
        ("PDU2-MIB", "pduOrientation"),
        ("PDU2-MIB", "pduUptime"),
        ("PDU2-MIB", "tripCauseOutletHandling"))
)
if mibBuilder.loadTexts:
    configGroup.setStatus("current")

logGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 2, 2)
)
logGroup.setObjects(
      *(("PDU2-MIB", "dataLogging"),
        ("PDU2-MIB", "oldestLogID"),
        ("PDU2-MIB", "newestLogID"),
        ("PDU2-MIB", "logTimeStamp"),
        ("PDU2-MIB", "dataLoggingEnableForAllSensors"),
        ("PDU2-MIB", "logUnitSensorDataAvailable"),
        ("PDU2-MIB", "logUnitSensorState"),
        ("PDU2-MIB", "logUnitSensorAvgValue"),
        ("PDU2-MIB", "logUnitSensorMaxValue"),
        ("PDU2-MIB", "logUnitSensorMinValue"),
        ("PDU2-MIB", "logUnitSensorSignedAvgValue"),
        ("PDU2-MIB", "logUnitSensorSignedMaxValue"),
        ("PDU2-MIB", "logUnitSensorSignedMinValue"),
        ("PDU2-MIB", "logInletSensorDataAvailable"),
        ("PDU2-MIB", "logInletSensorState"),
        ("PDU2-MIB", "logInletSensorAvgValue"),
        ("PDU2-MIB", "logInletSensorMaxValue"),
        ("PDU2-MIB", "logInletSensorMinValue"),
        ("PDU2-MIB", "logInletSensorSignedAvgValue"),
        ("PDU2-MIB", "logInletSensorSignedMaxValue"),
        ("PDU2-MIB", "logInletSensorSignedMinValue"),
        ("PDU2-MIB", "logInletPoleSensorDataAvailable"),
        ("PDU2-MIB", "logInletPoleSensorState"),
        ("PDU2-MIB", "logInletPoleSensorAvgValue"),
        ("PDU2-MIB", "logInletPoleSensorMaxValue"),
        ("PDU2-MIB", "logInletPoleSensorMinValue"),
        ("PDU2-MIB", "logInletPoleSensorSignedAvgValue"),
        ("PDU2-MIB", "logInletPoleSensorSignedMaxValue"),
        ("PDU2-MIB", "logInletPoleSensorSignedMinValue"),
        ("PDU2-MIB", "logInletLinePairSensorDataAvailable"),
        ("PDU2-MIB", "logInletLinePairSensorState"),
        ("PDU2-MIB", "logInletLinePairSensorAvgValue"),
        ("PDU2-MIB", "logInletLinePairSensorMaxValue"),
        ("PDU2-MIB", "logInletLinePairSensorMinValue"),
        ("PDU2-MIB", "logInletLinePairSensorSignedAvgValue"),
        ("PDU2-MIB", "logInletLinePairSensorSignedMaxValue"),
        ("PDU2-MIB", "logInletLinePairSensorSignedMinValue"),
        ("PDU2-MIB", "logOutletSensorDataAvailable"),
        ("PDU2-MIB", "logOutletSensorState"),
        ("PDU2-MIB", "logOutletSensorAvgValue"),
        ("PDU2-MIB", "logOutletSensorMaxValue"),
        ("PDU2-MIB", "logOutletSensorMinValue"),
        ("PDU2-MIB", "logOutletSensorSignedAvgValue"),
        ("PDU2-MIB", "logOutletSensorSignedMaxValue"),
        ("PDU2-MIB", "logOutletSensorSignedMinValue"),
        ("PDU2-MIB", "logOutletPoleSensorDataAvailable"),
        ("PDU2-MIB", "logOutletPoleSensorState"),
        ("PDU2-MIB", "logOutletPoleSensorAvgValue"),
        ("PDU2-MIB", "logOutletPoleSensorMaxValue"),
        ("PDU2-MIB", "logOutletPoleSensorMinValue"),
        ("PDU2-MIB", "logOutletPoleSensorSignedAvgValue"),
        ("PDU2-MIB", "logOutletPoleSensorSignedMaxValue"),
        ("PDU2-MIB", "logOutletPoleSensorSignedMinValue"),
        ("PDU2-MIB", "logOverCurrentProtectorSensorDataAvailable"),
        ("PDU2-MIB", "logOverCurrentProtectorSensorState"),
        ("PDU2-MIB", "logOverCurrentProtectorSensorAvgValue"),
        ("PDU2-MIB", "logOverCurrentProtectorSensorMaxValue"),
        ("PDU2-MIB", "logOverCurrentProtectorSensorMinValue"),
        ("PDU2-MIB", "logOverCurrentProtectorSensorSignedAvgValue"),
        ("PDU2-MIB", "logOverCurrentProtectorSensorSignedMaxValue"),
        ("PDU2-MIB", "logOverCurrentProtectorSensorSignedMinValue"),
        ("PDU2-MIB", "logExternalSensorDataAvailable"),
        ("PDU2-MIB", "logExternalSensorState"),
        ("PDU2-MIB", "logExternalSensorAvgValue"),
        ("PDU2-MIB", "logExternalSensorMaxValue"),
        ("PDU2-MIB", "logExternalSensorMinValue"),
        ("PDU2-MIB", "logTransferSwitchSensorDataAvailable"),
        ("PDU2-MIB", "logTransferSwitchSensorState"),
        ("PDU2-MIB", "logTransferSwitchSensorAvgValue"),
        ("PDU2-MIB", "logTransferSwitchSensorMaxValue"),
        ("PDU2-MIB", "logTransferSwitchSensorMinValue"),
        ("PDU2-MIB", "logTransferSwitchSensorSignedAvgValue"),
        ("PDU2-MIB", "logTransferSwitchSensorSignedMaxValue"),
        ("PDU2-MIB", "logTransferSwitchSensorSignedMinValue"),
        ("PDU2-MIB", "logCircuitSensorDataAvailable"),
        ("PDU2-MIB", "logCircuitSensorState"),
        ("PDU2-MIB", "logCircuitSensorAvgValue"),
        ("PDU2-MIB", "logCircuitSensorMaxValue"),
        ("PDU2-MIB", "logCircuitSensorMinValue"),
        ("PDU2-MIB", "logCircuitSensorSignedAvgValue"),
        ("PDU2-MIB", "logCircuitSensorSignedMaxValue"),
        ("PDU2-MIB", "logCircuitSensorSignedMinValue"),
        ("PDU2-MIB", "logCircuitPoleSensorDataAvailable"),
        ("PDU2-MIB", "logCircuitPoleSensorState"),
        ("PDU2-MIB", "logCircuitPoleSensorAvgValue"),
        ("PDU2-MIB", "logCircuitPoleSensorMaxValue"),
        ("PDU2-MIB", "logCircuitPoleSensorMinValue"),
        ("PDU2-MIB", "logCircuitPoleSensorSignedAvgValue"),
        ("PDU2-MIB", "logCircuitPoleSensorSignedMaxValue"),
        ("PDU2-MIB", "logCircuitPoleSensorSignedMinValue"),
        ("PDU2-MIB", "logOutletGroupSensorDataAvailable"),
        ("PDU2-MIB", "logOutletGroupSensorState"),
        ("PDU2-MIB", "logOutletGroupSensorAvgValue"),
        ("PDU2-MIB", "logOutletGroupSensorMaxValue"),
        ("PDU2-MIB", "logOutletGroupSensorMinValue"),
        ("PDU2-MIB", "logOutletGroupSensorSignedAvgValue"),
        ("PDU2-MIB", "logOutletGroupSensorSignedMaxValue"),
        ("PDU2-MIB", "logOutletGroupSensorSignedMinValue"))
)
if mibBuilder.loadTexts:
    logGroup.setStatus("current")

measurementsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 2, 3)
)
measurementsGroup.setObjects(
      *(("PDU2-MIB", "measurementsUnitSensorIsAvailable"),
        ("PDU2-MIB", "measurementsUnitSensorState"),
        ("PDU2-MIB", "measurementsUnitSensorValue"),
        ("PDU2-MIB", "measurementsUnitSensorTimeStamp"),
        ("PDU2-MIB", "measurementsUnitSensorSignedValue"),
        ("PDU2-MIB", "measurementsUnitSensorMinMaxValid"),
        ("PDU2-MIB", "measurementsUnitSensorMinValue"),
        ("PDU2-MIB", "measurementsUnitSensorSignedMinValue"),
        ("PDU2-MIB", "measurementsUnitSensorMinTimeStamp"),
        ("PDU2-MIB", "measurementsUnitSensorMaxValue"),
        ("PDU2-MIB", "measurementsUnitSensorSignedMaxValue"),
        ("PDU2-MIB", "measurementsUnitSensorMaxTimeStamp"),
        ("PDU2-MIB", "measurementsUnitSensorMinMaxResetTimeStamp"),
        ("PDU2-MIB", "measurementsUnitSensorResetTimeStamp"),
        ("PDU2-MIB", "measurementsInletSensorIsAvailable"),
        ("PDU2-MIB", "measurementsInletSensorState"),
        ("PDU2-MIB", "measurementsInletSensorValue"),
        ("PDU2-MIB", "measurementsInletSensorTimeStamp"),
        ("PDU2-MIB", "measurementsInletSensorSignedValue"),
        ("PDU2-MIB", "measurementsInletSensorMinMaxValid"),
        ("PDU2-MIB", "measurementsInletSensorMinValue"),
        ("PDU2-MIB", "measurementsInletSensorSignedMinValue"),
        ("PDU2-MIB", "measurementsInletSensorMinTimeStamp"),
        ("PDU2-MIB", "measurementsInletSensorMaxValue"),
        ("PDU2-MIB", "measurementsInletSensorSignedMaxValue"),
        ("PDU2-MIB", "measurementsInletSensorMaxTimeStamp"),
        ("PDU2-MIB", "measurementsInletSensorMinMaxResetTimeStamp"),
        ("PDU2-MIB", "measurementsInletSensorResetTimeStamp"),
        ("PDU2-MIB", "measurementsInletPoleSensorIsAvailable"),
        ("PDU2-MIB", "measurementsInletPoleSensorState"),
        ("PDU2-MIB", "measurementsInletPoleSensorValue"),
        ("PDU2-MIB", "measurementsInletPoleSensorTimeStamp"),
        ("PDU2-MIB", "measurementsInletPoleSensorSignedValue"),
        ("PDU2-MIB", "measurementsInletPoleSensorMinMaxValid"),
        ("PDU2-MIB", "measurementsInletPoleSensorMinValue"),
        ("PDU2-MIB", "measurementsInletPoleSensorSignedMinValue"),
        ("PDU2-MIB", "measurementsInletPoleSensorMinTimeStamp"),
        ("PDU2-MIB", "measurementsInletPoleSensorMaxValue"),
        ("PDU2-MIB", "measurementsInletPoleSensorSignedMaxValue"),
        ("PDU2-MIB", "measurementsInletPoleSensorMaxTimeStamp"),
        ("PDU2-MIB", "measurementsInletPoleSensorMinMaxResetTimeStamp"),
        ("PDU2-MIB", "measurementsInletLinePairSensorIsAvailable"),
        ("PDU2-MIB", "measurementsInletLinePairSensorState"),
        ("PDU2-MIB", "measurementsInletLinePairSensorValue"),
        ("PDU2-MIB", "measurementsInletLinePairSensorTimeStamp"),
        ("PDU2-MIB", "measurementsInletLinePairSensorSignedValue"),
        ("PDU2-MIB", "measurementsInletLinePairSensorMinMaxValid"),
        ("PDU2-MIB", "measurementsInletLinePairSensorMinValue"),
        ("PDU2-MIB", "measurementsInletLinePairSensorSignedMinValue"),
        ("PDU2-MIB", "measurementsInletLinePairSensorMinTimeStamp"),
        ("PDU2-MIB", "measurementsInletLinePairSensorMaxValue"),
        ("PDU2-MIB", "measurementsInletLinePairSensorSignedMaxValue"),
        ("PDU2-MIB", "measurementsInletLinePairSensorMaxTimeStamp"),
        ("PDU2-MIB", "measurementsInletLinePairSensorMinMaxResetTimeStamp"),
        ("PDU2-MIB", "measurementsOutletSensorIsAvailable"),
        ("PDU2-MIB", "measurementsOutletSensorState"),
        ("PDU2-MIB", "measurementsOutletSensorValue"),
        ("PDU2-MIB", "measurementsOutletSensorTimeStamp"),
        ("PDU2-MIB", "measurementsOutletSensorSignedValue"),
        ("PDU2-MIB", "measurementsOutletSensorMinMaxValid"),
        ("PDU2-MIB", "measurementsOutletSensorMinValue"),
        ("PDU2-MIB", "measurementsOutletSensorSignedMinValue"),
        ("PDU2-MIB", "measurementsOutletSensorMinTimeStamp"),
        ("PDU2-MIB", "measurementsOutletSensorMaxValue"),
        ("PDU2-MIB", "measurementsOutletSensorSignedMaxValue"),
        ("PDU2-MIB", "measurementsOutletSensorMaxTimeStamp"),
        ("PDU2-MIB", "measurementsOutletSensorMinMaxResetTimeStamp"),
        ("PDU2-MIB", "measurementsOutletSensorResetTimeStamp"),
        ("PDU2-MIB", "measurementsOutletPoleSensorIsAvailable"),
        ("PDU2-MIB", "measurementsOutletPoleSensorState"),
        ("PDU2-MIB", "measurementsOutletPoleSensorValue"),
        ("PDU2-MIB", "measurementsOutletPoleSensorTimeStamp"),
        ("PDU2-MIB", "measurementsOutletPoleSensorSignedValue"),
        ("PDU2-MIB", "measurementsOutletPoleSensorMinMaxValid"),
        ("PDU2-MIB", "measurementsOutletPoleSensorMinValue"),
        ("PDU2-MIB", "measurementsOutletPoleSensorSignedMinValue"),
        ("PDU2-MIB", "measurementsOutletPoleSensorMinTimeStamp"),
        ("PDU2-MIB", "measurementsOutletPoleSensorMaxValue"),
        ("PDU2-MIB", "measurementsOutletPoleSensorSignedMaxValue"),
        ("PDU2-MIB", "measurementsOutletPoleSensorMaxTimeStamp"),
        ("PDU2-MIB", "measurementsOutletPoleSensorMinMaxResetTimeStamp"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorIsAvailable"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorState"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorValue"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorTimeStamp"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorSignedValue"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorMinMaxValid"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorMinValue"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorSignedMinValue"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorMinTimeStamp"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorMaxValue"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorSignedMaxValue"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorMaxTimeStamp"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorMinMaxResetTimeStamp"),
        ("PDU2-MIB", "measurementsExternalSensorIsAvailable"),
        ("PDU2-MIB", "measurementsExternalSensorState"),
        ("PDU2-MIB", "measurementsExternalSensorValue"),
        ("PDU2-MIB", "measurementsExternalSensorTimeStamp"),
        ("PDU2-MIB", "measurementsExternalSensorMinMaxValid"),
        ("PDU2-MIB", "measurementsExternalSensorMinValue"),
        ("PDU2-MIB", "measurementsExternalSensorMinTimeStamp"),
        ("PDU2-MIB", "measurementsExternalSensorMaxValue"),
        ("PDU2-MIB", "measurementsExternalSensorMaxTimeStamp"),
        ("PDU2-MIB", "measurementsExternalSensorMinMaxResetTimeStamp"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorIsAvailable"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorState"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorValue"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorTimeStamp"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorSignedValue"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorMinMaxValid"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorMinValue"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorSignedMinValue"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorMinTimeStamp"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorMaxValue"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorSignedMaxValue"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorMaxTimeStamp"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorMinMaxResetTimeStamp"),
        ("PDU2-MIB", "measurementsCircuitSensorIsAvailable"),
        ("PDU2-MIB", "measurementsCircuitSensorState"),
        ("PDU2-MIB", "measurementsCircuitSensorValue"),
        ("PDU2-MIB", "measurementsCircuitSensorTimeStamp"),
        ("PDU2-MIB", "measurementsCircuitSensorSignedValue"),
        ("PDU2-MIB", "measurementsCircuitSensorMinMaxValid"),
        ("PDU2-MIB", "measurementsCircuitSensorMinValue"),
        ("PDU2-MIB", "measurementsCircuitSensorSignedMinValue"),
        ("PDU2-MIB", "measurementsCircuitSensorMinTimeStamp"),
        ("PDU2-MIB", "measurementsCircuitSensorMaxValue"),
        ("PDU2-MIB", "measurementsCircuitSensorSignedMaxValue"),
        ("PDU2-MIB", "measurementsCircuitSensorMaxTimeStamp"),
        ("PDU2-MIB", "measurementsCircuitSensorMinMaxResetTimeStamp"),
        ("PDU2-MIB", "measurementsCircuitSensorResetTimeStamp"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorIsAvailable"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorState"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorValue"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorTimeStamp"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorSignedValue"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorMinMaxValid"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorMinValue"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorSignedMinValue"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorMinTimeStamp"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorMaxValue"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorSignedMaxValue"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorMaxTimeStamp"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorMinMaxResetTimeStamp"),
        ("PDU2-MIB", "measurementsOutletGroupSensorIsAvailable"),
        ("PDU2-MIB", "measurementsOutletGroupSensorState"),
        ("PDU2-MIB", "measurementsOutletGroupSensorValue"),
        ("PDU2-MIB", "measurementsOutletGroupSensorTimeStamp"),
        ("PDU2-MIB", "measurementsOutletGroupSensorSignedValue"),
        ("PDU2-MIB", "measurementsOutletGroupSensorMinMaxValid"),
        ("PDU2-MIB", "measurementsOutletGroupSensorMinValue"),
        ("PDU2-MIB", "measurementsOutletGroupSensorSignedMinValue"),
        ("PDU2-MIB", "measurementsOutletGroupSensorMinTimeStamp"),
        ("PDU2-MIB", "measurementsOutletGroupSensorMaxValue"),
        ("PDU2-MIB", "measurementsOutletGroupSensorSignedMaxValue"),
        ("PDU2-MIB", "measurementsOutletGroupSensorMaxTimeStamp"),
        ("PDU2-MIB", "measurementsOutletGroupSensorMinMaxResetTimeStamp"),
        ("PDU2-MIB", "measurementsOutletGroupSensorResetTimeStamp"))
)
if mibBuilder.loadTexts:
    measurementsGroup.setStatus("current")

controlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 2, 4)
)
controlGroup.setObjects(
      *(("PDU2-MIB", "switchingOperation"),
        ("PDU2-MIB", "outletSwitchingState"),
        ("PDU2-MIB", "outletSwitchingTimeStamp"),
        ("PDU2-MIB", "outletSuspendedState"),
        ("PDU2-MIB", "transferSwitchActiveInlet"),
        ("PDU2-MIB", "transferSwitchTransferToInlet"),
        ("PDU2-MIB", "transferSwitchAlarmOverride"),
        ("PDU2-MIB", "transferSwitchLastTransferReason"),
        ("PDU2-MIB", "actuatorState"),
        ("PDU2-MIB", "rcmState"),
        ("PDU2-MIB", "inletSensorResetValue"),
        ("PDU2-MIB", "inletSensorResetMinMax"),
        ("PDU2-MIB", "inletPoleSensorResetMinMax"),
        ("PDU2-MIB", "inletLinePairSensorResetMinMax"),
        ("PDU2-MIB", "outletSensorResetValue"),
        ("PDU2-MIB", "outletSensorResetMinMax"),
        ("PDU2-MIB", "outletPoleSensorResetMinMax"),
        ("PDU2-MIB", "unitSensorResetValue"),
        ("PDU2-MIB", "unitSensorResetMinMax"),
        ("PDU2-MIB", "overCurrentProtectorSensorResetMinMax"),
        ("PDU2-MIB", "externalSensorResetMinMax"),
        ("PDU2-MIB", "transferSwitchSensorResetMinMax"),
        ("PDU2-MIB", "circuitSensorResetValue"),
        ("PDU2-MIB", "circuitSensorResetMinMax"),
        ("PDU2-MIB", "circuitPoleSensorResetMinMax"),
        ("PDU2-MIB", "outletGroupSwitchingOperation"),
        ("PDU2-MIB", "outletGroupSensorResetValue"),
        ("PDU2-MIB", "outletGroupSensorResetMinMax"),
        ("PDU2-MIB", "serverPowerControlOperation"),
        ("PDU2-MIB", "overCurrentProtectorRcmState"))
)
if mibBuilder.loadTexts:
    controlGroup.setStatus("current")

trapInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 2, 5)
)
trapInformationGroup.setObjects(
      *(("PDU2-MIB", "userName"),
        ("PDU2-MIB", "targetUser"),
        ("PDU2-MIB", "newTargetUser"),
        ("PDU2-MIB", "imageVersion"),
        ("PDU2-MIB", "roleName"),
        ("PDU2-MIB", "oldSensorState"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "inletPoleNumber"),
        ("PDU2-MIB", "outletPoleNumber"),
        ("PDU2-MIB", "externalSensorNumber"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "smtpMessageRecipients"),
        ("PDU2-MIB", "smtpServer"),
        ("PDU2-MIB", "errorDescription"),
        ("PDU2-MIB", "deviceChangedParameter"),
        ("PDU2-MIB", "changedParameterNewValue"),
        ("PDU2-MIB", "webcamModel"),
        ("PDU2-MIB", "webcamConnectionPort"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "peripheralDeviceRomcode"),
        ("PDU2-MIB", "peripheralDeviceFirmwareUpdateState"),
        ("PDU2-MIB", "circuitNumber"),
        ("PDU2-MIB", "circuitPoleNumber"),
        ("PDU2-MIB", "phoneNumber"),
        ("PDU2-MIB", "smartCardReaderId"),
        ("PDU2-MIB", "smartCardTimestamp"),
        ("PDU2-MIB", "smartCardType"),
        ("PDU2-MIB", "smartCardId"),
        ("PDU2-MIB", "suspectedTripCauseLabel"),
        ("PDU2-MIB", "smartCardReaderDescription"),
        ("PDU2-MIB", "smartCardReaderManufacturer"),
        ("PDU2-MIB", "smartCardReaderName"),
        ("PDU2-MIB", "smartCardReaderProduct"),
        ("PDU2-MIB", "smartCardReaderSerialNumber"),
        ("PDU2-MIB", "smartCardReaderChannel"),
        ("PDU2-MIB", "smartCardReaderPosition"),
        ("PDU2-MIB", "outletGroupNumber"),
        ("PDU2-MIB", "serverPowerOperation"),
        ("PDU2-MIB", "serverPowerResult"),
        ("PDU2-MIB", "webcamName"),
        ("PDU2-MIB", "webcamFolderUrl"),
        ("PDU2-MIB", "keypadDescription"),
        ("PDU2-MIB", "keypadId"),
        ("PDU2-MIB", "keypadPinTimestamp"),
        ("PDU2-MIB", "keypadPin"),
        ("PDU2-MIB", "keypadManufacturer"),
        ("PDU2-MIB", "keypadName"),
        ("PDU2-MIB", "keypadProduct"),
        ("PDU2-MIB", "keypadSerialNumber"),
        ("PDU2-MIB", "keypadChannel"),
        ("PDU2-MIB", "keypadPosition"),
        ("PDU2-MIB", "doorAccessRuleId"),
        ("PDU2-MIB", "doorAccessDenialReason"),
        ("PDU2-MIB", "doorAccessRuleName"),
        ("PDU2-MIB", "inletLinePairNumber"),
        ("PDU2-MIB", "dipSwellEventVoltage"),
        ("PDU2-MIB", "dipSwellEventTimeStamp"),
        ("PDU2-MIB", "dipSwellEventDuration"),
        ("PDU2-MIB", "portFuseState"),
        ("PDU2-MIB", "externalPortFuseId"),
        ("PDU2-MIB", "externalPortName"),
        ("PDU2-MIB", "linkUnitId"),
        ("PDU2-MIB", "linkUnitAddress"),
        ("PDU2-MIB", "doorHandleName"),
        ("PDU2-MIB", "doorLockName"),
        ("PDU2-MIB", "doorStateName"))
)
if mibBuilder.loadTexts:
    trapInformationGroup.setStatus("current")

reliabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 2, 10)
)
reliabilityGroup.setObjects(
      *(("PDU2-MIB", "reliabilityId"),
        ("PDU2-MIB", "reliabilityDataValue"),
        ("PDU2-MIB", "reliabilityDataMaxPossible"),
        ("PDU2-MIB", "reliabilityDataWorstValue"),
        ("PDU2-MIB", "reliabilityDataThreshold"),
        ("PDU2-MIB", "reliabilityDataRawUpperBytes"),
        ("PDU2-MIB", "reliabilityDataRawLowerBytes"),
        ("PDU2-MIB", "reliabilityDataFlags"),
        ("PDU2-MIB", "reliabilityErrorLogId"),
        ("PDU2-MIB", "reliabilityErrorLogValue"),
        ("PDU2-MIB", "reliabilityErrorLogThreshold"),
        ("PDU2-MIB", "reliabilityErrorLogRawUpperBytes"),
        ("PDU2-MIB", "reliabilityErrorLogRawLowerBytes"),
        ("PDU2-MIB", "reliabilityErrorLogPOH"),
        ("PDU2-MIB", "reliabilityErrorLogTime"),
        ("PDU2-MIB", "reliabilityDataTableSequenceNumber"),
        ("PDU2-MIB", "hwFailureComponentId"),
        ("PDU2-MIB", "hwFailureType"),
        ("PDU2-MIB", "hwFailureAsserted"),
        ("PDU2-MIB", "hwFailureLastAssertTimeStamp"),
        ("PDU2-MIB", "hwFailureLastDeassertTimeStamp"),
        ("PDU2-MIB", "hwFailureAssertCount"))
)
if mibBuilder.loadTexts:
    reliabilityGroup.setStatus("current")

ipAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 2, 12)
)
ipAddressGroup.setObjects(
      *(("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "netmask"),
        ("PDU2-MIB", "gateway"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "pxInetNetmask"),
        ("PDU2-MIB", "pxInetGateway"))
)
if mibBuilder.loadTexts:
    ipAddressGroup.setStatus("deprecated")

oldConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 2, 13)
)
oldConfigGroup.setObjects(
      *(("PDU2-MIB", "outletSequencingDelay"),
        ("PDU2-MIB", "unitSensorAccuracy"),
        ("PDU2-MIB", "unitSensorTolerance"),
        ("PDU2-MIB", "inletSensorAccuracy"),
        ("PDU2-MIB", "inletSensorTolerance"),
        ("PDU2-MIB", "inletPoleSensorAccuracy"),
        ("PDU2-MIB", "inletPoleSensorTolerance"),
        ("PDU2-MIB", "outletSensorAccuracy"),
        ("PDU2-MIB", "outletSensorTolerance"),
        ("PDU2-MIB", "outletPoleSensorAccuracy"),
        ("PDU2-MIB", "outletPoleSensorTolerance"),
        ("PDU2-MIB", "overCurrentProtectorSensorAccuracy"),
        ("PDU2-MIB", "overCurrentProtectorSensorTolerance"),
        ("PDU2-MIB", "externalSensorAccuracy"),
        ("PDU2-MIB", "externalSensorTolerance"),
        ("PDU2-MIB", "transferSwitchSensorAccuracy"),
        ("PDU2-MIB", "transferSwitchSensorTolerance"),
        ("PDU2-MIB", "inletRatedFrequency"),
        ("PDU2-MIB", "inletRatedVA"),
        ("PDU2-MIB", "pxMACAddress"),
        ("PDU2-MIB", "networkInterfaceType"),
        ("PDU2-MIB", "activeDNSServerAddressSource"),
        ("PDU2-MIB", "activeNTPServerAddressSource"),
        ("PDU2-MIB", "inletPlug"),
        ("PDU2-MIB", "outletReceptacle"),
        ("PDU2-MIB", "lhxSupportEnabled"))
)
if mibBuilder.loadTexts:
    oldConfigGroup.setStatus("deprecated")

obsoleteObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 2, 20)
)
obsoleteObjectsGroup.setObjects(
      *(("PDU2-MIB", "useDHCPProvidedNTPServer"),
        ("PDU2-MIB", "inletRCMResidualOperatingCurrent"),
        ("PDU2-MIB", "wireSensorAccuracy"),
        ("PDU2-MIB", "wireSensorTolerance"),
        ("PDU2-MIB", "wireCount"),
        ("PDU2-MIB", "wireLabel"),
        ("PDU2-MIB", "wireCapabilities"),
        ("PDU2-MIB", "wireSensorLogAvailable"),
        ("PDU2-MIB", "wireSensorUnits"),
        ("PDU2-MIB", "wireSensorDecimalDigits"),
        ("PDU2-MIB", "wireSensorResolution"),
        ("PDU2-MIB", "wireSensorMaximum"),
        ("PDU2-MIB", "wireSensorMinimum"),
        ("PDU2-MIB", "wireSensorHysteresis"),
        ("PDU2-MIB", "wireSensorStateChangeDelay"),
        ("PDU2-MIB", "wireSensorLowerCriticalThreshold"),
        ("PDU2-MIB", "wireSensorLowerWarningThreshold"),
        ("PDU2-MIB", "wireSensorUpperCriticalThreshold"),
        ("PDU2-MIB", "wireSensorUpperWarningThreshold"),
        ("PDU2-MIB", "wireSensorEnabledThresholds"),
        ("PDU2-MIB", "wirePowerSource"),
        ("PDU2-MIB", "logWireSensorDataAvailable"),
        ("PDU2-MIB", "logWireSensorState"),
        ("PDU2-MIB", "logWireSensorAvgValue"),
        ("PDU2-MIB", "logWireSensorMaxValue"),
        ("PDU2-MIB", "logWireSensorMinValue"),
        ("PDU2-MIB", "measurementsWireSensorIsAvailable"),
        ("PDU2-MIB", "measurementsWireSensorState"),
        ("PDU2-MIB", "measurementsWireSensorValue"),
        ("PDU2-MIB", "measurementsWireSensorTimeStamp"))
)
if mibBuilder.loadTexts:
    obsoleteObjectsGroup.setStatus("obsolete")


# Notification objects

systemStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 1)
)
systemStarted.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    systemStarted.setStatus(
        "current"
    )

systemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 2)
)
systemReset.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    systemReset.setStatus(
        "current"
    )

userLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 3)
)
userLogin.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    userLogin.setStatus(
        "current"
    )

userLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 4)
)
userLogout.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    userLogout.setStatus(
        "current"
    )

userAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 5)
)
userAuthenticationFailure.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    userAuthenticationFailure.setStatus(
        "current"
    )

userSessionTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 8)
)
userSessionTimeout.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    userSessionTimeout.setStatus(
        "current"
    )

userAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 11)
)
userAdded.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "targetUser"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    userAdded.setStatus(
        "current"
    )

userModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 12)
)
userModified.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "targetUser"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    userModified.setStatus(
        "current"
    )

userDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 13)
)
userDeleted.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "targetUser"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    userDeleted.setStatus(
        "current"
    )

roleAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 14)
)
roleAdded.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "roleName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    roleAdded.setStatus(
        "current"
    )

roleModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 15)
)
roleModified.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "roleName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    roleModified.setStatus(
        "current"
    )

roleDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 16)
)
roleDeleted.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "roleName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    roleDeleted.setStatus(
        "current"
    )

deviceUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 20)
)
deviceUpdateStarted.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "imageVersion"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    deviceUpdateStarted.setStatus(
        "current"
    )

deviceUpdateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 21)
)
deviceUpdateCompleted.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "imageVersion"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    deviceUpdateCompleted.setStatus(
        "current"
    )

userBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 22)
)
userBlocked.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    userBlocked.setStatus(
        "current"
    )

powerControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 23)
)
powerControl.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "outletLabel"),
        ("PDU2-MIB", "measurementsOutletSensorState"),
        ("PDU2-MIB", "switchingOperation"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    powerControl.setStatus(
        "current"
    )

userPasswordChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 24)
)
userPasswordChanged.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "targetUser"),
        ("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    userPasswordChanged.setStatus(
        "current"
    )

passwordSettingsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 28)
)
passwordSettingsChanged.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    passwordSettingsChanged.setStatus(
        "current"
    )

firmwareValidationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 38)
)
firmwareValidationFailed.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    firmwareValidationFailed.setStatus(
        "current"
    )

logFileCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 41)
)
logFileCleared.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    logFileCleared.setStatus(
        "current"
    )

bulkConfigurationSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 53)
)
bulkConfigurationSaved.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    bulkConfigurationSaved.setStatus(
        "current"
    )

bulkConfigurationCopied = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 54)
)
bulkConfigurationCopied.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    bulkConfigurationCopied.setStatus(
        "current"
    )

pduSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 60)
)
pduSensorStateChange.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "measurementsUnitSensorTimeStamp"),
        ("PDU2-MIB", "measurementsUnitSensorValue"),
        ("PDU2-MIB", "measurementsUnitSensorState"),
        ("PDU2-MIB", "measurementsUnitSensorSignedValue"),
        ("PDU2-MIB", "oldSensorState"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    pduSensorStateChange.setStatus(
        "deprecated"
    )

inletSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 61)
)
inletSensorStateChange.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "inletLabel"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "measurementsInletSensorTimeStamp"),
        ("PDU2-MIB", "measurementsInletSensorValue"),
        ("PDU2-MIB", "measurementsInletSensorState"),
        ("PDU2-MIB", "measurementsInletSensorSignedValue"),
        ("PDU2-MIB", "oldSensorState"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    inletSensorStateChange.setStatus(
        "current"
    )

inletPoleSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 62)
)
inletPoleSensorStateChange.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "inletLabel"),
        ("PDU2-MIB", "inletPoleNumber"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "measurementsInletPoleSensorTimeStamp"),
        ("PDU2-MIB", "measurementsInletPoleSensorValue"),
        ("PDU2-MIB", "measurementsInletPoleSensorState"),
        ("PDU2-MIB", "measurementsInletPoleSensorSignedValue"),
        ("PDU2-MIB", "oldSensorState"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    inletPoleSensorStateChange.setStatus(
        "current"
    )

outletSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 63)
)
outletSensorStateChange.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "outletLabel"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "measurementsOutletSensorTimeStamp"),
        ("PDU2-MIB", "measurementsOutletSensorValue"),
        ("PDU2-MIB", "measurementsOutletSensorState"),
        ("PDU2-MIB", "measurementsOutletSensorSignedValue"),
        ("PDU2-MIB", "oldSensorState"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    outletSensorStateChange.setStatus(
        "current"
    )

outletPoleSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 64)
)
outletPoleSensorStateChange.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "outletLabel"),
        ("PDU2-MIB", "outletPoleNumber"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "measurementsOutletPoleSensorTimeStamp"),
        ("PDU2-MIB", "measurementsOutletPoleSensorValue"),
        ("PDU2-MIB", "measurementsOutletPoleSensorState"),
        ("PDU2-MIB", "measurementsOutletPoleSensorSignedValue"),
        ("PDU2-MIB", "oldSensorState"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    outletPoleSensorStateChange.setStatus(
        "current"
    )

overCurrentProtectorSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 65)
)
overCurrentProtectorSensorStateChange.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "overCurrentProtectorLabel"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorTimeStamp"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorValue"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorState"),
        ("PDU2-MIB", "measurementsOverCurrentProtectorSensorSignedValue"),
        ("PDU2-MIB", "oldSensorState"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "suspectedTripCauseLabel"))
)
if mibBuilder.loadTexts:
    overCurrentProtectorSensorStateChange.setStatus(
        "current"
    )

externalSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 66)
)
externalSensorStateChange.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "externalSensorNumber"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "measurementsExternalSensorTimeStamp"),
        ("PDU2-MIB", "measurementsExternalSensorValue"),
        ("PDU2-MIB", "measurementsExternalSensorState"),
        ("PDU2-MIB", "oldSensorState"),
        ("PDU2-MIB", "externalSensorSerialNumber"),
        ("PDU2-MIB", "externalOnOffSensorSubtype"),
        ("PDU2-MIB", "externalSensorChannelNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "externalSensorName"))
)
if mibBuilder.loadTexts:
    externalSensorStateChange.setStatus(
        "current"
    )

smtpMessageTransmissionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 67)
)
smtpMessageTransmissionFailure.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "smtpMessageRecipients"),
        ("PDU2-MIB", "smtpServer"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    smtpMessageTransmissionFailure.setStatus(
        "current"
    )

ldapError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 68)
)
ldapError.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "errorDescription"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    ldapError.setStatus(
        "current"
    )

deviceUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 70)
)
deviceUpdateFailed.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "imageVersion"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    deviceUpdateFailed.setStatus(
        "current"
    )

loadSheddingModeEntered = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 71)
)
loadSheddingModeEntered.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    loadSheddingModeEntered.setStatus(
        "current"
    )

loadSheddingModeExited = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 72)
)
loadSheddingModeExited.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    loadSheddingModeExited.setStatus(
        "current"
    )

pingServerEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 73)
)
pingServerEnabled.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "serverIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    pingServerEnabled.setStatus(
        "current"
    )

pingServerDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 74)
)
pingServerDisabled.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "serverIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    pingServerDisabled.setStatus(
        "current"
    )

serverNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 75)
)
serverNotReachable.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "serverIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    serverNotReachable.setStatus(
        "current"
    )

serverReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 76)
)
serverReachable.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "serverIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    serverReachable.setStatus(
        "current"
    )

rfCodeTagConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 77)
)
rfCodeTagConnected.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    rfCodeTagConnected.setStatus(
        "deprecated"
    )

rfCodeTagDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 78)
)
rfCodeTagDisconnected.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    rfCodeTagDisconnected.setStatus(
        "deprecated"
    )

deviceIdentificationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 79)
)
deviceIdentificationChanged.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "deviceChangedParameter"),
        ("PDU2-MIB", "changedParameterNewValue"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    deviceIdentificationChanged.setStatus(
        "current"
    )

usbExpansionUnitConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 80)
)
usbExpansionUnitConnected.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    usbExpansionUnitConnected.setStatus(
        "current"
    )

usbExpansionUnitDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 81)
)
usbExpansionUnitDisconnected.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    usbExpansionUnitDisconnected.setStatus(
        "current"
    )

lhxSupportChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 82)
)
lhxSupportChanged.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "lhxSupportEnabled"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    lhxSupportChanged.setStatus(
        "deprecated"
    )

userAcceptedRestrictedServiceAgreement = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 83)
)
userAcceptedRestrictedServiceAgreement.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    userAcceptedRestrictedServiceAgreement.setStatus(
        "current"
    )

userDeclinedRestrictedServiceAgreement = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 84)
)
userDeclinedRestrictedServiceAgreement.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    userDeclinedRestrictedServiceAgreement.setStatus(
        "current"
    )

wireSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 85)
)
wireSensorStateChange.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "wireLabel"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "measurementsWireSensorTimeStamp"),
        ("PDU2-MIB", "measurementsWireSensorValue"),
        ("PDU2-MIB", "measurementsWireSensorState"),
        ("PDU2-MIB", "oldSensorState"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    wireSensorStateChange.setStatus(
        "obsolete"
    )

transferSwitchSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 86)
)
transferSwitchSensorStateChange.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "transferSwitchLabel"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorTimeStamp"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorValue"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorState"),
        ("PDU2-MIB", "measurementsTransferSwitchSensorSignedValue"),
        ("PDU2-MIB", "oldSensorState"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "transferSwitchLastTransferReason"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    transferSwitchSensorStateChange.setStatus(
        "current"
    )

deviceSettingsSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 88)
)
deviceSettingsSaved.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    deviceSettingsSaved.setStatus(
        "current"
    )

deviceSettingsRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 89)
)
deviceSettingsRestored.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxIPAddress"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    deviceSettingsRestored.setStatus(
        "current"
    )

webcamInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 90)
)
webcamInserted.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "webcamModel"),
        ("PDU2-MIB", "webcamConnectionPort"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    webcamInserted.setStatus(
        "current"
    )

webcamRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 91)
)
webcamRemoved.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "webcamModel"),
        ("PDU2-MIB", "webcamConnectionPort"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    webcamRemoved.setStatus(
        "current"
    )

inletEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 92)
)
inletEnabled.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "inletLabel"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    inletEnabled.setStatus(
        "current"
    )

inletDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 93)
)
inletDisabled.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "inletLabel"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    inletDisabled.setStatus(
        "current"
    )

serverConnectivityUnrecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 94)
)
serverConnectivityUnrecoverable.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "serverIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    serverConnectivityUnrecoverable.setStatus(
        "current"
    )

radiusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 95)
)
radiusError.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "errorDescription"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    radiusError.setStatus(
        "current"
    )

serverReachabilityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 96)
)
serverReachabilityError.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "serverIPAddress"),
        ("PDU2-MIB", "errorDescription"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    serverReachabilityError.setStatus(
        "current"
    )

inletSensorReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 97)
)
inletSensorReset.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "inletLabel"),
        ("PDU2-MIB", "typeOfSensor"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    inletSensorReset.setStatus(
        "current"
    )

outletSensorReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 98)
)
outletSensorReset.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "outletLabel"),
        ("PDU2-MIB", "typeOfSensor"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    outletSensorReset.setStatus(
        "current"
    )

unknownPeripheralDeviceAttached = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 99)
)
unknownPeripheralDeviceAttached.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "peripheralDeviceRomcode"),
        ("PDU2-MIB", "peripheralDevicePackagePosition"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    unknownPeripheralDeviceAttached.setStatus(
        "current"
    )

peripheralDeviceFirmwareUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 100)
)
peripheralDeviceFirmwareUpdate.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "peripheralDevicePackageSerialNumber"),
        ("PDU2-MIB", "peripheralDeviceFirmwareUpdateState"),
        ("PDU2-MIB", "peripheralDevicePackageFirmwareVersion"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    peripheralDeviceFirmwareUpdate.setStatus(
        "current"
    )

unitSensorReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 101)
)
unitSensorReset.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "typeOfSensor"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    unitSensorReset.setStatus(
        "current"
    )

unitSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 102)
)
unitSensorStateChange.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "measurementsUnitSensorTimeStamp"),
        ("PDU2-MIB", "measurementsUnitSensorValue"),
        ("PDU2-MIB", "measurementsUnitSensorState"),
        ("PDU2-MIB", "measurementsUnitSensorSignedValue"),
        ("PDU2-MIB", "oldSensorState"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    unitSensorStateChange.setStatus(
        "current"
    )

circuitSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 103)
)
circuitSensorStateChange.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "circuitNumber"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "measurementsCircuitSensorTimeStamp"),
        ("PDU2-MIB", "measurementsCircuitSensorValue"),
        ("PDU2-MIB", "measurementsCircuitSensorState"),
        ("PDU2-MIB", "measurementsCircuitSensorSignedValue"),
        ("PDU2-MIB", "oldSensorState"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    circuitSensorStateChange.setStatus(
        "current"
    )

circuitPoleSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 104)
)
circuitPoleSensorStateChange.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "circuitNumber"),
        ("PDU2-MIB", "circuitPoleNumber"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorTimeStamp"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorValue"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorState"),
        ("PDU2-MIB", "measurementsCircuitPoleSensorSignedValue"),
        ("PDU2-MIB", "oldSensorState"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    circuitPoleSensorStateChange.setStatus(
        "current"
    )

circuitAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 105)
)
circuitAdded.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "circuitNumber"),
        ("PDU2-MIB", "circuitName"),
        ("PDU2-MIB", "circuitType"),
        ("PDU2-MIB", "circuitRatedCurrent"),
        ("PDU2-MIB", "circuitCTRating"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    circuitAdded.setStatus(
        "current"
    )

circuitDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 106)
)
circuitDeleted.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "circuitNumber"),
        ("PDU2-MIB", "circuitName"),
        ("PDU2-MIB", "circuitType"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    circuitDeleted.setStatus(
        "current"
    )

circuitModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 107)
)
circuitModified.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "circuitNumber"),
        ("PDU2-MIB", "circuitName"),
        ("PDU2-MIB", "circuitType"),
        ("PDU2-MIB", "circuitRatedCurrent"),
        ("PDU2-MIB", "circuitCTRating"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    circuitModified.setStatus(
        "current"
    )

circuitSensorReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 108)
)
circuitSensorReset.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "circuitNumber"),
        ("PDU2-MIB", "typeOfSensor"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    circuitSensorReset.setStatus(
        "current"
    )

powerMeterAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 109)
)
powerMeterAdded.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "powerMeterPhaseCTRating"),
        ("PDU2-MIB", "powerMeterNeutralCTRating"),
        ("PDU2-MIB", "powerMeterEarthCTRating"),
        ("PDU2-MIB", "powerMeterPanelPositions"),
        ("PDU2-MIB", "powerMeterPanelLayout"),
        ("PDU2-MIB", "powerMeterPanelNumbering"),
        ("PDU2-MIB", "powerMeterType"),
        ("PDU2-MIB", "inletRatedCurrent"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    powerMeterAdded.setStatus(
        "current"
    )

powerMeterDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 110)
)
powerMeterDeleted.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "powerMeterType"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    powerMeterDeleted.setStatus(
        "current"
    )

powerMeterModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 111)
)
powerMeterModified.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "powerMeterPhaseCTRating"),
        ("PDU2-MIB", "powerMeterNeutralCTRating"),
        ("PDU2-MIB", "powerMeterEarthCTRating"),
        ("PDU2-MIB", "powerMeterType"),
        ("PDU2-MIB", "inletRatedCurrent"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    powerMeterModified.setStatus(
        "current"
    )

smsMessageTransmissionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 112)
)
smsMessageTransmissionFailure.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "phoneNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    smsMessageTransmissionFailure.setStatus(
        "current"
    )

smartCardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 113)
)
smartCardInserted.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "smartCardReaderId"),
        ("PDU2-MIB", "smartCardTimestamp"),
        ("PDU2-MIB", "smartCardType"),
        ("PDU2-MIB", "smartCardId"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "smartCardReaderManufacturer"),
        ("PDU2-MIB", "smartCardReaderProduct"),
        ("PDU2-MIB", "smartCardReaderSerialNumber"),
        ("PDU2-MIB", "smartCardReaderChannel"),
        ("PDU2-MIB", "smartCardReaderPosition"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "smartCardReaderName"),
        ("PDU2-MIB", "smartCardReaderDescription"))
)
if mibBuilder.loadTexts:
    smartCardInserted.setStatus(
        "current"
    )

smartCardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 114)
)
smartCardRemoved.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "smartCardReaderId"),
        ("PDU2-MIB", "smartCardTimestamp"),
        ("PDU2-MIB", "smartCardType"),
        ("PDU2-MIB", "smartCardId"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "smartCardReaderManufacturer"),
        ("PDU2-MIB", "smartCardReaderProduct"),
        ("PDU2-MIB", "smartCardReaderSerialNumber"),
        ("PDU2-MIB", "smartCardReaderChannel"),
        ("PDU2-MIB", "smartCardReaderPosition"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "smartCardReaderName"),
        ("PDU2-MIB", "smartCardReaderDescription"))
)
if mibBuilder.loadTexts:
    smartCardRemoved.setStatus(
        "current"
    )

rawConfigurationDownloaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 115)
)
rawConfigurationDownloaded.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    rawConfigurationDownloaded.setStatus(
        "current"
    )

rawConfigurationUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 116)
)
rawConfigurationUpdated.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    rawConfigurationUpdated.setStatus(
        "current"
    )

hwFailureStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 117)
)
hwFailureStatusChanged.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "hwFailureComponentId"),
        ("PDU2-MIB", "hwFailureType"),
        ("PDU2-MIB", "hwFailureAsserted"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    hwFailureStatusChanged.setStatus(
        "current"
    )

outletGroupAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 118)
)
outletGroupAdded.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "outletGroupNumber"),
        ("PDU2-MIB", "outletGroupName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    outletGroupAdded.setStatus(
        "current"
    )

outletGroupModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 119)
)
outletGroupModified.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "outletGroupNumber"),
        ("PDU2-MIB", "outletGroupName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    outletGroupModified.setStatus(
        "current"
    )

outletGroupDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 120)
)
outletGroupDeleted.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "outletGroupNumber"),
        ("PDU2-MIB", "outletGroupName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    outletGroupDeleted.setStatus(
        "current"
    )

outletGroupSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 121)
)
outletGroupSensorStateChange.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "outletGroupNumber"),
        ("PDU2-MIB", "outletGroupName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "measurementsOutletGroupSensorTimeStamp"),
        ("PDU2-MIB", "measurementsOutletGroupSensorValue"),
        ("PDU2-MIB", "measurementsOutletGroupSensorState"),
        ("PDU2-MIB", "measurementsOutletGroupSensorSignedValue"),
        ("PDU2-MIB", "oldSensorState"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    outletGroupSensorStateChange.setStatus(
        "current"
    )

outletGroupSensorReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 122)
)
outletGroupSensorReset.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "outletGroupNumber"),
        ("PDU2-MIB", "outletGroupName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "typeOfSensor"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    outletGroupSensorReset.setStatus(
        "current"
    )

outletGroupPowerControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 123)
)
outletGroupPowerControl.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "outletGroupNumber"),
        ("PDU2-MIB", "outletGroupName"),
        ("PDU2-MIB", "outletGroupSwitchingOperation"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    outletGroupPowerControl.setStatus(
        "current"
    )

serverPowerControlInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 124)
)
serverPowerControlInitiated.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "serverIPAddress"),
        ("PDU2-MIB", "serverPowerOperation"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    serverPowerControlInitiated.setStatus(
        "current"
    )

serverPowerControlCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 125)
)
serverPowerControlCompleted.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "serverIPAddress"),
        ("PDU2-MIB", "serverPowerResult"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    serverPowerControlCompleted.setStatus(
        "current"
    )

webcamStorageUploadStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 126)
)
webcamStorageUploadStarted.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "webcamName"),
        ("PDU2-MIB", "webcamFolderUrl"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    webcamStorageUploadStarted.setStatus(
        "current"
    )

testEventTriggered = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 127)
)
testEventTriggered.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "userName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    testEventTriggered.setStatus(
        "current"
    )

actuatorSwitched = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 128)
)
actuatorSwitched.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "externalSensorNumber"),
        ("PDU2-MIB", "externalSensorName"),
        ("PDU2-MIB", "externalSensorSerialNumber"),
        ("PDU2-MIB", "externalOnOffSensorSubtype"),
        ("PDU2-MIB", "externalSensorChannelNumber"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "actuatorState"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    actuatorSwitched.setStatus(
        "current"
    )

keypadPinEntered = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 129)
)
keypadPinEntered.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "keypadId"),
        ("PDU2-MIB", "keypadPinTimestamp"),
        ("PDU2-MIB", "keypadPin"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "keypadManufacturer"),
        ("PDU2-MIB", "keypadProduct"),
        ("PDU2-MIB", "keypadSerialNumber"),
        ("PDU2-MIB", "keypadChannel"),
        ("PDU2-MIB", "keypadPosition"),
        ("PDU2-MIB", "keypadName"),
        ("PDU2-MIB", "keypadDescription"))
)
if mibBuilder.loadTexts:
    keypadPinEntered.setStatus(
        "current"
    )

doorAccessGranted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 130)
)
doorAccessGranted.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "doorAccessRuleId"),
        ("PDU2-MIB", "doorAccessRuleName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    doorAccessGranted.setStatus(
        "current"
    )

doorAccessDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 131)
)
doorAccessDenied.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "doorAccessRuleId"),
        ("PDU2-MIB", "doorAccessRuleName"),
        ("PDU2-MIB", "doorAccessDenialReason"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    doorAccessDenied.setStatus(
        "current"
    )

doorAccessRuleAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 132)
)
doorAccessRuleAdded.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "doorAccessRuleId"),
        ("PDU2-MIB", "doorAccessRuleName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    doorAccessRuleAdded.setStatus(
        "current"
    )

doorAccessRuleChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 133)
)
doorAccessRuleChanged.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "doorAccessRuleId"),
        ("PDU2-MIB", "doorAccessRuleName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    doorAccessRuleChanged.setStatus(
        "current"
    )

doorAccessRuleDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 134)
)
doorAccessRuleDeleted.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "doorAccessRuleId"),
        ("PDU2-MIB", "doorAccessRuleName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    doorAccessRuleDeleted.setStatus(
        "current"
    )

inletLinePairSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 135)
)
inletLinePairSensorStateChange.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "inletLabel"),
        ("PDU2-MIB", "inletLinePairNumber"),
        ("PDU2-MIB", "typeOfSensor"),
        ("PDU2-MIB", "measurementsInletLinePairSensorTimeStamp"),
        ("PDU2-MIB", "measurementsInletLinePairSensorValue"),
        ("PDU2-MIB", "measurementsInletLinePairSensorState"),
        ("PDU2-MIB", "measurementsInletLinePairSensorSignedValue"),
        ("PDU2-MIB", "oldSensorState"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    inletLinePairSensorStateChange.setStatus(
        "current"
    )

tacPlusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 136)
)
tacPlusError.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "errorDescription"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    tacPlusError.setStatus(
        "current"
    )

outletSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 137)
)
outletSuspended.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "outletLabel"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    outletSuspended.setStatus(
        "current"
    )

userRenamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 138)
)
userRenamed.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "targetUser"),
        ("PDU2-MIB", "newTargetUser"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    userRenamed.setStatus(
        "current"
    )

inletDipEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 151)
)
inletDipEvent.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "inletLabel"),
        ("PDU2-MIB", "dipSwellEventVoltage"),
        ("PDU2-MIB", "dipSwellEventTimeStamp"),
        ("PDU2-MIB", "dipSwellEventDuration"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    inletDipEvent.setStatus(
        "current"
    )

inletSwellEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 152)
)
inletSwellEvent.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "inletLabel"),
        ("PDU2-MIB", "dipSwellEventVoltage"),
        ("PDU2-MIB", "dipSwellEventTimeStamp"),
        ("PDU2-MIB", "dipSwellEventDuration"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    inletSwellEvent.setStatus(
        "current"
    )

inletPoleDipEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 153)
)
inletPoleDipEvent.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "inletLabel"),
        ("PDU2-MIB", "inletPoleNumber"),
        ("PDU2-MIB", "dipSwellEventVoltage"),
        ("PDU2-MIB", "dipSwellEventTimeStamp"),
        ("PDU2-MIB", "dipSwellEventDuration"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    inletPoleDipEvent.setStatus(
        "current"
    )

inletPoleSwellEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 154)
)
inletPoleSwellEvent.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "inletLabel"),
        ("PDU2-MIB", "inletPoleNumber"),
        ("PDU2-MIB", "dipSwellEventVoltage"),
        ("PDU2-MIB", "dipSwellEventTimeStamp"),
        ("PDU2-MIB", "dipSwellEventDuration"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    inletPoleSwellEvent.setStatus(
        "current"
    )

portFuseStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 155)
)
portFuseStateChange.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "portFuseState"),
        ("PDU2-MIB", "externalPortFuseId"),
        ("PDU2-MIB", "externalPortName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    portFuseStateChange.setStatus(
        "current"
    )

linkUnitAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 156)
)
linkUnitAdded.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "linkUnitId"),
        ("PDU2-MIB", "linkUnitAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    linkUnitAdded.setStatus(
        "current"
    )

linkUnitReleased = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 157)
)
linkUnitReleased.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "linkUnitId"),
        ("PDU2-MIB", "linkUnitAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    linkUnitReleased.setStatus(
        "current"
    )

linkUnitCommunicationOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 158)
)
linkUnitCommunicationOk.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "linkUnitId"),
        ("PDU2-MIB", "linkUnitAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    linkUnitCommunicationOk.setStatus(
        "current"
    )

linkUnitCommunicationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 159)
)
linkUnitCommunicationFailed.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "linkUnitId"),
        ("PDU2-MIB", "linkUnitAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    linkUnitCommunicationFailed.setStatus(
        "current"
    )

doorMechanicallyUnlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 160)
)
doorMechanicallyUnlocked.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "doorHandleName"),
        ("PDU2-MIB", "doorLockName"),
        ("PDU2-MIB", "doorStateName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    doorMechanicallyUnlocked.setStatus(
        "current"
    )

doorForcedOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 161)
)
doorForcedOpen.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "pduNumber"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "doorHandleName"),
        ("PDU2-MIB", "doorLockName"),
        ("PDU2-MIB", "doorStateName"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"))
)
if mibBuilder.loadTexts:
    doorForcedOpen.setStatus(
        "current"
    )

outletServiceModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 6, 0, 162)
)
outletServiceModeChanged.setObjects(
      *(("PDU2-MIB", "pduName"),
        ("PDU2-MIB", "userName"),
        ("PDU2-MIB", "pxInetAddressType"),
        ("PDU2-MIB", "pxInetIPAddress"),
        ("PDU2-MIB", "agentInetPortNumber"),
        ("PDU2-MIB", "outletLabel"),
        ("PDU2-MIB", "outletServiceMode"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("PDU2-MIB", "pduSerialNumber"),
        ("PDU2-MIB", "pduNumber"))
)
if mibBuilder.loadTexts:
    outletServiceModeChanged.setStatus(
        "current"
    )


# Notifications groups

trapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 2, 9)
)
trapsGroup.setObjects(
      *(("PDU2-MIB", "systemStarted"),
        ("PDU2-MIB", "systemReset"),
        ("PDU2-MIB", "userLogin"),
        ("PDU2-MIB", "userLogout"),
        ("PDU2-MIB", "userAuthenticationFailure"),
        ("PDU2-MIB", "userSessionTimeout"),
        ("PDU2-MIB", "userAdded"),
        ("PDU2-MIB", "userRenamed"),
        ("PDU2-MIB", "userModified"),
        ("PDU2-MIB", "userDeleted"),
        ("PDU2-MIB", "roleAdded"),
        ("PDU2-MIB", "roleModified"),
        ("PDU2-MIB", "roleDeleted"),
        ("PDU2-MIB", "deviceUpdateStarted"),
        ("PDU2-MIB", "deviceUpdateCompleted"),
        ("PDU2-MIB", "userBlocked"),
        ("PDU2-MIB", "powerControl"),
        ("PDU2-MIB", "userPasswordChanged"),
        ("PDU2-MIB", "passwordSettingsChanged"),
        ("PDU2-MIB", "firmwareValidationFailed"),
        ("PDU2-MIB", "logFileCleared"),
        ("PDU2-MIB", "bulkConfigurationSaved"),
        ("PDU2-MIB", "bulkConfigurationCopied"),
        ("PDU2-MIB", "inletSensorStateChange"),
        ("PDU2-MIB", "inletPoleSensorStateChange"),
        ("PDU2-MIB", "outletSensorStateChange"),
        ("PDU2-MIB", "outletPoleSensorStateChange"),
        ("PDU2-MIB", "overCurrentProtectorSensorStateChange"),
        ("PDU2-MIB", "externalSensorStateChange"),
        ("PDU2-MIB", "smtpMessageTransmissionFailure"),
        ("PDU2-MIB", "ldapError"),
        ("PDU2-MIB", "deviceUpdateFailed"),
        ("PDU2-MIB", "loadSheddingModeEntered"),
        ("PDU2-MIB", "loadSheddingModeExited"),
        ("PDU2-MIB", "pingServerEnabled"),
        ("PDU2-MIB", "pingServerDisabled"),
        ("PDU2-MIB", "serverNotReachable"),
        ("PDU2-MIB", "serverReachable"),
        ("PDU2-MIB", "deviceIdentificationChanged"),
        ("PDU2-MIB", "usbExpansionUnitConnected"),
        ("PDU2-MIB", "usbExpansionUnitDisconnected"),
        ("PDU2-MIB", "userAcceptedRestrictedServiceAgreement"),
        ("PDU2-MIB", "userDeclinedRestrictedServiceAgreement"),
        ("PDU2-MIB", "transferSwitchSensorStateChange"),
        ("PDU2-MIB", "deviceSettingsSaved"),
        ("PDU2-MIB", "deviceSettingsRestored"),
        ("PDU2-MIB", "webcamInserted"),
        ("PDU2-MIB", "webcamRemoved"),
        ("PDU2-MIB", "inletEnabled"),
        ("PDU2-MIB", "inletDisabled"),
        ("PDU2-MIB", "serverConnectivityUnrecoverable"),
        ("PDU2-MIB", "radiusError"),
        ("PDU2-MIB", "serverReachabilityError"),
        ("PDU2-MIB", "inletSensorReset"),
        ("PDU2-MIB", "outletSensorReset"),
        ("PDU2-MIB", "unitSensorReset"),
        ("PDU2-MIB", "circuitSensorReset"),
        ("PDU2-MIB", "unknownPeripheralDeviceAttached"),
        ("PDU2-MIB", "peripheralDeviceFirmwareUpdate"),
        ("PDU2-MIB", "unitSensorStateChange"),
        ("PDU2-MIB", "circuitSensorStateChange"),
        ("PDU2-MIB", "circuitPoleSensorStateChange"),
        ("PDU2-MIB", "circuitAdded"),
        ("PDU2-MIB", "circuitDeleted"),
        ("PDU2-MIB", "circuitModified"),
        ("PDU2-MIB", "powerMeterAdded"),
        ("PDU2-MIB", "powerMeterDeleted"),
        ("PDU2-MIB", "powerMeterModified"),
        ("PDU2-MIB", "smsMessageTransmissionFailure"),
        ("PDU2-MIB", "smartCardInserted"),
        ("PDU2-MIB", "smartCardRemoved"),
        ("PDU2-MIB", "rawConfigurationDownloaded"),
        ("PDU2-MIB", "rawConfigurationUpdated"),
        ("PDU2-MIB", "hwFailureStatusChanged"),
        ("PDU2-MIB", "outletGroupAdded"),
        ("PDU2-MIB", "outletGroupModified"),
        ("PDU2-MIB", "outletGroupDeleted"),
        ("PDU2-MIB", "outletGroupSensorStateChange"),
        ("PDU2-MIB", "outletGroupSensorReset"),
        ("PDU2-MIB", "outletGroupPowerControl"),
        ("PDU2-MIB", "serverPowerControlInitiated"),
        ("PDU2-MIB", "serverPowerControlCompleted"),
        ("PDU2-MIB", "webcamStorageUploadStarted"),
        ("PDU2-MIB", "testEventTriggered"),
        ("PDU2-MIB", "actuatorSwitched"),
        ("PDU2-MIB", "keypadPinEntered"),
        ("PDU2-MIB", "doorAccessGranted"),
        ("PDU2-MIB", "doorAccessDenied"),
        ("PDU2-MIB", "doorAccessRuleAdded"),
        ("PDU2-MIB", "doorAccessRuleChanged"),
        ("PDU2-MIB", "doorAccessRuleDeleted"),
        ("PDU2-MIB", "inletLinePairSensorStateChange"),
        ("PDU2-MIB", "tacPlusError"),
        ("PDU2-MIB", "outletSuspended"),
        ("PDU2-MIB", "inletDipEvent"),
        ("PDU2-MIB", "inletSwellEvent"),
        ("PDU2-MIB", "inletPoleDipEvent"),
        ("PDU2-MIB", "inletPoleSwellEvent"),
        ("PDU2-MIB", "portFuseStateChange"),
        ("PDU2-MIB", "linkUnitAdded"),
        ("PDU2-MIB", "linkUnitReleased"),
        ("PDU2-MIB", "linkUnitCommunicationOk"),
        ("PDU2-MIB", "linkUnitCommunicationFailed"),
        ("PDU2-MIB", "doorMechanicallyUnlocked"),
        ("PDU2-MIB", "doorForcedOpen"),
        ("PDU2-MIB", "outletServiceModeChanged"))
)
if mibBuilder.loadTexts:
    trapsGroup.setStatus(
        "current"
    )

oldTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 2, 16)
)
oldTrapsGroup.setObjects(
      *(("PDU2-MIB", "pduSensorStateChange"),
        ("PDU2-MIB", "rfCodeTagConnected"),
        ("PDU2-MIB", "rfCodeTagDisconnected"),
        ("PDU2-MIB", "lhxSupportChanged"))
)
if mibBuilder.loadTexts:
    oldTrapsGroup.setStatus(
        "deprecated"
    )

obsoleteTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 2, 17)
)
obsoleteTrapsGroup.setObjects(
    ("PDU2-MIB", "wireSensorStateChange")
)
if mibBuilder.loadTexts:
    obsoleteTrapsGroup.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance

complianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 1, 1)
)
complianceRev1.setObjects(
      *(("PDU2-MIB", "ipAddressGroup"),
        ("PDU2-MIB", "oldConfigGroup"),
        ("PDU2-MIB", "oldTrapsGroup"))
)
if mibBuilder.loadTexts:
    complianceRev1.setStatus(
        "deprecated"
    )

complianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13742, 6, 9, 1, 2)
)
complianceRev2.setObjects(
      *(("PDU2-MIB", "configGroup"),
        ("PDU2-MIB", "logGroup"),
        ("PDU2-MIB", "measurementsGroup"),
        ("PDU2-MIB", "controlGroup"),
        ("PDU2-MIB", "trapInformationGroup"),
        ("PDU2-MIB", "trapsGroup"),
        ("PDU2-MIB", "reliabilityGroup"))
)
if mibBuilder.loadTexts:
    complianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDU2-MIB",
    **{"SensorTypeEnumeration": SensorTypeEnumeration,
       "SensorStateEnumeration": SensorStateEnumeration,
       "PlugTypeEnumeration": PlugTypeEnumeration,
       "ReceptacleTypeEnumeration": ReceptacleTypeEnumeration,
       "OverCurrentProtectorTypeEnumeration": OverCurrentProtectorTypeEnumeration,
       "BoardTypeEnumeration": BoardTypeEnumeration,
       "OutletSwitchingOperationsEnumeration": OutletSwitchingOperationsEnumeration,
       "SensorUnitsEnumeration": SensorUnitsEnumeration,
       "DaisychainMemberTypeEnumeration": DaisychainMemberTypeEnumeration,
       "URL": URL,
       "GlobalOutletStateOnStartupEnumeration": GlobalOutletStateOnStartupEnumeration,
       "OutletStateOnStartupEnumeration": OutletStateOnStartupEnumeration,
       "ExternalSensorsZCoordinateUnitsEnumeration": ExternalSensorsZCoordinateUnitsEnumeration,
       "HundredthsOfAPercentage": HundredthsOfAPercentage,
       "DeviceIdentificationParameterEnumeration": DeviceIdentificationParameterEnumeration,
       "TransferSwitchTransferReasonEnumeration": TransferSwitchTransferReasonEnumeration,
       "ProductTypeEnumeration": ProductTypeEnumeration,
       "RelayPowerLossBehaviorEnumeration": RelayPowerLossBehaviorEnumeration,
       "TripCauseOutletHandlingEnumeration": TripCauseOutletHandlingEnumeration,
       "DeviceCascadeTypeEnumeration": DeviceCascadeTypeEnumeration,
       "PeripheralDeviceFirmwareUpdateStateEnumeration": PeripheralDeviceFirmwareUpdateStateEnumeration,
       "PanelLayoutEnumeration": PanelLayoutEnumeration,
       "PanelNumberingEnumeration": PanelNumberingEnumeration,
       "CircuitTypeEnumeration": CircuitTypeEnumeration,
       "PhaseEnumeration": PhaseEnumeration,
       "LineEnumeration": LineEnumeration,
       "PowerMeterTypeEnumeration": PowerMeterTypeEnumeration,
       "NetworkInterfaceTypeEnumeration": NetworkInterfaceTypeEnumeration,
       "AddressSourceEnumeration": AddressSourceEnumeration,
       "HwFailureTypeEnumeration": HwFailureTypeEnumeration,
       "ServerPowerStateEnumeration": ServerPowerStateEnumeration,
       "ServerPowerControlResultEnumeration": ServerPowerControlResultEnumeration,
       "PduOrientationEnumeration": PduOrientationEnumeration,
       "PortFuseStateEnumeration": PortFuseStateEnumeration,
       "raritan": raritan,
       "pdu2": pdu2,
       "traps": traps,
       "trapInformation": trapInformation,
       "trapInformationTable": trapInformationTable,
       "trapInformationEntry": trapInformationEntry,
       "userName": userName,
       "targetUser": targetUser,
       "imageVersion": imageVersion,
       "roleName": roleName,
       "smtpMessageRecipients": smtpMessageRecipients,
       "smtpServer": smtpServer,
       "newTargetUser": newTargetUser,
       "oldSensorState": oldSensorState,
       "pduNumber": pduNumber,
       "inletPoleNumber": inletPoleNumber,
       "outletPoleNumber": outletPoleNumber,
       "externalSensorNumber": externalSensorNumber,
       "typeOfSensor": typeOfSensor,
       "errorDescription": errorDescription,
       "deviceChangedParameter": deviceChangedParameter,
       "changedParameterNewValue": changedParameterNewValue,
       "lhxSupportEnabled": lhxSupportEnabled,
       "webcamModel": webcamModel,
       "webcamConnectionPort": webcamConnectionPort,
       "agentInetPortNumber": agentInetPortNumber,
       "peripheralDeviceRomcode": peripheralDeviceRomcode,
       "peripheralDeviceFirmwareUpdateState": peripheralDeviceFirmwareUpdateState,
       "circuitNumber": circuitNumber,
       "circuitPoleNumber": circuitPoleNumber,
       "phoneNumber": phoneNumber,
       "smartCardReaderId": smartCardReaderId,
       "smartCardTimestamp": smartCardTimestamp,
       "smartCardType": smartCardType,
       "smartCardId": smartCardId,
       "suspectedTripCauseLabel": suspectedTripCauseLabel,
       "smartCardReaderManufacturer": smartCardReaderManufacturer,
       "smartCardReaderProduct": smartCardReaderProduct,
       "smartCardReaderSerialNumber": smartCardReaderSerialNumber,
       "smartCardReaderChannel": smartCardReaderChannel,
       "outletGroupNumber": outletGroupNumber,
       "serverPowerOperation": serverPowerOperation,
       "serverPowerResult": serverPowerResult,
       "webcamName": webcamName,
       "webcamFolderUrl": webcamFolderUrl,
       "keypadId": keypadId,
       "keypadPinTimestamp": keypadPinTimestamp,
       "keypadPin": keypadPin,
       "keypadManufacturer": keypadManufacturer,
       "keypadProduct": keypadProduct,
       "keypadSerialNumber": keypadSerialNumber,
       "keypadChannel": keypadChannel,
       "doorAccessRuleId": doorAccessRuleId,
       "doorAccessDenialReason": doorAccessDenialReason,
       "doorAccessRuleName": doorAccessRuleName,
       "smartCardReaderPosition": smartCardReaderPosition,
       "keypadPosition": keypadPosition,
       "keypadDescription": keypadDescription,
       "keypadName": keypadName,
       "smartCardReaderDescription": smartCardReaderDescription,
       "smartCardReaderName": smartCardReaderName,
       "inletLinePairNumber": inletLinePairNumber,
       "dipSwellEventVoltage": dipSwellEventVoltage,
       "dipSwellEventTimeStamp": dipSwellEventTimeStamp,
       "dipSwellEventDuration": dipSwellEventDuration,
       "portFuseState": portFuseState,
       "externalPortFuseId": externalPortFuseId,
       "externalPortName": externalPortName,
       "linkUnitId": linkUnitId,
       "linkUnitAddress": linkUnitAddress,
       "doorHandleName": doorHandleName,
       "doorLockName": doorLockName,
       "doorStateName": doorStateName,
       "systemStarted": systemStarted,
       "systemReset": systemReset,
       "userLogin": userLogin,
       "userLogout": userLogout,
       "userAuthenticationFailure": userAuthenticationFailure,
       "userSessionTimeout": userSessionTimeout,
       "userAdded": userAdded,
       "userModified": userModified,
       "userDeleted": userDeleted,
       "roleAdded": roleAdded,
       "roleModified": roleModified,
       "roleDeleted": roleDeleted,
       "deviceUpdateStarted": deviceUpdateStarted,
       "deviceUpdateCompleted": deviceUpdateCompleted,
       "userBlocked": userBlocked,
       "powerControl": powerControl,
       "userPasswordChanged": userPasswordChanged,
       "passwordSettingsChanged": passwordSettingsChanged,
       "firmwareValidationFailed": firmwareValidationFailed,
       "logFileCleared": logFileCleared,
       "bulkConfigurationSaved": bulkConfigurationSaved,
       "bulkConfigurationCopied": bulkConfigurationCopied,
       "pduSensorStateChange": pduSensorStateChange,
       "inletSensorStateChange": inletSensorStateChange,
       "inletPoleSensorStateChange": inletPoleSensorStateChange,
       "outletSensorStateChange": outletSensorStateChange,
       "outletPoleSensorStateChange": outletPoleSensorStateChange,
       "overCurrentProtectorSensorStateChange": overCurrentProtectorSensorStateChange,
       "externalSensorStateChange": externalSensorStateChange,
       "smtpMessageTransmissionFailure": smtpMessageTransmissionFailure,
       "ldapError": ldapError,
       "deviceUpdateFailed": deviceUpdateFailed,
       "loadSheddingModeEntered": loadSheddingModeEntered,
       "loadSheddingModeExited": loadSheddingModeExited,
       "pingServerEnabled": pingServerEnabled,
       "pingServerDisabled": pingServerDisabled,
       "serverNotReachable": serverNotReachable,
       "serverReachable": serverReachable,
       "rfCodeTagConnected": rfCodeTagConnected,
       "rfCodeTagDisconnected": rfCodeTagDisconnected,
       "deviceIdentificationChanged": deviceIdentificationChanged,
       "usbExpansionUnitConnected": usbExpansionUnitConnected,
       "usbExpansionUnitDisconnected": usbExpansionUnitDisconnected,
       "lhxSupportChanged": lhxSupportChanged,
       "userAcceptedRestrictedServiceAgreement": userAcceptedRestrictedServiceAgreement,
       "userDeclinedRestrictedServiceAgreement": userDeclinedRestrictedServiceAgreement,
       "wireSensorStateChange": wireSensorStateChange,
       "transferSwitchSensorStateChange": transferSwitchSensorStateChange,
       "deviceSettingsSaved": deviceSettingsSaved,
       "deviceSettingsRestored": deviceSettingsRestored,
       "webcamInserted": webcamInserted,
       "webcamRemoved": webcamRemoved,
       "inletEnabled": inletEnabled,
       "inletDisabled": inletDisabled,
       "serverConnectivityUnrecoverable": serverConnectivityUnrecoverable,
       "radiusError": radiusError,
       "serverReachabilityError": serverReachabilityError,
       "inletSensorReset": inletSensorReset,
       "outletSensorReset": outletSensorReset,
       "unknownPeripheralDeviceAttached": unknownPeripheralDeviceAttached,
       "peripheralDeviceFirmwareUpdate": peripheralDeviceFirmwareUpdate,
       "unitSensorReset": unitSensorReset,
       "unitSensorStateChange": unitSensorStateChange,
       "circuitSensorStateChange": circuitSensorStateChange,
       "circuitPoleSensorStateChange": circuitPoleSensorStateChange,
       "circuitAdded": circuitAdded,
       "circuitDeleted": circuitDeleted,
       "circuitModified": circuitModified,
       "circuitSensorReset": circuitSensorReset,
       "powerMeterAdded": powerMeterAdded,
       "powerMeterDeleted": powerMeterDeleted,
       "powerMeterModified": powerMeterModified,
       "smsMessageTransmissionFailure": smsMessageTransmissionFailure,
       "smartCardInserted": smartCardInserted,
       "smartCardRemoved": smartCardRemoved,
       "rawConfigurationDownloaded": rawConfigurationDownloaded,
       "rawConfigurationUpdated": rawConfigurationUpdated,
       "hwFailureStatusChanged": hwFailureStatusChanged,
       "outletGroupAdded": outletGroupAdded,
       "outletGroupModified": outletGroupModified,
       "outletGroupDeleted": outletGroupDeleted,
       "outletGroupSensorStateChange": outletGroupSensorStateChange,
       "outletGroupSensorReset": outletGroupSensorReset,
       "outletGroupPowerControl": outletGroupPowerControl,
       "serverPowerControlInitiated": serverPowerControlInitiated,
       "serverPowerControlCompleted": serverPowerControlCompleted,
       "webcamStorageUploadStarted": webcamStorageUploadStarted,
       "testEventTriggered": testEventTriggered,
       "actuatorSwitched": actuatorSwitched,
       "keypadPinEntered": keypadPinEntered,
       "doorAccessGranted": doorAccessGranted,
       "doorAccessDenied": doorAccessDenied,
       "doorAccessRuleAdded": doorAccessRuleAdded,
       "doorAccessRuleChanged": doorAccessRuleChanged,
       "doorAccessRuleDeleted": doorAccessRuleDeleted,
       "inletLinePairSensorStateChange": inletLinePairSensorStateChange,
       "tacPlusError": tacPlusError,
       "outletSuspended": outletSuspended,
       "userRenamed": userRenamed,
       "inletDipEvent": inletDipEvent,
       "inletSwellEvent": inletSwellEvent,
       "inletPoleDipEvent": inletPoleDipEvent,
       "inletPoleSwellEvent": inletPoleSwellEvent,
       "portFuseStateChange": portFuseStateChange,
       "linkUnitAdded": linkUnitAdded,
       "linkUnitReleased": linkUnitReleased,
       "linkUnitCommunicationOk": linkUnitCommunicationOk,
       "linkUnitCommunicationFailed": linkUnitCommunicationFailed,
       "doorMechanicallyUnlocked": doorMechanicallyUnlocked,
       "doorForcedOpen": doorForcedOpen,
       "outletServiceModeChanged": outletServiceModeChanged,
       "board": board,
       "environmental": environmental,
       "configuration": configuration,
       "pduCount": pduCount,
       "unit": unit,
       "nameplateTable": nameplateTable,
       "nameplateEntry": nameplateEntry,
       "pduId": pduId,
       "pduManufacturer": pduManufacturer,
       "pduModel": pduModel,
       "pduSerialNumber": pduSerialNumber,
       "pduRatedVoltage": pduRatedVoltage,
       "pduRatedCurrent": pduRatedCurrent,
       "pduRatedFrequency": pduRatedFrequency,
       "pduRatedVA": pduRatedVA,
       "pduImage": pduImage,
       "unitConfigurationTable": unitConfigurationTable,
       "unitConfigurationEntry": unitConfigurationEntry,
       "inletCount": inletCount,
       "overCurrentProtectorCount": overCurrentProtectorCount,
       "outletCount": outletCount,
       "inletControllerCount": inletControllerCount,
       "outletControllerCount": outletControllerCount,
       "externalSensorCount": externalSensorCount,
       "pxIPAddress": pxIPAddress,
       "netmask": netmask,
       "gateway": gateway,
       "pxMACAddress": pxMACAddress,
       "utcOffset": utcOffset,
       "pduName": pduName,
       "networkInterfaceType": networkInterfaceType,
       "externalSensorsZCoordinateUnits": externalSensorsZCoordinateUnits,
       "unitDeviceCapabilities": unitDeviceCapabilities,
       "outletSequencingDelay": outletSequencingDelay,
       "globalOutletPowerCyclingPowerOffPeriod": globalOutletPowerCyclingPowerOffPeriod,
       "globalOutletStateOnStartup": globalOutletStateOnStartup,
       "outletPowerupSequence": outletPowerupSequence,
       "pduPowerCyclingPowerOffPeriod": pduPowerCyclingPowerOffPeriod,
       "pduDaisychainMemberType": pduDaisychainMemberType,
       "managedExternalSensorCount": managedExternalSensorCount,
       "pxInetAddressType": pxInetAddressType,
       "pxInetIPAddress": pxInetIPAddress,
       "pxInetNetmask": pxInetNetmask,
       "pxInetGateway": pxInetGateway,
       "loadShedding": loadShedding,
       "serverCount": serverCount,
       "inrushGuardDelay": inrushGuardDelay,
       "cascadedDeviceConnected": cascadedDeviceConnected,
       "synchronizeWithNTPServer": synchronizeWithNTPServer,
       "useDHCPProvidedNTPServer": useDHCPProvidedNTPServer,
       "firstNTPServerAddressType": firstNTPServerAddressType,
       "firstNTPServerAddress": firstNTPServerAddress,
       "secondNTPServerAddressType": secondNTPServerAddressType,
       "secondNTPServerAddress": secondNTPServerAddress,
       "wireCount": wireCount,
       "transferSwitchCount": transferSwitchCount,
       "productType": productType,
       "meteringControllerCount": meteringControllerCount,
       "relayBehaviorOnPowerLoss": relayBehaviorOnPowerLoss,
       "deviceCascadeType": deviceCascadeType,
       "deviceCascadePosition": deviceCascadePosition,
       "peripheralDevicesAutoManagement": peripheralDevicesAutoManagement,
       "frontPanelOutletSwitching": frontPanelOutletSwitching,
       "frontPanelRCMSelfTest": frontPanelRCMSelfTest,
       "frontPanelActuatorControl": frontPanelActuatorControl,
       "circuitCount": circuitCount,
       "activeDNSServerCount": activeDNSServerCount,
       "activeNTPServerCount": activeNTPServerCount,
       "peripheralDevicePackageCount": peripheralDevicePackageCount,
       "outletGroupCount": outletGroupCount,
       "demandUpdateInterval": demandUpdateInterval,
       "demandAveragingIntervals": demandAveragingIntervals,
       "hasDCInlets": hasDCInlets,
       "pduOrientation": pduOrientation,
       "pduUptime": pduUptime,
       "tripCauseOutletHandling": tripCauseOutletHandling,
       "controllerConfigurationTable": controllerConfigurationTable,
       "controllerConfigurationEntry": controllerConfigurationEntry,
       "boardType": boardType,
       "boardIndex": boardIndex,
       "boardVersion": boardVersion,
       "boardFirmwareVersion": boardFirmwareVersion,
       "boardFirmwareTimeStamp": boardFirmwareTimeStamp,
       "logConfigurationTable": logConfigurationTable,
       "logConfigurationEntry": logConfigurationEntry,
       "dataLogging": dataLogging,
       "measurementPeriod": measurementPeriod,
       "measurementsPerLogEntry": measurementsPerLogEntry,
       "logSize": logSize,
       "dataLoggingEnableForAllSensors": dataLoggingEnableForAllSensors,
       "unitSensorConfigurationTable": unitSensorConfigurationTable,
       "unitSensorConfigurationEntry": unitSensorConfigurationEntry,
       "sensorType": sensorType,
       "unitSensorLogAvailable": unitSensorLogAvailable,
       "unitSensorUnits": unitSensorUnits,
       "unitSensorDecimalDigits": unitSensorDecimalDigits,
       "unitSensorAccuracy": unitSensorAccuracy,
       "unitSensorResolution": unitSensorResolution,
       "unitSensorTolerance": unitSensorTolerance,
       "unitSensorMaximum": unitSensorMaximum,
       "unitSensorMinimum": unitSensorMinimum,
       "unitSensorHysteresis": unitSensorHysteresis,
       "unitSensorStateChangeDelay": unitSensorStateChangeDelay,
       "unitSensorLowerCriticalThreshold": unitSensorLowerCriticalThreshold,
       "unitSensorLowerWarningThreshold": unitSensorLowerWarningThreshold,
       "unitSensorUpperCriticalThreshold": unitSensorUpperCriticalThreshold,
       "unitSensorUpperWarningThreshold": unitSensorUpperWarningThreshold,
       "unitSensorEnabledThresholds": unitSensorEnabledThresholds,
       "unitSensorSignedMaximum": unitSensorSignedMaximum,
       "unitSensorSignedMinimum": unitSensorSignedMinimum,
       "unitSensorSignedLowerCriticalThreshold": unitSensorSignedLowerCriticalThreshold,
       "unitSensorSignedLowerWarningThreshold": unitSensorSignedLowerWarningThreshold,
       "unitSensorSignedUpperCriticalThreshold": unitSensorSignedUpperCriticalThreshold,
       "unitSensorSignedUpperWarningThreshold": unitSensorSignedUpperWarningThreshold,
       "activeDNSServerTable": activeDNSServerTable,
       "activeDNSServerEntry": activeDNSServerEntry,
       "activeDNSServerIndex": activeDNSServerIndex,
       "activeDNSServerAddressType": activeDNSServerAddressType,
       "activeDNSServerAddress": activeDNSServerAddress,
       "activeDNSServerAddressSource": activeDNSServerAddressSource,
       "activeNTPServerTable": activeNTPServerTable,
       "activeNTPServerEntry": activeNTPServerEntry,
       "activeNTPServerIndex": activeNTPServerIndex,
       "activeNTPServerAddressType": activeNTPServerAddressType,
       "activeNTPServerAddress": activeNTPServerAddress,
       "activeNTPServerAddressSource": activeNTPServerAddressSource,
       "inlets": inlets,
       "inletConfigurationTable": inletConfigurationTable,
       "inletConfigurationEntry": inletConfigurationEntry,
       "inletId": inletId,
       "inletLabel": inletLabel,
       "inletName": inletName,
       "inletPlug": inletPlug,
       "inletPoleCount": inletPoleCount,
       "inletRatedVoltage": inletRatedVoltage,
       "inletRatedCurrent": inletRatedCurrent,
       "inletRatedFrequency": inletRatedFrequency,
       "inletRatedVA": inletRatedVA,
       "inletDeviceCapabilities": inletDeviceCapabilities,
       "inletPoleCapabilities": inletPoleCapabilities,
       "inletPlugDescriptor": inletPlugDescriptor,
       "inletEnableState": inletEnableState,
       "inletRCMResidualOperatingCurrent": inletRCMResidualOperatingCurrent,
       "inletIsDC": inletIsDC,
       "inletLinePairCount": inletLinePairCount,
       "inletLinePairCapabilities": inletLinePairCapabilities,
       "inletSensorConfigurationTable": inletSensorConfigurationTable,
       "inletSensorConfigurationEntry": inletSensorConfigurationEntry,
       "inletSensorLogAvailable": inletSensorLogAvailable,
       "inletSensorUnits": inletSensorUnits,
       "inletSensorDecimalDigits": inletSensorDecimalDigits,
       "inletSensorAccuracy": inletSensorAccuracy,
       "inletSensorResolution": inletSensorResolution,
       "inletSensorTolerance": inletSensorTolerance,
       "inletSensorMaximum": inletSensorMaximum,
       "inletSensorMinimum": inletSensorMinimum,
       "inletSensorHysteresis": inletSensorHysteresis,
       "inletSensorStateChangeDelay": inletSensorStateChangeDelay,
       "inletSensorLowerCriticalThreshold": inletSensorLowerCriticalThreshold,
       "inletSensorLowerWarningThreshold": inletSensorLowerWarningThreshold,
       "inletSensorUpperCriticalThreshold": inletSensorUpperCriticalThreshold,
       "inletSensorUpperWarningThreshold": inletSensorUpperWarningThreshold,
       "inletSensorEnabledThresholds": inletSensorEnabledThresholds,
       "inletSensorSignedMaximum": inletSensorSignedMaximum,
       "inletSensorSignedMinimum": inletSensorSignedMinimum,
       "inletSensorSignedLowerCriticalThreshold": inletSensorSignedLowerCriticalThreshold,
       "inletSensorSignedLowerWarningThreshold": inletSensorSignedLowerWarningThreshold,
       "inletSensorSignedUpperCriticalThreshold": inletSensorSignedUpperCriticalThreshold,
       "inletSensorSignedUpperWarningThreshold": inletSensorSignedUpperWarningThreshold,
       "inletPoleConfigurationTable": inletPoleConfigurationTable,
       "inletPoleConfigurationEntry": inletPoleConfigurationEntry,
       "inletPoleLine": inletPoleLine,
       "inletPoleNode": inletPoleNode,
       "inletPoleSensorConfigurationTable": inletPoleSensorConfigurationTable,
       "inletPoleSensorConfigurationEntry": inletPoleSensorConfigurationEntry,
       "inletPoleIndex": inletPoleIndex,
       "inletPoleSensorLogAvailable": inletPoleSensorLogAvailable,
       "inletPoleSensorUnits": inletPoleSensorUnits,
       "inletPoleSensorDecimalDigits": inletPoleSensorDecimalDigits,
       "inletPoleSensorAccuracy": inletPoleSensorAccuracy,
       "inletPoleSensorResolution": inletPoleSensorResolution,
       "inletPoleSensorTolerance": inletPoleSensorTolerance,
       "inletPoleSensorMaximum": inletPoleSensorMaximum,
       "inletPoleSensorMinimum": inletPoleSensorMinimum,
       "inletPoleSensorHysteresis": inletPoleSensorHysteresis,
       "inletPoleSensorStateChangeDelay": inletPoleSensorStateChangeDelay,
       "inletPoleSensorLowerCriticalThreshold": inletPoleSensorLowerCriticalThreshold,
       "inletPoleSensorLowerWarningThreshold": inletPoleSensorLowerWarningThreshold,
       "inletPoleSensorUpperCriticalThreshold": inletPoleSensorUpperCriticalThreshold,
       "inletPoleSensorUpperWarningThreshold": inletPoleSensorUpperWarningThreshold,
       "inletPoleSensorEnabledThresholds": inletPoleSensorEnabledThresholds,
       "inletPoleSensorSignedMaximum": inletPoleSensorSignedMaximum,
       "inletPoleSensorSignedMinimum": inletPoleSensorSignedMinimum,
       "inletPoleSensorSignedLowerCriticalThreshold": inletPoleSensorSignedLowerCriticalThreshold,
       "inletPoleSensorSignedLowerWarningThreshold": inletPoleSensorSignedLowerWarningThreshold,
       "inletPoleSensorSignedUpperCriticalThreshold": inletPoleSensorSignedUpperCriticalThreshold,
       "inletPoleSensorSignedUpperWarningThreshold": inletPoleSensorSignedUpperWarningThreshold,
       "inletLinePairConfigurationTable": inletLinePairConfigurationTable,
       "inletLinePairConfigurationEntry": inletLinePairConfigurationEntry,
       "inletLinePairIndex": inletLinePairIndex,
       "inletLinePairLeftLine": inletLinePairLeftLine,
       "inletLinePairRightLine": inletLinePairRightLine,
       "inletLinePairLeftNode": inletLinePairLeftNode,
       "inletLinePairRightNode": inletLinePairRightNode,
       "inletLinePairSensorConfigurationTable": inletLinePairSensorConfigurationTable,
       "inletLinePairSensorConfigurationEntry": inletLinePairSensorConfigurationEntry,
       "inletLinePairSensorLogAvailable": inletLinePairSensorLogAvailable,
       "inletLinePairSensorUnits": inletLinePairSensorUnits,
       "inletLinePairSensorDecimalDigits": inletLinePairSensorDecimalDigits,
       "inletLinePairSensorResolution": inletLinePairSensorResolution,
       "inletLinePairSensorMaximum": inletLinePairSensorMaximum,
       "inletLinePairSensorMinimum": inletLinePairSensorMinimum,
       "inletLinePairSensorHysteresis": inletLinePairSensorHysteresis,
       "inletLinePairSensorStateChangeDelay": inletLinePairSensorStateChangeDelay,
       "inletLinePairSensorLowerCriticalThreshold": inletLinePairSensorLowerCriticalThreshold,
       "inletLinePairSensorLowerWarningThreshold": inletLinePairSensorLowerWarningThreshold,
       "inletLinePairSensorUpperCriticalThreshold": inletLinePairSensorUpperCriticalThreshold,
       "inletLinePairSensorUpperWarningThreshold": inletLinePairSensorUpperWarningThreshold,
       "inletLinePairSensorEnabledThresholds": inletLinePairSensorEnabledThresholds,
       "inletLinePairSensorSignedMaximum": inletLinePairSensorSignedMaximum,
       "inletLinePairSensorSignedMinimum": inletLinePairSensorSignedMinimum,
       "inletLinePairSensorSignedLowerCriticalThreshold": inletLinePairSensorSignedLowerCriticalThreshold,
       "inletLinePairSensorSignedLowerWarningThreshold": inletLinePairSensorSignedLowerWarningThreshold,
       "inletLinePairSensorSignedUpperCriticalThreshold": inletLinePairSensorSignedUpperCriticalThreshold,
       "inletLinePairSensorSignedUpperWarningThreshold": inletLinePairSensorSignedUpperWarningThreshold,
       "overCurrentProtector": overCurrentProtector,
       "overCurrentProtectorConfigurationTable": overCurrentProtectorConfigurationTable,
       "overCurrentProtectorConfigurationEntry": overCurrentProtectorConfigurationEntry,
       "overCurrentProtectorIndex": overCurrentProtectorIndex,
       "overCurrentProtectorLabel": overCurrentProtectorLabel,
       "overCurrentProtectorName": overCurrentProtectorName,
       "overCurrentProtectorType": overCurrentProtectorType,
       "overCurrentProtectorRatedCurrent": overCurrentProtectorRatedCurrent,
       "overCurrentProtectorPoleCount": overCurrentProtectorPoleCount,
       "overCurrentProtectorCapabilities": overCurrentProtectorCapabilities,
       "overCurrentProtectorPowerSource": overCurrentProtectorPowerSource,
       "overCurrentProtectorSensorConfigurationTable": overCurrentProtectorSensorConfigurationTable,
       "overCurrentProtectorSensorConfigurationEntry": overCurrentProtectorSensorConfigurationEntry,
       "overCurrentProtectorSensorLogAvailable": overCurrentProtectorSensorLogAvailable,
       "overCurrentProtectorSensorUnits": overCurrentProtectorSensorUnits,
       "overCurrentProtectorSensorDecimalDigits": overCurrentProtectorSensorDecimalDigits,
       "overCurrentProtectorSensorAccuracy": overCurrentProtectorSensorAccuracy,
       "overCurrentProtectorSensorResolution": overCurrentProtectorSensorResolution,
       "overCurrentProtectorSensorTolerance": overCurrentProtectorSensorTolerance,
       "overCurrentProtectorSensorMaximum": overCurrentProtectorSensorMaximum,
       "overCurrentProtectorSensorMinimum": overCurrentProtectorSensorMinimum,
       "overCurrentProtectorSensorHysteresis": overCurrentProtectorSensorHysteresis,
       "overCurrentProtectorSensorStateChangeDelay": overCurrentProtectorSensorStateChangeDelay,
       "overCurrentProtectorSensorLowerCriticalThreshold": overCurrentProtectorSensorLowerCriticalThreshold,
       "overCurrentProtectorSensorLowerWarningThreshold": overCurrentProtectorSensorLowerWarningThreshold,
       "overCurrentProtectorSensorUpperCriticalThreshold": overCurrentProtectorSensorUpperCriticalThreshold,
       "overCurrentProtectorSensorUpperWarningThreshold": overCurrentProtectorSensorUpperWarningThreshold,
       "overCurrentProtectorSensorEnabledThresholds": overCurrentProtectorSensorEnabledThresholds,
       "overCurrentProtectorSensorSignedMaximum": overCurrentProtectorSensorSignedMaximum,
       "overCurrentProtectorSensorSignedMinimum": overCurrentProtectorSensorSignedMinimum,
       "overCurrentProtectorSensorSignedLowerCriticalThreshold": overCurrentProtectorSensorSignedLowerCriticalThreshold,
       "overCurrentProtectorSensorSignedLowerWarningThreshold": overCurrentProtectorSensorSignedLowerWarningThreshold,
       "overCurrentProtectorSensorSignedUpperCriticalThreshold": overCurrentProtectorSensorSignedUpperCriticalThreshold,
       "overCurrentProtectorSensorSignedUpperWarningThreshold": overCurrentProtectorSensorSignedUpperWarningThreshold,
       "overCurrentProtectorPoleConfigurationTable": overCurrentProtectorPoleConfigurationTable,
       "overCurrentProtectorPoleConfigurationEntry": overCurrentProtectorPoleConfigurationEntry,
       "overCurrentProtectorPoleIndex": overCurrentProtectorPoleIndex,
       "overCurrentProtectorPoleLine": overCurrentProtectorPoleLine,
       "overCurrentProtectorPoleInNode": overCurrentProtectorPoleInNode,
       "overCurrentProtectorPoleOutNode": overCurrentProtectorPoleOutNode,
       "outlets": outlets,
       "outletConfigurationTable": outletConfigurationTable,
       "outletConfigurationEntry": outletConfigurationEntry,
       "outletId": outletId,
       "outletLabel": outletLabel,
       "outletName": outletName,
       "outletReceptacle": outletReceptacle,
       "outletPoleCount": outletPoleCount,
       "outletRatedVoltage": outletRatedVoltage,
       "outletRatedCurrent": outletRatedCurrent,
       "outletRatedVA": outletRatedVA,
       "outletDeviceCapabilities": outletDeviceCapabilities,
       "outletPoleCapabilities": outletPoleCapabilities,
       "outletPowerCyclingPowerOffPeriod": outletPowerCyclingPowerOffPeriod,
       "outletStateOnStartup": outletStateOnStartup,
       "outletUseGlobalPowerCyclingPowerOffPeriod": outletUseGlobalPowerCyclingPowerOffPeriod,
       "outletSwitchable": outletSwitchable,
       "outletReceptacleDescriptor": outletReceptacleDescriptor,
       "outletNonCritical": outletNonCritical,
       "outletSequenceDelay": outletSequenceDelay,
       "outletPowerSource": outletPowerSource,
       "outletServiceMode": outletServiceMode,
       "outletSensorConfigurationTable": outletSensorConfigurationTable,
       "outletSensorConfigurationEntry": outletSensorConfigurationEntry,
       "outletSensorLogAvailable": outletSensorLogAvailable,
       "outletSensorUnits": outletSensorUnits,
       "outletSensorDecimalDigits": outletSensorDecimalDigits,
       "outletSensorAccuracy": outletSensorAccuracy,
       "outletSensorResolution": outletSensorResolution,
       "outletSensorTolerance": outletSensorTolerance,
       "outletSensorMaximum": outletSensorMaximum,
       "outletSensorMinimum": outletSensorMinimum,
       "outletSensorHysteresis": outletSensorHysteresis,
       "outletSensorStateChangeDelay": outletSensorStateChangeDelay,
       "outletSensorLowerCriticalThreshold": outletSensorLowerCriticalThreshold,
       "outletSensorLowerWarningThreshold": outletSensorLowerWarningThreshold,
       "outletSensorUpperCriticalThreshold": outletSensorUpperCriticalThreshold,
       "outletSensorUpperWarningThreshold": outletSensorUpperWarningThreshold,
       "outletSensorEnabledThresholds": outletSensorEnabledThresholds,
       "outletSensorSignedMaximum": outletSensorSignedMaximum,
       "outletSensorSignedMinimum": outletSensorSignedMinimum,
       "outletSensorSignedLowerCriticalThreshold": outletSensorSignedLowerCriticalThreshold,
       "outletSensorSignedLowerWarningThreshold": outletSensorSignedLowerWarningThreshold,
       "outletSensorSignedUpperCriticalThreshold": outletSensorSignedUpperCriticalThreshold,
       "outletSensorSignedUpperWarningThreshold": outletSensorSignedUpperWarningThreshold,
       "outletPoleConfigurationTable": outletPoleConfigurationTable,
       "outletPoleConfigurationEntry": outletPoleConfigurationEntry,
       "outletPoleLine": outletPoleLine,
       "outletPoleNode": outletPoleNode,
       "outletPoleSensorConfigurationTable": outletPoleSensorConfigurationTable,
       "outletPoleSensorConfigurationEntry": outletPoleSensorConfigurationEntry,
       "outletPoleIndex": outletPoleIndex,
       "outletPoleSensorLogAvailable": outletPoleSensorLogAvailable,
       "outletPoleSensorUnits": outletPoleSensorUnits,
       "outletPoleSensorDecimalDigits": outletPoleSensorDecimalDigits,
       "outletPoleSensorAccuracy": outletPoleSensorAccuracy,
       "outletPoleSensorResolution": outletPoleSensorResolution,
       "outletPoleSensorTolerance": outletPoleSensorTolerance,
       "outletPoleSensorMaximum": outletPoleSensorMaximum,
       "outletPoleSensorMinimum": outletPoleSensorMinimum,
       "outletPoleSensorHysteresis": outletPoleSensorHysteresis,
       "outletPoleSensorStateChangeDelay": outletPoleSensorStateChangeDelay,
       "outletPoleSensorLowerCriticalThreshold": outletPoleSensorLowerCriticalThreshold,
       "outletPoleSensorLowerWarningThreshold": outletPoleSensorLowerWarningThreshold,
       "outletPoleSensorUpperCriticalThreshold": outletPoleSensorUpperCriticalThreshold,
       "outletPoleSensorUpperWarningThreshold": outletPoleSensorUpperWarningThreshold,
       "outletPoleSensorEnabledThresholds": outletPoleSensorEnabledThresholds,
       "outletPoleSensorSignedMaximum": outletPoleSensorSignedMaximum,
       "outletPoleSensorSignedMinimum": outletPoleSensorSignedMinimum,
       "outletPoleSensorSignedLowerCriticalThreshold": outletPoleSensorSignedLowerCriticalThreshold,
       "outletPoleSensorSignedLowerWarningThreshold": outletPoleSensorSignedLowerWarningThreshold,
       "outletPoleSensorSignedUpperCriticalThreshold": outletPoleSensorSignedUpperCriticalThreshold,
       "outletPoleSensorSignedUpperWarningThreshold": outletPoleSensorSignedUpperWarningThreshold,
       "externalSensors": externalSensors,
       "externalSensorConfigurationTable": externalSensorConfigurationTable,
       "externalSensorConfigurationEntry": externalSensorConfigurationEntry,
       "sensorID": sensorID,
       "externalSensorType": externalSensorType,
       "externalSensorSerialNumber": externalSensorSerialNumber,
       "externalSensorName": externalSensorName,
       "externalSensorDescription": externalSensorDescription,
       "externalSensorXCoordinate": externalSensorXCoordinate,
       "externalSensorYCoordinate": externalSensorYCoordinate,
       "externalSensorZCoordinate": externalSensorZCoordinate,
       "externalSensorChannelNumber": externalSensorChannelNumber,
       "externalOnOffSensorSubtype": externalOnOffSensorSubtype,
       "externalSensorLogAvailable": externalSensorLogAvailable,
       "externalSensorUnits": externalSensorUnits,
       "externalSensorDecimalDigits": externalSensorDecimalDigits,
       "externalSensorAccuracy": externalSensorAccuracy,
       "externalSensorResolution": externalSensorResolution,
       "externalSensorTolerance": externalSensorTolerance,
       "externalSensorMaximum": externalSensorMaximum,
       "externalSensorMinimum": externalSensorMinimum,
       "externalSensorHysteresis": externalSensorHysteresis,
       "externalSensorStateChangeDelay": externalSensorStateChangeDelay,
       "externalSensorLowerCriticalThreshold": externalSensorLowerCriticalThreshold,
       "externalSensorLowerWarningThreshold": externalSensorLowerWarningThreshold,
       "externalSensorUpperCriticalThreshold": externalSensorUpperCriticalThreshold,
       "externalSensorUpperWarningThreshold": externalSensorUpperWarningThreshold,
       "externalSensorEnabledThresholds": externalSensorEnabledThresholds,
       "externalSensorIsActuator": externalSensorIsActuator,
       "externalSensorPosition": externalSensorPosition,
       "externalSensorUseDefaultThresholds": externalSensorUseDefaultThresholds,
       "externalSensorAlarmedToNormalDelay": externalSensorAlarmedToNormalDelay,
       "externalSensorTypeDefaultThresholdsTable": externalSensorTypeDefaultThresholdsTable,
       "externalSensorTypeDefaultThresholdsEntry": externalSensorTypeDefaultThresholdsEntry,
       "externalSensorTypeDefaultHysteresis": externalSensorTypeDefaultHysteresis,
       "externalSensorTypeDefaultStateChangeDelay": externalSensorTypeDefaultStateChangeDelay,
       "externalSensorTypeDefaultLowerCriticalThreshold": externalSensorTypeDefaultLowerCriticalThreshold,
       "externalSensorTypeDefaultLowerWarningThreshold": externalSensorTypeDefaultLowerWarningThreshold,
       "externalSensorTypeDefaultUpperCriticalThreshold": externalSensorTypeDefaultUpperCriticalThreshold,
       "externalSensorTypeDefaultUpperWarningThreshold": externalSensorTypeDefaultUpperWarningThreshold,
       "externalSensorTypeDefaultEnabledThresholds": externalSensorTypeDefaultEnabledThresholds,
       "externalSensorTypeDefaultUnit": externalSensorTypeDefaultUnit,
       "externalSensorTypeDefaultDecimalDigits": externalSensorTypeDefaultDecimalDigits,
       "externalSensorTypeDefaultMaximum": externalSensorTypeDefaultMaximum,
       "externalSensorTypeDefaultMinimum": externalSensorTypeDefaultMinimum,
       "peripheralDevicePackageTable": peripheralDevicePackageTable,
       "peripheralDevicePackageEntry": peripheralDevicePackageEntry,
       "peripheralDevicePackageId": peripheralDevicePackageId,
       "peripheralDevicePackageSerialNumber": peripheralDevicePackageSerialNumber,
       "peripheralDevicePackageModel": peripheralDevicePackageModel,
       "peripheralDevicePackageFirmwareVersion": peripheralDevicePackageFirmwareVersion,
       "peripheralDevicePackageMinFirmwareVersion": peripheralDevicePackageMinFirmwareVersion,
       "peripheralDevicePackageFirmwareTimeStamp": peripheralDevicePackageFirmwareTimeStamp,
       "peripheralDevicePackagePosition": peripheralDevicePackagePosition,
       "peripheralDevicePackageState": peripheralDevicePackageState,
       "serverReachability": serverReachability,
       "serverReachabilityTable": serverReachabilityTable,
       "serverReachabilityEntry": serverReachabilityEntry,
       "serverID": serverID,
       "serverIPAddress": serverIPAddress,
       "serverPingEnabled": serverPingEnabled,
       "wires": wires,
       "wireConfigurationTable": wireConfigurationTable,
       "wireConfigurationEntry": wireConfigurationEntry,
       "wireId": wireId,
       "wireLabel": wireLabel,
       "wireCapabilities": wireCapabilities,
       "wirePowerSource": wirePowerSource,
       "wireSensorConfigurationTable": wireSensorConfigurationTable,
       "wireSensorConfigurationEntry": wireSensorConfigurationEntry,
       "wireSensorLogAvailable": wireSensorLogAvailable,
       "wireSensorUnits": wireSensorUnits,
       "wireSensorDecimalDigits": wireSensorDecimalDigits,
       "wireSensorAccuracy": wireSensorAccuracy,
       "wireSensorResolution": wireSensorResolution,
       "wireSensorTolerance": wireSensorTolerance,
       "wireSensorMaximum": wireSensorMaximum,
       "wireSensorMinimum": wireSensorMinimum,
       "wireSensorHysteresis": wireSensorHysteresis,
       "wireSensorStateChangeDelay": wireSensorStateChangeDelay,
       "wireSensorLowerCriticalThreshold": wireSensorLowerCriticalThreshold,
       "wireSensorLowerWarningThreshold": wireSensorLowerWarningThreshold,
       "wireSensorUpperCriticalThreshold": wireSensorUpperCriticalThreshold,
       "wireSensorUpperWarningThreshold": wireSensorUpperWarningThreshold,
       "wireSensorEnabledThresholds": wireSensorEnabledThresholds,
       "transferSwitch": transferSwitch,
       "transferSwitchConfigurationTable": transferSwitchConfigurationTable,
       "transferSwitchConfigurationEntry": transferSwitchConfigurationEntry,
       "transferSwitchId": transferSwitchId,
       "transferSwitchLabel": transferSwitchLabel,
       "transferSwitchName": transferSwitchName,
       "transferSwitchPreferredInlet": transferSwitchPreferredInlet,
       "transferSwitchPoleCount": transferSwitchPoleCount,
       "transferSwitchAutoReTransferEnabled": transferSwitchAutoReTransferEnabled,
       "transferSwitchAutoReTransferWaitTime": transferSwitchAutoReTransferWaitTime,
       "transferSwitchAutoReTransferRequiresPhaseSync": transferSwitchAutoReTransferRequiresPhaseSync,
       "transferSwitchFrontPanelManualTransferButtonEnabled": transferSwitchFrontPanelManualTransferButtonEnabled,
       "transferSwitchCapabilities": transferSwitchCapabilities,
       "transferSwitchPowerSource1": transferSwitchPowerSource1,
       "transferSwitchPowerSource2": transferSwitchPowerSource2,
       "transferSwitchSensorConfigurationTable": transferSwitchSensorConfigurationTable,
       "transferSwitchSensorConfigurationEntry": transferSwitchSensorConfigurationEntry,
       "transferSwitchSensorLogAvailable": transferSwitchSensorLogAvailable,
       "transferSwitchSensorUnits": transferSwitchSensorUnits,
       "transferSwitchSensorDecimalDigits": transferSwitchSensorDecimalDigits,
       "transferSwitchSensorAccuracy": transferSwitchSensorAccuracy,
       "transferSwitchSensorResolution": transferSwitchSensorResolution,
       "transferSwitchSensorTolerance": transferSwitchSensorTolerance,
       "transferSwitchSensorMaximum": transferSwitchSensorMaximum,
       "transferSwitchSensorMinimum": transferSwitchSensorMinimum,
       "transferSwitchSensorHysteresis": transferSwitchSensorHysteresis,
       "transferSwitchSensorStateChangeDelay": transferSwitchSensorStateChangeDelay,
       "transferSwitchSensorLowerCriticalThreshold": transferSwitchSensorLowerCriticalThreshold,
       "transferSwitchSensorLowerWarningThreshold": transferSwitchSensorLowerWarningThreshold,
       "transferSwitchSensorUpperCriticalThreshold": transferSwitchSensorUpperCriticalThreshold,
       "transferSwitchSensorUpperWarningThreshold": transferSwitchSensorUpperWarningThreshold,
       "transferSwitchSensorEnabledThresholds": transferSwitchSensorEnabledThresholds,
       "transferSwitchSensorSignedMaximum": transferSwitchSensorSignedMaximum,
       "transferSwitchSensorSignedMinimum": transferSwitchSensorSignedMinimum,
       "transferSwitchSensorSignedLowerCriticalThreshold": transferSwitchSensorSignedLowerCriticalThreshold,
       "transferSwitchSensorSignedLowerWarningThreshold": transferSwitchSensorSignedLowerWarningThreshold,
       "transferSwitchSensorSignedUpperCriticalThreshold": transferSwitchSensorSignedUpperCriticalThreshold,
       "transferSwitchSensorSignedUpperWarningThreshold": transferSwitchSensorSignedUpperWarningThreshold,
       "transferSwitchPoleConfigurationTable": transferSwitchPoleConfigurationTable,
       "transferSwitchPoleConfigurationEntry": transferSwitchPoleConfigurationEntry,
       "transferSwitchPoleIndex": transferSwitchPoleIndex,
       "transferSwitchPoleLine": transferSwitchPoleLine,
       "transferSwitchPoleIn1Node": transferSwitchPoleIn1Node,
       "transferSwitchPoleIn2Node": transferSwitchPoleIn2Node,
       "transferSwitchPoleOutNode": transferSwitchPoleOutNode,
       "powerMeter": powerMeter,
       "powerMeterConfigurationTable": powerMeterConfigurationTable,
       "powerMeterConfigurationEntry": powerMeterConfigurationEntry,
       "powerMeterPhaseCTRating": powerMeterPhaseCTRating,
       "powerMeterNeutralCTRating": powerMeterNeutralCTRating,
       "powerMeterEarthCTRating": powerMeterEarthCTRating,
       "powerMeterBranchCount": powerMeterBranchCount,
       "powerMeterPanelPositions": powerMeterPanelPositions,
       "powerMeterPanelLayout": powerMeterPanelLayout,
       "powerMeterPanelNumbering": powerMeterPanelNumbering,
       "powerMeterType": powerMeterType,
       "circuit": circuit,
       "circuitConfigurationTable": circuitConfigurationTable,
       "circuitConfigurationEntry": circuitConfigurationEntry,
       "circuitId": circuitId,
       "circuitPoleCount": circuitPoleCount,
       "circuitName": circuitName,
       "circuitType": circuitType,
       "circuitRatedCurrent": circuitRatedCurrent,
       "circuitCTRating": circuitCTRating,
       "circuitCapabilities": circuitCapabilities,
       "circuitPoleCapabilities": circuitPoleCapabilities,
       "circuitPowerSource": circuitPowerSource,
       "circuitPoleConfigurationTable": circuitPoleConfigurationTable,
       "circuitPoleConfigurationEntry": circuitPoleConfigurationEntry,
       "circuitPoleId": circuitPoleId,
       "circuitPolePanelPosition": circuitPolePanelPosition,
       "circuitPoleCTNumber": circuitPoleCTNumber,
       "circuitPolePhase": circuitPolePhase,
       "circuitSensorConfigurationTable": circuitSensorConfigurationTable,
       "circuitSensorConfigurationEntry": circuitSensorConfigurationEntry,
       "circuitSensorLogAvailable": circuitSensorLogAvailable,
       "circuitSensorUnits": circuitSensorUnits,
       "circuitSensorDecimalDigits": circuitSensorDecimalDigits,
       "circuitSensorResolution": circuitSensorResolution,
       "circuitSensorMaximum": circuitSensorMaximum,
       "circuitSensorMinimum": circuitSensorMinimum,
       "circuitSensorHysteresis": circuitSensorHysteresis,
       "circuitSensorStateChangeDelay": circuitSensorStateChangeDelay,
       "circuitSensorLowerCriticalThreshold": circuitSensorLowerCriticalThreshold,
       "circuitSensorLowerWarningThreshold": circuitSensorLowerWarningThreshold,
       "circuitSensorUpperCriticalThreshold": circuitSensorUpperCriticalThreshold,
       "circuitSensorUpperWarningThreshold": circuitSensorUpperWarningThreshold,
       "circuitSensorEnabledThresholds": circuitSensorEnabledThresholds,
       "circuitSensorSignedMaximum": circuitSensorSignedMaximum,
       "circuitSensorSignedMinimum": circuitSensorSignedMinimum,
       "circuitSensorSignedLowerCriticalThreshold": circuitSensorSignedLowerCriticalThreshold,
       "circuitSensorSignedLowerWarningThreshold": circuitSensorSignedLowerWarningThreshold,
       "circuitSensorSignedUpperCriticalThreshold": circuitSensorSignedUpperCriticalThreshold,
       "circuitSensorSignedUpperWarningThreshold": circuitSensorSignedUpperWarningThreshold,
       "circuitPoleSensorConfigurationTable": circuitPoleSensorConfigurationTable,
       "circuitPoleSensorConfigurationEntry": circuitPoleSensorConfigurationEntry,
       "circuitPoleSensorLogAvailable": circuitPoleSensorLogAvailable,
       "circuitPoleSensorUnits": circuitPoleSensorUnits,
       "circuitPoleSensorDecimalDigits": circuitPoleSensorDecimalDigits,
       "circuitPoleSensorResolution": circuitPoleSensorResolution,
       "circuitPoleSensorMaximum": circuitPoleSensorMaximum,
       "circuitPoleSensorMinimum": circuitPoleSensorMinimum,
       "circuitPoleSensorHysteresis": circuitPoleSensorHysteresis,
       "circuitPoleSensorStateChangeDelay": circuitPoleSensorStateChangeDelay,
       "circuitPoleSensorLowerCriticalThreshold": circuitPoleSensorLowerCriticalThreshold,
       "circuitPoleSensorLowerWarningThreshold": circuitPoleSensorLowerWarningThreshold,
       "circuitPoleSensorUpperCriticalThreshold": circuitPoleSensorUpperCriticalThreshold,
       "circuitPoleSensorUpperWarningThreshold": circuitPoleSensorUpperWarningThreshold,
       "circuitPoleSensorEnabledThresholds": circuitPoleSensorEnabledThresholds,
       "circuitPoleSensorSignedMaximum": circuitPoleSensorSignedMaximum,
       "circuitPoleSensorSignedMinimum": circuitPoleSensorSignedMinimum,
       "circuitPoleSensorSignedLowerCriticalThreshold": circuitPoleSensorSignedLowerCriticalThreshold,
       "circuitPoleSensorSignedLowerWarningThreshold": circuitPoleSensorSignedLowerWarningThreshold,
       "circuitPoleSensorSignedUpperCriticalThreshold": circuitPoleSensorSignedUpperCriticalThreshold,
       "circuitPoleSensorSignedUpperWarningThreshold": circuitPoleSensorSignedUpperWarningThreshold,
       "outletGroups": outletGroups,
       "outletGroupConfigurationTable": outletGroupConfigurationTable,
       "outletGroupConfigurationEntry": outletGroupConfigurationEntry,
       "outletGroupId": outletGroupId,
       "outletGroupName": outletGroupName,
       "outletGroupCapabilities": outletGroupCapabilities,
       "outletGroupMembers": outletGroupMembers,
       "outletGroupSensorConfigurationTable": outletGroupSensorConfigurationTable,
       "outletGroupSensorConfigurationEntry": outletGroupSensorConfigurationEntry,
       "outletGroupSensorLogAvailable": outletGroupSensorLogAvailable,
       "outletGroupSensorUnits": outletGroupSensorUnits,
       "outletGroupSensorDecimalDigits": outletGroupSensorDecimalDigits,
       "outletGroupSensorResolution": outletGroupSensorResolution,
       "outletGroupSensorMaximum": outletGroupSensorMaximum,
       "outletGroupSensorMinimum": outletGroupSensorMinimum,
       "outletGroupSensorHysteresis": outletGroupSensorHysteresis,
       "outletGroupSensorStateChangeDelay": outletGroupSensorStateChangeDelay,
       "outletGroupSensorLowerCriticalThreshold": outletGroupSensorLowerCriticalThreshold,
       "outletGroupSensorLowerWarningThreshold": outletGroupSensorLowerWarningThreshold,
       "outletGroupSensorUpperCriticalThreshold": outletGroupSensorUpperCriticalThreshold,
       "outletGroupSensorUpperWarningThreshold": outletGroupSensorUpperWarningThreshold,
       "outletGroupSensorEnabledThresholds": outletGroupSensorEnabledThresholds,
       "outletGroupSensorSignedMaximum": outletGroupSensorSignedMaximum,
       "outletGroupSensorSignedMinimum": outletGroupSensorSignedMinimum,
       "outletGroupSensorSignedLowerCriticalThreshold": outletGroupSensorSignedLowerCriticalThreshold,
       "outletGroupSensorSignedLowerWarningThreshold": outletGroupSensorSignedLowerWarningThreshold,
       "outletGroupSensorSignedUpperCriticalThreshold": outletGroupSensorSignedUpperCriticalThreshold,
       "outletGroupSensorSignedUpperWarningThreshold": outletGroupSensorSignedUpperWarningThreshold,
       "control": control,
       "outletControl": outletControl,
       "outletSwitchControlTable": outletSwitchControlTable,
       "outletSwitchControlEntry": outletSwitchControlEntry,
       "switchingOperation": switchingOperation,
       "outletSwitchingState": outletSwitchingState,
       "outletSwitchingTimeStamp": outletSwitchingTimeStamp,
       "outletSuspendedState": outletSuspendedState,
       "externalSensorControl": externalSensorControl,
       "externalSensorControlTable": externalSensorControlTable,
       "externalSensorControlEntry": externalSensorControlEntry,
       "externalSensorResetMinMax": externalSensorResetMinMax,
       "transferSwitchControl": transferSwitchControl,
       "transferSwitchControlTable": transferSwitchControlTable,
       "transferSwitchControlEntry": transferSwitchControlEntry,
       "transferSwitchActiveInlet": transferSwitchActiveInlet,
       "transferSwitchTransferToInlet": transferSwitchTransferToInlet,
       "transferSwitchAlarmOverride": transferSwitchAlarmOverride,
       "transferSwitchLastTransferReason": transferSwitchLastTransferReason,
       "actuatorControl": actuatorControl,
       "actuatorControlTable": actuatorControlTable,
       "actuatorControlEntry": actuatorControlEntry,
       "actuatorState": actuatorState,
       "rcmControl": rcmControl,
       "rcmSelfTestTable": rcmSelfTestTable,
       "rcmSelfTestEntry": rcmSelfTestEntry,
       "rcmState": rcmState,
       "overCurrentProtectorRcmSelfTestTable": overCurrentProtectorRcmSelfTestTable,
       "overCurrentProtectorRcmSelfTestEntry": overCurrentProtectorRcmSelfTestEntry,
       "overCurrentProtectorRcmState": overCurrentProtectorRcmState,
       "inletSensorControl": inletSensorControl,
       "inletSensorControlTable": inletSensorControlTable,
       "inletSensorControlEntry": inletSensorControlEntry,
       "inletSensorResetValue": inletSensorResetValue,
       "inletSensorResetMinMax": inletSensorResetMinMax,
       "inletPoleSensorControlTable": inletPoleSensorControlTable,
       "inletPoleSensorControlEntry": inletPoleSensorControlEntry,
       "inletPoleSensorResetMinMax": inletPoleSensorResetMinMax,
       "inletLinePairSensorControlTable": inletLinePairSensorControlTable,
       "inletLinePairSensorControlEntry": inletLinePairSensorControlEntry,
       "inletLinePairSensorResetMinMax": inletLinePairSensorResetMinMax,
       "outletSensorControl": outletSensorControl,
       "outletSensorControlTable": outletSensorControlTable,
       "outletSensorControlEntry": outletSensorControlEntry,
       "outletSensorResetValue": outletSensorResetValue,
       "outletSensorResetMinMax": outletSensorResetMinMax,
       "outletPoleSensorControlTable": outletPoleSensorControlTable,
       "outletPoleSensorControlEntry": outletPoleSensorControlEntry,
       "outletPoleSensorResetMinMax": outletPoleSensorResetMinMax,
       "unitSensorControl": unitSensorControl,
       "unitSensorControlTable": unitSensorControlTable,
       "unitSensorControlEntry": unitSensorControlEntry,
       "unitSensorResetValue": unitSensorResetValue,
       "unitSensorResetMinMax": unitSensorResetMinMax,
       "circuitSensorControl": circuitSensorControl,
       "circuitSensorControlTable": circuitSensorControlTable,
       "circuitSensorControlEntry": circuitSensorControlEntry,
       "circuitSensorResetValue": circuitSensorResetValue,
       "circuitSensorResetMinMax": circuitSensorResetMinMax,
       "circuitPoleSensorControlTable": circuitPoleSensorControlTable,
       "circuitPoleSensorControlEntry": circuitPoleSensorControlEntry,
       "circuitPoleSensorResetMinMax": circuitPoleSensorResetMinMax,
       "outletGroupControl": outletGroupControl,
       "outletGroupSwitchControlTable": outletGroupSwitchControlTable,
       "outletGroupSwitchControlEntry": outletGroupSwitchControlEntry,
       "outletGroupSwitchingOperation": outletGroupSwitchingOperation,
       "outletGroupSensorControl": outletGroupSensorControl,
       "outletGroupSensorControlTable": outletGroupSensorControlTable,
       "outletGroupSensorControlEntry": outletGroupSensorControlEntry,
       "outletGroupSensorResetValue": outletGroupSensorResetValue,
       "outletGroupSensorResetMinMax": outletGroupSensorResetMinMax,
       "serverPowerControl": serverPowerControl,
       "serverPowerControlTable": serverPowerControlTable,
       "serverPowerControlEntry": serverPowerControlEntry,
       "serverPowerControlOperation": serverPowerControlOperation,
       "overCurrentProtectorSensorControl": overCurrentProtectorSensorControl,
       "overCurrentProtectorSensorControlTable": overCurrentProtectorSensorControlTable,
       "overCurrentProtectorSensorControlEntry": overCurrentProtectorSensorControlEntry,
       "overCurrentProtectorSensorResetMinMax": overCurrentProtectorSensorResetMinMax,
       "transferSwitchSensorControl": transferSwitchSensorControl,
       "transferSwitchSensorControlTable": transferSwitchSensorControlTable,
       "transferSwitchSensorControlEntry": transferSwitchSensorControlEntry,
       "transferSwitchSensorResetMinMax": transferSwitchSensorResetMinMax,
       "measurements": measurements,
       "measurementsUnit": measurementsUnit,
       "unitSensorMeasurementsTable": unitSensorMeasurementsTable,
       "unitSensorMeasurementsEntry": unitSensorMeasurementsEntry,
       "measurementsUnitSensorIsAvailable": measurementsUnitSensorIsAvailable,
       "measurementsUnitSensorState": measurementsUnitSensorState,
       "measurementsUnitSensorValue": measurementsUnitSensorValue,
       "measurementsUnitSensorTimeStamp": measurementsUnitSensorTimeStamp,
       "measurementsUnitSensorSignedValue": measurementsUnitSensorSignedValue,
       "measurementsUnitSensorMinMaxValid": measurementsUnitSensorMinMaxValid,
       "measurementsUnitSensorMinValue": measurementsUnitSensorMinValue,
       "measurementsUnitSensorSignedMinValue": measurementsUnitSensorSignedMinValue,
       "measurementsUnitSensorMinTimeStamp": measurementsUnitSensorMinTimeStamp,
       "measurementsUnitSensorMaxValue": measurementsUnitSensorMaxValue,
       "measurementsUnitSensorSignedMaxValue": measurementsUnitSensorSignedMaxValue,
       "measurementsUnitSensorMaxTimeStamp": measurementsUnitSensorMaxTimeStamp,
       "measurementsUnitSensorMinMaxResetTimeStamp": measurementsUnitSensorMinMaxResetTimeStamp,
       "measurementsUnitSensorResetTimeStamp": measurementsUnitSensorResetTimeStamp,
       "measurementsInlet": measurementsInlet,
       "inletSensorMeasurementsTable": inletSensorMeasurementsTable,
       "inletSensorMeasurementsEntry": inletSensorMeasurementsEntry,
       "measurementsInletSensorIsAvailable": measurementsInletSensorIsAvailable,
       "measurementsInletSensorState": measurementsInletSensorState,
       "measurementsInletSensorValue": measurementsInletSensorValue,
       "measurementsInletSensorTimeStamp": measurementsInletSensorTimeStamp,
       "measurementsInletSensorSignedValue": measurementsInletSensorSignedValue,
       "measurementsInletSensorMinMaxValid": measurementsInletSensorMinMaxValid,
       "measurementsInletSensorMinValue": measurementsInletSensorMinValue,
       "measurementsInletSensorSignedMinValue": measurementsInletSensorSignedMinValue,
       "measurementsInletSensorMinTimeStamp": measurementsInletSensorMinTimeStamp,
       "measurementsInletSensorMaxValue": measurementsInletSensorMaxValue,
       "measurementsInletSensorSignedMaxValue": measurementsInletSensorSignedMaxValue,
       "measurementsInletSensorMaxTimeStamp": measurementsInletSensorMaxTimeStamp,
       "measurementsInletSensorMinMaxResetTimeStamp": measurementsInletSensorMinMaxResetTimeStamp,
       "measurementsInletSensorResetTimeStamp": measurementsInletSensorResetTimeStamp,
       "inletPoleSensorMeasurementsTable": inletPoleSensorMeasurementsTable,
       "inletPoleSensorMeasurementsEntry": inletPoleSensorMeasurementsEntry,
       "measurementsInletPoleSensorIsAvailable": measurementsInletPoleSensorIsAvailable,
       "measurementsInletPoleSensorState": measurementsInletPoleSensorState,
       "measurementsInletPoleSensorValue": measurementsInletPoleSensorValue,
       "measurementsInletPoleSensorTimeStamp": measurementsInletPoleSensorTimeStamp,
       "measurementsInletPoleSensorSignedValue": measurementsInletPoleSensorSignedValue,
       "measurementsInletPoleSensorMinMaxValid": measurementsInletPoleSensorMinMaxValid,
       "measurementsInletPoleSensorMinValue": measurementsInletPoleSensorMinValue,
       "measurementsInletPoleSensorSignedMinValue": measurementsInletPoleSensorSignedMinValue,
       "measurementsInletPoleSensorMinTimeStamp": measurementsInletPoleSensorMinTimeStamp,
       "measurementsInletPoleSensorMaxValue": measurementsInletPoleSensorMaxValue,
       "measurementsInletPoleSensorSignedMaxValue": measurementsInletPoleSensorSignedMaxValue,
       "measurementsInletPoleSensorMaxTimeStamp": measurementsInletPoleSensorMaxTimeStamp,
       "measurementsInletPoleSensorMinMaxResetTimeStamp": measurementsInletPoleSensorMinMaxResetTimeStamp,
       "inletLinePairSensorMeasurementsTable": inletLinePairSensorMeasurementsTable,
       "inletLinePairSensorMeasurementsEntry": inletLinePairSensorMeasurementsEntry,
       "measurementsInletLinePairSensorIsAvailable": measurementsInletLinePairSensorIsAvailable,
       "measurementsInletLinePairSensorState": measurementsInletLinePairSensorState,
       "measurementsInletLinePairSensorValue": measurementsInletLinePairSensorValue,
       "measurementsInletLinePairSensorTimeStamp": measurementsInletLinePairSensorTimeStamp,
       "measurementsInletLinePairSensorSignedValue": measurementsInletLinePairSensorSignedValue,
       "measurementsInletLinePairSensorMinMaxValid": measurementsInletLinePairSensorMinMaxValid,
       "measurementsInletLinePairSensorMinValue": measurementsInletLinePairSensorMinValue,
       "measurementsInletLinePairSensorSignedMinValue": measurementsInletLinePairSensorSignedMinValue,
       "measurementsInletLinePairSensorMinTimeStamp": measurementsInletLinePairSensorMinTimeStamp,
       "measurementsInletLinePairSensorMaxValue": measurementsInletLinePairSensorMaxValue,
       "measurementsInletLinePairSensorSignedMaxValue": measurementsInletLinePairSensorSignedMaxValue,
       "measurementsInletLinePairSensorMaxTimeStamp": measurementsInletLinePairSensorMaxTimeStamp,
       "measurementsInletLinePairSensorMinMaxResetTimeStamp": measurementsInletLinePairSensorMinMaxResetTimeStamp,
       "measurementsOverCurrentProtector": measurementsOverCurrentProtector,
       "overCurrentProtectorSensorMeasurementsTable": overCurrentProtectorSensorMeasurementsTable,
       "overCurrentProtectorSensorMeasurementsEntry": overCurrentProtectorSensorMeasurementsEntry,
       "measurementsOverCurrentProtectorSensorIsAvailable": measurementsOverCurrentProtectorSensorIsAvailable,
       "measurementsOverCurrentProtectorSensorState": measurementsOverCurrentProtectorSensorState,
       "measurementsOverCurrentProtectorSensorValue": measurementsOverCurrentProtectorSensorValue,
       "measurementsOverCurrentProtectorSensorTimeStamp": measurementsOverCurrentProtectorSensorTimeStamp,
       "measurementsOverCurrentProtectorSensorSignedValue": measurementsOverCurrentProtectorSensorSignedValue,
       "measurementsOverCurrentProtectorSensorMinMaxValid": measurementsOverCurrentProtectorSensorMinMaxValid,
       "measurementsOverCurrentProtectorSensorMinValue": measurementsOverCurrentProtectorSensorMinValue,
       "measurementsOverCurrentProtectorSensorSignedMinValue": measurementsOverCurrentProtectorSensorSignedMinValue,
       "measurementsOverCurrentProtectorSensorMinTimeStamp": measurementsOverCurrentProtectorSensorMinTimeStamp,
       "measurementsOverCurrentProtectorSensorMaxValue": measurementsOverCurrentProtectorSensorMaxValue,
       "measurementsOverCurrentProtectorSensorSignedMaxValue": measurementsOverCurrentProtectorSensorSignedMaxValue,
       "measurementsOverCurrentProtectorSensorMaxTimeStamp": measurementsOverCurrentProtectorSensorMaxTimeStamp,
       "measurementsOverCurrentProtectorSensorMinMaxResetTimeStamp": measurementsOverCurrentProtectorSensorMinMaxResetTimeStamp,
       "measurementsOutlet": measurementsOutlet,
       "outletSensorMeasurementsTable": outletSensorMeasurementsTable,
       "outletSensorMeasurementsEntry": outletSensorMeasurementsEntry,
       "measurementsOutletSensorIsAvailable": measurementsOutletSensorIsAvailable,
       "measurementsOutletSensorState": measurementsOutletSensorState,
       "measurementsOutletSensorValue": measurementsOutletSensorValue,
       "measurementsOutletSensorTimeStamp": measurementsOutletSensorTimeStamp,
       "measurementsOutletSensorSignedValue": measurementsOutletSensorSignedValue,
       "measurementsOutletSensorMinMaxValid": measurementsOutletSensorMinMaxValid,
       "measurementsOutletSensorMinValue": measurementsOutletSensorMinValue,
       "measurementsOutletSensorSignedMinValue": measurementsOutletSensorSignedMinValue,
       "measurementsOutletSensorMinTimeStamp": measurementsOutletSensorMinTimeStamp,
       "measurementsOutletSensorMaxValue": measurementsOutletSensorMaxValue,
       "measurementsOutletSensorSignedMaxValue": measurementsOutletSensorSignedMaxValue,
       "measurementsOutletSensorMaxTimeStamp": measurementsOutletSensorMaxTimeStamp,
       "measurementsOutletSensorMinMaxResetTimeStamp": measurementsOutletSensorMinMaxResetTimeStamp,
       "measurementsOutletSensorResetTimeStamp": measurementsOutletSensorResetTimeStamp,
       "outletPoleSensorMeasurementsTable": outletPoleSensorMeasurementsTable,
       "outletPoleSensorMeasurementsEntry": outletPoleSensorMeasurementsEntry,
       "measurementsOutletPoleSensorIsAvailable": measurementsOutletPoleSensorIsAvailable,
       "measurementsOutletPoleSensorState": measurementsOutletPoleSensorState,
       "measurementsOutletPoleSensorValue": measurementsOutletPoleSensorValue,
       "measurementsOutletPoleSensorTimeStamp": measurementsOutletPoleSensorTimeStamp,
       "measurementsOutletPoleSensorSignedValue": measurementsOutletPoleSensorSignedValue,
       "measurementsOutletPoleSensorMinMaxValid": measurementsOutletPoleSensorMinMaxValid,
       "measurementsOutletPoleSensorMinValue": measurementsOutletPoleSensorMinValue,
       "measurementsOutletPoleSensorSignedMinValue": measurementsOutletPoleSensorSignedMinValue,
       "measurementsOutletPoleSensorMinTimeStamp": measurementsOutletPoleSensorMinTimeStamp,
       "measurementsOutletPoleSensorMaxValue": measurementsOutletPoleSensorMaxValue,
       "measurementsOutletPoleSensorSignedMaxValue": measurementsOutletPoleSensorSignedMaxValue,
       "measurementsOutletPoleSensorMaxTimeStamp": measurementsOutletPoleSensorMaxTimeStamp,
       "measurementsOutletPoleSensorMinMaxResetTimeStamp": measurementsOutletPoleSensorMinMaxResetTimeStamp,
       "measurementsExternalSensor": measurementsExternalSensor,
       "externalSensorMeasurementsTable": externalSensorMeasurementsTable,
       "externalSensorMeasurementsEntry": externalSensorMeasurementsEntry,
       "measurementsExternalSensorIsAvailable": measurementsExternalSensorIsAvailable,
       "measurementsExternalSensorState": measurementsExternalSensorState,
       "measurementsExternalSensorValue": measurementsExternalSensorValue,
       "measurementsExternalSensorTimeStamp": measurementsExternalSensorTimeStamp,
       "measurementsExternalSensorMinMaxValid": measurementsExternalSensorMinMaxValid,
       "measurementsExternalSensorMinValue": measurementsExternalSensorMinValue,
       "measurementsExternalSensorMinTimeStamp": measurementsExternalSensorMinTimeStamp,
       "measurementsExternalSensorMaxValue": measurementsExternalSensorMaxValue,
       "measurementsExternalSensorMaxTimeStamp": measurementsExternalSensorMaxTimeStamp,
       "measurementsExternalSensorMinMaxResetTimeStamp": measurementsExternalSensorMinMaxResetTimeStamp,
       "measurementsWire": measurementsWire,
       "wireSensorMeasurementsTable": wireSensorMeasurementsTable,
       "wireSensorMeasurementsEntry": wireSensorMeasurementsEntry,
       "measurementsWireSensorIsAvailable": measurementsWireSensorIsAvailable,
       "measurementsWireSensorState": measurementsWireSensorState,
       "measurementsWireSensorValue": measurementsWireSensorValue,
       "measurementsWireSensorTimeStamp": measurementsWireSensorTimeStamp,
       "measurementsTransferSwitch": measurementsTransferSwitch,
       "transferSwitchSensorMeasurementsTable": transferSwitchSensorMeasurementsTable,
       "transferSwitchSensorMeasurementsEntry": transferSwitchSensorMeasurementsEntry,
       "measurementsTransferSwitchSensorIsAvailable": measurementsTransferSwitchSensorIsAvailable,
       "measurementsTransferSwitchSensorState": measurementsTransferSwitchSensorState,
       "measurementsTransferSwitchSensorValue": measurementsTransferSwitchSensorValue,
       "measurementsTransferSwitchSensorTimeStamp": measurementsTransferSwitchSensorTimeStamp,
       "measurementsTransferSwitchSensorSignedValue": measurementsTransferSwitchSensorSignedValue,
       "measurementsTransferSwitchSensorMinMaxValid": measurementsTransferSwitchSensorMinMaxValid,
       "measurementsTransferSwitchSensorMinValue": measurementsTransferSwitchSensorMinValue,
       "measurementsTransferSwitchSensorSignedMinValue": measurementsTransferSwitchSensorSignedMinValue,
       "measurementsTransferSwitchSensorMinTimeStamp": measurementsTransferSwitchSensorMinTimeStamp,
       "measurementsTransferSwitchSensorMaxValue": measurementsTransferSwitchSensorMaxValue,
       "measurementsTransferSwitchSensorSignedMaxValue": measurementsTransferSwitchSensorSignedMaxValue,
       "measurementsTransferSwitchSensorMaxTimeStamp": measurementsTransferSwitchSensorMaxTimeStamp,
       "measurementsTransferSwitchSensorMinMaxResetTimeStamp": measurementsTransferSwitchSensorMinMaxResetTimeStamp,
       "measurementsCircuit": measurementsCircuit,
       "circuitSensorMeasurementsTable": circuitSensorMeasurementsTable,
       "circuitSensorMeasurementsEntry": circuitSensorMeasurementsEntry,
       "measurementsCircuitSensorIsAvailable": measurementsCircuitSensorIsAvailable,
       "measurementsCircuitSensorState": measurementsCircuitSensorState,
       "measurementsCircuitSensorValue": measurementsCircuitSensorValue,
       "measurementsCircuitSensorTimeStamp": measurementsCircuitSensorTimeStamp,
       "measurementsCircuitSensorSignedValue": measurementsCircuitSensorSignedValue,
       "measurementsCircuitSensorMinMaxValid": measurementsCircuitSensorMinMaxValid,
       "measurementsCircuitSensorMinValue": measurementsCircuitSensorMinValue,
       "measurementsCircuitSensorSignedMinValue": measurementsCircuitSensorSignedMinValue,
       "measurementsCircuitSensorMinTimeStamp": measurementsCircuitSensorMinTimeStamp,
       "measurementsCircuitSensorMaxValue": measurementsCircuitSensorMaxValue,
       "measurementsCircuitSensorSignedMaxValue": measurementsCircuitSensorSignedMaxValue,
       "measurementsCircuitSensorMaxTimeStamp": measurementsCircuitSensorMaxTimeStamp,
       "measurementsCircuitSensorMinMaxResetTimeStamp": measurementsCircuitSensorMinMaxResetTimeStamp,
       "measurementsCircuitSensorResetTimeStamp": measurementsCircuitSensorResetTimeStamp,
       "circuitPoleSensorMeasurementsTable": circuitPoleSensorMeasurementsTable,
       "circuitPoleSensorMeasurementsEntry": circuitPoleSensorMeasurementsEntry,
       "measurementsCircuitPoleSensorIsAvailable": measurementsCircuitPoleSensorIsAvailable,
       "measurementsCircuitPoleSensorState": measurementsCircuitPoleSensorState,
       "measurementsCircuitPoleSensorValue": measurementsCircuitPoleSensorValue,
       "measurementsCircuitPoleSensorTimeStamp": measurementsCircuitPoleSensorTimeStamp,
       "measurementsCircuitPoleSensorSignedValue": measurementsCircuitPoleSensorSignedValue,
       "measurementsCircuitPoleSensorMinMaxValid": measurementsCircuitPoleSensorMinMaxValid,
       "measurementsCircuitPoleSensorMinValue": measurementsCircuitPoleSensorMinValue,
       "measurementsCircuitPoleSensorSignedMinValue": measurementsCircuitPoleSensorSignedMinValue,
       "measurementsCircuitPoleSensorMinTimeStamp": measurementsCircuitPoleSensorMinTimeStamp,
       "measurementsCircuitPoleSensorMaxValue": measurementsCircuitPoleSensorMaxValue,
       "measurementsCircuitPoleSensorSignedMaxValue": measurementsCircuitPoleSensorSignedMaxValue,
       "measurementsCircuitPoleSensorMaxTimeStamp": measurementsCircuitPoleSensorMaxTimeStamp,
       "measurementsCircuitPoleSensorMinMaxResetTimeStamp": measurementsCircuitPoleSensorMinMaxResetTimeStamp,
       "measurementsOutletGroup": measurementsOutletGroup,
       "outletGroupSensorMeasurementsTable": outletGroupSensorMeasurementsTable,
       "outletGroupSensorMeasurementsEntry": outletGroupSensorMeasurementsEntry,
       "measurementsOutletGroupSensorIsAvailable": measurementsOutletGroupSensorIsAvailable,
       "measurementsOutletGroupSensorState": measurementsOutletGroupSensorState,
       "measurementsOutletGroupSensorValue": measurementsOutletGroupSensorValue,
       "measurementsOutletGroupSensorTimeStamp": measurementsOutletGroupSensorTimeStamp,
       "measurementsOutletGroupSensorSignedValue": measurementsOutletGroupSensorSignedValue,
       "measurementsOutletGroupSensorMinMaxValid": measurementsOutletGroupSensorMinMaxValid,
       "measurementsOutletGroupSensorMinValue": measurementsOutletGroupSensorMinValue,
       "measurementsOutletGroupSensorSignedMinValue": measurementsOutletGroupSensorSignedMinValue,
       "measurementsOutletGroupSensorMinTimeStamp": measurementsOutletGroupSensorMinTimeStamp,
       "measurementsOutletGroupSensorMaxValue": measurementsOutletGroupSensorMaxValue,
       "measurementsOutletGroupSensorSignedMaxValue": measurementsOutletGroupSensorSignedMaxValue,
       "measurementsOutletGroupSensorMaxTimeStamp": measurementsOutletGroupSensorMaxTimeStamp,
       "measurementsOutletGroupSensorMinMaxResetTimeStamp": measurementsOutletGroupSensorMinMaxResetTimeStamp,
       "measurementsOutletGroupSensorResetTimeStamp": measurementsOutletGroupSensorResetTimeStamp,
       "log": log,
       "logUnit": logUnit,
       "logIndexTable": logIndexTable,
       "logIndexEntry": logIndexEntry,
       "oldestLogID": oldestLogID,
       "newestLogID": newestLogID,
       "logTimeStampTable": logTimeStampTable,
       "logTimeStampEntry": logTimeStampEntry,
       "logIndex": logIndex,
       "logTimeStamp": logTimeStamp,
       "unitSensorLogTable": unitSensorLogTable,
       "unitSensorLogEntry": unitSensorLogEntry,
       "logUnitSensorDataAvailable": logUnitSensorDataAvailable,
       "logUnitSensorState": logUnitSensorState,
       "logUnitSensorAvgValue": logUnitSensorAvgValue,
       "logUnitSensorMaxValue": logUnitSensorMaxValue,
       "logUnitSensorMinValue": logUnitSensorMinValue,
       "logUnitSensorSignedAvgValue": logUnitSensorSignedAvgValue,
       "logUnitSensorSignedMaxValue": logUnitSensorSignedMaxValue,
       "logUnitSensorSignedMinValue": logUnitSensorSignedMinValue,
       "logInlet": logInlet,
       "inletSensorLogTable": inletSensorLogTable,
       "inletSensorLogEntry": inletSensorLogEntry,
       "logInletSensorDataAvailable": logInletSensorDataAvailable,
       "logInletSensorState": logInletSensorState,
       "logInletSensorAvgValue": logInletSensorAvgValue,
       "logInletSensorMaxValue": logInletSensorMaxValue,
       "logInletSensorMinValue": logInletSensorMinValue,
       "logInletSensorSignedAvgValue": logInletSensorSignedAvgValue,
       "logInletSensorSignedMaxValue": logInletSensorSignedMaxValue,
       "logInletSensorSignedMinValue": logInletSensorSignedMinValue,
       "inletPoleSensorLogTable": inletPoleSensorLogTable,
       "inletPoleSensorLogEntry": inletPoleSensorLogEntry,
       "logInletPoleSensorDataAvailable": logInletPoleSensorDataAvailable,
       "logInletPoleSensorState": logInletPoleSensorState,
       "logInletPoleSensorAvgValue": logInletPoleSensorAvgValue,
       "logInletPoleSensorMaxValue": logInletPoleSensorMaxValue,
       "logInletPoleSensorMinValue": logInletPoleSensorMinValue,
       "logInletPoleSensorSignedAvgValue": logInletPoleSensorSignedAvgValue,
       "logInletPoleSensorSignedMaxValue": logInletPoleSensorSignedMaxValue,
       "logInletPoleSensorSignedMinValue": logInletPoleSensorSignedMinValue,
       "inletLinePairSensorLogTable": inletLinePairSensorLogTable,
       "inletLinePairSensorLogEntry": inletLinePairSensorLogEntry,
       "logInletLinePairSensorDataAvailable": logInletLinePairSensorDataAvailable,
       "logInletLinePairSensorState": logInletLinePairSensorState,
       "logInletLinePairSensorAvgValue": logInletLinePairSensorAvgValue,
       "logInletLinePairSensorMaxValue": logInletLinePairSensorMaxValue,
       "logInletLinePairSensorMinValue": logInletLinePairSensorMinValue,
       "logInletLinePairSensorSignedAvgValue": logInletLinePairSensorSignedAvgValue,
       "logInletLinePairSensorSignedMaxValue": logInletLinePairSensorSignedMaxValue,
       "logInletLinePairSensorSignedMinValue": logInletLinePairSensorSignedMinValue,
       "logOverCurrentProtector": logOverCurrentProtector,
       "overCurrentProtectorSensorLogTable": overCurrentProtectorSensorLogTable,
       "overCurrentProtectorSensorLogEntry": overCurrentProtectorSensorLogEntry,
       "logOverCurrentProtectorSensorDataAvailable": logOverCurrentProtectorSensorDataAvailable,
       "logOverCurrentProtectorSensorState": logOverCurrentProtectorSensorState,
       "logOverCurrentProtectorSensorAvgValue": logOverCurrentProtectorSensorAvgValue,
       "logOverCurrentProtectorSensorMaxValue": logOverCurrentProtectorSensorMaxValue,
       "logOverCurrentProtectorSensorMinValue": logOverCurrentProtectorSensorMinValue,
       "logOverCurrentProtectorSensorSignedAvgValue": logOverCurrentProtectorSensorSignedAvgValue,
       "logOverCurrentProtectorSensorSignedMaxValue": logOverCurrentProtectorSensorSignedMaxValue,
       "logOverCurrentProtectorSensorSignedMinValue": logOverCurrentProtectorSensorSignedMinValue,
       "logOutlet": logOutlet,
       "outletSensorLogTable": outletSensorLogTable,
       "outletSensorLogEntry": outletSensorLogEntry,
       "logOutletSensorDataAvailable": logOutletSensorDataAvailable,
       "logOutletSensorState": logOutletSensorState,
       "logOutletSensorAvgValue": logOutletSensorAvgValue,
       "logOutletSensorMaxValue": logOutletSensorMaxValue,
       "logOutletSensorMinValue": logOutletSensorMinValue,
       "logOutletSensorSignedAvgValue": logOutletSensorSignedAvgValue,
       "logOutletSensorSignedMaxValue": logOutletSensorSignedMaxValue,
       "logOutletSensorSignedMinValue": logOutletSensorSignedMinValue,
       "outletPoleSensorLogTable": outletPoleSensorLogTable,
       "outletPoleSensorLogEntry": outletPoleSensorLogEntry,
       "logOutletPoleSensorDataAvailable": logOutletPoleSensorDataAvailable,
       "logOutletPoleSensorState": logOutletPoleSensorState,
       "logOutletPoleSensorAvgValue": logOutletPoleSensorAvgValue,
       "logOutletPoleSensorMaxValue": logOutletPoleSensorMaxValue,
       "logOutletPoleSensorMinValue": logOutletPoleSensorMinValue,
       "logOutletPoleSensorSignedAvgValue": logOutletPoleSensorSignedAvgValue,
       "logOutletPoleSensorSignedMaxValue": logOutletPoleSensorSignedMaxValue,
       "logOutletPoleSensorSignedMinValue": logOutletPoleSensorSignedMinValue,
       "logExternalSensor": logExternalSensor,
       "externalSensorLogTable": externalSensorLogTable,
       "externalSensorLogEntry": externalSensorLogEntry,
       "logExternalSensorDataAvailable": logExternalSensorDataAvailable,
       "logExternalSensorState": logExternalSensorState,
       "logExternalSensorAvgValue": logExternalSensorAvgValue,
       "logExternalSensorMaxValue": logExternalSensorMaxValue,
       "logExternalSensorMinValue": logExternalSensorMinValue,
       "logWire": logWire,
       "wireSensorLogTable": wireSensorLogTable,
       "wireSensorLogEntry": wireSensorLogEntry,
       "logWireSensorDataAvailable": logWireSensorDataAvailable,
       "logWireSensorState": logWireSensorState,
       "logWireSensorAvgValue": logWireSensorAvgValue,
       "logWireSensorMaxValue": logWireSensorMaxValue,
       "logWireSensorMinValue": logWireSensorMinValue,
       "logTransferSwitch": logTransferSwitch,
       "transferSwitchSensorLogTable": transferSwitchSensorLogTable,
       "transferSwitchSensorLogEntry": transferSwitchSensorLogEntry,
       "logTransferSwitchSensorDataAvailable": logTransferSwitchSensorDataAvailable,
       "logTransferSwitchSensorState": logTransferSwitchSensorState,
       "logTransferSwitchSensorAvgValue": logTransferSwitchSensorAvgValue,
       "logTransferSwitchSensorMaxValue": logTransferSwitchSensorMaxValue,
       "logTransferSwitchSensorMinValue": logTransferSwitchSensorMinValue,
       "logTransferSwitchSensorSignedAvgValue": logTransferSwitchSensorSignedAvgValue,
       "logTransferSwitchSensorSignedMaxValue": logTransferSwitchSensorSignedMaxValue,
       "logTransferSwitchSensorSignedMinValue": logTransferSwitchSensorSignedMinValue,
       "logCircuit": logCircuit,
       "circuitSensorLogTable": circuitSensorLogTable,
       "circuitSensorLogEntry": circuitSensorLogEntry,
       "logCircuitSensorDataAvailable": logCircuitSensorDataAvailable,
       "logCircuitSensorState": logCircuitSensorState,
       "logCircuitSensorAvgValue": logCircuitSensorAvgValue,
       "logCircuitSensorMaxValue": logCircuitSensorMaxValue,
       "logCircuitSensorMinValue": logCircuitSensorMinValue,
       "logCircuitSensorSignedAvgValue": logCircuitSensorSignedAvgValue,
       "logCircuitSensorSignedMaxValue": logCircuitSensorSignedMaxValue,
       "logCircuitSensorSignedMinValue": logCircuitSensorSignedMinValue,
       "circuitPoleSensorLogTable": circuitPoleSensorLogTable,
       "circuitPoleSensorLogEntry": circuitPoleSensorLogEntry,
       "logCircuitPoleSensorDataAvailable": logCircuitPoleSensorDataAvailable,
       "logCircuitPoleSensorState": logCircuitPoleSensorState,
       "logCircuitPoleSensorAvgValue": logCircuitPoleSensorAvgValue,
       "logCircuitPoleSensorMaxValue": logCircuitPoleSensorMaxValue,
       "logCircuitPoleSensorMinValue": logCircuitPoleSensorMinValue,
       "logCircuitPoleSensorSignedAvgValue": logCircuitPoleSensorSignedAvgValue,
       "logCircuitPoleSensorSignedMaxValue": logCircuitPoleSensorSignedMaxValue,
       "logCircuitPoleSensorSignedMinValue": logCircuitPoleSensorSignedMinValue,
       "logOutletGroup": logOutletGroup,
       "outletGroupSensorLogTable": outletGroupSensorLogTable,
       "outletGroupSensorLogEntry": outletGroupSensorLogEntry,
       "logOutletGroupSensorDataAvailable": logOutletGroupSensorDataAvailable,
       "logOutletGroupSensorState": logOutletGroupSensorState,
       "logOutletGroupSensorAvgValue": logOutletGroupSensorAvgValue,
       "logOutletGroupSensorMaxValue": logOutletGroupSensorMaxValue,
       "logOutletGroupSensorMinValue": logOutletGroupSensorMinValue,
       "logOutletGroupSensorSignedAvgValue": logOutletGroupSensorSignedAvgValue,
       "logOutletGroupSensorSignedMaxValue": logOutletGroupSensorSignedMaxValue,
       "logOutletGroupSensorSignedMinValue": logOutletGroupSensorSignedMinValue,
       "conformance": conformance,
       "compliances": compliances,
       "complianceRev1": complianceRev1,
       "complianceRev2": complianceRev2,
       "groups": groups,
       "configGroup": configGroup,
       "logGroup": logGroup,
       "measurementsGroup": measurementsGroup,
       "controlGroup": controlGroup,
       "trapInformationGroup": trapInformationGroup,
       "trapsGroup": trapsGroup,
       "reliabilityGroup": reliabilityGroup,
       "ipAddressGroup": ipAddressGroup,
       "oldConfigGroup": oldConfigGroup,
       "oldTrapsGroup": oldTrapsGroup,
       "obsoleteTrapsGroup": obsoleteTrapsGroup,
       "obsoleteObjectsGroup": obsoleteObjectsGroup,
       "reliability": reliability,
       "reliabilityData": reliabilityData,
       "reliabilityDataTableSequenceNumber": reliabilityDataTableSequenceNumber,
       "reliabilityDataTable": reliabilityDataTable,
       "reliabilityDataEntry": reliabilityDataEntry,
       "reliabilityIndex": reliabilityIndex,
       "reliabilityId": reliabilityId,
       "reliabilityDataValue": reliabilityDataValue,
       "reliabilityDataMaxPossible": reliabilityDataMaxPossible,
       "reliabilityDataWorstValue": reliabilityDataWorstValue,
       "reliabilityDataThreshold": reliabilityDataThreshold,
       "reliabilityDataRawUpperBytes": reliabilityDataRawUpperBytes,
       "reliabilityDataRawLowerBytes": reliabilityDataRawLowerBytes,
       "reliabilityDataFlags": reliabilityDataFlags,
       "reliabilityErrorLog": reliabilityErrorLog,
       "reliabilityErrorLogTable": reliabilityErrorLogTable,
       "reliabilityErrorLogEntry": reliabilityErrorLogEntry,
       "reliabilityErrorLogIndex": reliabilityErrorLogIndex,
       "reliabilityErrorLogId": reliabilityErrorLogId,
       "reliabilityErrorLogValue": reliabilityErrorLogValue,
       "reliabilityErrorLogThreshold": reliabilityErrorLogThreshold,
       "reliabilityErrorLogRawUpperBytes": reliabilityErrorLogRawUpperBytes,
       "reliabilityErrorLogRawLowerBytes": reliabilityErrorLogRawLowerBytes,
       "reliabilityErrorLogPOH": reliabilityErrorLogPOH,
       "reliabilityErrorLogTime": reliabilityErrorLogTime,
       "reliabilityHardwareHealth": reliabilityHardwareHealth,
       "hwFailureTable": hwFailureTable,
       "hwFailureEntry": hwFailureEntry,
       "hwFailureIndex": hwFailureIndex,
       "hwFailureComponentId": hwFailureComponentId,
       "hwFailureType": hwFailureType,
       "hwFailureAsserted": hwFailureAsserted,
       "hwFailureLastAssertTimeStamp": hwFailureLastAssertTimeStamp,
       "hwFailureLastDeassertTimeStamp": hwFailureLastDeassertTimeStamp,
       "hwFailureAssertCount": hwFailureAssertCount}
)
