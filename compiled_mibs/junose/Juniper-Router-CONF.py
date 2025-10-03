# SNMP MIB module (Juniper-Router-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\Juniper-Router-CONF
# Produced by pysmi-1.6.2 at Thu Oct  2 12:07:35 2025
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

juniRouterAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 37)
)
if mibBuilder.loadTexts:
    juniRouterAgent.setRevisions(
        ("2004-05-06 20:30",
         "2004-01-26 15:53",
         "2003-04-24 14:16",
         "2002-05-10 19:06",
         "2001-03-29 18:17")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniRouterAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 1)
)
if mibBuilder.loadTexts:
    juniRouterAgentV1.setProductRelease("""\
Version 1 of the Router component of the JUNOSe SNMP agent.  This
        version of the Router component was supported in JUNOSe 1.3 and 2.x
        system releases.""")
if mibBuilder.loadTexts:
    juniRouterAgentV1.setStatus(
        "obsolete"
    )

juniRouterAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 2)
)
if mibBuilder.loadTexts:
    juniRouterAgentV2.setProductRelease("""\
Version 2 of the Router component of the JUNOSe SNMP agent.  This
        version of the Router component was supported in JUNOSe 3.x system
        releases.""")
if mibBuilder.loadTexts:
    juniRouterAgentV2.setStatus(
        "obsolete"
    )

juniRouterAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 3)
)
if mibBuilder.loadTexts:
    juniRouterAgentV3.setProductRelease("""\
Version 3 of the Router component of the JUNOSe SNMP agent.  This
        version of the Router component was supported in JUNOSe 4.x system
        releases.""")
if mibBuilder.loadTexts:
    juniRouterAgentV3.setStatus(
        "obsolete"
    )

juniRouterAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 4)
)
if mibBuilder.loadTexts:
    juniRouterAgentV4.setProductRelease("""\
Version 4 of the Router component of the JUNOSe SNMP agent.  This
        version of the Router component was supported in JUNOSe 5.0 and 5.1
        system releases.""")
if mibBuilder.loadTexts:
    juniRouterAgentV4.setStatus(
        "obsolete"
    )

juniRouterAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 5)
)
if mibBuilder.loadTexts:
    juniRouterAgentV5.setProductRelease("""\
Version 5 of the Router component of the JUNOSe SNMP agent.  This
        version of the Router component is supported in JUNOSe 5.2 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniRouterAgentV5.setStatus(
        "obsolete"
    )

juniRouterAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 37, 6)
)
if mibBuilder.loadTexts:
    juniRouterAgentV6.setProductRelease("""\
Version 6 of the Router component of the JUNOSe SNMP agent.  This
        version of the Router component is supported in JUNOSe 6.1 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniRouterAgentV6.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-Router-CONF",
    **{"juniRouterAgent": juniRouterAgent,
       "juniRouterAgentV1": juniRouterAgentV1,
       "juniRouterAgentV2": juniRouterAgentV2,
       "juniRouterAgentV3": juniRouterAgentV3,
       "juniRouterAgentV4": juniRouterAgentV4,
       "juniRouterAgentV5": juniRouterAgentV5,
       "juniRouterAgentV6": juniRouterAgentV6}
)
