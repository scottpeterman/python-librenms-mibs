# SNMP MIB module (COLUBRIS-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\hpmsm\COLUBRIS-PRODUCTS-MIB.my
# Produced by pysmi-1.6.2 at Thu Oct  2 11:52:00 2025
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

(colubrisModules,
 colubrisProducts) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisModules",
    "colubrisProducts")

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

colubrisProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 4, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisCN1000_ObjectIdentity = ObjectIdentity
colubrisCN1000 = _ColubrisCN1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 1)
)
_ColubrisCN1000HEREUARE_ObjectIdentity = ObjectIdentity
colubrisCN1000HEREUARE = _ColubrisCN1000HEREUARE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 2)
)
_ColubrisCN1050_ObjectIdentity = ObjectIdentity
colubrisCN1050 = _ColubrisCN1050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 3)
)
_ColubrisCN1054_ObjectIdentity = ObjectIdentity
colubrisCN1054 = _ColubrisCN1054_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 4)
)
_ColubrisCN3000_ObjectIdentity = ObjectIdentity
colubrisCN3000 = _ColubrisCN3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 5)
)
_ColubrisCN100HEREUARE_ObjectIdentity = ObjectIdentity
colubrisCN100HEREUARE = _ColubrisCN100HEREUARE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 6)
)
_ColubrisCN100TRAVELNET_ObjectIdentity = ObjectIdentity
colubrisCN100TRAVELNET = _ColubrisCN100TRAVELNET_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 7)
)
_ColubrisCN300_ObjectIdentity = ObjectIdentity
colubrisCN300 = _ColubrisCN300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 8)
)
_ColubrisCN1150_ObjectIdentity = ObjectIdentity
colubrisCN1150 = _ColubrisCN1150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 9)
)
_ColubrisCN3100_ObjectIdentity = ObjectIdentity
colubrisCN3100 = _ColubrisCN3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 10)
)
_ColubrisCN1000LIGHT_ObjectIdentity = ObjectIdentity
colubrisCN1000LIGHT = _ColubrisCN1000LIGHT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 11)
)
_ColubrisCN3500_ObjectIdentity = ObjectIdentity
colubrisCN3500 = _ColubrisCN3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 12)
)
_ColubrisCN310_ObjectIdentity = ObjectIdentity
colubrisCN310 = _ColubrisCN310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 13)
)
_ColubrisCN1500_ObjectIdentity = ObjectIdentity
colubrisCN1500 = _ColubrisCN1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 14)
)
_ColubrisCN1550_ObjectIdentity = ObjectIdentity
colubrisCN1550 = _ColubrisCN1550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 15)
)
_ColubrisCN3200_ObjectIdentity = ObjectIdentity
colubrisCN3200 = _ColubrisCN3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 16)
)
_ColubrisCN1200_ObjectIdentity = ObjectIdentity
colubrisCN1200 = _ColubrisCN1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 17)
)
_ColubrisCN1250_ObjectIdentity = ObjectIdentity
colubrisCN1250 = _ColubrisCN1250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 18)
)
_ColubrisCN320SE_ObjectIdentity = ObjectIdentity
colubrisCN320SE = _ColubrisCN320SE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 19)
)
_ColubrisCN320_ObjectIdentity = ObjectIdentity
colubrisCN320 = _ColubrisCN320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 20)
)
_ColubrisCN1220_ObjectIdentity = ObjectIdentity
colubrisCN1220 = _ColubrisCN1220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 21)
)
_ColubrisCN200_ObjectIdentity = ObjectIdentity
colubrisCN200 = _ColubrisCN200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 22)
)
_ColubrisCN3300_ObjectIdentity = ObjectIdentity
colubrisCN3300 = _ColubrisCN3300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 23)
)
_ColubrisCN330_ObjectIdentity = ObjectIdentity
colubrisCN330 = _ColubrisCN330_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 24)
)
_ColubrisMSC5200_ObjectIdentity = ObjectIdentity
colubrisMSC5200 = _ColubrisMSC5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 25)
)
_ColubrisWCB200_ObjectIdentity = ObjectIdentity
colubrisWCB200 = _ColubrisWCB200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 26)
)
_ColubrisMSC5500_ObjectIdentity = ObjectIdentity
colubrisMSC5500 = _ColubrisMSC5500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 27)
)
_ColubrisMAP625_ObjectIdentity = ObjectIdentity
colubrisMAP625 = _ColubrisMAP625_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 28)
)
_ColubrisMAP630_ObjectIdentity = ObjectIdentity
colubrisMAP630 = _ColubrisMAP630_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 29)
)
_ColubrisMAP330SENSOR_ObjectIdentity = ObjectIdentity
colubrisMAP330SENSOR = _ColubrisMAP330SENSOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 32)
)
_Colubris1300_ObjectIdentity = ObjectIdentity
colubris1300 = _Colubris1300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 33)
)
_Colubris1500_ObjectIdentity = ObjectIdentity
colubris1500 = _Colubris1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 34)
)
_ColubrisMSC5100_ObjectIdentity = ObjectIdentity
colubrisMSC5100 = _ColubrisMSC5100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 35)
)
_ColubrisMSM410_ObjectIdentity = ObjectIdentity
colubrisMSM410 = _ColubrisMSM410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1, 41)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-PRODUCTS-MIB",
    **{"colubrisCN1000": colubrisCN1000,
       "colubrisCN1000HEREUARE": colubrisCN1000HEREUARE,
       "colubrisCN1050": colubrisCN1050,
       "colubrisCN1054": colubrisCN1054,
       "colubrisCN3000": colubrisCN3000,
       "colubrisCN100HEREUARE": colubrisCN100HEREUARE,
       "colubrisCN100TRAVELNET": colubrisCN100TRAVELNET,
       "colubrisCN300": colubrisCN300,
       "colubrisCN1150": colubrisCN1150,
       "colubrisCN3100": colubrisCN3100,
       "colubrisCN1000LIGHT": colubrisCN1000LIGHT,
       "colubrisCN3500": colubrisCN3500,
       "colubrisCN310": colubrisCN310,
       "colubrisCN1500": colubrisCN1500,
       "colubrisCN1550": colubrisCN1550,
       "colubrisCN3200": colubrisCN3200,
       "colubrisCN1200": colubrisCN1200,
       "colubrisCN1250": colubrisCN1250,
       "colubrisCN320SE": colubrisCN320SE,
       "colubrisCN320": colubrisCN320,
       "colubrisCN1220": colubrisCN1220,
       "colubrisCN200": colubrisCN200,
       "colubrisCN3300": colubrisCN3300,
       "colubrisCN330": colubrisCN330,
       "colubrisMSC5200": colubrisMSC5200,
       "colubrisWCB200": colubrisWCB200,
       "colubrisMSC5500": colubrisMSC5500,
       "colubrisMAP625": colubrisMAP625,
       "colubrisMAP630": colubrisMAP630,
       "colubrisMAP330SENSOR": colubrisMAP330SENSOR,
       "colubris1300": colubris1300,
       "colubris1500": colubris1500,
       "colubrisMSC5100": colubrisMSC5100,
       "colubrisMSM410": colubrisMSM410,
       "colubrisProductsMIB": colubrisProductsMIB}
)
