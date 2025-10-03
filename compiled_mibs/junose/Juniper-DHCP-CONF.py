# SNMP MIB module (Juniper-DHCP-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\Juniper-DHCP-CONF
# Produced by pysmi-1.6.2 at Thu Oct  2 12:06:05 2025
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

juniDhcpAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8)
)
if mibBuilder.loadTexts:
    juniDhcpAgent.setRevisions(
        ("2007-01-31 20:38",
         "2005-11-04 19:53",
         "2005-05-17 19:18",
         "2005-12-05 21:31",
         "2004-11-08 16:16",
         "2004-01-23 16:30",
         "2003-09-05 19:03",
         "2002-12-17 16:59",
         "2002-05-10 19:37",
         "2001-03-30 18:46")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniDhcpRelayAgent_ObjectIdentity = ObjectIdentity
juniDhcpRelayAgent = _JuniDhcpRelayAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1)
)
if mibBuilder.loadTexts:
    juniDhcpRelayAgent.setStatus("current")
_JuniDhcpProxyAgent_ObjectIdentity = ObjectIdentity
juniDhcpProxyAgent = _JuniDhcpProxyAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 2)
)
if mibBuilder.loadTexts:
    juniDhcpProxyAgent.setStatus("current")
_JuniDhcpLocalServerAgent_ObjectIdentity = ObjectIdentity
juniDhcpLocalServerAgent = _JuniDhcpLocalServerAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3)
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerAgent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniDhcpRelayAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV1.setProductRelease("""\
Version 1 of the DHCP relay subcomponent of the JUNOSe SNMP agent.
        This version of the DHCP relay subcomponent was supported in JUNOSe 1.3
        thru 3.x system releases.""")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV1.setStatus(
        "obsolete"
    )

juniDhcpRelayAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 2)
)
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV2.setProductRelease("""\
Version 2 of the DHCP relay subcomponent of the JUNOSe SNMP agent.
        This version of the DHCP relay subcomponent was supported in JUNOSe 4.x
        system releases.""")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV2.setStatus(
        "obsolete"
    )

juniDhcpRelayAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 3)
)
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV3.setProductRelease("""\
Version 3 of the DHCP relay subcomponent of the JUNOSe SNMP agent.
        This version of the DHCP relay subcomponent was supported in JUNOSe 5.0
        system releases.""")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV3.setStatus(
        "obsolete"
    )

juniDhcpRelayAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 4)
)
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV4.setProductRelease("""\
Version 4 of the DHCP relay subcomponent of the JUNOSe SNMP agent.
        This version of the DHCP relay subcomponent is supported in JUNOSe 5.1
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV4.setStatus(
        "obsolete"
    )

juniDhcpRelayAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 5)
)
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV5.setProductRelease("""\
Version 5 of the DHCP relay subcomponent of the JUNOSe SNMP agent.
        This version of the DHCP relay subcomponent is supported in JUNOSe 6.1
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV5.setStatus(
        "obsolete"
    )

juniDhcpRelayAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 6)
)
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV6.setProductRelease("""\
Version 6 of the DHCP relay subcomponent of the JUNOSe SNMP agent.
        This version of the DHCP relay subcomponent is supported in JUNOSe 7.0
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV6.setStatus(
        "obsolete"
    )

juniDhcpRelayAgentV7 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 7)
)
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV7.setProductRelease("""\
Version 7 of the DHCP relay subcomponent of the JUNOSe SNMP agent.
        This version of the DHCP relay subcomponent is supported in JUNOSe 7.0
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV7.setStatus(
        "obsolete"
    )

juniDhcpRelayAgentV8 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 8)
)
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV8.setProductRelease("""\
Version 8 of the DHCP relay subcomponent of the JUNOSe SNMP agent.
        This version of the DHCP relay subcomponent is supported in JUNOSe 7.2
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV8.setStatus(
        "obsolete"
    )

juniDhcpRelayAgentV9 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 9)
)
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV9.setProductRelease("""\
Version 9 of the DHCP relay subcomponent of the JUNOSe SNMP agent.
        This version of the DHCP relay subcomponent is supported in JUNOSe 8.0
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentV9.setStatus(
        "current"
    )

juniDhcpProxyAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    juniDhcpProxyAgentV1.setProductRelease("""\
Version 1 of the DHCP proxy subcomponent of the JUNOSe SNMP agent.
        This version of the DHCP proxy subcomponent is supported in JUNOSe 1.3
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniDhcpProxyAgentV1.setStatus(
        "current"
    )

juniDhcpLocalServerAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 1)
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerAgentV1.setProductRelease("""\
Version 1 of the DHCP local server subcomponent of JUNOSe SNMP agent.
        This version of the DHCP local server subcomponent was supported in
        JUNOSe 3.1 and subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    juniDhcpLocalServerAgentV1.setStatus(
        "obsolete"
    )

juniDhcpLocalServerAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 2)
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerAgentV2.setProductRelease("""\
Version 2 of the DHCP local server subcomponent of JUNOSe SNMP agent.
        This version of the DHCP local server subcomponent was supported in
        JUNOSe 4.0 through 5.1 system releases.""")
if mibBuilder.loadTexts:
    juniDhcpLocalServerAgentV2.setStatus(
        "obsolete"
    )

juniDhcpLocalServerAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 3)
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerAgentV3.setProductRelease("""\
Version 3 of the DHCP local server subcomponent of JUNOSe SNMP agent.
        This version of the DHCP local server subcomponent is supported in
        JUNOSe 5.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniDhcpLocalServerAgentV3.setStatus(
        "current"
    )

juniDhcpLocalServerAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 5)
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerAgentV5.setProductRelease("""\
Version 5 of the DHCP local server subcomponent of JUNOSe SNMP agent.
        This version of the DHCP local server subcomponent is supported in
        JUNOSe 6.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniDhcpLocalServerAgentV5.setStatus(
        "obsolete"
    )

juniDhcpLocalServerAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 6)
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerAgentV6.setProductRelease("""\
Version 6 of the DHCP local server subcomponent of JUNOSe SNMP agent.
        This version of the DHCP local server subcomponent is supported in
        JUNOSe 7.1 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniDhcpLocalServerAgentV6.setStatus(
        "obsolete"
    )

juniDhcpLocalServerAgentV7 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 7)
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerAgentV7.setProductRelease("""\
Version 7 of the DHCP local server subcomponent of JUNOSe SNMP agent.
        This version of the DHCP local server subcomponent is supported in
        JUNOSe 8.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniDhcpLocalServerAgentV7.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-DHCP-CONF",
    **{"juniDhcpAgent": juniDhcpAgent,
       "juniDhcpRelayAgent": juniDhcpRelayAgent,
       "juniDhcpRelayAgentV1": juniDhcpRelayAgentV1,
       "juniDhcpRelayAgentV2": juniDhcpRelayAgentV2,
       "juniDhcpRelayAgentV3": juniDhcpRelayAgentV3,
       "juniDhcpRelayAgentV4": juniDhcpRelayAgentV4,
       "juniDhcpRelayAgentV5": juniDhcpRelayAgentV5,
       "juniDhcpRelayAgentV6": juniDhcpRelayAgentV6,
       "juniDhcpRelayAgentV7": juniDhcpRelayAgentV7,
       "juniDhcpRelayAgentV8": juniDhcpRelayAgentV8,
       "juniDhcpRelayAgentV9": juniDhcpRelayAgentV9,
       "juniDhcpProxyAgent": juniDhcpProxyAgent,
       "juniDhcpProxyAgentV1": juniDhcpProxyAgentV1,
       "juniDhcpLocalServerAgent": juniDhcpLocalServerAgent,
       "juniDhcpLocalServerAgentV1": juniDhcpLocalServerAgentV1,
       "juniDhcpLocalServerAgentV2": juniDhcpLocalServerAgentV2,
       "juniDhcpLocalServerAgentV3": juniDhcpLocalServerAgentV3,
       "juniDhcpLocalServerAgentV5": juniDhcpLocalServerAgentV5,
       "juniDhcpLocalServerAgentV6": juniDhcpLocalServerAgentV6,
       "juniDhcpLocalServerAgentV7": juniDhcpLocalServerAgentV7}
)
