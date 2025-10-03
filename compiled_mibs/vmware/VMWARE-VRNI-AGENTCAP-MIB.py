# SNMP MIB module (VMWARE-VRNI-AGENTCAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMWARE-VRNI-AGENTCAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:37 2025
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

vmwVRNIAgentCapabilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125)
)
if mibBuilder.loadTexts:
    vmwVRNIAgentCapabilityMIB.setRevisions(
        ("2023-03-10 00:00",
         "2022-09-07 00:00",
         "2022-03-30 00:00",
         "2021-10-01 00:00",
         "2021-05-24 00:00",
         "2020-05-20 00:00",
         "2019-08-19 00:00",
         "2019-06-06 00:00",
         "2019-03-22 00:00",
         "2018-12-04 00:00",
         "2018-09-12 00:00",
         "2017-10-13 00:00",
         "2017-09-05 00:00",
         "2017-06-01 00:00",
         "2017-03-02 00:00",
         "2016-11-22 00:01")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwVRNICapability_ObjectIdentity = ObjectIdentity
vmwVRNICapability = _VmwVRNICapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

vmwVRNIAgent2016v320 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 6)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2016v320.setProductRelease("3.2.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2016v320.setStatus(
        "current"
    )

vmwVRNIAgent2017v330 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 7)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2017v330.setProductRelease("3.3.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2017v330.setStatus(
        "current"
    )

vmwVRNIAgent2017v340 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 8)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2017v340.setProductRelease("3.4.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2017v340.setStatus(
        "current"
    )

vmwVRNIAgent2016v350 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 9)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2016v350.setProductRelease("3.5.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2016v350.setStatus(
        "current"
    )

vmwVRNIAgent2018v390 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 11)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2018v390.setProductRelease("3.9.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2018v390.setStatus(
        "current"
    )

vmwVRNIAgent2018v400 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 12)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2018v400.setProductRelease("4.0.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2018v400.setStatus(
        "current"
    )

vmwVRNIAgent2019v410 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 13)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2019v410.setProductRelease("4.1.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2019v410.setStatus(
        "current"
    )

vmwVRNIAgent2019v420 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 14)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2019v420.setProductRelease("4.2.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2019v420.setStatus(
        "current"
    )

vmwVRNIAgent2019v500 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 15)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2019v500.setProductRelease("5.0.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2019v500.setStatus(
        "current"
    )

vmwVRNIAgent2020v520 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 16)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2020v520.setProductRelease("5.2.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2020v520.setStatus(
        "current"
    )

vmwVRNIAgent2021v620 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 17)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2021v620.setProductRelease("6.2.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2021v620.setStatus(
        "current"
    )

vmwVRNIAgent2021v640 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 18)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2021v640.setProductRelease("6.4.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2021v640.setStatus(
        "current"
    )

vmwVRNIAgent2021v650 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 19)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2021v650.setProductRelease("6.6.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2021v650.setStatus(
        "current"
    )

vmwVRNIAgent2021v660 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 20)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2021v660.setProductRelease("6.8.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2021v660.setStatus(
        "current"
    )

vmwVRNIAgent2021v670 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 21)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2021v670.setProductRelease("6.10.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2021v670.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-VRNI-AGENTCAP-MIB",
    **{"vmwVRNIAgentCapabilityMIB": vmwVRNIAgentCapabilityMIB,
       "vmwVRNICapability": vmwVRNICapability,
       "vmwVRNIAgent2016v320": vmwVRNIAgent2016v320,
       "vmwVRNIAgent2017v330": vmwVRNIAgent2017v330,
       "vmwVRNIAgent2017v340": vmwVRNIAgent2017v340,
       "vmwVRNIAgent2016v350": vmwVRNIAgent2016v350,
       "vmwVRNIAgent2018v390": vmwVRNIAgent2018v390,
       "vmwVRNIAgent2018v400": vmwVRNIAgent2018v400,
       "vmwVRNIAgent2019v410": vmwVRNIAgent2019v410,
       "vmwVRNIAgent2019v420": vmwVRNIAgent2019v420,
       "vmwVRNIAgent2019v500": vmwVRNIAgent2019v500,
       "vmwVRNIAgent2020v520": vmwVRNIAgent2020v520,
       "vmwVRNIAgent2021v620": vmwVRNIAgent2021v620,
       "vmwVRNIAgent2021v640": vmwVRNIAgent2021v640,
       "vmwVRNIAgent2021v650": vmwVRNIAgent2021v650,
       "vmwVRNIAgent2021v660": vmwVRNIAgent2021v660,
       "vmwVRNIAgent2021v670": vmwVRNIAgent2021v670}
)
