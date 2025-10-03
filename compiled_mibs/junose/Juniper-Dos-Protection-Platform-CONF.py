# SNMP MIB module (Juniper-Dos-Protection-Platform-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\broken\Juniper-Dos-Protection-Platform-CONF
# Produced by pysmi-1.6.2 at Thu Oct  2 12:05:33 2025
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

(juniAgents,) = mibBuilder.importSymbols(
    "Juniper-Agents",
    "juniAgents")

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
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

juniDosProtectionPlatformAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 77)
)
if mibBuilder.loadTexts:
    juniDosProtectionPlatformAgent.setRevisions(
        ("2006-07-01 00:00",
         "2006-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniDosProtectionPlatformAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 77, 1)
)
if mibBuilder.loadTexts:
    juniDosProtectionPlatformAgentV1.setProductRelease("""\
Version 1 of the Dos Protection Platform component of the JUNOSe SNMP agent.
        This version of the Dos Protection Platform component is supported in JUNOSe 7.3
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniDosProtectionPlatformAgentV1.setStatus(
        "current"
    )

juniDosProtectionPlatformAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 77, 2)
)
if mibBuilder.loadTexts:
    juniDosProtectionPlatformAgentV2.setProductRelease("""\
Version 1 of the Dos Protection Platform component of the JUNOSe SNMP agent.
        This version of the Dos Protection Platform component is supported in JUNOSe -.-
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniDosProtectionPlatformAgentV2.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-Dos-Protection-Platform-CONF",
    **{"juniDosProtectionPlatformAgent": juniDosProtectionPlatformAgent,
       "juniDosProtectionPlatformAgentV1": juniDosProtectionPlatformAgentV1,
       "juniDosProtectionPlatformAgentV2": juniDosProtectionPlatformAgentV2}
)
