# SNMP MIB module (TRELLIX-SENSOR-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\trellix\TRELLIX-SENSOR-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:49 2025
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

(ivProducts,) = mibBuilder.importSymbols(
    "TRELLIX-INTRUVERT-SMI",
    "ivProducts")


# MODULE-IDENTITY

ivSensor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1)
)
if mibBuilder.loadTexts:
    ivSensor.setRevisions(
        ("2007-07-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IvIndex_ObjectIdentity = ObjectIdentity
ivIndex = _IvIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1)
)


class _SlotIndex_Type(Integer32):
    """Custom type slotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SlotIndex_Type.__name__ = "Integer32"
_SlotIndex_Object = MibScalar
slotIndex = _SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 1),
    _SlotIndex_Type()
)
slotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIndex.setStatus("current")


class _ProcessorIndex_Type(Integer32):
    """Custom type processorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ProcessorIndex_Type.__name__ = "Integer32"
_ProcessorIndex_Object = MibScalar
processorIndex = _ProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 2),
    _ProcessorIndex_Type()
)
processorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorIndex.setStatus("current")


class _NpIndex_Type(Integer32):
    """Custom type npIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NpIndex_Type.__name__ = "Integer32"
_NpIndex_Object = MibScalar
npIndex = _NpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 3),
    _NpIndex_Type()
)
npIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIndex.setStatus("current")


class _MgmtPortIndex_Type(Integer32):
    """Custom type mgmtPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MgmtPortIndex_Type.__name__ = "Integer32"
_MgmtPortIndex_Object = MibScalar
mgmtPortIndex = _MgmtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 4),
    _MgmtPortIndex_Type()
)
mgmtPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtPortIndex.setStatus("current")


class _IntfPortIndex_Type(Integer32):
    """Custom type intfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IntfPortIndex_Type.__name__ = "Integer32"
_IntfPortIndex_Object = MibScalar
intfPortIndex = _IntfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 5),
    _IntfPortIndex_Type()
)
intfPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPortIndex.setStatus("current")


class _RespPortIndex_Type(Integer32):
    """Custom type respPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_RespPortIndex_Type.__name__ = "Integer32"
_RespPortIndex_Object = MibScalar
respPortIndex = _RespPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 6),
    _RespPortIndex_Type()
)
respPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respPortIndex.setStatus("current")


class _BundleIndex_Type(Integer32):
    """Custom type bundleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_BundleIndex_Type.__name__ = "Integer32"
_BundleIndex_Object = MibScalar
bundleIndex = _BundleIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 7),
    _BundleIndex_Type()
)
bundleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleIndex.setStatus("current")


class _QedIndex_Type(Integer32):
    """Custom type qedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_QedIndex_Type.__name__ = "Integer32"
_QedIndex_Object = MibScalar
qedIndex = _QedIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 8),
    _QedIndex_Type()
)
qedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qedIndex.setStatus("current")


class _SibyteIndex_Type(Integer32):
    """Custom type sibyteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SibyteIndex_Type.__name__ = "Integer32"
_SibyteIndex_Object = MibScalar
sibyteIndex = _SibyteIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 9),
    _SibyteIndex_Type()
)
sibyteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sibyteIndex.setStatus("current")


class _RateLimitQueueIndex_Type(Integer32):
    """Custom type rateLimitQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RateLimitQueueIndex_Type.__name__ = "Integer32"
_RateLimitQueueIndex_Object = MibScalar
rateLimitQueueIndex = _RateLimitQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 10),
    _RateLimitQueueIndex_Type()
)
rateLimitQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitQueueIndex.setStatus("current")


class _IntfPhysicalPortIndex_Type(Integer32):
    """Custom type intfPhysicalPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IntfPhysicalPortIndex_Type.__name__ = "Integer32"
_IntfPhysicalPortIndex_Object = MibScalar
intfPhysicalPortIndex = _IntfPhysicalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 11),
    _IntfPhysicalPortIndex_Type()
)
intfPhysicalPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfPhysicalPortIndex.setStatus("current")


class _NtpServerIndex_Type(Integer32):
    """Custom type ntpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NtpServerIndex_Type.__name__ = "Integer32"
_NtpServerIndex_Object = MibScalar
ntpServerIndex = _NtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 12),
    _NtpServerIndex_Type()
)
ntpServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServerIndex.setStatus("current")


class _IntfVirtualSlotIndex_Type(Integer32):
    """Custom type intfVirtualSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IntfVirtualSlotIndex_Type.__name__ = "Integer32"
_IntfVirtualSlotIndex_Object = MibScalar
intfVirtualSlotIndex = _IntfVirtualSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 13),
    _IntfVirtualSlotIndex_Type()
)
intfVirtualSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfVirtualSlotIndex.setStatus("current")


class _IntfVirtualPortIndex_Type(Integer32):
    """Custom type intfVirtualPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IntfVirtualPortIndex_Type.__name__ = "Integer32"
_IntfVirtualPortIndex_Object = MibScalar
intfVirtualPortIndex = _IntfVirtualPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 14),
    _IntfVirtualPortIndex_Type()
)
intfVirtualPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfVirtualPortIndex.setStatus("current")


class _SslProbeIpv4Index_Type(Integer32):
    """Custom type sslProbeIpv4Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SslProbeIpv4Index_Type.__name__ = "Integer32"
_SslProbeIpv4Index_Object = MibScalar
sslProbeIpv4Index = _SslProbeIpv4Index_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 15),
    _SslProbeIpv4Index_Type()
)
sslProbeIpv4Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProbeIpv4Index.setStatus("current")


class _ProcessorNumIndex_Type(Integer32):
    """Custom type processorNumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ProcessorNumIndex_Type.__name__ = "Integer32"
_ProcessorNumIndex_Object = MibScalar
processorNumIndex = _ProcessorNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 16),
    _ProcessorNumIndex_Type()
)
processorNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorNumIndex.setStatus("current")


class _SslProbeIpv6Index_Type(Integer32):
    """Custom type sslProbeIpv6Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SslProbeIpv6Index_Type.__name__ = "Integer32"
_SslProbeIpv6Index_Object = MibScalar
sslProbeIpv6Index = _SslProbeIpv6Index_Object(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 1, 17),
    _SslProbeIpv6Index_Type()
)
sslProbeIpv6Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProbeIpv6Index.setStatus("current")
_IvSensorConfiguration_ObjectIdentity = ObjectIdentity
ivSensorConfiguration = _IvSensorConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 2)
)
_IvSensorPerformance_ObjectIdentity = ObjectIdentity
ivSensorPerformance = _IvSensorPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 3)
)
_IvSensorTraps_ObjectIdentity = ObjectIdentity
ivSensorTraps = _IvSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 4)
)
_IvFirewallConfiguration_ObjectIdentity = ObjectIdentity
ivFirewallConfiguration = _IvFirewallConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 5)
)
_IvFirewallPerformance_ObjectIdentity = ObjectIdentity
ivFirewallPerformance = _IvFirewallPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8962, 2, 1, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRELLIX-SENSOR-SMI",
    **{"ivSensor": ivSensor,
       "ivIndex": ivIndex,
       "slotIndex": slotIndex,
       "processorIndex": processorIndex,
       "npIndex": npIndex,
       "mgmtPortIndex": mgmtPortIndex,
       "intfPortIndex": intfPortIndex,
       "respPortIndex": respPortIndex,
       "bundleIndex": bundleIndex,
       "qedIndex": qedIndex,
       "sibyteIndex": sibyteIndex,
       "rateLimitQueueIndex": rateLimitQueueIndex,
       "intfPhysicalPortIndex": intfPhysicalPortIndex,
       "ntpServerIndex": ntpServerIndex,
       "intfVirtualSlotIndex": intfVirtualSlotIndex,
       "intfVirtualPortIndex": intfVirtualPortIndex,
       "sslProbeIpv4Index": sslProbeIpv4Index,
       "processorNumIndex": processorNumIndex,
       "sslProbeIpv6Index": sslProbeIpv6Index,
       "ivSensorConfiguration": ivSensorConfiguration,
       "ivSensorPerformance": ivSensorPerformance,
       "ivSensorTraps": ivSensorTraps,
       "ivFirewallConfiguration": ivFirewallConfiguration,
       "ivFirewallPerformance": ivFirewallPerformance}
)
