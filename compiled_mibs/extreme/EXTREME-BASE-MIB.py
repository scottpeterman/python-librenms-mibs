# SNMP MIB module (EXTREME-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\extreme\EXTREME-BASE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:19 2025
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

extremenetworks = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916)
)
if mibBuilder.loadTexts:
    extremenetworks.setRevisions(
        ("2019-12-06 16:20",
         "2019-09-04 21:20",
         "2019-08-05 10:31",
         "2018-09-26 23:02",
         "2019-09-18 14:00",
         "2019-05-06 15:07",
         "2019-05-03 09:00",
         "2019-04-01 17:53",
         "2019-01-28 12:35",
         "2019-01-04 14:22",
         "2019-01-04 12:55",
         "2018-11-21 19:46",
         "2018-10-09 17:02",
         "2018-09-17 12:20",
         "2018-09-14 15:31",
         "2018-07-25 11:45",
         "2018-07-02 09:00",
         "2018-06-14 18:39",
         "2018-06-07 14:05",
         "2018-05-17 13:33",
         "2018-05-01 14:46",
         "2018-03-13 09:15",
         "2018-03-01 16:31",
         "2018-02-08 14:15",
         "2018-02-07 13:47",
         "2017-11-14 12:51",
         "2017-10-25 14:22",
         "2017-10-03 14:51",
         "2017-06-28 03:38",
         "2017-06-01 11:23",
         "2017-04-21 17:48",
         "2017-04-10 13:34",
         "2016-12-05 15:03",
         "2016-10-26 15:03",
         "2016-08-05 18:09",
         "2016-07-25 08:10",
         "2016-06-21 11:42",
         "2016-04-22 12:49",
         "2016-04-08 12:47",
         "2016-03-29 00:00",
         "2016-03-17 00:00",
         "2015-05-18 00:00",
         "2015-04-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(TextualConvention, OctetString):
    status = "current"


class L4Port(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )



class ExtremeGenAddr(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class ExtremeDeviceId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class WPACipherSet(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("none", 0),
          ("wep64", 1),
          ("tkip", 2),
          ("wrap", 3),
          ("ccmp", 4),
          ("wep128", 5),
          ("other", 6))
    )


class WPAKeyMgmtSet(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("none", 0),
          ("dot1x", 1),
          ("psk", 2))
    )


class ClientAuthType(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("open", 1),
          ("wep", 2),
          ("mac-based", 3),
          ("dot1x", 4),
          ("wpa-psk", 5),
          ("web-based", 6),
          ("wpa2", 7),
          ("wpa", 8),
          ("wpa2-psk", 9))
    )



class WirelessRemoteConnectBindingType(TextualConvention, Integer32):
    status = "current"
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
          ("mac-address", 1),
          ("serial-number", 2),
          ("ip-address", 3))
    )



# MIB Managed Objects in the order of their OIDs

_ExtremeV1Traps_ObjectIdentity = ObjectIdentity
extremeV1Traps = _ExtremeV1Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 0)
)
_ExtremeAgent_ObjectIdentity = ObjectIdentity
extremeAgent = _ExtremeAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1)
)
_ExtremeSystem_ObjectIdentity = ObjectIdentity
extremeSystem = _ExtremeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1)
)
_ExtremeVlan_ObjectIdentity = ObjectIdentity
extremeVlan = _ExtremeVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2)
)
_ExtremeQos_ObjectIdentity = ObjectIdentity
extremeQos = _ExtremeQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3)
)
_ExtremePort_ObjectIdentity = ObjectIdentity
extremePort = _ExtremePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4)
)
_ExtremeVC_ObjectIdentity = ObjectIdentity
extremeVC = _ExtremeVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 5)
)
_ExtremeTrapPoll_ObjectIdentity = ObjectIdentity
extremeTrapPoll = _ExtremeTrapPoll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 6)
)
_ExtremeQosPolicy_ObjectIdentity = ObjectIdentity
extremeQosPolicy = _ExtremeQosPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7)
)
_ExtremeDlcs_ObjectIdentity = ObjectIdentity
extremeDlcs = _ExtremeDlcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 8)
)
_ExtremeFileTransfer_ObjectIdentity = ObjectIdentity
extremeFileTransfer = _ExtremeFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 10)
)
_ExtremeRtStats_ObjectIdentity = ObjectIdentity
extremeRtStats = _ExtremeRtStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 11)
)
_ExtremeEsrp_ObjectIdentity = ObjectIdentity
extremeEsrp = _ExtremeEsrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12)
)
_ExtremeEdp_ObjectIdentity = ObjectIdentity
extremeEdp = _ExtremeEdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 13)
)
_ExtremeSlb_ObjectIdentity = ObjectIdentity
extremeSlb = _ExtremeSlb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 14)
)
_ExtremeOspf_ObjectIdentity = ObjectIdentity
extremeOspf = _ExtremeOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 15)
)
_ExtremeFdb_ObjectIdentity = ObjectIdentity
extremeFdb = _ExtremeFdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16)
)
_ExtremeStp_ObjectIdentity = ObjectIdentity
extremeStp = _ExtremeStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 17)
)
_ExtremeEaps_ObjectIdentity = ObjectIdentity
extremeEaps = _ExtremeEaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18)
)
_ExtremeLacp_ObjectIdentity = ObjectIdentity
extremeLacp = _ExtremeLacp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 19)
)
_ExtremePOSMib_ObjectIdentity = ObjectIdentity
extremePOSMib = _ExtremePOSMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 20)
)
_ExtremeNPMib_ObjectIdentity = ObjectIdentity
extremeNPMib = _ExtremeNPMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 21)
)
_ExtremeNetFlow_ObjectIdentity = ObjectIdentity
extremeNetFlow = _ExtremeNetFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 22)
)
_ExtremeSnmpv3_ObjectIdentity = ObjectIdentity
extremeSnmpv3 = _ExtremeSnmpv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 23)
)
_ExtremeCable_ObjectIdentity = ObjectIdentity
extremeCable = _ExtremeCable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 24)
)
_ExtremeWireless_ObjectIdentity = ObjectIdentity
extremeWireless = _ExtremeWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25)
)
_ExtremeAP_ObjectIdentity = ObjectIdentity
extremeAP = _ExtremeAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 1)
)
_ExtremeLAC_ObjectIdentity = ObjectIdentity
extremeLAC = _ExtremeLAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 25, 2)
)
_ExtremeServices_ObjectIdentity = ObjectIdentity
extremeServices = _ExtremeServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 26)
)
_ExtremePoE_ObjectIdentity = ObjectIdentity
extremePoE = _ExtremePoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 27)
)
_ExtremeDosMib_ObjectIdentity = ObjectIdentity
extremeDosMib = _ExtremeDosMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 28)
)
_ExtremeEnhDosMib_ObjectIdentity = ObjectIdentity
extremeEnhDosMib = _ExtremeEnhDosMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 29)
)
_ExtremeClearflow_ObjectIdentity = ObjectIdentity
extremeClearflow = _ExtremeClearflow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 30)
)
_ExtremeEntity_ObjectIdentity = ObjectIdentity
extremeEntity = _ExtremeEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 31)
)
_ExtremeSwMonitor_ObjectIdentity = ObjectIdentity
extremeSwMonitor = _ExtremeSwMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 32)
)
_ExtremeStackable_ObjectIdentity = ObjectIdentity
extremeStackable = _ExtremeStackable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 33)
)
_ExtremeIpSecurity_ObjectIdentity = ObjectIdentity
extremeIpSecurity = _ExtremeIpSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 34)
)
_ExtremeUpm_ObjectIdentity = ObjectIdentity
extremeUpm = _ExtremeUpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 35)
)
_ExtremeIdMgr_ObjectIdentity = ObjectIdentity
extremeIdMgr = _ExtremeIdMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36)
)
_ExtremeMplsMIB_ObjectIdentity = ObjectIdentity
extremeMplsMIB = _ExtremeMplsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37)
)
_ExtremeHclag_ObjectIdentity = ObjectIdentity
extremeHclag = _ExtremeHclag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 38)
)
_ExtremeVM_ObjectIdentity = ObjectIdentity
extremeVM = _ExtremeVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 39)
)
_ExtremeAutoProvision_ObjectIdentity = ObjectIdentity
extremeAutoProvision = _ExtremeAutoProvision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 40)
)
_ExtremeMlag_ObjectIdentity = ObjectIdentity
extremeMlag = _ExtremeMlag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41)
)
_ExtremeCfgMgmt_ObjectIdentity = ObjectIdentity
extremeCfgMgmt = _ExtremeCfgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 42)
)
_ExtremeBfd_ObjectIdentity = ObjectIdentity
extremeBfd = _ExtremeBfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43)
)
_ExtremeMacAuthMIB_ObjectIdentity = ObjectIdentity
extremeMacAuthMIB = _ExtremeMacAuthMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 44)
)
_ExtremePbbMib_ObjectIdentity = ObjectIdentity
extremePbbMib = _ExtremePbbMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 45)
)
_ExtremeErps_ObjectIdentity = ObjectIdentity
extremeErps = _ExtremeErps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 46)
)
_ExtremeCfm_ObjectIdentity = ObjectIdentity
extremeCfm = _ExtremeCfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 47)
)
_ExtremeAcl_ObjectIdentity = ObjectIdentity
extremeAcl = _ExtremeAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 48)
)
_ExtremeVrrpMIB_ObjectIdentity = ObjectIdentity
extremeVrrpMIB = _ExtremeVrrpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 49)
)
_ExtremeOspfv3MIB_ObjectIdentity = ObjectIdentity
extremeOspfv3MIB = _ExtremeOspfv3MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 50)
)
_ExtremeBgp4V2_ObjectIdentity = ObjectIdentity
extremeBgp4V2 = _ExtremeBgp4V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51)
)
_ExtremeBgp4V2TC_ObjectIdentity = ObjectIdentity
extremeBgp4V2TC = _ExtremeBgp4V2TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 52)
)
_ExtremeInternal_ObjectIdentity = ObjectIdentity
extremeInternal = _ExtremeInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 1000)
)
_ExtremeProduct_ObjectIdentity = ObjectIdentity
extremeProduct = _ExtremeProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2)
)
_Summit1_ObjectIdentity = ObjectIdentity
summit1 = _Summit1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 1)
)
_Summit2_ObjectIdentity = ObjectIdentity
summit2 = _Summit2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 2)
)
_Summit3_ObjectIdentity = ObjectIdentity
summit3 = _Summit3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 3)
)
_Summit4_ObjectIdentity = ObjectIdentity
summit4 = _Summit4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 4)
)
_Summit4fx_ObjectIdentity = ObjectIdentity
summit4fx = _Summit4fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 5)
)
_Summit48_ObjectIdentity = ObjectIdentity
summit48 = _Summit48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 6)
)
_Summit24_ObjectIdentity = ObjectIdentity
summit24 = _Summit24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 7)
)
_BlackDiamond6800_ObjectIdentity = ObjectIdentity
blackDiamond6800 = _BlackDiamond6800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 8)
)
_BlackDiamond6808_ObjectIdentity = ObjectIdentity
blackDiamond6808 = _BlackDiamond6808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 11)
)
_Summit7iSX_ObjectIdentity = ObjectIdentity
summit7iSX = _Summit7iSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 12)
)
_Summit7iTX_ObjectIdentity = ObjectIdentity
summit7iTX = _Summit7iTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 13)
)
_Summit1iTX_ObjectIdentity = ObjectIdentity
summit1iTX = _Summit1iTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 14)
)
_Summit5i_ObjectIdentity = ObjectIdentity
summit5i = _Summit5i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 15)
)
_Summit48i_ObjectIdentity = ObjectIdentity
summit48i = _Summit48i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 16)
)
_Alpine3808_ObjectIdentity = ObjectIdentity
alpine3808 = _Alpine3808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 17)
)
_Summit1iSX_ObjectIdentity = ObjectIdentity
summit1iSX = _Summit1iSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 19)
)
_Alpine3804_ObjectIdentity = ObjectIdentity
alpine3804 = _Alpine3804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 20)
)
_Summit5iLX_ObjectIdentity = ObjectIdentity
summit5iLX = _Summit5iLX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 21)
)
_Summit5iTX_ObjectIdentity = ObjectIdentity
summit5iTX = _Summit5iTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 22)
)
_EnetSwitch24Port_ObjectIdentity = ObjectIdentity
enetSwitch24Port = _EnetSwitch24Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 23)
)
_BlackDiamond6816_ObjectIdentity = ObjectIdentity
blackDiamond6816 = _BlackDiamond6816_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 24)
)
_Summit24e3_ObjectIdentity = ObjectIdentity
summit24e3 = _Summit24e3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 25)
)
_Alpine3802_ObjectIdentity = ObjectIdentity
alpine3802 = _Alpine3802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 26)
)
_BlackDiamond6804_ObjectIdentity = ObjectIdentity
blackDiamond6804 = _BlackDiamond6804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 27)
)
_Summit48si_ObjectIdentity = ObjectIdentity
summit48si = _Summit48si_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 28)
)
_SummitPx1_ObjectIdentity = ObjectIdentity
summitPx1 = _SummitPx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 30)
)
_Summit24e2TX_ObjectIdentity = ObjectIdentity
summit24e2TX = _Summit24e2TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 40)
)
_Summit24e2SX_ObjectIdentity = ObjectIdentity
summit24e2SX = _Summit24e2SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 41)
)
_Summit200_24_ObjectIdentity = ObjectIdentity
summit200_24 = _Summit200_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 53)
)
_Summit200_48_ObjectIdentity = ObjectIdentity
summit200_48 = _Summit200_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 54)
)
_Summit300_48_ObjectIdentity = ObjectIdentity
summit300_48 = _Summit300_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 55)
)
_Bd10808_ObjectIdentity = ObjectIdentity
bd10808 = _Bd10808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 56)
)
_Summit400_48t_ObjectIdentity = ObjectIdentity
summit400_48t = _Summit400_48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 58)
)
_Summit300_24_ObjectIdentity = ObjectIdentity
summit300_24 = _Summit300_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 61)
)
_Bd8810_ObjectIdentity = ObjectIdentity
bd8810 = _Bd8810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 62)
)
_Summit400_24t_ObjectIdentity = ObjectIdentity
summit400_24t = _Summit400_24t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 63)
)
_Summit400_24p_ObjectIdentity = ObjectIdentity
summit400_24p = _Summit400_24p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 64)
)
_SummitX450_24x_ObjectIdentity = ObjectIdentity
summitX450_24x = _SummitX450_24x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 65)
)
_SummitX450_24t_ObjectIdentity = ObjectIdentity
summitX450_24t = _SummitX450_24t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 66)
)
_SummitStack_ObjectIdentity = ObjectIdentity
summitStack = _SummitStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 67)
)
_SummitWM100_ObjectIdentity = ObjectIdentity
summitWM100 = _SummitWM100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 68)
)
_SummitWM1000_ObjectIdentity = ObjectIdentity
summitWM1000 = _SummitWM1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 69)
)
_Summit200_24fx_ObjectIdentity = ObjectIdentity
summit200_24fx = _Summit200_24fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 70)
)
_SummitX450a_24t_ObjectIdentity = ObjectIdentity
summitX450a_24t = _SummitX450a_24t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 71)
)
_SummitX450e_24p_ObjectIdentity = ObjectIdentity
summitX450e_24p = _SummitX450e_24p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 72)
)
_Bd8806_ObjectIdentity = ObjectIdentity
bd8806 = _Bd8806_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 74)
)
_Altitude350_ObjectIdentity = ObjectIdentity
altitude350 = _Altitude350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 75)
)
_SummitX450a_48t_ObjectIdentity = ObjectIdentity
summitX450a_48t = _SummitX450a_48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 76)
)
_Bd12804_ObjectIdentity = ObjectIdentity
bd12804 = _Bd12804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 77)
)
_SummitX450e_48p_ObjectIdentity = ObjectIdentity
summitX450e_48p = _SummitX450e_48p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 79)
)
_SummitX450a_24tDC_ObjectIdentity = ObjectIdentity
summitX450a_24tDC = _SummitX450a_24tDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 80)
)
_SummitX450a_24xDC_ObjectIdentity = ObjectIdentity
summitX450a_24xDC = _SummitX450a_24xDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 82)
)
_SentriantCE150_ObjectIdentity = ObjectIdentity
sentriantCE150 = _SentriantCE150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 83)
)
_SummitX450a_24x_ObjectIdentity = ObjectIdentity
summitX450a_24x = _SummitX450a_24x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 84)
)
_Bd12802_ObjectIdentity = ObjectIdentity
bd12802 = _Bd12802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 85)
)
_Altitude300_ObjectIdentity = ObjectIdentity
altitude300 = _Altitude300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 86)
)
_SummitX450a_48tDC_ObjectIdentity = ObjectIdentity
summitX450a_48tDC = _SummitX450a_48tDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 87)
)
_SummitX250_24t_ObjectIdentity = ObjectIdentity
summitX250_24t = _SummitX250_24t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 88)
)
_SummitX250_24p_ObjectIdentity = ObjectIdentity
summitX250_24p = _SummitX250_24p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 89)
)
_SummitX250_24x_ObjectIdentity = ObjectIdentity
summitX250_24x = _SummitX250_24x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 90)
)
_SummitX250_48t_ObjectIdentity = ObjectIdentity
summitX250_48t = _SummitX250_48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 91)
)
_SummitX250_48p_ObjectIdentity = ObjectIdentity
summitX250_48p = _SummitX250_48p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 92)
)
_SummitVer2Stack_ObjectIdentity = ObjectIdentity
summitVer2Stack = _SummitVer2Stack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 93)
)
_SummitWM200_ObjectIdentity = ObjectIdentity
summitWM200 = _SummitWM200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 94)
)
_SummitWM2000_ObjectIdentity = ObjectIdentity
summitWM2000 = _SummitWM2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 95)
)
_SummitWM100Lite_ObjectIdentity = ObjectIdentity
summitWM100Lite = _SummitWM100Lite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 96)
)
_SummitX250_24tDC_ObjectIdentity = ObjectIdentity
summitX250_24tDC = _SummitX250_24tDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 97)
)
_SummitX250_24xDC_ObjectIdentity = ObjectIdentity
summitX250_24xDC = _SummitX250_24xDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 98)
)
_SummitX250_48tDC_ObjectIdentity = ObjectIdentity
summitX250_48tDC = _SummitX250_48tDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 99)
)
_SummitX150_24t_ObjectIdentity = ObjectIdentity
summitX150_24t = _SummitX150_24t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 100)
)
_SummitX150_24tDC_ObjectIdentity = ObjectIdentity
summitX150_24tDC = _SummitX150_24tDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 101)
)
_SummitX150_24p_ObjectIdentity = ObjectIdentity
summitX150_24p = _SummitX150_24p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 102)
)
_SummitX150_24x_ObjectIdentity = ObjectIdentity
summitX150_24x = _SummitX150_24x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 103)
)
_SummitX150_24xDC_ObjectIdentity = ObjectIdentity
summitX150_24xDC = _SummitX150_24xDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 104)
)
_SummitX150_48t_ObjectIdentity = ObjectIdentity
summitX150_48t = _SummitX150_48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 105)
)
_SummitX150_48tDC_ObjectIdentity = ObjectIdentity
summitX150_48tDC = _SummitX150_48tDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 106)
)
_SummitX150_48p_ObjectIdentity = ObjectIdentity
summitX150_48p = _SummitX150_48p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 107)
)
_SentriantAGSW_ObjectIdentity = ObjectIdentity
sentriantAGSW = _SentriantAGSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 108)
)
_SentriantAG200_ObjectIdentity = ObjectIdentity
sentriantAG200 = _SentriantAG200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 109)
)
_SummitWM20_ObjectIdentity = ObjectIdentity
summitWM20 = _SummitWM20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 110)
)
_SummitX350_24t_ObjectIdentity = ObjectIdentity
summitX350_24t = _SummitX350_24t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 111)
)
_SummitX350_48t_ObjectIdentity = ObjectIdentity
summitX350_48t = _SummitX350_48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 112)
)
_SummitX650_24t_ObjectIdentity = ObjectIdentity
summitX650_24t = _SummitX650_24t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 113)
)
_SummitX650_24x_ObjectIdentity = ObjectIdentity
summitX650_24x = _SummitX650_24x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 114)
)
_SentriantNG300_ObjectIdentity = ObjectIdentity
sentriantNG300 = _SentriantNG300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 115)
)
_Altitude360_ObjectIdentity = ObjectIdentity
altitude360 = _Altitude360_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 116)
)
_Altitude450_ObjectIdentity = ObjectIdentity
altitude450 = _Altitude450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 117)
)
_SummitX650_24x_SSns_ObjectIdentity = ObjectIdentity
summitX650_24x_SSns = _SummitX650_24x_SSns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 118)
)
_SummitX650_24t_SSns_ObjectIdentity = ObjectIdentity
summitX650_24t_SSns = _SummitX650_24t_SSns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 119)
)
_SummitX650_24x_SS_ObjectIdentity = ObjectIdentity
summitX650_24x_SS = _SummitX650_24x_SS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 120)
)
_SummitX650_24t_SS_ObjectIdentity = ObjectIdentity
summitX650_24t_SS = _SummitX650_24t_SS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 121)
)
_SummitX650_24x_10G8X_ObjectIdentity = ObjectIdentity
summitX650_24x_10G8X = _SummitX650_24x_10G8X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 122)
)
_SummitX650_24t_10G8X_ObjectIdentity = ObjectIdentity
summitX650_24t_10G8X = _SummitX650_24t_10G8X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 123)
)
_SummitX650_24x_SS256_ObjectIdentity = ObjectIdentity
summitX650_24x_SS256 = _SummitX650_24x_SS256_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 124)
)
_SummitX650_24t_SS256_ObjectIdentity = ObjectIdentity
summitX650_24t_SS256 = _SummitX650_24t_SS256_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 125)
)
_SummitX650_24x_SS512_ObjectIdentity = ObjectIdentity
summitX650_24x_SS512 = _SummitX650_24x_SS512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 126)
)
_SummitX650_24t_SS512_ObjectIdentity = ObjectIdentity
summitX650_24t_SS512 = _SummitX650_24t_SS512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 127)
)
_Bd20808_ObjectIdentity = ObjectIdentity
bd20808 = _Bd20808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 128)
)
_Nwi_e450a_ObjectIdentity = ObjectIdentity
nwi_e450a = _Nwi_e450a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 129)
)
_SentriantPS200v1_ObjectIdentity = ObjectIdentity
sentriantPS200v1 = _SentriantPS200v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 130)
)
_WirelessProducts_ObjectIdentity = ObjectIdentity
wirelessProducts = _WirelessProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 131)
)
_SummitWM3700_ObjectIdentity = ObjectIdentity
summitWM3700 = _SummitWM3700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 131, 15)
)
_SummitWM3600_ObjectIdentity = ObjectIdentity
summitWM3600 = _SummitWM3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 131, 16)
)
_SummitWM3400_ObjectIdentity = ObjectIdentity
summitWM3400 = _SummitWM3400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 131, 18)
)
_Bd20804_ObjectIdentity = ObjectIdentity
bd20804 = _Bd20804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 132)
)
_SummitX480_48t_ObjectIdentity = ObjectIdentity
summitX480_48t = _SummitX480_48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 133)
)
_SummitX480_48t_SS_ObjectIdentity = ObjectIdentity
summitX480_48t_SS = _SummitX480_48t_SS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 134)
)
_SummitX480_48t_10G4X_ObjectIdentity = ObjectIdentity
summitX480_48t_10G4X = _SummitX480_48t_10G4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 135)
)
_SummitX480_48t_SS128_ObjectIdentity = ObjectIdentity
summitX480_48t_SS128 = _SummitX480_48t_SS128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 136)
)
_SummitX480_24x_ObjectIdentity = ObjectIdentity
summitX480_24x = _SummitX480_24x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 137)
)
_SummitX480_24x_SS_ObjectIdentity = ObjectIdentity
summitX480_24x_SS = _SummitX480_24x_SS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 138)
)
_SummitX480_24x_10G4X_ObjectIdentity = ObjectIdentity
summitX480_24x_10G4X = _SummitX480_24x_10G4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 139)
)
_SummitX480_24x_SS128_ObjectIdentity = ObjectIdentity
summitX480_24x_SS128 = _SummitX480_24x_SS128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 140)
)
_SummitX480_48x_ObjectIdentity = ObjectIdentity
summitX480_48x = _SummitX480_48x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 141)
)
_SummitX480_48x_SS_ObjectIdentity = ObjectIdentity
summitX480_48x_SS = _SummitX480_48x_SS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 142)
)
_SummitX480_48x_10G4X_ObjectIdentity = ObjectIdentity
summitX480_48x_10G4X = _SummitX480_48x_10G4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 143)
)
_SummitX480_48x_SS128_ObjectIdentity = ObjectIdentity
summitX480_48x_SS128 = _SummitX480_48x_SS128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 144)
)
_Altitude3510_ObjectIdentity = ObjectIdentity
altitude3510 = _Altitude3510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 145)
)
_Altitude3550_ObjectIdentity = ObjectIdentity
altitude3550 = _Altitude3550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 146)
)
_Altitude4610_ObjectIdentity = ObjectIdentity
altitude4610 = _Altitude4610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 148)
)
_Altitude4620_ObjectIdentity = ObjectIdentity
altitude4620 = _Altitude4620_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 149)
)
_SummitX450e_24t_ObjectIdentity = ObjectIdentity
summitX450e_24t = _SummitX450e_24t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 150)
)
_SummitX450e_48t_ObjectIdentity = ObjectIdentity
summitX450e_48t = _SummitX450e_48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 151)
)
_SummitX460_24t_ObjectIdentity = ObjectIdentity
summitX460_24t = _SummitX460_24t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 152)
)
_SummitX460_24p_ObjectIdentity = ObjectIdentity
summitX460_24p = _SummitX460_24p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 153)
)
_SummitX460_24x_ObjectIdentity = ObjectIdentity
summitX460_24x = _SummitX460_24x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 154)
)
_SummitX460_48t_ObjectIdentity = ObjectIdentity
summitX460_48t = _SummitX460_48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 155)
)
_SummitX460_48p_ObjectIdentity = ObjectIdentity
summitX460_48p = _SummitX460_48p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 156)
)
_SummitX460_48x_ObjectIdentity = ObjectIdentity
summitX460_48x = _SummitX460_48x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 157)
)
_Altitude4700_ObjectIdentity = ObjectIdentity
altitude4700 = _Altitude4700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 158)
)
_SummitX480_24x_SSV80_ObjectIdentity = ObjectIdentity
summitX480_24x_SSV80 = _SummitX480_24x_SSV80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 159)
)
_SummitX480_48x_SSV80_ObjectIdentity = ObjectIdentity
summitX480_48x_SSV80 = _SummitX480_48x_SSV80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 160)
)
_SummitX480_48t_SSV80_ObjectIdentity = ObjectIdentity
summitX480_48t_SSV80 = _SummitX480_48t_SSV80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 161)
)
_SummitX650_24x_40G4X_ObjectIdentity = ObjectIdentity
summitX650_24x_40G4X = _SummitX650_24x_40G4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 162)
)
_SummitX650_24t_40G4X_ObjectIdentity = ObjectIdentity
summitX650_24t_40G4X = _SummitX650_24t_40G4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 163)
)
_SummitX480_24x_40G4X_ObjectIdentity = ObjectIdentity
summitX480_24x_40G4X = _SummitX480_24x_40G4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 164)
)
_SummitX480_48x_40G4X_ObjectIdentity = ObjectIdentity
summitX480_48x_40G4X = _SummitX480_48x_40G4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 165)
)
_SummitX480_48t_40G4X_ObjectIdentity = ObjectIdentity
summitX480_48t_40G4X = _SummitX480_48t_40G4X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 166)
)
_SummitX670_48x_ObjectIdentity = ObjectIdentity
summitX670_48x = _SummitX670_48x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 167)
)
_SummitX670v_48x_ObjectIdentity = ObjectIdentity
summitX670v_48x = _SummitX670v_48x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 168)
)
_E4g_400_ObjectIdentity = ObjectIdentity
e4g_400 = _E4g_400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 169)
)
_Bdx8_ObjectIdentity = ObjectIdentity
bdx8 = _Bdx8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 170)
)
_E4g_200_ObjectIdentity = ObjectIdentity
e4g_200 = _E4g_200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 171)
)
_SummitX440_8t_ObjectIdentity = ObjectIdentity
summitX440_8t = _SummitX440_8t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 172)
)
_SummitX440_8p_ObjectIdentity = ObjectIdentity
summitX440_8p = _SummitX440_8p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 173)
)
_SummitX440_24t_ObjectIdentity = ObjectIdentity
summitX440_24t = _SummitX440_24t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 174)
)
_SummitX440_24p_ObjectIdentity = ObjectIdentity
summitX440_24p = _SummitX440_24p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 175)
)
_SummitX440_48t_ObjectIdentity = ObjectIdentity
summitX440_48t = _SummitX440_48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 176)
)
_SummitX440_48p_ObjectIdentity = ObjectIdentity
summitX440_48p = _SummitX440_48p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 177)
)
_SummitX440_24t_10G_ObjectIdentity = ObjectIdentity
summitX440_24t_10G = _SummitX440_24t_10G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 178)
)
_SummitX440_24p_10G_ObjectIdentity = ObjectIdentity
summitX440_24p_10G = _SummitX440_24p_10G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 179)
)
_SummitX440_48t_10G_ObjectIdentity = ObjectIdentity
summitX440_48t_10G = _SummitX440_48t_10G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 180)
)
_SummitX440_48p_10G_ObjectIdentity = ObjectIdentity
summitX440_48p_10G = _SummitX440_48p_10G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 181)
)
_Ags100_24t_ObjectIdentity = ObjectIdentity
ags100_24t = _Ags100_24t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 182)
)
_Ags150_24p_ObjectIdentity = ObjectIdentity
ags150_24p = _Ags150_24p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 183)
)
_SummitX670v_48t_ObjectIdentity = ObjectIdentity
summitX670v_48t = _SummitX670v_48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 184)
)
_SummitX440_L2_24t_ObjectIdentity = ObjectIdentity
summitX440_L2_24t = _SummitX440_L2_24t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 185)
)
_SummitX440_L2_48t_ObjectIdentity = ObjectIdentity
summitX440_L2_48t = _SummitX440_L2_48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 186)
)
_E4g_200_12x_ObjectIdentity = ObjectIdentity
e4g_200_12x = _E4g_200_12x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 187)
)
_SummitX440_24x_ObjectIdentity = ObjectIdentity
summitX440_24x = _SummitX440_24x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 188)
)
_SummitX440_24x_10g_ObjectIdentity = ObjectIdentity
summitX440_24x_10g = _SummitX440_24x_10g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 189)
)
_SummitX430_24t_ObjectIdentity = ObjectIdentity
summitX430_24t = _SummitX430_24t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 190)
)
_SummitX430_48t_ObjectIdentity = ObjectIdentity
summitX430_48t = _SummitX430_48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 191)
)
_SummitX440_24tdc_ObjectIdentity = ObjectIdentity
summitX440_24tdc = _SummitX440_24tdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 192)
)
_SummitX440_48tdc_ObjectIdentity = ObjectIdentity
summitX440_48tdc = _SummitX440_48tdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 193)
)
_SummitX770_32q_ObjectIdentity = ObjectIdentity
summitX770_32q = _SummitX770_32q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 194)
)
_SummitX670G2_48x_4q_ObjectIdentity = ObjectIdentity
summitX670G2_48x_4q = _SummitX670G2_48x_4q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 195)
)
_SummitX670G2_72x_ObjectIdentity = ObjectIdentity
summitX670G2_72x = _SummitX670G2_72x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 196)
)
_SummitX460G2_24t_10G4_ObjectIdentity = ObjectIdentity
summitX460G2_24t_10G4 = _SummitX460G2_24t_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 197)
)
_SummitX460G2_24p_10G4_ObjectIdentity = ObjectIdentity
summitX460G2_24p_10G4 = _SummitX460G2_24p_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 198)
)
_SummitX460G2_24x_10G4_ObjectIdentity = ObjectIdentity
summitX460G2_24x_10G4 = _SummitX460G2_24x_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 199)
)
_SummitX460G2_48t_10G4_ObjectIdentity = ObjectIdentity
summitX460G2_48t_10G4 = _SummitX460G2_48t_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 200)
)
_SummitX460G2_48p_10G4_ObjectIdentity = ObjectIdentity
summitX460G2_48p_10G4 = _SummitX460G2_48p_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 201)
)
_SummitX460G2_48x_10G4_ObjectIdentity = ObjectIdentity
summitX460G2_48x_10G4 = _SummitX460G2_48x_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 202)
)
_SummitX430_8p_ObjectIdentity = ObjectIdentity
summitX430_8p = _SummitX430_8p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 203)
)
_SummitX430_24p_ObjectIdentity = ObjectIdentity
summitX430_24p = _SummitX430_24p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 204)
)
_AviatCtr_8440_ObjectIdentity = ObjectIdentity
aviatCtr_8440 = _AviatCtr_8440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 205)
)
_SummitX450G2_24t_10G4_ObjectIdentity = ObjectIdentity
summitX450G2_24t_10G4 = _SummitX450G2_24t_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 206)
)
_SummitX450G2_24p_10G4_ObjectIdentity = ObjectIdentity
summitX450G2_24p_10G4 = _SummitX450G2_24p_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 207)
)
_SummitX450G2_48t_10G4_ObjectIdentity = ObjectIdentity
summitX450G2_48t_10G4 = _SummitX450G2_48t_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 208)
)
_SummitX450G2_48p_10G4_ObjectIdentity = ObjectIdentity
summitX450G2_48p_10G4 = _SummitX450G2_48p_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 209)
)
_SummitX450G2_24t_G4_ObjectIdentity = ObjectIdentity
summitX450G2_24t_G4 = _SummitX450G2_24t_G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 210)
)
_SummitX450G2_24p_G4_ObjectIdentity = ObjectIdentity
summitX450G2_24p_G4 = _SummitX450G2_24p_G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 211)
)
_SummitX450G2_48t_G4_ObjectIdentity = ObjectIdentity
summitX450G2_48t_G4 = _SummitX450G2_48t_G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 212)
)
_SummitX450G2_48p_G4_ObjectIdentity = ObjectIdentity
summitX450G2_48p_G4 = _SummitX450G2_48p_G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 213)
)
_SummitX460G2_24t_G4_ObjectIdentity = ObjectIdentity
summitX460G2_24t_G4 = _SummitX460G2_24t_G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 214)
)
_SummitX460G2_24p_G4_ObjectIdentity = ObjectIdentity
summitX460G2_24p_G4 = _SummitX460G2_24p_G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 215)
)
_SummitX460G2_48t_G4_ObjectIdentity = ObjectIdentity
summitX460G2_48t_G4 = _SummitX460G2_48t_G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 216)
)
_SummitX460G2_48p_G4_ObjectIdentity = ObjectIdentity
summitX460G2_48p_G4 = _SummitX460G2_48p_G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 217)
)
_OneC_A_600_ObjectIdentity = ObjectIdentity
oneC_A_600 = _OneC_A_600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 218)
)
_OneC_V_ObjectIdentity = ObjectIdentity
oneC_V = _OneC_V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 219)
)
_SummitX440G2_48p_10G4_ObjectIdentity = ObjectIdentity
summitX440G2_48p_10G4 = _SummitX440G2_48p_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 220)
)
_SummitX440G2_48t_10G4_ObjectIdentity = ObjectIdentity
summitX440G2_48t_10G4 = _SummitX440G2_48t_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 221)
)
_SummitX440G2_48t_10G4_DC_ObjectIdentity = ObjectIdentity
summitX440G2_48t_10G4_DC = _SummitX440G2_48t_10G4_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 222)
)
_SummitX440G2_24p_10G4_ObjectIdentity = ObjectIdentity
summitX440G2_24p_10G4 = _SummitX440G2_24p_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 223)
)
_SummitX440G2_24t_10G4_ObjectIdentity = ObjectIdentity
summitX440G2_24t_10G4 = _SummitX440G2_24t_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 224)
)
_SummitX440G2_24t_10G4_DC_ObjectIdentity = ObjectIdentity
summitX440G2_24t_10G4_DC = _SummitX440G2_24t_10G4_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 225)
)
_SummitX440G2_24x_10G4_ObjectIdentity = ObjectIdentity
summitX440G2_24x_10G4 = _SummitX440G2_24x_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 226)
)
_SummitX440G2_12p_10G4_ObjectIdentity = ObjectIdentity
summitX440G2_12p_10G4 = _SummitX440G2_12p_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 227)
)
_SummitX440G2_12t_10G4_ObjectIdentity = ObjectIdentity
summitX440G2_12t_10G4 = _SummitX440G2_12t_10G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 228)
)
_SummitX440G2_12t8fx_G4_ObjectIdentity = ObjectIdentity
summitX440G2_12t8fx_G4 = _SummitX440G2_12t8fx_G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 229)
)
_SummitX440G2_24t_G4_ObjectIdentity = ObjectIdentity
summitX440G2_24t_G4 = _SummitX440G2_24t_G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 230)
)
_SummitX440G2_24fx_G4_ObjectIdentity = ObjectIdentity
summitX440G2_24fx_G4 = _SummitX440G2_24fx_G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 231)
)
_SummitX620_16T_ObjectIdentity = ObjectIdentity
summitX620_16T = _SummitX620_16T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 232)
)
_SummitX620_16P_ObjectIdentity = ObjectIdentity
summitX620_16P = _SummitX620_16P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 233)
)
_SummitX620_16X_ObjectIdentity = ObjectIdentity
summitX620_16X = _SummitX620_16X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 234)
)
_SummitX620_8T_2X_ObjectIdentity = ObjectIdentity
summitX620_8T_2X = _SummitX620_8T_2X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 235)
)
_SummitX620_10X_ObjectIdentity = ObjectIdentity
summitX620_10X = _SummitX620_10X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 236)
)
_SummitX870_32C_ObjectIdentity = ObjectIdentity
summitX870_32C = _SummitX870_32C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 237)
)
_SummitX870_96X_8C_ObjectIdentity = ObjectIdentity
summitX870_96X_8C = _SummitX870_96X_8C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 238)
)
_Ecos_ObjectIdentity = ObjectIdentity
ecos = _Ecos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 239)
)
_Isw_4P_2_G2_ObjectIdentity = ObjectIdentity
isw_4P_2_G2 = _Isw_4P_2_G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 240)
)
_Isw_8P_G4_ObjectIdentity = ObjectIdentity
isw_8P_G4 = _Isw_8P_G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 241)
)
_Isw_4GP_2G_G2_ObjectIdentity = ObjectIdentity
isw_4GP_2G_G2 = _Isw_4GP_2G_G2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 242)
)
_Isw_8GP_G4_ObjectIdentity = ObjectIdentity
isw_8GP_G4 = _Isw_8GP_G4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 243)
)
_X690_48t_4q_2c_ObjectIdentity = ObjectIdentity
x690_48t_4q_2c = _X690_48t_4q_2c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 247)
)
_X690_48x_4q_2c_ObjectIdentity = ObjectIdentity
x690_48x_4q_2c = _X690_48x_4q_2c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 248)
)
_ExtremeSNSxNSSxA_ObjectIdentity = ObjectIdentity
extremeSNSxNSSxA = _ExtremeSNSxNSSxA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 249)
)
if mibBuilder.loadTexts:
    extremeSNSxNSSxA.setStatus("current")
_ExtremeNSxAx20_ObjectIdentity = ObjectIdentity
extremeNSxAx20 = _ExtremeNSxAx20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 250)
)
if mibBuilder.loadTexts:
    extremeNSxAx20.setStatus("current")
_ExtremeNACxAx20_ObjectIdentity = ObjectIdentity
extremeNACxAx20 = _ExtremeNACxAx20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 251)
)
if mibBuilder.loadTexts:
    extremeNACxAx20.setStatus("current")
_ExtremeIAxV_ObjectIdentity = ObjectIdentity
extremeIAxV = _ExtremeIAxV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 252)
)
if mibBuilder.loadTexts:
    extremeIAxV.setStatus("current")
_ExtremeIAxAx20_ObjectIdentity = ObjectIdentity
extremeIAxAx20 = _ExtremeIAxAx20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 253)
)
if mibBuilder.loadTexts:
    extremeIAxAx20.setStatus("current")
_ExtremeIAxAx300_ObjectIdentity = ObjectIdentity
extremeIAxAx300 = _ExtremeIAxAx300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 254)
)
if mibBuilder.loadTexts:
    extremeIAxAx300.setStatus("current")
_ExtremePVxV_ObjectIdentity = ObjectIdentity
extremePVxV = _ExtremePVxV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 255)
)
if mibBuilder.loadTexts:
    extremePVxV.setStatus("current")
_ExtremePVxAx300_ObjectIdentity = ObjectIdentity
extremePVxAx300 = _ExtremePVxAx300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 256)
)
if mibBuilder.loadTexts:
    extremePVxAx300.setStatus("current")
_SummitX460_G2_16mp_32p_10GE4_ObjectIdentity = ObjectIdentity
summitX460_G2_16mp_32p_10GE4 = _SummitX460_G2_16mp_32p_10GE4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 257)
)
_SummitX460G2_24p_24hp_ObjectIdentity = ObjectIdentity
summitX460G2_24p_24hp = _SummitX460G2_24p_24hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 258)
)
_SummitX460G2_24t_24ht_ObjectIdentity = ObjectIdentity
summitX460G2_24t_24ht = _SummitX460G2_24t_24ht_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 259)
)
_Extreme210_12t_GE2_ObjectIdentity = ObjectIdentity
extreme210_12t_GE2 = _Extreme210_12t_GE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 260)
)
if mibBuilder.loadTexts:
    extreme210_12t_GE2.setStatus("current")
_Extreme210_12p_GE2_ObjectIdentity = ObjectIdentity
extreme210_12p_GE2 = _Extreme210_12p_GE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 261)
)
if mibBuilder.loadTexts:
    extreme210_12p_GE2.setStatus("current")
_Extreme210_24t_GE2_ObjectIdentity = ObjectIdentity
extreme210_24t_GE2 = _Extreme210_24t_GE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 262)
)
if mibBuilder.loadTexts:
    extreme210_24t_GE2.setStatus("current")
_Extreme210_24p_GE2_ObjectIdentity = ObjectIdentity
extreme210_24p_GE2 = _Extreme210_24p_GE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 263)
)
if mibBuilder.loadTexts:
    extreme210_24p_GE2.setStatus("current")
_Extreme210_48t_GE4_ObjectIdentity = ObjectIdentity
extreme210_48t_GE4 = _Extreme210_48t_GE4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 264)
)
if mibBuilder.loadTexts:
    extreme210_48t_GE4.setStatus("current")
_Extreme210_48p_GE4_ObjectIdentity = ObjectIdentity
extreme210_48p_GE4 = _Extreme210_48p_GE4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 265)
)
if mibBuilder.loadTexts:
    extreme210_48p_GE4.setStatus("current")
_Extreme220_12t_10GE2_ObjectIdentity = ObjectIdentity
extreme220_12t_10GE2 = _Extreme220_12t_10GE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 266)
)
if mibBuilder.loadTexts:
    extreme220_12t_10GE2.setStatus("current")
_Extreme220_12p_10GE2_ObjectIdentity = ObjectIdentity
extreme220_12p_10GE2 = _Extreme220_12p_10GE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 267)
)
if mibBuilder.loadTexts:
    extreme220_12p_10GE2.setStatus("current")
_Extreme220_24t_10GE2_ObjectIdentity = ObjectIdentity
extreme220_24t_10GE2 = _Extreme220_24t_10GE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 268)
)
if mibBuilder.loadTexts:
    extreme220_24t_10GE2.setStatus("current")
_Extreme220_24p_10GE2_ObjectIdentity = ObjectIdentity
extreme220_24p_10GE2 = _Extreme220_24p_10GE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 269)
)
if mibBuilder.loadTexts:
    extreme220_24p_10GE2.setStatus("current")
_Extreme220_48t_10GE4_ObjectIdentity = ObjectIdentity
extreme220_48t_10GE4 = _Extreme220_48t_10GE4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 270)
)
if mibBuilder.loadTexts:
    extreme220_48t_10GE4.setStatus("current")
_Extreme220_48p_10GE4_ObjectIdentity = ObjectIdentity
extreme220_48p_10GE4 = _Extreme220_48p_10GE4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 271)
)
if mibBuilder.loadTexts:
    extreme220_48p_10GE4.setStatus("current")
_Extreme240_8mt_16t_10GE4_ObjectIdentity = ObjectIdentity
extreme240_8mt_16t_10GE4 = _Extreme240_8mt_16t_10GE4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 272)
)
if mibBuilder.loadTexts:
    extreme240_8mt_16t_10GE4.setStatus("current")
_Extreme240_8mp_16p_10GE4_ObjectIdentity = ObjectIdentity
extreme240_8mp_16p_10GE4 = _Extreme240_8mp_16p_10GE4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 273)
)
if mibBuilder.loadTexts:
    extreme240_8mp_16p_10GE4.setStatus("current")
_Extreme240_32t_16mt_10GE6_ObjectIdentity = ObjectIdentity
extreme240_32t_16mt_10GE6 = _Extreme240_32t_16mt_10GE6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 274)
)
if mibBuilder.loadTexts:
    extreme240_32t_16mt_10GE6.setStatus("current")
_Extreme240_32p_16mp_10GE6_ObjectIdentity = ObjectIdentity
extreme240_32p_16mp_10GE6 = _Extreme240_32p_16mp_10GE6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 275)
)
if mibBuilder.loadTexts:
    extreme240_32p_16mp_10GE6.setStatus("current")
_Extreme825_48v_6c_ObjectIdentity = ObjectIdentity
extreme825_48v_6c = _Extreme825_48v_6c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 276)
)
if mibBuilder.loadTexts:
    extreme825_48v_6c.setStatus("current")
_ExtremeNMSxAx25_ObjectIdentity = ObjectIdentity
extremeNMSxAx25 = _ExtremeNMSxAx25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 277)
)
if mibBuilder.loadTexts:
    extremeNMSxAx25.setStatus("current")
_ExtremeNMSxAx305_ObjectIdentity = ObjectIdentity
extremeNMSxAx305 = _ExtremeNMSxAx305_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 278)
)
if mibBuilder.loadTexts:
    extremeNMSxAx305.setStatus("current")
_ExtremeIAxAx25_ObjectIdentity = ObjectIdentity
extremeIAxAx25 = _ExtremeIAxAx25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 279)
)
if mibBuilder.loadTexts:
    extremeIAxAx25.setStatus("current")
_ExtremeIAxAx305_ObjectIdentity = ObjectIdentity
extremeIAxAx305 = _ExtremeIAxAx305_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 280)
)
if mibBuilder.loadTexts:
    extremeIAxAx305.setStatus("current")
_ExtremePVxAx305_ObjectIdentity = ObjectIdentity
extremePVxAx305 = _ExtremePVxAx305_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 281)
)
if mibBuilder.loadTexts:
    extremePVxAx305.setStatus("current")
_ExtremeEMPx35_ObjectIdentity = ObjectIdentity
extremeEMPx35 = _ExtremeEMPx35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 282)
)
if mibBuilder.loadTexts:
    extremeEMPx35.setStatus("current")
_ExtremeEMPx5310_ObjectIdentity = ObjectIdentity
extremeEMPx5310 = _ExtremeEMPx5310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 283)
)
if mibBuilder.loadTexts:
    extremeEMPx5310.setStatus("current")
_ExtremeEMPxV_ObjectIdentity = ObjectIdentity
extremeEMPxV = _ExtremeEMPxV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 284)
)
if mibBuilder.loadTexts:
    extremeEMPxV.setStatus("current")
_XtremeWhitebox_ObjectIdentity = ObjectIdentity
xtremeWhitebox = _XtremeWhitebox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 286)
)
_Vm386EXOS_ObjectIdentity = ObjectIdentity
vm386EXOS = _Vm386EXOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 291)
)
if mibBuilder.loadTexts:
    vm386EXOS.setStatus("current")
_ExtremeNMSxV_ObjectIdentity = ObjectIdentity
extremeNMSxV = _ExtremeNMSxV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 292)
)
if mibBuilder.loadTexts:
    extremeNMSxV.setStatus("current")
_ExtremeSSxIxA_ObjectIdentity = ObjectIdentity
extremeSSxIxA = _ExtremeSSxIxA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 293)
)
if mibBuilder.loadTexts:
    extremeSSxIxA.setStatus("current")
_ExtremeESEx2000_ObjectIdentity = ObjectIdentity
extremeESEx2000 = _ExtremeESEx2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 294)
)
if mibBuilder.loadTexts:
    extremeESEx2000.setStatus("current")
_ExtremeFabricManager_ObjectIdentity = ObjectIdentity
extremeFabricManager = _ExtremeFabricManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 295)
)
if mibBuilder.loadTexts:
    extremeFabricManager.setStatus("current")
_X590_24t_1q_2c_ObjectIdentity = ObjectIdentity
x590_24t_1q_2c = _X590_24t_1q_2c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 296)
)
if mibBuilder.loadTexts:
    x590_24t_1q_2c.setStatus("current")
_X590_24x_1q_1c_ObjectIdentity = ObjectIdentity
x590_24x_1q_1c = _X590_24x_1q_1c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 297)
)
if mibBuilder.loadTexts:
    x590_24x_1q_1c.setStatus("current")
_SlxOsAcctonAS771232X_ObjectIdentity = ObjectIdentity
slxOsAcctonAS771232X = _SlxOsAcctonAS771232X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 298)
)
if mibBuilder.loadTexts:
    slxOsAcctonAS771232X.setStatus("current")
_SlxOsDniAG9032v1_ObjectIdentity = ObjectIdentity
slxOsDniAG9032v1 = _SlxOsDniAG9032v1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 299)
)
if mibBuilder.loadTexts:
    slxOsDniAG9032v1.setStatus("current")
_Es6108x32c_ObjectIdentity = ObjectIdentity
es6108x32c = _Es6108x32c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 300)
)
if mibBuilder.loadTexts:
    es6108x32c.setStatus("current")
_Es6108x48vx8c_ObjectIdentity = ObjectIdentity
es6108x48vx8c = _Es6108x48vx8c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 301)
)
if mibBuilder.loadTexts:
    es6108x48vx8c.setStatus("current")
_Vsp7432CQ_ObjectIdentity = ObjectIdentity
vsp7432CQ = _Vsp7432CQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 302)
)
if mibBuilder.loadTexts:
    vsp7432CQ.setStatus("current")
_Vsp7456VSC_ObjectIdentity = ObjectIdentity
vsp7456VSC = _Vsp7456VSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 303)
)
if mibBuilder.loadTexts:
    vsp7456VSC.setStatus("current")
_ExtremeSLX9030_ObjectIdentity = ObjectIdentity
extremeSLX9030 = _ExtremeSLX9030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 304)
)
if mibBuilder.loadTexts:
    extremeSLX9030.setStatus("current")
_ExtremeSLX9030T_ObjectIdentity = ObjectIdentity
extremeSLX9030T = _ExtremeSLX9030T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 305)
)
if mibBuilder.loadTexts:
    extremeSLX9030T.setStatus("current")
_ExtremeSLX9640_ObjectIdentity = ObjectIdentity
extremeSLX9640 = _ExtremeSLX9640_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 306)
)
if mibBuilder.loadTexts:
    extremeSLX9640.setStatus("current")
_Vsp1100_ObjectIdentity = ObjectIdentity
vsp1100 = _Vsp1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 307)
)
if mibBuilder.loadTexts:
    vsp1100.setStatus("current")
_ExtremeCspAwsSubnetType_ObjectIdentity = ObjectIdentity
extremeCspAwsSubnetType = _ExtremeCspAwsSubnetType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 308)
)
if mibBuilder.loadTexts:
    extremeCspAwsSubnetType.setStatus("current")
_ExtremeCspGcpSubnetType_ObjectIdentity = ObjectIdentity
extremeCspGcpSubnetType = _ExtremeCspGcpSubnetType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 309)
)
if mibBuilder.loadTexts:
    extremeCspGcpSubnetType.setStatus("current")
_ExtremeCspAzureSubnetType_ObjectIdentity = ObjectIdentity
extremeCspAzureSubnetType = _ExtremeCspAzureSubnetType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 310)
)
if mibBuilder.loadTexts:
    extremeCspAzureSubnetType.setStatus("current")
_ExtremeMcsVmwareHypervisorType_ObjectIdentity = ObjectIdentity
extremeMcsVmwareHypervisorType = _ExtremeMcsVmwareHypervisorType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 311)
)
if mibBuilder.loadTexts:
    extremeMcsVmwareHypervisorType.setStatus("current")
_X465_48t_ObjectIdentity = ObjectIdentity
x465_48t = _X465_48t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 312)
)
if mibBuilder.loadTexts:
    x465_48t.setStatus("current")
_X465_48p_ObjectIdentity = ObjectIdentity
x465_48p = _X465_48p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 313)
)
if mibBuilder.loadTexts:
    x465_48p.setStatus("current")
_X465_48w_ObjectIdentity = ObjectIdentity
x465_48w = _X465_48w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 314)
)
if mibBuilder.loadTexts:
    x465_48w.setStatus("current")
_X465_24mu_ObjectIdentity = ObjectIdentity
x465_24mu = _X465_24mu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 315)
)
if mibBuilder.loadTexts:
    x465_24mu.setStatus("current")
_X465_24mu_24w_ObjectIdentity = ObjectIdentity
x465_24mu_24w = _X465_24mu_24w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 316)
)
if mibBuilder.loadTexts:
    x465_24mu_24w.setStatus("current")
_X465_24w_ObjectIdentity = ObjectIdentity
x465_24w = _X465_24w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 319)
)
if mibBuilder.loadTexts:
    x465_24w.setStatus("current")
_X725_48y_8c_ObjectIdentity = ObjectIdentity
x725_48y_8c = _X725_48y_8c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 320)
)
if mibBuilder.loadTexts:
    x725_48y_8c.setStatus("current")
_ExtremeSnVirtualSensor100_ObjectIdentity = ObjectIdentity
extremeSnVirtualSensor100 = _ExtremeSnVirtualSensor100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 321)
)
if mibBuilder.loadTexts:
    extremeSnVirtualSensor100.setStatus("current")
_ExtremeSnVirtualSensor250_ObjectIdentity = ObjectIdentity
extremeSnVirtualSensor250 = _ExtremeSnVirtualSensor250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 322)
)
if mibBuilder.loadTexts:
    extremeSnVirtualSensor250.setStatus("current")
_Vsp7400_48Y_8C_ObjectIdentity = ObjectIdentity
vsp7400_48Y_8C = _Vsp7400_48Y_8C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 325)
)
if mibBuilder.loadTexts:
    vsp7400_48Y_8C.setStatus("current")
_ExtremeVirtualTAP_ObjectIdentity = ObjectIdentity
extremeVirtualTAP = _ExtremeVirtualTAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 326)
)
if mibBuilder.loadTexts:
    extremeVirtualTAP.setStatus("current")
_ExtremeVirtualPB_ObjectIdentity = ObjectIdentity
extremeVirtualPB = _ExtremeVirtualPB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 327)
)
if mibBuilder.loadTexts:
    extremeVirtualPB.setStatus("current")
_X695_48y_8c_ObjectIdentity = ObjectIdentity
x695_48y_8c = _X695_48y_8c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 328)
)
if mibBuilder.loadTexts:
    x695_48y_8c.setStatus("current")
_ExtremeOnieStack_ObjectIdentity = ObjectIdentity
extremeOnieStack = _ExtremeOnieStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 329)
)
if mibBuilder.loadTexts:
    extremeOnieStack.setStatus("current")
_X465_24xe_ObjectIdentity = ObjectIdentity
x465_24xe = _X465_24xe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 330)
)
if mibBuilder.loadTexts:
    x465_24xe.setStatus("current")
_X465_24s_ObjectIdentity = ObjectIdentity
x465_24s = _X465_24s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 331)
)
if mibBuilder.loadTexts:
    x465_24s.setStatus("current")
_ExtremeSLX9150_ObjectIdentity = ObjectIdentity
extremeSLX9150 = _ExtremeSLX9150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 332)
)
if mibBuilder.loadTexts:
    extremeSLX9150.setStatus("current")
_ExtremeSLX9150T_ObjectIdentity = ObjectIdentity
extremeSLX9150T = _ExtremeSLX9150T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 333)
)
if mibBuilder.loadTexts:
    extremeSLX9150T.setStatus("current")
_ExtremeSLX9250_ObjectIdentity = ObjectIdentity
extremeSLX9250 = _ExtremeSLX9250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 334)
)
if mibBuilder.loadTexts:
    extremeSLX9250.setStatus("current")
_ExtremeSLX9740x40_ObjectIdentity = ObjectIdentity
extremeSLX9740x40 = _ExtremeSLX9740x40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 335)
)
if mibBuilder.loadTexts:
    extremeSLX9740x40.setStatus("current")
_ExtremeSLX9740x80_ObjectIdentity = ObjectIdentity
extremeSLX9740x80 = _ExtremeSLX9740x80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 336)
)
if mibBuilder.loadTexts:
    extremeSLX9740x80.setStatus("current")
_Xa1440_ObjectIdentity = ObjectIdentity
xa1440 = _Xa1440_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 337)
)
if mibBuilder.loadTexts:
    xa1440.setStatus("current")
_Xa1480_ObjectIdentity = ObjectIdentity
xa1480 = _Xa1480_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 338)
)
if mibBuilder.loadTexts:
    xa1480.setStatus("current")
_ExtremeECAx6125_ObjectIdentity = ObjectIdentity
extremeECAx6125 = _ExtremeECAx6125_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 339)
)
if mibBuilder.loadTexts:
    extremeECAx6125.setStatus("current")
_X435_24p_4s_ObjectIdentity = ObjectIdentity
x435_24p_4s = _X435_24p_4s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 343)
)
if mibBuilder.loadTexts:
    x435_24p_4s.setStatus("current")
_X435_24t_4s_ObjectIdentity = ObjectIdentity
x435_24t_4s = _X435_24t_4s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 344)
)
if mibBuilder.loadTexts:
    x435_24t_4s.setStatus("current")
_X435_8p_4s_ObjectIdentity = ObjectIdentity
x435_8p_4s = _X435_8p_4s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 345)
)
if mibBuilder.loadTexts:
    x435_8p_4s.setStatus("current")
_X435_8t_4s_ObjectIdentity = ObjectIdentity
x435_8t_4s = _X435_8t_4s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 346)
)
if mibBuilder.loadTexts:
    x435_8t_4s.setStatus("current")
_X435_8p_2t_w_ObjectIdentity = ObjectIdentity
x435_8p_2t_w = _X435_8p_2t_w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 347)
)
if mibBuilder.loadTexts:
    x435_8p_2t_w.setStatus("current")
_X465i_48w_ObjectIdentity = ObjectIdentity
x465i_48w = _X465i_48w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 348)
)
if mibBuilder.loadTexts:
    x465i_48w.setStatus("current")
_ExtremeECAx6120H_ObjectIdentity = ObjectIdentity
extremeECAx6120H = _ExtremeECAx6120H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 2, 356)
)
if mibBuilder.loadTexts:
    extremeECAx6120H.setStatus("current")
_ExtremeMisc_ObjectIdentity = ObjectIdentity
extremeMisc = _ExtremeMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3)
)
_ExtremeOids_ObjectIdentity = ObjectIdentity
extremeOids = _ExtremeOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1)
)
_ExtremeMauType_ObjectIdentity = ObjectIdentity
extremeMauType = _ExtremeMauType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1)
)
_ExtremeMauType1000BaseSX_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseSX = _ExtremeMauType1000BaseSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 1)
)
_ExtremeMauType1000BaseLX_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseLX = _ExtremeMauType1000BaseLX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 2)
)
_ExtremeMauType1000BaseCX_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseCX = _ExtremeMauType1000BaseCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 3)
)
_ExtremeMauType1000BaseSXFD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseSXFD = _ExtremeMauType1000BaseSXFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 4)
)
_ExtremeMauType1000BaseLXFD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseLXFD = _ExtremeMauType1000BaseLXFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 5)
)
_ExtremeMauType1000BaseCXFD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseCXFD = _ExtremeMauType1000BaseCXFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 6)
)
_ExtremeMauType1000BaseWDMHD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseWDMHD = _ExtremeMauType1000BaseWDMHD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 7)
)
_ExtremeMauType1000BaseWDMFD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseWDMFD = _ExtremeMauType1000BaseWDMFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 8)
)
_ExtremeMauType1000BaseLX70HD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseLX70HD = _ExtremeMauType1000BaseLX70HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 9)
)
_ExtremeMauType1000BaseLX70FD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseLX70FD = _ExtremeMauType1000BaseLX70FD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 10)
)
_ExtremeMauType1000BaseZXHD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseZXHD = _ExtremeMauType1000BaseZXHD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 11)
)
_ExtremeMauType1000BaseZXFD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseZXFD = _ExtremeMauType1000BaseZXFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 12)
)
_ExtremeMauType1000BaseLX100HD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseLX100HD = _ExtremeMauType1000BaseLX100HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 13)
)
_ExtremeMauType1000BaseLX100FD_ObjectIdentity = ObjectIdentity
extremeMauType1000BaseLX100FD = _ExtremeMauType1000BaseLX100FD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 14)
)
_ExtremeMauType10GBaseCX4_ObjectIdentity = ObjectIdentity
extremeMauType10GBaseCX4 = _ExtremeMauType10GBaseCX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 15)
)
_ExtremeMauType10GBaseZR_ObjectIdentity = ObjectIdentity
extremeMauType10GBaseZR = _ExtremeMauType10GBaseZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 16)
)
_ExtremeMauType10GBaseDWDM_ObjectIdentity = ObjectIdentity
extremeMauType10GBaseDWDM = _ExtremeMauType10GBaseDWDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 17)
)
_ExtremeMauType10GBaseCX_ObjectIdentity = ObjectIdentity
extremeMauType10GBaseCX = _ExtremeMauType10GBaseCX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 18)
)
_ExtremeMauType10GBaseT_ObjectIdentity = ObjectIdentity
extremeMauType10GBaseT = _ExtremeMauType10GBaseT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 19)
)
_ExtremeMauType40GBaseX_ObjectIdentity = ObjectIdentity
extremeMauType40GBaseX = _ExtremeMauType40GBaseX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 20)
)
_ExtremeMauType100GBaseX_ObjectIdentity = ObjectIdentity
extremeMauType100GBaseX = _ExtremeMauType100GBaseX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 21)
)
_ExtremeMauType40GBasePSM4_ObjectIdentity = ObjectIdentity
extremeMauType40GBasePSM4 = _ExtremeMauType40GBasePSM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 22)
)
_ExtremeMauType100GBaseSR4_ObjectIdentity = ObjectIdentity
extremeMauType100GBaseSR4 = _ExtremeMauType100GBaseSR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 23)
)
_ExtremeMauType100GBaseCR4_ObjectIdentity = ObjectIdentity
extremeMauType100GBaseCR4 = _ExtremeMauType100GBaseCR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 24)
)
_ExtremeMauType100GBaseCWDM4_ObjectIdentity = ObjectIdentity
extremeMauType100GBaseCWDM4 = _ExtremeMauType100GBaseCWDM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 25)
)
_ExtremeMauType100GBasePSM4_ObjectIdentity = ObjectIdentity
extremeMauType100GBasePSM4 = _ExtremeMauType100GBasePSM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 32)
)
_ExtremeMauType100GBaseSWDM4_ObjectIdentity = ObjectIdentity
extremeMauType100GBaseSWDM4 = _ExtremeMauType100GBaseSWDM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 33)
)
_ExtremeMauType25GBaseSR_ObjectIdentity = ObjectIdentity
extremeMauType25GBaseSR = _ExtremeMauType25GBaseSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 34)
)
_ExtremeMauType25GBaseESR_ObjectIdentity = ObjectIdentity
extremeMauType25GBaseESR = _ExtremeMauType25GBaseESR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 35)
)
_ExtremeMauType25GBaseLR_ObjectIdentity = ObjectIdentity
extremeMauType25GBaseLR = _ExtremeMauType25GBaseLR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 36)
)
_ExtremeMauType25GBaseCR4_ObjectIdentity = ObjectIdentity
extremeMauType25GBaseCR4 = _ExtremeMauType25GBaseCR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 37)
)
_ExtremeMauType100GBaseCWDM4Lite_ObjectIdentity = ObjectIdentity
extremeMauType100GBaseCWDM4Lite = _ExtremeMauType100GBaseCWDM4Lite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 38)
)
_ExtremeMauType100GBaseBIDI_ObjectIdentity = ObjectIdentity
extremeMauType100GBaseBIDI = _ExtremeMauType100GBaseBIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 39)
)
_ExtremeMauType10GBaseBX10U_ObjectIdentity = ObjectIdentity
extremeMauType10GBaseBX10U = _ExtremeMauType10GBaseBX10U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 40)
)
_ExtremeMauType10GBaseBX10D_ObjectIdentity = ObjectIdentity
extremeMauType10GBaseBX10D = _ExtremeMauType10GBaseBX10D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 41)
)
_ExtremeMauType10GBaseBX40U_ObjectIdentity = ObjectIdentity
extremeMauType10GBaseBX40U = _ExtremeMauType10GBaseBX40U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 42)
)
_ExtremeMauType10GBaseBX40D_ObjectIdentity = ObjectIdentity
extremeMauType10GBaseBX40D = _ExtremeMauType10GBaseBX40D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 43)
)
_ExtremeV2Traps_ObjectIdentity = ObjectIdentity
extremeV2Traps = _ExtremeV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-BASE-MIB",
    **{"PortList": PortList,
       "L4Port": L4Port,
       "ExtremeGenAddr": ExtremeGenAddr,
       "ExtremeDeviceId": ExtremeDeviceId,
       "WPACipherSet": WPACipherSet,
       "WPAKeyMgmtSet": WPAKeyMgmtSet,
       "ClientAuthType": ClientAuthType,
       "WirelessRemoteConnectBindingType": WirelessRemoteConnectBindingType,
       "extremenetworks": extremenetworks,
       "extremeV1Traps": extremeV1Traps,
       "extremeAgent": extremeAgent,
       "extremeSystem": extremeSystem,
       "extremeVlan": extremeVlan,
       "extremeQos": extremeQos,
       "extremePort": extremePort,
       "extremeVC": extremeVC,
       "extremeTrapPoll": extremeTrapPoll,
       "extremeQosPolicy": extremeQosPolicy,
       "extremeDlcs": extremeDlcs,
       "extremeFileTransfer": extremeFileTransfer,
       "extremeRtStats": extremeRtStats,
       "extremeEsrp": extremeEsrp,
       "extremeEdp": extremeEdp,
       "extremeSlb": extremeSlb,
       "extremeOspf": extremeOspf,
       "extremeFdb": extremeFdb,
       "extremeStp": extremeStp,
       "extremeEaps": extremeEaps,
       "extremeLacp": extremeLacp,
       "extremePOSMib": extremePOSMib,
       "extremeNPMib": extremeNPMib,
       "extremeNetFlow": extremeNetFlow,
       "extremeSnmpv3": extremeSnmpv3,
       "extremeCable": extremeCable,
       "extremeWireless": extremeWireless,
       "extremeAP": extremeAP,
       "extremeLAC": extremeLAC,
       "extremeServices": extremeServices,
       "extremePoE": extremePoE,
       "extremeDosMib": extremeDosMib,
       "extremeEnhDosMib": extremeEnhDosMib,
       "extremeClearflow": extremeClearflow,
       "extremeEntity": extremeEntity,
       "extremeSwMonitor": extremeSwMonitor,
       "extremeStackable": extremeStackable,
       "extremeIpSecurity": extremeIpSecurity,
       "extremeUpm": extremeUpm,
       "extremeIdMgr": extremeIdMgr,
       "extremeMplsMIB": extremeMplsMIB,
       "extremeHclag": extremeHclag,
       "extremeVM": extremeVM,
       "extremeAutoProvision": extremeAutoProvision,
       "extremeMlag": extremeMlag,
       "extremeCfgMgmt": extremeCfgMgmt,
       "extremeBfd": extremeBfd,
       "extremeMacAuthMIB": extremeMacAuthMIB,
       "extremePbbMib": extremePbbMib,
       "extremeErps": extremeErps,
       "extremeCfm": extremeCfm,
       "extremeAcl": extremeAcl,
       "extremeVrrpMIB": extremeVrrpMIB,
       "extremeOspfv3MIB": extremeOspfv3MIB,
       "extremeBgp4V2": extremeBgp4V2,
       "extremeBgp4V2TC": extremeBgp4V2TC,
       "extremeInternal": extremeInternal,
       "extremeProduct": extremeProduct,
       "summit1": summit1,
       "summit2": summit2,
       "summit3": summit3,
       "summit4": summit4,
       "summit4fx": summit4fx,
       "summit48": summit48,
       "summit24": summit24,
       "blackDiamond6800": blackDiamond6800,
       "blackDiamond6808": blackDiamond6808,
       "summit7iSX": summit7iSX,
       "summit7iTX": summit7iTX,
       "summit1iTX": summit1iTX,
       "summit5i": summit5i,
       "summit48i": summit48i,
       "alpine3808": alpine3808,
       "summit1iSX": summit1iSX,
       "alpine3804": alpine3804,
       "summit5iLX": summit5iLX,
       "summit5iTX": summit5iTX,
       "enetSwitch24Port": enetSwitch24Port,
       "blackDiamond6816": blackDiamond6816,
       "summit24e3": summit24e3,
       "alpine3802": alpine3802,
       "blackDiamond6804": blackDiamond6804,
       "summit48si": summit48si,
       "summitPx1": summitPx1,
       "summit24e2TX": summit24e2TX,
       "summit24e2SX": summit24e2SX,
       "summit200-24": summit200_24,
       "summit200-48": summit200_48,
       "summit300-48": summit300_48,
       "bd10808": bd10808,
       "summit400-48t": summit400_48t,
       "summit300-24": summit300_24,
       "bd8810": bd8810,
       "summit400-24t": summit400_24t,
       "summit400-24p": summit400_24p,
       "summitX450-24x": summitX450_24x,
       "summitX450-24t": summitX450_24t,
       "summitStack": summitStack,
       "summitWM100": summitWM100,
       "summitWM1000": summitWM1000,
       "summit200-24fx": summit200_24fx,
       "summitX450a-24t": summitX450a_24t,
       "summitX450e-24p": summitX450e_24p,
       "bd8806": bd8806,
       "altitude350": altitude350,
       "summitX450a-48t": summitX450a_48t,
       "bd12804": bd12804,
       "summitX450e-48p": summitX450e_48p,
       "summitX450a-24tDC": summitX450a_24tDC,
       "summitX450a-24xDC": summitX450a_24xDC,
       "sentriantCE150": sentriantCE150,
       "summitX450a-24x": summitX450a_24x,
       "bd12802": bd12802,
       "altitude300": altitude300,
       "summitX450a-48tDC": summitX450a_48tDC,
       "summitX250-24t": summitX250_24t,
       "summitX250-24p": summitX250_24p,
       "summitX250-24x": summitX250_24x,
       "summitX250-48t": summitX250_48t,
       "summitX250-48p": summitX250_48p,
       "summitVer2Stack": summitVer2Stack,
       "summitWM200": summitWM200,
       "summitWM2000": summitWM2000,
       "summitWM100Lite": summitWM100Lite,
       "summitX250-24tDC": summitX250_24tDC,
       "summitX250-24xDC": summitX250_24xDC,
       "summitX250-48tDC": summitX250_48tDC,
       "summitX150-24t": summitX150_24t,
       "summitX150-24tDC": summitX150_24tDC,
       "summitX150-24p": summitX150_24p,
       "summitX150-24x": summitX150_24x,
       "summitX150-24xDC": summitX150_24xDC,
       "summitX150-48t": summitX150_48t,
       "summitX150-48tDC": summitX150_48tDC,
       "summitX150-48p": summitX150_48p,
       "sentriantAGSW": sentriantAGSW,
       "sentriantAG200": sentriantAG200,
       "summitWM20": summitWM20,
       "summitX350-24t": summitX350_24t,
       "summitX350-48t": summitX350_48t,
       "summitX650-24t": summitX650_24t,
       "summitX650-24x": summitX650_24x,
       "sentriantNG300": sentriantNG300,
       "altitude360": altitude360,
       "altitude450": altitude450,
       "summitX650-24x-SSns": summitX650_24x_SSns,
       "summitX650-24t-SSns": summitX650_24t_SSns,
       "summitX650-24x-SS": summitX650_24x_SS,
       "summitX650-24t-SS": summitX650_24t_SS,
       "summitX650-24x-10G8X": summitX650_24x_10G8X,
       "summitX650-24t-10G8X": summitX650_24t_10G8X,
       "summitX650-24x-SS256": summitX650_24x_SS256,
       "summitX650-24t-SS256": summitX650_24t_SS256,
       "summitX650-24x-SS512": summitX650_24x_SS512,
       "summitX650-24t-SS512": summitX650_24t_SS512,
       "bd20808": bd20808,
       "nwi-e450a": nwi_e450a,
       "sentriantPS200v1": sentriantPS200v1,
       "wirelessProducts": wirelessProducts,
       "summitWM3700": summitWM3700,
       "summitWM3600": summitWM3600,
       "summitWM3400": summitWM3400,
       "bd20804": bd20804,
       "summitX480-48t": summitX480_48t,
       "summitX480-48t-SS": summitX480_48t_SS,
       "summitX480-48t-10G4X": summitX480_48t_10G4X,
       "summitX480-48t-SS128": summitX480_48t_SS128,
       "summitX480-24x": summitX480_24x,
       "summitX480-24x-SS": summitX480_24x_SS,
       "summitX480-24x-10G4X": summitX480_24x_10G4X,
       "summitX480-24x-SS128": summitX480_24x_SS128,
       "summitX480-48x": summitX480_48x,
       "summitX480-48x-SS": summitX480_48x_SS,
       "summitX480-48x-10G4X": summitX480_48x_10G4X,
       "summitX480-48x-SS128": summitX480_48x_SS128,
       "altitude3510": altitude3510,
       "altitude3550": altitude3550,
       "altitude4610": altitude4610,
       "altitude4620": altitude4620,
       "summitX450e-24t": summitX450e_24t,
       "summitX450e-48t": summitX450e_48t,
       "summitX460-24t": summitX460_24t,
       "summitX460-24p": summitX460_24p,
       "summitX460-24x": summitX460_24x,
       "summitX460-48t": summitX460_48t,
       "summitX460-48p": summitX460_48p,
       "summitX460-48x": summitX460_48x,
       "altitude4700": altitude4700,
       "summitX480-24x-SSV80": summitX480_24x_SSV80,
       "summitX480-48x-SSV80": summitX480_48x_SSV80,
       "summitX480-48t-SSV80": summitX480_48t_SSV80,
       "summitX650-24x-40G4X": summitX650_24x_40G4X,
       "summitX650-24t-40G4X": summitX650_24t_40G4X,
       "summitX480-24x-40G4X": summitX480_24x_40G4X,
       "summitX480-48x-40G4X": summitX480_48x_40G4X,
       "summitX480-48t-40G4X": summitX480_48t_40G4X,
       "summitX670-48x": summitX670_48x,
       "summitX670v-48x": summitX670v_48x,
       "e4g-400": e4g_400,
       "bdx8": bdx8,
       "e4g-200": e4g_200,
       "summitX440-8t": summitX440_8t,
       "summitX440-8p": summitX440_8p,
       "summitX440-24t": summitX440_24t,
       "summitX440-24p": summitX440_24p,
       "summitX440-48t": summitX440_48t,
       "summitX440-48p": summitX440_48p,
       "summitX440-24t-10G": summitX440_24t_10G,
       "summitX440-24p-10G": summitX440_24p_10G,
       "summitX440-48t-10G": summitX440_48t_10G,
       "summitX440-48p-10G": summitX440_48p_10G,
       "ags100-24t": ags100_24t,
       "ags150-24p": ags150_24p,
       "summitX670v-48t": summitX670v_48t,
       "summitX440-L2-24t": summitX440_L2_24t,
       "summitX440-L2-48t": summitX440_L2_48t,
       "e4g-200-12x": e4g_200_12x,
       "summitX440-24x": summitX440_24x,
       "summitX440-24x-10g": summitX440_24x_10g,
       "summitX430-24t": summitX430_24t,
       "summitX430-48t": summitX430_48t,
       "summitX440-24tdc": summitX440_24tdc,
       "summitX440-48tdc": summitX440_48tdc,
       "summitX770-32q": summitX770_32q,
       "summitX670G2-48x-4q": summitX670G2_48x_4q,
       "summitX670G2-72x": summitX670G2_72x,
       "summitX460G2-24t-10G4": summitX460G2_24t_10G4,
       "summitX460G2-24p-10G4": summitX460G2_24p_10G4,
       "summitX460G2-24x-10G4": summitX460G2_24x_10G4,
       "summitX460G2-48t-10G4": summitX460G2_48t_10G4,
       "summitX460G2-48p-10G4": summitX460G2_48p_10G4,
       "summitX460G2-48x-10G4": summitX460G2_48x_10G4,
       "summitX430-8p": summitX430_8p,
       "summitX430-24p": summitX430_24p,
       "aviatCtr-8440": aviatCtr_8440,
       "summitX450G2-24t-10G4": summitX450G2_24t_10G4,
       "summitX450G2-24p-10G4": summitX450G2_24p_10G4,
       "summitX450G2-48t-10G4": summitX450G2_48t_10G4,
       "summitX450G2-48p-10G4": summitX450G2_48p_10G4,
       "summitX450G2-24t-G4": summitX450G2_24t_G4,
       "summitX450G2-24p-G4": summitX450G2_24p_G4,
       "summitX450G2-48t-G4": summitX450G2_48t_G4,
       "summitX450G2-48p-G4": summitX450G2_48p_G4,
       "summitX460G2-24t-G4": summitX460G2_24t_G4,
       "summitX460G2-24p-G4": summitX460G2_24p_G4,
       "summitX460G2-48t-G4": summitX460G2_48t_G4,
       "summitX460G2-48p-G4": summitX460G2_48p_G4,
       "oneC-A-600": oneC_A_600,
       "oneC-V": oneC_V,
       "summitX440G2-48p-10G4": summitX440G2_48p_10G4,
       "summitX440G2-48t-10G4": summitX440G2_48t_10G4,
       "summitX440G2-48t-10G4-DC": summitX440G2_48t_10G4_DC,
       "summitX440G2-24p-10G4": summitX440G2_24p_10G4,
       "summitX440G2-24t-10G4": summitX440G2_24t_10G4,
       "summitX440G2-24t-10G4-DC": summitX440G2_24t_10G4_DC,
       "summitX440G2-24x-10G4": summitX440G2_24x_10G4,
       "summitX440G2-12p-10G4": summitX440G2_12p_10G4,
       "summitX440G2-12t-10G4": summitX440G2_12t_10G4,
       "summitX440G2-12t8fx-G4": summitX440G2_12t8fx_G4,
       "summitX440G2-24t-G4": summitX440G2_24t_G4,
       "summitX440G2-24fx-G4": summitX440G2_24fx_G4,
       "summitX620-16T": summitX620_16T,
       "summitX620-16P": summitX620_16P,
       "summitX620-16X": summitX620_16X,
       "summitX620-8T-2X": summitX620_8T_2X,
       "summitX620-10X": summitX620_10X,
       "summitX870-32C": summitX870_32C,
       "summitX870-96X-8C": summitX870_96X_8C,
       "ecos": ecos,
       "isw-4P-2-G2": isw_4P_2_G2,
       "isw-8P-G4": isw_8P_G4,
       "isw-4GP-2G-G2": isw_4GP_2G_G2,
       "isw-8GP-G4": isw_8GP_G4,
       "x690-48t-4q-2c": x690_48t_4q_2c,
       "x690-48x-4q-2c": x690_48x_4q_2c,
       "extremeSNSxNSSxA": extremeSNSxNSSxA,
       "extremeNSxAx20": extremeNSxAx20,
       "extremeNACxAx20": extremeNACxAx20,
       "extremeIAxV": extremeIAxV,
       "extremeIAxAx20": extremeIAxAx20,
       "extremeIAxAx300": extremeIAxAx300,
       "extremePVxV": extremePVxV,
       "extremePVxAx300": extremePVxAx300,
       "summitX460-G2-16mp-32p-10GE4": summitX460_G2_16mp_32p_10GE4,
       "summitX460G2-24p-24hp": summitX460G2_24p_24hp,
       "summitX460G2-24t-24ht": summitX460G2_24t_24ht,
       "extreme210-12t-GE2": extreme210_12t_GE2,
       "extreme210-12p-GE2": extreme210_12p_GE2,
       "extreme210-24t-GE2": extreme210_24t_GE2,
       "extreme210-24p-GE2": extreme210_24p_GE2,
       "extreme210-48t-GE4": extreme210_48t_GE4,
       "extreme210-48p-GE4": extreme210_48p_GE4,
       "extreme220-12t-10GE2": extreme220_12t_10GE2,
       "extreme220-12p-10GE2": extreme220_12p_10GE2,
       "extreme220-24t-10GE2": extreme220_24t_10GE2,
       "extreme220-24p-10GE2": extreme220_24p_10GE2,
       "extreme220-48t-10GE4": extreme220_48t_10GE4,
       "extreme220-48p-10GE4": extreme220_48p_10GE4,
       "extreme240-8mt-16t-10GE4": extreme240_8mt_16t_10GE4,
       "extreme240-8mp-16p-10GE4": extreme240_8mp_16p_10GE4,
       "extreme240-32t-16mt-10GE6": extreme240_32t_16mt_10GE6,
       "extreme240-32p-16mp-10GE6": extreme240_32p_16mp_10GE6,
       "extreme825-48v-6c": extreme825_48v_6c,
       "extremeNMSxAx25": extremeNMSxAx25,
       "extremeNMSxAx305": extremeNMSxAx305,
       "extremeIAxAx25": extremeIAxAx25,
       "extremeIAxAx305": extremeIAxAx305,
       "extremePVxAx305": extremePVxAx305,
       "extremeEMPx35": extremeEMPx35,
       "extremeEMPx5310": extremeEMPx5310,
       "extremeEMPxV": extremeEMPxV,
       "xtremeWhitebox": xtremeWhitebox,
       "vm386EXOS": vm386EXOS,
       "extremeNMSxV": extremeNMSxV,
       "extremeSSxIxA": extremeSSxIxA,
       "extremeESEx2000": extremeESEx2000,
       "extremeFabricManager": extremeFabricManager,
       "x590-24t-1q-2c": x590_24t_1q_2c,
       "x590-24x-1q-1c": x590_24x_1q_1c,
       "slxOsAcctonAS771232X": slxOsAcctonAS771232X,
       "slxOsDniAG9032v1": slxOsDniAG9032v1,
       "es6108x32c": es6108x32c,
       "es6108x48vx8c": es6108x48vx8c,
       "vsp7432CQ": vsp7432CQ,
       "vsp7456VSC": vsp7456VSC,
       "extremeSLX9030": extremeSLX9030,
       "extremeSLX9030T": extremeSLX9030T,
       "extremeSLX9640": extremeSLX9640,
       "vsp1100": vsp1100,
       "extremeCspAwsSubnetType": extremeCspAwsSubnetType,
       "extremeCspGcpSubnetType": extremeCspGcpSubnetType,
       "extremeCspAzureSubnetType": extremeCspAzureSubnetType,
       "extremeMcsVmwareHypervisorType": extremeMcsVmwareHypervisorType,
       "x465-48t": x465_48t,
       "x465-48p": x465_48p,
       "x465-48w": x465_48w,
       "x465-24mu": x465_24mu,
       "x465-24mu-24w": x465_24mu_24w,
       "x465-24w": x465_24w,
       "x725-48y-8c": x725_48y_8c,
       "extremeSnVirtualSensor100": extremeSnVirtualSensor100,
       "extremeSnVirtualSensor250": extremeSnVirtualSensor250,
       "vsp7400-48Y-8C": vsp7400_48Y_8C,
       "extremeVirtualTAP": extremeVirtualTAP,
       "extremeVirtualPB": extremeVirtualPB,
       "x695-48y-8c": x695_48y_8c,
       "extremeOnieStack": extremeOnieStack,
       "x465-24xe": x465_24xe,
       "x465-24s": x465_24s,
       "extremeSLX9150": extremeSLX9150,
       "extremeSLX9150T": extremeSLX9150T,
       "extremeSLX9250": extremeSLX9250,
       "extremeSLX9740x40": extremeSLX9740x40,
       "extremeSLX9740x80": extremeSLX9740x80,
       "xa1440": xa1440,
       "xa1480": xa1480,
       "extremeECAx6125": extremeECAx6125,
       "x435-24p-4s": x435_24p_4s,
       "x435-24t-4s": x435_24t_4s,
       "x435-8p-4s": x435_8p_4s,
       "x435-8t-4s": x435_8t_4s,
       "x435-8p-2t-w": x435_8p_2t_w,
       "x465i-48w": x465i_48w,
       "extremeECAx6120H": extremeECAx6120H,
       "extremeMisc": extremeMisc,
       "extremeOids": extremeOids,
       "extremeMauType": extremeMauType,
       "extremeMauType1000BaseSX": extremeMauType1000BaseSX,
       "extremeMauType1000BaseLX": extremeMauType1000BaseLX,
       "extremeMauType1000BaseCX": extremeMauType1000BaseCX,
       "extremeMauType1000BaseSXFD": extremeMauType1000BaseSXFD,
       "extremeMauType1000BaseLXFD": extremeMauType1000BaseLXFD,
       "extremeMauType1000BaseCXFD": extremeMauType1000BaseCXFD,
       "extremeMauType1000BaseWDMHD": extremeMauType1000BaseWDMHD,
       "extremeMauType1000BaseWDMFD": extremeMauType1000BaseWDMFD,
       "extremeMauType1000BaseLX70HD": extremeMauType1000BaseLX70HD,
       "extremeMauType1000BaseLX70FD": extremeMauType1000BaseLX70FD,
       "extremeMauType1000BaseZXHD": extremeMauType1000BaseZXHD,
       "extremeMauType1000BaseZXFD": extremeMauType1000BaseZXFD,
       "extremeMauType1000BaseLX100HD": extremeMauType1000BaseLX100HD,
       "extremeMauType1000BaseLX100FD": extremeMauType1000BaseLX100FD,
       "extremeMauType10GBaseCX4": extremeMauType10GBaseCX4,
       "extremeMauType10GBaseZR": extremeMauType10GBaseZR,
       "extremeMauType10GBaseDWDM": extremeMauType10GBaseDWDM,
       "extremeMauType10GBaseCX": extremeMauType10GBaseCX,
       "extremeMauType10GBaseT": extremeMauType10GBaseT,
       "extremeMauType40GBaseX": extremeMauType40GBaseX,
       "extremeMauType100GBaseX": extremeMauType100GBaseX,
       "extremeMauType40GBasePSM4": extremeMauType40GBasePSM4,
       "extremeMauType100GBaseSR4": extremeMauType100GBaseSR4,
       "extremeMauType100GBaseCR4": extremeMauType100GBaseCR4,
       "extremeMauType100GBaseCWDM4": extremeMauType100GBaseCWDM4,
       "extremeMauType100GBasePSM4": extremeMauType100GBasePSM4,
       "extremeMauType100GBaseSWDM4": extremeMauType100GBaseSWDM4,
       "extremeMauType25GBaseSR": extremeMauType25GBaseSR,
       "extremeMauType25GBaseESR": extremeMauType25GBaseESR,
       "extremeMauType25GBaseLR": extremeMauType25GBaseLR,
       "extremeMauType25GBaseCR4": extremeMauType25GBaseCR4,
       "extremeMauType100GBaseCWDM4Lite": extremeMauType100GBaseCWDM4Lite,
       "extremeMauType100GBaseBIDI": extremeMauType100GBaseBIDI,
       "extremeMauType10GBaseBX10U": extremeMauType10GBaseBX10U,
       "extremeMauType10GBaseBX10D": extremeMauType10GBaseBX10D,
       "extremeMauType10GBaseBX40U": extremeMauType10GBaseBX40U,
       "extremeMauType10GBaseBX40D": extremeMauType10GBaseBX40D,
       "extremeV2Traps": extremeV2Traps}
)
