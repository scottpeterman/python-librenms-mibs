# SNMP MIB module (Juniper-DS3-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\Juniper-DS3-CONF
# Produced by pysmi-1.6.2 at Thu Oct  2 12:06:16 2025
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

juniDs3Agent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 11)
)
if mibBuilder.loadTexts:
    juniDs3Agent.setRevisions(
        ("2003-09-29 21:05",
         "2003-01-30 19:08",
         "2003-01-30 16:37",
         "2002-08-27 18:48",
         "2001-04-18 19:41")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniDs3AgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 1)
)
if mibBuilder.loadTexts:
    juniDs3AgentV1.setProductRelease("""\
Version 1 of the DS3 component of the JUNOSe SNMP agent.  This version
        of the DS3 component was supported in JUNOSe 1.0 system releases.""")
if mibBuilder.loadTexts:
    juniDs3AgentV1.setStatus(
        "obsolete"
    )

juniDs3AgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 2)
)
if mibBuilder.loadTexts:
    juniDs3AgentV2.setProductRelease("""\
Version 2 of the DS3 component of the JUNOSe SNMP agent.  This version
        of the DS3 component was supported in JUNOSe 1.1 thru JUNOSe 2.5 system
        releases.""")
if mibBuilder.loadTexts:
    juniDs3AgentV2.setStatus(
        "obsolete"
    )

juniDs3AgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 3)
)
if mibBuilder.loadTexts:
    juniDs3AgentV3.setProductRelease("""\
Version 3 of the DS3 component of the JUNOSe SNMP agent.  This version
        of the DS3 component was supported in JUNOSe 2.6 and subsequent JUNOSe
        2.x system releases.""")
if mibBuilder.loadTexts:
    juniDs3AgentV3.setStatus(
        "obsolete"
    )

juniDs3AgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 4)
)
if mibBuilder.loadTexts:
    juniDs3AgentV4.setProductRelease("""\
Version 4 of the DS3 component of the JUNOSe SNMP agent.  This version
        of the DS3 component was supported in JUNOSe 3.x system releases.""")
if mibBuilder.loadTexts:
    juniDs3AgentV4.setStatus(
        "obsolete"
    )

juniDs3AgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 5)
)
if mibBuilder.loadTexts:
    juniDs3AgentV5.setProductRelease("""\
Version 5 of the DS3 component of the JUNOSe SNMP agent.  This version
        of the DS3 component was supported in JUNOSe 4.0 system releases.""")
if mibBuilder.loadTexts:
    juniDs3AgentV5.setStatus(
        "obsolete"
    )

juniDs3AgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 11, 6)
)
if mibBuilder.loadTexts:
    juniDs3AgentV6.setProductRelease("""\
Version 6 of the DS3 component of the JUNOSe SNMP agent.  This version
        of the DS3 component is supported in JUNOSe 4.1 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniDs3AgentV6.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-DS3-CONF",
    **{"juniDs3Agent": juniDs3Agent,
       "juniDs3AgentV1": juniDs3AgentV1,
       "juniDs3AgentV2": juniDs3AgentV2,
       "juniDs3AgentV3": juniDs3AgentV3,
       "juniDs3AgentV4": juniDs3AgentV4,
       "juniDs3AgentV5": juniDs3AgentV5,
       "juniDs3AgentV6": juniDs3AgentV6}
)
