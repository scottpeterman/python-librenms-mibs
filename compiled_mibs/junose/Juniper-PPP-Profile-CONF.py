# SNMP MIB module (Juniper-PPP-Profile-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\Juniper-PPP-Profile-CONF
# Produced by pysmi-1.6.2 at Thu Oct  2 12:07:17 2025
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

juniPppProfileAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3)
)
if mibBuilder.loadTexts:
    juniPppProfileAgent.setRevisions(
        ("2009-09-18 07:24",
         "2009-08-10 14:23",
         "2007-07-12 12:15",
         "2005-10-19 16:26",
         "2003-11-03 21:32",
         "2003-03-13 16:47",
         "2002-09-06 16:54",
         "2002-09-03 22:38",
         "2002-01-25 14:10",
         "2002-01-16 17:58",
         "2002-01-08 19:43",
         "2001-10-17 17:10")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniPppProfileAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 1)
)
if mibBuilder.loadTexts:
    juniPppProfileAgentV1.setProductRelease("""\
Version 1 of the PPP Profile component of the JUNOSe SNMP agent.  This
        version of the PPP Profile component was supported in JUNOSe 3.0 through
        3.2 system releases.""")
if mibBuilder.loadTexts:
    juniPppProfileAgentV1.setStatus(
        "obsolete"
    )

juniPppProfileAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 2)
)
if mibBuilder.loadTexts:
    juniPppProfileAgentV2.setProductRelease("""\
Version 2 of the PPP Profile component of the JUNOSe SNMP agent.  This
        version of the PPP Profile component was supported in JUNOSe 3.3 system
        release.""")
if mibBuilder.loadTexts:
    juniPppProfileAgentV2.setStatus(
        "obsolete"
    )

juniPppProfileAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 3)
)
if mibBuilder.loadTexts:
    juniPppProfileAgentV3.setProductRelease("""\
Version 3 of the PPP Profile component of the JUNOSe SNMP agent.  This
        version of the PPP Profile component was supported in JUNOSe 3.4 and
        subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    juniPppProfileAgentV3.setStatus(
        "obsolete"
    )

juniPppProfileAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 4)
)
if mibBuilder.loadTexts:
    juniPppProfileAgentV4.setProductRelease("""\
Version 4 of the PPP Profile component of the JUNOSe SNMP agent.  This
        version of the PPP Profile component was supported in JUNOSe 4.0 system
        releases.""")
if mibBuilder.loadTexts:
    juniPppProfileAgentV4.setStatus(
        "obsolete"
    )

juniPppProfileAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 5)
)
if mibBuilder.loadTexts:
    juniPppProfileAgentV5.setProductRelease("""\
Version 5 of the PPP Profile component of the JUNOSe SNMP agent.  This
        version of the PPP Profile component was supported in JUNOSe 4.1 through
        5.0 system releases.""")
if mibBuilder.loadTexts:
    juniPppProfileAgentV5.setStatus(
        "obsolete"
    )

juniPppProfileAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 6)
)
if mibBuilder.loadTexts:
    juniPppProfileAgentV6.setProductRelease("""\
Version 6 of the PPP Profile component of the JUNOSe SNMP agent.  This
        version of the PPP Profile component was supported in JUNOSe 5.1 and 5.2
        system releases.""")
if mibBuilder.loadTexts:
    juniPppProfileAgentV6.setStatus(
        "obsolete"
    )

juniPppProfileAgentV7 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 7)
)
if mibBuilder.loadTexts:
    juniPppProfileAgentV7.setProductRelease("""\
Version 7 of the PPP Profile component of the JUNOSe SNMP agent.  This
        version of the PPP Profile component is supported in JUNOSe 5.3 through
        7.2 system releases.""")
if mibBuilder.loadTexts:
    juniPppProfileAgentV7.setStatus(
        "obsolete"
    )

juniPppProfileAgentV8 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 8)
)
if mibBuilder.loadTexts:
    juniPppProfileAgentV8.setProductRelease("""\
Version 8 of the PPP Profile component of the JUNOSe SNMP agent.  This
        version of the PPP Profile component is supported in JUNOSe 7.2 system
        releases.""")
if mibBuilder.loadTexts:
    juniPppProfileAgentV8.setStatus(
        "obsolete"
    )

juniPppProfileAgentV9 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 9)
)
if mibBuilder.loadTexts:
    juniPppProfileAgentV9.setProductRelease("""\
Version 9 of the PPP Profile component of the JUNOSe SNMP agent.  This
        version of the PPP Profile component is supported in JUNOSe 7.3 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniPppProfileAgentV9.setStatus(
        "obsolete"
    )

juniPppProfileAgentV10 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 10)
)
if mibBuilder.loadTexts:
    juniPppProfileAgentV10.setProductRelease("""\
Version 10 of the PPP Profile component of the JUNOSe SNMP agent.  This
        version of the PPP Profile component is supported in JUNOSe 11.0 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniPppProfileAgentV10.setStatus(
        "obsolete"
    )

juniPppProfileAgentV11 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3, 11)
)
if mibBuilder.loadTexts:
    juniPppProfileAgentV11.setProductRelease("""\
Version 11 of the PPP Profile component of the JUNOSe SNMP agent.  This
        version of the PPP Profile component is supported in JUNOSe 11.1 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniPppProfileAgentV11.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-PPP-Profile-CONF",
    **{"juniPppProfileAgent": juniPppProfileAgent,
       "juniPppProfileAgentV1": juniPppProfileAgentV1,
       "juniPppProfileAgentV2": juniPppProfileAgentV2,
       "juniPppProfileAgentV3": juniPppProfileAgentV3,
       "juniPppProfileAgentV4": juniPppProfileAgentV4,
       "juniPppProfileAgentV5": juniPppProfileAgentV5,
       "juniPppProfileAgentV6": juniPppProfileAgentV6,
       "juniPppProfileAgentV7": juniPppProfileAgentV7,
       "juniPppProfileAgentV8": juniPppProfileAgentV8,
       "juniPppProfileAgentV9": juniPppProfileAgentV9,
       "juniPppProfileAgentV10": juniPppProfileAgentV10,
       "juniPppProfileAgentV11": juniPppProfileAgentV11}
)
