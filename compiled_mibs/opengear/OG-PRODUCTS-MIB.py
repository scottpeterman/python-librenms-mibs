# SNMP MIB module (OG-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\opengear\OG-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:29 2025
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

(ogModules,
 ogProducts) = mibBuilder.importSymbols(
    "OG-SMI-MIB",
    "ogModules",
    "ogProducts")

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

ogProductsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 11, 2)
)
if mibBuilder.loadTexts:
    ogProductsMib.setRevisions(
        ("2023-01-18 00:00",
         "2020-05-20 00:00",
         "2018-06-15 00:00",
         "2016-06-27 00:00",
         "2016-02-10 00:00",
         "2015-06-02 00:00",
         "2013-08-11 00:00",
         "2011-08-15 01:23",
         "2010-04-15 11:27")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgCM4001_ObjectIdentity = ObjectIdentity
ogCM4001 = _OgCM4001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 1)
)
_OgCM4002_ObjectIdentity = ObjectIdentity
ogCM4002 = _OgCM4002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 2)
)
_OgCM4008_ObjectIdentity = ObjectIdentity
ogCM4008 = _OgCM4008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 3)
)
_OgCM41xx_ObjectIdentity = ObjectIdentity
ogCM41xx = _OgCM41xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 10)
)
_OgCM71xx_ObjectIdentity = ObjectIdentity
ogCM71xx = _OgCM71xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 11)
)
_OgCM7196_ObjectIdentity = ObjectIdentity
ogCM7196 = _OgCM7196_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 12)
)
_OgSD4001_ObjectIdentity = ObjectIdentity
ogSD4001 = _OgSD4001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 20)
)
_OgSD4002_ObjectIdentity = ObjectIdentity
ogSD4002 = _OgSD4002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 21)
)
_OgSD4008_ObjectIdentity = ObjectIdentity
ogSD4008 = _OgSD4008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 22)
)
_OgSD4001DW_ObjectIdentity = ObjectIdentity
ogSD4001DW = _OgSD4001DW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 23)
)
_OgSD4002DX_ObjectIdentity = ObjectIdentity
ogSD4002DX = _OgSD4002DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 24)
)
_OgCD_ObjectIdentity = ObjectIdentity
ogCD = _OgCD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 30)
)
_OgCMx86_ObjectIdentity = ObjectIdentity
ogCMx86 = _OgCMx86_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 31)
)
_OgCMS61xx_ObjectIdentity = ObjectIdentity
ogCMS61xx = _OgCMS61xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 40)
)
_OgLighthouse_ObjectIdentity = ObjectIdentity
ogLighthouse = _OgLighthouse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 41)
)
_OgLighthouse5_ObjectIdentity = ObjectIdentity
ogLighthouse5 = _OgLighthouse5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 42)
)
_OgIM4004_ObjectIdentity = ObjectIdentity
ogIM4004 = _OgIM4004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 50)
)
_OgIM42xx_ObjectIdentity = ObjectIdentity
ogIM42xx = _OgIM42xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 60)
)
_OgIM72xx_ObjectIdentity = ObjectIdentity
ogIM72xx = _OgIM72xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 61)
)
_OgKCS61xx_ObjectIdentity = ObjectIdentity
ogKCS61xx = _OgKCS61xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 70)
)
_OgACM500x_ObjectIdentity = ObjectIdentity
ogACM500x = _OgACM500x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 80)
)
_OgACM550x_ObjectIdentity = ObjectIdentity
ogACM550x = _OgACM550x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 81)
)
_OgACM700x_ObjectIdentity = ObjectIdentity
ogACM700x = _OgACM700x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 90)
)
_OgACM70045_ObjectIdentity = ObjectIdentity
ogACM70045 = _OgACM70045_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 91)
)
_OgOperationsManager_ObjectIdentity = ObjectIdentity
ogOperationsManager = _OgOperationsManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 101)
)
_OgOM12xx_ObjectIdentity = ObjectIdentity
ogOM12xx = _OgOM12xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 110)
)
_OgOM22xx_ObjectIdentity = ObjectIdentity
ogOM22xx = _OgOM22xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 120)
)
_OgCM81xx_ObjectIdentity = ObjectIdentity
ogCM81xx = _OgCM81xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 130)
)
_OgEM80xx_ObjectIdentity = ObjectIdentity
ogEM80xx = _OgEM80xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1, 140)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-PRODUCTS-MIB",
    **{"ogCM4001": ogCM4001,
       "ogCM4002": ogCM4002,
       "ogCM4008": ogCM4008,
       "ogCM41xx": ogCM41xx,
       "ogCM71xx": ogCM71xx,
       "ogCM7196": ogCM7196,
       "ogSD4001": ogSD4001,
       "ogSD4002": ogSD4002,
       "ogSD4008": ogSD4008,
       "ogSD4001DW": ogSD4001DW,
       "ogSD4002DX": ogSD4002DX,
       "ogCD": ogCD,
       "ogCMx86": ogCMx86,
       "ogCMS61xx": ogCMS61xx,
       "ogLighthouse": ogLighthouse,
       "ogLighthouse5": ogLighthouse5,
       "ogIM4004": ogIM4004,
       "ogIM42xx": ogIM42xx,
       "ogIM72xx": ogIM72xx,
       "ogKCS61xx": ogKCS61xx,
       "ogACM500x": ogACM500x,
       "ogACM550x": ogACM550x,
       "ogACM700x": ogACM700x,
       "ogACM70045": ogACM70045,
       "ogOperationsManager": ogOperationsManager,
       "ogOM12xx": ogOM12xx,
       "ogOM22xx": ogOM22xx,
       "ogCM81xx": ogCM81xx,
       "ogEM80xx": ogEM80xx,
       "ogProductsMib": ogProductsMib}
)
