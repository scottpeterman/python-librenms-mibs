# SNMP MIB module (TELDAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\teldat\TELDAT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:57 2025
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
 Opaque,
 NotificationType,
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
    "Opaque",
    "NotificationType",
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

_Teldat_ObjectIdentity = ObjectIdentity
teldat = _Teldat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007)
)
_Teladmin_ObjectIdentity = ObjectIdentity
teladmin = _Teladmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1)
)
_Telobjid_ObjectIdentity = ObjectIdentity
telobjid = _Telobjid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1)
)
_TeldatSreTrap_ObjectIdentity = ObjectIdentity
teldatSreTrap = _TeldatSreTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1)
)
_TeldatSreTrap_GW_ObjectIdentity = ObjectIdentity
teldatSreTrap_GW = _TeldatSreTrap_GW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 1)
)
_TeldatSreTrap_FLT_ObjectIdentity = ObjectIdentity
teldatSreTrap_FLT = _TeldatSreTrap_FLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 2)
)
_TeldatSreTrap_BRS_ObjectIdentity = ObjectIdentity
teldatSreTrap_BRS = _TeldatSreTrap_BRS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 3)
)
_TeldatSreTrap_ARP_ObjectIdentity = ObjectIdentity
teldatSreTrap_ARP = _TeldatSreTrap_ARP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 5)
)
_TeldatSreTrap_IP_ObjectIdentity = ObjectIdentity
teldatSreTrap_IP = _TeldatSreTrap_IP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 10)
)
_TeldatSreTrap_ICMP_ObjectIdentity = ObjectIdentity
teldatSreTrap_ICMP = _TeldatSreTrap_ICMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 11)
)
_TeldatSreTrap_TCP_ObjectIdentity = ObjectIdentity
teldatSreTrap_TCP = _TeldatSreTrap_TCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 12)
)
_TeldatSreTrap_UDP_ObjectIdentity = ObjectIdentity
teldatSreTrap_UDP = _TeldatSreTrap_UDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 13)
)
_TeldatSreTrap_ORIP_ObjectIdentity = ObjectIdentity
teldatSreTrap_ORIP = _TeldatSreTrap_ORIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 15)
)
_TeldatSreTrap_SPF_ObjectIdentity = ObjectIdentity
teldatSreTrap_SPF = _TeldatSreTrap_SPF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 17)
)
_TeldatSreTrap_TFTP_ObjectIdentity = ObjectIdentity
teldatSreTrap_TFTP = _TeldatSreTrap_TFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 19)
)
_TeldatSreTrap_SNMP_ObjectIdentity = ObjectIdentity
teldatSreTrap_SNMP = _TeldatSreTrap_SNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 21)
)
_TeldatSreTrap_SRT_ObjectIdentity = ObjectIdentity
teldatSreTrap_SRT = _TeldatSreTrap_SRT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 72)
)
_TeldatSreTrap_BR_ObjectIdentity = ObjectIdentity
teldatSreTrap_BR = _TeldatSreTrap_BR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 74)
)
_TeldatSreTrap_FTP_ObjectIdentity = ObjectIdentity
teldatSreTrap_FTP = _TeldatSreTrap_FTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 80)
)
_TeldatSreTrap_ETH_ObjectIdentity = ObjectIdentity
teldatSreTrap_ETH = _TeldatSreTrap_ETH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 81)
)
_TeldatSreTrap_SL_ObjectIdentity = ObjectIdentity
teldatSreTrap_SL = _TeldatSreTrap_SL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 83)
)
_TeldatSreTrap_TKR_ObjectIdentity = ObjectIdentity
teldatSreTrap_TKR = _TeldatSreTrap_TKR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 84)
)
_TeldatSreTrap_SDLC_ObjectIdentity = ObjectIdentity
teldatSreTrap_SDLC = _TeldatSreTrap_SDLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 90)
)
_TeldatSreTrap_FR_ObjectIdentity = ObjectIdentity
teldatSreTrap_FR = _TeldatSreTrap_FR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 92)
)
_TeldatSreTrap_PPP_ObjectIdentity = ObjectIdentity
teldatSreTrap_PPP = _TeldatSreTrap_PPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 95)
)
_TeldatSreTrap_X252_ObjectIdentity = ObjectIdentity
teldatSreTrap_X252 = _TeldatSreTrap_X252_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 97)
)
_TeldatSreTrap_X253_ObjectIdentity = ObjectIdentity
teldatSreTrap_X253 = _TeldatSreTrap_X253_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 98)
)
_TeldatSreTrap_RDSI_ObjectIdentity = ObjectIdentity
teldatSreTrap_RDSI = _TeldatSreTrap_RDSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 99)
)
_TeldatSreTrap_LLC_ObjectIdentity = ObjectIdentity
teldatSreTrap_LLC = _TeldatSreTrap_LLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 103)
)
_TeldatSreTrap_BAN_ObjectIdentity = ObjectIdentity
teldatSreTrap_BAN = _TeldatSreTrap_BAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 109)
)
_TeldatSreTrap_NBS_ObjectIdentity = ObjectIdentity
teldatSreTrap_NBS = _TeldatSreTrap_NBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 110)
)
_TeldatSreTrap_CIF_ObjectIdentity = ObjectIdentity
teldatSreTrap_CIF = _TeldatSreTrap_CIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 111)
)
_TeldatSreTrap_GSTP_ObjectIdentity = ObjectIdentity
teldatSreTrap_GSTP = _TeldatSreTrap_GSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 112)
)
_TeldatSreTrap_FRBK_ObjectIdentity = ObjectIdentity
teldatSreTrap_FRBK = _TeldatSreTrap_FRBK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 114)
)
_TeldatSreTrap_PRI_ObjectIdentity = ObjectIdentity
teldatSreTrap_PRI = _TeldatSreTrap_PRI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 115)
)
_TeldatSreTrap_DLS_ObjectIdentity = ObjectIdentity
teldatSreTrap_DLS = _TeldatSreTrap_DLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 116)
)
_TeldatSreTrap_PCMC_ObjectIdentity = ObjectIdentity
teldatSreTrap_PCMC = _TeldatSreTrap_PCMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 118)
)
_TeldatSreTrap_LAPD_ObjectIdentity = ObjectIdentity
teldatSreTrap_LAPD = _TeldatSreTrap_LAPD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 119)
)
_TeldatSreTrap_TNIP_ObjectIdentity = ObjectIdentity
teldatSreTrap_TNIP = _TeldatSreTrap_TNIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 120)
)
_TeldatSreTrap_MBBU_ObjectIdentity = ObjectIdentity
teldatSreTrap_MBBU = _TeldatSreTrap_MBBU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 123)
)
_TeldatSreTrap_BIR64_ObjectIdentity = ObjectIdentity
teldatSreTrap_BIR64 = _TeldatSreTrap_BIR64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 124)
)
_TeldatSreTrap_REXISMRU_ObjectIdentity = ObjectIdentity
teldatSreTrap_REXISMRU = _TeldatSreTrap_REXISMRU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 125)
)
_TeldatSreTrap_REXISFT_ObjectIdentity = ObjectIdentity
teldatSreTrap_REXISFT = _TeldatSreTrap_REXISFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 126)
)
_TeldatSreTrap_ICUPLUS_ObjectIdentity = ObjectIdentity
teldatSreTrap_ICUPLUS = _TeldatSreTrap_ICUPLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 127)
)
_TeldatSreTrap_Q933_ObjectIdentity = ObjectIdentity
teldatSreTrap_Q933 = _TeldatSreTrap_Q933_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 128)
)
_TeldatSreTrap_IPPN_ObjectIdentity = ObjectIdentity
teldatSreTrap_IPPN = _TeldatSreTrap_IPPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 129)
)
_TeldatSreTrap_RAD_ObjectIdentity = ObjectIdentity
teldatSreTrap_RAD = _TeldatSreTrap_RAD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 130)
)
_TeldatSreTrap_H323_ObjectIdentity = ObjectIdentity
teldatSreTrap_H323 = _TeldatSreTrap_H323_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 131)
)
_TeldatSreTrap_DHCP_ObjectIdentity = ObjectIdentity
teldatSreTrap_DHCP = _TeldatSreTrap_DHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 133)
)
_TeldatSreTrap_IP6_ObjectIdentity = ObjectIdentity
teldatSreTrap_IP6 = _TeldatSreTrap_IP6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 134)
)
_TeldatSreTrap_TVRP_ObjectIdentity = ObjectIdentity
teldatSreTrap_TVRP = _TeldatSreTrap_TVRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 135)
)
_TeldatSreTrap_ATM_ObjectIdentity = ObjectIdentity
teldatSreTrap_ATM = _TeldatSreTrap_ATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 136)
)
_TeldatSreTrap_IPSEC_ObjectIdentity = ObjectIdentity
teldatSreTrap_IPSEC = _TeldatSreTrap_IPSEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 138)
)
_TeldatSreTrap_NTP_ObjectIdentity = ObjectIdentity
teldatSreTrap_NTP = _TeldatSreTrap_NTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 139)
)
_TeldatSreTrap_ADSL_ObjectIdentity = ObjectIdentity
teldatSreTrap_ADSL = _TeldatSreTrap_ADSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 140)
)
_TeldatSreTrap_HTTP_ObjectIdentity = ObjectIdentity
teldatSreTrap_HTTP = _TeldatSreTrap_HTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 142)
)
_TeldatSreTrap_DEP_ObjectIdentity = ObjectIdentity
teldatSreTrap_DEP = _TeldatSreTrap_DEP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 144)
)
_TeldatSreTrap_ASDP_ObjectIdentity = ObjectIdentity
teldatSreTrap_ASDP = _TeldatSreTrap_ASDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 145)
)
_TeldatSreTrap_LDAP_ObjectIdentity = ObjectIdentity
teldatSreTrap_LDAP = _TeldatSreTrap_LDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 146)
)
_TeldatSreTrap_SCEP_ObjectIdentity = ObjectIdentity
teldatSreTrap_SCEP = _TeldatSreTrap_SCEP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 147)
)
_TeldatSreTrap_P3OE_ObjectIdentity = ObjectIdentity
teldatSreTrap_P3OE = _TeldatSreTrap_P3OE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 148)
)
_TeldatSreTrap_AT_ObjectIdentity = ObjectIdentity
teldatSreTrap_AT = _TeldatSreTrap_AT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 149)
)
_TeldatSreTrap_ASYNC_ObjectIdentity = ObjectIdentity
teldatSreTrap_ASYNC = _TeldatSreTrap_ASYNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 150)
)
_TeldatSreTrap_SYNC_ObjectIdentity = ObjectIdentity
teldatSreTrap_SYNC = _TeldatSreTrap_SYNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 151)
)
_TeldatSreTrap_DNS_ObjectIdentity = ObjectIdentity
teldatSreTrap_DNS = _TeldatSreTrap_DNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 152)
)
_TeldatSreTrap_VSN_ObjectIdentity = ObjectIdentity
teldatSreTrap_VSN = _TeldatSreTrap_VSN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 153)
)
_TeldatSreTrap_NAPT_ObjectIdentity = ObjectIdentity
teldatSreTrap_NAPT = _TeldatSreTrap_NAPT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 154)
)
_TeldatSreTrap_VID_ObjectIdentity = ObjectIdentity
teldatSreTrap_VID = _TeldatSreTrap_VID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 155)
)
_TeldatSreTrap_PRL_ObjectIdentity = ObjectIdentity
teldatSreTrap_PRL = _TeldatSreTrap_PRL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 156)
)
_TeldatSreTrap_HDSL_ObjectIdentity = ObjectIdentity
teldatSreTrap_HDSL = _TeldatSreTrap_HDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 157)
)
_TeldatSreTrap_PGMO_ObjectIdentity = ObjectIdentity
teldatSreTrap_PGMO = _TeldatSreTrap_PGMO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 158)
)
_TeldatSreTrap_RTSP_ObjectIdentity = ObjectIdentity
teldatSreTrap_RTSP = _TeldatSreTrap_RTSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 159)
)
_TeldatSreTrap_DNAT_ObjectIdentity = ObjectIdentity
teldatSreTrap_DNAT = _TeldatSreTrap_DNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 160)
)
_TeldatSreTrap_G703_ObjectIdentity = ObjectIdentity
teldatSreTrap_G703 = _TeldatSreTrap_G703_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 161)
)
_TeldatSreTrap_POLR_ObjectIdentity = ObjectIdentity
teldatSreTrap_POLR = _TeldatSreTrap_POLR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 162)
)
_TeldatSreTrap_XN_ObjectIdentity = ObjectIdentity
teldatSreTrap_XN = _TeldatSreTrap_XN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 163)
)
_TeldatSreTrap_XNS_ObjectIdentity = ObjectIdentity
teldatSreTrap_XNS = _TeldatSreTrap_XNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 164)
)
_TeldatSreTrap_IPX_ObjectIdentity = ObjectIdentity
teldatSreTrap_IPX = _TeldatSreTrap_IPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 165)
)
_TeldatSreTrap_IGMP_ObjectIdentity = ObjectIdentity
teldatSreTrap_IGMP = _TeldatSreTrap_IGMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 166)
)
_TeldatSreTrap_AINST_ObjectIdentity = ObjectIdentity
teldatSreTrap_AINST = _TeldatSreTrap_AINST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 167)
)
_TeldatSreTrap_BGP_ObjectIdentity = ObjectIdentity
teldatSreTrap_BGP = _TeldatSreTrap_BGP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 169)
)
_TeldatSreTrap_NSM_ObjectIdentity = ObjectIdentity
teldatSreTrap_NSM = _TeldatSreTrap_NSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 170)
)
_TeldatSreTrap_TLNT_ObjectIdentity = ObjectIdentity
teldatSreTrap_TLNT = _TeldatSreTrap_TLNT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 171)
)
_TeldatSreTrap_L2TP_ObjectIdentity = ObjectIdentity
teldatSreTrap_L2TP = _TeldatSreTrap_L2TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 172)
)
_TeldatSreTrap_NSLA_ObjectIdentity = ObjectIdentity
teldatSreTrap_NSLA = _TeldatSreTrap_NSLA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 173)
)
_TeldatSreTrap_VOIP_ObjectIdentity = ObjectIdentity
teldatSreTrap_VOIP = _TeldatSreTrap_VOIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 174)
)
_TeldatSreTrap_TTTP_ObjectIdentity = ObjectIdentity
teldatSreTrap_TTTP = _TeldatSreTrap_TTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 175)
)
_TeldatSreTrap_IKE_ObjectIdentity = ObjectIdentity
teldatSreTrap_IKE = _TeldatSreTrap_IKE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 176)
)
_TeldatSreTrap_HSSI_ObjectIdentity = ObjectIdentity
teldatSreTrap_HSSI = _TeldatSreTrap_HSSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 177)
)
_TeldatSreTrap_SCADA_ObjectIdentity = ObjectIdentity
teldatSreTrap_SCADA = _TeldatSreTrap_SCADA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 178)
)
_TeldatSreTrap_VRRP_ObjectIdentity = ObjectIdentity
teldatSreTrap_VRRP = _TeldatSreTrap_VRRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 179)
)
_TeldatSreTrap_SIP_ObjectIdentity = ObjectIdentity
teldatSreTrap_SIP = _TeldatSreTrap_SIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 180)
)
_TeldatSreTrap_IPHC_ObjectIdentity = ObjectIdentity
teldatSreTrap_IPHC = _TeldatSreTrap_IPHC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 181)
)
_TeldatSreTrap_DHCPC_ObjectIdentity = ObjectIdentity
teldatSreTrap_DHCPC = _TeldatSreTrap_DHCPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 182)
)
_TeldatSreTrap_CNSL_ObjectIdentity = ObjectIdentity
teldatSreTrap_CNSL = _TeldatSreTrap_CNSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 183)
)
_TeldatSreTrap_TLPHY_ObjectIdentity = ObjectIdentity
teldatSreTrap_TLPHY = _TeldatSreTrap_TLPHY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 184)
)
_TeldatSreTrap_NHRP_ObjectIdentity = ObjectIdentity
teldatSreTrap_NHRP = _TeldatSreTrap_NHRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 185)
)
_TeldatSreTrap_SNAT_ObjectIdentity = ObjectIdentity
teldatSreTrap_SNAT = _TeldatSreTrap_SNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 186)
)
_TeldatSreTrap_STUN_ObjectIdentity = ObjectIdentity
teldatSreTrap_STUN = _TeldatSreTrap_STUN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 187)
)
_TeldatSreTrap_WLAN_ObjectIdentity = ObjectIdentity
teldatSreTrap_WLAN = _TeldatSreTrap_WLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 188)
)
_TeldatSreTrap_SCDFW_ObjectIdentity = ObjectIdentity
teldatSreTrap_SCDFW = _TeldatSreTrap_SCDFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 189)
)
_TeldatSreTrap_HDLC_ObjectIdentity = ObjectIdentity
teldatSreTrap_HDLC = _TeldatSreTrap_HDLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 190)
)
_TeldatSreTrap_EAP_ObjectIdentity = ObjectIdentity
teldatSreTrap_EAP = _TeldatSreTrap_EAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 191)
)
_TeldatSreTrap_EIBZ_ObjectIdentity = ObjectIdentity
teldatSreTrap_EIBZ = _TeldatSreTrap_EIBZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 192)
)
_TeldatSreTrap_PHYS_ObjectIdentity = ObjectIdentity
teldatSreTrap_PHYS = _TeldatSreTrap_PHYS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 193)
)
_TeldatSreTrap_SPOOF_ObjectIdentity = ObjectIdentity
teldatSreTrap_SPOOF = _TeldatSreTrap_SPOOF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 194)
)
_TeldatSreTrap_IRVOZ_ObjectIdentity = ObjectIdentity
teldatSreTrap_IRVOZ = _TeldatSreTrap_IRVOZ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 195)
)
_TeldatSreTrap_RSTP_ObjectIdentity = ObjectIdentity
teldatSreTrap_RSTP = _TeldatSreTrap_RSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 196)
)
_TeldatSreTrap_TIDP_ObjectIdentity = ObjectIdentity
teldatSreTrap_TIDP = _TeldatSreTrap_TIDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 197)
)
_TeldatSreTrap_NOE_ObjectIdentity = ObjectIdentity
teldatSreTrap_NOE = _TeldatSreTrap_NOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 198)
)
_TeldatSreTrap_AFS_ObjectIdentity = ObjectIdentity
teldatSreTrap_AFS = _TeldatSreTrap_AFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 199)
)
_TeldatSreTrap_X28_ObjectIdentity = ObjectIdentity
teldatSreTrap_X28 = _TeldatSreTrap_X28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 200)
)
_TeldatSreTrap_BFD_ObjectIdentity = ObjectIdentity
teldatSreTrap_BFD = _TeldatSreTrap_BFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 203)
)
_TeldatSreTrap_DNSU_ObjectIdentity = ObjectIdentity
teldatSreTrap_DNSU = _TeldatSreTrap_DNSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 204)
)
_TeldatSreTrap_UDP6_ObjectIdentity = ObjectIdentity
teldatSreTrap_UDP6 = _TeldatSreTrap_UDP6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 205)
)
_TeldatSreTrap_ICM6O_ObjectIdentity = ObjectIdentity
teldatSreTrap_ICM6O = _TeldatSreTrap_ICM6O_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 206)
)
_TeldatSreTrap_CELL_ObjectIdentity = ObjectIdentity
teldatSreTrap_CELL = _TeldatSreTrap_CELL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 208)
)
_TeldatSreTrap_SSL_ObjectIdentity = ObjectIdentity
teldatSreTrap_SSL = _TeldatSreTrap_SSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 209)
)
_TeldatSreTrap_SCCP_ObjectIdentity = ObjectIdentity
teldatSreTrap_SCCP = _TeldatSreTrap_SCCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 210)
)
_TeldatSreTrap_WWAN_ObjectIdentity = ObjectIdentity
teldatSreTrap_WWAN = _TeldatSreTrap_WWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 211)
)
_TeldatSreTrap_ISTD_ObjectIdentity = ObjectIdentity
teldatSreTrap_ISTD = _TeldatSreTrap_ISTD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 212)
)
_TeldatSreTrap_DOT1X_ObjectIdentity = ObjectIdentity
teldatSreTrap_DOT1X = _TeldatSreTrap_DOT1X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 213)
)
_TeldatSreTrap_EOAM_ObjectIdentity = ObjectIdentity
teldatSreTrap_EOAM = _TeldatSreTrap_EOAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 214)
)
_TeldatSreTrap_SSH_ObjectIdentity = ObjectIdentity
teldatSreTrap_SSH = _TeldatSreTrap_SSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 215)
)
_TeldatSreTrap_CDP_ObjectIdentity = ObjectIdentity
teldatSreTrap_CDP = _TeldatSreTrap_CDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 216)
)
_TeldatSreTrap_PIO_ObjectIdentity = ObjectIdentity
teldatSreTrap_PIO = _TeldatSreTrap_PIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 217)
)
_TeldatSreTrap_FLOW_ObjectIdentity = ObjectIdentity
teldatSreTrap_FLOW = _TeldatSreTrap_FLOW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 218)
)
_TeldatSreTrap_RIP_ObjectIdentity = ObjectIdentity
teldatSreTrap_RIP = _TeldatSreTrap_RIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 219)
)
_TeldatSreTrap_MGCP_ObjectIdentity = ObjectIdentity
teldatSreTrap_MGCP = _TeldatSreTrap_MGCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 220)
)
_TeldatSreTrap_TIPS_ObjectIdentity = ObjectIdentity
teldatSreTrap_TIPS = _TeldatSreTrap_TIPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 221)
)
_TeldatSreTrap_SRVP_ObjectIdentity = ObjectIdentity
teldatSreTrap_SRVP = _TeldatSreTrap_SRVP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 222)
)
_TeldatSreTrap_SPI_ObjectIdentity = ObjectIdentity
teldatSreTrap_SPI = _TeldatSreTrap_SPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 223)
)
_TeldatSreTrap_VLI_ObjectIdentity = ObjectIdentity
teldatSreTrap_VLI = _TeldatSreTrap_VLI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 224)
)
_TeldatSreTrap_ACAT_ObjectIdentity = ObjectIdentity
teldatSreTrap_ACAT = _TeldatSreTrap_ACAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 225)
)
_TeldatSreTrap_AAA_ObjectIdentity = ObjectIdentity
teldatSreTrap_AAA = _TeldatSreTrap_AAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 226)
)
_TeldatSreTrap_SDEV_ObjectIdentity = ObjectIdentity
teldatSreTrap_SDEV = _TeldatSreTrap_SDEV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 227)
)
_TeldatSreTrap_G104_ObjectIdentity = ObjectIdentity
teldatSreTrap_G104 = _TeldatSreTrap_G104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 228)
)
_TeldatSreTrap_I101_ObjectIdentity = ObjectIdentity
teldatSreTrap_I101 = _TeldatSreTrap_I101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 229)
)
_TeldatSreTrap_IPSF_ObjectIdentity = ObjectIdentity
teldatSreTrap_IPSF = _TeldatSreTrap_IPSF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 230)
)
_TeldatSreTrap_DH6C_ObjectIdentity = ObjectIdentity
teldatSreTrap_DH6C = _TeldatSreTrap_DH6C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 231)
)
_TeldatSreTrap_NEIG_ObjectIdentity = ObjectIdentity
teldatSreTrap_NEIG = _TeldatSreTrap_NEIG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 232)
)
_TeldatSreTrap_ND_ObjectIdentity = ObjectIdentity
teldatSreTrap_ND = _TeldatSreTrap_ND_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 233)
)
_TeldatSreTrap_ICM6_ObjectIdentity = ObjectIdentity
teldatSreTrap_ICM6 = _TeldatSreTrap_ICM6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 234)
)
_TeldatSreTrap_LLDP_ObjectIdentity = ObjectIdentity
teldatSreTrap_LLDP = _TeldatSreTrap_LLDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 235)
)
_TeldatSreTrap_RIP6_ObjectIdentity = ObjectIdentity
teldatSreTrap_RIP6 = _TeldatSreTrap_RIP6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 236)
)
_TeldatSreTrap_MLD6_ObjectIdentity = ObjectIdentity
teldatSreTrap_MLD6 = _TeldatSreTrap_MLD6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 237)
)
_TeldatSreTrap_PIM_ObjectIdentity = ObjectIdentity
teldatSreTrap_PIM = _TeldatSreTrap_PIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 238)
)
_TeldatSreTrap_MRTE_ObjectIdentity = ObjectIdentity
teldatSreTrap_MRTE = _TeldatSreTrap_MRTE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 239)
)
_TeldatSreTrap_ACL_ObjectIdentity = ObjectIdentity
teldatSreTrap_ACL = _TeldatSreTrap_ACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 240)
)
_TeldatSreTrap_SPF6_ObjectIdentity = ObjectIdentity
teldatSreTrap_SPF6 = _TeldatSreTrap_SPF6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 241)
)
_TeldatSreTrap_NIC_ObjectIdentity = ObjectIdentity
teldatSreTrap_NIC = _TeldatSreTrap_NIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 242)
)
_TeldatSreTrap_MSDP_ObjectIdentity = ObjectIdentity
teldatSreTrap_MSDP = _TeldatSreTrap_MSDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 244)
)
_TeldatSreTrap_ACT_ObjectIdentity = ObjectIdentity
teldatSreTrap_ACT = _TeldatSreTrap_ACT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 245)
)
_TeldatSreTrap_TDGS_ObjectIdentity = ObjectIdentity
teldatSreTrap_TDGS = _TeldatSreTrap_TDGS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 255)
)
_TeldatSreTrap_GPSF_ObjectIdentity = ObjectIdentity
teldatSreTrap_GPSF = _TeldatSreTrap_GPSF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 256)
)
_TeldatSreTrap_WNMS_ObjectIdentity = ObjectIdentity
teldatSreTrap_WNMS = _TeldatSreTrap_WNMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 257)
)
_TeldatSreTrap_DH6S_ObjectIdentity = ObjectIdentity
teldatSreTrap_DH6S = _TeldatSreTrap_DH6S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 259)
)
_TeldatSreTrap_CFM_ObjectIdentity = ObjectIdentity
teldatSreTrap_CFM = _TeldatSreTrap_CFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 264)
)
_TeldatSreTrap_PRIME_ObjectIdentity = ObjectIdentity
teldatSreTrap_PRIME = _TeldatSreTrap_PRIME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 265)
)
_TeldatSreTrap_SMGT_ObjectIdentity = ObjectIdentity
teldatSreTrap_SMGT = _TeldatSreTrap_SMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 1, 266)
)
_SreTrapSubSist_Type = Integer32
_SreTrapSubSist_Object = MibScalar
sreTrapSubSist = _SreTrapSubSist_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 2),
    _SreTrapSubSist_Type()
)
sreTrapSubSist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreTrapSubSist.setStatus("mandatory")
_SreTrapEvento_Type = Integer32
_SreTrapEvento_Object = MibScalar
sreTrapEvento = _SreTrapEvento_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 3),
    _SreTrapEvento_Type()
)
sreTrapEvento.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreTrapEvento.setStatus("mandatory")
_SreTrapVar1_Type = Opaque
_SreTrapVar1_Object = MibScalar
sreTrapVar1 = _SreTrapVar1_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 4),
    _SreTrapVar1_Type()
)
sreTrapVar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreTrapVar1.setStatus("mandatory")
_SreTrapVar2_Type = Opaque
_SreTrapVar2_Object = MibScalar
sreTrapVar2 = _SreTrapVar2_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 5),
    _SreTrapVar2_Type()
)
sreTrapVar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreTrapVar2.setStatus("mandatory")
_SreTrapVar3_Type = Opaque
_SreTrapVar3_Object = MibScalar
sreTrapVar3 = _SreTrapVar3_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 6),
    _SreTrapVar3_Type()
)
sreTrapVar3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreTrapVar3.setStatus("mandatory")
_SreTrapVar4_Type = Opaque
_SreTrapVar4_Object = MibScalar
sreTrapVar4 = _SreTrapVar4_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 7),
    _SreTrapVar4_Type()
)
sreTrapVar4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreTrapVar4.setStatus("mandatory")
_SreTrapVar5_Type = Opaque
_SreTrapVar5_Object = MibScalar
sreTrapVar5 = _SreTrapVar5_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 8),
    _SreTrapVar5_Type()
)
sreTrapVar5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreTrapVar5.setStatus("mandatory")
_SreTrapVar6_Type = Opaque
_SreTrapVar6_Object = MibScalar
sreTrapVar6 = _SreTrapVar6_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 9),
    _SreTrapVar6_Type()
)
sreTrapVar6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreTrapVar6.setStatus("mandatory")
_SreTrapVar7_Type = Opaque
_SreTrapVar7_Object = MibScalar
sreTrapVar7 = _SreTrapVar7_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 10),
    _SreTrapVar7_Type()
)
sreTrapVar7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreTrapVar7.setStatus("mandatory")
_SreTrapVar8_Type = Opaque
_SreTrapVar8_Object = MibScalar
sreTrapVar8 = _SreTrapVar8_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 11),
    _SreTrapVar8_Type()
)
sreTrapVar8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreTrapVar8.setStatus("mandatory")
_SreTrapVar9_Type = Opaque
_SreTrapVar9_Object = MibScalar
sreTrapVar9 = _SreTrapVar9_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 12),
    _SreTrapVar9_Type()
)
sreTrapVar9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreTrapVar9.setStatus("mandatory")
_Equipo_rexis_mru_ObjectIdentity = ObjectIdentity
equipo_rexis_mru = _Equipo_rexis_mru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 15)
)
_Equipo_mbbu_ObjectIdentity = ObjectIdentity
equipo_mbbu = _Equipo_mbbu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 16)
)
_Equipo_bir_u_ObjectIdentity = ObjectIdentity
equipo_bir_u = _Equipo_bir_u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 20)
)
_Equipo_ebano_ObjectIdentity = ObjectIdentity
equipo_ebano = _Equipo_ebano_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 21)
)
_Equipo_nucleox_plus_ObjectIdentity = ObjectIdentity
equipo_nucleox_plus = _Equipo_nucleox_plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 32)
)
_Equipo_cbra_ObjectIdentity = ObjectIdentity
equipo_cbra = _Equipo_cbra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 33)
)
_Equipo_centrix_b_ObjectIdentity = ObjectIdentity
equipo_centrix_b = _Equipo_centrix_b_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 34)
)
_Equipo_centrix_p_ObjectIdentity = ObjectIdentity
equipo_centrix_p = _Equipo_centrix_p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 35)
)
_Equipo_temis_ObjectIdentity = ObjectIdentity
equipo_temis = _Equipo_temis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 36)
)
_Equipo_novacom_ObjectIdentity = ObjectIdentity
equipo_novacom = _Equipo_novacom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 37)
)
_Equipo_router_maestro_ObjectIdentity = ObjectIdentity
equipo_router_maestro = _Equipo_router_maestro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 38)
)
_Equipo_cbra20_ObjectIdentity = ObjectIdentity
equipo_cbra20 = _Equipo_cbra20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 39)
)
_Equipo_np20h_ObjectIdentity = ObjectIdentity
equipo_np20h = _Equipo_np20h_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 40)
)
_Equipo_icu_plus_ObjectIdentity = ObjectIdentity
equipo_icu_plus = _Equipo_icu_plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 41)
)
_Equipo_centrix_f_ObjectIdentity = ObjectIdentity
equipo_centrix_f = _Equipo_centrix_f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 42)
)
_Equipo_cbra_tar_ObjectIdentity = ObjectIdentity
equipo_cbra_tar = _Equipo_cbra_tar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 43)
)
_Equipo_aura_ObjectIdentity = ObjectIdentity
equipo_aura = _Equipo_aura_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 44)
)
_Equipo_kronos_ObjectIdentity = ObjectIdentity
equipo_kronos = _Equipo_kronos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 45)
)
_Equipo_teldat_C2_ObjectIdentity = ObjectIdentity
equipo_teldat_C2 = _Equipo_teldat_C2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 46)
)
_Equipo_operador_remoto_ObjectIdentity = ObjectIdentity
equipo_operador_remoto = _Equipo_operador_remoto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 47)
)
_Equipo_visor_ObjectIdentity = ObjectIdentity
equipo_visor = _Equipo_visor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 48)
)
_Equipo_voxnet_ObjectIdentity = ObjectIdentity
equipo_voxnet = _Equipo_voxnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 49)
)
_Equipo_dusac32_ObjectIdentity = ObjectIdentity
equipo_dusac32 = _Equipo_dusac32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 50)
)
_Equipo_novacom_x25_ObjectIdentity = ObjectIdentity
equipo_novacom_x25 = _Equipo_novacom_x25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 51)
)
_Equipo_enaplan_ObjectIdentity = ObjectIdentity
equipo_enaplan = _Equipo_enaplan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 52)
)
_Equipo_teldat_C3_ObjectIdentity = ObjectIdentity
equipo_teldat_C3 = _Equipo_teldat_C3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 53)
)
_Equipo_atlas_standard_ObjectIdentity = ObjectIdentity
equipo_atlas_standard = _Equipo_atlas_standard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 56)
)
_Equipo_teldat_C2B_ObjectIdentity = ObjectIdentity
equipo_teldat_C2B = _Equipo_teldat_C2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 57)
)
_Equipo_teldat_CSW_ObjectIdentity = ObjectIdentity
equipo_teldat_CSW = _Equipo_teldat_CSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 58)
)
_Equipo_teldat_C3_1_ObjectIdentity = ObjectIdentity
equipo_teldat_C3_1 = _Equipo_teldat_C3_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 59)
)
_Equipo_teldat_C3B_1_ObjectIdentity = ObjectIdentity
equipo_teldat_C3B_1 = _Equipo_teldat_C3B_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 60)
)
_Equipo_teldat_C2BM_ObjectIdentity = ObjectIdentity
equipo_teldat_C2BM = _Equipo_teldat_C2BM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 61)
)
_Equipo_atlas_basico_ObjectIdentity = ObjectIdentity
equipo_atlas_basico = _Equipo_atlas_basico_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 62)
)
_Equipo_teldat_C2i_ObjectIdentity = ObjectIdentity
equipo_teldat_C2i = _Equipo_teldat_C2i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 63)
)
_Equipo_teldat_C3i_ObjectIdentity = ObjectIdentity
equipo_teldat_C3i = _Equipo_teldat_C3i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 64)
)
_Equipo_teldat_C3B_ObjectIdentity = ObjectIdentity
equipo_teldat_C3B = _Equipo_teldat_C3B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 65)
)
_Equipo_teldat_C3G_ObjectIdentity = ObjectIdentity
equipo_teldat_C3G = _Equipo_teldat_C3G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 66)
)
_Equipo_teldat_C4_ObjectIdentity = ObjectIdentity
equipo_teldat_C4 = _Equipo_teldat_C4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 67)
)
_Equipo_teldat_C4i_ObjectIdentity = ObjectIdentity
equipo_teldat_C4i = _Equipo_teldat_C4i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 68)
)
_Equipo_teldat_C4B_ObjectIdentity = ObjectIdentity
equipo_teldat_C4B = _Equipo_teldat_C4B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 69)
)
_Equipo_centrix_sec_ObjectIdentity = ObjectIdentity
equipo_centrix_sec = _Equipo_centrix_sec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 70)
)
_Equipo_centrix_d_ObjectIdentity = ObjectIdentity
equipo_centrix_d = _Equipo_centrix_d_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 71)
)
_Equipo_teldat_C2_UP_ObjectIdentity = ObjectIdentity
equipo_teldat_C2_UP = _Equipo_teldat_C2_UP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 72)
)
_Equipo_teldat_C6_ObjectIdentity = ObjectIdentity
equipo_teldat_C6 = _Equipo_teldat_C6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 73)
)
_Equipo_centrix_ng_ObjectIdentity = ObjectIdentity
equipo_centrix_ng = _Equipo_centrix_ng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 74)
)
_Equipo_atlas_voxnet_ObjectIdentity = ObjectIdentity
equipo_atlas_voxnet = _Equipo_atlas_voxnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 75)
)
_Equipo_s2_ObjectIdentity = ObjectIdentity
equipo_s2 = _Equipo_s2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 76)
)
_Equipo_s4_ObjectIdentity = ObjectIdentity
equipo_s4 = _Equipo_s4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 77)
)
_Equipo_s2i_ObjectIdentity = ObjectIdentity
equipo_s2i = _Equipo_s2i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 78)
)
_Equipo_s4i_ObjectIdentity = ObjectIdentity
equipo_s4i = _Equipo_s4i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 79)
)
_Equipo_g2_ObjectIdentity = ObjectIdentity
equipo_g2 = _Equipo_g2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 80)
)
_Equipo_g3_ObjectIdentity = ObjectIdentity
equipo_g3 = _Equipo_g3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 81)
)
_Equipo_g4_ObjectIdentity = ObjectIdentity
equipo_g4 = _Equipo_g4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 82)
)
_Equipo_g2i_ObjectIdentity = ObjectIdentity
equipo_g2i = _Equipo_g2i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 83)
)
_Equipo_g3i_ObjectIdentity = ObjectIdentity
equipo_g3i = _Equipo_g3i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 84)
)
_Equipo_g4i_ObjectIdentity = ObjectIdentity
equipo_g4i = _Equipo_g4i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 85)
)
_Equipo_c1_ObjectIdentity = ObjectIdentity
equipo_c1 = _Equipo_c1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 86)
)
_Equipo_c1B_ObjectIdentity = ObjectIdentity
equipo_c1B = _Equipo_c1B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 87)
)
_Equipo_c1i_ObjectIdentity = ObjectIdentity
equipo_c1i = _Equipo_c1i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 88)
)
_Equipo_s1_ObjectIdentity = ObjectIdentity
equipo_s1 = _Equipo_s1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 89)
)
_Equipo_s1i_ObjectIdentity = ObjectIdentity
equipo_s1i = _Equipo_s1i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 90)
)
_Equipo_g1_ObjectIdentity = ObjectIdentity
equipo_g1 = _Equipo_g1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 91)
)
_Equipo_g1i_ObjectIdentity = ObjectIdentity
equipo_g1i = _Equipo_g1i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 92)
)
_Equipo_g3_lite_ObjectIdentity = ObjectIdentity
equipo_g3_lite = _Equipo_g3_lite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 93)
)
_Equipo_C3G_lite_ObjectIdentity = ObjectIdentity
equipo_C3G_lite = _Equipo_C3G_lite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 94)
)
_Equipo_atlas_100_ObjectIdentity = ObjectIdentity
equipo_atlas_100 = _Equipo_atlas_100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 96)
)
_Equipo_atlas_300V_ObjectIdentity = ObjectIdentity
equipo_atlas_300V = _Equipo_atlas_300V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 97)
)
_Equipo_c1G_ObjectIdentity = ObjectIdentity
equipo_c1G = _Equipo_c1G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 98)
)
_Equipo_atlas_250_ObjectIdentity = ObjectIdentity
equipo_atlas_250 = _Equipo_atlas_250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 101)
)
_Equipo_c4G_ObjectIdentity = ObjectIdentity
equipo_c4G = _Equipo_c4G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 102)
)
_Equipo_atlas_100B_ObjectIdentity = ObjectIdentity
equipo_atlas_100B = _Equipo_atlas_100B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 103)
)
_Equipo_atlas_150_ObjectIdentity = ObjectIdentity
equipo_atlas_150 = _Equipo_atlas_150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 104)
)
_Equipo_a2_ObjectIdentity = ObjectIdentity
equipo_a2 = _Equipo_a2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 105)
)
_Equipo_a3_ObjectIdentity = ObjectIdentity
equipo_a3 = _Equipo_a3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 106)
)
_Equipo_a4_ObjectIdentity = ObjectIdentity
equipo_a4 = _Equipo_a4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 107)
)
_Equipo_a2i_ObjectIdentity = ObjectIdentity
equipo_a2i = _Equipo_a2i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 108)
)
_Equipo_a3i_ObjectIdentity = ObjectIdentity
equipo_a3i = _Equipo_a3i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 109)
)
_Equipo_a4i_ObjectIdentity = ObjectIdentity
equipo_a4i = _Equipo_a4i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 110)
)
_Equipo_a1_ObjectIdentity = ObjectIdentity
equipo_a1 = _Equipo_a1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 111)
)
_Equipo_a1i_ObjectIdentity = ObjectIdentity
equipo_a1i = _Equipo_a1i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 112)
)
_Equipo_g4_cdma_ObjectIdentity = ObjectIdentity
equipo_g4_cdma = _Equipo_g4_cdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 114)
)
_Equipo_g4i_cdma_ObjectIdentity = ObjectIdentity
equipo_g4i_cdma = _Equipo_g4i_cdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 115)
)
_Equipo_g3_cdma_ObjectIdentity = ObjectIdentity
equipo_g3_cdma = _Equipo_g3_cdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 116)
)
_Equipo_g3i_cdma_ObjectIdentity = ObjectIdentity
equipo_g3i_cdma = _Equipo_g3i_cdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 117)
)
_Equipo_g1_cdma_ObjectIdentity = ObjectIdentity
equipo_g1_cdma = _Equipo_g1_cdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 118)
)
_Equipo_g1i_cdma_ObjectIdentity = ObjectIdentity
equipo_g1i_cdma = _Equipo_g1i_cdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 119)
)
_Equipo_c1plus_ObjectIdentity = ObjectIdentity
equipo_c1plus = _Equipo_c1plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 122)
)
_Equipo_c1iplus_ObjectIdentity = ObjectIdentity
equipo_c1iplus = _Equipo_c1iplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 123)
)
_Equipo_atlas_50_ObjectIdentity = ObjectIdentity
equipo_atlas_50 = _Equipo_atlas_50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 126)
)
_Equipo_g4plus_ObjectIdentity = ObjectIdentity
equipo_g4plus = _Equipo_g4plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 127)
)
_Equipo_g3plus_ObjectIdentity = ObjectIdentity
equipo_g3plus = _Equipo_g3plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 128)
)
_Equipo_g1plus_ObjectIdentity = ObjectIdentity
equipo_g1plus = _Equipo_g1plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 129)
)
_Equipo_g4iplus_ObjectIdentity = ObjectIdentity
equipo_g4iplus = _Equipo_g4iplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 130)
)
_Equipo_g3iplus_ObjectIdentity = ObjectIdentity
equipo_g3iplus = _Equipo_g3iplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 131)
)
_Equipo_g1iplus_ObjectIdentity = ObjectIdentity
equipo_g1iplus = _Equipo_g1iplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 132)
)
_Equipo_atlas_250SW_ObjectIdentity = ObjectIdentity
equipo_atlas_250SW = _Equipo_atlas_250SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 133)
)
_Equipo_atlas_150SW_ObjectIdentity = ObjectIdentity
equipo_atlas_150SW = _Equipo_atlas_150SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 134)
)
_Equipo_atlas_50SW_ObjectIdentity = ObjectIdentity
equipo_atlas_50SW = _Equipo_atlas_50SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 135)
)
_Equipo_vyda_1M_ObjectIdentity = ObjectIdentity
equipo_vyda_1M = _Equipo_vyda_1M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 136)
)
_Equipo_vyda_2M_ObjectIdentity = ObjectIdentity
equipo_vyda_2M = _Equipo_vyda_2M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 137)
)
_Equipo_vyda_3M_ObjectIdentity = ObjectIdentity
equipo_vyda_3M = _Equipo_vyda_3M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 138)
)
_Equipo_atlas_300_ObjectIdentity = ObjectIdentity
equipo_atlas_300 = _Equipo_atlas_300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 139)
)
_Equipo_atlas_152_ObjectIdentity = ObjectIdentity
equipo_atlas_152 = _Equipo_atlas_152_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 140)
)
_Equipo_vyda_compact_ObjectIdentity = ObjectIdentity
equipo_vyda_compact = _Equipo_vyda_compact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 141)
)
_Equipo_C8plus_ObjectIdentity = ObjectIdentity
equipo_C8plus = _Equipo_C8plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 142)
)
_Equipo_C8iplus_ObjectIdentity = ObjectIdentity
equipo_C8iplus = _Equipo_C8iplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 143)
)
_Equipo_C9plus_ObjectIdentity = ObjectIdentity
equipo_C9plus = _Equipo_C9plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 144)
)
_Equipo_C9iplus_ObjectIdentity = ObjectIdentity
equipo_C9iplus = _Equipo_C9iplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 145)
)
_Equipo_atlas_360_ObjectIdentity = ObjectIdentity
equipo_atlas_360 = _Equipo_atlas_360_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 146)
)
_Equipo_c1plus_SW_ObjectIdentity = ObjectIdentity
equipo_c1plus_SW = _Equipo_c1plus_SW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 147)
)
_Equipo_c1a_ObjectIdentity = ObjectIdentity
equipo_c1a = _Equipo_c1a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 148)
)
_Equipo_s1a_ObjectIdentity = ObjectIdentity
equipo_s1a = _Equipo_s1a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 149)
)
_Equipo_g1a_ObjectIdentity = ObjectIdentity
equipo_g1a = _Equipo_g1a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 150)
)
_Equipo_g1a_cdma_ObjectIdentity = ObjectIdentity
equipo_g1a_cdma = _Equipo_g1a_cdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 151)
)
_Equipo_a1a_ObjectIdentity = ObjectIdentity
equipo_a1a = _Equipo_a1a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 152)
)
_Equipo_c2a_ObjectIdentity = ObjectIdentity
equipo_c2a = _Equipo_c2a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 155)
)
_Equipo_s2a_ObjectIdentity = ObjectIdentity
equipo_s2a = _Equipo_s2a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 156)
)
_Equipo_g2a_ObjectIdentity = ObjectIdentity
equipo_g2a = _Equipo_g2a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 157)
)
_Equipo_a2a_ObjectIdentity = ObjectIdentity
equipo_a2a = _Equipo_a2a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 158)
)
_Equipo_c4a_ObjectIdentity = ObjectIdentity
equipo_c4a = _Equipo_c4a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 159)
)
_Equipo_s4a_ObjectIdentity = ObjectIdentity
equipo_s4a = _Equipo_s4a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 160)
)
_Equipo_g4a_ObjectIdentity = ObjectIdentity
equipo_g4a = _Equipo_g4a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 161)
)
_Equipo_g4a_cdma_ObjectIdentity = ObjectIdentity
equipo_g4a_cdma = _Equipo_g4a_cdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 162)
)
_Equipo_a4a_ObjectIdentity = ObjectIdentity
equipo_a4a = _Equipo_a4a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 163)
)
_Equipo_cirus_ObjectIdentity = ObjectIdentity
equipo_cirus = _Equipo_cirus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 165)
)
_Equipo_h1_ObjectIdentity = ObjectIdentity
equipo_h1 = _Equipo_h1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 166)
)
_Equipo_atlas_260_ObjectIdentity = ObjectIdentity
equipo_atlas_260 = _Equipo_atlas_260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 167)
)
_Equipo_atlas_160_ObjectIdentity = ObjectIdentity
equipo_atlas_160 = _Equipo_atlas_160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 168)
)
_Equipo_vyda_4M_ObjectIdentity = ObjectIdentity
equipo_vyda_4M = _Equipo_vyda_4M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 169)
)
_Equipo_t200g_ObjectIdentity = ObjectIdentity
equipo_t200g = _Equipo_t200g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 170)
)
_Equipo_h1_auto_ObjectIdentity = ObjectIdentity
equipo_h1_auto = _Equipo_h1_auto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 171)
)
_Equipo_g1n_ObjectIdentity = ObjectIdentity
equipo_g1n = _Equipo_g1n_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 172)
)
_Equipo_v1_ObjectIdentity = ObjectIdentity
equipo_v1 = _Equipo_v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 173)
)
_Equipo_c1plusl_ObjectIdentity = ObjectIdentity
equipo_c1plusl = _Equipo_c1plusl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 174)
)
_Equipo_h4_ObjectIdentity = ObjectIdentity
equipo_h4 = _Equipo_h4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 175)
)
_Equipo_t200_ObjectIdentity = ObjectIdentity
equipo_t200 = _Equipo_t200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 176)
)
_Equipo_h1plus_ObjectIdentity = ObjectIdentity
equipo_h1plus = _Equipo_h1plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 177)
)
_Equipo_regesta_rp81_ObjectIdentity = ObjectIdentity
equipo_regesta_rp81 = _Equipo_regesta_rp81_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 178)
)
_Equipo_regesta_rp82_ObjectIdentity = ObjectIdentity
equipo_regesta_rp82 = _Equipo_regesta_rp82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 179)
)
_Equipo_regesta_1_ObjectIdentity = ObjectIdentity
equipo_regesta_1 = _Equipo_regesta_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 180)
)
_Equipo_f1plus_ObjectIdentity = ObjectIdentity
equipo_f1plus = _Equipo_f1plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 181)
)
_Equipo_l1plus_ObjectIdentity = ObjectIdentity
equipo_l1plus = _Equipo_l1plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 183)
)
_Equipo_regesta_rp61er_ObjectIdentity = ObjectIdentity
equipo_regesta_rp61er = _Equipo_regesta_rp61er_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 184)
)
_Equipo_regesta_rp62er_ObjectIdentity = ObjectIdentity
equipo_regesta_rp62er = _Equipo_regesta_rp62er_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 185)
)
_Equipo_3geplus_ObjectIdentity = ObjectIdentity
equipo_3geplus = _Equipo_3geplus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 186)
)
_Equipo_atlas_60_ObjectIdentity = ObjectIdentity
equipo_atlas_60 = _Equipo_atlas_60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 187)
)
_Equipo_3geplus_cdma_ObjectIdentity = ObjectIdentity
equipo_3geplus_cdma = _Equipo_3geplus_cdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 188)
)
_Equipo_h1auto_plus_ObjectIdentity = ObjectIdentity
equipo_h1auto_plus = _Equipo_h1auto_plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 189)
)
_Equipo_k_ObjectIdentity = ObjectIdentity
equipo_k = _Equipo_k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 190)
)
_Equipo_v_ObjectIdentity = ObjectIdentity
equipo_v = _Equipo_v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 191)
)
_Equipo_connect_104_ObjectIdentity = ObjectIdentity
equipo_connect_104 = _Equipo_connect_104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 192)
)
_Equipo_h1rail_ObjectIdentity = ObjectIdentity
equipo_h1rail = _Equipo_h1rail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 193)
)
_Equipo_kf_ObjectIdentity = ObjectIdentity
equipo_kf = _Equipo_kf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 194)
)
_Equipo_m1_ObjectIdentity = ObjectIdentity
equipo_m1 = _Equipo_m1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 199)
)
_Equipo_m1f_ObjectIdentity = ObjectIdentity
equipo_m1f = _Equipo_m1f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 200)
)
_Equipo_4Ge_ObjectIdentity = ObjectIdentity
equipo_4Ge = _Equipo_4Ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 201)
)
_Router_oa5710v_ObjectIdentity = ObjectIdentity
router_oa5710v = _Router_oa5710v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 202)
)
_Router_oa5720_ObjectIdentity = ObjectIdentity
router_oa5720 = _Router_oa5720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 203)
)
_Router_oa5840_ObjectIdentity = ObjectIdentity
router_oa5840 = _Router_oa5840_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 204)
)
_Router_oa5850_ObjectIdentity = ObjectIdentity
router_oa5850 = _Router_oa5850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 205)
)
_Router_oa5725r61er_ObjectIdentity = ObjectIdentity
router_oa5725r61er = _Router_oa5725r61er_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 206)
)
_Router_oa5725r62er_ObjectIdentity = ObjectIdentity
router_oa5725r62er = _Router_oa5725r62er_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 207)
)
_Router_oa5725a3g_ObjectIdentity = ObjectIdentity
router_oa5725a3g = _Router_oa5725a3g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 208)
)
_Router_oa5725alte_ObjectIdentity = ObjectIdentity
router_oa5725alte = _Router_oa5725alte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 209)
)
_Router_esrwwanenabler_ObjectIdentity = ObjectIdentity
router_esrwwanenabler = _Router_esrwwanenabler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 210)
)
_Equipo_connect_104_v_ObjectIdentity = ObjectIdentity
equipo_connect_104_v = _Equipo_connect_104_v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 211)
)
_Equipo_connect_104_kf_ObjectIdentity = ObjectIdentity
equipo_connect_104_kf = _Equipo_connect_104_kf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 212)
)
_Equipo_connect_4ge_ObjectIdentity = ObjectIdentity
equipo_connect_4ge = _Equipo_connect_4ge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 213)
)
_Equipo_bintecrsc_ObjectIdentity = ObjectIdentity
equipo_bintecrsc = _Equipo_bintecrsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 214)
)
_Equipo_regesta_lite_ObjectIdentity = ObjectIdentity
equipo_regesta_lite = _Equipo_regesta_lite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 215)
)
_Equipo_bintecrvc_ObjectIdentity = ObjectIdentity
equipo_bintecrvc = _Equipo_bintecrvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 216)
)
_Equipo_H2auto_ObjectIdentity = ObjectIdentity
equipo_H2auto = _Equipo_H2auto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 217)
)
_Equipo_iM8_ObjectIdentity = ObjectIdentity
equipo_iM8 = _Equipo_iM8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 219)
)
_Equipo_iM8_Plus_ObjectIdentity = ObjectIdentity
equipo_iM8_Plus = _Equipo_iM8_Plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 220)
)
_Equipo_H2auto_Plus_ObjectIdentity = ObjectIdentity
equipo_H2auto_Plus = _Equipo_H2auto_Plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 221)
)
_Equipo_regesta_plc_ObjectIdentity = ObjectIdentity
equipo_regesta_plc = _Equipo_regesta_plc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 222)
)
_Equipo_Atlas_i70_ObjectIdentity = ObjectIdentity
equipo_Atlas_i70 = _Equipo_Atlas_i70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 223)
)
_Equipo_Atlas_i70_Plus_ObjectIdentity = ObjectIdentity
equipo_Atlas_i70_Plus = _Equipo_Atlas_i70_Plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 224)
)
_Equipo_h2rail_lite_ObjectIdentity = ObjectIdentity
equipo_h2rail_lite = _Equipo_h2rail_lite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 225)
)
_Equipo_h2rail_lite2_ObjectIdentity = ObjectIdentity
equipo_h2rail_lite2 = _Equipo_h2rail_lite2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 226)
)
_Equipo_h2rail_ObjectIdentity = ObjectIdentity
equipo_h2rail = _Equipo_h2rail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 227)
)
_Equipo_regesta_comp_plc_ObjectIdentity = ObjectIdentity
equipo_regesta_comp_plc = _Equipo_regesta_comp_plc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 1, 229)
)
_Telstatus_ObjectIdentity = ObjectIdentity
telstatus = _Telstatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2)
)
_TelAdminStatusSystem_ObjectIdentity = ObjectIdentity
telAdminStatusSystem = _TelAdminStatusSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 1)
)


class _TelAdminStatusSystemCode_Type(Integer32):
    """Custom type telAdminStatusSystemCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(15,
              16,
              20,
              21,
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
              96,
              97,
              98,
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
              114,
              115,
              116,
              117,
              118,
              119,
              122,
              123,
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
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
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
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              229)
        )
    )
    namedValues = NamedValues(
        *(("rexis-mru", 15),
          ("mbbu", 16),
          ("bir-u", 20),
          ("ebano", 21),
          ("nucleox-plus", 32),
          ("cbra", 33),
          ("centrix-b", 34),
          ("centrix-p", 35),
          ("temis", 36),
          ("novacom", 37),
          ("master-router", 38),
          ("cbra2x", 39),
          ("np2xh", 40),
          ("icu-plus", 41),
          ("centrix-f", 42),
          ("cbra-tar", 43),
          ("aura", 44),
          ("kronos", 45),
          ("teldat-C", 46),
          ("remote-operator", 47),
          ("visor", 48),
          ("voxnet", 49),
          ("dusac32", 50),
          ("novacom-x25", 51),
          ("enaplan", 52),
          ("teldat-C3", 53),
          ("atlas", 56),
          ("c2B", 57),
          ("web-probe", 58),
          ("c3-1", 59),
          ("c3B-1", 60),
          ("c2BM", 61),
          ("basic-atlas", 62),
          ("c2i", 63),
          ("c3i", 64),
          ("c3B", 65),
          ("c3G", 66),
          ("c4", 67),
          ("c4i", 68),
          ("c4B", 69),
          ("centrix-sec", 70),
          ("centrix-d", 71),
          ("c2-UP", 72),
          ("c6", 73),
          ("centrix-ng", 74),
          ("atlas-voxnet", 75),
          ("s2", 76),
          ("s4", 77),
          ("s2i", 78),
          ("s4i", 79),
          ("g2", 80),
          ("g3", 81),
          ("g4", 82),
          ("g2i", 83),
          ("g3i", 84),
          ("g4i", 85),
          ("c1", 86),
          ("c1B", 87),
          ("c1i", 88),
          ("s1", 89),
          ("s1i", 90),
          ("g1", 91),
          ("g1i", 92),
          ("g3-lite", 93),
          ("c3G-lite", 94),
          ("atlas-100", 96),
          ("atlas-300V", 97),
          ("c1G", 98),
          ("atlas-250", 101),
          ("c4G", 102),
          ("atlas-100B", 103),
          ("atlas-150", 104),
          ("a2", 105),
          ("a3", 106),
          ("a4", 107),
          ("a2i", 108),
          ("a3i", 109),
          ("a4i", 110),
          ("a1", 111),
          ("a1i", 112),
          ("g4-cdma", 114),
          ("g4i-cdma", 115),
          ("g3-cdma", 116),
          ("g3i-cdma", 117),
          ("g1-cdma", 118),
          ("g1i-cdma", 119),
          ("c1plus", 122),
          ("c1iplus", 123),
          ("atlas-50", 126),
          ("g4plus", 127),
          ("g3plus", 128),
          ("g1plus", 129),
          ("g4iplus", 130),
          ("g3iplus", 131),
          ("g1iplus", 132),
          ("atlas-250-web-probe", 133),
          ("atlas-150-web-probe", 134),
          ("atlas-50-web-probe", 135),
          ("vyda-1M", 136),
          ("vyda-2M", 137),
          ("vyda-3M", 138),
          ("atlas-300", 139),
          ("atlas-152", 140),
          ("vyda-compact", 141),
          ("c8plus", 142),
          ("c8iplus", 143),
          ("c9plus", 144),
          ("c9iplus", 145),
          ("atlas-360", 146),
          ("c1plus-web-probe", 147),
          ("c1a", 148),
          ("s1a", 149),
          ("g1a", 150),
          ("g1a-cdma", 151),
          ("a1a", 152),
          ("c2a", 155),
          ("s2a", 156),
          ("g2a", 157),
          ("a2a", 158),
          ("c4a", 159),
          ("s4a", 160),
          ("g4a", 161),
          ("g4a-cdma", 162),
          ("a4a", 163),
          ("cirus", 165),
          ("h1", 166),
          ("atlas-260", 167),
          ("atlas-160", 168),
          ("vyda-4M", 169),
          ("teldat-t200g", 170),
          ("teldat-h1-auto", 171),
          ("teldat-g1n", 172),
          ("teldat-v1", 173),
          ("teldat-c1plusl", 174),
          ("teldat-h4", 175),
          ("teldat-t200", 176),
          ("teldat-h1plus", 177),
          ("regesta-rp81", 178),
          ("regesta-rp82", 179),
          ("regesta-1", 180),
          ("teldat-f1plus", 181),
          ("teldat-l1plus", 183),
          ("regesta-rp61er", 184),
          ("regesta-rp62er", 185),
          ("teldat-3geplus", 186),
          ("atlas-60", 187),
          ("teldat-3geplus-cdma", 188),
          ("teldat-h1auto-plus", 189),
          ("teldat-k", 190),
          ("teldat-v", 191),
          ("connect-104", 192),
          ("teldat-h1rail", 193),
          ("teldat-kf", 194),
          ("teldat-m1", 199),
          ("teldat-m1f", 200),
          ("teldat-4Ge", 201),
          ("oa5710v", 202),
          ("oa5720", 203),
          ("oa5840", 204),
          ("oa5850", 205),
          ("oa5725r61er", 206),
          ("oa5725r62er", 207),
          ("oa5725a3g", 208),
          ("oa5725alte", 209),
          ("esrwwanenabler", 210),
          ("connect-104v", 211),
          ("connect-104kf", 212),
          ("connect-4ge", 213),
          ("bintecrsc", 214),
          ("regesta-lite", 215),
          ("bintecrvc", 216),
          ("teldat-h2auto", 217),
          ("teldat-im8", 219),
          ("teldat-im8plus", 220),
          ("teldat-h2auto-plus", 221),
          ("regesta-plc", 222),
          ("atlasi70", 223),
          ("atlasi70plus", 224),
          ("teldat-h2rail-lite", 225),
          ("teldat-h2rail-lite2", 226),
          ("teldat-h2rail", 227),
          ("regesta-compact-plc", 229))
    )


_TelAdminStatusSystemCode_Type.__name__ = "Integer32"
_TelAdminStatusSystemCode_Object = MibScalar
telAdminStatusSystemCode = _TelAdminStatusSystemCode_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 1, 1),
    _TelAdminStatusSystemCode_Type()
)
telAdminStatusSystemCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusSystemCode.setStatus("mandatory")


class _TelAdminStatusSystemSwLicLev_Type(Integer32):
    """Custom type telAdminStatusSystemSwLicLev based on Integer32"""
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
              45)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("teldatC", 1),
          ("atlas", 2),
          ("visornet", 3),
          ("teldatS", 4),
          ("teldatG", 5),
          ("atlas2G", 6),
          ("atlas150", 7),
          ("teldatA", 8),
          ("atlas50", 9),
          ("atlas300", 10),
          ("atlas152", 11),
          ("teldatc1plus", 12),
          ("teldatc8plus", 13),
          ("teldatc9plus", 14),
          ("atlas360", 15),
          ("teldatH1", 16),
          ("atlas260", 17),
          ("atlas160", 18),
          ("teldatt200g", 19),
          ("teldath1auto", 20),
          ("teldatg1n", 21),
          ("teldatc1pluslite", 22),
          ("teldatv1", 23),
          ("teldatH4-teldatl1plus", 24),
          ("teldatt200", 25),
          ("teldath1plus-teldatf1plus-teldat3Geplus", 26),
          ("regestaPro-ER", 27),
          ("atlas60", 28),
          ("teldath1autoplus", 29),
          ("teldatv", 30),
          ("teldatconnect104", 31),
          ("teldatk", 32),
          ("teldathrail", 33),
          ("teldatm1", 34),
          ("teldat4ge", 35),
          ("teldatconnect104v", 36),
          ("teldatconnect104kf", 37),
          ("teldatconnect4ge", 38),
          ("teldath2auto", 39),
          ("teldatim8", 40),
          ("teldatim8plus", 41),
          ("atlasi70", 42),
          ("atlasi70plus", 43),
          ("teldath2autoplus", 44),
          ("teldath2rail", 45))
    )


_TelAdminStatusSystemSwLicLev_Type.__name__ = "Integer32"
_TelAdminStatusSystemSwLicLev_Object = MibScalar
telAdminStatusSystemSwLicLev = _TelAdminStatusSystemSwLicLev_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 1, 2),
    _TelAdminStatusSystemSwLicLev_Type()
)
telAdminStatusSystemSwLicLev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusSystemSwLicLev.setStatus("mandatory")
_TelAdminStatusSystemSwLicSub_Type = Integer32
_TelAdminStatusSystemSwLicSub_Object = MibScalar
telAdminStatusSystemSwLicSub = _TelAdminStatusSystemSwLicSub_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 1, 3),
    _TelAdminStatusSystemSwLicSub_Type()
)
telAdminStatusSystemSwLicSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusSystemSwLicSub.setStatus("mandatory")
_TelAdminStatusSystemNumSerie_Type = Integer32
_TelAdminStatusSystemNumSerie_Object = MibScalar
telAdminStatusSystemNumSerie = _TelAdminStatusSystemNumSerie_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 1, 4),
    _TelAdminStatusSystemNumSerie_Type()
)
telAdminStatusSystemNumSerie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusSystemNumSerie.setStatus("mandatory")
_TelAdminStatusSystemPcbType_Type = DisplayString
_TelAdminStatusSystemPcbType_Object = MibScalar
telAdminStatusSystemPcbType = _TelAdminStatusSystemPcbType_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 1, 5),
    _TelAdminStatusSystemPcbType_Type()
)
telAdminStatusSystemPcbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusSystemPcbType.setStatus("mandatory")
_TelAdminStatusSystemAppVersion_Type = DisplayString
_TelAdminStatusSystemAppVersion_Object = MibScalar
telAdminStatusSystemAppVersion = _TelAdminStatusSystemAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 1, 6),
    _TelAdminStatusSystemAppVersion_Type()
)
telAdminStatusSystemAppVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusSystemAppVersion.setStatus("mandatory")
_TelAdminStatusSystemBootVersion_Type = DisplayString
_TelAdminStatusSystemBootVersion_Object = MibScalar
telAdminStatusSystemBootVersion = _TelAdminStatusSystemBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 1, 7),
    _TelAdminStatusSystemBootVersion_Type()
)
telAdminStatusSystemBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusSystemBootVersion.setStatus("mandatory")


class _TelAdminStatusSystemClock_Type(OctetString):
    """Custom type telAdminStatusSystemClock based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TelAdminStatusSystemClock_Type.__name__ = "OctetString"
_TelAdminStatusSystemClock_Object = MibScalar
telAdminStatusSystemClock = _TelAdminStatusSystemClock_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 1, 8),
    _TelAdminStatusSystemClock_Type()
)
telAdminStatusSystemClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telAdminStatusSystemClock.setStatus("mandatory")


class _TelAdminStatusSystemBoardType_Type(Integer32):
    """Custom type telAdminStatusSystemBoardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              16,
              24,
              32,
              40,
              48,
              56,
              64,
              72,
              80,
              88,
              96,
              112,
              120,
              128,
              136,
              144,
              152,
              160,
              168,
              176,
              184,
              192,
              200,
              208,
              216,
              224,
              272,
              288,
              296,
              304,
              312,
              320,
              328,
              336,
              368,
              376,
              520,
              528,
              536,
              544,
              552,
              560,
              576,
              584,
              592,
              600,
              608,
              616,
              624,
              632,
              640,
              648,
              656,
              664,
              672,
              680,
              688,
              696,
              704,
              712,
              720,
              728,
              736,
              744,
              752,
              760,
              872,
              880)
        )
    )
    namedValues = NamedValues(
        *(("adsl-860", 8),
          ("visornet-860", 16),
          ("h1-autoplus", 24),
          ("adsl-855", 32),
          ("h1-rail", 40),
          ("visornet-2C", 48),
          ("cbra-univ", 56),
          ("atlas", 64),
          ("cbra-dual", 72),
          ("tldt-new-C3", 80),
          ("univ-tjt", 88),
          ("tldt-m", 96),
          ("hermes", 112),
          ("univ-bas", 120),
          ("zeus", 128),
          ("nike", 136),
          ("minos", 144),
          ("pnlp", 152),
          ("hades", 160),
          ("tldt-m-a", 168),
          ("tldt-t200", 176),
          ("univ-tjt-a", 184),
          ("at-h1", 192),
          ("h1-auto", 200),
          ("at-h4", 208),
          ("tldt-t200-w", 216),
          ("h1-like-h2-rail", 224),
          ("ares", 272),
          ("at-160", 288),
          ("iropro", 296),
          ("tldt-k", 304),
          ("tldt-m1", 312),
          ("anteth4g", 320),
          ("tldt-im1", 328),
          ("tldt-im2", 336),
          ("tldt-h2-auto-plus", 368),
          ("tldt-h2-rail", 376),
          ("c1plusl", 520),
          ("v1", 528),
          ("h1plus", 536),
          ("c1plusl-b", 544),
          ("c1plusl-ur2", 552),
          ("c1plusl-annexm", 560),
          ("rp61er", 576),
          ("rp62er", 584),
          ("rp61er-ac", 592),
          ("rp62er-ac", 600),
          ("vdsl2", 608),
          ("rp62er-ur2", 616),
          ("rp61er-ur2", 624),
          ("rp62er-ac-ur2", 632),
          ("rp61er-ac-ur2", 640),
          ("rp62er-bj", 648),
          ("rp61er-bj", 656),
          ("rp62er-ac-bj", 664),
          ("rp61er-ac-bj", 672),
          ("rp62er-j", 680),
          ("rp61er-j", 688),
          ("rp62er-ac-j", 696),
          ("rp61er-ac-j", 704),
          ("rp62er-b", 712),
          ("rp61er-b", 720),
          ("rp62er-ac-b", 728),
          ("rp61er-ac-b", 736),
          ("rp21er", 744),
          ("rp22er", 752),
          ("v1-bj", 760),
          ("rp-plc", 872),
          ("rp-cmp-plc", 880))
    )


_TelAdminStatusSystemBoardType_Type.__name__ = "Integer32"
_TelAdminStatusSystemBoardType_Object = MibScalar
telAdminStatusSystemBoardType = _TelAdminStatusSystemBoardType_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 1, 9),
    _TelAdminStatusSystemBoardType_Type()
)
telAdminStatusSystemBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusSystemBoardType.setStatus("mandatory")
_TelAdminStatusSystemBoardRevision_Type = Integer32
_TelAdminStatusSystemBoardRevision_Object = MibScalar
telAdminStatusSystemBoardRevision = _TelAdminStatusSystemBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 1, 10),
    _TelAdminStatusSystemBoardRevision_Type()
)
telAdminStatusSystemBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusSystemBoardRevision.setStatus("mandatory")


class _TelAdminStatusSystemSmartCard_Type(Integer32):
    """Custom type telAdminStatusSystemSmartCard based on Integer32"""
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


_TelAdminStatusSystemSmartCard_Type.__name__ = "Integer32"
_TelAdminStatusSystemSmartCard_Object = MibScalar
telAdminStatusSystemSmartCard = _TelAdminStatusSystemSmartCard_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 1, 11),
    _TelAdminStatusSystemSmartCard_Type()
)
telAdminStatusSystemSmartCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusSystemSmartCard.setStatus("mandatory")
_TelAdminStatusLedsTable_Object = MibTable
telAdminStatusLedsTable = _TelAdminStatusLedsTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 2)
)
if mibBuilder.loadTexts:
    telAdminStatusLedsTable.setStatus("mandatory")
_TelAdminStatusLedsEntry_Object = MibTableRow
telAdminStatusLedsEntry = _TelAdminStatusLedsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 2, 1)
)
telAdminStatusLedsEntry.setIndexNames(
    (0, "TELDAT-MIB", "telAdminStatusLedNum"),
)
if mibBuilder.loadTexts:
    telAdminStatusLedsEntry.setStatus("mandatory")


class _TelAdminStatusLedNum_Type(Integer32):
    """Custom type telAdminStatusLedNum based on Integer32"""
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
        *(("led-1", 1),
          ("led-2", 2),
          ("led-3", 3),
          ("led-4", 4),
          ("led-5", 5),
          ("led-6", 6),
          ("led-7", 7),
          ("led-8", 8),
          ("led-9", 9),
          ("led-10", 10),
          ("led-11", 11),
          ("led-12", 12),
          ("led-13", 13),
          ("led-14", 14),
          ("led-15", 15),
          ("led-16", 16),
          ("led-17", 17),
          ("led-18", 18),
          ("led-19", 19),
          ("led-20", 20),
          ("led-21", 21),
          ("led-22", 22),
          ("led-23", 23),
          ("led-24", 24))
    )


_TelAdminStatusLedNum_Type.__name__ = "Integer32"
_TelAdminStatusLedNum_Object = MibTableColumn
telAdminStatusLedNum = _TelAdminStatusLedNum_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 2, 1, 1),
    _TelAdminStatusLedNum_Type()
)
telAdminStatusLedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusLedNum.setStatus("mandatory")


class _TelAdminStatusLedStatus_Type(Integer32):
    """Custom type telAdminStatusLedStatus based on Integer32"""
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
        *(("off", 0),
          ("red", 1),
          ("green", 2),
          ("orange", 3))
    )


_TelAdminStatusLedStatus_Type.__name__ = "Integer32"
_TelAdminStatusLedStatus_Object = MibTableColumn
telAdminStatusLedStatus = _TelAdminStatusLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 2, 1, 2),
    _TelAdminStatusLedStatus_Type()
)
telAdminStatusLedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telAdminStatusLedStatus.setStatus("mandatory")
_TelAdminStatusBugsTable_Object = MibTable
telAdminStatusBugsTable = _TelAdminStatusBugsTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 3)
)
if mibBuilder.loadTexts:
    telAdminStatusBugsTable.setStatus("obsolete")
_TelAdminStatusBugsEntry_Object = MibTableRow
telAdminStatusBugsEntry = _TelAdminStatusBugsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 3, 1)
)
telAdminStatusBugsEntry.setIndexNames(
    (0, "TELDAT-MIB", "telAdminStatusBugNum"),
)
if mibBuilder.loadTexts:
    telAdminStatusBugsEntry.setStatus("obsolete")
_TelAdminStatusBugNum_Type = Integer32
_TelAdminStatusBugNum_Object = MibTableColumn
telAdminStatusBugNum = _TelAdminStatusBugNum_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 3, 1, 1),
    _TelAdminStatusBugNum_Type()
)
telAdminStatusBugNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusBugNum.setStatus("obsolete")
_TelAdminStatusBugMsg_Type = DisplayString
_TelAdminStatusBugMsg_Object = MibTableColumn
telAdminStatusBugMsg = _TelAdminStatusBugMsg_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 3, 1, 2),
    _TelAdminStatusBugMsg_Type()
)
telAdminStatusBugMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusBugMsg.setStatus("obsolete")


class _TelAdminStatusBugsClear_Type(Integer32):
    """Custom type telAdminStatusBugsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-delete-bugs", 0),
          ("delete-bugs", 1))
    )


_TelAdminStatusBugsClear_Type.__name__ = "Integer32"
_TelAdminStatusBugsClear_Object = MibScalar
telAdminStatusBugsClear = _TelAdminStatusBugsClear_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 4),
    _TelAdminStatusBugsClear_Type()
)
telAdminStatusBugsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telAdminStatusBugsClear.setStatus("obsolete")


class _TelAdminStatusReload_Type(Integer32):
    """Custom type telAdminStatusReload based on Integer32"""
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
        *(("undefined", 0),
          ("reset", 1),
          ("already-reset", 2),
          ("not-reset", 3))
    )


_TelAdminStatusReload_Type.__name__ = "Integer32"
_TelAdminStatusReload_Object = MibScalar
telAdminStatusReload = _TelAdminStatusReload_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 5),
    _TelAdminStatusReload_Type()
)
telAdminStatusReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telAdminStatusReload.setStatus("mandatory")


class _TelAdminStatusRestart_Type(Integer32):
    """Custom type telAdminStatusRestart based on Integer32"""
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
        *(("undefined", 0),
          ("restart", 1),
          ("restarted", 2),
          ("not-restarted", 3))
    )


_TelAdminStatusRestart_Type.__name__ = "Integer32"
_TelAdminStatusRestart_Object = MibScalar
telAdminStatusRestart = _TelAdminStatusRestart_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 6),
    _TelAdminStatusRestart_Type()
)
telAdminStatusRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telAdminStatusRestart.setStatus("mandatory")


class _TelAdminStatusSaveConfig_Type(Integer32):
    """Custom type telAdminStatusSaveConfig based on Integer32"""
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
        *(("undefined", 0),
          ("save-configuration", 1),
          ("saved-configuration", 2),
          ("not-saved-configuration", 3))
    )


_TelAdminStatusSaveConfig_Type.__name__ = "Integer32"
_TelAdminStatusSaveConfig_Object = MibScalar
telAdminStatusSaveConfig = _TelAdminStatusSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 7),
    _TelAdminStatusSaveConfig_Type()
)
telAdminStatusSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telAdminStatusSaveConfig.setStatus("mandatory")
_TelAdminStatusSram_ObjectIdentity = ObjectIdentity
telAdminStatusSram = _TelAdminStatusSram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 8)
)
_TelAdminStatusSramRecordTable_Object = MibTable
telAdminStatusSramRecordTable = _TelAdminStatusSramRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    telAdminStatusSramRecordTable.setStatus("obsolete")
_TelAdminStatusSramRecordEntry_Object = MibTableRow
telAdminStatusSramRecordEntry = _TelAdminStatusSramRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 8, 1, 1)
)
telAdminStatusSramRecordEntry.setIndexNames(
    (0, "TELDAT-MIB", "sramRecordType"),
    (0, "TELDAT-MIB", "sramRecordSubtype"),
    (0, "TELDAT-MIB", "sramRecordInstance"),
)
if mibBuilder.loadTexts:
    telAdminStatusSramRecordEntry.setStatus("obsolete")
_SramRecordType_Type = Integer32
_SramRecordType_Object = MibTableColumn
sramRecordType = _SramRecordType_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 8, 1, 1, 1),
    _SramRecordType_Type()
)
sramRecordType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sramRecordType.setStatus("obsolete")
_SramRecordSubtype_Type = Integer32
_SramRecordSubtype_Object = MibTableColumn
sramRecordSubtype = _SramRecordSubtype_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 8, 1, 1, 2),
    _SramRecordSubtype_Type()
)
sramRecordSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sramRecordSubtype.setStatus("obsolete")
_SramRecordInstance_Type = Integer32
_SramRecordInstance_Object = MibTableColumn
sramRecordInstance = _SramRecordInstance_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 8, 1, 1, 3),
    _SramRecordInstance_Type()
)
sramRecordInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sramRecordInstance.setStatus("obsolete")
_SramRecordItem_Type = Opaque
_SramRecordItem_Object = MibTableColumn
sramRecordItem = _SramRecordItem_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 8, 1, 1, 4),
    _SramRecordItem_Type()
)
sramRecordItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sramRecordItem.setStatus("obsolete")
_TelAdminStatusSRE_ObjectIdentity = ObjectIdentity
telAdminStatusSRE = _TelAdminStatusSRE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9)
)
_TelAdminStatusSRESubRecordTable_Object = MibTable
telAdminStatusSRESubRecordTable = _TelAdminStatusSRESubRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    telAdminStatusSRESubRecordTable.setStatus("mandatory")
_TelAdminStatusSRESubRecordEntry_Object = MibTableRow
telAdminStatusSRESubRecordEntry = _TelAdminStatusSRESubRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 1, 1)
)
telAdminStatusSRESubRecordEntry.setIndexNames(
    (0, "TELDAT-MIB", "sreSubId"),
)
if mibBuilder.loadTexts:
    telAdminStatusSRESubRecordEntry.setStatus("mandatory")
_SreSubId_Type = Integer32
_SreSubId_Object = MibTableColumn
sreSubId = _SreSubId_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 1, 1, 1),
    _SreSubId_Type()
)
sreSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreSubId.setStatus("mandatory")
_SreSubShortName_Type = DisplayString
_SreSubShortName_Object = MibTableColumn
sreSubShortName = _SreSubShortName_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 1, 1, 2),
    _SreSubShortName_Type()
)
sreSubShortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreSubShortName.setStatus("mandatory")
_SreSubLongName_Type = DisplayString
_SreSubLongName_Object = MibTableColumn
sreSubLongName = _SreSubLongName_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 1, 1, 3),
    _SreSubLongName_Type()
)
sreSubLongName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreSubLongName.setStatus("mandatory")
_SreSubNumEvent_Type = Integer32
_SreSubNumEvent_Object = MibTableColumn
sreSubNumEvent = _SreSubNumEvent_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 1, 1, 4),
    _SreSubNumEvent_Type()
)
sreSubNumEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreSubNumEvent.setStatus("mandatory")


class _SreSubTraceLvlConf_Type(Integer32):
    """Custom type sreSubTraceLvlConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SreSubTraceLvlConf_Type.__name__ = "Integer32"
_SreSubTraceLvlConf_Object = MibTableColumn
sreSubTraceLvlConf = _SreSubTraceLvlConf_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 1, 1, 5),
    _SreSubTraceLvlConf_Type()
)
sreSubTraceLvlConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sreSubTraceLvlConf.setStatus("mandatory")


class _SreSubSyslogLvlConf_Type(Integer32):
    """Custom type sreSubSyslogLvlConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SreSubSyslogLvlConf_Type.__name__ = "Integer32"
_SreSubSyslogLvlConf_Object = MibTableColumn
sreSubSyslogLvlConf = _SreSubSyslogLvlConf_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 1, 1, 6),
    _SreSubSyslogLvlConf_Type()
)
sreSubSyslogLvlConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sreSubSyslogLvlConf.setStatus("mandatory")


class _SreSubTrapLvlConf_Type(Integer32):
    """Custom type sreSubTrapLvlConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SreSubTrapLvlConf_Type.__name__ = "Integer32"
_SreSubTrapLvlConf_Object = MibTableColumn
sreSubTrapLvlConf = _SreSubTrapLvlConf_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 1, 1, 7),
    _SreSubTrapLvlConf_Type()
)
sreSubTrapLvlConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sreSubTrapLvlConf.setStatus("mandatory")


class _SreSubTrap1LvlConf_Type(Integer32):
    """Custom type sreSubTrap1LvlConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SreSubTrap1LvlConf_Type.__name__ = "Integer32"
_SreSubTrap1LvlConf_Object = MibTableColumn
sreSubTrap1LvlConf = _SreSubTrap1LvlConf_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 1, 1, 8),
    _SreSubTrap1LvlConf_Type()
)
sreSubTrap1LvlConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sreSubTrap1LvlConf.setStatus("mandatory")


class _SreSubTrap2LvlConf_Type(Integer32):
    """Custom type sreSubTrap2LvlConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SreSubTrap2LvlConf_Type.__name__ = "Integer32"
_SreSubTrap2LvlConf_Object = MibTableColumn
sreSubTrap2LvlConf = _SreSubTrap2LvlConf_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 1, 1, 9),
    _SreSubTrap2LvlConf_Type()
)
sreSubTrap2LvlConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sreSubTrap2LvlConf.setStatus("mandatory")


class _SreSubTrap3LvlConf_Type(Integer32):
    """Custom type sreSubTrap3LvlConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SreSubTrap3LvlConf_Type.__name__ = "Integer32"
_SreSubTrap3LvlConf_Object = MibTableColumn
sreSubTrap3LvlConf = _SreSubTrap3LvlConf_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 1, 1, 10),
    _SreSubTrap3LvlConf_Type()
)
sreSubTrap3LvlConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sreSubTrap3LvlConf.setStatus("mandatory")


class _SreSubTrap4LvlConf_Type(Integer32):
    """Custom type sreSubTrap4LvlConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SreSubTrap4LvlConf_Type.__name__ = "Integer32"
_SreSubTrap4LvlConf_Object = MibTableColumn
sreSubTrap4LvlConf = _SreSubTrap4LvlConf_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 1, 1, 11),
    _SreSubTrap4LvlConf_Type()
)
sreSubTrap4LvlConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sreSubTrap4LvlConf.setStatus("mandatory")
_TelAdminStatusSREEventRecordTable_Object = MibTable
telAdminStatusSREEventRecordTable = _TelAdminStatusSREEventRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    telAdminStatusSREEventRecordTable.setStatus("mandatory")
_TelAdminStatusSREEventRecordEntry_Object = MibTableRow
telAdminStatusSREEventRecordEntry = _TelAdminStatusSREEventRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 2, 1)
)
telAdminStatusSREEventRecordEntry.setIndexNames(
    (0, "TELDAT-MIB", "sreEvnSubId"),
    (0, "TELDAT-MIB", "sreEvnEvnId"),
)
if mibBuilder.loadTexts:
    telAdminStatusSREEventRecordEntry.setStatus("mandatory")
_SreEvnSubId_Type = Integer32
_SreEvnSubId_Object = MibTableColumn
sreEvnSubId = _SreEvnSubId_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 2, 1, 1),
    _SreEvnSubId_Type()
)
sreEvnSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreEvnSubId.setStatus("mandatory")
_SreEvnEvnId_Type = Integer32
_SreEvnEvnId_Object = MibTableColumn
sreEvnEvnId = _SreEvnEvnId_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 2, 1, 2),
    _SreEvnEvnId_Type()
)
sreEvnEvnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreEvnEvnId.setStatus("mandatory")
_SreEvnMsg_Type = DisplayString
_SreEvnMsg_Object = MibTableColumn
sreEvnMsg = _SreEvnMsg_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 2, 1, 3),
    _SreEvnMsg_Type()
)
sreEvnMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreEvnMsg.setStatus("mandatory")


class _SreEvnLvl_Type(Integer32):
    """Custom type sreEvnLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SreEvnLvl_Type.__name__ = "Integer32"
_SreEvnLvl_Object = MibTableColumn
sreEvnLvl = _SreEvnLvl_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 2, 1, 4),
    _SreEvnLvl_Type()
)
sreEvnLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreEvnLvl.setStatus("mandatory")
_SreEvnMeter_Type = Counter32
_SreEvnMeter_Object = MibTableColumn
sreEvnMeter = _SreEvnMeter_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 2, 1, 5),
    _SreEvnMeter_Type()
)
sreEvnMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreEvnMeter.setStatus("mandatory")


class _SreEvnStatusAct_Type(Integer32):
    """Custom type sreEvnStatusAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SreEvnStatusAct_Type.__name__ = "Integer32"
_SreEvnStatusAct_Object = MibTableColumn
sreEvnStatusAct = _SreEvnStatusAct_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 2, 1, 6),
    _SreEvnStatusAct_Type()
)
sreEvnStatusAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sreEvnStatusAct.setStatus("mandatory")


class _SreEvnStatusCon_Type(Integer32):
    """Custom type sreEvnStatusCon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SreEvnStatusCon_Type.__name__ = "Integer32"
_SreEvnStatusCon_Object = MibTableColumn
sreEvnStatusCon = _SreEvnStatusCon_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 2, 1, 7),
    _SreEvnStatusCon_Type()
)
sreEvnStatusCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sreEvnStatusCon.setStatus("mandatory")
_TelAdminStatusSREGroupRecordTable_Object = MibTable
telAdminStatusSREGroupRecordTable = _TelAdminStatusSREGroupRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3)
)
if mibBuilder.loadTexts:
    telAdminStatusSREGroupRecordTable.setStatus("mandatory")
_TelAdminStatusSREGroupRecordEntry_Object = MibTableRow
telAdminStatusSREGroupRecordEntry = _TelAdminStatusSREGroupRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1)
)
telAdminStatusSREGroupRecordEntry.setIndexNames(
    (0, "TELDAT-MIB", "sreGrpId"),
)
if mibBuilder.loadTexts:
    telAdminStatusSREGroupRecordEntry.setStatus("mandatory")
_SreGrpId_Type = Integer32
_SreGrpId_Object = MibTableColumn
sreGrpId = _SreGrpId_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 1),
    _SreGrpId_Type()
)
sreGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpId.setStatus("mandatory")
_SreGrpName_Type = DisplayString
_SreGrpName_Object = MibTableColumn
sreGrpName = _SreGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 2),
    _SreGrpName_Type()
)
sreGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpName.setStatus("mandatory")


class _SreGrpStatusCon_Type(Integer32):
    """Custom type sreGrpStatusCon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SreGrpStatusCon_Type.__name__ = "Integer32"
_SreGrpStatusCon_Object = MibTableColumn
sreGrpStatusCon = _SreGrpStatusCon_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 3),
    _SreGrpStatusCon_Type()
)
sreGrpStatusCon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sreGrpStatusCon.setStatus("mandatory")
_SreGrpGrpSub1Id_Type = Integer32
_SreGrpGrpSub1Id_Object = MibTableColumn
sreGrpGrpSub1Id = _SreGrpGrpSub1Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 4),
    _SreGrpGrpSub1Id_Type()
)
sreGrpGrpSub1Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub1Id.setStatus("mandatory")
_SreGrpGrpEvn1Id_Type = Integer32
_SreGrpGrpEvn1Id_Object = MibTableColumn
sreGrpGrpEvn1Id = _SreGrpGrpEvn1Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 5),
    _SreGrpGrpEvn1Id_Type()
)
sreGrpGrpEvn1Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn1Id.setStatus("mandatory")
_SreGrpGrpSub2Id_Type = Integer32
_SreGrpGrpSub2Id_Object = MibTableColumn
sreGrpGrpSub2Id = _SreGrpGrpSub2Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 6),
    _SreGrpGrpSub2Id_Type()
)
sreGrpGrpSub2Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub2Id.setStatus("mandatory")
_SreGrpGrpEvn2Id_Type = Integer32
_SreGrpGrpEvn2Id_Object = MibTableColumn
sreGrpGrpEvn2Id = _SreGrpGrpEvn2Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 7),
    _SreGrpGrpEvn2Id_Type()
)
sreGrpGrpEvn2Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn2Id.setStatus("mandatory")
_SreGrpGrpSub3Id_Type = Integer32
_SreGrpGrpSub3Id_Object = MibTableColumn
sreGrpGrpSub3Id = _SreGrpGrpSub3Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 8),
    _SreGrpGrpSub3Id_Type()
)
sreGrpGrpSub3Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub3Id.setStatus("mandatory")
_SreGrpGrpEvn3Id_Type = Integer32
_SreGrpGrpEvn3Id_Object = MibTableColumn
sreGrpGrpEvn3Id = _SreGrpGrpEvn3Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 9),
    _SreGrpGrpEvn3Id_Type()
)
sreGrpGrpEvn3Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn3Id.setStatus("mandatory")
_SreGrpGrpSub4Id_Type = Integer32
_SreGrpGrpSub4Id_Object = MibTableColumn
sreGrpGrpSub4Id = _SreGrpGrpSub4Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 10),
    _SreGrpGrpSub4Id_Type()
)
sreGrpGrpSub4Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub4Id.setStatus("mandatory")
_SreGrpGrpEvn4Id_Type = Integer32
_SreGrpGrpEvn4Id_Object = MibTableColumn
sreGrpGrpEvn4Id = _SreGrpGrpEvn4Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 11),
    _SreGrpGrpEvn4Id_Type()
)
sreGrpGrpEvn4Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn4Id.setStatus("mandatory")
_SreGrpGrpSub5Id_Type = Integer32
_SreGrpGrpSub5Id_Object = MibTableColumn
sreGrpGrpSub5Id = _SreGrpGrpSub5Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 12),
    _SreGrpGrpSub5Id_Type()
)
sreGrpGrpSub5Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub5Id.setStatus("mandatory")
_SreGrpGrpEvn5Id_Type = Integer32
_SreGrpGrpEvn5Id_Object = MibTableColumn
sreGrpGrpEvn5Id = _SreGrpGrpEvn5Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 13),
    _SreGrpGrpEvn5Id_Type()
)
sreGrpGrpEvn5Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn5Id.setStatus("mandatory")
_SreGrpGrpSub6Id_Type = Integer32
_SreGrpGrpSub6Id_Object = MibTableColumn
sreGrpGrpSub6Id = _SreGrpGrpSub6Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 14),
    _SreGrpGrpSub6Id_Type()
)
sreGrpGrpSub6Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub6Id.setStatus("mandatory")
_SreGrpGrpEvn6Id_Type = Integer32
_SreGrpGrpEvn6Id_Object = MibTableColumn
sreGrpGrpEvn6Id = _SreGrpGrpEvn6Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 15),
    _SreGrpGrpEvn6Id_Type()
)
sreGrpGrpEvn6Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn6Id.setStatus("mandatory")
_SreGrpGrpSub7Id_Type = Integer32
_SreGrpGrpSub7Id_Object = MibTableColumn
sreGrpGrpSub7Id = _SreGrpGrpSub7Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 16),
    _SreGrpGrpSub7Id_Type()
)
sreGrpGrpSub7Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub7Id.setStatus("mandatory")
_SreGrpGrpEvn7Id_Type = Integer32
_SreGrpGrpEvn7Id_Object = MibTableColumn
sreGrpGrpEvn7Id = _SreGrpGrpEvn7Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 17),
    _SreGrpGrpEvn7Id_Type()
)
sreGrpGrpEvn7Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn7Id.setStatus("mandatory")
_SreGrpGrpSub8Id_Type = Integer32
_SreGrpGrpSub8Id_Object = MibTableColumn
sreGrpGrpSub8Id = _SreGrpGrpSub8Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 18),
    _SreGrpGrpSub8Id_Type()
)
sreGrpGrpSub8Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub8Id.setStatus("mandatory")
_SreGrpGrpEvn8Id_Type = Integer32
_SreGrpGrpEvn8Id_Object = MibTableColumn
sreGrpGrpEvn8Id = _SreGrpGrpEvn8Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 19),
    _SreGrpGrpEvn8Id_Type()
)
sreGrpGrpEvn8Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn8Id.setStatus("mandatory")
_SreGrpGrpSub9Id_Type = Integer32
_SreGrpGrpSub9Id_Object = MibTableColumn
sreGrpGrpSub9Id = _SreGrpGrpSub9Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 20),
    _SreGrpGrpSub9Id_Type()
)
sreGrpGrpSub9Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub9Id.setStatus("mandatory")
_SreGrpGrpEvn9Id_Type = Integer32
_SreGrpGrpEvn9Id_Object = MibTableColumn
sreGrpGrpEvn9Id = _SreGrpGrpEvn9Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 21),
    _SreGrpGrpEvn9Id_Type()
)
sreGrpGrpEvn9Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn9Id.setStatus("mandatory")
_SreGrpGrpSub10Id_Type = Integer32
_SreGrpGrpSub10Id_Object = MibTableColumn
sreGrpGrpSub10Id = _SreGrpGrpSub10Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 22),
    _SreGrpGrpSub10Id_Type()
)
sreGrpGrpSub10Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub10Id.setStatus("mandatory")
_SreGrpGrpEvn10Id_Type = Integer32
_SreGrpGrpEvn10Id_Object = MibTableColumn
sreGrpGrpEvn10Id = _SreGrpGrpEvn10Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 23),
    _SreGrpGrpEvn10Id_Type()
)
sreGrpGrpEvn10Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn10Id.setStatus("mandatory")
_SreGrpGrpSub11Id_Type = Integer32
_SreGrpGrpSub11Id_Object = MibTableColumn
sreGrpGrpSub11Id = _SreGrpGrpSub11Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 24),
    _SreGrpGrpSub11Id_Type()
)
sreGrpGrpSub11Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub11Id.setStatus("mandatory")
_SreGrpGrpEvn11Id_Type = Integer32
_SreGrpGrpEvn11Id_Object = MibTableColumn
sreGrpGrpEvn11Id = _SreGrpGrpEvn11Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 25),
    _SreGrpGrpEvn11Id_Type()
)
sreGrpGrpEvn11Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn11Id.setStatus("mandatory")
_SreGrpGrpSub12Id_Type = Integer32
_SreGrpGrpSub12Id_Object = MibTableColumn
sreGrpGrpSub12Id = _SreGrpGrpSub12Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 26),
    _SreGrpGrpSub12Id_Type()
)
sreGrpGrpSub12Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub12Id.setStatus("mandatory")
_SreGrpGrpEvn12Id_Type = Integer32
_SreGrpGrpEvn12Id_Object = MibTableColumn
sreGrpGrpEvn12Id = _SreGrpGrpEvn12Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 27),
    _SreGrpGrpEvn12Id_Type()
)
sreGrpGrpEvn12Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn12Id.setStatus("mandatory")
_SreGrpGrpSub13Id_Type = Integer32
_SreGrpGrpSub13Id_Object = MibTableColumn
sreGrpGrpSub13Id = _SreGrpGrpSub13Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 28),
    _SreGrpGrpSub13Id_Type()
)
sreGrpGrpSub13Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub13Id.setStatus("mandatory")
_SreGrpGrpEvn13Id_Type = Integer32
_SreGrpGrpEvn13Id_Object = MibTableColumn
sreGrpGrpEvn13Id = _SreGrpGrpEvn13Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 29),
    _SreGrpGrpEvn13Id_Type()
)
sreGrpGrpEvn13Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn13Id.setStatus("mandatory")
_SreGrpGrpSub14Id_Type = Integer32
_SreGrpGrpSub14Id_Object = MibTableColumn
sreGrpGrpSub14Id = _SreGrpGrpSub14Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 30),
    _SreGrpGrpSub14Id_Type()
)
sreGrpGrpSub14Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub14Id.setStatus("mandatory")
_SreGrpGrpEvn14Id_Type = Integer32
_SreGrpGrpEvn14Id_Object = MibTableColumn
sreGrpGrpEvn14Id = _SreGrpGrpEvn14Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 31),
    _SreGrpGrpEvn14Id_Type()
)
sreGrpGrpEvn14Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn14Id.setStatus("mandatory")
_SreGrpGrpSub15Id_Type = Integer32
_SreGrpGrpSub15Id_Object = MibTableColumn
sreGrpGrpSub15Id = _SreGrpGrpSub15Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 32),
    _SreGrpGrpSub15Id_Type()
)
sreGrpGrpSub15Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub15Id.setStatus("mandatory")
_SreGrpGrpEvn15Id_Type = Integer32
_SreGrpGrpEvn15Id_Object = MibTableColumn
sreGrpGrpEvn15Id = _SreGrpGrpEvn15Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 33),
    _SreGrpGrpEvn15Id_Type()
)
sreGrpGrpEvn15Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn15Id.setStatus("mandatory")
_SreGrpGrpSub16Id_Type = Integer32
_SreGrpGrpSub16Id_Object = MibTableColumn
sreGrpGrpSub16Id = _SreGrpGrpSub16Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 34),
    _SreGrpGrpSub16Id_Type()
)
sreGrpGrpSub16Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub16Id.setStatus("mandatory")
_SreGrpGrpEvn16Id_Type = Integer32
_SreGrpGrpEvn16Id_Object = MibTableColumn
sreGrpGrpEvn16Id = _SreGrpGrpEvn16Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 35),
    _SreGrpGrpEvn16Id_Type()
)
sreGrpGrpEvn16Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn16Id.setStatus("mandatory")
_SreGrpGrpSub17Id_Type = Integer32
_SreGrpGrpSub17Id_Object = MibTableColumn
sreGrpGrpSub17Id = _SreGrpGrpSub17Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 36),
    _SreGrpGrpSub17Id_Type()
)
sreGrpGrpSub17Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub17Id.setStatus("mandatory")
_SreGrpGrpEvn17Id_Type = Integer32
_SreGrpGrpEvn17Id_Object = MibTableColumn
sreGrpGrpEvn17Id = _SreGrpGrpEvn17Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 37),
    _SreGrpGrpEvn17Id_Type()
)
sreGrpGrpEvn17Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn17Id.setStatus("mandatory")
_SreGrpGrpSub18Id_Type = Integer32
_SreGrpGrpSub18Id_Object = MibTableColumn
sreGrpGrpSub18Id = _SreGrpGrpSub18Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 38),
    _SreGrpGrpSub18Id_Type()
)
sreGrpGrpSub18Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub18Id.setStatus("mandatory")
_SreGrpGrpEvn18Id_Type = Integer32
_SreGrpGrpEvn18Id_Object = MibTableColumn
sreGrpGrpEvn18Id = _SreGrpGrpEvn18Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 39),
    _SreGrpGrpEvn18Id_Type()
)
sreGrpGrpEvn18Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn18Id.setStatus("mandatory")
_SreGrpGrpSub19Id_Type = Integer32
_SreGrpGrpSub19Id_Object = MibTableColumn
sreGrpGrpSub19Id = _SreGrpGrpSub19Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 40),
    _SreGrpGrpSub19Id_Type()
)
sreGrpGrpSub19Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub19Id.setStatus("mandatory")
_SreGrpGrpEvn19Id_Type = Integer32
_SreGrpGrpEvn19Id_Object = MibTableColumn
sreGrpGrpEvn19Id = _SreGrpGrpEvn19Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 41),
    _SreGrpGrpEvn19Id_Type()
)
sreGrpGrpEvn19Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn19Id.setStatus("mandatory")
_SreGrpGrpSub20Id_Type = Integer32
_SreGrpGrpSub20Id_Object = MibTableColumn
sreGrpGrpSub20Id = _SreGrpGrpSub20Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 42),
    _SreGrpGrpSub20Id_Type()
)
sreGrpGrpSub20Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpSub20Id.setStatus("mandatory")
_SreGrpGrpEvn20Id_Type = Integer32
_SreGrpGrpEvn20Id_Object = MibTableColumn
sreGrpGrpEvn20Id = _SreGrpGrpEvn20Id_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 3, 1, 43),
    _SreGrpGrpEvn20Id_Type()
)
sreGrpGrpEvn20Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sreGrpGrpEvn20Id.setStatus("mandatory")


class _TelAdminStatusSREClearConf_Type(Integer32):
    """Custom type telAdminStatusSREClearConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("with-configuration", 0),
          ("without-configuration", 1))
    )


_TelAdminStatusSREClearConf_Type.__name__ = "Integer32"
_TelAdminStatusSREClearConf_Object = MibScalar
telAdminStatusSREClearConf = _TelAdminStatusSREClearConf_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 9, 4),
    _TelAdminStatusSREClearConf_Type()
)
telAdminStatusSREClearConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telAdminStatusSREClearConf.setStatus("mandatory")
_TelAdminStatusIfTable_Object = MibTable
telAdminStatusIfTable = _TelAdminStatusIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 10)
)
if mibBuilder.loadTexts:
    telAdminStatusIfTable.setStatus("mandatory")
_TelAdminStatusIfEntry_Object = MibTableRow
telAdminStatusIfEntry = _TelAdminStatusIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 10, 1)
)
telAdminStatusIfEntry.setIndexNames(
    (0, "TELDAT-MIB", "telAdminStatusIfIndex"),
)
if mibBuilder.loadTexts:
    telAdminStatusIfEntry.setStatus("mandatory")
_TelAdminStatusIfIndex_Type = Integer32
_TelAdminStatusIfIndex_Object = MibTableColumn
telAdminStatusIfIndex = _TelAdminStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 10, 1, 1),
    _TelAdminStatusIfIndex_Type()
)
telAdminStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusIfIndex.setStatus("mandatory")


class _TelAdminStatusIfType_Type(Integer32):
    """Custom type telAdminStatusIfType based on Integer32"""
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
              61441,
              61442,
              61443,
              61444,
              61445,
              61446)
        )
    )
    namedValues = NamedValues(
        *(("sr-MICRO-NODE-X25-NET", 1),
          ("sr-PCI-WAN-PQ2-SDLC", 2),
          ("sr-MICRO-NODE-ISAC-NET", 3),
          ("sr-MICRO-NODE-XOT-NET", 4),
          ("sr-MICRO-NODE-270-NET", 5),
          ("sr-COM4", 6),
          ("sr-PRO4", 7),
          ("sr-IBD", 8),
          ("sr-PCI-AMDETH", 9),
          ("sr-AMDETH", 10),
          ("sr-QUIC-SL-X28", 11),
          ("sr-QUIC-SL-ASTM", 12),
          ("sr-QUIC-SL-UDAFO", 13),
          ("sr-FASTETH", 14),
          ("sr-VCOM4", 15),
          ("sr-dummy-voip", 16),
          ("sr-PCI-CELLULAR-VOIP", 17),
          ("sr-ATC2", 18),
          ("sr-DIAL-G-HDLC", 19),
          ("sr-DIAL-G-FR", 20),
          ("sr-DIAL-G-PPP", 21),
          ("sr-DIAL-G-X25", 22),
          ("sr-SRLY-GWSL", 23),
          ("sr-SRLY-ATC2", 24),
          ("sr-SRLY-G1SL", 25),
          ("sr-FRGENSL", 26),
          ("sr-NSETH", 27),
          ("sr-TELDAT-BVI-SUBIFC", 28),
          ("sr-TELDAT-FR-SUBIFC", 29),
          ("sr-PPPGENSL", 30),
          ("sr-PPPATC2", 31),
          ("sr-PPPCOM2", 32),
          ("sr-QSL", 33),
          ("sr-PPPQSL", 34),
          ("sr-FRQSL", 35),
          ("sr-SRLY-QSL", 36),
          ("sr-XQSL", 37),
          ("sr-NULL-DEV", 38),
          ("sr-YDC-ISDN", 39),
          ("sr-DIAL-FR", 40),
          ("sr-DIAL-PPP", 41),
          ("sr-QUIC-PRI-SIG", 42),
          ("sr-SDLC-QSL", 43),
          ("sr-QSLCH", 44),
          ("sr-SDLC-QSLCH", 45),
          ("sr-PPP-QSLCH", 46),
          ("sr-FR-QSLCH", 47),
          ("sr-XQSLCH", 48),
          ("sr-SRLY-QSLCH", 49),
          ("sr-PCI-PRI-ACODES", 50),
          ("sr-PCI-BRI-ACODES", 51),
          ("sr-ISDN-VOIP", 52),
          ("sr-SL-HSSI", 53),
          ("sr-FR-HSSI", 54),
          ("sr-PPP-HSSI", 55),
          ("sr-QUIC-ETH", 56),
          ("sr-QUIC-TKR", 57),
          ("sr-QUIC-SL-PSL", 58),
          ("sr-QUIC-SL-PPP", 59),
          ("sr-QUIC-SL-X25", 60),
          ("sr-QUIC-SL-FR", 61),
          ("sr-QUIC-SL-SRLY", 62),
          ("sr-QUIC-SL-SDLC", 63),
          ("sr-QUIC-SL-V25B", 64),
          ("sr-QUIC-ISDNH", 65),
          ("sr-TEL-PRU", 66),
          ("sr-TEL-PRU-FAST", 67),
          ("sr-TEL-MOTOROLA", 68),
          ("sr-TELDAT-TKR", 69),
          ("sr-TELDAT-ETH", 70),
          ("sr-TELDAT-ISAC", 71),
          ("sr-TELDAT-XOT", 72),
          ("sr-TELDAT-270", 73),
          ("sr-TELDAT-TNIP", 74),
          ("sr-TELDAT-MPPP", 75),
          ("sr-FR-ISDN", 76),
          ("sr-TELDAT-ATM", 77),
          ("sr-TELDAT-ATM-SUBIFC", 78),
          ("sr-TELDAT-ASDP", 79),
          ("sr-QMC-BRI", 80),
          ("sr-TELDAT-SYNC-SL", 81),
          ("sr-TELDAT-ASYNC-SL", 82),
          ("sr-QUIC-SL-APTB", 83),
          ("sr-TELDAT-ATM-FS", 84),
          ("sr-TELDAT-LPBK", 85),
          ("sr-TELDAT-PCI-PRI-M32X", 86),
          ("sr-TELDAT-DIALROUT", 87),
          ("sr-PCI-WAN-PQ2-ASYNC", 88),
          ("sr-DSCC4-ATC2", 89),
          ("sr-PCI-WAN-PQ2-SYN", 90),
          ("sr-PCI-AMD-MICREL-ETH", 91),
          ("sr-MOT-MICREL-ETH", 92),
          ("sr-ALARM-RELY", 93),
          ("sr-PCI-MEMORY-CARD", 94),
          ("sr-TELDAT-ETH-SUBIFC", 95),
          ("sr-PCI-POTS-VOIP-CARD", 96),
          ("sr-PCI-BRI-VOIP-CARD", 97),
          ("sr-PCI-PRI-VOIP-CARD", 98),
          ("sr-PCI-E-M-VOIP-CARD", 99),
          ("sr-TELDAT-LOOPBACK", 100),
          ("sr-TELDAT-L2TP", 101),
          ("sr-FCC-ETH", 102),
          ("sr-PCMCIA-SERIAL", 103),
          ("sr-DSCC4-HSSI", 104),
          ("sr-TELDAT-BVI", 105),
          ("sr-QUIC-SL-SCADA", 106),
          ("sr-TELDAT-ATM-PQ2SAR", 107),
          ("sr-PCI-QMC-BRI", 108),
          ("sr-PCI-POTS-3S10VOIP-CARD", 109),
          ("sr-PCI-POTS-2S2OVOIP-CARD", 110),
          ("sr-PCI-INTEL-GIGABIT-ETH", 111),
          ("sr-ATHEROS-WLAN-BASE", 112),
          ("sr-FCC-MARVELL", 113),
          ("sr-TELDAT-SEPI", 114),
          ("sr-FCC-MICREL", 115),
          ("sr-ETSEC-ETH", 116),
          ("sr-EIB-ZENNIO", 117),
          ("sr-GPIO-12", 118),
          ("sr-QUIC-AUTO-INST-SL", 119),
          ("sr-PCI-PRI-PQ2", 120),
          ("sr-ETSEC-MARVELL-ETH", 121),
          ("sr-QUIC-SL-MODEMEMU", 122),
          ("sr-PCI-VALARM-SL-MDMEMU", 123),
          ("sr-PCI-VALARM-SL-SEPI", 124),
          ("sr-PCI-CELLULAR", 125),
          ("sr-REMOTE-CELLULAR", 126),
          ("sr-PCI-WAN-PQ2-SCADA", 127),
          ("sr-TELDAT-ETH-SOFTETH", 128),
          ("sr-TELDAT-ATM-SOFTSAR", 129),
          ("sr-PCI-PQII-FCC-MARVELL-ETH", 130),
          ("sr-TELDAT-ETH-SOFTPTM", 131),
          ("sr-TELDAT-SERIAL-SOFTUSB", 132),
          ("sr-PCI-PQII-WDMPON", 133),
          ("sr-TELDAT-SOFTWLAN-BASE", 134),
          ("sr-PCI-WAN-PQ2-ASTM", 135),
          ("sr-PCI-WAN-PQ2-X28", 136),
          ("sr-PCI-WAN-PQ2-ASDP", 137),
          ("sr-TELDAT-SOFTNIC", 138),
          ("sr-DIAL-G-DIP", 139),
          ("sr-TELDAT-USBNIC", 140),
          ("sr-ATHEROS-WLAN-VAP", 141),
          ("sr-TELDAT-SOFTWAN", 142),
          ("sr-TELDAT-SWETH", 143),
          ("sr-QUIC-SL-IEC101GW", 144),
          ("sr-PCI-WAN-PQ2-IEC101GW", 145),
          ("sr-TELDAT-SOFTUART", 146),
          ("sr-TELDAT-SOFTSCADA", 147),
          ("sr-TELDAT-SOFTIEC101GW", 148),
          ("sr-TELDAT-SOFTASDP", 149),
          ("sr-STANDALONE-GPS", 150),
          ("sr-SL-GPSDATA", 151),
          ("sr-SOFTWLAN-VAP", 152),
          ("sr-FSL-CELLULAR", 153),
          ("sr-SOFTETH-SWITCH", 154),
          ("sr-TELDAT-USBETH", 155),
          ("sr-TELDAT-SOFTUSBETH", 156),
          ("sr-TELDAT-ETH-FMAN", 157),
          ("sr-TELDAT-ETH-FMAN-SWITCH", 158),
          ("sr-TELDAT-SOFTPRIME", 159),
          ("sr-FSL-GPSUSB", 160),
          ("sr-TELDAT-ETH-FMAN-MII", 161),
          ("sr-XHCI-CELLULAR", 162),
          ("sr-MICRO-NODE-ROUTER", 61441),
          ("sr-MICRO-NODE-RDSI-B", 61442),
          ("sr-MICRO-NODE-ISAC", 61443),
          ("sr-MICRO-NODE-X25", 61444),
          ("sr-MICRO-NODE-XOT", 61445),
          ("sr-MICRO-NODE-270", 61446))
    )


_TelAdminStatusIfType_Type.__name__ = "Integer32"
_TelAdminStatusIfType_Object = MibTableColumn
telAdminStatusIfType = _TelAdminStatusIfType_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 10, 1, 2),
    _TelAdminStatusIfType_Type()
)
telAdminStatusIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusIfType.setStatus("mandatory")


class _TelAdminStatusIfCon_Type(Integer32):
    """Custom type telAdminStatusIfCon based on Integer32"""
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
              54)
        )
    )
    namedValues = NamedValues(
        *(("no-conn", 0),
          ("lan-conn", 1),
          ("wan1-conn", 2),
          ("wan2-conn", 3),
          ("wan3-conn", 4),
          ("wan4-conn", 5),
          ("wan5-conn", 6),
          ("wan6-conn", 7),
          ("wan7-conn", 8),
          ("wan8-conn", 9),
          ("rdsi1-conn", 10),
          ("rdsi2-conn", 11),
          ("adsl1-conn", 12),
          ("adsl2-conn", 13),
          ("adsl3-conn", 14),
          ("adsl4-conn", 15),
          ("lan-conn-exp", 16),
          ("uart1-conn", 17),
          ("uart2-conn", 18),
          ("uart3-conn", 19),
          ("uart4-conn", 20),
          ("rs232-conn", 21),
          ("rs485-conn", 22),
          ("slot1-conn", 23),
          ("slot2-conn", 24),
          ("slot3-conn", 25),
          ("rf-conn", 26),
          ("lan1-conn", 27),
          ("lan2-conn", 28),
          ("lan3-conn", 29),
          ("lan4-conn", 30),
          ("pots-conn", 31),
          ("slot4-conn", 32),
          ("slot5-conn", 33),
          ("exp-switch1", 34),
          ("usb-conn", 35),
          ("ethwan-conn", 36),
          ("config-conn", 37),
          ("lan1-switch-conn", 38),
          ("irp-slot3-conn", 39),
          ("usb-uart-conn-1", 40),
          ("usb-uart-conn-2", 41),
          ("gps-conn", 42),
          ("rf-conn-1", 43),
          ("rf-conn-2", 44),
          ("usb-conn-1", 45),
          ("usb-conn-2", 46),
          ("irp-slot2-conn", 47),
          ("wifi1-conn", 48),
          ("wifi2-conn", 49),
          ("im-slot1-conn", 50),
          ("im-slot2-conn", 51),
          ("prime-pw-conn", 52),
          ("slot1-switch-0-conn", 53),
          ("slot1-switch-1-conn", 54))
    )


_TelAdminStatusIfCon_Type.__name__ = "Integer32"
_TelAdminStatusIfCon_Object = MibTableColumn
telAdminStatusIfCon = _TelAdminStatusIfCon_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 10, 1, 3),
    _TelAdminStatusIfCon_Type()
)
telAdminStatusIfCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusIfCon.setStatus("mandatory")
_TelAdminStatusIfHdw_Type = DisplayString
_TelAdminStatusIfHdw_Object = MibTableColumn
telAdminStatusIfHdw = _TelAdminStatusIfHdw_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 10, 1, 4),
    _TelAdminStatusIfHdw_Type()
)
telAdminStatusIfHdw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusIfHdw.setStatus("mandatory")
_TelAdminStatusEthTime_Type = DisplayString
_TelAdminStatusEthTime_Object = MibScalar
telAdminStatusEthTime = _TelAdminStatusEthTime_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 11),
    _TelAdminStatusEthTime_Type()
)
telAdminStatusEthTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminStatusEthTime.setStatus("mandatory")


class _TelAdminConfActDev_Type(Integer32):
    """Custom type telAdminConfActDev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("smartcard-flash", 1),
          ("smartcard", 2),
          ("flash", 3))
    )


_TelAdminConfActDev_Type.__name__ = "Integer32"
_TelAdminConfActDev_Object = MibScalar
telAdminConfActDev = _TelAdminConfActDev_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 12),
    _TelAdminConfActDev_Type()
)
telAdminConfActDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telAdminConfActDev.setStatus("mandatory")


class _TelAdminConfConfSavedDev_Type(Integer32):
    """Custom type telAdminConfConfSavedDev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("smartcard", 1),
          ("flash", 2),
          ("smartcard-flash", 3))
    )


_TelAdminConfConfSavedDev_Type.__name__ = "Integer32"
_TelAdminConfConfSavedDev_Object = MibScalar
telAdminConfConfSavedDev = _TelAdminConfConfSavedDev_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 13),
    _TelAdminConfConfSavedDev_Type()
)
telAdminConfConfSavedDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telAdminConfConfSavedDev.setStatus("mandatory")


class _TelAdminStatusConfirmConfig_Type(Integer32):
    """Custom type telAdminStatusConfirmConfig based on Integer32"""
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
        *(("confirmed", 0),
          ("test-cnfg-inactive", 1),
          ("test-cnfg-active", 2),
          ("configuration-recovered", 3),
          ("undefined", 4))
    )


_TelAdminStatusConfirmConfig_Type.__name__ = "Integer32"
_TelAdminStatusConfirmConfig_Object = MibScalar
telAdminStatusConfirmConfig = _TelAdminStatusConfirmConfig_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 14),
    _TelAdminStatusConfirmConfig_Type()
)
telAdminStatusConfirmConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telAdminStatusConfirmConfig.setStatus("mandatory")


class _TelAdminStatusConfirmEnabled_Type(Integer32):
    """Custom type telAdminStatusConfirmEnabled based on Integer32"""
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


_TelAdminStatusConfirmEnabled_Type.__name__ = "Integer32"
_TelAdminStatusConfirmEnabled_Object = MibScalar
telAdminStatusConfirmEnabled = _TelAdminStatusConfirmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 15),
    _TelAdminStatusConfirmEnabled_Type()
)
telAdminStatusConfirmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telAdminStatusConfirmEnabled.setStatus("mandatory")


class _TelAdminStatusTimeoutConfirm_Type(Integer32):
    """Custom type telAdminStatusTimeoutConfirm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3024000),
    )


_TelAdminStatusTimeoutConfirm_Type.__name__ = "Integer32"
_TelAdminStatusTimeoutConfirm_Object = MibScalar
telAdminStatusTimeoutConfirm = _TelAdminStatusTimeoutConfirm_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 16),
    _TelAdminStatusTimeoutConfirm_Type()
)
telAdminStatusTimeoutConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telAdminStatusTimeoutConfirm.setStatus("mandatory")


class _TelAdminStatusSaveRunningConfig_Type(Integer32):
    """Custom type telAdminStatusSaveRunningConfig based on Integer32"""
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
        *(("undefined", 0),
          ("save-configuration", 1),
          ("saved-configuration", 2),
          ("not-saved-configuration", 3))
    )


_TelAdminStatusSaveRunningConfig_Type.__name__ = "Integer32"
_TelAdminStatusSaveRunningConfig_Object = MibScalar
telAdminStatusSaveRunningConfig = _TelAdminStatusSaveRunningConfig_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 2, 17),
    _TelAdminStatusSaveRunningConfig_Type()
)
telAdminStatusSaveRunningConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telAdminStatusSaveRunningConfig.setStatus("mandatory")
_TelMciTraps_ObjectIdentity = ObjectIdentity
telMciTraps = _TelMciTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 3)
)
_TelTrapVarIPAddr_Type = IpAddress
_TelTrapVarIPAddr_Object = MibScalar
telTrapVarIPAddr = _TelTrapVarIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 3, 1),
    _TelTrapVarIPAddr_Type()
)
telTrapVarIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telTrapVarIPAddr.setStatus("mandatory")
_TelTrapVarVelCir_Type = Integer32
_TelTrapVarVelCir_Object = MibScalar
telTrapVarVelCir = _TelTrapVarVelCir_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 3, 2),
    _TelTrapVarVelCir_Type()
)
telTrapVarVelCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telTrapVarVelCir.setStatus("mandatory")
_TelTrapVarVelBckp_Type = Integer32
_TelTrapVarVelBckp_Object = MibScalar
telTrapVarVelBckp = _TelTrapVarVelBckp_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 3, 3),
    _TelTrapVarVelBckp_Type()
)
telTrapVarVelBckp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telTrapVarVelBckp.setStatus("mandatory")
_TelTrapVarPrioBackp_Type = Integer32
_TelTrapVarPrioBackp_Object = MibScalar
telTrapVarPrioBackp = _TelTrapVarPrioBackp_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 3, 4),
    _TelTrapVarPrioBackp_Type()
)
telTrapVarPrioBackp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telTrapVarPrioBackp.setStatus("mandatory")
_TelTrapVarTipoBackp_Type = Integer32
_TelTrapVarTipoBackp_Object = MibScalar
telTrapVarTipoBackp = _TelTrapVarTipoBackp_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 3, 5),
    _TelTrapVarTipoBackp_Type()
)
telTrapVarTipoBackp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telTrapVarTipoBackp.setStatus("mandatory")
_TelTrapVarTipoEquip_Type = Integer32
_TelTrapVarTipoEquip_Object = MibScalar
telTrapVarTipoEquip = _TelTrapVarTipoEquip_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 3, 6),
    _TelTrapVarTipoEquip_Type()
)
telTrapVarTipoEquip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telTrapVarTipoEquip.setStatus("mandatory")
_TelTrapVarCustomerName_Type = DisplayString
_TelTrapVarCustomerName_Object = MibScalar
telTrapVarCustomerName = _TelTrapVarCustomerName_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 3, 7),
    _TelTrapVarCustomerName_Type()
)
telTrapVarCustomerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telTrapVarCustomerName.setStatus("mandatory")
_TelTrapVarRouterName_Type = DisplayString
_TelTrapVarRouterName_Object = MibScalar
telTrapVarRouterName = _TelTrapVarRouterName_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 3, 8),
    _TelTrapVarRouterName_Type()
)
telTrapVarRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telTrapVarRouterName.setStatus("mandatory")
_TelTrapVarRouterPort_Type = Integer32
_TelTrapVarRouterPort_Object = MibScalar
telTrapVarRouterPort = _TelTrapVarRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 3, 9),
    _TelTrapVarRouterPort_Type()
)
telTrapVarRouterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telTrapVarRouterPort.setStatus("mandatory")
_TelTrapVarCircuitID_Type = Integer32
_TelTrapVarCircuitID_Object = MibScalar
telTrapVarCircuitID = _TelTrapVarCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 3, 10),
    _TelTrapVarCircuitID_Type()
)
telTrapVarCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telTrapVarCircuitID.setStatus("mandatory")
_TelTrapVarSequenceNum_Type = Integer32
_TelTrapVarSequenceNum_Object = MibScalar
telTrapVarSequenceNum = _TelTrapVarSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 2007, 1, 3, 11),
    _TelTrapVarSequenceNum_Type()
)
telTrapVarSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telTrapVarSequenceNum.setStatus("mandatory")
_TelEventTraps_ObjectIdentity = ObjectIdentity
telEventTraps = _TelEventTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 1, 4)
)
_Telproto_ObjectIdentity = ObjectIdentity
telproto = _Telproto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 3)
)
_Telproip_ObjectIdentity = ObjectIdentity
telproip = _Telproip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 3, 2)
)
_Teldefgw_ObjectIdentity = ObjectIdentity
teldefgw = _Teldefgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 3, 2, 1)
)
_TelProtoIpDefGwAddress_Type = IpAddress
_TelProtoIpDefGwAddress_Object = MibScalar
telProtoIpDefGwAddress = _TelProtoIpDefGwAddress_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 2, 1, 1),
    _TelProtoIpDefGwAddress_Type()
)
telProtoIpDefGwAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProtoIpDefGwAddress.setStatus("optional")
_TelProtoIpDefGwCost_Type = Integer32
_TelProtoIpDefGwCost_Object = MibScalar
telProtoIpDefGwCost = _TelProtoIpDefGwCost_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 2, 1, 2),
    _TelProtoIpDefGwCost_Type()
)
telProtoIpDefGwCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProtoIpDefGwCost.setStatus("optional")
_TelProtoIpDefGwAge_Type = Integer32
_TelProtoIpDefGwAge_Object = MibScalar
telProtoIpDefGwAge = _TelProtoIpDefGwAge_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 2, 1, 3),
    _TelProtoIpDefGwAge_Type()
)
telProtoIpDefGwAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProtoIpDefGwAge.setStatus("optional")
_Telprofr_ObjectIdentity = ObjectIdentity
telprofr = _Telprofr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3)
)
_TelfrLmiTable_Object = MibTable
telfrLmiTable = _TelfrLmiTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 1)
)
if mibBuilder.loadTexts:
    telfrLmiTable.setStatus("mandatory")
_TelfrLmiEntry_Object = MibTableRow
telfrLmiEntry = _TelfrLmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 1, 1)
)
telfrLmiEntry.setIndexNames(
    (0, "TELDAT-MIB", "telfrLmiifIndex"),
)
if mibBuilder.loadTexts:
    telfrLmiEntry.setStatus("mandatory")
_TelfrLmiifIndex_Type = Integer32
_TelfrLmiifIndex_Object = MibTableColumn
telfrLmiifIndex = _TelfrLmiifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 1, 1, 1),
    _TelfrLmiifIndex_Type()
)
telfrLmiifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telfrLmiifIndex.setStatus("mandatory")


class _TelfrLmiBroadcas_Type(Integer32):
    """Custom type telfrLmiBroadcas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_TelfrLmiBroadcas_Type.__name__ = "Integer32"
_TelfrLmiBroadcas_Object = MibTableColumn
telfrLmiBroadcas = _TelfrLmiBroadcas_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 1, 1, 2),
    _TelfrLmiBroadcas_Type()
)
telfrLmiBroadcas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telfrLmiBroadcas.setStatus("mandatory")


class _TelfrLmiMonitConges_Type(Integer32):
    """Custom type telfrLmiMonitConges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_TelfrLmiMonitConges_Type.__name__ = "Integer32"
_TelfrLmiMonitConges_Object = MibTableColumn
telfrLmiMonitConges = _TelfrLmiMonitConges_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 1, 1, 3),
    _TelfrLmiMonitConges_Type()
)
telfrLmiMonitConges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telfrLmiMonitConges.setStatus("mandatory")


class _TelfrLmiMonitCIR_Type(Integer32):
    """Custom type telfrLmiMonitCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_TelfrLmiMonitCIR_Type.__name__ = "Integer32"
_TelfrLmiMonitCIR_Object = MibTableColumn
telfrLmiMonitCIR = _TelfrLmiMonitCIR_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 1, 1, 4),
    _TelfrLmiMonitCIR_Type()
)
telfrLmiMonitCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telfrLmiMonitCIR.setStatus("mandatory")


class _TelfrLmiOrphans_Type(Integer32):
    """Custom type telfrLmiOrphans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_TelfrLmiOrphans_Type.__name__ = "Integer32"
_TelfrLmiOrphans_Object = MibTableColumn
telfrLmiOrphans = _TelfrLmiOrphans_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 1, 1, 5),
    _TelfrLmiOrphans_Type()
)
telfrLmiOrphans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telfrLmiOrphans.setStatus("mandatory")


class _TelfrLmiIRIncrement_Type(Integer32):
    """Custom type telfrLmiIRIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TelfrLmiIRIncrement_Type.__name__ = "Integer32"
_TelfrLmiIRIncrement_Object = MibTableColumn
telfrLmiIRIncrement = _TelfrLmiIRIncrement_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 1, 1, 6),
    _TelfrLmiIRIncrement_Type()
)
telfrLmiIRIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telfrLmiIRIncrement.setStatus("mandatory")


class _TelfrLmiIRDecrement_Type(Integer32):
    """Custom type telfrLmiIRDecrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TelfrLmiIRDecrement_Type.__name__ = "Integer32"
_TelfrLmiIRDecrement_Object = MibTableColumn
telfrLmiIRDecrement = _TelfrLmiIRDecrement_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 1, 1, 7),
    _TelfrLmiIRDecrement_Type()
)
telfrLmiIRDecrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telfrLmiIRDecrement.setStatus("mandatory")


class _TelfrLmiMIRCIR_Type(Integer32):
    """Custom type telfrLmiMIRCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TelfrLmiMIRCIR_Type.__name__ = "Integer32"
_TelfrLmiMIRCIR_Object = MibTableColumn
telfrLmiMIRCIR = _TelfrLmiMIRCIR_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 1, 1, 8),
    _TelfrLmiMIRCIR_Type()
)
telfrLmiMIRCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telfrLmiMIRCIR.setStatus("mandatory")
_TelfrCircuitTable_Object = MibTable
telfrCircuitTable = _TelfrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 2)
)
if mibBuilder.loadTexts:
    telfrCircuitTable.setStatus("mandatory")
_TelfrCircuitEntry_Object = MibTableRow
telfrCircuitEntry = _TelfrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 2, 1)
)
telfrCircuitEntry.setIndexNames(
    (0, "TELDAT-MIB", "telfrCircuitifIndex"),
    (0, "TELDAT-MIB", "telfrCircuitDlci"),
)
if mibBuilder.loadTexts:
    telfrCircuitEntry.setStatus("mandatory")
_TelfrCircuitifIndex_Type = Integer32
_TelfrCircuitifIndex_Object = MibTableColumn
telfrCircuitifIndex = _TelfrCircuitifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 2, 1, 1),
    _TelfrCircuitifIndex_Type()
)
telfrCircuitifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telfrCircuitifIndex.setStatus("mandatory")
_TelfrCircuitDlci_Type = Integer32
_TelfrCircuitDlci_Object = MibTableColumn
telfrCircuitDlci = _TelfrCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 2, 1, 2),
    _TelfrCircuitDlci_Type()
)
telfrCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telfrCircuitDlci.setStatus("mandatory")


class _TelfrCircuitCifrar_Type(Integer32):
    """Custom type telfrCircuitCifrar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_TelfrCircuitCifrar_Type.__name__ = "Integer32"
_TelfrCircuitCifrar_Object = MibTableColumn
telfrCircuitCifrar = _TelfrCircuitCifrar_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 2, 1, 3),
    _TelfrCircuitCifrar_Type()
)
telfrCircuitCifrar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telfrCircuitCifrar.setStatus("mandatory")


class _TelfrCircuitBack_Up_FR_Type(Integer32):
    """Custom type telfrCircuitBack_Up_FR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_TelfrCircuitBack_Up_FR_Type.__name__ = "Integer32"
_TelfrCircuitBack_Up_FR_Object = MibTableColumn
telfrCircuitBack_Up_FR = _TelfrCircuitBack_Up_FR_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 2, 1, 4),
    _TelfrCircuitBack_Up_FR_Type()
)
telfrCircuitBack_Up_FR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telfrCircuitBack_Up_FR.setStatus("mandatory")


class _TelfrCircuitBack_Up_RDSI_Type(Integer32):
    """Custom type telfrCircuitBack_Up_RDSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_TelfrCircuitBack_Up_RDSI_Type.__name__ = "Integer32"
_TelfrCircuitBack_Up_RDSI_Object = MibTableColumn
telfrCircuitBack_Up_RDSI = _TelfrCircuitBack_Up_RDSI_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 2, 1, 5),
    _TelfrCircuitBack_Up_RDSI_Type()
)
telfrCircuitBack_Up_RDSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telfrCircuitBack_Up_RDSI.setStatus("mandatory")


class _TelfrCircuitBack_Up_RDSI_siempre_Type(Integer32):
    """Custom type telfrCircuitBack_Up_RDSI_siempre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_TelfrCircuitBack_Up_RDSI_siempre_Type.__name__ = "Integer32"
_TelfrCircuitBack_Up_RDSI_siempre_Object = MibTableColumn
telfrCircuitBack_Up_RDSI_siempre = _TelfrCircuitBack_Up_RDSI_siempre_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 2, 1, 6),
    _TelfrCircuitBack_Up_RDSI_siempre_Type()
)
telfrCircuitBack_Up_RDSI_siempre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telfrCircuitBack_Up_RDSI_siempre.setStatus("mandatory")


class _TelfrCircuitName_Type(DisplayString):
    """Custom type telfrCircuitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_TelfrCircuitName_Type.__name__ = "DisplayString"
_TelfrCircuitName_Object = MibTableColumn
telfrCircuitName = _TelfrCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 3, 2, 1, 7),
    _TelfrCircuitName_Type()
)
telfrCircuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telfrCircuitName.setStatus("mandatory")
_Telproisdn_ObjectIdentity = ObjectIdentity
telproisdn = _Telproisdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4)
)
_TelproisdncallTable_Object = MibTable
telproisdncallTable = _TelproisdncallTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 1)
)
if mibBuilder.loadTexts:
    telproisdncallTable.setStatus("obsolete")
_TelproisdncallEntry_Object = MibTableRow
telproisdncallEntry = _TelproisdncallEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 1, 1)
)
telproisdncallEntry.setIndexNames(
    (0, "TELDAT-MIB", "telproisdncallid"),
)
if mibBuilder.loadTexts:
    telproisdncallEntry.setStatus("obsolete")


class _Telproisdncallstatus_Type(Integer32):
    """Custom type telproisdncallstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Telproisdncallstatus_Type.__name__ = "Integer32"
_Telproisdncallstatus_Object = MibTableColumn
telproisdncallstatus = _Telproisdncallstatus_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 1, 1, 1),
    _Telproisdncallstatus_Type()
)
telproisdncallstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallstatus.setStatus("obsolete")


class _Telproisdncalltype_Type(Integer32):
    """Custom type telproisdncalltype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 0),
          ("outgoing", 1))
    )


_Telproisdncalltype_Type.__name__ = "Integer32"
_Telproisdncalltype_Object = MibTableColumn
telproisdncalltype = _Telproisdncalltype_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 1, 1, 2),
    _Telproisdncalltype_Type()
)
telproisdncalltype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncalltype.setStatus("obsolete")
_Telproisdncallref_Type = Integer32
_Telproisdncallref_Object = MibTableColumn
telproisdncallref = _Telproisdncallref_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 1, 1, 3),
    _Telproisdncallref_Type()
)
telproisdncallref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallref.setStatus("obsolete")
_Telproisdncallchannel_Type = Integer32
_Telproisdncallchannel_Object = MibTableColumn
telproisdncallchannel = _Telproisdncallchannel_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 1, 1, 4),
    _Telproisdncallchannel_Type()
)
telproisdncallchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallchannel.setStatus("obsolete")
_Telproisdncallid_Type = Integer32
_Telproisdncallid_Object = MibTableColumn
telproisdncallid = _Telproisdncallid_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 1, 1, 5),
    _Telproisdncallid_Type()
)
telproisdncallid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallid.setStatus("obsolete")
_Telproisdncallcallednum_Type = DisplayString
_Telproisdncallcallednum_Object = MibTableColumn
telproisdncallcallednum = _Telproisdncallcallednum_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 1, 1, 6),
    _Telproisdncallcallednum_Type()
)
telproisdncallcallednum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallcallednum.setStatus("obsolete")
_Telproisdncallcallingnum_Type = DisplayString
_Telproisdncallcallingnum_Object = MibTableColumn
telproisdncallcallingnum = _Telproisdncallcallingnum_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 1, 1, 7),
    _Telproisdncallcallingnum_Type()
)
telproisdncallcallingnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallcallingnum.setStatus("obsolete")
_Telproisdncallchargedunits_Type = Integer32
_Telproisdncallchargedunits_Object = MibTableColumn
telproisdncallchargedunits = _Telproisdncallchargedunits_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 1, 1, 8),
    _Telproisdncallchargedunits_Type()
)
telproisdncallchargedunits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallchargedunits.setStatus("obsolete")
_Telproisdncallinittime_Type = OctetString
_Telproisdncallinittime_Object = MibTableColumn
telproisdncallinittime = _Telproisdncallinittime_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 1, 1, 9),
    _Telproisdncallinittime_Type()
)
telproisdncallinittime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallinittime.setStatus("obsolete")
_Telproisdncallinitdate_Type = OctetString
_Telproisdncallinitdate_Object = MibTableColumn
telproisdncallinitdate = _Telproisdncallinitdate_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 1, 1, 10),
    _Telproisdncallinitdate_Type()
)
telproisdncallinitdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallinitdate.setStatus("obsolete")
_TelproisdncallhistoryTable_Object = MibTable
telproisdncallhistoryTable = _TelproisdncallhistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2)
)
if mibBuilder.loadTexts:
    telproisdncallhistoryTable.setStatus("obsolete")
_TelproisdncallhistoryEntry_Object = MibTableRow
telproisdncallhistoryEntry = _TelproisdncallhistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2, 1)
)
telproisdncallhistoryEntry.setIndexNames(
    (0, "TELDAT-MIB", "telproisdncallhistoryindex"),
)
if mibBuilder.loadTexts:
    telproisdncallhistoryEntry.setStatus("obsolete")
_Telproisdncallhistoryindex_Type = Integer32
_Telproisdncallhistoryindex_Object = MibTableColumn
telproisdncallhistoryindex = _Telproisdncallhistoryindex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2, 1, 1),
    _Telproisdncallhistoryindex_Type()
)
telproisdncallhistoryindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallhistoryindex.setStatus("obsolete")


class _Telproisdncallhistorytype_Type(Integer32):
    """Custom type telproisdncallhistorytype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 0),
          ("outgoing", 1))
    )


_Telproisdncallhistorytype_Type.__name__ = "Integer32"
_Telproisdncallhistorytype_Object = MibTableColumn
telproisdncallhistorytype = _Telproisdncallhistorytype_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2, 1, 2),
    _Telproisdncallhistorytype_Type()
)
telproisdncallhistorytype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallhistorytype.setStatus("obsolete")
_Telproisdncallhistoryref_Type = Integer32
_Telproisdncallhistoryref_Object = MibTableColumn
telproisdncallhistoryref = _Telproisdncallhistoryref_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2, 1, 3),
    _Telproisdncallhistoryref_Type()
)
telproisdncallhistoryref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallhistoryref.setStatus("obsolete")
_Telproisdncallhistorychannel_Type = Integer32
_Telproisdncallhistorychannel_Object = MibTableColumn
telproisdncallhistorychannel = _Telproisdncallhistorychannel_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2, 1, 4),
    _Telproisdncallhistorychannel_Type()
)
telproisdncallhistorychannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallhistorychannel.setStatus("obsolete")
_Telproisdncallhistoryid_Type = Integer32
_Telproisdncallhistoryid_Object = MibTableColumn
telproisdncallhistoryid = _Telproisdncallhistoryid_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2, 1, 5),
    _Telproisdncallhistoryid_Type()
)
telproisdncallhistoryid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallhistoryid.setStatus("obsolete")
_Telproisdncallhistorycallednum_Type = DisplayString
_Telproisdncallhistorycallednum_Object = MibTableColumn
telproisdncallhistorycallednum = _Telproisdncallhistorycallednum_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2, 1, 6),
    _Telproisdncallhistorycallednum_Type()
)
telproisdncallhistorycallednum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallhistorycallednum.setStatus("obsolete")
_Telproisdncallhistorycallingnum_Type = DisplayString
_Telproisdncallhistorycallingnum_Object = MibTableColumn
telproisdncallhistorycallingnum = _Telproisdncallhistorycallingnum_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2, 1, 7),
    _Telproisdncallhistorycallingnum_Type()
)
telproisdncallhistorycallingnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallhistorycallingnum.setStatus("obsolete")
_Telproisdncallhistorychargedunits_Type = Integer32
_Telproisdncallhistorychargedunits_Object = MibTableColumn
telproisdncallhistorychargedunits = _Telproisdncallhistorychargedunits_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2, 1, 8),
    _Telproisdncallhistorychargedunits_Type()
)
telproisdncallhistorychargedunits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallhistorychargedunits.setStatus("obsolete")


class _Telproisdncallhistorycause_Type(Integer32):
    """Custom type telproisdncallhistorycause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              6,
              16,
              17,
              18,
              19,
              21,
              22,
              27,
              28,
              31,
              34,
              38,
              41,
              42,
              44,
              47,
              49,
              57,
              58,
              63,
              65,
              66,
              79,
              81,
              82,
              88,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              111,
              127)
        )
    )
    namedValues = NamedValues(
        *(("non-attributed-number", 1),
          ("no-route-to-destination", 3),
          ("unacceptable-channel", 6),
          ("normal-call-release", 16),
          ("user-busy", 17),
          ("user-do-not-answer", 18),
          ("notified-user-no-answer-from-user", 19),
          ("rejected-call", 21),
          ("changed-number", 22),
          ("destination-out-of-service", 27),
          ("non-valid-number-format", 28),
          ("normal", 31),
          ("no-circuit-or-available-channel", 34),
          ("network-out-of-service", 38),
          ("temporal-failure", 41),
          ("congestion-in-switching-node", 42),
          ("demanded-circuit-or-non-available-channel", 44),
          ("non-available-resources", 47),
          ("non-available-quality-of-service", 49),
          ("not-authorized-carrier-capacity", 57),
          ("not-authorized-carrier-capacity-at-the-moment", 58),
          ("service-class-or-non-available-option", 63),
          ("not-performed-carrier-capacity", 65),
          ("not-performed-channel-type", 66),
          ("not-performed-option-or-service", 79),
          ("non-valid-call-reference-value", 81),
          ("non-existent-identified-channel", 82),
          ("incompatible-destination", 88),
          ("non-valid-message", 95),
          ("mandatory-information-element-absent", 96),
          ("message-type-non-existent-or-non-performed", 97),
          ("message-non-existent-or-non-performed", 98),
          ("information-element-non-existent-or-non-performed", 99),
          ("information-element-content-non-valid", 100),
          ("incompatible-message-with-call-status", 101),
          ("recovering-at-timer-expiration", 102),
          ("protocol-error", 111),
          ("interworking", 127))
    )


_Telproisdncallhistorycause_Type.__name__ = "Integer32"
_Telproisdncallhistorycause_Object = MibTableColumn
telproisdncallhistorycause = _Telproisdncallhistorycause_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2, 1, 9),
    _Telproisdncallhistorycause_Type()
)
telproisdncallhistorycause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallhistorycause.setStatus("obsolete")
_Telproisdncallhistorydiagnostic_Type = Integer32
_Telproisdncallhistorydiagnostic_Object = MibTableColumn
telproisdncallhistorydiagnostic = _Telproisdncallhistorydiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2, 1, 10),
    _Telproisdncallhistorydiagnostic_Type()
)
telproisdncallhistorydiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallhistorydiagnostic.setStatus("obsolete")
_Telproisdncallhistoryinittime_Type = OctetString
_Telproisdncallhistoryinittime_Object = MibTableColumn
telproisdncallhistoryinittime = _Telproisdncallhistoryinittime_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2, 1, 11),
    _Telproisdncallhistoryinittime_Type()
)
telproisdncallhistoryinittime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallhistoryinittime.setStatus("obsolete")
_Telproisdncallhistoryendtime_Type = OctetString
_Telproisdncallhistoryendtime_Object = MibTableColumn
telproisdncallhistoryendtime = _Telproisdncallhistoryendtime_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2, 1, 12),
    _Telproisdncallhistoryendtime_Type()
)
telproisdncallhistoryendtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallhistoryendtime.setStatus("obsolete")
_Telproisdncallhistoryinitdate_Type = OctetString
_Telproisdncallhistoryinitdate_Object = MibTableColumn
telproisdncallhistoryinitdate = _Telproisdncallhistoryinitdate_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2, 1, 13),
    _Telproisdncallhistoryinitdate_Type()
)
telproisdncallhistoryinitdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallhistoryinitdate.setStatus("obsolete")
_Telproisdncallhistoryenddate_Type = OctetString
_Telproisdncallhistoryenddate_Object = MibTableColumn
telproisdncallhistoryenddate = _Telproisdncallhistoryenddate_Object(
    (1, 3, 6, 1, 4, 1, 2007, 3, 4, 2, 1, 14),
    _Telproisdncallhistoryenddate_Type()
)
telproisdncallhistoryenddate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telproisdncallhistoryenddate.setStatus("obsolete")
_Telproducts_ObjectIdentity = ObjectIdentity
telproducts = _Telproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4)
)

# Managed Objects groups


# Notification objects

telSistemaEventos = NotificationType(
    (1, 3, 6, 1, 4, 1, 2007, 0, 1)
)
telSistemaEventos.setObjects(
      *(("TELDAT-MIB", "sreTrapSubSist"),
        ("TELDAT-MIB", "sreTrapEvento"),
        ("TELDAT-MIB", "sreTrapVar1"),
        ("TELDAT-MIB", "sreTrapVar2"),
        ("TELDAT-MIB", "sreTrapVar3"),
        ("TELDAT-MIB", "sreTrapVar4"),
        ("TELDAT-MIB", "sreTrapVar5"),
        ("TELDAT-MIB", "sreTrapVar6"),
        ("TELDAT-MIB", "sreTrapVar7"),
        ("TELDAT-MIB", "sreTrapVar8"),
        ("TELDAT-MIB", "sreTrapVar9"))
)
if mibBuilder.loadTexts:
    telSistemaEventos.setStatus(
        ""
    )

telTECircuitTrapUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2007, 1, 3, 0, 1)
)
telTECircuitTrapUp.setObjects(
      *(("TELDAT-MIB", "telTrapVarIPAddr"),
        ("TELDAT-MIB", "telTrapVarVelCir"),
        ("TELDAT-MIB", "telTrapVarVelBckp"),
        ("TELDAT-MIB", "telTrapVarPrioBackp"),
        ("TELDAT-MIB", "telTrapVarTipoBackp"),
        ("TELDAT-MIB", "telTrapVarTipoEquip"),
        ("TELDAT-MIB", "telTrapVarCustomerName"),
        ("TELDAT-MIB", "telTrapVarRouterName"),
        ("TELDAT-MIB", "telTrapVarRouterPort"),
        ("TELDAT-MIB", "telTrapVarCircuitID"),
        ("TELDAT-MIB", "telTrapVarSequenceNum"))
)
if mibBuilder.loadTexts:
    telTECircuitTrapUp.setStatus(
        ""
    )

telTECircuitTrapBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 2007, 1, 3, 0, 2)
)
telTECircuitTrapBackup.setObjects(
      *(("TELDAT-MIB", "telTrapVarIPAddr"),
        ("TELDAT-MIB", "telTrapVarVelCir"),
        ("TELDAT-MIB", "telTrapVarVelBckp"),
        ("TELDAT-MIB", "telTrapVarPrioBackp"),
        ("TELDAT-MIB", "telTrapVarTipoBackp"),
        ("TELDAT-MIB", "telTrapVarTipoEquip"),
        ("TELDAT-MIB", "telTrapVarCustomerName"),
        ("TELDAT-MIB", "telTrapVarRouterName"),
        ("TELDAT-MIB", "telTrapVarRouterPort"),
        ("TELDAT-MIB", "telTrapVarCircuitID"),
        ("TELDAT-MIB", "telTrapVarSequenceNum"))
)
if mibBuilder.loadTexts:
    telTECircuitTrapBackup.setStatus(
        ""
    )

telTECircuitTrapDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2007, 1, 3, 0, 3)
)
telTECircuitTrapDown.setObjects(
      *(("TELDAT-MIB", "telTrapVarIPAddr"),
        ("TELDAT-MIB", "telTrapVarVelCir"),
        ("TELDAT-MIB", "telTrapVarVelBckp"),
        ("TELDAT-MIB", "telTrapVarPrioBackp"),
        ("TELDAT-MIB", "telTrapVarTipoBackp"),
        ("TELDAT-MIB", "telTrapVarTipoEquip"),
        ("TELDAT-MIB", "telTrapVarCustomerName"),
        ("TELDAT-MIB", "telTrapVarRouterName"),
        ("TELDAT-MIB", "telTrapVarRouterPort"),
        ("TELDAT-MIB", "telTrapVarCircuitID"),
        ("TELDAT-MIB", "telTrapVarSequenceNum"))
)
if mibBuilder.loadTexts:
    telTECircuitTrapDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELDAT-MIB",
    **{"teldat": teldat,
       "telSistemaEventos": telSistemaEventos,
       "teladmin": teladmin,
       "telobjid": telobjid,
       "teldatSreTrap": teldatSreTrap,
       "teldatSreTrap-GW": teldatSreTrap_GW,
       "teldatSreTrap-FLT": teldatSreTrap_FLT,
       "teldatSreTrap-BRS": teldatSreTrap_BRS,
       "teldatSreTrap-ARP": teldatSreTrap_ARP,
       "teldatSreTrap-IP": teldatSreTrap_IP,
       "teldatSreTrap-ICMP": teldatSreTrap_ICMP,
       "teldatSreTrap-TCP": teldatSreTrap_TCP,
       "teldatSreTrap-UDP": teldatSreTrap_UDP,
       "teldatSreTrap-ORIP": teldatSreTrap_ORIP,
       "teldatSreTrap-SPF": teldatSreTrap_SPF,
       "teldatSreTrap-TFTP": teldatSreTrap_TFTP,
       "teldatSreTrap-SNMP": teldatSreTrap_SNMP,
       "teldatSreTrap-SRT": teldatSreTrap_SRT,
       "teldatSreTrap-BR": teldatSreTrap_BR,
       "teldatSreTrap-FTP": teldatSreTrap_FTP,
       "teldatSreTrap-ETH": teldatSreTrap_ETH,
       "teldatSreTrap-SL": teldatSreTrap_SL,
       "teldatSreTrap-TKR": teldatSreTrap_TKR,
       "teldatSreTrap-SDLC": teldatSreTrap_SDLC,
       "teldatSreTrap-FR": teldatSreTrap_FR,
       "teldatSreTrap-PPP": teldatSreTrap_PPP,
       "teldatSreTrap-X252": teldatSreTrap_X252,
       "teldatSreTrap-X253": teldatSreTrap_X253,
       "teldatSreTrap-RDSI": teldatSreTrap_RDSI,
       "teldatSreTrap-LLC": teldatSreTrap_LLC,
       "teldatSreTrap-BAN": teldatSreTrap_BAN,
       "teldatSreTrap-NBS": teldatSreTrap_NBS,
       "teldatSreTrap-CIF": teldatSreTrap_CIF,
       "teldatSreTrap-GSTP": teldatSreTrap_GSTP,
       "teldatSreTrap-FRBK": teldatSreTrap_FRBK,
       "teldatSreTrap-PRI": teldatSreTrap_PRI,
       "teldatSreTrap-DLS": teldatSreTrap_DLS,
       "teldatSreTrap-PCMC": teldatSreTrap_PCMC,
       "teldatSreTrap-LAPD": teldatSreTrap_LAPD,
       "teldatSreTrap-TNIP": teldatSreTrap_TNIP,
       "teldatSreTrap-MBBU": teldatSreTrap_MBBU,
       "teldatSreTrap-BIR64": teldatSreTrap_BIR64,
       "teldatSreTrap-REXISMRU": teldatSreTrap_REXISMRU,
       "teldatSreTrap-REXISFT": teldatSreTrap_REXISFT,
       "teldatSreTrap-ICUPLUS": teldatSreTrap_ICUPLUS,
       "teldatSreTrap-Q933": teldatSreTrap_Q933,
       "teldatSreTrap-IPPN": teldatSreTrap_IPPN,
       "teldatSreTrap-RAD": teldatSreTrap_RAD,
       "teldatSreTrap-H323": teldatSreTrap_H323,
       "teldatSreTrap-DHCP": teldatSreTrap_DHCP,
       "teldatSreTrap-IP6": teldatSreTrap_IP6,
       "teldatSreTrap-TVRP": teldatSreTrap_TVRP,
       "teldatSreTrap-ATM": teldatSreTrap_ATM,
       "teldatSreTrap-IPSEC": teldatSreTrap_IPSEC,
       "teldatSreTrap-NTP": teldatSreTrap_NTP,
       "teldatSreTrap-ADSL": teldatSreTrap_ADSL,
       "teldatSreTrap-HTTP": teldatSreTrap_HTTP,
       "teldatSreTrap-DEP": teldatSreTrap_DEP,
       "teldatSreTrap-ASDP": teldatSreTrap_ASDP,
       "teldatSreTrap-LDAP": teldatSreTrap_LDAP,
       "teldatSreTrap-SCEP": teldatSreTrap_SCEP,
       "teldatSreTrap-P3OE": teldatSreTrap_P3OE,
       "teldatSreTrap-AT": teldatSreTrap_AT,
       "teldatSreTrap-ASYNC": teldatSreTrap_ASYNC,
       "teldatSreTrap-SYNC": teldatSreTrap_SYNC,
       "teldatSreTrap-DNS": teldatSreTrap_DNS,
       "teldatSreTrap-VSN": teldatSreTrap_VSN,
       "teldatSreTrap-NAPT": teldatSreTrap_NAPT,
       "teldatSreTrap-VID": teldatSreTrap_VID,
       "teldatSreTrap-PRL": teldatSreTrap_PRL,
       "teldatSreTrap-HDSL": teldatSreTrap_HDSL,
       "teldatSreTrap-PGMO": teldatSreTrap_PGMO,
       "teldatSreTrap-RTSP": teldatSreTrap_RTSP,
       "teldatSreTrap-DNAT": teldatSreTrap_DNAT,
       "teldatSreTrap-G703": teldatSreTrap_G703,
       "teldatSreTrap-POLR": teldatSreTrap_POLR,
       "teldatSreTrap-XN": teldatSreTrap_XN,
       "teldatSreTrap-XNS": teldatSreTrap_XNS,
       "teldatSreTrap-IPX": teldatSreTrap_IPX,
       "teldatSreTrap-IGMP": teldatSreTrap_IGMP,
       "teldatSreTrap-AINST": teldatSreTrap_AINST,
       "teldatSreTrap-BGP": teldatSreTrap_BGP,
       "teldatSreTrap-NSM": teldatSreTrap_NSM,
       "teldatSreTrap-TLNT": teldatSreTrap_TLNT,
       "teldatSreTrap-L2TP": teldatSreTrap_L2TP,
       "teldatSreTrap-NSLA": teldatSreTrap_NSLA,
       "teldatSreTrap-VOIP": teldatSreTrap_VOIP,
       "teldatSreTrap-TTTP": teldatSreTrap_TTTP,
       "teldatSreTrap-IKE": teldatSreTrap_IKE,
       "teldatSreTrap-HSSI": teldatSreTrap_HSSI,
       "teldatSreTrap-SCADA": teldatSreTrap_SCADA,
       "teldatSreTrap-VRRP": teldatSreTrap_VRRP,
       "teldatSreTrap-SIP": teldatSreTrap_SIP,
       "teldatSreTrap-IPHC": teldatSreTrap_IPHC,
       "teldatSreTrap-DHCPC": teldatSreTrap_DHCPC,
       "teldatSreTrap-CNSL": teldatSreTrap_CNSL,
       "teldatSreTrap-TLPHY": teldatSreTrap_TLPHY,
       "teldatSreTrap-NHRP": teldatSreTrap_NHRP,
       "teldatSreTrap-SNAT": teldatSreTrap_SNAT,
       "teldatSreTrap-STUN": teldatSreTrap_STUN,
       "teldatSreTrap-WLAN": teldatSreTrap_WLAN,
       "teldatSreTrap-SCDFW": teldatSreTrap_SCDFW,
       "teldatSreTrap-HDLC": teldatSreTrap_HDLC,
       "teldatSreTrap-EAP": teldatSreTrap_EAP,
       "teldatSreTrap-EIBZ": teldatSreTrap_EIBZ,
       "teldatSreTrap-PHYS": teldatSreTrap_PHYS,
       "teldatSreTrap-SPOOF": teldatSreTrap_SPOOF,
       "teldatSreTrap-IRVOZ": teldatSreTrap_IRVOZ,
       "teldatSreTrap-RSTP": teldatSreTrap_RSTP,
       "teldatSreTrap-TIDP": teldatSreTrap_TIDP,
       "teldatSreTrap-NOE": teldatSreTrap_NOE,
       "teldatSreTrap-AFS": teldatSreTrap_AFS,
       "teldatSreTrap-X28": teldatSreTrap_X28,
       "teldatSreTrap-BFD": teldatSreTrap_BFD,
       "teldatSreTrap-DNSU": teldatSreTrap_DNSU,
       "teldatSreTrap-UDP6": teldatSreTrap_UDP6,
       "teldatSreTrap-ICM6O": teldatSreTrap_ICM6O,
       "teldatSreTrap-CELL": teldatSreTrap_CELL,
       "teldatSreTrap-SSL": teldatSreTrap_SSL,
       "teldatSreTrap-SCCP": teldatSreTrap_SCCP,
       "teldatSreTrap-WWAN": teldatSreTrap_WWAN,
       "teldatSreTrap-ISTD": teldatSreTrap_ISTD,
       "teldatSreTrap-DOT1X": teldatSreTrap_DOT1X,
       "teldatSreTrap-EOAM": teldatSreTrap_EOAM,
       "teldatSreTrap-SSH": teldatSreTrap_SSH,
       "teldatSreTrap-CDP": teldatSreTrap_CDP,
       "teldatSreTrap-PIO": teldatSreTrap_PIO,
       "teldatSreTrap-FLOW": teldatSreTrap_FLOW,
       "teldatSreTrap-RIP": teldatSreTrap_RIP,
       "teldatSreTrap-MGCP": teldatSreTrap_MGCP,
       "teldatSreTrap-TIPS": teldatSreTrap_TIPS,
       "teldatSreTrap-SRVP": teldatSreTrap_SRVP,
       "teldatSreTrap-SPI": teldatSreTrap_SPI,
       "teldatSreTrap-VLI": teldatSreTrap_VLI,
       "teldatSreTrap-ACAT": teldatSreTrap_ACAT,
       "teldatSreTrap-AAA": teldatSreTrap_AAA,
       "teldatSreTrap-SDEV": teldatSreTrap_SDEV,
       "teldatSreTrap-G104": teldatSreTrap_G104,
       "teldatSreTrap-I101": teldatSreTrap_I101,
       "teldatSreTrap-IPSF": teldatSreTrap_IPSF,
       "teldatSreTrap-DH6C": teldatSreTrap_DH6C,
       "teldatSreTrap-NEIG": teldatSreTrap_NEIG,
       "teldatSreTrap-ND": teldatSreTrap_ND,
       "teldatSreTrap-ICM6": teldatSreTrap_ICM6,
       "teldatSreTrap-LLDP": teldatSreTrap_LLDP,
       "teldatSreTrap-RIP6": teldatSreTrap_RIP6,
       "teldatSreTrap-MLD6": teldatSreTrap_MLD6,
       "teldatSreTrap-PIM": teldatSreTrap_PIM,
       "teldatSreTrap-MRTE": teldatSreTrap_MRTE,
       "teldatSreTrap-ACL": teldatSreTrap_ACL,
       "teldatSreTrap-SPF6": teldatSreTrap_SPF6,
       "teldatSreTrap-NIC": teldatSreTrap_NIC,
       "teldatSreTrap-MSDP": teldatSreTrap_MSDP,
       "teldatSreTrap-ACT": teldatSreTrap_ACT,
       "teldatSreTrap-TDGS": teldatSreTrap_TDGS,
       "teldatSreTrap-GPSF": teldatSreTrap_GPSF,
       "teldatSreTrap-WNMS": teldatSreTrap_WNMS,
       "teldatSreTrap-DH6S": teldatSreTrap_DH6S,
       "teldatSreTrap-CFM": teldatSreTrap_CFM,
       "teldatSreTrap-PRIME": teldatSreTrap_PRIME,
       "teldatSreTrap-SMGT": teldatSreTrap_SMGT,
       "sreTrapSubSist": sreTrapSubSist,
       "sreTrapEvento": sreTrapEvento,
       "sreTrapVar1": sreTrapVar1,
       "sreTrapVar2": sreTrapVar2,
       "sreTrapVar3": sreTrapVar3,
       "sreTrapVar4": sreTrapVar4,
       "sreTrapVar5": sreTrapVar5,
       "sreTrapVar6": sreTrapVar6,
       "sreTrapVar7": sreTrapVar7,
       "sreTrapVar8": sreTrapVar8,
       "sreTrapVar9": sreTrapVar9,
       "equipo-rexis-mru": equipo_rexis_mru,
       "equipo-mbbu": equipo_mbbu,
       "equipo-bir-u": equipo_bir_u,
       "equipo-ebano": equipo_ebano,
       "equipo-nucleox-plus": equipo_nucleox_plus,
       "equipo-cbra": equipo_cbra,
       "equipo-centrix-b": equipo_centrix_b,
       "equipo-centrix-p": equipo_centrix_p,
       "equipo-temis": equipo_temis,
       "equipo-novacom": equipo_novacom,
       "equipo-router-maestro": equipo_router_maestro,
       "equipo-cbra20": equipo_cbra20,
       "equipo-np20h": equipo_np20h,
       "equipo-icu-plus": equipo_icu_plus,
       "equipo-centrix-f": equipo_centrix_f,
       "equipo-cbra-tar": equipo_cbra_tar,
       "equipo-aura": equipo_aura,
       "equipo-kronos": equipo_kronos,
       "equipo-teldat-C2": equipo_teldat_C2,
       "equipo-operador-remoto": equipo_operador_remoto,
       "equipo-visor": equipo_visor,
       "equipo-voxnet": equipo_voxnet,
       "equipo-dusac32": equipo_dusac32,
       "equipo-novacom-x25": equipo_novacom_x25,
       "equipo-enaplan": equipo_enaplan,
       "equipo-teldat-C3": equipo_teldat_C3,
       "equipo-atlas-standard": equipo_atlas_standard,
       "equipo-teldat-C2B": equipo_teldat_C2B,
       "equipo-teldat-CSW": equipo_teldat_CSW,
       "equipo-teldat-C3-1": equipo_teldat_C3_1,
       "equipo-teldat-C3B-1": equipo_teldat_C3B_1,
       "equipo-teldat-C2BM": equipo_teldat_C2BM,
       "equipo-atlas-basico": equipo_atlas_basico,
       "equipo-teldat-C2i": equipo_teldat_C2i,
       "equipo-teldat-C3i": equipo_teldat_C3i,
       "equipo-teldat-C3B": equipo_teldat_C3B,
       "equipo-teldat-C3G": equipo_teldat_C3G,
       "equipo-teldat-C4": equipo_teldat_C4,
       "equipo-teldat-C4i": equipo_teldat_C4i,
       "equipo-teldat-C4B": equipo_teldat_C4B,
       "equipo-centrix-sec": equipo_centrix_sec,
       "equipo-centrix-d": equipo_centrix_d,
       "equipo-teldat-C2-UP": equipo_teldat_C2_UP,
       "equipo-teldat-C6": equipo_teldat_C6,
       "equipo-centrix-ng": equipo_centrix_ng,
       "equipo-atlas-voxnet": equipo_atlas_voxnet,
       "equipo-s2": equipo_s2,
       "equipo-s4": equipo_s4,
       "equipo-s2i": equipo_s2i,
       "equipo-s4i": equipo_s4i,
       "equipo-g2": equipo_g2,
       "equipo-g3": equipo_g3,
       "equipo-g4": equipo_g4,
       "equipo-g2i": equipo_g2i,
       "equipo-g3i": equipo_g3i,
       "equipo-g4i": equipo_g4i,
       "equipo-c1": equipo_c1,
       "equipo-c1B": equipo_c1B,
       "equipo-c1i": equipo_c1i,
       "equipo-s1": equipo_s1,
       "equipo-s1i": equipo_s1i,
       "equipo-g1": equipo_g1,
       "equipo-g1i": equipo_g1i,
       "equipo-g3-lite": equipo_g3_lite,
       "equipo-C3G-lite": equipo_C3G_lite,
       "equipo-atlas-100": equipo_atlas_100,
       "equipo-atlas-300V": equipo_atlas_300V,
       "equipo-c1G": equipo_c1G,
       "equipo-atlas-250": equipo_atlas_250,
       "equipo-c4G": equipo_c4G,
       "equipo-atlas-100B": equipo_atlas_100B,
       "equipo-atlas-150": equipo_atlas_150,
       "equipo-a2": equipo_a2,
       "equipo-a3": equipo_a3,
       "equipo-a4": equipo_a4,
       "equipo-a2i": equipo_a2i,
       "equipo-a3i": equipo_a3i,
       "equipo-a4i": equipo_a4i,
       "equipo-a1": equipo_a1,
       "equipo-a1i": equipo_a1i,
       "equipo-g4-cdma": equipo_g4_cdma,
       "equipo-g4i-cdma": equipo_g4i_cdma,
       "equipo-g3-cdma": equipo_g3_cdma,
       "equipo-g3i-cdma": equipo_g3i_cdma,
       "equipo-g1-cdma": equipo_g1_cdma,
       "equipo-g1i-cdma": equipo_g1i_cdma,
       "equipo-c1plus": equipo_c1plus,
       "equipo-c1iplus": equipo_c1iplus,
       "equipo-atlas-50": equipo_atlas_50,
       "equipo-g4plus": equipo_g4plus,
       "equipo-g3plus": equipo_g3plus,
       "equipo-g1plus": equipo_g1plus,
       "equipo-g4iplus": equipo_g4iplus,
       "equipo-g3iplus": equipo_g3iplus,
       "equipo-g1iplus": equipo_g1iplus,
       "equipo-atlas-250SW": equipo_atlas_250SW,
       "equipo-atlas-150SW": equipo_atlas_150SW,
       "equipo-atlas-50SW": equipo_atlas_50SW,
       "equipo-vyda-1M": equipo_vyda_1M,
       "equipo-vyda-2M": equipo_vyda_2M,
       "equipo-vyda-3M": equipo_vyda_3M,
       "equipo-atlas-300": equipo_atlas_300,
       "equipo-atlas-152": equipo_atlas_152,
       "equipo-vyda-compact": equipo_vyda_compact,
       "equipo-C8plus": equipo_C8plus,
       "equipo-C8iplus": equipo_C8iplus,
       "equipo-C9plus": equipo_C9plus,
       "equipo-C9iplus": equipo_C9iplus,
       "equipo-atlas-360": equipo_atlas_360,
       "equipo-c1plus-SW": equipo_c1plus_SW,
       "equipo-c1a": equipo_c1a,
       "equipo-s1a": equipo_s1a,
       "equipo-g1a": equipo_g1a,
       "equipo-g1a-cdma": equipo_g1a_cdma,
       "equipo-a1a": equipo_a1a,
       "equipo-c2a": equipo_c2a,
       "equipo-s2a": equipo_s2a,
       "equipo-g2a": equipo_g2a,
       "equipo-a2a": equipo_a2a,
       "equipo-c4a": equipo_c4a,
       "equipo-s4a": equipo_s4a,
       "equipo-g4a": equipo_g4a,
       "equipo-g4a-cdma": equipo_g4a_cdma,
       "equipo-a4a": equipo_a4a,
       "equipo-cirus": equipo_cirus,
       "equipo-h1": equipo_h1,
       "equipo-atlas-260": equipo_atlas_260,
       "equipo-atlas-160": equipo_atlas_160,
       "equipo-vyda-4M": equipo_vyda_4M,
       "equipo-t200g": equipo_t200g,
       "equipo-h1-auto": equipo_h1_auto,
       "equipo-g1n": equipo_g1n,
       "equipo-v1": equipo_v1,
       "equipo-c1plusl": equipo_c1plusl,
       "equipo-h4": equipo_h4,
       "equipo-t200": equipo_t200,
       "equipo-h1plus": equipo_h1plus,
       "equipo-regesta-rp81": equipo_regesta_rp81,
       "equipo-regesta-rp82": equipo_regesta_rp82,
       "equipo-regesta-1": equipo_regesta_1,
       "equipo-f1plus": equipo_f1plus,
       "equipo-l1plus": equipo_l1plus,
       "equipo-regesta-rp61er": equipo_regesta_rp61er,
       "equipo-regesta-rp62er": equipo_regesta_rp62er,
       "equipo-3geplus": equipo_3geplus,
       "equipo-atlas-60": equipo_atlas_60,
       "equipo-3geplus-cdma": equipo_3geplus_cdma,
       "equipo-h1auto-plus": equipo_h1auto_plus,
       "equipo-k": equipo_k,
       "equipo-v": equipo_v,
       "equipo-connect-104": equipo_connect_104,
       "equipo-h1rail": equipo_h1rail,
       "equipo-kf": equipo_kf,
       "equipo-m1": equipo_m1,
       "equipo-m1f": equipo_m1f,
       "equipo-4Ge": equipo_4Ge,
       "router-oa5710v": router_oa5710v,
       "router-oa5720": router_oa5720,
       "router-oa5840": router_oa5840,
       "router-oa5850": router_oa5850,
       "router-oa5725r61er": router_oa5725r61er,
       "router-oa5725r62er": router_oa5725r62er,
       "router-oa5725a3g": router_oa5725a3g,
       "router-oa5725alte": router_oa5725alte,
       "router-esrwwanenabler": router_esrwwanenabler,
       "equipo-connect-104-v": equipo_connect_104_v,
       "equipo-connect-104-kf": equipo_connect_104_kf,
       "equipo-connect-4ge": equipo_connect_4ge,
       "equipo-bintecrsc": equipo_bintecrsc,
       "equipo-regesta-lite": equipo_regesta_lite,
       "equipo-bintecrvc": equipo_bintecrvc,
       "equipo-H2auto": equipo_H2auto,
       "equipo-iM8": equipo_iM8,
       "equipo-iM8-Plus": equipo_iM8_Plus,
       "equipo-H2auto-Plus": equipo_H2auto_Plus,
       "equipo-regesta-plc": equipo_regesta_plc,
       "equipo-Atlas-i70": equipo_Atlas_i70,
       "equipo-Atlas-i70-Plus": equipo_Atlas_i70_Plus,
       "equipo-h2rail-lite": equipo_h2rail_lite,
       "equipo-h2rail-lite2": equipo_h2rail_lite2,
       "equipo-h2rail": equipo_h2rail,
       "equipo-regesta-comp-plc": equipo_regesta_comp_plc,
       "telstatus": telstatus,
       "telAdminStatusSystem": telAdminStatusSystem,
       "telAdminStatusSystemCode": telAdminStatusSystemCode,
       "telAdminStatusSystemSwLicLev": telAdminStatusSystemSwLicLev,
       "telAdminStatusSystemSwLicSub": telAdminStatusSystemSwLicSub,
       "telAdminStatusSystemNumSerie": telAdminStatusSystemNumSerie,
       "telAdminStatusSystemPcbType": telAdminStatusSystemPcbType,
       "telAdminStatusSystemAppVersion": telAdminStatusSystemAppVersion,
       "telAdminStatusSystemBootVersion": telAdminStatusSystemBootVersion,
       "telAdminStatusSystemClock": telAdminStatusSystemClock,
       "telAdminStatusSystemBoardType": telAdminStatusSystemBoardType,
       "telAdminStatusSystemBoardRevision": telAdminStatusSystemBoardRevision,
       "telAdminStatusSystemSmartCard": telAdminStatusSystemSmartCard,
       "telAdminStatusLedsTable": telAdminStatusLedsTable,
       "telAdminStatusLedsEntry": telAdminStatusLedsEntry,
       "telAdminStatusLedNum": telAdminStatusLedNum,
       "telAdminStatusLedStatus": telAdminStatusLedStatus,
       "telAdminStatusBugsTable": telAdminStatusBugsTable,
       "telAdminStatusBugsEntry": telAdminStatusBugsEntry,
       "telAdminStatusBugNum": telAdminStatusBugNum,
       "telAdminStatusBugMsg": telAdminStatusBugMsg,
       "telAdminStatusBugsClear": telAdminStatusBugsClear,
       "telAdminStatusReload": telAdminStatusReload,
       "telAdminStatusRestart": telAdminStatusRestart,
       "telAdminStatusSaveConfig": telAdminStatusSaveConfig,
       "telAdminStatusSram": telAdminStatusSram,
       "telAdminStatusSramRecordTable": telAdminStatusSramRecordTable,
       "telAdminStatusSramRecordEntry": telAdminStatusSramRecordEntry,
       "sramRecordType": sramRecordType,
       "sramRecordSubtype": sramRecordSubtype,
       "sramRecordInstance": sramRecordInstance,
       "sramRecordItem": sramRecordItem,
       "telAdminStatusSRE": telAdminStatusSRE,
       "telAdminStatusSRESubRecordTable": telAdminStatusSRESubRecordTable,
       "telAdminStatusSRESubRecordEntry": telAdminStatusSRESubRecordEntry,
       "sreSubId": sreSubId,
       "sreSubShortName": sreSubShortName,
       "sreSubLongName": sreSubLongName,
       "sreSubNumEvent": sreSubNumEvent,
       "sreSubTraceLvlConf": sreSubTraceLvlConf,
       "sreSubSyslogLvlConf": sreSubSyslogLvlConf,
       "sreSubTrapLvlConf": sreSubTrapLvlConf,
       "sreSubTrap1LvlConf": sreSubTrap1LvlConf,
       "sreSubTrap2LvlConf": sreSubTrap2LvlConf,
       "sreSubTrap3LvlConf": sreSubTrap3LvlConf,
       "sreSubTrap4LvlConf": sreSubTrap4LvlConf,
       "telAdminStatusSREEventRecordTable": telAdminStatusSREEventRecordTable,
       "telAdminStatusSREEventRecordEntry": telAdminStatusSREEventRecordEntry,
       "sreEvnSubId": sreEvnSubId,
       "sreEvnEvnId": sreEvnEvnId,
       "sreEvnMsg": sreEvnMsg,
       "sreEvnLvl": sreEvnLvl,
       "sreEvnMeter": sreEvnMeter,
       "sreEvnStatusAct": sreEvnStatusAct,
       "sreEvnStatusCon": sreEvnStatusCon,
       "telAdminStatusSREGroupRecordTable": telAdminStatusSREGroupRecordTable,
       "telAdminStatusSREGroupRecordEntry": telAdminStatusSREGroupRecordEntry,
       "sreGrpId": sreGrpId,
       "sreGrpName": sreGrpName,
       "sreGrpStatusCon": sreGrpStatusCon,
       "sreGrpGrpSub1Id": sreGrpGrpSub1Id,
       "sreGrpGrpEvn1Id": sreGrpGrpEvn1Id,
       "sreGrpGrpSub2Id": sreGrpGrpSub2Id,
       "sreGrpGrpEvn2Id": sreGrpGrpEvn2Id,
       "sreGrpGrpSub3Id": sreGrpGrpSub3Id,
       "sreGrpGrpEvn3Id": sreGrpGrpEvn3Id,
       "sreGrpGrpSub4Id": sreGrpGrpSub4Id,
       "sreGrpGrpEvn4Id": sreGrpGrpEvn4Id,
       "sreGrpGrpSub5Id": sreGrpGrpSub5Id,
       "sreGrpGrpEvn5Id": sreGrpGrpEvn5Id,
       "sreGrpGrpSub6Id": sreGrpGrpSub6Id,
       "sreGrpGrpEvn6Id": sreGrpGrpEvn6Id,
       "sreGrpGrpSub7Id": sreGrpGrpSub7Id,
       "sreGrpGrpEvn7Id": sreGrpGrpEvn7Id,
       "sreGrpGrpSub8Id": sreGrpGrpSub8Id,
       "sreGrpGrpEvn8Id": sreGrpGrpEvn8Id,
       "sreGrpGrpSub9Id": sreGrpGrpSub9Id,
       "sreGrpGrpEvn9Id": sreGrpGrpEvn9Id,
       "sreGrpGrpSub10Id": sreGrpGrpSub10Id,
       "sreGrpGrpEvn10Id": sreGrpGrpEvn10Id,
       "sreGrpGrpSub11Id": sreGrpGrpSub11Id,
       "sreGrpGrpEvn11Id": sreGrpGrpEvn11Id,
       "sreGrpGrpSub12Id": sreGrpGrpSub12Id,
       "sreGrpGrpEvn12Id": sreGrpGrpEvn12Id,
       "sreGrpGrpSub13Id": sreGrpGrpSub13Id,
       "sreGrpGrpEvn13Id": sreGrpGrpEvn13Id,
       "sreGrpGrpSub14Id": sreGrpGrpSub14Id,
       "sreGrpGrpEvn14Id": sreGrpGrpEvn14Id,
       "sreGrpGrpSub15Id": sreGrpGrpSub15Id,
       "sreGrpGrpEvn15Id": sreGrpGrpEvn15Id,
       "sreGrpGrpSub16Id": sreGrpGrpSub16Id,
       "sreGrpGrpEvn16Id": sreGrpGrpEvn16Id,
       "sreGrpGrpSub17Id": sreGrpGrpSub17Id,
       "sreGrpGrpEvn17Id": sreGrpGrpEvn17Id,
       "sreGrpGrpSub18Id": sreGrpGrpSub18Id,
       "sreGrpGrpEvn18Id": sreGrpGrpEvn18Id,
       "sreGrpGrpSub19Id": sreGrpGrpSub19Id,
       "sreGrpGrpEvn19Id": sreGrpGrpEvn19Id,
       "sreGrpGrpSub20Id": sreGrpGrpSub20Id,
       "sreGrpGrpEvn20Id": sreGrpGrpEvn20Id,
       "telAdminStatusSREClearConf": telAdminStatusSREClearConf,
       "telAdminStatusIfTable": telAdminStatusIfTable,
       "telAdminStatusIfEntry": telAdminStatusIfEntry,
       "telAdminStatusIfIndex": telAdminStatusIfIndex,
       "telAdminStatusIfType": telAdminStatusIfType,
       "telAdminStatusIfCon": telAdminStatusIfCon,
       "telAdminStatusIfHdw": telAdminStatusIfHdw,
       "telAdminStatusEthTime": telAdminStatusEthTime,
       "telAdminConfActDev": telAdminConfActDev,
       "telAdminConfConfSavedDev": telAdminConfConfSavedDev,
       "telAdminStatusConfirmConfig": telAdminStatusConfirmConfig,
       "telAdminStatusConfirmEnabled": telAdminStatusConfirmEnabled,
       "telAdminStatusTimeoutConfirm": telAdminStatusTimeoutConfirm,
       "telAdminStatusSaveRunningConfig": telAdminStatusSaveRunningConfig,
       "telMciTraps": telMciTraps,
       "telTECircuitTrapUp": telTECircuitTrapUp,
       "telTECircuitTrapBackup": telTECircuitTrapBackup,
       "telTECircuitTrapDown": telTECircuitTrapDown,
       "telTrapVarIPAddr": telTrapVarIPAddr,
       "telTrapVarVelCir": telTrapVarVelCir,
       "telTrapVarVelBckp": telTrapVarVelBckp,
       "telTrapVarPrioBackp": telTrapVarPrioBackp,
       "telTrapVarTipoBackp": telTrapVarTipoBackp,
       "telTrapVarTipoEquip": telTrapVarTipoEquip,
       "telTrapVarCustomerName": telTrapVarCustomerName,
       "telTrapVarRouterName": telTrapVarRouterName,
       "telTrapVarRouterPort": telTrapVarRouterPort,
       "telTrapVarCircuitID": telTrapVarCircuitID,
       "telTrapVarSequenceNum": telTrapVarSequenceNum,
       "telEventTraps": telEventTraps,
       "telproto": telproto,
       "telproip": telproip,
       "teldefgw": teldefgw,
       "telProtoIpDefGwAddress": telProtoIpDefGwAddress,
       "telProtoIpDefGwCost": telProtoIpDefGwCost,
       "telProtoIpDefGwAge": telProtoIpDefGwAge,
       "telprofr": telprofr,
       "telfrLmiTable": telfrLmiTable,
       "telfrLmiEntry": telfrLmiEntry,
       "telfrLmiifIndex": telfrLmiifIndex,
       "telfrLmiBroadcas": telfrLmiBroadcas,
       "telfrLmiMonitConges": telfrLmiMonitConges,
       "telfrLmiMonitCIR": telfrLmiMonitCIR,
       "telfrLmiOrphans": telfrLmiOrphans,
       "telfrLmiIRIncrement": telfrLmiIRIncrement,
       "telfrLmiIRDecrement": telfrLmiIRDecrement,
       "telfrLmiMIRCIR": telfrLmiMIRCIR,
       "telfrCircuitTable": telfrCircuitTable,
       "telfrCircuitEntry": telfrCircuitEntry,
       "telfrCircuitifIndex": telfrCircuitifIndex,
       "telfrCircuitDlci": telfrCircuitDlci,
       "telfrCircuitCifrar": telfrCircuitCifrar,
       "telfrCircuitBack-Up-FR": telfrCircuitBack_Up_FR,
       "telfrCircuitBack-Up-RDSI": telfrCircuitBack_Up_RDSI,
       "telfrCircuitBack-Up-RDSI-siempre": telfrCircuitBack_Up_RDSI_siempre,
       "telfrCircuitName": telfrCircuitName,
       "telproisdn": telproisdn,
       "telproisdncallTable": telproisdncallTable,
       "telproisdncallEntry": telproisdncallEntry,
       "telproisdncallstatus": telproisdncallstatus,
       "telproisdncalltype": telproisdncalltype,
       "telproisdncallref": telproisdncallref,
       "telproisdncallchannel": telproisdncallchannel,
       "telproisdncallid": telproisdncallid,
       "telproisdncallcallednum": telproisdncallcallednum,
       "telproisdncallcallingnum": telproisdncallcallingnum,
       "telproisdncallchargedunits": telproisdncallchargedunits,
       "telproisdncallinittime": telproisdncallinittime,
       "telproisdncallinitdate": telproisdncallinitdate,
       "telproisdncallhistoryTable": telproisdncallhistoryTable,
       "telproisdncallhistoryEntry": telproisdncallhistoryEntry,
       "telproisdncallhistoryindex": telproisdncallhistoryindex,
       "telproisdncallhistorytype": telproisdncallhistorytype,
       "telproisdncallhistoryref": telproisdncallhistoryref,
       "telproisdncallhistorychannel": telproisdncallhistorychannel,
       "telproisdncallhistoryid": telproisdncallhistoryid,
       "telproisdncallhistorycallednum": telproisdncallhistorycallednum,
       "telproisdncallhistorycallingnum": telproisdncallhistorycallingnum,
       "telproisdncallhistorychargedunits": telproisdncallhistorychargedunits,
       "telproisdncallhistorycause": telproisdncallhistorycause,
       "telproisdncallhistorydiagnostic": telproisdncallhistorydiagnostic,
       "telproisdncallhistoryinittime": telproisdncallhistoryinittime,
       "telproisdncallhistoryendtime": telproisdncallhistoryendtime,
       "telproisdncallhistoryinitdate": telproisdncallhistoryinitdate,
       "telproisdncallhistoryenddate": telproisdncallhistoryenddate,
       "telproducts": telproducts}
)
