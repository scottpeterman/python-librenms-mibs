# SNMP MIB module (ZTE-AN-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\zte\ZTE-AN-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:41 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

zxAccessNode = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082)
)
if mibBuilder.loadTexts:
    zxAccessNode.setRevisions(
        ("2016-10-19 00:00",
         "2015-04-01 00:00",
         "2011-07-04 00:00",
         "2011-05-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxAnEquipment_ObjectIdentity = ObjectIdentity
zxAnEquipment = _ZxAnEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10)
)
if mibBuilder.loadTexts:
    zxAnEquipment.setStatus("current")
_ZxAnSystem_ObjectIdentity = ObjectIdentity
zxAnSystem = _ZxAnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20)
)
if mibBuilder.loadTexts:
    zxAnSystem.setStatus("current")
_ZxAnInterface_ObjectIdentity = ObjectIdentity
zxAnInterface = _ZxAnInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 30)
)
if mibBuilder.loadTexts:
    zxAnInterface.setStatus("current")
_ZxAnBridge_ObjectIdentity = ObjectIdentity
zxAnBridge = _ZxAnBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 40)
)
if mibBuilder.loadTexts:
    zxAnBridge.setStatus("current")
_ZxAnQos_ObjectIdentity = ObjectIdentity
zxAnQos = _ZxAnQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 50)
)
if mibBuilder.loadTexts:
    zxAnQos.setStatus("current")
_ZxAnMulticast_ObjectIdentity = ObjectIdentity
zxAnMulticast = _ZxAnMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 60)
)
if mibBuilder.loadTexts:
    zxAnMulticast.setStatus("current")
_ZxAnServiceSecurity_ObjectIdentity = ObjectIdentity
zxAnServiceSecurity = _ZxAnServiceSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 70)
)
if mibBuilder.loadTexts:
    zxAnServiceSecurity.setStatus("current")
_ZxAnOam_ObjectIdentity = ObjectIdentity
zxAnOam = _ZxAnOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 80)
)
if mibBuilder.loadTexts:
    zxAnOam.setStatus("current")
_ZxAnLayer3_ObjectIdentity = ObjectIdentity
zxAnLayer3 = _ZxAnLayer3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 90)
)
if mibBuilder.loadTexts:
    zxAnLayer3.setStatus("current")
_ZxAnVoice_ObjectIdentity = ObjectIdentity
zxAnVoice = _ZxAnVoice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 100)
)
if mibBuilder.loadTexts:
    zxAnVoice.setStatus("current")
_ZxAnServiceProvision_ObjectIdentity = ObjectIdentity
zxAnServiceProvision = _ZxAnServiceProvision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 110)
)
if mibBuilder.loadTexts:
    zxAnServiceProvision.setStatus("current")
_ZxAnClockSync_ObjectIdentity = ObjectIdentity
zxAnClockSync = _ZxAnClockSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 120)
)
if mibBuilder.loadTexts:
    zxAnClockSync.setStatus("current")
_ZxAnDsl_ObjectIdentity = ObjectIdentity
zxAnDsl = _ZxAnDsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 130)
)
if mibBuilder.loadTexts:
    zxAnDsl.setStatus("current")
_ZxAnCes_ObjectIdentity = ObjectIdentity
zxAnCes = _ZxAnCes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 140)
)
if mibBuilder.loadTexts:
    zxAnCes.setStatus("current")
_ZxAnVideo_ObjectIdentity = ObjectIdentity
zxAnVideo = _ZxAnVideo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 150)
)
if mibBuilder.loadTexts:
    zxAnVideo.setStatus("current")
_ZxAnPon_ObjectIdentity = ObjectIdentity
zxAnPon = _ZxAnPon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 500)
)
if mibBuilder.loadTexts:
    zxAnPon.setStatus("current")
_ZxAnMpls_ObjectIdentity = ObjectIdentity
zxAnMpls = _ZxAnMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 505)
)
if mibBuilder.loadTexts:
    zxAnMpls.setStatus("current")
_ZxAnWireless_ObjectIdentity = ObjectIdentity
zxAnWireless = _ZxAnWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 510)
)
_ZxAnVrg_ObjectIdentity = ObjectIdentity
zxAnVrg = _ZxAnVrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 515)
)
if mibBuilder.loadTexts:
    zxAnVrg.setStatus("current")
_ZxAnVnd_ObjectIdentity = ObjectIdentity
zxAnVnd = _ZxAnVnd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 530)
)
if mibBuilder.loadTexts:
    zxAnVnd.setStatus("current")
_ZxAnAgentCapability_ObjectIdentity = ObjectIdentity
zxAnAgentCapability = _ZxAnAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000)
)
if mibBuilder.loadTexts:
    zxAnAgentCapability.setStatus("current")
_ZxAnStandardMibAgentCapability_ObjectIdentity = ObjectIdentity
zxAnStandardMibAgentCapability = _ZxAnStandardMibAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 10)
)
_IpCapability_ObjectIdentity = ObjectIdentity
ipCapability = _IpCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 10, 10)
)
_ZxAnPrivateMibAgentCapability_ObjectIdentity = ObjectIdentity
zxAnPrivateMibAgentCapability = _ZxAnPrivateMibAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20)
)
_ZxAnEquipmentCapability_ObjectIdentity = ObjectIdentity
zxAnEquipmentCapability = _ZxAnEquipmentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 10)
)
_ZxAnSystemCapability_ObjectIdentity = ObjectIdentity
zxAnSystemCapability = _ZxAnSystemCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 20)
)
_ZxAnInterfaceCapability_ObjectIdentity = ObjectIdentity
zxAnInterfaceCapability = _ZxAnInterfaceCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 30)
)
_ZxAnBridgeCapability_ObjectIdentity = ObjectIdentity
zxAnBridgeCapability = _ZxAnBridgeCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 40)
)
_ZxAnQosAgentCapability_ObjectIdentity = ObjectIdentity
zxAnQosAgentCapability = _ZxAnQosAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 50)
)
_ZxAnMulticastCapability_ObjectIdentity = ObjectIdentity
zxAnMulticastCapability = _ZxAnMulticastCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 60)
)
_ZxAnServiceSecurityCapability_ObjectIdentity = ObjectIdentity
zxAnServiceSecurityCapability = _ZxAnServiceSecurityCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 70)
)
_ZxAnOamCapability_ObjectIdentity = ObjectIdentity
zxAnOamCapability = _ZxAnOamCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 80)
)
_ZxAnLayer3Capability_ObjectIdentity = ObjectIdentity
zxAnLayer3Capability = _ZxAnLayer3Capability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 90)
)
_ZxAnVoiceCapability_ObjectIdentity = ObjectIdentity
zxAnVoiceCapability = _ZxAnVoiceCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 100)
)
_ZxAnServiceProvisionCapability_ObjectIdentity = ObjectIdentity
zxAnServiceProvisionCapability = _ZxAnServiceProvisionCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 110)
)
_ZxAnClockSyncCapability_ObjectIdentity = ObjectIdentity
zxAnClockSyncCapability = _ZxAnClockSyncCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 120)
)
_ZxAnPonCapability_ObjectIdentity = ObjectIdentity
zxAnPonCapability = _ZxAnPonCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 500)
)
_ZxAnMplsCapability_ObjectIdentity = ObjectIdentity
zxAnMplsCapability = _ZxAnMplsCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 505)
)
_ZxAnWirelessCapability_ObjectIdentity = ObjectIdentity
zxAnWirelessCapability = _ZxAnWirelessCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 510)
)
_ZxAnVrgCapability_ObjectIdentity = ObjectIdentity
zxAnVrgCapability = _ZxAnVrgCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 515)
)
_ZnAnVndCapability_ObjectIdentity = ObjectIdentity
znAnVndCapability = _ZnAnVndCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1000, 20, 530)
)
_ZxAnProducts_ObjectIdentity = ObjectIdentity
zxAnProducts = _ZxAnProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 1001)
)
if mibBuilder.loadTexts:
    zxAnProducts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-SMI",
    **{"zte": zte,
       "zxAccessNode": zxAccessNode,
       "zxAnEquipment": zxAnEquipment,
       "zxAnSystem": zxAnSystem,
       "zxAnInterface": zxAnInterface,
       "zxAnBridge": zxAnBridge,
       "zxAnQos": zxAnQos,
       "zxAnMulticast": zxAnMulticast,
       "zxAnServiceSecurity": zxAnServiceSecurity,
       "zxAnOam": zxAnOam,
       "zxAnLayer3": zxAnLayer3,
       "zxAnVoice": zxAnVoice,
       "zxAnServiceProvision": zxAnServiceProvision,
       "zxAnClockSync": zxAnClockSync,
       "zxAnDsl": zxAnDsl,
       "zxAnCes": zxAnCes,
       "zxAnVideo": zxAnVideo,
       "zxAnPon": zxAnPon,
       "zxAnMpls": zxAnMpls,
       "zxAnWireless": zxAnWireless,
       "zxAnVrg": zxAnVrg,
       "zxAnVnd": zxAnVnd,
       "zxAnAgentCapability": zxAnAgentCapability,
       "zxAnStandardMibAgentCapability": zxAnStandardMibAgentCapability,
       "ipCapability": ipCapability,
       "zxAnPrivateMibAgentCapability": zxAnPrivateMibAgentCapability,
       "zxAnEquipmentCapability": zxAnEquipmentCapability,
       "zxAnSystemCapability": zxAnSystemCapability,
       "zxAnInterfaceCapability": zxAnInterfaceCapability,
       "zxAnBridgeCapability": zxAnBridgeCapability,
       "zxAnQosAgentCapability": zxAnQosAgentCapability,
       "zxAnMulticastCapability": zxAnMulticastCapability,
       "zxAnServiceSecurityCapability": zxAnServiceSecurityCapability,
       "zxAnOamCapability": zxAnOamCapability,
       "zxAnLayer3Capability": zxAnLayer3Capability,
       "zxAnVoiceCapability": zxAnVoiceCapability,
       "zxAnServiceProvisionCapability": zxAnServiceProvisionCapability,
       "zxAnClockSyncCapability": zxAnClockSyncCapability,
       "zxAnPonCapability": zxAnPonCapability,
       "zxAnMplsCapability": zxAnMplsCapability,
       "zxAnWirelessCapability": zxAnWirelessCapability,
       "zxAnVrgCapability": zxAnVrgCapability,
       "znAnVndCapability": znAnVndCapability,
       "zxAnProducts": zxAnProducts}
)
