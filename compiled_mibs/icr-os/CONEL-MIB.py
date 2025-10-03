# SNMP MIB module (CONEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\icr-os\CONEL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:20 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Conel_ObjectIdentity = ObjectIdentity
conel = _Conel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1)
)
_RouterER75_ObjectIdentity = ObjectIdentity
routerER75 = _RouterER75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 1)
)
_RouterER75i_ObjectIdentity = ObjectIdentity
routerER75i = _RouterER75i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 2)
)
_RouterUR5_ObjectIdentity = ObjectIdentity
routerUR5 = _RouterUR5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 3)
)
_RouterUR5i_ObjectIdentity = ObjectIdentity
routerUR5i = _RouterUR5i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 4)
)
_RouterXR5i_ObjectIdentity = ObjectIdentity
routerXR5i = _RouterXR5i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 5)
)
_RouterER75iV2_ObjectIdentity = ObjectIdentity
routerER75iV2 = _RouterER75iV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 6)
)
_RouterUR5V2_ObjectIdentity = ObjectIdentity
routerUR5V2 = _RouterUR5V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 7)
)
_RouterUR5iV2_ObjectIdentity = ObjectIdentity
routerUR5iV2 = _RouterUR5iV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 8)
)
_RouterXR5iV2_ObjectIdentity = ObjectIdentity
routerXR5iV2 = _RouterXR5iV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 9)
)
_RouterLR77V2_ObjectIdentity = ObjectIdentity
routerLR77V2 = _RouterLR77V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 10)
)
_RouterCR10V2_ObjectIdentity = ObjectIdentity
routerCR10V2 = _RouterCR10V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 11)
)
_RouterUCR11V2_ObjectIdentity = ObjectIdentity
routerUCR11V2 = _RouterUCR11V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 12)
)
_RouterUR5iV2L_ObjectIdentity = ObjectIdentity
routerUR5iV2L = _RouterUR5iV2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 13)
)
_RouterSpectre3G_ObjectIdentity = ObjectIdentity
routerSpectre3G = _RouterSpectre3G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 14)
)
_RouterSpectreRT_ObjectIdentity = ObjectIdentity
routerSpectreRT = _RouterSpectreRT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 15)
)
_RouterRR75i_ObjectIdentity = ObjectIdentity
routerRR75i = _RouterRR75i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 16)
)
_RouterSpectreLTEAT_ObjectIdentity = ObjectIdentity
routerSpectreLTEAT = _RouterSpectreLTEAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 17)
)
_RouterXR5iV2E_ObjectIdentity = ObjectIdentity
routerXR5iV2E = _RouterXR5iV2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 18)
)
_RouterBiviasV2HC_ObjectIdentity = ObjectIdentity
routerBiviasV2HC = _RouterBiviasV2HC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 19)
)
_RouterBiviasV2LC_ObjectIdentity = ObjectIdentity
routerBiviasV2LC = _RouterBiviasV2LC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 20)
)
_RouterSpectreLTEVZ_ObjectIdentity = ObjectIdentity
routerSpectreLTEVZ = _RouterSpectreLTEVZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 21)
)
_RouterBiviasV2LL_ObjectIdentity = ObjectIdentity
routerBiviasV2LL = _RouterBiviasV2LL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 22)
)
_RouterBiviasV2LH_ObjectIdentity = ObjectIdentity
routerBiviasV2LH = _RouterBiviasV2LH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 23)
)
_RouterBiviasV2HH_ObjectIdentity = ObjectIdentity
routerBiviasV2HH = _RouterBiviasV2HH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 24)
)
_RouterLR77V2L_ObjectIdentity = ObjectIdentity
routerLR77V2L = _RouterLR77V2L_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 25)
)
_RouterSpectreV3HSPA_ObjectIdentity = ObjectIdentity
routerSpectreV3HSPA = _RouterSpectreV3HSPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 26)
)
_RouterSpectreV3LTE_ObjectIdentity = ObjectIdentity
routerSpectreV3LTE = _RouterSpectreV3LTE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 27)
)
_RouterSpectreV3CDMA_ObjectIdentity = ObjectIdentity
routerSpectreV3CDMA = _RouterSpectreV3CDMA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 28)
)
_RouterSpectreV3ERT_ObjectIdentity = ObjectIdentity
routerSpectreV3ERT = _RouterSpectreV3ERT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 29)
)
_RouterSpectreV3TLTE_ObjectIdentity = ObjectIdentity
routerSpectreV3TLTE = _RouterSpectreV3TLTE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 32)
)
_RouterSpectreV3LTEUS_ObjectIdentity = ObjectIdentity
routerSpectreV3LTEUS = _RouterSpectreV3LTEUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 35)
)
_RouterSpectreV3LLTE_ObjectIdentity = ObjectIdentity
routerSpectreV3LLTE = _RouterSpectreV3LLTE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 36)
)
_RouterSpectreV3LLTEUS_ObjectIdentity = ObjectIdentity
routerSpectreV3LLTEUS = _RouterSpectreV3LLTEUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 37)
)
_RouterSpectreV3ERTUS_ObjectIdentity = ObjectIdentity
routerSpectreV3ERTUS = _RouterSpectreV3ERTUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 38)
)
_RouterSpectreV3LERT_ObjectIdentity = ObjectIdentity
routerSpectreV3LERT = _RouterSpectreV3LERT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 39)
)
_RouterSpectreV3LERTUS_ObjectIdentity = ObjectIdentity
routerSpectreV3LERTUS = _RouterSpectreV3LERTUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 40)
)
_RouterSpectreV3TLTEUS_ObjectIdentity = ObjectIdentity
routerSpectreV3TLTEUS = _RouterSpectreV3TLTEUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 41)
)
_RouterICR321X_ObjectIdentity = ObjectIdentity
routerICR321X = _RouterICR321X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 42)
)
_RouterICR323X_ObjectIdentity = ObjectIdentity
routerICR323X = _RouterICR323X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 43)
)
_RouterICR324X_ObjectIdentity = ObjectIdentity
routerICR324X = _RouterICR324X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 44)
)
_RouterICR320X_ObjectIdentity = ObjectIdentity
routerICR320X = _RouterICR320X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 45)
)
_RouterICR383X_ObjectIdentity = ObjectIdentity
routerICR383X = _RouterICR383X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 46)
)
_RouterICR213X_ObjectIdentity = ObjectIdentity
routerICR213X = _RouterICR213X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 47)
)
_RouterICR233X_ObjectIdentity = ObjectIdentity
routerICR233X = _RouterICR233X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 48)
)
_RouterICR440X_ObjectIdentity = ObjectIdentity
routerICR440X = _RouterICR440X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 49)
)
_RouterICR443X_ObjectIdentity = ObjectIdentity
routerICR443X = _RouterICR443X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 50)
)
_RouterICR444X_ObjectIdentity = ObjectIdentity
routerICR444X = _RouterICR444X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 51)
)
_RouterICR203X_ObjectIdentity = ObjectIdentity
routerICR203X = _RouterICR203X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 52)
)
_RouterICR204X_ObjectIdentity = ObjectIdentity
routerICR204X = _RouterICR204X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 53)
)
_RouterICR240X_ObjectIdentity = ObjectIdentity
routerICR240X = _RouterICR240X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 54)
)
_RouterICR243X_ObjectIdentity = ObjectIdentity
routerICR243X = _RouterICR243X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 55)
)
_RouterICR244X_ObjectIdentity = ObjectIdentity
routerICR244X = _RouterICR244X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 56)
)
_RouterICR201X_ObjectIdentity = ObjectIdentity
routerICR201X = _RouterICR201X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 57)
)
_RouterICR241X_ObjectIdentity = ObjectIdentity
routerICR241X = _RouterICR241X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 58)
)
_RouterICR445X_ObjectIdentity = ObjectIdentity
routerICR445X = _RouterICR445X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 59)
)
_RouterICR446X_ObjectIdentity = ObjectIdentity
routerICR446X = _RouterICR446X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 60)
)
_RouterICR250X_ObjectIdentity = ObjectIdentity
routerICR250X = _RouterICR250X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 61)
)
_RouterICR253X_ObjectIdentity = ObjectIdentity
routerICR253X = _RouterICR253X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 62)
)
_RouterICR254X_ObjectIdentity = ObjectIdentity
routerICR254X = _RouterICR254X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 63)
)
_RouterICR260X_ObjectIdentity = ObjectIdentity
routerICR260X = _RouterICR260X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 64)
)
_RouterICR263X_ObjectIdentity = ObjectIdentity
routerICR263X = _RouterICR263X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 65)
)
_RouterICR264X_ObjectIdentity = ObjectIdentity
routerICR264X = _RouterICR264X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 66)
)
_RouterICR270X_ObjectIdentity = ObjectIdentity
routerICR270X = _RouterICR270X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 67)
)
_RouterICR271X_ObjectIdentity = ObjectIdentity
routerICR271X = _RouterICR271X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 68)
)
_RouterICR273X_ObjectIdentity = ObjectIdentity
routerICR273X = _RouterICR273X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 69)
)
_RouterICR274X_ObjectIdentity = ObjectIdentity
routerICR274X = _RouterICR274X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 70)
)
_RouterICR280X_ObjectIdentity = ObjectIdentity
routerICR280X = _RouterICR280X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 71)
)
_RouterICR281X_ObjectIdentity = ObjectIdentity
routerICR281X = _RouterICR281X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 72)
)
_RouterICR283X_ObjectIdentity = ObjectIdentity
routerICR283X = _RouterICR283X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 73)
)
_RouterICR284X_ObjectIdentity = ObjectIdentity
routerICR284X = _RouterICR284X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 1, 74)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONEL-MIB",
    **{"conel": conel,
       "products": products,
       "routerER75": routerER75,
       "routerER75i": routerER75i,
       "routerUR5": routerUR5,
       "routerUR5i": routerUR5i,
       "routerXR5i": routerXR5i,
       "routerER75iV2": routerER75iV2,
       "routerUR5V2": routerUR5V2,
       "routerUR5iV2": routerUR5iV2,
       "routerXR5iV2": routerXR5iV2,
       "routerLR77V2": routerLR77V2,
       "routerCR10V2": routerCR10V2,
       "routerUCR11V2": routerUCR11V2,
       "routerUR5iV2L": routerUR5iV2L,
       "routerSpectre3G": routerSpectre3G,
       "routerSpectreRT": routerSpectreRT,
       "routerRR75i": routerRR75i,
       "routerSpectreLTEAT": routerSpectreLTEAT,
       "routerXR5iV2E": routerXR5iV2E,
       "routerBiviasV2HC": routerBiviasV2HC,
       "routerBiviasV2LC": routerBiviasV2LC,
       "routerSpectreLTEVZ": routerSpectreLTEVZ,
       "routerBiviasV2LL": routerBiviasV2LL,
       "routerBiviasV2LH": routerBiviasV2LH,
       "routerBiviasV2HH": routerBiviasV2HH,
       "routerLR77V2L": routerLR77V2L,
       "routerSpectreV3HSPA": routerSpectreV3HSPA,
       "routerSpectreV3LTE": routerSpectreV3LTE,
       "routerSpectreV3CDMA": routerSpectreV3CDMA,
       "routerSpectreV3ERT": routerSpectreV3ERT,
       "routerSpectreV3TLTE": routerSpectreV3TLTE,
       "routerSpectreV3LTEUS": routerSpectreV3LTEUS,
       "routerSpectreV3LLTE": routerSpectreV3LLTE,
       "routerSpectreV3LLTEUS": routerSpectreV3LLTEUS,
       "routerSpectreV3ERTUS": routerSpectreV3ERTUS,
       "routerSpectreV3LERT": routerSpectreV3LERT,
       "routerSpectreV3LERTUS": routerSpectreV3LERTUS,
       "routerSpectreV3TLTEUS": routerSpectreV3TLTEUS,
       "routerICR321X": routerICR321X,
       "routerICR323X": routerICR323X,
       "routerICR324X": routerICR324X,
       "routerICR320X": routerICR320X,
       "routerICR383X": routerICR383X,
       "routerICR213X": routerICR213X,
       "routerICR233X": routerICR233X,
       "routerICR440X": routerICR440X,
       "routerICR443X": routerICR443X,
       "routerICR444X": routerICR444X,
       "routerICR203X": routerICR203X,
       "routerICR204X": routerICR204X,
       "routerICR240X": routerICR240X,
       "routerICR243X": routerICR243X,
       "routerICR244X": routerICR244X,
       "routerICR201X": routerICR201X,
       "routerICR241X": routerICR241X,
       "routerICR445X": routerICR445X,
       "routerICR446X": routerICR446X,
       "routerICR250X": routerICR250X,
       "routerICR253X": routerICR253X,
       "routerICR254X": routerICR254X,
       "routerICR260X": routerICR260X,
       "routerICR263X": routerICR263X,
       "routerICR264X": routerICR264X,
       "routerICR270X": routerICR270X,
       "routerICR271X": routerICR271X,
       "routerICR273X": routerICR273X,
       "routerICR274X": routerICR274X,
       "routerICR280X": routerICR280X,
       "routerICR281X": routerICR281X,
       "routerICR283X": routerICR283X,
       "routerICR284X": routerICR284X}
)
