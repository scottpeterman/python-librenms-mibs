# SNMP MIB module (CAMBIUM-PTP670-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cambium\CAMBIUM-PTP670-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:30 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cambium = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713)
)
if mibBuilder.loadTexts:
    cambium.setRevisions(
        ("2018-09-04 23:49",
         "2018-05-25 18:14",
         "2017-11-24 09:19",
         "2017-09-06 16:59",
         "2017-06-15 18:31",
         "2017-02-24 11:59")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ptp_ObjectIdentity = ObjectIdentity
ptp = _Ptp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 1)
)
_Ptmp_ObjectIdentity = ObjectIdentity
ptmp = _Ptmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 2)
)
_Ptp670_ObjectIdentity = ObjectIdentity
ptp670 = _Ptp670_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11)
)
_Dfs_ObjectIdentity = ObjectIdentity
dfs = _Dfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 3)
)


class _DfsTableNumber_Type(Integer32):
    """Custom type dfsTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 305),
    )


_DfsTableNumber_Type.__name__ = "Integer32"
_DfsTableNumber_Object = MibScalar
dfsTableNumber = _DfsTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 3, 1),
    _DfsTableNumber_Type()
)
dfsTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsTableNumber.setStatus("current")
_DfsTable_Object = MibTable
dfsTable = _DfsTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 3, 2)
)
if mibBuilder.loadTexts:
    dfsTable.setStatus("current")
_DfsTableEntry_Object = MibTableRow
dfsTableEntry = _DfsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 3, 2, 1)
)
dfsTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "dfsTableIndex"),
)
if mibBuilder.loadTexts:
    dfsTableEntry.setStatus("current")


class _DfsTableIndex_Type(Integer32):
    """Custom type dfsTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 305),
    )


_DfsTableIndex_Type.__name__ = "Integer32"
_DfsTableIndex_Object = MibTableColumn
dfsTableIndex = _DfsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 3, 2, 1, 1),
    _DfsTableIndex_Type()
)
dfsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfsTableIndex.setStatus("current")
_DfsMeans_Type = Integer32
_DfsMeans_Object = MibTableColumn
dfsMeans = _DfsMeans_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 3, 2, 1, 2),
    _DfsMeans_Type()
)
dfsMeans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsMeans.setStatus("current")
_DfsNineNinePointNinePercentiles_Type = Integer32
_DfsNineNinePointNinePercentiles_Object = MibTableColumn
dfsNineNinePointNinePercentiles = _DfsNineNinePointNinePercentiles_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 3, 2, 1, 3),
    _DfsNineNinePointNinePercentiles_Type()
)
dfsNineNinePointNinePercentiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsNineNinePointNinePercentiles.setStatus("current")
_DfsPeaks_Type = Integer32
_DfsPeaks_Object = MibTableColumn
dfsPeaks = _DfsPeaks_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 3, 2, 1, 4),
    _DfsPeaks_Type()
)
dfsPeaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsPeaks.setStatus("current")


class _ExtendedSpectrumScanning_Type(Integer32):
    """Custom type extendedSpectrumScanning based on Integer32"""
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


_ExtendedSpectrumScanning_Type.__name__ = "Integer32"
_ExtendedSpectrumScanning_Object = MibScalar
extendedSpectrumScanning = _ExtendedSpectrumScanning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 3, 3),
    _ExtendedSpectrumScanning_Type()
)
extendedSpectrumScanning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendedSpectrumScanning.setStatus("current")
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 4)
)


class _LocalPacketFiltering_Type(Integer32):
    """Custom type localPacketFiltering based on Integer32"""
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


_LocalPacketFiltering_Type.__name__ = "Integer32"
_LocalPacketFiltering_Object = MibScalar
localPacketFiltering = _LocalPacketFiltering_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 4, 1),
    _LocalPacketFiltering_Type()
)
localPacketFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localPacketFiltering.setStatus("current")
_PacketsToInternalStack_Type = Counter64
_PacketsToInternalStack_Object = MibScalar
packetsToInternalStack = _PacketsToInternalStack_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 4, 2),
    _PacketsToInternalStack_Type()
)
packetsToInternalStack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetsToInternalStack.setStatus("current")
_PacketsFromInternalStack_Type = Counter64
_PacketsFromInternalStack_Object = MibScalar
packetsFromInternalStack = _PacketsFromInternalStack_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 4, 3),
    _PacketsFromInternalStack_Type()
)
packetsFromInternalStack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetsFromInternalStack.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5)
)
_IPv4Address_Type = IpAddress
_IPv4Address_Object = MibScalar
iPv4Address = _IPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 1),
    _IPv4Address_Type()
)
iPv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPv4Address.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 2),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_GatewayIPAddress_Type = IpAddress
_GatewayIPAddress_Object = MibScalar
gatewayIPAddress = _GatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 3),
    _GatewayIPAddress_Type()
)
gatewayIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayIPAddress.setStatus("current")


class _TargetMACAddress_Type(OctetString):
    """Custom type targetMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_TargetMACAddress_Type.__name__ = "OctetString"
_TargetMACAddress_Object = MibScalar
targetMACAddress = _TargetMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 4),
    _TargetMACAddress_Type()
)
targetMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetMACAddress.setStatus("current")


class _MasterSlaveMode_Type(Integer32):
    """Custom type masterSlaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )


_MasterSlaveMode_Type.__name__ = "Integer32"
_MasterSlaveMode_Object = MibScalar
masterSlaveMode = _MasterSlaveMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 5),
    _MasterSlaveMode_Type()
)
masterSlaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterSlaveMode.setStatus("current")


class _MaximumTransmitPower_Type(Integer32):
    """Custom type maximumTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 30),
    )


_MaximumTransmitPower_Type.__name__ = "Integer32"
_MaximumTransmitPower_Object = MibScalar
maximumTransmitPower = _MaximumTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 6),
    _MaximumTransmitPower_Type()
)
maximumTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumTransmitPower.setStatus("current")


class _AntennaGain_Type(Integer32):
    """Custom type antennaGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 610),
    )


_AntennaGain_Type.__name__ = "Integer32"
_AntennaGain_Object = MibScalar
antennaGain = _AntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 7),
    _AntennaGain_Type()
)
antennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antennaGain.setStatus("current")


class _CableLoss_Type(Integer32):
    """Custom type cableLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CableLoss_Type.__name__ = "Integer32"
_CableLoss_Object = MibScalar
cableLoss = _CableLoss_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 8),
    _CableLoss_Type()
)
cableLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableLoss.setStatus("current")
_EIRP_Type = Integer32
_EIRP_Object = MibScalar
eIRP = _EIRP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 9),
    _EIRP_Type()
)
eIRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eIRP.setStatus("current")


class _ChannelBandwidth_Type(Integer32):
    """Custom type channelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bw30MHz", 0),
          ("bw15MHz", 1),
          ("bw10MHz", 2),
          ("bw5MHz", 3),
          ("bw20MHz", 4),
          ("bw56MHz", 5),
          ("bw50MHz", 6),
          ("bw40MHz", 7),
          ("bw45MHz", 8))
    )


_ChannelBandwidth_Type.__name__ = "Integer32"
_ChannelBandwidth_Object = MibScalar
channelBandwidth = _ChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 11),
    _ChannelBandwidth_Type()
)
channelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelBandwidth.setStatus("current")


class _LinkName_Type(DisplayString):
    """Custom type linkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LinkName_Type.__name__ = "DisplayString"
_LinkName_Object = MibScalar
linkName = _LinkName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 14),
    _LinkName_Type()
)
linkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkName.setStatus("current")


class _SiteName_Type(DisplayString):
    """Custom type siteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SiteName_Type.__name__ = "DisplayString"
_SiteName_Object = MibScalar
siteName = _SiteName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 15),
    _SiteName_Type()
)
siteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteName.setStatus("current")


class _AccessMethod_Type(Integer32):
    """Custom type accessMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkAccess", 0),
          ("linkNameAccess", 1),
          ("groupAccess", 2))
    )


_AccessMethod_Type.__name__ = "Integer32"
_AccessMethod_Object = MibScalar
accessMethod = _AccessMethod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 16),
    _AccessMethod_Type()
)
accessMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessMethod.setStatus("current")


class _GroupID_Type(Integer32):
    """Custom type groupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GroupID_Type.__name__ = "Integer32"
_GroupID_Object = MibScalar
groupID = _GroupID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 17),
    _GroupID_Type()
)
groupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupID.setStatus("current")


class _IPv6Address_Type(DisplayString):
    """Custom type iPv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_IPv6Address_Type.__name__ = "DisplayString"
_IPv6Address_Object = MibScalar
iPv6Address = _IPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 18),
    _IPv6Address_Type()
)
iPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPv6Address.setStatus("current")


class _IPVersion_Type(Integer32):
    """Custom type iPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iPv4", 0),
          ("iPv6", 1),
          ("dualIPv4andIPv6", 2))
    )


_IPVersion_Type.__name__ = "Integer32"
_IPVersion_Object = MibScalar
iPVersion = _IPVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 20),
    _IPVersion_Type()
)
iPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPVersion.setStatus("current")


class _IPv6AutoConfiguredLinkLocalAddress_Type(DisplayString):
    """Custom type iPv6AutoConfiguredLinkLocalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_IPv6AutoConfiguredLinkLocalAddress_Type.__name__ = "DisplayString"
_IPv6AutoConfiguredLinkLocalAddress_Object = MibScalar
iPv6AutoConfiguredLinkLocalAddress = _IPv6AutoConfiguredLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 21),
    _IPv6AutoConfiguredLinkLocalAddress_Type()
)
iPv6AutoConfiguredLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPv6AutoConfiguredLinkLocalAddress.setStatus("current")


class _IPv6PrefixLength_Type(Integer32):
    """Custom type iPv6PrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IPv6PrefixLength_Type.__name__ = "Integer32"
_IPv6PrefixLength_Object = MibScalar
iPv6PrefixLength = _IPv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 22),
    _IPv6PrefixLength_Type()
)
iPv6PrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPv6PrefixLength.setStatus("current")


class _IPv6GatewayAddress_Type(DisplayString):
    """Custom type iPv6GatewayAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_IPv6GatewayAddress_Type.__name__ = "DisplayString"
_IPv6GatewayAddress_Object = MibScalar
iPv6GatewayAddress = _IPv6GatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 23),
    _IPv6GatewayAddress_Type()
)
iPv6GatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPv6GatewayAddress.setStatus("current")


class _RemoteInternetAddressTypeLinked_Type(Integer32):
    """Custom type remoteInternetAddressTypeLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipv4z", 3),
          ("ipv6z", 4),
          ("unknown6", 5),
          ("unknown7", 6),
          ("unknown8", 7),
          ("unknown9", 8),
          ("unknown10", 9),
          ("unknown11", 10),
          ("unknown12", 11),
          ("unknown13", 12),
          ("unknown14", 13),
          ("unknown15", 14),
          ("unknown16", 15),
          ("dns", 16))
    )


_RemoteInternetAddressTypeLinked_Type.__name__ = "Integer32"
_RemoteInternetAddressTypeLinked_Object = MibScalar
remoteInternetAddressTypeLinked = _RemoteInternetAddressTypeLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 24),
    _RemoteInternetAddressTypeLinked_Type()
)
remoteInternetAddressTypeLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteInternetAddressTypeLinked.setStatus("current")
_RemoteInternetAddressLinked_Type = InetAddress
_RemoteInternetAddressLinked_Object = MibScalar
remoteInternetAddressLinked = _RemoteInternetAddressLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 25),
    _RemoteInternetAddressLinked_Type()
)
remoteInternetAddressLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteInternetAddressLinked.setStatus("current")
_SubbandLowestFrequency_Type = Integer32
_SubbandLowestFrequency_Object = MibScalar
subbandLowestFrequency = _SubbandLowestFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 26),
    _SubbandLowestFrequency_Type()
)
subbandLowestFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subbandLowestFrequency.setStatus("current")
_SubbandHighestFrequency_Type = Integer32
_SubbandHighestFrequency_Object = MibScalar
subbandHighestFrequency = _SubbandHighestFrequency_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 27),
    _SubbandHighestFrequency_Type()
)
subbandHighestFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subbandHighestFrequency.setStatus("current")


class _EnableTransmission_Type(Integer32):
    """Custom type enableTransmission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 0),
          ("muted", 1))
    )


_EnableTransmission_Type.__name__ = "Integer32"
_EnableTransmission_Object = MibScalar
enableTransmission = _EnableTransmission_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 28),
    _EnableTransmission_Type()
)
enableTransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableTransmission.setStatus("current")


class _AntennaSelection_Type(Integer32):
    """Custom type antennaSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("integrated", 0),
          ("connectorized", 1))
    )


_AntennaSelection_Type.__name__ = "Integer32"
_AntennaSelection_Object = MibScalar
antennaSelection = _AntennaSelection_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 29),
    _AntennaSelection_Type()
)
antennaSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antennaSelection.setStatus("current")


class _TransmitterChannels_Type(Integer32):
    """Custom type transmitterChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("handV", 0),
          ("hOnly", 1),
          ("vOnly", 2))
    )


_TransmitterChannels_Type.__name__ = "Integer32"
_TransmitterChannels_Object = MibScalar
transmitterChannels = _TransmitterChannels_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 30),
    _TransmitterChannels_Type()
)
transmitterChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transmitterChannels.setStatus("current")


class _WirelessTopology_Type(Integer32):
    """Custom type wirelessTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pointToPoint", 0),
          ("highCapacityMultiPoint", 1))
    )


_WirelessTopology_Type.__name__ = "Integer32"
_WirelessTopology_Object = MibScalar
wirelessTopology = _WirelessTopology_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 31),
    _WirelessTopology_Type()
)
wirelessTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessTopology.setStatus("current")


class _ConfigurationInstancedTableNumber_Type(Integer32):
    """Custom type configurationInstancedTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ConfigurationInstancedTableNumber_Type.__name__ = "Integer32"
_ConfigurationInstancedTableNumber_Object = MibScalar
configurationInstancedTableNumber = _ConfigurationInstancedTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 32),
    _ConfigurationInstancedTableNumber_Type()
)
configurationInstancedTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationInstancedTableNumber.setStatus("current")
_ConfigurationInstancedTable_Object = MibTable
configurationInstancedTable = _ConfigurationInstancedTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 33)
)
if mibBuilder.loadTexts:
    configurationInstancedTable.setStatus("current")
_ConfigurationInstancedTableEntry_Object = MibTableRow
configurationInstancedTableEntry = _ConfigurationInstancedTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 33, 1)
)
configurationInstancedTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "configurationInstancedTableIndex"),
)
if mibBuilder.loadTexts:
    configurationInstancedTableEntry.setStatus("current")


class _ConfigurationInstancedTableIndex_Type(Integer32):
    """Custom type configurationInstancedTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ConfigurationInstancedTableIndex_Type.__name__ = "Integer32"
_ConfigurationInstancedTableIndex_Object = MibTableColumn
configurationInstancedTableIndex = _ConfigurationInstancedTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 33, 1, 1),
    _ConfigurationInstancedTableIndex_Type()
)
configurationInstancedTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configurationInstancedTableIndex.setStatus("current")


class _RemoteInternetAddressType_Type(Integer32):
    """Custom type remoteInternetAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipv4z", 3),
          ("ipv6z", 4),
          ("unknown6", 5),
          ("unknown7", 6),
          ("unknown8", 7),
          ("unknown9", 8),
          ("unknown10", 9),
          ("unknown11", 10),
          ("unknown12", 11),
          ("unknown13", 12),
          ("unknown14", 13),
          ("unknown15", 14),
          ("unknown16", 15),
          ("dns", 16))
    )


_RemoteInternetAddressType_Type.__name__ = "Integer32"
_RemoteInternetAddressType_Object = MibTableColumn
remoteInternetAddressType = _RemoteInternetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 33, 1, 2),
    _RemoteInternetAddressType_Type()
)
remoteInternetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteInternetAddressType.setStatus("current")
_RemoteInternetAddress_Type = InetAddress
_RemoteInternetAddress_Object = MibTableColumn
remoteInternetAddress = _RemoteInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 33, 1, 3),
    _RemoteInternetAddress_Type()
)
remoteInternetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteInternetAddress.setStatus("current")


class _RemoteUnitName_Type(DisplayString):
    """Custom type remoteUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteUnitName_Type.__name__ = "DisplayString"
_RemoteUnitName_Object = MibTableColumn
remoteUnitName = _RemoteUnitName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 33, 1, 4),
    _RemoteUnitName_Type()
)
remoteUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUnitName.setStatus("current")


class _UnitName_Type(DisplayString):
    """Custom type unitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UnitName_Type.__name__ = "DisplayString"
_UnitName_Object = MibScalar
unitName = _UnitName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 34),
    _UnitName_Type()
)
unitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitName.setStatus("current")


class _AuthorizationMethod_Type(Integer32):
    """Custom type authorizationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("whitelist", 0),
          ("blacklist", 1))
    )


_AuthorizationMethod_Type.__name__ = "Integer32"
_AuthorizationMethod_Object = MibScalar
authorizationMethod = _AuthorizationMethod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 35),
    _AuthorizationMethod_Type()
)
authorizationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorizationMethod.setStatus("current")


class _RemoteUnitNameLinked_Type(DisplayString):
    """Custom type remoteUnitNameLinked based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteUnitNameLinked_Type.__name__ = "DisplayString"
_RemoteUnitNameLinked_Object = MibScalar
remoteUnitNameLinked = _RemoteUnitNameLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 5, 36),
    _RemoteUnitNameLinked_Type()
)
remoteUnitNameLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteUnitNameLinked.setStatus("current")
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6)
)


class _MainPSUPortAutoNegotiation_Type(Integer32):
    """Custom type mainPSUPortAutoNegotiation based on Integer32"""
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


_MainPSUPortAutoNegotiation_Type.__name__ = "Integer32"
_MainPSUPortAutoNegotiation_Object = MibScalar
mainPSUPortAutoNegotiation = _MainPSUPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 1),
    _MainPSUPortAutoNegotiation_Type()
)
mainPSUPortAutoNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortAutoNegotiation.setStatus("current")


class _MainPSUPortAutoNegAdvertisement_Type(Bits):
    """Custom type mainPSUPortAutoNegAdvertisement based on Bits"""
    namedValues = NamedValues(
        *(("negInvalid", 2),
          ("neg10MbpsHalfDuplex", 3),
          ("neg10MbpsFullDuplex", 4),
          ("neg100MbpsHalfDuplex", 5),
          ("neg100MbpsFullDuplex", 6),
          ("neg1000MbpsFullDuplex", 7))
    )

_MainPSUPortAutoNegAdvertisement_Type.__name__ = "Bits"
_MainPSUPortAutoNegAdvertisement_Object = MibScalar
mainPSUPortAutoNegAdvertisement = _MainPSUPortAutoNegAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 2),
    _MainPSUPortAutoNegAdvertisement_Type()
)
mainPSUPortAutoNegAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortAutoNegAdvertisement.setStatus("current")


class _MainPSUPortAutoMdix_Type(Integer32):
    """Custom type mainPSUPortAutoMdix based on Integer32"""
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


_MainPSUPortAutoMdix_Type.__name__ = "Integer32"
_MainPSUPortAutoMdix_Object = MibScalar
mainPSUPortAutoMdix = _MainPSUPortAutoMdix_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 3),
    _MainPSUPortAutoMdix_Type()
)
mainPSUPortAutoMdix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortAutoMdix.setStatus("current")


class _MainPSUPortStatus_Type(Integer32):
    """Custom type mainPSUPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("copperLinkUp", 1),
          ("fiberLinkUp", 2))
    )


_MainPSUPortStatus_Type.__name__ = "Integer32"
_MainPSUPortStatus_Object = MibScalar
mainPSUPortStatus = _MainPSUPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 4),
    _MainPSUPortStatus_Type()
)
mainPSUPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortStatus.setStatus("current")


class _MainPSUPortSpeedAndDuplex_Type(Integer32):
    """Custom type mainPSUPortSpeedAndDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("speed1000MbpsFullDuplex", 0),
          ("speed100MbpsFullDuplex", 1),
          ("speed100MbpsHalfDuplex", 2),
          ("speed10MbpsFullDuplex", 3),
          ("speed10MbpsHalfDuplex", 4),
          ("speedUnknown6", 5))
    )


_MainPSUPortSpeedAndDuplex_Type.__name__ = "Integer32"
_MainPSUPortSpeedAndDuplex_Object = MibScalar
mainPSUPortSpeedAndDuplex = _MainPSUPortSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 5),
    _MainPSUPortSpeedAndDuplex_Type()
)
mainPSUPortSpeedAndDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortSpeedAndDuplex.setStatus("current")


class _DataPortWirelessDownAlert_Type(Integer32):
    """Custom type dataPortWirelessDownAlert based on Integer32"""
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


_DataPortWirelessDownAlert_Type.__name__ = "Integer32"
_DataPortWirelessDownAlert_Object = MibScalar
dataPortWirelessDownAlert = _DataPortWirelessDownAlert_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 6),
    _DataPortWirelessDownAlert_Type()
)
dataPortWirelessDownAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataPortWirelessDownAlert.setStatus("current")


class _UseVLANForManagementInterfaces_Type(Integer32):
    """Custom type useVLANForManagementInterfaces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noVLANTagging", 0),
          ("iEEE8021QTaggedCTagType8100", 1),
          ("iEEE8021adTaggedSTagorBTagType88a8", 2))
    )


_UseVLANForManagementInterfaces_Type.__name__ = "Integer32"
_UseVLANForManagementInterfaces_Object = MibScalar
useVLANForManagementInterfaces = _UseVLANForManagementInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 7),
    _UseVLANForManagementInterfaces_Type()
)
useVLANForManagementInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useVLANForManagementInterfaces.setStatus("current")


class _VLANManagementPriority_Type(Integer32):
    """Custom type vLANManagementPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("p0", 0),
          ("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4),
          ("p5", 5),
          ("p6", 6),
          ("p7", 7))
    )


_VLANManagementPriority_Type.__name__ = "Integer32"
_VLANManagementPriority_Object = MibScalar
vLANManagementPriority = _VLANManagementPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 8),
    _VLANManagementPriority_Type()
)
vLANManagementPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLANManagementPriority.setStatus("current")


class _VLANManagementVID_Type(Integer32):
    """Custom type vLANManagementVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_VLANManagementVID_Type.__name__ = "Integer32"
_VLANManagementVID_Object = MibScalar
vLANManagementVID = _VLANManagementVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 11),
    _VLANManagementVID_Type()
)
vLANManagementVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLANManagementVID.setStatus("current")


class _AuxPortStatus_Type(Integer32):
    """Custom type auxPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("copperLinkUp", 1))
    )


_AuxPortStatus_Type.__name__ = "Integer32"
_AuxPortStatus_Object = MibScalar
auxPortStatus = _AuxPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 12),
    _AuxPortStatus_Type()
)
auxPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortStatus.setStatus("current")


class _AuxPortSpeedAndDuplex_Type(Integer32):
    """Custom type auxPortSpeedAndDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("speed1000MbpsFullDuplex", 0),
          ("speed100MbpsFullDuplex", 1),
          ("speed100MbpsHalfDuplex", 2),
          ("speed10MbpsFullDuplex", 3),
          ("speed10MbpsHalfDuplex", 4),
          ("speedUnknown6", 5))
    )


_AuxPortSpeedAndDuplex_Type.__name__ = "Integer32"
_AuxPortSpeedAndDuplex_Object = MibScalar
auxPortSpeedAndDuplex = _AuxPortSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 13),
    _AuxPortSpeedAndDuplex_Type()
)
auxPortSpeedAndDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortSpeedAndDuplex.setStatus("current")


class _EthernetPriorityTableNumber_Type(Integer32):
    """Custom type ethernetPriorityTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 9),
    )


_EthernetPriorityTableNumber_Type.__name__ = "Integer32"
_EthernetPriorityTableNumber_Object = MibScalar
ethernetPriorityTableNumber = _EthernetPriorityTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 14),
    _EthernetPriorityTableNumber_Type()
)
ethernetPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetPriorityTableNumber.setStatus("current")
_EthernetPriorityTable_Object = MibTable
ethernetPriorityTable = _EthernetPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 15)
)
if mibBuilder.loadTexts:
    ethernetPriorityTable.setStatus("current")
_EthernetPriorityTableEntry_Object = MibTableRow
ethernetPriorityTableEntry = _EthernetPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 15, 1)
)
ethernetPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "ethernetPriorityTableIndex"),
)
if mibBuilder.loadTexts:
    ethernetPriorityTableEntry.setStatus("current")


class _EthernetPriorityTableIndex_Type(Integer32):
    """Custom type ethernetPriorityTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("p0", 1),
          ("p1", 2),
          ("p2", 3),
          ("p3", 4),
          ("p4", 5),
          ("p5", 6),
          ("p6", 7),
          ("p7", 8),
          ("untagged", 9))
    )


_EthernetPriorityTableIndex_Type.__name__ = "Integer32"
_EthernetPriorityTableIndex_Object = MibTableColumn
ethernetPriorityTableIndex = _EthernetPriorityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 15, 1, 1),
    _EthernetPriorityTableIndex_Type()
)
ethernetPriorityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethernetPriorityTableIndex.setStatus("current")


class _EthernetPriorityQueueMapping_Type(Integer32):
    """Custom type ethernetPriorityQueueMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7))
    )


_EthernetPriorityQueueMapping_Type.__name__ = "Integer32"
_EthernetPriorityQueueMapping_Object = MibTableColumn
ethernetPriorityQueueMapping = _EthernetPriorityQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 15, 1, 2),
    _EthernetPriorityQueueMapping_Type()
)
ethernetPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetPriorityQueueMapping.setStatus("current")


class _L2CPPriorityTableNumber_Type(Integer32):
    """Custom type l2CPPriorityTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
    )


_L2CPPriorityTableNumber_Type.__name__ = "Integer32"
_L2CPPriorityTableNumber_Object = MibScalar
l2CPPriorityTableNumber = _L2CPPriorityTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 16),
    _L2CPPriorityTableNumber_Type()
)
l2CPPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2CPPriorityTableNumber.setStatus("current")
_L2CPPriorityTable_Object = MibTable
l2CPPriorityTable = _L2CPPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 17)
)
if mibBuilder.loadTexts:
    l2CPPriorityTable.setStatus("current")
_L2CPPriorityTableEntry_Object = MibTableRow
l2CPPriorityTableEntry = _L2CPPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 17, 1)
)
l2CPPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "l2CPPriorityTableIndex"),
)
if mibBuilder.loadTexts:
    l2CPPriorityTableEntry.setStatus("current")


class _L2CPPriorityTableIndex_Type(Integer32):
    """Custom type l2CPPriorityTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("mRP", 2),
          ("cFM", 3),
          ("rAPS", 4),
          ("eAPS", 5),
          ("pPPoEDiscoveryLCP", 6))
    )


_L2CPPriorityTableIndex_Type.__name__ = "Integer32"
_L2CPPriorityTableIndex_Object = MibTableColumn
l2CPPriorityTableIndex = _L2CPPriorityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 17, 1, 1),
    _L2CPPriorityTableIndex_Type()
)
l2CPPriorityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2CPPriorityTableIndex.setStatus("current")


class _L2CPPriorityQueueMapping_Type(Integer32):
    """Custom type l2CPPriorityQueueMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7))
    )


_L2CPPriorityQueueMapping_Type.__name__ = "Integer32"
_L2CPPriorityQueueMapping_Object = MibTableColumn
l2CPPriorityQueueMapping = _L2CPPriorityQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 17, 1, 2),
    _L2CPPriorityQueueMapping_Type()
)
l2CPPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2CPPriorityQueueMapping.setStatus("current")


class _IPDSCPPriorityTableNumber_Type(Integer32):
    """Custom type iPDSCPPriorityTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 64),
    )


_IPDSCPPriorityTableNumber_Type.__name__ = "Integer32"
_IPDSCPPriorityTableNumber_Object = MibScalar
iPDSCPPriorityTableNumber = _IPDSCPPriorityTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 18),
    _IPDSCPPriorityTableNumber_Type()
)
iPDSCPPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPDSCPPriorityTableNumber.setStatus("current")
_IPDSCPPriorityTable_Object = MibTable
iPDSCPPriorityTable = _IPDSCPPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 19)
)
if mibBuilder.loadTexts:
    iPDSCPPriorityTable.setStatus("current")
_IPDSCPPriorityTableEntry_Object = MibTableRow
iPDSCPPriorityTableEntry = _IPDSCPPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 19, 1)
)
iPDSCPPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "iPDSCPPriorityTableIndex"),
)
if mibBuilder.loadTexts:
    iPDSCPPriorityTableEntry.setStatus("current")


class _IPDSCPPriorityTableIndex_Type(Integer32):
    """Custom type iPDSCPPriorityTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IPDSCPPriorityTableIndex_Type.__name__ = "Integer32"
_IPDSCPPriorityTableIndex_Object = MibTableColumn
iPDSCPPriorityTableIndex = _IPDSCPPriorityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 19, 1, 1),
    _IPDSCPPriorityTableIndex_Type()
)
iPDSCPPriorityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iPDSCPPriorityTableIndex.setStatus("current")


class _IPDSCPPriorityQueueMapping_Type(Integer32):
    """Custom type iPDSCPPriorityQueueMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7))
    )


_IPDSCPPriorityQueueMapping_Type.__name__ = "Integer32"
_IPDSCPPriorityQueueMapping_Object = MibTableColumn
iPDSCPPriorityQueueMapping = _IPDSCPPriorityQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 19, 1, 2),
    _IPDSCPPriorityQueueMapping_Type()
)
iPDSCPPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPDSCPPriorityQueueMapping.setStatus("current")


class _MPLSTCPriorityTableNumber_Type(Integer32):
    """Custom type mPLSTCPriorityTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8),
    )


_MPLSTCPriorityTableNumber_Type.__name__ = "Integer32"
_MPLSTCPriorityTableNumber_Object = MibScalar
mPLSTCPriorityTableNumber = _MPLSTCPriorityTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 20),
    _MPLSTCPriorityTableNumber_Type()
)
mPLSTCPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mPLSTCPriorityTableNumber.setStatus("current")
_MPLSTCPriorityTable_Object = MibTable
mPLSTCPriorityTable = _MPLSTCPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 21)
)
if mibBuilder.loadTexts:
    mPLSTCPriorityTable.setStatus("current")
_MPLSTCPriorityTableEntry_Object = MibTableRow
mPLSTCPriorityTableEntry = _MPLSTCPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 21, 1)
)
mPLSTCPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "mPLSTCPriorityTableIndex"),
)
if mibBuilder.loadTexts:
    mPLSTCPriorityTableEntry.setStatus("current")


class _MPLSTCPriorityTableIndex_Type(Integer32):
    """Custom type mPLSTCPriorityTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MPLSTCPriorityTableIndex_Type.__name__ = "Integer32"
_MPLSTCPriorityTableIndex_Object = MibTableColumn
mPLSTCPriorityTableIndex = _MPLSTCPriorityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 21, 1, 1),
    _MPLSTCPriorityTableIndex_Type()
)
mPLSTCPriorityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mPLSTCPriorityTableIndex.setStatus("current")


class _MPLSTCPriorityQueueMapping_Type(Integer32):
    """Custom type mPLSTCPriorityQueueMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7))
    )


_MPLSTCPriorityQueueMapping_Type.__name__ = "Integer32"
_MPLSTCPriorityQueueMapping_Object = MibTableColumn
mPLSTCPriorityQueueMapping = _MPLSTCPriorityQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 21, 1, 2),
    _MPLSTCPriorityQueueMapping_Type()
)
mPLSTCPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mPLSTCPriorityQueueMapping.setStatus("current")


class _ManagementPortWirelessDownAlert_Type(Integer32):
    """Custom type managementPortWirelessDownAlert based on Integer32"""
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


_ManagementPortWirelessDownAlert_Type.__name__ = "Integer32"
_ManagementPortWirelessDownAlert_Object = MibScalar
managementPortWirelessDownAlert = _ManagementPortWirelessDownAlert_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 23),
    _ManagementPortWirelessDownAlert_Type()
)
managementPortWirelessDownAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementPortWirelessDownAlert.setStatus("current")


class _QOSPriorityScheme_Type(Integer32):
    """Custom type qOSPriorityScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 0),
          ("iPMPLS", 1))
    )


_QOSPriorityScheme_Type.__name__ = "Integer32"
_QOSPriorityScheme_Object = MibScalar
qOSPriorityScheme = _QOSPriorityScheme_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 24),
    _QOSPriorityScheme_Type()
)
qOSPriorityScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qOSPriorityScheme.setStatus("current")


class _UnknownNetworkPriorityQueueMapping_Type(Integer32):
    """Custom type unknownNetworkPriorityQueueMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7))
    )


_UnknownNetworkPriorityQueueMapping_Type.__name__ = "Integer32"
_UnknownNetworkPriorityQueueMapping_Object = MibScalar
unknownNetworkPriorityQueueMapping = _UnknownNetworkPriorityQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 25),
    _UnknownNetworkPriorityQueueMapping_Type()
)
unknownNetworkPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknownNetworkPriorityQueueMapping.setStatus("current")


class _DSCPManagementPriority_Type(Integer32):
    """Custom type dSCPManagementPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DSCPManagementPriority_Type.__name__ = "Integer32"
_DSCPManagementPriority_Object = MibScalar
dSCPManagementPriority = _DSCPManagementPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 26),
    _DSCPManagementPriority_Type()
)
dSCPManagementPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSCPManagementPriority.setStatus("current")


class _DataBridgingStatusLinked_Type(Integer32):
    """Custom type dataBridgingStatusLinked based on Integer32"""
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


_DataBridgingStatusLinked_Type.__name__ = "Integer32"
_DataBridgingStatusLinked_Object = MibScalar
dataBridgingStatusLinked = _DataBridgingStatusLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 27),
    _DataBridgingStatusLinked_Type()
)
dataBridgingStatusLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataBridgingStatusLinked.setStatus("current")


class _MainPSUPortAllocation_Type(Integer32):
    """Custom type mainPSUPortAllocation based on Integer32"""
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
        *(("disabled", 0),
          ("dataOnly", 1),
          ("dataandInBandManagement", 2),
          ("outofBandLocalManagement", 3),
          ("outofBandRemoteManagement", 4))
    )


_MainPSUPortAllocation_Type.__name__ = "Integer32"
_MainPSUPortAllocation_Object = MibScalar
mainPSUPortAllocation = _MainPSUPortAllocation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 28),
    _MainPSUPortAllocation_Type()
)
mainPSUPortAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortAllocation.setStatus("current")


class _AuxPortAllocation_Type(Integer32):
    """Custom type auxPortAllocation based on Integer32"""
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
        *(("disabled", 0),
          ("dataOnly", 1),
          ("dataandInBandManagement", 2),
          ("outofBandLocalManagement", 3),
          ("outofBandRemoteManagement", 4))
    )


_AuxPortAllocation_Type.__name__ = "Integer32"
_AuxPortAllocation_Object = MibScalar
auxPortAllocation = _AuxPortAllocation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 29),
    _AuxPortAllocation_Type()
)
auxPortAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortAllocation.setStatus("current")


class _SFPPortAllocation_Type(Integer32):
    """Custom type sFPPortAllocation based on Integer32"""
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
        *(("disabled", 0),
          ("dataOnly", 1),
          ("dataandInBandManagement", 2),
          ("outofBandLocalManagement", 3),
          ("outofBandRemoteManagement", 4))
    )


_SFPPortAllocation_Type.__name__ = "Integer32"
_SFPPortAllocation_Object = MibScalar
sFPPortAllocation = _SFPPortAllocation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 30),
    _SFPPortAllocation_Type()
)
sFPPortAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortAllocation.setStatus("current")


class _DataPortPauseFrames_Type(Integer32):
    """Custom type dataPortPauseFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 0),
          ("discard", 1))
    )


_DataPortPauseFrames_Type.__name__ = "Integer32"
_DataPortPauseFrames_Object = MibScalar
dataPortPauseFrames = _DataPortPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 31),
    _DataPortPauseFrames_Type()
)
dataPortPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortPauseFrames.setStatus("current")


class _SFPPortAutoNegotiation_Type(Integer32):
    """Custom type sFPPortAutoNegotiation based on Integer32"""
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


_SFPPortAutoNegotiation_Type.__name__ = "Integer32"
_SFPPortAutoNegotiation_Object = MibScalar
sFPPortAutoNegotiation = _SFPPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 32),
    _SFPPortAutoNegotiation_Type()
)
sFPPortAutoNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortAutoNegotiation.setStatus("current")


class _SFPPortAutoNegAdvertisement_Type(Bits):
    """Custom type sFPPortAutoNegAdvertisement based on Bits"""
    namedValues = NamedValues(
        *(("negInvalid", 2),
          ("neg10MbpsHalfDuplex", 3),
          ("neg10MbpsFullDuplex", 4),
          ("neg100MbpsHalfDuplex", 5),
          ("neg100MbpsFullDuplex", 6),
          ("neg1000MbpsFullDuplex", 7))
    )

_SFPPortAutoNegAdvertisement_Type.__name__ = "Bits"
_SFPPortAutoNegAdvertisement_Object = MibScalar
sFPPortAutoNegAdvertisement = _SFPPortAutoNegAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 33),
    _SFPPortAutoNegAdvertisement_Type()
)
sFPPortAutoNegAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortAutoNegAdvertisement.setStatus("current")


class _SFPPortAutoMdix_Type(Integer32):
    """Custom type sFPPortAutoMdix based on Integer32"""
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


_SFPPortAutoMdix_Type.__name__ = "Integer32"
_SFPPortAutoMdix_Object = MibScalar
sFPPortAutoMdix = _SFPPortAutoMdix_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 34),
    _SFPPortAutoMdix_Type()
)
sFPPortAutoMdix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortAutoMdix.setStatus("current")


class _SFPPortStatus_Type(Integer32):
    """Custom type sFPPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("copperLinkUp", 1),
          ("fiberLinkUp", 2))
    )


_SFPPortStatus_Type.__name__ = "Integer32"
_SFPPortStatus_Object = MibScalar
sFPPortStatus = _SFPPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 35),
    _SFPPortStatus_Type()
)
sFPPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortStatus.setStatus("current")


class _SFPPortSpeedAndDuplex_Type(Integer32):
    """Custom type sFPPortSpeedAndDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("speed1000MbpsFullDuplex", 0),
          ("speed100MbpsFullDuplex", 1),
          ("speed100MbpsHalfDuplex", 2),
          ("speed10MbpsFullDuplex", 3),
          ("speed10MbpsHalfDuplex", 4),
          ("speedUnknown6", 5))
    )


_SFPPortSpeedAndDuplex_Type.__name__ = "Integer32"
_SFPPortSpeedAndDuplex_Object = MibScalar
sFPPortSpeedAndDuplex = _SFPPortSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 36),
    _SFPPortSpeedAndDuplex_Type()
)
sFPPortSpeedAndDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortSpeedAndDuplex.setStatus("current")


class _AuxPortPowerOverEthernetOutput_Type(Integer32):
    """Custom type auxPortPowerOverEthernetOutput based on Integer32"""
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


_AuxPortPowerOverEthernetOutput_Type.__name__ = "Integer32"
_AuxPortPowerOverEthernetOutput_Object = MibScalar
auxPortPowerOverEthernetOutput = _AuxPortPowerOverEthernetOutput_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 37),
    _AuxPortPowerOverEthernetOutput_Type()
)
auxPortPowerOverEthernetOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortPowerOverEthernetOutput.setStatus("current")


class _AuxPortPowerOverEthernetOutputStatus_Type(Integer32):
    """Custom type auxPortPowerOverEthernetOutputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("poEOutputOn", 0),
          ("poEOutputDisabled", 1),
          ("poEOutputEnabledbutNotActiveErrororNoLoadPresent", 2),
          ("poEOutputOverloadError", 3),
          ("poEOutputOverTempError", 4),
          ("poEOutputErrorDetected", 5))
    )


_AuxPortPowerOverEthernetOutputStatus_Type.__name__ = "Integer32"
_AuxPortPowerOverEthernetOutputStatus_Object = MibScalar
auxPortPowerOverEthernetOutputStatus = _AuxPortPowerOverEthernetOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 38),
    _AuxPortPowerOverEthernetOutputStatus_Type()
)
auxPortPowerOverEthernetOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortPowerOverEthernetOutputStatus.setStatus("current")


class _SyncETracking_Type(Integer32):
    """Custom type syncETracking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("internalTDMUseOnly", 2))
    )


_SyncETracking_Type.__name__ = "Integer32"
_SyncETracking_Object = MibScalar
syncETracking = _SyncETracking_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 39),
    _SyncETracking_Type()
)
syncETracking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncETracking.setStatus("current")


class _SyncEEquipmentClock_Type(Integer32):
    """Custom type syncEEquipmentClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eECOption1", 0),
          ("eECOption2", 1))
    )


_SyncEEquipmentClock_Type.__name__ = "Integer32"
_SyncEEquipmentClock_Object = MibScalar
syncEEquipmentClock = _SyncEEquipmentClock_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 40),
    _SyncEEquipmentClock_Type()
)
syncEEquipmentClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncEEquipmentClock.setStatus("current")


class _MainPSUPortQLRxOverwrite_Type(Integer32):
    """Custom type mainPSUPortQLRxOverwrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("qLPRS", 1),
          ("qLSTU", 2),
          ("qLPRC", 3),
          ("qLST2", 4),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST3E", 7),
          ("qLEEC2QLST3", 8),
          ("qLEEC1QLSEC", 9),
          ("qLSMC", 10),
          ("qLPROV", 11),
          ("qLDNUQLDUS", 12))
    )


_MainPSUPortQLRxOverwrite_Type.__name__ = "Integer32"
_MainPSUPortQLRxOverwrite_Object = MibScalar
mainPSUPortQLRxOverwrite = _MainPSUPortQLRxOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 41),
    _MainPSUPortQLRxOverwrite_Type()
)
mainPSUPortQLRxOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainPSUPortQLRxOverwrite.setStatus("current")


class _MainPSUPortSSMTx_Type(Integer32):
    """Custom type mainPSUPortSSMTx based on Integer32"""
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


_MainPSUPortSSMTx_Type.__name__ = "Integer32"
_MainPSUPortSSMTx_Object = MibScalar
mainPSUPortSSMTx = _MainPSUPortSSMTx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 42),
    _MainPSUPortSSMTx_Type()
)
mainPSUPortSSMTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainPSUPortSSMTx.setStatus("current")


class _SFPPortSSMTx_Type(Integer32):
    """Custom type sFPPortSSMTx based on Integer32"""
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


_SFPPortSSMTx_Type.__name__ = "Integer32"
_SFPPortSSMTx_Object = MibScalar
sFPPortSSMTx = _SFPPortSSMTx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 43),
    _SFPPortSSMTx_Type()
)
sFPPortSSMTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFPPortSSMTx.setStatus("current")


class _AuxPortSSMTx_Type(Integer32):
    """Custom type auxPortSSMTx based on Integer32"""
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


_AuxPortSSMTx_Type.__name__ = "Integer32"
_AuxPortSSMTx_Object = MibScalar
auxPortSSMTx = _AuxPortSSMTx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 44),
    _AuxPortSSMTx_Type()
)
auxPortSSMTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxPortSSMTx.setStatus("current")


class _SyncETrackingState_Type(Integer32):
    """Custom type syncETrackingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("acquiringWirelessLock", 1),
          ("freeRunning", 2),
          ("lockedLocalAcquiringHoldover", 3),
          ("lockedLocalHoldoverAcquired", 4),
          ("holdover", 5),
          ("lockedRemoteAcquiringHoldover", 6),
          ("lockedRemoteHoldoverAcquired", 7))
    )


_SyncETrackingState_Type.__name__ = "Integer32"
_SyncETrackingState_Object = MibScalar
syncETrackingState = _SyncETrackingState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 45),
    _SyncETrackingState_Type()
)
syncETrackingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncETrackingState.setStatus("current")


class _MainPSUPortQLRx_Type(Integer32):
    """Custom type mainPSUPortQLRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLPRS", 1),
          ("qLSTU", 2),
          ("qLPRC", 3),
          ("qLST2", 4),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST3E", 7),
          ("qLEEC2QLST3", 8),
          ("qLEEC1QLSEC", 9),
          ("qLSMC", 10),
          ("qLPROV", 11),
          ("qLDNUQLDUS", 12),
          ("qLFAILED", 13))
    )


_MainPSUPortQLRx_Type.__name__ = "Integer32"
_MainPSUPortQLRx_Object = MibScalar
mainPSUPortQLRx = _MainPSUPortQLRx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 46),
    _MainPSUPortQLRx_Type()
)
mainPSUPortQLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortQLRx.setStatus("current")


class _AuxPortQLRx_Type(Integer32):
    """Custom type auxPortQLRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLPRS", 1),
          ("qLSTU", 2),
          ("qLPRC", 3),
          ("qLST2", 4),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST3E", 7),
          ("qLEEC2QLST3", 8),
          ("qLEEC1QLSEC", 9),
          ("qLSMC", 10),
          ("qLPROV", 11),
          ("qLDNUQLDUS", 12),
          ("qLFAILED", 13))
    )


_AuxPortQLRx_Type.__name__ = "Integer32"
_AuxPortQLRx_Object = MibScalar
auxPortQLRx = _AuxPortQLRx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 47),
    _AuxPortQLRx_Type()
)
auxPortQLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortQLRx.setStatus("current")


class _SFPPortQLRx_Type(Integer32):
    """Custom type sFPPortQLRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLPRS", 1),
          ("qLSTU", 2),
          ("qLPRC", 3),
          ("qLST2", 4),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST3E", 7),
          ("qLEEC2QLST3", 8),
          ("qLEEC1QLSEC", 9),
          ("qLSMC", 10),
          ("qLPROV", 11),
          ("qLDNUQLDUS", 12),
          ("qLFAILED", 13))
    )


_SFPPortQLRx_Type.__name__ = "Integer32"
_SFPPortQLRx_Object = MibScalar
sFPPortQLRx = _SFPPortQLRx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 48),
    _SFPPortQLRx_Type()
)
sFPPortQLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortQLRx.setStatus("current")


class _MainPSUPortQLTx_Type(Integer32):
    """Custom type mainPSUPortQLTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLPRS", 1),
          ("qLSTU", 2),
          ("qLPRC", 3),
          ("qLST2", 4),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST3E", 7),
          ("qLEEC2QLST3", 8),
          ("qLEEC1QLSEC", 9),
          ("qLSMC", 10),
          ("qLPROV", 11),
          ("qLDNUQLDUS", 12))
    )


_MainPSUPortQLTx_Type.__name__ = "Integer32"
_MainPSUPortQLTx_Object = MibScalar
mainPSUPortQLTx = _MainPSUPortQLTx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 49),
    _MainPSUPortQLTx_Type()
)
mainPSUPortQLTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortQLTx.setStatus("current")


class _AuxPortQLTx_Type(Integer32):
    """Custom type auxPortQLTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLPRS", 1),
          ("qLSTU", 2),
          ("qLPRC", 3),
          ("qLST2", 4),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST3E", 7),
          ("qLEEC2QLST3", 8),
          ("qLEEC1QLSEC", 9),
          ("qLSMC", 10),
          ("qLPROV", 11),
          ("qLDNUQLDUS", 12))
    )


_AuxPortQLTx_Type.__name__ = "Integer32"
_AuxPortQLTx_Object = MibScalar
auxPortQLTx = _AuxPortQLTx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 50),
    _AuxPortQLTx_Type()
)
auxPortQLTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortQLTx.setStatus("current")


class _SFPPortQLTx_Type(Integer32):
    """Custom type sFPPortQLTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLPRS", 1),
          ("qLSTU", 2),
          ("qLPRC", 3),
          ("qLST2", 4),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST3E", 7),
          ("qLEEC2QLST3", 8),
          ("qLEEC1QLSEC", 9),
          ("qLSMC", 10),
          ("qLPROV", 11),
          ("qLDNUQLDUS", 12))
    )


_SFPPortQLTx_Type.__name__ = "Integer32"
_SFPPortQLTx_Object = MibScalar
sFPPortQLTx = _SFPPortQLTx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 51),
    _SFPPortQLTx_Type()
)
sFPPortQLTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortQLTx.setStatus("current")


class _MainPSUPortSyncEMasterSlaveStatus_Type(Integer32):
    """Custom type mainPSUPortSyncEMasterSlaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )


_MainPSUPortSyncEMasterSlaveStatus_Type.__name__ = "Integer32"
_MainPSUPortSyncEMasterSlaveStatus_Object = MibScalar
mainPSUPortSyncEMasterSlaveStatus = _MainPSUPortSyncEMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 52),
    _MainPSUPortSyncEMasterSlaveStatus_Type()
)
mainPSUPortSyncEMasterSlaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortSyncEMasterSlaveStatus.setStatus("current")


class _AuxPortSyncEMasterSlaveStatus_Type(Integer32):
    """Custom type auxPortSyncEMasterSlaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )


_AuxPortSyncEMasterSlaveStatus_Type.__name__ = "Integer32"
_AuxPortSyncEMasterSlaveStatus_Object = MibScalar
auxPortSyncEMasterSlaveStatus = _AuxPortSyncEMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 53),
    _AuxPortSyncEMasterSlaveStatus_Type()
)
auxPortSyncEMasterSlaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortSyncEMasterSlaveStatus.setStatus("current")


class _SFPPortSyncEMasterSlaveStatus_Type(Integer32):
    """Custom type sFPPortSyncEMasterSlaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )


_SFPPortSyncEMasterSlaveStatus_Type.__name__ = "Integer32"
_SFPPortSyncEMasterSlaveStatus_Object = MibScalar
sFPPortSyncEMasterSlaveStatus = _SFPPortSyncEMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 54),
    _SFPPortSyncEMasterSlaveStatus_Type()
)
sFPPortSyncEMasterSlaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortSyncEMasterSlaveStatus.setStatus("current")


class _MainPSUPortGigabitMasterSlaveStatus_Type(Integer32):
    """Custom type mainPSUPortGigabitMasterSlaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1),
          ("notApplicable", 2))
    )


_MainPSUPortGigabitMasterSlaveStatus_Type.__name__ = "Integer32"
_MainPSUPortGigabitMasterSlaveStatus_Object = MibScalar
mainPSUPortGigabitMasterSlaveStatus = _MainPSUPortGigabitMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 55),
    _MainPSUPortGigabitMasterSlaveStatus_Type()
)
mainPSUPortGigabitMasterSlaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortGigabitMasterSlaveStatus.setStatus("current")


class _AuxPortGigabitMasterSlaveStatus_Type(Integer32):
    """Custom type auxPortGigabitMasterSlaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1),
          ("notApplicable", 2))
    )


_AuxPortGigabitMasterSlaveStatus_Type.__name__ = "Integer32"
_AuxPortGigabitMasterSlaveStatus_Object = MibScalar
auxPortGigabitMasterSlaveStatus = _AuxPortGigabitMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 56),
    _AuxPortGigabitMasterSlaveStatus_Type()
)
auxPortGigabitMasterSlaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortGigabitMasterSlaveStatus.setStatus("current")


class _SFPPortGigabitMasterSlaveStatus_Type(Integer32):
    """Custom type sFPPortGigabitMasterSlaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1),
          ("notApplicable", 2))
    )


_SFPPortGigabitMasterSlaveStatus_Type.__name__ = "Integer32"
_SFPPortGigabitMasterSlaveStatus_Object = MibScalar
sFPPortGigabitMasterSlaveStatus = _SFPPortGigabitMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 57),
    _SFPPortGigabitMasterSlaveStatus_Type()
)
sFPPortGigabitMasterSlaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortGigabitMasterSlaveStatus.setStatus("current")


class _TransparentClock_Type(Integer32):
    """Custom type transparentClock based on Integer32"""
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


_TransparentClock_Type.__name__ = "Integer32"
_TransparentClock_Object = MibScalar
transparentClock = _TransparentClock_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 58),
    _TransparentClock_Type()
)
transparentClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transparentClock.setStatus("current")


class _TransparentClockVLAN_Type(Integer32):
    """Custom type transparentClockVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("sTagged", 1),
          ("cTagged", 2))
    )


_TransparentClockVLAN_Type.__name__ = "Integer32"
_TransparentClockVLAN_Object = MibScalar
transparentClockVLAN = _TransparentClockVLAN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 59),
    _TransparentClockVLAN_Type()
)
transparentClockVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transparentClockVLAN.setStatus("current")


class _TransparentClockVID_Type(Integer32):
    """Custom type transparentClockVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_TransparentClockVID_Type.__name__ = "Integer32"
_TransparentClockVID_Object = MibScalar
transparentClockVID = _TransparentClockVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 60),
    _TransparentClockVID_Type()
)
transparentClockVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transparentClockVID.setStatus("current")


class _MainPSUPortAcceptedQLRx_Type(Integer32):
    """Custom type mainPSUPortAcceptedQLRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLPRS", 1),
          ("qLSTU", 2),
          ("qLPRC", 3),
          ("qLST2", 4),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST3E", 7),
          ("qLEEC2QLST3", 8),
          ("qLEEC1QLSEC", 9),
          ("qLSMC", 10),
          ("qLPROV", 11),
          ("qLDNUQLDUS", 12),
          ("qLFAILED", 13))
    )


_MainPSUPortAcceptedQLRx_Type.__name__ = "Integer32"
_MainPSUPortAcceptedQLRx_Object = MibScalar
mainPSUPortAcceptedQLRx = _MainPSUPortAcceptedQLRx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 61),
    _MainPSUPortAcceptedQLRx_Type()
)
mainPSUPortAcceptedQLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortAcceptedQLRx.setStatus("current")


class _AuxPortAcceptedQLRx_Type(Integer32):
    """Custom type auxPortAcceptedQLRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLPRS", 1),
          ("qLSTU", 2),
          ("qLPRC", 3),
          ("qLST2", 4),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST3E", 7),
          ("qLEEC2QLST3", 8),
          ("qLEEC1QLSEC", 9),
          ("qLSMC", 10),
          ("qLPROV", 11),
          ("qLDNUQLDUS", 12),
          ("qLFAILED", 13))
    )


_AuxPortAcceptedQLRx_Type.__name__ = "Integer32"
_AuxPortAcceptedQLRx_Object = MibScalar
auxPortAcceptedQLRx = _AuxPortAcceptedQLRx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 62),
    _AuxPortAcceptedQLRx_Type()
)
auxPortAcceptedQLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortAcceptedQLRx.setStatus("current")


class _SFPPortAcceptedQLRx_Type(Integer32):
    """Custom type sFPPortAcceptedQLRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("qLPRS", 1),
          ("qLSTU", 2),
          ("qLPRC", 3),
          ("qLST2", 4),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST3E", 7),
          ("qLEEC2QLST3", 8),
          ("qLEEC1QLSEC", 9),
          ("qLSMC", 10),
          ("qLPROV", 11),
          ("qLDNUQLDUS", 12),
          ("qLFAILED", 13))
    )


_SFPPortAcceptedQLRx_Type.__name__ = "Integer32"
_SFPPortAcceptedQLRx_Object = MibScalar
sFPPortAcceptedQLRx = _SFPPortAcceptedQLRx_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 63),
    _SFPPortAcceptedQLRx_Type()
)
sFPPortAcceptedQLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortAcceptedQLRx.setStatus("current")


class _MainPSUPortSyncERxStatus_Type(Integer32):
    """Custom type mainPSUPortSyncERxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 0),
          ("waittoRestore", 1),
          ("failed", 2))
    )


_MainPSUPortSyncERxStatus_Type.__name__ = "Integer32"
_MainPSUPortSyncERxStatus_Object = MibScalar
mainPSUPortSyncERxStatus = _MainPSUPortSyncERxStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 64),
    _MainPSUPortSyncERxStatus_Type()
)
mainPSUPortSyncERxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortSyncERxStatus.setStatus("current")


class _AuxPortSyncERxStatus_Type(Integer32):
    """Custom type auxPortSyncERxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 0),
          ("waittoRestore", 1),
          ("failed", 2))
    )


_AuxPortSyncERxStatus_Type.__name__ = "Integer32"
_AuxPortSyncERxStatus_Object = MibScalar
auxPortSyncERxStatus = _AuxPortSyncERxStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 65),
    _AuxPortSyncERxStatus_Type()
)
auxPortSyncERxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortSyncERxStatus.setStatus("current")


class _SFPPortSyncERxStatus_Type(Integer32):
    """Custom type sFPPortSyncERxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 0),
          ("waittoRestore", 1),
          ("failed", 2))
    )


_SFPPortSyncERxStatus_Type.__name__ = "Integer32"
_SFPPortSyncERxStatus_Object = MibScalar
sFPPortSyncERxStatus = _SFPPortSyncERxStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 66),
    _SFPPortSyncERxStatus_Type()
)
sFPPortSyncERxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortSyncERxStatus.setStatus("current")


class _NIDULanPortStatus_Type(Integer32):
    """Custom type nIDULanPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("copperLinkUp", 1),
          ("fiberLinkUp", 2))
    )


_NIDULanPortStatus_Type.__name__ = "Integer32"
_NIDULanPortStatus_Object = MibScalar
nIDULanPortStatus = _NIDULanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 67),
    _NIDULanPortStatus_Type()
)
nIDULanPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortStatus.setStatus("current")


class _NIDULanPortSpeedAndDuplex_Type(Integer32):
    """Custom type nIDULanPortSpeedAndDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("speed1000MbpsFullDuplex", 0),
          ("speed100MbpsFullDuplex", 1),
          ("speed100MbpsHalfDuplex", 2),
          ("speed10MbpsFullDuplex", 3),
          ("speed10MbpsHalfDuplex", 4),
          ("speedUnknown6", 5))
    )


_NIDULanPortSpeedAndDuplex_Type.__name__ = "Integer32"
_NIDULanPortSpeedAndDuplex_Object = MibScalar
nIDULanPortSpeedAndDuplex = _NIDULanPortSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 68),
    _NIDULanPortSpeedAndDuplex_Type()
)
nIDULanPortSpeedAndDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortSpeedAndDuplex.setStatus("current")


class _OOBPriorityQueueMapping_Type(Integer32):
    """Custom type oOBPriorityQueueMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7))
    )


_OOBPriorityQueueMapping_Type.__name__ = "Integer32"
_OOBPriorityQueueMapping_Object = MibScalar
oOBPriorityQueueMapping = _OOBPriorityQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 69),
    _OOBPriorityQueueMapping_Type()
)
oOBPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oOBPriorityQueueMapping.setStatus("current")


class _NIDULanPortAutoNegotiation_Type(Integer32):
    """Custom type nIDULanPortAutoNegotiation based on Integer32"""
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


_NIDULanPortAutoNegotiation_Type.__name__ = "Integer32"
_NIDULanPortAutoNegotiation_Object = MibScalar
nIDULanPortAutoNegotiation = _NIDULanPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 70),
    _NIDULanPortAutoNegotiation_Type()
)
nIDULanPortAutoNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortAutoNegotiation.setStatus("current")


class _NIDULanPortAutoNegAdvertisement_Type(Bits):
    """Custom type nIDULanPortAutoNegAdvertisement based on Bits"""
    namedValues = NamedValues(
        *(("negInvalid", 2),
          ("neg10MbpsHalfDuplex", 3),
          ("neg10MbpsFullDuplex", 4),
          ("neg100MbpsHalfDuplex", 5),
          ("neg100MbpsFullDuplex", 6),
          ("neg1000MbpsFullDuplex", 7))
    )

_NIDULanPortAutoNegAdvertisement_Type.__name__ = "Bits"
_NIDULanPortAutoNegAdvertisement_Object = MibScalar
nIDULanPortAutoNegAdvertisement = _NIDULanPortAutoNegAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 71),
    _NIDULanPortAutoNegAdvertisement_Type()
)
nIDULanPortAutoNegAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortAutoNegAdvertisement.setStatus("current")


class _NIDULanPortAutoMdix_Type(Integer32):
    """Custom type nIDULanPortAutoMdix based on Integer32"""
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


_NIDULanPortAutoMdix_Type.__name__ = "Integer32"
_NIDULanPortAutoMdix_Object = MibScalar
nIDULanPortAutoMdix = _NIDULanPortAutoMdix_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 72),
    _NIDULanPortAutoMdix_Type()
)
nIDULanPortAutoMdix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortAutoMdix.setStatus("current")


class _NIDULanPortGigabitMasterSlaveStatus_Type(Integer32):
    """Custom type nIDULanPortGigabitMasterSlaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1),
          ("notApplicable", 2))
    )


_NIDULanPortGigabitMasterSlaveStatus_Type.__name__ = "Integer32"
_NIDULanPortGigabitMasterSlaveStatus_Object = MibScalar
nIDULanPortGigabitMasterSlaveStatus = _NIDULanPortGigabitMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 73),
    _NIDULanPortGigabitMasterSlaveStatus_Type()
)
nIDULanPortGigabitMasterSlaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortGigabitMasterSlaveStatus.setStatus("current")
_TxMABFrames_Type = Integer32
_TxMABFrames_Object = MibScalar
txMABFrames = _TxMABFrames_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 74),
    _TxMABFrames_Type()
)
txMABFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMABFrames.setStatus("current")


class _ManagementNetworkAccessEnabled_Type(Integer32):
    """Custom type managementNetworkAccessEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ManagementNetworkAccessEnabled_Type.__name__ = "Integer32"
_ManagementNetworkAccessEnabled_Object = MibScalar
managementNetworkAccessEnabled = _ManagementNetworkAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 75),
    _ManagementNetworkAccessEnabled_Type()
)
managementNetworkAccessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementNetworkAccessEnabled.setStatus("current")


class _TransparentClockPort_Type(Integer32):
    """Custom type transparentClockPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("mainPSU", 0),
          ("aux", 1),
          ("sFP", 2),
          ("mainPSUplusAux", 3),
          ("mainPSUplusSFP", 4),
          ("auxplusSFP", 5),
          ("mainPSUplusAuxplusSFP", 6))
    )


_TransparentClockPort_Type.__name__ = "Integer32"
_TransparentClockPort_Object = MibScalar
transparentClockPort = _TransparentClockPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 81),
    _TransparentClockPort_Type()
)
transparentClockPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transparentClockPort.setStatus("current")


class _SyncESlavePort_Type(Integer32):
    """Custom type syncESlavePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mainPSUPort", 0),
          ("sFPPort", 1))
    )


_SyncESlavePort_Type.__name__ = "Integer32"
_SyncESlavePort_Object = MibScalar
syncESlavePort = _SyncESlavePort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 82),
    _SyncESlavePort_Type()
)
syncESlavePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncESlavePort.setStatus("current")


class _SFPPortQLRxOverwrite_Type(Integer32):
    """Custom type sFPPortQLRxOverwrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("qLPRS", 1),
          ("qLSTU", 2),
          ("qLPRC", 3),
          ("qLST2", 4),
          ("qLSSUAQLTNC", 5),
          ("qLSSUB", 6),
          ("qLST3E", 7),
          ("qLEEC2QLST3", 8),
          ("qLEEC1QLSEC", 9),
          ("qLSMC", 10),
          ("qLPROV", 11),
          ("qLDNUQLDUS", 12))
    )


_SFPPortQLRxOverwrite_Type.__name__ = "Integer32"
_SFPPortQLRxOverwrite_Object = MibScalar
sFPPortQLRxOverwrite = _SFPPortQLRxOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 83),
    _SFPPortQLRxOverwrite_Type()
)
sFPPortQLRxOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFPPortQLRxOverwrite.setStatus("current")


class _EthernetInstancedTableNumber_Type(Integer32):
    """Custom type ethernetInstancedTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EthernetInstancedTableNumber_Type.__name__ = "Integer32"
_EthernetInstancedTableNumber_Object = MibScalar
ethernetInstancedTableNumber = _EthernetInstancedTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 84),
    _EthernetInstancedTableNumber_Type()
)
ethernetInstancedTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInstancedTableNumber.setStatus("current")
_EthernetInstancedTable_Object = MibTable
ethernetInstancedTable = _EthernetInstancedTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 85)
)
if mibBuilder.loadTexts:
    ethernetInstancedTable.setStatus("current")
_EthernetInstancedTableEntry_Object = MibTableRow
ethernetInstancedTableEntry = _EthernetInstancedTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 85, 1)
)
ethernetInstancedTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "ethernetInstancedTableIndex"),
)
if mibBuilder.loadTexts:
    ethernetInstancedTableEntry.setStatus("current")


class _EthernetInstancedTableIndex_Type(Integer32):
    """Custom type ethernetInstancedTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EthernetInstancedTableIndex_Type.__name__ = "Integer32"
_EthernetInstancedTableIndex_Object = MibTableColumn
ethernetInstancedTableIndex = _EthernetInstancedTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 85, 1, 1),
    _EthernetInstancedTableIndex_Type()
)
ethernetInstancedTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethernetInstancedTableIndex.setStatus("current")


class _DataBridgingStatus_Type(Integer32):
    """Custom type dataBridgingStatus based on Integer32"""
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


_DataBridgingStatus_Type.__name__ = "Integer32"
_DataBridgingStatus_Object = MibTableColumn
dataBridgingStatus = _DataBridgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 85, 1, 2),
    _DataBridgingStatus_Type()
)
dataBridgingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataBridgingStatus.setStatus("current")


class _EthernetStatisticsTableNumber_Type(Integer32):
    """Custom type ethernetStatisticsTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EthernetStatisticsTableNumber_Type.__name__ = "Integer32"
_EthernetStatisticsTableNumber_Object = MibScalar
ethernetStatisticsTableNumber = _EthernetStatisticsTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 86),
    _EthernetStatisticsTableNumber_Type()
)
ethernetStatisticsTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetStatisticsTableNumber.setStatus("current")
_EthernetStatisticsTable_Object = MibTable
ethernetStatisticsTable = _EthernetStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 87)
)
if mibBuilder.loadTexts:
    ethernetStatisticsTable.setStatus("current")
_EthernetStatisticsTableEntry_Object = MibTableRow
ethernetStatisticsTableEntry = _EthernetStatisticsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 87, 1)
)
ethernetStatisticsTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "ethernetStatisticsTableIndex"),
)
if mibBuilder.loadTexts:
    ethernetStatisticsTableEntry.setStatus("current")


class _EthernetStatisticsTableIndex_Type(Integer32):
    """Custom type ethernetStatisticsTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EthernetStatisticsTableIndex_Type.__name__ = "Integer32"
_EthernetStatisticsTableIndex_Object = MibTableColumn
ethernetStatisticsTableIndex = _EthernetStatisticsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 87, 1, 1),
    _EthernetStatisticsTableIndex_Type()
)
ethernetStatisticsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethernetStatisticsTableIndex.setStatus("current")
_EthernetStatisticsDataSource_Type = ObjectIdentifier
_EthernetStatisticsDataSource_Object = MibTableColumn
ethernetStatisticsDataSource = _EthernetStatisticsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 87, 1, 2),
    _EthernetStatisticsDataSource_Type()
)
ethernetStatisticsDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetStatisticsDataSource.setStatus("current")
_EthernetStatisticsRxOctets_Type = Counter64
_EthernetStatisticsRxOctets_Object = MibTableColumn
ethernetStatisticsRxOctets = _EthernetStatisticsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 87, 1, 3),
    _EthernetStatisticsRxOctets_Type()
)
ethernetStatisticsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetStatisticsRxOctets.setStatus("current")
_EthernetStatisticsRxFrames_Type = Counter64
_EthernetStatisticsRxFrames_Object = MibTableColumn
ethernetStatisticsRxFrames = _EthernetStatisticsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 87, 1, 4),
    _EthernetStatisticsRxFrames_Type()
)
ethernetStatisticsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetStatisticsRxFrames.setStatus("current")
_EthernetStatisticsRxBroadcasts_Type = Counter64
_EthernetStatisticsRxBroadcasts_Object = MibTableColumn
ethernetStatisticsRxBroadcasts = _EthernetStatisticsRxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 87, 1, 5),
    _EthernetStatisticsRxBroadcasts_Type()
)
ethernetStatisticsRxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetStatisticsRxBroadcasts.setStatus("current")
_EthernetStatisticsRxFramesWithError_Type = Counter64
_EthernetStatisticsRxFramesWithError_Object = MibTableColumn
ethernetStatisticsRxFramesWithError = _EthernetStatisticsRxFramesWithError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 87, 1, 6),
    _EthernetStatisticsRxFramesWithError_Type()
)
ethernetStatisticsRxFramesWithError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetStatisticsRxFramesWithError.setStatus("current")
_EthernetStatisticsRxFramesUndersize_Type = Counter64
_EthernetStatisticsRxFramesUndersize_Object = MibTableColumn
ethernetStatisticsRxFramesUndersize = _EthernetStatisticsRxFramesUndersize_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 87, 1, 7),
    _EthernetStatisticsRxFramesUndersize_Type()
)
ethernetStatisticsRxFramesUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetStatisticsRxFramesUndersize.setStatus("current")
_EthernetStatisticsRxFramesOversize_Type = Counter64
_EthernetStatisticsRxFramesOversize_Object = MibTableColumn
ethernetStatisticsRxFramesOversize = _EthernetStatisticsRxFramesOversize_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 87, 1, 8),
    _EthernetStatisticsRxFramesOversize_Type()
)
ethernetStatisticsRxFramesOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetStatisticsRxFramesOversize.setStatus("current")
_EthernetStatisticsTxOctets_Type = Counter64
_EthernetStatisticsTxOctets_Object = MibTableColumn
ethernetStatisticsTxOctets = _EthernetStatisticsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 87, 1, 9),
    _EthernetStatisticsTxOctets_Type()
)
ethernetStatisticsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetStatisticsTxOctets.setStatus("current")
_EthernetStatisticsTxFrames_Type = Counter64
_EthernetStatisticsTxFrames_Object = MibTableColumn
ethernetStatisticsTxFrames = _EthernetStatisticsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 87, 1, 10),
    _EthernetStatisticsTxFrames_Type()
)
ethernetStatisticsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetStatisticsTxFrames.setStatus("current")
_EthernetStatisticsTxBroadcasts_Type = Counter64
_EthernetStatisticsTxBroadcasts_Object = MibTableColumn
ethernetStatisticsTxBroadcasts = _EthernetStatisticsTxBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 6, 87, 1, 11),
    _EthernetStatisticsTxBroadcasts_Type()
)
ethernetStatisticsTxBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetStatisticsTxBroadcasts.setStatus("current")
_TDM_ObjectIdentity = ObjectIdentity
tDM = _TDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 7)
)


class _TDMInterfaceControl_Type(Integer32):
    """Custom type tDMInterfaceControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("e1", 1),
          ("t1", 2))
    )


_TDMInterfaceControl_Type.__name__ = "Integer32"
_TDMInterfaceControl_Object = MibScalar
tDMInterfaceControl = _TDMInterfaceControl_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 7, 1),
    _TDMInterfaceControl_Type()
)
tDMInterfaceControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMInterfaceControl.setStatus("current")


class _TDMInterfaceStatus_Type(Integer32):
    """Custom type tDMInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("connectedNotConfigured", 1),
          ("notConnected", 2),
          ("nIDUdetectedonAUXport", 3),
          ("error", 4),
          ("codeDownloadInProgress", 5))
    )


_TDMInterfaceStatus_Type.__name__ = "Integer32"
_TDMInterfaceStatus_Object = MibScalar
tDMInterfaceStatus = _TDMInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 7, 2),
    _TDMInterfaceStatus_Type()
)
tDMInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMInterfaceStatus.setStatus("current")


class _TDMEnabledChannels_Type(Integer32):
    """Custom type tDMEnabledChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_TDMEnabledChannels_Type.__name__ = "Integer32"
_TDMEnabledChannels_Object = MibScalar
tDMEnabledChannels = _TDMEnabledChannels_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 7, 3),
    _TDMEnabledChannels_Type()
)
tDMEnabledChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMEnabledChannels.setStatus("current")


class _TdmTableNumber_Type(Integer32):
    """Custom type tdmTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TdmTableNumber_Type.__name__ = "Integer32"
_TdmTableNumber_Object = MibScalar
tdmTableNumber = _TdmTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 7, 4),
    _TdmTableNumber_Type()
)
tdmTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmTableNumber.setStatus("current")
_TdmTable_Object = MibTable
tdmTable = _TdmTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 7, 5)
)
if mibBuilder.loadTexts:
    tdmTable.setStatus("current")
_TdmTableEntry_Object = MibTableRow
tdmTableEntry = _TdmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 7, 5, 1)
)
tdmTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "tdmTableIndex"),
)
if mibBuilder.loadTexts:
    tdmTableEntry.setStatus("current")


class _TdmTableIndex_Type(Integer32):
    """Custom type tdmTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TdmTableIndex_Type.__name__ = "Integer32"
_TdmTableIndex_Object = MibTableColumn
tdmTableIndex = _TdmTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 7, 5, 1, 1),
    _TdmTableIndex_Type()
)
tdmTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdmTableIndex.setStatus("current")


class _TDMChannelStatus_Type(Integer32):
    """Custom type tDMChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("noSignalLocal", 1),
          ("noSignalRemote", 2),
          ("noSignalLocalandRemote", 3),
          ("remoteTiming", 4),
          ("noSignalLocalandRemoteTiming", 5),
          ("disabled", 6))
    )


_TDMChannelStatus_Type.__name__ = "Integer32"
_TDMChannelStatus_Object = MibTableColumn
tDMChannelStatus = _TDMChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 7, 5, 1, 2),
    _TDMChannelStatus_Type()
)
tDMChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMChannelStatus.setStatus("current")


class _TDMChannelLineCode_Type(Integer32):
    """Custom type tDMChannelLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aMI", 0),
          ("b8ZSorHDB3", 1))
    )


_TDMChannelLineCode_Type.__name__ = "Integer32"
_TDMChannelLineCode_Object = MibTableColumn
tDMChannelLineCode = _TDMChannelLineCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 7, 5, 1, 3),
    _TDMChannelLineCode_Type()
)
tDMChannelLineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMChannelLineCode.setStatus("current")


class _TDMChannelCableLength_Type(Integer32):
    """Custom type tDMChannelCableLength based on Integer32"""
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
        *(("feet133", 0),
          ("feet266", 1),
          ("feet399", 2),
          ("feet533", 3),
          ("feet655", 4))
    )


_TDMChannelCableLength_Type.__name__ = "Integer32"
_TDMChannelCableLength_Object = MibTableColumn
tDMChannelCableLength = _TDMChannelCableLength_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 7, 5, 1, 4),
    _TDMChannelCableLength_Type()
)
tDMChannelCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMChannelCableLength.setStatus("current")


class _TDMChannelLoopback_Type(Integer32):
    """Custom type tDMChannelLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("copper", 1),
          ("wireless", 2))
    )


_TDMChannelLoopback_Type.__name__ = "Integer32"
_TDMChannelLoopback_Object = MibTableColumn
tDMChannelLoopback = _TDMChannelLoopback_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 7, 5, 1, 5),
    _TDMChannelLoopback_Type()
)
tDMChannelLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMChannelLoopback.setStatus("current")


class _TDMConfigurationMismatch_Type(Integer32):
    """Custom type tDMConfigurationMismatch based on Integer32"""
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
        *(("ok", 0),
          ("linetypemismatch", 1),
          ("enabledchannelsmismatch", 2),
          ("linetypeandenabledchannelsmismatch", 3))
    )


_TDMConfigurationMismatch_Type.__name__ = "Integer32"
_TDMConfigurationMismatch_Object = MibScalar
tDMConfigurationMismatch = _TDMConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 7, 6),
    _TDMConfigurationMismatch_Type()
)
tDMConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMConfigurationMismatch.setStatus("current")


class _LowestTDMModulationMode_Type(Integer32):
    """Custom type lowestTDMModulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("modAcquisition", 0),
          ("modBpsk63percent", 1),
          ("modQpsk63percentSingle", 2),
          ("modTransient1", 3),
          ("modQpsk87percentSingle", 4),
          ("modTransient2", 5),
          ("mod16qam63percentSingleA", 6),
          ("modTransient3", 7),
          ("mod16qam87percentSingle", 8),
          ("modTransient4", 9),
          ("mod64qam75percentSingle", 10),
          ("modTransient5", 11),
          ("mod64qam92percentSingle", 12),
          ("modTransient6", 13),
          ("mod256qam81percentSingle", 14),
          ("mod16qam63percentSingleB", 15),
          ("mod16qam63percentDual", 16),
          ("modTransient7", 17),
          ("mod16qam87percentDual", 18),
          ("modTransient8", 19),
          ("mod64qam75percentDual", 20),
          ("modTransient9", 21),
          ("mod64qam92percentDual", 22),
          ("modTransient10", 23),
          ("mod256qam81percentDual", 24))
    )


_LowestTDMModulationMode_Type.__name__ = "Integer32"
_LowestTDMModulationMode_Object = MibScalar
lowestTDMModulationMode = _LowestTDMModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 7, 7),
    _LowestTDMModulationMode_Type()
)
lowestTDMModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowestTDMModulationMode.setStatus("current")
_License_ObjectIdentity = ObjectIdentity
license = _License_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8)
)


class _RegulatoryBand_Type(Integer32):
    """Custom type regulatoryBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("regInvalid", 0),
          ("reg158GHz", 1),
          ("reg258GHz", 2),
          ("reg358GHz", 3),
          ("reg458GHzWithRTTT", 4),
          ("reg558GHz", 5),
          ("reg658GHz", 6),
          ("reg754GHz", 7),
          ("reg854GHz", 8),
          ("reg954GHz", 9),
          ("reg1058GHz", 10),
          ("reg1158GHz", 11),
          ("reg1254GHz", 12),
          ("reg1354GHz", 13),
          ("reg1449GHzPublicSafety", 14),
          ("reg15", 15),
          ("reg1659GHz", 16),
          ("reg1759GHz", 17),
          ("reg1849GHzPublicSafety", 18),
          ("reg1958GHz", 19),
          ("reg2054GHz", 20),
          ("reg2154GHz", 21),
          ("reg2258GHz", 22),
          ("reg23", 23),
          ("reg2458GHz", 24),
          ("reg2558GHz", 25),
          ("reg2654GHz", 26),
          ("reg2758GHz", 27),
          ("reg2858GHz", 28),
          ("reg2958GHz", 29),
          ("reg3054GHz", 30),
          ("reg3158GHz", 31),
          ("reg3249GHzLicensed", 32),
          ("reg3349GHzETSIBroadbandDisasterRelief", 33),
          ("reg3458GHz", 34),
          ("reg3558GHz", 35),
          ("reg3654GHz", 36),
          ("reg3758GHz", 37),
          ("reg3852GHz", 38),
          ("reg3951GHzETSIBroadbandDisasterRelief", 39),
          ("reg4054GHz", 40),
          ("reg4154GHz", 41),
          ("reg4254GHz", 42),
          ("reg4354GHz", 43),
          ("reg4458GHz", 44),
          ("reg4558GHz", 45),
          ("reg4658GHz", 46),
          ("reg4758GHz", 47),
          ("reg4858GHz", 48),
          ("reg4958GHz", 49),
          ("reg5058GHz", 50),
          ("reg5158GHz", 51),
          ("reg5258GHz", 52),
          ("reg5358GHz", 53),
          ("reg5458GHz", 54),
          ("reg5558GHz", 55),
          ("reg5654GHz", 56),
          ("reg5754GHz", 57),
          ("reg5858GHz", 58),
          ("reg5958GHz", 59),
          ("reg6058GHz", 60),
          ("reg6149GHz", 61),
          ("reg6251GHz52GHz", 62),
          ("reg6352GHz", 63),
          ("reg6451GHz", 64),
          ("reg6551GHz", 65),
          ("reg6651GHz", 66),
          ("reg6752GHz", 67),
          ("reg6852GHz", 68),
          ("reg6952GHz", 69),
          ("reg7052GHz", 70),
          ("reg7152GHz", 71),
          ("reg7252GHz", 72),
          ("reg7352GHz", 73),
          ("reg7452GHz", 74),
          ("reg7552GHz", 75),
          ("reg7652GHz", 76),
          ("reg7752GHz", 77),
          ("reg7849GHz", 78),
          ("reg7954GHz", 79),
          ("reg8049GHz", 80),
          ("reg8147GHz", 81),
          ("reg8247GHz", 82),
          ("reg8352GHz", 83),
          ("reg8451GHz", 84),
          ("reg8551GHz52GHz", 85),
          ("reg8652GHz54GHz", 86),
          ("reg8758GHz", 87),
          ("reg8849GHz", 88),
          ("reg8949GHz", 89),
          ("reg9054GHzParabolicantenna", 90),
          ("reg9152GHzParabolicantenna", 91),
          ("reg9251GHzParabolicantenna", 92),
          ("reg9349GHz", 93),
          ("reg9449GHz", 94),
          ("reg9545GHz", 95),
          ("reg9648GHz", 96),
          ("reg9752GHz", 97),
          ("reg9849GHz27dBiantenna", 98),
          ("reg9949GHz29dBiantenna", 99),
          ("reg10048GHz", 100),
          ("reg10158GHz", 101),
          ("reg102", 102),
          ("reg103", 103),
          ("reg10458GHzNoRTTT", 104),
          ("reg105", 105),
          ("reg106", 106),
          ("reg107", 107),
          ("reg108", 108),
          ("reg109", 109),
          ("reg110", 110),
          ("reg111", 111),
          ("reg112", 112),
          ("reg113", 113),
          ("reg114", 114),
          ("reg115", 115),
          ("reg116", 116),
          ("reg117", 117),
          ("reg118", 118),
          ("reg119", 119),
          ("reg120", 120),
          ("reg121", 121),
          ("reg122", 122),
          ("reg123", 123),
          ("reg124", 124),
          ("reg125", 125),
          ("reg126", 126),
          ("reg127", 127),
          ("reg128", 128),
          ("reg129", 129),
          ("reg130", 130),
          ("reg131", 131),
          ("reg132", 132),
          ("reg133", 133),
          ("reg134", 134),
          ("reg135", 135),
          ("reg136", 136),
          ("reg137", 137),
          ("reg138", 138),
          ("reg139", 139),
          ("reg140", 140),
          ("reg141", 141),
          ("reg142", 142),
          ("reg143", 143),
          ("reg144", 144),
          ("reg145", 145),
          ("reg146", 146),
          ("reg147", 147),
          ("reg148", 148),
          ("reg149", 149),
          ("reg150", 150),
          ("reg151", 151),
          ("reg152", 152),
          ("reg153", 153),
          ("reg154", 154),
          ("reg155", 155),
          ("reg156", 156),
          ("reg157", 157),
          ("reg158", 158),
          ("reg159", 159),
          ("reg160", 160),
          ("reg161", 161),
          ("reg162", 162),
          ("reg163", 163),
          ("reg164", 164),
          ("reg165", 165),
          ("reg166", 166),
          ("reg167", 167),
          ("reg168", 168),
          ("reg169", 169),
          ("reg170", 170),
          ("reg171", 171),
          ("reg172", 172),
          ("reg173", 173),
          ("reg174", 174),
          ("reg175", 175),
          ("reg176", 176),
          ("reg177", 177),
          ("reg178", 178),
          ("reg179", 179),
          ("reg180", 180),
          ("reg181", 181),
          ("reg182", 182),
          ("reg183", 183),
          ("reg184", 184),
          ("reg185", 185),
          ("reg186", 186),
          ("reg187", 187),
          ("reg188", 188),
          ("reg189", 189),
          ("reg190", 190),
          ("reg191", 191),
          ("reg192", 192),
          ("reg193", 193),
          ("reg194", 194),
          ("reg195", 195),
          ("reg196", 196),
          ("reg197", 197),
          ("reg198", 198),
          ("reg199", 199),
          ("reg200", 200),
          ("reg201", 201),
          ("reg202", 202),
          ("reg203", 203),
          ("reg204", 204),
          ("reg205", 205),
          ("reg206", 206),
          ("reg207", 207),
          ("reg208", 208),
          ("reg209", 209),
          ("reg210", 210),
          ("reg211", 211),
          ("reg212", 212),
          ("reg213", 213),
          ("reg214", 214),
          ("reg215", 215),
          ("reg216", 216),
          ("reg217", 217),
          ("reg218", 218),
          ("reg219", 219),
          ("reg220", 220),
          ("reg221", 221),
          ("reg222", 222),
          ("reg223", 223),
          ("reg224", 224),
          ("reg225", 225),
          ("reg226", 226),
          ("reg227", 227),
          ("reg228", 228),
          ("reg229", 229),
          ("reg230", 230),
          ("reg231", 231),
          ("reg232", 232),
          ("reg233", 233),
          ("reg234", 234),
          ("reg235", 235),
          ("reg236", 236),
          ("reg237", 237),
          ("reg238", 238),
          ("reg239", 239),
          ("reg240", 240),
          ("reg241", 241),
          ("reg242", 242),
          ("reg243", 243),
          ("reg244", 244),
          ("reg245", 245),
          ("reg246", 246),
          ("reg247", 247),
          ("reg248", 248),
          ("reg249", 249),
          ("reg250", 250),
          ("reg251", 251),
          ("reg252", 252),
          ("reg253", 253),
          ("reg254", 254),
          ("reg255", 255))
    )


_RegulatoryBand_Type.__name__ = "Integer32"
_RegulatoryBand_Object = MibScalar
regulatoryBand = _RegulatoryBand_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 1),
    _RegulatoryBand_Type()
)
regulatoryBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regulatoryBand.setStatus("current")


class _ProductVariant_Type(Integer32):
    """Custom type productVariant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("pTPxx400Full", 0),
          ("pTPxx400Deprecated1", 1),
          ("pTPxx400Deprecated2", 2),
          ("pTPxx400Lite", 3),
          ("spare1", 4),
          ("pTPxx300", 5),
          ("spare2", 6),
          ("spare3", 7),
          ("pTPxx500FullDeprecated", 8),
          ("pTPxx500LiteDeprecated", 9),
          ("pTPxx500", 10),
          ("pTPxx600Lite", 11),
          ("pTPxx600Full", 12),
          ("pTPxx650", 13),
          ("pMP455", 14),
          ("pTP800", 15),
          ("pMPMedusa", 16),
          ("pTPxx700", 17),
          ("pTP50670", 18),
          ("pTP50670ATEX", 19),
          ("pTP48670", 20))
    )


_ProductVariant_Type.__name__ = "Integer32"
_ProductVariant_Object = MibScalar
productVariant = _ProductVariant_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 2),
    _ProductVariant_Type()
)
productVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVariant.setStatus("current")


class _ProductName_Type(DisplayString):
    """Custom type productName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ProductName_Type.__name__ = "DisplayString"
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 3),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")


class _FrequencyVariant_Type(Integer32):
    """Custom type frequencyVariant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freq50XXX", 0),
          ("freq45XXX", 1),
          ("freq48XXX", 2))
    )


_FrequencyVariant_Type.__name__ = "Integer32"
_FrequencyVariant_Object = MibScalar
frequencyVariant = _FrequencyVariant_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 5),
    _FrequencyVariant_Type()
)
frequencyVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequencyVariant.setStatus("current")


class _SNMPv3Enable_Type(Integer32):
    """Custom type sNMPv3Enable based on Integer32"""
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


_SNMPv3Enable_Type.__name__ = "Integer32"
_SNMPv3Enable_Object = MibScalar
sNMPv3Enable = _SNMPv3Enable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 9),
    _SNMPv3Enable_Type()
)
sNMPv3Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPv3Enable.setStatus("current")


class _LicenseVersion_Type(Integer32):
    """Custom type licenseVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_LicenseVersion_Type.__name__ = "Integer32"
_LicenseVersion_Object = MibScalar
licenseVersion = _LicenseVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 12),
    _LicenseVersion_Type()
)
licenseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseVersion.setStatus("current")


class _LicenseUnitSerialNumber_Type(DisplayString):
    """Custom type licenseUnitSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_LicenseUnitSerialNumber_Type.__name__ = "DisplayString"
_LicenseUnitSerialNumber_Object = MibScalar
licenseUnitSerialNumber = _LicenseUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 13),
    _LicenseUnitSerialNumber_Type()
)
licenseUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseUnitSerialNumber.setStatus("current")


class _LicenseIssueNumber_Type(Integer32):
    """Custom type licenseIssueNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LicenseIssueNumber_Type.__name__ = "Integer32"
_LicenseIssueNumber_Object = MibScalar
licenseIssueNumber = _LicenseIssueNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 15),
    _LicenseIssueNumber_Type()
)
licenseIssueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseIssueNumber.setStatus("current")


class _LicenseCountry_Type(DisplayString):
    """Custom type licenseCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 103),
    )


_LicenseCountry_Type.__name__ = "DisplayString"
_LicenseCountry_Object = MibScalar
licenseCountry = _LicenseCountry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 16),
    _LicenseCountry_Type()
)
licenseCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseCountry.setStatus("current")


class _LicenseNumberOfRegulatoryBands_Type(Integer32):
    """Custom type licenseNumberOfRegulatoryBands based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_LicenseNumberOfRegulatoryBands_Type.__name__ = "Integer32"
_LicenseNumberOfRegulatoryBands_Object = MibScalar
licenseNumberOfRegulatoryBands = _LicenseNumberOfRegulatoryBands_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 17),
    _LicenseNumberOfRegulatoryBands_Type()
)
licenseNumberOfRegulatoryBands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseNumberOfRegulatoryBands.setStatus("current")
_LicenseRegulatoryBandsTable_Object = MibTable
licenseRegulatoryBandsTable = _LicenseRegulatoryBandsTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 18)
)
if mibBuilder.loadTexts:
    licenseRegulatoryBandsTable.setStatus("current")
_LicenseRegulatoryBandsTableEntry_Object = MibTableRow
licenseRegulatoryBandsTableEntry = _LicenseRegulatoryBandsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 18, 1)
)
licenseRegulatoryBandsTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "licenseRegulatoryBandsTableIndex"),
)
if mibBuilder.loadTexts:
    licenseRegulatoryBandsTableEntry.setStatus("current")


class _LicenseRegulatoryBandsTableIndex_Type(Integer32):
    """Custom type licenseRegulatoryBandsTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LicenseRegulatoryBandsTableIndex_Type.__name__ = "Integer32"
_LicenseRegulatoryBandsTableIndex_Object = MibTableColumn
licenseRegulatoryBandsTableIndex = _LicenseRegulatoryBandsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 18, 1, 1),
    _LicenseRegulatoryBandsTableIndex_Type()
)
licenseRegulatoryBandsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    licenseRegulatoryBandsTableIndex.setStatus("current")


class _LicenseRegulatoryBandsList_Type(Integer32):
    """Custom type licenseRegulatoryBandsList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("regInvalid", 0),
          ("reg158GHz", 1),
          ("reg258GHz", 2),
          ("reg358GHz", 3),
          ("reg458GHzWithRTTT", 4),
          ("reg558GHz", 5),
          ("reg658GHz", 6),
          ("reg754GHz", 7),
          ("reg854GHz", 8),
          ("reg954GHz", 9),
          ("reg1058GHz", 10),
          ("reg1158GHz", 11),
          ("reg1254GHz", 12),
          ("reg1354GHz", 13),
          ("reg1449GHzPublicSafety", 14),
          ("reg15", 15),
          ("reg1659GHz", 16),
          ("reg1759GHz", 17),
          ("reg1849GHzPublicSafety", 18),
          ("reg1958GHz", 19),
          ("reg2054GHz", 20),
          ("reg2154GHz", 21),
          ("reg2258GHz", 22),
          ("reg23", 23),
          ("reg2458GHz", 24),
          ("reg2558GHz", 25),
          ("reg2654GHz", 26),
          ("reg2758GHz", 27),
          ("reg2858GHz", 28),
          ("reg2958GHz", 29),
          ("reg3054GHz", 30),
          ("reg3158GHz", 31),
          ("reg3249GHzLicensed", 32),
          ("reg3349GHzETSIBroadbandDisasterRelief", 33),
          ("reg3458GHz", 34),
          ("reg3558GHz", 35),
          ("reg3654GHz", 36),
          ("reg3758GHz", 37),
          ("reg3852GHz", 38),
          ("reg3951GHzETSIBroadbandDisasterRelief", 39),
          ("reg4054GHz", 40),
          ("reg4154GHz", 41),
          ("reg4254GHz", 42),
          ("reg4354GHz", 43),
          ("reg4458GHz", 44),
          ("reg4558GHz", 45),
          ("reg4658GHz", 46),
          ("reg4758GHz", 47),
          ("reg4858GHz", 48),
          ("reg4958GHz", 49),
          ("reg5058GHz", 50),
          ("reg5158GHz", 51),
          ("reg5258GHz", 52),
          ("reg5358GHz", 53),
          ("reg5458GHz", 54),
          ("reg5558GHz", 55),
          ("reg5654GHz", 56),
          ("reg5754GHz", 57),
          ("reg5858GHz", 58),
          ("reg5958GHz", 59),
          ("reg6058GHz", 60),
          ("reg6149GHz", 61),
          ("reg6251GHz52GHz", 62),
          ("reg6352GHz", 63),
          ("reg6451GHz", 64),
          ("reg6551GHz", 65),
          ("reg6651GHz", 66),
          ("reg6752GHz", 67),
          ("reg6852GHz", 68),
          ("reg6952GHz", 69),
          ("reg7052GHz", 70),
          ("reg7152GHz", 71),
          ("reg7252GHz", 72),
          ("reg7352GHz", 73),
          ("reg7452GHz", 74),
          ("reg7552GHz", 75),
          ("reg7652GHz", 76),
          ("reg7752GHz", 77),
          ("reg7849GHz", 78),
          ("reg7954GHz", 79),
          ("reg8049GHz", 80),
          ("reg8147GHz", 81),
          ("reg8247GHz", 82),
          ("reg8352GHz", 83),
          ("reg8451GHz", 84),
          ("reg8551GHz52GHz", 85),
          ("reg8652GHz54GHz", 86),
          ("reg8758GHz", 87),
          ("reg8849GHz", 88),
          ("reg8949GHz", 89),
          ("reg9054GHzParabolicantenna", 90),
          ("reg9152GHzParabolicantenna", 91),
          ("reg9251GHzParabolicantenna", 92),
          ("reg9349GHz", 93),
          ("reg9449GHz", 94),
          ("reg9545GHz", 95),
          ("reg9648GHz", 96),
          ("reg9752GHz", 97),
          ("reg9849GHz27dBiantenna", 98),
          ("reg9949GHz29dBiantenna", 99),
          ("reg10048GHz", 100),
          ("reg10158GHz", 101),
          ("reg102", 102),
          ("reg103", 103),
          ("reg10458GHzNoRTTT", 104),
          ("reg105", 105),
          ("reg106", 106),
          ("reg107", 107),
          ("reg108", 108),
          ("reg109", 109),
          ("reg110", 110),
          ("reg111", 111),
          ("reg112", 112),
          ("reg113", 113),
          ("reg114", 114),
          ("reg115", 115),
          ("reg116", 116),
          ("reg117", 117),
          ("reg118", 118),
          ("reg119", 119),
          ("reg120", 120),
          ("reg121", 121),
          ("reg122", 122),
          ("reg123", 123),
          ("reg124", 124),
          ("reg125", 125),
          ("reg126", 126),
          ("reg127", 127),
          ("reg128", 128),
          ("reg129", 129),
          ("reg130", 130),
          ("reg131", 131),
          ("reg132", 132),
          ("reg133", 133),
          ("reg134", 134),
          ("reg135", 135),
          ("reg136", 136),
          ("reg137", 137),
          ("reg138", 138),
          ("reg139", 139),
          ("reg140", 140),
          ("reg141", 141),
          ("reg142", 142),
          ("reg143", 143),
          ("reg144", 144),
          ("reg145", 145),
          ("reg146", 146),
          ("reg147", 147),
          ("reg148", 148),
          ("reg149", 149),
          ("reg150", 150),
          ("reg151", 151),
          ("reg152", 152),
          ("reg153", 153),
          ("reg154", 154),
          ("reg155", 155),
          ("reg156", 156),
          ("reg157", 157),
          ("reg158", 158),
          ("reg159", 159),
          ("reg160", 160),
          ("reg161", 161),
          ("reg162", 162),
          ("reg163", 163),
          ("reg164", 164),
          ("reg165", 165),
          ("reg166", 166),
          ("reg167", 167),
          ("reg168", 168),
          ("reg169", 169),
          ("reg170", 170),
          ("reg171", 171),
          ("reg172", 172),
          ("reg173", 173),
          ("reg174", 174),
          ("reg175", 175),
          ("reg176", 176),
          ("reg177", 177),
          ("reg178", 178),
          ("reg179", 179),
          ("reg180", 180),
          ("reg181", 181),
          ("reg182", 182),
          ("reg183", 183),
          ("reg184", 184),
          ("reg185", 185),
          ("reg186", 186),
          ("reg187", 187),
          ("reg188", 188),
          ("reg189", 189),
          ("reg190", 190),
          ("reg191", 191),
          ("reg192", 192),
          ("reg193", 193),
          ("reg194", 194),
          ("reg195", 195),
          ("reg196", 196),
          ("reg197", 197),
          ("reg198", 198),
          ("reg199", 199),
          ("reg200", 200),
          ("reg201", 201),
          ("reg202", 202),
          ("reg203", 203),
          ("reg204", 204),
          ("reg205", 205),
          ("reg206", 206),
          ("reg207", 207),
          ("reg208", 208),
          ("reg209", 209),
          ("reg210", 210),
          ("reg211", 211),
          ("reg212", 212),
          ("reg213", 213),
          ("reg214", 214),
          ("reg215", 215),
          ("reg216", 216),
          ("reg217", 217),
          ("reg218", 218),
          ("reg219", 219),
          ("reg220", 220),
          ("reg221", 221),
          ("reg222", 222),
          ("reg223", 223),
          ("reg224", 224),
          ("reg225", 225),
          ("reg226", 226),
          ("reg227", 227),
          ("reg228", 228),
          ("reg229", 229),
          ("reg230", 230),
          ("reg231", 231),
          ("reg232", 232),
          ("reg233", 233),
          ("reg234", 234),
          ("reg235", 235),
          ("reg236", 236),
          ("reg237", 237),
          ("reg238", 238),
          ("reg239", 239),
          ("reg240", 240),
          ("reg241", 241),
          ("reg242", 242),
          ("reg243", 243),
          ("reg244", 244),
          ("reg245", 245),
          ("reg246", 246),
          ("reg247", 247),
          ("reg248", 248),
          ("reg249", 249),
          ("reg250", 250),
          ("reg251", 251),
          ("reg252", 252),
          ("reg253", 253),
          ("reg254", 254),
          ("reg255", 255))
    )


_LicenseRegulatoryBandsList_Type.__name__ = "Integer32"
_LicenseRegulatoryBandsList_Object = MibTableColumn
licenseRegulatoryBandsList = _LicenseRegulatoryBandsList_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 18, 1, 2),
    _LicenseRegulatoryBandsList_Type()
)
licenseRegulatoryBandsList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseRegulatoryBandsList.setStatus("current")


class _LicenseBandwidthCap_Type(Integer32):
    """Custom type licenseBandwidthCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LicenseBandwidthCap_Type.__name__ = "Integer32"
_LicenseBandwidthCap_Object = MibScalar
licenseBandwidthCap = _LicenseBandwidthCap_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 20),
    _LicenseBandwidthCap_Type()
)
licenseBandwidthCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseBandwidthCap.setStatus("current")


class _LicenseEncryption_Type(Integer32):
    """Custom type licenseEncryption based on Integer32"""
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
          ("aES128bit", 1),
          ("aES192bit", 2),
          ("aES256bit", 3))
    )


_LicenseEncryption_Type.__name__ = "Integer32"
_LicenseEncryption_Object = MibScalar
licenseEncryption = _LicenseEncryption_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 21),
    _LicenseEncryption_Type()
)
licenseEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseEncryption.setStatus("current")


class _LicenseSecurityLevel_Type(Integer32):
    """Custom type licenseSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("fIPS", 1),
          ("uCAPL", 2))
    )


_LicenseSecurityLevel_Type.__name__ = "Integer32"
_LicenseSecurityLevel_Object = MibScalar
licenseSecurityLevel = _LicenseSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 22),
    _LicenseSecurityLevel_Type()
)
licenseSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseSecurityLevel.setStatus("current")


class _LicenseGroupAccess_Type(Integer32):
    """Custom type licenseGroupAccess based on Integer32"""
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


_LicenseGroupAccess_Type.__name__ = "Integer32"
_LicenseGroupAccess_Object = MibScalar
licenseGroupAccess = _LicenseGroupAccess_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 23),
    _LicenseGroupAccess_Type()
)
licenseGroupAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseGroupAccess.setStatus("current")


class _LicenseOOBManagementSupport_Type(Integer32):
    """Custom type licenseOOBManagementSupport based on Integer32"""
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


_LicenseOOBManagementSupport_Type.__name__ = "Integer32"
_LicenseOOBManagementSupport_Object = MibScalar
licenseOOBManagementSupport = _LicenseOOBManagementSupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 24),
    _LicenseOOBManagementSupport_Type()
)
licenseOOBManagementSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseOOBManagementSupport.setStatus("current")


class _LicenseSFPPortSupport_Type(Integer32):
    """Custom type licenseSFPPortSupport based on Integer32"""
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


_LicenseSFPPortSupport_Type.__name__ = "Integer32"
_LicenseSFPPortSupport_Object = MibScalar
licenseSFPPortSupport = _LicenseSFPPortSupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 25),
    _LicenseSFPPortSupport_Type()
)
licenseSFPPortSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseSFPPortSupport.setStatus("current")


class _LicenseAuxiliaryPortSupport_Type(Integer32):
    """Custom type licenseAuxiliaryPortSupport based on Integer32"""
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


_LicenseAuxiliaryPortSupport_Type.__name__ = "Integer32"
_LicenseAuxiliaryPortSupport_Object = MibScalar
licenseAuxiliaryPortSupport = _LicenseAuxiliaryPortSupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 26),
    _LicenseAuxiliaryPortSupport_Type()
)
licenseAuxiliaryPortSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseAuxiliaryPortSupport.setStatus("current")


class _LicenseCapacity_Type(Integer32):
    """Custom type licenseCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 0),
          ("mid", 1),
          ("lite", 2))
    )


_LicenseCapacity_Type.__name__ = "Integer32"
_LicenseCapacity_Object = MibScalar
licenseCapacity = _LicenseCapacity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 27),
    _LicenseCapacity_Type()
)
licenseCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseCapacity.setStatus("current")


class _LicenseMaxNumberOfTDMChannels_Type(Integer32):
    """Custom type licenseMaxNumberOfTDMChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_LicenseMaxNumberOfTDMChannels_Type.__name__ = "Integer32"
_LicenseMaxNumberOfTDMChannels_Object = MibScalar
licenseMaxNumberOfTDMChannels = _LicenseMaxNumberOfTDMChannels_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 28),
    _LicenseMaxNumberOfTDMChannels_Type()
)
licenseMaxNumberOfTDMChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseMaxNumberOfTDMChannels.setStatus("current")


class _LicenseIEEE1588Support_Type(Integer32):
    """Custom type licenseIEEE1588Support based on Integer32"""
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


_LicenseIEEE1588Support_Type.__name__ = "Integer32"
_LicenseIEEE1588Support_Object = MibScalar
licenseIEEE1588Support = _LicenseIEEE1588Support_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 29),
    _LicenseIEEE1588Support_Type()
)
licenseIEEE1588Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseIEEE1588Support.setStatus("current")


class _LicenseSyncESupport_Type(Integer32):
    """Custom type licenseSyncESupport based on Integer32"""
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


_LicenseSyncESupport_Type.__name__ = "Integer32"
_LicenseSyncESupport_Object = MibScalar
licenseSyncESupport = _LicenseSyncESupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 30),
    _LicenseSyncESupport_Type()
)
licenseSyncESupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseSyncESupport.setStatus("current")


class _LicenseIPv6Support_Type(Integer32):
    """Custom type licenseIPv6Support based on Integer32"""
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


_LicenseIPv6Support_Type.__name__ = "Integer32"
_LicenseIPv6Support_Object = MibScalar
licenseIPv6Support = _LicenseIPv6Support_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 31),
    _LicenseIPv6Support_Type()
)
licenseIPv6Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseIPv6Support.setStatus("current")


class _LicenseMinimumFirmwareVersion_Type(DisplayString):
    """Custom type licenseMinimumFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_LicenseMinimumFirmwareVersion_Type.__name__ = "DisplayString"
_LicenseMinimumFirmwareVersion_Object = MibScalar
licenseMinimumFirmwareVersion = _LicenseMinimumFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 32),
    _LicenseMinimumFirmwareVersion_Type()
)
licenseMinimumFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseMinimumFirmwareVersion.setStatus("current")


class _LicenseFullCapabilityTrialStatus_Type(Integer32):
    """Custom type licenseFullCapabilityTrialStatus based on Integer32"""
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
        *(("available", 0),
          ("active", 1),
          ("inactive", 2),
          ("expired", 3),
          ("unavailable", 4))
    )


_LicenseFullCapabilityTrialStatus_Type.__name__ = "Integer32"
_LicenseFullCapabilityTrialStatus_Object = MibScalar
licenseFullCapabilityTrialStatus = _LicenseFullCapabilityTrialStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 33),
    _LicenseFullCapabilityTrialStatus_Type()
)
licenseFullCapabilityTrialStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseFullCapabilityTrialStatus.setStatus("current")


class _LicenseRemainingTrialPeriod_Type(Integer32):
    """Custom type licenseRemainingTrialPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_LicenseRemainingTrialPeriod_Type.__name__ = "Integer32"
_LicenseRemainingTrialPeriod_Object = MibScalar
licenseRemainingTrialPeriod = _LicenseRemainingTrialPeriod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 34),
    _LicenseRemainingTrialPeriod_Type()
)
licenseRemainingTrialPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseRemainingTrialPeriod.setStatus("current")


class _LicenseRemainingTrialPeriodAlarm_Type(Integer32):
    """Custom type licenseRemainingTrialPeriodAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("fullCapabilityTrialNotActiveOrMoreThan7DaysRemaining", 0),
          ("fullCapabilityTrialExpiringInLessThan7Days", 1),
          ("fullCapabilityTrialExpiringInLessThan6Days", 2),
          ("fullCapabilityTrialExpiringInLessThan5Days", 3),
          ("fullCapabilityTrialExpiringInLessThan4Days", 4),
          ("fullCapabilityTrialExpiringInLessThan3Days", 5),
          ("fullCapabilityTrialExpiringInLessThan2Days", 6),
          ("fullCapabilityTrialExpiringInLessThan1Day", 7),
          ("fullCapabilityTrialHasExpired", 8))
    )


_LicenseRemainingTrialPeriodAlarm_Type.__name__ = "Integer32"
_LicenseRemainingTrialPeriodAlarm_Object = MibScalar
licenseRemainingTrialPeriodAlarm = _LicenseRemainingTrialPeriodAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 35),
    _LicenseRemainingTrialPeriodAlarm_Type()
)
licenseRemainingTrialPeriodAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseRemainingTrialPeriodAlarm.setStatus("current")


class _CapacityVariantMismatchLinked_Type(Integer32):
    """Custom type capacityVariantMismatchLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("mismatchDetected", 1))
    )


_CapacityVariantMismatchLinked_Type.__name__ = "Integer32"
_CapacityVariantMismatchLinked_Object = MibScalar
capacityVariantMismatchLinked = _CapacityVariantMismatchLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 36),
    _CapacityVariantMismatchLinked_Type()
)
capacityVariantMismatchLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capacityVariantMismatchLinked.setStatus("current")


class _LicenseTDDSyncSupport_Type(Integer32):
    """Custom type licenseTDDSyncSupport based on Integer32"""
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


_LicenseTDDSyncSupport_Type.__name__ = "Integer32"
_LicenseTDDSyncSupport_Object = MibScalar
licenseTDDSyncSupport = _LicenseTDDSyncSupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 37),
    _LicenseTDDSyncSupport_Type()
)
licenseTDDSyncSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseTDDSyncSupport.setStatus("current")


class _LicenseMaxLinkRange_Type(Integer32):
    """Custom type licenseMaxLinkRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2499),
    )


_LicenseMaxLinkRange_Type.__name__ = "Integer32"
_LicenseMaxLinkRange_Object = MibScalar
licenseMaxLinkRange = _LicenseMaxLinkRange_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 38),
    _LicenseMaxLinkRange_Type()
)
licenseMaxLinkRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseMaxLinkRange.setStatus("current")


class _LicenseTrialPeriod_Type(Integer32):
    """Custom type licenseTrialPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_LicenseTrialPeriod_Type.__name__ = "Integer32"
_LicenseTrialPeriod_Object = MibScalar
licenseTrialPeriod = _LicenseTrialPeriod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 39),
    _LicenseTrialPeriod_Type()
)
licenseTrialPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseTrialPeriod.setStatus("current")


class _LicenseRARSupport_Type(Integer32):
    """Custom type licenseRARSupport based on Integer32"""
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
        *(("disabled", 0),
          ("mAB", 1),
          ("dLEP", 2),
          ("mABandDLEP", 3))
    )


_LicenseRARSupport_Type.__name__ = "Integer32"
_LicenseRARSupport_Object = MibScalar
licenseRARSupport = _LicenseRARSupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 40),
    _LicenseRARSupport_Type()
)
licenseRARSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseRARSupport.setStatus("current")


class _LicenseGasGroup_Type(Integer32):
    """Custom type licenseGasGroup based on Integer32"""
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
        *(("nonHAZLOCUnit", 0),
          ("gasGroupA", 1),
          ("gasGroupB", 2),
          ("gasGroupC", 3),
          ("gasGroupD", 4))
    )


_LicenseGasGroup_Type.__name__ = "Integer32"
_LicenseGasGroup_Object = MibScalar
licenseGasGroup = _LicenseGasGroup_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 41),
    _LicenseGasGroup_Type()
)
licenseGasGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseGasGroup.setStatus("current")


class _LicenseLongMinimumFirmwareVersion_Type(DisplayString):
    """Custom type licenseLongMinimumFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LicenseLongMinimumFirmwareVersion_Type.__name__ = "DisplayString"
_LicenseLongMinimumFirmwareVersion_Object = MibScalar
licenseLongMinimumFirmwareVersion = _LicenseLongMinimumFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 42),
    _LicenseLongMinimumFirmwareVersion_Type()
)
licenseLongMinimumFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseLongMinimumFirmwareVersion.setStatus("current")


class _LicenseHCMPSupport_Type(Integer32):
    """Custom type licenseHCMPSupport based on Integer32"""
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
        *(("disabled", 0),
          ("slaveEnabled", 1),
          ("masterEnabled", 2),
          ("masterandSlaveEnabled", 3))
    )


_LicenseHCMPSupport_Type.__name__ = "Integer32"
_LicenseHCMPSupport_Object = MibScalar
licenseHCMPSupport = _LicenseHCMPSupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 43),
    _LicenseHCMPSupport_Type()
)
licenseHCMPSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseHCMPSupport.setStatus("current")


class _LicenseInstancedTableNumber_Type(Integer32):
    """Custom type licenseInstancedTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_LicenseInstancedTableNumber_Type.__name__ = "Integer32"
_LicenseInstancedTableNumber_Object = MibScalar
licenseInstancedTableNumber = _LicenseInstancedTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 44),
    _LicenseInstancedTableNumber_Type()
)
licenseInstancedTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseInstancedTableNumber.setStatus("current")
_LicenseInstancedTable_Object = MibTable
licenseInstancedTable = _LicenseInstancedTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 45)
)
if mibBuilder.loadTexts:
    licenseInstancedTable.setStatus("current")
_LicenseInstancedTableEntry_Object = MibTableRow
licenseInstancedTableEntry = _LicenseInstancedTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 45, 1)
)
licenseInstancedTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "licenseInstancedTableIndex"),
)
if mibBuilder.loadTexts:
    licenseInstancedTableEntry.setStatus("current")


class _LicenseInstancedTableIndex_Type(Integer32):
    """Custom type licenseInstancedTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_LicenseInstancedTableIndex_Type.__name__ = "Integer32"
_LicenseInstancedTableIndex_Object = MibTableColumn
licenseInstancedTableIndex = _LicenseInstancedTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 45, 1, 1),
    _LicenseInstancedTableIndex_Type()
)
licenseInstancedTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    licenseInstancedTableIndex.setStatus("current")


class _CapacityVariantMismatch_Type(Integer32):
    """Custom type capacityVariantMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("mismatchDetected", 1))
    )


_CapacityVariantMismatch_Type.__name__ = "Integer32"
_CapacityVariantMismatch_Object = MibTableColumn
capacityVariantMismatch = _CapacityVariantMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 45, 1, 2),
    _CapacityVariantMismatch_Type()
)
capacityVariantMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capacityVariantMismatch.setStatus("current")


class _LicenseTLSRekey_Type(Integer32):
    """Custom type licenseTLSRekey based on Integer32"""
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


_LicenseTLSRekey_Type.__name__ = "Integer32"
_LicenseTLSRekey_Object = MibScalar
licenseTLSRekey = _LicenseTLSRekey_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 46),
    _LicenseTLSRekey_Type()
)
licenseTLSRekey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseTLSRekey.setStatus("current")


class _LicenseAdvanceHCMPSupport_Type(Integer32):
    """Custom type licenseAdvanceHCMPSupport based on Integer32"""
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
        *(("disabled", 0),
          ("slaveEnabled", 1),
          ("masterEnabled", 2),
          ("masterandSlaveEnabled", 3))
    )


_LicenseAdvanceHCMPSupport_Type.__name__ = "Integer32"
_LicenseAdvanceHCMPSupport_Object = MibScalar
licenseAdvanceHCMPSupport = _LicenseAdvanceHCMPSupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 47),
    _LicenseAdvanceHCMPSupport_Type()
)
licenseAdvanceHCMPSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseAdvanceHCMPSupport.setStatus("current")


class _LicenseMinFirmwareVersionPTP650Emulation_Type(DisplayString):
    """Custom type licenseMinFirmwareVersionPTP650Emulation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LicenseMinFirmwareVersionPTP650Emulation_Type.__name__ = "DisplayString"
_LicenseMinFirmwareVersionPTP650Emulation_Object = MibScalar
licenseMinFirmwareVersionPTP650Emulation = _LicenseMinFirmwareVersionPTP650Emulation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 8, 48),
    _LicenseMinFirmwareVersionPTP650Emulation_Type()
)
licenseMinFirmwareVersionPTP650Emulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseMinFirmwareVersionPTP650Emulation.setStatus("current")
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9)
)


class _TargetRange_Type(Integer32):
    """Custom type targetRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_TargetRange_Type.__name__ = "Integer32"
_TargetRange_Object = MibScalar
targetRange = _TargetRange_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 1),
    _TargetRange_Type()
)
targetRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetRange.setStatus("current")


class _RangingMode_Type(Integer32):
    """Custom type rangingMode based on Integer32"""
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
        *(("auto0to40km", 0),
          ("auto0to100km", 1),
          ("auto0to200km", 2),
          ("auto0to250km", 3),
          ("targetRange", 4))
    )


_RangingMode_Type.__name__ = "Integer32"
_RangingMode_Object = MibScalar
rangingMode = _RangingMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 2),
    _RangingMode_Type()
)
rangingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rangingMode.setStatus("current")


class _InstallStatusLinked_Type(Integer32):
    """Custom type installStatusLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("wrongPeer", 1))
    )


_InstallStatusLinked_Type.__name__ = "Integer32"
_InstallStatusLinked_Object = MibScalar
installStatusLinked = _InstallStatusLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 3),
    _InstallStatusLinked_Type()
)
installStatusLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installStatusLinked.setStatus("current")


class _InstallArmState_Type(Integer32):
    """Custom type installArmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disarmed", 0),
          ("armed", 1))
    )


_InstallArmState_Type.__name__ = "Integer32"
_InstallArmState_Object = MibScalar
installArmState = _InstallArmState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 4),
    _InstallArmState_Type()
)
installArmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    installArmState.setStatus("current")


class _TFTPServerPortNumber_Type(Integer32):
    """Custom type tFTPServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TFTPServerPortNumber_Type.__name__ = "Integer32"
_TFTPServerPortNumber_Object = MibScalar
tFTPServerPortNumber = _TFTPServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 6),
    _TFTPServerPortNumber_Type()
)
tFTPServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFTPServerPortNumber.setStatus("current")


class _TFTPSoftwareUpgradeFileName_Type(DisplayString):
    """Custom type tFTPSoftwareUpgradeFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TFTPSoftwareUpgradeFileName_Type.__name__ = "DisplayString"
_TFTPSoftwareUpgradeFileName_Object = MibScalar
tFTPSoftwareUpgradeFileName = _TFTPSoftwareUpgradeFileName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 7),
    _TFTPSoftwareUpgradeFileName_Type()
)
tFTPSoftwareUpgradeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFTPSoftwareUpgradeFileName.setStatus("current")
_TFTPStartSoftwareUpgrade_Type = Integer32
_TFTPStartSoftwareUpgrade_Object = MibScalar
tFTPStartSoftwareUpgrade = _TFTPStartSoftwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 8),
    _TFTPStartSoftwareUpgrade_Type()
)
tFTPStartSoftwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFTPStartSoftwareUpgrade.setStatus("current")


class _TFTPSoftwareUpgradeStatus_Type(Integer32):
    """Custom type tFTPSoftwareUpgradeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("uploadinprogress", 1),
          ("uploadsuccessfulprogrammingFLASH", 2),
          ("upgradesuccessfulreboottorunthenewsoftwareimage", 3),
          ("upgradefailed", 4),
          ("upgradewarning", 5))
    )


_TFTPSoftwareUpgradeStatus_Type.__name__ = "Integer32"
_TFTPSoftwareUpgradeStatus_Object = MibScalar
tFTPSoftwareUpgradeStatus = _TFTPSoftwareUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 9),
    _TFTPSoftwareUpgradeStatus_Type()
)
tFTPSoftwareUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFTPSoftwareUpgradeStatus.setStatus("current")


class _TFTPSoftwareUpgradeStatusText_Type(DisplayString):
    """Custom type tFTPSoftwareUpgradeStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TFTPSoftwareUpgradeStatusText_Type.__name__ = "DisplayString"
_TFTPSoftwareUpgradeStatusText_Object = MibScalar
tFTPSoftwareUpgradeStatusText = _TFTPSoftwareUpgradeStatusText_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 10),
    _TFTPSoftwareUpgradeStatusText_Type()
)
tFTPSoftwareUpgradeStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFTPSoftwareUpgradeStatusText.setStatus("current")


class _TFTPSoftwareUpgradeStatusAdditionalText_Type(DisplayString):
    """Custom type tFTPSoftwareUpgradeStatusAdditionalText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TFTPSoftwareUpgradeStatusAdditionalText_Type.__name__ = "DisplayString"
_TFTPSoftwareUpgradeStatusAdditionalText_Object = MibScalar
tFTPSoftwareUpgradeStatusAdditionalText = _TFTPSoftwareUpgradeStatusAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 11),
    _TFTPSoftwareUpgradeStatusAdditionalText_Type()
)
tFTPSoftwareUpgradeStatusAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFTPSoftwareUpgradeStatusAdditionalText.setStatus("current")


class _HTTPAccessEnabled_Type(Integer32):
    """Custom type hTTPAccessEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_HTTPAccessEnabled_Type.__name__ = "Integer32"
_HTTPAccessEnabled_Object = MibScalar
hTTPAccessEnabled = _HTTPAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 12),
    _HTTPAccessEnabled_Type()
)
hTTPAccessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hTTPAccessEnabled.setStatus("current")


class _TelnetAccessEnabled_Type(Integer32):
    """Custom type telnetAccessEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TelnetAccessEnabled_Type.__name__ = "Integer32"
_TelnetAccessEnabled_Object = MibScalar
telnetAccessEnabled = _TelnetAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 13),
    _TelnetAccessEnabled_Type()
)
telnetAccessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetAccessEnabled.setStatus("current")


class _HTTPPortNumber_Type(Integer32):
    """Custom type hTTPPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HTTPPortNumber_Type.__name__ = "Integer32"
_HTTPPortNumber_Object = MibScalar
hTTPPortNumber = _HTTPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 14),
    _HTTPPortNumber_Type()
)
hTTPPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hTTPPortNumber.setStatus("current")


class _HTTPSPortNumber_Type(Integer32):
    """Custom type hTTPSPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HTTPSPortNumber_Type.__name__ = "Integer32"
_HTTPSPortNumber_Object = MibScalar
hTTPSPortNumber = _HTTPSPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 15),
    _HTTPSPortNumber_Type()
)
hTTPSPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hTTPSPortNumber.setStatus("current")


class _TelnetPortNumber_Type(Integer32):
    """Custom type telnetPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TelnetPortNumber_Type.__name__ = "Integer32"
_TelnetPortNumber_Object = MibScalar
telnetPortNumber = _TelnetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 16),
    _TelnetPortNumber_Type()
)
telnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortNumber.setStatus("current")


class _HTTPSAccessEnabled_Type(Integer32):
    """Custom type hTTPSAccessEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_HTTPSAccessEnabled_Type.__name__ = "Integer32"
_HTTPSAccessEnabled_Object = MibScalar
hTTPSAccessEnabled = _HTTPSAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 17),
    _HTTPSAccessEnabled_Type()
)
hTTPSAccessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hTTPSAccessEnabled.setStatus("current")


class _TFTPServerInternetAddressType_Type(Integer32):
    """Custom type tFTPServerInternetAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipv4z", 3),
          ("ipv6z", 4),
          ("unknown6", 5),
          ("unknown7", 6),
          ("unknown8", 7),
          ("unknown9", 8),
          ("unknown10", 9),
          ("unknown11", 10),
          ("unknown12", 11),
          ("unknown13", 12),
          ("unknown14", 13),
          ("unknown15", 14),
          ("unknown16", 15),
          ("dns", 16))
    )


_TFTPServerInternetAddressType_Type.__name__ = "Integer32"
_TFTPServerInternetAddressType_Object = MibScalar
tFTPServerInternetAddressType = _TFTPServerInternetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 18),
    _TFTPServerInternetAddressType_Type()
)
tFTPServerInternetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFTPServerInternetAddressType.setStatus("current")
_TFTPServerInternetAddress_Type = InetAddress
_TFTPServerInternetAddress_Object = MibScalar
tFTPServerInternetAddress = _TFTPServerInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 19),
    _TFTPServerInternetAddress_Type()
)
tFTPServerInternetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFTPServerInternetAddress.setStatus("current")


class _LowestDataModulationMode_Type(Integer32):
    """Custom type lowestDataModulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("modAcquisition", 0),
          ("modBpsk63percent", 1),
          ("modQpsk63percentSingle", 2),
          ("modTransient1", 3),
          ("modQpsk87percentSingle", 4),
          ("modTransient2", 5),
          ("mod16qam63percentSingleA", 6),
          ("modTransient3", 7),
          ("mod16qam87percentSingle", 8),
          ("modTransient4", 9),
          ("mod64qam75percentSingle", 10),
          ("modTransient5", 11),
          ("mod64qam92percentSingle", 12),
          ("modTransient6", 13),
          ("mod256qam81percentSingle", 14),
          ("mod16qam63percentSingleB", 15),
          ("mod16qam63percentDual", 16),
          ("modTransient7", 17),
          ("mod16qam87percentDual", 18),
          ("modTransient8", 19),
          ("mod64qam75percentDual", 20),
          ("modTransient9", 21),
          ("mod64qam92percentDual", 22),
          ("modTransient10", 23),
          ("mod256qam81percentDual", 24))
    )


_LowestDataModulationMode_Type.__name__ = "Integer32"
_LowestDataModulationMode_Object = MibScalar
lowestDataModulationMode = _LowestDataModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 20),
    _LowestDataModulationMode_Type()
)
lowestDataModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowestDataModulationMode.setStatus("current")


class _TFTPClient_Type(Integer32):
    """Custom type tFTPClient based on Integer32"""
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


_TFTPClient_Type.__name__ = "Integer32"
_TFTPClient_Object = MibScalar
tFTPClient = _TFTPClient_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 22),
    _TFTPClient_Type()
)
tFTPClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFTPClient.setStatus("current")


class _MgmtInstancedTableNumber_Type(Integer32):
    """Custom type mgmtInstancedTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MgmtInstancedTableNumber_Type.__name__ = "Integer32"
_MgmtInstancedTableNumber_Object = MibScalar
mgmtInstancedTableNumber = _MgmtInstancedTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 23),
    _MgmtInstancedTableNumber_Type()
)
mgmtInstancedTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtInstancedTableNumber.setStatus("current")
_MgmtInstancedTable_Object = MibTable
mgmtInstancedTable = _MgmtInstancedTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 24)
)
if mibBuilder.loadTexts:
    mgmtInstancedTable.setStatus("current")
_MgmtInstancedTableEntry_Object = MibTableRow
mgmtInstancedTableEntry = _MgmtInstancedTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 24, 1)
)
mgmtInstancedTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "mgmtInstancedTableIndex"),
)
if mibBuilder.loadTexts:
    mgmtInstancedTableEntry.setStatus("current")


class _MgmtInstancedTableIndex_Type(Integer32):
    """Custom type mgmtInstancedTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MgmtInstancedTableIndex_Type.__name__ = "Integer32"
_MgmtInstancedTableIndex_Object = MibTableColumn
mgmtInstancedTableIndex = _MgmtInstancedTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 24, 1, 1),
    _MgmtInstancedTableIndex_Type()
)
mgmtInstancedTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mgmtInstancedTableIndex.setStatus("current")


class _InstallStatus_Type(Integer32):
    """Custom type installStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("wrongPeer", 1))
    )


_InstallStatus_Type.__name__ = "Integer32"
_InstallStatus_Object = MibTableColumn
installStatus = _InstallStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 24, 1, 2),
    _InstallStatus_Type()
)
installStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installStatus.setStatus("current")


class _TFTPServerResolvedInternetAddress_Type(DisplayString):
    """Custom type tFTPServerResolvedInternetAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TFTPServerResolvedInternetAddress_Type.__name__ = "DisplayString"
_TFTPServerResolvedInternetAddress_Object = MibScalar
tFTPServerResolvedInternetAddress = _TFTPServerResolvedInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 25),
    _TFTPServerResolvedInternetAddress_Type()
)
tFTPServerResolvedInternetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFTPServerResolvedInternetAddress.setStatus("current")


class _InstallationMode_Type(Integer32):
    """Custom type installationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("armWithTones", 0),
          ("armWithoutTones", 1),
          ("changeConfigWithoutArming", 2))
    )


_InstallationMode_Type.__name__ = "Integer32"
_InstallationMode_Object = MibScalar
installationMode = _InstallationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 9, 26),
    _InstallationMode_Type()
)
installationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    installationMode.setStatus("current")
_PhyControl_ObjectIdentity = ObjectIdentity
phyControl = _PhyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 10)
)


class _LinkSymmetry_Type(Integer32):
    """Custom type linkSymmetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("symmetryAdaptive", 0),
          ("symmetry2to1", 1),
          ("symmetry1to1", 2),
          ("symmetry1to2", 3),
          ("symmetry3to1", 4),
          ("symmetry1to3", 5),
          ("symmetry5to1", 6),
          ("symmetry1to5", 7))
    )


_LinkSymmetry_Type.__name__ = "Integer32"
_LinkSymmetry_Object = MibScalar
linkSymmetry = _LinkSymmetry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 10, 1),
    _LinkSymmetry_Type()
)
linkSymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSymmetry.setStatus("current")


class _UserConfiguredMaxModulationMode_Type(Integer32):
    """Custom type userConfiguredMaxModulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("modBpsk63percent", 0),
          ("modQpsk63percent", 1),
          ("modQpsk87percent", 2),
          ("mod16qam63percent", 3),
          ("mod16qam87percent", 4),
          ("mod64qam75percent", 5),
          ("mod64qam92percent", 6),
          ("mod256qam81percent", 7))
    )


_UserConfiguredMaxModulationMode_Type.__name__ = "Integer32"
_UserConfiguredMaxModulationMode_Object = MibScalar
userConfiguredMaxModulationMode = _UserConfiguredMaxModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 10, 2),
    _UserConfiguredMaxModulationMode_Type()
)
userConfiguredMaxModulationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userConfiguredMaxModulationMode.setStatus("current")


class _LinkModeOptimization_Type(Integer32):
    """Custom type linkModeOptimization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("iPTraffic", 0),
          ("tDMTraffic", 1))
    )


_LinkModeOptimization_Type.__name__ = "Integer32"
_LinkModeOptimization_Object = MibScalar
linkModeOptimization = _LinkModeOptimization_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 10, 3),
    _LinkModeOptimization_Type()
)
linkModeOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkModeOptimization.setStatus("current")


class _TxColorCode_Type(Integer32):
    """Custom type txColorCode based on Integer32"""
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
        *(("a", 0),
          ("b", 1),
          ("c", 2),
          ("d", 3),
          ("e", 4))
    )


_TxColorCode_Type.__name__ = "Integer32"
_TxColorCode_Object = MibScalar
txColorCode = _TxColorCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 10, 4),
    _TxColorCode_Type()
)
txColorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txColorCode.setStatus("current")


class _RxColorCode_Type(Integer32):
    """Custom type rxColorCode based on Integer32"""
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
        *(("a", 0),
          ("b", 1),
          ("c", 2),
          ("d", 3),
          ("e", 4))
    )


_RxColorCode_Type.__name__ = "Integer32"
_RxColorCode_Object = MibScalar
rxColorCode = _RxColorCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 10, 5),
    _RxColorCode_Type()
)
rxColorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxColorCode.setStatus("current")


class _RemoteMaximumTransmitPowerLinked_Type(Integer32):
    """Custom type remoteMaximumTransmitPowerLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 30),
    )


_RemoteMaximumTransmitPowerLinked_Type.__name__ = "Integer32"
_RemoteMaximumTransmitPowerLinked_Object = MibScalar
remoteMaximumTransmitPowerLinked = _RemoteMaximumTransmitPowerLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 10, 6),
    _RemoteMaximumTransmitPowerLinked_Type()
)
remoteMaximumTransmitPowerLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMaximumTransmitPowerLinked.setStatus("current")


class _PhyControlInstancedTableNumber_Type(Integer32):
    """Custom type phyControlInstancedTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PhyControlInstancedTableNumber_Type.__name__ = "Integer32"
_PhyControlInstancedTableNumber_Object = MibScalar
phyControlInstancedTableNumber = _PhyControlInstancedTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 10, 7),
    _PhyControlInstancedTableNumber_Type()
)
phyControlInstancedTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyControlInstancedTableNumber.setStatus("current")
_PhyControlInstancedTable_Object = MibTable
phyControlInstancedTable = _PhyControlInstancedTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 10, 8)
)
if mibBuilder.loadTexts:
    phyControlInstancedTable.setStatus("current")
_PhyControlInstancedTableEntry_Object = MibTableRow
phyControlInstancedTableEntry = _PhyControlInstancedTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 10, 8, 1)
)
phyControlInstancedTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "phyControlInstancedTableIndex"),
)
if mibBuilder.loadTexts:
    phyControlInstancedTableEntry.setStatus("current")


class _PhyControlInstancedTableIndex_Type(Integer32):
    """Custom type phyControlInstancedTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PhyControlInstancedTableIndex_Type.__name__ = "Integer32"
_PhyControlInstancedTableIndex_Object = MibTableColumn
phyControlInstancedTableIndex = _PhyControlInstancedTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 10, 8, 1, 1),
    _PhyControlInstancedTableIndex_Type()
)
phyControlInstancedTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    phyControlInstancedTableIndex.setStatus("current")


class _RemoteMaximumTransmitPower_Type(Integer32):
    """Custom type remoteMaximumTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 30),
    )


_RemoteMaximumTransmitPower_Type.__name__ = "Integer32"
_RemoteMaximumTransmitPower_Object = MibTableColumn
remoteMaximumTransmitPower = _RemoteMaximumTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 10, 8, 1, 2),
    _RemoteMaximumTransmitPower_Type()
)
remoteMaximumTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMaximumTransmitPower.setStatus("current")
_PhyStatus_ObjectIdentity = ObjectIdentity
phyStatus = _PhyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12)
)


class _LinkLossLinked_Type(Integer32):
    """Custom type linkLossLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_LinkLossLinked_Type.__name__ = "Integer32"
_LinkLossLinked_Object = MibScalar
linkLossLinked = _LinkLossLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 1),
    _LinkLossLinked_Type()
)
linkLossLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLossLinked.setStatus("current")
_ReceivePowerLinked_Type = Integer32
_ReceivePowerLinked_Object = MibScalar
receivePowerLinked = _ReceivePowerLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 2),
    _ReceivePowerLinked_Type()
)
receivePowerLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivePowerLinked.setStatus("current")
_VectorErrorLinked_Type = Integer32
_VectorErrorLinked_Object = MibScalar
vectorErrorLinked = _VectorErrorLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 3),
    _VectorErrorLinked_Type()
)
vectorErrorLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vectorErrorLinked.setStatus("current")
_TransmitPowerLinked_Type = Integer32
_TransmitPowerLinked_Object = MibScalar
transmitPowerLinked = _TransmitPowerLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 4),
    _TransmitPowerLinked_Type()
)
transmitPowerLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitPowerLinked.setStatus("current")


class _ReceiveChannel_Type(Integer32):
    """Custom type receiveChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 305),
    )


_ReceiveChannel_Type.__name__ = "Integer32"
_ReceiveChannel_Object = MibScalar
receiveChannel = _ReceiveChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 5),
    _ReceiveChannel_Type()
)
receiveChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveChannel.setStatus("current")


class _TransmitChannel_Type(Integer32):
    """Custom type transmitChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 305),
    )


_TransmitChannel_Type.__name__ = "Integer32"
_TransmitChannel_Object = MibScalar
transmitChannel = _TransmitChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 6),
    _TransmitChannel_Type()
)
transmitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitChannel.setStatus("current")


class _ReceiveFreqMHz_Type(Integer32):
    """Custom type receiveFreqMHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6050),
    )


_ReceiveFreqMHz_Type.__name__ = "Integer32"
_ReceiveFreqMHz_Object = MibScalar
receiveFreqMHz = _ReceiveFreqMHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 7),
    _ReceiveFreqMHz_Type()
)
receiveFreqMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveFreqMHz.setStatus("current")


class _TransmitFreqMHz_Type(Integer32):
    """Custom type transmitFreqMHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6050),
    )


_TransmitFreqMHz_Type.__name__ = "Integer32"
_TransmitFreqMHz_Object = MibScalar
transmitFreqMHz = _TransmitFreqMHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 8),
    _TransmitFreqMHz_Type()
)
transmitFreqMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitFreqMHz.setStatus("current")
_SignalStrengthRatioLinked_Type = Integer32
_SignalStrengthRatioLinked_Object = MibScalar
signalStrengthRatioLinked = _SignalStrengthRatioLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 9),
    _SignalStrengthRatioLinked_Type()
)
signalStrengthRatioLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalStrengthRatioLinked.setStatus("current")


class _ReceiveFreqKHz_Type(Integer32):
    """Custom type receiveFreqKHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6050000),
    )


_ReceiveFreqKHz_Type.__name__ = "Integer32"
_ReceiveFreqKHz_Object = MibScalar
receiveFreqKHz = _ReceiveFreqKHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 10),
    _ReceiveFreqKHz_Type()
)
receiveFreqKHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveFreqKHz.setStatus("current")


class _TransmitFreqKHz_Type(Integer32):
    """Custom type transmitFreqKHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6050000),
    )


_TransmitFreqKHz_Type.__name__ = "Integer32"
_TransmitFreqKHz_Object = MibScalar
transmitFreqKHz = _TransmitFreqKHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 11),
    _TransmitFreqKHz_Type()
)
transmitFreqKHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitFreqKHz.setStatus("current")
_RawReceivePowerLinked_Type = Integer32
_RawReceivePowerLinked_Object = MibScalar
rawReceivePowerLinked = _RawReceivePowerLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 12),
    _RawReceivePowerLinked_Type()
)
rawReceivePowerLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawReceivePowerLinked.setStatus("current")
_RangeLinked_Type = Integer32
_RangeLinked_Object = MibScalar
rangeLinked = _RangeLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 13),
    _RangeLinked_Type()
)
rangeLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rangeLinked.setStatus("current")


class _ReceiveModulationModeLinked_Type(Integer32):
    """Custom type receiveModulationModeLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_ReceiveModulationModeLinked_Type.__name__ = "Integer32"
_ReceiveModulationModeLinked_Object = MibScalar
receiveModulationModeLinked = _ReceiveModulationModeLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 14),
    _ReceiveModulationModeLinked_Type()
)
receiveModulationModeLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveModulationModeLinked.setStatus("current")


class _TransmitModulationModeLinked_Type(Integer32):
    """Custom type transmitModulationModeLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_TransmitModulationModeLinked_Type.__name__ = "Integer32"
_TransmitModulationModeLinked_Object = MibScalar
transmitModulationModeLinked = _TransmitModulationModeLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 15),
    _TransmitModulationModeLinked_Type()
)
transmitModulationModeLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitModulationModeLinked.setStatus("current")


class _SearchStateLinked_Type(Integer32):
    """Custom type searchStateLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("registering", 0),
          ("searching", 1),
          ("acquiring", 2))
    )


_SearchStateLinked_Type.__name__ = "Integer32"
_SearchStateLinked_Object = MibScalar
searchStateLinked = _SearchStateLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 16),
    _SearchStateLinked_Type()
)
searchStateLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    searchStateLinked.setStatus("current")


class _RemoteMACAddressLinked_Type(OctetString):
    """Custom type remoteMACAddressLinked based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RemoteMACAddressLinked_Type.__name__ = "OctetString"
_RemoteMACAddressLinked_Object = MibScalar
remoteMACAddressLinked = _RemoteMACAddressLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 17),
    _RemoteMACAddressLinked_Type()
)
remoteMACAddressLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMACAddressLinked.setStatus("current")


class _PhyInstancedStatusTableNumber_Type(Integer32):
    """Custom type phyInstancedStatusTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PhyInstancedStatusTableNumber_Type.__name__ = "Integer32"
_PhyInstancedStatusTableNumber_Object = MibScalar
phyInstancedStatusTableNumber = _PhyInstancedStatusTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 18),
    _PhyInstancedStatusTableNumber_Type()
)
phyInstancedStatusTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyInstancedStatusTableNumber.setStatus("current")
_PhyInstancedStatusTable_Object = MibTable
phyInstancedStatusTable = _PhyInstancedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 19)
)
if mibBuilder.loadTexts:
    phyInstancedStatusTable.setStatus("current")
_PhyInstancedStatusTableEntry_Object = MibTableRow
phyInstancedStatusTableEntry = _PhyInstancedStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 19, 1)
)
phyInstancedStatusTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "phyInstancedStatusTableIndex"),
)
if mibBuilder.loadTexts:
    phyInstancedStatusTableEntry.setStatus("current")


class _PhyInstancedStatusTableIndex_Type(Integer32):
    """Custom type phyInstancedStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PhyInstancedStatusTableIndex_Type.__name__ = "Integer32"
_PhyInstancedStatusTableIndex_Object = MibTableColumn
phyInstancedStatusTableIndex = _PhyInstancedStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 19, 1, 1),
    _PhyInstancedStatusTableIndex_Type()
)
phyInstancedStatusTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    phyInstancedStatusTableIndex.setStatus("current")


class _LinkLoss_Type(Integer32):
    """Custom type linkLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_LinkLoss_Type.__name__ = "Integer32"
_LinkLoss_Object = MibTableColumn
linkLoss = _LinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 19, 1, 2),
    _LinkLoss_Type()
)
linkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLoss.setStatus("current")
_ReceivePower_Type = Integer32
_ReceivePower_Object = MibTableColumn
receivePower = _ReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 19, 1, 3),
    _ReceivePower_Type()
)
receivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivePower.setStatus("current")
_VectorError_Type = Integer32
_VectorError_Object = MibTableColumn
vectorError = _VectorError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 19, 1, 4),
    _VectorError_Type()
)
vectorError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vectorError.setStatus("current")
_SignalStrengthRatio_Type = Integer32
_SignalStrengthRatio_Object = MibTableColumn
signalStrengthRatio = _SignalStrengthRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 19, 1, 5),
    _SignalStrengthRatio_Type()
)
signalStrengthRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalStrengthRatio.setStatus("current")
_Range_Type = Integer32
_Range_Object = MibTableColumn
range = _Range_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 19, 1, 6),
    _Range_Type()
)
range.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range.setStatus("current")


class _ReceiveModulationMode_Type(Integer32):
    """Custom type receiveModulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("modAcquisition", 0),
          ("modBpsk63percent", 1),
          ("modQpsk63percentSingle", 2),
          ("modTransient1", 3),
          ("modQpsk87percentSingle", 4),
          ("modTransient2", 5),
          ("mod16qam63percentSingleA", 6),
          ("modTransient3", 7),
          ("mod16qam87percentSingle", 8),
          ("modTransient4", 9),
          ("mod64qam75percentSingle", 10),
          ("modTransient5", 11),
          ("mod64qam92percentSingle", 12),
          ("modTransient6", 13),
          ("mod256qam81percentSingle", 14),
          ("mod16qam63percentSingleB", 15),
          ("mod16qam63percentDual", 16),
          ("modTransient7", 17),
          ("mod16qam87percentDual", 18),
          ("modTransient8", 19),
          ("mod64qam75percentDual", 20),
          ("modTransient9", 21),
          ("mod64qam92percentDual", 22),
          ("modTransient10", 23),
          ("mod256qam81percentDual", 24))
    )


_ReceiveModulationMode_Type.__name__ = "Integer32"
_ReceiveModulationMode_Object = MibTableColumn
receiveModulationMode = _ReceiveModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 19, 1, 7),
    _ReceiveModulationMode_Type()
)
receiveModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveModulationMode.setStatus("current")


class _TransmitModulationMode_Type(Integer32):
    """Custom type transmitModulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("modAcquisition", 0),
          ("modBpsk63percent", 1),
          ("modQpsk63percentSingle", 2),
          ("modTransient1", 3),
          ("modQpsk87percentSingle", 4),
          ("modTransient2", 5),
          ("mod16qam63percentSingleA", 6),
          ("modTransient3", 7),
          ("mod16qam87percentSingle", 8),
          ("modTransient4", 9),
          ("mod64qam75percentSingle", 10),
          ("modTransient5", 11),
          ("mod64qam92percentSingle", 12),
          ("modTransient6", 13),
          ("mod256qam81percentSingle", 14),
          ("mod16qam63percentSingleB", 15),
          ("mod16qam63percentDual", 16),
          ("modTransient7", 17),
          ("mod16qam87percentDual", 18),
          ("modTransient8", 19),
          ("mod64qam75percentDual", 20),
          ("modTransient9", 21),
          ("mod64qam92percentDual", 22),
          ("modTransient10", 23),
          ("mod256qam81percentDual", 24))
    )


_TransmitModulationMode_Type.__name__ = "Integer32"
_TransmitModulationMode_Object = MibTableColumn
transmitModulationMode = _TransmitModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 19, 1, 8),
    _TransmitModulationMode_Type()
)
transmitModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitModulationMode.setStatus("current")


class _SearchState_Type(Integer32):
    """Custom type searchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("registering", 0),
          ("searching", 1),
          ("acquiring", 2))
    )


_SearchState_Type.__name__ = "Integer32"
_SearchState_Object = MibTableColumn
searchState = _SearchState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 19, 1, 9),
    _SearchState_Type()
)
searchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    searchState.setStatus("current")


class _RemoteMACAddress_Type(OctetString):
    """Custom type remoteMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RemoteMACAddress_Type.__name__ = "OctetString"
_RemoteMACAddress_Object = MibTableColumn
remoteMACAddress = _RemoteMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 19, 1, 10),
    _RemoteMACAddress_Type()
)
remoteMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMACAddress.setStatus("current")
_RawReceivePower_Type = Integer32
_RawReceivePower_Object = MibTableColumn
rawReceivePower = _RawReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 19, 1, 11),
    _RawReceivePower_Type()
)
rawReceivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rawReceivePower.setStatus("current")
_TransmitPower_Type = Integer32
_TransmitPower_Object = MibTableColumn
transmitPower = _TransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 19, 1, 12),
    _TransmitPower_Type()
)
transmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitPower.setStatus("current")


class _TempPcb_Type(Integer32):
    """Custom type tempPcb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_TempPcb_Type.__name__ = "Integer32"
_TempPcb_Object = MibScalar
tempPcb = _TempPcb_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 12, 20),
    _TempPcb_Type()
)
tempPcb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempPcb.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13)
)


class _UnitOutOfCalibration_Type(Integer32):
    """Custom type unitOutOfCalibration based on Integer32"""
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
        *(("calibrated", 0),
          ("partialCalibration", 1),
          ("invalidCalibration", 2),
          ("bandwidthvariantunsupportedPAsShutdown", 3),
          ("outOfCalibrationPAsShutdown", 4))
    )


_UnitOutOfCalibration_Type.__name__ = "Integer32"
_UnitOutOfCalibration_Object = MibScalar
unitOutOfCalibration = _UnitOutOfCalibration_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 1),
    _UnitOutOfCalibration_Type()
)
unitOutOfCalibration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitOutOfCalibration.setStatus("current")


class _IncompatibleRegulatoryBandsLinked_Type(Integer32):
    """Custom type incompatibleRegulatoryBandsLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("regOK", 0),
          ("regIncompatibleLicenseKeys", 1))
    )


_IncompatibleRegulatoryBandsLinked_Type.__name__ = "Integer32"
_IncompatibleRegulatoryBandsLinked_Object = MibScalar
incompatibleRegulatoryBandsLinked = _IncompatibleRegulatoryBandsLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 4),
    _IncompatibleRegulatoryBandsLinked_Type()
)
incompatibleRegulatoryBandsLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incompatibleRegulatoryBandsLinked.setStatus("current")


class _NoWirelessChannelAvailable_Type(Integer32):
    """Custom type noWirelessChannelAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("noWirelessChannelAvailable", 1))
    )


_NoWirelessChannelAvailable_Type.__name__ = "Integer32"
_NoWirelessChannelAvailable_Object = MibScalar
noWirelessChannelAvailable = _NoWirelessChannelAvailable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 5),
    _NoWirelessChannelAvailable_Type()
)
noWirelessChannelAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noWirelessChannelAvailable.setStatus("current")


class _WirelessLinkDisabledWarning_Type(Integer32):
    """Custom type wirelessLinkDisabledWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("disabledBySNMPifAdminStatus", 1))
    )


_WirelessLinkDisabledWarning_Type.__name__ = "Integer32"
_WirelessLinkDisabledWarning_Object = MibScalar
wirelessLinkDisabledWarning = _WirelessLinkDisabledWarning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 6),
    _WirelessLinkDisabledWarning_Type()
)
wirelessLinkDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkDisabledWarning.setStatus("current")


class _MainPSUPortDisabledWarning_Type(Integer32):
    """Custom type mainPSUPortDisabledWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("disabledBySNMPifAdminStatus", 1))
    )


_MainPSUPortDisabledWarning_Type.__name__ = "Integer32"
_MainPSUPortDisabledWarning_Object = MibScalar
mainPSUPortDisabledWarning = _MainPSUPortDisabledWarning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 7),
    _MainPSUPortDisabledWarning_Type()
)
mainPSUPortDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortDisabledWarning.setStatus("current")


class _SFPError_Type(Integer32):
    """Custom type sFPError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("installedSFPNotLicensed", 1),
          ("fiberLinkNotEstablishedButLOSNotDetected", 2),
          ("fiberLinkNotEstablishedAndLOSDetected", 3),
          ("installedSFPNotSupported", 4),
          ("sFPInitializationFailed", 5))
    )


_SFPError_Type.__name__ = "Integer32"
_SFPError_Object = MibScalar
sFPError = _SFPError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 8),
    _SFPError_Type()
)
sFPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPError.setStatus("current")


class _MainPSUPortConfigurationMismatch_Type(Integer32):
    """Custom type mainPSUPortConfigurationMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("mismatchDetected", 1))
    )


_MainPSUPortConfigurationMismatch_Type.__name__ = "Integer32"
_MainPSUPortConfigurationMismatch_Object = MibScalar
mainPSUPortConfigurationMismatch = _MainPSUPortConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 9),
    _MainPSUPortConfigurationMismatch_Type()
)
mainPSUPortConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainPSUPortConfigurationMismatch.setStatus("current")


class _IncompatibleMasterAndSlaveLinked_Type(Integer32):
    """Custom type incompatibleMasterAndSlaveLinked based on Integer32"""
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
        *(("ok", 0),
          ("incompatibleProductVariants", 1),
          ("differentSoftwareVersionsRunning", 2),
          ("tDDFrameConfigurationModeMismatch", 3))
    )


_IncompatibleMasterAndSlaveLinked_Type.__name__ = "Integer32"
_IncompatibleMasterAndSlaveLinked_Object = MibScalar
incompatibleMasterAndSlaveLinked = _IncompatibleMasterAndSlaveLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 10),
    _IncompatibleMasterAndSlaveLinked_Type()
)
incompatibleMasterAndSlaveLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incompatibleMasterAndSlaveLinked.setStatus("current")


class _TDDSynchronizationStatus_Type(Integer32):
    """Custom type tDDSynchronizationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("holdover", 1),
          ("holdoverNoGPSSyncIn", 2),
          ("notSynchronized", 3),
          ("notSynchronizedNoGPSSyncIn", 4),
          ("pTPSYNCNotConnected", 5),
          ("initialising", 6),
          ("clusterTimingMaster", 7),
          ("acquiringLock", 8),
          ("inactive", 9))
    )


_TDDSynchronizationStatus_Type.__name__ = "Integer32"
_TDDSynchronizationStatus_Object = MibScalar
tDDSynchronizationStatus = _TDDSynchronizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 11),
    _TDDSynchronizationStatus_Type()
)
tDDSynchronizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDDSynchronizationStatus.setStatus("current")


class _AuxPortDisabledWarning_Type(Integer32):
    """Custom type auxPortDisabledWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("disabledBySNMPifAdminStatus", 1))
    )


_AuxPortDisabledWarning_Type.__name__ = "Integer32"
_AuxPortDisabledWarning_Object = MibScalar
auxPortDisabledWarning = _AuxPortDisabledWarning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 12),
    _AuxPortDisabledWarning_Type()
)
auxPortDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortDisabledWarning.setStatus("current")


class _TDDSynchronizationAlarm_Type(Integer32):
    """Custom type tDDSynchronizationAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("synchronizationLost", 1),
          ("referenceSignalLost", 2))
    )


_TDDSynchronizationAlarm_Type.__name__ = "Integer32"
_TDDSynchronizationAlarm_Object = MibScalar
tDDSynchronizationAlarm = _TDDSynchronizationAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 13),
    _TDDSynchronizationAlarm_Type()
)
tDDSynchronizationAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDDSynchronizationAlarm.setStatus("current")


class _LinkModeOptimizationMismatchLinked_Type(Integer32):
    """Custom type linkModeOptimizationMismatchLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("linkModeOptimizationMismatch", 1))
    )


_LinkModeOptimizationMismatchLinked_Type.__name__ = "Integer32"
_LinkModeOptimizationMismatchLinked_Object = MibScalar
linkModeOptimizationMismatchLinked = _LinkModeOptimizationMismatchLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 14),
    _LinkModeOptimizationMismatchLinked_Type()
)
linkModeOptimizationMismatchLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkModeOptimizationMismatchLinked.setStatus("current")


class _AuxPortConfigurationMismatch_Type(Integer32):
    """Custom type auxPortConfigurationMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("mismatchDetected", 1))
    )


_AuxPortConfigurationMismatch_Type.__name__ = "Integer32"
_AuxPortConfigurationMismatch_Object = MibScalar
auxPortConfigurationMismatch = _AuxPortConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 15),
    _AuxPortConfigurationMismatch_Type()
)
auxPortConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxPortConfigurationMismatch.setStatus("current")


class _SecureModeAlarm_Type(Integer32):
    """Custom type secureModeAlarm based on Integer32"""
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
        *(("secureModeIsActive", 0),
          ("secureModeIsNotConfigured", 1),
          ("secureModeIsConfiguredButNotActive", 2),
          ("secureModeIsNotSupported", 3))
    )


_SecureModeAlarm_Type.__name__ = "Integer32"
_SecureModeAlarm_Object = MibScalar
secureModeAlarm = _SecureModeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 16),
    _SecureModeAlarm_Type()
)
secureModeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureModeAlarm.setStatus("current")


class _DataBridgingStatusAlarmLinked_Type(Integer32):
    """Custom type dataBridgingStatusAlarmLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bridgingEnabled", 0),
          ("bridgingDisabled", 1))
    )


_DataBridgingStatusAlarmLinked_Type.__name__ = "Integer32"
_DataBridgingStatusAlarmLinked_Object = MibScalar
dataBridgingStatusAlarmLinked = _DataBridgingStatusAlarmLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 17),
    _DataBridgingStatusAlarmLinked_Type()
)
dataBridgingStatusAlarmLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataBridgingStatusAlarmLinked.setStatus("current")


class _SFPPortDisabledWarning_Type(Integer32):
    """Custom type sFPPortDisabledWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("disabledBySNMPifAdminStatus", 1))
    )


_SFPPortDisabledWarning_Type.__name__ = "Integer32"
_SFPPortDisabledWarning_Object = MibScalar
sFPPortDisabledWarning = _SFPPortDisabledWarning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 18),
    _SFPPortDisabledWarning_Type()
)
sFPPortDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortDisabledWarning.setStatus("current")


class _SFPPortConfigurationMismatch_Type(Integer32):
    """Custom type sFPPortConfigurationMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("mismatchDetected", 1))
    )


_SFPPortConfigurationMismatch_Type.__name__ = "Integer32"
_SFPPortConfigurationMismatch_Object = MibScalar
sFPPortConfigurationMismatch = _SFPPortConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 19),
    _SFPPortConfigurationMismatch_Type()
)
sFPPortConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFPPortConfigurationMismatch.setStatus("current")


class _MaxLinkRangeExceededLinked_Type(Integer32):
    """Custom type maxLinkRangeExceededLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("maxLinkRangeOK", 0),
          ("maxLinkRangeExceeded", 1))
    )


_MaxLinkRangeExceededLinked_Type.__name__ = "Integer32"
_MaxLinkRangeExceededLinked_Object = MibScalar
maxLinkRangeExceededLinked = _MaxLinkRangeExceededLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 20),
    _MaxLinkRangeExceededLinked_Type()
)
maxLinkRangeExceededLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLinkRangeExceededLinked.setStatus("current")


class _NIDULanPortDisabledWarning_Type(Integer32):
    """Custom type nIDULanPortDisabledWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("disabledBySNMPifAdminStatus", 1))
    )


_NIDULanPortDisabledWarning_Type.__name__ = "Integer32"
_NIDULanPortDisabledWarning_Object = MibScalar
nIDULanPortDisabledWarning = _NIDULanPortDisabledWarning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 21),
    _NIDULanPortDisabledWarning_Type()
)
nIDULanPortDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortDisabledWarning.setStatus("current")


class _NIDULanPortConfigurationMismatch_Type(Integer32):
    """Custom type nIDULanPortConfigurationMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("mismatchDetected", 1))
    )


_NIDULanPortConfigurationMismatch_Type.__name__ = "Integer32"
_NIDULanPortConfigurationMismatch_Object = MibScalar
nIDULanPortConfigurationMismatch = _NIDULanPortConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 22),
    _NIDULanPortConfigurationMismatch_Type()
)
nIDULanPortConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nIDULanPortConfigurationMismatch.setStatus("current")


class _PortAllocationMismatchLinked_Type(Integer32):
    """Custom type portAllocationMismatchLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("portAllocationOK", 0),
          ("mismatchinOutofBandRemoteManagementService", 1))
    )


_PortAllocationMismatchLinked_Type.__name__ = "Integer32"
_PortAllocationMismatchLinked_Object = MibScalar
portAllocationMismatchLinked = _PortAllocationMismatchLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 23),
    _PortAllocationMismatchLinked_Type()
)
portAllocationMismatchLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAllocationMismatchLinked.setStatus("current")


class _TransparentClockSourcePortAlarm_Type(Integer32):
    """Custom type transparentClockSourcePortAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("invalidTransparentClockSourcePort", 1))
    )


_TransparentClockSourcePortAlarm_Type.__name__ = "Integer32"
_TransparentClockSourcePortAlarm_Object = MibScalar
transparentClockSourcePortAlarm = _TransparentClockSourcePortAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 25),
    _TransparentClockSourcePortAlarm_Type()
)
transparentClockSourcePortAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transparentClockSourcePortAlarm.setStatus("current")


class _AlarmInstancedTableNumber_Type(Integer32):
    """Custom type alarmInstancedTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlarmInstancedTableNumber_Type.__name__ = "Integer32"
_AlarmInstancedTableNumber_Object = MibScalar
alarmInstancedTableNumber = _AlarmInstancedTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 26),
    _AlarmInstancedTableNumber_Type()
)
alarmInstancedTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmInstancedTableNumber.setStatus("current")
_AlarmInstancedTable_Object = MibTable
alarmInstancedTable = _AlarmInstancedTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 27)
)
if mibBuilder.loadTexts:
    alarmInstancedTable.setStatus("current")
_AlarmInstancedTableEntry_Object = MibTableRow
alarmInstancedTableEntry = _AlarmInstancedTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 27, 1)
)
alarmInstancedTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "alarmInstancedTableIndex"),
)
if mibBuilder.loadTexts:
    alarmInstancedTableEntry.setStatus("current")


class _AlarmInstancedTableIndex_Type(Integer32):
    """Custom type alarmInstancedTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlarmInstancedTableIndex_Type.__name__ = "Integer32"
_AlarmInstancedTableIndex_Object = MibTableColumn
alarmInstancedTableIndex = _AlarmInstancedTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 27, 1, 1),
    _AlarmInstancedTableIndex_Type()
)
alarmInstancedTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmInstancedTableIndex.setStatus("current")


class _IncompatibleMasterAndSlave_Type(Integer32):
    """Custom type incompatibleMasterAndSlave based on Integer32"""
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
        *(("ok", 0),
          ("incompatibleProductVariants", 1),
          ("differentSoftwareVersionsRunning", 2),
          ("tDDFrameConfigurationModeMismatch", 3))
    )


_IncompatibleMasterAndSlave_Type.__name__ = "Integer32"
_IncompatibleMasterAndSlave_Object = MibTableColumn
incompatibleMasterAndSlave = _IncompatibleMasterAndSlave_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 27, 1, 2),
    _IncompatibleMasterAndSlave_Type()
)
incompatibleMasterAndSlave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incompatibleMasterAndSlave.setStatus("current")


class _LinkModeOptimizationMismatch_Type(Integer32):
    """Custom type linkModeOptimizationMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("linkModeOptimizationMismatch", 1))
    )


_LinkModeOptimizationMismatch_Type.__name__ = "Integer32"
_LinkModeOptimizationMismatch_Object = MibTableColumn
linkModeOptimizationMismatch = _LinkModeOptimizationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 27, 1, 3),
    _LinkModeOptimizationMismatch_Type()
)
linkModeOptimizationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkModeOptimizationMismatch.setStatus("current")


class _DataBridgingStatusAlarm_Type(Integer32):
    """Custom type dataBridgingStatusAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bridgingEnabled", 0),
          ("bridgingDisabled", 1))
    )


_DataBridgingStatusAlarm_Type.__name__ = "Integer32"
_DataBridgingStatusAlarm_Object = MibTableColumn
dataBridgingStatusAlarm = _DataBridgingStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 27, 1, 4),
    _DataBridgingStatusAlarm_Type()
)
dataBridgingStatusAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataBridgingStatusAlarm.setStatus("current")


class _MaxLinkRangeExceeded_Type(Integer32):
    """Custom type maxLinkRangeExceeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("maxLinkRangeOK", 0),
          ("maxLinkRangeExceeded", 1))
    )


_MaxLinkRangeExceeded_Type.__name__ = "Integer32"
_MaxLinkRangeExceeded_Object = MibTableColumn
maxLinkRangeExceeded = _MaxLinkRangeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 27, 1, 5),
    _MaxLinkRangeExceeded_Type()
)
maxLinkRangeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLinkRangeExceeded.setStatus("current")


class _PortAllocationMismatch_Type(Integer32):
    """Custom type portAllocationMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("portAllocationOK", 0),
          ("mismatchinOutofBandRemoteManagementService", 1))
    )


_PortAllocationMismatch_Type.__name__ = "Integer32"
_PortAllocationMismatch_Object = MibTableColumn
portAllocationMismatch = _PortAllocationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 27, 1, 6),
    _PortAllocationMismatch_Type()
)
portAllocationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAllocationMismatch.setStatus("current")


class _WirelessLinkStatusAlarm_Type(Integer32):
    """Custom type wirelessLinkStatusAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )


_WirelessLinkStatusAlarm_Type.__name__ = "Integer32"
_WirelessLinkStatusAlarm_Object = MibTableColumn
wirelessLinkStatusAlarm = _WirelessLinkStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 27, 1, 7),
    _WirelessLinkStatusAlarm_Type()
)
wirelessLinkStatusAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatusAlarm.setStatus("current")


class _IncompatibleRegulatoryBands_Type(Integer32):
    """Custom type incompatibleRegulatoryBands based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("regOK", 0),
          ("regIncompatibleLicenseKeys", 1))
    )


_IncompatibleRegulatoryBands_Type.__name__ = "Integer32"
_IncompatibleRegulatoryBands_Object = MibTableColumn
incompatibleRegulatoryBands = _IncompatibleRegulatoryBands_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 27, 1, 8),
    _IncompatibleRegulatoryBands_Type()
)
incompatibleRegulatoryBands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incompatibleRegulatoryBands.setStatus("current")


class _SecureLicenseSignatureAlarm_Type(Integer32):
    """Custom type secureLicenseSignatureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licenseisDSA2048signed", 0),
          ("licenseisDSA1024signed", 1),
          ("licensesignaturealarmisnotrelevant", 2))
    )


_SecureLicenseSignatureAlarm_Type.__name__ = "Integer32"
_SecureLicenseSignatureAlarm_Object = MibScalar
secureLicenseSignatureAlarm = _SecureLicenseSignatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 13, 28),
    _SecureLicenseSignatureAlarm_Type()
)
secureLicenseSignatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secureLicenseSignatureAlarm.setStatus("current")
_Apc_ObjectIdentity = ObjectIdentity
apc = _Apc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 14)
)


class _AtpcHcmpMasterTargetRxPower_Type(Integer32):
    """Custom type atpcHcmpMasterTargetRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, -30),
    )


_AtpcHcmpMasterTargetRxPower_Type.__name__ = "Integer32"
_AtpcHcmpMasterTargetRxPower_Object = MibScalar
atpcHcmpMasterTargetRxPower = _AtpcHcmpMasterTargetRxPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 14, 1),
    _AtpcHcmpMasterTargetRxPower_Type()
)
atpcHcmpMasterTargetRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atpcHcmpMasterTargetRxPower.setStatus("current")


class _AtpcHcmpMasterTxPower_Type(Integer32):
    """Custom type atpcHcmpMasterTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 30),
    )


_AtpcHcmpMasterTxPower_Type.__name__ = "Integer32"
_AtpcHcmpMasterTxPower_Object = MibScalar
atpcHcmpMasterTxPower = _AtpcHcmpMasterTxPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 14, 2),
    _AtpcHcmpMasterTxPower_Type()
)
atpcHcmpMasterTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atpcHcmpMasterTxPower.setStatus("current")
_Smtp_ObjectIdentity = ObjectIdentity
smtp = _Smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 15)
)


class _SMTPEmailAlert_Type(Integer32):
    """Custom type sMTPEmailAlert based on Integer32"""
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


_SMTPEmailAlert_Type.__name__ = "Integer32"
_SMTPEmailAlert_Object = MibScalar
sMTPEmailAlert = _SMTPEmailAlert_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 15, 1),
    _SMTPEmailAlert_Type()
)
sMTPEmailAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPEmailAlert.setStatus("current")


class _SMTPServerPortNumber_Type(Integer32):
    """Custom type sMTPServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SMTPServerPortNumber_Type.__name__ = "Integer32"
_SMTPServerPortNumber_Object = MibScalar
sMTPServerPortNumber = _SMTPServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 15, 3),
    _SMTPServerPortNumber_Type()
)
sMTPServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPServerPortNumber.setStatus("current")


class _SMTPSourceEmailAddress_Type(DisplayString):
    """Custom type sMTPSourceEmailAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SMTPSourceEmailAddress_Type.__name__ = "DisplayString"
_SMTPSourceEmailAddress_Object = MibScalar
sMTPSourceEmailAddress = _SMTPSourceEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 15, 4),
    _SMTPSourceEmailAddress_Type()
)
sMTPSourceEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPSourceEmailAddress.setStatus("current")


class _SMTPDestinationEmailAddress_Type(DisplayString):
    """Custom type sMTPDestinationEmailAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SMTPDestinationEmailAddress_Type.__name__ = "DisplayString"
_SMTPDestinationEmailAddress_Object = MibScalar
sMTPDestinationEmailAddress = _SMTPDestinationEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 15, 5),
    _SMTPDestinationEmailAddress_Type()
)
sMTPDestinationEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPDestinationEmailAddress.setStatus("current")


class _SMTPEnabledMessages_Type(Bits):
    """Custom type sMTPEnabledMessages based on Bits"""
    namedValues = NamedValues(
        *(("nIDULanPortUpDown", 0),
          ("sFPPortUpDown", 1),
          ("auxPortUpDown", 2),
          ("mainPSUPortUpDown", 3),
          ("enabledDiagnosticAlarms", 4),
          ("dFSImpulseInterference", 5),
          ("channelChange", 6),
          ("wirelessPortUpDown", 7),
          ("listenBeforeTalk", 15))
    )

_SMTPEnabledMessages_Type.__name__ = "Bits"
_SMTPEnabledMessages_Object = MibScalar
sMTPEnabledMessages = _SMTPEnabledMessages_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 15, 6),
    _SMTPEnabledMessages_Type()
)
sMTPEnabledMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPEnabledMessages.setStatus("current")


class _SMTPServerInternetAddressType_Type(Integer32):
    """Custom type sMTPServerInternetAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipv4z", 3),
          ("ipv6z", 4),
          ("unknown6", 5),
          ("unknown7", 6),
          ("unknown8", 7),
          ("unknown9", 8),
          ("unknown10", 9),
          ("unknown11", 10),
          ("unknown12", 11),
          ("unknown13", 12),
          ("unknown14", 13),
          ("unknown15", 14),
          ("unknown16", 15),
          ("dns", 16))
    )


_SMTPServerInternetAddressType_Type.__name__ = "Integer32"
_SMTPServerInternetAddressType_Object = MibScalar
sMTPServerInternetAddressType = _SMTPServerInternetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 15, 7),
    _SMTPServerInternetAddressType_Type()
)
sMTPServerInternetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sMTPServerInternetAddressType.setStatus("current")
_SMTPServerInternetAddress_Type = InetAddress
_SMTPServerInternetAddress_Object = MibScalar
sMTPServerInternetAddress = _SMTPServerInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 15, 8),
    _SMTPServerInternetAddress_Type()
)
sMTPServerInternetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPServerInternetAddress.setStatus("current")


class _SMTPServerResolvedInternetAddress_Type(DisplayString):
    """Custom type sMTPServerResolvedInternetAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SMTPServerResolvedInternetAddress_Type.__name__ = "DisplayString"
_SMTPServerResolvedInternetAddress_Object = MibScalar
sMTPServerResolvedInternetAddress = _SMTPServerResolvedInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 15, 9),
    _SMTPServerResolvedInternetAddress_Type()
)
sMTPServerResolvedInternetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sMTPServerResolvedInternetAddress.setStatus("current")
_SnmpControl_ObjectIdentity = ObjectIdentity
snmpControl = _SnmpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16)
)


class _SNMPPortNumber_Type(Integer32):
    """Custom type sNMPPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SNMPPortNumber_Type.__name__ = "Integer32"
_SNMPPortNumber_Object = MibScalar
sNMPPortNumber = _SNMPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16, 1),
    _SNMPPortNumber_Type()
)
sNMPPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPPortNumber.setStatus("current")


class _SNMPCommunityString_Type(DisplayString):
    """Custom type sNMPCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SNMPCommunityString_Type.__name__ = "DisplayString"
_SNMPCommunityString_Object = MibScalar
sNMPCommunityString = _SNMPCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16, 2),
    _SNMPCommunityString_Type()
)
sNMPCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPCommunityString.setStatus("current")


class _SNMPTrapTableNumber_Type(Integer32):
    """Custom type sNMPTrapTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_SNMPTrapTableNumber_Type.__name__ = "Integer32"
_SNMPTrapTableNumber_Object = MibScalar
sNMPTrapTableNumber = _SNMPTrapTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16, 3),
    _SNMPTrapTableNumber_Type()
)
sNMPTrapTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPTrapTableNumber.setStatus("current")
_SNMPTrapTable_Object = MibTable
sNMPTrapTable = _SNMPTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16, 4)
)
if mibBuilder.loadTexts:
    sNMPTrapTable.setStatus("current")
_SNMPTrapTableEntry_Object = MibTableRow
sNMPTrapTableEntry = _SNMPTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16, 4, 1)
)
sNMPTrapTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "sNMPTrapTableIndex"),
)
if mibBuilder.loadTexts:
    sNMPTrapTableEntry.setStatus("current")


class _SNMPTrapTableIndex_Type(Integer32):
    """Custom type sNMPTrapTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SNMPTrapTableIndex_Type.__name__ = "Integer32"
_SNMPTrapTableIndex_Object = MibTableColumn
sNMPTrapTableIndex = _SNMPTrapTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16, 4, 1, 1),
    _SNMPTrapTableIndex_Type()
)
sNMPTrapTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sNMPTrapTableIndex.setStatus("current")


class _SNMPTrapPortNumber_Type(Integer32):
    """Custom type sNMPTrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SNMPTrapPortNumber_Type.__name__ = "Integer32"
_SNMPTrapPortNumber_Object = MibTableColumn
sNMPTrapPortNumber = _SNMPTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16, 4, 1, 3),
    _SNMPTrapPortNumber_Type()
)
sNMPTrapPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPTrapPortNumber.setStatus("current")


class _SNMPTrapInternetAddressType_Type(Integer32):
    """Custom type sNMPTrapInternetAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipv4z", 3),
          ("ipv6z", 4),
          ("unknown6", 5),
          ("unknown7", 6),
          ("unknown8", 7),
          ("unknown9", 8),
          ("unknown10", 9),
          ("unknown11", 10),
          ("unknown12", 11),
          ("unknown13", 12),
          ("unknown14", 13),
          ("unknown15", 14),
          ("unknown16", 15),
          ("dns", 16))
    )


_SNMPTrapInternetAddressType_Type.__name__ = "Integer32"
_SNMPTrapInternetAddressType_Object = MibTableColumn
sNMPTrapInternetAddressType = _SNMPTrapInternetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16, 4, 1, 4),
    _SNMPTrapInternetAddressType_Type()
)
sNMPTrapInternetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPTrapInternetAddressType.setStatus("current")
_SNMPTrapInternetAddress_Type = InetAddress
_SNMPTrapInternetAddress_Object = MibTableColumn
sNMPTrapInternetAddress = _SNMPTrapInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16, 4, 1, 5),
    _SNMPTrapInternetAddress_Type()
)
sNMPTrapInternetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPTrapInternetAddress.setStatus("current")


class _SNMPTrapReceiverEnabled_Type(Integer32):
    """Custom type sNMPTrapReceiverEnabled based on Integer32"""
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


_SNMPTrapReceiverEnabled_Type.__name__ = "Integer32"
_SNMPTrapReceiverEnabled_Object = MibTableColumn
sNMPTrapReceiverEnabled = _SNMPTrapReceiverEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16, 4, 1, 6),
    _SNMPTrapReceiverEnabled_Type()
)
sNMPTrapReceiverEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPTrapReceiverEnabled.setStatus("current")


class _SNMPTrapResolvedInternetAddress_Type(DisplayString):
    """Custom type sNMPTrapResolvedInternetAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SNMPTrapResolvedInternetAddress_Type.__name__ = "DisplayString"
_SNMPTrapResolvedInternetAddress_Object = MibTableColumn
sNMPTrapResolvedInternetAddress = _SNMPTrapResolvedInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16, 4, 1, 7),
    _SNMPTrapResolvedInternetAddress_Type()
)
sNMPTrapResolvedInternetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPTrapResolvedInternetAddress.setStatus("current")


class _SNMPTrapVersion_Type(Integer32):
    """Custom type sNMPTrapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1))
    )


_SNMPTrapVersion_Type.__name__ = "Integer32"
_SNMPTrapVersion_Object = MibScalar
sNMPTrapVersion = _SNMPTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16, 5),
    _SNMPTrapVersion_Type()
)
sNMPTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPTrapVersion.setStatus("current")


class _SNMPEnabledTraps_Type(Bits):
    """Custom type sNMPEnabledTraps based on Bits"""
    namedValues = NamedValues(
        *(("auxPortUpDown", 0),
          ("mainPSUPortUpDown", 1),
          ("authenticationFailure", 2),
          ("enabledDiagnosticAlarms", 3),
          ("dFSImpulseInterference", 4),
          ("channelChange", 5),
          ("wirelessPortUpDown", 6),
          ("coldStart", 7),
          ("listenBeforeTalk", 13),
          ("nIDULanPortUpDown", 14),
          ("sFPPortUpDown", 15))
    )

_SNMPEnabledTraps_Type.__name__ = "Bits"
_SNMPEnabledTraps_Object = MibScalar
sNMPEnabledTraps = _SNMPEnabledTraps_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16, 6),
    _SNMPEnabledTraps_Type()
)
sNMPEnabledTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPEnabledTraps.setStatus("current")


class _EnabledDiagnosticAlarms_Type(Bits):
    """Custom type enabledDiagnosticAlarms based on Bits"""
    namedValues = NamedValues(
        *(("portState", 0),
          ("incompatibleMasterAndSlave", 1),
          ("incompatibleRegulatoryBands", 2),
          ("maximumLinkRangeExceeded", 3),
          ("unitOutOfCalibration", 4),
          ("installArmState", 5),
          ("installStatus", 6),
          ("regulatoryBand", 7),
          ("syslogLocalWrapped", 8),
          ("syslogLocalNearlyFull", 9),
          ("syslogDisabledWarning", 10),
          ("linkModeOptimizationMismatch", 11),
          ("tDDSynchronizationAlarm", 12),
          ("wirelessLinkDisabledWarning", 13),
          ("sNTPSynchronizationFailed", 14),
          ("noWirelessChannelAvailable", 15),
          ("licenseSignatureLengthAlarm", 16),
          ("wirelessLinkStatus", 17),
          ("tDMAlarms", 18),
          ("capacityVariantMismatch", 19),
          ("remainingFullCapacityTrialTime", 20),
          ("dataBridgingStatus", 21),
          ("secureModeAlarm", 22),
          ("syslogClientDisabledWarning", 23))
    )

_EnabledDiagnosticAlarms_Type.__name__ = "Bits"
_EnabledDiagnosticAlarms_Object = MibScalar
enabledDiagnosticAlarms = _EnabledDiagnosticAlarms_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16, 7),
    _EnabledDiagnosticAlarms_Type()
)
enabledDiagnosticAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enabledDiagnosticAlarms.setStatus("current")


class _SNMPSendAllTrapsAtStartup_Type(Integer32):
    """Custom type sNMPSendAllTrapsAtStartup based on Integer32"""
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


_SNMPSendAllTrapsAtStartup_Type.__name__ = "Integer32"
_SNMPSendAllTrapsAtStartup_Object = MibScalar
sNMPSendAllTrapsAtStartup = _SNMPSendAllTrapsAtStartup_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 16, 8),
    _SNMPSendAllTrapsAtStartup_Type()
)
sNMPSendAllTrapsAtStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPSendAllTrapsAtStartup.setStatus("current")
_Sntp_ObjectIdentity = ObjectIdentity
sntp = _Sntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17)
)


class _SNTPState_Type(Integer32):
    """Custom type sNTPState based on Integer32"""
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


_SNTPState_Type.__name__ = "Integer32"
_SNTPState_Object = MibScalar
sNTPState = _SNTPState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 1),
    _SNTPState_Type()
)
sNTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPState.setStatus("current")


class _SNTPPollInterval_Type(Integer32):
    """Custom type sNTPPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 43200),
    )


_SNTPPollInterval_Type.__name__ = "Integer32"
_SNTPPollInterval_Object = MibScalar
sNTPPollInterval = _SNTPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 4),
    _SNTPPollInterval_Type()
)
sNTPPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPPollInterval.setStatus("current")


class _SNTPSync_Type(Integer32):
    """Custom type sNTPSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noSync", 0),
          ("inSync", 1))
    )


_SNTPSync_Type.__name__ = "Integer32"
_SNTPSync_Object = MibScalar
sNTPSync = _SNTPSync_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 5),
    _SNTPSync_Type()
)
sNTPSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPSync.setStatus("current")
_SNTPLastSync_Type = Integer32
_SNTPLastSync_Object = MibScalar
sNTPLastSync = _SNTPLastSync_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 6),
    _SNTPLastSync_Type()
)
sNTPLastSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPLastSync.setStatus("current")
_SystemClock_Type = Integer32
_SystemClock_Object = MibScalar
systemClock = _SystemClock_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 7),
    _SystemClock_Type()
)
systemClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemClock.setStatus("current")


class _TimeZone_Type(Integer32):
    """Custom type timeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50)
        )
    )
    namedValues = NamedValues(
        *(("gmtMinus1200", 0),
          ("gmtMinus1130", 1),
          ("gmtMinus1100", 2),
          ("gmtMinus1030", 3),
          ("gmtMinus1000", 4),
          ("gmtMinus0930", 5),
          ("gmtMinus0900", 6),
          ("gmtMinus0830", 7),
          ("gmtMinus0800", 8),
          ("gmtMinus0730", 9),
          ("gmtMinus0700", 10),
          ("gmtMinus0630", 11),
          ("gmtMinus0600", 12),
          ("gmtMinus0530", 13),
          ("gmtMinus0500", 14),
          ("gmtMinus0430", 15),
          ("gmtMinus0400", 16),
          ("gmtMinus0330", 17),
          ("gmtMinus0300", 18),
          ("gmtMinus0230", 19),
          ("gmtMinus0200", 20),
          ("gmtMinus0130", 21),
          ("gmtMinus0100", 22),
          ("gmtMinus0030", 23),
          ("gmtZero", 24),
          ("gmtPlus0030", 25),
          ("gmtPlus0100", 26),
          ("gmtPlus0130", 27),
          ("gmtPlus0200", 28),
          ("gmtPlus0230", 29),
          ("gmtPlus0300", 30),
          ("gmtPlus0330", 31),
          ("gmtPlus0400", 32),
          ("gmtPlus0430", 33),
          ("gmtPlus0500", 34),
          ("gmtPlus0530", 35),
          ("gmtPlus0600", 36),
          ("gmtPlus0630", 37),
          ("gmtPlus0700", 38),
          ("gmtPlus0730", 39),
          ("gmtPlus0800", 40),
          ("gmtPlus0830", 41),
          ("gmtPlus0900", 42),
          ("gmtPlus0930", 43),
          ("gmtPlus1000", 44),
          ("gmtPlus1030", 45),
          ("gmtPlus1100", 46),
          ("gmtPlus1130", 47),
          ("gmtPlus1200", 48),
          ("gmtPlus1230", 49),
          ("gmtPlus1300", 50))
    )


_TimeZone_Type.__name__ = "Integer32"
_TimeZone_Object = MibScalar
timeZone = _TimeZone_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 8),
    _TimeZone_Type()
)
timeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeZone.setStatus("current")


class _DaylightSaving_Type(Integer32):
    """Custom type daylightSaving based on Integer32"""
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


_DaylightSaving_Type.__name__ = "Integer32"
_DaylightSaving_Object = MibScalar
daylightSaving = _DaylightSaving_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 9),
    _DaylightSaving_Type()
)
daylightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSaving.setStatus("current")


class _SNTPPrimaryServer_Type(Integer32):
    """Custom type sNTPPrimaryServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("server1", 0),
          ("server2", 1))
    )


_SNTPPrimaryServer_Type.__name__ = "Integer32"
_SNTPPrimaryServer_Object = MibScalar
sNTPPrimaryServer = _SNTPPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 10),
    _SNTPPrimaryServer_Type()
)
sNTPPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPPrimaryServer.setStatus("current")


class _SNTPPrimaryServerDeadTime_Type(Integer32):
    """Custom type sNTPPrimaryServerDeadTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_SNTPPrimaryServerDeadTime_Type.__name__ = "Integer32"
_SNTPPrimaryServerDeadTime_Object = MibScalar
sNTPPrimaryServerDeadTime = _SNTPPrimaryServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 11),
    _SNTPPrimaryServerDeadTime_Type()
)
sNTPPrimaryServerDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPPrimaryServerDeadTime.setStatus("current")


class _SNTPServerRetries_Type(Integer32):
    """Custom type sNTPServerRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SNTPServerRetries_Type.__name__ = "Integer32"
_SNTPServerRetries_Object = MibScalar
sNTPServerRetries = _SNTPServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 12),
    _SNTPServerRetries_Type()
)
sNTPServerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPServerRetries.setStatus("current")


class _SNTPServerTimeout_Type(Integer32):
    """Custom type sNTPServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SNTPServerTimeout_Type.__name__ = "Integer32"
_SNTPServerTimeout_Object = MibScalar
sNTPServerTimeout = _SNTPServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 13),
    _SNTPServerTimeout_Type()
)
sNTPServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPServerTimeout.setStatus("current")


class _SNTPServerTableNumber_Type(Integer32):
    """Custom type sNTPServerTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_SNTPServerTableNumber_Type.__name__ = "Integer32"
_SNTPServerTableNumber_Object = MibScalar
sNTPServerTableNumber = _SNTPServerTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 14),
    _SNTPServerTableNumber_Type()
)
sNTPServerTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPServerTableNumber.setStatus("current")
_SNTPServerTable_Object = MibTable
sNTPServerTable = _SNTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 15)
)
if mibBuilder.loadTexts:
    sNTPServerTable.setStatus("current")
_SNTPServerTableEntry_Object = MibTableRow
sNTPServerTableEntry = _SNTPServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 15, 1)
)
sNTPServerTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "sNTPServerTableIndex"),
)
if mibBuilder.loadTexts:
    sNTPServerTableEntry.setStatus("current")


class _SNTPServerTableIndex_Type(Integer32):
    """Custom type sNTPServerTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SNTPServerTableIndex_Type.__name__ = "Integer32"
_SNTPServerTableIndex_Object = MibTableColumn
sNTPServerTableIndex = _SNTPServerTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 15, 1, 1),
    _SNTPServerTableIndex_Type()
)
sNTPServerTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sNTPServerTableIndex.setStatus("current")


class _SNTPServerPortNumber_Type(Integer32):
    """Custom type sNTPServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SNTPServerPortNumber_Type.__name__ = "Integer32"
_SNTPServerPortNumber_Object = MibTableColumn
sNTPServerPortNumber = _SNTPServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 15, 1, 3),
    _SNTPServerPortNumber_Type()
)
sNTPServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPServerPortNumber.setStatus("current")


class _SNTPServerStatus_Type(DisplayString):
    """Custom type sNTPServerStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SNTPServerStatus_Type.__name__ = "DisplayString"
_SNTPServerStatus_Object = MibTableColumn
sNTPServerStatus = _SNTPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 15, 1, 4),
    _SNTPServerStatus_Type()
)
sNTPServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPServerStatus.setStatus("current")


class _SNTPServerInternetAddressType_Type(Integer32):
    """Custom type sNTPServerInternetAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipv4z", 3),
          ("ipv6z", 4),
          ("unknown6", 5),
          ("unknown7", 6),
          ("unknown8", 7),
          ("unknown9", 8),
          ("unknown10", 9),
          ("unknown11", 10),
          ("unknown12", 11),
          ("unknown13", 12),
          ("unknown14", 13),
          ("unknown15", 14),
          ("unknown16", 15),
          ("dns", 16))
    )


_SNTPServerInternetAddressType_Type.__name__ = "Integer32"
_SNTPServerInternetAddressType_Object = MibTableColumn
sNTPServerInternetAddressType = _SNTPServerInternetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 15, 1, 5),
    _SNTPServerInternetAddressType_Type()
)
sNTPServerInternetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPServerInternetAddressType.setStatus("current")
_SNTPServerInternetAddress_Type = InetAddress
_SNTPServerInternetAddress_Object = MibTableColumn
sNTPServerInternetAddress = _SNTPServerInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 15, 1, 6),
    _SNTPServerInternetAddress_Type()
)
sNTPServerInternetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPServerInternetAddress.setStatus("current")


class _SNTPServerResolvedInternetAddress_Type(DisplayString):
    """Custom type sNTPServerResolvedInternetAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SNTPServerResolvedInternetAddress_Type.__name__ = "DisplayString"
_SNTPServerResolvedInternetAddress_Object = MibTableColumn
sNTPServerResolvedInternetAddress = _SNTPServerResolvedInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 15, 1, 7),
    _SNTPServerResolvedInternetAddress_Type()
)
sNTPServerResolvedInternetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPServerResolvedInternetAddress.setStatus("current")


class _SNTPServerAuthenticationProtocol_Type(Integer32):
    """Custom type sNTPServerAuthenticationProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("mD5", 1),
          ("sHA1", 2))
    )


_SNTPServerAuthenticationProtocol_Type.__name__ = "Integer32"
_SNTPServerAuthenticationProtocol_Object = MibTableColumn
sNTPServerAuthenticationProtocol = _SNTPServerAuthenticationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 15, 1, 8),
    _SNTPServerAuthenticationProtocol_Type()
)
sNTPServerAuthenticationProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPServerAuthenticationProtocol.setStatus("current")
_SNTPServerKeyIdentifier_Type = Integer32
_SNTPServerKeyIdentifier_Object = MibTableColumn
sNTPServerKeyIdentifier = _SNTPServerKeyIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 17, 15, 1, 9),
    _SNTPServerKeyIdentifier_Type()
)
sNTPServerKeyIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPServerKeyIdentifier.setStatus("current")
_Reset_ObjectIdentity = ObjectIdentity
reset = _Reset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 18)
)


class _SystemReset_Type(Integer32):
    """Custom type systemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("running", 0),
          ("consoleReboot", 1))
    )


_SystemReset_Type.__name__ = "Integer32"
_SystemReset_Object = MibScalar
systemReset = _SystemReset_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 18, 1),
    _SystemReset_Type()
)
systemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReset.setStatus("current")
_Versions_ObjectIdentity = ObjectIdentity
versions = _Versions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 19)
)


class _SoftwareVersion_Type(DisplayString):
    """Custom type softwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SoftwareVersion_Type.__name__ = "DisplayString"
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 19, 1),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")


class _HardwareVersion_Type(DisplayString):
    """Custom type hardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HardwareVersion_Type.__name__ = "DisplayString"
_HardwareVersion_Object = MibScalar
hardwareVersion = _HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 19, 2),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("current")


class _SecondarySoftwareVersion_Type(DisplayString):
    """Custom type secondarySoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SecondarySoftwareVersion_Type.__name__ = "DisplayString"
_SecondarySoftwareVersion_Object = MibScalar
secondarySoftwareVersion = _SecondarySoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 19, 3),
    _SecondarySoftwareVersion_Type()
)
secondarySoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondarySoftwareVersion.setStatus("current")


class _BootVersion_Type(DisplayString):
    """Custom type bootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_BootVersion_Type.__name__ = "DisplayString"
_BootVersion_Object = MibScalar
bootVersion = _BootVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 19, 4),
    _BootVersion_Type()
)
bootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootVersion.setStatus("current")
_PubStats_ObjectIdentity = ObjectIdentity
pubStats = _PubStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20)
)
_ReceiveDataRateLinked_Type = Integer32
_ReceiveDataRateLinked_Object = MibScalar
receiveDataRateLinked = _ReceiveDataRateLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 1),
    _ReceiveDataRateLinked_Type()
)
receiveDataRateLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveDataRateLinked.setStatus("current")
_TransmitDataRateLinked_Type = Integer32
_TransmitDataRateLinked_Object = MibScalar
transmitDataRateLinked = _TransmitDataRateLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 2),
    _TransmitDataRateLinked_Type()
)
transmitDataRateLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitDataRateLinked.setStatus("current")
_AggregateDataRateLinked_Type = Integer32
_AggregateDataRateLinked_Object = MibScalar
aggregateDataRateLinked = _AggregateDataRateLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 3),
    _AggregateDataRateLinked_Type()
)
aggregateDataRateLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregateDataRateLinked.setStatus("current")


class _WirelessLinkAvailabilityLinked_Type(Integer32):
    """Custom type wirelessLinkAvailabilityLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_WirelessLinkAvailabilityLinked_Type.__name__ = "Integer32"
_WirelessLinkAvailabilityLinked_Object = MibScalar
wirelessLinkAvailabilityLinked = _WirelessLinkAvailabilityLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 4),
    _WirelessLinkAvailabilityLinked_Type()
)
wirelessLinkAvailabilityLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkAvailabilityLinked.setStatus("current")


class _WirelessLinkStatusLinked_Type(Integer32):
    """Custom type wirelessLinkStatusLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("registering", 1),
          ("searching", 2),
          ("acquiring", 3),
          ("radarCAC", 4),
          ("initialising", 5))
    )


_WirelessLinkStatusLinked_Type.__name__ = "Integer32"
_WirelessLinkStatusLinked_Object = MibScalar
wirelessLinkStatusLinked = _WirelessLinkStatusLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 5),
    _WirelessLinkStatusLinked_Type()
)
wirelessLinkStatusLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatusLinked.setStatus("current")
_ByteErrorRatioLinked_Type = Integer32
_ByteErrorRatioLinked_Object = MibScalar
byteErrorRatioLinked = _ByteErrorRatioLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 6),
    _ByteErrorRatioLinked_Type()
)
byteErrorRatioLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    byteErrorRatioLinked.setStatus("current")


class _ReceiveModulationModeDetailLinked_Type(Integer32):
    """Custom type receiveModulationModeDetailLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("runningAtMaximumReceiveMode", 0),
          ("runningAtUserConfiguredMaxModulationMode", 1),
          ("restrictedBecauseInstallationIsArmed", 2),
          ("restrictedBecauseOfByteErrorsOnTheWirelessLink", 3),
          ("restrictedBecauseTheLinkParametersAreUpdating", 4),
          ("restrictedBecauseChannelChangeIsInProgress", 5),
          ("restrictedDueToTheLowEthernetLinkSpeed", 6),
          ("runningAtMaximumReceiveModeForChannelBandwidth", 7),
          ("limitedByTheWirelessConditions", 8),
          ("restrictedBecauseFullCapabilityTrialLicenseExpired", 9))
    )


_ReceiveModulationModeDetailLinked_Type.__name__ = "Integer32"
_ReceiveModulationModeDetailLinked_Object = MibScalar
receiveModulationModeDetailLinked = _ReceiveModulationModeDetailLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 7),
    _ReceiveModulationModeDetailLinked_Type()
)
receiveModulationModeDetailLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveModulationModeDetailLinked.setStatus("current")


class _DataBridgingAvailabilityLinked_Type(Integer32):
    """Custom type dataBridgingAvailabilityLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_DataBridgingAvailabilityLinked_Type.__name__ = "Integer32"
_DataBridgingAvailabilityLinked_Object = MibScalar
dataBridgingAvailabilityLinked = _DataBridgingAvailabilityLinked_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 8),
    _DataBridgingAvailabilityLinked_Type()
)
dataBridgingAvailabilityLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataBridgingAvailabilityLinked.setStatus("current")


class _PubInstancedStatsTableNumber_Type(Integer32):
    """Custom type pubInstancedStatsTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PubInstancedStatsTableNumber_Type.__name__ = "Integer32"
_PubInstancedStatsTableNumber_Object = MibScalar
pubInstancedStatsTableNumber = _PubInstancedStatsTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 9),
    _PubInstancedStatsTableNumber_Type()
)
pubInstancedStatsTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pubInstancedStatsTableNumber.setStatus("current")
_PubInstancedStatsTable_Object = MibTable
pubInstancedStatsTable = _PubInstancedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10)
)
if mibBuilder.loadTexts:
    pubInstancedStatsTable.setStatus("current")
_PubInstancedStatsTableEntry_Object = MibTableRow
pubInstancedStatsTableEntry = _PubInstancedStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1)
)
pubInstancedStatsTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "pubInstancedStatsTableIndex"),
)
if mibBuilder.loadTexts:
    pubInstancedStatsTableEntry.setStatus("current")


class _PubInstancedStatsTableIndex_Type(Integer32):
    """Custom type pubInstancedStatsTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PubInstancedStatsTableIndex_Type.__name__ = "Integer32"
_PubInstancedStatsTableIndex_Object = MibTableColumn
pubInstancedStatsTableIndex = _PubInstancedStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1, 1),
    _PubInstancedStatsTableIndex_Type()
)
pubInstancedStatsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pubInstancedStatsTableIndex.setStatus("current")
_ReceiveDataRate_Type = Integer32
_ReceiveDataRate_Object = MibTableColumn
receiveDataRate = _ReceiveDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1, 2),
    _ReceiveDataRate_Type()
)
receiveDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveDataRate.setStatus("current")
_TransmitDataRate_Type = Integer32
_TransmitDataRate_Object = MibTableColumn
transmitDataRate = _TransmitDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1, 3),
    _TransmitDataRate_Type()
)
transmitDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitDataRate.setStatus("current")
_AggregateDataRate_Type = Integer32
_AggregateDataRate_Object = MibTableColumn
aggregateDataRate = _AggregateDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1, 4),
    _AggregateDataRate_Type()
)
aggregateDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggregateDataRate.setStatus("current")


class _WirelessLinkAvailability_Type(Integer32):
    """Custom type wirelessLinkAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_WirelessLinkAvailability_Type.__name__ = "Integer32"
_WirelessLinkAvailability_Object = MibTableColumn
wirelessLinkAvailability = _WirelessLinkAvailability_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1, 5),
    _WirelessLinkAvailability_Type()
)
wirelessLinkAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkAvailability.setStatus("current")


class _WirelessLinkStatus_Type(Integer32):
    """Custom type wirelessLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("registering", 1),
          ("searching", 2),
          ("acquiring", 3),
          ("radarCAC", 4),
          ("initialising", 5))
    )


_WirelessLinkStatus_Type.__name__ = "Integer32"
_WirelessLinkStatus_Object = MibTableColumn
wirelessLinkStatus = _WirelessLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1, 6),
    _WirelessLinkStatus_Type()
)
wirelessLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatus.setStatus("current")


class _ReceiveModulationModeDetail_Type(Integer32):
    """Custom type receiveModulationModeDetail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("runningAtMaximumReceiveMode", 0),
          ("runningAtUserConfiguredMaxModulationMode", 1),
          ("restrictedBecauseInstallationIsArmed", 2),
          ("restrictedBecauseOfByteErrorsOnTheWirelessLink", 3),
          ("restrictedBecauseTheLinkParametersAreUpdating", 4),
          ("restrictedBecauseChannelChangeIsInProgress", 5),
          ("restrictedDueToTheLowEthernetLinkSpeed", 6),
          ("runningAtMaximumReceiveModeForChannelBandwidth", 7),
          ("limitedByTheWirelessConditions", 8),
          ("restrictedBecauseFullCapabilityTrialLicenseExpired", 9),
          ("acquiringLink", 10))
    )


_ReceiveModulationModeDetail_Type.__name__ = "Integer32"
_ReceiveModulationModeDetail_Object = MibTableColumn
receiveModulationModeDetail = _ReceiveModulationModeDetail_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1, 7),
    _ReceiveModulationModeDetail_Type()
)
receiveModulationModeDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveModulationModeDetail.setStatus("current")


class _DataBridgingAvailability_Type(Integer32):
    """Custom type dataBridgingAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_DataBridgingAvailability_Type.__name__ = "Integer32"
_DataBridgingAvailability_Object = MibTableColumn
dataBridgingAvailability = _DataBridgingAvailability_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1, 8),
    _DataBridgingAvailability_Type()
)
dataBridgingAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataBridgingAvailability.setStatus("current")
_ByteErrorRatio_Type = Integer32
_ByteErrorRatio_Object = MibTableColumn
byteErrorRatio = _ByteErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1, 9),
    _ByteErrorRatio_Type()
)
byteErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    byteErrorRatio.setStatus("current")
_WirelessOutEthernetOctets_Type = Counter64
_WirelessOutEthernetOctets_Object = MibTableColumn
wirelessOutEthernetOctets = _WirelessOutEthernetOctets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1, 10),
    _WirelessOutEthernetOctets_Type()
)
wirelessOutEthernetOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessOutEthernetOctets.setStatus("current")
_WirelessOutAllOctets_Type = Counter64
_WirelessOutAllOctets_Object = MibTableColumn
wirelessOutAllOctets = _WirelessOutAllOctets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1, 11),
    _WirelessOutAllOctets_Type()
)
wirelessOutAllOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessOutAllOctets.setStatus("current")
_WirelessOutOctets_Type = Counter64
_WirelessOutOctets_Object = MibTableColumn
wirelessOutOctets = _WirelessOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1, 12),
    _WirelessOutOctets_Type()
)
wirelessOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessOutOctets.setStatus("current")
_ErroredSeconds_Type = Integer32
_ErroredSeconds_Object = MibTableColumn
erroredSeconds = _ErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1, 13),
    _ErroredSeconds_Type()
)
erroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erroredSeconds.setStatus("current")
_SeverelyErroredSeconds_Type = Integer32
_SeverelyErroredSeconds_Object = MibTableColumn
severelyErroredSeconds = _SeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1, 14),
    _SeverelyErroredSeconds_Type()
)
severelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severelyErroredSeconds.setStatus("current")
_UnavailableSeconds_Type = Integer32
_UnavailableSeconds_Object = MibTableColumn
unavailableSeconds = _UnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 20, 10, 1, 15),
    _UnavailableSeconds_Type()
)
unavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unavailableSeconds.setStatus("current")
_Encryption_ObjectIdentity = ObjectIdentity
encryption = _Encryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 22)
)


class _EncryptionAlgorithm_Type(Integer32):
    """Custom type encryptionAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pSKAES128bit", 1),
          ("pSKAES192bit", 2),
          ("pSKAES256bit", 3),
          ("tLSRSA", 4),
          ("tLSPSK128bit", 5),
          ("tLSPSK256bit", 6))
    )


_EncryptionAlgorithm_Type.__name__ = "Integer32"
_EncryptionAlgorithm_Object = MibScalar
encryptionAlgorithm = _EncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 22, 1),
    _EncryptionAlgorithm_Type()
)
encryptionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionAlgorithm.setStatus("current")


class _TLSMinimumSecurityLevel_Type(Integer32):
    """Custom type tLSMinimumSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("aES128bitTLSRSA", 1),
          ("aES256bitTLSRSA", 2))
    )


_TLSMinimumSecurityLevel_Type.__name__ = "Integer32"
_TLSMinimumSecurityLevel_Object = MibScalar
tLSMinimumSecurityLevel = _TLSMinimumSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 22, 2),
    _TLSMinimumSecurityLevel_Type()
)
tLSMinimumSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tLSMinimumSecurityLevel.setStatus("current")
_TDDControl_ObjectIdentity = ObjectIdentity
tDDControl = _TDDControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 23)
)


class _TDDSynchronizationMode_Type(Integer32):
    """Custom type tDDSynchronizationMode based on Integer32"""
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


_TDDSynchronizationMode_Type.__name__ = "Integer32"
_TDDSynchronizationMode_Object = MibScalar
tDDSynchronizationMode = _TDDSynchronizationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 23, 1),
    _TDDSynchronizationMode_Type()
)
tDDSynchronizationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDDSynchronizationMode.setStatus("current")


class _HCMPMaximumLinkRange_Type(Integer32):
    """Custom type hCMPMaximumLinkRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1000),
    )


_HCMPMaximumLinkRange_Type.__name__ = "Integer32"
_HCMPMaximumLinkRange_Object = MibScalar
hCMPMaximumLinkRange = _HCMPMaximumLinkRange_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 23, 2),
    _HCMPMaximumLinkRange_Type()
)
hCMPMaximumLinkRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hCMPMaximumLinkRange.setStatus("current")


class _MaximumNumberOfSlaves_Type(Integer32):
    """Custom type maximumNumberOfSlaves based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MaximumNumberOfSlaves_Type.__name__ = "Integer32"
_MaximumNumberOfSlaves_Object = MibScalar
maximumNumberOfSlaves = _MaximumNumberOfSlaves_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 23, 3),
    _MaximumNumberOfSlaves_Type()
)
maximumNumberOfSlaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumNumberOfSlaves.setStatus("current")


class _HCMPLinkSymmetry_Type(Integer32):
    """Custom type hCMPLinkSymmetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("symmetry4to1", 0),
          ("symmetry3to1", 1),
          ("symmetry2to1", 2),
          ("symmetry1to1", 3),
          ("symmetry1to2", 4),
          ("symmetry1to3", 5),
          ("symmetry1to4", 6))
    )


_HCMPLinkSymmetry_Type.__name__ = "Integer32"
_HCMPLinkSymmetry_Object = MibScalar
hCMPLinkSymmetry = _HCMPLinkSymmetry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 23, 4),
    _HCMPLinkSymmetry_Type()
)
hCMPLinkSymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hCMPLinkSymmetry.setStatus("current")
_SyslogControl_ObjectIdentity = ObjectIdentity
syslogControl = _SyslogControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 24)
)


class _SyslogClient_Type(Integer32):
    """Custom type syslogClient based on Integer32"""
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


_SyslogClient_Type.__name__ = "Integer32"
_SyslogClient_Object = MibScalar
syslogClient = _SyslogClient_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 24, 1),
    _SyslogClient_Type()
)
syslogClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogClient.setStatus("current")


class _SyslogState_Type(Integer32):
    """Custom type syslogState based on Integer32"""
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


_SyslogState_Type.__name__ = "Integer32"
_SyslogState_Object = MibScalar
syslogState = _SyslogState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 24, 2),
    _SyslogState_Type()
)
syslogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogState.setStatus("current")
_AAAControl_ObjectIdentity = ObjectIdentity
aAAControl = _AAAControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 25)
)


class _UserTableNumber_Type(Integer32):
    """Custom type userTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_UserTableNumber_Type.__name__ = "Integer32"
_UserTableNumber_Object = MibScalar
userTableNumber = _UserTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 25, 1),
    _UserTableNumber_Type()
)
userTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userTableNumber.setStatus("current")
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 25, 2)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserTableEntry_Object = MibTableRow
userTableEntry = _UserTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 25, 2, 1)
)
userTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "userTableIndex"),
)
if mibBuilder.loadTexts:
    userTableEntry.setStatus("current")


class _UserTableIndex_Type(Integer32):
    """Custom type userTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_UserTableIndex_Type.__name__ = "Integer32"
_UserTableIndex_Object = MibTableColumn
userTableIndex = _UserTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 25, 2, 1, 1),
    _UserTableIndex_Type()
)
userTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userTableIndex.setStatus("current")


class _UserName_Type(DisplayString):
    """Custom type userName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 67),
    )


_UserName_Type.__name__ = "DisplayString"
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 25, 2, 1, 2),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _UserRole_Type(Integer32):
    """Custom type userRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 0),
          ("systemAdministrator", 1),
          ("securityOfficer", 2))
    )


_UserRole_Type.__name__ = "Integer32"
_UserRole_Object = MibTableColumn
userRole = _UserRole_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 25, 2, 1, 3),
    _UserRole_Type()
)
userRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userRole.setStatus("current")


class _UserEnabled_Type(Integer32):
    """Custom type userEnabled based on Integer32"""
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


_UserEnabled_Type.__name__ = "Integer32"
_UserEnabled_Object = MibTableColumn
userEnabled = _UserEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 25, 2, 1, 4),
    _UserEnabled_Type()
)
userEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userEnabled.setStatus("current")


class _UserPassword_Type(DisplayString):
    """Custom type userPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 67),
    )


_UserPassword_Type.__name__ = "DisplayString"
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 25, 2, 1, 5),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPassword.setStatus("current")
_RouterProtocols_ObjectIdentity = ObjectIdentity
routerProtocols = _RouterProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 26)
)


class _MicrowaveAdaptiveBandwidth_Type(Integer32):
    """Custom type microwaveAdaptiveBandwidth based on Integer32"""
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


_MicrowaveAdaptiveBandwidth_Type.__name__ = "Integer32"
_MicrowaveAdaptiveBandwidth_Object = MibScalar
microwaveAdaptiveBandwidth = _MicrowaveAdaptiveBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 26, 1),
    _MicrowaveAdaptiveBandwidth_Type()
)
microwaveAdaptiveBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    microwaveAdaptiveBandwidth.setStatus("current")


class _MABNominalModulationMode_Type(Integer32):
    """Custom type mABNominalModulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("modAcquisition", 0),
          ("modBpsk63percent", 1),
          ("modQpsk63percentSingle", 2),
          ("modTransient1", 3),
          ("modQpsk87percentSingle", 4),
          ("modTransient2", 5),
          ("mod16qam63percentSingleA", 6),
          ("modTransient3", 7),
          ("mod16qam87percentSingle", 8),
          ("modTransient4", 9),
          ("mod64qam75percentSingle", 10),
          ("modTransient5", 11),
          ("mod64qam92percentSingle", 12),
          ("modTransient6", 13),
          ("mod256qam81percentSingle", 14),
          ("mod16qam63percentSingleB", 15),
          ("mod16qam63percentDual", 16),
          ("modTransient7", 17),
          ("mod16qam87percentDual", 18),
          ("modTransient8", 19),
          ("mod64qam75percentDual", 20),
          ("modTransient9", 21),
          ("mod64qam92percentDual", 22),
          ("modTransient10", 23),
          ("mod256qam81percentDual", 24))
    )


_MABNominalModulationMode_Type.__name__ = "Integer32"
_MABNominalModulationMode_Object = MibScalar
mABNominalModulationMode = _MABNominalModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 26, 2),
    _MABNominalModulationMode_Type()
)
mABNominalModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABNominalModulationMode.setStatus("current")


class _MABTransmissionInterval_Type(Integer32):
    """Custom type mABTransmissionInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transmissionInterval1s", 0),
          ("transmissionInterval10s", 1),
          ("transmissionInterval60s", 2))
    )


_MABTransmissionInterval_Type.__name__ = "Integer32"
_MABTransmissionInterval_Object = MibScalar
mABTransmissionInterval = _MABTransmissionInterval_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 26, 3),
    _MABTransmissionInterval_Type()
)
mABTransmissionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABTransmissionInterval.setStatus("current")


class _MABHoldoffPeriod_Type(Integer32):
    """Custom type mABHoldoffPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_MABHoldoffPeriod_Type.__name__ = "Integer32"
_MABHoldoffPeriod_Object = MibScalar
mABHoldoffPeriod = _MABHoldoffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 26, 4),
    _MABHoldoffPeriod_Type()
)
mABHoldoffPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABHoldoffPeriod.setStatus("current")


class _MABMaintenanceLevel_Type(Integer32):
    """Custom type mABMaintenanceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MABMaintenanceLevel_Type.__name__ = "Integer32"
_MABMaintenanceLevel_Object = MibScalar
mABMaintenanceLevel = _MABMaintenanceLevel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 26, 5),
    _MABMaintenanceLevel_Type()
)
mABMaintenanceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABMaintenanceLevel.setStatus("current")


class _UseVLANForMABProtocol_Type(Integer32):
    """Custom type useVLANForMABProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noVLANTagging", 0),
          ("iEEE8021QTaggedCTagType8100", 1))
    )


_UseVLANForMABProtocol_Type.__name__ = "Integer32"
_UseVLANForMABProtocol_Object = MibScalar
useVLANForMABProtocol = _UseVLANForMABProtocol_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 26, 6),
    _UseVLANForMABProtocol_Type()
)
useVLANForMABProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    useVLANForMABProtocol.setStatus("current")


class _MABProtocolVID_Type(Integer32):
    """Custom type mABProtocolVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MABProtocolVID_Type.__name__ = "Integer32"
_MABProtocolVID_Object = MibScalar
mABProtocolVID = _MABProtocolVID_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 26, 7),
    _MABProtocolVID_Type()
)
mABProtocolVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABProtocolVID.setStatus("current")


class _MABProtocolVLANPriority_Type(Integer32):
    """Custom type mABProtocolVLANPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MABProtocolVLANPriority_Type.__name__ = "Integer32"
_MABProtocolVLANPriority_Object = MibScalar
mABProtocolVLANPriority = _MABProtocolVLANPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 26, 8),
    _MABProtocolVLANPriority_Type()
)
mABProtocolVLANPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABProtocolVLANPriority.setStatus("current")


class _MABState_Type(Integer32):
    """Custom type mABState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("degraded", 1))
    )


_MABState_Type.__name__ = "Integer32"
_MABState_Object = MibScalar
mABState = _MABState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 26, 9),
    _MABState_Type()
)
mABState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABState.setStatus("current")


class _MABNominalTransmitCapacity_Type(Integer32):
    """Custom type mABNominalTransmitCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MABNominalTransmitCapacity_Type.__name__ = "Integer32"
_MABNominalTransmitCapacity_Object = MibScalar
mABNominalTransmitCapacity = _MABNominalTransmitCapacity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 26, 10),
    _MABNominalTransmitCapacity_Type()
)
mABNominalTransmitCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABNominalTransmitCapacity.setStatus("current")


class _MABCurrentTransmitCapacity_Type(Integer32):
    """Custom type mABCurrentTransmitCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MABCurrentTransmitCapacity_Type.__name__ = "Integer32"
_MABCurrentTransmitCapacity_Object = MibScalar
mABCurrentTransmitCapacity = _MABCurrentTransmitCapacity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 26, 11),
    _MABCurrentTransmitCapacity_Type()
)
mABCurrentTransmitCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mABCurrentTransmitCapacity.setStatus("current")
_CableDiagnostics_ObjectIdentity = ObjectIdentity
cableDiagnostics = _CableDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27)
)


class _CableDiagnosticsPorts_Type(Bits):
    """Custom type cableDiagnosticsPorts based on Bits"""
    namedValues = NamedValues(
        *(("auxPort", 6),
          ("mainPSUPort", 7))
    )

_CableDiagnosticsPorts_Type.__name__ = "Bits"
_CableDiagnosticsPorts_Object = MibScalar
cableDiagnosticsPorts = _CableDiagnosticsPorts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 1),
    _CableDiagnosticsPorts_Type()
)
cableDiagnosticsPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableDiagnosticsPorts.setStatus("current")


class _CableDiagnosticsControl_Type(Integer32):
    """Custom type cableDiagnosticsControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("startTest", 0),
          ("testInProgress", 1))
    )


_CableDiagnosticsControl_Type.__name__ = "Integer32"
_CableDiagnosticsControl_Object = MibScalar
cableDiagnosticsControl = _CableDiagnosticsControl_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 2),
    _CableDiagnosticsControl_Type()
)
cableDiagnosticsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableDiagnosticsControl.setStatus("current")


class _CableDiagnosticsWarning_Type(Integer32):
    """Custom type cableDiagnosticsWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("testInProgress", 1))
    )


_CableDiagnosticsWarning_Type.__name__ = "Integer32"
_CableDiagnosticsWarning_Object = MibScalar
cableDiagnosticsWarning = _CableDiagnosticsWarning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 3),
    _CableDiagnosticsWarning_Type()
)
cableDiagnosticsWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagnosticsWarning.setStatus("current")


class _CableDiagnosticsResultTableNumber_Type(Integer32):
    """Custom type cableDiagnosticsResultTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CableDiagnosticsResultTableNumber_Type.__name__ = "Integer32"
_CableDiagnosticsResultTableNumber_Object = MibScalar
cableDiagnosticsResultTableNumber = _CableDiagnosticsResultTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 4),
    _CableDiagnosticsResultTableNumber_Type()
)
cableDiagnosticsResultTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagnosticsResultTableNumber.setStatus("current")
_CableDiagnosticsResultTable_Object = MibTable
cableDiagnosticsResultTable = _CableDiagnosticsResultTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 5)
)
if mibBuilder.loadTexts:
    cableDiagnosticsResultTable.setStatus("current")
_CableDiagnosticsResultTableEntry_Object = MibTableRow
cableDiagnosticsResultTableEntry = _CableDiagnosticsResultTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 5, 1)
)
cableDiagnosticsResultTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "cableDiagnosticsResultTableIndex"),
)
if mibBuilder.loadTexts:
    cableDiagnosticsResultTableEntry.setStatus("current")


class _CableDiagnosticsResultTableIndex_Type(Integer32):
    """Custom type cableDiagnosticsResultTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CableDiagnosticsResultTableIndex_Type.__name__ = "Integer32"
_CableDiagnosticsResultTableIndex_Object = MibTableColumn
cableDiagnosticsResultTableIndex = _CableDiagnosticsResultTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 5, 1, 1),
    _CableDiagnosticsResultTableIndex_Type()
)
cableDiagnosticsResultTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cableDiagnosticsResultTableIndex.setStatus("current")
_CableDiagnosticsResultsDateTime_Type = Integer32
_CableDiagnosticsResultsDateTime_Object = MibTableColumn
cableDiagnosticsResultsDateTime = _CableDiagnosticsResultsDateTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 5, 1, 2),
    _CableDiagnosticsResultsDateTime_Type()
)
cableDiagnosticsResultsDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagnosticsResultsDateTime.setStatus("current")


class _CableDiagPair1Results_Type(Integer32):
    """Custom type cableDiagPair1Results based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("unknown", 1),
          ("inProgress", 2),
          ("notTested", 3),
          ("openCircuit", 4),
          ("shortCircuit", 5))
    )


_CableDiagPair1Results_Type.__name__ = "Integer32"
_CableDiagPair1Results_Object = MibTableColumn
cableDiagPair1Results = _CableDiagPair1Results_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 5, 1, 3),
    _CableDiagPair1Results_Type()
)
cableDiagPair1Results.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair1Results.setStatus("current")
_CableDiagPair1Distance_Type = Integer32
_CableDiagPair1Distance_Object = MibTableColumn
cableDiagPair1Distance = _CableDiagPair1Distance_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 5, 1, 4),
    _CableDiagPair1Distance_Type()
)
cableDiagPair1Distance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair1Distance.setStatus("current")


class _CableDiagPair2Results_Type(Integer32):
    """Custom type cableDiagPair2Results based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("unknown", 1),
          ("inProgress", 2),
          ("notTested", 3),
          ("openCircuit", 4),
          ("shortCircuit", 5))
    )


_CableDiagPair2Results_Type.__name__ = "Integer32"
_CableDiagPair2Results_Object = MibTableColumn
cableDiagPair2Results = _CableDiagPair2Results_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 5, 1, 5),
    _CableDiagPair2Results_Type()
)
cableDiagPair2Results.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair2Results.setStatus("current")
_CableDiagPair2Distance_Type = Integer32
_CableDiagPair2Distance_Object = MibTableColumn
cableDiagPair2Distance = _CableDiagPair2Distance_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 5, 1, 6),
    _CableDiagPair2Distance_Type()
)
cableDiagPair2Distance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair2Distance.setStatus("current")


class _CableDiagPair3Results_Type(Integer32):
    """Custom type cableDiagPair3Results based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("unknown", 1),
          ("inProgress", 2),
          ("notTested", 3),
          ("openCircuit", 4),
          ("shortCircuit", 5))
    )


_CableDiagPair3Results_Type.__name__ = "Integer32"
_CableDiagPair3Results_Object = MibTableColumn
cableDiagPair3Results = _CableDiagPair3Results_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 5, 1, 7),
    _CableDiagPair3Results_Type()
)
cableDiagPair3Results.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair3Results.setStatus("current")
_CableDiagPair3Distance_Type = Integer32
_CableDiagPair3Distance_Object = MibTableColumn
cableDiagPair3Distance = _CableDiagPair3Distance_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 5, 1, 8),
    _CableDiagPair3Distance_Type()
)
cableDiagPair3Distance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair3Distance.setStatus("current")


class _CableDiagPair4Results_Type(Integer32):
    """Custom type cableDiagPair4Results based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("unknown", 1),
          ("inProgress", 2),
          ("notTested", 3),
          ("openCircuit", 4),
          ("shortCircuit", 5))
    )


_CableDiagPair4Results_Type.__name__ = "Integer32"
_CableDiagPair4Results_Object = MibTableColumn
cableDiagPair4Results = _CableDiagPair4Results_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 5, 1, 9),
    _CableDiagPair4Results_Type()
)
cableDiagPair4Results.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair4Results.setStatus("current")
_CableDiagPair4Distance_Type = Integer32
_CableDiagPair4Distance_Object = MibTableColumn
cableDiagPair4Distance = _CableDiagPair4Distance_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 27, 5, 1, 10),
    _CableDiagPair4Distance_Type()
)
cableDiagPair4Distance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagPair4Distance.setStatus("current")
_UnitIdentification_ObjectIdentity = ObjectIdentity
unitIdentification = _UnitIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 28)
)


class _DeviceMACAddress_Type(OctetString):
    """Custom type deviceMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_DeviceMACAddress_Type.__name__ = "OctetString"
_DeviceMACAddress_Object = MibScalar
deviceMACAddress = _DeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 28, 1),
    _DeviceMACAddress_Type()
)
deviceMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMACAddress.setStatus("current")


class _DeviceESN_Type(DisplayString):
    """Custom type deviceESN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DeviceESN_Type.__name__ = "DisplayString"
_DeviceESN_Object = MibScalar
deviceESN = _DeviceESN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 28, 2),
    _DeviceESN_Type()
)
deviceESN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceESN.setStatus("current")


class _DeviceMSN_Type(DisplayString):
    """Custom type deviceMSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DeviceMSN_Type.__name__ = "DisplayString"
_DeviceMSN_Object = MibScalar
deviceMSN = _DeviceMSN_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 28, 3),
    _DeviceMSN_Type()
)
deviceMSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMSN.setStatus("current")
_AuthorizationControl_ObjectIdentity = ObjectIdentity
authorizationControl = _AuthorizationControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 29)
)


class _AuthorizationControlTableNumber_Type(Integer32):
    """Custom type authorizationControlTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AuthorizationControlTableNumber_Type.__name__ = "Integer32"
_AuthorizationControlTableNumber_Object = MibScalar
authorizationControlTableNumber = _AuthorizationControlTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 29, 1),
    _AuthorizationControlTableNumber_Type()
)
authorizationControlTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authorizationControlTableNumber.setStatus("current")
_AuthorizationControlTable_Object = MibTable
authorizationControlTable = _AuthorizationControlTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 29, 2)
)
if mibBuilder.loadTexts:
    authorizationControlTable.setStatus("current")
_AuthorizationControlTableEntry_Object = MibTableRow
authorizationControlTableEntry = _AuthorizationControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 29, 2, 1)
)
authorizationControlTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "authorizationControlTableIndex"),
)
if mibBuilder.loadTexts:
    authorizationControlTableEntry.setStatus("current")


class _AuthorizationControlTableIndex_Type(Integer32):
    """Custom type authorizationControlTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AuthorizationControlTableIndex_Type.__name__ = "Integer32"
_AuthorizationControlTableIndex_Object = MibTableColumn
authorizationControlTableIndex = _AuthorizationControlTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 29, 2, 1, 1),
    _AuthorizationControlTableIndex_Type()
)
authorizationControlTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    authorizationControlTableIndex.setStatus("current")


class _WhitelistRMMacAddress_Type(OctetString):
    """Custom type whitelistRMMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_WhitelistRMMacAddress_Type.__name__ = "OctetString"
_WhitelistRMMacAddress_Object = MibTableColumn
whitelistRMMacAddress = _WhitelistRMMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 29, 2, 1, 2),
    _WhitelistRMMacAddress_Type()
)
whitelistRMMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    whitelistRMMacAddress.setStatus("current")


class _WhitelistRMEnabled_Type(Integer32):
    """Custom type whitelistRMEnabled based on Integer32"""
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


_WhitelistRMEnabled_Type.__name__ = "Integer32"
_WhitelistRMEnabled_Object = MibTableColumn
whitelistRMEnabled = _WhitelistRMEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 29, 2, 1, 3),
    _WhitelistRMEnabled_Type()
)
whitelistRMEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    whitelistRMEnabled.setStatus("current")


class _BlacklistRMMacAddress_Type(OctetString):
    """Custom type blacklistRMMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_BlacklistRMMacAddress_Type.__name__ = "OctetString"
_BlacklistRMMacAddress_Object = MibTableColumn
blacklistRMMacAddress = _BlacklistRMMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 29, 2, 1, 4),
    _BlacklistRMMacAddress_Type()
)
blacklistRMMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blacklistRMMacAddress.setStatus("current")


class _BlacklistRMEnabled_Type(Integer32):
    """Custom type blacklistRMEnabled based on Integer32"""
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


_BlacklistRMEnabled_Type.__name__ = "Integer32"
_BlacklistRMEnabled_Object = MibTableColumn
blacklistRMEnabled = _BlacklistRMEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 29, 2, 1, 5),
    _BlacklistRMEnabled_Type()
)
blacklistRMEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blacklistRMEnabled.setStatus("current")
_DNS_ObjectIdentity = ObjectIdentity
dNS = _DNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 30)
)


class _DNSResolver_Type(Integer32):
    """Custom type dNSResolver based on Integer32"""
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


_DNSResolver_Type.__name__ = "Integer32"
_DNSResolver_Object = MibScalar
dNSResolver = _DNSResolver_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 30, 1),
    _DNSResolver_Type()
)
dNSResolver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNSResolver.setStatus("current")


class _DNSPrimaryServer_Type(Integer32):
    """Custom type dNSPrimaryServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("server1", 0),
          ("server2", 1))
    )


_DNSPrimaryServer_Type.__name__ = "Integer32"
_DNSPrimaryServer_Object = MibScalar
dNSPrimaryServer = _DNSPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 30, 2),
    _DNSPrimaryServer_Type()
)
dNSPrimaryServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dNSPrimaryServer.setStatus("current")


class _DNSServerTableNumber_Type(Integer32):
    """Custom type dNSServerTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_DNSServerTableNumber_Type.__name__ = "Integer32"
_DNSServerTableNumber_Object = MibScalar
dNSServerTableNumber = _DNSServerTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 30, 3),
    _DNSServerTableNumber_Type()
)
dNSServerTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dNSServerTableNumber.setStatus("current")
_DNSServerTable_Object = MibTable
dNSServerTable = _DNSServerTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 30, 4)
)
if mibBuilder.loadTexts:
    dNSServerTable.setStatus("current")
_DNSServerTableEntry_Object = MibTableRow
dNSServerTableEntry = _DNSServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 30, 4, 1)
)
dNSServerTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP670-MIB", "dNSServerTableIndex"),
)
if mibBuilder.loadTexts:
    dNSServerTableEntry.setStatus("current")


class _DNSServerTableIndex_Type(Integer32):
    """Custom type dNSServerTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DNSServerTableIndex_Type.__name__ = "Integer32"
_DNSServerTableIndex_Object = MibTableColumn
dNSServerTableIndex = _DNSServerTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 30, 4, 1, 1),
    _DNSServerTableIndex_Type()
)
dNSServerTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dNSServerTableIndex.setStatus("current")


class _DNSServerInternetAddressType_Type(Integer32):
    """Custom type dNSServerInternetAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("ipv4z", 3),
          ("ipv6z", 4),
          ("unknown6", 5),
          ("unknown7", 6),
          ("unknown8", 7),
          ("unknown9", 8),
          ("unknown10", 9),
          ("unknown11", 10),
          ("unknown12", 11),
          ("unknown13", 12),
          ("unknown14", 13),
          ("unknown15", 14),
          ("unknown16", 15),
          ("dns", 16))
    )


_DNSServerInternetAddressType_Type.__name__ = "Integer32"
_DNSServerInternetAddressType_Object = MibTableColumn
dNSServerInternetAddressType = _DNSServerInternetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 30, 4, 1, 2),
    _DNSServerInternetAddressType_Type()
)
dNSServerInternetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dNSServerInternetAddressType.setStatus("current")
_DNSServerInternetAddress_Type = InetAddress
_DNSServerInternetAddress_Object = MibTableColumn
dNSServerInternetAddress = _DNSServerInternetAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 30, 4, 1, 3),
    _DNSServerInternetAddress_Type()
)
dNSServerInternetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNSServerInternetAddress.setStatus("current")


class _DNSServerPortNumber_Type(Integer32):
    """Custom type dNSServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_DNSServerPortNumber_Type.__name__ = "Integer32"
_DNSServerPortNumber_Object = MibTableColumn
dNSServerPortNumber = _DNSServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 30, 4, 1, 4),
    _DNSServerPortNumber_Type()
)
dNSServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dNSServerPortNumber.setStatus("current")
_Supplementary_ObjectIdentity = ObjectIdentity
supplementary = _Supplementary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 96)
)


class _Longitude_Type(DisplayString):
    """Custom type longitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_Longitude_Type.__name__ = "DisplayString"
_Longitude_Object = MibScalar
longitude = _Longitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 96, 1),
    _Longitude_Type()
)
longitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    longitude.setStatus("current")


class _Latitude_Type(DisplayString):
    """Custom type latitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_Latitude_Type.__name__ = "DisplayString"
_Latitude_Object = MibScalar
latitude = _Latitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 96, 2),
    _Latitude_Type()
)
latitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latitude.setStatus("current")
_Altitude_Type = Integer32
_Altitude_Object = MibScalar
altitude = _Altitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 11, 96, 3),
    _Altitude_Type()
)
altitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altitude.setStatus("current")
_PtpGroups_ObjectIdentity = ObjectIdentity
ptpGroups = _PtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98)
)
_PtpTraps_ObjectIdentity = ObjectIdentity
ptpTraps = _PtpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99)
)
_PtpTrapPrefix_ObjectIdentity = ObjectIdentity
ptpTrapPrefix = _PtpTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0)
)

# Managed Objects groups

dfsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 3)
)
dfsGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "dfsTableNumber"),
        ("CAMBIUM-PTP670-MIB", "extendedSpectrumScanning"),
        ("CAMBIUM-PTP670-MIB", "dfsMeans"),
        ("CAMBIUM-PTP670-MIB", "dfsNineNinePointNinePercentiles"),
        ("CAMBIUM-PTP670-MIB", "dfsPeaks"))
)
if mibBuilder.loadTexts:
    dfsGroup.setStatus("current")

bridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 4)
)
bridgeGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "localPacketFiltering"),
        ("CAMBIUM-PTP670-MIB", "packetsToInternalStack"),
        ("CAMBIUM-PTP670-MIB", "packetsFromInternalStack"))
)
if mibBuilder.loadTexts:
    bridgeGroup.setStatus("current")

configurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 5)
)
configurationGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "iPv4Address"),
        ("CAMBIUM-PTP670-MIB", "subnetMask"),
        ("CAMBIUM-PTP670-MIB", "gatewayIPAddress"),
        ("CAMBIUM-PTP670-MIB", "targetMACAddress"),
        ("CAMBIUM-PTP670-MIB", "masterSlaveMode"),
        ("CAMBIUM-PTP670-MIB", "maximumTransmitPower"),
        ("CAMBIUM-PTP670-MIB", "antennaGain"),
        ("CAMBIUM-PTP670-MIB", "cableLoss"),
        ("CAMBIUM-PTP670-MIB", "eIRP"),
        ("CAMBIUM-PTP670-MIB", "channelBandwidth"),
        ("CAMBIUM-PTP670-MIB", "linkName"),
        ("CAMBIUM-PTP670-MIB", "siteName"),
        ("CAMBIUM-PTP670-MIB", "accessMethod"),
        ("CAMBIUM-PTP670-MIB", "groupID"),
        ("CAMBIUM-PTP670-MIB", "iPv6Address"),
        ("CAMBIUM-PTP670-MIB", "iPVersion"),
        ("CAMBIUM-PTP670-MIB", "iPv6AutoConfiguredLinkLocalAddress"),
        ("CAMBIUM-PTP670-MIB", "iPv6PrefixLength"),
        ("CAMBIUM-PTP670-MIB", "iPv6GatewayAddress"),
        ("CAMBIUM-PTP670-MIB", "remoteInternetAddressTypeLinked"),
        ("CAMBIUM-PTP670-MIB", "remoteInternetAddressLinked"),
        ("CAMBIUM-PTP670-MIB", "subbandLowestFrequency"),
        ("CAMBIUM-PTP670-MIB", "subbandHighestFrequency"),
        ("CAMBIUM-PTP670-MIB", "enableTransmission"),
        ("CAMBIUM-PTP670-MIB", "antennaSelection"),
        ("CAMBIUM-PTP670-MIB", "transmitterChannels"),
        ("CAMBIUM-PTP670-MIB", "wirelessTopology"),
        ("CAMBIUM-PTP670-MIB", "configurationInstancedTableNumber"),
        ("CAMBIUM-PTP670-MIB", "unitName"),
        ("CAMBIUM-PTP670-MIB", "authorizationMethod"),
        ("CAMBIUM-PTP670-MIB", "remoteUnitNameLinked"),
        ("CAMBIUM-PTP670-MIB", "remoteInternetAddressType"),
        ("CAMBIUM-PTP670-MIB", "remoteInternetAddress"),
        ("CAMBIUM-PTP670-MIB", "remoteUnitName"))
)
if mibBuilder.loadTexts:
    configurationGroup.setStatus("current")

ethernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 6)
)
ethernetGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "mainPSUPortAutoNegotiation"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortAutoNegAdvertisement"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortAutoMdix"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortStatus"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortSpeedAndDuplex"),
        ("CAMBIUM-PTP670-MIB", "dataPortWirelessDownAlert"),
        ("CAMBIUM-PTP670-MIB", "useVLANForManagementInterfaces"),
        ("CAMBIUM-PTP670-MIB", "vLANManagementPriority"),
        ("CAMBIUM-PTP670-MIB", "vLANManagementVID"),
        ("CAMBIUM-PTP670-MIB", "auxPortStatus"),
        ("CAMBIUM-PTP670-MIB", "auxPortSpeedAndDuplex"),
        ("CAMBIUM-PTP670-MIB", "ethernetPriorityTableNumber"),
        ("CAMBIUM-PTP670-MIB", "l2CPPriorityTableNumber"),
        ("CAMBIUM-PTP670-MIB", "iPDSCPPriorityTableNumber"),
        ("CAMBIUM-PTP670-MIB", "mPLSTCPriorityTableNumber"),
        ("CAMBIUM-PTP670-MIB", "managementPortWirelessDownAlert"),
        ("CAMBIUM-PTP670-MIB", "qOSPriorityScheme"),
        ("CAMBIUM-PTP670-MIB", "unknownNetworkPriorityQueueMapping"),
        ("CAMBIUM-PTP670-MIB", "dSCPManagementPriority"),
        ("CAMBIUM-PTP670-MIB", "dataBridgingStatusLinked"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortAllocation"),
        ("CAMBIUM-PTP670-MIB", "auxPortAllocation"),
        ("CAMBIUM-PTP670-MIB", "sFPPortAllocation"),
        ("CAMBIUM-PTP670-MIB", "dataPortPauseFrames"),
        ("CAMBIUM-PTP670-MIB", "sFPPortAutoNegotiation"),
        ("CAMBIUM-PTP670-MIB", "sFPPortAutoNegAdvertisement"),
        ("CAMBIUM-PTP670-MIB", "sFPPortAutoMdix"),
        ("CAMBIUM-PTP670-MIB", "sFPPortStatus"),
        ("CAMBIUM-PTP670-MIB", "sFPPortSpeedAndDuplex"),
        ("CAMBIUM-PTP670-MIB", "auxPortPowerOverEthernetOutput"),
        ("CAMBIUM-PTP670-MIB", "auxPortPowerOverEthernetOutputStatus"),
        ("CAMBIUM-PTP670-MIB", "syncETracking"),
        ("CAMBIUM-PTP670-MIB", "syncEEquipmentClock"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortQLRxOverwrite"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortSSMTx"),
        ("CAMBIUM-PTP670-MIB", "sFPPortSSMTx"),
        ("CAMBIUM-PTP670-MIB", "auxPortSSMTx"),
        ("CAMBIUM-PTP670-MIB", "syncETrackingState"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortQLRx"),
        ("CAMBIUM-PTP670-MIB", "auxPortQLRx"),
        ("CAMBIUM-PTP670-MIB", "sFPPortQLRx"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortQLTx"),
        ("CAMBIUM-PTP670-MIB", "auxPortQLTx"),
        ("CAMBIUM-PTP670-MIB", "sFPPortQLTx"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortSyncEMasterSlaveStatus"),
        ("CAMBIUM-PTP670-MIB", "auxPortSyncEMasterSlaveStatus"),
        ("CAMBIUM-PTP670-MIB", "sFPPortSyncEMasterSlaveStatus"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortGigabitMasterSlaveStatus"),
        ("CAMBIUM-PTP670-MIB", "auxPortGigabitMasterSlaveStatus"),
        ("CAMBIUM-PTP670-MIB", "sFPPortGigabitMasterSlaveStatus"),
        ("CAMBIUM-PTP670-MIB", "transparentClock"),
        ("CAMBIUM-PTP670-MIB", "transparentClockVLAN"),
        ("CAMBIUM-PTP670-MIB", "transparentClockVID"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortAcceptedQLRx"),
        ("CAMBIUM-PTP670-MIB", "auxPortAcceptedQLRx"),
        ("CAMBIUM-PTP670-MIB", "sFPPortAcceptedQLRx"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortSyncERxStatus"),
        ("CAMBIUM-PTP670-MIB", "auxPortSyncERxStatus"),
        ("CAMBIUM-PTP670-MIB", "sFPPortSyncERxStatus"),
        ("CAMBIUM-PTP670-MIB", "nIDULanPortStatus"),
        ("CAMBIUM-PTP670-MIB", "nIDULanPortSpeedAndDuplex"),
        ("CAMBIUM-PTP670-MIB", "oOBPriorityQueueMapping"),
        ("CAMBIUM-PTP670-MIB", "nIDULanPortAutoNegotiation"),
        ("CAMBIUM-PTP670-MIB", "nIDULanPortAutoNegAdvertisement"),
        ("CAMBIUM-PTP670-MIB", "nIDULanPortAutoMdix"),
        ("CAMBIUM-PTP670-MIB", "nIDULanPortGigabitMasterSlaveStatus"),
        ("CAMBIUM-PTP670-MIB", "txMABFrames"),
        ("CAMBIUM-PTP670-MIB", "managementNetworkAccessEnabled"),
        ("CAMBIUM-PTP670-MIB", "transparentClockPort"),
        ("CAMBIUM-PTP670-MIB", "syncESlavePort"),
        ("CAMBIUM-PTP670-MIB", "sFPPortQLRxOverwrite"),
        ("CAMBIUM-PTP670-MIB", "ethernetInstancedTableNumber"),
        ("CAMBIUM-PTP670-MIB", "ethernetStatisticsTableNumber"),
        ("CAMBIUM-PTP670-MIB", "ethernetPriorityQueueMapping"),
        ("CAMBIUM-PTP670-MIB", "l2CPPriorityQueueMapping"),
        ("CAMBIUM-PTP670-MIB", "iPDSCPPriorityQueueMapping"),
        ("CAMBIUM-PTP670-MIB", "mPLSTCPriorityQueueMapping"),
        ("CAMBIUM-PTP670-MIB", "dataBridgingStatus"),
        ("CAMBIUM-PTP670-MIB", "ethernetStatisticsDataSource"),
        ("CAMBIUM-PTP670-MIB", "ethernetStatisticsRxOctets"),
        ("CAMBIUM-PTP670-MIB", "ethernetStatisticsRxFrames"),
        ("CAMBIUM-PTP670-MIB", "ethernetStatisticsRxBroadcasts"),
        ("CAMBIUM-PTP670-MIB", "ethernetStatisticsRxFramesWithError"),
        ("CAMBIUM-PTP670-MIB", "ethernetStatisticsRxFramesUndersize"),
        ("CAMBIUM-PTP670-MIB", "ethernetStatisticsRxFramesOversize"),
        ("CAMBIUM-PTP670-MIB", "ethernetStatisticsTxOctets"),
        ("CAMBIUM-PTP670-MIB", "ethernetStatisticsTxFrames"),
        ("CAMBIUM-PTP670-MIB", "ethernetStatisticsTxBroadcasts"))
)
if mibBuilder.loadTexts:
    ethernetGroup.setStatus("current")

tDMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 7)
)
tDMGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "tDMInterfaceControl"),
        ("CAMBIUM-PTP670-MIB", "tDMInterfaceStatus"),
        ("CAMBIUM-PTP670-MIB", "tDMEnabledChannels"),
        ("CAMBIUM-PTP670-MIB", "tdmTableNumber"),
        ("CAMBIUM-PTP670-MIB", "tDMConfigurationMismatch"),
        ("CAMBIUM-PTP670-MIB", "lowestTDMModulationMode"),
        ("CAMBIUM-PTP670-MIB", "tDMChannelStatus"),
        ("CAMBIUM-PTP670-MIB", "tDMChannelLineCode"),
        ("CAMBIUM-PTP670-MIB", "tDMChannelCableLength"),
        ("CAMBIUM-PTP670-MIB", "tDMChannelLoopback"))
)
if mibBuilder.loadTexts:
    tDMGroup.setStatus("current")

licenseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 8)
)
licenseGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "regulatoryBand"),
        ("CAMBIUM-PTP670-MIB", "productVariant"),
        ("CAMBIUM-PTP670-MIB", "productName"),
        ("CAMBIUM-PTP670-MIB", "frequencyVariant"),
        ("CAMBIUM-PTP670-MIB", "sNMPv3Enable"),
        ("CAMBIUM-PTP670-MIB", "licenseVersion"),
        ("CAMBIUM-PTP670-MIB", "licenseUnitSerialNumber"),
        ("CAMBIUM-PTP670-MIB", "licenseIssueNumber"),
        ("CAMBIUM-PTP670-MIB", "licenseCountry"),
        ("CAMBIUM-PTP670-MIB", "licenseNumberOfRegulatoryBands"),
        ("CAMBIUM-PTP670-MIB", "licenseBandwidthCap"),
        ("CAMBIUM-PTP670-MIB", "licenseEncryption"),
        ("CAMBIUM-PTP670-MIB", "licenseSecurityLevel"),
        ("CAMBIUM-PTP670-MIB", "licenseGroupAccess"),
        ("CAMBIUM-PTP670-MIB", "licenseOOBManagementSupport"),
        ("CAMBIUM-PTP670-MIB", "licenseSFPPortSupport"),
        ("CAMBIUM-PTP670-MIB", "licenseAuxiliaryPortSupport"),
        ("CAMBIUM-PTP670-MIB", "licenseCapacity"),
        ("CAMBIUM-PTP670-MIB", "licenseMaxNumberOfTDMChannels"),
        ("CAMBIUM-PTP670-MIB", "licenseIEEE1588Support"),
        ("CAMBIUM-PTP670-MIB", "licenseSyncESupport"),
        ("CAMBIUM-PTP670-MIB", "licenseIPv6Support"),
        ("CAMBIUM-PTP670-MIB", "licenseMinimumFirmwareVersion"),
        ("CAMBIUM-PTP670-MIB", "licenseFullCapabilityTrialStatus"),
        ("CAMBIUM-PTP670-MIB", "licenseRemainingTrialPeriod"),
        ("CAMBIUM-PTP670-MIB", "licenseRemainingTrialPeriodAlarm"),
        ("CAMBIUM-PTP670-MIB", "capacityVariantMismatchLinked"),
        ("CAMBIUM-PTP670-MIB", "licenseTDDSyncSupport"),
        ("CAMBIUM-PTP670-MIB", "licenseMaxLinkRange"),
        ("CAMBIUM-PTP670-MIB", "licenseTrialPeriod"),
        ("CAMBIUM-PTP670-MIB", "licenseRARSupport"),
        ("CAMBIUM-PTP670-MIB", "licenseGasGroup"),
        ("CAMBIUM-PTP670-MIB", "licenseLongMinimumFirmwareVersion"),
        ("CAMBIUM-PTP670-MIB", "licenseHCMPSupport"),
        ("CAMBIUM-PTP670-MIB", "licenseInstancedTableNumber"),
        ("CAMBIUM-PTP670-MIB", "licenseTLSRekey"),
        ("CAMBIUM-PTP670-MIB", "licenseAdvanceHCMPSupport"),
        ("CAMBIUM-PTP670-MIB", "licenseMinFirmwareVersionPTP650Emulation"),
        ("CAMBIUM-PTP670-MIB", "capacityVariantMismatch"),
        ("CAMBIUM-PTP670-MIB", "licenseRegulatoryBandsList"))
)
if mibBuilder.loadTexts:
    licenseGroup.setStatus("current")

managementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 9)
)
managementGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "targetRange"),
        ("CAMBIUM-PTP670-MIB", "rangingMode"),
        ("CAMBIUM-PTP670-MIB", "installStatusLinked"),
        ("CAMBIUM-PTP670-MIB", "installArmState"),
        ("CAMBIUM-PTP670-MIB", "tFTPServerPortNumber"),
        ("CAMBIUM-PTP670-MIB", "tFTPSoftwareUpgradeFileName"),
        ("CAMBIUM-PTP670-MIB", "tFTPStartSoftwareUpgrade"),
        ("CAMBIUM-PTP670-MIB", "tFTPSoftwareUpgradeStatus"),
        ("CAMBIUM-PTP670-MIB", "tFTPSoftwareUpgradeStatusText"),
        ("CAMBIUM-PTP670-MIB", "tFTPSoftwareUpgradeStatusAdditionalText"),
        ("CAMBIUM-PTP670-MIB", "hTTPAccessEnabled"),
        ("CAMBIUM-PTP670-MIB", "telnetAccessEnabled"),
        ("CAMBIUM-PTP670-MIB", "hTTPPortNumber"),
        ("CAMBIUM-PTP670-MIB", "hTTPSPortNumber"),
        ("CAMBIUM-PTP670-MIB", "telnetPortNumber"),
        ("CAMBIUM-PTP670-MIB", "hTTPSAccessEnabled"),
        ("CAMBIUM-PTP670-MIB", "tFTPServerInternetAddressType"),
        ("CAMBIUM-PTP670-MIB", "tFTPServerInternetAddress"),
        ("CAMBIUM-PTP670-MIB", "lowestDataModulationMode"),
        ("CAMBIUM-PTP670-MIB", "tFTPClient"),
        ("CAMBIUM-PTP670-MIB", "mgmtInstancedTableNumber"),
        ("CAMBIUM-PTP670-MIB", "tFTPServerResolvedInternetAddress"),
        ("CAMBIUM-PTP670-MIB", "installationMode"),
        ("CAMBIUM-PTP670-MIB", "installStatus"))
)
if mibBuilder.loadTexts:
    managementGroup.setStatus("current")

phyControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 10)
)
phyControlGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "linkSymmetry"),
        ("CAMBIUM-PTP670-MIB", "userConfiguredMaxModulationMode"),
        ("CAMBIUM-PTP670-MIB", "linkModeOptimization"),
        ("CAMBIUM-PTP670-MIB", "txColorCode"),
        ("CAMBIUM-PTP670-MIB", "rxColorCode"),
        ("CAMBIUM-PTP670-MIB", "remoteMaximumTransmitPowerLinked"),
        ("CAMBIUM-PTP670-MIB", "phyControlInstancedTableNumber"),
        ("CAMBIUM-PTP670-MIB", "remoteMaximumTransmitPower"))
)
if mibBuilder.loadTexts:
    phyControlGroup.setStatus("current")

phyStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 12)
)
phyStatusGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "linkLossLinked"),
        ("CAMBIUM-PTP670-MIB", "receivePowerLinked"),
        ("CAMBIUM-PTP670-MIB", "vectorErrorLinked"),
        ("CAMBIUM-PTP670-MIB", "transmitPowerLinked"),
        ("CAMBIUM-PTP670-MIB", "receiveChannel"),
        ("CAMBIUM-PTP670-MIB", "transmitChannel"),
        ("CAMBIUM-PTP670-MIB", "receiveFreqMHz"),
        ("CAMBIUM-PTP670-MIB", "transmitFreqMHz"),
        ("CAMBIUM-PTP670-MIB", "signalStrengthRatioLinked"),
        ("CAMBIUM-PTP670-MIB", "receiveFreqKHz"),
        ("CAMBIUM-PTP670-MIB", "transmitFreqKHz"),
        ("CAMBIUM-PTP670-MIB", "rawReceivePowerLinked"),
        ("CAMBIUM-PTP670-MIB", "rangeLinked"),
        ("CAMBIUM-PTP670-MIB", "receiveModulationModeLinked"),
        ("CAMBIUM-PTP670-MIB", "transmitModulationModeLinked"),
        ("CAMBIUM-PTP670-MIB", "searchStateLinked"),
        ("CAMBIUM-PTP670-MIB", "remoteMACAddressLinked"),
        ("CAMBIUM-PTP670-MIB", "phyInstancedStatusTableNumber"),
        ("CAMBIUM-PTP670-MIB", "tempPcb"),
        ("CAMBIUM-PTP670-MIB", "linkLoss"),
        ("CAMBIUM-PTP670-MIB", "receivePower"),
        ("CAMBIUM-PTP670-MIB", "vectorError"),
        ("CAMBIUM-PTP670-MIB", "signalStrengthRatio"),
        ("CAMBIUM-PTP670-MIB", "range"),
        ("CAMBIUM-PTP670-MIB", "receiveModulationMode"),
        ("CAMBIUM-PTP670-MIB", "transmitModulationMode"),
        ("CAMBIUM-PTP670-MIB", "searchState"),
        ("CAMBIUM-PTP670-MIB", "remoteMACAddress"),
        ("CAMBIUM-PTP670-MIB", "rawReceivePower"),
        ("CAMBIUM-PTP670-MIB", "transmitPower"))
)
if mibBuilder.loadTexts:
    phyStatusGroup.setStatus("current")

alarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 13)
)
alarmsGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "unitOutOfCalibration"),
        ("CAMBIUM-PTP670-MIB", "incompatibleRegulatoryBandsLinked"),
        ("CAMBIUM-PTP670-MIB", "noWirelessChannelAvailable"),
        ("CAMBIUM-PTP670-MIB", "wirelessLinkDisabledWarning"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortDisabledWarning"),
        ("CAMBIUM-PTP670-MIB", "sFPError"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortConfigurationMismatch"),
        ("CAMBIUM-PTP670-MIB", "incompatibleMasterAndSlaveLinked"),
        ("CAMBIUM-PTP670-MIB", "tDDSynchronizationStatus"),
        ("CAMBIUM-PTP670-MIB", "auxPortDisabledWarning"),
        ("CAMBIUM-PTP670-MIB", "tDDSynchronizationAlarm"),
        ("CAMBIUM-PTP670-MIB", "linkModeOptimizationMismatchLinked"),
        ("CAMBIUM-PTP670-MIB", "auxPortConfigurationMismatch"),
        ("CAMBIUM-PTP670-MIB", "secureModeAlarm"),
        ("CAMBIUM-PTP670-MIB", "dataBridgingStatusAlarmLinked"),
        ("CAMBIUM-PTP670-MIB", "sFPPortDisabledWarning"),
        ("CAMBIUM-PTP670-MIB", "sFPPortConfigurationMismatch"),
        ("CAMBIUM-PTP670-MIB", "maxLinkRangeExceededLinked"),
        ("CAMBIUM-PTP670-MIB", "nIDULanPortDisabledWarning"),
        ("CAMBIUM-PTP670-MIB", "nIDULanPortConfigurationMismatch"),
        ("CAMBIUM-PTP670-MIB", "portAllocationMismatchLinked"),
        ("CAMBIUM-PTP670-MIB", "transparentClockSourcePortAlarm"),
        ("CAMBIUM-PTP670-MIB", "alarmInstancedTableNumber"),
        ("CAMBIUM-PTP670-MIB", "secureLicenseSignatureAlarm"),
        ("CAMBIUM-PTP670-MIB", "incompatibleMasterAndSlave"),
        ("CAMBIUM-PTP670-MIB", "linkModeOptimizationMismatch"),
        ("CAMBIUM-PTP670-MIB", "dataBridgingStatusAlarm"),
        ("CAMBIUM-PTP670-MIB", "maxLinkRangeExceeded"),
        ("CAMBIUM-PTP670-MIB", "portAllocationMismatch"),
        ("CAMBIUM-PTP670-MIB", "wirelessLinkStatusAlarm"),
        ("CAMBIUM-PTP670-MIB", "incompatibleRegulatoryBands"))
)
if mibBuilder.loadTexts:
    alarmsGroup.setStatus("current")

apcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 14)
)
apcGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "atpcHcmpMasterTargetRxPower"),
        ("CAMBIUM-PTP670-MIB", "atpcHcmpMasterTxPower"))
)
if mibBuilder.loadTexts:
    apcGroup.setStatus("current")

smtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 15)
)
smtpGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "sMTPEmailAlert"),
        ("CAMBIUM-PTP670-MIB", "sMTPServerPortNumber"),
        ("CAMBIUM-PTP670-MIB", "sMTPSourceEmailAddress"),
        ("CAMBIUM-PTP670-MIB", "sMTPDestinationEmailAddress"),
        ("CAMBIUM-PTP670-MIB", "sMTPEnabledMessages"),
        ("CAMBIUM-PTP670-MIB", "sMTPServerInternetAddressType"),
        ("CAMBIUM-PTP670-MIB", "sMTPServerInternetAddress"),
        ("CAMBIUM-PTP670-MIB", "sMTPServerResolvedInternetAddress"))
)
if mibBuilder.loadTexts:
    smtpGroup.setStatus("current")

snmpControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 16)
)
snmpControlGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "sNMPPortNumber"),
        ("CAMBIUM-PTP670-MIB", "sNMPCommunityString"),
        ("CAMBIUM-PTP670-MIB", "sNMPTrapTableNumber"),
        ("CAMBIUM-PTP670-MIB", "sNMPTrapVersion"),
        ("CAMBIUM-PTP670-MIB", "sNMPEnabledTraps"),
        ("CAMBIUM-PTP670-MIB", "enabledDiagnosticAlarms"),
        ("CAMBIUM-PTP670-MIB", "sNMPSendAllTrapsAtStartup"),
        ("CAMBIUM-PTP670-MIB", "sNMPTrapPortNumber"),
        ("CAMBIUM-PTP670-MIB", "sNMPTrapInternetAddressType"),
        ("CAMBIUM-PTP670-MIB", "sNMPTrapInternetAddress"),
        ("CAMBIUM-PTP670-MIB", "sNMPTrapReceiverEnabled"),
        ("CAMBIUM-PTP670-MIB", "sNMPTrapResolvedInternetAddress"))
)
if mibBuilder.loadTexts:
    snmpControlGroup.setStatus("current")

sntpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 17)
)
sntpGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "sNTPState"),
        ("CAMBIUM-PTP670-MIB", "sNTPPollInterval"),
        ("CAMBIUM-PTP670-MIB", "sNTPSync"),
        ("CAMBIUM-PTP670-MIB", "sNTPLastSync"),
        ("CAMBIUM-PTP670-MIB", "systemClock"),
        ("CAMBIUM-PTP670-MIB", "timeZone"),
        ("CAMBIUM-PTP670-MIB", "daylightSaving"),
        ("CAMBIUM-PTP670-MIB", "sNTPPrimaryServer"),
        ("CAMBIUM-PTP670-MIB", "sNTPPrimaryServerDeadTime"),
        ("CAMBIUM-PTP670-MIB", "sNTPServerRetries"),
        ("CAMBIUM-PTP670-MIB", "sNTPServerTimeout"),
        ("CAMBIUM-PTP670-MIB", "sNTPServerTableNumber"),
        ("CAMBIUM-PTP670-MIB", "sNTPServerPortNumber"),
        ("CAMBIUM-PTP670-MIB", "sNTPServerStatus"),
        ("CAMBIUM-PTP670-MIB", "sNTPServerInternetAddressType"),
        ("CAMBIUM-PTP670-MIB", "sNTPServerInternetAddress"),
        ("CAMBIUM-PTP670-MIB", "sNTPServerResolvedInternetAddress"),
        ("CAMBIUM-PTP670-MIB", "sNTPServerAuthenticationProtocol"),
        ("CAMBIUM-PTP670-MIB", "sNTPServerKeyIdentifier"))
)
if mibBuilder.loadTexts:
    sntpGroup.setStatus("current")

resetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 18)
)
resetGroup.setObjects(
    ("CAMBIUM-PTP670-MIB", "systemReset")
)
if mibBuilder.loadTexts:
    resetGroup.setStatus("current")

versionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 19)
)
versionsGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "softwareVersion"),
        ("CAMBIUM-PTP670-MIB", "hardwareVersion"),
        ("CAMBIUM-PTP670-MIB", "secondarySoftwareVersion"),
        ("CAMBIUM-PTP670-MIB", "bootVersion"))
)
if mibBuilder.loadTexts:
    versionsGroup.setStatus("current")

pubStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 20)
)
pubStatsGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "receiveDataRateLinked"),
        ("CAMBIUM-PTP670-MIB", "transmitDataRateLinked"),
        ("CAMBIUM-PTP670-MIB", "aggregateDataRateLinked"),
        ("CAMBIUM-PTP670-MIB", "wirelessLinkAvailabilityLinked"),
        ("CAMBIUM-PTP670-MIB", "wirelessLinkStatusLinked"),
        ("CAMBIUM-PTP670-MIB", "byteErrorRatioLinked"),
        ("CAMBIUM-PTP670-MIB", "receiveModulationModeDetailLinked"),
        ("CAMBIUM-PTP670-MIB", "dataBridgingAvailabilityLinked"),
        ("CAMBIUM-PTP670-MIB", "pubInstancedStatsTableNumber"),
        ("CAMBIUM-PTP670-MIB", "receiveDataRate"),
        ("CAMBIUM-PTP670-MIB", "transmitDataRate"),
        ("CAMBIUM-PTP670-MIB", "aggregateDataRate"),
        ("CAMBIUM-PTP670-MIB", "wirelessLinkAvailability"),
        ("CAMBIUM-PTP670-MIB", "wirelessLinkStatus"),
        ("CAMBIUM-PTP670-MIB", "receiveModulationModeDetail"),
        ("CAMBIUM-PTP670-MIB", "dataBridgingAvailability"),
        ("CAMBIUM-PTP670-MIB", "byteErrorRatio"),
        ("CAMBIUM-PTP670-MIB", "wirelessOutEthernetOctets"),
        ("CAMBIUM-PTP670-MIB", "wirelessOutAllOctets"),
        ("CAMBIUM-PTP670-MIB", "wirelessOutOctets"),
        ("CAMBIUM-PTP670-MIB", "erroredSeconds"),
        ("CAMBIUM-PTP670-MIB", "severelyErroredSeconds"),
        ("CAMBIUM-PTP670-MIB", "unavailableSeconds"))
)
if mibBuilder.loadTexts:
    pubStatsGroup.setStatus("current")

encryptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 22)
)
encryptionGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "encryptionAlgorithm"),
        ("CAMBIUM-PTP670-MIB", "tLSMinimumSecurityLevel"))
)
if mibBuilder.loadTexts:
    encryptionGroup.setStatus("current")

tDDControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 23)
)
tDDControlGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "tDDSynchronizationMode"),
        ("CAMBIUM-PTP670-MIB", "hCMPMaximumLinkRange"),
        ("CAMBIUM-PTP670-MIB", "maximumNumberOfSlaves"),
        ("CAMBIUM-PTP670-MIB", "hCMPLinkSymmetry"))
)
if mibBuilder.loadTexts:
    tDDControlGroup.setStatus("current")

syslogControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 24)
)
syslogControlGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "syslogClient"),
        ("CAMBIUM-PTP670-MIB", "syslogState"))
)
if mibBuilder.loadTexts:
    syslogControlGroup.setStatus("current")

aAAControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 25)
)
aAAControlGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "userTableNumber"),
        ("CAMBIUM-PTP670-MIB", "userName"),
        ("CAMBIUM-PTP670-MIB", "userRole"),
        ("CAMBIUM-PTP670-MIB", "userEnabled"),
        ("CAMBIUM-PTP670-MIB", "userPassword"))
)
if mibBuilder.loadTexts:
    aAAControlGroup.setStatus("current")

routerProtocolsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 26)
)
routerProtocolsGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "microwaveAdaptiveBandwidth"),
        ("CAMBIUM-PTP670-MIB", "mABNominalModulationMode"),
        ("CAMBIUM-PTP670-MIB", "mABTransmissionInterval"),
        ("CAMBIUM-PTP670-MIB", "mABHoldoffPeriod"),
        ("CAMBIUM-PTP670-MIB", "mABMaintenanceLevel"),
        ("CAMBIUM-PTP670-MIB", "useVLANForMABProtocol"),
        ("CAMBIUM-PTP670-MIB", "mABProtocolVID"),
        ("CAMBIUM-PTP670-MIB", "mABProtocolVLANPriority"),
        ("CAMBIUM-PTP670-MIB", "mABState"),
        ("CAMBIUM-PTP670-MIB", "mABNominalTransmitCapacity"),
        ("CAMBIUM-PTP670-MIB", "mABCurrentTransmitCapacity"))
)
if mibBuilder.loadTexts:
    routerProtocolsGroup.setStatus("current")

cableDiagnosticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 27)
)
cableDiagnosticsGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "cableDiagnosticsPorts"),
        ("CAMBIUM-PTP670-MIB", "cableDiagnosticsControl"),
        ("CAMBIUM-PTP670-MIB", "cableDiagnosticsWarning"),
        ("CAMBIUM-PTP670-MIB", "cableDiagnosticsResultTableNumber"),
        ("CAMBIUM-PTP670-MIB", "cableDiagnosticsResultsDateTime"),
        ("CAMBIUM-PTP670-MIB", "cableDiagPair1Results"),
        ("CAMBIUM-PTP670-MIB", "cableDiagPair1Distance"),
        ("CAMBIUM-PTP670-MIB", "cableDiagPair2Results"),
        ("CAMBIUM-PTP670-MIB", "cableDiagPair2Distance"),
        ("CAMBIUM-PTP670-MIB", "cableDiagPair3Results"),
        ("CAMBIUM-PTP670-MIB", "cableDiagPair3Distance"),
        ("CAMBIUM-PTP670-MIB", "cableDiagPair4Results"),
        ("CAMBIUM-PTP670-MIB", "cableDiagPair4Distance"))
)
if mibBuilder.loadTexts:
    cableDiagnosticsGroup.setStatus("current")

unitIdentificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 28)
)
unitIdentificationGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "deviceMACAddress"),
        ("CAMBIUM-PTP670-MIB", "deviceESN"),
        ("CAMBIUM-PTP670-MIB", "deviceMSN"))
)
if mibBuilder.loadTexts:
    unitIdentificationGroup.setStatus("current")

authorizationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 29)
)
authorizationControlGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "authorizationControlTableNumber"),
        ("CAMBIUM-PTP670-MIB", "whitelistRMMacAddress"),
        ("CAMBIUM-PTP670-MIB", "whitelistRMEnabled"),
        ("CAMBIUM-PTP670-MIB", "blacklistRMMacAddress"),
        ("CAMBIUM-PTP670-MIB", "blacklistRMEnabled"))
)
if mibBuilder.loadTexts:
    authorizationControlGroup.setStatus("current")

dNSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 30)
)
dNSGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "dNSResolver"),
        ("CAMBIUM-PTP670-MIB", "dNSPrimaryServer"),
        ("CAMBIUM-PTP670-MIB", "dNSServerTableNumber"),
        ("CAMBIUM-PTP670-MIB", "dNSServerInternetAddressType"),
        ("CAMBIUM-PTP670-MIB", "dNSServerInternetAddress"),
        ("CAMBIUM-PTP670-MIB", "dNSServerPortNumber"))
)
if mibBuilder.loadTexts:
    dNSGroup.setStatus("current")

supplementaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 96)
)
supplementaryGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "longitude"),
        ("CAMBIUM-PTP670-MIB", "latitude"),
        ("CAMBIUM-PTP670-MIB", "altitude"))
)
if mibBuilder.loadTexts:
    supplementaryGroup.setStatus("current")


# Notification objects

channelChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 1)
)
channelChangeTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "receiveChannel")
)
if mibBuilder.loadTexts:
    channelChangeTrap.setStatus(
        "current"
    )

dfsImpulsiveInterferenceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 2)
)
dfsImpulsiveInterferenceTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "receiveChannel")
)
if mibBuilder.loadTexts:
    dfsImpulsiveInterferenceTrap.setStatus(
        "current"
    )

mainPSUPortStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 3)
)
mainPSUPortStatusTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "mainPSUPortStatus")
)
if mibBuilder.loadTexts:
    mainPSUPortStatusTrap.setStatus(
        "current"
    )

mainPSUPortDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 4)
)
mainPSUPortDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "mainPSUPortDisabledWarning")
)
if mibBuilder.loadTexts:
    mainPSUPortDisabledWarningTrap.setStatus(
        "current"
    )

mainPSUPortConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 5)
)
mainPSUPortConfigurationMismatchTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "mainPSUPortConfigurationMismatch")
)
if mibBuilder.loadTexts:
    mainPSUPortConfigurationMismatchTrap.setStatus(
        "current"
    )

auxPortStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 6)
)
auxPortStatusTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "auxPortStatus")
)
if mibBuilder.loadTexts:
    auxPortStatusTrap.setStatus(
        "current"
    )

auxPortDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 7)
)
auxPortDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "auxPortDisabledWarning")
)
if mibBuilder.loadTexts:
    auxPortDisabledWarningTrap.setStatus(
        "current"
    )

regulatoryBandTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 8)
)
regulatoryBandTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "regulatoryBand")
)
if mibBuilder.loadTexts:
    regulatoryBandTrap.setStatus(
        "current"
    )

installStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 9)
)
installStatusTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "installStatus")
)
if mibBuilder.loadTexts:
    installStatusTrap.setStatus(
        "current"
    )

installArmStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 10)
)
installArmStateTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "installArmState")
)
if mibBuilder.loadTexts:
    installArmStateTrap.setStatus(
        "current"
    )

unitOutOfCalibrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 11)
)
unitOutOfCalibrationTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "unitOutOfCalibration")
)
if mibBuilder.loadTexts:
    unitOutOfCalibrationTrap.setStatus(
        "current"
    )

auxPortPowerOverEthernetOutputStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 12)
)
auxPortPowerOverEthernetOutputStatusTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "auxPortPowerOverEthernetOutputStatus")
)
if mibBuilder.loadTexts:
    auxPortPowerOverEthernetOutputStatusTrap.setStatus(
        "current"
    )

incompatibleRegulatoryBandsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 14)
)
incompatibleRegulatoryBandsTrap.setObjects(
      *(("CAMBIUM-PTP670-MIB", "incompatibleRegulatoryBands"),
        ("CAMBIUM-PTP670-MIB", "remoteMACAddress"))
)
if mibBuilder.loadTexts:
    incompatibleRegulatoryBandsTrap.setStatus(
        "current"
    )

noWirelessChannelAvailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 15)
)
noWirelessChannelAvailableTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "noWirelessChannelAvailable")
)
if mibBuilder.loadTexts:
    noWirelessChannelAvailableTrap.setStatus(
        "current"
    )

wirelessLinkDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 16)
)
wirelessLinkDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "wirelessLinkDisabledWarning")
)
if mibBuilder.loadTexts:
    wirelessLinkDisabledWarningTrap.setStatus(
        "current"
    )

auxPortConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 17)
)
auxPortConfigurationMismatchTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "auxPortConfigurationMismatch")
)
if mibBuilder.loadTexts:
    auxPortConfigurationMismatchTrap.setStatus(
        "current"
    )

sFPErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 18)
)
sFPErrorTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "sFPError")
)
if mibBuilder.loadTexts:
    sFPErrorTrap.setStatus(
        "current"
    )

sFPPortStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 19)
)
sFPPortStatusTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "sFPPortStatus")
)
if mibBuilder.loadTexts:
    sFPPortStatusTrap.setStatus(
        "current"
    )

incompatibleMasterAndSlaveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 20)
)
incompatibleMasterAndSlaveTrap.setObjects(
      *(("CAMBIUM-PTP670-MIB", "incompatibleMasterAndSlave"),
        ("CAMBIUM-PTP670-MIB", "remoteMACAddress"))
)
if mibBuilder.loadTexts:
    incompatibleMasterAndSlaveTrap.setStatus(
        "current"
    )

sNTPSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 21)
)
sNTPSyncTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "sNTPSync")
)
if mibBuilder.loadTexts:
    sNTPSyncTrap.setStatus(
        "current"
    )

tDDSynchronizationAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 22)
)
tDDSynchronizationAlarmTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "tDDSynchronizationAlarm")
)
if mibBuilder.loadTexts:
    tDDSynchronizationAlarmTrap.setStatus(
        "current"
    )

sFPPortDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 23)
)
sFPPortDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "sFPPortDisabledWarning")
)
if mibBuilder.loadTexts:
    sFPPortDisabledWarningTrap.setStatus(
        "current"
    )

sFPPortConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 24)
)
sFPPortConfigurationMismatchTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "sFPPortConfigurationMismatch")
)
if mibBuilder.loadTexts:
    sFPPortConfigurationMismatchTrap.setStatus(
        "current"
    )

linkModeOptimizationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 25)
)
linkModeOptimizationMismatchTrap.setObjects(
      *(("CAMBIUM-PTP670-MIB", "linkModeOptimizationMismatch"),
        ("CAMBIUM-PTP670-MIB", "remoteMACAddress"))
)
if mibBuilder.loadTexts:
    linkModeOptimizationMismatchTrap.setStatus(
        "current"
    )

tDMInterfaceStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 26)
)
tDMInterfaceStatusTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "tDMInterfaceStatus")
)
if mibBuilder.loadTexts:
    tDMInterfaceStatusTrap.setStatus(
        "current"
    )

tDMChannelStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 27)
)
tDMChannelStatusTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "tDMChannelStatus")
)
if mibBuilder.loadTexts:
    tDMChannelStatusTrap.setStatus(
        "current"
    )

tDMChannelLoopbackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 28)
)
tDMChannelLoopbackTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "tDMChannelLoopback")
)
if mibBuilder.loadTexts:
    tDMChannelLoopbackTrap.setStatus(
        "current"
    )

nIDULanPortStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 29)
)
nIDULanPortStatusTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "nIDULanPortStatus")
)
if mibBuilder.loadTexts:
    nIDULanPortStatusTrap.setStatus(
        "current"
    )

syslogStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 30)
)
syslogStateTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "syslogState")
)
if mibBuilder.loadTexts:
    syslogStateTrap.setStatus(
        "current"
    )

syslogLocalNearlyFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 31)
)
if mibBuilder.loadTexts:
    syslogLocalNearlyFullTrap.setStatus(
        "current"
    )

syslogLocalWrappedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 32)
)
if mibBuilder.loadTexts:
    syslogLocalWrappedTrap.setStatus(
        "current"
    )

syslogClientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 33)
)
syslogClientTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "syslogClient")
)
if mibBuilder.loadTexts:
    syslogClientTrap.setStatus(
        "current"
    )

secureModeAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 34)
)
secureModeAlarmTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "secureModeAlarm")
)
if mibBuilder.loadTexts:
    secureModeAlarmTrap.setStatus(
        "current"
    )

dataBridgingStatusAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 35)
)
dataBridgingStatusAlarmTrap.setObjects(
      *(("CAMBIUM-PTP670-MIB", "dataBridgingStatusAlarm"),
        ("CAMBIUM-PTP670-MIB", "remoteMACAddress"))
)
if mibBuilder.loadTexts:
    dataBridgingStatusAlarmTrap.setStatus(
        "current"
    )

licenseRemainingTrialPeriodAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 36)
)
licenseRemainingTrialPeriodAlarmTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "licenseRemainingTrialPeriodAlarm")
)
if mibBuilder.loadTexts:
    licenseRemainingTrialPeriodAlarmTrap.setStatus(
        "current"
    )

capacityVariantMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 37)
)
capacityVariantMismatchTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "capacityVariantMismatch")
)
if mibBuilder.loadTexts:
    capacityVariantMismatchTrap.setStatus(
        "current"
    )

maxLinkRangeExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 38)
)
maxLinkRangeExceededTrap.setObjects(
      *(("CAMBIUM-PTP670-MIB", "maxLinkRangeExceeded"),
        ("CAMBIUM-PTP670-MIB", "remoteMACAddress"))
)
if mibBuilder.loadTexts:
    maxLinkRangeExceededTrap.setStatus(
        "current"
    )

tDMConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 39)
)
tDMConfigurationMismatchTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "tDMConfigurationMismatch")
)
if mibBuilder.loadTexts:
    tDMConfigurationMismatchTrap.setStatus(
        "current"
    )

nIDULanPortDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 40)
)
nIDULanPortDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "nIDULanPortDisabledWarning")
)
if mibBuilder.loadTexts:
    nIDULanPortDisabledWarningTrap.setStatus(
        "current"
    )

nIDULanPortConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 41)
)
nIDULanPortConfigurationMismatchTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "nIDULanPortConfigurationMismatch")
)
if mibBuilder.loadTexts:
    nIDULanPortConfigurationMismatchTrap.setStatus(
        "current"
    )

portAllocationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 44)
)
portAllocationMismatchTrap.setObjects(
      *(("CAMBIUM-PTP670-MIB", "portAllocationMismatch"),
        ("CAMBIUM-PTP670-MIB", "remoteMACAddress"))
)
if mibBuilder.loadTexts:
    portAllocationMismatchTrap.setStatus(
        "current"
    )

wirelessLinkStatusAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 45)
)
wirelessLinkStatusAlarmTrap.setObjects(
      *(("CAMBIUM-PTP670-MIB", "wirelessLinkStatusAlarm"),
        ("CAMBIUM-PTP670-MIB", "remoteMACAddress"))
)
if mibBuilder.loadTexts:
    wirelessLinkStatusAlarmTrap.setStatus(
        "current"
    )

lbtDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 46)
)
lbtDetectedTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "receiveChannel")
)
if mibBuilder.loadTexts:
    lbtDetectedTrap.setStatus(
        "current"
    )

secureLicenseSignatureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 11, 99, 0, 47)
)
secureLicenseSignatureAlarmTrap.setObjects(
    ("CAMBIUM-PTP670-MIB", "secureLicenseSignatureAlarm")
)
if mibBuilder.loadTexts:
    secureLicenseSignatureAlarmTrap.setStatus(
        "current"
    )


# Notifications groups

notificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 17713, 11, 98, 99)
)
notificationsGroup.setObjects(
      *(("CAMBIUM-PTP670-MIB", "channelChangeTrap"),
        ("CAMBIUM-PTP670-MIB", "dfsImpulsiveInterferenceTrap"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortStatusTrap"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortDisabledWarningTrap"),
        ("CAMBIUM-PTP670-MIB", "mainPSUPortConfigurationMismatchTrap"),
        ("CAMBIUM-PTP670-MIB", "auxPortStatusTrap"),
        ("CAMBIUM-PTP670-MIB", "auxPortDisabledWarningTrap"),
        ("CAMBIUM-PTP670-MIB", "regulatoryBandTrap"),
        ("CAMBIUM-PTP670-MIB", "installStatusTrap"),
        ("CAMBIUM-PTP670-MIB", "installArmStateTrap"),
        ("CAMBIUM-PTP670-MIB", "unitOutOfCalibrationTrap"),
        ("CAMBIUM-PTP670-MIB", "auxPortPowerOverEthernetOutputStatusTrap"),
        ("CAMBIUM-PTP670-MIB", "incompatibleRegulatoryBandsTrap"),
        ("CAMBIUM-PTP670-MIB", "noWirelessChannelAvailableTrap"),
        ("CAMBIUM-PTP670-MIB", "wirelessLinkDisabledWarningTrap"),
        ("CAMBIUM-PTP670-MIB", "auxPortConfigurationMismatchTrap"),
        ("CAMBIUM-PTP670-MIB", "sFPErrorTrap"),
        ("CAMBIUM-PTP670-MIB", "sFPPortStatusTrap"),
        ("CAMBIUM-PTP670-MIB", "incompatibleMasterAndSlaveTrap"),
        ("CAMBIUM-PTP670-MIB", "sNTPSyncTrap"),
        ("CAMBIUM-PTP670-MIB", "tDDSynchronizationAlarmTrap"),
        ("CAMBIUM-PTP670-MIB", "sFPPortDisabledWarningTrap"),
        ("CAMBIUM-PTP670-MIB", "sFPPortConfigurationMismatchTrap"),
        ("CAMBIUM-PTP670-MIB", "linkModeOptimizationMismatchTrap"),
        ("CAMBIUM-PTP670-MIB", "tDMInterfaceStatusTrap"),
        ("CAMBIUM-PTP670-MIB", "tDMChannelStatusTrap"),
        ("CAMBIUM-PTP670-MIB", "tDMChannelLoopbackTrap"),
        ("CAMBIUM-PTP670-MIB", "nIDULanPortStatusTrap"),
        ("CAMBIUM-PTP670-MIB", "syslogStateTrap"),
        ("CAMBIUM-PTP670-MIB", "syslogLocalNearlyFullTrap"),
        ("CAMBIUM-PTP670-MIB", "syslogLocalWrappedTrap"),
        ("CAMBIUM-PTP670-MIB", "syslogClientTrap"),
        ("CAMBIUM-PTP670-MIB", "secureModeAlarmTrap"),
        ("CAMBIUM-PTP670-MIB", "dataBridgingStatusAlarmTrap"),
        ("CAMBIUM-PTP670-MIB", "licenseRemainingTrialPeriodAlarmTrap"),
        ("CAMBIUM-PTP670-MIB", "capacityVariantMismatchTrap"),
        ("CAMBIUM-PTP670-MIB", "maxLinkRangeExceededTrap"),
        ("CAMBIUM-PTP670-MIB", "tDMConfigurationMismatchTrap"),
        ("CAMBIUM-PTP670-MIB", "nIDULanPortDisabledWarningTrap"),
        ("CAMBIUM-PTP670-MIB", "nIDULanPortConfigurationMismatchTrap"),
        ("CAMBIUM-PTP670-MIB", "portAllocationMismatchTrap"),
        ("CAMBIUM-PTP670-MIB", "wirelessLinkStatusAlarmTrap"),
        ("CAMBIUM-PTP670-MIB", "lbtDetectedTrap"),
        ("CAMBIUM-PTP670-MIB", "secureLicenseSignatureAlarmTrap"))
)
if mibBuilder.loadTexts:
    notificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ptpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 17713, 11, 97)
)
ptpCompliance.setObjects(
      *(("CAMBIUM-PTP670-MIB", "dfsGroup"),
        ("CAMBIUM-PTP670-MIB", "bridgeGroup"),
        ("CAMBIUM-PTP670-MIB", "configurationGroup"),
        ("CAMBIUM-PTP670-MIB", "ethernetGroup"),
        ("CAMBIUM-PTP670-MIB", "tDMGroup"),
        ("CAMBIUM-PTP670-MIB", "licenseGroup"),
        ("CAMBIUM-PTP670-MIB", "managementGroup"),
        ("CAMBIUM-PTP670-MIB", "phyControlGroup"),
        ("CAMBIUM-PTP670-MIB", "phyStatusGroup"),
        ("CAMBIUM-PTP670-MIB", "alarmsGroup"),
        ("CAMBIUM-PTP670-MIB", "apcGroup"),
        ("CAMBIUM-PTP670-MIB", "smtpGroup"),
        ("CAMBIUM-PTP670-MIB", "snmpControlGroup"),
        ("CAMBIUM-PTP670-MIB", "sntpGroup"),
        ("CAMBIUM-PTP670-MIB", "resetGroup"),
        ("CAMBIUM-PTP670-MIB", "versionsGroup"),
        ("CAMBIUM-PTP670-MIB", "pubStatsGroup"),
        ("CAMBIUM-PTP670-MIB", "encryptionGroup"),
        ("CAMBIUM-PTP670-MIB", "tDDControlGroup"),
        ("CAMBIUM-PTP670-MIB", "aAAControlGroup"),
        ("CAMBIUM-PTP670-MIB", "syslogControlGroup"),
        ("CAMBIUM-PTP670-MIB", "routerProtocolsGroup"),
        ("CAMBIUM-PTP670-MIB", "cableDiagnosticsGroup"),
        ("CAMBIUM-PTP670-MIB", "unitIdentificationGroup"),
        ("CAMBIUM-PTP670-MIB", "authorizationControlGroup"),
        ("CAMBIUM-PTP670-MIB", "dNSGroup"),
        ("CAMBIUM-PTP670-MIB", "supplementaryGroup"),
        ("CAMBIUM-PTP670-MIB", "notificationsGroup"))
)
if mibBuilder.loadTexts:
    ptpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-PTP670-MIB",
    **{"cambium": cambium,
       "ptp": ptp,
       "ptmp": ptmp,
       "ptp670": ptp670,
       "dfs": dfs,
       "dfsTableNumber": dfsTableNumber,
       "dfsTable": dfsTable,
       "dfsTableEntry": dfsTableEntry,
       "dfsTableIndex": dfsTableIndex,
       "dfsMeans": dfsMeans,
       "dfsNineNinePointNinePercentiles": dfsNineNinePointNinePercentiles,
       "dfsPeaks": dfsPeaks,
       "extendedSpectrumScanning": extendedSpectrumScanning,
       "bridge": bridge,
       "localPacketFiltering": localPacketFiltering,
       "packetsToInternalStack": packetsToInternalStack,
       "packetsFromInternalStack": packetsFromInternalStack,
       "configuration": configuration,
       "iPv4Address": iPv4Address,
       "subnetMask": subnetMask,
       "gatewayIPAddress": gatewayIPAddress,
       "targetMACAddress": targetMACAddress,
       "masterSlaveMode": masterSlaveMode,
       "maximumTransmitPower": maximumTransmitPower,
       "antennaGain": antennaGain,
       "cableLoss": cableLoss,
       "eIRP": eIRP,
       "channelBandwidth": channelBandwidth,
       "linkName": linkName,
       "siteName": siteName,
       "accessMethod": accessMethod,
       "groupID": groupID,
       "iPv6Address": iPv6Address,
       "iPVersion": iPVersion,
       "iPv6AutoConfiguredLinkLocalAddress": iPv6AutoConfiguredLinkLocalAddress,
       "iPv6PrefixLength": iPv6PrefixLength,
       "iPv6GatewayAddress": iPv6GatewayAddress,
       "remoteInternetAddressTypeLinked": remoteInternetAddressTypeLinked,
       "remoteInternetAddressLinked": remoteInternetAddressLinked,
       "subbandLowestFrequency": subbandLowestFrequency,
       "subbandHighestFrequency": subbandHighestFrequency,
       "enableTransmission": enableTransmission,
       "antennaSelection": antennaSelection,
       "transmitterChannels": transmitterChannels,
       "wirelessTopology": wirelessTopology,
       "configurationInstancedTableNumber": configurationInstancedTableNumber,
       "configurationInstancedTable": configurationInstancedTable,
       "configurationInstancedTableEntry": configurationInstancedTableEntry,
       "configurationInstancedTableIndex": configurationInstancedTableIndex,
       "remoteInternetAddressType": remoteInternetAddressType,
       "remoteInternetAddress": remoteInternetAddress,
       "remoteUnitName": remoteUnitName,
       "unitName": unitName,
       "authorizationMethod": authorizationMethod,
       "remoteUnitNameLinked": remoteUnitNameLinked,
       "ethernet": ethernet,
       "mainPSUPortAutoNegotiation": mainPSUPortAutoNegotiation,
       "mainPSUPortAutoNegAdvertisement": mainPSUPortAutoNegAdvertisement,
       "mainPSUPortAutoMdix": mainPSUPortAutoMdix,
       "mainPSUPortStatus": mainPSUPortStatus,
       "mainPSUPortSpeedAndDuplex": mainPSUPortSpeedAndDuplex,
       "dataPortWirelessDownAlert": dataPortWirelessDownAlert,
       "useVLANForManagementInterfaces": useVLANForManagementInterfaces,
       "vLANManagementPriority": vLANManagementPriority,
       "vLANManagementVID": vLANManagementVID,
       "auxPortStatus": auxPortStatus,
       "auxPortSpeedAndDuplex": auxPortSpeedAndDuplex,
       "ethernetPriorityTableNumber": ethernetPriorityTableNumber,
       "ethernetPriorityTable": ethernetPriorityTable,
       "ethernetPriorityTableEntry": ethernetPriorityTableEntry,
       "ethernetPriorityTableIndex": ethernetPriorityTableIndex,
       "ethernetPriorityQueueMapping": ethernetPriorityQueueMapping,
       "l2CPPriorityTableNumber": l2CPPriorityTableNumber,
       "l2CPPriorityTable": l2CPPriorityTable,
       "l2CPPriorityTableEntry": l2CPPriorityTableEntry,
       "l2CPPriorityTableIndex": l2CPPriorityTableIndex,
       "l2CPPriorityQueueMapping": l2CPPriorityQueueMapping,
       "iPDSCPPriorityTableNumber": iPDSCPPriorityTableNumber,
       "iPDSCPPriorityTable": iPDSCPPriorityTable,
       "iPDSCPPriorityTableEntry": iPDSCPPriorityTableEntry,
       "iPDSCPPriorityTableIndex": iPDSCPPriorityTableIndex,
       "iPDSCPPriorityQueueMapping": iPDSCPPriorityQueueMapping,
       "mPLSTCPriorityTableNumber": mPLSTCPriorityTableNumber,
       "mPLSTCPriorityTable": mPLSTCPriorityTable,
       "mPLSTCPriorityTableEntry": mPLSTCPriorityTableEntry,
       "mPLSTCPriorityTableIndex": mPLSTCPriorityTableIndex,
       "mPLSTCPriorityQueueMapping": mPLSTCPriorityQueueMapping,
       "managementPortWirelessDownAlert": managementPortWirelessDownAlert,
       "qOSPriorityScheme": qOSPriorityScheme,
       "unknownNetworkPriorityQueueMapping": unknownNetworkPriorityQueueMapping,
       "dSCPManagementPriority": dSCPManagementPriority,
       "dataBridgingStatusLinked": dataBridgingStatusLinked,
       "mainPSUPortAllocation": mainPSUPortAllocation,
       "auxPortAllocation": auxPortAllocation,
       "sFPPortAllocation": sFPPortAllocation,
       "dataPortPauseFrames": dataPortPauseFrames,
       "sFPPortAutoNegotiation": sFPPortAutoNegotiation,
       "sFPPortAutoNegAdvertisement": sFPPortAutoNegAdvertisement,
       "sFPPortAutoMdix": sFPPortAutoMdix,
       "sFPPortStatus": sFPPortStatus,
       "sFPPortSpeedAndDuplex": sFPPortSpeedAndDuplex,
       "auxPortPowerOverEthernetOutput": auxPortPowerOverEthernetOutput,
       "auxPortPowerOverEthernetOutputStatus": auxPortPowerOverEthernetOutputStatus,
       "syncETracking": syncETracking,
       "syncEEquipmentClock": syncEEquipmentClock,
       "mainPSUPortQLRxOverwrite": mainPSUPortQLRxOverwrite,
       "mainPSUPortSSMTx": mainPSUPortSSMTx,
       "sFPPortSSMTx": sFPPortSSMTx,
       "auxPortSSMTx": auxPortSSMTx,
       "syncETrackingState": syncETrackingState,
       "mainPSUPortQLRx": mainPSUPortQLRx,
       "auxPortQLRx": auxPortQLRx,
       "sFPPortQLRx": sFPPortQLRx,
       "mainPSUPortQLTx": mainPSUPortQLTx,
       "auxPortQLTx": auxPortQLTx,
       "sFPPortQLTx": sFPPortQLTx,
       "mainPSUPortSyncEMasterSlaveStatus": mainPSUPortSyncEMasterSlaveStatus,
       "auxPortSyncEMasterSlaveStatus": auxPortSyncEMasterSlaveStatus,
       "sFPPortSyncEMasterSlaveStatus": sFPPortSyncEMasterSlaveStatus,
       "mainPSUPortGigabitMasterSlaveStatus": mainPSUPortGigabitMasterSlaveStatus,
       "auxPortGigabitMasterSlaveStatus": auxPortGigabitMasterSlaveStatus,
       "sFPPortGigabitMasterSlaveStatus": sFPPortGigabitMasterSlaveStatus,
       "transparentClock": transparentClock,
       "transparentClockVLAN": transparentClockVLAN,
       "transparentClockVID": transparentClockVID,
       "mainPSUPortAcceptedQLRx": mainPSUPortAcceptedQLRx,
       "auxPortAcceptedQLRx": auxPortAcceptedQLRx,
       "sFPPortAcceptedQLRx": sFPPortAcceptedQLRx,
       "mainPSUPortSyncERxStatus": mainPSUPortSyncERxStatus,
       "auxPortSyncERxStatus": auxPortSyncERxStatus,
       "sFPPortSyncERxStatus": sFPPortSyncERxStatus,
       "nIDULanPortStatus": nIDULanPortStatus,
       "nIDULanPortSpeedAndDuplex": nIDULanPortSpeedAndDuplex,
       "oOBPriorityQueueMapping": oOBPriorityQueueMapping,
       "nIDULanPortAutoNegotiation": nIDULanPortAutoNegotiation,
       "nIDULanPortAutoNegAdvertisement": nIDULanPortAutoNegAdvertisement,
       "nIDULanPortAutoMdix": nIDULanPortAutoMdix,
       "nIDULanPortGigabitMasterSlaveStatus": nIDULanPortGigabitMasterSlaveStatus,
       "txMABFrames": txMABFrames,
       "managementNetworkAccessEnabled": managementNetworkAccessEnabled,
       "transparentClockPort": transparentClockPort,
       "syncESlavePort": syncESlavePort,
       "sFPPortQLRxOverwrite": sFPPortQLRxOverwrite,
       "ethernetInstancedTableNumber": ethernetInstancedTableNumber,
       "ethernetInstancedTable": ethernetInstancedTable,
       "ethernetInstancedTableEntry": ethernetInstancedTableEntry,
       "ethernetInstancedTableIndex": ethernetInstancedTableIndex,
       "dataBridgingStatus": dataBridgingStatus,
       "ethernetStatisticsTableNumber": ethernetStatisticsTableNumber,
       "ethernetStatisticsTable": ethernetStatisticsTable,
       "ethernetStatisticsTableEntry": ethernetStatisticsTableEntry,
       "ethernetStatisticsTableIndex": ethernetStatisticsTableIndex,
       "ethernetStatisticsDataSource": ethernetStatisticsDataSource,
       "ethernetStatisticsRxOctets": ethernetStatisticsRxOctets,
       "ethernetStatisticsRxFrames": ethernetStatisticsRxFrames,
       "ethernetStatisticsRxBroadcasts": ethernetStatisticsRxBroadcasts,
       "ethernetStatisticsRxFramesWithError": ethernetStatisticsRxFramesWithError,
       "ethernetStatisticsRxFramesUndersize": ethernetStatisticsRxFramesUndersize,
       "ethernetStatisticsRxFramesOversize": ethernetStatisticsRxFramesOversize,
       "ethernetStatisticsTxOctets": ethernetStatisticsTxOctets,
       "ethernetStatisticsTxFrames": ethernetStatisticsTxFrames,
       "ethernetStatisticsTxBroadcasts": ethernetStatisticsTxBroadcasts,
       "tDM": tDM,
       "tDMInterfaceControl": tDMInterfaceControl,
       "tDMInterfaceStatus": tDMInterfaceStatus,
       "tDMEnabledChannels": tDMEnabledChannels,
       "tdmTableNumber": tdmTableNumber,
       "tdmTable": tdmTable,
       "tdmTableEntry": tdmTableEntry,
       "tdmTableIndex": tdmTableIndex,
       "tDMChannelStatus": tDMChannelStatus,
       "tDMChannelLineCode": tDMChannelLineCode,
       "tDMChannelCableLength": tDMChannelCableLength,
       "tDMChannelLoopback": tDMChannelLoopback,
       "tDMConfigurationMismatch": tDMConfigurationMismatch,
       "lowestTDMModulationMode": lowestTDMModulationMode,
       "license": license,
       "regulatoryBand": regulatoryBand,
       "productVariant": productVariant,
       "productName": productName,
       "frequencyVariant": frequencyVariant,
       "sNMPv3Enable": sNMPv3Enable,
       "licenseVersion": licenseVersion,
       "licenseUnitSerialNumber": licenseUnitSerialNumber,
       "licenseIssueNumber": licenseIssueNumber,
       "licenseCountry": licenseCountry,
       "licenseNumberOfRegulatoryBands": licenseNumberOfRegulatoryBands,
       "licenseRegulatoryBandsTable": licenseRegulatoryBandsTable,
       "licenseRegulatoryBandsTableEntry": licenseRegulatoryBandsTableEntry,
       "licenseRegulatoryBandsTableIndex": licenseRegulatoryBandsTableIndex,
       "licenseRegulatoryBandsList": licenseRegulatoryBandsList,
       "licenseBandwidthCap": licenseBandwidthCap,
       "licenseEncryption": licenseEncryption,
       "licenseSecurityLevel": licenseSecurityLevel,
       "licenseGroupAccess": licenseGroupAccess,
       "licenseOOBManagementSupport": licenseOOBManagementSupport,
       "licenseSFPPortSupport": licenseSFPPortSupport,
       "licenseAuxiliaryPortSupport": licenseAuxiliaryPortSupport,
       "licenseCapacity": licenseCapacity,
       "licenseMaxNumberOfTDMChannels": licenseMaxNumberOfTDMChannels,
       "licenseIEEE1588Support": licenseIEEE1588Support,
       "licenseSyncESupport": licenseSyncESupport,
       "licenseIPv6Support": licenseIPv6Support,
       "licenseMinimumFirmwareVersion": licenseMinimumFirmwareVersion,
       "licenseFullCapabilityTrialStatus": licenseFullCapabilityTrialStatus,
       "licenseRemainingTrialPeriod": licenseRemainingTrialPeriod,
       "licenseRemainingTrialPeriodAlarm": licenseRemainingTrialPeriodAlarm,
       "capacityVariantMismatchLinked": capacityVariantMismatchLinked,
       "licenseTDDSyncSupport": licenseTDDSyncSupport,
       "licenseMaxLinkRange": licenseMaxLinkRange,
       "licenseTrialPeriod": licenseTrialPeriod,
       "licenseRARSupport": licenseRARSupport,
       "licenseGasGroup": licenseGasGroup,
       "licenseLongMinimumFirmwareVersion": licenseLongMinimumFirmwareVersion,
       "licenseHCMPSupport": licenseHCMPSupport,
       "licenseInstancedTableNumber": licenseInstancedTableNumber,
       "licenseInstancedTable": licenseInstancedTable,
       "licenseInstancedTableEntry": licenseInstancedTableEntry,
       "licenseInstancedTableIndex": licenseInstancedTableIndex,
       "capacityVariantMismatch": capacityVariantMismatch,
       "licenseTLSRekey": licenseTLSRekey,
       "licenseAdvanceHCMPSupport": licenseAdvanceHCMPSupport,
       "licenseMinFirmwareVersionPTP650Emulation": licenseMinFirmwareVersionPTP650Emulation,
       "management": management,
       "targetRange": targetRange,
       "rangingMode": rangingMode,
       "installStatusLinked": installStatusLinked,
       "installArmState": installArmState,
       "tFTPServerPortNumber": tFTPServerPortNumber,
       "tFTPSoftwareUpgradeFileName": tFTPSoftwareUpgradeFileName,
       "tFTPStartSoftwareUpgrade": tFTPStartSoftwareUpgrade,
       "tFTPSoftwareUpgradeStatus": tFTPSoftwareUpgradeStatus,
       "tFTPSoftwareUpgradeStatusText": tFTPSoftwareUpgradeStatusText,
       "tFTPSoftwareUpgradeStatusAdditionalText": tFTPSoftwareUpgradeStatusAdditionalText,
       "hTTPAccessEnabled": hTTPAccessEnabled,
       "telnetAccessEnabled": telnetAccessEnabled,
       "hTTPPortNumber": hTTPPortNumber,
       "hTTPSPortNumber": hTTPSPortNumber,
       "telnetPortNumber": telnetPortNumber,
       "hTTPSAccessEnabled": hTTPSAccessEnabled,
       "tFTPServerInternetAddressType": tFTPServerInternetAddressType,
       "tFTPServerInternetAddress": tFTPServerInternetAddress,
       "lowestDataModulationMode": lowestDataModulationMode,
       "tFTPClient": tFTPClient,
       "mgmtInstancedTableNumber": mgmtInstancedTableNumber,
       "mgmtInstancedTable": mgmtInstancedTable,
       "mgmtInstancedTableEntry": mgmtInstancedTableEntry,
       "mgmtInstancedTableIndex": mgmtInstancedTableIndex,
       "installStatus": installStatus,
       "tFTPServerResolvedInternetAddress": tFTPServerResolvedInternetAddress,
       "installationMode": installationMode,
       "phyControl": phyControl,
       "linkSymmetry": linkSymmetry,
       "userConfiguredMaxModulationMode": userConfiguredMaxModulationMode,
       "linkModeOptimization": linkModeOptimization,
       "txColorCode": txColorCode,
       "rxColorCode": rxColorCode,
       "remoteMaximumTransmitPowerLinked": remoteMaximumTransmitPowerLinked,
       "phyControlInstancedTableNumber": phyControlInstancedTableNumber,
       "phyControlInstancedTable": phyControlInstancedTable,
       "phyControlInstancedTableEntry": phyControlInstancedTableEntry,
       "phyControlInstancedTableIndex": phyControlInstancedTableIndex,
       "remoteMaximumTransmitPower": remoteMaximumTransmitPower,
       "phyStatus": phyStatus,
       "linkLossLinked": linkLossLinked,
       "receivePowerLinked": receivePowerLinked,
       "vectorErrorLinked": vectorErrorLinked,
       "transmitPowerLinked": transmitPowerLinked,
       "receiveChannel": receiveChannel,
       "transmitChannel": transmitChannel,
       "receiveFreqMHz": receiveFreqMHz,
       "transmitFreqMHz": transmitFreqMHz,
       "signalStrengthRatioLinked": signalStrengthRatioLinked,
       "receiveFreqKHz": receiveFreqKHz,
       "transmitFreqKHz": transmitFreqKHz,
       "rawReceivePowerLinked": rawReceivePowerLinked,
       "rangeLinked": rangeLinked,
       "receiveModulationModeLinked": receiveModulationModeLinked,
       "transmitModulationModeLinked": transmitModulationModeLinked,
       "searchStateLinked": searchStateLinked,
       "remoteMACAddressLinked": remoteMACAddressLinked,
       "phyInstancedStatusTableNumber": phyInstancedStatusTableNumber,
       "phyInstancedStatusTable": phyInstancedStatusTable,
       "phyInstancedStatusTableEntry": phyInstancedStatusTableEntry,
       "phyInstancedStatusTableIndex": phyInstancedStatusTableIndex,
       "linkLoss": linkLoss,
       "receivePower": receivePower,
       "vectorError": vectorError,
       "signalStrengthRatio": signalStrengthRatio,
       "range": range,
       "receiveModulationMode": receiveModulationMode,
       "transmitModulationMode": transmitModulationMode,
       "searchState": searchState,
       "remoteMACAddress": remoteMACAddress,
       "rawReceivePower": rawReceivePower,
       "transmitPower": transmitPower,
       "tempPcb": tempPcb,
       "alarms": alarms,
       "unitOutOfCalibration": unitOutOfCalibration,
       "incompatibleRegulatoryBandsLinked": incompatibleRegulatoryBandsLinked,
       "noWirelessChannelAvailable": noWirelessChannelAvailable,
       "wirelessLinkDisabledWarning": wirelessLinkDisabledWarning,
       "mainPSUPortDisabledWarning": mainPSUPortDisabledWarning,
       "sFPError": sFPError,
       "mainPSUPortConfigurationMismatch": mainPSUPortConfigurationMismatch,
       "incompatibleMasterAndSlaveLinked": incompatibleMasterAndSlaveLinked,
       "tDDSynchronizationStatus": tDDSynchronizationStatus,
       "auxPortDisabledWarning": auxPortDisabledWarning,
       "tDDSynchronizationAlarm": tDDSynchronizationAlarm,
       "linkModeOptimizationMismatchLinked": linkModeOptimizationMismatchLinked,
       "auxPortConfigurationMismatch": auxPortConfigurationMismatch,
       "secureModeAlarm": secureModeAlarm,
       "dataBridgingStatusAlarmLinked": dataBridgingStatusAlarmLinked,
       "sFPPortDisabledWarning": sFPPortDisabledWarning,
       "sFPPortConfigurationMismatch": sFPPortConfigurationMismatch,
       "maxLinkRangeExceededLinked": maxLinkRangeExceededLinked,
       "nIDULanPortDisabledWarning": nIDULanPortDisabledWarning,
       "nIDULanPortConfigurationMismatch": nIDULanPortConfigurationMismatch,
       "portAllocationMismatchLinked": portAllocationMismatchLinked,
       "transparentClockSourcePortAlarm": transparentClockSourcePortAlarm,
       "alarmInstancedTableNumber": alarmInstancedTableNumber,
       "alarmInstancedTable": alarmInstancedTable,
       "alarmInstancedTableEntry": alarmInstancedTableEntry,
       "alarmInstancedTableIndex": alarmInstancedTableIndex,
       "incompatibleMasterAndSlave": incompatibleMasterAndSlave,
       "linkModeOptimizationMismatch": linkModeOptimizationMismatch,
       "dataBridgingStatusAlarm": dataBridgingStatusAlarm,
       "maxLinkRangeExceeded": maxLinkRangeExceeded,
       "portAllocationMismatch": portAllocationMismatch,
       "wirelessLinkStatusAlarm": wirelessLinkStatusAlarm,
       "incompatibleRegulatoryBands": incompatibleRegulatoryBands,
       "secureLicenseSignatureAlarm": secureLicenseSignatureAlarm,
       "apc": apc,
       "atpcHcmpMasterTargetRxPower": atpcHcmpMasterTargetRxPower,
       "atpcHcmpMasterTxPower": atpcHcmpMasterTxPower,
       "smtp": smtp,
       "sMTPEmailAlert": sMTPEmailAlert,
       "sMTPServerPortNumber": sMTPServerPortNumber,
       "sMTPSourceEmailAddress": sMTPSourceEmailAddress,
       "sMTPDestinationEmailAddress": sMTPDestinationEmailAddress,
       "sMTPEnabledMessages": sMTPEnabledMessages,
       "sMTPServerInternetAddressType": sMTPServerInternetAddressType,
       "sMTPServerInternetAddress": sMTPServerInternetAddress,
       "sMTPServerResolvedInternetAddress": sMTPServerResolvedInternetAddress,
       "snmpControl": snmpControl,
       "sNMPPortNumber": sNMPPortNumber,
       "sNMPCommunityString": sNMPCommunityString,
       "sNMPTrapTableNumber": sNMPTrapTableNumber,
       "sNMPTrapTable": sNMPTrapTable,
       "sNMPTrapTableEntry": sNMPTrapTableEntry,
       "sNMPTrapTableIndex": sNMPTrapTableIndex,
       "sNMPTrapPortNumber": sNMPTrapPortNumber,
       "sNMPTrapInternetAddressType": sNMPTrapInternetAddressType,
       "sNMPTrapInternetAddress": sNMPTrapInternetAddress,
       "sNMPTrapReceiverEnabled": sNMPTrapReceiverEnabled,
       "sNMPTrapResolvedInternetAddress": sNMPTrapResolvedInternetAddress,
       "sNMPTrapVersion": sNMPTrapVersion,
       "sNMPEnabledTraps": sNMPEnabledTraps,
       "enabledDiagnosticAlarms": enabledDiagnosticAlarms,
       "sNMPSendAllTrapsAtStartup": sNMPSendAllTrapsAtStartup,
       "sntp": sntp,
       "sNTPState": sNTPState,
       "sNTPPollInterval": sNTPPollInterval,
       "sNTPSync": sNTPSync,
       "sNTPLastSync": sNTPLastSync,
       "systemClock": systemClock,
       "timeZone": timeZone,
       "daylightSaving": daylightSaving,
       "sNTPPrimaryServer": sNTPPrimaryServer,
       "sNTPPrimaryServerDeadTime": sNTPPrimaryServerDeadTime,
       "sNTPServerRetries": sNTPServerRetries,
       "sNTPServerTimeout": sNTPServerTimeout,
       "sNTPServerTableNumber": sNTPServerTableNumber,
       "sNTPServerTable": sNTPServerTable,
       "sNTPServerTableEntry": sNTPServerTableEntry,
       "sNTPServerTableIndex": sNTPServerTableIndex,
       "sNTPServerPortNumber": sNTPServerPortNumber,
       "sNTPServerStatus": sNTPServerStatus,
       "sNTPServerInternetAddressType": sNTPServerInternetAddressType,
       "sNTPServerInternetAddress": sNTPServerInternetAddress,
       "sNTPServerResolvedInternetAddress": sNTPServerResolvedInternetAddress,
       "sNTPServerAuthenticationProtocol": sNTPServerAuthenticationProtocol,
       "sNTPServerKeyIdentifier": sNTPServerKeyIdentifier,
       "reset": reset,
       "systemReset": systemReset,
       "versions": versions,
       "softwareVersion": softwareVersion,
       "hardwareVersion": hardwareVersion,
       "secondarySoftwareVersion": secondarySoftwareVersion,
       "bootVersion": bootVersion,
       "pubStats": pubStats,
       "receiveDataRateLinked": receiveDataRateLinked,
       "transmitDataRateLinked": transmitDataRateLinked,
       "aggregateDataRateLinked": aggregateDataRateLinked,
       "wirelessLinkAvailabilityLinked": wirelessLinkAvailabilityLinked,
       "wirelessLinkStatusLinked": wirelessLinkStatusLinked,
       "byteErrorRatioLinked": byteErrorRatioLinked,
       "receiveModulationModeDetailLinked": receiveModulationModeDetailLinked,
       "dataBridgingAvailabilityLinked": dataBridgingAvailabilityLinked,
       "pubInstancedStatsTableNumber": pubInstancedStatsTableNumber,
       "pubInstancedStatsTable": pubInstancedStatsTable,
       "pubInstancedStatsTableEntry": pubInstancedStatsTableEntry,
       "pubInstancedStatsTableIndex": pubInstancedStatsTableIndex,
       "receiveDataRate": receiveDataRate,
       "transmitDataRate": transmitDataRate,
       "aggregateDataRate": aggregateDataRate,
       "wirelessLinkAvailability": wirelessLinkAvailability,
       "wirelessLinkStatus": wirelessLinkStatus,
       "receiveModulationModeDetail": receiveModulationModeDetail,
       "dataBridgingAvailability": dataBridgingAvailability,
       "byteErrorRatio": byteErrorRatio,
       "wirelessOutEthernetOctets": wirelessOutEthernetOctets,
       "wirelessOutAllOctets": wirelessOutAllOctets,
       "wirelessOutOctets": wirelessOutOctets,
       "erroredSeconds": erroredSeconds,
       "severelyErroredSeconds": severelyErroredSeconds,
       "unavailableSeconds": unavailableSeconds,
       "encryption": encryption,
       "encryptionAlgorithm": encryptionAlgorithm,
       "tLSMinimumSecurityLevel": tLSMinimumSecurityLevel,
       "tDDControl": tDDControl,
       "tDDSynchronizationMode": tDDSynchronizationMode,
       "hCMPMaximumLinkRange": hCMPMaximumLinkRange,
       "maximumNumberOfSlaves": maximumNumberOfSlaves,
       "hCMPLinkSymmetry": hCMPLinkSymmetry,
       "syslogControl": syslogControl,
       "syslogClient": syslogClient,
       "syslogState": syslogState,
       "aAAControl": aAAControl,
       "userTableNumber": userTableNumber,
       "userTable": userTable,
       "userTableEntry": userTableEntry,
       "userTableIndex": userTableIndex,
       "userName": userName,
       "userRole": userRole,
       "userEnabled": userEnabled,
       "userPassword": userPassword,
       "routerProtocols": routerProtocols,
       "microwaveAdaptiveBandwidth": microwaveAdaptiveBandwidth,
       "mABNominalModulationMode": mABNominalModulationMode,
       "mABTransmissionInterval": mABTransmissionInterval,
       "mABHoldoffPeriod": mABHoldoffPeriod,
       "mABMaintenanceLevel": mABMaintenanceLevel,
       "useVLANForMABProtocol": useVLANForMABProtocol,
       "mABProtocolVID": mABProtocolVID,
       "mABProtocolVLANPriority": mABProtocolVLANPriority,
       "mABState": mABState,
       "mABNominalTransmitCapacity": mABNominalTransmitCapacity,
       "mABCurrentTransmitCapacity": mABCurrentTransmitCapacity,
       "cableDiagnostics": cableDiagnostics,
       "cableDiagnosticsPorts": cableDiagnosticsPorts,
       "cableDiagnosticsControl": cableDiagnosticsControl,
       "cableDiagnosticsWarning": cableDiagnosticsWarning,
       "cableDiagnosticsResultTableNumber": cableDiagnosticsResultTableNumber,
       "cableDiagnosticsResultTable": cableDiagnosticsResultTable,
       "cableDiagnosticsResultTableEntry": cableDiagnosticsResultTableEntry,
       "cableDiagnosticsResultTableIndex": cableDiagnosticsResultTableIndex,
       "cableDiagnosticsResultsDateTime": cableDiagnosticsResultsDateTime,
       "cableDiagPair1Results": cableDiagPair1Results,
       "cableDiagPair1Distance": cableDiagPair1Distance,
       "cableDiagPair2Results": cableDiagPair2Results,
       "cableDiagPair2Distance": cableDiagPair2Distance,
       "cableDiagPair3Results": cableDiagPair3Results,
       "cableDiagPair3Distance": cableDiagPair3Distance,
       "cableDiagPair4Results": cableDiagPair4Results,
       "cableDiagPair4Distance": cableDiagPair4Distance,
       "unitIdentification": unitIdentification,
       "deviceMACAddress": deviceMACAddress,
       "deviceESN": deviceESN,
       "deviceMSN": deviceMSN,
       "authorizationControl": authorizationControl,
       "authorizationControlTableNumber": authorizationControlTableNumber,
       "authorizationControlTable": authorizationControlTable,
       "authorizationControlTableEntry": authorizationControlTableEntry,
       "authorizationControlTableIndex": authorizationControlTableIndex,
       "whitelistRMMacAddress": whitelistRMMacAddress,
       "whitelistRMEnabled": whitelistRMEnabled,
       "blacklistRMMacAddress": blacklistRMMacAddress,
       "blacklistRMEnabled": blacklistRMEnabled,
       "dNS": dNS,
       "dNSResolver": dNSResolver,
       "dNSPrimaryServer": dNSPrimaryServer,
       "dNSServerTableNumber": dNSServerTableNumber,
       "dNSServerTable": dNSServerTable,
       "dNSServerTableEntry": dNSServerTableEntry,
       "dNSServerTableIndex": dNSServerTableIndex,
       "dNSServerInternetAddressType": dNSServerInternetAddressType,
       "dNSServerInternetAddress": dNSServerInternetAddress,
       "dNSServerPortNumber": dNSServerPortNumber,
       "supplementary": supplementary,
       "longitude": longitude,
       "latitude": latitude,
       "altitude": altitude,
       "ptpCompliance": ptpCompliance,
       "ptpGroups": ptpGroups,
       "dfsGroup": dfsGroup,
       "bridgeGroup": bridgeGroup,
       "configurationGroup": configurationGroup,
       "ethernetGroup": ethernetGroup,
       "tDMGroup": tDMGroup,
       "licenseGroup": licenseGroup,
       "managementGroup": managementGroup,
       "phyControlGroup": phyControlGroup,
       "phyStatusGroup": phyStatusGroup,
       "alarmsGroup": alarmsGroup,
       "apcGroup": apcGroup,
       "smtpGroup": smtpGroup,
       "snmpControlGroup": snmpControlGroup,
       "sntpGroup": sntpGroup,
       "resetGroup": resetGroup,
       "versionsGroup": versionsGroup,
       "pubStatsGroup": pubStatsGroup,
       "encryptionGroup": encryptionGroup,
       "tDDControlGroup": tDDControlGroup,
       "syslogControlGroup": syslogControlGroup,
       "aAAControlGroup": aAAControlGroup,
       "routerProtocolsGroup": routerProtocolsGroup,
       "cableDiagnosticsGroup": cableDiagnosticsGroup,
       "unitIdentificationGroup": unitIdentificationGroup,
       "authorizationControlGroup": authorizationControlGroup,
       "dNSGroup": dNSGroup,
       "supplementaryGroup": supplementaryGroup,
       "notificationsGroup": notificationsGroup,
       "ptpTraps": ptpTraps,
       "ptpTrapPrefix": ptpTrapPrefix,
       "channelChangeTrap": channelChangeTrap,
       "dfsImpulsiveInterferenceTrap": dfsImpulsiveInterferenceTrap,
       "mainPSUPortStatusTrap": mainPSUPortStatusTrap,
       "mainPSUPortDisabledWarningTrap": mainPSUPortDisabledWarningTrap,
       "mainPSUPortConfigurationMismatchTrap": mainPSUPortConfigurationMismatchTrap,
       "auxPortStatusTrap": auxPortStatusTrap,
       "auxPortDisabledWarningTrap": auxPortDisabledWarningTrap,
       "regulatoryBandTrap": regulatoryBandTrap,
       "installStatusTrap": installStatusTrap,
       "installArmStateTrap": installArmStateTrap,
       "unitOutOfCalibrationTrap": unitOutOfCalibrationTrap,
       "auxPortPowerOverEthernetOutputStatusTrap": auxPortPowerOverEthernetOutputStatusTrap,
       "incompatibleRegulatoryBandsTrap": incompatibleRegulatoryBandsTrap,
       "noWirelessChannelAvailableTrap": noWirelessChannelAvailableTrap,
       "wirelessLinkDisabledWarningTrap": wirelessLinkDisabledWarningTrap,
       "auxPortConfigurationMismatchTrap": auxPortConfigurationMismatchTrap,
       "sFPErrorTrap": sFPErrorTrap,
       "sFPPortStatusTrap": sFPPortStatusTrap,
       "incompatibleMasterAndSlaveTrap": incompatibleMasterAndSlaveTrap,
       "sNTPSyncTrap": sNTPSyncTrap,
       "tDDSynchronizationAlarmTrap": tDDSynchronizationAlarmTrap,
       "sFPPortDisabledWarningTrap": sFPPortDisabledWarningTrap,
       "sFPPortConfigurationMismatchTrap": sFPPortConfigurationMismatchTrap,
       "linkModeOptimizationMismatchTrap": linkModeOptimizationMismatchTrap,
       "tDMInterfaceStatusTrap": tDMInterfaceStatusTrap,
       "tDMChannelStatusTrap": tDMChannelStatusTrap,
       "tDMChannelLoopbackTrap": tDMChannelLoopbackTrap,
       "nIDULanPortStatusTrap": nIDULanPortStatusTrap,
       "syslogStateTrap": syslogStateTrap,
       "syslogLocalNearlyFullTrap": syslogLocalNearlyFullTrap,
       "syslogLocalWrappedTrap": syslogLocalWrappedTrap,
       "syslogClientTrap": syslogClientTrap,
       "secureModeAlarmTrap": secureModeAlarmTrap,
       "dataBridgingStatusAlarmTrap": dataBridgingStatusAlarmTrap,
       "licenseRemainingTrialPeriodAlarmTrap": licenseRemainingTrialPeriodAlarmTrap,
       "capacityVariantMismatchTrap": capacityVariantMismatchTrap,
       "maxLinkRangeExceededTrap": maxLinkRangeExceededTrap,
       "tDMConfigurationMismatchTrap": tDMConfigurationMismatchTrap,
       "nIDULanPortDisabledWarningTrap": nIDULanPortDisabledWarningTrap,
       "nIDULanPortConfigurationMismatchTrap": nIDULanPortConfigurationMismatchTrap,
       "portAllocationMismatchTrap": portAllocationMismatchTrap,
       "wirelessLinkStatusAlarmTrap": wirelessLinkStatusAlarmTrap,
       "lbtDetectedTrap": lbtDetectedTrap,
       "secureLicenseSignatureAlarmTrap": secureLicenseSignatureAlarmTrap}
)
