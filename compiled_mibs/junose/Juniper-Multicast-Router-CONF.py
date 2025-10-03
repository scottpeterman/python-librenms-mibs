# SNMP MIB module (Juniper-Multicast-Router-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\broken\Juniper-Multicast-Router-CONF
# Produced by pysmi-1.6.2 at Thu Oct  2 12:05:41 2025
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

juniMRouterAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 55)
)
if mibBuilder.loadTexts:
    juniMRouterAgent.setRevisions(
        ("2006-09-18 08:09",
         "2006-09-02 11:02",
         "2006-06-15 10:13",
         "2002-10-28 20:04",
         "2002-04-01 20:17")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniMRouterAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 55, 1)
)
if mibBuilder.loadTexts:
    juniMRouterAgentV1.setProductRelease("""\
Version 1 of the multicast router component of the JUNOSe SNMP agent.
        This version of the multicast router component was supported in JUNOSe
        4.1 and subsequent 4.x system releases.""")
if mibBuilder.loadTexts:
    juniMRouterAgentV1.setStatus(
        "obsolete"
    )

juniMRouterAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 55, 2)
)
if mibBuilder.loadTexts:
    juniMRouterAgentV2.setProductRelease("""\
Version 2 of the multicast router component of the JUNOSe SNMP agent.
        These capabilities became obsolete when support was added to Juniper-MROUTER-MIB
        This version of the multicast router component is supported in the
        Juniper JUNOSe 5.0 and subsequent system releases upto 8.0.0.""")
if mibBuilder.loadTexts:
    juniMRouterAgentV2.setStatus(
        "obsolete"
    )

juniMRouterAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 55, 3)
)
if mibBuilder.loadTexts:
    juniMRouterAgentV3.setProductRelease("""\
Version 3 of the multicast router component of the JUNOSe SNMP agent.
        This version of the multicast router component is supported in the
        Juniper JUNOSe 8.1 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniMRouterAgentV3.setStatus(
        "obsolete"
    )

uniMRouterAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 55, 4)
)
if mibBuilder.loadTexts:
    uniMRouterAgentV4.setProductRelease("""\
Version 4 of the multicast router component of the JUNOSe SNMP agent.
        This version of the multicast router component is supported in the
        Juniper JUNOSe 8.1 and subsequent system releases.""")
if mibBuilder.loadTexts:
    uniMRouterAgentV4.setStatus(
        "obsolete"
    )

uniMRouterAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 55, 5)
)
if mibBuilder.loadTexts:
    uniMRouterAgentV5.setProductRelease("""\
Version 5 of the multicast router component of the JUNOSe SNMP agent.
        This version of the multicast router component is supported in the
        Juniper JUNOSe 8.1 and subsequent system releases.""")
if mibBuilder.loadTexts:
    uniMRouterAgentV5.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-Multicast-Router-CONF",
    **{"juniMRouterAgent": juniMRouterAgent,
       "juniMRouterAgentV1": juniMRouterAgentV1,
       "juniMRouterAgentV2": juniMRouterAgentV2,
       "juniMRouterAgentV3": juniMRouterAgentV3,
       "uniMRouterAgentV4": uniMRouterAgentV4,
       "uniMRouterAgentV5": uniMRouterAgentV5}
)
