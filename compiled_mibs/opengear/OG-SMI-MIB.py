# SNMP MIB module (OG-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\opengear\OG-SMI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:24 2025
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

opengear = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049)
)
if mibBuilder.loadTexts:
    opengear.setRevisions(
        ("2018-06-15 00:00",
         "2013-11-15 00:00",
         "2013-08-11 00:00",
         "2010-03-22 11:27",
         "2005-02-24 01:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgProducts_ObjectIdentity = ObjectIdentity
ogProducts = _OgProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1)
)
if mibBuilder.loadTexts:
    ogProducts.setStatus("current")
_OgLegacyMgmt_ObjectIdentity = ObjectIdentity
ogLegacyMgmt = _OgLegacyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2)
)
if mibBuilder.loadTexts:
    ogLegacyMgmt.setStatus("current")
_OgExperimental_ObjectIdentity = ObjectIdentity
ogExperimental = _OgExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 3)
)
if mibBuilder.loadTexts:
    ogExperimental.setStatus("current")
_OgInternal_ObjectIdentity = ObjectIdentity
ogInternal = _OgInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 4)
)
if mibBuilder.loadTexts:
    ogInternal.setStatus("current")
_OgReserved1_ObjectIdentity = ObjectIdentity
ogReserved1 = _OgReserved1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 5)
)
if mibBuilder.loadTexts:
    ogReserved1.setStatus("current")
_OgReserved2_ObjectIdentity = ObjectIdentity
ogReserved2 = _OgReserved2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 6)
)
if mibBuilder.loadTexts:
    ogReserved2.setStatus("current")
_OtherEnterprises_ObjectIdentity = ObjectIdentity
otherEnterprises = _OtherEnterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 7)
)
if mibBuilder.loadTexts:
    otherEnterprises.setStatus("current")
_OgAgentCapability_ObjectIdentity = ObjectIdentity
ogAgentCapability = _OgAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 8)
)
if mibBuilder.loadTexts:
    ogAgentCapability.setStatus("current")
_OgConfig_ObjectIdentity = ObjectIdentity
ogConfig = _OgConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 9)
)
if mibBuilder.loadTexts:
    ogConfig.setStatus("current")
_OgMgmt_ObjectIdentity = ObjectIdentity
ogMgmt = _OgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10)
)
if mibBuilder.loadTexts:
    ogMgmt.setStatus("current")
_OgModules_ObjectIdentity = ObjectIdentity
ogModules = _OgModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 11)
)
if mibBuilder.loadTexts:
    ogModules.setStatus("current")
_OgSpecific_ObjectIdentity = ObjectIdentity
ogSpecific = _OgSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 18)
)
if mibBuilder.loadTexts:
    ogSpecific.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-SMI-MIB",
    **{"opengear": opengear,
       "ogProducts": ogProducts,
       "ogLegacyMgmt": ogLegacyMgmt,
       "ogExperimental": ogExperimental,
       "ogInternal": ogInternal,
       "ogReserved1": ogReserved1,
       "ogReserved2": ogReserved2,
       "otherEnterprises": otherEnterprises,
       "ogAgentCapability": ogAgentCapability,
       "ogConfig": ogConfig,
       "ogMgmt": ogMgmt,
       "ogModules": ogModules,
       "ogSpecific": ogSpecific}
)
