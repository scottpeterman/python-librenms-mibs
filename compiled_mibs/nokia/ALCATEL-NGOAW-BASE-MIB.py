# SNMP MIB module (ALCATEL-NGOAW-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\stellar\ALCATEL-NGOAW-BASE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:16:42 2025
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

alcatelNGOAWBaseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802)
)
if mibBuilder.loadTexts:
    alcatelNGOAWBaseMIB.setRevisions(
        ("2016-09-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Alcatel_ObjectIdentity = ObjectIdentity
alcatel = _Alcatel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486)
)
if mibBuilder.loadTexts:
    alcatel.setStatus("current")
_AlcatelNGOAWManagement_ObjectIdentity = ObjectIdentity
alcatelNGOAWManagement = _AlcatelNGOAWManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1)
)
if mibBuilder.loadTexts:
    alcatelNGOAWManagement.setStatus("current")
_ManagementNGOAWHardware_ObjectIdentity = ObjectIdentity
managementNGOAWHardware = _ManagementNGOAWHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1)
)
if mibBuilder.loadTexts:
    managementNGOAWHardware.setStatus("current")
_HardwareNGOAWEntities_ObjectIdentity = ObjectIdentity
hardwareNGOAWEntities = _HardwareNGOAWEntities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hardwareNGOAWEntities.setStatus("current")
_HardwareNGOAWDevices_ObjectIdentity = ObjectIdentity
hardwareNGOAWDevices = _HardwareNGOAWDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hardwareNGOAWDevices.setStatus("current")
_ManagementNGOAWSoftware_ObjectIdentity = ObjectIdentity
managementNGOAWSoftware = _ManagementNGOAWSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 2)
)
if mibBuilder.loadTexts:
    managementNGOAWSoftware.setStatus("current")
_SoftwareNGOAWEntities_ObjectIdentity = ObjectIdentity
softwareNGOAWEntities = _SoftwareNGOAWEntities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 2, 1)
)
if mibBuilder.loadTexts:
    softwareNGOAWEntities.setStatus("current")
_SoftwareNGOAWServices_ObjectIdentity = ObjectIdentity
softwareNGOAWServices = _SoftwareNGOAWServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 2, 2)
)
if mibBuilder.loadTexts:
    softwareNGOAWServices.setStatus("current")
_ManagementNGOAWAgentCapabilities_ObjectIdentity = ObjectIdentity
managementNGOAWAgentCapabilities = _ManagementNGOAWAgentCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 802, 1, 4)
)
if mibBuilder.loadTexts:
    managementNGOAWAgentCapabilities.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-NGOAW-BASE-MIB",
    **{"alcatel": alcatel,
       "alcatelNGOAWBaseMIB": alcatelNGOAWBaseMIB,
       "alcatelNGOAWManagement": alcatelNGOAWManagement,
       "managementNGOAWHardware": managementNGOAWHardware,
       "hardwareNGOAWEntities": hardwareNGOAWEntities,
       "hardwareNGOAWDevices": hardwareNGOAWDevices,
       "managementNGOAWSoftware": managementNGOAWSoftware,
       "softwareNGOAWEntities": softwareNGOAWEntities,
       "softwareNGOAWServices": softwareNGOAWServices,
       "managementNGOAWAgentCapabilities": managementNGOAWAgentCapabilities}
)
