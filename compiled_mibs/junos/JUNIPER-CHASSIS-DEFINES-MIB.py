# SNMP MIB module (JUNIPER-CHASSIS-DEFINES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-CHASSIS-DEFINES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:00 2025
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

(jnxMibs,
 jnxProducts) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs",
    "jnxProducts")

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

jnxChassisDefines = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 25)
)
if mibBuilder.loadTexts:
    jnxChassisDefines.setRevisions(
        ("2010-02-01 00:00",
         "2011-02-07 00:00",
         "2012-07-18 00:00",
         "2012-09-13 00:00",
         "2012-09-13 00:00",
         "2013-01-10 00:00",
         "2013-10-17 00:00",
         "2014-01-27 00:00",
         "2014-04-01 00:00",
         "2014-06-17 00:00",
         "2014-07-14 00:00",
         "2014-07-16 00:00",
         "2014-09-05 00:00",
         "2014-09-27 00:00",
         "2014-12-25 00:00",
         "2015-01-08 00:00",
         "2015-01-20 00:00",
         "2015-02-24 00:00",
         "2015-03-25 00:00",
         "2015-04-14 00:00",
         "2015-05-20 00:00",
         "2015-07-12 00:00",
         "2015-07-23 00:00",
         "2015-07-28 00:00",
         "2015-08-19 00:00",
         "2015-09-02 00:00",
         "2015-11-17 00:00",
         "2015-10-12 00:00",
         "2015-10-13 00:00",
         "2016-02-08 00:00",
         "2016-02-19 00:00",
         "2016-02-23 00:00",
         "2016-02-23 00:00",
         "2016-04-06 00:00",
         "2016-04-20 00:00",
         "2016-07-15 00:00",
         "2016-02-23 00:00",
         "2016-06-06 00:00",
         "2016-05-06 00:00",
         "2016-05-11 00:00",
         "2016-05-31 00:00",
         "2016-06-06 00:00",
         "2016-06-15 00:00",
         "2016-07-15 00:00",
         "2016-08-31 00:00",
         "2016-09-15 00:00",
         "2016-09-30 00:00",
         "2016-11-03 00:00",
         "2016-11-21 00:00",
         "2016-11-21 00:00",
         "2016-12-06 00:00",
         "2016-12-20 00:00",
         "2017-02-09 00:00",
         "2017-03-30 00:00",
         "2017-03-06 00:00",
         "2017-05-03 00:00",
         "2017-05-15 00:00",
         "2017-06-02 00:00",
         "2017-06-03 00:00",
         "2017-06-19 00:00",
         "2017-06-28 00:00",
         "2017-07-04 00:00",
         "2017-08-01 00:00",
         "2017-09-08 00:00",
         "2017-10-23 00:00",
         "2017-11-15 00:00",
         "2017-11-22 00:00",
         "2017-12-08 00:00",
         "2017-12-28 00:00",
         "2018-03-20 00:00",
         "2018-05-11 00:00",
         "2018-06-15 00:00",
         "2018-04-18 00:00",
         "2018-06-26 00:00",
         "2018-07-05 00:00",
         "2018-09-17 00:00",
         "2018-09-24 00:00",
         "2018-10-12 00:00",
         "2018-11-26 00:00",
         "2018-12-11 00:00",
         "2019-01-10 00:00",
         "2019-06-11 00:00",
         "2019-08-20 00:00",
         "2019-09-30 00:00",
         "2019-11-06 00:00",
         "2019-11-07 00:00",
         "2019-11-08 00:00",
         "2019-11-10 00:00",
         "2019-11-20 00:00",
         "2019-12-20 00:00",
         "2020-01-09 00:00",
         "2020-02-20 00:00",
         "2020-03-12 00:00",
         "2020-04-14 00:00",
         "2020-04-24 00:00",
         "2020-05-08 00:00",
         "2020-08-26 00:00",
         "2020-11-08 00:00",
         "2020-11-16 00:00",
         "2020-11-18 00:00",
         "2020-12-07 20:00",
         "2021-01-25 00:00",
         "2021-05-18 00:00",
         "2021-06-08 00:00",
         "2021-06-23 00:00",
         "2021-12-07 00:00",
         "2022-01-18 00:00",
         "2022-03-08 00:00",
         "2022-03-17 00:00",
         "2022-03-18 00:00",
         "2022-04-29 00:00",
         "2022-03-08 00:00",
         "2022-08-01 00:00",
         "2022-09-23 00:00",
         "2023-02-13 00:00",
         "2023-04-15 00:00",
         "2023-04-15 00:00",
         "2023-05-24 00:00",
         "2023-06-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxClassification_ObjectIdentity = ObjectIdentity
jnxClassification = _JnxClassification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1)
)
_JnxClassGeneral_ObjectIdentity = ObjectIdentity
jnxClassGeneral = _JnxClassGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1)
)
_JnxProductLine_ObjectIdentity = ObjectIdentity
jnxProductLine = _JnxProductLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1)
)
_JnxProductLineM40_ObjectIdentity = ObjectIdentity
jnxProductLineM40 = _JnxProductLineM40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 1)
)
_JnxProductLineM20_ObjectIdentity = ObjectIdentity
jnxProductLineM20 = _JnxProductLineM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 2)
)
_JnxProductLineM160_ObjectIdentity = ObjectIdentity
jnxProductLineM160 = _JnxProductLineM160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 3)
)
_JnxProductLineM10_ObjectIdentity = ObjectIdentity
jnxProductLineM10 = _JnxProductLineM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 4)
)
_JnxProductLineM5_ObjectIdentity = ObjectIdentity
jnxProductLineM5 = _JnxProductLineM5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 5)
)
_JnxProductLineT640_ObjectIdentity = ObjectIdentity
jnxProductLineT640 = _JnxProductLineT640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 6)
)
_JnxProductLineT320_ObjectIdentity = ObjectIdentity
jnxProductLineT320 = _JnxProductLineT320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 7)
)
_JnxProductLineM40e_ObjectIdentity = ObjectIdentity
jnxProductLineM40e = _JnxProductLineM40e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 8)
)
_JnxProductLineM320_ObjectIdentity = ObjectIdentity
jnxProductLineM320 = _JnxProductLineM320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 9)
)
_JnxProductLineM7i_ObjectIdentity = ObjectIdentity
jnxProductLineM7i = _JnxProductLineM7i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 10)
)
_JnxProductLineM10i_ObjectIdentity = ObjectIdentity
jnxProductLineM10i = _JnxProductLineM10i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 11)
)
_JnxProductLineJ2300_ObjectIdentity = ObjectIdentity
jnxProductLineJ2300 = _JnxProductLineJ2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 13)
)
_JnxProductLineJ4300_ObjectIdentity = ObjectIdentity
jnxProductLineJ4300 = _JnxProductLineJ4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 14)
)
_JnxProductLineJ6300_ObjectIdentity = ObjectIdentity
jnxProductLineJ6300 = _JnxProductLineJ6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 15)
)
_JnxProductLineIRM_ObjectIdentity = ObjectIdentity
jnxProductLineIRM = _JnxProductLineIRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 16)
)
_JnxProductLineTX_ObjectIdentity = ObjectIdentity
jnxProductLineTX = _JnxProductLineTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 17)
)
_JnxProductLineM120_ObjectIdentity = ObjectIdentity
jnxProductLineM120 = _JnxProductLineM120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 18)
)
_JnxProductLineJ4350_ObjectIdentity = ObjectIdentity
jnxProductLineJ4350 = _JnxProductLineJ4350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 19)
)
_JnxProductLineJ6350_ObjectIdentity = ObjectIdentity
jnxProductLineJ6350 = _JnxProductLineJ6350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 20)
)
_JnxProductLineMX960_ObjectIdentity = ObjectIdentity
jnxProductLineMX960 = _JnxProductLineMX960_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 21)
)
_JnxProductLineJ4320_ObjectIdentity = ObjectIdentity
jnxProductLineJ4320 = _JnxProductLineJ4320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 22)
)
_JnxProductLineJ2320_ObjectIdentity = ObjectIdentity
jnxProductLineJ2320 = _JnxProductLineJ2320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 23)
)
_JnxProductLineJ2350_ObjectIdentity = ObjectIdentity
jnxProductLineJ2350 = _JnxProductLineJ2350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 24)
)
_JnxProductLineMX480_ObjectIdentity = ObjectIdentity
jnxProductLineMX480 = _JnxProductLineMX480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 25)
)
_JnxProductLineSRX5800_ObjectIdentity = ObjectIdentity
jnxProductLineSRX5800 = _JnxProductLineSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 26)
)
_JnxProductLineT1600_ObjectIdentity = ObjectIdentity
jnxProductLineT1600 = _JnxProductLineT1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 27)
)
_JnxProductLineSRX5600_ObjectIdentity = ObjectIdentity
jnxProductLineSRX5600 = _JnxProductLineSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 28)
)
_JnxProductLineMX240_ObjectIdentity = ObjectIdentity
jnxProductLineMX240 = _JnxProductLineMX240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 29)
)
_JnxProductLineEX3200_ObjectIdentity = ObjectIdentity
jnxProductLineEX3200 = _JnxProductLineEX3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 30)
)
_JnxProductLineEX4200_ObjectIdentity = ObjectIdentity
jnxProductLineEX4200 = _JnxProductLineEX4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 31)
)
_JnxProductLineEX8208_ObjectIdentity = ObjectIdentity
jnxProductLineEX8208 = _JnxProductLineEX8208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 32)
)
_JnxProductLineEX8216_ObjectIdentity = ObjectIdentity
jnxProductLineEX8216 = _JnxProductLineEX8216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 33)
)
_JnxProductLineSRX3600_ObjectIdentity = ObjectIdentity
jnxProductLineSRX3600 = _JnxProductLineSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 34)
)
_JnxProductLineSRX3400_ObjectIdentity = ObjectIdentity
jnxProductLineSRX3400 = _JnxProductLineSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 35)
)
_JnxProductLineSRX210_ObjectIdentity = ObjectIdentity
jnxProductLineSRX210 = _JnxProductLineSRX210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 36)
)
_JnxProductLineTXP_ObjectIdentity = ObjectIdentity
jnxProductLineTXP = _JnxProductLineTXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 37)
)
_JnxProductLineJCS_ObjectIdentity = ObjectIdentity
jnxProductLineJCS = _JnxProductLineJCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 38)
)
_JnxProductLineSRX240_ObjectIdentity = ObjectIdentity
jnxProductLineSRX240 = _JnxProductLineSRX240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 39)
)
_JnxProductLineSRX650_ObjectIdentity = ObjectIdentity
jnxProductLineSRX650 = _JnxProductLineSRX650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 40)
)
_JnxProductLineSRX100_ObjectIdentity = ObjectIdentity
jnxProductLineSRX100 = _JnxProductLineSRX100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 41)
)
_JnxProductLineLN1000V_ObjectIdentity = ObjectIdentity
jnxProductLineLN1000V = _JnxProductLineLN1000V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 42)
)
_JnxProductLineEX2200_ObjectIdentity = ObjectIdentity
jnxProductLineEX2200 = _JnxProductLineEX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 43)
)
_JnxProductLineEX4500_ObjectIdentity = ObjectIdentity
jnxProductLineEX4500 = _JnxProductLineEX4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 44)
)
_JnxProductLineFXSeries_ObjectIdentity = ObjectIdentity
jnxProductLineFXSeries = _JnxProductLineFXSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 45)
)
_JnxProductLineIBM4274M02J02M_ObjectIdentity = ObjectIdentity
jnxProductLineIBM4274M02J02M = _JnxProductLineIBM4274M02J02M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 46)
)
_JnxProductLineIBM4274M06J06M_ObjectIdentity = ObjectIdentity
jnxProductLineIBM4274M06J06M = _JnxProductLineIBM4274M06J06M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 47)
)
_JnxProductLineIBM4274M11J11M_ObjectIdentity = ObjectIdentity
jnxProductLineIBM4274M11J11M = _JnxProductLineIBM4274M11J11M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 48)
)
_JnxProductLineSRX1400_ObjectIdentity = ObjectIdentity
jnxProductLineSRX1400 = _JnxProductLineSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 49)
)
_JnxProductLineIBM4274S58J58S_ObjectIdentity = ObjectIdentity
jnxProductLineIBM4274S58J58S = _JnxProductLineIBM4274S58J58S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 50)
)
_JnxProductLineIBM4274S56J56S_ObjectIdentity = ObjectIdentity
jnxProductLineIBM4274S56J56S = _JnxProductLineIBM4274S56J56S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 51)
)
_JnxProductLineIBM4274S36J36S_ObjectIdentity = ObjectIdentity
jnxProductLineIBM4274S36J36S = _JnxProductLineIBM4274S36J36S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 52)
)
_JnxProductLineIBM4274S34J34S_ObjectIdentity = ObjectIdentity
jnxProductLineIBM4274S34J34S = _JnxProductLineIBM4274S34J34S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 53)
)
_JnxProductLineIBM427348EJ48E_ObjectIdentity = ObjectIdentity
jnxProductLineIBM427348EJ48E = _JnxProductLineIBM427348EJ48E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 54)
)
_JnxProductLineIBM4274E08J08E_ObjectIdentity = ObjectIdentity
jnxProductLineIBM4274E08J08E = _JnxProductLineIBM4274E08J08E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 55)
)
_JnxProductLineIBM4274E16J16E_ObjectIdentity = ObjectIdentity
jnxProductLineIBM4274E16J16E = _JnxProductLineIBM4274E16J16E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 56)
)
_JnxProductLineMX80_ObjectIdentity = ObjectIdentity
jnxProductLineMX80 = _JnxProductLineMX80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 57)
)
_JnxProductLineSRX220_ObjectIdentity = ObjectIdentity
jnxProductLineSRX220 = _JnxProductLineSRX220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 58)
)
_JnxProductLineEXXRE_ObjectIdentity = ObjectIdentity
jnxProductLineEXXRE = _JnxProductLineEXXRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 59)
)
_JnxProductLineQFXInterconnect_ObjectIdentity = ObjectIdentity
jnxProductLineQFXInterconnect = _JnxProductLineQFXInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 60)
)
_JnxProductLineQFXNode_ObjectIdentity = ObjectIdentity
jnxProductLineQFXNode = _JnxProductLineQFXNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 61)
)
_JnxProductLineQFXJVRE_ObjectIdentity = ObjectIdentity
jnxProductLineQFXJVRE = _JnxProductLineQFXJVRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 62)
)
_JnxProductLineEX4300_ObjectIdentity = ObjectIdentity
jnxProductLineEX4300 = _JnxProductLineEX4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 63)
)
_JnxProductLineSRX110_ObjectIdentity = ObjectIdentity
jnxProductLineSRX110 = _JnxProductLineSRX110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 64)
)
_JnxProductLineSRX120_ObjectIdentity = ObjectIdentity
jnxProductLineSRX120 = _JnxProductLineSRX120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 65)
)
_JnxProductLineMAG8600_ObjectIdentity = ObjectIdentity
jnxProductLineMAG8600 = _JnxProductLineMAG8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 66)
)
_JnxProductLineMAG6611_ObjectIdentity = ObjectIdentity
jnxProductLineMAG6611 = _JnxProductLineMAG6611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 67)
)
_JnxProductLineMAG6610_ObjectIdentity = ObjectIdentity
jnxProductLineMAG6610 = _JnxProductLineMAG6610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 68)
)
_JnxProductLinePTX5000_ObjectIdentity = ObjectIdentity
jnxProductLinePTX5000 = _JnxProductLinePTX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 69)
)
_JnxProductLineIBM0719J45E_ObjectIdentity = ObjectIdentity
jnxProductLineIBM0719J45E = _JnxProductLineIBM0719J45E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 71)
)
_JnxProductLineIBMJ08F_ObjectIdentity = ObjectIdentity
jnxProductLineIBMJ08F = _JnxProductLineIBMJ08F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 72)
)
_JnxProductLineIBMJ52F_ObjectIdentity = ObjectIdentity
jnxProductLineIBMJ52F = _JnxProductLineIBMJ52F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 73)
)
_JnxProductLineEX6210_ObjectIdentity = ObjectIdentity
jnxProductLineEX6210 = _JnxProductLineEX6210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 74)
)
_JnxProductLineDellJFX3500_ObjectIdentity = ObjectIdentity
jnxProductLineDellJFX3500 = _JnxProductLineDellJFX3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 75)
)
_JnxProductLineEX3300_ObjectIdentity = ObjectIdentity
jnxProductLineEX3300 = _JnxProductLineEX3300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 76)
)
_JnxProductLineDELLJSRX3600_ObjectIdentity = ObjectIdentity
jnxProductLineDELLJSRX3600 = _JnxProductLineDELLJSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 77)
)
_JnxProductLineDELLJSRX3400_ObjectIdentity = ObjectIdentity
jnxProductLineDELLJSRX3400 = _JnxProductLineDELLJSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 78)
)
_JnxProductLineDELLJSRX1400_ObjectIdentity = ObjectIdentity
jnxProductLineDELLJSRX1400 = _JnxProductLineDELLJSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 79)
)
_JnxProductLineDELLJSRX5800_ObjectIdentity = ObjectIdentity
jnxProductLineDELLJSRX5800 = _JnxProductLineDELLJSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 80)
)
_JnxProductLineDELLJSRX5600_ObjectIdentity = ObjectIdentity
jnxProductLineDELLJSRX5600 = _JnxProductLineDELLJSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 81)
)
_JnxProductLineQFXSwitch_ObjectIdentity = ObjectIdentity
jnxProductLineQFXSwitch = _JnxProductLineQFXSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 82)
)
_JnxProductLineT4000_ObjectIdentity = ObjectIdentity
jnxProductLineT4000 = _JnxProductLineT4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 83)
)
_JnxProductLineQFX3000_ObjectIdentity = ObjectIdentity
jnxProductLineQFX3000 = _JnxProductLineQFX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 84)
)
_JnxProductLineQFX5000_ObjectIdentity = ObjectIdentity
jnxProductLineQFX5000 = _JnxProductLineQFX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 85)
)
_JnxProductLineSRX550_ObjectIdentity = ObjectIdentity
jnxProductLineSRX550 = _JnxProductLineSRX550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 86)
)
_JnxProductLineACX_ObjectIdentity = ObjectIdentity
jnxProductLineACX = _JnxProductLineACX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 87)
)
_JnxProductLineMX40_ObjectIdentity = ObjectIdentity
jnxProductLineMX40 = _JnxProductLineMX40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 88)
)
_JnxProductLineMX10_ObjectIdentity = ObjectIdentity
jnxProductLineMX10 = _JnxProductLineMX10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 89)
)
_JnxProductLineMX5_ObjectIdentity = ObjectIdentity
jnxProductLineMX5 = _JnxProductLineMX5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 90)
)
_JnxProductLineQFXMInterconnect_ObjectIdentity = ObjectIdentity
jnxProductLineQFXMInterconnect = _JnxProductLineQFXMInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 91)
)
_JnxProductLineEX4550_ObjectIdentity = ObjectIdentity
jnxProductLineEX4550 = _JnxProductLineEX4550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 92)
)
_JnxProductLineMX2020_ObjectIdentity = ObjectIdentity
jnxProductLineMX2020 = _JnxProductLineMX2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 93)
)
_JnxProductLineVseries_ObjectIdentity = ObjectIdentity
jnxProductLineVseries = _JnxProductLineVseries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 94)
)
_JnxProductLineLN2600_ObjectIdentity = ObjectIdentity
jnxProductLineLN2600 = _JnxProductLineLN2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 95)
)
_JnxProductLineFireflyPerimeter_ObjectIdentity = ObjectIdentity
jnxProductLineFireflyPerimeter = _JnxProductLineFireflyPerimeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 96)
)
_JnxProductLineMX104_ObjectIdentity = ObjectIdentity
jnxProductLineMX104 = _JnxProductLineMX104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 97)
)
_JnxProductLinePTX3000_ObjectIdentity = ObjectIdentity
jnxProductLinePTX3000 = _JnxProductLinePTX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 98)
)
_JnxProductLineMX2010_ObjectIdentity = ObjectIdentity
jnxProductLineMX2010 = _JnxProductLineMX2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 99)
)
_JnxProductLineQFX3100_ObjectIdentity = ObjectIdentity
jnxProductLineQFX3100 = _JnxProductLineQFX3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 100)
)
_JnxProductLineLN2800_ObjectIdentity = ObjectIdentity
jnxProductLineLN2800 = _JnxProductLineLN2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 101)
)
_JnxProductLineEX9214_ObjectIdentity = ObjectIdentity
jnxProductLineEX9214 = _JnxProductLineEX9214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 102)
)
_JnxProductLineEX9208_ObjectIdentity = ObjectIdentity
jnxProductLineEX9208 = _JnxProductLineEX9208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 103)
)
_JnxProductLineEX9204_ObjectIdentity = ObjectIdentity
jnxProductLineEX9204 = _JnxProductLineEX9204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 104)
)
_JnxProductLineSRX5400_ObjectIdentity = ObjectIdentity
jnxProductLineSRX5400 = _JnxProductLineSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 105)
)
_JnxProductLineIBM4274S54J54S_ObjectIdentity = ObjectIdentity
jnxProductLineIBM4274S54J54S = _JnxProductLineIBM4274S54J54S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 106)
)
_JnxProductLineDELLJSRX5400_ObjectIdentity = ObjectIdentity
jnxProductLineDELLJSRX5400 = _JnxProductLineDELLJSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 107)
)
_JnxProductLineVMX_ObjectIdentity = ObjectIdentity
jnxProductLineVMX = _JnxProductLineVMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 108)
)
_JnxProductLineEX4600_ObjectIdentity = ObjectIdentity
jnxProductLineEX4600 = _JnxProductLineEX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 109)
)
_JnxProductLineVRR_ObjectIdentity = ObjectIdentity
jnxProductLineVRR = _JnxProductLineVRR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 110)
)
_JnxProductLineOCPAcc_ObjectIdentity = ObjectIdentity
jnxProductLineOCPAcc = _JnxProductLineOCPAcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 112)
)
_JnxProductLineACX1000_ObjectIdentity = ObjectIdentity
jnxProductLineACX1000 = _JnxProductLineACX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 113)
)
_JnxProductLineACX2000_ObjectIdentity = ObjectIdentity
jnxProductLineACX2000 = _JnxProductLineACX2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 114)
)
_JnxProductLineACX1100_ObjectIdentity = ObjectIdentity
jnxProductLineACX1100 = _JnxProductLineACX1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 115)
)
_JnxProductLineACX2100_ObjectIdentity = ObjectIdentity
jnxProductLineACX2100 = _JnxProductLineACX2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 116)
)
_JnxProductLineACX2200_ObjectIdentity = ObjectIdentity
jnxProductLineACX2200 = _JnxProductLineACX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 117)
)
_JnxProductLineACX4000_ObjectIdentity = ObjectIdentity
jnxProductLineACX4000 = _JnxProductLineACX4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 118)
)
_JnxProductLineACX500AC_ObjectIdentity = ObjectIdentity
jnxProductLineACX500AC = _JnxProductLineACX500AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 119)
)
_JnxProductLineACX500DC_ObjectIdentity = ObjectIdentity
jnxProductLineACX500DC = _JnxProductLineACX500DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 120)
)
_JnxProductLineACX500OAC_ObjectIdentity = ObjectIdentity
jnxProductLineACX500OAC = _JnxProductLineACX500OAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 121)
)
_JnxProductLineACX500ODC_ObjectIdentity = ObjectIdentity
jnxProductLineACX500ODC = _JnxProductLineACX500ODC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 122)
)
_JnxProductLineACX500OPOEAC_ObjectIdentity = ObjectIdentity
jnxProductLineACX500OPOEAC = _JnxProductLineACX500OPOEAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 123)
)
_JnxProductLineACX500OPOEDC_ObjectIdentity = ObjectIdentity
jnxProductLineACX500OPOEDC = _JnxProductLineACX500OPOEDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 124)
)
_JnxProductLineSatelliteDevice_ObjectIdentity = ObjectIdentity
jnxProductLineSatelliteDevice = _JnxProductLineSatelliteDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 125)
)
_JnxProductLineACX5048_ObjectIdentity = ObjectIdentity
jnxProductLineACX5048 = _JnxProductLineACX5048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 126)
)
_JnxProductLineACX5096_ObjectIdentity = ObjectIdentity
jnxProductLineACX5096 = _JnxProductLineACX5096_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 127)
)
_JnxProductLineLN1000CC_ObjectIdentity = ObjectIdentity
jnxProductLineLN1000CC = _JnxProductLineLN1000CC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 128)
)
_JnxProductLineVSRX_ObjectIdentity = ObjectIdentity
jnxProductLineVSRX = _JnxProductLineVSRX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 129)
)
_JnxProductLinePTX1000_ObjectIdentity = ObjectIdentity
jnxProductLinePTX1000 = _JnxProductLinePTX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 130)
)
_JnxProductLineEX3400_ObjectIdentity = ObjectIdentity
jnxProductLineEX3400 = _JnxProductLineEX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 131)
)
_JnxProductLineEX2300_ObjectIdentity = ObjectIdentity
jnxProductLineEX2300 = _JnxProductLineEX2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 132)
)
_JnxProductLineSRX300_ObjectIdentity = ObjectIdentity
jnxProductLineSRX300 = _JnxProductLineSRX300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 133)
)
_JnxProductLineSRX320_ObjectIdentity = ObjectIdentity
jnxProductLineSRX320 = _JnxProductLineSRX320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 134)
)
_JnxProductLineSRX340_ObjectIdentity = ObjectIdentity
jnxProductLineSRX340 = _JnxProductLineSRX340_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 135)
)
_JnxProductLineSRX345_ObjectIdentity = ObjectIdentity
jnxProductLineSRX345 = _JnxProductLineSRX345_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 136)
)
_JnxProductLineSRX1500_ObjectIdentity = ObjectIdentity
jnxProductLineSRX1500 = _JnxProductLineSRX1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 137)
)
_JnxProductLineNFX_ObjectIdentity = ObjectIdentity
jnxProductLineNFX = _JnxProductLineNFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 138)
)
_JnxProductLineJNP10003_ObjectIdentity = ObjectIdentity
jnxProductLineJNP10003 = _JnxProductLineJNP10003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 139)
)
_JnxProductLineSRX4600_ObjectIdentity = ObjectIdentity
jnxProductLineSRX4600 = _JnxProductLineSRX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 140)
)
_JnxProductLineSRX4800_ObjectIdentity = ObjectIdentity
jnxProductLineSRX4800 = _JnxProductLineSRX4800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 141)
)
_JnxProductLineSRX4100_ObjectIdentity = ObjectIdentity
jnxProductLineSRX4100 = _JnxProductLineSRX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 142)
)
_JnxProductLineSRX4200_ObjectIdentity = ObjectIdentity
jnxProductLineSRX4200 = _JnxProductLineSRX4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 143)
)
_JnxProductLineJNP204_ObjectIdentity = ObjectIdentity
jnxProductLineJNP204 = _JnxProductLineJNP204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 144)
)
_JnxProductLineMX2008_ObjectIdentity = ObjectIdentity
jnxProductLineMX2008 = _JnxProductLineMX2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 145)
)
_JnxProductLineMXTSR80_ObjectIdentity = ObjectIdentity
jnxProductLineMXTSR80 = _JnxProductLineMXTSR80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 146)
)
_JnxProductLinePTX10008_ObjectIdentity = ObjectIdentity
jnxProductLinePTX10008 = _JnxProductLinePTX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 147)
)
_JnxProductLineACX5448_ObjectIdentity = ObjectIdentity
jnxProductLineACX5448 = _JnxProductLineACX5448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 148)
)
_JnxProductLinePTX10016_ObjectIdentity = ObjectIdentity
jnxProductLinePTX10016 = _JnxProductLinePTX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 150)
)
_JnxProductLineEX9251_ObjectIdentity = ObjectIdentity
jnxProductLineEX9251 = _JnxProductLineEX9251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 151)
)
_JnxProductLineMX150_ObjectIdentity = ObjectIdentity
jnxProductLineMX150 = _JnxProductLineMX150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 152)
)
_JnxProductLineJNP10001_ObjectIdentity = ObjectIdentity
jnxProductLineJNP10001 = _JnxProductLineJNP10001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 153)
)
_JnxProductLineMX10008_ObjectIdentity = ObjectIdentity
jnxProductLineMX10008 = _JnxProductLineMX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 154)
)
_JnxProductLineMX10016_ObjectIdentity = ObjectIdentity
jnxProductLineMX10016 = _JnxProductLineMX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 155)
)
_JnxProductLineEX9253_ObjectIdentity = ObjectIdentity
jnxProductLineEX9253 = _JnxProductLineEX9253_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 156)
)
_JnxProductLineJRR200_ObjectIdentity = ObjectIdentity
jnxProductLineJRR200 = _JnxProductLineJRR200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 157)
)
_JnxProductLineACX5448M_ObjectIdentity = ObjectIdentity
jnxProductLineACX5448M = _JnxProductLineACX5448M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 158)
)
_JnxProductLineACX5448D_ObjectIdentity = ObjectIdentity
jnxProductLineACX5448D = _JnxProductLineACX5448D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 159)
)
_JnxProductLineACX6360OR_ObjectIdentity = ObjectIdentity
jnxProductLineACX6360OR = _JnxProductLineACX6360OR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 160)
)
_JnxProductLineACX6360OX_ObjectIdentity = ObjectIdentity
jnxProductLineACX6360OX = _JnxProductLineACX6360OX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 161)
)
_JnxProductLineACX710_ObjectIdentity = ObjectIdentity
jnxProductLineACX710 = _JnxProductLineACX710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 162)
)
_JnxProductLineACX5800_ObjectIdentity = ObjectIdentity
jnxProductLineACX5800 = _JnxProductLineACX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 163)
)
_JnxProductLineSRX380_ObjectIdentity = ObjectIdentity
jnxProductLineSRX380 = _JnxProductLineSRX380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 164)
)
_JnxProductLineEX4400_ObjectIdentity = ObjectIdentity
jnxProductLineEX4400 = _JnxProductLineEX4400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 165)
)
_JnxProductLineR6675_ObjectIdentity = ObjectIdentity
jnxProductLineR6675 = _JnxProductLineR6675_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 166)
)
_JnxProductLineMX304_ObjectIdentity = ObjectIdentity
jnxProductLineMX304 = _JnxProductLineMX304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 167)
)
_JnxProductLineMX10004_ObjectIdentity = ObjectIdentity
jnxProductLineMX10004 = _JnxProductLineMX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 168)
)
_JnxProductLineEX4100_ObjectIdentity = ObjectIdentity
jnxProductLineEX4100 = _JnxProductLineEX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 169)
)
_JnxProductLineEX4650_ObjectIdentity = ObjectIdentity
jnxProductLineEX4650 = _JnxProductLineEX4650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 508)
)
_JnxProductLinePTX1000260C_ObjectIdentity = ObjectIdentity
jnxProductLinePTX1000260C = _JnxProductLinePTX1000260C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 513)
)
_JnxProductLinePTX1000380c_ObjectIdentity = ObjectIdentity
jnxProductLinePTX1000380c = _JnxProductLinePTX1000380c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 523)
)
_JnxProductLinePTX10003160c_ObjectIdentity = ObjectIdentity
jnxProductLinePTX10003160c = _JnxProductLinePTX10003160c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 524)
)
_JnxProductLineQFX1000380c_ObjectIdentity = ObjectIdentity
jnxProductLineQFX1000380c = _JnxProductLineQFX1000380c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 525)
)
_JnxProductLineQFX10003160c_ObjectIdentity = ObjectIdentity
jnxProductLineQFX10003160c = _JnxProductLineQFX10003160c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 526)
)
_JnxProductLinePTX1000136mr_ObjectIdentity = ObjectIdentity
jnxProductLinePTX1000136mr = _JnxProductLinePTX1000136mr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 555)
)
_JnxProductLinePTX10004_ObjectIdentity = ObjectIdentity
jnxProductLinePTX10004 = _JnxProductLinePTX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 570)
)
_JnxProductLineACX753_ObjectIdentity = ObjectIdentity
jnxProductLineACX753 = _JnxProductLineACX753_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 576)
)
_JnxProductLineSRX1800_ObjectIdentity = ObjectIdentity
jnxProductLineSRX1800 = _JnxProductLineSRX1800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 577)
)
_JnxProductLineACX7KSwitch_ObjectIdentity = ObjectIdentity
jnxProductLineACX7KSwitch = _JnxProductLineACX7KSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 578)
)
_JnxProductLineACX710032c_ObjectIdentity = ObjectIdentity
jnxProductLineACX710032c = _JnxProductLineACX710032c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 579)
)
_JnxProductLineACX710048l_ObjectIdentity = ObjectIdentity
jnxProductLineACX710048l = _JnxProductLineACX710048l_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 580)
)
_JnxProductLineACX7908_ObjectIdentity = ObjectIdentity
jnxProductLineACX7908 = _JnxProductLineACX7908_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 581)
)
_JnxProductLineACX7024_ObjectIdentity = ObjectIdentity
jnxProductLineACX7024 = _JnxProductLineACX7024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 582)
)
_JnxProductLineSRX1600_ObjectIdentity = ObjectIdentity
jnxProductLineSRX1600 = _JnxProductLineSRX1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 583)
)
_JnxProductLineSRX2300_ObjectIdentity = ObjectIdentity
jnxProductLineSRX2300 = _JnxProductLineSRX2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 584)
)
_JnxProductLineSRX4300_ObjectIdentity = ObjectIdentity
jnxProductLineSRX4300 = _JnxProductLineSRX4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 585)
)
_JnxProductLineACX7332_ObjectIdentity = ObjectIdentity
jnxProductLineACX7332 = _JnxProductLineACX7332_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 586)
)
_JnxProductLineACX7348_ObjectIdentity = ObjectIdentity
jnxProductLineACX7348 = _JnxProductLineACX7348_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 587)
)
_JnxProductLineACX7024X_ObjectIdentity = ObjectIdentity
jnxProductLineACX7024X = _JnxProductLineACX7024X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 588)
)
_JnxProductLinePTX1000236qdd_ObjectIdentity = ObjectIdentity
jnxProductLinePTX1000236qdd = _JnxProductLinePTX1000236qdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 589)
)
_JnxProductLineSRX4700_ObjectIdentity = ObjectIdentity
jnxProductLineSRX4700 = _JnxProductLineSRX4700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 1, 590)
)
_JnxProductName_ObjectIdentity = ObjectIdentity
jnxProductName = _JnxProductName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2)
)
_JnxProductNameM40_ObjectIdentity = ObjectIdentity
jnxProductNameM40 = _JnxProductNameM40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 1)
)
_JnxProductNameM20_ObjectIdentity = ObjectIdentity
jnxProductNameM20 = _JnxProductNameM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 2)
)
_JnxProductNameM160_ObjectIdentity = ObjectIdentity
jnxProductNameM160 = _JnxProductNameM160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 3)
)
_JnxProductNameM10_ObjectIdentity = ObjectIdentity
jnxProductNameM10 = _JnxProductNameM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 4)
)
_JnxProductNameM5_ObjectIdentity = ObjectIdentity
jnxProductNameM5 = _JnxProductNameM5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 5)
)
_JnxProductNameT640_ObjectIdentity = ObjectIdentity
jnxProductNameT640 = _JnxProductNameT640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 6)
)
_JnxProductNameT320_ObjectIdentity = ObjectIdentity
jnxProductNameT320 = _JnxProductNameT320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 7)
)
_JnxProductNameM40e_ObjectIdentity = ObjectIdentity
jnxProductNameM40e = _JnxProductNameM40e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 8)
)
_JnxProductNameM320_ObjectIdentity = ObjectIdentity
jnxProductNameM320 = _JnxProductNameM320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 9)
)
_JnxProductNameM7i_ObjectIdentity = ObjectIdentity
jnxProductNameM7i = _JnxProductNameM7i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 10)
)
_JnxProductNameM10i_ObjectIdentity = ObjectIdentity
jnxProductNameM10i = _JnxProductNameM10i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 11)
)
_JnxProductNameJ2300_ObjectIdentity = ObjectIdentity
jnxProductNameJ2300 = _JnxProductNameJ2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 13)
)
_JnxProductNameJ4300_ObjectIdentity = ObjectIdentity
jnxProductNameJ4300 = _JnxProductNameJ4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 14)
)
_JnxProductNameJ6300_ObjectIdentity = ObjectIdentity
jnxProductNameJ6300 = _JnxProductNameJ6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 15)
)
_JnxProductNameIRM_ObjectIdentity = ObjectIdentity
jnxProductNameIRM = _JnxProductNameIRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 16)
)
_JnxProductNameTX_ObjectIdentity = ObjectIdentity
jnxProductNameTX = _JnxProductNameTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 17)
)
_JnxProductNameM120_ObjectIdentity = ObjectIdentity
jnxProductNameM120 = _JnxProductNameM120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 18)
)
_JnxProductNameJ4350_ObjectIdentity = ObjectIdentity
jnxProductNameJ4350 = _JnxProductNameJ4350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 19)
)
_JnxProductNameJ6350_ObjectIdentity = ObjectIdentity
jnxProductNameJ6350 = _JnxProductNameJ6350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 20)
)
_JnxProductNameMX960_ObjectIdentity = ObjectIdentity
jnxProductNameMX960 = _JnxProductNameMX960_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 21)
)
_JnxProductNameJ4320_ObjectIdentity = ObjectIdentity
jnxProductNameJ4320 = _JnxProductNameJ4320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 22)
)
_JnxProductNameJ2320_ObjectIdentity = ObjectIdentity
jnxProductNameJ2320 = _JnxProductNameJ2320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 23)
)
_JnxProductNameJ2350_ObjectIdentity = ObjectIdentity
jnxProductNameJ2350 = _JnxProductNameJ2350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 24)
)
_JnxProductNameMX480_ObjectIdentity = ObjectIdentity
jnxProductNameMX480 = _JnxProductNameMX480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 25)
)
_JnxProductNameSRX5800_ObjectIdentity = ObjectIdentity
jnxProductNameSRX5800 = _JnxProductNameSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 26)
)
_JnxProductNameT1600_ObjectIdentity = ObjectIdentity
jnxProductNameT1600 = _JnxProductNameT1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 27)
)
_JnxProductNameSRX5600_ObjectIdentity = ObjectIdentity
jnxProductNameSRX5600 = _JnxProductNameSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 28)
)
_JnxProductNameMX240_ObjectIdentity = ObjectIdentity
jnxProductNameMX240 = _JnxProductNameMX240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 29)
)
_JnxProductNameEX3200_ObjectIdentity = ObjectIdentity
jnxProductNameEX3200 = _JnxProductNameEX3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 30)
)
_JnxProductNameEX4200_ObjectIdentity = ObjectIdentity
jnxProductNameEX4200 = _JnxProductNameEX4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 31)
)
_JnxProductNameEX8208_ObjectIdentity = ObjectIdentity
jnxProductNameEX8208 = _JnxProductNameEX8208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 32)
)
_JnxProductNameEX8216_ObjectIdentity = ObjectIdentity
jnxProductNameEX8216 = _JnxProductNameEX8216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 33)
)
_JnxProductNameSRX3600_ObjectIdentity = ObjectIdentity
jnxProductNameSRX3600 = _JnxProductNameSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 34)
)
_JnxProductNameSRX3400_ObjectIdentity = ObjectIdentity
jnxProductNameSRX3400 = _JnxProductNameSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 35)
)
_JnxProductNameSRX210_ObjectIdentity = ObjectIdentity
jnxProductNameSRX210 = _JnxProductNameSRX210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 36)
)
_JnxProductNameTXP_ObjectIdentity = ObjectIdentity
jnxProductNameTXP = _JnxProductNameTXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 37)
)
_JnxProductNameJCS_ObjectIdentity = ObjectIdentity
jnxProductNameJCS = _JnxProductNameJCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 38)
)
_JnxProductNameSRX240_ObjectIdentity = ObjectIdentity
jnxProductNameSRX240 = _JnxProductNameSRX240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 39)
)
_JnxProductNameSRX650_ObjectIdentity = ObjectIdentity
jnxProductNameSRX650 = _JnxProductNameSRX650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 40)
)
_JnxProductNameSRX100_ObjectIdentity = ObjectIdentity
jnxProductNameSRX100 = _JnxProductNameSRX100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 41)
)
_JnxProductNameLN1000V_ObjectIdentity = ObjectIdentity
jnxProductNameLN1000V = _JnxProductNameLN1000V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 42)
)
_JnxProductNameEX2200_ObjectIdentity = ObjectIdentity
jnxProductNameEX2200 = _JnxProductNameEX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 43)
)
_JnxProductNameEX4500_ObjectIdentity = ObjectIdentity
jnxProductNameEX4500 = _JnxProductNameEX4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 44)
)
_JnxProductNameFXSeries_ObjectIdentity = ObjectIdentity
jnxProductNameFXSeries = _JnxProductNameFXSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 45)
)
_JnxProductNameIBM4274M02J02M_ObjectIdentity = ObjectIdentity
jnxProductNameIBM4274M02J02M = _JnxProductNameIBM4274M02J02M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 46)
)
_JnxProductNameIBM4274M06J06M_ObjectIdentity = ObjectIdentity
jnxProductNameIBM4274M06J06M = _JnxProductNameIBM4274M06J06M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 47)
)
_JnxProductNameIBM4274M11J11M_ObjectIdentity = ObjectIdentity
jnxProductNameIBM4274M11J11M = _JnxProductNameIBM4274M11J11M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 48)
)
_JnxProductNameSRX1400_ObjectIdentity = ObjectIdentity
jnxProductNameSRX1400 = _JnxProductNameSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 49)
)
_JnxProductNameIBM4274S58J58S_ObjectIdentity = ObjectIdentity
jnxProductNameIBM4274S58J58S = _JnxProductNameIBM4274S58J58S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 50)
)
_JnxProductNameIBM4274S56J56S_ObjectIdentity = ObjectIdentity
jnxProductNameIBM4274S56J56S = _JnxProductNameIBM4274S56J56S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 51)
)
_JnxProductNameIBM4274S36J36S_ObjectIdentity = ObjectIdentity
jnxProductNameIBM4274S36J36S = _JnxProductNameIBM4274S36J36S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 52)
)
_JnxProductNameIBM4274S34J34S_ObjectIdentity = ObjectIdentity
jnxProductNameIBM4274S34J34S = _JnxProductNameIBM4274S34J34S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 53)
)
_JnxProductNameIBM427348EJ48E_ObjectIdentity = ObjectIdentity
jnxProductNameIBM427348EJ48E = _JnxProductNameIBM427348EJ48E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 54)
)
_JnxProductNameIBM4274E08J08E_ObjectIdentity = ObjectIdentity
jnxProductNameIBM4274E08J08E = _JnxProductNameIBM4274E08J08E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 55)
)
_JnxProductNameIBM4274E16J16E_ObjectIdentity = ObjectIdentity
jnxProductNameIBM4274E16J16E = _JnxProductNameIBM4274E16J16E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 56)
)
_JnxProductNameMX80_ObjectIdentity = ObjectIdentity
jnxProductNameMX80 = _JnxProductNameMX80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 57)
)
_JnxProductNameSRX220_ObjectIdentity = ObjectIdentity
jnxProductNameSRX220 = _JnxProductNameSRX220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 58)
)
_JnxProductNameEXXRE_ObjectIdentity = ObjectIdentity
jnxProductNameEXXRE = _JnxProductNameEXXRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 59)
)
_JnxProductNameQFXInterconnect_ObjectIdentity = ObjectIdentity
jnxProductNameQFXInterconnect = _JnxProductNameQFXInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 60)
)
_JnxProductNameQFXNode_ObjectIdentity = ObjectIdentity
jnxProductNameQFXNode = _JnxProductNameQFXNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 61)
)
_JnxProductNameQFXJVRE_ObjectIdentity = ObjectIdentity
jnxProductNameQFXJVRE = _JnxProductNameQFXJVRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 62)
)
_JnxProductNameEX4300_ObjectIdentity = ObjectIdentity
jnxProductNameEX4300 = _JnxProductNameEX4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 63)
)
_JnxProductNameSRX110_ObjectIdentity = ObjectIdentity
jnxProductNameSRX110 = _JnxProductNameSRX110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 64)
)
_JnxProductNameSRX120_ObjectIdentity = ObjectIdentity
jnxProductNameSRX120 = _JnxProductNameSRX120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 65)
)
_JnxProductNameMAG8600_ObjectIdentity = ObjectIdentity
jnxProductNameMAG8600 = _JnxProductNameMAG8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 66)
)
_JnxProductNameMAG6611_ObjectIdentity = ObjectIdentity
jnxProductNameMAG6611 = _JnxProductNameMAG6611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 67)
)
_JnxProductNameMAG6610_ObjectIdentity = ObjectIdentity
jnxProductNameMAG6610 = _JnxProductNameMAG6610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 68)
)
_JnxProductNamePTX5000_ObjectIdentity = ObjectIdentity
jnxProductNamePTX5000 = _JnxProductNamePTX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 69)
)
_JnxProductNameIBM0719J45E_ObjectIdentity = ObjectIdentity
jnxProductNameIBM0719J45E = _JnxProductNameIBM0719J45E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 71)
)
_JnxProductNameIBMJ08F_ObjectIdentity = ObjectIdentity
jnxProductNameIBMJ08F = _JnxProductNameIBMJ08F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 72)
)
_JnxProductNameIBMJ52F_ObjectIdentity = ObjectIdentity
jnxProductNameIBMJ52F = _JnxProductNameIBMJ52F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 73)
)
_JnxProductNameEX6210_ObjectIdentity = ObjectIdentity
jnxProductNameEX6210 = _JnxProductNameEX6210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 74)
)
_JnxProductNameDellJFX3500_ObjectIdentity = ObjectIdentity
jnxProductNameDellJFX3500 = _JnxProductNameDellJFX3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 75)
)
_JnxProductNameEX3300_ObjectIdentity = ObjectIdentity
jnxProductNameEX3300 = _JnxProductNameEX3300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 76)
)
_JnxProductNameDELLJSRX3600_ObjectIdentity = ObjectIdentity
jnxProductNameDELLJSRX3600 = _JnxProductNameDELLJSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 77)
)
_JnxProductNameDELLJSRX3400_ObjectIdentity = ObjectIdentity
jnxProductNameDELLJSRX3400 = _JnxProductNameDELLJSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 78)
)
_JnxProductNameDELLJSRX1400_ObjectIdentity = ObjectIdentity
jnxProductNameDELLJSRX1400 = _JnxProductNameDELLJSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 79)
)
_JnxProductNameDELLJSRX5800_ObjectIdentity = ObjectIdentity
jnxProductNameDELLJSRX5800 = _JnxProductNameDELLJSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 80)
)
_JnxProductNameDELLJSRX5600_ObjectIdentity = ObjectIdentity
jnxProductNameDELLJSRX5600 = _JnxProductNameDELLJSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 81)
)
_JnxProductNameQFXSwitch_ObjectIdentity = ObjectIdentity
jnxProductNameQFXSwitch = _JnxProductNameQFXSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 82)
)
_JnxProductNameT4000_ObjectIdentity = ObjectIdentity
jnxProductNameT4000 = _JnxProductNameT4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 83)
)
_JnxProductNameQFX3000_ObjectIdentity = ObjectIdentity
jnxProductNameQFX3000 = _JnxProductNameQFX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 84)
)
_JnxProductNameQFX5000_ObjectIdentity = ObjectIdentity
jnxProductNameQFX5000 = _JnxProductNameQFX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 85)
)
_JnxProductNameSRX550_ObjectIdentity = ObjectIdentity
jnxProductNameSRX550 = _JnxProductNameSRX550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 86)
)
_JnxProductNameACX_ObjectIdentity = ObjectIdentity
jnxProductNameACX = _JnxProductNameACX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 87)
)
_JnxProductNameMX40_ObjectIdentity = ObjectIdentity
jnxProductNameMX40 = _JnxProductNameMX40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 88)
)
_JnxProductNameMX10_ObjectIdentity = ObjectIdentity
jnxProductNameMX10 = _JnxProductNameMX10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 89)
)
_JnxProductNameMX5_ObjectIdentity = ObjectIdentity
jnxProductNameMX5 = _JnxProductNameMX5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 90)
)
_JnxProductNameQFXMInterconnect_ObjectIdentity = ObjectIdentity
jnxProductNameQFXMInterconnect = _JnxProductNameQFXMInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 91)
)
_JnxProductNameEX4550_ObjectIdentity = ObjectIdentity
jnxProductNameEX4550 = _JnxProductNameEX4550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 92)
)
_JnxProductNameMX2020_ObjectIdentity = ObjectIdentity
jnxProductNameMX2020 = _JnxProductNameMX2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 93)
)
_JnxProductNameVseries_ObjectIdentity = ObjectIdentity
jnxProductNameVseries = _JnxProductNameVseries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 94)
)
_JnxProductNameLN2600_ObjectIdentity = ObjectIdentity
jnxProductNameLN2600 = _JnxProductNameLN2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 95)
)
_JnxProductNameFireflyPerimeter_ObjectIdentity = ObjectIdentity
jnxProductNameFireflyPerimeter = _JnxProductNameFireflyPerimeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 96)
)
_JnxProductNameMX104_ObjectIdentity = ObjectIdentity
jnxProductNameMX104 = _JnxProductNameMX104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 97)
)
_JnxProductNamePTX3000_ObjectIdentity = ObjectIdentity
jnxProductNamePTX3000 = _JnxProductNamePTX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 98)
)
_JnxProductNameMX2010_ObjectIdentity = ObjectIdentity
jnxProductNameMX2010 = _JnxProductNameMX2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 99)
)
_JnxProductNameQFX3100_ObjectIdentity = ObjectIdentity
jnxProductNameQFX3100 = _JnxProductNameQFX3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 100)
)
_JnxProductNameLN2800_ObjectIdentity = ObjectIdentity
jnxProductNameLN2800 = _JnxProductNameLN2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 101)
)
_JnxProductNameEX9214_ObjectIdentity = ObjectIdentity
jnxProductNameEX9214 = _JnxProductNameEX9214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 102)
)
_JnxProductNameEX9208_ObjectIdentity = ObjectIdentity
jnxProductNameEX9208 = _JnxProductNameEX9208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 103)
)
_JnxProductNameEX9204_ObjectIdentity = ObjectIdentity
jnxProductNameEX9204 = _JnxProductNameEX9204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 104)
)
_JnxProductNameSRX5400_ObjectIdentity = ObjectIdentity
jnxProductNameSRX5400 = _JnxProductNameSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 105)
)
_JnxProductNameIBM4274S54J54S_ObjectIdentity = ObjectIdentity
jnxProductNameIBM4274S54J54S = _JnxProductNameIBM4274S54J54S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 106)
)
_JnxProductNameDELLJSRX5400_ObjectIdentity = ObjectIdentity
jnxProductNameDELLJSRX5400 = _JnxProductNameDELLJSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 107)
)
_JnxProductNameVMX_ObjectIdentity = ObjectIdentity
jnxProductNameVMX = _JnxProductNameVMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 108)
)
_JnxProductNameEX4600_ObjectIdentity = ObjectIdentity
jnxProductNameEX4600 = _JnxProductNameEX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 109)
)
_JnxProductNameVRR_ObjectIdentity = ObjectIdentity
jnxProductNameVRR = _JnxProductNameVRR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 110)
)
_JnxProductNameMX10440G_ObjectIdentity = ObjectIdentity
jnxProductNameMX10440G = _JnxProductNameMX10440G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 111)
)
_JnxProductNameOCPAcc_ObjectIdentity = ObjectIdentity
jnxProductNameOCPAcc = _JnxProductNameOCPAcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 112)
)
_JnxProductNameACX1000_ObjectIdentity = ObjectIdentity
jnxProductNameACX1000 = _JnxProductNameACX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 113)
)
_JnxProductNameACX2000_ObjectIdentity = ObjectIdentity
jnxProductNameACX2000 = _JnxProductNameACX2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 114)
)
_JnxProductNameACX1100_ObjectIdentity = ObjectIdentity
jnxProductNameACX1100 = _JnxProductNameACX1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 115)
)
_JnxProductNameACX2100_ObjectIdentity = ObjectIdentity
jnxProductNameACX2100 = _JnxProductNameACX2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 116)
)
_JnxProductNameACX2200_ObjectIdentity = ObjectIdentity
jnxProductNameACX2200 = _JnxProductNameACX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 117)
)
_JnxProductNameACX4000_ObjectIdentity = ObjectIdentity
jnxProductNameACX4000 = _JnxProductNameACX4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 118)
)
_JnxProductNameACX500AC_ObjectIdentity = ObjectIdentity
jnxProductNameACX500AC = _JnxProductNameACX500AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 119)
)
_JnxProductNameACX500DC_ObjectIdentity = ObjectIdentity
jnxProductNameACX500DC = _JnxProductNameACX500DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 120)
)
_JnxProductNameACX500OAC_ObjectIdentity = ObjectIdentity
jnxProductNameACX500OAC = _JnxProductNameACX500OAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 121)
)
_JnxProductNameACX500ODC_ObjectIdentity = ObjectIdentity
jnxProductNameACX500ODC = _JnxProductNameACX500ODC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 122)
)
_JnxProductNameACX500OPOEAC_ObjectIdentity = ObjectIdentity
jnxProductNameACX500OPOEAC = _JnxProductNameACX500OPOEAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 123)
)
_JnxProductNameACX500OPOEDC_ObjectIdentity = ObjectIdentity
jnxProductNameACX500OPOEDC = _JnxProductNameACX500OPOEDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 124)
)
_JnxProductNameSatelliteDevice_ObjectIdentity = ObjectIdentity
jnxProductNameSatelliteDevice = _JnxProductNameSatelliteDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 125)
)
_JnxProductNameACX5048_ObjectIdentity = ObjectIdentity
jnxProductNameACX5048 = _JnxProductNameACX5048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 126)
)
_JnxProductNameACX5096_ObjectIdentity = ObjectIdentity
jnxProductNameACX5096 = _JnxProductNameACX5096_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 127)
)
_JnxProductNameLN1000CC_ObjectIdentity = ObjectIdentity
jnxProductNameLN1000CC = _JnxProductNameLN1000CC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 128)
)
_JnxProductNameVSRX_ObjectIdentity = ObjectIdentity
jnxProductNameVSRX = _JnxProductNameVSRX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 129)
)
_JnxProductNamePTX1000_ObjectIdentity = ObjectIdentity
jnxProductNamePTX1000 = _JnxProductNamePTX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 130)
)
_JnxProductNameEX3400_ObjectIdentity = ObjectIdentity
jnxProductNameEX3400 = _JnxProductNameEX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 131)
)
_JnxProductNameEX2300_ObjectIdentity = ObjectIdentity
jnxProductNameEX2300 = _JnxProductNameEX2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 132)
)
_JnxProductNameSRX300_ObjectIdentity = ObjectIdentity
jnxProductNameSRX300 = _JnxProductNameSRX300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 133)
)
_JnxProductNameSRX320_ObjectIdentity = ObjectIdentity
jnxProductNameSRX320 = _JnxProductNameSRX320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 134)
)
_JnxProductNameSRX340_ObjectIdentity = ObjectIdentity
jnxProductNameSRX340 = _JnxProductNameSRX340_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 135)
)
_JnxProductNameSRX345_ObjectIdentity = ObjectIdentity
jnxProductNameSRX345 = _JnxProductNameSRX345_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 136)
)
_JnxProductNameSRX1500_ObjectIdentity = ObjectIdentity
jnxProductNameSRX1500 = _JnxProductNameSRX1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 137)
)
_JnxProductNameNFX_ObjectIdentity = ObjectIdentity
jnxProductNameNFX = _JnxProductNameNFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 138)
)
_JnxProductNameJNP10003_ObjectIdentity = ObjectIdentity
jnxProductNameJNP10003 = _JnxProductNameJNP10003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 139)
)
_JnxProductNameSRX4600_ObjectIdentity = ObjectIdentity
jnxProductNameSRX4600 = _JnxProductNameSRX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 140)
)
_JnxProductNameSRX4800_ObjectIdentity = ObjectIdentity
jnxProductNameSRX4800 = _JnxProductNameSRX4800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 141)
)
_JnxProductNameSRX4100_ObjectIdentity = ObjectIdentity
jnxProductNameSRX4100 = _JnxProductNameSRX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 142)
)
_JnxProductNameSRX4200_ObjectIdentity = ObjectIdentity
jnxProductNameSRX4200 = _JnxProductNameSRX4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 143)
)
_JnxProductNameJNP204_ObjectIdentity = ObjectIdentity
jnxProductNameJNP204 = _JnxProductNameJNP204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 144)
)
_JnxProductNameMX2008_ObjectIdentity = ObjectIdentity
jnxProductNameMX2008 = _JnxProductNameMX2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 145)
)
_JnxProductNameMXTSR80_ObjectIdentity = ObjectIdentity
jnxProductNameMXTSR80 = _JnxProductNameMXTSR80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 146)
)
_JnxProductNamePTX10008_ObjectIdentity = ObjectIdentity
jnxProductNamePTX10008 = _JnxProductNamePTX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 147)
)
_JnxProductNameACX5448_ObjectIdentity = ObjectIdentity
jnxProductNameACX5448 = _JnxProductNameACX5448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 148)
)
_JnxProductNamePTX10016_ObjectIdentity = ObjectIdentity
jnxProductNamePTX10016 = _JnxProductNamePTX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 150)
)
_JnxProductNameEX9251_ObjectIdentity = ObjectIdentity
jnxProductNameEX9251 = _JnxProductNameEX9251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 151)
)
_JnxProductNameMX150_ObjectIdentity = ObjectIdentity
jnxProductNameMX150 = _JnxProductNameMX150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 152)
)
_JnxProductNameJNP10001_ObjectIdentity = ObjectIdentity
jnxProductNameJNP10001 = _JnxProductNameJNP10001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 153)
)
_JnxProductNameMX10008_ObjectIdentity = ObjectIdentity
jnxProductNameMX10008 = _JnxProductNameMX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 154)
)
_JnxProductNameMX10016_ObjectIdentity = ObjectIdentity
jnxProductNameMX10016 = _JnxProductNameMX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 155)
)
_JnxProductNameEX9253_ObjectIdentity = ObjectIdentity
jnxProductNameEX9253 = _JnxProductNameEX9253_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 156)
)
_JnxProductNameJRR200_ObjectIdentity = ObjectIdentity
jnxProductNameJRR200 = _JnxProductNameJRR200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 157)
)
_JnxProductNameACX5448M_ObjectIdentity = ObjectIdentity
jnxProductNameACX5448M = _JnxProductNameACX5448M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 158)
)
_JnxProductNameACX5448D_ObjectIdentity = ObjectIdentity
jnxProductNameACX5448D = _JnxProductNameACX5448D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 159)
)
_JnxProductNameACX6360OR_ObjectIdentity = ObjectIdentity
jnxProductNameACX6360OR = _JnxProductNameACX6360OR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 160)
)
_JnxProductNameACX6360OX_ObjectIdentity = ObjectIdentity
jnxProductNameACX6360OX = _JnxProductNameACX6360OX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 161)
)
_JnxProductNameACX710_ObjectIdentity = ObjectIdentity
jnxProductNameACX710 = _JnxProductNameACX710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 162)
)
_JnxProductNameACX5800_ObjectIdentity = ObjectIdentity
jnxProductNameACX5800 = _JnxProductNameACX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 163)
)
_JnxProductNameSRX380_ObjectIdentity = ObjectIdentity
jnxProductNameSRX380 = _JnxProductNameSRX380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 164)
)
_JnxProductNameEX4400_ObjectIdentity = ObjectIdentity
jnxProductNameEX4400 = _JnxProductNameEX4400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 165)
)
_JnxProductNameR6675_ObjectIdentity = ObjectIdentity
jnxProductNameR6675 = _JnxProductNameR6675_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 166)
)
_JnxProductNameMX304_ObjectIdentity = ObjectIdentity
jnxProductNameMX304 = _JnxProductNameMX304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 167)
)
_JnxProductNameMX10004_ObjectIdentity = ObjectIdentity
jnxProductNameMX10004 = _JnxProductNameMX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 168)
)
_JnxProductNameEX4100_ObjectIdentity = ObjectIdentity
jnxProductNameEX4100 = _JnxProductNameEX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 169)
)
_JnxProductNameEX4650_ObjectIdentity = ObjectIdentity
jnxProductNameEX4650 = _JnxProductNameEX4650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 508)
)
_JnxProductNamePTX1000260C_ObjectIdentity = ObjectIdentity
jnxProductNamePTX1000260C = _JnxProductNamePTX1000260C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 513)
)
_JnxProductNamePTX1000380c_ObjectIdentity = ObjectIdentity
jnxProductNamePTX1000380c = _JnxProductNamePTX1000380c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 523)
)
_JnxProductNamePTX10003160c_ObjectIdentity = ObjectIdentity
jnxProductNamePTX10003160c = _JnxProductNamePTX10003160c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 524)
)
_JnxProductNameQFX1000380c_ObjectIdentity = ObjectIdentity
jnxProductNameQFX1000380c = _JnxProductNameQFX1000380c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 525)
)
_JnxProductNameQFX10003160c_ObjectIdentity = ObjectIdentity
jnxProductNameQFX10003160c = _JnxProductNameQFX10003160c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 526)
)
_JnxProductNamePTX1000136mr_ObjectIdentity = ObjectIdentity
jnxProductNamePTX1000136mr = _JnxProductNamePTX1000136mr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 555)
)
_JnxProductNamePTX10004_ObjectIdentity = ObjectIdentity
jnxProductNamePTX10004 = _JnxProductNamePTX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 570)
)
_JnxProductNameACX753_ObjectIdentity = ObjectIdentity
jnxProductNameACX753 = _JnxProductNameACX753_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 576)
)
_JnxProductNameSRX1800_ObjectIdentity = ObjectIdentity
jnxProductNameSRX1800 = _JnxProductNameSRX1800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 577)
)
_JnxProductNameACX7KSwitch_ObjectIdentity = ObjectIdentity
jnxProductNameACX7KSwitch = _JnxProductNameACX7KSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 578)
)
_JnxProductNameACX710032c_ObjectIdentity = ObjectIdentity
jnxProductNameACX710032c = _JnxProductNameACX710032c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 579)
)
_JnxProductNameACX710048l_ObjectIdentity = ObjectIdentity
jnxProductNameACX710048l = _JnxProductNameACX710048l_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 580)
)
_JnxProductNameACX7908_ObjectIdentity = ObjectIdentity
jnxProductNameACX7908 = _JnxProductNameACX7908_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 581)
)
_JnxProductNameACX7024_ObjectIdentity = ObjectIdentity
jnxProductNameACX7024 = _JnxProductNameACX7024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 582)
)
_JnxProductNameSRX1600_ObjectIdentity = ObjectIdentity
jnxProductNameSRX1600 = _JnxProductNameSRX1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 583)
)
_JnxProductNameSRX2300_ObjectIdentity = ObjectIdentity
jnxProductNameSRX2300 = _JnxProductNameSRX2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 584)
)
_JnxProductNameSRX4300_ObjectIdentity = ObjectIdentity
jnxProductNameSRX4300 = _JnxProductNameSRX4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 585)
)
_JnxProductNameACX7332_ObjectIdentity = ObjectIdentity
jnxProductNameACX7332 = _JnxProductNameACX7332_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 586)
)
_JnxProductNameACX7348_ObjectIdentity = ObjectIdentity
jnxProductNameACX7348 = _JnxProductNameACX7348_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 587)
)
_JnxProductNameACX7024X_ObjectIdentity = ObjectIdentity
jnxProductNameACX7024X = _JnxProductNameACX7024X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 588)
)
_JnxProductNamePTX1000236qdd_ObjectIdentity = ObjectIdentity
jnxProductNamePTX1000236qdd = _JnxProductNamePTX1000236qdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 589)
)
_JnxProductNameSRX4700_ObjectIdentity = ObjectIdentity
jnxProductNameSRX4700 = _JnxProductNameSRX4700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 2, 590)
)
_JnxProductModel_ObjectIdentity = ObjectIdentity
jnxProductModel = _JnxProductModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3)
)
_JnxProductModelM40_ObjectIdentity = ObjectIdentity
jnxProductModelM40 = _JnxProductModelM40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 1)
)
_JnxProductModelM20_ObjectIdentity = ObjectIdentity
jnxProductModelM20 = _JnxProductModelM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 2)
)
_JnxProductModelM160_ObjectIdentity = ObjectIdentity
jnxProductModelM160 = _JnxProductModelM160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 3)
)
_JnxProductModelM10_ObjectIdentity = ObjectIdentity
jnxProductModelM10 = _JnxProductModelM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 4)
)
_JnxProductModelM5_ObjectIdentity = ObjectIdentity
jnxProductModelM5 = _JnxProductModelM5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 5)
)
_JnxProductModelT640_ObjectIdentity = ObjectIdentity
jnxProductModelT640 = _JnxProductModelT640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 6)
)
_JnxProductModelT320_ObjectIdentity = ObjectIdentity
jnxProductModelT320 = _JnxProductModelT320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 7)
)
_JnxProductModelM40e_ObjectIdentity = ObjectIdentity
jnxProductModelM40e = _JnxProductModelM40e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 8)
)
_JnxProductModelM320_ObjectIdentity = ObjectIdentity
jnxProductModelM320 = _JnxProductModelM320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 9)
)
_JnxProductModelM7i_ObjectIdentity = ObjectIdentity
jnxProductModelM7i = _JnxProductModelM7i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 10)
)
_JnxProductModelM10i_ObjectIdentity = ObjectIdentity
jnxProductModelM10i = _JnxProductModelM10i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 11)
)
_JnxProductModelIRM_ObjectIdentity = ObjectIdentity
jnxProductModelIRM = _JnxProductModelIRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 16)
)
_JnxProductModelTX_ObjectIdentity = ObjectIdentity
jnxProductModelTX = _JnxProductModelTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 17)
)
_JnxProductModelM120_ObjectIdentity = ObjectIdentity
jnxProductModelM120 = _JnxProductModelM120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 18)
)
_JnxProductModelMX960_ObjectIdentity = ObjectIdentity
jnxProductModelMX960 = _JnxProductModelMX960_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 21)
)
_JnxProductModelMX480_ObjectIdentity = ObjectIdentity
jnxProductModelMX480 = _JnxProductModelMX480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 25)
)
_JnxProductModelSRX5800_ObjectIdentity = ObjectIdentity
jnxProductModelSRX5800 = _JnxProductModelSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 26)
)
_JnxProductModelT1600_ObjectIdentity = ObjectIdentity
jnxProductModelT1600 = _JnxProductModelT1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 27)
)
_JnxProductModelSRX5600_ObjectIdentity = ObjectIdentity
jnxProductModelSRX5600 = _JnxProductModelSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 28)
)
_JnxProductModelMX240_ObjectIdentity = ObjectIdentity
jnxProductModelMX240 = _JnxProductModelMX240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 29)
)
_JnxProductModelEX3200_ObjectIdentity = ObjectIdentity
jnxProductModelEX3200 = _JnxProductModelEX3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 30)
)
_JnxProductModelEX4200_ObjectIdentity = ObjectIdentity
jnxProductModelEX4200 = _JnxProductModelEX4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 31)
)
_JnxProductModelEX8208_ObjectIdentity = ObjectIdentity
jnxProductModelEX8208 = _JnxProductModelEX8208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 32)
)
_JnxProductModelEX8216_ObjectIdentity = ObjectIdentity
jnxProductModelEX8216 = _JnxProductModelEX8216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 33)
)
_JnxProductModelSRX3600_ObjectIdentity = ObjectIdentity
jnxProductModelSRX3600 = _JnxProductModelSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 34)
)
_JnxProductModelSRX3400_ObjectIdentity = ObjectIdentity
jnxProductModelSRX3400 = _JnxProductModelSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 35)
)
_JnxProductModelTXP_ObjectIdentity = ObjectIdentity
jnxProductModelTXP = _JnxProductModelTXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 37)
)
_JnxProductModelJCS_ObjectIdentity = ObjectIdentity
jnxProductModelJCS = _JnxProductModelJCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 38)
)
_JnxProductModelLN1000V_ObjectIdentity = ObjectIdentity
jnxProductModelLN1000V = _JnxProductModelLN1000V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 42)
)
_JnxProductModelEX2200_ObjectIdentity = ObjectIdentity
jnxProductModelEX2200 = _JnxProductModelEX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 43)
)
_JnxProductModelEX4500_ObjectIdentity = ObjectIdentity
jnxProductModelEX4500 = _JnxProductModelEX4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 44)
)
_JnxProductModelFXSeries_ObjectIdentity = ObjectIdentity
jnxProductModelFXSeries = _JnxProductModelFXSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 45)
)
_JnxProductModelIBM4274M02J02M_ObjectIdentity = ObjectIdentity
jnxProductModelIBM4274M02J02M = _JnxProductModelIBM4274M02J02M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 46)
)
_JnxProductModelIBM4274M06J06M_ObjectIdentity = ObjectIdentity
jnxProductModelIBM4274M06J06M = _JnxProductModelIBM4274M06J06M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 47)
)
_JnxProductModelIBM4274M11J11M_ObjectIdentity = ObjectIdentity
jnxProductModelIBM4274M11J11M = _JnxProductModelIBM4274M11J11M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 48)
)
_JnxProductModelSRX1400_ObjectIdentity = ObjectIdentity
jnxProductModelSRX1400 = _JnxProductModelSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 49)
)
_JnxProductModelIBM4274S58J58S_ObjectIdentity = ObjectIdentity
jnxProductModelIBM4274S58J58S = _JnxProductModelIBM4274S58J58S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 50)
)
_JnxProductModelIBM4274S56J56S_ObjectIdentity = ObjectIdentity
jnxProductModelIBM4274S56J56S = _JnxProductModelIBM4274S56J56S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 51)
)
_JnxProductModelIBM4274S36J36S_ObjectIdentity = ObjectIdentity
jnxProductModelIBM4274S36J36S = _JnxProductModelIBM4274S36J36S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 52)
)
_JnxProductModelIBM4274S34J34S_ObjectIdentity = ObjectIdentity
jnxProductModelIBM4274S34J34S = _JnxProductModelIBM4274S34J34S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 53)
)
_JnxProductModelIBM427348EJ48E_ObjectIdentity = ObjectIdentity
jnxProductModelIBM427348EJ48E = _JnxProductModelIBM427348EJ48E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 54)
)
_JnxProductModelIBM4274E08J08E_ObjectIdentity = ObjectIdentity
jnxProductModelIBM4274E08J08E = _JnxProductModelIBM4274E08J08E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 55)
)
_JnxProductModelIBM4274E16J16E_ObjectIdentity = ObjectIdentity
jnxProductModelIBM4274E16J16E = _JnxProductModelIBM4274E16J16E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 56)
)
_JnxProductModelMX80_ObjectIdentity = ObjectIdentity
jnxProductModelMX80 = _JnxProductModelMX80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 57)
)
_JnxProductModelEXXRE_ObjectIdentity = ObjectIdentity
jnxProductModelEXXRE = _JnxProductModelEXXRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 59)
)
_JnxProductModelQFXInterconnect_ObjectIdentity = ObjectIdentity
jnxProductModelQFXInterconnect = _JnxProductModelQFXInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 60)
)
_JnxProductModelQFXNode_ObjectIdentity = ObjectIdentity
jnxProductModelQFXNode = _JnxProductModelQFXNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 61)
)
_JnxProductModelQFXJVRE_ObjectIdentity = ObjectIdentity
jnxProductModelQFXJVRE = _JnxProductModelQFXJVRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 62)
)
_JnxProductModelEX4300_ObjectIdentity = ObjectIdentity
jnxProductModelEX4300 = _JnxProductModelEX4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 63)
)
_JnxProductModelMAG8600_ObjectIdentity = ObjectIdentity
jnxProductModelMAG8600 = _JnxProductModelMAG8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 66)
)
_JnxProductModelMAG6611_ObjectIdentity = ObjectIdentity
jnxProductModelMAG6611 = _JnxProductModelMAG6611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 67)
)
_JnxProductModelMAG6610_ObjectIdentity = ObjectIdentity
jnxProductModelMAG6610 = _JnxProductModelMAG6610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 68)
)
_JnxProductModelPTX5000_ObjectIdentity = ObjectIdentity
jnxProductModelPTX5000 = _JnxProductModelPTX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 69)
)
_JnxProductModelIBM0719J45E_ObjectIdentity = ObjectIdentity
jnxProductModelIBM0719J45E = _JnxProductModelIBM0719J45E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 71)
)
_JnxProductModelIBMJ08F_ObjectIdentity = ObjectIdentity
jnxProductModelIBMJ08F = _JnxProductModelIBMJ08F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 72)
)
_JnxProductModelIBMJ52F_ObjectIdentity = ObjectIdentity
jnxProductModelIBMJ52F = _JnxProductModelIBMJ52F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 73)
)
_JnxProductModelEX6210_ObjectIdentity = ObjectIdentity
jnxProductModelEX6210 = _JnxProductModelEX6210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 74)
)
_JnxProductModelDellJFX3500_ObjectIdentity = ObjectIdentity
jnxProductModelDellJFX3500 = _JnxProductModelDellJFX3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 75)
)
_JnxProductModelEX3300_ObjectIdentity = ObjectIdentity
jnxProductModelEX3300 = _JnxProductModelEX3300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 76)
)
_JnxProductModelDELLJSRX3600_ObjectIdentity = ObjectIdentity
jnxProductModelDELLJSRX3600 = _JnxProductModelDELLJSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 77)
)
_JnxProductModelDELLJSRX3400_ObjectIdentity = ObjectIdentity
jnxProductModelDELLJSRX3400 = _JnxProductModelDELLJSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 78)
)
_JnxProductModelDELLJSRX1400_ObjectIdentity = ObjectIdentity
jnxProductModelDELLJSRX1400 = _JnxProductModelDELLJSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 79)
)
_JnxProductModelDELLJSRX5800_ObjectIdentity = ObjectIdentity
jnxProductModelDELLJSRX5800 = _JnxProductModelDELLJSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 80)
)
_JnxProductModelDELLJSRX5600_ObjectIdentity = ObjectIdentity
jnxProductModelDELLJSRX5600 = _JnxProductModelDELLJSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 81)
)
_JnxProductModelQFXSwitch_ObjectIdentity = ObjectIdentity
jnxProductModelQFXSwitch = _JnxProductModelQFXSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 82)
)
_JnxProductModelT4000_ObjectIdentity = ObjectIdentity
jnxProductModelT4000 = _JnxProductModelT4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 83)
)
_JnxProductModelQFX3000_ObjectIdentity = ObjectIdentity
jnxProductModelQFX3000 = _JnxProductModelQFX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 84)
)
_JnxProductModelQFX5000_ObjectIdentity = ObjectIdentity
jnxProductModelQFX5000 = _JnxProductModelQFX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 85)
)
_JnxProductModelACX_ObjectIdentity = ObjectIdentity
jnxProductModelACX = _JnxProductModelACX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 87)
)
_JnxProductModelMX40_ObjectIdentity = ObjectIdentity
jnxProductModelMX40 = _JnxProductModelMX40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 88)
)
_JnxProductModelMX10_ObjectIdentity = ObjectIdentity
jnxProductModelMX10 = _JnxProductModelMX10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 89)
)
_JnxProductModelMX5_ObjectIdentity = ObjectIdentity
jnxProductModelMX5 = _JnxProductModelMX5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 90)
)
_JnxProductModelQFXMInterconnect_ObjectIdentity = ObjectIdentity
jnxProductModelQFXMInterconnect = _JnxProductModelQFXMInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 91)
)
_JnxProductModelEX4550_ObjectIdentity = ObjectIdentity
jnxProductModelEX4550 = _JnxProductModelEX4550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 92)
)
_JnxProductModelMX2020_ObjectIdentity = ObjectIdentity
jnxProductModelMX2020 = _JnxProductModelMX2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 93)
)
_JnxProductModelLN2600_ObjectIdentity = ObjectIdentity
jnxProductModelLN2600 = _JnxProductModelLN2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 95)
)
_JnxProductModelMX104_ObjectIdentity = ObjectIdentity
jnxProductModelMX104 = _JnxProductModelMX104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 97)
)
_JnxProductModelPTX3000_ObjectIdentity = ObjectIdentity
jnxProductModelPTX3000 = _JnxProductModelPTX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 98)
)
_JnxProductModelMX2010_ObjectIdentity = ObjectIdentity
jnxProductModelMX2010 = _JnxProductModelMX2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 99)
)
_JnxProductModelQFX3100_ObjectIdentity = ObjectIdentity
jnxProductModelQFX3100 = _JnxProductModelQFX3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 100)
)
_JnxProductModelEX9214_ObjectIdentity = ObjectIdentity
jnxProductModelEX9214 = _JnxProductModelEX9214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 102)
)
_JnxProductModelEX9208_ObjectIdentity = ObjectIdentity
jnxProductModelEX9208 = _JnxProductModelEX9208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 103)
)
_JnxProductModelEX9204_ObjectIdentity = ObjectIdentity
jnxProductModelEX9204 = _JnxProductModelEX9204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 104)
)
_JnxProductModelSRX5400_ObjectIdentity = ObjectIdentity
jnxProductModelSRX5400 = _JnxProductModelSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 105)
)
_JnxProductModelIBM4274S54J54S_ObjectIdentity = ObjectIdentity
jnxProductModelIBM4274S54J54S = _JnxProductModelIBM4274S54J54S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 106)
)
_JnxProductModelDELLJSRX5400_ObjectIdentity = ObjectIdentity
jnxProductModelDELLJSRX5400 = _JnxProductModelDELLJSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 107)
)
_JnxProductModelVMX_ObjectIdentity = ObjectIdentity
jnxProductModelVMX = _JnxProductModelVMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 108)
)
_JnxProductModelEX4600_ObjectIdentity = ObjectIdentity
jnxProductModelEX4600 = _JnxProductModelEX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 109)
)
_JnxProductModelVRR_ObjectIdentity = ObjectIdentity
jnxProductModelVRR = _JnxProductModelVRR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 110)
)
_JnxProductModelOCPAcc_ObjectIdentity = ObjectIdentity
jnxProductModelOCPAcc = _JnxProductModelOCPAcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 112)
)
_JnxProductModelACX1000_ObjectIdentity = ObjectIdentity
jnxProductModelACX1000 = _JnxProductModelACX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 113)
)
_JnxProductModelACX2000_ObjectIdentity = ObjectIdentity
jnxProductModelACX2000 = _JnxProductModelACX2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 114)
)
_JnxProductModelACX1100_ObjectIdentity = ObjectIdentity
jnxProductModelACX1100 = _JnxProductModelACX1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 115)
)
_JnxProductModelACX2100_ObjectIdentity = ObjectIdentity
jnxProductModelACX2100 = _JnxProductModelACX2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 116)
)
_JnxProductModelACX2200_ObjectIdentity = ObjectIdentity
jnxProductModelACX2200 = _JnxProductModelACX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 117)
)
_JnxProductModelACX4000_ObjectIdentity = ObjectIdentity
jnxProductModelACX4000 = _JnxProductModelACX4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 118)
)
_JnxProductModelACX500AC_ObjectIdentity = ObjectIdentity
jnxProductModelACX500AC = _JnxProductModelACX500AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 119)
)
_JnxProductModelACX500DC_ObjectIdentity = ObjectIdentity
jnxProductModelACX500DC = _JnxProductModelACX500DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 120)
)
_JnxProductModelACX500OAC_ObjectIdentity = ObjectIdentity
jnxProductModelACX500OAC = _JnxProductModelACX500OAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 121)
)
_JnxProductModelACX500ODC_ObjectIdentity = ObjectIdentity
jnxProductModelACX500ODC = _JnxProductModelACX500ODC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 122)
)
_JnxProductModelACX500OPOEAC_ObjectIdentity = ObjectIdentity
jnxProductModelACX500OPOEAC = _JnxProductModelACX500OPOEAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 123)
)
_JnxProductModelACX500OPOEDC_ObjectIdentity = ObjectIdentity
jnxProductModelACX500OPOEDC = _JnxProductModelACX500OPOEDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 124)
)
_JnxProductModelSatelliteDevice_ObjectIdentity = ObjectIdentity
jnxProductModelSatelliteDevice = _JnxProductModelSatelliteDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 125)
)
_JnxProductModelACX5048_ObjectIdentity = ObjectIdentity
jnxProductModelACX5048 = _JnxProductModelACX5048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 126)
)
_JnxProductModelACX5096_ObjectIdentity = ObjectIdentity
jnxProductModelACX5096 = _JnxProductModelACX5096_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 127)
)
_JnxProductModelLN1000CC_ObjectIdentity = ObjectIdentity
jnxProductModelLN1000CC = _JnxProductModelLN1000CC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 128)
)
_JnxProductModelPTX1000_ObjectIdentity = ObjectIdentity
jnxProductModelPTX1000 = _JnxProductModelPTX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 130)
)
_JnxProductModelEX3400_ObjectIdentity = ObjectIdentity
jnxProductModelEX3400 = _JnxProductModelEX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 131)
)
_JnxProductModelEX2300_ObjectIdentity = ObjectIdentity
jnxProductModelEX2300 = _JnxProductModelEX2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 132)
)
_JnxProductModelNFX_ObjectIdentity = ObjectIdentity
jnxProductModelNFX = _JnxProductModelNFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 138)
)
_JnxProductModelJNP10003_ObjectIdentity = ObjectIdentity
jnxProductModelJNP10003 = _JnxProductModelJNP10003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 139)
)
_JnxProductModelSRX4600_ObjectIdentity = ObjectIdentity
jnxProductModelSRX4600 = _JnxProductModelSRX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 140)
)
_JnxProductModelSRX4800_ObjectIdentity = ObjectIdentity
jnxProductModelSRX4800 = _JnxProductModelSRX4800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 141)
)
_JnxProductModelJNP204_ObjectIdentity = ObjectIdentity
jnxProductModelJNP204 = _JnxProductModelJNP204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 144)
)
_JnxProductModelMX2008_ObjectIdentity = ObjectIdentity
jnxProductModelMX2008 = _JnxProductModelMX2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 145)
)
_JnxProductModelMXTSR80_ObjectIdentity = ObjectIdentity
jnxProductModelMXTSR80 = _JnxProductModelMXTSR80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 146)
)
_JnxProductModelPTX10008_ObjectIdentity = ObjectIdentity
jnxProductModelPTX10008 = _JnxProductModelPTX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 147)
)
_JnxProductModelACX5448_ObjectIdentity = ObjectIdentity
jnxProductModelACX5448 = _JnxProductModelACX5448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 148)
)
_JnxProductModelPTX10016_ObjectIdentity = ObjectIdentity
jnxProductModelPTX10016 = _JnxProductModelPTX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 150)
)
_JnxProductModelEX9251_ObjectIdentity = ObjectIdentity
jnxProductModelEX9251 = _JnxProductModelEX9251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 151)
)
_JnxProductModelMX150_ObjectIdentity = ObjectIdentity
jnxProductModelMX150 = _JnxProductModelMX150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 152)
)
_JnxProductModelJNP10001_ObjectIdentity = ObjectIdentity
jnxProductModelJNP10001 = _JnxProductModelJNP10001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 153)
)
_JnxProductModelMX10008_ObjectIdentity = ObjectIdentity
jnxProductModelMX10008 = _JnxProductModelMX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 154)
)
_JnxProductModelMX10016_ObjectIdentity = ObjectIdentity
jnxProductModelMX10016 = _JnxProductModelMX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 155)
)
_JnxProductModelEX9253_ObjectIdentity = ObjectIdentity
jnxProductModelEX9253 = _JnxProductModelEX9253_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 156)
)
_JnxProductModelACX5448M_ObjectIdentity = ObjectIdentity
jnxProductModelACX5448M = _JnxProductModelACX5448M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 158)
)
_JnxProductModelACX5448D_ObjectIdentity = ObjectIdentity
jnxProductModelACX5448D = _JnxProductModelACX5448D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 159)
)
_JnxProductModelACX6360OR_ObjectIdentity = ObjectIdentity
jnxProductModelACX6360OR = _JnxProductModelACX6360OR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 160)
)
_JnxProductModelACX6360OX_ObjectIdentity = ObjectIdentity
jnxProductModelACX6360OX = _JnxProductModelACX6360OX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 161)
)
_JnxProductModelACX710_ObjectIdentity = ObjectIdentity
jnxProductModelACX710 = _JnxProductModelACX710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 162)
)
_JnxProductModelACX5800_ObjectIdentity = ObjectIdentity
jnxProductModelACX5800 = _JnxProductModelACX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 163)
)
_JnxProductModelEX4400_ObjectIdentity = ObjectIdentity
jnxProductModelEX4400 = _JnxProductModelEX4400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 165)
)
_JnxProductModelR6675_ObjectIdentity = ObjectIdentity
jnxProductModelR6675 = _JnxProductModelR6675_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 166)
)
_JnxProductModelMX304_ObjectIdentity = ObjectIdentity
jnxProductModelMX304 = _JnxProductModelMX304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 167)
)
_JnxProductModelMX10004_ObjectIdentity = ObjectIdentity
jnxProductModelMX10004 = _JnxProductModelMX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 168)
)
_JnxProductModelEX4100_ObjectIdentity = ObjectIdentity
jnxProductModelEX4100 = _JnxProductModelEX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 169)
)
_JnxProductModelEX4650_ObjectIdentity = ObjectIdentity
jnxProductModelEX4650 = _JnxProductModelEX4650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 508)
)
_JnxProductModelPTX1000260C_ObjectIdentity = ObjectIdentity
jnxProductModelPTX1000260C = _JnxProductModelPTX1000260C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 513)
)
_JnxProductModelPTX1000380c_ObjectIdentity = ObjectIdentity
jnxProductModelPTX1000380c = _JnxProductModelPTX1000380c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 523)
)
_JnxProductModelPTX10003160c_ObjectIdentity = ObjectIdentity
jnxProductModelPTX10003160c = _JnxProductModelPTX10003160c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 524)
)
_JnxProductModelQFX1000380c_ObjectIdentity = ObjectIdentity
jnxProductModelQFX1000380c = _JnxProductModelQFX1000380c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 525)
)
_JnxProductModelQFX10003160c_ObjectIdentity = ObjectIdentity
jnxProductModelQFX10003160c = _JnxProductModelQFX10003160c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 526)
)
_JnxProductModelPTX1000136mr_ObjectIdentity = ObjectIdentity
jnxProductModelPTX1000136mr = _JnxProductModelPTX1000136mr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 555)
)
_JnxProductModelPTX10004_ObjectIdentity = ObjectIdentity
jnxProductModelPTX10004 = _JnxProductModelPTX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 570)
)
_JnxProductModelACX753_ObjectIdentity = ObjectIdentity
jnxProductModelACX753 = _JnxProductModelACX753_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 576)
)
_JnxProductModelSRX1800_ObjectIdentity = ObjectIdentity
jnxProductModelSRX1800 = _JnxProductModelSRX1800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 577)
)
_JnxProductModelACX7KSwitch_ObjectIdentity = ObjectIdentity
jnxProductModelACX7KSwitch = _JnxProductModelACX7KSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 578)
)
_JnxProductModelACX710032c_ObjectIdentity = ObjectIdentity
jnxProductModelACX710032c = _JnxProductModelACX710032c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 579)
)
_JnxProductModelACX710048l_ObjectIdentity = ObjectIdentity
jnxProductModelACX710048l = _JnxProductModelACX710048l_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 580)
)
_JnxProductModelACX7908_ObjectIdentity = ObjectIdentity
jnxProductModelACX7908 = _JnxProductModelACX7908_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 581)
)
_JnxProductModelACX7024_ObjectIdentity = ObjectIdentity
jnxProductModelACX7024 = _JnxProductModelACX7024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 582)
)
_JnxProductModelACX7332_ObjectIdentity = ObjectIdentity
jnxProductModelACX7332 = _JnxProductModelACX7332_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 586)
)
_JnxProductModelACX7348_ObjectIdentity = ObjectIdentity
jnxProductModelACX7348 = _JnxProductModelACX7348_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 587)
)
_JnxProductModelACX7024X_ObjectIdentity = ObjectIdentity
jnxProductModelACX7024X = _JnxProductModelACX7024X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 588)
)
_JnxProductModelPTX1000236qdd_ObjectIdentity = ObjectIdentity
jnxProductModelPTX1000236qdd = _JnxProductModelPTX1000236qdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 3, 589)
)
_JnxProductVariation_ObjectIdentity = ObjectIdentity
jnxProductVariation = _JnxProductVariation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4)
)
_JnxProductVariationM40_ObjectIdentity = ObjectIdentity
jnxProductVariationM40 = _JnxProductVariationM40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 1)
)
_JnxProductVariationM20_ObjectIdentity = ObjectIdentity
jnxProductVariationM20 = _JnxProductVariationM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 2)
)
_JnxProductVariationM160_ObjectIdentity = ObjectIdentity
jnxProductVariationM160 = _JnxProductVariationM160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 3)
)
_JnxProductVariationM10_ObjectIdentity = ObjectIdentity
jnxProductVariationM10 = _JnxProductVariationM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 4)
)
_JnxProductVariationM5_ObjectIdentity = ObjectIdentity
jnxProductVariationM5 = _JnxProductVariationM5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 5)
)
_JnxProductVariationT640_ObjectIdentity = ObjectIdentity
jnxProductVariationT640 = _JnxProductVariationT640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 6)
)
_JnxProductVariationT320_ObjectIdentity = ObjectIdentity
jnxProductVariationT320 = _JnxProductVariationT320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 7)
)
_JnxProductVariationM40e_ObjectIdentity = ObjectIdentity
jnxProductVariationM40e = _JnxProductVariationM40e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 8)
)
_JnxProductVariationM320_ObjectIdentity = ObjectIdentity
jnxProductVariationM320 = _JnxProductVariationM320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 9)
)
_JnxProductVariationM7i_ObjectIdentity = ObjectIdentity
jnxProductVariationM7i = _JnxProductVariationM7i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 10)
)
_JnxProductVariationM10i_ObjectIdentity = ObjectIdentity
jnxProductVariationM10i = _JnxProductVariationM10i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 11)
)
_JnxProductVariationIRM_ObjectIdentity = ObjectIdentity
jnxProductVariationIRM = _JnxProductVariationIRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 16)
)
_JnxProductVariationTX_ObjectIdentity = ObjectIdentity
jnxProductVariationTX = _JnxProductVariationTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 17)
)
_JnxProductVariationM120_ObjectIdentity = ObjectIdentity
jnxProductVariationM120 = _JnxProductVariationM120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 18)
)
_JnxProductVariationMX960_ObjectIdentity = ObjectIdentity
jnxProductVariationMX960 = _JnxProductVariationMX960_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 21)
)
_JnxProductVariationMX480_ObjectIdentity = ObjectIdentity
jnxProductVariationMX480 = _JnxProductVariationMX480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 25)
)
_JnxProductVariationSRX5800_ObjectIdentity = ObjectIdentity
jnxProductVariationSRX5800 = _JnxProductVariationSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 26)
)
_JnxProductVariationT1600_ObjectIdentity = ObjectIdentity
jnxProductVariationT1600 = _JnxProductVariationT1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 27)
)
_JnxProductVariationSRX5600_ObjectIdentity = ObjectIdentity
jnxProductVariationSRX5600 = _JnxProductVariationSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 28)
)
_JnxProductVariationMX240_ObjectIdentity = ObjectIdentity
jnxProductVariationMX240 = _JnxProductVariationMX240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 29)
)
_JnxProductVariationEX3200_ObjectIdentity = ObjectIdentity
jnxProductVariationEX3200 = _JnxProductVariationEX3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 30)
)
_JnxProductEX3200port24T_ObjectIdentity = ObjectIdentity
jnxProductEX3200port24T = _JnxProductEX3200port24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 30, 1)
)
_JnxProductEX3200port24P_ObjectIdentity = ObjectIdentity
jnxProductEX3200port24P = _JnxProductEX3200port24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 30, 2)
)
_JnxProductEX3200port48T_ObjectIdentity = ObjectIdentity
jnxProductEX3200port48T = _JnxProductEX3200port48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 30, 3)
)
_JnxProductEX3200port48P_ObjectIdentity = ObjectIdentity
jnxProductEX3200port48P = _JnxProductEX3200port48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 30, 4)
)
_JnxProductVariationEX4200_ObjectIdentity = ObjectIdentity
jnxProductVariationEX4200 = _JnxProductVariationEX4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 31)
)
_JnxProductEX4200port24T_ObjectIdentity = ObjectIdentity
jnxProductEX4200port24T = _JnxProductEX4200port24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 31, 1)
)
_JnxProductEX4200port24P_ObjectIdentity = ObjectIdentity
jnxProductEX4200port24P = _JnxProductEX4200port24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 31, 2)
)
_JnxProductEX4200port48T_ObjectIdentity = ObjectIdentity
jnxProductEX4200port48T = _JnxProductEX4200port48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 31, 3)
)
_JnxProductEX4200port48P_ObjectIdentity = ObjectIdentity
jnxProductEX4200port48P = _JnxProductEX4200port48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 31, 4)
)
_JnxProductEX4200port24F_ObjectIdentity = ObjectIdentity
jnxProductEX4200port24F = _JnxProductEX4200port24F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 31, 5)
)
_JnxProductEX4200port24PX_ObjectIdentity = ObjectIdentity
jnxProductEX4200port24PX = _JnxProductEX4200port24PX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 31, 6)
)
_JnxProductEX4200port48PX_ObjectIdentity = ObjectIdentity
jnxProductEX4200port48PX = _JnxProductEX4200port48PX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 31, 7)
)
_JnxProductVariationEX8208_ObjectIdentity = ObjectIdentity
jnxProductVariationEX8208 = _JnxProductVariationEX8208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 32)
)
_JnxProductVariationEX8216_ObjectIdentity = ObjectIdentity
jnxProductVariationEX8216 = _JnxProductVariationEX8216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 33)
)
_JnxProductVariationSRX3600_ObjectIdentity = ObjectIdentity
jnxProductVariationSRX3600 = _JnxProductVariationSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 34)
)
_JnxProductVariationSRX3400_ObjectIdentity = ObjectIdentity
jnxProductVariationSRX3400 = _JnxProductVariationSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 35)
)
_JnxProductVariationTXP_ObjectIdentity = ObjectIdentity
jnxProductVariationTXP = _JnxProductVariationTXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 37)
)
_JnxProductVariationJCS_ObjectIdentity = ObjectIdentity
jnxProductVariationJCS = _JnxProductVariationJCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 38)
)
_JnxProductVariationLN1000V_ObjectIdentity = ObjectIdentity
jnxProductVariationLN1000V = _JnxProductVariationLN1000V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 42)
)
_JnxProductVariationEX2200_ObjectIdentity = ObjectIdentity
jnxProductVariationEX2200 = _JnxProductVariationEX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 43)
)
_JnxProductEX2200port24T_ObjectIdentity = ObjectIdentity
jnxProductEX2200port24T = _JnxProductEX2200port24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 43, 1)
)
_JnxProductEX2200port24P_ObjectIdentity = ObjectIdentity
jnxProductEX2200port24P = _JnxProductEX2200port24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 43, 2)
)
_JnxProductEX2200port48T_ObjectIdentity = ObjectIdentity
jnxProductEX2200port48T = _JnxProductEX2200port48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 43, 3)
)
_JnxProductEX2200port48P_ObjectIdentity = ObjectIdentity
jnxProductEX2200port48P = _JnxProductEX2200port48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 43, 4)
)
_JnxProductEX2200Cport12T_ObjectIdentity = ObjectIdentity
jnxProductEX2200Cport12T = _JnxProductEX2200Cport12T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 43, 5)
)
_JnxProductEX2200Cport12P_ObjectIdentity = ObjectIdentity
jnxProductEX2200Cport12P = _JnxProductEX2200Cport12P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 43, 6)
)
_JnxProductEX2200port24TDC_ObjectIdentity = ObjectIdentity
jnxProductEX2200port24TDC = _JnxProductEX2200port24TDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 43, 7)
)
_JnxProductVariationEX4500_ObjectIdentity = ObjectIdentity
jnxProductVariationEX4500 = _JnxProductVariationEX4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 44)
)
_JnxProductEX4500port40F_ObjectIdentity = ObjectIdentity
jnxProductEX4500port40F = _JnxProductEX4500port40F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 44, 1)
)
_JnxProductEX4500port20F_ObjectIdentity = ObjectIdentity
jnxProductEX4500port20F = _JnxProductEX4500port20F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 44, 2)
)
_JnxProductVariationFXSeries_ObjectIdentity = ObjectIdentity
jnxProductVariationFXSeries = _JnxProductVariationFXSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 45)
)
_JnxProductFX1600port_ObjectIdentity = ObjectIdentity
jnxProductFX1600port = _JnxProductFX1600port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 45, 1)
)
_JnxProductFX2160port_ObjectIdentity = ObjectIdentity
jnxProductFX2160port = _JnxProductFX2160port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 45, 2)
)
_JnxProductVariationIBM4274M02J02M_ObjectIdentity = ObjectIdentity
jnxProductVariationIBM4274M02J02M = _JnxProductVariationIBM4274M02J02M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 46)
)
_JnxProductVariationIBM4274M06J06M_ObjectIdentity = ObjectIdentity
jnxProductVariationIBM4274M06J06M = _JnxProductVariationIBM4274M06J06M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 47)
)
_JnxProductVariationIBM4274M11J11M_ObjectIdentity = ObjectIdentity
jnxProductVariationIBM4274M11J11M = _JnxProductVariationIBM4274M11J11M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 48)
)
_JnxProductVariationSRX1400_ObjectIdentity = ObjectIdentity
jnxProductVariationSRX1400 = _JnxProductVariationSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 49)
)
_JnxProductVariationIBM4274S58J58S_ObjectIdentity = ObjectIdentity
jnxProductVariationIBM4274S58J58S = _JnxProductVariationIBM4274S58J58S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 50)
)
_JnxProductVariationIBM4274S56J56S_ObjectIdentity = ObjectIdentity
jnxProductVariationIBM4274S56J56S = _JnxProductVariationIBM4274S56J56S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 51)
)
_JnxProductVariationIBM4274S36J36S_ObjectIdentity = ObjectIdentity
jnxProductVariationIBM4274S36J36S = _JnxProductVariationIBM4274S36J36S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 52)
)
_JnxProductVariationIBM4274S34J34S_ObjectIdentity = ObjectIdentity
jnxProductVariationIBM4274S34J34S = _JnxProductVariationIBM4274S34J34S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 53)
)
_JnxProductVariationIBM427348EJ48E_ObjectIdentity = ObjectIdentity
jnxProductVariationIBM427348EJ48E = _JnxProductVariationIBM427348EJ48E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 54)
)
_JnxProductIBM427348EJ48Eport24T_ObjectIdentity = ObjectIdentity
jnxProductIBM427348EJ48Eport24T = _JnxProductIBM427348EJ48Eport24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 54, 1)
)
_JnxProductIBM427348EJ48Eport24P_ObjectIdentity = ObjectIdentity
jnxProductIBM427348EJ48Eport24P = _JnxProductIBM427348EJ48Eport24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 54, 2)
)
_JnxProductIBM427348EJ48Eport48T_ObjectIdentity = ObjectIdentity
jnxProductIBM427348EJ48Eport48T = _JnxProductIBM427348EJ48Eport48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 54, 3)
)
_JnxProductIBM427348EJ48Eport48P_ObjectIdentity = ObjectIdentity
jnxProductIBM427348EJ48Eport48P = _JnxProductIBM427348EJ48Eport48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 54, 4)
)
_JnxProductIBM427348EJ48Eport24F_ObjectIdentity = ObjectIdentity
jnxProductIBM427348EJ48Eport24F = _JnxProductIBM427348EJ48Eport24F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 54, 5)
)
_JnxProductVariationIBM4274E08J08E_ObjectIdentity = ObjectIdentity
jnxProductVariationIBM4274E08J08E = _JnxProductVariationIBM4274E08J08E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 55)
)
_JnxProductVariationIBM4274E16J16E_ObjectIdentity = ObjectIdentity
jnxProductVariationIBM4274E16J16E = _JnxProductVariationIBM4274E16J16E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 56)
)
_JnxProductVariationMX80_ObjectIdentity = ObjectIdentity
jnxProductVariationMX80 = _JnxProductVariationMX80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 57)
)
_JnxProductMX80_ObjectIdentity = ObjectIdentity
jnxProductMX80 = _JnxProductMX80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 57, 1)
)
_JnxProductMX80_48T_ObjectIdentity = ObjectIdentity
jnxProductMX80_48T = _JnxProductMX80_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 57, 2)
)
_JnxProductMX80_T_ObjectIdentity = ObjectIdentity
jnxProductMX80_T = _JnxProductMX80_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 57, 3)
)
_JnxProductMX80_P_ObjectIdentity = ObjectIdentity
jnxProductMX80_P = _JnxProductMX80_P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 57, 4)
)
_JnxProductVariationEXXRE_ObjectIdentity = ObjectIdentity
jnxProductVariationEXXRE = _JnxProductVariationEXXRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 59)
)
_JnxProductEXXRE_ObjectIdentity = ObjectIdentity
jnxProductEXXRE = _JnxProductEXXRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 59, 1)
)
_JnxProductVariationQFXInterconnect_ObjectIdentity = ObjectIdentity
jnxProductVariationQFXInterconnect = _JnxProductVariationQFXInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 60)
)
_JnxProductQFX3008_ObjectIdentity = ObjectIdentity
jnxProductQFX3008 = _JnxProductQFX3008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 60, 1)
)
_JnxProductQFXC083008_ObjectIdentity = ObjectIdentity
jnxProductQFXC083008 = _JnxProductQFXC083008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 60, 2)
)
_JnxProductQFX3008I_ObjectIdentity = ObjectIdentity
jnxProductQFX3008I = _JnxProductQFX3008I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 60, 3)
)
_JnxProductVariationQFXNode_ObjectIdentity = ObjectIdentity
jnxProductVariationQFXNode = _JnxProductVariationQFXNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 61)
)
_JnxProductQFX3500_ObjectIdentity = ObjectIdentity
jnxProductQFX3500 = _JnxProductQFX3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 61, 1)
)
_JnxProductQFX5500_ObjectIdentity = ObjectIdentity
jnxProductQFX5500 = _JnxProductQFX5500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 61, 2)
)
_JnxProductQFX360016Q_ObjectIdentity = ObjectIdentity
jnxProductQFX360016Q = _JnxProductQFX360016Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 61, 3)
)
_JnxProductQFX350048T4Q_ObjectIdentity = ObjectIdentity
jnxProductQFX350048T4Q = _JnxProductQFX350048T4Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 61, 4)
)
_JnxProductQFX510024QF_ObjectIdentity = ObjectIdentity
jnxProductQFX510024QF = _JnxProductQFX510024QF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 61, 5)
)
_JnxProductQFX510048S6QF_ObjectIdentity = ObjectIdentity
jnxProductQFX510048S6QF = _JnxProductQFX510048S6QF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 61, 6)
)
_JnxProductQFX510096S6QF_ObjectIdentity = ObjectIdentity
jnxProductQFX510096S6QF = _JnxProductQFX510096S6QF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 61, 7)
)
_JnxProductQFX510048C6QF_ObjectIdentity = ObjectIdentity
jnxProductQFX510048C6QF = _JnxProductQFX510048C6QF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 61, 8)
)
_JnxProductVariationEX4300_ObjectIdentity = ObjectIdentity
jnxProductVariationEX4300 = _JnxProductVariationEX4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 63)
)
_JnxProductEX4300port24T_ObjectIdentity = ObjectIdentity
jnxProductEX4300port24T = _JnxProductEX4300port24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 63, 1)
)
_JnxProductEX4300port48T_ObjectIdentity = ObjectIdentity
jnxProductEX4300port48T = _JnxProductEX4300port48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 63, 2)
)
_JnxProductEX4300port48TBF_ObjectIdentity = ObjectIdentity
jnxProductEX4300port48TBF = _JnxProductEX4300port48TBF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 63, 3)
)
_JnxProductEX4300port48TDC_ObjectIdentity = ObjectIdentity
jnxProductEX4300port48TDC = _JnxProductEX4300port48TDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 63, 4)
)
_JnxProductEX4300port48TDCBF_ObjectIdentity = ObjectIdentity
jnxProductEX4300port48TDCBF = _JnxProductEX4300port48TDCBF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 63, 5)
)
_JnxProductEX4300port24P_ObjectIdentity = ObjectIdentity
jnxProductEX4300port24P = _JnxProductEX4300port24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 63, 6)
)
_JnxProductEX4300port48P_ObjectIdentity = ObjectIdentity
jnxProductEX4300port48P = _JnxProductEX4300port48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 63, 7)
)
_JnxProductEX4300port32F_ObjectIdentity = ObjectIdentity
jnxProductEX4300port32F = _JnxProductEX4300port32F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 63, 8)
)
_JnxProductEX4300port48MP_ObjectIdentity = ObjectIdentity
jnxProductEX4300port48MP = _JnxProductEX4300port48MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 63, 9)
)
_JnxProductVariationMAG8600_ObjectIdentity = ObjectIdentity
jnxProductVariationMAG8600 = _JnxProductVariationMAG8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 66)
)
_JnxProductVariationMAG6611_ObjectIdentity = ObjectIdentity
jnxProductVariationMAG6611 = _JnxProductVariationMAG6611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 67)
)
_JnxProductVariationMAG6610_ObjectIdentity = ObjectIdentity
jnxProductVariationMAG6610 = _JnxProductVariationMAG6610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 68)
)
_JnxProductVariationPTX5000_ObjectIdentity = ObjectIdentity
jnxProductVariationPTX5000 = _JnxProductVariationPTX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 69)
)
_JnxProductVariationIBM0719J45E_ObjectIdentity = ObjectIdentity
jnxProductVariationIBM0719J45E = _JnxProductVariationIBM0719J45E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 71)
)
_JnxProductIBM0719J45Eport40F_ObjectIdentity = ObjectIdentity
jnxProductIBM0719J45Eport40F = _JnxProductIBM0719J45Eport40F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 71, 1)
)
_JnxProductIBM0719J45Eport20F_ObjectIdentity = ObjectIdentity
jnxProductIBM0719J45Eport20F = _JnxProductIBM0719J45Eport20F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 71, 2)
)
_JnxProductVariationIBMJ08F_ObjectIdentity = ObjectIdentity
jnxProductVariationIBMJ08F = _JnxProductVariationIBMJ08F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 72)
)
_JnxProductIBM2413F08J08F_ObjectIdentity = ObjectIdentity
jnxProductIBM2413F08J08F = _JnxProductIBM2413F08J08F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 72, 1)
)
_JnxProductVariationIBMJ52F_ObjectIdentity = ObjectIdentity
jnxProductVariationIBMJ52F = _JnxProductVariationIBMJ52F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 73)
)
_JnxProductIBM2409F52J52F_ObjectIdentity = ObjectIdentity
jnxProductIBM2409F52J52F = _JnxProductIBM2409F52J52F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 73, 1)
)
_JnxProductIBM8729HC1J52F_ObjectIdentity = ObjectIdentity
jnxProductIBM8729HC1J52F = _JnxProductIBM8729HC1J52F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 73, 2)
)
_JnxProductVariationEX6210_ObjectIdentity = ObjectIdentity
jnxProductVariationEX6210 = _JnxProductVariationEX6210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 74)
)
_JnxProductVariationDellJFX3500_ObjectIdentity = ObjectIdentity
jnxProductVariationDellJFX3500 = _JnxProductVariationDellJFX3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 75)
)
_JnxProductVariationEX3300_ObjectIdentity = ObjectIdentity
jnxProductVariationEX3300 = _JnxProductVariationEX3300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 76)
)
_JnxProductEX3300port24T_ObjectIdentity = ObjectIdentity
jnxProductEX3300port24T = _JnxProductEX3300port24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 76, 1)
)
_JnxProductEX3300port24P_ObjectIdentity = ObjectIdentity
jnxProductEX3300port24P = _JnxProductEX3300port24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 76, 2)
)
_JnxProductEX3300port48T_ObjectIdentity = ObjectIdentity
jnxProductEX3300port48T = _JnxProductEX3300port48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 76, 3)
)
_JnxProductEX3300port48P_ObjectIdentity = ObjectIdentity
jnxProductEX3300port48P = _JnxProductEX3300port48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 76, 4)
)
_JnxProductEX3300port24TDC_ObjectIdentity = ObjectIdentity
jnxProductEX3300port24TDC = _JnxProductEX3300port24TDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 76, 5)
)
_JnxProductEX3300port48TBF_ObjectIdentity = ObjectIdentity
jnxProductEX3300port48TBF = _JnxProductEX3300port48TBF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 76, 6)
)
_JnxProductVariationDELLJSRX3600_ObjectIdentity = ObjectIdentity
jnxProductVariationDELLJSRX3600 = _JnxProductVariationDELLJSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 77)
)
_JnxProductVariationDELLJSRX3400_ObjectIdentity = ObjectIdentity
jnxProductVariationDELLJSRX3400 = _JnxProductVariationDELLJSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 78)
)
_JnxProductVariationDELLJSRX1400_ObjectIdentity = ObjectIdentity
jnxProductVariationDELLJSRX1400 = _JnxProductVariationDELLJSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 79)
)
_JnxProductVariationDELLJSRX5800_ObjectIdentity = ObjectIdentity
jnxProductVariationDELLJSRX5800 = _JnxProductVariationDELLJSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 80)
)
_JnxProductVariationDELLJSRX5600_ObjectIdentity = ObjectIdentity
jnxProductVariationDELLJSRX5600 = _JnxProductVariationDELLJSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 81)
)
_JnxProductVariationQFXSwitch_ObjectIdentity = ObjectIdentity
jnxProductVariationQFXSwitch = _JnxProductVariationQFXSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82)
)
_JnxProductQFX3500s_ObjectIdentity = ObjectIdentity
jnxProductQFX3500s = _JnxProductQFX3500s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 1)
)
_JnxProductQFX360016QS_ObjectIdentity = ObjectIdentity
jnxProductQFX360016QS = _JnxProductQFX360016QS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 2)
)
_JnxProductQFX350048T4QS_ObjectIdentity = ObjectIdentity
jnxProductQFX350048T4QS = _JnxProductQFX350048T4QS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 3)
)
_JnxProductQFX510024Q_ObjectIdentity = ObjectIdentity
jnxProductQFX510024Q = _JnxProductQFX510024Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 4)
)
_JnxProductQFX510048S6Q_ObjectIdentity = ObjectIdentity
jnxProductQFX510048S6Q = _JnxProductQFX510048S6Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 5)
)
_JnxProductQFX510096S8Q_ObjectIdentity = ObjectIdentity
jnxProductQFX510096S8Q = _JnxProductQFX510096S8Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 6)
)
_JnxProductQFX510048C6Q_ObjectIdentity = ObjectIdentity
jnxProductQFX510048C6Q = _JnxProductQFX510048C6Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 7)
)
_JnxProductQFX510024QHP_ObjectIdentity = ObjectIdentity
jnxProductQFX510024QHP = _JnxProductQFX510024QHP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 8)
)
_JnxProductQFX510048T6Q_ObjectIdentity = ObjectIdentity
jnxProductQFX510048T6Q = _JnxProductQFX510048T6Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 9)
)
_JnxProductQFX1000236Q_ObjectIdentity = ObjectIdentity
jnxProductQFX1000236Q = _JnxProductQFX1000236Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 10)
)
_JnxProductQFX1000272Q_ObjectIdentity = ObjectIdentity
jnxProductQFX1000272Q = _JnxProductQFX1000272Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 11)
)
_JnxProductQFX10004_ObjectIdentity = ObjectIdentity
jnxProductQFX10004 = _JnxProductQFX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 12)
)
_JnxProductQFX10008_ObjectIdentity = ObjectIdentity
jnxProductQFX10008 = _JnxProductQFX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 13)
)
_JnxProductQFX10016_ObjectIdentity = ObjectIdentity
jnxProductQFX10016 = _JnxProductQFX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 14)
)
_JnxProductQFX520032C32Q_ObjectIdentity = ObjectIdentity
jnxProductQFX520032C32Q = _JnxProductQFX520032C32Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 15)
)
_JnxProductQFX520032C64Q_ObjectIdentity = ObjectIdentity
jnxProductQFX520032C64Q = _JnxProductQFX520032C64Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 16)
)
_JnxProductQFX511048S4C_ObjectIdentity = ObjectIdentity
jnxProductQFX511048S4C = _JnxProductQFX511048S4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 17)
)
_JnxProductQFX511032Q_ObjectIdentity = ObjectIdentity
jnxProductQFX511032Q = _JnxProductQFX511032Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 18)
)
_JnxProductNameQFX1000260C_ObjectIdentity = ObjectIdentity
jnxProductNameQFX1000260C = _JnxProductNameQFX1000260C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 19)
)
_JnxProductQFX521064C_ObjectIdentity = ObjectIdentity
jnxProductQFX521064C = _JnxProductQFX521064C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 20)
)
_JnxProductQFX520048Y_ObjectIdentity = ObjectIdentity
jnxProductQFX520048Y = _JnxProductQFX520048Y_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 21)
)
_JnxProductQFX512048Y8C_ObjectIdentity = ObjectIdentity
jnxProductQFX512048Y8C = _JnxProductQFX512048Y8C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 22)
)
_JnxProductAS781664X_ObjectIdentity = ObjectIdentity
jnxProductAS781664X = _JnxProductAS781664X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 23)
)
_JnxProductQFX512032C_ObjectIdentity = ObjectIdentity
jnxProductQFX512032C = _JnxProductQFX512032C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 24)
)
_JnxProductQFX522032CD_ObjectIdentity = ObjectIdentity
jnxProductQFX522032CD = _JnxProductQFX522032CD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 25)
)
_JnxProductQFX5220128C_ObjectIdentity = ObjectIdentity
jnxProductQFX5220128C = _JnxProductQFX5220128C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 26)
)
_JnxProductQFX512048T6C_ObjectIdentity = ObjectIdentity
jnxProductQFX512048T6C = _JnxProductQFX512048T6C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 27)
)
_JnxProductQFX513032CD_ObjectIdentity = ObjectIdentity
jnxProductQFX513032CD = _JnxProductQFX513032CD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 28)
)
_JnxProductQFX513048C_ObjectIdentity = ObjectIdentity
jnxProductQFX513048C = _JnxProductQFX513048C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 29)
)
_JnxProductQFX512048YM8C_ObjectIdentity = ObjectIdentity
jnxProductQFX512048YM8C = _JnxProductQFX512048YM8C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 30)
)
_JnxProductQFX5700_ObjectIdentity = ObjectIdentity
jnxProductQFX5700 = _JnxProductQFX5700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 31)
)
_JnxProductQFX523064CD_ObjectIdentity = ObjectIdentity
jnxProductQFX523064CD = _JnxProductQFX523064CD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 32)
)
_JnxProductQFX5130E32CD_ObjectIdentity = ObjectIdentity
jnxProductQFX5130E32CD = _JnxProductQFX5130E32CD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 33)
)
_JnxProductQFX524064OSFP_ObjectIdentity = ObjectIdentity
jnxProductQFX524064OSFP = _JnxProductQFX524064OSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 34)
)
_JnxProductQFX524064QSFPDD_ObjectIdentity = ObjectIdentity
jnxProductQFX524064QSFPDD = _JnxProductQFX524064QSFPDD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 82, 35)
)
_JnxProductVariationT4000_ObjectIdentity = ObjectIdentity
jnxProductVariationT4000 = _JnxProductVariationT4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 83)
)
_JnxProductVariationQFX3000_ObjectIdentity = ObjectIdentity
jnxProductVariationQFX3000 = _JnxProductVariationQFX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 84)
)
_JnxProductQFX3000_G_ObjectIdentity = ObjectIdentity
jnxProductQFX3000_G = _JnxProductQFX3000_G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 84, 1)
)
_JnxProductQFX3000_M_ObjectIdentity = ObjectIdentity
jnxProductQFX3000_M = _JnxProductQFX3000_M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 84, 2)
)
_JnxProductVariationQFX5000_ObjectIdentity = ObjectIdentity
jnxProductVariationQFX5000 = _JnxProductVariationQFX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 85)
)
_JnxProductVariationACX_ObjectIdentity = ObjectIdentity
jnxProductVariationACX = _JnxProductVariationACX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 87)
)
_JnxProductACX500IDC_ObjectIdentity = ObjectIdentity
jnxProductACX500IDC = _JnxProductACX500IDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 87, 11)
)
_JnxProductACX500IAC_ObjectIdentity = ObjectIdentity
jnxProductACX500IAC = _JnxProductACX500IAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 87, 12)
)
_JnxProductVariationMX40_ObjectIdentity = ObjectIdentity
jnxProductVariationMX40 = _JnxProductVariationMX40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 88)
)
_JnxProductMX40_ObjectIdentity = ObjectIdentity
jnxProductMX40 = _JnxProductMX40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 88, 1)
)
_JnxProductVariationMX10_ObjectIdentity = ObjectIdentity
jnxProductVariationMX10 = _JnxProductVariationMX10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 89)
)
_JnxProductMX10_ObjectIdentity = ObjectIdentity
jnxProductMX10 = _JnxProductMX10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 89, 1)
)
_JnxProductVariationMX5_ObjectIdentity = ObjectIdentity
jnxProductVariationMX5 = _JnxProductVariationMX5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 90)
)
_JnxProductMX5_ObjectIdentity = ObjectIdentity
jnxProductMX5 = _JnxProductMX5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 90, 1)
)
_JnxProductVariationQFXMInterconnect_ObjectIdentity = ObjectIdentity
jnxProductVariationQFXMInterconnect = _JnxProductVariationQFXMInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 91)
)
_JnxProductQFX3600I_ObjectIdentity = ObjectIdentity
jnxProductQFX3600I = _JnxProductQFX3600I_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 91, 1)
)
_JnxProductQFX510024QI_ObjectIdentity = ObjectIdentity
jnxProductQFX510024QI = _JnxProductQFX510024QI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 91, 2)
)
_JnxProductVariationEX4550_ObjectIdentity = ObjectIdentity
jnxProductVariationEX4550 = _JnxProductVariationEX4550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 92)
)
_JnxProductEX4550port32F_ObjectIdentity = ObjectIdentity
jnxProductEX4550port32F = _JnxProductEX4550port32F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 92, 1)
)
_JnxProductEX4550port32T_ObjectIdentity = ObjectIdentity
jnxProductEX4550port32T = _JnxProductEX4550port32T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 92, 2)
)
_JnxProductVariationMX2020_ObjectIdentity = ObjectIdentity
jnxProductVariationMX2020 = _JnxProductVariationMX2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 93)
)
_JnxProductVariationLN2600_ObjectIdentity = ObjectIdentity
jnxProductVariationLN2600 = _JnxProductVariationLN2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 95)
)
_JnxProductVariationMX104_ObjectIdentity = ObjectIdentity
jnxProductVariationMX104 = _JnxProductVariationMX104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 97)
)
_JnxProductMX104_ObjectIdentity = ObjectIdentity
jnxProductMX104 = _JnxProductMX104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 97, 1)
)
_JnxProductVariationPTX3000_ObjectIdentity = ObjectIdentity
jnxProductVariationPTX3000 = _JnxProductVariationPTX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 98)
)
_JnxProductVariationMX2010_ObjectIdentity = ObjectIdentity
jnxProductVariationMX2010 = _JnxProductVariationMX2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 99)
)
_JnxProductVariationQFX3100_ObjectIdentity = ObjectIdentity
jnxProductVariationQFX3100 = _JnxProductVariationQFX3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 100)
)
_JnxProductVariationEX9214_ObjectIdentity = ObjectIdentity
jnxProductVariationEX9214 = _JnxProductVariationEX9214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 102)
)
_JnxProductVariationEX9208_ObjectIdentity = ObjectIdentity
jnxProductVariationEX9208 = _JnxProductVariationEX9208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 103)
)
_JnxProductVariationEX9204_ObjectIdentity = ObjectIdentity
jnxProductVariationEX9204 = _JnxProductVariationEX9204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 104)
)
_JnxProductVariationSRX5400_ObjectIdentity = ObjectIdentity
jnxProductVariationSRX5400 = _JnxProductVariationSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 105)
)
_JnxProductVariationIBM4274S54J54S_ObjectIdentity = ObjectIdentity
jnxProductVariationIBM4274S54J54S = _JnxProductVariationIBM4274S54J54S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 106)
)
_JnxProductVariationDELLJSRX5400_ObjectIdentity = ObjectIdentity
jnxProductVariationDELLJSRX5400 = _JnxProductVariationDELLJSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 107)
)
_JnxProductVariationEX4600_ObjectIdentity = ObjectIdentity
jnxProductVariationEX4600 = _JnxProductVariationEX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 109)
)
_JnxProductEX4600_ObjectIdentity = ObjectIdentity
jnxProductEX4600 = _JnxProductEX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 109, 1)
)
_JnxProductVariationOCPAcc_ObjectIdentity = ObjectIdentity
jnxProductVariationOCPAcc = _JnxProductVariationOCPAcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 112)
)
_JnxProductOCP48S_ObjectIdentity = ObjectIdentity
jnxProductOCP48S = _JnxProductOCP48S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 112, 1)
)
_JnxProductOCP48T_ObjectIdentity = ObjectIdentity
jnxProductOCP48T = _JnxProductOCP48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 112, 2)
)
_JnxProductVariationACX1000_ObjectIdentity = ObjectIdentity
jnxProductVariationACX1000 = _JnxProductVariationACX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 113)
)
_JnxProductACX1000_ObjectIdentity = ObjectIdentity
jnxProductACX1000 = _JnxProductACX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 113, 1)
)
_JnxProductVariationACX2000_ObjectIdentity = ObjectIdentity
jnxProductVariationACX2000 = _JnxProductVariationACX2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 114)
)
_JnxProductACX2000_ObjectIdentity = ObjectIdentity
jnxProductACX2000 = _JnxProductACX2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 114, 1)
)
_JnxProductVariationACX1100_ObjectIdentity = ObjectIdentity
jnxProductVariationACX1100 = _JnxProductVariationACX1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 115)
)
_JnxProductACX1100_ObjectIdentity = ObjectIdentity
jnxProductACX1100 = _JnxProductACX1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 115, 1)
)
_JnxProductVariationACX2100_ObjectIdentity = ObjectIdentity
jnxProductVariationACX2100 = _JnxProductVariationACX2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 116)
)
_JnxProductACX2100_ObjectIdentity = ObjectIdentity
jnxProductACX2100 = _JnxProductACX2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 116, 1)
)
_JnxProductVariationACX2200_ObjectIdentity = ObjectIdentity
jnxProductVariationACX2200 = _JnxProductVariationACX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 117)
)
_JnxProductACX2200_ObjectIdentity = ObjectIdentity
jnxProductACX2200 = _JnxProductACX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 117, 1)
)
_JnxProductVariationACX4000_ObjectIdentity = ObjectIdentity
jnxProductVariationACX4000 = _JnxProductVariationACX4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 118)
)
_JnxProductACX4000_ObjectIdentity = ObjectIdentity
jnxProductACX4000 = _JnxProductACX4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 118, 1)
)
_JnxProductVariationACX500AC_ObjectIdentity = ObjectIdentity
jnxProductVariationACX500AC = _JnxProductVariationACX500AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 119)
)
_JnxProductACX500AC_ObjectIdentity = ObjectIdentity
jnxProductACX500AC = _JnxProductACX500AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 119, 1)
)
_JnxProductVariationACX500DC_ObjectIdentity = ObjectIdentity
jnxProductVariationACX500DC = _JnxProductVariationACX500DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 120)
)
_JnxProductACX500DC_ObjectIdentity = ObjectIdentity
jnxProductACX500DC = _JnxProductACX500DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 120, 1)
)
_JnxProductVariationACX500OAC_ObjectIdentity = ObjectIdentity
jnxProductVariationACX500OAC = _JnxProductVariationACX500OAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 121)
)
_JnxProductACX500OAC_ObjectIdentity = ObjectIdentity
jnxProductACX500OAC = _JnxProductACX500OAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 121, 1)
)
_JnxProductVariationACX500ODC_ObjectIdentity = ObjectIdentity
jnxProductVariationACX500ODC = _JnxProductVariationACX500ODC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 122)
)
_JnxProductACX500ODC_ObjectIdentity = ObjectIdentity
jnxProductACX500ODC = _JnxProductACX500ODC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 122, 1)
)
_JnxProductVariationACX500OPOEAC_ObjectIdentity = ObjectIdentity
jnxProductVariationACX500OPOEAC = _JnxProductVariationACX500OPOEAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 123)
)
_JnxProductACX500OPOEAC_ObjectIdentity = ObjectIdentity
jnxProductACX500OPOEAC = _JnxProductACX500OPOEAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 123, 1)
)
_JnxProductVariationACX500OPOEDC_ObjectIdentity = ObjectIdentity
jnxProductVariationACX500OPOEDC = _JnxProductVariationACX500OPOEDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 124)
)
_JnxProductACX500OPOEDC_ObjectIdentity = ObjectIdentity
jnxProductACX500OPOEDC = _JnxProductACX500OPOEDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 124, 1)
)
_JnxProductVariationACX5048_ObjectIdentity = ObjectIdentity
jnxProductVariationACX5048 = _JnxProductVariationACX5048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 126)
)
_JnxProductACX5048_ObjectIdentity = ObjectIdentity
jnxProductACX5048 = _JnxProductACX5048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 126, 1)
)
_JnxProductVariationACX5096_ObjectIdentity = ObjectIdentity
jnxProductVariationACX5096 = _JnxProductVariationACX5096_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 127)
)
_JnxProductACX5096_ObjectIdentity = ObjectIdentity
jnxProductACX5096 = _JnxProductACX5096_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 127, 1)
)
_JnxProductVariationLN1000CC_ObjectIdentity = ObjectIdentity
jnxProductVariationLN1000CC = _JnxProductVariationLN1000CC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 128)
)
_JnxProductVariationPTX1000_ObjectIdentity = ObjectIdentity
jnxProductVariationPTX1000 = _JnxProductVariationPTX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 130)
)
_JnxProductVariationEX3400_ObjectIdentity = ObjectIdentity
jnxProductVariationEX3400 = _JnxProductVariationEX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 131)
)
_JnxProductEX3400port24T_ObjectIdentity = ObjectIdentity
jnxProductEX3400port24T = _JnxProductEX3400port24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 131, 1)
)
_JnxProductEX3400port48T_ObjectIdentity = ObjectIdentity
jnxProductEX3400port48T = _JnxProductEX3400port48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 131, 2)
)
_JnxProductEX3400port24P_ObjectIdentity = ObjectIdentity
jnxProductEX3400port24P = _JnxProductEX3400port24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 131, 3)
)
_JnxProductEX3400port48P_ObjectIdentity = ObjectIdentity
jnxProductEX3400port48P = _JnxProductEX3400port48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 131, 4)
)
_JnxProductVariationEX2300_ObjectIdentity = ObjectIdentity
jnxProductVariationEX2300 = _JnxProductVariationEX2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 132)
)
_JnxProductEX2300port24T_ObjectIdentity = ObjectIdentity
jnxProductEX2300port24T = _JnxProductEX2300port24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 132, 1)
)
_JnxProductEX2300port48T_ObjectIdentity = ObjectIdentity
jnxProductEX2300port48T = _JnxProductEX2300port48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 132, 2)
)
_JnxProductEX2300port24P_ObjectIdentity = ObjectIdentity
jnxProductEX2300port24P = _JnxProductEX2300port24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 132, 3)
)
_JnxProductEX2300port48P_ObjectIdentity = ObjectIdentity
jnxProductEX2300port48P = _JnxProductEX2300port48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 132, 4)
)
_JnxProductEX2300Cport12T_ObjectIdentity = ObjectIdentity
jnxProductEX2300Cport12T = _JnxProductEX2300Cport12T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 132, 5)
)
_JnxProductEX2300Cport12P_ObjectIdentity = ObjectIdentity
jnxProductEX2300Cport12P = _JnxProductEX2300Cport12P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 132, 6)
)
_JnxProductEX2300port24MP_ObjectIdentity = ObjectIdentity
jnxProductEX2300port24MP = _JnxProductEX2300port24MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 132, 7)
)
_JnxProductEX2300port48MP_ObjectIdentity = ObjectIdentity
jnxProductEX2300port48MP = _JnxProductEX2300port48MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 132, 8)
)
_JnxProductVariationNFX_ObjectIdentity = ObjectIdentity
jnxProductVariationNFX = _JnxProductVariationNFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138)
)
_JnxProductNFX250ATTS1_ObjectIdentity = ObjectIdentity
jnxProductNFX250ATTS1 = _JnxProductNFX250ATTS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 1)
)
_JnxProductNFX250ATTS1SCHost_ObjectIdentity = ObjectIdentity
jnxProductNFX250ATTS1SCHost = _JnxProductNFX250ATTS1SCHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 1, 1)
)
_JnxProductNFX250ATTS1SCJdm_ObjectIdentity = ObjectIdentity
jnxProductNFX250ATTS1SCJdm = _JnxProductNFX250ATTS1SCJdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 1, 2)
)
_JnxProductNFX250ATTS1SCJcp_ObjectIdentity = ObjectIdentity
jnxProductNFX250ATTS1SCJcp = _JnxProductNFX250ATTS1SCJcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 1, 3)
)
_JnxProductNFX250ATTS2_ObjectIdentity = ObjectIdentity
jnxProductNFX250ATTS2 = _JnxProductNFX250ATTS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 2)
)
_JnxProductNFX250ATTS2SCHost_ObjectIdentity = ObjectIdentity
jnxProductNFX250ATTS2SCHost = _JnxProductNFX250ATTS2SCHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 2, 1)
)
_JnxProductNFX250ATTS2SCJdm_ObjectIdentity = ObjectIdentity
jnxProductNFX250ATTS2SCJdm = _JnxProductNFX250ATTS2SCJdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 2, 2)
)
_JnxProductNFX250ATTS2SCJcp_ObjectIdentity = ObjectIdentity
jnxProductNFX250ATTS2SCJcp = _JnxProductNFX250ATTS2SCJcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 2, 3)
)
_JnxProductNFX250ATTLS1_ObjectIdentity = ObjectIdentity
jnxProductNFX250ATTLS1 = _JnxProductNFX250ATTLS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 3)
)
_JnxProductNFX250ATTLS1SCHost_ObjectIdentity = ObjectIdentity
jnxProductNFX250ATTLS1SCHost = _JnxProductNFX250ATTLS1SCHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 3, 1)
)
_JnxProductNFX250ATTLS1SCJdm_ObjectIdentity = ObjectIdentity
jnxProductNFX250ATTLS1SCJdm = _JnxProductNFX250ATTLS1SCJdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 3, 2)
)
_JnxProductNFX250ATTLS1SCJcp_ObjectIdentity = ObjectIdentity
jnxProductNFX250ATTLS1SCJcp = _JnxProductNFX250ATTLS1SCJcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 3, 3)
)
_JnxProductNFX250S1_ObjectIdentity = ObjectIdentity
jnxProductNFX250S1 = _JnxProductNFX250S1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 4)
)
_JnxProductNFX250S1SCHost_ObjectIdentity = ObjectIdentity
jnxProductNFX250S1SCHost = _JnxProductNFX250S1SCHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 4, 1)
)
_JnxProductNFX250S1SCJdm_ObjectIdentity = ObjectIdentity
jnxProductNFX250S1SCJdm = _JnxProductNFX250S1SCJdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 4, 2)
)
_JnxProductNFX250S1SCJcp_ObjectIdentity = ObjectIdentity
jnxProductNFX250S1SCJcp = _JnxProductNFX250S1SCJcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 4, 3)
)
_JnxProductNFX250S2_ObjectIdentity = ObjectIdentity
jnxProductNFX250S2 = _JnxProductNFX250S2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 5)
)
_JnxProductNFX250S2SCHost_ObjectIdentity = ObjectIdentity
jnxProductNFX250S2SCHost = _JnxProductNFX250S2SCHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 5, 1)
)
_JnxProductNFX250S2SCJdm_ObjectIdentity = ObjectIdentity
jnxProductNFX250S2SCJdm = _JnxProductNFX250S2SCJdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 5, 2)
)
_JnxProductNFX250S2SCJcp_ObjectIdentity = ObjectIdentity
jnxProductNFX250S2SCJcp = _JnxProductNFX250S2SCJcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 5, 3)
)
_JnxProductNFX250LS1_ObjectIdentity = ObjectIdentity
jnxProductNFX250LS1 = _JnxProductNFX250LS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 6)
)
_JnxProductNFX250LS1SCHost_ObjectIdentity = ObjectIdentity
jnxProductNFX250LS1SCHost = _JnxProductNFX250LS1SCHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 6, 1)
)
_JnxProductNFX250LS1SCJdm_ObjectIdentity = ObjectIdentity
jnxProductNFX250LS1SCJdm = _JnxProductNFX250LS1SCJdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 6, 2)
)
_JnxProductNFX250LS1SCJcp_ObjectIdentity = ObjectIdentity
jnxProductNFX250LS1SCJcp = _JnxProductNFX250LS1SCJcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 6, 3)
)
_JnxProductNFXVirtual_ObjectIdentity = ObjectIdentity
jnxProductNFXVirtual = _JnxProductNFXVirtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 7)
)
_JnxProductNFXVirtualSCHost_ObjectIdentity = ObjectIdentity
jnxProductNFXVirtualSCHost = _JnxProductNFXVirtualSCHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 7, 1)
)
_JnxProductNFXVirtualSCJdm_ObjectIdentity = ObjectIdentity
jnxProductNFXVirtualSCJdm = _JnxProductNFXVirtualSCJdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 7, 2)
)
_JnxProductNFXVirtualSCJcp_ObjectIdentity = ObjectIdentity
jnxProductNFXVirtualSCJcp = _JnxProductNFXVirtualSCJcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 7, 3)
)
_JnxProductNFX250S1E_ObjectIdentity = ObjectIdentity
jnxProductNFX250S1E = _JnxProductNFX250S1E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 8)
)
_JnxProductNFX250S1ESCHost_ObjectIdentity = ObjectIdentity
jnxProductNFX250S1ESCHost = _JnxProductNFX250S1ESCHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 8, 1)
)
_JnxProductNFX250S1ESCJdm_ObjectIdentity = ObjectIdentity
jnxProductNFX250S1ESCJdm = _JnxProductNFX250S1ESCJdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 8, 2)
)
_JnxProductNFX250S1ESCJcp_ObjectIdentity = ObjectIdentity
jnxProductNFX250S1ESCJcp = _JnxProductNFX250S1ESCJcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 8, 3)
)
_JnxProductNFX150CS1_ObjectIdentity = ObjectIdentity
jnxProductNFX150CS1 = _JnxProductNFX150CS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 9)
)
_JnxProductNFX150CS1AE_ObjectIdentity = ObjectIdentity
jnxProductNFX150CS1AE = _JnxProductNFX150CS1AE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 10)
)
_JnxProductNFX150CS1AA_ObjectIdentity = ObjectIdentity
jnxProductNFX150CS1AA = _JnxProductNFX150CS1AA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 11)
)
_JnxProductNFX150S1_ObjectIdentity = ObjectIdentity
jnxProductNFX150S1 = _JnxProductNFX150S1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 12)
)
_JnxProductNFX350S1_ObjectIdentity = ObjectIdentity
jnxProductNFX350S1 = _JnxProductNFX350S1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 13)
)
_JnxProductNFXWhiteBox1_ObjectIdentity = ObjectIdentity
jnxProductNFXWhiteBox1 = _JnxProductNFXWhiteBox1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 14)
)
_JnxProductNFX150CS1EAE_ObjectIdentity = ObjectIdentity
jnxProductNFX150CS1EAE = _JnxProductNFX150CS1EAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 15)
)
_JnxProductNFX150CS1EAA_ObjectIdentity = ObjectIdentity
jnxProductNFX150CS1EAA = _JnxProductNFX150CS1EAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 16)
)
_JnxProductNFX150S1E_ObjectIdentity = ObjectIdentity
jnxProductNFX150S1E = _JnxProductNFX150S1E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 17)
)
_JnxProductNFX350S2_ObjectIdentity = ObjectIdentity
jnxProductNFX350S2 = _JnxProductNFX350S2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 18)
)
_JnxProductNFX350S3_ObjectIdentity = ObjectIdentity
jnxProductNFX350S3 = _JnxProductNFX350S3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 19)
)
_JnxProductNFXOPAL_ObjectIdentity = ObjectIdentity
jnxProductNFXOPAL = _JnxProductNFXOPAL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 20)
)
_JnxProductNFX350X_ObjectIdentity = ObjectIdentity
jnxProductNFX350X = _JnxProductNFX350X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 138, 21)
)
_JnxProductVariationJNP10003_ObjectIdentity = ObjectIdentity
jnxProductVariationJNP10003 = _JnxProductVariationJNP10003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 139)
)
_JnxProductVariationSRX4600_ObjectIdentity = ObjectIdentity
jnxProductVariationSRX4600 = _JnxProductVariationSRX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 140)
)
_JnxProductVariationSRX4800_ObjectIdentity = ObjectIdentity
jnxProductVariationSRX4800 = _JnxProductVariationSRX4800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 141)
)
_JnxProductVariationJNP204_ObjectIdentity = ObjectIdentity
jnxProductVariationJNP204 = _JnxProductVariationJNP204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 144)
)
_JnxProductVariationMX2008_ObjectIdentity = ObjectIdentity
jnxProductVariationMX2008 = _JnxProductVariationMX2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 145)
)
_JnxProductVariationMXTSR80_ObjectIdentity = ObjectIdentity
jnxProductVariationMXTSR80 = _JnxProductVariationMXTSR80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 146)
)
_JnxProductMXTSR80_ObjectIdentity = ObjectIdentity
jnxProductMXTSR80 = _JnxProductMXTSR80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 146, 1)
)
_JnxProductVariationPTX10008_ObjectIdentity = ObjectIdentity
jnxProductVariationPTX10008 = _JnxProductVariationPTX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 147)
)
_JnxProductVariationACX5448_ObjectIdentity = ObjectIdentity
jnxProductVariationACX5448 = _JnxProductVariationACX5448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 148)
)
_JnxProductACX5448_ObjectIdentity = ObjectIdentity
jnxProductACX5448 = _JnxProductACX5448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 148, 1)
)
_JnxProductVariationPTX10016_ObjectIdentity = ObjectIdentity
jnxProductVariationPTX10016 = _JnxProductVariationPTX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 150)
)
_JnxProductVariationEX9251_ObjectIdentity = ObjectIdentity
jnxProductVariationEX9251 = _JnxProductVariationEX9251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 151)
)
_JnxProductVariationJNP10001_ObjectIdentity = ObjectIdentity
jnxProductVariationJNP10001 = _JnxProductVariationJNP10001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 153)
)
_JnxProductVariationMX10008_ObjectIdentity = ObjectIdentity
jnxProductVariationMX10008 = _JnxProductVariationMX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 154)
)
_JnxProductVariationMX10016_ObjectIdentity = ObjectIdentity
jnxProductVariationMX10016 = _JnxProductVariationMX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 155)
)
_JnxProductVariationEX9253_ObjectIdentity = ObjectIdentity
jnxProductVariationEX9253 = _JnxProductVariationEX9253_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 156)
)
_JnxProductVariationACX5448M_ObjectIdentity = ObjectIdentity
jnxProductVariationACX5448M = _JnxProductVariationACX5448M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 158)
)
_JnxProductACX5448M_ObjectIdentity = ObjectIdentity
jnxProductACX5448M = _JnxProductACX5448M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 158, 1)
)
_JnxProductVariationACX5448D_ObjectIdentity = ObjectIdentity
jnxProductVariationACX5448D = _JnxProductVariationACX5448D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 159)
)
_JnxProductACX5448D_ObjectIdentity = ObjectIdentity
jnxProductACX5448D = _JnxProductACX5448D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 159, 1)
)
_JnxProductVariationACX6360OR_ObjectIdentity = ObjectIdentity
jnxProductVariationACX6360OR = _JnxProductVariationACX6360OR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 160)
)
_JnxProductVariationACX6360OX_ObjectIdentity = ObjectIdentity
jnxProductVariationACX6360OX = _JnxProductVariationACX6360OX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 161)
)
_JnxProductVariationACX710_ObjectIdentity = ObjectIdentity
jnxProductVariationACX710 = _JnxProductVariationACX710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 162)
)
_JnxProductACX710_ObjectIdentity = ObjectIdentity
jnxProductACX710 = _JnxProductACX710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 162, 1)
)
_JnxProductVariationACX5800_ObjectIdentity = ObjectIdentity
jnxProductVariationACX5800 = _JnxProductVariationACX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 163)
)
_JnxProductACX5800_ObjectIdentity = ObjectIdentity
jnxProductACX5800 = _JnxProductACX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 163, 1)
)
_JnxProductVariationEX4400_ObjectIdentity = ObjectIdentity
jnxProductVariationEX4400 = _JnxProductVariationEX4400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 165)
)
_JnxProductEX4400port48MP_ObjectIdentity = ObjectIdentity
jnxProductEX4400port48MP = _JnxProductEX4400port48MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 165, 1)
)
_JnxProductEX4400port24MP_ObjectIdentity = ObjectIdentity
jnxProductEX4400port24MP = _JnxProductEX4400port24MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 165, 2)
)
_JnxProductEX4400port48P_ObjectIdentity = ObjectIdentity
jnxProductEX4400port48P = _JnxProductEX4400port48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 165, 3)
)
_JnxProductEX4400port24P_ObjectIdentity = ObjectIdentity
jnxProductEX4400port24P = _JnxProductEX4400port24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 165, 4)
)
_JnxProductEX4400port48T_ObjectIdentity = ObjectIdentity
jnxProductEX4400port48T = _JnxProductEX4400port48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 165, 5)
)
_JnxProductEX4400port24T_ObjectIdentity = ObjectIdentity
jnxProductEX4400port24T = _JnxProductEX4400port24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 165, 6)
)
_JnxProductEX4400port48F_ObjectIdentity = ObjectIdentity
jnxProductEX4400port48F = _JnxProductEX4400port48F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 165, 7)
)
_JnxProductEX4400port24X_ObjectIdentity = ObjectIdentity
jnxProductEX4400port24X = _JnxProductEX4400port24X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 165, 8)
)
_JnxProductVariationR6675_ObjectIdentity = ObjectIdentity
jnxProductVariationR6675 = _JnxProductVariationR6675_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 166)
)
_JnxProductR6675_ObjectIdentity = ObjectIdentity
jnxProductR6675 = _JnxProductR6675_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 166, 1)
)
_JnxProductVariationMX304_ObjectIdentity = ObjectIdentity
jnxProductVariationMX304 = _JnxProductVariationMX304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 167)
)
_JnxProductVariationMX10004_ObjectIdentity = ObjectIdentity
jnxProductVariationMX10004 = _JnxProductVariationMX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 168)
)
_JnxProductVariationEX4100_ObjectIdentity = ObjectIdentity
jnxProductVariationEX4100 = _JnxProductVariationEX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169)
)
_JnxProductEX4100port48MP_ObjectIdentity = ObjectIdentity
jnxProductEX4100port48MP = _JnxProductEX4100port48MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169, 1)
)
_JnxProductEX4100port24MP_ObjectIdentity = ObjectIdentity
jnxProductEX4100port24MP = _JnxProductEX4100port24MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169, 2)
)
_JnxProductEX4100port48P_ObjectIdentity = ObjectIdentity
jnxProductEX4100port48P = _JnxProductEX4100port48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169, 3)
)
_JnxProductEX4100port24P_ObjectIdentity = ObjectIdentity
jnxProductEX4100port24P = _JnxProductEX4100port24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169, 4)
)
_JnxProductEX4100port48T_ObjectIdentity = ObjectIdentity
jnxProductEX4100port48T = _JnxProductEX4100port48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169, 5)
)
_JnxProductEX4100port24T_ObjectIdentity = ObjectIdentity
jnxProductEX4100port24T = _JnxProductEX4100port24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169, 6)
)
_JnxProductEX4100portF48P_ObjectIdentity = ObjectIdentity
jnxProductEX4100portF48P = _JnxProductEX4100portF48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169, 7)
)
_JnxProductEX4100portF24P_ObjectIdentity = ObjectIdentity
jnxProductEX4100portF24P = _JnxProductEX4100portF24P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169, 8)
)
_JnxProductEX4100portF48T_ObjectIdentity = ObjectIdentity
jnxProductEX4100portF48T = _JnxProductEX4100portF48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169, 9)
)
_JnxProductEX4100portF24T_ObjectIdentity = ObjectIdentity
jnxProductEX4100portF24T = _JnxProductEX4100portF24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169, 10)
)
_JnxProductEX4100portF12P_ObjectIdentity = ObjectIdentity
jnxProductEX4100portF12P = _JnxProductEX4100portF12P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169, 11)
)
_JnxProductEX4100portF12T_ObjectIdentity = ObjectIdentity
jnxProductEX4100portF12T = _JnxProductEX4100portF12T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169, 12)
)
_JnxProductEX4100portH12MP_ObjectIdentity = ObjectIdentity
jnxProductEX4100portH12MP = _JnxProductEX4100portH12MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169, 13)
)
_JnxProductEX4100portH24MP_ObjectIdentity = ObjectIdentity
jnxProductEX4100portH24MP = _JnxProductEX4100portH24MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169, 14)
)
_JnxProductEX4100portH24F_ObjectIdentity = ObjectIdentity
jnxProductEX4100portH24F = _JnxProductEX4100portH24F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 169, 15)
)
_JnxProductVariationEX4650_ObjectIdentity = ObjectIdentity
jnxProductVariationEX4650 = _JnxProductVariationEX4650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 508)
)
_JnxProductEX465048Y8C_ObjectIdentity = ObjectIdentity
jnxProductEX465048Y8C = _JnxProductEX465048Y8C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 508, 1)
)
_JnxProductVariationPTX1000260C_ObjectIdentity = ObjectIdentity
jnxProductVariationPTX1000260C = _JnxProductVariationPTX1000260C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 513)
)
_JnxProductVariationPTX1000380c_ObjectIdentity = ObjectIdentity
jnxProductVariationPTX1000380c = _JnxProductVariationPTX1000380c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 523)
)
_JnxProductVariationPTX10003160c_ObjectIdentity = ObjectIdentity
jnxProductVariationPTX10003160c = _JnxProductVariationPTX10003160c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 524)
)
_JnxProductVariationQFX1000380c_ObjectIdentity = ObjectIdentity
jnxProductVariationQFX1000380c = _JnxProductVariationQFX1000380c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 525)
)
_JnxProductVariationQFX10003160c_ObjectIdentity = ObjectIdentity
jnxProductVariationQFX10003160c = _JnxProductVariationQFX10003160c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 526)
)
_JnxProductVariationPTX1000136mr_ObjectIdentity = ObjectIdentity
jnxProductVariationPTX1000136mr = _JnxProductVariationPTX1000136mr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 555)
)
_JnxProductVariationPTX10004_ObjectIdentity = ObjectIdentity
jnxProductVariationPTX10004 = _JnxProductVariationPTX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 570)
)
_JnxProductVariationACX753_ObjectIdentity = ObjectIdentity
jnxProductVariationACX753 = _JnxProductVariationACX753_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 576)
)
_JnxProductVariationACX7KSwitch_ObjectIdentity = ObjectIdentity
jnxProductVariationACX7KSwitch = _JnxProductVariationACX7KSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 578)
)
_JnxProductACX710032C_ObjectIdentity = ObjectIdentity
jnxProductACX710032C = _JnxProductACX710032C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 578, 1)
)
_JnxProductACX710048L_ObjectIdentity = ObjectIdentity
jnxProductACX710048L = _JnxProductACX710048L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 578, 2)
)
_JnxProductACX7509_ObjectIdentity = ObjectIdentity
jnxProductACX7509 = _JnxProductACX7509_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 578, 3)
)
_JnxProductVariationACX710032c_ObjectIdentity = ObjectIdentity
jnxProductVariationACX710032c = _JnxProductVariationACX710032c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 579)
)
_JnxProductVariationACX710048l_ObjectIdentity = ObjectIdentity
jnxProductVariationACX710048l = _JnxProductVariationACX710048l_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 580)
)
_JnxProductVariationACX7908_ObjectIdentity = ObjectIdentity
jnxProductVariationACX7908 = _JnxProductVariationACX7908_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 581)
)
_JnxProductVariationACX7024_ObjectIdentity = ObjectIdentity
jnxProductVariationACX7024 = _JnxProductVariationACX7024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 582)
)
_JnxProductVariationACX7332_ObjectIdentity = ObjectIdentity
jnxProductVariationACX7332 = _JnxProductVariationACX7332_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 586)
)
_JnxProductVariationACX7348_ObjectIdentity = ObjectIdentity
jnxProductVariationACX7348 = _JnxProductVariationACX7348_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 587)
)
_JnxProductVariationACX7024X_ObjectIdentity = ObjectIdentity
jnxProductVariationACX7024X = _JnxProductVariationACX7024X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 588)
)
_JnxProductVariationPTX1000236qdd_ObjectIdentity = ObjectIdentity
jnxProductVariationPTX1000236qdd = _JnxProductVariationPTX1000236qdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 1, 4, 589)
)
_JnxClassContainers_ObjectIdentity = ObjectIdentity
jnxClassContainers = _JnxClassContainers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2)
)
_JnxChassis_ObjectIdentity = ObjectIdentity
jnxChassis = _JnxChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1)
)
_JnxChassisM40_ObjectIdentity = ObjectIdentity
jnxChassisM40 = _JnxChassisM40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 1)
)
_JnxChassisM20_ObjectIdentity = ObjectIdentity
jnxChassisM20 = _JnxChassisM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 2)
)
_JnxChassisM160_ObjectIdentity = ObjectIdentity
jnxChassisM160 = _JnxChassisM160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 3)
)
_JnxChassisM10_ObjectIdentity = ObjectIdentity
jnxChassisM10 = _JnxChassisM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 4)
)
_JnxChassisM5_ObjectIdentity = ObjectIdentity
jnxChassisM5 = _JnxChassisM5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 5)
)
_JnxChassisT640_ObjectIdentity = ObjectIdentity
jnxChassisT640 = _JnxChassisT640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 6)
)
_JnxChassisT320_ObjectIdentity = ObjectIdentity
jnxChassisT320 = _JnxChassisT320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 7)
)
_JnxChassisM40e_ObjectIdentity = ObjectIdentity
jnxChassisM40e = _JnxChassisM40e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 8)
)
_JnxChassisM320_ObjectIdentity = ObjectIdentity
jnxChassisM320 = _JnxChassisM320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 9)
)
_JnxChassisM7i_ObjectIdentity = ObjectIdentity
jnxChassisM7i = _JnxChassisM7i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 10)
)
_JnxChassisM10i_ObjectIdentity = ObjectIdentity
jnxChassisM10i = _JnxChassisM10i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 11)
)
_JnxChassisJ2300_ObjectIdentity = ObjectIdentity
jnxChassisJ2300 = _JnxChassisJ2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 13)
)
_JnxChassisJ4300_ObjectIdentity = ObjectIdentity
jnxChassisJ4300 = _JnxChassisJ4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 14)
)
_JnxChassisJ6300_ObjectIdentity = ObjectIdentity
jnxChassisJ6300 = _JnxChassisJ6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 15)
)
_JnxChassisIRM_ObjectIdentity = ObjectIdentity
jnxChassisIRM = _JnxChassisIRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 16)
)
_JnxChassisTX_ObjectIdentity = ObjectIdentity
jnxChassisTX = _JnxChassisTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 17)
)
_JnxChassisM120_ObjectIdentity = ObjectIdentity
jnxChassisM120 = _JnxChassisM120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 18)
)
_JnxChassisJ4350_ObjectIdentity = ObjectIdentity
jnxChassisJ4350 = _JnxChassisJ4350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 19)
)
_JnxChassisJ6350_ObjectIdentity = ObjectIdentity
jnxChassisJ6350 = _JnxChassisJ6350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 20)
)
_JnxChassisMX960_ObjectIdentity = ObjectIdentity
jnxChassisMX960 = _JnxChassisMX960_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 21)
)
_JnxChassisJ4320_ObjectIdentity = ObjectIdentity
jnxChassisJ4320 = _JnxChassisJ4320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 22)
)
_JnxChassisJ2320_ObjectIdentity = ObjectIdentity
jnxChassisJ2320 = _JnxChassisJ2320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 23)
)
_JnxChassisJ2350_ObjectIdentity = ObjectIdentity
jnxChassisJ2350 = _JnxChassisJ2350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 24)
)
_JnxChassisMX480_ObjectIdentity = ObjectIdentity
jnxChassisMX480 = _JnxChassisMX480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 25)
)
_JnxChassisSRX5800_ObjectIdentity = ObjectIdentity
jnxChassisSRX5800 = _JnxChassisSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 26)
)
_JnxChassisT1600_ObjectIdentity = ObjectIdentity
jnxChassisT1600 = _JnxChassisT1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 27)
)
_JnxChassisSRX5600_ObjectIdentity = ObjectIdentity
jnxChassisSRX5600 = _JnxChassisSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 28)
)
_JnxChassisMX240_ObjectIdentity = ObjectIdentity
jnxChassisMX240 = _JnxChassisMX240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 29)
)
_JnxChassisEX3200_ObjectIdentity = ObjectIdentity
jnxChassisEX3200 = _JnxChassisEX3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 30)
)
_JnxChassisEX4200_ObjectIdentity = ObjectIdentity
jnxChassisEX4200 = _JnxChassisEX4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 31)
)
_JnxEX4200RE0_ObjectIdentity = ObjectIdentity
jnxEX4200RE0 = _JnxEX4200RE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 31, 1)
)
_JnxEX4200RE1_ObjectIdentity = ObjectIdentity
jnxEX4200RE1 = _JnxEX4200RE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 31, 2)
)
_JnxChassisEX8208_ObjectIdentity = ObjectIdentity
jnxChassisEX8208 = _JnxChassisEX8208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 32)
)
_JnxChassisEX8216_ObjectIdentity = ObjectIdentity
jnxChassisEX8216 = _JnxChassisEX8216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 33)
)
_JnxChassisSRX3600_ObjectIdentity = ObjectIdentity
jnxChassisSRX3600 = _JnxChassisSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 34)
)
_JnxChassisSRX3400_ObjectIdentity = ObjectIdentity
jnxChassisSRX3400 = _JnxChassisSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 35)
)
_JnxChassisSRX210_ObjectIdentity = ObjectIdentity
jnxChassisSRX210 = _JnxChassisSRX210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 36)
)
_JnxChassisTXP_ObjectIdentity = ObjectIdentity
jnxChassisTXP = _JnxChassisTXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 37)
)
_JnxChassisJCS_ObjectIdentity = ObjectIdentity
jnxChassisJCS = _JnxChassisJCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 38)
)
_JnxChassisSRX240_ObjectIdentity = ObjectIdentity
jnxChassisSRX240 = _JnxChassisSRX240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 39)
)
_JnxChassisSRX650_ObjectIdentity = ObjectIdentity
jnxChassisSRX650 = _JnxChassisSRX650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 40)
)
_JnxChassisSRX100_ObjectIdentity = ObjectIdentity
jnxChassisSRX100 = _JnxChassisSRX100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 41)
)
_JnxChassisLN1000V_ObjectIdentity = ObjectIdentity
jnxChassisLN1000V = _JnxChassisLN1000V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 42)
)
_JnxChassisEX2200_ObjectIdentity = ObjectIdentity
jnxChassisEX2200 = _JnxChassisEX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 43)
)
_JnxChassisEX4500_ObjectIdentity = ObjectIdentity
jnxChassisEX4500 = _JnxChassisEX4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 44)
)
_JnxEX4500RE0_ObjectIdentity = ObjectIdentity
jnxEX4500RE0 = _JnxEX4500RE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 44, 1)
)
_JnxEX4500RE1_ObjectIdentity = ObjectIdentity
jnxEX4500RE1 = _JnxEX4500RE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 44, 2)
)
_JnxChassisFXChassis_ObjectIdentity = ObjectIdentity
jnxChassisFXChassis = _JnxChassisFXChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 45)
)
_JnxChassisIBM4274M02J02M_ObjectIdentity = ObjectIdentity
jnxChassisIBM4274M02J02M = _JnxChassisIBM4274M02J02M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 46)
)
_JnxChassisIBM4274M06J06M_ObjectIdentity = ObjectIdentity
jnxChassisIBM4274M06J06M = _JnxChassisIBM4274M06J06M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 47)
)
_JnxChassisIBM4274M11J11M_ObjectIdentity = ObjectIdentity
jnxChassisIBM4274M11J11M = _JnxChassisIBM4274M11J11M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 48)
)
_JnxChassisSRX1400_ObjectIdentity = ObjectIdentity
jnxChassisSRX1400 = _JnxChassisSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 49)
)
_JnxChassisIBM4274S58J58S_ObjectIdentity = ObjectIdentity
jnxChassisIBM4274S58J58S = _JnxChassisIBM4274S58J58S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 50)
)
_JnxChassisIBM4274S56J56S_ObjectIdentity = ObjectIdentity
jnxChassisIBM4274S56J56S = _JnxChassisIBM4274S56J56S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 51)
)
_JnxChassisIBM4274S36J36S_ObjectIdentity = ObjectIdentity
jnxChassisIBM4274S36J36S = _JnxChassisIBM4274S36J36S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 52)
)
_JnxChassisIBM4274S34J34S_ObjectIdentity = ObjectIdentity
jnxChassisIBM4274S34J34S = _JnxChassisIBM4274S34J34S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 53)
)
_JnxChassisIBM427348EJ48E_ObjectIdentity = ObjectIdentity
jnxChassisIBM427348EJ48E = _JnxChassisIBM427348EJ48E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 54)
)
_JnxIBM427348EJ48ERE0_ObjectIdentity = ObjectIdentity
jnxIBM427348EJ48ERE0 = _JnxIBM427348EJ48ERE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 54, 1)
)
_JnxIBM427348EJ48ERE1_ObjectIdentity = ObjectIdentity
jnxIBM427348EJ48ERE1 = _JnxIBM427348EJ48ERE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 54, 2)
)
_JnxChassisIBM4274E08J08E_ObjectIdentity = ObjectIdentity
jnxChassisIBM4274E08J08E = _JnxChassisIBM4274E08J08E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 55)
)
_JnxChassisIBM4274E16J16E_ObjectIdentity = ObjectIdentity
jnxChassisIBM4274E16J16E = _JnxChassisIBM4274E16J16E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 56)
)
_JnxChassisMX80_ObjectIdentity = ObjectIdentity
jnxChassisMX80 = _JnxChassisMX80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 57)
)
_JnxChassisSRX220_ObjectIdentity = ObjectIdentity
jnxChassisSRX220 = _JnxChassisSRX220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 58)
)
_JnxChassisEXXRE_ObjectIdentity = ObjectIdentity
jnxChassisEXXRE = _JnxChassisEXXRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 59)
)
_JnxEXXRERE0_ObjectIdentity = ObjectIdentity
jnxEXXRERE0 = _JnxEXXRERE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 59, 1)
)
_JnxEXXRERE1_ObjectIdentity = ObjectIdentity
jnxEXXRERE1 = _JnxEXXRERE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 59, 2)
)
_JnxChassisQFXInterconnect_ObjectIdentity = ObjectIdentity
jnxChassisQFXInterconnect = _JnxChassisQFXInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 60)
)
_JnxChassisQFXNode_ObjectIdentity = ObjectIdentity
jnxChassisQFXNode = _JnxChassisQFXNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 61)
)
_JnxChassisQFXJVRE_ObjectIdentity = ObjectIdentity
jnxChassisQFXJVRE = _JnxChassisQFXJVRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 62)
)
_JnxChassisEX4300_ObjectIdentity = ObjectIdentity
jnxChassisEX4300 = _JnxChassisEX4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 63)
)
_JnxEX4300RE0_ObjectIdentity = ObjectIdentity
jnxEX4300RE0 = _JnxEX4300RE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 63, 1)
)
_JnxEX4300RE1_ObjectIdentity = ObjectIdentity
jnxEX4300RE1 = _JnxEX4300RE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 63, 2)
)
_JnxEX4300MPRE0_ObjectIdentity = ObjectIdentity
jnxEX4300MPRE0 = _JnxEX4300MPRE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 63, 3)
)
_JnxChassisSRX110_ObjectIdentity = ObjectIdentity
jnxChassisSRX110 = _JnxChassisSRX110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 64)
)
_JnxChassisSRX120_ObjectIdentity = ObjectIdentity
jnxChassisSRX120 = _JnxChassisSRX120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 65)
)
_JnxChassisMAG8600_ObjectIdentity = ObjectIdentity
jnxChassisMAG8600 = _JnxChassisMAG8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 66)
)
_JnxChassisMAG6611_ObjectIdentity = ObjectIdentity
jnxChassisMAG6611 = _JnxChassisMAG6611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 67)
)
_JnxChassisMAG6610_ObjectIdentity = ObjectIdentity
jnxChassisMAG6610 = _JnxChassisMAG6610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 68)
)
_JnxChassisPTX5000_ObjectIdentity = ObjectIdentity
jnxChassisPTX5000 = _JnxChassisPTX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 69)
)
_JnxChassisIBM0719J45E_ObjectIdentity = ObjectIdentity
jnxChassisIBM0719J45E = _JnxChassisIBM0719J45E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 71)
)
_JnxIBM0719J45ERE0_ObjectIdentity = ObjectIdentity
jnxIBM0719J45ERE0 = _JnxIBM0719J45ERE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 71, 1)
)
_JnxIBM0719J45ERE1_ObjectIdentity = ObjectIdentity
jnxIBM0719J45ERE1 = _JnxIBM0719J45ERE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 71, 2)
)
_JnxChassisIBMJ08F_ObjectIdentity = ObjectIdentity
jnxChassisIBMJ08F = _JnxChassisIBMJ08F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 72)
)
_JnxChassisIBMJ52F_ObjectIdentity = ObjectIdentity
jnxChassisIBMJ52F = _JnxChassisIBMJ52F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 73)
)
_JnxChassisEX6210_ObjectIdentity = ObjectIdentity
jnxChassisEX6210 = _JnxChassisEX6210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 74)
)
_JnxChassisDellJFX3500_ObjectIdentity = ObjectIdentity
jnxChassisDellJFX3500 = _JnxChassisDellJFX3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 75)
)
_JnxChassisEX3300_ObjectIdentity = ObjectIdentity
jnxChassisEX3300 = _JnxChassisEX3300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 76)
)
_JnxEX3300RE0_ObjectIdentity = ObjectIdentity
jnxEX3300RE0 = _JnxEX3300RE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 76, 1)
)
_JnxEX3300RE1_ObjectIdentity = ObjectIdentity
jnxEX3300RE1 = _JnxEX3300RE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 76, 2)
)
_JnxChassisDELLJSRX3600_ObjectIdentity = ObjectIdentity
jnxChassisDELLJSRX3600 = _JnxChassisDELLJSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 77)
)
_JnxChassisDELLJSRX3400_ObjectIdentity = ObjectIdentity
jnxChassisDELLJSRX3400 = _JnxChassisDELLJSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 78)
)
_JnxChassisDELLJSRX1400_ObjectIdentity = ObjectIdentity
jnxChassisDELLJSRX1400 = _JnxChassisDELLJSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 79)
)
_JnxChassisDELLJSRX5800_ObjectIdentity = ObjectIdentity
jnxChassisDELLJSRX5800 = _JnxChassisDELLJSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 80)
)
_JnxChassisDELLJSRX5600_ObjectIdentity = ObjectIdentity
jnxChassisDELLJSRX5600 = _JnxChassisDELLJSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 81)
)
_JnxChassisQFXSwitch_ObjectIdentity = ObjectIdentity
jnxChassisQFXSwitch = _JnxChassisQFXSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 82)
)
_JnxChassisT4000_ObjectIdentity = ObjectIdentity
jnxChassisT4000 = _JnxChassisT4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 83)
)
_JnxChassisQFX3000_ObjectIdentity = ObjectIdentity
jnxChassisQFX3000 = _JnxChassisQFX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 84)
)
_JnxChassisQFX5000_ObjectIdentity = ObjectIdentity
jnxChassisQFX5000 = _JnxChassisQFX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 85)
)
_JnxChassisSRX550_ObjectIdentity = ObjectIdentity
jnxChassisSRX550 = _JnxChassisSRX550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 86)
)
_JnxChassisACX_ObjectIdentity = ObjectIdentity
jnxChassisACX = _JnxChassisACX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 87)
)
_JnxChassisMX40_ObjectIdentity = ObjectIdentity
jnxChassisMX40 = _JnxChassisMX40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 88)
)
_JnxChassisMX10_ObjectIdentity = ObjectIdentity
jnxChassisMX10 = _JnxChassisMX10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 89)
)
_JnxChassisMX5_ObjectIdentity = ObjectIdentity
jnxChassisMX5 = _JnxChassisMX5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 90)
)
_JnxChassisQFXMInterconnect_ObjectIdentity = ObjectIdentity
jnxChassisQFXMInterconnect = _JnxChassisQFXMInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 91)
)
_JnxChassisEX4550_ObjectIdentity = ObjectIdentity
jnxChassisEX4550 = _JnxChassisEX4550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 92)
)
_JnxEX4550RE0_ObjectIdentity = ObjectIdentity
jnxEX4550RE0 = _JnxEX4550RE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 92, 1)
)
_JnxEX4550RE1_ObjectIdentity = ObjectIdentity
jnxEX4550RE1 = _JnxEX4550RE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 92, 2)
)
_JnxChassisMX2020_ObjectIdentity = ObjectIdentity
jnxChassisMX2020 = _JnxChassisMX2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 93)
)
_JnxChassisVseries_ObjectIdentity = ObjectIdentity
jnxChassisVseries = _JnxChassisVseries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 94)
)
_JnxChassisLN2600_ObjectIdentity = ObjectIdentity
jnxChassisLN2600 = _JnxChassisLN2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 95)
)
_JnxChassisFireflyPerimeter_ObjectIdentity = ObjectIdentity
jnxChassisFireflyPerimeter = _JnxChassisFireflyPerimeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 96)
)
_JnxChassisMX104_ObjectIdentity = ObjectIdentity
jnxChassisMX104 = _JnxChassisMX104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 97)
)
_JnxChassisPTX3000_ObjectIdentity = ObjectIdentity
jnxChassisPTX3000 = _JnxChassisPTX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 98)
)
_JnxChassisMX2010_ObjectIdentity = ObjectIdentity
jnxChassisMX2010 = _JnxChassisMX2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 99)
)
_JnxChassisQFX3100_ObjectIdentity = ObjectIdentity
jnxChassisQFX3100 = _JnxChassisQFX3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 100)
)
_JnxChassisLN2800_ObjectIdentity = ObjectIdentity
jnxChassisLN2800 = _JnxChassisLN2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 101)
)
_JnxChassisEX9214_ObjectIdentity = ObjectIdentity
jnxChassisEX9214 = _JnxChassisEX9214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 102)
)
_JnxChassisEX9208_ObjectIdentity = ObjectIdentity
jnxChassisEX9208 = _JnxChassisEX9208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 103)
)
_JnxChassisEX9204_ObjectIdentity = ObjectIdentity
jnxChassisEX9204 = _JnxChassisEX9204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 104)
)
_JnxChassisSRX5400_ObjectIdentity = ObjectIdentity
jnxChassisSRX5400 = _JnxChassisSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 105)
)
_JnxChassisIBM4274S54J54S_ObjectIdentity = ObjectIdentity
jnxChassisIBM4274S54J54S = _JnxChassisIBM4274S54J54S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 106)
)
_JnxChassisDELLJSRX5400_ObjectIdentity = ObjectIdentity
jnxChassisDELLJSRX5400 = _JnxChassisDELLJSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 107)
)
_JnxChassisVMX_ObjectIdentity = ObjectIdentity
jnxChassisVMX = _JnxChassisVMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 108)
)
_JnxChassisEX4600_ObjectIdentity = ObjectIdentity
jnxChassisEX4600 = _JnxChassisEX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 109)
)
_JnxChassisVRR_ObjectIdentity = ObjectIdentity
jnxChassisVRR = _JnxChassisVRR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 110)
)
_JnxChassisACX1000_ObjectIdentity = ObjectIdentity
jnxChassisACX1000 = _JnxChassisACX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 113)
)
_JnxChassisACX2000_ObjectIdentity = ObjectIdentity
jnxChassisACX2000 = _JnxChassisACX2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 114)
)
_JnxChassisACX1100_ObjectIdentity = ObjectIdentity
jnxChassisACX1100 = _JnxChassisACX1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 115)
)
_JnxChassisACX2100_ObjectIdentity = ObjectIdentity
jnxChassisACX2100 = _JnxChassisACX2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 116)
)
_JnxChassisACX2200_ObjectIdentity = ObjectIdentity
jnxChassisACX2200 = _JnxChassisACX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 117)
)
_JnxChassisACX4000_ObjectIdentity = ObjectIdentity
jnxChassisACX4000 = _JnxChassisACX4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 118)
)
_JnxChassisACX500AC_ObjectIdentity = ObjectIdentity
jnxChassisACX500AC = _JnxChassisACX500AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 119)
)
_JnxChassisACX500DC_ObjectIdentity = ObjectIdentity
jnxChassisACX500DC = _JnxChassisACX500DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 120)
)
_JnxChassisACX500OAC_ObjectIdentity = ObjectIdentity
jnxChassisACX500OAC = _JnxChassisACX500OAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 121)
)
_JnxChassisACX500ODC_ObjectIdentity = ObjectIdentity
jnxChassisACX500ODC = _JnxChassisACX500ODC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 122)
)
_JnxChassisACX500OPOEAC_ObjectIdentity = ObjectIdentity
jnxChassisACX500OPOEAC = _JnxChassisACX500OPOEAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 123)
)
_JnxChassisACX500OPOEDC_ObjectIdentity = ObjectIdentity
jnxChassisACX500OPOEDC = _JnxChassisACX500OPOEDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 124)
)
_JnxChassisSatelliteDevice_ObjectIdentity = ObjectIdentity
jnxChassisSatelliteDevice = _JnxChassisSatelliteDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 125)
)
_JnxChassisACX5048_ObjectIdentity = ObjectIdentity
jnxChassisACX5048 = _JnxChassisACX5048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 126)
)
_JnxChassisACX5096_ObjectIdentity = ObjectIdentity
jnxChassisACX5096 = _JnxChassisACX5096_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 127)
)
_JnxChassisLN1000CC_ObjectIdentity = ObjectIdentity
jnxChassisLN1000CC = _JnxChassisLN1000CC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 128)
)
_JnxChassisVSRX_ObjectIdentity = ObjectIdentity
jnxChassisVSRX = _JnxChassisVSRX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 129)
)
_JnxChassisPTX1000_ObjectIdentity = ObjectIdentity
jnxChassisPTX1000 = _JnxChassisPTX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 130)
)
_JnxChassisEX3400_ObjectIdentity = ObjectIdentity
jnxChassisEX3400 = _JnxChassisEX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 131)
)
_JnxEX3400RE0_ObjectIdentity = ObjectIdentity
jnxEX3400RE0 = _JnxEX3400RE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 131, 1)
)
_JnxEX3400RE1_ObjectIdentity = ObjectIdentity
jnxEX3400RE1 = _JnxEX3400RE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 131, 2)
)
_JnxChassisEX2300_ObjectIdentity = ObjectIdentity
jnxChassisEX2300 = _JnxChassisEX2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 132)
)
_JnxEX2300RE0_ObjectIdentity = ObjectIdentity
jnxEX2300RE0 = _JnxEX2300RE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 132, 1)
)
_JnxEX2300RE1_ObjectIdentity = ObjectIdentity
jnxEX2300RE1 = _JnxEX2300RE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 132, 2)
)
_JnxChassisSRX300_ObjectIdentity = ObjectIdentity
jnxChassisSRX300 = _JnxChassisSRX300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 133)
)
_JnxChassisSRX320_ObjectIdentity = ObjectIdentity
jnxChassisSRX320 = _JnxChassisSRX320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 134)
)
_JnxChassisSRX340_ObjectIdentity = ObjectIdentity
jnxChassisSRX340 = _JnxChassisSRX340_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 135)
)
_JnxChassisSRX345_ObjectIdentity = ObjectIdentity
jnxChassisSRX345 = _JnxChassisSRX345_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 136)
)
_JnxChassisSRX1500_ObjectIdentity = ObjectIdentity
jnxChassisSRX1500 = _JnxChassisSRX1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 137)
)
_JnxChassisNFX_ObjectIdentity = ObjectIdentity
jnxChassisNFX = _JnxChassisNFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 138)
)
_JnxChassisJNP10003_ObjectIdentity = ObjectIdentity
jnxChassisJNP10003 = _JnxChassisJNP10003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 139)
)
_JnxChassisSRX4600_ObjectIdentity = ObjectIdentity
jnxChassisSRX4600 = _JnxChassisSRX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 140)
)
_JnxChassisSRX4800_ObjectIdentity = ObjectIdentity
jnxChassisSRX4800 = _JnxChassisSRX4800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 141)
)
_JnxChassisSRX4100_ObjectIdentity = ObjectIdentity
jnxChassisSRX4100 = _JnxChassisSRX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 142)
)
_JnxChassisSRX4200_ObjectIdentity = ObjectIdentity
jnxChassisSRX4200 = _JnxChassisSRX4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 143)
)
_JnxChassisJNP204_ObjectIdentity = ObjectIdentity
jnxChassisJNP204 = _JnxChassisJNP204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 144)
)
_JnxChassisMX2008_ObjectIdentity = ObjectIdentity
jnxChassisMX2008 = _JnxChassisMX2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 145)
)
_JnxChassisMXTSR80_ObjectIdentity = ObjectIdentity
jnxChassisMXTSR80 = _JnxChassisMXTSR80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 146)
)
_JnxChassisPTX10008_ObjectIdentity = ObjectIdentity
jnxChassisPTX10008 = _JnxChassisPTX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 147)
)
_JnxChassisACX5448_ObjectIdentity = ObjectIdentity
jnxChassisACX5448 = _JnxChassisACX5448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 148)
)
_JnxChassisPTX10016_ObjectIdentity = ObjectIdentity
jnxChassisPTX10016 = _JnxChassisPTX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 150)
)
_JnxChassisEX9251_ObjectIdentity = ObjectIdentity
jnxChassisEX9251 = _JnxChassisEX9251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 151)
)
_JnxChassisMX150_ObjectIdentity = ObjectIdentity
jnxChassisMX150 = _JnxChassisMX150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 152)
)
_JnxChassisJNP10001_ObjectIdentity = ObjectIdentity
jnxChassisJNP10001 = _JnxChassisJNP10001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 153)
)
_JnxChassisMX10008_ObjectIdentity = ObjectIdentity
jnxChassisMX10008 = _JnxChassisMX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 154)
)
_JnxChassisMX10016_ObjectIdentity = ObjectIdentity
jnxChassisMX10016 = _JnxChassisMX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 155)
)
_JnxChassisEX9253_ObjectIdentity = ObjectIdentity
jnxChassisEX9253 = _JnxChassisEX9253_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 156)
)
_JnxChassisJRR200_ObjectIdentity = ObjectIdentity
jnxChassisJRR200 = _JnxChassisJRR200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 157)
)
_JnxChassisACX5448M_ObjectIdentity = ObjectIdentity
jnxChassisACX5448M = _JnxChassisACX5448M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 158)
)
_JnxChassisACX5448D_ObjectIdentity = ObjectIdentity
jnxChassisACX5448D = _JnxChassisACX5448D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 159)
)
_JnxChassisACX6360OR_ObjectIdentity = ObjectIdentity
jnxChassisACX6360OR = _JnxChassisACX6360OR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 160)
)
_JnxChassisACX6360OX_ObjectIdentity = ObjectIdentity
jnxChassisACX6360OX = _JnxChassisACX6360OX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 161)
)
_JnxChassisACX710_ObjectIdentity = ObjectIdentity
jnxChassisACX710 = _JnxChassisACX710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 162)
)
_JnxChassisACX5800_ObjectIdentity = ObjectIdentity
jnxChassisACX5800 = _JnxChassisACX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 163)
)
_JnxChassisSRX380_ObjectIdentity = ObjectIdentity
jnxChassisSRX380 = _JnxChassisSRX380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 164)
)
_JnxChassisEX4400_ObjectIdentity = ObjectIdentity
jnxChassisEX4400 = _JnxChassisEX4400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 165)
)
_JnxEX4400RE0_ObjectIdentity = ObjectIdentity
jnxEX4400RE0 = _JnxEX4400RE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 165, 1)
)
_JnxEX4400RE1_ObjectIdentity = ObjectIdentity
jnxEX4400RE1 = _JnxEX4400RE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 165, 2)
)
_JnxChassisR6675_ObjectIdentity = ObjectIdentity
jnxChassisR6675 = _JnxChassisR6675_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 166)
)
_JnxChassisMX304_ObjectIdentity = ObjectIdentity
jnxChassisMX304 = _JnxChassisMX304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 167)
)
_JnxChassisMX10004_ObjectIdentity = ObjectIdentity
jnxChassisMX10004 = _JnxChassisMX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 168)
)
_JnxChassisEX4100_ObjectIdentity = ObjectIdentity
jnxChassisEX4100 = _JnxChassisEX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 169)
)
_JnxEX4100RE0_ObjectIdentity = ObjectIdentity
jnxEX4100RE0 = _JnxEX4100RE0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 169, 1)
)
_JnxEX4100RE1_ObjectIdentity = ObjectIdentity
jnxEX4100RE1 = _JnxEX4100RE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 169, 2)
)
_JnxChassisEX4650_ObjectIdentity = ObjectIdentity
jnxChassisEX4650 = _JnxChassisEX4650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 508)
)
_JnxChassisPTX1000260C_ObjectIdentity = ObjectIdentity
jnxChassisPTX1000260C = _JnxChassisPTX1000260C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 513)
)
_JnxChassisPTX1000380c_ObjectIdentity = ObjectIdentity
jnxChassisPTX1000380c = _JnxChassisPTX1000380c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 523)
)
_JnxChassisPTX10003160c_ObjectIdentity = ObjectIdentity
jnxChassisPTX10003160c = _JnxChassisPTX10003160c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 524)
)
_JnxChassisQFX1000380c_ObjectIdentity = ObjectIdentity
jnxChassisQFX1000380c = _JnxChassisQFX1000380c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 525)
)
_JnxChassisQFX10003160c_ObjectIdentity = ObjectIdentity
jnxChassisQFX10003160c = _JnxChassisQFX10003160c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 526)
)
_JnxChassisPTX1000136mr_ObjectIdentity = ObjectIdentity
jnxChassisPTX1000136mr = _JnxChassisPTX1000136mr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 555)
)
_JnxChassisPTX10004_ObjectIdentity = ObjectIdentity
jnxChassisPTX10004 = _JnxChassisPTX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 570)
)
_JnxChassisACX753_ObjectIdentity = ObjectIdentity
jnxChassisACX753 = _JnxChassisACX753_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 576)
)
_JnxChassisSRX1800_ObjectIdentity = ObjectIdentity
jnxChassisSRX1800 = _JnxChassisSRX1800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 577)
)
_JnxChassisACX7KSwitch_ObjectIdentity = ObjectIdentity
jnxChassisACX7KSwitch = _JnxChassisACX7KSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 578)
)
_JnxChassisACX710032c_ObjectIdentity = ObjectIdentity
jnxChassisACX710032c = _JnxChassisACX710032c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 579)
)
_JnxChassisACX710048l_ObjectIdentity = ObjectIdentity
jnxChassisACX710048l = _JnxChassisACX710048l_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 580)
)
_JnxChassisACX7908_ObjectIdentity = ObjectIdentity
jnxChassisACX7908 = _JnxChassisACX7908_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 581)
)
_JnxChassisACX7024_ObjectIdentity = ObjectIdentity
jnxChassisACX7024 = _JnxChassisACX7024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 582)
)
_JnxChassisSRX1600_ObjectIdentity = ObjectIdentity
jnxChassisSRX1600 = _JnxChassisSRX1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 583)
)
_JnxChassisSRX2300_ObjectIdentity = ObjectIdentity
jnxChassisSRX2300 = _JnxChassisSRX2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 584)
)
_JnxChassisSRX4300_ObjectIdentity = ObjectIdentity
jnxChassisSRX4300 = _JnxChassisSRX4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 585)
)
_JnxChassisACX7332_ObjectIdentity = ObjectIdentity
jnxChassisACX7332 = _JnxChassisACX7332_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 586)
)
_JnxChassisACX7348_ObjectIdentity = ObjectIdentity
jnxChassisACX7348 = _JnxChassisACX7348_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 587)
)
_JnxChassisACX7024X_ObjectIdentity = ObjectIdentity
jnxChassisACX7024X = _JnxChassisACX7024X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 588)
)
_JnxChassisPTX1000236qdd_ObjectIdentity = ObjectIdentity
jnxChassisPTX1000236qdd = _JnxChassisPTX1000236qdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 589)
)
_JnxChassisSRX4700_ObjectIdentity = ObjectIdentity
jnxChassisSRX4700 = _JnxChassisSRX4700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 1, 590)
)
_JnxSlot_ObjectIdentity = ObjectIdentity
jnxSlot = _JnxSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2)
)
_JnxSlotM40_ObjectIdentity = ObjectIdentity
jnxSlotM40 = _JnxSlotM40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 1)
)
_JnxSlotFPC_ObjectIdentity = ObjectIdentity
jnxSlotFPC = _JnxSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 1, 1)
)
_JnxSlotSCB_ObjectIdentity = ObjectIdentity
jnxSlotSCB = _JnxSlotSCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 1, 2)
)
_JnxSlotHostCtlr_ObjectIdentity = ObjectIdentity
jnxSlotHostCtlr = _JnxSlotHostCtlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 1, 3)
)
_JnxSlotPowerSupply_ObjectIdentity = ObjectIdentity
jnxSlotPowerSupply = _JnxSlotPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 1, 4)
)
_JnxSlotCoolingImpeller_ObjectIdentity = ObjectIdentity
jnxSlotCoolingImpeller = _JnxSlotCoolingImpeller_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 1, 5)
)
_JnxSlotCoolingFan_ObjectIdentity = ObjectIdentity
jnxSlotCoolingFan = _JnxSlotCoolingFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 1, 6)
)
_JnxSlotRoutingEngine_ObjectIdentity = ObjectIdentity
jnxSlotRoutingEngine = _JnxSlotRoutingEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 1, 7)
)
_JnxSlotM20_ObjectIdentity = ObjectIdentity
jnxSlotM20 = _JnxSlotM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 2)
)
_JnxM20SlotFPC_ObjectIdentity = ObjectIdentity
jnxM20SlotFPC = _JnxM20SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 2, 1)
)
_JnxM20SlotSSB_ObjectIdentity = ObjectIdentity
jnxM20SlotSSB = _JnxM20SlotSSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 2, 2)
)
_JnxM20SlotRE_ObjectIdentity = ObjectIdentity
jnxM20SlotRE = _JnxM20SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 2, 3)
)
_JnxM20SlotPower_ObjectIdentity = ObjectIdentity
jnxM20SlotPower = _JnxM20SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 2, 4)
)
_JnxM20SlotFan_ObjectIdentity = ObjectIdentity
jnxM20SlotFan = _JnxM20SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 2, 5)
)
_JnxM20SlotFrontPanel_ObjectIdentity = ObjectIdentity
jnxM20SlotFrontPanel = _JnxM20SlotFrontPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 2, 6)
)
_JnxSlotM160_ObjectIdentity = ObjectIdentity
jnxSlotM160 = _JnxSlotM160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 3)
)
_JnxM160SlotFPC_ObjectIdentity = ObjectIdentity
jnxM160SlotFPC = _JnxM160SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 3, 1)
)
_JnxM160SlotSFM_ObjectIdentity = ObjectIdentity
jnxM160SlotSFM = _JnxM160SlotSFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 3, 2)
)
_JnxM160SlotHM_ObjectIdentity = ObjectIdentity
jnxM160SlotHM = _JnxM160SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 3, 3)
)
_JnxM160SlotPCG_ObjectIdentity = ObjectIdentity
jnxM160SlotPCG = _JnxM160SlotPCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 3, 4)
)
_JnxM160SlotPower_ObjectIdentity = ObjectIdentity
jnxM160SlotPower = _JnxM160SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 3, 5)
)
_JnxM160SlotFan_ObjectIdentity = ObjectIdentity
jnxM160SlotFan = _JnxM160SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 3, 6)
)
_JnxM160SlotMCS_ObjectIdentity = ObjectIdentity
jnxM160SlotMCS = _JnxM160SlotMCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 3, 7)
)
_JnxM160SlotFPM_ObjectIdentity = ObjectIdentity
jnxM160SlotFPM = _JnxM160SlotFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 3, 8)
)
_JnxM160SlotCIP_ObjectIdentity = ObjectIdentity
jnxM160SlotCIP = _JnxM160SlotCIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 3, 9)
)
_JnxSlotM10_ObjectIdentity = ObjectIdentity
jnxSlotM10 = _JnxSlotM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 4)
)
_JnxM10SlotFPC_ObjectIdentity = ObjectIdentity
jnxM10SlotFPC = _JnxM10SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 4, 1)
)
_JnxM10SlotFEB_ObjectIdentity = ObjectIdentity
jnxM10SlotFEB = _JnxM10SlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 4, 2)
)
_JnxM10SlotRE_ObjectIdentity = ObjectIdentity
jnxM10SlotRE = _JnxM10SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 4, 3)
)
_JnxM10SlotPower_ObjectIdentity = ObjectIdentity
jnxM10SlotPower = _JnxM10SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 4, 4)
)
_JnxM10SlotFan_ObjectIdentity = ObjectIdentity
jnxM10SlotFan = _JnxM10SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 4, 5)
)
_JnxSlotM5_ObjectIdentity = ObjectIdentity
jnxSlotM5 = _JnxSlotM5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 5)
)
_JnxM5SlotFPC_ObjectIdentity = ObjectIdentity
jnxM5SlotFPC = _JnxM5SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 5, 1)
)
_JnxM5SlotFEB_ObjectIdentity = ObjectIdentity
jnxM5SlotFEB = _JnxM5SlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 5, 2)
)
_JnxM5SlotRE_ObjectIdentity = ObjectIdentity
jnxM5SlotRE = _JnxM5SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 5, 3)
)
_JnxM5SlotPower_ObjectIdentity = ObjectIdentity
jnxM5SlotPower = _JnxM5SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 5, 4)
)
_JnxM5SlotFan_ObjectIdentity = ObjectIdentity
jnxM5SlotFan = _JnxM5SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 5, 5)
)
_JnxSlotT640_ObjectIdentity = ObjectIdentity
jnxSlotT640 = _JnxSlotT640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 6)
)
_JnxT640SlotFPC_ObjectIdentity = ObjectIdentity
jnxT640SlotFPC = _JnxT640SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 6, 1)
)
_JnxT640SlotSIB_ObjectIdentity = ObjectIdentity
jnxT640SlotSIB = _JnxT640SlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 6, 2)
)
_JnxT640SlotHM_ObjectIdentity = ObjectIdentity
jnxT640SlotHM = _JnxT640SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 6, 3)
)
_JnxT640SlotSCG_ObjectIdentity = ObjectIdentity
jnxT640SlotSCG = _JnxT640SlotSCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 6, 4)
)
_JnxT640SlotPower_ObjectIdentity = ObjectIdentity
jnxT640SlotPower = _JnxT640SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 6, 5)
)
_JnxT640SlotFan_ObjectIdentity = ObjectIdentity
jnxT640SlotFan = _JnxT640SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 6, 6)
)
_JnxT640SlotCB_ObjectIdentity = ObjectIdentity
jnxT640SlotCB = _JnxT640SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 6, 7)
)
_JnxT640SlotFPB_ObjectIdentity = ObjectIdentity
jnxT640SlotFPB = _JnxT640SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 6, 8)
)
_JnxT640SlotCIP_ObjectIdentity = ObjectIdentity
jnxT640SlotCIP = _JnxT640SlotCIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 6, 9)
)
_JnxT640SlotSPMB_ObjectIdentity = ObjectIdentity
jnxT640SlotSPMB = _JnxT640SlotSPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 6, 10)
)
_JnxT640SlotPSD_ObjectIdentity = ObjectIdentity
jnxT640SlotPSD = _JnxT640SlotPSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 6, 11)
)
_JnxSlotT320_ObjectIdentity = ObjectIdentity
jnxSlotT320 = _JnxSlotT320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 7)
)
_JnxT320SlotFPC_ObjectIdentity = ObjectIdentity
jnxT320SlotFPC = _JnxT320SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 7, 1)
)
_JnxT320SlotSIB_ObjectIdentity = ObjectIdentity
jnxT320SlotSIB = _JnxT320SlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 7, 2)
)
_JnxT320SlotHM_ObjectIdentity = ObjectIdentity
jnxT320SlotHM = _JnxT320SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 7, 3)
)
_JnxT320SlotSCG_ObjectIdentity = ObjectIdentity
jnxT320SlotSCG = _JnxT320SlotSCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 7, 4)
)
_JnxT320SlotPower_ObjectIdentity = ObjectIdentity
jnxT320SlotPower = _JnxT320SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 7, 5)
)
_JnxT320SlotFan_ObjectIdentity = ObjectIdentity
jnxT320SlotFan = _JnxT320SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 7, 6)
)
_JnxT320SlotCB_ObjectIdentity = ObjectIdentity
jnxT320SlotCB = _JnxT320SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 7, 7)
)
_JnxT320SlotFPB_ObjectIdentity = ObjectIdentity
jnxT320SlotFPB = _JnxT320SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 7, 8)
)
_JnxT320SlotCIP_ObjectIdentity = ObjectIdentity
jnxT320SlotCIP = _JnxT320SlotCIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 7, 9)
)
_JnxT320SlotSPMB_ObjectIdentity = ObjectIdentity
jnxT320SlotSPMB = _JnxT320SlotSPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 7, 10)
)
_JnxT320SlotPSD_ObjectIdentity = ObjectIdentity
jnxT320SlotPSD = _JnxT320SlotPSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 7, 11)
)
_JnxSlotM40e_ObjectIdentity = ObjectIdentity
jnxSlotM40e = _JnxSlotM40e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 8)
)
_JnxM40eSlotFPC_ObjectIdentity = ObjectIdentity
jnxM40eSlotFPC = _JnxM40eSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 8, 1)
)
_JnxM40eSlotSFM_ObjectIdentity = ObjectIdentity
jnxM40eSlotSFM = _JnxM40eSlotSFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 8, 2)
)
_JnxM40eSlotHM_ObjectIdentity = ObjectIdentity
jnxM40eSlotHM = _JnxM40eSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 8, 3)
)
_JnxM40eSlotPCG_ObjectIdentity = ObjectIdentity
jnxM40eSlotPCG = _JnxM40eSlotPCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 8, 4)
)
_JnxM40eSlotPower_ObjectIdentity = ObjectIdentity
jnxM40eSlotPower = _JnxM40eSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 8, 5)
)
_JnxM40eSlotFan_ObjectIdentity = ObjectIdentity
jnxM40eSlotFan = _JnxM40eSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 8, 6)
)
_JnxM40eSlotMCS_ObjectIdentity = ObjectIdentity
jnxM40eSlotMCS = _JnxM40eSlotMCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 8, 7)
)
_JnxM40eSlotFPM_ObjectIdentity = ObjectIdentity
jnxM40eSlotFPM = _JnxM40eSlotFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 8, 8)
)
_JnxM40eSlotCIP_ObjectIdentity = ObjectIdentity
jnxM40eSlotCIP = _JnxM40eSlotCIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 8, 9)
)
_JnxSlotM320_ObjectIdentity = ObjectIdentity
jnxSlotM320 = _JnxSlotM320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 9)
)
_JnxM320SlotFPC_ObjectIdentity = ObjectIdentity
jnxM320SlotFPC = _JnxM320SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 9, 1)
)
_JnxM320SlotSIB_ObjectIdentity = ObjectIdentity
jnxM320SlotSIB = _JnxM320SlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 9, 2)
)
_JnxM320SlotHM_ObjectIdentity = ObjectIdentity
jnxM320SlotHM = _JnxM320SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 9, 3)
)
_JnxM320SlotPower_ObjectIdentity = ObjectIdentity
jnxM320SlotPower = _JnxM320SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 9, 4)
)
_JnxM320SlotFan_ObjectIdentity = ObjectIdentity
jnxM320SlotFan = _JnxM320SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 9, 5)
)
_JnxM320SlotCB_ObjectIdentity = ObjectIdentity
jnxM320SlotCB = _JnxM320SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 9, 6)
)
_JnxM320SlotFPB_ObjectIdentity = ObjectIdentity
jnxM320SlotFPB = _JnxM320SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 9, 7)
)
_JnxM320SlotCIP_ObjectIdentity = ObjectIdentity
jnxM320SlotCIP = _JnxM320SlotCIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 9, 8)
)
_JnxSlotM7i_ObjectIdentity = ObjectIdentity
jnxSlotM7i = _JnxSlotM7i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 10)
)
_JnxM7iSlotFPC_ObjectIdentity = ObjectIdentity
jnxM7iSlotFPC = _JnxM7iSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 10, 1)
)
_JnxM7iSlotCFEB_ObjectIdentity = ObjectIdentity
jnxM7iSlotCFEB = _JnxM7iSlotCFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 10, 2)
)
_JnxM7iSlotRE_ObjectIdentity = ObjectIdentity
jnxM7iSlotRE = _JnxM7iSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 10, 3)
)
_JnxM7iSlotPower_ObjectIdentity = ObjectIdentity
jnxM7iSlotPower = _JnxM7iSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 10, 4)
)
_JnxM7iSlotFan_ObjectIdentity = ObjectIdentity
jnxM7iSlotFan = _JnxM7iSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 10, 5)
)
_JnxSlotM10i_ObjectIdentity = ObjectIdentity
jnxSlotM10i = _JnxSlotM10i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 11)
)
_JnxM10iSlotFPC_ObjectIdentity = ObjectIdentity
jnxM10iSlotFPC = _JnxM10iSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 11, 1)
)
_JnxM10iSlotCFEB_ObjectIdentity = ObjectIdentity
jnxM10iSlotCFEB = _JnxM10iSlotCFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 11, 2)
)
_JnxM10iSlotRE_ObjectIdentity = ObjectIdentity
jnxM10iSlotRE = _JnxM10iSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 11, 3)
)
_JnxM10iSlotPower_ObjectIdentity = ObjectIdentity
jnxM10iSlotPower = _JnxM10iSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 11, 4)
)
_JnxM10iSlotFan_ObjectIdentity = ObjectIdentity
jnxM10iSlotFan = _JnxM10iSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 11, 5)
)
_JnxM10iSlotHCM_ObjectIdentity = ObjectIdentity
jnxM10iSlotHCM = _JnxM10iSlotHCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 11, 6)
)
_JnxSlotJ2300_ObjectIdentity = ObjectIdentity
jnxSlotJ2300 = _JnxSlotJ2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 13)
)
_JnxJ2300SlotFPC_ObjectIdentity = ObjectIdentity
jnxJ2300SlotFPC = _JnxJ2300SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 13, 1)
)
_JnxJ2300SlotRE_ObjectIdentity = ObjectIdentity
jnxJ2300SlotRE = _JnxJ2300SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 13, 2)
)
_JnxJ2300SlotFan_ObjectIdentity = ObjectIdentity
jnxJ2300SlotFan = _JnxJ2300SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 13, 3)
)
_JnxSlotJ4300_ObjectIdentity = ObjectIdentity
jnxSlotJ4300 = _JnxSlotJ4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 14)
)
_JnxJ4300SlotFPC_ObjectIdentity = ObjectIdentity
jnxJ4300SlotFPC = _JnxJ4300SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 14, 1)
)
_JnxJ4300SlotRE_ObjectIdentity = ObjectIdentity
jnxJ4300SlotRE = _JnxJ4300SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 14, 2)
)
_JnxJ4300SlotFan_ObjectIdentity = ObjectIdentity
jnxJ4300SlotFan = _JnxJ4300SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 14, 3)
)
_JnxSlotJ6300_ObjectIdentity = ObjectIdentity
jnxSlotJ6300 = _JnxSlotJ6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 15)
)
_JnxJ6300SlotFPC_ObjectIdentity = ObjectIdentity
jnxJ6300SlotFPC = _JnxJ6300SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 15, 1)
)
_JnxJ6300SlotRE_ObjectIdentity = ObjectIdentity
jnxJ6300SlotRE = _JnxJ6300SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 15, 2)
)
_JnxJ6300SlotFan_ObjectIdentity = ObjectIdentity
jnxJ6300SlotFan = _JnxJ6300SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 15, 3)
)
_JnxSlotIRM_ObjectIdentity = ObjectIdentity
jnxSlotIRM = _JnxSlotIRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 16)
)
_JnxIRMSlotFPC_ObjectIdentity = ObjectIdentity
jnxIRMSlotFPC = _JnxIRMSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 16, 1)
)
_JnxIRMSlotCFEB_ObjectIdentity = ObjectIdentity
jnxIRMSlotCFEB = _JnxIRMSlotCFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 16, 2)
)
_JnxIRMSlotRE_ObjectIdentity = ObjectIdentity
jnxIRMSlotRE = _JnxIRMSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 16, 3)
)
_JnxIRMSlotPower_ObjectIdentity = ObjectIdentity
jnxIRMSlotPower = _JnxIRMSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 16, 4)
)
_JnxSlotTX_ObjectIdentity = ObjectIdentity
jnxSlotTX = _JnxSlotTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 17)
)
_JnxTXSlotSIB_ObjectIdentity = ObjectIdentity
jnxTXSlotSIB = _JnxTXSlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 17, 1)
)
_JnxTXSlotHM_ObjectIdentity = ObjectIdentity
jnxTXSlotHM = _JnxTXSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 17, 2)
)
_JnxTXSlotPower_ObjectIdentity = ObjectIdentity
jnxTXSlotPower = _JnxTXSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 17, 3)
)
_JnxTXSlotFan_ObjectIdentity = ObjectIdentity
jnxTXSlotFan = _JnxTXSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 17, 4)
)
_JnxTXSlotCB_ObjectIdentity = ObjectIdentity
jnxTXSlotCB = _JnxTXSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 17, 5)
)
_JnxTXSlotFPB_ObjectIdentity = ObjectIdentity
jnxTXSlotFPB = _JnxTXSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 17, 6)
)
_JnxTXSlotCIP_ObjectIdentity = ObjectIdentity
jnxTXSlotCIP = _JnxTXSlotCIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 17, 7)
)
_JnxTXSlotSPMB_ObjectIdentity = ObjectIdentity
jnxTXSlotSPMB = _JnxTXSlotSPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 17, 8)
)
_JnxTXSlotLCC_ObjectIdentity = ObjectIdentity
jnxTXSlotLCC = _JnxTXSlotLCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 17, 9)
)
_JnxSlotM120_ObjectIdentity = ObjectIdentity
jnxSlotM120 = _JnxSlotM120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 18)
)
_JnxM120SlotFPC_ObjectIdentity = ObjectIdentity
jnxM120SlotFPC = _JnxM120SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 18, 1)
)
_JnxM120SlotFEB_ObjectIdentity = ObjectIdentity
jnxM120SlotFEB = _JnxM120SlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 18, 2)
)
_JnxM120SlotHM_ObjectIdentity = ObjectIdentity
jnxM120SlotHM = _JnxM120SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 18, 3)
)
_JnxM120SlotPower_ObjectIdentity = ObjectIdentity
jnxM120SlotPower = _JnxM120SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 18, 4)
)
_JnxM120SlotFan_ObjectIdentity = ObjectIdentity
jnxM120SlotFan = _JnxM120SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 18, 5)
)
_JnxM120SlotCB_ObjectIdentity = ObjectIdentity
jnxM120SlotCB = _JnxM120SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 18, 6)
)
_JnxM120SlotFPB_ObjectIdentity = ObjectIdentity
jnxM120SlotFPB = _JnxM120SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 18, 7)
)
_JnxSlotJ4350_ObjectIdentity = ObjectIdentity
jnxSlotJ4350 = _JnxSlotJ4350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 19)
)
_JnxJ4350SlotFPC_ObjectIdentity = ObjectIdentity
jnxJ4350SlotFPC = _JnxJ4350SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 19, 1)
)
_JnxJ4350SlotRE_ObjectIdentity = ObjectIdentity
jnxJ4350SlotRE = _JnxJ4350SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 19, 2)
)
_JnxJ4350SlotPower_ObjectIdentity = ObjectIdentity
jnxJ4350SlotPower = _JnxJ4350SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 19, 3)
)
_JnxJ4350SlotFan_ObjectIdentity = ObjectIdentity
jnxJ4350SlotFan = _JnxJ4350SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 19, 4)
)
_JnxSlotJ6350_ObjectIdentity = ObjectIdentity
jnxSlotJ6350 = _JnxSlotJ6350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 20)
)
_JnxJ6350SlotFPC_ObjectIdentity = ObjectIdentity
jnxJ6350SlotFPC = _JnxJ6350SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 20, 1)
)
_JnxJ6350SlotRE_ObjectIdentity = ObjectIdentity
jnxJ6350SlotRE = _JnxJ6350SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 20, 2)
)
_JnxJ6350SlotPower_ObjectIdentity = ObjectIdentity
jnxJ6350SlotPower = _JnxJ6350SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 20, 3)
)
_JnxJ6350SlotFan_ObjectIdentity = ObjectIdentity
jnxJ6350SlotFan = _JnxJ6350SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 20, 4)
)
_JnxSlotMX960_ObjectIdentity = ObjectIdentity
jnxSlotMX960 = _JnxSlotMX960_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 21)
)
_JnxMX960SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX960SlotFPC = _JnxMX960SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 21, 1)
)
_JnxMX960SlotHM_ObjectIdentity = ObjectIdentity
jnxMX960SlotHM = _JnxMX960SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 21, 2)
)
_JnxMX960SlotPower_ObjectIdentity = ObjectIdentity
jnxMX960SlotPower = _JnxMX960SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 21, 3)
)
_JnxMX960SlotFan_ObjectIdentity = ObjectIdentity
jnxMX960SlotFan = _JnxMX960SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 21, 4)
)
_JnxMX960SlotCB_ObjectIdentity = ObjectIdentity
jnxMX960SlotCB = _JnxMX960SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 21, 5)
)
_JnxMX960SlotFPB_ObjectIdentity = ObjectIdentity
jnxMX960SlotFPB = _JnxMX960SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 21, 6)
)
_JnxSlotJ4320_ObjectIdentity = ObjectIdentity
jnxSlotJ4320 = _JnxSlotJ4320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 22)
)
_JnxJ4320SlotFPC_ObjectIdentity = ObjectIdentity
jnxJ4320SlotFPC = _JnxJ4320SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 22, 1)
)
_JnxJ4320SlotRE_ObjectIdentity = ObjectIdentity
jnxJ4320SlotRE = _JnxJ4320SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 22, 2)
)
_JnxSlotJ2320_ObjectIdentity = ObjectIdentity
jnxSlotJ2320 = _JnxSlotJ2320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 23)
)
_JnxJ2320SlotFPC_ObjectIdentity = ObjectIdentity
jnxJ2320SlotFPC = _JnxJ2320SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 23, 1)
)
_JnxJ2320SlotRE_ObjectIdentity = ObjectIdentity
jnxJ2320SlotRE = _JnxJ2320SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 23, 2)
)
_JnxJ2320SlotPower_ObjectIdentity = ObjectIdentity
jnxJ2320SlotPower = _JnxJ2320SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 23, 3)
)
_JnxJ2320SlotFan_ObjectIdentity = ObjectIdentity
jnxJ2320SlotFan = _JnxJ2320SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 23, 4)
)
_JnxSlotJ2350_ObjectIdentity = ObjectIdentity
jnxSlotJ2350 = _JnxSlotJ2350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 24)
)
_JnxJ2350SlotFPC_ObjectIdentity = ObjectIdentity
jnxJ2350SlotFPC = _JnxJ2350SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 24, 1)
)
_JnxJ2350SlotRE_ObjectIdentity = ObjectIdentity
jnxJ2350SlotRE = _JnxJ2350SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 24, 2)
)
_JnxJ2350SlotPower_ObjectIdentity = ObjectIdentity
jnxJ2350SlotPower = _JnxJ2350SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 24, 3)
)
_JnxJ2350SlotFan_ObjectIdentity = ObjectIdentity
jnxJ2350SlotFan = _JnxJ2350SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 24, 4)
)
_JnxSlotMX480_ObjectIdentity = ObjectIdentity
jnxSlotMX480 = _JnxSlotMX480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 25)
)
_JnxMX480SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX480SlotFPC = _JnxMX480SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 25, 1)
)
_JnxMX480SlotHM_ObjectIdentity = ObjectIdentity
jnxMX480SlotHM = _JnxMX480SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 25, 2)
)
_JnxMX480SlotPower_ObjectIdentity = ObjectIdentity
jnxMX480SlotPower = _JnxMX480SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 25, 3)
)
_JnxMX480SlotFan_ObjectIdentity = ObjectIdentity
jnxMX480SlotFan = _JnxMX480SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 25, 4)
)
_JnxMX480SlotCB_ObjectIdentity = ObjectIdentity
jnxMX480SlotCB = _JnxMX480SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 25, 5)
)
_JnxMX480SlotFPB_ObjectIdentity = ObjectIdentity
jnxMX480SlotFPB = _JnxMX480SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 25, 6)
)
_JnxSlotSRX5800_ObjectIdentity = ObjectIdentity
jnxSlotSRX5800 = _JnxSlotSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 26)
)
_JnxSRX5800SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX5800SlotFPC = _JnxSRX5800SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 26, 1)
)
_JnxSRX5800SlotHM_ObjectIdentity = ObjectIdentity
jnxSRX5800SlotHM = _JnxSRX5800SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 26, 2)
)
_JnxSRX5800SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX5800SlotPower = _JnxSRX5800SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 26, 3)
)
_JnxSRX5800SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX5800SlotFan = _JnxSRX5800SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 26, 4)
)
_JnxSRX5800SlotCB_ObjectIdentity = ObjectIdentity
jnxSRX5800SlotCB = _JnxSRX5800SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 26, 5)
)
_JnxSRX5800SlotFPB_ObjectIdentity = ObjectIdentity
jnxSRX5800SlotFPB = _JnxSRX5800SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 26, 6)
)
_JnxSlotT1600_ObjectIdentity = ObjectIdentity
jnxSlotT1600 = _JnxSlotT1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 27)
)
_JnxT1600SlotFPC_ObjectIdentity = ObjectIdentity
jnxT1600SlotFPC = _JnxT1600SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 27, 1)
)
_JnxT1600SlotSIB_ObjectIdentity = ObjectIdentity
jnxT1600SlotSIB = _JnxT1600SlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 27, 2)
)
_JnxT1600SlotHM_ObjectIdentity = ObjectIdentity
jnxT1600SlotHM = _JnxT1600SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 27, 3)
)
_JnxT1600SlotSCG_ObjectIdentity = ObjectIdentity
jnxT1600SlotSCG = _JnxT1600SlotSCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 27, 4)
)
_JnxT1600SlotPower_ObjectIdentity = ObjectIdentity
jnxT1600SlotPower = _JnxT1600SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 27, 5)
)
_JnxT1600SlotFan_ObjectIdentity = ObjectIdentity
jnxT1600SlotFan = _JnxT1600SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 27, 6)
)
_JnxT1600SlotCB_ObjectIdentity = ObjectIdentity
jnxT1600SlotCB = _JnxT1600SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 27, 7)
)
_JnxT1600SlotFPB_ObjectIdentity = ObjectIdentity
jnxT1600SlotFPB = _JnxT1600SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 27, 8)
)
_JnxT1600SlotCIP_ObjectIdentity = ObjectIdentity
jnxT1600SlotCIP = _JnxT1600SlotCIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 27, 9)
)
_JnxT1600SlotSPMB_ObjectIdentity = ObjectIdentity
jnxT1600SlotSPMB = _JnxT1600SlotSPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 27, 10)
)
_JnxT1600SlotPSD_ObjectIdentity = ObjectIdentity
jnxT1600SlotPSD = _JnxT1600SlotPSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 27, 11)
)
_JnxSlotSRX5600_ObjectIdentity = ObjectIdentity
jnxSlotSRX5600 = _JnxSlotSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 28)
)
_JnxSRX5600SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX5600SlotFPC = _JnxSRX5600SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 28, 1)
)
_JnxSRX5600SlotHM_ObjectIdentity = ObjectIdentity
jnxSRX5600SlotHM = _JnxSRX5600SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 28, 2)
)
_JnxSRX5600SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX5600SlotPower = _JnxSRX5600SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 28, 3)
)
_JnxSRX5600SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX5600SlotFan = _JnxSRX5600SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 28, 4)
)
_JnxSRX5600SlotCB_ObjectIdentity = ObjectIdentity
jnxSRX5600SlotCB = _JnxSRX5600SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 28, 5)
)
_JnxSRX5600SlotFPB_ObjectIdentity = ObjectIdentity
jnxSRX5600SlotFPB = _JnxSRX5600SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 28, 6)
)
_JnxSlotMX240_ObjectIdentity = ObjectIdentity
jnxSlotMX240 = _JnxSlotMX240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 29)
)
_JnxMX240SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX240SlotFPC = _JnxMX240SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 29, 1)
)
_JnxMX240SlotHM_ObjectIdentity = ObjectIdentity
jnxMX240SlotHM = _JnxMX240SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 29, 2)
)
_JnxMX240SlotPower_ObjectIdentity = ObjectIdentity
jnxMX240SlotPower = _JnxMX240SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 29, 3)
)
_JnxMX240SlotFan_ObjectIdentity = ObjectIdentity
jnxMX240SlotFan = _JnxMX240SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 29, 4)
)
_JnxMX240SlotCB_ObjectIdentity = ObjectIdentity
jnxMX240SlotCB = _JnxMX240SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 29, 5)
)
_JnxMX240SlotFPB_ObjectIdentity = ObjectIdentity
jnxMX240SlotFPB = _JnxMX240SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 29, 6)
)
_JnxSlotEX3200_ObjectIdentity = ObjectIdentity
jnxSlotEX3200 = _JnxSlotEX3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 30)
)
_JnxEX3200SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX3200SlotFPC = _JnxEX3200SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 30, 1)
)
_JnxEX3200SlotPower_ObjectIdentity = ObjectIdentity
jnxEX3200SlotPower = _JnxEX3200SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 30, 1, 1)
)
_JnxEX3200SlotFan_ObjectIdentity = ObjectIdentity
jnxEX3200SlotFan = _JnxEX3200SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 30, 1, 2)
)
_JnxEX3200SlotRE_ObjectIdentity = ObjectIdentity
jnxEX3200SlotRE = _JnxEX3200SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 30, 1, 3)
)
_JnxSlotEX4200_ObjectIdentity = ObjectIdentity
jnxSlotEX4200 = _JnxSlotEX4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 31)
)
_JnxEX4200SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX4200SlotFPC = _JnxEX4200SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 31, 1)
)
_JnxEX4200SlotPower_ObjectIdentity = ObjectIdentity
jnxEX4200SlotPower = _JnxEX4200SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 31, 1, 1)
)
_JnxEX4200SlotFan_ObjectIdentity = ObjectIdentity
jnxEX4200SlotFan = _JnxEX4200SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 31, 1, 2)
)
_JnxSlotEX8208_ObjectIdentity = ObjectIdentity
jnxSlotEX8208 = _JnxSlotEX8208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 32)
)
_JnxEX8208SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX8208SlotFPC = _JnxEX8208SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 32, 1)
)
_JnxEX8208Slot48S_ObjectIdentity = ObjectIdentity
jnxEX8208Slot48S = _JnxEX8208Slot48S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 32, 1, 1)
)
_JnxEX8208Slot48T_ObjectIdentity = ObjectIdentity
jnxEX8208Slot48T = _JnxEX8208Slot48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 32, 1, 2)
)
_JnxEX8208Slot8XS_ObjectIdentity = ObjectIdentity
jnxEX8208Slot8XS = _JnxEX8208Slot8XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 32, 1, 3)
)
_JnxEX8208HM_ObjectIdentity = ObjectIdentity
jnxEX8208HM = _JnxEX8208HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 32, 3)
)
_JnxEX8208SlotPower_ObjectIdentity = ObjectIdentity
jnxEX8208SlotPower = _JnxEX8208SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 32, 4)
)
_JnxEX8208SlotFan_ObjectIdentity = ObjectIdentity
jnxEX8208SlotFan = _JnxEX8208SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 32, 5)
)
_JnxEX8208SlotFT_ObjectIdentity = ObjectIdentity
jnxEX8208SlotFT = _JnxEX8208SlotFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 32, 5, 1)
)
_JnxEX8208SlotCBD_ObjectIdentity = ObjectIdentity
jnxEX8208SlotCBD = _JnxEX8208SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 32, 6)
)
_JnxSlotEX8216_ObjectIdentity = ObjectIdentity
jnxSlotEX8216 = _JnxSlotEX8216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 33)
)
_JnxEX8216SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX8216SlotFPC = _JnxEX8216SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 33, 1)
)
_JnxEX8216Slot48S_ObjectIdentity = ObjectIdentity
jnxEX8216Slot48S = _JnxEX8216Slot48S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 33, 1, 1)
)
_JnxEX8216Slot48T_ObjectIdentity = ObjectIdentity
jnxEX8216Slot48T = _JnxEX8216Slot48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 33, 1, 2)
)
_JnxEX8216Slot8XS_ObjectIdentity = ObjectIdentity
jnxEX8216Slot8XS = _JnxEX8216Slot8XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 33, 1, 3)
)
_JnxEX8216SIB_ObjectIdentity = ObjectIdentity
jnxEX8216SIB = _JnxEX8216SIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 33, 2)
)
_JnxEX8216HM_ObjectIdentity = ObjectIdentity
jnxEX8216HM = _JnxEX8216HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 33, 3)
)
_JnxEX8216SlotPower_ObjectIdentity = ObjectIdentity
jnxEX8216SlotPower = _JnxEX8216SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 33, 4)
)
_JnxEX8216SlotFan_ObjectIdentity = ObjectIdentity
jnxEX8216SlotFan = _JnxEX8216SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 33, 5)
)
_JnxEX8216SlotFT_ObjectIdentity = ObjectIdentity
jnxEX8216SlotFT = _JnxEX8216SlotFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 33, 5, 1)
)
_JnxEX8216SlotRFT_ObjectIdentity = ObjectIdentity
jnxEX8216SlotRFT = _JnxEX8216SlotRFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 33, 5, 2)
)
_JnxEX8216SlotCBD_ObjectIdentity = ObjectIdentity
jnxEX8216SlotCBD = _JnxEX8216SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 33, 6)
)
_JnxSlotSRX3600_ObjectIdentity = ObjectIdentity
jnxSlotSRX3600 = _JnxSlotSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 34)
)
_JnxSRX3600SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX3600SlotFPC = _JnxSRX3600SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 34, 1)
)
_JnxSRX3600SlotHM_ObjectIdentity = ObjectIdentity
jnxSRX3600SlotHM = _JnxSRX3600SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 34, 2)
)
_JnxSRX3600SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX3600SlotPower = _JnxSRX3600SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 34, 3)
)
_JnxSRX3600SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX3600SlotFan = _JnxSRX3600SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 34, 4)
)
_JnxSRX3600SlotCB_ObjectIdentity = ObjectIdentity
jnxSRX3600SlotCB = _JnxSRX3600SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 34, 5)
)
_JnxSRX3600SlotFPB_ObjectIdentity = ObjectIdentity
jnxSRX3600SlotFPB = _JnxSRX3600SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 34, 6)
)
_JnxSlotSRX3400_ObjectIdentity = ObjectIdentity
jnxSlotSRX3400 = _JnxSlotSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 35)
)
_JnxSRX3400SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX3400SlotFPC = _JnxSRX3400SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 35, 1)
)
_JnxSRX3400SlotHM_ObjectIdentity = ObjectIdentity
jnxSRX3400SlotHM = _JnxSRX3400SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 35, 2)
)
_JnxSRX3400SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX3400SlotPower = _JnxSRX3400SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 35, 3)
)
_JnxSRX3400SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX3400SlotFan = _JnxSRX3400SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 35, 4)
)
_JnxSRX3400SlotCB_ObjectIdentity = ObjectIdentity
jnxSRX3400SlotCB = _JnxSRX3400SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 35, 5)
)
_JnxSRX3400SlotFPB_ObjectIdentity = ObjectIdentity
jnxSRX3400SlotFPB = _JnxSRX3400SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 35, 6)
)
_JnxSlotSRX210_ObjectIdentity = ObjectIdentity
jnxSlotSRX210 = _JnxSlotSRX210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 36)
)
_JnxSRX210SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX210SlotFPC = _JnxSRX210SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 36, 1)
)
_JnxSRX210SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX210SlotRE = _JnxSRX210SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 36, 2)
)
_JnxSRX210SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX210SlotPower = _JnxSRX210SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 36, 3)
)
_JnxSRX210SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX210SlotFan = _JnxSRX210SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 36, 4)
)
_JnxSlotTXP_ObjectIdentity = ObjectIdentity
jnxSlotTXP = _JnxSlotTXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 37)
)
_JnxTXPSlotSIB_ObjectIdentity = ObjectIdentity
jnxTXPSlotSIB = _JnxTXPSlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 37, 1)
)
_JnxTXPSlotHM_ObjectIdentity = ObjectIdentity
jnxTXPSlotHM = _JnxTXPSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 37, 2)
)
_JnxTXPSlotPower_ObjectIdentity = ObjectIdentity
jnxTXPSlotPower = _JnxTXPSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 37, 3)
)
_JnxTXPSlotFan_ObjectIdentity = ObjectIdentity
jnxTXPSlotFan = _JnxTXPSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 37, 4)
)
_JnxTXPSlotCB_ObjectIdentity = ObjectIdentity
jnxTXPSlotCB = _JnxTXPSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 37, 5)
)
_JnxTXPSlotFPB_ObjectIdentity = ObjectIdentity
jnxTXPSlotFPB = _JnxTXPSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 37, 6)
)
_JnxTXPSlotCIP_ObjectIdentity = ObjectIdentity
jnxTXPSlotCIP = _JnxTXPSlotCIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 37, 7)
)
_JnxTXPSlotSPMB_ObjectIdentity = ObjectIdentity
jnxTXPSlotSPMB = _JnxTXPSlotSPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 37, 8)
)
_JnxTXPSlotLCC_ObjectIdentity = ObjectIdentity
jnxTXPSlotLCC = _JnxTXPSlotLCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 37, 9)
)
_JnxTXPSlotSFC_ObjectIdentity = ObjectIdentity
jnxTXPSlotSFC = _JnxTXPSlotSFC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 37, 10)
)
_JnxSlotJCS_ObjectIdentity = ObjectIdentity
jnxSlotJCS = _JnxSlotJCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 38)
)
_JnxJCSSlotHM_ObjectIdentity = ObjectIdentity
jnxJCSSlotHM = _JnxJCSSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 38, 1)
)
_JnxJCSSlotFPC_ObjectIdentity = ObjectIdentity
jnxJCSSlotFPC = _JnxJCSSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 38, 2)
)
_JnxSlotSRX240_ObjectIdentity = ObjectIdentity
jnxSlotSRX240 = _JnxSlotSRX240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 39)
)
_JnxSRX240SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX240SlotFPC = _JnxSRX240SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 39, 1)
)
_JnxSRX240SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX240SlotRE = _JnxSRX240SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 39, 2)
)
_JnxSRX240SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX240SlotPower = _JnxSRX240SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 39, 3)
)
_JnxSRX240SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX240SlotFan = _JnxSRX240SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 39, 4)
)
_JnxSlotSRX650_ObjectIdentity = ObjectIdentity
jnxSlotSRX650 = _JnxSlotSRX650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 40)
)
_JnxSRX650SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX650SlotFPC = _JnxSRX650SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 40, 1)
)
_JnxSRX650SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX650SlotRE = _JnxSRX650SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 40, 2)
)
_JnxSRX650SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX650SlotPower = _JnxSRX650SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 40, 3)
)
_JnxSRX650SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX650SlotFan = _JnxSRX650SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 40, 4)
)
_JnxSlotSRX100_ObjectIdentity = ObjectIdentity
jnxSlotSRX100 = _JnxSlotSRX100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 41)
)
_JnxSRX100SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX100SlotFPC = _JnxSRX100SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 41, 1)
)
_JnxSRX100SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX100SlotRE = _JnxSRX100SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 41, 2)
)
_JnxSRX100SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX100SlotPower = _JnxSRX100SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 41, 3)
)
_JnxSRX100SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX100SlotFan = _JnxSRX100SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 41, 4)
)
_JnxSlotLN1000V_ObjectIdentity = ObjectIdentity
jnxSlotLN1000V = _JnxSlotLN1000V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 42)
)
_JnxLN1000VSlotFPC_ObjectIdentity = ObjectIdentity
jnxLN1000VSlotFPC = _JnxLN1000VSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 42, 1)
)
_JnxLN1000VSlotRE_ObjectIdentity = ObjectIdentity
jnxLN1000VSlotRE = _JnxLN1000VSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 42, 2)
)
_JnxLN1000VSlotPower_ObjectIdentity = ObjectIdentity
jnxLN1000VSlotPower = _JnxLN1000VSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 42, 3)
)
_JnxLN1000VSlotFan_ObjectIdentity = ObjectIdentity
jnxLN1000VSlotFan = _JnxLN1000VSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 42, 4)
)
_JnxSlotEX2200_ObjectIdentity = ObjectIdentity
jnxSlotEX2200 = _JnxSlotEX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 43)
)
_JnxEX2200SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX2200SlotFPC = _JnxEX2200SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 43, 1)
)
_JnxEX2200SlotPower_ObjectIdentity = ObjectIdentity
jnxEX2200SlotPower = _JnxEX2200SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 43, 1, 1)
)
_JnxEX2200SlotFan_ObjectIdentity = ObjectIdentity
jnxEX2200SlotFan = _JnxEX2200SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 43, 1, 2)
)
_JnxEX2200SlotRE_ObjectIdentity = ObjectIdentity
jnxEX2200SlotRE = _JnxEX2200SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 43, 1, 3)
)
_JnxSlotEX4500_ObjectIdentity = ObjectIdentity
jnxSlotEX4500 = _JnxSlotEX4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 44)
)
_JnxEX4500SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX4500SlotFPC = _JnxEX4500SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 44, 1)
)
_JnxEX4500SlotPower_ObjectIdentity = ObjectIdentity
jnxEX4500SlotPower = _JnxEX4500SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 44, 1, 1)
)
_JnxEX4500SlotFan_ObjectIdentity = ObjectIdentity
jnxEX4500SlotFan = _JnxEX4500SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 44, 1, 2)
)
_JnxEX4500SlotRE_ObjectIdentity = ObjectIdentity
jnxEX4500SlotRE = _JnxEX4500SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 44, 1, 3)
)
_JnxSlotIBM4274M02J02M_ObjectIdentity = ObjectIdentity
jnxSlotIBM4274M02J02M = _JnxSlotIBM4274M02J02M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 46)
)
_JnxIBM4274M02J02MSlotFPC_ObjectIdentity = ObjectIdentity
jnxIBM4274M02J02MSlotFPC = _JnxIBM4274M02J02MSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 46, 1)
)
_JnxIBM4274M02J02MSlotHM_ObjectIdentity = ObjectIdentity
jnxIBM4274M02J02MSlotHM = _JnxIBM4274M02J02MSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 46, 2)
)
_JnxIBM4274M02J02MSlotPower_ObjectIdentity = ObjectIdentity
jnxIBM4274M02J02MSlotPower = _JnxIBM4274M02J02MSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 46, 3)
)
_JnxIBM4274M02J02MSlotFan_ObjectIdentity = ObjectIdentity
jnxIBM4274M02J02MSlotFan = _JnxIBM4274M02J02MSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 46, 4)
)
_JnxIBM4274M02J02MSlotCB_ObjectIdentity = ObjectIdentity
jnxIBM4274M02J02MSlotCB = _JnxIBM4274M02J02MSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 46, 5)
)
_JnxIBM4274M02J02MSlotFPB_ObjectIdentity = ObjectIdentity
jnxIBM4274M02J02MSlotFPB = _JnxIBM4274M02J02MSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 46, 6)
)
_JnxSlotIBM4274M06J06M_ObjectIdentity = ObjectIdentity
jnxSlotIBM4274M06J06M = _JnxSlotIBM4274M06J06M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 47)
)
_JnxIBM4274M06J06MSlotFPC_ObjectIdentity = ObjectIdentity
jnxIBM4274M06J06MSlotFPC = _JnxIBM4274M06J06MSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 47, 1)
)
_JnxIBM4274M06J06MSlotHM_ObjectIdentity = ObjectIdentity
jnxIBM4274M06J06MSlotHM = _JnxIBM4274M06J06MSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 47, 2)
)
_JnxIBM4274M06J06MSlotPower_ObjectIdentity = ObjectIdentity
jnxIBM4274M06J06MSlotPower = _JnxIBM4274M06J06MSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 47, 3)
)
_JnxIBM4274M06J06MSlotFan_ObjectIdentity = ObjectIdentity
jnxIBM4274M06J06MSlotFan = _JnxIBM4274M06J06MSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 47, 4)
)
_JnxIBM4274M06J06MSlotCB_ObjectIdentity = ObjectIdentity
jnxIBM4274M06J06MSlotCB = _JnxIBM4274M06J06MSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 47, 5)
)
_JnxIBM4274M06J06MSlotFPB_ObjectIdentity = ObjectIdentity
jnxIBM4274M06J06MSlotFPB = _JnxIBM4274M06J06MSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 47, 6)
)
_JnxSlotIBM4274M11J11M_ObjectIdentity = ObjectIdentity
jnxSlotIBM4274M11J11M = _JnxSlotIBM4274M11J11M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 48)
)
_JnxIBM4274M11J11MSlotFPC_ObjectIdentity = ObjectIdentity
jnxIBM4274M11J11MSlotFPC = _JnxIBM4274M11J11MSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 48, 1)
)
_JnxIBM4274M11J11MSlotHM_ObjectIdentity = ObjectIdentity
jnxIBM4274M11J11MSlotHM = _JnxIBM4274M11J11MSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 48, 2)
)
_JnxIBM4274M11J11MSlotPower_ObjectIdentity = ObjectIdentity
jnxIBM4274M11J11MSlotPower = _JnxIBM4274M11J11MSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 48, 3)
)
_JnxIBM4274M11J11MSlotFan_ObjectIdentity = ObjectIdentity
jnxIBM4274M11J11MSlotFan = _JnxIBM4274M11J11MSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 48, 4)
)
_JnxIBM4274M11J11MSlotCB_ObjectIdentity = ObjectIdentity
jnxIBM4274M11J11MSlotCB = _JnxIBM4274M11J11MSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 48, 5)
)
_JnxIBM4274M11J11MSlotFPB_ObjectIdentity = ObjectIdentity
jnxIBM4274M11J11MSlotFPB = _JnxIBM4274M11J11MSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 48, 6)
)
_JnxSlotSRX1400_ObjectIdentity = ObjectIdentity
jnxSlotSRX1400 = _JnxSlotSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 49)
)
_JnxSRX1400SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX1400SlotFPC = _JnxSRX1400SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 49, 1)
)
_JnxSRX1400SlotHM_ObjectIdentity = ObjectIdentity
jnxSRX1400SlotHM = _JnxSRX1400SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 49, 2)
)
_JnxSRX1400SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX1400SlotPower = _JnxSRX1400SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 49, 3)
)
_JnxSRX1400SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX1400SlotFan = _JnxSRX1400SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 49, 4)
)
_JnxSRX1400SlotCB_ObjectIdentity = ObjectIdentity
jnxSRX1400SlotCB = _JnxSRX1400SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 49, 5)
)
_JnxSRX1400SlotFPB_ObjectIdentity = ObjectIdentity
jnxSRX1400SlotFPB = _JnxSRX1400SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 49, 6)
)
_JnxSlotIBM4274S58J58S_ObjectIdentity = ObjectIdentity
jnxSlotIBM4274S58J58S = _JnxSlotIBM4274S58J58S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 50)
)
_JnxIBM4274S58J58SSlotFPC_ObjectIdentity = ObjectIdentity
jnxIBM4274S58J58SSlotFPC = _JnxIBM4274S58J58SSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 50, 1)
)
_JnxIBM4274S58J58SSlotHM_ObjectIdentity = ObjectIdentity
jnxIBM4274S58J58SSlotHM = _JnxIBM4274S58J58SSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 50, 2)
)
_JnxIBM4274S58J58SSlotPower_ObjectIdentity = ObjectIdentity
jnxIBM4274S58J58SSlotPower = _JnxIBM4274S58J58SSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 50, 3)
)
_JnxIBM4274S58J58SSlotFan_ObjectIdentity = ObjectIdentity
jnxIBM4274S58J58SSlotFan = _JnxIBM4274S58J58SSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 50, 4)
)
_JnxIBM4274S58J58SSlotCB_ObjectIdentity = ObjectIdentity
jnxIBM4274S58J58SSlotCB = _JnxIBM4274S58J58SSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 50, 5)
)
_JnxIBM4274S58J58SSlotFPB_ObjectIdentity = ObjectIdentity
jnxIBM4274S58J58SSlotFPB = _JnxIBM4274S58J58SSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 50, 6)
)
_JnxSlotIBM4274S56J56S_ObjectIdentity = ObjectIdentity
jnxSlotIBM4274S56J56S = _JnxSlotIBM4274S56J56S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 51)
)
_JnxIBM4274S56J56SSlotFPC_ObjectIdentity = ObjectIdentity
jnxIBM4274S56J56SSlotFPC = _JnxIBM4274S56J56SSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 51, 1)
)
_JnxIBM4274S56J56SSlotHM_ObjectIdentity = ObjectIdentity
jnxIBM4274S56J56SSlotHM = _JnxIBM4274S56J56SSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 51, 2)
)
_JnxIBM4274S56J56SSlotPower_ObjectIdentity = ObjectIdentity
jnxIBM4274S56J56SSlotPower = _JnxIBM4274S56J56SSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 51, 3)
)
_JnxIBM4274S56J56SSlotFan_ObjectIdentity = ObjectIdentity
jnxIBM4274S56J56SSlotFan = _JnxIBM4274S56J56SSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 51, 4)
)
_JnxIBM4274S56J56SSlotCB_ObjectIdentity = ObjectIdentity
jnxIBM4274S56J56SSlotCB = _JnxIBM4274S56J56SSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 51, 5)
)
_JnxIBM4274S56J56SSlotFPB_ObjectIdentity = ObjectIdentity
jnxIBM4274S56J56SSlotFPB = _JnxIBM4274S56J56SSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 51, 6)
)
_JnxSlotIBM4274S36J36S_ObjectIdentity = ObjectIdentity
jnxSlotIBM4274S36J36S = _JnxSlotIBM4274S36J36S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 52)
)
_JnxIBM4274S36J36SSlotFPC_ObjectIdentity = ObjectIdentity
jnxIBM4274S36J36SSlotFPC = _JnxIBM4274S36J36SSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 52, 1)
)
_JnxIBM4274S36J36SSlotHM_ObjectIdentity = ObjectIdentity
jnxIBM4274S36J36SSlotHM = _JnxIBM4274S36J36SSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 52, 2)
)
_JnxIBM4274S36J36SSlotPower_ObjectIdentity = ObjectIdentity
jnxIBM4274S36J36SSlotPower = _JnxIBM4274S36J36SSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 52, 3)
)
_JnxIBM4274S36J36SSlotFan_ObjectIdentity = ObjectIdentity
jnxIBM4274S36J36SSlotFan = _JnxIBM4274S36J36SSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 52, 4)
)
_JnxIBM4274S36J36SSlotCB_ObjectIdentity = ObjectIdentity
jnxIBM4274S36J36SSlotCB = _JnxIBM4274S36J36SSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 52, 5)
)
_JnxIBM4274S36J36SSlotFPB_ObjectIdentity = ObjectIdentity
jnxIBM4274S36J36SSlotFPB = _JnxIBM4274S36J36SSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 52, 6)
)
_JnxSlotIBM4274S34J34S_ObjectIdentity = ObjectIdentity
jnxSlotIBM4274S34J34S = _JnxSlotIBM4274S34J34S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 53)
)
_JnxIBM4274S34J34SSlotFPC_ObjectIdentity = ObjectIdentity
jnxIBM4274S34J34SSlotFPC = _JnxIBM4274S34J34SSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 53, 1)
)
_JnxIBM4274S34J34SSlotHM_ObjectIdentity = ObjectIdentity
jnxIBM4274S34J34SSlotHM = _JnxIBM4274S34J34SSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 53, 2)
)
_JnxIBM4274S34J34SSlotPower_ObjectIdentity = ObjectIdentity
jnxIBM4274S34J34SSlotPower = _JnxIBM4274S34J34SSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 53, 3)
)
_JnxIBM4274S34J34SSlotFan_ObjectIdentity = ObjectIdentity
jnxIBM4274S34J34SSlotFan = _JnxIBM4274S34J34SSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 53, 4)
)
_JnxIBM4274S34J34SSlotCB_ObjectIdentity = ObjectIdentity
jnxIBM4274S34J34SSlotCB = _JnxIBM4274S34J34SSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 53, 5)
)
_JnxIBM4274S34J34SSlotFPB_ObjectIdentity = ObjectIdentity
jnxIBM4274S34J34SSlotFPB = _JnxIBM4274S34J34SSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 53, 6)
)
_JnxSlotIBM427348EJ48E_ObjectIdentity = ObjectIdentity
jnxSlotIBM427348EJ48E = _JnxSlotIBM427348EJ48E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 54)
)
_JnxIBM427348EJ48ESlotFPC_ObjectIdentity = ObjectIdentity
jnxIBM427348EJ48ESlotFPC = _JnxIBM427348EJ48ESlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 54, 1)
)
_JnxIBM427348EJ48ESlotPower_ObjectIdentity = ObjectIdentity
jnxIBM427348EJ48ESlotPower = _JnxIBM427348EJ48ESlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 54, 1, 1)
)
_JnxIBM427348EJ48ESlotFan_ObjectIdentity = ObjectIdentity
jnxIBM427348EJ48ESlotFan = _JnxIBM427348EJ48ESlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 54, 1, 2)
)
_JnxSlotIBM4274E08J08E_ObjectIdentity = ObjectIdentity
jnxSlotIBM4274E08J08E = _JnxSlotIBM4274E08J08E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 55)
)
_JnxIBM4274E08J08ESlotFPC_ObjectIdentity = ObjectIdentity
jnxIBM4274E08J08ESlotFPC = _JnxIBM4274E08J08ESlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 55, 1)
)
_JnxIBM4274E08J08ESlot48S_ObjectIdentity = ObjectIdentity
jnxIBM4274E08J08ESlot48S = _JnxIBM4274E08J08ESlot48S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 55, 1, 1)
)
_JnxIBM4274E08J08ESlot48T_ObjectIdentity = ObjectIdentity
jnxIBM4274E08J08ESlot48T = _JnxIBM4274E08J08ESlot48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 55, 1, 2)
)
_JnxIBM4274E08J08ESlot8XS_ObjectIdentity = ObjectIdentity
jnxIBM4274E08J08ESlot8XS = _JnxIBM4274E08J08ESlot8XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 55, 1, 3)
)
_JnxIBM4274E08J08EHM_ObjectIdentity = ObjectIdentity
jnxIBM4274E08J08EHM = _JnxIBM4274E08J08EHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 55, 3)
)
_JnxIBM4274E08J08ESlotPower_ObjectIdentity = ObjectIdentity
jnxIBM4274E08J08ESlotPower = _JnxIBM4274E08J08ESlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 55, 4)
)
_JnxIBM4274E08J08ESlotFan_ObjectIdentity = ObjectIdentity
jnxIBM4274E08J08ESlotFan = _JnxIBM4274E08J08ESlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 55, 5)
)
_JnxIBM4274E08J08ESlotFT_ObjectIdentity = ObjectIdentity
jnxIBM4274E08J08ESlotFT = _JnxIBM4274E08J08ESlotFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 55, 5, 1)
)
_JnxIBM4274E08J08ESlotCBD_ObjectIdentity = ObjectIdentity
jnxIBM4274E08J08ESlotCBD = _JnxIBM4274E08J08ESlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 55, 6)
)
_JnxSlotIBM4274E16J16E_ObjectIdentity = ObjectIdentity
jnxSlotIBM4274E16J16E = _JnxSlotIBM4274E16J16E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 56)
)
_JnxIBM4274E16J16ESlotFPC_ObjectIdentity = ObjectIdentity
jnxIBM4274E16J16ESlotFPC = _JnxIBM4274E16J16ESlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 56, 1)
)
_JnxIBM4274E16J16ESlot48S_ObjectIdentity = ObjectIdentity
jnxIBM4274E16J16ESlot48S = _JnxIBM4274E16J16ESlot48S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 56, 1, 1)
)
_JnxIBM4274E16J16ESlot48T_ObjectIdentity = ObjectIdentity
jnxIBM4274E16J16ESlot48T = _JnxIBM4274E16J16ESlot48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 56, 1, 2)
)
_JnxIBM4274E16J16ESlot8XS_ObjectIdentity = ObjectIdentity
jnxIBM4274E16J16ESlot8XS = _JnxIBM4274E16J16ESlot8XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 56, 1, 3)
)
_JnxIBM4274E16J16ESIB_ObjectIdentity = ObjectIdentity
jnxIBM4274E16J16ESIB = _JnxIBM4274E16J16ESIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 56, 2)
)
_JnxIBM4274E16J16EHM_ObjectIdentity = ObjectIdentity
jnxIBM4274E16J16EHM = _JnxIBM4274E16J16EHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 56, 3)
)
_JnxIBM4274E16J16ESlotPower_ObjectIdentity = ObjectIdentity
jnxIBM4274E16J16ESlotPower = _JnxIBM4274E16J16ESlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 56, 4)
)
_JnxIBM4274E16J16ESlotFan_ObjectIdentity = ObjectIdentity
jnxIBM4274E16J16ESlotFan = _JnxIBM4274E16J16ESlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 56, 5)
)
_JnxIBM4274E16J16ESlotFT_ObjectIdentity = ObjectIdentity
jnxIBM4274E16J16ESlotFT = _JnxIBM4274E16J16ESlotFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 56, 5, 1)
)
_JnxIBM4274E16J16ESlotRFT_ObjectIdentity = ObjectIdentity
jnxIBM4274E16J16ESlotRFT = _JnxIBM4274E16J16ESlotRFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 56, 5, 2)
)
_JnxIBM4274E16J16ESlotCBD_ObjectIdentity = ObjectIdentity
jnxIBM4274E16J16ESlotCBD = _JnxIBM4274E16J16ESlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 56, 6)
)
_JnxSlotMX80_ObjectIdentity = ObjectIdentity
jnxSlotMX80 = _JnxSlotMX80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 57)
)
_JnxMX80SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX80SlotFPC = _JnxMX80SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 57, 1)
)
_JnxMX80SlotCFEB_ObjectIdentity = ObjectIdentity
jnxMX80SlotCFEB = _JnxMX80SlotCFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 57, 2)
)
_JnxMX80SlotRE_ObjectIdentity = ObjectIdentity
jnxMX80SlotRE = _JnxMX80SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 57, 3)
)
_JnxMX80SlotPower_ObjectIdentity = ObjectIdentity
jnxMX80SlotPower = _JnxMX80SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 57, 4)
)
_JnxMX80SlotFan_ObjectIdentity = ObjectIdentity
jnxMX80SlotFan = _JnxMX80SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 57, 5)
)
_JnxSlotSRX220_ObjectIdentity = ObjectIdentity
jnxSlotSRX220 = _JnxSlotSRX220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 58)
)
_JnxSRX220SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX220SlotFPC = _JnxSRX220SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 58, 1)
)
_JnxSRX220SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX220SlotRE = _JnxSRX220SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 58, 2)
)
_JnxSRX220SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX220SlotPower = _JnxSRX220SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 58, 3)
)
_JnxSRX220SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX220SlotFan = _JnxSRX220SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 58, 4)
)
_JnxSlotEXXRE_ObjectIdentity = ObjectIdentity
jnxSlotEXXRE = _JnxSlotEXXRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 59)
)
_JnxEXXRESlotPower_ObjectIdentity = ObjectIdentity
jnxEXXRESlotPower = _JnxEXXRESlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 59, 1)
)
_JnxEXXRESlotFan_ObjectIdentity = ObjectIdentity
jnxEXXRESlotFan = _JnxEXXRESlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 59, 2)
)
_JnxEXXRESlotHM_ObjectIdentity = ObjectIdentity
jnxEXXRESlotHM = _JnxEXXRESlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 59, 3)
)
_JnxEXXRESlotLCC_ObjectIdentity = ObjectIdentity
jnxEXXRESlotLCC = _JnxEXXRESlotLCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 59, 4)
)
_JnxSlotQFXInterconnect_ObjectIdentity = ObjectIdentity
jnxSlotQFXInterconnect = _JnxSlotQFXInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 60)
)
_JnxQFXInterconnectSlotFPC_ObjectIdentity = ObjectIdentity
jnxQFXInterconnectSlotFPC = _JnxQFXInterconnectSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 60, 1)
)
_JnxQFXInterconnectSlotHM_ObjectIdentity = ObjectIdentity
jnxQFXInterconnectSlotHM = _JnxQFXInterconnectSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 60, 2)
)
_JnxQFXInterconnectSlotPower_ObjectIdentity = ObjectIdentity
jnxQFXInterconnectSlotPower = _JnxQFXInterconnectSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 60, 3)
)
_JnxQFXInterconnectSlotFan_ObjectIdentity = ObjectIdentity
jnxQFXInterconnectSlotFan = _JnxQFXInterconnectSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 60, 4)
)
_JnxQFXInterconnectSlotCBD_ObjectIdentity = ObjectIdentity
jnxQFXInterconnectSlotCBD = _JnxQFXInterconnectSlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 60, 5)
)
_JnxQFXInterconnectSlotFPB_ObjectIdentity = ObjectIdentity
jnxQFXInterconnectSlotFPB = _JnxQFXInterconnectSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 60, 6)
)
_JnxSlotQFXNode_ObjectIdentity = ObjectIdentity
jnxSlotQFXNode = _JnxSlotQFXNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 61)
)
_JnxQFXNodeSlotFPC_ObjectIdentity = ObjectIdentity
jnxQFXNodeSlotFPC = _JnxQFXNodeSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 61, 1)
)
_JnxQFXNodeSlotHM_ObjectIdentity = ObjectIdentity
jnxQFXNodeSlotHM = _JnxQFXNodeSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 61, 2)
)
_JnxQFXNodeSlotPower_ObjectIdentity = ObjectIdentity
jnxQFXNodeSlotPower = _JnxQFXNodeSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 61, 3)
)
_JnxQFXNodeSlotFan_ObjectIdentity = ObjectIdentity
jnxQFXNodeSlotFan = _JnxQFXNodeSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 61, 4)
)
_JnxQFXNodeSlotFPB_ObjectIdentity = ObjectIdentity
jnxQFXNodeSlotFPB = _JnxQFXNodeSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 61, 5)
)
_JnxSlotQFXJVRE_ObjectIdentity = ObjectIdentity
jnxSlotQFXJVRE = _JnxSlotQFXJVRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 62)
)
_JnxQFXJVRESlotFPC_ObjectIdentity = ObjectIdentity
jnxQFXJVRESlotFPC = _JnxQFXJVRESlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 62, 1)
)
_JnxQFXJVRESlotHM_ObjectIdentity = ObjectIdentity
jnxQFXJVRESlotHM = _JnxQFXJVRESlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 62, 2)
)
_JnxQFXJVRESlotPower_ObjectIdentity = ObjectIdentity
jnxQFXJVRESlotPower = _JnxQFXJVRESlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 62, 3)
)
_JnxQFXJVRESlotFan_ObjectIdentity = ObjectIdentity
jnxQFXJVRESlotFan = _JnxQFXJVRESlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 62, 4)
)
_JnxQFXJVRESlotFPB_ObjectIdentity = ObjectIdentity
jnxQFXJVRESlotFPB = _JnxQFXJVRESlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 62, 5)
)
_JnxSlotEX4300_ObjectIdentity = ObjectIdentity
jnxSlotEX4300 = _JnxSlotEX4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 63)
)
_JnxEX4300SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX4300SlotFPC = _JnxEX4300SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 63, 1)
)
_JnxEX4300SlotPower_ObjectIdentity = ObjectIdentity
jnxEX4300SlotPower = _JnxEX4300SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 63, 1, 1)
)
_JnxEX4300SlotFan_ObjectIdentity = ObjectIdentity
jnxEX4300SlotFan = _JnxEX4300SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 63, 1, 2)
)
_JnxEX4300MPSlotFPC_ObjectIdentity = ObjectIdentity
jnxEX4300MPSlotFPC = _JnxEX4300MPSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 63, 2)
)
_JnxEX4300MPSlotFan_ObjectIdentity = ObjectIdentity
jnxEX4300MPSlotFan = _JnxEX4300MPSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 63, 2, 1)
)
_JnxSlotSRX110_ObjectIdentity = ObjectIdentity
jnxSlotSRX110 = _JnxSlotSRX110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 64)
)
_JnxSRX110SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX110SlotFPC = _JnxSRX110SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 64, 1)
)
_JnxSRX110SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX110SlotRE = _JnxSRX110SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 64, 2)
)
_JnxSRX110SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX110SlotPower = _JnxSRX110SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 64, 3)
)
_JnxSRX110SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX110SlotFan = _JnxSRX110SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 64, 4)
)
_JnxSlotSRX120_ObjectIdentity = ObjectIdentity
jnxSlotSRX120 = _JnxSlotSRX120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 65)
)
_JnxSRX120SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX120SlotFPC = _JnxSRX120SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 65, 1)
)
_JnxSRX120SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX120SlotRE = _JnxSRX120SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 65, 2)
)
_JnxSRX120SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX120SlotPower = _JnxSRX120SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 65, 3)
)
_JnxSRX120SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX120SlotFan = _JnxSRX120SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 65, 4)
)
_JnxSlotMAG8600_ObjectIdentity = ObjectIdentity
jnxSlotMAG8600 = _JnxSlotMAG8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 66)
)
_JnxMAG8600SlotFPC_ObjectIdentity = ObjectIdentity
jnxMAG8600SlotFPC = _JnxMAG8600SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 66, 1)
)
_JnxMAG8600SlotRE_ObjectIdentity = ObjectIdentity
jnxMAG8600SlotRE = _JnxMAG8600SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 66, 2)
)
_JnxMAG8600SlotPower_ObjectIdentity = ObjectIdentity
jnxMAG8600SlotPower = _JnxMAG8600SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 66, 3)
)
_JnxMAG8600SlotFan_ObjectIdentity = ObjectIdentity
jnxMAG8600SlotFan = _JnxMAG8600SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 66, 4)
)
_JnxMAG8600SlotCB_ObjectIdentity = ObjectIdentity
jnxMAG8600SlotCB = _JnxMAG8600SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 66, 5)
)
_JnxSlotMAG6611_ObjectIdentity = ObjectIdentity
jnxSlotMAG6611 = _JnxSlotMAG6611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 67)
)
_JnxMAG6611SlotFPC_ObjectIdentity = ObjectIdentity
jnxMAG6611SlotFPC = _JnxMAG6611SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 67, 1)
)
_JnxMAG6611SlotRE_ObjectIdentity = ObjectIdentity
jnxMAG6611SlotRE = _JnxMAG6611SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 67, 2)
)
_JnxMAG6611SlotPower_ObjectIdentity = ObjectIdentity
jnxMAG6611SlotPower = _JnxMAG6611SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 67, 3)
)
_JnxMAG6611SlotFan_ObjectIdentity = ObjectIdentity
jnxMAG6611SlotFan = _JnxMAG6611SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 67, 4)
)
_JnxMAG6611SlotCB_ObjectIdentity = ObjectIdentity
jnxMAG6611SlotCB = _JnxMAG6611SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 67, 5)
)
_JnxSlotMAG6610_ObjectIdentity = ObjectIdentity
jnxSlotMAG6610 = _JnxSlotMAG6610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 68)
)
_JnxMAG6610SlotFPC_ObjectIdentity = ObjectIdentity
jnxMAG6610SlotFPC = _JnxMAG6610SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 68, 1)
)
_JnxMAG6610SlotRE_ObjectIdentity = ObjectIdentity
jnxMAG6610SlotRE = _JnxMAG6610SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 68, 2)
)
_JnxMAG6610SlotPower_ObjectIdentity = ObjectIdentity
jnxMAG6610SlotPower = _JnxMAG6610SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 68, 3)
)
_JnxMAG6610SlotFan_ObjectIdentity = ObjectIdentity
jnxMAG6610SlotFan = _JnxMAG6610SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 68, 4)
)
_JnxMAG6610SlotCB_ObjectIdentity = ObjectIdentity
jnxMAG6610SlotCB = _JnxMAG6610SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 68, 5)
)
_JnxSlotPTX5000_ObjectIdentity = ObjectIdentity
jnxSlotPTX5000 = _JnxSlotPTX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 69)
)
_JnxPTX5000SlotSIB_ObjectIdentity = ObjectIdentity
jnxPTX5000SlotSIB = _JnxPTX5000SlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 69, 1)
)
_JnxPTX5000SlotHM_ObjectIdentity = ObjectIdentity
jnxPTX5000SlotHM = _JnxPTX5000SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 69, 2)
)
_JnxPTX5000SlotFPC_ObjectIdentity = ObjectIdentity
jnxPTX5000SlotFPC = _JnxPTX5000SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 69, 3)
)
_JnxPTX5000SlotFan_ObjectIdentity = ObjectIdentity
jnxPTX5000SlotFan = _JnxPTX5000SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 69, 4)
)
_JnxPTX5000SlotCB_ObjectIdentity = ObjectIdentity
jnxPTX5000SlotCB = _JnxPTX5000SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 69, 5)
)
_JnxPTX5000SlotFPB_ObjectIdentity = ObjectIdentity
jnxPTX5000SlotFPB = _JnxPTX5000SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 69, 6)
)
_JnxPTX5000SlotSPMB_ObjectIdentity = ObjectIdentity
jnxPTX5000SlotSPMB = _JnxPTX5000SlotSPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 69, 7)
)
_JnxPTX5000SlotPDU_ObjectIdentity = ObjectIdentity
jnxPTX5000SlotPDU = _JnxPTX5000SlotPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 69, 8)
)
_JnxPTX5000SlotPSM_ObjectIdentity = ObjectIdentity
jnxPTX5000SlotPSM = _JnxPTX5000SlotPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 69, 9)
)
_JnxPTX5000SlotCCG_ObjectIdentity = ObjectIdentity
jnxPTX5000SlotCCG = _JnxPTX5000SlotCCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 69, 10)
)
_JnxPTX5000SlotPIC_ObjectIdentity = ObjectIdentity
jnxPTX5000SlotPIC = _JnxPTX5000SlotPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 69, 11)
)
_JnxSlotIBM0719J45E_ObjectIdentity = ObjectIdentity
jnxSlotIBM0719J45E = _JnxSlotIBM0719J45E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 71)
)
_JnxIBM0719J45ESlotFPC_ObjectIdentity = ObjectIdentity
jnxIBM0719J45ESlotFPC = _JnxIBM0719J45ESlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 71, 1)
)
_JnxIBM0719J45ESlotPower_ObjectIdentity = ObjectIdentity
jnxIBM0719J45ESlotPower = _JnxIBM0719J45ESlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 71, 1, 1)
)
_JnxIBM0719J45ESlotFan_ObjectIdentity = ObjectIdentity
jnxIBM0719J45ESlotFan = _JnxIBM0719J45ESlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 71, 1, 2)
)
_JnxIBM0719J45ESlotRE_ObjectIdentity = ObjectIdentity
jnxIBM0719J45ESlotRE = _JnxIBM0719J45ESlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 71, 1, 3)
)
_JnxSlotIBMJ08F_ObjectIdentity = ObjectIdentity
jnxSlotIBMJ08F = _JnxSlotIBMJ08F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 72)
)
_JnxIBMJ08FSlotFPC_ObjectIdentity = ObjectIdentity
jnxIBMJ08FSlotFPC = _JnxIBMJ08FSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 72, 1)
)
_JnxIBMJ08FSlotHM_ObjectIdentity = ObjectIdentity
jnxIBMJ08FSlotHM = _JnxIBMJ08FSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 72, 2)
)
_JnxIBMJ08FSlotPower_ObjectIdentity = ObjectIdentity
jnxIBMJ08FSlotPower = _JnxIBMJ08FSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 72, 3)
)
_JnxIBMJ08FSlotFan_ObjectIdentity = ObjectIdentity
jnxIBMJ08FSlotFan = _JnxIBMJ08FSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 72, 4)
)
_JnxIBMJ08FSlotCBD_ObjectIdentity = ObjectIdentity
jnxIBMJ08FSlotCBD = _JnxIBMJ08FSlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 72, 5)
)
_JnxIBMJ08FSlotFPB_ObjectIdentity = ObjectIdentity
jnxIBMJ08FSlotFPB = _JnxIBMJ08FSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 72, 6)
)
_JnxSlotIBMJ52F_ObjectIdentity = ObjectIdentity
jnxSlotIBMJ52F = _JnxSlotIBMJ52F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 73)
)
_JnxIBMJ52FSlotFPC_ObjectIdentity = ObjectIdentity
jnxIBMJ52FSlotFPC = _JnxIBMJ52FSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 73, 1)
)
_JnxIBMJ52FSlotHM_ObjectIdentity = ObjectIdentity
jnxIBMJ52FSlotHM = _JnxIBMJ52FSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 73, 2)
)
_JnxIBMJ52FSlotPower_ObjectIdentity = ObjectIdentity
jnxIBMJ52FSlotPower = _JnxIBMJ52FSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 73, 3)
)
_JnxIBMJ52FSlotFan_ObjectIdentity = ObjectIdentity
jnxIBMJ52FSlotFan = _JnxIBMJ52FSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 73, 4)
)
_JnxIBMJ52FSlotFPB_ObjectIdentity = ObjectIdentity
jnxIBMJ52FSlotFPB = _JnxIBMJ52FSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 73, 5)
)
_JnxSlotEX6210_ObjectIdentity = ObjectIdentity
jnxSlotEX6210 = _JnxSlotEX6210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 74)
)
_JnxEX6210SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX6210SlotFPC = _JnxEX6210SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 74, 1)
)
_JnxEX6210Slot48P_ObjectIdentity = ObjectIdentity
jnxEX6210Slot48P = _JnxEX6210Slot48P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 74, 1, 1)
)
_JnxEX6210Slot48T_ObjectIdentity = ObjectIdentity
jnxEX6210Slot48T = _JnxEX6210Slot48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 74, 1, 2)
)
_JnxEX6210HM_ObjectIdentity = ObjectIdentity
jnxEX6210HM = _JnxEX6210HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 74, 3)
)
_JnxEX6210SlotPower_ObjectIdentity = ObjectIdentity
jnxEX6210SlotPower = _JnxEX6210SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 74, 4)
)
_JnxEX6210SlotFan_ObjectIdentity = ObjectIdentity
jnxEX6210SlotFan = _JnxEX6210SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 74, 5)
)
_JnxEX6210SlotFT_ObjectIdentity = ObjectIdentity
jnxEX6210SlotFT = _JnxEX6210SlotFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 74, 5, 1)
)
_JnxEX6210SlotCBD_ObjectIdentity = ObjectIdentity
jnxEX6210SlotCBD = _JnxEX6210SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 74, 6)
)
_JnxSlotDellJFX3500_ObjectIdentity = ObjectIdentity
jnxSlotDellJFX3500 = _JnxSlotDellJFX3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 75)
)
_JnxDellJFX3500SlotFPC_ObjectIdentity = ObjectIdentity
jnxDellJFX3500SlotFPC = _JnxDellJFX3500SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 75, 1)
)
_JnxDellJFX3500SlotHM_ObjectIdentity = ObjectIdentity
jnxDellJFX3500SlotHM = _JnxDellJFX3500SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 75, 2)
)
_JnxDellJFX3500SlotPower_ObjectIdentity = ObjectIdentity
jnxDellJFX3500SlotPower = _JnxDellJFX3500SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 75, 3)
)
_JnxDellJFX3500SlotFan_ObjectIdentity = ObjectIdentity
jnxDellJFX3500SlotFan = _JnxDellJFX3500SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 75, 4)
)
_JnxDellJFX3500SlotFPB_ObjectIdentity = ObjectIdentity
jnxDellJFX3500SlotFPB = _JnxDellJFX3500SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 75, 5)
)
_JnxSlotEX3300_ObjectIdentity = ObjectIdentity
jnxSlotEX3300 = _JnxSlotEX3300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 76)
)
_JnxEX3300SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX3300SlotFPC = _JnxEX3300SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 76, 1)
)
_JnxEX3300SlotPower_ObjectIdentity = ObjectIdentity
jnxEX3300SlotPower = _JnxEX3300SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 76, 1, 1)
)
_JnxEX3300SlotFan_ObjectIdentity = ObjectIdentity
jnxEX3300SlotFan = _JnxEX3300SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 76, 1, 2)
)
_JnxSlotDELLJSRX3600_ObjectIdentity = ObjectIdentity
jnxSlotDELLJSRX3600 = _JnxSlotDELLJSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 77)
)
_JnxDELLJSRX3600SlotFPC_ObjectIdentity = ObjectIdentity
jnxDELLJSRX3600SlotFPC = _JnxDELLJSRX3600SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 77, 1)
)
_JnxDELLJSRX3600SlotHM_ObjectIdentity = ObjectIdentity
jnxDELLJSRX3600SlotHM = _JnxDELLJSRX3600SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 77, 2)
)
_JnxDELLJSRX3600SlotPower_ObjectIdentity = ObjectIdentity
jnxDELLJSRX3600SlotPower = _JnxDELLJSRX3600SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 77, 3)
)
_JnxDELLJSRX3600SlotFan_ObjectIdentity = ObjectIdentity
jnxDELLJSRX3600SlotFan = _JnxDELLJSRX3600SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 77, 4)
)
_JnxDELLJSRX3600SlotCB_ObjectIdentity = ObjectIdentity
jnxDELLJSRX3600SlotCB = _JnxDELLJSRX3600SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 77, 5)
)
_JnxDELLJSRX3600SlotFPB_ObjectIdentity = ObjectIdentity
jnxDELLJSRX3600SlotFPB = _JnxDELLJSRX3600SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 77, 6)
)
_JnxSlotDELLJSRX3400_ObjectIdentity = ObjectIdentity
jnxSlotDELLJSRX3400 = _JnxSlotDELLJSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 78)
)
_JnxDELLJSRX3400SlotFPC_ObjectIdentity = ObjectIdentity
jnxDELLJSRX3400SlotFPC = _JnxDELLJSRX3400SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 78, 1)
)
_JnxDELLJSRX3400SlotHM_ObjectIdentity = ObjectIdentity
jnxDELLJSRX3400SlotHM = _JnxDELLJSRX3400SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 78, 2)
)
_JnxDELLJSRX3400SlotPower_ObjectIdentity = ObjectIdentity
jnxDELLJSRX3400SlotPower = _JnxDELLJSRX3400SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 78, 3)
)
_JnxDELLJSRX3400SlotFan_ObjectIdentity = ObjectIdentity
jnxDELLJSRX3400SlotFan = _JnxDELLJSRX3400SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 78, 4)
)
_JnxDELLJSRX3400SlotCB_ObjectIdentity = ObjectIdentity
jnxDELLJSRX3400SlotCB = _JnxDELLJSRX3400SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 78, 5)
)
_JnxDELLJSRX3400SlotFPB_ObjectIdentity = ObjectIdentity
jnxDELLJSRX3400SlotFPB = _JnxDELLJSRX3400SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 78, 6)
)
_JnxSlotDELLJSRX1400_ObjectIdentity = ObjectIdentity
jnxSlotDELLJSRX1400 = _JnxSlotDELLJSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 79)
)
_JnxDELLJSRX1400SlotFPC_ObjectIdentity = ObjectIdentity
jnxDELLJSRX1400SlotFPC = _JnxDELLJSRX1400SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 79, 1)
)
_JnxDELLJSRX1400SlotHM_ObjectIdentity = ObjectIdentity
jnxDELLJSRX1400SlotHM = _JnxDELLJSRX1400SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 79, 2)
)
_JnxDELLJSRX1400SlotPower_ObjectIdentity = ObjectIdentity
jnxDELLJSRX1400SlotPower = _JnxDELLJSRX1400SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 79, 3)
)
_JnxDELLJSRX1400SlotFan_ObjectIdentity = ObjectIdentity
jnxDELLJSRX1400SlotFan = _JnxDELLJSRX1400SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 79, 4)
)
_JnxDELLJSRX1400SlotCB_ObjectIdentity = ObjectIdentity
jnxDELLJSRX1400SlotCB = _JnxDELLJSRX1400SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 79, 5)
)
_JnxDELLJSRX1400SlotFPB_ObjectIdentity = ObjectIdentity
jnxDELLJSRX1400SlotFPB = _JnxDELLJSRX1400SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 79, 6)
)
_JnxSlotDELLJSRX5800_ObjectIdentity = ObjectIdentity
jnxSlotDELLJSRX5800 = _JnxSlotDELLJSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 80)
)
_JnxDELLJSRX5800SlotFPC_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5800SlotFPC = _JnxDELLJSRX5800SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 80, 1)
)
_JnxDELLJSRX5800SlotHM_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5800SlotHM = _JnxDELLJSRX5800SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 80, 2)
)
_JnxDELLJSRX5800SlotPower_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5800SlotPower = _JnxDELLJSRX5800SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 80, 3)
)
_JnxDELLJSRX5800SlotFan_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5800SlotFan = _JnxDELLJSRX5800SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 80, 4)
)
_JnxDELLJSRX5800SlotCB_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5800SlotCB = _JnxDELLJSRX5800SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 80, 5)
)
_JnxDELLJSRX5800SlotFPB_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5800SlotFPB = _JnxDELLJSRX5800SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 80, 6)
)
_JnxSlotDELLJSRX5600_ObjectIdentity = ObjectIdentity
jnxSlotDELLJSRX5600 = _JnxSlotDELLJSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 81)
)
_JnxDELLJSRX5600SlotFPC_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5600SlotFPC = _JnxDELLJSRX5600SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 81, 1)
)
_JnxDELLJSRX5600SlotHM_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5600SlotHM = _JnxDELLJSRX5600SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 81, 2)
)
_JnxDELLJSRX5600SlotPower_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5600SlotPower = _JnxDELLJSRX5600SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 81, 3)
)
_JnxDELLJSRX5600SlotFan_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5600SlotFan = _JnxDELLJSRX5600SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 81, 4)
)
_JnxDELLJSRX5600SlotCB_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5600SlotCB = _JnxDELLJSRX5600SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 81, 5)
)
_JnxDELLJSRX5600SlotFPB_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5600SlotFPB = _JnxDELLJSRX5600SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 81, 6)
)
_JnxSlotQFXSwitch_ObjectIdentity = ObjectIdentity
jnxSlotQFXSwitch = _JnxSlotQFXSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 82)
)
_JnxQFXSwitchSlotFPC_ObjectIdentity = ObjectIdentity
jnxQFXSwitchSlotFPC = _JnxQFXSwitchSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 82, 1)
)
_JnxQFXSwitchSlotHM_ObjectIdentity = ObjectIdentity
jnxQFXSwitchSlotHM = _JnxQFXSwitchSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 82, 2)
)
_JnxQFXSwitchSlotPower_ObjectIdentity = ObjectIdentity
jnxQFXSwitchSlotPower = _JnxQFXSwitchSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 82, 3)
)
_JnxQFXSwitchSlotFan_ObjectIdentity = ObjectIdentity
jnxQFXSwitchSlotFan = _JnxQFXSwitchSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 82, 4)
)
_JnxQFXSwitchSlotFPB_ObjectIdentity = ObjectIdentity
jnxQFXSwitchSlotFPB = _JnxQFXSwitchSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 82, 5)
)
_JnxQFXSwitchSlotCBD_ObjectIdentity = ObjectIdentity
jnxQFXSwitchSlotCBD = _JnxQFXSwitchSlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 82, 6)
)
_JnxQFXSwitchSlotSIB_ObjectIdentity = ObjectIdentity
jnxQFXSwitchSlotSIB = _JnxQFXSwitchSlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 82, 7)
)
_JnxQFXSwitchSlotFEB_ObjectIdentity = ObjectIdentity
jnxQFXSwitchSlotFEB = _JnxQFXSwitchSlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 82, 8)
)
_JnxSlotT4000_ObjectIdentity = ObjectIdentity
jnxSlotT4000 = _JnxSlotT4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 83)
)
_JnxT4000SlotFPC_ObjectIdentity = ObjectIdentity
jnxT4000SlotFPC = _JnxT4000SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 83, 1)
)
_JnxT4000SlotSIB_ObjectIdentity = ObjectIdentity
jnxT4000SlotSIB = _JnxT4000SlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 83, 2)
)
_JnxT4000SlotHM_ObjectIdentity = ObjectIdentity
jnxT4000SlotHM = _JnxT4000SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 83, 3)
)
_JnxT4000SlotSCG_ObjectIdentity = ObjectIdentity
jnxT4000SlotSCG = _JnxT4000SlotSCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 83, 4)
)
_JnxT4000SlotPower_ObjectIdentity = ObjectIdentity
jnxT4000SlotPower = _JnxT4000SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 83, 5)
)
_JnxT4000SlotFan_ObjectIdentity = ObjectIdentity
jnxT4000SlotFan = _JnxT4000SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 83, 6)
)
_JnxT4000SlotCB_ObjectIdentity = ObjectIdentity
jnxT4000SlotCB = _JnxT4000SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 83, 7)
)
_JnxT4000SlotFPB_ObjectIdentity = ObjectIdentity
jnxT4000SlotFPB = _JnxT4000SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 83, 8)
)
_JnxT4000SlotCIP_ObjectIdentity = ObjectIdentity
jnxT4000SlotCIP = _JnxT4000SlotCIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 83, 9)
)
_JnxT4000SlotSPMB_ObjectIdentity = ObjectIdentity
jnxT4000SlotSPMB = _JnxT4000SlotSPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 83, 10)
)
_JnxT4000SlotPSD_ObjectIdentity = ObjectIdentity
jnxT4000SlotPSD = _JnxT4000SlotPSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 83, 11)
)
_JnxSlotSRX550_ObjectIdentity = ObjectIdentity
jnxSlotSRX550 = _JnxSlotSRX550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 86)
)
_JnxSRX550SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX550SlotFPC = _JnxSRX550SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 86, 1)
)
_JnxSRX550SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX550SlotRE = _JnxSRX550SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 86, 2)
)
_JnxSRX550SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX550SlotPower = _JnxSRX550SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 86, 3)
)
_JnxSRX550SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX550SlotFan = _JnxSRX550SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 86, 4)
)
_JnxSlotACX_ObjectIdentity = ObjectIdentity
jnxSlotACX = _JnxSlotACX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 87)
)
_JnxACXSlotFPC_ObjectIdentity = ObjectIdentity
jnxACXSlotFPC = _JnxACXSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 87, 1)
)
_JnxACXSlotFEB_ObjectIdentity = ObjectIdentity
jnxACXSlotFEB = _JnxACXSlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 87, 2)
)
_JnxACXSlotRE_ObjectIdentity = ObjectIdentity
jnxACXSlotRE = _JnxACXSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 87, 3)
)
_JnxACXSlotPower_ObjectIdentity = ObjectIdentity
jnxACXSlotPower = _JnxACXSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 87, 4)
)
_JnxACXSlotFan_ObjectIdentity = ObjectIdentity
jnxACXSlotFan = _JnxACXSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 87, 5)
)
_JnxSlotMX40_ObjectIdentity = ObjectIdentity
jnxSlotMX40 = _JnxSlotMX40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 88)
)
_JnxMX40SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX40SlotFPC = _JnxMX40SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 88, 1)
)
_JnxMX40SlotCFEB_ObjectIdentity = ObjectIdentity
jnxMX40SlotCFEB = _JnxMX40SlotCFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 88, 2)
)
_JnxMX40SlotRE_ObjectIdentity = ObjectIdentity
jnxMX40SlotRE = _JnxMX40SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 88, 3)
)
_JnxMX40SlotPower_ObjectIdentity = ObjectIdentity
jnxMX40SlotPower = _JnxMX40SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 88, 4)
)
_JnxMX40SlotFan_ObjectIdentity = ObjectIdentity
jnxMX40SlotFan = _JnxMX40SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 88, 5)
)
_JnxSlotMX10_ObjectIdentity = ObjectIdentity
jnxSlotMX10 = _JnxSlotMX10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 89)
)
_JnxMX10SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX10SlotFPC = _JnxMX10SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 89, 1)
)
_JnxMX10SlotCFEB_ObjectIdentity = ObjectIdentity
jnxMX10SlotCFEB = _JnxMX10SlotCFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 89, 2)
)
_JnxMX10SlotRE_ObjectIdentity = ObjectIdentity
jnxMX10SlotRE = _JnxMX10SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 89, 3)
)
_JnxMX10SlotPower_ObjectIdentity = ObjectIdentity
jnxMX10SlotPower = _JnxMX10SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 89, 4)
)
_JnxMX10SlotFan_ObjectIdentity = ObjectIdentity
jnxMX10SlotFan = _JnxMX10SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 89, 5)
)
_JnxSlotMX5_ObjectIdentity = ObjectIdentity
jnxSlotMX5 = _JnxSlotMX5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 90)
)
_JnxMX5SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX5SlotFPC = _JnxMX5SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 90, 1)
)
_JnxMX5SlotCFEB_ObjectIdentity = ObjectIdentity
jnxMX5SlotCFEB = _JnxMX5SlotCFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 90, 2)
)
_JnxMX5SlotRE_ObjectIdentity = ObjectIdentity
jnxMX5SlotRE = _JnxMX5SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 90, 3)
)
_JnxMX5SlotPower_ObjectIdentity = ObjectIdentity
jnxMX5SlotPower = _JnxMX5SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 90, 4)
)
_JnxMX5SlotFan_ObjectIdentity = ObjectIdentity
jnxMX5SlotFan = _JnxMX5SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 90, 5)
)
_JnxSlotQFXMInterconnect_ObjectIdentity = ObjectIdentity
jnxSlotQFXMInterconnect = _JnxSlotQFXMInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 91)
)
_JnxQFXMInterconnectSlotFPC_ObjectIdentity = ObjectIdentity
jnxQFXMInterconnectSlotFPC = _JnxQFXMInterconnectSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 91, 1)
)
_JnxQFXMInterconnectSlotHM_ObjectIdentity = ObjectIdentity
jnxQFXMInterconnectSlotHM = _JnxQFXMInterconnectSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 91, 2)
)
_JnxQFXMInterconnectSlotPower_ObjectIdentity = ObjectIdentity
jnxQFXMInterconnectSlotPower = _JnxQFXMInterconnectSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 91, 3)
)
_JnxQFXMInterconnectSlotFan_ObjectIdentity = ObjectIdentity
jnxQFXMInterconnectSlotFan = _JnxQFXMInterconnectSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 91, 4)
)
_JnxQFXMInterconnectSlotFPB_ObjectIdentity = ObjectIdentity
jnxQFXMInterconnectSlotFPB = _JnxQFXMInterconnectSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 91, 5)
)
_JnxSlotEX4550_ObjectIdentity = ObjectIdentity
jnxSlotEX4550 = _JnxSlotEX4550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 92)
)
_JnxEX4550SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX4550SlotFPC = _JnxEX4550SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 92, 1)
)
_JnxEX4550SlotPower_ObjectIdentity = ObjectIdentity
jnxEX4550SlotPower = _JnxEX4550SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 92, 1, 1)
)
_JnxEX4550SlotFan_ObjectIdentity = ObjectIdentity
jnxEX4550SlotFan = _JnxEX4550SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 92, 1, 2)
)
_JnxEX4550SlotRE_ObjectIdentity = ObjectIdentity
jnxEX4550SlotRE = _JnxEX4550SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 92, 1, 3)
)
_JnxSlotMX2020_ObjectIdentity = ObjectIdentity
jnxSlotMX2020 = _JnxSlotMX2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 93)
)
_JnxMX2020SlotSFB_ObjectIdentity = ObjectIdentity
jnxMX2020SlotSFB = _JnxMX2020SlotSFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 93, 1)
)
_JnxMX2020SlotHM_ObjectIdentity = ObjectIdentity
jnxMX2020SlotHM = _JnxMX2020SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 93, 2)
)
_JnxMX2020SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX2020SlotFPC = _JnxMX2020SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 93, 3)
)
_JnxMX2020SlotFan_ObjectIdentity = ObjectIdentity
jnxMX2020SlotFan = _JnxMX2020SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 93, 4)
)
_JnxMX2020SlotCB_ObjectIdentity = ObjectIdentity
jnxMX2020SlotCB = _JnxMX2020SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 93, 5)
)
_JnxMX2020SlotFPB_ObjectIdentity = ObjectIdentity
jnxMX2020SlotFPB = _JnxMX2020SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 93, 6)
)
_JnxMX2020SlotSPMB_ObjectIdentity = ObjectIdentity
jnxMX2020SlotSPMB = _JnxMX2020SlotSPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 93, 7)
)
_JnxMX2020SlotPDM_ObjectIdentity = ObjectIdentity
jnxMX2020SlotPDM = _JnxMX2020SlotPDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 93, 8)
)
_JnxMX2020SlotPSM_ObjectIdentity = ObjectIdentity
jnxMX2020SlotPSM = _JnxMX2020SlotPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 93, 9)
)
_JnxMX2020SlotADC_ObjectIdentity = ObjectIdentity
jnxMX2020SlotADC = _JnxMX2020SlotADC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 93, 10)
)
_JnxSlotVseries_ObjectIdentity = ObjectIdentity
jnxSlotVseries = _JnxSlotVseries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 94)
)
_JnxVseriesSlotFPC_ObjectIdentity = ObjectIdentity
jnxVseriesSlotFPC = _JnxVseriesSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 94, 1)
)
_JnxVseriesSlotRE_ObjectIdentity = ObjectIdentity
jnxVseriesSlotRE = _JnxVseriesSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 94, 2)
)
_JnxVseriesSlotPower_ObjectIdentity = ObjectIdentity
jnxVseriesSlotPower = _JnxVseriesSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 94, 3)
)
_JnxVseriesSlotFan_ObjectIdentity = ObjectIdentity
jnxVseriesSlotFan = _JnxVseriesSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 94, 4)
)
_JnxSlotLN2600_ObjectIdentity = ObjectIdentity
jnxSlotLN2600 = _JnxSlotLN2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 95)
)
_JnxLN2600SlotFPC_ObjectIdentity = ObjectIdentity
jnxLN2600SlotFPC = _JnxLN2600SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 95, 1)
)
_JnxLN2600SlotRE_ObjectIdentity = ObjectIdentity
jnxLN2600SlotRE = _JnxLN2600SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 95, 2)
)
_JnxLN2600SlotPower_ObjectIdentity = ObjectIdentity
jnxLN2600SlotPower = _JnxLN2600SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 95, 3)
)
_JnxLN2600SlotFan_ObjectIdentity = ObjectIdentity
jnxLN2600SlotFan = _JnxLN2600SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 95, 4)
)
_JnxSlotFireflyPerimeter_ObjectIdentity = ObjectIdentity
jnxSlotFireflyPerimeter = _JnxSlotFireflyPerimeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 96)
)
_JnxFireflyPerimeterSlotFPC_ObjectIdentity = ObjectIdentity
jnxFireflyPerimeterSlotFPC = _JnxFireflyPerimeterSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 96, 1)
)
_JnxFireflyPerimeterSlotRE_ObjectIdentity = ObjectIdentity
jnxFireflyPerimeterSlotRE = _JnxFireflyPerimeterSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 96, 2)
)
_JnxFireflyPerimeterSlotPower_ObjectIdentity = ObjectIdentity
jnxFireflyPerimeterSlotPower = _JnxFireflyPerimeterSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 96, 3)
)
_JnxFireflyPerimeterSlotFan_ObjectIdentity = ObjectIdentity
jnxFireflyPerimeterSlotFan = _JnxFireflyPerimeterSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 96, 4)
)
_JnxSlotMX104_ObjectIdentity = ObjectIdentity
jnxSlotMX104 = _JnxSlotMX104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 97)
)
_JnxMX104SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX104SlotFPC = _JnxMX104SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 97, 1)
)
_JnxMX104SlotAFEB_ObjectIdentity = ObjectIdentity
jnxMX104SlotAFEB = _JnxMX104SlotAFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 97, 2)
)
_JnxMX104SlotRE_ObjectIdentity = ObjectIdentity
jnxMX104SlotRE = _JnxMX104SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 97, 3)
)
_JnxMX104SlotPower_ObjectIdentity = ObjectIdentity
jnxMX104SlotPower = _JnxMX104SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 97, 4)
)
_JnxMX104SlotFan_ObjectIdentity = ObjectIdentity
jnxMX104SlotFan = _JnxMX104SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 97, 5)
)
_JnxMX104SlotFPM_ObjectIdentity = ObjectIdentity
jnxMX104SlotFPM = _JnxMX104SlotFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 97, 6)
)
_JnxSlotPTX3000_ObjectIdentity = ObjectIdentity
jnxSlotPTX3000 = _JnxSlotPTX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 98)
)
_JnxPTX3000SlotSIB_ObjectIdentity = ObjectIdentity
jnxPTX3000SlotSIB = _JnxPTX3000SlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 98, 1)
)
_JnxPTX3000SlotHM_ObjectIdentity = ObjectIdentity
jnxPTX3000SlotHM = _JnxPTX3000SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 98, 2)
)
_JnxPTX3000SlotFPC_ObjectIdentity = ObjectIdentity
jnxPTX3000SlotFPC = _JnxPTX3000SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 98, 3)
)
_JnxPTX3000SlotFan_ObjectIdentity = ObjectIdentity
jnxPTX3000SlotFan = _JnxPTX3000SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 98, 4)
)
_JnxPTX3000SlotCB_ObjectIdentity = ObjectIdentity
jnxPTX3000SlotCB = _JnxPTX3000SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 98, 5)
)
_JnxPTX3000SlotFPB_ObjectIdentity = ObjectIdentity
jnxPTX3000SlotFPB = _JnxPTX3000SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 98, 6)
)
_JnxPTX3000SlotPSM_ObjectIdentity = ObjectIdentity
jnxPTX3000SlotPSM = _JnxPTX3000SlotPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 98, 7)
)
_JnxPTX3000SlotPIC_ObjectIdentity = ObjectIdentity
jnxPTX3000SlotPIC = _JnxPTX3000SlotPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 98, 8)
)
_JnxSlotMX2010_ObjectIdentity = ObjectIdentity
jnxSlotMX2010 = _JnxSlotMX2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 99)
)
_JnxMX2010SlotSFB_ObjectIdentity = ObjectIdentity
jnxMX2010SlotSFB = _JnxMX2010SlotSFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 99, 1)
)
_JnxMX2010SlotHM_ObjectIdentity = ObjectIdentity
jnxMX2010SlotHM = _JnxMX2010SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 99, 2)
)
_JnxMX2010SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX2010SlotFPC = _JnxMX2010SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 99, 3)
)
_JnxMX2010SlotFan_ObjectIdentity = ObjectIdentity
jnxMX2010SlotFan = _JnxMX2010SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 99, 4)
)
_JnxMX2010SlotCB_ObjectIdentity = ObjectIdentity
jnxMX2010SlotCB = _JnxMX2010SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 99, 5)
)
_JnxMX2010SlotFPB_ObjectIdentity = ObjectIdentity
jnxMX2010SlotFPB = _JnxMX2010SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 99, 6)
)
_JnxMX2010SlotSPMB_ObjectIdentity = ObjectIdentity
jnxMX2010SlotSPMB = _JnxMX2010SlotSPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 99, 7)
)
_JnxMX2010SlotPDM_ObjectIdentity = ObjectIdentity
jnxMX2010SlotPDM = _JnxMX2010SlotPDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 99, 8)
)
_JnxMX2010SlotPSM_ObjectIdentity = ObjectIdentity
jnxMX2010SlotPSM = _JnxMX2010SlotPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 99, 9)
)
_JnxMX2010SlotADC_ObjectIdentity = ObjectIdentity
jnxMX2010SlotADC = _JnxMX2010SlotADC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 99, 10)
)
_JnxSlotQFX3100_ObjectIdentity = ObjectIdentity
jnxSlotQFX3100 = _JnxSlotQFX3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 100)
)
_JnxQFX3100SlotCPU_ObjectIdentity = ObjectIdentity
jnxQFX3100SlotCPU = _JnxQFX3100SlotCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 100, 1)
)
_JnxQFX3100SlotMemory_ObjectIdentity = ObjectIdentity
jnxQFX3100SlotMemory = _JnxQFX3100SlotMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 100, 2)
)
_JnxQFX3100SlotPower_ObjectIdentity = ObjectIdentity
jnxQFX3100SlotPower = _JnxQFX3100SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 100, 3)
)
_JnxQFX3100SlotFan_ObjectIdentity = ObjectIdentity
jnxQFX3100SlotFan = _JnxQFX3100SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 100, 4)
)
_JnxQFX3100SlotHardDisk_ObjectIdentity = ObjectIdentity
jnxQFX3100SlotHardDisk = _JnxQFX3100SlotHardDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 100, 5)
)
_JnxQFX3100SlotNIC_ObjectIdentity = ObjectIdentity
jnxQFX3100SlotNIC = _JnxQFX3100SlotNIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 100, 6)
)
_JnxSlotLN2800_ObjectIdentity = ObjectIdentity
jnxSlotLN2800 = _JnxSlotLN2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 101)
)
_JnxLN2800SlotFPC_ObjectIdentity = ObjectIdentity
jnxLN2800SlotFPC = _JnxLN2800SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 101, 1)
)
_JnxLN2800SlotRE_ObjectIdentity = ObjectIdentity
jnxLN2800SlotRE = _JnxLN2800SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 101, 2)
)
_JnxLN2800SlotPower_ObjectIdentity = ObjectIdentity
jnxLN2800SlotPower = _JnxLN2800SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 101, 3)
)
_JnxLN2800SlotFan_ObjectIdentity = ObjectIdentity
jnxLN2800SlotFan = _JnxLN2800SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 101, 4)
)
_JnxSlotEX9214_ObjectIdentity = ObjectIdentity
jnxSlotEX9214 = _JnxSlotEX9214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 102)
)
_JnxEX9214SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX9214SlotFPC = _JnxEX9214SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 102, 1)
)
_JnxEX9214SlotHM_ObjectIdentity = ObjectIdentity
jnxEX9214SlotHM = _JnxEX9214SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 102, 2)
)
_JnxEX9214SlotPower_ObjectIdentity = ObjectIdentity
jnxEX9214SlotPower = _JnxEX9214SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 102, 3)
)
_JnxEX9214SlotFan_ObjectIdentity = ObjectIdentity
jnxEX9214SlotFan = _JnxEX9214SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 102, 4)
)
_JnxEX9214SlotCB_ObjectIdentity = ObjectIdentity
jnxEX9214SlotCB = _JnxEX9214SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 102, 5)
)
_JnxEX9214SlotFPB_ObjectIdentity = ObjectIdentity
jnxEX9214SlotFPB = _JnxEX9214SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 102, 6)
)
_JnxSlotEX9208_ObjectIdentity = ObjectIdentity
jnxSlotEX9208 = _JnxSlotEX9208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 103)
)
_JnxEX9208SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX9208SlotFPC = _JnxEX9208SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 103, 1)
)
_JnxEX9208SlotHM_ObjectIdentity = ObjectIdentity
jnxEX9208SlotHM = _JnxEX9208SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 103, 2)
)
_JnxEX9208SlotPower_ObjectIdentity = ObjectIdentity
jnxEX9208SlotPower = _JnxEX9208SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 103, 3)
)
_JnxEX9208SlotFan_ObjectIdentity = ObjectIdentity
jnxEX9208SlotFan = _JnxEX9208SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 103, 4)
)
_JnxEX9208SlotCB_ObjectIdentity = ObjectIdentity
jnxEX9208SlotCB = _JnxEX9208SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 103, 5)
)
_JnxEX9208SlotFPB_ObjectIdentity = ObjectIdentity
jnxEX9208SlotFPB = _JnxEX9208SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 103, 6)
)
_JnxSlotEX9204_ObjectIdentity = ObjectIdentity
jnxSlotEX9204 = _JnxSlotEX9204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 104)
)
_JnxEX9204SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX9204SlotFPC = _JnxEX9204SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 104, 1)
)
_JnxEX9204SlotHM_ObjectIdentity = ObjectIdentity
jnxEX9204SlotHM = _JnxEX9204SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 104, 2)
)
_JnxEX9204SlotPower_ObjectIdentity = ObjectIdentity
jnxEX9204SlotPower = _JnxEX9204SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 104, 3)
)
_JnxEX9204SlotFan_ObjectIdentity = ObjectIdentity
jnxEX9204SlotFan = _JnxEX9204SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 104, 4)
)
_JnxEX9204SlotCB_ObjectIdentity = ObjectIdentity
jnxEX9204SlotCB = _JnxEX9204SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 104, 5)
)
_JnxEX9204SlotFPB_ObjectIdentity = ObjectIdentity
jnxEX9204SlotFPB = _JnxEX9204SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 104, 6)
)
_JnxSlotSRX5400_ObjectIdentity = ObjectIdentity
jnxSlotSRX5400 = _JnxSlotSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 105)
)
_JnxSRX5400SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX5400SlotFPC = _JnxSRX5400SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 105, 1)
)
_JnxSRX5400SlotHM_ObjectIdentity = ObjectIdentity
jnxSRX5400SlotHM = _JnxSRX5400SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 105, 2)
)
_JnxSRX5400SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX5400SlotPower = _JnxSRX5400SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 105, 3)
)
_JnxSRX5400SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX5400SlotFan = _JnxSRX5400SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 105, 4)
)
_JnxSRX5400SlotCB_ObjectIdentity = ObjectIdentity
jnxSRX5400SlotCB = _JnxSRX5400SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 105, 5)
)
_JnxSRX5400SlotFPB_ObjectIdentity = ObjectIdentity
jnxSRX5400SlotFPB = _JnxSRX5400SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 105, 6)
)
_JnxSlotIBM4274S54J54S_ObjectIdentity = ObjectIdentity
jnxSlotIBM4274S54J54S = _JnxSlotIBM4274S54J54S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 106)
)
_JnxIBM4274S54J54SSlotFPC_ObjectIdentity = ObjectIdentity
jnxIBM4274S54J54SSlotFPC = _JnxIBM4274S54J54SSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 106, 1)
)
_JnxIBM4274S54J54SSlotHM_ObjectIdentity = ObjectIdentity
jnxIBM4274S54J54SSlotHM = _JnxIBM4274S54J54SSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 106, 2)
)
_JnxIBM4274S54J54SSlotPower_ObjectIdentity = ObjectIdentity
jnxIBM4274S54J54SSlotPower = _JnxIBM4274S54J54SSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 106, 3)
)
_JnxIBM4274S54J54SSlotFan_ObjectIdentity = ObjectIdentity
jnxIBM4274S54J54SSlotFan = _JnxIBM4274S54J54SSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 106, 4)
)
_JnxIBM4274S54J54SSlotCB_ObjectIdentity = ObjectIdentity
jnxIBM4274S54J54SSlotCB = _JnxIBM4274S54J54SSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 106, 5)
)
_JnxIBM4274S54J54SSlotFPB_ObjectIdentity = ObjectIdentity
jnxIBM4274S54J54SSlotFPB = _JnxIBM4274S54J54SSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 106, 6)
)
_JnxSlotDELLJSRX5400_ObjectIdentity = ObjectIdentity
jnxSlotDELLJSRX5400 = _JnxSlotDELLJSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 107)
)
_JnxDELLJSRX5400SlotFPC_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5400SlotFPC = _JnxDELLJSRX5400SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 107, 1)
)
_JnxDELLJSRX5400SlotHM_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5400SlotHM = _JnxDELLJSRX5400SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 107, 2)
)
_JnxDELLJSRX5400SlotPower_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5400SlotPower = _JnxDELLJSRX5400SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 107, 3)
)
_JnxDELLJSRX5400SlotFan_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5400SlotFan = _JnxDELLJSRX5400SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 107, 4)
)
_JnxDELLJSRX5400SlotCB_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5400SlotCB = _JnxDELLJSRX5400SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 107, 5)
)
_JnxDELLJSRX5400SlotFPB_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5400SlotFPB = _JnxDELLJSRX5400SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 107, 6)
)
_JnxSlotVMX_ObjectIdentity = ObjectIdentity
jnxSlotVMX = _JnxSlotVMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 108)
)
_JnxVMXSlotFPC_ObjectIdentity = ObjectIdentity
jnxVMXSlotFPC = _JnxVMXSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 108, 1)
)
_JnxVMxSlotPower_ObjectIdentity = ObjectIdentity
jnxVMxSlotPower = _JnxVMxSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 108, 2)
)
_JnxVMXSlotFan_ObjectIdentity = ObjectIdentity
jnxVMXSlotFan = _JnxVMXSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 108, 3)
)
_JnxVMXSlotCB_ObjectIdentity = ObjectIdentity
jnxVMXSlotCB = _JnxVMXSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 108, 4)
)
_JnxVMXSlotHM_ObjectIdentity = ObjectIdentity
jnxVMXSlotHM = _JnxVMXSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 108, 5)
)
_JnxSlotEX4600_ObjectIdentity = ObjectIdentity
jnxSlotEX4600 = _JnxSlotEX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 109)
)
_JnxEX4600SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX4600SlotFPC = _JnxEX4600SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 109, 1)
)
_JnxEX4600HM_ObjectIdentity = ObjectIdentity
jnxEX4600HM = _JnxEX4600HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 109, 2)
)
_JnxEX4600SlotPower_ObjectIdentity = ObjectIdentity
jnxEX4600SlotPower = _JnxEX4600SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 109, 3)
)
_JnxEX4600SlotFan_ObjectIdentity = ObjectIdentity
jnxEX4600SlotFan = _JnxEX4600SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 109, 4)
)
_JnxSlotVRR_ObjectIdentity = ObjectIdentity
jnxSlotVRR = _JnxSlotVRR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 110)
)
_JnxVRRSlotFPC_ObjectIdentity = ObjectIdentity
jnxVRRSlotFPC = _JnxVRRSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 110, 1)
)
_JnxVRRSlotRE_ObjectIdentity = ObjectIdentity
jnxVRRSlotRE = _JnxVRRSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 110, 2)
)
_JnxVRRSlotPower_ObjectIdentity = ObjectIdentity
jnxVRRSlotPower = _JnxVRRSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 110, 3)
)
_JnxVRRSlotFan_ObjectIdentity = ObjectIdentity
jnxVRRSlotFan = _JnxVRRSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 110, 4)
)
_JnxVRRSlotHM_ObjectIdentity = ObjectIdentity
jnxVRRSlotHM = _JnxVRRSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 110, 5)
)
_JnxVRRSlotCB_ObjectIdentity = ObjectIdentity
jnxVRRSlotCB = _JnxVRRSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 110, 6)
)
_JnxVRRSlotFPB_ObjectIdentity = ObjectIdentity
jnxVRRSlotFPB = _JnxVRRSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 110, 7)
)
_JnxSlotACX1000_ObjectIdentity = ObjectIdentity
jnxSlotACX1000 = _JnxSlotACX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 113)
)
_JnxACX1000SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX1000SlotFPC = _JnxACX1000SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 113, 1)
)
_JnxACX1000SlotFEB_ObjectIdentity = ObjectIdentity
jnxACX1000SlotFEB = _JnxACX1000SlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 113, 2)
)
_JnxACX1000SlotRE_ObjectIdentity = ObjectIdentity
jnxACX1000SlotRE = _JnxACX1000SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 113, 3)
)
_JnxACX1000SlotPower_ObjectIdentity = ObjectIdentity
jnxACX1000SlotPower = _JnxACX1000SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 113, 4)
)
_JnxSlotACX2000_ObjectIdentity = ObjectIdentity
jnxSlotACX2000 = _JnxSlotACX2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 114)
)
_JnxACX2000SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX2000SlotFPC = _JnxACX2000SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 114, 1)
)
_JnxACX2000SlotFEB_ObjectIdentity = ObjectIdentity
jnxACX2000SlotFEB = _JnxACX2000SlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 114, 2)
)
_JnxACX2000SlotRE_ObjectIdentity = ObjectIdentity
jnxACX2000SlotRE = _JnxACX2000SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 114, 3)
)
_JnxACX2000SlotPower_ObjectIdentity = ObjectIdentity
jnxACX2000SlotPower = _JnxACX2000SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 114, 4)
)
_JnxSlotACX1100_ObjectIdentity = ObjectIdentity
jnxSlotACX1100 = _JnxSlotACX1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 115)
)
_JnxACX1100SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX1100SlotFPC = _JnxACX1100SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 115, 1)
)
_JnxACX1100SlotFEB_ObjectIdentity = ObjectIdentity
jnxACX1100SlotFEB = _JnxACX1100SlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 115, 2)
)
_JnxACX1100SlotRE_ObjectIdentity = ObjectIdentity
jnxACX1100SlotRE = _JnxACX1100SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 115, 3)
)
_JnxACX1100SlotPower_ObjectIdentity = ObjectIdentity
jnxACX1100SlotPower = _JnxACX1100SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 115, 4)
)
_JnxSlotACX2100_ObjectIdentity = ObjectIdentity
jnxSlotACX2100 = _JnxSlotACX2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 116)
)
_JnxACX2100SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX2100SlotFPC = _JnxACX2100SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 116, 1)
)
_JnxACX2100SlotFEB_ObjectIdentity = ObjectIdentity
jnxACX2100SlotFEB = _JnxACX2100SlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 116, 2)
)
_JnxACX2100SlotRE_ObjectIdentity = ObjectIdentity
jnxACX2100SlotRE = _JnxACX2100SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 116, 3)
)
_JnxACX2100SlotPower_ObjectIdentity = ObjectIdentity
jnxACX2100SlotPower = _JnxACX2100SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 116, 4)
)
_JnxSlotACX2200_ObjectIdentity = ObjectIdentity
jnxSlotACX2200 = _JnxSlotACX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 117)
)
_JnxACX2200SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX2200SlotFPC = _JnxACX2200SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 117, 1)
)
_JnxACX2200SlotFEB_ObjectIdentity = ObjectIdentity
jnxACX2200SlotFEB = _JnxACX2200SlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 117, 2)
)
_JnxACX2200SlotRE_ObjectIdentity = ObjectIdentity
jnxACX2200SlotRE = _JnxACX2200SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 117, 3)
)
_JnxACX2200SlotPower_ObjectIdentity = ObjectIdentity
jnxACX2200SlotPower = _JnxACX2200SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 117, 4)
)
_JnxSlotACX4000_ObjectIdentity = ObjectIdentity
jnxSlotACX4000 = _JnxSlotACX4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 118)
)
_JnxACX4000SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX4000SlotFPC = _JnxACX4000SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 118, 1)
)
_JnxACX4000SlotFEB_ObjectIdentity = ObjectIdentity
jnxACX4000SlotFEB = _JnxACX4000SlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 118, 2)
)
_JnxACX4000SlotRE_ObjectIdentity = ObjectIdentity
jnxACX4000SlotRE = _JnxACX4000SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 118, 3)
)
_JnxACX4000SlotPower_ObjectIdentity = ObjectIdentity
jnxACX4000SlotPower = _JnxACX4000SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 118, 4)
)
_JnxACX4000SlotFan_ObjectIdentity = ObjectIdentity
jnxACX4000SlotFan = _JnxACX4000SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 118, 5)
)
_JnxSlotACX500AC_ObjectIdentity = ObjectIdentity
jnxSlotACX500AC = _JnxSlotACX500AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 119)
)
_JnxACX500ACSlotFPC_ObjectIdentity = ObjectIdentity
jnxACX500ACSlotFPC = _JnxACX500ACSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 119, 1)
)
_JnxACX500ACSlotFEB_ObjectIdentity = ObjectIdentity
jnxACX500ACSlotFEB = _JnxACX500ACSlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 119, 2)
)
_JnxACX500ACSlotRE_ObjectIdentity = ObjectIdentity
jnxACX500ACSlotRE = _JnxACX500ACSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 119, 3)
)
_JnxACX500ACSlotPower_ObjectIdentity = ObjectIdentity
jnxACX500ACSlotPower = _JnxACX500ACSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 119, 4)
)
_JnxSlotACX500DC_ObjectIdentity = ObjectIdentity
jnxSlotACX500DC = _JnxSlotACX500DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 120)
)
_JnxACX500DCSlotFPC_ObjectIdentity = ObjectIdentity
jnxACX500DCSlotFPC = _JnxACX500DCSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 120, 1)
)
_JnxACX500DCSlotFEB_ObjectIdentity = ObjectIdentity
jnxACX500DCSlotFEB = _JnxACX500DCSlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 120, 2)
)
_JnxACX500DCSlotRE_ObjectIdentity = ObjectIdentity
jnxACX500DCSlotRE = _JnxACX500DCSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 120, 3)
)
_JnxACX500DCSlotPower_ObjectIdentity = ObjectIdentity
jnxACX500DCSlotPower = _JnxACX500DCSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 120, 4)
)
_JnxSlotACX500OAC_ObjectIdentity = ObjectIdentity
jnxSlotACX500OAC = _JnxSlotACX500OAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 121)
)
_JnxACX500OACSlotFPC_ObjectIdentity = ObjectIdentity
jnxACX500OACSlotFPC = _JnxACX500OACSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 121, 1)
)
_JnxACX500OACSlotFEB_ObjectIdentity = ObjectIdentity
jnxACX500OACSlotFEB = _JnxACX500OACSlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 121, 2)
)
_JnxACX500OACSlotRE_ObjectIdentity = ObjectIdentity
jnxACX500OACSlotRE = _JnxACX500OACSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 121, 3)
)
_JnxACX500OACSlotPower_ObjectIdentity = ObjectIdentity
jnxACX500OACSlotPower = _JnxACX500OACSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 121, 4)
)
_JnxSlotACX500ODC_ObjectIdentity = ObjectIdentity
jnxSlotACX500ODC = _JnxSlotACX500ODC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 122)
)
_JnxACX500ODCSlotFPC_ObjectIdentity = ObjectIdentity
jnxACX500ODCSlotFPC = _JnxACX500ODCSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 122, 1)
)
_JnxACX500ODCSlotFEB_ObjectIdentity = ObjectIdentity
jnxACX500ODCSlotFEB = _JnxACX500ODCSlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 122, 2)
)
_JnxACX500ODCSlotRE_ObjectIdentity = ObjectIdentity
jnxACX500ODCSlotRE = _JnxACX500ODCSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 122, 3)
)
_JnxACX500ODCSlotPower_ObjectIdentity = ObjectIdentity
jnxACX500ODCSlotPower = _JnxACX500ODCSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 122, 4)
)
_JnxSlotACX500OPOEAC_ObjectIdentity = ObjectIdentity
jnxSlotACX500OPOEAC = _JnxSlotACX500OPOEAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 123)
)
_JnxACX500OPOEACSlotFPC_ObjectIdentity = ObjectIdentity
jnxACX500OPOEACSlotFPC = _JnxACX500OPOEACSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 123, 1)
)
_JnxACX500OPOEACSlotFEB_ObjectIdentity = ObjectIdentity
jnxACX500OPOEACSlotFEB = _JnxACX500OPOEACSlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 123, 2)
)
_JnxACX500OPOEACSlotRE_ObjectIdentity = ObjectIdentity
jnxACX500OPOEACSlotRE = _JnxACX500OPOEACSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 123, 3)
)
_JnxACX500OPOEACSlotPower_ObjectIdentity = ObjectIdentity
jnxACX500OPOEACSlotPower = _JnxACX500OPOEACSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 123, 4)
)
_JnxSlotACX500OPOEDC_ObjectIdentity = ObjectIdentity
jnxSlotACX500OPOEDC = _JnxSlotACX500OPOEDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 124)
)
_JnxACX500OPOEDCSlotFPC_ObjectIdentity = ObjectIdentity
jnxACX500OPOEDCSlotFPC = _JnxACX500OPOEDCSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 124, 1)
)
_JnxACX500OPOEDCSlotFEB_ObjectIdentity = ObjectIdentity
jnxACX500OPOEDCSlotFEB = _JnxACX500OPOEDCSlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 124, 2)
)
_JnxACX500OPOEDCSlotRE_ObjectIdentity = ObjectIdentity
jnxACX500OPOEDCSlotRE = _JnxACX500OPOEDCSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 124, 3)
)
_JnxACX500OPOEDCSlotPower_ObjectIdentity = ObjectIdentity
jnxACX500OPOEDCSlotPower = _JnxACX500OPOEDCSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 124, 4)
)
_JnxSlotSatelliteDevice_ObjectIdentity = ObjectIdentity
jnxSlotSatelliteDevice = _JnxSlotSatelliteDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 125)
)
_JnxSatelliteDeviceSlotFPC_ObjectIdentity = ObjectIdentity
jnxSatelliteDeviceSlotFPC = _JnxSatelliteDeviceSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 125, 1)
)
_JnxSatelliteDeviceSlotPower_ObjectIdentity = ObjectIdentity
jnxSatelliteDeviceSlotPower = _JnxSatelliteDeviceSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 125, 2)
)
_JnxSatelliteDeviceSlotFan_ObjectIdentity = ObjectIdentity
jnxSatelliteDeviceSlotFan = _JnxSatelliteDeviceSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 125, 3)
)
_JnxSlotACX5048_ObjectIdentity = ObjectIdentity
jnxSlotACX5048 = _JnxSlotACX5048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 126)
)
_JnxACX5048SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX5048SlotFPC = _JnxACX5048SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 126, 1)
)
_JnxACX5048SlotHM_ObjectIdentity = ObjectIdentity
jnxACX5048SlotHM = _JnxACX5048SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 126, 2)
)
_JnxACX5048SlotPower_ObjectIdentity = ObjectIdentity
jnxACX5048SlotPower = _JnxACX5048SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 126, 3)
)
_JnxACX5048SlotFan_ObjectIdentity = ObjectIdentity
jnxACX5048SlotFan = _JnxACX5048SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 126, 4)
)
_JnxACX5048SlotFPB_ObjectIdentity = ObjectIdentity
jnxACX5048SlotFPB = _JnxACX5048SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 126, 5)
)
_JnxSlotACX5096_ObjectIdentity = ObjectIdentity
jnxSlotACX5096 = _JnxSlotACX5096_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 127)
)
_JnxACX5096SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX5096SlotFPC = _JnxACX5096SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 127, 1)
)
_JnxACX5096SlotHM_ObjectIdentity = ObjectIdentity
jnxACX5096SlotHM = _JnxACX5096SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 127, 2)
)
_JnxACX5096SlotPower_ObjectIdentity = ObjectIdentity
jnxACX5096SlotPower = _JnxACX5096SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 127, 3)
)
_JnxACX5096SlotFan_ObjectIdentity = ObjectIdentity
jnxACX5096SlotFan = _JnxACX5096SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 127, 4)
)
_JnxACX5096SlotFPB_ObjectIdentity = ObjectIdentity
jnxACX5096SlotFPB = _JnxACX5096SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 127, 5)
)
_JnxSlotLN1000CC_ObjectIdentity = ObjectIdentity
jnxSlotLN1000CC = _JnxSlotLN1000CC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 128)
)
_JnxLN1000CCSlotFPC_ObjectIdentity = ObjectIdentity
jnxLN1000CCSlotFPC = _JnxLN1000CCSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 128, 1)
)
_JnxLN1000CCSlotRE_ObjectIdentity = ObjectIdentity
jnxLN1000CCSlotRE = _JnxLN1000CCSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 128, 2)
)
_JnxLN1000CCSlotPower_ObjectIdentity = ObjectIdentity
jnxLN1000CCSlotPower = _JnxLN1000CCSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 128, 3)
)
_JnxLN1000CCSlotFan_ObjectIdentity = ObjectIdentity
jnxLN1000CCSlotFan = _JnxLN1000CCSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 128, 4)
)
_JnxSlotVSRX_ObjectIdentity = ObjectIdentity
jnxSlotVSRX = _JnxSlotVSRX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 129)
)
_JnxVSRXSlotFPC_ObjectIdentity = ObjectIdentity
jnxVSRXSlotFPC = _JnxVSRXSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 129, 1)
)
_JnxVSRXSlotRE_ObjectIdentity = ObjectIdentity
jnxVSRXSlotRE = _JnxVSRXSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 129, 2)
)
_JnxVSRXSlotPower_ObjectIdentity = ObjectIdentity
jnxVSRXSlotPower = _JnxVSRXSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 129, 3)
)
_JnxVSRXSlotFan_ObjectIdentity = ObjectIdentity
jnxVSRXSlotFan = _JnxVSRXSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 129, 4)
)
_JnxSlotPTX1000_ObjectIdentity = ObjectIdentity
jnxSlotPTX1000 = _JnxSlotPTX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 130)
)
_JnxPTX1000SlotFPC_ObjectIdentity = ObjectIdentity
jnxPTX1000SlotFPC = _JnxPTX1000SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 130, 1)
)
_JnxPTX1000SlotHM_ObjectIdentity = ObjectIdentity
jnxPTX1000SlotHM = _JnxPTX1000SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 130, 2)
)
_JnxPTX1000SlotPower_ObjectIdentity = ObjectIdentity
jnxPTX1000SlotPower = _JnxPTX1000SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 130, 3)
)
_JnxPTX1000SlotFan_ObjectIdentity = ObjectIdentity
jnxPTX1000SlotFan = _JnxPTX1000SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 130, 4)
)
_JnxPTX1000SlotFPB_ObjectIdentity = ObjectIdentity
jnxPTX1000SlotFPB = _JnxPTX1000SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 130, 5)
)
_JnxSlotEX3400_ObjectIdentity = ObjectIdentity
jnxSlotEX3400 = _JnxSlotEX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 131)
)
_JnxEX3400SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX3400SlotFPC = _JnxEX3400SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 131, 1)
)
_JnxEX3400SlotPower_ObjectIdentity = ObjectIdentity
jnxEX3400SlotPower = _JnxEX3400SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 131, 1, 1)
)
_JnxEX3400SlotFan_ObjectIdentity = ObjectIdentity
jnxEX3400SlotFan = _JnxEX3400SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 131, 1, 2)
)
_JnxSlotEX2300_ObjectIdentity = ObjectIdentity
jnxSlotEX2300 = _JnxSlotEX2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 132)
)
_JnxEX2300SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX2300SlotFPC = _JnxEX2300SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 132, 1)
)
_JnxEX2300SlotPower_ObjectIdentity = ObjectIdentity
jnxEX2300SlotPower = _JnxEX2300SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 132, 1, 1)
)
_JnxEX2300SlotFan_ObjectIdentity = ObjectIdentity
jnxEX2300SlotFan = _JnxEX2300SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 132, 1, 2)
)
_JnxSlotSRX300_ObjectIdentity = ObjectIdentity
jnxSlotSRX300 = _JnxSlotSRX300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 133)
)
_JnxSRX300SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX300SlotFPC = _JnxSRX300SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 133, 1)
)
_JnxSRX300SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX300SlotRE = _JnxSRX300SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 133, 2)
)
_JnxSRX300SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX300SlotPower = _JnxSRX300SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 133, 3)
)
_JnxSRX300SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX300SlotFan = _JnxSRX300SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 133, 4)
)
_JnxSlotSRX320_ObjectIdentity = ObjectIdentity
jnxSlotSRX320 = _JnxSlotSRX320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 134)
)
_JnxSRX320SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX320SlotFPC = _JnxSRX320SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 134, 1)
)
_JnxSRX320SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX320SlotRE = _JnxSRX320SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 134, 2)
)
_JnxSRX320SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX320SlotPower = _JnxSRX320SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 134, 3)
)
_JnxSRX320SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX320SlotFan = _JnxSRX320SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 134, 4)
)
_JnxSlotSRX340_ObjectIdentity = ObjectIdentity
jnxSlotSRX340 = _JnxSlotSRX340_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 135)
)
_JnxSRX340SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX340SlotFPC = _JnxSRX340SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 135, 1)
)
_JnxSRX340SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX340SlotRE = _JnxSRX340SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 135, 2)
)
_JnxSRX340SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX340SlotPower = _JnxSRX340SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 135, 3)
)
_JnxSRX340SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX340SlotFan = _JnxSRX340SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 135, 4)
)
_JnxSlotSRX345_ObjectIdentity = ObjectIdentity
jnxSlotSRX345 = _JnxSlotSRX345_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 136)
)
_JnxSRX345SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX345SlotFPC = _JnxSRX345SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 136, 1)
)
_JnxSRX345SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX345SlotRE = _JnxSRX345SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 136, 2)
)
_JnxSRX345SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX345SlotPower = _JnxSRX345SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 136, 3)
)
_JnxSRX345SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX345SlotFan = _JnxSRX345SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 136, 4)
)
_JnxSlotSRX1500_ObjectIdentity = ObjectIdentity
jnxSlotSRX1500 = _JnxSlotSRX1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 137)
)
_JnxSRX1500SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX1500SlotFPC = _JnxSRX1500SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 137, 1)
)
_JnxSRX1500SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX1500SlotRE = _JnxSRX1500SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 137, 2)
)
_JnxSRX1500SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX1500SlotPower = _JnxSRX1500SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 137, 3)
)
_JnxSRX1500SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX1500SlotFan = _JnxSRX1500SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 137, 4)
)
_JnxSRX1500SlotCB_ObjectIdentity = ObjectIdentity
jnxSRX1500SlotCB = _JnxSRX1500SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 137, 5)
)
_JnxSlotNFX_ObjectIdentity = ObjectIdentity
jnxSlotNFX = _JnxSlotNFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 138)
)
_JnxNFXSlotFPC_ObjectIdentity = ObjectIdentity
jnxNFXSlotFPC = _JnxNFXSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 138, 1)
)
_JnxNFXSlotPIC_ObjectIdentity = ObjectIdentity
jnxNFXSlotPIC = _JnxNFXSlotPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 138, 2)
)
_JnxNFXSlotHM_ObjectIdentity = ObjectIdentity
jnxNFXSlotHM = _JnxNFXSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 138, 3)
)
_JnxNFXSlotPower_ObjectIdentity = ObjectIdentity
jnxNFXSlotPower = _JnxNFXSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 138, 4)
)
_JnxNFXSlotFan_ObjectIdentity = ObjectIdentity
jnxNFXSlotFan = _JnxNFXSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 138, 5)
)
_JnxSlotJNP10003_ObjectIdentity = ObjectIdentity
jnxSlotJNP10003 = _JnxSlotJNP10003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 139)
)
_JnxJNP10003SlotHM_ObjectIdentity = ObjectIdentity
jnxJNP10003SlotHM = _JnxJNP10003SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 139, 1)
)
_JnxJNP10003SlotFPC_ObjectIdentity = ObjectIdentity
jnxJNP10003SlotFPC = _JnxJNP10003SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 139, 2)
)
_JnxJNP10003SlotFan_ObjectIdentity = ObjectIdentity
jnxJNP10003SlotFan = _JnxJNP10003SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 139, 3)
)
_JnxJNP10003SlotCB_ObjectIdentity = ObjectIdentity
jnxJNP10003SlotCB = _JnxJNP10003SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 139, 4)
)
_JnxJNP10003SlotPower_ObjectIdentity = ObjectIdentity
jnxJNP10003SlotPower = _JnxJNP10003SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 139, 5)
)
_JnxSlotSRX4600_ObjectIdentity = ObjectIdentity
jnxSlotSRX4600 = _JnxSlotSRX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 140)
)
_JnxSRX4600SlotHM_ObjectIdentity = ObjectIdentity
jnxSRX4600SlotHM = _JnxSRX4600SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 140, 1)
)
_JnxSRX4600SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX4600SlotFPC = _JnxSRX4600SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 140, 2)
)
_JnxSRX4600SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX4600SlotFan = _JnxSRX4600SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 140, 3)
)
_JnxSRX4600SlotSPMB_ObjectIdentity = ObjectIdentity
jnxSRX4600SlotSPMB = _JnxSRX4600SlotSPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 140, 4)
)
_JnxSRX4600SlotPSM_ObjectIdentity = ObjectIdentity
jnxSRX4600SlotPSM = _JnxSRX4600SlotPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 140, 5)
)
_JnxSlotSRX4800_ObjectIdentity = ObjectIdentity
jnxSlotSRX4800 = _JnxSlotSRX4800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 141)
)
_JnxSRX4800SlotHM_ObjectIdentity = ObjectIdentity
jnxSRX4800SlotHM = _JnxSRX4800SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 141, 1)
)
_JnxSRX4800SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX4800SlotFPC = _JnxSRX4800SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 141, 2)
)
_JnxSRX4800SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX4800SlotFan = _JnxSRX4800SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 141, 3)
)
_JnxSRX4800SlotSPMB_ObjectIdentity = ObjectIdentity
jnxSRX4800SlotSPMB = _JnxSRX4800SlotSPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 141, 4)
)
_JnxSRX4800SlotPSM_ObjectIdentity = ObjectIdentity
jnxSRX4800SlotPSM = _JnxSRX4800SlotPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 141, 5)
)
_JnxSlotSRX4100_ObjectIdentity = ObjectIdentity
jnxSlotSRX4100 = _JnxSlotSRX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 142)
)
_JnxSRX4100SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX4100SlotFPC = _JnxSRX4100SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 142, 1)
)
_JnxSRX4100SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX4100SlotRE = _JnxSRX4100SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 142, 2)
)
_JnxSRX4100SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX4100SlotPower = _JnxSRX4100SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 142, 3)
)
_JnxSRX4100SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX4100SlotFan = _JnxSRX4100SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 142, 4)
)
_JnxSlotSRX4200_ObjectIdentity = ObjectIdentity
jnxSlotSRX4200 = _JnxSlotSRX4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 143)
)
_JnxSRX4200SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX4200SlotFPC = _JnxSRX4200SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 143, 1)
)
_JnxSRX4200SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX4200SlotRE = _JnxSRX4200SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 143, 2)
)
_JnxSRX4200SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX4200SlotPower = _JnxSRX4200SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 143, 3)
)
_JnxSRX4200SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX4200SlotFan = _JnxSRX4200SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 143, 4)
)
_JnxSlotJNP204_ObjectIdentity = ObjectIdentity
jnxSlotJNP204 = _JnxSlotJNP204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 144)
)
_JnxJNP204SlotHM_ObjectIdentity = ObjectIdentity
jnxJNP204SlotHM = _JnxJNP204SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 144, 1)
)
_JnxJNP204SlotFPC_ObjectIdentity = ObjectIdentity
jnxJNP204SlotFPC = _JnxJNP204SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 144, 2)
)
_JnxJNP204SlotFan_ObjectIdentity = ObjectIdentity
jnxJNP204SlotFan = _JnxJNP204SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 144, 3)
)
_JnxJNP204SlotCB_ObjectIdentity = ObjectIdentity
jnxJNP204SlotCB = _JnxJNP204SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 144, 4)
)
_JnxJNP204SlotPower_ObjectIdentity = ObjectIdentity
jnxJNP204SlotPower = _JnxJNP204SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 144, 5)
)
_JnxSlotMX2008_ObjectIdentity = ObjectIdentity
jnxSlotMX2008 = _JnxSlotMX2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 145)
)
_JnxMX2008SlotSFB_ObjectIdentity = ObjectIdentity
jnxMX2008SlotSFB = _JnxMX2008SlotSFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 145, 1)
)
_JnxMX2008SlotHM_ObjectIdentity = ObjectIdentity
jnxMX2008SlotHM = _JnxMX2008SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 145, 2)
)
_JnxMX2008SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX2008SlotFPC = _JnxMX2008SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 145, 3)
)
_JnxMX2008SlotFan_ObjectIdentity = ObjectIdentity
jnxMX2008SlotFan = _JnxMX2008SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 145, 4)
)
_JnxMX2008SlotRCB_ObjectIdentity = ObjectIdentity
jnxMX2008SlotRCB = _JnxMX2008SlotRCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 145, 5)
)
_JnxMX2008SlotFPB_ObjectIdentity = ObjectIdentity
jnxMX2008SlotFPB = _JnxMX2008SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 145, 6)
)
_JnxMX2008SlotPDM_ObjectIdentity = ObjectIdentity
jnxMX2008SlotPDM = _JnxMX2008SlotPDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 145, 7)
)
_JnxMX2008SlotPSM_ObjectIdentity = ObjectIdentity
jnxMX2008SlotPSM = _JnxMX2008SlotPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 145, 8)
)
_JnxMX2008SlotADC_ObjectIdentity = ObjectIdentity
jnxMX2008SlotADC = _JnxMX2008SlotADC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 145, 9)
)
_JnxSlotMXTSR80_ObjectIdentity = ObjectIdentity
jnxSlotMXTSR80 = _JnxSlotMXTSR80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 146)
)
_JnxMXTSR80SlotFPC_ObjectIdentity = ObjectIdentity
jnxMXTSR80SlotFPC = _JnxMXTSR80SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 146, 1)
)
_JnxMXTSR80SlotAFEB_ObjectIdentity = ObjectIdentity
jnxMXTSR80SlotAFEB = _JnxMXTSR80SlotAFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 146, 2)
)
_JnxMXTSR80SlotRE_ObjectIdentity = ObjectIdentity
jnxMXTSR80SlotRE = _JnxMXTSR80SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 146, 3)
)
_JnxMXTSR80SlotPower_ObjectIdentity = ObjectIdentity
jnxMXTSR80SlotPower = _JnxMXTSR80SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 146, 4)
)
_JnxMXTSR80SlotFan_ObjectIdentity = ObjectIdentity
jnxMXTSR80SlotFan = _JnxMXTSR80SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 146, 5)
)
_JnxMXTSR80SlotFPM_ObjectIdentity = ObjectIdentity
jnxMXTSR80SlotFPM = _JnxMXTSR80SlotFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 146, 6)
)
_JnxSlotPTX10008_ObjectIdentity = ObjectIdentity
jnxSlotPTX10008 = _JnxSlotPTX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 147)
)
_JnxPTX10008SlotFPC_ObjectIdentity = ObjectIdentity
jnxPTX10008SlotFPC = _JnxPTX10008SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 147, 1)
)
_JnxPTX10008SlotHM_ObjectIdentity = ObjectIdentity
jnxPTX10008SlotHM = _JnxPTX10008SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 147, 2)
)
_JnxPTX10008SlotPower_ObjectIdentity = ObjectIdentity
jnxPTX10008SlotPower = _JnxPTX10008SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 147, 3)
)
_JnxPTX10008SlotFan_ObjectIdentity = ObjectIdentity
jnxPTX10008SlotFan = _JnxPTX10008SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 147, 4)
)
_JnxPTX10008SlotFPB_ObjectIdentity = ObjectIdentity
jnxPTX10008SlotFPB = _JnxPTX10008SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 147, 5)
)
_JnxPTX10008SlotCBD_ObjectIdentity = ObjectIdentity
jnxPTX10008SlotCBD = _JnxPTX10008SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 147, 6)
)
_JnxPTX10008SlotSIB_ObjectIdentity = ObjectIdentity
jnxPTX10008SlotSIB = _JnxPTX10008SlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 147, 7)
)
_JnxPTX10008SlotFPM_ObjectIdentity = ObjectIdentity
jnxPTX10008SlotFPM = _JnxPTX10008SlotFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 147, 8)
)
_JnxPTX10008SlotFTC_ObjectIdentity = ObjectIdentity
jnxPTX10008SlotFTC = _JnxPTX10008SlotFTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 147, 9)
)
_JnxPTX10008SlotBackplane_ObjectIdentity = ObjectIdentity
jnxPTX10008SlotBackplane = _JnxPTX10008SlotBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 147, 10)
)
_JnxSlotACX5448_ObjectIdentity = ObjectIdentity
jnxSlotACX5448 = _JnxSlotACX5448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 148)
)
_JnxACX5448SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX5448SlotFPC = _JnxACX5448SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 148, 1)
)
_JnxACX5448SlotFEB_ObjectIdentity = ObjectIdentity
jnxACX5448SlotFEB = _JnxACX5448SlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 148, 2)
)
_JnxACX5448SlotRE_ObjectIdentity = ObjectIdentity
jnxACX5448SlotRE = _JnxACX5448SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 148, 3)
)
_JnxACX5448SlotPower_ObjectIdentity = ObjectIdentity
jnxACX5448SlotPower = _JnxACX5448SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 148, 4)
)
_JnxACX5448SlotFan_ObjectIdentity = ObjectIdentity
jnxACX5448SlotFan = _JnxACX5448SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 148, 5)
)
_JnxSlotPTX10016_ObjectIdentity = ObjectIdentity
jnxSlotPTX10016 = _JnxSlotPTX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 150)
)
_JnxPTX10016SlotFPC_ObjectIdentity = ObjectIdentity
jnxPTX10016SlotFPC = _JnxPTX10016SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 150, 1)
)
_JnxPTX10016SlotHM_ObjectIdentity = ObjectIdentity
jnxPTX10016SlotHM = _JnxPTX10016SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 150, 2)
)
_JnxPTX10016SlotPower_ObjectIdentity = ObjectIdentity
jnxPTX10016SlotPower = _JnxPTX10016SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 150, 3)
)
_JnxPTX10016SlotFan_ObjectIdentity = ObjectIdentity
jnxPTX10016SlotFan = _JnxPTX10016SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 150, 4)
)
_JnxPTX10016SlotFPB_ObjectIdentity = ObjectIdentity
jnxPTX10016SlotFPB = _JnxPTX10016SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 150, 5)
)
_JnxPTX10016SlotCBD_ObjectIdentity = ObjectIdentity
jnxPTX10016SlotCBD = _JnxPTX10016SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 150, 6)
)
_JnxPTX10016SlotSIB_ObjectIdentity = ObjectIdentity
jnxPTX10016SlotSIB = _JnxPTX10016SlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 150, 7)
)
_JnxPTX10016SlotFTC_ObjectIdentity = ObjectIdentity
jnxPTX10016SlotFTC = _JnxPTX10016SlotFTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 150, 8)
)
_JnxPTX10016SlotBackplane_ObjectIdentity = ObjectIdentity
jnxPTX10016SlotBackplane = _JnxPTX10016SlotBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 150, 9)
)
_JnxSlotEX9251_ObjectIdentity = ObjectIdentity
jnxSlotEX9251 = _JnxSlotEX9251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 151)
)
_JnxEX9251SlotHM_ObjectIdentity = ObjectIdentity
jnxEX9251SlotHM = _JnxEX9251SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 151, 1)
)
_JnxEX9251SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX9251SlotFPC = _JnxEX9251SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 151, 2)
)
_JnxEX9251SlotFan_ObjectIdentity = ObjectIdentity
jnxEX9251SlotFan = _JnxEX9251SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 151, 3)
)
_JnxEX9251SlotCB_ObjectIdentity = ObjectIdentity
jnxEX9251SlotCB = _JnxEX9251SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 151, 4)
)
_JnxEX9251SlotPower_ObjectIdentity = ObjectIdentity
jnxEX9251SlotPower = _JnxEX9251SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 151, 5)
)
_JnxSlotMX150_ObjectIdentity = ObjectIdentity
jnxSlotMX150 = _JnxSlotMX150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 152)
)
_JnxMX150SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX150SlotFPC = _JnxMX150SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 152, 1)
)
_JnxMX150SlotPower_ObjectIdentity = ObjectIdentity
jnxMX150SlotPower = _JnxMX150SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 152, 2)
)
_JnxMX150SlotFan_ObjectIdentity = ObjectIdentity
jnxMX150SlotFan = _JnxMX150SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 152, 3)
)
_JnxMX150SlotCB_ObjectIdentity = ObjectIdentity
jnxMX150SlotCB = _JnxMX150SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 152, 4)
)
_JnxMX150SlotHM_ObjectIdentity = ObjectIdentity
jnxMX150SlotHM = _JnxMX150SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 152, 5)
)
_JnxSlotJNP10001_ObjectIdentity = ObjectIdentity
jnxSlotJNP10001 = _JnxSlotJNP10001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 153)
)
_JnxJNP10001SlotHM_ObjectIdentity = ObjectIdentity
jnxJNP10001SlotHM = _JnxJNP10001SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 153, 1)
)
_JnxJNP10001SlotFPC_ObjectIdentity = ObjectIdentity
jnxJNP10001SlotFPC = _JnxJNP10001SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 153, 2)
)
_JnxJNP10001SlotFan_ObjectIdentity = ObjectIdentity
jnxJNP10001SlotFan = _JnxJNP10001SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 153, 3)
)
_JnxJNP10001SlotPower_ObjectIdentity = ObjectIdentity
jnxJNP10001SlotPower = _JnxJNP10001SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 153, 4)
)
_JnxSlotMX10008_ObjectIdentity = ObjectIdentity
jnxSlotMX10008 = _JnxSlotMX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 154)
)
_JnxMX10008SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX10008SlotFPC = _JnxMX10008SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 154, 1)
)
_JnxMX10008SlotHM_ObjectIdentity = ObjectIdentity
jnxMX10008SlotHM = _JnxMX10008SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 154, 2)
)
_JnxMX10008SlotPower_ObjectIdentity = ObjectIdentity
jnxMX10008SlotPower = _JnxMX10008SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 154, 3)
)
_JnxMX10008SlotFan_ObjectIdentity = ObjectIdentity
jnxMX10008SlotFan = _JnxMX10008SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 154, 4)
)
_JnxMX10008SlotFPB_ObjectIdentity = ObjectIdentity
jnxMX10008SlotFPB = _JnxMX10008SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 154, 5)
)
_JnxMX10008SlotCBD_ObjectIdentity = ObjectIdentity
jnxMX10008SlotCBD = _JnxMX10008SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 154, 6)
)
_JnxMX10008SlotSFB_ObjectIdentity = ObjectIdentity
jnxMX10008SlotSFB = _JnxMX10008SlotSFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 154, 7)
)
_JnxMX10008SlotFTC_ObjectIdentity = ObjectIdentity
jnxMX10008SlotFTC = _JnxMX10008SlotFTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 154, 8)
)
_JnxSlotMX10016_ObjectIdentity = ObjectIdentity
jnxSlotMX10016 = _JnxSlotMX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 155)
)
_JnxMX10016SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX10016SlotFPC = _JnxMX10016SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 155, 1)
)
_JnxMX10016SlotHM_ObjectIdentity = ObjectIdentity
jnxMX10016SlotHM = _JnxMX10016SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 155, 2)
)
_JnxMX10016SlotPower_ObjectIdentity = ObjectIdentity
jnxMX10016SlotPower = _JnxMX10016SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 155, 3)
)
_JnxMX10016SlotFan_ObjectIdentity = ObjectIdentity
jnxMX10016SlotFan = _JnxMX10016SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 155, 4)
)
_JnxMX10016SlotFPB_ObjectIdentity = ObjectIdentity
jnxMX10016SlotFPB = _JnxMX10016SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 155, 5)
)
_JnxMX10016SlotCBD_ObjectIdentity = ObjectIdentity
jnxMX10016SlotCBD = _JnxMX10016SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 155, 6)
)
_JnxMX10016SlotSFB_ObjectIdentity = ObjectIdentity
jnxMX10016SlotSFB = _JnxMX10016SlotSFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 155, 7)
)
_JnxMX10016SlotFTC_ObjectIdentity = ObjectIdentity
jnxMX10016SlotFTC = _JnxMX10016SlotFTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 155, 8)
)
_JnxSlotEX9253_ObjectIdentity = ObjectIdentity
jnxSlotEX9253 = _JnxSlotEX9253_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 156)
)
_JnxEX9253SlotHM_ObjectIdentity = ObjectIdentity
jnxEX9253SlotHM = _JnxEX9253SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 156, 1)
)
_JnxEX9253SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX9253SlotFPC = _JnxEX9253SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 156, 2)
)
_JnxEX9253SlotFan_ObjectIdentity = ObjectIdentity
jnxEX9253SlotFan = _JnxEX9253SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 156, 3)
)
_JnxEX9253SlotCB_ObjectIdentity = ObjectIdentity
jnxEX9253SlotCB = _JnxEX9253SlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 156, 4)
)
_JnxEX9253SlotPower_ObjectIdentity = ObjectIdentity
jnxEX9253SlotPower = _JnxEX9253SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 156, 5)
)
_JnxSlotJRR200_ObjectIdentity = ObjectIdentity
jnxSlotJRR200 = _JnxSlotJRR200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 157)
)
_JnxJRR200SlotRE_ObjectIdentity = ObjectIdentity
jnxJRR200SlotRE = _JnxJRR200SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 157, 1)
)
_JnxJRR200SlotPower_ObjectIdentity = ObjectIdentity
jnxJRR200SlotPower = _JnxJRR200SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 157, 2)
)
_JnxJRR200SlotFan_ObjectIdentity = ObjectIdentity
jnxJRR200SlotFan = _JnxJRR200SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 157, 3)
)
_JnxSlotACX5448M_ObjectIdentity = ObjectIdentity
jnxSlotACX5448M = _JnxSlotACX5448M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 158)
)
_JnxACX5448MSlotFPC_ObjectIdentity = ObjectIdentity
jnxACX5448MSlotFPC = _JnxACX5448MSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 158, 1)
)
_JnxACX5448MSlotFEB_ObjectIdentity = ObjectIdentity
jnxACX5448MSlotFEB = _JnxACX5448MSlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 158, 2)
)
_JnxACX5448MSlotRE_ObjectIdentity = ObjectIdentity
jnxACX5448MSlotRE = _JnxACX5448MSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 158, 3)
)
_JnxACX5448MSlotPower_ObjectIdentity = ObjectIdentity
jnxACX5448MSlotPower = _JnxACX5448MSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 158, 4)
)
_JnxACX5448MSlotFan_ObjectIdentity = ObjectIdentity
jnxACX5448MSlotFan = _JnxACX5448MSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 158, 5)
)
_JnxSlotACX5448D_ObjectIdentity = ObjectIdentity
jnxSlotACX5448D = _JnxSlotACX5448D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 159)
)
_JnxACX5448DSlotFPC_ObjectIdentity = ObjectIdentity
jnxACX5448DSlotFPC = _JnxACX5448DSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 159, 1)
)
_JnxACX5448DSlotFEB_ObjectIdentity = ObjectIdentity
jnxACX5448DSlotFEB = _JnxACX5448DSlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 159, 2)
)
_JnxACX5448DSlotRE_ObjectIdentity = ObjectIdentity
jnxACX5448DSlotRE = _JnxACX5448DSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 159, 3)
)
_JnxACX5448DSlotPower_ObjectIdentity = ObjectIdentity
jnxACX5448DSlotPower = _JnxACX5448DSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 159, 4)
)
_JnxACX5448DSlotFan_ObjectIdentity = ObjectIdentity
jnxACX5448DSlotFan = _JnxACX5448DSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 159, 5)
)
_JnxSlotACX6360OR_ObjectIdentity = ObjectIdentity
jnxSlotACX6360OR = _JnxSlotACX6360OR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 160)
)
_JnxACX6360ORSlotHM_ObjectIdentity = ObjectIdentity
jnxACX6360ORSlotHM = _JnxACX6360ORSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 160, 1)
)
_JnxACX6360ORSlotFPC_ObjectIdentity = ObjectIdentity
jnxACX6360ORSlotFPC = _JnxACX6360ORSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 160, 2)
)
_JnxACX6360ORSlotFan_ObjectIdentity = ObjectIdentity
jnxACX6360ORSlotFan = _JnxACX6360ORSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 160, 3)
)
_JnxACX6360ORSlotPower_ObjectIdentity = ObjectIdentity
jnxACX6360ORSlotPower = _JnxACX6360ORSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 160, 4)
)
_JnxSlotACX6360OX_ObjectIdentity = ObjectIdentity
jnxSlotACX6360OX = _JnxSlotACX6360OX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 161)
)
_JnxACX6360OXSlotHM_ObjectIdentity = ObjectIdentity
jnxACX6360OXSlotHM = _JnxACX6360OXSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 161, 1)
)
_JnxACX6360OXSlotFPC_ObjectIdentity = ObjectIdentity
jnxACX6360OXSlotFPC = _JnxACX6360OXSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 161, 2)
)
_JnxACX6360OXSlotFan_ObjectIdentity = ObjectIdentity
jnxACX6360OXSlotFan = _JnxACX6360OXSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 161, 3)
)
_JnxACX6360OXSlotPower_ObjectIdentity = ObjectIdentity
jnxACX6360OXSlotPower = _JnxACX6360OXSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 161, 4)
)
_JnxSlotACX710_ObjectIdentity = ObjectIdentity
jnxSlotACX710 = _JnxSlotACX710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 162)
)
_JnxACX710SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX710SlotFPC = _JnxACX710SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 162, 1)
)
_JnxACX710SlotRE_ObjectIdentity = ObjectIdentity
jnxACX710SlotRE = _JnxACX710SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 162, 2)
)
_JnxACX710SlotPower_ObjectIdentity = ObjectIdentity
jnxACX710SlotPower = _JnxACX710SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 162, 3)
)
_JnxACX710SlotFan_ObjectIdentity = ObjectIdentity
jnxACX710SlotFan = _JnxACX710SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 162, 4)
)
_JnxSlotACX5800_ObjectIdentity = ObjectIdentity
jnxSlotACX5800 = _JnxSlotACX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 163)
)
_JnxACX5800SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX5800SlotFPC = _JnxACX5800SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 163, 1)
)
_JnxACX5800SlotFEB_ObjectIdentity = ObjectIdentity
jnxACX5800SlotFEB = _JnxACX5800SlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 163, 2)
)
_JnxACX5800SlotRE_ObjectIdentity = ObjectIdentity
jnxACX5800SlotRE = _JnxACX5800SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 163, 3)
)
_JnxACX5800SlotPower_ObjectIdentity = ObjectIdentity
jnxACX5800SlotPower = _JnxACX5800SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 163, 4)
)
_JnxSlotSRX380_ObjectIdentity = ObjectIdentity
jnxSlotSRX380 = _JnxSlotSRX380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 164)
)
_JnxSRX380SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX380SlotFPC = _JnxSRX380SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 164, 1)
)
_JnxSRX380SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX380SlotRE = _JnxSRX380SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 164, 2)
)
_JnxSRX380SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX380SlotPower = _JnxSRX380SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 164, 3)
)
_JnxSRX380SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX380SlotFan = _JnxSRX380SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 164, 4)
)
_JnxSlotEX4400_ObjectIdentity = ObjectIdentity
jnxSlotEX4400 = _JnxSlotEX4400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 165)
)
_JnxEX4400SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX4400SlotFPC = _JnxEX4400SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 165, 1)
)
_JnxEX4400SlotPower_ObjectIdentity = ObjectIdentity
jnxEX4400SlotPower = _JnxEX4400SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 165, 1, 1)
)
_JnxEX4400SlotFan_ObjectIdentity = ObjectIdentity
jnxEX4400SlotFan = _JnxEX4400SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 165, 1, 2)
)
_JnxSlotR6675_ObjectIdentity = ObjectIdentity
jnxSlotR6675 = _JnxSlotR6675_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 166)
)
_JnxR6675SlotFPC_ObjectIdentity = ObjectIdentity
jnxR6675SlotFPC = _JnxR6675SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 166, 1)
)
_JnxR6675SlotRE_ObjectIdentity = ObjectIdentity
jnxR6675SlotRE = _JnxR6675SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 166, 2)
)
_JnxR6675SlotPower_ObjectIdentity = ObjectIdentity
jnxR6675SlotPower = _JnxR6675SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 166, 3)
)
_JnxR6675SlotFan_ObjectIdentity = ObjectIdentity
jnxR6675SlotFan = _JnxR6675SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 166, 4)
)
_JnxSlotMX304_ObjectIdentity = ObjectIdentity
jnxSlotMX304 = _JnxSlotMX304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 167)
)
_JnxMX304SlotHM_ObjectIdentity = ObjectIdentity
jnxMX304SlotHM = _JnxMX304SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 167, 1)
)
_JnxMX304SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX304SlotFPC = _JnxMX304SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 167, 2)
)
_JnxMX304SlotFan_ObjectIdentity = ObjectIdentity
jnxMX304SlotFan = _JnxMX304SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 167, 3)
)
_JnxMX304SlotPower_ObjectIdentity = ObjectIdentity
jnxMX304SlotPower = _JnxMX304SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 167, 4)
)
_JnxMX304SlotPMB_ObjectIdentity = ObjectIdentity
jnxMX304SlotPMB = _JnxMX304SlotPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 167, 5)
)
_JnxMX304SlotSFB_ObjectIdentity = ObjectIdentity
jnxMX304SlotSFB = _JnxMX304SlotSFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 167, 6)
)
_JnxMX304SlotTIB_ObjectIdentity = ObjectIdentity
jnxMX304SlotTIB = _JnxMX304SlotTIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 167, 7)
)
_JnxMX304SlotCBD_ObjectIdentity = ObjectIdentity
jnxMX304SlotCBD = _JnxMX304SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 167, 8)
)
_JnxSlotMX10004_ObjectIdentity = ObjectIdentity
jnxSlotMX10004 = _JnxSlotMX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 168)
)
_JnxMX10004SlotFPC_ObjectIdentity = ObjectIdentity
jnxMX10004SlotFPC = _JnxMX10004SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 168, 1)
)
_JnxMX10004SlotHM_ObjectIdentity = ObjectIdentity
jnxMX10004SlotHM = _JnxMX10004SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 168, 2)
)
_JnxMX10004SlotPower_ObjectIdentity = ObjectIdentity
jnxMX10004SlotPower = _JnxMX10004SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 168, 3)
)
_JnxMX10004SlotFan_ObjectIdentity = ObjectIdentity
jnxMX10004SlotFan = _JnxMX10004SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 168, 4)
)
_JnxMX10004SlotFPB_ObjectIdentity = ObjectIdentity
jnxMX10004SlotFPB = _JnxMX10004SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 168, 5)
)
_JnxMX10004SlotCBD_ObjectIdentity = ObjectIdentity
jnxMX10004SlotCBD = _JnxMX10004SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 168, 6)
)
_JnxMX10004SlotSFB_ObjectIdentity = ObjectIdentity
jnxMX10004SlotSFB = _JnxMX10004SlotSFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 168, 7)
)
_JnxMX10004SlotFTC_ObjectIdentity = ObjectIdentity
jnxMX10004SlotFTC = _JnxMX10004SlotFTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 168, 8)
)
_JnxSlotEX4100_ObjectIdentity = ObjectIdentity
jnxSlotEX4100 = _JnxSlotEX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 169)
)
_JnxEX4100SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX4100SlotFPC = _JnxEX4100SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 169, 1)
)
_JnxEX4100SlotPower_ObjectIdentity = ObjectIdentity
jnxEX4100SlotPower = _JnxEX4100SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 169, 1, 1)
)
_JnxEX4100SlotFan_ObjectIdentity = ObjectIdentity
jnxEX4100SlotFan = _JnxEX4100SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 169, 1, 2)
)
_JnxSlotEX4650_ObjectIdentity = ObjectIdentity
jnxSlotEX4650 = _JnxSlotEX4650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 508)
)
_JnxEX4650SlotFPC_ObjectIdentity = ObjectIdentity
jnxEX4650SlotFPC = _JnxEX4650SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 508, 1)
)
_JnxEX4650SlotHM_ObjectIdentity = ObjectIdentity
jnxEX4650SlotHM = _JnxEX4650SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 508, 2)
)
_JnxEX4650SlotPower_ObjectIdentity = ObjectIdentity
jnxEX4650SlotPower = _JnxEX4650SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 508, 3)
)
_JnxEX4650SlotFan_ObjectIdentity = ObjectIdentity
jnxEX4650SlotFan = _JnxEX4650SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 508, 4)
)
_JnxEX4650SlotRE_ObjectIdentity = ObjectIdentity
jnxEX4650SlotRE = _JnxEX4650SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 508, 5)
)
_JnxSlotPTX1000260C_ObjectIdentity = ObjectIdentity
jnxSlotPTX1000260C = _JnxSlotPTX1000260C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 513)
)
_JnxPTX1000260CSlotFPC_ObjectIdentity = ObjectIdentity
jnxPTX1000260CSlotFPC = _JnxPTX1000260CSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 513, 1)
)
_JnxPTX1000260CSlotHM_ObjectIdentity = ObjectIdentity
jnxPTX1000260CSlotHM = _JnxPTX1000260CSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 513, 2)
)
_JnxPTX1000260CSlotPower_ObjectIdentity = ObjectIdentity
jnxPTX1000260CSlotPower = _JnxPTX1000260CSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 513, 3)
)
_JnxPTX1000260CSlotFan_ObjectIdentity = ObjectIdentity
jnxPTX1000260CSlotFan = _JnxPTX1000260CSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 513, 4)
)
_JnxPTX1000260CSlotFPB_ObjectIdentity = ObjectIdentity
jnxPTX1000260CSlotFPB = _JnxPTX1000260CSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 513, 5)
)
_JnxSlotPTX1000380c_ObjectIdentity = ObjectIdentity
jnxSlotPTX1000380c = _JnxSlotPTX1000380c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 523)
)
_JnxPTX1000380cSlotRE_ObjectIdentity = ObjectIdentity
jnxPTX1000380cSlotRE = _JnxPTX1000380cSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 523, 1)
)
_JnxPTX1000380cSlotCB_ObjectIdentity = ObjectIdentity
jnxPTX1000380cSlotCB = _JnxPTX1000380cSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 523, 2)
)
_JnxPTX1000380cSlotFPC_ObjectIdentity = ObjectIdentity
jnxPTX1000380cSlotFPC = _JnxPTX1000380cSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 523, 3)
)
_JnxPTX1000380cSlotFan_ObjectIdentity = ObjectIdentity
jnxPTX1000380cSlotFan = _JnxPTX1000380cSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 523, 4)
)
_JnxPTX1000380cSlotFPM_ObjectIdentity = ObjectIdentity
jnxPTX1000380cSlotFPM = _JnxPTX1000380cSlotFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 523, 5)
)
_JnxPTX1000380cSlotSIB_ObjectIdentity = ObjectIdentity
jnxPTX1000380cSlotSIB = _JnxPTX1000380cSlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 523, 6)
)
_JnxPTX1000380cSlotPIC_ObjectIdentity = ObjectIdentity
jnxPTX1000380cSlotPIC = _JnxPTX1000380cSlotPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 523, 7)
)
_JnxPTX1000380cSlotPDU_ObjectIdentity = ObjectIdentity
jnxPTX1000380cSlotPDU = _JnxPTX1000380cSlotPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 523, 8)
)
_JnxPTX1000380cSlotPSM_ObjectIdentity = ObjectIdentity
jnxPTX1000380cSlotPSM = _JnxPTX1000380cSlotPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 523, 9)
)
_JnxSlotPTX10003160c_ObjectIdentity = ObjectIdentity
jnxSlotPTX10003160c = _JnxSlotPTX10003160c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 524)
)
_JnxPTX10003160cSlotRE_ObjectIdentity = ObjectIdentity
jnxPTX10003160cSlotRE = _JnxPTX10003160cSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 524, 1)
)
_JnxPTX10003160cSlotCB_ObjectIdentity = ObjectIdentity
jnxPTX10003160cSlotCB = _JnxPTX10003160cSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 524, 2)
)
_JnxPTX10003160cSlotFPC_ObjectIdentity = ObjectIdentity
jnxPTX10003160cSlotFPC = _JnxPTX10003160cSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 524, 3)
)
_JnxPTX10003160cSlotFan_ObjectIdentity = ObjectIdentity
jnxPTX10003160cSlotFan = _JnxPTX10003160cSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 524, 4)
)
_JnxPTX10003160cSlotFPM_ObjectIdentity = ObjectIdentity
jnxPTX10003160cSlotFPM = _JnxPTX10003160cSlotFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 524, 5)
)
_JnxPTX10003160cSlotSIB_ObjectIdentity = ObjectIdentity
jnxPTX10003160cSlotSIB = _JnxPTX10003160cSlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 524, 6)
)
_JnxPTX10003160cSlotPIC_ObjectIdentity = ObjectIdentity
jnxPTX10003160cSlotPIC = _JnxPTX10003160cSlotPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 524, 7)
)
_JnxPTX10003160cSlotPDU_ObjectIdentity = ObjectIdentity
jnxPTX10003160cSlotPDU = _JnxPTX10003160cSlotPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 524, 8)
)
_JnxPTX10003160cSlotPSM_ObjectIdentity = ObjectIdentity
jnxPTX10003160cSlotPSM = _JnxPTX10003160cSlotPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 524, 9)
)
_JnxSlotQFX1000380c_ObjectIdentity = ObjectIdentity
jnxSlotQFX1000380c = _JnxSlotQFX1000380c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 525)
)
_JnxQFX1000380cSlotRE_ObjectIdentity = ObjectIdentity
jnxQFX1000380cSlotRE = _JnxQFX1000380cSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 525, 1)
)
_JnxQFX1000380cSlotCB_ObjectIdentity = ObjectIdentity
jnxQFX1000380cSlotCB = _JnxQFX1000380cSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 525, 2)
)
_JnxQFX1000380cSlotFPC_ObjectIdentity = ObjectIdentity
jnxQFX1000380cSlotFPC = _JnxQFX1000380cSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 525, 3)
)
_JnxQFX1000380cSlotFan_ObjectIdentity = ObjectIdentity
jnxQFX1000380cSlotFan = _JnxQFX1000380cSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 525, 4)
)
_JnxQFX1000380cSlotFPM_ObjectIdentity = ObjectIdentity
jnxQFX1000380cSlotFPM = _JnxQFX1000380cSlotFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 525, 5)
)
_JnxQFX1000380cSlotSIB_ObjectIdentity = ObjectIdentity
jnxQFX1000380cSlotSIB = _JnxQFX1000380cSlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 525, 6)
)
_JnxQFX1000380cSlotPIC_ObjectIdentity = ObjectIdentity
jnxQFX1000380cSlotPIC = _JnxQFX1000380cSlotPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 525, 7)
)
_JnxQFX1000380cSlotPDU_ObjectIdentity = ObjectIdentity
jnxQFX1000380cSlotPDU = _JnxQFX1000380cSlotPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 525, 8)
)
_JnxQFX1000380cSlotPSM_ObjectIdentity = ObjectIdentity
jnxQFX1000380cSlotPSM = _JnxQFX1000380cSlotPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 525, 9)
)
_JnxSlotQFX10003160c_ObjectIdentity = ObjectIdentity
jnxSlotQFX10003160c = _JnxSlotQFX10003160c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 526)
)
_JnxQFX10003160cSlotRE_ObjectIdentity = ObjectIdentity
jnxQFX10003160cSlotRE = _JnxQFX10003160cSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 526, 1)
)
_JnxQFX10003160cSlotCB_ObjectIdentity = ObjectIdentity
jnxQFX10003160cSlotCB = _JnxQFX10003160cSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 526, 2)
)
_JnxQFX10003160cSlotFPC_ObjectIdentity = ObjectIdentity
jnxQFX10003160cSlotFPC = _JnxQFX10003160cSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 526, 3)
)
_JnxQFX10003160cSlotFan_ObjectIdentity = ObjectIdentity
jnxQFX10003160cSlotFan = _JnxQFX10003160cSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 526, 4)
)
_JnxQFX10003160cSlotFPM_ObjectIdentity = ObjectIdentity
jnxQFX10003160cSlotFPM = _JnxQFX10003160cSlotFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 526, 5)
)
_JnxQFX10003160cSlotSIB_ObjectIdentity = ObjectIdentity
jnxQFX10003160cSlotSIB = _JnxQFX10003160cSlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 526, 6)
)
_JnxQFX10003160cSlotPIC_ObjectIdentity = ObjectIdentity
jnxQFX10003160cSlotPIC = _JnxQFX10003160cSlotPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 526, 7)
)
_JnxQFX10003160cSlotPDU_ObjectIdentity = ObjectIdentity
jnxQFX10003160cSlotPDU = _JnxQFX10003160cSlotPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 526, 8)
)
_JnxQFX10003160cSlotPSM_ObjectIdentity = ObjectIdentity
jnxQFX10003160cSlotPSM = _JnxQFX10003160cSlotPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 526, 9)
)
_JnxSlotPTX1000136mr_ObjectIdentity = ObjectIdentity
jnxSlotPTX1000136mr = _JnxSlotPTX1000136mr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 555)
)
_JnxPTX1000136mrSlotRE_ObjectIdentity = ObjectIdentity
jnxPTX1000136mrSlotRE = _JnxPTX1000136mrSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 555, 1)
)
_JnxPTX1000136mrSlotCB_ObjectIdentity = ObjectIdentity
jnxPTX1000136mrSlotCB = _JnxPTX1000136mrSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 555, 2)
)
_JnxPTX1000136mrSlotFPC_ObjectIdentity = ObjectIdentity
jnxPTX1000136mrSlotFPC = _JnxPTX1000136mrSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 555, 3)
)
_JnxPTX1000136mrSlotFan_ObjectIdentity = ObjectIdentity
jnxPTX1000136mrSlotFan = _JnxPTX1000136mrSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 555, 4)
)
_JnxPTX1000136mrSlotSIB_ObjectIdentity = ObjectIdentity
jnxPTX1000136mrSlotSIB = _JnxPTX1000136mrSlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 555, 5)
)
_JnxPTX1000136mrSlotPIC_ObjectIdentity = ObjectIdentity
jnxPTX1000136mrSlotPIC = _JnxPTX1000136mrSlotPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 555, 6)
)
_JnxPTX1000136mrSlotPSM_ObjectIdentity = ObjectIdentity
jnxPTX1000136mrSlotPSM = _JnxPTX1000136mrSlotPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 555, 7)
)
_JnxSlotPTX10004_ObjectIdentity = ObjectIdentity
jnxSlotPTX10004 = _JnxSlotPTX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 570)
)
_JnxPTX10004SlotFPC_ObjectIdentity = ObjectIdentity
jnxPTX10004SlotFPC = _JnxPTX10004SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 570, 1)
)
_JnxPTX10004SlotHM_ObjectIdentity = ObjectIdentity
jnxPTX10004SlotHM = _JnxPTX10004SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 570, 2)
)
_JnxPTX10004SlotPower_ObjectIdentity = ObjectIdentity
jnxPTX10004SlotPower = _JnxPTX10004SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 570, 3)
)
_JnxPTX10004SlotFan_ObjectIdentity = ObjectIdentity
jnxPTX10004SlotFan = _JnxPTX10004SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 570, 4)
)
_JnxPTX10004SlotFPB_ObjectIdentity = ObjectIdentity
jnxPTX10004SlotFPB = _JnxPTX10004SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 570, 5)
)
_JnxPTX10004SlotCBD_ObjectIdentity = ObjectIdentity
jnxPTX10004SlotCBD = _JnxPTX10004SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 570, 6)
)
_JnxPTX10004SlotSIB_ObjectIdentity = ObjectIdentity
jnxPTX10004SlotSIB = _JnxPTX10004SlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 570, 7)
)
_JnxPTX10004SlotFPM_ObjectIdentity = ObjectIdentity
jnxPTX10004SlotFPM = _JnxPTX10004SlotFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 570, 8)
)
_JnxPTX10004SlotFTC_ObjectIdentity = ObjectIdentity
jnxPTX10004SlotFTC = _JnxPTX10004SlotFTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 570, 9)
)
_JnxPTX10004SlotBackplane_ObjectIdentity = ObjectIdentity
jnxPTX10004SlotBackplane = _JnxPTX10004SlotBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 570, 10)
)
_JnxSlotACX753_ObjectIdentity = ObjectIdentity
jnxSlotACX753 = _JnxSlotACX753_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 576)
)
_JnxACX753SlotRE_ObjectIdentity = ObjectIdentity
jnxACX753SlotRE = _JnxACX753SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 576, 1)
)
_JnxACX753SlotPSM_ObjectIdentity = ObjectIdentity
jnxACX753SlotPSM = _JnxACX753SlotPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 576, 2)
)
_JnxACX753SlotFan_ObjectIdentity = ObjectIdentity
jnxACX753SlotFan = _JnxACX753SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 576, 3)
)
_JnxACX753SlotCBD_ObjectIdentity = ObjectIdentity
jnxACX753SlotCBD = _JnxACX753SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 576, 4)
)
_JnxACX753SlotBackplane_ObjectIdentity = ObjectIdentity
jnxACX753SlotBackplane = _JnxACX753SlotBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 576, 5)
)
_JnxACX753SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX753SlotFPC = _JnxACX753SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 576, 6)
)
_JnxACX753SlotPIC_ObjectIdentity = ObjectIdentity
jnxACX753SlotPIC = _JnxACX753SlotPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 576, 7)
)
_JnxACX753SlotFEB_ObjectIdentity = ObjectIdentity
jnxACX753SlotFEB = _JnxACX753SlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 576, 8)
)
_JnxSlotSRX1800_ObjectIdentity = ObjectIdentity
jnxSlotSRX1800 = _JnxSlotSRX1800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 577)
)
_JnxSRX1800SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX1800SlotFPC = _JnxSRX1800SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 577, 1)
)
_JnxSRX1800SlotPIC_ObjectIdentity = ObjectIdentity
jnxSRX1800SlotPIC = _JnxSRX1800SlotPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 577, 2)
)
_JnxSRX1800SlotHM_ObjectIdentity = ObjectIdentity
jnxSRX1800SlotHM = _JnxSRX1800SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 577, 3)
)
_JnxSRX1800SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX1800SlotPower = _JnxSRX1800SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 577, 4)
)
_JnxSRX1800SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX1800SlotFan = _JnxSRX1800SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 577, 5)
)
_JnxSlotACX7KSwitch_ObjectIdentity = ObjectIdentity
jnxSlotACX7KSwitch = _JnxSlotACX7KSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 578)
)
_JnxACX7KSwitchSlotFPC_ObjectIdentity = ObjectIdentity
jnxACX7KSwitchSlotFPC = _JnxACX7KSwitchSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 578, 1)
)
_JnxACX7KSwitchSlotHM_ObjectIdentity = ObjectIdentity
jnxACX7KSwitchSlotHM = _JnxACX7KSwitchSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 578, 2)
)
_JnxACX7KSwitchSlotPower_ObjectIdentity = ObjectIdentity
jnxACX7KSwitchSlotPower = _JnxACX7KSwitchSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 578, 3)
)
_JnxACX7KSwitchSlotFan_ObjectIdentity = ObjectIdentity
jnxACX7KSwitchSlotFan = _JnxACX7KSwitchSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 578, 4)
)
_JnxACX7KSwitchSlotFPB_ObjectIdentity = ObjectIdentity
jnxACX7KSwitchSlotFPB = _JnxACX7KSwitchSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 578, 5)
)
_JnxACX7KSwitchSlotCBD_ObjectIdentity = ObjectIdentity
jnxACX7KSwitchSlotCBD = _JnxACX7KSwitchSlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 578, 6)
)
_JnxACX7KSwitchSlotSIB_ObjectIdentity = ObjectIdentity
jnxACX7KSwitchSlotSIB = _JnxACX7KSwitchSlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 578, 7)
)
_JnxACX7KSwitchSlotFEB_ObjectIdentity = ObjectIdentity
jnxACX7KSwitchSlotFEB = _JnxACX7KSwitchSlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 578, 8)
)
_JnxSlotACX710032c_ObjectIdentity = ObjectIdentity
jnxSlotACX710032c = _JnxSlotACX710032c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 579)
)
_JnxACX710032cSlotFPC_ObjectIdentity = ObjectIdentity
jnxACX710032cSlotFPC = _JnxACX710032cSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 579, 1)
)
_JnxACX710032cSlotHM_ObjectIdentity = ObjectIdentity
jnxACX710032cSlotHM = _JnxACX710032cSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 579, 2)
)
_JnxACX710032cSlotPower_ObjectIdentity = ObjectIdentity
jnxACX710032cSlotPower = _JnxACX710032cSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 579, 3)
)
_JnxACX710032cSlotFan_ObjectIdentity = ObjectIdentity
jnxACX710032cSlotFan = _JnxACX710032cSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 579, 4)
)
_JnxACX710032cSlotFPB_ObjectIdentity = ObjectIdentity
jnxACX710032cSlotFPB = _JnxACX710032cSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 579, 5)
)
_JnxACX710032cSlotCBD_ObjectIdentity = ObjectIdentity
jnxACX710032cSlotCBD = _JnxACX710032cSlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 579, 6)
)
_JnxACX710032cSlotSIB_ObjectIdentity = ObjectIdentity
jnxACX710032cSlotSIB = _JnxACX710032cSlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 579, 7)
)
_JnxACX710032cSlotFEB_ObjectIdentity = ObjectIdentity
jnxACX710032cSlotFEB = _JnxACX710032cSlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 579, 8)
)
_JnxSlotACX710048l_ObjectIdentity = ObjectIdentity
jnxSlotACX710048l = _JnxSlotACX710048l_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 580)
)
_JnxACX710048lSlotFPC_ObjectIdentity = ObjectIdentity
jnxACX710048lSlotFPC = _JnxACX710048lSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 580, 1)
)
_JnxACX710048lSlotHM_ObjectIdentity = ObjectIdentity
jnxACX710048lSlotHM = _JnxACX710048lSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 580, 2)
)
_JnxACX710048lSlotPower_ObjectIdentity = ObjectIdentity
jnxACX710048lSlotPower = _JnxACX710048lSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 580, 3)
)
_JnxACX710048lSlotFan_ObjectIdentity = ObjectIdentity
jnxACX710048lSlotFan = _JnxACX710048lSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 580, 4)
)
_JnxACX710048lSlotFPB_ObjectIdentity = ObjectIdentity
jnxACX710048lSlotFPB = _JnxACX710048lSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 580, 5)
)
_JnxACX710048lSlotCBD_ObjectIdentity = ObjectIdentity
jnxACX710048lSlotCBD = _JnxACX710048lSlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 580, 6)
)
_JnxACX710048lSlotSIB_ObjectIdentity = ObjectIdentity
jnxACX710048lSlotSIB = _JnxACX710048lSlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 580, 7)
)
_JnxACX710048lSlotFEB_ObjectIdentity = ObjectIdentity
jnxACX710048lSlotFEB = _JnxACX710048lSlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 580, 8)
)
_JnxSlotACX7908_ObjectIdentity = ObjectIdentity
jnxSlotACX7908 = _JnxSlotACX7908_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 581)
)
_JnxACX7908SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX7908SlotFPC = _JnxACX7908SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 581, 1)
)
_JnxACX7908SlotHM_ObjectIdentity = ObjectIdentity
jnxACX7908SlotHM = _JnxACX7908SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 581, 2)
)
_JnxACX7908SlotPower_ObjectIdentity = ObjectIdentity
jnxACX7908SlotPower = _JnxACX7908SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 581, 3)
)
_JnxACX7908SlotFan_ObjectIdentity = ObjectIdentity
jnxACX7908SlotFan = _JnxACX7908SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 581, 4)
)
_JnxACX7908SlotCBD_ObjectIdentity = ObjectIdentity
jnxACX7908SlotCBD = _JnxACX7908SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 581, 5)
)
_JnxACX7908SlotSIB_ObjectIdentity = ObjectIdentity
jnxACX7908SlotSIB = _JnxACX7908SlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 581, 6)
)
_JnxACX7908SlotFPM_ObjectIdentity = ObjectIdentity
jnxACX7908SlotFPM = _JnxACX7908SlotFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 581, 7)
)
_JnxACX7908SlotBackplane_ObjectIdentity = ObjectIdentity
jnxACX7908SlotBackplane = _JnxACX7908SlotBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 581, 8)
)
_JnxSlotACX7024_ObjectIdentity = ObjectIdentity
jnxSlotACX7024 = _JnxSlotACX7024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 582)
)
_JnxACX7024SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX7024SlotFPC = _JnxACX7024SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 582, 1)
)
_JnxACX7024SlotHM_ObjectIdentity = ObjectIdentity
jnxACX7024SlotHM = _JnxACX7024SlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 582, 2)
)
_JnxACX7024SlotPower_ObjectIdentity = ObjectIdentity
jnxACX7024SlotPower = _JnxACX7024SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 582, 3)
)
_JnxACX7024SlotFan_ObjectIdentity = ObjectIdentity
jnxACX7024SlotFan = _JnxACX7024SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 582, 4)
)
_JnxACX7024SlotFPB_ObjectIdentity = ObjectIdentity
jnxACX7024SlotFPB = _JnxACX7024SlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 582, 5)
)
_JnxACX7024SlotCBD_ObjectIdentity = ObjectIdentity
jnxACX7024SlotCBD = _JnxACX7024SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 582, 6)
)
_JnxACX7024SlotSIB_ObjectIdentity = ObjectIdentity
jnxACX7024SlotSIB = _JnxACX7024SlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 582, 7)
)
_JnxACX7024SlotFEB_ObjectIdentity = ObjectIdentity
jnxACX7024SlotFEB = _JnxACX7024SlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 582, 8)
)
_JnxSlotSRX1600_ObjectIdentity = ObjectIdentity
jnxSlotSRX1600 = _JnxSlotSRX1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 583)
)
_JnxSRX1600SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX1600SlotFPC = _JnxSRX1600SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 583, 1)
)
_JnxSRX1600SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX1600SlotRE = _JnxSRX1600SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 583, 2)
)
_JnxSRX1600SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX1600SlotPower = _JnxSRX1600SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 583, 3)
)
_JnxSRX1600SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX1600SlotFan = _JnxSRX1600SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 583, 4)
)
_JnxSRX1600SlotCBD_ObjectIdentity = ObjectIdentity
jnxSRX1600SlotCBD = _JnxSRX1600SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 583, 5)
)
_JnxSlotSRX2300_ObjectIdentity = ObjectIdentity
jnxSlotSRX2300 = _JnxSlotSRX2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 584)
)
_JnxSRX2300SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX2300SlotFPC = _JnxSRX2300SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 584, 1)
)
_JnxSRX2300SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX2300SlotRE = _JnxSRX2300SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 584, 2)
)
_JnxSRX2300SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX2300SlotPower = _JnxSRX2300SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 584, 3)
)
_JnxSRX2300SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX2300SlotFan = _JnxSRX2300SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 584, 4)
)
_JnxSRX2300SlotCBD_ObjectIdentity = ObjectIdentity
jnxSRX2300SlotCBD = _JnxSRX2300SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 584, 5)
)
_JnxSlotSRX4300_ObjectIdentity = ObjectIdentity
jnxSlotSRX4300 = _JnxSlotSRX4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 585)
)
_JnxSRX4300SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX4300SlotFPC = _JnxSRX4300SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 585, 1)
)
_JnxSRX4300SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX4300SlotRE = _JnxSRX4300SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 585, 2)
)
_JnxSRX4300SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX4300SlotPower = _JnxSRX4300SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 585, 3)
)
_JnxSRX4300SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX4300SlotFan = _JnxSRX4300SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 585, 4)
)
_JnxSRX4300SlotCBD_ObjectIdentity = ObjectIdentity
jnxSRX4300SlotCBD = _JnxSRX4300SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 585, 5)
)
_JnxSlotACX7332_ObjectIdentity = ObjectIdentity
jnxSlotACX7332 = _JnxSlotACX7332_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 586)
)
_JnxACX7332SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX7332SlotFPC = _JnxACX7332SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 586, 1)
)
_JnxACX7332SlotRE_ObjectIdentity = ObjectIdentity
jnxACX7332SlotRE = _JnxACX7332SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 586, 2)
)
_JnxACX7332SlotPower_ObjectIdentity = ObjectIdentity
jnxACX7332SlotPower = _JnxACX7332SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 586, 3)
)
_JnxACX7332SlotFan_ObjectIdentity = ObjectIdentity
jnxACX7332SlotFan = _JnxACX7332SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 586, 4)
)
_JnxACX7332SlotFEB_ObjectIdentity = ObjectIdentity
jnxACX7332SlotFEB = _JnxACX7332SlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 586, 5)
)
_JnxACX7332SlotCBD_ObjectIdentity = ObjectIdentity
jnxACX7332SlotCBD = _JnxACX7332SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 586, 6)
)
_JnxSlotACX7348_ObjectIdentity = ObjectIdentity
jnxSlotACX7348 = _JnxSlotACX7348_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 587)
)
_JnxACX7348SlotFPC_ObjectIdentity = ObjectIdentity
jnxACX7348SlotFPC = _JnxACX7348SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 587, 1)
)
_JnxACX7348SlotRE_ObjectIdentity = ObjectIdentity
jnxACX7348SlotRE = _JnxACX7348SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 587, 2)
)
_JnxACX7348SlotPower_ObjectIdentity = ObjectIdentity
jnxACX7348SlotPower = _JnxACX7348SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 587, 3)
)
_JnxACX7348SlotFan_ObjectIdentity = ObjectIdentity
jnxACX7348SlotFan = _JnxACX7348SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 587, 4)
)
_JnxACX7348SlotFEB_ObjectIdentity = ObjectIdentity
jnxACX7348SlotFEB = _JnxACX7348SlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 587, 5)
)
_JnxACX7348SlotCBD_ObjectIdentity = ObjectIdentity
jnxACX7348SlotCBD = _JnxACX7348SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 587, 6)
)
_JnxSlotACX7024X_ObjectIdentity = ObjectIdentity
jnxSlotACX7024X = _JnxSlotACX7024X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 588)
)
_JnxACX7024XSlotFPC_ObjectIdentity = ObjectIdentity
jnxACX7024XSlotFPC = _JnxACX7024XSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 588, 1)
)
_JnxACX7024XSlotHM_ObjectIdentity = ObjectIdentity
jnxACX7024XSlotHM = _JnxACX7024XSlotHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 588, 2)
)
_JnxACX7024XSlotPower_ObjectIdentity = ObjectIdentity
jnxACX7024XSlotPower = _JnxACX7024XSlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 588, 3)
)
_JnxACX7024XSlotFan_ObjectIdentity = ObjectIdentity
jnxACX7024XSlotFan = _JnxACX7024XSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 588, 4)
)
_JnxACX7024XSlotFPB_ObjectIdentity = ObjectIdentity
jnxACX7024XSlotFPB = _JnxACX7024XSlotFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 588, 5)
)
_JnxACX7024XSlotCBD_ObjectIdentity = ObjectIdentity
jnxACX7024XSlotCBD = _JnxACX7024XSlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 588, 6)
)
_JnxACX7024XSlotSIB_ObjectIdentity = ObjectIdentity
jnxACX7024XSlotSIB = _JnxACX7024XSlotSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 588, 7)
)
_JnxACX7024XSlotFEB_ObjectIdentity = ObjectIdentity
jnxACX7024XSlotFEB = _JnxACX7024XSlotFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 588, 8)
)
_JnxSlotPTX1000236qdd_ObjectIdentity = ObjectIdentity
jnxSlotPTX1000236qdd = _JnxSlotPTX1000236qdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 589)
)
_JnxPTX1000236qddSlotRE_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddSlotRE = _JnxPTX1000236qddSlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 589, 1)
)
_JnxPTX1000236qddSlotCB_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddSlotCB = _JnxPTX1000236qddSlotCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 589, 2)
)
_JnxPTX1000236qddSlotFPC_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddSlotFPC = _JnxPTX1000236qddSlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 589, 3)
)
_JnxPTX1000236qddSlotFan_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddSlotFan = _JnxPTX1000236qddSlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 589, 4)
)
_JnxPTX1000236qddSlotPIC_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddSlotPIC = _JnxPTX1000236qddSlotPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 589, 5)
)
_JnxPTX1000236qddSlotPSM_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddSlotPSM = _JnxPTX1000236qddSlotPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 589, 6)
)
_JnxPTX1000236qddSlotBackplane_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddSlotBackplane = _JnxPTX1000236qddSlotBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 589, 7)
)
_JnxPTX1000236qddSlotFPM_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddSlotFPM = _JnxPTX1000236qddSlotFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 589, 8)
)
_JnxSlotSRX4700_ObjectIdentity = ObjectIdentity
jnxSlotSRX4700 = _JnxSlotSRX4700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 590)
)
_JnxSRX4700SlotFPC_ObjectIdentity = ObjectIdentity
jnxSRX4700SlotFPC = _JnxSRX4700SlotFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 590, 1)
)
_JnxSRX4700SlotRE_ObjectIdentity = ObjectIdentity
jnxSRX4700SlotRE = _JnxSRX4700SlotRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 590, 2)
)
_JnxSRX4700SlotPower_ObjectIdentity = ObjectIdentity
jnxSRX4700SlotPower = _JnxSRX4700SlotPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 590, 3)
)
_JnxSRX4700SlotFan_ObjectIdentity = ObjectIdentity
jnxSRX4700SlotFan = _JnxSRX4700SlotFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 590, 4)
)
_JnxSRX4700SlotCBD_ObjectIdentity = ObjectIdentity
jnxSRX4700SlotCBD = _JnxSRX4700SlotCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 2, 590, 5)
)
_JnxMediaCardSpace_ObjectIdentity = ObjectIdentity
jnxMediaCardSpace = _JnxMediaCardSpace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3)
)
_JnxMediaCardSpaceM40_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceM40 = _JnxMediaCardSpaceM40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 1)
)
_JnxMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMediaCardSpacePIC = _JnxMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 1, 1)
)
_JnxMediaCardSpaceM20_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceM20 = _JnxMediaCardSpaceM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 2)
)
_JnxM20MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxM20MediaCardSpacePIC = _JnxM20MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 2, 1)
)
_JnxMediaCardSpaceM160_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceM160 = _JnxMediaCardSpaceM160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 3)
)
_JnxM160MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxM160MediaCardSpacePIC = _JnxM160MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 3, 1)
)
_JnxMediaCardSpaceM10_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceM10 = _JnxMediaCardSpaceM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 4)
)
_JnxM10MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxM10MediaCardSpacePIC = _JnxM10MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 4, 1)
)
_JnxMediaCardSpaceM5_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceM5 = _JnxMediaCardSpaceM5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 5)
)
_JnxM5MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxM5MediaCardSpacePIC = _JnxM5MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 5, 1)
)
_JnxMediaCardSpaceT640_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceT640 = _JnxMediaCardSpaceT640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 6)
)
_JnxT640MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxT640MediaCardSpacePIC = _JnxT640MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 6, 1)
)
_JnxMediaCardSpaceT320_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceT320 = _JnxMediaCardSpaceT320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 7)
)
_JnxT320MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxT320MediaCardSpacePIC = _JnxT320MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 7, 1)
)
_JnxMediaCardSpaceM40e_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceM40e = _JnxMediaCardSpaceM40e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 8)
)
_JnxM40eMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxM40eMediaCardSpacePIC = _JnxM40eMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 8, 1)
)
_JnxMediaCardSpaceM320_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceM320 = _JnxMediaCardSpaceM320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 9)
)
_JnxM320MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxM320MediaCardSpacePIC = _JnxM320MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 9, 1)
)
_JnxM320MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxM320MediaCardSpaceMIC = _JnxM320MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 9, 2)
)
_JnxMediaCardSpaceM7i_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceM7i = _JnxMediaCardSpaceM7i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 10)
)
_JnxM7iMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxM7iMediaCardSpacePIC = _JnxM7iMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 10, 1)
)
_JnxMediaCardSpaceM10i_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceM10i = _JnxMediaCardSpaceM10i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 11)
)
_JnxM10iMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxM10iMediaCardSpacePIC = _JnxM10iMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 11, 1)
)
_JnxMediaCardSpaceJ2300_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceJ2300 = _JnxMediaCardSpaceJ2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 13)
)
_JnxJ2300MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxJ2300MediaCardSpacePIC = _JnxJ2300MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 13, 1)
)
_JnxMediaCardSpaceJ4300_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceJ4300 = _JnxMediaCardSpaceJ4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 14)
)
_JnxJ4300MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxJ4300MediaCardSpacePIC = _JnxJ4300MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 14, 1)
)
_JnxMediaCardSpaceJ6300_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceJ6300 = _JnxMediaCardSpaceJ6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 15)
)
_JnxJ6300MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxJ6300MediaCardSpacePIC = _JnxJ6300MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 15, 1)
)
_JnxMediaCardSpaceIRM_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceIRM = _JnxMediaCardSpaceIRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 16)
)
_JnxIRMMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxIRMMediaCardSpacePIC = _JnxIRMMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 16, 1)
)
_JnxMediaCardSpaceTX_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceTX = _JnxMediaCardSpaceTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 17)
)
_JnxTXMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxTXMediaCardSpacePIC = _JnxTXMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 17, 1)
)
_JnxMediaCardSpaceM120_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceM120 = _JnxMediaCardSpaceM120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 18)
)
_JnxM120MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxM120MediaCardSpacePIC = _JnxM120MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 18, 1)
)
_JnxMediaCardSpaceJ4350_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceJ4350 = _JnxMediaCardSpaceJ4350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 19)
)
_JnxJ4350MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxJ4350MediaCardSpacePIC = _JnxJ4350MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 19, 1)
)
_JnxMediaCardSpaceJ6350_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceJ6350 = _JnxMediaCardSpaceJ6350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 20)
)
_JnxJ6350MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxJ6350MediaCardSpacePIC = _JnxJ6350MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 20, 1)
)
_JnxMediaCardSpaceMX960_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX960 = _JnxMediaCardSpaceMX960_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 21)
)
_JnxMX960MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX960MediaCardSpacePIC = _JnxMX960MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 21, 1)
)
_JnxMX960MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxMX960MediaCardSpaceMIC = _JnxMX960MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 21, 2)
)
_JnxMediaCardSpaceJ4320_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceJ4320 = _JnxMediaCardSpaceJ4320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 22)
)
_JnxJ4320MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxJ4320MediaCardSpacePIC = _JnxJ4320MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 22, 1)
)
_JnxMediaCardSpaceJ2320_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceJ2320 = _JnxMediaCardSpaceJ2320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 23)
)
_JnxJ2320MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxJ2320MediaCardSpacePIC = _JnxJ2320MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 23, 1)
)
_JnxMediaCardSpaceJ2350_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceJ2350 = _JnxMediaCardSpaceJ2350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 24)
)
_JnxJ2350MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxJ2350MediaCardSpacePIC = _JnxJ2350MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 24, 1)
)
_JnxMediaCardSpaceMX480_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX480 = _JnxMediaCardSpaceMX480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 25)
)
_JnxMX480MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX480MediaCardSpacePIC = _JnxMX480MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 25, 1)
)
_JnxMX480MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxMX480MediaCardSpaceMIC = _JnxMX480MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 25, 2)
)
_JnxMediaCardSpaceSRX5800_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX5800 = _JnxMediaCardSpaceSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 26)
)
_JnxSRX5800MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX5800MediaCardSpacePIC = _JnxSRX5800MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 26, 1)
)
_JnxMediaCardSpaceT1600_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceT1600 = _JnxMediaCardSpaceT1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 27)
)
_JnxT1600MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxT1600MediaCardSpacePIC = _JnxT1600MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 27, 1)
)
_JnxMediaCardSpaceSRX5600_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX5600 = _JnxMediaCardSpaceSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 28)
)
_JnxSRX5600MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX5600MediaCardSpacePIC = _JnxSRX5600MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 28, 1)
)
_JnxMediaCardSpaceMX240_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX240 = _JnxMediaCardSpaceMX240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 29)
)
_JnxMX240MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX240MediaCardSpacePIC = _JnxMX240MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 29, 1)
)
_JnxMX240MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxMX240MediaCardSpaceMIC = _JnxMX240MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 29, 2)
)
_JnxMediaCardSpaceEX3200_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX3200 = _JnxMediaCardSpaceEX3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 30)
)
_JnxEX3200MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX3200MediaCardSpacePIC = _JnxEX3200MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 30, 1)
)
_JnxMediaCardSpaceEX4200_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX4200 = _JnxMediaCardSpaceEX4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 31)
)
_JnxEX4200MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX4200MediaCardSpacePIC = _JnxEX4200MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 31, 1)
)
_JnxMediaCardSpaceEX8208_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX8208 = _JnxMediaCardSpaceEX8208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 32)
)
_JnxEX8208MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX8208MediaCardSpacePIC = _JnxEX8208MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 32, 1)
)
_JnxMediaCardSpaceEX8216_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX8216 = _JnxMediaCardSpaceEX8216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 33)
)
_JnxEX8216MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX8216MediaCardSpacePIC = _JnxEX8216MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 33, 1)
)
_JnxMediaCardSpaceSRX3600_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX3600 = _JnxMediaCardSpaceSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 34)
)
_JnxSRX3600MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX3600MediaCardSpacePIC = _JnxSRX3600MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 34, 1)
)
_JnxMediaCardSpaceSRX3400_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX3400 = _JnxMediaCardSpaceSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 35)
)
_JnxSRX3400MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX3400MediaCardSpacePIC = _JnxSRX3400MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 35, 1)
)
_JnxMediaCardSpaceSRX210_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX210 = _JnxMediaCardSpaceSRX210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 36)
)
_JnxSRX210MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX210MediaCardSpacePIC = _JnxSRX210MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 36, 1)
)
_JnxMediaCardSpaceTXP_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceTXP = _JnxMediaCardSpaceTXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 37)
)
_JnxTXPMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxTXPMediaCardSpacePIC = _JnxTXPMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 37, 1)
)
_JnxMediaCardSpaceJCS_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceJCS = _JnxMediaCardSpaceJCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 38)
)
_JnxJCSMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxJCSMediaCardSpacePIC = _JnxJCSMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 38, 1)
)
_JnxMediaCardSpaceSRX240_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX240 = _JnxMediaCardSpaceSRX240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 39)
)
_JnxSRX240MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX240MediaCardSpacePIC = _JnxSRX240MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 39, 1)
)
_JnxMediaCardSpaceSRX650_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX650 = _JnxMediaCardSpaceSRX650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 40)
)
_JnxSRX650MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX650MediaCardSpacePIC = _JnxSRX650MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 40, 1)
)
_JnxMediaCardSpaceSRX100_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX100 = _JnxMediaCardSpaceSRX100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 41)
)
_JnxSRX100MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX100MediaCardSpacePIC = _JnxSRX100MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 41, 1)
)
_JnxMediaCardSpaceLN1000V_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceLN1000V = _JnxMediaCardSpaceLN1000V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 42)
)
_JnxLN1000VMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxLN1000VMediaCardSpacePIC = _JnxLN1000VMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 42, 1)
)
_JnxMediaCardSpaceEX2200_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX2200 = _JnxMediaCardSpaceEX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 43)
)
_JnxEX2200MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX2200MediaCardSpacePIC = _JnxEX2200MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 43, 1)
)
_JnxMediaCardSpaceEX4500_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX4500 = _JnxMediaCardSpaceEX4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 44)
)
_JnxEX4500MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX4500MediaCardSpacePIC = _JnxEX4500MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 44, 1)
)
_JnxMediaCardSpaceIBM4274M02J02M_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceIBM4274M02J02M = _JnxMediaCardSpaceIBM4274M02J02M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 46)
)
_JnxIBM4274M02J02MMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxIBM4274M02J02MMediaCardSpacePIC = _JnxIBM4274M02J02MMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 46, 1)
)
_JnxIBM4274M02J02MMediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxIBM4274M02J02MMediaCardSpaceMIC = _JnxIBM4274M02J02MMediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 46, 2)
)
_JnxMediaCardSpaceIBM4274M06J06M_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceIBM4274M06J06M = _JnxMediaCardSpaceIBM4274M06J06M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 47)
)
_JnxIBM4274M06J06MMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxIBM4274M06J06MMediaCardSpacePIC = _JnxIBM4274M06J06MMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 47, 1)
)
_JnxIBM4274M06J06MMediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxIBM4274M06J06MMediaCardSpaceMIC = _JnxIBM4274M06J06MMediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 47, 2)
)
_JnxMediaCardSpaceIBM4274M11J11M_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceIBM4274M11J11M = _JnxMediaCardSpaceIBM4274M11J11M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 48)
)
_JnxIBM4274M11J11MMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxIBM4274M11J11MMediaCardSpacePIC = _JnxIBM4274M11J11MMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 48, 1)
)
_JnxIBM4274M11J11MMediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxIBM4274M11J11MMediaCardSpaceMIC = _JnxIBM4274M11J11MMediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 48, 2)
)
_JnxMediaCardSpaceSRX1400_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX1400 = _JnxMediaCardSpaceSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 49)
)
_JnxSRX1400MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX1400MediaCardSpacePIC = _JnxSRX1400MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 49, 1)
)
_JnxMediaCardSpaceIBM4274S58J58S_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceIBM4274S58J58S = _JnxMediaCardSpaceIBM4274S58J58S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 50)
)
_JnxIBM4274S58J58SMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxIBM4274S58J58SMediaCardSpacePIC = _JnxIBM4274S58J58SMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 50, 1)
)
_JnxMediaCardSpaceIBM4274S56J56S_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceIBM4274S56J56S = _JnxMediaCardSpaceIBM4274S56J56S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 51)
)
_JnxIBM4274S56J56SMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxIBM4274S56J56SMediaCardSpacePIC = _JnxIBM4274S56J56SMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 51, 1)
)
_JnxMediaCardSpaceIBM4274S36J36S_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceIBM4274S36J36S = _JnxMediaCardSpaceIBM4274S36J36S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 52)
)
_JnxIBM4274S36J36SMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxIBM4274S36J36SMediaCardSpacePIC = _JnxIBM4274S36J36SMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 52, 1)
)
_JnxMediaCardSpaceIBM4274S34J34S_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceIBM4274S34J34S = _JnxMediaCardSpaceIBM4274S34J34S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 53)
)
_JnxIBM4274S34J34SMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxIBM4274S34J34SMediaCardSpacePIC = _JnxIBM4274S34J34SMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 53, 1)
)
_JnxMediaCardSpaceIBM427348EJ48E_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceIBM427348EJ48E = _JnxMediaCardSpaceIBM427348EJ48E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 54)
)
_JnxIBM427348EJ48EMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxIBM427348EJ48EMediaCardSpacePIC = _JnxIBM427348EJ48EMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 54, 1)
)
_JnxMediaCardSpaceIBM4274E08J08E_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceIBM4274E08J08E = _JnxMediaCardSpaceIBM4274E08J08E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 55)
)
_JnxIBM4274E08J08EMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxIBM4274E08J08EMediaCardSpacePIC = _JnxIBM4274E08J08EMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 55, 1)
)
_JnxMediaCardSpaceIBM4274E16J16E_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceIBM4274E16J16E = _JnxMediaCardSpaceIBM4274E16J16E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 56)
)
_JnxIBM4274E16J16EMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxIBM4274E16J16EMediaCardSpacePIC = _JnxIBM4274E16J16EMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 56, 1)
)
_JnxMediaCardSpaceMX80_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX80 = _JnxMediaCardSpaceMX80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 57)
)
_JnxMX80MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX80MediaCardSpacePIC = _JnxMX80MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 57, 1)
)
_JnxMX80MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxMX80MediaCardSpaceMIC = _JnxMX80MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 57, 2)
)
_JnxMediaCardSpaceSRX220_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX220 = _JnxMediaCardSpaceSRX220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 58)
)
_JnxSRX220MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX220MediaCardSpacePIC = _JnxSRX220MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 58, 1)
)
_JnxMediaCardSpaceEXXRE_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEXXRE = _JnxMediaCardSpaceEXXRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 59)
)
_JnxEXXREMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEXXREMediaCardSpacePIC = _JnxEXXREMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 59, 1)
)
_JnxMediaCardSpaceQFXInterconnect_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceQFXInterconnect = _JnxMediaCardSpaceQFXInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 60)
)
_JnxQFXInterconnectMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxQFXInterconnectMediaCardSpacePIC = _JnxQFXInterconnectMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 60, 1)
)
_JnxMediaCardSpaceQFXNode_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceQFXNode = _JnxMediaCardSpaceQFXNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 61)
)
_JnxQFXNodeMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxQFXNodeMediaCardSpacePIC = _JnxQFXNodeMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 61, 1)
)
_JnxMediaCardSpaceQFXJVRE_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceQFXJVRE = _JnxMediaCardSpaceQFXJVRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 62)
)
_JnxQFXJVREMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxQFXJVREMediaCardSpacePIC = _JnxQFXJVREMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 62, 1)
)
_JnxMediaCardSpaceEX4300_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX4300 = _JnxMediaCardSpaceEX4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 63)
)
_JnxEX4300MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX4300MediaCardSpacePIC = _JnxEX4300MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 63, 1)
)
_JnxMediaCardSpaceSRX110_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX110 = _JnxMediaCardSpaceSRX110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 64)
)
_JnxSRX110MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX110MediaCardSpacePIC = _JnxSRX110MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 64, 1)
)
_JnxMediaCardSpaceSRX120_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX120 = _JnxMediaCardSpaceSRX120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 65)
)
_JnxSRX120MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX120MediaCardSpacePIC = _JnxSRX120MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 65, 1)
)
_JnxMediaCardSpaceMAG8600_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMAG8600 = _JnxMediaCardSpaceMAG8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 66)
)
_JnxMAG8600MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMAG8600MediaCardSpacePIC = _JnxMAG8600MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 66, 1)
)
_JnxMediaCardSpaceMAG6611_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMAG6611 = _JnxMediaCardSpaceMAG6611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 67)
)
_JnxMAG6611MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMAG6611MediaCardSpacePIC = _JnxMAG6611MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 67, 1)
)
_JnxMediaCardSpaceMAG6610_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMAG6610 = _JnxMediaCardSpaceMAG6610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 68)
)
_JnxMAG6610MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMAG6610MediaCardSpacePIC = _JnxMAG6610MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 68, 1)
)
_JnxMediaCardSpacePTX5000_ObjectIdentity = ObjectIdentity
jnxMediaCardSpacePTX5000 = _JnxMediaCardSpacePTX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 69)
)
_JnxPTX5000MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxPTX5000MediaCardSpacePIC = _JnxPTX5000MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 69, 1)
)
_JnxMediaCardSpaceIBM0719J45E_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceIBM0719J45E = _JnxMediaCardSpaceIBM0719J45E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 71)
)
_JnxIBM0719J45EMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxIBM0719J45EMediaCardSpacePIC = _JnxIBM0719J45EMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 71, 1)
)
_JnxMediaCardSpaceIBMJ08F_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceIBMJ08F = _JnxMediaCardSpaceIBMJ08F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 72)
)
_JnxIBMJ08FMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxIBMJ08FMediaCardSpacePIC = _JnxIBMJ08FMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 72, 1)
)
_JnxMediaCardSpaceIBMJ52F_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceIBMJ52F = _JnxMediaCardSpaceIBMJ52F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 73)
)
_JnxIBMJ52FMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxIBMJ52FMediaCardSpacePIC = _JnxIBMJ52FMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 73, 1)
)
_JnxMediaCardSpaceEX6210_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX6210 = _JnxMediaCardSpaceEX6210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 74)
)
_JnxEX6210MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX6210MediaCardSpacePIC = _JnxEX6210MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 74, 1)
)
_JnxMediaCardSpaceDellJFX3500_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceDellJFX3500 = _JnxMediaCardSpaceDellJFX3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 75)
)
_JnxDellJFX3500MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxDellJFX3500MediaCardSpacePIC = _JnxDellJFX3500MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 75, 1)
)
_JnxMediaCardSpaceEX3300_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX3300 = _JnxMediaCardSpaceEX3300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 76)
)
_JnxEX3300MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX3300MediaCardSpacePIC = _JnxEX3300MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 76, 1)
)
_JnxMediaCardSpaceDELLJSRX3600_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceDELLJSRX3600 = _JnxMediaCardSpaceDELLJSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 77)
)
_JnxDELLJSRX3600MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxDELLJSRX3600MediaCardSpacePIC = _JnxDELLJSRX3600MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 77, 1)
)
_JnxMediaCardSpaceDELLJSRX3400_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceDELLJSRX3400 = _JnxMediaCardSpaceDELLJSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 78)
)
_JnxDELLJSRX3400MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxDELLJSRX3400MediaCardSpacePIC = _JnxDELLJSRX3400MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 78, 1)
)
_JnxMediaCardSpaceDELLJSRX1400_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceDELLJSRX1400 = _JnxMediaCardSpaceDELLJSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 79)
)
_JnxDELLJSRX1400MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxDELLJSRX1400MediaCardSpacePIC = _JnxDELLJSRX1400MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 79, 1)
)
_JnxMediaCardSpaceDELLJSRX5800_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceDELLJSRX5800 = _JnxMediaCardSpaceDELLJSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 80)
)
_JnxDELLJSRX5800MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5800MediaCardSpacePIC = _JnxDELLJSRX5800MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 80, 1)
)
_JnxMediaCardSpaceDELLJSRX5600_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceDELLJSRX5600 = _JnxMediaCardSpaceDELLJSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 81)
)
_JnxDELLJSRX5600MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5600MediaCardSpacePIC = _JnxDELLJSRX5600MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 81, 1)
)
_JnxMediaCardSpaceQFXSwitch_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceQFXSwitch = _JnxMediaCardSpaceQFXSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 82)
)
_JnxQFXSwitchMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxQFXSwitchMediaCardSpacePIC = _JnxQFXSwitchMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 82, 1)
)
_JnxMediaCardSpaceT4000_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceT4000 = _JnxMediaCardSpaceT4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 83)
)
_JnxT4000MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxT4000MediaCardSpacePIC = _JnxT4000MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 83, 1)
)
_JnxMediaCardSpaceSRX550_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX550 = _JnxMediaCardSpaceSRX550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 86)
)
_JnxSRX550MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX550MediaCardSpacePIC = _JnxSRX550MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 86, 1)
)
_JnxMediaCardSpaceACX_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX = _JnxMediaCardSpaceACX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 87)
)
_JnxACXMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACXMediaCardSpacePIC = _JnxACXMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 87, 1)
)
_JnxACXMediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACXMediaCardSpaceMIC = _JnxACXMediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 87, 2)
)
_JnxMediaCardSpaceMX40_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX40 = _JnxMediaCardSpaceMX40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 88)
)
_JnxMX40MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX40MediaCardSpacePIC = _JnxMX40MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 88, 1)
)
_JnxMX40MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxMX40MediaCardSpaceMIC = _JnxMX40MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 88, 2)
)
_JnxMediaCardSpaceMX10_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX10 = _JnxMediaCardSpaceMX10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 89)
)
_JnxMX10MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX10MediaCardSpacePIC = _JnxMX10MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 89, 1)
)
_JnxMX10MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxMX10MediaCardSpaceMIC = _JnxMX10MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 89, 2)
)
_JnxMediaCardSpaceMX5_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX5 = _JnxMediaCardSpaceMX5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 90)
)
_JnxMX5MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX5MediaCardSpacePIC = _JnxMX5MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 90, 1)
)
_JnxMX5MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxMX5MediaCardSpaceMIC = _JnxMX5MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 90, 2)
)
_JnxMediaCardSpaceQFXMInterconnect_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceQFXMInterconnect = _JnxMediaCardSpaceQFXMInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 91)
)
_JnxQFXMInterconnectMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxQFXMInterconnectMediaCardSpacePIC = _JnxQFXMInterconnectMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 91, 1)
)
_JnxMediaCardSpaceEX4550_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX4550 = _JnxMediaCardSpaceEX4550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 92)
)
_JnxEX4550MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX4550MediaCardSpacePIC = _JnxEX4550MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 92, 1)
)
_JnxMediaCardSpaceMX2020_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX2020 = _JnxMediaCardSpaceMX2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 93)
)
_JnxMX2020MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX2020MediaCardSpacePIC = _JnxMX2020MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 93, 1)
)
_JnxMX2020MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxMX2020MediaCardSpaceMIC = _JnxMX2020MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 93, 2)
)
_JnxMediaCardSpaceLN2600_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceLN2600 = _JnxMediaCardSpaceLN2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 95)
)
_JnxLN2600MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxLN2600MediaCardSpacePIC = _JnxLN2600MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 95, 1)
)
_JnxMediaCardSpaceFireflyPerimeter_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceFireflyPerimeter = _JnxMediaCardSpaceFireflyPerimeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 96)
)
_JnxFireflyPerimeterMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxFireflyPerimeterMediaCardSpacePIC = _JnxFireflyPerimeterMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 96, 1)
)
_JnxMediaCardSpaceMX104_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX104 = _JnxMediaCardSpaceMX104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 97)
)
_JnxMX104MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX104MediaCardSpacePIC = _JnxMX104MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 97, 1)
)
_JnxMX104MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxMX104MediaCardSpaceMIC = _JnxMX104MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 97, 2)
)
_JnxMediaCardSpacePTX3000_ObjectIdentity = ObjectIdentity
jnxMediaCardSpacePTX3000 = _JnxMediaCardSpacePTX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 98)
)
_JnxPTX3000MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxPTX3000MediaCardSpacePIC = _JnxPTX3000MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 98, 1)
)
_JnxMediaCardSpaceMX2010_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX2010 = _JnxMediaCardSpaceMX2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 99)
)
_JnxMX2010MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX2010MediaCardSpacePIC = _JnxMX2010MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 99, 1)
)
_JnxMX2010MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxMX2010MediaCardSpaceMIC = _JnxMX2010MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 99, 2)
)
_JnxMediaCardSpaceLN2800_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceLN2800 = _JnxMediaCardSpaceLN2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 101)
)
_JnxLN2800MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxLN2800MediaCardSpacePIC = _JnxLN2800MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 101, 1)
)
_JnxMediaCardSpaceEX9214_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX9214 = _JnxMediaCardSpaceEX9214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 102)
)
_JnxEX9214MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX9214MediaCardSpacePIC = _JnxEX9214MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 102, 1)
)
_JnxEX9214MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxEX9214MediaCardSpaceMIC = _JnxEX9214MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 102, 2)
)
_JnxMediaCardSpaceEX9208_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX9208 = _JnxMediaCardSpaceEX9208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 103)
)
_JnxEX9208MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX9208MediaCardSpacePIC = _JnxEX9208MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 103, 1)
)
_JnxEX9208MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxEX9208MediaCardSpaceMIC = _JnxEX9208MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 103, 2)
)
_JnxMediaCardSpaceEX9204_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX9204 = _JnxMediaCardSpaceEX9204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 104)
)
_JnxEX9204MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX9204MediaCardSpacePIC = _JnxEX9204MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 104, 1)
)
_JnxEX9204MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxEX9204MediaCardSpaceMIC = _JnxEX9204MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 104, 2)
)
_JnxMediaCardSpaceSRX5400_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX5400 = _JnxMediaCardSpaceSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 105)
)
_JnxSRX5400MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX5400MediaCardSpacePIC = _JnxSRX5400MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 105, 1)
)
_JnxMediaCardSpaceIBM4274S54J54S_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceIBM4274S54J54S = _JnxMediaCardSpaceIBM4274S54J54S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 106)
)
_JnxIBM4274S54J54SMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxIBM4274S54J54SMediaCardSpacePIC = _JnxIBM4274S54J54SMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 106, 1)
)
_JnxMediaCardSpaceDELLJSRX5400_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceDELLJSRX5400 = _JnxMediaCardSpaceDELLJSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 107)
)
_JnxDELLJSRX5400MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxDELLJSRX5400MediaCardSpacePIC = _JnxDELLJSRX5400MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 107, 1)
)
_JnxMediaCardSpaceVMX_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceVMX = _JnxMediaCardSpaceVMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 108)
)
_JnxVMXMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxVMXMediaCardSpacePIC = _JnxVMXMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 108, 1)
)
_JnxVMXMediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxVMXMediaCardSpaceMIC = _JnxVMXMediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 108, 2)
)
_JnxMediaCardSpaceEX4600_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX4600 = _JnxMediaCardSpaceEX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 109)
)
_JnxEX4600MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX4600MediaCardSpacePIC = _JnxEX4600MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 109, 1)
)
_JnxMediaCardSpaceACX1000_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX1000 = _JnxMediaCardSpaceACX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 113)
)
_JnxACX1000MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX1000MediaCardSpacePIC = _JnxACX1000MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 113, 1)
)
_JnxACX1000MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX1000MediaCardSpaceMIC = _JnxACX1000MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 113, 2)
)
_JnxMediaCardSpaceACX2000_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX2000 = _JnxMediaCardSpaceACX2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 114)
)
_JnxACX2000MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX2000MediaCardSpacePIC = _JnxACX2000MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 114, 1)
)
_JnxACX2000MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX2000MediaCardSpaceMIC = _JnxACX2000MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 114, 2)
)
_JnxMediaCardSpaceACX1100_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX1100 = _JnxMediaCardSpaceACX1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 115)
)
_JnxACX1100MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX1100MediaCardSpacePIC = _JnxACX1100MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 115, 1)
)
_JnxACX1100MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX1100MediaCardSpaceMIC = _JnxACX1100MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 115, 2)
)
_JnxMediaCardSpaceACX2100_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX2100 = _JnxMediaCardSpaceACX2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 116)
)
_JnxACX2100MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX2100MediaCardSpacePIC = _JnxACX2100MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 116, 1)
)
_JnxACX2100MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX2100MediaCardSpaceMIC = _JnxACX2100MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 116, 2)
)
_JnxMediaCardSpaceACX2200_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX2200 = _JnxMediaCardSpaceACX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 117)
)
_JnxACX2200MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX2200MediaCardSpacePIC = _JnxACX2200MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 117, 1)
)
_JnxACX2200MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX2200MediaCardSpaceMIC = _JnxACX2200MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 117, 2)
)
_JnxMediaCardSpaceACX4000_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX4000 = _JnxMediaCardSpaceACX4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 118)
)
_JnxACX4000MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX4000MediaCardSpacePIC = _JnxACX4000MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 118, 1)
)
_JnxACX4000MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX4000MediaCardSpaceMIC = _JnxACX4000MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 118, 2)
)
_JnxMediaCardSpaceACX500AC_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX500AC = _JnxMediaCardSpaceACX500AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 119)
)
_JnxACX500ACMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX500ACMediaCardSpacePIC = _JnxACX500ACMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 119, 1)
)
_JnxACX500ACMediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX500ACMediaCardSpaceMIC = _JnxACX500ACMediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 119, 2)
)
_JnxMediaCardSpaceACX500DC_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX500DC = _JnxMediaCardSpaceACX500DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 120)
)
_JnxACX500DCMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX500DCMediaCardSpacePIC = _JnxACX500DCMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 120, 1)
)
_JnxACX500DCMediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX500DCMediaCardSpaceMIC = _JnxACX500DCMediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 120, 2)
)
_JnxMediaCardSpaceACX500OAC_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX500OAC = _JnxMediaCardSpaceACX500OAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 121)
)
_JnxACX500OACMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX500OACMediaCardSpacePIC = _JnxACX500OACMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 121, 1)
)
_JnxACX500OACMediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX500OACMediaCardSpaceMIC = _JnxACX500OACMediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 121, 2)
)
_JnxMediaCardSpaceACX500ODC_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX500ODC = _JnxMediaCardSpaceACX500ODC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 122)
)
_JnxACX500ODCMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX500ODCMediaCardSpacePIC = _JnxACX500ODCMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 122, 1)
)
_JnxACX500ODCMediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX500ODCMediaCardSpaceMIC = _JnxACX500ODCMediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 122, 2)
)
_JnxMediaCardSpaceACX500OPOEAC_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX500OPOEAC = _JnxMediaCardSpaceACX500OPOEAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 123)
)
_JnxACX500OPOEACMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX500OPOEACMediaCardSpacePIC = _JnxACX500OPOEACMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 123, 1)
)
_JnxACX500OPOEACMediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX500OPOEACMediaCardSpaceMIC = _JnxACX500OPOEACMediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 123, 2)
)
_JnxMediaCardSpaceACX500OPOEDC_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX500OPOEDC = _JnxMediaCardSpaceACX500OPOEDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 124)
)
_JnxACX500OPOEDCMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX500OPOEDCMediaCardSpacePIC = _JnxACX500OPOEDCMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 124, 1)
)
_JnxACX500OPOEDCMediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX500OPOEDCMediaCardSpaceMIC = _JnxACX500OPOEDCMediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 124, 2)
)
_JnxMediaCardSpaceSatelliteDevice_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSatelliteDevice = _JnxMediaCardSpaceSatelliteDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 125)
)
_JnxSatelliteDeviceMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSatelliteDeviceMediaCardSpacePIC = _JnxSatelliteDeviceMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 125, 1)
)
_JnxMediaCardSpaceACX5048_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX5048 = _JnxMediaCardSpaceACX5048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 126)
)
_JnxACX5048MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX5048MediaCardSpacePIC = _JnxACX5048MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 126, 1)
)
_JnxMediaCardSpaceACX5096_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX5096 = _JnxMediaCardSpaceACX5096_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 127)
)
_JnxACX5096MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX5096MediaCardSpacePIC = _JnxACX5096MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 127, 1)
)
_JnxMediaCardSpaceLN1000CC_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceLN1000CC = _JnxMediaCardSpaceLN1000CC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 128)
)
_JnxLN1000CCMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxLN1000CCMediaCardSpacePIC = _JnxLN1000CCMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 128, 1)
)
_JnxMediaCardSpaceVSRX_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceVSRX = _JnxMediaCardSpaceVSRX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 129)
)
_JnxVSRXMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxVSRXMediaCardSpacePIC = _JnxVSRXMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 129, 1)
)
_JnxMediaCardSpacePTX1000_ObjectIdentity = ObjectIdentity
jnxMediaCardSpacePTX1000 = _JnxMediaCardSpacePTX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 130)
)
_JnxPTX1000MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxPTX1000MediaCardSpacePIC = _JnxPTX1000MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 130, 1)
)
_JnxMediaCardSpaceEX3400_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX3400 = _JnxMediaCardSpaceEX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 131)
)
_JnxEX3400MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX3400MediaCardSpacePIC = _JnxEX3400MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 131, 1)
)
_JnxMediaCardSpaceEX2300_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX2300 = _JnxMediaCardSpaceEX2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 132)
)
_JnxEX2300MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX2300MediaCardSpacePIC = _JnxEX2300MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 132, 1)
)
_JnxMediaCardSpaceSRX300_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX300 = _JnxMediaCardSpaceSRX300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 133)
)
_JnxSRX300MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX300MediaCardSpacePIC = _JnxSRX300MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 133, 1)
)
_JnxMediaCardSpaceSRX320_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX320 = _JnxMediaCardSpaceSRX320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 134)
)
_JnxSRX320MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX320MediaCardSpacePIC = _JnxSRX320MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 134, 1)
)
_JnxMediaCardSpaceSRX340_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX340 = _JnxMediaCardSpaceSRX340_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 135)
)
_JnxSRX340MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX340MediaCardSpacePIC = _JnxSRX340MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 135, 1)
)
_JnxMediaCardSpaceSRX345_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX345 = _JnxMediaCardSpaceSRX345_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 136)
)
_JnxSRX345MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX345MediaCardSpacePIC = _JnxSRX345MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 136, 1)
)
_JnxMediaCardSpaceSRX1500_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX1500 = _JnxMediaCardSpaceSRX1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 137)
)
_JnxSRX1500MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX1500MediaCardSpacePIC = _JnxSRX1500MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 137, 1)
)
_JnxMediaCardSpaceJNP10003_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceJNP10003 = _JnxMediaCardSpaceJNP10003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 139)
)
_JnxJNP10003MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxJNP10003MediaCardSpacePIC = _JnxJNP10003MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 139, 1)
)
_JnxPicJNP1000312xQSFP28MacsecTIC_ObjectIdentity = ObjectIdentity
jnxPicJNP1000312xQSFP28MacsecTIC = _JnxPicJNP1000312xQSFP28MacsecTIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 139, 2)
)
_JnxJNP10003MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxJNP10003MediaCardSpaceMIC = _JnxJNP10003MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 139, 3)
)
_JnxMediaCardSpaceSRX4600_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX4600 = _JnxMediaCardSpaceSRX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 140)
)
_JnxSRX4600MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX4600MediaCardSpacePIC = _JnxSRX4600MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 140, 1)
)
_JnxMediaCardSpaceSRX4800_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX4800 = _JnxMediaCardSpaceSRX4800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 141)
)
_JnxSRX4800MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX4800MediaCardSpacePIC = _JnxSRX4800MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 141, 1)
)
_JnxSRX4800MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxSRX4800MediaCardSpaceMIC = _JnxSRX4800MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 141, 2)
)
_JnxMediaCardSpaceSRX4100_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX4100 = _JnxMediaCardSpaceSRX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 142)
)
_JnxSRX4100MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX4100MediaCardSpacePIC = _JnxSRX4100MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 142, 1)
)
_JnxMediaCardSpaceSRX4200_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX4200 = _JnxMediaCardSpaceSRX4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 143)
)
_JnxMediaCardSpaceJNP204_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceJNP204 = _JnxMediaCardSpaceJNP204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 144)
)
_JnxPicJNP204MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxPicJNP204MediaCardSpacePIC = _JnxPicJNP204MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 144, 1)
)
_JnxPicJNP2048XSFPP_ObjectIdentity = ObjectIdentity
jnxPicJNP2048XSFPP = _JnxPicJNP2048XSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 144, 2)
)
_JnxMediaCardSpaceMX2008_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX2008 = _JnxMediaCardSpaceMX2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 145)
)
_JnxMX2008MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX2008MediaCardSpacePIC = _JnxMX2008MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 145, 1)
)
_JnxMX2008MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxMX2008MediaCardSpaceMIC = _JnxMX2008MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 145, 2)
)
_JnxMediaCardSpaceMXTSR80_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMXTSR80 = _JnxMediaCardSpaceMXTSR80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 146)
)
_JnxMXTSR80MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMXTSR80MediaCardSpacePIC = _JnxMXTSR80MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 146, 1)
)
_JnxMXTSR80MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxMXTSR80MediaCardSpaceMIC = _JnxMXTSR80MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 146, 2)
)
_JnxMediaCardSpacePTX10008_ObjectIdentity = ObjectIdentity
jnxMediaCardSpacePTX10008 = _JnxMediaCardSpacePTX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 147)
)
_JnxPTX10008MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxPTX10008MediaCardSpacePIC = _JnxPTX10008MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 147, 1)
)
_JnxMediaCardSpaceACX5448_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX5448 = _JnxMediaCardSpaceACX5448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 148)
)
_JnxACX5448MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX5448MediaCardSpacePIC = _JnxACX5448MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 148, 1)
)
_JnxACX5448MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX5448MediaCardSpaceMIC = _JnxACX5448MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 148, 2)
)
_JnxMediaCardSpacePTX10016_ObjectIdentity = ObjectIdentity
jnxMediaCardSpacePTX10016 = _JnxMediaCardSpacePTX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 150)
)
_JnxPTX10016MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxPTX10016MediaCardSpacePIC = _JnxPTX10016MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 150, 1)
)
_JnxMediaCardSpaceEX9251_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX9251 = _JnxMediaCardSpaceEX9251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 151)
)
_JnxPicEX92514xQSFP28_ObjectIdentity = ObjectIdentity
jnxPicEX92514xQSFP28 = _JnxPicEX92514xQSFP28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 151, 1)
)
_JnxPicEX92518XSFPP_ObjectIdentity = ObjectIdentity
jnxPicEX92518XSFPP = _JnxPicEX92518XSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 151, 2)
)
_JnxMediaCardSpaceMX150_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX150 = _JnxMediaCardSpaceMX150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 152)
)
_JnxMX150MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX150MediaCardSpacePIC = _JnxMX150MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 152, 1)
)
_JnxMX150MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxMX150MediaCardSpaceMIC = _JnxMX150MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 152, 2)
)
_JnxMediaCardSpaceJNP10001_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceJNP10001 = _JnxMediaCardSpaceJNP10001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 153)
)
_JnxJNP10001MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxJNP10001MediaCardSpacePIC = _JnxJNP10001MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 153, 1)
)
_JnxPicJNP1000116xQSFP28MacsecTIC_ObjectIdentity = ObjectIdentity
jnxPicJNP1000116xQSFP28MacsecTIC = _JnxPicJNP1000116xQSFP28MacsecTIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 153, 2)
)
_JnxMediaCardSpaceMX10008_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX10008 = _JnxMediaCardSpaceMX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 154)
)
_JnxMX10008MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX10008MediaCardSpacePIC = _JnxMX10008MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 154, 1)
)
_JnxMediaCardSpaceMX10016_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX10016 = _JnxMediaCardSpaceMX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 155)
)
_JnxMX10016MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX10016MediaCardSpacePIC = _JnxMX10016MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 155, 1)
)
_JnxMediaCardSpaceEX9253_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX9253 = _JnxMediaCardSpaceEX9253_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 156)
)
_JnxEX9253MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX9253MediaCardSpacePIC = _JnxEX9253MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 156, 1)
)
_JnxPicEX925312xQSFP28MacsecTIC_ObjectIdentity = ObjectIdentity
jnxPicEX925312xQSFP28MacsecTIC = _JnxPicEX925312xQSFP28MacsecTIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 156, 2)
)
_JnxEX9253MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxEX9253MediaCardSpaceMIC = _JnxEX9253MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 156, 3)
)
_JnxMediaCardSpaceACX5448M_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX5448M = _JnxMediaCardSpaceACX5448M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 158)
)
_JnxACX5448MMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX5448MMediaCardSpacePIC = _JnxACX5448MMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 158, 1)
)
_JnxACX5448MMediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX5448MMediaCardSpaceMIC = _JnxACX5448MMediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 158, 2)
)
_JnxMediaCardSpaceACX5448D_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX5448D = _JnxMediaCardSpaceACX5448D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 159)
)
_JnxACX5448DMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX5448DMediaCardSpacePIC = _JnxACX5448DMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 159, 1)
)
_JnxACX5448DMediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX5448DMediaCardSpaceMIC = _JnxACX5448DMediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 159, 2)
)
_JnxMediaCardSpaceACX6360OR_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX6360OR = _JnxMediaCardSpaceACX6360OR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 160)
)
_JnxACX6360ORMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX6360ORMediaCardSpacePIC = _JnxACX6360ORMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 160, 1)
)
_JnxPicACX6360OR20xQSFP28TIC_ObjectIdentity = ObjectIdentity
jnxPicACX6360OR20xQSFP28TIC = _JnxPicACX6360OR20xQSFP28TIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 160, 2)
)
_JnxPicACX6360OR8xCFP2DCOTIC_ObjectIdentity = ObjectIdentity
jnxPicACX6360OR8xCFP2DCOTIC = _JnxPicACX6360OR8xCFP2DCOTIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 160, 3)
)
_JnxMediaCardSpaceACX6360OX_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX6360OX = _JnxMediaCardSpaceACX6360OX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 161)
)
_JnxACX6360OXMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX6360OXMediaCardSpacePIC = _JnxACX6360OXMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 161, 1)
)
_JnxPicACX6360OX20xQSFP28TIC_ObjectIdentity = ObjectIdentity
jnxPicACX6360OX20xQSFP28TIC = _JnxPicACX6360OX20xQSFP28TIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 161, 2)
)
_JnxPicACX6360OX8xCFP2DCOTIC_ObjectIdentity = ObjectIdentity
jnxPicACX6360OX8xCFP2DCOTIC = _JnxPicACX6360OX8xCFP2DCOTIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 161, 3)
)
_JnxMediaCardSpaceACX710_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX710 = _JnxMediaCardSpaceACX710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 162)
)
_JnxACX710MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX710MediaCardSpacePIC = _JnxACX710MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 162, 1)
)
_JnxACX710MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX710MediaCardSpaceMIC = _JnxACX710MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 162, 2)
)
_JnxMediaCardSpaceACX5800_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX5800 = _JnxMediaCardSpaceACX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 163)
)
_JnxACX5800MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX5800MediaCardSpacePIC = _JnxACX5800MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 163, 1)
)
_JnxACX5800MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxACX5800MediaCardSpaceMIC = _JnxACX5800MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 163, 2)
)
_JnxMediaCardSpaceSRX380_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX380 = _JnxMediaCardSpaceSRX380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 164)
)
_JnxSRX380MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX380MediaCardSpacePIC = _JnxSRX380MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 164, 1)
)
_JnxMediaCardSpaceEX4400_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX4400 = _JnxMediaCardSpaceEX4400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 165)
)
_JnxEX4400MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX4400MediaCardSpacePIC = _JnxEX4400MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 165, 1)
)
_JnxMediaCardSpaceR6675_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceR6675 = _JnxMediaCardSpaceR6675_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 166)
)
_JnxR6675MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxR6675MediaCardSpacePIC = _JnxR6675MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 166, 1)
)
_JnxR6675MediaCardSpaceMIC_ObjectIdentity = ObjectIdentity
jnxR6675MediaCardSpaceMIC = _JnxR6675MediaCardSpaceMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 166, 2)
)
_JnxMediaCardSpaceMX304_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX304 = _JnxMediaCardSpaceMX304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 167)
)
_JnxMX304MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX304MediaCardSpacePIC = _JnxMX304MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 167, 1)
)
_JnxMediaCardSpaceMX10004_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceMX10004 = _JnxMediaCardSpaceMX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 168)
)
_JnxMX10004MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxMX10004MediaCardSpacePIC = _JnxMX10004MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 168, 1)
)
_JnxMediaCardSpaceEX4100_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX4100 = _JnxMediaCardSpaceEX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 169)
)
_JnxEX4100MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX4100MediaCardSpacePIC = _JnxEX4100MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 169, 1)
)
_JnxMediaCardSpaceEX4650_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceEX4650 = _JnxMediaCardSpaceEX4650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 508)
)
_JnxEX4650MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxEX4650MediaCardSpacePIC = _JnxEX4650MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 508, 1)
)
_JnxMediaCardSpacePTX1000260C_ObjectIdentity = ObjectIdentity
jnxMediaCardSpacePTX1000260C = _JnxMediaCardSpacePTX1000260C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 513)
)
_JnxPTX1000260CMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxPTX1000260CMediaCardSpacePIC = _JnxPTX1000260CMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 513, 1)
)
_JnxMediaCardSpacePTX10004_ObjectIdentity = ObjectIdentity
jnxMediaCardSpacePTX10004 = _JnxMediaCardSpacePTX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 570)
)
_JnxPTX10004MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxPTX10004MediaCardSpacePIC = _JnxPTX10004MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 570, 1)
)
_JnxMediaCardSpaceACX7KSwitch_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX7KSwitch = _JnxMediaCardSpaceACX7KSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 578)
)
_JnxACX7KSwitchMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX7KSwitchMediaCardSpacePIC = _JnxACX7KSwitchMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 578, 1)
)
_JnxMediaCardSpaceACX710032c_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX710032c = _JnxMediaCardSpaceACX710032c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 579)
)
_JnxACX710032cMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX710032cMediaCardSpacePIC = _JnxACX710032cMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 579, 1)
)
_JnxMediaCardSpaceACX710048l_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX710048l = _JnxMediaCardSpaceACX710048l_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 580)
)
_JnxACX710048lMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX710048lMediaCardSpacePIC = _JnxACX710048lMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 580, 1)
)
_JnxMediaCardSpaceACX7908_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX7908 = _JnxMediaCardSpaceACX7908_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 581)
)
_JnxACX7908MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX7908MediaCardSpacePIC = _JnxACX7908MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 581, 1)
)
_JnxMediaCardSpaceACX7024_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX7024 = _JnxMediaCardSpaceACX7024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 582)
)
_JnxACX7024MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX7024MediaCardSpacePIC = _JnxACX7024MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 582, 1)
)
_JnxMediaCardSpaceSRX1600_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX1600 = _JnxMediaCardSpaceSRX1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 583)
)
_JnxSRX1600MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX1600MediaCardSpacePIC = _JnxSRX1600MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 583, 1)
)
_JnxMediaCardSpaceSRX2300_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX2300 = _JnxMediaCardSpaceSRX2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 584)
)
_JnxSRX2300MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX2300MediaCardSpacePIC = _JnxSRX2300MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 584, 1)
)
_JnxMediaCardSpaceSRX4300_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX4300 = _JnxMediaCardSpaceSRX4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 585)
)
_JnxSRX4300MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX4300MediaCardSpacePIC = _JnxSRX4300MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 585, 1)
)
_JnxMediaCardSpaceACX7332_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX7332 = _JnxMediaCardSpaceACX7332_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 586)
)
_JnxACX7332MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX7332MediaCardSpacePIC = _JnxACX7332MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 586, 1)
)
_JnxMediaCardSpaceACX7348_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX7348 = _JnxMediaCardSpaceACX7348_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 587)
)
_JnxACX7348MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX7348MediaCardSpacePIC = _JnxACX7348MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 587, 1)
)
_JnxMediaCardSpaceACX7024X_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceACX7024X = _JnxMediaCardSpaceACX7024X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 588)
)
_JnxACX7024XMediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxACX7024XMediaCardSpacePIC = _JnxACX7024XMediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 588, 1)
)
_JnxMediaCardSpaceSRX4700_ObjectIdentity = ObjectIdentity
jnxMediaCardSpaceSRX4700 = _JnxMediaCardSpaceSRX4700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 590)
)
_JnxSRX4700MediaCardSpacePIC_ObjectIdentity = ObjectIdentity
jnxSRX4700MediaCardSpacePIC = _JnxSRX4700MediaCardSpacePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 3, 590, 1)
)
_JnxSubSpace_ObjectIdentity = ObjectIdentity
jnxSubSpace = _JnxSubSpace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 4)
)
_JnxSubSpaceM160_ObjectIdentity = ObjectIdentity
jnxSubSpaceM160 = _JnxSubSpaceM160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 4, 1)
)
_JnxM160SubSpaceSFM_ObjectIdentity = ObjectIdentity
jnxM160SubSpaceSFM = _JnxM160SubSpaceSFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 2, 4, 1, 1)
)
_JnxClassContents_ObjectIdentity = ObjectIdentity
jnxClassContents = _JnxClassContents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3)
)
_JnxBackplane_ObjectIdentity = ObjectIdentity
jnxBackplane = _JnxBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1)
)
_JnxBackplaneM40_ObjectIdentity = ObjectIdentity
jnxBackplaneM40 = _JnxBackplaneM40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 1)
)
_JnxBackplaneM20_ObjectIdentity = ObjectIdentity
jnxBackplaneM20 = _JnxBackplaneM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 2)
)
_JnxMidplaneM160_ObjectIdentity = ObjectIdentity
jnxMidplaneM160 = _JnxMidplaneM160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 3)
)
_JnxMidplaneM10_ObjectIdentity = ObjectIdentity
jnxMidplaneM10 = _JnxMidplaneM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 4)
)
_JnxMidplaneM5_ObjectIdentity = ObjectIdentity
jnxMidplaneM5 = _JnxMidplaneM5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 5)
)
_JnxMidplaneT640_ObjectIdentity = ObjectIdentity
jnxMidplaneT640 = _JnxMidplaneT640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 6)
)
_JnxMidplaneT320_ObjectIdentity = ObjectIdentity
jnxMidplaneT320 = _JnxMidplaneT320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 7)
)
_JnxMidplaneM40e_ObjectIdentity = ObjectIdentity
jnxMidplaneM40e = _JnxMidplaneM40e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 8)
)
_JnxMidplaneM320_ObjectIdentity = ObjectIdentity
jnxMidplaneM320 = _JnxMidplaneM320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 9)
)
_JnxMidplaneM7i_ObjectIdentity = ObjectIdentity
jnxMidplaneM7i = _JnxMidplaneM7i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 10)
)
_JnxMidplaneM10i_ObjectIdentity = ObjectIdentity
jnxMidplaneM10i = _JnxMidplaneM10i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 11)
)
_JnxMidplaneJ2300_ObjectIdentity = ObjectIdentity
jnxMidplaneJ2300 = _JnxMidplaneJ2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 13)
)
_JnxMidplaneJ4300_ObjectIdentity = ObjectIdentity
jnxMidplaneJ4300 = _JnxMidplaneJ4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 14)
)
_JnxMidplaneJ6300_ObjectIdentity = ObjectIdentity
jnxMidplaneJ6300 = _JnxMidplaneJ6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 15)
)
_JnxMidplaneIRM_ObjectIdentity = ObjectIdentity
jnxMidplaneIRM = _JnxMidplaneIRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 16)
)
_JnxMidplaneTX_ObjectIdentity = ObjectIdentity
jnxMidplaneTX = _JnxMidplaneTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 17)
)
_JnxMidplaneM120_ObjectIdentity = ObjectIdentity
jnxMidplaneM120 = _JnxMidplaneM120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 18)
)
_JnxMidplaneJ4350_ObjectIdentity = ObjectIdentity
jnxMidplaneJ4350 = _JnxMidplaneJ4350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 19)
)
_JnxMidplaneJ6350_ObjectIdentity = ObjectIdentity
jnxMidplaneJ6350 = _JnxMidplaneJ6350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 20)
)
_JnxMidplaneMX960_ObjectIdentity = ObjectIdentity
jnxMidplaneMX960 = _JnxMidplaneMX960_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 21)
)
_JnxMidplaneJ4320_ObjectIdentity = ObjectIdentity
jnxMidplaneJ4320 = _JnxMidplaneJ4320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 22)
)
_JnxMidplaneJ2320_ObjectIdentity = ObjectIdentity
jnxMidplaneJ2320 = _JnxMidplaneJ2320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 23)
)
_JnxMidplaneJ2350_ObjectIdentity = ObjectIdentity
jnxMidplaneJ2350 = _JnxMidplaneJ2350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 24)
)
_JnxMidplaneMX480_ObjectIdentity = ObjectIdentity
jnxMidplaneMX480 = _JnxMidplaneMX480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 25)
)
_JnxMidplaneSRX5800_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX5800 = _JnxMidplaneSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 26)
)
_JnxMidplaneT1600_ObjectIdentity = ObjectIdentity
jnxMidplaneT1600 = _JnxMidplaneT1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 27)
)
_JnxMidplaneSRX5600_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX5600 = _JnxMidplaneSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 28)
)
_JnxMidplaneMX240_ObjectIdentity = ObjectIdentity
jnxMidplaneMX240 = _JnxMidplaneMX240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 29)
)
_JnxBackplaneEX8208_ObjectIdentity = ObjectIdentity
jnxBackplaneEX8208 = _JnxBackplaneEX8208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 32)
)
_JnxMidplaneEX8216_ObjectIdentity = ObjectIdentity
jnxMidplaneEX8216 = _JnxMidplaneEX8216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 33)
)
_JnxMidplaneSRX3600_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX3600 = _JnxMidplaneSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 34)
)
_JnxMidplaneSRX3400_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX3400 = _JnxMidplaneSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 35)
)
_JnxMidplaneSRX210_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX210 = _JnxMidplaneSRX210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 36)
)
_JnxMidplaneTXP_ObjectIdentity = ObjectIdentity
jnxMidplaneTXP = _JnxMidplaneTXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 37)
)
_JnxMidplaneJCS_ObjectIdentity = ObjectIdentity
jnxMidplaneJCS = _JnxMidplaneJCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 38)
)
_JnxMidplaneSRX240_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX240 = _JnxMidplaneSRX240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 39)
)
_JnxMidplaneSRX650_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX650 = _JnxMidplaneSRX650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 40)
)
_JnxMidplaneSRX100_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX100 = _JnxMidplaneSRX100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 41)
)
_JnxMidplaneLN1000V_ObjectIdentity = ObjectIdentity
jnxMidplaneLN1000V = _JnxMidplaneLN1000V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 42)
)
_JnxMidplaneIBM4274M02J02M_ObjectIdentity = ObjectIdentity
jnxMidplaneIBM4274M02J02M = _JnxMidplaneIBM4274M02J02M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 46)
)
_JnxMidplaneIBM4274M06J06M_ObjectIdentity = ObjectIdentity
jnxMidplaneIBM4274M06J06M = _JnxMidplaneIBM4274M06J06M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 47)
)
_JnxMidplaneIBM4274M11J11M_ObjectIdentity = ObjectIdentity
jnxMidplaneIBM4274M11J11M = _JnxMidplaneIBM4274M11J11M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 48)
)
_JnxMidplaneSRX1400_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX1400 = _JnxMidplaneSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 49)
)
_JnxMidplaneIBM4274S58J58S_ObjectIdentity = ObjectIdentity
jnxMidplaneIBM4274S58J58S = _JnxMidplaneIBM4274S58J58S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 50)
)
_JnxMidplaneIBM4274S56J56S_ObjectIdentity = ObjectIdentity
jnxMidplaneIBM4274S56J56S = _JnxMidplaneIBM4274S56J56S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 51)
)
_JnxMidplaneIBM4274S36J36S_ObjectIdentity = ObjectIdentity
jnxMidplaneIBM4274S36J36S = _JnxMidplaneIBM4274S36J36S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 52)
)
_JnxMidplaneIBM4274S34J34S_ObjectIdentity = ObjectIdentity
jnxMidplaneIBM4274S34J34S = _JnxMidplaneIBM4274S34J34S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 53)
)
_JnxBackplaneIBM4274E08J08E_ObjectIdentity = ObjectIdentity
jnxBackplaneIBM4274E08J08E = _JnxBackplaneIBM4274E08J08E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 55)
)
_JnxMidplaneIBM4274E16J16E_ObjectIdentity = ObjectIdentity
jnxMidplaneIBM4274E16J16E = _JnxMidplaneIBM4274E16J16E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 56)
)
_JnxMidplaneMX80_ObjectIdentity = ObjectIdentity
jnxMidplaneMX80 = _JnxMidplaneMX80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 57)
)
_JnxMidplaneSRX220_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX220 = _JnxMidplaneSRX220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 58)
)
_JnxBackplaneEXXRE_ObjectIdentity = ObjectIdentity
jnxBackplaneEXXRE = _JnxBackplaneEXXRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 59)
)
_JnxMidplaneQFXInterconnect_ObjectIdentity = ObjectIdentity
jnxMidplaneQFXInterconnect = _JnxMidplaneQFXInterconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 60)
)
_JnxMidplaneSRX110_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX110 = _JnxMidplaneSRX110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 64)
)
_JnxMidplaneSRX120_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX120 = _JnxMidplaneSRX120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 65)
)
_JnxMidplaneMAG8600_ObjectIdentity = ObjectIdentity
jnxMidplaneMAG8600 = _JnxMidplaneMAG8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 66)
)
_JnxMidplaneMAG6611_ObjectIdentity = ObjectIdentity
jnxMidplaneMAG6611 = _JnxMidplaneMAG6611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 67)
)
_JnxMidplaneMAG6610_ObjectIdentity = ObjectIdentity
jnxMidplaneMAG6610 = _JnxMidplaneMAG6610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 68)
)
_JnxMidplanePTX5000_ObjectIdentity = ObjectIdentity
jnxMidplanePTX5000 = _JnxMidplanePTX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 69)
)
_JnxMidplaneIBMJ08F_ObjectIdentity = ObjectIdentity
jnxMidplaneIBMJ08F = _JnxMidplaneIBMJ08F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 72)
)
_JnxBackplaneEX6210_ObjectIdentity = ObjectIdentity
jnxBackplaneEX6210 = _JnxBackplaneEX6210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 74)
)
_JnxMidplaneDELLJSRX3600_ObjectIdentity = ObjectIdentity
jnxMidplaneDELLJSRX3600 = _JnxMidplaneDELLJSRX3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 77)
)
_JnxMidplaneDELLJSRX3400_ObjectIdentity = ObjectIdentity
jnxMidplaneDELLJSRX3400 = _JnxMidplaneDELLJSRX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 78)
)
_JnxMidplaneDELLJSRX1400_ObjectIdentity = ObjectIdentity
jnxMidplaneDELLJSRX1400 = _JnxMidplaneDELLJSRX1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 79)
)
_JnxMidplaneDELLJSRX5800_ObjectIdentity = ObjectIdentity
jnxMidplaneDELLJSRX5800 = _JnxMidplaneDELLJSRX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 80)
)
_JnxMidplaneDELLJSRX5600_ObjectIdentity = ObjectIdentity
jnxMidplaneDELLJSRX5600 = _JnxMidplaneDELLJSRX5600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 81)
)
_JnxMidplaneT4000_ObjectIdentity = ObjectIdentity
jnxMidplaneT4000 = _JnxMidplaneT4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 83)
)
_JnxMidplaneSRX550_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX550 = _JnxMidplaneSRX550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 86)
)
_JnxMidplaneACX_ObjectIdentity = ObjectIdentity
jnxMidplaneACX = _JnxMidplaneACX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 87)
)
_JnxMidplaneMX40_ObjectIdentity = ObjectIdentity
jnxMidplaneMX40 = _JnxMidplaneMX40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 88)
)
_JnxMidplaneMX10_ObjectIdentity = ObjectIdentity
jnxMidplaneMX10 = _JnxMidplaneMX10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 89)
)
_JnxMidplaneMX5_ObjectIdentity = ObjectIdentity
jnxMidplaneMX5 = _JnxMidplaneMX5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 90)
)
_JnxBackplaneMX2020_ObjectIdentity = ObjectIdentity
jnxBackplaneMX2020 = _JnxBackplaneMX2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 93)
)
_JnxBackplaneLowerMX2020_ObjectIdentity = ObjectIdentity
jnxBackplaneLowerMX2020 = _JnxBackplaneLowerMX2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 93, 1)
)
_JnxBackplaneUpperMX2020_ObjectIdentity = ObjectIdentity
jnxBackplaneUpperMX2020 = _JnxBackplaneUpperMX2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 93, 2)
)
_JnxBackplaneLowerPowerMX2020_ObjectIdentity = ObjectIdentity
jnxBackplaneLowerPowerMX2020 = _JnxBackplaneLowerPowerMX2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 93, 3)
)
_JnxBackplaneUpperPowerMX2020_ObjectIdentity = ObjectIdentity
jnxBackplaneUpperPowerMX2020 = _JnxBackplaneUpperPowerMX2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 93, 4)
)
_JnxMidplaneVseries_ObjectIdentity = ObjectIdentity
jnxMidplaneVseries = _JnxMidplaneVseries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 94)
)
_JnxMidplaneLN2600_ObjectIdentity = ObjectIdentity
jnxMidplaneLN2600 = _JnxMidplaneLN2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 95)
)
_JnxMidplaneFireflyPerimeter_ObjectIdentity = ObjectIdentity
jnxMidplaneFireflyPerimeter = _JnxMidplaneFireflyPerimeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 96)
)
_JnxMidplaneMX104_ObjectIdentity = ObjectIdentity
jnxMidplaneMX104 = _JnxMidplaneMX104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 97)
)
_JnxMidplanePTX3000_ObjectIdentity = ObjectIdentity
jnxMidplanePTX3000 = _JnxMidplanePTX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 98)
)
_JnxBackplaneMX2010_ObjectIdentity = ObjectIdentity
jnxBackplaneMX2010 = _JnxBackplaneMX2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 99)
)
_JnxBackplaneLowerMX2010_ObjectIdentity = ObjectIdentity
jnxBackplaneLowerMX2010 = _JnxBackplaneLowerMX2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 99, 1)
)
_JnxBackplaneUpperMX2010_ObjectIdentity = ObjectIdentity
jnxBackplaneUpperMX2010 = _JnxBackplaneUpperMX2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 99, 2)
)
_JnxBackplanePowerMX2010_ObjectIdentity = ObjectIdentity
jnxBackplanePowerMX2010 = _JnxBackplanePowerMX2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 99, 3)
)
_JnxMidplaneLN2800_ObjectIdentity = ObjectIdentity
jnxMidplaneLN2800 = _JnxMidplaneLN2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 101)
)
_JnxMidplaneEX9214_ObjectIdentity = ObjectIdentity
jnxMidplaneEX9214 = _JnxMidplaneEX9214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 102)
)
_JnxMidplaneEX9208_ObjectIdentity = ObjectIdentity
jnxMidplaneEX9208 = _JnxMidplaneEX9208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 103)
)
_JnxMidplaneEX9204_ObjectIdentity = ObjectIdentity
jnxMidplaneEX9204 = _JnxMidplaneEX9204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 104)
)
_JnxMidplaneSRX5400_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX5400 = _JnxMidplaneSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 105)
)
_JnxMidplaneIBM4274S54J54S_ObjectIdentity = ObjectIdentity
jnxMidplaneIBM4274S54J54S = _JnxMidplaneIBM4274S54J54S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 106)
)
_JnxMidplaneDELLJSRX5400_ObjectIdentity = ObjectIdentity
jnxMidplaneDELLJSRX5400 = _JnxMidplaneDELLJSRX5400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 107)
)
_JnxMidplaneVMX_ObjectIdentity = ObjectIdentity
jnxMidplaneVMX = _JnxMidplaneVMX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 108)
)
_JnxMidplaneVRR_ObjectIdentity = ObjectIdentity
jnxMidplaneVRR = _JnxMidplaneVRR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 110)
)
_JnxMidplaneACX1000_ObjectIdentity = ObjectIdentity
jnxMidplaneACX1000 = _JnxMidplaneACX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 113)
)
_JnxMidplaneACX2000_ObjectIdentity = ObjectIdentity
jnxMidplaneACX2000 = _JnxMidplaneACX2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 114)
)
_JnxMidplaneACX1100_ObjectIdentity = ObjectIdentity
jnxMidplaneACX1100 = _JnxMidplaneACX1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 115)
)
_JnxMidplaneACX2100_ObjectIdentity = ObjectIdentity
jnxMidplaneACX2100 = _JnxMidplaneACX2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 116)
)
_JnxMidplaneACX2200_ObjectIdentity = ObjectIdentity
jnxMidplaneACX2200 = _JnxMidplaneACX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 117)
)
_JnxMidplaneACX4000_ObjectIdentity = ObjectIdentity
jnxMidplaneACX4000 = _JnxMidplaneACX4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 118)
)
_JnxMidplaneACX500AC_ObjectIdentity = ObjectIdentity
jnxMidplaneACX500AC = _JnxMidplaneACX500AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 119)
)
_JnxMidplaneACX500DC_ObjectIdentity = ObjectIdentity
jnxMidplaneACX500DC = _JnxMidplaneACX500DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 120)
)
_JnxMidplaneACX500OAC_ObjectIdentity = ObjectIdentity
jnxMidplaneACX500OAC = _JnxMidplaneACX500OAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 121)
)
_JnxMidplaneACX500ODC_ObjectIdentity = ObjectIdentity
jnxMidplaneACX500ODC = _JnxMidplaneACX500ODC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 122)
)
_JnxMidplaneACX500OPOEAC_ObjectIdentity = ObjectIdentity
jnxMidplaneACX500OPOEAC = _JnxMidplaneACX500OPOEAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 123)
)
_JnxMidplaneACX500OPOEDC_ObjectIdentity = ObjectIdentity
jnxMidplaneACX500OPOEDC = _JnxMidplaneACX500OPOEDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 124)
)
_JnxMidplaneLN1000CC_ObjectIdentity = ObjectIdentity
jnxMidplaneLN1000CC = _JnxMidplaneLN1000CC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 128)
)
_JnxMidplaneVSRX_ObjectIdentity = ObjectIdentity
jnxMidplaneVSRX = _JnxMidplaneVSRX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 129)
)
_JnxMidplaneSRX300_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX300 = _JnxMidplaneSRX300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 133)
)
_JnxMidplaneSRX320_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX320 = _JnxMidplaneSRX320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 134)
)
_JnxMidplaneSRX340_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX340 = _JnxMidplaneSRX340_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 135)
)
_JnxMidplaneSRX345_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX345 = _JnxMidplaneSRX345_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 136)
)
_JnxMidplaneSRX1500_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX1500 = _JnxMidplaneSRX1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 137)
)
_JnxMidplaneSRX4100_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX4100 = _JnxMidplaneSRX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 142)
)
_JnxMidplaneSRX4200_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX4200 = _JnxMidplaneSRX4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 143)
)
_JnxMidplaneMX2008_ObjectIdentity = ObjectIdentity
jnxMidplaneMX2008 = _JnxMidplaneMX2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 145)
)
_JnxBackMidplaneMX2008_ObjectIdentity = ObjectIdentity
jnxBackMidplaneMX2008 = _JnxBackMidplaneMX2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 145, 1)
)
_JnxPowerMidplaneMX2008_ObjectIdentity = ObjectIdentity
jnxPowerMidplaneMX2008 = _JnxPowerMidplaneMX2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 145, 2)
)
_JnxMidplaneMXTSR80_ObjectIdentity = ObjectIdentity
jnxMidplaneMXTSR80 = _JnxMidplaneMXTSR80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 146)
)
_JnxMidplaneACX5448_ObjectIdentity = ObjectIdentity
jnxMidplaneACX5448 = _JnxMidplaneACX5448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 148)
)
_JnxMidplaneMX150_ObjectIdentity = ObjectIdentity
jnxMidplaneMX150 = _JnxMidplaneMX150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 152)
)
_JnxMidplaneJRR200_ObjectIdentity = ObjectIdentity
jnxMidplaneJRR200 = _JnxMidplaneJRR200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 157)
)
_JnxMidplaneACX5448M_ObjectIdentity = ObjectIdentity
jnxMidplaneACX5448M = _JnxMidplaneACX5448M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 158)
)
_JnxMidplaneACX5448D_ObjectIdentity = ObjectIdentity
jnxMidplaneACX5448D = _JnxMidplaneACX5448D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 159)
)
_JnxMidplaneACX710_ObjectIdentity = ObjectIdentity
jnxMidplaneACX710 = _JnxMidplaneACX710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 162)
)
_JnxMidplaneACX5800_ObjectIdentity = ObjectIdentity
jnxMidplaneACX5800 = _JnxMidplaneACX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 163)
)
_JnxMidplaneSRX380_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX380 = _JnxMidplaneSRX380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 164)
)
_JnxMidplaneR6675_ObjectIdentity = ObjectIdentity
jnxMidplaneR6675 = _JnxMidplaneR6675_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 166)
)
_JnxMidplaneSRX1600_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX1600 = _JnxMidplaneSRX1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 583)
)
_JnxMidplaneSRX2300_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX2300 = _JnxMidplaneSRX2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 584)
)
_JnxMidplaneSRX4300_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX4300 = _JnxMidplaneSRX4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 585)
)
_JnxMidplaneACX7332_ObjectIdentity = ObjectIdentity
jnxMidplaneACX7332 = _JnxMidplaneACX7332_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 586)
)
_JnxMidplaneACX7348_ObjectIdentity = ObjectIdentity
jnxMidplaneACX7348 = _JnxMidplaneACX7348_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 587)
)
_JnxMidplaneSRX4700_ObjectIdentity = ObjectIdentity
jnxMidplaneSRX4700 = _JnxMidplaneSRX4700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 1, 590)
)
_JnxModule_ObjectIdentity = ObjectIdentity
jnxModule = _JnxModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2)
)
_JnxModuleM40_ObjectIdentity = ObjectIdentity
jnxModuleM40 = _JnxModuleM40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1)
)
_JnxModuleSCB_ObjectIdentity = ObjectIdentity
jnxModuleSCB = _JnxModuleSCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1, 1)
)
_JnxModuleFPC_ObjectIdentity = ObjectIdentity
jnxModuleFPC = _JnxModuleFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1, 2)
)
_JnxCommonFPC_ObjectIdentity = ObjectIdentity
jnxCommonFPC = _JnxCommonFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1, 2, 1)
)
_JnxOc48FPC_ObjectIdentity = ObjectIdentity
jnxOc48FPC = _JnxOc48FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1, 2, 2)
)
_JnxModuleHostCtlr_ObjectIdentity = ObjectIdentity
jnxModuleHostCtlr = _JnxModuleHostCtlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1, 3)
)
_JnxHostCtlrMaxi_ObjectIdentity = ObjectIdentity
jnxHostCtlrMaxi = _JnxHostCtlrMaxi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1, 3, 1)
)
_JnxHostCtlrMini_ObjectIdentity = ObjectIdentity
jnxHostCtlrMini = _JnxHostCtlrMini_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1, 3, 2)
)
_JnxModulePowerSupply_ObjectIdentity = ObjectIdentity
jnxModulePowerSupply = _JnxModulePowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1, 4)
)
_JnxPowerSupplyAC_ObjectIdentity = ObjectIdentity
jnxPowerSupplyAC = _JnxPowerSupplyAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1, 4, 1)
)
_JnxPowerSupplyDC_ObjectIdentity = ObjectIdentity
jnxPowerSupplyDC = _JnxPowerSupplyDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1, 4, 2)
)
_JnxModuleCooling_ObjectIdentity = ObjectIdentity
jnxModuleCooling = _JnxModuleCooling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1, 5)
)
_JnxCoolingImpeller_ObjectIdentity = ObjectIdentity
jnxCoolingImpeller = _JnxCoolingImpeller_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1, 5, 1)
)
_JnxCoolingFan_ObjectIdentity = ObjectIdentity
jnxCoolingFan = _JnxCoolingFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1, 5, 2)
)
_JnxModuleFrontPanelDisplay_ObjectIdentity = ObjectIdentity
jnxModuleFrontPanelDisplay = _JnxModuleFrontPanelDisplay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1, 6)
)
_JnxModuleRoutingEngine_ObjectIdentity = ObjectIdentity
jnxModuleRoutingEngine = _JnxModuleRoutingEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 1, 7)
)
_JnxModuleM20_ObjectIdentity = ObjectIdentity
jnxModuleM20 = _JnxModuleM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 2)
)
_JnxM20FPC_ObjectIdentity = ObjectIdentity
jnxM20FPC = _JnxM20FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 2, 1)
)
_JnxM20SSB_ObjectIdentity = ObjectIdentity
jnxM20SSB = _JnxM20SSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 2, 2)
)
_JnxM20RE_ObjectIdentity = ObjectIdentity
jnxM20RE = _JnxM20RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 2, 3)
)
_JnxM20Power_ObjectIdentity = ObjectIdentity
jnxM20Power = _JnxM20Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 2, 4)
)
_JnxM20PowerAC_ObjectIdentity = ObjectIdentity
jnxM20PowerAC = _JnxM20PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 2, 4, 1)
)
_JnxM20PowerDC_ObjectIdentity = ObjectIdentity
jnxM20PowerDC = _JnxM20PowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 2, 4, 2)
)
_JnxM20Fan_ObjectIdentity = ObjectIdentity
jnxM20Fan = _JnxM20Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 2, 5)
)
_JnxM20FrontPanel_ObjectIdentity = ObjectIdentity
jnxM20FrontPanel = _JnxM20FrontPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 2, 6)
)
_JnxModuleM160_ObjectIdentity = ObjectIdentity
jnxModuleM160 = _JnxModuleM160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 3)
)
_JnxM160FPC_ObjectIdentity = ObjectIdentity
jnxM160FPC = _JnxM160FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 3, 1)
)
_JnxM160SFM_ObjectIdentity = ObjectIdentity
jnxM160SFM = _JnxM160SFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 3, 2)
)
_JnxM160HM_ObjectIdentity = ObjectIdentity
jnxM160HM = _JnxM160HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 3, 3)
)
_JnxM160PCG_ObjectIdentity = ObjectIdentity
jnxM160PCG = _JnxM160PCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 3, 4)
)
_JnxM160Power_ObjectIdentity = ObjectIdentity
jnxM160Power = _JnxM160Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 3, 5)
)
_JnxM160Fan_ObjectIdentity = ObjectIdentity
jnxM160Fan = _JnxM160Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 3, 6)
)
_JnxM160MCS_ObjectIdentity = ObjectIdentity
jnxM160MCS = _JnxM160MCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 3, 7)
)
_JnxM160FPM_ObjectIdentity = ObjectIdentity
jnxM160FPM = _JnxM160FPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 3, 8)
)
_JnxM160CIP_ObjectIdentity = ObjectIdentity
jnxM160CIP = _JnxM160CIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 3, 9)
)
_JnxModuleM10_ObjectIdentity = ObjectIdentity
jnxModuleM10 = _JnxModuleM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 4)
)
_JnxM10FPC_ObjectIdentity = ObjectIdentity
jnxM10FPC = _JnxM10FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 4, 1)
)
_JnxM10FEB_ObjectIdentity = ObjectIdentity
jnxM10FEB = _JnxM10FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 4, 2)
)
_JnxM10RE_ObjectIdentity = ObjectIdentity
jnxM10RE = _JnxM10RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 4, 3)
)
_JnxM10Power_ObjectIdentity = ObjectIdentity
jnxM10Power = _JnxM10Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 4, 4)
)
_JnxM10PowerAC_ObjectIdentity = ObjectIdentity
jnxM10PowerAC = _JnxM10PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 4, 4, 1)
)
_JnxM10PowerDC_ObjectIdentity = ObjectIdentity
jnxM10PowerDC = _JnxM10PowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 4, 4, 2)
)
_JnxM10Fan_ObjectIdentity = ObjectIdentity
jnxM10Fan = _JnxM10Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 4, 5)
)
_JnxModuleM5_ObjectIdentity = ObjectIdentity
jnxModuleM5 = _JnxModuleM5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 5)
)
_JnxM5FPC_ObjectIdentity = ObjectIdentity
jnxM5FPC = _JnxM5FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 5, 1)
)
_JnxM5FEB_ObjectIdentity = ObjectIdentity
jnxM5FEB = _JnxM5FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 5, 2)
)
_JnxM5RE_ObjectIdentity = ObjectIdentity
jnxM5RE = _JnxM5RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 5, 3)
)
_JnxM5Power_ObjectIdentity = ObjectIdentity
jnxM5Power = _JnxM5Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 5, 4)
)
_JnxM5PowerAC_ObjectIdentity = ObjectIdentity
jnxM5PowerAC = _JnxM5PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 5, 4, 1)
)
_JnxM5PowerDC_ObjectIdentity = ObjectIdentity
jnxM5PowerDC = _JnxM5PowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 5, 4, 2)
)
_JnxM5Fan_ObjectIdentity = ObjectIdentity
jnxM5Fan = _JnxM5Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 5, 5)
)
_JnxModuleT640_ObjectIdentity = ObjectIdentity
jnxModuleT640 = _JnxModuleT640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 6)
)
_JnxT640FPC_ObjectIdentity = ObjectIdentity
jnxT640FPC = _JnxT640FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 6, 1)
)
_JnxT640SIB_ObjectIdentity = ObjectIdentity
jnxT640SIB = _JnxT640SIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 6, 2)
)
_JnxT640HM_ObjectIdentity = ObjectIdentity
jnxT640HM = _JnxT640HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 6, 3)
)
_JnxT640SCG_ObjectIdentity = ObjectIdentity
jnxT640SCG = _JnxT640SCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 6, 4)
)
_JnxT640Power_ObjectIdentity = ObjectIdentity
jnxT640Power = _JnxT640Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 6, 5)
)
_JnxT640Fan_ObjectIdentity = ObjectIdentity
jnxT640Fan = _JnxT640Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 6, 6)
)
_JnxT640CB_ObjectIdentity = ObjectIdentity
jnxT640CB = _JnxT640CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 6, 7)
)
_JnxT640FPB_ObjectIdentity = ObjectIdentity
jnxT640FPB = _JnxT640FPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 6, 8)
)
_JnxT640CIP_ObjectIdentity = ObjectIdentity
jnxT640CIP = _JnxT640CIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 6, 9)
)
_JnxT640SPMB_ObjectIdentity = ObjectIdentity
jnxT640SPMB = _JnxT640SPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 6, 10)
)
_JnxModuleT320_ObjectIdentity = ObjectIdentity
jnxModuleT320 = _JnxModuleT320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 7)
)
_JnxT320FPC_ObjectIdentity = ObjectIdentity
jnxT320FPC = _JnxT320FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 7, 1)
)
_JnxT320SIB_ObjectIdentity = ObjectIdentity
jnxT320SIB = _JnxT320SIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 7, 2)
)
_JnxT320HM_ObjectIdentity = ObjectIdentity
jnxT320HM = _JnxT320HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 7, 3)
)
_JnxT320SCG_ObjectIdentity = ObjectIdentity
jnxT320SCG = _JnxT320SCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 7, 4)
)
_JnxT320Power_ObjectIdentity = ObjectIdentity
jnxT320Power = _JnxT320Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 7, 5)
)
_JnxT320Fan_ObjectIdentity = ObjectIdentity
jnxT320Fan = _JnxT320Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 7, 6)
)
_JnxT320CB_ObjectIdentity = ObjectIdentity
jnxT320CB = _JnxT320CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 7, 7)
)
_JnxT320FPB_ObjectIdentity = ObjectIdentity
jnxT320FPB = _JnxT320FPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 7, 8)
)
_JnxT320CIP_ObjectIdentity = ObjectIdentity
jnxT320CIP = _JnxT320CIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 7, 9)
)
_JnxT320SPMB_ObjectIdentity = ObjectIdentity
jnxT320SPMB = _JnxT320SPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 7, 10)
)
_JnxModuleM40e_ObjectIdentity = ObjectIdentity
jnxModuleM40e = _JnxModuleM40e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 8)
)
_JnxM40eFPC_ObjectIdentity = ObjectIdentity
jnxM40eFPC = _JnxM40eFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 8, 1)
)
_JnxM40eSFM_ObjectIdentity = ObjectIdentity
jnxM40eSFM = _JnxM40eSFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 8, 2)
)
_JnxM40eHM_ObjectIdentity = ObjectIdentity
jnxM40eHM = _JnxM40eHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 8, 3)
)
_JnxM40ePCG_ObjectIdentity = ObjectIdentity
jnxM40ePCG = _JnxM40ePCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 8, 4)
)
_JnxM40ePower_ObjectIdentity = ObjectIdentity
jnxM40ePower = _JnxM40ePower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 8, 5)
)
_JnxM40eFan_ObjectIdentity = ObjectIdentity
jnxM40eFan = _JnxM40eFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 8, 6)
)
_JnxM40eMCS_ObjectIdentity = ObjectIdentity
jnxM40eMCS = _JnxM40eMCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 8, 7)
)
_JnxM40eFPM_ObjectIdentity = ObjectIdentity
jnxM40eFPM = _JnxM40eFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 8, 8)
)
_JnxM40eCIP_ObjectIdentity = ObjectIdentity
jnxM40eCIP = _JnxM40eCIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 8, 9)
)
_JnxModuleM320_ObjectIdentity = ObjectIdentity
jnxModuleM320 = _JnxModuleM320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 9)
)
_JnxM320FPC_ObjectIdentity = ObjectIdentity
jnxM320FPC = _JnxM320FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 9, 1)
)
_JnxM320SIB_ObjectIdentity = ObjectIdentity
jnxM320SIB = _JnxM320SIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 9, 2)
)
_JnxM320HM_ObjectIdentity = ObjectIdentity
jnxM320HM = _JnxM320HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 9, 3)
)
_JnxM320Power_ObjectIdentity = ObjectIdentity
jnxM320Power = _JnxM320Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 9, 4)
)
_JnxM320Fan_ObjectIdentity = ObjectIdentity
jnxM320Fan = _JnxM320Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 9, 5)
)
_JnxM320CB_ObjectIdentity = ObjectIdentity
jnxM320CB = _JnxM320CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 9, 6)
)
_JnxM320FPB_ObjectIdentity = ObjectIdentity
jnxM320FPB = _JnxM320FPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 9, 7)
)
_JnxM320CIP_ObjectIdentity = ObjectIdentity
jnxM320CIP = _JnxM320CIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 9, 8)
)
_JnxModuleM7i_ObjectIdentity = ObjectIdentity
jnxModuleM7i = _JnxModuleM7i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 10)
)
_JnxM7iFPC_ObjectIdentity = ObjectIdentity
jnxM7iFPC = _JnxM7iFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 10, 1)
)
_JnxM7iCFEB_ObjectIdentity = ObjectIdentity
jnxM7iCFEB = _JnxM7iCFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 10, 2)
)
_JnxM7iRE_ObjectIdentity = ObjectIdentity
jnxM7iRE = _JnxM7iRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 10, 3)
)
_JnxM7iPower_ObjectIdentity = ObjectIdentity
jnxM7iPower = _JnxM7iPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 10, 4)
)
_JnxM7iPowerAC_ObjectIdentity = ObjectIdentity
jnxM7iPowerAC = _JnxM7iPowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 10, 4, 1)
)
_JnxM7iFan_ObjectIdentity = ObjectIdentity
jnxM7iFan = _JnxM7iFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 10, 5)
)
_JnxModuleM10i_ObjectIdentity = ObjectIdentity
jnxModuleM10i = _JnxModuleM10i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 11)
)
_JnxM10iFPC_ObjectIdentity = ObjectIdentity
jnxM10iFPC = _JnxM10iFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 11, 1)
)
_JnxM10iCFEB_ObjectIdentity = ObjectIdentity
jnxM10iCFEB = _JnxM10iCFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 11, 2)
)
_JnxM10iRE_ObjectIdentity = ObjectIdentity
jnxM10iRE = _JnxM10iRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 11, 3)
)
_JnxM10iPower_ObjectIdentity = ObjectIdentity
jnxM10iPower = _JnxM10iPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 11, 4)
)
_JnxM10iPowerAC_ObjectIdentity = ObjectIdentity
jnxM10iPowerAC = _JnxM10iPowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 11, 4, 1)
)
_JnxM10iFan_ObjectIdentity = ObjectIdentity
jnxM10iFan = _JnxM10iFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 11, 5)
)
_JnxM10iHCM_ObjectIdentity = ObjectIdentity
jnxM10iHCM = _JnxM10iHCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 11, 6)
)
_JnxModuleGeneric_ObjectIdentity = ObjectIdentity
jnxModuleGeneric = _JnxModuleGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12)
)
_JnxFPC_ObjectIdentity = ObjectIdentity
jnxFPC = _JnxFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12, 1)
)
_JnxCBD_ObjectIdentity = ObjectIdentity
jnxCBD = _JnxCBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12, 2)
)
_JnxHM_ObjectIdentity = ObjectIdentity
jnxHM = _JnxHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12, 3)
)
_JnxPCMCIACard_ObjectIdentity = ObjectIdentity
jnxPCMCIACard = _JnxPCMCIACard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12, 3, 1)
)
_JnxUSBHub_ObjectIdentity = ObjectIdentity
jnxUSBHub = _JnxUSBHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12, 3, 2)
)
_JnxRCompactFlash_ObjectIdentity = ObjectIdentity
jnxRCompactFlash = _JnxRCompactFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12, 3, 3)
)
_JnxPower_ObjectIdentity = ObjectIdentity
jnxPower = _JnxPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12, 4)
)
_JnxFan_ObjectIdentity = ObjectIdentity
jnxFan = _JnxFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12, 5)
)
_JnxFPB_ObjectIdentity = ObjectIdentity
jnxFPB = _JnxFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12, 6)
)
_JnxCIP_ObjectIdentity = ObjectIdentity
jnxCIP = _JnxCIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12, 7)
)
_JnxSIB_ObjectIdentity = ObjectIdentity
jnxSIB = _JnxSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12, 8)
)
_JnxSFB_ObjectIdentity = ObjectIdentity
jnxSFB = _JnxSFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12, 9)
)
_JnxFTC_ObjectIdentity = ObjectIdentity
jnxFTC = _JnxFTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12, 10)
)
_JnxFEB_ObjectIdentity = ObjectIdentity
jnxFEB = _JnxFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12, 11)
)
_JnxTIB_ObjectIdentity = ObjectIdentity
jnxTIB = _JnxTIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 12, 12)
)
_JnxModuleJ2300_ObjectIdentity = ObjectIdentity
jnxModuleJ2300 = _JnxModuleJ2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 13)
)
_JnxJ2300FPC_ObjectIdentity = ObjectIdentity
jnxJ2300FPC = _JnxJ2300FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 13, 1)
)
_JnxJ2300RE_ObjectIdentity = ObjectIdentity
jnxJ2300RE = _JnxJ2300RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 13, 2)
)
_JnxJ2300Fan_ObjectIdentity = ObjectIdentity
jnxJ2300Fan = _JnxJ2300Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 13, 3)
)
_JnxModuleJ4300_ObjectIdentity = ObjectIdentity
jnxModuleJ4300 = _JnxModuleJ4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 14)
)
_JnxJ4300FPC_ObjectIdentity = ObjectIdentity
jnxJ4300FPC = _JnxJ4300FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 14, 1)
)
_JnxJ4300RE_ObjectIdentity = ObjectIdentity
jnxJ4300RE = _JnxJ4300RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 14, 2)
)
_JnxJ4300Fan_ObjectIdentity = ObjectIdentity
jnxJ4300Fan = _JnxJ4300Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 14, 3)
)
_JnxModuleJ6300_ObjectIdentity = ObjectIdentity
jnxModuleJ6300 = _JnxModuleJ6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 15)
)
_JnxJ6300FPC_ObjectIdentity = ObjectIdentity
jnxJ6300FPC = _JnxJ6300FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 15, 1)
)
_JnxJ6300RE_ObjectIdentity = ObjectIdentity
jnxJ6300RE = _JnxJ6300RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 15, 2)
)
_JnxJ6300Fan_ObjectIdentity = ObjectIdentity
jnxJ6300Fan = _JnxJ6300Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 15, 3)
)
_JnxModuleIRM_ObjectIdentity = ObjectIdentity
jnxModuleIRM = _JnxModuleIRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 16)
)
_JnxIRMFPC_ObjectIdentity = ObjectIdentity
jnxIRMFPC = _JnxIRMFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 16, 1)
)
_JnxIRMCFEB_ObjectIdentity = ObjectIdentity
jnxIRMCFEB = _JnxIRMCFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 16, 2)
)
_JnxIRMRE_ObjectIdentity = ObjectIdentity
jnxIRMRE = _JnxIRMRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 16, 3)
)
_JnxIRMPower_ObjectIdentity = ObjectIdentity
jnxIRMPower = _JnxIRMPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 16, 4)
)
_JnxIRMPowerDC_ObjectIdentity = ObjectIdentity
jnxIRMPowerDC = _JnxIRMPowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 16, 4, 1)
)
_JnxModuleTX_ObjectIdentity = ObjectIdentity
jnxModuleTX = _JnxModuleTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 17)
)
_JnxTXSIB_ObjectIdentity = ObjectIdentity
jnxTXSIB = _JnxTXSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 17, 1)
)
_JnxTXHM_ObjectIdentity = ObjectIdentity
jnxTXHM = _JnxTXHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 17, 2)
)
_JnxTXPower_ObjectIdentity = ObjectIdentity
jnxTXPower = _JnxTXPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 17, 3)
)
_JnxTXFan_ObjectIdentity = ObjectIdentity
jnxTXFan = _JnxTXFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 17, 4)
)
_JnxTXCB_ObjectIdentity = ObjectIdentity
jnxTXCB = _JnxTXCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 17, 5)
)
_JnxTXFPB_ObjectIdentity = ObjectIdentity
jnxTXFPB = _JnxTXFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 17, 6)
)
_JnxTXCIP_ObjectIdentity = ObjectIdentity
jnxTXCIP = _JnxTXCIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 17, 7)
)
_JnxTXSPMB_ObjectIdentity = ObjectIdentity
jnxTXSPMB = _JnxTXSPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 17, 8)
)
_JnxTXLCC_ObjectIdentity = ObjectIdentity
jnxTXLCC = _JnxTXLCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 17, 9)
)
_JnxModuleM120_ObjectIdentity = ObjectIdentity
jnxModuleM120 = _JnxModuleM120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 18)
)
_JnxM120FEB_ObjectIdentity = ObjectIdentity
jnxM120FEB = _JnxM120FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 18, 1)
)
_JnxModuleJ4350_ObjectIdentity = ObjectIdentity
jnxModuleJ4350 = _JnxModuleJ4350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 19)
)
_JnxJ4350FPC_ObjectIdentity = ObjectIdentity
jnxJ4350FPC = _JnxJ4350FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 19, 1)
)
_JnxJ4350RE_ObjectIdentity = ObjectIdentity
jnxJ4350RE = _JnxJ4350RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 19, 2)
)
_JnxJ4350Power_ObjectIdentity = ObjectIdentity
jnxJ4350Power = _JnxJ4350Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 19, 3)
)
_JnxJ4350Fan_ObjectIdentity = ObjectIdentity
jnxJ4350Fan = _JnxJ4350Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 19, 4)
)
_JnxModuleJ6350_ObjectIdentity = ObjectIdentity
jnxModuleJ6350 = _JnxModuleJ6350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 20)
)
_JnxJ6350FPC_ObjectIdentity = ObjectIdentity
jnxJ6350FPC = _JnxJ6350FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 20, 1)
)
_JnxJ6350RE_ObjectIdentity = ObjectIdentity
jnxJ6350RE = _JnxJ6350RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 20, 2)
)
_JnxJ6350Power_ObjectIdentity = ObjectIdentity
jnxJ6350Power = _JnxJ6350Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 20, 3)
)
_JnxJ6350Fan_ObjectIdentity = ObjectIdentity
jnxJ6350Fan = _JnxJ6350Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 20, 4)
)
_JnxModuleJ4320_ObjectIdentity = ObjectIdentity
jnxModuleJ4320 = _JnxModuleJ4320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 22)
)
_JnxJ4320FPC_ObjectIdentity = ObjectIdentity
jnxJ4320FPC = _JnxJ4320FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 22, 1)
)
_JnxJ4320RE_ObjectIdentity = ObjectIdentity
jnxJ4320RE = _JnxJ4320RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 22, 2)
)
_JnxModuleJ2320_ObjectIdentity = ObjectIdentity
jnxModuleJ2320 = _JnxModuleJ2320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 23)
)
_JnxJ2320FPC_ObjectIdentity = ObjectIdentity
jnxJ2320FPC = _JnxJ2320FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 23, 1)
)
_JnxJ2320RE_ObjectIdentity = ObjectIdentity
jnxJ2320RE = _JnxJ2320RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 23, 2)
)
_JnxJ2320Power_ObjectIdentity = ObjectIdentity
jnxJ2320Power = _JnxJ2320Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 23, 3)
)
_JnxJ2320Fan_ObjectIdentity = ObjectIdentity
jnxJ2320Fan = _JnxJ2320Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 23, 4)
)
_JnxModuleJ2350_ObjectIdentity = ObjectIdentity
jnxModuleJ2350 = _JnxModuleJ2350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 24)
)
_JnxJ2350FPC_ObjectIdentity = ObjectIdentity
jnxJ2350FPC = _JnxJ2350FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 24, 1)
)
_JnxJ2350RE_ObjectIdentity = ObjectIdentity
jnxJ2350RE = _JnxJ2350RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 24, 2)
)
_JnxJ2350Power_ObjectIdentity = ObjectIdentity
jnxJ2350Power = _JnxJ2350Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 24, 3)
)
_JnxJ2350Fan_ObjectIdentity = ObjectIdentity
jnxJ2350Fan = _JnxJ2350Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 24, 4)
)
_JnxModuleT1600_ObjectIdentity = ObjectIdentity
jnxModuleT1600 = _JnxModuleT1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 27)
)
_JnxT1600FPC_ObjectIdentity = ObjectIdentity
jnxT1600FPC = _JnxT1600FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 27, 1)
)
_JnxT1600SIB_ObjectIdentity = ObjectIdentity
jnxT1600SIB = _JnxT1600SIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 27, 2)
)
_JnxT1600HM_ObjectIdentity = ObjectIdentity
jnxT1600HM = _JnxT1600HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 27, 3)
)
_JnxT1600SCG_ObjectIdentity = ObjectIdentity
jnxT1600SCG = _JnxT1600SCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 27, 4)
)
_JnxT1600Power_ObjectIdentity = ObjectIdentity
jnxT1600Power = _JnxT1600Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 27, 5)
)
_JnxT1600Fan_ObjectIdentity = ObjectIdentity
jnxT1600Fan = _JnxT1600Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 27, 6)
)
_JnxT1600CB_ObjectIdentity = ObjectIdentity
jnxT1600CB = _JnxT1600CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 27, 7)
)
_JnxT1600FPB_ObjectIdentity = ObjectIdentity
jnxT1600FPB = _JnxT1600FPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 27, 8)
)
_JnxT1600CIP_ObjectIdentity = ObjectIdentity
jnxT1600CIP = _JnxT1600CIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 27, 9)
)
_JnxT1600SPMB_ObjectIdentity = ObjectIdentity
jnxT1600SPMB = _JnxT1600SPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 27, 10)
)
_JnxModuleEX3200_ObjectIdentity = ObjectIdentity
jnxModuleEX3200 = _JnxModuleEX3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 30)
)
_JnxEX3200FPC_ObjectIdentity = ObjectIdentity
jnxEX3200FPC = _JnxEX3200FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 30, 1)
)
_JnxEX3200Power_ObjectIdentity = ObjectIdentity
jnxEX3200Power = _JnxEX3200Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 30, 1, 1)
)
_JnxEX3200Fan_ObjectIdentity = ObjectIdentity
jnxEX3200Fan = _JnxEX3200Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 30, 1, 2)
)
_JnxEX3200RE_ObjectIdentity = ObjectIdentity
jnxEX3200RE = _JnxEX3200RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 30, 1, 3)
)
_JnxModuleEX4200_ObjectIdentity = ObjectIdentity
jnxModuleEX4200 = _JnxModuleEX4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 31)
)
_JnxEX4200FPC_ObjectIdentity = ObjectIdentity
jnxEX4200FPC = _JnxEX4200FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 31, 1)
)
_JnxEX4200Power_ObjectIdentity = ObjectIdentity
jnxEX4200Power = _JnxEX4200Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 31, 1, 1)
)
_JnxEX4200Fan_ObjectIdentity = ObjectIdentity
jnxEX4200Fan = _JnxEX4200Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 31, 1, 2)
)
_JnxModuleSRX210_ObjectIdentity = ObjectIdentity
jnxModuleSRX210 = _JnxModuleSRX210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 36)
)
_JnxSRX210FPC_ObjectIdentity = ObjectIdentity
jnxSRX210FPC = _JnxSRX210FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 36, 1)
)
_JnxSRX210RE_ObjectIdentity = ObjectIdentity
jnxSRX210RE = _JnxSRX210RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 36, 2)
)
_JnxSRX210Power_ObjectIdentity = ObjectIdentity
jnxSRX210Power = _JnxSRX210Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 36, 3)
)
_JnxSRX210Fan_ObjectIdentity = ObjectIdentity
jnxSRX210Fan = _JnxSRX210Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 36, 4)
)
_JnxModuleTXP_ObjectIdentity = ObjectIdentity
jnxModuleTXP = _JnxModuleTXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 37)
)
_JnxTXPSIB_ObjectIdentity = ObjectIdentity
jnxTXPSIB = _JnxTXPSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 37, 1)
)
_JnxTXPHM_ObjectIdentity = ObjectIdentity
jnxTXPHM = _JnxTXPHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 37, 2)
)
_JnxTXPPower_ObjectIdentity = ObjectIdentity
jnxTXPPower = _JnxTXPPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 37, 3)
)
_JnxTXPFan_ObjectIdentity = ObjectIdentity
jnxTXPFan = _JnxTXPFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 37, 4)
)
_JnxTXPCB_ObjectIdentity = ObjectIdentity
jnxTXPCB = _JnxTXPCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 37, 5)
)
_JnxTXPFPB_ObjectIdentity = ObjectIdentity
jnxTXPFPB = _JnxTXPFPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 37, 6)
)
_JnxTXPCIP_ObjectIdentity = ObjectIdentity
jnxTXPCIP = _JnxTXPCIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 37, 7)
)
_JnxTXPSPMB_ObjectIdentity = ObjectIdentity
jnxTXPSPMB = _JnxTXPSPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 37, 8)
)
_JnxTXPLCC_ObjectIdentity = ObjectIdentity
jnxTXPLCC = _JnxTXPLCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 37, 9)
)
_JnxTXPSFC_ObjectIdentity = ObjectIdentity
jnxTXPSFC = _JnxTXPSFC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 37, 10)
)
_JnxModuleJCS_ObjectIdentity = ObjectIdentity
jnxModuleJCS = _JnxModuleJCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 38)
)
_JnxJCSHM_ObjectIdentity = ObjectIdentity
jnxJCSHM = _JnxJCSHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 38, 1)
)
_JnxJCSBBD_ObjectIdentity = ObjectIdentity
jnxJCSBBD = _JnxJCSBBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 38, 1, 1)
)
_JnxJCSFPC_ObjectIdentity = ObjectIdentity
jnxJCSFPC = _JnxJCSFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 38, 2)
)
_JnxJCSPIC_ObjectIdentity = ObjectIdentity
jnxJCSPIC = _JnxJCSPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 38, 3)
)
_JnxModuleSRX240_ObjectIdentity = ObjectIdentity
jnxModuleSRX240 = _JnxModuleSRX240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 39)
)
_JnxSRX240FPC_ObjectIdentity = ObjectIdentity
jnxSRX240FPC = _JnxSRX240FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 39, 1)
)
_JnxSRX240RE_ObjectIdentity = ObjectIdentity
jnxSRX240RE = _JnxSRX240RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 39, 2)
)
_JnxSRX240Power_ObjectIdentity = ObjectIdentity
jnxSRX240Power = _JnxSRX240Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 39, 3)
)
_JnxSRX240Fan_ObjectIdentity = ObjectIdentity
jnxSRX240Fan = _JnxSRX240Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 39, 4)
)
_JnxModuleSRX650_ObjectIdentity = ObjectIdentity
jnxModuleSRX650 = _JnxModuleSRX650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 40)
)
_JnxSRX650FPC_ObjectIdentity = ObjectIdentity
jnxSRX650FPC = _JnxSRX650FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 40, 1)
)
_JnxSRX650RE_ObjectIdentity = ObjectIdentity
jnxSRX650RE = _JnxSRX650RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 40, 2)
)
_JnxSRX650Power_ObjectIdentity = ObjectIdentity
jnxSRX650Power = _JnxSRX650Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 40, 3)
)
_JnxSRX650Fan_ObjectIdentity = ObjectIdentity
jnxSRX650Fan = _JnxSRX650Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 40, 4)
)
_JnxModuleSRX100_ObjectIdentity = ObjectIdentity
jnxModuleSRX100 = _JnxModuleSRX100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 41)
)
_JnxSRX100FPC_ObjectIdentity = ObjectIdentity
jnxSRX100FPC = _JnxSRX100FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 41, 1)
)
_JnxSRX100RE_ObjectIdentity = ObjectIdentity
jnxSRX100RE = _JnxSRX100RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 41, 2)
)
_JnxSRX100Power_ObjectIdentity = ObjectIdentity
jnxSRX100Power = _JnxSRX100Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 41, 3)
)
_JnxSRX100Fan_ObjectIdentity = ObjectIdentity
jnxSRX100Fan = _JnxSRX100Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 41, 4)
)
_JnxModuleEX2200_ObjectIdentity = ObjectIdentity
jnxModuleEX2200 = _JnxModuleEX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 43)
)
_JnxEX2200FPC_ObjectIdentity = ObjectIdentity
jnxEX2200FPC = _JnxEX2200FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 43, 1)
)
_JnxEX2200Power_ObjectIdentity = ObjectIdentity
jnxEX2200Power = _JnxEX2200Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 43, 1, 1)
)
_JnxEX2200Fan_ObjectIdentity = ObjectIdentity
jnxEX2200Fan = _JnxEX2200Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 43, 1, 2)
)
_JnxEX2200RE_ObjectIdentity = ObjectIdentity
jnxEX2200RE = _JnxEX2200RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 43, 1, 3)
)
_JnxModuleEX4500_ObjectIdentity = ObjectIdentity
jnxModuleEX4500 = _JnxModuleEX4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 44)
)
_JnxEX4500FPC_ObjectIdentity = ObjectIdentity
jnxEX4500FPC = _JnxEX4500FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 44, 1)
)
_JnxEX4500Power_ObjectIdentity = ObjectIdentity
jnxEX4500Power = _JnxEX4500Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 44, 1, 1)
)
_JnxEX4500Fan_ObjectIdentity = ObjectIdentity
jnxEX4500Fan = _JnxEX4500Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 44, 1, 2)
)
_JnxEX4500RE_ObjectIdentity = ObjectIdentity
jnxEX4500RE = _JnxEX4500RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 44, 1, 3)
)
_JnxModuleIBM427348EJ48E_ObjectIdentity = ObjectIdentity
jnxModuleIBM427348EJ48E = _JnxModuleIBM427348EJ48E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 54)
)
_JnxIBM427348EJ48EFPC_ObjectIdentity = ObjectIdentity
jnxIBM427348EJ48EFPC = _JnxIBM427348EJ48EFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 54, 1)
)
_JnxIBM427348EJ48EPower_ObjectIdentity = ObjectIdentity
jnxIBM427348EJ48EPower = _JnxIBM427348EJ48EPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 54, 1, 1)
)
_JnxIBM427348EJ48EFan_ObjectIdentity = ObjectIdentity
jnxIBM427348EJ48EFan = _JnxIBM427348EJ48EFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 54, 1, 2)
)
_JnxModuleMX80_ObjectIdentity = ObjectIdentity
jnxModuleMX80 = _JnxModuleMX80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 57)
)
_JnxMX80FPC_ObjectIdentity = ObjectIdentity
jnxMX80FPC = _JnxMX80FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 57, 1)
)
_JnxMX80CFEB_ObjectIdentity = ObjectIdentity
jnxMX80CFEB = _JnxMX80CFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 57, 2)
)
_JnxMX80RE_ObjectIdentity = ObjectIdentity
jnxMX80RE = _JnxMX80RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 57, 3)
)
_JnxMX80Power_ObjectIdentity = ObjectIdentity
jnxMX80Power = _JnxMX80Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 57, 4)
)
_JnxMX80PowerAC_ObjectIdentity = ObjectIdentity
jnxMX80PowerAC = _JnxMX80PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 57, 5)
)
_JnxMX80Fan_ObjectIdentity = ObjectIdentity
jnxMX80Fan = _JnxMX80Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 57, 6)
)
_JnxModuleSRX220_ObjectIdentity = ObjectIdentity
jnxModuleSRX220 = _JnxModuleSRX220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 58)
)
_JnxSRX220FPC_ObjectIdentity = ObjectIdentity
jnxSRX220FPC = _JnxSRX220FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 58, 1)
)
_JnxSRX220RE_ObjectIdentity = ObjectIdentity
jnxSRX220RE = _JnxSRX220RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 58, 2)
)
_JnxSRX220Power_ObjectIdentity = ObjectIdentity
jnxSRX220Power = _JnxSRX220Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 58, 3)
)
_JnxSRX220Fan_ObjectIdentity = ObjectIdentity
jnxSRX220Fan = _JnxSRX220Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 58, 4)
)
_JnxModuleEXXRE_ObjectIdentity = ObjectIdentity
jnxModuleEXXRE = _JnxModuleEXXRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 59)
)
_JnxEXXREPower_ObjectIdentity = ObjectIdentity
jnxEXXREPower = _JnxEXXREPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 59, 1)
)
_JnxEXXREFan_ObjectIdentity = ObjectIdentity
jnxEXXREFan = _JnxEXXREFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 59, 2)
)
_JnxEXXREHM_ObjectIdentity = ObjectIdentity
jnxEXXREHM = _JnxEXXREHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 59, 3)
)
_JnxEXXRELCC_ObjectIdentity = ObjectIdentity
jnxEXXRELCC = _JnxEXXRELCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 59, 4)
)
_JnxModuleEX4300_ObjectIdentity = ObjectIdentity
jnxModuleEX4300 = _JnxModuleEX4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 63)
)
_JnxEX4300FPC_ObjectIdentity = ObjectIdentity
jnxEX4300FPC = _JnxEX4300FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 63, 1)
)
_JnxEX4300Power_ObjectIdentity = ObjectIdentity
jnxEX4300Power = _JnxEX4300Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 63, 1, 1)
)
_JnxEX4300Fan_ObjectIdentity = ObjectIdentity
jnxEX4300Fan = _JnxEX4300Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 63, 1, 2)
)
_JnxModuleSRX110_ObjectIdentity = ObjectIdentity
jnxModuleSRX110 = _JnxModuleSRX110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 64)
)
_JnxSRX110FPC_ObjectIdentity = ObjectIdentity
jnxSRX110FPC = _JnxSRX110FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 64, 1)
)
_JnxSRX110RE_ObjectIdentity = ObjectIdentity
jnxSRX110RE = _JnxSRX110RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 64, 2)
)
_JnxSRX110Power_ObjectIdentity = ObjectIdentity
jnxSRX110Power = _JnxSRX110Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 64, 3)
)
_JnxSRX110Fan_ObjectIdentity = ObjectIdentity
jnxSRX110Fan = _JnxSRX110Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 64, 4)
)
_JnxModuleSRX120_ObjectIdentity = ObjectIdentity
jnxModuleSRX120 = _JnxModuleSRX120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 65)
)
_JnxSRX120FPC_ObjectIdentity = ObjectIdentity
jnxSRX120FPC = _JnxSRX120FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 65, 1)
)
_JnxSRX120RE_ObjectIdentity = ObjectIdentity
jnxSRX120RE = _JnxSRX120RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 65, 2)
)
_JnxSRX120Power_ObjectIdentity = ObjectIdentity
jnxSRX120Power = _JnxSRX120Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 65, 3)
)
_JnxSRX120Fan_ObjectIdentity = ObjectIdentity
jnxSRX120Fan = _JnxSRX120Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 65, 4)
)
_JnxModulePTX5000_ObjectIdentity = ObjectIdentity
jnxModulePTX5000 = _JnxModulePTX5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 69)
)
_JnxPTX5000SIB_ObjectIdentity = ObjectIdentity
jnxPTX5000SIB = _JnxPTX5000SIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 69, 1)
)
_JnxPTX5000HM_ObjectIdentity = ObjectIdentity
jnxPTX5000HM = _JnxPTX5000HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 69, 2)
)
_JnxPTX5000FPC_ObjectIdentity = ObjectIdentity
jnxPTX5000FPC = _JnxPTX5000FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 69, 3)
)
_JnxPTX5000Fan_ObjectIdentity = ObjectIdentity
jnxPTX5000Fan = _JnxPTX5000Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 69, 4)
)
_JnxPTX5000CB_ObjectIdentity = ObjectIdentity
jnxPTX5000CB = _JnxPTX5000CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 69, 5)
)
_JnxPTX5000FPB_ObjectIdentity = ObjectIdentity
jnxPTX5000FPB = _JnxPTX5000FPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 69, 6)
)
_JnxPTX5000SPMB_ObjectIdentity = ObjectIdentity
jnxPTX5000SPMB = _JnxPTX5000SPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 69, 7)
)
_JnxPTX5000PDU_ObjectIdentity = ObjectIdentity
jnxPTX5000PDU = _JnxPTX5000PDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 69, 8)
)
_JnxPTX5000PSM_ObjectIdentity = ObjectIdentity
jnxPTX5000PSM = _JnxPTX5000PSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 69, 9)
)
_JnxPTX5000CCG_ObjectIdentity = ObjectIdentity
jnxPTX5000CCG = _JnxPTX5000CCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 69, 10)
)
_JnxPTX5000PIC_ObjectIdentity = ObjectIdentity
jnxPTX5000PIC = _JnxPTX5000PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 69, 11)
)
_JnxModuleIBM0719J45E_ObjectIdentity = ObjectIdentity
jnxModuleIBM0719J45E = _JnxModuleIBM0719J45E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 71)
)
_JnxIBM0719J45EFPC_ObjectIdentity = ObjectIdentity
jnxIBM0719J45EFPC = _JnxIBM0719J45EFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 71, 1)
)
_JnxIBM0719J45EPower_ObjectIdentity = ObjectIdentity
jnxIBM0719J45EPower = _JnxIBM0719J45EPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 71, 1, 1)
)
_JnxIBM0719J45EFan_ObjectIdentity = ObjectIdentity
jnxIBM0719J45EFan = _JnxIBM0719J45EFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 71, 1, 2)
)
_JnxIBM0719J45ERE_ObjectIdentity = ObjectIdentity
jnxIBM0719J45ERE = _JnxIBM0719J45ERE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 71, 1, 3)
)
_JnxModuleEX3300_ObjectIdentity = ObjectIdentity
jnxModuleEX3300 = _JnxModuleEX3300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 76)
)
_JnxEX3300FPC_ObjectIdentity = ObjectIdentity
jnxEX3300FPC = _JnxEX3300FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 76, 1)
)
_JnxEX3300Power_ObjectIdentity = ObjectIdentity
jnxEX3300Power = _JnxEX3300Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 76, 1, 1)
)
_JnxEX3300Fan_ObjectIdentity = ObjectIdentity
jnxEX3300Fan = _JnxEX3300Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 76, 1, 2)
)
_JnxEX3300RE_ObjectIdentity = ObjectIdentity
jnxEX3300RE = _JnxEX3300RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 76, 1, 3)
)
_JnxModuleT4000_ObjectIdentity = ObjectIdentity
jnxModuleT4000 = _JnxModuleT4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 83)
)
_JnxT4000SIB_ObjectIdentity = ObjectIdentity
jnxT4000SIB = _JnxT4000SIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 83, 1)
)
_JnxT4000SCG_ObjectIdentity = ObjectIdentity
jnxT4000SCG = _JnxT4000SCG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 83, 2)
)
_JnxT4000CB_ObjectIdentity = ObjectIdentity
jnxT4000CB = _JnxT4000CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 83, 3)
)
_JnxT4000SPMB_ObjectIdentity = ObjectIdentity
jnxT4000SPMB = _JnxT4000SPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 83, 4)
)
_JnxModuleSRX550_ObjectIdentity = ObjectIdentity
jnxModuleSRX550 = _JnxModuleSRX550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 86)
)
_JnxSRX550FPC_ObjectIdentity = ObjectIdentity
jnxSRX550FPC = _JnxSRX550FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 86, 1)
)
_JnxSRX550RE_ObjectIdentity = ObjectIdentity
jnxSRX550RE = _JnxSRX550RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 86, 2)
)
_JnxSRX550Power_ObjectIdentity = ObjectIdentity
jnxSRX550Power = _JnxSRX550Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 86, 3)
)
_JnxSRX550Fan_ObjectIdentity = ObjectIdentity
jnxSRX550Fan = _JnxSRX550Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 86, 4)
)
_JnxModuleACX_ObjectIdentity = ObjectIdentity
jnxModuleACX = _JnxModuleACX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 87)
)
_JnxACXFPC_ObjectIdentity = ObjectIdentity
jnxACXFPC = _JnxACXFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 87, 1)
)
_JnxACXFEB_ObjectIdentity = ObjectIdentity
jnxACXFEB = _JnxACXFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 87, 2)
)
_JnxACXRE_ObjectIdentity = ObjectIdentity
jnxACXRE = _JnxACXRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 87, 3)
)
_JnxACXPower_ObjectIdentity = ObjectIdentity
jnxACXPower = _JnxACXPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 87, 4)
)
_JnxACXPowerDC_ObjectIdentity = ObjectIdentity
jnxACXPowerDC = _JnxACXPowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 87, 4, 1)
)
_JnxACXPowerAC_ObjectIdentity = ObjectIdentity
jnxACXPowerAC = _JnxACXPowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 87, 4, 2)
)
_JnxACXFan_ObjectIdentity = ObjectIdentity
jnxACXFan = _JnxACXFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 87, 5)
)
_JnxModuleMX40_ObjectIdentity = ObjectIdentity
jnxModuleMX40 = _JnxModuleMX40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 88)
)
_JnxMX40FPC_ObjectIdentity = ObjectIdentity
jnxMX40FPC = _JnxMX40FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 88, 1)
)
_JnxMX40CFEB_ObjectIdentity = ObjectIdentity
jnxMX40CFEB = _JnxMX40CFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 88, 2)
)
_JnxMX40RE_ObjectIdentity = ObjectIdentity
jnxMX40RE = _JnxMX40RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 88, 3)
)
_JnxMX40Power_ObjectIdentity = ObjectIdentity
jnxMX40Power = _JnxMX40Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 88, 4)
)
_JnxMX40PowerAC_ObjectIdentity = ObjectIdentity
jnxMX40PowerAC = _JnxMX40PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 88, 5)
)
_JnxMX40Fan_ObjectIdentity = ObjectIdentity
jnxMX40Fan = _JnxMX40Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 88, 6)
)
_JnxModuleMX10_ObjectIdentity = ObjectIdentity
jnxModuleMX10 = _JnxModuleMX10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 89)
)
_JnxMX10FPC_ObjectIdentity = ObjectIdentity
jnxMX10FPC = _JnxMX10FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 89, 1)
)
_JnxMX10CFEB_ObjectIdentity = ObjectIdentity
jnxMX10CFEB = _JnxMX10CFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 89, 2)
)
_JnxMX10RE_ObjectIdentity = ObjectIdentity
jnxMX10RE = _JnxMX10RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 89, 3)
)
_JnxMX10Power_ObjectIdentity = ObjectIdentity
jnxMX10Power = _JnxMX10Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 89, 4)
)
_JnxMX10PowerAC_ObjectIdentity = ObjectIdentity
jnxMX10PowerAC = _JnxMX10PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 89, 5)
)
_JnxMX10Fan_ObjectIdentity = ObjectIdentity
jnxMX10Fan = _JnxMX10Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 89, 6)
)
_JnxModuleMX5_ObjectIdentity = ObjectIdentity
jnxModuleMX5 = _JnxModuleMX5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 90)
)
_JnxMX5FPC_ObjectIdentity = ObjectIdentity
jnxMX5FPC = _JnxMX5FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 90, 1)
)
_JnxMX5CFEB_ObjectIdentity = ObjectIdentity
jnxMX5CFEB = _JnxMX5CFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 90, 2)
)
_JnxMX5RE_ObjectIdentity = ObjectIdentity
jnxMX5RE = _JnxMX5RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 90, 3)
)
_JnxMX5Power_ObjectIdentity = ObjectIdentity
jnxMX5Power = _JnxMX5Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 90, 4)
)
_JnxMX5PowerAC_ObjectIdentity = ObjectIdentity
jnxMX5PowerAC = _JnxMX5PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 90, 5)
)
_JnxMX5Fan_ObjectIdentity = ObjectIdentity
jnxMX5Fan = _JnxMX5Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 90, 6)
)
_JnxModuleEX4550_ObjectIdentity = ObjectIdentity
jnxModuleEX4550 = _JnxModuleEX4550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 92)
)
_JnxEX4550FPC_ObjectIdentity = ObjectIdentity
jnxEX4550FPC = _JnxEX4550FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 92, 1)
)
_JnxEX4550Power_ObjectIdentity = ObjectIdentity
jnxEX4550Power = _JnxEX4550Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 92, 1, 1)
)
_JnxEX4550Fan_ObjectIdentity = ObjectIdentity
jnxEX4550Fan = _JnxEX4550Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 92, 1, 2)
)
_JnxEX4550RE_ObjectIdentity = ObjectIdentity
jnxEX4550RE = _JnxEX4550RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 92, 1, 3)
)
_JnxModuleMX2020_ObjectIdentity = ObjectIdentity
jnxModuleMX2020 = _JnxModuleMX2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 93)
)
_JnxMX2020SFB_ObjectIdentity = ObjectIdentity
jnxMX2020SFB = _JnxMX2020SFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 93, 1)
)
_JnxMX2020HM_ObjectIdentity = ObjectIdentity
jnxMX2020HM = _JnxMX2020HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 93, 2)
)
_JnxMX2020FPC_ObjectIdentity = ObjectIdentity
jnxMX2020FPC = _JnxMX2020FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 93, 3)
)
_JnxMX2020Fan_ObjectIdentity = ObjectIdentity
jnxMX2020Fan = _JnxMX2020Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 93, 4)
)
_JnxMX2020CB_ObjectIdentity = ObjectIdentity
jnxMX2020CB = _JnxMX2020CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 93, 5)
)
_JnxMX2020FPB_ObjectIdentity = ObjectIdentity
jnxMX2020FPB = _JnxMX2020FPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 93, 6)
)
_JnxMX2020SPMB_ObjectIdentity = ObjectIdentity
jnxMX2020SPMB = _JnxMX2020SPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 93, 7)
)
_JnxMX2020PDM_ObjectIdentity = ObjectIdentity
jnxMX2020PDM = _JnxMX2020PDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 93, 8)
)
_JnxMX2020PSM_ObjectIdentity = ObjectIdentity
jnxMX2020PSM = _JnxMX2020PSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 93, 9)
)
_JnxMX2020ADC_ObjectIdentity = ObjectIdentity
jnxMX2020ADC = _JnxMX2020ADC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 93, 10)
)
_JnxModuleVseries_ObjectIdentity = ObjectIdentity
jnxModuleVseries = _JnxModuleVseries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 94)
)
_JnxVseriesFPC_ObjectIdentity = ObjectIdentity
jnxVseriesFPC = _JnxVseriesFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 94, 1)
)
_JnxVseriesRE_ObjectIdentity = ObjectIdentity
jnxVseriesRE = _JnxVseriesRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 94, 2)
)
_JnxVseriesPower_ObjectIdentity = ObjectIdentity
jnxVseriesPower = _JnxVseriesPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 94, 3)
)
_JnxVseriesFan_ObjectIdentity = ObjectIdentity
jnxVseriesFan = _JnxVseriesFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 94, 4)
)
_JnxModuleFireflyPerimeter_ObjectIdentity = ObjectIdentity
jnxModuleFireflyPerimeter = _JnxModuleFireflyPerimeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 96)
)
_JnxFireflyPerimeterFPC_ObjectIdentity = ObjectIdentity
jnxFireflyPerimeterFPC = _JnxFireflyPerimeterFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 96, 1)
)
_JnxFireflyPerimeterRE_ObjectIdentity = ObjectIdentity
jnxFireflyPerimeterRE = _JnxFireflyPerimeterRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 96, 2)
)
_JnxFireflyPerimeterPower_ObjectIdentity = ObjectIdentity
jnxFireflyPerimeterPower = _JnxFireflyPerimeterPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 96, 3)
)
_JnxFireflyPerimeterFan_ObjectIdentity = ObjectIdentity
jnxFireflyPerimeterFan = _JnxFireflyPerimeterFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 96, 4)
)
_JnxModuleMX104_ObjectIdentity = ObjectIdentity
jnxModuleMX104 = _JnxModuleMX104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 97)
)
_JnxMX104FPC_ObjectIdentity = ObjectIdentity
jnxMX104FPC = _JnxMX104FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 97, 1)
)
_JnxMX104FEB_ObjectIdentity = ObjectIdentity
jnxMX104FEB = _JnxMX104FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 97, 2)
)
_JnxMX104RE_ObjectIdentity = ObjectIdentity
jnxMX104RE = _JnxMX104RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 97, 3)
)
_JnxMX104Power_ObjectIdentity = ObjectIdentity
jnxMX104Power = _JnxMX104Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 97, 4)
)
_JnxMX104PowerAC_ObjectIdentity = ObjectIdentity
jnxMX104PowerAC = _JnxMX104PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 97, 5)
)
_JnxMX104Fan_ObjectIdentity = ObjectIdentity
jnxMX104Fan = _JnxMX104Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 97, 6)
)
_JnxMX104FPM_ObjectIdentity = ObjectIdentity
jnxMX104FPM = _JnxMX104FPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 97, 7)
)
_JnxModulePTX3000_ObjectIdentity = ObjectIdentity
jnxModulePTX3000 = _JnxModulePTX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 98)
)
_JnxPTX3000SIB_ObjectIdentity = ObjectIdentity
jnxPTX3000SIB = _JnxPTX3000SIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 98, 1)
)
_JnxPTX3000HM_ObjectIdentity = ObjectIdentity
jnxPTX3000HM = _JnxPTX3000HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 98, 2)
)
_JnxPTX3000FPC_ObjectIdentity = ObjectIdentity
jnxPTX3000FPC = _JnxPTX3000FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 98, 3)
)
_JnxPTX3000Fan_ObjectIdentity = ObjectIdentity
jnxPTX3000Fan = _JnxPTX3000Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 98, 4)
)
_JnxPTX3000CB_ObjectIdentity = ObjectIdentity
jnxPTX3000CB = _JnxPTX3000CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 98, 5)
)
_JnxPTX3000FPB_ObjectIdentity = ObjectIdentity
jnxPTX3000FPB = _JnxPTX3000FPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 98, 6)
)
_JnxPTX3000PSM_ObjectIdentity = ObjectIdentity
jnxPTX3000PSM = _JnxPTX3000PSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 98, 7)
)
_JnxPTX3000PIC_ObjectIdentity = ObjectIdentity
jnxPTX3000PIC = _JnxPTX3000PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 98, 8)
)
_JnxModuleMX2010_ObjectIdentity = ObjectIdentity
jnxModuleMX2010 = _JnxModuleMX2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 99)
)
_JnxMX2010SFB_ObjectIdentity = ObjectIdentity
jnxMX2010SFB = _JnxMX2010SFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 99, 1)
)
_JnxMX2010HM_ObjectIdentity = ObjectIdentity
jnxMX2010HM = _JnxMX2010HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 99, 2)
)
_JnxMX2010FPC_ObjectIdentity = ObjectIdentity
jnxMX2010FPC = _JnxMX2010FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 99, 3)
)
_JnxMX2010Fan_ObjectIdentity = ObjectIdentity
jnxMX2010Fan = _JnxMX2010Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 99, 4)
)
_JnxMX2010CB_ObjectIdentity = ObjectIdentity
jnxMX2010CB = _JnxMX2010CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 99, 5)
)
_JnxMX2010FPB_ObjectIdentity = ObjectIdentity
jnxMX2010FPB = _JnxMX2010FPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 99, 6)
)
_JnxMX2010SPMB_ObjectIdentity = ObjectIdentity
jnxMX2010SPMB = _JnxMX2010SPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 99, 7)
)
_JnxMX2010PDM_ObjectIdentity = ObjectIdentity
jnxMX2010PDM = _JnxMX2010PDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 99, 8)
)
_JnxMX2010PSM_ObjectIdentity = ObjectIdentity
jnxMX2010PSM = _JnxMX2010PSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 99, 9)
)
_JnxMX2010ADC_ObjectIdentity = ObjectIdentity
jnxMX2010ADC = _JnxMX2010ADC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 99, 10)
)
_JnxModuleLN2800_ObjectIdentity = ObjectIdentity
jnxModuleLN2800 = _JnxModuleLN2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 101)
)
_JnxLN2800FPC_ObjectIdentity = ObjectIdentity
jnxLN2800FPC = _JnxLN2800FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 101, 1)
)
_JnxLN2800RE_ObjectIdentity = ObjectIdentity
jnxLN2800RE = _JnxLN2800RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 101, 2)
)
_JnxLN2800Power_ObjectIdentity = ObjectIdentity
jnxLN2800Power = _JnxLN2800Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 101, 3)
)
_JnxModuleVRR_ObjectIdentity = ObjectIdentity
jnxModuleVRR = _JnxModuleVRR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 110)
)
_JnxVRRFPC_ObjectIdentity = ObjectIdentity
jnxVRRFPC = _JnxVRRFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 110, 1)
)
_JnxVRRRE_ObjectIdentity = ObjectIdentity
jnxVRRRE = _JnxVRRRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 110, 2)
)
_JnxVRRPower_ObjectIdentity = ObjectIdentity
jnxVRRPower = _JnxVRRPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 110, 3)
)
_JnxVRRFan_ObjectIdentity = ObjectIdentity
jnxVRRFan = _JnxVRRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 110, 4)
)
_JnxModuleACX1000_ObjectIdentity = ObjectIdentity
jnxModuleACX1000 = _JnxModuleACX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 113)
)
_JnxACX1000FPC_ObjectIdentity = ObjectIdentity
jnxACX1000FPC = _JnxACX1000FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 113, 1)
)
_JnxACX1000FEB_ObjectIdentity = ObjectIdentity
jnxACX1000FEB = _JnxACX1000FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 113, 2)
)
_JnxACX1000RE_ObjectIdentity = ObjectIdentity
jnxACX1000RE = _JnxACX1000RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 113, 3)
)
_JnxACX1000Power_ObjectIdentity = ObjectIdentity
jnxACX1000Power = _JnxACX1000Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 113, 4)
)
_JnxACX1000PowerDC_ObjectIdentity = ObjectIdentity
jnxACX1000PowerDC = _JnxACX1000PowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 113, 4, 1)
)
_JnxModuleACX2000_ObjectIdentity = ObjectIdentity
jnxModuleACX2000 = _JnxModuleACX2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 114)
)
_JnxACX2000FPC_ObjectIdentity = ObjectIdentity
jnxACX2000FPC = _JnxACX2000FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 114, 1)
)
_JnxACX2000FEB_ObjectIdentity = ObjectIdentity
jnxACX2000FEB = _JnxACX2000FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 114, 2)
)
_JnxACX2000RE_ObjectIdentity = ObjectIdentity
jnxACX2000RE = _JnxACX2000RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 114, 3)
)
_JnxACX2000Power_ObjectIdentity = ObjectIdentity
jnxACX2000Power = _JnxACX2000Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 114, 4)
)
_JnxACX2000PowerDC_ObjectIdentity = ObjectIdentity
jnxACX2000PowerDC = _JnxACX2000PowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 114, 4, 1)
)
_JnxModuleACX1100_ObjectIdentity = ObjectIdentity
jnxModuleACX1100 = _JnxModuleACX1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 115)
)
_JnxACX1100FPC_ObjectIdentity = ObjectIdentity
jnxACX1100FPC = _JnxACX1100FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 115, 1)
)
_JnxACX1100FEB_ObjectIdentity = ObjectIdentity
jnxACX1100FEB = _JnxACX1100FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 115, 2)
)
_JnxACX1100RE_ObjectIdentity = ObjectIdentity
jnxACX1100RE = _JnxACX1100RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 115, 3)
)
_JnxACX1100Power_ObjectIdentity = ObjectIdentity
jnxACX1100Power = _JnxACX1100Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 115, 4)
)
_JnxACX1100PowerDC_ObjectIdentity = ObjectIdentity
jnxACX1100PowerDC = _JnxACX1100PowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 115, 4, 1)
)
_JnxACX1100PowerAC_ObjectIdentity = ObjectIdentity
jnxACX1100PowerAC = _JnxACX1100PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 115, 4, 2)
)
_JnxModuleACX2100_ObjectIdentity = ObjectIdentity
jnxModuleACX2100 = _JnxModuleACX2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 116)
)
_JnxACX2100FPC_ObjectIdentity = ObjectIdentity
jnxACX2100FPC = _JnxACX2100FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 116, 1)
)
_JnxACX2100FEB_ObjectIdentity = ObjectIdentity
jnxACX2100FEB = _JnxACX2100FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 116, 2)
)
_JnxACX2100RE_ObjectIdentity = ObjectIdentity
jnxACX2100RE = _JnxACX2100RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 116, 3)
)
_JnxACX2100Power_ObjectIdentity = ObjectIdentity
jnxACX2100Power = _JnxACX2100Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 116, 4)
)
_JnxACX2100PowerDC_ObjectIdentity = ObjectIdentity
jnxACX2100PowerDC = _JnxACX2100PowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 116, 4, 1)
)
_JnxACX2100PowerAC_ObjectIdentity = ObjectIdentity
jnxACX2100PowerAC = _JnxACX2100PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 116, 4, 2)
)
_JnxModuleACX2200_ObjectIdentity = ObjectIdentity
jnxModuleACX2200 = _JnxModuleACX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 117)
)
_JnxACX2200FPC_ObjectIdentity = ObjectIdentity
jnxACX2200FPC = _JnxACX2200FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 117, 1)
)
_JnxACX2200FEB_ObjectIdentity = ObjectIdentity
jnxACX2200FEB = _JnxACX2200FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 117, 2)
)
_JnxACX2200RE_ObjectIdentity = ObjectIdentity
jnxACX2200RE = _JnxACX2200RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 117, 3)
)
_JnxACX2200Power_ObjectIdentity = ObjectIdentity
jnxACX2200Power = _JnxACX2200Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 117, 4)
)
_JnxACX2200PowerDC_ObjectIdentity = ObjectIdentity
jnxACX2200PowerDC = _JnxACX2200PowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 117, 4, 1)
)
_JnxACX2200PowerAC_ObjectIdentity = ObjectIdentity
jnxACX2200PowerAC = _JnxACX2200PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 117, 4, 2)
)
_JnxModuleACX4000_ObjectIdentity = ObjectIdentity
jnxModuleACX4000 = _JnxModuleACX4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 118)
)
_JnxACX4000FPC_ObjectIdentity = ObjectIdentity
jnxACX4000FPC = _JnxACX4000FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 118, 1)
)
_JnxACX4000FEB_ObjectIdentity = ObjectIdentity
jnxACX4000FEB = _JnxACX4000FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 118, 2)
)
_JnxACX4000RE_ObjectIdentity = ObjectIdentity
jnxACX4000RE = _JnxACX4000RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 118, 3)
)
_JnxACX4000Power_ObjectIdentity = ObjectIdentity
jnxACX4000Power = _JnxACX4000Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 118, 4)
)
_JnxACX4000PowerDC_ObjectIdentity = ObjectIdentity
jnxACX4000PowerDC = _JnxACX4000PowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 118, 4, 1)
)
_JnxACX4000PowerAC_ObjectIdentity = ObjectIdentity
jnxACX4000PowerAC = _JnxACX4000PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 118, 4, 2)
)
_JnxACX4000Fan_ObjectIdentity = ObjectIdentity
jnxACX4000Fan = _JnxACX4000Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 118, 5)
)
_JnxModuleACX500AC_ObjectIdentity = ObjectIdentity
jnxModuleACX500AC = _JnxModuleACX500AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 119)
)
_JnxACX500ACFPC_ObjectIdentity = ObjectIdentity
jnxACX500ACFPC = _JnxACX500ACFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 119, 1)
)
_JnxACX500ACFEB_ObjectIdentity = ObjectIdentity
jnxACX500ACFEB = _JnxACX500ACFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 119, 2)
)
_JnxACX500ACRE_ObjectIdentity = ObjectIdentity
jnxACX500ACRE = _JnxACX500ACRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 119, 3)
)
_JnxACX500ACPower_ObjectIdentity = ObjectIdentity
jnxACX500ACPower = _JnxACX500ACPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 119, 4)
)
_JnxACX500ACPowerAC_ObjectIdentity = ObjectIdentity
jnxACX500ACPowerAC = _JnxACX500ACPowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 119, 4, 1)
)
_JnxModuleACX500DC_ObjectIdentity = ObjectIdentity
jnxModuleACX500DC = _JnxModuleACX500DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 120)
)
_JnxACX500DCFPC_ObjectIdentity = ObjectIdentity
jnxACX500DCFPC = _JnxACX500DCFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 120, 1)
)
_JnxACX500DCFEB_ObjectIdentity = ObjectIdentity
jnxACX500DCFEB = _JnxACX500DCFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 120, 2)
)
_JnxACX500DCRE_ObjectIdentity = ObjectIdentity
jnxACX500DCRE = _JnxACX500DCRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 120, 3)
)
_JnxACX500DCPower_ObjectIdentity = ObjectIdentity
jnxACX500DCPower = _JnxACX500DCPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 120, 4)
)
_JnxACX500DCPowerDC_ObjectIdentity = ObjectIdentity
jnxACX500DCPowerDC = _JnxACX500DCPowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 120, 4, 1)
)
_JnxModuleACX500OAC_ObjectIdentity = ObjectIdentity
jnxModuleACX500OAC = _JnxModuleACX500OAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 121)
)
_JnxACX500OACFPC_ObjectIdentity = ObjectIdentity
jnxACX500OACFPC = _JnxACX500OACFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 121, 1)
)
_JnxACX500OACFEB_ObjectIdentity = ObjectIdentity
jnxACX500OACFEB = _JnxACX500OACFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 121, 2)
)
_JnxACX500OACRE_ObjectIdentity = ObjectIdentity
jnxACX500OACRE = _JnxACX500OACRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 121, 3)
)
_JnxACX500OACPower_ObjectIdentity = ObjectIdentity
jnxACX500OACPower = _JnxACX500OACPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 121, 4)
)
_JnxACX500OACPowerAC_ObjectIdentity = ObjectIdentity
jnxACX500OACPowerAC = _JnxACX500OACPowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 121, 4, 1)
)
_JnxModuleACX500ODC_ObjectIdentity = ObjectIdentity
jnxModuleACX500ODC = _JnxModuleACX500ODC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 122)
)
_JnxACX500ODCFPC_ObjectIdentity = ObjectIdentity
jnxACX500ODCFPC = _JnxACX500ODCFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 122, 1)
)
_JnxACX500ODCFEB_ObjectIdentity = ObjectIdentity
jnxACX500ODCFEB = _JnxACX500ODCFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 122, 2)
)
_JnxACX500ODCRE_ObjectIdentity = ObjectIdentity
jnxACX500ODCRE = _JnxACX500ODCRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 122, 3)
)
_JnxACX500ODCPower_ObjectIdentity = ObjectIdentity
jnxACX500ODCPower = _JnxACX500ODCPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 122, 4)
)
_JnxACX500ODCPowerDC_ObjectIdentity = ObjectIdentity
jnxACX500ODCPowerDC = _JnxACX500ODCPowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 122, 4, 1)
)
_JnxModuleACX500OPOEAC_ObjectIdentity = ObjectIdentity
jnxModuleACX500OPOEAC = _JnxModuleACX500OPOEAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 123)
)
_JnxACX500OPOEACFPC_ObjectIdentity = ObjectIdentity
jnxACX500OPOEACFPC = _JnxACX500OPOEACFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 123, 1)
)
_JnxACX500OPOEACFEB_ObjectIdentity = ObjectIdentity
jnxACX500OPOEACFEB = _JnxACX500OPOEACFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 123, 2)
)
_JnxACX500OPOEACRE_ObjectIdentity = ObjectIdentity
jnxACX500OPOEACRE = _JnxACX500OPOEACRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 123, 3)
)
_JnxACX500OPOEACPower_ObjectIdentity = ObjectIdentity
jnxACX500OPOEACPower = _JnxACX500OPOEACPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 123, 4)
)
_JnxACX500OPOEACPowerAC_ObjectIdentity = ObjectIdentity
jnxACX500OPOEACPowerAC = _JnxACX500OPOEACPowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 123, 4, 1)
)
_JnxModuleACX500OPOEDC_ObjectIdentity = ObjectIdentity
jnxModuleACX500OPOEDC = _JnxModuleACX500OPOEDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 124)
)
_JnxACX500OPOEDCFPC_ObjectIdentity = ObjectIdentity
jnxACX500OPOEDCFPC = _JnxACX500OPOEDCFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 124, 1)
)
_JnxACX500OPOEDCFEB_ObjectIdentity = ObjectIdentity
jnxACX500OPOEDCFEB = _JnxACX500OPOEDCFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 124, 2)
)
_JnxACX500OPOEDCRE_ObjectIdentity = ObjectIdentity
jnxACX500OPOEDCRE = _JnxACX500OPOEDCRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 124, 3)
)
_JnxACX500OPOEDCPower_ObjectIdentity = ObjectIdentity
jnxACX500OPOEDCPower = _JnxACX500OPOEDCPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 124, 4)
)
_JnxACX500OPOEDCPowerDC_ObjectIdentity = ObjectIdentity
jnxACX500OPOEDCPowerDC = _JnxACX500OPOEDCPowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 124, 4, 1)
)
_JnxModuleVSRX_ObjectIdentity = ObjectIdentity
jnxModuleVSRX = _JnxModuleVSRX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 129)
)
_JnxVSRXFPC_ObjectIdentity = ObjectIdentity
jnxVSRXFPC = _JnxVSRXFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 129, 1)
)
_JnxVSRXRE_ObjectIdentity = ObjectIdentity
jnxVSRXRE = _JnxVSRXRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 129, 2)
)
_JnxVSRXPower_ObjectIdentity = ObjectIdentity
jnxVSRXPower = _JnxVSRXPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 129, 3)
)
_JnxVSRXFan_ObjectIdentity = ObjectIdentity
jnxVSRXFan = _JnxVSRXFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 129, 4)
)
_JnxModuleEX3400_ObjectIdentity = ObjectIdentity
jnxModuleEX3400 = _JnxModuleEX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 131)
)
_JnxEX3400FPC_ObjectIdentity = ObjectIdentity
jnxEX3400FPC = _JnxEX3400FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 131, 1)
)
_JnxEX3400Power_ObjectIdentity = ObjectIdentity
jnxEX3400Power = _JnxEX3400Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 131, 1, 1)
)
_JnxEX3400Fan_ObjectIdentity = ObjectIdentity
jnxEX3400Fan = _JnxEX3400Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 131, 1, 2)
)
_JnxModuleEX2300_ObjectIdentity = ObjectIdentity
jnxModuleEX2300 = _JnxModuleEX2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 132)
)
_JnxEX2300FPC_ObjectIdentity = ObjectIdentity
jnxEX2300FPC = _JnxEX2300FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 132, 1)
)
_JnxEX2300Power_ObjectIdentity = ObjectIdentity
jnxEX2300Power = _JnxEX2300Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 132, 1, 1)
)
_JnxEX2300Fan_ObjectIdentity = ObjectIdentity
jnxEX2300Fan = _JnxEX2300Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 132, 1, 2)
)
_JnxModuleSRX300_ObjectIdentity = ObjectIdentity
jnxModuleSRX300 = _JnxModuleSRX300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 133)
)
_JnxSRX300FPC_ObjectIdentity = ObjectIdentity
jnxSRX300FPC = _JnxSRX300FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 133, 1)
)
_JnxSRX300RE_ObjectIdentity = ObjectIdentity
jnxSRX300RE = _JnxSRX300RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 133, 2)
)
_JnxSRX300Power_ObjectIdentity = ObjectIdentity
jnxSRX300Power = _JnxSRX300Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 133, 3)
)
_JnxSRX300Fan_ObjectIdentity = ObjectIdentity
jnxSRX300Fan = _JnxSRX300Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 133, 4)
)
_JnxModuleSRX320_ObjectIdentity = ObjectIdentity
jnxModuleSRX320 = _JnxModuleSRX320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 134)
)
_JnxSRX320FPC_ObjectIdentity = ObjectIdentity
jnxSRX320FPC = _JnxSRX320FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 134, 1)
)
_JnxSRX320RE_ObjectIdentity = ObjectIdentity
jnxSRX320RE = _JnxSRX320RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 134, 2)
)
_JnxSRX320Power_ObjectIdentity = ObjectIdentity
jnxSRX320Power = _JnxSRX320Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 134, 3)
)
_JnxSRX320Fan_ObjectIdentity = ObjectIdentity
jnxSRX320Fan = _JnxSRX320Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 134, 4)
)
_JnxModuleSRX340_ObjectIdentity = ObjectIdentity
jnxModuleSRX340 = _JnxModuleSRX340_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 135)
)
_JnxSRX340FPC_ObjectIdentity = ObjectIdentity
jnxSRX340FPC = _JnxSRX340FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 135, 1)
)
_JnxSRX340RE_ObjectIdentity = ObjectIdentity
jnxSRX340RE = _JnxSRX340RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 135, 2)
)
_JnxSRX340Power_ObjectIdentity = ObjectIdentity
jnxSRX340Power = _JnxSRX340Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 135, 3)
)
_JnxSRX340Fan_ObjectIdentity = ObjectIdentity
jnxSRX340Fan = _JnxSRX340Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 135, 4)
)
_JnxModuleSRX345_ObjectIdentity = ObjectIdentity
jnxModuleSRX345 = _JnxModuleSRX345_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 136)
)
_JnxSRX345FPC_ObjectIdentity = ObjectIdentity
jnxSRX345FPC = _JnxSRX345FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 136, 1)
)
_JnxSRX345RE_ObjectIdentity = ObjectIdentity
jnxSRX345RE = _JnxSRX345RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 136, 2)
)
_JnxSRX345Power_ObjectIdentity = ObjectIdentity
jnxSRX345Power = _JnxSRX345Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 136, 3)
)
_JnxSRX345Fan_ObjectIdentity = ObjectIdentity
jnxSRX345Fan = _JnxSRX345Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 136, 4)
)
_JnxModuleSRX1500_ObjectIdentity = ObjectIdentity
jnxModuleSRX1500 = _JnxModuleSRX1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 137)
)
_JnxSRX1500FPC_ObjectIdentity = ObjectIdentity
jnxSRX1500FPC = _JnxSRX1500FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 137, 1)
)
_JnxSRX1500RE_ObjectIdentity = ObjectIdentity
jnxSRX1500RE = _JnxSRX1500RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 137, 2)
)
_JnxSRX1500Power_ObjectIdentity = ObjectIdentity
jnxSRX1500Power = _JnxSRX1500Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 137, 3)
)
_JnxSRX1500Fan_ObjectIdentity = ObjectIdentity
jnxSRX1500Fan = _JnxSRX1500Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 137, 4)
)
_JnxSRX1500CB_ObjectIdentity = ObjectIdentity
jnxSRX1500CB = _JnxSRX1500CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 137, 5)
)
_JnxModuleJNP10003_ObjectIdentity = ObjectIdentity
jnxModuleJNP10003 = _JnxModuleJNP10003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 139)
)
_JnxJNP10003HM_ObjectIdentity = ObjectIdentity
jnxJNP10003HM = _JnxJNP10003HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 139, 1)
)
_JnxJNP10003FPC_ObjectIdentity = ObjectIdentity
jnxJNP10003FPC = _JnxJNP10003FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 139, 2)
)
_JnxJNP10003Fan_ObjectIdentity = ObjectIdentity
jnxJNP10003Fan = _JnxJNP10003Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 139, 3)
)
_JnxJNP10003CB_ObjectIdentity = ObjectIdentity
jnxJNP10003CB = _JnxJNP10003CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 139, 4)
)
_JnxJNP10003Power_ObjectIdentity = ObjectIdentity
jnxJNP10003Power = _JnxJNP10003Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 139, 5)
)
_JnxModuleSRX4600_ObjectIdentity = ObjectIdentity
jnxModuleSRX4600 = _JnxModuleSRX4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 140)
)
_JnxSRX4600HM_ObjectIdentity = ObjectIdentity
jnxSRX4600HM = _JnxSRX4600HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 140, 1)
)
_JnxSRX4600FPC_ObjectIdentity = ObjectIdentity
jnxSRX4600FPC = _JnxSRX4600FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 140, 2)
)
_JnxSRX4600Fan_ObjectIdentity = ObjectIdentity
jnxSRX4600Fan = _JnxSRX4600Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 140, 3)
)
_JnxSRX4600SPMB_ObjectIdentity = ObjectIdentity
jnxSRX4600SPMB = _JnxSRX4600SPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 140, 4)
)
_JnxSRX4600PSM_ObjectIdentity = ObjectIdentity
jnxSRX4600PSM = _JnxSRX4600PSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 140, 5)
)
_JnxModuleSRX4800_ObjectIdentity = ObjectIdentity
jnxModuleSRX4800 = _JnxModuleSRX4800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 141)
)
_JnxSRX4800HM_ObjectIdentity = ObjectIdentity
jnxSRX4800HM = _JnxSRX4800HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 141, 1)
)
_JnxSRX4800FPC_ObjectIdentity = ObjectIdentity
jnxSRX4800FPC = _JnxSRX4800FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 141, 2)
)
_JnxSRX4800Fan_ObjectIdentity = ObjectIdentity
jnxSRX4800Fan = _JnxSRX4800Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 141, 3)
)
_JnxSRX4800SPMB_ObjectIdentity = ObjectIdentity
jnxSRX4800SPMB = _JnxSRX4800SPMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 141, 4)
)
_JnxSRX4800PSM_ObjectIdentity = ObjectIdentity
jnxSRX4800PSM = _JnxSRX4800PSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 141, 5)
)
_JnxModuleSRX4100_ObjectIdentity = ObjectIdentity
jnxModuleSRX4100 = _JnxModuleSRX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 142)
)
_JnxSRX4100FPC_ObjectIdentity = ObjectIdentity
jnxSRX4100FPC = _JnxSRX4100FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 142, 1)
)
_JnxSRX4100RE_ObjectIdentity = ObjectIdentity
jnxSRX4100RE = _JnxSRX4100RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 142, 2)
)
_JnxSRX4100Power_ObjectIdentity = ObjectIdentity
jnxSRX4100Power = _JnxSRX4100Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 142, 3)
)
_JnxSRX4100Fan_ObjectIdentity = ObjectIdentity
jnxSRX4100Fan = _JnxSRX4100Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 142, 4)
)
_JnxModuleSRX4200_ObjectIdentity = ObjectIdentity
jnxModuleSRX4200 = _JnxModuleSRX4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 143)
)
_JnxSRX4200FPC_ObjectIdentity = ObjectIdentity
jnxSRX4200FPC = _JnxSRX4200FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 143, 1)
)
_JnxSRX4200RE_ObjectIdentity = ObjectIdentity
jnxSRX4200RE = _JnxSRX4200RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 143, 2)
)
_JnxSRX4200Power_ObjectIdentity = ObjectIdentity
jnxSRX4200Power = _JnxSRX4200Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 143, 3)
)
_JnxSRX4200Fan_ObjectIdentity = ObjectIdentity
jnxSRX4200Fan = _JnxSRX4200Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 143, 4)
)
_JnxModuleJNP204_ObjectIdentity = ObjectIdentity
jnxModuleJNP204 = _JnxModuleJNP204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 144)
)
_JnxJNP204HM_ObjectIdentity = ObjectIdentity
jnxJNP204HM = _JnxJNP204HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 144, 1)
)
_JnxJNP204FPC_ObjectIdentity = ObjectIdentity
jnxJNP204FPC = _JnxJNP204FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 144, 2)
)
_JnxJNP204Fan_ObjectIdentity = ObjectIdentity
jnxJNP204Fan = _JnxJNP204Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 144, 3)
)
_JnxJNP204CB_ObjectIdentity = ObjectIdentity
jnxJNP204CB = _JnxJNP204CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 144, 4)
)
_JnxJNP204Power_ObjectIdentity = ObjectIdentity
jnxJNP204Power = _JnxJNP204Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 144, 5)
)
_JnxModuleMX2008_ObjectIdentity = ObjectIdentity
jnxModuleMX2008 = _JnxModuleMX2008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 145)
)
_JnxMX2008SFB_ObjectIdentity = ObjectIdentity
jnxMX2008SFB = _JnxMX2008SFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 145, 1)
)
_JnxMX2008HM_ObjectIdentity = ObjectIdentity
jnxMX2008HM = _JnxMX2008HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 145, 2)
)
_JnxMX2008FPC_ObjectIdentity = ObjectIdentity
jnxMX2008FPC = _JnxMX2008FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 145, 3)
)
_JnxMX2008Fan_ObjectIdentity = ObjectIdentity
jnxMX2008Fan = _JnxMX2008Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 145, 4)
)
_JnxMX2008RCB_ObjectIdentity = ObjectIdentity
jnxMX2008RCB = _JnxMX2008RCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 145, 5)
)
_JnxMX2008FPB_ObjectIdentity = ObjectIdentity
jnxMX2008FPB = _JnxMX2008FPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 145, 6)
)
_JnxMX2008PDM_ObjectIdentity = ObjectIdentity
jnxMX2008PDM = _JnxMX2008PDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 145, 7)
)
_JnxMX2008PSM_ObjectIdentity = ObjectIdentity
jnxMX2008PSM = _JnxMX2008PSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 145, 8)
)
_JnxMX2008ADC_ObjectIdentity = ObjectIdentity
jnxMX2008ADC = _JnxMX2008ADC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 145, 9)
)
_JnxModuleMXTSR80_ObjectIdentity = ObjectIdentity
jnxModuleMXTSR80 = _JnxModuleMXTSR80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 146)
)
_JnxMXTSR80FPC_ObjectIdentity = ObjectIdentity
jnxMXTSR80FPC = _JnxMXTSR80FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 146, 1)
)
_JnxMXTSR80FEB_ObjectIdentity = ObjectIdentity
jnxMXTSR80FEB = _JnxMXTSR80FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 146, 2)
)
_JnxMXTSR80RE_ObjectIdentity = ObjectIdentity
jnxMXTSR80RE = _JnxMXTSR80RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 146, 3)
)
_JnxMXTSR80Power_ObjectIdentity = ObjectIdentity
jnxMXTSR80Power = _JnxMXTSR80Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 146, 4)
)
_JnxMXTSR80PowerAC_ObjectIdentity = ObjectIdentity
jnxMXTSR80PowerAC = _JnxMXTSR80PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 146, 5)
)
_JnxMXTSR80Fan_ObjectIdentity = ObjectIdentity
jnxMXTSR80Fan = _JnxMXTSR80Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 146, 6)
)
_JnxMXTSR80FPM_ObjectIdentity = ObjectIdentity
jnxMXTSR80FPM = _JnxMXTSR80FPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 146, 7)
)
_JnxModulePTX10008_ObjectIdentity = ObjectIdentity
jnxModulePTX10008 = _JnxModulePTX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 147)
)
_JnxPTX10008FPC_ObjectIdentity = ObjectIdentity
jnxPTX10008FPC = _JnxPTX10008FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 147, 1)
)
_JnxPTX10008HM_ObjectIdentity = ObjectIdentity
jnxPTX10008HM = _JnxPTX10008HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 147, 2)
)
_JnxPTX10008Power_ObjectIdentity = ObjectIdentity
jnxPTX10008Power = _JnxPTX10008Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 147, 3)
)
_JnxPTX10008Fan_ObjectIdentity = ObjectIdentity
jnxPTX10008Fan = _JnxPTX10008Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 147, 4)
)
_JnxPTX10008FPB_ObjectIdentity = ObjectIdentity
jnxPTX10008FPB = _JnxPTX10008FPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 147, 5)
)
_JnxPTX10008CBD_ObjectIdentity = ObjectIdentity
jnxPTX10008CBD = _JnxPTX10008CBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 147, 6)
)
_JnxPTX10008SIB_ObjectIdentity = ObjectIdentity
jnxPTX10008SIB = _JnxPTX10008SIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 147, 7)
)
_JnxPTX10008FPM_ObjectIdentity = ObjectIdentity
jnxPTX10008FPM = _JnxPTX10008FPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 147, 8)
)
_JnxPTX10008FTC_ObjectIdentity = ObjectIdentity
jnxPTX10008FTC = _JnxPTX10008FTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 147, 9)
)
_JnxPTX10008Backplane_ObjectIdentity = ObjectIdentity
jnxPTX10008Backplane = _JnxPTX10008Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 147, 10)
)
_JnxModuleACX5448_ObjectIdentity = ObjectIdentity
jnxModuleACX5448 = _JnxModuleACX5448_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 148)
)
_JnxACX5448FPC_ObjectIdentity = ObjectIdentity
jnxACX5448FPC = _JnxACX5448FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 148, 1)
)
_JnxACX5448FEB_ObjectIdentity = ObjectIdentity
jnxACX5448FEB = _JnxACX5448FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 148, 2)
)
_JnxACX5448RE_ObjectIdentity = ObjectIdentity
jnxACX5448RE = _JnxACX5448RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 148, 3)
)
_JnxACX5448Power_ObjectIdentity = ObjectIdentity
jnxACX5448Power = _JnxACX5448Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 148, 4)
)
_JnxACX5448PowerDC_ObjectIdentity = ObjectIdentity
jnxACX5448PowerDC = _JnxACX5448PowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 148, 4, 1)
)
_JnxACX5448PowerAC_ObjectIdentity = ObjectIdentity
jnxACX5448PowerAC = _JnxACX5448PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 148, 4, 2)
)
_JnxACX5448Fan_ObjectIdentity = ObjectIdentity
jnxACX5448Fan = _JnxACX5448Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 148, 5)
)
_JnxModulePTX10016_ObjectIdentity = ObjectIdentity
jnxModulePTX10016 = _JnxModulePTX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 150)
)
_JnxPTX10016FPC_ObjectIdentity = ObjectIdentity
jnxPTX10016FPC = _JnxPTX10016FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 150, 1)
)
_JnxPTX10016HM_ObjectIdentity = ObjectIdentity
jnxPTX10016HM = _JnxPTX10016HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 150, 2)
)
_JnxPTX10016Power_ObjectIdentity = ObjectIdentity
jnxPTX10016Power = _JnxPTX10016Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 150, 3)
)
_JnxPTX10016Fan_ObjectIdentity = ObjectIdentity
jnxPTX10016Fan = _JnxPTX10016Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 150, 4)
)
_JnxPTX10016FPB_ObjectIdentity = ObjectIdentity
jnxPTX10016FPB = _JnxPTX10016FPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 150, 5)
)
_JnxPTX10016CBD_ObjectIdentity = ObjectIdentity
jnxPTX10016CBD = _JnxPTX10016CBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 150, 6)
)
_JnxPTX10016SIB_ObjectIdentity = ObjectIdentity
jnxPTX10016SIB = _JnxPTX10016SIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 150, 7)
)
_JnxPTX10016FTC_ObjectIdentity = ObjectIdentity
jnxPTX10016FTC = _JnxPTX10016FTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 150, 8)
)
_JnxPTX10016Backplane_ObjectIdentity = ObjectIdentity
jnxPTX10016Backplane = _JnxPTX10016Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 150, 9)
)
_JnxModuleEX9251_ObjectIdentity = ObjectIdentity
jnxModuleEX9251 = _JnxModuleEX9251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 151)
)
_JnxEX9251HM_ObjectIdentity = ObjectIdentity
jnxEX9251HM = _JnxEX9251HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 151, 1)
)
_JnxEX9251FPC_ObjectIdentity = ObjectIdentity
jnxEX9251FPC = _JnxEX9251FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 151, 2)
)
_JnxEX9251Fan_ObjectIdentity = ObjectIdentity
jnxEX9251Fan = _JnxEX9251Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 151, 3)
)
_JnxEX9251CB_ObjectIdentity = ObjectIdentity
jnxEX9251CB = _JnxEX9251CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 151, 4)
)
_JnxEX9251Power_ObjectIdentity = ObjectIdentity
jnxEX9251Power = _JnxEX9251Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 151, 5)
)
_JnxModuleJNP10001_ObjectIdentity = ObjectIdentity
jnxModuleJNP10001 = _JnxModuleJNP10001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 153)
)
_JnxJNP10001HM_ObjectIdentity = ObjectIdentity
jnxJNP10001HM = _JnxJNP10001HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 153, 1)
)
_JnxJNP10001FPC_ObjectIdentity = ObjectIdentity
jnxJNP10001FPC = _JnxJNP10001FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 153, 2)
)
_JnxJNP10001Fan_ObjectIdentity = ObjectIdentity
jnxJNP10001Fan = _JnxJNP10001Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 153, 3)
)
_JnxJNP10001Power_ObjectIdentity = ObjectIdentity
jnxJNP10001Power = _JnxJNP10001Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 153, 4)
)
_JnxModuleMX10008_ObjectIdentity = ObjectIdentity
jnxModuleMX10008 = _JnxModuleMX10008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 154)
)
_JnxMX10008SFB_ObjectIdentity = ObjectIdentity
jnxMX10008SFB = _JnxMX10008SFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 154, 1)
)
_JnxMX10008HM_ObjectIdentity = ObjectIdentity
jnxMX10008HM = _JnxMX10008HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 154, 2)
)
_JnxMX10008FPC_ObjectIdentity = ObjectIdentity
jnxMX10008FPC = _JnxMX10008FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 154, 3)
)
_JnxMX10008Fan_ObjectIdentity = ObjectIdentity
jnxMX10008Fan = _JnxMX10008Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 154, 4)
)
_JnxMX10008CBD_ObjectIdentity = ObjectIdentity
jnxMX10008CBD = _JnxMX10008CBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 154, 5)
)
_JnxMX10008Power_ObjectIdentity = ObjectIdentity
jnxMX10008Power = _JnxMX10008Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 154, 6)
)
_JnxMX10008FPB_ObjectIdentity = ObjectIdentity
jnxMX10008FPB = _JnxMX10008FPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 154, 7)
)
_JnxMX10008FTC_ObjectIdentity = ObjectIdentity
jnxMX10008FTC = _JnxMX10008FTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 154, 8)
)
_JnxModuleMX10016_ObjectIdentity = ObjectIdentity
jnxModuleMX10016 = _JnxModuleMX10016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 155)
)
_JnxMX10016SFB_ObjectIdentity = ObjectIdentity
jnxMX10016SFB = _JnxMX10016SFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 155, 1)
)
_JnxMX10016HM_ObjectIdentity = ObjectIdentity
jnxMX10016HM = _JnxMX10016HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 155, 2)
)
_JnxMX10016FPC_ObjectIdentity = ObjectIdentity
jnxMX10016FPC = _JnxMX10016FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 155, 3)
)
_JnxMX10016Fan_ObjectIdentity = ObjectIdentity
jnxMX10016Fan = _JnxMX10016Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 155, 4)
)
_JnxMX10016CBD_ObjectIdentity = ObjectIdentity
jnxMX10016CBD = _JnxMX10016CBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 155, 5)
)
_JnxMX10016Power_ObjectIdentity = ObjectIdentity
jnxMX10016Power = _JnxMX10016Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 155, 6)
)
_JnxMX10016FPB_ObjectIdentity = ObjectIdentity
jnxMX10016FPB = _JnxMX10016FPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 155, 7)
)
_JnxModuleEX9253_ObjectIdentity = ObjectIdentity
jnxModuleEX9253 = _JnxModuleEX9253_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 156)
)
_JnxEX9253HM_ObjectIdentity = ObjectIdentity
jnxEX9253HM = _JnxEX9253HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 156, 1)
)
_JnxEX9253FPC_ObjectIdentity = ObjectIdentity
jnxEX9253FPC = _JnxEX9253FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 156, 2)
)
_JnxEX9253Fan_ObjectIdentity = ObjectIdentity
jnxEX9253Fan = _JnxEX9253Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 156, 3)
)
_JnxEX9253CB_ObjectIdentity = ObjectIdentity
jnxEX9253CB = _JnxEX9253CB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 156, 4)
)
_JnxEX9253Power_ObjectIdentity = ObjectIdentity
jnxEX9253Power = _JnxEX9253Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 156, 5)
)
_JnxModuleJRR200_ObjectIdentity = ObjectIdentity
jnxModuleJRR200 = _JnxModuleJRR200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 157)
)
_JnxJRR200RE_ObjectIdentity = ObjectIdentity
jnxJRR200RE = _JnxJRR200RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 157, 1)
)
_JnxJRR200Power_ObjectIdentity = ObjectIdentity
jnxJRR200Power = _JnxJRR200Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 157, 2)
)
_JnxJRR200Fan_ObjectIdentity = ObjectIdentity
jnxJRR200Fan = _JnxJRR200Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 157, 3)
)
_JnxModuleACX5448M_ObjectIdentity = ObjectIdentity
jnxModuleACX5448M = _JnxModuleACX5448M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 158)
)
_JnxACX5448MFPC_ObjectIdentity = ObjectIdentity
jnxACX5448MFPC = _JnxACX5448MFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 158, 1)
)
_JnxACX5448MFEB_ObjectIdentity = ObjectIdentity
jnxACX5448MFEB = _JnxACX5448MFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 158, 2)
)
_JnxACX5448MRE_ObjectIdentity = ObjectIdentity
jnxACX5448MRE = _JnxACX5448MRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 158, 3)
)
_JnxACX5448MPower_ObjectIdentity = ObjectIdentity
jnxACX5448MPower = _JnxACX5448MPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 158, 4)
)
_JnxACX5448MPowerDC_ObjectIdentity = ObjectIdentity
jnxACX5448MPowerDC = _JnxACX5448MPowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 158, 4, 1)
)
_JnxACX5448MPowerAC_ObjectIdentity = ObjectIdentity
jnxACX5448MPowerAC = _JnxACX5448MPowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 158, 4, 2)
)
_JnxACX5448MFan_ObjectIdentity = ObjectIdentity
jnxACX5448MFan = _JnxACX5448MFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 158, 5)
)
_JnxModuleACX5448D_ObjectIdentity = ObjectIdentity
jnxModuleACX5448D = _JnxModuleACX5448D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 159)
)
_JnxACX5448DFPC_ObjectIdentity = ObjectIdentity
jnxACX5448DFPC = _JnxACX5448DFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 159, 1)
)
_JnxACX5448DFEB_ObjectIdentity = ObjectIdentity
jnxACX5448DFEB = _JnxACX5448DFEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 159, 2)
)
_JnxACX5448DRE_ObjectIdentity = ObjectIdentity
jnxACX5448DRE = _JnxACX5448DRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 159, 3)
)
_JnxACX5448DPower_ObjectIdentity = ObjectIdentity
jnxACX5448DPower = _JnxACX5448DPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 159, 4)
)
_JnxACX5448DPowerDC_ObjectIdentity = ObjectIdentity
jnxACX5448DPowerDC = _JnxACX5448DPowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 159, 4, 1)
)
_JnxACX5448DPowerAC_ObjectIdentity = ObjectIdentity
jnxACX5448DPowerAC = _JnxACX5448DPowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 159, 4, 2)
)
_JnxACX5448DFan_ObjectIdentity = ObjectIdentity
jnxACX5448DFan = _JnxACX5448DFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 159, 5)
)
_JnxModuleACX6360OR_ObjectIdentity = ObjectIdentity
jnxModuleACX6360OR = _JnxModuleACX6360OR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 160)
)
_JnxACX6360ORHM_ObjectIdentity = ObjectIdentity
jnxACX6360ORHM = _JnxACX6360ORHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 160, 1)
)
_JnxACX6360ORFPC_ObjectIdentity = ObjectIdentity
jnxACX6360ORFPC = _JnxACX6360ORFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 160, 2)
)
_JnxACX6360ORFan_ObjectIdentity = ObjectIdentity
jnxACX6360ORFan = _JnxACX6360ORFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 160, 3)
)
_JnxACX6360ORPower_ObjectIdentity = ObjectIdentity
jnxACX6360ORPower = _JnxACX6360ORPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 160, 4)
)
_JnxModuleACX6360OX_ObjectIdentity = ObjectIdentity
jnxModuleACX6360OX = _JnxModuleACX6360OX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 161)
)
_JnxACX6360OXHM_ObjectIdentity = ObjectIdentity
jnxACX6360OXHM = _JnxACX6360OXHM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 161, 1)
)
_JnxACX6360OXFPC_ObjectIdentity = ObjectIdentity
jnxACX6360OXFPC = _JnxACX6360OXFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 161, 2)
)
_JnxACX6360OXFan_ObjectIdentity = ObjectIdentity
jnxACX6360OXFan = _JnxACX6360OXFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 161, 3)
)
_JnxACX6360OXPower_ObjectIdentity = ObjectIdentity
jnxACX6360OXPower = _JnxACX6360OXPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 161, 4)
)
_JnxModuleACX710_ObjectIdentity = ObjectIdentity
jnxModuleACX710 = _JnxModuleACX710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 162)
)
_JnxACX710FPC_ObjectIdentity = ObjectIdentity
jnxACX710FPC = _JnxACX710FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 162, 1)
)
_JnxACX710RE_ObjectIdentity = ObjectIdentity
jnxACX710RE = _JnxACX710RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 162, 2)
)
_JnxACX710Power_ObjectIdentity = ObjectIdentity
jnxACX710Power = _JnxACX710Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 162, 3)
)
_JnxACX710PowerDC_ObjectIdentity = ObjectIdentity
jnxACX710PowerDC = _JnxACX710PowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 162, 3, 1)
)
_JnxACX710PowerAC_ObjectIdentity = ObjectIdentity
jnxACX710PowerAC = _JnxACX710PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 162, 3, 2)
)
_JnxACX710Fan_ObjectIdentity = ObjectIdentity
jnxACX710Fan = _JnxACX710Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 162, 4)
)
_JnxModuleACX5800_ObjectIdentity = ObjectIdentity
jnxModuleACX5800 = _JnxModuleACX5800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 163)
)
_JnxACX5800FPC_ObjectIdentity = ObjectIdentity
jnxACX5800FPC = _JnxACX5800FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 163, 1)
)
_JnxACX5800FEB_ObjectIdentity = ObjectIdentity
jnxACX5800FEB = _JnxACX5800FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 163, 2)
)
_JnxACX5800RE_ObjectIdentity = ObjectIdentity
jnxACX5800RE = _JnxACX5800RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 163, 3)
)
_JnxACX5800Power_ObjectIdentity = ObjectIdentity
jnxACX5800Power = _JnxACX5800Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 163, 4)
)
_JnxACX5800PowerDC_ObjectIdentity = ObjectIdentity
jnxACX5800PowerDC = _JnxACX5800PowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 163, 4, 1)
)
_JnxACX5800PowerAC_ObjectIdentity = ObjectIdentity
jnxACX5800PowerAC = _JnxACX5800PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 163, 4, 2)
)
_JnxModuleSRX380_ObjectIdentity = ObjectIdentity
jnxModuleSRX380 = _JnxModuleSRX380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 164)
)
_JnxSRX380FPC_ObjectIdentity = ObjectIdentity
jnxSRX380FPC = _JnxSRX380FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 164, 1)
)
_JnxSRX380RE_ObjectIdentity = ObjectIdentity
jnxSRX380RE = _JnxSRX380RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 164, 2)
)
_JnxSRX380Power_ObjectIdentity = ObjectIdentity
jnxSRX380Power = _JnxSRX380Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 164, 3)
)
_JnxSRX380Fan_ObjectIdentity = ObjectIdentity
jnxSRX380Fan = _JnxSRX380Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 164, 4)
)
_JnxModuleEX4400_ObjectIdentity = ObjectIdentity
jnxModuleEX4400 = _JnxModuleEX4400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 165)
)
_JnxEX4400FPC_ObjectIdentity = ObjectIdentity
jnxEX4400FPC = _JnxEX4400FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 165, 1)
)
_JnxEX4400Power_ObjectIdentity = ObjectIdentity
jnxEX4400Power = _JnxEX4400Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 165, 1, 1)
)
_JnxEX4400Fan_ObjectIdentity = ObjectIdentity
jnxEX4400Fan = _JnxEX4400Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 165, 1, 2)
)
_JnxModuleR6675_ObjectIdentity = ObjectIdentity
jnxModuleR6675 = _JnxModuleR6675_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 166)
)
_JnxR6675FPC_ObjectIdentity = ObjectIdentity
jnxR6675FPC = _JnxR6675FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 166, 1)
)
_JnxR6675RE_ObjectIdentity = ObjectIdentity
jnxR6675RE = _JnxR6675RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 166, 2)
)
_JnxR6675Power_ObjectIdentity = ObjectIdentity
jnxR6675Power = _JnxR6675Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 166, 3)
)
_JnxR6675PowerDC_ObjectIdentity = ObjectIdentity
jnxR6675PowerDC = _JnxR6675PowerDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 166, 3, 1)
)
_JnxR6675PowerAC_ObjectIdentity = ObjectIdentity
jnxR6675PowerAC = _JnxR6675PowerAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 166, 3, 2)
)
_JnxR6675Fan_ObjectIdentity = ObjectIdentity
jnxR6675Fan = _JnxR6675Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 166, 4)
)
_JnxModuleMX304_ObjectIdentity = ObjectIdentity
jnxModuleMX304 = _JnxModuleMX304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 167)
)
_JnxMX304HM_ObjectIdentity = ObjectIdentity
jnxMX304HM = _JnxMX304HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 167, 1)
)
_JnxMX304FPC_ObjectIdentity = ObjectIdentity
jnxMX304FPC = _JnxMX304FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 167, 2)
)
_JnxMX304Fan_ObjectIdentity = ObjectIdentity
jnxMX304Fan = _JnxMX304Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 167, 3)
)
_JnxMX304Power_ObjectIdentity = ObjectIdentity
jnxMX304Power = _JnxMX304Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 167, 4)
)
_JnxMX304PMB_ObjectIdentity = ObjectIdentity
jnxMX304PMB = _JnxMX304PMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 167, 5)
)
_JnxMX304SFB_ObjectIdentity = ObjectIdentity
jnxMX304SFB = _JnxMX304SFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 167, 6)
)
_JnxMX304TIB_ObjectIdentity = ObjectIdentity
jnxMX304TIB = _JnxMX304TIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 167, 7)
)
_JnxMX304CBD_ObjectIdentity = ObjectIdentity
jnxMX304CBD = _JnxMX304CBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 167, 8)
)
_JnxModuleMX10004_ObjectIdentity = ObjectIdentity
jnxModuleMX10004 = _JnxModuleMX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 168)
)
_JnxMX10004SFB_ObjectIdentity = ObjectIdentity
jnxMX10004SFB = _JnxMX10004SFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 168, 1)
)
_JnxMX10004HM_ObjectIdentity = ObjectIdentity
jnxMX10004HM = _JnxMX10004HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 168, 2)
)
_JnxMX10004FPC_ObjectIdentity = ObjectIdentity
jnxMX10004FPC = _JnxMX10004FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 168, 3)
)
_JnxMX10004Fan_ObjectIdentity = ObjectIdentity
jnxMX10004Fan = _JnxMX10004Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 168, 4)
)
_JnxMX10004CBD_ObjectIdentity = ObjectIdentity
jnxMX10004CBD = _JnxMX10004CBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 168, 5)
)
_JnxMX10004Power_ObjectIdentity = ObjectIdentity
jnxMX10004Power = _JnxMX10004Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 168, 6)
)
_JnxMX10004FPB_ObjectIdentity = ObjectIdentity
jnxMX10004FPB = _JnxMX10004FPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 168, 7)
)
_JnxMX10004FTC_ObjectIdentity = ObjectIdentity
jnxMX10004FTC = _JnxMX10004FTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 168, 8)
)
_JnxModuleEX4100_ObjectIdentity = ObjectIdentity
jnxModuleEX4100 = _JnxModuleEX4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 169)
)
_JnxEX4100FPC_ObjectIdentity = ObjectIdentity
jnxEX4100FPC = _JnxEX4100FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 169, 1)
)
_JnxEX4100Power_ObjectIdentity = ObjectIdentity
jnxEX4100Power = _JnxEX4100Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 169, 1, 1)
)
_JnxEX4100Fan_ObjectIdentity = ObjectIdentity
jnxEX4100Fan = _JnxEX4100Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 169, 1, 2)
)
_JnxModuleEX4650_ObjectIdentity = ObjectIdentity
jnxModuleEX4650 = _JnxModuleEX4650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 508)
)
_JnxEX4650FPC_ObjectIdentity = ObjectIdentity
jnxEX4650FPC = _JnxEX4650FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 508, 1)
)
_JnxEX4650Power_ObjectIdentity = ObjectIdentity
jnxEX4650Power = _JnxEX4650Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 508, 1, 1)
)
_JnxEX4650Fan_ObjectIdentity = ObjectIdentity
jnxEX4650Fan = _JnxEX4650Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 508, 1, 2)
)
_JnxEX4650RE_ObjectIdentity = ObjectIdentity
jnxEX4650RE = _JnxEX4650RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 508, 1, 3)
)
_JnxModulePTX1000380c_ObjectIdentity = ObjectIdentity
jnxModulePTX1000380c = _JnxModulePTX1000380c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 523)
)
_JnxPTX1000380cRE_ObjectIdentity = ObjectIdentity
jnxPTX1000380cRE = _JnxPTX1000380cRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 523, 1)
)
_JnxPTX1000380cCB_ObjectIdentity = ObjectIdentity
jnxPTX1000380cCB = _JnxPTX1000380cCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 523, 2)
)
_JnxPTX1000380cFPC_ObjectIdentity = ObjectIdentity
jnxPTX1000380cFPC = _JnxPTX1000380cFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 523, 3)
)
_JnxPTX1000380cFan_ObjectIdentity = ObjectIdentity
jnxPTX1000380cFan = _JnxPTX1000380cFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 523, 4)
)
_JnxPTX1000380cFPM_ObjectIdentity = ObjectIdentity
jnxPTX1000380cFPM = _JnxPTX1000380cFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 523, 5)
)
_JnxPTX1000380cSIB_ObjectIdentity = ObjectIdentity
jnxPTX1000380cSIB = _JnxPTX1000380cSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 523, 6)
)
_JnxPTX1000380cPIC_ObjectIdentity = ObjectIdentity
jnxPTX1000380cPIC = _JnxPTX1000380cPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 523, 7)
)
_JnxPTX1000380cPDU_ObjectIdentity = ObjectIdentity
jnxPTX1000380cPDU = _JnxPTX1000380cPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 523, 8)
)
_JnxPTX1000380cPSM_ObjectIdentity = ObjectIdentity
jnxPTX1000380cPSM = _JnxPTX1000380cPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 523, 9)
)
_JnxModulePTX10003160c_ObjectIdentity = ObjectIdentity
jnxModulePTX10003160c = _JnxModulePTX10003160c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 524)
)
_JnxPTX10003160cRE_ObjectIdentity = ObjectIdentity
jnxPTX10003160cRE = _JnxPTX10003160cRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 524, 1)
)
_JnxPTX10003160cCB_ObjectIdentity = ObjectIdentity
jnxPTX10003160cCB = _JnxPTX10003160cCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 524, 2)
)
_JnxPTX10003160cFPC_ObjectIdentity = ObjectIdentity
jnxPTX10003160cFPC = _JnxPTX10003160cFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 524, 3)
)
_JnxPTX10003160cFan_ObjectIdentity = ObjectIdentity
jnxPTX10003160cFan = _JnxPTX10003160cFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 524, 4)
)
_JnxPTX10003160cFPM_ObjectIdentity = ObjectIdentity
jnxPTX10003160cFPM = _JnxPTX10003160cFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 524, 5)
)
_JnxPTX10003160cSIB_ObjectIdentity = ObjectIdentity
jnxPTX10003160cSIB = _JnxPTX10003160cSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 524, 6)
)
_JnxPTX10003160cPIC_ObjectIdentity = ObjectIdentity
jnxPTX10003160cPIC = _JnxPTX10003160cPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 524, 7)
)
_JnxPTX10003160cPDU_ObjectIdentity = ObjectIdentity
jnxPTX10003160cPDU = _JnxPTX10003160cPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 524, 8)
)
_JnxPTX10003160cPSM_ObjectIdentity = ObjectIdentity
jnxPTX10003160cPSM = _JnxPTX10003160cPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 524, 9)
)
_JnxModuleQFX1000380c_ObjectIdentity = ObjectIdentity
jnxModuleQFX1000380c = _JnxModuleQFX1000380c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 525)
)
_JnxQFX1000380cRE_ObjectIdentity = ObjectIdentity
jnxQFX1000380cRE = _JnxQFX1000380cRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 525, 1)
)
_JnxQFX1000380cCB_ObjectIdentity = ObjectIdentity
jnxQFX1000380cCB = _JnxQFX1000380cCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 525, 2)
)
_JnxQFX1000380cFPC_ObjectIdentity = ObjectIdentity
jnxQFX1000380cFPC = _JnxQFX1000380cFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 525, 3)
)
_JnxQFX1000380cFan_ObjectIdentity = ObjectIdentity
jnxQFX1000380cFan = _JnxQFX1000380cFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 525, 4)
)
_JnxQFX1000380cFPM_ObjectIdentity = ObjectIdentity
jnxQFX1000380cFPM = _JnxQFX1000380cFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 525, 5)
)
_JnxQFX1000380cSIB_ObjectIdentity = ObjectIdentity
jnxQFX1000380cSIB = _JnxQFX1000380cSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 525, 6)
)
_JnxQFX1000380cPIC_ObjectIdentity = ObjectIdentity
jnxQFX1000380cPIC = _JnxQFX1000380cPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 525, 7)
)
_JnxQFX1000380cPDU_ObjectIdentity = ObjectIdentity
jnxQFX1000380cPDU = _JnxQFX1000380cPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 525, 8)
)
_JnxQFX1000380cPSM_ObjectIdentity = ObjectIdentity
jnxQFX1000380cPSM = _JnxQFX1000380cPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 525, 9)
)
_JnxModuleQFX10003160c_ObjectIdentity = ObjectIdentity
jnxModuleQFX10003160c = _JnxModuleQFX10003160c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 526)
)
_JnxQFX10003160cRE_ObjectIdentity = ObjectIdentity
jnxQFX10003160cRE = _JnxQFX10003160cRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 526, 1)
)
_JnxQFX10003160cCB_ObjectIdentity = ObjectIdentity
jnxQFX10003160cCB = _JnxQFX10003160cCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 526, 2)
)
_JnxQFX10003160cFPC_ObjectIdentity = ObjectIdentity
jnxQFX10003160cFPC = _JnxQFX10003160cFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 526, 3)
)
_JnxQFX10003160cFan_ObjectIdentity = ObjectIdentity
jnxQFX10003160cFan = _JnxQFX10003160cFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 526, 4)
)
_JnxQFX10003160cFPM_ObjectIdentity = ObjectIdentity
jnxQFX10003160cFPM = _JnxQFX10003160cFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 526, 5)
)
_JnxQFX10003160cSIB_ObjectIdentity = ObjectIdentity
jnxQFX10003160cSIB = _JnxQFX10003160cSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 526, 6)
)
_JnxQFX10003160cPIC_ObjectIdentity = ObjectIdentity
jnxQFX10003160cPIC = _JnxQFX10003160cPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 526, 7)
)
_JnxQFX10003160cPDU_ObjectIdentity = ObjectIdentity
jnxQFX10003160cPDU = _JnxQFX10003160cPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 526, 8)
)
_JnxQFX10003160cPSM_ObjectIdentity = ObjectIdentity
jnxQFX10003160cPSM = _JnxQFX10003160cPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 526, 9)
)
_JnxModulePTX1000136mr_ObjectIdentity = ObjectIdentity
jnxModulePTX1000136mr = _JnxModulePTX1000136mr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 555)
)
_JnxPTX1000136mrRE_ObjectIdentity = ObjectIdentity
jnxPTX1000136mrRE = _JnxPTX1000136mrRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 555, 1)
)
_JnxPTX1000136mrCB_ObjectIdentity = ObjectIdentity
jnxPTX1000136mrCB = _JnxPTX1000136mrCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 555, 2)
)
_JnxPTX1000136mrFPC_ObjectIdentity = ObjectIdentity
jnxPTX1000136mrFPC = _JnxPTX1000136mrFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 555, 3)
)
_JnxPTX1000136mrFan_ObjectIdentity = ObjectIdentity
jnxPTX1000136mrFan = _JnxPTX1000136mrFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 555, 4)
)
_JnxPTX1000136mrSIB_ObjectIdentity = ObjectIdentity
jnxPTX1000136mrSIB = _JnxPTX1000136mrSIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 555, 5)
)
_JnxPTX1000136mrPIC_ObjectIdentity = ObjectIdentity
jnxPTX1000136mrPIC = _JnxPTX1000136mrPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 555, 6)
)
_JnxPTX1000136mrPSM_ObjectIdentity = ObjectIdentity
jnxPTX1000136mrPSM = _JnxPTX1000136mrPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 555, 7)
)
_JnxModulePTX10004_ObjectIdentity = ObjectIdentity
jnxModulePTX10004 = _JnxModulePTX10004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 570)
)
_JnxPTX10004FPC_ObjectIdentity = ObjectIdentity
jnxPTX10004FPC = _JnxPTX10004FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 570, 1)
)
_JnxPTX10004HM_ObjectIdentity = ObjectIdentity
jnxPTX10004HM = _JnxPTX10004HM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 570, 2)
)
_JnxPTX10004Power_ObjectIdentity = ObjectIdentity
jnxPTX10004Power = _JnxPTX10004Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 570, 3)
)
_JnxPTX10004Fan_ObjectIdentity = ObjectIdentity
jnxPTX10004Fan = _JnxPTX10004Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 570, 4)
)
_JnxPTX10004FPB_ObjectIdentity = ObjectIdentity
jnxPTX10004FPB = _JnxPTX10004FPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 570, 5)
)
_JnxPTX10004CBD_ObjectIdentity = ObjectIdentity
jnxPTX10004CBD = _JnxPTX10004CBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 570, 6)
)
_JnxPTX10004SIB_ObjectIdentity = ObjectIdentity
jnxPTX10004SIB = _JnxPTX10004SIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 570, 7)
)
_JnxPTX10004FPM_ObjectIdentity = ObjectIdentity
jnxPTX10004FPM = _JnxPTX10004FPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 570, 8)
)
_JnxPTX10004FTC_ObjectIdentity = ObjectIdentity
jnxPTX10004FTC = _JnxPTX10004FTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 570, 9)
)
_JnxPTX10004Backplane_ObjectIdentity = ObjectIdentity
jnxPTX10004Backplane = _JnxPTX10004Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 570, 10)
)
_JnxModuleACX753_ObjectIdentity = ObjectIdentity
jnxModuleACX753 = _JnxModuleACX753_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 576)
)
_JnxACX753RE_ObjectIdentity = ObjectIdentity
jnxACX753RE = _JnxACX753RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 576, 1)
)
_JnxACX753PSM_ObjectIdentity = ObjectIdentity
jnxACX753PSM = _JnxACX753PSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 576, 2)
)
_JnxACX753Fan_ObjectIdentity = ObjectIdentity
jnxACX753Fan = _JnxACX753Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 576, 3)
)
_JnxACX753CBD_ObjectIdentity = ObjectIdentity
jnxACX753CBD = _JnxACX753CBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 576, 4)
)
_JnxACX753Backplane_ObjectIdentity = ObjectIdentity
jnxACX753Backplane = _JnxACX753Backplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 576, 5)
)
_JnxACX753FPC_ObjectIdentity = ObjectIdentity
jnxACX753FPC = _JnxACX753FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 576, 6)
)
_JnxACX753PIC_ObjectIdentity = ObjectIdentity
jnxACX753PIC = _JnxACX753PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 576, 7)
)
_JnxACX753FEB_ObjectIdentity = ObjectIdentity
jnxACX753FEB = _JnxACX753FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 576, 8)
)
_JnxModuleSRX1600_ObjectIdentity = ObjectIdentity
jnxModuleSRX1600 = _JnxModuleSRX1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 583)
)
_JnxSRX1600FPC_ObjectIdentity = ObjectIdentity
jnxSRX1600FPC = _JnxSRX1600FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 583, 1)
)
_JnxSRX1600RE_ObjectIdentity = ObjectIdentity
jnxSRX1600RE = _JnxSRX1600RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 583, 2)
)
_JnxSRX1600Power_ObjectIdentity = ObjectIdentity
jnxSRX1600Power = _JnxSRX1600Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 583, 3)
)
_JnxSRX1600Fan_ObjectIdentity = ObjectIdentity
jnxSRX1600Fan = _JnxSRX1600Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 583, 4)
)
_JnxSRX1600CBD_ObjectIdentity = ObjectIdentity
jnxSRX1600CBD = _JnxSRX1600CBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 583, 5)
)
_JnxModuleSRX2300_ObjectIdentity = ObjectIdentity
jnxModuleSRX2300 = _JnxModuleSRX2300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 584)
)
_JnxSRX2300FPC_ObjectIdentity = ObjectIdentity
jnxSRX2300FPC = _JnxSRX2300FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 584, 1)
)
_JnxSRX2300RE_ObjectIdentity = ObjectIdentity
jnxSRX2300RE = _JnxSRX2300RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 584, 2)
)
_JnxSRX2300Power_ObjectIdentity = ObjectIdentity
jnxSRX2300Power = _JnxSRX2300Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 584, 3)
)
_JnxSRX2300Fan_ObjectIdentity = ObjectIdentity
jnxSRX2300Fan = _JnxSRX2300Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 584, 4)
)
_JnxSRX2300CBD_ObjectIdentity = ObjectIdentity
jnxSRX2300CBD = _JnxSRX2300CBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 584, 5)
)
_JnxModuleSRX4300_ObjectIdentity = ObjectIdentity
jnxModuleSRX4300 = _JnxModuleSRX4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 585)
)
_JnxSRX4300FPC_ObjectIdentity = ObjectIdentity
jnxSRX4300FPC = _JnxSRX4300FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 585, 1)
)
_JnxSRX4300RE_ObjectIdentity = ObjectIdentity
jnxSRX4300RE = _JnxSRX4300RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 585, 2)
)
_JnxSRX4300Power_ObjectIdentity = ObjectIdentity
jnxSRX4300Power = _JnxSRX4300Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 585, 3)
)
_JnxSRX4300Fan_ObjectIdentity = ObjectIdentity
jnxSRX4300Fan = _JnxSRX4300Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 585, 4)
)
_JnxSRX4300CBD_ObjectIdentity = ObjectIdentity
jnxSRX4300CBD = _JnxSRX4300CBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 585, 5)
)
_JnxModuleACX7332_ObjectIdentity = ObjectIdentity
jnxModuleACX7332 = _JnxModuleACX7332_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 586)
)
_JnxACX7332FPC_ObjectIdentity = ObjectIdentity
jnxACX7332FPC = _JnxACX7332FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 586, 1)
)
_JnxACX7332RE_ObjectIdentity = ObjectIdentity
jnxACX7332RE = _JnxACX7332RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 586, 2)
)
_JnxACX7332Power_ObjectIdentity = ObjectIdentity
jnxACX7332Power = _JnxACX7332Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 586, 3)
)
_JnxACX7332Fan_ObjectIdentity = ObjectIdentity
jnxACX7332Fan = _JnxACX7332Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 586, 4)
)
_JnxACX7332FEB_ObjectIdentity = ObjectIdentity
jnxACX7332FEB = _JnxACX7332FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 586, 5)
)
_JnxACX7332CBD_ObjectIdentity = ObjectIdentity
jnxACX7332CBD = _JnxACX7332CBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 586, 6)
)
_JnxModuleACX7348_ObjectIdentity = ObjectIdentity
jnxModuleACX7348 = _JnxModuleACX7348_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 587)
)
_JnxACX7348FPC_ObjectIdentity = ObjectIdentity
jnxACX7348FPC = _JnxACX7348FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 587, 1)
)
_JnxACX7348RE_ObjectIdentity = ObjectIdentity
jnxACX7348RE = _JnxACX7348RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 587, 2)
)
_JnxACX7348Power_ObjectIdentity = ObjectIdentity
jnxACX7348Power = _JnxACX7348Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 587, 3)
)
_JnxACX7348Fan_ObjectIdentity = ObjectIdentity
jnxACX7348Fan = _JnxACX7348Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 587, 4)
)
_JnxACX7348FEB_ObjectIdentity = ObjectIdentity
jnxACX7348FEB = _JnxACX7348FEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 587, 5)
)
_JnxACX7348CBD_ObjectIdentity = ObjectIdentity
jnxACX7348CBD = _JnxACX7348CBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 587, 6)
)
_JnxModulePTX1000236qdd_ObjectIdentity = ObjectIdentity
jnxModulePTX1000236qdd = _JnxModulePTX1000236qdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 589)
)
_JnxPTX1000236qddRE_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddRE = _JnxPTX1000236qddRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 589, 1)
)
_JnxPTX1000236qddCB_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddCB = _JnxPTX1000236qddCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 589, 2)
)
_JnxPTX1000236qddFPC_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddFPC = _JnxPTX1000236qddFPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 589, 3)
)
_JnxPTX1000236qddFan_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddFan = _JnxPTX1000236qddFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 589, 4)
)
_JnxPTX1000236qddPIC_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddPIC = _JnxPTX1000236qddPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 589, 5)
)
_JnxPTX1000236qddPSM_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddPSM = _JnxPTX1000236qddPSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 589, 6)
)
_JnxPTX1000236qddBackplane_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddBackplane = _JnxPTX1000236qddBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 589, 7)
)
_JnxPTX1000236qddFPM_ObjectIdentity = ObjectIdentity
jnxPTX1000236qddFPM = _JnxPTX1000236qddFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 589, 8)
)
_JnxModuleSRX4700_ObjectIdentity = ObjectIdentity
jnxModuleSRX4700 = _JnxModuleSRX4700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 590)
)
_JnxSRX4700FPC_ObjectIdentity = ObjectIdentity
jnxSRX4700FPC = _JnxSRX4700FPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 590, 1)
)
_JnxSRX4700RE_ObjectIdentity = ObjectIdentity
jnxSRX4700RE = _JnxSRX4700RE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 590, 2)
)
_JnxSRX4700Power_ObjectIdentity = ObjectIdentity
jnxSRX4700Power = _JnxSRX4700Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 590, 3)
)
_JnxSRX4700Fan_ObjectIdentity = ObjectIdentity
jnxSRX4700Fan = _JnxSRX4700Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 590, 4)
)
_JnxSRX4700CBD_ObjectIdentity = ObjectIdentity
jnxSRX4700CBD = _JnxSRX4700CBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 2, 590, 5)
)
_JnxSubmodule_ObjectIdentity = ObjectIdentity
jnxSubmodule = _JnxSubmodule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3)
)
_JnxSubmoduleM40_ObjectIdentity = ObjectIdentity
jnxSubmoduleM40 = _JnxSubmoduleM40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1)
)
_JnxM40PIC0_ObjectIdentity = ObjectIdentity
jnxM40PIC0 = _JnxM40PIC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 2)
)
_JnxM40SonetOc48_ObjectIdentity = ObjectIdentity
jnxM40SonetOc48 = _JnxM40SonetOc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 2, 1)
)
_JnxM40PIC_ObjectIdentity = ObjectIdentity
jnxM40PIC = _JnxM40PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3)
)
_JnxM40QuadSonetOc3_ObjectIdentity = ObjectIdentity
jnxM40QuadSonetOc3 = _JnxM40QuadSonetOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 1)
)
_JnxM40SonetOc12_ObjectIdentity = ObjectIdentity
jnxM40SonetOc12 = _JnxM40SonetOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 2)
)
_JnxM40GigEther_ObjectIdentity = ObjectIdentity
jnxM40GigEther = _JnxM40GigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 3)
)
_JnxM40QuadT3_ObjectIdentity = ObjectIdentity
jnxM40QuadT3 = _JnxM40QuadT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 4)
)
_JnxM40QuadE3_ObjectIdentity = ObjectIdentity
jnxM40QuadE3 = _JnxM40QuadE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 5)
)
_JnxM40DualAtmOc3_ObjectIdentity = ObjectIdentity
jnxM40DualAtmOc3 = _JnxM40DualAtmOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 6)
)
_JnxM40AtmOc12_ObjectIdentity = ObjectIdentity
jnxM40AtmOc12 = _JnxM40AtmOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 7)
)
_JnxM40Tunnel_ObjectIdentity = ObjectIdentity
jnxM40Tunnel = _JnxM40Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 8)
)
_JnxM40ChOc12toDs3_ObjectIdentity = ObjectIdentity
jnxM40ChOc12toDs3 = _JnxM40ChOc12toDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 9)
)
_JnxM40QuadEther_ObjectIdentity = ObjectIdentity
jnxM40QuadEther = _JnxM40QuadEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 10)
)
_JnxM40QuadE1_ObjectIdentity = ObjectIdentity
jnxM40QuadE1 = _JnxM40QuadE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 11)
)
_JnxM40QuadT1_ObjectIdentity = ObjectIdentity
jnxM40QuadT1 = _JnxM40QuadT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 12)
)
_JnxM40SonetOc48Sr_ObjectIdentity = ObjectIdentity
jnxM40SonetOc48Sr = _JnxM40SonetOc48Sr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 13)
)
_JnxM40QuadChT3_ObjectIdentity = ObjectIdentity
jnxM40QuadChT3 = _JnxM40QuadChT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 14)
)
_JnxM40SonetOc48Lr_ObjectIdentity = ObjectIdentity
jnxM40SonetOc48Lr = _JnxM40SonetOc48Lr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 15)
)
_JnxM40QuadAtmE3_ObjectIdentity = ObjectIdentity
jnxM40QuadAtmE3 = _JnxM40QuadAtmE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 16)
)
_JnxM40QuadAtmT3_ObjectIdentity = ObjectIdentity
jnxM40QuadAtmT3 = _JnxM40QuadAtmT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 17)
)
_JnxM40GigEtherBundle_ObjectIdentity = ObjectIdentity
jnxM40GigEtherBundle = _JnxM40GigEtherBundle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 18)
)
_JnxM40Multilink128_ObjectIdentity = ObjectIdentity
jnxM40Multilink128 = _JnxM40Multilink128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 19)
)
_JnxM40Multilink32_ObjectIdentity = ObjectIdentity
jnxM40Multilink32 = _JnxM40Multilink32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 20)
)
_JnxM40Multilink4_ObjectIdentity = ObjectIdentity
jnxM40Multilink4 = _JnxM40Multilink4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 21)
)
_JnxM40ChStm1_ObjectIdentity = ObjectIdentity
jnxM40ChStm1 = _JnxM40ChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 22)
)
_JnxM40DenseEther12_ObjectIdentity = ObjectIdentity
jnxM40DenseEther12 = _JnxM40DenseEther12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 24)
)
_JnxM40DecaChE1_ObjectIdentity = ObjectIdentity
jnxM40DecaChE1 = _JnxM40DecaChE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 25)
)
_JnxM40ChDs3toDs0_ObjectIdentity = ObjectIdentity
jnxM40ChDs3toDs0 = _JnxM40ChDs3toDs0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 26)
)
_JnxM40DualChDs3toDs0_ObjectIdentity = ObjectIdentity
jnxM40DualChDs3toDs0 = _JnxM40DualChDs3toDs0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 27)
)
_JnxM40DenseEther8_ObjectIdentity = ObjectIdentity
jnxM40DenseEther8 = _JnxM40DenseEther8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 28)
)
_JnxM40Crypto800_ObjectIdentity = ObjectIdentity
jnxM40Crypto800 = _JnxM40Crypto800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 30)
)
_JnxM40LsMultilink128_ObjectIdentity = ObjectIdentity
jnxM40LsMultilink128 = _JnxM40LsMultilink128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 32)
)
_JnxM40LsMultilink32_ObjectIdentity = ObjectIdentity
jnxM40LsMultilink32 = _JnxM40LsMultilink32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 33)
)
_JnxM40LsMultilink4_ObjectIdentity = ObjectIdentity
jnxM40LsMultilink4 = _JnxM40LsMultilink4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 34)
)
_JnxM40AtmIIOc12_ObjectIdentity = ObjectIdentity
jnxM40AtmIIOc12 = _JnxM40AtmIIOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 35)
)
_JnxM40DualAtmIIOc3_ObjectIdentity = ObjectIdentity
jnxM40DualAtmIIOc3 = _JnxM40DualAtmIIOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 36)
)
_JnxM40DualQChDS3_ObjectIdentity = ObjectIdentity
jnxM40DualQChDS3 = _JnxM40DualQChDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 37)
)
_JnxM40QuadQChT3_ObjectIdentity = ObjectIdentity
jnxM40QuadQChT3 = _JnxM40QuadQChT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 38)
)
_JnxM40QChOc12_ObjectIdentity = ObjectIdentity
jnxM40QChOc12 = _JnxM40QChOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 39)
)
_JnxM40QChStm1_ObjectIdentity = ObjectIdentity
jnxM40QChStm1 = _JnxM40QChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 40)
)
_JnxM40DualQChStm1_ObjectIdentity = ObjectIdentity
jnxM40DualQChStm1 = _JnxM40DualQChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 41)
)
_JnxM40DecaQChE1_ObjectIdentity = ObjectIdentity
jnxM40DecaQChE1 = _JnxM40DecaQChE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 42)
)
_JnxM40DualEIA530_ObjectIdentity = ObjectIdentity
jnxM40DualEIA530 = _JnxM40DualEIA530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 43)
)
_JnxM40DecaQChT1_ObjectIdentity = ObjectIdentity
jnxM40DecaQChT1 = _JnxM40DecaQChT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 1, 3, 44)
)
_JnxSubmoduleM20_ObjectIdentity = ObjectIdentity
jnxSubmoduleM20 = _JnxSubmoduleM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2)
)
_JnxM20PIC0_ObjectIdentity = ObjectIdentity
jnxM20PIC0 = _JnxM20PIC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 1)
)
_JnxM20SonetOc48_ObjectIdentity = ObjectIdentity
jnxM20SonetOc48 = _JnxM20SonetOc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 1, 1)
)
_JnxM20PIC_ObjectIdentity = ObjectIdentity
jnxM20PIC = _JnxM20PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2)
)
_JnxM20QuadSonetOc3_ObjectIdentity = ObjectIdentity
jnxM20QuadSonetOc3 = _JnxM20QuadSonetOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 1)
)
_JnxM20SonetOc12_ObjectIdentity = ObjectIdentity
jnxM20SonetOc12 = _JnxM20SonetOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 2)
)
_JnxM20GigEther_ObjectIdentity = ObjectIdentity
jnxM20GigEther = _JnxM20GigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 3)
)
_JnxM20QuadT3_ObjectIdentity = ObjectIdentity
jnxM20QuadT3 = _JnxM20QuadT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 4)
)
_JnxM20QuadE3_ObjectIdentity = ObjectIdentity
jnxM20QuadE3 = _JnxM20QuadE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 5)
)
_JnxM20DualAtmOc3_ObjectIdentity = ObjectIdentity
jnxM20DualAtmOc3 = _JnxM20DualAtmOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 6)
)
_JnxM20AtmOc12_ObjectIdentity = ObjectIdentity
jnxM20AtmOc12 = _JnxM20AtmOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 7)
)
_JnxM20Tunnel_ObjectIdentity = ObjectIdentity
jnxM20Tunnel = _JnxM20Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 8)
)
_JnxM20ChOc12toDs3_ObjectIdentity = ObjectIdentity
jnxM20ChOc12toDs3 = _JnxM20ChOc12toDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 9)
)
_JnxM20QuadEther_ObjectIdentity = ObjectIdentity
jnxM20QuadEther = _JnxM20QuadEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 10)
)
_JnxM20QuadE1_ObjectIdentity = ObjectIdentity
jnxM20QuadE1 = _JnxM20QuadE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 11)
)
_JnxM20QuadT1_ObjectIdentity = ObjectIdentity
jnxM20QuadT1 = _JnxM20QuadT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 12)
)
_JnxM20SonetOc48Sr_ObjectIdentity = ObjectIdentity
jnxM20SonetOc48Sr = _JnxM20SonetOc48Sr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 13)
)
_JnxM20QuadChT3_ObjectIdentity = ObjectIdentity
jnxM20QuadChT3 = _JnxM20QuadChT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 14)
)
_JnxM20SonetOc48Lr_ObjectIdentity = ObjectIdentity
jnxM20SonetOc48Lr = _JnxM20SonetOc48Lr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 15)
)
_JnxM20QuadAtmE3_ObjectIdentity = ObjectIdentity
jnxM20QuadAtmE3 = _JnxM20QuadAtmE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 16)
)
_JnxM20QuadAtmT3_ObjectIdentity = ObjectIdentity
jnxM20QuadAtmT3 = _JnxM20QuadAtmT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 17)
)
_JnxM20GigEtherBundle_ObjectIdentity = ObjectIdentity
jnxM20GigEtherBundle = _JnxM20GigEtherBundle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 18)
)
_JnxM20Multilink128_ObjectIdentity = ObjectIdentity
jnxM20Multilink128 = _JnxM20Multilink128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 19)
)
_JnxM20Multilink32_ObjectIdentity = ObjectIdentity
jnxM20Multilink32 = _JnxM20Multilink32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 20)
)
_JnxM20Multilink4_ObjectIdentity = ObjectIdentity
jnxM20Multilink4 = _JnxM20Multilink4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 21)
)
_JnxM20ChStm1_ObjectIdentity = ObjectIdentity
jnxM20ChStm1 = _JnxM20ChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 22)
)
_JnxM20DenseEther12_ObjectIdentity = ObjectIdentity
jnxM20DenseEther12 = _JnxM20DenseEther12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 24)
)
_JnxM20DecaChE1_ObjectIdentity = ObjectIdentity
jnxM20DecaChE1 = _JnxM20DecaChE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 25)
)
_JnxM20ChDs3toDs0_ObjectIdentity = ObjectIdentity
jnxM20ChDs3toDs0 = _JnxM20ChDs3toDs0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 26)
)
_JnxM20DualChDs3toDs0_ObjectIdentity = ObjectIdentity
jnxM20DualChDs3toDs0 = _JnxM20DualChDs3toDs0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 27)
)
_JnxM20DenseEther8_ObjectIdentity = ObjectIdentity
jnxM20DenseEther8 = _JnxM20DenseEther8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 28)
)
_JnxM20Crypto800_ObjectIdentity = ObjectIdentity
jnxM20Crypto800 = _JnxM20Crypto800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 30)
)
_JnxM20GgsnControl_ObjectIdentity = ObjectIdentity
jnxM20GgsnControl = _JnxM20GgsnControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 31)
)
_JnxM20GgsnData_ObjectIdentity = ObjectIdentity
jnxM20GgsnData = _JnxM20GgsnData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 32)
)
_JnxM20LsMultilink128_ObjectIdentity = ObjectIdentity
jnxM20LsMultilink128 = _JnxM20LsMultilink128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 34)
)
_JnxM20LsMultilink32_ObjectIdentity = ObjectIdentity
jnxM20LsMultilink32 = _JnxM20LsMultilink32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 35)
)
_JnxM20LsMultilink4_ObjectIdentity = ObjectIdentity
jnxM20LsMultilink4 = _JnxM20LsMultilink4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 36)
)
_JnxM20AtmIIOc12_ObjectIdentity = ObjectIdentity
jnxM20AtmIIOc12 = _JnxM20AtmIIOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 37)
)
_JnxM20DualAtmIIOc3_ObjectIdentity = ObjectIdentity
jnxM20DualAtmIIOc3 = _JnxM20DualAtmIIOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 38)
)
_JnxM20DualQChDS3_ObjectIdentity = ObjectIdentity
jnxM20DualQChDS3 = _JnxM20DualQChDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 39)
)
_JnxM20QuadQChT3_ObjectIdentity = ObjectIdentity
jnxM20QuadQChT3 = _JnxM20QuadQChT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 40)
)
_JnxM20QChOc12_ObjectIdentity = ObjectIdentity
jnxM20QChOc12 = _JnxM20QChOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 41)
)
_JnxM20QChStm1_ObjectIdentity = ObjectIdentity
jnxM20QChStm1 = _JnxM20QChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 42)
)
_JnxM20DualQChStm1_ObjectIdentity = ObjectIdentity
jnxM20DualQChStm1 = _JnxM20DualQChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 43)
)
_JnxM20DecaQChE1_ObjectIdentity = ObjectIdentity
jnxM20DecaQChE1 = _JnxM20DecaQChE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 44)
)
_JnxM20DualEIA530_ObjectIdentity = ObjectIdentity
jnxM20DualEIA530 = _JnxM20DualEIA530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 45)
)
_JnxM20PassiveMonitor_ObjectIdentity = ObjectIdentity
jnxM20PassiveMonitor = _JnxM20PassiveMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 46)
)
_JnxM20DecaQChT1_ObjectIdentity = ObjectIdentity
jnxM20DecaQChT1 = _JnxM20DecaQChT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 2, 2, 47)
)
_JnxSubmoduleM160_ObjectIdentity = ObjectIdentity
jnxSubmoduleM160 = _JnxSubmoduleM160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3)
)
_JnxM160SubSFM_ObjectIdentity = ObjectIdentity
jnxM160SubSFM = _JnxM160SubSFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 2)
)
_JnxM160SPP_ObjectIdentity = ObjectIdentity
jnxM160SPP = _JnxM160SPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 2, 1)
)
_JnxM160SPR_ObjectIdentity = ObjectIdentity
jnxM160SPR = _JnxM160SPR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 2, 2)
)
_JnxM160SubFPM_ObjectIdentity = ObjectIdentity
jnxM160SubFPM = _JnxM160SubFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 3)
)
_JnxM160FPMCMB_ObjectIdentity = ObjectIdentity
jnxM160FPMCMB = _JnxM160FPMCMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 3, 1)
)
_JnxM160FPMDisplay_ObjectIdentity = ObjectIdentity
jnxM160FPMDisplay = _JnxM160FPMDisplay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 3, 2)
)
_JnxM160PIC0_ObjectIdentity = ObjectIdentity
jnxM160PIC0 = _JnxM160PIC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 4)
)
_JnxM160SonetOc192Sr_ObjectIdentity = ObjectIdentity
jnxM160SonetOc192Sr = _JnxM160SonetOc192Sr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 4, 1)
)
_JnxM160SonetOc192Sr2_ObjectIdentity = ObjectIdentity
jnxM160SonetOc192Sr2 = _JnxM160SonetOc192Sr2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 4, 2)
)
_JnxM160SonetOc192Lr1_ObjectIdentity = ObjectIdentity
jnxM160SonetOc192Lr1 = _JnxM160SonetOc192Lr1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 4, 3)
)
_JnxM160PIC1_ObjectIdentity = ObjectIdentity
jnxM160PIC1 = _JnxM160PIC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5)
)
_JnxM160QuadSonetOc3_ObjectIdentity = ObjectIdentity
jnxM160QuadSonetOc3 = _JnxM160QuadSonetOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 1)
)
_JnxM160SonetOc12_ObjectIdentity = ObjectIdentity
jnxM160SonetOc12 = _JnxM160SonetOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 2)
)
_JnxM160GigEther_ObjectIdentity = ObjectIdentity
jnxM160GigEther = _JnxM160GigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 3)
)
_JnxM160QuadT3_ObjectIdentity = ObjectIdentity
jnxM160QuadT3 = _JnxM160QuadT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 4)
)
_JnxM160QuadE3_ObjectIdentity = ObjectIdentity
jnxM160QuadE3 = _JnxM160QuadE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 5)
)
_JnxM160DualAtmOc3_ObjectIdentity = ObjectIdentity
jnxM160DualAtmOc3 = _JnxM160DualAtmOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 6)
)
_JnxM160AtmOc12_ObjectIdentity = ObjectIdentity
jnxM160AtmOc12 = _JnxM160AtmOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 7)
)
_JnxM160ChOc12toDs3_ObjectIdentity = ObjectIdentity
jnxM160ChOc12toDs3 = _JnxM160ChOc12toDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 8)
)
_JnxM160QuadEther_ObjectIdentity = ObjectIdentity
jnxM160QuadEther = _JnxM160QuadEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 9)
)
_JnxM160QuadE1_ObjectIdentity = ObjectIdentity
jnxM160QuadE1 = _JnxM160QuadE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 10)
)
_JnxM160QuadT1_ObjectIdentity = ObjectIdentity
jnxM160QuadT1 = _JnxM160QuadT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 11)
)
_JnxM160QuadChT3_ObjectIdentity = ObjectIdentity
jnxM160QuadChT3 = _JnxM160QuadChT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 12)
)
_JnxM160QuadAtmE3_ObjectIdentity = ObjectIdentity
jnxM160QuadAtmE3 = _JnxM160QuadAtmE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 13)
)
_JnxM160QuadAtmT3_ObjectIdentity = ObjectIdentity
jnxM160QuadAtmT3 = _JnxM160QuadAtmT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 14)
)
_JnxM160GigEtherBundle_ObjectIdentity = ObjectIdentity
jnxM160GigEtherBundle = _JnxM160GigEtherBundle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 15)
)
_JnxM160ChStm1_ObjectIdentity = ObjectIdentity
jnxM160ChStm1 = _JnxM160ChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 16)
)
_JnxM160DecaChE1_ObjectIdentity = ObjectIdentity
jnxM160DecaChE1 = _JnxM160DecaChE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 17)
)
_JnxM160ChDs3toDs0_ObjectIdentity = ObjectIdentity
jnxM160ChDs3toDs0 = _JnxM160ChDs3toDs0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 18)
)
_JnxM160DualChDs3toDs0_ObjectIdentity = ObjectIdentity
jnxM160DualChDs3toDs0 = _JnxM160DualChDs3toDs0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 19)
)
_JnxM160DenseEther8_ObjectIdentity = ObjectIdentity
jnxM160DenseEther8 = _JnxM160DenseEther8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 20)
)
_JnxM160AtmIIOc12_ObjectIdentity = ObjectIdentity
jnxM160AtmIIOc12 = _JnxM160AtmIIOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 23)
)
_JnxM160DualAtmIIOc3_ObjectIdentity = ObjectIdentity
jnxM160DualAtmIIOc3 = _JnxM160DualAtmIIOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 24)
)
_JnxM160DualQChDS3_ObjectIdentity = ObjectIdentity
jnxM160DualQChDS3 = _JnxM160DualQChDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 25)
)
_JnxM160QuadQChT3_ObjectIdentity = ObjectIdentity
jnxM160QuadQChT3 = _JnxM160QuadQChT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 26)
)
_JnxM160QChOc12_ObjectIdentity = ObjectIdentity
jnxM160QChOc12 = _JnxM160QChOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 27)
)
_JnxM160QChStm1_ObjectIdentity = ObjectIdentity
jnxM160QChStm1 = _JnxM160QChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 28)
)
_JnxM160DualQChStm1_ObjectIdentity = ObjectIdentity
jnxM160DualQChStm1 = _JnxM160DualQChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 29)
)
_JnxM160DecaQChE1_ObjectIdentity = ObjectIdentity
jnxM160DecaQChE1 = _JnxM160DecaQChE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 30)
)
_JnxM160DualEIA530_ObjectIdentity = ObjectIdentity
jnxM160DualEIA530 = _JnxM160DualEIA530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 31)
)
_JnxM160PassiveMonitor_ObjectIdentity = ObjectIdentity
jnxM160PassiveMonitor = _JnxM160PassiveMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 32)
)
_JnxM160DecaQChT1_ObjectIdentity = ObjectIdentity
jnxM160DecaQChT1 = _JnxM160DecaQChT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 5, 33)
)
_JnxM160PIC2_ObjectIdentity = ObjectIdentity
jnxM160PIC2 = _JnxM160PIC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 6)
)
_JnxM160SonetOc48Sr_ObjectIdentity = ObjectIdentity
jnxM160SonetOc48Sr = _JnxM160SonetOc48Sr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 6, 1)
)
_JnxM160Tunnel_ObjectIdentity = ObjectIdentity
jnxM160Tunnel = _JnxM160Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 6, 2)
)
_JnxM160DualGigEther_ObjectIdentity = ObjectIdentity
jnxM160DualGigEther = _JnxM160DualGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 6, 3)
)
_JnxM160QuadSonetOc12_ObjectIdentity = ObjectIdentity
jnxM160QuadSonetOc12 = _JnxM160QuadSonetOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 6, 4)
)
_JnxM160SonetOc48Lr_ObjectIdentity = ObjectIdentity
jnxM160SonetOc48Lr = _JnxM160SonetOc48Lr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 6, 5)
)
_JnxM160DenseEther48_ObjectIdentity = ObjectIdentity
jnxM160DenseEther48 = _JnxM160DenseEther48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 6, 6)
)
_JnxM160QuadGigEther_ObjectIdentity = ObjectIdentity
jnxM160QuadGigEther = _JnxM160QuadGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 6, 7)
)
_JnxM160Crypto800_ObjectIdentity = ObjectIdentity
jnxM160Crypto800 = _JnxM160Crypto800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 6, 9)
)
_JnxM160QuadOc3_ObjectIdentity = ObjectIdentity
jnxM160QuadOc3 = _JnxM160QuadOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 6, 10)
)
_JnxM160DualQHGE_ObjectIdentity = ObjectIdentity
jnxM160DualQHGE = _JnxM160DualQHGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 6, 11)
)
_JnxM160DualAtmIIOc12_ObjectIdentity = ObjectIdentity
jnxM160DualAtmIIOc12 = _JnxM160DualAtmIIOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 3, 6, 12)
)
_JnxSubmoduleM10_ObjectIdentity = ObjectIdentity
jnxSubmoduleM10 = _JnxSubmoduleM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4)
)
_JnxM10PIC_ObjectIdentity = ObjectIdentity
jnxM10PIC = _JnxM10PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1)
)
_JnxM10QuadSonetOc3_ObjectIdentity = ObjectIdentity
jnxM10QuadSonetOc3 = _JnxM10QuadSonetOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 1)
)
_JnxM10SonetOc12_ObjectIdentity = ObjectIdentity
jnxM10SonetOc12 = _JnxM10SonetOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 2)
)
_JnxM10GigEther_ObjectIdentity = ObjectIdentity
jnxM10GigEther = _JnxM10GigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 3)
)
_JnxM10QuadT3_ObjectIdentity = ObjectIdentity
jnxM10QuadT3 = _JnxM10QuadT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 4)
)
_JnxM10QuadE3_ObjectIdentity = ObjectIdentity
jnxM10QuadE3 = _JnxM10QuadE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 5)
)
_JnxM10DualAtmOc3_ObjectIdentity = ObjectIdentity
jnxM10DualAtmOc3 = _JnxM10DualAtmOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 6)
)
_JnxM10AtmOc12_ObjectIdentity = ObjectIdentity
jnxM10AtmOc12 = _JnxM10AtmOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 7)
)
_JnxM10Tunnel_ObjectIdentity = ObjectIdentity
jnxM10Tunnel = _JnxM10Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 8)
)
_JnxM10ChOc12toDs3_ObjectIdentity = ObjectIdentity
jnxM10ChOc12toDs3 = _JnxM10ChOc12toDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 9)
)
_JnxM10QuadEther_ObjectIdentity = ObjectIdentity
jnxM10QuadEther = _JnxM10QuadEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 10)
)
_JnxM10QuadE1_ObjectIdentity = ObjectIdentity
jnxM10QuadE1 = _JnxM10QuadE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 11)
)
_JnxM10QuadT1_ObjectIdentity = ObjectIdentity
jnxM10QuadT1 = _JnxM10QuadT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 12)
)
_JnxM10SonetOc48Sr_ObjectIdentity = ObjectIdentity
jnxM10SonetOc48Sr = _JnxM10SonetOc48Sr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 13)
)
_JnxM10QuadChT3_ObjectIdentity = ObjectIdentity
jnxM10QuadChT3 = _JnxM10QuadChT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 14)
)
_JnxM10SonetOc48Lr_ObjectIdentity = ObjectIdentity
jnxM10SonetOc48Lr = _JnxM10SonetOc48Lr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 15)
)
_JnxM10QuadAtmE3_ObjectIdentity = ObjectIdentity
jnxM10QuadAtmE3 = _JnxM10QuadAtmE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 16)
)
_JnxM10QuadAtmT3_ObjectIdentity = ObjectIdentity
jnxM10QuadAtmT3 = _JnxM10QuadAtmT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 17)
)
_JnxM10GigEtherBundle_ObjectIdentity = ObjectIdentity
jnxM10GigEtherBundle = _JnxM10GigEtherBundle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 18)
)
_JnxM10Multilink128_ObjectIdentity = ObjectIdentity
jnxM10Multilink128 = _JnxM10Multilink128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 19)
)
_JnxM10Multilink32_ObjectIdentity = ObjectIdentity
jnxM10Multilink32 = _JnxM10Multilink32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 20)
)
_JnxM10Multilink4_ObjectIdentity = ObjectIdentity
jnxM10Multilink4 = _JnxM10Multilink4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 21)
)
_JnxM10ChStm1_ObjectIdentity = ObjectIdentity
jnxM10ChStm1 = _JnxM10ChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 22)
)
_JnxM10DualChDs3_ObjectIdentity = ObjectIdentity
jnxM10DualChDs3 = _JnxM10DualChDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 23)
)
_JnxM10DualDs3_ObjectIdentity = ObjectIdentity
jnxM10DualDs3 = _JnxM10DualDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 24)
)
_JnxM10DualSonetOc3_ObjectIdentity = ObjectIdentity
jnxM10DualSonetOc3 = _JnxM10DualSonetOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 25)
)
_JnxM10DualE3_ObjectIdentity = ObjectIdentity
jnxM10DualE3 = _JnxM10DualE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 26)
)
_JnxM10DenseEther12_ObjectIdentity = ObjectIdentity
jnxM10DenseEther12 = _JnxM10DenseEther12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 28)
)
_JnxM10DecaChE1_ObjectIdentity = ObjectIdentity
jnxM10DecaChE1 = _JnxM10DecaChE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 29)
)
_JnxM10ChDs3toDs0_ObjectIdentity = ObjectIdentity
jnxM10ChDs3toDs0 = _JnxM10ChDs3toDs0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 30)
)
_JnxM10DualChDs3toDs0_ObjectIdentity = ObjectIdentity
jnxM10DualChDs3toDs0 = _JnxM10DualChDs3toDs0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 31)
)
_JnxM10DenseEther8_ObjectIdentity = ObjectIdentity
jnxM10DenseEther8 = _JnxM10DenseEther8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 32)
)
_JnxM10Crypto800_ObjectIdentity = ObjectIdentity
jnxM10Crypto800 = _JnxM10Crypto800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 34)
)
_JnxM10LsMultilink128_ObjectIdentity = ObjectIdentity
jnxM10LsMultilink128 = _JnxM10LsMultilink128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 36)
)
_JnxM10LsMultilink32_ObjectIdentity = ObjectIdentity
jnxM10LsMultilink32 = _JnxM10LsMultilink32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 37)
)
_JnxM10LsMultilink4_ObjectIdentity = ObjectIdentity
jnxM10LsMultilink4 = _JnxM10LsMultilink4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 38)
)
_JnxM10AtmIIOc12_ObjectIdentity = ObjectIdentity
jnxM10AtmIIOc12 = _JnxM10AtmIIOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 39)
)
_JnxM10DualAtmIIOc3_ObjectIdentity = ObjectIdentity
jnxM10DualAtmIIOc3 = _JnxM10DualAtmIIOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 40)
)
_JnxM10DualQChDs3_ObjectIdentity = ObjectIdentity
jnxM10DualQChDs3 = _JnxM10DualQChDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 41)
)
_JnxM10QuadQChT3_ObjectIdentity = ObjectIdentity
jnxM10QuadQChT3 = _JnxM10QuadQChT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 42)
)
_JnxM10QChOc12_ObjectIdentity = ObjectIdentity
jnxM10QChOc12 = _JnxM10QChOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 43)
)
_JnxM10QChStm1_ObjectIdentity = ObjectIdentity
jnxM10QChStm1 = _JnxM10QChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 44)
)
_JnxM10DualQChStm1_ObjectIdentity = ObjectIdentity
jnxM10DualQChStm1 = _JnxM10DualQChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 45)
)
_JnxM10DecaQChE1_ObjectIdentity = ObjectIdentity
jnxM10DecaQChE1 = _JnxM10DecaQChE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 46)
)
_JnxM10DualEIA530_ObjectIdentity = ObjectIdentity
jnxM10DualEIA530 = _JnxM10DualEIA530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 47)
)
_JnxM10DecaQChT1_ObjectIdentity = ObjectIdentity
jnxM10DecaQChT1 = _JnxM10DecaQChT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 4, 1, 48)
)
_JnxSubmoduleM5_ObjectIdentity = ObjectIdentity
jnxSubmoduleM5 = _JnxSubmoduleM5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5)
)
_JnxM5PIC_ObjectIdentity = ObjectIdentity
jnxM5PIC = _JnxM5PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1)
)
_JnxM5QuadSonetOc3_ObjectIdentity = ObjectIdentity
jnxM5QuadSonetOc3 = _JnxM5QuadSonetOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 1)
)
_JnxM5SonetOc12_ObjectIdentity = ObjectIdentity
jnxM5SonetOc12 = _JnxM5SonetOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 2)
)
_JnxM5GigEther_ObjectIdentity = ObjectIdentity
jnxM5GigEther = _JnxM5GigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 3)
)
_JnxM5QuadT3_ObjectIdentity = ObjectIdentity
jnxM5QuadT3 = _JnxM5QuadT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 4)
)
_JnxM5QuadE3_ObjectIdentity = ObjectIdentity
jnxM5QuadE3 = _JnxM5QuadE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 5)
)
_JnxM5DualAtmOc3_ObjectIdentity = ObjectIdentity
jnxM5DualAtmOc3 = _JnxM5DualAtmOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 6)
)
_JnxM5AtmOc12_ObjectIdentity = ObjectIdentity
jnxM5AtmOc12 = _JnxM5AtmOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 7)
)
_JnxM5Tunnel_ObjectIdentity = ObjectIdentity
jnxM5Tunnel = _JnxM5Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 8)
)
_JnxM5ChOc12toDs3_ObjectIdentity = ObjectIdentity
jnxM5ChOc12toDs3 = _JnxM5ChOc12toDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 9)
)
_JnxM5QuadEther_ObjectIdentity = ObjectIdentity
jnxM5QuadEther = _JnxM5QuadEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 10)
)
_JnxM5QuadE1_ObjectIdentity = ObjectIdentity
jnxM5QuadE1 = _JnxM5QuadE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 11)
)
_JnxM5QuadT1_ObjectIdentity = ObjectIdentity
jnxM5QuadT1 = _JnxM5QuadT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 12)
)
_JnxM5QuadChT3_ObjectIdentity = ObjectIdentity
jnxM5QuadChT3 = _JnxM5QuadChT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 14)
)
_JnxM5QuadAtmE3_ObjectIdentity = ObjectIdentity
jnxM5QuadAtmE3 = _JnxM5QuadAtmE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 16)
)
_JnxM5QuadAtmT3_ObjectIdentity = ObjectIdentity
jnxM5QuadAtmT3 = _JnxM5QuadAtmT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 17)
)
_JnxM5GigEtherBundle_ObjectIdentity = ObjectIdentity
jnxM5GigEtherBundle = _JnxM5GigEtherBundle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 18)
)
_JnxM5Multilink128_ObjectIdentity = ObjectIdentity
jnxM5Multilink128 = _JnxM5Multilink128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 19)
)
_JnxM5Multilink32_ObjectIdentity = ObjectIdentity
jnxM5Multilink32 = _JnxM5Multilink32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 20)
)
_JnxM5Multilink4_ObjectIdentity = ObjectIdentity
jnxM5Multilink4 = _JnxM5Multilink4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 21)
)
_JnxM5ChStm1_ObjectIdentity = ObjectIdentity
jnxM5ChStm1 = _JnxM5ChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 22)
)
_JnxM5DualChDs3_ObjectIdentity = ObjectIdentity
jnxM5DualChDs3 = _JnxM5DualChDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 23)
)
_JnxM5DualDs3_ObjectIdentity = ObjectIdentity
jnxM5DualDs3 = _JnxM5DualDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 24)
)
_JnxM5DualSonetOc3_ObjectIdentity = ObjectIdentity
jnxM5DualSonetOc3 = _JnxM5DualSonetOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 25)
)
_JnxM5DualE3_ObjectIdentity = ObjectIdentity
jnxM5DualE3 = _JnxM5DualE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 26)
)
_JnxM5DenseEther12_ObjectIdentity = ObjectIdentity
jnxM5DenseEther12 = _JnxM5DenseEther12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 28)
)
_JnxM5DecaChE1_ObjectIdentity = ObjectIdentity
jnxM5DecaChE1 = _JnxM5DecaChE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 29)
)
_JnxM5ChDs3toDs0_ObjectIdentity = ObjectIdentity
jnxM5ChDs3toDs0 = _JnxM5ChDs3toDs0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 30)
)
_JnxM5DualChDs3toDs0_ObjectIdentity = ObjectIdentity
jnxM5DualChDs3toDs0 = _JnxM5DualChDs3toDs0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 31)
)
_JnxM5DenseEther8_ObjectIdentity = ObjectIdentity
jnxM5DenseEther8 = _JnxM5DenseEther8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 32)
)
_JnxM5Crypto800_ObjectIdentity = ObjectIdentity
jnxM5Crypto800 = _JnxM5Crypto800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 34)
)
_JnxM5LsMultilink128_ObjectIdentity = ObjectIdentity
jnxM5LsMultilink128 = _JnxM5LsMultilink128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 36)
)
_JnxM5LsMultilink32_ObjectIdentity = ObjectIdentity
jnxM5LsMultilink32 = _JnxM5LsMultilink32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 37)
)
_JnxM5LsMultilink4_ObjectIdentity = ObjectIdentity
jnxM5LsMultilink4 = _JnxM5LsMultilink4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 38)
)
_JnxM5AtmIIOc12_ObjectIdentity = ObjectIdentity
jnxM5AtmIIOc12 = _JnxM5AtmIIOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 39)
)
_JnxM5DualAtmIIOc3_ObjectIdentity = ObjectIdentity
jnxM5DualAtmIIOc3 = _JnxM5DualAtmIIOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 40)
)
_JnxM5DualQChDs3_ObjectIdentity = ObjectIdentity
jnxM5DualQChDs3 = _JnxM5DualQChDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 41)
)
_JnxM5QuadQChT3_ObjectIdentity = ObjectIdentity
jnxM5QuadQChT3 = _JnxM5QuadQChT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 42)
)
_JnxM5QChOc12_ObjectIdentity = ObjectIdentity
jnxM5QChOc12 = _JnxM5QChOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 43)
)
_JnxM5QChStm1_ObjectIdentity = ObjectIdentity
jnxM5QChStm1 = _JnxM5QChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 44)
)
_JnxM5DualQChStm1_ObjectIdentity = ObjectIdentity
jnxM5DualQChStm1 = _JnxM5DualQChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 45)
)
_JnxM5DecaQChE1_ObjectIdentity = ObjectIdentity
jnxM5DecaQChE1 = _JnxM5DecaQChE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 46)
)
_JnxM5DualEIA530_ObjectIdentity = ObjectIdentity
jnxM5DualEIA530 = _JnxM5DualEIA530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 47)
)
_JnxM5DecaQChT1_ObjectIdentity = ObjectIdentity
jnxM5DecaQChT1 = _JnxM5DecaQChT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 5, 1, 48)
)
_JnxSubmoduleT640_ObjectIdentity = ObjectIdentity
jnxSubmoduleT640 = _JnxSubmoduleT640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6)
)
_JnxT640PIC0_ObjectIdentity = ObjectIdentity
jnxT640PIC0 = _JnxT640PIC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 1)
)
_JnxT640PIC1_ObjectIdentity = ObjectIdentity
jnxT640PIC1 = _JnxT640PIC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 2)
)
_JnxT640PIC2_ObjectIdentity = ObjectIdentity
jnxT640PIC2 = _JnxT640PIC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 3)
)
_JnxT640DualGigEther_ObjectIdentity = ObjectIdentity
jnxT640DualGigEther = _JnxT640DualGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 3, 1)
)
_JnxT640QuadGigEther_ObjectIdentity = ObjectIdentity
jnxT640QuadGigEther = _JnxT640QuadGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 3, 2)
)
_JnxT640QuadSonetOc12_ObjectIdentity = ObjectIdentity
jnxT640QuadSonetOc12 = _JnxT640QuadSonetOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 3, 3)
)
_JnxT640SonetOc48Sr_ObjectIdentity = ObjectIdentity
jnxT640SonetOc48Sr = _JnxT640SonetOc48Sr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 3, 4)
)
_JnxT640SonetOc48Lr_ObjectIdentity = ObjectIdentity
jnxT640SonetOc48Lr = _JnxT640SonetOc48Lr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 3, 5)
)
_JnxT640DualAtmIIOc12_ObjectIdentity = ObjectIdentity
jnxT640DualAtmIIOc12 = _JnxT640DualAtmIIOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 3, 6)
)
_JnxT640QuadOc3_ObjectIdentity = ObjectIdentity
jnxT640QuadOc3 = _JnxT640QuadOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 3, 7)
)
_JnxT640DualQHGE_ObjectIdentity = ObjectIdentity
jnxT640DualQHGE = _JnxT640DualQHGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 3, 8)
)
_JnxT640PIC3_ObjectIdentity = ObjectIdentity
jnxT640PIC3 = _JnxT640PIC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 4)
)
_JnxT640SonetOc192Sr2_ObjectIdentity = ObjectIdentity
jnxT640SonetOc192Sr2 = _JnxT640SonetOc192Sr2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 4, 1)
)
_JnxT640Tunnel_ObjectIdentity = ObjectIdentity
jnxT640Tunnel = _JnxT640Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 4, 2)
)
_JnxT640QuadSonetOc48_ObjectIdentity = ObjectIdentity
jnxT640QuadSonetOc48 = _JnxT640QuadSonetOc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 4, 3)
)
_JnxT640SonetOc192Vsr_ObjectIdentity = ObjectIdentity
jnxT640SonetOc192Vsr = _JnxT640SonetOc192Vsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 4, 4)
)
_JnxT640SonetOc192Lr_ObjectIdentity = ObjectIdentity
jnxT640SonetOc192Lr = _JnxT640SonetOc192Lr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 4, 5)
)
_JnxT640TenGigEther_ObjectIdentity = ObjectIdentity
jnxT640TenGigEther = _JnxT640TenGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 4, 6)
)
_JnxT640NX1GigEther_ObjectIdentity = ObjectIdentity
jnxT640NX1GigEther = _JnxT640NX1GigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 6, 4, 7)
)
_JnxSubmoduleT320_ObjectIdentity = ObjectIdentity
jnxSubmoduleT320 = _JnxSubmoduleT320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7)
)
_JnxT320PIC0_ObjectIdentity = ObjectIdentity
jnxT320PIC0 = _JnxT320PIC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 1)
)
_JnxT320PIC1_ObjectIdentity = ObjectIdentity
jnxT320PIC1 = _JnxT320PIC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 2)
)
_JnxT320DualAtmIIOc3_ObjectIdentity = ObjectIdentity
jnxT320DualAtmIIOc3 = _JnxT320DualAtmIIOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 2, 1)
)
_JnxT320QuadSonetOc3_ObjectIdentity = ObjectIdentity
jnxT320QuadSonetOc3 = _JnxT320QuadSonetOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 2, 3)
)
_JnxT320DualAtmOc3_ObjectIdentity = ObjectIdentity
jnxT320DualAtmOc3 = _JnxT320DualAtmOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 2, 4)
)
_JnxT320AtmOc12_ObjectIdentity = ObjectIdentity
jnxT320AtmOc12 = _JnxT320AtmOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 2, 5)
)
_JnxT320QuadEther_ObjectIdentity = ObjectIdentity
jnxT320QuadEther = _JnxT320QuadEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 2, 6)
)
_JnxT320SonetOc12_ObjectIdentity = ObjectIdentity
jnxT320SonetOc12 = _JnxT320SonetOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 2, 7)
)
_JnxT320AtmIIOc12_ObjectIdentity = ObjectIdentity
jnxT320AtmIIOc12 = _JnxT320AtmIIOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 2, 8)
)
_JnxT320PIC2_ObjectIdentity = ObjectIdentity
jnxT320PIC2 = _JnxT320PIC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 3)
)
_JnxT320DualGigEther_ObjectIdentity = ObjectIdentity
jnxT320DualGigEther = _JnxT320DualGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 3, 1)
)
_JnxT320QuadGigEther_ObjectIdentity = ObjectIdentity
jnxT320QuadGigEther = _JnxT320QuadGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 3, 2)
)
_JnxT320QuadSonetOc12_ObjectIdentity = ObjectIdentity
jnxT320QuadSonetOc12 = _JnxT320QuadSonetOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 3, 3)
)
_JnxT320SonetOc48Sr_ObjectIdentity = ObjectIdentity
jnxT320SonetOc48Sr = _JnxT320SonetOc48Sr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 3, 4)
)
_JnxT320SonetOc48Lr_ObjectIdentity = ObjectIdentity
jnxT320SonetOc48Lr = _JnxT320SonetOc48Lr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 3, 5)
)
_JnxT320DualAtmIIOc12_ObjectIdentity = ObjectIdentity
jnxT320DualAtmIIOc12 = _JnxT320DualAtmIIOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 3, 6)
)
_JnxT320QuadOc3_ObjectIdentity = ObjectIdentity
jnxT320QuadOc3 = _JnxT320QuadOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 3, 7)
)
_JnxT320DualQHGE_ObjectIdentity = ObjectIdentity
jnxT320DualQHGE = _JnxT320DualQHGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 3, 8)
)
_JnxT320PIC3_ObjectIdentity = ObjectIdentity
jnxT320PIC3 = _JnxT320PIC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 4)
)
_JnxT320SonetOc192Sr2_ObjectIdentity = ObjectIdentity
jnxT320SonetOc192Sr2 = _JnxT320SonetOc192Sr2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 4, 1)
)
_JnxT320Tunnel_ObjectIdentity = ObjectIdentity
jnxT320Tunnel = _JnxT320Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 4, 2)
)
_JnxT320QuadSonetOc48_ObjectIdentity = ObjectIdentity
jnxT320QuadSonetOc48 = _JnxT320QuadSonetOc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 4, 3)
)
_JnxT320SonetOc192Vsr_ObjectIdentity = ObjectIdentity
jnxT320SonetOc192Vsr = _JnxT320SonetOc192Vsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 4, 4)
)
_JnxT320SonetOc192Lr_ObjectIdentity = ObjectIdentity
jnxT320SonetOc192Lr = _JnxT320SonetOc192Lr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 4, 5)
)
_JnxT320TenGigEther_ObjectIdentity = ObjectIdentity
jnxT320TenGigEther = _JnxT320TenGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 4, 6)
)
_JnxT320NX1GigEther_ObjectIdentity = ObjectIdentity
jnxT320NX1GigEther = _JnxT320NX1GigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 7, 4, 7)
)
_JnxSubmoduleM40e_ObjectIdentity = ObjectIdentity
jnxSubmoduleM40e = _JnxSubmoduleM40e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8)
)
_JnxM40eSubSFM_ObjectIdentity = ObjectIdentity
jnxM40eSubSFM = _JnxM40eSubSFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 2)
)
_JnxM40eSPP_ObjectIdentity = ObjectIdentity
jnxM40eSPP = _JnxM40eSPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 2, 1)
)
_JnxM40eSPR_ObjectIdentity = ObjectIdentity
jnxM40eSPR = _JnxM40eSPR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 2, 2)
)
_JnxM40eSubFPM_ObjectIdentity = ObjectIdentity
jnxM40eSubFPM = _JnxM40eSubFPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 3)
)
_JnxM40eFPMCMB_ObjectIdentity = ObjectIdentity
jnxM40eFPMCMB = _JnxM40eFPMCMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 3, 1)
)
_JnxM40eFPMDisplay_ObjectIdentity = ObjectIdentity
jnxM40eFPMDisplay = _JnxM40eFPMDisplay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 3, 2)
)
_JnxM40ePIC0_ObjectIdentity = ObjectIdentity
jnxM40ePIC0 = _JnxM40ePIC0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 4)
)
_JnxM40ePIC1_ObjectIdentity = ObjectIdentity
jnxM40ePIC1 = _JnxM40ePIC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5)
)
_JnxM40eQuadSonetOc3_ObjectIdentity = ObjectIdentity
jnxM40eQuadSonetOc3 = _JnxM40eQuadSonetOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 1)
)
_JnxM40eSonetOc12_ObjectIdentity = ObjectIdentity
jnxM40eSonetOc12 = _JnxM40eSonetOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 2)
)
_JnxM40eGigEther_ObjectIdentity = ObjectIdentity
jnxM40eGigEther = _JnxM40eGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 3)
)
_JnxM40eQuadT3_ObjectIdentity = ObjectIdentity
jnxM40eQuadT3 = _JnxM40eQuadT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 4)
)
_JnxM40eQuadE3_ObjectIdentity = ObjectIdentity
jnxM40eQuadE3 = _JnxM40eQuadE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 5)
)
_JnxM40eDualAtmOc3_ObjectIdentity = ObjectIdentity
jnxM40eDualAtmOc3 = _JnxM40eDualAtmOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 6)
)
_JnxM40eAtmOc12_ObjectIdentity = ObjectIdentity
jnxM40eAtmOc12 = _JnxM40eAtmOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 7)
)
_JnxM40eChOc12toDs3_ObjectIdentity = ObjectIdentity
jnxM40eChOc12toDs3 = _JnxM40eChOc12toDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 8)
)
_JnxM40eQuadEther_ObjectIdentity = ObjectIdentity
jnxM40eQuadEther = _JnxM40eQuadEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 9)
)
_JnxM40eQuadE1_ObjectIdentity = ObjectIdentity
jnxM40eQuadE1 = _JnxM40eQuadE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 10)
)
_JnxM40eQuadT1_ObjectIdentity = ObjectIdentity
jnxM40eQuadT1 = _JnxM40eQuadT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 11)
)
_JnxM40eQuadChT3_ObjectIdentity = ObjectIdentity
jnxM40eQuadChT3 = _JnxM40eQuadChT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 12)
)
_JnxM40eQuadAtmE3_ObjectIdentity = ObjectIdentity
jnxM40eQuadAtmE3 = _JnxM40eQuadAtmE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 13)
)
_JnxM40eQuadAtmT3_ObjectIdentity = ObjectIdentity
jnxM40eQuadAtmT3 = _JnxM40eQuadAtmT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 14)
)
_JnxM40eGigEtherBundle_ObjectIdentity = ObjectIdentity
jnxM40eGigEtherBundle = _JnxM40eGigEtherBundle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 15)
)
_JnxM40eChStm1_ObjectIdentity = ObjectIdentity
jnxM40eChStm1 = _JnxM40eChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 16)
)
_JnxM40eDecaChE1_ObjectIdentity = ObjectIdentity
jnxM40eDecaChE1 = _JnxM40eDecaChE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 17)
)
_JnxM40eChDs3toDs0_ObjectIdentity = ObjectIdentity
jnxM40eChDs3toDs0 = _JnxM40eChDs3toDs0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 18)
)
_JnxM40eDualChDs3toDs0_ObjectIdentity = ObjectIdentity
jnxM40eDualChDs3toDs0 = _JnxM40eDualChDs3toDs0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 19)
)
_JnxM40eDenseEther8_ObjectIdentity = ObjectIdentity
jnxM40eDenseEther8 = _JnxM40eDenseEther8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 20)
)
_JnxM40eAtmIIOc12_ObjectIdentity = ObjectIdentity
jnxM40eAtmIIOc12 = _JnxM40eAtmIIOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 23)
)
_JnxM40eDualAtmIIOc3_ObjectIdentity = ObjectIdentity
jnxM40eDualAtmIIOc3 = _JnxM40eDualAtmIIOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 24)
)
_JnxM40eDualQChDS3_ObjectIdentity = ObjectIdentity
jnxM40eDualQChDS3 = _JnxM40eDualQChDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 25)
)
_JnxM40eQuadQChT3_ObjectIdentity = ObjectIdentity
jnxM40eQuadQChT3 = _JnxM40eQuadQChT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 26)
)
_JnxM40eLsMultilink128_ObjectIdentity = ObjectIdentity
jnxM40eLsMultilink128 = _JnxM40eLsMultilink128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 27)
)
_JnxM40eLsMultilink32_ObjectIdentity = ObjectIdentity
jnxM40eLsMultilink32 = _JnxM40eLsMultilink32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 28)
)
_JnxM40eLsMultilink4_ObjectIdentity = ObjectIdentity
jnxM40eLsMultilink4 = _JnxM40eLsMultilink4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 29)
)
_JnxM40eQChOc12_ObjectIdentity = ObjectIdentity
jnxM40eQChOc12 = _JnxM40eQChOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 30)
)
_JnxM40eQChStm1_ObjectIdentity = ObjectIdentity
jnxM40eQChStm1 = _JnxM40eQChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 31)
)
_JnxM40eDualQChStm1_ObjectIdentity = ObjectIdentity
jnxM40eDualQChStm1 = _JnxM40eDualQChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 32)
)
_JnxM40eDecaQChE1_ObjectIdentity = ObjectIdentity
jnxM40eDecaQChE1 = _JnxM40eDecaQChE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 33)
)
_JnxM40eDualEIA530_ObjectIdentity = ObjectIdentity
jnxM40eDualEIA530 = _JnxM40eDualEIA530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 34)
)
_JnxM40ePassiveMonitor_ObjectIdentity = ObjectIdentity
jnxM40ePassiveMonitor = _JnxM40ePassiveMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 35)
)
_JnxM40eMultilink128_ObjectIdentity = ObjectIdentity
jnxM40eMultilink128 = _JnxM40eMultilink128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 36)
)
_JnxM40eMultilink32_ObjectIdentity = ObjectIdentity
jnxM40eMultilink32 = _JnxM40eMultilink32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 37)
)
_JnxM40eMultilink4_ObjectIdentity = ObjectIdentity
jnxM40eMultilink4 = _JnxM40eMultilink4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 38)
)
_JnxM40eDenseEther12_ObjectIdentity = ObjectIdentity
jnxM40eDenseEther12 = _JnxM40eDenseEther12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 39)
)
_JnxM40eDecaQChT1_ObjectIdentity = ObjectIdentity
jnxM40eDecaQChT1 = _JnxM40eDecaQChT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 5, 40)
)
_JnxM40ePIC2_ObjectIdentity = ObjectIdentity
jnxM40ePIC2 = _JnxM40ePIC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 6)
)
_JnxM40eSonetOc48Sr_ObjectIdentity = ObjectIdentity
jnxM40eSonetOc48Sr = _JnxM40eSonetOc48Sr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 6, 1)
)
_JnxM40eTunnel_ObjectIdentity = ObjectIdentity
jnxM40eTunnel = _JnxM40eTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 6, 2)
)
_JnxM40eDualGigEther_ObjectIdentity = ObjectIdentity
jnxM40eDualGigEther = _JnxM40eDualGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 6, 3)
)
_JnxM40eQuadSonetOc12_ObjectIdentity = ObjectIdentity
jnxM40eQuadSonetOc12 = _JnxM40eQuadSonetOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 6, 4)
)
_JnxM40eSonetOc48Lr_ObjectIdentity = ObjectIdentity
jnxM40eSonetOc48Lr = _JnxM40eSonetOc48Lr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 6, 5)
)
_JnxM40eDenseEther48_ObjectIdentity = ObjectIdentity
jnxM40eDenseEther48 = _JnxM40eDenseEther48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 6, 6)
)
_JnxM40eQuadGigEther_ObjectIdentity = ObjectIdentity
jnxM40eQuadGigEther = _JnxM40eQuadGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 6, 7)
)
_JnxM40eCrypto800_ObjectIdentity = ObjectIdentity
jnxM40eCrypto800 = _JnxM40eCrypto800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 6, 9)
)
_JnxM40eQuadOc3_ObjectIdentity = ObjectIdentity
jnxM40eQuadOc3 = _JnxM40eQuadOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 6, 10)
)
_JnxM40eDualQHGE_ObjectIdentity = ObjectIdentity
jnxM40eDualQHGE = _JnxM40eDualQHGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 6, 11)
)
_JnxM40eDualAtmIIOc12_ObjectIdentity = ObjectIdentity
jnxM40eDualAtmIIOc12 = _JnxM40eDualAtmIIOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 8, 6, 12)
)
_JnxSubmoduleM7i_ObjectIdentity = ObjectIdentity
jnxSubmoduleM7i = _JnxSubmoduleM7i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 10)
)
_JnxM7iPIC_ObjectIdentity = ObjectIdentity
jnxM7iPIC = _JnxM7iPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 10, 2)
)
_JnxSubmoduleGeneric_ObjectIdentity = ObjectIdentity
jnxSubmoduleGeneric = _JnxSubmoduleGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12)
)
_JnxPic_ObjectIdentity = ObjectIdentity
jnxPic = _JnxPic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1)
)
_JnxPicType3TenGigEther_ObjectIdentity = ObjectIdentity
jnxPicType3TenGigEther = _JnxPicType3TenGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 1)
)
_JnxPicChDs3toDs0_ObjectIdentity = ObjectIdentity
jnxPicChDs3toDs0 = _JnxPicChDs3toDs0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 2)
)
_JnxPicDualChDs3toDs0_ObjectIdentity = ObjectIdentity
jnxPicDualChDs3toDs0 = _JnxPicDualChDs3toDs0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 3)
)
_JnxPicAtmIIOc12_ObjectIdentity = ObjectIdentity
jnxPicAtmIIOc12 = _JnxPicAtmIIOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 4)
)
_JnxPicAtmOc12_ObjectIdentity = ObjectIdentity
jnxPicAtmOc12 = _JnxPicAtmOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 5)
)
_JnxPicM7iTunnel_ObjectIdentity = ObjectIdentity
jnxPicM7iTunnel = _JnxPicM7iTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 6)
)
_JnxPicChOc12toDs3_ObjectIdentity = ObjectIdentity
jnxPicChOc12toDs3 = _JnxPicChOc12toDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 7)
)
_JnxPicCrypto800_ObjectIdentity = ObjectIdentity
jnxPicCrypto800 = _JnxPicCrypto800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 8)
)
_JnxPicType2DualAtmIIOc12_ObjectIdentity = ObjectIdentity
jnxPicType2DualAtmIIOc12 = _JnxPicType2DualAtmIIOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 9)
)
_JnxPicDualAtmIIOc3_ObjectIdentity = ObjectIdentity
jnxPicDualAtmIIOc3 = _JnxPicDualAtmIIOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 10)
)
_JnxPicDualAtmOc3_ObjectIdentity = ObjectIdentity
jnxPicDualAtmOc3 = _JnxPicDualAtmOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 11)
)
_JnxPicDualChDs3_ObjectIdentity = ObjectIdentity
jnxPicDualChDs3 = _JnxPicDualChDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 12)
)
_JnxPicDualE3_ObjectIdentity = ObjectIdentity
jnxPicDualE3 = _JnxPicDualE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 13)
)
_JnxPicDualEia530_ObjectIdentity = ObjectIdentity
jnxPicDualEia530 = _JnxPicDualEia530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 14)
)
_JnxPicDualQChStm1_ObjectIdentity = ObjectIdentity
jnxPicDualQChStm1 = _JnxPicDualQChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 15)
)
_JnxPicDualQChDs3_ObjectIdentity = ObjectIdentity
jnxPicDualQChDs3 = _JnxPicDualQChDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 16)
)
_JnxPicType2DualQHGE_ObjectIdentity = ObjectIdentity
jnxPicType2DualQHGE = _JnxPicType2DualQHGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 17)
)
_JnxPicDualSonetOc3_ObjectIdentity = ObjectIdentity
jnxPicDualSonetOc3 = _JnxPicDualSonetOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 18)
)
_JnxPicDualDs3_ObjectIdentity = ObjectIdentity
jnxPicDualDs3 = _JnxPicDualDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 19)
)
_JnxPicType1Tunnel_ObjectIdentity = ObjectIdentity
jnxPicType1Tunnel = _JnxPicType1Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 20)
)
_JnxPicGgsnControl_ObjectIdentity = ObjectIdentity
jnxPicGgsnControl = _JnxPicGgsnControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 21)
)
_JnxPicGgsnData_ObjectIdentity = ObjectIdentity
jnxPicGgsnData = _JnxPicGgsnData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 22)
)
_JnxPicType3TenPortGigEther_ObjectIdentity = ObjectIdentity
jnxPicType3TenPortGigEther = _JnxPicType3TenPortGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 23)
)
_JnxPicType3SonetOc192Lr_ObjectIdentity = ObjectIdentity
jnxPicType3SonetOc192Lr = _JnxPicType3SonetOc192Lr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 24)
)
_JnxPicType3SonetOc192Sr2_ObjectIdentity = ObjectIdentity
jnxPicType3SonetOc192Sr2 = _JnxPicType3SonetOc192Sr2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 25)
)
_JnxPicType3SonetOc192Vsr_ObjectIdentity = ObjectIdentity
jnxPicType3SonetOc192Vsr = _JnxPicType3SonetOc192Vsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 26)
)
_JnxPicType3QuadSonetOc48_ObjectIdentity = ObjectIdentity
jnxPicType3QuadSonetOc48 = _JnxPicType3QuadSonetOc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 27)
)
_JnxPicType3Tunnel_ObjectIdentity = ObjectIdentity
jnxPicType3Tunnel = _JnxPicType3Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 28)
)
_JnxPicGigEther_ObjectIdentity = ObjectIdentity
jnxPicGigEther = _JnxPicGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 29)
)
_JnxPicLsMultilink128_ObjectIdentity = ObjectIdentity
jnxPicLsMultilink128 = _JnxPicLsMultilink128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 30)
)
_JnxPicLsMultilink32_ObjectIdentity = ObjectIdentity
jnxPicLsMultilink32 = _JnxPicLsMultilink32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 31)
)
_JnxPicLsMultilink4_ObjectIdentity = ObjectIdentity
jnxPicLsMultilink4 = _JnxPicLsMultilink4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 32)
)
_JnxPicType2DenseEther48_ObjectIdentity = ObjectIdentity
jnxPicType2DenseEther48 = _JnxPicType2DenseEther48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 33)
)
_JnxPicType2DualGigEther_ObjectIdentity = ObjectIdentity
jnxPicType2DualGigEther = _JnxPicType2DualGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 34)
)
_JnxPicType2SonetOc48Lr_ObjectIdentity = ObjectIdentity
jnxPicType2SonetOc48Lr = _JnxPicType2SonetOc48Lr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 35)
)
_JnxPicType2QuadGigEther_ObjectIdentity = ObjectIdentity
jnxPicType2QuadGigEther = _JnxPicType2QuadGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 36)
)
_JnxPicType2QuadSonetOc12_ObjectIdentity = ObjectIdentity
jnxPicType2QuadSonetOc12 = _JnxPicType2QuadSonetOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 37)
)
_JnxPicType2QuadSonetOc3_ObjectIdentity = ObjectIdentity
jnxPicType2QuadSonetOc3 = _JnxPicType2QuadSonetOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 38)
)
_JnxPicType1SonetOc192Sr2_ObjectIdentity = ObjectIdentity
jnxPicType1SonetOc192Sr2 = _JnxPicType1SonetOc192Sr2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 39)
)
_JnxPicType1SonetOc192Lr1_ObjectIdentity = ObjectIdentity
jnxPicType1SonetOc192Lr1 = _JnxPicType1SonetOc192Lr1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 40)
)
_JnxPicType1SonetOc192Sr_ObjectIdentity = ObjectIdentity
jnxPicType1SonetOc192Sr = _JnxPicType1SonetOc192Sr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 41)
)
_JnxPicType1SonetOc192Vsr_ObjectIdentity = ObjectIdentity
jnxPicType1SonetOc192Vsr = _JnxPicType1SonetOc192Vsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 42)
)
_JnxPicType2SonetOc48Sr_ObjectIdentity = ObjectIdentity
jnxPicType2SonetOc48Sr = _JnxPicType2SonetOc48Sr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 43)
)
_JnxPicType2Tunnel_ObjectIdentity = ObjectIdentity
jnxPicType2Tunnel = _JnxPicType2Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 44)
)
_JnxPicDecaChE1_ObjectIdentity = ObjectIdentity
jnxPicDecaChE1 = _JnxPicDecaChE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 45)
)
_JnxPicDenseEther12_ObjectIdentity = ObjectIdentity
jnxPicDenseEther12 = _JnxPicDenseEther12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 46)
)
_JnxPicDenseEtherFX8_ObjectIdentity = ObjectIdentity
jnxPicDenseEtherFX8 = _JnxPicDenseEtherFX8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 48)
)
_JnxPicGigEtherBundle_ObjectIdentity = ObjectIdentity
jnxPicGigEtherBundle = _JnxPicGigEtherBundle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 49)
)
_JnxPicSonetOc48Lr_ObjectIdentity = ObjectIdentity
jnxPicSonetOc48Lr = _JnxPicSonetOc48Lr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 50)
)
_JnxPicSonetOc48Sr_ObjectIdentity = ObjectIdentity
jnxPicSonetOc48Sr = _JnxPicSonetOc48Sr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 51)
)
_JnxPicMultilink128_ObjectIdentity = ObjectIdentity
jnxPicMultilink128 = _JnxPicMultilink128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 52)
)
_JnxPicMultilink32_ObjectIdentity = ObjectIdentity
jnxPicMultilink32 = _JnxPicMultilink32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 53)
)
_JnxPicMultilink4_ObjectIdentity = ObjectIdentity
jnxPicMultilink4 = _JnxPicMultilink4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 54)
)
_JnxPicPassiveMonitor_ObjectIdentity = ObjectIdentity
jnxPicPassiveMonitor = _JnxPicPassiveMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 55)
)
_JnxPicDecaQChE1_ObjectIdentity = ObjectIdentity
jnxPicDecaQChE1 = _JnxPicDecaQChE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 56)
)
_JnxPicQChOc12_ObjectIdentity = ObjectIdentity
jnxPicQChOc12 = _JnxPicQChOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 57)
)
_JnxPicQuadAtmE3_ObjectIdentity = ObjectIdentity
jnxPicQuadAtmE3 = _JnxPicQuadAtmE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 58)
)
_JnxPicQuadAtmT3_ObjectIdentity = ObjectIdentity
jnxPicQuadAtmT3 = _JnxPicQuadAtmT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 59)
)
_JnxPicQuadChT3_ObjectIdentity = ObjectIdentity
jnxPicQuadChT3 = _JnxPicQuadChT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 60)
)
_JnxPicQuadE1_ObjectIdentity = ObjectIdentity
jnxPicQuadE1 = _JnxPicQuadE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 61)
)
_JnxPicQuadE3_ObjectIdentity = ObjectIdentity
jnxPicQuadE3 = _JnxPicQuadE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 62)
)
_JnxPicQuadEther_ObjectIdentity = ObjectIdentity
jnxPicQuadEther = _JnxPicQuadEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 63)
)
_JnxPicQuadQChT3_ObjectIdentity = ObjectIdentity
jnxPicQuadQChT3 = _JnxPicQuadQChT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 64)
)
_JnxPicQuadSonetOc3_ObjectIdentity = ObjectIdentity
jnxPicQuadSonetOc3 = _JnxPicQuadSonetOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 65)
)
_JnxPicQuadT1_ObjectIdentity = ObjectIdentity
jnxPicQuadT1 = _JnxPicQuadT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 66)
)
_JnxPicQuadT3_ObjectIdentity = ObjectIdentity
jnxPicQuadT3 = _JnxPicQuadT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 67)
)
_JnxPicChStm1_ObjectIdentity = ObjectIdentity
jnxPicChStm1 = _JnxPicChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 68)
)
_JnxPicQChStm1_ObjectIdentity = ObjectIdentity
jnxPicQChStm1 = _JnxPicQChStm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 69)
)
_JnxPicSingleQHGE_ObjectIdentity = ObjectIdentity
jnxPicSingleQHGE = _JnxPicSingleQHGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 70)
)
_JnxPicSonetOc12_ObjectIdentity = ObjectIdentity
jnxPicSonetOc12 = _JnxPicSonetOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 71)
)
_JnxPicSonetOc48_ObjectIdentity = ObjectIdentity
jnxPicSonetOc48 = _JnxPicSonetOc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 72)
)
_JnxPicTunnel_ObjectIdentity = ObjectIdentity
jnxPicTunnel = _JnxPicTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 73)
)
_JnxPicGeneralServices_ObjectIdentity = ObjectIdentity
jnxPicGeneralServices = _JnxPicGeneralServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 74)
)
_JnxPicPassiveMonitorAsp_ObjectIdentity = ObjectIdentity
jnxPicPassiveMonitorAsp = _JnxPicPassiveMonitorAsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 75)
)
_JnxPicType1TenGigEther_ObjectIdentity = ObjectIdentity
jnxPicType1TenGigEther = _JnxPicType1TenGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 76)
)
_JnxPicDualATMIIE3_ObjectIdentity = ObjectIdentity
jnxPicDualATMIIE3 = _JnxPicDualATMIIE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 77)
)
_JnxPicQuadATMIIE3_ObjectIdentity = ObjectIdentity
jnxPicQuadATMIIE3 = _JnxPicQuadATMIIE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 78)
)
_JnxPicQuadATMIIT3_ObjectIdentity = ObjectIdentity
jnxPicQuadATMIIT3 = _JnxPicQuadATMIIT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 79)
)
_JnxPicQuadQE3_ObjectIdentity = ObjectIdentity
jnxPicQuadQE3 = _JnxPicQuadQE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 80)
)
_JnxPicType1Oc48SFP_ObjectIdentity = ObjectIdentity
jnxPicType1Oc48SFP = _JnxPicType1Oc48SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 81)
)
_JnxPicType2Oc48SFP_ObjectIdentity = ObjectIdentity
jnxPicType2Oc48SFP = _JnxPicType2Oc48SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 82)
)
_JnxPicGgsnInspection_ObjectIdentity = ObjectIdentity
jnxPicGgsnInspection = _JnxPicGgsnInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 83)
)
_JnxPicType3QuadSonetOc48SFP_ObjectIdentity = ObjectIdentity
jnxPicType3QuadSonetOc48SFP = _JnxPicType3QuadSonetOc48SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 84)
)
_JnxPicType3TenGigEtherXenpak_ObjectIdentity = ObjectIdentity
jnxPicType3TenGigEtherXenpak = _JnxPicType3TenGigEtherXenpak_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 85)
)
_JnxPicIntServices_ObjectIdentity = ObjectIdentity
jnxPicIntServices = _JnxPicIntServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 86)
)
_JnxPicDualFicFE_ObjectIdentity = ObjectIdentity
jnxPicDualFicFE = _JnxPicDualFicFE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 87)
)
_JnxPicFicGE_ObjectIdentity = ObjectIdentity
jnxPicFicGE = _JnxPicFicGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 88)
)
_JnxPicSingleSGE_ObjectIdentity = ObjectIdentity
jnxPicSingleSGE = _JnxPicSingleSGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 89)
)
_JnxPicDualSGE_ObjectIdentity = ObjectIdentity
jnxPicDualSGE = _JnxPicDualSGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 90)
)
_JnxPicQuadSGE_ObjectIdentity = ObjectIdentity
jnxPicQuadSGE = _JnxPicQuadSGE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 91)
)
_JnxPicType3SonetOc192Sr1_ObjectIdentity = ObjectIdentity
jnxPicType3SonetOc192Sr1 = _JnxPicType3SonetOc192Sr1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 92)
)
_JnxPicAdaptiveServicesII_ObjectIdentity = ObjectIdentity
jnxPicAdaptiveServicesII = _JnxPicAdaptiveServicesII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 93)
)
_JnxPicJseriesEthT1Combo_ObjectIdentity = ObjectIdentity
jnxPicJseriesEthT1Combo = _JnxPicJseriesEthT1Combo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 94)
)
_JnxPicJseriesEthE1Combo_ObjectIdentity = ObjectIdentity
jnxPicJseriesEthE1Combo = _JnxPicJseriesEthE1Combo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 95)
)
_JnxPicJseriesEthSerCombo_ObjectIdentity = ObjectIdentity
jnxPicJseriesEthSerCombo = _JnxPicJseriesEthSerCombo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 96)
)
_JnxPicJseriesDualEth_ObjectIdentity = ObjectIdentity
jnxPicJseriesDualEth = _JnxPicJseriesDualEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 97)
)
_JnxPicJseriesDualT1_ObjectIdentity = ObjectIdentity
jnxPicJseriesDualT1 = _JnxPicJseriesDualT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 98)
)
_JnxPicJseriesDualE1_ObjectIdentity = ObjectIdentity
jnxPicJseriesDualE1 = _JnxPicJseriesDualE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 99)
)
_JnxPicJseriesDualSerial_ObjectIdentity = ObjectIdentity
jnxPicJseriesDualSerial = _JnxPicJseriesDualSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 100)
)
_JnxPicJseriesT3_ObjectIdentity = ObjectIdentity
jnxPicJseriesT3 = _JnxPicJseriesT3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 101)
)
_JnxPicType2AtmIIOc48_ObjectIdentity = ObjectIdentity
jnxPicType2AtmIIOc48 = _JnxPicType2AtmIIOc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 102)
)
_JnxPicSonetOc768Sr_ObjectIdentity = ObjectIdentity
jnxPicSonetOc768Sr = _JnxPicSonetOc768Sr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 103)
)
_JnxPicQuadSonetOc192XFP_ObjectIdentity = ObjectIdentity
jnxPicQuadSonetOc192XFP = _JnxPicQuadSonetOc192XFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 104)
)
_JnxPicType4Tunnel_ObjectIdentity = ObjectIdentity
jnxPicType4Tunnel = _JnxPicType4Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 105)
)
_JnxPicQChoc3_ObjectIdentity = ObjectIdentity
jnxPicQChoc3 = _JnxPicQChoc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 106)
)
_JnxPicType3DWDMTenGigEther_ObjectIdentity = ObjectIdentity
jnxPicType3DWDMTenGigEther = _JnxPicType3DWDMTenGigEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 108)
)
_JnxPicType4QuadOC192_ObjectIdentity = ObjectIdentity
jnxPicType4QuadOC192 = _JnxPicType4QuadOC192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 109)
)
_JnxPicType1Load_ObjectIdentity = ObjectIdentity
jnxPicType1Load = _JnxPicType1Load_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 111)
)
_JnxPicType2Load_ObjectIdentity = ObjectIdentity
jnxPicType2Load = _JnxPicType2Load_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 112)
)
_JnxPicType3Load_ObjectIdentity = ObjectIdentity
jnxPicType3Load = _JnxPicType3Load_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 113)
)
_JnxPicType4Load_ObjectIdentity = ObjectIdentity
jnxPicType4Load = _JnxPicType4Load_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 114)
)
_JnxPicGgsnControlV1_ObjectIdentity = ObjectIdentity
jnxPicGgsnControlV1 = _JnxPicGgsnControlV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 115)
)
_JnxPicGgsnDataV1_ObjectIdentity = ObjectIdentity
jnxPicGgsnDataV1 = _JnxPicGgsnDataV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 116)
)
_JnxPicMonitoring3_ObjectIdentity = ObjectIdentity
jnxPicMonitoring3 = _JnxPicMonitoring3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 117)
)
_JnxPicGgsnPhoenix_ObjectIdentity = ObjectIdentity
jnxPicGgsnPhoenix = _JnxPicGgsnPhoenix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 118)
)
_JnxPicAdaptiveServicesFips_ObjectIdentity = ObjectIdentity
jnxPicAdaptiveServicesFips = _JnxPicAdaptiveServicesFips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 119)
)
_JnxPicMonitoring3V1_ObjectIdentity = ObjectIdentity
jnxPicMonitoring3V1 = _JnxPicMonitoring3V1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 120)
)
_JnxPicGgsnPhoenixV1_ObjectIdentity = ObjectIdentity
jnxPicGgsnPhoenixV1 = _JnxPicGgsnPhoenixV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 121)
)
_JnxPicJseriesE3_ObjectIdentity = ObjectIdentity
jnxPicJseriesE3 = _JnxPicJseriesE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 122)
)
_JnxPicLinkServicesII_ObjectIdentity = ObjectIdentity
jnxPicLinkServicesII = _JnxPicLinkServicesII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 123)
)
_JnxPicDecaQChT1_ObjectIdentity = ObjectIdentity
jnxPicDecaQChT1 = _JnxPicDecaQChT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 124)
)
_JnxPicType3IQ21X10GE_ObjectIdentity = ObjectIdentity
jnxPicType3IQ21X10GE = _JnxPicType3IQ21X10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 125)
)
_JnxPicType2IQ28X1GE_ObjectIdentity = ObjectIdentity
jnxPicType2IQ28X1GE = _JnxPicType2IQ28X1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 126)
)
_JnxPicType1IQ24X1GE_ObjectIdentity = ObjectIdentity
jnxPicType1IQ24X1GE = _JnxPicType1IQ24X1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 127)
)
_JnxPic10GEUplink_ObjectIdentity = ObjectIdentity
jnxPic10GEUplink = _JnxPic10GEUplink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 128)
)
_JnxPicType2IQ21X10GE_ObjectIdentity = ObjectIdentity
jnxPicType2IQ21X10GE = _JnxPicType2IQ21X10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 129)
)
_JnxPicType1MultiServices_ObjectIdentity = ObjectIdentity
jnxPicType1MultiServices = _JnxPicType1MultiServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 130)
)
_JnxPicType2MultiServices_ObjectIdentity = ObjectIdentity
jnxPicType2MultiServices = _JnxPicType2MultiServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 131)
)
_JnxPicType3MultiServices_ObjectIdentity = ObjectIdentity
jnxPicType3MultiServices = _JnxPicType3MultiServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 132)
)
_JnxPicSonetOc192Uplink_ObjectIdentity = ObjectIdentity
jnxPicSonetOc192Uplink = _JnxPicSonetOc192Uplink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 133)
)
_JnxPicXDpc10X1GE_ObjectIdentity = ObjectIdentity
jnxPicXDpc10X1GE = _JnxPicXDpc10X1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 134)
)
_JnxPicXQDpc10X1GE_ObjectIdentity = ObjectIdentity
jnxPicXQDpc10X1GE = _JnxPicXQDpc10X1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 135)
)
_JnxPicXDpc1X10GE_ObjectIdentity = ObjectIdentity
jnxPicXDpc1X10GE = _JnxPicXDpc1X10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 136)
)
_JnxPicXQDpc1X10GE_ObjectIdentity = ObjectIdentity
jnxPicXQDpc1X10GE = _JnxPicXQDpc1X10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 137)
)
_JnxPicType3SonetOc192Xfp_ObjectIdentity = ObjectIdentity
jnxPicType3SonetOc192Xfp = _JnxPicType3SonetOc192Xfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 138)
)
_JnxPicType3IQ28X1GE_ObjectIdentity = ObjectIdentity
jnxPicType3IQ28X1GE = _JnxPicType3IQ28X1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 139)
)
_JnxPicType2Sonetoc48Sr2_ObjectIdentity = ObjectIdentity
jnxPicType2Sonetoc48Sr2 = _JnxPicType2Sonetoc48Sr2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 140)
)
_JnxPicType2Sonetoc12Sr2_ObjectIdentity = ObjectIdentity
jnxPicType2Sonetoc12Sr2 = _JnxPicType2Sonetoc12Sr2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 141)
)
_JnxPicType2Sonetoc3Sr2_ObjectIdentity = ObjectIdentity
jnxPicType2Sonetoc3Sr2 = _JnxPicType2Sonetoc3Sr2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 142)
)
_JnxPicStoli4X10GE_ObjectIdentity = ObjectIdentity
jnxPicStoli4X10GE = _JnxPicStoli4X10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 143)
)
_JnxPicType1Sonet4Xoc3_ObjectIdentity = ObjectIdentity
jnxPicType1Sonet4Xoc3 = _JnxPicType1Sonet4Xoc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 144)
)
_JnxPicType1Sonet2Xoc3_ObjectIdentity = ObjectIdentity
jnxPicType1Sonet2Xoc3 = _JnxPicType1Sonet2Xoc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 145)
)
_JnxPicType1Sonet1Xoc12_ObjectIdentity = ObjectIdentity
jnxPicType1Sonet1Xoc12 = _JnxPicType1Sonet1Xoc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 146)
)
_JnxPicGgsnStargateType2_ObjectIdentity = ObjectIdentity
jnxPicGgsnStargateType2 = _JnxPicGgsnStargateType2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 147)
)
_JnxPicUQDpc10X1GE_ObjectIdentity = ObjectIdentity
jnxPicUQDpc10X1GE = _JnxPicUQDpc10X1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 148)
)
_JnxPicUQDpc1X10GE_ObjectIdentity = ObjectIdentity
jnxPicUQDpc1X10GE = _JnxPicUQDpc1X10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 149)
)
_JnxPicNPC_ObjectIdentity = ObjectIdentity
jnxPicNPC = _JnxPicNPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 150)
)
_JnxPicIOC16xGETP_ObjectIdentity = ObjectIdentity
jnxPicIOC16xGETP = _JnxPicIOC16xGETP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 151)
)
_JnxPicIOC16xGESFP_ObjectIdentity = ObjectIdentity
jnxPicIOC16xGESFP = _JnxPicIOC16xGESFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 152)
)
_JnxPicIOC2x10GEXFP_ObjectIdentity = ObjectIdentity
jnxPicIOC2x10GEXFP = _JnxPicIOC2x10GEXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 153)
)
_JnxPicIOC8xGETP4xGESFP_ObjectIdentity = ObjectIdentity
jnxPicIOC8xGETP4xGESFP = _JnxPicIOC8xGETP4xGESFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 154)
)
_JnxPicSPCRMIx1_ObjectIdentity = ObjectIdentity
jnxPicSPCRMIx1 = _JnxPicSPCRMIx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 155)
)
_JnxPicType3EnhancedLoad_ObjectIdentity = ObjectIdentity
jnxPicType3EnhancedLoad = _JnxPicType3EnhancedLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 156)
)
_JnxPicCE4xCHOC3SFP_ObjectIdentity = ObjectIdentity
jnxPicCE4xCHOC3SFP = _JnxPicCE4xCHOC3SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 157)
)
_JnxPicCE12xT1E1_ObjectIdentity = ObjectIdentity
jnxPicCE12xT1E1 = _JnxPicCE12xT1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 158)
)
_JnxPicXDpc10X1GERJ45_ObjectIdentity = ObjectIdentity
jnxPicXDpc10X1GERJ45 = _JnxPicXDpc10X1GERJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 159)
)
_JnxPicQ2ChOc12_ObjectIdentity = ObjectIdentity
jnxPicQ2ChOc12 = _JnxPicQ2ChOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 160)
)
_JnxPicQ2Oc12_ObjectIdentity = ObjectIdentity
jnxPicQ2Oc12 = _JnxPicQ2Oc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 161)
)
_JnxPicQ2ChOc3_ObjectIdentity = ObjectIdentity
jnxPicQ2ChOc3 = _JnxPicQ2ChOc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 162)
)
_JnxPicQ2Oc3_ObjectIdentity = ObjectIdentity
jnxPicQ2Oc3 = _JnxPicQ2Oc3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 163)
)
_JnxPicQ2ChDs3_ObjectIdentity = ObjectIdentity
jnxPicQ2ChDs3 = _JnxPicQ2ChDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 164)
)
_JnxPicQ2Ds3_ObjectIdentity = ObjectIdentity
jnxPicQ2Ds3 = _JnxPicQ2Ds3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 165)
)
_JnxPicQ21xChOc48_ObjectIdentity = ObjectIdentity
jnxPicQ21xChOc48 = _JnxPicQ21xChOc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 166)
)
_JnxPicQ24xChOc12_ObjectIdentity = ObjectIdentity
jnxPicQ24xChOc12 = _JnxPicQ24xChOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 167)
)
_JnxPicQ210xChE1T1_ObjectIdentity = ObjectIdentity
jnxPicQ210xChE1T1 = _JnxPicQ210xChE1T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 168)
)
_JnxPicOlivet_ObjectIdentity = ObjectIdentity
jnxPicOlivet = _JnxPicOlivet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 169)
)
_JnxPicType1IQ2E4X1GE_ObjectIdentity = ObjectIdentity
jnxPicType1IQ2E4X1GE = _JnxPicType1IQ2E4X1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 170)
)
_JnxPicType2IQ2E8X1GE_ObjectIdentity = ObjectIdentity
jnxPicType2IQ2E8X1GE = _JnxPicType2IQ2E8X1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 171)
)
_JnxPicType3IQ2E8X1GE_ObjectIdentity = ObjectIdentity
jnxPicType3IQ2E8X1GE = _JnxPicType3IQ2E8X1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 172)
)
_JnxPicType3IQ2E1X10GE_ObjectIdentity = ObjectIdentity
jnxPicType3IQ2E1X10GE = _JnxPicType3IQ2E1X10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 173)
)
_JnxPicASPCTYPE1_ObjectIdentity = ObjectIdentity
jnxPicASPCTYPE1 = _JnxPicASPCTYPE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 174)
)
_JnxPicASPCTYPE2_ObjectIdentity = ObjectIdentity
jnxPicASPCTYPE2 = _JnxPicASPCTYPE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 175)
)
_JnxPicASPCTYPE3_ObjectIdentity = ObjectIdentity
jnxPicASPCTYPE3 = _JnxPicASPCTYPE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 176)
)
_JnxPicFIOC16X1GETP_ObjectIdentity = ObjectIdentity
jnxPicFIOC16X1GETP = _JnxPicFIOC16X1GETP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 177)
)
_JnxPicFIOC16X1GESFP_ObjectIdentity = ObjectIdentity
jnxPicFIOC16X1GESFP = _JnxPicFIOC16X1GESFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 178)
)
_JnxPicFIOC4X10GEXFP_ObjectIdentity = ObjectIdentity
jnxPicFIOC4X10GEXFP = _JnxPicFIOC4X10GEXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 179)
)
_JnxPicMIC20XGESFP_ObjectIdentity = ObjectIdentity
jnxPicMIC20XGESFP = _JnxPicMIC20XGESFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 180)
)
_JnxPicMIC2X10GEXFP_ObjectIdentity = ObjectIdentity
jnxPicMIC2X10GEXFP = _JnxPicMIC2X10GEXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 181)
)
_JnxPicMIC40XGERJ45_ObjectIdentity = ObjectIdentity
jnxPicMIC40XGERJ45 = _JnxPicMIC40XGERJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 182)
)
_JnxPicMIC4X10GEXFP_ObjectIdentity = ObjectIdentity
jnxPicMIC4X10GEXFP = _JnxPicMIC4X10GEXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 183)
)
_JnxPicMICLoad_ObjectIdentity = ObjectIdentity
jnxPicMICLoad = _JnxPicMICLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 184)
)
_JnxPicMICH10XGESFP_ObjectIdentity = ObjectIdentity
jnxPicMICH10XGESFP = _JnxPicMICH10XGESFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 185)
)
_JnxPicMICH1X10GEXFP_ObjectIdentity = ObjectIdentity
jnxPicMICH1X10GEXFP = _JnxPicMICH1X10GEXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 186)
)
_JnxPicMICH10XGERJ45_ObjectIdentity = ObjectIdentity
jnxPicMICH10XGERJ45 = _JnxPicMICH10XGERJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 187)
)
_JnxPicMICH2X10GEXFP_ObjectIdentity = ObjectIdentity
jnxPicMICH2X10GEXFP = _JnxPicMICH2X10GEXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 188)
)
_JnxPicMICHLoad_ObjectIdentity = ObjectIdentity
jnxPicMICHLoad = _JnxPicMICHLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 189)
)
_JnxPicOtn1X10GE_ObjectIdentity = ObjectIdentity
jnxPicOtn1X10GE = _JnxPicOtn1X10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 190)
)
_JnxPicStoli10X10GE_ObjectIdentity = ObjectIdentity
jnxPicStoli10X10GE = _JnxPicStoli10X10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 191)
)
_JnxPicStoli100GE_ObjectIdentity = ObjectIdentity
jnxPicStoli100GE = _JnxPicStoli100GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 192)
)
_JnxPicType3Q24xChOc12_ObjectIdentity = ObjectIdentity
jnxPicType3Q24xChOc12 = _JnxPicType3Q24xChOc12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 193)
)
_JnxPicStoli100GESlot1_ObjectIdentity = ObjectIdentity
jnxPicStoli100GESlot1 = _JnxPicStoli100GESlot1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 194)
)
_JnxPicUplinkSFPplus1G4_ObjectIdentity = ObjectIdentity
jnxPicUplinkSFPplus1G4 = _JnxPicUplinkSFPplus1G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 195)
)
_JnxPicUplinkSFPplus10G2_ObjectIdentity = ObjectIdentity
jnxPicUplinkSFPplus10G2 = _JnxPicUplinkSFPplus10G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 196)
)
_JnxPicUplinkXFP2port_ObjectIdentity = ObjectIdentity
jnxPicUplinkXFP2port = _JnxPicUplinkXFP2port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 197)
)
_JnxPicUplinkSFP4port_ObjectIdentity = ObjectIdentity
jnxPicUplinkSFP4port = _JnxPicUplinkSFP4port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 198)
)
_JnxPicUplinkSFPplus4port_ObjectIdentity = ObjectIdentity
jnxPicUplinkSFPplus4port = _JnxPicUplinkSFPplus4port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 199)
)
_JnxPicXDpcCombo10X1GE_ObjectIdentity = ObjectIdentity
jnxPicXDpcCombo10X1GE = _JnxPicXDpcCombo10X1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 200)
)
_JnxPicXQDpcCombo10X1GE_ObjectIdentity = ObjectIdentity
jnxPicXQDpcCombo10X1GE = _JnxPicXQDpcCombo10X1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 201)
)
_JnxPicTAZ4X10GEXFP_ObjectIdentity = ObjectIdentity
jnxPicTAZ4X10GEXFP = _JnxPicTAZ4X10GEXFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 202)
)
_JnxPicTAZ48XGERJ45_ObjectIdentity = ObjectIdentity
jnxPicTAZ48XGERJ45 = _JnxPicTAZ48XGERJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 203)
)
_JnxPicStoli1X40GECFP_ObjectIdentity = ObjectIdentity
jnxPicStoli1X40GECFP = _JnxPicStoli1X40GECFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 204)
)
_JnxPicOtnOc192_ObjectIdentity = ObjectIdentity
jnxPicOtnOc192 = _JnxPicOtnOc192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 205)
)
_JnxPICStoli100GESNAP12_ObjectIdentity = ObjectIdentity
jnxPICStoli100GESNAP12 = _JnxPICStoli100GESNAP12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 206)
)
_JnxPicEX820048S_ObjectIdentity = ObjectIdentity
jnxPicEX820048S = _JnxPicEX820048S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 207)
)
_JnxPicEX820048T_ObjectIdentity = ObjectIdentity
jnxPicEX820048T = _JnxPicEX820048T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 208)
)
_JnxPicEX82008XS_ObjectIdentity = ObjectIdentity
jnxPicEX82008XS = _JnxPicEX82008XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 209)
)
_JnxPicMIC4X10GESFPPLUS_ObjectIdentity = ObjectIdentity
jnxPicMIC4X10GESFPPLUS = _JnxPicMIC4X10GESFPPLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 210)
)
_JnxPicEX4500UplinkSFPPlus4Port_ObjectIdentity = ObjectIdentity
jnxPicEX4500UplinkSFPPlus4Port = _JnxPicEX4500UplinkSFPPlus4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 211)
)
_JnxPicSoho48X10GE_ObjectIdentity = ObjectIdentity
jnxPicSoho48X10GE = _JnxPicSoho48X10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 212)
)
_JnxPicM2LoopBack_ObjectIdentity = ObjectIdentity
jnxPicM2LoopBack = _JnxPicM2LoopBack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 213)
)
_JnxPicCtpGluon4xT1E1_ObjectIdentity = ObjectIdentity
jnxPicCtpGluon4xT1E1 = _JnxPicCtpGluon4xT1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 214)
)
_JnxPicCtpGluon4xSerial_ObjectIdentity = ObjectIdentity
jnxPicCtpGluon4xSerial = _JnxPicCtpGluon4xSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 215)
)
_JnxPicSng24x10GE_ObjectIdentity = ObjectIdentity
jnxPicSng24x10GE = _JnxPicSng24x10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 216)
)
_JnxPicSng2x100GE_ObjectIdentity = ObjectIdentity
jnxPicSng2x100GE = _JnxPicSng2x100GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 217)
)
_JnxPicSngLoad_ObjectIdentity = ObjectIdentity
jnxPicSngLoad = _JnxPicSngLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 218)
)
_JnxPicSysio6XGERJ456XGESFP_ObjectIdentity = ObjectIdentity
jnxPicSysio6XGERJ456XGESFP = _JnxPicSysio6XGERJ456XGESFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 219)
)
_JnxPicSysio6XGERJ453XGESFP3X10GESFPPlus_ObjectIdentity = ObjectIdentity
jnxPicSysio6XGERJ453XGESFP3X10GESFPPlus = _JnxPicSysio6XGERJ453XGESFP3X10GESFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 220)
)
_JnxPicDualWideSPCNPC_ObjectIdentity = ObjectIdentity
jnxPicDualWideSPCNPC = _JnxPicDualWideSPCNPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 221)
)
_JnxPicDualWideNPCSPC_ObjectIdentity = ObjectIdentity
jnxPicDualWideNPCSPC = _JnxPicDualWideNPCSPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 222)
)
_JnxPicTAZ12XGERJ45_ObjectIdentity = ObjectIdentity
jnxPicTAZ12XGERJ45 = _JnxPicTAZ12XGERJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 223)
)
_JnxPicType1MultiServicesFIPS_ObjectIdentity = ObjectIdentity
jnxPicType1MultiServicesFIPS = _JnxPicType1MultiServicesFIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 224)
)
_JnxPicType2MultiServicesFIPS_ObjectIdentity = ObjectIdentity
jnxPicType2MultiServicesFIPS = _JnxPicType2MultiServicesFIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 225)
)
_JnxPicType3MultiServicesFIPS_ObjectIdentity = ObjectIdentity
jnxPicType3MultiServicesFIPS = _JnxPicType3MultiServicesFIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 226)
)
_JnxPicEX4500UplinkXFP4Port_ObjectIdentity = ObjectIdentity
jnxPicEX4500UplinkXFP4Port = _JnxPicEX4500UplinkXFP4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 227)
)
_JnxPicEX4500M2Optical_ObjectIdentity = ObjectIdentity
jnxPicEX4500M2Optical = _JnxPicEX4500M2Optical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 228)
)
_JnxPicEX4500M2Legacy_ObjectIdentity = ObjectIdentity
jnxPicEX4500M2Legacy = _JnxPicEX4500M2Legacy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 229)
)
_JnxPicEX820036XS_ObjectIdentity = ObjectIdentity
jnxPicEX820036XS = _JnxPicEX820036XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 230)
)
_JnxPicEX820040XS_ObjectIdentity = ObjectIdentity
jnxPicEX820040XS = _JnxPicEX820040XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 231)
)
_JnxPicEX820048PL_ObjectIdentity = ObjectIdentity
jnxPicEX820048PL = _JnxPicEX820048PL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 232)
)
_JnxPicEX82002XS40P_ObjectIdentity = ObjectIdentity
jnxPicEX82002XS40P = _JnxPicEX82002XS40P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 233)
)
_JnxPicType1ASPCXLP_ObjectIdentity = ObjectIdentity
jnxPicType1ASPCXLP = _JnxPicType1ASPCXLP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 234)
)
_JnxPicType2ASPCXLP_ObjectIdentity = ObjectIdentity
jnxPicType2ASPCXLP = _JnxPicType2ASPCXLP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 235)
)
_JnxPicType3ASPCXLP_ObjectIdentity = ObjectIdentity
jnxPicType3ASPCXLP = _JnxPicType3ASPCXLP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 236)
)
_JnxPicSPCXLPx1_ObjectIdentity = ObjectIdentity
jnxPicSPCXLPx1 = _JnxPicSPCXLPx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 237)
)
_JnxPicStoli40GE_ObjectIdentity = ObjectIdentity
jnxPicStoli40GE = _JnxPicStoli40GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 238)
)
_JnxPicHyp1X100GECFP_ObjectIdentity = ObjectIdentity
jnxPicHyp1X100GECFP = _JnxPicHyp1X100GECFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 239)
)
_JnxPicHyp1X40GECFP_ObjectIdentity = ObjectIdentity
jnxPicHyp1X40GECFP = _JnxPicHyp1X40GECFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 240)
)
_JnxPicHypX100GECXP_ObjectIdentity = ObjectIdentity
jnxPicHypX100GECXP = _JnxPicHypX100GECXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 241)
)
_JnxPicHyp10X10GESFPP_ObjectIdentity = ObjectIdentity
jnxPicHyp10X10GESFPP = _JnxPicHyp10X10GESFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 242)
)
_JnxPic12x10GE_ObjectIdentity = ObjectIdentity
jnxPic12x10GE = _JnxPic12x10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 243)
)
_JnxPic1x100GE_ObjectIdentity = ObjectIdentity
jnxPic1x100GE = _JnxPic1x100GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 244)
)
_JnxPicHyp2X40GEQSFP_ObjectIdentity = ObjectIdentity
jnxPicHyp2X40GEQSFP = _JnxPicHyp2X40GEQSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 245)
)
_JnxPicHercules24X10GE_ObjectIdentity = ObjectIdentity
jnxPicHercules24X10GE = _JnxPicHercules24X10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 246)
)
_JnxPicCTPGluonSerialMS_ObjectIdentity = ObjectIdentity
jnxPicCTPGluonSerialMS = _JnxPicCTPGluonSerialMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 247)
)
_JnxPicAgent00SLC1X10GE_ObjectIdentity = ObjectIdentity
jnxPicAgent00SLC1X10GE = _JnxPicAgent00SLC1X10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 248)
)
_JnxPicAgent00SLC4X1GE_ObjectIdentity = ObjectIdentity
jnxPicAgent00SLC4X1GE = _JnxPicAgent00SLC4X1GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 249)
)
_JnxPicQFXSFE16x40GEQSFP_ObjectIdentity = ObjectIdentity
jnxPicQFXSFE16x40GEQSFP = _JnxPicQFXSFE16x40GEQSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 250)
)
_JnxPicQFXSFI16x40GE_ObjectIdentity = ObjectIdentity
jnxPicQFXSFI16x40GE = _JnxPicQFXSFI16x40GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 251)
)
_JnxPicQFXSRI16x40GE_ObjectIdentity = ObjectIdentity
jnxPicQFXSRI16x40GE = _JnxPicQFXSRI16x40GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 252)
)
_JnxPicQFX48x10GESFPPlus_ObjectIdentity = ObjectIdentity
jnxPicQFX48x10GESFPPlus = _JnxPicQFX48x10GESFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 253)
)
_JnxPicQFX4x40GEQSFP_ObjectIdentity = ObjectIdentity
jnxPicQFX4x40GEQSFP = _JnxPicQFX4x40GEQSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 254)
)
_JnxPicQFX2x80GEQCXP_ObjectIdentity = ObjectIdentity
jnxPicQFX2x80GEQCXP = _JnxPicQFX2x80GEQCXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 255)
)
_JnxPicType3IQECC4XOC48_ObjectIdentity = ObjectIdentity
jnxPicType3IQECC4XOC48 = _JnxPicType3IQECC4XOC48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 256)
)
_JnxPicSng2x40GE_ObjectIdentity = ObjectIdentity
jnxPicSng2x40GE = _JnxPicSng2x40GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 257)
)
_JnxPicIBM0719J45EUplinkSFPPlus4Port_ObjectIdentity = ObjectIdentity
jnxPicIBM0719J45EUplinkSFPPlus4Port = _JnxPicIBM0719J45EUplinkSFPPlus4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 258)
)
_JnxPicIBM0719J45EUplinkXFP4Port_ObjectIdentity = ObjectIdentity
jnxPicIBM0719J45EUplinkXFP4Port = _JnxPicIBM0719J45EUplinkXFP4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 259)
)
_JnxPicIBM0719J45EM2Optical_ObjectIdentity = ObjectIdentity
jnxPicIBM0719J45EM2Optical = _JnxPicIBM0719J45EM2Optical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 260)
)
_JnxPicIBM0719J45EM2Legacy_ObjectIdentity = ObjectIdentity
jnxPicIBM0719J45EM2Legacy = _JnxPicIBM0719J45EM2Legacy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 261)
)
_JnxPicIBMJ08FSFE16x40GEQSFP_ObjectIdentity = ObjectIdentity
jnxPicIBMJ08FSFE16x40GEQSFP = _JnxPicIBMJ08FSFE16x40GEQSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 262)
)
_JnxPicIBMJ08FSFI16xFabric_ObjectIdentity = ObjectIdentity
jnxPicIBMJ08FSFI16xFabric = _JnxPicIBMJ08FSFI16xFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 263)
)
_JnxPicIBMJ08FSRI16xFabric_ObjectIdentity = ObjectIdentity
jnxPicIBMJ08FSRI16xFabric = _JnxPicIBMJ08FSRI16xFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 264)
)
_JnxPicIBMJ52F48x10GESFPPlus_ObjectIdentity = ObjectIdentity
jnxPicIBMJ52F48x10GESFPPlus = _JnxPicIBMJ52F48x10GESFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 265)
)
_JnxPicIBMJ52F4x40GEQSFP_ObjectIdentity = ObjectIdentity
jnxPicIBMJ52F4x40GEQSFP = _JnxPicIBMJ52F4x40GEQSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 266)
)
_JnxPicDellJFX350048x10GESFPPlus_ObjectIdentity = ObjectIdentity
jnxPicDellJFX350048x10GESFPPlus = _JnxPicDellJFX350048x10GESFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 267)
)
_JnxPicEX820048TES_ObjectIdentity = ObjectIdentity
jnxPicEX820048TES = _JnxPicEX820048TES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 268)
)
_JnxPicEX820048SES_ObjectIdentity = ObjectIdentity
jnxPicEX820048SES = _JnxPicEX820048SES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 269)
)
_JnxPicEX82008XSES_ObjectIdentity = ObjectIdentity
jnxPicEX82008XSES = _JnxPicEX82008XSES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 270)
)
_JnxPicEX820040XSES_ObjectIdentity = ObjectIdentity
jnxPicEX820040XSES = _JnxPicEX820040XSES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 271)
)
_JnxPicEX820048TES4X_ObjectIdentity = ObjectIdentity
jnxPicEX820048TES4X = _JnxPicEX820048TES4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 272)
)
_JnxPicEX820048SES4X_ObjectIdentity = ObjectIdentity
jnxPicEX820048SES4X = _JnxPicEX820048SES4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 273)
)
_JnxPicEX82008XSES4X_ObjectIdentity = ObjectIdentity
jnxPicEX82008XSES4X = _JnxPicEX82008XSES4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 274)
)
_JnxPicEX820040XSES4X_ObjectIdentity = ObjectIdentity
jnxPicEX820040XSES4X = _JnxPicEX820040XSES4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 275)
)
_JnxPicEX620048T_ObjectIdentity = ObjectIdentity
jnxPicEX620048T = _JnxPicEX620048T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 276)
)
_JnxPicEX620048P_ObjectIdentity = ObjectIdentity
jnxPicEX620048P = _JnxPicEX620048P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 277)
)
_JnxPicEX62004XS_ObjectIdentity = ObjectIdentity
jnxPicEX62004XS = _JnxPicEX62004XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 278)
)
_JnxPicDellJFX35004x40GEQSFP_ObjectIdentity = ObjectIdentity
jnxPicDellJFX35004x40GEQSFP = _JnxPicDellJFX35004x40GEQSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 279)
)
_JnxPicEX820048TL_ObjectIdentity = ObjectIdentity
jnxPicEX820048TL = _JnxPicEX820048TL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 280)
)
_JnxPicEX82002XS40T_ObjectIdentity = ObjectIdentity
jnxPicEX82002XS40T = _JnxPicEX82002XS40T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 281)
)
_JnxPicType2MSPrism_ObjectIdentity = ObjectIdentity
jnxPicType2MSPrism = _JnxPicType2MSPrism_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 282)
)
_JnxPicMicMSPrism_ObjectIdentity = ObjectIdentity
jnxPicMicMSPrism = _JnxPicMicMSPrism_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 283)
)
_JnxPicQFX16x10GESFPPlus_ObjectIdentity = ObjectIdentity
jnxPicQFX16x10GESFPPlus = _JnxPicQFX16x10GESFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 284)
)
_JnxPicIBMJ52F16x10GESFPPlus_ObjectIdentity = ObjectIdentity
jnxPicIBMJ52F16x10GESFPPlus = _JnxPicIBMJ52F16x10GESFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 285)
)
_JnxPicDellJFX350016x10GESFPPlus_ObjectIdentity = ObjectIdentity
jnxPicDellJFX350016x10GESFPPlus = _JnxPicDellJFX350016x10GESFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 286)
)
_JnxPicQFX10xPTunnel_ObjectIdentity = ObjectIdentity
jnxPicQFX10xPTunnel = _JnxPicQFX10xPTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 287)
)
_JnxPicIBMJ52F10xPTunnel_ObjectIdentity = ObjectIdentity
jnxPicIBMJ52F10xPTunnel = _JnxPicIBMJ52F10xPTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 288)
)
_JnxPic16XT1E1CEMIC_ObjectIdentity = ObjectIdentity
jnxPic16XT1E1CEMIC = _JnxPic16XT1E1CEMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 289)
)
_JnxPic8XT1E1CEMIC_ObjectIdentity = ObjectIdentity
jnxPic8XT1E1CEMIC = _JnxPic8XT1E1CEMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 290)
)
_JnxPic8xGERJ452xPOEMIC_ObjectIdentity = ObjectIdentity
jnxPic8xGERJ452xPOEMIC = _JnxPic8xGERJ452xPOEMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 291)
)
_JnxPic2xGESFPMIC_ObjectIdentity = ObjectIdentity
jnxPic2xGESFPMIC = _JnxPic2xGESFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 292)
)
_JnxPic2x10GESFPPLUSMIC_ObjectIdentity = ObjectIdentity
jnxPic2x10GESFPPLUSMIC = _JnxPic2x10GESFPPLUSMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 293)
)
_JnxPic4xGESFPRJ45COMBOMIC_ObjectIdentity = ObjectIdentity
jnxPic4xGESFPRJ45COMBOMIC = _JnxPic4xGESFPRJ45COMBOMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 294)
)
_JnxPicUplinkDualMedia2port_ObjectIdentity = ObjectIdentity
jnxPicUplinkDualMedia2port = _JnxPicUplinkDualMedia2port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 295)
)
_JnxPicEX3300UplinkSFPPlus4Port_ObjectIdentity = ObjectIdentity
jnxPicEX3300UplinkSFPPlus4Port = _JnxPicEX3300UplinkSFPPlus4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 296)
)
_JnxPicEX4500UplinkSFP4Port_ObjectIdentity = ObjectIdentity
jnxPicEX4500UplinkSFP4Port = _JnxPicEX4500UplinkSFP4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 297)
)
_JnxPicEX4550UplinkEm8XFP_ObjectIdentity = ObjectIdentity
jnxPicEX4550UplinkEm8XFP = _JnxPicEX4550UplinkEm8XFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 298)
)
_JnxPicEX4550UplinkEm8XT_ObjectIdentity = ObjectIdentity
jnxPicEX4550UplinkEm8XT = _JnxPicEX4550UplinkEm8XT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 299)
)
_JnxPicEX4550UplinkEm2QSFP_ObjectIdentity = ObjectIdentity
jnxPicEX4550UplinkEm2QSFP = _JnxPicEX4550UplinkEm2QSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 300)
)
_JnxPicEX4550VC128G_ObjectIdentity = ObjectIdentity
jnxPicEX4550VC128G = _JnxPicEX4550VC128G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 301)
)
_JnxPicQFX16x80GCXP_ObjectIdentity = ObjectIdentity
jnxPicQFX16x80GCXP = _JnxPicQFX16x80GCXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 302)
)
_JnxPicQFX63x10GESFPPlus_ObjectIdentity = ObjectIdentity
jnxPicQFX63x10GESFPPlus = _JnxPicQFX63x10GESFPPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 303)
)
_JnxPicQFX16x40GEQSFP_ObjectIdentity = ObjectIdentity
jnxPicQFX16x40GEQSFP = _JnxPicQFX16x40GEQSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 304)
)
_JnxPic6xGESFPRJ45_ObjectIdentity = ObjectIdentity
jnxPic6xGESFPRJ45 = _JnxPic6xGESFPRJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 305)
)
_JnxPicMXPISA16xT1E1RJ48_ObjectIdentity = ObjectIdentity
jnxPicMXPISA16xT1E1RJ48 = _JnxPicMXPISA16xT1E1RJ48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 306)
)
_JnxPic6x40GEQSFPP_ObjectIdentity = ObjectIdentity
jnxPic6x40GEQSFPP = _JnxPic6x40GEQSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 307)
)
_JnxPicACX1xOC124xOC3SFP_ObjectIdentity = ObjectIdentity
jnxPicACX1xOC124xOC3SFP = _JnxPicACX1xOC124xOC3SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 308)
)
_JnxPicACXPISA16xT1E1RJ48_ObjectIdentity = ObjectIdentity
jnxPicACXPISA16xT1E1RJ48 = _JnxPicACXPISA16xT1E1RJ48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 309)
)
_JnxPic8x10GESFPPMIC_ObjectIdentity = ObjectIdentity
jnxPic8x10GESFPPMIC = _JnxPic8x10GESFPPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 310)
)
_JnxPic1x100GECFPMIC_ObjectIdentity = ObjectIdentity
jnxPic1x100GECFPMIC = _JnxPic1x100GECFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 311)
)
_JnxPic4x10GESFPPMIC_ObjectIdentity = ObjectIdentity
jnxPic4x10GESFPPMIC = _JnxPic4x10GESFPPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 312)
)
_JnxPicPTX2x100GOTNPIC_ObjectIdentity = ObjectIdentity
jnxPicPTX2x100GOTNPIC = _JnxPicPTX2x100GOTNPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 313)
)
_JnxPicMXXLPDPCPIC_ObjectIdentity = ObjectIdentity
jnxPicMXXLPDPCPIC = _JnxPicMXXLPDPCPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 314)
)
_JnxPicMXXLP8GMIC_ObjectIdentity = ObjectIdentity
jnxPicMXXLP8GMIC = _JnxPicMXXLP8GMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 315)
)
_JnxPicMXXLP16GMIC_ObjectIdentity = ObjectIdentity
jnxPicMXXLP16GMIC = _JnxPicMXXLP16GMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 316)
)
_JnxPicMXXLP8GFIPSMIC_ObjectIdentity = ObjectIdentity
jnxPicMXXLP8GFIPSMIC = _JnxPicMXXLP8GFIPSMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 317)
)
_JnxPicMXXLP16GFIPSMIC_ObjectIdentity = ObjectIdentity
jnxPicMXXLP16GFIPSMIC = _JnxPicMXXLP16GFIPSMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 318)
)
_JnxPicEX4300QSFP4Port_ObjectIdentity = ObjectIdentity
jnxPicEX4300QSFP4Port = _JnxPicEX4300QSFP4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 319)
)
_JnxPicEX4300UplinkSFPPlus4Port_ObjectIdentity = ObjectIdentity
jnxPicEX4300UplinkSFPPlus4Port = _JnxPicEX4300UplinkSFPPlus4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 320)
)
_JnxPicNPIOC2x10GESFPPLUSPIC_ObjectIdentity = ObjectIdentity
jnxPicNPIOC2x10GESFPPLUSPIC = _JnxPicNPIOC2x10GESFPPLUSPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 321)
)
_JnxPic4CHDS3E3MICSR_ObjectIdentity = ObjectIdentity
jnxPic4CHDS3E3MICSR = _JnxPic4CHDS3E3MICSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 322)
)
_JnxPic4CHOC31CHOC12MICSR_ObjectIdentity = ObjectIdentity
jnxPic4CHOC31CHOC12MICSR = _JnxPic4CHOC31CHOC12MICSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 323)
)
_JnxPicSNG24x10GELWOPIC_ObjectIdentity = ObjectIdentity
jnxPicSNG24x10GELWOPIC = _JnxPicSNG24x10GELWOPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 324)
)
_JnxPic8xGESFPRJ45COMBOMIC_ObjectIdentity = ObjectIdentity
jnxPic8xGESFPRJ45COMBOMIC = _JnxPic8xGESFPRJ45COMBOMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 325)
)
_JnxPic4X10GESFPPLUSMIC_ObjectIdentity = ObjectIdentity
jnxPic4X10GESFPPLUSMIC = _JnxPic4X10GESFPPLUSMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 326)
)
_JnxPic4xGERJ45MIC_ObjectIdentity = ObjectIdentity
jnxPic4xGERJ45MIC = _JnxPic4xGERJ45MIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 327)
)
_JnxPic24X10GESFPPMIC_ObjectIdentity = ObjectIdentity
jnxPic24X10GESFPPMIC = _JnxPic24X10GESFPPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 328)
)
_JnxPic24X10GESFPPOTNMIC_ObjectIdentity = ObjectIdentity
jnxPic24X10GESFPPOTNMIC = _JnxPic24X10GESFPPOTNMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 329)
)
_JnxPic2X100GECFP2MIC_ObjectIdentity = ObjectIdentity
jnxPic2X100GECFP2MIC = _JnxPic2X100GECFP2MIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 330)
)
_JnxPic12X10GESFPPPIC_ObjectIdentity = ObjectIdentity
jnxPic12X10GESFPPPIC = _JnxPic12X10GESFPPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 331)
)
_JnxPic12X10GESFPPOTNPIC_ObjectIdentity = ObjectIdentity
jnxPic12X10GESFPPOTNPIC = _JnxPic12X10GESFPPOTNPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 332)
)
_JnxPic2X100GECFP2PIC_ObjectIdentity = ObjectIdentity
jnxPic2X100GECFP2PIC = _JnxPic2X100GECFP2PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 333)
)
_JnxPicWdSf12X10GESFPPPIC_ObjectIdentity = ObjectIdentity
jnxPicWdSf12X10GESFPPPIC = _JnxPicWdSf12X10GESFPPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 334)
)
_JnxPicNX10GESFPPOTNDEBUGPIC_ObjectIdentity = ObjectIdentity
jnxPicNX10GESFPPOTNDEBUGPIC = _JnxPicNX10GESFPPOTNDEBUGPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 335)
)
_JnxPicWdSf12X10GESFPPOTNPIC_ObjectIdentity = ObjectIdentity
jnxPicWdSf12X10GESFPPOTNPIC = _JnxPicWdSf12X10GESFPPOTNPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 336)
)
_JnxPic3X40GEQSFPPPIC_ObjectIdentity = ObjectIdentity
jnxPic3X40GEQSFPPPIC = _JnxPic3X40GEQSFPPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 337)
)
_JnxPic1X100GECFP2PIC_ObjectIdentity = ObjectIdentity
jnxPic1X100GECFP2PIC = _JnxPic1X100GECFP2PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 338)
)
_JnxPicQFX48x10GESFP_ObjectIdentity = ObjectIdentity
jnxPicQFX48x10GESFP = _JnxPicQFX48x10GESFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 339)
)
_JnxPicKFIPCSFPPPIC_ObjectIdentity = ObjectIdentity
jnxPicKFIPCSFPPPIC = _JnxPicKFIPCSFPPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 341)
)
_JnxPicKFIPCCFP2PIC_ObjectIdentity = ObjectIdentity
jnxPicKFIPCCFP2PIC = _JnxPicKFIPCCFP2PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 342)
)
_JnxPicJAVAxUplinkSFFPlusMACSEC4PORT_ObjectIdentity = ObjectIdentity
jnxPicJAVAxUplinkSFFPlusMACSEC4PORT = _JnxPicJAVAxUplinkSFFPlusMACSEC4PORT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 343)
)
_JnxPicEX8200M48XSO_ObjectIdentity = ObjectIdentity
jnxPicEX8200M48XSO = _JnxPicEX8200M48XSO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 344)
)
_JnxPicEX8200M12LQO_ObjectIdentity = ObjectIdentity
jnxPicEX8200M12LQO = _JnxPicEX8200M12LQO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 345)
)
_JnxPicEX8200M2CF_ObjectIdentity = ObjectIdentity
jnxPicEX8200M2CF = _JnxPicEX8200M2CF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 346)
)
_JnxPicOpusQic4X40G_ObjectIdentity = ObjectIdentity
jnxPicOpusQic4X40G = _JnxPicOpusQic4X40G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 347)
)
_JnxPic20XGESfpEHMIC_ObjectIdentity = ObjectIdentity
jnxPic20XGESfpEHMIC = _JnxPic20XGESfpEHMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 348)
)
_JnxPic1XCOC124XCOC3CEHMIC_ObjectIdentity = ObjectIdentity
jnxPic1XCOC124XCOC3CEHMIC = _JnxPic1XCOC124XCOC3CEHMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 349)
)
_JnxPicPISA16XT1E1HMIC_ObjectIdentity = ObjectIdentity
jnxPicPISA16XT1E1HMIC = _JnxPicPISA16XT1E1HMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 350)
)
_JnxPic20XGESFPEMIC_ObjectIdentity = ObjectIdentity
jnxPic20XGESFPEMIC = _JnxPic20XGESFPEMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 351)
)
_JnxPicUplinkMacsecSFPplus1G4_ObjectIdentity = ObjectIdentity
jnxPicUplinkMacsecSFPplus1G4 = _JnxPicUplinkMacsecSFPplus1G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 352)
)
_JnxPicUplinkMacsecSFPplus10G2_ObjectIdentity = ObjectIdentity
jnxPicUplinkMacsecSFPplus10G2 = _JnxPicUplinkMacsecSFPplus10G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 353)
)
_JnxPicUplinkMacsecSFPplus4port_ObjectIdentity = ObjectIdentity
jnxPicUplinkMacsecSFPplus4port = _JnxPicUplinkMacsecSFPplus4port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 354)
)
_JnxPicVMX10X1GEPIC_ObjectIdentity = ObjectIdentity
jnxPicVMX10X1GEPIC = _JnxPicVMX10X1GEPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 355)
)
_JnxPic10XGESFPHALFEHMIC_ObjectIdentity = ObjectIdentity
jnxPic10XGESFPHALFEHMIC = _JnxPic10XGESFPHALFEHMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 356)
)
_JnxPic10XGESFPHALFEMIC_ObjectIdentity = ObjectIdentity
jnxPic10XGESFPHALFEMIC = _JnxPic10XGESFPHALFEMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 357)
)
_JnxPic1xOC124xOC3SFP_ObjectIdentity = ObjectIdentity
jnxPic1xOC124xOC3SFP = _JnxPic1xOC124xOC3SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 358)
)
_JnxPicEX920040x1GbERJ45_ObjectIdentity = ObjectIdentity
jnxPicEX920040x1GbERJ45 = _JnxPicEX920040x1GbERJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 359)
)
_JnxPicEX920020x1GbESFP_ObjectIdentity = ObjectIdentity
jnxPicEX920020x1GbESFP = _JnxPicEX920020x1GbESFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 360)
)
_JnxPicEX92002x40GbEQSFPP_ObjectIdentity = ObjectIdentity
jnxPicEX92002x40GbEQSFPP = _JnxPicEX92002x40GbEQSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 361)
)
_JnxPic4X100GECXPMIC_ObjectIdentity = ObjectIdentity
jnxPic4X100GECXPMIC = _JnxPic4X100GECXPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 362)
)
_JnxPicQFXEM4Q_ObjectIdentity = ObjectIdentity
jnxPicQFXEM4Q = _JnxPicQFXEM4Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 363)
)
_JnxPicQFXEM8S_ObjectIdentity = ObjectIdentity
jnxPicQFXEM8S = _JnxPicQFXEM8S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 364)
)
_JnxPicSRXIOC21X100GECFP_ObjectIdentity = ObjectIdentity
jnxPicSRXIOC21X100GECFP = _JnxPicSRXIOC21X100GECFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 365)
)
_JnxPicSRXIOC210X10GESFPP_ObjectIdentity = ObjectIdentity
jnxPicSRXIOC210X10GESFPP = _JnxPicSRXIOC210X10GESFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 366)
)
_JnxPicSRXIOC22X40GEQSFP_ObjectIdentity = ObjectIdentity
jnxPicSRXIOC22X40GEQSFP = _JnxPicSRXIOC22X40GEQSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 367)
)
_JnxPicCHV4X100GCFP2_ObjectIdentity = ObjectIdentity
jnxPicCHV4X100GCFP2 = _JnxPicCHV4X100GCFP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 368)
)
_JnxPicCHVLOAD_ObjectIdentity = ObjectIdentity
jnxPicCHVLOAD = _JnxPicCHVLOAD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 369)
)
_JnxPicEX4300UplinkSFPPlus8Port_ObjectIdentity = ObjectIdentity
jnxPicEX4300UplinkSFPPlus8Port = _JnxPicEX4300UplinkSFPPlus8Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 370)
)
_JnxPicEX4300UplinkQSFP2Port_ObjectIdentity = ObjectIdentity
jnxPicEX4300UplinkQSFP2Port = _JnxPicEX4300UplinkQSFP2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 371)
)
_JnxPicCHVfake4X100GCFP2_ObjectIdentity = ObjectIdentity
jnxPicCHVfake4X100GCFP2 = _JnxPicCHVfake4X100GCFP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 372)
)
_JnxPicQFX510024Q_ObjectIdentity = ObjectIdentity
jnxPicQFX510024Q = _JnxPicQFX510024Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 373)
)
_JnxPicWdSf2X10GESFPPOTNPIC_ObjectIdentity = ObjectIdentity
jnxPicWdSf2X10GESFPPOTNPIC = _JnxPicWdSf2X10GESFPPOTNPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 374)
)
_JnxPicEX920012X10GESFPPPIC_ObjectIdentity = ObjectIdentity
jnxPicEX920012X10GESFPPPIC = _JnxPicEX920012X10GESFPPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 375)
)
_JnxPicEX92003X40GEQSFPPPIC_ObjectIdentity = ObjectIdentity
jnxPicEX92003X40GEQSFPPPIC = _JnxPicEX92003X40GEQSFPPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 376)
)
_JnxPicEX920020X1GESFPMACSECMIC_ObjectIdentity = ObjectIdentity
jnxPicEX920020X1GESFPMACSECMIC = _JnxPicEX920020X1GESFPMACSECMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 377)
)
_JnxPicEX920020X1GESFPMACSECHALFMIC_ObjectIdentity = ObjectIdentity
jnxPicEX920020X1GESFPMACSECHALFMIC = _JnxPicEX920020X1GESFPMACSECHALFMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 378)
)
_JnxPicEX4300QSFP2Port_ObjectIdentity = ObjectIdentity
jnxPicEX4300QSFP2Port = _JnxPicEX4300QSFP2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 379)
)
_JnxPicCHV4X100GOTNCFP2_ObjectIdentity = ObjectIdentity
jnxPicCHV4X100GOTNCFP2 = _JnxPicCHV4X100GOTNCFP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 380)
)
_JnxPicCHV48X10G12X40GLWOPIC_ObjectIdentity = ObjectIdentity
jnxPicCHV48X10G12X40GLWOPIC = _JnxPicCHV48X10G12X40GLWOPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 381)
)
_JnxPicQFX24x40GEFQSFP_ObjectIdentity = ObjectIdentity
jnxPicQFX24x40GEFQSFP = _JnxPicQFX24x40GEFQSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 382)
)
_JnxPicQFX48x10GEFSFP_ObjectIdentity = ObjectIdentity
jnxPicQFX48x10GEFSFP = _JnxPicQFX48x10GEFSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 383)
)
_JnxPicQFX6x40GEFQSFP_ObjectIdentity = ObjectIdentity
jnxPicQFX6x40GEFQSFP = _JnxPicQFX6x40GEFQSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 384)
)
_JnxPicQFX96X10GEFSFP8X40GEFQSFP_ObjectIdentity = ObjectIdentity
jnxPicQFX96X10GEFSFP8X40GEFQSFP = _JnxPicQFX96X10GEFSFP8X40GEFQSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 385)
)
_JnxPicQFX48X10GECSFP6X40GEFQSFP_ObjectIdentity = ObjectIdentity
jnxPicQFX48X10GECSFP6X40GEFQSFP = _JnxPicQFX48X10GECSFP6X40GEFQSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 386)
)
_JnxPicQFX510048S6Q_ObjectIdentity = ObjectIdentity
jnxPicQFX510048S6Q = _JnxPicQFX510048S6Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 387)
)
_JnxPicQFX510024S4Q_ObjectIdentity = ObjectIdentity
jnxPicQFX510024S4Q = _JnxPicQFX510024S4Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 388)
)
_JnxPicQFX510096S8Q_ObjectIdentity = ObjectIdentity
jnxPicQFX510096S8Q = _JnxPicQFX510096S8Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 389)
)
_JnxPicQFX510048C6Q_ObjectIdentity = ObjectIdentity
jnxPicQFX510048C6Q = _JnxPicQFX510048C6Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 390)
)
_JnxPicEX460024S4Q_ObjectIdentity = ObjectIdentity
jnxPicEX460024S4Q = _JnxPicEX460024S4Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 391)
)
_JnxPicEX4600EM8F_ObjectIdentity = ObjectIdentity
jnxPicEX4600EM8F = _JnxPicEX4600EM8F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 392)
)
_JnxPic8X100GECFP4MIC_ObjectIdentity = ObjectIdentity
jnxPic8X100GECFP4MIC = _JnxPic8X100GECFP4MIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 393)
)
_JnxPic12X40GEQSFPPMIC_ObjectIdentity = ObjectIdentity
jnxPic12X40GEQSFPPMIC = _JnxPic12X40GEQSFPPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 394)
)
_JnxPicMPC8LOADMIC_ObjectIdentity = ObjectIdentity
jnxPicMPC8LOADMIC = _JnxPicMPC8LOADMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 395)
)
_JnxPic6XQSFPP_ObjectIdentity = ObjectIdentity
jnxPic6XQSFPP = _JnxPic6XQSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 396)
)
_JnxPic20X10GE_ObjectIdentity = ObjectIdentity
jnxPic20X10GE = _JnxPic20X10GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 397)
)
_JnxPicQFX510048C6QF_ObjectIdentity = ObjectIdentity
jnxPicQFX510048C6QF = _JnxPicQFX510048C6QF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 398)
)
_JnxPicQFX510048C6QFQSFP_ObjectIdentity = ObjectIdentity
jnxPicQFX510048C6QFQSFP = _JnxPicQFX510048C6QFQSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 399)
)
_JnxPicCHV12X40GLWOPIC_ObjectIdentity = ObjectIdentity
jnxPicCHV12X40GLWOPIC = _JnxPicCHV12X40GLWOPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 400)
)
_JnxPicSRXIOC220X1GESFP_ObjectIdentity = ObjectIdentity
jnxPicSRXIOC220X1GESFP = _JnxPicSRXIOC220X1GESFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 401)
)
_JnxPicSRXIOC210X1GESFP_ObjectIdentity = ObjectIdentity
jnxPicSRXIOC210X1GESFP = _JnxPicSRXIOC210X1GESFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 402)
)
_JnxPic3xGERJ453xPOEMIC_ObjectIdentity = ObjectIdentity
jnxPic3xGERJ453xPOEMIC = _JnxPic3xGERJ453xPOEMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 403)
)
_JnxPic3xGERJ45MIC_ObjectIdentity = ObjectIdentity
jnxPic3xGERJ45MIC = _JnxPic3xGERJ45MIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 404)
)
_JnxPic4xGESFPRJ453xPOEMIC_ObjectIdentity = ObjectIdentity
jnxPic4xGESFPRJ453xPOEMIC = _JnxPic4xGESFPRJ453xPOEMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 405)
)
_JnxPic3xGESFP_ObjectIdentity = ObjectIdentity
jnxPic3xGESFP = _JnxPic3xGESFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 406)
)
_JnxPicMultiserviceBuiltin_ObjectIdentity = ObjectIdentity
jnxPicMultiserviceBuiltin = _JnxPicMultiserviceBuiltin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 407)
)
_JnxPicCHV4X100GCXPPIC_ObjectIdentity = ObjectIdentity
jnxPicCHV4X100GCXPPIC = _JnxPicCHV4X100GCXPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 408)
)
_JnxPicPTXMLC24X10GESFPP_ObjectIdentity = ObjectIdentity
jnxPicPTXMLC24X10GESFPP = _JnxPicPTXMLC24X10GESFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 409)
)
_JnxPicCordoba1X100DwdmMIC_ObjectIdentity = ObjectIdentity
jnxPicCordoba1X100DwdmMIC = _JnxPicCordoba1X100DwdmMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 410)
)
_JnxPicPTXLoadMIC_ObjectIdentity = ObjectIdentity
jnxPicPTXLoadMIC = _JnxPicPTXLoadMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 411)
)
_JnxPicIOCIII12X10SFPP_ObjectIdentity = ObjectIdentity
jnxPicIOCIII12X10SFPP = _JnxPicIOCIII12X10SFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 412)
)
_JnxPicIOCIII4X40QSFPP_ObjectIdentity = ObjectIdentity
jnxPicIOCIII4X40QSFPP = _JnxPicIOCIII4X40QSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 413)
)
_JnxPicIOCIII1X100CFP2_ObjectIdentity = ObjectIdentity
jnxPicIOCIII1X100CFP2 = _JnxPicIOCIII1X100CFP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 414)
)
_JnxPicIOCIII2X10SFPP_ObjectIdentity = ObjectIdentity
jnxPicIOCIII2X10SFPP = _JnxPicIOCIII2X10SFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 415)
)
_JnxPicEX920010X10GESFPPMIC_ObjectIdentity = ObjectIdentity
jnxPicEX920010X10GESFPPMIC = _JnxPicEX920010X10GESFPPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 416)
)
_JnxPicEX920020X10GESFPPMIC_ObjectIdentity = ObjectIdentity
jnxPicEX920020X10GESFPPMIC = _JnxPicEX920020X10GESFPPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 417)
)
_JnxPicEX92006XQSFPPPIC_ObjectIdentity = ObjectIdentity
jnxPicEX92006XQSFPPPIC = _JnxPicEX92006XQSFPPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 418)
)
_JnxPicPTX15X100GEREV1PIC_ObjectIdentity = ObjectIdentity
jnxPicPTX15X100GEREV1PIC = _JnxPicPTX15X100GEREV1PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 419)
)
_JnxPicPTX10X100GEREV1PIC_ObjectIdentity = ObjectIdentity
jnxPicPTX10X100GEREV1PIC = _JnxPicPTX10X100GEREV1PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 420)
)
_JnxPicPTX2X100GMETROOTNPIC_ObjectIdentity = ObjectIdentity
jnxPicPTX2X100GMETROOTNPIC = _JnxPicPTX2X100GMETROOTNPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 421)
)
_JnxPicQFX510024QAA_ObjectIdentity = ObjectIdentity
jnxPicQFX510024QAA = _JnxPicQFX510024QAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 422)
)
_JnxPicQFXPFA4Q_ObjectIdentity = ObjectIdentity
jnxPicQFXPFA4Q = _JnxPicQFXPFA4Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 423)
)
_JnxPicACX5048_ObjectIdentity = ObjectIdentity
jnxPicACX5048 = _JnxPicACX5048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 424)
)
_JnxPicACX5096_ObjectIdentity = ObjectIdentity
jnxPicACX5096 = _JnxPicACX5096_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 425)
)
_JnxPicCordoba5X100DwdmPIC_ObjectIdentity = ObjectIdentity
jnxPicCordoba5X100DwdmPIC = _JnxPicCordoba5X100DwdmPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 426)
)
_JnxPicSHO10X100GEQSFPPIC_ObjectIdentity = ObjectIdentity
jnxPicSHO10X100GEQSFPPIC = _JnxPicSHO10X100GEQSFPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 431)
)
_JnxPicVQFX5C24X100GEPIC_ObjectIdentity = ObjectIdentity
jnxPicVQFX5C24X100GEPIC = _JnxPicVQFX5C24X100GEPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 432)
)
_JnxPicPTX1K72X40GEPIC_ObjectIdentity = ObjectIdentity
jnxPicPTX1K72X40GEPIC = _JnxPicPTX1K72X40GEPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 433)
)
_JnxPicQFX1000236Q_ObjectIdentity = ObjectIdentity
jnxPicQFX1000236Q = _JnxPicQFX1000236Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 434)
)
_JnxPicQFX1000272Q_ObjectIdentity = ObjectIdentity
jnxPicQFX1000272Q = _JnxPicQFX1000272Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 435)
)
_JnxPicQFX520032C32Q_ObjectIdentity = ObjectIdentity
jnxPicQFX520032C32Q = _JnxPicQFX520032C32Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 436)
)
_JnxPicQFX520032C64Q_ObjectIdentity = ObjectIdentity
jnxPicQFX520032C64Q = _JnxPicQFX520032C64Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 437)
)
_JnxPicQ511048S4Q2C_ObjectIdentity = ObjectIdentity
jnxPicQ511048S4Q2C = _JnxPicQ511048S4Q2C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 438)
)
_JnxPicQ511032Q4C_ObjectIdentity = ObjectIdentity
jnxPicQ511032Q4C = _JnxPicQ511032Q4C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 439)
)
_JnxPicEX3400QSFP2Port_ObjectIdentity = ObjectIdentity
jnxPicEX3400QSFP2Port = _JnxPicEX3400QSFP2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 440)
)
_JnxPicEX3400UplinkSFPPlus4Port_ObjectIdentity = ObjectIdentity
jnxPicEX3400UplinkSFPPlus4Port = _JnxPicEX3400UplinkSFPPlus4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 441)
)
_JnxPic10GE40GE100GEPIC_ObjectIdentity = ObjectIdentity
jnxPic10GE40GE100GEPIC = _JnxPic10GE40GE100GEPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 442)
)
_JnxPicEX2300UplinkSFPPlus4Port_ObjectIdentity = ObjectIdentity
jnxPicEX2300UplinkSFPPlus4Port = _JnxPicEX2300UplinkSFPPlus4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 443)
)
_JnxPicEX2300UplinkSFPPlus2Port_ObjectIdentity = ObjectIdentity
jnxPicEX2300UplinkSFPPlus2Port = _JnxPicEX2300UplinkSFPPlus2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 444)
)
_JnxPicSRXSMET1E1RPIC_ObjectIdentity = ObjectIdentity
jnxPicSRXSMET1E1RPIC = _JnxPicSRXSMET1E1RPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 445)
)
_JnxPicSRXSMEVDSLANNEXARPIC_ObjectIdentity = ObjectIdentity
jnxPicSRXSMEVDSLANNEXARPIC = _JnxPicSRXSMEVDSLANNEXARPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 446)
)
_JnxPicSRXSMESERIALRPIC_ObjectIdentity = ObjectIdentity
jnxPicSRXSMESERIALRPIC = _JnxPicSRXSMESERIALRPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 447)
)
_JnxPicSRXSME16PORTGEPOERPIC_ObjectIdentity = ObjectIdentity
jnxPicSRXSME16PORTGEPOERPIC = _JnxPicSRXSME16PORTGEPOERPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 448)
)
_JnxPicSRXSME8SFPRPIC_ObjectIdentity = ObjectIdentity
jnxPicSRXSME8SFPRPIC = _JnxPicSRXSME8SFPRPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 449)
)
_JnxPicULC36Q12Q28_ObjectIdentity = ObjectIdentity
jnxPicULC36Q12Q28 = _JnxPicULC36Q12Q28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 450)
)
_JnxPicULC30Q28_ObjectIdentity = ObjectIdentity
jnxPicULC30Q28 = _JnxPicULC30Q28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 451)
)
_JnxPicVMXMIC_ObjectIdentity = ObjectIdentity
jnxPicVMXMIC = _JnxPicVMXMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 452)
)
_JnxPicMIC8OC3OC124OC48_ObjectIdentity = ObjectIdentity
jnxPicMIC8OC3OC124OC48 = _JnxPicMIC8OC3OC124OC48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 453)
)
_JnxPicMIC4OC3OC121OC48_ObjectIdentity = ObjectIdentity
jnxPicMIC4OC3OC121OC48 = _JnxPicMIC4OC3OC121OC48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 454)
)
_JnxPicMIC8DS3E3_ObjectIdentity = ObjectIdentity
jnxPicMIC8DS3E3 = _JnxPicMIC8DS3E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 455)
)
_JnxPicMIC8CHDS3E3_ObjectIdentity = ObjectIdentity
jnxPicMIC8CHDS3E3 = _JnxPicMIC8CHDS3E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 456)
)
_JnxPicMIC8CHOC34CHOC12_ObjectIdentity = ObjectIdentity
jnxPicMIC8CHOC34CHOC12 = _JnxPicMIC8CHOC34CHOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 457)
)
_JnxPicMIC4CHOC32CHOC12_ObjectIdentity = ObjectIdentity
jnxPicMIC4CHOC32CHOC12 = _JnxPicMIC4CHOC32CHOC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 458)
)
_JnxPicMIC1CHOC48_ObjectIdentity = ObjectIdentity
jnxPicMIC1CHOC48 = _JnxPicMIC1CHOC48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 459)
)
_JnxPicMIC12CHE1T1_ObjectIdentity = ObjectIdentity
jnxPicMIC12CHE1T1 = _JnxPicMIC12CHE1T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 460)
)
_JnxPicMIC1OC192HOVCAT_ObjectIdentity = ObjectIdentity
jnxPicMIC1OC192HOVCAT = _JnxPicMIC1OC192HOVCAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 461)
)
_JnxPicSHO10X100GEQSFPV2PIC_ObjectIdentity = ObjectIdentity
jnxPicSHO10X100GEQSFPV2PIC = _JnxPicSHO10X100GEQSFPV2PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 462)
)
_JnxPicGLD96x10GE24x40GE8x100GEQSFPV2PIC_ObjectIdentity = ObjectIdentity
jnxPicGLD96x10GE24x40GE8x100GEQSFPV2PIC = _JnxPicGLD96x10GE24x40GE8x100GEQSFPV2PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 463)
)
_JnxPicSummitSRX1RU4xQSFP28PIC_ObjectIdentity = ObjectIdentity
jnxPicSummitSRX1RU4xQSFP28PIC = _JnxPicSummitSRX1RU4xQSFP28PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 464)
)
_JnxPicSummitSRX1RU8xSFPPPIC_ObjectIdentity = ObjectIdentity
jnxPicSummitSRX1RU8xSFPPPIC = _JnxPicSummitSRX1RU8xSFPPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 465)
)
_JnxPicSummitSRX3RU4xQSFPPPIC_ObjectIdentity = ObjectIdentity
jnxPicSummitSRX3RU4xQSFPPPIC = _JnxPicSummitSRX3RU4xQSFPPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 466)
)
_JnxPicOpusFcQic8X10G_ObjectIdentity = ObjectIdentity
jnxPicOpusFcQic8X10G = _JnxPicOpusFcQic8X10G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 467)
)
_JnxPicPTX3X400GE12X100GECFP8PIC_ObjectIdentity = ObjectIdentity
jnxPicPTX3X400GE12X100GECFP8PIC = _JnxPicPTX3X400GE12X100GECFP8PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 468)
)
_JnxPicSummitLoadTIC_ObjectIdentity = ObjectIdentity
jnxPicSummitLoadTIC = _JnxPicSummitLoadTIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 469)
)
_JnxPicMXTSR802xSFPP2xSFPSecureMIC_ObjectIdentity = ObjectIdentity
jnxPicMXTSR802xSFPP2xSFPSecureMIC = _JnxPicMXTSR802xSFPP2xSFPSecureMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 470)
)
_JnxPicValeLoadTicS2SAirFlow_ObjectIdentity = ObjectIdentity
jnxPicValeLoadTicS2SAirFlow = _JnxPicValeLoadTicS2SAirFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 471)
)
_JnxPicSRXSMELTEAAPIC_ObjectIdentity = ObjectIdentity
jnxPicSRXSMELTEAAPIC = _JnxPicSRXSMELTEAAPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 472)
)
_JnxPicSRXSMELTEAEPIC_ObjectIdentity = ObjectIdentity
jnxPicSRXSMELTEAEPIC = _JnxPicSRXSMELTEAEPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 473)
)
_JnxPic5XQSFPP_ObjectIdentity = ObjectIdentity
jnxPic5XQSFPP = _JnxPic5XQSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 474)
)
_JnxPicEX4300MP4xSFPPlusPIC_ObjectIdentity = ObjectIdentity
jnxPicEX4300MP4xSFPPlusPIC = _JnxPicEX4300MP4xSFPPlusPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 475)
)
_JnxPicEX4300MP2xQSFPPIC_ObjectIdentity = ObjectIdentity
jnxPicEX4300MP2xQSFPPIC = _JnxPicEX4300MP2xQSFPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 476)
)
_JnxPicEx4300MP1xQSFP28PIC_ObjectIdentity = ObjectIdentity
jnxPicEx4300MP1xQSFP28PIC = _JnxPicEx4300MP1xQSFP28PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 477)
)
_JnxPicNFXEM8T_ObjectIdentity = ObjectIdentity
jnxPicNFXEM8T = _JnxPicNFXEM8T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 478)
)
_JnxPicNFXEM4XSFP_ObjectIdentity = ObjectIdentity
jnxPicNFXEM4XSFP = _JnxPicNFXEM4XSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 479)
)
_JnxPicNFXEM8XSFP_ObjectIdentity = ObjectIdentity
jnxPicNFXEM8XSFP = _JnxPicNFXEM8XSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 480)
)
_JnxPicNFXEM2T2SFP_ObjectIdentity = ObjectIdentity
jnxPicNFXEM2T2SFP = _JnxPicNFXEM2T2SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 481)
)
_JnxPicNFXEMLTEAE_ObjectIdentity = ObjectIdentity
jnxPicNFXEMLTEAE = _JnxPicNFXEMLTEAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 482)
)
_JnxPicNFXEMLTEAA_ObjectIdentity = ObjectIdentity
jnxPicNFXEMLTEAA = _JnxPicNFXEMLTEAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 483)
)
_JnxPicSummitMX3RU6xQSPPPIC_ObjectIdentity = ObjectIdentity
jnxPicSummitMX3RU6xQSPPPIC = _JnxPicSummitMX3RU6xQSPPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 484)
)
_JnxPicSummitMX3RU12xQSFP28MacsecTIC_ObjectIdentity = ObjectIdentity
jnxPicSummitMX3RU12xQSFP28MacsecTIC = _JnxPicSummitMX3RU12xQSFP28MacsecTIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 485)
)
_JnxPicSummitMX3RU12xQSFP28TIC_ObjectIdentity = ObjectIdentity
jnxPicSummitMX3RU12xQSFP28TIC = _JnxPicSummitMX3RU12xQSFP28TIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 486)
)
_JnxPicSummitSRXHA4xSFPPPIC_ObjectIdentity = ObjectIdentity
jnxPicSummitSRXHA4xSFPPPIC = _JnxPicSummitSRXHA4xSFPPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 487)
)
_JnxPicQFX540016QSFP28TIC_ObjectIdentity = ObjectIdentity
jnxPicQFX540016QSFP28TIC = _JnxPicQFX540016QSFP28TIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 488)
)
_JnxPicEX4300MPQSFPPlus4Port_ObjectIdentity = ObjectIdentity
jnxPicEX4300MPQSFPPlus4Port = _JnxPicEX4300MPQSFPPlus4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 489)
)
_JnxPicBracklaPIC_ObjectIdentity = ObjectIdentity
jnxPicBracklaPIC = _JnxPicBracklaPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 490)
)
_JnxPicACX544848X10GESFPMIC_ObjectIdentity = ObjectIdentity
jnxPicACX544848X10GESFPMIC = _JnxPicACX544848X10GESFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 491)
)
_JnxPicACX54484X100GESFPMIC_ObjectIdentity = ObjectIdentity
jnxPicACX54484X100GESFPMIC = _JnxPicACX54484X100GESFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 492)
)
_JnxPicRedbull10xQSFPPPIC_ObjectIdentity = ObjectIdentity
jnxPicRedbull10xQSFPPPIC = _JnxPicRedbull10xQSFPPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 493)
)
_JnxPicPTXfake3X400GECFP8_ObjectIdentity = ObjectIdentity
jnxPicPTXfake3X400GECFP8 = _JnxPicPTXfake3X400GECFP8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 494)
)
_JnxPicSummitSRXFLOWPIC_ObjectIdentity = ObjectIdentity
jnxPicSummitSRXFLOWPIC = _JnxPicSummitSRXFLOWPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 495)
)
_JnxPicStout12xQSFP28MacsecTIC_ObjectIdentity = ObjectIdentity
jnxPicStout12xQSFP28MacsecTIC = _JnxPicStout12xQSFP28MacsecTIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 497)
)
_JnxPicPTX10008XCFP2DCOTIC_ObjectIdentity = ObjectIdentity
jnxPicPTX10008XCFP2DCOTIC = _JnxPicPTX10008XCFP2DCOTIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 498)
)
_JnxPicQFX1000260C_ObjectIdentity = ObjectIdentity
jnxPicQFX1000260C = _JnxPicQFX1000260C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 499)
)
_JnxPicEX2300MPUplinkSFPPlus6Port_ObjectIdentity = ObjectIdentity
jnxPicEX2300MPUplinkSFPPlus6Port = _JnxPicEX2300MPUplinkSFPPlus6Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 500)
)
_JnxPicEX2300MPUplinkSFPPlus4Port_ObjectIdentity = ObjectIdentity
jnxPicEX2300MPUplinkSFPPlus4Port = _JnxPicEX2300MPUplinkSFPPlus4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 501)
)
_JnxPicSPC3SPUCPType1PIC_ObjectIdentity = ObjectIdentity
jnxPicSPC3SPUCPType1PIC = _JnxPicSPC3SPUCPType1PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 502)
)
_JnxPicSPC3SPUFlowType2PIC_ObjectIdentity = ObjectIdentity
jnxPicSPC3SPUFlowType2PIC = _JnxPicSPC3SPUFlowType2PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 503)
)
_JnxPicSPC3SPUCPFlowType3PIC_ObjectIdentity = ObjectIdentity
jnxPicSPC3SPUCPFlowType3PIC = _JnxPicSPC3SPUCPFlowType3PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 504)
)
_JnxPicGLD15x100GE15x40GE60x10GEQSFPPIC_ObjectIdentity = ObjectIdentity
jnxPicGLD15x100GE15x40GE60x10GEQSFPPIC = _JnxPicGLD15x100GE15x40GE60x10GEQSFPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 505)
)
_JnxPicGLD96x10GE24x40GEQSFPPIC_ObjectIdentity = ObjectIdentity
jnxPicGLD96x10GE24x40GEQSFPPIC = _JnxPicGLD96x10GE24x40GEQSFPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 506)
)
_JnxPicIndus4xQSFP28MacsecPIC_ObjectIdentity = ObjectIdentity
jnxPicIndus4xQSFP28MacsecPIC = _JnxPicIndus4xQSFP28MacsecPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 507)
)
_JnxPic2x10GESFPP20xGESFPMACSecMIC_ObjectIdentity = ObjectIdentity
jnxPic2x10GESFPP20xGESFPMACSecMIC = _JnxPic2x10GESFPP20xGESFPMACSecMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 509)
)
_JnxPicIndus4xQSFP28SyncePIC_ObjectIdentity = ObjectIdentity
jnxPicIndus4xQSFP28SyncePIC = _JnxPicIndus4xQSFP28SyncePIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 510)
)
_JnxPicQFX521064C_ObjectIdentity = ObjectIdentity
jnxPicQFX521064C = _JnxPicQFX521064C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 511)
)
_JnxPicQFX520048Y_ObjectIdentity = ObjectIdentity
jnxPicQFX520048Y = _JnxPicQFX520048Y_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 512)
)
_JnxPicPTX1000260C_ObjectIdentity = ObjectIdentity
jnxPicPTX1000260C = _JnxPicPTX1000260C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 513)
)
_JnxPicSapphire32CDPIC_ObjectIdentity = ObjectIdentity
jnxPicSapphire32CDPIC = _JnxPicSapphire32CDPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 514)
)
_JnxPicSapphire128CPIC_ObjectIdentity = ObjectIdentity
jnxPicSapphire128CPIC = _JnxPicSapphire128CPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 515)
)
_JnxPicDCOSQFX520032CPIC_ObjectIdentity = ObjectIdentity
jnxPicDCOSQFX520032CPIC = _JnxPicDCOSQFX520032CPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 516)
)
_JnxPicRB5xQSFPP_ObjectIdentity = ObjectIdentity
jnxPicRB5xQSFPP = _JnxPicRB5xQSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 517)
)
_JnxPicJnp10k36xQSFPDD_ObjectIdentity = ObjectIdentity
jnxPicJnp10k36xQSFPDD = _JnxPicJnp10k36xQSFPDD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 518)
)
_JnxPicQFX512048Y8C_ObjectIdentity = ObjectIdentity
jnxPicQFX512048Y8C = _JnxPicQFX512048Y8C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 519)
)
_JnxPicEX465048Y8C_ObjectIdentity = ObjectIdentity
jnxPicEX465048Y8C = _JnxPicEX465048Y8C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 520)
)
_JnxPicAttella8XQSFP28PIC_ObjectIdentity = ObjectIdentity
jnxPicAttella8XQSFP28PIC = _JnxPicAttella8XQSFP28PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 521)
)
_JnxPicAttella4XCFP2DCOPIC_ObjectIdentity = ObjectIdentity
jnxPicAttella4XCFP2DCOPIC = _JnxPicAttella4XCFP2DCOPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 522)
)
_JnxPicACX5448M44X10GESFPMIC_ObjectIdentity = ObjectIdentity
jnxPicACX5448M44X10GESFPMIC = _JnxPicACX5448M44X10GESFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 527)
)
_JnxPicACX5448M6X100GEQSFPMIC_ObjectIdentity = ObjectIdentity
jnxPicACX5448M6X100GEQSFPMIC = _JnxPicACX5448M6X100GEQSFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 528)
)
_JnxPicACX5448D36X10GESFPMIC_ObjectIdentity = ObjectIdentity
jnxPicACX5448D36X10GESFPMIC = _JnxPicACX5448D36X10GESFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 529)
)
_JnxPicACX5448D2X100GEQSFPMIC_ObjectIdentity = ObjectIdentity
jnxPicACX5448D2X100GEQSFPMIC = _JnxPicACX5448D2X100GEQSFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 530)
)
_JnxPicACX5448D2X200GECFP2DCOMIC_ObjectIdentity = ObjectIdentity
jnxPicACX5448D2X200GECFP2DCOMIC = _JnxPicACX5448D2X200GECFP2DCOMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 531)
)
_JnxPicAS781664X_ObjectIdentity = ObjectIdentity
jnxPicAS781664X = _JnxPicAS781664X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 532)
)
_JnxPicQFX512032C_ObjectIdentity = ObjectIdentity
jnxPicQFX512032C = _JnxPicQFX512032C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 533)
)
_JnxPicIOCIV6XQSFPP_ObjectIdentity = ObjectIdentity
jnxPicIOCIV6XQSFPP = _JnxPicIOCIV6XQSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 534)
)
_JnxPicIOCIV20X10GESFPP_ObjectIdentity = ObjectIdentity
jnxPicIOCIV20X10GESFPP = _JnxPicIOCIV20X10GESFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 535)
)
_JnxPicMXSPC3PIC_ObjectIdentity = ObjectIdentity
jnxPicMXSPC3PIC = _JnxPicMXSPC3PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 536)
)
_JnxPicJnp10k36xQDDPIC_ObjectIdentity = ObjectIdentity
jnxPicJnp10k36xQDDPIC = _JnxPicJnp10k36xQDDPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 537)
)
_JnxPicSRXSMEWAPUSPIC_ObjectIdentity = ObjectIdentity
jnxPicSRXSMEWAPUSPIC = _JnxPicSRXSMEWAPUSPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 538)
)
_JnxPicSRXSMEWAPISPIC_ObjectIdentity = ObjectIdentity
jnxPicSRXSMEWAPISPIC = _JnxPicSRXSMEWAPISPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 539)
)
_JnxPicSRXSMEWAPWWPIC_ObjectIdentity = ObjectIdentity
jnxPicSRXSMEWAPWWPIC = _JnxPicSRXSMEWAPWWPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 540)
)
_JnxPicACX71024X10GESFPMIC_ObjectIdentity = ObjectIdentity
jnxPicACX71024X10GESFPMIC = _JnxPicACX71024X10GESFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 541)
)
_JnxPicACX7104X100GESFPMIC_ObjectIdentity = ObjectIdentity
jnxPicACX7104X100GESFPMIC = _JnxPicACX7104X100GESFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 542)
)
_JnxPicACX580048X10GESFPMIC_ObjectIdentity = ObjectIdentity
jnxPicACX580048X10GESFPMIC = _JnxPicACX580048X10GESFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 543)
)
_JnxPicACX580032X10GESFPMIC_ObjectIdentity = ObjectIdentity
jnxPicACX580032X10GESFPMIC = _JnxPicACX580032X10GESFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 544)
)
_JnxPicACX58004X100GESFPMIC_ObjectIdentity = ObjectIdentity
jnxPicACX58004X100GESFPMIC = _JnxPicACX58004X100GESFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 545)
)
_JnxPicR667524X10GESFPMIC_ObjectIdentity = ObjectIdentity
jnxPicR667524X10GESFPMIC = _JnxPicR667524X10GESFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 546)
)
_JnxPicR66754X100GESFPMIC_ObjectIdentity = ObjectIdentity
jnxPicR66754X100GESFPMIC = _JnxPicR66754X100GESFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 547)
)
_JnxPicR627448X10GESFPMIC_ObjectIdentity = ObjectIdentity
jnxPicR627448X10GESFPMIC = _JnxPicR627448X10GESFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 548)
)
_JnxPicR627432X10GESFPMIC_ObjectIdentity = ObjectIdentity
jnxPicR627432X10GESFPMIC = _JnxPicR627432X10GESFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 549)
)
_JnxPicR62744X100GESFPMIC_ObjectIdentity = ObjectIdentity
jnxPicR62744X100GESFPMIC = _JnxPicR62744X100GESFPMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 550)
)
_JnxPicEX44004x25GESFP28PIC_ObjectIdentity = ObjectIdentity
jnxPicEX44004x25GESFP28PIC = _JnxPicEX44004x25GESFP28PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 551)
)
_JnxPicEX44004x10GESFPPPIC_ObjectIdentity = ObjectIdentity
jnxPicEX44004x10GESFPPPIC = _JnxPicEX44004x10GESFPPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 552)
)
_JnxPicQFX512048T6C_ObjectIdentity = ObjectIdentity
jnxPicQFX512048T6C = _JnxPicQFX512048T6C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 553)
)
_JnxPicArdbegPIC_ObjectIdentity = ObjectIdentity
jnxPicArdbegPIC = _JnxPicArdbegPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 554)
)
_JnxPicJnp10k4xQDD32xQ_ObjectIdentity = ObjectIdentity
jnxPicJnp10k4xQDD32xQ = _JnxPicJnp10k4xQDD32xQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 556)
)
_JnxPicEXMRATE5XQSFPP_ObjectIdentity = ObjectIdentity
jnxPicEXMRATE5XQSFPP = _JnxPicEXMRATE5XQSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 557)
)
_JnxPicQFX513032CDPIC_ObjectIdentity = ObjectIdentity
jnxPicQFX513032CDPIC = _JnxPicQFX513032CDPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 558)
)
_JnxPicQFX513048CPIC_ObjectIdentity = ObjectIdentity
jnxPicQFX513048CPIC = _JnxPicQFX513048CPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 559)
)
_JnxPicACX7538x25GESFP28PIC_ObjectIdentity = ObjectIdentity
jnxPicACX7538x25GESFP28PIC = _JnxPicACX7538x25GESFP28PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 560)
)
_JnxPicACX7532x100GEQSFP28PIC_ObjectIdentity = ObjectIdentity
jnxPicACX7532x100GEQSFP28PIC = _JnxPicACX7532x100GEQSFP28PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 561)
)
_JnxPicACX7534x100GEQSFP28PIC_ObjectIdentity = ObjectIdentity
jnxPicACX7534x100GEQSFP28PIC = _JnxPicACX7534x100GEQSFP28PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 562)
)
_JnxPicACX7538x10GESFPPIC_ObjectIdentity = ObjectIdentity
jnxPicACX7538x10GESFPPIC = _JnxPicACX7538x10GESFPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 563)
)
_JnxPicJerrico2PIC_ObjectIdentity = ObjectIdentity
jnxPicJerrico2PIC = _JnxPicJerrico2PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 564)
)
_JnxPicJNP710048LPIC_ObjectIdentity = ObjectIdentity
jnxPicJNP710048LPIC = _JnxPicJNP710048LPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 565)
)
_JnxPicACX710032CPIC_ObjectIdentity = ObjectIdentity
jnxPicACX710032CPIC = _JnxPicACX710032CPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 566)
)
_JnxPicJNP710080PIC_ObjectIdentity = ObjectIdentity
jnxPicJNP710080PIC = _JnxPicJNP710080PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 567)
)
_JnxPicDaniel24xSFPP1G10GPIC_ObjectIdentity = ObjectIdentity
jnxPicDaniel24xSFPP1G10GPIC = _JnxPicDaniel24xSFPP1G10GPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 568)
)
_JnxPicQFX512048YM8C_ObjectIdentity = ObjectIdentity
jnxPicQFX512048YM8C = _JnxPicQFX512048YM8C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 569)
)
_JnxPicLC96004xQDDPIC_ObjectIdentity = ObjectIdentity
jnxPicLC96004xQDDPIC = _JnxPicLC96004xQDDPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 570)
)
_JnxPicQFX570016x100QSFP28PIC_ObjectIdentity = ObjectIdentity
jnxPicQFX570016x100QSFP28PIC = _JnxPicQFX570016x100QSFP28PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 571)
)
_JnxPicQFX57004x400QSFP56DDPIC_ObjectIdentity = ObjectIdentity
jnxPicQFX57004x400QSFP56DDPIC = _JnxPicQFX57004x400QSFP56DDPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 572)
)
_JnxPicACX75520x1G10G25G50GSFP28PIC_ObjectIdentity = ObjectIdentity
jnxPicACX75520x1G10G25G50GSFP28PIC = _JnxPicACX75520x1G10G25G50GSFP28PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 573)
)
_JnxPicJNP710048LPSMPIC_ObjectIdentity = ObjectIdentity
jnxPicJNP710048LPSMPIC = _JnxPicJNP710048LPSMPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 574)
)
_JnxPicACX710032CPSMPIC_ObjectIdentity = ObjectIdentity
jnxPicACX710032CPSMPIC = _JnxPicACX710032CPSMPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 575)
)
_JnxPicSRXEMLTEAA_ObjectIdentity = ObjectIdentity
jnxPicSRXEMLTEAA = _JnxPicSRXEMLTEAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 576)
)
_JnxPicSRXEMLTEAE_ObjectIdentity = ObjectIdentity
jnxPicSRXEMLTEAE = _JnxPicSRXEMLTEAE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 577)
)
_JnxPicSRXEM4T2SFP_ObjectIdentity = ObjectIdentity
jnxPicSRXEM4T2SFP = _JnxPicSRXEM4T2SFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 578)
)
_JnxPicACX75516x100QSFP28PIC_ObjectIdentity = ObjectIdentity
jnxPicACX75516x100QSFP28PIC = _JnxPicACX75516x100QSFP28PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 579)
)
_JnxPicACX7554x400QSFP56DDPIC_ObjectIdentity = ObjectIdentity
jnxPicACX7554x400QSFP56DDPIC = _JnxPicACX7554x400QSFP56DDPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 580)
)
_JnxPicWBONLPIC_ObjectIdentity = ObjectIdentity
jnxPicWBONLPIC = _JnxPicWBONLPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 581)
)
_JnxPic5GS6GLPIC_ObjectIdentity = ObjectIdentity
jnxPic5GS6GLPIC = _JnxPic5GS6GLPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 582)
)
_JnxPic5GS6MWNAPIC_ObjectIdentity = ObjectIdentity
jnxPic5GS6MWNAPIC = _JnxPic5GS6MWNAPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 583)
)
_JnxPic5GS6MWEAPIC_ObjectIdentity = ObjectIdentity
jnxPic5GS6MWEAPIC = _JnxPic5GS6MWEAPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 584)
)
_JnxPicTabascoCryptoSPC4Type1PIC_ObjectIdentity = ObjectIdentity
jnxPicTabascoCryptoSPC4Type1PIC = _JnxPicTabascoCryptoSPC4Type1PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 585)
)
_JnxPicTabascoCryptoSPC4Type2PIC_ObjectIdentity = ObjectIdentity
jnxPicTabascoCryptoSPC4Type2PIC = _JnxPicTabascoCryptoSPC4Type2PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 586)
)
_JnxPicTabascoCryptoSPC4Type3PIC_ObjectIdentity = ObjectIdentity
jnxPicTabascoCryptoSPC4Type3PIC = _JnxPicTabascoCryptoSPC4Type3PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 587)
)
_JnxPicTabascoCryptoSPC4MXPIC_ObjectIdentity = ObjectIdentity
jnxPicTabascoCryptoSPC4MXPIC = _JnxPicTabascoCryptoSPC4MXPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 588)
)
_JnxPicEX44002xQSFP28PIC_ObjectIdentity = ObjectIdentity
jnxPicEX44002xQSFP28PIC = _JnxPicEX44002xQSFP28PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 589)
)
_JnxPicACX75520x10G25G50GSFP28PIC_ObjectIdentity = ObjectIdentity
jnxPicACX75520x10G25G50GSFP28PIC = _JnxPicACX75520x10G25G50GSFP28PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 590)
)
_JnxPicQFX523064CDPIC_ObjectIdentity = ObjectIdentity
jnxPicQFX523064CDPIC = _JnxPicQFX523064CDPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 591)
)
_JnxPicMX304PIC_ObjectIdentity = ObjectIdentity
jnxPicMX304PIC = _JnxPicMX304PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 592)
)
_JnxPicEX4100UplinkSFPPlus4Port_ObjectIdentity = ObjectIdentity
jnxPicEX4100UplinkSFPPlus4Port = _JnxPicEX4100UplinkSFPPlus4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 593)
)
_JnxPicEX4100UplinkSFPPlus2Port_ObjectIdentity = ObjectIdentity
jnxPicEX4100UplinkSFPPlus2Port = _JnxPicEX4100UplinkSFPPlus2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 594)
)
_JnxPicEX4100VCSFP284Port_ObjectIdentity = ObjectIdentity
jnxPicEX4100VCSFP284Port = _JnxPicEX4100VCSFP284Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 595)
)
_JnxPicIOCV5XQSFPP_ObjectIdentity = ObjectIdentity
jnxPicIOCV5XQSFPP = _JnxPicIOCV5XQSFPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 596)
)
_JnxPicEX44001xQSFP28PIC_ObjectIdentity = ObjectIdentity
jnxPicEX44001xQSFP28PIC = _JnxPicEX44001xQSFP28PIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 597)
)
_JnxPicGLQFX513048CPIC_ObjectIdentity = ObjectIdentity
jnxPicGLQFX513048CPIC = _JnxPicGLQFX513048CPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 598)
)
_JnxPicLC48002xQDD12xSDDPIC_ObjectIdentity = ObjectIdentity
jnxPicLC48002xQDD12xSDDPIC = _JnxPicLC48002xQDD12xSDDPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 600)
)
_JnxPicLC480016xSDDPIC_ObjectIdentity = ObjectIdentity
jnxPicLC480016xSDDPIC = _JnxPicLC480016xSDDPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 601)
)
_JnxPicLC48004xQDD8xQPIC_ObjectIdentity = ObjectIdentity
jnxPicLC48004xQDD8xQPIC = _JnxPicLC48004xQDD8xQPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 602)
)
_JnxPicGLQFX513048CMPIC_ObjectIdentity = ObjectIdentity
jnxPicGLQFX513048CMPIC = _JnxPicGLQFX513048CMPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 603)
)
_JnxPicGLDQFX5130E32CDPIC_ObjectIdentity = ObjectIdentity
jnxPicGLDQFX5130E32CDPIC = _JnxPicGLDQFX5130E32CDPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 604)
)
_JnxPicSRX160016x1GT_ObjectIdentity = ObjectIdentity
jnxPicSRX160016x1GT = _JnxPicSRX160016x1GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 605)
)
_JnxPicSRX16002xSFP28_ObjectIdentity = ObjectIdentity
jnxPicSRX16002xSFP28 = _JnxPicSRX16002xSFP28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 606)
)
_JnxPicSRX16004xSFP_ObjectIdentity = ObjectIdentity
jnxPicSRX16004xSFP = _JnxPicSRX16004xSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 607)
)
_JnxPicSRX23008x10GT_ObjectIdentity = ObjectIdentity
jnxPicSRX23008x10GT = _JnxPicSRX23008x10GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 608)
)
_JnxPicSRX23008xSFP_ObjectIdentity = ObjectIdentity
jnxPicSRX23008xSFP = _JnxPicSRX23008xSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 609)
)
_JnxPicSRX23004xSFP28_ObjectIdentity = ObjectIdentity
jnxPicSRX23004xSFP28 = _JnxPicSRX23004xSFP28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 610)
)
_JnxPicSRX23002QSFP28_ObjectIdentity = ObjectIdentity
jnxPicSRX23002QSFP28 = _JnxPicSRX23002QSFP28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 611)
)
_JnxPicSRX43008x10GT_ObjectIdentity = ObjectIdentity
jnxPicSRX43008x10GT = _JnxPicSRX43008x10GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 612)
)
_JnxPicSRX43008xSFP_ObjectIdentity = ObjectIdentity
jnxPicSRX43008xSFP = _JnxPicSRX43008xSFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 613)
)
_JnxPicSRX43004xSFP28_ObjectIdentity = ObjectIdentity
jnxPicSRX43004xSFP28 = _JnxPicSRX43004xSFP28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 614)
)
_JnxPicSRX43006QSFP28_ObjectIdentity = ObjectIdentity
jnxPicSRX43006QSFP28 = _JnxPicSRX43006QSFP28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 615)
)
_JnxPicQFX524064OSFPPIC_ObjectIdentity = ObjectIdentity
jnxPicQFX524064OSFPPIC = _JnxPicQFX524064OSFPPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 616)
)
_JnxPicQFX524064QSFPDDPIC_ObjectIdentity = ObjectIdentity
jnxPicQFX524064QSFPDDPIC = _JnxPicQFX524064QSFPDDPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 617)
)
_JnxPicSRX47001xQSFPDD5xQSFP288xSFP56_ObjectIdentity = ObjectIdentity
jnxPicSRX47001xQSFPDD5xQSFP288xSFP56 = _JnxPicSRX47001xQSFPDD5xQSFP288xSFP56_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 618)
)
_JnxPicSRX4700FlowPIC_ObjectIdentity = ObjectIdentity
jnxPicSRX4700FlowPIC = _JnxPicSRX4700FlowPIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 619)
)
_JnxPicEX4100VCSFPSFPPlus2Port_ObjectIdentity = ObjectIdentity
jnxPicEX4100VCSFPSFPPlus2Port = _JnxPicEX4100VCSFPSFPPlus2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 620)
)
_JnxPicEX4100VCSFPSFPPlus4Port_ObjectIdentity = ObjectIdentity
jnxPicEX4100VCSFPSFPPlus4Port = _JnxPicEX4100VCSFPSFPPlus4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 1, 621)
)
_JnxMic_ObjectIdentity = ObjectIdentity
jnxMic = _JnxMic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 3, 12, 2)
)
_JnxMiscComponent_ObjectIdentity = ObjectIdentity
jnxMiscComponent = _JnxMiscComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 4)
)
_JnxTempSensor_ObjectIdentity = ObjectIdentity
jnxTempSensor = _JnxTempSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 3, 4, 1)
)
_JnxClassStatus_ObjectIdentity = ObjectIdentity
jnxClassStatus = _JnxClassStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 4)
)
_JnxStatusSource_ObjectIdentity = ObjectIdentity
jnxStatusSource = _JnxStatusSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 4, 1)
)
_JnxStatusSourceM40_ObjectIdentity = ObjectIdentity
jnxStatusSourceM40 = _JnxStatusSourceM40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 4, 1, 1)
)
_JnxChassisSlotLED_ObjectIdentity = ObjectIdentity
jnxChassisSlotLED = _JnxChassisSlotLED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 4, 1, 1, 1)
)
_JnxChassisAlarmLED_ObjectIdentity = ObjectIdentity
jnxChassisAlarmLED = _JnxChassisAlarmLED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 4, 1, 1, 2)
)
_JnxHostCtlrLED_ObjectIdentity = ObjectIdentity
jnxHostCtlrLED = _JnxHostCtlrLED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 4, 1, 1, 3)
)
_JnxChassisTempSensor_ObjectIdentity = ObjectIdentity
jnxChassisTempSensor = _JnxChassisTempSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 4, 1, 1, 4)
)
_JnxRoutingEngineLED_ObjectIdentity = ObjectIdentity
jnxRoutingEngineLED = _JnxRoutingEngineLED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 1, 4, 1, 1, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-CHASSIS-DEFINES-MIB",
    **{"jnxClassification": jnxClassification,
       "jnxClassGeneral": jnxClassGeneral,
       "jnxProductLine": jnxProductLine,
       "jnxProductLineM40": jnxProductLineM40,
       "jnxProductLineM20": jnxProductLineM20,
       "jnxProductLineM160": jnxProductLineM160,
       "jnxProductLineM10": jnxProductLineM10,
       "jnxProductLineM5": jnxProductLineM5,
       "jnxProductLineT640": jnxProductLineT640,
       "jnxProductLineT320": jnxProductLineT320,
       "jnxProductLineM40e": jnxProductLineM40e,
       "jnxProductLineM320": jnxProductLineM320,
       "jnxProductLineM7i": jnxProductLineM7i,
       "jnxProductLineM10i": jnxProductLineM10i,
       "jnxProductLineJ2300": jnxProductLineJ2300,
       "jnxProductLineJ4300": jnxProductLineJ4300,
       "jnxProductLineJ6300": jnxProductLineJ6300,
       "jnxProductLineIRM": jnxProductLineIRM,
       "jnxProductLineTX": jnxProductLineTX,
       "jnxProductLineM120": jnxProductLineM120,
       "jnxProductLineJ4350": jnxProductLineJ4350,
       "jnxProductLineJ6350": jnxProductLineJ6350,
       "jnxProductLineMX960": jnxProductLineMX960,
       "jnxProductLineJ4320": jnxProductLineJ4320,
       "jnxProductLineJ2320": jnxProductLineJ2320,
       "jnxProductLineJ2350": jnxProductLineJ2350,
       "jnxProductLineMX480": jnxProductLineMX480,
       "jnxProductLineSRX5800": jnxProductLineSRX5800,
       "jnxProductLineT1600": jnxProductLineT1600,
       "jnxProductLineSRX5600": jnxProductLineSRX5600,
       "jnxProductLineMX240": jnxProductLineMX240,
       "jnxProductLineEX3200": jnxProductLineEX3200,
       "jnxProductLineEX4200": jnxProductLineEX4200,
       "jnxProductLineEX8208": jnxProductLineEX8208,
       "jnxProductLineEX8216": jnxProductLineEX8216,
       "jnxProductLineSRX3600": jnxProductLineSRX3600,
       "jnxProductLineSRX3400": jnxProductLineSRX3400,
       "jnxProductLineSRX210": jnxProductLineSRX210,
       "jnxProductLineTXP": jnxProductLineTXP,
       "jnxProductLineJCS": jnxProductLineJCS,
       "jnxProductLineSRX240": jnxProductLineSRX240,
       "jnxProductLineSRX650": jnxProductLineSRX650,
       "jnxProductLineSRX100": jnxProductLineSRX100,
       "jnxProductLineLN1000V": jnxProductLineLN1000V,
       "jnxProductLineEX2200": jnxProductLineEX2200,
       "jnxProductLineEX4500": jnxProductLineEX4500,
       "jnxProductLineFXSeries": jnxProductLineFXSeries,
       "jnxProductLineIBM4274M02J02M": jnxProductLineIBM4274M02J02M,
       "jnxProductLineIBM4274M06J06M": jnxProductLineIBM4274M06J06M,
       "jnxProductLineIBM4274M11J11M": jnxProductLineIBM4274M11J11M,
       "jnxProductLineSRX1400": jnxProductLineSRX1400,
       "jnxProductLineIBM4274S58J58S": jnxProductLineIBM4274S58J58S,
       "jnxProductLineIBM4274S56J56S": jnxProductLineIBM4274S56J56S,
       "jnxProductLineIBM4274S36J36S": jnxProductLineIBM4274S36J36S,
       "jnxProductLineIBM4274S34J34S": jnxProductLineIBM4274S34J34S,
       "jnxProductLineIBM427348EJ48E": jnxProductLineIBM427348EJ48E,
       "jnxProductLineIBM4274E08J08E": jnxProductLineIBM4274E08J08E,
       "jnxProductLineIBM4274E16J16E": jnxProductLineIBM4274E16J16E,
       "jnxProductLineMX80": jnxProductLineMX80,
       "jnxProductLineSRX220": jnxProductLineSRX220,
       "jnxProductLineEXXRE": jnxProductLineEXXRE,
       "jnxProductLineQFXInterconnect": jnxProductLineQFXInterconnect,
       "jnxProductLineQFXNode": jnxProductLineQFXNode,
       "jnxProductLineQFXJVRE": jnxProductLineQFXJVRE,
       "jnxProductLineEX4300": jnxProductLineEX4300,
       "jnxProductLineSRX110": jnxProductLineSRX110,
       "jnxProductLineSRX120": jnxProductLineSRX120,
       "jnxProductLineMAG8600": jnxProductLineMAG8600,
       "jnxProductLineMAG6611": jnxProductLineMAG6611,
       "jnxProductLineMAG6610": jnxProductLineMAG6610,
       "jnxProductLinePTX5000": jnxProductLinePTX5000,
       "jnxProductLineIBM0719J45E": jnxProductLineIBM0719J45E,
       "jnxProductLineIBMJ08F": jnxProductLineIBMJ08F,
       "jnxProductLineIBMJ52F": jnxProductLineIBMJ52F,
       "jnxProductLineEX6210": jnxProductLineEX6210,
       "jnxProductLineDellJFX3500": jnxProductLineDellJFX3500,
       "jnxProductLineEX3300": jnxProductLineEX3300,
       "jnxProductLineDELLJSRX3600": jnxProductLineDELLJSRX3600,
       "jnxProductLineDELLJSRX3400": jnxProductLineDELLJSRX3400,
       "jnxProductLineDELLJSRX1400": jnxProductLineDELLJSRX1400,
       "jnxProductLineDELLJSRX5800": jnxProductLineDELLJSRX5800,
       "jnxProductLineDELLJSRX5600": jnxProductLineDELLJSRX5600,
       "jnxProductLineQFXSwitch": jnxProductLineQFXSwitch,
       "jnxProductLineT4000": jnxProductLineT4000,
       "jnxProductLineQFX3000": jnxProductLineQFX3000,
       "jnxProductLineQFX5000": jnxProductLineQFX5000,
       "jnxProductLineSRX550": jnxProductLineSRX550,
       "jnxProductLineACX": jnxProductLineACX,
       "jnxProductLineMX40": jnxProductLineMX40,
       "jnxProductLineMX10": jnxProductLineMX10,
       "jnxProductLineMX5": jnxProductLineMX5,
       "jnxProductLineQFXMInterconnect": jnxProductLineQFXMInterconnect,
       "jnxProductLineEX4550": jnxProductLineEX4550,
       "jnxProductLineMX2020": jnxProductLineMX2020,
       "jnxProductLineVseries": jnxProductLineVseries,
       "jnxProductLineLN2600": jnxProductLineLN2600,
       "jnxProductLineFireflyPerimeter": jnxProductLineFireflyPerimeter,
       "jnxProductLineMX104": jnxProductLineMX104,
       "jnxProductLinePTX3000": jnxProductLinePTX3000,
       "jnxProductLineMX2010": jnxProductLineMX2010,
       "jnxProductLineQFX3100": jnxProductLineQFX3100,
       "jnxProductLineLN2800": jnxProductLineLN2800,
       "jnxProductLineEX9214": jnxProductLineEX9214,
       "jnxProductLineEX9208": jnxProductLineEX9208,
       "jnxProductLineEX9204": jnxProductLineEX9204,
       "jnxProductLineSRX5400": jnxProductLineSRX5400,
       "jnxProductLineIBM4274S54J54S": jnxProductLineIBM4274S54J54S,
       "jnxProductLineDELLJSRX5400": jnxProductLineDELLJSRX5400,
       "jnxProductLineVMX": jnxProductLineVMX,
       "jnxProductLineEX4600": jnxProductLineEX4600,
       "jnxProductLineVRR": jnxProductLineVRR,
       "jnxProductLineOCPAcc": jnxProductLineOCPAcc,
       "jnxProductLineACX1000": jnxProductLineACX1000,
       "jnxProductLineACX2000": jnxProductLineACX2000,
       "jnxProductLineACX1100": jnxProductLineACX1100,
       "jnxProductLineACX2100": jnxProductLineACX2100,
       "jnxProductLineACX2200": jnxProductLineACX2200,
       "jnxProductLineACX4000": jnxProductLineACX4000,
       "jnxProductLineACX500AC": jnxProductLineACX500AC,
       "jnxProductLineACX500DC": jnxProductLineACX500DC,
       "jnxProductLineACX500OAC": jnxProductLineACX500OAC,
       "jnxProductLineACX500ODC": jnxProductLineACX500ODC,
       "jnxProductLineACX500OPOEAC": jnxProductLineACX500OPOEAC,
       "jnxProductLineACX500OPOEDC": jnxProductLineACX500OPOEDC,
       "jnxProductLineSatelliteDevice": jnxProductLineSatelliteDevice,
       "jnxProductLineACX5048": jnxProductLineACX5048,
       "jnxProductLineACX5096": jnxProductLineACX5096,
       "jnxProductLineLN1000CC": jnxProductLineLN1000CC,
       "jnxProductLineVSRX": jnxProductLineVSRX,
       "jnxProductLinePTX1000": jnxProductLinePTX1000,
       "jnxProductLineEX3400": jnxProductLineEX3400,
       "jnxProductLineEX2300": jnxProductLineEX2300,
       "jnxProductLineSRX300": jnxProductLineSRX300,
       "jnxProductLineSRX320": jnxProductLineSRX320,
       "jnxProductLineSRX340": jnxProductLineSRX340,
       "jnxProductLineSRX345": jnxProductLineSRX345,
       "jnxProductLineSRX1500": jnxProductLineSRX1500,
       "jnxProductLineNFX": jnxProductLineNFX,
       "jnxProductLineJNP10003": jnxProductLineJNP10003,
       "jnxProductLineSRX4600": jnxProductLineSRX4600,
       "jnxProductLineSRX4800": jnxProductLineSRX4800,
       "jnxProductLineSRX4100": jnxProductLineSRX4100,
       "jnxProductLineSRX4200": jnxProductLineSRX4200,
       "jnxProductLineJNP204": jnxProductLineJNP204,
       "jnxProductLineMX2008": jnxProductLineMX2008,
       "jnxProductLineMXTSR80": jnxProductLineMXTSR80,
       "jnxProductLinePTX10008": jnxProductLinePTX10008,
       "jnxProductLineACX5448": jnxProductLineACX5448,
       "jnxProductLinePTX10016": jnxProductLinePTX10016,
       "jnxProductLineEX9251": jnxProductLineEX9251,
       "jnxProductLineMX150": jnxProductLineMX150,
       "jnxProductLineJNP10001": jnxProductLineJNP10001,
       "jnxProductLineMX10008": jnxProductLineMX10008,
       "jnxProductLineMX10016": jnxProductLineMX10016,
       "jnxProductLineEX9253": jnxProductLineEX9253,
       "jnxProductLineJRR200": jnxProductLineJRR200,
       "jnxProductLineACX5448M": jnxProductLineACX5448M,
       "jnxProductLineACX5448D": jnxProductLineACX5448D,
       "jnxProductLineACX6360OR": jnxProductLineACX6360OR,
       "jnxProductLineACX6360OX": jnxProductLineACX6360OX,
       "jnxProductLineACX710": jnxProductLineACX710,
       "jnxProductLineACX5800": jnxProductLineACX5800,
       "jnxProductLineSRX380": jnxProductLineSRX380,
       "jnxProductLineEX4400": jnxProductLineEX4400,
       "jnxProductLineR6675": jnxProductLineR6675,
       "jnxProductLineMX304": jnxProductLineMX304,
       "jnxProductLineMX10004": jnxProductLineMX10004,
       "jnxProductLineEX4100": jnxProductLineEX4100,
       "jnxProductLineEX4650": jnxProductLineEX4650,
       "jnxProductLinePTX1000260C": jnxProductLinePTX1000260C,
       "jnxProductLinePTX1000380c": jnxProductLinePTX1000380c,
       "jnxProductLinePTX10003160c": jnxProductLinePTX10003160c,
       "jnxProductLineQFX1000380c": jnxProductLineQFX1000380c,
       "jnxProductLineQFX10003160c": jnxProductLineQFX10003160c,
       "jnxProductLinePTX1000136mr": jnxProductLinePTX1000136mr,
       "jnxProductLinePTX10004": jnxProductLinePTX10004,
       "jnxProductLineACX753": jnxProductLineACX753,
       "jnxProductLineSRX1800": jnxProductLineSRX1800,
       "jnxProductLineACX7KSwitch": jnxProductLineACX7KSwitch,
       "jnxProductLineACX710032c": jnxProductLineACX710032c,
       "jnxProductLineACX710048l": jnxProductLineACX710048l,
       "jnxProductLineACX7908": jnxProductLineACX7908,
       "jnxProductLineACX7024": jnxProductLineACX7024,
       "jnxProductLineSRX1600": jnxProductLineSRX1600,
       "jnxProductLineSRX2300": jnxProductLineSRX2300,
       "jnxProductLineSRX4300": jnxProductLineSRX4300,
       "jnxProductLineACX7332": jnxProductLineACX7332,
       "jnxProductLineACX7348": jnxProductLineACX7348,
       "jnxProductLineACX7024X": jnxProductLineACX7024X,
       "jnxProductLinePTX1000236qdd": jnxProductLinePTX1000236qdd,
       "jnxProductLineSRX4700": jnxProductLineSRX4700,
       "jnxProductName": jnxProductName,
       "jnxProductNameM40": jnxProductNameM40,
       "jnxProductNameM20": jnxProductNameM20,
       "jnxProductNameM160": jnxProductNameM160,
       "jnxProductNameM10": jnxProductNameM10,
       "jnxProductNameM5": jnxProductNameM5,
       "jnxProductNameT640": jnxProductNameT640,
       "jnxProductNameT320": jnxProductNameT320,
       "jnxProductNameM40e": jnxProductNameM40e,
       "jnxProductNameM320": jnxProductNameM320,
       "jnxProductNameM7i": jnxProductNameM7i,
       "jnxProductNameM10i": jnxProductNameM10i,
       "jnxProductNameJ2300": jnxProductNameJ2300,
       "jnxProductNameJ4300": jnxProductNameJ4300,
       "jnxProductNameJ6300": jnxProductNameJ6300,
       "jnxProductNameIRM": jnxProductNameIRM,
       "jnxProductNameTX": jnxProductNameTX,
       "jnxProductNameM120": jnxProductNameM120,
       "jnxProductNameJ4350": jnxProductNameJ4350,
       "jnxProductNameJ6350": jnxProductNameJ6350,
       "jnxProductNameMX960": jnxProductNameMX960,
       "jnxProductNameJ4320": jnxProductNameJ4320,
       "jnxProductNameJ2320": jnxProductNameJ2320,
       "jnxProductNameJ2350": jnxProductNameJ2350,
       "jnxProductNameMX480": jnxProductNameMX480,
       "jnxProductNameSRX5800": jnxProductNameSRX5800,
       "jnxProductNameT1600": jnxProductNameT1600,
       "jnxProductNameSRX5600": jnxProductNameSRX5600,
       "jnxProductNameMX240": jnxProductNameMX240,
       "jnxProductNameEX3200": jnxProductNameEX3200,
       "jnxProductNameEX4200": jnxProductNameEX4200,
       "jnxProductNameEX8208": jnxProductNameEX8208,
       "jnxProductNameEX8216": jnxProductNameEX8216,
       "jnxProductNameSRX3600": jnxProductNameSRX3600,
       "jnxProductNameSRX3400": jnxProductNameSRX3400,
       "jnxProductNameSRX210": jnxProductNameSRX210,
       "jnxProductNameTXP": jnxProductNameTXP,
       "jnxProductNameJCS": jnxProductNameJCS,
       "jnxProductNameSRX240": jnxProductNameSRX240,
       "jnxProductNameSRX650": jnxProductNameSRX650,
       "jnxProductNameSRX100": jnxProductNameSRX100,
       "jnxProductNameLN1000V": jnxProductNameLN1000V,
       "jnxProductNameEX2200": jnxProductNameEX2200,
       "jnxProductNameEX4500": jnxProductNameEX4500,
       "jnxProductNameFXSeries": jnxProductNameFXSeries,
       "jnxProductNameIBM4274M02J02M": jnxProductNameIBM4274M02J02M,
       "jnxProductNameIBM4274M06J06M": jnxProductNameIBM4274M06J06M,
       "jnxProductNameIBM4274M11J11M": jnxProductNameIBM4274M11J11M,
       "jnxProductNameSRX1400": jnxProductNameSRX1400,
       "jnxProductNameIBM4274S58J58S": jnxProductNameIBM4274S58J58S,
       "jnxProductNameIBM4274S56J56S": jnxProductNameIBM4274S56J56S,
       "jnxProductNameIBM4274S36J36S": jnxProductNameIBM4274S36J36S,
       "jnxProductNameIBM4274S34J34S": jnxProductNameIBM4274S34J34S,
       "jnxProductNameIBM427348EJ48E": jnxProductNameIBM427348EJ48E,
       "jnxProductNameIBM4274E08J08E": jnxProductNameIBM4274E08J08E,
       "jnxProductNameIBM4274E16J16E": jnxProductNameIBM4274E16J16E,
       "jnxProductNameMX80": jnxProductNameMX80,
       "jnxProductNameSRX220": jnxProductNameSRX220,
       "jnxProductNameEXXRE": jnxProductNameEXXRE,
       "jnxProductNameQFXInterconnect": jnxProductNameQFXInterconnect,
       "jnxProductNameQFXNode": jnxProductNameQFXNode,
       "jnxProductNameQFXJVRE": jnxProductNameQFXJVRE,
       "jnxProductNameEX4300": jnxProductNameEX4300,
       "jnxProductNameSRX110": jnxProductNameSRX110,
       "jnxProductNameSRX120": jnxProductNameSRX120,
       "jnxProductNameMAG8600": jnxProductNameMAG8600,
       "jnxProductNameMAG6611": jnxProductNameMAG6611,
       "jnxProductNameMAG6610": jnxProductNameMAG6610,
       "jnxProductNamePTX5000": jnxProductNamePTX5000,
       "jnxProductNameIBM0719J45E": jnxProductNameIBM0719J45E,
       "jnxProductNameIBMJ08F": jnxProductNameIBMJ08F,
       "jnxProductNameIBMJ52F": jnxProductNameIBMJ52F,
       "jnxProductNameEX6210": jnxProductNameEX6210,
       "jnxProductNameDellJFX3500": jnxProductNameDellJFX3500,
       "jnxProductNameEX3300": jnxProductNameEX3300,
       "jnxProductNameDELLJSRX3600": jnxProductNameDELLJSRX3600,
       "jnxProductNameDELLJSRX3400": jnxProductNameDELLJSRX3400,
       "jnxProductNameDELLJSRX1400": jnxProductNameDELLJSRX1400,
       "jnxProductNameDELLJSRX5800": jnxProductNameDELLJSRX5800,
       "jnxProductNameDELLJSRX5600": jnxProductNameDELLJSRX5600,
       "jnxProductNameQFXSwitch": jnxProductNameQFXSwitch,
       "jnxProductNameT4000": jnxProductNameT4000,
       "jnxProductNameQFX3000": jnxProductNameQFX3000,
       "jnxProductNameQFX5000": jnxProductNameQFX5000,
       "jnxProductNameSRX550": jnxProductNameSRX550,
       "jnxProductNameACX": jnxProductNameACX,
       "jnxProductNameMX40": jnxProductNameMX40,
       "jnxProductNameMX10": jnxProductNameMX10,
       "jnxProductNameMX5": jnxProductNameMX5,
       "jnxProductNameQFXMInterconnect": jnxProductNameQFXMInterconnect,
       "jnxProductNameEX4550": jnxProductNameEX4550,
       "jnxProductNameMX2020": jnxProductNameMX2020,
       "jnxProductNameVseries": jnxProductNameVseries,
       "jnxProductNameLN2600": jnxProductNameLN2600,
       "jnxProductNameFireflyPerimeter": jnxProductNameFireflyPerimeter,
       "jnxProductNameMX104": jnxProductNameMX104,
       "jnxProductNamePTX3000": jnxProductNamePTX3000,
       "jnxProductNameMX2010": jnxProductNameMX2010,
       "jnxProductNameQFX3100": jnxProductNameQFX3100,
       "jnxProductNameLN2800": jnxProductNameLN2800,
       "jnxProductNameEX9214": jnxProductNameEX9214,
       "jnxProductNameEX9208": jnxProductNameEX9208,
       "jnxProductNameEX9204": jnxProductNameEX9204,
       "jnxProductNameSRX5400": jnxProductNameSRX5400,
       "jnxProductNameIBM4274S54J54S": jnxProductNameIBM4274S54J54S,
       "jnxProductNameDELLJSRX5400": jnxProductNameDELLJSRX5400,
       "jnxProductNameVMX": jnxProductNameVMX,
       "jnxProductNameEX4600": jnxProductNameEX4600,
       "jnxProductNameVRR": jnxProductNameVRR,
       "jnxProductNameMX10440G": jnxProductNameMX10440G,
       "jnxProductNameOCPAcc": jnxProductNameOCPAcc,
       "jnxProductNameACX1000": jnxProductNameACX1000,
       "jnxProductNameACX2000": jnxProductNameACX2000,
       "jnxProductNameACX1100": jnxProductNameACX1100,
       "jnxProductNameACX2100": jnxProductNameACX2100,
       "jnxProductNameACX2200": jnxProductNameACX2200,
       "jnxProductNameACX4000": jnxProductNameACX4000,
       "jnxProductNameACX500AC": jnxProductNameACX500AC,
       "jnxProductNameACX500DC": jnxProductNameACX500DC,
       "jnxProductNameACX500OAC": jnxProductNameACX500OAC,
       "jnxProductNameACX500ODC": jnxProductNameACX500ODC,
       "jnxProductNameACX500OPOEAC": jnxProductNameACX500OPOEAC,
       "jnxProductNameACX500OPOEDC": jnxProductNameACX500OPOEDC,
       "jnxProductNameSatelliteDevice": jnxProductNameSatelliteDevice,
       "jnxProductNameACX5048": jnxProductNameACX5048,
       "jnxProductNameACX5096": jnxProductNameACX5096,
       "jnxProductNameLN1000CC": jnxProductNameLN1000CC,
       "jnxProductNameVSRX": jnxProductNameVSRX,
       "jnxProductNamePTX1000": jnxProductNamePTX1000,
       "jnxProductNameEX3400": jnxProductNameEX3400,
       "jnxProductNameEX2300": jnxProductNameEX2300,
       "jnxProductNameSRX300": jnxProductNameSRX300,
       "jnxProductNameSRX320": jnxProductNameSRX320,
       "jnxProductNameSRX340": jnxProductNameSRX340,
       "jnxProductNameSRX345": jnxProductNameSRX345,
       "jnxProductNameSRX1500": jnxProductNameSRX1500,
       "jnxProductNameNFX": jnxProductNameNFX,
       "jnxProductNameJNP10003": jnxProductNameJNP10003,
       "jnxProductNameSRX4600": jnxProductNameSRX4600,
       "jnxProductNameSRX4800": jnxProductNameSRX4800,
       "jnxProductNameSRX4100": jnxProductNameSRX4100,
       "jnxProductNameSRX4200": jnxProductNameSRX4200,
       "jnxProductNameJNP204": jnxProductNameJNP204,
       "jnxProductNameMX2008": jnxProductNameMX2008,
       "jnxProductNameMXTSR80": jnxProductNameMXTSR80,
       "jnxProductNamePTX10008": jnxProductNamePTX10008,
       "jnxProductNameACX5448": jnxProductNameACX5448,
       "jnxProductNamePTX10016": jnxProductNamePTX10016,
       "jnxProductNameEX9251": jnxProductNameEX9251,
       "jnxProductNameMX150": jnxProductNameMX150,
       "jnxProductNameJNP10001": jnxProductNameJNP10001,
       "jnxProductNameMX10008": jnxProductNameMX10008,
       "jnxProductNameMX10016": jnxProductNameMX10016,
       "jnxProductNameEX9253": jnxProductNameEX9253,
       "jnxProductNameJRR200": jnxProductNameJRR200,
       "jnxProductNameACX5448M": jnxProductNameACX5448M,
       "jnxProductNameACX5448D": jnxProductNameACX5448D,
       "jnxProductNameACX6360OR": jnxProductNameACX6360OR,
       "jnxProductNameACX6360OX": jnxProductNameACX6360OX,
       "jnxProductNameACX710": jnxProductNameACX710,
       "jnxProductNameACX5800": jnxProductNameACX5800,
       "jnxProductNameSRX380": jnxProductNameSRX380,
       "jnxProductNameEX4400": jnxProductNameEX4400,
       "jnxProductNameR6675": jnxProductNameR6675,
       "jnxProductNameMX304": jnxProductNameMX304,
       "jnxProductNameMX10004": jnxProductNameMX10004,
       "jnxProductNameEX4100": jnxProductNameEX4100,
       "jnxProductNameEX4650": jnxProductNameEX4650,
       "jnxProductNamePTX1000260C": jnxProductNamePTX1000260C,
       "jnxProductNamePTX1000380c": jnxProductNamePTX1000380c,
       "jnxProductNamePTX10003160c": jnxProductNamePTX10003160c,
       "jnxProductNameQFX1000380c": jnxProductNameQFX1000380c,
       "jnxProductNameQFX10003160c": jnxProductNameQFX10003160c,
       "jnxProductNamePTX1000136mr": jnxProductNamePTX1000136mr,
       "jnxProductNamePTX10004": jnxProductNamePTX10004,
       "jnxProductNameACX753": jnxProductNameACX753,
       "jnxProductNameSRX1800": jnxProductNameSRX1800,
       "jnxProductNameACX7KSwitch": jnxProductNameACX7KSwitch,
       "jnxProductNameACX710032c": jnxProductNameACX710032c,
       "jnxProductNameACX710048l": jnxProductNameACX710048l,
       "jnxProductNameACX7908": jnxProductNameACX7908,
       "jnxProductNameACX7024": jnxProductNameACX7024,
       "jnxProductNameSRX1600": jnxProductNameSRX1600,
       "jnxProductNameSRX2300": jnxProductNameSRX2300,
       "jnxProductNameSRX4300": jnxProductNameSRX4300,
       "jnxProductNameACX7332": jnxProductNameACX7332,
       "jnxProductNameACX7348": jnxProductNameACX7348,
       "jnxProductNameACX7024X": jnxProductNameACX7024X,
       "jnxProductNamePTX1000236qdd": jnxProductNamePTX1000236qdd,
       "jnxProductNameSRX4700": jnxProductNameSRX4700,
       "jnxProductModel": jnxProductModel,
       "jnxProductModelM40": jnxProductModelM40,
       "jnxProductModelM20": jnxProductModelM20,
       "jnxProductModelM160": jnxProductModelM160,
       "jnxProductModelM10": jnxProductModelM10,
       "jnxProductModelM5": jnxProductModelM5,
       "jnxProductModelT640": jnxProductModelT640,
       "jnxProductModelT320": jnxProductModelT320,
       "jnxProductModelM40e": jnxProductModelM40e,
       "jnxProductModelM320": jnxProductModelM320,
       "jnxProductModelM7i": jnxProductModelM7i,
       "jnxProductModelM10i": jnxProductModelM10i,
       "jnxProductModelIRM": jnxProductModelIRM,
       "jnxProductModelTX": jnxProductModelTX,
       "jnxProductModelM120": jnxProductModelM120,
       "jnxProductModelMX960": jnxProductModelMX960,
       "jnxProductModelMX480": jnxProductModelMX480,
       "jnxProductModelSRX5800": jnxProductModelSRX5800,
       "jnxProductModelT1600": jnxProductModelT1600,
       "jnxProductModelSRX5600": jnxProductModelSRX5600,
       "jnxProductModelMX240": jnxProductModelMX240,
       "jnxProductModelEX3200": jnxProductModelEX3200,
       "jnxProductModelEX4200": jnxProductModelEX4200,
       "jnxProductModelEX8208": jnxProductModelEX8208,
       "jnxProductModelEX8216": jnxProductModelEX8216,
       "jnxProductModelSRX3600": jnxProductModelSRX3600,
       "jnxProductModelSRX3400": jnxProductModelSRX3400,
       "jnxProductModelTXP": jnxProductModelTXP,
       "jnxProductModelJCS": jnxProductModelJCS,
       "jnxProductModelLN1000V": jnxProductModelLN1000V,
       "jnxProductModelEX2200": jnxProductModelEX2200,
       "jnxProductModelEX4500": jnxProductModelEX4500,
       "jnxProductModelFXSeries": jnxProductModelFXSeries,
       "jnxProductModelIBM4274M02J02M": jnxProductModelIBM4274M02J02M,
       "jnxProductModelIBM4274M06J06M": jnxProductModelIBM4274M06J06M,
       "jnxProductModelIBM4274M11J11M": jnxProductModelIBM4274M11J11M,
       "jnxProductModelSRX1400": jnxProductModelSRX1400,
       "jnxProductModelIBM4274S58J58S": jnxProductModelIBM4274S58J58S,
       "jnxProductModelIBM4274S56J56S": jnxProductModelIBM4274S56J56S,
       "jnxProductModelIBM4274S36J36S": jnxProductModelIBM4274S36J36S,
       "jnxProductModelIBM4274S34J34S": jnxProductModelIBM4274S34J34S,
       "jnxProductModelIBM427348EJ48E": jnxProductModelIBM427348EJ48E,
       "jnxProductModelIBM4274E08J08E": jnxProductModelIBM4274E08J08E,
       "jnxProductModelIBM4274E16J16E": jnxProductModelIBM4274E16J16E,
       "jnxProductModelMX80": jnxProductModelMX80,
       "jnxProductModelEXXRE": jnxProductModelEXXRE,
       "jnxProductModelQFXInterconnect": jnxProductModelQFXInterconnect,
       "jnxProductModelQFXNode": jnxProductModelQFXNode,
       "jnxProductModelQFXJVRE": jnxProductModelQFXJVRE,
       "jnxProductModelEX4300": jnxProductModelEX4300,
       "jnxProductModelMAG8600": jnxProductModelMAG8600,
       "jnxProductModelMAG6611": jnxProductModelMAG6611,
       "jnxProductModelMAG6610": jnxProductModelMAG6610,
       "jnxProductModelPTX5000": jnxProductModelPTX5000,
       "jnxProductModelIBM0719J45E": jnxProductModelIBM0719J45E,
       "jnxProductModelIBMJ08F": jnxProductModelIBMJ08F,
       "jnxProductModelIBMJ52F": jnxProductModelIBMJ52F,
       "jnxProductModelEX6210": jnxProductModelEX6210,
       "jnxProductModelDellJFX3500": jnxProductModelDellJFX3500,
       "jnxProductModelEX3300": jnxProductModelEX3300,
       "jnxProductModelDELLJSRX3600": jnxProductModelDELLJSRX3600,
       "jnxProductModelDELLJSRX3400": jnxProductModelDELLJSRX3400,
       "jnxProductModelDELLJSRX1400": jnxProductModelDELLJSRX1400,
       "jnxProductModelDELLJSRX5800": jnxProductModelDELLJSRX5800,
       "jnxProductModelDELLJSRX5600": jnxProductModelDELLJSRX5600,
       "jnxProductModelQFXSwitch": jnxProductModelQFXSwitch,
       "jnxProductModelT4000": jnxProductModelT4000,
       "jnxProductModelQFX3000": jnxProductModelQFX3000,
       "jnxProductModelQFX5000": jnxProductModelQFX5000,
       "jnxProductModelACX": jnxProductModelACX,
       "jnxProductModelMX40": jnxProductModelMX40,
       "jnxProductModelMX10": jnxProductModelMX10,
       "jnxProductModelMX5": jnxProductModelMX5,
       "jnxProductModelQFXMInterconnect": jnxProductModelQFXMInterconnect,
       "jnxProductModelEX4550": jnxProductModelEX4550,
       "jnxProductModelMX2020": jnxProductModelMX2020,
       "jnxProductModelLN2600": jnxProductModelLN2600,
       "jnxProductModelMX104": jnxProductModelMX104,
       "jnxProductModelPTX3000": jnxProductModelPTX3000,
       "jnxProductModelMX2010": jnxProductModelMX2010,
       "jnxProductModelQFX3100": jnxProductModelQFX3100,
       "jnxProductModelEX9214": jnxProductModelEX9214,
       "jnxProductModelEX9208": jnxProductModelEX9208,
       "jnxProductModelEX9204": jnxProductModelEX9204,
       "jnxProductModelSRX5400": jnxProductModelSRX5400,
       "jnxProductModelIBM4274S54J54S": jnxProductModelIBM4274S54J54S,
       "jnxProductModelDELLJSRX5400": jnxProductModelDELLJSRX5400,
       "jnxProductModelVMX": jnxProductModelVMX,
       "jnxProductModelEX4600": jnxProductModelEX4600,
       "jnxProductModelVRR": jnxProductModelVRR,
       "jnxProductModelOCPAcc": jnxProductModelOCPAcc,
       "jnxProductModelACX1000": jnxProductModelACX1000,
       "jnxProductModelACX2000": jnxProductModelACX2000,
       "jnxProductModelACX1100": jnxProductModelACX1100,
       "jnxProductModelACX2100": jnxProductModelACX2100,
       "jnxProductModelACX2200": jnxProductModelACX2200,
       "jnxProductModelACX4000": jnxProductModelACX4000,
       "jnxProductModelACX500AC": jnxProductModelACX500AC,
       "jnxProductModelACX500DC": jnxProductModelACX500DC,
       "jnxProductModelACX500OAC": jnxProductModelACX500OAC,
       "jnxProductModelACX500ODC": jnxProductModelACX500ODC,
       "jnxProductModelACX500OPOEAC": jnxProductModelACX500OPOEAC,
       "jnxProductModelACX500OPOEDC": jnxProductModelACX500OPOEDC,
       "jnxProductModelSatelliteDevice": jnxProductModelSatelliteDevice,
       "jnxProductModelACX5048": jnxProductModelACX5048,
       "jnxProductModelACX5096": jnxProductModelACX5096,
       "jnxProductModelLN1000CC": jnxProductModelLN1000CC,
       "jnxProductModelPTX1000": jnxProductModelPTX1000,
       "jnxProductModelEX3400": jnxProductModelEX3400,
       "jnxProductModelEX2300": jnxProductModelEX2300,
       "jnxProductModelNFX": jnxProductModelNFX,
       "jnxProductModelJNP10003": jnxProductModelJNP10003,
       "jnxProductModelSRX4600": jnxProductModelSRX4600,
       "jnxProductModelSRX4800": jnxProductModelSRX4800,
       "jnxProductModelJNP204": jnxProductModelJNP204,
       "jnxProductModelMX2008": jnxProductModelMX2008,
       "jnxProductModelMXTSR80": jnxProductModelMXTSR80,
       "jnxProductModelPTX10008": jnxProductModelPTX10008,
       "jnxProductModelACX5448": jnxProductModelACX5448,
       "jnxProductModelPTX10016": jnxProductModelPTX10016,
       "jnxProductModelEX9251": jnxProductModelEX9251,
       "jnxProductModelMX150": jnxProductModelMX150,
       "jnxProductModelJNP10001": jnxProductModelJNP10001,
       "jnxProductModelMX10008": jnxProductModelMX10008,
       "jnxProductModelMX10016": jnxProductModelMX10016,
       "jnxProductModelEX9253": jnxProductModelEX9253,
       "jnxProductModelACX5448M": jnxProductModelACX5448M,
       "jnxProductModelACX5448D": jnxProductModelACX5448D,
       "jnxProductModelACX6360OR": jnxProductModelACX6360OR,
       "jnxProductModelACX6360OX": jnxProductModelACX6360OX,
       "jnxProductModelACX710": jnxProductModelACX710,
       "jnxProductModelACX5800": jnxProductModelACX5800,
       "jnxProductModelEX4400": jnxProductModelEX4400,
       "jnxProductModelR6675": jnxProductModelR6675,
       "jnxProductModelMX304": jnxProductModelMX304,
       "jnxProductModelMX10004": jnxProductModelMX10004,
       "jnxProductModelEX4100": jnxProductModelEX4100,
       "jnxProductModelEX4650": jnxProductModelEX4650,
       "jnxProductModelPTX1000260C": jnxProductModelPTX1000260C,
       "jnxProductModelPTX1000380c": jnxProductModelPTX1000380c,
       "jnxProductModelPTX10003160c": jnxProductModelPTX10003160c,
       "jnxProductModelQFX1000380c": jnxProductModelQFX1000380c,
       "jnxProductModelQFX10003160c": jnxProductModelQFX10003160c,
       "jnxProductModelPTX1000136mr": jnxProductModelPTX1000136mr,
       "jnxProductModelPTX10004": jnxProductModelPTX10004,
       "jnxProductModelACX753": jnxProductModelACX753,
       "jnxProductModelSRX1800": jnxProductModelSRX1800,
       "jnxProductModelACX7KSwitch": jnxProductModelACX7KSwitch,
       "jnxProductModelACX710032c": jnxProductModelACX710032c,
       "jnxProductModelACX710048l": jnxProductModelACX710048l,
       "jnxProductModelACX7908": jnxProductModelACX7908,
       "jnxProductModelACX7024": jnxProductModelACX7024,
       "jnxProductModelACX7332": jnxProductModelACX7332,
       "jnxProductModelACX7348": jnxProductModelACX7348,
       "jnxProductModelACX7024X": jnxProductModelACX7024X,
       "jnxProductModelPTX1000236qdd": jnxProductModelPTX1000236qdd,
       "jnxProductVariation": jnxProductVariation,
       "jnxProductVariationM40": jnxProductVariationM40,
       "jnxProductVariationM20": jnxProductVariationM20,
       "jnxProductVariationM160": jnxProductVariationM160,
       "jnxProductVariationM10": jnxProductVariationM10,
       "jnxProductVariationM5": jnxProductVariationM5,
       "jnxProductVariationT640": jnxProductVariationT640,
       "jnxProductVariationT320": jnxProductVariationT320,
       "jnxProductVariationM40e": jnxProductVariationM40e,
       "jnxProductVariationM320": jnxProductVariationM320,
       "jnxProductVariationM7i": jnxProductVariationM7i,
       "jnxProductVariationM10i": jnxProductVariationM10i,
       "jnxProductVariationIRM": jnxProductVariationIRM,
       "jnxProductVariationTX": jnxProductVariationTX,
       "jnxProductVariationM120": jnxProductVariationM120,
       "jnxProductVariationMX960": jnxProductVariationMX960,
       "jnxProductVariationMX480": jnxProductVariationMX480,
       "jnxProductVariationSRX5800": jnxProductVariationSRX5800,
       "jnxProductVariationT1600": jnxProductVariationT1600,
       "jnxProductVariationSRX5600": jnxProductVariationSRX5600,
       "jnxProductVariationMX240": jnxProductVariationMX240,
       "jnxProductVariationEX3200": jnxProductVariationEX3200,
       "jnxProductEX3200port24T": jnxProductEX3200port24T,
       "jnxProductEX3200port24P": jnxProductEX3200port24P,
       "jnxProductEX3200port48T": jnxProductEX3200port48T,
       "jnxProductEX3200port48P": jnxProductEX3200port48P,
       "jnxProductVariationEX4200": jnxProductVariationEX4200,
       "jnxProductEX4200port24T": jnxProductEX4200port24T,
       "jnxProductEX4200port24P": jnxProductEX4200port24P,
       "jnxProductEX4200port48T": jnxProductEX4200port48T,
       "jnxProductEX4200port48P": jnxProductEX4200port48P,
       "jnxProductEX4200port24F": jnxProductEX4200port24F,
       "jnxProductEX4200port24PX": jnxProductEX4200port24PX,
       "jnxProductEX4200port48PX": jnxProductEX4200port48PX,
       "jnxProductVariationEX8208": jnxProductVariationEX8208,
       "jnxProductVariationEX8216": jnxProductVariationEX8216,
       "jnxProductVariationSRX3600": jnxProductVariationSRX3600,
       "jnxProductVariationSRX3400": jnxProductVariationSRX3400,
       "jnxProductVariationTXP": jnxProductVariationTXP,
       "jnxProductVariationJCS": jnxProductVariationJCS,
       "jnxProductVariationLN1000V": jnxProductVariationLN1000V,
       "jnxProductVariationEX2200": jnxProductVariationEX2200,
       "jnxProductEX2200port24T": jnxProductEX2200port24T,
       "jnxProductEX2200port24P": jnxProductEX2200port24P,
       "jnxProductEX2200port48T": jnxProductEX2200port48T,
       "jnxProductEX2200port48P": jnxProductEX2200port48P,
       "jnxProductEX2200Cport12T": jnxProductEX2200Cport12T,
       "jnxProductEX2200Cport12P": jnxProductEX2200Cport12P,
       "jnxProductEX2200port24TDC": jnxProductEX2200port24TDC,
       "jnxProductVariationEX4500": jnxProductVariationEX4500,
       "jnxProductEX4500port40F": jnxProductEX4500port40F,
       "jnxProductEX4500port20F": jnxProductEX4500port20F,
       "jnxProductVariationFXSeries": jnxProductVariationFXSeries,
       "jnxProductFX1600port": jnxProductFX1600port,
       "jnxProductFX2160port": jnxProductFX2160port,
       "jnxProductVariationIBM4274M02J02M": jnxProductVariationIBM4274M02J02M,
       "jnxProductVariationIBM4274M06J06M": jnxProductVariationIBM4274M06J06M,
       "jnxProductVariationIBM4274M11J11M": jnxProductVariationIBM4274M11J11M,
       "jnxProductVariationSRX1400": jnxProductVariationSRX1400,
       "jnxProductVariationIBM4274S58J58S": jnxProductVariationIBM4274S58J58S,
       "jnxProductVariationIBM4274S56J56S": jnxProductVariationIBM4274S56J56S,
       "jnxProductVariationIBM4274S36J36S": jnxProductVariationIBM4274S36J36S,
       "jnxProductVariationIBM4274S34J34S": jnxProductVariationIBM4274S34J34S,
       "jnxProductVariationIBM427348EJ48E": jnxProductVariationIBM427348EJ48E,
       "jnxProductIBM427348EJ48Eport24T": jnxProductIBM427348EJ48Eport24T,
       "jnxProductIBM427348EJ48Eport24P": jnxProductIBM427348EJ48Eport24P,
       "jnxProductIBM427348EJ48Eport48T": jnxProductIBM427348EJ48Eport48T,
       "jnxProductIBM427348EJ48Eport48P": jnxProductIBM427348EJ48Eport48P,
       "jnxProductIBM427348EJ48Eport24F": jnxProductIBM427348EJ48Eport24F,
       "jnxProductVariationIBM4274E08J08E": jnxProductVariationIBM4274E08J08E,
       "jnxProductVariationIBM4274E16J16E": jnxProductVariationIBM4274E16J16E,
       "jnxProductVariationMX80": jnxProductVariationMX80,
       "jnxProductMX80": jnxProductMX80,
       "jnxProductMX80-48T": jnxProductMX80_48T,
       "jnxProductMX80-T": jnxProductMX80_T,
       "jnxProductMX80-P": jnxProductMX80_P,
       "jnxProductVariationEXXRE": jnxProductVariationEXXRE,
       "jnxProductEXXRE": jnxProductEXXRE,
       "jnxProductVariationQFXInterconnect": jnxProductVariationQFXInterconnect,
       "jnxProductQFX3008": jnxProductQFX3008,
       "jnxProductQFXC083008": jnxProductQFXC083008,
       "jnxProductQFX3008I": jnxProductQFX3008I,
       "jnxProductVariationQFXNode": jnxProductVariationQFXNode,
       "jnxProductQFX3500": jnxProductQFX3500,
       "jnxProductQFX5500": jnxProductQFX5500,
       "jnxProductQFX360016Q": jnxProductQFX360016Q,
       "jnxProductQFX350048T4Q": jnxProductQFX350048T4Q,
       "jnxProductQFX510024QF": jnxProductQFX510024QF,
       "jnxProductQFX510048S6QF": jnxProductQFX510048S6QF,
       "jnxProductQFX510096S6QF": jnxProductQFX510096S6QF,
       "jnxProductQFX510048C6QF": jnxProductQFX510048C6QF,
       "jnxProductVariationEX4300": jnxProductVariationEX4300,
       "jnxProductEX4300port24T": jnxProductEX4300port24T,
       "jnxProductEX4300port48T": jnxProductEX4300port48T,
       "jnxProductEX4300port48TBF": jnxProductEX4300port48TBF,
       "jnxProductEX4300port48TDC": jnxProductEX4300port48TDC,
       "jnxProductEX4300port48TDCBF": jnxProductEX4300port48TDCBF,
       "jnxProductEX4300port24P": jnxProductEX4300port24P,
       "jnxProductEX4300port48P": jnxProductEX4300port48P,
       "jnxProductEX4300port32F": jnxProductEX4300port32F,
       "jnxProductEX4300port48MP": jnxProductEX4300port48MP,
       "jnxProductVariationMAG8600": jnxProductVariationMAG8600,
       "jnxProductVariationMAG6611": jnxProductVariationMAG6611,
       "jnxProductVariationMAG6610": jnxProductVariationMAG6610,
       "jnxProductVariationPTX5000": jnxProductVariationPTX5000,
       "jnxProductVariationIBM0719J45E": jnxProductVariationIBM0719J45E,
       "jnxProductIBM0719J45Eport40F": jnxProductIBM0719J45Eport40F,
       "jnxProductIBM0719J45Eport20F": jnxProductIBM0719J45Eport20F,
       "jnxProductVariationIBMJ08F": jnxProductVariationIBMJ08F,
       "jnxProductIBM2413F08J08F": jnxProductIBM2413F08J08F,
       "jnxProductVariationIBMJ52F": jnxProductVariationIBMJ52F,
       "jnxProductIBM2409F52J52F": jnxProductIBM2409F52J52F,
       "jnxProductIBM8729HC1J52F": jnxProductIBM8729HC1J52F,
       "jnxProductVariationEX6210": jnxProductVariationEX6210,
       "jnxProductVariationDellJFX3500": jnxProductVariationDellJFX3500,
       "jnxProductVariationEX3300": jnxProductVariationEX3300,
       "jnxProductEX3300port24T": jnxProductEX3300port24T,
       "jnxProductEX3300port24P": jnxProductEX3300port24P,
       "jnxProductEX3300port48T": jnxProductEX3300port48T,
       "jnxProductEX3300port48P": jnxProductEX3300port48P,
       "jnxProductEX3300port24TDC": jnxProductEX3300port24TDC,
       "jnxProductEX3300port48TBF": jnxProductEX3300port48TBF,
       "jnxProductVariationDELLJSRX3600": jnxProductVariationDELLJSRX3600,
       "jnxProductVariationDELLJSRX3400": jnxProductVariationDELLJSRX3400,
       "jnxProductVariationDELLJSRX1400": jnxProductVariationDELLJSRX1400,
       "jnxProductVariationDELLJSRX5800": jnxProductVariationDELLJSRX5800,
       "jnxProductVariationDELLJSRX5600": jnxProductVariationDELLJSRX5600,
       "jnxProductVariationQFXSwitch": jnxProductVariationQFXSwitch,
       "jnxProductQFX3500s": jnxProductQFX3500s,
       "jnxProductQFX360016QS": jnxProductQFX360016QS,
       "jnxProductQFX350048T4QS": jnxProductQFX350048T4QS,
       "jnxProductQFX510024Q": jnxProductQFX510024Q,
       "jnxProductQFX510048S6Q": jnxProductQFX510048S6Q,
       "jnxProductQFX510096S8Q": jnxProductQFX510096S8Q,
       "jnxProductQFX510048C6Q": jnxProductQFX510048C6Q,
       "jnxProductQFX510024QHP": jnxProductQFX510024QHP,
       "jnxProductQFX510048T6Q": jnxProductQFX510048T6Q,
       "jnxProductQFX1000236Q": jnxProductQFX1000236Q,
       "jnxProductQFX1000272Q": jnxProductQFX1000272Q,
       "jnxProductQFX10004": jnxProductQFX10004,
       "jnxProductQFX10008": jnxProductQFX10008,
       "jnxProductQFX10016": jnxProductQFX10016,
       "jnxProductQFX520032C32Q": jnxProductQFX520032C32Q,
       "jnxProductQFX520032C64Q": jnxProductQFX520032C64Q,
       "jnxProductQFX511048S4C": jnxProductQFX511048S4C,
       "jnxProductQFX511032Q": jnxProductQFX511032Q,
       "jnxProductNameQFX1000260C": jnxProductNameQFX1000260C,
       "jnxProductQFX521064C": jnxProductQFX521064C,
       "jnxProductQFX520048Y": jnxProductQFX520048Y,
       "jnxProductQFX512048Y8C": jnxProductQFX512048Y8C,
       "jnxProductAS781664X": jnxProductAS781664X,
       "jnxProductQFX512032C": jnxProductQFX512032C,
       "jnxProductQFX522032CD": jnxProductQFX522032CD,
       "jnxProductQFX5220128C": jnxProductQFX5220128C,
       "jnxProductQFX512048T6C": jnxProductQFX512048T6C,
       "jnxProductQFX513032CD": jnxProductQFX513032CD,
       "jnxProductQFX513048C": jnxProductQFX513048C,
       "jnxProductQFX512048YM8C": jnxProductQFX512048YM8C,
       "jnxProductQFX5700": jnxProductQFX5700,
       "jnxProductQFX523064CD": jnxProductQFX523064CD,
       "jnxProductQFX5130E32CD": jnxProductQFX5130E32CD,
       "jnxProductQFX524064OSFP": jnxProductQFX524064OSFP,
       "jnxProductQFX524064QSFPDD": jnxProductQFX524064QSFPDD,
       "jnxProductVariationT4000": jnxProductVariationT4000,
       "jnxProductVariationQFX3000": jnxProductVariationQFX3000,
       "jnxProductQFX3000-G": jnxProductQFX3000_G,
       "jnxProductQFX3000-M": jnxProductQFX3000_M,
       "jnxProductVariationQFX5000": jnxProductVariationQFX5000,
       "jnxProductVariationACX": jnxProductVariationACX,
       "jnxProductACX500IDC": jnxProductACX500IDC,
       "jnxProductACX500IAC": jnxProductACX500IAC,
       "jnxProductVariationMX40": jnxProductVariationMX40,
       "jnxProductMX40": jnxProductMX40,
       "jnxProductVariationMX10": jnxProductVariationMX10,
       "jnxProductMX10": jnxProductMX10,
       "jnxProductVariationMX5": jnxProductVariationMX5,
       "jnxProductMX5": jnxProductMX5,
       "jnxProductVariationQFXMInterconnect": jnxProductVariationQFXMInterconnect,
       "jnxProductQFX3600I": jnxProductQFX3600I,
       "jnxProductQFX510024QI": jnxProductQFX510024QI,
       "jnxProductVariationEX4550": jnxProductVariationEX4550,
       "jnxProductEX4550port32F": jnxProductEX4550port32F,
       "jnxProductEX4550port32T": jnxProductEX4550port32T,
       "jnxProductVariationMX2020": jnxProductVariationMX2020,
       "jnxProductVariationLN2600": jnxProductVariationLN2600,
       "jnxProductVariationMX104": jnxProductVariationMX104,
       "jnxProductMX104": jnxProductMX104,
       "jnxProductVariationPTX3000": jnxProductVariationPTX3000,
       "jnxProductVariationMX2010": jnxProductVariationMX2010,
       "jnxProductVariationQFX3100": jnxProductVariationQFX3100,
       "jnxProductVariationEX9214": jnxProductVariationEX9214,
       "jnxProductVariationEX9208": jnxProductVariationEX9208,
       "jnxProductVariationEX9204": jnxProductVariationEX9204,
       "jnxProductVariationSRX5400": jnxProductVariationSRX5400,
       "jnxProductVariationIBM4274S54J54S": jnxProductVariationIBM4274S54J54S,
       "jnxProductVariationDELLJSRX5400": jnxProductVariationDELLJSRX5400,
       "jnxProductVariationEX4600": jnxProductVariationEX4600,
       "jnxProductEX4600": jnxProductEX4600,
       "jnxProductVariationOCPAcc": jnxProductVariationOCPAcc,
       "jnxProductOCP48S": jnxProductOCP48S,
       "jnxProductOCP48T": jnxProductOCP48T,
       "jnxProductVariationACX1000": jnxProductVariationACX1000,
       "jnxProductACX1000": jnxProductACX1000,
       "jnxProductVariationACX2000": jnxProductVariationACX2000,
       "jnxProductACX2000": jnxProductACX2000,
       "jnxProductVariationACX1100": jnxProductVariationACX1100,
       "jnxProductACX1100": jnxProductACX1100,
       "jnxProductVariationACX2100": jnxProductVariationACX2100,
       "jnxProductACX2100": jnxProductACX2100,
       "jnxProductVariationACX2200": jnxProductVariationACX2200,
       "jnxProductACX2200": jnxProductACX2200,
       "jnxProductVariationACX4000": jnxProductVariationACX4000,
       "jnxProductACX4000": jnxProductACX4000,
       "jnxProductVariationACX500AC": jnxProductVariationACX500AC,
       "jnxProductACX500AC": jnxProductACX500AC,
       "jnxProductVariationACX500DC": jnxProductVariationACX500DC,
       "jnxProductACX500DC": jnxProductACX500DC,
       "jnxProductVariationACX500OAC": jnxProductVariationACX500OAC,
       "jnxProductACX500OAC": jnxProductACX500OAC,
       "jnxProductVariationACX500ODC": jnxProductVariationACX500ODC,
       "jnxProductACX500ODC": jnxProductACX500ODC,
       "jnxProductVariationACX500OPOEAC": jnxProductVariationACX500OPOEAC,
       "jnxProductACX500OPOEAC": jnxProductACX500OPOEAC,
       "jnxProductVariationACX500OPOEDC": jnxProductVariationACX500OPOEDC,
       "jnxProductACX500OPOEDC": jnxProductACX500OPOEDC,
       "jnxProductVariationACX5048": jnxProductVariationACX5048,
       "jnxProductACX5048": jnxProductACX5048,
       "jnxProductVariationACX5096": jnxProductVariationACX5096,
       "jnxProductACX5096": jnxProductACX5096,
       "jnxProductVariationLN1000CC": jnxProductVariationLN1000CC,
       "jnxProductVariationPTX1000": jnxProductVariationPTX1000,
       "jnxProductVariationEX3400": jnxProductVariationEX3400,
       "jnxProductEX3400port24T": jnxProductEX3400port24T,
       "jnxProductEX3400port48T": jnxProductEX3400port48T,
       "jnxProductEX3400port24P": jnxProductEX3400port24P,
       "jnxProductEX3400port48P": jnxProductEX3400port48P,
       "jnxProductVariationEX2300": jnxProductVariationEX2300,
       "jnxProductEX2300port24T": jnxProductEX2300port24T,
       "jnxProductEX2300port48T": jnxProductEX2300port48T,
       "jnxProductEX2300port24P": jnxProductEX2300port24P,
       "jnxProductEX2300port48P": jnxProductEX2300port48P,
       "jnxProductEX2300Cport12T": jnxProductEX2300Cport12T,
       "jnxProductEX2300Cport12P": jnxProductEX2300Cport12P,
       "jnxProductEX2300port24MP": jnxProductEX2300port24MP,
       "jnxProductEX2300port48MP": jnxProductEX2300port48MP,
       "jnxProductVariationNFX": jnxProductVariationNFX,
       "jnxProductNFX250ATTS1": jnxProductNFX250ATTS1,
       "jnxProductNFX250ATTS1SCHost": jnxProductNFX250ATTS1SCHost,
       "jnxProductNFX250ATTS1SCJdm": jnxProductNFX250ATTS1SCJdm,
       "jnxProductNFX250ATTS1SCJcp": jnxProductNFX250ATTS1SCJcp,
       "jnxProductNFX250ATTS2": jnxProductNFX250ATTS2,
       "jnxProductNFX250ATTS2SCHost": jnxProductNFX250ATTS2SCHost,
       "jnxProductNFX250ATTS2SCJdm": jnxProductNFX250ATTS2SCJdm,
       "jnxProductNFX250ATTS2SCJcp": jnxProductNFX250ATTS2SCJcp,
       "jnxProductNFX250ATTLS1": jnxProductNFX250ATTLS1,
       "jnxProductNFX250ATTLS1SCHost": jnxProductNFX250ATTLS1SCHost,
       "jnxProductNFX250ATTLS1SCJdm": jnxProductNFX250ATTLS1SCJdm,
       "jnxProductNFX250ATTLS1SCJcp": jnxProductNFX250ATTLS1SCJcp,
       "jnxProductNFX250S1": jnxProductNFX250S1,
       "jnxProductNFX250S1SCHost": jnxProductNFX250S1SCHost,
       "jnxProductNFX250S1SCJdm": jnxProductNFX250S1SCJdm,
       "jnxProductNFX250S1SCJcp": jnxProductNFX250S1SCJcp,
       "jnxProductNFX250S2": jnxProductNFX250S2,
       "jnxProductNFX250S2SCHost": jnxProductNFX250S2SCHost,
       "jnxProductNFX250S2SCJdm": jnxProductNFX250S2SCJdm,
       "jnxProductNFX250S2SCJcp": jnxProductNFX250S2SCJcp,
       "jnxProductNFX250LS1": jnxProductNFX250LS1,
       "jnxProductNFX250LS1SCHost": jnxProductNFX250LS1SCHost,
       "jnxProductNFX250LS1SCJdm": jnxProductNFX250LS1SCJdm,
       "jnxProductNFX250LS1SCJcp": jnxProductNFX250LS1SCJcp,
       "jnxProductNFXVirtual": jnxProductNFXVirtual,
       "jnxProductNFXVirtualSCHost": jnxProductNFXVirtualSCHost,
       "jnxProductNFXVirtualSCJdm": jnxProductNFXVirtualSCJdm,
       "jnxProductNFXVirtualSCJcp": jnxProductNFXVirtualSCJcp,
       "jnxProductNFX250S1E": jnxProductNFX250S1E,
       "jnxProductNFX250S1ESCHost": jnxProductNFX250S1ESCHost,
       "jnxProductNFX250S1ESCJdm": jnxProductNFX250S1ESCJdm,
       "jnxProductNFX250S1ESCJcp": jnxProductNFX250S1ESCJcp,
       "jnxProductNFX150CS1": jnxProductNFX150CS1,
       "jnxProductNFX150CS1AE": jnxProductNFX150CS1AE,
       "jnxProductNFX150CS1AA": jnxProductNFX150CS1AA,
       "jnxProductNFX150S1": jnxProductNFX150S1,
       "jnxProductNFX350S1": jnxProductNFX350S1,
       "jnxProductNFXWhiteBox1": jnxProductNFXWhiteBox1,
       "jnxProductNFX150CS1EAE": jnxProductNFX150CS1EAE,
       "jnxProductNFX150CS1EAA": jnxProductNFX150CS1EAA,
       "jnxProductNFX150S1E": jnxProductNFX150S1E,
       "jnxProductNFX350S2": jnxProductNFX350S2,
       "jnxProductNFX350S3": jnxProductNFX350S3,
       "jnxProductNFXOPAL": jnxProductNFXOPAL,
       "jnxProductNFX350X": jnxProductNFX350X,
       "jnxProductVariationJNP10003": jnxProductVariationJNP10003,
       "jnxProductVariationSRX4600": jnxProductVariationSRX4600,
       "jnxProductVariationSRX4800": jnxProductVariationSRX4800,
       "jnxProductVariationJNP204": jnxProductVariationJNP204,
       "jnxProductVariationMX2008": jnxProductVariationMX2008,
       "jnxProductVariationMXTSR80": jnxProductVariationMXTSR80,
       "jnxProductMXTSR80": jnxProductMXTSR80,
       "jnxProductVariationPTX10008": jnxProductVariationPTX10008,
       "jnxProductVariationACX5448": jnxProductVariationACX5448,
       "jnxProductACX5448": jnxProductACX5448,
       "jnxProductVariationPTX10016": jnxProductVariationPTX10016,
       "jnxProductVariationEX9251": jnxProductVariationEX9251,
       "jnxProductVariationJNP10001": jnxProductVariationJNP10001,
       "jnxProductVariationMX10008": jnxProductVariationMX10008,
       "jnxProductVariationMX10016": jnxProductVariationMX10016,
       "jnxProductVariationEX9253": jnxProductVariationEX9253,
       "jnxProductVariationACX5448M": jnxProductVariationACX5448M,
       "jnxProductACX5448M": jnxProductACX5448M,
       "jnxProductVariationACX5448D": jnxProductVariationACX5448D,
       "jnxProductACX5448D": jnxProductACX5448D,
       "jnxProductVariationACX6360OR": jnxProductVariationACX6360OR,
       "jnxProductVariationACX6360OX": jnxProductVariationACX6360OX,
       "jnxProductVariationACX710": jnxProductVariationACX710,
       "jnxProductACX710": jnxProductACX710,
       "jnxProductVariationACX5800": jnxProductVariationACX5800,
       "jnxProductACX5800": jnxProductACX5800,
       "jnxProductVariationEX4400": jnxProductVariationEX4400,
       "jnxProductEX4400port48MP": jnxProductEX4400port48MP,
       "jnxProductEX4400port24MP": jnxProductEX4400port24MP,
       "jnxProductEX4400port48P": jnxProductEX4400port48P,
       "jnxProductEX4400port24P": jnxProductEX4400port24P,
       "jnxProductEX4400port48T": jnxProductEX4400port48T,
       "jnxProductEX4400port24T": jnxProductEX4400port24T,
       "jnxProductEX4400port48F": jnxProductEX4400port48F,
       "jnxProductEX4400port24X": jnxProductEX4400port24X,
       "jnxProductVariationR6675": jnxProductVariationR6675,
       "jnxProductR6675": jnxProductR6675,
       "jnxProductVariationMX304": jnxProductVariationMX304,
       "jnxProductVariationMX10004": jnxProductVariationMX10004,
       "jnxProductVariationEX4100": jnxProductVariationEX4100,
       "jnxProductEX4100port48MP": jnxProductEX4100port48MP,
       "jnxProductEX4100port24MP": jnxProductEX4100port24MP,
       "jnxProductEX4100port48P": jnxProductEX4100port48P,
       "jnxProductEX4100port24P": jnxProductEX4100port24P,
       "jnxProductEX4100port48T": jnxProductEX4100port48T,
       "jnxProductEX4100port24T": jnxProductEX4100port24T,
       "jnxProductEX4100portF48P": jnxProductEX4100portF48P,
       "jnxProductEX4100portF24P": jnxProductEX4100portF24P,
       "jnxProductEX4100portF48T": jnxProductEX4100portF48T,
       "jnxProductEX4100portF24T": jnxProductEX4100portF24T,
       "jnxProductEX4100portF12P": jnxProductEX4100portF12P,
       "jnxProductEX4100portF12T": jnxProductEX4100portF12T,
       "jnxProductEX4100portH12MP": jnxProductEX4100portH12MP,
       "jnxProductEX4100portH24MP": jnxProductEX4100portH24MP,
       "jnxProductEX4100portH24F": jnxProductEX4100portH24F,
       "jnxProductVariationEX4650": jnxProductVariationEX4650,
       "jnxProductEX465048Y8C": jnxProductEX465048Y8C,
       "jnxProductVariationPTX1000260C": jnxProductVariationPTX1000260C,
       "jnxProductVariationPTX1000380c": jnxProductVariationPTX1000380c,
       "jnxProductVariationPTX10003160c": jnxProductVariationPTX10003160c,
       "jnxProductVariationQFX1000380c": jnxProductVariationQFX1000380c,
       "jnxProductVariationQFX10003160c": jnxProductVariationQFX10003160c,
       "jnxProductVariationPTX1000136mr": jnxProductVariationPTX1000136mr,
       "jnxProductVariationPTX10004": jnxProductVariationPTX10004,
       "jnxProductVariationACX753": jnxProductVariationACX753,
       "jnxProductVariationACX7KSwitch": jnxProductVariationACX7KSwitch,
       "jnxProductACX710032C": jnxProductACX710032C,
       "jnxProductACX710048L": jnxProductACX710048L,
       "jnxProductACX7509": jnxProductACX7509,
       "jnxProductVariationACX710032c": jnxProductVariationACX710032c,
       "jnxProductVariationACX710048l": jnxProductVariationACX710048l,
       "jnxProductVariationACX7908": jnxProductVariationACX7908,
       "jnxProductVariationACX7024": jnxProductVariationACX7024,
       "jnxProductVariationACX7332": jnxProductVariationACX7332,
       "jnxProductVariationACX7348": jnxProductVariationACX7348,
       "jnxProductVariationACX7024X": jnxProductVariationACX7024X,
       "jnxProductVariationPTX1000236qdd": jnxProductVariationPTX1000236qdd,
       "jnxClassContainers": jnxClassContainers,
       "jnxChassis": jnxChassis,
       "jnxChassisM40": jnxChassisM40,
       "jnxChassisM20": jnxChassisM20,
       "jnxChassisM160": jnxChassisM160,
       "jnxChassisM10": jnxChassisM10,
       "jnxChassisM5": jnxChassisM5,
       "jnxChassisT640": jnxChassisT640,
       "jnxChassisT320": jnxChassisT320,
       "jnxChassisM40e": jnxChassisM40e,
       "jnxChassisM320": jnxChassisM320,
       "jnxChassisM7i": jnxChassisM7i,
       "jnxChassisM10i": jnxChassisM10i,
       "jnxChassisJ2300": jnxChassisJ2300,
       "jnxChassisJ4300": jnxChassisJ4300,
       "jnxChassisJ6300": jnxChassisJ6300,
       "jnxChassisIRM": jnxChassisIRM,
       "jnxChassisTX": jnxChassisTX,
       "jnxChassisM120": jnxChassisM120,
       "jnxChassisJ4350": jnxChassisJ4350,
       "jnxChassisJ6350": jnxChassisJ6350,
       "jnxChassisMX960": jnxChassisMX960,
       "jnxChassisJ4320": jnxChassisJ4320,
       "jnxChassisJ2320": jnxChassisJ2320,
       "jnxChassisJ2350": jnxChassisJ2350,
       "jnxChassisMX480": jnxChassisMX480,
       "jnxChassisSRX5800": jnxChassisSRX5800,
       "jnxChassisT1600": jnxChassisT1600,
       "jnxChassisSRX5600": jnxChassisSRX5600,
       "jnxChassisMX240": jnxChassisMX240,
       "jnxChassisEX3200": jnxChassisEX3200,
       "jnxChassisEX4200": jnxChassisEX4200,
       "jnxEX4200RE0": jnxEX4200RE0,
       "jnxEX4200RE1": jnxEX4200RE1,
       "jnxChassisEX8208": jnxChassisEX8208,
       "jnxChassisEX8216": jnxChassisEX8216,
       "jnxChassisSRX3600": jnxChassisSRX3600,
       "jnxChassisSRX3400": jnxChassisSRX3400,
       "jnxChassisSRX210": jnxChassisSRX210,
       "jnxChassisTXP": jnxChassisTXP,
       "jnxChassisJCS": jnxChassisJCS,
       "jnxChassisSRX240": jnxChassisSRX240,
       "jnxChassisSRX650": jnxChassisSRX650,
       "jnxChassisSRX100": jnxChassisSRX100,
       "jnxChassisLN1000V": jnxChassisLN1000V,
       "jnxChassisEX2200": jnxChassisEX2200,
       "jnxChassisEX4500": jnxChassisEX4500,
       "jnxEX4500RE0": jnxEX4500RE0,
       "jnxEX4500RE1": jnxEX4500RE1,
       "jnxChassisFXChassis": jnxChassisFXChassis,
       "jnxChassisIBM4274M02J02M": jnxChassisIBM4274M02J02M,
       "jnxChassisIBM4274M06J06M": jnxChassisIBM4274M06J06M,
       "jnxChassisIBM4274M11J11M": jnxChassisIBM4274M11J11M,
       "jnxChassisSRX1400": jnxChassisSRX1400,
       "jnxChassisIBM4274S58J58S": jnxChassisIBM4274S58J58S,
       "jnxChassisIBM4274S56J56S": jnxChassisIBM4274S56J56S,
       "jnxChassisIBM4274S36J36S": jnxChassisIBM4274S36J36S,
       "jnxChassisIBM4274S34J34S": jnxChassisIBM4274S34J34S,
       "jnxChassisIBM427348EJ48E": jnxChassisIBM427348EJ48E,
       "jnxIBM427348EJ48ERE0": jnxIBM427348EJ48ERE0,
       "jnxIBM427348EJ48ERE1": jnxIBM427348EJ48ERE1,
       "jnxChassisIBM4274E08J08E": jnxChassisIBM4274E08J08E,
       "jnxChassisIBM4274E16J16E": jnxChassisIBM4274E16J16E,
       "jnxChassisMX80": jnxChassisMX80,
       "jnxChassisSRX220": jnxChassisSRX220,
       "jnxChassisEXXRE": jnxChassisEXXRE,
       "jnxEXXRERE0": jnxEXXRERE0,
       "jnxEXXRERE1": jnxEXXRERE1,
       "jnxChassisQFXInterconnect": jnxChassisQFXInterconnect,
       "jnxChassisQFXNode": jnxChassisQFXNode,
       "jnxChassisQFXJVRE": jnxChassisQFXJVRE,
       "jnxChassisEX4300": jnxChassisEX4300,
       "jnxEX4300RE0": jnxEX4300RE0,
       "jnxEX4300RE1": jnxEX4300RE1,
       "jnxEX4300MPRE0": jnxEX4300MPRE0,
       "jnxChassisSRX110": jnxChassisSRX110,
       "jnxChassisSRX120": jnxChassisSRX120,
       "jnxChassisMAG8600": jnxChassisMAG8600,
       "jnxChassisMAG6611": jnxChassisMAG6611,
       "jnxChassisMAG6610": jnxChassisMAG6610,
       "jnxChassisPTX5000": jnxChassisPTX5000,
       "jnxChassisIBM0719J45E": jnxChassisIBM0719J45E,
       "jnxIBM0719J45ERE0": jnxIBM0719J45ERE0,
       "jnxIBM0719J45ERE1": jnxIBM0719J45ERE1,
       "jnxChassisIBMJ08F": jnxChassisIBMJ08F,
       "jnxChassisIBMJ52F": jnxChassisIBMJ52F,
       "jnxChassisEX6210": jnxChassisEX6210,
       "jnxChassisDellJFX3500": jnxChassisDellJFX3500,
       "jnxChassisEX3300": jnxChassisEX3300,
       "jnxEX3300RE0": jnxEX3300RE0,
       "jnxEX3300RE1": jnxEX3300RE1,
       "jnxChassisDELLJSRX3600": jnxChassisDELLJSRX3600,
       "jnxChassisDELLJSRX3400": jnxChassisDELLJSRX3400,
       "jnxChassisDELLJSRX1400": jnxChassisDELLJSRX1400,
       "jnxChassisDELLJSRX5800": jnxChassisDELLJSRX5800,
       "jnxChassisDELLJSRX5600": jnxChassisDELLJSRX5600,
       "jnxChassisQFXSwitch": jnxChassisQFXSwitch,
       "jnxChassisT4000": jnxChassisT4000,
       "jnxChassisQFX3000": jnxChassisQFX3000,
       "jnxChassisQFX5000": jnxChassisQFX5000,
       "jnxChassisSRX550": jnxChassisSRX550,
       "jnxChassisACX": jnxChassisACX,
       "jnxChassisMX40": jnxChassisMX40,
       "jnxChassisMX10": jnxChassisMX10,
       "jnxChassisMX5": jnxChassisMX5,
       "jnxChassisQFXMInterconnect": jnxChassisQFXMInterconnect,
       "jnxChassisEX4550": jnxChassisEX4550,
       "jnxEX4550RE0": jnxEX4550RE0,
       "jnxEX4550RE1": jnxEX4550RE1,
       "jnxChassisMX2020": jnxChassisMX2020,
       "jnxChassisVseries": jnxChassisVseries,
       "jnxChassisLN2600": jnxChassisLN2600,
       "jnxChassisFireflyPerimeter": jnxChassisFireflyPerimeter,
       "jnxChassisMX104": jnxChassisMX104,
       "jnxChassisPTX3000": jnxChassisPTX3000,
       "jnxChassisMX2010": jnxChassisMX2010,
       "jnxChassisQFX3100": jnxChassisQFX3100,
       "jnxChassisLN2800": jnxChassisLN2800,
       "jnxChassisEX9214": jnxChassisEX9214,
       "jnxChassisEX9208": jnxChassisEX9208,
       "jnxChassisEX9204": jnxChassisEX9204,
       "jnxChassisSRX5400": jnxChassisSRX5400,
       "jnxChassisIBM4274S54J54S": jnxChassisIBM4274S54J54S,
       "jnxChassisDELLJSRX5400": jnxChassisDELLJSRX5400,
       "jnxChassisVMX": jnxChassisVMX,
       "jnxChassisEX4600": jnxChassisEX4600,
       "jnxChassisVRR": jnxChassisVRR,
       "jnxChassisACX1000": jnxChassisACX1000,
       "jnxChassisACX2000": jnxChassisACX2000,
       "jnxChassisACX1100": jnxChassisACX1100,
       "jnxChassisACX2100": jnxChassisACX2100,
       "jnxChassisACX2200": jnxChassisACX2200,
       "jnxChassisACX4000": jnxChassisACX4000,
       "jnxChassisACX500AC": jnxChassisACX500AC,
       "jnxChassisACX500DC": jnxChassisACX500DC,
       "jnxChassisACX500OAC": jnxChassisACX500OAC,
       "jnxChassisACX500ODC": jnxChassisACX500ODC,
       "jnxChassisACX500OPOEAC": jnxChassisACX500OPOEAC,
       "jnxChassisACX500OPOEDC": jnxChassisACX500OPOEDC,
       "jnxChassisSatelliteDevice": jnxChassisSatelliteDevice,
       "jnxChassisACX5048": jnxChassisACX5048,
       "jnxChassisACX5096": jnxChassisACX5096,
       "jnxChassisLN1000CC": jnxChassisLN1000CC,
       "jnxChassisVSRX": jnxChassisVSRX,
       "jnxChassisPTX1000": jnxChassisPTX1000,
       "jnxChassisEX3400": jnxChassisEX3400,
       "jnxEX3400RE0": jnxEX3400RE0,
       "jnxEX3400RE1": jnxEX3400RE1,
       "jnxChassisEX2300": jnxChassisEX2300,
       "jnxEX2300RE0": jnxEX2300RE0,
       "jnxEX2300RE1": jnxEX2300RE1,
       "jnxChassisSRX300": jnxChassisSRX300,
       "jnxChassisSRX320": jnxChassisSRX320,
       "jnxChassisSRX340": jnxChassisSRX340,
       "jnxChassisSRX345": jnxChassisSRX345,
       "jnxChassisSRX1500": jnxChassisSRX1500,
       "jnxChassisNFX": jnxChassisNFX,
       "jnxChassisJNP10003": jnxChassisJNP10003,
       "jnxChassisSRX4600": jnxChassisSRX4600,
       "jnxChassisSRX4800": jnxChassisSRX4800,
       "jnxChassisSRX4100": jnxChassisSRX4100,
       "jnxChassisSRX4200": jnxChassisSRX4200,
       "jnxChassisJNP204": jnxChassisJNP204,
       "jnxChassisMX2008": jnxChassisMX2008,
       "jnxChassisMXTSR80": jnxChassisMXTSR80,
       "jnxChassisPTX10008": jnxChassisPTX10008,
       "jnxChassisACX5448": jnxChassisACX5448,
       "jnxChassisPTX10016": jnxChassisPTX10016,
       "jnxChassisEX9251": jnxChassisEX9251,
       "jnxChassisMX150": jnxChassisMX150,
       "jnxChassisJNP10001": jnxChassisJNP10001,
       "jnxChassisMX10008": jnxChassisMX10008,
       "jnxChassisMX10016": jnxChassisMX10016,
       "jnxChassisEX9253": jnxChassisEX9253,
       "jnxChassisJRR200": jnxChassisJRR200,
       "jnxChassisACX5448M": jnxChassisACX5448M,
       "jnxChassisACX5448D": jnxChassisACX5448D,
       "jnxChassisACX6360OR": jnxChassisACX6360OR,
       "jnxChassisACX6360OX": jnxChassisACX6360OX,
       "jnxChassisACX710": jnxChassisACX710,
       "jnxChassisACX5800": jnxChassisACX5800,
       "jnxChassisSRX380": jnxChassisSRX380,
       "jnxChassisEX4400": jnxChassisEX4400,
       "jnxEX4400RE0": jnxEX4400RE0,
       "jnxEX4400RE1": jnxEX4400RE1,
       "jnxChassisR6675": jnxChassisR6675,
       "jnxChassisMX304": jnxChassisMX304,
       "jnxChassisMX10004": jnxChassisMX10004,
       "jnxChassisEX4100": jnxChassisEX4100,
       "jnxEX4100RE0": jnxEX4100RE0,
       "jnxEX4100RE1": jnxEX4100RE1,
       "jnxChassisEX4650": jnxChassisEX4650,
       "jnxChassisPTX1000260C": jnxChassisPTX1000260C,
       "jnxChassisPTX1000380c": jnxChassisPTX1000380c,
       "jnxChassisPTX10003160c": jnxChassisPTX10003160c,
       "jnxChassisQFX1000380c": jnxChassisQFX1000380c,
       "jnxChassisQFX10003160c": jnxChassisQFX10003160c,
       "jnxChassisPTX1000136mr": jnxChassisPTX1000136mr,
       "jnxChassisPTX10004": jnxChassisPTX10004,
       "jnxChassisACX753": jnxChassisACX753,
       "jnxChassisSRX1800": jnxChassisSRX1800,
       "jnxChassisACX7KSwitch": jnxChassisACX7KSwitch,
       "jnxChassisACX710032c": jnxChassisACX710032c,
       "jnxChassisACX710048l": jnxChassisACX710048l,
       "jnxChassisACX7908": jnxChassisACX7908,
       "jnxChassisACX7024": jnxChassisACX7024,
       "jnxChassisSRX1600": jnxChassisSRX1600,
       "jnxChassisSRX2300": jnxChassisSRX2300,
       "jnxChassisSRX4300": jnxChassisSRX4300,
       "jnxChassisACX7332": jnxChassisACX7332,
       "jnxChassisACX7348": jnxChassisACX7348,
       "jnxChassisACX7024X": jnxChassisACX7024X,
       "jnxChassisPTX1000236qdd": jnxChassisPTX1000236qdd,
       "jnxChassisSRX4700": jnxChassisSRX4700,
       "jnxSlot": jnxSlot,
       "jnxSlotM40": jnxSlotM40,
       "jnxSlotFPC": jnxSlotFPC,
       "jnxSlotSCB": jnxSlotSCB,
       "jnxSlotHostCtlr": jnxSlotHostCtlr,
       "jnxSlotPowerSupply": jnxSlotPowerSupply,
       "jnxSlotCoolingImpeller": jnxSlotCoolingImpeller,
       "jnxSlotCoolingFan": jnxSlotCoolingFan,
       "jnxSlotRoutingEngine": jnxSlotRoutingEngine,
       "jnxSlotM20": jnxSlotM20,
       "jnxM20SlotFPC": jnxM20SlotFPC,
       "jnxM20SlotSSB": jnxM20SlotSSB,
       "jnxM20SlotRE": jnxM20SlotRE,
       "jnxM20SlotPower": jnxM20SlotPower,
       "jnxM20SlotFan": jnxM20SlotFan,
       "jnxM20SlotFrontPanel": jnxM20SlotFrontPanel,
       "jnxSlotM160": jnxSlotM160,
       "jnxM160SlotFPC": jnxM160SlotFPC,
       "jnxM160SlotSFM": jnxM160SlotSFM,
       "jnxM160SlotHM": jnxM160SlotHM,
       "jnxM160SlotPCG": jnxM160SlotPCG,
       "jnxM160SlotPower": jnxM160SlotPower,
       "jnxM160SlotFan": jnxM160SlotFan,
       "jnxM160SlotMCS": jnxM160SlotMCS,
       "jnxM160SlotFPM": jnxM160SlotFPM,
       "jnxM160SlotCIP": jnxM160SlotCIP,
       "jnxSlotM10": jnxSlotM10,
       "jnxM10SlotFPC": jnxM10SlotFPC,
       "jnxM10SlotFEB": jnxM10SlotFEB,
       "jnxM10SlotRE": jnxM10SlotRE,
       "jnxM10SlotPower": jnxM10SlotPower,
       "jnxM10SlotFan": jnxM10SlotFan,
       "jnxSlotM5": jnxSlotM5,
       "jnxM5SlotFPC": jnxM5SlotFPC,
       "jnxM5SlotFEB": jnxM5SlotFEB,
       "jnxM5SlotRE": jnxM5SlotRE,
       "jnxM5SlotPower": jnxM5SlotPower,
       "jnxM5SlotFan": jnxM5SlotFan,
       "jnxSlotT640": jnxSlotT640,
       "jnxT640SlotFPC": jnxT640SlotFPC,
       "jnxT640SlotSIB": jnxT640SlotSIB,
       "jnxT640SlotHM": jnxT640SlotHM,
       "jnxT640SlotSCG": jnxT640SlotSCG,
       "jnxT640SlotPower": jnxT640SlotPower,
       "jnxT640SlotFan": jnxT640SlotFan,
       "jnxT640SlotCB": jnxT640SlotCB,
       "jnxT640SlotFPB": jnxT640SlotFPB,
       "jnxT640SlotCIP": jnxT640SlotCIP,
       "jnxT640SlotSPMB": jnxT640SlotSPMB,
       "jnxT640SlotPSD": jnxT640SlotPSD,
       "jnxSlotT320": jnxSlotT320,
       "jnxT320SlotFPC": jnxT320SlotFPC,
       "jnxT320SlotSIB": jnxT320SlotSIB,
       "jnxT320SlotHM": jnxT320SlotHM,
       "jnxT320SlotSCG": jnxT320SlotSCG,
       "jnxT320SlotPower": jnxT320SlotPower,
       "jnxT320SlotFan": jnxT320SlotFan,
       "jnxT320SlotCB": jnxT320SlotCB,
       "jnxT320SlotFPB": jnxT320SlotFPB,
       "jnxT320SlotCIP": jnxT320SlotCIP,
       "jnxT320SlotSPMB": jnxT320SlotSPMB,
       "jnxT320SlotPSD": jnxT320SlotPSD,
       "jnxSlotM40e": jnxSlotM40e,
       "jnxM40eSlotFPC": jnxM40eSlotFPC,
       "jnxM40eSlotSFM": jnxM40eSlotSFM,
       "jnxM40eSlotHM": jnxM40eSlotHM,
       "jnxM40eSlotPCG": jnxM40eSlotPCG,
       "jnxM40eSlotPower": jnxM40eSlotPower,
       "jnxM40eSlotFan": jnxM40eSlotFan,
       "jnxM40eSlotMCS": jnxM40eSlotMCS,
       "jnxM40eSlotFPM": jnxM40eSlotFPM,
       "jnxM40eSlotCIP": jnxM40eSlotCIP,
       "jnxSlotM320": jnxSlotM320,
       "jnxM320SlotFPC": jnxM320SlotFPC,
       "jnxM320SlotSIB": jnxM320SlotSIB,
       "jnxM320SlotHM": jnxM320SlotHM,
       "jnxM320SlotPower": jnxM320SlotPower,
       "jnxM320SlotFan": jnxM320SlotFan,
       "jnxM320SlotCB": jnxM320SlotCB,
       "jnxM320SlotFPB": jnxM320SlotFPB,
       "jnxM320SlotCIP": jnxM320SlotCIP,
       "jnxSlotM7i": jnxSlotM7i,
       "jnxM7iSlotFPC": jnxM7iSlotFPC,
       "jnxM7iSlotCFEB": jnxM7iSlotCFEB,
       "jnxM7iSlotRE": jnxM7iSlotRE,
       "jnxM7iSlotPower": jnxM7iSlotPower,
       "jnxM7iSlotFan": jnxM7iSlotFan,
       "jnxSlotM10i": jnxSlotM10i,
       "jnxM10iSlotFPC": jnxM10iSlotFPC,
       "jnxM10iSlotCFEB": jnxM10iSlotCFEB,
       "jnxM10iSlotRE": jnxM10iSlotRE,
       "jnxM10iSlotPower": jnxM10iSlotPower,
       "jnxM10iSlotFan": jnxM10iSlotFan,
       "jnxM10iSlotHCM": jnxM10iSlotHCM,
       "jnxSlotJ2300": jnxSlotJ2300,
       "jnxJ2300SlotFPC": jnxJ2300SlotFPC,
       "jnxJ2300SlotRE": jnxJ2300SlotRE,
       "jnxJ2300SlotFan": jnxJ2300SlotFan,
       "jnxSlotJ4300": jnxSlotJ4300,
       "jnxJ4300SlotFPC": jnxJ4300SlotFPC,
       "jnxJ4300SlotRE": jnxJ4300SlotRE,
       "jnxJ4300SlotFan": jnxJ4300SlotFan,
       "jnxSlotJ6300": jnxSlotJ6300,
       "jnxJ6300SlotFPC": jnxJ6300SlotFPC,
       "jnxJ6300SlotRE": jnxJ6300SlotRE,
       "jnxJ6300SlotFan": jnxJ6300SlotFan,
       "jnxSlotIRM": jnxSlotIRM,
       "jnxIRMSlotFPC": jnxIRMSlotFPC,
       "jnxIRMSlotCFEB": jnxIRMSlotCFEB,
       "jnxIRMSlotRE": jnxIRMSlotRE,
       "jnxIRMSlotPower": jnxIRMSlotPower,
       "jnxSlotTX": jnxSlotTX,
       "jnxTXSlotSIB": jnxTXSlotSIB,
       "jnxTXSlotHM": jnxTXSlotHM,
       "jnxTXSlotPower": jnxTXSlotPower,
       "jnxTXSlotFan": jnxTXSlotFan,
       "jnxTXSlotCB": jnxTXSlotCB,
       "jnxTXSlotFPB": jnxTXSlotFPB,
       "jnxTXSlotCIP": jnxTXSlotCIP,
       "jnxTXSlotSPMB": jnxTXSlotSPMB,
       "jnxTXSlotLCC": jnxTXSlotLCC,
       "jnxSlotM120": jnxSlotM120,
       "jnxM120SlotFPC": jnxM120SlotFPC,
       "jnxM120SlotFEB": jnxM120SlotFEB,
       "jnxM120SlotHM": jnxM120SlotHM,
       "jnxM120SlotPower": jnxM120SlotPower,
       "jnxM120SlotFan": jnxM120SlotFan,
       "jnxM120SlotCB": jnxM120SlotCB,
       "jnxM120SlotFPB": jnxM120SlotFPB,
       "jnxSlotJ4350": jnxSlotJ4350,
       "jnxJ4350SlotFPC": jnxJ4350SlotFPC,
       "jnxJ4350SlotRE": jnxJ4350SlotRE,
       "jnxJ4350SlotPower": jnxJ4350SlotPower,
       "jnxJ4350SlotFan": jnxJ4350SlotFan,
       "jnxSlotJ6350": jnxSlotJ6350,
       "jnxJ6350SlotFPC": jnxJ6350SlotFPC,
       "jnxJ6350SlotRE": jnxJ6350SlotRE,
       "jnxJ6350SlotPower": jnxJ6350SlotPower,
       "jnxJ6350SlotFan": jnxJ6350SlotFan,
       "jnxSlotMX960": jnxSlotMX960,
       "jnxMX960SlotFPC": jnxMX960SlotFPC,
       "jnxMX960SlotHM": jnxMX960SlotHM,
       "jnxMX960SlotPower": jnxMX960SlotPower,
       "jnxMX960SlotFan": jnxMX960SlotFan,
       "jnxMX960SlotCB": jnxMX960SlotCB,
       "jnxMX960SlotFPB": jnxMX960SlotFPB,
       "jnxSlotJ4320": jnxSlotJ4320,
       "jnxJ4320SlotFPC": jnxJ4320SlotFPC,
       "jnxJ4320SlotRE": jnxJ4320SlotRE,
       "jnxSlotJ2320": jnxSlotJ2320,
       "jnxJ2320SlotFPC": jnxJ2320SlotFPC,
       "jnxJ2320SlotRE": jnxJ2320SlotRE,
       "jnxJ2320SlotPower": jnxJ2320SlotPower,
       "jnxJ2320SlotFan": jnxJ2320SlotFan,
       "jnxSlotJ2350": jnxSlotJ2350,
       "jnxJ2350SlotFPC": jnxJ2350SlotFPC,
       "jnxJ2350SlotRE": jnxJ2350SlotRE,
       "jnxJ2350SlotPower": jnxJ2350SlotPower,
       "jnxJ2350SlotFan": jnxJ2350SlotFan,
       "jnxSlotMX480": jnxSlotMX480,
       "jnxMX480SlotFPC": jnxMX480SlotFPC,
       "jnxMX480SlotHM": jnxMX480SlotHM,
       "jnxMX480SlotPower": jnxMX480SlotPower,
       "jnxMX480SlotFan": jnxMX480SlotFan,
       "jnxMX480SlotCB": jnxMX480SlotCB,
       "jnxMX480SlotFPB": jnxMX480SlotFPB,
       "jnxSlotSRX5800": jnxSlotSRX5800,
       "jnxSRX5800SlotFPC": jnxSRX5800SlotFPC,
       "jnxSRX5800SlotHM": jnxSRX5800SlotHM,
       "jnxSRX5800SlotPower": jnxSRX5800SlotPower,
       "jnxSRX5800SlotFan": jnxSRX5800SlotFan,
       "jnxSRX5800SlotCB": jnxSRX5800SlotCB,
       "jnxSRX5800SlotFPB": jnxSRX5800SlotFPB,
       "jnxSlotT1600": jnxSlotT1600,
       "jnxT1600SlotFPC": jnxT1600SlotFPC,
       "jnxT1600SlotSIB": jnxT1600SlotSIB,
       "jnxT1600SlotHM": jnxT1600SlotHM,
       "jnxT1600SlotSCG": jnxT1600SlotSCG,
       "jnxT1600SlotPower": jnxT1600SlotPower,
       "jnxT1600SlotFan": jnxT1600SlotFan,
       "jnxT1600SlotCB": jnxT1600SlotCB,
       "jnxT1600SlotFPB": jnxT1600SlotFPB,
       "jnxT1600SlotCIP": jnxT1600SlotCIP,
       "jnxT1600SlotSPMB": jnxT1600SlotSPMB,
       "jnxT1600SlotPSD": jnxT1600SlotPSD,
       "jnxSlotSRX5600": jnxSlotSRX5600,
       "jnxSRX5600SlotFPC": jnxSRX5600SlotFPC,
       "jnxSRX5600SlotHM": jnxSRX5600SlotHM,
       "jnxSRX5600SlotPower": jnxSRX5600SlotPower,
       "jnxSRX5600SlotFan": jnxSRX5600SlotFan,
       "jnxSRX5600SlotCB": jnxSRX5600SlotCB,
       "jnxSRX5600SlotFPB": jnxSRX5600SlotFPB,
       "jnxSlotMX240": jnxSlotMX240,
       "jnxMX240SlotFPC": jnxMX240SlotFPC,
       "jnxMX240SlotHM": jnxMX240SlotHM,
       "jnxMX240SlotPower": jnxMX240SlotPower,
       "jnxMX240SlotFan": jnxMX240SlotFan,
       "jnxMX240SlotCB": jnxMX240SlotCB,
       "jnxMX240SlotFPB": jnxMX240SlotFPB,
       "jnxSlotEX3200": jnxSlotEX3200,
       "jnxEX3200SlotFPC": jnxEX3200SlotFPC,
       "jnxEX3200SlotPower": jnxEX3200SlotPower,
       "jnxEX3200SlotFan": jnxEX3200SlotFan,
       "jnxEX3200SlotRE": jnxEX3200SlotRE,
       "jnxSlotEX4200": jnxSlotEX4200,
       "jnxEX4200SlotFPC": jnxEX4200SlotFPC,
       "jnxEX4200SlotPower": jnxEX4200SlotPower,
       "jnxEX4200SlotFan": jnxEX4200SlotFan,
       "jnxSlotEX8208": jnxSlotEX8208,
       "jnxEX8208SlotFPC": jnxEX8208SlotFPC,
       "jnxEX8208Slot48S": jnxEX8208Slot48S,
       "jnxEX8208Slot48T": jnxEX8208Slot48T,
       "jnxEX8208Slot8XS": jnxEX8208Slot8XS,
       "jnxEX8208HM": jnxEX8208HM,
       "jnxEX8208SlotPower": jnxEX8208SlotPower,
       "jnxEX8208SlotFan": jnxEX8208SlotFan,
       "jnxEX8208SlotFT": jnxEX8208SlotFT,
       "jnxEX8208SlotCBD": jnxEX8208SlotCBD,
       "jnxSlotEX8216": jnxSlotEX8216,
       "jnxEX8216SlotFPC": jnxEX8216SlotFPC,
       "jnxEX8216Slot48S": jnxEX8216Slot48S,
       "jnxEX8216Slot48T": jnxEX8216Slot48T,
       "jnxEX8216Slot8XS": jnxEX8216Slot8XS,
       "jnxEX8216SIB": jnxEX8216SIB,
       "jnxEX8216HM": jnxEX8216HM,
       "jnxEX8216SlotPower": jnxEX8216SlotPower,
       "jnxEX8216SlotFan": jnxEX8216SlotFan,
       "jnxEX8216SlotFT": jnxEX8216SlotFT,
       "jnxEX8216SlotRFT": jnxEX8216SlotRFT,
       "jnxEX8216SlotCBD": jnxEX8216SlotCBD,
       "jnxSlotSRX3600": jnxSlotSRX3600,
       "jnxSRX3600SlotFPC": jnxSRX3600SlotFPC,
       "jnxSRX3600SlotHM": jnxSRX3600SlotHM,
       "jnxSRX3600SlotPower": jnxSRX3600SlotPower,
       "jnxSRX3600SlotFan": jnxSRX3600SlotFan,
       "jnxSRX3600SlotCB": jnxSRX3600SlotCB,
       "jnxSRX3600SlotFPB": jnxSRX3600SlotFPB,
       "jnxSlotSRX3400": jnxSlotSRX3400,
       "jnxSRX3400SlotFPC": jnxSRX3400SlotFPC,
       "jnxSRX3400SlotHM": jnxSRX3400SlotHM,
       "jnxSRX3400SlotPower": jnxSRX3400SlotPower,
       "jnxSRX3400SlotFan": jnxSRX3400SlotFan,
       "jnxSRX3400SlotCB": jnxSRX3400SlotCB,
       "jnxSRX3400SlotFPB": jnxSRX3400SlotFPB,
       "jnxSlotSRX210": jnxSlotSRX210,
       "jnxSRX210SlotFPC": jnxSRX210SlotFPC,
       "jnxSRX210SlotRE": jnxSRX210SlotRE,
       "jnxSRX210SlotPower": jnxSRX210SlotPower,
       "jnxSRX210SlotFan": jnxSRX210SlotFan,
       "jnxSlotTXP": jnxSlotTXP,
       "jnxTXPSlotSIB": jnxTXPSlotSIB,
       "jnxTXPSlotHM": jnxTXPSlotHM,
       "jnxTXPSlotPower": jnxTXPSlotPower,
       "jnxTXPSlotFan": jnxTXPSlotFan,
       "jnxTXPSlotCB": jnxTXPSlotCB,
       "jnxTXPSlotFPB": jnxTXPSlotFPB,
       "jnxTXPSlotCIP": jnxTXPSlotCIP,
       "jnxTXPSlotSPMB": jnxTXPSlotSPMB,
       "jnxTXPSlotLCC": jnxTXPSlotLCC,
       "jnxTXPSlotSFC": jnxTXPSlotSFC,
       "jnxSlotJCS": jnxSlotJCS,
       "jnxJCSSlotHM": jnxJCSSlotHM,
       "jnxJCSSlotFPC": jnxJCSSlotFPC,
       "jnxSlotSRX240": jnxSlotSRX240,
       "jnxSRX240SlotFPC": jnxSRX240SlotFPC,
       "jnxSRX240SlotRE": jnxSRX240SlotRE,
       "jnxSRX240SlotPower": jnxSRX240SlotPower,
       "jnxSRX240SlotFan": jnxSRX240SlotFan,
       "jnxSlotSRX650": jnxSlotSRX650,
       "jnxSRX650SlotFPC": jnxSRX650SlotFPC,
       "jnxSRX650SlotRE": jnxSRX650SlotRE,
       "jnxSRX650SlotPower": jnxSRX650SlotPower,
       "jnxSRX650SlotFan": jnxSRX650SlotFan,
       "jnxSlotSRX100": jnxSlotSRX100,
       "jnxSRX100SlotFPC": jnxSRX100SlotFPC,
       "jnxSRX100SlotRE": jnxSRX100SlotRE,
       "jnxSRX100SlotPower": jnxSRX100SlotPower,
       "jnxSRX100SlotFan": jnxSRX100SlotFan,
       "jnxSlotLN1000V": jnxSlotLN1000V,
       "jnxLN1000VSlotFPC": jnxLN1000VSlotFPC,
       "jnxLN1000VSlotRE": jnxLN1000VSlotRE,
       "jnxLN1000VSlotPower": jnxLN1000VSlotPower,
       "jnxLN1000VSlotFan": jnxLN1000VSlotFan,
       "jnxSlotEX2200": jnxSlotEX2200,
       "jnxEX2200SlotFPC": jnxEX2200SlotFPC,
       "jnxEX2200SlotPower": jnxEX2200SlotPower,
       "jnxEX2200SlotFan": jnxEX2200SlotFan,
       "jnxEX2200SlotRE": jnxEX2200SlotRE,
       "jnxSlotEX4500": jnxSlotEX4500,
       "jnxEX4500SlotFPC": jnxEX4500SlotFPC,
       "jnxEX4500SlotPower": jnxEX4500SlotPower,
       "jnxEX4500SlotFan": jnxEX4500SlotFan,
       "jnxEX4500SlotRE": jnxEX4500SlotRE,
       "jnxSlotIBM4274M02J02M": jnxSlotIBM4274M02J02M,
       "jnxIBM4274M02J02MSlotFPC": jnxIBM4274M02J02MSlotFPC,
       "jnxIBM4274M02J02MSlotHM": jnxIBM4274M02J02MSlotHM,
       "jnxIBM4274M02J02MSlotPower": jnxIBM4274M02J02MSlotPower,
       "jnxIBM4274M02J02MSlotFan": jnxIBM4274M02J02MSlotFan,
       "jnxIBM4274M02J02MSlotCB": jnxIBM4274M02J02MSlotCB,
       "jnxIBM4274M02J02MSlotFPB": jnxIBM4274M02J02MSlotFPB,
       "jnxSlotIBM4274M06J06M": jnxSlotIBM4274M06J06M,
       "jnxIBM4274M06J06MSlotFPC": jnxIBM4274M06J06MSlotFPC,
       "jnxIBM4274M06J06MSlotHM": jnxIBM4274M06J06MSlotHM,
       "jnxIBM4274M06J06MSlotPower": jnxIBM4274M06J06MSlotPower,
       "jnxIBM4274M06J06MSlotFan": jnxIBM4274M06J06MSlotFan,
       "jnxIBM4274M06J06MSlotCB": jnxIBM4274M06J06MSlotCB,
       "jnxIBM4274M06J06MSlotFPB": jnxIBM4274M06J06MSlotFPB,
       "jnxSlotIBM4274M11J11M": jnxSlotIBM4274M11J11M,
       "jnxIBM4274M11J11MSlotFPC": jnxIBM4274M11J11MSlotFPC,
       "jnxIBM4274M11J11MSlotHM": jnxIBM4274M11J11MSlotHM,
       "jnxIBM4274M11J11MSlotPower": jnxIBM4274M11J11MSlotPower,
       "jnxIBM4274M11J11MSlotFan": jnxIBM4274M11J11MSlotFan,
       "jnxIBM4274M11J11MSlotCB": jnxIBM4274M11J11MSlotCB,
       "jnxIBM4274M11J11MSlotFPB": jnxIBM4274M11J11MSlotFPB,
       "jnxSlotSRX1400": jnxSlotSRX1400,
       "jnxSRX1400SlotFPC": jnxSRX1400SlotFPC,
       "jnxSRX1400SlotHM": jnxSRX1400SlotHM,
       "jnxSRX1400SlotPower": jnxSRX1400SlotPower,
       "jnxSRX1400SlotFan": jnxSRX1400SlotFan,
       "jnxSRX1400SlotCB": jnxSRX1400SlotCB,
       "jnxSRX1400SlotFPB": jnxSRX1400SlotFPB,
       "jnxSlotIBM4274S58J58S": jnxSlotIBM4274S58J58S,
       "jnxIBM4274S58J58SSlotFPC": jnxIBM4274S58J58SSlotFPC,
       "jnxIBM4274S58J58SSlotHM": jnxIBM4274S58J58SSlotHM,
       "jnxIBM4274S58J58SSlotPower": jnxIBM4274S58J58SSlotPower,
       "jnxIBM4274S58J58SSlotFan": jnxIBM4274S58J58SSlotFan,
       "jnxIBM4274S58J58SSlotCB": jnxIBM4274S58J58SSlotCB,
       "jnxIBM4274S58J58SSlotFPB": jnxIBM4274S58J58SSlotFPB,
       "jnxSlotIBM4274S56J56S": jnxSlotIBM4274S56J56S,
       "jnxIBM4274S56J56SSlotFPC": jnxIBM4274S56J56SSlotFPC,
       "jnxIBM4274S56J56SSlotHM": jnxIBM4274S56J56SSlotHM,
       "jnxIBM4274S56J56SSlotPower": jnxIBM4274S56J56SSlotPower,
       "jnxIBM4274S56J56SSlotFan": jnxIBM4274S56J56SSlotFan,
       "jnxIBM4274S56J56SSlotCB": jnxIBM4274S56J56SSlotCB,
       "jnxIBM4274S56J56SSlotFPB": jnxIBM4274S56J56SSlotFPB,
       "jnxSlotIBM4274S36J36S": jnxSlotIBM4274S36J36S,
       "jnxIBM4274S36J36SSlotFPC": jnxIBM4274S36J36SSlotFPC,
       "jnxIBM4274S36J36SSlotHM": jnxIBM4274S36J36SSlotHM,
       "jnxIBM4274S36J36SSlotPower": jnxIBM4274S36J36SSlotPower,
       "jnxIBM4274S36J36SSlotFan": jnxIBM4274S36J36SSlotFan,
       "jnxIBM4274S36J36SSlotCB": jnxIBM4274S36J36SSlotCB,
       "jnxIBM4274S36J36SSlotFPB": jnxIBM4274S36J36SSlotFPB,
       "jnxSlotIBM4274S34J34S": jnxSlotIBM4274S34J34S,
       "jnxIBM4274S34J34SSlotFPC": jnxIBM4274S34J34SSlotFPC,
       "jnxIBM4274S34J34SSlotHM": jnxIBM4274S34J34SSlotHM,
       "jnxIBM4274S34J34SSlotPower": jnxIBM4274S34J34SSlotPower,
       "jnxIBM4274S34J34SSlotFan": jnxIBM4274S34J34SSlotFan,
       "jnxIBM4274S34J34SSlotCB": jnxIBM4274S34J34SSlotCB,
       "jnxIBM4274S34J34SSlotFPB": jnxIBM4274S34J34SSlotFPB,
       "jnxSlotIBM427348EJ48E": jnxSlotIBM427348EJ48E,
       "jnxIBM427348EJ48ESlotFPC": jnxIBM427348EJ48ESlotFPC,
       "jnxIBM427348EJ48ESlotPower": jnxIBM427348EJ48ESlotPower,
       "jnxIBM427348EJ48ESlotFan": jnxIBM427348EJ48ESlotFan,
       "jnxSlotIBM4274E08J08E": jnxSlotIBM4274E08J08E,
       "jnxIBM4274E08J08ESlotFPC": jnxIBM4274E08J08ESlotFPC,
       "jnxIBM4274E08J08ESlot48S": jnxIBM4274E08J08ESlot48S,
       "jnxIBM4274E08J08ESlot48T": jnxIBM4274E08J08ESlot48T,
       "jnxIBM4274E08J08ESlot8XS": jnxIBM4274E08J08ESlot8XS,
       "jnxIBM4274E08J08EHM": jnxIBM4274E08J08EHM,
       "jnxIBM4274E08J08ESlotPower": jnxIBM4274E08J08ESlotPower,
       "jnxIBM4274E08J08ESlotFan": jnxIBM4274E08J08ESlotFan,
       "jnxIBM4274E08J08ESlotFT": jnxIBM4274E08J08ESlotFT,
       "jnxIBM4274E08J08ESlotCBD": jnxIBM4274E08J08ESlotCBD,
       "jnxSlotIBM4274E16J16E": jnxSlotIBM4274E16J16E,
       "jnxIBM4274E16J16ESlotFPC": jnxIBM4274E16J16ESlotFPC,
       "jnxIBM4274E16J16ESlot48S": jnxIBM4274E16J16ESlot48S,
       "jnxIBM4274E16J16ESlot48T": jnxIBM4274E16J16ESlot48T,
       "jnxIBM4274E16J16ESlot8XS": jnxIBM4274E16J16ESlot8XS,
       "jnxIBM4274E16J16ESIB": jnxIBM4274E16J16ESIB,
       "jnxIBM4274E16J16EHM": jnxIBM4274E16J16EHM,
       "jnxIBM4274E16J16ESlotPower": jnxIBM4274E16J16ESlotPower,
       "jnxIBM4274E16J16ESlotFan": jnxIBM4274E16J16ESlotFan,
       "jnxIBM4274E16J16ESlotFT": jnxIBM4274E16J16ESlotFT,
       "jnxIBM4274E16J16ESlotRFT": jnxIBM4274E16J16ESlotRFT,
       "jnxIBM4274E16J16ESlotCBD": jnxIBM4274E16J16ESlotCBD,
       "jnxSlotMX80": jnxSlotMX80,
       "jnxMX80SlotFPC": jnxMX80SlotFPC,
       "jnxMX80SlotCFEB": jnxMX80SlotCFEB,
       "jnxMX80SlotRE": jnxMX80SlotRE,
       "jnxMX80SlotPower": jnxMX80SlotPower,
       "jnxMX80SlotFan": jnxMX80SlotFan,
       "jnxSlotSRX220": jnxSlotSRX220,
       "jnxSRX220SlotFPC": jnxSRX220SlotFPC,
       "jnxSRX220SlotRE": jnxSRX220SlotRE,
       "jnxSRX220SlotPower": jnxSRX220SlotPower,
       "jnxSRX220SlotFan": jnxSRX220SlotFan,
       "jnxSlotEXXRE": jnxSlotEXXRE,
       "jnxEXXRESlotPower": jnxEXXRESlotPower,
       "jnxEXXRESlotFan": jnxEXXRESlotFan,
       "jnxEXXRESlotHM": jnxEXXRESlotHM,
       "jnxEXXRESlotLCC": jnxEXXRESlotLCC,
       "jnxSlotQFXInterconnect": jnxSlotQFXInterconnect,
       "jnxQFXInterconnectSlotFPC": jnxQFXInterconnectSlotFPC,
       "jnxQFXInterconnectSlotHM": jnxQFXInterconnectSlotHM,
       "jnxQFXInterconnectSlotPower": jnxQFXInterconnectSlotPower,
       "jnxQFXInterconnectSlotFan": jnxQFXInterconnectSlotFan,
       "jnxQFXInterconnectSlotCBD": jnxQFXInterconnectSlotCBD,
       "jnxQFXInterconnectSlotFPB": jnxQFXInterconnectSlotFPB,
       "jnxSlotQFXNode": jnxSlotQFXNode,
       "jnxQFXNodeSlotFPC": jnxQFXNodeSlotFPC,
       "jnxQFXNodeSlotHM": jnxQFXNodeSlotHM,
       "jnxQFXNodeSlotPower": jnxQFXNodeSlotPower,
       "jnxQFXNodeSlotFan": jnxQFXNodeSlotFan,
       "jnxQFXNodeSlotFPB": jnxQFXNodeSlotFPB,
       "jnxSlotQFXJVRE": jnxSlotQFXJVRE,
       "jnxQFXJVRESlotFPC": jnxQFXJVRESlotFPC,
       "jnxQFXJVRESlotHM": jnxQFXJVRESlotHM,
       "jnxQFXJVRESlotPower": jnxQFXJVRESlotPower,
       "jnxQFXJVRESlotFan": jnxQFXJVRESlotFan,
       "jnxQFXJVRESlotFPB": jnxQFXJVRESlotFPB,
       "jnxSlotEX4300": jnxSlotEX4300,
       "jnxEX4300SlotFPC": jnxEX4300SlotFPC,
       "jnxEX4300SlotPower": jnxEX4300SlotPower,
       "jnxEX4300SlotFan": jnxEX4300SlotFan,
       "jnxEX4300MPSlotFPC": jnxEX4300MPSlotFPC,
       "jnxEX4300MPSlotFan": jnxEX4300MPSlotFan,
       "jnxSlotSRX110": jnxSlotSRX110,
       "jnxSRX110SlotFPC": jnxSRX110SlotFPC,
       "jnxSRX110SlotRE": jnxSRX110SlotRE,
       "jnxSRX110SlotPower": jnxSRX110SlotPower,
       "jnxSRX110SlotFan": jnxSRX110SlotFan,
       "jnxSlotSRX120": jnxSlotSRX120,
       "jnxSRX120SlotFPC": jnxSRX120SlotFPC,
       "jnxSRX120SlotRE": jnxSRX120SlotRE,
       "jnxSRX120SlotPower": jnxSRX120SlotPower,
       "jnxSRX120SlotFan": jnxSRX120SlotFan,
       "jnxSlotMAG8600": jnxSlotMAG8600,
       "jnxMAG8600SlotFPC": jnxMAG8600SlotFPC,
       "jnxMAG8600SlotRE": jnxMAG8600SlotRE,
       "jnxMAG8600SlotPower": jnxMAG8600SlotPower,
       "jnxMAG8600SlotFan": jnxMAG8600SlotFan,
       "jnxMAG8600SlotCB": jnxMAG8600SlotCB,
       "jnxSlotMAG6611": jnxSlotMAG6611,
       "jnxMAG6611SlotFPC": jnxMAG6611SlotFPC,
       "jnxMAG6611SlotRE": jnxMAG6611SlotRE,
       "jnxMAG6611SlotPower": jnxMAG6611SlotPower,
       "jnxMAG6611SlotFan": jnxMAG6611SlotFan,
       "jnxMAG6611SlotCB": jnxMAG6611SlotCB,
       "jnxSlotMAG6610": jnxSlotMAG6610,
       "jnxMAG6610SlotFPC": jnxMAG6610SlotFPC,
       "jnxMAG6610SlotRE": jnxMAG6610SlotRE,
       "jnxMAG6610SlotPower": jnxMAG6610SlotPower,
       "jnxMAG6610SlotFan": jnxMAG6610SlotFan,
       "jnxMAG6610SlotCB": jnxMAG6610SlotCB,
       "jnxSlotPTX5000": jnxSlotPTX5000,
       "jnxPTX5000SlotSIB": jnxPTX5000SlotSIB,
       "jnxPTX5000SlotHM": jnxPTX5000SlotHM,
       "jnxPTX5000SlotFPC": jnxPTX5000SlotFPC,
       "jnxPTX5000SlotFan": jnxPTX5000SlotFan,
       "jnxPTX5000SlotCB": jnxPTX5000SlotCB,
       "jnxPTX5000SlotFPB": jnxPTX5000SlotFPB,
       "jnxPTX5000SlotSPMB": jnxPTX5000SlotSPMB,
       "jnxPTX5000SlotPDU": jnxPTX5000SlotPDU,
       "jnxPTX5000SlotPSM": jnxPTX5000SlotPSM,
       "jnxPTX5000SlotCCG": jnxPTX5000SlotCCG,
       "jnxPTX5000SlotPIC": jnxPTX5000SlotPIC,
       "jnxSlotIBM0719J45E": jnxSlotIBM0719J45E,
       "jnxIBM0719J45ESlotFPC": jnxIBM0719J45ESlotFPC,
       "jnxIBM0719J45ESlotPower": jnxIBM0719J45ESlotPower,
       "jnxIBM0719J45ESlotFan": jnxIBM0719J45ESlotFan,
       "jnxIBM0719J45ESlotRE": jnxIBM0719J45ESlotRE,
       "jnxSlotIBMJ08F": jnxSlotIBMJ08F,
       "jnxIBMJ08FSlotFPC": jnxIBMJ08FSlotFPC,
       "jnxIBMJ08FSlotHM": jnxIBMJ08FSlotHM,
       "jnxIBMJ08FSlotPower": jnxIBMJ08FSlotPower,
       "jnxIBMJ08FSlotFan": jnxIBMJ08FSlotFan,
       "jnxIBMJ08FSlotCBD": jnxIBMJ08FSlotCBD,
       "jnxIBMJ08FSlotFPB": jnxIBMJ08FSlotFPB,
       "jnxSlotIBMJ52F": jnxSlotIBMJ52F,
       "jnxIBMJ52FSlotFPC": jnxIBMJ52FSlotFPC,
       "jnxIBMJ52FSlotHM": jnxIBMJ52FSlotHM,
       "jnxIBMJ52FSlotPower": jnxIBMJ52FSlotPower,
       "jnxIBMJ52FSlotFan": jnxIBMJ52FSlotFan,
       "jnxIBMJ52FSlotFPB": jnxIBMJ52FSlotFPB,
       "jnxSlotEX6210": jnxSlotEX6210,
       "jnxEX6210SlotFPC": jnxEX6210SlotFPC,
       "jnxEX6210Slot48P": jnxEX6210Slot48P,
       "jnxEX6210Slot48T": jnxEX6210Slot48T,
       "jnxEX6210HM": jnxEX6210HM,
       "jnxEX6210SlotPower": jnxEX6210SlotPower,
       "jnxEX6210SlotFan": jnxEX6210SlotFan,
       "jnxEX6210SlotFT": jnxEX6210SlotFT,
       "jnxEX6210SlotCBD": jnxEX6210SlotCBD,
       "jnxSlotDellJFX3500": jnxSlotDellJFX3500,
       "jnxDellJFX3500SlotFPC": jnxDellJFX3500SlotFPC,
       "jnxDellJFX3500SlotHM": jnxDellJFX3500SlotHM,
       "jnxDellJFX3500SlotPower": jnxDellJFX3500SlotPower,
       "jnxDellJFX3500SlotFan": jnxDellJFX3500SlotFan,
       "jnxDellJFX3500SlotFPB": jnxDellJFX3500SlotFPB,
       "jnxSlotEX3300": jnxSlotEX3300,
       "jnxEX3300SlotFPC": jnxEX3300SlotFPC,
       "jnxEX3300SlotPower": jnxEX3300SlotPower,
       "jnxEX3300SlotFan": jnxEX3300SlotFan,
       "jnxSlotDELLJSRX3600": jnxSlotDELLJSRX3600,
       "jnxDELLJSRX3600SlotFPC": jnxDELLJSRX3600SlotFPC,
       "jnxDELLJSRX3600SlotHM": jnxDELLJSRX3600SlotHM,
       "jnxDELLJSRX3600SlotPower": jnxDELLJSRX3600SlotPower,
       "jnxDELLJSRX3600SlotFan": jnxDELLJSRX3600SlotFan,
       "jnxDELLJSRX3600SlotCB": jnxDELLJSRX3600SlotCB,
       "jnxDELLJSRX3600SlotFPB": jnxDELLJSRX3600SlotFPB,
       "jnxSlotDELLJSRX3400": jnxSlotDELLJSRX3400,
       "jnxDELLJSRX3400SlotFPC": jnxDELLJSRX3400SlotFPC,
       "jnxDELLJSRX3400SlotHM": jnxDELLJSRX3400SlotHM,
       "jnxDELLJSRX3400SlotPower": jnxDELLJSRX3400SlotPower,
       "jnxDELLJSRX3400SlotFan": jnxDELLJSRX3400SlotFan,
       "jnxDELLJSRX3400SlotCB": jnxDELLJSRX3400SlotCB,
       "jnxDELLJSRX3400SlotFPB": jnxDELLJSRX3400SlotFPB,
       "jnxSlotDELLJSRX1400": jnxSlotDELLJSRX1400,
       "jnxDELLJSRX1400SlotFPC": jnxDELLJSRX1400SlotFPC,
       "jnxDELLJSRX1400SlotHM": jnxDELLJSRX1400SlotHM,
       "jnxDELLJSRX1400SlotPower": jnxDELLJSRX1400SlotPower,
       "jnxDELLJSRX1400SlotFan": jnxDELLJSRX1400SlotFan,
       "jnxDELLJSRX1400SlotCB": jnxDELLJSRX1400SlotCB,
       "jnxDELLJSRX1400SlotFPB": jnxDELLJSRX1400SlotFPB,
       "jnxSlotDELLJSRX5800": jnxSlotDELLJSRX5800,
       "jnxDELLJSRX5800SlotFPC": jnxDELLJSRX5800SlotFPC,
       "jnxDELLJSRX5800SlotHM": jnxDELLJSRX5800SlotHM,
       "jnxDELLJSRX5800SlotPower": jnxDELLJSRX5800SlotPower,
       "jnxDELLJSRX5800SlotFan": jnxDELLJSRX5800SlotFan,
       "jnxDELLJSRX5800SlotCB": jnxDELLJSRX5800SlotCB,
       "jnxDELLJSRX5800SlotFPB": jnxDELLJSRX5800SlotFPB,
       "jnxSlotDELLJSRX5600": jnxSlotDELLJSRX5600,
       "jnxDELLJSRX5600SlotFPC": jnxDELLJSRX5600SlotFPC,
       "jnxDELLJSRX5600SlotHM": jnxDELLJSRX5600SlotHM,
       "jnxDELLJSRX5600SlotPower": jnxDELLJSRX5600SlotPower,
       "jnxDELLJSRX5600SlotFan": jnxDELLJSRX5600SlotFan,
       "jnxDELLJSRX5600SlotCB": jnxDELLJSRX5600SlotCB,
       "jnxDELLJSRX5600SlotFPB": jnxDELLJSRX5600SlotFPB,
       "jnxSlotQFXSwitch": jnxSlotQFXSwitch,
       "jnxQFXSwitchSlotFPC": jnxQFXSwitchSlotFPC,
       "jnxQFXSwitchSlotHM": jnxQFXSwitchSlotHM,
       "jnxQFXSwitchSlotPower": jnxQFXSwitchSlotPower,
       "jnxQFXSwitchSlotFan": jnxQFXSwitchSlotFan,
       "jnxQFXSwitchSlotFPB": jnxQFXSwitchSlotFPB,
       "jnxQFXSwitchSlotCBD": jnxQFXSwitchSlotCBD,
       "jnxQFXSwitchSlotSIB": jnxQFXSwitchSlotSIB,
       "jnxQFXSwitchSlotFEB": jnxQFXSwitchSlotFEB,
       "jnxSlotT4000": jnxSlotT4000,
       "jnxT4000SlotFPC": jnxT4000SlotFPC,
       "jnxT4000SlotSIB": jnxT4000SlotSIB,
       "jnxT4000SlotHM": jnxT4000SlotHM,
       "jnxT4000SlotSCG": jnxT4000SlotSCG,
       "jnxT4000SlotPower": jnxT4000SlotPower,
       "jnxT4000SlotFan": jnxT4000SlotFan,
       "jnxT4000SlotCB": jnxT4000SlotCB,
       "jnxT4000SlotFPB": jnxT4000SlotFPB,
       "jnxT4000SlotCIP": jnxT4000SlotCIP,
       "jnxT4000SlotSPMB": jnxT4000SlotSPMB,
       "jnxT4000SlotPSD": jnxT4000SlotPSD,
       "jnxSlotSRX550": jnxSlotSRX550,
       "jnxSRX550SlotFPC": jnxSRX550SlotFPC,
       "jnxSRX550SlotRE": jnxSRX550SlotRE,
       "jnxSRX550SlotPower": jnxSRX550SlotPower,
       "jnxSRX550SlotFan": jnxSRX550SlotFan,
       "jnxSlotACX": jnxSlotACX,
       "jnxACXSlotFPC": jnxACXSlotFPC,
       "jnxACXSlotFEB": jnxACXSlotFEB,
       "jnxACXSlotRE": jnxACXSlotRE,
       "jnxACXSlotPower": jnxACXSlotPower,
       "jnxACXSlotFan": jnxACXSlotFan,
       "jnxSlotMX40": jnxSlotMX40,
       "jnxMX40SlotFPC": jnxMX40SlotFPC,
       "jnxMX40SlotCFEB": jnxMX40SlotCFEB,
       "jnxMX40SlotRE": jnxMX40SlotRE,
       "jnxMX40SlotPower": jnxMX40SlotPower,
       "jnxMX40SlotFan": jnxMX40SlotFan,
       "jnxSlotMX10": jnxSlotMX10,
       "jnxMX10SlotFPC": jnxMX10SlotFPC,
       "jnxMX10SlotCFEB": jnxMX10SlotCFEB,
       "jnxMX10SlotRE": jnxMX10SlotRE,
       "jnxMX10SlotPower": jnxMX10SlotPower,
       "jnxMX10SlotFan": jnxMX10SlotFan,
       "jnxSlotMX5": jnxSlotMX5,
       "jnxMX5SlotFPC": jnxMX5SlotFPC,
       "jnxMX5SlotCFEB": jnxMX5SlotCFEB,
       "jnxMX5SlotRE": jnxMX5SlotRE,
       "jnxMX5SlotPower": jnxMX5SlotPower,
       "jnxMX5SlotFan": jnxMX5SlotFan,
       "jnxSlotQFXMInterconnect": jnxSlotQFXMInterconnect,
       "jnxQFXMInterconnectSlotFPC": jnxQFXMInterconnectSlotFPC,
       "jnxQFXMInterconnectSlotHM": jnxQFXMInterconnectSlotHM,
       "jnxQFXMInterconnectSlotPower": jnxQFXMInterconnectSlotPower,
       "jnxQFXMInterconnectSlotFan": jnxQFXMInterconnectSlotFan,
       "jnxQFXMInterconnectSlotFPB": jnxQFXMInterconnectSlotFPB,
       "jnxSlotEX4550": jnxSlotEX4550,
       "jnxEX4550SlotFPC": jnxEX4550SlotFPC,
       "jnxEX4550SlotPower": jnxEX4550SlotPower,
       "jnxEX4550SlotFan": jnxEX4550SlotFan,
       "jnxEX4550SlotRE": jnxEX4550SlotRE,
       "jnxSlotMX2020": jnxSlotMX2020,
       "jnxMX2020SlotSFB": jnxMX2020SlotSFB,
       "jnxMX2020SlotHM": jnxMX2020SlotHM,
       "jnxMX2020SlotFPC": jnxMX2020SlotFPC,
       "jnxMX2020SlotFan": jnxMX2020SlotFan,
       "jnxMX2020SlotCB": jnxMX2020SlotCB,
       "jnxMX2020SlotFPB": jnxMX2020SlotFPB,
       "jnxMX2020SlotSPMB": jnxMX2020SlotSPMB,
       "jnxMX2020SlotPDM": jnxMX2020SlotPDM,
       "jnxMX2020SlotPSM": jnxMX2020SlotPSM,
       "jnxMX2020SlotADC": jnxMX2020SlotADC,
       "jnxSlotVseries": jnxSlotVseries,
       "jnxVseriesSlotFPC": jnxVseriesSlotFPC,
       "jnxVseriesSlotRE": jnxVseriesSlotRE,
       "jnxVseriesSlotPower": jnxVseriesSlotPower,
       "jnxVseriesSlotFan": jnxVseriesSlotFan,
       "jnxSlotLN2600": jnxSlotLN2600,
       "jnxLN2600SlotFPC": jnxLN2600SlotFPC,
       "jnxLN2600SlotRE": jnxLN2600SlotRE,
       "jnxLN2600SlotPower": jnxLN2600SlotPower,
       "jnxLN2600SlotFan": jnxLN2600SlotFan,
       "jnxSlotFireflyPerimeter": jnxSlotFireflyPerimeter,
       "jnxFireflyPerimeterSlotFPC": jnxFireflyPerimeterSlotFPC,
       "jnxFireflyPerimeterSlotRE": jnxFireflyPerimeterSlotRE,
       "jnxFireflyPerimeterSlotPower": jnxFireflyPerimeterSlotPower,
       "jnxFireflyPerimeterSlotFan": jnxFireflyPerimeterSlotFan,
       "jnxSlotMX104": jnxSlotMX104,
       "jnxMX104SlotFPC": jnxMX104SlotFPC,
       "jnxMX104SlotAFEB": jnxMX104SlotAFEB,
       "jnxMX104SlotRE": jnxMX104SlotRE,
       "jnxMX104SlotPower": jnxMX104SlotPower,
       "jnxMX104SlotFan": jnxMX104SlotFan,
       "jnxMX104SlotFPM": jnxMX104SlotFPM,
       "jnxSlotPTX3000": jnxSlotPTX3000,
       "jnxPTX3000SlotSIB": jnxPTX3000SlotSIB,
       "jnxPTX3000SlotHM": jnxPTX3000SlotHM,
       "jnxPTX3000SlotFPC": jnxPTX3000SlotFPC,
       "jnxPTX3000SlotFan": jnxPTX3000SlotFan,
       "jnxPTX3000SlotCB": jnxPTX3000SlotCB,
       "jnxPTX3000SlotFPB": jnxPTX3000SlotFPB,
       "jnxPTX3000SlotPSM": jnxPTX3000SlotPSM,
       "jnxPTX3000SlotPIC": jnxPTX3000SlotPIC,
       "jnxSlotMX2010": jnxSlotMX2010,
       "jnxMX2010SlotSFB": jnxMX2010SlotSFB,
       "jnxMX2010SlotHM": jnxMX2010SlotHM,
       "jnxMX2010SlotFPC": jnxMX2010SlotFPC,
       "jnxMX2010SlotFan": jnxMX2010SlotFan,
       "jnxMX2010SlotCB": jnxMX2010SlotCB,
       "jnxMX2010SlotFPB": jnxMX2010SlotFPB,
       "jnxMX2010SlotSPMB": jnxMX2010SlotSPMB,
       "jnxMX2010SlotPDM": jnxMX2010SlotPDM,
       "jnxMX2010SlotPSM": jnxMX2010SlotPSM,
       "jnxMX2010SlotADC": jnxMX2010SlotADC,
       "jnxSlotQFX3100": jnxSlotQFX3100,
       "jnxQFX3100SlotCPU": jnxQFX3100SlotCPU,
       "jnxQFX3100SlotMemory": jnxQFX3100SlotMemory,
       "jnxQFX3100SlotPower": jnxQFX3100SlotPower,
       "jnxQFX3100SlotFan": jnxQFX3100SlotFan,
       "jnxQFX3100SlotHardDisk": jnxQFX3100SlotHardDisk,
       "jnxQFX3100SlotNIC": jnxQFX3100SlotNIC,
       "jnxSlotLN2800": jnxSlotLN2800,
       "jnxLN2800SlotFPC": jnxLN2800SlotFPC,
       "jnxLN2800SlotRE": jnxLN2800SlotRE,
       "jnxLN2800SlotPower": jnxLN2800SlotPower,
       "jnxLN2800SlotFan": jnxLN2800SlotFan,
       "jnxSlotEX9214": jnxSlotEX9214,
       "jnxEX9214SlotFPC": jnxEX9214SlotFPC,
       "jnxEX9214SlotHM": jnxEX9214SlotHM,
       "jnxEX9214SlotPower": jnxEX9214SlotPower,
       "jnxEX9214SlotFan": jnxEX9214SlotFan,
       "jnxEX9214SlotCB": jnxEX9214SlotCB,
       "jnxEX9214SlotFPB": jnxEX9214SlotFPB,
       "jnxSlotEX9208": jnxSlotEX9208,
       "jnxEX9208SlotFPC": jnxEX9208SlotFPC,
       "jnxEX9208SlotHM": jnxEX9208SlotHM,
       "jnxEX9208SlotPower": jnxEX9208SlotPower,
       "jnxEX9208SlotFan": jnxEX9208SlotFan,
       "jnxEX9208SlotCB": jnxEX9208SlotCB,
       "jnxEX9208SlotFPB": jnxEX9208SlotFPB,
       "jnxSlotEX9204": jnxSlotEX9204,
       "jnxEX9204SlotFPC": jnxEX9204SlotFPC,
       "jnxEX9204SlotHM": jnxEX9204SlotHM,
       "jnxEX9204SlotPower": jnxEX9204SlotPower,
       "jnxEX9204SlotFan": jnxEX9204SlotFan,
       "jnxEX9204SlotCB": jnxEX9204SlotCB,
       "jnxEX9204SlotFPB": jnxEX9204SlotFPB,
       "jnxSlotSRX5400": jnxSlotSRX5400,
       "jnxSRX5400SlotFPC": jnxSRX5400SlotFPC,
       "jnxSRX5400SlotHM": jnxSRX5400SlotHM,
       "jnxSRX5400SlotPower": jnxSRX5400SlotPower,
       "jnxSRX5400SlotFan": jnxSRX5400SlotFan,
       "jnxSRX5400SlotCB": jnxSRX5400SlotCB,
       "jnxSRX5400SlotFPB": jnxSRX5400SlotFPB,
       "jnxSlotIBM4274S54J54S": jnxSlotIBM4274S54J54S,
       "jnxIBM4274S54J54SSlotFPC": jnxIBM4274S54J54SSlotFPC,
       "jnxIBM4274S54J54SSlotHM": jnxIBM4274S54J54SSlotHM,
       "jnxIBM4274S54J54SSlotPower": jnxIBM4274S54J54SSlotPower,
       "jnxIBM4274S54J54SSlotFan": jnxIBM4274S54J54SSlotFan,
       "jnxIBM4274S54J54SSlotCB": jnxIBM4274S54J54SSlotCB,
       "jnxIBM4274S54J54SSlotFPB": jnxIBM4274S54J54SSlotFPB,
       "jnxSlotDELLJSRX5400": jnxSlotDELLJSRX5400,
       "jnxDELLJSRX5400SlotFPC": jnxDELLJSRX5400SlotFPC,
       "jnxDELLJSRX5400SlotHM": jnxDELLJSRX5400SlotHM,
       "jnxDELLJSRX5400SlotPower": jnxDELLJSRX5400SlotPower,
       "jnxDELLJSRX5400SlotFan": jnxDELLJSRX5400SlotFan,
       "jnxDELLJSRX5400SlotCB": jnxDELLJSRX5400SlotCB,
       "jnxDELLJSRX5400SlotFPB": jnxDELLJSRX5400SlotFPB,
       "jnxSlotVMX": jnxSlotVMX,
       "jnxVMXSlotFPC": jnxVMXSlotFPC,
       "jnxVMxSlotPower": jnxVMxSlotPower,
       "jnxVMXSlotFan": jnxVMXSlotFan,
       "jnxVMXSlotCB": jnxVMXSlotCB,
       "jnxVMXSlotHM": jnxVMXSlotHM,
       "jnxSlotEX4600": jnxSlotEX4600,
       "jnxEX4600SlotFPC": jnxEX4600SlotFPC,
       "jnxEX4600HM": jnxEX4600HM,
       "jnxEX4600SlotPower": jnxEX4600SlotPower,
       "jnxEX4600SlotFan": jnxEX4600SlotFan,
       "jnxSlotVRR": jnxSlotVRR,
       "jnxVRRSlotFPC": jnxVRRSlotFPC,
       "jnxVRRSlotRE": jnxVRRSlotRE,
       "jnxVRRSlotPower": jnxVRRSlotPower,
       "jnxVRRSlotFan": jnxVRRSlotFan,
       "jnxVRRSlotHM": jnxVRRSlotHM,
       "jnxVRRSlotCB": jnxVRRSlotCB,
       "jnxVRRSlotFPB": jnxVRRSlotFPB,
       "jnxSlotACX1000": jnxSlotACX1000,
       "jnxACX1000SlotFPC": jnxACX1000SlotFPC,
       "jnxACX1000SlotFEB": jnxACX1000SlotFEB,
       "jnxACX1000SlotRE": jnxACX1000SlotRE,
       "jnxACX1000SlotPower": jnxACX1000SlotPower,
       "jnxSlotACX2000": jnxSlotACX2000,
       "jnxACX2000SlotFPC": jnxACX2000SlotFPC,
       "jnxACX2000SlotFEB": jnxACX2000SlotFEB,
       "jnxACX2000SlotRE": jnxACX2000SlotRE,
       "jnxACX2000SlotPower": jnxACX2000SlotPower,
       "jnxSlotACX1100": jnxSlotACX1100,
       "jnxACX1100SlotFPC": jnxACX1100SlotFPC,
       "jnxACX1100SlotFEB": jnxACX1100SlotFEB,
       "jnxACX1100SlotRE": jnxACX1100SlotRE,
       "jnxACX1100SlotPower": jnxACX1100SlotPower,
       "jnxSlotACX2100": jnxSlotACX2100,
       "jnxACX2100SlotFPC": jnxACX2100SlotFPC,
       "jnxACX2100SlotFEB": jnxACX2100SlotFEB,
       "jnxACX2100SlotRE": jnxACX2100SlotRE,
       "jnxACX2100SlotPower": jnxACX2100SlotPower,
       "jnxSlotACX2200": jnxSlotACX2200,
       "jnxACX2200SlotFPC": jnxACX2200SlotFPC,
       "jnxACX2200SlotFEB": jnxACX2200SlotFEB,
       "jnxACX2200SlotRE": jnxACX2200SlotRE,
       "jnxACX2200SlotPower": jnxACX2200SlotPower,
       "jnxSlotACX4000": jnxSlotACX4000,
       "jnxACX4000SlotFPC": jnxACX4000SlotFPC,
       "jnxACX4000SlotFEB": jnxACX4000SlotFEB,
       "jnxACX4000SlotRE": jnxACX4000SlotRE,
       "jnxACX4000SlotPower": jnxACX4000SlotPower,
       "jnxACX4000SlotFan": jnxACX4000SlotFan,
       "jnxSlotACX500AC": jnxSlotACX500AC,
       "jnxACX500ACSlotFPC": jnxACX500ACSlotFPC,
       "jnxACX500ACSlotFEB": jnxACX500ACSlotFEB,
       "jnxACX500ACSlotRE": jnxACX500ACSlotRE,
       "jnxACX500ACSlotPower": jnxACX500ACSlotPower,
       "jnxSlotACX500DC": jnxSlotACX500DC,
       "jnxACX500DCSlotFPC": jnxACX500DCSlotFPC,
       "jnxACX500DCSlotFEB": jnxACX500DCSlotFEB,
       "jnxACX500DCSlotRE": jnxACX500DCSlotRE,
       "jnxACX500DCSlotPower": jnxACX500DCSlotPower,
       "jnxSlotACX500OAC": jnxSlotACX500OAC,
       "jnxACX500OACSlotFPC": jnxACX500OACSlotFPC,
       "jnxACX500OACSlotFEB": jnxACX500OACSlotFEB,
       "jnxACX500OACSlotRE": jnxACX500OACSlotRE,
       "jnxACX500OACSlotPower": jnxACX500OACSlotPower,
       "jnxSlotACX500ODC": jnxSlotACX500ODC,
       "jnxACX500ODCSlotFPC": jnxACX500ODCSlotFPC,
       "jnxACX500ODCSlotFEB": jnxACX500ODCSlotFEB,
       "jnxACX500ODCSlotRE": jnxACX500ODCSlotRE,
       "jnxACX500ODCSlotPower": jnxACX500ODCSlotPower,
       "jnxSlotACX500OPOEAC": jnxSlotACX500OPOEAC,
       "jnxACX500OPOEACSlotFPC": jnxACX500OPOEACSlotFPC,
       "jnxACX500OPOEACSlotFEB": jnxACX500OPOEACSlotFEB,
       "jnxACX500OPOEACSlotRE": jnxACX500OPOEACSlotRE,
       "jnxACX500OPOEACSlotPower": jnxACX500OPOEACSlotPower,
       "jnxSlotACX500OPOEDC": jnxSlotACX500OPOEDC,
       "jnxACX500OPOEDCSlotFPC": jnxACX500OPOEDCSlotFPC,
       "jnxACX500OPOEDCSlotFEB": jnxACX500OPOEDCSlotFEB,
       "jnxACX500OPOEDCSlotRE": jnxACX500OPOEDCSlotRE,
       "jnxACX500OPOEDCSlotPower": jnxACX500OPOEDCSlotPower,
       "jnxSlotSatelliteDevice": jnxSlotSatelliteDevice,
       "jnxSatelliteDeviceSlotFPC": jnxSatelliteDeviceSlotFPC,
       "jnxSatelliteDeviceSlotPower": jnxSatelliteDeviceSlotPower,
       "jnxSatelliteDeviceSlotFan": jnxSatelliteDeviceSlotFan,
       "jnxSlotACX5048": jnxSlotACX5048,
       "jnxACX5048SlotFPC": jnxACX5048SlotFPC,
       "jnxACX5048SlotHM": jnxACX5048SlotHM,
       "jnxACX5048SlotPower": jnxACX5048SlotPower,
       "jnxACX5048SlotFan": jnxACX5048SlotFan,
       "jnxACX5048SlotFPB": jnxACX5048SlotFPB,
       "jnxSlotACX5096": jnxSlotACX5096,
       "jnxACX5096SlotFPC": jnxACX5096SlotFPC,
       "jnxACX5096SlotHM": jnxACX5096SlotHM,
       "jnxACX5096SlotPower": jnxACX5096SlotPower,
       "jnxACX5096SlotFan": jnxACX5096SlotFan,
       "jnxACX5096SlotFPB": jnxACX5096SlotFPB,
       "jnxSlotLN1000CC": jnxSlotLN1000CC,
       "jnxLN1000CCSlotFPC": jnxLN1000CCSlotFPC,
       "jnxLN1000CCSlotRE": jnxLN1000CCSlotRE,
       "jnxLN1000CCSlotPower": jnxLN1000CCSlotPower,
       "jnxLN1000CCSlotFan": jnxLN1000CCSlotFan,
       "jnxSlotVSRX": jnxSlotVSRX,
       "jnxVSRXSlotFPC": jnxVSRXSlotFPC,
       "jnxVSRXSlotRE": jnxVSRXSlotRE,
       "jnxVSRXSlotPower": jnxVSRXSlotPower,
       "jnxVSRXSlotFan": jnxVSRXSlotFan,
       "jnxSlotPTX1000": jnxSlotPTX1000,
       "jnxPTX1000SlotFPC": jnxPTX1000SlotFPC,
       "jnxPTX1000SlotHM": jnxPTX1000SlotHM,
       "jnxPTX1000SlotPower": jnxPTX1000SlotPower,
       "jnxPTX1000SlotFan": jnxPTX1000SlotFan,
       "jnxPTX1000SlotFPB": jnxPTX1000SlotFPB,
       "jnxSlotEX3400": jnxSlotEX3400,
       "jnxEX3400SlotFPC": jnxEX3400SlotFPC,
       "jnxEX3400SlotPower": jnxEX3400SlotPower,
       "jnxEX3400SlotFan": jnxEX3400SlotFan,
       "jnxSlotEX2300": jnxSlotEX2300,
       "jnxEX2300SlotFPC": jnxEX2300SlotFPC,
       "jnxEX2300SlotPower": jnxEX2300SlotPower,
       "jnxEX2300SlotFan": jnxEX2300SlotFan,
       "jnxSlotSRX300": jnxSlotSRX300,
       "jnxSRX300SlotFPC": jnxSRX300SlotFPC,
       "jnxSRX300SlotRE": jnxSRX300SlotRE,
       "jnxSRX300SlotPower": jnxSRX300SlotPower,
       "jnxSRX300SlotFan": jnxSRX300SlotFan,
       "jnxSlotSRX320": jnxSlotSRX320,
       "jnxSRX320SlotFPC": jnxSRX320SlotFPC,
       "jnxSRX320SlotRE": jnxSRX320SlotRE,
       "jnxSRX320SlotPower": jnxSRX320SlotPower,
       "jnxSRX320SlotFan": jnxSRX320SlotFan,
       "jnxSlotSRX340": jnxSlotSRX340,
       "jnxSRX340SlotFPC": jnxSRX340SlotFPC,
       "jnxSRX340SlotRE": jnxSRX340SlotRE,
       "jnxSRX340SlotPower": jnxSRX340SlotPower,
       "jnxSRX340SlotFan": jnxSRX340SlotFan,
       "jnxSlotSRX345": jnxSlotSRX345,
       "jnxSRX345SlotFPC": jnxSRX345SlotFPC,
       "jnxSRX345SlotRE": jnxSRX345SlotRE,
       "jnxSRX345SlotPower": jnxSRX345SlotPower,
       "jnxSRX345SlotFan": jnxSRX345SlotFan,
       "jnxSlotSRX1500": jnxSlotSRX1500,
       "jnxSRX1500SlotFPC": jnxSRX1500SlotFPC,
       "jnxSRX1500SlotRE": jnxSRX1500SlotRE,
       "jnxSRX1500SlotPower": jnxSRX1500SlotPower,
       "jnxSRX1500SlotFan": jnxSRX1500SlotFan,
       "jnxSRX1500SlotCB": jnxSRX1500SlotCB,
       "jnxSlotNFX": jnxSlotNFX,
       "jnxNFXSlotFPC": jnxNFXSlotFPC,
       "jnxNFXSlotPIC": jnxNFXSlotPIC,
       "jnxNFXSlotHM": jnxNFXSlotHM,
       "jnxNFXSlotPower": jnxNFXSlotPower,
       "jnxNFXSlotFan": jnxNFXSlotFan,
       "jnxSlotJNP10003": jnxSlotJNP10003,
       "jnxJNP10003SlotHM": jnxJNP10003SlotHM,
       "jnxJNP10003SlotFPC": jnxJNP10003SlotFPC,
       "jnxJNP10003SlotFan": jnxJNP10003SlotFan,
       "jnxJNP10003SlotCB": jnxJNP10003SlotCB,
       "jnxJNP10003SlotPower": jnxJNP10003SlotPower,
       "jnxSlotSRX4600": jnxSlotSRX4600,
       "jnxSRX4600SlotHM": jnxSRX4600SlotHM,
       "jnxSRX4600SlotFPC": jnxSRX4600SlotFPC,
       "jnxSRX4600SlotFan": jnxSRX4600SlotFan,
       "jnxSRX4600SlotSPMB": jnxSRX4600SlotSPMB,
       "jnxSRX4600SlotPSM": jnxSRX4600SlotPSM,
       "jnxSlotSRX4800": jnxSlotSRX4800,
       "jnxSRX4800SlotHM": jnxSRX4800SlotHM,
       "jnxSRX4800SlotFPC": jnxSRX4800SlotFPC,
       "jnxSRX4800SlotFan": jnxSRX4800SlotFan,
       "jnxSRX4800SlotSPMB": jnxSRX4800SlotSPMB,
       "jnxSRX4800SlotPSM": jnxSRX4800SlotPSM,
       "jnxSlotSRX4100": jnxSlotSRX4100,
       "jnxSRX4100SlotFPC": jnxSRX4100SlotFPC,
       "jnxSRX4100SlotRE": jnxSRX4100SlotRE,
       "jnxSRX4100SlotPower": jnxSRX4100SlotPower,
       "jnxSRX4100SlotFan": jnxSRX4100SlotFan,
       "jnxSlotSRX4200": jnxSlotSRX4200,
       "jnxSRX4200SlotFPC": jnxSRX4200SlotFPC,
       "jnxSRX4200SlotRE": jnxSRX4200SlotRE,
       "jnxSRX4200SlotPower": jnxSRX4200SlotPower,
       "jnxSRX4200SlotFan": jnxSRX4200SlotFan,
       "jnxSlotJNP204": jnxSlotJNP204,
       "jnxJNP204SlotHM": jnxJNP204SlotHM,
       "jnxJNP204SlotFPC": jnxJNP204SlotFPC,
       "jnxJNP204SlotFan": jnxJNP204SlotFan,
       "jnxJNP204SlotCB": jnxJNP204SlotCB,
       "jnxJNP204SlotPower": jnxJNP204SlotPower,
       "jnxSlotMX2008": jnxSlotMX2008,
       "jnxMX2008SlotSFB": jnxMX2008SlotSFB,
       "jnxMX2008SlotHM": jnxMX2008SlotHM,
       "jnxMX2008SlotFPC": jnxMX2008SlotFPC,
       "jnxMX2008SlotFan": jnxMX2008SlotFan,
       "jnxMX2008SlotRCB": jnxMX2008SlotRCB,
       "jnxMX2008SlotFPB": jnxMX2008SlotFPB,
       "jnxMX2008SlotPDM": jnxMX2008SlotPDM,
       "jnxMX2008SlotPSM": jnxMX2008SlotPSM,
       "jnxMX2008SlotADC": jnxMX2008SlotADC,
       "jnxSlotMXTSR80": jnxSlotMXTSR80,
       "jnxMXTSR80SlotFPC": jnxMXTSR80SlotFPC,
       "jnxMXTSR80SlotAFEB": jnxMXTSR80SlotAFEB,
       "jnxMXTSR80SlotRE": jnxMXTSR80SlotRE,
       "jnxMXTSR80SlotPower": jnxMXTSR80SlotPower,
       "jnxMXTSR80SlotFan": jnxMXTSR80SlotFan,
       "jnxMXTSR80SlotFPM": jnxMXTSR80SlotFPM,
       "jnxSlotPTX10008": jnxSlotPTX10008,
       "jnxPTX10008SlotFPC": jnxPTX10008SlotFPC,
       "jnxPTX10008SlotHM": jnxPTX10008SlotHM,
       "jnxPTX10008SlotPower": jnxPTX10008SlotPower,
       "jnxPTX10008SlotFan": jnxPTX10008SlotFan,
       "jnxPTX10008SlotFPB": jnxPTX10008SlotFPB,
       "jnxPTX10008SlotCBD": jnxPTX10008SlotCBD,
       "jnxPTX10008SlotSIB": jnxPTX10008SlotSIB,
       "jnxPTX10008SlotFPM": jnxPTX10008SlotFPM,
       "jnxPTX10008SlotFTC": jnxPTX10008SlotFTC,
       "jnxPTX10008SlotBackplane": jnxPTX10008SlotBackplane,
       "jnxSlotACX5448": jnxSlotACX5448,
       "jnxACX5448SlotFPC": jnxACX5448SlotFPC,
       "jnxACX5448SlotFEB": jnxACX5448SlotFEB,
       "jnxACX5448SlotRE": jnxACX5448SlotRE,
       "jnxACX5448SlotPower": jnxACX5448SlotPower,
       "jnxACX5448SlotFan": jnxACX5448SlotFan,
       "jnxSlotPTX10016": jnxSlotPTX10016,
       "jnxPTX10016SlotFPC": jnxPTX10016SlotFPC,
       "jnxPTX10016SlotHM": jnxPTX10016SlotHM,
       "jnxPTX10016SlotPower": jnxPTX10016SlotPower,
       "jnxPTX10016SlotFan": jnxPTX10016SlotFan,
       "jnxPTX10016SlotFPB": jnxPTX10016SlotFPB,
       "jnxPTX10016SlotCBD": jnxPTX10016SlotCBD,
       "jnxPTX10016SlotSIB": jnxPTX10016SlotSIB,
       "jnxPTX10016SlotFTC": jnxPTX10016SlotFTC,
       "jnxPTX10016SlotBackplane": jnxPTX10016SlotBackplane,
       "jnxSlotEX9251": jnxSlotEX9251,
       "jnxEX9251SlotHM": jnxEX9251SlotHM,
       "jnxEX9251SlotFPC": jnxEX9251SlotFPC,
       "jnxEX9251SlotFan": jnxEX9251SlotFan,
       "jnxEX9251SlotCB": jnxEX9251SlotCB,
       "jnxEX9251SlotPower": jnxEX9251SlotPower,
       "jnxSlotMX150": jnxSlotMX150,
       "jnxMX150SlotFPC": jnxMX150SlotFPC,
       "jnxMX150SlotPower": jnxMX150SlotPower,
       "jnxMX150SlotFan": jnxMX150SlotFan,
       "jnxMX150SlotCB": jnxMX150SlotCB,
       "jnxMX150SlotHM": jnxMX150SlotHM,
       "jnxSlotJNP10001": jnxSlotJNP10001,
       "jnxJNP10001SlotHM": jnxJNP10001SlotHM,
       "jnxJNP10001SlotFPC": jnxJNP10001SlotFPC,
       "jnxJNP10001SlotFan": jnxJNP10001SlotFan,
       "jnxJNP10001SlotPower": jnxJNP10001SlotPower,
       "jnxSlotMX10008": jnxSlotMX10008,
       "jnxMX10008SlotFPC": jnxMX10008SlotFPC,
       "jnxMX10008SlotHM": jnxMX10008SlotHM,
       "jnxMX10008SlotPower": jnxMX10008SlotPower,
       "jnxMX10008SlotFan": jnxMX10008SlotFan,
       "jnxMX10008SlotFPB": jnxMX10008SlotFPB,
       "jnxMX10008SlotCBD": jnxMX10008SlotCBD,
       "jnxMX10008SlotSFB": jnxMX10008SlotSFB,
       "jnxMX10008SlotFTC": jnxMX10008SlotFTC,
       "jnxSlotMX10016": jnxSlotMX10016,
       "jnxMX10016SlotFPC": jnxMX10016SlotFPC,
       "jnxMX10016SlotHM": jnxMX10016SlotHM,
       "jnxMX10016SlotPower": jnxMX10016SlotPower,
       "jnxMX10016SlotFan": jnxMX10016SlotFan,
       "jnxMX10016SlotFPB": jnxMX10016SlotFPB,
       "jnxMX10016SlotCBD": jnxMX10016SlotCBD,
       "jnxMX10016SlotSFB": jnxMX10016SlotSFB,
       "jnxMX10016SlotFTC": jnxMX10016SlotFTC,
       "jnxSlotEX9253": jnxSlotEX9253,
       "jnxEX9253SlotHM": jnxEX9253SlotHM,
       "jnxEX9253SlotFPC": jnxEX9253SlotFPC,
       "jnxEX9253SlotFan": jnxEX9253SlotFan,
       "jnxEX9253SlotCB": jnxEX9253SlotCB,
       "jnxEX9253SlotPower": jnxEX9253SlotPower,
       "jnxSlotJRR200": jnxSlotJRR200,
       "jnxJRR200SlotRE": jnxJRR200SlotRE,
       "jnxJRR200SlotPower": jnxJRR200SlotPower,
       "jnxJRR200SlotFan": jnxJRR200SlotFan,
       "jnxSlotACX5448M": jnxSlotACX5448M,
       "jnxACX5448MSlotFPC": jnxACX5448MSlotFPC,
       "jnxACX5448MSlotFEB": jnxACX5448MSlotFEB,
       "jnxACX5448MSlotRE": jnxACX5448MSlotRE,
       "jnxACX5448MSlotPower": jnxACX5448MSlotPower,
       "jnxACX5448MSlotFan": jnxACX5448MSlotFan,
       "jnxSlotACX5448D": jnxSlotACX5448D,
       "jnxACX5448DSlotFPC": jnxACX5448DSlotFPC,
       "jnxACX5448DSlotFEB": jnxACX5448DSlotFEB,
       "jnxACX5448DSlotRE": jnxACX5448DSlotRE,
       "jnxACX5448DSlotPower": jnxACX5448DSlotPower,
       "jnxACX5448DSlotFan": jnxACX5448DSlotFan,
       "jnxSlotACX6360OR": jnxSlotACX6360OR,
       "jnxACX6360ORSlotHM": jnxACX6360ORSlotHM,
       "jnxACX6360ORSlotFPC": jnxACX6360ORSlotFPC,
       "jnxACX6360ORSlotFan": jnxACX6360ORSlotFan,
       "jnxACX6360ORSlotPower": jnxACX6360ORSlotPower,
       "jnxSlotACX6360OX": jnxSlotACX6360OX,
       "jnxACX6360OXSlotHM": jnxACX6360OXSlotHM,
       "jnxACX6360OXSlotFPC": jnxACX6360OXSlotFPC,
       "jnxACX6360OXSlotFan": jnxACX6360OXSlotFan,
       "jnxACX6360OXSlotPower": jnxACX6360OXSlotPower,
       "jnxSlotACX710": jnxSlotACX710,
       "jnxACX710SlotFPC": jnxACX710SlotFPC,
       "jnxACX710SlotRE": jnxACX710SlotRE,
       "jnxACX710SlotPower": jnxACX710SlotPower,
       "jnxACX710SlotFan": jnxACX710SlotFan,
       "jnxSlotACX5800": jnxSlotACX5800,
       "jnxACX5800SlotFPC": jnxACX5800SlotFPC,
       "jnxACX5800SlotFEB": jnxACX5800SlotFEB,
       "jnxACX5800SlotRE": jnxACX5800SlotRE,
       "jnxACX5800SlotPower": jnxACX5800SlotPower,
       "jnxSlotSRX380": jnxSlotSRX380,
       "jnxSRX380SlotFPC": jnxSRX380SlotFPC,
       "jnxSRX380SlotRE": jnxSRX380SlotRE,
       "jnxSRX380SlotPower": jnxSRX380SlotPower,
       "jnxSRX380SlotFan": jnxSRX380SlotFan,
       "jnxSlotEX4400": jnxSlotEX4400,
       "jnxEX4400SlotFPC": jnxEX4400SlotFPC,
       "jnxEX4400SlotPower": jnxEX4400SlotPower,
       "jnxEX4400SlotFan": jnxEX4400SlotFan,
       "jnxSlotR6675": jnxSlotR6675,
       "jnxR6675SlotFPC": jnxR6675SlotFPC,
       "jnxR6675SlotRE": jnxR6675SlotRE,
       "jnxR6675SlotPower": jnxR6675SlotPower,
       "jnxR6675SlotFan": jnxR6675SlotFan,
       "jnxSlotMX304": jnxSlotMX304,
       "jnxMX304SlotHM": jnxMX304SlotHM,
       "jnxMX304SlotFPC": jnxMX304SlotFPC,
       "jnxMX304SlotFan": jnxMX304SlotFan,
       "jnxMX304SlotPower": jnxMX304SlotPower,
       "jnxMX304SlotPMB": jnxMX304SlotPMB,
       "jnxMX304SlotSFB": jnxMX304SlotSFB,
       "jnxMX304SlotTIB": jnxMX304SlotTIB,
       "jnxMX304SlotCBD": jnxMX304SlotCBD,
       "jnxSlotMX10004": jnxSlotMX10004,
       "jnxMX10004SlotFPC": jnxMX10004SlotFPC,
       "jnxMX10004SlotHM": jnxMX10004SlotHM,
       "jnxMX10004SlotPower": jnxMX10004SlotPower,
       "jnxMX10004SlotFan": jnxMX10004SlotFan,
       "jnxMX10004SlotFPB": jnxMX10004SlotFPB,
       "jnxMX10004SlotCBD": jnxMX10004SlotCBD,
       "jnxMX10004SlotSFB": jnxMX10004SlotSFB,
       "jnxMX10004SlotFTC": jnxMX10004SlotFTC,
       "jnxSlotEX4100": jnxSlotEX4100,
       "jnxEX4100SlotFPC": jnxEX4100SlotFPC,
       "jnxEX4100SlotPower": jnxEX4100SlotPower,
       "jnxEX4100SlotFan": jnxEX4100SlotFan,
       "jnxSlotEX4650": jnxSlotEX4650,
       "jnxEX4650SlotFPC": jnxEX4650SlotFPC,
       "jnxEX4650SlotHM": jnxEX4650SlotHM,
       "jnxEX4650SlotPower": jnxEX4650SlotPower,
       "jnxEX4650SlotFan": jnxEX4650SlotFan,
       "jnxEX4650SlotRE": jnxEX4650SlotRE,
       "jnxSlotPTX1000260C": jnxSlotPTX1000260C,
       "jnxPTX1000260CSlotFPC": jnxPTX1000260CSlotFPC,
       "jnxPTX1000260CSlotHM": jnxPTX1000260CSlotHM,
       "jnxPTX1000260CSlotPower": jnxPTX1000260CSlotPower,
       "jnxPTX1000260CSlotFan": jnxPTX1000260CSlotFan,
       "jnxPTX1000260CSlotFPB": jnxPTX1000260CSlotFPB,
       "jnxSlotPTX1000380c": jnxSlotPTX1000380c,
       "jnxPTX1000380cSlotRE": jnxPTX1000380cSlotRE,
       "jnxPTX1000380cSlotCB": jnxPTX1000380cSlotCB,
       "jnxPTX1000380cSlotFPC": jnxPTX1000380cSlotFPC,
       "jnxPTX1000380cSlotFan": jnxPTX1000380cSlotFan,
       "jnxPTX1000380cSlotFPM": jnxPTX1000380cSlotFPM,
       "jnxPTX1000380cSlotSIB": jnxPTX1000380cSlotSIB,
       "jnxPTX1000380cSlotPIC": jnxPTX1000380cSlotPIC,
       "jnxPTX1000380cSlotPDU": jnxPTX1000380cSlotPDU,
       "jnxPTX1000380cSlotPSM": jnxPTX1000380cSlotPSM,
       "jnxSlotPTX10003160c": jnxSlotPTX10003160c,
       "jnxPTX10003160cSlotRE": jnxPTX10003160cSlotRE,
       "jnxPTX10003160cSlotCB": jnxPTX10003160cSlotCB,
       "jnxPTX10003160cSlotFPC": jnxPTX10003160cSlotFPC,
       "jnxPTX10003160cSlotFan": jnxPTX10003160cSlotFan,
       "jnxPTX10003160cSlotFPM": jnxPTX10003160cSlotFPM,
       "jnxPTX10003160cSlotSIB": jnxPTX10003160cSlotSIB,
       "jnxPTX10003160cSlotPIC": jnxPTX10003160cSlotPIC,
       "jnxPTX10003160cSlotPDU": jnxPTX10003160cSlotPDU,
       "jnxPTX10003160cSlotPSM": jnxPTX10003160cSlotPSM,
       "jnxSlotQFX1000380c": jnxSlotQFX1000380c,
       "jnxQFX1000380cSlotRE": jnxQFX1000380cSlotRE,
       "jnxQFX1000380cSlotCB": jnxQFX1000380cSlotCB,
       "jnxQFX1000380cSlotFPC": jnxQFX1000380cSlotFPC,
       "jnxQFX1000380cSlotFan": jnxQFX1000380cSlotFan,
       "jnxQFX1000380cSlotFPM": jnxQFX1000380cSlotFPM,
       "jnxQFX1000380cSlotSIB": jnxQFX1000380cSlotSIB,
       "jnxQFX1000380cSlotPIC": jnxQFX1000380cSlotPIC,
       "jnxQFX1000380cSlotPDU": jnxQFX1000380cSlotPDU,
       "jnxQFX1000380cSlotPSM": jnxQFX1000380cSlotPSM,
       "jnxSlotQFX10003160c": jnxSlotQFX10003160c,
       "jnxQFX10003160cSlotRE": jnxQFX10003160cSlotRE,
       "jnxQFX10003160cSlotCB": jnxQFX10003160cSlotCB,
       "jnxQFX10003160cSlotFPC": jnxQFX10003160cSlotFPC,
       "jnxQFX10003160cSlotFan": jnxQFX10003160cSlotFan,
       "jnxQFX10003160cSlotFPM": jnxQFX10003160cSlotFPM,
       "jnxQFX10003160cSlotSIB": jnxQFX10003160cSlotSIB,
       "jnxQFX10003160cSlotPIC": jnxQFX10003160cSlotPIC,
       "jnxQFX10003160cSlotPDU": jnxQFX10003160cSlotPDU,
       "jnxQFX10003160cSlotPSM": jnxQFX10003160cSlotPSM,
       "jnxSlotPTX1000136mr": jnxSlotPTX1000136mr,
       "jnxPTX1000136mrSlotRE": jnxPTX1000136mrSlotRE,
       "jnxPTX1000136mrSlotCB": jnxPTX1000136mrSlotCB,
       "jnxPTX1000136mrSlotFPC": jnxPTX1000136mrSlotFPC,
       "jnxPTX1000136mrSlotFan": jnxPTX1000136mrSlotFan,
       "jnxPTX1000136mrSlotSIB": jnxPTX1000136mrSlotSIB,
       "jnxPTX1000136mrSlotPIC": jnxPTX1000136mrSlotPIC,
       "jnxPTX1000136mrSlotPSM": jnxPTX1000136mrSlotPSM,
       "jnxSlotPTX10004": jnxSlotPTX10004,
       "jnxPTX10004SlotFPC": jnxPTX10004SlotFPC,
       "jnxPTX10004SlotHM": jnxPTX10004SlotHM,
       "jnxPTX10004SlotPower": jnxPTX10004SlotPower,
       "jnxPTX10004SlotFan": jnxPTX10004SlotFan,
       "jnxPTX10004SlotFPB": jnxPTX10004SlotFPB,
       "jnxPTX10004SlotCBD": jnxPTX10004SlotCBD,
       "jnxPTX10004SlotSIB": jnxPTX10004SlotSIB,
       "jnxPTX10004SlotFPM": jnxPTX10004SlotFPM,
       "jnxPTX10004SlotFTC": jnxPTX10004SlotFTC,
       "jnxPTX10004SlotBackplane": jnxPTX10004SlotBackplane,
       "jnxSlotACX753": jnxSlotACX753,
       "jnxACX753SlotRE": jnxACX753SlotRE,
       "jnxACX753SlotPSM": jnxACX753SlotPSM,
       "jnxACX753SlotFan": jnxACX753SlotFan,
       "jnxACX753SlotCBD": jnxACX753SlotCBD,
       "jnxACX753SlotBackplane": jnxACX753SlotBackplane,
       "jnxACX753SlotFPC": jnxACX753SlotFPC,
       "jnxACX753SlotPIC": jnxACX753SlotPIC,
       "jnxACX753SlotFEB": jnxACX753SlotFEB,
       "jnxSlotSRX1800": jnxSlotSRX1800,
       "jnxSRX1800SlotFPC": jnxSRX1800SlotFPC,
       "jnxSRX1800SlotPIC": jnxSRX1800SlotPIC,
       "jnxSRX1800SlotHM": jnxSRX1800SlotHM,
       "jnxSRX1800SlotPower": jnxSRX1800SlotPower,
       "jnxSRX1800SlotFan": jnxSRX1800SlotFan,
       "jnxSlotACX7KSwitch": jnxSlotACX7KSwitch,
       "jnxACX7KSwitchSlotFPC": jnxACX7KSwitchSlotFPC,
       "jnxACX7KSwitchSlotHM": jnxACX7KSwitchSlotHM,
       "jnxACX7KSwitchSlotPower": jnxACX7KSwitchSlotPower,
       "jnxACX7KSwitchSlotFan": jnxACX7KSwitchSlotFan,
       "jnxACX7KSwitchSlotFPB": jnxACX7KSwitchSlotFPB,
       "jnxACX7KSwitchSlotCBD": jnxACX7KSwitchSlotCBD,
       "jnxACX7KSwitchSlotSIB": jnxACX7KSwitchSlotSIB,
       "jnxACX7KSwitchSlotFEB": jnxACX7KSwitchSlotFEB,
       "jnxSlotACX710032c": jnxSlotACX710032c,
       "jnxACX710032cSlotFPC": jnxACX710032cSlotFPC,
       "jnxACX710032cSlotHM": jnxACX710032cSlotHM,
       "jnxACX710032cSlotPower": jnxACX710032cSlotPower,
       "jnxACX710032cSlotFan": jnxACX710032cSlotFan,
       "jnxACX710032cSlotFPB": jnxACX710032cSlotFPB,
       "jnxACX710032cSlotCBD": jnxACX710032cSlotCBD,
       "jnxACX710032cSlotSIB": jnxACX710032cSlotSIB,
       "jnxACX710032cSlotFEB": jnxACX710032cSlotFEB,
       "jnxSlotACX710048l": jnxSlotACX710048l,
       "jnxACX710048lSlotFPC": jnxACX710048lSlotFPC,
       "jnxACX710048lSlotHM": jnxACX710048lSlotHM,
       "jnxACX710048lSlotPower": jnxACX710048lSlotPower,
       "jnxACX710048lSlotFan": jnxACX710048lSlotFan,
       "jnxACX710048lSlotFPB": jnxACX710048lSlotFPB,
       "jnxACX710048lSlotCBD": jnxACX710048lSlotCBD,
       "jnxACX710048lSlotSIB": jnxACX710048lSlotSIB,
       "jnxACX710048lSlotFEB": jnxACX710048lSlotFEB,
       "jnxSlotACX7908": jnxSlotACX7908,
       "jnxACX7908SlotFPC": jnxACX7908SlotFPC,
       "jnxACX7908SlotHM": jnxACX7908SlotHM,
       "jnxACX7908SlotPower": jnxACX7908SlotPower,
       "jnxACX7908SlotFan": jnxACX7908SlotFan,
       "jnxACX7908SlotCBD": jnxACX7908SlotCBD,
       "jnxACX7908SlotSIB": jnxACX7908SlotSIB,
       "jnxACX7908SlotFPM": jnxACX7908SlotFPM,
       "jnxACX7908SlotBackplane": jnxACX7908SlotBackplane,
       "jnxSlotACX7024": jnxSlotACX7024,
       "jnxACX7024SlotFPC": jnxACX7024SlotFPC,
       "jnxACX7024SlotHM": jnxACX7024SlotHM,
       "jnxACX7024SlotPower": jnxACX7024SlotPower,
       "jnxACX7024SlotFan": jnxACX7024SlotFan,
       "jnxACX7024SlotFPB": jnxACX7024SlotFPB,
       "jnxACX7024SlotCBD": jnxACX7024SlotCBD,
       "jnxACX7024SlotSIB": jnxACX7024SlotSIB,
       "jnxACX7024SlotFEB": jnxACX7024SlotFEB,
       "jnxSlotSRX1600": jnxSlotSRX1600,
       "jnxSRX1600SlotFPC": jnxSRX1600SlotFPC,
       "jnxSRX1600SlotRE": jnxSRX1600SlotRE,
       "jnxSRX1600SlotPower": jnxSRX1600SlotPower,
       "jnxSRX1600SlotFan": jnxSRX1600SlotFan,
       "jnxSRX1600SlotCBD": jnxSRX1600SlotCBD,
       "jnxSlotSRX2300": jnxSlotSRX2300,
       "jnxSRX2300SlotFPC": jnxSRX2300SlotFPC,
       "jnxSRX2300SlotRE": jnxSRX2300SlotRE,
       "jnxSRX2300SlotPower": jnxSRX2300SlotPower,
       "jnxSRX2300SlotFan": jnxSRX2300SlotFan,
       "jnxSRX2300SlotCBD": jnxSRX2300SlotCBD,
       "jnxSlotSRX4300": jnxSlotSRX4300,
       "jnxSRX4300SlotFPC": jnxSRX4300SlotFPC,
       "jnxSRX4300SlotRE": jnxSRX4300SlotRE,
       "jnxSRX4300SlotPower": jnxSRX4300SlotPower,
       "jnxSRX4300SlotFan": jnxSRX4300SlotFan,
       "jnxSRX4300SlotCBD": jnxSRX4300SlotCBD,
       "jnxSlotACX7332": jnxSlotACX7332,
       "jnxACX7332SlotFPC": jnxACX7332SlotFPC,
       "jnxACX7332SlotRE": jnxACX7332SlotRE,
       "jnxACX7332SlotPower": jnxACX7332SlotPower,
       "jnxACX7332SlotFan": jnxACX7332SlotFan,
       "jnxACX7332SlotFEB": jnxACX7332SlotFEB,
       "jnxACX7332SlotCBD": jnxACX7332SlotCBD,
       "jnxSlotACX7348": jnxSlotACX7348,
       "jnxACX7348SlotFPC": jnxACX7348SlotFPC,
       "jnxACX7348SlotRE": jnxACX7348SlotRE,
       "jnxACX7348SlotPower": jnxACX7348SlotPower,
       "jnxACX7348SlotFan": jnxACX7348SlotFan,
       "jnxACX7348SlotFEB": jnxACX7348SlotFEB,
       "jnxACX7348SlotCBD": jnxACX7348SlotCBD,
       "jnxSlotACX7024X": jnxSlotACX7024X,
       "jnxACX7024XSlotFPC": jnxACX7024XSlotFPC,
       "jnxACX7024XSlotHM": jnxACX7024XSlotHM,
       "jnxACX7024XSlotPower": jnxACX7024XSlotPower,
       "jnxACX7024XSlotFan": jnxACX7024XSlotFan,
       "jnxACX7024XSlotFPB": jnxACX7024XSlotFPB,
       "jnxACX7024XSlotCBD": jnxACX7024XSlotCBD,
       "jnxACX7024XSlotSIB": jnxACX7024XSlotSIB,
       "jnxACX7024XSlotFEB": jnxACX7024XSlotFEB,
       "jnxSlotPTX1000236qdd": jnxSlotPTX1000236qdd,
       "jnxPTX1000236qddSlotRE": jnxPTX1000236qddSlotRE,
       "jnxPTX1000236qddSlotCB": jnxPTX1000236qddSlotCB,
       "jnxPTX1000236qddSlotFPC": jnxPTX1000236qddSlotFPC,
       "jnxPTX1000236qddSlotFan": jnxPTX1000236qddSlotFan,
       "jnxPTX1000236qddSlotPIC": jnxPTX1000236qddSlotPIC,
       "jnxPTX1000236qddSlotPSM": jnxPTX1000236qddSlotPSM,
       "jnxPTX1000236qddSlotBackplane": jnxPTX1000236qddSlotBackplane,
       "jnxPTX1000236qddSlotFPM": jnxPTX1000236qddSlotFPM,
       "jnxSlotSRX4700": jnxSlotSRX4700,
       "jnxSRX4700SlotFPC": jnxSRX4700SlotFPC,
       "jnxSRX4700SlotRE": jnxSRX4700SlotRE,
       "jnxSRX4700SlotPower": jnxSRX4700SlotPower,
       "jnxSRX4700SlotFan": jnxSRX4700SlotFan,
       "jnxSRX4700SlotCBD": jnxSRX4700SlotCBD,
       "jnxMediaCardSpace": jnxMediaCardSpace,
       "jnxMediaCardSpaceM40": jnxMediaCardSpaceM40,
       "jnxMediaCardSpacePIC": jnxMediaCardSpacePIC,
       "jnxMediaCardSpaceM20": jnxMediaCardSpaceM20,
       "jnxM20MediaCardSpacePIC": jnxM20MediaCardSpacePIC,
       "jnxMediaCardSpaceM160": jnxMediaCardSpaceM160,
       "jnxM160MediaCardSpacePIC": jnxM160MediaCardSpacePIC,
       "jnxMediaCardSpaceM10": jnxMediaCardSpaceM10,
       "jnxM10MediaCardSpacePIC": jnxM10MediaCardSpacePIC,
       "jnxMediaCardSpaceM5": jnxMediaCardSpaceM5,
       "jnxM5MediaCardSpacePIC": jnxM5MediaCardSpacePIC,
       "jnxMediaCardSpaceT640": jnxMediaCardSpaceT640,
       "jnxT640MediaCardSpacePIC": jnxT640MediaCardSpacePIC,
       "jnxMediaCardSpaceT320": jnxMediaCardSpaceT320,
       "jnxT320MediaCardSpacePIC": jnxT320MediaCardSpacePIC,
       "jnxMediaCardSpaceM40e": jnxMediaCardSpaceM40e,
       "jnxM40eMediaCardSpacePIC": jnxM40eMediaCardSpacePIC,
       "jnxMediaCardSpaceM320": jnxMediaCardSpaceM320,
       "jnxM320MediaCardSpacePIC": jnxM320MediaCardSpacePIC,
       "jnxM320MediaCardSpaceMIC": jnxM320MediaCardSpaceMIC,
       "jnxMediaCardSpaceM7i": jnxMediaCardSpaceM7i,
       "jnxM7iMediaCardSpacePIC": jnxM7iMediaCardSpacePIC,
       "jnxMediaCardSpaceM10i": jnxMediaCardSpaceM10i,
       "jnxM10iMediaCardSpacePIC": jnxM10iMediaCardSpacePIC,
       "jnxMediaCardSpaceJ2300": jnxMediaCardSpaceJ2300,
       "jnxJ2300MediaCardSpacePIC": jnxJ2300MediaCardSpacePIC,
       "jnxMediaCardSpaceJ4300": jnxMediaCardSpaceJ4300,
       "jnxJ4300MediaCardSpacePIC": jnxJ4300MediaCardSpacePIC,
       "jnxMediaCardSpaceJ6300": jnxMediaCardSpaceJ6300,
       "jnxJ6300MediaCardSpacePIC": jnxJ6300MediaCardSpacePIC,
       "jnxMediaCardSpaceIRM": jnxMediaCardSpaceIRM,
       "jnxIRMMediaCardSpacePIC": jnxIRMMediaCardSpacePIC,
       "jnxMediaCardSpaceTX": jnxMediaCardSpaceTX,
       "jnxTXMediaCardSpacePIC": jnxTXMediaCardSpacePIC,
       "jnxMediaCardSpaceM120": jnxMediaCardSpaceM120,
       "jnxM120MediaCardSpacePIC": jnxM120MediaCardSpacePIC,
       "jnxMediaCardSpaceJ4350": jnxMediaCardSpaceJ4350,
       "jnxJ4350MediaCardSpacePIC": jnxJ4350MediaCardSpacePIC,
       "jnxMediaCardSpaceJ6350": jnxMediaCardSpaceJ6350,
       "jnxJ6350MediaCardSpacePIC": jnxJ6350MediaCardSpacePIC,
       "jnxMediaCardSpaceMX960": jnxMediaCardSpaceMX960,
       "jnxMX960MediaCardSpacePIC": jnxMX960MediaCardSpacePIC,
       "jnxMX960MediaCardSpaceMIC": jnxMX960MediaCardSpaceMIC,
       "jnxMediaCardSpaceJ4320": jnxMediaCardSpaceJ4320,
       "jnxJ4320MediaCardSpacePIC": jnxJ4320MediaCardSpacePIC,
       "jnxMediaCardSpaceJ2320": jnxMediaCardSpaceJ2320,
       "jnxJ2320MediaCardSpacePIC": jnxJ2320MediaCardSpacePIC,
       "jnxMediaCardSpaceJ2350": jnxMediaCardSpaceJ2350,
       "jnxJ2350MediaCardSpacePIC": jnxJ2350MediaCardSpacePIC,
       "jnxMediaCardSpaceMX480": jnxMediaCardSpaceMX480,
       "jnxMX480MediaCardSpacePIC": jnxMX480MediaCardSpacePIC,
       "jnxMX480MediaCardSpaceMIC": jnxMX480MediaCardSpaceMIC,
       "jnxMediaCardSpaceSRX5800": jnxMediaCardSpaceSRX5800,
       "jnxSRX5800MediaCardSpacePIC": jnxSRX5800MediaCardSpacePIC,
       "jnxMediaCardSpaceT1600": jnxMediaCardSpaceT1600,
       "jnxT1600MediaCardSpacePIC": jnxT1600MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX5600": jnxMediaCardSpaceSRX5600,
       "jnxSRX5600MediaCardSpacePIC": jnxSRX5600MediaCardSpacePIC,
       "jnxMediaCardSpaceMX240": jnxMediaCardSpaceMX240,
       "jnxMX240MediaCardSpacePIC": jnxMX240MediaCardSpacePIC,
       "jnxMX240MediaCardSpaceMIC": jnxMX240MediaCardSpaceMIC,
       "jnxMediaCardSpaceEX3200": jnxMediaCardSpaceEX3200,
       "jnxEX3200MediaCardSpacePIC": jnxEX3200MediaCardSpacePIC,
       "jnxMediaCardSpaceEX4200": jnxMediaCardSpaceEX4200,
       "jnxEX4200MediaCardSpacePIC": jnxEX4200MediaCardSpacePIC,
       "jnxMediaCardSpaceEX8208": jnxMediaCardSpaceEX8208,
       "jnxEX8208MediaCardSpacePIC": jnxEX8208MediaCardSpacePIC,
       "jnxMediaCardSpaceEX8216": jnxMediaCardSpaceEX8216,
       "jnxEX8216MediaCardSpacePIC": jnxEX8216MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX3600": jnxMediaCardSpaceSRX3600,
       "jnxSRX3600MediaCardSpacePIC": jnxSRX3600MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX3400": jnxMediaCardSpaceSRX3400,
       "jnxSRX3400MediaCardSpacePIC": jnxSRX3400MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX210": jnxMediaCardSpaceSRX210,
       "jnxSRX210MediaCardSpacePIC": jnxSRX210MediaCardSpacePIC,
       "jnxMediaCardSpaceTXP": jnxMediaCardSpaceTXP,
       "jnxTXPMediaCardSpacePIC": jnxTXPMediaCardSpacePIC,
       "jnxMediaCardSpaceJCS": jnxMediaCardSpaceJCS,
       "jnxJCSMediaCardSpacePIC": jnxJCSMediaCardSpacePIC,
       "jnxMediaCardSpaceSRX240": jnxMediaCardSpaceSRX240,
       "jnxSRX240MediaCardSpacePIC": jnxSRX240MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX650": jnxMediaCardSpaceSRX650,
       "jnxSRX650MediaCardSpacePIC": jnxSRX650MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX100": jnxMediaCardSpaceSRX100,
       "jnxSRX100MediaCardSpacePIC": jnxSRX100MediaCardSpacePIC,
       "jnxMediaCardSpaceLN1000V": jnxMediaCardSpaceLN1000V,
       "jnxLN1000VMediaCardSpacePIC": jnxLN1000VMediaCardSpacePIC,
       "jnxMediaCardSpaceEX2200": jnxMediaCardSpaceEX2200,
       "jnxEX2200MediaCardSpacePIC": jnxEX2200MediaCardSpacePIC,
       "jnxMediaCardSpaceEX4500": jnxMediaCardSpaceEX4500,
       "jnxEX4500MediaCardSpacePIC": jnxEX4500MediaCardSpacePIC,
       "jnxMediaCardSpaceIBM4274M02J02M": jnxMediaCardSpaceIBM4274M02J02M,
       "jnxIBM4274M02J02MMediaCardSpacePIC": jnxIBM4274M02J02MMediaCardSpacePIC,
       "jnxIBM4274M02J02MMediaCardSpaceMIC": jnxIBM4274M02J02MMediaCardSpaceMIC,
       "jnxMediaCardSpaceIBM4274M06J06M": jnxMediaCardSpaceIBM4274M06J06M,
       "jnxIBM4274M06J06MMediaCardSpacePIC": jnxIBM4274M06J06MMediaCardSpacePIC,
       "jnxIBM4274M06J06MMediaCardSpaceMIC": jnxIBM4274M06J06MMediaCardSpaceMIC,
       "jnxMediaCardSpaceIBM4274M11J11M": jnxMediaCardSpaceIBM4274M11J11M,
       "jnxIBM4274M11J11MMediaCardSpacePIC": jnxIBM4274M11J11MMediaCardSpacePIC,
       "jnxIBM4274M11J11MMediaCardSpaceMIC": jnxIBM4274M11J11MMediaCardSpaceMIC,
       "jnxMediaCardSpaceSRX1400": jnxMediaCardSpaceSRX1400,
       "jnxSRX1400MediaCardSpacePIC": jnxSRX1400MediaCardSpacePIC,
       "jnxMediaCardSpaceIBM4274S58J58S": jnxMediaCardSpaceIBM4274S58J58S,
       "jnxIBM4274S58J58SMediaCardSpacePIC": jnxIBM4274S58J58SMediaCardSpacePIC,
       "jnxMediaCardSpaceIBM4274S56J56S": jnxMediaCardSpaceIBM4274S56J56S,
       "jnxIBM4274S56J56SMediaCardSpacePIC": jnxIBM4274S56J56SMediaCardSpacePIC,
       "jnxMediaCardSpaceIBM4274S36J36S": jnxMediaCardSpaceIBM4274S36J36S,
       "jnxIBM4274S36J36SMediaCardSpacePIC": jnxIBM4274S36J36SMediaCardSpacePIC,
       "jnxMediaCardSpaceIBM4274S34J34S": jnxMediaCardSpaceIBM4274S34J34S,
       "jnxIBM4274S34J34SMediaCardSpacePIC": jnxIBM4274S34J34SMediaCardSpacePIC,
       "jnxMediaCardSpaceIBM427348EJ48E": jnxMediaCardSpaceIBM427348EJ48E,
       "jnxIBM427348EJ48EMediaCardSpacePIC": jnxIBM427348EJ48EMediaCardSpacePIC,
       "jnxMediaCardSpaceIBM4274E08J08E": jnxMediaCardSpaceIBM4274E08J08E,
       "jnxIBM4274E08J08EMediaCardSpacePIC": jnxIBM4274E08J08EMediaCardSpacePIC,
       "jnxMediaCardSpaceIBM4274E16J16E": jnxMediaCardSpaceIBM4274E16J16E,
       "jnxIBM4274E16J16EMediaCardSpacePIC": jnxIBM4274E16J16EMediaCardSpacePIC,
       "jnxMediaCardSpaceMX80": jnxMediaCardSpaceMX80,
       "jnxMX80MediaCardSpacePIC": jnxMX80MediaCardSpacePIC,
       "jnxMX80MediaCardSpaceMIC": jnxMX80MediaCardSpaceMIC,
       "jnxMediaCardSpaceSRX220": jnxMediaCardSpaceSRX220,
       "jnxSRX220MediaCardSpacePIC": jnxSRX220MediaCardSpacePIC,
       "jnxMediaCardSpaceEXXRE": jnxMediaCardSpaceEXXRE,
       "jnxEXXREMediaCardSpacePIC": jnxEXXREMediaCardSpacePIC,
       "jnxMediaCardSpaceQFXInterconnect": jnxMediaCardSpaceQFXInterconnect,
       "jnxQFXInterconnectMediaCardSpacePIC": jnxQFXInterconnectMediaCardSpacePIC,
       "jnxMediaCardSpaceQFXNode": jnxMediaCardSpaceQFXNode,
       "jnxQFXNodeMediaCardSpacePIC": jnxQFXNodeMediaCardSpacePIC,
       "jnxMediaCardSpaceQFXJVRE": jnxMediaCardSpaceQFXJVRE,
       "jnxQFXJVREMediaCardSpacePIC": jnxQFXJVREMediaCardSpacePIC,
       "jnxMediaCardSpaceEX4300": jnxMediaCardSpaceEX4300,
       "jnxEX4300MediaCardSpacePIC": jnxEX4300MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX110": jnxMediaCardSpaceSRX110,
       "jnxSRX110MediaCardSpacePIC": jnxSRX110MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX120": jnxMediaCardSpaceSRX120,
       "jnxSRX120MediaCardSpacePIC": jnxSRX120MediaCardSpacePIC,
       "jnxMediaCardSpaceMAG8600": jnxMediaCardSpaceMAG8600,
       "jnxMAG8600MediaCardSpacePIC": jnxMAG8600MediaCardSpacePIC,
       "jnxMediaCardSpaceMAG6611": jnxMediaCardSpaceMAG6611,
       "jnxMAG6611MediaCardSpacePIC": jnxMAG6611MediaCardSpacePIC,
       "jnxMediaCardSpaceMAG6610": jnxMediaCardSpaceMAG6610,
       "jnxMAG6610MediaCardSpacePIC": jnxMAG6610MediaCardSpacePIC,
       "jnxMediaCardSpacePTX5000": jnxMediaCardSpacePTX5000,
       "jnxPTX5000MediaCardSpacePIC": jnxPTX5000MediaCardSpacePIC,
       "jnxMediaCardSpaceIBM0719J45E": jnxMediaCardSpaceIBM0719J45E,
       "jnxIBM0719J45EMediaCardSpacePIC": jnxIBM0719J45EMediaCardSpacePIC,
       "jnxMediaCardSpaceIBMJ08F": jnxMediaCardSpaceIBMJ08F,
       "jnxIBMJ08FMediaCardSpacePIC": jnxIBMJ08FMediaCardSpacePIC,
       "jnxMediaCardSpaceIBMJ52F": jnxMediaCardSpaceIBMJ52F,
       "jnxIBMJ52FMediaCardSpacePIC": jnxIBMJ52FMediaCardSpacePIC,
       "jnxMediaCardSpaceEX6210": jnxMediaCardSpaceEX6210,
       "jnxEX6210MediaCardSpacePIC": jnxEX6210MediaCardSpacePIC,
       "jnxMediaCardSpaceDellJFX3500": jnxMediaCardSpaceDellJFX3500,
       "jnxDellJFX3500MediaCardSpacePIC": jnxDellJFX3500MediaCardSpacePIC,
       "jnxMediaCardSpaceEX3300": jnxMediaCardSpaceEX3300,
       "jnxEX3300MediaCardSpacePIC": jnxEX3300MediaCardSpacePIC,
       "jnxMediaCardSpaceDELLJSRX3600": jnxMediaCardSpaceDELLJSRX3600,
       "jnxDELLJSRX3600MediaCardSpacePIC": jnxDELLJSRX3600MediaCardSpacePIC,
       "jnxMediaCardSpaceDELLJSRX3400": jnxMediaCardSpaceDELLJSRX3400,
       "jnxDELLJSRX3400MediaCardSpacePIC": jnxDELLJSRX3400MediaCardSpacePIC,
       "jnxMediaCardSpaceDELLJSRX1400": jnxMediaCardSpaceDELLJSRX1400,
       "jnxDELLJSRX1400MediaCardSpacePIC": jnxDELLJSRX1400MediaCardSpacePIC,
       "jnxMediaCardSpaceDELLJSRX5800": jnxMediaCardSpaceDELLJSRX5800,
       "jnxDELLJSRX5800MediaCardSpacePIC": jnxDELLJSRX5800MediaCardSpacePIC,
       "jnxMediaCardSpaceDELLJSRX5600": jnxMediaCardSpaceDELLJSRX5600,
       "jnxDELLJSRX5600MediaCardSpacePIC": jnxDELLJSRX5600MediaCardSpacePIC,
       "jnxMediaCardSpaceQFXSwitch": jnxMediaCardSpaceQFXSwitch,
       "jnxQFXSwitchMediaCardSpacePIC": jnxQFXSwitchMediaCardSpacePIC,
       "jnxMediaCardSpaceT4000": jnxMediaCardSpaceT4000,
       "jnxT4000MediaCardSpacePIC": jnxT4000MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX550": jnxMediaCardSpaceSRX550,
       "jnxSRX550MediaCardSpacePIC": jnxSRX550MediaCardSpacePIC,
       "jnxMediaCardSpaceACX": jnxMediaCardSpaceACX,
       "jnxACXMediaCardSpacePIC": jnxACXMediaCardSpacePIC,
       "jnxACXMediaCardSpaceMIC": jnxACXMediaCardSpaceMIC,
       "jnxMediaCardSpaceMX40": jnxMediaCardSpaceMX40,
       "jnxMX40MediaCardSpacePIC": jnxMX40MediaCardSpacePIC,
       "jnxMX40MediaCardSpaceMIC": jnxMX40MediaCardSpaceMIC,
       "jnxMediaCardSpaceMX10": jnxMediaCardSpaceMX10,
       "jnxMX10MediaCardSpacePIC": jnxMX10MediaCardSpacePIC,
       "jnxMX10MediaCardSpaceMIC": jnxMX10MediaCardSpaceMIC,
       "jnxMediaCardSpaceMX5": jnxMediaCardSpaceMX5,
       "jnxMX5MediaCardSpacePIC": jnxMX5MediaCardSpacePIC,
       "jnxMX5MediaCardSpaceMIC": jnxMX5MediaCardSpaceMIC,
       "jnxMediaCardSpaceQFXMInterconnect": jnxMediaCardSpaceQFXMInterconnect,
       "jnxQFXMInterconnectMediaCardSpacePIC": jnxQFXMInterconnectMediaCardSpacePIC,
       "jnxMediaCardSpaceEX4550": jnxMediaCardSpaceEX4550,
       "jnxEX4550MediaCardSpacePIC": jnxEX4550MediaCardSpacePIC,
       "jnxMediaCardSpaceMX2020": jnxMediaCardSpaceMX2020,
       "jnxMX2020MediaCardSpacePIC": jnxMX2020MediaCardSpacePIC,
       "jnxMX2020MediaCardSpaceMIC": jnxMX2020MediaCardSpaceMIC,
       "jnxMediaCardSpaceLN2600": jnxMediaCardSpaceLN2600,
       "jnxLN2600MediaCardSpacePIC": jnxLN2600MediaCardSpacePIC,
       "jnxMediaCardSpaceFireflyPerimeter": jnxMediaCardSpaceFireflyPerimeter,
       "jnxFireflyPerimeterMediaCardSpacePIC": jnxFireflyPerimeterMediaCardSpacePIC,
       "jnxMediaCardSpaceMX104": jnxMediaCardSpaceMX104,
       "jnxMX104MediaCardSpacePIC": jnxMX104MediaCardSpacePIC,
       "jnxMX104MediaCardSpaceMIC": jnxMX104MediaCardSpaceMIC,
       "jnxMediaCardSpacePTX3000": jnxMediaCardSpacePTX3000,
       "jnxPTX3000MediaCardSpacePIC": jnxPTX3000MediaCardSpacePIC,
       "jnxMediaCardSpaceMX2010": jnxMediaCardSpaceMX2010,
       "jnxMX2010MediaCardSpacePIC": jnxMX2010MediaCardSpacePIC,
       "jnxMX2010MediaCardSpaceMIC": jnxMX2010MediaCardSpaceMIC,
       "jnxMediaCardSpaceLN2800": jnxMediaCardSpaceLN2800,
       "jnxLN2800MediaCardSpacePIC": jnxLN2800MediaCardSpacePIC,
       "jnxMediaCardSpaceEX9214": jnxMediaCardSpaceEX9214,
       "jnxEX9214MediaCardSpacePIC": jnxEX9214MediaCardSpacePIC,
       "jnxEX9214MediaCardSpaceMIC": jnxEX9214MediaCardSpaceMIC,
       "jnxMediaCardSpaceEX9208": jnxMediaCardSpaceEX9208,
       "jnxEX9208MediaCardSpacePIC": jnxEX9208MediaCardSpacePIC,
       "jnxEX9208MediaCardSpaceMIC": jnxEX9208MediaCardSpaceMIC,
       "jnxMediaCardSpaceEX9204": jnxMediaCardSpaceEX9204,
       "jnxEX9204MediaCardSpacePIC": jnxEX9204MediaCardSpacePIC,
       "jnxEX9204MediaCardSpaceMIC": jnxEX9204MediaCardSpaceMIC,
       "jnxMediaCardSpaceSRX5400": jnxMediaCardSpaceSRX5400,
       "jnxSRX5400MediaCardSpacePIC": jnxSRX5400MediaCardSpacePIC,
       "jnxMediaCardSpaceIBM4274S54J54S": jnxMediaCardSpaceIBM4274S54J54S,
       "jnxIBM4274S54J54SMediaCardSpacePIC": jnxIBM4274S54J54SMediaCardSpacePIC,
       "jnxMediaCardSpaceDELLJSRX5400": jnxMediaCardSpaceDELLJSRX5400,
       "jnxDELLJSRX5400MediaCardSpacePIC": jnxDELLJSRX5400MediaCardSpacePIC,
       "jnxMediaCardSpaceVMX": jnxMediaCardSpaceVMX,
       "jnxVMXMediaCardSpacePIC": jnxVMXMediaCardSpacePIC,
       "jnxVMXMediaCardSpaceMIC": jnxVMXMediaCardSpaceMIC,
       "jnxMediaCardSpaceEX4600": jnxMediaCardSpaceEX4600,
       "jnxEX4600MediaCardSpacePIC": jnxEX4600MediaCardSpacePIC,
       "jnxMediaCardSpaceACX1000": jnxMediaCardSpaceACX1000,
       "jnxACX1000MediaCardSpacePIC": jnxACX1000MediaCardSpacePIC,
       "jnxACX1000MediaCardSpaceMIC": jnxACX1000MediaCardSpaceMIC,
       "jnxMediaCardSpaceACX2000": jnxMediaCardSpaceACX2000,
       "jnxACX2000MediaCardSpacePIC": jnxACX2000MediaCardSpacePIC,
       "jnxACX2000MediaCardSpaceMIC": jnxACX2000MediaCardSpaceMIC,
       "jnxMediaCardSpaceACX1100": jnxMediaCardSpaceACX1100,
       "jnxACX1100MediaCardSpacePIC": jnxACX1100MediaCardSpacePIC,
       "jnxACX1100MediaCardSpaceMIC": jnxACX1100MediaCardSpaceMIC,
       "jnxMediaCardSpaceACX2100": jnxMediaCardSpaceACX2100,
       "jnxACX2100MediaCardSpacePIC": jnxACX2100MediaCardSpacePIC,
       "jnxACX2100MediaCardSpaceMIC": jnxACX2100MediaCardSpaceMIC,
       "jnxMediaCardSpaceACX2200": jnxMediaCardSpaceACX2200,
       "jnxACX2200MediaCardSpacePIC": jnxACX2200MediaCardSpacePIC,
       "jnxACX2200MediaCardSpaceMIC": jnxACX2200MediaCardSpaceMIC,
       "jnxMediaCardSpaceACX4000": jnxMediaCardSpaceACX4000,
       "jnxACX4000MediaCardSpacePIC": jnxACX4000MediaCardSpacePIC,
       "jnxACX4000MediaCardSpaceMIC": jnxACX4000MediaCardSpaceMIC,
       "jnxMediaCardSpaceACX500AC": jnxMediaCardSpaceACX500AC,
       "jnxACX500ACMediaCardSpacePIC": jnxACX500ACMediaCardSpacePIC,
       "jnxACX500ACMediaCardSpaceMIC": jnxACX500ACMediaCardSpaceMIC,
       "jnxMediaCardSpaceACX500DC": jnxMediaCardSpaceACX500DC,
       "jnxACX500DCMediaCardSpacePIC": jnxACX500DCMediaCardSpacePIC,
       "jnxACX500DCMediaCardSpaceMIC": jnxACX500DCMediaCardSpaceMIC,
       "jnxMediaCardSpaceACX500OAC": jnxMediaCardSpaceACX500OAC,
       "jnxACX500OACMediaCardSpacePIC": jnxACX500OACMediaCardSpacePIC,
       "jnxACX500OACMediaCardSpaceMIC": jnxACX500OACMediaCardSpaceMIC,
       "jnxMediaCardSpaceACX500ODC": jnxMediaCardSpaceACX500ODC,
       "jnxACX500ODCMediaCardSpacePIC": jnxACX500ODCMediaCardSpacePIC,
       "jnxACX500ODCMediaCardSpaceMIC": jnxACX500ODCMediaCardSpaceMIC,
       "jnxMediaCardSpaceACX500OPOEAC": jnxMediaCardSpaceACX500OPOEAC,
       "jnxACX500OPOEACMediaCardSpacePIC": jnxACX500OPOEACMediaCardSpacePIC,
       "jnxACX500OPOEACMediaCardSpaceMIC": jnxACX500OPOEACMediaCardSpaceMIC,
       "jnxMediaCardSpaceACX500OPOEDC": jnxMediaCardSpaceACX500OPOEDC,
       "jnxACX500OPOEDCMediaCardSpacePIC": jnxACX500OPOEDCMediaCardSpacePIC,
       "jnxACX500OPOEDCMediaCardSpaceMIC": jnxACX500OPOEDCMediaCardSpaceMIC,
       "jnxMediaCardSpaceSatelliteDevice": jnxMediaCardSpaceSatelliteDevice,
       "jnxSatelliteDeviceMediaCardSpacePIC": jnxSatelliteDeviceMediaCardSpacePIC,
       "jnxMediaCardSpaceACX5048": jnxMediaCardSpaceACX5048,
       "jnxACX5048MediaCardSpacePIC": jnxACX5048MediaCardSpacePIC,
       "jnxMediaCardSpaceACX5096": jnxMediaCardSpaceACX5096,
       "jnxACX5096MediaCardSpacePIC": jnxACX5096MediaCardSpacePIC,
       "jnxMediaCardSpaceLN1000CC": jnxMediaCardSpaceLN1000CC,
       "jnxLN1000CCMediaCardSpacePIC": jnxLN1000CCMediaCardSpacePIC,
       "jnxMediaCardSpaceVSRX": jnxMediaCardSpaceVSRX,
       "jnxVSRXMediaCardSpacePIC": jnxVSRXMediaCardSpacePIC,
       "jnxMediaCardSpacePTX1000": jnxMediaCardSpacePTX1000,
       "jnxPTX1000MediaCardSpacePIC": jnxPTX1000MediaCardSpacePIC,
       "jnxMediaCardSpaceEX3400": jnxMediaCardSpaceEX3400,
       "jnxEX3400MediaCardSpacePIC": jnxEX3400MediaCardSpacePIC,
       "jnxMediaCardSpaceEX2300": jnxMediaCardSpaceEX2300,
       "jnxEX2300MediaCardSpacePIC": jnxEX2300MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX300": jnxMediaCardSpaceSRX300,
       "jnxSRX300MediaCardSpacePIC": jnxSRX300MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX320": jnxMediaCardSpaceSRX320,
       "jnxSRX320MediaCardSpacePIC": jnxSRX320MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX340": jnxMediaCardSpaceSRX340,
       "jnxSRX340MediaCardSpacePIC": jnxSRX340MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX345": jnxMediaCardSpaceSRX345,
       "jnxSRX345MediaCardSpacePIC": jnxSRX345MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX1500": jnxMediaCardSpaceSRX1500,
       "jnxSRX1500MediaCardSpacePIC": jnxSRX1500MediaCardSpacePIC,
       "jnxMediaCardSpaceJNP10003": jnxMediaCardSpaceJNP10003,
       "jnxJNP10003MediaCardSpacePIC": jnxJNP10003MediaCardSpacePIC,
       "jnxPicJNP1000312xQSFP28MacsecTIC": jnxPicJNP1000312xQSFP28MacsecTIC,
       "jnxJNP10003MediaCardSpaceMIC": jnxJNP10003MediaCardSpaceMIC,
       "jnxMediaCardSpaceSRX4600": jnxMediaCardSpaceSRX4600,
       "jnxSRX4600MediaCardSpacePIC": jnxSRX4600MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX4800": jnxMediaCardSpaceSRX4800,
       "jnxSRX4800MediaCardSpacePIC": jnxSRX4800MediaCardSpacePIC,
       "jnxSRX4800MediaCardSpaceMIC": jnxSRX4800MediaCardSpaceMIC,
       "jnxMediaCardSpaceSRX4100": jnxMediaCardSpaceSRX4100,
       "jnxSRX4100MediaCardSpacePIC": jnxSRX4100MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX4200": jnxMediaCardSpaceSRX4200,
       "jnxMediaCardSpaceJNP204": jnxMediaCardSpaceJNP204,
       "jnxPicJNP204MediaCardSpacePIC": jnxPicJNP204MediaCardSpacePIC,
       "jnxPicJNP2048XSFPP": jnxPicJNP2048XSFPP,
       "jnxMediaCardSpaceMX2008": jnxMediaCardSpaceMX2008,
       "jnxMX2008MediaCardSpacePIC": jnxMX2008MediaCardSpacePIC,
       "jnxMX2008MediaCardSpaceMIC": jnxMX2008MediaCardSpaceMIC,
       "jnxMediaCardSpaceMXTSR80": jnxMediaCardSpaceMXTSR80,
       "jnxMXTSR80MediaCardSpacePIC": jnxMXTSR80MediaCardSpacePIC,
       "jnxMXTSR80MediaCardSpaceMIC": jnxMXTSR80MediaCardSpaceMIC,
       "jnxMediaCardSpacePTX10008": jnxMediaCardSpacePTX10008,
       "jnxPTX10008MediaCardSpacePIC": jnxPTX10008MediaCardSpacePIC,
       "jnxMediaCardSpaceACX5448": jnxMediaCardSpaceACX5448,
       "jnxACX5448MediaCardSpacePIC": jnxACX5448MediaCardSpacePIC,
       "jnxACX5448MediaCardSpaceMIC": jnxACX5448MediaCardSpaceMIC,
       "jnxMediaCardSpacePTX10016": jnxMediaCardSpacePTX10016,
       "jnxPTX10016MediaCardSpacePIC": jnxPTX10016MediaCardSpacePIC,
       "jnxMediaCardSpaceEX9251": jnxMediaCardSpaceEX9251,
       "jnxPicEX92514xQSFP28": jnxPicEX92514xQSFP28,
       "jnxPicEX92518XSFPP": jnxPicEX92518XSFPP,
       "jnxMediaCardSpaceMX150": jnxMediaCardSpaceMX150,
       "jnxMX150MediaCardSpacePIC": jnxMX150MediaCardSpacePIC,
       "jnxMX150MediaCardSpaceMIC": jnxMX150MediaCardSpaceMIC,
       "jnxMediaCardSpaceJNP10001": jnxMediaCardSpaceJNP10001,
       "jnxJNP10001MediaCardSpacePIC": jnxJNP10001MediaCardSpacePIC,
       "jnxPicJNP1000116xQSFP28MacsecTIC": jnxPicJNP1000116xQSFP28MacsecTIC,
       "jnxMediaCardSpaceMX10008": jnxMediaCardSpaceMX10008,
       "jnxMX10008MediaCardSpacePIC": jnxMX10008MediaCardSpacePIC,
       "jnxMediaCardSpaceMX10016": jnxMediaCardSpaceMX10016,
       "jnxMX10016MediaCardSpacePIC": jnxMX10016MediaCardSpacePIC,
       "jnxMediaCardSpaceEX9253": jnxMediaCardSpaceEX9253,
       "jnxEX9253MediaCardSpacePIC": jnxEX9253MediaCardSpacePIC,
       "jnxPicEX925312xQSFP28MacsecTIC": jnxPicEX925312xQSFP28MacsecTIC,
       "jnxEX9253MediaCardSpaceMIC": jnxEX9253MediaCardSpaceMIC,
       "jnxMediaCardSpaceACX5448M": jnxMediaCardSpaceACX5448M,
       "jnxACX5448MMediaCardSpacePIC": jnxACX5448MMediaCardSpacePIC,
       "jnxACX5448MMediaCardSpaceMIC": jnxACX5448MMediaCardSpaceMIC,
       "jnxMediaCardSpaceACX5448D": jnxMediaCardSpaceACX5448D,
       "jnxACX5448DMediaCardSpacePIC": jnxACX5448DMediaCardSpacePIC,
       "jnxACX5448DMediaCardSpaceMIC": jnxACX5448DMediaCardSpaceMIC,
       "jnxMediaCardSpaceACX6360OR": jnxMediaCardSpaceACX6360OR,
       "jnxACX6360ORMediaCardSpacePIC": jnxACX6360ORMediaCardSpacePIC,
       "jnxPicACX6360OR20xQSFP28TIC": jnxPicACX6360OR20xQSFP28TIC,
       "jnxPicACX6360OR8xCFP2DCOTIC": jnxPicACX6360OR8xCFP2DCOTIC,
       "jnxMediaCardSpaceACX6360OX": jnxMediaCardSpaceACX6360OX,
       "jnxACX6360OXMediaCardSpacePIC": jnxACX6360OXMediaCardSpacePIC,
       "jnxPicACX6360OX20xQSFP28TIC": jnxPicACX6360OX20xQSFP28TIC,
       "jnxPicACX6360OX8xCFP2DCOTIC": jnxPicACX6360OX8xCFP2DCOTIC,
       "jnxMediaCardSpaceACX710": jnxMediaCardSpaceACX710,
       "jnxACX710MediaCardSpacePIC": jnxACX710MediaCardSpacePIC,
       "jnxACX710MediaCardSpaceMIC": jnxACX710MediaCardSpaceMIC,
       "jnxMediaCardSpaceACX5800": jnxMediaCardSpaceACX5800,
       "jnxACX5800MediaCardSpacePIC": jnxACX5800MediaCardSpacePIC,
       "jnxACX5800MediaCardSpaceMIC": jnxACX5800MediaCardSpaceMIC,
       "jnxMediaCardSpaceSRX380": jnxMediaCardSpaceSRX380,
       "jnxSRX380MediaCardSpacePIC": jnxSRX380MediaCardSpacePIC,
       "jnxMediaCardSpaceEX4400": jnxMediaCardSpaceEX4400,
       "jnxEX4400MediaCardSpacePIC": jnxEX4400MediaCardSpacePIC,
       "jnxMediaCardSpaceR6675": jnxMediaCardSpaceR6675,
       "jnxR6675MediaCardSpacePIC": jnxR6675MediaCardSpacePIC,
       "jnxR6675MediaCardSpaceMIC": jnxR6675MediaCardSpaceMIC,
       "jnxMediaCardSpaceMX304": jnxMediaCardSpaceMX304,
       "jnxMX304MediaCardSpacePIC": jnxMX304MediaCardSpacePIC,
       "jnxMediaCardSpaceMX10004": jnxMediaCardSpaceMX10004,
       "jnxMX10004MediaCardSpacePIC": jnxMX10004MediaCardSpacePIC,
       "jnxMediaCardSpaceEX4100": jnxMediaCardSpaceEX4100,
       "jnxEX4100MediaCardSpacePIC": jnxEX4100MediaCardSpacePIC,
       "jnxMediaCardSpaceEX4650": jnxMediaCardSpaceEX4650,
       "jnxEX4650MediaCardSpacePIC": jnxEX4650MediaCardSpacePIC,
       "jnxMediaCardSpacePTX1000260C": jnxMediaCardSpacePTX1000260C,
       "jnxPTX1000260CMediaCardSpacePIC": jnxPTX1000260CMediaCardSpacePIC,
       "jnxMediaCardSpacePTX10004": jnxMediaCardSpacePTX10004,
       "jnxPTX10004MediaCardSpacePIC": jnxPTX10004MediaCardSpacePIC,
       "jnxMediaCardSpaceACX7KSwitch": jnxMediaCardSpaceACX7KSwitch,
       "jnxACX7KSwitchMediaCardSpacePIC": jnxACX7KSwitchMediaCardSpacePIC,
       "jnxMediaCardSpaceACX710032c": jnxMediaCardSpaceACX710032c,
       "jnxACX710032cMediaCardSpacePIC": jnxACX710032cMediaCardSpacePIC,
       "jnxMediaCardSpaceACX710048l": jnxMediaCardSpaceACX710048l,
       "jnxACX710048lMediaCardSpacePIC": jnxACX710048lMediaCardSpacePIC,
       "jnxMediaCardSpaceACX7908": jnxMediaCardSpaceACX7908,
       "jnxACX7908MediaCardSpacePIC": jnxACX7908MediaCardSpacePIC,
       "jnxMediaCardSpaceACX7024": jnxMediaCardSpaceACX7024,
       "jnxACX7024MediaCardSpacePIC": jnxACX7024MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX1600": jnxMediaCardSpaceSRX1600,
       "jnxSRX1600MediaCardSpacePIC": jnxSRX1600MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX2300": jnxMediaCardSpaceSRX2300,
       "jnxSRX2300MediaCardSpacePIC": jnxSRX2300MediaCardSpacePIC,
       "jnxMediaCardSpaceSRX4300": jnxMediaCardSpaceSRX4300,
       "jnxSRX4300MediaCardSpacePIC": jnxSRX4300MediaCardSpacePIC,
       "jnxMediaCardSpaceACX7332": jnxMediaCardSpaceACX7332,
       "jnxACX7332MediaCardSpacePIC": jnxACX7332MediaCardSpacePIC,
       "jnxMediaCardSpaceACX7348": jnxMediaCardSpaceACX7348,
       "jnxACX7348MediaCardSpacePIC": jnxACX7348MediaCardSpacePIC,
       "jnxMediaCardSpaceACX7024X": jnxMediaCardSpaceACX7024X,
       "jnxACX7024XMediaCardSpacePIC": jnxACX7024XMediaCardSpacePIC,
       "jnxMediaCardSpaceSRX4700": jnxMediaCardSpaceSRX4700,
       "jnxSRX4700MediaCardSpacePIC": jnxSRX4700MediaCardSpacePIC,
       "jnxSubSpace": jnxSubSpace,
       "jnxSubSpaceM160": jnxSubSpaceM160,
       "jnxM160SubSpaceSFM": jnxM160SubSpaceSFM,
       "jnxClassContents": jnxClassContents,
       "jnxBackplane": jnxBackplane,
       "jnxBackplaneM40": jnxBackplaneM40,
       "jnxBackplaneM20": jnxBackplaneM20,
       "jnxMidplaneM160": jnxMidplaneM160,
       "jnxMidplaneM10": jnxMidplaneM10,
       "jnxMidplaneM5": jnxMidplaneM5,
       "jnxMidplaneT640": jnxMidplaneT640,
       "jnxMidplaneT320": jnxMidplaneT320,
       "jnxMidplaneM40e": jnxMidplaneM40e,
       "jnxMidplaneM320": jnxMidplaneM320,
       "jnxMidplaneM7i": jnxMidplaneM7i,
       "jnxMidplaneM10i": jnxMidplaneM10i,
       "jnxMidplaneJ2300": jnxMidplaneJ2300,
       "jnxMidplaneJ4300": jnxMidplaneJ4300,
       "jnxMidplaneJ6300": jnxMidplaneJ6300,
       "jnxMidplaneIRM": jnxMidplaneIRM,
       "jnxMidplaneTX": jnxMidplaneTX,
       "jnxMidplaneM120": jnxMidplaneM120,
       "jnxMidplaneJ4350": jnxMidplaneJ4350,
       "jnxMidplaneJ6350": jnxMidplaneJ6350,
       "jnxMidplaneMX960": jnxMidplaneMX960,
       "jnxMidplaneJ4320": jnxMidplaneJ4320,
       "jnxMidplaneJ2320": jnxMidplaneJ2320,
       "jnxMidplaneJ2350": jnxMidplaneJ2350,
       "jnxMidplaneMX480": jnxMidplaneMX480,
       "jnxMidplaneSRX5800": jnxMidplaneSRX5800,
       "jnxMidplaneT1600": jnxMidplaneT1600,
       "jnxMidplaneSRX5600": jnxMidplaneSRX5600,
       "jnxMidplaneMX240": jnxMidplaneMX240,
       "jnxBackplaneEX8208": jnxBackplaneEX8208,
       "jnxMidplaneEX8216": jnxMidplaneEX8216,
       "jnxMidplaneSRX3600": jnxMidplaneSRX3600,
       "jnxMidplaneSRX3400": jnxMidplaneSRX3400,
       "jnxMidplaneSRX210": jnxMidplaneSRX210,
       "jnxMidplaneTXP": jnxMidplaneTXP,
       "jnxMidplaneJCS": jnxMidplaneJCS,
       "jnxMidplaneSRX240": jnxMidplaneSRX240,
       "jnxMidplaneSRX650": jnxMidplaneSRX650,
       "jnxMidplaneSRX100": jnxMidplaneSRX100,
       "jnxMidplaneLN1000V": jnxMidplaneLN1000V,
       "jnxMidplaneIBM4274M02J02M": jnxMidplaneIBM4274M02J02M,
       "jnxMidplaneIBM4274M06J06M": jnxMidplaneIBM4274M06J06M,
       "jnxMidplaneIBM4274M11J11M": jnxMidplaneIBM4274M11J11M,
       "jnxMidplaneSRX1400": jnxMidplaneSRX1400,
       "jnxMidplaneIBM4274S58J58S": jnxMidplaneIBM4274S58J58S,
       "jnxMidplaneIBM4274S56J56S": jnxMidplaneIBM4274S56J56S,
       "jnxMidplaneIBM4274S36J36S": jnxMidplaneIBM4274S36J36S,
       "jnxMidplaneIBM4274S34J34S": jnxMidplaneIBM4274S34J34S,
       "jnxBackplaneIBM4274E08J08E": jnxBackplaneIBM4274E08J08E,
       "jnxMidplaneIBM4274E16J16E": jnxMidplaneIBM4274E16J16E,
       "jnxMidplaneMX80": jnxMidplaneMX80,
       "jnxMidplaneSRX220": jnxMidplaneSRX220,
       "jnxBackplaneEXXRE": jnxBackplaneEXXRE,
       "jnxMidplaneQFXInterconnect": jnxMidplaneQFXInterconnect,
       "jnxMidplaneSRX110": jnxMidplaneSRX110,
       "jnxMidplaneSRX120": jnxMidplaneSRX120,
       "jnxMidplaneMAG8600": jnxMidplaneMAG8600,
       "jnxMidplaneMAG6611": jnxMidplaneMAG6611,
       "jnxMidplaneMAG6610": jnxMidplaneMAG6610,
       "jnxMidplanePTX5000": jnxMidplanePTX5000,
       "jnxMidplaneIBMJ08F": jnxMidplaneIBMJ08F,
       "jnxBackplaneEX6210": jnxBackplaneEX6210,
       "jnxMidplaneDELLJSRX3600": jnxMidplaneDELLJSRX3600,
       "jnxMidplaneDELLJSRX3400": jnxMidplaneDELLJSRX3400,
       "jnxMidplaneDELLJSRX1400": jnxMidplaneDELLJSRX1400,
       "jnxMidplaneDELLJSRX5800": jnxMidplaneDELLJSRX5800,
       "jnxMidplaneDELLJSRX5600": jnxMidplaneDELLJSRX5600,
       "jnxMidplaneT4000": jnxMidplaneT4000,
       "jnxMidplaneSRX550": jnxMidplaneSRX550,
       "jnxMidplaneACX": jnxMidplaneACX,
       "jnxMidplaneMX40": jnxMidplaneMX40,
       "jnxMidplaneMX10": jnxMidplaneMX10,
       "jnxMidplaneMX5": jnxMidplaneMX5,
       "jnxBackplaneMX2020": jnxBackplaneMX2020,
       "jnxBackplaneLowerMX2020": jnxBackplaneLowerMX2020,
       "jnxBackplaneUpperMX2020": jnxBackplaneUpperMX2020,
       "jnxBackplaneLowerPowerMX2020": jnxBackplaneLowerPowerMX2020,
       "jnxBackplaneUpperPowerMX2020": jnxBackplaneUpperPowerMX2020,
       "jnxMidplaneVseries": jnxMidplaneVseries,
       "jnxMidplaneLN2600": jnxMidplaneLN2600,
       "jnxMidplaneFireflyPerimeter": jnxMidplaneFireflyPerimeter,
       "jnxMidplaneMX104": jnxMidplaneMX104,
       "jnxMidplanePTX3000": jnxMidplanePTX3000,
       "jnxBackplaneMX2010": jnxBackplaneMX2010,
       "jnxBackplaneLowerMX2010": jnxBackplaneLowerMX2010,
       "jnxBackplaneUpperMX2010": jnxBackplaneUpperMX2010,
       "jnxBackplanePowerMX2010": jnxBackplanePowerMX2010,
       "jnxMidplaneLN2800": jnxMidplaneLN2800,
       "jnxMidplaneEX9214": jnxMidplaneEX9214,
       "jnxMidplaneEX9208": jnxMidplaneEX9208,
       "jnxMidplaneEX9204": jnxMidplaneEX9204,
       "jnxMidplaneSRX5400": jnxMidplaneSRX5400,
       "jnxMidplaneIBM4274S54J54S": jnxMidplaneIBM4274S54J54S,
       "jnxMidplaneDELLJSRX5400": jnxMidplaneDELLJSRX5400,
       "jnxMidplaneVMX": jnxMidplaneVMX,
       "jnxMidplaneVRR": jnxMidplaneVRR,
       "jnxMidplaneACX1000": jnxMidplaneACX1000,
       "jnxMidplaneACX2000": jnxMidplaneACX2000,
       "jnxMidplaneACX1100": jnxMidplaneACX1100,
       "jnxMidplaneACX2100": jnxMidplaneACX2100,
       "jnxMidplaneACX2200": jnxMidplaneACX2200,
       "jnxMidplaneACX4000": jnxMidplaneACX4000,
       "jnxMidplaneACX500AC": jnxMidplaneACX500AC,
       "jnxMidplaneACX500DC": jnxMidplaneACX500DC,
       "jnxMidplaneACX500OAC": jnxMidplaneACX500OAC,
       "jnxMidplaneACX500ODC": jnxMidplaneACX500ODC,
       "jnxMidplaneACX500OPOEAC": jnxMidplaneACX500OPOEAC,
       "jnxMidplaneACX500OPOEDC": jnxMidplaneACX500OPOEDC,
       "jnxMidplaneLN1000CC": jnxMidplaneLN1000CC,
       "jnxMidplaneVSRX": jnxMidplaneVSRX,
       "jnxMidplaneSRX300": jnxMidplaneSRX300,
       "jnxMidplaneSRX320": jnxMidplaneSRX320,
       "jnxMidplaneSRX340": jnxMidplaneSRX340,
       "jnxMidplaneSRX345": jnxMidplaneSRX345,
       "jnxMidplaneSRX1500": jnxMidplaneSRX1500,
       "jnxMidplaneSRX4100": jnxMidplaneSRX4100,
       "jnxMidplaneSRX4200": jnxMidplaneSRX4200,
       "jnxMidplaneMX2008": jnxMidplaneMX2008,
       "jnxBackMidplaneMX2008": jnxBackMidplaneMX2008,
       "jnxPowerMidplaneMX2008": jnxPowerMidplaneMX2008,
       "jnxMidplaneMXTSR80": jnxMidplaneMXTSR80,
       "jnxMidplaneACX5448": jnxMidplaneACX5448,
       "jnxMidplaneMX150": jnxMidplaneMX150,
       "jnxMidplaneJRR200": jnxMidplaneJRR200,
       "jnxMidplaneACX5448M": jnxMidplaneACX5448M,
       "jnxMidplaneACX5448D": jnxMidplaneACX5448D,
       "jnxMidplaneACX710": jnxMidplaneACX710,
       "jnxMidplaneACX5800": jnxMidplaneACX5800,
       "jnxMidplaneSRX380": jnxMidplaneSRX380,
       "jnxMidplaneR6675": jnxMidplaneR6675,
       "jnxMidplaneSRX1600": jnxMidplaneSRX1600,
       "jnxMidplaneSRX2300": jnxMidplaneSRX2300,
       "jnxMidplaneSRX4300": jnxMidplaneSRX4300,
       "jnxMidplaneACX7332": jnxMidplaneACX7332,
       "jnxMidplaneACX7348": jnxMidplaneACX7348,
       "jnxMidplaneSRX4700": jnxMidplaneSRX4700,
       "jnxModule": jnxModule,
       "jnxModuleM40": jnxModuleM40,
       "jnxModuleSCB": jnxModuleSCB,
       "jnxModuleFPC": jnxModuleFPC,
       "jnxCommonFPC": jnxCommonFPC,
       "jnxOc48FPC": jnxOc48FPC,
       "jnxModuleHostCtlr": jnxModuleHostCtlr,
       "jnxHostCtlrMaxi": jnxHostCtlrMaxi,
       "jnxHostCtlrMini": jnxHostCtlrMini,
       "jnxModulePowerSupply": jnxModulePowerSupply,
       "jnxPowerSupplyAC": jnxPowerSupplyAC,
       "jnxPowerSupplyDC": jnxPowerSupplyDC,
       "jnxModuleCooling": jnxModuleCooling,
       "jnxCoolingImpeller": jnxCoolingImpeller,
       "jnxCoolingFan": jnxCoolingFan,
       "jnxModuleFrontPanelDisplay": jnxModuleFrontPanelDisplay,
       "jnxModuleRoutingEngine": jnxModuleRoutingEngine,
       "jnxModuleM20": jnxModuleM20,
       "jnxM20FPC": jnxM20FPC,
       "jnxM20SSB": jnxM20SSB,
       "jnxM20RE": jnxM20RE,
       "jnxM20Power": jnxM20Power,
       "jnxM20PowerAC": jnxM20PowerAC,
       "jnxM20PowerDC": jnxM20PowerDC,
       "jnxM20Fan": jnxM20Fan,
       "jnxM20FrontPanel": jnxM20FrontPanel,
       "jnxModuleM160": jnxModuleM160,
       "jnxM160FPC": jnxM160FPC,
       "jnxM160SFM": jnxM160SFM,
       "jnxM160HM": jnxM160HM,
       "jnxM160PCG": jnxM160PCG,
       "jnxM160Power": jnxM160Power,
       "jnxM160Fan": jnxM160Fan,
       "jnxM160MCS": jnxM160MCS,
       "jnxM160FPM": jnxM160FPM,
       "jnxM160CIP": jnxM160CIP,
       "jnxModuleM10": jnxModuleM10,
       "jnxM10FPC": jnxM10FPC,
       "jnxM10FEB": jnxM10FEB,
       "jnxM10RE": jnxM10RE,
       "jnxM10Power": jnxM10Power,
       "jnxM10PowerAC": jnxM10PowerAC,
       "jnxM10PowerDC": jnxM10PowerDC,
       "jnxM10Fan": jnxM10Fan,
       "jnxModuleM5": jnxModuleM5,
       "jnxM5FPC": jnxM5FPC,
       "jnxM5FEB": jnxM5FEB,
       "jnxM5RE": jnxM5RE,
       "jnxM5Power": jnxM5Power,
       "jnxM5PowerAC": jnxM5PowerAC,
       "jnxM5PowerDC": jnxM5PowerDC,
       "jnxM5Fan": jnxM5Fan,
       "jnxModuleT640": jnxModuleT640,
       "jnxT640FPC": jnxT640FPC,
       "jnxT640SIB": jnxT640SIB,
       "jnxT640HM": jnxT640HM,
       "jnxT640SCG": jnxT640SCG,
       "jnxT640Power": jnxT640Power,
       "jnxT640Fan": jnxT640Fan,
       "jnxT640CB": jnxT640CB,
       "jnxT640FPB": jnxT640FPB,
       "jnxT640CIP": jnxT640CIP,
       "jnxT640SPMB": jnxT640SPMB,
       "jnxModuleT320": jnxModuleT320,
       "jnxT320FPC": jnxT320FPC,
       "jnxT320SIB": jnxT320SIB,
       "jnxT320HM": jnxT320HM,
       "jnxT320SCG": jnxT320SCG,
       "jnxT320Power": jnxT320Power,
       "jnxT320Fan": jnxT320Fan,
       "jnxT320CB": jnxT320CB,
       "jnxT320FPB": jnxT320FPB,
       "jnxT320CIP": jnxT320CIP,
       "jnxT320SPMB": jnxT320SPMB,
       "jnxModuleM40e": jnxModuleM40e,
       "jnxM40eFPC": jnxM40eFPC,
       "jnxM40eSFM": jnxM40eSFM,
       "jnxM40eHM": jnxM40eHM,
       "jnxM40ePCG": jnxM40ePCG,
       "jnxM40ePower": jnxM40ePower,
       "jnxM40eFan": jnxM40eFan,
       "jnxM40eMCS": jnxM40eMCS,
       "jnxM40eFPM": jnxM40eFPM,
       "jnxM40eCIP": jnxM40eCIP,
       "jnxModuleM320": jnxModuleM320,
       "jnxM320FPC": jnxM320FPC,
       "jnxM320SIB": jnxM320SIB,
       "jnxM320HM": jnxM320HM,
       "jnxM320Power": jnxM320Power,
       "jnxM320Fan": jnxM320Fan,
       "jnxM320CB": jnxM320CB,
       "jnxM320FPB": jnxM320FPB,
       "jnxM320CIP": jnxM320CIP,
       "jnxModuleM7i": jnxModuleM7i,
       "jnxM7iFPC": jnxM7iFPC,
       "jnxM7iCFEB": jnxM7iCFEB,
       "jnxM7iRE": jnxM7iRE,
       "jnxM7iPower": jnxM7iPower,
       "jnxM7iPowerAC": jnxM7iPowerAC,
       "jnxM7iFan": jnxM7iFan,
       "jnxModuleM10i": jnxModuleM10i,
       "jnxM10iFPC": jnxM10iFPC,
       "jnxM10iCFEB": jnxM10iCFEB,
       "jnxM10iRE": jnxM10iRE,
       "jnxM10iPower": jnxM10iPower,
       "jnxM10iPowerAC": jnxM10iPowerAC,
       "jnxM10iFan": jnxM10iFan,
       "jnxM10iHCM": jnxM10iHCM,
       "jnxModuleGeneric": jnxModuleGeneric,
       "jnxFPC": jnxFPC,
       "jnxCBD": jnxCBD,
       "jnxHM": jnxHM,
       "jnxPCMCIACard": jnxPCMCIACard,
       "jnxUSBHub": jnxUSBHub,
       "jnxRCompactFlash": jnxRCompactFlash,
       "jnxPower": jnxPower,
       "jnxFan": jnxFan,
       "jnxFPB": jnxFPB,
       "jnxCIP": jnxCIP,
       "jnxSIB": jnxSIB,
       "jnxSFB": jnxSFB,
       "jnxFTC": jnxFTC,
       "jnxFEB": jnxFEB,
       "jnxTIB": jnxTIB,
       "jnxModuleJ2300": jnxModuleJ2300,
       "jnxJ2300FPC": jnxJ2300FPC,
       "jnxJ2300RE": jnxJ2300RE,
       "jnxJ2300Fan": jnxJ2300Fan,
       "jnxModuleJ4300": jnxModuleJ4300,
       "jnxJ4300FPC": jnxJ4300FPC,
       "jnxJ4300RE": jnxJ4300RE,
       "jnxJ4300Fan": jnxJ4300Fan,
       "jnxModuleJ6300": jnxModuleJ6300,
       "jnxJ6300FPC": jnxJ6300FPC,
       "jnxJ6300RE": jnxJ6300RE,
       "jnxJ6300Fan": jnxJ6300Fan,
       "jnxModuleIRM": jnxModuleIRM,
       "jnxIRMFPC": jnxIRMFPC,
       "jnxIRMCFEB": jnxIRMCFEB,
       "jnxIRMRE": jnxIRMRE,
       "jnxIRMPower": jnxIRMPower,
       "jnxIRMPowerDC": jnxIRMPowerDC,
       "jnxModuleTX": jnxModuleTX,
       "jnxTXSIB": jnxTXSIB,
       "jnxTXHM": jnxTXHM,
       "jnxTXPower": jnxTXPower,
       "jnxTXFan": jnxTXFan,
       "jnxTXCB": jnxTXCB,
       "jnxTXFPB": jnxTXFPB,
       "jnxTXCIP": jnxTXCIP,
       "jnxTXSPMB": jnxTXSPMB,
       "jnxTXLCC": jnxTXLCC,
       "jnxModuleM120": jnxModuleM120,
       "jnxM120FEB": jnxM120FEB,
       "jnxModuleJ4350": jnxModuleJ4350,
       "jnxJ4350FPC": jnxJ4350FPC,
       "jnxJ4350RE": jnxJ4350RE,
       "jnxJ4350Power": jnxJ4350Power,
       "jnxJ4350Fan": jnxJ4350Fan,
       "jnxModuleJ6350": jnxModuleJ6350,
       "jnxJ6350FPC": jnxJ6350FPC,
       "jnxJ6350RE": jnxJ6350RE,
       "jnxJ6350Power": jnxJ6350Power,
       "jnxJ6350Fan": jnxJ6350Fan,
       "jnxModuleJ4320": jnxModuleJ4320,
       "jnxJ4320FPC": jnxJ4320FPC,
       "jnxJ4320RE": jnxJ4320RE,
       "jnxModuleJ2320": jnxModuleJ2320,
       "jnxJ2320FPC": jnxJ2320FPC,
       "jnxJ2320RE": jnxJ2320RE,
       "jnxJ2320Power": jnxJ2320Power,
       "jnxJ2320Fan": jnxJ2320Fan,
       "jnxModuleJ2350": jnxModuleJ2350,
       "jnxJ2350FPC": jnxJ2350FPC,
       "jnxJ2350RE": jnxJ2350RE,
       "jnxJ2350Power": jnxJ2350Power,
       "jnxJ2350Fan": jnxJ2350Fan,
       "jnxModuleT1600": jnxModuleT1600,
       "jnxT1600FPC": jnxT1600FPC,
       "jnxT1600SIB": jnxT1600SIB,
       "jnxT1600HM": jnxT1600HM,
       "jnxT1600SCG": jnxT1600SCG,
       "jnxT1600Power": jnxT1600Power,
       "jnxT1600Fan": jnxT1600Fan,
       "jnxT1600CB": jnxT1600CB,
       "jnxT1600FPB": jnxT1600FPB,
       "jnxT1600CIP": jnxT1600CIP,
       "jnxT1600SPMB": jnxT1600SPMB,
       "jnxModuleEX3200": jnxModuleEX3200,
       "jnxEX3200FPC": jnxEX3200FPC,
       "jnxEX3200Power": jnxEX3200Power,
       "jnxEX3200Fan": jnxEX3200Fan,
       "jnxEX3200RE": jnxEX3200RE,
       "jnxModuleEX4200": jnxModuleEX4200,
       "jnxEX4200FPC": jnxEX4200FPC,
       "jnxEX4200Power": jnxEX4200Power,
       "jnxEX4200Fan": jnxEX4200Fan,
       "jnxModuleSRX210": jnxModuleSRX210,
       "jnxSRX210FPC": jnxSRX210FPC,
       "jnxSRX210RE": jnxSRX210RE,
       "jnxSRX210Power": jnxSRX210Power,
       "jnxSRX210Fan": jnxSRX210Fan,
       "jnxModuleTXP": jnxModuleTXP,
       "jnxTXPSIB": jnxTXPSIB,
       "jnxTXPHM": jnxTXPHM,
       "jnxTXPPower": jnxTXPPower,
       "jnxTXPFan": jnxTXPFan,
       "jnxTXPCB": jnxTXPCB,
       "jnxTXPFPB": jnxTXPFPB,
       "jnxTXPCIP": jnxTXPCIP,
       "jnxTXPSPMB": jnxTXPSPMB,
       "jnxTXPLCC": jnxTXPLCC,
       "jnxTXPSFC": jnxTXPSFC,
       "jnxModuleJCS": jnxModuleJCS,
       "jnxJCSHM": jnxJCSHM,
       "jnxJCSBBD": jnxJCSBBD,
       "jnxJCSFPC": jnxJCSFPC,
       "jnxJCSPIC": jnxJCSPIC,
       "jnxModuleSRX240": jnxModuleSRX240,
       "jnxSRX240FPC": jnxSRX240FPC,
       "jnxSRX240RE": jnxSRX240RE,
       "jnxSRX240Power": jnxSRX240Power,
       "jnxSRX240Fan": jnxSRX240Fan,
       "jnxModuleSRX650": jnxModuleSRX650,
       "jnxSRX650FPC": jnxSRX650FPC,
       "jnxSRX650RE": jnxSRX650RE,
       "jnxSRX650Power": jnxSRX650Power,
       "jnxSRX650Fan": jnxSRX650Fan,
       "jnxModuleSRX100": jnxModuleSRX100,
       "jnxSRX100FPC": jnxSRX100FPC,
       "jnxSRX100RE": jnxSRX100RE,
       "jnxSRX100Power": jnxSRX100Power,
       "jnxSRX100Fan": jnxSRX100Fan,
       "jnxModuleEX2200": jnxModuleEX2200,
       "jnxEX2200FPC": jnxEX2200FPC,
       "jnxEX2200Power": jnxEX2200Power,
       "jnxEX2200Fan": jnxEX2200Fan,
       "jnxEX2200RE": jnxEX2200RE,
       "jnxModuleEX4500": jnxModuleEX4500,
       "jnxEX4500FPC": jnxEX4500FPC,
       "jnxEX4500Power": jnxEX4500Power,
       "jnxEX4500Fan": jnxEX4500Fan,
       "jnxEX4500RE": jnxEX4500RE,
       "jnxModuleIBM427348EJ48E": jnxModuleIBM427348EJ48E,
       "jnxIBM427348EJ48EFPC": jnxIBM427348EJ48EFPC,
       "jnxIBM427348EJ48EPower": jnxIBM427348EJ48EPower,
       "jnxIBM427348EJ48EFan": jnxIBM427348EJ48EFan,
       "jnxModuleMX80": jnxModuleMX80,
       "jnxMX80FPC": jnxMX80FPC,
       "jnxMX80CFEB": jnxMX80CFEB,
       "jnxMX80RE": jnxMX80RE,
       "jnxMX80Power": jnxMX80Power,
       "jnxMX80PowerAC": jnxMX80PowerAC,
       "jnxMX80Fan": jnxMX80Fan,
       "jnxModuleSRX220": jnxModuleSRX220,
       "jnxSRX220FPC": jnxSRX220FPC,
       "jnxSRX220RE": jnxSRX220RE,
       "jnxSRX220Power": jnxSRX220Power,
       "jnxSRX220Fan": jnxSRX220Fan,
       "jnxModuleEXXRE": jnxModuleEXXRE,
       "jnxEXXREPower": jnxEXXREPower,
       "jnxEXXREFan": jnxEXXREFan,
       "jnxEXXREHM": jnxEXXREHM,
       "jnxEXXRELCC": jnxEXXRELCC,
       "jnxModuleEX4300": jnxModuleEX4300,
       "jnxEX4300FPC": jnxEX4300FPC,
       "jnxEX4300Power": jnxEX4300Power,
       "jnxEX4300Fan": jnxEX4300Fan,
       "jnxModuleSRX110": jnxModuleSRX110,
       "jnxSRX110FPC": jnxSRX110FPC,
       "jnxSRX110RE": jnxSRX110RE,
       "jnxSRX110Power": jnxSRX110Power,
       "jnxSRX110Fan": jnxSRX110Fan,
       "jnxModuleSRX120": jnxModuleSRX120,
       "jnxSRX120FPC": jnxSRX120FPC,
       "jnxSRX120RE": jnxSRX120RE,
       "jnxSRX120Power": jnxSRX120Power,
       "jnxSRX120Fan": jnxSRX120Fan,
       "jnxModulePTX5000": jnxModulePTX5000,
       "jnxPTX5000SIB": jnxPTX5000SIB,
       "jnxPTX5000HM": jnxPTX5000HM,
       "jnxPTX5000FPC": jnxPTX5000FPC,
       "jnxPTX5000Fan": jnxPTX5000Fan,
       "jnxPTX5000CB": jnxPTX5000CB,
       "jnxPTX5000FPB": jnxPTX5000FPB,
       "jnxPTX5000SPMB": jnxPTX5000SPMB,
       "jnxPTX5000PDU": jnxPTX5000PDU,
       "jnxPTX5000PSM": jnxPTX5000PSM,
       "jnxPTX5000CCG": jnxPTX5000CCG,
       "jnxPTX5000PIC": jnxPTX5000PIC,
       "jnxModuleIBM0719J45E": jnxModuleIBM0719J45E,
       "jnxIBM0719J45EFPC": jnxIBM0719J45EFPC,
       "jnxIBM0719J45EPower": jnxIBM0719J45EPower,
       "jnxIBM0719J45EFan": jnxIBM0719J45EFan,
       "jnxIBM0719J45ERE": jnxIBM0719J45ERE,
       "jnxModuleEX3300": jnxModuleEX3300,
       "jnxEX3300FPC": jnxEX3300FPC,
       "jnxEX3300Power": jnxEX3300Power,
       "jnxEX3300Fan": jnxEX3300Fan,
       "jnxEX3300RE": jnxEX3300RE,
       "jnxModuleT4000": jnxModuleT4000,
       "jnxT4000SIB": jnxT4000SIB,
       "jnxT4000SCG": jnxT4000SCG,
       "jnxT4000CB": jnxT4000CB,
       "jnxT4000SPMB": jnxT4000SPMB,
       "jnxModuleSRX550": jnxModuleSRX550,
       "jnxSRX550FPC": jnxSRX550FPC,
       "jnxSRX550RE": jnxSRX550RE,
       "jnxSRX550Power": jnxSRX550Power,
       "jnxSRX550Fan": jnxSRX550Fan,
       "jnxModuleACX": jnxModuleACX,
       "jnxACXFPC": jnxACXFPC,
       "jnxACXFEB": jnxACXFEB,
       "jnxACXRE": jnxACXRE,
       "jnxACXPower": jnxACXPower,
       "jnxACXPowerDC": jnxACXPowerDC,
       "jnxACXPowerAC": jnxACXPowerAC,
       "jnxACXFan": jnxACXFan,
       "jnxModuleMX40": jnxModuleMX40,
       "jnxMX40FPC": jnxMX40FPC,
       "jnxMX40CFEB": jnxMX40CFEB,
       "jnxMX40RE": jnxMX40RE,
       "jnxMX40Power": jnxMX40Power,
       "jnxMX40PowerAC": jnxMX40PowerAC,
       "jnxMX40Fan": jnxMX40Fan,
       "jnxModuleMX10": jnxModuleMX10,
       "jnxMX10FPC": jnxMX10FPC,
       "jnxMX10CFEB": jnxMX10CFEB,
       "jnxMX10RE": jnxMX10RE,
       "jnxMX10Power": jnxMX10Power,
       "jnxMX10PowerAC": jnxMX10PowerAC,
       "jnxMX10Fan": jnxMX10Fan,
       "jnxModuleMX5": jnxModuleMX5,
       "jnxMX5FPC": jnxMX5FPC,
       "jnxMX5CFEB": jnxMX5CFEB,
       "jnxMX5RE": jnxMX5RE,
       "jnxMX5Power": jnxMX5Power,
       "jnxMX5PowerAC": jnxMX5PowerAC,
       "jnxMX5Fan": jnxMX5Fan,
       "jnxModuleEX4550": jnxModuleEX4550,
       "jnxEX4550FPC": jnxEX4550FPC,
       "jnxEX4550Power": jnxEX4550Power,
       "jnxEX4550Fan": jnxEX4550Fan,
       "jnxEX4550RE": jnxEX4550RE,
       "jnxModuleMX2020": jnxModuleMX2020,
       "jnxMX2020SFB": jnxMX2020SFB,
       "jnxMX2020HM": jnxMX2020HM,
       "jnxMX2020FPC": jnxMX2020FPC,
       "jnxMX2020Fan": jnxMX2020Fan,
       "jnxMX2020CB": jnxMX2020CB,
       "jnxMX2020FPB": jnxMX2020FPB,
       "jnxMX2020SPMB": jnxMX2020SPMB,
       "jnxMX2020PDM": jnxMX2020PDM,
       "jnxMX2020PSM": jnxMX2020PSM,
       "jnxMX2020ADC": jnxMX2020ADC,
       "jnxModuleVseries": jnxModuleVseries,
       "jnxVseriesFPC": jnxVseriesFPC,
       "jnxVseriesRE": jnxVseriesRE,
       "jnxVseriesPower": jnxVseriesPower,
       "jnxVseriesFan": jnxVseriesFan,
       "jnxModuleFireflyPerimeter": jnxModuleFireflyPerimeter,
       "jnxFireflyPerimeterFPC": jnxFireflyPerimeterFPC,
       "jnxFireflyPerimeterRE": jnxFireflyPerimeterRE,
       "jnxFireflyPerimeterPower": jnxFireflyPerimeterPower,
       "jnxFireflyPerimeterFan": jnxFireflyPerimeterFan,
       "jnxModuleMX104": jnxModuleMX104,
       "jnxMX104FPC": jnxMX104FPC,
       "jnxMX104FEB": jnxMX104FEB,
       "jnxMX104RE": jnxMX104RE,
       "jnxMX104Power": jnxMX104Power,
       "jnxMX104PowerAC": jnxMX104PowerAC,
       "jnxMX104Fan": jnxMX104Fan,
       "jnxMX104FPM": jnxMX104FPM,
       "jnxModulePTX3000": jnxModulePTX3000,
       "jnxPTX3000SIB": jnxPTX3000SIB,
       "jnxPTX3000HM": jnxPTX3000HM,
       "jnxPTX3000FPC": jnxPTX3000FPC,
       "jnxPTX3000Fan": jnxPTX3000Fan,
       "jnxPTX3000CB": jnxPTX3000CB,
       "jnxPTX3000FPB": jnxPTX3000FPB,
       "jnxPTX3000PSM": jnxPTX3000PSM,
       "jnxPTX3000PIC": jnxPTX3000PIC,
       "jnxModuleMX2010": jnxModuleMX2010,
       "jnxMX2010SFB": jnxMX2010SFB,
       "jnxMX2010HM": jnxMX2010HM,
       "jnxMX2010FPC": jnxMX2010FPC,
       "jnxMX2010Fan": jnxMX2010Fan,
       "jnxMX2010CB": jnxMX2010CB,
       "jnxMX2010FPB": jnxMX2010FPB,
       "jnxMX2010SPMB": jnxMX2010SPMB,
       "jnxMX2010PDM": jnxMX2010PDM,
       "jnxMX2010PSM": jnxMX2010PSM,
       "jnxMX2010ADC": jnxMX2010ADC,
       "jnxModuleLN2800": jnxModuleLN2800,
       "jnxLN2800FPC": jnxLN2800FPC,
       "jnxLN2800RE": jnxLN2800RE,
       "jnxLN2800Power": jnxLN2800Power,
       "jnxModuleVRR": jnxModuleVRR,
       "jnxVRRFPC": jnxVRRFPC,
       "jnxVRRRE": jnxVRRRE,
       "jnxVRRPower": jnxVRRPower,
       "jnxVRRFan": jnxVRRFan,
       "jnxModuleACX1000": jnxModuleACX1000,
       "jnxACX1000FPC": jnxACX1000FPC,
       "jnxACX1000FEB": jnxACX1000FEB,
       "jnxACX1000RE": jnxACX1000RE,
       "jnxACX1000Power": jnxACX1000Power,
       "jnxACX1000PowerDC": jnxACX1000PowerDC,
       "jnxModuleACX2000": jnxModuleACX2000,
       "jnxACX2000FPC": jnxACX2000FPC,
       "jnxACX2000FEB": jnxACX2000FEB,
       "jnxACX2000RE": jnxACX2000RE,
       "jnxACX2000Power": jnxACX2000Power,
       "jnxACX2000PowerDC": jnxACX2000PowerDC,
       "jnxModuleACX1100": jnxModuleACX1100,
       "jnxACX1100FPC": jnxACX1100FPC,
       "jnxACX1100FEB": jnxACX1100FEB,
       "jnxACX1100RE": jnxACX1100RE,
       "jnxACX1100Power": jnxACX1100Power,
       "jnxACX1100PowerDC": jnxACX1100PowerDC,
       "jnxACX1100PowerAC": jnxACX1100PowerAC,
       "jnxModuleACX2100": jnxModuleACX2100,
       "jnxACX2100FPC": jnxACX2100FPC,
       "jnxACX2100FEB": jnxACX2100FEB,
       "jnxACX2100RE": jnxACX2100RE,
       "jnxACX2100Power": jnxACX2100Power,
       "jnxACX2100PowerDC": jnxACX2100PowerDC,
       "jnxACX2100PowerAC": jnxACX2100PowerAC,
       "jnxModuleACX2200": jnxModuleACX2200,
       "jnxACX2200FPC": jnxACX2200FPC,
       "jnxACX2200FEB": jnxACX2200FEB,
       "jnxACX2200RE": jnxACX2200RE,
       "jnxACX2200Power": jnxACX2200Power,
       "jnxACX2200PowerDC": jnxACX2200PowerDC,
       "jnxACX2200PowerAC": jnxACX2200PowerAC,
       "jnxModuleACX4000": jnxModuleACX4000,
       "jnxACX4000FPC": jnxACX4000FPC,
       "jnxACX4000FEB": jnxACX4000FEB,
       "jnxACX4000RE": jnxACX4000RE,
       "jnxACX4000Power": jnxACX4000Power,
       "jnxACX4000PowerDC": jnxACX4000PowerDC,
       "jnxACX4000PowerAC": jnxACX4000PowerAC,
       "jnxACX4000Fan": jnxACX4000Fan,
       "jnxModuleACX500AC": jnxModuleACX500AC,
       "jnxACX500ACFPC": jnxACX500ACFPC,
       "jnxACX500ACFEB": jnxACX500ACFEB,
       "jnxACX500ACRE": jnxACX500ACRE,
       "jnxACX500ACPower": jnxACX500ACPower,
       "jnxACX500ACPowerAC": jnxACX500ACPowerAC,
       "jnxModuleACX500DC": jnxModuleACX500DC,
       "jnxACX500DCFPC": jnxACX500DCFPC,
       "jnxACX500DCFEB": jnxACX500DCFEB,
       "jnxACX500DCRE": jnxACX500DCRE,
       "jnxACX500DCPower": jnxACX500DCPower,
       "jnxACX500DCPowerDC": jnxACX500DCPowerDC,
       "jnxModuleACX500OAC": jnxModuleACX500OAC,
       "jnxACX500OACFPC": jnxACX500OACFPC,
       "jnxACX500OACFEB": jnxACX500OACFEB,
       "jnxACX500OACRE": jnxACX500OACRE,
       "jnxACX500OACPower": jnxACX500OACPower,
       "jnxACX500OACPowerAC": jnxACX500OACPowerAC,
       "jnxModuleACX500ODC": jnxModuleACX500ODC,
       "jnxACX500ODCFPC": jnxACX500ODCFPC,
       "jnxACX500ODCFEB": jnxACX500ODCFEB,
       "jnxACX500ODCRE": jnxACX500ODCRE,
       "jnxACX500ODCPower": jnxACX500ODCPower,
       "jnxACX500ODCPowerDC": jnxACX500ODCPowerDC,
       "jnxModuleACX500OPOEAC": jnxModuleACX500OPOEAC,
       "jnxACX500OPOEACFPC": jnxACX500OPOEACFPC,
       "jnxACX500OPOEACFEB": jnxACX500OPOEACFEB,
       "jnxACX500OPOEACRE": jnxACX500OPOEACRE,
       "jnxACX500OPOEACPower": jnxACX500OPOEACPower,
       "jnxACX500OPOEACPowerAC": jnxACX500OPOEACPowerAC,
       "jnxModuleACX500OPOEDC": jnxModuleACX500OPOEDC,
       "jnxACX500OPOEDCFPC": jnxACX500OPOEDCFPC,
       "jnxACX500OPOEDCFEB": jnxACX500OPOEDCFEB,
       "jnxACX500OPOEDCRE": jnxACX500OPOEDCRE,
       "jnxACX500OPOEDCPower": jnxACX500OPOEDCPower,
       "jnxACX500OPOEDCPowerDC": jnxACX500OPOEDCPowerDC,
       "jnxModuleVSRX": jnxModuleVSRX,
       "jnxVSRXFPC": jnxVSRXFPC,
       "jnxVSRXRE": jnxVSRXRE,
       "jnxVSRXPower": jnxVSRXPower,
       "jnxVSRXFan": jnxVSRXFan,
       "jnxModuleEX3400": jnxModuleEX3400,
       "jnxEX3400FPC": jnxEX3400FPC,
       "jnxEX3400Power": jnxEX3400Power,
       "jnxEX3400Fan": jnxEX3400Fan,
       "jnxModuleEX2300": jnxModuleEX2300,
       "jnxEX2300FPC": jnxEX2300FPC,
       "jnxEX2300Power": jnxEX2300Power,
       "jnxEX2300Fan": jnxEX2300Fan,
       "jnxModuleSRX300": jnxModuleSRX300,
       "jnxSRX300FPC": jnxSRX300FPC,
       "jnxSRX300RE": jnxSRX300RE,
       "jnxSRX300Power": jnxSRX300Power,
       "jnxSRX300Fan": jnxSRX300Fan,
       "jnxModuleSRX320": jnxModuleSRX320,
       "jnxSRX320FPC": jnxSRX320FPC,
       "jnxSRX320RE": jnxSRX320RE,
       "jnxSRX320Power": jnxSRX320Power,
       "jnxSRX320Fan": jnxSRX320Fan,
       "jnxModuleSRX340": jnxModuleSRX340,
       "jnxSRX340FPC": jnxSRX340FPC,
       "jnxSRX340RE": jnxSRX340RE,
       "jnxSRX340Power": jnxSRX340Power,
       "jnxSRX340Fan": jnxSRX340Fan,
       "jnxModuleSRX345": jnxModuleSRX345,
       "jnxSRX345FPC": jnxSRX345FPC,
       "jnxSRX345RE": jnxSRX345RE,
       "jnxSRX345Power": jnxSRX345Power,
       "jnxSRX345Fan": jnxSRX345Fan,
       "jnxModuleSRX1500": jnxModuleSRX1500,
       "jnxSRX1500FPC": jnxSRX1500FPC,
       "jnxSRX1500RE": jnxSRX1500RE,
       "jnxSRX1500Power": jnxSRX1500Power,
       "jnxSRX1500Fan": jnxSRX1500Fan,
       "jnxSRX1500CB": jnxSRX1500CB,
       "jnxModuleJNP10003": jnxModuleJNP10003,
       "jnxJNP10003HM": jnxJNP10003HM,
       "jnxJNP10003FPC": jnxJNP10003FPC,
       "jnxJNP10003Fan": jnxJNP10003Fan,
       "jnxJNP10003CB": jnxJNP10003CB,
       "jnxJNP10003Power": jnxJNP10003Power,
       "jnxModuleSRX4600": jnxModuleSRX4600,
       "jnxSRX4600HM": jnxSRX4600HM,
       "jnxSRX4600FPC": jnxSRX4600FPC,
       "jnxSRX4600Fan": jnxSRX4600Fan,
       "jnxSRX4600SPMB": jnxSRX4600SPMB,
       "jnxSRX4600PSM": jnxSRX4600PSM,
       "jnxModuleSRX4800": jnxModuleSRX4800,
       "jnxSRX4800HM": jnxSRX4800HM,
       "jnxSRX4800FPC": jnxSRX4800FPC,
       "jnxSRX4800Fan": jnxSRX4800Fan,
       "jnxSRX4800SPMB": jnxSRX4800SPMB,
       "jnxSRX4800PSM": jnxSRX4800PSM,
       "jnxModuleSRX4100": jnxModuleSRX4100,
       "jnxSRX4100FPC": jnxSRX4100FPC,
       "jnxSRX4100RE": jnxSRX4100RE,
       "jnxSRX4100Power": jnxSRX4100Power,
       "jnxSRX4100Fan": jnxSRX4100Fan,
       "jnxModuleSRX4200": jnxModuleSRX4200,
       "jnxSRX4200FPC": jnxSRX4200FPC,
       "jnxSRX4200RE": jnxSRX4200RE,
       "jnxSRX4200Power": jnxSRX4200Power,
       "jnxSRX4200Fan": jnxSRX4200Fan,
       "jnxModuleJNP204": jnxModuleJNP204,
       "jnxJNP204HM": jnxJNP204HM,
       "jnxJNP204FPC": jnxJNP204FPC,
       "jnxJNP204Fan": jnxJNP204Fan,
       "jnxJNP204CB": jnxJNP204CB,
       "jnxJNP204Power": jnxJNP204Power,
       "jnxModuleMX2008": jnxModuleMX2008,
       "jnxMX2008SFB": jnxMX2008SFB,
       "jnxMX2008HM": jnxMX2008HM,
       "jnxMX2008FPC": jnxMX2008FPC,
       "jnxMX2008Fan": jnxMX2008Fan,
       "jnxMX2008RCB": jnxMX2008RCB,
       "jnxMX2008FPB": jnxMX2008FPB,
       "jnxMX2008PDM": jnxMX2008PDM,
       "jnxMX2008PSM": jnxMX2008PSM,
       "jnxMX2008ADC": jnxMX2008ADC,
       "jnxModuleMXTSR80": jnxModuleMXTSR80,
       "jnxMXTSR80FPC": jnxMXTSR80FPC,
       "jnxMXTSR80FEB": jnxMXTSR80FEB,
       "jnxMXTSR80RE": jnxMXTSR80RE,
       "jnxMXTSR80Power": jnxMXTSR80Power,
       "jnxMXTSR80PowerAC": jnxMXTSR80PowerAC,
       "jnxMXTSR80Fan": jnxMXTSR80Fan,
       "jnxMXTSR80FPM": jnxMXTSR80FPM,
       "jnxModulePTX10008": jnxModulePTX10008,
       "jnxPTX10008FPC": jnxPTX10008FPC,
       "jnxPTX10008HM": jnxPTX10008HM,
       "jnxPTX10008Power": jnxPTX10008Power,
       "jnxPTX10008Fan": jnxPTX10008Fan,
       "jnxPTX10008FPB": jnxPTX10008FPB,
       "jnxPTX10008CBD": jnxPTX10008CBD,
       "jnxPTX10008SIB": jnxPTX10008SIB,
       "jnxPTX10008FPM": jnxPTX10008FPM,
       "jnxPTX10008FTC": jnxPTX10008FTC,
       "jnxPTX10008Backplane": jnxPTX10008Backplane,
       "jnxModuleACX5448": jnxModuleACX5448,
       "jnxACX5448FPC": jnxACX5448FPC,
       "jnxACX5448FEB": jnxACX5448FEB,
       "jnxACX5448RE": jnxACX5448RE,
       "jnxACX5448Power": jnxACX5448Power,
       "jnxACX5448PowerDC": jnxACX5448PowerDC,
       "jnxACX5448PowerAC": jnxACX5448PowerAC,
       "jnxACX5448Fan": jnxACX5448Fan,
       "jnxModulePTX10016": jnxModulePTX10016,
       "jnxPTX10016FPC": jnxPTX10016FPC,
       "jnxPTX10016HM": jnxPTX10016HM,
       "jnxPTX10016Power": jnxPTX10016Power,
       "jnxPTX10016Fan": jnxPTX10016Fan,
       "jnxPTX10016FPB": jnxPTX10016FPB,
       "jnxPTX10016CBD": jnxPTX10016CBD,
       "jnxPTX10016SIB": jnxPTX10016SIB,
       "jnxPTX10016FTC": jnxPTX10016FTC,
       "jnxPTX10016Backplane": jnxPTX10016Backplane,
       "jnxModuleEX9251": jnxModuleEX9251,
       "jnxEX9251HM": jnxEX9251HM,
       "jnxEX9251FPC": jnxEX9251FPC,
       "jnxEX9251Fan": jnxEX9251Fan,
       "jnxEX9251CB": jnxEX9251CB,
       "jnxEX9251Power": jnxEX9251Power,
       "jnxModuleJNP10001": jnxModuleJNP10001,
       "jnxJNP10001HM": jnxJNP10001HM,
       "jnxJNP10001FPC": jnxJNP10001FPC,
       "jnxJNP10001Fan": jnxJNP10001Fan,
       "jnxJNP10001Power": jnxJNP10001Power,
       "jnxModuleMX10008": jnxModuleMX10008,
       "jnxMX10008SFB": jnxMX10008SFB,
       "jnxMX10008HM": jnxMX10008HM,
       "jnxMX10008FPC": jnxMX10008FPC,
       "jnxMX10008Fan": jnxMX10008Fan,
       "jnxMX10008CBD": jnxMX10008CBD,
       "jnxMX10008Power": jnxMX10008Power,
       "jnxMX10008FPB": jnxMX10008FPB,
       "jnxMX10008FTC": jnxMX10008FTC,
       "jnxModuleMX10016": jnxModuleMX10016,
       "jnxMX10016SFB": jnxMX10016SFB,
       "jnxMX10016HM": jnxMX10016HM,
       "jnxMX10016FPC": jnxMX10016FPC,
       "jnxMX10016Fan": jnxMX10016Fan,
       "jnxMX10016CBD": jnxMX10016CBD,
       "jnxMX10016Power": jnxMX10016Power,
       "jnxMX10016FPB": jnxMX10016FPB,
       "jnxModuleEX9253": jnxModuleEX9253,
       "jnxEX9253HM": jnxEX9253HM,
       "jnxEX9253FPC": jnxEX9253FPC,
       "jnxEX9253Fan": jnxEX9253Fan,
       "jnxEX9253CB": jnxEX9253CB,
       "jnxEX9253Power": jnxEX9253Power,
       "jnxModuleJRR200": jnxModuleJRR200,
       "jnxJRR200RE": jnxJRR200RE,
       "jnxJRR200Power": jnxJRR200Power,
       "jnxJRR200Fan": jnxJRR200Fan,
       "jnxModuleACX5448M": jnxModuleACX5448M,
       "jnxACX5448MFPC": jnxACX5448MFPC,
       "jnxACX5448MFEB": jnxACX5448MFEB,
       "jnxACX5448MRE": jnxACX5448MRE,
       "jnxACX5448MPower": jnxACX5448MPower,
       "jnxACX5448MPowerDC": jnxACX5448MPowerDC,
       "jnxACX5448MPowerAC": jnxACX5448MPowerAC,
       "jnxACX5448MFan": jnxACX5448MFan,
       "jnxModuleACX5448D": jnxModuleACX5448D,
       "jnxACX5448DFPC": jnxACX5448DFPC,
       "jnxACX5448DFEB": jnxACX5448DFEB,
       "jnxACX5448DRE": jnxACX5448DRE,
       "jnxACX5448DPower": jnxACX5448DPower,
       "jnxACX5448DPowerDC": jnxACX5448DPowerDC,
       "jnxACX5448DPowerAC": jnxACX5448DPowerAC,
       "jnxACX5448DFan": jnxACX5448DFan,
       "jnxModuleACX6360OR": jnxModuleACX6360OR,
       "jnxACX6360ORHM": jnxACX6360ORHM,
       "jnxACX6360ORFPC": jnxACX6360ORFPC,
       "jnxACX6360ORFan": jnxACX6360ORFan,
       "jnxACX6360ORPower": jnxACX6360ORPower,
       "jnxModuleACX6360OX": jnxModuleACX6360OX,
       "jnxACX6360OXHM": jnxACX6360OXHM,
       "jnxACX6360OXFPC": jnxACX6360OXFPC,
       "jnxACX6360OXFan": jnxACX6360OXFan,
       "jnxACX6360OXPower": jnxACX6360OXPower,
       "jnxModuleACX710": jnxModuleACX710,
       "jnxACX710FPC": jnxACX710FPC,
       "jnxACX710RE": jnxACX710RE,
       "jnxACX710Power": jnxACX710Power,
       "jnxACX710PowerDC": jnxACX710PowerDC,
       "jnxACX710PowerAC": jnxACX710PowerAC,
       "jnxACX710Fan": jnxACX710Fan,
       "jnxModuleACX5800": jnxModuleACX5800,
       "jnxACX5800FPC": jnxACX5800FPC,
       "jnxACX5800FEB": jnxACX5800FEB,
       "jnxACX5800RE": jnxACX5800RE,
       "jnxACX5800Power": jnxACX5800Power,
       "jnxACX5800PowerDC": jnxACX5800PowerDC,
       "jnxACX5800PowerAC": jnxACX5800PowerAC,
       "jnxModuleSRX380": jnxModuleSRX380,
       "jnxSRX380FPC": jnxSRX380FPC,
       "jnxSRX380RE": jnxSRX380RE,
       "jnxSRX380Power": jnxSRX380Power,
       "jnxSRX380Fan": jnxSRX380Fan,
       "jnxModuleEX4400": jnxModuleEX4400,
       "jnxEX4400FPC": jnxEX4400FPC,
       "jnxEX4400Power": jnxEX4400Power,
       "jnxEX4400Fan": jnxEX4400Fan,
       "jnxModuleR6675": jnxModuleR6675,
       "jnxR6675FPC": jnxR6675FPC,
       "jnxR6675RE": jnxR6675RE,
       "jnxR6675Power": jnxR6675Power,
       "jnxR6675PowerDC": jnxR6675PowerDC,
       "jnxR6675PowerAC": jnxR6675PowerAC,
       "jnxR6675Fan": jnxR6675Fan,
       "jnxModuleMX304": jnxModuleMX304,
       "jnxMX304HM": jnxMX304HM,
       "jnxMX304FPC": jnxMX304FPC,
       "jnxMX304Fan": jnxMX304Fan,
       "jnxMX304Power": jnxMX304Power,
       "jnxMX304PMB": jnxMX304PMB,
       "jnxMX304SFB": jnxMX304SFB,
       "jnxMX304TIB": jnxMX304TIB,
       "jnxMX304CBD": jnxMX304CBD,
       "jnxModuleMX10004": jnxModuleMX10004,
       "jnxMX10004SFB": jnxMX10004SFB,
       "jnxMX10004HM": jnxMX10004HM,
       "jnxMX10004FPC": jnxMX10004FPC,
       "jnxMX10004Fan": jnxMX10004Fan,
       "jnxMX10004CBD": jnxMX10004CBD,
       "jnxMX10004Power": jnxMX10004Power,
       "jnxMX10004FPB": jnxMX10004FPB,
       "jnxMX10004FTC": jnxMX10004FTC,
       "jnxModuleEX4100": jnxModuleEX4100,
       "jnxEX4100FPC": jnxEX4100FPC,
       "jnxEX4100Power": jnxEX4100Power,
       "jnxEX4100Fan": jnxEX4100Fan,
       "jnxModuleEX4650": jnxModuleEX4650,
       "jnxEX4650FPC": jnxEX4650FPC,
       "jnxEX4650Power": jnxEX4650Power,
       "jnxEX4650Fan": jnxEX4650Fan,
       "jnxEX4650RE": jnxEX4650RE,
       "jnxModulePTX1000380c": jnxModulePTX1000380c,
       "jnxPTX1000380cRE": jnxPTX1000380cRE,
       "jnxPTX1000380cCB": jnxPTX1000380cCB,
       "jnxPTX1000380cFPC": jnxPTX1000380cFPC,
       "jnxPTX1000380cFan": jnxPTX1000380cFan,
       "jnxPTX1000380cFPM": jnxPTX1000380cFPM,
       "jnxPTX1000380cSIB": jnxPTX1000380cSIB,
       "jnxPTX1000380cPIC": jnxPTX1000380cPIC,
       "jnxPTX1000380cPDU": jnxPTX1000380cPDU,
       "jnxPTX1000380cPSM": jnxPTX1000380cPSM,
       "jnxModulePTX10003160c": jnxModulePTX10003160c,
       "jnxPTX10003160cRE": jnxPTX10003160cRE,
       "jnxPTX10003160cCB": jnxPTX10003160cCB,
       "jnxPTX10003160cFPC": jnxPTX10003160cFPC,
       "jnxPTX10003160cFan": jnxPTX10003160cFan,
       "jnxPTX10003160cFPM": jnxPTX10003160cFPM,
       "jnxPTX10003160cSIB": jnxPTX10003160cSIB,
       "jnxPTX10003160cPIC": jnxPTX10003160cPIC,
       "jnxPTX10003160cPDU": jnxPTX10003160cPDU,
       "jnxPTX10003160cPSM": jnxPTX10003160cPSM,
       "jnxModuleQFX1000380c": jnxModuleQFX1000380c,
       "jnxQFX1000380cRE": jnxQFX1000380cRE,
       "jnxQFX1000380cCB": jnxQFX1000380cCB,
       "jnxQFX1000380cFPC": jnxQFX1000380cFPC,
       "jnxQFX1000380cFan": jnxQFX1000380cFan,
       "jnxQFX1000380cFPM": jnxQFX1000380cFPM,
       "jnxQFX1000380cSIB": jnxQFX1000380cSIB,
       "jnxQFX1000380cPIC": jnxQFX1000380cPIC,
       "jnxQFX1000380cPDU": jnxQFX1000380cPDU,
       "jnxQFX1000380cPSM": jnxQFX1000380cPSM,
       "jnxModuleQFX10003160c": jnxModuleQFX10003160c,
       "jnxQFX10003160cRE": jnxQFX10003160cRE,
       "jnxQFX10003160cCB": jnxQFX10003160cCB,
       "jnxQFX10003160cFPC": jnxQFX10003160cFPC,
       "jnxQFX10003160cFan": jnxQFX10003160cFan,
       "jnxQFX10003160cFPM": jnxQFX10003160cFPM,
       "jnxQFX10003160cSIB": jnxQFX10003160cSIB,
       "jnxQFX10003160cPIC": jnxQFX10003160cPIC,
       "jnxQFX10003160cPDU": jnxQFX10003160cPDU,
       "jnxQFX10003160cPSM": jnxQFX10003160cPSM,
       "jnxModulePTX1000136mr": jnxModulePTX1000136mr,
       "jnxPTX1000136mrRE": jnxPTX1000136mrRE,
       "jnxPTX1000136mrCB": jnxPTX1000136mrCB,
       "jnxPTX1000136mrFPC": jnxPTX1000136mrFPC,
       "jnxPTX1000136mrFan": jnxPTX1000136mrFan,
       "jnxPTX1000136mrSIB": jnxPTX1000136mrSIB,
       "jnxPTX1000136mrPIC": jnxPTX1000136mrPIC,
       "jnxPTX1000136mrPSM": jnxPTX1000136mrPSM,
       "jnxModulePTX10004": jnxModulePTX10004,
       "jnxPTX10004FPC": jnxPTX10004FPC,
       "jnxPTX10004HM": jnxPTX10004HM,
       "jnxPTX10004Power": jnxPTX10004Power,
       "jnxPTX10004Fan": jnxPTX10004Fan,
       "jnxPTX10004FPB": jnxPTX10004FPB,
       "jnxPTX10004CBD": jnxPTX10004CBD,
       "jnxPTX10004SIB": jnxPTX10004SIB,
       "jnxPTX10004FPM": jnxPTX10004FPM,
       "jnxPTX10004FTC": jnxPTX10004FTC,
       "jnxPTX10004Backplane": jnxPTX10004Backplane,
       "jnxModuleACX753": jnxModuleACX753,
       "jnxACX753RE": jnxACX753RE,
       "jnxACX753PSM": jnxACX753PSM,
       "jnxACX753Fan": jnxACX753Fan,
       "jnxACX753CBD": jnxACX753CBD,
       "jnxACX753Backplane": jnxACX753Backplane,
       "jnxACX753FPC": jnxACX753FPC,
       "jnxACX753PIC": jnxACX753PIC,
       "jnxACX753FEB": jnxACX753FEB,
       "jnxModuleSRX1600": jnxModuleSRX1600,
       "jnxSRX1600FPC": jnxSRX1600FPC,
       "jnxSRX1600RE": jnxSRX1600RE,
       "jnxSRX1600Power": jnxSRX1600Power,
       "jnxSRX1600Fan": jnxSRX1600Fan,
       "jnxSRX1600CBD": jnxSRX1600CBD,
       "jnxModuleSRX2300": jnxModuleSRX2300,
       "jnxSRX2300FPC": jnxSRX2300FPC,
       "jnxSRX2300RE": jnxSRX2300RE,
       "jnxSRX2300Power": jnxSRX2300Power,
       "jnxSRX2300Fan": jnxSRX2300Fan,
       "jnxSRX2300CBD": jnxSRX2300CBD,
       "jnxModuleSRX4300": jnxModuleSRX4300,
       "jnxSRX4300FPC": jnxSRX4300FPC,
       "jnxSRX4300RE": jnxSRX4300RE,
       "jnxSRX4300Power": jnxSRX4300Power,
       "jnxSRX4300Fan": jnxSRX4300Fan,
       "jnxSRX4300CBD": jnxSRX4300CBD,
       "jnxModuleACX7332": jnxModuleACX7332,
       "jnxACX7332FPC": jnxACX7332FPC,
       "jnxACX7332RE": jnxACX7332RE,
       "jnxACX7332Power": jnxACX7332Power,
       "jnxACX7332Fan": jnxACX7332Fan,
       "jnxACX7332FEB": jnxACX7332FEB,
       "jnxACX7332CBD": jnxACX7332CBD,
       "jnxModuleACX7348": jnxModuleACX7348,
       "jnxACX7348FPC": jnxACX7348FPC,
       "jnxACX7348RE": jnxACX7348RE,
       "jnxACX7348Power": jnxACX7348Power,
       "jnxACX7348Fan": jnxACX7348Fan,
       "jnxACX7348FEB": jnxACX7348FEB,
       "jnxACX7348CBD": jnxACX7348CBD,
       "jnxModulePTX1000236qdd": jnxModulePTX1000236qdd,
       "jnxPTX1000236qddRE": jnxPTX1000236qddRE,
       "jnxPTX1000236qddCB": jnxPTX1000236qddCB,
       "jnxPTX1000236qddFPC": jnxPTX1000236qddFPC,
       "jnxPTX1000236qddFan": jnxPTX1000236qddFan,
       "jnxPTX1000236qddPIC": jnxPTX1000236qddPIC,
       "jnxPTX1000236qddPSM": jnxPTX1000236qddPSM,
       "jnxPTX1000236qddBackplane": jnxPTX1000236qddBackplane,
       "jnxPTX1000236qddFPM": jnxPTX1000236qddFPM,
       "jnxModuleSRX4700": jnxModuleSRX4700,
       "jnxSRX4700FPC": jnxSRX4700FPC,
       "jnxSRX4700RE": jnxSRX4700RE,
       "jnxSRX4700Power": jnxSRX4700Power,
       "jnxSRX4700Fan": jnxSRX4700Fan,
       "jnxSRX4700CBD": jnxSRX4700CBD,
       "jnxSubmodule": jnxSubmodule,
       "jnxSubmoduleM40": jnxSubmoduleM40,
       "jnxM40PIC0": jnxM40PIC0,
       "jnxM40SonetOc48": jnxM40SonetOc48,
       "jnxM40PIC": jnxM40PIC,
       "jnxM40QuadSonetOc3": jnxM40QuadSonetOc3,
       "jnxM40SonetOc12": jnxM40SonetOc12,
       "jnxM40GigEther": jnxM40GigEther,
       "jnxM40QuadT3": jnxM40QuadT3,
       "jnxM40QuadE3": jnxM40QuadE3,
       "jnxM40DualAtmOc3": jnxM40DualAtmOc3,
       "jnxM40AtmOc12": jnxM40AtmOc12,
       "jnxM40Tunnel": jnxM40Tunnel,
       "jnxM40ChOc12toDs3": jnxM40ChOc12toDs3,
       "jnxM40QuadEther": jnxM40QuadEther,
       "jnxM40QuadE1": jnxM40QuadE1,
       "jnxM40QuadT1": jnxM40QuadT1,
       "jnxM40SonetOc48Sr": jnxM40SonetOc48Sr,
       "jnxM40QuadChT3": jnxM40QuadChT3,
       "jnxM40SonetOc48Lr": jnxM40SonetOc48Lr,
       "jnxM40QuadAtmE3": jnxM40QuadAtmE3,
       "jnxM40QuadAtmT3": jnxM40QuadAtmT3,
       "jnxM40GigEtherBundle": jnxM40GigEtherBundle,
       "jnxM40Multilink128": jnxM40Multilink128,
       "jnxM40Multilink32": jnxM40Multilink32,
       "jnxM40Multilink4": jnxM40Multilink4,
       "jnxM40ChStm1": jnxM40ChStm1,
       "jnxM40DenseEther12": jnxM40DenseEther12,
       "jnxM40DecaChE1": jnxM40DecaChE1,
       "jnxM40ChDs3toDs0": jnxM40ChDs3toDs0,
       "jnxM40DualChDs3toDs0": jnxM40DualChDs3toDs0,
       "jnxM40DenseEther8": jnxM40DenseEther8,
       "jnxM40Crypto800": jnxM40Crypto800,
       "jnxM40LsMultilink128": jnxM40LsMultilink128,
       "jnxM40LsMultilink32": jnxM40LsMultilink32,
       "jnxM40LsMultilink4": jnxM40LsMultilink4,
       "jnxM40AtmIIOc12": jnxM40AtmIIOc12,
       "jnxM40DualAtmIIOc3": jnxM40DualAtmIIOc3,
       "jnxM40DualQChDS3": jnxM40DualQChDS3,
       "jnxM40QuadQChT3": jnxM40QuadQChT3,
       "jnxM40QChOc12": jnxM40QChOc12,
       "jnxM40QChStm1": jnxM40QChStm1,
       "jnxM40DualQChStm1": jnxM40DualQChStm1,
       "jnxM40DecaQChE1": jnxM40DecaQChE1,
       "jnxM40DualEIA530": jnxM40DualEIA530,
       "jnxM40DecaQChT1": jnxM40DecaQChT1,
       "jnxSubmoduleM20": jnxSubmoduleM20,
       "jnxM20PIC0": jnxM20PIC0,
       "jnxM20SonetOc48": jnxM20SonetOc48,
       "jnxM20PIC": jnxM20PIC,
       "jnxM20QuadSonetOc3": jnxM20QuadSonetOc3,
       "jnxM20SonetOc12": jnxM20SonetOc12,
       "jnxM20GigEther": jnxM20GigEther,
       "jnxM20QuadT3": jnxM20QuadT3,
       "jnxM20QuadE3": jnxM20QuadE3,
       "jnxM20DualAtmOc3": jnxM20DualAtmOc3,
       "jnxM20AtmOc12": jnxM20AtmOc12,
       "jnxM20Tunnel": jnxM20Tunnel,
       "jnxM20ChOc12toDs3": jnxM20ChOc12toDs3,
       "jnxM20QuadEther": jnxM20QuadEther,
       "jnxM20QuadE1": jnxM20QuadE1,
       "jnxM20QuadT1": jnxM20QuadT1,
       "jnxM20SonetOc48Sr": jnxM20SonetOc48Sr,
       "jnxM20QuadChT3": jnxM20QuadChT3,
       "jnxM20SonetOc48Lr": jnxM20SonetOc48Lr,
       "jnxM20QuadAtmE3": jnxM20QuadAtmE3,
       "jnxM20QuadAtmT3": jnxM20QuadAtmT3,
       "jnxM20GigEtherBundle": jnxM20GigEtherBundle,
       "jnxM20Multilink128": jnxM20Multilink128,
       "jnxM20Multilink32": jnxM20Multilink32,
       "jnxM20Multilink4": jnxM20Multilink4,
       "jnxM20ChStm1": jnxM20ChStm1,
       "jnxM20DenseEther12": jnxM20DenseEther12,
       "jnxM20DecaChE1": jnxM20DecaChE1,
       "jnxM20ChDs3toDs0": jnxM20ChDs3toDs0,
       "jnxM20DualChDs3toDs0": jnxM20DualChDs3toDs0,
       "jnxM20DenseEther8": jnxM20DenseEther8,
       "jnxM20Crypto800": jnxM20Crypto800,
       "jnxM20GgsnControl": jnxM20GgsnControl,
       "jnxM20GgsnData": jnxM20GgsnData,
       "jnxM20LsMultilink128": jnxM20LsMultilink128,
       "jnxM20LsMultilink32": jnxM20LsMultilink32,
       "jnxM20LsMultilink4": jnxM20LsMultilink4,
       "jnxM20AtmIIOc12": jnxM20AtmIIOc12,
       "jnxM20DualAtmIIOc3": jnxM20DualAtmIIOc3,
       "jnxM20DualQChDS3": jnxM20DualQChDS3,
       "jnxM20QuadQChT3": jnxM20QuadQChT3,
       "jnxM20QChOc12": jnxM20QChOc12,
       "jnxM20QChStm1": jnxM20QChStm1,
       "jnxM20DualQChStm1": jnxM20DualQChStm1,
       "jnxM20DecaQChE1": jnxM20DecaQChE1,
       "jnxM20DualEIA530": jnxM20DualEIA530,
       "jnxM20PassiveMonitor": jnxM20PassiveMonitor,
       "jnxM20DecaQChT1": jnxM20DecaQChT1,
       "jnxSubmoduleM160": jnxSubmoduleM160,
       "jnxM160SubSFM": jnxM160SubSFM,
       "jnxM160SPP": jnxM160SPP,
       "jnxM160SPR": jnxM160SPR,
       "jnxM160SubFPM": jnxM160SubFPM,
       "jnxM160FPMCMB": jnxM160FPMCMB,
       "jnxM160FPMDisplay": jnxM160FPMDisplay,
       "jnxM160PIC0": jnxM160PIC0,
       "jnxM160SonetOc192Sr": jnxM160SonetOc192Sr,
       "jnxM160SonetOc192Sr2": jnxM160SonetOc192Sr2,
       "jnxM160SonetOc192Lr1": jnxM160SonetOc192Lr1,
       "jnxM160PIC1": jnxM160PIC1,
       "jnxM160QuadSonetOc3": jnxM160QuadSonetOc3,
       "jnxM160SonetOc12": jnxM160SonetOc12,
       "jnxM160GigEther": jnxM160GigEther,
       "jnxM160QuadT3": jnxM160QuadT3,
       "jnxM160QuadE3": jnxM160QuadE3,
       "jnxM160DualAtmOc3": jnxM160DualAtmOc3,
       "jnxM160AtmOc12": jnxM160AtmOc12,
       "jnxM160ChOc12toDs3": jnxM160ChOc12toDs3,
       "jnxM160QuadEther": jnxM160QuadEther,
       "jnxM160QuadE1": jnxM160QuadE1,
       "jnxM160QuadT1": jnxM160QuadT1,
       "jnxM160QuadChT3": jnxM160QuadChT3,
       "jnxM160QuadAtmE3": jnxM160QuadAtmE3,
       "jnxM160QuadAtmT3": jnxM160QuadAtmT3,
       "jnxM160GigEtherBundle": jnxM160GigEtherBundle,
       "jnxM160ChStm1": jnxM160ChStm1,
       "jnxM160DecaChE1": jnxM160DecaChE1,
       "jnxM160ChDs3toDs0": jnxM160ChDs3toDs0,
       "jnxM160DualChDs3toDs0": jnxM160DualChDs3toDs0,
       "jnxM160DenseEther8": jnxM160DenseEther8,
       "jnxM160AtmIIOc12": jnxM160AtmIIOc12,
       "jnxM160DualAtmIIOc3": jnxM160DualAtmIIOc3,
       "jnxM160DualQChDS3": jnxM160DualQChDS3,
       "jnxM160QuadQChT3": jnxM160QuadQChT3,
       "jnxM160QChOc12": jnxM160QChOc12,
       "jnxM160QChStm1": jnxM160QChStm1,
       "jnxM160DualQChStm1": jnxM160DualQChStm1,
       "jnxM160DecaQChE1": jnxM160DecaQChE1,
       "jnxM160DualEIA530": jnxM160DualEIA530,
       "jnxM160PassiveMonitor": jnxM160PassiveMonitor,
       "jnxM160DecaQChT1": jnxM160DecaQChT1,
       "jnxM160PIC2": jnxM160PIC2,
       "jnxM160SonetOc48Sr": jnxM160SonetOc48Sr,
       "jnxM160Tunnel": jnxM160Tunnel,
       "jnxM160DualGigEther": jnxM160DualGigEther,
       "jnxM160QuadSonetOc12": jnxM160QuadSonetOc12,
       "jnxM160SonetOc48Lr": jnxM160SonetOc48Lr,
       "jnxM160DenseEther48": jnxM160DenseEther48,
       "jnxM160QuadGigEther": jnxM160QuadGigEther,
       "jnxM160Crypto800": jnxM160Crypto800,
       "jnxM160QuadOc3": jnxM160QuadOc3,
       "jnxM160DualQHGE": jnxM160DualQHGE,
       "jnxM160DualAtmIIOc12": jnxM160DualAtmIIOc12,
       "jnxSubmoduleM10": jnxSubmoduleM10,
       "jnxM10PIC": jnxM10PIC,
       "jnxM10QuadSonetOc3": jnxM10QuadSonetOc3,
       "jnxM10SonetOc12": jnxM10SonetOc12,
       "jnxM10GigEther": jnxM10GigEther,
       "jnxM10QuadT3": jnxM10QuadT3,
       "jnxM10QuadE3": jnxM10QuadE3,
       "jnxM10DualAtmOc3": jnxM10DualAtmOc3,
       "jnxM10AtmOc12": jnxM10AtmOc12,
       "jnxM10Tunnel": jnxM10Tunnel,
       "jnxM10ChOc12toDs3": jnxM10ChOc12toDs3,
       "jnxM10QuadEther": jnxM10QuadEther,
       "jnxM10QuadE1": jnxM10QuadE1,
       "jnxM10QuadT1": jnxM10QuadT1,
       "jnxM10SonetOc48Sr": jnxM10SonetOc48Sr,
       "jnxM10QuadChT3": jnxM10QuadChT3,
       "jnxM10SonetOc48Lr": jnxM10SonetOc48Lr,
       "jnxM10QuadAtmE3": jnxM10QuadAtmE3,
       "jnxM10QuadAtmT3": jnxM10QuadAtmT3,
       "jnxM10GigEtherBundle": jnxM10GigEtherBundle,
       "jnxM10Multilink128": jnxM10Multilink128,
       "jnxM10Multilink32": jnxM10Multilink32,
       "jnxM10Multilink4": jnxM10Multilink4,
       "jnxM10ChStm1": jnxM10ChStm1,
       "jnxM10DualChDs3": jnxM10DualChDs3,
       "jnxM10DualDs3": jnxM10DualDs3,
       "jnxM10DualSonetOc3": jnxM10DualSonetOc3,
       "jnxM10DualE3": jnxM10DualE3,
       "jnxM10DenseEther12": jnxM10DenseEther12,
       "jnxM10DecaChE1": jnxM10DecaChE1,
       "jnxM10ChDs3toDs0": jnxM10ChDs3toDs0,
       "jnxM10DualChDs3toDs0": jnxM10DualChDs3toDs0,
       "jnxM10DenseEther8": jnxM10DenseEther8,
       "jnxM10Crypto800": jnxM10Crypto800,
       "jnxM10LsMultilink128": jnxM10LsMultilink128,
       "jnxM10LsMultilink32": jnxM10LsMultilink32,
       "jnxM10LsMultilink4": jnxM10LsMultilink4,
       "jnxM10AtmIIOc12": jnxM10AtmIIOc12,
       "jnxM10DualAtmIIOc3": jnxM10DualAtmIIOc3,
       "jnxM10DualQChDs3": jnxM10DualQChDs3,
       "jnxM10QuadQChT3": jnxM10QuadQChT3,
       "jnxM10QChOc12": jnxM10QChOc12,
       "jnxM10QChStm1": jnxM10QChStm1,
       "jnxM10DualQChStm1": jnxM10DualQChStm1,
       "jnxM10DecaQChE1": jnxM10DecaQChE1,
       "jnxM10DualEIA530": jnxM10DualEIA530,
       "jnxM10DecaQChT1": jnxM10DecaQChT1,
       "jnxSubmoduleM5": jnxSubmoduleM5,
       "jnxM5PIC": jnxM5PIC,
       "jnxM5QuadSonetOc3": jnxM5QuadSonetOc3,
       "jnxM5SonetOc12": jnxM5SonetOc12,
       "jnxM5GigEther": jnxM5GigEther,
       "jnxM5QuadT3": jnxM5QuadT3,
       "jnxM5QuadE3": jnxM5QuadE3,
       "jnxM5DualAtmOc3": jnxM5DualAtmOc3,
       "jnxM5AtmOc12": jnxM5AtmOc12,
       "jnxM5Tunnel": jnxM5Tunnel,
       "jnxM5ChOc12toDs3": jnxM5ChOc12toDs3,
       "jnxM5QuadEther": jnxM5QuadEther,
       "jnxM5QuadE1": jnxM5QuadE1,
       "jnxM5QuadT1": jnxM5QuadT1,
       "jnxM5QuadChT3": jnxM5QuadChT3,
       "jnxM5QuadAtmE3": jnxM5QuadAtmE3,
       "jnxM5QuadAtmT3": jnxM5QuadAtmT3,
       "jnxM5GigEtherBundle": jnxM5GigEtherBundle,
       "jnxM5Multilink128": jnxM5Multilink128,
       "jnxM5Multilink32": jnxM5Multilink32,
       "jnxM5Multilink4": jnxM5Multilink4,
       "jnxM5ChStm1": jnxM5ChStm1,
       "jnxM5DualChDs3": jnxM5DualChDs3,
       "jnxM5DualDs3": jnxM5DualDs3,
       "jnxM5DualSonetOc3": jnxM5DualSonetOc3,
       "jnxM5DualE3": jnxM5DualE3,
       "jnxM5DenseEther12": jnxM5DenseEther12,
       "jnxM5DecaChE1": jnxM5DecaChE1,
       "jnxM5ChDs3toDs0": jnxM5ChDs3toDs0,
       "jnxM5DualChDs3toDs0": jnxM5DualChDs3toDs0,
       "jnxM5DenseEther8": jnxM5DenseEther8,
       "jnxM5Crypto800": jnxM5Crypto800,
       "jnxM5LsMultilink128": jnxM5LsMultilink128,
       "jnxM5LsMultilink32": jnxM5LsMultilink32,
       "jnxM5LsMultilink4": jnxM5LsMultilink4,
       "jnxM5AtmIIOc12": jnxM5AtmIIOc12,
       "jnxM5DualAtmIIOc3": jnxM5DualAtmIIOc3,
       "jnxM5DualQChDs3": jnxM5DualQChDs3,
       "jnxM5QuadQChT3": jnxM5QuadQChT3,
       "jnxM5QChOc12": jnxM5QChOc12,
       "jnxM5QChStm1": jnxM5QChStm1,
       "jnxM5DualQChStm1": jnxM5DualQChStm1,
       "jnxM5DecaQChE1": jnxM5DecaQChE1,
       "jnxM5DualEIA530": jnxM5DualEIA530,
       "jnxM5DecaQChT1": jnxM5DecaQChT1,
       "jnxSubmoduleT640": jnxSubmoduleT640,
       "jnxT640PIC0": jnxT640PIC0,
       "jnxT640PIC1": jnxT640PIC1,
       "jnxT640PIC2": jnxT640PIC2,
       "jnxT640DualGigEther": jnxT640DualGigEther,
       "jnxT640QuadGigEther": jnxT640QuadGigEther,
       "jnxT640QuadSonetOc12": jnxT640QuadSonetOc12,
       "jnxT640SonetOc48Sr": jnxT640SonetOc48Sr,
       "jnxT640SonetOc48Lr": jnxT640SonetOc48Lr,
       "jnxT640DualAtmIIOc12": jnxT640DualAtmIIOc12,
       "jnxT640QuadOc3": jnxT640QuadOc3,
       "jnxT640DualQHGE": jnxT640DualQHGE,
       "jnxT640PIC3": jnxT640PIC3,
       "jnxT640SonetOc192Sr2": jnxT640SonetOc192Sr2,
       "jnxT640Tunnel": jnxT640Tunnel,
       "jnxT640QuadSonetOc48": jnxT640QuadSonetOc48,
       "jnxT640SonetOc192Vsr": jnxT640SonetOc192Vsr,
       "jnxT640SonetOc192Lr": jnxT640SonetOc192Lr,
       "jnxT640TenGigEther": jnxT640TenGigEther,
       "jnxT640NX1GigEther": jnxT640NX1GigEther,
       "jnxSubmoduleT320": jnxSubmoduleT320,
       "jnxT320PIC0": jnxT320PIC0,
       "jnxT320PIC1": jnxT320PIC1,
       "jnxT320DualAtmIIOc3": jnxT320DualAtmIIOc3,
       "jnxT320QuadSonetOc3": jnxT320QuadSonetOc3,
       "jnxT320DualAtmOc3": jnxT320DualAtmOc3,
       "jnxT320AtmOc12": jnxT320AtmOc12,
       "jnxT320QuadEther": jnxT320QuadEther,
       "jnxT320SonetOc12": jnxT320SonetOc12,
       "jnxT320AtmIIOc12": jnxT320AtmIIOc12,
       "jnxT320PIC2": jnxT320PIC2,
       "jnxT320DualGigEther": jnxT320DualGigEther,
       "jnxT320QuadGigEther": jnxT320QuadGigEther,
       "jnxT320QuadSonetOc12": jnxT320QuadSonetOc12,
       "jnxT320SonetOc48Sr": jnxT320SonetOc48Sr,
       "jnxT320SonetOc48Lr": jnxT320SonetOc48Lr,
       "jnxT320DualAtmIIOc12": jnxT320DualAtmIIOc12,
       "jnxT320QuadOc3": jnxT320QuadOc3,
       "jnxT320DualQHGE": jnxT320DualQHGE,
       "jnxT320PIC3": jnxT320PIC3,
       "jnxT320SonetOc192Sr2": jnxT320SonetOc192Sr2,
       "jnxT320Tunnel": jnxT320Tunnel,
       "jnxT320QuadSonetOc48": jnxT320QuadSonetOc48,
       "jnxT320SonetOc192Vsr": jnxT320SonetOc192Vsr,
       "jnxT320SonetOc192Lr": jnxT320SonetOc192Lr,
       "jnxT320TenGigEther": jnxT320TenGigEther,
       "jnxT320NX1GigEther": jnxT320NX1GigEther,
       "jnxSubmoduleM40e": jnxSubmoduleM40e,
       "jnxM40eSubSFM": jnxM40eSubSFM,
       "jnxM40eSPP": jnxM40eSPP,
       "jnxM40eSPR": jnxM40eSPR,
       "jnxM40eSubFPM": jnxM40eSubFPM,
       "jnxM40eFPMCMB": jnxM40eFPMCMB,
       "jnxM40eFPMDisplay": jnxM40eFPMDisplay,
       "jnxM40ePIC0": jnxM40ePIC0,
       "jnxM40ePIC1": jnxM40ePIC1,
       "jnxM40eQuadSonetOc3": jnxM40eQuadSonetOc3,
       "jnxM40eSonetOc12": jnxM40eSonetOc12,
       "jnxM40eGigEther": jnxM40eGigEther,
       "jnxM40eQuadT3": jnxM40eQuadT3,
       "jnxM40eQuadE3": jnxM40eQuadE3,
       "jnxM40eDualAtmOc3": jnxM40eDualAtmOc3,
       "jnxM40eAtmOc12": jnxM40eAtmOc12,
       "jnxM40eChOc12toDs3": jnxM40eChOc12toDs3,
       "jnxM40eQuadEther": jnxM40eQuadEther,
       "jnxM40eQuadE1": jnxM40eQuadE1,
       "jnxM40eQuadT1": jnxM40eQuadT1,
       "jnxM40eQuadChT3": jnxM40eQuadChT3,
       "jnxM40eQuadAtmE3": jnxM40eQuadAtmE3,
       "jnxM40eQuadAtmT3": jnxM40eQuadAtmT3,
       "jnxM40eGigEtherBundle": jnxM40eGigEtherBundle,
       "jnxM40eChStm1": jnxM40eChStm1,
       "jnxM40eDecaChE1": jnxM40eDecaChE1,
       "jnxM40eChDs3toDs0": jnxM40eChDs3toDs0,
       "jnxM40eDualChDs3toDs0": jnxM40eDualChDs3toDs0,
       "jnxM40eDenseEther8": jnxM40eDenseEther8,
       "jnxM40eAtmIIOc12": jnxM40eAtmIIOc12,
       "jnxM40eDualAtmIIOc3": jnxM40eDualAtmIIOc3,
       "jnxM40eDualQChDS3": jnxM40eDualQChDS3,
       "jnxM40eQuadQChT3": jnxM40eQuadQChT3,
       "jnxM40eLsMultilink128": jnxM40eLsMultilink128,
       "jnxM40eLsMultilink32": jnxM40eLsMultilink32,
       "jnxM40eLsMultilink4": jnxM40eLsMultilink4,
       "jnxM40eQChOc12": jnxM40eQChOc12,
       "jnxM40eQChStm1": jnxM40eQChStm1,
       "jnxM40eDualQChStm1": jnxM40eDualQChStm1,
       "jnxM40eDecaQChE1": jnxM40eDecaQChE1,
       "jnxM40eDualEIA530": jnxM40eDualEIA530,
       "jnxM40ePassiveMonitor": jnxM40ePassiveMonitor,
       "jnxM40eMultilink128": jnxM40eMultilink128,
       "jnxM40eMultilink32": jnxM40eMultilink32,
       "jnxM40eMultilink4": jnxM40eMultilink4,
       "jnxM40eDenseEther12": jnxM40eDenseEther12,
       "jnxM40eDecaQChT1": jnxM40eDecaQChT1,
       "jnxM40ePIC2": jnxM40ePIC2,
       "jnxM40eSonetOc48Sr": jnxM40eSonetOc48Sr,
       "jnxM40eTunnel": jnxM40eTunnel,
       "jnxM40eDualGigEther": jnxM40eDualGigEther,
       "jnxM40eQuadSonetOc12": jnxM40eQuadSonetOc12,
       "jnxM40eSonetOc48Lr": jnxM40eSonetOc48Lr,
       "jnxM40eDenseEther48": jnxM40eDenseEther48,
       "jnxM40eQuadGigEther": jnxM40eQuadGigEther,
       "jnxM40eCrypto800": jnxM40eCrypto800,
       "jnxM40eQuadOc3": jnxM40eQuadOc3,
       "jnxM40eDualQHGE": jnxM40eDualQHGE,
       "jnxM40eDualAtmIIOc12": jnxM40eDualAtmIIOc12,
       "jnxSubmoduleM7i": jnxSubmoduleM7i,
       "jnxM7iPIC": jnxM7iPIC,
       "jnxSubmoduleGeneric": jnxSubmoduleGeneric,
       "jnxPic": jnxPic,
       "jnxPicType3TenGigEther": jnxPicType3TenGigEther,
       "jnxPicChDs3toDs0": jnxPicChDs3toDs0,
       "jnxPicDualChDs3toDs0": jnxPicDualChDs3toDs0,
       "jnxPicAtmIIOc12": jnxPicAtmIIOc12,
       "jnxPicAtmOc12": jnxPicAtmOc12,
       "jnxPicM7iTunnel": jnxPicM7iTunnel,
       "jnxPicChOc12toDs3": jnxPicChOc12toDs3,
       "jnxPicCrypto800": jnxPicCrypto800,
       "jnxPicType2DualAtmIIOc12": jnxPicType2DualAtmIIOc12,
       "jnxPicDualAtmIIOc3": jnxPicDualAtmIIOc3,
       "jnxPicDualAtmOc3": jnxPicDualAtmOc3,
       "jnxPicDualChDs3": jnxPicDualChDs3,
       "jnxPicDualE3": jnxPicDualE3,
       "jnxPicDualEia530": jnxPicDualEia530,
       "jnxPicDualQChStm1": jnxPicDualQChStm1,
       "jnxPicDualQChDs3": jnxPicDualQChDs3,
       "jnxPicType2DualQHGE": jnxPicType2DualQHGE,
       "jnxPicDualSonetOc3": jnxPicDualSonetOc3,
       "jnxPicDualDs3": jnxPicDualDs3,
       "jnxPicType1Tunnel": jnxPicType1Tunnel,
       "jnxPicGgsnControl": jnxPicGgsnControl,
       "jnxPicGgsnData": jnxPicGgsnData,
       "jnxPicType3TenPortGigEther": jnxPicType3TenPortGigEther,
       "jnxPicType3SonetOc192Lr": jnxPicType3SonetOc192Lr,
       "jnxPicType3SonetOc192Sr2": jnxPicType3SonetOc192Sr2,
       "jnxPicType3SonetOc192Vsr": jnxPicType3SonetOc192Vsr,
       "jnxPicType3QuadSonetOc48": jnxPicType3QuadSonetOc48,
       "jnxPicType3Tunnel": jnxPicType3Tunnel,
       "jnxPicGigEther": jnxPicGigEther,
       "jnxPicLsMultilink128": jnxPicLsMultilink128,
       "jnxPicLsMultilink32": jnxPicLsMultilink32,
       "jnxPicLsMultilink4": jnxPicLsMultilink4,
       "jnxPicType2DenseEther48": jnxPicType2DenseEther48,
       "jnxPicType2DualGigEther": jnxPicType2DualGigEther,
       "jnxPicType2SonetOc48Lr": jnxPicType2SonetOc48Lr,
       "jnxPicType2QuadGigEther": jnxPicType2QuadGigEther,
       "jnxPicType2QuadSonetOc12": jnxPicType2QuadSonetOc12,
       "jnxPicType2QuadSonetOc3": jnxPicType2QuadSonetOc3,
       "jnxPicType1SonetOc192Sr2": jnxPicType1SonetOc192Sr2,
       "jnxPicType1SonetOc192Lr1": jnxPicType1SonetOc192Lr1,
       "jnxPicType1SonetOc192Sr": jnxPicType1SonetOc192Sr,
       "jnxPicType1SonetOc192Vsr": jnxPicType1SonetOc192Vsr,
       "jnxPicType2SonetOc48Sr": jnxPicType2SonetOc48Sr,
       "jnxPicType2Tunnel": jnxPicType2Tunnel,
       "jnxPicDecaChE1": jnxPicDecaChE1,
       "jnxPicDenseEther12": jnxPicDenseEther12,
       "jnxPicDenseEtherFX8": jnxPicDenseEtherFX8,
       "jnxPicGigEtherBundle": jnxPicGigEtherBundle,
       "jnxPicSonetOc48Lr": jnxPicSonetOc48Lr,
       "jnxPicSonetOc48Sr": jnxPicSonetOc48Sr,
       "jnxPicMultilink128": jnxPicMultilink128,
       "jnxPicMultilink32": jnxPicMultilink32,
       "jnxPicMultilink4": jnxPicMultilink4,
       "jnxPicPassiveMonitor": jnxPicPassiveMonitor,
       "jnxPicDecaQChE1": jnxPicDecaQChE1,
       "jnxPicQChOc12": jnxPicQChOc12,
       "jnxPicQuadAtmE3": jnxPicQuadAtmE3,
       "jnxPicQuadAtmT3": jnxPicQuadAtmT3,
       "jnxPicQuadChT3": jnxPicQuadChT3,
       "jnxPicQuadE1": jnxPicQuadE1,
       "jnxPicQuadE3": jnxPicQuadE3,
       "jnxPicQuadEther": jnxPicQuadEther,
       "jnxPicQuadQChT3": jnxPicQuadQChT3,
       "jnxPicQuadSonetOc3": jnxPicQuadSonetOc3,
       "jnxPicQuadT1": jnxPicQuadT1,
       "jnxPicQuadT3": jnxPicQuadT3,
       "jnxPicChStm1": jnxPicChStm1,
       "jnxPicQChStm1": jnxPicQChStm1,
       "jnxPicSingleQHGE": jnxPicSingleQHGE,
       "jnxPicSonetOc12": jnxPicSonetOc12,
       "jnxPicSonetOc48": jnxPicSonetOc48,
       "jnxPicTunnel": jnxPicTunnel,
       "jnxPicGeneralServices": jnxPicGeneralServices,
       "jnxPicPassiveMonitorAsp": jnxPicPassiveMonitorAsp,
       "jnxPicType1TenGigEther": jnxPicType1TenGigEther,
       "jnxPicDualATMIIE3": jnxPicDualATMIIE3,
       "jnxPicQuadATMIIE3": jnxPicQuadATMIIE3,
       "jnxPicQuadATMIIT3": jnxPicQuadATMIIT3,
       "jnxPicQuadQE3": jnxPicQuadQE3,
       "jnxPicType1Oc48SFP": jnxPicType1Oc48SFP,
       "jnxPicType2Oc48SFP": jnxPicType2Oc48SFP,
       "jnxPicGgsnInspection": jnxPicGgsnInspection,
       "jnxPicType3QuadSonetOc48SFP": jnxPicType3QuadSonetOc48SFP,
       "jnxPicType3TenGigEtherXenpak": jnxPicType3TenGigEtherXenpak,
       "jnxPicIntServices": jnxPicIntServices,
       "jnxPicDualFicFE": jnxPicDualFicFE,
       "jnxPicFicGE": jnxPicFicGE,
       "jnxPicSingleSGE": jnxPicSingleSGE,
       "jnxPicDualSGE": jnxPicDualSGE,
       "jnxPicQuadSGE": jnxPicQuadSGE,
       "jnxPicType3SonetOc192Sr1": jnxPicType3SonetOc192Sr1,
       "jnxPicAdaptiveServicesII": jnxPicAdaptiveServicesII,
       "jnxPicJseriesEthT1Combo": jnxPicJseriesEthT1Combo,
       "jnxPicJseriesEthE1Combo": jnxPicJseriesEthE1Combo,
       "jnxPicJseriesEthSerCombo": jnxPicJseriesEthSerCombo,
       "jnxPicJseriesDualEth": jnxPicJseriesDualEth,
       "jnxPicJseriesDualT1": jnxPicJseriesDualT1,
       "jnxPicJseriesDualE1": jnxPicJseriesDualE1,
       "jnxPicJseriesDualSerial": jnxPicJseriesDualSerial,
       "jnxPicJseriesT3": jnxPicJseriesT3,
       "jnxPicType2AtmIIOc48": jnxPicType2AtmIIOc48,
       "jnxPicSonetOc768Sr": jnxPicSonetOc768Sr,
       "jnxPicQuadSonetOc192XFP": jnxPicQuadSonetOc192XFP,
       "jnxPicType4Tunnel": jnxPicType4Tunnel,
       "jnxPicQChoc3": jnxPicQChoc3,
       "jnxPicType3DWDMTenGigEther": jnxPicType3DWDMTenGigEther,
       "jnxPicType4QuadOC192": jnxPicType4QuadOC192,
       "jnxPicType1Load": jnxPicType1Load,
       "jnxPicType2Load": jnxPicType2Load,
       "jnxPicType3Load": jnxPicType3Load,
       "jnxPicType4Load": jnxPicType4Load,
       "jnxPicGgsnControlV1": jnxPicGgsnControlV1,
       "jnxPicGgsnDataV1": jnxPicGgsnDataV1,
       "jnxPicMonitoring3": jnxPicMonitoring3,
       "jnxPicGgsnPhoenix": jnxPicGgsnPhoenix,
       "jnxPicAdaptiveServicesFips": jnxPicAdaptiveServicesFips,
       "jnxPicMonitoring3V1": jnxPicMonitoring3V1,
       "jnxPicGgsnPhoenixV1": jnxPicGgsnPhoenixV1,
       "jnxPicJseriesE3": jnxPicJseriesE3,
       "jnxPicLinkServicesII": jnxPicLinkServicesII,
       "jnxPicDecaQChT1": jnxPicDecaQChT1,
       "jnxPicType3IQ21X10GE": jnxPicType3IQ21X10GE,
       "jnxPicType2IQ28X1GE": jnxPicType2IQ28X1GE,
       "jnxPicType1IQ24X1GE": jnxPicType1IQ24X1GE,
       "jnxPic10GEUplink": jnxPic10GEUplink,
       "jnxPicType2IQ21X10GE": jnxPicType2IQ21X10GE,
       "jnxPicType1MultiServices": jnxPicType1MultiServices,
       "jnxPicType2MultiServices": jnxPicType2MultiServices,
       "jnxPicType3MultiServices": jnxPicType3MultiServices,
       "jnxPicSonetOc192Uplink": jnxPicSonetOc192Uplink,
       "jnxPicXDpc10X1GE": jnxPicXDpc10X1GE,
       "jnxPicXQDpc10X1GE": jnxPicXQDpc10X1GE,
       "jnxPicXDpc1X10GE": jnxPicXDpc1X10GE,
       "jnxPicXQDpc1X10GE": jnxPicXQDpc1X10GE,
       "jnxPicType3SonetOc192Xfp": jnxPicType3SonetOc192Xfp,
       "jnxPicType3IQ28X1GE": jnxPicType3IQ28X1GE,
       "jnxPicType2Sonetoc48Sr2": jnxPicType2Sonetoc48Sr2,
       "jnxPicType2Sonetoc12Sr2": jnxPicType2Sonetoc12Sr2,
       "jnxPicType2Sonetoc3Sr2": jnxPicType2Sonetoc3Sr2,
       "jnxPicStoli4X10GE": jnxPicStoli4X10GE,
       "jnxPicType1Sonet4Xoc3": jnxPicType1Sonet4Xoc3,
       "jnxPicType1Sonet2Xoc3": jnxPicType1Sonet2Xoc3,
       "jnxPicType1Sonet1Xoc12": jnxPicType1Sonet1Xoc12,
       "jnxPicGgsnStargateType2": jnxPicGgsnStargateType2,
       "jnxPicUQDpc10X1GE": jnxPicUQDpc10X1GE,
       "jnxPicUQDpc1X10GE": jnxPicUQDpc1X10GE,
       "jnxPicNPC": jnxPicNPC,
       "jnxPicIOC16xGETP": jnxPicIOC16xGETP,
       "jnxPicIOC16xGESFP": jnxPicIOC16xGESFP,
       "jnxPicIOC2x10GEXFP": jnxPicIOC2x10GEXFP,
       "jnxPicIOC8xGETP4xGESFP": jnxPicIOC8xGETP4xGESFP,
       "jnxPicSPCRMIx1": jnxPicSPCRMIx1,
       "jnxPicType3EnhancedLoad": jnxPicType3EnhancedLoad,
       "jnxPicCE4xCHOC3SFP": jnxPicCE4xCHOC3SFP,
       "jnxPicCE12xT1E1": jnxPicCE12xT1E1,
       "jnxPicXDpc10X1GERJ45": jnxPicXDpc10X1GERJ45,
       "jnxPicQ2ChOc12": jnxPicQ2ChOc12,
       "jnxPicQ2Oc12": jnxPicQ2Oc12,
       "jnxPicQ2ChOc3": jnxPicQ2ChOc3,
       "jnxPicQ2Oc3": jnxPicQ2Oc3,
       "jnxPicQ2ChDs3": jnxPicQ2ChDs3,
       "jnxPicQ2Ds3": jnxPicQ2Ds3,
       "jnxPicQ21xChOc48": jnxPicQ21xChOc48,
       "jnxPicQ24xChOc12": jnxPicQ24xChOc12,
       "jnxPicQ210xChE1T1": jnxPicQ210xChE1T1,
       "jnxPicOlivet": jnxPicOlivet,
       "jnxPicType1IQ2E4X1GE": jnxPicType1IQ2E4X1GE,
       "jnxPicType2IQ2E8X1GE": jnxPicType2IQ2E8X1GE,
       "jnxPicType3IQ2E8X1GE": jnxPicType3IQ2E8X1GE,
       "jnxPicType3IQ2E1X10GE": jnxPicType3IQ2E1X10GE,
       "jnxPicASPCTYPE1": jnxPicASPCTYPE1,
       "jnxPicASPCTYPE2": jnxPicASPCTYPE2,
       "jnxPicASPCTYPE3": jnxPicASPCTYPE3,
       "jnxPicFIOC16X1GETP": jnxPicFIOC16X1GETP,
       "jnxPicFIOC16X1GESFP": jnxPicFIOC16X1GESFP,
       "jnxPicFIOC4X10GEXFP": jnxPicFIOC4X10GEXFP,
       "jnxPicMIC20XGESFP": jnxPicMIC20XGESFP,
       "jnxPicMIC2X10GEXFP": jnxPicMIC2X10GEXFP,
       "jnxPicMIC40XGERJ45": jnxPicMIC40XGERJ45,
       "jnxPicMIC4X10GEXFP": jnxPicMIC4X10GEXFP,
       "jnxPicMICLoad": jnxPicMICLoad,
       "jnxPicMICH10XGESFP": jnxPicMICH10XGESFP,
       "jnxPicMICH1X10GEXFP": jnxPicMICH1X10GEXFP,
       "jnxPicMICH10XGERJ45": jnxPicMICH10XGERJ45,
       "jnxPicMICH2X10GEXFP": jnxPicMICH2X10GEXFP,
       "jnxPicMICHLoad": jnxPicMICHLoad,
       "jnxPicOtn1X10GE": jnxPicOtn1X10GE,
       "jnxPicStoli10X10GE": jnxPicStoli10X10GE,
       "jnxPicStoli100GE": jnxPicStoli100GE,
       "jnxPicType3Q24xChOc12": jnxPicType3Q24xChOc12,
       "jnxPicStoli100GESlot1": jnxPicStoli100GESlot1,
       "jnxPicUplinkSFPplus1G4": jnxPicUplinkSFPplus1G4,
       "jnxPicUplinkSFPplus10G2": jnxPicUplinkSFPplus10G2,
       "jnxPicUplinkXFP2port": jnxPicUplinkXFP2port,
       "jnxPicUplinkSFP4port": jnxPicUplinkSFP4port,
       "jnxPicUplinkSFPplus4port": jnxPicUplinkSFPplus4port,
       "jnxPicXDpcCombo10X1GE": jnxPicXDpcCombo10X1GE,
       "jnxPicXQDpcCombo10X1GE": jnxPicXQDpcCombo10X1GE,
       "jnxPicTAZ4X10GEXFP": jnxPicTAZ4X10GEXFP,
       "jnxPicTAZ48XGERJ45": jnxPicTAZ48XGERJ45,
       "jnxPicStoli1X40GECFP": jnxPicStoli1X40GECFP,
       "jnxPicOtnOc192": jnxPicOtnOc192,
       "jnxPICStoli100GESNAP12": jnxPICStoli100GESNAP12,
       "jnxPicEX820048S": jnxPicEX820048S,
       "jnxPicEX820048T": jnxPicEX820048T,
       "jnxPicEX82008XS": jnxPicEX82008XS,
       "jnxPicMIC4X10GESFPPLUS": jnxPicMIC4X10GESFPPLUS,
       "jnxPicEX4500UplinkSFPPlus4Port": jnxPicEX4500UplinkSFPPlus4Port,
       "jnxPicSoho48X10GE": jnxPicSoho48X10GE,
       "jnxPicM2LoopBack": jnxPicM2LoopBack,
       "jnxPicCtpGluon4xT1E1": jnxPicCtpGluon4xT1E1,
       "jnxPicCtpGluon4xSerial": jnxPicCtpGluon4xSerial,
       "jnxPicSng24x10GE": jnxPicSng24x10GE,
       "jnxPicSng2x100GE": jnxPicSng2x100GE,
       "jnxPicSngLoad": jnxPicSngLoad,
       "jnxPicSysio6XGERJ456XGESFP": jnxPicSysio6XGERJ456XGESFP,
       "jnxPicSysio6XGERJ453XGESFP3X10GESFPPlus": jnxPicSysio6XGERJ453XGESFP3X10GESFPPlus,
       "jnxPicDualWideSPCNPC": jnxPicDualWideSPCNPC,
       "jnxPicDualWideNPCSPC": jnxPicDualWideNPCSPC,
       "jnxPicTAZ12XGERJ45": jnxPicTAZ12XGERJ45,
       "jnxPicType1MultiServicesFIPS": jnxPicType1MultiServicesFIPS,
       "jnxPicType2MultiServicesFIPS": jnxPicType2MultiServicesFIPS,
       "jnxPicType3MultiServicesFIPS": jnxPicType3MultiServicesFIPS,
       "jnxPicEX4500UplinkXFP4Port": jnxPicEX4500UplinkXFP4Port,
       "jnxPicEX4500M2Optical": jnxPicEX4500M2Optical,
       "jnxPicEX4500M2Legacy": jnxPicEX4500M2Legacy,
       "jnxPicEX820036XS": jnxPicEX820036XS,
       "jnxPicEX820040XS": jnxPicEX820040XS,
       "jnxPicEX820048PL": jnxPicEX820048PL,
       "jnxPicEX82002XS40P": jnxPicEX82002XS40P,
       "jnxPicType1ASPCXLP": jnxPicType1ASPCXLP,
       "jnxPicType2ASPCXLP": jnxPicType2ASPCXLP,
       "jnxPicType3ASPCXLP": jnxPicType3ASPCXLP,
       "jnxPicSPCXLPx1": jnxPicSPCXLPx1,
       "jnxPicStoli40GE": jnxPicStoli40GE,
       "jnxPicHyp1X100GECFP": jnxPicHyp1X100GECFP,
       "jnxPicHyp1X40GECFP": jnxPicHyp1X40GECFP,
       "jnxPicHypX100GECXP": jnxPicHypX100GECXP,
       "jnxPicHyp10X10GESFPP": jnxPicHyp10X10GESFPP,
       "jnxPic12x10GE": jnxPic12x10GE,
       "jnxPic1x100GE": jnxPic1x100GE,
       "jnxPicHyp2X40GEQSFP": jnxPicHyp2X40GEQSFP,
       "jnxPicHercules24X10GE": jnxPicHercules24X10GE,
       "jnxPicCTPGluonSerialMS": jnxPicCTPGluonSerialMS,
       "jnxPicAgent00SLC1X10GE": jnxPicAgent00SLC1X10GE,
       "jnxPicAgent00SLC4X1GE": jnxPicAgent00SLC4X1GE,
       "jnxPicQFXSFE16x40GEQSFP": jnxPicQFXSFE16x40GEQSFP,
       "jnxPicQFXSFI16x40GE": jnxPicQFXSFI16x40GE,
       "jnxPicQFXSRI16x40GE": jnxPicQFXSRI16x40GE,
       "jnxPicQFX48x10GESFPPlus": jnxPicQFX48x10GESFPPlus,
       "jnxPicQFX4x40GEQSFP": jnxPicQFX4x40GEQSFP,
       "jnxPicQFX2x80GEQCXP": jnxPicQFX2x80GEQCXP,
       "jnxPicType3IQECC4XOC48": jnxPicType3IQECC4XOC48,
       "jnxPicSng2x40GE": jnxPicSng2x40GE,
       "jnxPicIBM0719J45EUplinkSFPPlus4Port": jnxPicIBM0719J45EUplinkSFPPlus4Port,
       "jnxPicIBM0719J45EUplinkXFP4Port": jnxPicIBM0719J45EUplinkXFP4Port,
       "jnxPicIBM0719J45EM2Optical": jnxPicIBM0719J45EM2Optical,
       "jnxPicIBM0719J45EM2Legacy": jnxPicIBM0719J45EM2Legacy,
       "jnxPicIBMJ08FSFE16x40GEQSFP": jnxPicIBMJ08FSFE16x40GEQSFP,
       "jnxPicIBMJ08FSFI16xFabric": jnxPicIBMJ08FSFI16xFabric,
       "jnxPicIBMJ08FSRI16xFabric": jnxPicIBMJ08FSRI16xFabric,
       "jnxPicIBMJ52F48x10GESFPPlus": jnxPicIBMJ52F48x10GESFPPlus,
       "jnxPicIBMJ52F4x40GEQSFP": jnxPicIBMJ52F4x40GEQSFP,
       "jnxPicDellJFX350048x10GESFPPlus": jnxPicDellJFX350048x10GESFPPlus,
       "jnxPicEX820048TES": jnxPicEX820048TES,
       "jnxPicEX820048SES": jnxPicEX820048SES,
       "jnxPicEX82008XSES": jnxPicEX82008XSES,
       "jnxPicEX820040XSES": jnxPicEX820040XSES,
       "jnxPicEX820048TES4X": jnxPicEX820048TES4X,
       "jnxPicEX820048SES4X": jnxPicEX820048SES4X,
       "jnxPicEX82008XSES4X": jnxPicEX82008XSES4X,
       "jnxPicEX820040XSES4X": jnxPicEX820040XSES4X,
       "jnxPicEX620048T": jnxPicEX620048T,
       "jnxPicEX620048P": jnxPicEX620048P,
       "jnxPicEX62004XS": jnxPicEX62004XS,
       "jnxPicDellJFX35004x40GEQSFP": jnxPicDellJFX35004x40GEQSFP,
       "jnxPicEX820048TL": jnxPicEX820048TL,
       "jnxPicEX82002XS40T": jnxPicEX82002XS40T,
       "jnxPicType2MSPrism": jnxPicType2MSPrism,
       "jnxPicMicMSPrism": jnxPicMicMSPrism,
       "jnxPicQFX16x10GESFPPlus": jnxPicQFX16x10GESFPPlus,
       "jnxPicIBMJ52F16x10GESFPPlus": jnxPicIBMJ52F16x10GESFPPlus,
       "jnxPicDellJFX350016x10GESFPPlus": jnxPicDellJFX350016x10GESFPPlus,
       "jnxPicQFX10xPTunnel": jnxPicQFX10xPTunnel,
       "jnxPicIBMJ52F10xPTunnel": jnxPicIBMJ52F10xPTunnel,
       "jnxPic16XT1E1CEMIC": jnxPic16XT1E1CEMIC,
       "jnxPic8XT1E1CEMIC": jnxPic8XT1E1CEMIC,
       "jnxPic8xGERJ452xPOEMIC": jnxPic8xGERJ452xPOEMIC,
       "jnxPic2xGESFPMIC": jnxPic2xGESFPMIC,
       "jnxPic2x10GESFPPLUSMIC": jnxPic2x10GESFPPLUSMIC,
       "jnxPic4xGESFPRJ45COMBOMIC": jnxPic4xGESFPRJ45COMBOMIC,
       "jnxPicUplinkDualMedia2port": jnxPicUplinkDualMedia2port,
       "jnxPicEX3300UplinkSFPPlus4Port": jnxPicEX3300UplinkSFPPlus4Port,
       "jnxPicEX4500UplinkSFP4Port": jnxPicEX4500UplinkSFP4Port,
       "jnxPicEX4550UplinkEm8XFP": jnxPicEX4550UplinkEm8XFP,
       "jnxPicEX4550UplinkEm8XT": jnxPicEX4550UplinkEm8XT,
       "jnxPicEX4550UplinkEm2QSFP": jnxPicEX4550UplinkEm2QSFP,
       "jnxPicEX4550VC128G": jnxPicEX4550VC128G,
       "jnxPicQFX16x80GCXP": jnxPicQFX16x80GCXP,
       "jnxPicQFX63x10GESFPPlus": jnxPicQFX63x10GESFPPlus,
       "jnxPicQFX16x40GEQSFP": jnxPicQFX16x40GEQSFP,
       "jnxPic6xGESFPRJ45": jnxPic6xGESFPRJ45,
       "jnxPicMXPISA16xT1E1RJ48": jnxPicMXPISA16xT1E1RJ48,
       "jnxPic6x40GEQSFPP": jnxPic6x40GEQSFPP,
       "jnxPicACX1xOC124xOC3SFP": jnxPicACX1xOC124xOC3SFP,
       "jnxPicACXPISA16xT1E1RJ48": jnxPicACXPISA16xT1E1RJ48,
       "jnxPic8x10GESFPPMIC": jnxPic8x10GESFPPMIC,
       "jnxPic1x100GECFPMIC": jnxPic1x100GECFPMIC,
       "jnxPic4x10GESFPPMIC": jnxPic4x10GESFPPMIC,
       "jnxPicPTX2x100GOTNPIC": jnxPicPTX2x100GOTNPIC,
       "jnxPicMXXLPDPCPIC": jnxPicMXXLPDPCPIC,
       "jnxPicMXXLP8GMIC": jnxPicMXXLP8GMIC,
       "jnxPicMXXLP16GMIC": jnxPicMXXLP16GMIC,
       "jnxPicMXXLP8GFIPSMIC": jnxPicMXXLP8GFIPSMIC,
       "jnxPicMXXLP16GFIPSMIC": jnxPicMXXLP16GFIPSMIC,
       "jnxPicEX4300QSFP4Port": jnxPicEX4300QSFP4Port,
       "jnxPicEX4300UplinkSFPPlus4Port": jnxPicEX4300UplinkSFPPlus4Port,
       "jnxPicNPIOC2x10GESFPPLUSPIC": jnxPicNPIOC2x10GESFPPLUSPIC,
       "jnxPic4CHDS3E3MICSR": jnxPic4CHDS3E3MICSR,
       "jnxPic4CHOC31CHOC12MICSR": jnxPic4CHOC31CHOC12MICSR,
       "jnxPicSNG24x10GELWOPIC": jnxPicSNG24x10GELWOPIC,
       "jnxPic8xGESFPRJ45COMBOMIC": jnxPic8xGESFPRJ45COMBOMIC,
       "jnxPic4X10GESFPPLUSMIC": jnxPic4X10GESFPPLUSMIC,
       "jnxPic4xGERJ45MIC": jnxPic4xGERJ45MIC,
       "jnxPic24X10GESFPPMIC": jnxPic24X10GESFPPMIC,
       "jnxPic24X10GESFPPOTNMIC": jnxPic24X10GESFPPOTNMIC,
       "jnxPic2X100GECFP2MIC": jnxPic2X100GECFP2MIC,
       "jnxPic12X10GESFPPPIC": jnxPic12X10GESFPPPIC,
       "jnxPic12X10GESFPPOTNPIC": jnxPic12X10GESFPPOTNPIC,
       "jnxPic2X100GECFP2PIC": jnxPic2X100GECFP2PIC,
       "jnxPicWdSf12X10GESFPPPIC": jnxPicWdSf12X10GESFPPPIC,
       "jnxPicNX10GESFPPOTNDEBUGPIC": jnxPicNX10GESFPPOTNDEBUGPIC,
       "jnxPicWdSf12X10GESFPPOTNPIC": jnxPicWdSf12X10GESFPPOTNPIC,
       "jnxPic3X40GEQSFPPPIC": jnxPic3X40GEQSFPPPIC,
       "jnxPic1X100GECFP2PIC": jnxPic1X100GECFP2PIC,
       "jnxPicQFX48x10GESFP": jnxPicQFX48x10GESFP,
       "jnxPicKFIPCSFPPPIC": jnxPicKFIPCSFPPPIC,
       "jnxPicKFIPCCFP2PIC": jnxPicKFIPCCFP2PIC,
       "jnxPicJAVAxUplinkSFFPlusMACSEC4PORT": jnxPicJAVAxUplinkSFFPlusMACSEC4PORT,
       "jnxPicEX8200M48XSO": jnxPicEX8200M48XSO,
       "jnxPicEX8200M12LQO": jnxPicEX8200M12LQO,
       "jnxPicEX8200M2CF": jnxPicEX8200M2CF,
       "jnxPicOpusQic4X40G": jnxPicOpusQic4X40G,
       "jnxPic20XGESfpEHMIC": jnxPic20XGESfpEHMIC,
       "jnxPic1XCOC124XCOC3CEHMIC": jnxPic1XCOC124XCOC3CEHMIC,
       "jnxPicPISA16XT1E1HMIC": jnxPicPISA16XT1E1HMIC,
       "jnxPic20XGESFPEMIC": jnxPic20XGESFPEMIC,
       "jnxPicUplinkMacsecSFPplus1G4": jnxPicUplinkMacsecSFPplus1G4,
       "jnxPicUplinkMacsecSFPplus10G2": jnxPicUplinkMacsecSFPplus10G2,
       "jnxPicUplinkMacsecSFPplus4port": jnxPicUplinkMacsecSFPplus4port,
       "jnxPicVMX10X1GEPIC": jnxPicVMX10X1GEPIC,
       "jnxPic10XGESFPHALFEHMIC": jnxPic10XGESFPHALFEHMIC,
       "jnxPic10XGESFPHALFEMIC": jnxPic10XGESFPHALFEMIC,
       "jnxPic1xOC124xOC3SFP": jnxPic1xOC124xOC3SFP,
       "jnxPicEX920040x1GbERJ45": jnxPicEX920040x1GbERJ45,
       "jnxPicEX920020x1GbESFP": jnxPicEX920020x1GbESFP,
       "jnxPicEX92002x40GbEQSFPP": jnxPicEX92002x40GbEQSFPP,
       "jnxPic4X100GECXPMIC": jnxPic4X100GECXPMIC,
       "jnxPicQFXEM4Q": jnxPicQFXEM4Q,
       "jnxPicQFXEM8S": jnxPicQFXEM8S,
       "jnxPicSRXIOC21X100GECFP": jnxPicSRXIOC21X100GECFP,
       "jnxPicSRXIOC210X10GESFPP": jnxPicSRXIOC210X10GESFPP,
       "jnxPicSRXIOC22X40GEQSFP": jnxPicSRXIOC22X40GEQSFP,
       "jnxPicCHV4X100GCFP2": jnxPicCHV4X100GCFP2,
       "jnxPicCHVLOAD": jnxPicCHVLOAD,
       "jnxPicEX4300UplinkSFPPlus8Port": jnxPicEX4300UplinkSFPPlus8Port,
       "jnxPicEX4300UplinkQSFP2Port": jnxPicEX4300UplinkQSFP2Port,
       "jnxPicCHVfake4X100GCFP2": jnxPicCHVfake4X100GCFP2,
       "jnxPicQFX510024Q": jnxPicQFX510024Q,
       "jnxPicWdSf2X10GESFPPOTNPIC": jnxPicWdSf2X10GESFPPOTNPIC,
       "jnxPicEX920012X10GESFPPPIC": jnxPicEX920012X10GESFPPPIC,
       "jnxPicEX92003X40GEQSFPPPIC": jnxPicEX92003X40GEQSFPPPIC,
       "jnxPicEX920020X1GESFPMACSECMIC": jnxPicEX920020X1GESFPMACSECMIC,
       "jnxPicEX920020X1GESFPMACSECHALFMIC": jnxPicEX920020X1GESFPMACSECHALFMIC,
       "jnxPicEX4300QSFP2Port": jnxPicEX4300QSFP2Port,
       "jnxPicCHV4X100GOTNCFP2": jnxPicCHV4X100GOTNCFP2,
       "jnxPicCHV48X10G12X40GLWOPIC": jnxPicCHV48X10G12X40GLWOPIC,
       "jnxPicQFX24x40GEFQSFP": jnxPicQFX24x40GEFQSFP,
       "jnxPicQFX48x10GEFSFP": jnxPicQFX48x10GEFSFP,
       "jnxPicQFX6x40GEFQSFP": jnxPicQFX6x40GEFQSFP,
       "jnxPicQFX96X10GEFSFP8X40GEFQSFP": jnxPicQFX96X10GEFSFP8X40GEFQSFP,
       "jnxPicQFX48X10GECSFP6X40GEFQSFP": jnxPicQFX48X10GECSFP6X40GEFQSFP,
       "jnxPicQFX510048S6Q": jnxPicQFX510048S6Q,
       "jnxPicQFX510024S4Q": jnxPicQFX510024S4Q,
       "jnxPicQFX510096S8Q": jnxPicQFX510096S8Q,
       "jnxPicQFX510048C6Q": jnxPicQFX510048C6Q,
       "jnxPicEX460024S4Q": jnxPicEX460024S4Q,
       "jnxPicEX4600EM8F": jnxPicEX4600EM8F,
       "jnxPic8X100GECFP4MIC": jnxPic8X100GECFP4MIC,
       "jnxPic12X40GEQSFPPMIC": jnxPic12X40GEQSFPPMIC,
       "jnxPicMPC8LOADMIC": jnxPicMPC8LOADMIC,
       "jnxPic6XQSFPP": jnxPic6XQSFPP,
       "jnxPic20X10GE": jnxPic20X10GE,
       "jnxPicQFX510048C6QF": jnxPicQFX510048C6QF,
       "jnxPicQFX510048C6QFQSFP": jnxPicQFX510048C6QFQSFP,
       "jnxPicCHV12X40GLWOPIC": jnxPicCHV12X40GLWOPIC,
       "jnxPicSRXIOC220X1GESFP": jnxPicSRXIOC220X1GESFP,
       "jnxPicSRXIOC210X1GESFP": jnxPicSRXIOC210X1GESFP,
       "jnxPic3xGERJ453xPOEMIC": jnxPic3xGERJ453xPOEMIC,
       "jnxPic3xGERJ45MIC": jnxPic3xGERJ45MIC,
       "jnxPic4xGESFPRJ453xPOEMIC": jnxPic4xGESFPRJ453xPOEMIC,
       "jnxPic3xGESFP": jnxPic3xGESFP,
       "jnxPicMultiserviceBuiltin": jnxPicMultiserviceBuiltin,
       "jnxPicCHV4X100GCXPPIC": jnxPicCHV4X100GCXPPIC,
       "jnxPicPTXMLC24X10GESFPP": jnxPicPTXMLC24X10GESFPP,
       "jnxPicCordoba1X100DwdmMIC": jnxPicCordoba1X100DwdmMIC,
       "jnxPicPTXLoadMIC": jnxPicPTXLoadMIC,
       "jnxPicIOCIII12X10SFPP": jnxPicIOCIII12X10SFPP,
       "jnxPicIOCIII4X40QSFPP": jnxPicIOCIII4X40QSFPP,
       "jnxPicIOCIII1X100CFP2": jnxPicIOCIII1X100CFP2,
       "jnxPicIOCIII2X10SFPP": jnxPicIOCIII2X10SFPP,
       "jnxPicEX920010X10GESFPPMIC": jnxPicEX920010X10GESFPPMIC,
       "jnxPicEX920020X10GESFPPMIC": jnxPicEX920020X10GESFPPMIC,
       "jnxPicEX92006XQSFPPPIC": jnxPicEX92006XQSFPPPIC,
       "jnxPicPTX15X100GEREV1PIC": jnxPicPTX15X100GEREV1PIC,
       "jnxPicPTX10X100GEREV1PIC": jnxPicPTX10X100GEREV1PIC,
       "jnxPicPTX2X100GMETROOTNPIC": jnxPicPTX2X100GMETROOTNPIC,
       "jnxPicQFX510024QAA": jnxPicQFX510024QAA,
       "jnxPicQFXPFA4Q": jnxPicQFXPFA4Q,
       "jnxPicACX5048": jnxPicACX5048,
       "jnxPicACX5096": jnxPicACX5096,
       "jnxPicCordoba5X100DwdmPIC": jnxPicCordoba5X100DwdmPIC,
       "jnxPicSHO10X100GEQSFPPIC": jnxPicSHO10X100GEQSFPPIC,
       "jnxPicVQFX5C24X100GEPIC": jnxPicVQFX5C24X100GEPIC,
       "jnxPicPTX1K72X40GEPIC": jnxPicPTX1K72X40GEPIC,
       "jnxPicQFX1000236Q": jnxPicQFX1000236Q,
       "jnxPicQFX1000272Q": jnxPicQFX1000272Q,
       "jnxPicQFX520032C32Q": jnxPicQFX520032C32Q,
       "jnxPicQFX520032C64Q": jnxPicQFX520032C64Q,
       "jnxPicQ511048S4Q2C": jnxPicQ511048S4Q2C,
       "jnxPicQ511032Q4C": jnxPicQ511032Q4C,
       "jnxPicEX3400QSFP2Port": jnxPicEX3400QSFP2Port,
       "jnxPicEX3400UplinkSFPPlus4Port": jnxPicEX3400UplinkSFPPlus4Port,
       "jnxPic10GE40GE100GEPIC": jnxPic10GE40GE100GEPIC,
       "jnxPicEX2300UplinkSFPPlus4Port": jnxPicEX2300UplinkSFPPlus4Port,
       "jnxPicEX2300UplinkSFPPlus2Port": jnxPicEX2300UplinkSFPPlus2Port,
       "jnxPicSRXSMET1E1RPIC": jnxPicSRXSMET1E1RPIC,
       "jnxPicSRXSMEVDSLANNEXARPIC": jnxPicSRXSMEVDSLANNEXARPIC,
       "jnxPicSRXSMESERIALRPIC": jnxPicSRXSMESERIALRPIC,
       "jnxPicSRXSME16PORTGEPOERPIC": jnxPicSRXSME16PORTGEPOERPIC,
       "jnxPicSRXSME8SFPRPIC": jnxPicSRXSME8SFPRPIC,
       "jnxPicULC36Q12Q28": jnxPicULC36Q12Q28,
       "jnxPicULC30Q28": jnxPicULC30Q28,
       "jnxPicVMXMIC": jnxPicVMXMIC,
       "jnxPicMIC8OC3OC124OC48": jnxPicMIC8OC3OC124OC48,
       "jnxPicMIC4OC3OC121OC48": jnxPicMIC4OC3OC121OC48,
       "jnxPicMIC8DS3E3": jnxPicMIC8DS3E3,
       "jnxPicMIC8CHDS3E3": jnxPicMIC8CHDS3E3,
       "jnxPicMIC8CHOC34CHOC12": jnxPicMIC8CHOC34CHOC12,
       "jnxPicMIC4CHOC32CHOC12": jnxPicMIC4CHOC32CHOC12,
       "jnxPicMIC1CHOC48": jnxPicMIC1CHOC48,
       "jnxPicMIC12CHE1T1": jnxPicMIC12CHE1T1,
       "jnxPicMIC1OC192HOVCAT": jnxPicMIC1OC192HOVCAT,
       "jnxPicSHO10X100GEQSFPV2PIC": jnxPicSHO10X100GEQSFPV2PIC,
       "jnxPicGLD96x10GE24x40GE8x100GEQSFPV2PIC": jnxPicGLD96x10GE24x40GE8x100GEQSFPV2PIC,
       "jnxPicSummitSRX1RU4xQSFP28PIC": jnxPicSummitSRX1RU4xQSFP28PIC,
       "jnxPicSummitSRX1RU8xSFPPPIC": jnxPicSummitSRX1RU8xSFPPPIC,
       "jnxPicSummitSRX3RU4xQSFPPPIC": jnxPicSummitSRX3RU4xQSFPPPIC,
       "jnxPicOpusFcQic8X10G": jnxPicOpusFcQic8X10G,
       "jnxPicPTX3X400GE12X100GECFP8PIC": jnxPicPTX3X400GE12X100GECFP8PIC,
       "jnxPicSummitLoadTIC": jnxPicSummitLoadTIC,
       "jnxPicMXTSR802xSFPP2xSFPSecureMIC": jnxPicMXTSR802xSFPP2xSFPSecureMIC,
       "jnxPicValeLoadTicS2SAirFlow": jnxPicValeLoadTicS2SAirFlow,
       "jnxPicSRXSMELTEAAPIC": jnxPicSRXSMELTEAAPIC,
       "jnxPicSRXSMELTEAEPIC": jnxPicSRXSMELTEAEPIC,
       "jnxPic5XQSFPP": jnxPic5XQSFPP,
       "jnxPicEX4300MP4xSFPPlusPIC": jnxPicEX4300MP4xSFPPlusPIC,
       "jnxPicEX4300MP2xQSFPPIC": jnxPicEX4300MP2xQSFPPIC,
       "jnxPicEx4300MP1xQSFP28PIC": jnxPicEx4300MP1xQSFP28PIC,
       "jnxPicNFXEM8T": jnxPicNFXEM8T,
       "jnxPicNFXEM4XSFP": jnxPicNFXEM4XSFP,
       "jnxPicNFXEM8XSFP": jnxPicNFXEM8XSFP,
       "jnxPicNFXEM2T2SFP": jnxPicNFXEM2T2SFP,
       "jnxPicNFXEMLTEAE": jnxPicNFXEMLTEAE,
       "jnxPicNFXEMLTEAA": jnxPicNFXEMLTEAA,
       "jnxPicSummitMX3RU6xQSPPPIC": jnxPicSummitMX3RU6xQSPPPIC,
       "jnxPicSummitMX3RU12xQSFP28MacsecTIC": jnxPicSummitMX3RU12xQSFP28MacsecTIC,
       "jnxPicSummitMX3RU12xQSFP28TIC": jnxPicSummitMX3RU12xQSFP28TIC,
       "jnxPicSummitSRXHA4xSFPPPIC": jnxPicSummitSRXHA4xSFPPPIC,
       "jnxPicQFX540016QSFP28TIC": jnxPicQFX540016QSFP28TIC,
       "jnxPicEX4300MPQSFPPlus4Port": jnxPicEX4300MPQSFPPlus4Port,
       "jnxPicBracklaPIC": jnxPicBracklaPIC,
       "jnxPicACX544848X10GESFPMIC": jnxPicACX544848X10GESFPMIC,
       "jnxPicACX54484X100GESFPMIC": jnxPicACX54484X100GESFPMIC,
       "jnxPicRedbull10xQSFPPPIC": jnxPicRedbull10xQSFPPPIC,
       "jnxPicPTXfake3X400GECFP8": jnxPicPTXfake3X400GECFP8,
       "jnxPicSummitSRXFLOWPIC": jnxPicSummitSRXFLOWPIC,
       "jnxPicStout12xQSFP28MacsecTIC": jnxPicStout12xQSFP28MacsecTIC,
       "jnxPicPTX10008XCFP2DCOTIC": jnxPicPTX10008XCFP2DCOTIC,
       "jnxPicQFX1000260C": jnxPicQFX1000260C,
       "jnxPicEX2300MPUplinkSFPPlus6Port": jnxPicEX2300MPUplinkSFPPlus6Port,
       "jnxPicEX2300MPUplinkSFPPlus4Port": jnxPicEX2300MPUplinkSFPPlus4Port,
       "jnxPicSPC3SPUCPType1PIC": jnxPicSPC3SPUCPType1PIC,
       "jnxPicSPC3SPUFlowType2PIC": jnxPicSPC3SPUFlowType2PIC,
       "jnxPicSPC3SPUCPFlowType3PIC": jnxPicSPC3SPUCPFlowType3PIC,
       "jnxPicGLD15x100GE15x40GE60x10GEQSFPPIC": jnxPicGLD15x100GE15x40GE60x10GEQSFPPIC,
       "jnxPicGLD96x10GE24x40GEQSFPPIC": jnxPicGLD96x10GE24x40GEQSFPPIC,
       "jnxPicIndus4xQSFP28MacsecPIC": jnxPicIndus4xQSFP28MacsecPIC,
       "jnxPic2x10GESFPP20xGESFPMACSecMIC": jnxPic2x10GESFPP20xGESFPMACSecMIC,
       "jnxPicIndus4xQSFP28SyncePIC": jnxPicIndus4xQSFP28SyncePIC,
       "jnxPicQFX521064C": jnxPicQFX521064C,
       "jnxPicQFX520048Y": jnxPicQFX520048Y,
       "jnxPicPTX1000260C": jnxPicPTX1000260C,
       "jnxPicSapphire32CDPIC": jnxPicSapphire32CDPIC,
       "jnxPicSapphire128CPIC": jnxPicSapphire128CPIC,
       "jnxPicDCOSQFX520032CPIC": jnxPicDCOSQFX520032CPIC,
       "jnxPicRB5xQSFPP": jnxPicRB5xQSFPP,
       "jnxPicJnp10k36xQSFPDD": jnxPicJnp10k36xQSFPDD,
       "jnxPicQFX512048Y8C": jnxPicQFX512048Y8C,
       "jnxPicEX465048Y8C": jnxPicEX465048Y8C,
       "jnxPicAttella8XQSFP28PIC": jnxPicAttella8XQSFP28PIC,
       "jnxPicAttella4XCFP2DCOPIC": jnxPicAttella4XCFP2DCOPIC,
       "jnxPicACX5448M44X10GESFPMIC": jnxPicACX5448M44X10GESFPMIC,
       "jnxPicACX5448M6X100GEQSFPMIC": jnxPicACX5448M6X100GEQSFPMIC,
       "jnxPicACX5448D36X10GESFPMIC": jnxPicACX5448D36X10GESFPMIC,
       "jnxPicACX5448D2X100GEQSFPMIC": jnxPicACX5448D2X100GEQSFPMIC,
       "jnxPicACX5448D2X200GECFP2DCOMIC": jnxPicACX5448D2X200GECFP2DCOMIC,
       "jnxPicAS781664X": jnxPicAS781664X,
       "jnxPicQFX512032C": jnxPicQFX512032C,
       "jnxPicIOCIV6XQSFPP": jnxPicIOCIV6XQSFPP,
       "jnxPicIOCIV20X10GESFPP": jnxPicIOCIV20X10GESFPP,
       "jnxPicMXSPC3PIC": jnxPicMXSPC3PIC,
       "jnxPicJnp10k36xQDDPIC": jnxPicJnp10k36xQDDPIC,
       "jnxPicSRXSMEWAPUSPIC": jnxPicSRXSMEWAPUSPIC,
       "jnxPicSRXSMEWAPISPIC": jnxPicSRXSMEWAPISPIC,
       "jnxPicSRXSMEWAPWWPIC": jnxPicSRXSMEWAPWWPIC,
       "jnxPicACX71024X10GESFPMIC": jnxPicACX71024X10GESFPMIC,
       "jnxPicACX7104X100GESFPMIC": jnxPicACX7104X100GESFPMIC,
       "jnxPicACX580048X10GESFPMIC": jnxPicACX580048X10GESFPMIC,
       "jnxPicACX580032X10GESFPMIC": jnxPicACX580032X10GESFPMIC,
       "jnxPicACX58004X100GESFPMIC": jnxPicACX58004X100GESFPMIC,
       "jnxPicR667524X10GESFPMIC": jnxPicR667524X10GESFPMIC,
       "jnxPicR66754X100GESFPMIC": jnxPicR66754X100GESFPMIC,
       "jnxPicR627448X10GESFPMIC": jnxPicR627448X10GESFPMIC,
       "jnxPicR627432X10GESFPMIC": jnxPicR627432X10GESFPMIC,
       "jnxPicR62744X100GESFPMIC": jnxPicR62744X100GESFPMIC,
       "jnxPicEX44004x25GESFP28PIC": jnxPicEX44004x25GESFP28PIC,
       "jnxPicEX44004x10GESFPPPIC": jnxPicEX44004x10GESFPPPIC,
       "jnxPicQFX512048T6C": jnxPicQFX512048T6C,
       "jnxPicArdbegPIC": jnxPicArdbegPIC,
       "jnxPicJnp10k4xQDD32xQ": jnxPicJnp10k4xQDD32xQ,
       "jnxPicEXMRATE5XQSFPP": jnxPicEXMRATE5XQSFPP,
       "jnxPicQFX513032CDPIC": jnxPicQFX513032CDPIC,
       "jnxPicQFX513048CPIC": jnxPicQFX513048CPIC,
       "jnxPicACX7538x25GESFP28PIC": jnxPicACX7538x25GESFP28PIC,
       "jnxPicACX7532x100GEQSFP28PIC": jnxPicACX7532x100GEQSFP28PIC,
       "jnxPicACX7534x100GEQSFP28PIC": jnxPicACX7534x100GEQSFP28PIC,
       "jnxPicACX7538x10GESFPPIC": jnxPicACX7538x10GESFPPIC,
       "jnxPicJerrico2PIC": jnxPicJerrico2PIC,
       "jnxPicJNP710048LPIC": jnxPicJNP710048LPIC,
       "jnxPicACX710032CPIC": jnxPicACX710032CPIC,
       "jnxPicJNP710080PIC": jnxPicJNP710080PIC,
       "jnxPicDaniel24xSFPP1G10GPIC": jnxPicDaniel24xSFPP1G10GPIC,
       "jnxPicQFX512048YM8C": jnxPicQFX512048YM8C,
       "jnxPicLC96004xQDDPIC": jnxPicLC96004xQDDPIC,
       "jnxPicQFX570016x100QSFP28PIC": jnxPicQFX570016x100QSFP28PIC,
       "jnxPicQFX57004x400QSFP56DDPIC": jnxPicQFX57004x400QSFP56DDPIC,
       "jnxPicACX75520x1G10G25G50GSFP28PIC": jnxPicACX75520x1G10G25G50GSFP28PIC,
       "jnxPicJNP710048LPSMPIC": jnxPicJNP710048LPSMPIC,
       "jnxPicACX710032CPSMPIC": jnxPicACX710032CPSMPIC,
       "jnxPicSRXEMLTEAA": jnxPicSRXEMLTEAA,
       "jnxPicSRXEMLTEAE": jnxPicSRXEMLTEAE,
       "jnxPicSRXEM4T2SFP": jnxPicSRXEM4T2SFP,
       "jnxPicACX75516x100QSFP28PIC": jnxPicACX75516x100QSFP28PIC,
       "jnxPicACX7554x400QSFP56DDPIC": jnxPicACX7554x400QSFP56DDPIC,
       "jnxPicWBONLPIC": jnxPicWBONLPIC,
       "jnxPic5GS6GLPIC": jnxPic5GS6GLPIC,
       "jnxPic5GS6MWNAPIC": jnxPic5GS6MWNAPIC,
       "jnxPic5GS6MWEAPIC": jnxPic5GS6MWEAPIC,
       "jnxPicTabascoCryptoSPC4Type1PIC": jnxPicTabascoCryptoSPC4Type1PIC,
       "jnxPicTabascoCryptoSPC4Type2PIC": jnxPicTabascoCryptoSPC4Type2PIC,
       "jnxPicTabascoCryptoSPC4Type3PIC": jnxPicTabascoCryptoSPC4Type3PIC,
       "jnxPicTabascoCryptoSPC4MXPIC": jnxPicTabascoCryptoSPC4MXPIC,
       "jnxPicEX44002xQSFP28PIC": jnxPicEX44002xQSFP28PIC,
       "jnxPicACX75520x10G25G50GSFP28PIC": jnxPicACX75520x10G25G50GSFP28PIC,
       "jnxPicQFX523064CDPIC": jnxPicQFX523064CDPIC,
       "jnxPicMX304PIC": jnxPicMX304PIC,
       "jnxPicEX4100UplinkSFPPlus4Port": jnxPicEX4100UplinkSFPPlus4Port,
       "jnxPicEX4100UplinkSFPPlus2Port": jnxPicEX4100UplinkSFPPlus2Port,
       "jnxPicEX4100VCSFP284Port": jnxPicEX4100VCSFP284Port,
       "jnxPicIOCV5XQSFPP": jnxPicIOCV5XQSFPP,
       "jnxPicEX44001xQSFP28PIC": jnxPicEX44001xQSFP28PIC,
       "jnxPicGLQFX513048CPIC": jnxPicGLQFX513048CPIC,
       "jnxPicLC48002xQDD12xSDDPIC": jnxPicLC48002xQDD12xSDDPIC,
       "jnxPicLC480016xSDDPIC": jnxPicLC480016xSDDPIC,
       "jnxPicLC48004xQDD8xQPIC": jnxPicLC48004xQDD8xQPIC,
       "jnxPicGLQFX513048CMPIC": jnxPicGLQFX513048CMPIC,
       "jnxPicGLDQFX5130E32CDPIC": jnxPicGLDQFX5130E32CDPIC,
       "jnxPicSRX160016x1GT": jnxPicSRX160016x1GT,
       "jnxPicSRX16002xSFP28": jnxPicSRX16002xSFP28,
       "jnxPicSRX16004xSFP": jnxPicSRX16004xSFP,
       "jnxPicSRX23008x10GT": jnxPicSRX23008x10GT,
       "jnxPicSRX23008xSFP": jnxPicSRX23008xSFP,
       "jnxPicSRX23004xSFP28": jnxPicSRX23004xSFP28,
       "jnxPicSRX23002QSFP28": jnxPicSRX23002QSFP28,
       "jnxPicSRX43008x10GT": jnxPicSRX43008x10GT,
       "jnxPicSRX43008xSFP": jnxPicSRX43008xSFP,
       "jnxPicSRX43004xSFP28": jnxPicSRX43004xSFP28,
       "jnxPicSRX43006QSFP28": jnxPicSRX43006QSFP28,
       "jnxPicQFX524064OSFPPIC": jnxPicQFX524064OSFPPIC,
       "jnxPicQFX524064QSFPDDPIC": jnxPicQFX524064QSFPDDPIC,
       "jnxPicSRX47001xQSFPDD5xQSFP288xSFP56": jnxPicSRX47001xQSFPDD5xQSFP288xSFP56,
       "jnxPicSRX4700FlowPIC": jnxPicSRX4700FlowPIC,
       "jnxPicEX4100VCSFPSFPPlus2Port": jnxPicEX4100VCSFPSFPPlus2Port,
       "jnxPicEX4100VCSFPSFPPlus4Port": jnxPicEX4100VCSFPSFPPlus4Port,
       "jnxMic": jnxMic,
       "jnxMiscComponent": jnxMiscComponent,
       "jnxTempSensor": jnxTempSensor,
       "jnxClassStatus": jnxClassStatus,
       "jnxStatusSource": jnxStatusSource,
       "jnxStatusSourceM40": jnxStatusSourceM40,
       "jnxChassisSlotLED": jnxChassisSlotLED,
       "jnxChassisAlarmLED": jnxChassisAlarmLED,
       "jnxHostCtlrLED": jnxHostCtlrLED,
       "jnxChassisTempSensor": jnxChassisTempSensor,
       "jnxRoutingEngineLED": jnxRoutingEngineLED,
       "jnxChassisDefines": jnxChassisDefines}
)
