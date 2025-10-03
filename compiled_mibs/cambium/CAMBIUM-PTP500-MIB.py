# SNMP MIB module (CAMBIUM-PTP500-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cambium\300\CAMBIUM-PTP500-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:26 2025
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
        ("2014-03-14 16:04",
         "2013-02-08 08:38",
         "2012-07-09 17:50",
         "2012-03-28 10:37",
         "2011-07-13 16:57",
         "2010-09-22 14:49",
         "2009-05-29 09:25",
         "2008-11-04 10:22",
         "2008-06-26 16:44",
         "2008-04-11 18:08")
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
_Ptp500_ObjectIdentity = ObjectIdentity
ptp500 = _Ptp500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5)
)
_Dfs_ObjectIdentity = ObjectIdentity
dfs = _Dfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 3)
)


class _DfsTableNumber_Type(Integer32):
    """Custom type dfsTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_DfsTableNumber_Type.__name__ = "Integer32"
_DfsTableNumber_Object = MibScalar
dfsTableNumber = _DfsTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 3, 1),
    _DfsTableNumber_Type()
)
dfsTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsTableNumber.setStatus("current")
_DfsTable_Object = MibTable
dfsTable = _DfsTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 3, 2)
)
if mibBuilder.loadTexts:
    dfsTable.setStatus("current")
_DfsTableEntry_Object = MibTableRow
dfsTableEntry = _DfsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 3, 2, 1)
)
dfsTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP500-MIB", "dfsTableIndex"),
)
if mibBuilder.loadTexts:
    dfsTableEntry.setStatus("current")


class _DfsTableIndex_Type(Integer32):
    """Custom type dfsTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_DfsTableIndex_Type.__name__ = "Integer32"
_DfsTableIndex_Object = MibTableColumn
dfsTableIndex = _DfsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 3, 2, 1, 1),
    _DfsTableIndex_Type()
)
dfsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dfsTableIndex.setStatus("current")
_DfsMeans_Type = Integer32
_DfsMeans_Object = MibTableColumn
dfsMeans = _DfsMeans_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 3, 2, 1, 2),
    _DfsMeans_Type()
)
dfsMeans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsMeans.setStatus("current")
_DfsNineNinePointNinePercentiles_Type = Integer32
_DfsNineNinePointNinePercentiles_Object = MibTableColumn
dfsNineNinePointNinePercentiles = _DfsNineNinePointNinePercentiles_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 3, 2, 1, 3),
    _DfsNineNinePointNinePercentiles_Type()
)
dfsNineNinePointNinePercentiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsNineNinePointNinePercentiles.setStatus("current")
_DfsPeaks_Type = Integer32
_DfsPeaks_Object = MibTableColumn
dfsPeaks = _DfsPeaks_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 3, 2, 1, 4),
    _DfsPeaks_Type()
)
dfsPeaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfsPeaks.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 5)
)
_IPAddress_Type = IpAddress
_IPAddress_Object = MibScalar
iPAddress = _IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 5, 1),
    _IPAddress_Type()
)
iPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPAddress.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 5, 2),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_GatewayIPAddress_Type = IpAddress
_GatewayIPAddress_Object = MibScalar
gatewayIPAddress = _GatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 5, 3),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 5, 4),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 5, 5),
    _MasterSlaveMode_Type()
)
masterSlaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterSlaveMode.setStatus("current")


class _MaximumTransmitPower_Type(Integer32):
    """Custom type maximumTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 27),
    )


_MaximumTransmitPower_Type.__name__ = "Integer32"
_MaximumTransmitPower_Object = MibScalar
maximumTransmitPower = _MaximumTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 5, 6),
    _MaximumTransmitPower_Type()
)
maximumTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumTransmitPower.setStatus("current")


class _AntennaGain_Type(Integer32):
    """Custom type antennaGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 610),
    )


_AntennaGain_Type.__name__ = "Integer32"
_AntennaGain_Object = MibScalar
antennaGain = _AntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 5, 7),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 5, 8),
    _CableLoss_Type()
)
cableLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableLoss.setStatus("current")
_EIRP_Type = Integer32
_EIRP_Object = MibScalar
eIRP = _EIRP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 5, 9),
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
              4)
        )
    )
    namedValues = NamedValues(
        *(("bw30MHz", 0),
          ("bw15MHz", 1),
          ("bw10MHz", 2),
          ("bw5MHz", 3),
          ("bw20MHz", 4))
    )


_ChannelBandwidth_Type.__name__ = "Integer32"
_ChannelBandwidth_Object = MibScalar
channelBandwidth = _ChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 5, 11),
    _ChannelBandwidth_Type()
)
channelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelBandwidth.setStatus("current")
_RemoteIPAddress_Type = IpAddress
_RemoteIPAddress_Object = MibScalar
remoteIPAddress = _RemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 5, 12),
    _RemoteIPAddress_Type()
)
remoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIPAddress.setStatus("current")


class _LinkName_Type(DisplayString):
    """Custom type linkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LinkName_Type.__name__ = "DisplayString"
_LinkName_Object = MibScalar
linkName = _LinkName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 5, 14),
    _LinkName_Type()
)
linkName.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 5, 15),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 5, 16),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 5, 17),
    _GroupID_Type()
)
groupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupID.setStatus("current")
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 6)
)


class _DataPortAutoNegotiation_Type(Integer32):
    """Custom type dataPortAutoNegotiation based on Integer32"""
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


_DataPortAutoNegotiation_Type.__name__ = "Integer32"
_DataPortAutoNegotiation_Object = MibScalar
dataPortAutoNegotiation = _DataPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 6, 1),
    _DataPortAutoNegotiation_Type()
)
dataPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataPortAutoNegotiation.setStatus("current")


class _DataPortAutoNegAdvertisement_Type(Bits):
    """Custom type dataPortAutoNegAdvertisement based on Bits"""
    namedValues = NamedValues(
        *(("negInvalid", 2),
          ("neg10MbpsHalfDuplex", 3),
          ("neg10MbpsFullDuplex", 4),
          ("neg100MbpsHalfDuplex", 5),
          ("neg100MbpsFullDuplex", 6),
          ("negUnknown1", 7))
    )

_DataPortAutoNegAdvertisement_Type.__name__ = "Bits"
_DataPortAutoNegAdvertisement_Object = MibScalar
dataPortAutoNegAdvertisement = _DataPortAutoNegAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 6, 2),
    _DataPortAutoNegAdvertisement_Type()
)
dataPortAutoNegAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataPortAutoNegAdvertisement.setStatus("current")


class _DataPortAutoMdix_Type(Integer32):
    """Custom type dataPortAutoMdix based on Integer32"""
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


_DataPortAutoMdix_Type.__name__ = "Integer32"
_DataPortAutoMdix_Object = MibScalar
dataPortAutoMdix = _DataPortAutoMdix_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 6, 3),
    _DataPortAutoMdix_Type()
)
dataPortAutoMdix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataPortAutoMdix.setStatus("current")


class _DataPortStatus_Type(Integer32):
    """Custom type dataPortStatus based on Integer32"""
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


_DataPortStatus_Type.__name__ = "Integer32"
_DataPortStatus_Object = MibScalar
dataPortStatus = _DataPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 6, 4),
    _DataPortStatus_Type()
)
dataPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortStatus.setStatus("current")


class _DataPortSpeedAndDuplex_Type(Integer32):
    """Custom type dataPortSpeedAndDuplex based on Integer32"""
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


_DataPortSpeedAndDuplex_Type.__name__ = "Integer32"
_DataPortSpeedAndDuplex_Object = MibScalar
dataPortSpeedAndDuplex = _DataPortSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 6, 5),
    _DataPortSpeedAndDuplex_Type()
)
dataPortSpeedAndDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortSpeedAndDuplex.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 5, 6, 6),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 6, 7),
    _UseVLANForManagementInterfaces_Type()
)
useVLANForManagementInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useVLANForManagementInterfaces.setStatus("current")


class _VLANManagementPriority_Type(Integer32):
    """Custom type vLANManagementPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VLANManagementPriority_Type.__name__ = "Integer32"
_VLANManagementPriority_Object = MibScalar
vLANManagementPriority = _VLANManagementPriority_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 6, 8),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 6, 11),
    _VLANManagementVID_Type()
)
vLANManagementVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLANManagementVID.setStatus("current")


class _VLANPriorityTableNumber_Type(Integer32):
    """Custom type vLANPriorityTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 9),
    )


_VLANPriorityTableNumber_Type.__name__ = "Integer32"
_VLANPriorityTableNumber_Object = MibScalar
vLANPriorityTableNumber = _VLANPriorityTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 6, 14),
    _VLANPriorityTableNumber_Type()
)
vLANPriorityTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLANPriorityTableNumber.setStatus("current")
_VLANPriorityTable_Object = MibTable
vLANPriorityTable = _VLANPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 6, 15)
)
if mibBuilder.loadTexts:
    vLANPriorityTable.setStatus("current")
_VLANPriorityTableEntry_Object = MibTableRow
vLANPriorityTableEntry = _VLANPriorityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 6, 15, 1)
)
vLANPriorityTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP500-MIB", "vLANPriorityTableIndex"),
)
if mibBuilder.loadTexts:
    vLANPriorityTableEntry.setStatus("current")


class _VLANPriorityQueueMapping_Type(Integer32):
    """Custom type vLANPriorityQueueMapping based on Integer32"""
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


_VLANPriorityQueueMapping_Type.__name__ = "Integer32"
_VLANPriorityQueueMapping_Object = MibTableColumn
vLANPriorityQueueMapping = _VLANPriorityQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 6, 15, 1, 1),
    _VLANPriorityQueueMapping_Type()
)
vLANPriorityQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLANPriorityQueueMapping.setStatus("current")


class _VLANPriorityTableIndex_Type(Integer32):
    """Custom type vLANPriorityTableIndex based on Integer32"""
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


_VLANPriorityTableIndex_Type.__name__ = "Integer32"
_VLANPriorityTableIndex_Object = MibTableColumn
vLANPriorityTableIndex = _VLANPriorityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 6, 15, 1, 2),
    _VLANPriorityTableIndex_Type()
)
vLANPriorityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLANPriorityTableIndex.setStatus("current")
_Telecom_ObjectIdentity = ObjectIdentity
telecom = _Telecom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 7)
)


class _TelecomsInterface_Type(Integer32):
    """Custom type telecomsInterface based on Integer32"""
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


_TelecomsInterface_Type.__name__ = "Integer32"
_TelecomsInterface_Object = MibScalar
telecomsInterface = _TelecomsInterface_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 7, 1),
    _TelecomsInterface_Type()
)
telecomsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telecomsInterface.setStatus("current")


class _TelecomsChannelStatus_Type(Integer32):
    """Custom type telecomsChannelStatus based on Integer32"""
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
        *(("disabled", 0),
          ("noSignalLocal", 1),
          ("noSignalRemote", 2),
          ("noSignalLocalandRemote", 3),
          ("up", 4),
          ("remoteTiming", 5),
          ("noSignalLocalandRemoteTiming", 6))
    )


_TelecomsChannelStatus_Type.__name__ = "Integer32"
_TelecomsChannelStatus_Object = MibScalar
telecomsChannelStatus = _TelecomsChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 7, 2),
    _TelecomsChannelStatus_Type()
)
telecomsChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telecomsChannelStatus.setStatus("current")


class _TelecomsLineCode_Type(Integer32):
    """Custom type telecomsLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aMI", 0),
          ("b8ZSHDB3", 1))
    )


_TelecomsLineCode_Type.__name__ = "Integer32"
_TelecomsLineCode_Object = MibScalar
telecomsLineCode = _TelecomsLineCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 7, 4),
    _TelecomsLineCode_Type()
)
telecomsLineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telecomsLineCode.setStatus("current")


class _TelecomsCableLength_Type(Integer32):
    """Custom type telecomsCableLength based on Integer32"""
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


_TelecomsCableLength_Type.__name__ = "Integer32"
_TelecomsCableLength_Object = MibScalar
telecomsCableLength = _TelecomsCableLength_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 7, 6),
    _TelecomsCableLength_Type()
)
telecomsCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telecomsCableLength.setStatus("current")


class _TelecomsLoopback_Type(Integer32):
    """Custom type telecomsLoopback based on Integer32"""
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


_TelecomsLoopback_Type.__name__ = "Integer32"
_TelecomsLoopback_Object = MibScalar
telecomsLoopback = _TelecomsLoopback_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 7, 8),
    _TelecomsLoopback_Type()
)
telecomsLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telecomsLoopback.setStatus("current")
_Licence_ObjectIdentity = ObjectIdentity
licence = _Licence_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 8)
)


class _RegionCode_Type(Integer32):
    """Custom type regionCode based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("regionCodeInvalid", 0),
          ("regionCode1", 1),
          ("regionCode2", 2),
          ("regionCode3", 3),
          ("regionCode4", 4),
          ("regionCode5", 5),
          ("regionCode6", 6),
          ("regionCode7", 7),
          ("regionCode8", 8),
          ("regionCode9", 9),
          ("regionCode10", 10),
          ("regionCode11", 11),
          ("regionCode12", 12),
          ("regionCode13", 13),
          ("regionCode14", 14),
          ("regionCode15", 15),
          ("regionCode16", 16),
          ("regionCode17", 17),
          ("regionCode18", 18),
          ("regionCode19", 19),
          ("regionCode20", 20),
          ("regionCode21", 21),
          ("regionCode22", 22),
          ("regionCode23", 23),
          ("regionCode24", 24),
          ("regionCode25", 25),
          ("regionCode26", 26),
          ("regionCode27", 27),
          ("regionCode28", 28),
          ("regionCode29", 29),
          ("regionCode30", 30),
          ("regionCode31", 31))
    )


_RegionCode_Type.__name__ = "Integer32"
_RegionCode_Object = MibScalar
regionCode = _RegionCode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 8, 1),
    _RegionCode_Type()
)
regionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regionCode.setStatus("current")


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
              15)
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
          ("spare5", 13),
          ("spare6", 14),
          ("pTP800", 15))
    )


_ProductVariant_Type.__name__ = "Integer32"
_ProductVariant_Object = MibScalar
productVariant = _ProductVariant_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 8, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 8, 3),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")


class _EthernetFiberSupport_Type(Integer32):
    """Custom type ethernetFiberSupport based on Integer32"""
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


_EthernetFiberSupport_Type.__name__ = "Integer32"
_EthernetFiberSupport_Object = MibScalar
ethernetFiberSupport = _EthernetFiberSupport_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 8, 4),
    _EthernetFiberSupport_Type()
)
ethernetFiberSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetFiberSupport.setStatus("current")


class _FrequencyVariant_Type(Integer32):
    """Custom type frequencyVariant based on Integer32"""
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
        *(("freq5800MHz", 0),
          ("freq5400MHz", 1),
          ("freq4900MHz", 2),
          ("freq2500MHz", 3),
          ("freq5800MHz2", 4),
          ("freq5400MHz2", 5),
          ("freq4500MHz", 6),
          ("freq5900MHz", 7),
          ("freq5200MHz", 8),
          ("freq5100MHz", 9),
          ("freq4800MHz", 10))
    )


_FrequencyVariant_Type.__name__ = "Integer32"
_FrequencyVariant_Object = MibScalar
frequencyVariant = _FrequencyVariant_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 8, 5),
    _FrequencyVariant_Type()
)
frequencyVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequencyVariant.setStatus("current")


class _BandwidthVariant_Type(Integer32):
    """Custom type bandwidthVariant based on Integer32"""
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
        *(("bw30MHz", 0),
          ("bw15MHz", 1),
          ("bw10MHz", 2),
          ("bw5MHz", 3),
          ("bw20MHz", 4))
    )


_BandwidthVariant_Type.__name__ = "Integer32"
_BandwidthVariant_Object = MibScalar
bandwidthVariant = _BandwidthVariant_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 8, 6),
    _BandwidthVariant_Type()
)
bandwidthVariant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthVariant.setStatus("current")


class _ConstantPowerSpectralDensity_Type(Integer32):
    """Custom type constantPowerSpectralDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("constant", 0),
          ("fullPower", 1))
    )


_ConstantPowerSpectralDensity_Type.__name__ = "Integer32"
_ConstantPowerSpectralDensity_Object = MibScalar
constantPowerSpectralDensity = _ConstantPowerSpectralDensity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 8, 7),
    _ConstantPowerSpectralDensity_Type()
)
constantPowerSpectralDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    constantPowerSpectralDensity.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 5, 8, 9),
    _SNMPv3Enable_Type()
)
sNMPv3Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPv3Enable.setStatus("current")


class _LicensedCapacity_Type(Integer32):
    """Custom type licensedCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("capacity25Mbps", 0),
          ("capacity52Mbps", 1),
          ("capacity105Mbps", 2))
    )


_LicensedCapacity_Type.__name__ = "Integer32"
_LicensedCapacity_Object = MibScalar
licensedCapacity = _LicensedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 8, 11),
    _LicensedCapacity_Type()
)
licensedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licensedCapacity.setStatus("current")
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 9)
)


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
_InstallStatus_Object = MibScalar
installStatus = _InstallStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 9, 3),
    _InstallStatus_Type()
)
installStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installStatus.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 5, 9, 4),
    _InstallArmState_Type()
)
installArmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installArmState.setStatus("current")
_TFTPServerIPAddress_Type = IpAddress
_TFTPServerIPAddress_Object = MibScalar
tFTPServerIPAddress = _TFTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 9, 5),
    _TFTPServerIPAddress_Type()
)
tFTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFTPServerIPAddress.setStatus("current")


class _TFTPServerPortNumber_Type(Integer32):
    """Custom type tFTPServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TFTPServerPortNumber_Type.__name__ = "Integer32"
_TFTPServerPortNumber_Object = MibScalar
tFTPServerPortNumber = _TFTPServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 9, 6),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 9, 7),
    _TFTPSoftwareUpgradeFileName_Type()
)
tFTPSoftwareUpgradeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tFTPSoftwareUpgradeFileName.setStatus("current")
_TFTPStartSoftwareUpgrade_Type = Integer32
_TFTPStartSoftwareUpgrade_Object = MibScalar
tFTPStartSoftwareUpgrade = _TFTPStartSoftwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 9, 8),
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
              4)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("uploadinprogress", 1),
          ("uploadsuccessfulprogrammingFLASH", 2),
          ("upgradesuccessfulreboottorunthenewsoftwareimage", 3),
          ("upgradefailed", 4))
    )


_TFTPSoftwareUpgradeStatus_Type.__name__ = "Integer32"
_TFTPSoftwareUpgradeStatus_Object = MibScalar
tFTPSoftwareUpgradeStatus = _TFTPSoftwareUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 9, 9),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 9, 10),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 9, 11),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 9, 12),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 9, 13),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 9, 14),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 9, 15),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 9, 16),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 9, 17),
    _HTTPSAccessEnabled_Type()
)
hTTPSAccessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hTTPSAccessEnabled.setStatus("current")
_PhyControl_ObjectIdentity = ObjectIdentity
phyControl = _PhyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 10)
)


class _LinkSymmetry_Type(Integer32):
    """Custom type linkSymmetry based on Integer32"""
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
        *(("symmetryAdaptive", 0),
          ("symmetry3to1", 1),
          ("symmetry1to1", 2),
          ("symmetry1to3", 3))
    )


_LinkSymmetry_Type.__name__ = "Integer32"
_LinkSymmetry_Object = MibScalar
linkSymmetry = _LinkSymmetry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 10, 1),
    _LinkSymmetry_Type()
)
linkSymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSymmetry.setStatus("current")


class _LinkModeOptimisation_Type(Integer32):
    """Custom type linkModeOptimisation based on Integer32"""
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


_LinkModeOptimisation_Type.__name__ = "Integer32"
_LinkModeOptimisation_Object = MibScalar
linkModeOptimisation = _LinkModeOptimisation_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 10, 2),
    _LinkModeOptimisation_Type()
)
linkModeOptimisation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkModeOptimisation.setStatus("current")


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
              6)
        )
    )
    namedValues = NamedValues(
        *(("modBpsk50percent", 0),
          ("modQpsk50percent", 1),
          ("modQpsk75percent", 2),
          ("mod16qam50percent", 3),
          ("mod16qam75percent", 4),
          ("mod64qam67percent", 5),
          ("mod64qam83percent", 6))
    )


_UserConfiguredMaxModulationMode_Type.__name__ = "Integer32"
_UserConfiguredMaxModulationMode_Object = MibScalar
userConfiguredMaxModulationMode = _UserConfiguredMaxModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 10, 3),
    _UserConfiguredMaxModulationMode_Type()
)
userConfiguredMaxModulationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userConfiguredMaxModulationMode.setStatus("current")


class _RemoteMaximumTransmitPower_Type(Integer32):
    """Custom type remoteMaximumTransmitPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 27),
    )


_RemoteMaximumTransmitPower_Type.__name__ = "Integer32"
_RemoteMaximumTransmitPower_Object = MibScalar
remoteMaximumTransmitPower = _RemoteMaximumTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 10, 4),
    _RemoteMaximumTransmitPower_Type()
)
remoteMaximumTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMaximumTransmitPower.setStatus("current")
_PhyStatus_ObjectIdentity = ObjectIdentity
phyStatus = _PhyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12)
)
_ReceivePower_Type = Integer32
_ReceivePower_Object = MibScalar
receivePower = _ReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12, 1),
    _ReceivePower_Type()
)
receivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivePower.setStatus("current")
_VectorError_Type = Integer32
_VectorError_Object = MibScalar
vectorError = _VectorError_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12, 2),
    _VectorError_Type()
)
vectorError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vectorError.setStatus("current")
_TransmitPower_Type = Integer32
_TransmitPower_Object = MibScalar
transmitPower = _TransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12, 3),
    _TransmitPower_Type()
)
transmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitPower.setStatus("current")
_Range_Type = Integer32
_Range_Object = MibScalar
range = _Range_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12, 4),
    _Range_Type()
)
range.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    range.setStatus("current")


class _LinkLoss_Type(Integer32):
    """Custom type linkLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 500),
    )


_LinkLoss_Type.__name__ = "Integer32"
_LinkLoss_Object = MibScalar
linkLoss = _LinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12, 5),
    _LinkLoss_Type()
)
linkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLoss.setStatus("current")


class _ReceiveChannel_Type(Integer32):
    """Custom type receiveChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ReceiveChannel_Type.__name__ = "Integer32"
_ReceiveChannel_Object = MibScalar
receiveChannel = _ReceiveChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12, 6),
    _ReceiveChannel_Type()
)
receiveChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveChannel.setStatus("current")


class _TransmitChannel_Type(Integer32):
    """Custom type transmitChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TransmitChannel_Type.__name__ = "Integer32"
_TransmitChannel_Object = MibScalar
transmitChannel = _TransmitChannel_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12, 7),
    _TransmitChannel_Type()
)
transmitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitChannel.setStatus("current")


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
              15)
        )
    )
    namedValues = NamedValues(
        *(("modAcquisition", 0),
          ("modBpsk50percent", 1),
          ("modQpsk50percentSingle", 2),
          ("modQpsk75percentSingle", 3),
          ("mod16qam50percentSingle", 4),
          ("mod16qam75percentSingle", 5),
          ("mod64qam67percentSingle", 6),
          ("mod64qam83percentSingle", 7),
          ("modReserved1", 8),
          ("modQpsk50percentDual", 9),
          ("modQpsk75percentDual", 10),
          ("mod16qam50percentDual", 11),
          ("mod16qam75percentDual", 12),
          ("mod64qam67percentDual", 13),
          ("mod64qam83percentDual", 14),
          ("modReserved2", 15))
    )


_ReceiveModulationMode_Type.__name__ = "Integer32"
_ReceiveModulationMode_Object = MibScalar
receiveModulationMode = _ReceiveModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12, 8),
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("modAcquisition", 0),
          ("modBpsk50percent", 1),
          ("modQpsk50percentSingle", 2),
          ("modQpsk75percentSingle", 3),
          ("mod16qam50percentSingle", 4),
          ("mod16qam75percentSingle", 5),
          ("mod64qam67percentSingle", 6),
          ("mod64qam83percentSingle", 7),
          ("modReserved1", 8),
          ("modQpsk50percentDual", 9),
          ("modQpsk75percentDual", 10),
          ("mod16qam50percentDual", 11),
          ("mod16qam75percentDual", 12),
          ("mod64qam67percentDual", 13),
          ("mod64qam83percentDual", 14),
          ("modReserved2", 15))
    )


_TransmitModulationMode_Type.__name__ = "Integer32"
_TransmitModulationMode_Object = MibScalar
transmitModulationMode = _TransmitModulationMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12, 9),
    _TransmitModulationMode_Type()
)
transmitModulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitModulationMode.setStatus("current")


class _ReceiveFreqMHz_Type(Integer32):
    """Custom type receiveFreqMHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5925),
    )


_ReceiveFreqMHz_Type.__name__ = "Integer32"
_ReceiveFreqMHz_Object = MibScalar
receiveFreqMHz = _ReceiveFreqMHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12, 11),
    _ReceiveFreqMHz_Type()
)
receiveFreqMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveFreqMHz.setStatus("current")


class _TransmitFreqMHz_Type(Integer32):
    """Custom type transmitFreqMHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5925),
    )


_TransmitFreqMHz_Type.__name__ = "Integer32"
_TransmitFreqMHz_Object = MibScalar
transmitFreqMHz = _TransmitFreqMHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12, 12),
    _TransmitFreqMHz_Type()
)
transmitFreqMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitFreqMHz.setStatus("current")
_SignalStrengthRatio_Type = Integer32
_SignalStrengthRatio_Object = MibScalar
signalStrengthRatio = _SignalStrengthRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12, 13),
    _SignalStrengthRatio_Type()
)
signalStrengthRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalStrengthRatio.setStatus("current")


class _ReceiveFreqKHz_Type(Integer32):
    """Custom type receiveFreqKHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5925000),
    )


_ReceiveFreqKHz_Type.__name__ = "Integer32"
_ReceiveFreqKHz_Object = MibScalar
receiveFreqKHz = _ReceiveFreqKHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12, 14),
    _ReceiveFreqKHz_Type()
)
receiveFreqKHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveFreqKHz.setStatus("current")


class _TransmitFreqKHz_Type(Integer32):
    """Custom type transmitFreqKHz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5925000),
    )


_TransmitFreqKHz_Type.__name__ = "Integer32"
_TransmitFreqKHz_Object = MibScalar
transmitFreqKHz = _TransmitFreqKHz_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12, 15),
    _TransmitFreqKHz_Type()
)
transmitFreqKHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitFreqKHz.setStatus("current")


class _SearchState_Type(Integer32):
    """Custom type searchState based on Integer32"""
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
        *(("registering", 0),
          ("searching", 1),
          ("acquiring", 2),
          ("registeringAcquiring2", 3))
    )


_SearchState_Type.__name__ = "Integer32"
_SearchState_Object = MibScalar
searchState = _SearchState_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 12, 16),
    _SearchState_Type()
)
searchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    searchState.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 13)
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 13, 1),
    _UnitOutOfCalibration_Type()
)
unitOutOfCalibration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitOutOfCalibration.setStatus("current")


class _IncompatibleRegionCodes_Type(Integer32):
    """Custom type incompatibleRegionCodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("incompatibleLicenceKeys", 1))
    )


_IncompatibleRegionCodes_Type.__name__ = "Integer32"
_IncompatibleRegionCodes_Object = MibScalar
incompatibleRegionCodes = _IncompatibleRegionCodes_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 13, 4),
    _IncompatibleRegionCodes_Type()
)
incompatibleRegionCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incompatibleRegionCodes.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 5, 13, 5),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 13, 6),
    _WirelessLinkDisabledWarning_Type()
)
wirelessLinkDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkDisabledWarning.setStatus("current")


class _DataPortDisabledWarning_Type(Integer32):
    """Custom type dataPortDisabledWarning based on Integer32"""
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


_DataPortDisabledWarning_Type.__name__ = "Integer32"
_DataPortDisabledWarning_Object = MibScalar
dataPortDisabledWarning = _DataPortDisabledWarning_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 13, 7),
    _DataPortDisabledWarning_Type()
)
dataPortDisabledWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortDisabledWarning.setStatus("current")


class _DataPortConfigurationMismatch_Type(Integer32):
    """Custom type dataPortConfigurationMismatch based on Integer32"""
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


_DataPortConfigurationMismatch_Type.__name__ = "Integer32"
_DataPortConfigurationMismatch_Object = MibScalar
dataPortConfigurationMismatch = _DataPortConfigurationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 13, 9),
    _DataPortConfigurationMismatch_Type()
)
dataPortConfigurationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataPortConfigurationMismatch.setStatus("current")


class _IncompatibleMasterAndSlave_Type(Integer32):
    """Custom type incompatibleMasterAndSlave based on Integer32"""
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
          ("incompatibleProductVariants", 1),
          ("differentSoftwareVersionsRunning", 2))
    )


_IncompatibleMasterAndSlave_Type.__name__ = "Integer32"
_IncompatibleMasterAndSlave_Object = MibScalar
incompatibleMasterAndSlave = _IncompatibleMasterAndSlave_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 13, 10),
    _IncompatibleMasterAndSlave_Type()
)
incompatibleMasterAndSlave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    incompatibleMasterAndSlave.setStatus("current")


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
              8)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("holdover", 1),
          ("holdoverNotConnected", 2),
          ("acquiringLock", 3),
          ("noTimingReference", 4),
          ("timingSystemNotConnected", 5),
          ("initialising", 6),
          ("clusterTimingMaster", 7),
          ("tDDSyncNotActive", 8))
    )


_TDDSynchronizationStatus_Type.__name__ = "Integer32"
_TDDSynchronizationStatus_Object = MibScalar
tDDSynchronizationStatus = _TDDSynchronizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 13, 11),
    _TDDSynchronizationStatus_Type()
)
tDDSynchronizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDDSynchronizationStatus.setStatus("current")


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
          ("notSynchronized", 1),
          ("timingSystemFailure", 2))
    )


_TDDSynchronizationAlarm_Type.__name__ = "Integer32"
_TDDSynchronizationAlarm_Object = MibScalar
tDDSynchronizationAlarm = _TDDSynchronizationAlarm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 13, 13),
    _TDDSynchronizationAlarm_Type()
)
tDDSynchronizationAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDDSynchronizationAlarm.setStatus("current")


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
_LinkModeOptimizationMismatch_Object = MibScalar
linkModeOptimizationMismatch = _LinkModeOptimizationMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 13, 14),
    _LinkModeOptimizationMismatch_Type()
)
linkModeOptimizationMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkModeOptimizationMismatch.setStatus("current")


class _CapacityLicenseMismatch_Type(Integer32):
    """Custom type capacityLicenseMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("mismatchDetected", 1))
    )


_CapacityLicenseMismatch_Type.__name__ = "Integer32"
_CapacityLicenseMismatch_Object = MibScalar
capacityLicenseMismatch = _CapacityLicenseMismatch_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 13, 16),
    _CapacityLicenseMismatch_Type()
)
capacityLicenseMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capacityLicenseMismatch.setStatus("current")
_Smtp_ObjectIdentity = ObjectIdentity
smtp = _Smtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 15)
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 15, 1),
    _SMTPEmailAlert_Type()
)
sMTPEmailAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPEmailAlert.setStatus("current")
_SMTPServerIPAddress_Type = IpAddress
_SMTPServerIPAddress_Object = MibScalar
sMTPServerIPAddress = _SMTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 15, 2),
    _SMTPServerIPAddress_Type()
)
sMTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPServerIPAddress.setStatus("current")


class _SMTPServerPortNumber_Type(Integer32):
    """Custom type sMTPServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SMTPServerPortNumber_Type.__name__ = "Integer32"
_SMTPServerPortNumber_Object = MibScalar
sMTPServerPortNumber = _SMTPServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 15, 3),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 15, 4),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 15, 5),
    _SMTPDestinationEmailAddress_Type()
)
sMTPDestinationEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPDestinationEmailAddress.setStatus("current")


class _SMTPEnabledMessages_Type(Bits):
    """Custom type sMTPEnabledMessages based on Bits"""
    namedValues = NamedValues(
        *(("telecomsChannelUpDown", 1),
          ("unknown6", 2),
          ("dataPortUpDown", 3),
          ("enabledDiagnosticAlarms", 4),
          ("dFSImpulseInterference", 5),
          ("channelChange", 6),
          ("wirelessLinkUpDown", 7))
    )

_SMTPEnabledMessages_Type.__name__ = "Bits"
_SMTPEnabledMessages_Object = MibScalar
sMTPEnabledMessages = _SMTPEnabledMessages_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 15, 6),
    _SMTPEnabledMessages_Type()
)
sMTPEnabledMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sMTPEnabledMessages.setStatus("current")
_SnmpControl_ObjectIdentity = ObjectIdentity
snmpControl = _SnmpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 16)
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 16, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 16, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 16, 3),
    _SNMPTrapTableNumber_Type()
)
sNMPTrapTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMPTrapTableNumber.setStatus("current")
_SNMPTrapTable_Object = MibTable
sNMPTrapTable = _SNMPTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 16, 4)
)
if mibBuilder.loadTexts:
    sNMPTrapTable.setStatus("current")
_SNMPTrapTableEntry_Object = MibTableRow
sNMPTrapTableEntry = _SNMPTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 16, 4, 1)
)
sNMPTrapTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP500-MIB", "sNMPTrapTableIndex"),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 16, 4, 1, 1),
    _SNMPTrapTableIndex_Type()
)
sNMPTrapTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sNMPTrapTableIndex.setStatus("current")
_SNMPTrapIPAddress_Type = IpAddress
_SNMPTrapIPAddress_Object = MibTableColumn
sNMPTrapIPAddress = _SNMPTrapIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 16, 4, 1, 2),
    _SNMPTrapIPAddress_Type()
)
sNMPTrapIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPTrapIPAddress.setStatus("current")


class _SNMPTrapPortNumber_Type(Integer32):
    """Custom type sNMPTrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SNMPTrapPortNumber_Type.__name__ = "Integer32"
_SNMPTrapPortNumber_Object = MibTableColumn
sNMPTrapPortNumber = _SNMPTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 16, 4, 1, 3),
    _SNMPTrapPortNumber_Type()
)
sNMPTrapPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPTrapPortNumber.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 17713, 5, 16, 5),
    _SNMPTrapVersion_Type()
)
sNMPTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPTrapVersion.setStatus("current")


class _SNMPEnabledTraps_Type(Bits):
    """Custom type sNMPEnabledTraps based on Bits"""
    namedValues = NamedValues(
        *(("unknown8", 0),
          ("dataPortUpDown", 1),
          ("authenticationFailure", 2),
          ("enabledDiagnosticAlarms", 3),
          ("dFSImpulseInterference", 4),
          ("channelChange", 5),
          ("wirelessLinkUpDown", 6),
          ("coldStart", 7),
          ("telecomsChannelUpDown", 15))
    )

_SNMPEnabledTraps_Type.__name__ = "Bits"
_SNMPEnabledTraps_Object = MibScalar
sNMPEnabledTraps = _SNMPEnabledTraps_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 16, 6),
    _SNMPEnabledTraps_Type()
)
sNMPEnabledTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPEnabledTraps.setStatus("current")


class _EnabledDiagnosticAlarms_Type(Bits):
    """Custom type enabledDiagnosticAlarms based on Bits"""
    namedValues = NamedValues(
        *(("incompatibleMasterAndSlave", 0),
          ("incompatibleRegionCodes", 1),
          ("unknown6", 2),
          ("unknown5", 3),
          ("unitOutOfCalibration", 4),
          ("installArmState", 5),
          ("installStatus", 6),
          ("regionCode", 7),
          ("telecomsChannelStatus", 8),
          ("unknown15", 9),
          ("dataPortStatus", 10),
          ("dataPortDisabledWarning", 11),
          ("wirelessLinkDisabledWarning", 12),
          ("sNTPSynchronizationFailed", 13),
          ("noWirelessChannelAvailable", 14),
          ("dataPortConfigurationMismatch", 15),
          ("syslogClientDisabledWarning", 16),
          ("licensedCapacityMismatch", 17),
          ("syslogLocalWrapped", 18),
          ("syslogLocalNearlyFull", 19),
          ("syslogLocalEnableDisable", 20),
          ("linkModeOptimizationMismatch", 21),
          ("tDDSynchronizationAlarm", 22),
          ("telecomsChannelLoopback", 23))
    )

_EnabledDiagnosticAlarms_Type.__name__ = "Bits"
_EnabledDiagnosticAlarms_Object = MibScalar
enabledDiagnosticAlarms = _EnabledDiagnosticAlarms_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 16, 7),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 16, 8),
    _SNMPSendAllTrapsAtStartup_Type()
)
sNMPSendAllTrapsAtStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNMPSendAllTrapsAtStartup.setStatus("current")
_Sntp_ObjectIdentity = ObjectIdentity
sntp = _Sntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 17)
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 17, 1),
    _SNTPState_Type()
)
sNTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPState.setStatus("current")
_SNTPServerIPAddress_Type = IpAddress
_SNTPServerIPAddress_Object = MibScalar
sNTPServerIPAddress = _SNTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 17, 2),
    _SNTPServerIPAddress_Type()
)
sNTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPServerIPAddress.setStatus("current")


class _SNTPServerPortNumber_Type(Integer32):
    """Custom type sNTPServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SNTPServerPortNumber_Type.__name__ = "Integer32"
_SNTPServerPortNumber_Object = MibScalar
sNTPServerPortNumber = _SNTPServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 17, 3),
    _SNTPServerPortNumber_Type()
)
sNTPServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sNTPServerPortNumber.setStatus("current")


class _SNTPPollInterval_Type(Integer32):
    """Custom type sNTPPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 43200),
    )


_SNTPPollInterval_Type.__name__ = "Integer32"
_SNTPPollInterval_Object = MibScalar
sNTPPollInterval = _SNTPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 17, 4),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 17, 5),
    _SNTPSync_Type()
)
sNTPSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPSync.setStatus("current")
_SNTPLastSync_Type = Integer32
_SNTPLastSync_Object = MibScalar
sNTPLastSync = _SNTPLastSync_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 17, 6),
    _SNTPLastSync_Type()
)
sNTPLastSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNTPLastSync.setStatus("current")
_SystemClock_Type = Integer32
_SystemClock_Object = MibScalar
systemClock = _SystemClock_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 17, 7),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 17, 8),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 17, 9),
    _DaylightSaving_Type()
)
daylightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daylightSaving.setStatus("current")
_Reset_ObjectIdentity = ObjectIdentity
reset = _Reset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 18)
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 18, 1),
    _SystemReset_Type()
)
systemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReset.setStatus("current")
_Versions_ObjectIdentity = ObjectIdentity
versions = _Versions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 19)
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 19, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 19, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 19, 3),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 19, 4),
    _BootVersion_Type()
)
bootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootVersion.setStatus("current")
_PubStats_ObjectIdentity = ObjectIdentity
pubStats = _PubStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 20)
)
_ReceiveDataRate_Type = Integer32
_ReceiveDataRate_Object = MibScalar
receiveDataRate = _ReceiveDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 20, 1),
    _ReceiveDataRate_Type()
)
receiveDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveDataRate.setStatus("current")
_TransmitDataRate_Type = Integer32
_TransmitDataRate_Object = MibScalar
transmitDataRate = _TransmitDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 20, 2),
    _TransmitDataRate_Type()
)
transmitDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transmitDataRate.setStatus("current")
_AggregateDataRate_Type = Integer32
_AggregateDataRate_Object = MibScalar
aggregateDataRate = _AggregateDataRate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 20, 3),
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
_WirelessLinkAvailability_Object = MibScalar
wirelessLinkAvailability = _WirelessLinkAvailability_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 20, 4),
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
          ("acquiring", 2),
          ("searching", 3),
          ("radarCAC", 4),
          ("initialising", 5))
    )


_WirelessLinkStatus_Type.__name__ = "Integer32"
_WirelessLinkStatus_Object = MibScalar
wirelessLinkStatus = _WirelessLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 20, 5),
    _WirelessLinkStatus_Type()
)
wirelessLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLinkStatus.setStatus("current")
_ByteErrorRatio_Type = Integer32
_ByteErrorRatio_Object = MibScalar
byteErrorRatio = _ByteErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 20, 6),
    _ByteErrorRatio_Type()
)
byteErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    byteErrorRatio.setStatus("current")


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
              8)
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
          ("limitedByTheWirelessConditions", 8))
    )


_ReceiveModulationModeDetail_Type.__name__ = "Integer32"
_ReceiveModulationModeDetail_Object = MibScalar
receiveModulationModeDetail = _ReceiveModulationModeDetail_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 20, 7),
    _ReceiveModulationModeDetail_Type()
)
receiveModulationModeDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiveModulationModeDetail.setStatus("current")
_Encryption_ObjectIdentity = ObjectIdentity
encryption = _Encryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 22)
)


class _EncryptionAlgorithm_Type(Integer32):
    """Custom type encryptionAlgorithm based on Integer32"""
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
          ("aESRijndael", 1),
          ("aES256bitRijndael", 2))
    )


_EncryptionAlgorithm_Type.__name__ = "Integer32"
_EncryptionAlgorithm_Object = MibScalar
encryptionAlgorithm = _EncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 22, 1),
    _EncryptionAlgorithm_Type()
)
encryptionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionAlgorithm.setStatus("current")
_TDDControl_ObjectIdentity = ObjectIdentity
tDDControl = _TDDControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 23)
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 23, 1),
    _TDDSynchronizationMode_Type()
)
tDDSynchronizationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDDSynchronizationMode.setStatus("current")
_SyslogControl_ObjectIdentity = ObjectIdentity
syslogControl = _SyslogControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 24)
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 24, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 24, 2),
    _SyslogState_Type()
)
syslogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogState.setStatus("current")
_AAAControl_ObjectIdentity = ObjectIdentity
aAAControl = _AAAControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 25)
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 25, 1),
    _UserTableNumber_Type()
)
userTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userTableNumber.setStatus("current")
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 25, 2)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserTableEntry_Object = MibTableRow
userTableEntry = _UserTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 25, 2, 1)
)
userTableEntry.setIndexNames(
    (0, "CAMBIUM-PTP500-MIB", "userTableIndex"),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 25, 2, 1, 1),
    _UserTableIndex_Type()
)
userTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userTableIndex.setStatus("current")
_UserName_Type = OctetString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 25, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 25, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 25, 2, 1, 4),
    _UserEnabled_Type()
)
userEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userEnabled.setStatus("current")
_UserPassword_Type = OctetString
_UserPassword_Object = MibTableColumn
userPassword = _UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 25, 2, 1, 5),
    _UserPassword_Type()
)
userPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPassword.setStatus("current")
_Supplementary_ObjectIdentity = ObjectIdentity
supplementary = _Supplementary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 96)
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 96, 1),
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
    (1, 3, 6, 1, 4, 1, 17713, 5, 96, 2),
    _Latitude_Type()
)
latitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latitude.setStatus("current")
_Altitude_Type = Integer32
_Altitude_Object = MibScalar
altitude = _Altitude_Object(
    (1, 3, 6, 1, 4, 1, 17713, 5, 96, 3),
    _Altitude_Type()
)
altitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altitude.setStatus("current")
_PtpGroups_ObjectIdentity = ObjectIdentity
ptpGroups = _PtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98)
)
_PtpTraps_ObjectIdentity = ObjectIdentity
ptpTraps = _PtpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99)
)
_PtpTrapPrefix_ObjectIdentity = ObjectIdentity
ptpTrapPrefix = _PtpTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0)
)

# Managed Objects groups

dfsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 3)
)
dfsGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "dfsTableNumber"),
        ("CAMBIUM-PTP500-MIB", "dfsMeans"),
        ("CAMBIUM-PTP500-MIB", "dfsNineNinePointNinePercentiles"),
        ("CAMBIUM-PTP500-MIB", "dfsPeaks"))
)
if mibBuilder.loadTexts:
    dfsGroup.setStatus("current")

configurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 5)
)
configurationGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "iPAddress"),
        ("CAMBIUM-PTP500-MIB", "subnetMask"),
        ("CAMBIUM-PTP500-MIB", "gatewayIPAddress"),
        ("CAMBIUM-PTP500-MIB", "targetMACAddress"),
        ("CAMBIUM-PTP500-MIB", "masterSlaveMode"),
        ("CAMBIUM-PTP500-MIB", "maximumTransmitPower"),
        ("CAMBIUM-PTP500-MIB", "antennaGain"),
        ("CAMBIUM-PTP500-MIB", "cableLoss"),
        ("CAMBIUM-PTP500-MIB", "eIRP"),
        ("CAMBIUM-PTP500-MIB", "channelBandwidth"),
        ("CAMBIUM-PTP500-MIB", "remoteIPAddress"),
        ("CAMBIUM-PTP500-MIB", "linkName"),
        ("CAMBIUM-PTP500-MIB", "siteName"),
        ("CAMBIUM-PTP500-MIB", "accessMethod"),
        ("CAMBIUM-PTP500-MIB", "groupID"))
)
if mibBuilder.loadTexts:
    configurationGroup.setStatus("current")

ethernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 6)
)
ethernetGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "dataPortAutoNegotiation"),
        ("CAMBIUM-PTP500-MIB", "dataPortAutoNegAdvertisement"),
        ("CAMBIUM-PTP500-MIB", "dataPortAutoMdix"),
        ("CAMBIUM-PTP500-MIB", "dataPortStatus"),
        ("CAMBIUM-PTP500-MIB", "dataPortSpeedAndDuplex"),
        ("CAMBIUM-PTP500-MIB", "dataPortWirelessDownAlert"),
        ("CAMBIUM-PTP500-MIB", "useVLANForManagementInterfaces"),
        ("CAMBIUM-PTP500-MIB", "vLANManagementPriority"),
        ("CAMBIUM-PTP500-MIB", "vLANManagementVID"),
        ("CAMBIUM-PTP500-MIB", "vLANPriorityTableNumber"),
        ("CAMBIUM-PTP500-MIB", "vLANPriorityQueueMapping"))
)
if mibBuilder.loadTexts:
    ethernetGroup.setStatus("current")

telecomGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 7)
)
telecomGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "telecomsInterface"),
        ("CAMBIUM-PTP500-MIB", "telecomsChannelStatus"),
        ("CAMBIUM-PTP500-MIB", "telecomsLineCode"),
        ("CAMBIUM-PTP500-MIB", "telecomsCableLength"),
        ("CAMBIUM-PTP500-MIB", "telecomsLoopback"))
)
if mibBuilder.loadTexts:
    telecomGroup.setStatus("current")

licenceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 8)
)
licenceGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "regionCode"),
        ("CAMBIUM-PTP500-MIB", "productVariant"),
        ("CAMBIUM-PTP500-MIB", "productName"),
        ("CAMBIUM-PTP500-MIB", "ethernetFiberSupport"),
        ("CAMBIUM-PTP500-MIB", "frequencyVariant"),
        ("CAMBIUM-PTP500-MIB", "bandwidthVariant"),
        ("CAMBIUM-PTP500-MIB", "constantPowerSpectralDensity"),
        ("CAMBIUM-PTP500-MIB", "sNMPv3Enable"),
        ("CAMBIUM-PTP500-MIB", "licensedCapacity"))
)
if mibBuilder.loadTexts:
    licenceGroup.setStatus("current")

managementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 9)
)
managementGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "installStatus"),
        ("CAMBIUM-PTP500-MIB", "installArmState"),
        ("CAMBIUM-PTP500-MIB", "tFTPServerIPAddress"),
        ("CAMBIUM-PTP500-MIB", "tFTPServerPortNumber"),
        ("CAMBIUM-PTP500-MIB", "tFTPSoftwareUpgradeFileName"),
        ("CAMBIUM-PTP500-MIB", "tFTPStartSoftwareUpgrade"),
        ("CAMBIUM-PTP500-MIB", "tFTPSoftwareUpgradeStatus"),
        ("CAMBIUM-PTP500-MIB", "tFTPSoftwareUpgradeStatusText"),
        ("CAMBIUM-PTP500-MIB", "tFTPSoftwareUpgradeStatusAdditionalText"),
        ("CAMBIUM-PTP500-MIB", "hTTPAccessEnabled"),
        ("CAMBIUM-PTP500-MIB", "telnetAccessEnabled"),
        ("CAMBIUM-PTP500-MIB", "hTTPPortNumber"),
        ("CAMBIUM-PTP500-MIB", "hTTPSPortNumber"),
        ("CAMBIUM-PTP500-MIB", "telnetPortNumber"),
        ("CAMBIUM-PTP500-MIB", "hTTPSAccessEnabled"))
)
if mibBuilder.loadTexts:
    managementGroup.setStatus("current")

phyControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 10)
)
phyControlGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "linkSymmetry"),
        ("CAMBIUM-PTP500-MIB", "linkModeOptimisation"),
        ("CAMBIUM-PTP500-MIB", "userConfiguredMaxModulationMode"),
        ("CAMBIUM-PTP500-MIB", "remoteMaximumTransmitPower"))
)
if mibBuilder.loadTexts:
    phyControlGroup.setStatus("current")

phyStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 12)
)
phyStatusGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "receivePower"),
        ("CAMBIUM-PTP500-MIB", "vectorError"),
        ("CAMBIUM-PTP500-MIB", "transmitPower"),
        ("CAMBIUM-PTP500-MIB", "range"),
        ("CAMBIUM-PTP500-MIB", "linkLoss"),
        ("CAMBIUM-PTP500-MIB", "receiveChannel"),
        ("CAMBIUM-PTP500-MIB", "transmitChannel"),
        ("CAMBIUM-PTP500-MIB", "receiveModulationMode"),
        ("CAMBIUM-PTP500-MIB", "transmitModulationMode"),
        ("CAMBIUM-PTP500-MIB", "receiveFreqMHz"),
        ("CAMBIUM-PTP500-MIB", "transmitFreqMHz"),
        ("CAMBIUM-PTP500-MIB", "signalStrengthRatio"),
        ("CAMBIUM-PTP500-MIB", "receiveFreqKHz"),
        ("CAMBIUM-PTP500-MIB", "transmitFreqKHz"),
        ("CAMBIUM-PTP500-MIB", "searchState"))
)
if mibBuilder.loadTexts:
    phyStatusGroup.setStatus("current")

alarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 13)
)
alarmsGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "unitOutOfCalibration"),
        ("CAMBIUM-PTP500-MIB", "incompatibleRegionCodes"),
        ("CAMBIUM-PTP500-MIB", "noWirelessChannelAvailable"),
        ("CAMBIUM-PTP500-MIB", "wirelessLinkDisabledWarning"),
        ("CAMBIUM-PTP500-MIB", "dataPortDisabledWarning"),
        ("CAMBIUM-PTP500-MIB", "dataPortConfigurationMismatch"),
        ("CAMBIUM-PTP500-MIB", "incompatibleMasterAndSlave"),
        ("CAMBIUM-PTP500-MIB", "tDDSynchronizationStatus"),
        ("CAMBIUM-PTP500-MIB", "tDDSynchronizationAlarm"),
        ("CAMBIUM-PTP500-MIB", "linkModeOptimizationMismatch"),
        ("CAMBIUM-PTP500-MIB", "capacityLicenseMismatch"))
)
if mibBuilder.loadTexts:
    alarmsGroup.setStatus("current")

smtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 15)
)
smtpGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "sMTPEmailAlert"),
        ("CAMBIUM-PTP500-MIB", "sMTPServerIPAddress"),
        ("CAMBIUM-PTP500-MIB", "sMTPServerPortNumber"),
        ("CAMBIUM-PTP500-MIB", "sMTPSourceEmailAddress"),
        ("CAMBIUM-PTP500-MIB", "sMTPDestinationEmailAddress"),
        ("CAMBIUM-PTP500-MIB", "sMTPEnabledMessages"))
)
if mibBuilder.loadTexts:
    smtpGroup.setStatus("current")

snmpControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 16)
)
snmpControlGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "sNMPPortNumber"),
        ("CAMBIUM-PTP500-MIB", "sNMPCommunityString"),
        ("CAMBIUM-PTP500-MIB", "sNMPTrapTableNumber"),
        ("CAMBIUM-PTP500-MIB", "sNMPTrapVersion"),
        ("CAMBIUM-PTP500-MIB", "sNMPEnabledTraps"),
        ("CAMBIUM-PTP500-MIB", "enabledDiagnosticAlarms"),
        ("CAMBIUM-PTP500-MIB", "sNMPSendAllTrapsAtStartup"),
        ("CAMBIUM-PTP500-MIB", "sNMPTrapIPAddress"),
        ("CAMBIUM-PTP500-MIB", "sNMPTrapPortNumber"))
)
if mibBuilder.loadTexts:
    snmpControlGroup.setStatus("current")

sntpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 17)
)
sntpGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "sNTPState"),
        ("CAMBIUM-PTP500-MIB", "sNTPServerIPAddress"),
        ("CAMBIUM-PTP500-MIB", "sNTPServerPortNumber"),
        ("CAMBIUM-PTP500-MIB", "sNTPPollInterval"),
        ("CAMBIUM-PTP500-MIB", "sNTPSync"),
        ("CAMBIUM-PTP500-MIB", "sNTPLastSync"),
        ("CAMBIUM-PTP500-MIB", "systemClock"),
        ("CAMBIUM-PTP500-MIB", "timeZone"),
        ("CAMBIUM-PTP500-MIB", "daylightSaving"))
)
if mibBuilder.loadTexts:
    sntpGroup.setStatus("current")

resetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 18)
)
resetGroup.setObjects(
    ("CAMBIUM-PTP500-MIB", "systemReset")
)
if mibBuilder.loadTexts:
    resetGroup.setStatus("current")

versionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 19)
)
versionsGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "softwareVersion"),
        ("CAMBIUM-PTP500-MIB", "hardwareVersion"),
        ("CAMBIUM-PTP500-MIB", "secondarySoftwareVersion"),
        ("CAMBIUM-PTP500-MIB", "bootVersion"))
)
if mibBuilder.loadTexts:
    versionsGroup.setStatus("current")

pubStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 20)
)
pubStatsGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "receiveDataRate"),
        ("CAMBIUM-PTP500-MIB", "transmitDataRate"),
        ("CAMBIUM-PTP500-MIB", "aggregateDataRate"),
        ("CAMBIUM-PTP500-MIB", "wirelessLinkAvailability"),
        ("CAMBIUM-PTP500-MIB", "wirelessLinkStatus"),
        ("CAMBIUM-PTP500-MIB", "byteErrorRatio"),
        ("CAMBIUM-PTP500-MIB", "receiveModulationModeDetail"))
)
if mibBuilder.loadTexts:
    pubStatsGroup.setStatus("current")

encryptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 22)
)
encryptionGroup.setObjects(
    ("CAMBIUM-PTP500-MIB", "encryptionAlgorithm")
)
if mibBuilder.loadTexts:
    encryptionGroup.setStatus("current")

tDDControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 23)
)
tDDControlGroup.setObjects(
    ("CAMBIUM-PTP500-MIB", "tDDSynchronizationMode")
)
if mibBuilder.loadTexts:
    tDDControlGroup.setStatus("current")

syslogControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 24)
)
syslogControlGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "syslogClient"),
        ("CAMBIUM-PTP500-MIB", "syslogState"))
)
if mibBuilder.loadTexts:
    syslogControlGroup.setStatus("current")

aAAControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 25)
)
aAAControlGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "userTableNumber"),
        ("CAMBIUM-PTP500-MIB", "userName"),
        ("CAMBIUM-PTP500-MIB", "userRole"),
        ("CAMBIUM-PTP500-MIB", "userEnabled"),
        ("CAMBIUM-PTP500-MIB", "userPassword"))
)
if mibBuilder.loadTexts:
    aAAControlGroup.setStatus("current")

supplementaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 96)
)
supplementaryGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "longitude"),
        ("CAMBIUM-PTP500-MIB", "latitude"),
        ("CAMBIUM-PTP500-MIB", "altitude"))
)
if mibBuilder.loadTexts:
    supplementaryGroup.setStatus("current")


# Notification objects

channelChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 1)
)
channelChangeTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "receiveChannel")
)
if mibBuilder.loadTexts:
    channelChangeTrap.setStatus(
        "current"
    )

dfsImpulsiveInterferenceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 2)
)
dfsImpulsiveInterferenceTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "receiveChannel")
)
if mibBuilder.loadTexts:
    dfsImpulsiveInterferenceTrap.setStatus(
        "current"
    )

dataPortStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 3)
)
dataPortStatusTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "dataPortStatus")
)
if mibBuilder.loadTexts:
    dataPortStatusTrap.setStatus(
        "current"
    )

telecomsChannelStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 4)
)
telecomsChannelStatusTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "telecomsChannelStatus")
)
if mibBuilder.loadTexts:
    telecomsChannelStatusTrap.setStatus(
        "current"
    )

telecomsLoopbackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 6)
)
telecomsLoopbackTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "telecomsLoopback")
)
if mibBuilder.loadTexts:
    telecomsLoopbackTrap.setStatus(
        "current"
    )

regionCodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 8)
)
regionCodeTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "regionCode")
)
if mibBuilder.loadTexts:
    regionCodeTrap.setStatus(
        "current"
    )

installStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 9)
)
installStatusTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "installStatus")
)
if mibBuilder.loadTexts:
    installStatusTrap.setStatus(
        "current"
    )

installArmStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 10)
)
installArmStateTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "installArmState")
)
if mibBuilder.loadTexts:
    installArmStateTrap.setStatus(
        "current"
    )

unitOutOfCalibrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 11)
)
unitOutOfCalibrationTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "unitOutOfCalibration")
)
if mibBuilder.loadTexts:
    unitOutOfCalibrationTrap.setStatus(
        "current"
    )

incompatibleRegionCodesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 14)
)
incompatibleRegionCodesTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "incompatibleRegionCodes")
)
if mibBuilder.loadTexts:
    incompatibleRegionCodesTrap.setStatus(
        "current"
    )

noWirelessChannelAvailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 15)
)
noWirelessChannelAvailableTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "noWirelessChannelAvailable")
)
if mibBuilder.loadTexts:
    noWirelessChannelAvailableTrap.setStatus(
        "current"
    )

wirelessLinkDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 16)
)
wirelessLinkDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "wirelessLinkDisabledWarning")
)
if mibBuilder.loadTexts:
    wirelessLinkDisabledWarningTrap.setStatus(
        "current"
    )

dataPortDisabledWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 17)
)
dataPortDisabledWarningTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "dataPortDisabledWarning")
)
if mibBuilder.loadTexts:
    dataPortDisabledWarningTrap.setStatus(
        "current"
    )

dataPortConfigurationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 19)
)
dataPortConfigurationMismatchTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "dataPortConfigurationMismatch")
)
if mibBuilder.loadTexts:
    dataPortConfigurationMismatchTrap.setStatus(
        "current"
    )

incompatibleMasterAndSlaveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 20)
)
incompatibleMasterAndSlaveTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "incompatibleMasterAndSlave")
)
if mibBuilder.loadTexts:
    incompatibleMasterAndSlaveTrap.setStatus(
        "current"
    )

sNTPSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 21)
)
sNTPSyncTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "sNTPSync")
)
if mibBuilder.loadTexts:
    sNTPSyncTrap.setStatus(
        "current"
    )

tDDSynchronizationAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 22)
)
tDDSynchronizationAlarmTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "tDDSynchronizationAlarm")
)
if mibBuilder.loadTexts:
    tDDSynchronizationAlarmTrap.setStatus(
        "current"
    )

linkModeOptimizationMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 25)
)
linkModeOptimizationMismatchTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "linkModeOptimizationMismatch")
)
if mibBuilder.loadTexts:
    linkModeOptimizationMismatchTrap.setStatus(
        "current"
    )

capacityLicenseMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 27)
)
capacityLicenseMismatchTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "capacityLicenseMismatch")
)
if mibBuilder.loadTexts:
    capacityLicenseMismatchTrap.setStatus(
        "current"
    )

syslogStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 30)
)
syslogStateTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "syslogState")
)
if mibBuilder.loadTexts:
    syslogStateTrap.setStatus(
        "current"
    )

syslogLocalNearlyFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 31)
)
if mibBuilder.loadTexts:
    syslogLocalNearlyFullTrap.setStatus(
        "current"
    )

syslogLocalWrappedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 32)
)
if mibBuilder.loadTexts:
    syslogLocalWrappedTrap.setStatus(
        "current"
    )

syslogClientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17713, 5, 99, 0, 33)
)
syslogClientTrap.setObjects(
    ("CAMBIUM-PTP500-MIB", "syslogClient")
)
if mibBuilder.loadTexts:
    syslogClientTrap.setStatus(
        "current"
    )


# Notifications groups

notificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 17713, 5, 98, 99)
)
notificationsGroup.setObjects(
      *(("CAMBIUM-PTP500-MIB", "channelChangeTrap"),
        ("CAMBIUM-PTP500-MIB", "dfsImpulsiveInterferenceTrap"),
        ("CAMBIUM-PTP500-MIB", "dataPortStatusTrap"),
        ("CAMBIUM-PTP500-MIB", "telecomsChannelStatusTrap"),
        ("CAMBIUM-PTP500-MIB", "telecomsLoopbackTrap"),
        ("CAMBIUM-PTP500-MIB", "regionCodeTrap"),
        ("CAMBIUM-PTP500-MIB", "installStatusTrap"),
        ("CAMBIUM-PTP500-MIB", "installArmStateTrap"),
        ("CAMBIUM-PTP500-MIB", "unitOutOfCalibrationTrap"),
        ("CAMBIUM-PTP500-MIB", "incompatibleRegionCodesTrap"),
        ("CAMBIUM-PTP500-MIB", "noWirelessChannelAvailableTrap"),
        ("CAMBIUM-PTP500-MIB", "wirelessLinkDisabledWarningTrap"),
        ("CAMBIUM-PTP500-MIB", "dataPortDisabledWarningTrap"),
        ("CAMBIUM-PTP500-MIB", "dataPortConfigurationMismatchTrap"),
        ("CAMBIUM-PTP500-MIB", "incompatibleMasterAndSlaveTrap"),
        ("CAMBIUM-PTP500-MIB", "sNTPSyncTrap"),
        ("CAMBIUM-PTP500-MIB", "tDDSynchronizationAlarmTrap"),
        ("CAMBIUM-PTP500-MIB", "linkModeOptimizationMismatchTrap"),
        ("CAMBIUM-PTP500-MIB", "capacityLicenseMismatchTrap"),
        ("CAMBIUM-PTP500-MIB", "syslogStateTrap"),
        ("CAMBIUM-PTP500-MIB", "syslogLocalNearlyFullTrap"),
        ("CAMBIUM-PTP500-MIB", "syslogLocalWrappedTrap"),
        ("CAMBIUM-PTP500-MIB", "syslogClientTrap"))
)
if mibBuilder.loadTexts:
    notificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ptpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 17713, 5, 97)
)
ptpCompliance.setObjects(
      *(("CAMBIUM-PTP500-MIB", "dfsGroup"),
        ("CAMBIUM-PTP500-MIB", "configurationGroup"),
        ("CAMBIUM-PTP500-MIB", "ethernetGroup"),
        ("CAMBIUM-PTP500-MIB", "telecomGroup"),
        ("CAMBIUM-PTP500-MIB", "licenceGroup"),
        ("CAMBIUM-PTP500-MIB", "managementGroup"),
        ("CAMBIUM-PTP500-MIB", "phyControlGroup"),
        ("CAMBIUM-PTP500-MIB", "phyStatusGroup"),
        ("CAMBIUM-PTP500-MIB", "alarmsGroup"),
        ("CAMBIUM-PTP500-MIB", "smtpGroup"),
        ("CAMBIUM-PTP500-MIB", "snmpControlGroup"),
        ("CAMBIUM-PTP500-MIB", "sntpGroup"),
        ("CAMBIUM-PTP500-MIB", "resetGroup"),
        ("CAMBIUM-PTP500-MIB", "versionsGroup"),
        ("CAMBIUM-PTP500-MIB", "pubStatsGroup"),
        ("CAMBIUM-PTP500-MIB", "encryptionGroup"),
        ("CAMBIUM-PTP500-MIB", "tDDControlGroup"),
        ("CAMBIUM-PTP500-MIB", "aAAControlGroup"),
        ("CAMBIUM-PTP500-MIB", "syslogControlGroup"),
        ("CAMBIUM-PTP500-MIB", "supplementaryGroup"),
        ("CAMBIUM-PTP500-MIB", "notificationsGroup"))
)
if mibBuilder.loadTexts:
    ptpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-PTP500-MIB",
    **{"cambium": cambium,
       "ptp": ptp,
       "ptmp": ptmp,
       "ptp500": ptp500,
       "dfs": dfs,
       "dfsTableNumber": dfsTableNumber,
       "dfsTable": dfsTable,
       "dfsTableEntry": dfsTableEntry,
       "dfsTableIndex": dfsTableIndex,
       "dfsMeans": dfsMeans,
       "dfsNineNinePointNinePercentiles": dfsNineNinePointNinePercentiles,
       "dfsPeaks": dfsPeaks,
       "configuration": configuration,
       "iPAddress": iPAddress,
       "subnetMask": subnetMask,
       "gatewayIPAddress": gatewayIPAddress,
       "targetMACAddress": targetMACAddress,
       "masterSlaveMode": masterSlaveMode,
       "maximumTransmitPower": maximumTransmitPower,
       "antennaGain": antennaGain,
       "cableLoss": cableLoss,
       "eIRP": eIRP,
       "channelBandwidth": channelBandwidth,
       "remoteIPAddress": remoteIPAddress,
       "linkName": linkName,
       "siteName": siteName,
       "accessMethod": accessMethod,
       "groupID": groupID,
       "ethernet": ethernet,
       "dataPortAutoNegotiation": dataPortAutoNegotiation,
       "dataPortAutoNegAdvertisement": dataPortAutoNegAdvertisement,
       "dataPortAutoMdix": dataPortAutoMdix,
       "dataPortStatus": dataPortStatus,
       "dataPortSpeedAndDuplex": dataPortSpeedAndDuplex,
       "dataPortWirelessDownAlert": dataPortWirelessDownAlert,
       "useVLANForManagementInterfaces": useVLANForManagementInterfaces,
       "vLANManagementPriority": vLANManagementPriority,
       "vLANManagementVID": vLANManagementVID,
       "vLANPriorityTableNumber": vLANPriorityTableNumber,
       "vLANPriorityTable": vLANPriorityTable,
       "vLANPriorityTableEntry": vLANPriorityTableEntry,
       "vLANPriorityQueueMapping": vLANPriorityQueueMapping,
       "vLANPriorityTableIndex": vLANPriorityTableIndex,
       "telecom": telecom,
       "telecomsInterface": telecomsInterface,
       "telecomsChannelStatus": telecomsChannelStatus,
       "telecomsLineCode": telecomsLineCode,
       "telecomsCableLength": telecomsCableLength,
       "telecomsLoopback": telecomsLoopback,
       "licence": licence,
       "regionCode": regionCode,
       "productVariant": productVariant,
       "productName": productName,
       "ethernetFiberSupport": ethernetFiberSupport,
       "frequencyVariant": frequencyVariant,
       "bandwidthVariant": bandwidthVariant,
       "constantPowerSpectralDensity": constantPowerSpectralDensity,
       "sNMPv3Enable": sNMPv3Enable,
       "licensedCapacity": licensedCapacity,
       "management": management,
       "installStatus": installStatus,
       "installArmState": installArmState,
       "tFTPServerIPAddress": tFTPServerIPAddress,
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
       "phyControl": phyControl,
       "linkSymmetry": linkSymmetry,
       "linkModeOptimisation": linkModeOptimisation,
       "userConfiguredMaxModulationMode": userConfiguredMaxModulationMode,
       "remoteMaximumTransmitPower": remoteMaximumTransmitPower,
       "phyStatus": phyStatus,
       "receivePower": receivePower,
       "vectorError": vectorError,
       "transmitPower": transmitPower,
       "range": range,
       "linkLoss": linkLoss,
       "receiveChannel": receiveChannel,
       "transmitChannel": transmitChannel,
       "receiveModulationMode": receiveModulationMode,
       "transmitModulationMode": transmitModulationMode,
       "receiveFreqMHz": receiveFreqMHz,
       "transmitFreqMHz": transmitFreqMHz,
       "signalStrengthRatio": signalStrengthRatio,
       "receiveFreqKHz": receiveFreqKHz,
       "transmitFreqKHz": transmitFreqKHz,
       "searchState": searchState,
       "alarms": alarms,
       "unitOutOfCalibration": unitOutOfCalibration,
       "incompatibleRegionCodes": incompatibleRegionCodes,
       "noWirelessChannelAvailable": noWirelessChannelAvailable,
       "wirelessLinkDisabledWarning": wirelessLinkDisabledWarning,
       "dataPortDisabledWarning": dataPortDisabledWarning,
       "dataPortConfigurationMismatch": dataPortConfigurationMismatch,
       "incompatibleMasterAndSlave": incompatibleMasterAndSlave,
       "tDDSynchronizationStatus": tDDSynchronizationStatus,
       "tDDSynchronizationAlarm": tDDSynchronizationAlarm,
       "linkModeOptimizationMismatch": linkModeOptimizationMismatch,
       "capacityLicenseMismatch": capacityLicenseMismatch,
       "smtp": smtp,
       "sMTPEmailAlert": sMTPEmailAlert,
       "sMTPServerIPAddress": sMTPServerIPAddress,
       "sMTPServerPortNumber": sMTPServerPortNumber,
       "sMTPSourceEmailAddress": sMTPSourceEmailAddress,
       "sMTPDestinationEmailAddress": sMTPDestinationEmailAddress,
       "sMTPEnabledMessages": sMTPEnabledMessages,
       "snmpControl": snmpControl,
       "sNMPPortNumber": sNMPPortNumber,
       "sNMPCommunityString": sNMPCommunityString,
       "sNMPTrapTableNumber": sNMPTrapTableNumber,
       "sNMPTrapTable": sNMPTrapTable,
       "sNMPTrapTableEntry": sNMPTrapTableEntry,
       "sNMPTrapTableIndex": sNMPTrapTableIndex,
       "sNMPTrapIPAddress": sNMPTrapIPAddress,
       "sNMPTrapPortNumber": sNMPTrapPortNumber,
       "sNMPTrapVersion": sNMPTrapVersion,
       "sNMPEnabledTraps": sNMPEnabledTraps,
       "enabledDiagnosticAlarms": enabledDiagnosticAlarms,
       "sNMPSendAllTrapsAtStartup": sNMPSendAllTrapsAtStartup,
       "sntp": sntp,
       "sNTPState": sNTPState,
       "sNTPServerIPAddress": sNTPServerIPAddress,
       "sNTPServerPortNumber": sNTPServerPortNumber,
       "sNTPPollInterval": sNTPPollInterval,
       "sNTPSync": sNTPSync,
       "sNTPLastSync": sNTPLastSync,
       "systemClock": systemClock,
       "timeZone": timeZone,
       "daylightSaving": daylightSaving,
       "reset": reset,
       "systemReset": systemReset,
       "versions": versions,
       "softwareVersion": softwareVersion,
       "hardwareVersion": hardwareVersion,
       "secondarySoftwareVersion": secondarySoftwareVersion,
       "bootVersion": bootVersion,
       "pubStats": pubStats,
       "receiveDataRate": receiveDataRate,
       "transmitDataRate": transmitDataRate,
       "aggregateDataRate": aggregateDataRate,
       "wirelessLinkAvailability": wirelessLinkAvailability,
       "wirelessLinkStatus": wirelessLinkStatus,
       "byteErrorRatio": byteErrorRatio,
       "receiveModulationModeDetail": receiveModulationModeDetail,
       "encryption": encryption,
       "encryptionAlgorithm": encryptionAlgorithm,
       "tDDControl": tDDControl,
       "tDDSynchronizationMode": tDDSynchronizationMode,
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
       "supplementary": supplementary,
       "longitude": longitude,
       "latitude": latitude,
       "altitude": altitude,
       "ptpCompliance": ptpCompliance,
       "ptpGroups": ptpGroups,
       "dfsGroup": dfsGroup,
       "configurationGroup": configurationGroup,
       "ethernetGroup": ethernetGroup,
       "telecomGroup": telecomGroup,
       "licenceGroup": licenceGroup,
       "managementGroup": managementGroup,
       "phyControlGroup": phyControlGroup,
       "phyStatusGroup": phyStatusGroup,
       "alarmsGroup": alarmsGroup,
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
       "supplementaryGroup": supplementaryGroup,
       "notificationsGroup": notificationsGroup,
       "ptpTraps": ptpTraps,
       "ptpTrapPrefix": ptpTrapPrefix,
       "channelChangeTrap": channelChangeTrap,
       "dfsImpulsiveInterferenceTrap": dfsImpulsiveInterferenceTrap,
       "dataPortStatusTrap": dataPortStatusTrap,
       "telecomsChannelStatusTrap": telecomsChannelStatusTrap,
       "telecomsLoopbackTrap": telecomsLoopbackTrap,
       "regionCodeTrap": regionCodeTrap,
       "installStatusTrap": installStatusTrap,
       "installArmStateTrap": installArmStateTrap,
       "unitOutOfCalibrationTrap": unitOutOfCalibrationTrap,
       "incompatibleRegionCodesTrap": incompatibleRegionCodesTrap,
       "noWirelessChannelAvailableTrap": noWirelessChannelAvailableTrap,
       "wirelessLinkDisabledWarningTrap": wirelessLinkDisabledWarningTrap,
       "dataPortDisabledWarningTrap": dataPortDisabledWarningTrap,
       "dataPortConfigurationMismatchTrap": dataPortConfigurationMismatchTrap,
       "incompatibleMasterAndSlaveTrap": incompatibleMasterAndSlaveTrap,
       "sNTPSyncTrap": sNTPSyncTrap,
       "tDDSynchronizationAlarmTrap": tDDSynchronizationAlarmTrap,
       "linkModeOptimizationMismatchTrap": linkModeOptimizationMismatchTrap,
       "capacityLicenseMismatchTrap": capacityLicenseMismatchTrap,
       "syslogStateTrap": syslogStateTrap,
       "syslogLocalNearlyFullTrap": syslogLocalNearlyFullTrap,
       "syslogLocalWrappedTrap": syslogLocalWrappedTrap,
       "syslogClientTrap": syslogClientTrap}
)
