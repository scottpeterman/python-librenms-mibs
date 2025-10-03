# SNMP MIB module (VMWARE-NSX-MANAGER-AGENTCAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMWARE-NSX-MANAGER-AGENTCAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:22 2025
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

vmwNSXAgentCapabilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70, 25)
)
if mibBuilder.loadTexts:
    vmwNSXAgentCapabilityMIB.setRevisions(
        ("2020-06-03 00:00",
         "2016-10-24 00:01",
         "2016-10-24 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwNSXMCapability_ObjectIdentity = ObjectIdentity
vmwNSXMCapability = _VmwNSXMCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70, 25, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

vmwNSXManager2016x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 5)
)
if mibBuilder.loadTexts:
    vmwNSXManager2016x.setProductRelease("6.2.x")
if mibBuilder.loadTexts:
    vmwNSXManager2016x.setStatus(
        "current"
    )

vmwNSXManager2017x630 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 6)
)
if mibBuilder.loadTexts:
    vmwNSXManager2017x630.setProductRelease("6.3.0")
if mibBuilder.loadTexts:
    vmwNSXManager2017x630.setStatus(
        "current"
    )

vmwNSXManager2017x640 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 7)
)
if mibBuilder.loadTexts:
    vmwNSXManager2017x640.setProductRelease("6.4.0")
if mibBuilder.loadTexts:
    vmwNSXManager2017x640.setStatus(
        "current"
    )

vmwNSXManager2018x636 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 8)
)
if mibBuilder.loadTexts:
    vmwNSXManager2018x636.setProductRelease("6.3.6")
if mibBuilder.loadTexts:
    vmwNSXManager2018x636.setStatus(
        "current"
    )

vmwNSXManager2018x641 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 9)
)
if mibBuilder.loadTexts:
    vmwNSXManager2018x641.setProductRelease("6.4.1")
if mibBuilder.loadTexts:
    vmwNSXManager2018x641.setStatus(
        "current"
    )

vmwNSXManager2018x637 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 10)
)
if mibBuilder.loadTexts:
    vmwNSXManager2018x637.setProductRelease("6.3.7")
if mibBuilder.loadTexts:
    vmwNSXManager2018x637.setStatus(
        "current"
    )

vmwNSXManager2018x642 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 11)
)
if mibBuilder.loadTexts:
    vmwNSXManager2018x642.setProductRelease("6.4.2")
if mibBuilder.loadTexts:
    vmwNSXManager2018x642.setStatus(
        "current"
    )

vmwNSXManager2019x645 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 12)
)
if mibBuilder.loadTexts:
    vmwNSXManager2019x645.setProductRelease("6.4.5")
if mibBuilder.loadTexts:
    vmwNSXManager2019x645.setStatus(
        "current"
    )

vmwNSXManager2019x646 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 13)
)
if mibBuilder.loadTexts:
    vmwNSXManager2019x646.setProductRelease("6.4.6")
if mibBuilder.loadTexts:
    vmwNSXManager2019x646.setStatus(
        "current"
    )

vmwNSXManager2020x647 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 14)
)
if mibBuilder.loadTexts:
    vmwNSXManager2020x647.setProductRelease("6.4.7")
if mibBuilder.loadTexts:
    vmwNSXManager2020x647.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-NSX-MANAGER-AGENTCAP-MIB",
    **{"vmwNSXAgentCapabilityMIB": vmwNSXAgentCapabilityMIB,
       "vmwNSXMCapability": vmwNSXMCapability,
       "vmwNSXManager2016x": vmwNSXManager2016x,
       "vmwNSXManager2017x630": vmwNSXManager2017x630,
       "vmwNSXManager2017x640": vmwNSXManager2017x640,
       "vmwNSXManager2018x636": vmwNSXManager2018x636,
       "vmwNSXManager2018x641": vmwNSXManager2018x641,
       "vmwNSXManager2018x637": vmwNSXManager2018x637,
       "vmwNSXManager2018x642": vmwNSXManager2018x642,
       "vmwNSXManager2019x645": vmwNSXManager2019x645,
       "vmwNSXManager2019x646": vmwNSXManager2019x646,
       "vmwNSXManager2020x647": vmwNSXManager2020x647}
)
