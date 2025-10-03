# SNMP MIB module (VMWARE-VA-AGENTCAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMWARE-VA-AGENTCAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:32 2025
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

vmwVAAgentCapabilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70, 5)
)
if mibBuilder.loadTexts:
    vmwVAAgentCapabilityMIB.setRevisions(
        ("2022-09-15 00:00",
         "2020-03-27 00:00",
         "2017-10-13 00:00",
         "2016-04-22 00:00",
         "2015-01-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwVACapability_ObjectIdentity = ObjectIdentity
vmwVACapability = _VmwVACapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70, 5, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

vmwVA2015x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 5, 1, 5)
)
if mibBuilder.loadTexts:
    vmwVA2015x.setProductRelease("6.0.x")
if mibBuilder.loadTexts:
    vmwVA2015x.setStatus(
        "current"
    )

vmwVCSA2016x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 5, 1, 6)
)
if mibBuilder.loadTexts:
    vmwVCSA2016x.setProductRelease("6.5.x")
if mibBuilder.loadTexts:
    vmwVCSA2016x.setStatus(
        "current"
    )

vmwVCSA2017x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 5, 1, 7)
)
if mibBuilder.loadTexts:
    vmwVCSA2017x.setProductRelease("6.7.x")
if mibBuilder.loadTexts:
    vmwVCSA2017x.setStatus(
        "current"
    )

vmwVCSA2020x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 5, 1, 9)
)
if mibBuilder.loadTexts:
    vmwVCSA2020x.setProductRelease("7.0.x")
if mibBuilder.loadTexts:
    vmwVCSA2020x.setStatus(
        "current"
    )

vmwVCSA2022x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 5, 1, 10)
)
if mibBuilder.loadTexts:
    vmwVCSA2022x.setProductRelease("8.0.x")
if mibBuilder.loadTexts:
    vmwVCSA2022x.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-VA-AGENTCAP-MIB",
    **{"vmwVAAgentCapabilityMIB": vmwVAAgentCapabilityMIB,
       "vmwVACapability": vmwVACapability,
       "vmwVA2015x": vmwVA2015x,
       "vmwVCSA2016x": vmwVCSA2016x,
       "vmwVCSA2017x": vmwVCSA2017x,
       "vmwVCSA2020x": vmwVCSA2020x,
       "vmwVCSA2022x": vmwVCSA2022x}
)
