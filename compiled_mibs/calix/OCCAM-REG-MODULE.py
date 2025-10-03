# SNMP MIB module (OCCAM-REG-MODULE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\calix\OCCAM-REG-MODULE
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:22 2025
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
 iso,
 mib_2,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "snmpModules")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

occam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6066)
)
if mibBuilder.loadTexts:
    occam.setRevisions(
        ("2001-04-27 10:51",
         "2007-12-05 10:00",
         "2007-03-02 10:00",
         "2007-01-10 10:00",
         "2009-05-18 10:00",
         "2009-12-09 00:00",
         "2009-12-18 00:00",
         "2010-03-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_OccamProducts_ObjectIdentity = ObjectIdentity
occamProducts = _OccamProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1)
)
if mibBuilder.loadTexts:
    occamProducts.setStatus("current")
_Blc1100_ObjectIdentity = ObjectIdentity
blc1100 = _Blc1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 1)
)
_Blc1200_ObjectIdentity = ObjectIdentity
blc1200 = _Blc1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 2)
)
_Blc2200_ObjectIdentity = ObjectIdentity
blc2200 = _Blc2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 3)
)
_Blc1240_ObjectIdentity = ObjectIdentity
blc1240 = _Blc1240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 4)
)
_Blc6220_ObjectIdentity = ObjectIdentity
blc6220 = _Blc6220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 5)
)
_Blc1210_ObjectIdentity = ObjectIdentity
blc1210 = _Blc1210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 6)
)
_Blc1220_ObjectIdentity = ObjectIdentity
blc1220 = _Blc1220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 7)
)
_Blc6100_ObjectIdentity = ObjectIdentity
blc6100 = _Blc6100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 8)
)
_Blc6110_ObjectIdentity = ObjectIdentity
blc6110 = _Blc6110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 9)
)
_Blc6140_ObjectIdentity = ObjectIdentity
blc6140 = _Blc6140_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 10)
)
_Blc6150_ObjectIdentity = ObjectIdentity
blc6150 = _Blc6150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 11)
)
_Blc6205_ObjectIdentity = ObjectIdentity
blc6205 = _Blc6205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 12)
)
_Blc6235_ObjectIdentity = ObjectIdentity
blc6235 = _Blc6235_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 13)
)
_Blc6640_ObjectIdentity = ObjectIdentity
blc6640 = _Blc6640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 14)
)
_Blc6440_ObjectIdentity = ObjectIdentity
blc6440 = _Blc6440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 15)
)
_Blc6151_ObjectIdentity = ObjectIdentity
blc6151 = _Blc6151_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 16)
)
_Blc6248_ObjectIdentity = ObjectIdentity
blc6248 = _Blc6248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 17)
)
_Blc6208_ObjectIdentity = ObjectIdentity
blc6208 = _Blc6208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 18)
)
_Blc6212_ObjectIdentity = ObjectIdentity
blc6212 = _Blc6212_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 19)
)
_Blc615001_ObjectIdentity = ObjectIdentity
blc615001 = _Blc615001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 20)
)
_Blc664001_ObjectIdentity = ObjectIdentity
blc664001 = _Blc664001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 21)
)
_Blc644001_ObjectIdentity = ObjectIdentity
blc644001 = _Blc644001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 22)
)
_Blc620801_ObjectIdentity = ObjectIdentity
blc620801 = _Blc620801_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 23)
)
_Blc624801_ObjectIdentity = ObjectIdentity
blc624801 = _Blc624801_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 24)
)
_Blc621201_ObjectIdentity = ObjectIdentity
blc621201 = _Blc621201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 25)
)
_Blc6252_ObjectIdentity = ObjectIdentity
blc6252 = _Blc6252_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 26)
)
_Blc625201_ObjectIdentity = ObjectIdentity
blc625201 = _Blc625201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 27)
)
_Blc615101_ObjectIdentity = ObjectIdentity
blc615101 = _Blc615101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 28)
)
_Blc621202_ObjectIdentity = ObjectIdentity
blc621202 = _Blc621202_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 29)
)
_Blc625202_ObjectIdentity = ObjectIdentity
blc625202 = _Blc625202_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 30)
)
_Blc666001_ObjectIdentity = ObjectIdentity
blc666001 = _Blc666001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 31)
)
_Blc615201_ObjectIdentity = ObjectIdentity
blc615201 = _Blc615201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 32)
)
_Blc666002_ObjectIdentity = ObjectIdentity
blc666002 = _Blc666002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 35)
)
_Blc666003_ObjectIdentity = ObjectIdentity
blc666003 = _Blc666003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 36)
)
_Blc6312_ObjectIdentity = ObjectIdentity
blc6312 = _Blc6312_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 37)
)
_Blc6214_ObjectIdentity = ObjectIdentity
blc6214 = _Blc6214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 38)
)
_Blc6314_ObjectIdentity = ObjectIdentity
blc6314 = _Blc6314_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 39)
)
_Blc6246_ObjectIdentity = ObjectIdentity
blc6246 = _Blc6246_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 40)
)
_Blc6244_ObjectIdentity = ObjectIdentity
blc6244 = _Blc6244_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 41)
)
_Blc6242_ObjectIdentity = ObjectIdentity
blc6242 = _Blc6242_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 42)
)
_Blc6322_ObjectIdentity = ObjectIdentity
blc6322 = _Blc6322_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 43)
)
_Blc6450_ObjectIdentity = ObjectIdentity
blc6450 = _Blc6450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 44)
)
_Blc625203_ObjectIdentity = ObjectIdentity
blc625203 = _Blc625203_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 45)
)
_Blc632201_ObjectIdentity = ObjectIdentity
blc632201 = _Blc632201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 46)
)
_Blc6316_ObjectIdentity = ObjectIdentity
blc6316 = _Blc6316_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 50)
)
_Blc6216_ObjectIdentity = ObjectIdentity
blc6216 = _Blc6216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 1, 51)
)
_OccamGeneric_ObjectIdentity = ObjectIdentity
occamGeneric = _OccamGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2)
)
if mibBuilder.loadTexts:
    occamGeneric.setStatus("current")
_OccamGenericModules_ObjectIdentity = ObjectIdentity
occamGenericModules = _OccamGenericModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1)
)
if mibBuilder.loadTexts:
    occamGenericModules.setStatus("current")
_OccamGenericMonitorModules_ObjectIdentity = ObjectIdentity
occamGenericMonitorModules = _OccamGenericMonitorModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1)
)
if mibBuilder.loadTexts:
    occamGenericMonitorModules.setStatus("current")
_OccamGenericInterfaceModules_ObjectIdentity = ObjectIdentity
occamGenericInterfaceModules = _OccamGenericInterfaceModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2)
)
if mibBuilder.loadTexts:
    occamGenericInterfaceModules.setStatus("current")
_OccamGenericEtherlikeModules_ObjectIdentity = ObjectIdentity
occamGenericEtherlikeModules = _OccamGenericEtherlikeModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    occamGenericEtherlikeModules.setStatus("current")
_OccamGenericSerialModules_ObjectIdentity = ObjectIdentity
occamGenericSerialModules = _OccamGenericSerialModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    occamGenericSerialModules.setStatus("current")
_OccamGenericDslModules_ObjectIdentity = ObjectIdentity
occamGenericDslModules = _OccamGenericDslModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    occamGenericDslModules.setStatus("current")
_OccamGenericSubscriberModules_ObjectIdentity = ObjectIdentity
occamGenericSubscriberModules = _OccamGenericSubscriberModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    occamGenericSubscriberModules.setStatus("current")
_OccamGenericIgModules_ObjectIdentity = ObjectIdentity
occamGenericIgModules = _OccamGenericIgModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    occamGenericIgModules.setStatus("current")
_OccamGenericGponModules_ObjectIdentity = ObjectIdentity
occamGenericGponModules = _OccamGenericGponModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    occamGenericGponModules.setStatus("current")
_OccamGenericXdslModules_ObjectIdentity = ObjectIdentity
occamGenericXdslModules = _OccamGenericXdslModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    occamGenericXdslModules.setStatus("current")
_OccamGenericHardwareModules_ObjectIdentity = ObjectIdentity
occamGenericHardwareModules = _OccamGenericHardwareModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 3)
)
if mibBuilder.loadTexts:
    occamGenericHardwareModules.setStatus("current")
_OccamGenericNotifications_ObjectIdentity = ObjectIdentity
occamGenericNotifications = _OccamGenericNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 4)
)
if mibBuilder.loadTexts:
    occamGenericNotifications.setStatus("current")
_OccamCaps_ObjectIdentity = ObjectIdentity
occamCaps = _OccamCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 3)
)
if mibBuilder.loadTexts:
    occamCaps.setStatus("current")
_OccamModules_ObjectIdentity = ObjectIdentity
occamModules = _OccamModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 4)
)
if mibBuilder.loadTexts:
    occamModules.setStatus("current")
_Blc1100Modules_ObjectIdentity = ObjectIdentity
blc1100Modules = _Blc1100Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 4, 1)
)
_Blc1200Modules_ObjectIdentity = ObjectIdentity
blc1200Modules = _Blc1200Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 4, 2)
)
_Blc2200Modules_ObjectIdentity = ObjectIdentity
blc2200Modules = _Blc2200Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 4, 3)
)
_Blc1240Modules_ObjectIdentity = ObjectIdentity
blc1240Modules = _Blc1240Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 4, 4)
)
_Blc6220Modules_ObjectIdentity = ObjectIdentity
blc6220Modules = _Blc6220Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 4, 5)
)
_OccamVendors_ObjectIdentity = ObjectIdentity
occamVendors = _OccamVendors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 5)
)
if mibBuilder.loadTexts:
    occamVendors.setStatus("current")
_OccamEms_ObjectIdentity = ObjectIdentity
occamEms = _OccamEms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 6)
)
if mibBuilder.loadTexts:
    occamEms.setStatus("current")
_OccamEmsModules_ObjectIdentity = ObjectIdentity
occamEmsModules = _OccamEmsModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 6, 1)
)
if mibBuilder.loadTexts:
    occamEmsModules.setStatus("current")
_OccamEmsForwardingModules_ObjectIdentity = ObjectIdentity
occamEmsForwardingModules = _OccamEmsForwardingModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 6, 2)
)
if mibBuilder.loadTexts:
    occamEmsForwardingModules.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OCCAM-REG-MODULE",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "occam": occam,
       "occamProducts": occamProducts,
       "blc1100": blc1100,
       "blc1200": blc1200,
       "blc2200": blc2200,
       "blc1240": blc1240,
       "blc6220": blc6220,
       "blc1210": blc1210,
       "blc1220": blc1220,
       "blc6100": blc6100,
       "blc6110": blc6110,
       "blc6140": blc6140,
       "blc6150": blc6150,
       "blc6205": blc6205,
       "blc6235": blc6235,
       "blc6640": blc6640,
       "blc6440": blc6440,
       "blc6151": blc6151,
       "blc6248": blc6248,
       "blc6208": blc6208,
       "blc6212": blc6212,
       "blc615001": blc615001,
       "blc664001": blc664001,
       "blc644001": blc644001,
       "blc620801": blc620801,
       "blc624801": blc624801,
       "blc621201": blc621201,
       "blc6252": blc6252,
       "blc625201": blc625201,
       "blc615101": blc615101,
       "blc621202": blc621202,
       "blc625202": blc625202,
       "blc666001": blc666001,
       "blc615201": blc615201,
       "blc666002": blc666002,
       "blc666003": blc666003,
       "blc6312": blc6312,
       "blc6214": blc6214,
       "blc6314": blc6314,
       "blc6246": blc6246,
       "blc6244": blc6244,
       "blc6242": blc6242,
       "blc6322": blc6322,
       "blc6450": blc6450,
       "blc625203": blc625203,
       "blc632201": blc632201,
       "blc6316": blc6316,
       "blc6216": blc6216,
       "occamGeneric": occamGeneric,
       "occamGenericModules": occamGenericModules,
       "occamGenericMonitorModules": occamGenericMonitorModules,
       "occamGenericInterfaceModules": occamGenericInterfaceModules,
       "occamGenericEtherlikeModules": occamGenericEtherlikeModules,
       "occamGenericSerialModules": occamGenericSerialModules,
       "occamGenericDslModules": occamGenericDslModules,
       "occamGenericSubscriberModules": occamGenericSubscriberModules,
       "occamGenericIgModules": occamGenericIgModules,
       "occamGenericGponModules": occamGenericGponModules,
       "occamGenericXdslModules": occamGenericXdslModules,
       "occamGenericHardwareModules": occamGenericHardwareModules,
       "occamGenericNotifications": occamGenericNotifications,
       "occamCaps": occamCaps,
       "occamModules": occamModules,
       "blc1100Modules": blc1100Modules,
       "blc1200Modules": blc1200Modules,
       "blc2200Modules": blc2200Modules,
       "blc1240Modules": blc1240Modules,
       "blc6220Modules": blc6220Modules,
       "occamVendors": occamVendors,
       "occamEms": occamEms,
       "occamEmsModules": occamEmsModules,
       "occamEmsForwardingModules": occamEmsForwardingModules}
)
