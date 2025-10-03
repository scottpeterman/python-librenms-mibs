# SNMP MIB module (Juniper-Profile-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\Juniper-Profile-CONF
# Produced by pysmi-1.6.2 at Thu Oct  2 12:07:23 2025
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

(juniProfileAgents,) = mibBuilder.importSymbols(
    "Juniper-Agents",
    "juniProfileAgents")

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

juniProfileManagerAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1)
)
if mibBuilder.loadTexts:
    juniProfileManagerAgent.setRevisions(
        ("2002-12-17 20:00",
         "2002-09-06 16:54",
         "2001-03-29 18:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniProfileManagerAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1, 1)
)
if mibBuilder.loadTexts:
    juniProfileManagerAgentV1.setProductRelease("""\
Version 1 of the Profile Manager component of the JUNOSe SNMP agent.
        This version of the Profile Manager component was supported in JUNOSe
        1.1 thru 1.3 system releases.""")
if mibBuilder.loadTexts:
    juniProfileManagerAgentV1.setStatus(
        "obsolete"
    )

juniProfileManagerAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1, 2)
)
if mibBuilder.loadTexts:
    juniProfileManagerAgentV2.setProductRelease("""\
Version 2 of the Profile Manager component of the JUNOSe SNMP agent.
        This version of the Profile Manager component was supported in JUNOSe
        2.0 thru 5.0 system releases.""")
if mibBuilder.loadTexts:
    juniProfileManagerAgentV2.setStatus(
        "obsolete"
    )

juniProfileManagerAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1, 3)
)
if mibBuilder.loadTexts:
    juniProfileManagerAgentV3.setProductRelease("""\
Version 3 of the Profile Manager component of the JUNOSe SNMP agent.
        This version of the Profile Manager component is supported in JUNOSe 5.1
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniProfileManagerAgentV3.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-Profile-CONF",
    **{"juniProfileManagerAgent": juniProfileManagerAgent,
       "juniProfileManagerAgentV1": juniProfileManagerAgentV1,
       "juniProfileManagerAgentV2": juniProfileManagerAgentV2,
       "juniProfileManagerAgentV3": juniProfileManagerAgentV3}
)
