# SNMP MIB module (FORTINET-FORTIAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\FORTINET-FORTIAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:47 2025
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

(fortinet,) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "fortinet")

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

fnFortiAPMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120)
)
if mibBuilder.loadTexts:
    fnFortiAPMib.setRevisions(
        ("2018-10-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FapTraps_ObjectIdentity = ObjectIdentity
fapTraps = _FapTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 0)
)
_FapCommon_ObjectIdentity = ObjectIdentity
fapCommon = _FapCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 1)
)
_FapVersion_Type = DisplayString
_FapVersion_Object = MibScalar
fapVersion = _FapVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 1, 1),
    _FapVersion_Type()
)
fapVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVersion.setStatus("current")
_FapSerialNum_Type = DisplayString
_FapSerialNum_Object = MibScalar
fapSerialNum = _FapSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 1, 2),
    _FapSerialNum_Type()
)
fapSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapSerialNum.setStatus("current")
_FapHostName_Type = DisplayString
_FapHostName_Object = MibScalar
fapHostName = _FapHostName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 1, 3),
    _FapHostName_Type()
)
fapHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapHostName.setStatus("current")
_FapRegionCode_Type = DisplayString
_FapRegionCode_Object = MibScalar
fapRegionCode = _FapRegionCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 1, 4),
    _FapRegionCode_Type()
)
fapRegionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRegionCode.setStatus("current")


class _FapBaseMacAddr_Type(PhysAddress):
    """Custom type fapBaseMacAddr based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_FapBaseMacAddr_Type.__name__ = "PhysAddress"
_FapBaseMacAddr_Object = MibScalar
fapBaseMacAddr = _FapBaseMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 1, 5),
    _FapBaseMacAddr_Type()
)
fapBaseMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapBaseMacAddr.setStatus("current")
_FapBiosVer_Type = DisplayString
_FapBiosVer_Object = MibScalar
fapBiosVer = _FapBiosVer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 1, 6),
    _FapBiosVer_Type()
)
fapBiosVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapBiosVer.setStatus("current")
_FapBiosDataVer_Type = Integer32
_FapBiosDataVer_Object = MibScalar
fapBiosDataVer = _FapBiosDataVer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 1, 7),
    _FapBiosDataVer_Type()
)
fapBiosDataVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapBiosDataVer.setStatus("current")
_FapSysPartNum_Type = DisplayString
_FapSysPartNum_Object = MibScalar
fapSysPartNum = _FapSysPartNum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 1, 8),
    _FapSysPartNum_Type()
)
fapSysPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapSysPartNum.setStatus("current")
_FapWTPConfig_ObjectIdentity = ObjectIdentity
fapWTPConfig = _FapWTPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2)
)


class _FapWtpWanMode_Type(Integer32):
    """Custom type fapWtpWanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wanOnly", 0),
          ("wanLan", 1),
          ("aggregate", 2))
    )


_FapWtpWanMode_Type.__name__ = "Integer32"
_FapWtpWanMode_Object = MibScalar
fapWtpWanMode = _FapWtpWanMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 1),
    _FapWtpWanMode_Type()
)
fapWtpWanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpWanMode.setStatus("current")


class _FapWtpApAddrMode_Type(Integer32):
    """Custom type fapWtpApAddrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 0),
          ("static", 1))
    )


_FapWtpApAddrMode_Type.__name__ = "Integer32"
_FapWtpApAddrMode_Object = MibScalar
fapWtpApAddrMode = _FapWtpApAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 2),
    _FapWtpApAddrMode_Type()
)
fapWtpApAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpApAddrMode.setStatus("current")
_FapWtpApIpAddr_Type = IpAddress
_FapWtpApIpAddr_Object = MibScalar
fapWtpApIpAddr = _FapWtpApIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 3),
    _FapWtpApIpAddr_Type()
)
fapWtpApIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpApIpAddr.setStatus("current")
_FapWtpApIpNetmask_Type = IpAddress
_FapWtpApIpNetmask_Object = MibScalar
fapWtpApIpNetmask = _FapWtpApIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 4),
    _FapWtpApIpNetmask_Type()
)
fapWtpApIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpApIpNetmask.setStatus("current")
_FapWtpApIpGateway_Type = IpAddress
_FapWtpApIpGateway_Object = MibScalar
fapWtpApIpGateway = _FapWtpApIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 5),
    _FapWtpApIpGateway_Type()
)
fapWtpApIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpApIpGateway.setStatus("current")


class _FapWtpApMode_Type(Integer32):
    """Custom type fapWtpApMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("thinAp", 0),
          ("fatAp", 1),
          ("siteSurvey", 2))
    )


_FapWtpApMode_Type.__name__ = "Integer32"
_FapWtpApMode_Object = MibScalar
fapWtpApMode = _FapWtpApMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 6),
    _FapWtpApMode_Type()
)
fapWtpApMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpApMode.setStatus("current")
_FapWtpApDnsAddr_Type = IpAddress
_FapWtpApDnsAddr_Object = MibScalar
fapWtpApDnsAddr = _FapWtpApDnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 7),
    _FapWtpApDnsAddr_Type()
)
fapWtpApDnsAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpApDnsAddr.setStatus("current")


class _FapWtpApStpMode_Type(Integer32):
    """Custom type fapWtpApStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("disabledWithWanBlock", 2))
    )


_FapWtpApStpMode_Type.__name__ = "Integer32"
_FapWtpApStpMode_Object = MibScalar
fapWtpApStpMode = _FapWtpApStpMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 8),
    _FapWtpApStpMode_Type()
)
fapWtpApStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpApStpMode.setStatus("current")
_FapWtpApMgmtVlanID_Type = Integer32
_FapWtpApMgmtVlanID_Object = MibScalar
fapWtpApMgmtVlanID = _FapWtpApMgmtVlanID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 9),
    _FapWtpApMgmtVlanID_Type()
)
fapWtpApMgmtVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpApMgmtVlanID.setStatus("current")


class _FapWtpApAcDiscoveryType_Type(Integer32):
    """Custom type fapWtpApAcDiscoveryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("static", 1),
          ("dhcp", 2),
          ("dns", 3),
          ("broadcast", 5),
          ("multicast", 6),
          ("fortiCloud", 7))
    )


_FapWtpApAcDiscoveryType_Type.__name__ = "Integer32"
_FapWtpApAcDiscoveryType_Object = MibScalar
fapWtpApAcDiscoveryType = _FapWtpApAcDiscoveryType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 10),
    _FapWtpApAcDiscoveryType_Type()
)
fapWtpApAcDiscoveryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpApAcDiscoveryType.setStatus("current")
_FapWtpApAcAddr1_Type = IpAddress
_FapWtpApAcAddr1_Object = MibScalar
fapWtpApAcAddr1 = _FapWtpApAcAddr1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 11),
    _FapWtpApAcAddr1_Type()
)
fapWtpApAcAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpApAcAddr1.setStatus("current")
_FapWtpApAcAddr2_Type = IpAddress
_FapWtpApAcAddr2_Object = MibScalar
fapWtpApAcAddr2 = _FapWtpApAcAddr2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 12),
    _FapWtpApAcAddr2_Type()
)
fapWtpApAcAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpApAcAddr2.setStatus("current")
_FapWtpApAcAddr3_Type = IpAddress
_FapWtpApAcAddr3_Object = MibScalar
fapWtpApAcAddr3 = _FapWtpApAcAddr3_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 13),
    _FapWtpApAcAddr3_Type()
)
fapWtpApAcAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpApAcAddr3.setStatus("current")
_FapWtpApAcHostname1_Type = DisplayString
_FapWtpApAcHostname1_Object = MibScalar
fapWtpApAcHostname1 = _FapWtpApAcHostname1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 14),
    _FapWtpApAcHostname1_Type()
)
fapWtpApAcHostname1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpApAcHostname1.setStatus("current")
_FapWtpApAcHostname2_Type = DisplayString
_FapWtpApAcHostname2_Object = MibScalar
fapWtpApAcHostname2 = _FapWtpApAcHostname2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 15),
    _FapWtpApAcHostname2_Type()
)
fapWtpApAcHostname2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpApAcHostname2.setStatus("current")
_FapWtpApAcHostname3_Type = DisplayString
_FapWtpApAcHostname3_Object = MibScalar
fapWtpApAcHostname3 = _FapWtpApAcHostname3_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 16),
    _FapWtpApAcHostname3_Type()
)
fapWtpApAcHostname3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpApAcHostname3.setStatus("current")
_FapWtpAcMulticastAddr_Type = IpAddress
_FapWtpAcMulticastAddr_Object = MibScalar
fapWtpAcMulticastAddr = _FapWtpAcMulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 17),
    _FapWtpAcMulticastAddr_Type()
)
fapWtpAcMulticastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpAcMulticastAddr.setStatus("current")
_FapWtpAcDhcpCode_Type = Integer32
_FapWtpAcDhcpCode_Object = MibScalar
fapWtpAcDhcpCode = _FapWtpAcDhcpCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 18),
    _FapWtpAcDhcpCode_Type()
)
fapWtpAcDhcpCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpAcDhcpCode.setStatus("current")
_FapWtpAcFcldApCtrl_Type = DisplayString
_FapWtpAcFcldApCtrl_Object = MibScalar
fapWtpAcFcldApCtrl = _FapWtpAcFcldApCtrl_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 19),
    _FapWtpAcFcldApCtrl_Type()
)
fapWtpAcFcldApCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpAcFcldApCtrl.setStatus("current")
_FapWtpAcFcldId_Type = DisplayString
_FapWtpAcFcldId_Object = MibScalar
fapWtpAcFcldId = _FapWtpAcFcldId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 20),
    _FapWtpAcFcldId_Type()
)
fapWtpAcFcldId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpAcFcldId.setStatus("current")
_FapWtpAcFcldPassword_Type = DisplayString
_FapWtpAcFcldPassword_Object = MibScalar
fapWtpAcFcldPassword = _FapWtpAcFcldPassword_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 21),
    _FapWtpAcFcldPassword_Type()
)
fapWtpAcFcldPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpAcFcldPassword.setStatus("current")
_FapWtpAcCtrlPort_Type = Integer32
_FapWtpAcCtrlPort_Object = MibScalar
fapWtpAcCtrlPort = _FapWtpAcCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 22),
    _FapWtpAcCtrlPort_Type()
)
fapWtpAcCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpAcCtrlPort.setStatus("current")
_FapWtpAcDataChannelSecurity_Type = DisplayString
_FapWtpAcDataChannelSecurity_Object = MibScalar
fapWtpAcDataChannelSecurity = _FapWtpAcDataChannelSecurity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 23),
    _FapWtpAcDataChannelSecurity_Type()
)
fapWtpAcDataChannelSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpAcDataChannelSecurity.setStatus("current")


class _FapWtpMeshApType_Type(Integer32):
    """Custom type fapWtpMeshApType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 0),
          ("mesh", 1),
          ("ethernetMeshBackup", 2))
    )


_FapWtpMeshApType_Type.__name__ = "Integer32"
_FapWtpMeshApType_Object = MibScalar
fapWtpMeshApType = _FapWtpMeshApType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 24),
    _FapWtpMeshApType_Type()
)
fapWtpMeshApType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpMeshApType.setStatus("current")
_FapWtpMeshSSID_Type = DisplayString
_FapWtpMeshSSID_Object = MibScalar
fapWtpMeshSSID = _FapWtpMeshSSID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 25),
    _FapWtpMeshSSID_Type()
)
fapWtpMeshSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpMeshSSID.setStatus("current")
_FapWtpMeshPassword_Type = DisplayString
_FapWtpMeshPassword_Object = MibScalar
fapWtpMeshPassword = _FapWtpMeshPassword_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 26),
    _FapWtpMeshPassword_Type()
)
fapWtpMeshPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpMeshPassword.setStatus("current")


class _FapWtpEthBridge_Type(Integer32):
    """Custom type fapWtpEthBridge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapWtpEthBridge_Type.__name__ = "Integer32"
_FapWtpEthBridge_Object = MibScalar
fapWtpEthBridge = _FapWtpEthBridge_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 27),
    _FapWtpEthBridge_Type()
)
fapWtpEthBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpEthBridge.setStatus("current")
_FapWtpEthBridgeVlans_Type = DisplayString
_FapWtpEthBridgeVlans_Object = MibScalar
fapWtpEthBridgeVlans = _FapWtpEthBridgeVlans_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 28),
    _FapWtpEthBridgeVlans_Type()
)
fapWtpEthBridgeVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapWtpEthBridgeVlans.setStatus("current")


class _FapLedState_Type(Integer32):
    """Custom type fapLedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("controlledByAC", 2))
    )


_FapLedState_Type.__name__ = "Integer32"
_FapLedState_Object = MibScalar
fapLedState = _FapLedState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 29),
    _FapLedState_Type()
)
fapLedState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapLedState.setStatus("current")


class _FapPoeMode_Type(Integer32):
    """Custom type fapPoeMode based on Integer32"""
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
        *(("autoDetect", 0),
          ("ieee8023Af", 1),
          ("ieee8023At", 2),
          ("powerAdapter", 3),
          ("acControlled", 4),
          ("fullPowerMode", 5),
          ("highPowerMode", 6),
          ("lowPowerMode", 7))
    )


_FapPoeMode_Type.__name__ = "Integer32"
_FapPoeMode_Object = MibScalar
fapPoeMode = _FapPoeMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 2, 30),
    _FapPoeMode_Type()
)
fapPoeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fapPoeMode.setStatus("current")
_FapWTPStatus_ObjectIdentity = ObjectIdentity
fapWTPStatus = _FapWTPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3)
)


class _FapAcDiscoveryType_Type(Integer32):
    """Custom type fapAcDiscoveryType based on Integer32"""
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
        *(("unknown", 0),
          ("static", 1),
          ("dhcp", 2),
          ("dns", 3),
          ("acRefer", 4),
          ("broadcast", 5),
          ("multicast", 6),
          ("fortiCloud", 7))
    )


_FapAcDiscoveryType_Type.__name__ = "Integer32"
_FapAcDiscoveryType_Object = MibScalar
fapAcDiscoveryType = _FapAcDiscoveryType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 1),
    _FapAcDiscoveryType_Type()
)
fapAcDiscoveryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapAcDiscoveryType.setStatus("current")
_FapCtlmsgOffload_Type = DisplayString
_FapCtlmsgOffload_Object = MibScalar
fapCtlmsgOffload = _FapCtlmsgOffload_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 2),
    _FapCtlmsgOffload_Type()
)
fapCtlmsgOffload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapCtlmsgOffload.setStatus("current")
_FapAcCertVersion_Type = Integer32
_FapAcCertVersion_Object = MibScalar
fapAcCertVersion = _FapAcCertVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 3),
    _FapAcCertVersion_Type()
)
fapAcCertVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapAcCertVersion.setStatus("current")


class _FapPoeModeOper_Type(Integer32):
    """Custom type fapPoeModeOper based on Integer32"""
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
        *(("autoDetect", 0),
          ("ieee8023Af", 1),
          ("ieee8023At", 2),
          ("powerAdapter", 3),
          ("acControlled", 4),
          ("fullPowerMode", 5),
          ("highPowerMode", 6),
          ("lowPowerMode", 7))
    )


_FapPoeModeOper_Type.__name__ = "Integer32"
_FapPoeModeOper_Object = MibScalar
fapPoeModeOper = _FapPoeModeOper_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 4),
    _FapPoeModeOper_Type()
)
fapPoeModeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapPoeModeOper.setStatus("current")


class _FapLedMode_Type(Integer32):
    """Custom type fapLedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("normal", 1),
          ("blinking", 2))
    )


_FapLedMode_Type.__name__ = "Integer32"
_FapLedMode_Object = MibScalar
fapLedMode = _FapLedMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 5),
    _FapLedMode_Type()
)
fapLedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapLedMode.setStatus("current")
_FapAllowAccess_Type = DisplayString
_FapAllowAccess_Object = MibScalar
fapAllowAccess = _FapAllowAccess_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 6),
    _FapAllowAccess_Type()
)
fapAllowAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapAllowAccess.setStatus("current")


class _FapLldpAccess_Type(Integer32):
    """Custom type fapLldpAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapLldpAccess_Type.__name__ = "Integer32"
_FapLldpAccess_Object = MibScalar
fapLldpAccess = _FapLldpAccess_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 7),
    _FapLldpAccess_Type()
)
fapLldpAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapLldpAccess.setStatus("current")
_FapRadioCount_Type = Integer32
_FapRadioCount_Object = MibScalar
fapRadioCount = _FapRadioCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 8),
    _FapRadioCount_Type()
)
fapRadioCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioCount.setStatus("current")
_FapStationInfo_Type = DisplayString
_FapStationInfo_Object = MibScalar
fapStationInfo = _FapStationInfo_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 9),
    _FapStationInfo_Type()
)
fapStationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapStationInfo.setStatus("current")
_FapEchoInterval_Type = Integer32
_FapEchoInterval_Object = MibScalar
fapEchoInterval = _FapEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 10),
    _FapEchoInterval_Type()
)
fapEchoInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapEchoInterval.setStatus("current")
_FapKeepAliveInterval_Type = Integer32
_FapKeepAliveInterval_Object = MibScalar
fapKeepAliveInterval = _FapKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 11),
    _FapKeepAliveInterval_Type()
)
fapKeepAliveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapKeepAliveInterval.setStatus("current")
_FapRetransmitMax_Type = Integer32
_FapRetransmitMax_Object = MibScalar
fapRetransmitMax = _FapRetransmitMax_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 12),
    _FapRetransmitMax_Type()
)
fapRetransmitMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRetransmitMax.setStatus("current")
_FapDcDeadInterval_Type = Integer32
_FapDcDeadInterval_Object = MibScalar
fapDcDeadInterval = _FapDcDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 13),
    _FapDcDeadInterval_Type()
)
fapDcDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapDcDeadInterval.setStatus("current")
_FapDiscoveryInterval_Type = Integer32
_FapDiscoveryInterval_Object = MibScalar
fapDiscoveryInterval = _FapDiscoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 14),
    _FapDiscoveryInterval_Type()
)
fapDiscoveryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapDiscoveryInterval.setStatus("current")
_FapReportInterval_Type = Integer32
_FapReportInterval_Object = MibScalar
fapReportInterval = _FapReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 15),
    _FapReportInterval_Type()
)
fapReportInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapReportInterval.setStatus("current")
_FapStationStatsInterval_Type = Integer32
_FapStationStatsInterval_Object = MibScalar
fapStationStatsInterval = _FapStationStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 16),
    _FapStationStatsInterval_Type()
)
fapStationStatsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapStationStatsInterval.setStatus("current")
_FapVapStatsInterval_Type = Integer32
_FapVapStatsInterval_Object = MibScalar
fapVapStatsInterval = _FapVapStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 17),
    _FapVapStatsInterval_Type()
)
fapVapStatsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapStatsInterval.setStatus("current")
_FapRadioStatsInterval_Type = Integer32
_FapRadioStatsInterval_Object = MibScalar
fapRadioStatsInterval = _FapRadioStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 18),
    _FapRadioStatsInterval_Type()
)
fapRadioStatsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioStatsInterval.setStatus("current")
_FapStationCapInterval_Type = Integer32
_FapStationCapInterval_Object = MibScalar
fapStationCapInterval = _FapStationCapInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 19),
    _FapStationCapInterval_Type()
)
fapStationCapInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapStationCapInterval.setStatus("current")
_FapIdleTimeout_Type = Integer32
_FapIdleTimeout_Object = MibScalar
fapIdleTimeout = _FapIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 20),
    _FapIdleTimeout_Type()
)
fapIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapIdleTimeout.setStatus("current")
_FapStatisticsInterval_Type = Integer32
_FapStatisticsInterval_Object = MibScalar
fapStatisticsInterval = _FapStatisticsInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 21),
    _FapStatisticsInterval_Type()
)
fapStatisticsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapStatisticsInterval.setStatus("current")
_FapFortiPresenceInterval_Type = Integer32
_FapFortiPresenceInterval_Object = MibScalar
fapFortiPresenceInterval = _FapFortiPresenceInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 22),
    _FapFortiPresenceInterval_Type()
)
fapFortiPresenceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapFortiPresenceInterval.setStatus("current")
_FapFsmState_Type = DisplayString
_FapFsmState_Object = MibScalar
fapFsmState = _FapFsmState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 23),
    _FapFsmState_Type()
)
fapFsmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapFsmState.setStatus("current")
_FapWtpIpAddr_Type = IpAddress
_FapWtpIpAddr_Object = MibScalar
fapWtpIpAddr = _FapWtpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 24),
    _FapWtpIpAddr_Type()
)
fapWtpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapWtpIpAddr.setStatus("current")
_FapAcIpAddr_Type = IpAddress
_FapAcIpAddr_Object = MibScalar
fapAcIpAddr = _FapAcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 25),
    _FapAcIpAddr_Type()
)
fapAcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapAcIpAddr.setStatus("current")
_FapAcPort_Type = Integer32
_FapAcPort_Object = MibScalar
fapAcPort = _FapAcPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 26),
    _FapAcPort_Type()
)
fapAcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapAcPort.setStatus("current")


class _FapIpFragmentPrevent_Type(Integer32):
    """Custom type fapIpFragmentPrevent based on Integer32"""
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
          ("tcpMss", 1),
          ("tunMtu", 2),
          ("both", 3))
    )


_FapIpFragmentPrevent_Type.__name__ = "Integer32"
_FapIpFragmentPrevent_Object = MibScalar
fapIpFragmentPrevent = _FapIpFragmentPrevent_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 27),
    _FapIpFragmentPrevent_Type()
)
fapIpFragmentPrevent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapIpFragmentPrevent.setStatus("current")


class _FapAeroScout_Type(Integer32):
    """Custom type fapAeroScout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapAeroScout_Type.__name__ = "Integer32"
_FapAeroScout_Object = MibScalar
fapAeroScout = _FapAeroScout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 28),
    _FapAeroScout_Type()
)
fapAeroScout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapAeroScout.setStatus("current")


class _FapLanMode_Type(Integer32):
    """Custom type fapLanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("wanLan", 2))
    )


_FapLanMode_Type.__name__ = "Integer32"
_FapLanMode_Object = MibScalar
fapLanMode = _FapLanMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 29),
    _FapLanMode_Type()
)
fapLanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapLanMode.setStatus("current")
_FapLanPortCount_Type = Integer32
_FapLanPortCount_Object = MibScalar
fapLanPortCount = _FapLanPortCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 30),
    _FapLanPortCount_Type()
)
fapLanPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapLanPortCount.setStatus("current")


class _FapDataChannelStatus_Type(Integer32):
    """Custom type fapDataChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FapDataChannelStatus_Type.__name__ = "Integer32"
_FapDataChannelStatus_Object = MibScalar
fapDataChannelStatus = _FapDataChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 31),
    _FapDataChannelStatus_Type()
)
fapDataChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapDataChannelStatus.setStatus("current")


class _FapDataChannelSecurityOper_Type(Integer32):
    """Custom type fapDataChannelSecurityOper based on Integer32"""
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
        *(("clear", 0),
          ("dtls", 1),
          ("ipsec", 2),
          ("ipsecsn", 3))
    )


_FapDataChannelSecurityOper_Type.__name__ = "Integer32"
_FapDataChannelSecurityOper_Object = MibScalar
fapDataChannelSecurityOper = _FapDataChannelSecurityOper_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 32),
    _FapDataChannelSecurityOper_Type()
)
fapDataChannelSecurityOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapDataChannelSecurityOper.setStatus("current")
_FapFortiPresenceServer_Type = IpAddress
_FapFortiPresenceServer_Object = MibScalar
fapFortiPresenceServer = _FapFortiPresenceServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 33),
    _FapFortiPresenceServer_Type()
)
fapFortiPresenceServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapFortiPresenceServer.setStatus("current")
_FapFortiPresencePort_Type = Integer32
_FapFortiPresencePort_Object = MibScalar
fapFortiPresencePort = _FapFortiPresencePort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 34),
    _FapFortiPresencePort_Type()
)
fapFortiPresencePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapFortiPresencePort.setStatus("current")
_FapFortiPresenceProject_Type = DisplayString
_FapFortiPresenceProject_Object = MibScalar
fapFortiPresenceProject = _FapFortiPresenceProject_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 35),
    _FapFortiPresenceProject_Type()
)
fapFortiPresenceProject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapFortiPresenceProject.setStatus("current")
_FapWtpLocation_Type = DisplayString
_FapWtpLocation_Object = MibScalar
fapWtpLocation = _FapWtpLocation_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 36),
    _FapWtpLocation_Type()
)
fapWtpLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapWtpLocation.setStatus("current")
_FapFortiPresenceServerFQDN_Type = DisplayString
_FapFortiPresenceServerFQDN_Object = MibScalar
fapFortiPresenceServerFQDN = _FapFortiPresenceServerFQDN_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 37),
    _FapFortiPresenceServerFQDN_Type()
)
fapFortiPresenceServerFQDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapFortiPresenceServerFQDN.setStatus("current")
_FapWtpUptime_Type = TimeTicks
_FapWtpUptime_Object = MibScalar
fapWtpUptime = _FapWtpUptime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 38),
    _FapWtpUptime_Type()
)
fapWtpUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapWtpUptime.setStatus("current")
_FapByteRxCount_Type = Counter64
_FapByteRxCount_Object = MibScalar
fapByteRxCount = _FapByteRxCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 39),
    _FapByteRxCount_Type()
)
fapByteRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapByteRxCount.setStatus("current")
_FapByteTxCount_Type = Counter64
_FapByteTxCount_Object = MibScalar
fapByteTxCount = _FapByteTxCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 40),
    _FapByteTxCount_Type()
)
fapByteTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapByteTxCount.setStatus("current")
_FapCpuUsage_Type = Integer32
_FapCpuUsage_Object = MibScalar
fapCpuUsage = _FapCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 41),
    _FapCpuUsage_Type()
)
fapCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapCpuUsage.setStatus("current")
_FapMemoryUsage_Type = Integer32
_FapMemoryUsage_Object = MibScalar
fapMemoryUsage = _FapMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 42),
    _FapMemoryUsage_Type()
)
fapMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapMemoryUsage.setStatus("current")
_FapStationCount_Type = Integer32
_FapStationCount_Object = MibScalar
fapStationCount = _FapStationCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 43),
    _FapStationCount_Type()
)
fapStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapStationCount.setStatus("current")
_FapTemperature_Type = Integer32
_FapTemperature_Object = MibScalar
fapTemperature = _FapTemperature_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 3, 44),
    _FapTemperature_Type()
)
fapTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapTemperature.setStatus("current")
_FapRadioTables_ObjectIdentity = ObjectIdentity
fapRadioTables = _FapRadioTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4)
)
_FapRadioTable_Object = MibTable
fapRadioTable = _FapRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1)
)
if mibBuilder.loadTexts:
    fapRadioTable.setStatus("current")
_FapRadioEntry_Object = MibTableRow
fapRadioEntry = _FapRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1)
)
fapRadioEntry.setIndexNames(
    (0, "FORTINET-FORTIAP-MIB", "fapRadioIndex"),
)
if mibBuilder.loadTexts:
    fapRadioEntry.setStatus("current")


class _FapRadioIndex_Type(Integer32):
    """Custom type fapRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_FapRadioIndex_Type.__name__ = "Integer32"
_FapRadioIndex_Object = MibTableColumn
fapRadioIndex = _FapRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 1),
    _FapRadioIndex_Type()
)
fapRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fapRadioIndex.setStatus("current")


class _FapRadioMode_Type(Integer32):
    """Custom type fapRadioMode based on Integer32"""
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
        *(("ap", 0),
          ("disabled", 1),
          ("monitor", 2),
          ("sniffer", 3),
          ("failed", 4))
    )


_FapRadioMode_Type.__name__ = "Integer32"
_FapRadioMode_Object = MibTableColumn
fapRadioMode = _FapRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 2),
    _FapRadioMode_Type()
)
fapRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioMode.setStatus("current")
_FapRadioCountry_Type = DisplayString
_FapRadioCountry_Object = MibTableColumn
fapRadioCountry = _FapRadioCountry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 3),
    _FapRadioCountry_Type()
)
fapRadioCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioCountry.setStatus("current")
_FapRadioCountryId_Type = Integer32
_FapRadioCountryId_Object = MibTableColumn
fapRadioCountryId = _FapRadioCountryId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 4),
    _FapRadioCountryId_Type()
)
fapRadioCountryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioCountryId.setStatus("current")
_FapRadioStationInfo_Type = DisplayString
_FapRadioStationInfo_Object = MibTableColumn
fapRadioStationInfo = _FapRadioStationInfo_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 5),
    _FapRadioStationInfo_Type()
)
fapRadioStationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioStationInfo.setStatus("current")


class _FapRadioType_Type(Integer32):
    """Custom type fapRadioType based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("ieee80211a", 0),
          ("ieee80211b", 1),
          ("ieee80211gonly", 2),
          ("ieee80211ac2g", 3),
          ("ieee80211ac", 4),
          ("ieee80211n24G", 5),
          ("ieee80211n5G", 6),
          ("ieee80211n", 7),
          ("ieee80211ax24G", 8),
          ("ieee80211ax5G", 9),
          ("ieee80211ax", 10),
          ("ieee80211ax6G", 11),
          ("radioTypeInvalid", 255))
    )


_FapRadioType_Type.__name__ = "Integer32"
_FapRadioType_Object = MibTableColumn
fapRadioType = _FapRadioType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 6),
    _FapRadioType_Type()
)
fapRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioType.setStatus("current")


class _FapRadioHT2040Coexist_Type(Integer32):
    """Custom type fapRadioHT2040Coexist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapRadioHT2040Coexist_Type.__name__ = "Integer32"
_FapRadioHT2040Coexist_Object = MibTableColumn
fapRadioHT2040Coexist = _FapRadioHT2040Coexist_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 7),
    _FapRadioHT2040Coexist_Type()
)
fapRadioHT2040Coexist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioHT2040Coexist.setStatus("current")
_FapRadioBeaconInterval_Type = Integer32
_FapRadioBeaconInterval_Object = MibTableColumn
fapRadioBeaconInterval = _FapRadioBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 8),
    _FapRadioBeaconInterval_Type()
)
fapRadioBeaconInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioBeaconInterval.setStatus("current")
_FapRadioTxPowerConfig_Type = Integer32
_FapRadioTxPowerConfig_Object = MibTableColumn
fapRadioTxPowerConfig = _FapRadioTxPowerConfig_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 9),
    _FapRadioTxPowerConfig_Type()
)
fapRadioTxPowerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioTxPowerConfig.setStatus("current")
_FapRadioTxPowerOper_Type = Integer32
_FapRadioTxPowerOper_Object = MibTableColumn
fapRadioTxPowerOper = _FapRadioTxPowerOper_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 10),
    _FapRadioTxPowerOper_Type()
)
fapRadioTxPowerOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioTxPowerOper.setStatus("current")
_FapRadioTxPowerMax_Type = Integer32
_FapRadioTxPowerMax_Object = MibTableColumn
fapRadioTxPowerMax = _FapRadioTxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 11),
    _FapRadioTxPowerMax_Type()
)
fapRadioTxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioTxPowerMax.setStatus("current")


class _FapRadioChannelWidth_Type(Integer32):
    """Custom type fapRadioChannelWidth based on Integer32"""
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
        *(("bw20Mhz", 0),
          ("bw40Mhz", 1),
          ("bw80Mhz", 2),
          ("bw160Mhz", 3))
    )


_FapRadioChannelWidth_Type.__name__ = "Integer32"
_FapRadioChannelWidth_Object = MibTableColumn
fapRadioChannelWidth = _FapRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 12),
    _FapRadioChannelWidth_Type()
)
fapRadioChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioChannelWidth.setStatus("current")


class _FapRadioSGI_Type(Integer32):
    """Custom type fapRadioSGI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapRadioSGI_Type.__name__ = "Integer32"
_FapRadioSGI_Object = MibTableColumn
fapRadioSGI = _FapRadioSGI_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 13),
    _FapRadioSGI_Type()
)
fapRadioSGI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioSGI.setStatus("current")
_FapRadioChannelOper_Type = Integer32
_FapRadioChannelOper_Object = MibTableColumn
fapRadioChannelOper = _FapRadioChannelOper_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 14),
    _FapRadioChannelOper_Type()
)
fapRadioChannelOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioChannelOper.setStatus("current")


class _FapRadioChannelUtil_Type(Integer32):
    """Custom type fapRadioChannelUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("enabled2", 2))
    )


_FapRadioChannelUtil_Type.__name__ = "Integer32"
_FapRadioChannelUtil_Object = MibTableColumn
fapRadioChannelUtil = _FapRadioChannelUtil_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 15),
    _FapRadioChannelUtil_Type()
)
fapRadioChannelUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioChannelUtil.setStatus("current")


class _FapRadioSensorMode_Type(Integer32):
    """Custom type fapRadioSensorMode based on Integer32"""
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
          ("both", 1),
          ("foreignOnly", 2),
          ("invalid", 3))
    )


_FapRadioSensorMode_Type.__name__ = "Integer32"
_FapRadioSensorMode_Object = MibTableColumn
fapRadioSensorMode = _FapRadioSensorMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 16),
    _FapRadioSensorMode_Type()
)
fapRadioSensorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioSensorMode.setStatus("current")


class _FapRadioApScan_Type(Integer32):
    """Custom type fapRadioApScan based on Integer32"""
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
        *(("disable", 0),
          ("background", 1),
          ("foreground", 2),
          ("background2", 3),
          ("foreground2", 4))
    )


_FapRadioApScan_Type.__name__ = "Integer32"
_FapRadioApScan_Object = MibTableColumn
fapRadioApScan = _FapRadioApScan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 17),
    _FapRadioApScan_Type()
)
fapRadioApScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioApScan.setStatus("current")
_FapRadioApScanPeriod_Type = Integer32
_FapRadioApScanPeriod_Object = MibTableColumn
fapRadioApScanPeriod = _FapRadioApScanPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 18),
    _FapRadioApScanPeriod_Type()
)
fapRadioApScanPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioApScanPeriod.setStatus("current")
_FapRadioApScanInterval_Type = Integer32
_FapRadioApScanInterval_Object = MibTableColumn
fapRadioApScanInterval = _FapRadioApScanInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 19),
    _FapRadioApScanInterval_Type()
)
fapRadioApScanInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioApScanInterval.setStatus("current")
_FapRadioApScanDuration_Type = Integer32
_FapRadioApScanDuration_Object = MibTableColumn
fapRadioApScanDuration = _FapRadioApScanDuration_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 20),
    _FapRadioApScanDuration_Type()
)
fapRadioApScanDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioApScanDuration.setStatus("current")
_FapRadioApScanIdleTime_Type = Integer32
_FapRadioApScanIdleTime_Object = MibTableColumn
fapRadioApScanIdleTime = _FapRadioApScanIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 21),
    _FapRadioApScanIdleTime_Type()
)
fapRadioApScanIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioApScanIdleTime.setStatus("current")
_FapRadioApScanReportTimer_Type = Integer32
_FapRadioApScanReportTimer_Object = MibTableColumn
fapRadioApScanReportTimer = _FapRadioApScanReportTimer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 22),
    _FapRadioApScanReportTimer_Type()
)
fapRadioApScanReportTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioApScanReportTimer.setStatus("current")


class _FapRadioDARRP_Type(Integer32):
    """Custom type fapRadioDARRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapRadioDARRP_Type.__name__ = "Integer32"
_FapRadioDARRP_Object = MibTableColumn
fapRadioDARRP = _FapRadioDARRP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 23),
    _FapRadioDARRP_Type()
)
fapRadioDARRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioDARRP.setStatus("current")


class _FapRadioSpectralAnalysis_Type(Integer32):
    """Custom type fapRadioSpectralAnalysis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("scanOnly", 2))
    )


_FapRadioSpectralAnalysis_Type.__name__ = "Integer32"
_FapRadioSpectralAnalysis_Object = MibTableColumn
fapRadioSpectralAnalysis = _FapRadioSpectralAnalysis_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 24),
    _FapRadioSpectralAnalysis_Type()
)
fapRadioSpectralAnalysis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioSpectralAnalysis.setStatus("current")
_FapRadioWIDS_Type = DisplayString
_FapRadioWIDS_Object = MibTableColumn
fapRadioWIDS = _FapRadioWIDS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 25),
    _FapRadioWIDS_Type()
)
fapRadioWIDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioWIDS.setStatus("current")


class _FapRadioFortiPresence_Type(Integer32):
    """Custom type fapRadioFortiPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("foreign", 1),
          ("both", 2))
    )


_FapRadioFortiPresence_Type.__name__ = "Integer32"
_FapRadioFortiPresence_Object = MibTableColumn
fapRadioFortiPresence = _FapRadioFortiPresence_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 26),
    _FapRadioFortiPresence_Type()
)
fapRadioFortiPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioFortiPresence.setStatus("current")


class _FapRadioAirFairness_Type(Integer32):
    """Custom type fapRadioAirFairness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapRadioAirFairness_Type.__name__ = "Integer32"
_FapRadioAirFairness_Object = MibTableColumn
fapRadioAirFairness = _FapRadioAirFairness_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 27),
    _FapRadioAirFairness_Type()
)
fapRadioAirFairness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioAirFairness.setStatus("current")
_FapRadioConfigChannelList_Type = DisplayString
_FapRadioConfigChannelList_Object = MibTableColumn
fapRadioConfigChannelList = _FapRadioConfigChannelList_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 28),
    _FapRadioConfigChannelList_Type()
)
fapRadioConfigChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioConfigChannelList.setStatus("current")
_FapRadioHwChannelList_Type = DisplayString
_FapRadioHwChannelList_Object = MibTableColumn
fapRadioHwChannelList = _FapRadioHwChannelList_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 29),
    _FapRadioHwChannelList_Type()
)
fapRadioHwChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioHwChannelList.setStatus("current")
_FapRadioNolChannelList_Type = DisplayString
_FapRadioNolChannelList_Object = MibTableColumn
fapRadioNolChannelList = _FapRadioNolChannelList_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 4, 1, 1, 30),
    _FapRadioNolChannelList_Type()
)
fapRadioNolChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapRadioNolChannelList.setStatus("current")
_FapVapTables_ObjectIdentity = ObjectIdentity
fapVapTables = _FapVapTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7)
)
_FapVapTable_Object = MibTable
fapVapTable = _FapVapTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1)
)
if mibBuilder.loadTexts:
    fapVapTable.setStatus("current")
_FapVapEntry_Object = MibTableRow
fapVapEntry = _FapVapEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1)
)
fapVapEntry.setIndexNames(
    (0, "FORTINET-FORTIAP-MIB", "fapVapRadioId"),
    (0, "FORTINET-FORTIAP-MIB", "fapVapWlanId"),
)
if mibBuilder.loadTexts:
    fapVapEntry.setStatus("current")


class _FapVapRadioId_Type(Integer32):
    """Custom type fapVapRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_FapVapRadioId_Type.__name__ = "Integer32"
_FapVapRadioId_Object = MibTableColumn
fapVapRadioId = _FapVapRadioId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 1),
    _FapVapRadioId_Type()
)
fapVapRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fapVapRadioId.setStatus("current")


class _FapVapWlanId_Type(Integer32):
    """Custom type fapVapWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FapVapWlanId_Type.__name__ = "Integer32"
_FapVapWlanId_Object = MibTableColumn
fapVapWlanId = _FapVapWlanId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 2),
    _FapVapWlanId_Type()
)
fapVapWlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fapVapWlanId.setStatus("current")


class _FapVapBSSID_Type(PhysAddress):
    """Custom type fapVapBSSID based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_FapVapBSSID_Type.__name__ = "PhysAddress"
_FapVapBSSID_Object = MibTableColumn
fapVapBSSID = _FapVapBSSID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 3),
    _FapVapBSSID_Type()
)
fapVapBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapBSSID.setStatus("current")
_FapVapSSID_Type = DisplayString
_FapVapSSID_Object = MibTableColumn
fapVapSSID = _FapVapSSID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 4),
    _FapVapSSID_Type()
)
fapVapSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapSSID.setStatus("current")


class _FapVapAdmin_Type(Integer32):
    """Custom type fapVapAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_FapVapAdmin_Type.__name__ = "Integer32"
_FapVapAdmin_Object = MibTableColumn
fapVapAdmin = _FapVapAdmin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 5),
    _FapVapAdmin_Type()
)
fapVapAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapAdmin.setStatus("current")


class _FapVapStatus_Type(Integer32):
    """Custom type fapVapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_FapVapStatus_Type.__name__ = "Integer32"
_FapVapStatus_Object = MibTableColumn
fapVapStatus = _FapVapStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 6),
    _FapVapStatus_Type()
)
fapVapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapStatus.setStatus("current")


class _FapVapMeshBackhaul_Type(Integer32):
    """Custom type fapVapMeshBackhaul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapMeshBackhaul_Type.__name__ = "Integer32"
_FapVapMeshBackhaul_Object = MibTableColumn
fapVapMeshBackhaul = _FapVapMeshBackhaul_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 7),
    _FapVapMeshBackhaul_Type()
)
fapVapMeshBackhaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapMeshBackhaul.setStatus("current")


class _FapVapLocalAuth_Type(Integer32):
    """Custom type fapVapLocalAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapLocalAuth_Type.__name__ = "Integer32"
_FapVapLocalAuth_Object = MibTableColumn
fapVapLocalAuth = _FapVapLocalAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 8),
    _FapVapLocalAuth_Type()
)
fapVapLocalAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapLocalAuth.setStatus("current")


class _FapVapLocalStandAlone_Type(Integer32):
    """Custom type fapVapLocalStandAlone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapLocalStandAlone_Type.__name__ = "Integer32"
_FapVapLocalStandAlone_Object = MibTableColumn
fapVapLocalStandAlone = _FapVapLocalStandAlone_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 9),
    _FapVapLocalStandAlone_Type()
)
fapVapLocalStandAlone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapLocalStandAlone.setStatus("current")


class _FapVapNatMode_Type(Integer32):
    """Custom type fapVapNatMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapNatMode_Type.__name__ = "Integer32"
_FapVapNatMode_Object = MibTableColumn
fapVapNatMode = _FapVapNatMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 10),
    _FapVapNatMode_Type()
)
fapVapNatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapNatMode.setStatus("current")


class _FapVapLocalBridging_Type(Integer32):
    """Custom type fapVapLocalBridging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapLocalBridging_Type.__name__ = "Integer32"
_FapVapLocalBridging_Object = MibTableColumn
fapVapLocalBridging = _FapVapLocalBridging_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 11),
    _FapVapLocalBridging_Type()
)
fapVapLocalBridging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapLocalBridging.setStatus("current")


class _FapVapSplitTunnel_Type(Integer32):
    """Custom type fapVapSplitTunnel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapSplitTunnel_Type.__name__ = "Integer32"
_FapVapSplitTunnel_Object = MibTableColumn
fapVapSplitTunnel = _FapVapSplitTunnel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 12),
    _FapVapSplitTunnel_Type()
)
fapVapSplitTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapSplitTunnel.setStatus("current")


class _FapVapLanIsolation_Type(Integer32):
    """Custom type fapVapLanIsolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapLanIsolation_Type.__name__ = "Integer32"
_FapVapLanIsolation_Object = MibTableColumn
fapVapLanIsolation = _FapVapLanIsolation_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 13),
    _FapVapLanIsolation_Type()
)
fapVapLanIsolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapLanIsolation.setStatus("current")


class _FapVapIntraSsidPriv_Type(Integer32):
    """Custom type fapVapIntraSsidPriv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapIntraSsidPriv_Type.__name__ = "Integer32"
_FapVapIntraSsidPriv_Object = MibTableColumn
fapVapIntraSsidPriv = _FapVapIntraSsidPriv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 14),
    _FapVapIntraSsidPriv_Type()
)
fapVapIntraSsidPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapIntraSsidPriv.setStatus("current")


class _FapVapMacAuth_Type(Integer32):
    """Custom type fapVapMacAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapMacAuth_Type.__name__ = "Integer32"
_FapVapMacAuth_Object = MibTableColumn
fapVapMacAuth = _FapVapMacAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 15),
    _FapVapMacAuth_Type()
)
fapVapMacAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapMacAuth.setStatus("current")


class _FapVapMacAuthFailThrough_Type(Integer32):
    """Custom type fapVapMacAuthFailThrough based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapMacAuthFailThrough_Type.__name__ = "Integer32"
_FapVapMacAuthFailThrough_Object = MibTableColumn
fapVapMacAuthFailThrough = _FapVapMacAuthFailThrough_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 16),
    _FapVapMacAuthFailThrough_Type()
)
fapVapMacAuthFailThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapMacAuthFailThrough.setStatus("current")


class _FapVapTunnelType_Type(Integer32):
    """Custom type fapVapTunnelType based on Integer32"""
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
        *(("local", 0),
          ("ieee8023", 1),
          ("ieee80211", 2),
          ("invalid", 3))
    )


_FapVapTunnelType_Type.__name__ = "Integer32"
_FapVapTunnelType_Object = MibTableColumn
fapVapTunnelType = _FapVapTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 17),
    _FapVapTunnelType_Type()
)
fapVapTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapTunnelType.setStatus("current")


class _FapVapVlanId_Type(Integer32):
    """Custom type fapVapVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FapVapVlanId_Type.__name__ = "Integer32"
_FapVapVlanId_Object = MibTableColumn
fapVapVlanId = _FapVapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 18),
    _FapVapVlanId_Type()
)
fapVapVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapVlanId.setStatus("current")
_FapVapAuth_Type = DisplayString
_FapVapAuth_Object = MibTableColumn
fapVapAuth = _FapVapAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 19),
    _FapVapAuth_Type()
)
fapVapAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapAuth.setStatus("current")


class _FapVapProbRespSuppress_Type(Integer32):
    """Custom type fapVapProbRespSuppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapProbRespSuppress_Type.__name__ = "Integer32"
_FapVapProbRespSuppress_Object = MibTableColumn
fapVapProbRespSuppress = _FapVapProbRespSuppress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 20),
    _FapVapProbRespSuppress_Type()
)
fapVapProbRespSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapProbRespSuppress.setStatus("current")
_FapVapProbRespThresh_Type = Integer32
_FapVapProbRespThresh_Object = MibTableColumn
fapVapProbRespThresh = _FapVapProbRespThresh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 21),
    _FapVapProbRespThresh_Type()
)
fapVapProbRespThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapProbRespThresh.setStatus("current")


class _FapVapRxSop_Type(Integer32):
    """Custom type fapVapRxSop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapRxSop_Type.__name__ = "Integer32"
_FapVapRxSop_Object = MibTableColumn
fapVapRxSop = _FapVapRxSop_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 22),
    _FapVapRxSop_Type()
)
fapVapRxSop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapRxSop.setStatus("current")
_FapVapRx5GThresh_Type = Integer32
_FapVapRx5GThresh_Object = MibTableColumn
fapVapRx5GThresh = _FapVapRx5GThresh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 23),
    _FapVapRx5GThresh_Type()
)
fapVapRx5GThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapRx5GThresh.setStatus("current")
_FapVapRx2GThresh_Type = Integer32
_FapVapRx2GThresh_Object = MibTableColumn
fapVapRx2GThresh = _FapVapRx2GThresh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 24),
    _FapVapRx2GThresh_Type()
)
fapVapRx2GThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapRx2GThresh.setStatus("current")


class _FapVapLdpcType_Type(Integer32):
    """Custom type fapVapLdpcType based on Integer32"""
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
          ("ldpcRx", 1),
          ("ldpcTx", 2),
          ("ldpcRxTx", 3))
    )


_FapVapLdpcType_Type.__name__ = "Integer32"
_FapVapLdpcType_Object = MibTableColumn
fapVapLdpcType = _FapVapLdpcType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 25),
    _FapVapLdpcType_Type()
)
fapVapLdpcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapLdpcType.setStatus("current")


class _FapVapDhcpOp82Insert_Type(Integer32):
    """Custom type fapVapDhcpOp82Insert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapDhcpOp82Insert_Type.__name__ = "Integer32"
_FapVapDhcpOp82Insert_Object = MibTableColumn
fapVapDhcpOp82Insert = _FapVapDhcpOp82Insert_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 26),
    _FapVapDhcpOp82Insert_Type()
)
fapVapDhcpOp82Insert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapDhcpOp82Insert.setStatus("current")
_FapVapDhcpOp82CircId_Type = Integer32
_FapVapDhcpOp82CircId_Object = MibTableColumn
fapVapDhcpOp82CircId = _FapVapDhcpOp82CircId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 27),
    _FapVapDhcpOp82CircId_Type()
)
fapVapDhcpOp82CircId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapDhcpOp82CircId.setStatus("current")
_FapVapDhcpOp82RemId_Type = Integer32
_FapVapDhcpOp82RemId_Object = MibTableColumn
fapVapDhcpOp82RemId = _FapVapDhcpOp82RemId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 28),
    _FapVapDhcpOp82RemId_Type()
)
fapVapDhcpOp82RemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapDhcpOp82RemId.setStatus("current")
_FapVapBcSuppression_Type = DisplayString
_FapVapBcSuppression_Object = MibTableColumn
fapVapBcSuppression = _FapVapBcSuppression_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 29),
    _FapVapBcSuppression_Type()
)
fapVapBcSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapBcSuppression.setStatus("current")
_FapVapKeyId_Type = Integer32
_FapVapKeyId_Object = MibTableColumn
fapVapKeyId = _FapVapKeyId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 30),
    _FapVapKeyId_Type()
)
fapVapKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapKeyId.setStatus("current")
_FapVapKeyLength_Type = Integer32
_FapVapKeyLength_Object = MibTableColumn
fapVapKeyLength = _FapVapKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 31),
    _FapVapKeyLength_Type()
)
fapVapKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapKeyLength.setStatus("current")


class _FapVapPMF_Type(Integer32):
    """Custom type fapVapPMF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("optional", 1),
          ("required", 2))
    )


_FapVapPMF_Type.__name__ = "Integer32"
_FapVapPMF_Object = MibTableColumn
fapVapPMF = _FapVapPMF_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 32),
    _FapVapPMF_Type()
)
fapVapPMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapPMF.setStatus("current")


class _FapVapOKC_Type(Integer32):
    """Custom type fapVapOKC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapOKC_Type.__name__ = "Integer32"
_FapVapOKC_Object = MibTableColumn
fapVapOKC = _FapVapOKC_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 33),
    _FapVapOKC_Type()
)
fapVapOKC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapOKC.setStatus("current")


class _FapVapDynamicVLAN_Type(Integer32):
    """Custom type fapVapDynamicVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapDynamicVLAN_Type.__name__ = "Integer32"
_FapVapDynamicVLAN_Object = MibTableColumn
fapVapDynamicVLAN = _FapVapDynamicVLAN_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 34),
    _FapVapDynamicVLAN_Type()
)
fapVapDynamicVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapDynamicVLAN.setStatus("current")


class _FapVapExternRoaming_Type(Integer32):
    """Custom type fapVapExternRoaming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapExternRoaming_Type.__name__ = "Integer32"
_FapVapExternRoaming_Object = MibTableColumn
fapVapExternRoaming = _FapVapExternRoaming_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 35),
    _FapVapExternRoaming_Type()
)
fapVapExternRoaming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapExternRoaming.setStatus("current")


class _FapVapVoiceEnterprise_Type(Integer32):
    """Custom type fapVapVoiceEnterprise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapVoiceEnterprise_Type.__name__ = "Integer32"
_FapVapVoiceEnterprise_Object = MibTableColumn
fapVapVoiceEnterprise = _FapVapVoiceEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 36),
    _FapVapVoiceEnterprise_Type()
)
fapVapVoiceEnterprise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapVoiceEnterprise.setStatus("current")


class _FapVapFastBssTrans_Type(Integer32):
    """Custom type fapVapFastBssTrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapFastBssTrans_Type.__name__ = "Integer32"
_FapVapFastBssTrans_Object = MibTableColumn
fapVapFastBssTrans = _FapVapFastBssTrans_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 37),
    _FapVapFastBssTrans_Type()
)
fapVapFastBssTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapFastBssTrans.setStatus("current")


class _FapVapCpAuth_Type(Integer32):
    """Custom type fapVapCpAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapCpAuth_Type.__name__ = "Integer32"
_FapVapCpAuth_Object = MibTableColumn
fapVapCpAuth = _FapVapCpAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 38),
    _FapVapCpAuth_Type()
)
fapVapCpAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapCpAuth.setStatus("current")
_FapVapWebAuthServer_Type = DisplayString
_FapVapWebAuthServer_Object = MibTableColumn
fapVapWebAuthServer = _FapVapWebAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 39),
    _FapVapWebAuthServer_Type()
)
fapVapWebAuthServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapWebAuthServer.setStatus("current")
_FapVapAtfWeight_Type = Integer32
_FapVapAtfWeight_Object = MibTableColumn
fapVapAtfWeight = _FapVapAtfWeight_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 40),
    _FapVapAtfWeight_Type()
)
fapVapAtfWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapAtfWeight.setStatus("current")
_FapVapRadServer_Type = DisplayString
_FapVapRadServer_Object = MibTableColumn
fapVapRadServer = _FapVapRadServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 41),
    _FapVapRadServer_Type()
)
fapVapRadServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapRadServer.setStatus("current")
_FapVapRadAcctServer_Type = DisplayString
_FapVapRadAcctServer_Object = MibTableColumn
fapVapRadAcctServer = _FapVapRadAcctServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 42),
    _FapVapRadAcctServer_Type()
)
fapVapRadAcctServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapRadAcctServer.setStatus("current")
_FapVapRadAcctInterimIntv_Type = Integer32
_FapVapRadAcctInterimIntv_Object = MibTableColumn
fapVapRadAcctInterimIntv = _FapVapRadAcctInterimIntv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 43),
    _FapVapRadAcctInterimIntv_Type()
)
fapVapRadAcctInterimIntv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapRadAcctInterimIntv.setStatus("current")


class _FapVapRadCoA_Type(Integer32):
    """Custom type fapVapRadCoA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapRadCoA_Type.__name__ = "Integer32"
_FapVapRadCoA_Object = MibTableColumn
fapVapRadCoA = _FapVapRadCoA_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 44),
    _FapVapRadCoA_Type()
)
fapVapRadCoA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapRadCoA.setStatus("current")
_FapVapStaInfoCount_Type = Integer32
_FapVapStaInfoCount_Object = MibTableColumn
fapVapStaInfoCount = _FapVapStaInfoCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 45),
    _FapVapStaInfoCount_Type()
)
fapVapStaInfoCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapStaInfoCount.setStatus("current")
_FapVapStaInfoMax_Type = Integer32
_FapVapStaInfoMax_Object = MibTableColumn
fapVapStaInfoMax = _FapVapStaInfoMax_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 46),
    _FapVapStaInfoMax_Type()
)
fapVapStaInfoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapStaInfoMax.setStatus("current")
_FapVapRateLimitUL_Type = Integer32
_FapVapRateLimitUL_Object = MibTableColumn
fapVapRateLimitUL = _FapVapRateLimitUL_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 47),
    _FapVapRateLimitUL_Type()
)
fapVapRateLimitUL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapRateLimitUL.setStatus("current")
_FapVapRateLimitDL_Type = Integer32
_FapVapRateLimitDL_Object = MibTableColumn
fapVapRateLimitDL = _FapVapRateLimitDL_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 48),
    _FapVapRateLimitDL_Type()
)
fapVapRateLimitDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapRateLimitDL.setStatus("current")
_FapVapRateLimitUlUser_Type = Integer32
_FapVapRateLimitUlUser_Object = MibTableColumn
fapVapRateLimitUlUser = _FapVapRateLimitUlUser_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 49),
    _FapVapRateLimitUlUser_Type()
)
fapVapRateLimitUlUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapRateLimitUlUser.setStatus("current")
_FapVapRateLimitDLUser_Type = Integer32
_FapVapRateLimitDLUser_Object = MibTableColumn
fapVapRateLimitDLUser = _FapVapRateLimitDLUser_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 50),
    _FapVapRateLimitDLUser_Type()
)
fapVapRateLimitDLUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapRateLimitDLUser.setStatus("current")


class _FapVapRateLimitBurst_Type(Integer32):
    """Custom type fapVapRateLimitBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVapRateLimitBurst_Type.__name__ = "Integer32"
_FapVapRateLimitBurst_Object = MibTableColumn
fapVapRateLimitBurst = _FapVapRateLimitBurst_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 51),
    _FapVapRateLimitBurst_Type()
)
fapVapRateLimitBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapRateLimitBurst.setStatus("current")
_FapVapPrimaryWag_Type = DisplayString
_FapVapPrimaryWag_Object = MibTableColumn
fapVapPrimaryWag = _FapVapPrimaryWag_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 52),
    _FapVapPrimaryWag_Type()
)
fapVapPrimaryWag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapPrimaryWag.setStatus("current")
_FapVapSecondaryWag_Type = DisplayString
_FapVapSecondaryWag_Object = MibTableColumn
fapVapSecondaryWag = _FapVapSecondaryWag_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 53),
    _FapVapSecondaryWag_Type()
)
fapVapSecondaryWag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapSecondaryWag.setStatus("current")
_FapVapCurrentWag_Type = DisplayString
_FapVapCurrentWag_Object = MibTableColumn
fapVapCurrentWag = _FapVapCurrentWag_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 54),
    _FapVapCurrentWag_Type()
)
fapVapCurrentWag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapCurrentWag.setStatus("current")
_FapVapTunEchoIntv_Type = Integer32
_FapVapTunEchoIntv_Object = MibTableColumn
fapVapTunEchoIntv = _FapVapTunEchoIntv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 55),
    _FapVapTunEchoIntv_Type()
)
fapVapTunEchoIntv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapTunEchoIntv.setStatus("current")
_FapVapTunFallbackTimeout_Type = Integer32
_FapVapTunFallbackTimeout_Object = MibTableColumn
fapVapTunFallbackTimeout = _FapVapTunFallbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 56),
    _FapVapTunFallbackTimeout_Type()
)
fapVapTunFallbackTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVapTunFallbackTimeout.setStatus("current")


class _FapVap80211k_Type(Integer32):
    """Custom type fapVap80211k based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVap80211k_Type.__name__ = "Integer32"
_FapVap80211k_Object = MibTableColumn
fapVap80211k = _FapVap80211k_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 57),
    _FapVap80211k_Type()
)
fapVap80211k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVap80211k.setStatus("current")


class _FapVap80211v_Type(Integer32):
    """Custom type fapVap80211v based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FapVap80211v_Type.__name__ = "Integer32"
_FapVap80211v_Object = MibTableColumn
fapVap80211v = _FapVap80211v_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 7, 1, 1, 58),
    _FapVap80211v_Type()
)
fapVap80211v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapVap80211v.setStatus("current")
_FapStationTables_ObjectIdentity = ObjectIdentity
fapStationTables = _FapStationTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 8)
)
_FapStationTable_Object = MibTable
fapStationTable = _FapStationTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 8, 1)
)
if mibBuilder.loadTexts:
    fapStationTable.setStatus("current")
_FapStationEntry_Object = MibTableRow
fapStationEntry = _FapStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 8, 1, 1)
)
fapStationEntry.setIndexNames(
    (0, "FORTINET-FORTIAP-MIB", "fapStaRadioId"),
    (0, "FORTINET-FORTIAP-MIB", "fapStaWlanId"),
    (0, "FORTINET-FORTIAP-MIB", "fapStaMacAddr"),
)
if mibBuilder.loadTexts:
    fapStationEntry.setStatus("current")


class _FapStaRadioId_Type(Integer32):
    """Custom type fapStaRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_FapStaRadioId_Type.__name__ = "Integer32"
_FapStaRadioId_Object = MibTableColumn
fapStaRadioId = _FapStaRadioId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 8, 1, 1, 1),
    _FapStaRadioId_Type()
)
fapStaRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fapStaRadioId.setStatus("current")


class _FapStaWlanId_Type(Integer32):
    """Custom type fapStaWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FapStaWlanId_Type.__name__ = "Integer32"
_FapStaWlanId_Object = MibTableColumn
fapStaWlanId = _FapStaWlanId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 8, 1, 1, 2),
    _FapStaWlanId_Type()
)
fapStaWlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fapStaWlanId.setStatus("current")


class _FapStaMacAddr_Type(PhysAddress):
    """Custom type fapStaMacAddr based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_FapStaMacAddr_Type.__name__ = "PhysAddress"
_FapStaMacAddr_Object = MibTableColumn
fapStaMacAddr = _FapStaMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 8, 1, 1, 3),
    _FapStaMacAddr_Type()
)
fapStaMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fapStaMacAddr.setStatus("current")


class _FapStaBSSID_Type(PhysAddress):
    """Custom type fapStaBSSID based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_FapStaBSSID_Type.__name__ = "PhysAddress"
_FapStaBSSID_Object = MibTableColumn
fapStaBSSID = _FapStaBSSID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 8, 1, 1, 4),
    _FapStaBSSID_Type()
)
fapStaBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapStaBSSID.setStatus("current")


class _FapStaVlanId_Type(Integer32):
    """Custom type fapStaVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FapStaVlanId_Type.__name__ = "Integer32"
_FapStaVlanId_Object = MibTableColumn
fapStaVlanId = _FapStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 8, 1, 1, 5),
    _FapStaVlanId_Type()
)
fapStaVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapStaVlanId.setStatus("current")
_FapStaIpAddr_Type = IpAddress
_FapStaIpAddr_Object = MibTableColumn
fapStaIpAddr = _FapStaIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 8, 1, 1, 6),
    _FapStaIpAddr_Type()
)
fapStaIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapStaIpAddr.setStatus("current")
_FapStaSSID_Type = DisplayString
_FapStaSSID_Object = MibTableColumn
fapStaSSID = _FapStaSSID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 8, 1, 1, 7),
    _FapStaSSID_Type()
)
fapStaSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapStaSSID.setStatus("current")
_FapWagTables_ObjectIdentity = ObjectIdentity
fapWagTables = _FapWagTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9)
)
_FapWagTable_Object = MibTable
fapWagTable = _FapWagTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1)
)
if mibBuilder.loadTexts:
    fapWagTable.setStatus("current")
_FapWagEntry_Object = MibTableRow
fapWagEntry = _FapWagEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1, 1)
)
fapWagEntry.setIndexNames(
    (0, "FORTINET-FORTIAP-MIB", "fapWagTunType"),
    (0, "FORTINET-FORTIAP-MIB", "fapWagIpAddr"),
    (0, "FORTINET-FORTIAP-MIB", "fapWagPort"),
)
if mibBuilder.loadTexts:
    fapWagEntry.setStatus("current")


class _FapWagTunType_Type(Integer32):
    """Custom type fapWagTunType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l2tp", 1),
          ("gre", 2))
    )


_FapWagTunType_Type.__name__ = "Integer32"
_FapWagTunType_Object = MibTableColumn
fapWagTunType = _FapWagTunType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1, 1, 1),
    _FapWagTunType_Type()
)
fapWagTunType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fapWagTunType.setStatus("current")
_FapWagIpAddr_Type = IpAddress
_FapWagIpAddr_Object = MibTableColumn
fapWagIpAddr = _FapWagIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1, 1, 2),
    _FapWagIpAddr_Type()
)
fapWagIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fapWagIpAddr.setStatus("current")


class _FapWagPort_Type(Integer32):
    """Custom type fapWagPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_FapWagPort_Type.__name__ = "Integer32"
_FapWagPort_Object = MibTableColumn
fapWagPort = _FapWagPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1, 1, 3),
    _FapWagPort_Type()
)
fapWagPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fapWagPort.setStatus("current")


class _FapWagState_Type(Integer32):
    """Custom type fapWagState based on Integer32"""
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
        *(("init", 0),
          ("activemon", 1),
          ("alive", 2),
          ("dead", 3))
    )


_FapWagState_Type.__name__ = "Integer32"
_FapWagState_Object = MibTableColumn
fapWagState = _FapWagState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1, 1, 4),
    _FapWagState_Type()
)
fapWagState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapWagState.setStatus("current")
_FapWagRxPackets_Type = Counter64
_FapWagRxPackets_Object = MibTableColumn
fapWagRxPackets = _FapWagRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1, 1, 5),
    _FapWagRxPackets_Type()
)
fapWagRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapWagRxPackets.setStatus("current")
_FapWagRxBytes_Type = Counter64
_FapWagRxBytes_Object = MibTableColumn
fapWagRxBytes = _FapWagRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1, 1, 6),
    _FapWagRxBytes_Type()
)
fapWagRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapWagRxBytes.setStatus("current")
_FapWagRxErrors_Type = Counter64
_FapWagRxErrors_Object = MibTableColumn
fapWagRxErrors = _FapWagRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1, 1, 7),
    _FapWagRxErrors_Type()
)
fapWagRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapWagRxErrors.setStatus("current")
_FapWagTxPackets_Type = Counter64
_FapWagTxPackets_Object = MibTableColumn
fapWagTxPackets = _FapWagTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1, 1, 8),
    _FapWagTxPackets_Type()
)
fapWagTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapWagTxPackets.setStatus("current")
_FapWagTxBytes_Type = Counter64
_FapWagTxBytes_Object = MibTableColumn
fapWagTxBytes = _FapWagTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1, 1, 9),
    _FapWagTxBytes_Type()
)
fapWagTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapWagTxBytes.setStatus("current")
_FapWagTxErrors_Type = Counter64
_FapWagTxErrors_Object = MibTableColumn
fapWagTxErrors = _FapWagTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1, 1, 10),
    _FapWagTxErrors_Type()
)
fapWagTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapWagTxErrors.setStatus("current")
_FapWagAliveTime_Type = Integer32
_FapWagAliveTime_Object = MibTableColumn
fapWagAliveTime = _FapWagAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1, 1, 11),
    _FapWagAliveTime_Type()
)
fapWagAliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapWagAliveTime.setStatus("current")
_FapWagPingInterv_Type = Integer32
_FapWagPingInterv_Object = MibTableColumn
fapWagPingInterv = _FapWagPingInterv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1, 1, 12),
    _FapWagPingInterv_Type()
)
fapWagPingInterv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapWagPingInterv.setStatus("current")
_FapWagPingNum_Type = Integer32
_FapWagPingNum_Object = MibTableColumn
fapWagPingNum = _FapWagPingNum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1, 1, 13),
    _FapWagPingNum_Type()
)
fapWagPingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapWagPingNum.setStatus("current")
_FapWagDhcpAddr_Type = IpAddress
_FapWagDhcpAddr_Object = MibTableColumn
fapWagDhcpAddr = _FapWagDhcpAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 120, 9, 1, 1, 14),
    _FapWagDhcpAddr_Type()
)
fapWagDhcpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fapWagDhcpAddr.setStatus("current")
_FapModel_ObjectIdentity = ObjectIdentity
fapModel = _FapModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10)
)
_Fap221e_ObjectIdentity = ObjectIdentity
fap221e = _Fap221e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 22111)
)
_Fapu221ev_ObjectIdentity = ObjectIdentity
fapu221ev = _Fapu221ev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 22121)
)
_Faps221e_ObjectIdentity = ObjectIdentity
faps221e = _Faps221e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 22131)
)
_Fap222e_ObjectIdentity = ObjectIdentity
fap222e = _Fap222e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 22211)
)
_Fap223e_ObjectIdentity = ObjectIdentity
fap223e = _Fap223e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 22311)
)
_Fapu223ev_ObjectIdentity = ObjectIdentity
fapu223ev = _Fapu223ev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 22321)
)
_Faps223e_ObjectIdentity = ObjectIdentity
faps223e = _Faps223e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 22331)
)
_Fap224e_ObjectIdentity = ObjectIdentity
fap224e = _Fap224e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 22411)
)
_Fap231e_ObjectIdentity = ObjectIdentity
fap231e = _Fap231e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 23111)
)
_Fap231f_ObjectIdentity = ObjectIdentity
fap231f = _Fap231f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 23112)
)
_Fap231g_ObjectIdentity = ObjectIdentity
fap231g = _Fap231g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 23113)
)
_Fapu231f_ObjectIdentity = ObjectIdentity
fapu231f = _Fapu231f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 23122)
)
_Fap233g_ObjectIdentity = ObjectIdentity
fap233g = _Fap233g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 23313)
)
_Fap234f_ObjectIdentity = ObjectIdentity
fap234f = _Fap234f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 23412)
)
_Fap234g_ObjectIdentity = ObjectIdentity
fap234g = _Fap234g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 23413)
)
_Fapu234f_ObjectIdentity = ObjectIdentity
fapu234f = _Fapu234f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 23422)
)
_Fap23jf_ObjectIdentity = ObjectIdentity
fap23jf = _Fap23jf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 23912)
)
_Fapu24jev_ObjectIdentity = ObjectIdentity
fapu24jev = _Fapu24jev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 24921)
)
_Fapc24je_ObjectIdentity = ObjectIdentity
fapc24je = _Fapc24je_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 24941)
)
_Fap321e_ObjectIdentity = ObjectIdentity
fap321e = _Fap321e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 32111)
)
_Fapu321ev_ObjectIdentity = ObjectIdentity
fapu321ev = _Fapu321ev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 32121)
)
_Fapu323ev_ObjectIdentity = ObjectIdentity
fapu323ev = _Fapu323ev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 32321)
)
_Fap421e_ObjectIdentity = ObjectIdentity
fap421e = _Fap421e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 42111)
)
_Fapu421ev_ObjectIdentity = ObjectIdentity
fapu421ev = _Fapu421ev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 42121)
)
_Faps421e_ObjectIdentity = ObjectIdentity
faps421e = _Faps421e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 42131)
)
_Fapu422ev_ObjectIdentity = ObjectIdentity
fapu422ev = _Fapu422ev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 42221)
)
_Faps422e_ObjectIdentity = ObjectIdentity
faps422e = _Faps422e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 42231)
)
_Fap423e_ObjectIdentity = ObjectIdentity
fap423e = _Fap423e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 42311)
)
_Fapu423ev_ObjectIdentity = ObjectIdentity
fapu423ev = _Fapu423ev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 42321)
)
_Faps423e_ObjectIdentity = ObjectIdentity
faps423e = _Faps423e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 42331)
)
_Fap431f_ObjectIdentity = ObjectIdentity
fap431f = _Fap431f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 43112)
)
_Fap431g_ObjectIdentity = ObjectIdentity
fap431g = _Fap431g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 43113)
)
_Fapu431f_ObjectIdentity = ObjectIdentity
fapu431f = _Fapu431f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 43122)
)
_Fap432f_ObjectIdentity = ObjectIdentity
fap432f = _Fap432f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 43212)
)
_Fap432g_ObjectIdentity = ObjectIdentity
fap432g = _Fap432g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 43213)
)
_Fapu432f_ObjectIdentity = ObjectIdentity
fapu432f = _Fapu432f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 43222)
)
_Fap433f_ObjectIdentity = ObjectIdentity
fap433f = _Fap433f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 43312)
)
_Fap433g_ObjectIdentity = ObjectIdentity
fap433g = _Fap433g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 43313)
)
_Fapu433f_ObjectIdentity = ObjectIdentity
fapu433f = _Fapu433f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 43322)
)
_Fap831f_ObjectIdentity = ObjectIdentity
fap831f = _Fap831f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 83112)
)
_Fap231fl_ObjectIdentity = ObjectIdentity
fap231fl = _Fap231fl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 231121)
)
_Fap431fl_ObjectIdentity = ObjectIdentity
fap431fl = _Fap431fl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 431121)
)
_Fap432fr_ObjectIdentity = ObjectIdentity
fap432fr = _Fap432fr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 432122)
)
_Fap433fl_ObjectIdentity = ObjectIdentity
fap433fl = _Fap433fl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 10, 433121)
)
_FapMibConformance_ObjectIdentity = ObjectIdentity
fapMibConformance = _FapMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 120, 100)
)

# Managed Objects groups

fapTrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 120, 100, 2)
)
fapTrapObjectGroup.setObjects(
      *(("FORTINET-FORTIAP-MIB", "fapSerialNum"),
        ("FORTINET-FORTIAP-MIB", "fapAcIpAddr"))
)
if mibBuilder.loadTexts:
    fapTrapObjectGroup.setStatus("current")

fapSysCommGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 120, 100, 3)
)
fapSysCommGroup.setObjects(
      *(("FORTINET-FORTIAP-MIB", "fapVersion"),
        ("FORTINET-FORTIAP-MIB", "fapSerialNum"),
        ("FORTINET-FORTIAP-MIB", "fapHostName"),
        ("FORTINET-FORTIAP-MIB", "fapRegionCode"),
        ("FORTINET-FORTIAP-MIB", "fapBaseMacAddr"),
        ("FORTINET-FORTIAP-MIB", "fapBiosVer"),
        ("FORTINET-FORTIAP-MIB", "fapBiosDataVer"),
        ("FORTINET-FORTIAP-MIB", "fapSysPartNum"))
)
if mibBuilder.loadTexts:
    fapSysCommGroup.setStatus("current")

fapWtpConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 120, 100, 4)
)
fapWtpConfGroup.setObjects(
      *(("FORTINET-FORTIAP-MIB", "fapWtpWanMode"),
        ("FORTINET-FORTIAP-MIB", "fapWtpApAddrMode"),
        ("FORTINET-FORTIAP-MIB", "fapWtpApIpAddr"),
        ("FORTINET-FORTIAP-MIB", "fapWtpApIpNetmask"),
        ("FORTINET-FORTIAP-MIB", "fapWtpApIpGateway"),
        ("FORTINET-FORTIAP-MIB", "fapWtpApMode"),
        ("FORTINET-FORTIAP-MIB", "fapWtpApDnsAddr"),
        ("FORTINET-FORTIAP-MIB", "fapWtpApStpMode"),
        ("FORTINET-FORTIAP-MIB", "fapWtpApMgmtVlanID"),
        ("FORTINET-FORTIAP-MIB", "fapWtpApAcDiscoveryType"),
        ("FORTINET-FORTIAP-MIB", "fapWtpApAcAddr1"),
        ("FORTINET-FORTIAP-MIB", "fapWtpApAcAddr2"),
        ("FORTINET-FORTIAP-MIB", "fapWtpApAcAddr3"),
        ("FORTINET-FORTIAP-MIB", "fapWtpApAcHostname1"),
        ("FORTINET-FORTIAP-MIB", "fapWtpApAcHostname2"),
        ("FORTINET-FORTIAP-MIB", "fapWtpApAcHostname3"),
        ("FORTINET-FORTIAP-MIB", "fapWtpAcMulticastAddr"),
        ("FORTINET-FORTIAP-MIB", "fapWtpAcDhcpCode"),
        ("FORTINET-FORTIAP-MIB", "fapWtpAcFcldApCtrl"),
        ("FORTINET-FORTIAP-MIB", "fapWtpAcFcldId"),
        ("FORTINET-FORTIAP-MIB", "fapWtpAcFcldPassword"),
        ("FORTINET-FORTIAP-MIB", "fapWtpAcCtrlPort"),
        ("FORTINET-FORTIAP-MIB", "fapWtpAcDataChannelSecurity"),
        ("FORTINET-FORTIAP-MIB", "fapWtpMeshApType"),
        ("FORTINET-FORTIAP-MIB", "fapWtpMeshSSID"),
        ("FORTINET-FORTIAP-MIB", "fapWtpMeshPassword"),
        ("FORTINET-FORTIAP-MIB", "fapWtpEthBridge"),
        ("FORTINET-FORTIAP-MIB", "fapWtpEthBridgeVlans"),
        ("FORTINET-FORTIAP-MIB", "fapLedState"),
        ("FORTINET-FORTIAP-MIB", "fapPoeMode"))
)
if mibBuilder.loadTexts:
    fapWtpConfGroup.setStatus("current")

fapWtpStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 120, 100, 5)
)
fapWtpStatusGroup.setObjects(
      *(("FORTINET-FORTIAP-MIB", "fapAcDiscoveryType"),
        ("FORTINET-FORTIAP-MIB", "fapCtlmsgOffload"),
        ("FORTINET-FORTIAP-MIB", "fapAcCertVersion"),
        ("FORTINET-FORTIAP-MIB", "fapPoeModeOper"),
        ("FORTINET-FORTIAP-MIB", "fapLedMode"),
        ("FORTINET-FORTIAP-MIB", "fapAllowAccess"),
        ("FORTINET-FORTIAP-MIB", "fapLldpAccess"),
        ("FORTINET-FORTIAP-MIB", "fapRadioCount"),
        ("FORTINET-FORTIAP-MIB", "fapStationInfo"),
        ("FORTINET-FORTIAP-MIB", "fapEchoInterval"),
        ("FORTINET-FORTIAP-MIB", "fapKeepAliveInterval"),
        ("FORTINET-FORTIAP-MIB", "fapRetransmitMax"),
        ("FORTINET-FORTIAP-MIB", "fapDcDeadInterval"),
        ("FORTINET-FORTIAP-MIB", "fapDiscoveryInterval"),
        ("FORTINET-FORTIAP-MIB", "fapReportInterval"),
        ("FORTINET-FORTIAP-MIB", "fapStationStatsInterval"),
        ("FORTINET-FORTIAP-MIB", "fapVapStatsInterval"),
        ("FORTINET-FORTIAP-MIB", "fapRadioStatsInterval"),
        ("FORTINET-FORTIAP-MIB", "fapStationCapInterval"),
        ("FORTINET-FORTIAP-MIB", "fapIdleTimeout"),
        ("FORTINET-FORTIAP-MIB", "fapStatisticsInterval"),
        ("FORTINET-FORTIAP-MIB", "fapFortiPresenceInterval"),
        ("FORTINET-FORTIAP-MIB", "fapFsmState"),
        ("FORTINET-FORTIAP-MIB", "fapWtpIpAddr"),
        ("FORTINET-FORTIAP-MIB", "fapAcIpAddr"),
        ("FORTINET-FORTIAP-MIB", "fapAcPort"),
        ("FORTINET-FORTIAP-MIB", "fapIpFragmentPrevent"),
        ("FORTINET-FORTIAP-MIB", "fapAeroScout"),
        ("FORTINET-FORTIAP-MIB", "fapLanMode"),
        ("FORTINET-FORTIAP-MIB", "fapLanPortCount"),
        ("FORTINET-FORTIAP-MIB", "fapDataChannelStatus"),
        ("FORTINET-FORTIAP-MIB", "fapDataChannelSecurityOper"),
        ("FORTINET-FORTIAP-MIB", "fapFortiPresenceServer"),
        ("FORTINET-FORTIAP-MIB", "fapFortiPresencePort"),
        ("FORTINET-FORTIAP-MIB", "fapFortiPresenceProject"),
        ("FORTINET-FORTIAP-MIB", "fapWtpLocation"),
        ("FORTINET-FORTIAP-MIB", "fapFortiPresenceServerFQDN"),
        ("FORTINET-FORTIAP-MIB", "fapWtpUptime"),
        ("FORTINET-FORTIAP-MIB", "fapByteRxCount"),
        ("FORTINET-FORTIAP-MIB", "fapByteTxCount"),
        ("FORTINET-FORTIAP-MIB", "fapCpuUsage"),
        ("FORTINET-FORTIAP-MIB", "fapMemoryUsage"),
        ("FORTINET-FORTIAP-MIB", "fapStationCount"),
        ("FORTINET-FORTIAP-MIB", "fapTemperature"))
)
if mibBuilder.loadTexts:
    fapWtpStatusGroup.setStatus("current")

fapRadioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 120, 100, 6)
)
fapRadioGroup.setObjects(
      *(("FORTINET-FORTIAP-MIB", "fapRadioMode"),
        ("FORTINET-FORTIAP-MIB", "fapRadioCountry"),
        ("FORTINET-FORTIAP-MIB", "fapRadioCountryId"),
        ("FORTINET-FORTIAP-MIB", "fapRadioStationInfo"),
        ("FORTINET-FORTIAP-MIB", "fapRadioType"),
        ("FORTINET-FORTIAP-MIB", "fapRadioHT2040Coexist"),
        ("FORTINET-FORTIAP-MIB", "fapRadioBeaconInterval"),
        ("FORTINET-FORTIAP-MIB", "fapRadioTxPowerConfig"),
        ("FORTINET-FORTIAP-MIB", "fapRadioTxPowerOper"),
        ("FORTINET-FORTIAP-MIB", "fapRadioTxPowerMax"),
        ("FORTINET-FORTIAP-MIB", "fapRadioChannelWidth"),
        ("FORTINET-FORTIAP-MIB", "fapRadioSGI"),
        ("FORTINET-FORTIAP-MIB", "fapRadioChannelOper"),
        ("FORTINET-FORTIAP-MIB", "fapRadioChannelUtil"),
        ("FORTINET-FORTIAP-MIB", "fapRadioSensorMode"),
        ("FORTINET-FORTIAP-MIB", "fapRadioApScan"),
        ("FORTINET-FORTIAP-MIB", "fapRadioApScanPeriod"),
        ("FORTINET-FORTIAP-MIB", "fapRadioApScanInterval"),
        ("FORTINET-FORTIAP-MIB", "fapRadioApScanDuration"),
        ("FORTINET-FORTIAP-MIB", "fapRadioApScanIdleTime"),
        ("FORTINET-FORTIAP-MIB", "fapRadioApScanReportTimer"),
        ("FORTINET-FORTIAP-MIB", "fapRadioDARRP"),
        ("FORTINET-FORTIAP-MIB", "fapRadioSpectralAnalysis"),
        ("FORTINET-FORTIAP-MIB", "fapRadioWIDS"),
        ("FORTINET-FORTIAP-MIB", "fapRadioFortiPresence"),
        ("FORTINET-FORTIAP-MIB", "fapRadioAirFairness"),
        ("FORTINET-FORTIAP-MIB", "fapRadioConfigChannelList"),
        ("FORTINET-FORTIAP-MIB", "fapRadioHwChannelList"),
        ("FORTINET-FORTIAP-MIB", "fapRadioNolChannelList"))
)
if mibBuilder.loadTexts:
    fapRadioGroup.setStatus("current")

fapVapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 120, 100, 7)
)
fapVapGroup.setObjects(
      *(("FORTINET-FORTIAP-MIB", "fapVapBSSID"),
        ("FORTINET-FORTIAP-MIB", "fapVapSSID"),
        ("FORTINET-FORTIAP-MIB", "fapVapAdmin"),
        ("FORTINET-FORTIAP-MIB", "fapVapStatus"),
        ("FORTINET-FORTIAP-MIB", "fapVapMeshBackhaul"),
        ("FORTINET-FORTIAP-MIB", "fapVapLocalAuth"),
        ("FORTINET-FORTIAP-MIB", "fapVapLocalStandAlone"),
        ("FORTINET-FORTIAP-MIB", "fapVapNatMode"),
        ("FORTINET-FORTIAP-MIB", "fapVapLocalBridging"),
        ("FORTINET-FORTIAP-MIB", "fapVapSplitTunnel"),
        ("FORTINET-FORTIAP-MIB", "fapVapLanIsolation"),
        ("FORTINET-FORTIAP-MIB", "fapVapIntraSsidPriv"),
        ("FORTINET-FORTIAP-MIB", "fapVapMacAuth"),
        ("FORTINET-FORTIAP-MIB", "fapVapMacAuthFailThrough"),
        ("FORTINET-FORTIAP-MIB", "fapVapTunnelType"),
        ("FORTINET-FORTIAP-MIB", "fapVapVlanId"),
        ("FORTINET-FORTIAP-MIB", "fapVapAuth"),
        ("FORTINET-FORTIAP-MIB", "fapVapProbRespSuppress"),
        ("FORTINET-FORTIAP-MIB", "fapVapProbRespThresh"),
        ("FORTINET-FORTIAP-MIB", "fapVapRxSop"),
        ("FORTINET-FORTIAP-MIB", "fapVapRx5GThresh"),
        ("FORTINET-FORTIAP-MIB", "fapVapRx2GThresh"),
        ("FORTINET-FORTIAP-MIB", "fapVapLdpcType"),
        ("FORTINET-FORTIAP-MIB", "fapVapDhcpOp82Insert"),
        ("FORTINET-FORTIAP-MIB", "fapVapDhcpOp82CircId"),
        ("FORTINET-FORTIAP-MIB", "fapVapDhcpOp82RemId"),
        ("FORTINET-FORTIAP-MIB", "fapVapBcSuppression"),
        ("FORTINET-FORTIAP-MIB", "fapVapKeyId"),
        ("FORTINET-FORTIAP-MIB", "fapVapKeyLength"),
        ("FORTINET-FORTIAP-MIB", "fapVapPMF"),
        ("FORTINET-FORTIAP-MIB", "fapVapOKC"),
        ("FORTINET-FORTIAP-MIB", "fapVapDynamicVLAN"),
        ("FORTINET-FORTIAP-MIB", "fapVapExternRoaming"),
        ("FORTINET-FORTIAP-MIB", "fapVapVoiceEnterprise"),
        ("FORTINET-FORTIAP-MIB", "fapVapFastBssTrans"),
        ("FORTINET-FORTIAP-MIB", "fapVapCpAuth"),
        ("FORTINET-FORTIAP-MIB", "fapVapWebAuthServer"),
        ("FORTINET-FORTIAP-MIB", "fapVapAtfWeight"),
        ("FORTINET-FORTIAP-MIB", "fapVapRadServer"),
        ("FORTINET-FORTIAP-MIB", "fapVapRadAcctServer"),
        ("FORTINET-FORTIAP-MIB", "fapVapRadAcctInterimIntv"),
        ("FORTINET-FORTIAP-MIB", "fapVapRadCoA"),
        ("FORTINET-FORTIAP-MIB", "fapVapStaInfoCount"),
        ("FORTINET-FORTIAP-MIB", "fapVapStaInfoMax"),
        ("FORTINET-FORTIAP-MIB", "fapVapRateLimitUL"),
        ("FORTINET-FORTIAP-MIB", "fapVapRateLimitDL"),
        ("FORTINET-FORTIAP-MIB", "fapVapRateLimitUlUser"),
        ("FORTINET-FORTIAP-MIB", "fapVapRateLimitDLUser"),
        ("FORTINET-FORTIAP-MIB", "fapVapRateLimitBurst"),
        ("FORTINET-FORTIAP-MIB", "fapVapPrimaryWag"),
        ("FORTINET-FORTIAP-MIB", "fapVapSecondaryWag"),
        ("FORTINET-FORTIAP-MIB", "fapVapCurrentWag"),
        ("FORTINET-FORTIAP-MIB", "fapVapTunEchoIntv"),
        ("FORTINET-FORTIAP-MIB", "fapVapTunFallbackTimeout"),
        ("FORTINET-FORTIAP-MIB", "fapVap80211k"),
        ("FORTINET-FORTIAP-MIB", "fapVap80211v"))
)
if mibBuilder.loadTexts:
    fapVapGroup.setStatus("current")

fapWagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 120, 100, 8)
)
fapWagGroup.setObjects(
      *(("FORTINET-FORTIAP-MIB", "fapWagPingInterv"),
        ("FORTINET-FORTIAP-MIB", "fapWagPingNum"),
        ("FORTINET-FORTIAP-MIB", "fapWagDhcpAddr"),
        ("FORTINET-FORTIAP-MIB", "fapWagState"),
        ("FORTINET-FORTIAP-MIB", "fapWagAliveTime"),
        ("FORTINET-FORTIAP-MIB", "fapWagRxPackets"),
        ("FORTINET-FORTIAP-MIB", "fapWagRxBytes"),
        ("FORTINET-FORTIAP-MIB", "fapWagRxErrors"),
        ("FORTINET-FORTIAP-MIB", "fapWagTxPackets"),
        ("FORTINET-FORTIAP-MIB", "fapWagTxBytes"),
        ("FORTINET-FORTIAP-MIB", "fapWagTxErrors"))
)
if mibBuilder.loadTexts:
    fapWagGroup.setStatus("current")

fapStationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 120, 100, 9)
)
fapStationGroup.setObjects(
      *(("FORTINET-FORTIAP-MIB", "fapStaBSSID"),
        ("FORTINET-FORTIAP-MIB", "fapStaVlanId"),
        ("FORTINET-FORTIAP-MIB", "fapStaIpAddr"),
        ("FORTINET-FORTIAP-MIB", "fapStaSSID"))
)
if mibBuilder.loadTexts:
    fapStationGroup.setStatus("current")


# Notification objects

fapDevUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 120, 0, 1)
)
fapDevUp.setObjects(
    ("FORTINET-FORTIAP-MIB", "fapSerialNum")
)
if mibBuilder.loadTexts:
    fapDevUp.setStatus(
        "current"
    )

fapCpuOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 120, 0, 2)
)
fapCpuOverload.setObjects(
    ("FORTINET-FORTIAP-MIB", "fapSerialNum")
)
if mibBuilder.loadTexts:
    fapCpuOverload.setStatus(
        "current"
    )

fapMemOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 120, 0, 3)
)
fapMemOverload.setObjects(
    ("FORTINET-FORTIAP-MIB", "fapSerialNum")
)
if mibBuilder.loadTexts:
    fapMemOverload.setStatus(
        "current"
    )

fapDevDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 120, 0, 4)
)
fapDevDown.setObjects(
    ("FORTINET-FORTIAP-MIB", "fapSerialNum")
)
if mibBuilder.loadTexts:
    fapDevDown.setStatus(
        "current"
    )

fapAcConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 120, 0, 5)
)
fapAcConnected.setObjects(
      *(("FORTINET-FORTIAP-MIB", "fapAcIpAddr"),
        ("FORTINET-FORTIAP-MIB", "fapSerialNum"))
)
if mibBuilder.loadTexts:
    fapAcConnected.setStatus(
        "current"
    )


# Notifications groups

fapTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 120, 100, 1)
)
fapTrapGroup.setObjects(
      *(("FORTINET-FORTIAP-MIB", "fapDevUp"),
        ("FORTINET-FORTIAP-MIB", "fapDevDown"),
        ("FORTINET-FORTIAP-MIB", "fapAcConnected"),
        ("FORTINET-FORTIAP-MIB", "fapCpuOverload"),
        ("FORTINET-FORTIAP-MIB", "fapMemOverload"))
)
if mibBuilder.loadTexts:
    fapTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fapMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 120, 100, 100)
)
fapMibCompliance.setObjects(
      *(("FORTINET-FORTIAP-MIB", "fapTrapObjectGroup"),
        ("FORTINET-FORTIAP-MIB", "fapTrapGroup"),
        ("FORTINET-FORTIAP-MIB", "fapSysCommGroup"),
        ("FORTINET-FORTIAP-MIB", "fapWtpConfGroup"),
        ("FORTINET-FORTIAP-MIB", "fapWtpStatusGroup"),
        ("FORTINET-FORTIAP-MIB", "fapRadioGroup"),
        ("FORTINET-FORTIAP-MIB", "fapVapGroup"),
        ("FORTINET-FORTIAP-MIB", "fapWagGroup"),
        ("FORTINET-FORTIAP-MIB", "fapStationGroup"))
)
if mibBuilder.loadTexts:
    fapMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTIAP-MIB",
    **{"fnFortiAPMib": fnFortiAPMib,
       "fapTraps": fapTraps,
       "fapDevUp": fapDevUp,
       "fapCpuOverload": fapCpuOverload,
       "fapMemOverload": fapMemOverload,
       "fapDevDown": fapDevDown,
       "fapAcConnected": fapAcConnected,
       "fapCommon": fapCommon,
       "fapVersion": fapVersion,
       "fapSerialNum": fapSerialNum,
       "fapHostName": fapHostName,
       "fapRegionCode": fapRegionCode,
       "fapBaseMacAddr": fapBaseMacAddr,
       "fapBiosVer": fapBiosVer,
       "fapBiosDataVer": fapBiosDataVer,
       "fapSysPartNum": fapSysPartNum,
       "fapWTPConfig": fapWTPConfig,
       "fapWtpWanMode": fapWtpWanMode,
       "fapWtpApAddrMode": fapWtpApAddrMode,
       "fapWtpApIpAddr": fapWtpApIpAddr,
       "fapWtpApIpNetmask": fapWtpApIpNetmask,
       "fapWtpApIpGateway": fapWtpApIpGateway,
       "fapWtpApMode": fapWtpApMode,
       "fapWtpApDnsAddr": fapWtpApDnsAddr,
       "fapWtpApStpMode": fapWtpApStpMode,
       "fapWtpApMgmtVlanID": fapWtpApMgmtVlanID,
       "fapWtpApAcDiscoveryType": fapWtpApAcDiscoveryType,
       "fapWtpApAcAddr1": fapWtpApAcAddr1,
       "fapWtpApAcAddr2": fapWtpApAcAddr2,
       "fapWtpApAcAddr3": fapWtpApAcAddr3,
       "fapWtpApAcHostname1": fapWtpApAcHostname1,
       "fapWtpApAcHostname2": fapWtpApAcHostname2,
       "fapWtpApAcHostname3": fapWtpApAcHostname3,
       "fapWtpAcMulticastAddr": fapWtpAcMulticastAddr,
       "fapWtpAcDhcpCode": fapWtpAcDhcpCode,
       "fapWtpAcFcldApCtrl": fapWtpAcFcldApCtrl,
       "fapWtpAcFcldId": fapWtpAcFcldId,
       "fapWtpAcFcldPassword": fapWtpAcFcldPassword,
       "fapWtpAcCtrlPort": fapWtpAcCtrlPort,
       "fapWtpAcDataChannelSecurity": fapWtpAcDataChannelSecurity,
       "fapWtpMeshApType": fapWtpMeshApType,
       "fapWtpMeshSSID": fapWtpMeshSSID,
       "fapWtpMeshPassword": fapWtpMeshPassword,
       "fapWtpEthBridge": fapWtpEthBridge,
       "fapWtpEthBridgeVlans": fapWtpEthBridgeVlans,
       "fapLedState": fapLedState,
       "fapPoeMode": fapPoeMode,
       "fapWTPStatus": fapWTPStatus,
       "fapAcDiscoveryType": fapAcDiscoveryType,
       "fapCtlmsgOffload": fapCtlmsgOffload,
       "fapAcCertVersion": fapAcCertVersion,
       "fapPoeModeOper": fapPoeModeOper,
       "fapLedMode": fapLedMode,
       "fapAllowAccess": fapAllowAccess,
       "fapLldpAccess": fapLldpAccess,
       "fapRadioCount": fapRadioCount,
       "fapStationInfo": fapStationInfo,
       "fapEchoInterval": fapEchoInterval,
       "fapKeepAliveInterval": fapKeepAliveInterval,
       "fapRetransmitMax": fapRetransmitMax,
       "fapDcDeadInterval": fapDcDeadInterval,
       "fapDiscoveryInterval": fapDiscoveryInterval,
       "fapReportInterval": fapReportInterval,
       "fapStationStatsInterval": fapStationStatsInterval,
       "fapVapStatsInterval": fapVapStatsInterval,
       "fapRadioStatsInterval": fapRadioStatsInterval,
       "fapStationCapInterval": fapStationCapInterval,
       "fapIdleTimeout": fapIdleTimeout,
       "fapStatisticsInterval": fapStatisticsInterval,
       "fapFortiPresenceInterval": fapFortiPresenceInterval,
       "fapFsmState": fapFsmState,
       "fapWtpIpAddr": fapWtpIpAddr,
       "fapAcIpAddr": fapAcIpAddr,
       "fapAcPort": fapAcPort,
       "fapIpFragmentPrevent": fapIpFragmentPrevent,
       "fapAeroScout": fapAeroScout,
       "fapLanMode": fapLanMode,
       "fapLanPortCount": fapLanPortCount,
       "fapDataChannelStatus": fapDataChannelStatus,
       "fapDataChannelSecurityOper": fapDataChannelSecurityOper,
       "fapFortiPresenceServer": fapFortiPresenceServer,
       "fapFortiPresencePort": fapFortiPresencePort,
       "fapFortiPresenceProject": fapFortiPresenceProject,
       "fapWtpLocation": fapWtpLocation,
       "fapFortiPresenceServerFQDN": fapFortiPresenceServerFQDN,
       "fapWtpUptime": fapWtpUptime,
       "fapByteRxCount": fapByteRxCount,
       "fapByteTxCount": fapByteTxCount,
       "fapCpuUsage": fapCpuUsage,
       "fapMemoryUsage": fapMemoryUsage,
       "fapStationCount": fapStationCount,
       "fapTemperature": fapTemperature,
       "fapRadioTables": fapRadioTables,
       "fapRadioTable": fapRadioTable,
       "fapRadioEntry": fapRadioEntry,
       "fapRadioIndex": fapRadioIndex,
       "fapRadioMode": fapRadioMode,
       "fapRadioCountry": fapRadioCountry,
       "fapRadioCountryId": fapRadioCountryId,
       "fapRadioStationInfo": fapRadioStationInfo,
       "fapRadioType": fapRadioType,
       "fapRadioHT2040Coexist": fapRadioHT2040Coexist,
       "fapRadioBeaconInterval": fapRadioBeaconInterval,
       "fapRadioTxPowerConfig": fapRadioTxPowerConfig,
       "fapRadioTxPowerOper": fapRadioTxPowerOper,
       "fapRadioTxPowerMax": fapRadioTxPowerMax,
       "fapRadioChannelWidth": fapRadioChannelWidth,
       "fapRadioSGI": fapRadioSGI,
       "fapRadioChannelOper": fapRadioChannelOper,
       "fapRadioChannelUtil": fapRadioChannelUtil,
       "fapRadioSensorMode": fapRadioSensorMode,
       "fapRadioApScan": fapRadioApScan,
       "fapRadioApScanPeriod": fapRadioApScanPeriod,
       "fapRadioApScanInterval": fapRadioApScanInterval,
       "fapRadioApScanDuration": fapRadioApScanDuration,
       "fapRadioApScanIdleTime": fapRadioApScanIdleTime,
       "fapRadioApScanReportTimer": fapRadioApScanReportTimer,
       "fapRadioDARRP": fapRadioDARRP,
       "fapRadioSpectralAnalysis": fapRadioSpectralAnalysis,
       "fapRadioWIDS": fapRadioWIDS,
       "fapRadioFortiPresence": fapRadioFortiPresence,
       "fapRadioAirFairness": fapRadioAirFairness,
       "fapRadioConfigChannelList": fapRadioConfigChannelList,
       "fapRadioHwChannelList": fapRadioHwChannelList,
       "fapRadioNolChannelList": fapRadioNolChannelList,
       "fapVapTables": fapVapTables,
       "fapVapTable": fapVapTable,
       "fapVapEntry": fapVapEntry,
       "fapVapRadioId": fapVapRadioId,
       "fapVapWlanId": fapVapWlanId,
       "fapVapBSSID": fapVapBSSID,
       "fapVapSSID": fapVapSSID,
       "fapVapAdmin": fapVapAdmin,
       "fapVapStatus": fapVapStatus,
       "fapVapMeshBackhaul": fapVapMeshBackhaul,
       "fapVapLocalAuth": fapVapLocalAuth,
       "fapVapLocalStandAlone": fapVapLocalStandAlone,
       "fapVapNatMode": fapVapNatMode,
       "fapVapLocalBridging": fapVapLocalBridging,
       "fapVapSplitTunnel": fapVapSplitTunnel,
       "fapVapLanIsolation": fapVapLanIsolation,
       "fapVapIntraSsidPriv": fapVapIntraSsidPriv,
       "fapVapMacAuth": fapVapMacAuth,
       "fapVapMacAuthFailThrough": fapVapMacAuthFailThrough,
       "fapVapTunnelType": fapVapTunnelType,
       "fapVapVlanId": fapVapVlanId,
       "fapVapAuth": fapVapAuth,
       "fapVapProbRespSuppress": fapVapProbRespSuppress,
       "fapVapProbRespThresh": fapVapProbRespThresh,
       "fapVapRxSop": fapVapRxSop,
       "fapVapRx5GThresh": fapVapRx5GThresh,
       "fapVapRx2GThresh": fapVapRx2GThresh,
       "fapVapLdpcType": fapVapLdpcType,
       "fapVapDhcpOp82Insert": fapVapDhcpOp82Insert,
       "fapVapDhcpOp82CircId": fapVapDhcpOp82CircId,
       "fapVapDhcpOp82RemId": fapVapDhcpOp82RemId,
       "fapVapBcSuppression": fapVapBcSuppression,
       "fapVapKeyId": fapVapKeyId,
       "fapVapKeyLength": fapVapKeyLength,
       "fapVapPMF": fapVapPMF,
       "fapVapOKC": fapVapOKC,
       "fapVapDynamicVLAN": fapVapDynamicVLAN,
       "fapVapExternRoaming": fapVapExternRoaming,
       "fapVapVoiceEnterprise": fapVapVoiceEnterprise,
       "fapVapFastBssTrans": fapVapFastBssTrans,
       "fapVapCpAuth": fapVapCpAuth,
       "fapVapWebAuthServer": fapVapWebAuthServer,
       "fapVapAtfWeight": fapVapAtfWeight,
       "fapVapRadServer": fapVapRadServer,
       "fapVapRadAcctServer": fapVapRadAcctServer,
       "fapVapRadAcctInterimIntv": fapVapRadAcctInterimIntv,
       "fapVapRadCoA": fapVapRadCoA,
       "fapVapStaInfoCount": fapVapStaInfoCount,
       "fapVapStaInfoMax": fapVapStaInfoMax,
       "fapVapRateLimitUL": fapVapRateLimitUL,
       "fapVapRateLimitDL": fapVapRateLimitDL,
       "fapVapRateLimitUlUser": fapVapRateLimitUlUser,
       "fapVapRateLimitDLUser": fapVapRateLimitDLUser,
       "fapVapRateLimitBurst": fapVapRateLimitBurst,
       "fapVapPrimaryWag": fapVapPrimaryWag,
       "fapVapSecondaryWag": fapVapSecondaryWag,
       "fapVapCurrentWag": fapVapCurrentWag,
       "fapVapTunEchoIntv": fapVapTunEchoIntv,
       "fapVapTunFallbackTimeout": fapVapTunFallbackTimeout,
       "fapVap80211k": fapVap80211k,
       "fapVap80211v": fapVap80211v,
       "fapStationTables": fapStationTables,
       "fapStationTable": fapStationTable,
       "fapStationEntry": fapStationEntry,
       "fapStaRadioId": fapStaRadioId,
       "fapStaWlanId": fapStaWlanId,
       "fapStaMacAddr": fapStaMacAddr,
       "fapStaBSSID": fapStaBSSID,
       "fapStaVlanId": fapStaVlanId,
       "fapStaIpAddr": fapStaIpAddr,
       "fapStaSSID": fapStaSSID,
       "fapWagTables": fapWagTables,
       "fapWagTable": fapWagTable,
       "fapWagEntry": fapWagEntry,
       "fapWagTunType": fapWagTunType,
       "fapWagIpAddr": fapWagIpAddr,
       "fapWagPort": fapWagPort,
       "fapWagState": fapWagState,
       "fapWagRxPackets": fapWagRxPackets,
       "fapWagRxBytes": fapWagRxBytes,
       "fapWagRxErrors": fapWagRxErrors,
       "fapWagTxPackets": fapWagTxPackets,
       "fapWagTxBytes": fapWagTxBytes,
       "fapWagTxErrors": fapWagTxErrors,
       "fapWagAliveTime": fapWagAliveTime,
       "fapWagPingInterv": fapWagPingInterv,
       "fapWagPingNum": fapWagPingNum,
       "fapWagDhcpAddr": fapWagDhcpAddr,
       "fapModel": fapModel,
       "fap221e": fap221e,
       "fapu221ev": fapu221ev,
       "faps221e": faps221e,
       "fap222e": fap222e,
       "fap223e": fap223e,
       "fapu223ev": fapu223ev,
       "faps223e": faps223e,
       "fap224e": fap224e,
       "fap231e": fap231e,
       "fap231f": fap231f,
       "fap231g": fap231g,
       "fapu231f": fapu231f,
       "fap233g": fap233g,
       "fap234f": fap234f,
       "fap234g": fap234g,
       "fapu234f": fapu234f,
       "fap23jf": fap23jf,
       "fapu24jev": fapu24jev,
       "fapc24je": fapc24je,
       "fap321e": fap321e,
       "fapu321ev": fapu321ev,
       "fapu323ev": fapu323ev,
       "fap421e": fap421e,
       "fapu421ev": fapu421ev,
       "faps421e": faps421e,
       "fapu422ev": fapu422ev,
       "faps422e": faps422e,
       "fap423e": fap423e,
       "fapu423ev": fapu423ev,
       "faps423e": faps423e,
       "fap431f": fap431f,
       "fap431g": fap431g,
       "fapu431f": fapu431f,
       "fap432f": fap432f,
       "fap432g": fap432g,
       "fapu432f": fapu432f,
       "fap433f": fap433f,
       "fap433g": fap433g,
       "fapu433f": fapu433f,
       "fap831f": fap831f,
       "fap231fl": fap231fl,
       "fap431fl": fap431fl,
       "fap432fr": fap432fr,
       "fap433fl": fap433fl,
       "fapMibConformance": fapMibConformance,
       "fapTrapGroup": fapTrapGroup,
       "fapTrapObjectGroup": fapTrapObjectGroup,
       "fapSysCommGroup": fapSysCommGroup,
       "fapWtpConfGroup": fapWtpConfGroup,
       "fapWtpStatusGroup": fapWtpStatusGroup,
       "fapRadioGroup": fapRadioGroup,
       "fapVapGroup": fapVapGroup,
       "fapWagGroup": fapWagGroup,
       "fapStationGroup": fapStationGroup,
       "fapMibCompliance": fapMibCompliance}
)
