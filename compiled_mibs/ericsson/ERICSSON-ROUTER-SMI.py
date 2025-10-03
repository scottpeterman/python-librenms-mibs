# SNMP MIB module (ERICSSON-ROUTER-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\ERICSSON-ROUTER-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:26 2025
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

(ericsson,) = mibBuilder.importSymbols(
    "ERICSSON-TOP-MIB",
    "ericsson")

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

eriRouterSMI = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218)
)
if mibBuilder.loadTexts:
    eriRouterSMI.setRevisions(
        ("2015-01-14 18:00",
         "2011-01-19 18:00",
         "2002-06-06 00:00",
         "2001-06-27 00:00",
         "1998-04-18 23:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EriRouterProducts_ObjectIdentity = ObjectIdentity
eriRouterProducts = _EriRouterProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 1)
)
if mibBuilder.loadTexts:
    eriRouterProducts.setStatus("current")
_EriRouterMgmt_ObjectIdentity = ObjectIdentity
eriRouterMgmt = _EriRouterMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 2)
)
if mibBuilder.loadTexts:
    eriRouterMgmt.setStatus("current")
_EriRouterExperiment_ObjectIdentity = ObjectIdentity
eriRouterExperiment = _EriRouterExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 3)
)
if mibBuilder.loadTexts:
    eriRouterExperiment.setStatus("current")
_EriRouterCapabilities_ObjectIdentity = ObjectIdentity
eriRouterCapabilities = _EriRouterCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 4)
)
if mibBuilder.loadTexts:
    eriRouterCapabilities.setStatus("current")
_EriRouterModules_ObjectIdentity = ObjectIdentity
eriRouterModules = _EriRouterModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 5)
)
if mibBuilder.loadTexts:
    eriRouterModules.setStatus("current")
_EriRouterEntities_ObjectIdentity = ObjectIdentity
eriRouterEntities = _EriRouterEntities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 6)
)
if mibBuilder.loadTexts:
    eriRouterEntities.setStatus("current")
_EriRouterInternal_ObjectIdentity = ObjectIdentity
eriRouterInternal = _EriRouterInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 7)
)
if mibBuilder.loadTexts:
    eriRouterInternal.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERICSSON-ROUTER-SMI",
    **{"eriRouterSMI": eriRouterSMI,
       "eriRouterProducts": eriRouterProducts,
       "eriRouterMgmt": eriRouterMgmt,
       "eriRouterExperiment": eriRouterExperiment,
       "eriRouterCapabilities": eriRouterCapabilities,
       "eriRouterModules": eriRouterModules,
       "eriRouterEntities": eriRouterEntities,
       "eriRouterInternal": eriRouterInternal}
)
