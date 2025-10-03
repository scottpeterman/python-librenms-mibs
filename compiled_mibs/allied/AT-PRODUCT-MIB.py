# SNMP MIB module (AT-PRODUCT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\allied\AT-PRODUCT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:32 2025
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

(alliedTelesis,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "alliedTelesis")

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

products = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1)
)
if mibBuilder.loadTexts:
    products.setRevisions(
        ("2021-04-22 00:00",
         "2021-03-25 00:00",
         "2021-02-25 00:00",
         "2021-02-11 00:00",
         "2021-01-18 00:00",
         "2020-10-14 00:00",
         "2020-06-24 00:00",
         "2020-06-18 00:00",
         "2020-06-02 00:00",
         "2019-12-04 00:00",
         "2019-07-30 00:00",
         "2019-06-05 00:00",
         "2019-05-29 00:00",
         "2019-05-28 00:00",
         "2019-05-22 00:00",
         "2019-03-11 00:00",
         "2018-10-03 00:00",
         "2018-09-17 00:00",
         "2018-09-04 00:00",
         "2018-08-30 00:00",
         "2018-08-22 00:00",
         "2018-07-19 00:00",
         "2018-04-06 00:00",
         "2018-03-20 00:00",
         "2018-01-18 00:00",
         "2017-12-08 00:00",
         "2017-11-14 00:00",
         "2017-10-19 00:00",
         "2017-03-31 00:00",
         "2017-02-01 00:00",
         "2017-01-18 00:00",
         "2016-10-03 00:00",
         "2016-07-25 00:00",
         "2016-05-06 00:00",
         "2016-01-08 00:00",
         "2015-11-10 00:00",
         "2015-08-05 00:00",
         "2015-07-27 00:00",
         "2015-07-22 00:00",
         "2015-05-06 00:00",
         "2015-04-03 00:00",
         "2014-11-19 00:00",
         "2014-11-18 00:00",
         "2014-10-22 00:00",
         "2014-09-23 00:00",
         "2014-08-28 00:00",
         "2014-08-20 00:00",
         "2014-07-30 00:00",
         "2014-06-09 00:00",
         "2014-06-03 00:00",
         "2014-05-16 00:00",
         "2013-08-01 00:00",
         "2013-07-09 00:00",
         "2013-04-02 00:00",
         "2012-03-22 00:00",
         "2011-12-18 05:00",
         "2011-09-15 00:00",
         "2011-09-14 00:00",
         "2011-09-05 00:00",
         "2011-04-04 00:00",
         "2010-10-12 00:00",
         "2010-09-20 00:00",
         "2010-09-07 00:00",
         "2010-08-19 00:00",
         "2010-07-22 00:00",
         "2010-06-15 00:15",
         "2009-05-19 00:00",
         "2009-05-15 00:00",
         "2008-03-06 13:00",
         "2007-11-15 00:00",
         "2007-03-21 00:00",
         "2007-02-07 00:00",
         "2006-06-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BridgeRouter_ObjectIdentity = ObjectIdentity
bridgeRouter = _BridgeRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1)
)
if mibBuilder.loadTexts:
    bridgeRouter.setStatus("current")
_CentreComAR300Router_ObjectIdentity = ObjectIdentity
centreComAR300Router = _CentreComAR300Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 8)
)
_CentreComAR720Router_ObjectIdentity = ObjectIdentity
centreComAR720Router = _CentreComAR720Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 11)
)
_CentreComAR300LRouter_ObjectIdentity = ObjectIdentity
centreComAR300LRouter = _CentreComAR300LRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 12)
)
_CentreComAR310Router_ObjectIdentity = ObjectIdentity
centreComAR310Router = _CentreComAR310Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 13)
)
_CentreComAR300LURouter_ObjectIdentity = ObjectIdentity
centreComAR300LURouter = _CentreComAR300LURouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 14)
)
_CentreComAR300URouter_ObjectIdentity = ObjectIdentity
centreComAR300URouter = _CentreComAR300URouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 15)
)
_CentreComAR310URouter_ObjectIdentity = ObjectIdentity
centreComAR310URouter = _CentreComAR310URouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 16)
)
_CentreComAR350Router_ObjectIdentity = ObjectIdentity
centreComAR350Router = _CentreComAR350Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 17)
)
_CentreComAR370Router_ObjectIdentity = ObjectIdentity
centreComAR370Router = _CentreComAR370Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 18)
)
_CentreComAR330Router_ObjectIdentity = ObjectIdentity
centreComAR330Router = _CentreComAR330Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 19)
)
_CentreComAR395Router_ObjectIdentity = ObjectIdentity
centreComAR395Router = _CentreComAR395Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 20)
)
_CentreComAR390Router_ObjectIdentity = ObjectIdentity
centreComAR390Router = _CentreComAR390Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 21)
)
_CentreComAR370URouter_ObjectIdentity = ObjectIdentity
centreComAR370URouter = _CentreComAR370URouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 22)
)
_CentreComAR740Router_ObjectIdentity = ObjectIdentity
centreComAR740Router = _CentreComAR740Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 23)
)
_CentreComAR140SRouter_ObjectIdentity = ObjectIdentity
centreComAR140SRouter = _CentreComAR140SRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 24)
)
_CentreComAR140URouter_ObjectIdentity = ObjectIdentity
centreComAR140URouter = _CentreComAR140URouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 25)
)
_CentreComAR320Router_ObjectIdentity = ObjectIdentity
centreComAR320Router = _CentreComAR320Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 26)
)
_CentreComAR130SRouter_ObjectIdentity = ObjectIdentity
centreComAR130SRouter = _CentreComAR130SRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 27)
)
_CentreComAR130URouter_ObjectIdentity = ObjectIdentity
centreComAR130URouter = _CentreComAR130URouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 28)
)
_CentreComAR160Router_ObjectIdentity = ObjectIdentity
centreComAR160Router = _CentreComAR160Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 29)
)
_AtAR740RouterDC_ObjectIdentity = ObjectIdentity
atAR740RouterDC = _AtAR740RouterDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 43)
)
_CentreComAR120Router_ObjectIdentity = ObjectIdentity
centreComAR120Router = _CentreComAR120Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 44)
)
_AtAR410Router_ObjectIdentity = ObjectIdentity
atAR410Router = _AtAR410Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 47)
)
_AtAR725Router_ObjectIdentity = ObjectIdentity
atAR725Router = _AtAR725Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 48)
)
_AtAR745Router_ObjectIdentity = ObjectIdentity
atAR745Router = _AtAR745Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 49)
)
_AtAR410v2Router_ObjectIdentity = ObjectIdentity
atAR410v2Router = _AtAR410v2Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 50)
)
_AtAR410v3Router_ObjectIdentity = ObjectIdentity
atAR410v3Router = _AtAR410v3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 51)
)
_AtAR725RouterDC_ObjectIdentity = ObjectIdentity
atAR725RouterDC = _AtAR725RouterDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 52)
)
_AtAR745RouterDC_ObjectIdentity = ObjectIdentity
atAR745RouterDC = _AtAR745RouterDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 53)
)
_AtAR450Router_ObjectIdentity = ObjectIdentity
atAR450Router = _AtAR450Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 54)
)
_AtAR450DualRouter_ObjectIdentity = ObjectIdentity
atAR450DualRouter = _AtAR450DualRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 55)
)
_AtAR440Router_ObjectIdentity = ObjectIdentity
atAR440Router = _AtAR440Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 59)
)
_AtAR441Router_ObjectIdentity = ObjectIdentity
atAR441Router = _AtAR441Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 60)
)
_AtAR442Router_ObjectIdentity = ObjectIdentity
atAR442Router = _AtAR442Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 61)
)
_AtAR443Router_ObjectIdentity = ObjectIdentity
atAR443Router = _AtAR443Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 62)
)
_AtAR444Router_ObjectIdentity = ObjectIdentity
atAR444Router = _AtAR444Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 63)
)
_AtAR420Router_ObjectIdentity = ObjectIdentity
atAR420Router = _AtAR420Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 64)
)
_AtAR415SRouter_ObjectIdentity = ObjectIdentity
atAR415SRouter = _AtAR415SRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 71)
)
_AtAR415SRouterDC_ObjectIdentity = ObjectIdentity
atAR415SRouterDC = _AtAR415SRouterDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 72)
)
_AtAR550Router_ObjectIdentity = ObjectIdentity
atAR550Router = _AtAR550Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 73)
)
_AtAR551Router_ObjectIdentity = ObjectIdentity
atAR551Router = _AtAR551Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 74)
)
_AtAR552Router_ObjectIdentity = ObjectIdentity
atAR552Router = _AtAR552Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 75)
)
_AtAR550SRouterDP_ObjectIdentity = ObjectIdentity
atAR550SRouterDP = _AtAR550SRouterDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 76)
)
_AtAR570Router_ObjectIdentity = ObjectIdentity
atAR570Router = _AtAR570Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 78)
)
_AtAR770Router_ObjectIdentity = ObjectIdentity
atAR770Router = _AtAR770Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 79)
)
_AtAR750SRouterDP_ObjectIdentity = ObjectIdentity
atAR750SRouterDP = _AtAR750SRouterDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 80)
)
_AtAR560SRouter_ObjectIdentity = ObjectIdentity
atAR560SRouter = _AtAR560SRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 81)
)
_AtAR3050SRouter_ObjectIdentity = ObjectIdentity
atAR3050SRouter = _AtAR3050SRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 82)
)
_AtAR4050SRouter_ObjectIdentity = ObjectIdentity
atAR4050SRouter = _AtAR4050SRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 85)
)
_AtAR2050VRouter_ObjectIdentity = ObjectIdentity
atAR2050VRouter = _AtAR2050VRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 88)
)
_AtAR2010VRouter_ObjectIdentity = ObjectIdentity
atAR2010VRouter = _AtAR2010VRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 89)
)
_AtAR1050VRouter_ObjectIdentity = ObjectIdentity
atAR1050VRouter = _AtAR1050VRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 90)
)
_AtAR4050S5GRouter_ObjectIdentity = ObjectIdentity
atAR4050S5GRouter = _AtAR4050S5GRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 91)
)
_Swhub_ObjectIdentity = ObjectIdentity
swhub = _Swhub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4)
)
if mibBuilder.loadTexts:
    swhub.setStatus("current")
_Atx200GE52T_ObjectIdentity = ObjectIdentity
atx200GE52T = _Atx200GE52T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 181)
)
_Atx200GE28T_ObjectIdentity = ObjectIdentity
atx200GE28T = _Atx200GE28T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 182)
)
_Atx2109GT_ObjectIdentity = ObjectIdentity
atx2109GT = _Atx2109GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 196)
)
_Atx21016GT_ObjectIdentity = ObjectIdentity
atx21016GT = _Atx21016GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 197)
)
_Atx21024GT_ObjectIdentity = ObjectIdentity
atx21024GT = _Atx21024GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 198)
)
_Atx31026FT_ObjectIdentity = ObjectIdentity
atx31026FT = _Atx31026FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 216)
)
_Atx31050FT_ObjectIdentity = ObjectIdentity
atx31050FT = _Atx31050FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 217)
)
_Atx31026FP_ObjectIdentity = ObjectIdentity
atx31026FP = _Atx31026FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 218)
)
_Atx31050FP_ObjectIdentity = ObjectIdentity
atx31050FP = _Atx31050FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 219)
)
_Atx31026GT_ObjectIdentity = ObjectIdentity
atx31026GT = _Atx31026GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 220)
)
_Atx31050GT_ObjectIdentity = ObjectIdentity
atx31050GT = _Atx31050GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 221)
)
_Atx31026GP_ObjectIdentity = ObjectIdentity
atx31026GP = _Atx31026GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 222)
)
_Atx31050GP_ObjectIdentity = ObjectIdentity
atx31050GP = _Atx31050GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 223)
)
_Atx23010GT_ObjectIdentity = ObjectIdentity
atx23010GT = _Atx23010GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 224)
)
_Atx23018GT_ObjectIdentity = ObjectIdentity
atx23018GT = _Atx23018GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 225)
)
_Atx23028GT_ObjectIdentity = ObjectIdentity
atx23028GT = _Atx23028GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 226)
)
_Atx23052GT_ObjectIdentity = ObjectIdentity
atx23052GT = _Atx23052GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 227)
)
_Atx23010GP_ObjectIdentity = ObjectIdentity
atx23010GP = _Atx23010GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 228)
)
_Atx23018GP_ObjectIdentity = ObjectIdentity
atx23018GP = _Atx23018GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 229)
)
_Atx23028GP_ObjectIdentity = ObjectIdentity
atx23028GP = _Atx23028GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 230)
)
_Atx23052GP_ObjectIdentity = ObjectIdentity
atx23052GP = _Atx23052GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 231)
)
_Atx35010GPT_ObjectIdentity = ObjectIdentity
atx35010GPT = _Atx35010GPT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 232)
)
_AtGS924MX_ObjectIdentity = ObjectIdentity
atGS924MX = _AtGS924MX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 253)
)
_AtGS924MPX_ObjectIdentity = ObjectIdentity
atGS924MPX = _AtGS924MPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 254)
)
_AtGS948MX_ObjectIdentity = ObjectIdentity
atGS948MX = _AtGS948MX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 255)
)
_AtGS948MPX_ObjectIdentity = ObjectIdentity
atGS948MPX = _AtGS948MPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 256)
)
_AtXS916MXT_ObjectIdentity = ObjectIdentity
atXS916MXT = _AtXS916MXT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 257)
)
_AtXS916MXS_ObjectIdentity = ObjectIdentity
atXS916MXS = _AtXS916MXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 258)
)
_AtXS916MXP_ObjectIdentity = ObjectIdentity
atXS916MXP = _AtXS916MXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 259)
)
_AtSH23010GP_ObjectIdentity = ObjectIdentity
atSH23010GP = _AtSH23010GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 260)
)
_AtSH23018GP_ObjectIdentity = ObjectIdentity
atSH23018GP = _AtSH23018GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 261)
)
_AtSH23028GP_ObjectIdentity = ObjectIdentity
atSH23028GP = _AtSH23028GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 262)
)
_AtSH2109GT_ObjectIdentity = ObjectIdentity
atSH2109GT = _AtSH2109GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 263)
)
_AtSH21016GT_ObjectIdentity = ObjectIdentity
atSH21016GT = _AtSH21016GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 264)
)
_AtSH21024GT_ObjectIdentity = ObjectIdentity
atSH21024GT = _AtSH21024GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 265)
)
_AtSH31026FT_ObjectIdentity = ObjectIdentity
atSH31026FT = _AtSH31026FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 266)
)
_AtSH31050FT_ObjectIdentity = ObjectIdentity
atSH31050FT = _AtSH31050FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 267)
)
_AtSH31026FP_ObjectIdentity = ObjectIdentity
atSH31026FP = _AtSH31026FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 268)
)
_AtSH31050FP_ObjectIdentity = ObjectIdentity
atSH31050FP = _AtSH31050FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 269)
)
_AtSH23010GT_ObjectIdentity = ObjectIdentity
atSH23010GT = _AtSH23010GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 270)
)
_AtSH23018GT_ObjectIdentity = ObjectIdentity
atSH23018GT = _AtSH23018GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 271)
)
_AtSH23028GT_ObjectIdentity = ObjectIdentity
atSH23028GT = _AtSH23028GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 272)
)
_AtFS980M9_ObjectIdentity = ObjectIdentity
atFS980M9 = _AtFS980M9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 274)
)
_AtFS980M9PS_ObjectIdentity = ObjectIdentity
atFS980M9PS = _AtFS980M9PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 275)
)
_AtFS980M18_ObjectIdentity = ObjectIdentity
atFS980M18 = _AtFS980M18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 276)
)
_AtFS980M18PS_ObjectIdentity = ObjectIdentity
atFS980M18PS = _AtFS980M18PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 277)
)
_AtFS980M28_ObjectIdentity = ObjectIdentity
atFS980M28 = _AtFS980M28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 278)
)
_AtFS980M28PS_ObjectIdentity = ObjectIdentity
atFS980M28PS = _AtFS980M28PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 279)
)
_AtFS980M52_ObjectIdentity = ObjectIdentity
atFS980M52 = _AtFS980M52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 280)
)
_AtFS980M52PS_ObjectIdentity = ObjectIdentity
atFS980M52PS = _AtFS980M52PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 281)
)
_AtGS910M_ObjectIdentity = ObjectIdentity
atGS910M = _AtGS910M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 282)
)
_AtGS910MP_ObjectIdentity = ObjectIdentity
atGS910MP = _AtGS910MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 283)
)
_AtGS918M_ObjectIdentity = ObjectIdentity
atGS918M = _AtGS918M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 284)
)
_AtGS918MP_ObjectIdentity = ObjectIdentity
atGS918MP = _AtGS918MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 285)
)
_AtGS928M_ObjectIdentity = ObjectIdentity
atGS928M = _AtGS928M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 286)
)
_AtGS928MP_ObjectIdentity = ObjectIdentity
atGS928MP = _AtGS928MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 287)
)
_AtGS952M_ObjectIdentity = ObjectIdentity
atGS952M = _AtGS952M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 288)
)
_AtGS952MP_ObjectIdentity = ObjectIdentity
atGS952MP = _AtGS952MP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 289)
)
_Atx22052GT_ObjectIdentity = ObjectIdentity
atx22052GT = _Atx22052GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 290)
)
_Atx22052GP_ObjectIdentity = ObjectIdentity
atx22052GP = _Atx22052GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 291)
)
_Atx22028GS_ObjectIdentity = ObjectIdentity
atx22028GS = _Atx22028GS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 294)
)
_AtGS980M52_ObjectIdentity = ObjectIdentity
atGS980M52 = _AtGS980M52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 300)
)
_AtGS980M52PS_ObjectIdentity = ObjectIdentity
atGS980M52PS = _AtGS980M52PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 301)
)
_AtGS970M28PS_ObjectIdentity = ObjectIdentity
atGS970M28PS = _AtGS970M28PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 312)
)
_AtGS970M18PS_ObjectIdentity = ObjectIdentity
atGS970M18PS = _AtGS970M18PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 313)
)
_AtGS970M10PS_ObjectIdentity = ObjectIdentity
atGS970M10PS = _AtGS970M10PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 314)
)
_AtGS970M28_ObjectIdentity = ObjectIdentity
atGS970M28 = _AtGS970M28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 315)
)
_AtGS970M18_ObjectIdentity = ObjectIdentity
atGS970M18 = _AtGS970M18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 316)
)
_AtGS970M10_ObjectIdentity = ObjectIdentity
atGS970M10 = _AtGS970M10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 317)
)
_Atx230L17GT_ObjectIdentity = ObjectIdentity
atx230L17GT = _Atx230L17GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 319)
)
_Atx230L26GT_ObjectIdentity = ObjectIdentity
atx230L26GT = _Atx230L26GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 320)
)
_AtFS980M28DP_ObjectIdentity = ObjectIdentity
atFS980M28DP = _AtFS980M28DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 322)
)
_RouterSwitch_ObjectIdentity = ObjectIdentity
routerSwitch = _RouterSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14)
)
if mibBuilder.loadTexts:
    routerSwitch.setStatus("current")
_AtRapier24_ObjectIdentity = ObjectIdentity
atRapier24 = _AtRapier24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 1)
)
_AtRapier16fSC_ObjectIdentity = ObjectIdentity
atRapier16fSC = _AtRapier16fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 2)
)
_AtRapier16fVF_ObjectIdentity = ObjectIdentity
atRapier16fVF = _AtRapier16fVF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 3)
)
_AtRapier16fMT_ObjectIdentity = ObjectIdentity
atRapier16fMT = _AtRapier16fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 4)
)
_AtRapier48_ObjectIdentity = ObjectIdentity
atRapier48 = _AtRapier48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 5)
)
_AtRapier8t8fSC_ObjectIdentity = ObjectIdentity
atRapier8t8fSC = _AtRapier8t8fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 6)
)
_AtRapier8t8fSCi_ObjectIdentity = ObjectIdentity
atRapier8t8fSCi = _AtRapier8t8fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 7)
)
_AtRapier8t8fMT_ObjectIdentity = ObjectIdentity
atRapier8t8fMT = _AtRapier8t8fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 8)
)
_AtRapier8t8fMTi_ObjectIdentity = ObjectIdentity
atRapier8t8fMTi = _AtRapier8t8fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 9)
)
_AtRapier8fSC_ObjectIdentity = ObjectIdentity
atRapier8fSC = _AtRapier8fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 10)
)
_AtRapier8fSCi_ObjectIdentity = ObjectIdentity
atRapier8fSCi = _AtRapier8fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 11)
)
_AtRapier8fMT_ObjectIdentity = ObjectIdentity
atRapier8fMT = _AtRapier8fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 12)
)
_AtRapier8fMTi_ObjectIdentity = ObjectIdentity
atRapier8fMTi = _AtRapier8fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 13)
)
_AtRapier16fMTi_ObjectIdentity = ObjectIdentity
atRapier16fMTi = _AtRapier16fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 14)
)
_AtRapierG6_ObjectIdentity = ObjectIdentity
atRapierG6 = _AtRapierG6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 15)
)
_AtRapierG6SX_ObjectIdentity = ObjectIdentity
atRapierG6SX = _AtRapierG6SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 16)
)
_AtRapierG6LX_ObjectIdentity = ObjectIdentity
atRapierG6LX = _AtRapierG6LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 17)
)
_AtRapierG6MT_ObjectIdentity = ObjectIdentity
atRapierG6MT = _AtRapierG6MT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 18)
)
_AtRapier16fSCi_ObjectIdentity = ObjectIdentity
atRapier16fSCi = _AtRapier16fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 19)
)
_AtRapier24i_ObjectIdentity = ObjectIdentity
atRapier24i = _AtRapier24i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 20)
)
_AtRapier48i_ObjectIdentity = ObjectIdentity
atRapier48i = _AtRapier48i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 21)
)
_AtSwitchblade4AC_ObjectIdentity = ObjectIdentity
atSwitchblade4AC = _AtSwitchblade4AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 22)
)
_AtSwitchblade4DC_ObjectIdentity = ObjectIdentity
atSwitchblade4DC = _AtSwitchblade4DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 23)
)
_AtSwitchblade8AC_ObjectIdentity = ObjectIdentity
atSwitchblade8AC = _AtSwitchblade8AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 24)
)
_AtSwitchblade8DC_ObjectIdentity = ObjectIdentity
atSwitchblade8DC = _AtSwitchblade8DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 25)
)
_At9816GF_ObjectIdentity = ObjectIdentity
at9816GF = _At9816GF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 26)
)
_At9812TF_ObjectIdentity = ObjectIdentity
at9812TF = _At9812TF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 27)
)
_At9816GB_ObjectIdentity = ObjectIdentity
at9816GB = _At9816GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 28)
)
_At9812T_ObjectIdentity = ObjectIdentity
at9812T = _At9812T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 29)
)
_At8724XL_ObjectIdentity = ObjectIdentity
at8724XL = _At8724XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 30)
)
_At8748XL_ObjectIdentity = ObjectIdentity
at8748XL = _At8748XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 31)
)
_At8724XLDC_ObjectIdentity = ObjectIdentity
at8724XLDC = _At8724XLDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 32)
)
_At8748XLDC_ObjectIdentity = ObjectIdentity
at8748XLDC = _At8748XLDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 33)
)
_At9816GbDC_ObjectIdentity = ObjectIdentity
at9816GbDC = _At9816GbDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 34)
)
_At9812tDC_ObjectIdentity = ObjectIdentity
at9812tDC = _At9812tDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 35)
)
_At8824_ObjectIdentity = ObjectIdentity
at8824 = _At8824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 36)
)
_At8848_ObjectIdentity = ObjectIdentity
at8848 = _At8848_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 37)
)
_At8824DC_ObjectIdentity = ObjectIdentity
at8824DC = _At8824DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 38)
)
_At8848DC_ObjectIdentity = ObjectIdentity
at8848DC = _At8848DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 39)
)
_At8624XL80_ObjectIdentity = ObjectIdentity
at8624XL80 = _At8624XL80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 41)
)
_At8724XL80_ObjectIdentity = ObjectIdentity
at8724XL80 = _At8724XL80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 42)
)
_At8748XL80_ObjectIdentity = ObjectIdentity
at8748XL80 = _At8748XL80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 43)
)
_At8948EX_ObjectIdentity = ObjectIdentity
at8948EX = _At8948EX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 44)
)
_At8948i_ObjectIdentity = ObjectIdentity
at8948i = _At8948i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 45)
)
_At8624T2M_ObjectIdentity = ObjectIdentity
at8624T2M = _At8624T2M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 46)
)
_AtRapier24iDcNEBS_ObjectIdentity = ObjectIdentity
atRapier24iDcNEBS = _AtRapier24iDcNEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 47)
)
_At8724XLDcNEBS_ObjectIdentity = ObjectIdentity
at8724XLDcNEBS = _At8724XLDcNEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 48)
)
_At9924T_ObjectIdentity = ObjectIdentity
at9924T = _At9924T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 49)
)
_At9924SP_ObjectIdentity = ObjectIdentity
at9924SP = _At9924SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 50)
)
_At9924T4SP_ObjectIdentity = ObjectIdentity
at9924T4SP = _At9924T4SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 51)
)
_At9924TEMC_ObjectIdentity = ObjectIdentity
at9924TEMC = _At9924TEMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 53)
)
_At8724MLB_ObjectIdentity = ObjectIdentity
at8724MLB = _At8724MLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 55)
)
_At8624POE_ObjectIdentity = ObjectIdentity
at8624POE = _At8624POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 56)
)
_At9924Ts_ObjectIdentity = ObjectIdentity
at9924Ts = _At9924Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 57)
)
_At86482SP_ObjectIdentity = ObjectIdentity
at86482SP = _At86482SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 58)
)
_At9924Ti_ObjectIdentity = ObjectIdentity
at9924Ti = _At9924Ti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 59)
)
_At9924SPi_ObjectIdentity = ObjectIdentity
at9924SPi = _At9924SPi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 60)
)
_At9924Tsi_ObjectIdentity = ObjectIdentity
at9924Tsi = _At9924Tsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 61)
)
_At9924SPsi_ObjectIdentity = ObjectIdentity
at9924SPsi = _At9924SPsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 62)
)
_At8948iN_ObjectIdentity = ObjectIdentity
at8948iN = _At8948iN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 63)
)
_At9924TsiN_ObjectIdentity = ObjectIdentity
at9924TsiN = _At9924TsiN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 64)
)
_AtRapier48w_ObjectIdentity = ObjectIdentity
atRapier48w = _AtRapier48w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 65)
)
_At8724SlV2_ObjectIdentity = ObjectIdentity
at8724SlV2 = _At8724SlV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 67)
)
_X90048FS_ObjectIdentity = ObjectIdentity
x90048FS = _X90048FS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 68)
)
_AtSwitchBladex908_ObjectIdentity = ObjectIdentity
atSwitchBladex908 = _AtSwitchBladex908_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 69)
)
_Atx90012XTS_ObjectIdentity = ObjectIdentity
atx90012XTS = _Atx90012XTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 70)
)
_AtRapier48wb_ObjectIdentity = ObjectIdentity
atRapier48wb = _AtRapier48wb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 71)
)
_AtRapier48wAC_ObjectIdentity = ObjectIdentity
atRapier48wAC = _AtRapier48wAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 72)
)
_AtRapier48wbAC_ObjectIdentity = ObjectIdentity
atRapier48wbAC = _AtRapier48wbAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 73)
)
_Atx90024XT_ObjectIdentity = ObjectIdentity
atx90024XT = _Atx90024XT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 75)
)
_Atx90024XS_ObjectIdentity = ObjectIdentity
atx90024XS = _Atx90024XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 76)
)
_Atx90024XtN_ObjectIdentity = ObjectIdentity
atx90024XtN = _Atx90024XtN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 77)
)
_Atx60024Ts_ObjectIdentity = ObjectIdentity
atx60024Ts = _Atx60024Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 80)
)
_Atx60024TsXP_ObjectIdentity = ObjectIdentity
atx60024TsXP = _Atx60024TsXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 81)
)
_Atx60048Ts_ObjectIdentity = ObjectIdentity
atx60048Ts = _Atx60048Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 82)
)
_Atx60048TsXP_ObjectIdentity = ObjectIdentity
atx60048TsXP = _Atx60048TsXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 83)
)
_AtRapier24ibNEBS_ObjectIdentity = ObjectIdentity
atRapier24ibNEBS = _AtRapier24ibNEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 84)
)
_AtRapier24ibDcNEBS_ObjectIdentity = ObjectIdentity
atRapier24ibDcNEBS = _AtRapier24ibDcNEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 85)
)
_AtSBx8112_ObjectIdentity = ObjectIdentity
atSBx8112 = _AtSBx8112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 86)
)
_AtSBx81CFC400_ObjectIdentity = ObjectIdentity
atSBx81CFC400 = _AtSBx81CFC400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 87)
)
_AtSBx81CFC960_ObjectIdentity = ObjectIdentity
atSBx81CFC960 = _AtSBx81CFC960_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 88)
)
_AtSBx81CFC960v2_ObjectIdentity = ObjectIdentity
atSBx81CFC960v2 = _AtSBx81CFC960v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 89)
)
_Atx60024TsPoE_ObjectIdentity = ObjectIdentity
atx60024TsPoE = _Atx60024TsPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 91)
)
_Atx60024TsPoEPlus_ObjectIdentity = ObjectIdentity
atx60024TsPoEPlus = _Atx60024TsPoEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 92)
)
_X61048TsXPOEPlus_ObjectIdentity = ObjectIdentity
x61048TsXPOEPlus = _X61048TsXPOEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 93)
)
_X61048TsPOEPlus_ObjectIdentity = ObjectIdentity
x61048TsPOEPlus = _X61048TsPOEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 94)
)
_X61024TsXPOEPlus_ObjectIdentity = ObjectIdentity
x61024TsXPOEPlus = _X61024TsXPOEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 95)
)
_X61024TsPOEPlus_ObjectIdentity = ObjectIdentity
x61024TsPOEPlus = _X61024TsPOEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 96)
)
_X61048TsX_ObjectIdentity = ObjectIdentity
x61048TsX = _X61048TsX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 97)
)
_X61048Ts_ObjectIdentity = ObjectIdentity
x61048Ts = _X61048Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 98)
)
_X61024TsX_ObjectIdentity = ObjectIdentity
x61024TsX = _X61024TsX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 99)
)
_X61024Ts_ObjectIdentity = ObjectIdentity
x61024Ts = _X61024Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 100)
)
_X61024SPX_ObjectIdentity = ObjectIdentity
x61024SPX = _X61024SPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 101)
)
_AtRP48xDC_ObjectIdentity = ObjectIdentity
atRP48xDC = _AtRP48xDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 105)
)
_Atx51028GTX_ObjectIdentity = ObjectIdentity
atx51028GTX = _Atx51028GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 109)
)
_Atx51028GPX_ObjectIdentity = ObjectIdentity
atx51028GPX = _Atx51028GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 110)
)
_Atx51028GSX_ObjectIdentity = ObjectIdentity
atx51028GSX = _Atx51028GSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 111)
)
_Atx51052GTX_ObjectIdentity = ObjectIdentity
atx51052GTX = _Atx51052GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 112)
)
_Atx51052GPX_ObjectIdentity = ObjectIdentity
atx51052GPX = _Atx51052GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 113)
)
_AtSBx8106_ObjectIdentity = ObjectIdentity
atSBx8106 = _AtSBx8106_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 114)
)
_Atx510DP52GTX_ObjectIdentity = ObjectIdentity
atx510DP52GTX = _Atx510DP52GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 116)
)
_AtIX528GPX_ObjectIdentity = ObjectIdentity
atIX528GPX = _AtIX528GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 117)
)
_Atx93028GTX_ObjectIdentity = ObjectIdentity
atx93028GTX = _Atx93028GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 118)
)
_Atx93028GPX_ObjectIdentity = ObjectIdentity
atx93028GPX = _Atx93028GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 119)
)
_Atx93028GSX_ObjectIdentity = ObjectIdentity
atx93028GSX = _Atx93028GSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 120)
)
_Atx93052GTX_ObjectIdentity = ObjectIdentity
atx93052GTX = _Atx93052GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 121)
)
_Atx93052GPX_ObjectIdentity = ObjectIdentity
atx93052GPX = _Atx93052GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 122)
)
_Atdc2552xs_ObjectIdentity = ObjectIdentity
atdc2552xs = _Atdc2552xs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 123)
)
_Atx51028GSXDC_ObjectIdentity = ObjectIdentity
atx51028GSXDC = _Atx51028GSXDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 124)
)
_Atx510DP28GTX_ObjectIdentity = ObjectIdentity
atx510DP28GTX = _Atx510DP28GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 126)
)
_Atx510L28GT_ObjectIdentity = ObjectIdentity
atx510L28GT = _Atx510L28GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 127)
)
_Atx510L52GT_ObjectIdentity = ObjectIdentity
atx510L52GT = _Atx510L52GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 128)
)
_Atx510L28GP_ObjectIdentity = ObjectIdentity
atx510L28GP = _Atx510L28GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 129)
)
_Atx510L52GP_ObjectIdentity = ObjectIdentity
atx510L52GP = _Atx510L52GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 130)
)
_Atx51028GTXR_ObjectIdentity = ObjectIdentity
atx51028GTXR = _Atx51028GTXR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 131)
)
_Atx51052GTXR_ObjectIdentity = ObjectIdentity
atx51052GTXR = _Atx51052GTXR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 132)
)
_AtSH51028GTX_ObjectIdentity = ObjectIdentity
atSH51028GTX = _AtSH51028GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 133)
)
_AtSH51052GTX_ObjectIdentity = ObjectIdentity
atSH51052GTX = _AtSH51052GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 134)
)
_AtSH51028GPX_ObjectIdentity = ObjectIdentity
atSH51028GPX = _AtSH51028GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 135)
)
_AtSH51052GPX_ObjectIdentity = ObjectIdentity
atSH51052GPX = _AtSH51052GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 136)
)
_Atsbx908g2_ObjectIdentity = ObjectIdentity
atsbx908g2 = _Atsbx908g2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 137)
)
_Atsbx908g3_ObjectIdentity = ObjectIdentity
atsbx908g3 = _Atsbx908g3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 138)
)
_Atx55018XTQ_ObjectIdentity = ObjectIdentity
atx55018XTQ = _Atx55018XTQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 139)
)
_Atx55018XSQ_ObjectIdentity = ObjectIdentity
atx55018XSQ = _Atx55018XSQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 140)
)
_Atx55018XSPQm_ObjectIdentity = ObjectIdentity
atx55018XSPQm = _Atx55018XSPQm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 141)
)
_AtSBx81XLEM_ObjectIdentity = ObjectIdentity
atSBx81XLEM = _AtSBx81XLEM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 142)
)
_Atx53028GTXm_ObjectIdentity = ObjectIdentity
atx53028GTXm = _Atx53028GTXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 143)
)
_Atx53028GPXm_ObjectIdentity = ObjectIdentity
atx53028GPXm = _Atx53028GPXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 144)
)
_Atx530DP28GHXm_ObjectIdentity = ObjectIdentity
atx530DP28GHXm = _Atx530DP28GHXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 146)
)
_Atx53052GTXm_ObjectIdentity = ObjectIdentity
atx53052GTXm = _Atx53052GTXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 147)
)
_Atx53052GPXm_ObjectIdentity = ObjectIdentity
atx53052GPXm = _Atx53052GPXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 148)
)
_Atx530DP52GHXm_ObjectIdentity = ObjectIdentity
atx530DP52GHXm = _Atx530DP52GHXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 149)
)
_Atx95028XTQm_ObjectIdentity = ObjectIdentity
atx95028XTQm = _Atx95028XTQm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 150)
)
_Atx95028XSQ_ObjectIdentity = ObjectIdentity
atx95028XSQ = _Atx95028XSQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 151)
)
_Atx32010GH_ObjectIdentity = ObjectIdentity
atx32010GH = _Atx32010GH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 152)
)
_Atx32011GPT_ObjectIdentity = ObjectIdentity
atx32011GPT = _Atx32011GPT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 153)
)
_AtGS980MX28_ObjectIdentity = ObjectIdentity
atGS980MX28 = _AtGS980MX28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 154)
)
_AtGS980MX28PSm_ObjectIdentity = ObjectIdentity
atGS980MX28PSm = _AtGS980MX28PSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 155)
)
_AtGS980MX52_ObjectIdentity = ObjectIdentity
atGS980MX52 = _AtGS980MX52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 156)
)
_AtGS980MX52PSm_ObjectIdentity = ObjectIdentity
atGS980MX52PSm = _AtGS980MX52PSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 157)
)
_Atx530L28GTX_ObjectIdentity = ObjectIdentity
atx530L28GTX = _Atx530L28GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 158)
)
_Atx530L28GPX_ObjectIdentity = ObjectIdentity
atx530L28GPX = _Atx530L28GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 159)
)
_Atx530L52GTX_ObjectIdentity = ObjectIdentity
atx530L52GTX = _Atx530L52GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 160)
)
_Atx530L52GPX_ObjectIdentity = ObjectIdentity
atx530L52GPX = _Atx530L52GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 161)
)
_AtGS980EM10H_ObjectIdentity = ObjectIdentity
atGS980EM10H = _AtGS980EM10H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 162)
)
_AtGS980EM11PT_ObjectIdentity = ObjectIdentity
atGS980EM11PT = _AtGS980EM11PT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 163)
)
_Atx95052XTQm_ObjectIdentity = ObjectIdentity
atx95052XTQm = _Atx95052XTQm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 164)
)
_Atx95052XSQ_ObjectIdentity = ObjectIdentity
atx95052XSQ = _Atx95052XSQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 165)
)
_Atx530L10GHXm_ObjectIdentity = ObjectIdentity
atx530L10GHXm = _Atx530L10GHXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 166)
)
_Atx53010GHXm_ObjectIdentity = ObjectIdentity
atx53010GHXm = _Atx53010GHXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 168)
)
_Atx53018GHXm_ObjectIdentity = ObjectIdentity
atx53018GHXm = _Atx53018GHXm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 169)
)
_AtGS980MX10HSm_ObjectIdentity = ObjectIdentity
atGS980MX10HSm = _AtGS980MX10HSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 170)
)
_AtSBx81CFC960v2a_ObjectIdentity = ObjectIdentity
atSBx81CFC960v2a = _AtSBx81CFC960v2a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 172)
)
_IndustrialSwitch_ObjectIdentity = ObjectIdentity
industrialSwitch = _IndustrialSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24)
)
if mibBuilder.loadTexts:
    industrialSwitch.setStatus("current")
_AtIE2006GT_ObjectIdentity = ObjectIdentity
atIE2006GT = _AtIE2006GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 1)
)
_AtIE2006GP_ObjectIdentity = ObjectIdentity
atIE2006GP = _AtIE2006GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 2)
)
_AtIE2006GPW_ObjectIdentity = ObjectIdentity
atIE2006GPW = _AtIE2006GPW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 3)
)
_AtIE2006FT_ObjectIdentity = ObjectIdentity
atIE2006FT = _AtIE2006FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 6)
)
_AtIE2006FP_ObjectIdentity = ObjectIdentity
atIE2006FP = _AtIE2006FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 7)
)
_AtIE30012GT_ObjectIdentity = ObjectIdentity
atIE30012GT = _AtIE30012GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 8)
)
_AtIE30012GP_ObjectIdentity = ObjectIdentity
atIE30012GP = _AtIE30012GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 9)
)
_AtIE30012GS_ObjectIdentity = ObjectIdentity
atIE30012GS = _AtIE30012GS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 10)
)
_AtIE30020GST_ObjectIdentity = ObjectIdentity
atIE30020GST = _AtIE30020GST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 11)
)
_AtIE51028GSX_ObjectIdentity = ObjectIdentity
atIE51028GSX = _AtIE51028GSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 12)
)
_AtIE34012GP_ObjectIdentity = ObjectIdentity
atIE34012GP = _AtIE34012GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 13)
)
_AtIE340L18GP_ObjectIdentity = ObjectIdentity
atIE340L18GP = _AtIE340L18GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 14)
)
_AtIE34012GT_ObjectIdentity = ObjectIdentity
atIE34012GT = _AtIE34012GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 15)
)
_AtIE34020GP_ObjectIdentity = ObjectIdentity
atIE34020GP = _AtIE34020GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 16)
)
_AtIE21010GP_ObjectIdentity = ObjectIdentity
atIE21010GP = _AtIE21010GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 17)
)
_AtIE21018GP_ObjectIdentity = ObjectIdentity
atIE21018GP = _AtIE21018GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 24, 18)
)
_VirtualApp_ObjectIdentity = ObjectIdentity
virtualApp = _VirtualApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 26)
)
if mibBuilder.loadTexts:
    virtualApp.setStatus("current")
_AtVAA_ObjectIdentity = ObjectIdentity
atVAA = _AtVAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 26, 1)
)
_AtvFW_ObjectIdentity = ObjectIdentity
atvFW = _AtvFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 26, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-PRODUCT-MIB",
    **{"products": products,
       "bridgeRouter": bridgeRouter,
       "centreComAR300Router": centreComAR300Router,
       "centreComAR720Router": centreComAR720Router,
       "centreComAR300LRouter": centreComAR300LRouter,
       "centreComAR310Router": centreComAR310Router,
       "centreComAR300LURouter": centreComAR300LURouter,
       "centreComAR300URouter": centreComAR300URouter,
       "centreComAR310URouter": centreComAR310URouter,
       "centreComAR350Router": centreComAR350Router,
       "centreComAR370Router": centreComAR370Router,
       "centreComAR330Router": centreComAR330Router,
       "centreComAR395Router": centreComAR395Router,
       "centreComAR390Router": centreComAR390Router,
       "centreComAR370URouter": centreComAR370URouter,
       "centreComAR740Router": centreComAR740Router,
       "centreComAR140SRouter": centreComAR140SRouter,
       "centreComAR140URouter": centreComAR140URouter,
       "centreComAR320Router": centreComAR320Router,
       "centreComAR130SRouter": centreComAR130SRouter,
       "centreComAR130URouter": centreComAR130URouter,
       "centreComAR160Router": centreComAR160Router,
       "atAR740RouterDC": atAR740RouterDC,
       "centreComAR120Router": centreComAR120Router,
       "atAR410Router": atAR410Router,
       "atAR725Router": atAR725Router,
       "atAR745Router": atAR745Router,
       "atAR410v2Router": atAR410v2Router,
       "atAR410v3Router": atAR410v3Router,
       "atAR725RouterDC": atAR725RouterDC,
       "atAR745RouterDC": atAR745RouterDC,
       "atAR450Router": atAR450Router,
       "atAR450DualRouter": atAR450DualRouter,
       "atAR440Router": atAR440Router,
       "atAR441Router": atAR441Router,
       "atAR442Router": atAR442Router,
       "atAR443Router": atAR443Router,
       "atAR444Router": atAR444Router,
       "atAR420Router": atAR420Router,
       "atAR415SRouter": atAR415SRouter,
       "atAR415SRouterDC": atAR415SRouterDC,
       "atAR550Router": atAR550Router,
       "atAR551Router": atAR551Router,
       "atAR552Router": atAR552Router,
       "atAR550SRouterDP": atAR550SRouterDP,
       "atAR570Router": atAR570Router,
       "atAR770Router": atAR770Router,
       "atAR750SRouterDP": atAR750SRouterDP,
       "atAR560SRouter": atAR560SRouter,
       "atAR3050SRouter": atAR3050SRouter,
       "atAR4050SRouter": atAR4050SRouter,
       "atAR2050VRouter": atAR2050VRouter,
       "atAR2010VRouter": atAR2010VRouter,
       "atAR1050VRouter": atAR1050VRouter,
       "atAR4050S5GRouter": atAR4050S5GRouter,
       "swhub": swhub,
       "atx200GE52T": atx200GE52T,
       "atx200GE28T": atx200GE28T,
       "atx2109GT": atx2109GT,
       "atx21016GT": atx21016GT,
       "atx21024GT": atx21024GT,
       "atx31026FT": atx31026FT,
       "atx31050FT": atx31050FT,
       "atx31026FP": atx31026FP,
       "atx31050FP": atx31050FP,
       "atx31026GT": atx31026GT,
       "atx31050GT": atx31050GT,
       "atx31026GP": atx31026GP,
       "atx31050GP": atx31050GP,
       "atx23010GT": atx23010GT,
       "atx23018GT": atx23018GT,
       "atx23028GT": atx23028GT,
       "atx23052GT": atx23052GT,
       "atx23010GP": atx23010GP,
       "atx23018GP": atx23018GP,
       "atx23028GP": atx23028GP,
       "atx23052GP": atx23052GP,
       "atx35010GPT": atx35010GPT,
       "atGS924MX": atGS924MX,
       "atGS924MPX": atGS924MPX,
       "atGS948MX": atGS948MX,
       "atGS948MPX": atGS948MPX,
       "atXS916MXT": atXS916MXT,
       "atXS916MXS": atXS916MXS,
       "atXS916MXP": atXS916MXP,
       "atSH23010GP": atSH23010GP,
       "atSH23018GP": atSH23018GP,
       "atSH23028GP": atSH23028GP,
       "atSH2109GT": atSH2109GT,
       "atSH21016GT": atSH21016GT,
       "atSH21024GT": atSH21024GT,
       "atSH31026FT": atSH31026FT,
       "atSH31050FT": atSH31050FT,
       "atSH31026FP": atSH31026FP,
       "atSH31050FP": atSH31050FP,
       "atSH23010GT": atSH23010GT,
       "atSH23018GT": atSH23018GT,
       "atSH23028GT": atSH23028GT,
       "atFS980M9": atFS980M9,
       "atFS980M9PS": atFS980M9PS,
       "atFS980M18": atFS980M18,
       "atFS980M18PS": atFS980M18PS,
       "atFS980M28": atFS980M28,
       "atFS980M28PS": atFS980M28PS,
       "atFS980M52": atFS980M52,
       "atFS980M52PS": atFS980M52PS,
       "atGS910M": atGS910M,
       "atGS910MP": atGS910MP,
       "atGS918M": atGS918M,
       "atGS918MP": atGS918MP,
       "atGS928M": atGS928M,
       "atGS928MP": atGS928MP,
       "atGS952M": atGS952M,
       "atGS952MP": atGS952MP,
       "atx22052GT": atx22052GT,
       "atx22052GP": atx22052GP,
       "atx22028GS": atx22028GS,
       "atGS980M52": atGS980M52,
       "atGS980M52PS": atGS980M52PS,
       "atGS970M28PS": atGS970M28PS,
       "atGS970M18PS": atGS970M18PS,
       "atGS970M10PS": atGS970M10PS,
       "atGS970M28": atGS970M28,
       "atGS970M18": atGS970M18,
       "atGS970M10": atGS970M10,
       "atx230L17GT": atx230L17GT,
       "atx230L26GT": atx230L26GT,
       "atFS980M28DP": atFS980M28DP,
       "routerSwitch": routerSwitch,
       "atRapier24": atRapier24,
       "atRapier16fSC": atRapier16fSC,
       "atRapier16fVF": atRapier16fVF,
       "atRapier16fMT": atRapier16fMT,
       "atRapier48": atRapier48,
       "atRapier8t8fSC": atRapier8t8fSC,
       "atRapier8t8fSCi": atRapier8t8fSCi,
       "atRapier8t8fMT": atRapier8t8fMT,
       "atRapier8t8fMTi": atRapier8t8fMTi,
       "atRapier8fSC": atRapier8fSC,
       "atRapier8fSCi": atRapier8fSCi,
       "atRapier8fMT": atRapier8fMT,
       "atRapier8fMTi": atRapier8fMTi,
       "atRapier16fMTi": atRapier16fMTi,
       "atRapierG6": atRapierG6,
       "atRapierG6SX": atRapierG6SX,
       "atRapierG6LX": atRapierG6LX,
       "atRapierG6MT": atRapierG6MT,
       "atRapier16fSCi": atRapier16fSCi,
       "atRapier24i": atRapier24i,
       "atRapier48i": atRapier48i,
       "atSwitchblade4AC": atSwitchblade4AC,
       "atSwitchblade4DC": atSwitchblade4DC,
       "atSwitchblade8AC": atSwitchblade8AC,
       "atSwitchblade8DC": atSwitchblade8DC,
       "at9816GF": at9816GF,
       "at9812TF": at9812TF,
       "at9816GB": at9816GB,
       "at9812T": at9812T,
       "at8724XL": at8724XL,
       "at8748XL": at8748XL,
       "at8724XLDC": at8724XLDC,
       "at8748XLDC": at8748XLDC,
       "at9816GbDC": at9816GbDC,
       "at9812tDC": at9812tDC,
       "at8824": at8824,
       "at8848": at8848,
       "at8824DC": at8824DC,
       "at8848DC": at8848DC,
       "at8624XL80": at8624XL80,
       "at8724XL80": at8724XL80,
       "at8748XL80": at8748XL80,
       "at8948EX": at8948EX,
       "at8948i": at8948i,
       "at8624T2M": at8624T2M,
       "atRapier24iDcNEBS": atRapier24iDcNEBS,
       "at8724XLDcNEBS": at8724XLDcNEBS,
       "at9924T": at9924T,
       "at9924SP": at9924SP,
       "at9924T4SP": at9924T4SP,
       "at9924TEMC": at9924TEMC,
       "at8724MLB": at8724MLB,
       "at8624POE": at8624POE,
       "at9924Ts": at9924Ts,
       "at86482SP": at86482SP,
       "at9924Ti": at9924Ti,
       "at9924SPi": at9924SPi,
       "at9924Tsi": at9924Tsi,
       "at9924SPsi": at9924SPsi,
       "at8948iN": at8948iN,
       "at9924TsiN": at9924TsiN,
       "atRapier48w": atRapier48w,
       "at8724SlV2": at8724SlV2,
       "x90048FS": x90048FS,
       "atSwitchBladex908": atSwitchBladex908,
       "atx90012XTS": atx90012XTS,
       "atRapier48wb": atRapier48wb,
       "atRapier48wAC": atRapier48wAC,
       "atRapier48wbAC": atRapier48wbAC,
       "atx90024XT": atx90024XT,
       "atx90024XS": atx90024XS,
       "atx90024XtN": atx90024XtN,
       "atx60024Ts": atx60024Ts,
       "atx60024TsXP": atx60024TsXP,
       "atx60048Ts": atx60048Ts,
       "atx60048TsXP": atx60048TsXP,
       "atRapier24ibNEBS": atRapier24ibNEBS,
       "atRapier24ibDcNEBS": atRapier24ibDcNEBS,
       "atSBx8112": atSBx8112,
       "atSBx81CFC400": atSBx81CFC400,
       "atSBx81CFC960": atSBx81CFC960,
       "atSBx81CFC960v2": atSBx81CFC960v2,
       "atx60024TsPoE": atx60024TsPoE,
       "atx60024TsPoEPlus": atx60024TsPoEPlus,
       "x61048TsXPOEPlus": x61048TsXPOEPlus,
       "x61048TsPOEPlus": x61048TsPOEPlus,
       "x61024TsXPOEPlus": x61024TsXPOEPlus,
       "x61024TsPOEPlus": x61024TsPOEPlus,
       "x61048TsX": x61048TsX,
       "x61048Ts": x61048Ts,
       "x61024TsX": x61024TsX,
       "x61024Ts": x61024Ts,
       "x61024SPX": x61024SPX,
       "atRP48xDC": atRP48xDC,
       "atx51028GTX": atx51028GTX,
       "atx51028GPX": atx51028GPX,
       "atx51028GSX": atx51028GSX,
       "atx51052GTX": atx51052GTX,
       "atx51052GPX": atx51052GPX,
       "atSBx8106": atSBx8106,
       "atx510DP52GTX": atx510DP52GTX,
       "atIX528GPX": atIX528GPX,
       "atx93028GTX": atx93028GTX,
       "atx93028GPX": atx93028GPX,
       "atx93028GSX": atx93028GSX,
       "atx93052GTX": atx93052GTX,
       "atx93052GPX": atx93052GPX,
       "atdc2552xs": atdc2552xs,
       "atx51028GSXDC": atx51028GSXDC,
       "atx510DP28GTX": atx510DP28GTX,
       "atx510L28GT": atx510L28GT,
       "atx510L52GT": atx510L52GT,
       "atx510L28GP": atx510L28GP,
       "atx510L52GP": atx510L52GP,
       "atx51028GTXR": atx51028GTXR,
       "atx51052GTXR": atx51052GTXR,
       "atSH51028GTX": atSH51028GTX,
       "atSH51052GTX": atSH51052GTX,
       "atSH51028GPX": atSH51028GPX,
       "atSH51052GPX": atSH51052GPX,
       "atsbx908g2": atsbx908g2,
       "atsbx908g3": atsbx908g3,
       "atx55018XTQ": atx55018XTQ,
       "atx55018XSQ": atx55018XSQ,
       "atx55018XSPQm": atx55018XSPQm,
       "atSBx81XLEM": atSBx81XLEM,
       "atx53028GTXm": atx53028GTXm,
       "atx53028GPXm": atx53028GPXm,
       "atx530DP28GHXm": atx530DP28GHXm,
       "atx53052GTXm": atx53052GTXm,
       "atx53052GPXm": atx53052GPXm,
       "atx530DP52GHXm": atx530DP52GHXm,
       "atx95028XTQm": atx95028XTQm,
       "atx95028XSQ": atx95028XSQ,
       "atx32010GH": atx32010GH,
       "atx32011GPT": atx32011GPT,
       "atGS980MX28": atGS980MX28,
       "atGS980MX28PSm": atGS980MX28PSm,
       "atGS980MX52": atGS980MX52,
       "atGS980MX52PSm": atGS980MX52PSm,
       "atx530L28GTX": atx530L28GTX,
       "atx530L28GPX": atx530L28GPX,
       "atx530L52GTX": atx530L52GTX,
       "atx530L52GPX": atx530L52GPX,
       "atGS980EM10H": atGS980EM10H,
       "atGS980EM11PT": atGS980EM11PT,
       "atx95052XTQm": atx95052XTQm,
       "atx95052XSQ": atx95052XSQ,
       "atx530L10GHXm": atx530L10GHXm,
       "atx53010GHXm": atx53010GHXm,
       "atx53018GHXm": atx53018GHXm,
       "atGS980MX10HSm": atGS980MX10HSm,
       "atSBx81CFC960v2a": atSBx81CFC960v2a,
       "industrialSwitch": industrialSwitch,
       "atIE2006GT": atIE2006GT,
       "atIE2006GP": atIE2006GP,
       "atIE2006GPW": atIE2006GPW,
       "atIE2006FT": atIE2006FT,
       "atIE2006FP": atIE2006FP,
       "atIE30012GT": atIE30012GT,
       "atIE30012GP": atIE30012GP,
       "atIE30012GS": atIE30012GS,
       "atIE30020GST": atIE30020GST,
       "atIE51028GSX": atIE51028GSX,
       "atIE34012GP": atIE34012GP,
       "atIE340L18GP": atIE340L18GP,
       "atIE34012GT": atIE34012GT,
       "atIE34020GP": atIE34020GP,
       "atIE21010GP": atIE21010GP,
       "atIE21018GP": atIE21018GP,
       "virtualApp": virtualApp,
       "atVAA": atVAA,
       "atvFW": atvFW}
)
