# SNMP MIB module (SILVERPEAK-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\silverpeak\SILVERPEAK-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:08 2025
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

silverpeakNW = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23867)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SilverpeakProducts_ObjectIdentity = ObjectIdentity
silverpeakProducts = _SilverpeakProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 1)
)
if mibBuilder.loadTexts:
    silverpeakProducts.setStatus("current")
_SilverpeakModules_ObjectIdentity = ObjectIdentity
silverpeakModules = _SilverpeakModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 2)
)
if mibBuilder.loadTexts:
    silverpeakModules.setStatus("current")
_SilverpeakMgmt_ObjectIdentity = ObjectIdentity
silverpeakMgmt = _SilverpeakMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 3)
)
if mibBuilder.loadTexts:
    silverpeakMgmt.setStatus("current")
_SilverpeakNotifications_ObjectIdentity = ObjectIdentity
silverpeakNotifications = _SilverpeakNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 4)
)
if mibBuilder.loadTexts:
    silverpeakNotifications.setStatus("current")
_SilverpeakAgentCapability_ObjectIdentity = ObjectIdentity
silverpeakAgentCapability = _SilverpeakAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23867, 5)
)
if mibBuilder.loadTexts:
    silverpeakAgentCapability.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SILVERPEAK-SMI",
    **{"silverpeakNW": silverpeakNW,
       "silverpeakProducts": silverpeakProducts,
       "silverpeakModules": silverpeakModules,
       "silverpeakMgmt": silverpeakMgmt,
       "silverpeakNotifications": silverpeakNotifications,
       "silverpeakAgentCapability": silverpeakAgentCapability}
)
