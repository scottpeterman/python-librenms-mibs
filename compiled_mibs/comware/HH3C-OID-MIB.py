# SNMP MIB module (HH3C-OID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-OID-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:40 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3c_ObjectIdentity = ObjectIdentity
hh3c = _Hh3c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506)
)
_Hh3cProductId_ObjectIdentity = ObjectIdentity
hh3cProductId = _Hh3cProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 1)
)
_Hh3cCommon_ObjectIdentity = ObjectIdentity
hh3cCommon = _Hh3cCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2)
)
_Hh3cFtm_ObjectIdentity = ObjectIdentity
hh3cFtm = _Hh3cFtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 1)
)
_Hh3cUIMgt_ObjectIdentity = ObjectIdentity
hh3cUIMgt = _Hh3cUIMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 2)
)
_Hh3cSystemMan_ObjectIdentity = ObjectIdentity
hh3cSystemMan = _Hh3cSystemMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3)
)
_Hh3cConfig_ObjectIdentity = ObjectIdentity
hh3cConfig = _Hh3cConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 4)
)
_Hh3cFlash_ObjectIdentity = ObjectIdentity
hh3cFlash = _Hh3cFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 5)
)
_Hh3cEntityExtend_ObjectIdentity = ObjectIdentity
hh3cEntityExtend = _Hh3cEntityExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 6)
)
_Hh3cIPSecMonitor_ObjectIdentity = ObjectIdentity
hh3cIPSecMonitor = _Hh3cIPSecMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 7)
)
_Hh3cAcl_ObjectIdentity = ObjectIdentity
hh3cAcl = _Hh3cAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8)
)
_Hh3cVoiceVlan_ObjectIdentity = ObjectIdentity
hh3cVoiceVlan = _Hh3cVoiceVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9)
)
_Hh3cL4Redirect_ObjectIdentity = ObjectIdentity
hh3cL4Redirect = _Hh3cL4Redirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 10)
)
_Hh3cIpPBX_ObjectIdentity = ObjectIdentity
hh3cIpPBX = _Hh3cIpPBX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 11)
)
_Hh3cUser_ObjectIdentity = ObjectIdentity
hh3cUser = _Hh3cUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 12)
)
_Hh3cRadius_ObjectIdentity = ObjectIdentity
hh3cRadius = _Hh3cRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 13)
)
_Hh3cPowerEthernetExt_ObjectIdentity = ObjectIdentity
hh3cPowerEthernetExt = _Hh3cPowerEthernetExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14)
)
_Hh3cEntityRelation_ObjectIdentity = ObjectIdentity
hh3cEntityRelation = _Hh3cEntityRelation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 15)
)
_Hh3cProtocolVlan_ObjectIdentity = ObjectIdentity
hh3cProtocolVlan = _Hh3cProtocolVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 16)
)
_Hh3cQosProfile_ObjectIdentity = ObjectIdentity
hh3cQosProfile = _Hh3cQosProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 17)
)
_Hh3cNat_ObjectIdentity = ObjectIdentity
hh3cNat = _Hh3cNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18)
)
_Hh3cPos_ObjectIdentity = ObjectIdentity
hh3cPos = _Hh3cPos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 19)
)
_Hh3cNS_ObjectIdentity = ObjectIdentity
hh3cNS = _Hh3cNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 20)
)
_Hh3cAAL5_ObjectIdentity = ObjectIdentity
hh3cAAL5 = _Hh3cAAL5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21)
)
_Hh3cSSH_ObjectIdentity = ObjectIdentity
hh3cSSH = _Hh3cSSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 22)
)
_Hh3cRSA_ObjectIdentity = ObjectIdentity
hh3cRSA = _Hh3cRSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 23)
)
_Hh3cVrrpExt_ObjectIdentity = ObjectIdentity
hh3cVrrpExt = _Hh3cVrrpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 24)
)
_Hh3cIpa_ObjectIdentity = ObjectIdentity
hh3cIpa = _Hh3cIpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25)
)
_Hh3cPortSecurity_ObjectIdentity = ObjectIdentity
hh3cPortSecurity = _Hh3cPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26)
)
_Hh3cVpls_ObjectIdentity = ObjectIdentity
hh3cVpls = _Hh3cVpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 27)
)
_Hh3cE1_ObjectIdentity = ObjectIdentity
hh3cE1 = _Hh3cE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 28)
)
_Hh3cT1_ObjectIdentity = ObjectIdentity
hh3cT1 = _Hh3cT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 29)
)
_Hh3cIKEMonitor_ObjectIdentity = ObjectIdentity
hh3cIKEMonitor = _Hh3cIKEMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 30)
)
_Hh3cWebSwitch_ObjectIdentity = ObjectIdentity
hh3cWebSwitch = _Hh3cWebSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 31)
)
_Hh3cAutoDetect_ObjectIdentity = ObjectIdentity
hh3cAutoDetect = _Hh3cAutoDetect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 32)
)
_Hh3cIpBroadcast_ObjectIdentity = ObjectIdentity
hh3cIpBroadcast = _Hh3cIpBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 33)
)
_Hh3cIpx_ObjectIdentity = ObjectIdentity
hh3cIpx = _Hh3cIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34)
)
_Hh3cIPS_ObjectIdentity = ObjectIdentity
hh3cIPS = _Hh3cIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 35)
)
_Hh3cDhcpSnoop_ObjectIdentity = ObjectIdentity
hh3cDhcpSnoop = _Hh3cDhcpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36)
)
_Hh3cProtocolPriority_ObjectIdentity = ObjectIdentity
hh3cProtocolPriority = _Hh3cProtocolPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37)
)
_Hh3cTrap_ObjectIdentity = ObjectIdentity
hh3cTrap = _Hh3cTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38)
)
_Hh3cVoice_ObjectIdentity = ObjectIdentity
hh3cVoice = _Hh3cVoice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39)
)
_Hh3cIfExt_ObjectIdentity = ObjectIdentity
hh3cIfExt = _Hh3cIfExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40)
)
_Hh3cCfCard_ObjectIdentity = ObjectIdentity
hh3cCfCard = _Hh3cCfCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 41)
)
_Hh3cEpon_ObjectIdentity = ObjectIdentity
hh3cEpon = _Hh3cEpon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42)
)
_Hh3cDldp_ObjectIdentity = ObjectIdentity
hh3cDldp = _Hh3cDldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 43)
)
_Hh3cUnicast_ObjectIdentity = ObjectIdentity
hh3cUnicast = _Hh3cUnicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 44)
)
_Hh3cRrpp_ObjectIdentity = ObjectIdentity
hh3cRrpp = _Hh3cRrpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 45)
)
_Hh3cDomain_ObjectIdentity = ObjectIdentity
hh3cDomain = _Hh3cDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46)
)
_Hh3cIds_ObjectIdentity = ObjectIdentity
hh3cIds = _Hh3cIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 47)
)
_Hh3cRcr_ObjectIdentity = ObjectIdentity
hh3cRcr = _Hh3cRcr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 48)
)
_Hh3cAtmDxi_ObjectIdentity = ObjectIdentity
hh3cAtmDxi = _Hh3cAtmDxi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49)
)
_Hh3cMulticast_ObjectIdentity = ObjectIdentity
hh3cMulticast = _Hh3cMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 50)
)
_Hh3cMpm_ObjectIdentity = ObjectIdentity
hh3cMpm = _Hh3cMpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 51)
)
_Hh3cOadp_ObjectIdentity = ObjectIdentity
hh3cOadp = _Hh3cOadp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 52)
)
_Hh3cTunnel_ObjectIdentity = ObjectIdentity
hh3cTunnel = _Hh3cTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 53)
)
_Hh3cGre_ObjectIdentity = ObjectIdentity
hh3cGre = _Hh3cGre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 54)
)
_Hh3cObjectInfo_ObjectIdentity = ObjectIdentity
hh3cObjectInfo = _Hh3cObjectInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 55)
)
_Hh3cStorage_ObjectIdentity = ObjectIdentity
hh3cStorage = _Hh3cStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 56)
)
_Hh3cDvpn_ObjectIdentity = ObjectIdentity
hh3cDvpn = _Hh3cDvpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 57)
)
_Hh3cDhcpRelay_ObjectIdentity = ObjectIdentity
hh3cDhcpRelay = _Hh3cDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58)
)
_Hh3cIsis_ObjectIdentity = ObjectIdentity
hh3cIsis = _Hh3cIsis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 59)
)
_Hh3cRpr_ObjectIdentity = ObjectIdentity
hh3cRpr = _Hh3cRpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 60)
)
_Hh3cSubnetVlan_ObjectIdentity = ObjectIdentity
hh3cSubnetVlan = _Hh3cSubnetVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 61)
)
_Hh3cDlswExt_ObjectIdentity = ObjectIdentity
hh3cDlswExt = _Hh3cDlswExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 62)
)
_Hh3cSyslog_ObjectIdentity = ObjectIdentity
hh3cSyslog = _Hh3cSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 63)
)
_Hh3cFlowTemplate_ObjectIdentity = ObjectIdentity
hh3cFlowTemplate = _Hh3cFlowTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 64)
)
_Hh3cQos2_ObjectIdentity = ObjectIdentity
hh3cQos2 = _Hh3cQos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65)
)
_Hh3cIfQos2_ObjectIdentity = ObjectIdentity
hh3cIfQos2 = _Hh3cIfQos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1)
)
_Hh3cCBQos2_ObjectIdentity = ObjectIdentity
hh3cCBQos2 = _Hh3cCBQos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 2)
)
_Hh3cStormConstrain_ObjectIdentity = ObjectIdentity
hh3cStormConstrain = _Hh3cStormConstrain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 66)
)
_Hh3cIpAddrMIB_ObjectIdentity = ObjectIdentity
hh3cIpAddrMIB = _Hh3cIpAddrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67)
)
_Hh3cMirrGroup_ObjectIdentity = ObjectIdentity
hh3cMirrGroup = _Hh3cMirrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 68)
)
_Hh3cQINQ_ObjectIdentity = ObjectIdentity
hh3cQINQ = _Hh3cQINQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 69)
)
_Hh3cTransceiver_ObjectIdentity = ObjectIdentity
hh3cTransceiver = _Hh3cTransceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 70)
)
_Hh3cIpv6AddrMIB_ObjectIdentity = ObjectIdentity
hh3cIpv6AddrMIB = _Hh3cIpv6AddrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 71)
)
_Hh3cBfdMIB_ObjectIdentity = ObjectIdentity
hh3cBfdMIB = _Hh3cBfdMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 72)
)
_Hh3cRCP_ObjectIdentity = ObjectIdentity
hh3cRCP = _Hh3cRCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 73)
)
_Hh3cAcfp_ObjectIdentity = ObjectIdentity
hh3cAcfp = _Hh3cAcfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74)
)
_Hh3cDot11_ObjectIdentity = ObjectIdentity
hh3cDot11 = _Hh3cDot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75)
)
_Hh3cE1T1VI_ObjectIdentity = ObjectIdentity
hh3cE1T1VI = _Hh3cE1T1VI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 76)
)
_Hh3cL2VpnPwe3_ObjectIdentity = ObjectIdentity
hh3cL2VpnPwe3 = _Hh3cL2VpnPwe3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 78)
)
_Hh3cMplsOam_ObjectIdentity = ObjectIdentity
hh3cMplsOam = _Hh3cMplsOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79)
)
_Hh3cMplsOamPs_ObjectIdentity = ObjectIdentity
hh3cMplsOamPs = _Hh3cMplsOamPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80)
)
_Hh3cSiemMib_ObjectIdentity = ObjectIdentity
hh3cSiemMib = _Hh3cSiemMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 81)
)
_Hh3cUps_ObjectIdentity = ObjectIdentity
hh3cUps = _Hh3cUps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 82)
)
_Hh3cEOCCommon_ObjectIdentity = ObjectIdentity
hh3cEOCCommon = _Hh3cEOCCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 83)
)
_Hh3cHPEOC_ObjectIdentity = ObjectIdentity
hh3cHPEOC = _Hh3cHPEOC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84)
)
_Hh3cAFC_ObjectIdentity = ObjectIdentity
hh3cAFC = _Hh3cAFC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 85)
)
_Hh3cMultCDR_ObjectIdentity = ObjectIdentity
hh3cMultCDR = _Hh3cMultCDR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 86)
)
_Hh3cMACInformation_ObjectIdentity = ObjectIdentity
hh3cMACInformation = _Hh3cMACInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 87)
)
_Hh3cFireWall_ObjectIdentity = ObjectIdentity
hh3cFireWall = _Hh3cFireWall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 88)
)
_Hh3cDSP_ObjectIdentity = ObjectIdentity
hh3cDSP = _Hh3cDSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 89)
)
_Hh3cNetMan_ObjectIdentity = ObjectIdentity
hh3cNetMan = _Hh3cNetMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 90)
)
_Hh3cStack_ObjectIdentity = ObjectIdentity
hh3cStack = _Hh3cStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91)
)
_Hh3cPosa_ObjectIdentity = ObjectIdentity
hh3cPosa = _Hh3cPosa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 92)
)
_Hh3cWebAuthentication_ObjectIdentity = ObjectIdentity
hh3cWebAuthentication = _Hh3cWebAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 93)
)
_Hh3cCATVTransceiver_ObjectIdentity = ObjectIdentity
hh3cCATVTransceiver = _Hh3cCATVTransceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 94)
)
_Hh3cLpbkdt_ObjectIdentity = ObjectIdentity
hh3cLpbkdt = _Hh3cLpbkdt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 95)
)
_Hh3cMultiMedia_ObjectIdentity = ObjectIdentity
hh3cMultiMedia = _Hh3cMultiMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 96)
)
_Hh3cDns_ObjectIdentity = ObjectIdentity
hh3cDns = _Hh3cDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 97)
)
_Hh3c3GModem_ObjectIdentity = ObjectIdentity
hh3c3GModem = _Hh3c3GModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98)
)
_Hh3cPortal_ObjectIdentity = ObjectIdentity
hh3cPortal = _Hh3cPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99)
)
_Hh3clldp_ObjectIdentity = ObjectIdentity
hh3clldp = _Hh3clldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100)
)
_Hh3cDHCPServer_ObjectIdentity = ObjectIdentity
hh3cDHCPServer = _Hh3cDHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101)
)
_Hh3cPPPoEServer_ObjectIdentity = ObjectIdentity
hh3cPPPoEServer = _Hh3cPPPoEServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102)
)
_Hh3cL2Isolate_ObjectIdentity = ObjectIdentity
hh3cL2Isolate = _Hh3cL2Isolate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 103)
)
_Hh3cSnmpExt_ObjectIdentity = ObjectIdentity
hh3cSnmpExt = _Hh3cSnmpExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104)
)
_Hh3cVsi_ObjectIdentity = ObjectIdentity
hh3cVsi = _Hh3cVsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 105)
)
_Hh3cEvc_ObjectIdentity = ObjectIdentity
hh3cEvc = _Hh3cEvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106)
)
_Hh3cMinm_ObjectIdentity = ObjectIdentity
hh3cMinm = _Hh3cMinm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107)
)
_Hh3cBlg_ObjectIdentity = ObjectIdentity
hh3cBlg = _Hh3cBlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 108)
)
_Hh3cRS485_ObjectIdentity = ObjectIdentity
hh3cRS485 = _Hh3cRS485_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 109)
)
_Hh3cARPRatelimit_ObjectIdentity = ObjectIdentity
hh3cARPRatelimit = _Hh3cARPRatelimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 110)
)
_Hh3cLI_ObjectIdentity = ObjectIdentity
hh3cLI = _Hh3cLI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 111)
)
_Hh3cDar_ObjectIdentity = ObjectIdentity
hh3cDar = _Hh3cDar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 112)
)
_Hh3cPBR_ObjectIdentity = ObjectIdentity
hh3cPBR = _Hh3cPBR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113)
)
_Hh3cAAANasId_ObjectIdentity = ObjectIdentity
hh3cAAANasId = _Hh3cAAANasId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 114)
)
_Hh3cTeTunnel_ObjectIdentity = ObjectIdentity
hh3cTeTunnel = _Hh3cTeTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 115)
)
_Hh3cLB_ObjectIdentity = ObjectIdentity
hh3cLB = _Hh3cLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 116)
)
_Hh3cDldp2_ObjectIdentity = ObjectIdentity
hh3cDldp2 = _Hh3cDldp2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 117)
)
_Hh3cWIPS_ObjectIdentity = ObjectIdentity
hh3cWIPS = _Hh3cWIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 118)
)
_Hh3cInfoCenter_ObjectIdentity = ObjectIdentity
hh3cInfoCenter = _Hh3cInfoCenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 119)
)
_Hh3cFCoE_ObjectIdentity = ObjectIdentity
hh3cFCoE = _Hh3cFCoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120)
)
_Hh3cTRNG2_ObjectIdentity = ObjectIdentity
hh3cTRNG2 = _Hh3cTRNG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 121)
)
_Hh3cDhcp4_ObjectIdentity = ObjectIdentity
hh3cDhcp4 = _Hh3cDhcp4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 122)
)
_Hh3cMulticastSnoop_ObjectIdentity = ObjectIdentity
hh3cMulticastSnoop = _Hh3cMulticastSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 123)
)
_Hh3cDhcpSnoop2_ObjectIdentity = ObjectIdentity
hh3cDhcpSnoop2 = _Hh3cDhcpSnoop2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124)
)
_Hh3cRmonExt_ObjectIdentity = ObjectIdentity
hh3cRmonExt = _Hh3cRmonExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 125)
)
_Hh3cIPsecMonitorV2_ObjectIdentity = ObjectIdentity
hh3cIPsecMonitorV2 = _Hh3cIPsecMonitorV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 126)
)
_Hh3cSan_ObjectIdentity = ObjectIdentity
hh3cSan = _Hh3cSan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127)
)
_Hh3cSpb_ObjectIdentity = ObjectIdentity
hh3cSpb = _Hh3cSpb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128)
)
_Hh3cPex_ObjectIdentity = ObjectIdentity
hh3cPex = _Hh3cPex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129)
)
_Hh3cSlbg_ObjectIdentity = ObjectIdentity
hh3cSlbg = _Hh3cSlbg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 130)
)
_Hh3cPvst_ObjectIdentity = ObjectIdentity
hh3cPvst = _Hh3cPvst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 131)
)
_Hh3cEvi_ObjectIdentity = ObjectIdentity
hh3cEvi = _Hh3cEvi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 132)
)
_Hh3cIssuUpgrade_ObjectIdentity = ObjectIdentity
hh3cIssuUpgrade = _Hh3cIssuUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 133)
)
_Hh3cEvb_ObjectIdentity = ObjectIdentity
hh3cEvb = _Hh3cEvb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134)
)
_Hh3cFcoeMode_ObjectIdentity = ObjectIdentity
hh3cFcoeMode = _Hh3cFcoeMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 135)
)
_Hh3cMDC_ObjectIdentity = ObjectIdentity
hh3cMDC = _Hh3cMDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136)
)
_Hh3cQinQv2_ObjectIdentity = ObjectIdentity
hh3cQinQv2 = _Hh3cQinQv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 137)
)
_Hh3cVmap_ObjectIdentity = ObjectIdentity
hh3cVmap = _Hh3cVmap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 138)
)
_Hh3cL2tp_ObjectIdentity = ObjectIdentity
hh3cL2tp = _Hh3cL2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 139)
)
_Hh3cMultilinkPPPV2_ObjectIdentity = ObjectIdentity
hh3cMultilinkPPPV2 = _Hh3cMultilinkPPPV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 140)
)
_Hh3cLocAAASrv_ObjectIdentity = ObjectIdentity
hh3cLocAAASrv = _Hh3cLocAAASrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 141)
)
_Hh3cMplsExt_ObjectIdentity = ObjectIdentity
hh3cMplsExt = _Hh3cMplsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 142)
)
_Hh3cMplsTe_ObjectIdentity = ObjectIdentity
hh3cMplsTe = _Hh3cMplsTe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 143)
)
_Hh3cBpa_ObjectIdentity = ObjectIdentity
hh3cBpa = _Hh3cBpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 144)
)
_Hh3cLicense_ObjectIdentity = ObjectIdentity
hh3cLicense = _Hh3cLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 145)
)
_Hh3cARPSourceSuppression_ObjectIdentity = ObjectIdentity
hh3cARPSourceSuppression = _Hh3cARPSourceSuppression_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 146)
)
_Hh3cSmlk_ObjectIdentity = ObjectIdentity
hh3cSmlk = _Hh3cSmlk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 147)
)
_Hh3cLBv2_ObjectIdentity = ObjectIdentity
hh3cLBv2 = _Hh3cLBv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 148)
)
_Hh3cSession_ObjectIdentity = ObjectIdentity
hh3cSession = _Hh3cSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149)
)
_Hh3cVxlan_ObjectIdentity = ObjectIdentity
hh3cVxlan = _Hh3cVxlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 150)
)
_Hh3cRddc_ObjectIdentity = ObjectIdentity
hh3cRddc = _Hh3cRddc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 151)
)
_Hh3cIpRanDcn_ObjectIdentity = ObjectIdentity
hh3cIpRanDcn = _Hh3cIpRanDcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 152)
)
_Hh3c8021XExt2_ObjectIdentity = ObjectIdentity
hh3c8021XExt2 = _Hh3c8021XExt2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 153)
)
_Hh3cContext_ObjectIdentity = ObjectIdentity
hh3cContext = _Hh3cContext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 154)
)
_Hh3cObjp_ObjectIdentity = ObjectIdentity
hh3cObjp = _Hh3cObjp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 155)
)
_Hh3cNvgre_ObjectIdentity = ObjectIdentity
hh3cNvgre = _Hh3cNvgre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 156)
)
_Hh3cWlanMt_ObjectIdentity = ObjectIdentity
hh3cWlanMt = _Hh3cWlanMt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 157)
)
_Hh3cRbac_ObjectIdentity = ObjectIdentity
hh3cRbac = _Hh3cRbac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 158)
)
_Hh3cDHCP6Server_ObjectIdentity = ObjectIdentity
hh3cDHCP6Server = _Hh3cDHCP6Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 159)
)
_Hh3cMplsVpnBgp_ObjectIdentity = ObjectIdentity
hh3cMplsVpnBgp = _Hh3cMplsVpnBgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 160)
)
_Hh3cOspf_ObjectIdentity = ObjectIdentity
hh3cOspf = _Hh3cOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 161)
)
_Hh3cL2vpn_ObjectIdentity = ObjectIdentity
hh3cL2vpn = _Hh3cL2vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 162)
)
_Hh3cEntityVendorTypeOID_ObjectIdentity = ObjectIdentity
hh3cEntityVendorTypeOID = _Hh3cEntityVendorTypeOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 3)
)
_Hh3cNM_ObjectIdentity = ObjectIdentity
hh3cNM = _Hh3cNM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 4)
)
_Hh3cSystem_ObjectIdentity = ObjectIdentity
hh3cSystem = _Hh3cSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 6)
)
_Hh3cSNMPAgCpb_ObjectIdentity = ObjectIdentity
hh3cSNMPAgCpb = _Hh3cSNMPAgCpb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 7)
)
_Hh3cQosCapability_ObjectIdentity = ObjectIdentity
hh3cQosCapability = _Hh3cQosCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1)
)
_Hh3cRhw_ObjectIdentity = ObjectIdentity
hh3cRhw = _Hh3cRhw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8)
)
_Hh3cDHCPRelayMib_ObjectIdentity = ObjectIdentity
hh3cDHCPRelayMib = _Hh3cDHCPRelayMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 1)
)
_Hh3cDHCPServerMib_ObjectIdentity = ObjectIdentity
hh3cDHCPServerMib = _Hh3cDHCPServerMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2)
)
_Hh3cNqa_ObjectIdentity = ObjectIdentity
hh3cNqa = _Hh3cNqa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 3)
)
_Hh3crmonExtend_ObjectIdentity = ObjectIdentity
hh3crmonExtend = _Hh3crmonExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4)
)
_Hh3cpaeExtMib_ObjectIdentity = ObjectIdentity
hh3cpaeExtMib = _Hh3cpaeExtMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 6)
)
_Hh3cHgmp_ObjectIdentity = ObjectIdentity
hh3cHgmp = _Hh3cHgmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 7)
)
_Hh3cDevice_ObjectIdentity = ObjectIdentity
hh3cDevice = _Hh3cDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 8)
)
_Hh3cMpls_ObjectIdentity = ObjectIdentity
hh3cMpls = _Hh3cMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12)
)
_Hh3cMplsLsr_ObjectIdentity = ObjectIdentity
hh3cMplsLsr = _Hh3cMplsLsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 1)
)
_Hh3cMplsLdp_ObjectIdentity = ObjectIdentity
hh3cMplsLdp = _Hh3cMplsLdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 2)
)
_Hh3cMplsVpn_ObjectIdentity = ObjectIdentity
hh3cMplsVpn = _Hh3cMplsVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 12, 3)
)
_Hh3cTRNG_ObjectIdentity = ObjectIdentity
hh3cTRNG = _Hh3cTRNG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 13)
)
_Hh3cUserLogMIB_ObjectIdentity = ObjectIdentity
hh3cUserLogMIB = _Hh3cUserLogMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 18)
)
_Hh3cNTP_ObjectIdentity = ObjectIdentity
hh3cNTP = _Hh3cNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22)
)
_Hh3cLAG_ObjectIdentity = ObjectIdentity
hh3cLAG = _Hh3cLAG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25)
)
_Hh3cSmonExtend_ObjectIdentity = ObjectIdentity
hh3cSmonExtend = _Hh3cSmonExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 26)
)
_Hh3cQoS_ObjectIdentity = ObjectIdentity
hh3cQoS = _Hh3cQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 32)
)
_Hh3cMultilinkPPP_ObjectIdentity = ObjectIdentity
hh3cMultilinkPPP = _Hh3cMultilinkPPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 33)
)
_Hh3clswCommon_ObjectIdentity = ObjectIdentity
hh3clswCommon = _Hh3clswCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35)
)
_Hh3cLswExtInterface_ObjectIdentity = ObjectIdentity
hh3cLswExtInterface = _Hh3cLswExtInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1)
)
_Hh3cLswVlan_ObjectIdentity = ObjectIdentity
hh3cLswVlan = _Hh3cLswVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2)
)
_Hh3cLswMacPort_ObjectIdentity = ObjectIdentity
hh3cLswMacPort = _Hh3cLswMacPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3)
)
_Hh3cLswArpMib_ObjectIdentity = ObjectIdentity
hh3cLswArpMib = _Hh3cLswArpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 4)
)
_Hh3cLswL2InfMib_ObjectIdentity = ObjectIdentity
hh3cLswL2InfMib = _Hh3cLswL2InfMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5)
)
_Hh3cLswRstpMib_ObjectIdentity = ObjectIdentity
hh3cLswRstpMib = _Hh3cLswRstpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6)
)
_Hh3cLswIgmpsnoopingMib_ObjectIdentity = ObjectIdentity
hh3cLswIgmpsnoopingMib = _Hh3cLswIgmpsnoopingMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 7)
)
_Hh3cLswDhcpMib_ObjectIdentity = ObjectIdentity
hh3cLswDhcpMib = _Hh3cLswDhcpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8)
)
_Hh3cLswdevMMib_ObjectIdentity = ObjectIdentity
hh3cLswdevMMib = _Hh3cLswdevMMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 9)
)
_Hh3cLswTrapMib_ObjectIdentity = ObjectIdentity
hh3cLswTrapMib = _Hh3cLswTrapMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12)
)
_Hh3cdot1sMstp_ObjectIdentity = ObjectIdentity
hh3cdot1sMstp = _Hh3cdot1sMstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14)
)
_Hh3cLswQosAclMib_ObjectIdentity = ObjectIdentity
hh3cLswQosAclMib = _Hh3cLswQosAclMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16)
)
_Hh3cLswMix_ObjectIdentity = ObjectIdentity
hh3cLswMix = _Hh3cLswMix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 17)
)
_Hh3cLswDeviceAdmin_ObjectIdentity = ObjectIdentity
hh3cLswDeviceAdmin = _Hh3cLswDeviceAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 18)
)
_Hh3cmlsr_ObjectIdentity = ObjectIdentity
hh3cmlsr = _Hh3cmlsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36)
)
_Hh3cNDEC_ObjectIdentity = ObjectIdentity
hh3cNDEC = _Hh3cNDEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 2)
)
_Hh3credundancyPower_ObjectIdentity = ObjectIdentity
hh3credundancyPower = _Hh3credundancyPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 4)
)
_Hh3credundancyFan_ObjectIdentity = ObjectIdentity
hh3credundancyFan = _Hh3credundancyFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 5)
)
_Hh3cpos_ObjectIdentity = ObjectIdentity
hh3cpos = _Hh3cpos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8)
)
_Hh3cIsdnMib_ObjectIdentity = ObjectIdentity
hh3cIsdnMib = _Hh3cIsdnMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 9)
)
_Hh3cdlsw_ObjectIdentity = ObjectIdentity
hh3cdlsw = _Hh3cdlsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37)
)
_Hh3cSurveillanceMIB_ObjectIdentity = ObjectIdentity
hh3cSurveillanceMIB = _Hh3cSurveillanceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9)
)
_Hh3cVMMan_ObjectIdentity = ObjectIdentity
hh3cVMMan = _Hh3cVMMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1)
)
_Hh3cPUMan_ObjectIdentity = ObjectIdentity
hh3cPUMan = _Hh3cPUMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2)
)
_Hh3cMSMan_ObjectIdentity = ObjectIdentity
hh3cMSMan = _Hh3cMSMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 3)
)
_Hh3cStorageRef_ObjectIdentity = ObjectIdentity
hh3cStorageRef = _Hh3cStorageRef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10)
)
_Hh3cStorageMIB_ObjectIdentity = ObjectIdentity
hh3cStorageMIB = _Hh3cStorageMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 1)
)
_Hh3cStorageSnap_ObjectIdentity = ObjectIdentity
hh3cStorageSnap = _Hh3cStorageSnap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 2)
)
_Hh3cDisk_ObjectIdentity = ObjectIdentity
hh3cDisk = _Hh3cDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 3)
)
_Hh3cRaid_ObjectIdentity = ObjectIdentity
hh3cRaid = _Hh3cRaid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 4)
)
_Hh3cLogicVolume_ObjectIdentity = ObjectIdentity
hh3cLogicVolume = _Hh3cLogicVolume_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 10, 5)
)
_HpNetworking_ObjectIdentity = ObjectIdentity
hpNetworking = _HpNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 11)
)
_Hh3cJointMibs_ObjectIdentity = ObjectIdentity
hh3cJointMibs = _Hh3cJointMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-OID-MIB",
    **{"hh3c": hh3c,
       "hh3cProductId": hh3cProductId,
       "hh3cCommon": hh3cCommon,
       "hh3cFtm": hh3cFtm,
       "hh3cUIMgt": hh3cUIMgt,
       "hh3cSystemMan": hh3cSystemMan,
       "hh3cConfig": hh3cConfig,
       "hh3cFlash": hh3cFlash,
       "hh3cEntityExtend": hh3cEntityExtend,
       "hh3cIPSecMonitor": hh3cIPSecMonitor,
       "hh3cAcl": hh3cAcl,
       "hh3cVoiceVlan": hh3cVoiceVlan,
       "hh3cL4Redirect": hh3cL4Redirect,
       "hh3cIpPBX": hh3cIpPBX,
       "hh3cUser": hh3cUser,
       "hh3cRadius": hh3cRadius,
       "hh3cPowerEthernetExt": hh3cPowerEthernetExt,
       "hh3cEntityRelation": hh3cEntityRelation,
       "hh3cProtocolVlan": hh3cProtocolVlan,
       "hh3cQosProfile": hh3cQosProfile,
       "hh3cNat": hh3cNat,
       "hh3cPos": hh3cPos,
       "hh3cNS": hh3cNS,
       "hh3cAAL5": hh3cAAL5,
       "hh3cSSH": hh3cSSH,
       "hh3cRSA": hh3cRSA,
       "hh3cVrrpExt": hh3cVrrpExt,
       "hh3cIpa": hh3cIpa,
       "hh3cPortSecurity": hh3cPortSecurity,
       "hh3cVpls": hh3cVpls,
       "hh3cE1": hh3cE1,
       "hh3cT1": hh3cT1,
       "hh3cIKEMonitor": hh3cIKEMonitor,
       "hh3cWebSwitch": hh3cWebSwitch,
       "hh3cAutoDetect": hh3cAutoDetect,
       "hh3cIpBroadcast": hh3cIpBroadcast,
       "hh3cIpx": hh3cIpx,
       "hh3cIPS": hh3cIPS,
       "hh3cDhcpSnoop": hh3cDhcpSnoop,
       "hh3cProtocolPriority": hh3cProtocolPriority,
       "hh3cTrap": hh3cTrap,
       "hh3cVoice": hh3cVoice,
       "hh3cIfExt": hh3cIfExt,
       "hh3cCfCard": hh3cCfCard,
       "hh3cEpon": hh3cEpon,
       "hh3cDldp": hh3cDldp,
       "hh3cUnicast": hh3cUnicast,
       "hh3cRrpp": hh3cRrpp,
       "hh3cDomain": hh3cDomain,
       "hh3cIds": hh3cIds,
       "hh3cRcr": hh3cRcr,
       "hh3cAtmDxi": hh3cAtmDxi,
       "hh3cMulticast": hh3cMulticast,
       "hh3cMpm": hh3cMpm,
       "hh3cOadp": hh3cOadp,
       "hh3cTunnel": hh3cTunnel,
       "hh3cGre": hh3cGre,
       "hh3cObjectInfo": hh3cObjectInfo,
       "hh3cStorage": hh3cStorage,
       "hh3cDvpn": hh3cDvpn,
       "hh3cDhcpRelay": hh3cDhcpRelay,
       "hh3cIsis": hh3cIsis,
       "hh3cRpr": hh3cRpr,
       "hh3cSubnetVlan": hh3cSubnetVlan,
       "hh3cDlswExt": hh3cDlswExt,
       "hh3cSyslog": hh3cSyslog,
       "hh3cFlowTemplate": hh3cFlowTemplate,
       "hh3cQos2": hh3cQos2,
       "hh3cIfQos2": hh3cIfQos2,
       "hh3cCBQos2": hh3cCBQos2,
       "hh3cStormConstrain": hh3cStormConstrain,
       "hh3cIpAddrMIB": hh3cIpAddrMIB,
       "hh3cMirrGroup": hh3cMirrGroup,
       "hh3cQINQ": hh3cQINQ,
       "hh3cTransceiver": hh3cTransceiver,
       "hh3cIpv6AddrMIB": hh3cIpv6AddrMIB,
       "hh3cBfdMIB": hh3cBfdMIB,
       "hh3cRCP": hh3cRCP,
       "hh3cAcfp": hh3cAcfp,
       "hh3cDot11": hh3cDot11,
       "hh3cE1T1VI": hh3cE1T1VI,
       "hh3cL2VpnPwe3": hh3cL2VpnPwe3,
       "hh3cMplsOam": hh3cMplsOam,
       "hh3cMplsOamPs": hh3cMplsOamPs,
       "hh3cSiemMib": hh3cSiemMib,
       "hh3cUps": hh3cUps,
       "hh3cEOCCommon": hh3cEOCCommon,
       "hh3cHPEOC": hh3cHPEOC,
       "hh3cAFC": hh3cAFC,
       "hh3cMultCDR": hh3cMultCDR,
       "hh3cMACInformation": hh3cMACInformation,
       "hh3cFireWall": hh3cFireWall,
       "hh3cDSP": hh3cDSP,
       "hh3cNetMan": hh3cNetMan,
       "hh3cStack": hh3cStack,
       "hh3cPosa": hh3cPosa,
       "hh3cWebAuthentication": hh3cWebAuthentication,
       "hh3cCATVTransceiver": hh3cCATVTransceiver,
       "hh3cLpbkdt": hh3cLpbkdt,
       "hh3cMultiMedia": hh3cMultiMedia,
       "hh3cDns": hh3cDns,
       "hh3c3GModem": hh3c3GModem,
       "hh3cPortal": hh3cPortal,
       "hh3clldp": hh3clldp,
       "hh3cDHCPServer": hh3cDHCPServer,
       "hh3cPPPoEServer": hh3cPPPoEServer,
       "hh3cL2Isolate": hh3cL2Isolate,
       "hh3cSnmpExt": hh3cSnmpExt,
       "hh3cVsi": hh3cVsi,
       "hh3cEvc": hh3cEvc,
       "hh3cMinm": hh3cMinm,
       "hh3cBlg": hh3cBlg,
       "hh3cRS485": hh3cRS485,
       "hh3cARPRatelimit": hh3cARPRatelimit,
       "hh3cLI": hh3cLI,
       "hh3cDar": hh3cDar,
       "hh3cPBR": hh3cPBR,
       "hh3cAAANasId": hh3cAAANasId,
       "hh3cTeTunnel": hh3cTeTunnel,
       "hh3cLB": hh3cLB,
       "hh3cDldp2": hh3cDldp2,
       "hh3cWIPS": hh3cWIPS,
       "hh3cInfoCenter": hh3cInfoCenter,
       "hh3cFCoE": hh3cFCoE,
       "hh3cTRNG2": hh3cTRNG2,
       "hh3cDhcp4": hh3cDhcp4,
       "hh3cMulticastSnoop": hh3cMulticastSnoop,
       "hh3cDhcpSnoop2": hh3cDhcpSnoop2,
       "hh3cRmonExt": hh3cRmonExt,
       "hh3cIPsecMonitorV2": hh3cIPsecMonitorV2,
       "hh3cSan": hh3cSan,
       "hh3cSpb": hh3cSpb,
       "hh3cPex": hh3cPex,
       "hh3cSlbg": hh3cSlbg,
       "hh3cPvst": hh3cPvst,
       "hh3cEvi": hh3cEvi,
       "hh3cIssuUpgrade": hh3cIssuUpgrade,
       "hh3cEvb": hh3cEvb,
       "hh3cFcoeMode": hh3cFcoeMode,
       "hh3cMDC": hh3cMDC,
       "hh3cQinQv2": hh3cQinQv2,
       "hh3cVmap": hh3cVmap,
       "hh3cL2tp": hh3cL2tp,
       "hh3cMultilinkPPPV2": hh3cMultilinkPPPV2,
       "hh3cLocAAASrv": hh3cLocAAASrv,
       "hh3cMplsExt": hh3cMplsExt,
       "hh3cMplsTe": hh3cMplsTe,
       "hh3cBpa": hh3cBpa,
       "hh3cLicense": hh3cLicense,
       "hh3cARPSourceSuppression": hh3cARPSourceSuppression,
       "hh3cSmlk": hh3cSmlk,
       "hh3cLBv2": hh3cLBv2,
       "hh3cSession": hh3cSession,
       "hh3cVxlan": hh3cVxlan,
       "hh3cRddc": hh3cRddc,
       "hh3cIpRanDcn": hh3cIpRanDcn,
       "hh3c8021XExt2": hh3c8021XExt2,
       "hh3cContext": hh3cContext,
       "hh3cObjp": hh3cObjp,
       "hh3cNvgre": hh3cNvgre,
       "hh3cWlanMt": hh3cWlanMt,
       "hh3cRbac": hh3cRbac,
       "hh3cDHCP6Server": hh3cDHCP6Server,
       "hh3cMplsVpnBgp": hh3cMplsVpnBgp,
       "hh3cOspf": hh3cOspf,
       "hh3cL2vpn": hh3cL2vpn,
       "hh3cEntityVendorTypeOID": hh3cEntityVendorTypeOID,
       "hh3cNM": hh3cNM,
       "hh3cSystem": hh3cSystem,
       "hh3cSNMPAgCpb": hh3cSNMPAgCpb,
       "hh3cQosCapability": hh3cQosCapability,
       "hh3cRhw": hh3cRhw,
       "hh3cDHCPRelayMib": hh3cDHCPRelayMib,
       "hh3cDHCPServerMib": hh3cDHCPServerMib,
       "hh3cNqa": hh3cNqa,
       "hh3crmonExtend": hh3crmonExtend,
       "hh3cpaeExtMib": hh3cpaeExtMib,
       "hh3cHgmp": hh3cHgmp,
       "hh3cDevice": hh3cDevice,
       "hh3cMpls": hh3cMpls,
       "hh3cMplsLsr": hh3cMplsLsr,
       "hh3cMplsLdp": hh3cMplsLdp,
       "hh3cMplsVpn": hh3cMplsVpn,
       "hh3cTRNG": hh3cTRNG,
       "hh3cUserLogMIB": hh3cUserLogMIB,
       "hh3cNTP": hh3cNTP,
       "hh3cLAG": hh3cLAG,
       "hh3cSmonExtend": hh3cSmonExtend,
       "hh3cQoS": hh3cQoS,
       "hh3cMultilinkPPP": hh3cMultilinkPPP,
       "hh3clswCommon": hh3clswCommon,
       "hh3cLswExtInterface": hh3cLswExtInterface,
       "hh3cLswVlan": hh3cLswVlan,
       "hh3cLswMacPort": hh3cLswMacPort,
       "hh3cLswArpMib": hh3cLswArpMib,
       "hh3cLswL2InfMib": hh3cLswL2InfMib,
       "hh3cLswRstpMib": hh3cLswRstpMib,
       "hh3cLswIgmpsnoopingMib": hh3cLswIgmpsnoopingMib,
       "hh3cLswDhcpMib": hh3cLswDhcpMib,
       "hh3cLswdevMMib": hh3cLswdevMMib,
       "hh3cLswTrapMib": hh3cLswTrapMib,
       "hh3cdot1sMstp": hh3cdot1sMstp,
       "hh3cLswQosAclMib": hh3cLswQosAclMib,
       "hh3cLswMix": hh3cLswMix,
       "hh3cLswDeviceAdmin": hh3cLswDeviceAdmin,
       "hh3cmlsr": hh3cmlsr,
       "hh3cNDEC": hh3cNDEC,
       "hh3credundancyPower": hh3credundancyPower,
       "hh3credundancyFan": hh3credundancyFan,
       "hh3cpos": hh3cpos,
       "hh3cIsdnMib": hh3cIsdnMib,
       "hh3cdlsw": hh3cdlsw,
       "hh3cSurveillanceMIB": hh3cSurveillanceMIB,
       "hh3cVMMan": hh3cVMMan,
       "hh3cPUMan": hh3cPUMan,
       "hh3cMSMan": hh3cMSMan,
       "hh3cStorageRef": hh3cStorageRef,
       "hh3cStorageMIB": hh3cStorageMIB,
       "hh3cStorageSnap": hh3cStorageSnap,
       "hh3cDisk": hh3cDisk,
       "hh3cRaid": hh3cRaid,
       "hh3cLogicVolume": hh3cLogicVolume,
       "hpNetworking": hpNetworking,
       "hh3cJointMibs": hh3cJointMibs}
)
