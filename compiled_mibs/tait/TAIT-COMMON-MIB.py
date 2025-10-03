# SNMP MIB module (TAIT-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tait\TAIT-COMMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:32 2025
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

taitCommonRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 1, 1, 1)
)
if mibBuilder.loadTexts:
    taitCommonRegModule.setRevisions(
        ("2012-02-20 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tait_ObjectIdentity = ObjectIdentity
tait = _Tait_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570)
)
if mibBuilder.loadTexts:
    tait.setStatus("current")
_TaitRegistrations_ObjectIdentity = ObjectIdentity
taitRegistrations = _TaitRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 1)
)
if mibBuilder.loadTexts:
    taitRegistrations.setStatus("current")
_TaitModules_ObjectIdentity = ObjectIdentity
taitModules = _TaitModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 1, 1)
)
if mibBuilder.loadTexts:
    taitModules.setStatus("current")
_TaitGeneric_ObjectIdentity = ObjectIdentity
taitGeneric = _TaitGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2)
)
if mibBuilder.loadTexts:
    taitGeneric.setStatus("current")
_TaitProducts_ObjectIdentity = ObjectIdentity
taitProducts = _TaitProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 3)
)
if mibBuilder.loadTexts:
    taitProducts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TAIT-COMMON-MIB",
    **{"tait": tait,
       "taitRegistrations": taitRegistrations,
       "taitModules": taitModules,
       "taitCommonRegModule": taitCommonRegModule,
       "taitGeneric": taitGeneric,
       "taitProducts": taitProducts}
)
