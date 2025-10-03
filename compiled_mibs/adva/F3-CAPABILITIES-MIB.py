# SNMP MIB module (F3-CAPABILITIES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-CAPABILITIES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:46 2025
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

(f3Capabilities,) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "f3Capabilities")

(VlanIdOrAnyOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrAnyOrNone")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

f3CapabilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    f3CapabilityMIB.setRevisions(
        ("2020-02-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F3CapabilityDefinitions_ObjectIdentity = ObjectIdentity
f3CapabilityDefinitions = _F3CapabilityDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

f3BaseStandardsCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    f3BaseStandardsCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3BaseStandardsCapabilities.setStatus(
        "current"
    )

f3StandardIfEntityCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    f3StandardIfEntityCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3StandardIfEntityCapabilities.setStatus(
        "current"
    )

f3StandardTargetNotifCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    f3StandardTargetNotifCapabilities.setProductRelease("F3 - Standard Interface and Entity capabilities ")
if mibBuilder.loadTexts:
    f3StandardTargetNotifCapabilities.setStatus(
        "current"
    )

f3StandardSecurityCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    f3StandardSecurityCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3StandardSecurityCapabilities.setStatus(
        "current"
    )

f3StandardRMONCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    f3StandardRMONCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3StandardRMONCapabilities.setStatus(
        "current"
    )

f3StandardCfmCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    f3StandardCfmCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3StandardCfmCapabilities.setStatus(
        "current"
    )

f3StandardBridgeCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    f3StandardBridgeCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3StandardBridgeCapabilities.setStatus(
        "current"
    )

f3StandardLAGCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    f3StandardLAGCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3StandardLAGCapabilities.setStatus(
        "current"
    )

f3CommonVendorSpecificCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 9)
)
if mibBuilder.loadTexts:
    f3CommonVendorSpecificCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3CommonVendorSpecificCapabilities.setStatus(
        "current"
    )

f3FacilityCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 10)
)
if mibBuilder.loadTexts:
    f3FacilityCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3FacilityCapabilities.setStatus(
        "current"
    )

f3Nid206Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 11)
)
if mibBuilder.loadTexts:
    f3Nid206Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid206Capabilities.setStatus(
        "current"
    )

f3Nid201SyncECapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 12)
)
if mibBuilder.loadTexts:
    f3Nid201SyncECapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid201SyncECapabilities.setStatus(
        "current"
    )

f3Nid201NonSyncECapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 13)
)
if mibBuilder.loadTexts:
    f3Nid201NonSyncECapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid201NonSyncECapabilities.setStatus(
        "current"
    )

f3Nid206FCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 14)
)
if mibBuilder.loadTexts:
    f3Nid206FCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid206FCapabilities.setStatus(
        "current"
    )

f3Nid112Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 15)
)
if mibBuilder.loadTexts:
    f3Nid112Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid112Capabilities.setStatus(
        "current"
    )

f3Nid114Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 16)
)
if mibBuilder.loadTexts:
    f3Nid114Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid114Capabilities.setStatus(
        "current"
    )

f3EcpaCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 17)
)
if mibBuilder.loadTexts:
    f3EcpaCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3EcpaCapabilities.setStatus(
        "current"
    )

f3EsaCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 18)
)
if mibBuilder.loadTexts:
    f3EsaCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3EsaCapabilities.setStatus(
        "current"
    )

f3BridgeCapabilitiesCmHub = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 19)
)
if mibBuilder.loadTexts:
    f3BridgeCapabilitiesCmHub.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3BridgeCapabilitiesCmHub.setStatus(
        "current"
    )

f3CommonVendorSpecificCapabilitiesCmHub = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 20)
)
if mibBuilder.loadTexts:
    f3CommonVendorSpecificCapabilitiesCmHub.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3CommonVendorSpecificCapabilitiesCmHub.setStatus(
        "current"
    )

f3FacilityCapabilitiesCmHub = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 21)
)
if mibBuilder.loadTexts:
    f3FacilityCapabilitiesCmHub.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3FacilityCapabilitiesCmHub.setStatus(
        "current"
    )

f3EntityCmHubCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 22)
)
if mibBuilder.loadTexts:
    f3EntityCmHubCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3EntityCmHubCapabilities.setStatus(
        "current"
    )

f3Nid206VCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 23)
)
if mibBuilder.loadTexts:
    f3Nid206VCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid206VCapabilities.setStatus(
        "current"
    )

f3NidXG210Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 24)
)
if mibBuilder.loadTexts:
    f3NidXG210Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3NidXG210Capabilities.setStatus(
        "current"
    )

f3PtpCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 25)
)
if mibBuilder.loadTexts:
    f3PtpCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3PtpCapabilities.setStatus(
        "current"
    )

f3PseudoWireCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 26)
)
if mibBuilder.loadTexts:
    f3PseudoWireCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3PseudoWireCapabilities.setStatus(
        "current"
    )

f3DS1Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 27)
)
if mibBuilder.loadTexts:
    f3DS1Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3DS1Capabilities.setStatus(
        "current"
    )

f3SonetCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 28)
)
if mibBuilder.loadTexts:
    f3SonetCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3SonetCapabilities.setStatus(
        "current"
    )

f3SyncECapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 29)
)
if mibBuilder.loadTexts:
    f3SyncECapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3SyncECapabilities.setStatus(
        "current"
    )

f3CfmCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 30)
)
if mibBuilder.loadTexts:
    f3CfmCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3CfmCapabilities.setStatus(
        "current"
    )

f3LAGCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 31)
)
if mibBuilder.loadTexts:
    f3LAGCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3LAGCapabilities.setStatus(
        "current"
    )

f3PBBCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 32)
)
if mibBuilder.loadTexts:
    f3PBBCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3PBBCapabilities.setStatus(
        "current"
    )

f3Nid1804Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 33)
)
if mibBuilder.loadTexts:
    f3Nid1804Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid1804Capabilities.setStatus(
        "current"
    )

f3Nid3204Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 34)
)
if mibBuilder.loadTexts:
    f3Nid3204Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid3204Capabilities.setStatus(
        "current"
    )

f3BertCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 35)
)
if mibBuilder.loadTexts:
    f3BertCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3BertCapabilities.setStatus(
        "current"
    )

f3NidSyncProbeCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 36)
)
if mibBuilder.loadTexts:
    f3NidSyncProbeCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3NidSyncProbeCapabilities.setStatus(
        "current"
    )

f3SyncJackCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 37)
)
if mibBuilder.loadTexts:
    f3SyncJackCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3SyncJackCapabilities.setStatus(
        "current"
    )

f3EsmCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 38)
)
if mibBuilder.loadTexts:
    f3EsmCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3EsmCapabilities.setStatus(
        "current"
    )

f3AMPClientCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 39)
)
if mibBuilder.loadTexts:
    f3AMPClientCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3AMPClientCapabilities.setStatus(
        "current"
    )

f3AMPServerCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 40)
)
if mibBuilder.loadTexts:
    f3AMPServerCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3AMPServerCapabilities.setStatus(
        "current"
    )

f3Nid114HCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 41)
)
if mibBuilder.loadTexts:
    f3Nid114HCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid114HCapabilities.setStatus(
        "current"
    )

f3Nid114PHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 42)
)
if mibBuilder.loadTexts:
    f3Nid114PHCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid114PHCapabilities.setStatus(
        "current"
    )

f3ERPCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 43)
)
if mibBuilder.loadTexts:
    f3ERPCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3ERPCapabilities.setStatus(
        "current"
    )

f3ShgCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 44)
)
if mibBuilder.loadTexts:
    f3ShgCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3ShgCapabilities.setStatus(
        "current"
    )

f3Nid114SCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 45)
)
if mibBuilder.loadTexts:
    f3Nid114SCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid114SCapabilities.setStatus(
        "current"
    )

f3Nid114SHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 46)
)
if mibBuilder.loadTexts:
    f3Nid114SHCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Nid114SHCapabilities.setStatus(
        "current"
    )

f3Ipv6Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 47)
)
if mibBuilder.loadTexts:
    f3Ipv6Capabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3Ipv6Capabilities.setStatus(
        "current"
    )

f3SatCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 48)
)
if mibBuilder.loadTexts:
    f3SatCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3SatCapabilities.setStatus(
        "current"
    )

f3JdsuCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 49)
)
if mibBuilder.loadTexts:
    f3JdsuCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3JdsuCapabilities.setStatus(
        "current"
    )

f3PortMirrorCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 50)
)
if mibBuilder.loadTexts:
    f3PortMirrorCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3PortMirrorCapabilities.setStatus(
        "current"
    )

f3JdsuGeneratorCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 51)
)
if mibBuilder.loadTexts:
    f3JdsuGeneratorCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3JdsuGeneratorCapabilities.setStatus(
        "current"
    )

f3TwampCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 52)
)
if mibBuilder.loadTexts:
    f3TwampCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3TwampCapabilities.setStatus(
        "current"
    )

f3OspfCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 53)
)
if mibBuilder.loadTexts:
    f3OspfCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3OspfCapabilities.setStatus(
        "current"
    )

f3Mef35Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 54)
)
if mibBuilder.loadTexts:
    f3Mef35Capabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Mef35Capabilities.setStatus(
        "current"
    )

f3Nid112ProCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 55)
)
if mibBuilder.loadTexts:
    f3Nid112ProCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid112ProCapabilities.setStatus(
        "current"
    )

f3Nid112ProMCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 56)
)
if mibBuilder.loadTexts:
    f3Nid112ProMCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid112ProMCapabilities.setStatus(
        "current"
    )

f3Nid114ProCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 57)
)
if mibBuilder.loadTexts:
    f3Nid114ProCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114ProCapabilities.setStatus(
        "current"
    )

f3Nid114ProCCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 58)
)
if mibBuilder.loadTexts:
    f3Nid114ProCCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114ProCCapabilities.setStatus(
        "current"
    )

f3Nid114ProSHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 59)
)
if mibBuilder.loadTexts:
    f3Nid114ProSHCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114ProSHCapabilities.setStatus(
        "current"
    )

f3Nid114ProCSHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 60)
)
if mibBuilder.loadTexts:
    f3Nid114ProCSHCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114ProCSHCapabilities.setStatus(
        "current"
    )

f3Nid114ProHECapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 61)
)
if mibBuilder.loadTexts:
    f3Nid114ProHECapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114ProHECapabilities.setStatus(
        "current"
    )

f3Nid112ProHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 62)
)
if mibBuilder.loadTexts:
    f3Nid112ProHCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid112ProHCapabilities.setStatus(
        "current"
    )

f3ConnectGuardCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 63)
)
if mibBuilder.loadTexts:
    f3ConnectGuardCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3ConnectGuardCapabilities.setStatus(
        "current"
    )

f3L3Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 64)
)
if mibBuilder.loadTexts:
    f3L3Capabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3L3Capabilities.setStatus(
        "current"
    )

f3Nid114GCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 65)
)
if mibBuilder.loadTexts:
    f3Nid114GCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114GCapabilities.setStatus(
        "current"
    )

f3BfdCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 66)
)
if mibBuilder.loadTexts:
    f3BfdCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3BfdCapabilities.setStatus(
        "current"
    )

f3EoMplsCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 67)
)
if mibBuilder.loadTexts:
    f3EoMplsCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3EoMplsCapabilities.setStatus(
        "current"
    )

f3FpmCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 68)
)
if mibBuilder.loadTexts:
    f3FpmCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3FpmCapabilities.setStatus(
        "current"
    )

f3Nid114ProVMHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 69)
)
if mibBuilder.loadTexts:
    f3Nid114ProVMHCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114ProVMHCapabilities.setStatus(
        "current"
    )

f3Nid114ProVMCHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 70)
)
if mibBuilder.loadTexts:
    f3Nid114ProVMCHCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114ProVMCHCapabilities.setStatus(
        "current"
    )

f3Nid114ProVMCSHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 71)
)
if mibBuilder.loadTexts:
    f3Nid114ProVMCSHCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114ProVMCSHCapabilities.setStatus(
        "current"
    )

f3NidGe101ProCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 72)
)
if mibBuilder.loadTexts:
    f3NidGe101ProCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3NidGe101ProCapabilities.setStatus(
        "current"
    )

f3NidGo102ProSCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 73)
)
if mibBuilder.loadTexts:
    f3NidGo102ProSCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3NidGo102ProSCapabilities.setStatus(
        "current"
    )

f3NidGo102ProSPCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 74)
)
if mibBuilder.loadTexts:
    f3NidGo102ProSPCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3NidGo102ProSPCapabilities.setStatus(
        "current"
    )

f3NidCx101Pro30ACapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 75)
)
if mibBuilder.loadTexts:
    f3NidCx101Pro30ACapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3NidCx101Pro30ACapabilities.setStatus(
        "current"
    )

f3NidCx102Pro30ACapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 76)
)
if mibBuilder.loadTexts:
    f3NidCx102Pro30ACapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3NidCx102Pro30ACapabilities.setStatus(
        "current"
    )

f3IpfixCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 77)
)
if mibBuilder.loadTexts:
    f3IpfixCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3IpfixCapabilities.setStatus(
        "current"
    )

f3VxlanCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 78)
)
if mibBuilder.loadTexts:
    f3VxlanCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3VxlanCapabilities.setStatus(
        "current"
    )

f3GreCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 79)
)
if mibBuilder.loadTexts:
    f3GreCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3GreCapabilities.setStatus(
        "current"
    )

f3NtpCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 80)
)
if mibBuilder.loadTexts:
    f3NtpCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3NtpCapabilities.setStatus(
        "current"
    )

f3ElpCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 81)
)
if mibBuilder.loadTexts:
    f3ElpCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3ElpCapabilities.setStatus(
        "current"
    )

f3NidXG116PROCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 82)
)
if mibBuilder.loadTexts:
    f3NidXG116PROCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3NidXG116PROCapabilities.setStatus(
        "current"
    )

f3NidXG120PROCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 83)
)
if mibBuilder.loadTexts:
    f3NidXG120PROCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3NidXG120PROCapabilities.setStatus(
        "current"
    )

f3FacilityCapabilitiesXGPRO = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 84)
)
if mibBuilder.loadTexts:
    f3FacilityCapabilitiesXGPRO.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3FacilityCapabilitiesXGPRO.setStatus(
        "current"
    )

f3EoMplsCapabilitiesXG = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 85)
)
if mibBuilder.loadTexts:
    f3EoMplsCapabilitiesXG.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3EoMplsCapabilitiesXG.setStatus(
        "current"
    )

f3Nid112ProVMCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 86)
)
if mibBuilder.loadTexts:
    f3Nid112ProVMCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid112ProVMCapabilities.setStatus(
        "current"
    )

f3SystemCommonCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 87)
)
if mibBuilder.loadTexts:
    f3SystemCommonCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3SystemCommonCapabilities.setStatus(
        "current"
    )

f3NidXG116PROHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 88)
)
if mibBuilder.loadTexts:
    f3NidXG116PROHCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3NidXG116PROHCapabilities.setStatus(
        "current"
    )

f3NidGo102ProSMCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 89)
)
if mibBuilder.loadTexts:
    f3NidGo102ProSMCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3NidGo102ProSMCapabilities.setStatus(
        "current"
    )

f3NidXG118PROSHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 90)
)
if mibBuilder.loadTexts:
    f3NidXG118PROSHCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3NidXG118PROSHCapabilities.setStatus(
        "current"
    )

f3L3CapabilitiesGE = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 91)
)
if mibBuilder.loadTexts:
    f3L3CapabilitiesGE.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3L3CapabilitiesGE.setStatus(
        "current"
    )

f3L3TrafficOSPFCapabilties = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 92)
)
if mibBuilder.loadTexts:
    f3L3TrafficOSPFCapabilties.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3L3TrafficOSPFCapabilties.setStatus(
        "current"
    )

f3L3TrafficBGPCapabilties = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 93)
)
if mibBuilder.loadTexts:
    f3L3TrafficBGPCapabilties.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3L3TrafficBGPCapabilties.setStatus(
        "current"
    )

f3L3TrafficIPv6Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 94)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPv6Capabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3L3TrafficIPv6Capabilities.setStatus(
        "current"
    )

f3NidXG118PROACSHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 95)
)
if mibBuilder.loadTexts:
    f3NidXG118PROACSHCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3NidXG118PROACSHCapabilities.setStatus(
        "current"
    )

f3Nid114ProVMSHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 96)
)
if mibBuilder.loadTexts:
    f3Nid114ProVMSHCapabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Nid114ProVMSHCapabilities.setStatus(
        "current"
    )

f3NidGe104Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 97)
)
if mibBuilder.loadTexts:
    f3NidGe104Capabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3NidGe104Capabilities.setStatus(
        "current"
    )

f3NidXG120PROSHCapabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 98)
)
if mibBuilder.loadTexts:
    f3NidXG120PROSHCapabilities.setProductRelease("F3 - family of products")
if mibBuilder.loadTexts:
    f3NidXG120PROSHCapabilities.setStatus(
        "current"
    )

f3Rfc2544Capabilities = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2, 1, 1, 99)
)
if mibBuilder.loadTexts:
    f3Rfc2544Capabilities.setProductRelease("F3- family of products")
if mibBuilder.loadTexts:
    f3Rfc2544Capabilities.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-CAPABILITIES-MIB",
    **{"f3CapabilityMIB": f3CapabilityMIB,
       "f3CapabilityDefinitions": f3CapabilityDefinitions,
       "f3BaseStandardsCapabilities": f3BaseStandardsCapabilities,
       "f3StandardIfEntityCapabilities": f3StandardIfEntityCapabilities,
       "f3StandardTargetNotifCapabilities": f3StandardTargetNotifCapabilities,
       "f3StandardSecurityCapabilities": f3StandardSecurityCapabilities,
       "f3StandardRMONCapabilities": f3StandardRMONCapabilities,
       "f3StandardCfmCapabilities": f3StandardCfmCapabilities,
       "f3StandardBridgeCapabilities": f3StandardBridgeCapabilities,
       "f3StandardLAGCapabilities": f3StandardLAGCapabilities,
       "f3CommonVendorSpecificCapabilities": f3CommonVendorSpecificCapabilities,
       "f3FacilityCapabilities": f3FacilityCapabilities,
       "f3Nid206Capabilities": f3Nid206Capabilities,
       "f3Nid201SyncECapabilities": f3Nid201SyncECapabilities,
       "f3Nid201NonSyncECapabilities": f3Nid201NonSyncECapabilities,
       "f3Nid206FCapabilities": f3Nid206FCapabilities,
       "f3Nid112Capabilities": f3Nid112Capabilities,
       "f3Nid114Capabilities": f3Nid114Capabilities,
       "f3EcpaCapabilities": f3EcpaCapabilities,
       "f3EsaCapabilities": f3EsaCapabilities,
       "f3BridgeCapabilitiesCmHub": f3BridgeCapabilitiesCmHub,
       "f3CommonVendorSpecificCapabilitiesCmHub": f3CommonVendorSpecificCapabilitiesCmHub,
       "f3FacilityCapabilitiesCmHub": f3FacilityCapabilitiesCmHub,
       "f3EntityCmHubCapabilities": f3EntityCmHubCapabilities,
       "f3Nid206VCapabilities": f3Nid206VCapabilities,
       "f3NidXG210Capabilities": f3NidXG210Capabilities,
       "f3PtpCapabilities": f3PtpCapabilities,
       "f3PseudoWireCapabilities": f3PseudoWireCapabilities,
       "f3DS1Capabilities": f3DS1Capabilities,
       "f3SonetCapabilities": f3SonetCapabilities,
       "f3SyncECapabilities": f3SyncECapabilities,
       "f3CfmCapabilities": f3CfmCapabilities,
       "f3LAGCapabilities": f3LAGCapabilities,
       "f3PBBCapabilities": f3PBBCapabilities,
       "f3Nid1804Capabilities": f3Nid1804Capabilities,
       "f3Nid3204Capabilities": f3Nid3204Capabilities,
       "f3BertCapabilities": f3BertCapabilities,
       "f3NidSyncProbeCapabilities": f3NidSyncProbeCapabilities,
       "f3SyncJackCapabilities": f3SyncJackCapabilities,
       "f3EsmCapabilities": f3EsmCapabilities,
       "f3AMPClientCapabilities": f3AMPClientCapabilities,
       "f3AMPServerCapabilities": f3AMPServerCapabilities,
       "f3Nid114HCapabilities": f3Nid114HCapabilities,
       "f3Nid114PHCapabilities": f3Nid114PHCapabilities,
       "f3ERPCapabilities": f3ERPCapabilities,
       "f3ShgCapabilities": f3ShgCapabilities,
       "f3Nid114SCapabilities": f3Nid114SCapabilities,
       "f3Nid114SHCapabilities": f3Nid114SHCapabilities,
       "f3Ipv6Capabilities": f3Ipv6Capabilities,
       "f3SatCapabilities": f3SatCapabilities,
       "f3JdsuCapabilities": f3JdsuCapabilities,
       "f3PortMirrorCapabilities": f3PortMirrorCapabilities,
       "f3JdsuGeneratorCapabilities": f3JdsuGeneratorCapabilities,
       "f3TwampCapabilities": f3TwampCapabilities,
       "f3OspfCapabilities": f3OspfCapabilities,
       "f3Mef35Capabilities": f3Mef35Capabilities,
       "f3Nid112ProCapabilities": f3Nid112ProCapabilities,
       "f3Nid112ProMCapabilities": f3Nid112ProMCapabilities,
       "f3Nid114ProCapabilities": f3Nid114ProCapabilities,
       "f3Nid114ProCCapabilities": f3Nid114ProCCapabilities,
       "f3Nid114ProSHCapabilities": f3Nid114ProSHCapabilities,
       "f3Nid114ProCSHCapabilities": f3Nid114ProCSHCapabilities,
       "f3Nid114ProHECapabilities": f3Nid114ProHECapabilities,
       "f3Nid112ProHCapabilities": f3Nid112ProHCapabilities,
       "f3ConnectGuardCapabilities": f3ConnectGuardCapabilities,
       "f3L3Capabilities": f3L3Capabilities,
       "f3Nid114GCapabilities": f3Nid114GCapabilities,
       "f3BfdCapabilities": f3BfdCapabilities,
       "f3EoMplsCapabilities": f3EoMplsCapabilities,
       "f3FpmCapabilities": f3FpmCapabilities,
       "f3Nid114ProVMHCapabilities": f3Nid114ProVMHCapabilities,
       "f3Nid114ProVMCHCapabilities": f3Nid114ProVMCHCapabilities,
       "f3Nid114ProVMCSHCapabilities": f3Nid114ProVMCSHCapabilities,
       "f3NidGe101ProCapabilities": f3NidGe101ProCapabilities,
       "f3NidGo102ProSCapabilities": f3NidGo102ProSCapabilities,
       "f3NidGo102ProSPCapabilities": f3NidGo102ProSPCapabilities,
       "f3NidCx101Pro30ACapabilities": f3NidCx101Pro30ACapabilities,
       "f3NidCx102Pro30ACapabilities": f3NidCx102Pro30ACapabilities,
       "f3IpfixCapabilities": f3IpfixCapabilities,
       "f3VxlanCapabilities": f3VxlanCapabilities,
       "f3GreCapabilities": f3GreCapabilities,
       "f3NtpCapabilities": f3NtpCapabilities,
       "f3ElpCapabilities": f3ElpCapabilities,
       "f3NidXG116PROCapabilities": f3NidXG116PROCapabilities,
       "f3NidXG120PROCapabilities": f3NidXG120PROCapabilities,
       "f3FacilityCapabilitiesXGPRO": f3FacilityCapabilitiesXGPRO,
       "f3EoMplsCapabilitiesXG": f3EoMplsCapabilitiesXG,
       "f3Nid112ProVMCapabilities": f3Nid112ProVMCapabilities,
       "f3SystemCommonCapabilities": f3SystemCommonCapabilities,
       "f3NidXG116PROHCapabilities": f3NidXG116PROHCapabilities,
       "f3NidGo102ProSMCapabilities": f3NidGo102ProSMCapabilities,
       "f3NidXG118PROSHCapabilities": f3NidXG118PROSHCapabilities,
       "f3L3CapabilitiesGE": f3L3CapabilitiesGE,
       "f3L3TrafficOSPFCapabilties": f3L3TrafficOSPFCapabilties,
       "f3L3TrafficBGPCapabilties": f3L3TrafficBGPCapabilties,
       "f3L3TrafficIPv6Capabilities": f3L3TrafficIPv6Capabilities,
       "f3NidXG118PROACSHCapabilities": f3NidXG118PROACSHCapabilities,
       "f3Nid114ProVMSHCapabilities": f3Nid114ProVMSHCapabilities,
       "f3NidGe104Capabilities": f3NidGe104Capabilities,
       "f3NidXG120PROSHCapabilities": f3NidXG120PROSHCapabilities,
       "f3Rfc2544Capabilities": f3Rfc2544Capabilities}
)
