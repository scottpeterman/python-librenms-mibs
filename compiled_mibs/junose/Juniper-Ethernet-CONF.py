# SNMP MIB module (Juniper-Ethernet-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\Juniper-Ethernet-CONF
# Produced by pysmi-1.6.2 at Thu Oct  2 12:06:26 2025
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

juniEthernetAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 14)
)
if mibBuilder.loadTexts:
    juniEthernetAgent.setRevisions(
        ("2003-09-29 16:18",
         "2002-10-01 22:10",
         "2002-10-01 18:02",
         "2002-04-05 20:33",
         "2001-10-25 21:36")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniEthernetAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 1)
)
if mibBuilder.loadTexts:
    juniEthernetAgentV1.setProductRelease("""\
Version 1 of the Ethernet component of the JUNOSe SNMP agent.  This
        version of the Ethernet component was supported in JUNOSe 2.x system
        releases.""")
if mibBuilder.loadTexts:
    juniEthernetAgentV1.setStatus(
        "obsolete"
    )

juniEthernetAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 2)
)
if mibBuilder.loadTexts:
    juniEthernetAgentV2.setProductRelease("""\
Version 2 of the Ethernet component of the JUNOSe SNMP agent.  This
        version of the Ethernet component was supported in JUNOSe 3.x system
        releases.""")
if mibBuilder.loadTexts:
    juniEthernetAgentV2.setStatus(
        "obsolete"
    )

juniEthernetAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 3)
)
if mibBuilder.loadTexts:
    juniEthernetAgentV3.setProductRelease("""\
Version 3 of the Ethernet component of the JUNOSe SNMP agent.  This
        version of the Ethernet component was supported in JUNOSe 4.0 system
        releases.""")
if mibBuilder.loadTexts:
    juniEthernetAgentV3.setStatus(
        "obsolete"
    )

juniEthernetAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 4)
)
if mibBuilder.loadTexts:
    juniEthernetAgentV4.setProductRelease("""\
Version 4 of the Ethernet component of the JUNOSe SNMP agent.  This
        version of the Ethernet component was supported in JUNOSe 4.1 through
        5.1 system releases.""")
if mibBuilder.loadTexts:
    juniEthernetAgentV4.setStatus(
        "obsolete"
    )

juniEthernetAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 14, 5)
)
if mibBuilder.loadTexts:
    juniEthernetAgentV5.setProductRelease("""\
Version 5 of the Ethernet component of the JUNOSe SNMP agent.  This
        version of the Ethernet component is supported in JUNOSe 5.2 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniEthernetAgentV5.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-Ethernet-CONF",
    **{"juniEthernetAgent": juniEthernetAgent,
       "juniEthernetAgentV1": juniEthernetAgentV1,
       "juniEthernetAgentV2": juniEthernetAgentV2,
       "juniEthernetAgentV3": juniEthernetAgentV3,
       "juniEthernetAgentV4": juniEthernetAgentV4,
       "juniEthernetAgentV5": juniEthernetAgentV5}
)
