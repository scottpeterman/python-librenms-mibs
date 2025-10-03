# SNMP MIB module (MCAFEE-INTRUVERT-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\trellix\MCAFEE-INTRUVERT-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:46 2025
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

mcafee_intruvert = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8962)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IvConventions_ObjectIdentity = ObjectIdentity
ivConventions = _IvConventions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 1)
)
if mibBuilder.loadTexts:
    ivConventions.setStatus("current")
_IvProducts_ObjectIdentity = ObjectIdentity
ivProducts = _IvProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2)
)
if mibBuilder.loadTexts:
    ivProducts.setStatus("current")
_IvInventory_ObjectIdentity = ObjectIdentity
ivInventory = _IvInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 3)
)
if mibBuilder.loadTexts:
    ivInventory.setStatus("current")
_MatdProducts_ObjectIdentity = ObjectIdentity
matdProducts = _MatdProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 4)
)
if mibBuilder.loadTexts:
    matdProducts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MCAFEE-INTRUVERT-SMI",
    **{"mcafee-intruvert": mcafee_intruvert,
       "ivConventions": ivConventions,
       "ivProducts": ivProducts,
       "ivInventory": ivInventory,
       "matdProducts": matdProducts}
)
