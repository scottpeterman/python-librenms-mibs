# SNMP MIB module (DKT-GE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dkt\DKT-GE-MIB
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

geMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GeSwitchEngine_ObjectIdentity = ObjectIdentity
geSwitchEngine = _GeSwitchEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 14, 1)
)


class _GeATU_Type(OctetString):
    """Custom type geATU based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20480),
    )


_GeATU_Type.__name__ = "OctetString"
_GeATU_Object = MibScalar
geATU = _GeATU_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 1, 1),
    _GeATU_Type()
)
geATU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geATU.setStatus("current")


class _GeUnicastDelete_Type(OctetString):
    """Custom type geUnicastDelete based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GeUnicastDelete_Type.__name__ = "OctetString"
_GeUnicastDelete_Object = MibScalar
geUnicastDelete = _GeUnicastDelete_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 1, 2),
    _GeUnicastDelete_Type()
)
geUnicastDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geUnicastDelete.setStatus("current")
_GeMulticastDelete_Type = IpAddress
_GeMulticastDelete_Object = MibScalar
geMulticastDelete = _GeMulticastDelete_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 1, 3),
    _GeMulticastDelete_Type()
)
geMulticastDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geMulticastDelete.setStatus("current")


class _GeIGMPSnooping_Type(Integer32):
    """Custom type geIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeIGMPSnooping_Type.__name__ = "Integer32"
_GeIGMPSnooping_Object = MibScalar
geIGMPSnooping = _GeIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 1, 4),
    _GeIGMPSnooping_Type()
)
geIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geIGMPSnooping.setStatus("current")


class _GeVTU_Type(OctetString):
    """Custom type geVTU based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9600),
    )


_GeVTU_Type.__name__ = "OctetString"
_GeVTU_Object = MibScalar
geVTU = _GeVTU_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 1, 5),
    _GeVTU_Type()
)
geVTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geVTU.setStatus("current")


class _GeVLANCreate_Type(OctetString):
    """Custom type geVLANCreate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GeVLANCreate_Type.__name__ = "OctetString"
_GeVLANCreate_Object = MibScalar
geVLANCreate = _GeVLANCreate_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 1, 6),
    _GeVLANCreate_Type()
)
geVLANCreate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geVLANCreate.setStatus("current")


class _GeVLANDelete_Type(Integer32):
    """Custom type geVLANDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_GeVLANDelete_Type.__name__ = "Integer32"
_GeVLANDelete_Object = MibScalar
geVLANDelete = _GeVLANDelete_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 1, 7),
    _GeVLANDelete_Type()
)
geVLANDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geVLANDelete.setStatus("current")


class _GeClearVTU_Type(Integer32):
    """Custom type geClearVTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_GeClearVTU_Type.__name__ = "Integer32"
_GeClearVTU_Object = MibScalar
geClearVTU = _GeClearVTU_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 1, 8),
    _GeClearVTU_Type()
)
geClearVTU.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geClearVTU.setStatus("current")


class _GeDumpPIRLBuckets_Type(OctetString):
    """Custom type geDumpPIRLBuckets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_GeDumpPIRLBuckets_Type.__name__ = "OctetString"
_GeDumpPIRLBuckets_Object = MibScalar
geDumpPIRLBuckets = _GeDumpPIRLBuckets_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 1, 9),
    _GeDumpPIRLBuckets_Type()
)
geDumpPIRLBuckets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geDumpPIRLBuckets.setStatus("current")


class _GeVLANProviderMode_Type(Integer32):
    """Custom type geVLANProviderMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeVLANProviderMode_Type.__name__ = "Integer32"
_GeVLANProviderMode_Object = MibScalar
geVLANProviderMode = _GeVLANProviderMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 1, 10),
    _GeVLANProviderMode_Type()
)
geVLANProviderMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geVLANProviderMode.setStatus("current")
_GePorts_ObjectIdentity = ObjectIdentity
gePorts = _GePorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2)
)
_GeCPUPort_ObjectIdentity = ObjectIdentity
geCPUPort = _GeCPUPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1)
)


class _GeCPUPortAutoNegotiation_Type(Integer32):
    """Custom type geCPUPortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_GeCPUPortAutoNegotiation_Type.__name__ = "Integer32"
_GeCPUPortAutoNegotiation_Object = MibScalar
geCPUPortAutoNegotiation = _GeCPUPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 1),
    _GeCPUPortAutoNegotiation_Type()
)
geCPUPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geCPUPortAutoNegotiation.setStatus("current")


class _GeCPUPortSpeedMode_Type(OctetString):
    """Custom type geCPUPortSpeedMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_GeCPUPortSpeedMode_Type.__name__ = "OctetString"
_GeCPUPortSpeedMode_Object = MibScalar
geCPUPortSpeedMode = _GeCPUPortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 2),
    _GeCPUPortSpeedMode_Type()
)
geCPUPortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geCPUPortSpeedMode.setStatus("current")


class _GeCPUPortLinkStatus_Type(Integer32):
    """Custom type geCPUPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeCPUPortLinkStatus_Type.__name__ = "Integer32"
_GeCPUPortLinkStatus_Object = MibScalar
geCPUPortLinkStatus = _GeCPUPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 3),
    _GeCPUPortLinkStatus_Type()
)
geCPUPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geCPUPortLinkStatus.setStatus("current")


class _GeCPUPortFlowControl_Type(Integer32):
    """Custom type geCPUPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeCPUPortFlowControl_Type.__name__ = "Integer32"
_GeCPUPortFlowControl_Object = MibScalar
geCPUPortFlowControl = _GeCPUPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 4),
    _GeCPUPortFlowControl_Type()
)
geCPUPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geCPUPortFlowControl.setStatus("current")


class _GeCPUPortIEEEQoSPriority_Type(Integer32):
    """Custom type geCPUPortIEEEQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeCPUPortIEEEQoSPriority_Type.__name__ = "Integer32"
_GeCPUPortIEEEQoSPriority_Object = MibScalar
geCPUPortIEEEQoSPriority = _GeCPUPortIEEEQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 5),
    _GeCPUPortIEEEQoSPriority_Type()
)
geCPUPortIEEEQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geCPUPortIEEEQoSPriority.setStatus("current")


class _GeCPUPortIPQoSPriority_Type(Integer32):
    """Custom type geCPUPortIPQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeCPUPortIPQoSPriority_Type.__name__ = "Integer32"
_GeCPUPortIPQoSPriority_Object = MibScalar
geCPUPortIPQoSPriority = _GeCPUPortIPQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 6),
    _GeCPUPortIPQoSPriority_Type()
)
geCPUPortIPQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geCPUPortIPQoSPriority.setStatus("current")


class _GeCPUPortQoSPortMapRule_Type(Integer32):
    """Custom type geCPUPortQoSPortMapRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeCPUPortQoSPortMapRule_Type.__name__ = "Integer32"
_GeCPUPortQoSPortMapRule_Object = MibScalar
geCPUPortQoSPortMapRule = _GeCPUPortQoSPortMapRule_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 7),
    _GeCPUPortQoSPortMapRule_Type()
)
geCPUPortQoSPortMapRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geCPUPortQoSPortMapRule.setStatus("current")


class _GeCPUPortVIDNRLEnable_Type(Integer32):
    """Custom type geCPUPortVIDNRLEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeCPUPortVIDNRLEnable_Type.__name__ = "Integer32"
_GeCPUPortVIDNRLEnable_Object = MibScalar
geCPUPortVIDNRLEnable = _GeCPUPortVIDNRLEnable_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 8),
    _GeCPUPortVIDNRLEnable_Type()
)
geCPUPortVIDNRLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geCPUPortVIDNRLEnable.setStatus("current")


class _GeCPUPortDisablePIRL2Bucket_Type(Integer32):
    """Custom type geCPUPortDisablePIRL2Bucket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_GeCPUPortDisablePIRL2Bucket_Type.__name__ = "Integer32"
_GeCPUPortDisablePIRL2Bucket_Object = MibScalar
geCPUPortDisablePIRL2Bucket = _GeCPUPortDisablePIRL2Bucket_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 9),
    _GeCPUPortDisablePIRL2Bucket_Type()
)
geCPUPortDisablePIRL2Bucket.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geCPUPortDisablePIRL2Bucket.setStatus("current")
_GeCPUPortEgressRateLimitation_Type = Integer32
_GeCPUPortEgressRateLimitation_Object = MibScalar
geCPUPortEgressRateLimitation = _GeCPUPortEgressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 10),
    _GeCPUPortEgressRateLimitation_Type()
)
geCPUPortEgressRateLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geCPUPortEgressRateLimitation.setStatus("current")


class _GeCPUPortIngressRateLimitation_Type(OctetString):
    """Custom type geCPUPortIngressRateLimitation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GeCPUPortIngressRateLimitation_Type.__name__ = "OctetString"
_GeCPUPortIngressRateLimitation_Object = MibScalar
geCPUPortIngressRateLimitation = _GeCPUPortIngressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 11),
    _GeCPUPortIngressRateLimitation_Type()
)
geCPUPortIngressRateLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geCPUPortIngressRateLimitation.setStatus("current")
_GeCPUPortDefaultVLAN_Type = Integer32
_GeCPUPortDefaultVLAN_Object = MibScalar
geCPUPortDefaultVLAN = _GeCPUPortDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 12),
    _GeCPUPortDefaultVLAN_Type()
)
geCPUPortDefaultVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geCPUPortDefaultVLAN.setStatus("current")


class _GeCPUPortForceDefaultVID_Type(Integer32):
    """Custom type geCPUPortForceDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeCPUPortForceDefaultVID_Type.__name__ = "Integer32"
_GeCPUPortForceDefaultVID_Object = MibScalar
geCPUPortForceDefaultVID = _GeCPUPortForceDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 13),
    _GeCPUPortForceDefaultVID_Type()
)
geCPUPortForceDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geCPUPortForceDefaultVID.setStatus("current")


class _GeCPUPortVLANPortMode_Type(Integer32):
    """Custom type geCPUPortVLANPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_GeCPUPortVLANPortMode_Type.__name__ = "Integer32"
_GeCPUPortVLANPortMode_Object = MibScalar
geCPUPortVLANPortMode = _GeCPUPortVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 14),
    _GeCPUPortVLANPortMode_Type()
)
geCPUPortVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geCPUPortVLANPortMode.setStatus("current")


class _GeCPUPortBlockAllUnknown_Type(Integer32):
    """Custom type geCPUPortBlockAllUnknown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeCPUPortBlockAllUnknown_Type.__name__ = "Integer32"
_GeCPUPortBlockAllUnknown_Object = MibScalar
geCPUPortBlockAllUnknown = _GeCPUPortBlockAllUnknown_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 15),
    _GeCPUPortBlockAllUnknown_Type()
)
geCPUPortBlockAllUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geCPUPortBlockAllUnknown.setStatus("current")


class _GeCPUPortIGMPSnooping_Type(Integer32):
    """Custom type geCPUPortIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeCPUPortIGMPSnooping_Type.__name__ = "Integer32"
_GeCPUPortIGMPSnooping_Object = MibScalar
geCPUPortIGMPSnooping = _GeCPUPortIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 16),
    _GeCPUPortIGMPSnooping_Type()
)
geCPUPortIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geCPUPortIGMPSnooping.setStatus("current")


class _GeCPUPortAddUnicast_Type(OctetString):
    """Custom type geCPUPortAddUnicast based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GeCPUPortAddUnicast_Type.__name__ = "OctetString"
_GeCPUPortAddUnicast_Object = MibScalar
geCPUPortAddUnicast = _GeCPUPortAddUnicast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 17),
    _GeCPUPortAddUnicast_Type()
)
geCPUPortAddUnicast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geCPUPortAddUnicast.setStatus("current")
_GeCPUPortAddMulticast_Type = IpAddress
_GeCPUPortAddMulticast_Object = MibScalar
geCPUPortAddMulticast = _GeCPUPortAddMulticast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 18),
    _GeCPUPortAddMulticast_Type()
)
geCPUPortAddMulticast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geCPUPortAddMulticast.setStatus("current")


class _GeCPUPortMtu_Type(Integer32):
    """Custom type geCPUPortMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GeCPUPortMtu_Type.__name__ = "Integer32"
_GeCPUPortMtu_Object = MibScalar
geCPUPortMtu = _GeCPUPortMtu_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 1, 19),
    _GeCPUPortMtu_Type()
)
geCPUPortMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geCPUPortMtu.setStatus("current")
_GeWANPort_ObjectIdentity = ObjectIdentity
geWANPort = _GeWANPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2)
)


class _GeWANPortAutoNegotiation_Type(Integer32):
    """Custom type geWANPortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_GeWANPortAutoNegotiation_Type.__name__ = "Integer32"
_GeWANPortAutoNegotiation_Object = MibScalar
geWANPortAutoNegotiation = _GeWANPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 1),
    _GeWANPortAutoNegotiation_Type()
)
geWANPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geWANPortAutoNegotiation.setStatus("current")


class _GeWANPortSpeedMode_Type(OctetString):
    """Custom type geWANPortSpeedMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_GeWANPortSpeedMode_Type.__name__ = "OctetString"
_GeWANPortSpeedMode_Object = MibScalar
geWANPortSpeedMode = _GeWANPortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 2),
    _GeWANPortSpeedMode_Type()
)
geWANPortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geWANPortSpeedMode.setStatus("current")


class _GeWANPortLinkStatus_Type(Integer32):
    """Custom type geWANPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeWANPortLinkStatus_Type.__name__ = "Integer32"
_GeWANPortLinkStatus_Object = MibScalar
geWANPortLinkStatus = _GeWANPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 3),
    _GeWANPortLinkStatus_Type()
)
geWANPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geWANPortLinkStatus.setStatus("current")


class _GeWANPortFlowControl_Type(Integer32):
    """Custom type geWANPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeWANPortFlowControl_Type.__name__ = "Integer32"
_GeWANPortFlowControl_Object = MibScalar
geWANPortFlowControl = _GeWANPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 4),
    _GeWANPortFlowControl_Type()
)
geWANPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geWANPortFlowControl.setStatus("current")


class _GeWANPortIEEEQoSPriority_Type(Integer32):
    """Custom type geWANPortIEEEQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeWANPortIEEEQoSPriority_Type.__name__ = "Integer32"
_GeWANPortIEEEQoSPriority_Object = MibScalar
geWANPortIEEEQoSPriority = _GeWANPortIEEEQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 5),
    _GeWANPortIEEEQoSPriority_Type()
)
geWANPortIEEEQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geWANPortIEEEQoSPriority.setStatus("current")


class _GeWANPortIPQoSPriority_Type(Integer32):
    """Custom type geWANPortIPQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeWANPortIPQoSPriority_Type.__name__ = "Integer32"
_GeWANPortIPQoSPriority_Object = MibScalar
geWANPortIPQoSPriority = _GeWANPortIPQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 6),
    _GeWANPortIPQoSPriority_Type()
)
geWANPortIPQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geWANPortIPQoSPriority.setStatus("current")


class _GeWANPortQoSPortMapRule_Type(Integer32):
    """Custom type geWANPortQoSPortMapRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeWANPortQoSPortMapRule_Type.__name__ = "Integer32"
_GeWANPortQoSPortMapRule_Object = MibScalar
geWANPortQoSPortMapRule = _GeWANPortQoSPortMapRule_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 7),
    _GeWANPortQoSPortMapRule_Type()
)
geWANPortQoSPortMapRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geWANPortQoSPortMapRule.setStatus("current")


class _GeWANPortVIDNRLEnable_Type(Integer32):
    """Custom type geWANPortVIDNRLEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeWANPortVIDNRLEnable_Type.__name__ = "Integer32"
_GeWANPortVIDNRLEnable_Object = MibScalar
geWANPortVIDNRLEnable = _GeWANPortVIDNRLEnable_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 8),
    _GeWANPortVIDNRLEnable_Type()
)
geWANPortVIDNRLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geWANPortVIDNRLEnable.setStatus("current")


class _GeWANPortDisablePIRL2Bucket_Type(Integer32):
    """Custom type geWANPortDisablePIRL2Bucket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_GeWANPortDisablePIRL2Bucket_Type.__name__ = "Integer32"
_GeWANPortDisablePIRL2Bucket_Object = MibScalar
geWANPortDisablePIRL2Bucket = _GeWANPortDisablePIRL2Bucket_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 9),
    _GeWANPortDisablePIRL2Bucket_Type()
)
geWANPortDisablePIRL2Bucket.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geWANPortDisablePIRL2Bucket.setStatus("current")
_GeWANPortEgressRateLimitation_Type = Integer32
_GeWANPortEgressRateLimitation_Object = MibScalar
geWANPortEgressRateLimitation = _GeWANPortEgressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 10),
    _GeWANPortEgressRateLimitation_Type()
)
geWANPortEgressRateLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geWANPortEgressRateLimitation.setStatus("current")


class _GeWANPortIngressRateLimitation_Type(OctetString):
    """Custom type geWANPortIngressRateLimitation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GeWANPortIngressRateLimitation_Type.__name__ = "OctetString"
_GeWANPortIngressRateLimitation_Object = MibScalar
geWANPortIngressRateLimitation = _GeWANPortIngressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 11),
    _GeWANPortIngressRateLimitation_Type()
)
geWANPortIngressRateLimitation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geWANPortIngressRateLimitation.setStatus("current")
_GeWANPortDefaultVLAN_Type = Integer32
_GeWANPortDefaultVLAN_Object = MibScalar
geWANPortDefaultVLAN = _GeWANPortDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 12),
    _GeWANPortDefaultVLAN_Type()
)
geWANPortDefaultVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geWANPortDefaultVLAN.setStatus("current")


class _GeWANPortForceDefaultVID_Type(Integer32):
    """Custom type geWANPortForceDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeWANPortForceDefaultVID_Type.__name__ = "Integer32"
_GeWANPortForceDefaultVID_Object = MibScalar
geWANPortForceDefaultVID = _GeWANPortForceDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 13),
    _GeWANPortForceDefaultVID_Type()
)
geWANPortForceDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geWANPortForceDefaultVID.setStatus("current")


class _GeWANPortVLANPortMode_Type(Integer32):
    """Custom type geWANPortVLANPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_GeWANPortVLANPortMode_Type.__name__ = "Integer32"
_GeWANPortVLANPortMode_Object = MibScalar
geWANPortVLANPortMode = _GeWANPortVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 14),
    _GeWANPortVLANPortMode_Type()
)
geWANPortVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geWANPortVLANPortMode.setStatus("current")


class _GeWANPortBlockAllUnknown_Type(Integer32):
    """Custom type geWANPortBlockAllUnknown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeWANPortBlockAllUnknown_Type.__name__ = "Integer32"
_GeWANPortBlockAllUnknown_Object = MibScalar
geWANPortBlockAllUnknown = _GeWANPortBlockAllUnknown_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 15),
    _GeWANPortBlockAllUnknown_Type()
)
geWANPortBlockAllUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geWANPortBlockAllUnknown.setStatus("current")


class _GeWANPortIGMPSnooping_Type(Integer32):
    """Custom type geWANPortIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeWANPortIGMPSnooping_Type.__name__ = "Integer32"
_GeWANPortIGMPSnooping_Object = MibScalar
geWANPortIGMPSnooping = _GeWANPortIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 16),
    _GeWANPortIGMPSnooping_Type()
)
geWANPortIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geWANPortIGMPSnooping.setStatus("current")


class _GeWANPortAddUnicast_Type(OctetString):
    """Custom type geWANPortAddUnicast based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GeWANPortAddUnicast_Type.__name__ = "OctetString"
_GeWANPortAddUnicast_Object = MibScalar
geWANPortAddUnicast = _GeWANPortAddUnicast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 17),
    _GeWANPortAddUnicast_Type()
)
geWANPortAddUnicast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geWANPortAddUnicast.setStatus("current")
_GeWANPortAddMulticast_Type = IpAddress
_GeWANPortAddMulticast_Object = MibScalar
geWANPortAddMulticast = _GeWANPortAddMulticast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 18),
    _GeWANPortAddMulticast_Type()
)
geWANPortAddMulticast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geWANPortAddMulticast.setStatus("current")


class _GeWANPortMtu_Type(Integer32):
    """Custom type geWANPortMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GeWANPortMtu_Type.__name__ = "Integer32"
_GeWANPortMtu_Object = MibScalar
geWANPortMtu = _GeWANPortMtu_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 19),
    _GeWANPortMtu_Type()
)
geWANPortMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geWANPortMtu.setStatus("current")


class _GeWANPortArpMirroring_Type(Integer32):
    """Custom type geWANPortArpMirroring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeWANPortArpMirroring_Type.__name__ = "Integer32"
_GeWANPortArpMirroring_Object = MibScalar
geWANPortArpMirroring = _GeWANPortArpMirroring_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 2, 20),
    _GeWANPortArpMirroring_Type()
)
geWANPortArpMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geWANPortArpMirroring.setStatus("current")
_GeLAN1Port_ObjectIdentity = ObjectIdentity
geLAN1Port = _GeLAN1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3)
)


class _GeLAN1PortAutoNegotiation_Type(Integer32):
    """Custom type geLAN1PortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_GeLAN1PortAutoNegotiation_Type.__name__ = "Integer32"
_GeLAN1PortAutoNegotiation_Object = MibScalar
geLAN1PortAutoNegotiation = _GeLAN1PortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 1),
    _GeLAN1PortAutoNegotiation_Type()
)
geLAN1PortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN1PortAutoNegotiation.setStatus("current")


class _GeLAN1PortSpeedMode_Type(OctetString):
    """Custom type geLAN1PortSpeedMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_GeLAN1PortSpeedMode_Type.__name__ = "OctetString"
_GeLAN1PortSpeedMode_Object = MibScalar
geLAN1PortSpeedMode = _GeLAN1PortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 2),
    _GeLAN1PortSpeedMode_Type()
)
geLAN1PortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN1PortSpeedMode.setStatus("current")


class _GeLAN1PortLinkStatus_Type(Integer32):
    """Custom type geLAN1PortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN1PortLinkStatus_Type.__name__ = "Integer32"
_GeLAN1PortLinkStatus_Object = MibScalar
geLAN1PortLinkStatus = _GeLAN1PortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 3),
    _GeLAN1PortLinkStatus_Type()
)
geLAN1PortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geLAN1PortLinkStatus.setStatus("current")


class _GeLAN1PortFlowControl_Type(Integer32):
    """Custom type geLAN1PortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN1PortFlowControl_Type.__name__ = "Integer32"
_GeLAN1PortFlowControl_Object = MibScalar
geLAN1PortFlowControl = _GeLAN1PortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 4),
    _GeLAN1PortFlowControl_Type()
)
geLAN1PortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN1PortFlowControl.setStatus("current")


class _GeLAN1PortIEEEQoSPriority_Type(Integer32):
    """Custom type geLAN1PortIEEEQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN1PortIEEEQoSPriority_Type.__name__ = "Integer32"
_GeLAN1PortIEEEQoSPriority_Object = MibScalar
geLAN1PortIEEEQoSPriority = _GeLAN1PortIEEEQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 5),
    _GeLAN1PortIEEEQoSPriority_Type()
)
geLAN1PortIEEEQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN1PortIEEEQoSPriority.setStatus("current")


class _GeLAN1PortIPQoSPriority_Type(Integer32):
    """Custom type geLAN1PortIPQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN1PortIPQoSPriority_Type.__name__ = "Integer32"
_GeLAN1PortIPQoSPriority_Object = MibScalar
geLAN1PortIPQoSPriority = _GeLAN1PortIPQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 6),
    _GeLAN1PortIPQoSPriority_Type()
)
geLAN1PortIPQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN1PortIPQoSPriority.setStatus("current")


class _GeLAN1PortQoSPortMapRule_Type(Integer32):
    """Custom type geLAN1PortQoSPortMapRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN1PortQoSPortMapRule_Type.__name__ = "Integer32"
_GeLAN1PortQoSPortMapRule_Object = MibScalar
geLAN1PortQoSPortMapRule = _GeLAN1PortQoSPortMapRule_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 7),
    _GeLAN1PortQoSPortMapRule_Type()
)
geLAN1PortQoSPortMapRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN1PortQoSPortMapRule.setStatus("current")


class _GeLAN1PortVIDNRLEnable_Type(Integer32):
    """Custom type geLAN1PortVIDNRLEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN1PortVIDNRLEnable_Type.__name__ = "Integer32"
_GeLAN1PortVIDNRLEnable_Object = MibScalar
geLAN1PortVIDNRLEnable = _GeLAN1PortVIDNRLEnable_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 8),
    _GeLAN1PortVIDNRLEnable_Type()
)
geLAN1PortVIDNRLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN1PortVIDNRLEnable.setStatus("current")


class _GeLAN1PortDisablePIRL2Bucket_Type(Integer32):
    """Custom type geLAN1PortDisablePIRL2Bucket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_GeLAN1PortDisablePIRL2Bucket_Type.__name__ = "Integer32"
_GeLAN1PortDisablePIRL2Bucket_Object = MibScalar
geLAN1PortDisablePIRL2Bucket = _GeLAN1PortDisablePIRL2Bucket_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 9),
    _GeLAN1PortDisablePIRL2Bucket_Type()
)
geLAN1PortDisablePIRL2Bucket.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN1PortDisablePIRL2Bucket.setStatus("current")
_GeLAN1PortEgressRateLimitation_Type = Integer32
_GeLAN1PortEgressRateLimitation_Object = MibScalar
geLAN1PortEgressRateLimitation = _GeLAN1PortEgressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 10),
    _GeLAN1PortEgressRateLimitation_Type()
)
geLAN1PortEgressRateLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN1PortEgressRateLimitation.setStatus("current")


class _GeLAN1PortIngressRateLimitation_Type(OctetString):
    """Custom type geLAN1PortIngressRateLimitation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GeLAN1PortIngressRateLimitation_Type.__name__ = "OctetString"
_GeLAN1PortIngressRateLimitation_Object = MibScalar
geLAN1PortIngressRateLimitation = _GeLAN1PortIngressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 11),
    _GeLAN1PortIngressRateLimitation_Type()
)
geLAN1PortIngressRateLimitation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN1PortIngressRateLimitation.setStatus("current")
_GeLAN1PortDefaultVLAN_Type = Integer32
_GeLAN1PortDefaultVLAN_Object = MibScalar
geLAN1PortDefaultVLAN = _GeLAN1PortDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 12),
    _GeLAN1PortDefaultVLAN_Type()
)
geLAN1PortDefaultVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN1PortDefaultVLAN.setStatus("current")


class _GeLAN1PortForceDefaultVID_Type(Integer32):
    """Custom type geLAN1PortForceDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN1PortForceDefaultVID_Type.__name__ = "Integer32"
_GeLAN1PortForceDefaultVID_Object = MibScalar
geLAN1PortForceDefaultVID = _GeLAN1PortForceDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 13),
    _GeLAN1PortForceDefaultVID_Type()
)
geLAN1PortForceDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN1PortForceDefaultVID.setStatus("current")


class _GeLAN1PortVLANPortMode_Type(Integer32):
    """Custom type geLAN1PortVLANPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_GeLAN1PortVLANPortMode_Type.__name__ = "Integer32"
_GeLAN1PortVLANPortMode_Object = MibScalar
geLAN1PortVLANPortMode = _GeLAN1PortVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 14),
    _GeLAN1PortVLANPortMode_Type()
)
geLAN1PortVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN1PortVLANPortMode.setStatus("current")


class _GeLAN1PortBlockAllUnknown_Type(Integer32):
    """Custom type geLAN1PortBlockAllUnknown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN1PortBlockAllUnknown_Type.__name__ = "Integer32"
_GeLAN1PortBlockAllUnknown_Object = MibScalar
geLAN1PortBlockAllUnknown = _GeLAN1PortBlockAllUnknown_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 15),
    _GeLAN1PortBlockAllUnknown_Type()
)
geLAN1PortBlockAllUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN1PortBlockAllUnknown.setStatus("current")


class _GeLAN1PortIGMPSnooping_Type(Integer32):
    """Custom type geLAN1PortIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN1PortIGMPSnooping_Type.__name__ = "Integer32"
_GeLAN1PortIGMPSnooping_Object = MibScalar
geLAN1PortIGMPSnooping = _GeLAN1PortIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 16),
    _GeLAN1PortIGMPSnooping_Type()
)
geLAN1PortIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN1PortIGMPSnooping.setStatus("current")


class _GeLAN1PortAddUnicast_Type(OctetString):
    """Custom type geLAN1PortAddUnicast based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GeLAN1PortAddUnicast_Type.__name__ = "OctetString"
_GeLAN1PortAddUnicast_Object = MibScalar
geLAN1PortAddUnicast = _GeLAN1PortAddUnicast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 17),
    _GeLAN1PortAddUnicast_Type()
)
geLAN1PortAddUnicast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN1PortAddUnicast.setStatus("current")
_GeLAN1PortAddMulticast_Type = IpAddress
_GeLAN1PortAddMulticast_Object = MibScalar
geLAN1PortAddMulticast = _GeLAN1PortAddMulticast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 18),
    _GeLAN1PortAddMulticast_Type()
)
geLAN1PortAddMulticast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN1PortAddMulticast.setStatus("current")


class _GeLAN1PortMtu_Type(Integer32):
    """Custom type geLAN1PortMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GeLAN1PortMtu_Type.__name__ = "Integer32"
_GeLAN1PortMtu_Object = MibScalar
geLAN1PortMtu = _GeLAN1PortMtu_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 19),
    _GeLAN1PortMtu_Type()
)
geLAN1PortMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN1PortMtu.setStatus("current")


class _GeLAN1PortArpMirroring_Type(Integer32):
    """Custom type geLAN1PortArpMirroring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN1PortArpMirroring_Type.__name__ = "Integer32"
_GeLAN1PortArpMirroring_Object = MibScalar
geLAN1PortArpMirroring = _GeLAN1PortArpMirroring_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 3, 20),
    _GeLAN1PortArpMirroring_Type()
)
geLAN1PortArpMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN1PortArpMirroring.setStatus("current")
_GeLAN2Port_ObjectIdentity = ObjectIdentity
geLAN2Port = _GeLAN2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4)
)


class _GeLAN2PortAutoNegotiation_Type(Integer32):
    """Custom type geLAN2PortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_GeLAN2PortAutoNegotiation_Type.__name__ = "Integer32"
_GeLAN2PortAutoNegotiation_Object = MibScalar
geLAN2PortAutoNegotiation = _GeLAN2PortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 1),
    _GeLAN2PortAutoNegotiation_Type()
)
geLAN2PortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN2PortAutoNegotiation.setStatus("current")


class _GeLAN2PortSpeedMode_Type(OctetString):
    """Custom type geLAN2PortSpeedMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_GeLAN2PortSpeedMode_Type.__name__ = "OctetString"
_GeLAN2PortSpeedMode_Object = MibScalar
geLAN2PortSpeedMode = _GeLAN2PortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 2),
    _GeLAN2PortSpeedMode_Type()
)
geLAN2PortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN2PortSpeedMode.setStatus("current")


class _GeLAN2PortLinkStatus_Type(Integer32):
    """Custom type geLAN2PortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN2PortLinkStatus_Type.__name__ = "Integer32"
_GeLAN2PortLinkStatus_Object = MibScalar
geLAN2PortLinkStatus = _GeLAN2PortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 3),
    _GeLAN2PortLinkStatus_Type()
)
geLAN2PortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geLAN2PortLinkStatus.setStatus("current")


class _GeLAN2PortFlowControl_Type(Integer32):
    """Custom type geLAN2PortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN2PortFlowControl_Type.__name__ = "Integer32"
_GeLAN2PortFlowControl_Object = MibScalar
geLAN2PortFlowControl = _GeLAN2PortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 4),
    _GeLAN2PortFlowControl_Type()
)
geLAN2PortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN2PortFlowControl.setStatus("current")


class _GeLAN2PortIEEEQoSPriority_Type(Integer32):
    """Custom type geLAN2PortIEEEQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN2PortIEEEQoSPriority_Type.__name__ = "Integer32"
_GeLAN2PortIEEEQoSPriority_Object = MibScalar
geLAN2PortIEEEQoSPriority = _GeLAN2PortIEEEQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 5),
    _GeLAN2PortIEEEQoSPriority_Type()
)
geLAN2PortIEEEQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN2PortIEEEQoSPriority.setStatus("current")


class _GeLAN2PortIPQoSPriority_Type(Integer32):
    """Custom type geLAN2PortIPQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN2PortIPQoSPriority_Type.__name__ = "Integer32"
_GeLAN2PortIPQoSPriority_Object = MibScalar
geLAN2PortIPQoSPriority = _GeLAN2PortIPQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 6),
    _GeLAN2PortIPQoSPriority_Type()
)
geLAN2PortIPQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN2PortIPQoSPriority.setStatus("current")


class _GeLAN2PortQoSPortMapRule_Type(Integer32):
    """Custom type geLAN2PortQoSPortMapRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN2PortQoSPortMapRule_Type.__name__ = "Integer32"
_GeLAN2PortQoSPortMapRule_Object = MibScalar
geLAN2PortQoSPortMapRule = _GeLAN2PortQoSPortMapRule_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 7),
    _GeLAN2PortQoSPortMapRule_Type()
)
geLAN2PortQoSPortMapRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN2PortQoSPortMapRule.setStatus("current")


class _GeLAN2PortVIDNRLEnable_Type(Integer32):
    """Custom type geLAN2PortVIDNRLEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN2PortVIDNRLEnable_Type.__name__ = "Integer32"
_GeLAN2PortVIDNRLEnable_Object = MibScalar
geLAN2PortVIDNRLEnable = _GeLAN2PortVIDNRLEnable_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 8),
    _GeLAN2PortVIDNRLEnable_Type()
)
geLAN2PortVIDNRLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN2PortVIDNRLEnable.setStatus("current")


class _GeLAN2PortDisablePIRL2Bucket_Type(Integer32):
    """Custom type geLAN2PortDisablePIRL2Bucket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_GeLAN2PortDisablePIRL2Bucket_Type.__name__ = "Integer32"
_GeLAN2PortDisablePIRL2Bucket_Object = MibScalar
geLAN2PortDisablePIRL2Bucket = _GeLAN2PortDisablePIRL2Bucket_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 9),
    _GeLAN2PortDisablePIRL2Bucket_Type()
)
geLAN2PortDisablePIRL2Bucket.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN2PortDisablePIRL2Bucket.setStatus("current")
_GeLAN2PortEgressRateLimitation_Type = Integer32
_GeLAN2PortEgressRateLimitation_Object = MibScalar
geLAN2PortEgressRateLimitation = _GeLAN2PortEgressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 10),
    _GeLAN2PortEgressRateLimitation_Type()
)
geLAN2PortEgressRateLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN2PortEgressRateLimitation.setStatus("current")


class _GeLAN2PortIngressRateLimitation_Type(OctetString):
    """Custom type geLAN2PortIngressRateLimitation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GeLAN2PortIngressRateLimitation_Type.__name__ = "OctetString"
_GeLAN2PortIngressRateLimitation_Object = MibScalar
geLAN2PortIngressRateLimitation = _GeLAN2PortIngressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 11),
    _GeLAN2PortIngressRateLimitation_Type()
)
geLAN2PortIngressRateLimitation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN2PortIngressRateLimitation.setStatus("current")
_GeLAN2PortDefaultVLAN_Type = Integer32
_GeLAN2PortDefaultVLAN_Object = MibScalar
geLAN2PortDefaultVLAN = _GeLAN2PortDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 12),
    _GeLAN2PortDefaultVLAN_Type()
)
geLAN2PortDefaultVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN2PortDefaultVLAN.setStatus("current")


class _GeLAN2PortForceDefaultVID_Type(Integer32):
    """Custom type geLAN2PortForceDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN2PortForceDefaultVID_Type.__name__ = "Integer32"
_GeLAN2PortForceDefaultVID_Object = MibScalar
geLAN2PortForceDefaultVID = _GeLAN2PortForceDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 13),
    _GeLAN2PortForceDefaultVID_Type()
)
geLAN2PortForceDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN2PortForceDefaultVID.setStatus("current")


class _GeLAN2PortVLANPortMode_Type(Integer32):
    """Custom type geLAN2PortVLANPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_GeLAN2PortVLANPortMode_Type.__name__ = "Integer32"
_GeLAN2PortVLANPortMode_Object = MibScalar
geLAN2PortVLANPortMode = _GeLAN2PortVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 14),
    _GeLAN2PortVLANPortMode_Type()
)
geLAN2PortVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN2PortVLANPortMode.setStatus("current")


class _GeLAN2PortBlockAllUnknown_Type(Integer32):
    """Custom type geLAN2PortBlockAllUnknown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN2PortBlockAllUnknown_Type.__name__ = "Integer32"
_GeLAN2PortBlockAllUnknown_Object = MibScalar
geLAN2PortBlockAllUnknown = _GeLAN2PortBlockAllUnknown_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 15),
    _GeLAN2PortBlockAllUnknown_Type()
)
geLAN2PortBlockAllUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN2PortBlockAllUnknown.setStatus("current")


class _GeLAN2PortIGMPSnooping_Type(Integer32):
    """Custom type geLAN2PortIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN2PortIGMPSnooping_Type.__name__ = "Integer32"
_GeLAN2PortIGMPSnooping_Object = MibScalar
geLAN2PortIGMPSnooping = _GeLAN2PortIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 16),
    _GeLAN2PortIGMPSnooping_Type()
)
geLAN2PortIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN2PortIGMPSnooping.setStatus("current")


class _GeLAN2PortAddUnicast_Type(OctetString):
    """Custom type geLAN2PortAddUnicast based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GeLAN2PortAddUnicast_Type.__name__ = "OctetString"
_GeLAN2PortAddUnicast_Object = MibScalar
geLAN2PortAddUnicast = _GeLAN2PortAddUnicast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 17),
    _GeLAN2PortAddUnicast_Type()
)
geLAN2PortAddUnicast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN2PortAddUnicast.setStatus("current")
_GeLAN2PortAddMulticast_Type = IpAddress
_GeLAN2PortAddMulticast_Object = MibScalar
geLAN2PortAddMulticast = _GeLAN2PortAddMulticast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 18),
    _GeLAN2PortAddMulticast_Type()
)
geLAN2PortAddMulticast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN2PortAddMulticast.setStatus("current")


class _GeLAN2PortMtu_Type(Integer32):
    """Custom type geLAN2PortMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GeLAN2PortMtu_Type.__name__ = "Integer32"
_GeLAN2PortMtu_Object = MibScalar
geLAN2PortMtu = _GeLAN2PortMtu_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 19),
    _GeLAN2PortMtu_Type()
)
geLAN2PortMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN2PortMtu.setStatus("current")


class _GeLAN2PortArpMirroring_Type(Integer32):
    """Custom type geLAN2PortArpMirroring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN2PortArpMirroring_Type.__name__ = "Integer32"
_GeLAN2PortArpMirroring_Object = MibScalar
geLAN2PortArpMirroring = _GeLAN2PortArpMirroring_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 4, 20),
    _GeLAN2PortArpMirroring_Type()
)
geLAN2PortArpMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN2PortArpMirroring.setStatus("current")
_GeLAN3Port_ObjectIdentity = ObjectIdentity
geLAN3Port = _GeLAN3Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5)
)


class _GeLAN3PortAutoNegotiation_Type(Integer32):
    """Custom type geLAN3PortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_GeLAN3PortAutoNegotiation_Type.__name__ = "Integer32"
_GeLAN3PortAutoNegotiation_Object = MibScalar
geLAN3PortAutoNegotiation = _GeLAN3PortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 1),
    _GeLAN3PortAutoNegotiation_Type()
)
geLAN3PortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN3PortAutoNegotiation.setStatus("current")


class _GeLAN3PortSpeedMode_Type(OctetString):
    """Custom type geLAN3PortSpeedMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_GeLAN3PortSpeedMode_Type.__name__ = "OctetString"
_GeLAN3PortSpeedMode_Object = MibScalar
geLAN3PortSpeedMode = _GeLAN3PortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 2),
    _GeLAN3PortSpeedMode_Type()
)
geLAN3PortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN3PortSpeedMode.setStatus("current")


class _GeLAN3PortLinkStatus_Type(Integer32):
    """Custom type geLAN3PortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN3PortLinkStatus_Type.__name__ = "Integer32"
_GeLAN3PortLinkStatus_Object = MibScalar
geLAN3PortLinkStatus = _GeLAN3PortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 3),
    _GeLAN3PortLinkStatus_Type()
)
geLAN3PortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geLAN3PortLinkStatus.setStatus("current")


class _GeLAN3PortFlowControl_Type(Integer32):
    """Custom type geLAN3PortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN3PortFlowControl_Type.__name__ = "Integer32"
_GeLAN3PortFlowControl_Object = MibScalar
geLAN3PortFlowControl = _GeLAN3PortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 4),
    _GeLAN3PortFlowControl_Type()
)
geLAN3PortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN3PortFlowControl.setStatus("current")


class _GeLAN3PortIEEEQoSPriority_Type(Integer32):
    """Custom type geLAN3PortIEEEQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN3PortIEEEQoSPriority_Type.__name__ = "Integer32"
_GeLAN3PortIEEEQoSPriority_Object = MibScalar
geLAN3PortIEEEQoSPriority = _GeLAN3PortIEEEQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 5),
    _GeLAN3PortIEEEQoSPriority_Type()
)
geLAN3PortIEEEQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN3PortIEEEQoSPriority.setStatus("current")


class _GeLAN3PortIPQoSPriority_Type(Integer32):
    """Custom type geLAN3PortIPQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN3PortIPQoSPriority_Type.__name__ = "Integer32"
_GeLAN3PortIPQoSPriority_Object = MibScalar
geLAN3PortIPQoSPriority = _GeLAN3PortIPQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 6),
    _GeLAN3PortIPQoSPriority_Type()
)
geLAN3PortIPQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN3PortIPQoSPriority.setStatus("current")


class _GeLAN3PortQoSPortMapRule_Type(Integer32):
    """Custom type geLAN3PortQoSPortMapRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN3PortQoSPortMapRule_Type.__name__ = "Integer32"
_GeLAN3PortQoSPortMapRule_Object = MibScalar
geLAN3PortQoSPortMapRule = _GeLAN3PortQoSPortMapRule_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 7),
    _GeLAN3PortQoSPortMapRule_Type()
)
geLAN3PortQoSPortMapRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN3PortQoSPortMapRule.setStatus("current")


class _GeLAN3PortVIDNRLEnable_Type(Integer32):
    """Custom type geLAN3PortVIDNRLEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN3PortVIDNRLEnable_Type.__name__ = "Integer32"
_GeLAN3PortVIDNRLEnable_Object = MibScalar
geLAN3PortVIDNRLEnable = _GeLAN3PortVIDNRLEnable_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 8),
    _GeLAN3PortVIDNRLEnable_Type()
)
geLAN3PortVIDNRLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN3PortVIDNRLEnable.setStatus("current")


class _GeLAN3PortDisablePIRL2Bucket_Type(Integer32):
    """Custom type geLAN3PortDisablePIRL2Bucket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_GeLAN3PortDisablePIRL2Bucket_Type.__name__ = "Integer32"
_GeLAN3PortDisablePIRL2Bucket_Object = MibScalar
geLAN3PortDisablePIRL2Bucket = _GeLAN3PortDisablePIRL2Bucket_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 9),
    _GeLAN3PortDisablePIRL2Bucket_Type()
)
geLAN3PortDisablePIRL2Bucket.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN3PortDisablePIRL2Bucket.setStatus("current")
_GeLAN3PortEgressRateLimitation_Type = Integer32
_GeLAN3PortEgressRateLimitation_Object = MibScalar
geLAN3PortEgressRateLimitation = _GeLAN3PortEgressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 10),
    _GeLAN3PortEgressRateLimitation_Type()
)
geLAN3PortEgressRateLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN3PortEgressRateLimitation.setStatus("current")


class _GeLAN3PortIngressRateLimitation_Type(OctetString):
    """Custom type geLAN3PortIngressRateLimitation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GeLAN3PortIngressRateLimitation_Type.__name__ = "OctetString"
_GeLAN3PortIngressRateLimitation_Object = MibScalar
geLAN3PortIngressRateLimitation = _GeLAN3PortIngressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 11),
    _GeLAN3PortIngressRateLimitation_Type()
)
geLAN3PortIngressRateLimitation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN3PortIngressRateLimitation.setStatus("current")
_GeLAN3PortDefaultVLAN_Type = Integer32
_GeLAN3PortDefaultVLAN_Object = MibScalar
geLAN3PortDefaultVLAN = _GeLAN3PortDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 12),
    _GeLAN3PortDefaultVLAN_Type()
)
geLAN3PortDefaultVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN3PortDefaultVLAN.setStatus("current")


class _GeLAN3PortForceDefaultVID_Type(Integer32):
    """Custom type geLAN3PortForceDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN3PortForceDefaultVID_Type.__name__ = "Integer32"
_GeLAN3PortForceDefaultVID_Object = MibScalar
geLAN3PortForceDefaultVID = _GeLAN3PortForceDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 13),
    _GeLAN3PortForceDefaultVID_Type()
)
geLAN3PortForceDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN3PortForceDefaultVID.setStatus("current")


class _GeLAN3PortVLANPortMode_Type(Integer32):
    """Custom type geLAN3PortVLANPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_GeLAN3PortVLANPortMode_Type.__name__ = "Integer32"
_GeLAN3PortVLANPortMode_Object = MibScalar
geLAN3PortVLANPortMode = _GeLAN3PortVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 14),
    _GeLAN3PortVLANPortMode_Type()
)
geLAN3PortVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN3PortVLANPortMode.setStatus("current")


class _GeLAN3PortBlockAllUnknown_Type(Integer32):
    """Custom type geLAN3PortBlockAllUnknown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN3PortBlockAllUnknown_Type.__name__ = "Integer32"
_GeLAN3PortBlockAllUnknown_Object = MibScalar
geLAN3PortBlockAllUnknown = _GeLAN3PortBlockAllUnknown_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 15),
    _GeLAN3PortBlockAllUnknown_Type()
)
geLAN3PortBlockAllUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN3PortBlockAllUnknown.setStatus("current")


class _GeLAN3PortIGMPSnooping_Type(Integer32):
    """Custom type geLAN3PortIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN3PortIGMPSnooping_Type.__name__ = "Integer32"
_GeLAN3PortIGMPSnooping_Object = MibScalar
geLAN3PortIGMPSnooping = _GeLAN3PortIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 16),
    _GeLAN3PortIGMPSnooping_Type()
)
geLAN3PortIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN3PortIGMPSnooping.setStatus("current")


class _GeLAN3PortAddUnicast_Type(OctetString):
    """Custom type geLAN3PortAddUnicast based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GeLAN3PortAddUnicast_Type.__name__ = "OctetString"
_GeLAN3PortAddUnicast_Object = MibScalar
geLAN3PortAddUnicast = _GeLAN3PortAddUnicast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 17),
    _GeLAN3PortAddUnicast_Type()
)
geLAN3PortAddUnicast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN3PortAddUnicast.setStatus("current")
_GeLAN3PortAddMulticast_Type = IpAddress
_GeLAN3PortAddMulticast_Object = MibScalar
geLAN3PortAddMulticast = _GeLAN3PortAddMulticast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 18),
    _GeLAN3PortAddMulticast_Type()
)
geLAN3PortAddMulticast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN3PortAddMulticast.setStatus("current")


class _GeLAN3PortMtu_Type(Integer32):
    """Custom type geLAN3PortMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GeLAN3PortMtu_Type.__name__ = "Integer32"
_GeLAN3PortMtu_Object = MibScalar
geLAN3PortMtu = _GeLAN3PortMtu_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 19),
    _GeLAN3PortMtu_Type()
)
geLAN3PortMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN3PortMtu.setStatus("current")


class _GeLAN3PortArpMirroring_Type(Integer32):
    """Custom type geLAN3PortArpMirroring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN3PortArpMirroring_Type.__name__ = "Integer32"
_GeLAN3PortArpMirroring_Object = MibScalar
geLAN3PortArpMirroring = _GeLAN3PortArpMirroring_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 5, 20),
    _GeLAN3PortArpMirroring_Type()
)
geLAN3PortArpMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN3PortArpMirroring.setStatus("current")
_GeLAN4Port_ObjectIdentity = ObjectIdentity
geLAN4Port = _GeLAN4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6)
)


class _GeLAN4PortAutoNegotiation_Type(Integer32):
    """Custom type geLAN4PortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_GeLAN4PortAutoNegotiation_Type.__name__ = "Integer32"
_GeLAN4PortAutoNegotiation_Object = MibScalar
geLAN4PortAutoNegotiation = _GeLAN4PortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 1),
    _GeLAN4PortAutoNegotiation_Type()
)
geLAN4PortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN4PortAutoNegotiation.setStatus("current")


class _GeLAN4PortSpeedMode_Type(OctetString):
    """Custom type geLAN4PortSpeedMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_GeLAN4PortSpeedMode_Type.__name__ = "OctetString"
_GeLAN4PortSpeedMode_Object = MibScalar
geLAN4PortSpeedMode = _GeLAN4PortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 2),
    _GeLAN4PortSpeedMode_Type()
)
geLAN4PortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN4PortSpeedMode.setStatus("current")


class _GeLAN4PortLinkStatus_Type(Integer32):
    """Custom type geLAN4PortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN4PortLinkStatus_Type.__name__ = "Integer32"
_GeLAN4PortLinkStatus_Object = MibScalar
geLAN4PortLinkStatus = _GeLAN4PortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 3),
    _GeLAN4PortLinkStatus_Type()
)
geLAN4PortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geLAN4PortLinkStatus.setStatus("current")


class _GeLAN4PortFlowControl_Type(Integer32):
    """Custom type geLAN4PortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN4PortFlowControl_Type.__name__ = "Integer32"
_GeLAN4PortFlowControl_Object = MibScalar
geLAN4PortFlowControl = _GeLAN4PortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 4),
    _GeLAN4PortFlowControl_Type()
)
geLAN4PortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN4PortFlowControl.setStatus("current")


class _GeLAN4PortIEEEQoSPriority_Type(Integer32):
    """Custom type geLAN4PortIEEEQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN4PortIEEEQoSPriority_Type.__name__ = "Integer32"
_GeLAN4PortIEEEQoSPriority_Object = MibScalar
geLAN4PortIEEEQoSPriority = _GeLAN4PortIEEEQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 5),
    _GeLAN4PortIEEEQoSPriority_Type()
)
geLAN4PortIEEEQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN4PortIEEEQoSPriority.setStatus("current")


class _GeLAN4PortIPQoSPriority_Type(Integer32):
    """Custom type geLAN4PortIPQoSPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN4PortIPQoSPriority_Type.__name__ = "Integer32"
_GeLAN4PortIPQoSPriority_Object = MibScalar
geLAN4PortIPQoSPriority = _GeLAN4PortIPQoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 6),
    _GeLAN4PortIPQoSPriority_Type()
)
geLAN4PortIPQoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN4PortIPQoSPriority.setStatus("current")


class _GeLAN4PortQoSPortMapRule_Type(Integer32):
    """Custom type geLAN4PortQoSPortMapRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN4PortQoSPortMapRule_Type.__name__ = "Integer32"
_GeLAN4PortQoSPortMapRule_Object = MibScalar
geLAN4PortQoSPortMapRule = _GeLAN4PortQoSPortMapRule_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 7),
    _GeLAN4PortQoSPortMapRule_Type()
)
geLAN4PortQoSPortMapRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN4PortQoSPortMapRule.setStatus("current")


class _GeLAN4PortVIDNRLEnable_Type(Integer32):
    """Custom type geLAN4PortVIDNRLEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN4PortVIDNRLEnable_Type.__name__ = "Integer32"
_GeLAN4PortVIDNRLEnable_Object = MibScalar
geLAN4PortVIDNRLEnable = _GeLAN4PortVIDNRLEnable_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 8),
    _GeLAN4PortVIDNRLEnable_Type()
)
geLAN4PortVIDNRLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN4PortVIDNRLEnable.setStatus("current")


class _GeLAN4PortDisablePIRL2Bucket_Type(Integer32):
    """Custom type geLAN4PortDisablePIRL2Bucket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_GeLAN4PortDisablePIRL2Bucket_Type.__name__ = "Integer32"
_GeLAN4PortDisablePIRL2Bucket_Object = MibScalar
geLAN4PortDisablePIRL2Bucket = _GeLAN4PortDisablePIRL2Bucket_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 9),
    _GeLAN4PortDisablePIRL2Bucket_Type()
)
geLAN4PortDisablePIRL2Bucket.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN4PortDisablePIRL2Bucket.setStatus("current")
_GeLAN4PortEgressRateLimitation_Type = Integer32
_GeLAN4PortEgressRateLimitation_Object = MibScalar
geLAN4PortEgressRateLimitation = _GeLAN4PortEgressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 10),
    _GeLAN4PortEgressRateLimitation_Type()
)
geLAN4PortEgressRateLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN4PortEgressRateLimitation.setStatus("current")


class _GeLAN4PortIngressRateLimitation_Type(OctetString):
    """Custom type geLAN4PortIngressRateLimitation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GeLAN4PortIngressRateLimitation_Type.__name__ = "OctetString"
_GeLAN4PortIngressRateLimitation_Object = MibScalar
geLAN4PortIngressRateLimitation = _GeLAN4PortIngressRateLimitation_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 11),
    _GeLAN4PortIngressRateLimitation_Type()
)
geLAN4PortIngressRateLimitation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN4PortIngressRateLimitation.setStatus("current")
_GeLAN4PortDefaultVLAN_Type = Integer32
_GeLAN4PortDefaultVLAN_Object = MibScalar
geLAN4PortDefaultVLAN = _GeLAN4PortDefaultVLAN_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 12),
    _GeLAN4PortDefaultVLAN_Type()
)
geLAN4PortDefaultVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN4PortDefaultVLAN.setStatus("current")


class _GeLAN4PortForceDefaultVID_Type(Integer32):
    """Custom type geLAN4PortForceDefaultVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN4PortForceDefaultVID_Type.__name__ = "Integer32"
_GeLAN4PortForceDefaultVID_Object = MibScalar
geLAN4PortForceDefaultVID = _GeLAN4PortForceDefaultVID_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 13),
    _GeLAN4PortForceDefaultVID_Type()
)
geLAN4PortForceDefaultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN4PortForceDefaultVID.setStatus("current")


class _GeLAN4PortVLANPortMode_Type(Integer32):
    """Custom type geLAN4PortVLANPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_GeLAN4PortVLANPortMode_Type.__name__ = "Integer32"
_GeLAN4PortVLANPortMode_Object = MibScalar
geLAN4PortVLANPortMode = _GeLAN4PortVLANPortMode_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 14),
    _GeLAN4PortVLANPortMode_Type()
)
geLAN4PortVLANPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN4PortVLANPortMode.setStatus("current")


class _GeLAN4PortBlockAllUnknown_Type(Integer32):
    """Custom type geLAN4PortBlockAllUnknown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN4PortBlockAllUnknown_Type.__name__ = "Integer32"
_GeLAN4PortBlockAllUnknown_Object = MibScalar
geLAN4PortBlockAllUnknown = _GeLAN4PortBlockAllUnknown_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 15),
    _GeLAN4PortBlockAllUnknown_Type()
)
geLAN4PortBlockAllUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN4PortBlockAllUnknown.setStatus("current")


class _GeLAN4PortIGMPSnooping_Type(Integer32):
    """Custom type geLAN4PortIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN4PortIGMPSnooping_Type.__name__ = "Integer32"
_GeLAN4PortIGMPSnooping_Object = MibScalar
geLAN4PortIGMPSnooping = _GeLAN4PortIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 16),
    _GeLAN4PortIGMPSnooping_Type()
)
geLAN4PortIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN4PortIGMPSnooping.setStatus("current")


class _GeLAN4PortAddUnicast_Type(OctetString):
    """Custom type geLAN4PortAddUnicast based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_GeLAN4PortAddUnicast_Type.__name__ = "OctetString"
_GeLAN4PortAddUnicast_Object = MibScalar
geLAN4PortAddUnicast = _GeLAN4PortAddUnicast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 17),
    _GeLAN4PortAddUnicast_Type()
)
geLAN4PortAddUnicast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN4PortAddUnicast.setStatus("current")
_GeLAN4PortAddMulticast_Type = IpAddress
_GeLAN4PortAddMulticast_Object = MibScalar
geLAN4PortAddMulticast = _GeLAN4PortAddMulticast_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 18),
    _GeLAN4PortAddMulticast_Type()
)
geLAN4PortAddMulticast.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    geLAN4PortAddMulticast.setStatus("current")


class _GeLAN4PortMtu_Type(Integer32):
    """Custom type geLAN4PortMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GeLAN4PortMtu_Type.__name__ = "Integer32"
_GeLAN4PortMtu_Object = MibScalar
geLAN4PortMtu = _GeLAN4PortMtu_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 19),
    _GeLAN4PortMtu_Type()
)
geLAN4PortMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN4PortMtu.setStatus("current")


class _GeLAN4PortArpMirroring_Type(Integer32):
    """Custom type geLAN4PortArpMirroring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeLAN4PortArpMirroring_Type.__name__ = "Integer32"
_GeLAN4PortArpMirroring_Object = MibScalar
geLAN4PortArpMirroring = _GeLAN4PortArpMirroring_Object(
    (1, 3, 6, 1, 4, 1, 27304, 14, 2, 6, 20),
    _GeLAN4PortArpMirroring_Type()
)
geLAN4PortArpMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geLAN4PortArpMirroring.setStatus("current")

# Managed Objects groups

geModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27304, 14, 4)
)
geModuleGroup.setObjects(
      *(("DKT-GE-MIB", "geSwitchEngine"),
        ("DKT-GE-MIB", "geATU"),
        ("DKT-GE-MIB", "geUnicastDelete"),
        ("DKT-GE-MIB", "geMulticastDelete"),
        ("DKT-GE-MIB", "geIGMPSnooping"),
        ("DKT-GE-MIB", "geVTU"),
        ("DKT-GE-MIB", "geVLANCreate"),
        ("DKT-GE-MIB", "geVLANDelete"),
        ("DKT-GE-MIB", "geClearVTU"),
        ("DKT-GE-MIB", "geVLANProviderMode"),
        ("DKT-GE-MIB", "gePorts"),
        ("DKT-GE-MIB", "geDumpPIRLBuckets"),
        ("DKT-GE-MIB", "geCPUPort"),
        ("DKT-GE-MIB", "geCPUPortAutoNegotiation"),
        ("DKT-GE-MIB", "geCPUPortSpeedMode"),
        ("DKT-GE-MIB", "geCPUPortLinkStatus"),
        ("DKT-GE-MIB", "geCPUPortFlowControl"),
        ("DKT-GE-MIB", "geCPUPortIEEEQoSPriority"),
        ("DKT-GE-MIB", "geCPUPortIPQoSPriority"),
        ("DKT-GE-MIB", "geCPUPortQoSPortMapRule"),
        ("DKT-GE-MIB", "geCPUPortVIDNRLEnable"),
        ("DKT-GE-MIB", "geCPUPortDisablePIRL2Bucket"),
        ("DKT-GE-MIB", "geCPUPortEgressRateLimitation"),
        ("DKT-GE-MIB", "geCPUPortIngressRateLimitation"),
        ("DKT-GE-MIB", "geCPUPortDefaultVLAN"),
        ("DKT-GE-MIB", "geCPUPortForceDefaultVID"),
        ("DKT-GE-MIB", "geCPUPortVLANPortMode"),
        ("DKT-GE-MIB", "geCPUPortBlockAllUnknown"),
        ("DKT-GE-MIB", "geCPUPortIGMPSnooping"),
        ("DKT-GE-MIB", "geCPUPortAddUnicast"),
        ("DKT-GE-MIB", "geCPUPortAddMulticast"),
        ("DKT-GE-MIB", "geCPUPortMtu"),
        ("DKT-GE-MIB", "geWANPort"),
        ("DKT-GE-MIB", "geWANPortAutoNegotiation"),
        ("DKT-GE-MIB", "geWANPortSpeedMode"),
        ("DKT-GE-MIB", "geWANPortLinkStatus"),
        ("DKT-GE-MIB", "geWANPortFlowControl"),
        ("DKT-GE-MIB", "geWANPortIEEEQoSPriority"),
        ("DKT-GE-MIB", "geWANPortIPQoSPriority"),
        ("DKT-GE-MIB", "geWANPortQoSPortMapRule"),
        ("DKT-GE-MIB", "geWANPortVIDNRLEnable"),
        ("DKT-GE-MIB", "geWANPortDisablePIRL2Bucket"),
        ("DKT-GE-MIB", "geWANPortEgressRateLimitation"),
        ("DKT-GE-MIB", "geWANPortIngressRateLimitation"),
        ("DKT-GE-MIB", "geWANPortDefaultVLAN"),
        ("DKT-GE-MIB", "geWANPortForceDefaultVID"),
        ("DKT-GE-MIB", "geWANPortVLANPortMode"),
        ("DKT-GE-MIB", "geWANPortBlockAllUnknown"),
        ("DKT-GE-MIB", "geWANPortIGMPSnooping"),
        ("DKT-GE-MIB", "geWANPortAddUnicast"),
        ("DKT-GE-MIB", "geWANPortAddMulticast"),
        ("DKT-GE-MIB", "geWANPortMtu"),
        ("DKT-GE-MIB", "geWANPortArpMirroring"),
        ("DKT-GE-MIB", "geLAN1Port"),
        ("DKT-GE-MIB", "geLAN1PortAutoNegotiation"),
        ("DKT-GE-MIB", "geLAN1PortSpeedMode"),
        ("DKT-GE-MIB", "geLAN1PortLinkStatus"),
        ("DKT-GE-MIB", "geLAN1PortFlowControl"),
        ("DKT-GE-MIB", "geLAN1PortIEEEQoSPriority"),
        ("DKT-GE-MIB", "geLAN1PortIPQoSPriority"),
        ("DKT-GE-MIB", "geLAN1PortQoSPortMapRule"),
        ("DKT-GE-MIB", "geLAN1PortVIDNRLEnable"),
        ("DKT-GE-MIB", "geLAN1PortDisablePIRL2Bucket"),
        ("DKT-GE-MIB", "geLAN1PortEgressRateLimitation"),
        ("DKT-GE-MIB", "geLAN1PortIngressRateLimitation"),
        ("DKT-GE-MIB", "geLAN1PortDefaultVLAN"),
        ("DKT-GE-MIB", "geLAN1PortForceDefaultVID"),
        ("DKT-GE-MIB", "geLAN1PortVLANPortMode"),
        ("DKT-GE-MIB", "geLAN1PortBlockAllUnknown"),
        ("DKT-GE-MIB", "geLAN1PortIGMPSnooping"),
        ("DKT-GE-MIB", "geLAN1PortAddUnicast"),
        ("DKT-GE-MIB", "geLAN1PortAddMulticast"),
        ("DKT-GE-MIB", "geLAN1PortMtu"),
        ("DKT-GE-MIB", "geLAN1PortArpMirroring"),
        ("DKT-GE-MIB", "geLAN2Port"),
        ("DKT-GE-MIB", "geLAN2PortAutoNegotiation"),
        ("DKT-GE-MIB", "geLAN2PortSpeedMode"),
        ("DKT-GE-MIB", "geLAN2PortLinkStatus"),
        ("DKT-GE-MIB", "geLAN2PortFlowControl"),
        ("DKT-GE-MIB", "geLAN2PortIEEEQoSPriority"),
        ("DKT-GE-MIB", "geLAN2PortIPQoSPriority"),
        ("DKT-GE-MIB", "geLAN2PortQoSPortMapRule"),
        ("DKT-GE-MIB", "geLAN2PortVIDNRLEnable"),
        ("DKT-GE-MIB", "geLAN2PortDisablePIRL2Bucket"),
        ("DKT-GE-MIB", "geLAN2PortEgressRateLimitation"),
        ("DKT-GE-MIB", "geLAN2PortIngressRateLimitation"),
        ("DKT-GE-MIB", "geLAN2PortDefaultVLAN"),
        ("DKT-GE-MIB", "geLAN2PortForceDefaultVID"),
        ("DKT-GE-MIB", "geLAN2PortVLANPortMode"),
        ("DKT-GE-MIB", "geLAN2PortBlockAllUnknown"),
        ("DKT-GE-MIB", "geLAN2PortIGMPSnooping"),
        ("DKT-GE-MIB", "geLAN2PortAddUnicast"),
        ("DKT-GE-MIB", "geLAN2PortAddMulticast"),
        ("DKT-GE-MIB", "geLAN2PortMtu"),
        ("DKT-GE-MIB", "geLAN2PortArpMirroring"),
        ("DKT-GE-MIB", "geLAN3Port"),
        ("DKT-GE-MIB", "geLAN3PortAutoNegotiation"),
        ("DKT-GE-MIB", "geLAN3PortSpeedMode"),
        ("DKT-GE-MIB", "geLAN3PortLinkStatus"),
        ("DKT-GE-MIB", "geLAN3PortFlowControl"),
        ("DKT-GE-MIB", "geLAN3PortIEEEQoSPriority"),
        ("DKT-GE-MIB", "geLAN3PortIPQoSPriority"),
        ("DKT-GE-MIB", "geLAN3PortQoSPortMapRule"),
        ("DKT-GE-MIB", "geLAN3PortVIDNRLEnable"),
        ("DKT-GE-MIB", "geLAN3PortDisablePIRL2Bucket"),
        ("DKT-GE-MIB", "geLAN3PortEgressRateLimitation"),
        ("DKT-GE-MIB", "geLAN3PortIngressRateLimitation"),
        ("DKT-GE-MIB", "geLAN3PortDefaultVLAN"),
        ("DKT-GE-MIB", "geLAN3PortForceDefaultVID"),
        ("DKT-GE-MIB", "geLAN3PortVLANPortMode"),
        ("DKT-GE-MIB", "geLAN3PortBlockAllUnknown"),
        ("DKT-GE-MIB", "geLAN3PortIGMPSnooping"),
        ("DKT-GE-MIB", "geLAN3PortAddUnicast"),
        ("DKT-GE-MIB", "geLAN3PortAddMulticast"),
        ("DKT-GE-MIB", "geLAN3PortMtu"),
        ("DKT-GE-MIB", "geLAN3PortArpMirroring"),
        ("DKT-GE-MIB", "geLAN4Port"),
        ("DKT-GE-MIB", "geLAN4PortAutoNegotiation"),
        ("DKT-GE-MIB", "geLAN4PortSpeedMode"),
        ("DKT-GE-MIB", "geLAN4PortLinkStatus"),
        ("DKT-GE-MIB", "geLAN4PortFlowControl"),
        ("DKT-GE-MIB", "geLAN4PortIEEEQoSPriority"),
        ("DKT-GE-MIB", "geLAN4PortIPQoSPriority"),
        ("DKT-GE-MIB", "geLAN4PortQoSPortMapRule"),
        ("DKT-GE-MIB", "geLAN4PortVIDNRLEnable"),
        ("DKT-GE-MIB", "geLAN4PortDisablePIRL2Bucket"),
        ("DKT-GE-MIB", "geLAN4PortEgressRateLimitation"),
        ("DKT-GE-MIB", "geLAN4PortIngressRateLimitation"),
        ("DKT-GE-MIB", "geLAN4PortDefaultVLAN"),
        ("DKT-GE-MIB", "geLAN4PortForceDefaultVID"),
        ("DKT-GE-MIB", "geLAN4PortVLANPortMode"),
        ("DKT-GE-MIB", "geLAN4PortBlockAllUnknown"),
        ("DKT-GE-MIB", "geLAN4PortIGMPSnooping"),
        ("DKT-GE-MIB", "geLAN4PortAddUnicast"),
        ("DKT-GE-MIB", "geLAN4PortAddMulticast"),
        ("DKT-GE-MIB", "geLAN4PortMtu"),
        ("DKT-GE-MIB", "geLAN4PortArpMirroring"))
)
if mibBuilder.loadTexts:
    geModuleGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DKT-GE-MIB",
    **{"geMIB": geMIB,
       "geSwitchEngine": geSwitchEngine,
       "geATU": geATU,
       "geUnicastDelete": geUnicastDelete,
       "geMulticastDelete": geMulticastDelete,
       "geIGMPSnooping": geIGMPSnooping,
       "geVTU": geVTU,
       "geVLANCreate": geVLANCreate,
       "geVLANDelete": geVLANDelete,
       "geClearVTU": geClearVTU,
       "geDumpPIRLBuckets": geDumpPIRLBuckets,
       "geVLANProviderMode": geVLANProviderMode,
       "gePorts": gePorts,
       "geCPUPort": geCPUPort,
       "geCPUPortAutoNegotiation": geCPUPortAutoNegotiation,
       "geCPUPortSpeedMode": geCPUPortSpeedMode,
       "geCPUPortLinkStatus": geCPUPortLinkStatus,
       "geCPUPortFlowControl": geCPUPortFlowControl,
       "geCPUPortIEEEQoSPriority": geCPUPortIEEEQoSPriority,
       "geCPUPortIPQoSPriority": geCPUPortIPQoSPriority,
       "geCPUPortQoSPortMapRule": geCPUPortQoSPortMapRule,
       "geCPUPortVIDNRLEnable": geCPUPortVIDNRLEnable,
       "geCPUPortDisablePIRL2Bucket": geCPUPortDisablePIRL2Bucket,
       "geCPUPortEgressRateLimitation": geCPUPortEgressRateLimitation,
       "geCPUPortIngressRateLimitation": geCPUPortIngressRateLimitation,
       "geCPUPortDefaultVLAN": geCPUPortDefaultVLAN,
       "geCPUPortForceDefaultVID": geCPUPortForceDefaultVID,
       "geCPUPortVLANPortMode": geCPUPortVLANPortMode,
       "geCPUPortBlockAllUnknown": geCPUPortBlockAllUnknown,
       "geCPUPortIGMPSnooping": geCPUPortIGMPSnooping,
       "geCPUPortAddUnicast": geCPUPortAddUnicast,
       "geCPUPortAddMulticast": geCPUPortAddMulticast,
       "geCPUPortMtu": geCPUPortMtu,
       "geWANPort": geWANPort,
       "geWANPortAutoNegotiation": geWANPortAutoNegotiation,
       "geWANPortSpeedMode": geWANPortSpeedMode,
       "geWANPortLinkStatus": geWANPortLinkStatus,
       "geWANPortFlowControl": geWANPortFlowControl,
       "geWANPortIEEEQoSPriority": geWANPortIEEEQoSPriority,
       "geWANPortIPQoSPriority": geWANPortIPQoSPriority,
       "geWANPortQoSPortMapRule": geWANPortQoSPortMapRule,
       "geWANPortVIDNRLEnable": geWANPortVIDNRLEnable,
       "geWANPortDisablePIRL2Bucket": geWANPortDisablePIRL2Bucket,
       "geWANPortEgressRateLimitation": geWANPortEgressRateLimitation,
       "geWANPortIngressRateLimitation": geWANPortIngressRateLimitation,
       "geWANPortDefaultVLAN": geWANPortDefaultVLAN,
       "geWANPortForceDefaultVID": geWANPortForceDefaultVID,
       "geWANPortVLANPortMode": geWANPortVLANPortMode,
       "geWANPortBlockAllUnknown": geWANPortBlockAllUnknown,
       "geWANPortIGMPSnooping": geWANPortIGMPSnooping,
       "geWANPortAddUnicast": geWANPortAddUnicast,
       "geWANPortAddMulticast": geWANPortAddMulticast,
       "geWANPortMtu": geWANPortMtu,
       "geWANPortArpMirroring": geWANPortArpMirroring,
       "geLAN1Port": geLAN1Port,
       "geLAN1PortAutoNegotiation": geLAN1PortAutoNegotiation,
       "geLAN1PortSpeedMode": geLAN1PortSpeedMode,
       "geLAN1PortLinkStatus": geLAN1PortLinkStatus,
       "geLAN1PortFlowControl": geLAN1PortFlowControl,
       "geLAN1PortIEEEQoSPriority": geLAN1PortIEEEQoSPriority,
       "geLAN1PortIPQoSPriority": geLAN1PortIPQoSPriority,
       "geLAN1PortQoSPortMapRule": geLAN1PortQoSPortMapRule,
       "geLAN1PortVIDNRLEnable": geLAN1PortVIDNRLEnable,
       "geLAN1PortDisablePIRL2Bucket": geLAN1PortDisablePIRL2Bucket,
       "geLAN1PortEgressRateLimitation": geLAN1PortEgressRateLimitation,
       "geLAN1PortIngressRateLimitation": geLAN1PortIngressRateLimitation,
       "geLAN1PortDefaultVLAN": geLAN1PortDefaultVLAN,
       "geLAN1PortForceDefaultVID": geLAN1PortForceDefaultVID,
       "geLAN1PortVLANPortMode": geLAN1PortVLANPortMode,
       "geLAN1PortBlockAllUnknown": geLAN1PortBlockAllUnknown,
       "geLAN1PortIGMPSnooping": geLAN1PortIGMPSnooping,
       "geLAN1PortAddUnicast": geLAN1PortAddUnicast,
       "geLAN1PortAddMulticast": geLAN1PortAddMulticast,
       "geLAN1PortMtu": geLAN1PortMtu,
       "geLAN1PortArpMirroring": geLAN1PortArpMirroring,
       "geLAN2Port": geLAN2Port,
       "geLAN2PortAutoNegotiation": geLAN2PortAutoNegotiation,
       "geLAN2PortSpeedMode": geLAN2PortSpeedMode,
       "geLAN2PortLinkStatus": geLAN2PortLinkStatus,
       "geLAN2PortFlowControl": geLAN2PortFlowControl,
       "geLAN2PortIEEEQoSPriority": geLAN2PortIEEEQoSPriority,
       "geLAN2PortIPQoSPriority": geLAN2PortIPQoSPriority,
       "geLAN2PortQoSPortMapRule": geLAN2PortQoSPortMapRule,
       "geLAN2PortVIDNRLEnable": geLAN2PortVIDNRLEnable,
       "geLAN2PortDisablePIRL2Bucket": geLAN2PortDisablePIRL2Bucket,
       "geLAN2PortEgressRateLimitation": geLAN2PortEgressRateLimitation,
       "geLAN2PortIngressRateLimitation": geLAN2PortIngressRateLimitation,
       "geLAN2PortDefaultVLAN": geLAN2PortDefaultVLAN,
       "geLAN2PortForceDefaultVID": geLAN2PortForceDefaultVID,
       "geLAN2PortVLANPortMode": geLAN2PortVLANPortMode,
       "geLAN2PortBlockAllUnknown": geLAN2PortBlockAllUnknown,
       "geLAN2PortIGMPSnooping": geLAN2PortIGMPSnooping,
       "geLAN2PortAddUnicast": geLAN2PortAddUnicast,
       "geLAN2PortAddMulticast": geLAN2PortAddMulticast,
       "geLAN2PortMtu": geLAN2PortMtu,
       "geLAN2PortArpMirroring": geLAN2PortArpMirroring,
       "geLAN3Port": geLAN3Port,
       "geLAN3PortAutoNegotiation": geLAN3PortAutoNegotiation,
       "geLAN3PortSpeedMode": geLAN3PortSpeedMode,
       "geLAN3PortLinkStatus": geLAN3PortLinkStatus,
       "geLAN3PortFlowControl": geLAN3PortFlowControl,
       "geLAN3PortIEEEQoSPriority": geLAN3PortIEEEQoSPriority,
       "geLAN3PortIPQoSPriority": geLAN3PortIPQoSPriority,
       "geLAN3PortQoSPortMapRule": geLAN3PortQoSPortMapRule,
       "geLAN3PortVIDNRLEnable": geLAN3PortVIDNRLEnable,
       "geLAN3PortDisablePIRL2Bucket": geLAN3PortDisablePIRL2Bucket,
       "geLAN3PortEgressRateLimitation": geLAN3PortEgressRateLimitation,
       "geLAN3PortIngressRateLimitation": geLAN3PortIngressRateLimitation,
       "geLAN3PortDefaultVLAN": geLAN3PortDefaultVLAN,
       "geLAN3PortForceDefaultVID": geLAN3PortForceDefaultVID,
       "geLAN3PortVLANPortMode": geLAN3PortVLANPortMode,
       "geLAN3PortBlockAllUnknown": geLAN3PortBlockAllUnknown,
       "geLAN3PortIGMPSnooping": geLAN3PortIGMPSnooping,
       "geLAN3PortAddUnicast": geLAN3PortAddUnicast,
       "geLAN3PortAddMulticast": geLAN3PortAddMulticast,
       "geLAN3PortMtu": geLAN3PortMtu,
       "geLAN3PortArpMirroring": geLAN3PortArpMirroring,
       "geLAN4Port": geLAN4Port,
       "geLAN4PortAutoNegotiation": geLAN4PortAutoNegotiation,
       "geLAN4PortSpeedMode": geLAN4PortSpeedMode,
       "geLAN4PortLinkStatus": geLAN4PortLinkStatus,
       "geLAN4PortFlowControl": geLAN4PortFlowControl,
       "geLAN4PortIEEEQoSPriority": geLAN4PortIEEEQoSPriority,
       "geLAN4PortIPQoSPriority": geLAN4PortIPQoSPriority,
       "geLAN4PortQoSPortMapRule": geLAN4PortQoSPortMapRule,
       "geLAN4PortVIDNRLEnable": geLAN4PortVIDNRLEnable,
       "geLAN4PortDisablePIRL2Bucket": geLAN4PortDisablePIRL2Bucket,
       "geLAN4PortEgressRateLimitation": geLAN4PortEgressRateLimitation,
       "geLAN4PortIngressRateLimitation": geLAN4PortIngressRateLimitation,
       "geLAN4PortDefaultVLAN": geLAN4PortDefaultVLAN,
       "geLAN4PortForceDefaultVID": geLAN4PortForceDefaultVID,
       "geLAN4PortVLANPortMode": geLAN4PortVLANPortMode,
       "geLAN4PortBlockAllUnknown": geLAN4PortBlockAllUnknown,
       "geLAN4PortIGMPSnooping": geLAN4PortIGMPSnooping,
       "geLAN4PortAddUnicast": geLAN4PortAddUnicast,
       "geLAN4PortAddMulticast": geLAN4PortAddMulticast,
       "geLAN4PortMtu": geLAN4PortMtu,
       "geLAN4PortArpMirroring": geLAN4PortArpMirroring,
       "geModuleGroup": geModuleGroup}
)
