# SNMP MIB module (BCN-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecatnetworks\BCN-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:29 2025
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

(bcnModules,
 bcnProducts) = mibBuilder.importSymbols(
    "BCN-SMI-MIB",
    "bcnModules",
    "bcnProducts")

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

bcnProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 4, 2)
)
if mibBuilder.loadTexts:
    bcnProductsMIB.setRevisions(
        ("2010-11-30 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcnProductsAdonis_ObjectIdentity = ObjectIdentity
bcnProductsAdonis = _BcnProductsAdonis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 2, 1)
)
_BcnProductsProteus_ObjectIdentity = ObjectIdentity
bcnProductsProteus = _BcnProductsProteus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 2, 2)
)
_BcnProductsAdonis250_ObjectIdentity = ObjectIdentity
bcnProductsAdonis250 = _BcnProductsAdonis250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 2, 3)
)
_BcnProductsAdonis750_ObjectIdentity = ObjectIdentity
bcnProductsAdonis750 = _BcnProductsAdonis750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 2, 4)
)
_BcnProductsAdonis1000_ObjectIdentity = ObjectIdentity
bcnProductsAdonis1000 = _BcnProductsAdonis1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 2, 5)
)
_BcnProductsPoteus2150_ObjectIdentity = ObjectIdentity
bcnProductsPoteus2150 = _BcnProductsPoteus2150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 2, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCN-PRODUCTS-MIB",
    **{"bcnProductsAdonis": bcnProductsAdonis,
       "bcnProductsProteus": bcnProductsProteus,
       "bcnProductsAdonis250": bcnProductsAdonis250,
       "bcnProductsAdonis750": bcnProductsAdonis750,
       "bcnProductsAdonis1000": bcnProductsAdonis1000,
       "bcnProductsPoteus2150": bcnProductsPoteus2150,
       "bcnProductsMIB": bcnProductsMIB}
)
