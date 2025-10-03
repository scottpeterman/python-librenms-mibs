# SNMP MIB module (Juniper-Local-Address-Server-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\Juniper-Local-Address-Server-CONF
# Produced by pysmi-1.6.2 at Thu Oct  2 12:06:59 2025
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

juniLocalAddressServerAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 25)
)
if mibBuilder.loadTexts:
    juniLocalAddressServerAgent.setRevisions(
        ("2005-02-11 21:35",
         "2003-11-04 18:30",
         "2002-09-06 16:54",
         "2002-05-06 19:20",
         "2001-05-02 13:22")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniLocalAddressServerAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 1)
)
if mibBuilder.loadTexts:
    juniLocalAddressServerAgentV1.setProductRelease("""\
Version 1 of the Local Address Server component of the JUNOSe SNMP
        agent.  This version of the Local Address Server component was supported
        in JUNOSe 1.3 thru 3.1 system releases.""")
if mibBuilder.loadTexts:
    juniLocalAddressServerAgentV1.setStatus(
        "obsolete"
    )

juniLocalAddressServerAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 2)
)
if mibBuilder.loadTexts:
    juniLocalAddressServerAgentV2.setProductRelease("""\
Version 2 of the Local Address Server component of the JUNOSe SNMP
        agent.  This version of the Local Address Server component was supported
        in JUNOSe 3.2 system releases.""")
if mibBuilder.loadTexts:
    juniLocalAddressServerAgentV2.setStatus(
        "obsolete"
    )

juniLocalAddressServerAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 3)
)
if mibBuilder.loadTexts:
    juniLocalAddressServerAgentV3.setProductRelease("""\
Version 3 of the Local Address Server component of the JUNOSe SNMP
        agent.  This version of the Local Address Server component was supported
        in JUNOSe 3.3 thru 5.2 system releases.""")
if mibBuilder.loadTexts:
    juniLocalAddressServerAgentV3.setStatus(
        "obsolete"
    )

juniLocalAddressServerAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 4)
)
if mibBuilder.loadTexts:
    juniLocalAddressServerAgentV4.setProductRelease("""\
Version 4 of the Local Address Server component of the JUNOSe SNMP
        agent.  This version of the Local Address Server component is supported
        in JUNOSe 5.3 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniLocalAddressServerAgentV4.setStatus(
        "obsolete"
    )

juniLocalAddressServerAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 5)
)
if mibBuilder.loadTexts:
    juniLocalAddressServerAgentV5.setProductRelease("""\
Version 5 of the Local Address Server component of the JUNOSe SNMP
        agent.  This version of the Local Address Server component is supported
        in JUNOSe 6.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniLocalAddressServerAgentV5.setStatus(
        "obsolete"
    )

juniLocalAddressServerAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 6)
)
if mibBuilder.loadTexts:
    juniLocalAddressServerAgentV6.setProductRelease("""\
Version 6 of the Local Address Server component of the JUNOSe SNMP
        agent.  This version of the Local Address Server component is supported
        in JUNOSe 7.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniLocalAddressServerAgentV6.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-Local-Address-Server-CONF",
    **{"juniLocalAddressServerAgent": juniLocalAddressServerAgent,
       "juniLocalAddressServerAgentV1": juniLocalAddressServerAgentV1,
       "juniLocalAddressServerAgentV2": juniLocalAddressServerAgentV2,
       "juniLocalAddressServerAgentV3": juniLocalAddressServerAgentV3,
       "juniLocalAddressServerAgentV4": juniLocalAddressServerAgentV4,
       "juniLocalAddressServerAgentV5": juniLocalAddressServerAgentV5,
       "juniLocalAddressServerAgentV6": juniLocalAddressServerAgentV6}
)
