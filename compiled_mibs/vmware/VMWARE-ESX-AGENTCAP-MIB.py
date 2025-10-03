# SNMP MIB module (VMWARE-ESX-AGENTCAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMWARE-ESX-AGENTCAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:18 2025
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

(vmwareAgentCapabilities,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwareAgentCapabilities")


# MODULE-IDENTITY

vmwAgentCapabilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1)
)
if mibBuilder.loadTexts:
    vmwAgentCapabilityMIB.setRevisions(
        ("2022-09-15 00:00",
         "2020-03-27 00:00",
         "2017-10-13 00:00",
         "2016-04-22 00:00",
         "2015-01-12 00:00",
         "2014-08-02 00:00",
         "2012-10-03 00:00",
         "2012-07-13 00:00",
         "2010-10-18 00:00",
         "2008-10-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwEsxCapability_ObjectIdentity = ObjectIdentity
vmwEsxCapability = _VmwEsxCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

vmwESX40x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vmwESX40x.setProductRelease("4.0.x")
if mibBuilder.loadTexts:
    vmwESX40x.setStatus(
        "current"
    )

vmwESX41x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vmwESX41x.setProductRelease("4.1.x")
if mibBuilder.loadTexts:
    vmwESX41x.setStatus(
        "current"
    )

vmwESX50x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 3)
)
if mibBuilder.loadTexts:
    vmwESX50x.setProductRelease("5.0.x")
if mibBuilder.loadTexts:
    vmwESX50x.setStatus(
        "current"
    )

vmwESX51x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 4)
)
if mibBuilder.loadTexts:
    vmwESX51x.setProductRelease("5.1.x")
if mibBuilder.loadTexts:
    vmwESX51x.setStatus(
        "current"
    )

vmwESX55 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 5)
)
if mibBuilder.loadTexts:
    vmwESX55.setProductRelease("5.5.x")
if mibBuilder.loadTexts:
    vmwESX55.setStatus(
        "current"
    )

vmwESX60x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 10)
)
if mibBuilder.loadTexts:
    vmwESX60x.setProductRelease("6.0.x")
if mibBuilder.loadTexts:
    vmwESX60x.setStatus(
        "current"
    )

vmwESX65x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 15)
)
if mibBuilder.loadTexts:
    vmwESX65x.setProductRelease("6.5.x")
if mibBuilder.loadTexts:
    vmwESX65x.setStatus(
        "current"
    )

vmwESX67x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 16)
)
if mibBuilder.loadTexts:
    vmwESX67x.setProductRelease("6.7.x")
if mibBuilder.loadTexts:
    vmwESX67x.setStatus(
        "current"
    )

vmwESX70x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 17)
)
if mibBuilder.loadTexts:
    vmwESX70x.setProductRelease("7.0.x")
if mibBuilder.loadTexts:
    vmwESX70x.setStatus(
        "current"
    )

vmwESX80x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 18)
)
if mibBuilder.loadTexts:
    vmwESX80x.setProductRelease("8.0.x")
if mibBuilder.loadTexts:
    vmwESX80x.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-ESX-AGENTCAP-MIB",
    **{"vmwAgentCapabilityMIB": vmwAgentCapabilityMIB,
       "vmwEsxCapability": vmwEsxCapability,
       "vmwESX40x": vmwESX40x,
       "vmwESX41x": vmwESX41x,
       "vmwESX50x": vmwESX50x,
       "vmwESX51x": vmwESX51x,
       "vmwESX55": vmwESX55,
       "vmwESX60x": vmwESX60x,
       "vmwESX65x": vmwESX65x,
       "vmwESX67x": vmwESX67x,
       "vmwESX70x": vmwESX70x,
       "vmwESX80x": vmwESX80x}
)
