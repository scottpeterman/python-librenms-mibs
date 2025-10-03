# SNMP MIB module (TN-CES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-CES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:47 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnCesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60)
)
if mibBuilder.loadTexts:
    tnCesMIB.setRevisions(
        ("2015-11-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnCesNotifications_ObjectIdentity = ObjectIdentity
tnCesNotifications = _TnCesNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 0)
)
_TnCesEventDetails_Type = DisplayString
_TnCesEventDetails_Object = MibScalar
tnCesEventDetails = _TnCesEventDetails_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 0, 1),
    _TnCesEventDetails_Type()
)
tnCesEventDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesEventDetails.setStatus("current")


class _TnCesEventPriority_Type(Unsigned32):
    """Custom type tnCesEventPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_TnCesEventPriority_Type.__name__ = "Unsigned32"
_TnCesEventPriority_Object = MibScalar
tnCesEventPriority = _TnCesEventPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 0, 2),
    _TnCesEventPriority_Type()
)
tnCesEventPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesEventPriority.setStatus("current")
_TnCesEventId_ObjectIdentity = ObjectIdentity
tnCesEventId = _TnCesEventId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 0, 3)
)
_TnCesEventIdGeneral_ObjectIdentity = ObjectIdentity
tnCesEventIdGeneral = _TnCesEventIdGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 0, 3, 0)
)
_TnCesObjects_ObjectIdentity = ObjectIdentity
tnCesObjects = _TnCesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1)
)
_TnCesProtocol_ObjectIdentity = ObjectIdentity
tnCesProtocol = _TnCesProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 1)
)


class _TnCesProtocolType_Type(Integer32):
    """Custom type tnCesProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipUdpRtp", 0),
          ("ip", 1),
          ("mpls", 2),
          ("ethernet", 3))
    )


_TnCesProtocolType_Type.__name__ = "Integer32"
_TnCesProtocolType_Object = MibScalar
tnCesProtocolType = _TnCesProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 1, 1),
    _TnCesProtocolType_Type()
)
tnCesProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProtocolType.setStatus("current")
_TnCesProtocolUnderrunFixed_Type = TruthValue
_TnCesProtocolUnderrunFixed_Object = MibScalar
tnCesProtocolUnderrunFixed = _TnCesProtocolUnderrunFixed_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 1, 2),
    _TnCesProtocolUnderrunFixed_Type()
)
tnCesProtocolUnderrunFixed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProtocolUnderrunFixed.setStatus("current")


class _TnCesProtocolUnderrunValue_Type(Unsigned32):
    """Custom type tnCesProtocolUnderrunValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnCesProtocolUnderrunValue_Type.__name__ = "Unsigned32"
_TnCesProtocolUnderrunValue_Object = MibScalar
tnCesProtocolUnderrunValue = _TnCesProtocolUnderrunValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 1, 3),
    _TnCesProtocolUnderrunValue_Type()
)
tnCesProtocolUnderrunValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProtocolUnderrunValue.setStatus("current")


class _TnCesProtocolUDPBasePort_Type(Unsigned32):
    """Custom type tnCesProtocolUDPBasePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65472),
    )


_TnCesProtocolUDPBasePort_Type.__name__ = "Unsigned32"
_TnCesProtocolUDPBasePort_Object = MibScalar
tnCesProtocolUDPBasePort = _TnCesProtocolUDPBasePort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 1, 4),
    _TnCesProtocolUDPBasePort_Type()
)
tnCesProtocolUDPBasePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProtocolUDPBasePort.setStatus("current")
_TnCesProtocolEnableSSRCChecking_Type = TruthValue
_TnCesProtocolEnableSSRCChecking_Object = MibScalar
tnCesProtocolEnableSSRCChecking = _TnCesProtocolEnableSSRCChecking_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 1, 5),
    _TnCesProtocolEnableSSRCChecking_Type()
)
tnCesProtocolEnableSSRCChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesProtocolEnableSSRCChecking.setStatus("current")
_TnCesClockingAlternate_ObjectIdentity = ObjectIdentity
tnCesClockingAlternate = _TnCesClockingAlternate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 2)
)
_TnCesClockingAlternateEnable_Type = TruthValue
_TnCesClockingAlternateEnable_Object = MibScalar
tnCesClockingAlternateEnable = _TnCesClockingAlternateEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 2, 1),
    _TnCesClockingAlternateEnable_Type()
)
tnCesClockingAlternateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesClockingAlternateEnable.setStatus("current")
_TnCesClockRecovery_ObjectIdentity = ObjectIdentity
tnCesClockRecovery = _TnCesClockRecovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 3)
)


class _TnCesClockRecoveryAlgorithm_Type(Integer32):
    """Custom type tnCesClockRecoveryAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 1),
          ("adaptiveEnhanced", 2),
          ("adaptiveFrequency", 3))
    )


_TnCesClockRecoveryAlgorithm_Type.__name__ = "Integer32"
_TnCesClockRecoveryAlgorithm_Object = MibScalar
tnCesClockRecoveryAlgorithm = _TnCesClockRecoveryAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 3, 1),
    _TnCesClockRecoveryAlgorithm_Type()
)
tnCesClockRecoveryAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesClockRecoveryAlgorithm.setStatus("current")


class _TnCesClockRecoveryFilter_Type(Integer32):
    """Custom type tnCesClockRecoveryFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_TnCesClockRecoveryFilter_Type.__name__ = "Integer32"
_TnCesClockRecoveryFilter_Object = MibScalar
tnCesClockRecoveryFilter = _TnCesClockRecoveryFilter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 3, 2),
    _TnCesClockRecoveryFilter_Type()
)
tnCesClockRecoveryFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesClockRecoveryFilter.setStatus("current")


class _TnCesClockRecoveryMaxDeviation_Type(Unsigned32):
    """Custom type tnCesClockRecoveryMaxDeviation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 200),
    )


_TnCesClockRecoveryMaxDeviation_Type.__name__ = "Unsigned32"
_TnCesClockRecoveryMaxDeviation_Object = MibScalar
tnCesClockRecoveryMaxDeviation = _TnCesClockRecoveryMaxDeviation_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 3, 3),
    _TnCesClockRecoveryMaxDeviation_Type()
)
tnCesClockRecoveryMaxDeviation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesClockRecoveryMaxDeviation.setStatus("current")
_TnCesEvent_ObjectIdentity = ObjectIdentity
tnCesEvent = _TnCesEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 4)
)


class _TnCesEventThreshold_Type(Unsigned32):
    """Custom type tnCesEventThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TnCesEventThreshold_Type.__name__ = "Unsigned32"
_TnCesEventThreshold_Object = MibScalar
tnCesEventThreshold = _TnCesEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 4, 1),
    _TnCesEventThreshold_Type()
)
tnCesEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesEventThreshold.setStatus("current")


class _TnCesEventReportingInterval_Type(Unsigned32):
    """Custom type tnCesEventReportingInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_TnCesEventReportingInterval_Type.__name__ = "Unsigned32"
_TnCesEventReportingInterval_Object = MibScalar
tnCesEventReportingInterval = _TnCesEventReportingInterval_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 4, 2),
    _TnCesEventReportingInterval_Type()
)
tnCesEventReportingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesEventReportingInterval.setStatus("current")


class _TnCesEventThresholdEarly_Type(Unsigned32):
    """Custom type tnCesEventThresholdEarly based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnCesEventThresholdEarly_Type.__name__ = "Unsigned32"
_TnCesEventThresholdEarly_Object = MibScalar
tnCesEventThresholdEarly = _TnCesEventThresholdEarly_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 4, 3),
    _TnCesEventThresholdEarly_Type()
)
tnCesEventThresholdEarly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesEventThresholdEarly.setStatus("current")


class _TnCesEventThresholdLate_Type(Unsigned32):
    """Custom type tnCesEventThresholdLate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnCesEventThresholdLate_Type.__name__ = "Unsigned32"
_TnCesEventThresholdLate_Object = MibScalar
tnCesEventThresholdLate = _TnCesEventThresholdLate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 4, 4),
    _TnCesEventThresholdLate_Type()
)
tnCesEventThresholdLate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesEventThresholdLate.setStatus("current")


class _TnCesEventThresholdUnderrun_Type(Unsigned32):
    """Custom type tnCesEventThresholdUnderrun based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnCesEventThresholdUnderrun_Type.__name__ = "Unsigned32"
_TnCesEventThresholdUnderrun_Object = MibScalar
tnCesEventThresholdUnderrun = _TnCesEventThresholdUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 4, 5),
    _TnCesEventThresholdUnderrun_Type()
)
tnCesEventThresholdUnderrun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesEventThresholdUnderrun.setStatus("current")


class _TnCesEventThresholdDCO_Type(Unsigned32):
    """Custom type tnCesEventThresholdDCO based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnCesEventThresholdDCO_Type.__name__ = "Unsigned32"
_TnCesEventThresholdDCO_Object = MibScalar
tnCesEventThresholdDCO = _TnCesEventThresholdDCO_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 4, 6),
    _TnCesEventThresholdDCO_Type()
)
tnCesEventThresholdDCO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesEventThresholdDCO.setStatus("current")
_TnCesProcessor_ObjectIdentity = ObjectIdentity
tnCesProcessor = _TnCesProcessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 5)
)


class _TnCesProcessorVersion_Type(DisplayString):
    """Custom type tnCesProcessorVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_TnCesProcessorVersion_Type.__name__ = "DisplayString"
_TnCesProcessorVersion_Object = MibScalar
tnCesProcessorVersion = _TnCesProcessorVersion_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 5, 1),
    _TnCesProcessorVersion_Type()
)
tnCesProcessorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesProcessorVersion.setStatus("current")
_TnCesProcessorProtocolMatch1_Type = Counter32
_TnCesProcessorProtocolMatch1_Object = MibScalar
tnCesProcessorProtocolMatch1 = _TnCesProcessorProtocolMatch1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 5, 2),
    _TnCesProcessorProtocolMatch1_Type()
)
tnCesProcessorProtocolMatch1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesProcessorProtocolMatch1.setStatus("current")
_TnCesProcessorProtocolMatch2_Type = Counter32
_TnCesProcessorProtocolMatch2_Object = MibScalar
tnCesProcessorProtocolMatch2 = _TnCesProcessorProtocolMatch2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 5, 3),
    _TnCesProcessorProtocolMatch2_Type()
)
tnCesProcessorProtocolMatch2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesProcessorProtocolMatch2.setStatus("current")
_TnCesProcessorProtocolMatch3_Type = Counter32
_TnCesProcessorProtocolMatch3_Object = MibScalar
tnCesProcessorProtocolMatch3 = _TnCesProcessorProtocolMatch3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 5, 4),
    _TnCesProcessorProtocolMatch3_Type()
)
tnCesProcessorProtocolMatch3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesProcessorProtocolMatch3.setStatus("current")
_TnCesProcessorProtocolMatch4_Type = Counter32
_TnCesProcessorProtocolMatch4_Object = MibScalar
tnCesProcessorProtocolMatch4 = _TnCesProcessorProtocolMatch4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 5, 5),
    _TnCesProcessorProtocolMatch4_Type()
)
tnCesProcessorProtocolMatch4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesProcessorProtocolMatch4.setStatus("current")
_TnCesProcessorProtocolNoMatch_Type = Counter32
_TnCesProcessorProtocolNoMatch_Object = MibScalar
tnCesProcessorProtocolNoMatch = _TnCesProcessorProtocolNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 5, 6),
    _TnCesProcessorProtocolNoMatch_Type()
)
tnCesProcessorProtocolNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesProcessorProtocolNoMatch.setStatus("current")
_TnCesProcessorClassifyFail_Type = Counter32
_TnCesProcessorClassifyFail_Object = MibScalar
tnCesProcessorClassifyFail = _TnCesProcessorClassifyFail_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 5, 7),
    _TnCesProcessorClassifyFail_Type()
)
tnCesProcessorClassifyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesProcessorClassifyFail.setStatus("current")
_TnCesProcessorVerifyFail_Type = Counter32
_TnCesProcessorVerifyFail_Object = MibScalar
tnCesProcessorVerifyFail = _TnCesProcessorVerifyFail_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 5, 8),
    _TnCesProcessorVerifyFail_Type()
)
tnCesProcessorVerifyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesProcessorVerifyFail.setStatus("current")
_TnCesProcessorIpv4ChecksumFail_Type = Counter32
_TnCesProcessorIpv4ChecksumFail_Object = MibScalar
tnCesProcessorIpv4ChecksumFail = _TnCesProcessorIpv4ChecksumFail_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 5, 9),
    _TnCesProcessorIpv4ChecksumFail_Type()
)
tnCesProcessorIpv4ChecksumFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesProcessorIpv4ChecksumFail.setStatus("current")
_TnCesProcessorUdpChecksumFail_Type = Counter32
_TnCesProcessorUdpChecksumFail_Object = MibScalar
tnCesProcessorUdpChecksumFail = _TnCesProcessorUdpChecksumFail_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 5, 10),
    _TnCesProcessorUdpChecksumFail_Type()
)
tnCesProcessorUdpChecksumFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesProcessorUdpChecksumFail.setStatus("current")
_TnCesClockStatus_ObjectIdentity = ObjectIdentity
tnCesClockStatus = _TnCesClockStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 6)
)


class _TnCesClockStatusLock_Type(Integer32):
    """Custom type tnCesClockStatusLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clockLockAutomatic", 0),
          ("clockLockNormal", 1),
          ("clockLockHoldover", 2),
          ("clockLockFreerun", 3),
          ("clockLockUnknown", 4))
    )


_TnCesClockStatusLock_Type.__name__ = "Integer32"
_TnCesClockStatusLock_Object = MibScalar
tnCesClockStatusLock = _TnCesClockStatusLock_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 6, 1),
    _TnCesClockStatusLock_Type()
)
tnCesClockStatusLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesClockStatusLock.setStatus("current")
_TnCesClockStatusSlaveMode_Type = TruthValue
_TnCesClockStatusSlaveMode_Object = MibScalar
tnCesClockStatusSlaveMode = _TnCesClockStatusSlaveMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 6, 2),
    _TnCesClockStatusSlaveMode_Type()
)
tnCesClockStatusSlaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesClockStatusSlaveMode.setStatus("current")


class _TnCesClockStatusSource_Type(DisplayString):
    """Custom type tnCesClockStatusSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnCesClockStatusSource_Type.__name__ = "DisplayString"
_TnCesClockStatusSource_Object = MibScalar
tnCesClockStatusSource = _TnCesClockStatusSource_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 6, 3),
    _TnCesClockStatusSource_Type()
)
tnCesClockStatusSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesClockStatusSource.setStatus("current")
_TnCesTemperature_ObjectIdentity = ObjectIdentity
tnCesTemperature = _TnCesTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 7)
)
_TnCesTemperatureBoardWhole_Type = Unsigned32
_TnCesTemperatureBoardWhole_Object = MibScalar
tnCesTemperatureBoardWhole = _TnCesTemperatureBoardWhole_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 7, 1),
    _TnCesTemperatureBoardWhole_Type()
)
tnCesTemperatureBoardWhole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesTemperatureBoardWhole.setStatus("current")
_TnCesTemperatureBoardFrac_Type = Unsigned32
_TnCesTemperatureBoardFrac_Object = MibScalar
tnCesTemperatureBoardFrac = _TnCesTemperatureBoardFrac_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 7, 2),
    _TnCesTemperatureBoardFrac_Type()
)
tnCesTemperatureBoardFrac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesTemperatureBoardFrac.setStatus("current")
_TnCesTemperatureProcessorWhole_Type = Unsigned32
_TnCesTemperatureProcessorWhole_Object = MibScalar
tnCesTemperatureProcessorWhole = _TnCesTemperatureProcessorWhole_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 7, 3),
    _TnCesTemperatureProcessorWhole_Type()
)
tnCesTemperatureProcessorWhole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesTemperatureProcessorWhole.setStatus("current")
_TnCesTemperatureProcessorFrac_Type = Unsigned32
_TnCesTemperatureProcessorFrac_Object = MibScalar
tnCesTemperatureProcessorFrac = _TnCesTemperatureProcessorFrac_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 7, 4),
    _TnCesTemperatureProcessorFrac_Type()
)
tnCesTemperatureProcessorFrac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesTemperatureProcessorFrac.setStatus("current")
_TnCesIP_ObjectIdentity = ObjectIdentity
tnCesIP = _TnCesIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 8)
)
_TnCesIpv4AddrType_Type = InetAddressType
_TnCesIpv4AddrType_Object = MibScalar
tnCesIpv4AddrType = _TnCesIpv4AddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 8, 1),
    _TnCesIpv4AddrType_Type()
)
tnCesIpv4AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesIpv4AddrType.setStatus("current")
_TnCesIpv4Addr_Type = InetAddress
_TnCesIpv4Addr_Object = MibScalar
tnCesIpv4Addr = _TnCesIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 8, 2),
    _TnCesIpv4Addr_Type()
)
tnCesIpv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesIpv4Addr.setStatus("current")


class _TnCesIpv4PrefixLength_Type(Unsigned32):
    """Custom type tnCesIpv4PrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TnCesIpv4PrefixLength_Type.__name__ = "Unsigned32"
_TnCesIpv4PrefixLength_Object = MibScalar
tnCesIpv4PrefixLength = _TnCesIpv4PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 8, 3),
    _TnCesIpv4PrefixLength_Type()
)
tnCesIpv4PrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesIpv4PrefixLength.setStatus("current")
_TnCesIpv6AddrType_Type = InetAddressType
_TnCesIpv6AddrType_Object = MibScalar
tnCesIpv6AddrType = _TnCesIpv6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 8, 4),
    _TnCesIpv6AddrType_Type()
)
tnCesIpv6AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesIpv6AddrType.setStatus("current")
_TnCesIpv6Addr_Type = InetAddress
_TnCesIpv6Addr_Object = MibScalar
tnCesIpv6Addr = _TnCesIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 8, 5),
    _TnCesIpv6Addr_Type()
)
tnCesIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesIpv6Addr.setStatus("current")


class _TnCesIpv6PrefixLength_Type(Unsigned32):
    """Custom type tnCesIpv6PrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TnCesIpv6PrefixLength_Type.__name__ = "Unsigned32"
_TnCesIpv6PrefixLength_Object = MibScalar
tnCesIpv6PrefixLength = _TnCesIpv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 8, 6),
    _TnCesIpv6PrefixLength_Type()
)
tnCesIpv6PrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesIpv6PrefixLength.setStatus("current")
_TnCesClockPriority_ObjectIdentity = ObjectIdentity
tnCesClockPriority = _TnCesClockPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 9)
)
_TnCesMiscClockPriorityTable_Object = MibTable
tnCesMiscClockPriorityTable = _TnCesMiscClockPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tnCesMiscClockPriorityTable.setStatus("current")
_TnCesMiscClockPriorityEntry_Object = MibTableRow
tnCesMiscClockPriorityEntry = _TnCesMiscClockPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 9, 1, 1)
)
tnCesMiscClockPriorityEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesMiscClockPriorityItem"),
)
if mibBuilder.loadTexts:
    tnCesMiscClockPriorityEntry.setStatus("current")


class _TnCesMiscClockPriorityItem_Type(Integer32):
    """Custom type tnCesMiscClockPriorityItem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("internal", 1)
    )


_TnCesMiscClockPriorityItem_Type.__name__ = "Integer32"
_TnCesMiscClockPriorityItem_Object = MibTableColumn
tnCesMiscClockPriorityItem = _TnCesMiscClockPriorityItem_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 9, 1, 1, 1),
    _TnCesMiscClockPriorityItem_Type()
)
tnCesMiscClockPriorityItem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesMiscClockPriorityItem.setStatus("current")


class _TnCesMiscClockPriority_Type(Unsigned32):
    """Custom type tnCesMiscClockPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_TnCesMiscClockPriority_Type.__name__ = "Unsigned32"
_TnCesMiscClockPriority_Object = MibTableColumn
tnCesMiscClockPriority = _TnCesMiscClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 9, 1, 1, 2),
    _TnCesMiscClockPriority_Type()
)
tnCesMiscClockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesMiscClockPriority.setStatus("current")
_TnCesPRIClockPriorityTable_Object = MibTable
tnCesPRIClockPriorityTable = _TnCesPRIClockPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 9, 2)
)
if mibBuilder.loadTexts:
    tnCesPRIClockPriorityTable.setStatus("current")
_TnCesPRIClockPriorityEntry_Object = MibTableRow
tnCesPRIClockPriorityEntry = _TnCesPRIClockPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 9, 2, 1)
)
tnCesPRIClockPriorityEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesPRIClockPriorityIndex"),
)
if mibBuilder.loadTexts:
    tnCesPRIClockPriorityEntry.setStatus("current")


class _TnCesPRIClockPriorityIndex_Type(Unsigned32):
    """Custom type tnCesPRIClockPriorityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TnCesPRIClockPriorityIndex_Type.__name__ = "Unsigned32"
_TnCesPRIClockPriorityIndex_Object = MibTableColumn
tnCesPRIClockPriorityIndex = _TnCesPRIClockPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 9, 2, 1, 1),
    _TnCesPRIClockPriorityIndex_Type()
)
tnCesPRIClockPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesPRIClockPriorityIndex.setStatus("current")


class _TnCesPRIClockPriority_Type(Unsigned32):
    """Custom type tnCesPRIClockPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_TnCesPRIClockPriority_Type.__name__ = "Unsigned32"
_TnCesPRIClockPriority_Object = MibTableColumn
tnCesPRIClockPriority = _TnCesPRIClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 9, 2, 1, 2),
    _TnCesPRIClockPriority_Type()
)
tnCesPRIClockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesPRIClockPriority.setStatus("current")
_TnCesLLClockPriorityTable_Object = MibTable
tnCesLLClockPriorityTable = _TnCesLLClockPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 9, 3)
)
if mibBuilder.loadTexts:
    tnCesLLClockPriorityTable.setStatus("current")
_TnCesLLClockPriorityEntry_Object = MibTableRow
tnCesLLClockPriorityEntry = _TnCesLLClockPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 9, 3, 1)
)
tnCesLLClockPriorityEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesLLClockPriorityIndex"),
)
if mibBuilder.loadTexts:
    tnCesLLClockPriorityEntry.setStatus("current")


class _TnCesLLClockPriorityIndex_Type(Unsigned32):
    """Custom type tnCesLLClockPriorityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TnCesLLClockPriorityIndex_Type.__name__ = "Unsigned32"
_TnCesLLClockPriorityIndex_Object = MibTableColumn
tnCesLLClockPriorityIndex = _TnCesLLClockPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 9, 3, 1, 1),
    _TnCesLLClockPriorityIndex_Type()
)
tnCesLLClockPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesLLClockPriorityIndex.setStatus("current")


class _TnCesLLClockPriority_Type(Unsigned32):
    """Custom type tnCesLLClockPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_TnCesLLClockPriority_Type.__name__ = "Unsigned32"
_TnCesLLClockPriority_Object = MibTableColumn
tnCesLLClockPriority = _TnCesLLClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 9, 3, 1, 2),
    _TnCesLLClockPriority_Type()
)
tnCesLLClockPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLClockPriority.setStatus("current")
_TnCesMulticastJoinTable_Object = MibTable
tnCesMulticastJoinTable = _TnCesMulticastJoinTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 10)
)
if mibBuilder.loadTexts:
    tnCesMulticastJoinTable.setStatus("current")
_TnCesMulticastJoinEntry_Object = MibTableRow
tnCesMulticastJoinEntry = _TnCesMulticastJoinEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 10, 1)
)
tnCesMulticastJoinEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesMulticastJoinIndex"),
)
if mibBuilder.loadTexts:
    tnCesMulticastJoinEntry.setStatus("current")


class _TnCesMulticastJoinIndex_Type(Unsigned32):
    """Custom type tnCesMulticastJoinIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TnCesMulticastJoinIndex_Type.__name__ = "Unsigned32"
_TnCesMulticastJoinIndex_Object = MibTableColumn
tnCesMulticastJoinIndex = _TnCesMulticastJoinIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 10, 1, 1),
    _TnCesMulticastJoinIndex_Type()
)
tnCesMulticastJoinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesMulticastJoinIndex.setStatus("current")
_TnCesMulticastJoinAction_Type = TruthValue
_TnCesMulticastJoinAction_Object = MibTableColumn
tnCesMulticastJoinAction = _TnCesMulticastJoinAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 10, 1, 2),
    _TnCesMulticastJoinAction_Type()
)
tnCesMulticastJoinAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesMulticastJoinAction.setStatus("current")
_TnCesMulticastJoinAddrType_Type = InetAddressType
_TnCesMulticastJoinAddrType_Object = MibTableColumn
tnCesMulticastJoinAddrType = _TnCesMulticastJoinAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 10, 1, 3),
    _TnCesMulticastJoinAddrType_Type()
)
tnCesMulticastJoinAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesMulticastJoinAddrType.setStatus("current")
_TnCesMulticastJoinAddr_Type = InetAddress
_TnCesMulticastJoinAddr_Object = MibTableColumn
tnCesMulticastJoinAddr = _TnCesMulticastJoinAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 10, 1, 4),
    _TnCesMulticastJoinAddr_Type()
)
tnCesMulticastJoinAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesMulticastJoinAddr.setStatus("current")
_TnCesTDMTable_Object = MibTable
tnCesTDMTable = _TnCesTDMTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11)
)
if mibBuilder.loadTexts:
    tnCesTDMTable.setStatus("current")
_TnCesTDMEntry_Object = MibTableRow
tnCesTDMEntry = _TnCesTDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1)
)
tnCesTDMEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesTDMPortNumber"),
)
if mibBuilder.loadTexts:
    tnCesTDMEntry.setStatus("current")


class _TnCesTDMPortNumber_Type(Unsigned32):
    """Custom type tnCesTDMPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TnCesTDMPortNumber_Type.__name__ = "Unsigned32"
_TnCesTDMPortNumber_Object = MibTableColumn
tnCesTDMPortNumber = _TnCesTDMPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 1),
    _TnCesTDMPortNumber_Type()
)
tnCesTDMPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesTDMPortNumber.setStatus("current")


class _TnCesTDMPresentation_Type(Integer32):
    """Custom type tnCesTDMPresentation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("te", 0),
          ("nt", 1))
    )


_TnCesTDMPresentation_Type.__name__ = "Integer32"
_TnCesTDMPresentation_Object = MibTableColumn
tnCesTDMPresentation = _TnCesTDMPresentation_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 2),
    _TnCesTDMPresentation_Type()
)
tnCesTDMPresentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMPresentation.setStatus("current")


class _TnCesTDMFraming_Type(Integer32):
    """Custom type tnCesTDMFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("full", 0),
          ("fractional", 1))
    )


_TnCesTDMFraming_Type.__name__ = "Integer32"
_TnCesTDMFraming_Object = MibTableColumn
tnCesTDMFraming = _TnCesTDMFraming_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 3),
    _TnCesTDMFraming_Type()
)
tnCesTDMFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMFraming.setStatus("current")


class _TnCesTDMMode_Type(Integer32):
    """Custom type tnCesTDMMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e1", 0),
          ("t1", 1))
    )


_TnCesTDMMode_Type.__name__ = "Integer32"
_TnCesTDMMode_Object = MibTableColumn
tnCesTDMMode = _TnCesTDMMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 4),
    _TnCesTDMMode_Type()
)
tnCesTDMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMMode.setStatus("current")
_TnCesTDMTS0Passthrough_Type = TruthValue
_TnCesTDMTS0Passthrough_Object = MibTableColumn
tnCesTDMTS0Passthrough = _TnCesTDMTS0Passthrough_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 5),
    _TnCesTDMTS0Passthrough_Type()
)
tnCesTDMTS0Passthrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMTS0Passthrough.setStatus("current")
_TnCesTDMCRC4_Type = TruthValue
_TnCesTDMCRC4_Object = MibTableColumn
tnCesTDMCRC4 = _TnCesTDMCRC4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 6),
    _TnCesTDMCRC4_Type()
)
tnCesTDMCRC4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMCRC4.setStatus("current")
_TnCesTDMShutdownCallsOnFail_Type = TruthValue
_TnCesTDMShutdownCallsOnFail_Object = MibTableColumn
tnCesTDMShutdownCallsOnFail = _TnCesTDMShutdownCallsOnFail_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 7),
    _TnCesTDMShutdownCallsOnFail_Type()
)
tnCesTDMShutdownCallsOnFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMShutdownCallsOnFail.setStatus("current")


class _TnCesTDMImpedance_Type(Integer32):
    """Custom type tnCesTDMImpedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("impedance120ohms", 0),
          ("impedance75ohms", 1))
    )


_TnCesTDMImpedance_Type.__name__ = "Integer32"
_TnCesTDMImpedance_Object = MibTableColumn
tnCesTDMImpedance = _TnCesTDMImpedance_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 8),
    _TnCesTDMImpedance_Type()
)
tnCesTDMImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMImpedance.setStatus("current")


class _TnCesTDMT1Framing_Type(Integer32):
    """Custom type tnCesTDMT1Framing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("esf", 0),
          ("d4", 1))
    )


_TnCesTDMT1Framing_Type.__name__ = "Integer32"
_TnCesTDMT1Framing_Object = MibTableColumn
tnCesTDMT1Framing = _TnCesTDMT1Framing_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 9),
    _TnCesTDMT1Framing_Type()
)
tnCesTDMT1Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMT1Framing.setStatus("current")


class _TnCesTDMT1LineCode_Type(Integer32):
    """Custom type tnCesTDMT1LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b8zs", 0),
          ("ami", 1))
    )


_TnCesTDMT1LineCode_Type.__name__ = "Integer32"
_TnCesTDMT1LineCode_Object = MibTableColumn
tnCesTDMT1LineCode = _TnCesTDMT1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 10),
    _TnCesTDMT1LineCode_Type()
)
tnCesTDMT1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMT1LineCode.setStatus("current")


class _TnCesTDMT1LoopCodeType_Type(Integer32):
    """Custom type tnCesTDMT1LoopCodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fac1", 0),
          ("fac2", 1),
          ("fac3", 2),
          ("user", 3))
    )


_TnCesTDMT1LoopCodeType_Type.__name__ = "Integer32"
_TnCesTDMT1LoopCodeType_Object = MibTableColumn
tnCesTDMT1LoopCodeType = _TnCesTDMT1LoopCodeType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 11),
    _TnCesTDMT1LoopCodeType_Type()
)
tnCesTDMT1LoopCodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMT1LoopCodeType.setStatus("current")
_TnCesTDMT1LoopCodeRxEnable_Type = TruthValue
_TnCesTDMT1LoopCodeRxEnable_Object = MibTableColumn
tnCesTDMT1LoopCodeRxEnable = _TnCesTDMT1LoopCodeRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 12),
    _TnCesTDMT1LoopCodeRxEnable_Type()
)
tnCesTDMT1LoopCodeRxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMT1LoopCodeRxEnable.setStatus("current")


class _TnCesTDMT1LoopCodeUserUp_Type(Unsigned32):
    """Custom type tnCesTDMT1LoopCodeUserUp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnCesTDMT1LoopCodeUserUp_Type.__name__ = "Unsigned32"
_TnCesTDMT1LoopCodeUserUp_Object = MibTableColumn
tnCesTDMT1LoopCodeUserUp = _TnCesTDMT1LoopCodeUserUp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 13),
    _TnCesTDMT1LoopCodeUserUp_Type()
)
tnCesTDMT1LoopCodeUserUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMT1LoopCodeUserUp.setStatus("current")


class _TnCesTDMT1LoopCodeUserDown_Type(Unsigned32):
    """Custom type tnCesTDMT1LoopCodeUserDown based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnCesTDMT1LoopCodeUserDown_Type.__name__ = "Unsigned32"
_TnCesTDMT1LoopCodeUserDown_Object = MibTableColumn
tnCesTDMT1LoopCodeUserDown = _TnCesTDMT1LoopCodeUserDown_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 14),
    _TnCesTDMT1LoopCodeUserDown_Type()
)
tnCesTDMT1LoopCodeUserDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMT1LoopCodeUserDown.setStatus("current")


class _TnCesTDMT1LoopCodeUserLength_Type(Unsigned32):
    """Custom type tnCesTDMT1LoopCodeUserLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_TnCesTDMT1LoopCodeUserLength_Type.__name__ = "Unsigned32"
_TnCesTDMT1LoopCodeUserLength_Object = MibTableColumn
tnCesTDMT1LoopCodeUserLength = _TnCesTDMT1LoopCodeUserLength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 15),
    _TnCesTDMT1LoopCodeUserLength_Type()
)
tnCesTDMT1LoopCodeUserLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMT1LoopCodeUserLength.setStatus("current")
_TnCesTDMDTE_Type = TruthValue
_TnCesTDMDTE_Object = MibTableColumn
tnCesTDMDTE = _TnCesTDMDTE_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 11, 1, 16),
    _TnCesTDMDTE_Type()
)
tnCesTDMDTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMDTE.setStatus("current")
_TnCesLLTable_Object = MibTable
tnCesLLTable = _TnCesLLTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12)
)
if mibBuilder.loadTexts:
    tnCesLLTable.setStatus("current")
_TnCesLLEntry_Object = MibTableRow
tnCesLLEntry = _TnCesLLEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1)
)
tnCesLLEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesLLNumber"),
)
if mibBuilder.loadTexts:
    tnCesLLEntry.setStatus("current")


class _TnCesLLNumber_Type(Unsigned32):
    """Custom type tnCesLLNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnCesLLNumber_Type.__name__ = "Unsigned32"
_TnCesLLNumber_Object = MibTableColumn
tnCesLLNumber = _TnCesLLNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 1),
    _TnCesLLNumber_Type()
)
tnCesLLNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesLLNumber.setStatus("current")


class _TnCesLLname_Type(DisplayString):
    """Custom type tnCesLLname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnCesLLname_Type.__name__ = "DisplayString"
_TnCesLLname_Object = MibTableColumn
tnCesLLname = _TnCesLLname_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 2),
    _TnCesLLname_Type()
)
tnCesLLname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLname.setStatus("current")


class _TnCesLLDirection_Type(Integer32):
    """Custom type tnCesLLDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rx", 1),
          ("tx", 2),
          ("both", 3))
    )


_TnCesLLDirection_Type.__name__ = "Integer32"
_TnCesLLDirection_Object = MibTableColumn
tnCesLLDirection = _TnCesLLDirection_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 3),
    _TnCesLLDirection_Type()
)
tnCesLLDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLDirection.setStatus("current")
_TnCesLLRemoteIpAddrType_Type = InetAddressType
_TnCesLLRemoteIpAddrType_Object = MibTableColumn
tnCesLLRemoteIpAddrType = _TnCesLLRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 4),
    _TnCesLLRemoteIpAddrType_Type()
)
tnCesLLRemoteIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLRemoteIpAddrType.setStatus("current")
_TnCesLLRemoteIpAddr_Type = InetAddress
_TnCesLLRemoteIpAddr_Object = MibTableColumn
tnCesLLRemoteIpAddr = _TnCesLLRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 5),
    _TnCesLLRemoteIpAddr_Type()
)
tnCesLLRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLRemoteIpAddr.setStatus("current")
_TnCesLLSecondaryRemoteIpAddrType_Type = InetAddressType
_TnCesLLSecondaryRemoteIpAddrType_Object = MibTableColumn
tnCesLLSecondaryRemoteIpAddrType = _TnCesLLSecondaryRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 6),
    _TnCesLLSecondaryRemoteIpAddrType_Type()
)
tnCesLLSecondaryRemoteIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSecondaryRemoteIpAddrType.setStatus("current")
_TnCesLLSecondaryRemoteIpAddr_Type = InetAddress
_TnCesLLSecondaryRemoteIpAddr_Object = MibTableColumn
tnCesLLSecondaryRemoteIpAddr = _TnCesLLSecondaryRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 7),
    _TnCesLLSecondaryRemoteIpAddr_Type()
)
tnCesLLSecondaryRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSecondaryRemoteIpAddr.setStatus("current")


class _TnCesLLQosType_Type(Integer32):
    """Custom type tnCesLLQosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tos", 0),
          ("diffserv", 1))
    )


_TnCesLLQosType_Type.__name__ = "Integer32"
_TnCesLLQosType_Object = MibTableColumn
tnCesLLQosType = _TnCesLLQosType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 8),
    _TnCesLLQosType_Type()
)
tnCesLLQosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLQosType.setStatus("current")


class _TnCesLLQosTOS_Type(Unsigned32):
    """Custom type tnCesLLQosTOS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnCesLLQosTOS_Type.__name__ = "Unsigned32"
_TnCesLLQosTOS_Object = MibTableColumn
tnCesLLQosTOS = _TnCesLLQosTOS_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 9),
    _TnCesLLQosTOS_Type()
)
tnCesLLQosTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLQosTOS.setStatus("current")


class _TnCesLLQosDiffserv_Type(Unsigned32):
    """Custom type tnCesLLQosDiffserv based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TnCesLLQosDiffserv_Type.__name__ = "Unsigned32"
_TnCesLLQosDiffserv_Object = MibTableColumn
tnCesLLQosDiffserv = _TnCesLLQosDiffserv_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 10),
    _TnCesLLQosDiffserv_Type()
)
tnCesLLQosDiffserv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLQosDiffserv.setStatus("current")
_TnCesLLVlanTag_Type = TruthValue
_TnCesLLVlanTag_Object = MibTableColumn
tnCesLLVlanTag = _TnCesLLVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 11),
    _TnCesLLVlanTag_Type()
)
tnCesLLVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLVlanTag.setStatus("current")


class _TnCesLLVlanId_Type(Unsigned32):
    """Custom type tnCesLLVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_TnCesLLVlanId_Type.__name__ = "Unsigned32"
_TnCesLLVlanId_Object = MibTableColumn
tnCesLLVlanId = _TnCesLLVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 12),
    _TnCesLLVlanId_Type()
)
tnCesLLVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLVlanId.setStatus("current")


class _TnCesLLVlanPriority_Type(Unsigned32):
    """Custom type tnCesLLVlanPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnCesLLVlanPriority_Type.__name__ = "Unsigned32"
_TnCesLLVlanPriority_Object = MibTableColumn
tnCesLLVlanPriority = _TnCesLLVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 13),
    _TnCesLLVlanPriority_Type()
)
tnCesLLVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLVlanPriority.setStatus("current")


class _TnCesLLJitterBufferLength_Type(Unsigned32):
    """Custom type tnCesLLJitterBufferLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_TnCesLLJitterBufferLength_Type.__name__ = "Unsigned32"
_TnCesLLJitterBufferLength_Object = MibTableColumn
tnCesLLJitterBufferLength = _TnCesLLJitterBufferLength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 14),
    _TnCesLLJitterBufferLength_Type()
)
tnCesLLJitterBufferLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJitterBufferLength.setStatus("current")


class _TnCesLLFramesPerPacket_Type(Unsigned32):
    """Custom type tnCesLLFramesPerPacket based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnCesLLFramesPerPacket_Type.__name__ = "Unsigned32"
_TnCesLLFramesPerPacket_Object = MibTableColumn
tnCesLLFramesPerPacket = _TnCesLLFramesPerPacket_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 15),
    _TnCesLLFramesPerPacket_Type()
)
tnCesLLFramesPerPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLFramesPerPacket.setStatus("current")


class _TnCesLLRemoteLinkNumber_Type(Unsigned32):
    """Custom type tnCesLLRemoteLinkNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnCesLLRemoteLinkNumber_Type.__name__ = "Unsigned32"
_TnCesLLRemoteLinkNumber_Object = MibTableColumn
tnCesLLRemoteLinkNumber = _TnCesLLRemoteLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 12, 1, 16),
    _TnCesLLRemoteLinkNumber_Type()
)
tnCesLLRemoteLinkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLRemoteLinkNumber.setStatus("current")
_TnCesLLSchedTable_Object = MibTable
tnCesLLSchedTable = _TnCesLLSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13)
)
if mibBuilder.loadTexts:
    tnCesLLSchedTable.setStatus("current")
_TnCesLLSchedEntry_Object = MibTableRow
tnCesLLSchedEntry = _TnCesLLSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1)
)
tnCesLLSchedEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesLLSchedNumber"),
)
if mibBuilder.loadTexts:
    tnCesLLSchedEntry.setStatus("current")


class _TnCesLLSchedNumber_Type(Unsigned32):
    """Custom type tnCesLLSchedNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnCesLLSchedNumber_Type.__name__ = "Unsigned32"
_TnCesLLSchedNumber_Object = MibTableColumn
tnCesLLSchedNumber = _TnCesLLSchedNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 1),
    _TnCesLLSchedNumber_Type()
)
tnCesLLSchedNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesLLSchedNumber.setStatus("current")
_TnCesLLSchedEnable_Type = TruthValue
_TnCesLLSchedEnable_Object = MibTableColumn
tnCesLLSchedEnable = _TnCesLLSchedEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 2),
    _TnCesLLSchedEnable_Type()
)
tnCesLLSchedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedEnable.setStatus("current")


class _TnCesLLSchedStartTimeMonHours_Type(Unsigned32):
    """Custom type tnCesLLSchedStartTimeMonHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLSchedStartTimeMonHours_Type.__name__ = "Unsigned32"
_TnCesLLSchedStartTimeMonHours_Object = MibTableColumn
tnCesLLSchedStartTimeMonHours = _TnCesLLSchedStartTimeMonHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 3),
    _TnCesLLSchedStartTimeMonHours_Type()
)
tnCesLLSchedStartTimeMonHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStartTimeMonHours.setStatus("current")


class _TnCesLLSchedStartTimeMonMins_Type(Unsigned32):
    """Custom type tnCesLLSchedStartTimeMonMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLSchedStartTimeMonMins_Type.__name__ = "Unsigned32"
_TnCesLLSchedStartTimeMonMins_Object = MibTableColumn
tnCesLLSchedStartTimeMonMins = _TnCesLLSchedStartTimeMonMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 4),
    _TnCesLLSchedStartTimeMonMins_Type()
)
tnCesLLSchedStartTimeMonMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStartTimeMonMins.setStatus("current")


class _TnCesLLSchedStopTimeMonHours_Type(Unsigned32):
    """Custom type tnCesLLSchedStopTimeMonHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLSchedStopTimeMonHours_Type.__name__ = "Unsigned32"
_TnCesLLSchedStopTimeMonHours_Object = MibTableColumn
tnCesLLSchedStopTimeMonHours = _TnCesLLSchedStopTimeMonHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 5),
    _TnCesLLSchedStopTimeMonHours_Type()
)
tnCesLLSchedStopTimeMonHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStopTimeMonHours.setStatus("current")


class _TnCesLLSchedStopTimeMonMins_Type(Unsigned32):
    """Custom type tnCesLLSchedStopTimeMonMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLSchedStopTimeMonMins_Type.__name__ = "Unsigned32"
_TnCesLLSchedStopTimeMonMins_Object = MibTableColumn
tnCesLLSchedStopTimeMonMins = _TnCesLLSchedStopTimeMonMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 6),
    _TnCesLLSchedStopTimeMonMins_Type()
)
tnCesLLSchedStopTimeMonMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStopTimeMonMins.setStatus("current")


class _TnCesLLSchedStartTimeTueHours_Type(Unsigned32):
    """Custom type tnCesLLSchedStartTimeTueHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLSchedStartTimeTueHours_Type.__name__ = "Unsigned32"
_TnCesLLSchedStartTimeTueHours_Object = MibTableColumn
tnCesLLSchedStartTimeTueHours = _TnCesLLSchedStartTimeTueHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 7),
    _TnCesLLSchedStartTimeTueHours_Type()
)
tnCesLLSchedStartTimeTueHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStartTimeTueHours.setStatus("current")


class _TnCesLLSchedStartTimeTueMins_Type(Unsigned32):
    """Custom type tnCesLLSchedStartTimeTueMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLSchedStartTimeTueMins_Type.__name__ = "Unsigned32"
_TnCesLLSchedStartTimeTueMins_Object = MibTableColumn
tnCesLLSchedStartTimeTueMins = _TnCesLLSchedStartTimeTueMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 8),
    _TnCesLLSchedStartTimeTueMins_Type()
)
tnCesLLSchedStartTimeTueMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStartTimeTueMins.setStatus("current")


class _TnCesLLSchedStopTimeTueHours_Type(Unsigned32):
    """Custom type tnCesLLSchedStopTimeTueHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLSchedStopTimeTueHours_Type.__name__ = "Unsigned32"
_TnCesLLSchedStopTimeTueHours_Object = MibTableColumn
tnCesLLSchedStopTimeTueHours = _TnCesLLSchedStopTimeTueHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 9),
    _TnCesLLSchedStopTimeTueHours_Type()
)
tnCesLLSchedStopTimeTueHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStopTimeTueHours.setStatus("current")


class _TnCesLLSchedStopTimeTueMins_Type(Unsigned32):
    """Custom type tnCesLLSchedStopTimeTueMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLSchedStopTimeTueMins_Type.__name__ = "Unsigned32"
_TnCesLLSchedStopTimeTueMins_Object = MibTableColumn
tnCesLLSchedStopTimeTueMins = _TnCesLLSchedStopTimeTueMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 10),
    _TnCesLLSchedStopTimeTueMins_Type()
)
tnCesLLSchedStopTimeTueMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStopTimeTueMins.setStatus("current")


class _TnCesLLSchedStartTimeWedHours_Type(Unsigned32):
    """Custom type tnCesLLSchedStartTimeWedHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLSchedStartTimeWedHours_Type.__name__ = "Unsigned32"
_TnCesLLSchedStartTimeWedHours_Object = MibTableColumn
tnCesLLSchedStartTimeWedHours = _TnCesLLSchedStartTimeWedHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 11),
    _TnCesLLSchedStartTimeWedHours_Type()
)
tnCesLLSchedStartTimeWedHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStartTimeWedHours.setStatus("current")


class _TnCesLLSchedStartTimeWedMins_Type(Unsigned32):
    """Custom type tnCesLLSchedStartTimeWedMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLSchedStartTimeWedMins_Type.__name__ = "Unsigned32"
_TnCesLLSchedStartTimeWedMins_Object = MibTableColumn
tnCesLLSchedStartTimeWedMins = _TnCesLLSchedStartTimeWedMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 12),
    _TnCesLLSchedStartTimeWedMins_Type()
)
tnCesLLSchedStartTimeWedMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStartTimeWedMins.setStatus("current")


class _TnCesLLSchedStopTimeWedHours_Type(Unsigned32):
    """Custom type tnCesLLSchedStopTimeWedHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLSchedStopTimeWedHours_Type.__name__ = "Unsigned32"
_TnCesLLSchedStopTimeWedHours_Object = MibTableColumn
tnCesLLSchedStopTimeWedHours = _TnCesLLSchedStopTimeWedHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 13),
    _TnCesLLSchedStopTimeWedHours_Type()
)
tnCesLLSchedStopTimeWedHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStopTimeWedHours.setStatus("current")


class _TnCesLLSchedStopTimeWedMins_Type(Unsigned32):
    """Custom type tnCesLLSchedStopTimeWedMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLSchedStopTimeWedMins_Type.__name__ = "Unsigned32"
_TnCesLLSchedStopTimeWedMins_Object = MibTableColumn
tnCesLLSchedStopTimeWedMins = _TnCesLLSchedStopTimeWedMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 14),
    _TnCesLLSchedStopTimeWedMins_Type()
)
tnCesLLSchedStopTimeWedMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStopTimeWedMins.setStatus("current")


class _TnCesLLSchedStartTimeThuHours_Type(Unsigned32):
    """Custom type tnCesLLSchedStartTimeThuHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLSchedStartTimeThuHours_Type.__name__ = "Unsigned32"
_TnCesLLSchedStartTimeThuHours_Object = MibTableColumn
tnCesLLSchedStartTimeThuHours = _TnCesLLSchedStartTimeThuHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 15),
    _TnCesLLSchedStartTimeThuHours_Type()
)
tnCesLLSchedStartTimeThuHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStartTimeThuHours.setStatus("current")


class _TnCesLLSchedStartTimeThuMins_Type(Unsigned32):
    """Custom type tnCesLLSchedStartTimeThuMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLSchedStartTimeThuMins_Type.__name__ = "Unsigned32"
_TnCesLLSchedStartTimeThuMins_Object = MibTableColumn
tnCesLLSchedStartTimeThuMins = _TnCesLLSchedStartTimeThuMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 16),
    _TnCesLLSchedStartTimeThuMins_Type()
)
tnCesLLSchedStartTimeThuMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStartTimeThuMins.setStatus("current")


class _TnCesLLSchedStopTimeThuHours_Type(Unsigned32):
    """Custom type tnCesLLSchedStopTimeThuHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLSchedStopTimeThuHours_Type.__name__ = "Unsigned32"
_TnCesLLSchedStopTimeThuHours_Object = MibTableColumn
tnCesLLSchedStopTimeThuHours = _TnCesLLSchedStopTimeThuHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 17),
    _TnCesLLSchedStopTimeThuHours_Type()
)
tnCesLLSchedStopTimeThuHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStopTimeThuHours.setStatus("current")


class _TnCesLLSchedStopTimeThuMins_Type(Unsigned32):
    """Custom type tnCesLLSchedStopTimeThuMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLSchedStopTimeThuMins_Type.__name__ = "Unsigned32"
_TnCesLLSchedStopTimeThuMins_Object = MibTableColumn
tnCesLLSchedStopTimeThuMins = _TnCesLLSchedStopTimeThuMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 18),
    _TnCesLLSchedStopTimeThuMins_Type()
)
tnCesLLSchedStopTimeThuMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStopTimeThuMins.setStatus("current")


class _TnCesLLSchedStartTimeFriHours_Type(Unsigned32):
    """Custom type tnCesLLSchedStartTimeFriHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLSchedStartTimeFriHours_Type.__name__ = "Unsigned32"
_TnCesLLSchedStartTimeFriHours_Object = MibTableColumn
tnCesLLSchedStartTimeFriHours = _TnCesLLSchedStartTimeFriHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 19),
    _TnCesLLSchedStartTimeFriHours_Type()
)
tnCesLLSchedStartTimeFriHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStartTimeFriHours.setStatus("current")


class _TnCesLLSchedStartTimeFriMins_Type(Unsigned32):
    """Custom type tnCesLLSchedStartTimeFriMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLSchedStartTimeFriMins_Type.__name__ = "Unsigned32"
_TnCesLLSchedStartTimeFriMins_Object = MibTableColumn
tnCesLLSchedStartTimeFriMins = _TnCesLLSchedStartTimeFriMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 20),
    _TnCesLLSchedStartTimeFriMins_Type()
)
tnCesLLSchedStartTimeFriMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStartTimeFriMins.setStatus("current")


class _TnCesLLSchedStopTimeFriHours_Type(Unsigned32):
    """Custom type tnCesLLSchedStopTimeFriHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLSchedStopTimeFriHours_Type.__name__ = "Unsigned32"
_TnCesLLSchedStopTimeFriHours_Object = MibTableColumn
tnCesLLSchedStopTimeFriHours = _TnCesLLSchedStopTimeFriHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 21),
    _TnCesLLSchedStopTimeFriHours_Type()
)
tnCesLLSchedStopTimeFriHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStopTimeFriHours.setStatus("current")


class _TnCesLLSchedStopTimeFriMins_Type(Unsigned32):
    """Custom type tnCesLLSchedStopTimeFriMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLSchedStopTimeFriMins_Type.__name__ = "Unsigned32"
_TnCesLLSchedStopTimeFriMins_Object = MibTableColumn
tnCesLLSchedStopTimeFriMins = _TnCesLLSchedStopTimeFriMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 22),
    _TnCesLLSchedStopTimeFriMins_Type()
)
tnCesLLSchedStopTimeFriMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStopTimeFriMins.setStatus("current")


class _TnCesLLSchedStartTimeSatHours_Type(Unsigned32):
    """Custom type tnCesLLSchedStartTimeSatHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLSchedStartTimeSatHours_Type.__name__ = "Unsigned32"
_TnCesLLSchedStartTimeSatHours_Object = MibTableColumn
tnCesLLSchedStartTimeSatHours = _TnCesLLSchedStartTimeSatHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 23),
    _TnCesLLSchedStartTimeSatHours_Type()
)
tnCesLLSchedStartTimeSatHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStartTimeSatHours.setStatus("current")


class _TnCesLLSchedStartTimeSatMins_Type(Unsigned32):
    """Custom type tnCesLLSchedStartTimeSatMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLSchedStartTimeSatMins_Type.__name__ = "Unsigned32"
_TnCesLLSchedStartTimeSatMins_Object = MibTableColumn
tnCesLLSchedStartTimeSatMins = _TnCesLLSchedStartTimeSatMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 24),
    _TnCesLLSchedStartTimeSatMins_Type()
)
tnCesLLSchedStartTimeSatMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStartTimeSatMins.setStatus("current")


class _TnCesLLSchedStopTimeSatHours_Type(Unsigned32):
    """Custom type tnCesLLSchedStopTimeSatHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLSchedStopTimeSatHours_Type.__name__ = "Unsigned32"
_TnCesLLSchedStopTimeSatHours_Object = MibTableColumn
tnCesLLSchedStopTimeSatHours = _TnCesLLSchedStopTimeSatHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 25),
    _TnCesLLSchedStopTimeSatHours_Type()
)
tnCesLLSchedStopTimeSatHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStopTimeSatHours.setStatus("current")


class _TnCesLLSchedStopTimeSatMins_Type(Unsigned32):
    """Custom type tnCesLLSchedStopTimeSatMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLSchedStopTimeSatMins_Type.__name__ = "Unsigned32"
_TnCesLLSchedStopTimeSatMins_Object = MibTableColumn
tnCesLLSchedStopTimeSatMins = _TnCesLLSchedStopTimeSatMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 26),
    _TnCesLLSchedStopTimeSatMins_Type()
)
tnCesLLSchedStopTimeSatMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStopTimeSatMins.setStatus("current")


class _TnCesLLSchedStartTimeSunHours_Type(Unsigned32):
    """Custom type tnCesLLSchedStartTimeSunHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLSchedStartTimeSunHours_Type.__name__ = "Unsigned32"
_TnCesLLSchedStartTimeSunHours_Object = MibTableColumn
tnCesLLSchedStartTimeSunHours = _TnCesLLSchedStartTimeSunHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 27),
    _TnCesLLSchedStartTimeSunHours_Type()
)
tnCesLLSchedStartTimeSunHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStartTimeSunHours.setStatus("current")


class _TnCesLLSchedStartTimeSunMins_Type(Unsigned32):
    """Custom type tnCesLLSchedStartTimeSunMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLSchedStartTimeSunMins_Type.__name__ = "Unsigned32"
_TnCesLLSchedStartTimeSunMins_Object = MibTableColumn
tnCesLLSchedStartTimeSunMins = _TnCesLLSchedStartTimeSunMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 28),
    _TnCesLLSchedStartTimeSunMins_Type()
)
tnCesLLSchedStartTimeSunMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStartTimeSunMins.setStatus("current")


class _TnCesLLSchedStopTimeSunHours_Type(Unsigned32):
    """Custom type tnCesLLSchedStopTimeSunHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLSchedStopTimeSunHours_Type.__name__ = "Unsigned32"
_TnCesLLSchedStopTimeSunHours_Object = MibTableColumn
tnCesLLSchedStopTimeSunHours = _TnCesLLSchedStopTimeSunHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 29),
    _TnCesLLSchedStopTimeSunHours_Type()
)
tnCesLLSchedStopTimeSunHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStopTimeSunHours.setStatus("current")


class _TnCesLLSchedStopTimeSunMins_Type(Unsigned32):
    """Custom type tnCesLLSchedStopTimeSunMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLSchedStopTimeSunMins_Type.__name__ = "Unsigned32"
_TnCesLLSchedStopTimeSunMins_Object = MibTableColumn
tnCesLLSchedStopTimeSunMins = _TnCesLLSchedStopTimeSunMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 13, 1, 30),
    _TnCesLLSchedStopTimeSunMins_Type()
)
tnCesLLSchedStopTimeSunMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLSchedStopTimeSunMins.setStatus("current")
_TnCesLLJATable_Object = MibTable
tnCesLLJATable = _TnCesLLJATable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14)
)
if mibBuilder.loadTexts:
    tnCesLLJATable.setStatus("current")
_TnCesLLJAEntry_Object = MibTableRow
tnCesLLJAEntry = _TnCesLLJAEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1)
)
tnCesLLJAEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesLLJANumber"),
)
if mibBuilder.loadTexts:
    tnCesLLJAEntry.setStatus("current")


class _TnCesLLJANumber_Type(Unsigned32):
    """Custom type tnCesLLJANumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnCesLLJANumber_Type.__name__ = "Unsigned32"
_TnCesLLJANumber_Object = MibTableColumn
tnCesLLJANumber = _TnCesLLJANumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 1),
    _TnCesLLJANumber_Type()
)
tnCesLLJANumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesLLJANumber.setStatus("current")


class _TnCesLLJitterAdjustmentMode_Type(Integer32):
    """Custom type tnCesLLJitterAdjustmentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("always", 1),
          ("schedule", 2),
          ("once", 3))
    )


_TnCesLLJitterAdjustmentMode_Type.__name__ = "Integer32"
_TnCesLLJitterAdjustmentMode_Object = MibTableColumn
tnCesLLJitterAdjustmentMode = _TnCesLLJitterAdjustmentMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 2),
    _TnCesLLJitterAdjustmentMode_Type()
)
tnCesLLJitterAdjustmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJitterAdjustmentMode.setStatus("current")


class _TnCesLLJitterAdjustmentAfter_Type(Unsigned32):
    """Custom type tnCesLLJitterAdjustmentAfter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 999),
    )


_TnCesLLJitterAdjustmentAfter_Type.__name__ = "Unsigned32"
_TnCesLLJitterAdjustmentAfter_Object = MibTableColumn
tnCesLLJitterAdjustmentAfter = _TnCesLLJitterAdjustmentAfter_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 3),
    _TnCesLLJitterAdjustmentAfter_Type()
)
tnCesLLJitterAdjustmentAfter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJitterAdjustmentAfter.setStatus("current")


class _TnCesLLJASchedStartTimeMonHours_Type(Unsigned32):
    """Custom type tnCesLLJASchedStartTimeMonHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLJASchedStartTimeMonHours_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStartTimeMonHours_Object = MibTableColumn
tnCesLLJASchedStartTimeMonHours = _TnCesLLJASchedStartTimeMonHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 4),
    _TnCesLLJASchedStartTimeMonHours_Type()
)
tnCesLLJASchedStartTimeMonHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStartTimeMonHours.setStatus("current")


class _TnCesLLJASchedStartTimeMonMins_Type(Unsigned32):
    """Custom type tnCesLLJASchedStartTimeMonMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLJASchedStartTimeMonMins_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStartTimeMonMins_Object = MibTableColumn
tnCesLLJASchedStartTimeMonMins = _TnCesLLJASchedStartTimeMonMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 5),
    _TnCesLLJASchedStartTimeMonMins_Type()
)
tnCesLLJASchedStartTimeMonMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStartTimeMonMins.setStatus("current")


class _TnCesLLJASchedStopTimeMonHours_Type(Unsigned32):
    """Custom type tnCesLLJASchedStopTimeMonHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLJASchedStopTimeMonHours_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStopTimeMonHours_Object = MibTableColumn
tnCesLLJASchedStopTimeMonHours = _TnCesLLJASchedStopTimeMonHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 6),
    _TnCesLLJASchedStopTimeMonHours_Type()
)
tnCesLLJASchedStopTimeMonHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStopTimeMonHours.setStatus("current")


class _TnCesLLJASchedStopTimeMonMins_Type(Unsigned32):
    """Custom type tnCesLLJASchedStopTimeMonMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLJASchedStopTimeMonMins_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStopTimeMonMins_Object = MibTableColumn
tnCesLLJASchedStopTimeMonMins = _TnCesLLJASchedStopTimeMonMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 7),
    _TnCesLLJASchedStopTimeMonMins_Type()
)
tnCesLLJASchedStopTimeMonMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStopTimeMonMins.setStatus("current")


class _TnCesLLJASchedStartTimeTueHours_Type(Unsigned32):
    """Custom type tnCesLLJASchedStartTimeTueHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLJASchedStartTimeTueHours_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStartTimeTueHours_Object = MibTableColumn
tnCesLLJASchedStartTimeTueHours = _TnCesLLJASchedStartTimeTueHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 8),
    _TnCesLLJASchedStartTimeTueHours_Type()
)
tnCesLLJASchedStartTimeTueHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStartTimeTueHours.setStatus("current")


class _TnCesLLJASchedStartTimeTueMins_Type(Unsigned32):
    """Custom type tnCesLLJASchedStartTimeTueMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLJASchedStartTimeTueMins_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStartTimeTueMins_Object = MibTableColumn
tnCesLLJASchedStartTimeTueMins = _TnCesLLJASchedStartTimeTueMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 9),
    _TnCesLLJASchedStartTimeTueMins_Type()
)
tnCesLLJASchedStartTimeTueMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStartTimeTueMins.setStatus("current")


class _TnCesLLJASchedStopTimeTueHours_Type(Unsigned32):
    """Custom type tnCesLLJASchedStopTimeTueHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLJASchedStopTimeTueHours_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStopTimeTueHours_Object = MibTableColumn
tnCesLLJASchedStopTimeTueHours = _TnCesLLJASchedStopTimeTueHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 10),
    _TnCesLLJASchedStopTimeTueHours_Type()
)
tnCesLLJASchedStopTimeTueHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStopTimeTueHours.setStatus("current")


class _TnCesLLJASchedStopTimeTueMins_Type(Unsigned32):
    """Custom type tnCesLLJASchedStopTimeTueMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLJASchedStopTimeTueMins_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStopTimeTueMins_Object = MibTableColumn
tnCesLLJASchedStopTimeTueMins = _TnCesLLJASchedStopTimeTueMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 11),
    _TnCesLLJASchedStopTimeTueMins_Type()
)
tnCesLLJASchedStopTimeTueMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStopTimeTueMins.setStatus("current")


class _TnCesLLJASchedStartTimeWedHours_Type(Unsigned32):
    """Custom type tnCesLLJASchedStartTimeWedHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLJASchedStartTimeWedHours_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStartTimeWedHours_Object = MibTableColumn
tnCesLLJASchedStartTimeWedHours = _TnCesLLJASchedStartTimeWedHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 12),
    _TnCesLLJASchedStartTimeWedHours_Type()
)
tnCesLLJASchedStartTimeWedHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStartTimeWedHours.setStatus("current")


class _TnCesLLJASchedStartTimeWedMins_Type(Unsigned32):
    """Custom type tnCesLLJASchedStartTimeWedMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLJASchedStartTimeWedMins_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStartTimeWedMins_Object = MibTableColumn
tnCesLLJASchedStartTimeWedMins = _TnCesLLJASchedStartTimeWedMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 13),
    _TnCesLLJASchedStartTimeWedMins_Type()
)
tnCesLLJASchedStartTimeWedMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStartTimeWedMins.setStatus("current")


class _TnCesLLJASchedStopTimeWedHours_Type(Unsigned32):
    """Custom type tnCesLLJASchedStopTimeWedHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLJASchedStopTimeWedHours_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStopTimeWedHours_Object = MibTableColumn
tnCesLLJASchedStopTimeWedHours = _TnCesLLJASchedStopTimeWedHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 14),
    _TnCesLLJASchedStopTimeWedHours_Type()
)
tnCesLLJASchedStopTimeWedHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStopTimeWedHours.setStatus("current")


class _TnCesLLJASchedStopTimeWedMins_Type(Unsigned32):
    """Custom type tnCesLLJASchedStopTimeWedMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLJASchedStopTimeWedMins_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStopTimeWedMins_Object = MibTableColumn
tnCesLLJASchedStopTimeWedMins = _TnCesLLJASchedStopTimeWedMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 15),
    _TnCesLLJASchedStopTimeWedMins_Type()
)
tnCesLLJASchedStopTimeWedMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStopTimeWedMins.setStatus("current")


class _TnCesLLJASchedStartTimeThuHours_Type(Unsigned32):
    """Custom type tnCesLLJASchedStartTimeThuHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLJASchedStartTimeThuHours_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStartTimeThuHours_Object = MibTableColumn
tnCesLLJASchedStartTimeThuHours = _TnCesLLJASchedStartTimeThuHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 16),
    _TnCesLLJASchedStartTimeThuHours_Type()
)
tnCesLLJASchedStartTimeThuHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStartTimeThuHours.setStatus("current")


class _TnCesLLJASchedStartTimeThuMins_Type(Unsigned32):
    """Custom type tnCesLLJASchedStartTimeThuMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLJASchedStartTimeThuMins_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStartTimeThuMins_Object = MibTableColumn
tnCesLLJASchedStartTimeThuMins = _TnCesLLJASchedStartTimeThuMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 17),
    _TnCesLLJASchedStartTimeThuMins_Type()
)
tnCesLLJASchedStartTimeThuMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStartTimeThuMins.setStatus("current")


class _TnCesLLJASchedStopTimeThuHours_Type(Unsigned32):
    """Custom type tnCesLLJASchedStopTimeThuHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLJASchedStopTimeThuHours_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStopTimeThuHours_Object = MibTableColumn
tnCesLLJASchedStopTimeThuHours = _TnCesLLJASchedStopTimeThuHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 18),
    _TnCesLLJASchedStopTimeThuHours_Type()
)
tnCesLLJASchedStopTimeThuHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStopTimeThuHours.setStatus("current")


class _TnCesLLJASchedStopTimeThuMins_Type(Unsigned32):
    """Custom type tnCesLLJASchedStopTimeThuMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLJASchedStopTimeThuMins_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStopTimeThuMins_Object = MibTableColumn
tnCesLLJASchedStopTimeThuMins = _TnCesLLJASchedStopTimeThuMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 19),
    _TnCesLLJASchedStopTimeThuMins_Type()
)
tnCesLLJASchedStopTimeThuMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStopTimeThuMins.setStatus("current")


class _TnCesLLJASchedStartTimeFriHours_Type(Unsigned32):
    """Custom type tnCesLLJASchedStartTimeFriHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLJASchedStartTimeFriHours_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStartTimeFriHours_Object = MibTableColumn
tnCesLLJASchedStartTimeFriHours = _TnCesLLJASchedStartTimeFriHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 20),
    _TnCesLLJASchedStartTimeFriHours_Type()
)
tnCesLLJASchedStartTimeFriHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStartTimeFriHours.setStatus("current")


class _TnCesLLJASchedStartTimeFriMins_Type(Unsigned32):
    """Custom type tnCesLLJASchedStartTimeFriMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLJASchedStartTimeFriMins_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStartTimeFriMins_Object = MibTableColumn
tnCesLLJASchedStartTimeFriMins = _TnCesLLJASchedStartTimeFriMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 21),
    _TnCesLLJASchedStartTimeFriMins_Type()
)
tnCesLLJASchedStartTimeFriMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStartTimeFriMins.setStatus("current")


class _TnCesLLJASchedStopTimeFriHours_Type(Unsigned32):
    """Custom type tnCesLLJASchedStopTimeFriHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLJASchedStopTimeFriHours_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStopTimeFriHours_Object = MibTableColumn
tnCesLLJASchedStopTimeFriHours = _TnCesLLJASchedStopTimeFriHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 22),
    _TnCesLLJASchedStopTimeFriHours_Type()
)
tnCesLLJASchedStopTimeFriHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStopTimeFriHours.setStatus("current")


class _TnCesLLJASchedStopTimeFriMins_Type(Unsigned32):
    """Custom type tnCesLLJASchedStopTimeFriMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLJASchedStopTimeFriMins_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStopTimeFriMins_Object = MibTableColumn
tnCesLLJASchedStopTimeFriMins = _TnCesLLJASchedStopTimeFriMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 23),
    _TnCesLLJASchedStopTimeFriMins_Type()
)
tnCesLLJASchedStopTimeFriMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStopTimeFriMins.setStatus("current")


class _TnCesLLJASchedStartTimeSatHours_Type(Unsigned32):
    """Custom type tnCesLLJASchedStartTimeSatHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLJASchedStartTimeSatHours_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStartTimeSatHours_Object = MibTableColumn
tnCesLLJASchedStartTimeSatHours = _TnCesLLJASchedStartTimeSatHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 24),
    _TnCesLLJASchedStartTimeSatHours_Type()
)
tnCesLLJASchedStartTimeSatHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStartTimeSatHours.setStatus("current")


class _TnCesLLJASchedStartTimeSatMins_Type(Unsigned32):
    """Custom type tnCesLLJASchedStartTimeSatMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLJASchedStartTimeSatMins_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStartTimeSatMins_Object = MibTableColumn
tnCesLLJASchedStartTimeSatMins = _TnCesLLJASchedStartTimeSatMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 25),
    _TnCesLLJASchedStartTimeSatMins_Type()
)
tnCesLLJASchedStartTimeSatMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStartTimeSatMins.setStatus("current")


class _TnCesLLJASchedStopTimeSatHours_Type(Unsigned32):
    """Custom type tnCesLLJASchedStopTimeSatHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLJASchedStopTimeSatHours_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStopTimeSatHours_Object = MibTableColumn
tnCesLLJASchedStopTimeSatHours = _TnCesLLJASchedStopTimeSatHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 26),
    _TnCesLLJASchedStopTimeSatHours_Type()
)
tnCesLLJASchedStopTimeSatHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStopTimeSatHours.setStatus("current")


class _TnCesLLJASchedStopTimeSatMins_Type(Unsigned32):
    """Custom type tnCesLLJASchedStopTimeSatMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLJASchedStopTimeSatMins_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStopTimeSatMins_Object = MibTableColumn
tnCesLLJASchedStopTimeSatMins = _TnCesLLJASchedStopTimeSatMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 27),
    _TnCesLLJASchedStopTimeSatMins_Type()
)
tnCesLLJASchedStopTimeSatMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStopTimeSatMins.setStatus("current")


class _TnCesLLJASchedStartTimeSunHours_Type(Unsigned32):
    """Custom type tnCesLLJASchedStartTimeSunHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLJASchedStartTimeSunHours_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStartTimeSunHours_Object = MibTableColumn
tnCesLLJASchedStartTimeSunHours = _TnCesLLJASchedStartTimeSunHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 28),
    _TnCesLLJASchedStartTimeSunHours_Type()
)
tnCesLLJASchedStartTimeSunHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStartTimeSunHours.setStatus("current")


class _TnCesLLJASchedStartTimeSunMins_Type(Unsigned32):
    """Custom type tnCesLLJASchedStartTimeSunMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLJASchedStartTimeSunMins_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStartTimeSunMins_Object = MibTableColumn
tnCesLLJASchedStartTimeSunMins = _TnCesLLJASchedStartTimeSunMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 29),
    _TnCesLLJASchedStartTimeSunMins_Type()
)
tnCesLLJASchedStartTimeSunMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStartTimeSunMins.setStatus("current")


class _TnCesLLJASchedStopTimeSunHours_Type(Unsigned32):
    """Custom type tnCesLLJASchedStopTimeSunHours based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TnCesLLJASchedStopTimeSunHours_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStopTimeSunHours_Object = MibTableColumn
tnCesLLJASchedStopTimeSunHours = _TnCesLLJASchedStopTimeSunHours_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 30),
    _TnCesLLJASchedStopTimeSunHours_Type()
)
tnCesLLJASchedStopTimeSunHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStopTimeSunHours.setStatus("current")


class _TnCesLLJASchedStopTimeSunMins_Type(Unsigned32):
    """Custom type tnCesLLJASchedStopTimeSunMins based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TnCesLLJASchedStopTimeSunMins_Type.__name__ = "Unsigned32"
_TnCesLLJASchedStopTimeSunMins_Object = MibTableColumn
tnCesLLJASchedStopTimeSunMins = _TnCesLLJASchedStopTimeSunMins_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 14, 1, 31),
    _TnCesLLJASchedStopTimeSunMins_Type()
)
tnCesLLJASchedStopTimeSunMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLJASchedStopTimeSunMins.setStatus("current")
_TnCesLLChanSelectTable_Object = MibTable
tnCesLLChanSelectTable = _TnCesLLChanSelectTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 15)
)
if mibBuilder.loadTexts:
    tnCesLLChanSelectTable.setStatus("current")
_TnCesLLChanSelectEntry_Object = MibTableRow
tnCesLLChanSelectEntry = _TnCesLLChanSelectEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 15, 1)
)
tnCesLLChanSelectEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesLLChanSelectLLNumber"),
    (0, "TN-CES-MIB", "tnCesLLChanSelectPortNumber"),
)
if mibBuilder.loadTexts:
    tnCesLLChanSelectEntry.setStatus("current")


class _TnCesLLChanSelectLLNumber_Type(Unsigned32):
    """Custom type tnCesLLChanSelectLLNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnCesLLChanSelectLLNumber_Type.__name__ = "Unsigned32"
_TnCesLLChanSelectLLNumber_Object = MibTableColumn
tnCesLLChanSelectLLNumber = _TnCesLLChanSelectLLNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 15, 1, 1),
    _TnCesLLChanSelectLLNumber_Type()
)
tnCesLLChanSelectLLNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesLLChanSelectLLNumber.setStatus("current")


class _TnCesLLChanSelectPortNumber_Type(Unsigned32):
    """Custom type tnCesLLChanSelectPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TnCesLLChanSelectPortNumber_Type.__name__ = "Unsigned32"
_TnCesLLChanSelectPortNumber_Object = MibTableColumn
tnCesLLChanSelectPortNumber = _TnCesLLChanSelectPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 15, 1, 2),
    _TnCesLLChanSelectPortNumber_Type()
)
tnCesLLChanSelectPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesLLChanSelectPortNumber.setStatus("current")
_TnCesLLChanSelectAvailable_Type = Unsigned32
_TnCesLLChanSelectAvailable_Object = MibTableColumn
tnCesLLChanSelectAvailable = _TnCesLLChanSelectAvailable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 15, 1, 3),
    _TnCesLLChanSelectAvailable_Type()
)
tnCesLLChanSelectAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLChanSelectAvailable.setStatus("current")
_TnCesLLChanSelectUsed_Type = Unsigned32
_TnCesLLChanSelectUsed_Object = MibTableColumn
tnCesLLChanSelectUsed = _TnCesLLChanSelectUsed_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 15, 1, 4),
    _TnCesLLChanSelectUsed_Type()
)
tnCesLLChanSelectUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLChanSelectUsed.setStatus("current")
_TnCesLLAlternateTable_Object = MibTable
tnCesLLAlternateTable = _TnCesLLAlternateTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 16)
)
if mibBuilder.loadTexts:
    tnCesLLAlternateTable.setStatus("current")
_TnCesLLAlternateEntry_Object = MibTableRow
tnCesLLAlternateEntry = _TnCesLLAlternateEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 16, 1)
)
tnCesLLAlternateEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesLLAlternateLLNumber"),
)
if mibBuilder.loadTexts:
    tnCesLLAlternateEntry.setStatus("current")


class _TnCesLLAlternateLLNumber_Type(Unsigned32):
    """Custom type tnCesLLAlternateLLNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TnCesLLAlternateLLNumber_Type.__name__ = "Unsigned32"
_TnCesLLAlternateLLNumber_Object = MibTableColumn
tnCesLLAlternateLLNumber = _TnCesLLAlternateLLNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 16, 1, 1),
    _TnCesLLAlternateLLNumber_Type()
)
tnCesLLAlternateLLNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesLLAlternateLLNumber.setStatus("current")
_TnCesLLPlesiosynchronous_Type = TruthValue
_TnCesLLPlesiosynchronous_Object = MibTableColumn
tnCesLLPlesiosynchronous = _TnCesLLPlesiosynchronous_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 16, 1, 2),
    _TnCesLLPlesiosynchronous_Type()
)
tnCesLLPlesiosynchronous.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLPlesiosynchronous.setStatus("current")
_TnCesLLAsymmetric_Type = TruthValue
_TnCesLLAsymmetric_Object = MibTableColumn
tnCesLLAsymmetric = _TnCesLLAsymmetric_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 16, 1, 3),
    _TnCesLLAsymmetric_Type()
)
tnCesLLAsymmetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLAsymmetric.setStatus("current")


class _TnCesLLBytesPerPacketRx_Type(Unsigned32):
    """Custom type tnCesLLBytesPerPacketRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_TnCesLLBytesPerPacketRx_Type.__name__ = "Unsigned32"
_TnCesLLBytesPerPacketRx_Object = MibTableColumn
tnCesLLBytesPerPacketRx = _TnCesLLBytesPerPacketRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 16, 1, 4),
    _TnCesLLBytesPerPacketRx_Type()
)
tnCesLLBytesPerPacketRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLBytesPerPacketRx.setStatus("current")


class _TnCesLLBytesPerPacketTx_Type(Unsigned32):
    """Custom type tnCesLLBytesPerPacketTx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_TnCesLLBytesPerPacketTx_Type.__name__ = "Unsigned32"
_TnCesLLBytesPerPacketTx_Object = MibTableColumn
tnCesLLBytesPerPacketTx = _TnCesLLBytesPerPacketTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 16, 1, 5),
    _TnCesLLBytesPerPacketTx_Type()
)
tnCesLLBytesPerPacketTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLBytesPerPacketTx.setStatus("current")
_TnCesLLStatusTable_Object = MibTable
tnCesLLStatusTable = _TnCesLLStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17)
)
if mibBuilder.loadTexts:
    tnCesLLStatusTable.setStatus("current")
_TnCesLLStatusEntry_Object = MibTableRow
tnCesLLStatusEntry = _TnCesLLStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1)
)
tnCesLLStatusEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesLLStatusNumber"),
)
if mibBuilder.loadTexts:
    tnCesLLStatusEntry.setStatus("current")


class _TnCesLLStatusNumber_Type(Unsigned32):
    """Custom type tnCesLLStatusNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnCesLLStatusNumber_Type.__name__ = "Unsigned32"
_TnCesLLStatusNumber_Object = MibTableColumn
tnCesLLStatusNumber = _TnCesLLStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 1),
    _TnCesLLStatusNumber_Type()
)
tnCesLLStatusNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesLLStatusNumber.setStatus("current")
_TnCesLLStatusEnabled_Type = TruthValue
_TnCesLLStatusEnabled_Object = MibTableColumn
tnCesLLStatusEnabled = _TnCesLLStatusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 2),
    _TnCesLLStatusEnabled_Type()
)
tnCesLLStatusEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusEnabled.setStatus("current")
_TnCesLLStatusActive_Type = TruthValue
_TnCesLLStatusActive_Object = MibTableColumn
tnCesLLStatusActive = _TnCesLLStatusActive_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 3),
    _TnCesLLStatusActive_Type()
)
tnCesLLStatusActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusActive.setStatus("current")
_TnCesLLStatusArpResolved_Type = TruthValue
_TnCesLLStatusArpResolved_Object = MibTableColumn
tnCesLLStatusArpResolved = _TnCesLLStatusArpResolved_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 4),
    _TnCesLLStatusArpResolved_Type()
)
tnCesLLStatusArpResolved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusArpResolved.setStatus("current")


class _TnCesLLStatusNumberOfChannels_Type(Unsigned32):
    """Custom type tnCesLLStatusNumberOfChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TnCesLLStatusNumberOfChannels_Type.__name__ = "Unsigned32"
_TnCesLLStatusNumberOfChannels_Object = MibTableColumn
tnCesLLStatusNumberOfChannels = _TnCesLLStatusNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 5),
    _TnCesLLStatusNumberOfChannels_Type()
)
tnCesLLStatusNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusNumberOfChannels.setStatus("current")
_TnCesLLStatusRemoteMac_Type = MacAddress
_TnCesLLStatusRemoteMac_Object = MibTableColumn
tnCesLLStatusRemoteMac = _TnCesLLStatusRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 6),
    _TnCesLLStatusRemoteMac_Type()
)
tnCesLLStatusRemoteMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusRemoteMac.setStatus("current")
_TnCesLLStatusRemoteIpAddrType_Type = InetAddressType
_TnCesLLStatusRemoteIpAddrType_Object = MibTableColumn
tnCesLLStatusRemoteIpAddrType = _TnCesLLStatusRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 7),
    _TnCesLLStatusRemoteIpAddrType_Type()
)
tnCesLLStatusRemoteIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusRemoteIpAddrType.setStatus("current")
_TnCesLLStatusRemoteIpAddr_Type = InetAddress
_TnCesLLStatusRemoteIpAddr_Object = MibTableColumn
tnCesLLStatusRemoteIpAddr = _TnCesLLStatusRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 8),
    _TnCesLLStatusRemoteIpAddr_Type()
)
tnCesLLStatusRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusRemoteIpAddr.setStatus("current")
_TnCesLLStatusRemoteContextKnown_Type = TruthValue
_TnCesLLStatusRemoteContextKnown_Object = MibTableColumn
tnCesLLStatusRemoteContextKnown = _TnCesLLStatusRemoteContextKnown_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 9),
    _TnCesLLStatusRemoteContextKnown_Type()
)
tnCesLLStatusRemoteContextKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusRemoteContextKnown.setStatus("current")


class _TnCesLLStatusRemoteContextNumber_Type(Unsigned32):
    """Custom type tnCesLLStatusRemoteContextNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnCesLLStatusRemoteContextNumber_Type.__name__ = "Unsigned32"
_TnCesLLStatusRemoteContextNumber_Object = MibTableColumn
tnCesLLStatusRemoteContextNumber = _TnCesLLStatusRemoteContextNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 10),
    _TnCesLLStatusRemoteContextNumber_Type()
)
tnCesLLStatusRemoteContextNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusRemoteContextNumber.setStatus("current")
_TnCesLLStatusRemotePortKnown_Type = TruthValue
_TnCesLLStatusRemotePortKnown_Object = MibTableColumn
tnCesLLStatusRemotePortKnown = _TnCesLLStatusRemotePortKnown_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 11),
    _TnCesLLStatusRemotePortKnown_Type()
)
tnCesLLStatusRemotePortKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusRemotePortKnown.setStatus("current")


class _TnCesLLStatusRemotePort_Type(Unsigned32):
    """Custom type tnCesLLStatusRemotePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnCesLLStatusRemotePort_Type.__name__ = "Unsigned32"
_TnCesLLStatusRemotePort_Object = MibTableColumn
tnCesLLStatusRemotePort = _TnCesLLStatusRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 12),
    _TnCesLLStatusRemotePort_Type()
)
tnCesLLStatusRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusRemotePort.setStatus("current")
_TnCesLLStatusQueueLengthValid_Type = TruthValue
_TnCesLLStatusQueueLengthValid_Object = MibTableColumn
tnCesLLStatusQueueLengthValid = _TnCesLLStatusQueueLengthValid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 13),
    _TnCesLLStatusQueueLengthValid_Type()
)
tnCesLLStatusQueueLengthValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusQueueLengthValid.setStatus("current")
_TnCesLLStatusMinQueueLength_Type = Unsigned32
_TnCesLLStatusMinQueueLength_Object = MibTableColumn
tnCesLLStatusMinQueueLength = _TnCesLLStatusMinQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 14),
    _TnCesLLStatusMinQueueLength_Type()
)
tnCesLLStatusMinQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusMinQueueLength.setStatus("current")
_TnCesLLStatusMaxQueueLength_Type = Unsigned32
_TnCesLLStatusMaxQueueLength_Object = MibTableColumn
tnCesLLStatusMaxQueueLength = _TnCesLLStatusMaxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 15),
    _TnCesLLStatusMaxQueueLength_Type()
)
tnCesLLStatusMaxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusMaxQueueLength.setStatus("current")
_TnCesLLStatusAveQueueLengthWhole_Type = Unsigned32
_TnCesLLStatusAveQueueLengthWhole_Object = MibTableColumn
tnCesLLStatusAveQueueLengthWhole = _TnCesLLStatusAveQueueLengthWhole_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 16),
    _TnCesLLStatusAveQueueLengthWhole_Type()
)
tnCesLLStatusAveQueueLengthWhole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusAveQueueLengthWhole.setStatus("current")
_TnCesLLStatusAveQueueLengthFrac_Type = Unsigned32
_TnCesLLStatusAveQueueLengthFrac_Object = MibTableColumn
tnCesLLStatusAveQueueLengthFrac = _TnCesLLStatusAveQueueLengthFrac_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 17),
    _TnCesLLStatusAveQueueLengthFrac_Type()
)
tnCesLLStatusAveQueueLengthFrac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusAveQueueLengthFrac.setStatus("current")
_TnCesLLStatusEarly_Type = Counter32
_TnCesLLStatusEarly_Object = MibTableColumn
tnCesLLStatusEarly = _TnCesLLStatusEarly_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 18),
    _TnCesLLStatusEarly_Type()
)
tnCesLLStatusEarly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusEarly.setStatus("current")
_TnCesLLStatusLate_Type = Counter32
_TnCesLLStatusLate_Object = MibTableColumn
tnCesLLStatusLate = _TnCesLLStatusLate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 19),
    _TnCesLLStatusLate_Type()
)
tnCesLLStatusLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusLate.setStatus("current")
_TnCesLLStatusUnderrun_Type = Counter32
_TnCesLLStatusUnderrun_Object = MibTableColumn
tnCesLLStatusUnderrun = _TnCesLLStatusUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 20),
    _TnCesLLStatusUnderrun_Type()
)
tnCesLLStatusUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusUnderrun.setStatus("current")
_TnCesLLStatusLastSequence_Type = Counter32
_TnCesLLStatusLastSequence_Object = MibTableColumn
tnCesLLStatusLastSequence = _TnCesLLStatusLastSequence_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 21),
    _TnCesLLStatusLastSequence_Type()
)
tnCesLLStatusLastSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusLastSequence.setStatus("current")
_TnCesLLStatusPacketsRx_Type = Counter32
_TnCesLLStatusPacketsRx_Object = MibTableColumn
tnCesLLStatusPacketsRx = _TnCesLLStatusPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 22),
    _TnCesLLStatusPacketsRx_Type()
)
tnCesLLStatusPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusPacketsRx.setStatus("current")
_TnCesLLStatusPacketsTx_Type = Counter32
_TnCesLLStatusPacketsTx_Object = MibTableColumn
tnCesLLStatusPacketsTx = _TnCesLLStatusPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 23),
    _TnCesLLStatusPacketsTx_Type()
)
tnCesLLStatusPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusPacketsTx.setStatus("current")
_TnCesLLStatusSlipsReduceCount_Type = Counter32
_TnCesLLStatusSlipsReduceCount_Object = MibTableColumn
tnCesLLStatusSlipsReduceCount = _TnCesLLStatusSlipsReduceCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 24),
    _TnCesLLStatusSlipsReduceCount_Type()
)
tnCesLLStatusSlipsReduceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusSlipsReduceCount.setStatus("current")
_TnCesLLStatusSlipsExtendCount_Type = Counter32
_TnCesLLStatusSlipsExtendCount_Object = MibTableColumn
tnCesLLStatusSlipsExtendCount = _TnCesLLStatusSlipsExtendCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 25),
    _TnCesLLStatusSlipsExtendCount_Type()
)
tnCesLLStatusSlipsExtendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesLLStatusSlipsExtendCount.setStatus("current")
_TnCesLLLocalLoop_Type = TruthValue
_TnCesLLLocalLoop_Object = MibTableColumn
tnCesLLLocalLoop = _TnCesLLLocalLoop_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 26),
    _TnCesLLLocalLoop_Type()
)
tnCesLLLocalLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLLocalLoop.setStatus("current")
_TnCesLLRemoteLoop_Type = TruthValue
_TnCesLLRemoteLoop_Object = MibTableColumn
tnCesLLRemoteLoop = _TnCesLLRemoteLoop_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 27),
    _TnCesLLRemoteLoop_Type()
)
tnCesLLRemoteLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLRemoteLoop.setStatus("current")


class _TnCesLLNudge_Type(Integer32):
    """Custom type tnCesLLNudge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_TnCesLLNudge_Type.__name__ = "Integer32"
_TnCesLLNudge_Object = MibTableColumn
tnCesLLNudge = _TnCesLLNudge_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 28),
    _TnCesLLNudge_Type()
)
tnCesLLNudge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLNudge.setStatus("current")
_TnCesLLResetErrorStats_Type = TruthValue
_TnCesLLResetErrorStats_Object = MibTableColumn
tnCesLLResetErrorStats = _TnCesLLResetErrorStats_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 17, 1, 29),
    _TnCesLLResetErrorStats_Type()
)
tnCesLLResetErrorStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesLLResetErrorStats.setStatus("current")
_TnCesTDMStatusTable_Object = MibTable
tnCesTDMStatusTable = _TnCesTDMStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 18)
)
if mibBuilder.loadTexts:
    tnCesTDMStatusTable.setStatus("current")
_TnCesTDMStatusEntry_Object = MibTableRow
tnCesTDMStatusEntry = _TnCesTDMStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 18, 1)
)
tnCesTDMStatusEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesTDMStatusNumber"),
)
if mibBuilder.loadTexts:
    tnCesTDMStatusEntry.setStatus("current")


class _TnCesTDMStatusNumber_Type(Unsigned32):
    """Custom type tnCesTDMStatusNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TnCesTDMStatusNumber_Type.__name__ = "Unsigned32"
_TnCesTDMStatusNumber_Object = MibTableColumn
tnCesTDMStatusNumber = _TnCesTDMStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 18, 1, 1),
    _TnCesTDMStatusNumber_Type()
)
tnCesTDMStatusNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesTDMStatusNumber.setStatus("current")


class _TnCesTDMStatusPhysical_Type(DisplayString):
    """Custom type tnCesTDMStatusPhysical based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnCesTDMStatusPhysical_Type.__name__ = "DisplayString"
_TnCesTDMStatusPhysical_Object = MibTableColumn
tnCesTDMStatusPhysical = _TnCesTDMStatusPhysical_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 18, 1, 2),
    _TnCesTDMStatusPhysical_Type()
)
tnCesTDMStatusPhysical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesTDMStatusPhysical.setStatus("current")


class _TnCesTDMStatusRxSignalLevel_Type(DisplayString):
    """Custom type tnCesTDMStatusRxSignalLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnCesTDMStatusRxSignalLevel_Type.__name__ = "DisplayString"
_TnCesTDMStatusRxSignalLevel_Object = MibTableColumn
tnCesTDMStatusRxSignalLevel = _TnCesTDMStatusRxSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 18, 1, 3),
    _TnCesTDMStatusRxSignalLevel_Type()
)
tnCesTDMStatusRxSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesTDMStatusRxSignalLevel.setStatus("current")


class _TnCesTDMStatusRxError_Type(DisplayString):
    """Custom type tnCesTDMStatusRxError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnCesTDMStatusRxError_Type.__name__ = "DisplayString"
_TnCesTDMStatusRxError_Object = MibTableColumn
tnCesTDMStatusRxError = _TnCesTDMStatusRxError_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 18, 1, 4),
    _TnCesTDMStatusRxError_Type()
)
tnCesTDMStatusRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesTDMStatusRxError.setStatus("current")
_TnCesTDMLocalLoop_Type = TruthValue
_TnCesTDMLocalLoop_Object = MibTableColumn
tnCesTDMLocalLoop = _TnCesTDMLocalLoop_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 18, 1, 5),
    _TnCesTDMLocalLoop_Type()
)
tnCesTDMLocalLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMLocalLoop.setStatus("current")
_TnCesTDMRemoteLoop_Type = TruthValue
_TnCesTDMRemoteLoop_Object = MibTableColumn
tnCesTDMRemoteLoop = _TnCesTDMRemoteLoop_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 18, 1, 6),
    _TnCesTDMRemoteLoop_Type()
)
tnCesTDMRemoteLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMRemoteLoop.setStatus("current")
_TnCesTDMBreakCalls_Type = TruthValue
_TnCesTDMBreakCalls_Object = MibTableColumn
tnCesTDMBreakCalls = _TnCesTDMBreakCalls_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 18, 1, 7),
    _TnCesTDMBreakCalls_Type()
)
tnCesTDMBreakCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesTDMBreakCalls.setStatus("current")
_TnCesCallStatusTable_Object = MibTable
tnCesCallStatusTable = _TnCesCallStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 19)
)
if mibBuilder.loadTexts:
    tnCesCallStatusTable.setStatus("current")
_TnCesCallStatusEntry_Object = MibTableRow
tnCesCallStatusEntry = _TnCesCallStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 19, 1)
)
tnCesCallStatusEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesCallStatusNumber"),
)
if mibBuilder.loadTexts:
    tnCesCallStatusEntry.setStatus("current")


class _TnCesCallStatusNumber_Type(Unsigned32):
    """Custom type tnCesCallStatusNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TnCesCallStatusNumber_Type.__name__ = "Unsigned32"
_TnCesCallStatusNumber_Object = MibTableColumn
tnCesCallStatusNumber = _TnCesCallStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 19, 1, 1),
    _TnCesCallStatusNumber_Type()
)
tnCesCallStatusNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesCallStatusNumber.setStatus("current")
_TnCesCallStatusStartTime_Type = DateAndTime
_TnCesCallStatusStartTime_Object = MibTableColumn
tnCesCallStatusStartTime = _TnCesCallStatusStartTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 19, 1, 2),
    _TnCesCallStatusStartTime_Type()
)
tnCesCallStatusStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesCallStatusStartTime.setStatus("current")


class _TnCesCallStatusSource_Type(DisplayString):
    """Custom type tnCesCallStatusSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnCesCallStatusSource_Type.__name__ = "DisplayString"
_TnCesCallStatusSource_Object = MibTableColumn
tnCesCallStatusSource = _TnCesCallStatusSource_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 19, 1, 3),
    _TnCesCallStatusSource_Type()
)
tnCesCallStatusSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesCallStatusSource.setStatus("current")


class _TnCesCallStatusDestination_Type(DisplayString):
    """Custom type tnCesCallStatusDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TnCesCallStatusDestination_Type.__name__ = "DisplayString"
_TnCesCallStatusDestination_Object = MibTableColumn
tnCesCallStatusDestination = _TnCesCallStatusDestination_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 19, 1, 4),
    _TnCesCallStatusDestination_Type()
)
tnCesCallStatusDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesCallStatusDestination.setStatus("current")
_TnCesCallStatusOriginator_Type = TruthValue
_TnCesCallStatusOriginator_Object = MibTableColumn
tnCesCallStatusOriginator = _TnCesCallStatusOriginator_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 19, 1, 5),
    _TnCesCallStatusOriginator_Type()
)
tnCesCallStatusOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesCallStatusOriginator.setStatus("current")


class _TnCesCallStatusDestinationNumber_Type(DisplayString):
    """Custom type tnCesCallStatusDestinationNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_TnCesCallStatusDestinationNumber_Type.__name__ = "DisplayString"
_TnCesCallStatusDestinationNumber_Object = MibTableColumn
tnCesCallStatusDestinationNumber = _TnCesCallStatusDestinationNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 19, 1, 6),
    _TnCesCallStatusDestinationNumber_Type()
)
tnCesCallStatusDestinationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesCallStatusDestinationNumber.setStatus("current")


class _TnCesCallStatusSourceNumber_Type(DisplayString):
    """Custom type tnCesCallStatusSourceNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_TnCesCallStatusSourceNumber_Type.__name__ = "DisplayString"
_TnCesCallStatusSourceNumber_Object = MibTableColumn
tnCesCallStatusSourceNumber = _TnCesCallStatusSourceNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 19, 1, 7),
    _TnCesCallStatusSourceNumber_Type()
)
tnCesCallStatusSourceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesCallStatusSourceNumber.setStatus("current")


class _TnCesCallStatusState_Type(DisplayString):
    """Custom type tnCesCallStatusState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TnCesCallStatusState_Type.__name__ = "DisplayString"
_TnCesCallStatusState_Object = MibTableColumn
tnCesCallStatusState = _TnCesCallStatusState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 19, 1, 8),
    _TnCesCallStatusState_Type()
)
tnCesCallStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesCallStatusState.setStatus("current")
_TnCesClockStatusTable_Object = MibTable
tnCesClockStatusTable = _TnCesClockStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 20)
)
if mibBuilder.loadTexts:
    tnCesClockStatusTable.setStatus("current")
_TnCesClockStatusEntry_Object = MibTableRow
tnCesClockStatusEntry = _TnCesClockStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 20, 1)
)
tnCesClockStatusEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesClockStatusStreamNumber"),
)
if mibBuilder.loadTexts:
    tnCesClockStatusEntry.setStatus("current")


class _TnCesClockStatusStreamNumber_Type(Unsigned32):
    """Custom type tnCesClockStatusStreamNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TnCesClockStatusStreamNumber_Type.__name__ = "Unsigned32"
_TnCesClockStatusStreamNumber_Object = MibTableColumn
tnCesClockStatusStreamNumber = _TnCesClockStatusStreamNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 20, 1, 1),
    _TnCesClockStatusStreamNumber_Type()
)
tnCesClockStatusStreamNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesClockStatusStreamNumber.setStatus("current")


class _TnCesClockStatusStreamStatus_Type(Integer32):
    """Custom type tnCesClockStatusStreamStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("freerun", 0),
          ("holdover", 1),
          ("acquiring", 2),
          ("acquired", 3))
    )


_TnCesClockStatusStreamStatus_Type.__name__ = "Integer32"
_TnCesClockStatusStreamStatus_Object = MibTableColumn
tnCesClockStatusStreamStatus = _TnCesClockStatusStreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 20, 1, 2),
    _TnCesClockStatusStreamStatus_Type()
)
tnCesClockStatusStreamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesClockStatusStreamStatus.setStatus("current")


class _TnCesClockStatusStreamMode_Type(Integer32):
    """Custom type tnCesClockStatusStreamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clockRecoveryDisabled", 0),
          ("adaptive", 1),
          ("adaptiveEnhanced", 2),
          ("adaptiveFrequency", 3))
    )


_TnCesClockStatusStreamMode_Type.__name__ = "Integer32"
_TnCesClockStatusStreamMode_Object = MibTableColumn
tnCesClockStatusStreamMode = _TnCesClockStatusStreamMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 20, 1, 3),
    _TnCesClockStatusStreamMode_Type()
)
tnCesClockStatusStreamMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesClockStatusStreamMode.setStatus("current")
_TnCesClockStatusStreamDCO_Type = Integer32
_TnCesClockStatusStreamDCO_Object = MibTableColumn
tnCesClockStatusStreamDCO = _TnCesClockStatusStreamDCO_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 20, 1, 4),
    _TnCesClockStatusStreamDCO_Type()
)
tnCesClockStatusStreamDCO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesClockStatusStreamDCO.setStatus("current")
_TnCesClockStatusStreamDCOMin_Type = Integer32
_TnCesClockStatusStreamDCOMin_Object = MibTableColumn
tnCesClockStatusStreamDCOMin = _TnCesClockStatusStreamDCOMin_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 20, 1, 5),
    _TnCesClockStatusStreamDCOMin_Type()
)
tnCesClockStatusStreamDCOMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesClockStatusStreamDCOMin.setStatus("current")
_TnCesClockStatusStreamDCOMax_Type = Integer32
_TnCesClockStatusStreamDCOMax_Object = MibTableColumn
tnCesClockStatusStreamDCOMax = _TnCesClockStatusStreamDCOMax_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 20, 1, 6),
    _TnCesClockStatusStreamDCOMax_Type()
)
tnCesClockStatusStreamDCOMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesClockStatusStreamDCOMax.setStatus("current")
_TnCesClockStatusStreamDCOAvg_Type = Integer32
_TnCesClockStatusStreamDCOAvg_Object = MibTableColumn
tnCesClockStatusStreamDCOAvg = _TnCesClockStatusStreamDCOAvg_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 20, 1, 7),
    _TnCesClockStatusStreamDCOAvg_Type()
)
tnCesClockStatusStreamDCOAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesClockStatusStreamDCOAvg.setStatus("current")
_TnCesDebug_ObjectIdentity = ObjectIdentity
tnCesDebug = _TnCesDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 21)
)
_TnCesDebugTDMTable_Object = MibTable
tnCesDebugTDMTable = _TnCesDebugTDMTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 21, 1)
)
if mibBuilder.loadTexts:
    tnCesDebugTDMTable.setStatus("current")
_TnCesDebugTDMEntry_Object = MibTableRow
tnCesDebugTDMEntry = _TnCesDebugTDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 21, 1, 1)
)
tnCesDebugTDMEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesDebugTDMPortNumber"),
)
if mibBuilder.loadTexts:
    tnCesDebugTDMEntry.setStatus("current")


class _TnCesDebugTDMPortNumber_Type(Unsigned32):
    """Custom type tnCesDebugTDMPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TnCesDebugTDMPortNumber_Type.__name__ = "Unsigned32"
_TnCesDebugTDMPortNumber_Object = MibTableColumn
tnCesDebugTDMPortNumber = _TnCesDebugTDMPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 21, 1, 1, 1),
    _TnCesDebugTDMPortNumber_Type()
)
tnCesDebugTDMPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesDebugTDMPortNumber.setStatus("current")
_TnCesDebugTDMPortEnable_Type = TruthValue
_TnCesDebugTDMPortEnable_Object = MibTableColumn
tnCesDebugTDMPortEnable = _TnCesDebugTDMPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 21, 1, 1, 2),
    _TnCesDebugTDMPortEnable_Type()
)
tnCesDebugTDMPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesDebugTDMPortEnable.setStatus("current")
_TnCesDebugLLTable_Object = MibTable
tnCesDebugLLTable = _TnCesDebugLLTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 21, 2)
)
if mibBuilder.loadTexts:
    tnCesDebugLLTable.setStatus("current")
_TnCesDebugLLEntry_Object = MibTableRow
tnCesDebugLLEntry = _TnCesDebugLLEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 21, 2, 1)
)
tnCesDebugLLEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesDebugLLNumber"),
)
if mibBuilder.loadTexts:
    tnCesDebugLLEntry.setStatus("current")


class _TnCesDebugLLNumber_Type(Unsigned32):
    """Custom type tnCesDebugLLNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnCesDebugLLNumber_Type.__name__ = "Unsigned32"
_TnCesDebugLLNumber_Object = MibTableColumn
tnCesDebugLLNumber = _TnCesDebugLLNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 21, 2, 1, 1),
    _TnCesDebugLLNumber_Type()
)
tnCesDebugLLNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesDebugLLNumber.setStatus("current")
_TnCesDebugLLEnable_Type = TruthValue
_TnCesDebugLLEnable_Object = MibTableColumn
tnCesDebugLLEnable = _TnCesDebugLLEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 21, 2, 1, 2),
    _TnCesDebugLLEnable_Type()
)
tnCesDebugLLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesDebugLLEnable.setStatus("current")
_TnCesDebugMiscTable_Object = MibTable
tnCesDebugMiscTable = _TnCesDebugMiscTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 21, 3)
)
if mibBuilder.loadTexts:
    tnCesDebugMiscTable.setStatus("current")
_TnCesDebugMiscEntry_Object = MibTableRow
tnCesDebugMiscEntry = _TnCesDebugMiscEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 21, 3, 1)
)
tnCesDebugMiscEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesDebugMiscItem"),
)
if mibBuilder.loadTexts:
    tnCesDebugMiscEntry.setStatus("current")


class _TnCesDebugMiscItem_Type(Integer32):
    """Custom type tnCesDebugMiscItem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("control", 1),
          ("arp", 2),
          ("sip", 3),
          ("logicalLinkControl", 4),
          ("logicalLinkGlobal", 5))
    )


_TnCesDebugMiscItem_Type.__name__ = "Integer32"
_TnCesDebugMiscItem_Object = MibTableColumn
tnCesDebugMiscItem = _TnCesDebugMiscItem_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 21, 3, 1, 1),
    _TnCesDebugMiscItem_Type()
)
tnCesDebugMiscItem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesDebugMiscItem.setStatus("current")
_TnCesDebugMiscEnable_Type = TruthValue
_TnCesDebugMiscEnable_Object = MibTableColumn
tnCesDebugMiscEnable = _TnCesDebugMiscEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 21, 3, 1, 2),
    _TnCesDebugMiscEnable_Type()
)
tnCesDebugMiscEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesDebugMiscEnable.setStatus("current")
_TnCesRS530Table_Object = MibTable
tnCesRS530Table = _TnCesRS530Table_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 22)
)
if mibBuilder.loadTexts:
    tnCesRS530Table.setStatus("current")
_TnCesRS530Entry_Object = MibTableRow
tnCesRS530Entry = _TnCesRS530Entry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 22, 1)
)
tnCesRS530Entry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesRS530PortNumber"),
)
if mibBuilder.loadTexts:
    tnCesRS530Entry.setStatus("current")


class _TnCesRS530PortNumber_Type(Unsigned32):
    """Custom type tnCesRS530PortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TnCesRS530PortNumber_Type.__name__ = "Unsigned32"
_TnCesRS530PortNumber_Object = MibTableColumn
tnCesRS530PortNumber = _TnCesRS530PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 22, 1, 1),
    _TnCesRS530PortNumber_Type()
)
tnCesRS530PortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesRS530PortNumber.setStatus("current")
_TnCesRS530Rate_Type = Unsigned32
_TnCesRS530Rate_Object = MibTableColumn
tnCesRS530Rate = _TnCesRS530Rate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 22, 1, 2),
    _TnCesRS530Rate_Type()
)
tnCesRS530Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesRS530Rate.setStatus("current")
_TnCesRS530ShutdownCallsOnFail_Type = TruthValue
_TnCesRS530ShutdownCallsOnFail_Object = MibTableColumn
tnCesRS530ShutdownCallsOnFail = _TnCesRS530ShutdownCallsOnFail_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 22, 1, 3),
    _TnCesRS530ShutdownCallsOnFail_Type()
)
tnCesRS530ShutdownCallsOnFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesRS530ShutdownCallsOnFail.setStatus("current")
_TnCesRS530StatusTable_Object = MibTable
tnCesRS530StatusTable = _TnCesRS530StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 23)
)
if mibBuilder.loadTexts:
    tnCesRS530StatusTable.setStatus("current")
_TnCesRS530StatusEntry_Object = MibTableRow
tnCesRS530StatusEntry = _TnCesRS530StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 23, 1)
)
tnCesRS530StatusEntry.setIndexNames(
    (0, "TN-CES-MIB", "tnCesRS530StatusNumber"),
)
if mibBuilder.loadTexts:
    tnCesRS530StatusEntry.setStatus("current")


class _TnCesRS530StatusNumber_Type(Unsigned32):
    """Custom type tnCesRS530StatusNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TnCesRS530StatusNumber_Type.__name__ = "Unsigned32"
_TnCesRS530StatusNumber_Object = MibTableColumn
tnCesRS530StatusNumber = _TnCesRS530StatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 23, 1, 1),
    _TnCesRS530StatusNumber_Type()
)
tnCesRS530StatusNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCesRS530StatusNumber.setStatus("current")


class _TnCesRS530InterfaceType_Type(DisplayString):
    """Custom type tnCesRS530InterfaceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TnCesRS530InterfaceType_Type.__name__ = "DisplayString"
_TnCesRS530InterfaceType_Object = MibTableColumn
tnCesRS530InterfaceType = _TnCesRS530InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 23, 1, 2),
    _TnCesRS530InterfaceType_Type()
)
tnCesRS530InterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesRS530InterfaceType.setStatus("current")
_TnCesRS530StatusDTR_Type = TruthValue
_TnCesRS530StatusDTR_Object = MibTableColumn
tnCesRS530StatusDTR = _TnCesRS530StatusDTR_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 23, 1, 3),
    _TnCesRS530StatusDTR_Type()
)
tnCesRS530StatusDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesRS530StatusDTR.setStatus("current")
_TnCesRS530StatusDCD_Type = TruthValue
_TnCesRS530StatusDCD_Object = MibTableColumn
tnCesRS530StatusDCD = _TnCesRS530StatusDCD_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 23, 1, 4),
    _TnCesRS530StatusDCD_Type()
)
tnCesRS530StatusDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesRS530StatusDCD.setStatus("current")
_TnCesRS530StatusRTS_Type = TruthValue
_TnCesRS530StatusRTS_Object = MibTableColumn
tnCesRS530StatusRTS = _TnCesRS530StatusRTS_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 23, 1, 5),
    _TnCesRS530StatusRTS_Type()
)
tnCesRS530StatusRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesRS530StatusRTS.setStatus("current")
_TnCesRS530StatusCTS_Type = TruthValue
_TnCesRS530StatusCTS_Object = MibTableColumn
tnCesRS530StatusCTS = _TnCesRS530StatusCTS_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 23, 1, 6),
    _TnCesRS530StatusCTS_Type()
)
tnCesRS530StatusCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesRS530StatusCTS.setStatus("current")
_TnCesRS530StatusDSR_Type = TruthValue
_TnCesRS530StatusDSR_Object = MibTableColumn
tnCesRS530StatusDSR = _TnCesRS530StatusDSR_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 23, 1, 7),
    _TnCesRS530StatusDSR_Type()
)
tnCesRS530StatusDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCesRS530StatusDSR.setStatus("current")
_TnCesRS530LocalLoop_Type = TruthValue
_TnCesRS530LocalLoop_Object = MibTableColumn
tnCesRS530LocalLoop = _TnCesRS530LocalLoop_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 23, 1, 8),
    _TnCesRS530LocalLoop_Type()
)
tnCesRS530LocalLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesRS530LocalLoop.setStatus("current")
_TnCesRS530RemoteLoop_Type = TruthValue
_TnCesRS530RemoteLoop_Object = MibTableColumn
tnCesRS530RemoteLoop = _TnCesRS530RemoteLoop_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 23, 1, 9),
    _TnCesRS530RemoteLoop_Type()
)
tnCesRS530RemoteLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesRS530RemoteLoop.setStatus("current")
_TnCesRS530BreakCalls_Type = TruthValue
_TnCesRS530BreakCalls_Object = MibTableColumn
tnCesRS530BreakCalls = _TnCesRS530BreakCalls_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 1, 23, 1, 10),
    _TnCesRS530BreakCalls_Type()
)
tnCesRS530BreakCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnCesRS530BreakCalls.setStatus("current")
_TnCesConformance_ObjectIdentity = ObjectIdentity
tnCesConformance = _TnCesConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 2)
)
_TnCesCompliances_ObjectIdentity = ObjectIdentity
tnCesCompliances = _TnCesCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 2, 1)
)
_TnCesGroups_ObjectIdentity = ObjectIdentity
tnCesGroups = _TnCesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 2, 2)
)

# Managed Objects groups

tnCesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 2, 2, 1)
)
tnCesGroup.setObjects(
      *(("TN-CES-MIB", "tnCesMiscClockPriority"),
        ("TN-CES-MIB", "tnCesPRIClockPriority"),
        ("TN-CES-MIB", "tnCesLLClockPriority"),
        ("TN-CES-MIB", "tnCesEventThreshold"),
        ("TN-CES-MIB", "tnCesEventReportingInterval"),
        ("TN-CES-MIB", "tnCesEventThresholdEarly"),
        ("TN-CES-MIB", "tnCesEventThresholdLate"),
        ("TN-CES-MIB", "tnCesEventThresholdUnderrun"),
        ("TN-CES-MIB", "tnCesEventThresholdDCO"),
        ("TN-CES-MIB", "tnCesMulticastJoinAction"),
        ("TN-CES-MIB", "tnCesMulticastJoinAddrType"),
        ("TN-CES-MIB", "tnCesMulticastJoinAddr"),
        ("TN-CES-MIB", "tnCesProtocolUnderrunFixed"),
        ("TN-CES-MIB", "tnCesProtocolUnderrunValue"),
        ("TN-CES-MIB", "tnCesProtocolUDPBasePort"),
        ("TN-CES-MIB", "tnCesProtocolType"),
        ("TN-CES-MIB", "tnCesProtocolEnableSSRCChecking"),
        ("TN-CES-MIB", "tnCesClockRecoveryAlgorithm"),
        ("TN-CES-MIB", "tnCesClockRecoveryFilter"),
        ("TN-CES-MIB", "tnCesClockRecoveryMaxDeviation"),
        ("TN-CES-MIB", "tnCesTDMPresentation"),
        ("TN-CES-MIB", "tnCesTDMFraming"),
        ("TN-CES-MIB", "tnCesTDMMode"),
        ("TN-CES-MIB", "tnCesTDMTS0Passthrough"),
        ("TN-CES-MIB", "tnCesTDMCRC4"),
        ("TN-CES-MIB", "tnCesTDMShutdownCallsOnFail"),
        ("TN-CES-MIB", "tnCesTDMImpedance"),
        ("TN-CES-MIB", "tnCesTDMT1Framing"),
        ("TN-CES-MIB", "tnCesTDMT1LineCode"),
        ("TN-CES-MIB", "tnCesTDMT1LoopCodeType"),
        ("TN-CES-MIB", "tnCesTDMT1LoopCodeRxEnable"),
        ("TN-CES-MIB", "tnCesTDMT1LoopCodeUserDown"),
        ("TN-CES-MIB", "tnCesTDMT1LoopCodeUserUp"),
        ("TN-CES-MIB", "tnCesTDMT1LoopCodeUserLength"),
        ("TN-CES-MIB", "tnCesTDMDTE"),
        ("TN-CES-MIB", "tnCesLLname"),
        ("TN-CES-MIB", "tnCesLLDirection"),
        ("TN-CES-MIB", "tnCesLLRemoteIpAddrType"),
        ("TN-CES-MIB", "tnCesLLRemoteIpAddr"),
        ("TN-CES-MIB", "tnCesLLSecondaryRemoteIpAddrType"),
        ("TN-CES-MIB", "tnCesLLSecondaryRemoteIpAddr"),
        ("TN-CES-MIB", "tnCesLLQosType"),
        ("TN-CES-MIB", "tnCesLLQosTOS"),
        ("TN-CES-MIB", "tnCesLLQosDiffserv"),
        ("TN-CES-MIB", "tnCesLLVlanTag"),
        ("TN-CES-MIB", "tnCesLLVlanId"),
        ("TN-CES-MIB", "tnCesLLVlanPriority"),
        ("TN-CES-MIB", "tnCesLLJitterBufferLength"),
        ("TN-CES-MIB", "tnCesLLFramesPerPacket"),
        ("TN-CES-MIB", "tnCesLLRemoteLinkNumber"),
        ("TN-CES-MIB", "tnCesLLSchedEnable"),
        ("TN-CES-MIB", "tnCesLLSchedStartTimeMonHours"),
        ("TN-CES-MIB", "tnCesLLSchedStartTimeMonMins"),
        ("TN-CES-MIB", "tnCesLLSchedStopTimeMonHours"),
        ("TN-CES-MIB", "tnCesLLSchedStopTimeMonMins"),
        ("TN-CES-MIB", "tnCesLLSchedStartTimeTueHours"),
        ("TN-CES-MIB", "tnCesLLSchedStartTimeTueMins"),
        ("TN-CES-MIB", "tnCesLLSchedStopTimeTueHours"),
        ("TN-CES-MIB", "tnCesLLSchedStopTimeTueMins"),
        ("TN-CES-MIB", "tnCesLLSchedStartTimeWedHours"),
        ("TN-CES-MIB", "tnCesLLSchedStartTimeWedMins"),
        ("TN-CES-MIB", "tnCesLLSchedStopTimeWedHours"),
        ("TN-CES-MIB", "tnCesLLSchedStopTimeWedMins"),
        ("TN-CES-MIB", "tnCesLLSchedStartTimeThuHours"),
        ("TN-CES-MIB", "tnCesLLSchedStartTimeThuMins"),
        ("TN-CES-MIB", "tnCesLLSchedStopTimeThuHours"),
        ("TN-CES-MIB", "tnCesLLSchedStopTimeThuMins"),
        ("TN-CES-MIB", "tnCesLLSchedStartTimeFriHours"),
        ("TN-CES-MIB", "tnCesLLSchedStartTimeFriMins"),
        ("TN-CES-MIB", "tnCesLLSchedStopTimeFriHours"),
        ("TN-CES-MIB", "tnCesLLSchedStopTimeFriMins"),
        ("TN-CES-MIB", "tnCesLLSchedStartTimeSatHours"),
        ("TN-CES-MIB", "tnCesLLSchedStartTimeSatMins"),
        ("TN-CES-MIB", "tnCesLLSchedStopTimeSatHours"),
        ("TN-CES-MIB", "tnCesLLSchedStopTimeSatMins"),
        ("TN-CES-MIB", "tnCesLLSchedStartTimeSunHours"),
        ("TN-CES-MIB", "tnCesLLSchedStartTimeSunMins"),
        ("TN-CES-MIB", "tnCesLLSchedStopTimeSunHours"),
        ("TN-CES-MIB", "tnCesLLSchedStopTimeSunMins"),
        ("TN-CES-MIB", "tnCesLLJitterAdjustmentMode"),
        ("TN-CES-MIB", "tnCesLLJitterAdjustmentAfter"),
        ("TN-CES-MIB", "tnCesLLJASchedStartTimeMonHours"),
        ("TN-CES-MIB", "tnCesLLJASchedStartTimeMonMins"),
        ("TN-CES-MIB", "tnCesLLJASchedStopTimeMonHours"),
        ("TN-CES-MIB", "tnCesLLJASchedStopTimeMonMins"),
        ("TN-CES-MIB", "tnCesLLJASchedStartTimeTueHours"),
        ("TN-CES-MIB", "tnCesLLJASchedStartTimeTueMins"),
        ("TN-CES-MIB", "tnCesLLJASchedStopTimeTueHours"),
        ("TN-CES-MIB", "tnCesLLJASchedStopTimeTueMins"),
        ("TN-CES-MIB", "tnCesLLJASchedStartTimeWedHours"),
        ("TN-CES-MIB", "tnCesLLJASchedStartTimeWedMins"),
        ("TN-CES-MIB", "tnCesLLJASchedStopTimeWedHours"),
        ("TN-CES-MIB", "tnCesLLJASchedStopTimeWedMins"),
        ("TN-CES-MIB", "tnCesLLJASchedStartTimeThuHours"),
        ("TN-CES-MIB", "tnCesLLJASchedStartTimeThuMins"),
        ("TN-CES-MIB", "tnCesLLJASchedStopTimeThuHours"),
        ("TN-CES-MIB", "tnCesLLJASchedStopTimeThuMins"),
        ("TN-CES-MIB", "tnCesLLJASchedStartTimeFriHours"),
        ("TN-CES-MIB", "tnCesLLJASchedStartTimeFriMins"),
        ("TN-CES-MIB", "tnCesLLJASchedStopTimeFriHours"),
        ("TN-CES-MIB", "tnCesLLJASchedStopTimeFriMins"),
        ("TN-CES-MIB", "tnCesLLJASchedStartTimeSatHours"),
        ("TN-CES-MIB", "tnCesLLJASchedStartTimeSatMins"),
        ("TN-CES-MIB", "tnCesLLJASchedStopTimeSatHours"),
        ("TN-CES-MIB", "tnCesLLJASchedStopTimeSatMins"),
        ("TN-CES-MIB", "tnCesLLJASchedStartTimeSunHours"),
        ("TN-CES-MIB", "tnCesLLJASchedStartTimeSunMins"),
        ("TN-CES-MIB", "tnCesLLJASchedStopTimeSunHours"),
        ("TN-CES-MIB", "tnCesLLJASchedStopTimeSunMins"),
        ("TN-CES-MIB", "tnCesLLChanSelectAvailable"),
        ("TN-CES-MIB", "tnCesLLChanSelectUsed"),
        ("TN-CES-MIB", "tnCesClockingAlternateEnable"),
        ("TN-CES-MIB", "tnCesLLPlesiosynchronous"),
        ("TN-CES-MIB", "tnCesLLAsymmetric"),
        ("TN-CES-MIB", "tnCesLLBytesPerPacketRx"),
        ("TN-CES-MIB", "tnCesLLBytesPerPacketTx"),
        ("TN-CES-MIB", "tnCesLLStatusEnabled"),
        ("TN-CES-MIB", "tnCesLLStatusActive"),
        ("TN-CES-MIB", "tnCesLLStatusArpResolved"),
        ("TN-CES-MIB", "tnCesLLStatusNumberOfChannels"),
        ("TN-CES-MIB", "tnCesLLStatusRemoteMac"),
        ("TN-CES-MIB", "tnCesLLStatusRemoteIpAddrType"),
        ("TN-CES-MIB", "tnCesLLStatusRemoteIpAddr"),
        ("TN-CES-MIB", "tnCesLLStatusRemoteContextKnown"),
        ("TN-CES-MIB", "tnCesLLStatusRemoteContextNumber"),
        ("TN-CES-MIB", "tnCesLLStatusRemotePortKnown"),
        ("TN-CES-MIB", "tnCesLLStatusRemotePort"),
        ("TN-CES-MIB", "tnCesLLStatusQueueLengthValid"),
        ("TN-CES-MIB", "tnCesLLStatusMinQueueLength"),
        ("TN-CES-MIB", "tnCesLLStatusMaxQueueLength"),
        ("TN-CES-MIB", "tnCesLLStatusAveQueueLengthWhole"),
        ("TN-CES-MIB", "tnCesLLStatusAveQueueLengthFrac"),
        ("TN-CES-MIB", "tnCesLLStatusEarly"),
        ("TN-CES-MIB", "tnCesLLStatusLate"),
        ("TN-CES-MIB", "tnCesLLStatusUnderrun"),
        ("TN-CES-MIB", "tnCesLLStatusLastSequence"),
        ("TN-CES-MIB", "tnCesLLStatusPacketsRx"),
        ("TN-CES-MIB", "tnCesLLStatusPacketsTx"),
        ("TN-CES-MIB", "tnCesLLStatusSlipsReduceCount"),
        ("TN-CES-MIB", "tnCesLLStatusSlipsExtendCount"),
        ("TN-CES-MIB", "tnCesLLLocalLoop"),
        ("TN-CES-MIB", "tnCesLLRemoteLoop"),
        ("TN-CES-MIB", "tnCesLLNudge"),
        ("TN-CES-MIB", "tnCesLLResetErrorStats"),
        ("TN-CES-MIB", "tnCesTDMStatusPhysical"),
        ("TN-CES-MIB", "tnCesTDMStatusRxSignalLevel"),
        ("TN-CES-MIB", "tnCesTDMStatusRxError"),
        ("TN-CES-MIB", "tnCesTDMLocalLoop"),
        ("TN-CES-MIB", "tnCesTDMRemoteLoop"),
        ("TN-CES-MIB", "tnCesTDMBreakCalls"),
        ("TN-CES-MIB", "tnCesProcessorVersion"),
        ("TN-CES-MIB", "tnCesProcessorProtocolMatch1"),
        ("TN-CES-MIB", "tnCesProcessorProtocolMatch2"),
        ("TN-CES-MIB", "tnCesProcessorProtocolMatch3"),
        ("TN-CES-MIB", "tnCesProcessorProtocolMatch4"),
        ("TN-CES-MIB", "tnCesProcessorProtocolNoMatch"),
        ("TN-CES-MIB", "tnCesProcessorClassifyFail"),
        ("TN-CES-MIB", "tnCesProcessorVerifyFail"),
        ("TN-CES-MIB", "tnCesProcessorIpv4ChecksumFail"),
        ("TN-CES-MIB", "tnCesProcessorUdpChecksumFail"),
        ("TN-CES-MIB", "tnCesCallStatusStartTime"),
        ("TN-CES-MIB", "tnCesCallStatusSource"),
        ("TN-CES-MIB", "tnCesCallStatusDestination"),
        ("TN-CES-MIB", "tnCesCallStatusOriginator"),
        ("TN-CES-MIB", "tnCesCallStatusDestinationNumber"),
        ("TN-CES-MIB", "tnCesCallStatusSourceNumber"),
        ("TN-CES-MIB", "tnCesCallStatusState"),
        ("TN-CES-MIB", "tnCesClockStatusLock"),
        ("TN-CES-MIB", "tnCesClockStatusSlaveMode"),
        ("TN-CES-MIB", "tnCesClockStatusSource"),
        ("TN-CES-MIB", "tnCesClockStatusStreamStatus"),
        ("TN-CES-MIB", "tnCesClockStatusStreamMode"),
        ("TN-CES-MIB", "tnCesClockStatusStreamDCO"),
        ("TN-CES-MIB", "tnCesClockStatusStreamDCOMin"),
        ("TN-CES-MIB", "tnCesClockStatusStreamDCOMax"),
        ("TN-CES-MIB", "tnCesClockStatusStreamDCOAvg"),
        ("TN-CES-MIB", "tnCesTemperatureBoardWhole"),
        ("TN-CES-MIB", "tnCesTemperatureBoardFrac"),
        ("TN-CES-MIB", "tnCesTemperatureProcessorWhole"),
        ("TN-CES-MIB", "tnCesTemperatureProcessorFrac"),
        ("TN-CES-MIB", "tnCesDebugTDMPortEnable"),
        ("TN-CES-MIB", "tnCesDebugLLEnable"),
        ("TN-CES-MIB", "tnCesDebugMiscEnable"),
        ("TN-CES-MIB", "tnCesEventDetails"),
        ("TN-CES-MIB", "tnCesEventPriority"),
        ("TN-CES-MIB", "tnCesRS530Rate"),
        ("TN-CES-MIB", "tnCesRS530ShutdownCallsOnFail"),
        ("TN-CES-MIB", "tnCesRS530InterfaceType"),
        ("TN-CES-MIB", "tnCesRS530StatusDTR"),
        ("TN-CES-MIB", "tnCesRS530StatusDCD"),
        ("TN-CES-MIB", "tnCesRS530StatusRTS"),
        ("TN-CES-MIB", "tnCesRS530StatusCTS"),
        ("TN-CES-MIB", "tnCesRS530StatusDSR"),
        ("TN-CES-MIB", "tnCesRS530LocalLoop"),
        ("TN-CES-MIB", "tnCesRS530RemoteLoop"),
        ("TN-CES-MIB", "tnCesRS530BreakCalls"),
        ("TN-CES-MIB", "tnCesIpv4AddrType"),
        ("TN-CES-MIB", "tnCesIpv4Addr"),
        ("TN-CES-MIB", "tnCesIpv4PrefixLength"),
        ("TN-CES-MIB", "tnCesIpv6AddrType"),
        ("TN-CES-MIB", "tnCesIpv6Addr"),
        ("TN-CES-MIB", "tnCesIpv6PrefixLength"))
)
if mibBuilder.loadTexts:
    tnCesGroup.setStatus("current")


# Notification objects

tnCesGeneralEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 0, 3, 0, 1)
)
tnCesGeneralEvent.setObjects(
      *(("TN-CES-MIB", "tnCesEventDetails"),
        ("TN-CES-MIB", "tnCesEventPriority"))
)
if mibBuilder.loadTexts:
    tnCesGeneralEvent.setStatus(
        "current"
    )


# Notifications groups

tnCesTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 2, 2, 2)
)
tnCesTrapGroup.setObjects(
    ("TN-CES-MIB", "tnCesGeneralEvent")
)
if mibBuilder.loadTexts:
    tnCesTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tnCesMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 60, 2, 1, 1)
)
tnCesMIBCompliance.setObjects(
      *(("TN-CES-MIB", "tnCesGroup"),
        ("TN-CES-MIB", "tnCesTrapGroup"))
)
if mibBuilder.loadTexts:
    tnCesMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-CES-MIB",
    **{"tnCesMIB": tnCesMIB,
       "tnCesNotifications": tnCesNotifications,
       "tnCesEventDetails": tnCesEventDetails,
       "tnCesEventPriority": tnCesEventPriority,
       "tnCesEventId": tnCesEventId,
       "tnCesEventIdGeneral": tnCesEventIdGeneral,
       "tnCesGeneralEvent": tnCesGeneralEvent,
       "tnCesObjects": tnCesObjects,
       "tnCesProtocol": tnCesProtocol,
       "tnCesProtocolType": tnCesProtocolType,
       "tnCesProtocolUnderrunFixed": tnCesProtocolUnderrunFixed,
       "tnCesProtocolUnderrunValue": tnCesProtocolUnderrunValue,
       "tnCesProtocolUDPBasePort": tnCesProtocolUDPBasePort,
       "tnCesProtocolEnableSSRCChecking": tnCesProtocolEnableSSRCChecking,
       "tnCesClockingAlternate": tnCesClockingAlternate,
       "tnCesClockingAlternateEnable": tnCesClockingAlternateEnable,
       "tnCesClockRecovery": tnCesClockRecovery,
       "tnCesClockRecoveryAlgorithm": tnCesClockRecoveryAlgorithm,
       "tnCesClockRecoveryFilter": tnCesClockRecoveryFilter,
       "tnCesClockRecoveryMaxDeviation": tnCesClockRecoveryMaxDeviation,
       "tnCesEvent": tnCesEvent,
       "tnCesEventThreshold": tnCesEventThreshold,
       "tnCesEventReportingInterval": tnCesEventReportingInterval,
       "tnCesEventThresholdEarly": tnCesEventThresholdEarly,
       "tnCesEventThresholdLate": tnCesEventThresholdLate,
       "tnCesEventThresholdUnderrun": tnCesEventThresholdUnderrun,
       "tnCesEventThresholdDCO": tnCesEventThresholdDCO,
       "tnCesProcessor": tnCesProcessor,
       "tnCesProcessorVersion": tnCesProcessorVersion,
       "tnCesProcessorProtocolMatch1": tnCesProcessorProtocolMatch1,
       "tnCesProcessorProtocolMatch2": tnCesProcessorProtocolMatch2,
       "tnCesProcessorProtocolMatch3": tnCesProcessorProtocolMatch3,
       "tnCesProcessorProtocolMatch4": tnCesProcessorProtocolMatch4,
       "tnCesProcessorProtocolNoMatch": tnCesProcessorProtocolNoMatch,
       "tnCesProcessorClassifyFail": tnCesProcessorClassifyFail,
       "tnCesProcessorVerifyFail": tnCesProcessorVerifyFail,
       "tnCesProcessorIpv4ChecksumFail": tnCesProcessorIpv4ChecksumFail,
       "tnCesProcessorUdpChecksumFail": tnCesProcessorUdpChecksumFail,
       "tnCesClockStatus": tnCesClockStatus,
       "tnCesClockStatusLock": tnCesClockStatusLock,
       "tnCesClockStatusSlaveMode": tnCesClockStatusSlaveMode,
       "tnCesClockStatusSource": tnCesClockStatusSource,
       "tnCesTemperature": tnCesTemperature,
       "tnCesTemperatureBoardWhole": tnCesTemperatureBoardWhole,
       "tnCesTemperatureBoardFrac": tnCesTemperatureBoardFrac,
       "tnCesTemperatureProcessorWhole": tnCesTemperatureProcessorWhole,
       "tnCesTemperatureProcessorFrac": tnCesTemperatureProcessorFrac,
       "tnCesIP": tnCesIP,
       "tnCesIpv4AddrType": tnCesIpv4AddrType,
       "tnCesIpv4Addr": tnCesIpv4Addr,
       "tnCesIpv4PrefixLength": tnCesIpv4PrefixLength,
       "tnCesIpv6AddrType": tnCesIpv6AddrType,
       "tnCesIpv6Addr": tnCesIpv6Addr,
       "tnCesIpv6PrefixLength": tnCesIpv6PrefixLength,
       "tnCesClockPriority": tnCesClockPriority,
       "tnCesMiscClockPriorityTable": tnCesMiscClockPriorityTable,
       "tnCesMiscClockPriorityEntry": tnCesMiscClockPriorityEntry,
       "tnCesMiscClockPriorityItem": tnCesMiscClockPriorityItem,
       "tnCesMiscClockPriority": tnCesMiscClockPriority,
       "tnCesPRIClockPriorityTable": tnCesPRIClockPriorityTable,
       "tnCesPRIClockPriorityEntry": tnCesPRIClockPriorityEntry,
       "tnCesPRIClockPriorityIndex": tnCesPRIClockPriorityIndex,
       "tnCesPRIClockPriority": tnCesPRIClockPriority,
       "tnCesLLClockPriorityTable": tnCesLLClockPriorityTable,
       "tnCesLLClockPriorityEntry": tnCesLLClockPriorityEntry,
       "tnCesLLClockPriorityIndex": tnCesLLClockPriorityIndex,
       "tnCesLLClockPriority": tnCesLLClockPriority,
       "tnCesMulticastJoinTable": tnCesMulticastJoinTable,
       "tnCesMulticastJoinEntry": tnCesMulticastJoinEntry,
       "tnCesMulticastJoinIndex": tnCesMulticastJoinIndex,
       "tnCesMulticastJoinAction": tnCesMulticastJoinAction,
       "tnCesMulticastJoinAddrType": tnCesMulticastJoinAddrType,
       "tnCesMulticastJoinAddr": tnCesMulticastJoinAddr,
       "tnCesTDMTable": tnCesTDMTable,
       "tnCesTDMEntry": tnCesTDMEntry,
       "tnCesTDMPortNumber": tnCesTDMPortNumber,
       "tnCesTDMPresentation": tnCesTDMPresentation,
       "tnCesTDMFraming": tnCesTDMFraming,
       "tnCesTDMMode": tnCesTDMMode,
       "tnCesTDMTS0Passthrough": tnCesTDMTS0Passthrough,
       "tnCesTDMCRC4": tnCesTDMCRC4,
       "tnCesTDMShutdownCallsOnFail": tnCesTDMShutdownCallsOnFail,
       "tnCesTDMImpedance": tnCesTDMImpedance,
       "tnCesTDMT1Framing": tnCesTDMT1Framing,
       "tnCesTDMT1LineCode": tnCesTDMT1LineCode,
       "tnCesTDMT1LoopCodeType": tnCesTDMT1LoopCodeType,
       "tnCesTDMT1LoopCodeRxEnable": tnCesTDMT1LoopCodeRxEnable,
       "tnCesTDMT1LoopCodeUserUp": tnCesTDMT1LoopCodeUserUp,
       "tnCesTDMT1LoopCodeUserDown": tnCesTDMT1LoopCodeUserDown,
       "tnCesTDMT1LoopCodeUserLength": tnCesTDMT1LoopCodeUserLength,
       "tnCesTDMDTE": tnCesTDMDTE,
       "tnCesLLTable": tnCesLLTable,
       "tnCesLLEntry": tnCesLLEntry,
       "tnCesLLNumber": tnCesLLNumber,
       "tnCesLLname": tnCesLLname,
       "tnCesLLDirection": tnCesLLDirection,
       "tnCesLLRemoteIpAddrType": tnCesLLRemoteIpAddrType,
       "tnCesLLRemoteIpAddr": tnCesLLRemoteIpAddr,
       "tnCesLLSecondaryRemoteIpAddrType": tnCesLLSecondaryRemoteIpAddrType,
       "tnCesLLSecondaryRemoteIpAddr": tnCesLLSecondaryRemoteIpAddr,
       "tnCesLLQosType": tnCesLLQosType,
       "tnCesLLQosTOS": tnCesLLQosTOS,
       "tnCesLLQosDiffserv": tnCesLLQosDiffserv,
       "tnCesLLVlanTag": tnCesLLVlanTag,
       "tnCesLLVlanId": tnCesLLVlanId,
       "tnCesLLVlanPriority": tnCesLLVlanPriority,
       "tnCesLLJitterBufferLength": tnCesLLJitterBufferLength,
       "tnCesLLFramesPerPacket": tnCesLLFramesPerPacket,
       "tnCesLLRemoteLinkNumber": tnCesLLRemoteLinkNumber,
       "tnCesLLSchedTable": tnCesLLSchedTable,
       "tnCesLLSchedEntry": tnCesLLSchedEntry,
       "tnCesLLSchedNumber": tnCesLLSchedNumber,
       "tnCesLLSchedEnable": tnCesLLSchedEnable,
       "tnCesLLSchedStartTimeMonHours": tnCesLLSchedStartTimeMonHours,
       "tnCesLLSchedStartTimeMonMins": tnCesLLSchedStartTimeMonMins,
       "tnCesLLSchedStopTimeMonHours": tnCesLLSchedStopTimeMonHours,
       "tnCesLLSchedStopTimeMonMins": tnCesLLSchedStopTimeMonMins,
       "tnCesLLSchedStartTimeTueHours": tnCesLLSchedStartTimeTueHours,
       "tnCesLLSchedStartTimeTueMins": tnCesLLSchedStartTimeTueMins,
       "tnCesLLSchedStopTimeTueHours": tnCesLLSchedStopTimeTueHours,
       "tnCesLLSchedStopTimeTueMins": tnCesLLSchedStopTimeTueMins,
       "tnCesLLSchedStartTimeWedHours": tnCesLLSchedStartTimeWedHours,
       "tnCesLLSchedStartTimeWedMins": tnCesLLSchedStartTimeWedMins,
       "tnCesLLSchedStopTimeWedHours": tnCesLLSchedStopTimeWedHours,
       "tnCesLLSchedStopTimeWedMins": tnCesLLSchedStopTimeWedMins,
       "tnCesLLSchedStartTimeThuHours": tnCesLLSchedStartTimeThuHours,
       "tnCesLLSchedStartTimeThuMins": tnCesLLSchedStartTimeThuMins,
       "tnCesLLSchedStopTimeThuHours": tnCesLLSchedStopTimeThuHours,
       "tnCesLLSchedStopTimeThuMins": tnCesLLSchedStopTimeThuMins,
       "tnCesLLSchedStartTimeFriHours": tnCesLLSchedStartTimeFriHours,
       "tnCesLLSchedStartTimeFriMins": tnCesLLSchedStartTimeFriMins,
       "tnCesLLSchedStopTimeFriHours": tnCesLLSchedStopTimeFriHours,
       "tnCesLLSchedStopTimeFriMins": tnCesLLSchedStopTimeFriMins,
       "tnCesLLSchedStartTimeSatHours": tnCesLLSchedStartTimeSatHours,
       "tnCesLLSchedStartTimeSatMins": tnCesLLSchedStartTimeSatMins,
       "tnCesLLSchedStopTimeSatHours": tnCesLLSchedStopTimeSatHours,
       "tnCesLLSchedStopTimeSatMins": tnCesLLSchedStopTimeSatMins,
       "tnCesLLSchedStartTimeSunHours": tnCesLLSchedStartTimeSunHours,
       "tnCesLLSchedStartTimeSunMins": tnCesLLSchedStartTimeSunMins,
       "tnCesLLSchedStopTimeSunHours": tnCesLLSchedStopTimeSunHours,
       "tnCesLLSchedStopTimeSunMins": tnCesLLSchedStopTimeSunMins,
       "tnCesLLJATable": tnCesLLJATable,
       "tnCesLLJAEntry": tnCesLLJAEntry,
       "tnCesLLJANumber": tnCesLLJANumber,
       "tnCesLLJitterAdjustmentMode": tnCesLLJitterAdjustmentMode,
       "tnCesLLJitterAdjustmentAfter": tnCesLLJitterAdjustmentAfter,
       "tnCesLLJASchedStartTimeMonHours": tnCesLLJASchedStartTimeMonHours,
       "tnCesLLJASchedStartTimeMonMins": tnCesLLJASchedStartTimeMonMins,
       "tnCesLLJASchedStopTimeMonHours": tnCesLLJASchedStopTimeMonHours,
       "tnCesLLJASchedStopTimeMonMins": tnCesLLJASchedStopTimeMonMins,
       "tnCesLLJASchedStartTimeTueHours": tnCesLLJASchedStartTimeTueHours,
       "tnCesLLJASchedStartTimeTueMins": tnCesLLJASchedStartTimeTueMins,
       "tnCesLLJASchedStopTimeTueHours": tnCesLLJASchedStopTimeTueHours,
       "tnCesLLJASchedStopTimeTueMins": tnCesLLJASchedStopTimeTueMins,
       "tnCesLLJASchedStartTimeWedHours": tnCesLLJASchedStartTimeWedHours,
       "tnCesLLJASchedStartTimeWedMins": tnCesLLJASchedStartTimeWedMins,
       "tnCesLLJASchedStopTimeWedHours": tnCesLLJASchedStopTimeWedHours,
       "tnCesLLJASchedStopTimeWedMins": tnCesLLJASchedStopTimeWedMins,
       "tnCesLLJASchedStartTimeThuHours": tnCesLLJASchedStartTimeThuHours,
       "tnCesLLJASchedStartTimeThuMins": tnCesLLJASchedStartTimeThuMins,
       "tnCesLLJASchedStopTimeThuHours": tnCesLLJASchedStopTimeThuHours,
       "tnCesLLJASchedStopTimeThuMins": tnCesLLJASchedStopTimeThuMins,
       "tnCesLLJASchedStartTimeFriHours": tnCesLLJASchedStartTimeFriHours,
       "tnCesLLJASchedStartTimeFriMins": tnCesLLJASchedStartTimeFriMins,
       "tnCesLLJASchedStopTimeFriHours": tnCesLLJASchedStopTimeFriHours,
       "tnCesLLJASchedStopTimeFriMins": tnCesLLJASchedStopTimeFriMins,
       "tnCesLLJASchedStartTimeSatHours": tnCesLLJASchedStartTimeSatHours,
       "tnCesLLJASchedStartTimeSatMins": tnCesLLJASchedStartTimeSatMins,
       "tnCesLLJASchedStopTimeSatHours": tnCesLLJASchedStopTimeSatHours,
       "tnCesLLJASchedStopTimeSatMins": tnCesLLJASchedStopTimeSatMins,
       "tnCesLLJASchedStartTimeSunHours": tnCesLLJASchedStartTimeSunHours,
       "tnCesLLJASchedStartTimeSunMins": tnCesLLJASchedStartTimeSunMins,
       "tnCesLLJASchedStopTimeSunHours": tnCesLLJASchedStopTimeSunHours,
       "tnCesLLJASchedStopTimeSunMins": tnCesLLJASchedStopTimeSunMins,
       "tnCesLLChanSelectTable": tnCesLLChanSelectTable,
       "tnCesLLChanSelectEntry": tnCesLLChanSelectEntry,
       "tnCesLLChanSelectLLNumber": tnCesLLChanSelectLLNumber,
       "tnCesLLChanSelectPortNumber": tnCesLLChanSelectPortNumber,
       "tnCesLLChanSelectAvailable": tnCesLLChanSelectAvailable,
       "tnCesLLChanSelectUsed": tnCesLLChanSelectUsed,
       "tnCesLLAlternateTable": tnCesLLAlternateTable,
       "tnCesLLAlternateEntry": tnCesLLAlternateEntry,
       "tnCesLLAlternateLLNumber": tnCesLLAlternateLLNumber,
       "tnCesLLPlesiosynchronous": tnCesLLPlesiosynchronous,
       "tnCesLLAsymmetric": tnCesLLAsymmetric,
       "tnCesLLBytesPerPacketRx": tnCesLLBytesPerPacketRx,
       "tnCesLLBytesPerPacketTx": tnCesLLBytesPerPacketTx,
       "tnCesLLStatusTable": tnCesLLStatusTable,
       "tnCesLLStatusEntry": tnCesLLStatusEntry,
       "tnCesLLStatusNumber": tnCesLLStatusNumber,
       "tnCesLLStatusEnabled": tnCesLLStatusEnabled,
       "tnCesLLStatusActive": tnCesLLStatusActive,
       "tnCesLLStatusArpResolved": tnCesLLStatusArpResolved,
       "tnCesLLStatusNumberOfChannels": tnCesLLStatusNumberOfChannels,
       "tnCesLLStatusRemoteMac": tnCesLLStatusRemoteMac,
       "tnCesLLStatusRemoteIpAddrType": tnCesLLStatusRemoteIpAddrType,
       "tnCesLLStatusRemoteIpAddr": tnCesLLStatusRemoteIpAddr,
       "tnCesLLStatusRemoteContextKnown": tnCesLLStatusRemoteContextKnown,
       "tnCesLLStatusRemoteContextNumber": tnCesLLStatusRemoteContextNumber,
       "tnCesLLStatusRemotePortKnown": tnCesLLStatusRemotePortKnown,
       "tnCesLLStatusRemotePort": tnCesLLStatusRemotePort,
       "tnCesLLStatusQueueLengthValid": tnCesLLStatusQueueLengthValid,
       "tnCesLLStatusMinQueueLength": tnCesLLStatusMinQueueLength,
       "tnCesLLStatusMaxQueueLength": tnCesLLStatusMaxQueueLength,
       "tnCesLLStatusAveQueueLengthWhole": tnCesLLStatusAveQueueLengthWhole,
       "tnCesLLStatusAveQueueLengthFrac": tnCesLLStatusAveQueueLengthFrac,
       "tnCesLLStatusEarly": tnCesLLStatusEarly,
       "tnCesLLStatusLate": tnCesLLStatusLate,
       "tnCesLLStatusUnderrun": tnCesLLStatusUnderrun,
       "tnCesLLStatusLastSequence": tnCesLLStatusLastSequence,
       "tnCesLLStatusPacketsRx": tnCesLLStatusPacketsRx,
       "tnCesLLStatusPacketsTx": tnCesLLStatusPacketsTx,
       "tnCesLLStatusSlipsReduceCount": tnCesLLStatusSlipsReduceCount,
       "tnCesLLStatusSlipsExtendCount": tnCesLLStatusSlipsExtendCount,
       "tnCesLLLocalLoop": tnCesLLLocalLoop,
       "tnCesLLRemoteLoop": tnCesLLRemoteLoop,
       "tnCesLLNudge": tnCesLLNudge,
       "tnCesLLResetErrorStats": tnCesLLResetErrorStats,
       "tnCesTDMStatusTable": tnCesTDMStatusTable,
       "tnCesTDMStatusEntry": tnCesTDMStatusEntry,
       "tnCesTDMStatusNumber": tnCesTDMStatusNumber,
       "tnCesTDMStatusPhysical": tnCesTDMStatusPhysical,
       "tnCesTDMStatusRxSignalLevel": tnCesTDMStatusRxSignalLevel,
       "tnCesTDMStatusRxError": tnCesTDMStatusRxError,
       "tnCesTDMLocalLoop": tnCesTDMLocalLoop,
       "tnCesTDMRemoteLoop": tnCesTDMRemoteLoop,
       "tnCesTDMBreakCalls": tnCesTDMBreakCalls,
       "tnCesCallStatusTable": tnCesCallStatusTable,
       "tnCesCallStatusEntry": tnCesCallStatusEntry,
       "tnCesCallStatusNumber": tnCesCallStatusNumber,
       "tnCesCallStatusStartTime": tnCesCallStatusStartTime,
       "tnCesCallStatusSource": tnCesCallStatusSource,
       "tnCesCallStatusDestination": tnCesCallStatusDestination,
       "tnCesCallStatusOriginator": tnCesCallStatusOriginator,
       "tnCesCallStatusDestinationNumber": tnCesCallStatusDestinationNumber,
       "tnCesCallStatusSourceNumber": tnCesCallStatusSourceNumber,
       "tnCesCallStatusState": tnCesCallStatusState,
       "tnCesClockStatusTable": tnCesClockStatusTable,
       "tnCesClockStatusEntry": tnCesClockStatusEntry,
       "tnCesClockStatusStreamNumber": tnCesClockStatusStreamNumber,
       "tnCesClockStatusStreamStatus": tnCesClockStatusStreamStatus,
       "tnCesClockStatusStreamMode": tnCesClockStatusStreamMode,
       "tnCesClockStatusStreamDCO": tnCesClockStatusStreamDCO,
       "tnCesClockStatusStreamDCOMin": tnCesClockStatusStreamDCOMin,
       "tnCesClockStatusStreamDCOMax": tnCesClockStatusStreamDCOMax,
       "tnCesClockStatusStreamDCOAvg": tnCesClockStatusStreamDCOAvg,
       "tnCesDebug": tnCesDebug,
       "tnCesDebugTDMTable": tnCesDebugTDMTable,
       "tnCesDebugTDMEntry": tnCesDebugTDMEntry,
       "tnCesDebugTDMPortNumber": tnCesDebugTDMPortNumber,
       "tnCesDebugTDMPortEnable": tnCesDebugTDMPortEnable,
       "tnCesDebugLLTable": tnCesDebugLLTable,
       "tnCesDebugLLEntry": tnCesDebugLLEntry,
       "tnCesDebugLLNumber": tnCesDebugLLNumber,
       "tnCesDebugLLEnable": tnCesDebugLLEnable,
       "tnCesDebugMiscTable": tnCesDebugMiscTable,
       "tnCesDebugMiscEntry": tnCesDebugMiscEntry,
       "tnCesDebugMiscItem": tnCesDebugMiscItem,
       "tnCesDebugMiscEnable": tnCesDebugMiscEnable,
       "tnCesRS530Table": tnCesRS530Table,
       "tnCesRS530Entry": tnCesRS530Entry,
       "tnCesRS530PortNumber": tnCesRS530PortNumber,
       "tnCesRS530Rate": tnCesRS530Rate,
       "tnCesRS530ShutdownCallsOnFail": tnCesRS530ShutdownCallsOnFail,
       "tnCesRS530StatusTable": tnCesRS530StatusTable,
       "tnCesRS530StatusEntry": tnCesRS530StatusEntry,
       "tnCesRS530StatusNumber": tnCesRS530StatusNumber,
       "tnCesRS530InterfaceType": tnCesRS530InterfaceType,
       "tnCesRS530StatusDTR": tnCesRS530StatusDTR,
       "tnCesRS530StatusDCD": tnCesRS530StatusDCD,
       "tnCesRS530StatusRTS": tnCesRS530StatusRTS,
       "tnCesRS530StatusCTS": tnCesRS530StatusCTS,
       "tnCesRS530StatusDSR": tnCesRS530StatusDSR,
       "tnCesRS530LocalLoop": tnCesRS530LocalLoop,
       "tnCesRS530RemoteLoop": tnCesRS530RemoteLoop,
       "tnCesRS530BreakCalls": tnCesRS530BreakCalls,
       "tnCesConformance": tnCesConformance,
       "tnCesCompliances": tnCesCompliances,
       "tnCesMIBCompliance": tnCesMIBCompliance,
       "tnCesGroups": tnCesGroups,
       "tnCesGroup": tnCesGroup,
       "tnCesTrapGroup": tnCesTrapGroup}
)
