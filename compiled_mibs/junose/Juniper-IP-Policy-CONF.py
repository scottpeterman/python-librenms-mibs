# SNMP MIB module (Juniper-IP-Policy-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\Juniper-IP-Policy-CONF
# Produced by pysmi-1.6.2 at Thu Oct  2 12:06:44 2025
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

juniIpPolicyAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 22)
)
if mibBuilder.loadTexts:
    juniIpPolicyAgent.setRevisions(
        ("2003-02-05 14:58",
         "2002-09-06 16:54",
         "2001-05-01 20:13")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniIpPolicyAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 1)
)
if mibBuilder.loadTexts:
    juniIpPolicyAgentV1.setProductRelease("""\
Version 1 of the IP Policy component of the JUNOSe SNMP agent.  This
        version of the IP Policy component was supported in JUNOSe 1.x system
        releases.""")
if mibBuilder.loadTexts:
    juniIpPolicyAgentV1.setStatus(
        "obsolete"
    )

juniIpPolicyAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 2)
)
if mibBuilder.loadTexts:
    juniIpPolicyAgentV2.setProductRelease("""\
Version 2 of the IP Policy component of the JUNOSe SNMP agent.  This
        version of the IP Policy component was supported in JUNOSe 2.x system
        releases.""")
if mibBuilder.loadTexts:
    juniIpPolicyAgentV2.setStatus(
        "obsolete"
    )

juniIpPolicyAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 3)
)
if mibBuilder.loadTexts:
    juniIpPolicyAgentV3.setProductRelease("""\
Version 3 of the IP Policy component of the JUNOSe SNMP agent.  This
        version of the IP Policy component was supported in JUNOSe 3.0 thru 5.0
        system releases.""")
if mibBuilder.loadTexts:
    juniIpPolicyAgentV3.setStatus(
        "obsolete"
    )

juniIpPolicyAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 22, 4)
)
if mibBuilder.loadTexts:
    juniIpPolicyAgentV4.setProductRelease("""\
Version 4 of the IP Policy component of the JUNOSe SNMP agent.  This
        version of the IP Policy component is supported in JUNOSe 5.1 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniIpPolicyAgentV4.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-IP-Policy-CONF",
    **{"juniIpPolicyAgent": juniIpPolicyAgent,
       "juniIpPolicyAgentV1": juniIpPolicyAgentV1,
       "juniIpPolicyAgentV2": juniIpPolicyAgentV2,
       "juniIpPolicyAgentV3": juniIpPolicyAgentV3,
       "juniIpPolicyAgentV4": juniIpPolicyAgentV4}
)
