# SNMP MIB module (TACHYON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tachyon\TACHYON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:30 2025
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

(ifMIB,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifMIB")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

tachyon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 57344)
)
if mibBuilder.loadTexts:
    tachyon.setRevisions(
        ("2024-10-20 08:37",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tna30xMIB_ObjectIdentity = ObjectIdentity
tna30xMIB = _Tna30xMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57344, 1)
)
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57344, 1, 1)
)
_PhysicalPortCount_Type = Integer32
_PhysicalPortCount_Object = MibScalar
physicalPortCount = _PhysicalPortCount_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 1, 1),
    _PhysicalPortCount_Type()
)
physicalPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCount.setStatus("current")
_InternalSwitchMac_Type = DisplayString
_InternalSwitchMac_Object = MibScalar
internalSwitchMac = _InternalSwitchMac_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 1, 2),
    _InternalSwitchMac_Type()
)
internalSwitchMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalSwitchMac.setStatus("current")
_EthernetTable_Object = MibTable
ethernetTable = _EthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ethernetTable.setStatus("current")
_EthernetEntry_Object = MibTableRow
ethernetEntry = _EthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 1, 3, 1)
)
ethernetEntry.setIndexNames(
    (0, "TACHYON-MIB", "ethernetIfaceName"),
)
if mibBuilder.loadTexts:
    ethernetEntry.setStatus("current")
_EthernetName_Type = DisplayString
_EthernetName_Object = MibTableColumn
ethernetName = _EthernetName_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 1, 3, 1, 1),
    _EthernetName_Type()
)
ethernetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetName.setStatus("current")
_EthernetIfaceName_Type = DisplayString
_EthernetIfaceName_Object = MibTableColumn
ethernetIfaceName = _EthernetIfaceName_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 1, 3, 1, 2),
    _EthernetIfaceName_Type()
)
ethernetIfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetIfaceName.setStatus("current")
_EthernetParentIface_Type = DisplayString
_EthernetParentIface_Object = MibTableColumn
ethernetParentIface = _EthernetParentIface_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 1, 3, 1, 3),
    _EthernetParentIface_Type()
)
ethernetParentIface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetParentIface.setStatus("current")
_EthernetSwitchPortId_Type = Integer32
_EthernetSwitchPortId_Object = MibTableColumn
ethernetSwitchPortId = _EthernetSwitchPortId_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 1, 3, 1, 4),
    _EthernetSwitchPortId_Type()
)
ethernetSwitchPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetSwitchPortId.setStatus("current")
_EthernetLink_Type = Integer32
_EthernetLink_Object = MibTableColumn
ethernetLink = _EthernetLink_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 1, 3, 1, 5),
    _EthernetLink_Type()
)
ethernetLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetLink.setStatus("current")
_EthernetAutoNeg_Type = Integer32
_EthernetAutoNeg_Object = MibTableColumn
ethernetAutoNeg = _EthernetAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 1, 3, 1, 6),
    _EthernetAutoNeg_Type()
)
ethernetAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetAutoNeg.setStatus("current")
_EthernetSpeed_Type = Gauge32
_EthernetSpeed_Object = MibTableColumn
ethernetSpeed = _EthernetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 1, 3, 1, 7),
    _EthernetSpeed_Type()
)
ethernetSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetSpeed.setStatus("current")
_EthernetDuplex_Type = DisplayString
_EthernetDuplex_Object = MibTableColumn
ethernetDuplex = _EthernetDuplex_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 1, 3, 1, 8),
    _EthernetDuplex_Type()
)
ethernetDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetDuplex.setStatus("current")
_EthernetPoe_Type = DisplayString
_EthernetPoe_Object = MibTableColumn
ethernetPoe = _EthernetPoe_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 1, 3, 1, 9),
    _EthernetPoe_Type()
)
ethernetPoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetPoe.setStatus("current")
_EthernetEnabled_Type = Integer32
_EthernetEnabled_Object = MibTableColumn
ethernetEnabled = _EthernetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 1, 3, 1, 10),
    _EthernetEnabled_Type()
)
ethernetEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetEnabled.setStatus("current")
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2)
)
_WirelessRadioCount_Type = Integer32
_WirelessRadioCount_Object = MibScalar
wirelessRadioCount = _WirelessRadioCount_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 1),
    _WirelessRadioCount_Type()
)
wirelessRadioCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadioCount.setStatus("current")
_WirelessRadioTable_Object = MibTable
wirelessRadioTable = _WirelessRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wirelessRadioTable.setStatus("current")
_WirelessRadioEntry_Object = MibTableRow
wirelessRadioEntry = _WirelessRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 2, 1)
)
wirelessRadioEntry.setIndexNames(
    (0, "TACHYON-MIB", "wirelessRadioName"),
)
if mibBuilder.loadTexts:
    wirelessRadioEntry.setStatus("current")
_WirelessRadioMac_Type = DisplayString
_WirelessRadioMac_Object = MibTableColumn
wirelessRadioMac = _WirelessRadioMac_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 2, 1, 1),
    _WirelessRadioMac_Type()
)
wirelessRadioMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadioMac.setStatus("current")
_WirelessRadioName_Type = DisplayString
_WirelessRadioName_Object = MibTableColumn
wirelessRadioName = _WirelessRadioName_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 2, 1, 2),
    _WirelessRadioName_Type()
)
wirelessRadioName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadioName.setStatus("current")
_WirelessRadioTxPower_Type = Gauge32
_WirelessRadioTxPower_Object = MibTableColumn
wirelessRadioTxPower = _WirelessRadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 2, 1, 3),
    _WirelessRadioTxPower_Type()
)
wirelessRadioTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadioTxPower.setStatus("current")
_WirelessRadioChannel_Type = Integer32
_WirelessRadioChannel_Object = MibTableColumn
wirelessRadioChannel = _WirelessRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 2, 1, 4),
    _WirelessRadioChannel_Type()
)
wirelessRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadioChannel.setStatus("current")
_WirelessRadioFrequency_Type = Integer32
_WirelessRadioFrequency_Object = MibTableColumn
wirelessRadioFrequency = _WirelessRadioFrequency_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 2, 1, 5),
    _WirelessRadioFrequency_Type()
)
wirelessRadioFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadioFrequency.setStatus("current")
_WirelessRadioChannelWidth_Type = Integer32
_WirelessRadioChannelWidth_Object = MibTableColumn
wirelessRadioChannelWidth = _WirelessRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 2, 1, 6),
    _WirelessRadioChannelWidth_Type()
)
wirelessRadioChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadioChannelWidth.setStatus("current")
_WirelessRadioFailoverState_Type = DisplayString
_WirelessRadioFailoverState_Object = MibTableColumn
wirelessRadioFailoverState = _WirelessRadioFailoverState_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 2, 1, 7),
    _WirelessRadioFailoverState_Type()
)
wirelessRadioFailoverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadioFailoverState.setStatus("current")
_WirelessRadioAntennaKit_Type = DisplayString
_WirelessRadioAntennaKit_Object = MibTableColumn
wirelessRadioAntennaKit = _WirelessRadioAntennaKit_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 2, 1, 8),
    _WirelessRadioAntennaKit_Type()
)
wirelessRadioAntennaKit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadioAntennaKit.setStatus("current")
_WirelessRadioChannelLabel_Type = DisplayString
_WirelessRadioChannelLabel_Object = MibTableColumn
wirelessRadioChannelLabel = _WirelessRadioChannelLabel_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 2, 1, 9),
    _WirelessRadioChannelLabel_Type()
)
wirelessRadioChannelLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadioChannelLabel.setStatus("current")
_WirelessRadioModemTemperature_Type = Integer32
_WirelessRadioModemTemperature_Object = MibTableColumn
wirelessRadioModemTemperature = _WirelessRadioModemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 2, 1, 10),
    _WirelessRadioModemTemperature_Type()
)
wirelessRadioModemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadioModemTemperature.setStatus("current")
_WirelessRadioTemperature_Type = Integer32
_WirelessRadioTemperature_Object = MibTableColumn
wirelessRadioTemperature = _WirelessRadioTemperature_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 2, 1, 11),
    _WirelessRadioTemperature_Type()
)
wirelessRadioTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRadioTemperature.setStatus("current")
_WirelessVapsCount_Type = Integer32
_WirelessVapsCount_Object = MibScalar
wirelessVapsCount = _WirelessVapsCount_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 3),
    _WirelessVapsCount_Type()
)
wirelessVapsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessVapsCount.setStatus("current")
_WirelessVapsTable_Object = MibTable
wirelessVapsTable = _WirelessVapsTable_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 4)
)
if mibBuilder.loadTexts:
    wirelessVapsTable.setStatus("current")
_WirelessVapEntry_Object = MibTableRow
wirelessVapEntry = _WirelessVapEntry_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 4, 1)
)
wirelessVapEntry.setIndexNames(
    (0, "TACHYON-MIB", "wirelessVapIfIndex"),
)
if mibBuilder.loadTexts:
    wirelessVapEntry.setStatus("current")


class _WirelessVapIfIndex_Type(Integer32):
    """Custom type wirelessVapIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WirelessVapIfIndex_Type.__name__ = "Integer32"
_WirelessVapIfIndex_Object = MibTableColumn
wirelessVapIfIndex = _WirelessVapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 4, 1, 1),
    _WirelessVapIfIndex_Type()
)
wirelessVapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessVapIfIndex.setStatus("current")
_WirelessVapName_Type = DisplayString
_WirelessVapName_Object = MibTableColumn
wirelessVapName = _WirelessVapName_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 4, 1, 2),
    _WirelessVapName_Type()
)
wirelessVapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessVapName.setStatus("current")
_WirelessVapMac_Type = DisplayString
_WirelessVapMac_Object = MibTableColumn
wirelessVapMac = _WirelessVapMac_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 4, 1, 3),
    _WirelessVapMac_Type()
)
wirelessVapMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessVapMac.setStatus("current")
_WirelessVapRadio_Type = DisplayString
_WirelessVapRadio_Object = MibTableColumn
wirelessVapRadio = _WirelessVapRadio_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 4, 1, 4),
    _WirelessVapRadio_Type()
)
wirelessVapRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessVapRadio.setStatus("current")
_WirelessVapOperationMode_Type = DisplayString
_WirelessVapOperationMode_Object = MibTableColumn
wirelessVapOperationMode = _WirelessVapOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 4, 1, 5),
    _WirelessVapOperationMode_Type()
)
wirelessVapOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessVapOperationMode.setStatus("current")
_WirelessVapSsid_Type = DisplayString
_WirelessVapSsid_Object = MibTableColumn
wirelessVapSsid = _WirelessVapSsid_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 4, 1, 6),
    _WirelessVapSsid_Type()
)
wirelessVapSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessVapSsid.setStatus("current")
_WirelessVapPeerCount_Type = Counter32
_WirelessVapPeerCount_Object = MibTableColumn
wirelessVapPeerCount = _WirelessVapPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 4, 1, 7),
    _WirelessVapPeerCount_Type()
)
wirelessVapPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessVapPeerCount.setStatus("current")
_WirelessVapSecurity_Type = DisplayString
_WirelessVapSecurity_Object = MibTableColumn
wirelessVapSecurity = _WirelessVapSecurity_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 4, 1, 8),
    _WirelessVapSecurity_Type()
)
wirelessVapSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessVapSecurity.setStatus("current")
_WirelessVapPtpEnabled_Type = Integer32
_WirelessVapPtpEnabled_Object = MibTableColumn
wirelessVapPtpEnabled = _WirelessVapPtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 4, 1, 9),
    _WirelessVapPtpEnabled_Type()
)
wirelessVapPtpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessVapPtpEnabled.setStatus("current")
_WirelessPeersCount_Type = Integer32
_WirelessPeersCount_Object = MibScalar
wirelessPeersCount = _WirelessPeersCount_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 5),
    _WirelessPeersCount_Type()
)
wirelessPeersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeersCount.setStatus("current")
_WirelessPeersTable_Object = MibTable
wirelessPeersTable = _WirelessPeersTable_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6)
)
if mibBuilder.loadTexts:
    wirelessPeersTable.setStatus("current")
_WirelessPeerEntry_Object = MibTableRow
wirelessPeerEntry = _WirelessPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1)
)
wirelessPeerEntry.setIndexNames(
    (0, "TACHYON-MIB", "wirelessPeerMac"),
)
if mibBuilder.loadTexts:
    wirelessPeerEntry.setStatus("current")
_WirelessPeerMac_Type = DisplayString
_WirelessPeerMac_Object = MibTableColumn
wirelessPeerMac = _WirelessPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 1),
    _WirelessPeerMac_Type()
)
wirelessPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerMac.setStatus("current")
_WirelessPeerVap_Type = DisplayString
_WirelessPeerVap_Object = MibTableColumn
wirelessPeerVap = _WirelessPeerVap_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 2),
    _WirelessPeerVap_Type()
)
wirelessPeerVap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerVap.setStatus("current")
_WirelessPeerVapIfIndex_Type = Integer32
_WirelessPeerVapIfIndex_Object = MibTableColumn
wirelessPeerVapIfIndex = _WirelessPeerVapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 3),
    _WirelessPeerVapIfIndex_Type()
)
wirelessPeerVapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerVapIfIndex.setStatus("current")
_WirelessPeerRxPackets_Type = Counter64
_WirelessPeerRxPackets_Object = MibTableColumn
wirelessPeerRxPackets = _WirelessPeerRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 4),
    _WirelessPeerRxPackets_Type()
)
wirelessPeerRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerRxPackets.setStatus("current")
_WirelessPeerTxPackets_Type = Counter64
_WirelessPeerTxPackets_Object = MibTableColumn
wirelessPeerTxPackets = _WirelessPeerTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 5),
    _WirelessPeerTxPackets_Type()
)
wirelessPeerTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerTxPackets.setStatus("current")
_WirelessPeerRxPower_Type = Integer32
_WirelessPeerRxPower_Object = MibTableColumn
wirelessPeerRxPower = _WirelessPeerRxPower_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 6),
    _WirelessPeerRxPower_Type()
)
wirelessPeerRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerRxPower.setStatus("current")
_WirelessPeerTxRate_Type = Gauge32
_WirelessPeerTxRate_Object = MibTableColumn
wirelessPeerTxRate = _WirelessPeerTxRate_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 7),
    _WirelessPeerTxRate_Type()
)
wirelessPeerTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerTxRate.setStatus("current")
_WirelessPeerSnr_Type = Integer32
_WirelessPeerSnr_Object = MibTableColumn
wirelessPeerSnr = _WirelessPeerSnr_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 8),
    _WirelessPeerSnr_Type()
)
wirelessPeerSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerSnr.setStatus("current")
_WirelessPeerRxRate_Type = Gauge32
_WirelessPeerRxRate_Object = MibTableColumn
wirelessPeerRxRate = _WirelessPeerRxRate_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 9),
    _WirelessPeerRxRate_Type()
)
wirelessPeerRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerRxRate.setStatus("current")
_WirelessPeerTxMcs_Type = Integer32
_WirelessPeerTxMcs_Object = MibTableColumn
wirelessPeerTxMcs = _WirelessPeerTxMcs_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 10),
    _WirelessPeerTxMcs_Type()
)
wirelessPeerTxMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerTxMcs.setStatus("current")
_WirelessPeerRxMcs_Type = Integer32
_WirelessPeerRxMcs_Object = MibTableColumn
wirelessPeerRxMcs = _WirelessPeerRxMcs_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 11),
    _WirelessPeerRxMcs_Type()
)
wirelessPeerRxMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerRxMcs.setStatus("current")
_WirelessPeerLinkUptime_Type = Integer32
_WirelessPeerLinkUptime_Object = MibTableColumn
wirelessPeerLinkUptime = _WirelessPeerLinkUptime_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 12),
    _WirelessPeerLinkUptime_Type()
)
wirelessPeerLinkUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerLinkUptime.setStatus("current")
_WirelessPeerLinkDistance_Type = Integer32
_WirelessPeerLinkDistance_Object = MibTableColumn
wirelessPeerLinkDistance = _WirelessPeerLinkDistance_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 13),
    _WirelessPeerLinkDistance_Type()
)
wirelessPeerLinkDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerLinkDistance.setStatus("current")
_WirelessPeerRxBytes_Type = Counter64
_WirelessPeerRxBytes_Object = MibTableColumn
wirelessPeerRxBytes = _WirelessPeerRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 14),
    _WirelessPeerRxBytes_Type()
)
wirelessPeerRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerRxBytes.setStatus("current")
_WirelessPeerTxBytes_Type = Counter64
_WirelessPeerTxBytes_Object = MibTableColumn
wirelessPeerTxBytes = _WirelessPeerTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 15),
    _WirelessPeerTxBytes_Type()
)
wirelessPeerTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerTxBytes.setStatus("current")
_WirelessPeerTxSector_Type = Integer32
_WirelessPeerTxSector_Object = MibTableColumn
wirelessPeerTxSector = _WirelessPeerTxSector_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 16),
    _WirelessPeerTxSector_Type()
)
wirelessPeerTxSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerTxSector.setStatus("current")
_WirelessPeerRxSector_Type = Integer32
_WirelessPeerRxSector_Object = MibTableColumn
wirelessPeerRxSector = _WirelessPeerRxSector_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 17),
    _WirelessPeerRxSector_Type()
)
wirelessPeerRxSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerRxSector.setStatus("current")
_WirelessPeerModel_Type = DisplayString
_WirelessPeerModel_Object = MibTableColumn
wirelessPeerModel = _WirelessPeerModel_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 18),
    _WirelessPeerModel_Type()
)
wirelessPeerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerModel.setStatus("current")
_WirelessPeerAntennaKit_Type = DisplayString
_WirelessPeerAntennaKit_Object = MibTableColumn
wirelessPeerAntennaKit = _WirelessPeerAntennaKit_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 19),
    _WirelessPeerAntennaKit_Type()
)
wirelessPeerAntennaKit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerAntennaKit.setStatus("current")
_WirelessPeerName_Type = DisplayString
_WirelessPeerName_Object = MibTableColumn
wirelessPeerName = _WirelessPeerName_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 6, 1, 20),
    _WirelessPeerName_Type()
)
wirelessPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerName.setStatus("current")
_WirelessPeersByMacTable_Object = MibTable
wirelessPeersByMacTable = _WirelessPeersByMacTable_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7)
)
if mibBuilder.loadTexts:
    wirelessPeersByMacTable.setStatus("current")
_WirelessPeerByMacEntry_Object = MibTableRow
wirelessPeerByMacEntry = _WirelessPeerByMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1)
)
wirelessPeerByMacEntry.setIndexNames(
    (0, "TACHYON-MIB", "wirelessPeerXMac"),
)
if mibBuilder.loadTexts:
    wirelessPeerByMacEntry.setStatus("current")
_WirelessPeerXMac_Type = DisplayString
_WirelessPeerXMac_Object = MibTableColumn
wirelessPeerXMac = _WirelessPeerXMac_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 1),
    _WirelessPeerXMac_Type()
)
wirelessPeerXMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXMac.setStatus("current")
_WirelessPeerXVap_Type = DisplayString
_WirelessPeerXVap_Object = MibTableColumn
wirelessPeerXVap = _WirelessPeerXVap_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 2),
    _WirelessPeerXVap_Type()
)
wirelessPeerXVap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXVap.setStatus("current")
_WirelessPeerXVapIfIndex_Type = Integer32
_WirelessPeerXVapIfIndex_Object = MibTableColumn
wirelessPeerXVapIfIndex = _WirelessPeerXVapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 3),
    _WirelessPeerXVapIfIndex_Type()
)
wirelessPeerXVapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXVapIfIndex.setStatus("current")
_WirelessPeerXRxPackets_Type = Counter64
_WirelessPeerXRxPackets_Object = MibTableColumn
wirelessPeerXRxPackets = _WirelessPeerXRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 4),
    _WirelessPeerXRxPackets_Type()
)
wirelessPeerXRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXRxPackets.setStatus("current")
_WirelessPeerXTxPackets_Type = Counter64
_WirelessPeerXTxPackets_Object = MibTableColumn
wirelessPeerXTxPackets = _WirelessPeerXTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 5),
    _WirelessPeerXTxPackets_Type()
)
wirelessPeerXTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXTxPackets.setStatus("current")
_WirelessPeerXRxPower_Type = Integer32
_WirelessPeerXRxPower_Object = MibTableColumn
wirelessPeerXRxPower = _WirelessPeerXRxPower_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 6),
    _WirelessPeerXRxPower_Type()
)
wirelessPeerXRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXRxPower.setStatus("current")
_WirelessPeerXTxRate_Type = Gauge32
_WirelessPeerXTxRate_Object = MibTableColumn
wirelessPeerXTxRate = _WirelessPeerXTxRate_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 7),
    _WirelessPeerXTxRate_Type()
)
wirelessPeerXTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXTxRate.setStatus("current")
_WirelessPeerXSnr_Type = Integer32
_WirelessPeerXSnr_Object = MibTableColumn
wirelessPeerXSnr = _WirelessPeerXSnr_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 8),
    _WirelessPeerXSnr_Type()
)
wirelessPeerXSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXSnr.setStatus("current")
_WirelessPeerXRxRate_Type = Gauge32
_WirelessPeerXRxRate_Object = MibTableColumn
wirelessPeerXRxRate = _WirelessPeerXRxRate_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 9),
    _WirelessPeerXRxRate_Type()
)
wirelessPeerXRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXRxRate.setStatus("current")
_WirelessPeerXTxMcs_Type = Integer32
_WirelessPeerXTxMcs_Object = MibTableColumn
wirelessPeerXTxMcs = _WirelessPeerXTxMcs_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 10),
    _WirelessPeerXTxMcs_Type()
)
wirelessPeerXTxMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXTxMcs.setStatus("current")
_WirelessPeerXRxMcs_Type = Integer32
_WirelessPeerXRxMcs_Object = MibTableColumn
wirelessPeerXRxMcs = _WirelessPeerXRxMcs_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 11),
    _WirelessPeerXRxMcs_Type()
)
wirelessPeerXRxMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXRxMcs.setStatus("current")
_WirelessPeerXLinkUptime_Type = Integer32
_WirelessPeerXLinkUptime_Object = MibTableColumn
wirelessPeerXLinkUptime = _WirelessPeerXLinkUptime_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 12),
    _WirelessPeerXLinkUptime_Type()
)
wirelessPeerXLinkUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXLinkUptime.setStatus("current")
_WirelessPeerXLinkDistance_Type = Integer32
_WirelessPeerXLinkDistance_Object = MibTableColumn
wirelessPeerXLinkDistance = _WirelessPeerXLinkDistance_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 13),
    _WirelessPeerXLinkDistance_Type()
)
wirelessPeerXLinkDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXLinkDistance.setStatus("current")
_WirelessPeerXRxBytes_Type = Counter64
_WirelessPeerXRxBytes_Object = MibTableColumn
wirelessPeerXRxBytes = _WirelessPeerXRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 14),
    _WirelessPeerXRxBytes_Type()
)
wirelessPeerXRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXRxBytes.setStatus("current")
_WirelessPeerXTxBytes_Type = Counter64
_WirelessPeerXTxBytes_Object = MibTableColumn
wirelessPeerXTxBytes = _WirelessPeerXTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 15),
    _WirelessPeerXTxBytes_Type()
)
wirelessPeerXTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXTxBytes.setStatus("current")
_WirelessPeerXTxSector_Type = Integer32
_WirelessPeerXTxSector_Object = MibTableColumn
wirelessPeerXTxSector = _WirelessPeerXTxSector_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 16),
    _WirelessPeerXTxSector_Type()
)
wirelessPeerXTxSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXTxSector.setStatus("current")
_WirelessPeerXRxSector_Type = Integer32
_WirelessPeerXRxSector_Object = MibTableColumn
wirelessPeerXRxSector = _WirelessPeerXRxSector_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 17),
    _WirelessPeerXRxSector_Type()
)
wirelessPeerXRxSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXRxSector.setStatus("current")
_WirelessPeerXModel_Type = DisplayString
_WirelessPeerXModel_Object = MibTableColumn
wirelessPeerXModel = _WirelessPeerXModel_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 18),
    _WirelessPeerXModel_Type()
)
wirelessPeerXModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXModel.setStatus("current")
_WirelessPeerXAntennaKit_Type = DisplayString
_WirelessPeerXAntennaKit_Object = MibTableColumn
wirelessPeerXAntennaKit = _WirelessPeerXAntennaKit_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 19),
    _WirelessPeerXAntennaKit_Type()
)
wirelessPeerXAntennaKit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXAntennaKit.setStatus("current")
_WirelessPeerXName_Type = DisplayString
_WirelessPeerXName_Object = MibTableColumn
wirelessPeerXName = _WirelessPeerXName_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 2, 7, 1, 20),
    _WirelessPeerXName_Type()
)
wirelessPeerXName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPeerXName.setStatus("current")
_System_ext_ObjectIdentity = ObjectIdentity
system_ext = _System_ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 57344, 1, 3)
)
_DeviceModel_Type = DisplayString
_DeviceModel_Object = MibScalar
deviceModel = _DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 3, 1),
    _DeviceModel_Type()
)
deviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModel.setStatus("current")
_DeviceSerialNo_Type = DisplayString
_DeviceSerialNo_Object = MibScalar
deviceSerialNo = _DeviceSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 3, 2),
    _DeviceSerialNo_Type()
)
deviceSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSerialNo.setStatus("current")
_CpuTemperature_Type = Integer32
_CpuTemperature_Object = MibScalar
cpuTemperature = _CpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 3, 3),
    _CpuTemperature_Type()
)
cpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTemperature.setStatus("current")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 3, 4),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_FirmwareAlterateVersion_Type = DisplayString
_FirmwareAlterateVersion_Object = MibScalar
firmwareAlterateVersion = _FirmwareAlterateVersion_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 3, 5),
    _FirmwareAlterateVersion_Type()
)
firmwareAlterateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareAlterateVersion.setStatus("current")
_CpuUsagePercent_Type = Gauge32
_CpuUsagePercent_Object = MibScalar
cpuUsagePercent = _CpuUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 3, 6),
    _CpuUsagePercent_Type()
)
cpuUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUsagePercent.setStatus("current")
_MemoryUsagePercent_Type = Gauge32
_MemoryUsagePercent_Object = MibScalar
memoryUsagePercent = _MemoryUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 3, 7),
    _MemoryUsagePercent_Type()
)
memoryUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryUsagePercent.setStatus("current")
_DeviceUptime_Type = Counter32
_DeviceUptime_Object = MibScalar
deviceUptime = _DeviceUptime_Object(
    (1, 3, 6, 1, 4, 1, 57344, 1, 3, 8),
    _DeviceUptime_Type()
)
deviceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUptime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TACHYON-MIB",
    **{"tachyon": tachyon,
       "tna30xMIB": tna30xMIB,
       "ethernet": ethernet,
       "physicalPortCount": physicalPortCount,
       "internalSwitchMac": internalSwitchMac,
       "ethernetTable": ethernetTable,
       "ethernetEntry": ethernetEntry,
       "ethernetName": ethernetName,
       "ethernetIfaceName": ethernetIfaceName,
       "ethernetParentIface": ethernetParentIface,
       "ethernetSwitchPortId": ethernetSwitchPortId,
       "ethernetLink": ethernetLink,
       "ethernetAutoNeg": ethernetAutoNeg,
       "ethernetSpeed": ethernetSpeed,
       "ethernetDuplex": ethernetDuplex,
       "ethernetPoe": ethernetPoe,
       "ethernetEnabled": ethernetEnabled,
       "wireless": wireless,
       "wirelessRadioCount": wirelessRadioCount,
       "wirelessRadioTable": wirelessRadioTable,
       "wirelessRadioEntry": wirelessRadioEntry,
       "wirelessRadioMac": wirelessRadioMac,
       "wirelessRadioName": wirelessRadioName,
       "wirelessRadioTxPower": wirelessRadioTxPower,
       "wirelessRadioChannel": wirelessRadioChannel,
       "wirelessRadioFrequency": wirelessRadioFrequency,
       "wirelessRadioChannelWidth": wirelessRadioChannelWidth,
       "wirelessRadioFailoverState": wirelessRadioFailoverState,
       "wirelessRadioAntennaKit": wirelessRadioAntennaKit,
       "wirelessRadioChannelLabel": wirelessRadioChannelLabel,
       "wirelessRadioModemTemperature": wirelessRadioModemTemperature,
       "wirelessRadioTemperature": wirelessRadioTemperature,
       "wirelessVapsCount": wirelessVapsCount,
       "wirelessVapsTable": wirelessVapsTable,
       "wirelessVapEntry": wirelessVapEntry,
       "wirelessVapIfIndex": wirelessVapIfIndex,
       "wirelessVapName": wirelessVapName,
       "wirelessVapMac": wirelessVapMac,
       "wirelessVapRadio": wirelessVapRadio,
       "wirelessVapOperationMode": wirelessVapOperationMode,
       "wirelessVapSsid": wirelessVapSsid,
       "wirelessVapPeerCount": wirelessVapPeerCount,
       "wirelessVapSecurity": wirelessVapSecurity,
       "wirelessVapPtpEnabled": wirelessVapPtpEnabled,
       "wirelessPeersCount": wirelessPeersCount,
       "wirelessPeersTable": wirelessPeersTable,
       "wirelessPeerEntry": wirelessPeerEntry,
       "wirelessPeerMac": wirelessPeerMac,
       "wirelessPeerVap": wirelessPeerVap,
       "wirelessPeerVapIfIndex": wirelessPeerVapIfIndex,
       "wirelessPeerRxPackets": wirelessPeerRxPackets,
       "wirelessPeerTxPackets": wirelessPeerTxPackets,
       "wirelessPeerRxPower": wirelessPeerRxPower,
       "wirelessPeerTxRate": wirelessPeerTxRate,
       "wirelessPeerSnr": wirelessPeerSnr,
       "wirelessPeerRxRate": wirelessPeerRxRate,
       "wirelessPeerTxMcs": wirelessPeerTxMcs,
       "wirelessPeerRxMcs": wirelessPeerRxMcs,
       "wirelessPeerLinkUptime": wirelessPeerLinkUptime,
       "wirelessPeerLinkDistance": wirelessPeerLinkDistance,
       "wirelessPeerRxBytes": wirelessPeerRxBytes,
       "wirelessPeerTxBytes": wirelessPeerTxBytes,
       "wirelessPeerTxSector": wirelessPeerTxSector,
       "wirelessPeerRxSector": wirelessPeerRxSector,
       "wirelessPeerModel": wirelessPeerModel,
       "wirelessPeerAntennaKit": wirelessPeerAntennaKit,
       "wirelessPeerName": wirelessPeerName,
       "wirelessPeersByMacTable": wirelessPeersByMacTable,
       "wirelessPeerByMacEntry": wirelessPeerByMacEntry,
       "wirelessPeerXMac": wirelessPeerXMac,
       "wirelessPeerXVap": wirelessPeerXVap,
       "wirelessPeerXVapIfIndex": wirelessPeerXVapIfIndex,
       "wirelessPeerXRxPackets": wirelessPeerXRxPackets,
       "wirelessPeerXTxPackets": wirelessPeerXTxPackets,
       "wirelessPeerXRxPower": wirelessPeerXRxPower,
       "wirelessPeerXTxRate": wirelessPeerXTxRate,
       "wirelessPeerXSnr": wirelessPeerXSnr,
       "wirelessPeerXRxRate": wirelessPeerXRxRate,
       "wirelessPeerXTxMcs": wirelessPeerXTxMcs,
       "wirelessPeerXRxMcs": wirelessPeerXRxMcs,
       "wirelessPeerXLinkUptime": wirelessPeerXLinkUptime,
       "wirelessPeerXLinkDistance": wirelessPeerXLinkDistance,
       "wirelessPeerXRxBytes": wirelessPeerXRxBytes,
       "wirelessPeerXTxBytes": wirelessPeerXTxBytes,
       "wirelessPeerXTxSector": wirelessPeerXTxSector,
       "wirelessPeerXRxSector": wirelessPeerXRxSector,
       "wirelessPeerXModel": wirelessPeerXModel,
       "wirelessPeerXAntennaKit": wirelessPeerXAntennaKit,
       "wirelessPeerXName": wirelessPeerXName,
       "system-ext": system_ext,
       "deviceModel": deviceModel,
       "deviceSerialNo": deviceSerialNo,
       "cpuTemperature": cpuTemperature,
       "firmwareVersion": firmwareVersion,
       "firmwareAlterateVersion": firmwareAlterateVersion,
       "cpuUsagePercent": cpuUsagePercent,
       "memoryUsagePercent": memoryUsagePercent,
       "deviceUptime": deviceUptime}
)
