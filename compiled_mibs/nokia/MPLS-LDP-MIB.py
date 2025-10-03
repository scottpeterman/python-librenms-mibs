# SNMP MIB module (MPLS-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\MPLS-LDP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:11 2025
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mplsLdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65)
)
if mibBuilder.loadTexts:
    mplsLdpMIB.setRevisions(
        ("2006-01-04 00:00",
         "2000-03-04 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsLsrIdentifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class MplsLdpGenAddr(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class MplsLabel(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class MplsLdpIdentifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



class MplsLdpLabelTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("generic", 1),
          ("atm", 2),
          ("frameRelay", 3))
    )



class AtmVcIdentifier(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class AtmVpIdentifier(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



# MIB Managed Objects in the order of their OIDs

_MplsLdpObjects_ObjectIdentity = ObjectIdentity
mplsLdpObjects = _MplsLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1)
)
_MplsLdpLsrObjects_ObjectIdentity = ObjectIdentity
mplsLdpLsrObjects = _MplsLdpLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 1)
)
_MplsLdpLsrId_Type = MplsLsrIdentifier
_MplsLdpLsrId_Object = MibScalar
mplsLdpLsrId = _MplsLdpLsrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 1, 1),
    _MplsLdpLsrId_Type()
)
mplsLdpLsrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLsrId.setStatus("current")


class _MplsLdpLsrLabelRetentionMode_Type(Integer32):
    """Custom type mplsLdpLsrLabelRetentionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conservative", 1),
          ("liberal", 2))
    )


_MplsLdpLsrLabelRetentionMode_Type.__name__ = "Integer32"
_MplsLdpLsrLabelRetentionMode_Object = MibScalar
mplsLdpLsrLabelRetentionMode = _MplsLdpLsrLabelRetentionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 1, 2),
    _MplsLdpLsrLabelRetentionMode_Type()
)
mplsLdpLsrLabelRetentionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsLdpLsrLabelRetentionMode.setStatus("current")


class _MplsLdpLsrLoopDetectionCapable_Type(Integer32):
    """Custom type mplsLdpLsrLoopDetectionCapable based on Integer32"""
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
        *(("none", 1),
          ("other", 2),
          ("hopCount", 3),
          ("pathVector", 4),
          ("hopCountAndPathVector", 5))
    )


_MplsLdpLsrLoopDetectionCapable_Type.__name__ = "Integer32"
_MplsLdpLsrLoopDetectionCapable_Object = MibScalar
mplsLdpLsrLoopDetectionCapable = _MplsLdpLsrLoopDetectionCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 1, 3),
    _MplsLdpLsrLoopDetectionCapable_Type()
)
mplsLdpLsrLoopDetectionCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLsrLoopDetectionCapable.setStatus("current")
_MplsLdpEntityObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityObjects = _MplsLdpEntityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2)
)


class _MplsLdpEntityIndexNext_Type(Unsigned32):
    """Custom type mplsLdpEntityIndexNext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MplsLdpEntityIndexNext_Type.__name__ = "Unsigned32"
_MplsLdpEntityIndexNext_Object = MibScalar
mplsLdpEntityIndexNext = _MplsLdpEntityIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 1),
    _MplsLdpEntityIndexNext_Type()
)
mplsLdpEntityIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityIndexNext.setStatus("current")
_MplsLdpEntityTable_Object = MibTable
mplsLdpEntityTable = _MplsLdpEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mplsLdpEntityTable.setStatus("current")
_MplsLdpEntityEntry_Object = MibTableRow
mplsLdpEntityEntry = _MplsLdpEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1)
)
mplsLdpEntityEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityEntry.setStatus("current")
_MplsLdpEntityLdpId_Type = MplsLdpIdentifier
_MplsLdpEntityLdpId_Object = MibTableColumn
mplsLdpEntityLdpId = _MplsLdpEntityLdpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 1),
    _MplsLdpEntityLdpId_Type()
)
mplsLdpEntityLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityLdpId.setStatus("current")


class _MplsLdpEntityIndex_Type(Unsigned32):
    """Custom type mplsLdpEntityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsLdpEntityIndex_Type.__name__ = "Unsigned32"
_MplsLdpEntityIndex_Object = MibTableColumn
mplsLdpEntityIndex = _MplsLdpEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 2),
    _MplsLdpEntityIndex_Type()
)
mplsLdpEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityIndex.setStatus("current")
_MplsLdpEntityProtocolVersion_Type = Integer32
_MplsLdpEntityProtocolVersion_Object = MibTableColumn
mplsLdpEntityProtocolVersion = _MplsLdpEntityProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 3),
    _MplsLdpEntityProtocolVersion_Type()
)
mplsLdpEntityProtocolVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityProtocolVersion.setStatus("current")


class _MplsLdpEntityAdminStatus_Type(Integer32):
    """Custom type mplsLdpEntityAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MplsLdpEntityAdminStatus_Type.__name__ = "Integer32"
_MplsLdpEntityAdminStatus_Object = MibTableColumn
mplsLdpEntityAdminStatus = _MplsLdpEntityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 4),
    _MplsLdpEntityAdminStatus_Type()
)
mplsLdpEntityAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAdminStatus.setStatus("current")


class _MplsLdpEntityOperStatus_Type(Integer32):
    """Custom type mplsLdpEntityOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("enabled", 1),
          ("disabled", 2))
    )


_MplsLdpEntityOperStatus_Type.__name__ = "Integer32"
_MplsLdpEntityOperStatus_Object = MibTableColumn
mplsLdpEntityOperStatus = _MplsLdpEntityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 5),
    _MplsLdpEntityOperStatus_Type()
)
mplsLdpEntityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityOperStatus.setStatus("current")
_MplsLdpEntityWellKnownDiscoveryPort_Type = Unsigned32
_MplsLdpEntityWellKnownDiscoveryPort_Object = MibTableColumn
mplsLdpEntityWellKnownDiscoveryPort = _MplsLdpEntityWellKnownDiscoveryPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 6),
    _MplsLdpEntityWellKnownDiscoveryPort_Type()
)
mplsLdpEntityWellKnownDiscoveryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityWellKnownDiscoveryPort.setStatus("current")


class _MplsLdpEntityMaxPduLength_Type(Unsigned32):
    """Custom type mplsLdpEntityMaxPduLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsLdpEntityMaxPduLength_Type.__name__ = "Unsigned32"
_MplsLdpEntityMaxPduLength_Object = MibTableColumn
mplsLdpEntityMaxPduLength = _MplsLdpEntityMaxPduLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 7),
    _MplsLdpEntityMaxPduLength_Type()
)
mplsLdpEntityMaxPduLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityMaxPduLength.setStatus("current")


class _MplsLdpEntityKeepAliveHoldTimer_Type(Integer32):
    """Custom type mplsLdpEntityKeepAliveHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpEntityKeepAliveHoldTimer_Type.__name__ = "Integer32"
_MplsLdpEntityKeepAliveHoldTimer_Object = MibTableColumn
mplsLdpEntityKeepAliveHoldTimer = _MplsLdpEntityKeepAliveHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 8),
    _MplsLdpEntityKeepAliveHoldTimer_Type()
)
mplsLdpEntityKeepAliveHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityKeepAliveHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpEntityKeepAliveHoldTimer.setUnits("seconds")


class _MplsLdpEntityHelloHoldTimer_Type(Integer32):
    """Custom type mplsLdpEntityHelloHoldTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsLdpEntityHelloHoldTimer_Type.__name__ = "Integer32"
_MplsLdpEntityHelloHoldTimer_Object = MibTableColumn
mplsLdpEntityHelloHoldTimer = _MplsLdpEntityHelloHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 9),
    _MplsLdpEntityHelloHoldTimer_Type()
)
mplsLdpEntityHelloHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityHelloHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    mplsLdpEntityHelloHoldTimer.setUnits("seconds")


class _MplsLdpEntityFailedInitSessionTrapEnable_Type(Integer32):
    """Custom type mplsLdpEntityFailedInitSessionTrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_MplsLdpEntityFailedInitSessionTrapEnable_Type.__name__ = "Integer32"
_MplsLdpEntityFailedInitSessionTrapEnable_Object = MibTableColumn
mplsLdpEntityFailedInitSessionTrapEnable = _MplsLdpEntityFailedInitSessionTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 10),
    _MplsLdpEntityFailedInitSessionTrapEnable_Type()
)
mplsLdpEntityFailedInitSessionTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFailedInitSessionTrapEnable.setStatus("current")
_MplsLdpEntityFailedInitSessionThreshold_Type = Integer32
_MplsLdpEntityFailedInitSessionThreshold_Object = MibTableColumn
mplsLdpEntityFailedInitSessionThreshold = _MplsLdpEntityFailedInitSessionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 11),
    _MplsLdpEntityFailedInitSessionThreshold_Type()
)
mplsLdpEntityFailedInitSessionThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFailedInitSessionThreshold.setStatus("current")


class _MplsLdpEntityLabelDistributionMethod_Type(Integer32):
    """Custom type mplsLdpEntityLabelDistributionMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstreamOnDemand", 1),
          ("downstreamUnsolicited", 2))
    )


_MplsLdpEntityLabelDistributionMethod_Type.__name__ = "Integer32"
_MplsLdpEntityLabelDistributionMethod_Object = MibTableColumn
mplsLdpEntityLabelDistributionMethod = _MplsLdpEntityLabelDistributionMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 12),
    _MplsLdpEntityLabelDistributionMethod_Type()
)
mplsLdpEntityLabelDistributionMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityLabelDistributionMethod.setStatus("current")


class _MplsLdpEntityPVLimitMismatchTrapEnable_Type(Integer32):
    """Custom type mplsLdpEntityPVLimitMismatchTrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_MplsLdpEntityPVLimitMismatchTrapEnable_Type.__name__ = "Integer32"
_MplsLdpEntityPVLimitMismatchTrapEnable_Object = MibTableColumn
mplsLdpEntityPVLimitMismatchTrapEnable = _MplsLdpEntityPVLimitMismatchTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 13),
    _MplsLdpEntityPVLimitMismatchTrapEnable_Type()
)
mplsLdpEntityPVLimitMismatchTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityPVLimitMismatchTrapEnable.setStatus("current")


class _MplsLdpEntityPathVectorLimit_Type(Integer32):
    """Custom type mplsLdpEntityPathVectorLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsLdpEntityPathVectorLimit_Type.__name__ = "Integer32"
_MplsLdpEntityPathVectorLimit_Object = MibTableColumn
mplsLdpEntityPathVectorLimit = _MplsLdpEntityPathVectorLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 14),
    _MplsLdpEntityPathVectorLimit_Type()
)
mplsLdpEntityPathVectorLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityPathVectorLimit.setStatus("current")


class _MplsLdpEntityHopCountLoopDetection_Type(Integer32):
    """Custom type mplsLdpEntityHopCountLoopDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MplsLdpEntityHopCountLoopDetection_Type.__name__ = "Integer32"
_MplsLdpEntityHopCountLoopDetection_Object = MibTableColumn
mplsLdpEntityHopCountLoopDetection = _MplsLdpEntityHopCountLoopDetection_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 15),
    _MplsLdpEntityHopCountLoopDetection_Type()
)
mplsLdpEntityHopCountLoopDetection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityHopCountLoopDetection.setStatus("current")


class _MplsLdpEntityHopCount_Type(Unsigned32):
    """Custom type mplsLdpEntityHopCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsLdpEntityHopCount_Type.__name__ = "Unsigned32"
_MplsLdpEntityHopCount_Object = MibTableColumn
mplsLdpEntityHopCount = _MplsLdpEntityHopCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 16),
    _MplsLdpEntityHopCount_Type()
)
mplsLdpEntityHopCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityHopCount.setStatus("current")


class _MplsLdpEntityTargetedPeer_Type(TruthValue):
    """Custom type mplsLdpEntityTargetedPeer based on TruthValue"""
    defaultValue = 2


_MplsLdpEntityTargetedPeer_Type.__name__ = "TruthValue"
_MplsLdpEntityTargetedPeer_Object = MibTableColumn
mplsLdpEntityTargetedPeer = _MplsLdpEntityTargetedPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 17),
    _MplsLdpEntityTargetedPeer_Type()
)
mplsLdpEntityTargetedPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityTargetedPeer.setStatus("current")
_MplsLdpEntityTargetedPeerAddrType_Type = AddressFamilyNumbers
_MplsLdpEntityTargetedPeerAddrType_Object = MibTableColumn
mplsLdpEntityTargetedPeerAddrType = _MplsLdpEntityTargetedPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 18),
    _MplsLdpEntityTargetedPeerAddrType_Type()
)
mplsLdpEntityTargetedPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityTargetedPeerAddrType.setStatus("current")
_MplsLdpEntityTargetedPeerAddr_Type = MplsLdpGenAddr
_MplsLdpEntityTargetedPeerAddr_Object = MibTableColumn
mplsLdpEntityTargetedPeerAddr = _MplsLdpEntityTargetedPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 19),
    _MplsLdpEntityTargetedPeerAddr_Type()
)
mplsLdpEntityTargetedPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityTargetedPeerAddr.setStatus("current")
_MplsLdpEntityOptionalParameters_Type = MplsLdpLabelTypes
_MplsLdpEntityOptionalParameters_Object = MibTableColumn
mplsLdpEntityOptionalParameters = _MplsLdpEntityOptionalParameters_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 20),
    _MplsLdpEntityOptionalParameters_Type()
)
mplsLdpEntityOptionalParameters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityOptionalParameters.setStatus("current")
_MplsLdpEntityDiscontinuityTime_Type = TimeStamp
_MplsLdpEntityDiscontinuityTime_Object = MibTableColumn
mplsLdpEntityDiscontinuityTime = _MplsLdpEntityDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 21),
    _MplsLdpEntityDiscontinuityTime_Type()
)
mplsLdpEntityDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpEntityDiscontinuityTime.setStatus("current")
_MplsLdpEntityStorageType_Type = StorageType
_MplsLdpEntityStorageType_Object = MibTableColumn
mplsLdpEntityStorageType = _MplsLdpEntityStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 22),
    _MplsLdpEntityStorageType_Type()
)
mplsLdpEntityStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityStorageType.setStatus("current")
_MplsLdpEntityRowStatus_Type = RowStatus
_MplsLdpEntityRowStatus_Object = MibTableColumn
mplsLdpEntityRowStatus = _MplsLdpEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 2, 1, 23),
    _MplsLdpEntityRowStatus_Type()
)
mplsLdpEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityRowStatus.setStatus("current")
_MplsLdpEntityGenericObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityGenericObjects = _MplsLdpEntityGenericObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 3)
)
_MplsLdpEntityConfGenericTable_Object = MibTable
mplsLdpEntityConfGenericTable = _MplsLdpEntityConfGenericTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityConfGenericTable.setStatus("current")
_MplsLdpEntityConfGenericEntry_Object = MibTableRow
mplsLdpEntityConfGenericEntry = _MplsLdpEntityConfGenericEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 3, 1, 1)
)
mplsLdpEntityConfGenericEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpConfGenericIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityConfGenericEntry.setStatus("current")


class _MplsLdpConfGenericIndex_Type(Unsigned32):
    """Custom type mplsLdpConfGenericIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsLdpConfGenericIndex_Type.__name__ = "Unsigned32"
_MplsLdpConfGenericIndex_Object = MibTableColumn
mplsLdpConfGenericIndex = _MplsLdpConfGenericIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 3, 1, 1, 1),
    _MplsLdpConfGenericIndex_Type()
)
mplsLdpConfGenericIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpConfGenericIndex.setStatus("current")
_MplsLdpConfGenericIfIndexOrZero_Type = InterfaceIndexOrZero
_MplsLdpConfGenericIfIndexOrZero_Object = MibTableColumn
mplsLdpConfGenericIfIndexOrZero = _MplsLdpConfGenericIfIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 3, 1, 1, 2),
    _MplsLdpConfGenericIfIndexOrZero_Type()
)
mplsLdpConfGenericIfIndexOrZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpConfGenericIfIndexOrZero.setStatus("current")


class _MplsLdpConfGenericLabel_Type(Unsigned32):
    """Custom type mplsLdpConfGenericLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_MplsLdpConfGenericLabel_Type.__name__ = "Unsigned32"
_MplsLdpConfGenericLabel_Object = MibTableColumn
mplsLdpConfGenericLabel = _MplsLdpConfGenericLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 3, 1, 1, 3),
    _MplsLdpConfGenericLabel_Type()
)
mplsLdpConfGenericLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpConfGenericLabel.setStatus("current")
_MplsLdpConfGenericStorageType_Type = StorageType
_MplsLdpConfGenericStorageType_Object = MibTableColumn
mplsLdpConfGenericStorageType = _MplsLdpConfGenericStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 3, 1, 1, 4),
    _MplsLdpConfGenericStorageType_Type()
)
mplsLdpConfGenericStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpConfGenericStorageType.setStatus("current")
_MplsLdpConfGenericRowStatus_Type = RowStatus
_MplsLdpConfGenericRowStatus_Object = MibTableColumn
mplsLdpConfGenericRowStatus = _MplsLdpConfGenericRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 3, 1, 1, 5),
    _MplsLdpConfGenericRowStatus_Type()
)
mplsLdpConfGenericRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpConfGenericRowStatus.setStatus("current")
_MplsLdpEntityAtmObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityAtmObjects = _MplsLdpEntityAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4)
)
_MplsLdpEntityAtmParmsTable_Object = MibTable
mplsLdpEntityAtmParmsTable = _MplsLdpEntityAtmParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityAtmParmsTable.setStatus("current")
_MplsLdpEntityAtmParmsEntry_Object = MibTableRow
mplsLdpEntityAtmParmsEntry = _MplsLdpEntityAtmParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 1, 1)
)
mplsLdpEntityAtmParmsEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityAtmParmsEntry.setStatus("current")
_MplsLdpEntityAtmIfIndexOrZero_Type = InterfaceIndexOrZero
_MplsLdpEntityAtmIfIndexOrZero_Object = MibTableColumn
mplsLdpEntityAtmIfIndexOrZero = _MplsLdpEntityAtmIfIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 1, 1, 1),
    _MplsLdpEntityAtmIfIndexOrZero_Type()
)
mplsLdpEntityAtmIfIndexOrZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmIfIndexOrZero.setStatus("current")


class _MplsLdpEntityAtmMergeCap_Type(Integer32):
    """Custom type mplsLdpEntityAtmMergeCap based on Integer32"""
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
        *(("notSupported", 0),
          ("vpMerge", 1),
          ("vcMerge", 2),
          ("vpAndVcMerge", 3))
    )


_MplsLdpEntityAtmMergeCap_Type.__name__ = "Integer32"
_MplsLdpEntityAtmMergeCap_Object = MibTableColumn
mplsLdpEntityAtmMergeCap = _MplsLdpEntityAtmMergeCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 1, 1, 2),
    _MplsLdpEntityAtmMergeCap_Type()
)
mplsLdpEntityAtmMergeCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmMergeCap.setStatus("current")


class _MplsLdpEntityAtmLabelRangeComponents_Type(Unsigned32):
    """Custom type mplsLdpEntityAtmLabelRangeComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpEntityAtmLabelRangeComponents_Type.__name__ = "Unsigned32"
_MplsLdpEntityAtmLabelRangeComponents_Object = MibTableColumn
mplsLdpEntityAtmLabelRangeComponents = _MplsLdpEntityAtmLabelRangeComponents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 1, 1, 3),
    _MplsLdpEntityAtmLabelRangeComponents_Type()
)
mplsLdpEntityAtmLabelRangeComponents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLabelRangeComponents.setStatus("current")


class _MplsLdpEntityAtmVcDirectionality_Type(Integer32):
    """Custom type mplsLdpEntityAtmVcDirectionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 0),
          ("unidirectional", 1))
    )


_MplsLdpEntityAtmVcDirectionality_Type.__name__ = "Integer32"
_MplsLdpEntityAtmVcDirectionality_Object = MibTableColumn
mplsLdpEntityAtmVcDirectionality = _MplsLdpEntityAtmVcDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 1, 1, 4),
    _MplsLdpEntityAtmVcDirectionality_Type()
)
mplsLdpEntityAtmVcDirectionality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmVcDirectionality.setStatus("current")


class _MplsLdpEntityAtmLsrConnectivity_Type(Integer32):
    """Custom type mplsLdpEntityAtmLsrConnectivity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("indirect", 2))
    )


_MplsLdpEntityAtmLsrConnectivity_Type.__name__ = "Integer32"
_MplsLdpEntityAtmLsrConnectivity_Object = MibTableColumn
mplsLdpEntityAtmLsrConnectivity = _MplsLdpEntityAtmLsrConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 1, 1, 5),
    _MplsLdpEntityAtmLsrConnectivity_Type()
)
mplsLdpEntityAtmLsrConnectivity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmLsrConnectivity.setStatus("current")


class _MplsLdpEntityDefaultControlVpi_Type(AtmVpIdentifier):
    """Custom type mplsLdpEntityDefaultControlVpi based on AtmVpIdentifier"""
    defaultValue = 0


_MplsLdpEntityDefaultControlVpi_Type.__name__ = "AtmVpIdentifier"
_MplsLdpEntityDefaultControlVpi_Object = MibTableColumn
mplsLdpEntityDefaultControlVpi = _MplsLdpEntityDefaultControlVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 1, 1, 6),
    _MplsLdpEntityDefaultControlVpi_Type()
)
mplsLdpEntityDefaultControlVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityDefaultControlVpi.setStatus("current")


class _MplsLdpEntityDefaultControlVci_Type(AtmVcIdentifier):
    """Custom type mplsLdpEntityDefaultControlVci based on AtmVcIdentifier"""
    defaultValue = 32


_MplsLdpEntityDefaultControlVci_Type.__name__ = "AtmVcIdentifier"
_MplsLdpEntityDefaultControlVci_Object = MibTableColumn
mplsLdpEntityDefaultControlVci = _MplsLdpEntityDefaultControlVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 1, 1, 7),
    _MplsLdpEntityDefaultControlVci_Type()
)
mplsLdpEntityDefaultControlVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityDefaultControlVci.setStatus("current")


class _MplsLdpEntityUnlabTrafVpi_Type(AtmVpIdentifier):
    """Custom type mplsLdpEntityUnlabTrafVpi based on AtmVpIdentifier"""
    defaultValue = 0


_MplsLdpEntityUnlabTrafVpi_Type.__name__ = "AtmVpIdentifier"
_MplsLdpEntityUnlabTrafVpi_Object = MibTableColumn
mplsLdpEntityUnlabTrafVpi = _MplsLdpEntityUnlabTrafVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 1, 1, 8),
    _MplsLdpEntityUnlabTrafVpi_Type()
)
mplsLdpEntityUnlabTrafVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityUnlabTrafVpi.setStatus("current")


class _MplsLdpEntityUnlabTrafVci_Type(AtmVcIdentifier):
    """Custom type mplsLdpEntityUnlabTrafVci based on AtmVcIdentifier"""
    defaultValue = 32


_MplsLdpEntityUnlabTrafVci_Type.__name__ = "AtmVcIdentifier"
_MplsLdpEntityUnlabTrafVci_Object = MibTableColumn
mplsLdpEntityUnlabTrafVci = _MplsLdpEntityUnlabTrafVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 1, 1, 9),
    _MplsLdpEntityUnlabTrafVci_Type()
)
mplsLdpEntityUnlabTrafVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityUnlabTrafVci.setStatus("current")
_MplsLdpEntityAtmStorageType_Type = StorageType
_MplsLdpEntityAtmStorageType_Object = MibTableColumn
mplsLdpEntityAtmStorageType = _MplsLdpEntityAtmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 1, 1, 10),
    _MplsLdpEntityAtmStorageType_Type()
)
mplsLdpEntityAtmStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmStorageType.setStatus("current")
_MplsLdpEntityAtmRowStatus_Type = RowStatus
_MplsLdpEntityAtmRowStatus_Object = MibTableColumn
mplsLdpEntityAtmRowStatus = _MplsLdpEntityAtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 1, 1, 11),
    _MplsLdpEntityAtmRowStatus_Type()
)
mplsLdpEntityAtmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityAtmRowStatus.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeTable_Object = MibTable
mplsLdpEntityConfAtmLabelRangeTable = _MplsLdpEntityConfAtmLabelRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeTable.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeEntry_Object = MibTableRow
mplsLdpEntityConfAtmLabelRangeEntry = _MplsLdpEntityConfAtmLabelRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 2, 1)
)
mplsLdpEntityConfAtmLabelRangeEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityConfAtmLabelRangeMinimumVpi"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityConfAtmLabelRangeMinimumVci"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeEntry.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeMinimumVpi_Type = AtmVpIdentifier
_MplsLdpEntityConfAtmLabelRangeMinimumVpi_Object = MibTableColumn
mplsLdpEntityConfAtmLabelRangeMinimumVpi = _MplsLdpEntityConfAtmLabelRangeMinimumVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 2, 1, 1),
    _MplsLdpEntityConfAtmLabelRangeMinimumVpi_Type()
)
mplsLdpEntityConfAtmLabelRangeMinimumVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeMinimumVpi.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeMinimumVci_Type = AtmVcIdentifier
_MplsLdpEntityConfAtmLabelRangeMinimumVci_Object = MibTableColumn
mplsLdpEntityConfAtmLabelRangeMinimumVci = _MplsLdpEntityConfAtmLabelRangeMinimumVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 2, 1, 2),
    _MplsLdpEntityConfAtmLabelRangeMinimumVci_Type()
)
mplsLdpEntityConfAtmLabelRangeMinimumVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeMinimumVci.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeMaximumVpi_Type = AtmVpIdentifier
_MplsLdpEntityConfAtmLabelRangeMaximumVpi_Object = MibTableColumn
mplsLdpEntityConfAtmLabelRangeMaximumVpi = _MplsLdpEntityConfAtmLabelRangeMaximumVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 2, 1, 3),
    _MplsLdpEntityConfAtmLabelRangeMaximumVpi_Type()
)
mplsLdpEntityConfAtmLabelRangeMaximumVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeMaximumVpi.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeMaximumVci_Type = AtmVcIdentifier
_MplsLdpEntityConfAtmLabelRangeMaximumVci_Object = MibTableColumn
mplsLdpEntityConfAtmLabelRangeMaximumVci = _MplsLdpEntityConfAtmLabelRangeMaximumVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 2, 1, 4),
    _MplsLdpEntityConfAtmLabelRangeMaximumVci_Type()
)
mplsLdpEntityConfAtmLabelRangeMaximumVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeMaximumVci.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeStorageType_Type = StorageType
_MplsLdpEntityConfAtmLabelRangeStorageType_Object = MibTableColumn
mplsLdpEntityConfAtmLabelRangeStorageType = _MplsLdpEntityConfAtmLabelRangeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 2, 1, 5),
    _MplsLdpEntityConfAtmLabelRangeStorageType_Type()
)
mplsLdpEntityConfAtmLabelRangeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeStorageType.setStatus("current")
_MplsLdpEntityConfAtmLabelRangeRowStatus_Type = RowStatus
_MplsLdpEntityConfAtmLabelRangeRowStatus_Object = MibTableColumn
mplsLdpEntityConfAtmLabelRangeRowStatus = _MplsLdpEntityConfAtmLabelRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 4, 2, 1, 6),
    _MplsLdpEntityConfAtmLabelRangeRowStatus_Type()
)
mplsLdpEntityConfAtmLabelRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityConfAtmLabelRangeRowStatus.setStatus("current")
_MplsLdpEntityFrameRelayObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityFrameRelayObjects = _MplsLdpEntityFrameRelayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5)
)
_MplsLdpEntityFrameRelayParmsTable_Object = MibTable
mplsLdpEntityFrameRelayParmsTable = _MplsLdpEntityFrameRelayParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayParmsTable.setStatus("current")
_MplsLdpEntityFrameRelayParmsEntry_Object = MibTableRow
mplsLdpEntityFrameRelayParmsEntry = _MplsLdpEntityFrameRelayParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5, 1, 1)
)
mplsLdpEntityFrameRelayParmsEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityFrameRelayParmsEntry.setStatus("current")
_MplsLdpEntityFrIfIndexOrZero_Type = InterfaceIndexOrZero
_MplsLdpEntityFrIfIndexOrZero_Object = MibTableColumn
mplsLdpEntityFrIfIndexOrZero = _MplsLdpEntityFrIfIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5, 1, 1, 1),
    _MplsLdpEntityFrIfIndexOrZero_Type()
)
mplsLdpEntityFrIfIndexOrZero.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrIfIndexOrZero.setStatus("current")


class _MplsLdpEntityFrMergeCap_Type(Integer32):
    """Custom type mplsLdpEntityFrMergeCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("supported", 1))
    )


_MplsLdpEntityFrMergeCap_Type.__name__ = "Integer32"
_MplsLdpEntityFrMergeCap_Object = MibTableColumn
mplsLdpEntityFrMergeCap = _MplsLdpEntityFrMergeCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5, 1, 1, 2),
    _MplsLdpEntityFrMergeCap_Type()
)
mplsLdpEntityFrMergeCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrMergeCap.setStatus("current")


class _MplsLdpEntityFrLabelRangeComponents_Type(Unsigned32):
    """Custom type mplsLdpEntityFrLabelRangeComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpEntityFrLabelRangeComponents_Type.__name__ = "Unsigned32"
_MplsLdpEntityFrLabelRangeComponents_Object = MibTableColumn
mplsLdpEntityFrLabelRangeComponents = _MplsLdpEntityFrLabelRangeComponents_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5, 1, 1, 3),
    _MplsLdpEntityFrLabelRangeComponents_Type()
)
mplsLdpEntityFrLabelRangeComponents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrLabelRangeComponents.setStatus("current")


class _MplsLdpEntityFrLen_Type(Integer32):
    """Custom type mplsLdpEntityFrLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenDlciBits", 0),
          ("twentyThreeDlciBits", 2))
    )


_MplsLdpEntityFrLen_Type.__name__ = "Integer32"
_MplsLdpEntityFrLen_Object = MibTableColumn
mplsLdpEntityFrLen = _MplsLdpEntityFrLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5, 1, 1, 4),
    _MplsLdpEntityFrLen_Type()
)
mplsLdpEntityFrLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrLen.setStatus("current")


class _MplsLdpEntityFrVcDirectionality_Type(Integer32):
    """Custom type mplsLdpEntityFrVcDirectionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 0),
          ("unidirection", 1))
    )


_MplsLdpEntityFrVcDirectionality_Type.__name__ = "Integer32"
_MplsLdpEntityFrVcDirectionality_Object = MibTableColumn
mplsLdpEntityFrVcDirectionality = _MplsLdpEntityFrVcDirectionality_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5, 1, 1, 5),
    _MplsLdpEntityFrVcDirectionality_Type()
)
mplsLdpEntityFrVcDirectionality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrVcDirectionality.setStatus("current")
_MplsLdpEntityFrParmsStorageType_Type = StorageType
_MplsLdpEntityFrParmsStorageType_Object = MibTableColumn
mplsLdpEntityFrParmsStorageType = _MplsLdpEntityFrParmsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5, 1, 1, 6),
    _MplsLdpEntityFrParmsStorageType_Type()
)
mplsLdpEntityFrParmsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrParmsStorageType.setStatus("current")
_MplsLdpEntityFrParmsRowStatus_Type = RowStatus
_MplsLdpEntityFrParmsRowStatus_Object = MibTableColumn
mplsLdpEntityFrParmsRowStatus = _MplsLdpEntityFrParmsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5, 1, 1, 7),
    _MplsLdpEntityFrParmsRowStatus_Type()
)
mplsLdpEntityFrParmsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpEntityFrParmsRowStatus.setStatus("current")
_MplsLdpEntityConfFrLabelRangeTable_Object = MibTable
mplsLdpEntityConfFrLabelRangeTable = _MplsLdpEntityConfFrLabelRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    mplsLdpEntityConfFrLabelRangeTable.setStatus("current")
_MplsLdpEntityConfFrLabelRangeEntry_Object = MibTableRow
mplsLdpEntityConfFrLabelRangeEntry = _MplsLdpEntityConfFrLabelRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5, 2, 1)
)
mplsLdpEntityConfFrLabelRangeEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpConfFrMinimumDlci"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityConfFrLabelRangeEntry.setStatus("current")


class _MplsLdpConfFrMinimumDlci_Type(Integer32):
    """Custom type mplsLdpConfFrMinimumDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_MplsLdpConfFrMinimumDlci_Type.__name__ = "Integer32"
_MplsLdpConfFrMinimumDlci_Object = MibTableColumn
mplsLdpConfFrMinimumDlci = _MplsLdpConfFrMinimumDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5, 2, 1, 1),
    _MplsLdpConfFrMinimumDlci_Type()
)
mplsLdpConfFrMinimumDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpConfFrMinimumDlci.setStatus("current")


class _MplsLdpConfFrMaximumDlci_Type(Integer32):
    """Custom type mplsLdpConfFrMaximumDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_MplsLdpConfFrMaximumDlci_Type.__name__ = "Integer32"
_MplsLdpConfFrMaximumDlci_Object = MibTableColumn
mplsLdpConfFrMaximumDlci = _MplsLdpConfFrMaximumDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5, 2, 1, 2),
    _MplsLdpConfFrMaximumDlci_Type()
)
mplsLdpConfFrMaximumDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpConfFrMaximumDlci.setStatus("current")
_MplsLdpConfFrStorageType_Type = StorageType
_MplsLdpConfFrStorageType_Object = MibTableColumn
mplsLdpConfFrStorageType = _MplsLdpConfFrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5, 2, 1, 3),
    _MplsLdpConfFrStorageType_Type()
)
mplsLdpConfFrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpConfFrStorageType.setStatus("current")
_MplsLdpConfFrRowStatus_Type = RowStatus
_MplsLdpConfFrRowStatus_Object = MibTableColumn
mplsLdpConfFrRowStatus = _MplsLdpConfFrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 5, 2, 1, 4),
    _MplsLdpConfFrRowStatus_Type()
)
mplsLdpConfFrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsLdpConfFrRowStatus.setStatus("current")
_MplsLdpEntityStatsTable_Object = MibTable
mplsLdpEntityStatsTable = _MplsLdpEntityStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 6)
)
if mibBuilder.loadTexts:
    mplsLdpEntityStatsTable.setStatus("current")
_MplsLdpEntityStatsEntry_Object = MibTableRow
mplsLdpEntityStatsEntry = _MplsLdpEntityStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityStatsEntry.setStatus("current")
_MplsLdpAttemptedSessions_Type = Counter32
_MplsLdpAttemptedSessions_Object = MibTableColumn
mplsLdpAttemptedSessions = _MplsLdpAttemptedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 6, 1, 1),
    _MplsLdpAttemptedSessions_Type()
)
mplsLdpAttemptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpAttemptedSessions.setStatus("current")
_MplsLdpSessionRejectedNoHelloErrors_Type = Counter32
_MplsLdpSessionRejectedNoHelloErrors_Object = MibTableColumn
mplsLdpSessionRejectedNoHelloErrors = _MplsLdpSessionRejectedNoHelloErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 6, 1, 2),
    _MplsLdpSessionRejectedNoHelloErrors_Type()
)
mplsLdpSessionRejectedNoHelloErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionRejectedNoHelloErrors.setStatus("current")
_MplsLdpSessionRejectedAdvertisementErrors_Type = Counter32
_MplsLdpSessionRejectedAdvertisementErrors_Object = MibTableColumn
mplsLdpSessionRejectedAdvertisementErrors = _MplsLdpSessionRejectedAdvertisementErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 6, 1, 3),
    _MplsLdpSessionRejectedAdvertisementErrors_Type()
)
mplsLdpSessionRejectedAdvertisementErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionRejectedAdvertisementErrors.setStatus("current")
_MplsLdpSessionRejectedMaxPduErrors_Type = Counter32
_MplsLdpSessionRejectedMaxPduErrors_Object = MibTableColumn
mplsLdpSessionRejectedMaxPduErrors = _MplsLdpSessionRejectedMaxPduErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 6, 1, 4),
    _MplsLdpSessionRejectedMaxPduErrors_Type()
)
mplsLdpSessionRejectedMaxPduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionRejectedMaxPduErrors.setStatus("current")
_MplsLdpSessionRejectedLabelRangeErrors_Type = Counter32
_MplsLdpSessionRejectedLabelRangeErrors_Object = MibTableColumn
mplsLdpSessionRejectedLabelRangeErrors = _MplsLdpSessionRejectedLabelRangeErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 6, 1, 5),
    _MplsLdpSessionRejectedLabelRangeErrors_Type()
)
mplsLdpSessionRejectedLabelRangeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionRejectedLabelRangeErrors.setStatus("current")
_MplsLdpBadLdpIdentifierErrors_Type = Counter32
_MplsLdpBadLdpIdentifierErrors_Object = MibTableColumn
mplsLdpBadLdpIdentifierErrors = _MplsLdpBadLdpIdentifierErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 6, 1, 6),
    _MplsLdpBadLdpIdentifierErrors_Type()
)
mplsLdpBadLdpIdentifierErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpBadLdpIdentifierErrors.setStatus("current")
_MplsLdpBadPduLengthErrors_Type = Counter32
_MplsLdpBadPduLengthErrors_Object = MibTableColumn
mplsLdpBadPduLengthErrors = _MplsLdpBadPduLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 6, 1, 7),
    _MplsLdpBadPduLengthErrors_Type()
)
mplsLdpBadPduLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpBadPduLengthErrors.setStatus("current")
_MplsLdpBadMessageLengthErrors_Type = Counter32
_MplsLdpBadMessageLengthErrors_Object = MibTableColumn
mplsLdpBadMessageLengthErrors = _MplsLdpBadMessageLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 6, 1, 8),
    _MplsLdpBadMessageLengthErrors_Type()
)
mplsLdpBadMessageLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpBadMessageLengthErrors.setStatus("current")
_MplsLdpBadTlvLengthErrors_Type = Counter32
_MplsLdpBadTlvLengthErrors_Object = MibTableColumn
mplsLdpBadTlvLengthErrors = _MplsLdpBadTlvLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 6, 1, 9),
    _MplsLdpBadTlvLengthErrors_Type()
)
mplsLdpBadTlvLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpBadTlvLengthErrors.setStatus("current")
_MplsLdpMalformedTlvValueErrors_Type = Counter32
_MplsLdpMalformedTlvValueErrors_Object = MibTableColumn
mplsLdpMalformedTlvValueErrors = _MplsLdpMalformedTlvValueErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 6, 1, 10),
    _MplsLdpMalformedTlvValueErrors_Type()
)
mplsLdpMalformedTlvValueErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpMalformedTlvValueErrors.setStatus("current")
_MplsLdpKeepAliveTimerExpiredErrors_Type = Counter32
_MplsLdpKeepAliveTimerExpiredErrors_Object = MibTableColumn
mplsLdpKeepAliveTimerExpiredErrors = _MplsLdpKeepAliveTimerExpiredErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 6, 1, 11),
    _MplsLdpKeepAliveTimerExpiredErrors_Type()
)
mplsLdpKeepAliveTimerExpiredErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpKeepAliveTimerExpiredErrors.setStatus("current")
_MplsLdpShutdownNotifReceived_Type = Counter32
_MplsLdpShutdownNotifReceived_Object = MibTableColumn
mplsLdpShutdownNotifReceived = _MplsLdpShutdownNotifReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 6, 1, 12),
    _MplsLdpShutdownNotifReceived_Type()
)
mplsLdpShutdownNotifReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpShutdownNotifReceived.setStatus("current")
_MplsLdpShutdownNotifSent_Type = Counter32
_MplsLdpShutdownNotifSent_Object = MibTableColumn
mplsLdpShutdownNotifSent = _MplsLdpShutdownNotifSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 2, 6, 1, 13),
    _MplsLdpShutdownNotifSent_Type()
)
mplsLdpShutdownNotifSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpShutdownNotifSent.setStatus("current")
_MplsLdpEntityPeerObjects_ObjectIdentity = ObjectIdentity
mplsLdpEntityPeerObjects = _MplsLdpEntityPeerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3)
)
_MplsLdpEntityPeerTable_Object = MibTable
mplsLdpEntityPeerTable = _MplsLdpEntityPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mplsLdpEntityPeerTable.setStatus("current")
_MplsLdpEntityPeerEntry_Object = MibTableRow
mplsLdpEntityPeerEntry = _MplsLdpEntityPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 1, 1)
)
mplsLdpEntityPeerEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    mplsLdpEntityPeerEntry.setStatus("current")
_MplsLdpPeerLdpId_Type = MplsLdpIdentifier
_MplsLdpPeerLdpId_Object = MibTableColumn
mplsLdpPeerLdpId = _MplsLdpPeerLdpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 1, 1, 1),
    _MplsLdpPeerLdpId_Type()
)
mplsLdpPeerLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpPeerLdpId.setStatus("current")


class _MplsLdpPeerLabelDistributionMethod_Type(Integer32):
    """Custom type mplsLdpPeerLabelDistributionMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstreamOnDemand", 1),
          ("downstreamUnsolicited", 2))
    )


_MplsLdpPeerLabelDistributionMethod_Type.__name__ = "Integer32"
_MplsLdpPeerLabelDistributionMethod_Object = MibTableColumn
mplsLdpPeerLabelDistributionMethod = _MplsLdpPeerLabelDistributionMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 1, 1, 2),
    _MplsLdpPeerLabelDistributionMethod_Type()
)
mplsLdpPeerLabelDistributionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerLabelDistributionMethod.setStatus("current")


class _MplsLdpPeerLoopDetectionForPV_Type(Integer32):
    """Custom type mplsLdpPeerLoopDetectionForPV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MplsLdpPeerLoopDetectionForPV_Type.__name__ = "Integer32"
_MplsLdpPeerLoopDetectionForPV_Object = MibTableColumn
mplsLdpPeerLoopDetectionForPV = _MplsLdpPeerLoopDetectionForPV_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 1, 1, 3),
    _MplsLdpPeerLoopDetectionForPV_Type()
)
mplsLdpPeerLoopDetectionForPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerLoopDetectionForPV.setStatus("current")


class _MplsLdpPeerPathVectorLimit_Type(Integer32):
    """Custom type mplsLdpPeerPathVectorLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsLdpPeerPathVectorLimit_Type.__name__ = "Integer32"
_MplsLdpPeerPathVectorLimit_Object = MibTableColumn
mplsLdpPeerPathVectorLimit = _MplsLdpPeerPathVectorLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 1, 1, 4),
    _MplsLdpPeerPathVectorLimit_Type()
)
mplsLdpPeerPathVectorLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpPeerPathVectorLimit.setStatus("current")
_MplsLdpHelloAdjacencyObjects_ObjectIdentity = ObjectIdentity
mplsLdpHelloAdjacencyObjects = _MplsLdpHelloAdjacencyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 2)
)
_MplsLdpHelloAdjacencyTable_Object = MibTable
mplsLdpHelloAdjacencyTable = _MplsLdpHelloAdjacencyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyTable.setStatus("current")
_MplsLdpHelloAdjacencyEntry_Object = MibTableRow
mplsLdpHelloAdjacencyEntry = _MplsLdpHelloAdjacencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 2, 1, 1)
)
mplsLdpHelloAdjacencyEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpHelloAdjacencyIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyEntry.setStatus("current")


class _MplsLdpHelloAdjacencyIndex_Type(Unsigned32):
    """Custom type mplsLdpHelloAdjacencyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsLdpHelloAdjacencyIndex_Type.__name__ = "Unsigned32"
_MplsLdpHelloAdjacencyIndex_Object = MibTableColumn
mplsLdpHelloAdjacencyIndex = _MplsLdpHelloAdjacencyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 2, 1, 1, 1),
    _MplsLdpHelloAdjacencyIndex_Type()
)
mplsLdpHelloAdjacencyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyIndex.setStatus("current")
_MplsLdpHelloAdjacencyHoldTimeRemaining_Type = TimeInterval
_MplsLdpHelloAdjacencyHoldTimeRemaining_Object = MibTableColumn
mplsLdpHelloAdjacencyHoldTimeRemaining = _MplsLdpHelloAdjacencyHoldTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 2, 1, 1, 2),
    _MplsLdpHelloAdjacencyHoldTimeRemaining_Type()
)
mplsLdpHelloAdjacencyHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyHoldTimeRemaining.setStatus("current")


class _MplsLdpHelloAdjacencyType_Type(Integer32):
    """Custom type mplsLdpHelloAdjacencyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("targeted", 2))
    )


_MplsLdpHelloAdjacencyType_Type.__name__ = "Integer32"
_MplsLdpHelloAdjacencyType_Object = MibTableColumn
mplsLdpHelloAdjacencyType = _MplsLdpHelloAdjacencyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 2, 1, 1, 3),
    _MplsLdpHelloAdjacencyType_Type()
)
mplsLdpHelloAdjacencyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpHelloAdjacencyType.setStatus("current")
_MplsLdpSessionObjects_ObjectIdentity = ObjectIdentity
mplsLdpSessionObjects = _MplsLdpSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3)
)


class _MplsLdpSessionUpDownTrapEnable_Type(Integer32):
    """Custom type mplsLdpSessionUpDownTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_MplsLdpSessionUpDownTrapEnable_Type.__name__ = "Integer32"
_MplsLdpSessionUpDownTrapEnable_Object = MibScalar
mplsLdpSessionUpDownTrapEnable = _MplsLdpSessionUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 1),
    _MplsLdpSessionUpDownTrapEnable_Type()
)
mplsLdpSessionUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsLdpSessionUpDownTrapEnable.setStatus("current")
_MplsLdpSessionTable_Object = MibTable
mplsLdpSessionTable = _MplsLdpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    mplsLdpSessionTable.setStatus("current")
_MplsLdpSessionEntry_Object = MibTableRow
mplsLdpSessionEntry = _MplsLdpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 2, 1)
)
mplsLdpSessionEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    mplsLdpSessionEntry.setStatus("current")


class _MplsLdpSessionState_Type(Integer32):
    """Custom type mplsLdpSessionState based on Integer32"""
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
        *(("nonexistent", 1),
          ("initialized", 2),
          ("openrec", 3),
          ("opensent", 4),
          ("operational", 5))
    )


_MplsLdpSessionState_Type.__name__ = "Integer32"
_MplsLdpSessionState_Object = MibTableColumn
mplsLdpSessionState = _MplsLdpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 2, 1, 1),
    _MplsLdpSessionState_Type()
)
mplsLdpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionState.setStatus("current")


class _MplsLdpSessionProtocolVersion_Type(Integer32):
    """Custom type mplsLdpSessionProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpSessionProtocolVersion_Type.__name__ = "Integer32"
_MplsLdpSessionProtocolVersion_Object = MibTableColumn
mplsLdpSessionProtocolVersion = _MplsLdpSessionProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 2, 1, 2),
    _MplsLdpSessionProtocolVersion_Type()
)
mplsLdpSessionProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionProtocolVersion.setStatus("current")
_MplsLdpSessionKeepAliveHoldTimeRemaining_Type = TimeInterval
_MplsLdpSessionKeepAliveHoldTimeRemaining_Object = MibTableColumn
mplsLdpSessionKeepAliveHoldTimeRemaining = _MplsLdpSessionKeepAliveHoldTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 2, 1, 3),
    _MplsLdpSessionKeepAliveHoldTimeRemaining_Type()
)
mplsLdpSessionKeepAliveHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionKeepAliveHoldTimeRemaining.setStatus("current")


class _MplsLdpSessionMaxPduLength_Type(Unsigned32):
    """Custom type mplsLdpSessionMaxPduLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsLdpSessionMaxPduLength_Type.__name__ = "Unsigned32"
_MplsLdpSessionMaxPduLength_Object = MibTableColumn
mplsLdpSessionMaxPduLength = _MplsLdpSessionMaxPduLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 2, 1, 4),
    _MplsLdpSessionMaxPduLength_Type()
)
mplsLdpSessionMaxPduLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionMaxPduLength.setStatus("current")
_MplsLdpSessionDiscontinuityTime_Type = TimeStamp
_MplsLdpSessionDiscontinuityTime_Object = MibTableColumn
mplsLdpSessionDiscontinuityTime = _MplsLdpSessionDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 2, 1, 5),
    _MplsLdpSessionDiscontinuityTime_Type()
)
mplsLdpSessionDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionDiscontinuityTime.setStatus("current")
_MplsLdpAtmSessionTable_Object = MibTable
mplsLdpAtmSessionTable = _MplsLdpAtmSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    mplsLdpAtmSessionTable.setStatus("current")
_MplsLdpAtmSessionEntry_Object = MibTableRow
mplsLdpAtmSessionEntry = _MplsLdpAtmSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 4, 1)
)
mplsLdpAtmSessionEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionAtmLabelRangeLowerBoundVpi"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionAtmLabelRangeLowerBoundVci"),
)
if mibBuilder.loadTexts:
    mplsLdpAtmSessionEntry.setStatus("current")
_MplsLdpSessionAtmLabelRangeLowerBoundVpi_Type = AtmVpIdentifier
_MplsLdpSessionAtmLabelRangeLowerBoundVpi_Object = MibTableColumn
mplsLdpSessionAtmLabelRangeLowerBoundVpi = _MplsLdpSessionAtmLabelRangeLowerBoundVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 4, 1, 1),
    _MplsLdpSessionAtmLabelRangeLowerBoundVpi_Type()
)
mplsLdpSessionAtmLabelRangeLowerBoundVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLabelRangeLowerBoundVpi.setStatus("current")
_MplsLdpSessionAtmLabelRangeLowerBoundVci_Type = AtmVcIdentifier
_MplsLdpSessionAtmLabelRangeLowerBoundVci_Object = MibTableColumn
mplsLdpSessionAtmLabelRangeLowerBoundVci = _MplsLdpSessionAtmLabelRangeLowerBoundVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 4, 1, 2),
    _MplsLdpSessionAtmLabelRangeLowerBoundVci_Type()
)
mplsLdpSessionAtmLabelRangeLowerBoundVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLabelRangeLowerBoundVci.setStatus("current")
_MplsLdpSessionAtmLabelRangeUpperBoundVpi_Type = AtmVpIdentifier
_MplsLdpSessionAtmLabelRangeUpperBoundVpi_Object = MibTableColumn
mplsLdpSessionAtmLabelRangeUpperBoundVpi = _MplsLdpSessionAtmLabelRangeUpperBoundVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 4, 1, 3),
    _MplsLdpSessionAtmLabelRangeUpperBoundVpi_Type()
)
mplsLdpSessionAtmLabelRangeUpperBoundVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLabelRangeUpperBoundVpi.setStatus("current")
_MplsLdpSessionAtmLabelRangeUpperBoundVci_Type = AtmVcIdentifier
_MplsLdpSessionAtmLabelRangeUpperBoundVci_Object = MibTableColumn
mplsLdpSessionAtmLabelRangeUpperBoundVci = _MplsLdpSessionAtmLabelRangeUpperBoundVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 4, 1, 4),
    _MplsLdpSessionAtmLabelRangeUpperBoundVci_Type()
)
mplsLdpSessionAtmLabelRangeUpperBoundVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionAtmLabelRangeUpperBoundVci.setStatus("current")
_MplsLdpFrameRelaySessionTable_Object = MibTable
mplsLdpFrameRelaySessionTable = _MplsLdpFrameRelaySessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    mplsLdpFrameRelaySessionTable.setStatus("current")
_MplsLdpFrameRelaySessionEntry_Object = MibTableRow
mplsLdpFrameRelaySessionEntry = _MplsLdpFrameRelaySessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 5, 1)
)
mplsLdpFrameRelaySessionEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpFrSessionMinDlci"),
)
if mibBuilder.loadTexts:
    mplsLdpFrameRelaySessionEntry.setStatus("current")


class _MplsLdpFrSessionMinDlci_Type(Integer32):
    """Custom type mplsLdpFrSessionMinDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_MplsLdpFrSessionMinDlci_Type.__name__ = "Integer32"
_MplsLdpFrSessionMinDlci_Object = MibTableColumn
mplsLdpFrSessionMinDlci = _MplsLdpFrSessionMinDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 5, 1, 1),
    _MplsLdpFrSessionMinDlci_Type()
)
mplsLdpFrSessionMinDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpFrSessionMinDlci.setStatus("current")


class _MplsLdpFrSessionMaxDlci_Type(Integer32):
    """Custom type mplsLdpFrSessionMaxDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194303),
    )


_MplsLdpFrSessionMaxDlci_Type.__name__ = "Integer32"
_MplsLdpFrSessionMaxDlci_Object = MibTableColumn
mplsLdpFrSessionMaxDlci = _MplsLdpFrSessionMaxDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 5, 1, 2),
    _MplsLdpFrSessionMaxDlci_Type()
)
mplsLdpFrSessionMaxDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpFrSessionMaxDlci.setStatus("current")


class _MplsLdpFrSessionLen_Type(Integer32):
    """Custom type mplsLdpFrSessionLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenDlciBits", 0),
          ("twentyThreeDlciBits", 2))
    )


_MplsLdpFrSessionLen_Type.__name__ = "Integer32"
_MplsLdpFrSessionLen_Object = MibTableColumn
mplsLdpFrSessionLen = _MplsLdpFrSessionLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 5, 1, 3),
    _MplsLdpFrSessionLen_Type()
)
mplsLdpFrSessionLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpFrSessionLen.setStatus("current")
_MplsLdpSessionStatsTable_Object = MibTable
mplsLdpSessionStatsTable = _MplsLdpSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 6)
)
if mibBuilder.loadTexts:
    mplsLdpSessionStatsTable.setStatus("current")
_MplsLdpSessionStatsEntry_Object = MibTableRow
mplsLdpSessionStatsEntry = _MplsLdpSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 6, 1)
)
if mibBuilder.loadTexts:
    mplsLdpSessionStatsEntry.setStatus("current")
_MplsLdpSessionStatsUnknownMessageTypeErrors_Type = Counter32
_MplsLdpSessionStatsUnknownMessageTypeErrors_Object = MibTableColumn
mplsLdpSessionStatsUnknownMessageTypeErrors = _MplsLdpSessionStatsUnknownMessageTypeErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 6, 1, 1),
    _MplsLdpSessionStatsUnknownMessageTypeErrors_Type()
)
mplsLdpSessionStatsUnknownMessageTypeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionStatsUnknownMessageTypeErrors.setStatus("current")
_MplsLdpSessionStatsUnknownTlvErrors_Type = Counter32
_MplsLdpSessionStatsUnknownTlvErrors_Object = MibTableColumn
mplsLdpSessionStatsUnknownTlvErrors = _MplsLdpSessionStatsUnknownTlvErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 6, 1, 2),
    _MplsLdpSessionStatsUnknownTlvErrors_Type()
)
mplsLdpSessionStatsUnknownTlvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionStatsUnknownTlvErrors.setStatus("current")
_MplsLdpSessionPeerAddressTable_Object = MibTable
mplsLdpSessionPeerAddressTable = _MplsLdpSessionPeerAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 7)
)
if mibBuilder.loadTexts:
    mplsLdpSessionPeerAddressTable.setStatus("current")
_MplsLdpSessionPeerAddressEntry_Object = MibTableRow
mplsLdpSessionPeerAddressEntry = _MplsLdpSessionPeerAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 7, 1)
)
mplsLdpSessionPeerAddressEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpEntityLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpEntityIndex"),
    (0, "MPLS-LDP-MIB", "mplsLdpPeerLdpId"),
    (0, "MPLS-LDP-MIB", "mplsLdpSessionPeerAddressIndex"),
)
if mibBuilder.loadTexts:
    mplsLdpSessionPeerAddressEntry.setStatus("current")


class _MplsLdpSessionPeerAddressIndex_Type(Unsigned32):
    """Custom type mplsLdpSessionPeerAddressIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsLdpSessionPeerAddressIndex_Type.__name__ = "Unsigned32"
_MplsLdpSessionPeerAddressIndex_Object = MibTableColumn
mplsLdpSessionPeerAddressIndex = _MplsLdpSessionPeerAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 7, 1, 1),
    _MplsLdpSessionPeerAddressIndex_Type()
)
mplsLdpSessionPeerAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpSessionPeerAddressIndex.setStatus("current")
_MplsLdpSessionPeerNextHopAddressType_Type = AddressFamilyNumbers
_MplsLdpSessionPeerNextHopAddressType_Object = MibTableColumn
mplsLdpSessionPeerNextHopAddressType = _MplsLdpSessionPeerNextHopAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 7, 1, 2),
    _MplsLdpSessionPeerNextHopAddressType_Type()
)
mplsLdpSessionPeerNextHopAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionPeerNextHopAddressType.setStatus("current")
_MplsLdpSessionPeerNextHopAddress_Type = MplsLdpGenAddr
_MplsLdpSessionPeerNextHopAddress_Object = MibTableColumn
mplsLdpSessionPeerNextHopAddress = _MplsLdpSessionPeerNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 3, 3, 7, 1, 3),
    _MplsLdpSessionPeerNextHopAddress_Type()
)
mplsLdpSessionPeerNextHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpSessionPeerNextHopAddress.setStatus("current")
_MplsLdpLibObjects_ObjectIdentity = ObjectIdentity
mplsLdpLibObjects = _MplsLdpLibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6)
)


class _MplsLdpLibLspUpDownTrapEnable_Type(Integer32):
    """Custom type mplsLdpLibLspUpDownTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_MplsLdpLibLspUpDownTrapEnable_Type.__name__ = "Integer32"
_MplsLdpLibLspUpDownTrapEnable_Object = MibScalar
mplsLdpLibLspUpDownTrapEnable = _MplsLdpLibLspUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 1),
    _MplsLdpLibLspUpDownTrapEnable_Type()
)
mplsLdpLibLspUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsLdpLibLspUpDownTrapEnable.setStatus("current")
_MplsLdpLibTable_Object = MibTable
mplsLdpLibTable = _MplsLdpLibTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 2)
)
if mibBuilder.loadTexts:
    mplsLdpLibTable.setStatus("current")
_MplsLdpLibEntry_Object = MibTableRow
mplsLdpLibEntry = _MplsLdpLibEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 2, 1)
)
mplsLdpLibEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpLibLspId"),
)
if mibBuilder.loadTexts:
    mplsLdpLibEntry.setStatus("current")


class _MplsLdpLibLspId_Type(Unsigned32):
    """Custom type mplsLdpLibLspId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsLdpLibLspId_Type.__name__ = "Unsigned32"
_MplsLdpLibLspId_Object = MibTableColumn
mplsLdpLibLspId = _MplsLdpLibLspId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 2, 1, 1),
    _MplsLdpLibLspId_Type()
)
mplsLdpLibLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpLibLspId.setStatus("current")
_MplsLdpLibLabelInIfIndex_Type = InterfaceIndex
_MplsLdpLibLabelInIfIndex_Object = MibTableColumn
mplsLdpLibLabelInIfIndex = _MplsLdpLibLabelInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 2, 1, 2),
    _MplsLdpLibLabelInIfIndex_Type()
)
mplsLdpLibLabelInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLibLabelInIfIndex.setStatus("current")
_MplsLdpLibLabelOutIfIndex_Type = InterfaceIndex
_MplsLdpLibLabelOutIfIndex_Object = MibTableColumn
mplsLdpLibLabelOutIfIndex = _MplsLdpLibLabelOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 2, 1, 3),
    _MplsLdpLibLabelOutIfIndex_Type()
)
mplsLdpLibLabelOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLibLabelOutIfIndex.setStatus("current")
_MplsLdpLibInLabelType_Type = MplsLdpLabelTypes
_MplsLdpLibInLabelType_Object = MibTableColumn
mplsLdpLibInLabelType = _MplsLdpLibInLabelType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 2, 1, 4),
    _MplsLdpLibInLabelType_Type()
)
mplsLdpLibInLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLibInLabelType.setStatus("current")
_MplsLdpLibInLabel_Type = MplsLabel
_MplsLdpLibInLabel_Object = MibTableColumn
mplsLdpLibInLabel = _MplsLdpLibInLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 2, 1, 5),
    _MplsLdpLibInLabel_Type()
)
mplsLdpLibInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLibInLabel.setStatus("current")
_MplsLdpLibOutLabelType_Type = MplsLdpLabelTypes
_MplsLdpLibOutLabelType_Object = MibTableColumn
mplsLdpLibOutLabelType = _MplsLdpLibOutLabelType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 2, 1, 6),
    _MplsLdpLibOutLabelType_Type()
)
mplsLdpLibOutLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLibOutLabelType.setStatus("current")
_MplsLdpLibOutLabel_Type = MplsLabel
_MplsLdpLibOutLabel_Object = MibTableColumn
mplsLdpLibOutLabel = _MplsLdpLibOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 2, 1, 7),
    _MplsLdpLibOutLabel_Type()
)
mplsLdpLibOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLibOutLabel.setStatus("current")


class _MplsLdpLibOperationStatus_Type(Integer32):
    """Custom type mplsLdpLibOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("up", 2),
          ("down", 3))
    )


_MplsLdpLibOperationStatus_Type.__name__ = "Integer32"
_MplsLdpLibOperationStatus_Object = MibTableColumn
mplsLdpLibOperationStatus = _MplsLdpLibOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 2, 1, 8),
    _MplsLdpLibOperationStatus_Type()
)
mplsLdpLibOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLibOperationStatus.setStatus("current")
_MplsLdpLibLspLastChange_Type = TimeStamp
_MplsLdpLibLspLastChange_Object = MibTableColumn
mplsLdpLibLspLastChange = _MplsLdpLibLspLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 2, 1, 9),
    _MplsLdpLibLspLastChange_Type()
)
mplsLdpLibLspLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpLibLspLastChange.setStatus("current")
_MplsLdpFecTable_Object = MibTable
mplsLdpFecTable = _MplsLdpFecTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 3)
)
if mibBuilder.loadTexts:
    mplsLdpFecTable.setStatus("current")
_MplsLdpFecEntry_Object = MibTableRow
mplsLdpFecEntry = _MplsLdpFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 3, 1)
)
mplsLdpFecEntry.setIndexNames(
    (0, "MPLS-LDP-MIB", "mplsLdpFecType"),
    (0, "MPLS-LDP-MIB", "mplsLdpFecAddressFamily"),
    (0, "MPLS-LDP-MIB", "mplsLdpFecAddressLength"),
    (0, "MPLS-LDP-MIB", "mplsLdpFecAddress"),
    (0, "MPLS-LDP-MIB", "mplsLdpFecLspId"),
)
if mibBuilder.loadTexts:
    mplsLdpFecEntry.setStatus("current")


class _MplsLdpFecType_Type(Integer32):
    """Custom type mplsLdpFecType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("prefix", 1),
          ("hostAddress", 2))
    )


_MplsLdpFecType_Type.__name__ = "Integer32"
_MplsLdpFecType_Object = MibTableColumn
mplsLdpFecType = _MplsLdpFecType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 3, 1, 1),
    _MplsLdpFecType_Type()
)
mplsLdpFecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpFecType.setStatus("current")
_MplsLdpFecAddressFamily_Type = AddressFamilyNumbers
_MplsLdpFecAddressFamily_Object = MibTableColumn
mplsLdpFecAddressFamily = _MplsLdpFecAddressFamily_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 3, 1, 2),
    _MplsLdpFecAddressFamily_Type()
)
mplsLdpFecAddressFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpFecAddressFamily.setStatus("current")


class _MplsLdpFecAddressLength_Type(Integer32):
    """Custom type mplsLdpFecAddressLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsLdpFecAddressLength_Type.__name__ = "Integer32"
_MplsLdpFecAddressLength_Object = MibTableColumn
mplsLdpFecAddressLength = _MplsLdpFecAddressLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 3, 1, 3),
    _MplsLdpFecAddressLength_Type()
)
mplsLdpFecAddressLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpFecAddressLength.setStatus("current")
_MplsLdpFecAddress_Type = MplsLdpGenAddr
_MplsLdpFecAddress_Object = MibTableColumn
mplsLdpFecAddress = _MplsLdpFecAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 3, 1, 4),
    _MplsLdpFecAddress_Type()
)
mplsLdpFecAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpFecAddress.setStatus("current")


class _MplsLdpFecLspId_Type(Unsigned32):
    """Custom type mplsLdpFecLspId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MplsLdpFecLspId_Type.__name__ = "Unsigned32"
_MplsLdpFecLspId_Object = MibTableColumn
mplsLdpFecLspId = _MplsLdpFecLspId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 3, 1, 5),
    _MplsLdpFecLspId_Type()
)
mplsLdpFecLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsLdpFecLspId.setStatus("current")
_MplsLdpFecSessionRowPointer_Type = RowPointer
_MplsLdpFecSessionRowPointer_Object = MibTableColumn
mplsLdpFecSessionRowPointer = _MplsLdpFecSessionRowPointer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 1, 6, 3, 1, 6),
    _MplsLdpFecSessionRowPointer_Type()
)
mplsLdpFecSessionRowPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsLdpFecSessionRowPointer.setStatus("current")
_MplsLdpNotifications_ObjectIdentity = ObjectIdentity
mplsLdpNotifications = _MplsLdpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 2)
)
_MplsLdpNotificationPrefix_ObjectIdentity = ObjectIdentity
mplsLdpNotificationPrefix = _MplsLdpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 2, 0)
)
_MplsLdpConformance_ObjectIdentity = ObjectIdentity
mplsLdpConformance = _MplsLdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 3)
)
_MplsLdpGroups_ObjectIdentity = ObjectIdentity
mplsLdpGroups = _MplsLdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 3, 1)
)
_MplsLdpCompliances_ObjectIdentity = ObjectIdentity
mplsLdpCompliances = _MplsLdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 3, 2)
)
mplsLdpEntityEntry.registerAugmentions(
    ("MPLS-LDP-MIB",
     "mplsLdpEntityStatsEntry")
)
mplsLdpEntityStatsEntry.setIndexNames(*mplsLdpEntityEntry.getIndexNames())
mplsLdpSessionEntry.registerAugmentions(
    ("MPLS-LDP-MIB",
     "mplsLdpSessionStatsEntry")
)
mplsLdpSessionStatsEntry.setIndexNames(*mplsLdpSessionEntry.getIndexNames())

# Managed Objects groups

mplsLdpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 3, 1, 1)
)
mplsLdpGeneralGroup.setObjects(
      *(("MPLS-LDP-MIB", "mplsLdpLsrId"),
        ("MPLS-LDP-MIB", "mplsLdpLsrLabelRetentionMode"),
        ("MPLS-LDP-MIB", "mplsLdpLsrLoopDetectionCapable"),
        ("MPLS-LDP-MIB", "mplsLdpEntityIndexNext"),
        ("MPLS-LDP-MIB", "mplsLdpEntityProtocolVersion"),
        ("MPLS-LDP-MIB", "mplsLdpEntityAdminStatus"),
        ("MPLS-LDP-MIB", "mplsLdpEntityOperStatus"),
        ("MPLS-LDP-MIB", "mplsLdpEntityWellKnownDiscoveryPort"),
        ("MPLS-LDP-MIB", "mplsLdpEntityMaxPduLength"),
        ("MPLS-LDP-MIB", "mplsLdpEntityKeepAliveHoldTimer"),
        ("MPLS-LDP-MIB", "mplsLdpEntityHelloHoldTimer"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFailedInitSessionTrapEnable"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFailedInitSessionThreshold"),
        ("MPLS-LDP-MIB", "mplsLdpEntityLabelDistributionMethod"),
        ("MPLS-LDP-MIB", "mplsLdpEntityPVLimitMismatchTrapEnable"),
        ("MPLS-LDP-MIB", "mplsLdpEntityPathVectorLimit"),
        ("MPLS-LDP-MIB", "mplsLdpEntityHopCountLoopDetection"),
        ("MPLS-LDP-MIB", "mplsLdpEntityHopCount"),
        ("MPLS-LDP-MIB", "mplsLdpEntityTargetedPeer"),
        ("MPLS-LDP-MIB", "mplsLdpEntityTargetedPeerAddrType"),
        ("MPLS-LDP-MIB", "mplsLdpEntityTargetedPeerAddr"),
        ("MPLS-LDP-MIB", "mplsLdpEntityOptionalParameters"),
        ("MPLS-LDP-MIB", "mplsLdpEntityDiscontinuityTime"),
        ("MPLS-LDP-MIB", "mplsLdpEntityStorageType"),
        ("MPLS-LDP-MIB", "mplsLdpEntityRowStatus"),
        ("MPLS-LDP-MIB", "mplsLdpAttemptedSessions"),
        ("MPLS-LDP-MIB", "mplsLdpSessionRejectedNoHelloErrors"),
        ("MPLS-LDP-MIB", "mplsLdpSessionRejectedAdvertisementErrors"),
        ("MPLS-LDP-MIB", "mplsLdpSessionRejectedMaxPduErrors"),
        ("MPLS-LDP-MIB", "mplsLdpSessionRejectedLabelRangeErrors"),
        ("MPLS-LDP-MIB", "mplsLdpBadLdpIdentifierErrors"),
        ("MPLS-LDP-MIB", "mplsLdpBadPduLengthErrors"),
        ("MPLS-LDP-MIB", "mplsLdpBadMessageLengthErrors"),
        ("MPLS-LDP-MIB", "mplsLdpBadTlvLengthErrors"),
        ("MPLS-LDP-MIB", "mplsLdpMalformedTlvValueErrors"),
        ("MPLS-LDP-MIB", "mplsLdpKeepAliveTimerExpiredErrors"),
        ("MPLS-LDP-MIB", "mplsLdpShutdownNotifReceived"),
        ("MPLS-LDP-MIB", "mplsLdpShutdownNotifSent"),
        ("MPLS-LDP-MIB", "mplsLdpPeerLabelDistributionMethod"),
        ("MPLS-LDP-MIB", "mplsLdpPeerLoopDetectionForPV"),
        ("MPLS-LDP-MIB", "mplsLdpPeerPathVectorLimit"),
        ("MPLS-LDP-MIB", "mplsLdpHelloAdjacencyHoldTimeRemaining"),
        ("MPLS-LDP-MIB", "mplsLdpHelloAdjacencyType"),
        ("MPLS-LDP-MIB", "mplsLdpSessionUpDownTrapEnable"),
        ("MPLS-LDP-MIB", "mplsLdpSessionState"),
        ("MPLS-LDP-MIB", "mplsLdpSessionProtocolVersion"),
        ("MPLS-LDP-MIB", "mplsLdpSessionKeepAliveHoldTimeRemaining"),
        ("MPLS-LDP-MIB", "mplsLdpSessionMaxPduLength"),
        ("MPLS-LDP-MIB", "mplsLdpSessionDiscontinuityTime"),
        ("MPLS-LDP-MIB", "mplsLdpSessionStatsUnknownMessageTypeErrors"),
        ("MPLS-LDP-MIB", "mplsLdpSessionStatsUnknownTlvErrors"),
        ("MPLS-LDP-MIB", "mplsLdpSessionPeerNextHopAddressType"),
        ("MPLS-LDP-MIB", "mplsLdpSessionPeerNextHopAddress"),
        ("MPLS-LDP-MIB", "mplsLdpLibLspUpDownTrapEnable"),
        ("MPLS-LDP-MIB", "mplsLdpLibLabelInIfIndex"),
        ("MPLS-LDP-MIB", "mplsLdpLibLabelOutIfIndex"),
        ("MPLS-LDP-MIB", "mplsLdpLibInLabelType"),
        ("MPLS-LDP-MIB", "mplsLdpLibInLabel"),
        ("MPLS-LDP-MIB", "mplsLdpLibOutLabelType"),
        ("MPLS-LDP-MIB", "mplsLdpLibOutLabel"),
        ("MPLS-LDP-MIB", "mplsLdpLibOperationStatus"),
        ("MPLS-LDP-MIB", "mplsLdpLibLspLastChange"),
        ("MPLS-LDP-MIB", "mplsLdpFecSessionRowPointer"))
)
if mibBuilder.loadTexts:
    mplsLdpGeneralGroup.setStatus("current")

mplsLdpGenericGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 3, 1, 2)
)
mplsLdpGenericGroup.setObjects(
      *(("MPLS-LDP-MIB", "mplsLdpConfGenericIfIndexOrZero"),
        ("MPLS-LDP-MIB", "mplsLdpConfGenericLabel"),
        ("MPLS-LDP-MIB", "mplsLdpConfGenericStorageType"),
        ("MPLS-LDP-MIB", "mplsLdpConfGenericRowStatus"))
)
if mibBuilder.loadTexts:
    mplsLdpGenericGroup.setStatus("current")

mplsLdpAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 3, 1, 3)
)
mplsLdpAtmGroup.setObjects(
      *(("MPLS-LDP-MIB", "mplsLdpEntityAtmIfIndexOrZero"),
        ("MPLS-LDP-MIB", "mplsLdpEntityAtmMergeCap"),
        ("MPLS-LDP-MIB", "mplsLdpEntityAtmLabelRangeComponents"),
        ("MPLS-LDP-MIB", "mplsLdpEntityAtmVcDirectionality"),
        ("MPLS-LDP-MIB", "mplsLdpEntityAtmLsrConnectivity"),
        ("MPLS-LDP-MIB", "mplsLdpEntityDefaultControlVpi"),
        ("MPLS-LDP-MIB", "mplsLdpEntityDefaultControlVci"),
        ("MPLS-LDP-MIB", "mplsLdpEntityUnlabTrafVpi"),
        ("MPLS-LDP-MIB", "mplsLdpEntityUnlabTrafVci"),
        ("MPLS-LDP-MIB", "mplsLdpEntityAtmStorageType"),
        ("MPLS-LDP-MIB", "mplsLdpEntityAtmRowStatus"),
        ("MPLS-LDP-MIB", "mplsLdpEntityConfAtmLabelRangeMaximumVpi"),
        ("MPLS-LDP-MIB", "mplsLdpEntityConfAtmLabelRangeMaximumVci"),
        ("MPLS-LDP-MIB", "mplsLdpEntityConfAtmLabelRangeStorageType"),
        ("MPLS-LDP-MIB", "mplsLdpEntityConfAtmLabelRangeRowStatus"),
        ("MPLS-LDP-MIB", "mplsLdpSessionAtmLabelRangeUpperBoundVpi"),
        ("MPLS-LDP-MIB", "mplsLdpSessionAtmLabelRangeUpperBoundVci"))
)
if mibBuilder.loadTexts:
    mplsLdpAtmGroup.setStatus("current")

mplsLdpFrameRelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 3, 1, 4)
)
mplsLdpFrameRelayGroup.setObjects(
      *(("MPLS-LDP-MIB", "mplsLdpEntityFrIfIndexOrZero"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFrMergeCap"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFrLabelRangeComponents"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFrLen"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFrVcDirectionality"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFrParmsStorageType"),
        ("MPLS-LDP-MIB", "mplsLdpEntityFrParmsRowStatus"),
        ("MPLS-LDP-MIB", "mplsLdpConfFrMaximumDlci"),
        ("MPLS-LDP-MIB", "mplsLdpConfFrStorageType"),
        ("MPLS-LDP-MIB", "mplsLdpConfFrRowStatus"),
        ("MPLS-LDP-MIB", "mplsLdpFrSessionMaxDlci"),
        ("MPLS-LDP-MIB", "mplsLdpFrSessionLen"))
)
if mibBuilder.loadTexts:
    mplsLdpFrameRelayGroup.setStatus("current")


# Notification objects

mplsLdpFailedInitSessionThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 2, 0, 1)
)
mplsLdpFailedInitSessionThresholdExceeded.setObjects(
    ("MPLS-LDP-MIB", "mplsLdpEntityFailedInitSessionThreshold")
)
if mibBuilder.loadTexts:
    mplsLdpFailedInitSessionThresholdExceeded.setStatus(
        "current"
    )

mplsLdpPathVectorLimitMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 2, 0, 2)
)
mplsLdpPathVectorLimitMismatch.setObjects(
      *(("MPLS-LDP-MIB", "mplsLdpEntityPathVectorLimit"),
        ("MPLS-LDP-MIB", "mplsLdpPeerPathVectorLimit"))
)
if mibBuilder.loadTexts:
    mplsLdpPathVectorLimitMismatch.setStatus(
        "current"
    )

mplsLdpSessionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 2, 0, 3)
)
mplsLdpSessionUp.setObjects(
    ("MPLS-LDP-MIB", "mplsLdpSessionState")
)
if mibBuilder.loadTexts:
    mplsLdpSessionUp.setStatus(
        "current"
    )

mplsLdpSessionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 2, 0, 4)
)
mplsLdpSessionDown.setObjects(
    ("MPLS-LDP-MIB", "mplsLdpSessionState")
)
if mibBuilder.loadTexts:
    mplsLdpSessionDown.setStatus(
        "current"
    )

mplsLdpLibLspUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 2, 0, 5)
)
mplsLdpLibLspUp.setObjects(
    ("MPLS-LDP-MIB", "mplsLdpLibOperationStatus")
)
if mibBuilder.loadTexts:
    mplsLdpLibLspUp.setStatus(
        "current"
    )

mplsLdpLibLspDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 2, 0, 6)
)
mplsLdpLibLspDown.setObjects(
    ("MPLS-LDP-MIB", "mplsLdpLibOperationStatus")
)
if mibBuilder.loadTexts:
    mplsLdpLibLspDown.setStatus(
        "current"
    )


# Notifications groups

mplsLdpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 3, 1, 5)
)
mplsLdpNotificationsGroup.setObjects(
      *(("MPLS-LDP-MIB", "mplsLdpFailedInitSessionThresholdExceeded"),
        ("MPLS-LDP-MIB", "mplsLdpPathVectorLimitMismatch"),
        ("MPLS-LDP-MIB", "mplsLdpSessionUp"),
        ("MPLS-LDP-MIB", "mplsLdpSessionDown"),
        ("MPLS-LDP-MIB", "mplsLdpLibLspUp"),
        ("MPLS-LDP-MIB", "mplsLdpLibLspDown"))
)
if mibBuilder.loadTexts:
    mplsLdpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsLdpModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 65, 3, 2, 1)
)
mplsLdpModuleCompliance.setObjects(
      *(("MPLS-LDP-MIB", "mplsLdpGeneralGroup"),
        ("MPLS-LDP-MIB", "mplsLdpNotificationsGroup"),
        ("MPLS-LDP-MIB", "mplsLdpAtmGroup"),
        ("MPLS-LDP-MIB", "mplsLdpFrameRelayGroup"),
        ("MPLS-LDP-MIB", "mplsLdpGenericGroup"))
)
if mibBuilder.loadTexts:
    mplsLdpModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-LDP-MIB",
    **{"MplsLsrIdentifier": MplsLsrIdentifier,
       "MplsLdpGenAddr": MplsLdpGenAddr,
       "MplsLabel": MplsLabel,
       "MplsLdpIdentifier": MplsLdpIdentifier,
       "MplsLdpLabelTypes": MplsLdpLabelTypes,
       "AtmVcIdentifier": AtmVcIdentifier,
       "AtmVpIdentifier": AtmVpIdentifier,
       "mplsLdpMIB": mplsLdpMIB,
       "mplsLdpObjects": mplsLdpObjects,
       "mplsLdpLsrObjects": mplsLdpLsrObjects,
       "mplsLdpLsrId": mplsLdpLsrId,
       "mplsLdpLsrLabelRetentionMode": mplsLdpLsrLabelRetentionMode,
       "mplsLdpLsrLoopDetectionCapable": mplsLdpLsrLoopDetectionCapable,
       "mplsLdpEntityObjects": mplsLdpEntityObjects,
       "mplsLdpEntityIndexNext": mplsLdpEntityIndexNext,
       "mplsLdpEntityTable": mplsLdpEntityTable,
       "mplsLdpEntityEntry": mplsLdpEntityEntry,
       "mplsLdpEntityLdpId": mplsLdpEntityLdpId,
       "mplsLdpEntityIndex": mplsLdpEntityIndex,
       "mplsLdpEntityProtocolVersion": mplsLdpEntityProtocolVersion,
       "mplsLdpEntityAdminStatus": mplsLdpEntityAdminStatus,
       "mplsLdpEntityOperStatus": mplsLdpEntityOperStatus,
       "mplsLdpEntityWellKnownDiscoveryPort": mplsLdpEntityWellKnownDiscoveryPort,
       "mplsLdpEntityMaxPduLength": mplsLdpEntityMaxPduLength,
       "mplsLdpEntityKeepAliveHoldTimer": mplsLdpEntityKeepAliveHoldTimer,
       "mplsLdpEntityHelloHoldTimer": mplsLdpEntityHelloHoldTimer,
       "mplsLdpEntityFailedInitSessionTrapEnable": mplsLdpEntityFailedInitSessionTrapEnable,
       "mplsLdpEntityFailedInitSessionThreshold": mplsLdpEntityFailedInitSessionThreshold,
       "mplsLdpEntityLabelDistributionMethod": mplsLdpEntityLabelDistributionMethod,
       "mplsLdpEntityPVLimitMismatchTrapEnable": mplsLdpEntityPVLimitMismatchTrapEnable,
       "mplsLdpEntityPathVectorLimit": mplsLdpEntityPathVectorLimit,
       "mplsLdpEntityHopCountLoopDetection": mplsLdpEntityHopCountLoopDetection,
       "mplsLdpEntityHopCount": mplsLdpEntityHopCount,
       "mplsLdpEntityTargetedPeer": mplsLdpEntityTargetedPeer,
       "mplsLdpEntityTargetedPeerAddrType": mplsLdpEntityTargetedPeerAddrType,
       "mplsLdpEntityTargetedPeerAddr": mplsLdpEntityTargetedPeerAddr,
       "mplsLdpEntityOptionalParameters": mplsLdpEntityOptionalParameters,
       "mplsLdpEntityDiscontinuityTime": mplsLdpEntityDiscontinuityTime,
       "mplsLdpEntityStorageType": mplsLdpEntityStorageType,
       "mplsLdpEntityRowStatus": mplsLdpEntityRowStatus,
       "mplsLdpEntityGenericObjects": mplsLdpEntityGenericObjects,
       "mplsLdpEntityConfGenericTable": mplsLdpEntityConfGenericTable,
       "mplsLdpEntityConfGenericEntry": mplsLdpEntityConfGenericEntry,
       "mplsLdpConfGenericIndex": mplsLdpConfGenericIndex,
       "mplsLdpConfGenericIfIndexOrZero": mplsLdpConfGenericIfIndexOrZero,
       "mplsLdpConfGenericLabel": mplsLdpConfGenericLabel,
       "mplsLdpConfGenericStorageType": mplsLdpConfGenericStorageType,
       "mplsLdpConfGenericRowStatus": mplsLdpConfGenericRowStatus,
       "mplsLdpEntityAtmObjects": mplsLdpEntityAtmObjects,
       "mplsLdpEntityAtmParmsTable": mplsLdpEntityAtmParmsTable,
       "mplsLdpEntityAtmParmsEntry": mplsLdpEntityAtmParmsEntry,
       "mplsLdpEntityAtmIfIndexOrZero": mplsLdpEntityAtmIfIndexOrZero,
       "mplsLdpEntityAtmMergeCap": mplsLdpEntityAtmMergeCap,
       "mplsLdpEntityAtmLabelRangeComponents": mplsLdpEntityAtmLabelRangeComponents,
       "mplsLdpEntityAtmVcDirectionality": mplsLdpEntityAtmVcDirectionality,
       "mplsLdpEntityAtmLsrConnectivity": mplsLdpEntityAtmLsrConnectivity,
       "mplsLdpEntityDefaultControlVpi": mplsLdpEntityDefaultControlVpi,
       "mplsLdpEntityDefaultControlVci": mplsLdpEntityDefaultControlVci,
       "mplsLdpEntityUnlabTrafVpi": mplsLdpEntityUnlabTrafVpi,
       "mplsLdpEntityUnlabTrafVci": mplsLdpEntityUnlabTrafVci,
       "mplsLdpEntityAtmStorageType": mplsLdpEntityAtmStorageType,
       "mplsLdpEntityAtmRowStatus": mplsLdpEntityAtmRowStatus,
       "mplsLdpEntityConfAtmLabelRangeTable": mplsLdpEntityConfAtmLabelRangeTable,
       "mplsLdpEntityConfAtmLabelRangeEntry": mplsLdpEntityConfAtmLabelRangeEntry,
       "mplsLdpEntityConfAtmLabelRangeMinimumVpi": mplsLdpEntityConfAtmLabelRangeMinimumVpi,
       "mplsLdpEntityConfAtmLabelRangeMinimumVci": mplsLdpEntityConfAtmLabelRangeMinimumVci,
       "mplsLdpEntityConfAtmLabelRangeMaximumVpi": mplsLdpEntityConfAtmLabelRangeMaximumVpi,
       "mplsLdpEntityConfAtmLabelRangeMaximumVci": mplsLdpEntityConfAtmLabelRangeMaximumVci,
       "mplsLdpEntityConfAtmLabelRangeStorageType": mplsLdpEntityConfAtmLabelRangeStorageType,
       "mplsLdpEntityConfAtmLabelRangeRowStatus": mplsLdpEntityConfAtmLabelRangeRowStatus,
       "mplsLdpEntityFrameRelayObjects": mplsLdpEntityFrameRelayObjects,
       "mplsLdpEntityFrameRelayParmsTable": mplsLdpEntityFrameRelayParmsTable,
       "mplsLdpEntityFrameRelayParmsEntry": mplsLdpEntityFrameRelayParmsEntry,
       "mplsLdpEntityFrIfIndexOrZero": mplsLdpEntityFrIfIndexOrZero,
       "mplsLdpEntityFrMergeCap": mplsLdpEntityFrMergeCap,
       "mplsLdpEntityFrLabelRangeComponents": mplsLdpEntityFrLabelRangeComponents,
       "mplsLdpEntityFrLen": mplsLdpEntityFrLen,
       "mplsLdpEntityFrVcDirectionality": mplsLdpEntityFrVcDirectionality,
       "mplsLdpEntityFrParmsStorageType": mplsLdpEntityFrParmsStorageType,
       "mplsLdpEntityFrParmsRowStatus": mplsLdpEntityFrParmsRowStatus,
       "mplsLdpEntityConfFrLabelRangeTable": mplsLdpEntityConfFrLabelRangeTable,
       "mplsLdpEntityConfFrLabelRangeEntry": mplsLdpEntityConfFrLabelRangeEntry,
       "mplsLdpConfFrMinimumDlci": mplsLdpConfFrMinimumDlci,
       "mplsLdpConfFrMaximumDlci": mplsLdpConfFrMaximumDlci,
       "mplsLdpConfFrStorageType": mplsLdpConfFrStorageType,
       "mplsLdpConfFrRowStatus": mplsLdpConfFrRowStatus,
       "mplsLdpEntityStatsTable": mplsLdpEntityStatsTable,
       "mplsLdpEntityStatsEntry": mplsLdpEntityStatsEntry,
       "mplsLdpAttemptedSessions": mplsLdpAttemptedSessions,
       "mplsLdpSessionRejectedNoHelloErrors": mplsLdpSessionRejectedNoHelloErrors,
       "mplsLdpSessionRejectedAdvertisementErrors": mplsLdpSessionRejectedAdvertisementErrors,
       "mplsLdpSessionRejectedMaxPduErrors": mplsLdpSessionRejectedMaxPduErrors,
       "mplsLdpSessionRejectedLabelRangeErrors": mplsLdpSessionRejectedLabelRangeErrors,
       "mplsLdpBadLdpIdentifierErrors": mplsLdpBadLdpIdentifierErrors,
       "mplsLdpBadPduLengthErrors": mplsLdpBadPduLengthErrors,
       "mplsLdpBadMessageLengthErrors": mplsLdpBadMessageLengthErrors,
       "mplsLdpBadTlvLengthErrors": mplsLdpBadTlvLengthErrors,
       "mplsLdpMalformedTlvValueErrors": mplsLdpMalformedTlvValueErrors,
       "mplsLdpKeepAliveTimerExpiredErrors": mplsLdpKeepAliveTimerExpiredErrors,
       "mplsLdpShutdownNotifReceived": mplsLdpShutdownNotifReceived,
       "mplsLdpShutdownNotifSent": mplsLdpShutdownNotifSent,
       "mplsLdpEntityPeerObjects": mplsLdpEntityPeerObjects,
       "mplsLdpEntityPeerTable": mplsLdpEntityPeerTable,
       "mplsLdpEntityPeerEntry": mplsLdpEntityPeerEntry,
       "mplsLdpPeerLdpId": mplsLdpPeerLdpId,
       "mplsLdpPeerLabelDistributionMethod": mplsLdpPeerLabelDistributionMethod,
       "mplsLdpPeerLoopDetectionForPV": mplsLdpPeerLoopDetectionForPV,
       "mplsLdpPeerPathVectorLimit": mplsLdpPeerPathVectorLimit,
       "mplsLdpHelloAdjacencyObjects": mplsLdpHelloAdjacencyObjects,
       "mplsLdpHelloAdjacencyTable": mplsLdpHelloAdjacencyTable,
       "mplsLdpHelloAdjacencyEntry": mplsLdpHelloAdjacencyEntry,
       "mplsLdpHelloAdjacencyIndex": mplsLdpHelloAdjacencyIndex,
       "mplsLdpHelloAdjacencyHoldTimeRemaining": mplsLdpHelloAdjacencyHoldTimeRemaining,
       "mplsLdpHelloAdjacencyType": mplsLdpHelloAdjacencyType,
       "mplsLdpSessionObjects": mplsLdpSessionObjects,
       "mplsLdpSessionUpDownTrapEnable": mplsLdpSessionUpDownTrapEnable,
       "mplsLdpSessionTable": mplsLdpSessionTable,
       "mplsLdpSessionEntry": mplsLdpSessionEntry,
       "mplsLdpSessionState": mplsLdpSessionState,
       "mplsLdpSessionProtocolVersion": mplsLdpSessionProtocolVersion,
       "mplsLdpSessionKeepAliveHoldTimeRemaining": mplsLdpSessionKeepAliveHoldTimeRemaining,
       "mplsLdpSessionMaxPduLength": mplsLdpSessionMaxPduLength,
       "mplsLdpSessionDiscontinuityTime": mplsLdpSessionDiscontinuityTime,
       "mplsLdpAtmSessionTable": mplsLdpAtmSessionTable,
       "mplsLdpAtmSessionEntry": mplsLdpAtmSessionEntry,
       "mplsLdpSessionAtmLabelRangeLowerBoundVpi": mplsLdpSessionAtmLabelRangeLowerBoundVpi,
       "mplsLdpSessionAtmLabelRangeLowerBoundVci": mplsLdpSessionAtmLabelRangeLowerBoundVci,
       "mplsLdpSessionAtmLabelRangeUpperBoundVpi": mplsLdpSessionAtmLabelRangeUpperBoundVpi,
       "mplsLdpSessionAtmLabelRangeUpperBoundVci": mplsLdpSessionAtmLabelRangeUpperBoundVci,
       "mplsLdpFrameRelaySessionTable": mplsLdpFrameRelaySessionTable,
       "mplsLdpFrameRelaySessionEntry": mplsLdpFrameRelaySessionEntry,
       "mplsLdpFrSessionMinDlci": mplsLdpFrSessionMinDlci,
       "mplsLdpFrSessionMaxDlci": mplsLdpFrSessionMaxDlci,
       "mplsLdpFrSessionLen": mplsLdpFrSessionLen,
       "mplsLdpSessionStatsTable": mplsLdpSessionStatsTable,
       "mplsLdpSessionStatsEntry": mplsLdpSessionStatsEntry,
       "mplsLdpSessionStatsUnknownMessageTypeErrors": mplsLdpSessionStatsUnknownMessageTypeErrors,
       "mplsLdpSessionStatsUnknownTlvErrors": mplsLdpSessionStatsUnknownTlvErrors,
       "mplsLdpSessionPeerAddressTable": mplsLdpSessionPeerAddressTable,
       "mplsLdpSessionPeerAddressEntry": mplsLdpSessionPeerAddressEntry,
       "mplsLdpSessionPeerAddressIndex": mplsLdpSessionPeerAddressIndex,
       "mplsLdpSessionPeerNextHopAddressType": mplsLdpSessionPeerNextHopAddressType,
       "mplsLdpSessionPeerNextHopAddress": mplsLdpSessionPeerNextHopAddress,
       "mplsLdpLibObjects": mplsLdpLibObjects,
       "mplsLdpLibLspUpDownTrapEnable": mplsLdpLibLspUpDownTrapEnable,
       "mplsLdpLibTable": mplsLdpLibTable,
       "mplsLdpLibEntry": mplsLdpLibEntry,
       "mplsLdpLibLspId": mplsLdpLibLspId,
       "mplsLdpLibLabelInIfIndex": mplsLdpLibLabelInIfIndex,
       "mplsLdpLibLabelOutIfIndex": mplsLdpLibLabelOutIfIndex,
       "mplsLdpLibInLabelType": mplsLdpLibInLabelType,
       "mplsLdpLibInLabel": mplsLdpLibInLabel,
       "mplsLdpLibOutLabelType": mplsLdpLibOutLabelType,
       "mplsLdpLibOutLabel": mplsLdpLibOutLabel,
       "mplsLdpLibOperationStatus": mplsLdpLibOperationStatus,
       "mplsLdpLibLspLastChange": mplsLdpLibLspLastChange,
       "mplsLdpFecTable": mplsLdpFecTable,
       "mplsLdpFecEntry": mplsLdpFecEntry,
       "mplsLdpFecType": mplsLdpFecType,
       "mplsLdpFecAddressFamily": mplsLdpFecAddressFamily,
       "mplsLdpFecAddressLength": mplsLdpFecAddressLength,
       "mplsLdpFecAddress": mplsLdpFecAddress,
       "mplsLdpFecLspId": mplsLdpFecLspId,
       "mplsLdpFecSessionRowPointer": mplsLdpFecSessionRowPointer,
       "mplsLdpNotifications": mplsLdpNotifications,
       "mplsLdpNotificationPrefix": mplsLdpNotificationPrefix,
       "mplsLdpFailedInitSessionThresholdExceeded": mplsLdpFailedInitSessionThresholdExceeded,
       "mplsLdpPathVectorLimitMismatch": mplsLdpPathVectorLimitMismatch,
       "mplsLdpSessionUp": mplsLdpSessionUp,
       "mplsLdpSessionDown": mplsLdpSessionDown,
       "mplsLdpLibLspUp": mplsLdpLibLspUp,
       "mplsLdpLibLspDown": mplsLdpLibLspDown,
       "mplsLdpConformance": mplsLdpConformance,
       "mplsLdpGroups": mplsLdpGroups,
       "mplsLdpGeneralGroup": mplsLdpGeneralGroup,
       "mplsLdpGenericGroup": mplsLdpGenericGroup,
       "mplsLdpAtmGroup": mplsLdpAtmGroup,
       "mplsLdpFrameRelayGroup": mplsLdpFrameRelayGroup,
       "mplsLdpNotificationsGroup": mplsLdpNotificationsGroup,
       "mplsLdpCompliances": mplsLdpCompliances,
       "mplsLdpModuleCompliance": mplsLdpModuleCompliance}
)
