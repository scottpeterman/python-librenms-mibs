# SNMP MIB module (CALIX-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\calix\CALIX-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 11:22:45 2025
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

calixNetworks = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321)
)
if mibBuilder.loadTexts:
    calixNetworks.setRevisions(
        ("2000-08-31 00:26",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CalixRegistrations_ObjectIdentity = ObjectIdentity
calixRegistrations = _CalixRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1)
)
if mibBuilder.loadTexts:
    calixRegistrations.setStatus("current")
_CalixModules_ObjectIdentity = ObjectIdentity
calixModules = _CalixModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 1)
)
if mibBuilder.loadTexts:
    calixModules.setStatus("current")
_CalixProducts_ObjectIdentity = ObjectIdentity
calixProducts = _CalixProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2)
)
if mibBuilder.loadTexts:
    calixProducts.setStatus("current")
_CalixManagement_ObjectIdentity = ObjectIdentity
calixManagement = _CalixManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2)
)
if mibBuilder.loadTexts:
    calixManagement.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CALIX-SMI",
    **{"calixNetworks": calixNetworks,
       "calixRegistrations": calixRegistrations,
       "calixModules": calixModules,
       "calixProducts": calixProducts,
       "calixManagement": calixManagement}
)
