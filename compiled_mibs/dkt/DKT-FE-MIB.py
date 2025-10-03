# SNMP MIB module (DKT-FE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dkt\DKT-FE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:27 2025
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

(dkt,) = mibBuilder.importSymbols(
    "DKT-MIB",
    "dkt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

feMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FeSwitchEngine_ObjectIdentity = ObjectIdentity
feSwitchEngine = _FeSwitchEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 12, 1)
)


class _FeATU_Type(OctetString):
    """Custom type feATU based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20480),
    )


_FeATU_Type.__name__ = "OctetString"
_FeATU_Object = MibScalar
feATU = _FeATU_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 1, 1),
    _FeATU_Type()
)
feATU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feATU.setStatus("current")


class _FeUnicastDelete_Type(OctetString):
    """Custom type feUnicastDelete based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeUnicastDelete_Type.__name__ = "OctetString"
_FeUnicastDelete_Object = MibScalar
feUnicastDelete = _FeUnicastDelete_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 1, 2),
    _FeUnicastDelete_Type()
)
feUnicastDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feUnicastDelete.setStatus("current")
_FeMulticastDelete_Type = IpAddress
_FeMulticastDelete_Object = MibScalar
feMulticastDelete = _FeMulticastDelete_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 1, 3),
    _FeMulticastDelete_Type()
)
feMulticastDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feMulticastDelete.setStatus("current")


class _FeIGMPSnooping_Type(Integer32):
    """Custom type feIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeIGMPSnooping_Type.__name__ = "Integer32"
_FeIGMPSnooping_Object = MibScalar
feIGMPSnooping = _FeIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 1, 4),
    _FeIGMPSnooping_Type()
)
feIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feIGMPSnooping.setStatus("current")


class _FeVTU_Type(OctetString):
    """Custom type feVTU based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9600),
    )


_FeVTU_Type.__name__ = "OctetString"
_FeVTU_Object = MibScalar
feVTU = _FeVTU_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 1, 5),
    _FeVTU_Type()
)
feVTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feVTU.setStatus("current")


class _FeVLANCreate_Type(OctetString):
    """Custom type feVLANCreate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeVLANCreate_Type.__name__ = "OctetString"
_FeVLANCreate_Object = MibScalar
feVLANCreate = _FeVLANCreate_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 1, 6),
    _FeVLANCreate_Type()
)
feVLANCreate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feVLANCreate.setStatus("current")


class _FeVLANDelete_Type(Integer32):
    """Custom type feVLANDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_FeVLANDelete_Type.__name__ = "Integer32"
_FeVLANDelete_Object = MibScalar
feVLANDelete = _FeVLANDelete_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 1, 7),
    _FeVLANDelete_Type()
)
feVLANDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feVLANDelete.setStatus("current")


class _FeClearVTU_Type(Integer32):
    """Custom type feClearVTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_FeClearVTU_Type.__name__ = "Integer32"
_FeClearVTU_Object = MibScalar
feClearVTU = _FeClearVTU_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 1, 8),
    _FeClearVTU_Type()
)
feClearVTU.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feClearVTU.setStatus("current")


class _FeDumpPIRLBuckets_Type(OctetString):
    """Custom type feDumpPIRLBuckets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FeDumpPIRLBuckets_Type.__name__ = "OctetString"
_FeDumpPIRLBuckets_Object = MibScalar
feDumpPIRLBuckets = _FeDumpPIRLBuckets_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 1, 9),
    _FeDumpPIRLBuckets_Type()
)
feDumpPIRLBuckets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDumpPIRLBuckets.setStatus("current")


class _FeDisablePIRLBucket_Type(Integer32):
    """Custom type feDisablePIRLBucket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_FeDisablePIRLBucket_Type.__name__ = "Integer32"
_FeDisablePIRLBucket_Object = MibScalar
feDisablePIRLBucket = _FeDisablePIRLBucket_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 1, 10),
    _FeDisablePIRLBucket_Type()
)
feDisablePIRLBucket.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feDisablePIRLBucket.setStatus("current")


class _FeVLANProviderMode_Type(Integer32):
    """Custom type feVLANProviderMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeVLANProviderMode_Type.__name__ = "Integer32"
_FeVLANProviderMode_Object = MibScalar
feVLANProviderMode = _FeVLANProviderMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 1, 11),
    _FeVLANProviderMode_Type()
)
feVLANProviderMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feVLANProviderMode.setStatus("current")
_FePorts_ObjectIdentity = ObjectIdentity
fePorts = _FePorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2)
)
_FeCPUPort_ObjectIdentity = ObjectIdentity
feCPUPort = _FeCPUPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1)
)


class _FeCPUPortAutoNegotiation_Type(Integer32):
    """Custom type feCPUPortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FeCPUPortAutoNegotiation_Type.__name__ = "Integer32"
_FeCPUPortAutoNegotiation_Object = MibScalar
feCPUPortAutoNegotiation = _FeCPUPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 1),
    _FeCPUPortAutoNegotiation_Type()
)
feCPUPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortAutoNegotiation.setStatus("current")


class _FeCPUPortSpeedMode_Type(OctetString):
    """Custom type feCPUPortSpeedMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FeCPUPortSpeedMode_Type.__name__ = "OctetString"
_FeCPUPortSpeedMode_Object = MibScalar
feCPUPortSpeedMode = _FeCPUPortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 2),
    _FeCPUPortSpeedMode_Type()
)
feCPUPortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortSpeedMode.setStatus("current")


class _FeCPUPortLinkStatus_Type(Integer32):
    """Custom type feCPUPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeCPUPortLinkStatus_Type.__name__ = "Integer32"
_FeCPUPortLinkStatus_Object = MibScalar
feCPUPortLinkStatus = _FeCPUPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 3),
    _FeCPUPortLinkStatus_Type()
)
feCPUPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feCPUPortLinkStatus.setStatus("current")


class _FeCPUPortFlowControl_Type(Integer32):
    """Custom type feCPUPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeCPUPortFlowControl_Type.__name__ = "Integer32"
_FeCPUPortFlowControl_Object = MibScalar
feCPUPortFlowControl = _FeCPUPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 4),
    _FeCPUPortFlowControl_Type()
)
feCPUPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortFlowControl.setStatus("current")


class _FeCPUPortIEEEQoSPriority_Type(Integer32):
    """Custom type feCPUPortIEEEQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeCPUPortIEEEQoSPriority_Type.__name__ = "Integer32"
_FeCPUPortIEEEQoSPriority_Object = MibScalar
feCPUPortIEEEQoSPriority = _FeCPUPortIEEEQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 5),
    _FeCPUPortIEEEQoSPriority_Type()
)
feCPUPortIEEEQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortIEEEQoSPriority.setStatus("current")


class _FeCPUPortIPQoSPriority_Type(Integer32):
    """Custom type feCPUPortIPQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeCPUPortIPQoSPriority_Type.__name__ = "Integer32"
_FeCPUPortIPQoSPriority_Object = MibScalar
feCPUPortIPQoSPriority = _FeCPUPortIPQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 6),
    _FeCPUPortIPQoSPriority_Type()
)
feCPUPortIPQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortIPQoSPriority.setStatus("current")


class _FeCPUPortFramePriorityOverwrite_Type(OctetString):
    """Custom type feCPUPortFramePriorityOverwrite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeCPUPortFramePriorityOverwrite_Type.__name__ = "OctetString"
_FeCPUPortFramePriorityOverwrite_Object = MibScalar
feCPUPortFramePriorityOverwrite = _FeCPUPortFramePriorityOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 7),
    _FeCPUPortFramePriorityOverwrite_Type()
)
feCPUPortFramePriorityOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortFramePriorityOverwrite.setStatus("current")


class _FeCPUPortQueuePriorityOverwrite_Type(OctetString):
    """Custom type feCPUPortQueuePriorityOverwrite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeCPUPortQueuePriorityOverwrite_Type.__name__ = "OctetString"
_FeCPUPortQueuePriorityOverwrite_Object = MibScalar
feCPUPortQueuePriorityOverwrite = _FeCPUPortQueuePriorityOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 8),
    _FeCPUPortQueuePriorityOverwrite_Type()
)
feCPUPortQueuePriorityOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortQueuePriorityOverwrite.setStatus("current")


class _FeCPUPortQueuePriority_Type(OctetString):
    """Custom type feCPUPortQueuePriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeCPUPortQueuePriority_Type.__name__ = "OctetString"
_FeCPUPortQueuePriority_Object = MibScalar
feCPUPortQueuePriority = _FeCPUPortQueuePriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 9),
    _FeCPUPortQueuePriority_Type()
)
feCPUPortQueuePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortQueuePriority.setStatus("current")


class _FeCPUPortQoSPortMapRule_Type(Integer32):
    """Custom type feCPUPortQoSPortMapRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeCPUPortQoSPortMapRule_Type.__name__ = "Integer32"
_FeCPUPortQoSPortMapRule_Object = MibScalar
feCPUPortQoSPortMapRule = _FeCPUPortQoSPortMapRule_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 10),
    _FeCPUPortQoSPortMapRule_Type()
)
feCPUPortQoSPortMapRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortQoSPortMapRule.setStatus("current")


class _FeCPUPortVIDNRLEnable_Type(Integer32):
    """Custom type feCPUPortVIDNRLEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeCPUPortVIDNRLEnable_Type.__name__ = "Integer32"
_FeCPUPortVIDNRLEnable_Object = MibScalar
feCPUPortVIDNRLEnable = _FeCPUPortVIDNRLEnable_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 11),
    _FeCPUPortVIDNRLEnable_Type()
)
feCPUPortVIDNRLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortVIDNRLEnable.setStatus("current")


class _FeCPUPortMap2PIRL_Type(Integer32):
    """Custom type feCPUPortMap2PIRL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_FeCPUPortMap2PIRL_Type.__name__ = "Integer32"
_FeCPUPortMap2PIRL_Object = MibScalar
feCPUPortMap2PIRL = _FeCPUPortMap2PIRL_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 12),
    _FeCPUPortMap2PIRL_Type()
)
feCPUPortMap2PIRL.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feCPUPortMap2PIRL.setStatus("current")


class _FeCPUPortDeletePortMap2PIRL_Type(Integer32):
    """Custom type feCPUPortDeletePortMap2PIRL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_FeCPUPortDeletePortMap2PIRL_Type.__name__ = "Integer32"
_FeCPUPortDeletePortMap2PIRL_Object = MibScalar
feCPUPortDeletePortMap2PIRL = _FeCPUPortDeletePortMap2PIRL_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 13),
    _FeCPUPortDeletePortMap2PIRL_Type()
)
feCPUPortDeletePortMap2PIRL.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feCPUPortDeletePortMap2PIRL.setStatus("current")
_FeCPUPortEgressRateLimitation_Type = Integer32
_FeCPUPortEgressRateLimitation_Object = MibScalar
feCPUPortEgressRateLimitation = _FeCPUPortEgressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 14),
    _FeCPUPortEgressRateLimitation_Type()
)
feCPUPortEgressRateLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortEgressRateLimitation.setStatus("current")


class _FeCPUPortIngressRateLimitation_Type(OctetString):
    """Custom type feCPUPortIngressRateLimitation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeCPUPortIngressRateLimitation_Type.__name__ = "OctetString"
_FeCPUPortIngressRateLimitation_Object = MibScalar
feCPUPortIngressRateLimitation = _FeCPUPortIngressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 15),
    _FeCPUPortIngressRateLimitation_Type()
)
feCPUPortIngressRateLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortIngressRateLimitation.setStatus("current")
_FeCPUPortDefaultVLAN_Type = Integer32
_FeCPUPortDefaultVLAN_Object = MibScalar
feCPUPortDefaultVLAN = _FeCPUPortDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 16),
    _FeCPUPortDefaultVLAN_Type()
)
feCPUPortDefaultVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortDefaultVLAN.setStatus("current")


class _FeCPUPortForceDefaultVID_Type(Integer32):
    """Custom type feCPUPortForceDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeCPUPortForceDefaultVID_Type.__name__ = "Integer32"
_FeCPUPortForceDefaultVID_Object = MibScalar
feCPUPortForceDefaultVID = _FeCPUPortForceDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 17),
    _FeCPUPortForceDefaultVID_Type()
)
feCPUPortForceDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortForceDefaultVID.setStatus("current")


class _FeCPUPortVLANPortMode_Type(Integer32):
    """Custom type feCPUPortVLANPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FeCPUPortVLANPortMode_Type.__name__ = "Integer32"
_FeCPUPortVLANPortMode_Object = MibScalar
feCPUPortVLANPortMode = _FeCPUPortVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 18),
    _FeCPUPortVLANPortMode_Type()
)
feCPUPortVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortVLANPortMode.setStatus("current")


class _FeCPUPortBlockAllUnknown_Type(Integer32):
    """Custom type feCPUPortBlockAllUnknown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeCPUPortBlockAllUnknown_Type.__name__ = "Integer32"
_FeCPUPortBlockAllUnknown_Object = MibScalar
feCPUPortBlockAllUnknown = _FeCPUPortBlockAllUnknown_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 19),
    _FeCPUPortBlockAllUnknown_Type()
)
feCPUPortBlockAllUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortBlockAllUnknown.setStatus("current")


class _FeCPUPortIGMPSnooping_Type(Integer32):
    """Custom type feCPUPortIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeCPUPortIGMPSnooping_Type.__name__ = "Integer32"
_FeCPUPortIGMPSnooping_Object = MibScalar
feCPUPortIGMPSnooping = _FeCPUPortIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 20),
    _FeCPUPortIGMPSnooping_Type()
)
feCPUPortIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feCPUPortIGMPSnooping.setStatus("current")


class _FeCPUPortAddUnicast_Type(OctetString):
    """Custom type feCPUPortAddUnicast based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeCPUPortAddUnicast_Type.__name__ = "OctetString"
_FeCPUPortAddUnicast_Object = MibScalar
feCPUPortAddUnicast = _FeCPUPortAddUnicast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 21),
    _FeCPUPortAddUnicast_Type()
)
feCPUPortAddUnicast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feCPUPortAddUnicast.setStatus("current")
_FeCPUPortAddMulticast_Type = IpAddress
_FeCPUPortAddMulticast_Object = MibScalar
feCPUPortAddMulticast = _FeCPUPortAddMulticast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 1, 22),
    _FeCPUPortAddMulticast_Type()
)
feCPUPortAddMulticast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feCPUPortAddMulticast.setStatus("current")
_FeWANPort_ObjectIdentity = ObjectIdentity
feWANPort = _FeWANPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2)
)


class _FeWANPortAutoNegotiation_Type(Integer32):
    """Custom type feWANPortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FeWANPortAutoNegotiation_Type.__name__ = "Integer32"
_FeWANPortAutoNegotiation_Object = MibScalar
feWANPortAutoNegotiation = _FeWANPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 1),
    _FeWANPortAutoNegotiation_Type()
)
feWANPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortAutoNegotiation.setStatus("current")


class _FeWANPortSpeedMode_Type(OctetString):
    """Custom type feWANPortSpeedMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FeWANPortSpeedMode_Type.__name__ = "OctetString"
_FeWANPortSpeedMode_Object = MibScalar
feWANPortSpeedMode = _FeWANPortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 2),
    _FeWANPortSpeedMode_Type()
)
feWANPortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortSpeedMode.setStatus("current")


class _FeWANPortLinkStatus_Type(Integer32):
    """Custom type feWANPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeWANPortLinkStatus_Type.__name__ = "Integer32"
_FeWANPortLinkStatus_Object = MibScalar
feWANPortLinkStatus = _FeWANPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 3),
    _FeWANPortLinkStatus_Type()
)
feWANPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feWANPortLinkStatus.setStatus("current")


class _FeWANPortFlowControl_Type(Integer32):
    """Custom type feWANPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeWANPortFlowControl_Type.__name__ = "Integer32"
_FeWANPortFlowControl_Object = MibScalar
feWANPortFlowControl = _FeWANPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 4),
    _FeWANPortFlowControl_Type()
)
feWANPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortFlowControl.setStatus("current")


class _FeWANPortIEEEQoSPriority_Type(Integer32):
    """Custom type feWANPortIEEEQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeWANPortIEEEQoSPriority_Type.__name__ = "Integer32"
_FeWANPortIEEEQoSPriority_Object = MibScalar
feWANPortIEEEQoSPriority = _FeWANPortIEEEQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 5),
    _FeWANPortIEEEQoSPriority_Type()
)
feWANPortIEEEQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortIEEEQoSPriority.setStatus("current")


class _FeWANPortIPQoSPriority_Type(Integer32):
    """Custom type feWANPortIPQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeWANPortIPQoSPriority_Type.__name__ = "Integer32"
_FeWANPortIPQoSPriority_Object = MibScalar
feWANPortIPQoSPriority = _FeWANPortIPQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 6),
    _FeWANPortIPQoSPriority_Type()
)
feWANPortIPQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortIPQoSPriority.setStatus("current")


class _FeWANPortFramePriorityOverwrite_Type(OctetString):
    """Custom type feWANPortFramePriorityOverwrite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeWANPortFramePriorityOverwrite_Type.__name__ = "OctetString"
_FeWANPortFramePriorityOverwrite_Object = MibScalar
feWANPortFramePriorityOverwrite = _FeWANPortFramePriorityOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 7),
    _FeWANPortFramePriorityOverwrite_Type()
)
feWANPortFramePriorityOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortFramePriorityOverwrite.setStatus("current")


class _FeWANPortQueuePriorityOverwrite_Type(OctetString):
    """Custom type feWANPortQueuePriorityOverwrite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeWANPortQueuePriorityOverwrite_Type.__name__ = "OctetString"
_FeWANPortQueuePriorityOverwrite_Object = MibScalar
feWANPortQueuePriorityOverwrite = _FeWANPortQueuePriorityOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 8),
    _FeWANPortQueuePriorityOverwrite_Type()
)
feWANPortQueuePriorityOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortQueuePriorityOverwrite.setStatus("current")


class _FeWANPortQueuePriority_Type(OctetString):
    """Custom type feWANPortQueuePriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeWANPortQueuePriority_Type.__name__ = "OctetString"
_FeWANPortQueuePriority_Object = MibScalar
feWANPortQueuePriority = _FeWANPortQueuePriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 9),
    _FeWANPortQueuePriority_Type()
)
feWANPortQueuePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortQueuePriority.setStatus("current")


class _FeWANPortQoSPortMapRule_Type(Integer32):
    """Custom type feWANPortQoSPortMapRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeWANPortQoSPortMapRule_Type.__name__ = "Integer32"
_FeWANPortQoSPortMapRule_Object = MibScalar
feWANPortQoSPortMapRule = _FeWANPortQoSPortMapRule_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 10),
    _FeWANPortQoSPortMapRule_Type()
)
feWANPortQoSPortMapRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortQoSPortMapRule.setStatus("current")


class _FeWANPortVIDNRLEnable_Type(Integer32):
    """Custom type feWANPortVIDNRLEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeWANPortVIDNRLEnable_Type.__name__ = "Integer32"
_FeWANPortVIDNRLEnable_Object = MibScalar
feWANPortVIDNRLEnable = _FeWANPortVIDNRLEnable_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 11),
    _FeWANPortVIDNRLEnable_Type()
)
feWANPortVIDNRLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortVIDNRLEnable.setStatus("current")


class _FeWANPortMap2PIRL_Type(Integer32):
    """Custom type feWANPortMap2PIRL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_FeWANPortMap2PIRL_Type.__name__ = "Integer32"
_FeWANPortMap2PIRL_Object = MibScalar
feWANPortMap2PIRL = _FeWANPortMap2PIRL_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 12),
    _FeWANPortMap2PIRL_Type()
)
feWANPortMap2PIRL.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feWANPortMap2PIRL.setStatus("current")


class _FeWANPortDeletePortMap2PIRL_Type(Integer32):
    """Custom type feWANPortDeletePortMap2PIRL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_FeWANPortDeletePortMap2PIRL_Type.__name__ = "Integer32"
_FeWANPortDeletePortMap2PIRL_Object = MibScalar
feWANPortDeletePortMap2PIRL = _FeWANPortDeletePortMap2PIRL_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 13),
    _FeWANPortDeletePortMap2PIRL_Type()
)
feWANPortDeletePortMap2PIRL.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feWANPortDeletePortMap2PIRL.setStatus("current")
_FeWANPortEgressRateLimitation_Type = Integer32
_FeWANPortEgressRateLimitation_Object = MibScalar
feWANPortEgressRateLimitation = _FeWANPortEgressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 14),
    _FeWANPortEgressRateLimitation_Type()
)
feWANPortEgressRateLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortEgressRateLimitation.setStatus("current")


class _FeWANPortIngressRateLimitation_Type(OctetString):
    """Custom type feWANPortIngressRateLimitation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeWANPortIngressRateLimitation_Type.__name__ = "OctetString"
_FeWANPortIngressRateLimitation_Object = MibScalar
feWANPortIngressRateLimitation = _FeWANPortIngressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 15),
    _FeWANPortIngressRateLimitation_Type()
)
feWANPortIngressRateLimitation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feWANPortIngressRateLimitation.setStatus("current")
_FeWANPortDefaultVLAN_Type = Integer32
_FeWANPortDefaultVLAN_Object = MibScalar
feWANPortDefaultVLAN = _FeWANPortDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 16),
    _FeWANPortDefaultVLAN_Type()
)
feWANPortDefaultVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortDefaultVLAN.setStatus("current")


class _FeWANPortForceDefaultVID_Type(Integer32):
    """Custom type feWANPortForceDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeWANPortForceDefaultVID_Type.__name__ = "Integer32"
_FeWANPortForceDefaultVID_Object = MibScalar
feWANPortForceDefaultVID = _FeWANPortForceDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 17),
    _FeWANPortForceDefaultVID_Type()
)
feWANPortForceDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortForceDefaultVID.setStatus("current")


class _FeWANPortVLANPortMode_Type(Integer32):
    """Custom type feWANPortVLANPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FeWANPortVLANPortMode_Type.__name__ = "Integer32"
_FeWANPortVLANPortMode_Object = MibScalar
feWANPortVLANPortMode = _FeWANPortVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 18),
    _FeWANPortVLANPortMode_Type()
)
feWANPortVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortVLANPortMode.setStatus("current")


class _FeWANPortBlockAllUnknown_Type(Integer32):
    """Custom type feWANPortBlockAllUnknown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeWANPortBlockAllUnknown_Type.__name__ = "Integer32"
_FeWANPortBlockAllUnknown_Object = MibScalar
feWANPortBlockAllUnknown = _FeWANPortBlockAllUnknown_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 19),
    _FeWANPortBlockAllUnknown_Type()
)
feWANPortBlockAllUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortBlockAllUnknown.setStatus("current")


class _FeWANPortIGMPSnooping_Type(Integer32):
    """Custom type feWANPortIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeWANPortIGMPSnooping_Type.__name__ = "Integer32"
_FeWANPortIGMPSnooping_Object = MibScalar
feWANPortIGMPSnooping = _FeWANPortIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 20),
    _FeWANPortIGMPSnooping_Type()
)
feWANPortIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortIGMPSnooping.setStatus("current")


class _FeWANPortAddUnicast_Type(OctetString):
    """Custom type feWANPortAddUnicast based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeWANPortAddUnicast_Type.__name__ = "OctetString"
_FeWANPortAddUnicast_Object = MibScalar
feWANPortAddUnicast = _FeWANPortAddUnicast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 21),
    _FeWANPortAddUnicast_Type()
)
feWANPortAddUnicast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feWANPortAddUnicast.setStatus("current")
_FeWANPortAddMulticast_Type = IpAddress
_FeWANPortAddMulticast_Object = MibScalar
feWANPortAddMulticast = _FeWANPortAddMulticast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 22),
    _FeWANPortAddMulticast_Type()
)
feWANPortAddMulticast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feWANPortAddMulticast.setStatus("current")


class _FeWANPortArpMirroring_Type(Integer32):
    """Custom type feWANPortArpMirroring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeWANPortArpMirroring_Type.__name__ = "Integer32"
_FeWANPortArpMirroring_Object = MibScalar
feWANPortArpMirroring = _FeWANPortArpMirroring_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 2, 23),
    _FeWANPortArpMirroring_Type()
)
feWANPortArpMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feWANPortArpMirroring.setStatus("current")
_FeLAN1Port_ObjectIdentity = ObjectIdentity
feLAN1Port = _FeLAN1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3)
)


class _FeLAN1PortAutoNegotiation_Type(Integer32):
    """Custom type feLAN1PortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FeLAN1PortAutoNegotiation_Type.__name__ = "Integer32"
_FeLAN1PortAutoNegotiation_Object = MibScalar
feLAN1PortAutoNegotiation = _FeLAN1PortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 1),
    _FeLAN1PortAutoNegotiation_Type()
)
feLAN1PortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortAutoNegotiation.setStatus("current")


class _FeLAN1PortSpeedMode_Type(OctetString):
    """Custom type feLAN1PortSpeedMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FeLAN1PortSpeedMode_Type.__name__ = "OctetString"
_FeLAN1PortSpeedMode_Object = MibScalar
feLAN1PortSpeedMode = _FeLAN1PortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 2),
    _FeLAN1PortSpeedMode_Type()
)
feLAN1PortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortSpeedMode.setStatus("current")


class _FeLAN1PortLinkStatus_Type(Integer32):
    """Custom type feLAN1PortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN1PortLinkStatus_Type.__name__ = "Integer32"
_FeLAN1PortLinkStatus_Object = MibScalar
feLAN1PortLinkStatus = _FeLAN1PortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 3),
    _FeLAN1PortLinkStatus_Type()
)
feLAN1PortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feLAN1PortLinkStatus.setStatus("current")


class _FeLAN1PortFlowControl_Type(Integer32):
    """Custom type feLAN1PortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN1PortFlowControl_Type.__name__ = "Integer32"
_FeLAN1PortFlowControl_Object = MibScalar
feLAN1PortFlowControl = _FeLAN1PortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 4),
    _FeLAN1PortFlowControl_Type()
)
feLAN1PortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortFlowControl.setStatus("current")


class _FeLAN1PortIEEEQoSPriority_Type(Integer32):
    """Custom type feLAN1PortIEEEQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN1PortIEEEQoSPriority_Type.__name__ = "Integer32"
_FeLAN1PortIEEEQoSPriority_Object = MibScalar
feLAN1PortIEEEQoSPriority = _FeLAN1PortIEEEQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 5),
    _FeLAN1PortIEEEQoSPriority_Type()
)
feLAN1PortIEEEQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortIEEEQoSPriority.setStatus("current")


class _FeLAN1PortIPQoSPriority_Type(Integer32):
    """Custom type feLAN1PortIPQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN1PortIPQoSPriority_Type.__name__ = "Integer32"
_FeLAN1PortIPQoSPriority_Object = MibScalar
feLAN1PortIPQoSPriority = _FeLAN1PortIPQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 6),
    _FeLAN1PortIPQoSPriority_Type()
)
feLAN1PortIPQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortIPQoSPriority.setStatus("current")


class _FeLAN1PortFramePriorityOverwrite_Type(OctetString):
    """Custom type feLAN1PortFramePriorityOverwrite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN1PortFramePriorityOverwrite_Type.__name__ = "OctetString"
_FeLAN1PortFramePriorityOverwrite_Object = MibScalar
feLAN1PortFramePriorityOverwrite = _FeLAN1PortFramePriorityOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 7),
    _FeLAN1PortFramePriorityOverwrite_Type()
)
feLAN1PortFramePriorityOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortFramePriorityOverwrite.setStatus("current")


class _FeLAN1PortQueuePriorityOverwrite_Type(OctetString):
    """Custom type feLAN1PortQueuePriorityOverwrite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN1PortQueuePriorityOverwrite_Type.__name__ = "OctetString"
_FeLAN1PortQueuePriorityOverwrite_Object = MibScalar
feLAN1PortQueuePriorityOverwrite = _FeLAN1PortQueuePriorityOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 8),
    _FeLAN1PortQueuePriorityOverwrite_Type()
)
feLAN1PortQueuePriorityOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortQueuePriorityOverwrite.setStatus("current")


class _FeLAN1PortQueuePriority_Type(OctetString):
    """Custom type feLAN1PortQueuePriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN1PortQueuePriority_Type.__name__ = "OctetString"
_FeLAN1PortQueuePriority_Object = MibScalar
feLAN1PortQueuePriority = _FeLAN1PortQueuePriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 9),
    _FeLAN1PortQueuePriority_Type()
)
feLAN1PortQueuePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortQueuePriority.setStatus("current")


class _FeLAN1PortQoSPortMapRule_Type(Integer32):
    """Custom type feLAN1PortQoSPortMapRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN1PortQoSPortMapRule_Type.__name__ = "Integer32"
_FeLAN1PortQoSPortMapRule_Object = MibScalar
feLAN1PortQoSPortMapRule = _FeLAN1PortQoSPortMapRule_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 10),
    _FeLAN1PortQoSPortMapRule_Type()
)
feLAN1PortQoSPortMapRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortQoSPortMapRule.setStatus("current")


class _FeLAN1PortVIDNRLEnable_Type(Integer32):
    """Custom type feLAN1PortVIDNRLEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN1PortVIDNRLEnable_Type.__name__ = "Integer32"
_FeLAN1PortVIDNRLEnable_Object = MibScalar
feLAN1PortVIDNRLEnable = _FeLAN1PortVIDNRLEnable_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 11),
    _FeLAN1PortVIDNRLEnable_Type()
)
feLAN1PortVIDNRLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortVIDNRLEnable.setStatus("current")


class _FeLAN1PortMap2PIRL_Type(Integer32):
    """Custom type feLAN1PortMap2PIRL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_FeLAN1PortMap2PIRL_Type.__name__ = "Integer32"
_FeLAN1PortMap2PIRL_Object = MibScalar
feLAN1PortMap2PIRL = _FeLAN1PortMap2PIRL_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 12),
    _FeLAN1PortMap2PIRL_Type()
)
feLAN1PortMap2PIRL.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN1PortMap2PIRL.setStatus("current")


class _FeLAN1PortDeletePortMap2PIRL_Type(Integer32):
    """Custom type feLAN1PortDeletePortMap2PIRL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_FeLAN1PortDeletePortMap2PIRL_Type.__name__ = "Integer32"
_FeLAN1PortDeletePortMap2PIRL_Object = MibScalar
feLAN1PortDeletePortMap2PIRL = _FeLAN1PortDeletePortMap2PIRL_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 13),
    _FeLAN1PortDeletePortMap2PIRL_Type()
)
feLAN1PortDeletePortMap2PIRL.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN1PortDeletePortMap2PIRL.setStatus("current")
_FeLAN1PortEgressRateLimitation_Type = Integer32
_FeLAN1PortEgressRateLimitation_Object = MibScalar
feLAN1PortEgressRateLimitation = _FeLAN1PortEgressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 14),
    _FeLAN1PortEgressRateLimitation_Type()
)
feLAN1PortEgressRateLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortEgressRateLimitation.setStatus("current")


class _FeLAN1PortIngressRateLimitation_Type(OctetString):
    """Custom type feLAN1PortIngressRateLimitation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN1PortIngressRateLimitation_Type.__name__ = "OctetString"
_FeLAN1PortIngressRateLimitation_Object = MibScalar
feLAN1PortIngressRateLimitation = _FeLAN1PortIngressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 15),
    _FeLAN1PortIngressRateLimitation_Type()
)
feLAN1PortIngressRateLimitation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN1PortIngressRateLimitation.setStatus("current")
_FeLAN1PortDefaultVLAN_Type = Integer32
_FeLAN1PortDefaultVLAN_Object = MibScalar
feLAN1PortDefaultVLAN = _FeLAN1PortDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 16),
    _FeLAN1PortDefaultVLAN_Type()
)
feLAN1PortDefaultVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortDefaultVLAN.setStatus("current")


class _FeLAN1PortForceDefaultVID_Type(Integer32):
    """Custom type feLAN1PortForceDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN1PortForceDefaultVID_Type.__name__ = "Integer32"
_FeLAN1PortForceDefaultVID_Object = MibScalar
feLAN1PortForceDefaultVID = _FeLAN1PortForceDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 17),
    _FeLAN1PortForceDefaultVID_Type()
)
feLAN1PortForceDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortForceDefaultVID.setStatus("current")


class _FeLAN1PortVLANPortMode_Type(Integer32):
    """Custom type feLAN1PortVLANPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FeLAN1PortVLANPortMode_Type.__name__ = "Integer32"
_FeLAN1PortVLANPortMode_Object = MibScalar
feLAN1PortVLANPortMode = _FeLAN1PortVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 18),
    _FeLAN1PortVLANPortMode_Type()
)
feLAN1PortVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortVLANPortMode.setStatus("current")


class _FeLAN1PortBlockAllUnknown_Type(Integer32):
    """Custom type feLAN1PortBlockAllUnknown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN1PortBlockAllUnknown_Type.__name__ = "Integer32"
_FeLAN1PortBlockAllUnknown_Object = MibScalar
feLAN1PortBlockAllUnknown = _FeLAN1PortBlockAllUnknown_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 19),
    _FeLAN1PortBlockAllUnknown_Type()
)
feLAN1PortBlockAllUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortBlockAllUnknown.setStatus("current")


class _FeLAN1PortIGMPSnooping_Type(Integer32):
    """Custom type feLAN1PortIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN1PortIGMPSnooping_Type.__name__ = "Integer32"
_FeLAN1PortIGMPSnooping_Object = MibScalar
feLAN1PortIGMPSnooping = _FeLAN1PortIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 20),
    _FeLAN1PortIGMPSnooping_Type()
)
feLAN1PortIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortIGMPSnooping.setStatus("current")


class _FeLAN1PortAddUnicast_Type(OctetString):
    """Custom type feLAN1PortAddUnicast based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN1PortAddUnicast_Type.__name__ = "OctetString"
_FeLAN1PortAddUnicast_Object = MibScalar
feLAN1PortAddUnicast = _FeLAN1PortAddUnicast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 21),
    _FeLAN1PortAddUnicast_Type()
)
feLAN1PortAddUnicast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN1PortAddUnicast.setStatus("current")
_FeLAN1PortAddMulticast_Type = IpAddress
_FeLAN1PortAddMulticast_Object = MibScalar
feLAN1PortAddMulticast = _FeLAN1PortAddMulticast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 22),
    _FeLAN1PortAddMulticast_Type()
)
feLAN1PortAddMulticast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN1PortAddMulticast.setStatus("current")


class _FeLAN1PortArpMirroring_Type(Integer32):
    """Custom type feLAN1PortArpMirroring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN1PortArpMirroring_Type.__name__ = "Integer32"
_FeLAN1PortArpMirroring_Object = MibScalar
feLAN1PortArpMirroring = _FeLAN1PortArpMirroring_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 3, 23),
    _FeLAN1PortArpMirroring_Type()
)
feLAN1PortArpMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN1PortArpMirroring.setStatus("current")
_FeLAN2Port_ObjectIdentity = ObjectIdentity
feLAN2Port = _FeLAN2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4)
)


class _FeLAN2PortAutoNegotiation_Type(Integer32):
    """Custom type feLAN2PortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FeLAN2PortAutoNegotiation_Type.__name__ = "Integer32"
_FeLAN2PortAutoNegotiation_Object = MibScalar
feLAN2PortAutoNegotiation = _FeLAN2PortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 1),
    _FeLAN2PortAutoNegotiation_Type()
)
feLAN2PortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortAutoNegotiation.setStatus("current")


class _FeLAN2PortSpeedMode_Type(OctetString):
    """Custom type feLAN2PortSpeedMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FeLAN2PortSpeedMode_Type.__name__ = "OctetString"
_FeLAN2PortSpeedMode_Object = MibScalar
feLAN2PortSpeedMode = _FeLAN2PortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 2),
    _FeLAN2PortSpeedMode_Type()
)
feLAN2PortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortSpeedMode.setStatus("current")


class _FeLAN2PortLinkStatus_Type(Integer32):
    """Custom type feLAN2PortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN2PortLinkStatus_Type.__name__ = "Integer32"
_FeLAN2PortLinkStatus_Object = MibScalar
feLAN2PortLinkStatus = _FeLAN2PortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 3),
    _FeLAN2PortLinkStatus_Type()
)
feLAN2PortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feLAN2PortLinkStatus.setStatus("current")


class _FeLAN2PortFlowControl_Type(Integer32):
    """Custom type feLAN2PortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN2PortFlowControl_Type.__name__ = "Integer32"
_FeLAN2PortFlowControl_Object = MibScalar
feLAN2PortFlowControl = _FeLAN2PortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 4),
    _FeLAN2PortFlowControl_Type()
)
feLAN2PortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortFlowControl.setStatus("current")


class _FeLAN2PortIEEEQoSPriority_Type(Integer32):
    """Custom type feLAN2PortIEEEQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN2PortIEEEQoSPriority_Type.__name__ = "Integer32"
_FeLAN2PortIEEEQoSPriority_Object = MibScalar
feLAN2PortIEEEQoSPriority = _FeLAN2PortIEEEQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 5),
    _FeLAN2PortIEEEQoSPriority_Type()
)
feLAN2PortIEEEQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortIEEEQoSPriority.setStatus("current")


class _FeLAN2PortIPQoSPriority_Type(Integer32):
    """Custom type feLAN2PortIPQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN2PortIPQoSPriority_Type.__name__ = "Integer32"
_FeLAN2PortIPQoSPriority_Object = MibScalar
feLAN2PortIPQoSPriority = _FeLAN2PortIPQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 6),
    _FeLAN2PortIPQoSPriority_Type()
)
feLAN2PortIPQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortIPQoSPriority.setStatus("current")


class _FeLAN2PortFramePriorityOverwrite_Type(OctetString):
    """Custom type feLAN2PortFramePriorityOverwrite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN2PortFramePriorityOverwrite_Type.__name__ = "OctetString"
_FeLAN2PortFramePriorityOverwrite_Object = MibScalar
feLAN2PortFramePriorityOverwrite = _FeLAN2PortFramePriorityOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 7),
    _FeLAN2PortFramePriorityOverwrite_Type()
)
feLAN2PortFramePriorityOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortFramePriorityOverwrite.setStatus("current")


class _FeLAN2PortQueuePriorityOverwrite_Type(OctetString):
    """Custom type feLAN2PortQueuePriorityOverwrite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN2PortQueuePriorityOverwrite_Type.__name__ = "OctetString"
_FeLAN2PortQueuePriorityOverwrite_Object = MibScalar
feLAN2PortQueuePriorityOverwrite = _FeLAN2PortQueuePriorityOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 8),
    _FeLAN2PortQueuePriorityOverwrite_Type()
)
feLAN2PortQueuePriorityOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortQueuePriorityOverwrite.setStatus("current")


class _FeLAN2PortQueuePriority_Type(OctetString):
    """Custom type feLAN2PortQueuePriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN2PortQueuePriority_Type.__name__ = "OctetString"
_FeLAN2PortQueuePriority_Object = MibScalar
feLAN2PortQueuePriority = _FeLAN2PortQueuePriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 9),
    _FeLAN2PortQueuePriority_Type()
)
feLAN2PortQueuePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortQueuePriority.setStatus("current")


class _FeLAN2PortQoSPortMapRule_Type(Integer32):
    """Custom type feLAN2PortQoSPortMapRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN2PortQoSPortMapRule_Type.__name__ = "Integer32"
_FeLAN2PortQoSPortMapRule_Object = MibScalar
feLAN2PortQoSPortMapRule = _FeLAN2PortQoSPortMapRule_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 10),
    _FeLAN2PortQoSPortMapRule_Type()
)
feLAN2PortQoSPortMapRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortQoSPortMapRule.setStatus("current")


class _FeLAN2PortVIDNRLEnable_Type(Integer32):
    """Custom type feLAN2PortVIDNRLEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN2PortVIDNRLEnable_Type.__name__ = "Integer32"
_FeLAN2PortVIDNRLEnable_Object = MibScalar
feLAN2PortVIDNRLEnable = _FeLAN2PortVIDNRLEnable_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 11),
    _FeLAN2PortVIDNRLEnable_Type()
)
feLAN2PortVIDNRLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortVIDNRLEnable.setStatus("current")


class _FeLAN2PortMap2PIRL_Type(Integer32):
    """Custom type feLAN2PortMap2PIRL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_FeLAN2PortMap2PIRL_Type.__name__ = "Integer32"
_FeLAN2PortMap2PIRL_Object = MibScalar
feLAN2PortMap2PIRL = _FeLAN2PortMap2PIRL_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 12),
    _FeLAN2PortMap2PIRL_Type()
)
feLAN2PortMap2PIRL.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN2PortMap2PIRL.setStatus("current")


class _FeLAN2PortDeletePortMap2PIRL_Type(Integer32):
    """Custom type feLAN2PortDeletePortMap2PIRL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_FeLAN2PortDeletePortMap2PIRL_Type.__name__ = "Integer32"
_FeLAN2PortDeletePortMap2PIRL_Object = MibScalar
feLAN2PortDeletePortMap2PIRL = _FeLAN2PortDeletePortMap2PIRL_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 13),
    _FeLAN2PortDeletePortMap2PIRL_Type()
)
feLAN2PortDeletePortMap2PIRL.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN2PortDeletePortMap2PIRL.setStatus("current")
_FeLAN2PortEgressRateLimitation_Type = Integer32
_FeLAN2PortEgressRateLimitation_Object = MibScalar
feLAN2PortEgressRateLimitation = _FeLAN2PortEgressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 14),
    _FeLAN2PortEgressRateLimitation_Type()
)
feLAN2PortEgressRateLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortEgressRateLimitation.setStatus("current")


class _FeLAN2PortIngressRateLimitation_Type(OctetString):
    """Custom type feLAN2PortIngressRateLimitation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN2PortIngressRateLimitation_Type.__name__ = "OctetString"
_FeLAN2PortIngressRateLimitation_Object = MibScalar
feLAN2PortIngressRateLimitation = _FeLAN2PortIngressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 15),
    _FeLAN2PortIngressRateLimitation_Type()
)
feLAN2PortIngressRateLimitation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN2PortIngressRateLimitation.setStatus("current")
_FeLAN2PortDefaultVLAN_Type = Integer32
_FeLAN2PortDefaultVLAN_Object = MibScalar
feLAN2PortDefaultVLAN = _FeLAN2PortDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 16),
    _FeLAN2PortDefaultVLAN_Type()
)
feLAN2PortDefaultVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortDefaultVLAN.setStatus("current")


class _FeLAN2PortForceDefaultVID_Type(Integer32):
    """Custom type feLAN2PortForceDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN2PortForceDefaultVID_Type.__name__ = "Integer32"
_FeLAN2PortForceDefaultVID_Object = MibScalar
feLAN2PortForceDefaultVID = _FeLAN2PortForceDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 17),
    _FeLAN2PortForceDefaultVID_Type()
)
feLAN2PortForceDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortForceDefaultVID.setStatus("current")


class _FeLAN2PortVLANPortMode_Type(Integer32):
    """Custom type feLAN2PortVLANPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FeLAN2PortVLANPortMode_Type.__name__ = "Integer32"
_FeLAN2PortVLANPortMode_Object = MibScalar
feLAN2PortVLANPortMode = _FeLAN2PortVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 18),
    _FeLAN2PortVLANPortMode_Type()
)
feLAN2PortVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortVLANPortMode.setStatus("current")


class _FeLAN2PortBlockAllUnknown_Type(Integer32):
    """Custom type feLAN2PortBlockAllUnknown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN2PortBlockAllUnknown_Type.__name__ = "Integer32"
_FeLAN2PortBlockAllUnknown_Object = MibScalar
feLAN2PortBlockAllUnknown = _FeLAN2PortBlockAllUnknown_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 19),
    _FeLAN2PortBlockAllUnknown_Type()
)
feLAN2PortBlockAllUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortBlockAllUnknown.setStatus("current")


class _FeLAN2PortIGMPSnooping_Type(Integer32):
    """Custom type feLAN2PortIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN2PortIGMPSnooping_Type.__name__ = "Integer32"
_FeLAN2PortIGMPSnooping_Object = MibScalar
feLAN2PortIGMPSnooping = _FeLAN2PortIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 20),
    _FeLAN2PortIGMPSnooping_Type()
)
feLAN2PortIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortIGMPSnooping.setStatus("current")


class _FeLAN2PortAddUnicast_Type(OctetString):
    """Custom type feLAN2PortAddUnicast based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN2PortAddUnicast_Type.__name__ = "OctetString"
_FeLAN2PortAddUnicast_Object = MibScalar
feLAN2PortAddUnicast = _FeLAN2PortAddUnicast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 21),
    _FeLAN2PortAddUnicast_Type()
)
feLAN2PortAddUnicast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN2PortAddUnicast.setStatus("current")
_FeLAN2PortAddMulticast_Type = IpAddress
_FeLAN2PortAddMulticast_Object = MibScalar
feLAN2PortAddMulticast = _FeLAN2PortAddMulticast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 22),
    _FeLAN2PortAddMulticast_Type()
)
feLAN2PortAddMulticast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN2PortAddMulticast.setStatus("current")


class _FeLAN2PortArpMirroring_Type(Integer32):
    """Custom type feLAN2PortArpMirroring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN2PortArpMirroring_Type.__name__ = "Integer32"
_FeLAN2PortArpMirroring_Object = MibScalar
feLAN2PortArpMirroring = _FeLAN2PortArpMirroring_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 4, 23),
    _FeLAN2PortArpMirroring_Type()
)
feLAN2PortArpMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN2PortArpMirroring.setStatus("current")
_FeLAN3Port_ObjectIdentity = ObjectIdentity
feLAN3Port = _FeLAN3Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5)
)


class _FeLAN3PortAutoNegotiation_Type(Integer32):
    """Custom type feLAN3PortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FeLAN3PortAutoNegotiation_Type.__name__ = "Integer32"
_FeLAN3PortAutoNegotiation_Object = MibScalar
feLAN3PortAutoNegotiation = _FeLAN3PortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 1),
    _FeLAN3PortAutoNegotiation_Type()
)
feLAN3PortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortAutoNegotiation.setStatus("current")


class _FeLAN3PortSpeedMode_Type(OctetString):
    """Custom type feLAN3PortSpeedMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FeLAN3PortSpeedMode_Type.__name__ = "OctetString"
_FeLAN3PortSpeedMode_Object = MibScalar
feLAN3PortSpeedMode = _FeLAN3PortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 2),
    _FeLAN3PortSpeedMode_Type()
)
feLAN3PortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortSpeedMode.setStatus("current")


class _FeLAN3PortLinkStatus_Type(Integer32):
    """Custom type feLAN3PortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN3PortLinkStatus_Type.__name__ = "Integer32"
_FeLAN3PortLinkStatus_Object = MibScalar
feLAN3PortLinkStatus = _FeLAN3PortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 3),
    _FeLAN3PortLinkStatus_Type()
)
feLAN3PortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feLAN3PortLinkStatus.setStatus("current")


class _FeLAN3PortFlowControl_Type(Integer32):
    """Custom type feLAN3PortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN3PortFlowControl_Type.__name__ = "Integer32"
_FeLAN3PortFlowControl_Object = MibScalar
feLAN3PortFlowControl = _FeLAN3PortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 4),
    _FeLAN3PortFlowControl_Type()
)
feLAN3PortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortFlowControl.setStatus("current")


class _FeLAN3PortIEEEQoSPriority_Type(Integer32):
    """Custom type feLAN3PortIEEEQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN3PortIEEEQoSPriority_Type.__name__ = "Integer32"
_FeLAN3PortIEEEQoSPriority_Object = MibScalar
feLAN3PortIEEEQoSPriority = _FeLAN3PortIEEEQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 5),
    _FeLAN3PortIEEEQoSPriority_Type()
)
feLAN3PortIEEEQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortIEEEQoSPriority.setStatus("current")


class _FeLAN3PortIPQoSPriority_Type(Integer32):
    """Custom type feLAN3PortIPQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN3PortIPQoSPriority_Type.__name__ = "Integer32"
_FeLAN3PortIPQoSPriority_Object = MibScalar
feLAN3PortIPQoSPriority = _FeLAN3PortIPQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 6),
    _FeLAN3PortIPQoSPriority_Type()
)
feLAN3PortIPQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortIPQoSPriority.setStatus("current")


class _FeLAN3PortFramePriorityOverwrite_Type(OctetString):
    """Custom type feLAN3PortFramePriorityOverwrite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN3PortFramePriorityOverwrite_Type.__name__ = "OctetString"
_FeLAN3PortFramePriorityOverwrite_Object = MibScalar
feLAN3PortFramePriorityOverwrite = _FeLAN3PortFramePriorityOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 7),
    _FeLAN3PortFramePriorityOverwrite_Type()
)
feLAN3PortFramePriorityOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortFramePriorityOverwrite.setStatus("current")


class _FeLAN3PortQueuePriorityOverwrite_Type(OctetString):
    """Custom type feLAN3PortQueuePriorityOverwrite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN3PortQueuePriorityOverwrite_Type.__name__ = "OctetString"
_FeLAN3PortQueuePriorityOverwrite_Object = MibScalar
feLAN3PortQueuePriorityOverwrite = _FeLAN3PortQueuePriorityOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 8),
    _FeLAN3PortQueuePriorityOverwrite_Type()
)
feLAN3PortQueuePriorityOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortQueuePriorityOverwrite.setStatus("current")


class _FeLAN3PortQueuePriority_Type(OctetString):
    """Custom type feLAN3PortQueuePriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN3PortQueuePriority_Type.__name__ = "OctetString"
_FeLAN3PortQueuePriority_Object = MibScalar
feLAN3PortQueuePriority = _FeLAN3PortQueuePriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 9),
    _FeLAN3PortQueuePriority_Type()
)
feLAN3PortQueuePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortQueuePriority.setStatus("current")


class _FeLAN3PortQoSPortMapRule_Type(Integer32):
    """Custom type feLAN3PortQoSPortMapRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN3PortQoSPortMapRule_Type.__name__ = "Integer32"
_FeLAN3PortQoSPortMapRule_Object = MibScalar
feLAN3PortQoSPortMapRule = _FeLAN3PortQoSPortMapRule_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 10),
    _FeLAN3PortQoSPortMapRule_Type()
)
feLAN3PortQoSPortMapRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortQoSPortMapRule.setStatus("current")


class _FeLAN3PortVIDNRLEnable_Type(Integer32):
    """Custom type feLAN3PortVIDNRLEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN3PortVIDNRLEnable_Type.__name__ = "Integer32"
_FeLAN3PortVIDNRLEnable_Object = MibScalar
feLAN3PortVIDNRLEnable = _FeLAN3PortVIDNRLEnable_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 11),
    _FeLAN3PortVIDNRLEnable_Type()
)
feLAN3PortVIDNRLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortVIDNRLEnable.setStatus("current")


class _FeLAN3PortMap2PIRL_Type(Integer32):
    """Custom type feLAN3PortMap2PIRL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_FeLAN3PortMap2PIRL_Type.__name__ = "Integer32"
_FeLAN3PortMap2PIRL_Object = MibScalar
feLAN3PortMap2PIRL = _FeLAN3PortMap2PIRL_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 12),
    _FeLAN3PortMap2PIRL_Type()
)
feLAN3PortMap2PIRL.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN3PortMap2PIRL.setStatus("current")


class _FeLAN3PortDeletePortMap2PIRL_Type(Integer32):
    """Custom type feLAN3PortDeletePortMap2PIRL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_FeLAN3PortDeletePortMap2PIRL_Type.__name__ = "Integer32"
_FeLAN3PortDeletePortMap2PIRL_Object = MibScalar
feLAN3PortDeletePortMap2PIRL = _FeLAN3PortDeletePortMap2PIRL_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 13),
    _FeLAN3PortDeletePortMap2PIRL_Type()
)
feLAN3PortDeletePortMap2PIRL.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN3PortDeletePortMap2PIRL.setStatus("current")
_FeLAN3PortEgressRateLimitation_Type = Integer32
_FeLAN3PortEgressRateLimitation_Object = MibScalar
feLAN3PortEgressRateLimitation = _FeLAN3PortEgressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 14),
    _FeLAN3PortEgressRateLimitation_Type()
)
feLAN3PortEgressRateLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortEgressRateLimitation.setStatus("current")


class _FeLAN3PortIngressRateLimitation_Type(OctetString):
    """Custom type feLAN3PortIngressRateLimitation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN3PortIngressRateLimitation_Type.__name__ = "OctetString"
_FeLAN3PortIngressRateLimitation_Object = MibScalar
feLAN3PortIngressRateLimitation = _FeLAN3PortIngressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 15),
    _FeLAN3PortIngressRateLimitation_Type()
)
feLAN3PortIngressRateLimitation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN3PortIngressRateLimitation.setStatus("current")
_FeLAN3PortDefaultVLAN_Type = Integer32
_FeLAN3PortDefaultVLAN_Object = MibScalar
feLAN3PortDefaultVLAN = _FeLAN3PortDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 16),
    _FeLAN3PortDefaultVLAN_Type()
)
feLAN3PortDefaultVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortDefaultVLAN.setStatus("current")


class _FeLAN3PortForceDefaultVID_Type(Integer32):
    """Custom type feLAN3PortForceDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN3PortForceDefaultVID_Type.__name__ = "Integer32"
_FeLAN3PortForceDefaultVID_Object = MibScalar
feLAN3PortForceDefaultVID = _FeLAN3PortForceDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 17),
    _FeLAN3PortForceDefaultVID_Type()
)
feLAN3PortForceDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortForceDefaultVID.setStatus("current")


class _FeLAN3PortVLANPortMode_Type(Integer32):
    """Custom type feLAN3PortVLANPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FeLAN3PortVLANPortMode_Type.__name__ = "Integer32"
_FeLAN3PortVLANPortMode_Object = MibScalar
feLAN3PortVLANPortMode = _FeLAN3PortVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 18),
    _FeLAN3PortVLANPortMode_Type()
)
feLAN3PortVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortVLANPortMode.setStatus("current")


class _FeLAN3PortBlockAllUnknown_Type(Integer32):
    """Custom type feLAN3PortBlockAllUnknown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN3PortBlockAllUnknown_Type.__name__ = "Integer32"
_FeLAN3PortBlockAllUnknown_Object = MibScalar
feLAN3PortBlockAllUnknown = _FeLAN3PortBlockAllUnknown_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 19),
    _FeLAN3PortBlockAllUnknown_Type()
)
feLAN3PortBlockAllUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortBlockAllUnknown.setStatus("current")


class _FeLAN3PortIGMPSnooping_Type(Integer32):
    """Custom type feLAN3PortIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN3PortIGMPSnooping_Type.__name__ = "Integer32"
_FeLAN3PortIGMPSnooping_Object = MibScalar
feLAN3PortIGMPSnooping = _FeLAN3PortIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 20),
    _FeLAN3PortIGMPSnooping_Type()
)
feLAN3PortIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortIGMPSnooping.setStatus("current")


class _FeLAN3PortAddUnicast_Type(OctetString):
    """Custom type feLAN3PortAddUnicast based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN3PortAddUnicast_Type.__name__ = "OctetString"
_FeLAN3PortAddUnicast_Object = MibScalar
feLAN3PortAddUnicast = _FeLAN3PortAddUnicast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 21),
    _FeLAN3PortAddUnicast_Type()
)
feLAN3PortAddUnicast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN3PortAddUnicast.setStatus("current")
_FeLAN3PortAddMulticast_Type = IpAddress
_FeLAN3PortAddMulticast_Object = MibScalar
feLAN3PortAddMulticast = _FeLAN3PortAddMulticast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 22),
    _FeLAN3PortAddMulticast_Type()
)
feLAN3PortAddMulticast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN3PortAddMulticast.setStatus("current")


class _FeLAN3PortArpMirroring_Type(Integer32):
    """Custom type feLAN3PortArpMirroring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN3PortArpMirroring_Type.__name__ = "Integer32"
_FeLAN3PortArpMirroring_Object = MibScalar
feLAN3PortArpMirroring = _FeLAN3PortArpMirroring_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 5, 23),
    _FeLAN3PortArpMirroring_Type()
)
feLAN3PortArpMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN3PortArpMirroring.setStatus("current")
_FeLAN4Port_ObjectIdentity = ObjectIdentity
feLAN4Port = _FeLAN4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6)
)


class _FeLAN4PortAutoNegotiation_Type(Integer32):
    """Custom type feLAN4PortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FeLAN4PortAutoNegotiation_Type.__name__ = "Integer32"
_FeLAN4PortAutoNegotiation_Object = MibScalar
feLAN4PortAutoNegotiation = _FeLAN4PortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 1),
    _FeLAN4PortAutoNegotiation_Type()
)
feLAN4PortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortAutoNegotiation.setStatus("current")


class _FeLAN4PortSpeedMode_Type(OctetString):
    """Custom type feLAN4PortSpeedMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FeLAN4PortSpeedMode_Type.__name__ = "OctetString"
_FeLAN4PortSpeedMode_Object = MibScalar
feLAN4PortSpeedMode = _FeLAN4PortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 2),
    _FeLAN4PortSpeedMode_Type()
)
feLAN4PortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortSpeedMode.setStatus("current")


class _FeLAN4PortLinkStatus_Type(Integer32):
    """Custom type feLAN4PortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN4PortLinkStatus_Type.__name__ = "Integer32"
_FeLAN4PortLinkStatus_Object = MibScalar
feLAN4PortLinkStatus = _FeLAN4PortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 3),
    _FeLAN4PortLinkStatus_Type()
)
feLAN4PortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feLAN4PortLinkStatus.setStatus("current")


class _FeLAN4PortFlowControl_Type(Integer32):
    """Custom type feLAN4PortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN4PortFlowControl_Type.__name__ = "Integer32"
_FeLAN4PortFlowControl_Object = MibScalar
feLAN4PortFlowControl = _FeLAN4PortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 4),
    _FeLAN4PortFlowControl_Type()
)
feLAN4PortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortFlowControl.setStatus("current")


class _FeLAN4PortIEEEQoSPriority_Type(Integer32):
    """Custom type feLAN4PortIEEEQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN4PortIEEEQoSPriority_Type.__name__ = "Integer32"
_FeLAN4PortIEEEQoSPriority_Object = MibScalar
feLAN4PortIEEEQoSPriority = _FeLAN4PortIEEEQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 5),
    _FeLAN4PortIEEEQoSPriority_Type()
)
feLAN4PortIEEEQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortIEEEQoSPriority.setStatus("current")


class _FeLAN4PortIPQoSPriority_Type(Integer32):
    """Custom type feLAN4PortIPQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN4PortIPQoSPriority_Type.__name__ = "Integer32"
_FeLAN4PortIPQoSPriority_Object = MibScalar
feLAN4PortIPQoSPriority = _FeLAN4PortIPQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 6),
    _FeLAN4PortIPQoSPriority_Type()
)
feLAN4PortIPQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortIPQoSPriority.setStatus("current")


class _FeLAN4PortFramePriorityOverwrite_Type(OctetString):
    """Custom type feLAN4PortFramePriorityOverwrite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN4PortFramePriorityOverwrite_Type.__name__ = "OctetString"
_FeLAN4PortFramePriorityOverwrite_Object = MibScalar
feLAN4PortFramePriorityOverwrite = _FeLAN4PortFramePriorityOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 7),
    _FeLAN4PortFramePriorityOverwrite_Type()
)
feLAN4PortFramePriorityOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortFramePriorityOverwrite.setStatus("current")


class _FeLAN4PortQueuePriorityOverwrite_Type(OctetString):
    """Custom type feLAN4PortQueuePriorityOverwrite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN4PortQueuePriorityOverwrite_Type.__name__ = "OctetString"
_FeLAN4PortQueuePriorityOverwrite_Object = MibScalar
feLAN4PortQueuePriorityOverwrite = _FeLAN4PortQueuePriorityOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 8),
    _FeLAN4PortQueuePriorityOverwrite_Type()
)
feLAN4PortQueuePriorityOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortQueuePriorityOverwrite.setStatus("current")


class _FeLAN4PortQueuePriority_Type(OctetString):
    """Custom type feLAN4PortQueuePriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN4PortQueuePriority_Type.__name__ = "OctetString"
_FeLAN4PortQueuePriority_Object = MibScalar
feLAN4PortQueuePriority = _FeLAN4PortQueuePriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 9),
    _FeLAN4PortQueuePriority_Type()
)
feLAN4PortQueuePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortQueuePriority.setStatus("current")


class _FeLAN4PortQoSPortMapRule_Type(Integer32):
    """Custom type feLAN4PortQoSPortMapRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN4PortQoSPortMapRule_Type.__name__ = "Integer32"
_FeLAN4PortQoSPortMapRule_Object = MibScalar
feLAN4PortQoSPortMapRule = _FeLAN4PortQoSPortMapRule_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 10),
    _FeLAN4PortQoSPortMapRule_Type()
)
feLAN4PortQoSPortMapRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortQoSPortMapRule.setStatus("current")


class _FeLAN4PortVIDNRLEnable_Type(Integer32):
    """Custom type feLAN4PortVIDNRLEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN4PortVIDNRLEnable_Type.__name__ = "Integer32"
_FeLAN4PortVIDNRLEnable_Object = MibScalar
feLAN4PortVIDNRLEnable = _FeLAN4PortVIDNRLEnable_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 11),
    _FeLAN4PortVIDNRLEnable_Type()
)
feLAN4PortVIDNRLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortVIDNRLEnable.setStatus("current")


class _FeLAN4PortMap2PIRL_Type(Integer32):
    """Custom type feLAN4PortMap2PIRL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_FeLAN4PortMap2PIRL_Type.__name__ = "Integer32"
_FeLAN4PortMap2PIRL_Object = MibScalar
feLAN4PortMap2PIRL = _FeLAN4PortMap2PIRL_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 12),
    _FeLAN4PortMap2PIRL_Type()
)
feLAN4PortMap2PIRL.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN4PortMap2PIRL.setStatus("current")


class _FeLAN4PortDeletePortMap2PIRL_Type(Integer32):
    """Custom type feLAN4PortDeletePortMap2PIRL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_FeLAN4PortDeletePortMap2PIRL_Type.__name__ = "Integer32"
_FeLAN4PortDeletePortMap2PIRL_Object = MibScalar
feLAN4PortDeletePortMap2PIRL = _FeLAN4PortDeletePortMap2PIRL_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 13),
    _FeLAN4PortDeletePortMap2PIRL_Type()
)
feLAN4PortDeletePortMap2PIRL.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN4PortDeletePortMap2PIRL.setStatus("current")
_FeLAN4PortEgressRateLimitation_Type = Integer32
_FeLAN4PortEgressRateLimitation_Object = MibScalar
feLAN4PortEgressRateLimitation = _FeLAN4PortEgressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 14),
    _FeLAN4PortEgressRateLimitation_Type()
)
feLAN4PortEgressRateLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortEgressRateLimitation.setStatus("current")


class _FeLAN4PortIngressRateLimitation_Type(OctetString):
    """Custom type feLAN4PortIngressRateLimitation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN4PortIngressRateLimitation_Type.__name__ = "OctetString"
_FeLAN4PortIngressRateLimitation_Object = MibScalar
feLAN4PortIngressRateLimitation = _FeLAN4PortIngressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 15),
    _FeLAN4PortIngressRateLimitation_Type()
)
feLAN4PortIngressRateLimitation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN4PortIngressRateLimitation.setStatus("current")
_FeLAN4PortDefaultVLAN_Type = Integer32
_FeLAN4PortDefaultVLAN_Object = MibScalar
feLAN4PortDefaultVLAN = _FeLAN4PortDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 16),
    _FeLAN4PortDefaultVLAN_Type()
)
feLAN4PortDefaultVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortDefaultVLAN.setStatus("current")


class _FeLAN4PortForceDefaultVID_Type(Integer32):
    """Custom type feLAN4PortForceDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN4PortForceDefaultVID_Type.__name__ = "Integer32"
_FeLAN4PortForceDefaultVID_Object = MibScalar
feLAN4PortForceDefaultVID = _FeLAN4PortForceDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 17),
    _FeLAN4PortForceDefaultVID_Type()
)
feLAN4PortForceDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortForceDefaultVID.setStatus("current")


class _FeLAN4PortVLANPortMode_Type(Integer32):
    """Custom type feLAN4PortVLANPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FeLAN4PortVLANPortMode_Type.__name__ = "Integer32"
_FeLAN4PortVLANPortMode_Object = MibScalar
feLAN4PortVLANPortMode = _FeLAN4PortVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 18),
    _FeLAN4PortVLANPortMode_Type()
)
feLAN4PortVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortVLANPortMode.setStatus("current")


class _FeLAN4PortBlockAllUnknown_Type(Integer32):
    """Custom type feLAN4PortBlockAllUnknown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN4PortBlockAllUnknown_Type.__name__ = "Integer32"
_FeLAN4PortBlockAllUnknown_Object = MibScalar
feLAN4PortBlockAllUnknown = _FeLAN4PortBlockAllUnknown_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 19),
    _FeLAN4PortBlockAllUnknown_Type()
)
feLAN4PortBlockAllUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortBlockAllUnknown.setStatus("current")


class _FeLAN4PortIGMPSnooping_Type(Integer32):
    """Custom type feLAN4PortIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN4PortIGMPSnooping_Type.__name__ = "Integer32"
_FeLAN4PortIGMPSnooping_Object = MibScalar
feLAN4PortIGMPSnooping = _FeLAN4PortIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 20),
    _FeLAN4PortIGMPSnooping_Type()
)
feLAN4PortIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortIGMPSnooping.setStatus("current")


class _FeLAN4PortAddUnicast_Type(OctetString):
    """Custom type feLAN4PortAddUnicast based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FeLAN4PortAddUnicast_Type.__name__ = "OctetString"
_FeLAN4PortAddUnicast_Object = MibScalar
feLAN4PortAddUnicast = _FeLAN4PortAddUnicast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 21),
    _FeLAN4PortAddUnicast_Type()
)
feLAN4PortAddUnicast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN4PortAddUnicast.setStatus("current")
_FeLAN4PortAddMulticast_Type = IpAddress
_FeLAN4PortAddMulticast_Object = MibScalar
feLAN4PortAddMulticast = _FeLAN4PortAddMulticast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 22),
    _FeLAN4PortAddMulticast_Type()
)
feLAN4PortAddMulticast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    feLAN4PortAddMulticast.setStatus("current")


class _FeLAN4PortArpMirroring_Type(Integer32):
    """Custom type feLAN4PortArpMirroring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FeLAN4PortArpMirroring_Type.__name__ = "Integer32"
_FeLAN4PortArpMirroring_Object = MibScalar
feLAN4PortArpMirroring = _FeLAN4PortArpMirroring_Object(
    (1, 3, 6, 1, 4, 1, 27304, 12, 2, 6, 23),
    _FeLAN4PortArpMirroring_Type()
)
feLAN4PortArpMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feLAN4PortArpMirroring.setStatus("current")

# Managed Objects groups

feModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27304, 12, 4)
)
feModuleGroup.setObjects(
      *(("DKT-FE-MIB", "feSwitchEngine"),
        ("DKT-FE-MIB", "feATU"),
        ("DKT-FE-MIB", "feUnicastDelete"),
        ("DKT-FE-MIB", "feMulticastDelete"),
        ("DKT-FE-MIB", "feIGMPSnooping"),
        ("DKT-FE-MIB", "feVTU"),
        ("DKT-FE-MIB", "feVLANCreate"),
        ("DKT-FE-MIB", "feVLANDelete"),
        ("DKT-FE-MIB", "feClearVTU"),
        ("DKT-FE-MIB", "feDumpPIRLBuckets"),
        ("DKT-FE-MIB", "feDisablePIRLBucket"),
        ("DKT-FE-MIB", "feVLANProviderMode"),
        ("DKT-FE-MIB", "fePorts"),
        ("DKT-FE-MIB", "feCPUPort"),
        ("DKT-FE-MIB", "feCPUPortAutoNegotiation"),
        ("DKT-FE-MIB", "feCPUPortSpeedMode"),
        ("DKT-FE-MIB", "feCPUPortLinkStatus"),
        ("DKT-FE-MIB", "feCPUPortFlowControl"),
        ("DKT-FE-MIB", "feCPUPortIEEEQoSPriority"),
        ("DKT-FE-MIB", "feCPUPortIPQoSPriority"),
        ("DKT-FE-MIB", "feCPUPortFramePriorityOverwrite"),
        ("DKT-FE-MIB", "feCPUPortQueuePriorityOverwrite"),
        ("DKT-FE-MIB", "feCPUPortQueuePriority"),
        ("DKT-FE-MIB", "feCPUPortQoSPortMapRule"),
        ("DKT-FE-MIB", "feCPUPortVIDNRLEnable"),
        ("DKT-FE-MIB", "feCPUPortMap2PIRL"),
        ("DKT-FE-MIB", "feCPUPortDeletePortMap2PIRL"),
        ("DKT-FE-MIB", "feCPUPortEgressRateLimitation"),
        ("DKT-FE-MIB", "feCPUPortIngressRateLimitation"),
        ("DKT-FE-MIB", "feCPUPortDefaultVLAN"),
        ("DKT-FE-MIB", "feCPUPortForceDefaultVID"),
        ("DKT-FE-MIB", "feCPUPortVLANPortMode"),
        ("DKT-FE-MIB", "feCPUPortBlockAllUnknown"),
        ("DKT-FE-MIB", "feCPUPortIGMPSnooping"),
        ("DKT-FE-MIB", "feCPUPortAddUnicast"),
        ("DKT-FE-MIB", "feCPUPortAddMulticast"),
        ("DKT-FE-MIB", "feWANPort"),
        ("DKT-FE-MIB", "feWANPortAutoNegotiation"),
        ("DKT-FE-MIB", "feWANPortSpeedMode"),
        ("DKT-FE-MIB", "feWANPortLinkStatus"),
        ("DKT-FE-MIB", "feWANPortFlowControl"),
        ("DKT-FE-MIB", "feWANPortIEEEQoSPriority"),
        ("DKT-FE-MIB", "feWANPortIPQoSPriority"),
        ("DKT-FE-MIB", "feWANPortFramePriorityOverwrite"),
        ("DKT-FE-MIB", "feWANPortQueuePriorityOverwrite"),
        ("DKT-FE-MIB", "feWANPortQueuePriority"),
        ("DKT-FE-MIB", "feWANPortQoSPortMapRule"),
        ("DKT-FE-MIB", "feWANPortVIDNRLEnable"),
        ("DKT-FE-MIB", "feWANPortMap2PIRL"),
        ("DKT-FE-MIB", "feWANPortDeletePortMap2PIRL"),
        ("DKT-FE-MIB", "feWANPortEgressRateLimitation"),
        ("DKT-FE-MIB", "feWANPortIngressRateLimitation"),
        ("DKT-FE-MIB", "feWANPortDefaultVLAN"),
        ("DKT-FE-MIB", "feWANPortForceDefaultVID"),
        ("DKT-FE-MIB", "feWANPortVLANPortMode"),
        ("DKT-FE-MIB", "feWANPortBlockAllUnknown"),
        ("DKT-FE-MIB", "feWANPortIGMPSnooping"),
        ("DKT-FE-MIB", "feWANPortAddUnicast"),
        ("DKT-FE-MIB", "feWANPortAddMulticast"),
        ("DKT-FE-MIB", "feWANPortArpMirroring"),
        ("DKT-FE-MIB", "feLAN1Port"),
        ("DKT-FE-MIB", "feLAN1PortAutoNegotiation"),
        ("DKT-FE-MIB", "feLAN1PortSpeedMode"),
        ("DKT-FE-MIB", "feLAN1PortLinkStatus"),
        ("DKT-FE-MIB", "feLAN1PortFlowControl"),
        ("DKT-FE-MIB", "feLAN1PortIEEEQoSPriority"),
        ("DKT-FE-MIB", "feLAN1PortIPQoSPriority"),
        ("DKT-FE-MIB", "feLAN1PortFramePriorityOverwrite"),
        ("DKT-FE-MIB", "feLAN1PortQueuePriorityOverwrite"),
        ("DKT-FE-MIB", "feLAN1PortQueuePriority"),
        ("DKT-FE-MIB", "feLAN1PortQoSPortMapRule"),
        ("DKT-FE-MIB", "feLAN1PortVIDNRLEnable"),
        ("DKT-FE-MIB", "feLAN1PortMap2PIRL"),
        ("DKT-FE-MIB", "feLAN1PortDeletePortMap2PIRL"),
        ("DKT-FE-MIB", "feLAN1PortEgressRateLimitation"),
        ("DKT-FE-MIB", "feLAN1PortIngressRateLimitation"),
        ("DKT-FE-MIB", "feLAN1PortDefaultVLAN"),
        ("DKT-FE-MIB", "feLAN1PortForceDefaultVID"),
        ("DKT-FE-MIB", "feLAN1PortVLANPortMode"),
        ("DKT-FE-MIB", "feLAN1PortBlockAllUnknown"),
        ("DKT-FE-MIB", "feLAN1PortIGMPSnooping"),
        ("DKT-FE-MIB", "feLAN1PortAddUnicast"),
        ("DKT-FE-MIB", "feLAN1PortAddMulticast"),
        ("DKT-FE-MIB", "feLAN1PortArpMirroring"),
        ("DKT-FE-MIB", "feLAN2Port"),
        ("DKT-FE-MIB", "feLAN2PortAutoNegotiation"),
        ("DKT-FE-MIB", "feLAN2PortSpeedMode"),
        ("DKT-FE-MIB", "feLAN2PortLinkStatus"),
        ("DKT-FE-MIB", "feLAN2PortFlowControl"),
        ("DKT-FE-MIB", "feLAN2PortIEEEQoSPriority"),
        ("DKT-FE-MIB", "feLAN2PortIPQoSPriority"),
        ("DKT-FE-MIB", "feLAN2PortFramePriorityOverwrite"),
        ("DKT-FE-MIB", "feLAN2PortQueuePriorityOverwrite"),
        ("DKT-FE-MIB", "feLAN2PortQueuePriority"),
        ("DKT-FE-MIB", "feLAN2PortQoSPortMapRule"),
        ("DKT-FE-MIB", "feLAN2PortVIDNRLEnable"),
        ("DKT-FE-MIB", "feLAN2PortMap2PIRL"),
        ("DKT-FE-MIB", "feLAN2PortDeletePortMap2PIRL"),
        ("DKT-FE-MIB", "feLAN2PortEgressRateLimitation"),
        ("DKT-FE-MIB", "feLAN2PortIngressRateLimitation"),
        ("DKT-FE-MIB", "feLAN2PortDefaultVLAN"),
        ("DKT-FE-MIB", "feLAN2PortForceDefaultVID"),
        ("DKT-FE-MIB", "feLAN2PortVLANPortMode"),
        ("DKT-FE-MIB", "feLAN2PortBlockAllUnknown"),
        ("DKT-FE-MIB", "feLAN2PortIGMPSnooping"),
        ("DKT-FE-MIB", "feLAN2PortAddUnicast"),
        ("DKT-FE-MIB", "feLAN2PortAddMulticast"),
        ("DKT-FE-MIB", "feLAN2PortArpMirroring"),
        ("DKT-FE-MIB", "feLAN3Port"),
        ("DKT-FE-MIB", "feLAN3PortAutoNegotiation"),
        ("DKT-FE-MIB", "feLAN3PortSpeedMode"),
        ("DKT-FE-MIB", "feLAN3PortLinkStatus"),
        ("DKT-FE-MIB", "feLAN3PortFlowControl"),
        ("DKT-FE-MIB", "feLAN3PortIEEEQoSPriority"),
        ("DKT-FE-MIB", "feLAN3PortIPQoSPriority"),
        ("DKT-FE-MIB", "feLAN3PortFramePriorityOverwrite"),
        ("DKT-FE-MIB", "feLAN3PortQueuePriorityOverwrite"),
        ("DKT-FE-MIB", "feLAN3PortQueuePriority"),
        ("DKT-FE-MIB", "feLAN3PortQoSPortMapRule"),
        ("DKT-FE-MIB", "feLAN3PortVIDNRLEnable"),
        ("DKT-FE-MIB", "feLAN3PortMap2PIRL"),
        ("DKT-FE-MIB", "feLAN3PortDeletePortMap2PIRL"),
        ("DKT-FE-MIB", "feLAN3PortEgressRateLimitation"),
        ("DKT-FE-MIB", "feLAN3PortIngressRateLimitation"),
        ("DKT-FE-MIB", "feLAN3PortDefaultVLAN"),
        ("DKT-FE-MIB", "feLAN3PortForceDefaultVID"),
        ("DKT-FE-MIB", "feLAN3PortVLANPortMode"),
        ("DKT-FE-MIB", "feLAN3PortBlockAllUnknown"),
        ("DKT-FE-MIB", "feLAN3PortIGMPSnooping"),
        ("DKT-FE-MIB", "feLAN3PortAddUnicast"),
        ("DKT-FE-MIB", "feLAN3PortAddMulticast"),
        ("DKT-FE-MIB", "feLAN3PortArpMirroring"),
        ("DKT-FE-MIB", "feLAN4Port"),
        ("DKT-FE-MIB", "feLAN4PortAutoNegotiation"),
        ("DKT-FE-MIB", "feLAN4PortSpeedMode"),
        ("DKT-FE-MIB", "feLAN4PortLinkStatus"),
        ("DKT-FE-MIB", "feLAN4PortFlowControl"),
        ("DKT-FE-MIB", "feLAN4PortIEEEQoSPriority"),
        ("DKT-FE-MIB", "feLAN4PortIPQoSPriority"),
        ("DKT-FE-MIB", "feLAN4PortFramePriorityOverwrite"),
        ("DKT-FE-MIB", "feLAN4PortQueuePriorityOverwrite"),
        ("DKT-FE-MIB", "feLAN4PortQueuePriority"),
        ("DKT-FE-MIB", "feLAN4PortQoSPortMapRule"),
        ("DKT-FE-MIB", "feLAN4PortVIDNRLEnable"),
        ("DKT-FE-MIB", "feLAN4PortMap2PIRL"),
        ("DKT-FE-MIB", "feLAN4PortDeletePortMap2PIRL"),
        ("DKT-FE-MIB", "feLAN4PortEgressRateLimitation"),
        ("DKT-FE-MIB", "feLAN4PortIngressRateLimitation"),
        ("DKT-FE-MIB", "feLAN4PortDefaultVLAN"),
        ("DKT-FE-MIB", "feLAN4PortForceDefaultVID"),
        ("DKT-FE-MIB", "feLAN4PortVLANPortMode"),
        ("DKT-FE-MIB", "feLAN4PortBlockAllUnknown"),
        ("DKT-FE-MIB", "feLAN4PortIGMPSnooping"),
        ("DKT-FE-MIB", "feLAN4PortAddUnicast"),
        ("DKT-FE-MIB", "feLAN4PortAddMulticast"),
        ("DKT-FE-MIB", "feLAN4PortArpMirroring"))
)
if mibBuilder.loadTexts:
    feModuleGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DKT-FE-MIB",
    **{"feMIB": feMIB,
       "feSwitchEngine": feSwitchEngine,
       "feATU": feATU,
       "feUnicastDelete": feUnicastDelete,
       "feMulticastDelete": feMulticastDelete,
       "feIGMPSnooping": feIGMPSnooping,
       "feVTU": feVTU,
       "feVLANCreate": feVLANCreate,
       "feVLANDelete": feVLANDelete,
       "feClearVTU": feClearVTU,
       "feDumpPIRLBuckets": feDumpPIRLBuckets,
       "feDisablePIRLBucket": feDisablePIRLBucket,
       "feVLANProviderMode": feVLANProviderMode,
       "fePorts": fePorts,
       "feCPUPort": feCPUPort,
       "feCPUPortAutoNegotiation": feCPUPortAutoNegotiation,
       "feCPUPortSpeedMode": feCPUPortSpeedMode,
       "feCPUPortLinkStatus": feCPUPortLinkStatus,
       "feCPUPortFlowControl": feCPUPortFlowControl,
       "feCPUPortIEEEQoSPriority": feCPUPortIEEEQoSPriority,
       "feCPUPortIPQoSPriority": feCPUPortIPQoSPriority,
       "feCPUPortFramePriorityOverwrite": feCPUPortFramePriorityOverwrite,
       "feCPUPortQueuePriorityOverwrite": feCPUPortQueuePriorityOverwrite,
       "feCPUPortQueuePriority": feCPUPortQueuePriority,
       "feCPUPortQoSPortMapRule": feCPUPortQoSPortMapRule,
       "feCPUPortVIDNRLEnable": feCPUPortVIDNRLEnable,
       "feCPUPortMap2PIRL": feCPUPortMap2PIRL,
       "feCPUPortDeletePortMap2PIRL": feCPUPortDeletePortMap2PIRL,
       "feCPUPortEgressRateLimitation": feCPUPortEgressRateLimitation,
       "feCPUPortIngressRateLimitation": feCPUPortIngressRateLimitation,
       "feCPUPortDefaultVLAN": feCPUPortDefaultVLAN,
       "feCPUPortForceDefaultVID": feCPUPortForceDefaultVID,
       "feCPUPortVLANPortMode": feCPUPortVLANPortMode,
       "feCPUPortBlockAllUnknown": feCPUPortBlockAllUnknown,
       "feCPUPortIGMPSnooping": feCPUPortIGMPSnooping,
       "feCPUPortAddUnicast": feCPUPortAddUnicast,
       "feCPUPortAddMulticast": feCPUPortAddMulticast,
       "feWANPort": feWANPort,
       "feWANPortAutoNegotiation": feWANPortAutoNegotiation,
       "feWANPortSpeedMode": feWANPortSpeedMode,
       "feWANPortLinkStatus": feWANPortLinkStatus,
       "feWANPortFlowControl": feWANPortFlowControl,
       "feWANPortIEEEQoSPriority": feWANPortIEEEQoSPriority,
       "feWANPortIPQoSPriority": feWANPortIPQoSPriority,
       "feWANPortFramePriorityOverwrite": feWANPortFramePriorityOverwrite,
       "feWANPortQueuePriorityOverwrite": feWANPortQueuePriorityOverwrite,
       "feWANPortQueuePriority": feWANPortQueuePriority,
       "feWANPortQoSPortMapRule": feWANPortQoSPortMapRule,
       "feWANPortVIDNRLEnable": feWANPortVIDNRLEnable,
       "feWANPortMap2PIRL": feWANPortMap2PIRL,
       "feWANPortDeletePortMap2PIRL": feWANPortDeletePortMap2PIRL,
       "feWANPortEgressRateLimitation": feWANPortEgressRateLimitation,
       "feWANPortIngressRateLimitation": feWANPortIngressRateLimitation,
       "feWANPortDefaultVLAN": feWANPortDefaultVLAN,
       "feWANPortForceDefaultVID": feWANPortForceDefaultVID,
       "feWANPortVLANPortMode": feWANPortVLANPortMode,
       "feWANPortBlockAllUnknown": feWANPortBlockAllUnknown,
       "feWANPortIGMPSnooping": feWANPortIGMPSnooping,
       "feWANPortAddUnicast": feWANPortAddUnicast,
       "feWANPortAddMulticast": feWANPortAddMulticast,
       "feWANPortArpMirroring": feWANPortArpMirroring,
       "feLAN1Port": feLAN1Port,
       "feLAN1PortAutoNegotiation": feLAN1PortAutoNegotiation,
       "feLAN1PortSpeedMode": feLAN1PortSpeedMode,
       "feLAN1PortLinkStatus": feLAN1PortLinkStatus,
       "feLAN1PortFlowControl": feLAN1PortFlowControl,
       "feLAN1PortIEEEQoSPriority": feLAN1PortIEEEQoSPriority,
       "feLAN1PortIPQoSPriority": feLAN1PortIPQoSPriority,
       "feLAN1PortFramePriorityOverwrite": feLAN1PortFramePriorityOverwrite,
       "feLAN1PortQueuePriorityOverwrite": feLAN1PortQueuePriorityOverwrite,
       "feLAN1PortQueuePriority": feLAN1PortQueuePriority,
       "feLAN1PortQoSPortMapRule": feLAN1PortQoSPortMapRule,
       "feLAN1PortVIDNRLEnable": feLAN1PortVIDNRLEnable,
       "feLAN1PortMap2PIRL": feLAN1PortMap2PIRL,
       "feLAN1PortDeletePortMap2PIRL": feLAN1PortDeletePortMap2PIRL,
       "feLAN1PortEgressRateLimitation": feLAN1PortEgressRateLimitation,
       "feLAN1PortIngressRateLimitation": feLAN1PortIngressRateLimitation,
       "feLAN1PortDefaultVLAN": feLAN1PortDefaultVLAN,
       "feLAN1PortForceDefaultVID": feLAN1PortForceDefaultVID,
       "feLAN1PortVLANPortMode": feLAN1PortVLANPortMode,
       "feLAN1PortBlockAllUnknown": feLAN1PortBlockAllUnknown,
       "feLAN1PortIGMPSnooping": feLAN1PortIGMPSnooping,
       "feLAN1PortAddUnicast": feLAN1PortAddUnicast,
       "feLAN1PortAddMulticast": feLAN1PortAddMulticast,
       "feLAN1PortArpMirroring": feLAN1PortArpMirroring,
       "feLAN2Port": feLAN2Port,
       "feLAN2PortAutoNegotiation": feLAN2PortAutoNegotiation,
       "feLAN2PortSpeedMode": feLAN2PortSpeedMode,
       "feLAN2PortLinkStatus": feLAN2PortLinkStatus,
       "feLAN2PortFlowControl": feLAN2PortFlowControl,
       "feLAN2PortIEEEQoSPriority": feLAN2PortIEEEQoSPriority,
       "feLAN2PortIPQoSPriority": feLAN2PortIPQoSPriority,
       "feLAN2PortFramePriorityOverwrite": feLAN2PortFramePriorityOverwrite,
       "feLAN2PortQueuePriorityOverwrite": feLAN2PortQueuePriorityOverwrite,
       "feLAN2PortQueuePriority": feLAN2PortQueuePriority,
       "feLAN2PortQoSPortMapRule": feLAN2PortQoSPortMapRule,
       "feLAN2PortVIDNRLEnable": feLAN2PortVIDNRLEnable,
       "feLAN2PortMap2PIRL": feLAN2PortMap2PIRL,
       "feLAN2PortDeletePortMap2PIRL": feLAN2PortDeletePortMap2PIRL,
       "feLAN2PortEgressRateLimitation": feLAN2PortEgressRateLimitation,
       "feLAN2PortIngressRateLimitation": feLAN2PortIngressRateLimitation,
       "feLAN2PortDefaultVLAN": feLAN2PortDefaultVLAN,
       "feLAN2PortForceDefaultVID": feLAN2PortForceDefaultVID,
       "feLAN2PortVLANPortMode": feLAN2PortVLANPortMode,
       "feLAN2PortBlockAllUnknown": feLAN2PortBlockAllUnknown,
       "feLAN2PortIGMPSnooping": feLAN2PortIGMPSnooping,
       "feLAN2PortAddUnicast": feLAN2PortAddUnicast,
       "feLAN2PortAddMulticast": feLAN2PortAddMulticast,
       "feLAN2PortArpMirroring": feLAN2PortArpMirroring,
       "feLAN3Port": feLAN3Port,
       "feLAN3PortAutoNegotiation": feLAN3PortAutoNegotiation,
       "feLAN3PortSpeedMode": feLAN3PortSpeedMode,
       "feLAN3PortLinkStatus": feLAN3PortLinkStatus,
       "feLAN3PortFlowControl": feLAN3PortFlowControl,
       "feLAN3PortIEEEQoSPriority": feLAN3PortIEEEQoSPriority,
       "feLAN3PortIPQoSPriority": feLAN3PortIPQoSPriority,
       "feLAN3PortFramePriorityOverwrite": feLAN3PortFramePriorityOverwrite,
       "feLAN3PortQueuePriorityOverwrite": feLAN3PortQueuePriorityOverwrite,
       "feLAN3PortQueuePriority": feLAN3PortQueuePriority,
       "feLAN3PortQoSPortMapRule": feLAN3PortQoSPortMapRule,
       "feLAN3PortVIDNRLEnable": feLAN3PortVIDNRLEnable,
       "feLAN3PortMap2PIRL": feLAN3PortMap2PIRL,
       "feLAN3PortDeletePortMap2PIRL": feLAN3PortDeletePortMap2PIRL,
       "feLAN3PortEgressRateLimitation": feLAN3PortEgressRateLimitation,
       "feLAN3PortIngressRateLimitation": feLAN3PortIngressRateLimitation,
       "feLAN3PortDefaultVLAN": feLAN3PortDefaultVLAN,
       "feLAN3PortForceDefaultVID": feLAN3PortForceDefaultVID,
       "feLAN3PortVLANPortMode": feLAN3PortVLANPortMode,
       "feLAN3PortBlockAllUnknown": feLAN3PortBlockAllUnknown,
       "feLAN3PortIGMPSnooping": feLAN3PortIGMPSnooping,
       "feLAN3PortAddUnicast": feLAN3PortAddUnicast,
       "feLAN3PortAddMulticast": feLAN3PortAddMulticast,
       "feLAN3PortArpMirroring": feLAN3PortArpMirroring,
       "feLAN4Port": feLAN4Port,
       "feLAN4PortAutoNegotiation": feLAN4PortAutoNegotiation,
       "feLAN4PortSpeedMode": feLAN4PortSpeedMode,
       "feLAN4PortLinkStatus": feLAN4PortLinkStatus,
       "feLAN4PortFlowControl": feLAN4PortFlowControl,
       "feLAN4PortIEEEQoSPriority": feLAN4PortIEEEQoSPriority,
       "feLAN4PortIPQoSPriority": feLAN4PortIPQoSPriority,
       "feLAN4PortFramePriorityOverwrite": feLAN4PortFramePriorityOverwrite,
       "feLAN4PortQueuePriorityOverwrite": feLAN4PortQueuePriorityOverwrite,
       "feLAN4PortQueuePriority": feLAN4PortQueuePriority,
       "feLAN4PortQoSPortMapRule": feLAN4PortQoSPortMapRule,
       "feLAN4PortVIDNRLEnable": feLAN4PortVIDNRLEnable,
       "feLAN4PortMap2PIRL": feLAN4PortMap2PIRL,
       "feLAN4PortDeletePortMap2PIRL": feLAN4PortDeletePortMap2PIRL,
       "feLAN4PortEgressRateLimitation": feLAN4PortEgressRateLimitation,
       "feLAN4PortIngressRateLimitation": feLAN4PortIngressRateLimitation,
       "feLAN4PortDefaultVLAN": feLAN4PortDefaultVLAN,
       "feLAN4PortForceDefaultVID": feLAN4PortForceDefaultVID,
       "feLAN4PortVLANPortMode": feLAN4PortVLANPortMode,
       "feLAN4PortBlockAllUnknown": feLAN4PortBlockAllUnknown,
       "feLAN4PortIGMPSnooping": feLAN4PortIGMPSnooping,
       "feLAN4PortAddUnicast": feLAN4PortAddUnicast,
       "feLAN4PortAddMulticast": feLAN4PortAddMulticast,
       "feLAN4PortArpMirroring": feLAN4PortArpMirroring,
       "feModuleGroup": feModuleGroup}
)
