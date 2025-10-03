# SNMP MIB module (BCN-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecatnetworks\BCN-SMI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:24 2025
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

(bluecatnetworks,) = mibBuilder.importSymbols(
    "BLUECATNETWORKS-MIB",
    "bluecatnetworks")

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

bcnSMI = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 4, 1)
)
if mibBuilder.loadTexts:
    bcnSMI.setRevisions(
        ("2010-11-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcnProducts_ObjectIdentity = ObjectIdentity
bcnProducts = _BcnProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 2)
)
if mibBuilder.loadTexts:
    bcnProducts.setStatus("current")
_BcnMgmt_ObjectIdentity = ObjectIdentity
bcnMgmt = _BcnMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3)
)
if mibBuilder.loadTexts:
    bcnMgmt.setStatus("current")
_BcnServices_ObjectIdentity = ObjectIdentity
bcnServices = _BcnServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1)
)
if mibBuilder.loadTexts:
    bcnServices.setStatus("current")
_BcnModules_ObjectIdentity = ObjectIdentity
bcnModules = _BcnModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 4)
)
if mibBuilder.loadTexts:
    bcnModules.setStatus("current")
_BcnExperimental_ObjectIdentity = ObjectIdentity
bcnExperimental = _BcnExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 5)
)
if mibBuilder.loadTexts:
    bcnExperimental.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCN-SMI-MIB",
    **{"bcnProducts": bcnProducts,
       "bcnMgmt": bcnMgmt,
       "bcnServices": bcnServices,
       "bcnModules": bcnModules,
       "bcnSMI": bcnSMI,
       "bcnExperimental": bcnExperimental}
)
