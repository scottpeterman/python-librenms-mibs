# SNMP MIB module (A10-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\a10\A10-COMMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:13:59 2025
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

a10 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22610)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A10Products_ObjectIdentity = ObjectIdentity
a10Products = _A10Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1)
)
if mibBuilder.loadTexts:
    a10Products.setStatus("current")
_A10IDsentrie_ObjectIdentity = ObjectIdentity
a10IDsentrie = _A10IDsentrie_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 1)
)
if mibBuilder.loadTexts:
    a10IDsentrie.setStatus("current")
_A10IDsentrie1000_ObjectIdentity = ObjectIdentity
a10IDsentrie1000 = _A10IDsentrie1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 1, 1)
)
if mibBuilder.loadTexts:
    a10IDsentrie1000.setStatus("current")
_A10StealthWatch_ObjectIdentity = ObjectIdentity
a10StealthWatch = _A10StealthWatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 1, 2)
)
if mibBuilder.loadTexts:
    a10StealthWatch.setStatus("current")
_A10RetiEntity1000_ObjectIdentity = ObjectIdentity
a10RetiEntity1000 = _A10RetiEntity1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 1, 3)
)
if mibBuilder.loadTexts:
    a10RetiEntity1000.setStatus("current")
_A10EX_ObjectIdentity = ObjectIdentity
a10EX = _A10EX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 2)
)
if mibBuilder.loadTexts:
    a10EX.setStatus("current")
_A10EX2100_ObjectIdentity = ObjectIdentity
a10EX2100 = _A10EX2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 2, 1)
)
if mibBuilder.loadTexts:
    a10EX2100.setStatus("current")
_A10EX2180_ObjectIdentity = ObjectIdentity
a10EX2180 = _A10EX2180_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 2, 2)
)
if mibBuilder.loadTexts:
    a10EX2180.setStatus("current")
_A10EX2200_ObjectIdentity = ObjectIdentity
a10EX2200 = _A10EX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 2, 3)
)
if mibBuilder.loadTexts:
    a10EX2200.setStatus("current")
_A10EX2280_ObjectIdentity = ObjectIdentity
a10EX2280 = _A10EX2280_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 2, 4)
)
if mibBuilder.loadTexts:
    a10EX2280.setStatus("current")
_A10AX_ObjectIdentity = ObjectIdentity
a10AX = _A10AX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3)
)
if mibBuilder.loadTexts:
    a10AX.setStatus("current")
_A10AX2100_ObjectIdentity = ObjectIdentity
a10AX2100 = _A10AX2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 1)
)
if mibBuilder.loadTexts:
    a10AX2100.setStatus("current")
_A10AX3100_ObjectIdentity = ObjectIdentity
a10AX3100 = _A10AX3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 2)
)
if mibBuilder.loadTexts:
    a10AX3100.setStatus("current")
_A10AX3200_ObjectIdentity = ObjectIdentity
a10AX3200 = _A10AX3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 3)
)
if mibBuilder.loadTexts:
    a10AX3200.setStatus("current")
_A10AX2200_ObjectIdentity = ObjectIdentity
a10AX2200 = _A10AX2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 4)
)
if mibBuilder.loadTexts:
    a10AX2200.setStatus("current")
_A10AX2000_ObjectIdentity = ObjectIdentity
a10AX2000 = _A10AX2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 5)
)
if mibBuilder.loadTexts:
    a10AX2000.setStatus("current")
_A10AX1000_ObjectIdentity = ObjectIdentity
a10AX1000 = _A10AX1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 6)
)
if mibBuilder.loadTexts:
    a10AX1000.setStatus("current")
_A10AX5200_ObjectIdentity = ObjectIdentity
a10AX5200 = _A10AX5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 7)
)
if mibBuilder.loadTexts:
    a10AX5200.setStatus("current")
_A10AX2500_ObjectIdentity = ObjectIdentity
a10AX2500 = _A10AX2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 8)
)
if mibBuilder.loadTexts:
    a10AX2500.setStatus("current")
_A10AX2600_ObjectIdentity = ObjectIdentity
a10AX2600 = _A10AX2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 9)
)
if mibBuilder.loadTexts:
    a10AX2600.setStatus("current")
_A10AX3000_ObjectIdentity = ObjectIdentity
a10AX3000 = _A10AX3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 10)
)
if mibBuilder.loadTexts:
    a10AX3000.setStatus("current")
_A10HitachiBladeServer_ObjectIdentity = ObjectIdentity
a10HitachiBladeServer = _A10HitachiBladeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 11)
)
if mibBuilder.loadTexts:
    a10HitachiBladeServer.setStatus("current")
_A10AX5100_ObjectIdentity = ObjectIdentity
a10AX5100 = _A10AX5100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 12)
)
if mibBuilder.loadTexts:
    a10AX5100.setStatus("current")
_A10SoftAX_ObjectIdentity = ObjectIdentity
a10SoftAX = _A10SoftAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 13)
)
if mibBuilder.loadTexts:
    a10SoftAX.setStatus("current")
_A10AX3030_ObjectIdentity = ObjectIdentity
a10AX3030 = _A10AX3030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 14)
)
if mibBuilder.loadTexts:
    a10AX3030.setStatus("current")
_A10AX1030_ObjectIdentity = ObjectIdentity
a10AX1030 = _A10AX1030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 15)
)
if mibBuilder.loadTexts:
    a10AX1030.setStatus("current")
_A10AX3200_12_ObjectIdentity = ObjectIdentity
a10AX3200_12 = _A10AX3200_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 16)
)
if mibBuilder.loadTexts:
    a10AX3200_12.setStatus("current")
_A10AX3400_ObjectIdentity = ObjectIdentity
a10AX3400 = _A10AX3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 17)
)
if mibBuilder.loadTexts:
    a10AX3400.setStatus("current")
_A10AX3530_ObjectIdentity = ObjectIdentity
a10AX3530 = _A10AX3530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 18)
)
if mibBuilder.loadTexts:
    a10AX3530.setStatus("current")
_A10AX5630_ObjectIdentity = ObjectIdentity
a10AX5630 = _A10AX5630_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 19)
)
if mibBuilder.loadTexts:
    a10AX5630.setStatus("current")
_A10TH6430_ObjectIdentity = ObjectIdentity
a10TH6430 = _A10TH6430_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 20)
)
if mibBuilder.loadTexts:
    a10TH6430.setStatus("current")
_A10TH5430_ObjectIdentity = ObjectIdentity
a10TH5430 = _A10TH5430_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 21)
)
if mibBuilder.loadTexts:
    a10TH5430.setStatus("current")
_A10TH3030S_ObjectIdentity = ObjectIdentity
a10TH3030S = _A10TH3030S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 22)
)
if mibBuilder.loadTexts:
    a10TH3030S.setStatus("current")
_A10TH1030S_ObjectIdentity = ObjectIdentity
a10TH1030S = _A10TH1030S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 23)
)
if mibBuilder.loadTexts:
    a10TH1030S.setStatus("current")
_A10TH930S_ObjectIdentity = ObjectIdentity
a10TH930S = _A10TH930S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 3, 24)
)
if mibBuilder.loadTexts:
    a10TH930S.setStatus("current")
_A10CentMgmt_ObjectIdentity = ObjectIdentity
a10CentMgmt = _A10CentMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 4)
)
if mibBuilder.loadTexts:
    a10CentMgmt.setStatus("current")
_A10AGA1_ObjectIdentity = ObjectIdentity
a10AGA1 = _A10AGA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 4, 1)
)
if mibBuilder.loadTexts:
    a10AGA1.setStatus("current")
_A10AGA5000_ObjectIdentity = ObjectIdentity
a10AGA5000 = _A10AGA5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 4, 2)
)
if mibBuilder.loadTexts:
    a10AGA5000.setStatus("current")
_A10SoftAGA_ObjectIdentity = ObjectIdentity
a10SoftAGA = _A10SoftAGA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 1, 4, 3)
)
if mibBuilder.loadTexts:
    a10SoftAGA.setStatus("current")
_A10Mgmt_ObjectIdentity = ObjectIdentity
a10Mgmt = _A10Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2)
)
if mibBuilder.loadTexts:
    a10Mgmt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A10-COMMON-MIB",
    **{"a10": a10,
       "a10Products": a10Products,
       "a10IDsentrie": a10IDsentrie,
       "a10IDsentrie1000": a10IDsentrie1000,
       "a10StealthWatch": a10StealthWatch,
       "a10RetiEntity1000": a10RetiEntity1000,
       "a10EX": a10EX,
       "a10EX2100": a10EX2100,
       "a10EX2180": a10EX2180,
       "a10EX2200": a10EX2200,
       "a10EX2280": a10EX2280,
       "a10AX": a10AX,
       "a10AX2100": a10AX2100,
       "a10AX3100": a10AX3100,
       "a10AX3200": a10AX3200,
       "a10AX2200": a10AX2200,
       "a10AX2000": a10AX2000,
       "a10AX1000": a10AX1000,
       "a10AX5200": a10AX5200,
       "a10AX2500": a10AX2500,
       "a10AX2600": a10AX2600,
       "a10AX3000": a10AX3000,
       "a10HitachiBladeServer": a10HitachiBladeServer,
       "a10AX5100": a10AX5100,
       "a10SoftAX": a10SoftAX,
       "a10AX3030": a10AX3030,
       "a10AX1030": a10AX1030,
       "a10AX3200-12": a10AX3200_12,
       "a10AX3400": a10AX3400,
       "a10AX3530": a10AX3530,
       "a10AX5630": a10AX5630,
       "a10TH6430": a10TH6430,
       "a10TH5430": a10TH5430,
       "a10TH3030S": a10TH3030S,
       "a10TH1030S": a10TH1030S,
       "a10TH930S": a10TH930S,
       "a10CentMgmt": a10CentMgmt,
       "a10AGA1": a10AGA1,
       "a10AGA5000": a10AGA5000,
       "a10SoftAGA": a10SoftAGA,
       "a10Mgmt": a10Mgmt}
)
