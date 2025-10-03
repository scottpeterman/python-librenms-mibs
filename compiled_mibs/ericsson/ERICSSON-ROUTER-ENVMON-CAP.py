# SNMP MIB module (ERICSSON-ROUTER-ENVMON-CAP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\ERICSSON-ROUTER-ENVMON-CAP
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:28 2025
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

(eriRouterCapabilities,) = mibBuilder.importSymbols(
    "ERICSSON-ROUTER-SMI",
    "eriRouterCapabilities")

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

eriRouterEnvMonCap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 218, 4, 17)
)
if mibBuilder.loadTexts:
    eriRouterEnvMonCap.setRevisions(
        ("2015-01-14 18:00",
         "2011-09-02 00:00",
         "2011-06-15 00:00",
         "2010-11-11 00:00",
         "2008-11-11 00:00",
         "2006-01-16 00:00",
         "2002-06-05 00:00",
         "2001-07-25 00:00",
         "2000-04-24 00:00",
         "1999-03-09 23:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

eriRouterEnvMonCap1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 193, 218, 4, 17, 1)
)
if mibBuilder.loadTexts:
    eriRouterEnvMonCap1.setProductRelease("2.3.X.X")
if mibBuilder.loadTexts:
    eriRouterEnvMonCap1.setStatus(
        "obsolete"
    )

eriRouterEnvMonCap2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 193, 218, 4, 17, 2)
)
if mibBuilder.loadTexts:
    eriRouterEnvMonCap2.setProductRelease("4.0.X.X")
if mibBuilder.loadTexts:
    eriRouterEnvMonCap2.setStatus(
        "current"
    )

eriRouterEnvMonCap3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 193, 218, 4, 17, 3)
)
if mibBuilder.loadTexts:
    eriRouterEnvMonCap3.setProductRelease("SmartEdge 2.0.4")
if mibBuilder.loadTexts:
    eriRouterEnvMonCap3.setStatus(
        "current"
    )

eriRouterEnvMonCap4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 193, 218, 4, 17, 4)
)
if mibBuilder.loadTexts:
    eriRouterEnvMonCap4.setProductRelease("SmartEdge 5.0.5")
if mibBuilder.loadTexts:
    eriRouterEnvMonCap4.setStatus(
        "current"
    )

eriRouterEnvMonCap5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 193, 218, 4, 17, 5)
)
if mibBuilder.loadTexts:
    eriRouterEnvMonCap5.setProductRelease("SEOS 6.2.1 [SE]; SEOS 6.3.X [SM]; SEOS 11.1.X [SSR]")
if mibBuilder.loadTexts:
    eriRouterEnvMonCap5.setStatus(
        "current"
    )

eriRouterEnvMonCap6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 193, 218, 4, 17, 6)
)
if mibBuilder.loadTexts:
    eriRouterEnvMonCap6.setProductRelease("IPOS 11.1.X")
if mibBuilder.loadTexts:
    eriRouterEnvMonCap6.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERICSSON-ROUTER-ENVMON-CAP",
    **{"eriRouterEnvMonCap": eriRouterEnvMonCap,
       "eriRouterEnvMonCap1": eriRouterEnvMonCap1,
       "eriRouterEnvMonCap2": eriRouterEnvMonCap2,
       "eriRouterEnvMonCap3": eriRouterEnvMonCap3,
       "eriRouterEnvMonCap4": eriRouterEnvMonCap4,
       "eriRouterEnvMonCap5": eriRouterEnvMonCap5,
       "eriRouterEnvMonCap6": eriRouterEnvMonCap6}
)
