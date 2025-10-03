# SNMP MIB module (DRAFT-MSDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\DRAFT-MSDP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:02:27 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

msdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 92)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Msdp_ObjectIdentity = ObjectIdentity
msdp = _Msdp_ObjectIdentity(
    (1, 3, 6, 1, 3, 92, 1)
)
_MsdpTraps_ObjectIdentity = ObjectIdentity
msdpTraps = _MsdpTraps_ObjectIdentity(
    (1, 3, 6, 1, 3, 92, 1, 0)
)
_MsdpScalars_ObjectIdentity = ObjectIdentity
msdpScalars = _MsdpScalars_ObjectIdentity(
    (1, 3, 6, 1, 3, 92, 1, 1)
)
_MsdpEnabled_Type = TruthValue
_MsdpEnabled_Object = MibScalar
msdpEnabled = _MsdpEnabled_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 1),
    _MsdpEnabled_Type()
)
msdpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msdpEnabled.setStatus("current")
_MsdpCacheLifetime_Type = TimeTicks
_MsdpCacheLifetime_Object = MibScalar
msdpCacheLifetime = _MsdpCacheLifetime_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 2),
    _MsdpCacheLifetime_Type()
)
msdpCacheLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msdpCacheLifetime.setStatus("current")
_MsdpNumSACacheEntries_Type = Gauge32
_MsdpNumSACacheEntries_Object = MibScalar
msdpNumSACacheEntries = _MsdpNumSACacheEntries_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 3),
    _MsdpNumSACacheEntries_Type()
)
msdpNumSACacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpNumSACacheEntries.setStatus("current")


class _MsdpSAHoldDownPeriod_Type(Integer32):
    """Custom type msdpSAHoldDownPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdpSAHoldDownPeriod_Type.__name__ = "Integer32"
_MsdpSAHoldDownPeriod_Object = MibScalar
msdpSAHoldDownPeriod = _MsdpSAHoldDownPeriod_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 4),
    _MsdpSAHoldDownPeriod_Type()
)
msdpSAHoldDownPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpSAHoldDownPeriod.setStatus("current")
if mibBuilder.loadTexts:
    msdpSAHoldDownPeriod.setUnits("seconds")


class _MsdpSAStatePeriod_Type(Integer32):
    """Custom type msdpSAStatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdpSAStatePeriod_Type.__name__ = "Integer32"
_MsdpSAStatePeriod_Object = MibScalar
msdpSAStatePeriod = _MsdpSAStatePeriod_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5),
    _MsdpSAStatePeriod_Type()
)
msdpSAStatePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpSAStatePeriod.setStatus("current")
if mibBuilder.loadTexts:
    msdpSAStatePeriod.setUnits("seconds")
_MsdpRPAddressType_Type = InetAddressType
_MsdpRPAddressType_Object = MibScalar
msdpRPAddressType = _MsdpRPAddressType_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 6),
    _MsdpRPAddressType_Type()
)
msdpRPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msdpRPAddressType.setStatus("current")
_MsdpRPAddress_Type = InetAddress
_MsdpRPAddress_Object = MibScalar
msdpRPAddress = _MsdpRPAddress_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 7),
    _MsdpRPAddress_Type()
)
msdpRPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msdpRPAddress.setStatus("current")
_MsdpRequestsTable_Object = MibTable
msdpRequestsTable = _MsdpRequestsTable_Object(
    (1, 3, 6, 1, 3, 92, 1, 2)
)
if mibBuilder.loadTexts:
    msdpRequestsTable.setStatus("current")
_MsdpRequestsEntry_Object = MibTableRow
msdpRequestsEntry = _MsdpRequestsEntry_Object(
    (1, 3, 6, 1, 3, 92, 1, 2, 1)
)
msdpRequestsEntry.setIndexNames(
    (0, "DRAFT-MSDP-MIB", "msdpRequestsGroupAddressType"),
    (0, "DRAFT-MSDP-MIB", "msdpRequestsGroupAddress"),
    (0, "DRAFT-MSDP-MIB", "msdpRequestsGroupPrefix"),
    (0, "DRAFT-MSDP-MIB", "msdpRequestsPriority"),
)
if mibBuilder.loadTexts:
    msdpRequestsEntry.setStatus("current")
_MsdpRequestsGroupAddressType_Type = InetAddressType
_MsdpRequestsGroupAddressType_Object = MibTableColumn
msdpRequestsGroupAddressType = _MsdpRequestsGroupAddressType_Object(
    (1, 3, 6, 1, 3, 92, 1, 2, 1, 1),
    _MsdpRequestsGroupAddressType_Type()
)
msdpRequestsGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpRequestsGroupAddressType.setStatus("current")


class _MsdpRequestsGroupAddress_Type(InetAddress):
    """Custom type msdpRequestsGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_MsdpRequestsGroupAddress_Type.__name__ = "InetAddress"
_MsdpRequestsGroupAddress_Object = MibTableColumn
msdpRequestsGroupAddress = _MsdpRequestsGroupAddress_Object(
    (1, 3, 6, 1, 3, 92, 1, 2, 1, 2),
    _MsdpRequestsGroupAddress_Type()
)
msdpRequestsGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpRequestsGroupAddress.setStatus("current")
_MsdpRequestsGroupPrefix_Type = InetAddressPrefixLength
_MsdpRequestsGroupPrefix_Object = MibTableColumn
msdpRequestsGroupPrefix = _MsdpRequestsGroupPrefix_Object(
    (1, 3, 6, 1, 3, 92, 1, 2, 1, 3),
    _MsdpRequestsGroupPrefix_Type()
)
msdpRequestsGroupPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpRequestsGroupPrefix.setStatus("current")


class _MsdpRequestsPriority_Type(Integer32):
    """Custom type msdpRequestsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MsdpRequestsPriority_Type.__name__ = "Integer32"
_MsdpRequestsPriority_Object = MibTableColumn
msdpRequestsPriority = _MsdpRequestsPriority_Object(
    (1, 3, 6, 1, 3, 92, 1, 2, 1, 4),
    _MsdpRequestsPriority_Type()
)
msdpRequestsPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpRequestsPriority.setStatus("current")
_MsdpRequestsPeerType_Type = InetAddressType
_MsdpRequestsPeerType_Object = MibTableColumn
msdpRequestsPeerType = _MsdpRequestsPeerType_Object(
    (1, 3, 6, 1, 3, 92, 1, 2, 1, 5),
    _MsdpRequestsPeerType_Type()
)
msdpRequestsPeerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpRequestsPeerType.setStatus("current")
_MsdpRequestsPeer_Type = InetAddress
_MsdpRequestsPeer_Object = MibTableColumn
msdpRequestsPeer = _MsdpRequestsPeer_Object(
    (1, 3, 6, 1, 3, 92, 1, 2, 1, 6),
    _MsdpRequestsPeer_Type()
)
msdpRequestsPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpRequestsPeer.setStatus("current")
_MsdpRequestsStatus_Type = RowStatus
_MsdpRequestsStatus_Object = MibTableColumn
msdpRequestsStatus = _MsdpRequestsStatus_Object(
    (1, 3, 6, 1, 3, 92, 1, 2, 1, 7),
    _MsdpRequestsStatus_Type()
)
msdpRequestsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpRequestsStatus.setStatus("current")
_MsdpPeerTable_Object = MibTable
msdpPeerTable = _MsdpPeerTable_Object(
    (1, 3, 6, 1, 3, 92, 1, 3)
)
if mibBuilder.loadTexts:
    msdpPeerTable.setStatus("current")
_MsdpPeerEntry_Object = MibTableRow
msdpPeerEntry = _MsdpPeerEntry_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1)
)
msdpPeerEntry.setIndexNames(
    (0, "DRAFT-MSDP-MIB", "msdpPeerAddressType"),
    (0, "DRAFT-MSDP-MIB", "msdpPeerRemoteAddress"),
)
if mibBuilder.loadTexts:
    msdpPeerEntry.setStatus("current")
_MsdpPeerAddressType_Type = InetAddressType
_MsdpPeerAddressType_Object = MibTableColumn
msdpPeerAddressType = _MsdpPeerAddressType_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 1),
    _MsdpPeerAddressType_Type()
)
msdpPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpPeerAddressType.setStatus("current")


class _MsdpPeerRemoteAddress_Type(InetAddress):
    """Custom type msdpPeerRemoteAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_MsdpPeerRemoteAddress_Type.__name__ = "InetAddress"
_MsdpPeerRemoteAddress_Object = MibTableColumn
msdpPeerRemoteAddress = _MsdpPeerRemoteAddress_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 2),
    _MsdpPeerRemoteAddress_Type()
)
msdpPeerRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpPeerRemoteAddress.setStatus("current")


class _MsdpPeerState_Type(Integer32):
    """Custom type msdpPeerState based on Integer32"""
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
        *(("inactive", 1),
          ("listen", 2),
          ("connecting", 3),
          ("established", 4),
          ("disabled", 5))
    )


_MsdpPeerState_Type.__name__ = "Integer32"
_MsdpPeerState_Object = MibTableColumn
msdpPeerState = _MsdpPeerState_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 3),
    _MsdpPeerState_Type()
)
msdpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerState.setStatus("current")
_MsdpPeerRPFFailures_Type = Counter32
_MsdpPeerRPFFailures_Object = MibTableColumn
msdpPeerRPFFailures = _MsdpPeerRPFFailures_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 4),
    _MsdpPeerRPFFailures_Type()
)
msdpPeerRPFFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerRPFFailures.setStatus("current")
_MsdpPeerInSAs_Type = Counter32
_MsdpPeerInSAs_Object = MibTableColumn
msdpPeerInSAs = _MsdpPeerInSAs_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 5),
    _MsdpPeerInSAs_Type()
)
msdpPeerInSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerInSAs.setStatus("current")
_MsdpPeerOutSAs_Type = Counter32
_MsdpPeerOutSAs_Object = MibTableColumn
msdpPeerOutSAs = _MsdpPeerOutSAs_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 6),
    _MsdpPeerOutSAs_Type()
)
msdpPeerOutSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerOutSAs.setStatus("current")
_MsdpPeerInSARequests_Type = Counter32
_MsdpPeerInSARequests_Object = MibTableColumn
msdpPeerInSARequests = _MsdpPeerInSARequests_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 7),
    _MsdpPeerInSARequests_Type()
)
msdpPeerInSARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerInSARequests.setStatus("current")
_MsdpPeerOutSARequests_Type = Counter32
_MsdpPeerOutSARequests_Object = MibTableColumn
msdpPeerOutSARequests = _MsdpPeerOutSARequests_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 8),
    _MsdpPeerOutSARequests_Type()
)
msdpPeerOutSARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerOutSARequests.setStatus("current")
_MsdpPeerInSAResponses_Type = Counter32
_MsdpPeerInSAResponses_Object = MibTableColumn
msdpPeerInSAResponses = _MsdpPeerInSAResponses_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 9),
    _MsdpPeerInSAResponses_Type()
)
msdpPeerInSAResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerInSAResponses.setStatus("current")
_MsdpPeerOutSAResponses_Type = Counter32
_MsdpPeerOutSAResponses_Object = MibTableColumn
msdpPeerOutSAResponses = _MsdpPeerOutSAResponses_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 10),
    _MsdpPeerOutSAResponses_Type()
)
msdpPeerOutSAResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerOutSAResponses.setStatus("current")
_MsdpPeerInControlMessages_Type = Counter32
_MsdpPeerInControlMessages_Object = MibTableColumn
msdpPeerInControlMessages = _MsdpPeerInControlMessages_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 11),
    _MsdpPeerInControlMessages_Type()
)
msdpPeerInControlMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerInControlMessages.setStatus("current")
_MsdpPeerOutControlMessages_Type = Counter32
_MsdpPeerOutControlMessages_Object = MibTableColumn
msdpPeerOutControlMessages = _MsdpPeerOutControlMessages_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 12),
    _MsdpPeerOutControlMessages_Type()
)
msdpPeerOutControlMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerOutControlMessages.setStatus("current")
_MsdpPeerInDataPackets_Type = Counter32
_MsdpPeerInDataPackets_Object = MibTableColumn
msdpPeerInDataPackets = _MsdpPeerInDataPackets_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 13),
    _MsdpPeerInDataPackets_Type()
)
msdpPeerInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerInDataPackets.setStatus("current")
_MsdpPeerOutDataPackets_Type = Counter32
_MsdpPeerOutDataPackets_Object = MibTableColumn
msdpPeerOutDataPackets = _MsdpPeerOutDataPackets_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 14),
    _MsdpPeerOutDataPackets_Type()
)
msdpPeerOutDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerOutDataPackets.setStatus("current")
_MsdpPeerFsmEstablishedTransitions_Type = Counter32
_MsdpPeerFsmEstablishedTransitions_Object = MibTableColumn
msdpPeerFsmEstablishedTransitions = _MsdpPeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 15),
    _MsdpPeerFsmEstablishedTransitions_Type()
)
msdpPeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerFsmEstablishedTransitions.setStatus("current")
_MsdpPeerFsmEstablishedTime_Type = TimeStamp
_MsdpPeerFsmEstablishedTime_Object = MibTableColumn
msdpPeerFsmEstablishedTime = _MsdpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 16),
    _MsdpPeerFsmEstablishedTime_Type()
)
msdpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerFsmEstablishedTime.setStatus("current")
_MsdpPeerInMessageTime_Type = TimeStamp
_MsdpPeerInMessageTime_Object = MibTableColumn
msdpPeerInMessageTime = _MsdpPeerInMessageTime_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 17),
    _MsdpPeerInMessageTime_Type()
)
msdpPeerInMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerInMessageTime.setStatus("current")
_MsdpPeerLocalAddress_Type = InetAddress
_MsdpPeerLocalAddress_Object = MibTableColumn
msdpPeerLocalAddress = _MsdpPeerLocalAddress_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 18),
    _MsdpPeerLocalAddress_Type()
)
msdpPeerLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerLocalAddress.setStatus("current")


class _MsdpPeerConnectRetryInterval_Type(Integer32):
    """Custom type msdpPeerConnectRetryInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MsdpPeerConnectRetryInterval_Type.__name__ = "Integer32"
_MsdpPeerConnectRetryInterval_Object = MibTableColumn
msdpPeerConnectRetryInterval = _MsdpPeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 19),
    _MsdpPeerConnectRetryInterval_Type()
)
msdpPeerConnectRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerConnectRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    msdpPeerConnectRetryInterval.setUnits("seconds")


class _MsdpPeerHoldTimeConfigured_Type(Integer32):
    """Custom type msdpPeerHoldTimeConfigured based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_MsdpPeerHoldTimeConfigured_Type.__name__ = "Integer32"
_MsdpPeerHoldTimeConfigured_Object = MibTableColumn
msdpPeerHoldTimeConfigured = _MsdpPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 20),
    _MsdpPeerHoldTimeConfigured_Type()
)
msdpPeerHoldTimeConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerHoldTimeConfigured.setStatus("current")
if mibBuilder.loadTexts:
    msdpPeerHoldTimeConfigured.setUnits("seconds")


class _MsdpPeerKeepAliveConfigured_Type(Integer32):
    """Custom type msdpPeerKeepAliveConfigured based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_MsdpPeerKeepAliveConfigured_Type.__name__ = "Integer32"
_MsdpPeerKeepAliveConfigured_Object = MibTableColumn
msdpPeerKeepAliveConfigured = _MsdpPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 21),
    _MsdpPeerKeepAliveConfigured_Type()
)
msdpPeerKeepAliveConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerKeepAliveConfigured.setStatus("current")
if mibBuilder.loadTexts:
    msdpPeerKeepAliveConfigured.setUnits("seconds")


class _MsdpPeerDataTtl_Type(Integer32):
    """Custom type msdpPeerDataTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsdpPeerDataTtl_Type.__name__ = "Integer32"
_MsdpPeerDataTtl_Object = MibTableColumn
msdpPeerDataTtl = _MsdpPeerDataTtl_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 22),
    _MsdpPeerDataTtl_Type()
)
msdpPeerDataTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerDataTtl.setStatus("current")
_MsdpPeerProcessRequestsFrom_Type = TruthValue
_MsdpPeerProcessRequestsFrom_Object = MibTableColumn
msdpPeerProcessRequestsFrom = _MsdpPeerProcessRequestsFrom_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 23),
    _MsdpPeerProcessRequestsFrom_Type()
)
msdpPeerProcessRequestsFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerProcessRequestsFrom.setStatus("current")
_MsdpPeerStatus_Type = RowStatus
_MsdpPeerStatus_Object = MibTableColumn
msdpPeerStatus = _MsdpPeerStatus_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 24),
    _MsdpPeerStatus_Type()
)
msdpPeerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerStatus.setStatus("current")
_MsdpPeerRemotePort_Type = InetPortNumber
_MsdpPeerRemotePort_Object = MibTableColumn
msdpPeerRemotePort = _MsdpPeerRemotePort_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 25),
    _MsdpPeerRemotePort_Type()
)
msdpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerRemotePort.setStatus("current")
_MsdpPeerLocalPort_Type = InetPortNumber
_MsdpPeerLocalPort_Object = MibTableColumn
msdpPeerLocalPort = _MsdpPeerLocalPort_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 26),
    _MsdpPeerLocalPort_Type()
)
msdpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerLocalPort.setStatus("current")


class _MsdpPeerEncapsulationType_Type(Integer32):
    """Custom type msdpPeerEncapsulationType based on Integer32"""
    defaultValue = 3

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
          ("tcp", 1),
          ("udp", 2),
          ("gre", 3))
    )


_MsdpPeerEncapsulationType_Type.__name__ = "Integer32"
_MsdpPeerEncapsulationType_Object = MibTableColumn
msdpPeerEncapsulationType = _MsdpPeerEncapsulationType_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 27),
    _MsdpPeerEncapsulationType_Type()
)
msdpPeerEncapsulationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerEncapsulationType.setStatus("current")
_MsdpPeerConnectionAttempts_Type = Counter32
_MsdpPeerConnectionAttempts_Object = MibTableColumn
msdpPeerConnectionAttempts = _MsdpPeerConnectionAttempts_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 28),
    _MsdpPeerConnectionAttempts_Type()
)
msdpPeerConnectionAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerConnectionAttempts.setStatus("current")
_MsdpPeerInNotifications_Type = Counter32
_MsdpPeerInNotifications_Object = MibTableColumn
msdpPeerInNotifications = _MsdpPeerInNotifications_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 29),
    _MsdpPeerInNotifications_Type()
)
msdpPeerInNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerInNotifications.setStatus("current")
_MsdpPeerOutNotifications_Type = Counter32
_MsdpPeerOutNotifications_Object = MibTableColumn
msdpPeerOutNotifications = _MsdpPeerOutNotifications_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 30),
    _MsdpPeerOutNotifications_Type()
)
msdpPeerOutNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerOutNotifications.setStatus("current")


class _MsdpPeerLastError_Type(OctetString):
    """Custom type msdpPeerLastError based on OctetString"""
    defaultHexValue = "0000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_MsdpPeerLastError_Type.__name__ = "OctetString"
_MsdpPeerLastError_Object = MibTableColumn
msdpPeerLastError = _MsdpPeerLastError_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 31),
    _MsdpPeerLastError_Type()
)
msdpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerLastError.setStatus("current")


class _MsdpPeerIfIndex_Type(InterfaceIndexOrZero):
    """Custom type msdpPeerIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_MsdpPeerIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_MsdpPeerIfIndex_Object = MibTableColumn
msdpPeerIfIndex = _MsdpPeerIfIndex_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 32),
    _MsdpPeerIfIndex_Type()
)
msdpPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerIfIndex.setStatus("current")
_MsdpPeerDiscontinuityTime_Type = TimeStamp
_MsdpPeerDiscontinuityTime_Object = MibTableColumn
msdpPeerDiscontinuityTime = _MsdpPeerDiscontinuityTime_Object(
    (1, 3, 6, 1, 3, 92, 1, 3, 1, 33),
    _MsdpPeerDiscontinuityTime_Type()
)
msdpPeerDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerDiscontinuityTime.setStatus("current")
_MsdpSACacheTable_Object = MibTable
msdpSACacheTable = _MsdpSACacheTable_Object(
    (1, 3, 6, 1, 3, 92, 1, 4)
)
if mibBuilder.loadTexts:
    msdpSACacheTable.setStatus("current")
_MsdpSACacheEntry_Object = MibTableRow
msdpSACacheEntry = _MsdpSACacheEntry_Object(
    (1, 3, 6, 1, 3, 92, 1, 4, 1)
)
msdpSACacheEntry.setIndexNames(
    (0, "DRAFT-MSDP-MIB", "msdpSACacheAddrType"),
    (0, "DRAFT-MSDP-MIB", "msdpSACacheGroupAddr"),
    (0, "DRAFT-MSDP-MIB", "msdpSACacheSourceAddr"),
    (0, "DRAFT-MSDP-MIB", "msdpSACacheSourcePrefix"),
    (0, "DRAFT-MSDP-MIB", "msdpSACacheOriginRP"),
)
if mibBuilder.loadTexts:
    msdpSACacheEntry.setStatus("current")
_MsdpSACacheAddrType_Type = InetAddressType
_MsdpSACacheAddrType_Object = MibTableColumn
msdpSACacheAddrType = _MsdpSACacheAddrType_Object(
    (1, 3, 6, 1, 3, 92, 1, 4, 1, 1),
    _MsdpSACacheAddrType_Type()
)
msdpSACacheAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpSACacheAddrType.setStatus("current")


class _MsdpSACacheGroupAddr_Type(InetAddress):
    """Custom type msdpSACacheGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_MsdpSACacheGroupAddr_Type.__name__ = "InetAddress"
_MsdpSACacheGroupAddr_Object = MibTableColumn
msdpSACacheGroupAddr = _MsdpSACacheGroupAddr_Object(
    (1, 3, 6, 1, 3, 92, 1, 4, 1, 2),
    _MsdpSACacheGroupAddr_Type()
)
msdpSACacheGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpSACacheGroupAddr.setStatus("current")


class _MsdpSACacheSourceAddr_Type(InetAddress):
    """Custom type msdpSACacheSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_MsdpSACacheSourceAddr_Type.__name__ = "InetAddress"
_MsdpSACacheSourceAddr_Object = MibTableColumn
msdpSACacheSourceAddr = _MsdpSACacheSourceAddr_Object(
    (1, 3, 6, 1, 3, 92, 1, 4, 1, 3),
    _MsdpSACacheSourceAddr_Type()
)
msdpSACacheSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpSACacheSourceAddr.setStatus("current")
_MsdpSACacheSourcePrefix_Type = InetAddressPrefixLength
_MsdpSACacheSourcePrefix_Object = MibTableColumn
msdpSACacheSourcePrefix = _MsdpSACacheSourcePrefix_Object(
    (1, 3, 6, 1, 3, 92, 1, 4, 1, 4),
    _MsdpSACacheSourcePrefix_Type()
)
msdpSACacheSourcePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpSACacheSourcePrefix.setStatus("current")


class _MsdpSACacheOriginRP_Type(InetAddress):
    """Custom type msdpSACacheOriginRP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_MsdpSACacheOriginRP_Type.__name__ = "InetAddress"
_MsdpSACacheOriginRP_Object = MibTableColumn
msdpSACacheOriginRP = _MsdpSACacheOriginRP_Object(
    (1, 3, 6, 1, 3, 92, 1, 4, 1, 5),
    _MsdpSACacheOriginRP_Type()
)
msdpSACacheOriginRP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpSACacheOriginRP.setStatus("current")
_MsdpSACachePeerLearnedFrom_Type = InetAddress
_MsdpSACachePeerLearnedFrom_Object = MibTableColumn
msdpSACachePeerLearnedFrom = _MsdpSACachePeerLearnedFrom_Object(
    (1, 3, 6, 1, 3, 92, 1, 4, 1, 6),
    _MsdpSACachePeerLearnedFrom_Type()
)
msdpSACachePeerLearnedFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpSACachePeerLearnedFrom.setStatus("current")
_MsdpSACacheRPFPeer_Type = InetAddress
_MsdpSACacheRPFPeer_Object = MibTableColumn
msdpSACacheRPFPeer = _MsdpSACacheRPFPeer_Object(
    (1, 3, 6, 1, 3, 92, 1, 4, 1, 7),
    _MsdpSACacheRPFPeer_Type()
)
msdpSACacheRPFPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpSACacheRPFPeer.setStatus("current")
_MsdpSACacheInSAs_Type = Counter32
_MsdpSACacheInSAs_Object = MibTableColumn
msdpSACacheInSAs = _MsdpSACacheInSAs_Object(
    (1, 3, 6, 1, 3, 92, 1, 4, 1, 8),
    _MsdpSACacheInSAs_Type()
)
msdpSACacheInSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpSACacheInSAs.setStatus("current")
_MsdpSACacheInDataPackets_Type = Counter32
_MsdpSACacheInDataPackets_Object = MibTableColumn
msdpSACacheInDataPackets = _MsdpSACacheInDataPackets_Object(
    (1, 3, 6, 1, 3, 92, 1, 4, 1, 9),
    _MsdpSACacheInDataPackets_Type()
)
msdpSACacheInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpSACacheInDataPackets.setStatus("current")
_MsdpSACacheUpTime_Type = TimeTicks
_MsdpSACacheUpTime_Object = MibTableColumn
msdpSACacheUpTime = _MsdpSACacheUpTime_Object(
    (1, 3, 6, 1, 3, 92, 1, 4, 1, 10),
    _MsdpSACacheUpTime_Type()
)
msdpSACacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpSACacheUpTime.setStatus("current")
_MsdpSACacheExpiryTime_Type = TimeTicks
_MsdpSACacheExpiryTime_Object = MibTableColumn
msdpSACacheExpiryTime = _MsdpSACacheExpiryTime_Object(
    (1, 3, 6, 1, 3, 92, 1, 4, 1, 11),
    _MsdpSACacheExpiryTime_Type()
)
msdpSACacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpSACacheExpiryTime.setStatus("current")
_MsdpSACacheStatus_Type = RowStatus
_MsdpSACacheStatus_Object = MibTableColumn
msdpSACacheStatus = _MsdpSACacheStatus_Object(
    (1, 3, 6, 1, 3, 92, 1, 4, 1, 12),
    _MsdpSACacheStatus_Type()
)
msdpSACacheStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msdpSACacheStatus.setStatus("current")
_MsdpMeshGroupTable_Object = MibTable
msdpMeshGroupTable = _MsdpMeshGroupTable_Object(
    (1, 3, 6, 1, 3, 92, 1, 5)
)
if mibBuilder.loadTexts:
    msdpMeshGroupTable.setStatus("current")
_MsdpMeshGroupEntry_Object = MibTableRow
msdpMeshGroupEntry = _MsdpMeshGroupEntry_Object(
    (1, 3, 6, 1, 3, 92, 1, 5, 1)
)
msdpMeshGroupEntry.setIndexNames(
    (0, "DRAFT-MSDP-MIB", "msdpMeshGroupName"),
    (0, "DRAFT-MSDP-MIB", "msdpMeshGroupPeerAddressType"),
    (0, "DRAFT-MSDP-MIB", "msdpMeshGroupPeerAddress"),
)
if mibBuilder.loadTexts:
    msdpMeshGroupEntry.setStatus("current")


class _MsdpMeshGroupName_Type(DisplayString):
    """Custom type msdpMeshGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MsdpMeshGroupName_Type.__name__ = "DisplayString"
_MsdpMeshGroupName_Object = MibTableColumn
msdpMeshGroupName = _MsdpMeshGroupName_Object(
    (1, 3, 6, 1, 3, 92, 1, 5, 1, 1),
    _MsdpMeshGroupName_Type()
)
msdpMeshGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpMeshGroupName.setStatus("current")
_MsdpMeshGroupPeerAddressType_Type = InetAddressType
_MsdpMeshGroupPeerAddressType_Object = MibTableColumn
msdpMeshGroupPeerAddressType = _MsdpMeshGroupPeerAddressType_Object(
    (1, 3, 6, 1, 3, 92, 1, 5, 1, 2),
    _MsdpMeshGroupPeerAddressType_Type()
)
msdpMeshGroupPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpMeshGroupPeerAddressType.setStatus("current")


class _MsdpMeshGroupPeerAddress_Type(InetAddress):
    """Custom type msdpMeshGroupPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_MsdpMeshGroupPeerAddress_Type.__name__ = "InetAddress"
_MsdpMeshGroupPeerAddress_Object = MibTableColumn
msdpMeshGroupPeerAddress = _MsdpMeshGroupPeerAddress_Object(
    (1, 3, 6, 1, 3, 92, 1, 5, 1, 3),
    _MsdpMeshGroupPeerAddress_Type()
)
msdpMeshGroupPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpMeshGroupPeerAddress.setStatus("current")
_MsdpMeshGroupStatus_Type = RowStatus
_MsdpMeshGroupStatus_Object = MibTableColumn
msdpMeshGroupStatus = _MsdpMeshGroupStatus_Object(
    (1, 3, 6, 1, 3, 92, 1, 5, 1, 4),
    _MsdpMeshGroupStatus_Type()
)
msdpMeshGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpMeshGroupStatus.setStatus("current")
_MsdpMIBConformance_ObjectIdentity = ObjectIdentity
msdpMIBConformance = _MsdpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 92, 1, 6)
)
_MsdpMIBCompliances_ObjectIdentity = ObjectIdentity
msdpMIBCompliances = _MsdpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 92, 1, 6, 1)
)
_MsdpMIBGroups_ObjectIdentity = ObjectIdentity
msdpMIBGroups = _MsdpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 92, 1, 6, 2)
)

# Managed Objects groups

msdpMIBGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 6, 2, 1)
)
msdpMIBGlobalsGroup.setObjects(
    ("DRAFT-MSDP-MIB", "msdpEnabled")
)
if mibBuilder.loadTexts:
    msdpMIBGlobalsGroup.setStatus("current")

msdpMIBPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 6, 2, 2)
)
msdpMIBPeerGroup.setObjects(
      *(("DRAFT-MSDP-MIB", "msdpPeerRPFFailures"),
        ("DRAFT-MSDP-MIB", "msdpPeerState"),
        ("DRAFT-MSDP-MIB", "msdpPeerInSAs"),
        ("DRAFT-MSDP-MIB", "msdpPeerOutSAs"),
        ("DRAFT-MSDP-MIB", "msdpPeerInSARequests"),
        ("DRAFT-MSDP-MIB", "msdpPeerOutSARequests"),
        ("DRAFT-MSDP-MIB", "msdpPeerInSAResponses"),
        ("DRAFT-MSDP-MIB", "msdpPeerOutSAResponses"),
        ("DRAFT-MSDP-MIB", "msdpPeerInNotifications"),
        ("DRAFT-MSDP-MIB", "msdpPeerOutNotifications"),
        ("DRAFT-MSDP-MIB", "msdpPeerInControlMessages"),
        ("DRAFT-MSDP-MIB", "msdpPeerOutControlMessages"),
        ("DRAFT-MSDP-MIB", "msdpPeerFsmEstablishedTransitions"),
        ("DRAFT-MSDP-MIB", "msdpPeerFsmEstablishedTime"),
        ("DRAFT-MSDP-MIB", "msdpPeerLocalAddress"),
        ("DRAFT-MSDP-MIB", "msdpPeerRemotePort"),
        ("DRAFT-MSDP-MIB", "msdpPeerLocalPort"),
        ("DRAFT-MSDP-MIB", "msdpPeerConnectRetryInterval"),
        ("DRAFT-MSDP-MIB", "msdpPeerHoldTimeConfigured"),
        ("DRAFT-MSDP-MIB", "msdpPeerKeepAliveConfigured"),
        ("DRAFT-MSDP-MIB", "msdpPeerInMessageTime"),
        ("DRAFT-MSDP-MIB", "msdpPeerProcessRequestsFrom"),
        ("DRAFT-MSDP-MIB", "msdpPeerConnectionAttempts"),
        ("DRAFT-MSDP-MIB", "msdpPeerLastError"),
        ("DRAFT-MSDP-MIB", "msdpPeerIfIndex"),
        ("DRAFT-MSDP-MIB", "msdpPeerStatus"),
        ("DRAFT-MSDP-MIB", "msdpPeerDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    msdpMIBPeerGroup.setStatus("current")

msdpMIBEncapsulationGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 6, 2, 3)
)
msdpMIBEncapsulationGroup.setObjects(
      *(("DRAFT-MSDP-MIB", "msdpPeerInDataPackets"),
        ("DRAFT-MSDP-MIB", "msdpPeerOutDataPackets"),
        ("DRAFT-MSDP-MIB", "msdpPeerDataTtl"),
        ("DRAFT-MSDP-MIB", "msdpPeerEncapsulationType"))
)
if mibBuilder.loadTexts:
    msdpMIBEncapsulationGroup.setStatus("current")

msdpMIBSACacheGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 6, 2, 4)
)
msdpMIBSACacheGroup.setObjects(
      *(("DRAFT-MSDP-MIB", "msdpCacheLifetime"),
        ("DRAFT-MSDP-MIB", "msdpNumSACacheEntries"),
        ("DRAFT-MSDP-MIB", "msdpSAHoldDownPeriod"),
        ("DRAFT-MSDP-MIB", "msdpSAStatePeriod"),
        ("DRAFT-MSDP-MIB", "msdpSACachePeerLearnedFrom"),
        ("DRAFT-MSDP-MIB", "msdpSACacheRPFPeer"),
        ("DRAFT-MSDP-MIB", "msdpSACacheInSAs"),
        ("DRAFT-MSDP-MIB", "msdpSACacheInDataPackets"),
        ("DRAFT-MSDP-MIB", "msdpSACacheUpTime"),
        ("DRAFT-MSDP-MIB", "msdpSACacheExpiryTime"),
        ("DRAFT-MSDP-MIB", "msdpSACacheStatus"))
)
if mibBuilder.loadTexts:
    msdpMIBSACacheGroup.setStatus("current")

msdpMIBRequestsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 6, 2, 6)
)
msdpMIBRequestsGroup.setObjects(
      *(("DRAFT-MSDP-MIB", "msdpRequestsPeerType"),
        ("DRAFT-MSDP-MIB", "msdpRequestsPeer"),
        ("DRAFT-MSDP-MIB", "msdpRequestsStatus"))
)
if mibBuilder.loadTexts:
    msdpMIBRequestsGroup.setStatus("current")

msdpMIBRPGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 6, 2, 7)
)
msdpMIBRPGroup.setObjects(
      *(("DRAFT-MSDP-MIB", "msdpRPAddressType"),
        ("DRAFT-MSDP-MIB", "msdpRPAddress"))
)
if mibBuilder.loadTexts:
    msdpMIBRPGroup.setStatus("current")

msdpMIBMeshGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 6, 2, 8)
)
msdpMIBMeshGroupGroup.setObjects(
    ("DRAFT-MSDP-MIB", "msdpMeshGroupStatus")
)
if mibBuilder.loadTexts:
    msdpMIBMeshGroupGroup.setStatus("current")


# Notification objects

msdpEstablished = NotificationType(
    (1, 3, 6, 1, 3, 92, 1, 0, 1)
)
msdpEstablished.setObjects(
    ("DRAFT-MSDP-MIB", "msdpPeerFsmEstablishedTransitions")
)
if mibBuilder.loadTexts:
    msdpEstablished.setStatus(
        "current"
    )

msdpBackwardTransition = NotificationType(
    (1, 3, 6, 1, 3, 92, 1, 0, 2)
)
msdpBackwardTransition.setObjects(
    ("DRAFT-MSDP-MIB", "msdpPeerState")
)
if mibBuilder.loadTexts:
    msdpBackwardTransition.setStatus(
        "current"
    )


# Notifications groups

msdpMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 92, 1, 6, 2, 5)
)
msdpMIBNotificationGroup.setObjects(
      *(("DRAFT-MSDP-MIB", "msdpEstablished"),
        ("DRAFT-MSDP-MIB", "msdpBackwardTransition"))
)
if mibBuilder.loadTexts:
    msdpMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

msdpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 92, 1, 6, 1, 1)
)
msdpMIBCompliance.setObjects(
      *(("DRAFT-MSDP-MIB", "msdpMIBGlobalsGroup"),
        ("DRAFT-MSDP-MIB", "msdpMIBPeerGroup"),
        ("DRAFT-MSDP-MIB", "msdpMIBNotificationGroup"),
        ("DRAFT-MSDP-MIB", "msdpMIBEncapsulationGroup"),
        ("DRAFT-MSDP-MIB", "msdpMIBSACacheGroup"),
        ("DRAFT-MSDP-MIB", "msdpMIBRequestsGroup"),
        ("DRAFT-MSDP-MIB", "msdpMIBRPGroup"),
        ("DRAFT-MSDP-MIB", "msdpMIBMeshGroupGroup"))
)
if mibBuilder.loadTexts:
    msdpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DRAFT-MSDP-MIB",
    **{"msdpMIB": msdpMIB,
       "msdp": msdp,
       "msdpTraps": msdpTraps,
       "msdpEstablished": msdpEstablished,
       "msdpBackwardTransition": msdpBackwardTransition,
       "msdpScalars": msdpScalars,
       "msdpEnabled": msdpEnabled,
       "msdpCacheLifetime": msdpCacheLifetime,
       "msdpNumSACacheEntries": msdpNumSACacheEntries,
       "msdpSAHoldDownPeriod": msdpSAHoldDownPeriod,
       "msdpSAStatePeriod": msdpSAStatePeriod,
       "msdpRPAddressType": msdpRPAddressType,
       "msdpRPAddress": msdpRPAddress,
       "msdpRequestsTable": msdpRequestsTable,
       "msdpRequestsEntry": msdpRequestsEntry,
       "msdpRequestsGroupAddressType": msdpRequestsGroupAddressType,
       "msdpRequestsGroupAddress": msdpRequestsGroupAddress,
       "msdpRequestsGroupPrefix": msdpRequestsGroupPrefix,
       "msdpRequestsPriority": msdpRequestsPriority,
       "msdpRequestsPeerType": msdpRequestsPeerType,
       "msdpRequestsPeer": msdpRequestsPeer,
       "msdpRequestsStatus": msdpRequestsStatus,
       "msdpPeerTable": msdpPeerTable,
       "msdpPeerEntry": msdpPeerEntry,
       "msdpPeerAddressType": msdpPeerAddressType,
       "msdpPeerRemoteAddress": msdpPeerRemoteAddress,
       "msdpPeerState": msdpPeerState,
       "msdpPeerRPFFailures": msdpPeerRPFFailures,
       "msdpPeerInSAs": msdpPeerInSAs,
       "msdpPeerOutSAs": msdpPeerOutSAs,
       "msdpPeerInSARequests": msdpPeerInSARequests,
       "msdpPeerOutSARequests": msdpPeerOutSARequests,
       "msdpPeerInSAResponses": msdpPeerInSAResponses,
       "msdpPeerOutSAResponses": msdpPeerOutSAResponses,
       "msdpPeerInControlMessages": msdpPeerInControlMessages,
       "msdpPeerOutControlMessages": msdpPeerOutControlMessages,
       "msdpPeerInDataPackets": msdpPeerInDataPackets,
       "msdpPeerOutDataPackets": msdpPeerOutDataPackets,
       "msdpPeerFsmEstablishedTransitions": msdpPeerFsmEstablishedTransitions,
       "msdpPeerFsmEstablishedTime": msdpPeerFsmEstablishedTime,
       "msdpPeerInMessageTime": msdpPeerInMessageTime,
       "msdpPeerLocalAddress": msdpPeerLocalAddress,
       "msdpPeerConnectRetryInterval": msdpPeerConnectRetryInterval,
       "msdpPeerHoldTimeConfigured": msdpPeerHoldTimeConfigured,
       "msdpPeerKeepAliveConfigured": msdpPeerKeepAliveConfigured,
       "msdpPeerDataTtl": msdpPeerDataTtl,
       "msdpPeerProcessRequestsFrom": msdpPeerProcessRequestsFrom,
       "msdpPeerStatus": msdpPeerStatus,
       "msdpPeerRemotePort": msdpPeerRemotePort,
       "msdpPeerLocalPort": msdpPeerLocalPort,
       "msdpPeerEncapsulationType": msdpPeerEncapsulationType,
       "msdpPeerConnectionAttempts": msdpPeerConnectionAttempts,
       "msdpPeerInNotifications": msdpPeerInNotifications,
       "msdpPeerOutNotifications": msdpPeerOutNotifications,
       "msdpPeerLastError": msdpPeerLastError,
       "msdpPeerIfIndex": msdpPeerIfIndex,
       "msdpPeerDiscontinuityTime": msdpPeerDiscontinuityTime,
       "msdpSACacheTable": msdpSACacheTable,
       "msdpSACacheEntry": msdpSACacheEntry,
       "msdpSACacheAddrType": msdpSACacheAddrType,
       "msdpSACacheGroupAddr": msdpSACacheGroupAddr,
       "msdpSACacheSourceAddr": msdpSACacheSourceAddr,
       "msdpSACacheSourcePrefix": msdpSACacheSourcePrefix,
       "msdpSACacheOriginRP": msdpSACacheOriginRP,
       "msdpSACachePeerLearnedFrom": msdpSACachePeerLearnedFrom,
       "msdpSACacheRPFPeer": msdpSACacheRPFPeer,
       "msdpSACacheInSAs": msdpSACacheInSAs,
       "msdpSACacheInDataPackets": msdpSACacheInDataPackets,
       "msdpSACacheUpTime": msdpSACacheUpTime,
       "msdpSACacheExpiryTime": msdpSACacheExpiryTime,
       "msdpSACacheStatus": msdpSACacheStatus,
       "msdpMeshGroupTable": msdpMeshGroupTable,
       "msdpMeshGroupEntry": msdpMeshGroupEntry,
       "msdpMeshGroupName": msdpMeshGroupName,
       "msdpMeshGroupPeerAddressType": msdpMeshGroupPeerAddressType,
       "msdpMeshGroupPeerAddress": msdpMeshGroupPeerAddress,
       "msdpMeshGroupStatus": msdpMeshGroupStatus,
       "msdpMIBConformance": msdpMIBConformance,
       "msdpMIBCompliances": msdpMIBCompliances,
       "msdpMIBCompliance": msdpMIBCompliance,
       "msdpMIBGroups": msdpMIBGroups,
       "msdpMIBGlobalsGroup": msdpMIBGlobalsGroup,
       "msdpMIBPeerGroup": msdpMIBPeerGroup,
       "msdpMIBEncapsulationGroup": msdpMIBEncapsulationGroup,
       "msdpMIBSACacheGroup": msdpMIBSACacheGroup,
       "msdpMIBNotificationGroup": msdpMIBNotificationGroup,
       "msdpMIBRequestsGroup": msdpMIBRequestsGroup,
       "msdpMIBRPGroup": msdpMIBRPGroup,
       "msdpMIBMeshGroupGroup": msdpMIBMeshGroupGroup}
)
