# SNMP MIB module (CORERO-CMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\corero\CORERO-CMS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:31 2025
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
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

coreroCMSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4)
)
if mibBuilder.loadTexts:
    coreroCMSMIB.setRevisions(
        ("2017-06-16 00:00",
         "2016-01-28 00:00",
         "2014-04-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class TYPE_CMS_MODULE_STATE(String):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Corero_ObjectIdentity = ObjectIdentity
corero = _Corero_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41036)
)
_CoreroCMSMIBObjects_ObjectIdentity = ObjectIdentity
coreroCMSMIBObjects = _CoreroCMSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1)
)
_Defense_ObjectIdentity = ObjectIdentity
defense = _Defense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1)
)
_DefenseStatus_ObjectIdentity = ObjectIdentity
defenseStatus = _DefenseStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 1)
)
_DefenseStatusThreatAwareness_ObjectIdentity = ObjectIdentity
defenseStatusThreatAwareness = _DefenseStatusThreatAwareness_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 1, 1)
)


class _ExcessivePacketsFromBadClients_Type(TruthValue):
    """Custom type excessivePacketsFromBadClients based on TruthValue"""
    defaultValue = 2


_ExcessivePacketsFromBadClients_Type.__name__ = "TruthValue"
_ExcessivePacketsFromBadClients_Object = MibScalar
excessivePacketsFromBadClients = _ExcessivePacketsFromBadClients_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 1, 1, 1),
    _ExcessivePacketsFromBadClients_Type()
)
excessivePacketsFromBadClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excessivePacketsFromBadClients.setStatus("current")


class _ExcessiveProxySetupRate_Type(TruthValue):
    """Custom type excessiveProxySetupRate based on TruthValue"""
    defaultValue = 2


_ExcessiveProxySetupRate_Type.__name__ = "TruthValue"
_ExcessiveProxySetupRate_Object = MibScalar
excessiveProxySetupRate = _ExcessiveProxySetupRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 1, 1, 2),
    _ExcessiveProxySetupRate_Type()
)
excessiveProxySetupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excessiveProxySetupRate.setStatus("obsolete")


class _ExcessiveNewIpAddresses_Type(TruthValue):
    """Custom type excessiveNewIpAddresses based on TruthValue"""
    defaultValue = 2


_ExcessiveNewIpAddresses_Type.__name__ = "TruthValue"
_ExcessiveNewIpAddresses_Object = MibScalar
excessiveNewIpAddresses = _ExcessiveNewIpAddresses_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 1, 1, 3),
    _ExcessiveNewIpAddresses_Type()
)
excessiveNewIpAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excessiveNewIpAddresses.setStatus("current")


class _ExcessiveAddressTableUsage_Type(TruthValue):
    """Custom type excessiveAddressTableUsage based on TruthValue"""
    defaultValue = 2


_ExcessiveAddressTableUsage_Type.__name__ = "TruthValue"
_ExcessiveAddressTableUsage_Object = MibScalar
excessiveAddressTableUsage = _ExcessiveAddressTableUsage_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 1, 1, 4),
    _ExcessiveAddressTableUsage_Type()
)
excessiveAddressTableUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excessiveAddressTableUsage.setStatus("current")


class _ExcessiveTcpSetupRate_Type(TruthValue):
    """Custom type excessiveTcpSetupRate based on TruthValue"""
    defaultValue = 2


_ExcessiveTcpSetupRate_Type.__name__ = "TruthValue"
_ExcessiveTcpSetupRate_Object = MibScalar
excessiveTcpSetupRate = _ExcessiveTcpSetupRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 1, 1, 5),
    _ExcessiveTcpSetupRate_Type()
)
excessiveTcpSetupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excessiveTcpSetupRate.setStatus("current")


class _ExcessiveNonTcpSetupRate_Type(TruthValue):
    """Custom type excessiveNonTcpSetupRate based on TruthValue"""
    defaultValue = 2


_ExcessiveNonTcpSetupRate_Type.__name__ = "TruthValue"
_ExcessiveNonTcpSetupRate_Object = MibScalar
excessiveNonTcpSetupRate = _ExcessiveNonTcpSetupRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 1, 1, 6),
    _ExcessiveNonTcpSetupRate_Type()
)
excessiveNonTcpSetupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excessiveNonTcpSetupRate.setStatus("current")


class _ExcessiveFailedProxyRate_Type(TruthValue):
    """Custom type excessiveFailedProxyRate based on TruthValue"""
    defaultValue = 2


_ExcessiveFailedProxyRate_Type.__name__ = "TruthValue"
_ExcessiveFailedProxyRate_Object = MibScalar
excessiveFailedProxyRate = _ExcessiveFailedProxyRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 1, 1, 7),
    _ExcessiveFailedProxyRate_Type()
)
excessiveFailedProxyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excessiveFailedProxyRate.setStatus("obsolete")
_DefenseStatistics_ObjectIdentity = ObjectIdentity
defenseStatistics = _DefenseStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2)
)
_DefenseBlockRateStatistics_ObjectIdentity = ObjectIdentity
defenseBlockRateStatistics = _DefenseBlockRateStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 1)
)
_AllRulesBlockRate_Type = Gauge32
_AllRulesBlockRate_Object = MibScalar
allRulesBlockRate = _AllRulesBlockRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 1, 1),
    _AllRulesBlockRate_Type()
)
allRulesBlockRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allRulesBlockRate.setStatus("current")
_SystemIssueBlockRate_Type = Gauge32
_SystemIssueBlockRate_Object = MibScalar
systemIssueBlockRate = _SystemIssueBlockRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 1, 2),
    _SystemIssueBlockRate_Type()
)
systemIssueBlockRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemIssueBlockRate.setStatus("obsolete")
_NetworkAccessRestrictionBlockRate_Type = Gauge32
_NetworkAccessRestrictionBlockRate_Object = MibScalar
networkAccessRestrictionBlockRate = _NetworkAccessRestrictionBlockRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 1, 3),
    _NetworkAccessRestrictionBlockRate_Type()
)
networkAccessRestrictionBlockRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAccessRestrictionBlockRate.setStatus("obsolete")
_NetworkRateLimitBlockRate_Type = Gauge32
_NetworkRateLimitBlockRate_Object = MibScalar
networkRateLimitBlockRate = _NetworkRateLimitBlockRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 1, 4),
    _NetworkRateLimitBlockRate_Type()
)
networkRateLimitBlockRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRateLimitBlockRate.setStatus("obsolete")
_NetworkProtocolValidationBlockRate_Type = Gauge32
_NetworkProtocolValidationBlockRate_Object = MibScalar
networkProtocolValidationBlockRate = _NetworkProtocolValidationBlockRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 1, 5),
    _NetworkProtocolValidationBlockRate_Type()
)
networkProtocolValidationBlockRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkProtocolValidationBlockRate.setStatus("obsolete")
_NetworkIntegrityAnalysisBlockRate_Type = Gauge32
_NetworkIntegrityAnalysisBlockRate_Object = MibScalar
networkIntegrityAnalysisBlockRate = _NetworkIntegrityAnalysisBlockRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 1, 6),
    _NetworkIntegrityAnalysisBlockRate_Type()
)
networkIntegrityAnalysisBlockRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkIntegrityAnalysisBlockRate.setStatus("obsolete")
_ApplicationAccessRestrictionBlockRate_Type = Gauge32
_ApplicationAccessRestrictionBlockRate_Object = MibScalar
applicationAccessRestrictionBlockRate = _ApplicationAccessRestrictionBlockRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 1, 7),
    _ApplicationAccessRestrictionBlockRate_Type()
)
applicationAccessRestrictionBlockRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationAccessRestrictionBlockRate.setStatus("obsolete")
_ApplicationRateLimitBlockRate_Type = Gauge32
_ApplicationRateLimitBlockRate_Object = MibScalar
applicationRateLimitBlockRate = _ApplicationRateLimitBlockRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 1, 8),
    _ApplicationRateLimitBlockRate_Type()
)
applicationRateLimitBlockRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationRateLimitBlockRate.setStatus("obsolete")
_ApplicationProtocolValidationBlockRate_Type = Gauge32
_ApplicationProtocolValidationBlockRate_Object = MibScalar
applicationProtocolValidationBlockRate = _ApplicationProtocolValidationBlockRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 1, 9),
    _ApplicationProtocolValidationBlockRate_Type()
)
applicationProtocolValidationBlockRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationProtocolValidationBlockRate.setStatus("obsolete")
_ApplicationIntegrityAnalysisBlockRate_Type = Gauge32
_ApplicationIntegrityAnalysisBlockRate_Object = MibScalar
applicationIntegrityAnalysisBlockRate = _ApplicationIntegrityAnalysisBlockRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 1, 10),
    _ApplicationIntegrityAnalysisBlockRate_Type()
)
applicationIntegrityAnalysisBlockRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applicationIntegrityAnalysisBlockRate.setStatus("obsolete")
_DefenseSetupRateStatistics_ObjectIdentity = ObjectIdentity
defenseSetupRateStatistics = _DefenseSetupRateStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 2)
)
_TcpSetupRate_Type = Gauge32
_TcpSetupRate_Object = MibScalar
tcpSetupRate = _TcpSetupRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 2, 1),
    _TcpSetupRate_Type()
)
tcpSetupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpSetupRate.setStatus("current")
_NonTcpSetupRate_Type = Gauge32
_NonTcpSetupRate_Object = MibScalar
nonTcpSetupRate = _NonTcpSetupRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 2, 2),
    _NonTcpSetupRate_Type()
)
nonTcpSetupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nonTcpSetupRate.setStatus("current")
_UdpSetupRate_Type = Gauge32
_UdpSetupRate_Object = MibScalar
udpSetupRate = _UdpSetupRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 2, 3),
    _UdpSetupRate_Type()
)
udpSetupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSetupRate.setStatus("current")
_IcmpSetupRate_Type = Gauge32
_IcmpSetupRate_Object = MibScalar
icmpSetupRate = _IcmpSetupRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 2, 4),
    _IcmpSetupRate_Type()
)
icmpSetupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpSetupRate.setStatus("current")
_OtherIpSetupRate_Type = Gauge32
_OtherIpSetupRate_Object = MibScalar
otherIpSetupRate = _OtherIpSetupRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 2, 5),
    _OtherIpSetupRate_Type()
)
otherIpSetupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherIpSetupRate.setStatus("current")
_DefenseUsageStatistics_ObjectIdentity = ObjectIdentity
defenseUsageStatistics = _DefenseUsageStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 3)
)
_InUseFlows_Type = Gauge32
_InUseFlows_Object = MibScalar
inUseFlows = _InUseFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 3, 1),
    _InUseFlows_Type()
)
inUseFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inUseFlows.setStatus("current")
_InUseTcpFlows_Type = Gauge32
_InUseTcpFlows_Object = MibScalar
inUseTcpFlows = _InUseTcpFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 3, 2),
    _InUseTcpFlows_Type()
)
inUseTcpFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inUseTcpFlows.setStatus("current")
_InUseUdpFlows_Type = Gauge32
_InUseUdpFlows_Object = MibScalar
inUseUdpFlows = _InUseUdpFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 3, 3),
    _InUseUdpFlows_Type()
)
inUseUdpFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inUseUdpFlows.setStatus("current")
_InUseIcmpFlows_Type = Gauge32
_InUseIcmpFlows_Object = MibScalar
inUseIcmpFlows = _InUseIcmpFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 3, 4),
    _InUseIcmpFlows_Type()
)
inUseIcmpFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inUseIcmpFlows.setStatus("current")
_InUseOtherFlows_Type = Gauge32
_InUseOtherFlows_Object = MibScalar
inUseOtherFlows = _InUseOtherFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 3, 5),
    _InUseOtherFlows_Type()
)
inUseOtherFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inUseOtherFlows.setStatus("current")
_TotalProxySetups_Type = Counter64
_TotalProxySetups_Object = MibScalar
totalProxySetups = _TotalProxySetups_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 3, 6),
    _TotalProxySetups_Type()
)
totalProxySetups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalProxySetups.setStatus("obsolete")
_TotalProxyFailedSetups_Type = Counter64
_TotalProxyFailedSetups_Object = MibScalar
totalProxyFailedSetups = _TotalProxyFailedSetups_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 3, 7),
    _TotalProxyFailedSetups_Type()
)
totalProxyFailedSetups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalProxyFailedSetups.setStatus("obsolete")
_DefenseInterfaceStatistics_ObjectIdentity = ObjectIdentity
defenseInterfaceStatistics = _DefenseInterfaceStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4)
)
_ExternalPortPacketReceiveRate_Type = Gauge32
_ExternalPortPacketReceiveRate_Object = MibScalar
externalPortPacketReceiveRate = _ExternalPortPacketReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 1),
    _ExternalPortPacketReceiveRate_Type()
)
externalPortPacketReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortPacketReceiveRate.setStatus("current")
_ExternalPortBitReceiveRate_Type = Gauge32
_ExternalPortBitReceiveRate_Object = MibScalar
externalPortBitReceiveRate = _ExternalPortBitReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 2),
    _ExternalPortBitReceiveRate_Type()
)
externalPortBitReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortBitReceiveRate.setStatus("current")
_ExternalPortPacketTransmitRate_Type = Gauge32
_ExternalPortPacketTransmitRate_Object = MibScalar
externalPortPacketTransmitRate = _ExternalPortPacketTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 3),
    _ExternalPortPacketTransmitRate_Type()
)
externalPortPacketTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortPacketTransmitRate.setStatus("current")
_ExternalPortBitTransmitRate_Type = Gauge32
_ExternalPortBitTransmitRate_Object = MibScalar
externalPortBitTransmitRate = _ExternalPortBitTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 4),
    _ExternalPortBitTransmitRate_Type()
)
externalPortBitTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortBitTransmitRate.setStatus("current")
_InternalPortPacketReceiveRate_Type = Gauge32
_InternalPortPacketReceiveRate_Object = MibScalar
internalPortPacketReceiveRate = _InternalPortPacketReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 5),
    _InternalPortPacketReceiveRate_Type()
)
internalPortPacketReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalPortPacketReceiveRate.setStatus("current")
_InternalPortBitReceiveRate_Type = Gauge32
_InternalPortBitReceiveRate_Object = MibScalar
internalPortBitReceiveRate = _InternalPortBitReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 6),
    _InternalPortBitReceiveRate_Type()
)
internalPortBitReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalPortBitReceiveRate.setStatus("current")
_InternalPortPacketTransmitRate_Type = Gauge32
_InternalPortPacketTransmitRate_Object = MibScalar
internalPortPacketTransmitRate = _InternalPortPacketTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 7),
    _InternalPortPacketTransmitRate_Type()
)
internalPortPacketTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalPortPacketTransmitRate.setStatus("current")
_InternalPortBitTransmitRate_Type = Gauge32
_InternalPortBitTransmitRate_Object = MibScalar
internalPortBitTransmitRate = _InternalPortBitTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 8),
    _InternalPortBitTransmitRate_Type()
)
internalPortBitTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalPortBitTransmitRate.setStatus("current")
_ExternalPortReceivedPackets_Type = Counter64
_ExternalPortReceivedPackets_Object = MibScalar
externalPortReceivedPackets = _ExternalPortReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 9),
    _ExternalPortReceivedPackets_Type()
)
externalPortReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortReceivedPackets.setStatus("current")
_ExternalPortTransmittedPackets_Type = Counter64
_ExternalPortTransmittedPackets_Object = MibScalar
externalPortTransmittedPackets = _ExternalPortTransmittedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 10),
    _ExternalPortTransmittedPackets_Type()
)
externalPortTransmittedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortTransmittedPackets.setStatus("current")
_ExternalPortReceivedBytes_Type = Counter64
_ExternalPortReceivedBytes_Object = MibScalar
externalPortReceivedBytes = _ExternalPortReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 11),
    _ExternalPortReceivedBytes_Type()
)
externalPortReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortReceivedBytes.setStatus("current")
_ExternalPortTransmittedBytes_Type = Counter64
_ExternalPortTransmittedBytes_Object = MibScalar
externalPortTransmittedBytes = _ExternalPortTransmittedBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 12),
    _ExternalPortTransmittedBytes_Type()
)
externalPortTransmittedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortTransmittedBytes.setStatus("current")
_InternalPortReceivedPackets_Type = Counter64
_InternalPortReceivedPackets_Object = MibScalar
internalPortReceivedPackets = _InternalPortReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 13),
    _InternalPortReceivedPackets_Type()
)
internalPortReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalPortReceivedPackets.setStatus("current")
_InternalPortTransmittedPackets_Type = Counter64
_InternalPortTransmittedPackets_Object = MibScalar
internalPortTransmittedPackets = _InternalPortTransmittedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 14),
    _InternalPortTransmittedPackets_Type()
)
internalPortTransmittedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalPortTransmittedPackets.setStatus("current")
_InternalPortReceivedBytes_Type = Counter64
_InternalPortReceivedBytes_Object = MibScalar
internalPortReceivedBytes = _InternalPortReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 15),
    _InternalPortReceivedBytes_Type()
)
internalPortReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalPortReceivedBytes.setStatus("current")
_InternalPortTransmittedBytes_Type = Counter64
_InternalPortTransmittedBytes_Object = MibScalar
internalPortTransmittedBytes = _InternalPortTransmittedBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 16),
    _InternalPortTransmittedBytes_Type()
)
internalPortTransmittedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalPortTransmittedBytes.setStatus("current")
_ExternalPortReceivedBadCrcPackets_Type = Counter64
_ExternalPortReceivedBadCrcPackets_Object = MibScalar
externalPortReceivedBadCrcPackets = _ExternalPortReceivedBadCrcPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 17),
    _ExternalPortReceivedBadCrcPackets_Type()
)
externalPortReceivedBadCrcPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortReceivedBadCrcPackets.setStatus("current")
_InternalPortReceivedBadCrcPackets_Type = Counter64
_InternalPortReceivedBadCrcPackets_Object = MibScalar
internalPortReceivedBadCrcPackets = _InternalPortReceivedBadCrcPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 18),
    _InternalPortReceivedBadCrcPackets_Type()
)
internalPortReceivedBadCrcPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalPortReceivedBadCrcPackets.setStatus("current")
_ExternalPortReceivedOversizedPackets_Type = Counter64
_ExternalPortReceivedOversizedPackets_Object = MibScalar
externalPortReceivedOversizedPackets = _ExternalPortReceivedOversizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 19),
    _ExternalPortReceivedOversizedPackets_Type()
)
externalPortReceivedOversizedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortReceivedOversizedPackets.setStatus("current")
_InternalPortReceivedOversizedPackets_Type = Counter64
_InternalPortReceivedOversizedPackets_Object = MibScalar
internalPortReceivedOversizedPackets = _InternalPortReceivedOversizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 20),
    _InternalPortReceivedOversizedPackets_Type()
)
internalPortReceivedOversizedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalPortReceivedOversizedPackets.setStatus("current")
_ExternalPortReceivedJabberPackets_Type = Counter64
_ExternalPortReceivedJabberPackets_Object = MibScalar
externalPortReceivedJabberPackets = _ExternalPortReceivedJabberPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 21),
    _ExternalPortReceivedJabberPackets_Type()
)
externalPortReceivedJabberPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortReceivedJabberPackets.setStatus("current")
_InternalPortReceivedJabberPackets_Type = Counter64
_InternalPortReceivedJabberPackets_Object = MibScalar
internalPortReceivedJabberPackets = _InternalPortReceivedJabberPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 22),
    _InternalPortReceivedJabberPackets_Type()
)
internalPortReceivedJabberPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalPortReceivedJabberPackets.setStatus("current")
_ExternalPortTransmitErrorPackets_Type = Counter64
_ExternalPortTransmitErrorPackets_Object = MibScalar
externalPortTransmitErrorPackets = _ExternalPortTransmitErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 23),
    _ExternalPortTransmitErrorPackets_Type()
)
externalPortTransmitErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPortTransmitErrorPackets.setStatus("current")
_InternalPortTransmitErrorPackets_Type = Counter64
_InternalPortTransmitErrorPackets_Object = MibScalar
internalPortTransmitErrorPackets = _InternalPortTransmitErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 4, 24),
    _InternalPortTransmitErrorPackets_Type()
)
internalPortTransmitErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalPortTransmitErrorPackets.setStatus("current")
_DefenseIpAddressStatistics_ObjectIdentity = ObjectIdentity
defenseIpAddressStatistics = _DefenseIpAddressStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 5)
)
_InUseAddresses_Type = Gauge32
_InUseAddresses_Object = MibScalar
inUseAddresses = _InUseAddresses_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 5, 1),
    _InUseAddresses_Type()
)
inUseAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inUseAddresses.setStatus("current")
_InUseTrustedAddresses_Type = Gauge32
_InUseTrustedAddresses_Object = MibScalar
inUseTrustedAddresses = _InUseTrustedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 5, 2),
    _InUseTrustedAddresses_Type()
)
inUseTrustedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inUseTrustedAddresses.setStatus("current")
_InUseSuspiciousAddresses_Type = Gauge32
_InUseSuspiciousAddresses_Object = MibScalar
inUseSuspiciousAddresses = _InUseSuspiciousAddresses_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 5, 3),
    _InUseSuspiciousAddresses_Type()
)
inUseSuspiciousAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inUseSuspiciousAddresses.setStatus("current")
_InUseMaliciousAddresses_Type = Gauge32
_InUseMaliciousAddresses_Object = MibScalar
inUseMaliciousAddresses = _InUseMaliciousAddresses_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 5, 4),
    _InUseMaliciousAddresses_Type()
)
inUseMaliciousAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inUseMaliciousAddresses.setStatus("current")
_InUseUnclassifiedAddresses_Type = Gauge32
_InUseUnclassifiedAddresses_Object = MibScalar
inUseUnclassifiedAddresses = _InUseUnclassifiedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 2, 5, 5),
    _InUseUnclassifiedAddresses_Type()
)
inUseUnclassifiedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inUseUnclassifiedAddresses.setStatus("current")
_ProtectionGroupStatistics_ObjectIdentity = ObjectIdentity
protectionGroupStatistics = _ProtectionGroupStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3)
)
_ProtectionGroupTable_Object = MibTable
protectionGroupTable = _ProtectionGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    protectionGroupTable.setStatus("current")
_ProtectionGroupEntry_Object = MibTableRow
protectionGroupEntry = _ProtectionGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1)
)
protectionGroupEntry.setIndexNames(
    (0, "CORERO-CMS-MIB", "pgName"),
)
if mibBuilder.loadTexts:
    protectionGroupEntry.setStatus("current")
_PgName_Type = OctetString
_PgName_Object = MibTableColumn
pgName = _PgName_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 1),
    _PgName_Type()
)
pgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pgName.setStatus("current")
_PgExternalPortReceivedPackets_Type = Counter64
_PgExternalPortReceivedPackets_Object = MibTableColumn
pgExternalPortReceivedPackets = _PgExternalPortReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 2),
    _PgExternalPortReceivedPackets_Type()
)
pgExternalPortReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgExternalPortReceivedPackets.setStatus("current")
_PgExternalPortTransmittedPackets_Type = Counter64
_PgExternalPortTransmittedPackets_Object = MibTableColumn
pgExternalPortTransmittedPackets = _PgExternalPortTransmittedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 3),
    _PgExternalPortTransmittedPackets_Type()
)
pgExternalPortTransmittedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgExternalPortTransmittedPackets.setStatus("current")
_PgExternalPortReceivedBytes_Type = Counter64
_PgExternalPortReceivedBytes_Object = MibTableColumn
pgExternalPortReceivedBytes = _PgExternalPortReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 4),
    _PgExternalPortReceivedBytes_Type()
)
pgExternalPortReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgExternalPortReceivedBytes.setStatus("current")
_PgExternalPortTransmittedBytes_Type = Counter64
_PgExternalPortTransmittedBytes_Object = MibTableColumn
pgExternalPortTransmittedBytes = _PgExternalPortTransmittedBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 5),
    _PgExternalPortTransmittedBytes_Type()
)
pgExternalPortTransmittedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgExternalPortTransmittedBytes.setStatus("current")
_PgInternalPortReceivedPackets_Type = Counter64
_PgInternalPortReceivedPackets_Object = MibTableColumn
pgInternalPortReceivedPackets = _PgInternalPortReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 6),
    _PgInternalPortReceivedPackets_Type()
)
pgInternalPortReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgInternalPortReceivedPackets.setStatus("current")
_PgInternalPortTransmittedPackets_Type = Counter64
_PgInternalPortTransmittedPackets_Object = MibTableColumn
pgInternalPortTransmittedPackets = _PgInternalPortTransmittedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 7),
    _PgInternalPortTransmittedPackets_Type()
)
pgInternalPortTransmittedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgInternalPortTransmittedPackets.setStatus("current")
_PgInternalPortReceivedBytes_Type = Counter64
_PgInternalPortReceivedBytes_Object = MibTableColumn
pgInternalPortReceivedBytes = _PgInternalPortReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 8),
    _PgInternalPortReceivedBytes_Type()
)
pgInternalPortReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgInternalPortReceivedBytes.setStatus("current")
_PgInternalPortTransmittedBytes_Type = Counter64
_PgInternalPortTransmittedBytes_Object = MibTableColumn
pgInternalPortTransmittedBytes = _PgInternalPortTransmittedBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 9),
    _PgInternalPortTransmittedBytes_Type()
)
pgInternalPortTransmittedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgInternalPortTransmittedBytes.setStatus("current")
_PgExternalPortReceivedBadCrcPackets_Type = Counter64
_PgExternalPortReceivedBadCrcPackets_Object = MibTableColumn
pgExternalPortReceivedBadCrcPackets = _PgExternalPortReceivedBadCrcPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 10),
    _PgExternalPortReceivedBadCrcPackets_Type()
)
pgExternalPortReceivedBadCrcPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgExternalPortReceivedBadCrcPackets.setStatus("current")
_PgInternalPortReceivedBadCrcPackets_Type = Counter64
_PgInternalPortReceivedBadCrcPackets_Object = MibTableColumn
pgInternalPortReceivedBadCrcPackets = _PgInternalPortReceivedBadCrcPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 11),
    _PgInternalPortReceivedBadCrcPackets_Type()
)
pgInternalPortReceivedBadCrcPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgInternalPortReceivedBadCrcPackets.setStatus("current")
_PgExternalPortReceivedOversizedPackets_Type = Counter64
_PgExternalPortReceivedOversizedPackets_Object = MibTableColumn
pgExternalPortReceivedOversizedPackets = _PgExternalPortReceivedOversizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 12),
    _PgExternalPortReceivedOversizedPackets_Type()
)
pgExternalPortReceivedOversizedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgExternalPortReceivedOversizedPackets.setStatus("current")
_PgInternalPortReceivedOversizedPackets_Type = Counter64
_PgInternalPortReceivedOversizedPackets_Object = MibTableColumn
pgInternalPortReceivedOversizedPackets = _PgInternalPortReceivedOversizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 13),
    _PgInternalPortReceivedOversizedPackets_Type()
)
pgInternalPortReceivedOversizedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgInternalPortReceivedOversizedPackets.setStatus("current")
_PgExternalPortReceivedJabberPackets_Type = Counter64
_PgExternalPortReceivedJabberPackets_Object = MibTableColumn
pgExternalPortReceivedJabberPackets = _PgExternalPortReceivedJabberPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 14),
    _PgExternalPortReceivedJabberPackets_Type()
)
pgExternalPortReceivedJabberPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgExternalPortReceivedJabberPackets.setStatus("current")
_PgInternalPortReceivedJabberPackets_Type = Counter64
_PgInternalPortReceivedJabberPackets_Object = MibTableColumn
pgInternalPortReceivedJabberPackets = _PgInternalPortReceivedJabberPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 15),
    _PgInternalPortReceivedJabberPackets_Type()
)
pgInternalPortReceivedJabberPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgInternalPortReceivedJabberPackets.setStatus("current")
_PgExternalPortTransmitErrorPackets_Type = Counter64
_PgExternalPortTransmitErrorPackets_Object = MibTableColumn
pgExternalPortTransmitErrorPackets = _PgExternalPortTransmitErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 16),
    _PgExternalPortTransmitErrorPackets_Type()
)
pgExternalPortTransmitErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgExternalPortTransmitErrorPackets.setStatus("current")
_PgInternalPortTransmitErrorPackets_Type = Counter64
_PgInternalPortTransmitErrorPackets_Object = MibTableColumn
pgInternalPortTransmitErrorPackets = _PgInternalPortTransmitErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 1, 3, 1, 1, 17),
    _PgInternalPortTransmitErrorPackets_Type()
)
pgInternalPortTransmitErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgInternalPortTransmitErrorPackets.setStatus("current")
_CoreroCMSMIBConformance_ObjectIdentity = ObjectIdentity
coreroCMSMIBConformance = _CoreroCMSMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 2)
)
_CoreroCMSMIBCompliances_ObjectIdentity = ObjectIdentity
coreroCMSMIBCompliances = _CoreroCMSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 2, 1)
)
_CoreroCMSMIBGroups_ObjectIdentity = ObjectIdentity
coreroCMSMIBGroups = _CoreroCMSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 2, 2)
)

# Managed Objects groups

defenseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41036, 4, 2, 2, 1)
)
defenseGroup.setObjects(
      *(("CORERO-CMS-MIB", "defenseStatus"),
        ("CORERO-CMS-MIB", "defenseStatistics"),
        ("CORERO-CMS-MIB", "protectionGroupStatistics"))
)
if mibBuilder.loadTexts:
    defenseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

coreroCMSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 41036, 4, 2, 1, 2)
)
coreroCMSMIBCompliance.setObjects(
    ("CORERO-CMS-MIB", "defenseGroup")
)
if mibBuilder.loadTexts:
    coreroCMSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CORERO-CMS-MIB",
    **{"UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
       "String": String,
       "TYPE-CMS-MODULE-STATE": TYPE_CMS_MODULE_STATE,
       "corero": corero,
       "coreroCMSMIB": coreroCMSMIB,
       "coreroCMSMIBObjects": coreroCMSMIBObjects,
       "defense": defense,
       "defenseStatus": defenseStatus,
       "defenseStatusThreatAwareness": defenseStatusThreatAwareness,
       "excessivePacketsFromBadClients": excessivePacketsFromBadClients,
       "excessiveProxySetupRate": excessiveProxySetupRate,
       "excessiveNewIpAddresses": excessiveNewIpAddresses,
       "excessiveAddressTableUsage": excessiveAddressTableUsage,
       "excessiveTcpSetupRate": excessiveTcpSetupRate,
       "excessiveNonTcpSetupRate": excessiveNonTcpSetupRate,
       "excessiveFailedProxyRate": excessiveFailedProxyRate,
       "defenseStatistics": defenseStatistics,
       "defenseBlockRateStatistics": defenseBlockRateStatistics,
       "allRulesBlockRate": allRulesBlockRate,
       "systemIssueBlockRate": systemIssueBlockRate,
       "networkAccessRestrictionBlockRate": networkAccessRestrictionBlockRate,
       "networkRateLimitBlockRate": networkRateLimitBlockRate,
       "networkProtocolValidationBlockRate": networkProtocolValidationBlockRate,
       "networkIntegrityAnalysisBlockRate": networkIntegrityAnalysisBlockRate,
       "applicationAccessRestrictionBlockRate": applicationAccessRestrictionBlockRate,
       "applicationRateLimitBlockRate": applicationRateLimitBlockRate,
       "applicationProtocolValidationBlockRate": applicationProtocolValidationBlockRate,
       "applicationIntegrityAnalysisBlockRate": applicationIntegrityAnalysisBlockRate,
       "defenseSetupRateStatistics": defenseSetupRateStatistics,
       "tcpSetupRate": tcpSetupRate,
       "nonTcpSetupRate": nonTcpSetupRate,
       "udpSetupRate": udpSetupRate,
       "icmpSetupRate": icmpSetupRate,
       "otherIpSetupRate": otherIpSetupRate,
       "defenseUsageStatistics": defenseUsageStatistics,
       "inUseFlows": inUseFlows,
       "inUseTcpFlows": inUseTcpFlows,
       "inUseUdpFlows": inUseUdpFlows,
       "inUseIcmpFlows": inUseIcmpFlows,
       "inUseOtherFlows": inUseOtherFlows,
       "totalProxySetups": totalProxySetups,
       "totalProxyFailedSetups": totalProxyFailedSetups,
       "defenseInterfaceStatistics": defenseInterfaceStatistics,
       "externalPortPacketReceiveRate": externalPortPacketReceiveRate,
       "externalPortBitReceiveRate": externalPortBitReceiveRate,
       "externalPortPacketTransmitRate": externalPortPacketTransmitRate,
       "externalPortBitTransmitRate": externalPortBitTransmitRate,
       "internalPortPacketReceiveRate": internalPortPacketReceiveRate,
       "internalPortBitReceiveRate": internalPortBitReceiveRate,
       "internalPortPacketTransmitRate": internalPortPacketTransmitRate,
       "internalPortBitTransmitRate": internalPortBitTransmitRate,
       "externalPortReceivedPackets": externalPortReceivedPackets,
       "externalPortTransmittedPackets": externalPortTransmittedPackets,
       "externalPortReceivedBytes": externalPortReceivedBytes,
       "externalPortTransmittedBytes": externalPortTransmittedBytes,
       "internalPortReceivedPackets": internalPortReceivedPackets,
       "internalPortTransmittedPackets": internalPortTransmittedPackets,
       "internalPortReceivedBytes": internalPortReceivedBytes,
       "internalPortTransmittedBytes": internalPortTransmittedBytes,
       "externalPortReceivedBadCrcPackets": externalPortReceivedBadCrcPackets,
       "internalPortReceivedBadCrcPackets": internalPortReceivedBadCrcPackets,
       "externalPortReceivedOversizedPackets": externalPortReceivedOversizedPackets,
       "internalPortReceivedOversizedPackets": internalPortReceivedOversizedPackets,
       "externalPortReceivedJabberPackets": externalPortReceivedJabberPackets,
       "internalPortReceivedJabberPackets": internalPortReceivedJabberPackets,
       "externalPortTransmitErrorPackets": externalPortTransmitErrorPackets,
       "internalPortTransmitErrorPackets": internalPortTransmitErrorPackets,
       "defenseIpAddressStatistics": defenseIpAddressStatistics,
       "inUseAddresses": inUseAddresses,
       "inUseTrustedAddresses": inUseTrustedAddresses,
       "inUseSuspiciousAddresses": inUseSuspiciousAddresses,
       "inUseMaliciousAddresses": inUseMaliciousAddresses,
       "inUseUnclassifiedAddresses": inUseUnclassifiedAddresses,
       "protectionGroupStatistics": protectionGroupStatistics,
       "protectionGroupTable": protectionGroupTable,
       "protectionGroupEntry": protectionGroupEntry,
       "pgName": pgName,
       "pgExternalPortReceivedPackets": pgExternalPortReceivedPackets,
       "pgExternalPortTransmittedPackets": pgExternalPortTransmittedPackets,
       "pgExternalPortReceivedBytes": pgExternalPortReceivedBytes,
       "pgExternalPortTransmittedBytes": pgExternalPortTransmittedBytes,
       "pgInternalPortReceivedPackets": pgInternalPortReceivedPackets,
       "pgInternalPortTransmittedPackets": pgInternalPortTransmittedPackets,
       "pgInternalPortReceivedBytes": pgInternalPortReceivedBytes,
       "pgInternalPortTransmittedBytes": pgInternalPortTransmittedBytes,
       "pgExternalPortReceivedBadCrcPackets": pgExternalPortReceivedBadCrcPackets,
       "pgInternalPortReceivedBadCrcPackets": pgInternalPortReceivedBadCrcPackets,
       "pgExternalPortReceivedOversizedPackets": pgExternalPortReceivedOversizedPackets,
       "pgInternalPortReceivedOversizedPackets": pgInternalPortReceivedOversizedPackets,
       "pgExternalPortReceivedJabberPackets": pgExternalPortReceivedJabberPackets,
       "pgInternalPortReceivedJabberPackets": pgInternalPortReceivedJabberPackets,
       "pgExternalPortTransmitErrorPackets": pgExternalPortTransmitErrorPackets,
       "pgInternalPortTransmitErrorPackets": pgInternalPortTransmitErrorPackets,
       "coreroCMSMIBConformance": coreroCMSMIBConformance,
       "coreroCMSMIBCompliances": coreroCMSMIBCompliances,
       "coreroCMSMIBCompliance": coreroCMSMIBCompliance,
       "coreroCMSMIBGroups": coreroCMSMIBGroups,
       "defenseGroup": defenseGroup}
)
