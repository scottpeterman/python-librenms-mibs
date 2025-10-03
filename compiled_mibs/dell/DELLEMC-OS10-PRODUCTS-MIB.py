# SNMP MIB module (DELLEMC-OS10-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\DELLEMC-OS10-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:57 2025
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

os10Products = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2)
)
if mibBuilder.loadTexts:
    os10Products.setRevisions(
        ("2019-07-09 12:00",
         "2019-03-07 12:00",
         "2018-05-15 12:00",
         "2018-01-26 12:00",
         "2017-10-27 12:00",
         "2017-10-11 12:00",
         "2017-09-19 12:00",
         "2017-06-21 12:00",
         "2017-01-25 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Os10SSeriesProducts_ObjectIdentity = ObjectIdentity
os10SSeriesProducts = _Os10SSeriesProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1)
)
if mibBuilder.loadTexts:
    os10SSeriesProducts.setStatus("current")
_S6000on_ObjectIdentity = ObjectIdentity
s6000on = _S6000on_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 1)
)
if mibBuilder.loadTexts:
    s6000on.setStatus("current")
_S4048on_ObjectIdentity = ObjectIdentity
s4048on = _S4048on_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 2)
)
if mibBuilder.loadTexts:
    s4048on.setStatus("current")
_S4048Ton_ObjectIdentity = ObjectIdentity
s4048Ton = _S4048Ton_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 3)
)
if mibBuilder.loadTexts:
    s4048Ton.setStatus("current")
_S3048on_ObjectIdentity = ObjectIdentity
s3048on = _S3048on_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 4)
)
if mibBuilder.loadTexts:
    s3048on.setStatus("current")
_S6010on_ObjectIdentity = ObjectIdentity
s6010on = _S6010on_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 5)
)
if mibBuilder.loadTexts:
    s6010on.setStatus("current")
_S4148Fon_ObjectIdentity = ObjectIdentity
s4148Fon = _S4148Fon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 6)
)
if mibBuilder.loadTexts:
    s4148Fon.setStatus("current")
_S4128Fon_ObjectIdentity = ObjectIdentity
s4128Fon = _S4128Fon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 7)
)
if mibBuilder.loadTexts:
    s4128Fon.setStatus("current")
_S4148Ton_ObjectIdentity = ObjectIdentity
s4148Ton = _S4148Ton_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 8)
)
if mibBuilder.loadTexts:
    s4148Ton.setStatus("current")
_S4128Ton_ObjectIdentity = ObjectIdentity
s4128Ton = _S4128Ton_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 9)
)
if mibBuilder.loadTexts:
    s4128Ton.setStatus("current")
_S4148FEon_ObjectIdentity = ObjectIdentity
s4148FEon = _S4148FEon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 10)
)
if mibBuilder.loadTexts:
    s4148FEon.setStatus("current")
_S4148Uon_ObjectIdentity = ObjectIdentity
s4148Uon = _S4148Uon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 11)
)
if mibBuilder.loadTexts:
    s4148Uon.setStatus("current")
_S4200on_ObjectIdentity = ObjectIdentity
s4200on = _S4200on_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 12)
)
if mibBuilder.loadTexts:
    s4200on.setStatus("deprecated")
_S5148Fon_ObjectIdentity = ObjectIdentity
s5148Fon = _S5148Fon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 13)
)
if mibBuilder.loadTexts:
    s5148Fon.setStatus("current")
_S4248FBon_ObjectIdentity = ObjectIdentity
s4248FBon = _S4248FBon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 14)
)
if mibBuilder.loadTexts:
    s4248FBon.setStatus("current")
_S4248FBLon_ObjectIdentity = ObjectIdentity
s4248FBLon = _S4248FBLon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 15)
)
if mibBuilder.loadTexts:
    s4248FBLon.setStatus("current")
_S4112Fon_ObjectIdentity = ObjectIdentity
s4112Fon = _S4112Fon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 16)
)
if mibBuilder.loadTexts:
    s4112Fon.setStatus("current")
_S4112Ton_ObjectIdentity = ObjectIdentity
s4112Ton = _S4112Ton_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 17)
)
if mibBuilder.loadTexts:
    s4112Ton.setStatus("current")
_S5212Fon_ObjectIdentity = ObjectIdentity
s5212Fon = _S5212Fon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 18)
)
if mibBuilder.loadTexts:
    s5212Fon.setStatus("current")
_S5224Fon_ObjectIdentity = ObjectIdentity
s5224Fon = _S5224Fon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 19)
)
if mibBuilder.loadTexts:
    s5224Fon.setStatus("current")
_S5232Fon_ObjectIdentity = ObjectIdentity
s5232Fon = _S5232Fon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 20)
)
if mibBuilder.loadTexts:
    s5232Fon.setStatus("current")
_S5248Fon_ObjectIdentity = ObjectIdentity
s5248Fon = _S5248Fon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 21)
)
if mibBuilder.loadTexts:
    s5248Fon.setStatus("current")
_S5296Fon_ObjectIdentity = ObjectIdentity
s5296Fon = _S5296Fon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 1, 22)
)
if mibBuilder.loadTexts:
    s5296Fon.setStatus("current")
_Os10MSeriesProducts_ObjectIdentity = ObjectIdentity
os10MSeriesProducts = _Os10MSeriesProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 2)
)
if mibBuilder.loadTexts:
    os10MSeriesProducts.setStatus("current")
_Mx5108Non_ObjectIdentity = ObjectIdentity
mx5108Non = _Mx5108Non_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mx5108Non.setStatus("current")
_Mx9116Non_ObjectIdentity = ObjectIdentity
mx9116Non = _Mx9116Non_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mx9116Non.setStatus("current")
_Os10ZSeriesProducts_ObjectIdentity = ObjectIdentity
os10ZSeriesProducts = _Os10ZSeriesProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 3)
)
if mibBuilder.loadTexts:
    os10ZSeriesProducts.setStatus("current")
_Z9100on_ObjectIdentity = ObjectIdentity
z9100on = _Z9100on_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 3, 1)
)
if mibBuilder.loadTexts:
    z9100on.setStatus("current")
_Z9264Fon_ObjectIdentity = ObjectIdentity
z9264Fon = _Z9264Fon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 3, 2)
)
if mibBuilder.loadTexts:
    z9264Fon.setStatus("current")
_Z9232Fon_ObjectIdentity = ObjectIdentity
z9232Fon = _Z9232Fon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 3, 3)
)
if mibBuilder.loadTexts:
    z9232Fon.setStatus("current")
_Z9332Fon_ObjectIdentity = ObjectIdentity
z9332Fon = _Z9332Fon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 3, 4)
)
if mibBuilder.loadTexts:
    z9332Fon.setStatus("current")
_Os10NSeriesProducts_ObjectIdentity = ObjectIdentity
os10NSeriesProducts = _Os10NSeriesProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 4)
)
if mibBuilder.loadTexts:
    os10NSeriesProducts.setStatus("current")
_N3248TEon_ObjectIdentity = ObjectIdentity
n3248TEon = _N3248TEon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 2, 4, 1)
)
if mibBuilder.loadTexts:
    n3248TEon.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELLEMC-OS10-PRODUCTS-MIB",
    **{"os10Products": os10Products,
       "os10SSeriesProducts": os10SSeriesProducts,
       "s6000on": s6000on,
       "s4048on": s4048on,
       "s4048Ton": s4048Ton,
       "s3048on": s3048on,
       "s6010on": s6010on,
       "s4148Fon": s4148Fon,
       "s4128Fon": s4128Fon,
       "s4148Ton": s4148Ton,
       "s4128Ton": s4128Ton,
       "s4148FEon": s4148FEon,
       "s4148Uon": s4148Uon,
       "s4200on": s4200on,
       "s5148Fon": s5148Fon,
       "s4248FBon": s4248FBon,
       "s4248FBLon": s4248FBLon,
       "s4112Fon": s4112Fon,
       "s4112Ton": s4112Ton,
       "s5212Fon": s5212Fon,
       "s5224Fon": s5224Fon,
       "s5232Fon": s5232Fon,
       "s5248Fon": s5248Fon,
       "s5296Fon": s5296Fon,
       "os10MSeriesProducts": os10MSeriesProducts,
       "mx5108Non": mx5108Non,
       "mx9116Non": mx9116Non,
       "os10ZSeriesProducts": os10ZSeriesProducts,
       "z9100on": z9100on,
       "z9264Fon": z9264Fon,
       "z9232Fon": z9232Fon,
       "z9332Fon": z9332Fon,
       "os10NSeriesProducts": os10NSeriesProducts,
       "n3248TEon": n3248TEon}
)
