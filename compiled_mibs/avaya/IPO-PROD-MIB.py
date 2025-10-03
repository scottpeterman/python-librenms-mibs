# SNMP MIB module (IPO-PROD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\avaya\IPO-PROD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:07 2025
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

(products,) = mibBuilder.importSymbols(
    "AVAYAGEN-MIB",
    "products")

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

ipoProdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2)
)
if mibBuilder.loadTexts:
    ipoProdMIB.setRevisions(
        ("2014-08-06 00:00",
         "2014-05-30 00:00",
         "2014-02-27 00:00",
         "2013-12-10 00:00",
         "2012-07-23 00:00",
         "2012-03-26 00:00",
         "2011-11-14 11:28",
         "2011-08-11 16:58",
         "2011-02-10 14:57",
         "2011-02-01 14:57",
         "2011-01-11 16:30",
         "2010-06-09 15:15",
         "2010-04-28 16:26",
         "2009-08-26 17:13",
         "2009-08-05 10:48",
         "2006-08-16 11:00",
         "2006-08-02 17:52",
         "2006-07-13 22:20",
         "2006-06-10 14:16",
         "2006-06-07 10:14",
         "2006-05-24 16:20",
         "2006-05-24 16:15",
         "2006-04-04 00:00",
         "2004-08-06 00:00",
         "2004-03-03 00:00",
         "2004-01-06 00:00",
         "2003-10-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpoProdControllers_ObjectIdentity = ObjectIdentity
ipoProdControllers = _IpoProdControllers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1)
)
_IpoProd401Family_ObjectIdentity = ObjectIdentity
ipoProd401Family = _IpoProd401Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 1)
)
_IpoProd401DT2_ObjectIdentity = ObjectIdentity
ipoProd401DT2 = _IpoProd401DT2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipoProd401DT2.setStatus("current")
_IpoProd401DT4_ObjectIdentity = ObjectIdentity
ipoProd401DT4 = _IpoProd401DT4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipoProd401DT4.setStatus("current")
_IpoProd401DS2_ObjectIdentity = ObjectIdentity
ipoProd401DS2 = _IpoProd401DS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipoProd401DS2.setStatus("current")
_IpoProd401DS4_ObjectIdentity = ObjectIdentity
ipoProd401DS4 = _IpoProd401DS4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ipoProd401DS4.setStatus("current")
_IpoProd403Family_ObjectIdentity = ObjectIdentity
ipoProd403Family = _IpoProd403Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 2)
)
_IpoProd403DT_ObjectIdentity = ObjectIdentity
ipoProd403DT = _IpoProd403DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipoProd403DT.setStatus("current")
_IpoProd403DS_ObjectIdentity = ObjectIdentity
ipoProd403DS = _IpoProd403DS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ipoProd403DS.setStatus("current")
_IpoProd406Family_ObjectIdentity = ObjectIdentity
ipoProd406Family = _IpoProd406Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 3)
)
_IpoProd406_ObjectIdentity = ObjectIdentity
ipoProd406 = _IpoProd406_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ipoProd406.setStatus("current")
_IpoProd412Family_ObjectIdentity = ObjectIdentity
ipoProd412Family = _IpoProd412Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 4)
)
_IpoProd412_ObjectIdentity = ObjectIdentity
ipoProd412 = _IpoProd412_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipoProd412.setStatus("current")
_IpoProdSmallOfficeEditionFamily_ObjectIdentity = ObjectIdentity
ipoProdSmallOfficeEditionFamily = _IpoProdSmallOfficeEditionFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 5)
)
_IpoProdSmallOfficeEditionPOTS4_ObjectIdentity = ObjectIdentity
ipoProdSmallOfficeEditionPOTS4 = _IpoProdSmallOfficeEditionPOTS4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ipoProdSmallOfficeEditionPOTS4.setStatus("current")
_IpoProdSmallOfficeEditionPOTS8_ObjectIdentity = ObjectIdentity
ipoProdSmallOfficeEditionPOTS8 = _IpoProdSmallOfficeEditionPOTS8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ipoProdSmallOfficeEditionPOTS8.setStatus("current")
_IpoProdSmallOfficeEditionDT8_ObjectIdentity = ObjectIdentity
ipoProdSmallOfficeEditionDT8 = _IpoProdSmallOfficeEditionDT8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ipoProdSmallOfficeEditionDT8.setStatus("current")
_IpoProdSmallOfficeEditionDS8_ObjectIdentity = ObjectIdentity
ipoProdSmallOfficeEditionDS8 = _IpoProdSmallOfficeEditionDS8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    ipoProdSmallOfficeEditionDS8.setStatus("current")
_IpoProdR403Family_ObjectIdentity = ObjectIdentity
ipoProdR403Family = _IpoProdR403Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 6)
)
_IpoProdR403DT_ObjectIdentity = ObjectIdentity
ipoProdR403DT = _IpoProdR403DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ipoProdR403DT.setStatus("current")
_IpoProdR403DS_ObjectIdentity = ObjectIdentity
ipoProdR403DS = _IpoProdR403DS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ipoProdR403DS.setStatus("current")
_IpoProdR406Family_ObjectIdentity = ObjectIdentity
ipoProdR406Family = _IpoProdR406Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 7)
)
_IpoProdR406_ObjectIdentity = ObjectIdentity
ipoProdR406 = _IpoProdR406_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ipoProdR406.setStatus("current")
_IpoProdR406DT_ObjectIdentity = ObjectIdentity
ipoProdR406DT = _IpoProdR406DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ipoProdR406DT.setStatus("current")
_IpoProdR406DS_ObjectIdentity = ObjectIdentity
ipoProdR406DS = _IpoProdR406DS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    ipoProdR406DS.setStatus("current")
_IpoProdR406Full_ObjectIdentity = ObjectIdentity
ipoProdR406Full = _IpoProdR406Full_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 7, 4)
)
if mibBuilder.loadTexts:
    ipoProdR406Full.setStatus("current")
_IpoProdSogFamily_ObjectIdentity = ObjectIdentity
ipoProdSogFamily = _IpoProdSogFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 8)
)
_IpoProdSogSOEPOTS4_ObjectIdentity = ObjectIdentity
ipoProdSogSOEPOTS4 = _IpoProdSogSOEPOTS4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ipoProdSogSOEPOTS4.setStatus("current")
_IpoProdSogSOEPOTS8_ObjectIdentity = ObjectIdentity
ipoProdSogSOEPOTS8 = _IpoProdSogSOEPOTS8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ipoProdSogSOEPOTS8.setStatus("current")
_IpoProdSogSOEDT8_ObjectIdentity = ObjectIdentity
ipoProdSogSOEDT8 = _IpoProdSogSOEDT8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 8, 3)
)
if mibBuilder.loadTexts:
    ipoProdSogSOEDT8.setStatus("current")
_IpoProdSogSOEDS8_ObjectIdentity = ObjectIdentity
ipoProdSogSOEDS8 = _IpoProdSogSOEDS8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 8, 4)
)
if mibBuilder.loadTexts:
    ipoProdSogSOEDS8.setStatus("current")
_IpoProd500Family_ObjectIdentity = ObjectIdentity
ipoProd500Family = _IpoProd500Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 9)
)
_IpoProd500Slot4_ObjectIdentity = ObjectIdentity
ipoProd500Slot4 = _IpoProd500Slot4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    ipoProd500Slot4.setStatus("current")
_IpoProd500Slot8_ObjectIdentity = ObjectIdentity
ipoProd500Slot8 = _IpoProd500Slot8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    ipoProd500Slot8.setStatus("current")
_IpoProd500v2Family_ObjectIdentity = ObjectIdentity
ipoProd500v2Family = _IpoProd500v2Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10)
)
_IpoProd500v2IPOffice_ObjectIdentity = ObjectIdentity
ipoProd500v2IPOffice = _IpoProd500v2IPOffice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    ipoProd500v2IPOffice.setStatus("current")
_IpoProd500v2Partner_ObjectIdentity = ObjectIdentity
ipoProd500v2Partner = _IpoProd500v2Partner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    ipoProd500v2Partner.setStatus("current")
_IpoProd500v2Norstar_ObjectIdentity = ObjectIdentity
ipoProd500v2Norstar = _IpoProd500v2Norstar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 3)
)
if mibBuilder.loadTexts:
    ipoProd500v2Norstar.setStatus("current")
_IpoProd500v2Branch_ObjectIdentity = ObjectIdentity
ipoProd500v2Branch = _IpoProd500v2Branch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 4)
)
if mibBuilder.loadTexts:
    ipoProd500v2Branch.setStatus("current")
_IpoProd500v2Quick_ObjectIdentity = ObjectIdentity
ipoProd500v2Quick = _IpoProd500v2Quick_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 5)
)
if mibBuilder.loadTexts:
    ipoProd500v2Quick.setStatus("current")
_IpoProd500v2SEditionExpansion_ObjectIdentity = ObjectIdentity
ipoProd500v2SEditionExpansion = _IpoProd500v2SEditionExpansion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 6)
)
if mibBuilder.loadTexts:
    ipoProd500v2SEditionExpansion.setStatus("current")
_IpoProd500v2IPOfficeSelect_ObjectIdentity = ObjectIdentity
ipoProd500v2IPOfficeSelect = _IpoProd500v2IPOfficeSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 7)
)
if mibBuilder.loadTexts:
    ipoProd500v2IPOfficeSelect.setStatus("current")
_IpoProd500v2SEditionExpansionSelect_ObjectIdentity = ObjectIdentity
ipoProd500v2SEditionExpansionSelect = _IpoProd500v2SEditionExpansionSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 1, 10, 8)
)
if mibBuilder.loadTexts:
    ipoProd500v2SEditionExpansionSelect.setStatus("current")
_IpoProdExpModules_ObjectIdentity = ObjectIdentity
ipoProdExpModules = _IpoProdExpModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2)
)
_IpoProdExpModDT_ObjectIdentity = ObjectIdentity
ipoProdExpModDT = _IpoProdExpModDT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 1)
)
_IpoProdExpModDT16_ObjectIdentity = ObjectIdentity
ipoProdExpModDT16 = _IpoProdExpModDT16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipoProdExpModDT16.setStatus("current")
_IpoProdExpModDT30_ObjectIdentity = ObjectIdentity
ipoProdExpModDT30 = _IpoProdExpModDT30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ipoProdExpModDT30.setStatus("current")
_IpoProdExpModDS_ObjectIdentity = ObjectIdentity
ipoProdExpModDS = _IpoProdExpModDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 2)
)
_IpoProdExpModDS16_ObjectIdentity = ObjectIdentity
ipoProdExpModDS16 = _IpoProdExpModDS16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ipoProdExpModDS16.setStatus("current")
_IpoProdExpModDS30_ObjectIdentity = ObjectIdentity
ipoProdExpModDS30 = _IpoProdExpModDS30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ipoProdExpModDS30.setStatus("current")
_IpoProdExpModPhone_ObjectIdentity = ObjectIdentity
ipoProdExpModPhone = _IpoProdExpModPhone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 3)
)
_IpoProdExpModPhone8_ObjectIdentity = ObjectIdentity
ipoProdExpModPhone8 = _IpoProdExpModPhone8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ipoProdExpModPhone8.setStatus("current")
_IpoProdExpModPhone16_ObjectIdentity = ObjectIdentity
ipoProdExpModPhone16 = _IpoProdExpModPhone16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    ipoProdExpModPhone16.setStatus("current")
_IpoProdExpModPhone30_ObjectIdentity = ObjectIdentity
ipoProdExpModPhone30 = _IpoProdExpModPhone30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    ipoProdExpModPhone30.setStatus("current")
_IpoProdExpModS0_ObjectIdentity = ObjectIdentity
ipoProdExpModS0 = _IpoProdExpModS0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 4)
)
_IpoProdExpModS08_ObjectIdentity = ObjectIdentity
ipoProdExpModS08 = _IpoProdExpModS08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ipoProdExpModS08.setStatus("current")
_IpoProdExpModS016_ObjectIdentity = ObjectIdentity
ipoProdExpModS016 = _IpoProdExpModS016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    ipoProdExpModS016.setStatus("current")
_IpoProdExpModAnalog_ObjectIdentity = ObjectIdentity
ipoProdExpModAnalog = _IpoProdExpModAnalog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 5)
)
_IpoProdExpModATM8_ObjectIdentity = ObjectIdentity
ipoProdExpModATM8 = _IpoProdExpModATM8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ipoProdExpModATM8.setStatus("current")
_IpoProdExpModATM16_ObjectIdentity = ObjectIdentity
ipoProdExpModATM16 = _IpoProdExpModATM16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    ipoProdExpModATM16.setStatus("current")
_IpoProdExpModWAN_ObjectIdentity = ObjectIdentity
ipoProdExpModWAN = _IpoProdExpModWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 6)
)
_IpoProdExpModWAN3_ObjectIdentity = ObjectIdentity
ipoProdExpModWAN3 = _IpoProdExpModWAN3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ipoProdExpModWAN3.setStatus("current")
_IpoProdExpModRDS_ObjectIdentity = ObjectIdentity
ipoProdExpModRDS = _IpoProdExpModRDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 7)
)
_IpoProdExpModRDS16_ObjectIdentity = ObjectIdentity
ipoProdExpModRDS16 = _IpoProdExpModRDS16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    ipoProdExpModRDS16.setStatus("current")
_IpoProdExpModRDS30_ObjectIdentity = ObjectIdentity
ipoProdExpModRDS30 = _IpoProdExpModRDS30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 7, 2)
)
if mibBuilder.loadTexts:
    ipoProdExpModRDS30.setStatus("current")
_IpoProdExpModRPhone_ObjectIdentity = ObjectIdentity
ipoProdExpModRPhone = _IpoProdExpModRPhone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 8)
)
_IpoProdExpModRPhone8_ObjectIdentity = ObjectIdentity
ipoProdExpModRPhone8 = _IpoProdExpModRPhone8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 8, 1)
)
if mibBuilder.loadTexts:
    ipoProdExpModRPhone8.setStatus("current")
_IpoProdExpModRPhone16_ObjectIdentity = ObjectIdentity
ipoProdExpModRPhone16 = _IpoProdExpModRPhone16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 8, 2)
)
if mibBuilder.loadTexts:
    ipoProdExpModRPhone16.setStatus("current")
_IpoProdExpModRPhone30_ObjectIdentity = ObjectIdentity
ipoProdExpModRPhone30 = _IpoProdExpModRPhone30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 8, 3)
)
if mibBuilder.loadTexts:
    ipoProdExpModRPhone30.setStatus("current")
_IpoProdExpModDSA_ObjectIdentity = ObjectIdentity
ipoProdExpModDSA = _IpoProdExpModDSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 9)
)
_IpoProdExpModDSA16RJ21_ObjectIdentity = ObjectIdentity
ipoProdExpModDSA16RJ21 = _IpoProdExpModDSA16RJ21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 9, 1)
)
if mibBuilder.loadTexts:
    ipoProdExpModDSA16RJ21.setStatus("current")
_IpoProdExpModDSA30RJ21_ObjectIdentity = ObjectIdentity
ipoProdExpModDSA30RJ21 = _IpoProdExpModDSA30RJ21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 9, 2)
)
if mibBuilder.loadTexts:
    ipoProdExpModDSA30RJ21.setStatus("current")
_IpoProdExpModDSA16RJ45_ObjectIdentity = ObjectIdentity
ipoProdExpModDSA16RJ45 = _IpoProdExpModDSA16RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 9, 3)
)
if mibBuilder.loadTexts:
    ipoProdExpModDSA16RJ45.setStatus("current")
_IpoProdExpModDSA30RJ45_ObjectIdentity = ObjectIdentity
ipoProdExpModDSA30RJ45 = _IpoProdExpModDSA30RJ45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 2, 9, 4)
)
if mibBuilder.loadTexts:
    ipoProdExpModDSA30RJ45.setStatus("current")
_IpoProdSlots_ObjectIdentity = ObjectIdentity
ipoProdSlots = _IpoProdSlots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 3)
)
_IpoProdSlotVCM_ObjectIdentity = ObjectIdentity
ipoProdSlotVCM = _IpoProdSlotVCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ipoProdSlotVCM.setStatus("current")
_IpoProdSlotModems_ObjectIdentity = ObjectIdentity
ipoProdSlotModems = _IpoProdSlotModems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    ipoProdSlotModems.setStatus("current")
_IpoProdSlotVmailMemory_ObjectIdentity = ObjectIdentity
ipoProdSlotVmailMemory = _IpoProdSlotVmailMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    ipoProdSlotVmailMemory.setStatus("current")
_IpoProdSlotWAN_ObjectIdentity = ObjectIdentity
ipoProdSlotWAN = _IpoProdSlotWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    ipoProdSlotWAN.setStatus("current")
_IpoProdSlotPCCard_ObjectIdentity = ObjectIdentity
ipoProdSlotPCCard = _IpoProdSlotPCCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    ipoProdSlotPCCard.setStatus("current")
_IpoProdSlotTrunks_ObjectIdentity = ObjectIdentity
ipoProdSlotTrunks = _IpoProdSlotTrunks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    ipoProdSlotTrunks.setStatus("current")
_IpoProdSlotExpansion_ObjectIdentity = ObjectIdentity
ipoProdSlotExpansion = _IpoProdSlotExpansion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 7)
)
if mibBuilder.loadTexts:
    ipoProdSlotExpansion.setStatus("current")
_IpoProdSlot500Generic_ObjectIdentity = ObjectIdentity
ipoProdSlot500Generic = _IpoProdSlot500Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 8)
)
if mibBuilder.loadTexts:
    ipoProdSlot500Generic.setStatus("current")
_IpoProdSlotMezzanine_ObjectIdentity = ObjectIdentity
ipoProdSlotMezzanine = _IpoProdSlotMezzanine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 9)
)
if mibBuilder.loadTexts:
    ipoProdSlotMezzanine.setStatus("current")
_IpoProdSlotCarrierVCM_ObjectIdentity = ObjectIdentity
ipoProdSlotCarrierVCM = _IpoProdSlotCarrierVCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 10)
)
if mibBuilder.loadTexts:
    ipoProdSlotCarrierVCM.setStatus("current")
_IpoProdSlotCarrierTrunk_ObjectIdentity = ObjectIdentity
ipoProdSlotCarrierTrunk = _IpoProdSlotCarrierTrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 3, 11)
)
if mibBuilder.loadTexts:
    ipoProdSlotCarrierTrunk.setStatus("current")
_IpoProdSlotModules_ObjectIdentity = ObjectIdentity
ipoProdSlotModules = _IpoProdSlotModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4)
)
_IpoProdIntegralModules_ObjectIdentity = ObjectIdentity
ipoProdIntegralModules = _IpoProdIntegralModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1)
)
_IpoProdIntModVCM_ObjectIdentity = ObjectIdentity
ipoProdIntModVCM = _IpoProdIntModVCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1)
)
_IpoProdIntModVCM3_ObjectIdentity = ObjectIdentity
ipoProdIntModVCM3 = _IpoProdIntModVCM3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipoProdIntModVCM3.setStatus("current")
_IpoProdIntModVCM5_ObjectIdentity = ObjectIdentity
ipoProdIntModVCM5 = _IpoProdIntModVCM5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipoProdIntModVCM5.setStatus("current")
_IpoProdIntModVCM6_ObjectIdentity = ObjectIdentity
ipoProdIntModVCM6 = _IpoProdIntModVCM6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipoProdIntModVCM6.setStatus("current")
_IpoProdIntModVCM8_ObjectIdentity = ObjectIdentity
ipoProdIntModVCM8 = _IpoProdIntModVCM8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ipoProdIntModVCM8.setStatus("current")
_IpoProdIntModVCM10_ObjectIdentity = ObjectIdentity
ipoProdIntModVCM10 = _IpoProdIntModVCM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ipoProdIntModVCM10.setStatus("current")
_IpoProdIntModVCM12_ObjectIdentity = ObjectIdentity
ipoProdIntModVCM12 = _IpoProdIntModVCM12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ipoProdIntModVCM12.setStatus("current")
_IpoProdIntModVCM16_ObjectIdentity = ObjectIdentity
ipoProdIntModVCM16 = _IpoProdIntModVCM16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ipoProdIntModVCM16.setStatus("current")
_IpoProdIntModVCM20_ObjectIdentity = ObjectIdentity
ipoProdIntModVCM20 = _IpoProdIntModVCM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ipoProdIntModVCM20.setStatus("current")
_IpoProdIntModVCM30_ObjectIdentity = ObjectIdentity
ipoProdIntModVCM30 = _IpoProdIntModVCM30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    ipoProdIntModVCM30.setStatus("current")
_IpoProdIntModVCM24_ObjectIdentity = ObjectIdentity
ipoProdIntModVCM24 = _IpoProdIntModVCM24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 10)
)
if mibBuilder.loadTexts:
    ipoProdIntModVCM24.setStatus("current")
_IpoProdIntModVCM4_ObjectIdentity = ObjectIdentity
ipoProdIntModVCM4 = _IpoProdIntModVCM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 1, 11)
)
if mibBuilder.loadTexts:
    ipoProdIntModVCM4.setStatus("current")
_IpoProdIntModModem_ObjectIdentity = ObjectIdentity
ipoProdIntModModem = _IpoProdIntModModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 2)
)
_IpoProdIntModModemDual_ObjectIdentity = ObjectIdentity
ipoProdIntModModemDual = _IpoProdIntModModemDual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipoProdIntModModemDual.setStatus("current")
_IpoProdIntModModemMulti_ObjectIdentity = ObjectIdentity
ipoProdIntModModemMulti = _IpoProdIntModModemMulti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ipoProdIntModModemMulti.setStatus("current")
_IpoProdIntModWAN_ObjectIdentity = ObjectIdentity
ipoProdIntModWAN = _IpoProdIntModWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 3)
)
_IpoProdIntModWANModule_ObjectIdentity = ObjectIdentity
ipoProdIntModWANModule = _IpoProdIntModWANModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ipoProdIntModWANModule.setStatus("current")
_IpoProdIntModMem_ObjectIdentity = ObjectIdentity
ipoProdIntModMem = _IpoProdIntModMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 4)
)
_IpoProdIntModMemVmail_ObjectIdentity = ObjectIdentity
ipoProdIntModMemVmail = _IpoProdIntModMemVmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipoProdIntModMemVmail.setStatus("current")
_IpoProdTrunkModules_ObjectIdentity = ObjectIdentity
ipoProdTrunkModules = _IpoProdTrunkModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2)
)
_IpoProdTrunkAnalogQuad_ObjectIdentity = ObjectIdentity
ipoProdTrunkAnalogQuad = _IpoProdTrunkAnalogQuad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ipoProdTrunkAnalogQuad.setStatus("current")
_IpoProdTrunkBRIQuad_ObjectIdentity = ObjectIdentity
ipoProdTrunkBRIQuad = _IpoProdTrunkBRIQuad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    ipoProdTrunkBRIQuad.setStatus("current")
_IpoProdTrunkE1PRISingle_ObjectIdentity = ObjectIdentity
ipoProdTrunkE1PRISingle = _IpoProdTrunkE1PRISingle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 3)
)
if mibBuilder.loadTexts:
    ipoProdTrunkE1PRISingle.setStatus("current")
_IpoProdTrunkE1PRIDual_ObjectIdentity = ObjectIdentity
ipoProdTrunkE1PRIDual = _IpoProdTrunkE1PRIDual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    ipoProdTrunkE1PRIDual.setStatus("current")
_IpoProdTrunkJ1PRISingle_ObjectIdentity = ObjectIdentity
ipoProdTrunkJ1PRISingle = _IpoProdTrunkJ1PRISingle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 5)
)
if mibBuilder.loadTexts:
    ipoProdTrunkJ1PRISingle.setStatus("current")
_IpoProdTrunkJ1PRIDual_ObjectIdentity = ObjectIdentity
ipoProdTrunkJ1PRIDual = _IpoProdTrunkJ1PRIDual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 6)
)
if mibBuilder.loadTexts:
    ipoProdTrunkJ1PRIDual.setStatus("current")
_IpoProdTrunkT1PRISingle_ObjectIdentity = ObjectIdentity
ipoProdTrunkT1PRISingle = _IpoProdTrunkT1PRISingle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 7)
)
if mibBuilder.loadTexts:
    ipoProdTrunkT1PRISingle.setStatus("current")
_IpoProdTrunkT1PRIDual_ObjectIdentity = ObjectIdentity
ipoProdTrunkT1PRIDual = _IpoProdTrunkT1PRIDual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 8)
)
if mibBuilder.loadTexts:
    ipoProdTrunkT1PRIDual.setStatus("current")
_IpoProdTrunkIndex_ObjectIdentity = ObjectIdentity
ipoProdTrunkIndex = _IpoProdTrunkIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 9)
)
if mibBuilder.loadTexts:
    ipoProdTrunkIndex.setStatus("current")
_IpoProdTrunkR2Single_ObjectIdentity = ObjectIdentity
ipoProdTrunkR2Single = _IpoProdTrunkR2Single_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 10)
)
if mibBuilder.loadTexts:
    ipoProdTrunkR2Single.setStatus("current")
_IpoProdTrunkR2Dual_ObjectIdentity = ObjectIdentity
ipoProdTrunkR2Dual = _IpoProdTrunkR2Dual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 11)
)
if mibBuilder.loadTexts:
    ipoProdTrunkR2Dual.setStatus("current")
_IpoProdTrunkR2CoAxSingle_ObjectIdentity = ObjectIdentity
ipoProdTrunkR2CoAxSingle = _IpoProdTrunkR2CoAxSingle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 12)
)
if mibBuilder.loadTexts:
    ipoProdTrunkR2CoAxSingle.setStatus("current")
_IpoProdTrunkR2CoAxDual_ObjectIdentity = ObjectIdentity
ipoProdTrunkR2CoAxDual = _IpoProdTrunkR2CoAxDual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 13)
)
if mibBuilder.loadTexts:
    ipoProdTrunkR2CoAxDual.setStatus("current")
_IpoProdTrunkRAnalogQuad_ObjectIdentity = ObjectIdentity
ipoProdTrunkRAnalogQuad = _IpoProdTrunkRAnalogQuad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 14)
)
if mibBuilder.loadTexts:
    ipoProdTrunkRAnalogQuad.setStatus("current")
_IpoProdTrunk500AnalogQuad_ObjectIdentity = ObjectIdentity
ipoProdTrunk500AnalogQuad = _IpoProdTrunk500AnalogQuad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 15)
)
if mibBuilder.loadTexts:
    ipoProdTrunk500AnalogQuad.setStatus("current")
_IpoProdTrunk500BRIDual_ObjectIdentity = ObjectIdentity
ipoProdTrunk500BRIDual = _IpoProdTrunk500BRIDual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 16)
)
if mibBuilder.loadTexts:
    ipoProdTrunk500BRIDual.setStatus("current")
_IpoProdTrunk500BRIQuad_ObjectIdentity = ObjectIdentity
ipoProdTrunk500BRIQuad = _IpoProdTrunk500BRIQuad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 17)
)
if mibBuilder.loadTexts:
    ipoProdTrunk500BRIQuad.setStatus("current")
_IpoProdTrunkUniversalPRIDS0Single_ObjectIdentity = ObjectIdentity
ipoProdTrunkUniversalPRIDS0Single = _IpoProdTrunkUniversalPRIDS0Single_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 18)
)
if mibBuilder.loadTexts:
    ipoProdTrunkUniversalPRIDS0Single.setStatus("current")
_IpoProdTrunkUniversalPRIDS0Dual_ObjectIdentity = ObjectIdentity
ipoProdTrunkUniversalPRIDS0Dual = _IpoProdTrunkUniversalPRIDS0Dual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 19)
)
if mibBuilder.loadTexts:
    ipoProdTrunkUniversalPRIDS0Dual.setStatus("current")
_IpoProdTrunk500AnalogQuadV2_ObjectIdentity = ObjectIdentity
ipoProdTrunk500AnalogQuadV2 = _IpoProdTrunk500AnalogQuadV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 2, 20)
)
if mibBuilder.loadTexts:
    ipoProdTrunk500AnalogQuadV2.setStatus("current")
_IpoProdPCCardModules_ObjectIdentity = ObjectIdentity
ipoProdPCCardModules = _IpoProdPCCardModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 3)
)
_IpoProdPCCardMemVmail_ObjectIdentity = ObjectIdentity
ipoProdPCCardMemVmail = _IpoProdPCCardMemVmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    ipoProdPCCardMemVmail.setStatus("current")
_IpoProdPCCardWLAN_ObjectIdentity = ObjectIdentity
ipoProdPCCardWLAN = _IpoProdPCCardWLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 3, 2)
)
if mibBuilder.loadTexts:
    ipoProdPCCardWLAN.setStatus("current")
_IpoProdCarrierModules_ObjectIdentity = ObjectIdentity
ipoProdCarrierModules = _IpoProdCarrierModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 4)
)
_IpoProdCarrier_ObjectIdentity = ObjectIdentity
ipoProdCarrier = _IpoProdCarrier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 4, 1)
)
if mibBuilder.loadTexts:
    ipoProdCarrier.setStatus("current")
_IpoProdPhonePortModules_ObjectIdentity = ObjectIdentity
ipoProdPhonePortModules = _IpoProdPhonePortModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 5)
)
_IpoProdPhonePortPOT8_ObjectIdentity = ObjectIdentity
ipoProdPhonePortPOT8 = _IpoProdPhonePortPOT8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 5, 1)
)
if mibBuilder.loadTexts:
    ipoProdPhonePortPOT8.setStatus("current")
_IpoProdPhonePortDS8_ObjectIdentity = ObjectIdentity
ipoProdPhonePortDS8 = _IpoProdPhonePortDS8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 5, 2)
)
if mibBuilder.loadTexts:
    ipoProdPhonePortDS8.setStatus("current")
_IpoProdPhonePortPOT2_ObjectIdentity = ObjectIdentity
ipoProdPhonePortPOT2 = _IpoProdPhonePortPOT2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 5, 3)
)
if mibBuilder.loadTexts:
    ipoProdPhonePortPOT2.setStatus("current")
_IpoProdPhonePortCombo_ObjectIdentity = ObjectIdentity
ipoProdPhonePortCombo = _IpoProdPhonePortCombo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 5, 4)
)
if mibBuilder.loadTexts:
    ipoProdPhonePortCombo.setStatus("current")
_IpoProdPhonePortETR6_ObjectIdentity = ObjectIdentity
ipoProdPhonePortETR6 = _IpoProdPhonePortETR6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 5, 5)
)
if mibBuilder.loadTexts:
    ipoProdPhonePortETR6.setStatus("current")
_IpoProdPhonePortTCM8_ObjectIdentity = ObjectIdentity
ipoProdPhonePortTCM8 = _IpoProdPhonePortTCM8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 5, 6)
)
if mibBuilder.loadTexts:
    ipoProdPhonePortTCM8.setStatus("current")
_IpoProdVCMModules_ObjectIdentity = ObjectIdentity
ipoProdVCMModules = _IpoProdVCMModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 6)
)
_IpoProdVCMMod32_ObjectIdentity = ObjectIdentity
ipoProdVCMMod32 = _IpoProdVCMMod32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 6, 1)
)
if mibBuilder.loadTexts:
    ipoProdVCMMod32.setStatus("current")
_IpoProdVCMMod64_ObjectIdentity = ObjectIdentity
ipoProdVCMMod64 = _IpoProdVCMMod64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 6, 2)
)
if mibBuilder.loadTexts:
    ipoProdVCMMod64.setStatus("current")
_IpoProdVCMMod32V2_ObjectIdentity = ObjectIdentity
ipoProdVCMMod32V2 = _IpoProdVCMMod32V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 6, 3)
)
if mibBuilder.loadTexts:
    ipoProdVCMMod32V2.setStatus("current")
_IpoProdVCMMod64V2_ObjectIdentity = ObjectIdentity
ipoProdVCMMod64V2 = _IpoProdVCMMod64V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 6, 4)
)
if mibBuilder.loadTexts:
    ipoProdVCMMod64V2.setStatus("current")
_IpoProdExpansionModules_ObjectIdentity = ObjectIdentity
ipoProdExpansionModules = _IpoProdExpansionModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 7)
)
_IpoProdExpMod4Port_ObjectIdentity = ObjectIdentity
ipoProdExpMod4Port = _IpoProdExpMod4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 7, 1)
)
if mibBuilder.loadTexts:
    ipoProdExpMod4Port.setStatus("current")
_IpoProdUCPModules_ObjectIdentity = ObjectIdentity
ipoProdUCPModules = _IpoProdUCPModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 4, 8)
)
_IpoProdPorts_ObjectIdentity = ObjectIdentity
ipoProdPorts = _IpoProdPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5)
)
_IpoProdPortBRI_ObjectIdentity = ObjectIdentity
ipoProdPortBRI = _IpoProdPortBRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ipoProdPortBRI.setStatus("current")
_IpoProdPortE1PRI_ObjectIdentity = ObjectIdentity
ipoProdPortE1PRI = _IpoProdPortE1PRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    ipoProdPortE1PRI.setStatus("current")
_IpoProdPortJ1PRI_ObjectIdentity = ObjectIdentity
ipoProdPortJ1PRI = _IpoProdPortJ1PRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    ipoProdPortJ1PRI.setStatus("current")
_IpoProdPortT1PRI_ObjectIdentity = ObjectIdentity
ipoProdPortT1PRI = _IpoProdPortT1PRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    ipoProdPortT1PRI.setStatus("current")
_IpoProdPortR2_ObjectIdentity = ObjectIdentity
ipoProdPortR2 = _IpoProdPortR2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 5)
)
if mibBuilder.loadTexts:
    ipoProdPortR2.setStatus("current")
_IpoProdPortR2CoAx_ObjectIdentity = ObjectIdentity
ipoProdPortR2CoAx = _IpoProdPortR2CoAx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 6)
)
if mibBuilder.loadTexts:
    ipoProdPortR2CoAx.setStatus("current")
_IpoProdPortWAN_ObjectIdentity = ObjectIdentity
ipoProdPortWAN = _IpoProdPortWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 7)
)
if mibBuilder.loadTexts:
    ipoProdPortWAN.setStatus("current")
_IpoProdPortAnalog_ObjectIdentity = ObjectIdentity
ipoProdPortAnalog = _IpoProdPortAnalog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 8)
)
if mibBuilder.loadTexts:
    ipoProdPortAnalog.setStatus("current")
_IpoProdPortPower_ObjectIdentity = ObjectIdentity
ipoProdPortPower = _IpoProdPortPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 9)
)
if mibBuilder.loadTexts:
    ipoProdPortPower.setStatus("current")
_IpoProdPortDT_ObjectIdentity = ObjectIdentity
ipoProdPortDT = _IpoProdPortDT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 10)
)
if mibBuilder.loadTexts:
    ipoProdPortDT.setStatus("current")
_IpoProdPortDS_ObjectIdentity = ObjectIdentity
ipoProdPortDS = _IpoProdPortDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 11)
)
if mibBuilder.loadTexts:
    ipoProdPortDS.setStatus("current")
_IpoProdPortPOT_ObjectIdentity = ObjectIdentity
ipoProdPortPOT = _IpoProdPortPOT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 12)
)
if mibBuilder.loadTexts:
    ipoProdPortPOT.setStatus("current")
_IpoProdPortS0_ObjectIdentity = ObjectIdentity
ipoProdPortS0 = _IpoProdPortS0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 13)
)
if mibBuilder.loadTexts:
    ipoProdPortS0.setStatus("current")
_IpoProdPortLAN_ObjectIdentity = ObjectIdentity
ipoProdPortLAN = _IpoProdPortLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 14)
)
if mibBuilder.loadTexts:
    ipoProdPortLAN.setStatus("current")
_IpoProdPortWLAN_ObjectIdentity = ObjectIdentity
ipoProdPortWLAN = _IpoProdPortWLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 15)
)
if mibBuilder.loadTexts:
    ipoProdPortWLAN.setStatus("current")
_IpoProdPortDTE_ObjectIdentity = ObjectIdentity
ipoProdPortDTE = _IpoProdPortDTE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 16)
)
if mibBuilder.loadTexts:
    ipoProdPortDTE.setStatus("current")
_IpoProdPortUSB_ObjectIdentity = ObjectIdentity
ipoProdPortUSB = _IpoProdPortUSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 17)
)
if mibBuilder.loadTexts:
    ipoProdPortUSB.setStatus("current")
_IpoProdPortAudio_ObjectIdentity = ObjectIdentity
ipoProdPortAudio = _IpoProdPortAudio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 18)
)
if mibBuilder.loadTexts:
    ipoProdPortAudio.setStatus("current")
_IpoProdPortEtherWANLink_ObjectIdentity = ObjectIdentity
ipoProdPortEtherWANLink = _IpoProdPortEtherWANLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 19)
)
if mibBuilder.loadTexts:
    ipoProdPortEtherWANLink.setStatus("current")
_IpoProdPortExtOP_ObjectIdentity = ObjectIdentity
ipoProdPortExtOP = _IpoProdPortExtOP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 20)
)
if mibBuilder.loadTexts:
    ipoProdPortExtOP.setStatus("current")
_IpoProdPortNet1_ObjectIdentity = ObjectIdentity
ipoProdPortNet1 = _IpoProdPortNet1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 21)
)
if mibBuilder.loadTexts:
    ipoProdPortNet1.setStatus("current")
_IpoProdPortNet2_ObjectIdentity = ObjectIdentity
ipoProdPortNet2 = _IpoProdPortNet2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 5, 22)
)
if mibBuilder.loadTexts:
    ipoProdPortNet2.setStatus("current")
_IpoProdDongleModules_ObjectIdentity = ObjectIdentity
ipoProdDongleModules = _IpoProdDongleModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 6)
)
_IpoProdGenericDongle_ObjectIdentity = ObjectIdentity
ipoProdGenericDongle = _IpoProdGenericDongle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ipoProdGenericDongle.setStatus("current")
_IpoProdSubModules_ObjectIdentity = ObjectIdentity
ipoProdSubModules = _IpoProdSubModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 7)
)
_IpoProdSubModVCM10_ObjectIdentity = ObjectIdentity
ipoProdSubModVCM10 = _IpoProdSubModVCM10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    ipoProdSubModVCM10.setStatus("current")
_IpoProdUCModules_ObjectIdentity = ObjectIdentity
ipoProdUCModules = _IpoProdUCModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 8)
)
_IpoProdC110UCM_ObjectIdentity = ObjectIdentity
ipoProdC110UCM = _IpoProdC110UCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    ipoProdC110UCM.setStatus("current")
_IpoProdC110UCMV2_ObjectIdentity = ObjectIdentity
ipoProdC110UCMV2 = _IpoProdC110UCMV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    ipoProdC110UCMV2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPO-PROD-MIB",
    **{"ipoProdMIB": ipoProdMIB,
       "ipoProdControllers": ipoProdControllers,
       "ipoProd401Family": ipoProd401Family,
       "ipoProd401DT2": ipoProd401DT2,
       "ipoProd401DT4": ipoProd401DT4,
       "ipoProd401DS2": ipoProd401DS2,
       "ipoProd401DS4": ipoProd401DS4,
       "ipoProd403Family": ipoProd403Family,
       "ipoProd403DT": ipoProd403DT,
       "ipoProd403DS": ipoProd403DS,
       "ipoProd406Family": ipoProd406Family,
       "ipoProd406": ipoProd406,
       "ipoProd412Family": ipoProd412Family,
       "ipoProd412": ipoProd412,
       "ipoProdSmallOfficeEditionFamily": ipoProdSmallOfficeEditionFamily,
       "ipoProdSmallOfficeEditionPOTS4": ipoProdSmallOfficeEditionPOTS4,
       "ipoProdSmallOfficeEditionPOTS8": ipoProdSmallOfficeEditionPOTS8,
       "ipoProdSmallOfficeEditionDT8": ipoProdSmallOfficeEditionDT8,
       "ipoProdSmallOfficeEditionDS8": ipoProdSmallOfficeEditionDS8,
       "ipoProdR403Family": ipoProdR403Family,
       "ipoProdR403DT": ipoProdR403DT,
       "ipoProdR403DS": ipoProdR403DS,
       "ipoProdR406Family": ipoProdR406Family,
       "ipoProdR406": ipoProdR406,
       "ipoProdR406DT": ipoProdR406DT,
       "ipoProdR406DS": ipoProdR406DS,
       "ipoProdR406Full": ipoProdR406Full,
       "ipoProdSogFamily": ipoProdSogFamily,
       "ipoProdSogSOEPOTS4": ipoProdSogSOEPOTS4,
       "ipoProdSogSOEPOTS8": ipoProdSogSOEPOTS8,
       "ipoProdSogSOEDT8": ipoProdSogSOEDT8,
       "ipoProdSogSOEDS8": ipoProdSogSOEDS8,
       "ipoProd500Family": ipoProd500Family,
       "ipoProd500Slot4": ipoProd500Slot4,
       "ipoProd500Slot8": ipoProd500Slot8,
       "ipoProd500v2Family": ipoProd500v2Family,
       "ipoProd500v2IPOffice": ipoProd500v2IPOffice,
       "ipoProd500v2Partner": ipoProd500v2Partner,
       "ipoProd500v2Norstar": ipoProd500v2Norstar,
       "ipoProd500v2Branch": ipoProd500v2Branch,
       "ipoProd500v2Quick": ipoProd500v2Quick,
       "ipoProd500v2SEditionExpansion": ipoProd500v2SEditionExpansion,
       "ipoProd500v2IPOfficeSelect": ipoProd500v2IPOfficeSelect,
       "ipoProd500v2SEditionExpansionSelect": ipoProd500v2SEditionExpansionSelect,
       "ipoProdExpModules": ipoProdExpModules,
       "ipoProdExpModDT": ipoProdExpModDT,
       "ipoProdExpModDT16": ipoProdExpModDT16,
       "ipoProdExpModDT30": ipoProdExpModDT30,
       "ipoProdExpModDS": ipoProdExpModDS,
       "ipoProdExpModDS16": ipoProdExpModDS16,
       "ipoProdExpModDS30": ipoProdExpModDS30,
       "ipoProdExpModPhone": ipoProdExpModPhone,
       "ipoProdExpModPhone8": ipoProdExpModPhone8,
       "ipoProdExpModPhone16": ipoProdExpModPhone16,
       "ipoProdExpModPhone30": ipoProdExpModPhone30,
       "ipoProdExpModS0": ipoProdExpModS0,
       "ipoProdExpModS08": ipoProdExpModS08,
       "ipoProdExpModS016": ipoProdExpModS016,
       "ipoProdExpModAnalog": ipoProdExpModAnalog,
       "ipoProdExpModATM8": ipoProdExpModATM8,
       "ipoProdExpModATM16": ipoProdExpModATM16,
       "ipoProdExpModWAN": ipoProdExpModWAN,
       "ipoProdExpModWAN3": ipoProdExpModWAN3,
       "ipoProdExpModRDS": ipoProdExpModRDS,
       "ipoProdExpModRDS16": ipoProdExpModRDS16,
       "ipoProdExpModRDS30": ipoProdExpModRDS30,
       "ipoProdExpModRPhone": ipoProdExpModRPhone,
       "ipoProdExpModRPhone8": ipoProdExpModRPhone8,
       "ipoProdExpModRPhone16": ipoProdExpModRPhone16,
       "ipoProdExpModRPhone30": ipoProdExpModRPhone30,
       "ipoProdExpModDSA": ipoProdExpModDSA,
       "ipoProdExpModDSA16RJ21": ipoProdExpModDSA16RJ21,
       "ipoProdExpModDSA30RJ21": ipoProdExpModDSA30RJ21,
       "ipoProdExpModDSA16RJ45": ipoProdExpModDSA16RJ45,
       "ipoProdExpModDSA30RJ45": ipoProdExpModDSA30RJ45,
       "ipoProdSlots": ipoProdSlots,
       "ipoProdSlotVCM": ipoProdSlotVCM,
       "ipoProdSlotModems": ipoProdSlotModems,
       "ipoProdSlotVmailMemory": ipoProdSlotVmailMemory,
       "ipoProdSlotWAN": ipoProdSlotWAN,
       "ipoProdSlotPCCard": ipoProdSlotPCCard,
       "ipoProdSlotTrunks": ipoProdSlotTrunks,
       "ipoProdSlotExpansion": ipoProdSlotExpansion,
       "ipoProdSlot500Generic": ipoProdSlot500Generic,
       "ipoProdSlotMezzanine": ipoProdSlotMezzanine,
       "ipoProdSlotCarrierVCM": ipoProdSlotCarrierVCM,
       "ipoProdSlotCarrierTrunk": ipoProdSlotCarrierTrunk,
       "ipoProdSlotModules": ipoProdSlotModules,
       "ipoProdIntegralModules": ipoProdIntegralModules,
       "ipoProdIntModVCM": ipoProdIntModVCM,
       "ipoProdIntModVCM3": ipoProdIntModVCM3,
       "ipoProdIntModVCM5": ipoProdIntModVCM5,
       "ipoProdIntModVCM6": ipoProdIntModVCM6,
       "ipoProdIntModVCM8": ipoProdIntModVCM8,
       "ipoProdIntModVCM10": ipoProdIntModVCM10,
       "ipoProdIntModVCM12": ipoProdIntModVCM12,
       "ipoProdIntModVCM16": ipoProdIntModVCM16,
       "ipoProdIntModVCM20": ipoProdIntModVCM20,
       "ipoProdIntModVCM30": ipoProdIntModVCM30,
       "ipoProdIntModVCM24": ipoProdIntModVCM24,
       "ipoProdIntModVCM4": ipoProdIntModVCM4,
       "ipoProdIntModModem": ipoProdIntModModem,
       "ipoProdIntModModemDual": ipoProdIntModModemDual,
       "ipoProdIntModModemMulti": ipoProdIntModModemMulti,
       "ipoProdIntModWAN": ipoProdIntModWAN,
       "ipoProdIntModWANModule": ipoProdIntModWANModule,
       "ipoProdIntModMem": ipoProdIntModMem,
       "ipoProdIntModMemVmail": ipoProdIntModMemVmail,
       "ipoProdTrunkModules": ipoProdTrunkModules,
       "ipoProdTrunkAnalogQuad": ipoProdTrunkAnalogQuad,
       "ipoProdTrunkBRIQuad": ipoProdTrunkBRIQuad,
       "ipoProdTrunkE1PRISingle": ipoProdTrunkE1PRISingle,
       "ipoProdTrunkE1PRIDual": ipoProdTrunkE1PRIDual,
       "ipoProdTrunkJ1PRISingle": ipoProdTrunkJ1PRISingle,
       "ipoProdTrunkJ1PRIDual": ipoProdTrunkJ1PRIDual,
       "ipoProdTrunkT1PRISingle": ipoProdTrunkT1PRISingle,
       "ipoProdTrunkT1PRIDual": ipoProdTrunkT1PRIDual,
       "ipoProdTrunkIndex": ipoProdTrunkIndex,
       "ipoProdTrunkR2Single": ipoProdTrunkR2Single,
       "ipoProdTrunkR2Dual": ipoProdTrunkR2Dual,
       "ipoProdTrunkR2CoAxSingle": ipoProdTrunkR2CoAxSingle,
       "ipoProdTrunkR2CoAxDual": ipoProdTrunkR2CoAxDual,
       "ipoProdTrunkRAnalogQuad": ipoProdTrunkRAnalogQuad,
       "ipoProdTrunk500AnalogQuad": ipoProdTrunk500AnalogQuad,
       "ipoProdTrunk500BRIDual": ipoProdTrunk500BRIDual,
       "ipoProdTrunk500BRIQuad": ipoProdTrunk500BRIQuad,
       "ipoProdTrunkUniversalPRIDS0Single": ipoProdTrunkUniversalPRIDS0Single,
       "ipoProdTrunkUniversalPRIDS0Dual": ipoProdTrunkUniversalPRIDS0Dual,
       "ipoProdTrunk500AnalogQuadV2": ipoProdTrunk500AnalogQuadV2,
       "ipoProdPCCardModules": ipoProdPCCardModules,
       "ipoProdPCCardMemVmail": ipoProdPCCardMemVmail,
       "ipoProdPCCardWLAN": ipoProdPCCardWLAN,
       "ipoProdCarrierModules": ipoProdCarrierModules,
       "ipoProdCarrier": ipoProdCarrier,
       "ipoProdPhonePortModules": ipoProdPhonePortModules,
       "ipoProdPhonePortPOT8": ipoProdPhonePortPOT8,
       "ipoProdPhonePortDS8": ipoProdPhonePortDS8,
       "ipoProdPhonePortPOT2": ipoProdPhonePortPOT2,
       "ipoProdPhonePortCombo": ipoProdPhonePortCombo,
       "ipoProdPhonePortETR6": ipoProdPhonePortETR6,
       "ipoProdPhonePortTCM8": ipoProdPhonePortTCM8,
       "ipoProdVCMModules": ipoProdVCMModules,
       "ipoProdVCMMod32": ipoProdVCMMod32,
       "ipoProdVCMMod64": ipoProdVCMMod64,
       "ipoProdVCMMod32V2": ipoProdVCMMod32V2,
       "ipoProdVCMMod64V2": ipoProdVCMMod64V2,
       "ipoProdExpansionModules": ipoProdExpansionModules,
       "ipoProdExpMod4Port": ipoProdExpMod4Port,
       "ipoProdUCPModules": ipoProdUCPModules,
       "ipoProdPorts": ipoProdPorts,
       "ipoProdPortBRI": ipoProdPortBRI,
       "ipoProdPortE1PRI": ipoProdPortE1PRI,
       "ipoProdPortJ1PRI": ipoProdPortJ1PRI,
       "ipoProdPortT1PRI": ipoProdPortT1PRI,
       "ipoProdPortR2": ipoProdPortR2,
       "ipoProdPortR2CoAx": ipoProdPortR2CoAx,
       "ipoProdPortWAN": ipoProdPortWAN,
       "ipoProdPortAnalog": ipoProdPortAnalog,
       "ipoProdPortPower": ipoProdPortPower,
       "ipoProdPortDT": ipoProdPortDT,
       "ipoProdPortDS": ipoProdPortDS,
       "ipoProdPortPOT": ipoProdPortPOT,
       "ipoProdPortS0": ipoProdPortS0,
       "ipoProdPortLAN": ipoProdPortLAN,
       "ipoProdPortWLAN": ipoProdPortWLAN,
       "ipoProdPortDTE": ipoProdPortDTE,
       "ipoProdPortUSB": ipoProdPortUSB,
       "ipoProdPortAudio": ipoProdPortAudio,
       "ipoProdPortEtherWANLink": ipoProdPortEtherWANLink,
       "ipoProdPortExtOP": ipoProdPortExtOP,
       "ipoProdPortNet1": ipoProdPortNet1,
       "ipoProdPortNet2": ipoProdPortNet2,
       "ipoProdDongleModules": ipoProdDongleModules,
       "ipoProdGenericDongle": ipoProdGenericDongle,
       "ipoProdSubModules": ipoProdSubModules,
       "ipoProdSubModVCM10": ipoProdSubModVCM10,
       "ipoProdUCModules": ipoProdUCModules,
       "ipoProdC110UCM": ipoProdC110UCM,
       "ipoProdC110UCMV2": ipoProdC110UCMV2}
)
