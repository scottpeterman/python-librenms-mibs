# SNMP MIB module (FORTINET-FORTIGATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\FORTINET-FORTIGATE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:51 2025
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

(FnBoolState,
 FnIndex,
 fnAdminEntry,
 fnGenTrapMsg,
 fnSysSerial,
 fortinet) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "FnBoolState",
    "FnIndex",
    "fnAdminEntry",
    "fnGenTrapMsg",
    "fnSysSerial",
    "fortinet")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ifEntry,
 ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
    "ifIndex",
    "ifName")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

(AutonomousType,
 DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

fnFortiGateMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101)
)
if mibBuilder.loadTexts:
    fnFortiGateMib.setRevisions(
        ("2025-04-04 00:00",
         "2024-12-17 00:00",
         "2024-09-20 00:00",
         "2024-09-19 00:00",
         "2024-07-16 00:00",
         "2024-05-14 00:00",
         "2024-03-08 00:00",
         "2023-09-21 00:00",
         "2023-09-13 00:00",
         "2023-09-05 00:00",
         "2023-08-30 00:00",
         "2023-07-21 00:00",
         "2023-03-16 00:00",
         "2023-03-14 00:00",
         "2022-12-19 00:00",
         "2022-10-22 00:00",
         "2022-10-07 00:00",
         "2022-09-23 00:00",
         "2022-06-30 00:00",
         "2022-06-01 00:00",
         "2022-03-11 00:00",
         "2022-02-16 00:00",
         "2022-01-26 00:00",
         "2021-04-28 00:00",
         "2021-03-09 00:01",
         "2021-03-09 00:00",
         "2021-03-05 00:00",
         "2021-02-25 00:00",
         "2021-01-26 00:00",
         "2021-01-06 00:00",
         "2020-12-07 00:00",
         "2020-10-08 00:00",
         "2020-10-02 00:00",
         "2020-09-30 00:00",
         "2020-09-21 00:00",
         "2020-08-14 00:00",
         "2020-06-25 00:00",
         "2020-05-08 00:00",
         "2020-04-30 00:00",
         "2019-10-28 00:00",
         "2019-08-16 00:00",
         "2019-08-07 00:00",
         "2019-05-31 00:00",
         "2019-05-27 00:00",
         "2019-01-24 00:00",
         "2018-12-12 00:00",
         "2018-06-11 00:00",
         "2018-06-06 00:00",
         "2018-04-06 00:00",
         "2018-01-18 00:00",
         "2018-01-10 00:00",
         "2017-11-16 00:00",
         "2017-10-18 00:00",
         "2017-10-03 00:00",
         "2017-09-07 00:00",
         "2017-08-30 00:00",
         "2017-08-25 00:00",
         "2017-07-21 00:00",
         "2017-07-12 00:00",
         "2017-04-28 00:00",
         "2017-04-05 00:00",
         "2017-01-16 00:00",
         "2016-09-15 00:00",
         "2016-06-17 00:00",
         "2015-04-23 00:00",
         "2015-03-16 00:00",
         "2015-01-10 00:00",
         "2014-12-04 00:00",
         "2014-06-04 00:00",
         "2014-02-13 00:00",
         "2013-08-12 00:00",
         "2013-07-26 00:00",
         "2013-04-12 00:00",
         "2013-04-06 00:00",
         "2012-11-29 00:00",
         "2012-07-10 00:00",
         "2012-05-16 00:00",
         "2012-02-06 00:00",
         "2011-09-12 00:00",
         "2011-01-10 00:00",
         "2009-11-03 00:00",
         "2009-10-01 00:00",
         "2009-07-07 00:00",
         "2008-11-03 00:00",
         "2008-09-02 00:00",
         "2008-08-19 00:00",
         "2008-06-16 00:00",
         "2008-04-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FgVdIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class FgOpMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nat", 1),
          ("transparent", 2))
    )



class FgHaMode(TextualConvention, Integer32):
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
        *(("standalone", 1),
          ("activeActive", 2),
          ("activePassive", 3))
    )



class FgHaState(TextualConvention, Integer32):
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
        *(("primary", 1),
          ("secondary", 2),
          ("standalone", 3))
    )



class FgSgWorkerBladeIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class FgSgWorkerBladeState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("dead", 2),
          ("standby", 3),
          ("active", 4))
    )



class FgHaLBSchedule(TextualConvention, Integer32):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("hub", 2),
          ("leastConnections", 3),
          ("roundRobin", 4),
          ("weightedRoundRobin", 5),
          ("random", 6),
          ("ipBased", 7),
          ("ipPortBased", 8))
    )



class FgAdminPermLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              15,
              255)
        )
    )
    namedValues = NamedValues(
        *(("readAdmin", 0),
          ("writeAdmin", 1),
          ("domainAdmin", 15),
          ("superAdmin", 255))
    )



class FgFwUserAuthType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radiusSingle", 2),
          ("radiusMultiple", 3),
          ("ldap", 4))
    )



class FgFwAuthUserType(TextualConvention, Integer32):
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("fsso", 0),
          ("rsso", 1),
          ("ntlm", 2),
          ("fw", 3),
          ("wsso", 4),
          ("fsspCitrix", 5),
          ("ssoGuest", 6),
          ("disclaimer", 7),
          ("other", 8),
          ("unauth", 9),
          ("email", 10))
    )



class FgSessProto(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8,
              12,
              17,
              22,
              41,
              46,
              47,
              50,
              51,
              89,
              103,
              108,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ip", 0),
          ("icmp", 1),
          ("igmp", 2),
          ("ipip", 4),
          ("tcp", 6),
          ("egp", 8),
          ("pup", 12),
          ("udp", 17),
          ("idp", 22),
          ("ipv6", 41),
          ("rsvp", 46),
          ("gre", 47),
          ("esp", 50),
          ("ah", 51),
          ("ospf", 89),
          ("pim", 103),
          ("comp", 108),
          ("raw", 255))
    )



class FgP2PProto(TextualConvention, Integer32):
    status = "current"
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
        *(("bitTorrent", 0),
          ("eDonkey", 1),
          ("gnutella", 2),
          ("kaZaa", 3),
          ("skype", 4),
          ("winNY", 5))
    )



class FgScanAvDisposition(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("blocked", 2))
    )



class FgWanOptProtocols(TextualConvention, Integer32):
    status = "current"
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
        *(("http", 1),
          ("mapi", 2),
          ("cifs", 3),
          ("ftp", 4),
          ("tcp", 5))
    )



class FgWanOptHistPeriods(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("last10Min", 1),
          ("lastHour", 2),
          ("lastDay", 3),
          ("lastMonth", 4))
    )



class FgHaStatsSyncStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unsynchronized", 0),
          ("synchronized", 1))
    )



class FgWcWlanSecurityType(TextualConvention, Integer32):
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("open", 1),
          ("captivePortal", 2),
          ("wep64", 3),
          ("wep128", 4),
          ("wpaOnlyPersonal", 5),
          ("wpaOnlyEnterprise", 6),
          ("wpa2OnlyPersonal", 7),
          ("wpa2OnlyEnterprise", 8),
          ("wpaPersonal", 9),
          ("wpaEnterprise", 10),
          ("wpaOnlyPersonalCaptivePortal", 11),
          ("wpa2OnlyPersonalCaptivePortal", 12),
          ("wpaPersonalCaptivePortal", 13),
          ("wpa3Sae", 14),
          ("wpa3SaeTransition", 15),
          ("wpa3Enterprise", 16),
          ("wpa3Owe", 17),
          ("osen", 18))
    )



class FgWcWlanAuthenticationType(TextualConvention, Integer32):
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
        *(("other", 0),
          ("psk", 1),
          ("radiusServer", 2),
          ("userGroup", 3))
    )



class FgWcWlanEncryptionType(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 0),
          ("none", 1),
          ("tkip", 2),
          ("aes", 3),
          ("tkipAes", 4))
    )



class FgWcWtpRadioId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )



class FgWcWtpRadioType(TextualConvention, Integer32):
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 3),
          ("dot11n5g", 4),
          ("dot11n2g", 5),
          ("dot11ac", 6),
          ("dot11ngOnly", 7),
          ("dot11gOnly", 8),
          ("dot11n2GHzOnly", 9),
          ("dot11n5GHzOnly", 10),
          ("dot11acnOnly", 11),
          ("dot11acOnly", 12),
          ("dot11ax2g", 13),
          ("dot11ax5g", 14),
          ("dot11ax6g", 15),
          ("dot11axng2gOnly", 16),
          ("dot11axn2gOnly", 17),
          ("dot11ax2gOnly", 18),
          ("dot11axacn5gOnly", 19),
          ("dot11axac5gOnly", 20),
          ("dot11ax5gOnly", 21))
    )



class FgWcWtpChannelWidthType(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 0),
          ("width20MHz", 1),
          ("width40MHz", 2),
          ("width80MHz", 3),
          ("width160MHz", 4))
    )



class FgWcWtpRadioBandType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("band2GHz", 1),
          ("band5GHz", 2))
    )



class FgWcWtpRadioChannelNumber(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class FgWcWtpRadioMode(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 0),
          ("notExist", 1),
          ("disabled", 2),
          ("ap", 3),
          ("monitor", 4),
          ("sniffer", 5))
    )



class FgWcCountryString(TextualConvention, OctetString):
    status = "current"
    displayHint = "3a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



class FgNPUIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class FgLogDeviceIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_FgModel_ObjectIdentity = ObjectIdentity
fgModel = _FgModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1)
)
_FgtVM64_ObjectIdentity = ObjectIdentity
fgtVM64 = _FgtVM64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 30)
)
_FgtVM64XEN_ObjectIdentity = ObjectIdentity
fgtVM64XEN = _FgtVM64XEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 40)
)
_FgtVM64AWS_ObjectIdentity = ObjectIdentity
fgtVM64AWS = _FgtVM64AWS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 45)
)
_FgtVM64FGCAWS_ObjectIdentity = ObjectIdentity
fgtVM64FGCAWS = _FgtVM64FGCAWS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 46)
)
_FgtVM64OPC_ObjectIdentity = ObjectIdentity
fgtVM64OPC = _FgtVM64OPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 47)
)
_FgtVM64KVm_ObjectIdentity = ObjectIdentity
fgtVM64KVm = _FgtVM64KVm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 60)
)
_FgtVM64FGCKVM_ObjectIdentity = ObjectIdentity
fgtVM64FGCKVM = _FgtVM64FGCKVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 61)
)
_FgtVM64GCP_ObjectIdentity = ObjectIdentity
fgtVM64GCP = _FgtVM64GCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 65)
)
_FgtARM64KVM_ObjectIdentity = ObjectIdentity
fgtARM64KVM = _FgtARM64KVM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 66)
)
_FgtVM64HV_ObjectIdentity = ObjectIdentity
fgtVM64HV = _FgtVM64HV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 70)
)
_Fgt40F_ObjectIdentity = ObjectIdentity
fgt40F = _Fgt40F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 441)
)
_Fgt41F_ObjectIdentity = ObjectIdentity
fgt41F = _Fgt41F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 442)
)
_Fg40FI_ObjectIdentity = ObjectIdentity
fg40FI = _Fg40FI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 443)
)
_Fg41FI_ObjectIdentity = ObjectIdentity
fg41FI = _Fg41FI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 444)
)
_Fwf40F_ObjectIdentity = ObjectIdentity
fwf40F = _Fwf40F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 445)
)
_Fwf41F_ObjectIdentity = ObjectIdentity
fwf41F = _Fwf41F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 446)
)
_Fw40FI_ObjectIdentity = ObjectIdentity
fw40FI = _Fw40FI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 447)
)
_Fw41FI_ObjectIdentity = ObjectIdentity
fw41FI = _Fw41FI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 448)
)
_Fgt50G_ObjectIdentity = ObjectIdentity
fgt50G = _Fgt50G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 450)
)
_Fg50G5_ObjectIdentity = ObjectIdentity
fg50G5 = _Fg50G5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 451)
)
_Fg50GD_ObjectIdentity = ObjectIdentity
fg50GD = _Fg50GD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 452)
)
_Fg51G5_ObjectIdentity = ObjectIdentity
fg51G5 = _Fg51G5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 453)
)
_Fw50G5_ObjectIdentity = ObjectIdentity
fw50G5 = _Fw50G5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 454)
)
_Fwf50G_ObjectIdentity = ObjectIdentity
fwf50G = _Fwf50G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 455)
)
_Fwf51G_ObjectIdentity = ObjectIdentity
fwf51G = _Fwf51G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 456)
)
_Fwf50GD_ObjectIdentity = ObjectIdentity
fwf50GD = _Fwf50GD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 457)
)
_Fw51G5_ObjectIdentity = ObjectIdentity
fw51G5 = _Fw51G5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 458)
)
_Fgt51G_ObjectIdentity = ObjectIdentity
fgt51G = _Fgt51G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 459)
)
_Fg50GP_ObjectIdentity = ObjectIdentity
fg50GP = _Fg50GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 460)
)
_Fgt51GP_ObjectIdentity = ObjectIdentity
fgt51GP = _Fgt51GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 461)
)
_Fw50GS_ObjectIdentity = ObjectIdentity
fw50GS = _Fw50GS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 462)
)
_Fg50GS_ObjectIdentity = ObjectIdentity
fg50GS = _Fg50GS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 463)
)
_Fwf60E_ObjectIdentity = ObjectIdentity
fwf60E = _Fwf60E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 639)
)
_Fgt61E_ObjectIdentity = ObjectIdentity
fgt61E = _Fgt61E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 640)
)
_Fgt60E_ObjectIdentity = ObjectIdentity
fgt60E = _Fgt60E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 641)
)
_Fgt60EPOE_ObjectIdentity = ObjectIdentity
fgt60EPOE = _Fgt60EPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 642)
)
_Fgr60F_ObjectIdentity = ObjectIdentity
fgr60F = _Fgr60F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 643)
)
_Fgt60F_ObjectIdentity = ObjectIdentity
fgt60F = _Fgt60F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 644)
)
_Fgt61F_ObjectIdentity = ObjectIdentity
fgt61F = _Fgt61F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 645)
)
_Fwf60F_ObjectIdentity = ObjectIdentity
fwf60F = _Fwf60F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 646)
)
_Fwf61F_ObjectIdentity = ObjectIdentity
fwf61F = _Fwf61F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 647)
)
_Fgr60FI_ObjectIdentity = ObjectIdentity
fgr60FI = _Fgr60FI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 648)
)
_Fwf61E_ObjectIdentity = ObjectIdentity
fwf61E = _Fwf61E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 649)
)
_Fgt60EJ_ObjectIdentity = ObjectIdentity
fgt60EJ = _Fgt60EJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 661)
)
_Fwf60EJ_ObjectIdentity = ObjectIdentity
fwf60EJ = _Fwf60EJ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 662)
)
_Fgt60EV_ObjectIdentity = ObjectIdentity
fgt60EV = _Fgt60EV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 663)
)
_Fwf60EV_ObjectIdentity = ObjectIdentity
fwf60EV = _Fwf60EV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 664)
)
_Fgt70F_ObjectIdentity = ObjectIdentity
fgt70F = _Fgt70F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 701)
)
_Fgt71F_ObjectIdentity = ObjectIdentity
fgt71F = _Fgt71F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 702)
)
_Fr70FB_ObjectIdentity = ObjectIdentity
fr70FB = _Fr70FB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 704)
)
_Fr70FM_ObjectIdentity = ObjectIdentity
fr70FM = _Fr70FM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 705)
)
_Fw80FS_ObjectIdentity = ObjectIdentity
fw80FS = _Fw80FS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 826)
)
_Fw81FS_ObjectIdentity = ObjectIdentity
fw81FS = _Fw81FS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 827)
)
_Fgt80EPOE_ObjectIdentity = ObjectIdentity
fgt80EPOE = _Fgt80EPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 841)
)
_Fgt80E_ObjectIdentity = ObjectIdentity
fgt80E = _Fgt80E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 842)
)
_Fgt81E_ObjectIdentity = ObjectIdentity
fgt81E = _Fgt81E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 843)
)
_Fgt81EPOE_ObjectIdentity = ObjectIdentity
fgt81EPOE = _Fgt81EPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 844)
)
_Fgt80F_ObjectIdentity = ObjectIdentity
fgt80F = _Fgt80F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 845)
)
_Fgt81F_ObjectIdentity = ObjectIdentity
fgt81F = _Fgt81F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 846)
)
_Fgt80FBP_ObjectIdentity = ObjectIdentity
fgt80FBP = _Fgt80FBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 847)
)
_Fwf80F_ObjectIdentity = ObjectIdentity
fwf80F = _Fwf80F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 848)
)
_Fwf81F_ObjectIdentity = ObjectIdentity
fwf81F = _Fwf81F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 849)
)
_Fgt80FPOE_ObjectIdentity = ObjectIdentity
fgt80FPOE = _Fgt80FPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 850)
)
_Fgt81FPOE_ObjectIdentity = ObjectIdentity
fgt81FPOE = _Fgt81FPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 851)
)
_Fw81FD_ObjectIdentity = ObjectIdentity
fw81FD = _Fw81FD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 852)
)
_Fw81FP_ObjectIdentity = ObjectIdentity
fw81FP = _Fw81FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 853)
)
_Fgt80FDSL_ObjectIdentity = ObjectIdentity
fgt80FDSL = _Fgt80FDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 854)
)
_Fg900D_ObjectIdentity = ObjectIdentity
fg900D = _Fg900D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 900)
)
_Fgt90E_ObjectIdentity = ObjectIdentity
fgt90E = _Fgt90E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 940)
)
_Fgt91E_ObjectIdentity = ObjectIdentity
fgt91E = _Fgt91E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 941)
)
_Fgt90g_ObjectIdentity = ObjectIdentity
fgt90g = _Fgt90g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 942)
)
_Fgt91g_ObjectIdentity = ObjectIdentity
fgt91g = _Fgt91g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 943)
)
_Fwf90G_ObjectIdentity = ObjectIdentity
fwf90G = _Fwf90G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 944)
)
_Fwf91G_ObjectIdentity = ObjectIdentity
fwf91G = _Fwf91G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 945)
)
_Fgt100F_ObjectIdentity = ObjectIdentity
fgt100F = _Fgt100F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 1000)
)
_Fgt101F_ObjectIdentity = ObjectIdentity
fgt101F = _Fgt101F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 1001)
)
_Fgt140E_ObjectIdentity = ObjectIdentity
fgt140E = _Fgt140E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 1005)
)
_Fgt140EP_ObjectIdentity = ObjectIdentity
fgt140EP = _Fgt140EP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 1006)
)
_Fgt100E_ObjectIdentity = ObjectIdentity
fgt100E = _Fgt100E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 1041)
)
_Fgt100EF_ObjectIdentity = ObjectIdentity
fgt100EF = _Fgt100EF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 1042)
)
_Fgt101E_ObjectIdentity = ObjectIdentity
fgt101E = _Fgt101E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 1043)
)
_Fgt120g_ObjectIdentity = ObjectIdentity
fgt120g = _Fgt120g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 1201)
)
_Fgt121g_ObjectIdentity = ObjectIdentity
fgt121g = _Fgt121g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 1202)
)
_Fgt200E_ObjectIdentity = ObjectIdentity
fgt200E = _Fgt200E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 2009)
)
_Fgt201E_ObjectIdentity = ObjectIdentity
fgt201E = _Fgt201E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 2010)
)
_Fgt200F_ObjectIdentity = ObjectIdentity
fgt200F = _Fgt200F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 2011)
)
_Fgt201F_ObjectIdentity = ObjectIdentity
fgt201F = _Fgt201F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 2012)
)
_Fgt200G_ObjectIdentity = ObjectIdentity
fgt200G = _Fgt200G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 2013)
)
_Fgt201G_ObjectIdentity = ObjectIdentity
fgt201G = _Fgt201G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 2014)
)
_Fgt3HD_ObjectIdentity = ObjectIdentity
fgt3HD = _Fgt3HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 3006)
)
_Fgt300E_ObjectIdentity = ObjectIdentity
fgt300E = _Fgt300E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 3007)
)
_Fgt301E_ObjectIdentity = ObjectIdentity
fgt301E = _Fgt301E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 3008)
)
_Fgt400D_ObjectIdentity = ObjectIdentity
fgt400D = _Fgt400D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 4004)
)
_Fgt400E_ObjectIdentity = ObjectIdentity
fgt400E = _Fgt400E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 4007)
)
_Fgt401E_ObjectIdentity = ObjectIdentity
fgt401E = _Fgt401E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 4008)
)
_Fgt400EBP_ObjectIdentity = ObjectIdentity
fgt400EBP = _Fgt400EBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 4009)
)
_Fgt400F_ObjectIdentity = ObjectIdentity
fgt400F = _Fgt400F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 4010)
)
_Fgt401F_ObjectIdentity = ObjectIdentity
fgt401F = _Fgt401F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 4011)
)
_Fgt500D_ObjectIdentity = ObjectIdentity
fgt500D = _Fgt500D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 5004)
)
_Fgt500E_ObjectIdentity = ObjectIdentity
fgt500E = _Fgt500E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 5005)
)
_Fgt501E_ObjectIdentity = ObjectIdentity
fgt501E = _Fgt501E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 5006)
)
_Fgt600D_ObjectIdentity = ObjectIdentity
fgt600D = _Fgt600D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 6004)
)
_Fgt600E_ObjectIdentity = ObjectIdentity
fgt600E = _Fgt600E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 6005)
)
_Fgt601E_ObjectIdentity = ObjectIdentity
fgt601E = _Fgt601E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 6006)
)
_Fgt600F_ObjectIdentity = ObjectIdentity
fgt600F = _Fgt600F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 6007)
)
_Fgt601F_ObjectIdentity = ObjectIdentity
fgt601F = _Fgt601F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 6008)
)
_Fgt800D_ObjectIdentity = ObjectIdentity
fgt800D = _Fgt800D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 8004)
)
_Fgt900G_ObjectIdentity = ObjectIdentity
fgt900G = _Fgt900G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 9001)
)
_Fgt901G_ObjectIdentity = ObjectIdentity
fgt901G = _Fgt901G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 9002)
)
_Fgt1000D_ObjectIdentity = ObjectIdentity
fgt1000D = _Fgt1000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 10005)
)
_Fgt1100E_ObjectIdentity = ObjectIdentity
fgt1100E = _Fgt1100E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 10006)
)
_Fgt1101E_ObjectIdentity = ObjectIdentity
fgt1101E = _Fgt1101E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 10007)
)
_Fgt1000F_ObjectIdentity = ObjectIdentity
fgt1000F = _Fgt1000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 10008)
)
_Fgt1001F_ObjectIdentity = ObjectIdentity
fgt1001F = _Fgt1001F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 10009)
)
_Fgt1200D_ObjectIdentity = ObjectIdentity
fgt1200D = _Fgt1200D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 12000)
)
_Fgt1500D_ObjectIdentity = ObjectIdentity
fgt1500D = _Fgt1500D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 15000)
)
_Fgt1500DT_ObjectIdentity = ObjectIdentity
fgt1500DT = _Fgt1500DT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 15001)
)
_Fgt1801F_ObjectIdentity = ObjectIdentity
fgt1801F = _Fgt1801F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 15002)
)
_Fgt1800F_ObjectIdentity = ObjectIdentity
fgt1800F = _Fgt1800F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 15003)
)
_Ffw1801F_ObjectIdentity = ObjectIdentity
ffw1801F = _Ffw1801F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 15004)
)
_Fgt2200E_ObjectIdentity = ObjectIdentity
fgt2200E = _Fgt2200E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 18000)
)
_Fgt2201E_ObjectIdentity = ObjectIdentity
fgt2201E = _Fgt2201E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 18001)
)
_Fgt2000E_ObjectIdentity = ObjectIdentity
fgt2000E = _Fgt2000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 20000)
)
_Fgt2500E_ObjectIdentity = ObjectIdentity
fgt2500E = _Fgt2500E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 25000)
)
_Fgt2600F_ObjectIdentity = ObjectIdentity
fgt2600F = _Fgt2600F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 26000)
)
_Fgt2601F_ObjectIdentity = ObjectIdentity
fgt2601F = _Fgt2601F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 26001)
)
_Ffw2600F_ObjectIdentity = ObjectIdentity
ffw2600F = _Ffw2600F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 26002)
)
_Fgt3000D_ObjectIdentity = ObjectIdentity
fgt3000D = _Fgt3000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 30000)
)
_Fgt3300E_ObjectIdentity = ObjectIdentity
fgt3300E = _Fgt3300E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 30001)
)
_Fgt3301E_ObjectIdentity = ObjectIdentity
fgt3301E = _Fgt3301E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 30002)
)
_Fgt3000F_ObjectIdentity = ObjectIdentity
fgt3000F = _Fgt3000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 30003)
)
_Fgt3001F_ObjectIdentity = ObjectIdentity
fgt3001F = _Fgt3001F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 30004)
)
_Ffw3001F_ObjectIdentity = ObjectIdentity
ffw3001F = _Ffw3001F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 30005)
)
_Fgt3100D_ObjectIdentity = ObjectIdentity
fgt3100D = _Fgt3100D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 31000)
)
_Fgt3200D_ObjectIdentity = ObjectIdentity
fgt3200D = _Fgt3200D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 32000)
)
_Fgt3200F_ObjectIdentity = ObjectIdentity
fgt3200F = _Fgt3200F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 32010)
)
_Fgt3201F_ObjectIdentity = ObjectIdentity
fgt3201F = _Fgt3201F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 32011)
)
_Fgt3400E_ObjectIdentity = ObjectIdentity
fgt3400E = _Fgt3400E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 34001)
)
_Fgt3401E_ObjectIdentity = ObjectIdentity
fgt3401E = _Fgt3401E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 34011)
)
_Fgt3500F_ObjectIdentity = ObjectIdentity
fgt3500F = _Fgt3500F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 35001)
)
_Fgt3501F_ObjectIdentity = ObjectIdentity
fgt3501F = _Fgt3501F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 35011)
)
_Ffw3501F_ObjectIdentity = ObjectIdentity
ffw3501F = _Ffw3501F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 35012)
)
_Fgt3600E_ObjectIdentity = ObjectIdentity
fgt3600E = _Fgt3600E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 36001)
)
_Fgt3601E_ObjectIdentity = ObjectIdentity
fgt3601E = _Fgt3601E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 36011)
)
_Fgt3700D_ObjectIdentity = ObjectIdentity
fgt3700D = _Fgt3700D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 37000)
)
_Fgt3700F_ObjectIdentity = ObjectIdentity
fgt3700F = _Fgt3700F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 37001)
)
_Fgt3701F_ObjectIdentity = ObjectIdentity
fgt3701F = _Fgt3701F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 37011)
)
_Fgt3800D_ObjectIdentity = ObjectIdentity
fgt3800D = _Fgt3800D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 38001)
)
_Fgt4200F_ObjectIdentity = ObjectIdentity
fgt4200F = _Fgt4200F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 38002)
)
_Ffw4200F_ObjectIdentity = ObjectIdentity
ffw4200F = _Ffw4200F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 38006)
)
_Fgt3810D_ObjectIdentity = ObjectIdentity
fgt3810D = _Fgt3810D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 38101)
)
_Fgt3815D_ObjectIdentity = ObjectIdentity
fgt3815D = _Fgt3815D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 38150)
)
_Fgt4400F_ObjectIdentity = ObjectIdentity
fgt4400F = _Fgt4400F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 39001)
)
_Ffw4400F_ObjectIdentity = ObjectIdentity
ffw4400F = _Ffw4400F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 39007)
)
_Fgt3960E_ObjectIdentity = ObjectIdentity
fgt3960E = _Fgt3960E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 39601)
)
_Fgt3980E_ObjectIdentity = ObjectIdentity
fgt3980E = _Fgt3980E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 39801)
)
_Ffw3980E_ObjectIdentity = ObjectIdentity
ffw3980E = _Ffw3980E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 39804)
)
_Fgt4201F_ObjectIdentity = ObjectIdentity
fgt4201F = _Fgt4201F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 42002)
)
_Fgt4401F_ObjectIdentity = ObjectIdentity
fgt4401F = _Fgt4401F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 44001)
)
_Ffw4401F_ObjectIdentity = ObjectIdentity
ffw4401F = _Ffw4401F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 44002)
)
_Fgt4800F_ObjectIdentity = ObjectIdentity
fgt4800F = _Fgt4800F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 48000)
)
_Fgt4801F_ObjectIdentity = ObjectIdentity
fgt4801F = _Fgt4801F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 48001)
)
_Ffw4801F_ObjectIdentity = ObjectIdentity
ffw4801F = _Ffw4801F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 48003)
)
_Fgt5001D_ObjectIdentity = ObjectIdentity
fgt5001D = _Fgt5001D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 50015)
)
_Fgt5001E_ObjectIdentity = ObjectIdentity
fgt5001E = _Fgt5001E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 50016)
)
_Fgt5001E1_ObjectIdentity = ObjectIdentity
fgt5001E1 = _Fgt5001E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 50017)
)
_Fgt6000F_ObjectIdentity = ObjectIdentity
fgt6000F = _Fgt6000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 60001)
)
_Fgt7000E_ObjectIdentity = ObjectIdentity
fgt7000E = _Fgt7000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 70001)
)
_Fgt7000F_ObjectIdentity = ObjectIdentity
fgt7000F = _Fgt7000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 71201)
)
_Ffvmev_ObjectIdentity = ObjectIdentity
ffvmev = _Ffvmev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80000)
)
_Fgvmev_ObjectIdentity = ObjectIdentity
fgvmev = _Fgvmev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80001)
)
_Fgvmxx_ObjectIdentity = ObjectIdentity
fgvmxx = _Fgvmxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80002)
)
_Fgtvmx_ObjectIdentity = ObjectIdentity
fgtvmx = _Fgtvmx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80003)
)
_Fgvm00_ObjectIdentity = ObjectIdentity
fgvm00 = _Fgvm00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80004)
)
_Fgvm01_ObjectIdentity = ObjectIdentity
fgvm01 = _Fgvm01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80005)
)
_Fgvm02_ObjectIdentity = ObjectIdentity
fgvm02 = _Fgvm02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80006)
)
_Fgvm04_ObjectIdentity = ObjectIdentity
fgvm04 = _Fgvm04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80007)
)
_Fgvm08_ObjectIdentity = ObjectIdentity
fgvm08 = _Fgvm08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80008)
)
_Fgvm16_ObjectIdentity = ObjectIdentity
fgvm16 = _Fgvm16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80009)
)
_Fgvm32_ObjectIdentity = ObjectIdentity
fgvm32 = _Fgvm32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80010)
)
_Fgvm1v_ObjectIdentity = ObjectIdentity
fgvm1v = _Fgvm1v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80011)
)
_Fgvm2v_ObjectIdentity = ObjectIdentity
fgvm2v = _Fgvm2v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80012)
)
_Fgvm4v_ObjectIdentity = ObjectIdentity
fgvm4v = _Fgvm4v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80013)
)
_Fgvm8v_ObjectIdentity = ObjectIdentity
fgvm8v = _Fgvm8v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80014)
)
_Fgv16v_ObjectIdentity = ObjectIdentity
fgv16v = _Fgv16v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80015)
)
_Fgv32v_ObjectIdentity = ObjectIdentity
fgv32v = _Fgv32v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80016)
)
_Fgvulv_ObjectIdentity = ObjectIdentity
fgvulv = _Fgvulv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80019)
)
_Fgvmul_ObjectIdentity = ObjectIdentity
fgvmul = _Fgvmul_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80020)
)
_Fgvmsl_ObjectIdentity = ObjectIdentity
fgvmsl = _Fgvmsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80021)
)
_Fgvmsb_ObjectIdentity = ObjectIdentity
fgvmsb = _Fgvmsb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80022)
)
_Fgvmel_ObjectIdentity = ObjectIdentity
fgvmel = _Fgvmel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80023)
)
_Fgvmml_ObjectIdentity = ObjectIdentity
fgvmml = _Fgvmml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80024)
)
_Ffvmbb_ObjectIdentity = ObjectIdentity
ffvmbb = _Ffvmbb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80025)
)
_Fgvmpg_ObjectIdentity = ObjectIdentity
fgvmpg = _Fgvmpg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 80030)
)
_FgtARM64AWS_ObjectIdentity = ObjectIdentity
fgtARM64AWS = _FgtARM64AWS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 90007)
)
_FgtARM64XEN_ObjectIdentity = ObjectIdentity
fgtARM64XEN = _FgtARM64XEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 90008)
)
_FgtVM64ALI_ObjectIdentity = ObjectIdentity
fgtVM64ALI = _FgtVM64ALI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 90019)
)
_FgtVM64RAXONDEMAND_ObjectIdentity = ObjectIdentity
fgtVM64RAXONDEMAND = _FgtVM64RAXONDEMAND_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 90021)
)
_FgtVM64IBM_ObjectIdentity = ObjectIdentity
fgtVM64IBM = _FgtVM64IBM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 90022)
)
_FgtARM64OCI_ObjectIdentity = ObjectIdentity
fgtARM64OCI = _FgtARM64OCI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 90025)
)
_FgtARM64GCP_ObjectIdentity = ObjectIdentity
fgtARM64GCP = _FgtARM64GCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 90026)
)
_FgtARM64AZURE_ObjectIdentity = ObjectIdentity
fgtARM64AZURE = _FgtARM64AZURE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 90027)
)
_FfwVM64_ObjectIdentity = ObjectIdentity
ffwVM64 = _FfwVM64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 90070)
)
_FfwVM64KVm_ObjectIdentity = ObjectIdentity
ffwVM64KVm = _FfwVM64KVm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 90071)
)
_FgtVM64AZURE_ObjectIdentity = ObjectIdentity
fgtVM64AZURE = _FgtVM64AZURE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 1, 90081)
)
_FgTraps_ObjectIdentity = ObjectIdentity
fgTraps = _FgTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2)
)
_FgTrapPrefix_ObjectIdentity = ObjectIdentity
fgTrapPrefix = _FgTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0)
)
_FgVirtualDomain_ObjectIdentity = ObjectIdentity
fgVirtualDomain = _FgVirtualDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3)
)
_FgVdInfo_ObjectIdentity = ObjectIdentity
fgVdInfo = _FgVdInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 1)
)
_FgVdNumber_Type = Integer32
_FgVdNumber_Object = MibScalar
fgVdNumber = _FgVdNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 1, 1),
    _FgVdNumber_Type()
)
fgVdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdNumber.setStatus("current")
_FgVdMaxVdoms_Type = Integer32
_FgVdMaxVdoms_Object = MibScalar
fgVdMaxVdoms = _FgVdMaxVdoms_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 1, 2),
    _FgVdMaxVdoms_Type()
)
fgVdMaxVdoms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdMaxVdoms.setStatus("current")
_FgVdEnabled_Type = FnBoolState
_FgVdEnabled_Object = MibScalar
fgVdEnabled = _FgVdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 1, 3),
    _FgVdEnabled_Type()
)
fgVdEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEnabled.setStatus("current")
_FgVdTables_ObjectIdentity = ObjectIdentity
fgVdTables = _FgVdTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2)
)
_FgVdTable_Object = MibTable
fgVdTable = _FgVdTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1)
)
if mibBuilder.loadTexts:
    fgVdTable.setStatus("current")
_FgVdEntry_Object = MibTableRow
fgVdEntry = _FgVdEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1)
)
fgVdEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgVdEntry.setStatus("current")
_FgVdEntIndex_Type = FgVdIndex
_FgVdEntIndex_Object = MibTableColumn
fgVdEntIndex = _FgVdEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 1),
    _FgVdEntIndex_Type()
)
fgVdEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntIndex.setStatus("current")
_FgVdEntName_Type = DisplayString
_FgVdEntName_Object = MibTableColumn
fgVdEntName = _FgVdEntName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 2),
    _FgVdEntName_Type()
)
fgVdEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntName.setStatus("current")
_FgVdEntOpMode_Type = FgOpMode
_FgVdEntOpMode_Object = MibTableColumn
fgVdEntOpMode = _FgVdEntOpMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 3),
    _FgVdEntOpMode_Type()
)
fgVdEntOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntOpMode.setStatus("current")
_FgVdEntHaState_Type = FgHaState
_FgVdEntHaState_Object = MibTableColumn
fgVdEntHaState = _FgVdEntHaState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 4),
    _FgVdEntHaState_Type()
)
fgVdEntHaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntHaState.setStatus("current")


class _FgVdEntCpuUsage_Type(Gauge32):
    """Custom type fgVdEntCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgVdEntCpuUsage_Type.__name__ = "Gauge32"
_FgVdEntCpuUsage_Object = MibTableColumn
fgVdEntCpuUsage = _FgVdEntCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 5),
    _FgVdEntCpuUsage_Type()
)
fgVdEntCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntCpuUsage.setStatus("current")


class _FgVdEntMemUsage_Type(Gauge32):
    """Custom type fgVdEntMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgVdEntMemUsage_Type.__name__ = "Gauge32"
_FgVdEntMemUsage_Object = MibTableColumn
fgVdEntMemUsage = _FgVdEntMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 6),
    _FgVdEntMemUsage_Type()
)
fgVdEntMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntMemUsage.setStatus("current")
_FgVdEntSesCount_Type = Gauge32
_FgVdEntSesCount_Object = MibTableColumn
fgVdEntSesCount = _FgVdEntSesCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 7),
    _FgVdEntSesCount_Type()
)
fgVdEntSesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntSesCount.setStatus("current")
_FgVdEntSesRate_Type = Gauge32
_FgVdEntSesRate_Object = MibTableColumn
fgVdEntSesRate = _FgVdEntSesRate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 8),
    _FgVdEntSesRate_Type()
)
fgVdEntSesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntSesRate.setStatus("current")
if mibBuilder.loadTexts:
    fgVdEntSesRate.setUnits("Sessions Per Second")


class _FgVdEntChecksum_Type(DisplayString):
    """Custom type fgVdEntChecksum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgVdEntChecksum_Type.__name__ = "DisplayString"
_FgVdEntChecksum_Object = MibTableColumn
fgVdEntChecksum = _FgVdEntChecksum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 1, 1, 9),
    _FgVdEntChecksum_Type()
)
fgVdEntChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdEntChecksum.setStatus("current")
_FgVdTpTable_Object = MibTable
fgVdTpTable = _FgVdTpTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 2)
)
if mibBuilder.loadTexts:
    fgVdTpTable.setStatus("current")
_FgVdTpEntry_Object = MibTableRow
fgVdTpEntry = _FgVdTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 2, 1)
)
fgVdTpEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgVdTpEntry.setStatus("current")
_FgVdTpMgmtAddrType_Type = InetAddressType
_FgVdTpMgmtAddrType_Object = MibTableColumn
fgVdTpMgmtAddrType = _FgVdTpMgmtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 2, 1, 1),
    _FgVdTpMgmtAddrType_Type()
)
fgVdTpMgmtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdTpMgmtAddrType.setStatus("current")
_FgVdTpMgmtAddr_Type = InetAddress
_FgVdTpMgmtAddr_Object = MibTableColumn
fgVdTpMgmtAddr = _FgVdTpMgmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 2, 1, 2),
    _FgVdTpMgmtAddr_Type()
)
fgVdTpMgmtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdTpMgmtAddr.setStatus("current")
_FgVdTpMgmtMask_Type = InetAddressPrefixLength
_FgVdTpMgmtMask_Object = MibTableColumn
fgVdTpMgmtMask = _FgVdTpMgmtMask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 3, 2, 2, 1, 3),
    _FgVdTpMgmtMask_Type()
)
fgVdTpMgmtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVdTpMgmtMask.setStatus("current")
_FgSystem_ObjectIdentity = ObjectIdentity
fgSystem = _FgSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4)
)
_FgSystemInfo_ObjectIdentity = ObjectIdentity
fgSystemInfo = _FgSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1)
)


class _FgSysVersion_Type(DisplayString):
    """Custom type fgSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgSysVersion_Type.__name__ = "DisplayString"
_FgSysVersion_Object = MibScalar
fgSysVersion = _FgSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 1),
    _FgSysVersion_Type()
)
fgSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysVersion.setStatus("current")
_FgSysMgmtVdom_Type = FgVdIndex
_FgSysMgmtVdom_Object = MibScalar
fgSysMgmtVdom = _FgSysMgmtVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 2),
    _FgSysMgmtVdom_Type()
)
fgSysMgmtVdom.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgSysMgmtVdom.setStatus("current")


class _FgSysCpuUsage_Type(Gauge32):
    """Custom type fgSysCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgSysCpuUsage_Type.__name__ = "Gauge32"
_FgSysCpuUsage_Object = MibScalar
fgSysCpuUsage = _FgSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 3),
    _FgSysCpuUsage_Type()
)
fgSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysCpuUsage.setStatus("current")


class _FgSysMemUsage_Type(Gauge32):
    """Custom type fgSysMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgSysMemUsage_Type.__name__ = "Gauge32"
_FgSysMemUsage_Object = MibScalar
fgSysMemUsage = _FgSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 4),
    _FgSysMemUsage_Type()
)
fgSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysMemUsage.setStatus("current")
_FgSysMemCapacity_Type = Gauge32
_FgSysMemCapacity_Object = MibScalar
fgSysMemCapacity = _FgSysMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 5),
    _FgSysMemCapacity_Type()
)
fgSysMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysMemCapacity.setStatus("current")
_FgSysDiskUsage_Type = Gauge32
_FgSysDiskUsage_Object = MibScalar
fgSysDiskUsage = _FgSysDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 6),
    _FgSysDiskUsage_Type()
)
fgSysDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysDiskUsage.setStatus("current")
_FgSysDiskCapacity_Type = Gauge32
_FgSysDiskCapacity_Object = MibScalar
fgSysDiskCapacity = _FgSysDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 7),
    _FgSysDiskCapacity_Type()
)
fgSysDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysDiskCapacity.setStatus("current")
_FgSysSesCount_Type = Gauge32
_FgSysSesCount_Object = MibScalar
fgSysSesCount = _FgSysSesCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 8),
    _FgSysSesCount_Type()
)
fgSysSesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSesCount.setStatus("current")


class _FgSysLowMemUsage_Type(Gauge32):
    """Custom type fgSysLowMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgSysLowMemUsage_Type.__name__ = "Gauge32"
_FgSysLowMemUsage_Object = MibScalar
fgSysLowMemUsage = _FgSysLowMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 9),
    _FgSysLowMemUsage_Type()
)
fgSysLowMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysLowMemUsage.setStatus("current")
_FgSysLowMemCapacity_Type = Gauge32
_FgSysLowMemCapacity_Object = MibScalar
fgSysLowMemCapacity = _FgSysLowMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 10),
    _FgSysLowMemCapacity_Type()
)
fgSysLowMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysLowMemCapacity.setStatus("current")
_FgSysSesRate1_Type = Gauge32
_FgSysSesRate1_Object = MibScalar
fgSysSesRate1 = _FgSysSesRate1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 11),
    _FgSysSesRate1_Type()
)
fgSysSesRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSesRate1.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSesRate1.setUnits("Sessions Per Second")
_FgSysSesRate10_Type = Gauge32
_FgSysSesRate10_Object = MibScalar
fgSysSesRate10 = _FgSysSesRate10_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 12),
    _FgSysSesRate10_Type()
)
fgSysSesRate10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSesRate10.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSesRate10.setUnits("Sessions Per Second")
_FgSysSesRate30_Type = Gauge32
_FgSysSesRate30_Object = MibScalar
fgSysSesRate30 = _FgSysSesRate30_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 13),
    _FgSysSesRate30_Type()
)
fgSysSesRate30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSesRate30.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSesRate30.setUnits("Sessions Per Second")
_FgSysSesRate60_Type = Gauge32
_FgSysSesRate60_Object = MibScalar
fgSysSesRate60 = _FgSysSesRate60_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 14),
    _FgSysSesRate60_Type()
)
fgSysSesRate60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSesRate60.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSesRate60.setUnits("Sessions Per Second")
_FgSysSes6Count_Type = Gauge32
_FgSysSes6Count_Object = MibScalar
fgSysSes6Count = _FgSysSes6Count_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 15),
    _FgSysSes6Count_Type()
)
fgSysSes6Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSes6Count.setStatus("current")
_FgSysSes6Rate1_Type = Gauge32
_FgSysSes6Rate1_Object = MibScalar
fgSysSes6Rate1 = _FgSysSes6Rate1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 16),
    _FgSysSes6Rate1_Type()
)
fgSysSes6Rate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSes6Rate1.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSes6Rate1.setUnits("Sessions Per Second")
_FgSysSes6Rate10_Type = Gauge32
_FgSysSes6Rate10_Object = MibScalar
fgSysSes6Rate10 = _FgSysSes6Rate10_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 17),
    _FgSysSes6Rate10_Type()
)
fgSysSes6Rate10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSes6Rate10.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSes6Rate10.setUnits("Sessions Per Second")
_FgSysSes6Rate30_Type = Gauge32
_FgSysSes6Rate30_Object = MibScalar
fgSysSes6Rate30 = _FgSysSes6Rate30_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 18),
    _FgSysSes6Rate30_Type()
)
fgSysSes6Rate30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSes6Rate30.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSes6Rate30.setUnits("Sessions Per Second")
_FgSysSes6Rate60_Type = Gauge32
_FgSysSes6Rate60_Object = MibScalar
fgSysSes6Rate60 = _FgSysSes6Rate60_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 19),
    _FgSysSes6Rate60_Type()
)
fgSysSes6Rate60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysSes6Rate60.setStatus("current")
if mibBuilder.loadTexts:
    fgSysSes6Rate60.setUnits("Sessions Per Second")
_FgSysUpTime_Type = Counter64
_FgSysUpTime_Object = MibScalar
fgSysUpTime = _FgSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 20),
    _FgSysUpTime_Type()
)
fgSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysUpTime.setStatus("current")
if mibBuilder.loadTexts:
    fgSysUpTime.setUnits("hundredths of a second")
_FgSysNeedLogPartitionScan_Type = FnBoolState
_FgSysNeedLogPartitionScan_Object = MibScalar
fgSysNeedLogPartitionScan = _FgSysNeedLogPartitionScan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 21),
    _FgSysNeedLogPartitionScan_Type()
)
fgSysNeedLogPartitionScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysNeedLogPartitionScan.setStatus("current")


class _FgSysUpTimeDetail_Type(DisplayString):
    """Custom type fgSysUpTimeDetail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgSysUpTimeDetail_Type.__name__ = "DisplayString"
_FgSysUpTimeDetail_Object = MibScalar
fgSysUpTimeDetail = _FgSysUpTimeDetail_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 22),
    _FgSysUpTimeDetail_Type()
)
fgSysUpTimeDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysUpTimeDetail.setStatus("current")


class _FgSysRebootReason_Type(DisplayString):
    """Custom type fgSysRebootReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FgSysRebootReason_Type.__name__ = "DisplayString"
_FgSysRebootReason_Object = MibScalar
fgSysRebootReason = _FgSysRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 23),
    _FgSysRebootReason_Type()
)
fgSysRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysRebootReason.setStatus("current")
_FgSysNpuSesCount_Type = Gauge32
_FgSysNpuSesCount_Object = MibScalar
fgSysNpuSesCount = _FgSysNpuSesCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 24),
    _FgSysNpuSesCount_Type()
)
fgSysNpuSesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysNpuSesCount.setStatus("current")
_FgSysNpuSesRate1_Type = Gauge32
_FgSysNpuSesRate1_Object = MibScalar
fgSysNpuSesRate1 = _FgSysNpuSesRate1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 25),
    _FgSysNpuSesRate1_Type()
)
fgSysNpuSesRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysNpuSesRate1.setStatus("current")
if mibBuilder.loadTexts:
    fgSysNpuSesRate1.setUnits("Sessions Per Second")
_FgSysNpuSesRate10_Type = Gauge32
_FgSysNpuSesRate10_Object = MibScalar
fgSysNpuSesRate10 = _FgSysNpuSesRate10_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 26),
    _FgSysNpuSesRate10_Type()
)
fgSysNpuSesRate10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysNpuSesRate10.setStatus("current")
if mibBuilder.loadTexts:
    fgSysNpuSesRate10.setUnits("Sessions Per Second")
_FgSysNpuSesRate30_Type = Gauge32
_FgSysNpuSesRate30_Object = MibScalar
fgSysNpuSesRate30 = _FgSysNpuSesRate30_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 27),
    _FgSysNpuSesRate30_Type()
)
fgSysNpuSesRate30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysNpuSesRate30.setStatus("current")
if mibBuilder.loadTexts:
    fgSysNpuSesRate30.setUnits("Sessions Per Second")
_FgSysNpuSesRate60_Type = Gauge32
_FgSysNpuSesRate60_Object = MibScalar
fgSysNpuSesRate60 = _FgSysNpuSesRate60_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 28),
    _FgSysNpuSesRate60_Type()
)
fgSysNpuSesRate60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysNpuSesRate60.setStatus("current")
if mibBuilder.loadTexts:
    fgSysNpuSesRate60.setUnits("Sessions Per Second")
_FgSysNpuSes6Count_Type = Gauge32
_FgSysNpuSes6Count_Object = MibScalar
fgSysNpuSes6Count = _FgSysNpuSes6Count_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 29),
    _FgSysNpuSes6Count_Type()
)
fgSysNpuSes6Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysNpuSes6Count.setStatus("current")
_FgSysNpuSes6Rate1_Type = Gauge32
_FgSysNpuSes6Rate1_Object = MibScalar
fgSysNpuSes6Rate1 = _FgSysNpuSes6Rate1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 30),
    _FgSysNpuSes6Rate1_Type()
)
fgSysNpuSes6Rate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysNpuSes6Rate1.setStatus("current")
if mibBuilder.loadTexts:
    fgSysNpuSes6Rate1.setUnits("Sessions Per Second")
_FgSysNpuSes6Rate10_Type = Gauge32
_FgSysNpuSes6Rate10_Object = MibScalar
fgSysNpuSes6Rate10 = _FgSysNpuSes6Rate10_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 31),
    _FgSysNpuSes6Rate10_Type()
)
fgSysNpuSes6Rate10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysNpuSes6Rate10.setStatus("current")
if mibBuilder.loadTexts:
    fgSysNpuSes6Rate10.setUnits("Sessions Per Second")
_FgSysNpuSes6Rate30_Type = Gauge32
_FgSysNpuSes6Rate30_Object = MibScalar
fgSysNpuSes6Rate30 = _FgSysNpuSes6Rate30_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 32),
    _FgSysNpuSes6Rate30_Type()
)
fgSysNpuSes6Rate30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysNpuSes6Rate30.setStatus("current")
if mibBuilder.loadTexts:
    fgSysNpuSes6Rate30.setUnits("Sessions Per Second")
_FgSysNpuSes6Rate60_Type = Gauge32
_FgSysNpuSes6Rate60_Object = MibScalar
fgSysNpuSes6Rate60 = _FgSysNpuSes6Rate60_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 33),
    _FgSysNpuSes6Rate60_Type()
)
fgSysNpuSes6Rate60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysNpuSes6Rate60.setStatus("current")
if mibBuilder.loadTexts:
    fgSysNpuSes6Rate60.setUnits("Sessions Per Second")


class _FgDataCpuUsage_Type(Gauge32):
    """Custom type fgDataCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgDataCpuUsage_Type.__name__ = "Gauge32"
_FgDataCpuUsage_Object = MibScalar
fgDataCpuUsage = _FgDataCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 34),
    _FgDataCpuUsage_Type()
)
fgDataCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDataCpuUsage.setStatus("current")


class _FgDataMemUsage_Type(Gauge32):
    """Custom type fgDataMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgDataMemUsage_Type.__name__ = "Gauge32"
_FgDataMemUsage_Object = MibScalar
fgDataMemUsage = _FgDataMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 35),
    _FgDataMemUsage_Type()
)
fgDataMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDataMemUsage.setStatus("current")


class _FgSysFreeMemUsage_Type(Gauge32):
    """Custom type fgSysFreeMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgSysFreeMemUsage_Type.__name__ = "Gauge32"
_FgSysFreeMemUsage_Object = MibScalar
fgSysFreeMemUsage = _FgSysFreeMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 36),
    _FgSysFreeMemUsage_Type()
)
fgSysFreeMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysFreeMemUsage.setStatus("current")


class _FgSysFreeableMemUsage_Type(Gauge32):
    """Custom type fgSysFreeableMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgSysFreeableMemUsage_Type.__name__ = "Gauge32"
_FgSysFreeableMemUsage_Object = MibScalar
fgSysFreeableMemUsage = _FgSysFreeableMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 37),
    _FgSysFreeableMemUsage_Type()
)
fgSysFreeableMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysFreeableMemUsage.setStatus("current")


class _FgDataSecurityLevel_Type(Integer32):
    """Custom type fgDataSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_FgDataSecurityLevel_Type.__name__ = "Integer32"
_FgDataSecurityLevel_Object = MibScalar
fgDataSecurityLevel = _FgDataSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 1, 38),
    _FgDataSecurityLevel_Type()
)
fgDataSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDataSecurityLevel.setStatus("current")
_FgSoftware_ObjectIdentity = ObjectIdentity
fgSoftware = _FgSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 2)
)


class _FgSysVersionAv_Type(DisplayString):
    """Custom type fgSysVersionAv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgSysVersionAv_Type.__name__ = "DisplayString"
_FgSysVersionAv_Object = MibScalar
fgSysVersionAv = _FgSysVersionAv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 2, 1),
    _FgSysVersionAv_Type()
)
fgSysVersionAv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysVersionAv.setStatus("current")


class _FgSysVersionIps_Type(DisplayString):
    """Custom type fgSysVersionIps based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgSysVersionIps_Type.__name__ = "DisplayString"
_FgSysVersionIps_Object = MibScalar
fgSysVersionIps = _FgSysVersionIps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 2, 2),
    _FgSysVersionIps_Type()
)
fgSysVersionIps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysVersionIps.setStatus("current")


class _FgSysVersionAvEt_Type(DisplayString):
    """Custom type fgSysVersionAvEt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgSysVersionAvEt_Type.__name__ = "DisplayString"
_FgSysVersionAvEt_Object = MibScalar
fgSysVersionAvEt = _FgSysVersionAvEt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 2, 3),
    _FgSysVersionAvEt_Type()
)
fgSysVersionAvEt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysVersionAvEt.setStatus("current")


class _FgSysVersionIpsEt_Type(DisplayString):
    """Custom type fgSysVersionIpsEt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgSysVersionIpsEt_Type.__name__ = "DisplayString"
_FgSysVersionIpsEt_Object = MibScalar
fgSysVersionIpsEt = _FgSysVersionIpsEt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 2, 4),
    _FgSysVersionIpsEt_Type()
)
fgSysVersionIpsEt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSysVersionIpsEt.setStatus("current")
_FgHwSensors_ObjectIdentity = ObjectIdentity
fgHwSensors = _FgHwSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3)
)
_FgHwSensorCount_Type = Integer32
_FgHwSensorCount_Object = MibScalar
fgHwSensorCount = _FgHwSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3, 1),
    _FgHwSensorCount_Type()
)
fgHwSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHwSensorCount.setStatus("current")
_FgHwSensorTable_Object = MibTable
fgHwSensorTable = _FgHwSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3, 2)
)
if mibBuilder.loadTexts:
    fgHwSensorTable.setStatus("current")
_FgHwSensorEntry_Object = MibTableRow
fgHwSensorEntry = _FgHwSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3, 2, 1)
)
fgHwSensorEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgHwSensorEntIndex"),
)
if mibBuilder.loadTexts:
    fgHwSensorEntry.setStatus("current")
_FgHwSensorEntIndex_Type = FnIndex
_FgHwSensorEntIndex_Object = MibTableColumn
fgHwSensorEntIndex = _FgHwSensorEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3, 2, 1, 1),
    _FgHwSensorEntIndex_Type()
)
fgHwSensorEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgHwSensorEntIndex.setStatus("current")
_FgHwSensorEntName_Type = DisplayString
_FgHwSensorEntName_Object = MibTableColumn
fgHwSensorEntName = _FgHwSensorEntName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3, 2, 1, 2),
    _FgHwSensorEntName_Type()
)
fgHwSensorEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHwSensorEntName.setStatus("current")
_FgHwSensorEntValue_Type = DisplayString
_FgHwSensorEntValue_Object = MibTableColumn
fgHwSensorEntValue = _FgHwSensorEntValue_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3, 2, 1, 3),
    _FgHwSensorEntValue_Type()
)
fgHwSensorEntValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHwSensorEntValue.setStatus("current")


class _FgHwSensorEntAlarmStatus_Type(Integer32):
    """Custom type fgHwSensorEntAlarmStatus based on Integer32"""
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


_FgHwSensorEntAlarmStatus_Type.__name__ = "Integer32"
_FgHwSensorEntAlarmStatus_Object = MibTableColumn
fgHwSensorEntAlarmStatus = _FgHwSensorEntAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 3, 2, 1, 4),
    _FgHwSensorEntAlarmStatus_Type()
)
fgHwSensorEntAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHwSensorEntAlarmStatus.setStatus("current")
_FgProcessors_ObjectIdentity = ObjectIdentity
fgProcessors = _FgProcessors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4)
)
_FgProcessorCount_Type = Integer32
_FgProcessorCount_Object = MibScalar
fgProcessorCount = _FgProcessorCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 1),
    _FgProcessorCount_Type()
)
fgProcessorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorCount.setStatus("current")
_FgProcessorTable_Object = MibTable
fgProcessorTable = _FgProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2)
)
if mibBuilder.loadTexts:
    fgProcessorTable.setStatus("current")
_FgProcessorEntry_Object = MibTableRow
fgProcessorEntry = _FgProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1)
)
fgProcessorEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgProcessorEntIndex"),
)
if mibBuilder.loadTexts:
    fgProcessorEntry.setStatus("current")
_FgProcessorEntIndex_Type = FnIndex
_FgProcessorEntIndex_Object = MibTableColumn
fgProcessorEntIndex = _FgProcessorEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 1),
    _FgProcessorEntIndex_Type()
)
fgProcessorEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgProcessorEntIndex.setStatus("current")


class _FgProcessorUsage_Type(Gauge32):
    """Custom type fgProcessorUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgProcessorUsage_Type.__name__ = "Gauge32"
_FgProcessorUsage_Object = MibTableColumn
fgProcessorUsage = _FgProcessorUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 2),
    _FgProcessorUsage_Type()
)
fgProcessorUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorUsage.setStatus("current")
if mibBuilder.loadTexts:
    fgProcessorUsage.setUnits("%")


class _FgProcessorUsage5sec_Type(Gauge32):
    """Custom type fgProcessorUsage5sec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgProcessorUsage5sec_Type.__name__ = "Gauge32"
_FgProcessorUsage5sec_Object = MibTableColumn
fgProcessorUsage5sec = _FgProcessorUsage5sec_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 3),
    _FgProcessorUsage5sec_Type()
)
fgProcessorUsage5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorUsage5sec.setStatus("current")
if mibBuilder.loadTexts:
    fgProcessorUsage5sec.setUnits("%")
_FgProcessorType_Type = AutonomousType
_FgProcessorType_Object = MibTableColumn
fgProcessorType = _FgProcessorType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 4),
    _FgProcessorType_Type()
)
fgProcessorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorType.setStatus("current")
_FgProcessorContainedIn_Type = FnIndex
_FgProcessorContainedIn_Object = MibTableColumn
fgProcessorContainedIn = _FgProcessorContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 5),
    _FgProcessorContainedIn_Type()
)
fgProcessorContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorContainedIn.setStatus("current")
_FgProcessorPktRxCount_Type = Counter64
_FgProcessorPktRxCount_Object = MibTableColumn
fgProcessorPktRxCount = _FgProcessorPktRxCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 6),
    _FgProcessorPktRxCount_Type()
)
fgProcessorPktRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorPktRxCount.setStatus("current")
_FgProcessorPktTxCount_Type = Counter64
_FgProcessorPktTxCount_Object = MibTableColumn
fgProcessorPktTxCount = _FgProcessorPktTxCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 7),
    _FgProcessorPktTxCount_Type()
)
fgProcessorPktTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorPktTxCount.setStatus("current")
_FgProcessorPktDroppedCount_Type = Counter64
_FgProcessorPktDroppedCount_Object = MibTableColumn
fgProcessorPktDroppedCount = _FgProcessorPktDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 8),
    _FgProcessorPktDroppedCount_Type()
)
fgProcessorPktDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorPktDroppedCount.setStatus("current")


class _FgProcessorUserUsage_Type(Gauge32):
    """Custom type fgProcessorUserUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgProcessorUserUsage_Type.__name__ = "Gauge32"
_FgProcessorUserUsage_Object = MibTableColumn
fgProcessorUserUsage = _FgProcessorUserUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 9),
    _FgProcessorUserUsage_Type()
)
fgProcessorUserUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorUserUsage.setStatus("current")
if mibBuilder.loadTexts:
    fgProcessorUserUsage.setUnits("%")


class _FgProcessorSysUsage_Type(Gauge32):
    """Custom type fgProcessorSysUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgProcessorSysUsage_Type.__name__ = "Gauge32"
_FgProcessorSysUsage_Object = MibTableColumn
fgProcessorSysUsage = _FgProcessorSysUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 10),
    _FgProcessorSysUsage_Type()
)
fgProcessorSysUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorSysUsage.setStatus("current")
if mibBuilder.loadTexts:
    fgProcessorSysUsage.setUnits("%")
_FgProcessorPktTxDroppedCount_Type = Counter64
_FgProcessorPktTxDroppedCount_Object = MibTableColumn
fgProcessorPktTxDroppedCount = _FgProcessorPktTxDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 2, 1, 11),
    _FgProcessorPktTxDroppedCount_Type()
)
fgProcessorPktTxDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorPktTxDroppedCount.setStatus("current")
_FgProcessorTypes_ObjectIdentity = ObjectIdentity
fgProcessorTypes = _FgProcessorTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3)
)
_FgProcessorOther_ObjectIdentity = ObjectIdentity
fgProcessorOther = _FgProcessorOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 1)
)
if mibBuilder.loadTexts:
    fgProcessorOther.setStatus("current")
_FgProcessorIntel_ObjectIdentity = ObjectIdentity
fgProcessorIntel = _FgProcessorIntel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 2)
)
if mibBuilder.loadTexts:
    fgProcessorIntel.setStatus("current")
_FgProcessorAMD_ObjectIdentity = ObjectIdentity
fgProcessorAMD = _FgProcessorAMD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 3)
)
if mibBuilder.loadTexts:
    fgProcessorAMD.setStatus("current")
_FgProcessorXlr_ObjectIdentity = ObjectIdentity
fgProcessorXlr = _FgProcessorXlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 4)
)
if mibBuilder.loadTexts:
    fgProcessorXlr.setStatus("current")
_FgProcessorFnSoc_ObjectIdentity = ObjectIdentity
fgProcessorFnSoc = _FgProcessorFnSoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 5)
)
if mibBuilder.loadTexts:
    fgProcessorFnSoc.setStatus("current")
_FgProcessorFnNP2_ObjectIdentity = ObjectIdentity
fgProcessorFnNP2 = _FgProcessorFnNP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 6)
)
if mibBuilder.loadTexts:
    fgProcessorFnNP2.setStatus("current")
_FgProcessorFnNP4_ObjectIdentity = ObjectIdentity
fgProcessorFnNP4 = _FgProcessorFnNP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 7)
)
if mibBuilder.loadTexts:
    fgProcessorFnNP4.setStatus("current")
_FgProcessorFnNP6_ObjectIdentity = ObjectIdentity
fgProcessorFnNP6 = _FgProcessorFnNP6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 8)
)
if mibBuilder.loadTexts:
    fgProcessorFnNP6.setStatus("current")
_FgProcessorFnNP6LITE_ObjectIdentity = ObjectIdentity
fgProcessorFnNP6LITE = _FgProcessorFnNP6LITE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 9)
)
if mibBuilder.loadTexts:
    fgProcessorFnNP6LITE.setStatus("current")
_FgProcessorFnNP7_ObjectIdentity = ObjectIdentity
fgProcessorFnNP7 = _FgProcessorFnNP7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 10)
)
if mibBuilder.loadTexts:
    fgProcessorFnNP7.setStatus("current")
_FgProcessorFnNP6XLITE_ObjectIdentity = ObjectIdentity
fgProcessorFnNP6XLITE = _FgProcessorFnNP6XLITE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 11)
)
if mibBuilder.loadTexts:
    fgProcessorFnNP6XLITE.setStatus("current")
_FgProcessorFnNP7LITE_ObjectIdentity = ObjectIdentity
fgProcessorFnNP7LITE = _FgProcessorFnNP7LITE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 3, 12)
)
if mibBuilder.loadTexts:
    fgProcessorFnNP7LITE.setStatus("current")
_FgProcessorsTrapObjects_ObjectIdentity = ObjectIdentity
fgProcessorsTrapObjects = _FgProcessorsTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 4)
)
_FgPerCpuHighDetails_Type = DisplayString
_FgPerCpuHighDetails_Object = MibScalar
fgPerCpuHighDetails = _FgPerCpuHighDetails_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 4, 4, 1),
    _FgPerCpuHighDetails_Type()
)
fgPerCpuHighDetails.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgPerCpuHighDetails.setStatus("current")
_FgProcessorModules_ObjectIdentity = ObjectIdentity
fgProcessorModules = _FgProcessorModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5)
)
_FgProcessorModuleTypes_ObjectIdentity = ObjectIdentity
fgProcessorModuleTypes = _FgProcessorModuleTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1)
)
_FgProcModOther_ObjectIdentity = ObjectIdentity
fgProcModOther = _FgProcModOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 1)
)
if mibBuilder.loadTexts:
    fgProcModOther.setStatus("current")
_FgProcModIntegrated_ObjectIdentity = ObjectIdentity
fgProcModIntegrated = _FgProcModIntegrated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 2)
)
if mibBuilder.loadTexts:
    fgProcModIntegrated.setStatus("current")
_FgProcModIntegratedNPU_ObjectIdentity = ObjectIdentity
fgProcModIntegratedNPU = _FgProcModIntegratedNPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 1, 3)
)
if mibBuilder.loadTexts:
    fgProcModIntegratedNPU.setStatus("current")
_FgProcessorModuleCount_Type = Integer32
_FgProcessorModuleCount_Object = MibScalar
fgProcessorModuleCount = _FgProcessorModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 2),
    _FgProcessorModuleCount_Type()
)
fgProcessorModuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcessorModuleCount.setStatus("current")
_FgProcessorModuleTable_Object = MibTable
fgProcessorModuleTable = _FgProcessorModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3)
)
if mibBuilder.loadTexts:
    fgProcessorModuleTable.setStatus("current")
_FgProcessorModuleEntry_Object = MibTableRow
fgProcessorModuleEntry = _FgProcessorModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1)
)
fgProcessorModuleEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgProcModIndex"),
)
if mibBuilder.loadTexts:
    fgProcessorModuleEntry.setStatus("current")
_FgProcModIndex_Type = FnIndex
_FgProcModIndex_Object = MibTableColumn
fgProcModIndex = _FgProcModIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 1),
    _FgProcModIndex_Type()
)
fgProcModIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgProcModIndex.setStatus("current")
_FgProcModType_Type = AutonomousType
_FgProcModType_Object = MibTableColumn
fgProcModType = _FgProcModType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 2),
    _FgProcModType_Type()
)
fgProcModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModType.setStatus("current")


class _FgProcModName_Type(DisplayString):
    """Custom type fgProcModName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgProcModName_Type.__name__ = "DisplayString"
_FgProcModName_Object = MibTableColumn
fgProcModName = _FgProcModName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 3),
    _FgProcModName_Type()
)
fgProcModName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModName.setStatus("current")


class _FgProcModDescr_Type(DisplayString):
    """Custom type fgProcModDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgProcModDescr_Type.__name__ = "DisplayString"
_FgProcModDescr_Object = MibTableColumn
fgProcModDescr = _FgProcModDescr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 4),
    _FgProcModDescr_Type()
)
fgProcModDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModDescr.setStatus("current")
_FgProcModProcessorCount_Type = Integer32
_FgProcModProcessorCount_Object = MibTableColumn
fgProcModProcessorCount = _FgProcModProcessorCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 5),
    _FgProcModProcessorCount_Type()
)
fgProcModProcessorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModProcessorCount.setStatus("current")
_FgProcModMemCapacity_Type = Gauge32
_FgProcModMemCapacity_Object = MibTableColumn
fgProcModMemCapacity = _FgProcModMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 6),
    _FgProcModMemCapacity_Type()
)
fgProcModMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModMemCapacity.setStatus("current")


class _FgProcModMemUsage_Type(Gauge32):
    """Custom type fgProcModMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgProcModMemUsage_Type.__name__ = "Gauge32"
_FgProcModMemUsage_Object = MibTableColumn
fgProcModMemUsage = _FgProcModMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 7),
    _FgProcModMemUsage_Type()
)
fgProcModMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModMemUsage.setStatus("current")
_FgProcModSessionCount_Type = Gauge32
_FgProcModSessionCount_Object = MibTableColumn
fgProcModSessionCount = _FgProcModSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 8),
    _FgProcModSessionCount_Type()
)
fgProcModSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModSessionCount.setStatus("current")
_FgProcModSACount_Type = Gauge32
_FgProcModSACount_Object = MibTableColumn
fgProcModSACount = _FgProcModSACount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 5, 3, 1, 9),
    _FgProcModSACount_Type()
)
fgProcModSACount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgProcModSACount.setStatus("current")
_FgSystemInfoAdvanced_ObjectIdentity = ObjectIdentity
fgSystemInfoAdvanced = _FgSystemInfoAdvanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6)
)
_FgSysInfoAdvMem_ObjectIdentity = ObjectIdentity
fgSysInfoAdvMem = _FgSysInfoAdvMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1)
)
_FgSIAdvMemPageCache_Type = Gauge32
_FgSIAdvMemPageCache_Object = MibScalar
fgSIAdvMemPageCache = _FgSIAdvMemPageCache_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 1),
    _FgSIAdvMemPageCache_Type()
)
fgSIAdvMemPageCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemPageCache.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemPageCache.setUnits("KB")
_FgSIAdvMemCacheActive_Type = Gauge32
_FgSIAdvMemCacheActive_Object = MibScalar
fgSIAdvMemCacheActive = _FgSIAdvMemCacheActive_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 2),
    _FgSIAdvMemCacheActive_Type()
)
fgSIAdvMemCacheActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemCacheActive.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemCacheActive.setUnits("KB")
_FgSIAdvMemCacheInactive_Type = Gauge32
_FgSIAdvMemCacheInactive_Object = MibScalar
fgSIAdvMemCacheInactive = _FgSIAdvMemCacheInactive_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 3),
    _FgSIAdvMemCacheInactive_Type()
)
fgSIAdvMemCacheInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemCacheInactive.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemCacheInactive.setUnits("KB")
_FgSIAdvMemBuffer_Type = Gauge32
_FgSIAdvMemBuffer_Object = MibScalar
fgSIAdvMemBuffer = _FgSIAdvMemBuffer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 4),
    _FgSIAdvMemBuffer_Type()
)
fgSIAdvMemBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemBuffer.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemBuffer.setUnits("KB")
_FgSIAdvMemEnterKerConsThrsh_Type = Gauge32
_FgSIAdvMemEnterKerConsThrsh_Object = MibScalar
fgSIAdvMemEnterKerConsThrsh = _FgSIAdvMemEnterKerConsThrsh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 5),
    _FgSIAdvMemEnterKerConsThrsh_Type()
)
fgSIAdvMemEnterKerConsThrsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemEnterKerConsThrsh.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemEnterKerConsThrsh.setUnits("KB")
_FgSIAdvMemLeaveKerConsThrsh_Type = Gauge32
_FgSIAdvMemLeaveKerConsThrsh_Object = MibScalar
fgSIAdvMemLeaveKerConsThrsh = _FgSIAdvMemLeaveKerConsThrsh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 6),
    _FgSIAdvMemLeaveKerConsThrsh_Type()
)
fgSIAdvMemLeaveKerConsThrsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemLeaveKerConsThrsh.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemLeaveKerConsThrsh.setUnits("KB")
_FgSIAdvMemEnterProxyConsThrsh_Type = Gauge32
_FgSIAdvMemEnterProxyConsThrsh_Object = MibScalar
fgSIAdvMemEnterProxyConsThrsh = _FgSIAdvMemEnterProxyConsThrsh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 7),
    _FgSIAdvMemEnterProxyConsThrsh_Type()
)
fgSIAdvMemEnterProxyConsThrsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemEnterProxyConsThrsh.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemEnterProxyConsThrsh.setUnits("KB")
_FgSIAdvMemLeaveProxyConsThrsh_Type = Gauge32
_FgSIAdvMemLeaveProxyConsThrsh_Object = MibScalar
fgSIAdvMemLeaveProxyConsThrsh = _FgSIAdvMemLeaveProxyConsThrsh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 1, 8),
    _FgSIAdvMemLeaveProxyConsThrsh_Type()
)
fgSIAdvMemLeaveProxyConsThrsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvMemLeaveProxyConsThrsh.setStatus("current")
if mibBuilder.loadTexts:
    fgSIAdvMemLeaveProxyConsThrsh.setUnits("KB")
_FgSysInfoAdvSessions_ObjectIdentity = ObjectIdentity
fgSysInfoAdvSessions = _FgSysInfoAdvSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2)
)
_FgSIAdvSesEphemeralCount_Type = Gauge32
_FgSIAdvSesEphemeralCount_Object = MibScalar
fgSIAdvSesEphemeralCount = _FgSIAdvSesEphemeralCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2, 1),
    _FgSIAdvSesEphemeralCount_Type()
)
fgSIAdvSesEphemeralCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvSesEphemeralCount.setStatus("current")
_FgSIAdvSesEphemeralLimit_Type = Gauge32
_FgSIAdvSesEphemeralLimit_Object = MibScalar
fgSIAdvSesEphemeralLimit = _FgSIAdvSesEphemeralLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2, 2),
    _FgSIAdvSesEphemeralLimit_Type()
)
fgSIAdvSesEphemeralLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvSesEphemeralLimit.setStatus("current")
_FgSIAdvSesClashCount_Type = Gauge32
_FgSIAdvSesClashCount_Object = MibScalar
fgSIAdvSesClashCount = _FgSIAdvSesClashCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2, 3),
    _FgSIAdvSesClashCount_Type()
)
fgSIAdvSesClashCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvSesClashCount.setStatus("current")
_FgSIAdvSesExpCount_Type = Gauge32
_FgSIAdvSesExpCount_Object = MibScalar
fgSIAdvSesExpCount = _FgSIAdvSesExpCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2, 4),
    _FgSIAdvSesExpCount_Type()
)
fgSIAdvSesExpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvSesExpCount.setStatus("current")
_FgSIAdvSesSyncQFCount_Type = Gauge32
_FgSIAdvSesSyncQFCount_Object = MibScalar
fgSIAdvSesSyncQFCount = _FgSIAdvSesSyncQFCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2, 5),
    _FgSIAdvSesSyncQFCount_Type()
)
fgSIAdvSesSyncQFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvSesSyncQFCount.setStatus("current")
_FgSIAdvSesAcceptQFCount_Type = Gauge32
_FgSIAdvSesAcceptQFCount_Object = MibScalar
fgSIAdvSesAcceptQFCount = _FgSIAdvSesAcceptQFCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2, 6),
    _FgSIAdvSesAcceptQFCount_Type()
)
fgSIAdvSesAcceptQFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvSesAcceptQFCount.setStatus("current")
_FgSIAdvSesNoListenerCount_Type = Gauge32
_FgSIAdvSesNoListenerCount_Object = MibScalar
fgSIAdvSesNoListenerCount = _FgSIAdvSesNoListenerCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 2, 7),
    _FgSIAdvSesNoListenerCount_Type()
)
fgSIAdvSesNoListenerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSIAdvSesNoListenerCount.setStatus("current")
_FgSIAdvLicenseDetails_ObjectIdentity = ObjectIdentity
fgSIAdvLicenseDetails = _FgSIAdvLicenseDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3)
)
_FgLicContracts_ObjectIdentity = ObjectIdentity
fgLicContracts = _FgLicContracts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 1)
)
_FgLicContractCount_Type = Integer32
_FgLicContractCount_Object = MibScalar
fgLicContractCount = _FgLicContractCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 1, 1),
    _FgLicContractCount_Type()
)
fgLicContractCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLicContractCount.setStatus("current")
_FgLicContractTable_Object = MibTable
fgLicContractTable = _FgLicContractTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 1, 2)
)
if mibBuilder.loadTexts:
    fgLicContractTable.setStatus("current")
_FgLicContractEntry_Object = MibTableRow
fgLicContractEntry = _FgLicContractEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 1, 2, 1)
)
fgLicContractEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgLicContractEntry.setStatus("current")
_FgLicContractDesc_Type = DisplayString
_FgLicContractDesc_Object = MibTableColumn
fgLicContractDesc = _FgLicContractDesc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 1, 2, 1, 1),
    _FgLicContractDesc_Type()
)
fgLicContractDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLicContractDesc.setStatus("current")
_FgLicContractExpiry_Type = DisplayString
_FgLicContractExpiry_Object = MibTableColumn
fgLicContractExpiry = _FgLicContractExpiry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 1, 2, 1, 2),
    _FgLicContractExpiry_Type()
)
fgLicContractExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLicContractExpiry.setStatus("current")
_FgLicVersions_ObjectIdentity = ObjectIdentity
fgLicVersions = _FgLicVersions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 2)
)
_FgLicVersionCount_Type = Integer32
_FgLicVersionCount_Object = MibScalar
fgLicVersionCount = _FgLicVersionCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 2, 1),
    _FgLicVersionCount_Type()
)
fgLicVersionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLicVersionCount.setStatus("current")
_FgLicVersionTable_Object = MibTable
fgLicVersionTable = _FgLicVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 2, 2)
)
if mibBuilder.loadTexts:
    fgLicVersionTable.setStatus("current")
_FgLicVersionEntry_Object = MibTableRow
fgLicVersionEntry = _FgLicVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 2, 2, 1)
)
fgLicVersionEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgLicVersionEntry.setStatus("current")
_FgLicVersionDesc_Type = DisplayString
_FgLicVersionDesc_Object = MibTableColumn
fgLicVersionDesc = _FgLicVersionDesc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 2, 2, 1, 1),
    _FgLicVersionDesc_Type()
)
fgLicVersionDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLicVersionDesc.setStatus("current")
_FgLicVersionExpiry_Type = DisplayString
_FgLicVersionExpiry_Object = MibTableColumn
fgLicVersionExpiry = _FgLicVersionExpiry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 2, 2, 1, 2),
    _FgLicVersionExpiry_Type()
)
fgLicVersionExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLicVersionExpiry.setStatus("current")
_FgLicVersionNumber_Type = DisplayString
_FgLicVersionNumber_Object = MibTableColumn
fgLicVersionNumber = _FgLicVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 2, 2, 1, 3),
    _FgLicVersionNumber_Type()
)
fgLicVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLicVersionNumber.setStatus("current")
_FgLicVersionUpdTime_Type = DisplayString
_FgLicVersionUpdTime_Object = MibTableColumn
fgLicVersionUpdTime = _FgLicVersionUpdTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 2, 2, 1, 4),
    _FgLicVersionUpdTime_Type()
)
fgLicVersionUpdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLicVersionUpdTime.setStatus("current")
_FgLicVersionUpdMethod_Type = DisplayString
_FgLicVersionUpdMethod_Object = MibTableColumn
fgLicVersionUpdMethod = _FgLicVersionUpdMethod_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 2, 2, 1, 5),
    _FgLicVersionUpdMethod_Type()
)
fgLicVersionUpdMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLicVersionUpdMethod.setStatus("current")
_FgLicVersionTryTime_Type = DisplayString
_FgLicVersionTryTime_Object = MibTableColumn
fgLicVersionTryTime = _FgLicVersionTryTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 2, 2, 1, 6),
    _FgLicVersionTryTime_Type()
)
fgLicVersionTryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLicVersionTryTime.setStatus("current")
_FgLicVersionTryResult_Type = DisplayString
_FgLicVersionTryResult_Object = MibTableColumn
fgLicVersionTryResult = _FgLicVersionTryResult_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 2, 2, 1, 7),
    _FgLicVersionTryResult_Type()
)
fgLicVersionTryResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLicVersionTryResult.setStatus("current")
_FgLicAlContracts_ObjectIdentity = ObjectIdentity
fgLicAlContracts = _FgLicAlContracts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 3)
)
_FgLicAlContractCount_Type = Integer32
_FgLicAlContractCount_Object = MibScalar
fgLicAlContractCount = _FgLicAlContractCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 3, 1),
    _FgLicAlContractCount_Type()
)
fgLicAlContractCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLicAlContractCount.setStatus("current")
_FgLicAlContractTable_Object = MibTable
fgLicAlContractTable = _FgLicAlContractTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 3, 2)
)
if mibBuilder.loadTexts:
    fgLicAlContractTable.setStatus("current")
_FgLicAlContractEntry_Object = MibTableRow
fgLicAlContractEntry = _FgLicAlContractEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 3, 2, 1)
)
fgLicAlContractEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgLicAlContractEntry.setStatus("current")
_FgLicAlContractDesc_Type = DisplayString
_FgLicAlContractDesc_Object = MibTableColumn
fgLicAlContractDesc = _FgLicAlContractDesc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 3, 2, 1, 1),
    _FgLicAlContractDesc_Type()
)
fgLicAlContractDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLicAlContractDesc.setStatus("current")
_FgLicAlContractExpiry_Type = DisplayString
_FgLicAlContractExpiry_Object = MibTableColumn
fgLicAlContractExpiry = _FgLicAlContractExpiry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 6, 3, 3, 2, 1, 2),
    _FgLicAlContractExpiry_Type()
)
fgLicAlContractExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLicAlContractExpiry.setStatus("current")
_FgUsbports_ObjectIdentity = ObjectIdentity
fgUsbports = _FgUsbports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7)
)
_FgUsbportCount_Type = Integer32
_FgUsbportCount_Object = MibScalar
fgUsbportCount = _FgUsbportCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 1),
    _FgUsbportCount_Type()
)
fgUsbportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportCount.setStatus("current")
_FgUsbportTable_Object = MibTable
fgUsbportTable = _FgUsbportTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2)
)
if mibBuilder.loadTexts:
    fgUsbportTable.setStatus("current")
_FgUsbportEntry_Object = MibTableRow
fgUsbportEntry = _FgUsbportEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1)
)
fgUsbportEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgUsbportEntIndex"),
)
if mibBuilder.loadTexts:
    fgUsbportEntry.setStatus("current")
_FgUsbportEntIndex_Type = FnIndex
_FgUsbportEntIndex_Object = MibTableColumn
fgUsbportEntIndex = _FgUsbportEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 1),
    _FgUsbportEntIndex_Type()
)
fgUsbportEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgUsbportEntIndex.setStatus("current")


class _FgUsbportPlugged_Type(Integer32):
    """Custom type fgUsbportPlugged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unplugged", 0),
          ("plugged", 1))
    )


_FgUsbportPlugged_Type.__name__ = "Integer32"
_FgUsbportPlugged_Object = MibTableColumn
fgUsbportPlugged = _FgUsbportPlugged_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 2),
    _FgUsbportPlugged_Type()
)
fgUsbportPlugged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportPlugged.setStatus("current")
_FgUsbportVersion_Type = DisplayString
_FgUsbportVersion_Object = MibTableColumn
fgUsbportVersion = _FgUsbportVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 3),
    _FgUsbportVersion_Type()
)
fgUsbportVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportVersion.setStatus("current")


class _FgUsbportClass_Type(Integer32):
    """Custom type fgUsbportClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              13,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ifc", 0),
          ("audio", 1),
          ("comm", 2),
          ("hid", 3),
          ("physical", 5),
          ("image", 6),
          ("printer", 7),
          ("storage", 8),
          ("hub", 9),
          ("cdcData", 10),
          ("chipSmartCard", 11),
          ("contentSecurity", 13),
          ("appSpec", 254),
          ("vendorSpec", 255))
    )


_FgUsbportClass_Type.__name__ = "Integer32"
_FgUsbportClass_Object = MibTableColumn
fgUsbportClass = _FgUsbportClass_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 4),
    _FgUsbportClass_Type()
)
fgUsbportClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportClass.setStatus("current")
_FgUsbportVendId_Type = OctetString
_FgUsbportVendId_Object = MibTableColumn
fgUsbportVendId = _FgUsbportVendId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 5),
    _FgUsbportVendId_Type()
)
fgUsbportVendId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportVendId.setStatus("current")
_FgUsbportProdId_Type = OctetString
_FgUsbportProdId_Object = MibTableColumn
fgUsbportProdId = _FgUsbportProdId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 6),
    _FgUsbportProdId_Type()
)
fgUsbportProdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportProdId.setStatus("current")
_FgUsbportRevision_Type = DisplayString
_FgUsbportRevision_Object = MibTableColumn
fgUsbportRevision = _FgUsbportRevision_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 7),
    _FgUsbportRevision_Type()
)
fgUsbportRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportRevision.setStatus("current")
_FgUsbportManufacturer_Type = DisplayString
_FgUsbportManufacturer_Object = MibTableColumn
fgUsbportManufacturer = _FgUsbportManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 8),
    _FgUsbportManufacturer_Type()
)
fgUsbportManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportManufacturer.setStatus("current")
_FgUsbportProduct_Type = DisplayString
_FgUsbportProduct_Object = MibTableColumn
fgUsbportProduct = _FgUsbportProduct_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 9),
    _FgUsbportProduct_Type()
)
fgUsbportProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportProduct.setStatus("current")
_FgUsbportSerial_Type = DisplayString
_FgUsbportSerial_Object = MibTableColumn
fgUsbportSerial = _FgUsbportSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 7, 2, 1, 10),
    _FgUsbportSerial_Type()
)
fgUsbportSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbportSerial.setStatus("current")
_FgLinkMonitor_ObjectIdentity = ObjectIdentity
fgLinkMonitor = _FgLinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8)
)
_FgLinkMonitorNumber_Type = Integer32
_FgLinkMonitorNumber_Object = MibScalar
fgLinkMonitorNumber = _FgLinkMonitorNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 1),
    _FgLinkMonitorNumber_Type()
)
fgLinkMonitorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorNumber.setStatus("current")
_FgLinkMonitorTable_Object = MibTable
fgLinkMonitorTable = _FgLinkMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2)
)
if mibBuilder.loadTexts:
    fgLinkMonitorTable.setStatus("current")
_FgLinkMonitorEntry_Object = MibTableRow
fgLinkMonitorEntry = _FgLinkMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1)
)
fgLinkMonitorEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgLinkMonitorID"),
)
if mibBuilder.loadTexts:
    fgLinkMonitorEntry.setStatus("current")
_FgLinkMonitorID_Type = FnIndex
_FgLinkMonitorID_Object = MibTableColumn
fgLinkMonitorID = _FgLinkMonitorID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 1),
    _FgLinkMonitorID_Type()
)
fgLinkMonitorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgLinkMonitorID.setStatus("current")
_FgLinkMonitorName_Type = DisplayString
_FgLinkMonitorName_Object = MibTableColumn
fgLinkMonitorName = _FgLinkMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 2),
    _FgLinkMonitorName_Type()
)
fgLinkMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorName.setStatus("current")


class _FgLinkMonitorState_Type(Integer32):
    """Custom type fgLinkMonitorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alive", 0),
          ("dead", 1))
    )


_FgLinkMonitorState_Type.__name__ = "Integer32"
_FgLinkMonitorState_Object = MibTableColumn
fgLinkMonitorState = _FgLinkMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 3),
    _FgLinkMonitorState_Type()
)
fgLinkMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorState.setStatus("current")
_FgLinkMonitorLatency_Type = DisplayString
_FgLinkMonitorLatency_Object = MibTableColumn
fgLinkMonitorLatency = _FgLinkMonitorLatency_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 4),
    _FgLinkMonitorLatency_Type()
)
fgLinkMonitorLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorLatency.setStatus("current")
_FgLinkMonitorJitter_Type = DisplayString
_FgLinkMonitorJitter_Object = MibTableColumn
fgLinkMonitorJitter = _FgLinkMonitorJitter_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 5),
    _FgLinkMonitorJitter_Type()
)
fgLinkMonitorJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorJitter.setStatus("current")
_FgLinkMonitorPacketSend_Type = Counter64
_FgLinkMonitorPacketSend_Object = MibTableColumn
fgLinkMonitorPacketSend = _FgLinkMonitorPacketSend_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 6),
    _FgLinkMonitorPacketSend_Type()
)
fgLinkMonitorPacketSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorPacketSend.setStatus("current")
_FgLinkMonitorPacketRecv_Type = Counter64
_FgLinkMonitorPacketRecv_Object = MibTableColumn
fgLinkMonitorPacketRecv = _FgLinkMonitorPacketRecv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 7),
    _FgLinkMonitorPacketRecv_Type()
)
fgLinkMonitorPacketRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorPacketRecv.setStatus("current")
_FgLinkMonitorPacketLoss_Type = DisplayString
_FgLinkMonitorPacketLoss_Object = MibTableColumn
fgLinkMonitorPacketLoss = _FgLinkMonitorPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 8),
    _FgLinkMonitorPacketLoss_Type()
)
fgLinkMonitorPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorPacketLoss.setStatus("current")
_FgLinkMonitorVdom_Type = DisplayString
_FgLinkMonitorVdom_Object = MibTableColumn
fgLinkMonitorVdom = _FgLinkMonitorVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 9),
    _FgLinkMonitorVdom_Type()
)
fgLinkMonitorVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorVdom.setStatus("current")
_FgLinkMonitorBandwidthIn_Type = Counter32
_FgLinkMonitorBandwidthIn_Object = MibTableColumn
fgLinkMonitorBandwidthIn = _FgLinkMonitorBandwidthIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 10),
    _FgLinkMonitorBandwidthIn_Type()
)
fgLinkMonitorBandwidthIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorBandwidthIn.setStatus("current")
_FgLinkMonitorBandwidthOut_Type = Counter32
_FgLinkMonitorBandwidthOut_Object = MibTableColumn
fgLinkMonitorBandwidthOut = _FgLinkMonitorBandwidthOut_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 11),
    _FgLinkMonitorBandwidthOut_Type()
)
fgLinkMonitorBandwidthOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorBandwidthOut.setStatus("current")
_FgLinkMonitorBandwidthBi_Type = Counter32
_FgLinkMonitorBandwidthBi_Object = MibTableColumn
fgLinkMonitorBandwidthBi = _FgLinkMonitorBandwidthBi_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 12),
    _FgLinkMonitorBandwidthBi_Type()
)
fgLinkMonitorBandwidthBi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorBandwidthBi.setStatus("current")
_FgLinkMonitorOutofSeq_Type = Counter64
_FgLinkMonitorOutofSeq_Object = MibTableColumn
fgLinkMonitorOutofSeq = _FgLinkMonitorOutofSeq_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 13),
    _FgLinkMonitorOutofSeq_Type()
)
fgLinkMonitorOutofSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorOutofSeq.setStatus("current")
_FgLinkMonitorServer_Type = DisplayString
_FgLinkMonitorServer_Object = MibTableColumn
fgLinkMonitorServer = _FgLinkMonitorServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 14),
    _FgLinkMonitorServer_Type()
)
fgLinkMonitorServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorServer.setStatus("current")
_FgLinkMonitorProtocol_Type = DisplayString
_FgLinkMonitorProtocol_Object = MibTableColumn
fgLinkMonitorProtocol = _FgLinkMonitorProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 8, 2, 1, 15),
    _FgLinkMonitorProtocol_Type()
)
fgLinkMonitorProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLinkMonitorProtocol.setStatus("current")
_FgVWLHealthCheckLink_ObjectIdentity = ObjectIdentity
fgVWLHealthCheckLink = _FgVWLHealthCheckLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9)
)
_FgVWLHealthCheckLinkNumber_Type = Integer32
_FgVWLHealthCheckLinkNumber_Object = MibScalar
fgVWLHealthCheckLinkNumber = _FgVWLHealthCheckLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 1),
    _FgVWLHealthCheckLinkNumber_Type()
)
fgVWLHealthCheckLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkNumber.setStatus("current")
_FgVWLHealthCheckLinkTable_Object = MibTable
fgVWLHealthCheckLinkTable = _FgVWLHealthCheckLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2)
)
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkTable.setStatus("current")
_FgVWLHealthCheckLinkEntry_Object = MibTableRow
fgVWLHealthCheckLinkEntry = _FgVWLHealthCheckLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1)
)
fgVWLHealthCheckLinkEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkID"),
)
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkEntry.setStatus("current")
_FgVWLHealthCheckLinkID_Type = FnIndex
_FgVWLHealthCheckLinkID_Object = MibTableColumn
fgVWLHealthCheckLinkID = _FgVWLHealthCheckLinkID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 1),
    _FgVWLHealthCheckLinkID_Type()
)
fgVWLHealthCheckLinkID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkID.setStatus("current")
_FgVWLHealthCheckLinkName_Type = DisplayString
_FgVWLHealthCheckLinkName_Object = MibTableColumn
fgVWLHealthCheckLinkName = _FgVWLHealthCheckLinkName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 2),
    _FgVWLHealthCheckLinkName_Type()
)
fgVWLHealthCheckLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkName.setStatus("current")


class _FgVWLHealthCheckLinkSeq_Type(Gauge32):
    """Custom type fgVWLHealthCheckLinkSeq based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FgVWLHealthCheckLinkSeq_Type.__name__ = "Gauge32"
_FgVWLHealthCheckLinkSeq_Object = MibTableColumn
fgVWLHealthCheckLinkSeq = _FgVWLHealthCheckLinkSeq_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 3),
    _FgVWLHealthCheckLinkSeq_Type()
)
fgVWLHealthCheckLinkSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkSeq.setStatus("current")


class _FgVWLHealthCheckLinkState_Type(Integer32):
    """Custom type fgVWLHealthCheckLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alive", 0),
          ("dead", 1))
    )


_FgVWLHealthCheckLinkState_Type.__name__ = "Integer32"
_FgVWLHealthCheckLinkState_Object = MibTableColumn
fgVWLHealthCheckLinkState = _FgVWLHealthCheckLinkState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 4),
    _FgVWLHealthCheckLinkState_Type()
)
fgVWLHealthCheckLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkState.setStatus("current")
_FgVWLHealthCheckLinkLatency_Type = DisplayString
_FgVWLHealthCheckLinkLatency_Object = MibTableColumn
fgVWLHealthCheckLinkLatency = _FgVWLHealthCheckLinkLatency_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 5),
    _FgVWLHealthCheckLinkLatency_Type()
)
fgVWLHealthCheckLinkLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkLatency.setStatus("current")
_FgVWLHealthCheckLinkJitter_Type = DisplayString
_FgVWLHealthCheckLinkJitter_Object = MibTableColumn
fgVWLHealthCheckLinkJitter = _FgVWLHealthCheckLinkJitter_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 6),
    _FgVWLHealthCheckLinkJitter_Type()
)
fgVWLHealthCheckLinkJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkJitter.setStatus("current")
_FgVWLHealthCheckLinkPacketSend_Type = Counter64
_FgVWLHealthCheckLinkPacketSend_Object = MibTableColumn
fgVWLHealthCheckLinkPacketSend = _FgVWLHealthCheckLinkPacketSend_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 7),
    _FgVWLHealthCheckLinkPacketSend_Type()
)
fgVWLHealthCheckLinkPacketSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkPacketSend.setStatus("current")
_FgVWLHealthCheckLinkPacketRecv_Type = Counter64
_FgVWLHealthCheckLinkPacketRecv_Object = MibTableColumn
fgVWLHealthCheckLinkPacketRecv = _FgVWLHealthCheckLinkPacketRecv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 8),
    _FgVWLHealthCheckLinkPacketRecv_Type()
)
fgVWLHealthCheckLinkPacketRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkPacketRecv.setStatus("current")
_FgVWLHealthCheckLinkPacketLoss_Type = DisplayString
_FgVWLHealthCheckLinkPacketLoss_Object = MibTableColumn
fgVWLHealthCheckLinkPacketLoss = _FgVWLHealthCheckLinkPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 9),
    _FgVWLHealthCheckLinkPacketLoss_Type()
)
fgVWLHealthCheckLinkPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkPacketLoss.setStatus("current")
_FgVWLHealthCheckLinkVdom_Type = DisplayString
_FgVWLHealthCheckLinkVdom_Object = MibTableColumn
fgVWLHealthCheckLinkVdom = _FgVWLHealthCheckLinkVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 10),
    _FgVWLHealthCheckLinkVdom_Type()
)
fgVWLHealthCheckLinkVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkVdom.setStatus("current")
_FgVWLHealthCheckLinkBandwidthIn_Type = Counter32
_FgVWLHealthCheckLinkBandwidthIn_Object = MibTableColumn
fgVWLHealthCheckLinkBandwidthIn = _FgVWLHealthCheckLinkBandwidthIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 11),
    _FgVWLHealthCheckLinkBandwidthIn_Type()
)
fgVWLHealthCheckLinkBandwidthIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkBandwidthIn.setStatus("current")
_FgVWLHealthCheckLinkBandwidthOut_Type = Counter32
_FgVWLHealthCheckLinkBandwidthOut_Object = MibTableColumn
fgVWLHealthCheckLinkBandwidthOut = _FgVWLHealthCheckLinkBandwidthOut_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 12),
    _FgVWLHealthCheckLinkBandwidthOut_Type()
)
fgVWLHealthCheckLinkBandwidthOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkBandwidthOut.setStatus("current")
_FgVWLHealthCheckLinkBandwidthBi_Type = Counter32
_FgVWLHealthCheckLinkBandwidthBi_Object = MibTableColumn
fgVWLHealthCheckLinkBandwidthBi = _FgVWLHealthCheckLinkBandwidthBi_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 13),
    _FgVWLHealthCheckLinkBandwidthBi_Type()
)
fgVWLHealthCheckLinkBandwidthBi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkBandwidthBi.setStatus("current")
_FgVWLHealthCheckLinkIfName_Type = DisplayString
_FgVWLHealthCheckLinkIfName_Object = MibTableColumn
fgVWLHealthCheckLinkIfName = _FgVWLHealthCheckLinkIfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 14),
    _FgVWLHealthCheckLinkIfName_Type()
)
fgVWLHealthCheckLinkIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkIfName.setStatus("current")
_FgVWLHealthCheckLinkUsedBandwidthIn_Type = Counter32
_FgVWLHealthCheckLinkUsedBandwidthIn_Object = MibTableColumn
fgVWLHealthCheckLinkUsedBandwidthIn = _FgVWLHealthCheckLinkUsedBandwidthIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 15),
    _FgVWLHealthCheckLinkUsedBandwidthIn_Type()
)
fgVWLHealthCheckLinkUsedBandwidthIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkUsedBandwidthIn.setStatus("current")
_FgVWLHealthCheckLinkUsedBandwidthOut_Type = Counter32
_FgVWLHealthCheckLinkUsedBandwidthOut_Object = MibTableColumn
fgVWLHealthCheckLinkUsedBandwidthOut = _FgVWLHealthCheckLinkUsedBandwidthOut_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 16),
    _FgVWLHealthCheckLinkUsedBandwidthOut_Type()
)
fgVWLHealthCheckLinkUsedBandwidthOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkUsedBandwidthOut.setStatus("current")
_FgVWLHealthCheckLinkUsedBandwidthBi_Type = Counter32
_FgVWLHealthCheckLinkUsedBandwidthBi_Object = MibTableColumn
fgVWLHealthCheckLinkUsedBandwidthBi = _FgVWLHealthCheckLinkUsedBandwidthBi_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 17),
    _FgVWLHealthCheckLinkUsedBandwidthBi_Type()
)
fgVWLHealthCheckLinkUsedBandwidthBi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkUsedBandwidthBi.setStatus("current")
_FgVWLHealthCheckLinkMOSCodec_Type = DisplayString
_FgVWLHealthCheckLinkMOSCodec_Object = MibTableColumn
fgVWLHealthCheckLinkMOSCodec = _FgVWLHealthCheckLinkMOSCodec_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 18),
    _FgVWLHealthCheckLinkMOSCodec_Type()
)
fgVWLHealthCheckLinkMOSCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkMOSCodec.setStatus("current")
_FgVWLHealthCheckLinkMOS_Type = DisplayString
_FgVWLHealthCheckLinkMOS_Object = MibTableColumn
fgVWLHealthCheckLinkMOS = _FgVWLHealthCheckLinkMOS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 9, 2, 1, 19),
    _FgVWLHealthCheckLinkMOS_Type()
)
fgVWLHealthCheckLinkMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkMOS.setStatus("current")
_FgDisks_ObjectIdentity = ObjectIdentity
fgDisks = _FgDisks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10)
)
_FgDiskCount_Type = Integer32
_FgDiskCount_Object = MibScalar
fgDiskCount = _FgDiskCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 1),
    _FgDiskCount_Type()
)
fgDiskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDiskCount.setStatus("current")
_FgDiskTable_Object = MibTable
fgDiskTable = _FgDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 2)
)
if mibBuilder.loadTexts:
    fgDiskTable.setStatus("current")
_FgDiskEntry_Object = MibTableRow
fgDiskEntry = _FgDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 2, 1)
)
fgDiskEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgDiskIndex"),
)
if mibBuilder.loadTexts:
    fgDiskEntry.setStatus("current")
_FgDiskIndex_Type = FnIndex
_FgDiskIndex_Object = MibTableColumn
fgDiskIndex = _FgDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 2, 1, 1),
    _FgDiskIndex_Type()
)
fgDiskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgDiskIndex.setStatus("current")
_FgDiskName_Type = DisplayString
_FgDiskName_Object = MibTableColumn
fgDiskName = _FgDiskName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 2, 1, 2),
    _FgDiskName_Type()
)
fgDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDiskName.setStatus("current")
_FgDiskFsMountsTable_Object = MibTable
fgDiskFsMountsTable = _FgDiskFsMountsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 3)
)
if mibBuilder.loadTexts:
    fgDiskFsMountsTable.setStatus("current")
_FgDiskFsMountsEntry_Object = MibTableRow
fgDiskFsMountsEntry = _FgDiskFsMountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 3, 1)
)
fgDiskFsMountsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgDiskFsMountDevIdx"),
)
if mibBuilder.loadTexts:
    fgDiskFsMountsEntry.setStatus("current")
_FgDiskFsMountDevIdx_Type = FnIndex
_FgDiskFsMountDevIdx_Object = MibTableColumn
fgDiskFsMountDevIdx = _FgDiskFsMountDevIdx_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 3, 1, 1),
    _FgDiskFsMountDevIdx_Type()
)
fgDiskFsMountDevIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgDiskFsMountDevIdx.setStatus("current")
_FgDiskFsMountName_Type = DisplayString
_FgDiskFsMountName_Object = MibTableColumn
fgDiskFsMountName = _FgDiskFsMountName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 3, 1, 2),
    _FgDiskFsMountName_Type()
)
fgDiskFsMountName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDiskFsMountName.setStatus("current")
_FgDiskFsMountMountPoint_Type = DisplayString
_FgDiskFsMountMountPoint_Object = MibTableColumn
fgDiskFsMountMountPoint = _FgDiskFsMountMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 3, 1, 3),
    _FgDiskFsMountMountPoint_Type()
)
fgDiskFsMountMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDiskFsMountMountPoint.setStatus("current")
_FgDiskFsMountType_Type = DisplayString
_FgDiskFsMountType_Object = MibTableColumn
fgDiskFsMountType = _FgDiskFsMountType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 3, 1, 4),
    _FgDiskFsMountType_Type()
)
fgDiskFsMountType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDiskFsMountType.setStatus("current")
_FgDiskFsMountOptions_Type = DisplayString
_FgDiskFsMountOptions_Object = MibTableColumn
fgDiskFsMountOptions = _FgDiskFsMountOptions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 3, 1, 5),
    _FgDiskFsMountOptions_Type()
)
fgDiskFsMountOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDiskFsMountOptions.setStatus("current")
_FgDiskFsMountFreq_Type = Integer32
_FgDiskFsMountFreq_Object = MibTableColumn
fgDiskFsMountFreq = _FgDiskFsMountFreq_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 3, 1, 6),
    _FgDiskFsMountFreq_Type()
)
fgDiskFsMountFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDiskFsMountFreq.setStatus("current")
_FgDiskFsMountPassNo_Type = Integer32
_FgDiskFsMountPassNo_Object = MibTableColumn
fgDiskFsMountPassNo = _FgDiskFsMountPassNo_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 3, 1, 7),
    _FgDiskFsMountPassNo_Type()
)
fgDiskFsMountPassNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDiskFsMountPassNo.setStatus("current")
_FgDiskFsMountOptionsVal_Type = Unsigned32
_FgDiskFsMountOptionsVal_Object = MibTableColumn
fgDiskFsMountOptionsVal = _FgDiskFsMountOptionsVal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 3, 1, 8),
    _FgDiskFsMountOptionsVal_Type()
)
fgDiskFsMountOptionsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDiskFsMountOptionsVal.setStatus("current")
_FgDiskPartitionsTable_Object = MibTable
fgDiskPartitionsTable = _FgDiskPartitionsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 4)
)
if mibBuilder.loadTexts:
    fgDiskPartitionsTable.setStatus("current")
_FgDiskPartitionsEntry_Object = MibTableRow
fgDiskPartitionsEntry = _FgDiskPartitionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 4, 1)
)
fgDiskPartitionsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgDiskPartitionIdx"),
)
if mibBuilder.loadTexts:
    fgDiskPartitionsEntry.setStatus("current")
_FgDiskPartitionIdx_Type = FnIndex
_FgDiskPartitionIdx_Object = MibTableColumn
fgDiskPartitionIdx = _FgDiskPartitionIdx_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 4, 1, 1),
    _FgDiskPartitionIdx_Type()
)
fgDiskPartitionIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgDiskPartitionIdx.setStatus("current")
_FgDiskPartitionsMajor_Type = Integer32
_FgDiskPartitionsMajor_Object = MibTableColumn
fgDiskPartitionsMajor = _FgDiskPartitionsMajor_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 4, 1, 2),
    _FgDiskPartitionsMajor_Type()
)
fgDiskPartitionsMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDiskPartitionsMajor.setStatus("current")
_FgDiskPartitionsMinor_Type = Integer32
_FgDiskPartitionsMinor_Object = MibTableColumn
fgDiskPartitionsMinor = _FgDiskPartitionsMinor_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 4, 1, 3),
    _FgDiskPartitionsMinor_Type()
)
fgDiskPartitionsMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDiskPartitionsMinor.setStatus("current")
_FgDiskPartitionsBlockNum_Type = Integer32
_FgDiskPartitionsBlockNum_Object = MibTableColumn
fgDiskPartitionsBlockNum = _FgDiskPartitionsBlockNum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 4, 1, 4),
    _FgDiskPartitionsBlockNum_Type()
)
fgDiskPartitionsBlockNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDiskPartitionsBlockNum.setStatus("current")
_FgDiskPartitionsName_Type = DisplayString
_FgDiskPartitionsName_Object = MibTableColumn
fgDiskPartitionsName = _FgDiskPartitionsName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 10, 4, 1, 5),
    _FgDiskPartitionsName_Type()
)
fgDiskPartitionsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDiskPartitionsName.setStatus("current")
_FgSlaProbeClient_ObjectIdentity = ObjectIdentity
fgSlaProbeClient = _FgSlaProbeClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11)
)
_FgSlaProbeClientNumber_Type = Integer32
_FgSlaProbeClientNumber_Object = MibScalar
fgSlaProbeClientNumber = _FgSlaProbeClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 1),
    _FgSlaProbeClientNumber_Type()
)
fgSlaProbeClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientNumber.setStatus("current")
_FgSlaProbeClientTable_Object = MibTable
fgSlaProbeClientTable = _FgSlaProbeClientTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2)
)
if mibBuilder.loadTexts:
    fgSlaProbeClientTable.setStatus("current")
_FgSlaProbeClientEntry_Object = MibTableRow
fgSlaProbeClientEntry = _FgSlaProbeClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1)
)
fgSlaProbeClientEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgSlaProbeClientID"),
)
if mibBuilder.loadTexts:
    fgSlaProbeClientEntry.setStatus("current")
_FgSlaProbeClientID_Type = FnIndex
_FgSlaProbeClientID_Object = MibTableColumn
fgSlaProbeClientID = _FgSlaProbeClientID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 1),
    _FgSlaProbeClientID_Type()
)
fgSlaProbeClientID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgSlaProbeClientID.setStatus("current")
_FgSlaProbeClientIP_Type = IpAddress
_FgSlaProbeClientIP_Object = MibTableColumn
fgSlaProbeClientIP = _FgSlaProbeClientIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 2),
    _FgSlaProbeClientIP_Type()
)
fgSlaProbeClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientIP.setStatus("current")


class _FgSlaProbeClientState_Type(Integer32):
    """Custom type fgSlaProbeClientState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alive", 0),
          ("dead", 1))
    )


_FgSlaProbeClientState_Type.__name__ = "Integer32"
_FgSlaProbeClientState_Object = MibTableColumn
fgSlaProbeClientState = _FgSlaProbeClientState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 3),
    _FgSlaProbeClientState_Type()
)
fgSlaProbeClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientState.setStatus("current")
_FgSlaProbeClientAvgLatency_Type = DisplayString
_FgSlaProbeClientAvgLatency_Object = MibTableColumn
fgSlaProbeClientAvgLatency = _FgSlaProbeClientAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 4),
    _FgSlaProbeClientAvgLatency_Type()
)
fgSlaProbeClientAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientAvgLatency.setStatus("current")
_FgSlaProbeClientAvgLatencySD_Type = DisplayString
_FgSlaProbeClientAvgLatencySD_Object = MibTableColumn
fgSlaProbeClientAvgLatencySD = _FgSlaProbeClientAvgLatencySD_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 5),
    _FgSlaProbeClientAvgLatencySD_Type()
)
fgSlaProbeClientAvgLatencySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientAvgLatencySD.setStatus("current")
_FgSlaProbeClientAvgLatencyDS_Type = DisplayString
_FgSlaProbeClientAvgLatencyDS_Object = MibTableColumn
fgSlaProbeClientAvgLatencyDS = _FgSlaProbeClientAvgLatencyDS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 6),
    _FgSlaProbeClientAvgLatencyDS_Type()
)
fgSlaProbeClientAvgLatencyDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientAvgLatencyDS.setStatus("current")
_FgSlaProbeClientMinLatency_Type = DisplayString
_FgSlaProbeClientMinLatency_Object = MibTableColumn
fgSlaProbeClientMinLatency = _FgSlaProbeClientMinLatency_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 7),
    _FgSlaProbeClientMinLatency_Type()
)
fgSlaProbeClientMinLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientMinLatency.setStatus("current")
_FgSlaProbeClientMinLatencySD_Type = DisplayString
_FgSlaProbeClientMinLatencySD_Object = MibTableColumn
fgSlaProbeClientMinLatencySD = _FgSlaProbeClientMinLatencySD_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 8),
    _FgSlaProbeClientMinLatencySD_Type()
)
fgSlaProbeClientMinLatencySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientMinLatencySD.setStatus("current")
_FgSlaProbeClientMinLatencyDS_Type = DisplayString
_FgSlaProbeClientMinLatencyDS_Object = MibTableColumn
fgSlaProbeClientMinLatencyDS = _FgSlaProbeClientMinLatencyDS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 9),
    _FgSlaProbeClientMinLatencyDS_Type()
)
fgSlaProbeClientMinLatencyDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientMinLatencyDS.setStatus("current")
_FgSlaProbeClientMaxLatency_Type = DisplayString
_FgSlaProbeClientMaxLatency_Object = MibTableColumn
fgSlaProbeClientMaxLatency = _FgSlaProbeClientMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 10),
    _FgSlaProbeClientMaxLatency_Type()
)
fgSlaProbeClientMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientMaxLatency.setStatus("current")
_FgSlaProbeClientMaxLatencySD_Type = DisplayString
_FgSlaProbeClientMaxLatencySD_Object = MibTableColumn
fgSlaProbeClientMaxLatencySD = _FgSlaProbeClientMaxLatencySD_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 11),
    _FgSlaProbeClientMaxLatencySD_Type()
)
fgSlaProbeClientMaxLatencySD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientMaxLatencySD.setStatus("current")
_FgSlaProbeClientMaxLatencyDS_Type = DisplayString
_FgSlaProbeClientMaxLatencyDS_Object = MibTableColumn
fgSlaProbeClientMaxLatencyDS = _FgSlaProbeClientMaxLatencyDS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 12),
    _FgSlaProbeClientMaxLatencyDS_Type()
)
fgSlaProbeClientMaxLatencyDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientMaxLatencyDS.setStatus("current")
_FgSlaProbeClientAvgJitter_Type = DisplayString
_FgSlaProbeClientAvgJitter_Object = MibTableColumn
fgSlaProbeClientAvgJitter = _FgSlaProbeClientAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 13),
    _FgSlaProbeClientAvgJitter_Type()
)
fgSlaProbeClientAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientAvgJitter.setStatus("current")
_FgSlaProbeClientAvgJitterSD_Type = DisplayString
_FgSlaProbeClientAvgJitterSD_Object = MibTableColumn
fgSlaProbeClientAvgJitterSD = _FgSlaProbeClientAvgJitterSD_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 14),
    _FgSlaProbeClientAvgJitterSD_Type()
)
fgSlaProbeClientAvgJitterSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientAvgJitterSD.setStatus("current")
_FgSlaProbeClientAvgJitterDS_Type = DisplayString
_FgSlaProbeClientAvgJitterDS_Object = MibTableColumn
fgSlaProbeClientAvgJitterDS = _FgSlaProbeClientAvgJitterDS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 15),
    _FgSlaProbeClientAvgJitterDS_Type()
)
fgSlaProbeClientAvgJitterDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientAvgJitterDS.setStatus("current")
_FgSlaProbeClientMinJitter_Type = DisplayString
_FgSlaProbeClientMinJitter_Object = MibTableColumn
fgSlaProbeClientMinJitter = _FgSlaProbeClientMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 16),
    _FgSlaProbeClientMinJitter_Type()
)
fgSlaProbeClientMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientMinJitter.setStatus("current")
_FgSlaProbeClientMinJitterSD_Type = DisplayString
_FgSlaProbeClientMinJitterSD_Object = MibTableColumn
fgSlaProbeClientMinJitterSD = _FgSlaProbeClientMinJitterSD_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 17),
    _FgSlaProbeClientMinJitterSD_Type()
)
fgSlaProbeClientMinJitterSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientMinJitterSD.setStatus("current")
_FgSlaProbeClientMinJitterDS_Type = DisplayString
_FgSlaProbeClientMinJitterDS_Object = MibTableColumn
fgSlaProbeClientMinJitterDS = _FgSlaProbeClientMinJitterDS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 18),
    _FgSlaProbeClientMinJitterDS_Type()
)
fgSlaProbeClientMinJitterDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientMinJitterDS.setStatus("current")
_FgSlaProbeClientMaxJitter_Type = DisplayString
_FgSlaProbeClientMaxJitter_Object = MibTableColumn
fgSlaProbeClientMaxJitter = _FgSlaProbeClientMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 19),
    _FgSlaProbeClientMaxJitter_Type()
)
fgSlaProbeClientMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientMaxJitter.setStatus("current")
_FgSlaProbeClientMaxJitterSD_Type = DisplayString
_FgSlaProbeClientMaxJitterSD_Object = MibTableColumn
fgSlaProbeClientMaxJitterSD = _FgSlaProbeClientMaxJitterSD_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 20),
    _FgSlaProbeClientMaxJitterSD_Type()
)
fgSlaProbeClientMaxJitterSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientMaxJitterSD.setStatus("current")
_FgSlaProbeClientMaxJitterDS_Type = DisplayString
_FgSlaProbeClientMaxJitterDS_Object = MibTableColumn
fgSlaProbeClientMaxJitterDS = _FgSlaProbeClientMaxJitterDS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 21),
    _FgSlaProbeClientMaxJitterDS_Type()
)
fgSlaProbeClientMaxJitterDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientMaxJitterDS.setStatus("current")
_FgSlaProbeClientPktloss_Type = DisplayString
_FgSlaProbeClientPktloss_Object = MibTableColumn
fgSlaProbeClientPktloss = _FgSlaProbeClientPktloss_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 22),
    _FgSlaProbeClientPktloss_Type()
)
fgSlaProbeClientPktloss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientPktloss.setStatus("current")
_FgSlaProbeClientPktlossSD_Type = DisplayString
_FgSlaProbeClientPktlossSD_Object = MibTableColumn
fgSlaProbeClientPktlossSD = _FgSlaProbeClientPktlossSD_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 23),
    _FgSlaProbeClientPktlossSD_Type()
)
fgSlaProbeClientPktlossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientPktlossSD.setStatus("current")
_FgSlaProbeClientPktlossDS_Type = DisplayString
_FgSlaProbeClientPktlossDS_Object = MibTableColumn
fgSlaProbeClientPktlossDS = _FgSlaProbeClientPktlossDS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 24),
    _FgSlaProbeClientPktlossDS_Type()
)
fgSlaProbeClientPktlossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientPktlossDS.setStatus("current")
_FgSlaProbeClientOutofSeq_Type = Counter64
_FgSlaProbeClientOutofSeq_Object = MibTableColumn
fgSlaProbeClientOutofSeq = _FgSlaProbeClientOutofSeq_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 25),
    _FgSlaProbeClientOutofSeq_Type()
)
fgSlaProbeClientOutofSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientOutofSeq.setStatus("current")
_FgSlaProbeClientOutofSeqSD_Type = Counter64
_FgSlaProbeClientOutofSeqSD_Object = MibTableColumn
fgSlaProbeClientOutofSeqSD = _FgSlaProbeClientOutofSeqSD_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 26),
    _FgSlaProbeClientOutofSeqSD_Type()
)
fgSlaProbeClientOutofSeqSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientOutofSeqSD.setStatus("current")
_FgSlaProbeClientOutofSeqDS_Type = Counter64
_FgSlaProbeClientOutofSeqDS_Object = MibTableColumn
fgSlaProbeClientOutofSeqDS = _FgSlaProbeClientOutofSeqDS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 11, 2, 1, 27),
    _FgSlaProbeClientOutofSeqDS_Type()
)
fgSlaProbeClientOutofSeqDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSlaProbeClientOutofSeqDS.setStatus("current")
_FgDpdkEngs_ObjectIdentity = ObjectIdentity
fgDpdkEngs = _FgDpdkEngs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 12)
)
_FgDpdkEngCount_Type = Integer32
_FgDpdkEngCount_Object = MibScalar
fgDpdkEngCount = _FgDpdkEngCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 12, 1),
    _FgDpdkEngCount_Type()
)
fgDpdkEngCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDpdkEngCount.setStatus("current")
_FgDpdkEngTable_Object = MibTable
fgDpdkEngTable = _FgDpdkEngTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 12, 2)
)
if mibBuilder.loadTexts:
    fgDpdkEngTable.setStatus("current")
_FgDpdkEngEntry_Object = MibTableRow
fgDpdkEngEntry = _FgDpdkEngEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 12, 2, 1)
)
fgDpdkEngEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgDpdkEngEntIndex"),
)
if mibBuilder.loadTexts:
    fgDpdkEngEntry.setStatus("current")
_FgDpdkEngEntIndex_Type = FnIndex
_FgDpdkEngEntIndex_Object = MibTableColumn
fgDpdkEngEntIndex = _FgDpdkEngEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 12, 2, 1, 1),
    _FgDpdkEngEntIndex_Type()
)
fgDpdkEngEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgDpdkEngEntIndex.setStatus("current")


class _FgDpdkEngRxUsage_Type(Gauge32):
    """Custom type fgDpdkEngRxUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgDpdkEngRxUsage_Type.__name__ = "Gauge32"
_FgDpdkEngRxUsage_Object = MibTableColumn
fgDpdkEngRxUsage = _FgDpdkEngRxUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 12, 2, 1, 2),
    _FgDpdkEngRxUsage_Type()
)
fgDpdkEngRxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDpdkEngRxUsage.setStatus("current")
if mibBuilder.loadTexts:
    fgDpdkEngRxUsage.setUnits("%")


class _FgDpdkEngVnpUsage_Type(Gauge32):
    """Custom type fgDpdkEngVnpUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgDpdkEngVnpUsage_Type.__name__ = "Gauge32"
_FgDpdkEngVnpUsage_Object = MibTableColumn
fgDpdkEngVnpUsage = _FgDpdkEngVnpUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 12, 2, 1, 3),
    _FgDpdkEngVnpUsage_Type()
)
fgDpdkEngVnpUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDpdkEngVnpUsage.setStatus("current")
if mibBuilder.loadTexts:
    fgDpdkEngVnpUsage.setUnits("%")


class _FgDpdkEngIpsUsage_Type(Gauge32):
    """Custom type fgDpdkEngIpsUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgDpdkEngIpsUsage_Type.__name__ = "Gauge32"
_FgDpdkEngIpsUsage_Object = MibTableColumn
fgDpdkEngIpsUsage = _FgDpdkEngIpsUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 12, 2, 1, 4),
    _FgDpdkEngIpsUsage_Type()
)
fgDpdkEngIpsUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDpdkEngIpsUsage.setStatus("current")
if mibBuilder.loadTexts:
    fgDpdkEngIpsUsage.setUnits("%")


class _FgDpdkEngTxUsage_Type(Gauge32):
    """Custom type fgDpdkEngTxUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgDpdkEngTxUsage_Type.__name__ = "Gauge32"
_FgDpdkEngTxUsage_Object = MibTableColumn
fgDpdkEngTxUsage = _FgDpdkEngTxUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 12, 2, 1, 5),
    _FgDpdkEngTxUsage_Type()
)
fgDpdkEngTxUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDpdkEngTxUsage.setStatus("current")
if mibBuilder.loadTexts:
    fgDpdkEngTxUsage.setUnits("%")


class _FgDpdkEngIdle_Type(Gauge32):
    """Custom type fgDpdkEngIdle based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgDpdkEngIdle_Type.__name__ = "Gauge32"
_FgDpdkEngIdle_Object = MibTableColumn
fgDpdkEngIdle = _FgDpdkEngIdle_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 12, 2, 1, 6),
    _FgDpdkEngIdle_Type()
)
fgDpdkEngIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDpdkEngIdle.setStatus("current")
if mibBuilder.loadTexts:
    fgDpdkEngIdle.setUnits("%")
_FgDpdkEngToCpu_Type = Integer32
_FgDpdkEngToCpu_Object = MibTableColumn
fgDpdkEngToCpu = _FgDpdkEngToCpu_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 12, 2, 1, 7),
    _FgDpdkEngToCpu_Type()
)
fgDpdkEngToCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDpdkEngToCpu.setStatus("current")
_FgDigitalIO_ObjectIdentity = ObjectIdentity
fgDigitalIO = _FgDigitalIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 13)
)
_FgDioInfo_ObjectIdentity = ObjectIdentity
fgDioInfo = _FgDioInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 13, 1)
)
_FgDioTables_ObjectIdentity = ObjectIdentity
fgDioTables = _FgDioTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 13, 2)
)
_FgDioTable_Object = MibTable
fgDioTable = _FgDioTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 13, 2, 1)
)
if mibBuilder.loadTexts:
    fgDioTable.setStatus("current")
_FgDioEntry_Object = MibTableRow
fgDioEntry = _FgDioEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 13, 2, 1, 1)
)
fgDioEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgDioEntIndex"),
)
if mibBuilder.loadTexts:
    fgDioEntry.setStatus("current")
_FgDioEntIndex_Type = FnIndex
_FgDioEntIndex_Object = MibTableColumn
fgDioEntIndex = _FgDioEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 13, 2, 1, 1, 1),
    _FgDioEntIndex_Type()
)
fgDioEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgDioEntIndex.setStatus("current")
_FgDioEntName_Type = DisplayString
_FgDioEntName_Object = MibTableColumn
fgDioEntName = _FgDioEntName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 13, 2, 1, 1, 2),
    _FgDioEntName_Type()
)
fgDioEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDioEntName.setStatus("current")
_FgDioEntStatusMsg_Type = DisplayString
_FgDioEntStatusMsg_Object = MibTableColumn
fgDioEntStatusMsg = _FgDioEntStatusMsg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 13, 2, 1, 1, 3),
    _FgDioEntStatusMsg_Type()
)
fgDioEntStatusMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDioEntStatusMsg.setStatus("current")
_FgDioTrapObjects_ObjectIdentity = ObjectIdentity
fgDioTrapObjects = _FgDioTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 13, 3)
)


class _FgDioTrapType_Type(Integer32):
    """Custom type fgDioTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("stateChanged", 1)
    )


_FgDioTrapType_Type.__name__ = "Integer32"
_FgDioTrapType_Object = MibScalar
fgDioTrapType = _FgDioTrapType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 13, 3, 1),
    _FgDioTrapType_Type()
)
fgDioTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgDioTrapType.setStatus("current")
_FgChassisSensors_ObjectIdentity = ObjectIdentity
fgChassisSensors = _FgChassisSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 14)
)
_FgChassisSensorCount_Type = Integer32
_FgChassisSensorCount_Object = MibScalar
fgChassisSensorCount = _FgChassisSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 14, 1),
    _FgChassisSensorCount_Type()
)
fgChassisSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgChassisSensorCount.setStatus("current")
_FgChassisSensorTable_Object = MibTable
fgChassisSensorTable = _FgChassisSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 14, 2)
)
if mibBuilder.loadTexts:
    fgChassisSensorTable.setStatus("current")
_FgChassisSensorEntry_Object = MibTableRow
fgChassisSensorEntry = _FgChassisSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 14, 2, 1)
)
fgChassisSensorEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgChassisSensorEntIndex"),
)
if mibBuilder.loadTexts:
    fgChassisSensorEntry.setStatus("current")
_FgChassisSensorEntIndex_Type = FnIndex
_FgChassisSensorEntIndex_Object = MibTableColumn
fgChassisSensorEntIndex = _FgChassisSensorEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 14, 2, 1, 1),
    _FgChassisSensorEntIndex_Type()
)
fgChassisSensorEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgChassisSensorEntIndex.setStatus("current")
_FgChassisSensorEntName_Type = DisplayString
_FgChassisSensorEntName_Object = MibTableColumn
fgChassisSensorEntName = _FgChassisSensorEntName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 14, 2, 1, 2),
    _FgChassisSensorEntName_Type()
)
fgChassisSensorEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgChassisSensorEntName.setStatus("current")
_FgChassisSensorEntValue_Type = DisplayString
_FgChassisSensorEntValue_Object = MibTableColumn
fgChassisSensorEntValue = _FgChassisSensorEntValue_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 14, 2, 1, 3),
    _FgChassisSensorEntValue_Type()
)
fgChassisSensorEntValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgChassisSensorEntValue.setStatus("current")


class _FgChassisSensorEntAlarmStatus_Type(Integer32):
    """Custom type fgChassisSensorEntAlarmStatus based on Integer32"""
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


_FgChassisSensorEntAlarmStatus_Type.__name__ = "Integer32"
_FgChassisSensorEntAlarmStatus_Object = MibTableColumn
fgChassisSensorEntAlarmStatus = _FgChassisSensorEntAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 4, 14, 2, 1, 4),
    _FgChassisSensorEntAlarmStatus_Type()
)
fgChassisSensorEntAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgChassisSensorEntAlarmStatus.setStatus("current")
_FgFirewall_ObjectIdentity = ObjectIdentity
fgFirewall = _FgFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5)
)
_FgFwPolicies_ObjectIdentity = ObjectIdentity
fgFwPolicies = _FgFwPolicies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1)
)
_FgFwPolInfo_ObjectIdentity = ObjectIdentity
fgFwPolInfo = _FgFwPolInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 1)
)
_FgFwPolTables_ObjectIdentity = ObjectIdentity
fgFwPolTables = _FgFwPolTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2)
)
_FgFwPolStatsTable_Object = MibTable
fgFwPolStatsTable = _FgFwPolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fgFwPolStatsTable.setStatus("current")
_FgFwPolStatsEntry_Object = MibTableRow
fgFwPolStatsEntry = _FgFwPolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1, 1)
)
fgFwPolStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgFwPolID"),
)
if mibBuilder.loadTexts:
    fgFwPolStatsEntry.setStatus("current")
_FgFwPolID_Type = FnIndex
_FgFwPolID_Object = MibTableColumn
fgFwPolID = _FgFwPolID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1, 1, 1),
    _FgFwPolID_Type()
)
fgFwPolID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgFwPolID.setStatus("current")
_FgFwPolPktCount_Type = Counter32
_FgFwPolPktCount_Object = MibTableColumn
fgFwPolPktCount = _FgFwPolPktCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1, 1, 2),
    _FgFwPolPktCount_Type()
)
fgFwPolPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwPolPktCount.setStatus("current")
_FgFwPolByteCount_Type = Counter32
_FgFwPolByteCount_Object = MibTableColumn
fgFwPolByteCount = _FgFwPolByteCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1, 1, 3),
    _FgFwPolByteCount_Type()
)
fgFwPolByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwPolByteCount.setStatus("current")
_FgFwPolLastUsed_Type = DisplayString
_FgFwPolLastUsed_Object = MibTableColumn
fgFwPolLastUsed = _FgFwPolLastUsed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1, 1, 4),
    _FgFwPolLastUsed_Type()
)
fgFwPolLastUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwPolLastUsed.setStatus("current")
_FgFwPolPktCountHc_Type = Counter64
_FgFwPolPktCountHc_Object = MibTableColumn
fgFwPolPktCountHc = _FgFwPolPktCountHc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1, 1, 5),
    _FgFwPolPktCountHc_Type()
)
fgFwPolPktCountHc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwPolPktCountHc.setStatus("current")
_FgFwPolByteCountHc_Type = Counter64
_FgFwPolByteCountHc_Object = MibTableColumn
fgFwPolByteCountHc = _FgFwPolByteCountHc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 1, 1, 6),
    _FgFwPolByteCountHc_Type()
)
fgFwPolByteCountHc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwPolByteCountHc.setStatus("current")
_FgFwHsPolStatsTable_Object = MibTable
fgFwHsPolStatsTable = _FgFwHsPolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fgFwHsPolStatsTable.setStatus("current")
_FgFwHsPolStatsEntry_Object = MibTableRow
fgFwHsPolStatsEntry = _FgFwHsPolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 3, 1)
)
fgFwHsPolStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgFwHsPolID"),
)
if mibBuilder.loadTexts:
    fgFwHsPolStatsEntry.setStatus("current")
_FgFwHsPolID_Type = FnIndex
_FgFwHsPolID_Object = MibTableColumn
fgFwHsPolID = _FgFwHsPolID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 3, 1, 1),
    _FgFwHsPolID_Type()
)
fgFwHsPolID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgFwHsPolID.setStatus("current")
_FgFwHsPolPktCount_Type = Counter64
_FgFwHsPolPktCount_Object = MibTableColumn
fgFwHsPolPktCount = _FgFwHsPolPktCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 3, 1, 2),
    _FgFwHsPolPktCount_Type()
)
fgFwHsPolPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwHsPolPktCount.setStatus("current")
_FgFwHsPolByteCount_Type = Counter64
_FgFwHsPolByteCount_Object = MibTableColumn
fgFwHsPolByteCount = _FgFwHsPolByteCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 3, 1, 3),
    _FgFwHsPolByteCount_Type()
)
fgFwHsPolByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwHsPolByteCount.setStatus("current")
_FgFwHsPolLastUsed_Type = DisplayString
_FgFwHsPolLastUsed_Object = MibTableColumn
fgFwHsPolLastUsed = _FgFwHsPolLastUsed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 1, 2, 3, 1, 4),
    _FgFwHsPolLastUsed_Type()
)
fgFwHsPolLastUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwHsPolLastUsed.setStatus("current")
_FgFwUsers_ObjectIdentity = ObjectIdentity
fgFwUsers = _FgFwUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2)
)
_FgFwUserInfo_ObjectIdentity = ObjectIdentity
fgFwUserInfo = _FgFwUserInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 1)
)
_FgFwUserNumber_Type = Integer32
_FgFwUserNumber_Object = MibScalar
fgFwUserNumber = _FgFwUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 1, 1),
    _FgFwUserNumber_Type()
)
fgFwUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwUserNumber.setStatus("current")
_FgFwUserAuthTimeout_Type = Integer32
_FgFwUserAuthTimeout_Object = MibScalar
fgFwUserAuthTimeout = _FgFwUserAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 1, 2),
    _FgFwUserAuthTimeout_Type()
)
fgFwUserAuthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwUserAuthTimeout.setStatus("current")
_FgFwUserTables_ObjectIdentity = ObjectIdentity
fgFwUserTables = _FgFwUserTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2)
)
_FgFwUserTable_Object = MibTable
fgFwUserTable = _FgFwUserTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fgFwUserTable.setStatus("current")
_FgFwUserEntry_Object = MibTableRow
fgFwUserEntry = _FgFwUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2, 1, 1)
)
fgFwUserEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgFwUserIndex"),
)
if mibBuilder.loadTexts:
    fgFwUserEntry.setStatus("current")
_FgFwUserIndex_Type = FnIndex
_FgFwUserIndex_Object = MibTableColumn
fgFwUserIndex = _FgFwUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2, 1, 1, 1),
    _FgFwUserIndex_Type()
)
fgFwUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgFwUserIndex.setStatus("current")
_FgFwUserName_Type = DisplayString
_FgFwUserName_Object = MibTableColumn
fgFwUserName = _FgFwUserName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2, 1, 1, 2),
    _FgFwUserName_Type()
)
fgFwUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwUserName.setStatus("current")
_FgFwUserAuth_Type = FgFwUserAuthType
_FgFwUserAuth_Object = MibTableColumn
fgFwUserAuth = _FgFwUserAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2, 1, 1, 3),
    _FgFwUserAuth_Type()
)
fgFwUserAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwUserAuth.setStatus("current")
_FgFwUserState_Type = FnBoolState
_FgFwUserState_Object = MibTableColumn
fgFwUserState = _FgFwUserState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2, 1, 1, 4),
    _FgFwUserState_Type()
)
fgFwUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwUserState.setStatus("current")
_FgFwUserVdom_Type = FgVdIndex
_FgFwUserVdom_Object = MibTableColumn
fgFwUserVdom = _FgFwUserVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 2, 1, 1, 5),
    _FgFwUserVdom_Type()
)
fgFwUserVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwUserVdom.setStatus("current")
_FgFwAuthUserTables_ObjectIdentity = ObjectIdentity
fgFwAuthUserTables = _FgFwAuthUserTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3)
)
_FgFwAuthUserInfoTable_Object = MibTable
fgFwAuthUserInfoTable = _FgFwAuthUserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fgFwAuthUserInfoTable.setStatus("current")
_FgFwAuthUserInfoEntry_Object = MibTableRow
fgFwAuthUserInfoEntry = _FgFwAuthUserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 1, 1)
)
fgFwAuthUserInfoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgFwAuthUserInfoVdom"),
)
if mibBuilder.loadTexts:
    fgFwAuthUserInfoEntry.setStatus("current")
_FgFwAuthUserInfoVdom_Type = FgVdIndex
_FgFwAuthUserInfoVdom_Object = MibTableColumn
fgFwAuthUserInfoVdom = _FgFwAuthUserInfoVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 1, 1, 1),
    _FgFwAuthUserInfoVdom_Type()
)
fgFwAuthUserInfoVdom.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgFwAuthUserInfoVdom.setStatus("current")
_FgFwAuthIpv4UserNumber_Type = Integer32
_FgFwAuthIpv4UserNumber_Object = MibTableColumn
fgFwAuthIpv4UserNumber = _FgFwAuthIpv4UserNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 1, 1, 2),
    _FgFwAuthIpv4UserNumber_Type()
)
fgFwAuthIpv4UserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwAuthIpv4UserNumber.setStatus("current")
_FgFwAuthIpv6UserNumber_Type = Integer32
_FgFwAuthIpv6UserNumber_Object = MibTableColumn
fgFwAuthIpv6UserNumber = _FgFwAuthIpv6UserNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 1, 1, 3),
    _FgFwAuthIpv6UserNumber_Type()
)
fgFwAuthIpv6UserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwAuthIpv6UserNumber.setStatus("current")
_FgFwAuthIpv4UserTable_Object = MibTable
fgFwAuthIpv4UserTable = _FgFwAuthIpv4UserTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 2)
)
if mibBuilder.loadTexts:
    fgFwAuthIpv4UserTable.setStatus("current")
_FgFwAuthIpv4UserEntry_Object = MibTableRow
fgFwAuthIpv4UserEntry = _FgFwAuthIpv4UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 2, 1)
)
fgFwAuthIpv4UserEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgFwAuthIpv4UserIndex"),
)
if mibBuilder.loadTexts:
    fgFwAuthIpv4UserEntry.setStatus("current")
_FgFwAuthIpv4UserIndex_Type = FnIndex
_FgFwAuthIpv4UserIndex_Object = MibTableColumn
fgFwAuthIpv4UserIndex = _FgFwAuthIpv4UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 2, 1, 1),
    _FgFwAuthIpv4UserIndex_Type()
)
fgFwAuthIpv4UserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgFwAuthIpv4UserIndex.setStatus("current")
_FgFwAuthIpv4UserVdom_Type = FgVdIndex
_FgFwAuthIpv4UserVdom_Object = MibTableColumn
fgFwAuthIpv4UserVdom = _FgFwAuthIpv4UserVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 2, 1, 2),
    _FgFwAuthIpv4UserVdom_Type()
)
fgFwAuthIpv4UserVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwAuthIpv4UserVdom.setStatus("current")
_FgFwAuthIpv4UserName_Type = DisplayString
_FgFwAuthIpv4UserName_Object = MibTableColumn
fgFwAuthIpv4UserName = _FgFwAuthIpv4UserName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 2, 1, 3),
    _FgFwAuthIpv4UserName_Type()
)
fgFwAuthIpv4UserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwAuthIpv4UserName.setStatus("current")
_FgFwAuthIpv4UserType_Type = FgFwAuthUserType
_FgFwAuthIpv4UserType_Object = MibTableColumn
fgFwAuthIpv4UserType = _FgFwAuthIpv4UserType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 2, 1, 4),
    _FgFwAuthIpv4UserType_Type()
)
fgFwAuthIpv4UserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwAuthIpv4UserType.setStatus("current")
_FgFwAuthIpv4UserAddr_Type = IpAddress
_FgFwAuthIpv4UserAddr_Object = MibTableColumn
fgFwAuthIpv4UserAddr = _FgFwAuthIpv4UserAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 2, 1, 5),
    _FgFwAuthIpv4UserAddr_Type()
)
fgFwAuthIpv4UserAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwAuthIpv4UserAddr.setStatus("current")
_FgFwAuthIpv6UserTable_Object = MibTable
fgFwAuthIpv6UserTable = _FgFwAuthIpv6UserTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 3)
)
if mibBuilder.loadTexts:
    fgFwAuthIpv6UserTable.setStatus("current")
_FgFwAuthIpv6UserEntry_Object = MibTableRow
fgFwAuthIpv6UserEntry = _FgFwAuthIpv6UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 3, 1)
)
fgFwAuthIpv6UserEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgFwAuthIpv6UserIndex"),
)
if mibBuilder.loadTexts:
    fgFwAuthIpv6UserEntry.setStatus("current")
_FgFwAuthIpv6UserIndex_Type = FnIndex
_FgFwAuthIpv6UserIndex_Object = MibTableColumn
fgFwAuthIpv6UserIndex = _FgFwAuthIpv6UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 3, 1, 1),
    _FgFwAuthIpv6UserIndex_Type()
)
fgFwAuthIpv6UserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgFwAuthIpv6UserIndex.setStatus("current")
_FgFwAuthIpv6UserVdom_Type = FgVdIndex
_FgFwAuthIpv6UserVdom_Object = MibTableColumn
fgFwAuthIpv6UserVdom = _FgFwAuthIpv6UserVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 3, 1, 2),
    _FgFwAuthIpv6UserVdom_Type()
)
fgFwAuthIpv6UserVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwAuthIpv6UserVdom.setStatus("current")
_FgFwAuthIpv6UserName_Type = DisplayString
_FgFwAuthIpv6UserName_Object = MibTableColumn
fgFwAuthIpv6UserName = _FgFwAuthIpv6UserName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 3, 1, 3),
    _FgFwAuthIpv6UserName_Type()
)
fgFwAuthIpv6UserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwAuthIpv6UserName.setStatus("current")
_FgFwAuthIpv6UserType_Type = FgFwAuthUserType
_FgFwAuthIpv6UserType_Object = MibTableColumn
fgFwAuthIpv6UserType = _FgFwAuthIpv6UserType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 3, 1, 4),
    _FgFwAuthIpv6UserType_Type()
)
fgFwAuthIpv6UserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwAuthIpv6UserType.setStatus("current")
_FgFwAuthIpv6UserAddr_Type = Ipv6Address
_FgFwAuthIpv6UserAddr_Object = MibTableColumn
fgFwAuthIpv6UserAddr = _FgFwAuthIpv6UserAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 2, 3, 3, 1, 5),
    _FgFwAuthIpv6UserAddr_Type()
)
fgFwAuthIpv6UserAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwAuthIpv6UserAddr.setStatus("current")
_FgFwIppools_ObjectIdentity = ObjectIdentity
fgFwIppools = _FgFwIppools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3)
)
_FgFwIppTables_ObjectIdentity = ObjectIdentity
fgFwIppTables = _FgFwIppTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2)
)
_FgFwIppStatsTable_Object = MibTable
fgFwIppStatsTable = _FgFwIppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1)
)
if mibBuilder.loadTexts:
    fgFwIppStatsTable.setStatus("current")
_FgFwIppStatsEntry_Object = MibTableRow
fgFwIppStatsEntry = _FgFwIppStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1)
)
fgFwIppStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgFwIppStatsStartIp"),
    (0, "FORTINET-FORTIGATE-MIB", "fgFwIppStatsEndIp"),
)
if mibBuilder.loadTexts:
    fgFwIppStatsEntry.setStatus("current")
_FgFwIppStatsName_Type = DisplayString
_FgFwIppStatsName_Object = MibTableColumn
fgFwIppStatsName = _FgFwIppStatsName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 1),
    _FgFwIppStatsName_Type()
)
fgFwIppStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsName.setStatus("current")
_FgFwIppStatsType_Type = DisplayString
_FgFwIppStatsType_Object = MibTableColumn
fgFwIppStatsType = _FgFwIppStatsType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 2),
    _FgFwIppStatsType_Type()
)
fgFwIppStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsType.setStatus("current")
_FgFwIppStatsStartIp_Type = IpAddress
_FgFwIppStatsStartIp_Object = MibTableColumn
fgFwIppStatsStartIp = _FgFwIppStatsStartIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 3),
    _FgFwIppStatsStartIp_Type()
)
fgFwIppStatsStartIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgFwIppStatsStartIp.setStatus("current")
_FgFwIppStatsEndIp_Type = IpAddress
_FgFwIppStatsEndIp_Object = MibTableColumn
fgFwIppStatsEndIp = _FgFwIppStatsEndIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 4),
    _FgFwIppStatsEndIp_Type()
)
fgFwIppStatsEndIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgFwIppStatsEndIp.setStatus("current")
_FgFwIppStatsTotalSessions_Type = Gauge32
_FgFwIppStatsTotalSessions_Object = MibTableColumn
fgFwIppStatsTotalSessions = _FgFwIppStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 5),
    _FgFwIppStatsTotalSessions_Type()
)
fgFwIppStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsTotalSessions.setStatus("current")
_FgFwIppStatsTcpSessions_Type = Gauge32
_FgFwIppStatsTcpSessions_Object = MibTableColumn
fgFwIppStatsTcpSessions = _FgFwIppStatsTcpSessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 6),
    _FgFwIppStatsTcpSessions_Type()
)
fgFwIppStatsTcpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsTcpSessions.setStatus("current")
_FgFwIppStatsUdpSessions_Type = Gauge32
_FgFwIppStatsUdpSessions_Object = MibTableColumn
fgFwIppStatsUdpSessions = _FgFwIppStatsUdpSessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 7),
    _FgFwIppStatsUdpSessions_Type()
)
fgFwIppStatsUdpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsUdpSessions.setStatus("current")
_FgFwIppStatsOtherSessions_Type = Gauge32
_FgFwIppStatsOtherSessions_Object = MibTableColumn
fgFwIppStatsOtherSessions = _FgFwIppStatsOtherSessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 8),
    _FgFwIppStatsOtherSessions_Type()
)
fgFwIppStatsOtherSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsOtherSessions.setStatus("current")
_FgFwIppStatsTotalPBAs_Type = Gauge32
_FgFwIppStatsTotalPBAs_Object = MibTableColumn
fgFwIppStatsTotalPBAs = _FgFwIppStatsTotalPBAs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 9),
    _FgFwIppStatsTotalPBAs_Type()
)
fgFwIppStatsTotalPBAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsTotalPBAs.setStatus("current")
_FgFwIppStatsInusePBAs_Type = Gauge32
_FgFwIppStatsInusePBAs_Object = MibTableColumn
fgFwIppStatsInusePBAs = _FgFwIppStatsInusePBAs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 10),
    _FgFwIppStatsInusePBAs_Type()
)
fgFwIppStatsInusePBAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsInusePBAs.setStatus("current")
_FgFwIppStatsExpiringPBAs_Type = Gauge32
_FgFwIppStatsExpiringPBAs_Object = MibTableColumn
fgFwIppStatsExpiringPBAs = _FgFwIppStatsExpiringPBAs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 11),
    _FgFwIppStatsExpiringPBAs_Type()
)
fgFwIppStatsExpiringPBAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsExpiringPBAs.setStatus("current")


class _FgFwIppStatsFreePBAs_Type(Gauge32):
    """Custom type fgFwIppStatsFreePBAs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgFwIppStatsFreePBAs_Type.__name__ = "Gauge32"
_FgFwIppStatsFreePBAs_Object = MibTableColumn
fgFwIppStatsFreePBAs = _FgFwIppStatsFreePBAs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 12),
    _FgFwIppStatsFreePBAs_Type()
)
fgFwIppStatsFreePBAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsFreePBAs.setStatus("current")
_FgFwIppStatsFlags_Type = DisplayString
_FgFwIppStatsFlags_Object = MibTableColumn
fgFwIppStatsFlags = _FgFwIppStatsFlags_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 13),
    _FgFwIppStatsFlags_Type()
)
fgFwIppStatsFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsFlags.setStatus("current")
_FgFwIppStatsGroupName_Type = DisplayString
_FgFwIppStatsGroupName_Object = MibTableColumn
fgFwIppStatsGroupName = _FgFwIppStatsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 14),
    _FgFwIppStatsGroupName_Type()
)
fgFwIppStatsGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsGroupName.setStatus("current")
_FgFwIppStatsBlockSize_Type = Gauge32
_FgFwIppStatsBlockSize_Object = MibTableColumn
fgFwIppStatsBlockSize = _FgFwIppStatsBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 15),
    _FgFwIppStatsBlockSize_Type()
)
fgFwIppStatsBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsBlockSize.setStatus("current")
_FgFwIppStatsPortStart_Type = InetPortNumber
_FgFwIppStatsPortStart_Object = MibTableColumn
fgFwIppStatsPortStart = _FgFwIppStatsPortStart_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 16),
    _FgFwIppStatsPortStart_Type()
)
fgFwIppStatsPortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsPortStart.setStatus("current")
_FgFwIppStatsPortEnd_Type = InetPortNumber
_FgFwIppStatsPortEnd_Object = MibTableColumn
fgFwIppStatsPortEnd = _FgFwIppStatsPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 17),
    _FgFwIppStatsPortEnd_Type()
)
fgFwIppStatsPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsPortEnd.setStatus("current")
_FgFwIppStatsStartClientIP_Type = IpAddress
_FgFwIppStatsStartClientIP_Object = MibTableColumn
fgFwIppStatsStartClientIP = _FgFwIppStatsStartClientIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 18),
    _FgFwIppStatsStartClientIP_Type()
)
fgFwIppStatsStartClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsStartClientIP.setStatus("current")
_FgFwIppStatsEndClientIP_Type = IpAddress
_FgFwIppStatsEndClientIP_Object = MibTableColumn
fgFwIppStatsEndClientIP = _FgFwIppStatsEndClientIP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 19),
    _FgFwIppStatsEndClientIP_Type()
)
fgFwIppStatsEndClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsEndClientIP.setStatus("current")
_FgFwIppStatsRscTCP_Type = Gauge32
_FgFwIppStatsRscTCP_Object = MibTableColumn
fgFwIppStatsRscTCP = _FgFwIppStatsRscTCP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 20),
    _FgFwIppStatsRscTCP_Type()
)
fgFwIppStatsRscTCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsRscTCP.setStatus("current")
_FgFwIppStatsRscUDP_Type = Gauge32
_FgFwIppStatsRscUDP_Object = MibTableColumn
fgFwIppStatsRscUDP = _FgFwIppStatsRscUDP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 21),
    _FgFwIppStatsRscUDP_Type()
)
fgFwIppStatsRscUDP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsRscUDP.setStatus("current")
_FgFwIppStatsUsedRscTCP_Type = Gauge32
_FgFwIppStatsUsedRscTCP_Object = MibTableColumn
fgFwIppStatsUsedRscTCP = _FgFwIppStatsUsedRscTCP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 22),
    _FgFwIppStatsUsedRscTCP_Type()
)
fgFwIppStatsUsedRscTCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsUsedRscTCP.setStatus("current")
_FgFwIppStatsUsedRscUDP_Type = Gauge32
_FgFwIppStatsUsedRscUDP_Object = MibTableColumn
fgFwIppStatsUsedRscUDP = _FgFwIppStatsUsedRscUDP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 23),
    _FgFwIppStatsUsedRscUDP_Type()
)
fgFwIppStatsUsedRscUDP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsUsedRscUDP.setStatus("current")


class _FgFwIppStatsPercentageTCP_Type(Gauge32):
    """Custom type fgFwIppStatsPercentageTCP based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgFwIppStatsPercentageTCP_Type.__name__ = "Gauge32"
_FgFwIppStatsPercentageTCP_Object = MibTableColumn
fgFwIppStatsPercentageTCP = _FgFwIppStatsPercentageTCP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 24),
    _FgFwIppStatsPercentageTCP_Type()
)
fgFwIppStatsPercentageTCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsPercentageTCP.setStatus("current")


class _FgFwIppStatsPercentageUDP_Type(Gauge32):
    """Custom type fgFwIppStatsPercentageUDP based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgFwIppStatsPercentageUDP_Type.__name__ = "Gauge32"
_FgFwIppStatsPercentageUDP_Object = MibTableColumn
fgFwIppStatsPercentageUDP = _FgFwIppStatsPercentageUDP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 2, 1, 1, 25),
    _FgFwIppStatsPercentageUDP_Type()
)
fgFwIppStatsPercentageUDP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwIppStatsPercentageUDP.setStatus("current")
_FgFwIppTrapObjects_ObjectIdentity = ObjectIdentity
fgFwIppTrapObjects = _FgFwIppTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 3)
)


class _FgFwIppTrapType_Type(Integer32):
    """Custom type fgFwIppTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("raise", 1),
          ("clear", 2))
    )


_FgFwIppTrapType_Type.__name__ = "Integer32"
_FgFwIppTrapType_Object = MibScalar
fgFwIppTrapType = _FgFwIppTrapType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 3, 1),
    _FgFwIppTrapType_Type()
)
fgFwIppTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgFwIppTrapType.setStatus("current")
_FgFwTrapPoolUtilization_Type = Gauge32
_FgFwTrapPoolUtilization_Object = MibScalar
fgFwTrapPoolUtilization = _FgFwTrapPoolUtilization_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 3, 2),
    _FgFwTrapPoolUtilization_Type()
)
fgFwTrapPoolUtilization.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgFwTrapPoolUtilization.setStatus("current")
_FgFwIppTrapPoolProto_Type = Integer32
_FgFwIppTrapPoolProto_Object = MibScalar
fgFwIppTrapPoolProto = _FgFwIppTrapPoolProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 3, 3, 3),
    _FgFwIppTrapPoolProto_Type()
)
fgFwIppTrapPoolProto.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgFwIppTrapPoolProto.setStatus("current")
_FgFwGtp_ObjectIdentity = ObjectIdentity
fgFwGtp = _FgFwGtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4)
)
_FgFwGtpStats_ObjectIdentity = ObjectIdentity
fgFwGtpStats = _FgFwGtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1)
)
_FgFwGtpStatsRequest_Type = Gauge32
_FgFwGtpStatsRequest_Object = MibScalar
fgFwGtpStatsRequest = _FgFwGtpStatsRequest_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 1),
    _FgFwGtpStatsRequest_Type()
)
fgFwGtpStatsRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsRequest.setStatus("current")
_FgFwGtpStatsEchoRequest_Type = Gauge32
_FgFwGtpStatsEchoRequest_Object = MibScalar
fgFwGtpStatsEchoRequest = _FgFwGtpStatsEchoRequest_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 2),
    _FgFwGtpStatsEchoRequest_Type()
)
fgFwGtpStatsEchoRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsEchoRequest.setStatus("current")
_FgFwGtpStatsTunnel_Type = Gauge32
_FgFwGtpStatsTunnel_Object = MibScalar
fgFwGtpStatsTunnel = _FgFwGtpStatsTunnel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 3),
    _FgFwGtpStatsTunnel_Type()
)
fgFwGtpStatsTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsTunnel.setStatus("current")
_FgFwGtpStatsTunnelV0_Type = Gauge32
_FgFwGtpStatsTunnelV0_Object = MibScalar
fgFwGtpStatsTunnelV0 = _FgFwGtpStatsTunnelV0_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 4),
    _FgFwGtpStatsTunnelV0_Type()
)
fgFwGtpStatsTunnelV0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsTunnelV0.setStatus("current")
_FgFwGtpStatsPath_Type = Gauge32
_FgFwGtpStatsPath_Object = MibScalar
fgFwGtpStatsPath = _FgFwGtpStatsPath_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 5),
    _FgFwGtpStatsPath_Type()
)
fgFwGtpStatsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsPath.setStatus("current")
_FgFwGtpStatsBearer_Type = Gauge32
_FgFwGtpStatsBearer_Object = MibScalar
fgFwGtpStatsBearer = _FgFwGtpStatsBearer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 6),
    _FgFwGtpStatsBearer_Type()
)
fgFwGtpStatsBearer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsBearer.setStatus("current")
_FgFwGtpStatsFteid_Type = Gauge32
_FgFwGtpStatsFteid_Object = MibScalar
fgFwGtpStatsFteid = _FgFwGtpStatsFteid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 7),
    _FgFwGtpStatsFteid_Type()
)
fgFwGtpStatsFteid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsFteid.setStatus("current")
_FgFwGtpStatsProfile_Type = Gauge32
_FgFwGtpStatsProfile_Object = MibScalar
fgFwGtpStatsProfile = _FgFwGtpStatsProfile_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 8),
    _FgFwGtpStatsProfile_Type()
)
fgFwGtpStatsProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsProfile.setStatus("current")
_FgFwGtpStatsImsi_Type = Gauge32
_FgFwGtpStatsImsi_Object = MibScalar
fgFwGtpStatsImsi = _FgFwGtpStatsImsi_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 9),
    _FgFwGtpStatsImsi_Type()
)
fgFwGtpStatsImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsImsi.setStatus("current")
_FgFwGtpStatsApn_Type = Gauge32
_FgFwGtpStatsApn_Object = MibScalar
fgFwGtpStatsApn = _FgFwGtpStatsApn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 10),
    _FgFwGtpStatsApn_Type()
)
fgFwGtpStatsApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsApn.setStatus("current")
_FgFwGtpStatsApnShaper_Type = Gauge32
_FgFwGtpStatsApnShaper_Object = MibScalar
fgFwGtpStatsApnShaper = _FgFwGtpStatsApnShaper_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 11),
    _FgFwGtpStatsApnShaper_Type()
)
fgFwGtpStatsApnShaper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsApnShaper.setStatus("current")
_FgFwGtpStatsTunnelLimiter_Type = Gauge32
_FgFwGtpStatsTunnelLimiter_Object = MibScalar
fgFwGtpStatsTunnelLimiter = _FgFwGtpStatsTunnelLimiter_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 12),
    _FgFwGtpStatsTunnelLimiter_Type()
)
fgFwGtpStatsTunnelLimiter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsTunnelLimiter.setStatus("current")
_FgFwGtpStatsAdvPolicies_Type = Gauge32
_FgFwGtpStatsAdvPolicies_Object = MibScalar
fgFwGtpStatsAdvPolicies = _FgFwGtpStatsAdvPolicies_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 13),
    _FgFwGtpStatsAdvPolicies_Type()
)
fgFwGtpStatsAdvPolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsAdvPolicies.setStatus("current")
_FgFwGtpStatsIeRemovePolicies_Type = Gauge32
_FgFwGtpStatsIeRemovePolicies_Object = MibScalar
fgFwGtpStatsIeRemovePolicies = _FgFwGtpStatsIeRemovePolicies_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 14),
    _FgFwGtpStatsIeRemovePolicies_Type()
)
fgFwGtpStatsIeRemovePolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsIeRemovePolicies.setStatus("current")
_FgFwGtpStatsIpPolicy_Type = Gauge32
_FgFwGtpStatsIpPolicy_Object = MibScalar
fgFwGtpStatsIpPolicy = _FgFwGtpStatsIpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 15),
    _FgFwGtpStatsIpPolicy_Type()
)
fgFwGtpStatsIpPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsIpPolicy.setStatus("current")
_FgFwGtpStatsNoipPolicy_Type = Gauge32
_FgFwGtpStatsNoipPolicy_Object = MibScalar
fgFwGtpStatsNoipPolicy = _FgFwGtpStatsNoipPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 16),
    _FgFwGtpStatsNoipPolicy_Type()
)
fgFwGtpStatsNoipPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsNoipPolicy.setStatus("current")
_FgFwGtpStatsIeWlEntry_Type = Gauge32
_FgFwGtpStatsIeWlEntry_Object = MibScalar
fgFwGtpStatsIeWlEntry = _FgFwGtpStatsIeWlEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 17),
    _FgFwGtpStatsIeWlEntry_Type()
)
fgFwGtpStatsIeWlEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsIeWlEntry.setStatus("current")
_FgFwGtpStatsClash_Type = Counter64
_FgFwGtpStatsClash_Object = MibScalar
fgFwGtpStatsClash = _FgFwGtpStatsClash_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 18),
    _FgFwGtpStatsClash_Type()
)
fgFwGtpStatsClash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsClash.setStatus("current")
_FgFwGtpStatsDrop_Type = Counter64
_FgFwGtpStatsDrop_Object = MibScalar
fgFwGtpStatsDrop = _FgFwGtpStatsDrop_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 1, 19),
    _FgFwGtpStatsDrop_Type()
)
fgFwGtpStatsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpStatsDrop.setStatus("current")
_FgFwGtpRtStats_ObjectIdentity = ObjectIdentity
fgFwGtpRtStats = _FgFwGtpRtStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2)
)
_FgFwGtpRtStatsCPkts_ObjectIdentity = ObjectIdentity
fgFwGtpRtStatsCPkts = _FgFwGtpRtStatsCPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1)
)
_FgFwGtpRtStatsCForwarded_Type = Counter64
_FgFwGtpRtStatsCForwarded_Object = MibScalar
fgFwGtpRtStatsCForwarded = _FgFwGtpRtStatsCForwarded_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 1),
    _FgFwGtpRtStatsCForwarded_Type()
)
fgFwGtpRtStatsCForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCForwarded.setStatus("current")
_FgFwGtpRtStatsCRejected_Type = Counter64
_FgFwGtpRtStatsCRejected_Object = MibScalar
fgFwGtpRtStatsCRejected = _FgFwGtpRtStatsCRejected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 2),
    _FgFwGtpRtStatsCRejected_Type()
)
fgFwGtpRtStatsCRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCRejected.setStatus("current")
_FgFwGtpRtStatsCDropped0_Type = Counter64
_FgFwGtpRtStatsCDropped0_Object = MibScalar
fgFwGtpRtStatsCDropped0 = _FgFwGtpRtStatsCDropped0_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 3),
    _FgFwGtpRtStatsCDropped0_Type()
)
fgFwGtpRtStatsCDropped0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped0.setStatus("current")
_FgFwGtpRtStatsCDropped1_Type = Counter64
_FgFwGtpRtStatsCDropped1_Object = MibScalar
fgFwGtpRtStatsCDropped1 = _FgFwGtpRtStatsCDropped1_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 4),
    _FgFwGtpRtStatsCDropped1_Type()
)
fgFwGtpRtStatsCDropped1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped1.setStatus("current")
_FgFwGtpRtStatsCDropped2_Type = Counter64
_FgFwGtpRtStatsCDropped2_Object = MibScalar
fgFwGtpRtStatsCDropped2 = _FgFwGtpRtStatsCDropped2_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 5),
    _FgFwGtpRtStatsCDropped2_Type()
)
fgFwGtpRtStatsCDropped2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped2.setStatus("current")
_FgFwGtpRtStatsCDropped3_Type = Counter64
_FgFwGtpRtStatsCDropped3_Object = MibScalar
fgFwGtpRtStatsCDropped3 = _FgFwGtpRtStatsCDropped3_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 6),
    _FgFwGtpRtStatsCDropped3_Type()
)
fgFwGtpRtStatsCDropped3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped3.setStatus("current")
_FgFwGtpRtStatsCDropped4_Type = Counter64
_FgFwGtpRtStatsCDropped4_Object = MibScalar
fgFwGtpRtStatsCDropped4 = _FgFwGtpRtStatsCDropped4_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 7),
    _FgFwGtpRtStatsCDropped4_Type()
)
fgFwGtpRtStatsCDropped4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped4.setStatus("current")
_FgFwGtpRtStatsCDropped5_Type = Counter64
_FgFwGtpRtStatsCDropped5_Object = MibScalar
fgFwGtpRtStatsCDropped5 = _FgFwGtpRtStatsCDropped5_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 8),
    _FgFwGtpRtStatsCDropped5_Type()
)
fgFwGtpRtStatsCDropped5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped5.setStatus("current")
_FgFwGtpRtStatsCDropped6_Type = Counter64
_FgFwGtpRtStatsCDropped6_Object = MibScalar
fgFwGtpRtStatsCDropped6 = _FgFwGtpRtStatsCDropped6_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 9),
    _FgFwGtpRtStatsCDropped6_Type()
)
fgFwGtpRtStatsCDropped6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped6.setStatus("current")
_FgFwGtpRtStatsCDropped7_Type = Counter64
_FgFwGtpRtStatsCDropped7_Object = MibScalar
fgFwGtpRtStatsCDropped7 = _FgFwGtpRtStatsCDropped7_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 10),
    _FgFwGtpRtStatsCDropped7_Type()
)
fgFwGtpRtStatsCDropped7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped7.setStatus("current")
_FgFwGtpRtStatsCDropped8_Type = Counter64
_FgFwGtpRtStatsCDropped8_Object = MibScalar
fgFwGtpRtStatsCDropped8 = _FgFwGtpRtStatsCDropped8_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 11),
    _FgFwGtpRtStatsCDropped8_Type()
)
fgFwGtpRtStatsCDropped8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped8.setStatus("current")
_FgFwGtpRtStatsCDropped9_Type = Counter64
_FgFwGtpRtStatsCDropped9_Object = MibScalar
fgFwGtpRtStatsCDropped9 = _FgFwGtpRtStatsCDropped9_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 12),
    _FgFwGtpRtStatsCDropped9_Type()
)
fgFwGtpRtStatsCDropped9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped9.setStatus("current")
_FgFwGtpRtStatsCDropped10_Type = Counter64
_FgFwGtpRtStatsCDropped10_Object = MibScalar
fgFwGtpRtStatsCDropped10 = _FgFwGtpRtStatsCDropped10_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 13),
    _FgFwGtpRtStatsCDropped10_Type()
)
fgFwGtpRtStatsCDropped10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped10.setStatus("current")
_FgFwGtpRtStatsCDropped11_Type = Counter64
_FgFwGtpRtStatsCDropped11_Object = MibScalar
fgFwGtpRtStatsCDropped11 = _FgFwGtpRtStatsCDropped11_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 14),
    _FgFwGtpRtStatsCDropped11_Type()
)
fgFwGtpRtStatsCDropped11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped11.setStatus("current")
_FgFwGtpRtStatsCDropped12_Type = Counter64
_FgFwGtpRtStatsCDropped12_Object = MibScalar
fgFwGtpRtStatsCDropped12 = _FgFwGtpRtStatsCDropped12_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 15),
    _FgFwGtpRtStatsCDropped12_Type()
)
fgFwGtpRtStatsCDropped12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped12.setStatus("current")
_FgFwGtpRtStatsCDropped13_Type = Counter64
_FgFwGtpRtStatsCDropped13_Object = MibScalar
fgFwGtpRtStatsCDropped13 = _FgFwGtpRtStatsCDropped13_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 16),
    _FgFwGtpRtStatsCDropped13_Type()
)
fgFwGtpRtStatsCDropped13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped13.setStatus("current")
_FgFwGtpRtStatsCDropped14_Type = Counter64
_FgFwGtpRtStatsCDropped14_Object = MibScalar
fgFwGtpRtStatsCDropped14 = _FgFwGtpRtStatsCDropped14_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 17),
    _FgFwGtpRtStatsCDropped14_Type()
)
fgFwGtpRtStatsCDropped14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped14.setStatus("current")
_FgFwGtpRtStatsCDropped15_Type = Counter64
_FgFwGtpRtStatsCDropped15_Object = MibScalar
fgFwGtpRtStatsCDropped15 = _FgFwGtpRtStatsCDropped15_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 18),
    _FgFwGtpRtStatsCDropped15_Type()
)
fgFwGtpRtStatsCDropped15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped15.setStatus("current")
_FgFwGtpRtStatsCDropped16_Type = Counter64
_FgFwGtpRtStatsCDropped16_Object = MibScalar
fgFwGtpRtStatsCDropped16 = _FgFwGtpRtStatsCDropped16_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 19),
    _FgFwGtpRtStatsCDropped16_Type()
)
fgFwGtpRtStatsCDropped16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped16.setStatus("current")
_FgFwGtpRtStatsCDropped17_Type = Counter64
_FgFwGtpRtStatsCDropped17_Object = MibScalar
fgFwGtpRtStatsCDropped17 = _FgFwGtpRtStatsCDropped17_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 20),
    _FgFwGtpRtStatsCDropped17_Type()
)
fgFwGtpRtStatsCDropped17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped17.setStatus("current")
_FgFwGtpRtStatsCDropped18_Type = Counter64
_FgFwGtpRtStatsCDropped18_Object = MibScalar
fgFwGtpRtStatsCDropped18 = _FgFwGtpRtStatsCDropped18_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 21),
    _FgFwGtpRtStatsCDropped18_Type()
)
fgFwGtpRtStatsCDropped18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped18.setStatus("current")
_FgFwGtpRtStatsCDropped19_Type = Counter64
_FgFwGtpRtStatsCDropped19_Object = MibScalar
fgFwGtpRtStatsCDropped19 = _FgFwGtpRtStatsCDropped19_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 22),
    _FgFwGtpRtStatsCDropped19_Type()
)
fgFwGtpRtStatsCDropped19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped19.setStatus("current")
_FgFwGtpRtStatsCDropped20_Type = Counter64
_FgFwGtpRtStatsCDropped20_Object = MibScalar
fgFwGtpRtStatsCDropped20 = _FgFwGtpRtStatsCDropped20_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 23),
    _FgFwGtpRtStatsCDropped20_Type()
)
fgFwGtpRtStatsCDropped20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped20.setStatus("current")
_FgFwGtpRtStatsCDropped21_Type = Counter64
_FgFwGtpRtStatsCDropped21_Object = MibScalar
fgFwGtpRtStatsCDropped21 = _FgFwGtpRtStatsCDropped21_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 24),
    _FgFwGtpRtStatsCDropped21_Type()
)
fgFwGtpRtStatsCDropped21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped21.setStatus("current")
_FgFwGtpRtStatsCDropped22_Type = Counter64
_FgFwGtpRtStatsCDropped22_Object = MibScalar
fgFwGtpRtStatsCDropped22 = _FgFwGtpRtStatsCDropped22_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 25),
    _FgFwGtpRtStatsCDropped22_Type()
)
fgFwGtpRtStatsCDropped22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped22.setStatus("current")
_FgFwGtpRtStatsCDropped23_Type = Counter64
_FgFwGtpRtStatsCDropped23_Object = MibScalar
fgFwGtpRtStatsCDropped23 = _FgFwGtpRtStatsCDropped23_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 1, 26),
    _FgFwGtpRtStatsCDropped23_Type()
)
fgFwGtpRtStatsCDropped23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsCDropped23.setStatus("current")
_FgFwGtpRtStatsDPkts_ObjectIdentity = ObjectIdentity
fgFwGtpRtStatsDPkts = _FgFwGtpRtStatsDPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 2)
)
_FgFwGtpRtStatsDForwarded_Type = Counter64
_FgFwGtpRtStatsDForwarded_Object = MibScalar
fgFwGtpRtStatsDForwarded = _FgFwGtpRtStatsDForwarded_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 2, 1),
    _FgFwGtpRtStatsDForwarded_Type()
)
fgFwGtpRtStatsDForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsDForwarded.setStatus("current")
_FgFwGtpRtStatsDDroppedSanity_Type = Counter64
_FgFwGtpRtStatsDDroppedSanity_Object = MibScalar
fgFwGtpRtStatsDDroppedSanity = _FgFwGtpRtStatsDDroppedSanity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 2, 2),
    _FgFwGtpRtStatsDDroppedSanity_Type()
)
fgFwGtpRtStatsDDroppedSanity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsDDroppedSanity.setStatus("current")
_FgFwGtpRtStatsDDroppedMalMsg_Type = Counter64
_FgFwGtpRtStatsDDroppedMalMsg_Object = MibScalar
fgFwGtpRtStatsDDroppedMalMsg = _FgFwGtpRtStatsDDroppedMalMsg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 2, 3),
    _FgFwGtpRtStatsDDroppedMalMsg_Type()
)
fgFwGtpRtStatsDDroppedMalMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsDDroppedMalMsg.setStatus("current")
_FgFwGtpRtStatsDDroppedNoState_Type = Counter64
_FgFwGtpRtStatsDDroppedNoState_Object = MibScalar
fgFwGtpRtStatsDDroppedNoState = _FgFwGtpRtStatsDDroppedNoState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 2, 4),
    _FgFwGtpRtStatsDDroppedNoState_Type()
)
fgFwGtpRtStatsDDroppedNoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsDDroppedNoState.setStatus("current")
_FgFwGtpRtStatsDDroppedMalIe_Type = Counter64
_FgFwGtpRtStatsDDroppedMalIe_Object = MibScalar
fgFwGtpRtStatsDDroppedMalIe = _FgFwGtpRtStatsDDroppedMalIe_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 2, 5),
    _FgFwGtpRtStatsDDroppedMalIe_Type()
)
fgFwGtpRtStatsDDroppedMalIe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsDDroppedMalIe.setStatus("current")
_FgFwGtpRtStatsDDroppedGtpInGtp_Type = Counter64
_FgFwGtpRtStatsDDroppedGtpInGtp_Object = MibScalar
fgFwGtpRtStatsDDroppedGtpInGtp = _FgFwGtpRtStatsDDroppedGtpInGtp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 2, 6),
    _FgFwGtpRtStatsDDroppedGtpInGtp_Type()
)
fgFwGtpRtStatsDDroppedGtpInGtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsDDroppedGtpInGtp.setStatus("current")
_FgFwGtpRtStatsDDroppedSpoof_Type = Counter64
_FgFwGtpRtStatsDDroppedSpoof_Object = MibScalar
fgFwGtpRtStatsDDroppedSpoof = _FgFwGtpRtStatsDDroppedSpoof_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 2, 7),
    _FgFwGtpRtStatsDDroppedSpoof_Type()
)
fgFwGtpRtStatsDDroppedSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsDDroppedSpoof.setStatus("current")
_FgFwGtpRtStatsDDroppedIpPol_Type = Counter64
_FgFwGtpRtStatsDDroppedIpPol_Object = MibScalar
fgFwGtpRtStatsDDroppedIpPol = _FgFwGtpRtStatsDDroppedIpPol_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 2, 8),
    _FgFwGtpRtStatsDDroppedIpPol_Type()
)
fgFwGtpRtStatsDDroppedIpPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsDDroppedIpPol.setStatus("current")
_FgFwGtpRtStatsDDroppedMsgFilter_Type = Counter64
_FgFwGtpRtStatsDDroppedMsgFilter_Object = MibScalar
fgFwGtpRtStatsDDroppedMsgFilter = _FgFwGtpRtStatsDDroppedMsgFilter_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 2, 9),
    _FgFwGtpRtStatsDDroppedMsgFilter_Type()
)
fgFwGtpRtStatsDDroppedMsgFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsDDroppedMsgFilter.setStatus("current")
_FgFwGtpRtStatsDDroppedMsgRateLimit_Type = Counter64
_FgFwGtpRtStatsDDroppedMsgRateLimit_Object = MibScalar
fgFwGtpRtStatsDDroppedMsgRateLimit = _FgFwGtpRtStatsDDroppedMsgRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 2, 10),
    _FgFwGtpRtStatsDDroppedMsgRateLimit_Type()
)
fgFwGtpRtStatsDDroppedMsgRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsDDroppedMsgRateLimit.setStatus("current")
_FgFwGtpRtStatsDDroppedUnknownVersion_Type = Counter64
_FgFwGtpRtStatsDDroppedUnknownVersion_Object = MibScalar
fgFwGtpRtStatsDDroppedUnknownVersion = _FgFwGtpRtStatsDDroppedUnknownVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 2, 11),
    _FgFwGtpRtStatsDDroppedUnknownVersion_Type()
)
fgFwGtpRtStatsDDroppedUnknownVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsDDroppedUnknownVersion.setStatus("current")
_FgFwGtpRtStatsBPkts_ObjectIdentity = ObjectIdentity
fgFwGtpRtStatsBPkts = _FgFwGtpRtStatsBPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 3)
)
_FgFwGtpRtStatsBForwarded_Type = Counter64
_FgFwGtpRtStatsBForwarded_Object = MibScalar
fgFwGtpRtStatsBForwarded = _FgFwGtpRtStatsBForwarded_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 3, 1),
    _FgFwGtpRtStatsBForwarded_Type()
)
fgFwGtpRtStatsBForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsBForwarded.setStatus("current")
_FgFwGtpRtStatsBDroppedSanity_Type = Counter64
_FgFwGtpRtStatsBDroppedSanity_Object = MibScalar
fgFwGtpRtStatsBDroppedSanity = _FgFwGtpRtStatsBDroppedSanity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 3, 2),
    _FgFwGtpRtStatsBDroppedSanity_Type()
)
fgFwGtpRtStatsBDroppedSanity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsBDroppedSanity.setStatus("current")
_FgFwGtpRtStatsBDroppedMalMsg_Type = Counter64
_FgFwGtpRtStatsBDroppedMalMsg_Object = MibScalar
fgFwGtpRtStatsBDroppedMalMsg = _FgFwGtpRtStatsBDroppedMalMsg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 3, 3),
    _FgFwGtpRtStatsBDroppedMalMsg_Type()
)
fgFwGtpRtStatsBDroppedMalMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsBDroppedMalMsg.setStatus("current")
_FgFwGtpRtStatsBDroppedMalIe_Type = Counter64
_FgFwGtpRtStatsBDroppedMalIe_Object = MibScalar
fgFwGtpRtStatsBDroppedMalIe = _FgFwGtpRtStatsBDroppedMalIe_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 3, 4),
    _FgFwGtpRtStatsBDroppedMalIe_Type()
)
fgFwGtpRtStatsBDroppedMalIe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsBDroppedMalIe.setStatus("current")
_FgFwGtpRtStatsBDroppedMsgFilter_Type = Counter64
_FgFwGtpRtStatsBDroppedMsgFilter_Object = MibScalar
fgFwGtpRtStatsBDroppedMsgFilter = _FgFwGtpRtStatsBDroppedMsgFilter_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 4, 2, 3, 5),
    _FgFwGtpRtStatsBDroppedMsgFilter_Type()
)
fgFwGtpRtStatsBDroppedMsgFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwGtpRtStatsBDroppedMsgFilter.setStatus("current")
_FgFwAddresses_ObjectIdentity = ObjectIdentity
fgFwAddresses = _FgFwAddresses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 5)
)
_FgFwAddrTables_ObjectIdentity = ObjectIdentity
fgFwAddrTables = _FgFwAddrTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 5, 2)
)
_FgFwAddrDynEmsTable_Object = MibTable
fgFwAddrDynEmsTable = _FgFwAddrDynEmsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 5, 2, 1)
)
if mibBuilder.loadTexts:
    fgFwAddrDynEmsTable.setStatus("current")
_FgFwAddrDynEmsEntry_Object = MibTableRow
fgFwAddrDynEmsEntry = _FgFwAddrDynEmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 5, 2, 1, 1)
)
fgFwAddrDynEmsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgFwAddrDynEmsID"),
)
if mibBuilder.loadTexts:
    fgFwAddrDynEmsEntry.setStatus("current")
_FgFwAddrDynEmsID_Type = FnIndex
_FgFwAddrDynEmsID_Object = MibTableColumn
fgFwAddrDynEmsID = _FgFwAddrDynEmsID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 5, 2, 1, 1, 1),
    _FgFwAddrDynEmsID_Type()
)
fgFwAddrDynEmsID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgFwAddrDynEmsID.setStatus("current")
_FgFwAddrDynEmsName_Type = DisplayString
_FgFwAddrDynEmsName_Object = MibTableColumn
fgFwAddrDynEmsName = _FgFwAddrDynEmsName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 5, 2, 1, 1, 2),
    _FgFwAddrDynEmsName_Type()
)
fgFwAddrDynEmsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwAddrDynEmsName.setStatus("current")
_FgFwAddrDynEmsAddresses_Type = Unsigned32
_FgFwAddrDynEmsAddresses_Object = MibTableColumn
fgFwAddrDynEmsAddresses = _FgFwAddrDynEmsAddresses_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 5, 5, 2, 1, 1, 3),
    _FgFwAddrDynEmsAddresses_Type()
)
fgFwAddrDynEmsAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFwAddrDynEmsAddresses.setStatus("current")
_FgMgmt_ObjectIdentity = ObjectIdentity
fgMgmt = _FgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6)
)
_FgFmTrapPrefix_ObjectIdentity = ObjectIdentity
fgFmTrapPrefix = _FgFmTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 0)
)
_FgAdmin_ObjectIdentity = ObjectIdentity
fgAdmin = _FgAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1)
)
_FgAdminOptions_ObjectIdentity = ObjectIdentity
fgAdminOptions = _FgAdminOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1, 1)
)
_FgAdminIdleTimeout_Type = Integer32
_FgAdminIdleTimeout_Object = MibScalar
fgAdminIdleTimeout = _FgAdminIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1, 1, 1),
    _FgAdminIdleTimeout_Type()
)
fgAdminIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAdminIdleTimeout.setStatus("current")
_FgAdminLcdProtection_Type = FnBoolState
_FgAdminLcdProtection_Object = MibScalar
fgAdminLcdProtection = _FgAdminLcdProtection_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1, 1, 2),
    _FgAdminLcdProtection_Type()
)
fgAdminLcdProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAdminLcdProtection.setStatus("current")
_FgAdminTables_ObjectIdentity = ObjectIdentity
fgAdminTables = _FgAdminTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1, 2)
)
_FgAdminTable_Object = MibTable
fgAdminTable = _FgAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fgAdminTable.setStatus("current")
_FgAdminEntry_Object = MibTableRow
fgAdminEntry = _FgAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fgAdminEntry.setStatus("current")
_FgAdminVdom_Type = FgVdIndex
_FgAdminVdom_Object = MibTableColumn
fgAdminVdom = _FgAdminVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 1, 2, 1, 1, 1),
    _FgAdminVdom_Type()
)
fgAdminVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAdminVdom.setStatus("current")
_FgMgmtTrapObjects_ObjectIdentity = ObjectIdentity
fgMgmtTrapObjects = _FgMgmtTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 2)
)
_FgManIfIp_Type = IpAddress
_FgManIfIp_Object = MibScalar
fgManIfIp = _FgManIfIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 2, 1),
    _FgManIfIp_Type()
)
fgManIfIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgManIfIp.setStatus("current")
_FgManIfMask_Type = IpAddress
_FgManIfMask_Object = MibScalar
fgManIfMask = _FgManIfMask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 2, 2),
    _FgManIfMask_Type()
)
fgManIfMask.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgManIfMask.setStatus("current")
_FgManIfIp6_Type = Ipv6Address
_FgManIfIp6_Object = MibScalar
fgManIfIp6 = _FgManIfIp6_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 2, 3),
    _FgManIfIp6_Type()
)
fgManIfIp6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgManIfIp6.setStatus("current")


class _FgFazTrapType_Type(Integer32):
    """Custom type fgFazTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mainFailover", 1),
          ("altFailover", 2))
    )


_FgFazTrapType_Type.__name__ = "Integer32"
_FgFazTrapType_Object = MibScalar
fgFazTrapType = _FgFazTrapType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 2, 4),
    _FgFazTrapType_Type()
)
fgFazTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgFazTrapType.setStatus("current")
_FgIntf_ObjectIdentity = ObjectIdentity
fgIntf = _FgIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7)
)
_FgIntfInfo_ObjectIdentity = ObjectIdentity
fgIntfInfo = _FgIntfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 1)
)
_FgIntfTables_ObjectIdentity = ObjectIdentity
fgIntfTables = _FgIntfTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2)
)
_FgIntfTable_Object = MibTable
fgIntfTable = _FgIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2, 1)
)
if mibBuilder.loadTexts:
    fgIntfTable.setStatus("current")
_FgIntfEntry_Object = MibTableRow
fgIntfEntry = _FgIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fgIntfEntry.setStatus("current")
_FgIntfEntVdom_Type = FgVdIndex
_FgIntfEntVdom_Object = MibTableColumn
fgIntfEntVdom = _FgIntfEntVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2, 1, 1, 1),
    _FgIntfEntVdom_Type()
)
fgIntfEntVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfEntVdom.setStatus("current")
_FgIntfEntEstUpBandwidth_Type = Unsigned32
_FgIntfEntEstUpBandwidth_Object = MibTableColumn
fgIntfEntEstUpBandwidth = _FgIntfEntEstUpBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2, 1, 1, 2),
    _FgIntfEntEstUpBandwidth_Type()
)
fgIntfEntEstUpBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfEntEstUpBandwidth.setStatus("current")
_FgIntfEntEstDownBandwidth_Type = Unsigned32
_FgIntfEntEstDownBandwidth_Object = MibTableColumn
fgIntfEntEstDownBandwidth = _FgIntfEntEstDownBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2, 1, 1, 3),
    _FgIntfEntEstDownBandwidth_Type()
)
fgIntfEntEstDownBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfEntEstDownBandwidth.setStatus("current")
_FgIntfEntMeaUpBandwidth_Type = Unsigned32
_FgIntfEntMeaUpBandwidth_Object = MibTableColumn
fgIntfEntMeaUpBandwidth = _FgIntfEntMeaUpBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2, 1, 1, 4),
    _FgIntfEntMeaUpBandwidth_Type()
)
fgIntfEntMeaUpBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfEntMeaUpBandwidth.setStatus("current")
_FgIntfEntMeaDownBandwidth_Type = Unsigned32
_FgIntfEntMeaDownBandwidth_Object = MibTableColumn
fgIntfEntMeaDownBandwidth = _FgIntfEntMeaDownBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2, 1, 1, 5),
    _FgIntfEntMeaDownBandwidth_Type()
)
fgIntfEntMeaDownBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfEntMeaDownBandwidth.setStatus("current")
_FgIntfVlanTable_Object = MibTable
fgIntfVlanTable = _FgIntfVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2, 2)
)
if mibBuilder.loadTexts:
    fgIntfVlanTable.setStatus("current")
_FgIntfVlanEntry_Object = MibTableRow
fgIntfVlanEntry = _FgIntfVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2, 2, 1)
)
fgIntfVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fgIntfVlanEntry.setStatus("current")
_FgIntfVlanName_Type = DisplayString
_FgIntfVlanName_Object = MibTableColumn
fgIntfVlanName = _FgIntfVlanName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2, 2, 1, 1),
    _FgIntfVlanName_Type()
)
fgIntfVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVlanName.setStatus("current")
_FgIntfVlanID_Type = Unsigned32
_FgIntfVlanID_Object = MibTableColumn
fgIntfVlanID = _FgIntfVlanID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2, 2, 1, 2),
    _FgIntfVlanID_Type()
)
fgIntfVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVlanID.setStatus("current")
_FgIntfVlanPhyName_Type = DisplayString
_FgIntfVlanPhyName_Object = MibTableColumn
fgIntfVlanPhyName = _FgIntfVlanPhyName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 2, 2, 1, 3),
    _FgIntfVlanPhyName_Type()
)
fgIntfVlanPhyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVlanPhyName.setStatus("current")
_FgIntfVrrps_ObjectIdentity = ObjectIdentity
fgIntfVrrps = _FgIntfVrrps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3)
)
_FgIntfVrrpCount_Type = Integer32
_FgIntfVrrpCount_Object = MibScalar
fgIntfVrrpCount = _FgIntfVrrpCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 1),
    _FgIntfVrrpCount_Type()
)
fgIntfVrrpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVrrpCount.setStatus("current")
_FgIntfVrrpTable_Object = MibTable
fgIntfVrrpTable = _FgIntfVrrpTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2)
)
if mibBuilder.loadTexts:
    fgIntfVrrpTable.setStatus("current")
_FgIntfVrrpEntry_Object = MibTableRow
fgIntfVrrpEntry = _FgIntfVrrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2, 1)
)
fgIntfVrrpEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgIntfVrrpEntIndex"),
)
if mibBuilder.loadTexts:
    fgIntfVrrpEntry.setStatus("current")
_FgIntfVrrpEntIndex_Type = FnIndex
_FgIntfVrrpEntIndex_Object = MibTableColumn
fgIntfVrrpEntIndex = _FgIntfVrrpEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2, 1, 1),
    _FgIntfVrrpEntIndex_Type()
)
fgIntfVrrpEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgIntfVrrpEntIndex.setStatus("current")
_FgIntfVrrpEntVrId_Type = FnIndex
_FgIntfVrrpEntVrId_Object = MibTableColumn
fgIntfVrrpEntVrId = _FgIntfVrrpEntVrId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2, 1, 2),
    _FgIntfVrrpEntVrId_Type()
)
fgIntfVrrpEntVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVrrpEntVrId.setStatus("current")
_FgIntfVrrpEntGrpId_Type = FnIndex
_FgIntfVrrpEntGrpId_Object = MibTableColumn
fgIntfVrrpEntGrpId = _FgIntfVrrpEntGrpId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2, 1, 3),
    _FgIntfVrrpEntGrpId_Type()
)
fgIntfVrrpEntGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVrrpEntGrpId.setStatus("current")
_FgIntfVrrpEntIfName_Type = DisplayString
_FgIntfVrrpEntIfName_Object = MibTableColumn
fgIntfVrrpEntIfName = _FgIntfVrrpEntIfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2, 1, 4),
    _FgIntfVrrpEntIfName_Type()
)
fgIntfVrrpEntIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVrrpEntIfName.setStatus("current")


class _FgIntfVrrpEntState_Type(Integer32):
    """Custom type fgIntfVrrpEntState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("master", 2))
    )


_FgIntfVrrpEntState_Type.__name__ = "Integer32"
_FgIntfVrrpEntState_Object = MibTableColumn
fgIntfVrrpEntState = _FgIntfVrrpEntState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2, 1, 5),
    _FgIntfVrrpEntState_Type()
)
fgIntfVrrpEntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVrrpEntState.setStatus("current")
_FgIntfVrrpEntVrIp_Type = IpAddress
_FgIntfVrrpEntVrIp_Object = MibTableColumn
fgIntfVrrpEntVrIp = _FgIntfVrrpEntVrIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 3, 2, 1, 6),
    _FgIntfVrrpEntVrIp_Type()
)
fgIntfVrrpEntVrIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVrrpEntVrIp.setStatus("current")
_FgIntfVlanHbs_ObjectIdentity = ObjectIdentity
fgIntfVlanHbs = _FgIntfVlanHbs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4)
)
_FgIntfVlanHbCount_Type = Integer32
_FgIntfVlanHbCount_Object = MibScalar
fgIntfVlanHbCount = _FgIntfVlanHbCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4, 1),
    _FgIntfVlanHbCount_Type()
)
fgIntfVlanHbCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVlanHbCount.setStatus("current")
_FgIntfVlanHbTable_Object = MibTable
fgIntfVlanHbTable = _FgIntfVlanHbTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4, 2)
)
if mibBuilder.loadTexts:
    fgIntfVlanHbTable.setStatus("current")
_FgIntfVlanHbEntry_Object = MibTableRow
fgIntfVlanHbEntry = _FgIntfVlanHbEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4, 2, 1)
)
fgIntfVlanHbEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgIntfVlanHbEntIndex"),
)
if mibBuilder.loadTexts:
    fgIntfVlanHbEntry.setStatus("current")
_FgIntfVlanHbEntIndex_Type = FnIndex
_FgIntfVlanHbEntIndex_Object = MibTableColumn
fgIntfVlanHbEntIndex = _FgIntfVlanHbEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4, 2, 1, 1),
    _FgIntfVlanHbEntIndex_Type()
)
fgIntfVlanHbEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgIntfVlanHbEntIndex.setStatus("current")
_FgIntfVlanHbEntIfName_Type = DisplayString
_FgIntfVlanHbEntIfName_Object = MibTableColumn
fgIntfVlanHbEntIfName = _FgIntfVlanHbEntIfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4, 2, 1, 2),
    _FgIntfVlanHbEntIfName_Type()
)
fgIntfVlanHbEntIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVlanHbEntIfName.setStatus("current")
_FgIntfVlanHbEntSerial_Type = DisplayString
_FgIntfVlanHbEntSerial_Object = MibTableColumn
fgIntfVlanHbEntSerial = _FgIntfVlanHbEntSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4, 2, 1, 3),
    _FgIntfVlanHbEntSerial_Type()
)
fgIntfVlanHbEntSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVlanHbEntSerial.setStatus("current")


class _FgIntfVlanHbEntState_Type(Integer32):
    """Custom type fgIntfVlanHbEntState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_FgIntfVlanHbEntState_Type.__name__ = "Integer32"
_FgIntfVlanHbEntState_Object = MibTableColumn
fgIntfVlanHbEntState = _FgIntfVlanHbEntState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 4, 2, 1, 4),
    _FgIntfVlanHbEntState_Type()
)
fgIntfVlanHbEntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfVlanHbEntState.setStatus("current")
_FgIntfBcs_ObjectIdentity = ObjectIdentity
fgIntfBcs = _FgIntfBcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5)
)
_FgIntfBcTable_Object = MibTable
fgIntfBcTable = _FgIntfBcTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 2)
)
if mibBuilder.loadTexts:
    fgIntfBcTable.setStatus("current")
_FgIntfBcEntry_Object = MibTableRow
fgIntfBcEntry = _FgIntfBcEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 2, 1)
)
fgIntfBcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fgIntfBcEntry.setStatus("current")
_FgIntfBcAllocatedBandwidth_Type = Integer32
_FgIntfBcAllocatedBandwidth_Object = MibTableColumn
fgIntfBcAllocatedBandwidth = _FgIntfBcAllocatedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 2, 1, 1),
    _FgIntfBcAllocatedBandwidth_Type()
)
fgIntfBcAllocatedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcAllocatedBandwidth.setStatus("current")
_FgIntfBcGuaranteedBandwidth_Type = Integer32
_FgIntfBcGuaranteedBandwidth_Object = MibTableColumn
fgIntfBcGuaranteedBandwidth = _FgIntfBcGuaranteedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 2, 1, 2),
    _FgIntfBcGuaranteedBandwidth_Type()
)
fgIntfBcGuaranteedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcGuaranteedBandwidth.setStatus("current")
_FgIntfBcMaxBandwidth_Type = Integer32
_FgIntfBcMaxBandwidth_Object = MibTableColumn
fgIntfBcMaxBandwidth = _FgIntfBcMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 2, 1, 3),
    _FgIntfBcMaxBandwidth_Type()
)
fgIntfBcMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcMaxBandwidth.setStatus("current")
_FgIntfBcCurrentBandwidth_Type = Integer32
_FgIntfBcCurrentBandwidth_Object = MibTableColumn
fgIntfBcCurrentBandwidth = _FgIntfBcCurrentBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 2, 1, 4),
    _FgIntfBcCurrentBandwidth_Type()
)
fgIntfBcCurrentBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCurrentBandwidth.setStatus("current")
_FgIntfBcBytes_Type = Counter64
_FgIntfBcBytes_Object = MibTableColumn
fgIntfBcBytes = _FgIntfBcBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 2, 1, 5),
    _FgIntfBcBytes_Type()
)
fgIntfBcBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcBytes.setStatus("current")
_FgIntfBcDrops_Type = Counter64
_FgIntfBcDrops_Object = MibTableColumn
fgIntfBcDrops = _FgIntfBcDrops_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 2, 1, 6),
    _FgIntfBcDrops_Type()
)
fgIntfBcDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcDrops.setStatus("current")
_FgIntfBcInTable_Object = MibTable
fgIntfBcInTable = _FgIntfBcInTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 3)
)
if mibBuilder.loadTexts:
    fgIntfBcInTable.setStatus("current")
_FgIntfBcInEntry_Object = MibTableRow
fgIntfBcInEntry = _FgIntfBcInEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 3, 1)
)
fgIntfBcInEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fgIntfBcInEntry.setStatus("current")
_FgIntfBcInAllocatedBandwidth_Type = Integer32
_FgIntfBcInAllocatedBandwidth_Object = MibTableColumn
fgIntfBcInAllocatedBandwidth = _FgIntfBcInAllocatedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 3, 1, 1),
    _FgIntfBcInAllocatedBandwidth_Type()
)
fgIntfBcInAllocatedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcInAllocatedBandwidth.setStatus("current")
_FgIntfBcInGuaranteedBandwidth_Type = Integer32
_FgIntfBcInGuaranteedBandwidth_Object = MibTableColumn
fgIntfBcInGuaranteedBandwidth = _FgIntfBcInGuaranteedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 3, 1, 2),
    _FgIntfBcInGuaranteedBandwidth_Type()
)
fgIntfBcInGuaranteedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcInGuaranteedBandwidth.setStatus("current")
_FgIntfBcInMaxBandwidth_Type = Integer32
_FgIntfBcInMaxBandwidth_Object = MibTableColumn
fgIntfBcInMaxBandwidth = _FgIntfBcInMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 3, 1, 3),
    _FgIntfBcInMaxBandwidth_Type()
)
fgIntfBcInMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcInMaxBandwidth.setStatus("current")
_FgIntfBcInCurrentBandwidth_Type = Integer32
_FgIntfBcInCurrentBandwidth_Object = MibTableColumn
fgIntfBcInCurrentBandwidth = _FgIntfBcInCurrentBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 3, 1, 4),
    _FgIntfBcInCurrentBandwidth_Type()
)
fgIntfBcInCurrentBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcInCurrentBandwidth.setStatus("current")
_FgIntfBcInBytes_Type = Counter64
_FgIntfBcInBytes_Object = MibTableColumn
fgIntfBcInBytes = _FgIntfBcInBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 3, 1, 5),
    _FgIntfBcInBytes_Type()
)
fgIntfBcInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcInBytes.setStatus("current")
_FgIntfBcInDrops_Type = Counter64
_FgIntfBcInDrops_Object = MibTableColumn
fgIntfBcInDrops = _FgIntfBcInDrops_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 3, 1, 6),
    _FgIntfBcInDrops_Type()
)
fgIntfBcInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcInDrops.setStatus("current")
_FgIntfBcQTable_Object = MibTable
fgIntfBcQTable = _FgIntfBcQTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 4)
)
if mibBuilder.loadTexts:
    fgIntfBcQTable.setStatus("current")
_FgIntfBcQEntry_Object = MibTableRow
fgIntfBcQEntry = _FgIntfBcQEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 4, 1)
)
fgIntfBcQEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fgIntfBcQEntry.setStatus("current")
_FgIntfBcQPackets_Type = Counter64
_FgIntfBcQPackets_Object = MibTableColumn
fgIntfBcQPackets = _FgIntfBcQPackets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 4, 1, 1),
    _FgIntfBcQPackets_Type()
)
fgIntfBcQPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcQPackets.setStatus("current")
_FgIntfBcQBytes_Type = Counter64
_FgIntfBcQBytes_Object = MibTableColumn
fgIntfBcQBytes = _FgIntfBcQBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 4, 1, 2),
    _FgIntfBcQBytes_Type()
)
fgIntfBcQBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcQBytes.setStatus("current")
_FgIntfBcQPDrops_Type = Counter64
_FgIntfBcQPDrops_Object = MibTableColumn
fgIntfBcQPDrops = _FgIntfBcQPDrops_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 4, 1, 3),
    _FgIntfBcQPDrops_Type()
)
fgIntfBcQPDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcQPDrops.setStatus("current")
_FgIntfBcQBDrops_Type = Counter64
_FgIntfBcQBDrops_Object = MibTableColumn
fgIntfBcQBDrops = _FgIntfBcQBDrops_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 4, 1, 4),
    _FgIntfBcQBDrops_Type()
)
fgIntfBcQBDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcQBDrops.setStatus("current")
_FgIntfBcCfgTables_ObjectIdentity = ObjectIdentity
fgIntfBcCfgTables = _FgIntfBcCfgTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5)
)
_FgIntfBcCfgIfTable_Object = MibTable
fgIntfBcCfgIfTable = _FgIntfBcCfgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 1)
)
if mibBuilder.loadTexts:
    fgIntfBcCfgIfTable.setStatus("current")
_FgIntfBcCfgIfEntry_Object = MibTableRow
fgIntfBcCfgIfEntry = _FgIntfBcCfgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 1, 1)
)
fgIntfBcCfgIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fgIntfBcCfgIfEntry.setStatus("current")
_FgIntfBcCfgIfName_Type = DisplayString
_FgIntfBcCfgIfName_Object = MibTableColumn
fgIntfBcCfgIfName = _FgIntfBcCfgIfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 1, 1, 1),
    _FgIntfBcCfgIfName_Type()
)
fgIntfBcCfgIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgIfName.setStatus("current")
_FgIntfBcCfgIfEgressSProfile_Type = DisplayString
_FgIntfBcCfgIfEgressSProfile_Object = MibTableColumn
fgIntfBcCfgIfEgressSProfile = _FgIntfBcCfgIfEgressSProfile_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 1, 1, 2),
    _FgIntfBcCfgIfEgressSProfile_Type()
)
fgIntfBcCfgIfEgressSProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgIfEgressSProfile.setStatus("current")
_FgIntfBcCfgIfIngressSProfile_Type = DisplayString
_FgIntfBcCfgIfIngressSProfile_Object = MibTableColumn
fgIntfBcCfgIfIngressSProfile = _FgIntfBcCfgIfIngressSProfile_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 1, 1, 3),
    _FgIntfBcCfgIfIngressSProfile_Type()
)
fgIntfBcCfgIfIngressSProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgIfIngressSProfile.setStatus("current")
_FgIntfBcCfgIfEstUpBandwidth_Type = Unsigned32
_FgIntfBcCfgIfEstUpBandwidth_Object = MibTableColumn
fgIntfBcCfgIfEstUpBandwidth = _FgIntfBcCfgIfEstUpBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 1, 1, 4),
    _FgIntfBcCfgIfEstUpBandwidth_Type()
)
fgIntfBcCfgIfEstUpBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgIfEstUpBandwidth.setStatus("current")
_FgIntfBcCfgIfEstDownBandwidth_Type = Unsigned32
_FgIntfBcCfgIfEstDownBandwidth_Object = MibTableColumn
fgIntfBcCfgIfEstDownBandwidth = _FgIntfBcCfgIfEstDownBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 1, 1, 5),
    _FgIntfBcCfgIfEstDownBandwidth_Type()
)
fgIntfBcCfgIfEstDownBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgIfEstDownBandwidth.setStatus("current")
_FgIntfBcCfgIfInBandwidth_Type = Unsigned32
_FgIntfBcCfgIfInBandwidth_Object = MibTableColumn
fgIntfBcCfgIfInBandwidth = _FgIntfBcCfgIfInBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 1, 1, 6),
    _FgIntfBcCfgIfInBandwidth_Type()
)
fgIntfBcCfgIfInBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgIfInBandwidth.setStatus("current")
_FgIntfBcCfgIfOutBandwidth_Type = Unsigned32
_FgIntfBcCfgIfOutBandwidth_Object = MibTableColumn
fgIntfBcCfgIfOutBandwidth = _FgIntfBcCfgIfOutBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 1, 1, 7),
    _FgIntfBcCfgIfOutBandwidth_Type()
)
fgIntfBcCfgIfOutBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgIfOutBandwidth.setStatus("current")
_FgIntfBcCfgSproTable_Object = MibTable
fgIntfBcCfgSproTable = _FgIntfBcCfgSproTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 2)
)
if mibBuilder.loadTexts:
    fgIntfBcCfgSproTable.setStatus("current")
_FgIntfBcCfgSproEntry_Object = MibTableRow
fgIntfBcCfgSproEntry = _FgIntfBcCfgSproEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 2, 1)
)
fgIntfBcCfgSproEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSproID"),
)
if mibBuilder.loadTexts:
    fgIntfBcCfgSproEntry.setStatus("current")
_FgIntfBcCfgSproID_Type = FnIndex
_FgIntfBcCfgSproID_Object = MibTableColumn
fgIntfBcCfgSproID = _FgIntfBcCfgSproID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 2, 1, 1),
    _FgIntfBcCfgSproID_Type()
)
fgIntfBcCfgSproID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgIntfBcCfgSproID.setStatus("current")
_FgIntfBcCfgSproName_Type = DisplayString
_FgIntfBcCfgSproName_Object = MibTableColumn
fgIntfBcCfgSproName = _FgIntfBcCfgSproName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 2, 1, 2),
    _FgIntfBcCfgSproName_Type()
)
fgIntfBcCfgSproName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgSproName.setStatus("current")


class _FgIntfBcCfgSproType_Type(Integer32):
    """Custom type fgIntfBcCfgSproType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("policing", 0),
          ("queueing", 1))
    )


_FgIntfBcCfgSproType_Type.__name__ = "Integer32"
_FgIntfBcCfgSproType_Object = MibTableColumn
fgIntfBcCfgSproType = _FgIntfBcCfgSproType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 2, 1, 3),
    _FgIntfBcCfgSproType_Type()
)
fgIntfBcCfgSproType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgSproType.setStatus("current")
_FgIntfBcCfgSproDefaultClassId_Type = Unsigned32
_FgIntfBcCfgSproDefaultClassId_Object = MibTableColumn
fgIntfBcCfgSproDefaultClassId = _FgIntfBcCfgSproDefaultClassId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 2, 1, 4),
    _FgIntfBcCfgSproDefaultClassId_Type()
)
fgIntfBcCfgSproDefaultClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgSproDefaultClassId.setStatus("current")
_FgIntfBcCfgSproClassNum_Type = Unsigned32
_FgIntfBcCfgSproClassNum_Object = MibTableColumn
fgIntfBcCfgSproClassNum = _FgIntfBcCfgSproClassNum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 2, 1, 5),
    _FgIntfBcCfgSproClassNum_Type()
)
fgIntfBcCfgSproClassNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgSproClassNum.setStatus("current")
_FgIntfBcCfgSentTable_Object = MibTable
fgIntfBcCfgSentTable = _FgIntfBcCfgSentTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 3)
)
if mibBuilder.loadTexts:
    fgIntfBcCfgSentTable.setStatus("current")
_FgIntfBcCfgSentEntry_Object = MibTableRow
fgIntfBcCfgSentEntry = _FgIntfBcCfgSentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 3, 1)
)
fgIntfBcCfgSentEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSproID"),
    (0, "FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSentClassID"),
)
if mibBuilder.loadTexts:
    fgIntfBcCfgSentEntry.setStatus("current")
_FgIntfBcCfgSentClassID_Type = FnIndex
_FgIntfBcCfgSentClassID_Object = MibTableColumn
fgIntfBcCfgSentClassID = _FgIntfBcCfgSentClassID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 3, 1, 1),
    _FgIntfBcCfgSentClassID_Type()
)
fgIntfBcCfgSentClassID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgIntfBcCfgSentClassID.setStatus("current")
_FgIntfBcCfgSentClassName_Type = DisplayString
_FgIntfBcCfgSentClassName_Object = MibTableColumn
fgIntfBcCfgSentClassName = _FgIntfBcCfgSentClassName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 3, 1, 2),
    _FgIntfBcCfgSentClassName_Type()
)
fgIntfBcCfgSentClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgSentClassName.setStatus("current")
_FgIntfBcCfgSentGuaranteedBandwidth_Type = Integer32
_FgIntfBcCfgSentGuaranteedBandwidth_Object = MibTableColumn
fgIntfBcCfgSentGuaranteedBandwidth = _FgIntfBcCfgSentGuaranteedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 3, 1, 3),
    _FgIntfBcCfgSentGuaranteedBandwidth_Type()
)
fgIntfBcCfgSentGuaranteedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgSentGuaranteedBandwidth.setStatus("current")
_FgIntfBcCfgSentMaxBandwidth_Type = Integer32
_FgIntfBcCfgSentMaxBandwidth_Object = MibTableColumn
fgIntfBcCfgSentMaxBandwidth = _FgIntfBcCfgSentMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 3, 1, 4),
    _FgIntfBcCfgSentMaxBandwidth_Type()
)
fgIntfBcCfgSentMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgSentMaxBandwidth.setStatus("current")
_FgIntfBcCfgSpolTable_Object = MibTable
fgIntfBcCfgSpolTable = _FgIntfBcCfgSpolTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 4)
)
if mibBuilder.loadTexts:
    fgIntfBcCfgSpolTable.setStatus("current")
_FgIntfBcCfgSpolEntry_Object = MibTableRow
fgIntfBcCfgSpolEntry = _FgIntfBcCfgSpolEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 4, 1)
)
fgIntfBcCfgSpolEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSpolID"),
)
if mibBuilder.loadTexts:
    fgIntfBcCfgSpolEntry.setStatus("current")
_FgIntfBcCfgSpolID_Type = FnIndex
_FgIntfBcCfgSpolID_Object = MibTableColumn
fgIntfBcCfgSpolID = _FgIntfBcCfgSpolID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 4, 1, 1),
    _FgIntfBcCfgSpolID_Type()
)
fgIntfBcCfgSpolID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgIntfBcCfgSpolID.setStatus("current")
_FgIntfBcCfgSpolSrcaddr_Type = DisplayString
_FgIntfBcCfgSpolSrcaddr_Object = MibTableColumn
fgIntfBcCfgSpolSrcaddr = _FgIntfBcCfgSpolSrcaddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 4, 1, 2),
    _FgIntfBcCfgSpolSrcaddr_Type()
)
fgIntfBcCfgSpolSrcaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgSpolSrcaddr.setStatus("current")
_FgIntfBcCfgSpolDstaddr_Type = DisplayString
_FgIntfBcCfgSpolDstaddr_Object = MibTableColumn
fgIntfBcCfgSpolDstaddr = _FgIntfBcCfgSpolDstaddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 4, 1, 3),
    _FgIntfBcCfgSpolDstaddr_Type()
)
fgIntfBcCfgSpolDstaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgSpolDstaddr.setStatus("current")
_FgIntfBcCfgSpolSvr_Type = DisplayString
_FgIntfBcCfgSpolSvr_Object = MibTableColumn
fgIntfBcCfgSpolSvr = _FgIntfBcCfgSpolSvr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 4, 1, 4),
    _FgIntfBcCfgSpolSvr_Type()
)
fgIntfBcCfgSpolSvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgSpolSvr.setStatus("current")
_FgIntfBcCfgSpolComment_Type = DisplayString
_FgIntfBcCfgSpolComment_Object = MibTableColumn
fgIntfBcCfgSpolComment = _FgIntfBcCfgSpolComment_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 4, 1, 5),
    _FgIntfBcCfgSpolComment_Type()
)
fgIntfBcCfgSpolComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgSpolComment.setStatus("current")
_FgIntfBcCfgSpolClassName_Type = DisplayString
_FgIntfBcCfgSpolClassName_Object = MibTableColumn
fgIntfBcCfgSpolClassName = _FgIntfBcCfgSpolClassName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 5, 5, 4, 1, 6),
    _FgIntfBcCfgSpolClassName_Type()
)
fgIntfBcCfgSpolClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIntfBcCfgSpolClassName.setStatus("current")
_FgIntfTrapObjects_ObjectIdentity = ObjectIdentity
fgIntfTrapObjects = _FgIntfTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 6)
)


class _FgIntfTrapType_Type(Integer32):
    """Custom type fgIntfTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipConflict", 1)
    )


_FgIntfTrapType_Type.__name__ = "Integer32"
_FgIntfTrapType_Object = MibScalar
fgIntfTrapType = _FgIntfTrapType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 7, 6, 1),
    _FgIntfTrapType_Type()
)
fgIntfTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgIntfTrapType.setStatus("current")
_FgAntivirus_ObjectIdentity = ObjectIdentity
fgAntivirus = _FgAntivirus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8)
)
_FgAvInfo_ObjectIdentity = ObjectIdentity
fgAvInfo = _FgAvInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 1)
)
_FgAvTables_ObjectIdentity = ObjectIdentity
fgAvTables = _FgAvTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2)
)
_FgAvStatsTable_Object = MibTable
fgAvStatsTable = _FgAvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1)
)
if mibBuilder.loadTexts:
    fgAvStatsTable.setStatus("current")
_FgAvStatsEntry_Object = MibTableRow
fgAvStatsEntry = _FgAvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fgAvStatsEntry.setStatus("current")
_FgAvVirusDetected_Type = Counter32
_FgAvVirusDetected_Object = MibTableColumn
fgAvVirusDetected = _FgAvVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 1),
    _FgAvVirusDetected_Type()
)
fgAvVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvVirusDetected.setStatus("current")
_FgAvVirusBlocked_Type = Counter32
_FgAvVirusBlocked_Object = MibTableColumn
fgAvVirusBlocked = _FgAvVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 2),
    _FgAvVirusBlocked_Type()
)
fgAvVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvVirusBlocked.setStatus("current")
_FgAvHTTPVirusDetected_Type = Counter32
_FgAvHTTPVirusDetected_Object = MibTableColumn
fgAvHTTPVirusDetected = _FgAvHTTPVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 3),
    _FgAvHTTPVirusDetected_Type()
)
fgAvHTTPVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvHTTPVirusDetected.setStatus("current")
_FgAvHTTPVirusBlocked_Type = Counter32
_FgAvHTTPVirusBlocked_Object = MibTableColumn
fgAvHTTPVirusBlocked = _FgAvHTTPVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 4),
    _FgAvHTTPVirusBlocked_Type()
)
fgAvHTTPVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvHTTPVirusBlocked.setStatus("current")
_FgAvSMTPVirusDetected_Type = Counter32
_FgAvSMTPVirusDetected_Object = MibTableColumn
fgAvSMTPVirusDetected = _FgAvSMTPVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 5),
    _FgAvSMTPVirusDetected_Type()
)
fgAvSMTPVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvSMTPVirusDetected.setStatus("current")
_FgAvSMTPVirusBlocked_Type = Counter32
_FgAvSMTPVirusBlocked_Object = MibTableColumn
fgAvSMTPVirusBlocked = _FgAvSMTPVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 6),
    _FgAvSMTPVirusBlocked_Type()
)
fgAvSMTPVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvSMTPVirusBlocked.setStatus("current")
_FgAvPOP3VirusDetected_Type = Counter32
_FgAvPOP3VirusDetected_Object = MibTableColumn
fgAvPOP3VirusDetected = _FgAvPOP3VirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 7),
    _FgAvPOP3VirusDetected_Type()
)
fgAvPOP3VirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvPOP3VirusDetected.setStatus("current")
_FgAvPOP3VirusBlocked_Type = Counter32
_FgAvPOP3VirusBlocked_Object = MibTableColumn
fgAvPOP3VirusBlocked = _FgAvPOP3VirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 8),
    _FgAvPOP3VirusBlocked_Type()
)
fgAvPOP3VirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvPOP3VirusBlocked.setStatus("current")
_FgAvIMAPVirusDetected_Type = Counter32
_FgAvIMAPVirusDetected_Object = MibTableColumn
fgAvIMAPVirusDetected = _FgAvIMAPVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 9),
    _FgAvIMAPVirusDetected_Type()
)
fgAvIMAPVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvIMAPVirusDetected.setStatus("current")
_FgAvIMAPVirusBlocked_Type = Counter32
_FgAvIMAPVirusBlocked_Object = MibTableColumn
fgAvIMAPVirusBlocked = _FgAvIMAPVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 10),
    _FgAvIMAPVirusBlocked_Type()
)
fgAvIMAPVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvIMAPVirusBlocked.setStatus("current")
_FgAvFTPVirusDetected_Type = Counter32
_FgAvFTPVirusDetected_Object = MibTableColumn
fgAvFTPVirusDetected = _FgAvFTPVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 11),
    _FgAvFTPVirusDetected_Type()
)
fgAvFTPVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvFTPVirusDetected.setStatus("current")
_FgAvFTPVirusBlocked_Type = Counter32
_FgAvFTPVirusBlocked_Object = MibTableColumn
fgAvFTPVirusBlocked = _FgAvFTPVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 12),
    _FgAvFTPVirusBlocked_Type()
)
fgAvFTPVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvFTPVirusBlocked.setStatus("current")
_FgAvIMVirusDetected_Type = Counter32
_FgAvIMVirusDetected_Object = MibTableColumn
fgAvIMVirusDetected = _FgAvIMVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 13),
    _FgAvIMVirusDetected_Type()
)
fgAvIMVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvIMVirusDetected.setStatus("current")
_FgAvIMVirusBlocked_Type = Counter32
_FgAvIMVirusBlocked_Object = MibTableColumn
fgAvIMVirusBlocked = _FgAvIMVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 14),
    _FgAvIMVirusBlocked_Type()
)
fgAvIMVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvIMVirusBlocked.setStatus("current")
_FgAvNNTPVirusDetected_Type = Counter32
_FgAvNNTPVirusDetected_Object = MibTableColumn
fgAvNNTPVirusDetected = _FgAvNNTPVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 15),
    _FgAvNNTPVirusDetected_Type()
)
fgAvNNTPVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvNNTPVirusDetected.setStatus("current")
_FgAvNNTPVirusBlocked_Type = Counter32
_FgAvNNTPVirusBlocked_Object = MibTableColumn
fgAvNNTPVirusBlocked = _FgAvNNTPVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 16),
    _FgAvNNTPVirusBlocked_Type()
)
fgAvNNTPVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvNNTPVirusBlocked.setStatus("current")
_FgAvOversizedDetected_Type = Counter32
_FgAvOversizedDetected_Object = MibTableColumn
fgAvOversizedDetected = _FgAvOversizedDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 17),
    _FgAvOversizedDetected_Type()
)
fgAvOversizedDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvOversizedDetected.setStatus("current")
_FgAvOversizedBlocked_Type = Counter32
_FgAvOversizedBlocked_Object = MibTableColumn
fgAvOversizedBlocked = _FgAvOversizedBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 18),
    _FgAvOversizedBlocked_Type()
)
fgAvOversizedBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvOversizedBlocked.setStatus("current")
_FgAvMAPIVirusDetected_Type = Counter32
_FgAvMAPIVirusDetected_Object = MibTableColumn
fgAvMAPIVirusDetected = _FgAvMAPIVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 19),
    _FgAvMAPIVirusDetected_Type()
)
fgAvMAPIVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvMAPIVirusDetected.setStatus("current")
_FgAvMAPIVirusBlocked_Type = Counter32
_FgAvMAPIVirusBlocked_Object = MibTableColumn
fgAvMAPIVirusBlocked = _FgAvMAPIVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 20),
    _FgAvMAPIVirusBlocked_Type()
)
fgAvMAPIVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvMAPIVirusBlocked.setStatus("current")
_FgAvSMBVirusDetected_Type = Counter32
_FgAvSMBVirusDetected_Object = MibTableColumn
fgAvSMBVirusDetected = _FgAvSMBVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 21),
    _FgAvSMBVirusDetected_Type()
)
fgAvSMBVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvSMBVirusDetected.setStatus("current")
_FgAvSMBVirusBlocked_Type = Counter32
_FgAvSMBVirusBlocked_Object = MibTableColumn
fgAvSMBVirusBlocked = _FgAvSMBVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 2, 1, 1, 22),
    _FgAvSMBVirusBlocked_Type()
)
fgAvSMBVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAvSMBVirusBlocked.setStatus("current")
_FgAvTrapObjects_ObjectIdentity = ObjectIdentity
fgAvTrapObjects = _FgAvTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 3)
)
_FgAvTrapVirName_Type = DisplayString
_FgAvTrapVirName_Object = MibScalar
fgAvTrapVirName = _FgAvTrapVirName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 8, 3, 1),
    _FgAvTrapVirName_Type()
)
fgAvTrapVirName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgAvTrapVirName.setStatus("current")
_FgIps_ObjectIdentity = ObjectIdentity
fgIps = _FgIps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9)
)
_FgIpsInfo_ObjectIdentity = ObjectIdentity
fgIpsInfo = _FgIpsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 1)
)
_FgIpsTables_ObjectIdentity = ObjectIdentity
fgIpsTables = _FgIpsTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2)
)
_FgIpsStatsTable_Object = MibTable
fgIpsStatsTable = _FgIpsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1)
)
if mibBuilder.loadTexts:
    fgIpsStatsTable.setStatus("current")
_FgIpsStatsEntry_Object = MibTableRow
fgIpsStatsEntry = _FgIpsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fgIpsStatsEntry.setStatus("current")
_FgIpsIntrusionsDetected_Type = Counter32
_FgIpsIntrusionsDetected_Object = MibTableColumn
fgIpsIntrusionsDetected = _FgIpsIntrusionsDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 1),
    _FgIpsIntrusionsDetected_Type()
)
fgIpsIntrusionsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsIntrusionsDetected.setStatus("current")
_FgIpsIntrusionsBlocked_Type = Counter32
_FgIpsIntrusionsBlocked_Object = MibTableColumn
fgIpsIntrusionsBlocked = _FgIpsIntrusionsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 2),
    _FgIpsIntrusionsBlocked_Type()
)
fgIpsIntrusionsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsIntrusionsBlocked.setStatus("current")
_FgIpsCritSevDetections_Type = Counter32
_FgIpsCritSevDetections_Object = MibTableColumn
fgIpsCritSevDetections = _FgIpsCritSevDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 3),
    _FgIpsCritSevDetections_Type()
)
fgIpsCritSevDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsCritSevDetections.setStatus("current")
_FgIpsHighSevDetections_Type = Counter32
_FgIpsHighSevDetections_Object = MibTableColumn
fgIpsHighSevDetections = _FgIpsHighSevDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 4),
    _FgIpsHighSevDetections_Type()
)
fgIpsHighSevDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsHighSevDetections.setStatus("current")
_FgIpsMedSevDetections_Type = Counter32
_FgIpsMedSevDetections_Object = MibTableColumn
fgIpsMedSevDetections = _FgIpsMedSevDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 5),
    _FgIpsMedSevDetections_Type()
)
fgIpsMedSevDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsMedSevDetections.setStatus("current")
_FgIpsLowSevDetections_Type = Counter32
_FgIpsLowSevDetections_Object = MibTableColumn
fgIpsLowSevDetections = _FgIpsLowSevDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 6),
    _FgIpsLowSevDetections_Type()
)
fgIpsLowSevDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsLowSevDetections.setStatus("current")
_FgIpsInfoSevDetections_Type = Counter32
_FgIpsInfoSevDetections_Object = MibTableColumn
fgIpsInfoSevDetections = _FgIpsInfoSevDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 7),
    _FgIpsInfoSevDetections_Type()
)
fgIpsInfoSevDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsInfoSevDetections.setStatus("current")
_FgIpsSignatureDetections_Type = Counter32
_FgIpsSignatureDetections_Object = MibTableColumn
fgIpsSignatureDetections = _FgIpsSignatureDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 8),
    _FgIpsSignatureDetections_Type()
)
fgIpsSignatureDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsSignatureDetections.setStatus("current")
_FgIpsAnomalyDetections_Type = Counter32
_FgIpsAnomalyDetections_Object = MibTableColumn
fgIpsAnomalyDetections = _FgIpsAnomalyDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 2, 1, 1, 9),
    _FgIpsAnomalyDetections_Type()
)
fgIpsAnomalyDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpsAnomalyDetections.setStatus("current")
_FgIpsTrapObjects_ObjectIdentity = ObjectIdentity
fgIpsTrapObjects = _FgIpsTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 3)
)
_FgIpsTrapSigId_Type = FnIndex
_FgIpsTrapSigId_Object = MibScalar
fgIpsTrapSigId = _FgIpsTrapSigId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 3, 1),
    _FgIpsTrapSigId_Type()
)
fgIpsTrapSigId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgIpsTrapSigId.setStatus("current")
_FgIpsTrapSrcIp_Type = IpAddress
_FgIpsTrapSrcIp_Object = MibScalar
fgIpsTrapSrcIp = _FgIpsTrapSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 3, 2),
    _FgIpsTrapSrcIp_Type()
)
fgIpsTrapSrcIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgIpsTrapSrcIp.setStatus("current")
_FgIpsTrapSigMsg_Type = DisplayString
_FgIpsTrapSigMsg_Object = MibScalar
fgIpsTrapSigMsg = _FgIpsTrapSigMsg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 9, 3, 3),
    _FgIpsTrapSigMsg_Type()
)
fgIpsTrapSigMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgIpsTrapSigMsg.setStatus("current")
_FgApplications_ObjectIdentity = ObjectIdentity
fgApplications = _FgApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10)
)
_FgWebfilter_ObjectIdentity = ObjectIdentity
fgWebfilter = _FgWebfilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1)
)
_FgWebfilterInfo_ObjectIdentity = ObjectIdentity
fgWebfilterInfo = _FgWebfilterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 1)
)
_FgWebfilterTables_ObjectIdentity = ObjectIdentity
fgWebfilterTables = _FgWebfilterTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2)
)
_FgWebfilterStatsTable_Object = MibTable
fgWebfilterStatsTable = _FgWebfilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fgWebfilterStatsTable.setStatus("current")
_FgWebfilterStatsEntry_Object = MibTableRow
fgWebfilterStatsEntry = _FgWebfilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fgWebfilterStatsEntry.setStatus("current")
_FgWfHTTPBlocked_Type = Counter32
_FgWfHTTPBlocked_Object = MibTableColumn
fgWfHTTPBlocked = _FgWfHTTPBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1, 1),
    _FgWfHTTPBlocked_Type()
)
fgWfHTTPBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWfHTTPBlocked.setStatus("current")
_FgWfHTTPSBlocked_Type = Counter32
_FgWfHTTPSBlocked_Object = MibTableColumn
fgWfHTTPSBlocked = _FgWfHTTPSBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1, 2),
    _FgWfHTTPSBlocked_Type()
)
fgWfHTTPSBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWfHTTPSBlocked.setStatus("current")
_FgWfHTTPURLBlocked_Type = Counter32
_FgWfHTTPURLBlocked_Object = MibTableColumn
fgWfHTTPURLBlocked = _FgWfHTTPURLBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1, 3),
    _FgWfHTTPURLBlocked_Type()
)
fgWfHTTPURLBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWfHTTPURLBlocked.setStatus("current")
_FgWfHTTPSURLBlocked_Type = Counter32
_FgWfHTTPSURLBlocked_Object = MibTableColumn
fgWfHTTPSURLBlocked = _FgWfHTTPSURLBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1, 4),
    _FgWfHTTPSURLBlocked_Type()
)
fgWfHTTPSURLBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWfHTTPSURLBlocked.setStatus("current")
_FgWfActiveXBlocked_Type = Counter32
_FgWfActiveXBlocked_Object = MibTableColumn
fgWfActiveXBlocked = _FgWfActiveXBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1, 5),
    _FgWfActiveXBlocked_Type()
)
fgWfActiveXBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWfActiveXBlocked.setStatus("current")
_FgWfCookieBlocked_Type = Counter32
_FgWfCookieBlocked_Object = MibTableColumn
fgWfCookieBlocked = _FgWfCookieBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1, 6),
    _FgWfCookieBlocked_Type()
)
fgWfCookieBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWfCookieBlocked.setStatus("current")
_FgWfAppletBlocked_Type = Counter32
_FgWfAppletBlocked_Object = MibTableColumn
fgWfAppletBlocked = _FgWfAppletBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 1, 1, 7),
    _FgWfAppletBlocked_Type()
)
fgWfAppletBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWfAppletBlocked.setStatus("current")
_FgFortiGuardStatsTable_Object = MibTable
fgFortiGuardStatsTable = _FgFortiGuardStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fgFortiGuardStatsTable.setStatus("current")
_FgFortiGuardStatsEntry_Object = MibTableRow
fgFortiGuardStatsEntry = _FgFortiGuardStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fgFortiGuardStatsEntry.setStatus("current")
_FgFgWfHTTPExamined_Type = Counter32
_FgFgWfHTTPExamined_Object = MibTableColumn
fgFgWfHTTPExamined = _FgFgWfHTTPExamined_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 1),
    _FgFgWfHTTPExamined_Type()
)
fgFgWfHTTPExamined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPExamined.setStatus("current")
_FgFgWfHTTPSExamined_Type = Counter32
_FgFgWfHTTPSExamined_Object = MibTableColumn
fgFgWfHTTPSExamined = _FgFgWfHTTPSExamined_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 2),
    _FgFgWfHTTPSExamined_Type()
)
fgFgWfHTTPSExamined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPSExamined.setStatus("current")
_FgFgWfHTTPAllowed_Type = Counter32
_FgFgWfHTTPAllowed_Object = MibTableColumn
fgFgWfHTTPAllowed = _FgFgWfHTTPAllowed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 3),
    _FgFgWfHTTPAllowed_Type()
)
fgFgWfHTTPAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPAllowed.setStatus("current")
_FgFgWfHTTPSAllowed_Type = Counter32
_FgFgWfHTTPSAllowed_Object = MibTableColumn
fgFgWfHTTPSAllowed = _FgFgWfHTTPSAllowed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 4),
    _FgFgWfHTTPSAllowed_Type()
)
fgFgWfHTTPSAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPSAllowed.setStatus("current")
_FgFgWfHTTPBlocked_Type = Counter32
_FgFgWfHTTPBlocked_Object = MibTableColumn
fgFgWfHTTPBlocked = _FgFgWfHTTPBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 5),
    _FgFgWfHTTPBlocked_Type()
)
fgFgWfHTTPBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPBlocked.setStatus("current")
_FgFgWfHTTPSBlocked_Type = Counter32
_FgFgWfHTTPSBlocked_Object = MibTableColumn
fgFgWfHTTPSBlocked = _FgFgWfHTTPSBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 6),
    _FgFgWfHTTPSBlocked_Type()
)
fgFgWfHTTPSBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPSBlocked.setStatus("current")
_FgFgWfHTTPLogged_Type = Counter32
_FgFgWfHTTPLogged_Object = MibTableColumn
fgFgWfHTTPLogged = _FgFgWfHTTPLogged_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 7),
    _FgFgWfHTTPLogged_Type()
)
fgFgWfHTTPLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPLogged.setStatus("current")
_FgFgWfHTTPSLogged_Type = Counter32
_FgFgWfHTTPSLogged_Object = MibTableColumn
fgFgWfHTTPSLogged = _FgFgWfHTTPSLogged_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 8),
    _FgFgWfHTTPSLogged_Type()
)
fgFgWfHTTPSLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPSLogged.setStatus("current")
_FgFgWfHTTPOverridden_Type = Counter32
_FgFgWfHTTPOverridden_Object = MibTableColumn
fgFgWfHTTPOverridden = _FgFgWfHTTPOverridden_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 9),
    _FgFgWfHTTPOverridden_Type()
)
fgFgWfHTTPOverridden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPOverridden.setStatus("current")
_FgFgWfHTTPSOverridden_Type = Counter32
_FgFgWfHTTPSOverridden_Object = MibTableColumn
fgFgWfHTTPSOverridden = _FgFgWfHTTPSOverridden_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 1, 2, 2, 1, 10),
    _FgFgWfHTTPSOverridden_Type()
)
fgFgWfHTTPSOverridden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgFgWfHTTPSOverridden.setStatus("current")
_FgAppProxyHTTP_ObjectIdentity = ObjectIdentity
fgAppProxyHTTP = _FgAppProxyHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100)
)
_FgApHTTPUpTime_Type = Counter32
_FgApHTTPUpTime_Object = MibScalar
fgApHTTPUpTime = _FgApHTTPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100, 1),
    _FgApHTTPUpTime_Type()
)
fgApHTTPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApHTTPUpTime.setStatus("deprecated")


class _FgApHTTPMemUsage_Type(Gauge32):
    """Custom type fgApHTTPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApHTTPMemUsage_Type.__name__ = "Gauge32"
_FgApHTTPMemUsage_Object = MibScalar
fgApHTTPMemUsage = _FgApHTTPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100, 2),
    _FgApHTTPMemUsage_Type()
)
fgApHTTPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApHTTPMemUsage.setStatus("deprecated")
_FgApHTTPStatsTable_Object = MibTable
fgApHTTPStatsTable = _FgApHTTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100, 3)
)
if mibBuilder.loadTexts:
    fgApHTTPStatsTable.setStatus("current")
_FgApHTTPStatsEntry_Object = MibTableRow
fgApHTTPStatsEntry = _FgApHTTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100, 3, 1)
)
if mibBuilder.loadTexts:
    fgApHTTPStatsEntry.setStatus("current")
_FgApHTTPReqProcessed_Type = Counter32
_FgApHTTPReqProcessed_Object = MibTableColumn
fgApHTTPReqProcessed = _FgApHTTPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100, 3, 1, 1),
    _FgApHTTPReqProcessed_Type()
)
fgApHTTPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApHTTPReqProcessed.setStatus("current")
_FgApHTTPConnections_Type = Unsigned32
_FgApHTTPConnections_Object = MibScalar
fgApHTTPConnections = _FgApHTTPConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100, 4),
    _FgApHTTPConnections_Type()
)
fgApHTTPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApHTTPConnections.setStatus("current")
_FgApHTTPMaxConnections_Type = Unsigned32
_FgApHTTPMaxConnections_Object = MibScalar
fgApHTTPMaxConnections = _FgApHTTPMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 100, 5),
    _FgApHTTPMaxConnections_Type()
)
fgApHTTPMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApHTTPMaxConnections.setStatus("current")
_FgAppProxySMTP_ObjectIdentity = ObjectIdentity
fgAppProxySMTP = _FgAppProxySMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101)
)
_FgApSMTPUpTime_Type = Counter32
_FgApSMTPUpTime_Object = MibScalar
fgApSMTPUpTime = _FgApSMTPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 1),
    _FgApSMTPUpTime_Type()
)
fgApSMTPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSMTPUpTime.setStatus("deprecated")


class _FgApSMTPMemUsage_Type(Gauge32):
    """Custom type fgApSMTPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApSMTPMemUsage_Type.__name__ = "Gauge32"
_FgApSMTPMemUsage_Object = MibScalar
fgApSMTPMemUsage = _FgApSMTPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 2),
    _FgApSMTPMemUsage_Type()
)
fgApSMTPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSMTPMemUsage.setStatus("deprecated")
_FgApSMTPStatsTable_Object = MibTable
fgApSMTPStatsTable = _FgApSMTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 3)
)
if mibBuilder.loadTexts:
    fgApSMTPStatsTable.setStatus("current")
_FgApSMTPStatsEntry_Object = MibTableRow
fgApSMTPStatsEntry = _FgApSMTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 3, 1)
)
if mibBuilder.loadTexts:
    fgApSMTPStatsEntry.setStatus("current")
_FgApSMTPReqProcessed_Type = Counter32
_FgApSMTPReqProcessed_Object = MibTableColumn
fgApSMTPReqProcessed = _FgApSMTPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 3, 1, 1),
    _FgApSMTPReqProcessed_Type()
)
fgApSMTPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSMTPReqProcessed.setStatus("current")
_FgApSMTPSpamDetected_Type = Counter32
_FgApSMTPSpamDetected_Object = MibTableColumn
fgApSMTPSpamDetected = _FgApSMTPSpamDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 3, 1, 2),
    _FgApSMTPSpamDetected_Type()
)
fgApSMTPSpamDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSMTPSpamDetected.setStatus("current")
_FgApSMTPConnections_Type = Unsigned32
_FgApSMTPConnections_Object = MibScalar
fgApSMTPConnections = _FgApSMTPConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 4),
    _FgApSMTPConnections_Type()
)
fgApSMTPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSMTPConnections.setStatus("current")
_FgApSMTPMaxConnections_Type = Unsigned32
_FgApSMTPMaxConnections_Object = MibScalar
fgApSMTPMaxConnections = _FgApSMTPMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 101, 5),
    _FgApSMTPMaxConnections_Type()
)
fgApSMTPMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSMTPMaxConnections.setStatus("current")
_FgAppProxyPOP3_ObjectIdentity = ObjectIdentity
fgAppProxyPOP3 = _FgAppProxyPOP3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102)
)
_FgApPOP3UpTime_Type = Counter32
_FgApPOP3UpTime_Object = MibScalar
fgApPOP3UpTime = _FgApPOP3UpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 1),
    _FgApPOP3UpTime_Type()
)
fgApPOP3UpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApPOP3UpTime.setStatus("deprecated")


class _FgApPOP3MemUsage_Type(Gauge32):
    """Custom type fgApPOP3MemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApPOP3MemUsage_Type.__name__ = "Gauge32"
_FgApPOP3MemUsage_Object = MibScalar
fgApPOP3MemUsage = _FgApPOP3MemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 2),
    _FgApPOP3MemUsage_Type()
)
fgApPOP3MemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApPOP3MemUsage.setStatus("deprecated")
_FgApPOP3StatsTable_Object = MibTable
fgApPOP3StatsTable = _FgApPOP3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 3)
)
if mibBuilder.loadTexts:
    fgApPOP3StatsTable.setStatus("current")
_FgApPOP3StatsEntry_Object = MibTableRow
fgApPOP3StatsEntry = _FgApPOP3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 3, 1)
)
if mibBuilder.loadTexts:
    fgApPOP3StatsEntry.setStatus("current")
_FgApPOP3ReqProcessed_Type = Counter32
_FgApPOP3ReqProcessed_Object = MibTableColumn
fgApPOP3ReqProcessed = _FgApPOP3ReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 3, 1, 1),
    _FgApPOP3ReqProcessed_Type()
)
fgApPOP3ReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApPOP3ReqProcessed.setStatus("current")
_FgApPOP3SpamDetected_Type = Counter32
_FgApPOP3SpamDetected_Object = MibTableColumn
fgApPOP3SpamDetected = _FgApPOP3SpamDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 3, 1, 2),
    _FgApPOP3SpamDetected_Type()
)
fgApPOP3SpamDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApPOP3SpamDetected.setStatus("current")
_FgApPOP3Connections_Type = Unsigned32
_FgApPOP3Connections_Object = MibScalar
fgApPOP3Connections = _FgApPOP3Connections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 4),
    _FgApPOP3Connections_Type()
)
fgApPOP3Connections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApPOP3Connections.setStatus("current")
_FgApPOP3MaxConnections_Type = Unsigned32
_FgApPOP3MaxConnections_Object = MibScalar
fgApPOP3MaxConnections = _FgApPOP3MaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 102, 5),
    _FgApPOP3MaxConnections_Type()
)
fgApPOP3MaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApPOP3MaxConnections.setStatus("current")
_FgAppProxyIMAP_ObjectIdentity = ObjectIdentity
fgAppProxyIMAP = _FgAppProxyIMAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103)
)
_FgApIMAPUpTime_Type = Counter32
_FgApIMAPUpTime_Object = MibScalar
fgApIMAPUpTime = _FgApIMAPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 1),
    _FgApIMAPUpTime_Type()
)
fgApIMAPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMAPUpTime.setStatus("deprecated")


class _FgApIMAPMemUsage_Type(Gauge32):
    """Custom type fgApIMAPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApIMAPMemUsage_Type.__name__ = "Gauge32"
_FgApIMAPMemUsage_Object = MibScalar
fgApIMAPMemUsage = _FgApIMAPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 2),
    _FgApIMAPMemUsage_Type()
)
fgApIMAPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMAPMemUsage.setStatus("deprecated")
_FgApIMAPStatsTable_Object = MibTable
fgApIMAPStatsTable = _FgApIMAPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 3)
)
if mibBuilder.loadTexts:
    fgApIMAPStatsTable.setStatus("current")
_FgApIMAPStatsEntry_Object = MibTableRow
fgApIMAPStatsEntry = _FgApIMAPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 3, 1)
)
if mibBuilder.loadTexts:
    fgApIMAPStatsEntry.setStatus("current")
_FgApIMAPReqProcessed_Type = Counter32
_FgApIMAPReqProcessed_Object = MibTableColumn
fgApIMAPReqProcessed = _FgApIMAPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 3, 1, 1),
    _FgApIMAPReqProcessed_Type()
)
fgApIMAPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMAPReqProcessed.setStatus("current")
_FgApIMAPSpamDetected_Type = Counter32
_FgApIMAPSpamDetected_Object = MibTableColumn
fgApIMAPSpamDetected = _FgApIMAPSpamDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 3, 1, 2),
    _FgApIMAPSpamDetected_Type()
)
fgApIMAPSpamDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMAPSpamDetected.setStatus("current")
_FgApIMAPConnections_Type = Unsigned32
_FgApIMAPConnections_Object = MibScalar
fgApIMAPConnections = _FgApIMAPConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 4),
    _FgApIMAPConnections_Type()
)
fgApIMAPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMAPConnections.setStatus("current")
_FgApIMAPMaxConnections_Type = Unsigned32
_FgApIMAPMaxConnections_Object = MibScalar
fgApIMAPMaxConnections = _FgApIMAPMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 103, 5),
    _FgApIMAPMaxConnections_Type()
)
fgApIMAPMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMAPMaxConnections.setStatus("current")
_FgAppProxyNNTP_ObjectIdentity = ObjectIdentity
fgAppProxyNNTP = _FgAppProxyNNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104)
)
_FgApNNTPUpTime_Type = Counter32
_FgApNNTPUpTime_Object = MibScalar
fgApNNTPUpTime = _FgApNNTPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104, 1),
    _FgApNNTPUpTime_Type()
)
fgApNNTPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApNNTPUpTime.setStatus("deprecated")


class _FgApNNTPMemUsage_Type(Gauge32):
    """Custom type fgApNNTPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApNNTPMemUsage_Type.__name__ = "Gauge32"
_FgApNNTPMemUsage_Object = MibScalar
fgApNNTPMemUsage = _FgApNNTPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104, 2),
    _FgApNNTPMemUsage_Type()
)
fgApNNTPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApNNTPMemUsage.setStatus("deprecated")
_FgApNNTPStatsTable_Object = MibTable
fgApNNTPStatsTable = _FgApNNTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104, 3)
)
if mibBuilder.loadTexts:
    fgApNNTPStatsTable.setStatus("current")
_FgApNNTPStatsEntry_Object = MibTableRow
fgApNNTPStatsEntry = _FgApNNTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104, 3, 1)
)
if mibBuilder.loadTexts:
    fgApNNTPStatsEntry.setStatus("current")
_FgApNNTPReqProcessed_Type = Counter32
_FgApNNTPReqProcessed_Object = MibTableColumn
fgApNNTPReqProcessed = _FgApNNTPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104, 3, 1, 1),
    _FgApNNTPReqProcessed_Type()
)
fgApNNTPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApNNTPReqProcessed.setStatus("current")
_FgApNNTPConnections_Type = Unsigned32
_FgApNNTPConnections_Object = MibScalar
fgApNNTPConnections = _FgApNNTPConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104, 4),
    _FgApNNTPConnections_Type()
)
fgApNNTPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApNNTPConnections.setStatus("current")
_FgApNNTPMaxConnections_Type = Unsigned32
_FgApNNTPMaxConnections_Object = MibScalar
fgApNNTPMaxConnections = _FgApNNTPMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 104, 5),
    _FgApNNTPMaxConnections_Type()
)
fgApNNTPMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApNNTPMaxConnections.setStatus("current")
_FgAppProxyIM_ObjectIdentity = ObjectIdentity
fgAppProxyIM = _FgAppProxyIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 105)
)
_FgApIMUpTime_Type = Counter32
_FgApIMUpTime_Object = MibScalar
fgApIMUpTime = _FgApIMUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 105, 1),
    _FgApIMUpTime_Type()
)
fgApIMUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMUpTime.setStatus("current")


class _FgApIMMemUsage_Type(Gauge32):
    """Custom type fgApIMMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApIMMemUsage_Type.__name__ = "Gauge32"
_FgApIMMemUsage_Object = MibScalar
fgApIMMemUsage = _FgApIMMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 105, 2),
    _FgApIMMemUsage_Type()
)
fgApIMMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMMemUsage.setStatus("current")
_FgApIMStatsTable_Object = MibTable
fgApIMStatsTable = _FgApIMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 105, 3)
)
if mibBuilder.loadTexts:
    fgApIMStatsTable.setStatus("current")
_FgApIMStatsEntry_Object = MibTableRow
fgApIMStatsEntry = _FgApIMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 105, 3, 1)
)
if mibBuilder.loadTexts:
    fgApIMStatsEntry.setStatus("current")
_FgApIMReqProcessed_Type = Counter32
_FgApIMReqProcessed_Object = MibTableColumn
fgApIMReqProcessed = _FgApIMReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 105, 3, 1, 1),
    _FgApIMReqProcessed_Type()
)
fgApIMReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApIMReqProcessed.setStatus("current")
_FgAppProxySIP_ObjectIdentity = ObjectIdentity
fgAppProxySIP = _FgAppProxySIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106)
)
_FgApSIPUpTime_Type = Counter32
_FgApSIPUpTime_Object = MibScalar
fgApSIPUpTime = _FgApSIPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 1),
    _FgApSIPUpTime_Type()
)
fgApSIPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSIPUpTime.setStatus("current")


class _FgApSIPMemUsage_Type(Gauge32):
    """Custom type fgApSIPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApSIPMemUsage_Type.__name__ = "Gauge32"
_FgApSIPMemUsage_Object = MibScalar
fgApSIPMemUsage = _FgApSIPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 2),
    _FgApSIPMemUsage_Type()
)
fgApSIPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSIPMemUsage.setStatus("current")
_FgApSIPStatsTable_Object = MibTable
fgApSIPStatsTable = _FgApSIPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 3)
)
if mibBuilder.loadTexts:
    fgApSIPStatsTable.setStatus("current")
_FgApSIPStatsEntry_Object = MibTableRow
fgApSIPStatsEntry = _FgApSIPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 3, 1)
)
if mibBuilder.loadTexts:
    fgApSIPStatsEntry.setStatus("current")
_FgApSIPClientReg_Type = Counter32
_FgApSIPClientReg_Object = MibTableColumn
fgApSIPClientReg = _FgApSIPClientReg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 3, 1, 1),
    _FgApSIPClientReg_Type()
)
fgApSIPClientReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSIPClientReg.setStatus("current")
_FgApSIPCallHandling_Type = Counter32
_FgApSIPCallHandling_Object = MibTableColumn
fgApSIPCallHandling = _FgApSIPCallHandling_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 3, 1, 2),
    _FgApSIPCallHandling_Type()
)
fgApSIPCallHandling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSIPCallHandling.setStatus("current")
_FgApSIPServices_Type = Counter32
_FgApSIPServices_Object = MibTableColumn
fgApSIPServices = _FgApSIPServices_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 3, 1, 3),
    _FgApSIPServices_Type()
)
fgApSIPServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSIPServices.setStatus("current")
_FgApSIPOtherReq_Type = Counter32
_FgApSIPOtherReq_Object = MibTableColumn
fgApSIPOtherReq = _FgApSIPOtherReq_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 106, 3, 1, 4),
    _FgApSIPOtherReq_Type()
)
fgApSIPOtherReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApSIPOtherReq.setStatus("current")
_FgAppScanUnit_ObjectIdentity = ObjectIdentity
fgAppScanUnit = _FgAppScanUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 107)
)
_FgAppSuNumber_Type = Gauge32
_FgAppSuNumber_Object = MibScalar
fgAppSuNumber = _FgAppSuNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 107, 1),
    _FgAppSuNumber_Type()
)
fgAppSuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppSuNumber.setStatus("current")
_FgAppSuStatsTable_Object = MibTable
fgAppSuStatsTable = _FgAppSuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 107, 2)
)
if mibBuilder.loadTexts:
    fgAppSuStatsTable.setStatus("current")
_FgAppSuStatsEntry_Object = MibTableRow
fgAppSuStatsEntry = _FgAppSuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 107, 2, 1)
)
fgAppSuStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgAppSuIndex"),
)
if mibBuilder.loadTexts:
    fgAppSuStatsEntry.setStatus("current")
_FgAppSuIndex_Type = FnIndex
_FgAppSuIndex_Object = MibTableColumn
fgAppSuIndex = _FgAppSuIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 107, 2, 1, 1),
    _FgAppSuIndex_Type()
)
fgAppSuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgAppSuIndex.setStatus("current")
_FgAppSuFileScanned_Type = Counter32
_FgAppSuFileScanned_Object = MibTableColumn
fgAppSuFileScanned = _FgAppSuFileScanned_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 107, 2, 1, 2),
    _FgAppSuFileScanned_Type()
)
fgAppSuFileScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppSuFileScanned.setStatus("current")
_FgAppVoIP_ObjectIdentity = ObjectIdentity
fgAppVoIP = _FgAppVoIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 108)
)
_FgAppVoIPStatsTable_Object = MibTable
fgAppVoIPStatsTable = _FgAppVoIPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 108, 1)
)
if mibBuilder.loadTexts:
    fgAppVoIPStatsTable.setStatus("current")
_FgAppVoIPStatsEntry_Object = MibTableRow
fgAppVoIPStatsEntry = _FgAppVoIPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 108, 1, 1)
)
if mibBuilder.loadTexts:
    fgAppVoIPStatsEntry.setStatus("current")
_FgAppVoIPConn_Type = Gauge32
_FgAppVoIPConn_Object = MibTableColumn
fgAppVoIPConn = _FgAppVoIPConn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 108, 1, 1, 1),
    _FgAppVoIPConn_Type()
)
fgAppVoIPConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppVoIPConn.setStatus("current")
_FgAppVoIPCallBlocked_Type = Counter32
_FgAppVoIPCallBlocked_Object = MibTableColumn
fgAppVoIPCallBlocked = _FgAppVoIPCallBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 108, 1, 1, 2),
    _FgAppVoIPCallBlocked_Type()
)
fgAppVoIPCallBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppVoIPCallBlocked.setStatus("current")
_FgAppP2P_ObjectIdentity = ObjectIdentity
fgAppP2P = _FgAppP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109)
)
_FgAppP2PStatsTable_Object = MibTable
fgAppP2PStatsTable = _FgAppP2PStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 1)
)
if mibBuilder.loadTexts:
    fgAppP2PStatsTable.setStatus("current")
_FgAppP2PStatsEntry_Object = MibTableRow
fgAppP2PStatsEntry = _FgAppP2PStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 1, 1)
)
if mibBuilder.loadTexts:
    fgAppP2PStatsEntry.setStatus("current")
_FgAppP2PConnBlocked_Type = Counter32
_FgAppP2PConnBlocked_Object = MibTableColumn
fgAppP2PConnBlocked = _FgAppP2PConnBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 1, 1, 1),
    _FgAppP2PConnBlocked_Type()
)
fgAppP2PConnBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppP2PConnBlocked.setStatus("current")
_FgAppP2PProtoTable_Object = MibTable
fgAppP2PProtoTable = _FgAppP2PProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 2)
)
if mibBuilder.loadTexts:
    fgAppP2PProtoTable.setStatus("current")
_FgAppP2PProtoEntry_Object = MibTableRow
fgAppP2PProtoEntry = _FgAppP2PProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 2, 1)
)
fgAppP2PProtoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgAppP2PProtEntProto"),
)
if mibBuilder.loadTexts:
    fgAppP2PProtoEntry.setStatus("current")
_FgAppP2PProtEntProto_Type = FgP2PProto
_FgAppP2PProtEntProto_Object = MibTableColumn
fgAppP2PProtEntProto = _FgAppP2PProtEntProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 2, 1, 1),
    _FgAppP2PProtEntProto_Type()
)
fgAppP2PProtEntProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgAppP2PProtEntProto.setStatus("current")
_FgAppP2PProtEntBytes_Type = Counter64
_FgAppP2PProtEntBytes_Object = MibTableColumn
fgAppP2PProtEntBytes = _FgAppP2PProtEntBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 2, 1, 2),
    _FgAppP2PProtEntBytes_Type()
)
fgAppP2PProtEntBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppP2PProtEntBytes.setStatus("current")
_FgAppP2PProtoEntLastReset_Type = TimeTicks
_FgAppP2PProtoEntLastReset_Object = MibTableColumn
fgAppP2PProtoEntLastReset = _FgAppP2PProtoEntLastReset_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 109, 2, 1, 3),
    _FgAppP2PProtoEntLastReset_Type()
)
fgAppP2PProtoEntLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppP2PProtoEntLastReset.setStatus("current")
_FgAppIM_ObjectIdentity = ObjectIdentity
fgAppIM = _FgAppIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 110)
)
_FgAppIMStatsTable_Object = MibTable
fgAppIMStatsTable = _FgAppIMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 110, 1)
)
if mibBuilder.loadTexts:
    fgAppIMStatsTable.setStatus("current")
_FgAppIMStatsEntry_Object = MibTableRow
fgAppIMStatsEntry = _FgAppIMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 110, 1, 1)
)
if mibBuilder.loadTexts:
    fgAppIMStatsEntry.setStatus("current")
_FgAppIMMessages_Type = Counter32
_FgAppIMMessages_Object = MibTableColumn
fgAppIMMessages = _FgAppIMMessages_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 110, 1, 1, 1),
    _FgAppIMMessages_Type()
)
fgAppIMMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppIMMessages.setStatus("current")
_FgAppIMFileTransfered_Type = Counter32
_FgAppIMFileTransfered_Object = MibTableColumn
fgAppIMFileTransfered = _FgAppIMFileTransfered_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 110, 1, 1, 2),
    _FgAppIMFileTransfered_Type()
)
fgAppIMFileTransfered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppIMFileTransfered.setStatus("current")
_FgAppIMFileTxBlocked_Type = Counter32
_FgAppIMFileTxBlocked_Object = MibTableColumn
fgAppIMFileTxBlocked = _FgAppIMFileTxBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 110, 1, 1, 3),
    _FgAppIMFileTxBlocked_Type()
)
fgAppIMFileTxBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppIMFileTxBlocked.setStatus("current")
_FgAppIMConnBlocked_Type = Counter32
_FgAppIMConnBlocked_Object = MibTableColumn
fgAppIMConnBlocked = _FgAppIMConnBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 110, 1, 1, 4),
    _FgAppIMConnBlocked_Type()
)
fgAppIMConnBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppIMConnBlocked.setStatus("current")
_FgAppProxyFTP_ObjectIdentity = ObjectIdentity
fgAppProxyFTP = _FgAppProxyFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111)
)
_FgApFTPUpTime_Type = Counter32
_FgApFTPUpTime_Object = MibScalar
fgApFTPUpTime = _FgApFTPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111, 1),
    _FgApFTPUpTime_Type()
)
fgApFTPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApFTPUpTime.setStatus("deprecated")


class _FgApFTPMemUsage_Type(Gauge32):
    """Custom type fgApFTPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgApFTPMemUsage_Type.__name__ = "Gauge32"
_FgApFTPMemUsage_Object = MibScalar
fgApFTPMemUsage = _FgApFTPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111, 2),
    _FgApFTPMemUsage_Type()
)
fgApFTPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApFTPMemUsage.setStatus("deprecated")
_FgApFTPStatsTable_Object = MibTable
fgApFTPStatsTable = _FgApFTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111, 3)
)
if mibBuilder.loadTexts:
    fgApFTPStatsTable.setStatus("current")
_FgApFTPStatsEntry_Object = MibTableRow
fgApFTPStatsEntry = _FgApFTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111, 3, 1)
)
if mibBuilder.loadTexts:
    fgApFTPStatsEntry.setStatus("current")
_FgApFTPReqProcessed_Type = Counter32
_FgApFTPReqProcessed_Object = MibTableColumn
fgApFTPReqProcessed = _FgApFTPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111, 3, 1, 1),
    _FgApFTPReqProcessed_Type()
)
fgApFTPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApFTPReqProcessed.setStatus("current")
_FgApFTPConnections_Type = Unsigned32
_FgApFTPConnections_Object = MibScalar
fgApFTPConnections = _FgApFTPConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111, 4),
    _FgApFTPConnections_Type()
)
fgApFTPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApFTPConnections.setStatus("current")
_FgApFTPMaxConnections_Type = Unsigned32
_FgApFTPMaxConnections_Object = MibScalar
fgApFTPMaxConnections = _FgApFTPMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 111, 5),
    _FgApFTPMaxConnections_Type()
)
fgApFTPMaxConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgApFTPMaxConnections.setStatus("current")
_FgAppExplicitProxy_ObjectIdentity = ObjectIdentity
fgAppExplicitProxy = _FgAppExplicitProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112)
)
_FgExplicitProxyInfo_ObjectIdentity = ObjectIdentity
fgExplicitProxyInfo = _FgExplicitProxyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 1)
)
_FgExplicitProxyUpTime_Type = Counter32
_FgExplicitProxyUpTime_Object = MibScalar
fgExplicitProxyUpTime = _FgExplicitProxyUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 1, 1),
    _FgExplicitProxyUpTime_Type()
)
fgExplicitProxyUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyUpTime.setStatus("current")


class _FgExplicitProxyMemUsage_Type(Gauge32):
    """Custom type fgExplicitProxyMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgExplicitProxyMemUsage_Type.__name__ = "Gauge32"
_FgExplicitProxyMemUsage_Object = MibScalar
fgExplicitProxyMemUsage = _FgExplicitProxyMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 1, 2),
    _FgExplicitProxyMemUsage_Type()
)
fgExplicitProxyMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyMemUsage.setStatus("current")
_FgExplicitProxyRequests_Type = Counter64
_FgExplicitProxyRequests_Object = MibScalar
fgExplicitProxyRequests = _FgExplicitProxyRequests_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 1, 3),
    _FgExplicitProxyRequests_Type()
)
fgExplicitProxyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyRequests.setStatus("current")
_FgExplicitProxyStatsTable_Object = MibTable
fgExplicitProxyStatsTable = _FgExplicitProxyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 2)
)
if mibBuilder.loadTexts:
    fgExplicitProxyStatsTable.setStatus("current")
_FgExplicitProxyStatsEntry_Object = MibTableRow
fgExplicitProxyStatsEntry = _FgExplicitProxyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 2, 1)
)
fgExplicitProxyStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgExplicitProxyStatsEntry.setStatus("current")
_FgExplicitProxyUsers_Type = Integer32
_FgExplicitProxyUsers_Object = MibTableColumn
fgExplicitProxyUsers = _FgExplicitProxyUsers_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 2, 1, 1),
    _FgExplicitProxyUsers_Type()
)
fgExplicitProxyUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyUsers.setStatus("current")
_FgExplicitProxySessions_Type = Integer32
_FgExplicitProxySessions_Object = MibTableColumn
fgExplicitProxySessions = _FgExplicitProxySessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 2, 1, 2),
    _FgExplicitProxySessions_Type()
)
fgExplicitProxySessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxySessions.setStatus("current")
_FgExplicitProxyScanStatsTable_Object = MibTable
fgExplicitProxyScanStatsTable = _FgExplicitProxyScanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3)
)
if mibBuilder.loadTexts:
    fgExplicitProxyScanStatsTable.setStatus("current")
_FgExplicitProxyScanStatsEntry_Object = MibTableRow
fgExplicitProxyScanStatsEntry = _FgExplicitProxyScanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1)
)
fgExplicitProxyScanStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgExplicitProxyScanStatsDisp"),
)
if mibBuilder.loadTexts:
    fgExplicitProxyScanStatsEntry.setStatus("current")
_FgExplicitProxyScanStatsDisp_Type = FgScanAvDisposition
_FgExplicitProxyScanStatsDisp_Object = MibTableColumn
fgExplicitProxyScanStatsDisp = _FgExplicitProxyScanStatsDisp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 1),
    _FgExplicitProxyScanStatsDisp_Type()
)
fgExplicitProxyScanStatsDisp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgExplicitProxyScanStatsDisp.setStatus("current")
_FgExplicitProxyVirus_Type = Counter32
_FgExplicitProxyVirus_Object = MibTableColumn
fgExplicitProxyVirus = _FgExplicitProxyVirus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 2),
    _FgExplicitProxyVirus_Type()
)
fgExplicitProxyVirus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyVirus.setStatus("current")
_FgExplicitProxyBannedWords_Type = Counter32
_FgExplicitProxyBannedWords_Object = MibTableColumn
fgExplicitProxyBannedWords = _FgExplicitProxyBannedWords_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 3),
    _FgExplicitProxyBannedWords_Type()
)
fgExplicitProxyBannedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyBannedWords.setStatus("current")
_FgExplicitProxyPolicy_Type = Counter32
_FgExplicitProxyPolicy_Object = MibTableColumn
fgExplicitProxyPolicy = _FgExplicitProxyPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 4),
    _FgExplicitProxyPolicy_Type()
)
fgExplicitProxyPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyPolicy.setStatus("current")
_FgExplicitProxyOversized_Type = Counter32
_FgExplicitProxyOversized_Object = MibTableColumn
fgExplicitProxyOversized = _FgExplicitProxyOversized_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 5),
    _FgExplicitProxyOversized_Type()
)
fgExplicitProxyOversized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyOversized.setStatus("current")
_FgExplicitProxyArchNest_Type = Counter32
_FgExplicitProxyArchNest_Object = MibTableColumn
fgExplicitProxyArchNest = _FgExplicitProxyArchNest_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 6),
    _FgExplicitProxyArchNest_Type()
)
fgExplicitProxyArchNest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyArchNest.setStatus("current")
_FgExplicitProxyArchSize_Type = Counter32
_FgExplicitProxyArchSize_Object = MibTableColumn
fgExplicitProxyArchSize = _FgExplicitProxyArchSize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 7),
    _FgExplicitProxyArchSize_Type()
)
fgExplicitProxyArchSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyArchSize.setStatus("current")
_FgExplicitProxyArchEncrypted_Type = Counter32
_FgExplicitProxyArchEncrypted_Object = MibTableColumn
fgExplicitProxyArchEncrypted = _FgExplicitProxyArchEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 8),
    _FgExplicitProxyArchEncrypted_Type()
)
fgExplicitProxyArchEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyArchEncrypted.setStatus("current")
_FgExplicitProxyArchMultiPart_Type = Counter32
_FgExplicitProxyArchMultiPart_Object = MibTableColumn
fgExplicitProxyArchMultiPart = _FgExplicitProxyArchMultiPart_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 9),
    _FgExplicitProxyArchMultiPart_Type()
)
fgExplicitProxyArchMultiPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyArchMultiPart.setStatus("current")
_FgExplicitProxyArchUnsupported_Type = Counter32
_FgExplicitProxyArchUnsupported_Object = MibTableColumn
fgExplicitProxyArchUnsupported = _FgExplicitProxyArchUnsupported_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 10),
    _FgExplicitProxyArchUnsupported_Type()
)
fgExplicitProxyArchUnsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyArchUnsupported.setStatus("current")
_FgExplicitProxyArchBomb_Type = Counter32
_FgExplicitProxyArchBomb_Object = MibTableColumn
fgExplicitProxyArchBomb = _FgExplicitProxyArchBomb_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 11),
    _FgExplicitProxyArchBomb_Type()
)
fgExplicitProxyArchBomb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyArchBomb.setStatus("current")
_FgExplicitProxyArchCorrupt_Type = Counter32
_FgExplicitProxyArchCorrupt_Object = MibTableColumn
fgExplicitProxyArchCorrupt = _FgExplicitProxyArchCorrupt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 3, 1, 12),
    _FgExplicitProxyArchCorrupt_Type()
)
fgExplicitProxyArchCorrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyArchCorrupt.setStatus("current")
_FgExplicitProxyScriptStatsTable_Object = MibTable
fgExplicitProxyScriptStatsTable = _FgExplicitProxyScriptStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4)
)
if mibBuilder.loadTexts:
    fgExplicitProxyScriptStatsTable.setStatus("current")
_FgExplicitProxyScriptStatsEntry_Object = MibTableRow
fgExplicitProxyScriptStatsEntry = _FgExplicitProxyScriptStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4, 1)
)
fgExplicitProxyScriptStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgExplicitProxyScriptStatsEntry.setStatus("current")
_FgExplicitProxyFilteredApplets_Type = Counter32
_FgExplicitProxyFilteredApplets_Object = MibTableColumn
fgExplicitProxyFilteredApplets = _FgExplicitProxyFilteredApplets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4, 1, 1),
    _FgExplicitProxyFilteredApplets_Type()
)
fgExplicitProxyFilteredApplets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyFilteredApplets.setStatus("current")
_FgExplicitProxyFilteredActiveX_Type = Counter32
_FgExplicitProxyFilteredActiveX_Object = MibTableColumn
fgExplicitProxyFilteredActiveX = _FgExplicitProxyFilteredActiveX_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4, 1, 2),
    _FgExplicitProxyFilteredActiveX_Type()
)
fgExplicitProxyFilteredActiveX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyFilteredActiveX.setStatus("current")
_FgExplicitProxyFilteredJScript_Type = Counter32
_FgExplicitProxyFilteredJScript_Object = MibTableColumn
fgExplicitProxyFilteredJScript = _FgExplicitProxyFilteredJScript_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4, 1, 3),
    _FgExplicitProxyFilteredJScript_Type()
)
fgExplicitProxyFilteredJScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyFilteredJScript.setStatus("current")
_FgExplicitProxyFilteredJS_Type = Counter32
_FgExplicitProxyFilteredJS_Object = MibTableColumn
fgExplicitProxyFilteredJS = _FgExplicitProxyFilteredJS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4, 1, 4),
    _FgExplicitProxyFilteredJS_Type()
)
fgExplicitProxyFilteredJS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyFilteredJS.setStatus("current")
_FgExplicitProxyFilteredVBS_Type = Counter32
_FgExplicitProxyFilteredVBS_Object = MibTableColumn
fgExplicitProxyFilteredVBS = _FgExplicitProxyFilteredVBS_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4, 1, 5),
    _FgExplicitProxyFilteredVBS_Type()
)
fgExplicitProxyFilteredVBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyFilteredVBS.setStatus("current")
_FgExplicitProxyFilteredOthScript_Type = Counter32
_FgExplicitProxyFilteredOthScript_Object = MibTableColumn
fgExplicitProxyFilteredOthScript = _FgExplicitProxyFilteredOthScript_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 4, 1, 6),
    _FgExplicitProxyFilteredOthScript_Type()
)
fgExplicitProxyFilteredOthScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyFilteredOthScript.setStatus("current")
_FgExplicitProxyFilterStatsTable_Object = MibTable
fgExplicitProxyFilterStatsTable = _FgExplicitProxyFilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5)
)
if mibBuilder.loadTexts:
    fgExplicitProxyFilterStatsTable.setStatus("current")
_FgExplicitProxyFilterStatsEntry_Object = MibTableRow
fgExplicitProxyFilterStatsEntry = _FgExplicitProxyFilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1)
)
fgExplicitProxyFilterStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgExplicitProxyFilterStatsEntry.setStatus("current")
_FgExplicitProxyBlockedDLP_Type = Counter32
_FgExplicitProxyBlockedDLP_Object = MibTableColumn
fgExplicitProxyBlockedDLP = _FgExplicitProxyBlockedDLP_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1, 1),
    _FgExplicitProxyBlockedDLP_Type()
)
fgExplicitProxyBlockedDLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyBlockedDLP.setStatus("current")
_FgExplicitProxyBlockedConType_Type = Counter32
_FgExplicitProxyBlockedConType_Object = MibTableColumn
fgExplicitProxyBlockedConType = _FgExplicitProxyBlockedConType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1, 2),
    _FgExplicitProxyBlockedConType_Type()
)
fgExplicitProxyBlockedConType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyBlockedConType.setStatus("current")
_FgExplicitProxyExaminedURLs_Type = Counter32
_FgExplicitProxyExaminedURLs_Object = MibTableColumn
fgExplicitProxyExaminedURLs = _FgExplicitProxyExaminedURLs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1, 3),
    _FgExplicitProxyExaminedURLs_Type()
)
fgExplicitProxyExaminedURLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyExaminedURLs.setStatus("current")
_FgExplicitProxyAllowedURLs_Type = Counter32
_FgExplicitProxyAllowedURLs_Object = MibTableColumn
fgExplicitProxyAllowedURLs = _FgExplicitProxyAllowedURLs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1, 4),
    _FgExplicitProxyAllowedURLs_Type()
)
fgExplicitProxyAllowedURLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyAllowedURLs.setStatus("current")
_FgExplicitProxyBlockedURLs_Type = Counter32
_FgExplicitProxyBlockedURLs_Object = MibTableColumn
fgExplicitProxyBlockedURLs = _FgExplicitProxyBlockedURLs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1, 5),
    _FgExplicitProxyBlockedURLs_Type()
)
fgExplicitProxyBlockedURLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyBlockedURLs.setStatus("current")
_FgExplicitProxyLoggedURLs_Type = Counter32
_FgExplicitProxyLoggedURLs_Object = MibTableColumn
fgExplicitProxyLoggedURLs = _FgExplicitProxyLoggedURLs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1, 6),
    _FgExplicitProxyLoggedURLs_Type()
)
fgExplicitProxyLoggedURLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyLoggedURLs.setStatus("current")
_FgExplicitProxyOverriddenURLs_Type = Counter32
_FgExplicitProxyOverriddenURLs_Object = MibTableColumn
fgExplicitProxyOverriddenURLs = _FgExplicitProxyOverriddenURLs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 112, 5, 1, 7),
    _FgExplicitProxyOverriddenURLs_Type()
)
fgExplicitProxyOverriddenURLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgExplicitProxyOverriddenURLs.setStatus("current")
_FgAppWebCache_ObjectIdentity = ObjectIdentity
fgAppWebCache = _FgAppWebCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113)
)
_FgWebCacheInfo_ObjectIdentity = ObjectIdentity
fgWebCacheInfo = _FgWebCacheInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1)
)
_FgWebCacheRAMLimit_Type = Gauge32
_FgWebCacheRAMLimit_Object = MibScalar
fgWebCacheRAMLimit = _FgWebCacheRAMLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1, 1),
    _FgWebCacheRAMLimit_Type()
)
fgWebCacheRAMLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheRAMLimit.setStatus("current")
_FgWebCacheRAMUsage_Type = Gauge32
_FgWebCacheRAMUsage_Object = MibScalar
fgWebCacheRAMUsage = _FgWebCacheRAMUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1, 2),
    _FgWebCacheRAMUsage_Type()
)
fgWebCacheRAMUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheRAMUsage.setStatus("current")
_FgWebCacheRAMHits_Type = Gauge32
_FgWebCacheRAMHits_Object = MibScalar
fgWebCacheRAMHits = _FgWebCacheRAMHits_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1, 3),
    _FgWebCacheRAMHits_Type()
)
fgWebCacheRAMHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheRAMHits.setStatus("current")
_FgWebCacheRAMMisses_Type = Gauge32
_FgWebCacheRAMMisses_Object = MibScalar
fgWebCacheRAMMisses = _FgWebCacheRAMMisses_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1, 4),
    _FgWebCacheRAMMisses_Type()
)
fgWebCacheRAMMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheRAMMisses.setStatus("current")
_FgWebCacheRequests_Type = Gauge32
_FgWebCacheRequests_Object = MibScalar
fgWebCacheRequests = _FgWebCacheRequests_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1, 5),
    _FgWebCacheRequests_Type()
)
fgWebCacheRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheRequests.setStatus("current")
_FgWebCacheBypass_Type = Gauge32
_FgWebCacheBypass_Object = MibScalar
fgWebCacheBypass = _FgWebCacheBypass_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1, 6),
    _FgWebCacheBypass_Type()
)
fgWebCacheBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheBypass.setStatus("current")
_FgWebCacheUpTime_Type = Counter32
_FgWebCacheUpTime_Object = MibScalar
fgWebCacheUpTime = _FgWebCacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 1, 7),
    _FgWebCacheUpTime_Type()
)
fgWebCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheUpTime.setStatus("current")
_FgWebCacheDiskStatsTable_Object = MibTable
fgWebCacheDiskStatsTable = _FgWebCacheDiskStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 2)
)
if mibBuilder.loadTexts:
    fgWebCacheDiskStatsTable.setStatus("current")
_FgWebCacheDiskStatsEntry_Object = MibTableRow
fgWebCacheDiskStatsEntry = _FgWebCacheDiskStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 2, 1)
)
fgWebCacheDiskStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgWebCacheDisk"),
)
if mibBuilder.loadTexts:
    fgWebCacheDiskStatsEntry.setStatus("current")
_FgWebCacheDisk_Type = Unsigned32
_FgWebCacheDisk_Object = MibTableColumn
fgWebCacheDisk = _FgWebCacheDisk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 2, 1, 1),
    _FgWebCacheDisk_Type()
)
fgWebCacheDisk.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWebCacheDisk.setStatus("current")
_FgWebCacheDiskLimit_Type = CounterBasedGauge64
_FgWebCacheDiskLimit_Object = MibTableColumn
fgWebCacheDiskLimit = _FgWebCacheDiskLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 2, 1, 2),
    _FgWebCacheDiskLimit_Type()
)
fgWebCacheDiskLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheDiskLimit.setStatus("current")
_FgWebCacheDiskUsage_Type = CounterBasedGauge64
_FgWebCacheDiskUsage_Object = MibTableColumn
fgWebCacheDiskUsage = _FgWebCacheDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 2, 1, 3),
    _FgWebCacheDiskUsage_Type()
)
fgWebCacheDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheDiskUsage.setStatus("current")
_FgWebCacheDiskHits_Type = Counter32
_FgWebCacheDiskHits_Object = MibTableColumn
fgWebCacheDiskHits = _FgWebCacheDiskHits_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 2, 1, 4),
    _FgWebCacheDiskHits_Type()
)
fgWebCacheDiskHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheDiskHits.setStatus("current")
_FgWebCacheDiskMisses_Type = Counter32
_FgWebCacheDiskMisses_Object = MibTableColumn
fgWebCacheDiskMisses = _FgWebCacheDiskMisses_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 2, 1, 5),
    _FgWebCacheDiskMisses_Type()
)
fgWebCacheDiskMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheDiskMisses.setStatus("current")
_FgWebCacheDiskFailure_Type = Counter64
_FgWebCacheDiskFailure_Object = MibTableColumn
fgWebCacheDiskFailure = _FgWebCacheDiskFailure_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 113, 2, 1, 6),
    _FgWebCacheDiskFailure_Type()
)
fgWebCacheDiskFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWebCacheDiskFailure.setStatus("current")
_FgAppWanOpt_ObjectIdentity = ObjectIdentity
fgAppWanOpt = _FgAppWanOpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114)
)
_FgWanOptInfo_ObjectIdentity = ObjectIdentity
fgWanOptInfo = _FgWanOptInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1)
)
_FgMemCacheLimit_Type = Gauge32
_FgMemCacheLimit_Object = MibScalar
fgMemCacheLimit = _FgMemCacheLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1, 1),
    _FgMemCacheLimit_Type()
)
fgMemCacheLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMemCacheLimit.setStatus("current")
_FgMemCacheUsage_Type = Gauge32
_FgMemCacheUsage_Object = MibScalar
fgMemCacheUsage = _FgMemCacheUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1, 2),
    _FgMemCacheUsage_Type()
)
fgMemCacheUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMemCacheUsage.setStatus("current")
_FgMemCacheHits_Type = Gauge32
_FgMemCacheHits_Object = MibScalar
fgMemCacheHits = _FgMemCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1, 3),
    _FgMemCacheHits_Type()
)
fgMemCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMemCacheHits.setStatus("current")
_FgMemCacheMisses_Type = Gauge32
_FgMemCacheMisses_Object = MibScalar
fgMemCacheMisses = _FgMemCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1, 4),
    _FgMemCacheMisses_Type()
)
fgMemCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMemCacheMisses.setStatus("current")
_FgByteCacheRAMLimit_Type = Gauge32
_FgByteCacheRAMLimit_Object = MibScalar
fgByteCacheRAMLimit = _FgByteCacheRAMLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1, 5),
    _FgByteCacheRAMLimit_Type()
)
fgByteCacheRAMLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgByteCacheRAMLimit.setStatus("current")
_FgByteCacheRAMUsage_Type = Gauge32
_FgByteCacheRAMUsage_Object = MibScalar
fgByteCacheRAMUsage = _FgByteCacheRAMUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1, 6),
    _FgByteCacheRAMUsage_Type()
)
fgByteCacheRAMUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgByteCacheRAMUsage.setStatus("current")
_FgWanOptUpTime_Type = Counter32
_FgWanOptUpTime_Object = MibScalar
fgWanOptUpTime = _FgWanOptUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 1, 7),
    _FgWanOptUpTime_Type()
)
fgWanOptUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptUpTime.setStatus("current")
_FgWanOptStatsTable_Object = MibTable
fgWanOptStatsTable = _FgWanOptStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 2)
)
if mibBuilder.loadTexts:
    fgWanOptStatsTable.setStatus("current")
_FgWanOptStatsEntry_Object = MibTableRow
fgWanOptStatsEntry = _FgWanOptStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 2, 1)
)
fgWanOptStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgWanOptStatsEntry.setStatus("current")
_FgWanOptTunnels_Type = Gauge32
_FgWanOptTunnels_Object = MibTableColumn
fgWanOptTunnels = _FgWanOptTunnels_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 2, 1, 1),
    _FgWanOptTunnels_Type()
)
fgWanOptTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptTunnels.setStatus("current")
_FgWanOptLANBytesIn_Type = Gauge32
_FgWanOptLANBytesIn_Object = MibTableColumn
fgWanOptLANBytesIn = _FgWanOptLANBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 2, 1, 2),
    _FgWanOptLANBytesIn_Type()
)
fgWanOptLANBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptLANBytesIn.setStatus("current")
_FgWanOptLANBytesOut_Type = Gauge32
_FgWanOptLANBytesOut_Object = MibTableColumn
fgWanOptLANBytesOut = _FgWanOptLANBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 2, 1, 3),
    _FgWanOptLANBytesOut_Type()
)
fgWanOptLANBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptLANBytesOut.setStatus("current")
_FgWanOptWANBytesIn_Type = Gauge32
_FgWanOptWANBytesIn_Object = MibTableColumn
fgWanOptWANBytesIn = _FgWanOptWANBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 2, 1, 4),
    _FgWanOptWANBytesIn_Type()
)
fgWanOptWANBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptWANBytesIn.setStatus("current")
_FgWanOptWANBytesOut_Type = Gauge32
_FgWanOptWANBytesOut_Object = MibTableColumn
fgWanOptWANBytesOut = _FgWanOptWANBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 2, 1, 5),
    _FgWanOptWANBytesOut_Type()
)
fgWanOptWANBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptWANBytesOut.setStatus("current")
_FgWanOptHistoryStatsTable_Object = MibTable
fgWanOptHistoryStatsTable = _FgWanOptHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 3)
)
if mibBuilder.loadTexts:
    fgWanOptHistoryStatsTable.setStatus("current")
_FgWanOptHistoryStatsEntry_Object = MibTableRow
fgWanOptHistoryStatsEntry = _FgWanOptHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 3, 1)
)
fgWanOptHistoryStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWanOptHistPeriod"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWanOptProtocol"),
)
if mibBuilder.loadTexts:
    fgWanOptHistoryStatsEntry.setStatus("current")
_FgWanOptHistPeriod_Type = FgWanOptHistPeriods
_FgWanOptHistPeriod_Object = MibTableColumn
fgWanOptHistPeriod = _FgWanOptHistPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 3, 1, 1),
    _FgWanOptHistPeriod_Type()
)
fgWanOptHistPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWanOptHistPeriod.setStatus("current")
_FgWanOptProtocol_Type = FgWanOptProtocols
_FgWanOptProtocol_Object = MibTableColumn
fgWanOptProtocol = _FgWanOptProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 3, 1, 2),
    _FgWanOptProtocol_Type()
)
fgWanOptProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWanOptProtocol.setStatus("current")


class _FgWanOptReductionRate_Type(Gauge32):
    """Custom type fgWanOptReductionRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgWanOptReductionRate_Type.__name__ = "Gauge32"
_FgWanOptReductionRate_Object = MibTableColumn
fgWanOptReductionRate = _FgWanOptReductionRate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 3, 1, 3),
    _FgWanOptReductionRate_Type()
)
fgWanOptReductionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptReductionRate.setStatus("current")
_FgWanOptLanTraffic_Type = CounterBasedGauge64
_FgWanOptLanTraffic_Object = MibTableColumn
fgWanOptLanTraffic = _FgWanOptLanTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 3, 1, 4),
    _FgWanOptLanTraffic_Type()
)
fgWanOptLanTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptLanTraffic.setStatus("current")
_FgWanOptWanTraffic_Type = CounterBasedGauge64
_FgWanOptWanTraffic_Object = MibTableColumn
fgWanOptWanTraffic = _FgWanOptWanTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 3, 1, 5),
    _FgWanOptWanTraffic_Type()
)
fgWanOptWanTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptWanTraffic.setStatus("current")
_FgWanOptTrafficStatsTable_Object = MibTable
fgWanOptTrafficStatsTable = _FgWanOptTrafficStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 4)
)
if mibBuilder.loadTexts:
    fgWanOptTrafficStatsTable.setStatus("current")
_FgWanOptTrafficStatsEntry_Object = MibTableRow
fgWanOptTrafficStatsEntry = _FgWanOptTrafficStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 4, 1)
)
fgWanOptTrafficStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWanOptProtocol"),
)
if mibBuilder.loadTexts:
    fgWanOptTrafficStatsEntry.setStatus("current")
_FgWanOptLanInTraffic_Type = Counter64
_FgWanOptLanInTraffic_Object = MibTableColumn
fgWanOptLanInTraffic = _FgWanOptLanInTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 4, 1, 1),
    _FgWanOptLanInTraffic_Type()
)
fgWanOptLanInTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptLanInTraffic.setStatus("current")
_FgWanOptLanOutTraffic_Type = Counter64
_FgWanOptLanOutTraffic_Object = MibTableColumn
fgWanOptLanOutTraffic = _FgWanOptLanOutTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 4, 1, 2),
    _FgWanOptLanOutTraffic_Type()
)
fgWanOptLanOutTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptLanOutTraffic.setStatus("current")
_FgWanOptWanInTraffic_Type = Counter64
_FgWanOptWanInTraffic_Object = MibTableColumn
fgWanOptWanInTraffic = _FgWanOptWanInTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 4, 1, 3),
    _FgWanOptWanInTraffic_Type()
)
fgWanOptWanInTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptWanInTraffic.setStatus("current")
_FgWanOptWanOutTraffic_Type = Counter64
_FgWanOptWanOutTraffic_Object = MibTableColumn
fgWanOptWanOutTraffic = _FgWanOptWanOutTraffic_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 4, 1, 4),
    _FgWanOptWanOutTraffic_Type()
)
fgWanOptWanOutTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptWanOutTraffic.setStatus("current")
_FgWanOptDiskStatsTable_Object = MibTable
fgWanOptDiskStatsTable = _FgWanOptDiskStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 5)
)
if mibBuilder.loadTexts:
    fgWanOptDiskStatsTable.setStatus("current")
_FgWanOptDiskStatsEntry_Object = MibTableRow
fgWanOptDiskStatsEntry = _FgWanOptDiskStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 5, 1)
)
fgWanOptDiskStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgWanOptDisk"),
)
if mibBuilder.loadTexts:
    fgWanOptDiskStatsEntry.setStatus("current")
_FgWanOptDisk_Type = Unsigned32
_FgWanOptDisk_Object = MibTableColumn
fgWanOptDisk = _FgWanOptDisk_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 5, 1, 1),
    _FgWanOptDisk_Type()
)
fgWanOptDisk.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWanOptDisk.setStatus("current")
_FgWanOptDiskLimit_Type = CounterBasedGauge64
_FgWanOptDiskLimit_Object = MibTableColumn
fgWanOptDiskLimit = _FgWanOptDiskLimit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 5, 1, 2),
    _FgWanOptDiskLimit_Type()
)
fgWanOptDiskLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptDiskLimit.setStatus("current")
_FgWanOptDiskUsage_Type = CounterBasedGauge64
_FgWanOptDiskUsage_Object = MibTableColumn
fgWanOptDiskUsage = _FgWanOptDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 5, 1, 3),
    _FgWanOptDiskUsage_Type()
)
fgWanOptDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptDiskUsage.setStatus("current")
_FgWanOptDiskHits_Type = Counter32
_FgWanOptDiskHits_Object = MibTableColumn
fgWanOptDiskHits = _FgWanOptDiskHits_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 5, 1, 4),
    _FgWanOptDiskHits_Type()
)
fgWanOptDiskHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptDiskHits.setStatus("current")
_FgWanOptDiskMisses_Type = Counter32
_FgWanOptDiskMisses_Object = MibTableColumn
fgWanOptDiskMisses = _FgWanOptDiskMisses_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 5, 1, 5),
    _FgWanOptDiskMisses_Type()
)
fgWanOptDiskMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptDiskMisses.setStatus("current")
_FgWanOptDiskFailure_Type = Counter64
_FgWanOptDiskFailure_Object = MibTableColumn
fgWanOptDiskFailure = _FgWanOptDiskFailure_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 114, 5, 1, 6),
    _FgWanOptDiskFailure_Type()
)
fgWanOptDiskFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWanOptDiskFailure.setStatus("current")
_FgAppDNSProxy_ObjectIdentity = ObjectIdentity
fgAppDNSProxy = _FgAppDNSProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 115)
)
_FgDNSProxyStatsInfo_ObjectIdentity = ObjectIdentity
fgDNSProxyStatsInfo = _FgDNSProxyStatsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 115, 1)
)
_FgDNSProxyStatsUdpCacheHit_Type = Counter64
_FgDNSProxyStatsUdpCacheHit_Object = MibScalar
fgDNSProxyStatsUdpCacheHit = _FgDNSProxyStatsUdpCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 115, 1, 1),
    _FgDNSProxyStatsUdpCacheHit_Type()
)
fgDNSProxyStatsUdpCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDNSProxyStatsUdpCacheHit.setStatus("current")
_FgDNSProxyStatsUdpRatingCacheHit_Type = Counter64
_FgDNSProxyStatsUdpRatingCacheHit_Object = MibScalar
fgDNSProxyStatsUdpRatingCacheHit = _FgDNSProxyStatsUdpRatingCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 115, 1, 2),
    _FgDNSProxyStatsUdpRatingCacheHit_Type()
)
fgDNSProxyStatsUdpRatingCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDNSProxyStatsUdpRatingCacheHit.setStatus("current")
_FgDNSProxyStatsUdpReq_Type = Counter64
_FgDNSProxyStatsUdpReq_Object = MibScalar
fgDNSProxyStatsUdpReq = _FgDNSProxyStatsUdpReq_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 115, 1, 3),
    _FgDNSProxyStatsUdpReq_Type()
)
fgDNSProxyStatsUdpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDNSProxyStatsUdpReq.setStatus("current")
_FgDNSProxyStatsUdpRes_Type = Counter64
_FgDNSProxyStatsUdpRes_Object = MibScalar
fgDNSProxyStatsUdpRes = _FgDNSProxyStatsUdpRes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 115, 1, 4),
    _FgDNSProxyStatsUdpRes_Type()
)
fgDNSProxyStatsUdpRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDNSProxyStatsUdpRes.setStatus("current")
_FgDNSProxyStatsUdpFwd_Type = Counter64
_FgDNSProxyStatsUdpFwd_Object = MibScalar
fgDNSProxyStatsUdpFwd = _FgDNSProxyStatsUdpFwd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 115, 1, 5),
    _FgDNSProxyStatsUdpFwd_Type()
)
fgDNSProxyStatsUdpFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDNSProxyStatsUdpFwd.setStatus("current")
_FgDNSProxyStatsUdpRetrans_Type = Counter64
_FgDNSProxyStatsUdpRetrans_Object = MibScalar
fgDNSProxyStatsUdpRetrans = _FgDNSProxyStatsUdpRetrans_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 115, 1, 6),
    _FgDNSProxyStatsUdpRetrans_Type()
)
fgDNSProxyStatsUdpRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDNSProxyStatsUdpRetrans.setStatus("current")
_FgDNSProxyStatsUdpTo_Type = Counter64
_FgDNSProxyStatsUdpTo_Object = MibScalar
fgDNSProxyStatsUdpTo = _FgDNSProxyStatsUdpTo_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 115, 1, 7),
    _FgDNSProxyStatsUdpTo_Type()
)
fgDNSProxyStatsUdpTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDNSProxyStatsUdpTo.setStatus("current")
_FgDNSProxyStatsUdpFtgRes_Type = Counter64
_FgDNSProxyStatsUdpFtgRes_Object = MibScalar
fgDNSProxyStatsUdpFtgRes = _FgDNSProxyStatsUdpFtgRes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 115, 1, 8),
    _FgDNSProxyStatsUdpFtgRes_Type()
)
fgDNSProxyStatsUdpFtgRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDNSProxyStatsUdpFtgRes.setStatus("current")
_FgDNSProxyStatsUdpFtgFwd_Type = Counter64
_FgDNSProxyStatsUdpFtgFwd_Object = MibScalar
fgDNSProxyStatsUdpFtgFwd = _FgDNSProxyStatsUdpFtgFwd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 115, 1, 9),
    _FgDNSProxyStatsUdpFtgFwd_Type()
)
fgDNSProxyStatsUdpFtgFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDNSProxyStatsUdpFtgFwd.setStatus("current")
_FgDNSProxyStatsUdpFtgRetrans_Type = Counter64
_FgDNSProxyStatsUdpFtgRetrans_Object = MibScalar
fgDNSProxyStatsUdpFtgRetrans = _FgDNSProxyStatsUdpFtgRetrans_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 115, 1, 10),
    _FgDNSProxyStatsUdpFtgRetrans_Type()
)
fgDNSProxyStatsUdpFtgRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDNSProxyStatsUdpFtgRetrans.setStatus("current")
_FgAppFnbam_ObjectIdentity = ObjectIdentity
fgAppFnbam = _FgAppFnbam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 116)
)
_FgAppFnbamStatsInfo_ObjectIdentity = ObjectIdentity
fgAppFnbamStatsInfo = _FgAppFnbamStatsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 116, 1)
)
_FgAppFnbamStatsTotalAuthReqs_Type = Counter64
_FgAppFnbamStatsTotalAuthReqs_Object = MibScalar
fgAppFnbamStatsTotalAuthReqs = _FgAppFnbamStatsTotalAuthReqs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 116, 1, 1),
    _FgAppFnbamStatsTotalAuthReqs_Type()
)
fgAppFnbamStatsTotalAuthReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppFnbamStatsTotalAuthReqs.setStatus("current")
_FgAppFnbamStatsTotalEagainErrs_Type = Counter64
_FgAppFnbamStatsTotalEagainErrs_Object = MibScalar
fgAppFnbamStatsTotalEagainErrs = _FgAppFnbamStatsTotalEagainErrs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 116, 1, 2),
    _FgAppFnbamStatsTotalEagainErrs_Type()
)
fgAppFnbamStatsTotalEagainErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppFnbamStatsTotalEagainErrs.setStatus("current")
_FgAppFnbamStatsTotalLdapFails_Type = Counter64
_FgAppFnbamStatsTotalLdapFails_Object = MibScalar
fgAppFnbamStatsTotalLdapFails = _FgAppFnbamStatsTotalLdapFails_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 10, 116, 1, 3),
    _FgAppFnbamStatsTotalLdapFails_Type()
)
fgAppFnbamStatsTotalLdapFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgAppFnbamStatsTotalLdapFails.setStatus("current")
_FgInetProto_ObjectIdentity = ObjectIdentity
fgInetProto = _FgInetProto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11)
)
_FgInetProtoInfo_ObjectIdentity = ObjectIdentity
fgInetProtoInfo = _FgInetProtoInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 1)
)
_FgInetProtoTables_ObjectIdentity = ObjectIdentity
fgInetProtoTables = _FgInetProtoTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2)
)
_FgIpSessTable_Object = MibTable
fgIpSessTable = _FgIpSessTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1)
)
if mibBuilder.loadTexts:
    fgIpSessTable.setStatus("current")
_FgIpSessEntry_Object = MibTableRow
fgIpSessEntry = _FgIpSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1)
)
fgIpSessEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgIpSessIndex"),
)
if mibBuilder.loadTexts:
    fgIpSessEntry.setStatus("current")
_FgIpSessIndex_Type = FnIndex
_FgIpSessIndex_Object = MibTableColumn
fgIpSessIndex = _FgIpSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 1),
    _FgIpSessIndex_Type()
)
fgIpSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgIpSessIndex.setStatus("current")
_FgIpSessProto_Type = FgSessProto
_FgIpSessProto_Object = MibTableColumn
fgIpSessProto = _FgIpSessProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 2),
    _FgIpSessProto_Type()
)
fgIpSessProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessProto.setStatus("current")
_FgIpSessFromAddr_Type = IpAddress
_FgIpSessFromAddr_Object = MibTableColumn
fgIpSessFromAddr = _FgIpSessFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 3),
    _FgIpSessFromAddr_Type()
)
fgIpSessFromAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessFromAddr.setStatus("current")
_FgIpSessFromPort_Type = InetPortNumber
_FgIpSessFromPort_Object = MibTableColumn
fgIpSessFromPort = _FgIpSessFromPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 4),
    _FgIpSessFromPort_Type()
)
fgIpSessFromPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessFromPort.setStatus("current")
_FgIpSessToAddr_Type = IpAddress
_FgIpSessToAddr_Object = MibTableColumn
fgIpSessToAddr = _FgIpSessToAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 5),
    _FgIpSessToAddr_Type()
)
fgIpSessToAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessToAddr.setStatus("current")
_FgIpSessToPort_Type = InetPortNumber
_FgIpSessToPort_Object = MibTableColumn
fgIpSessToPort = _FgIpSessToPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 6),
    _FgIpSessToPort_Type()
)
fgIpSessToPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessToPort.setStatus("current")
_FgIpSessExp_Type = Gauge32
_FgIpSessExp_Object = MibTableColumn
fgIpSessExp = _FgIpSessExp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 7),
    _FgIpSessExp_Type()
)
fgIpSessExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessExp.setStatus("current")
_FgIpSessVdom_Type = FgVdIndex
_FgIpSessVdom_Object = MibTableColumn
fgIpSessVdom = _FgIpSessVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 1, 1, 8),
    _FgIpSessVdom_Type()
)
fgIpSessVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessVdom.setStatus("current")
_FgIpSessStatsTable_Object = MibTable
fgIpSessStatsTable = _FgIpSessStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 2)
)
if mibBuilder.loadTexts:
    fgIpSessStatsTable.setStatus("current")
_FgIpSessStatsEntry_Object = MibTableRow
fgIpSessStatsEntry = _FgIpSessStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fgIpSessStatsEntry.setStatus("current")
_FgIpSessNumber_Type = Gauge32
_FgIpSessNumber_Object = MibTableColumn
fgIpSessNumber = _FgIpSessNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 2, 1, 1),
    _FgIpSessNumber_Type()
)
fgIpSessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIpSessNumber.setStatus("current")
_FgIp6SessStatsTable_Object = MibTable
fgIp6SessStatsTable = _FgIp6SessStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 3)
)
if mibBuilder.loadTexts:
    fgIp6SessStatsTable.setStatus("current")
_FgIp6SessStatsEntry_Object = MibTableRow
fgIp6SessStatsEntry = _FgIp6SessStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fgIp6SessStatsEntry.setStatus("current")
_FgIp6SessNumber_Type = Gauge32
_FgIp6SessNumber_Object = MibTableColumn
fgIp6SessNumber = _FgIp6SessNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 11, 2, 3, 1, 1),
    _FgIp6SessNumber_Type()
)
fgIp6SessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgIp6SessNumber.setStatus("current")
_FgVpn_ObjectIdentity = ObjectIdentity
fgVpn = _FgVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12)
)
_FgVpnInfo_ObjectIdentity = ObjectIdentity
fgVpnInfo = _FgVpnInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 1)
)
_FgVpnTunnelUpCount_Type = Integer32
_FgVpnTunnelUpCount_Object = MibScalar
fgVpnTunnelUpCount = _FgVpnTunnelUpCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 1, 1),
    _FgVpnTunnelUpCount_Type()
)
fgVpnTunnelUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunnelUpCount.setStatus("current")
_FgVpnTables_ObjectIdentity = ObjectIdentity
fgVpnTables = _FgVpnTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2)
)
_FgVpnDialupTable_Object = MibTable
fgVpnDialupTable = _FgVpnDialupTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1)
)
if mibBuilder.loadTexts:
    fgVpnDialupTable.setStatus("current")
_FgVpnDialupEntry_Object = MibTableRow
fgVpnDialupEntry = _FgVpnDialupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1)
)
fgVpnDialupEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVpnDialupIndex"),
)
if mibBuilder.loadTexts:
    fgVpnDialupEntry.setStatus("current")
_FgVpnDialupIndex_Type = FnIndex
_FgVpnDialupIndex_Object = MibTableColumn
fgVpnDialupIndex = _FgVpnDialupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 1),
    _FgVpnDialupIndex_Type()
)
fgVpnDialupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgVpnDialupIndex.setStatus("current")
_FgVpnDialupGateway_Type = IpAddress
_FgVpnDialupGateway_Object = MibTableColumn
fgVpnDialupGateway = _FgVpnDialupGateway_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 2),
    _FgVpnDialupGateway_Type()
)
fgVpnDialupGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupGateway.setStatus("current")
_FgVpnDialupLifetime_Type = Integer32
_FgVpnDialupLifetime_Object = MibTableColumn
fgVpnDialupLifetime = _FgVpnDialupLifetime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 3),
    _FgVpnDialupLifetime_Type()
)
fgVpnDialupLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupLifetime.setStatus("current")
_FgVpnDialupTimeout_Type = Integer32
_FgVpnDialupTimeout_Object = MibTableColumn
fgVpnDialupTimeout = _FgVpnDialupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 4),
    _FgVpnDialupTimeout_Type()
)
fgVpnDialupTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupTimeout.setStatus("current")
_FgVpnDialupSrcBegin_Type = IpAddress
_FgVpnDialupSrcBegin_Object = MibTableColumn
fgVpnDialupSrcBegin = _FgVpnDialupSrcBegin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 5),
    _FgVpnDialupSrcBegin_Type()
)
fgVpnDialupSrcBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupSrcBegin.setStatus("current")
_FgVpnDialupSrcEnd_Type = IpAddress
_FgVpnDialupSrcEnd_Object = MibTableColumn
fgVpnDialupSrcEnd = _FgVpnDialupSrcEnd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 6),
    _FgVpnDialupSrcEnd_Type()
)
fgVpnDialupSrcEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupSrcEnd.setStatus("current")
_FgVpnDialupDstAddr_Type = IpAddress
_FgVpnDialupDstAddr_Object = MibTableColumn
fgVpnDialupDstAddr = _FgVpnDialupDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 7),
    _FgVpnDialupDstAddr_Type()
)
fgVpnDialupDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupDstAddr.setStatus("current")
_FgVpnDialupVdom_Type = FgVdIndex
_FgVpnDialupVdom_Object = MibTableColumn
fgVpnDialupVdom = _FgVpnDialupVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 8),
    _FgVpnDialupVdom_Type()
)
fgVpnDialupVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupVdom.setStatus("current")
_FgVpnDialupInOctets_Type = Counter64
_FgVpnDialupInOctets_Object = MibTableColumn
fgVpnDialupInOctets = _FgVpnDialupInOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 9),
    _FgVpnDialupInOctets_Type()
)
fgVpnDialupInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupInOctets.setStatus("current")
_FgVpnDialupOutOctets_Type = Counter64
_FgVpnDialupOutOctets_Object = MibTableColumn
fgVpnDialupOutOctets = _FgVpnDialupOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 1, 1, 10),
    _FgVpnDialupOutOctets_Type()
)
fgVpnDialupOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnDialupOutOctets.setStatus("current")
_FgVpnTunTable_Object = MibTable
fgVpnTunTable = _FgVpnTunTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2)
)
if mibBuilder.loadTexts:
    fgVpnTunTable.setStatus("current")
_FgVpnTunEntry_Object = MibTableRow
fgVpnTunEntry = _FgVpnTunEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1)
)
fgVpnTunEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVpnTunEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgVpnTunEntPhase2Index"),
)
if mibBuilder.loadTexts:
    fgVpnTunEntry.setStatus("current")
_FgVpnTunEntIndex_Type = FnIndex
_FgVpnTunEntIndex_Object = MibTableColumn
fgVpnTunEntIndex = _FgVpnTunEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 1),
    _FgVpnTunEntIndex_Type()
)
fgVpnTunEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgVpnTunEntIndex.setStatus("current")
_FgVpnTunEntPhase1Name_Type = DisplayString
_FgVpnTunEntPhase1Name_Object = MibTableColumn
fgVpnTunEntPhase1Name = _FgVpnTunEntPhase1Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 2),
    _FgVpnTunEntPhase1Name_Type()
)
fgVpnTunEntPhase1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntPhase1Name.setStatus("current")
_FgVpnTunEntPhase2Name_Type = DisplayString
_FgVpnTunEntPhase2Name_Object = MibTableColumn
fgVpnTunEntPhase2Name = _FgVpnTunEntPhase2Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 3),
    _FgVpnTunEntPhase2Name_Type()
)
fgVpnTunEntPhase2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntPhase2Name.setStatus("current")
_FgVpnTunEntRemGwyIp_Type = IpAddress
_FgVpnTunEntRemGwyIp_Object = MibTableColumn
fgVpnTunEntRemGwyIp = _FgVpnTunEntRemGwyIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 4),
    _FgVpnTunEntRemGwyIp_Type()
)
fgVpnTunEntRemGwyIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntRemGwyIp.setStatus("current")
_FgVpnTunEntRemGwyPort_Type = InetPortNumber
_FgVpnTunEntRemGwyPort_Object = MibTableColumn
fgVpnTunEntRemGwyPort = _FgVpnTunEntRemGwyPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 5),
    _FgVpnTunEntRemGwyPort_Type()
)
fgVpnTunEntRemGwyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntRemGwyPort.setStatus("current")
_FgVpnTunEntLocGwyIp_Type = IpAddress
_FgVpnTunEntLocGwyIp_Object = MibTableColumn
fgVpnTunEntLocGwyIp = _FgVpnTunEntLocGwyIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 6),
    _FgVpnTunEntLocGwyIp_Type()
)
fgVpnTunEntLocGwyIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntLocGwyIp.setStatus("current")
_FgVpnTunEntLocGwyPort_Type = InetPortNumber
_FgVpnTunEntLocGwyPort_Object = MibTableColumn
fgVpnTunEntLocGwyPort = _FgVpnTunEntLocGwyPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 7),
    _FgVpnTunEntLocGwyPort_Type()
)
fgVpnTunEntLocGwyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntLocGwyPort.setStatus("current")
_FgVpnTunEntSelectorSrcBeginIp_Type = IpAddress
_FgVpnTunEntSelectorSrcBeginIp_Object = MibTableColumn
fgVpnTunEntSelectorSrcBeginIp = _FgVpnTunEntSelectorSrcBeginIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 8),
    _FgVpnTunEntSelectorSrcBeginIp_Type()
)
fgVpnTunEntSelectorSrcBeginIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntSelectorSrcBeginIp.setStatus("current")
_FgVpnTunEntSelectorSrcEndIp_Type = IpAddress
_FgVpnTunEntSelectorSrcEndIp_Object = MibTableColumn
fgVpnTunEntSelectorSrcEndIp = _FgVpnTunEntSelectorSrcEndIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 9),
    _FgVpnTunEntSelectorSrcEndIp_Type()
)
fgVpnTunEntSelectorSrcEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntSelectorSrcEndIp.setStatus("current")
_FgVpnTunEntSelectorSrcPort_Type = InetPortNumber
_FgVpnTunEntSelectorSrcPort_Object = MibTableColumn
fgVpnTunEntSelectorSrcPort = _FgVpnTunEntSelectorSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 10),
    _FgVpnTunEntSelectorSrcPort_Type()
)
fgVpnTunEntSelectorSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntSelectorSrcPort.setStatus("current")
_FgVpnTunEntSelectorDstBeginIp_Type = IpAddress
_FgVpnTunEntSelectorDstBeginIp_Object = MibTableColumn
fgVpnTunEntSelectorDstBeginIp = _FgVpnTunEntSelectorDstBeginIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 11),
    _FgVpnTunEntSelectorDstBeginIp_Type()
)
fgVpnTunEntSelectorDstBeginIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntSelectorDstBeginIp.setStatus("current")
_FgVpnTunEntSelectorDstEndIp_Type = IpAddress
_FgVpnTunEntSelectorDstEndIp_Object = MibTableColumn
fgVpnTunEntSelectorDstEndIp = _FgVpnTunEntSelectorDstEndIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 12),
    _FgVpnTunEntSelectorDstEndIp_Type()
)
fgVpnTunEntSelectorDstEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntSelectorDstEndIp.setStatus("current")
_FgVpnTunEntSelectorDstPort_Type = InetPortNumber
_FgVpnTunEntSelectorDstPort_Object = MibTableColumn
fgVpnTunEntSelectorDstPort = _FgVpnTunEntSelectorDstPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 13),
    _FgVpnTunEntSelectorDstPort_Type()
)
fgVpnTunEntSelectorDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntSelectorDstPort.setStatus("current")
_FgVpnTunEntSelectorProto_Type = Integer32
_FgVpnTunEntSelectorProto_Object = MibTableColumn
fgVpnTunEntSelectorProto = _FgVpnTunEntSelectorProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 14),
    _FgVpnTunEntSelectorProto_Type()
)
fgVpnTunEntSelectorProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntSelectorProto.setStatus("current")
_FgVpnTunEntLifeSecs_Type = Gauge32
_FgVpnTunEntLifeSecs_Object = MibTableColumn
fgVpnTunEntLifeSecs = _FgVpnTunEntLifeSecs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 15),
    _FgVpnTunEntLifeSecs_Type()
)
fgVpnTunEntLifeSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntLifeSecs.setStatus("current")
_FgVpnTunEntLifeBytes_Type = Gauge32
_FgVpnTunEntLifeBytes_Object = MibTableColumn
fgVpnTunEntLifeBytes = _FgVpnTunEntLifeBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 16),
    _FgVpnTunEntLifeBytes_Type()
)
fgVpnTunEntLifeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntLifeBytes.setStatus("current")
_FgVpnTunEntTimeout_Type = Gauge32
_FgVpnTunEntTimeout_Object = MibTableColumn
fgVpnTunEntTimeout = _FgVpnTunEntTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 17),
    _FgVpnTunEntTimeout_Type()
)
fgVpnTunEntTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntTimeout.setStatus("current")
_FgVpnTunEntInOctets_Type = Counter64
_FgVpnTunEntInOctets_Object = MibTableColumn
fgVpnTunEntInOctets = _FgVpnTunEntInOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 18),
    _FgVpnTunEntInOctets_Type()
)
fgVpnTunEntInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntInOctets.setStatus("current")
_FgVpnTunEntOutOctets_Type = Counter64
_FgVpnTunEntOutOctets_Object = MibTableColumn
fgVpnTunEntOutOctets = _FgVpnTunEntOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 19),
    _FgVpnTunEntOutOctets_Type()
)
fgVpnTunEntOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntOutOctets.setStatus("current")


class _FgVpnTunEntStatus_Type(Integer32):
    """Custom type fgVpnTunEntStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_FgVpnTunEntStatus_Type.__name__ = "Integer32"
_FgVpnTunEntStatus_Object = MibTableColumn
fgVpnTunEntStatus = _FgVpnTunEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 20),
    _FgVpnTunEntStatus_Type()
)
fgVpnTunEntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntStatus.setStatus("current")
_FgVpnTunEntVdom_Type = FgVdIndex
_FgVpnTunEntVdom_Object = MibTableColumn
fgVpnTunEntVdom = _FgVpnTunEntVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 21),
    _FgVpnTunEntVdom_Type()
)
fgVpnTunEntVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnTunEntVdom.setStatus("current")
_FgVpnTunEntPhase2Index_Type = FnIndex
_FgVpnTunEntPhase2Index_Object = MibTableColumn
fgVpnTunEntPhase2Index = _FgVpnTunEntPhase2Index_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 2, 1, 22),
    _FgVpnTunEntPhase2Index_Type()
)
fgVpnTunEntPhase2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgVpnTunEntPhase2Index.setStatus("current")
_FgVpnSslStatsTable_Object = MibTable
fgVpnSslStatsTable = _FgVpnSslStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3)
)
if mibBuilder.loadTexts:
    fgVpnSslStatsTable.setStatus("current")
_FgVpnSslStatsEntry_Object = MibTableRow
fgVpnSslStatsEntry = _FgVpnSslStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fgVpnSslStatsEntry.setStatus("current")
_FgVpnSslState_Type = FnBoolState
_FgVpnSslState_Object = MibTableColumn
fgVpnSslState = _FgVpnSslState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1, 1),
    _FgVpnSslState_Type()
)
fgVpnSslState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslState.setStatus("current")
_FgVpnSslStatsLoginUsers_Type = Gauge32
_FgVpnSslStatsLoginUsers_Object = MibTableColumn
fgVpnSslStatsLoginUsers = _FgVpnSslStatsLoginUsers_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1, 2),
    _FgVpnSslStatsLoginUsers_Type()
)
fgVpnSslStatsLoginUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslStatsLoginUsers.setStatus("current")
_FgVpnSslStatsMaxUsers_Type = Counter32
_FgVpnSslStatsMaxUsers_Object = MibTableColumn
fgVpnSslStatsMaxUsers = _FgVpnSslStatsMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1, 3),
    _FgVpnSslStatsMaxUsers_Type()
)
fgVpnSslStatsMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslStatsMaxUsers.setStatus("current")
_FgVpnSslStatsActiveWebSessions_Type = Gauge32
_FgVpnSslStatsActiveWebSessions_Object = MibTableColumn
fgVpnSslStatsActiveWebSessions = _FgVpnSslStatsActiveWebSessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1, 4),
    _FgVpnSslStatsActiveWebSessions_Type()
)
fgVpnSslStatsActiveWebSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslStatsActiveWebSessions.setStatus("current")
_FgVpnSslStatsMaxWebSessions_Type = Counter32
_FgVpnSslStatsMaxWebSessions_Object = MibTableColumn
fgVpnSslStatsMaxWebSessions = _FgVpnSslStatsMaxWebSessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1, 5),
    _FgVpnSslStatsMaxWebSessions_Type()
)
fgVpnSslStatsMaxWebSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslStatsMaxWebSessions.setStatus("current")
_FgVpnSslStatsActiveTunnels_Type = Gauge32
_FgVpnSslStatsActiveTunnels_Object = MibTableColumn
fgVpnSslStatsActiveTunnels = _FgVpnSslStatsActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1, 6),
    _FgVpnSslStatsActiveTunnels_Type()
)
fgVpnSslStatsActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslStatsActiveTunnels.setStatus("current")
_FgVpnSslStatsMaxTunnels_Type = Counter32
_FgVpnSslStatsMaxTunnels_Object = MibTableColumn
fgVpnSslStatsMaxTunnels = _FgVpnSslStatsMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 3, 1, 7),
    _FgVpnSslStatsMaxTunnels_Type()
)
fgVpnSslStatsMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslStatsMaxTunnels.setStatus("current")
_FgVpnSslTunnelTable_Object = MibTable
fgVpnSslTunnelTable = _FgVpnSslTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4)
)
if mibBuilder.loadTexts:
    fgVpnSslTunnelTable.setStatus("current")
_FgVpnSslTunnelEntry_Object = MibTableRow
fgVpnSslTunnelEntry = _FgVpnSslTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1)
)
fgVpnSslTunnelEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelIndex"),
)
if mibBuilder.loadTexts:
    fgVpnSslTunnelEntry.setStatus("current")
_FgVpnSslTunnelIndex_Type = FnIndex
_FgVpnSslTunnelIndex_Object = MibTableColumn
fgVpnSslTunnelIndex = _FgVpnSslTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 1),
    _FgVpnSslTunnelIndex_Type()
)
fgVpnSslTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgVpnSslTunnelIndex.setStatus("current")
_FgVpnSslTunnelVdom_Type = FgVdIndex
_FgVpnSslTunnelVdom_Object = MibTableColumn
fgVpnSslTunnelVdom = _FgVpnSslTunnelVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 2),
    _FgVpnSslTunnelVdom_Type()
)
fgVpnSslTunnelVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslTunnelVdom.setStatus("current")
_FgVpnSslTunnelUserName_Type = DisplayString
_FgVpnSslTunnelUserName_Object = MibTableColumn
fgVpnSslTunnelUserName = _FgVpnSslTunnelUserName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 3),
    _FgVpnSslTunnelUserName_Type()
)
fgVpnSslTunnelUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslTunnelUserName.setStatus("current")
_FgVpnSslTunnelSrcIp_Type = IpAddress
_FgVpnSslTunnelSrcIp_Object = MibTableColumn
fgVpnSslTunnelSrcIp = _FgVpnSslTunnelSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 4),
    _FgVpnSslTunnelSrcIp_Type()
)
fgVpnSslTunnelSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslTunnelSrcIp.setStatus("current")
_FgVpnSslTunnelIp_Type = IpAddress
_FgVpnSslTunnelIp_Object = MibTableColumn
fgVpnSslTunnelIp = _FgVpnSslTunnelIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 5),
    _FgVpnSslTunnelIp_Type()
)
fgVpnSslTunnelIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslTunnelIp.setStatus("current")
_FgVpnSslTunnelUpTime_Type = Counter32
_FgVpnSslTunnelUpTime_Object = MibTableColumn
fgVpnSslTunnelUpTime = _FgVpnSslTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 6),
    _FgVpnSslTunnelUpTime_Type()
)
fgVpnSslTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslTunnelUpTime.setStatus("current")
_FgVpnSslTunnelBytesIn_Type = Counter64
_FgVpnSslTunnelBytesIn_Object = MibTableColumn
fgVpnSslTunnelBytesIn = _FgVpnSslTunnelBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 7),
    _FgVpnSslTunnelBytesIn_Type()
)
fgVpnSslTunnelBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslTunnelBytesIn.setStatus("current")
_FgVpnSslTunnelBytesOut_Type = Counter64
_FgVpnSslTunnelBytesOut_Object = MibTableColumn
fgVpnSslTunnelBytesOut = _FgVpnSslTunnelBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 2, 4, 1, 8),
    _FgVpnSslTunnelBytesOut_Type()
)
fgVpnSslTunnelBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpnSslTunnelBytesOut.setStatus("current")
_FgVpnTrapObjects_ObjectIdentity = ObjectIdentity
fgVpnTrapObjects = _FgVpnTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 3)
)
_FgVpnTrapLocalGateway_Type = IpAddress
_FgVpnTrapLocalGateway_Object = MibScalar
fgVpnTrapLocalGateway = _FgVpnTrapLocalGateway_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 3, 2),
    _FgVpnTrapLocalGateway_Type()
)
fgVpnTrapLocalGateway.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgVpnTrapLocalGateway.setStatus("current")
_FgVpnTrapRemoteGateway_Type = IpAddress
_FgVpnTrapRemoteGateway_Object = MibScalar
fgVpnTrapRemoteGateway = _FgVpnTrapRemoteGateway_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 3, 3),
    _FgVpnTrapRemoteGateway_Type()
)
fgVpnTrapRemoteGateway.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgVpnTrapRemoteGateway.setStatus("current")
_FgVpnTrapPhase1Name_Type = DisplayString
_FgVpnTrapPhase1Name_Object = MibScalar
fgVpnTrapPhase1Name = _FgVpnTrapPhase1Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 3, 4),
    _FgVpnTrapPhase1Name_Type()
)
fgVpnTrapPhase1Name.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgVpnTrapPhase1Name.setStatus("current")
_FgVpn2Tables_ObjectIdentity = ObjectIdentity
fgVpn2Tables = _FgVpn2Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4)
)
_FgVpn2DialupTable_Object = MibTable
fgVpn2DialupTable = _FgVpn2DialupTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1)
)
if mibBuilder.loadTexts:
    fgVpn2DialupTable.setStatus("current")
_FgVpn2DialupEntry_Object = MibTableRow
fgVpn2DialupEntry = _FgVpn2DialupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1)
)
fgVpn2DialupEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVpn2DialupIndex"),
)
if mibBuilder.loadTexts:
    fgVpn2DialupEntry.setStatus("current")
_FgVpn2DialupIndex_Type = FnIndex
_FgVpn2DialupIndex_Object = MibTableColumn
fgVpn2DialupIndex = _FgVpn2DialupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 1),
    _FgVpn2DialupIndex_Type()
)
fgVpn2DialupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgVpn2DialupIndex.setStatus("current")
_FgVpn2DialupGatewayType_Type = InetAddressType
_FgVpn2DialupGatewayType_Object = MibTableColumn
fgVpn2DialupGatewayType = _FgVpn2DialupGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 2),
    _FgVpn2DialupGatewayType_Type()
)
fgVpn2DialupGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupGatewayType.setStatus("current")
_FgVpn2DialupGateway_Type = InetAddress
_FgVpn2DialupGateway_Object = MibTableColumn
fgVpn2DialupGateway = _FgVpn2DialupGateway_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 3),
    _FgVpn2DialupGateway_Type()
)
fgVpn2DialupGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupGateway.setStatus("current")
_FgVpn2DialupLifetime_Type = Integer32
_FgVpn2DialupLifetime_Object = MibTableColumn
fgVpn2DialupLifetime = _FgVpn2DialupLifetime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 4),
    _FgVpn2DialupLifetime_Type()
)
fgVpn2DialupLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupLifetime.setStatus("current")
_FgVpn2DialupTimeout_Type = Integer32
_FgVpn2DialupTimeout_Object = MibTableColumn
fgVpn2DialupTimeout = _FgVpn2DialupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 5),
    _FgVpn2DialupTimeout_Type()
)
fgVpn2DialupTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupTimeout.setStatus("current")
_FgVpn2DialupSrcBeginType_Type = InetAddressType
_FgVpn2DialupSrcBeginType_Object = MibTableColumn
fgVpn2DialupSrcBeginType = _FgVpn2DialupSrcBeginType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 6),
    _FgVpn2DialupSrcBeginType_Type()
)
fgVpn2DialupSrcBeginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupSrcBeginType.setStatus("current")
_FgVpn2DialupSrcBegin_Type = InetAddress
_FgVpn2DialupSrcBegin_Object = MibTableColumn
fgVpn2DialupSrcBegin = _FgVpn2DialupSrcBegin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 7),
    _FgVpn2DialupSrcBegin_Type()
)
fgVpn2DialupSrcBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupSrcBegin.setStatus("current")
_FgVpn2DialupSrcEndType_Type = InetAddressType
_FgVpn2DialupSrcEndType_Object = MibTableColumn
fgVpn2DialupSrcEndType = _FgVpn2DialupSrcEndType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 8),
    _FgVpn2DialupSrcEndType_Type()
)
fgVpn2DialupSrcEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupSrcEndType.setStatus("current")
_FgVpn2DialupSrcEnd_Type = InetAddress
_FgVpn2DialupSrcEnd_Object = MibTableColumn
fgVpn2DialupSrcEnd = _FgVpn2DialupSrcEnd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 9),
    _FgVpn2DialupSrcEnd_Type()
)
fgVpn2DialupSrcEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupSrcEnd.setStatus("current")
_FgVpn2DialupDstBeginType_Type = InetAddressType
_FgVpn2DialupDstBeginType_Object = MibTableColumn
fgVpn2DialupDstBeginType = _FgVpn2DialupDstBeginType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 10),
    _FgVpn2DialupDstBeginType_Type()
)
fgVpn2DialupDstBeginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupDstBeginType.setStatus("current")
_FgVpn2DialupDstBegin_Type = InetAddress
_FgVpn2DialupDstBegin_Object = MibTableColumn
fgVpn2DialupDstBegin = _FgVpn2DialupDstBegin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 11),
    _FgVpn2DialupDstBegin_Type()
)
fgVpn2DialupDstBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupDstBegin.setStatus("current")
_FgVpn2DialupDstEndType_Type = InetAddressType
_FgVpn2DialupDstEndType_Object = MibTableColumn
fgVpn2DialupDstEndType = _FgVpn2DialupDstEndType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 12),
    _FgVpn2DialupDstEndType_Type()
)
fgVpn2DialupDstEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupDstEndType.setStatus("current")
_FgVpn2DialupDstEnd_Type = InetAddress
_FgVpn2DialupDstEnd_Object = MibTableColumn
fgVpn2DialupDstEnd = _FgVpn2DialupDstEnd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 13),
    _FgVpn2DialupDstEnd_Type()
)
fgVpn2DialupDstEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupDstEnd.setStatus("current")
_FgVpn2DialupInOctets_Type = Counter64
_FgVpn2DialupInOctets_Object = MibTableColumn
fgVpn2DialupInOctets = _FgVpn2DialupInOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 14),
    _FgVpn2DialupInOctets_Type()
)
fgVpn2DialupInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupInOctets.setStatus("current")
_FgVpn2DialupOutOctets_Type = Counter64
_FgVpn2DialupOutOctets_Object = MibTableColumn
fgVpn2DialupOutOctets = _FgVpn2DialupOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 15),
    _FgVpn2DialupOutOctets_Type()
)
fgVpn2DialupOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupOutOctets.setStatus("current")
_FgVpn2DialupPhase1Name_Type = DisplayString
_FgVpn2DialupPhase1Name_Object = MibTableColumn
fgVpn2DialupPhase1Name = _FgVpn2DialupPhase1Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 16),
    _FgVpn2DialupPhase1Name_Type()
)
fgVpn2DialupPhase1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupPhase1Name.setStatus("current")
_FgVpn2DialupVdom_Type = FgVdIndex
_FgVpn2DialupVdom_Object = MibTableColumn
fgVpn2DialupVdom = _FgVpn2DialupVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 1, 1, 17),
    _FgVpn2DialupVdom_Type()
)
fgVpn2DialupVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2DialupVdom.setStatus("current")
_FgVpn2TunTable_Object = MibTable
fgVpn2TunTable = _FgVpn2TunTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2)
)
if mibBuilder.loadTexts:
    fgVpn2TunTable.setStatus("current")
_FgVpn2TunEntry_Object = MibTableRow
fgVpn2TunEntry = _FgVpn2TunEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1)
)
fgVpn2TunEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVpn2TunIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgVpn2TunPhase2Index"),
)
if mibBuilder.loadTexts:
    fgVpn2TunEntry.setStatus("current")
_FgVpn2TunIndex_Type = FnIndex
_FgVpn2TunIndex_Object = MibTableColumn
fgVpn2TunIndex = _FgVpn2TunIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 1),
    _FgVpn2TunIndex_Type()
)
fgVpn2TunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgVpn2TunIndex.setStatus("current")
_FgVpn2TunPhase1Name_Type = DisplayString
_FgVpn2TunPhase1Name_Object = MibTableColumn
fgVpn2TunPhase1Name = _FgVpn2TunPhase1Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 2),
    _FgVpn2TunPhase1Name_Type()
)
fgVpn2TunPhase1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunPhase1Name.setStatus("current")
_FgVpn2TunPhase2Name_Type = DisplayString
_FgVpn2TunPhase2Name_Object = MibTableColumn
fgVpn2TunPhase2Name = _FgVpn2TunPhase2Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 3),
    _FgVpn2TunPhase2Name_Type()
)
fgVpn2TunPhase2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunPhase2Name.setStatus("current")
_FgVpn2TunRemGwyIpType_Type = InetAddressType
_FgVpn2TunRemGwyIpType_Object = MibTableColumn
fgVpn2TunRemGwyIpType = _FgVpn2TunRemGwyIpType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 4),
    _FgVpn2TunRemGwyIpType_Type()
)
fgVpn2TunRemGwyIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunRemGwyIpType.setStatus("current")
_FgVpn2TunRemGwyIp_Type = InetAddress
_FgVpn2TunRemGwyIp_Object = MibTableColumn
fgVpn2TunRemGwyIp = _FgVpn2TunRemGwyIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 5),
    _FgVpn2TunRemGwyIp_Type()
)
fgVpn2TunRemGwyIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunRemGwyIp.setStatus("current")
_FgVpn2TunRemGwyPort_Type = InetPortNumber
_FgVpn2TunRemGwyPort_Object = MibTableColumn
fgVpn2TunRemGwyPort = _FgVpn2TunRemGwyPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 6),
    _FgVpn2TunRemGwyPort_Type()
)
fgVpn2TunRemGwyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunRemGwyPort.setStatus("current")
_FgVpn2TunLocGwyIpType_Type = InetAddressType
_FgVpn2TunLocGwyIpType_Object = MibTableColumn
fgVpn2TunLocGwyIpType = _FgVpn2TunLocGwyIpType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 7),
    _FgVpn2TunLocGwyIpType_Type()
)
fgVpn2TunLocGwyIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunLocGwyIpType.setStatus("current")
_FgVpn2TunLocGwyIp_Type = InetAddress
_FgVpn2TunLocGwyIp_Object = MibTableColumn
fgVpn2TunLocGwyIp = _FgVpn2TunLocGwyIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 8),
    _FgVpn2TunLocGwyIp_Type()
)
fgVpn2TunLocGwyIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunLocGwyIp.setStatus("current")
_FgVpn2TunLocGwyPort_Type = InetPortNumber
_FgVpn2TunLocGwyPort_Object = MibTableColumn
fgVpn2TunLocGwyPort = _FgVpn2TunLocGwyPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 9),
    _FgVpn2TunLocGwyPort_Type()
)
fgVpn2TunLocGwyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunLocGwyPort.setStatus("current")
_FgVpn2TunSelSrcBeginIpType_Type = InetAddressType
_FgVpn2TunSelSrcBeginIpType_Object = MibTableColumn
fgVpn2TunSelSrcBeginIpType = _FgVpn2TunSelSrcBeginIpType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 10),
    _FgVpn2TunSelSrcBeginIpType_Type()
)
fgVpn2TunSelSrcBeginIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunSelSrcBeginIpType.setStatus("current")
_FgVpn2TunSelSrcBeginIp_Type = InetAddress
_FgVpn2TunSelSrcBeginIp_Object = MibTableColumn
fgVpn2TunSelSrcBeginIp = _FgVpn2TunSelSrcBeginIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 11),
    _FgVpn2TunSelSrcBeginIp_Type()
)
fgVpn2TunSelSrcBeginIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunSelSrcBeginIp.setStatus("current")
_FgVpn2TunSelSrcEndIpType_Type = InetAddressType
_FgVpn2TunSelSrcEndIpType_Object = MibTableColumn
fgVpn2TunSelSrcEndIpType = _FgVpn2TunSelSrcEndIpType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 12),
    _FgVpn2TunSelSrcEndIpType_Type()
)
fgVpn2TunSelSrcEndIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunSelSrcEndIpType.setStatus("current")
_FgVpn2TunSelSrcEndIp_Type = InetAddress
_FgVpn2TunSelSrcEndIp_Object = MibTableColumn
fgVpn2TunSelSrcEndIp = _FgVpn2TunSelSrcEndIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 13),
    _FgVpn2TunSelSrcEndIp_Type()
)
fgVpn2TunSelSrcEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunSelSrcEndIp.setStatus("current")
_FgVpn2TunSelSrcPort_Type = InetPortNumber
_FgVpn2TunSelSrcPort_Object = MibTableColumn
fgVpn2TunSelSrcPort = _FgVpn2TunSelSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 14),
    _FgVpn2TunSelSrcPort_Type()
)
fgVpn2TunSelSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunSelSrcPort.setStatus("current")
_FgVpn2TunSelDstBeginIpType_Type = InetAddressType
_FgVpn2TunSelDstBeginIpType_Object = MibTableColumn
fgVpn2TunSelDstBeginIpType = _FgVpn2TunSelDstBeginIpType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 15),
    _FgVpn2TunSelDstBeginIpType_Type()
)
fgVpn2TunSelDstBeginIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunSelDstBeginIpType.setStatus("current")
_FgVpn2TunSelDstBeginIp_Type = InetAddress
_FgVpn2TunSelDstBeginIp_Object = MibTableColumn
fgVpn2TunSelDstBeginIp = _FgVpn2TunSelDstBeginIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 16),
    _FgVpn2TunSelDstBeginIp_Type()
)
fgVpn2TunSelDstBeginIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunSelDstBeginIp.setStatus("current")
_FgVpn2TunSelDstEndIpType_Type = InetAddressType
_FgVpn2TunSelDstEndIpType_Object = MibTableColumn
fgVpn2TunSelDstEndIpType = _FgVpn2TunSelDstEndIpType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 17),
    _FgVpn2TunSelDstEndIpType_Type()
)
fgVpn2TunSelDstEndIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunSelDstEndIpType.setStatus("current")
_FgVpn2TunSelDstEndIp_Type = InetAddress
_FgVpn2TunSelDstEndIp_Object = MibTableColumn
fgVpn2TunSelDstEndIp = _FgVpn2TunSelDstEndIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 18),
    _FgVpn2TunSelDstEndIp_Type()
)
fgVpn2TunSelDstEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunSelDstEndIp.setStatus("current")
_FgVpn2TunSelDstPort_Type = InetPortNumber
_FgVpn2TunSelDstPort_Object = MibTableColumn
fgVpn2TunSelDstPort = _FgVpn2TunSelDstPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 19),
    _FgVpn2TunSelDstPort_Type()
)
fgVpn2TunSelDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunSelDstPort.setStatus("current")
_FgVpn2TunSelProto_Type = Integer32
_FgVpn2TunSelProto_Object = MibTableColumn
fgVpn2TunSelProto = _FgVpn2TunSelProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 20),
    _FgVpn2TunSelProto_Type()
)
fgVpn2TunSelProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunSelProto.setStatus("current")
_FgVpn2TunLifeSecs_Type = Gauge32
_FgVpn2TunLifeSecs_Object = MibTableColumn
fgVpn2TunLifeSecs = _FgVpn2TunLifeSecs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 21),
    _FgVpn2TunLifeSecs_Type()
)
fgVpn2TunLifeSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunLifeSecs.setStatus("current")
_FgVpn2TunLifeBytes_Type = Gauge32
_FgVpn2TunLifeBytes_Object = MibTableColumn
fgVpn2TunLifeBytes = _FgVpn2TunLifeBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 22),
    _FgVpn2TunLifeBytes_Type()
)
fgVpn2TunLifeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunLifeBytes.setStatus("current")
_FgVpn2TunTimeout_Type = Gauge32
_FgVpn2TunTimeout_Object = MibTableColumn
fgVpn2TunTimeout = _FgVpn2TunTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 23),
    _FgVpn2TunTimeout_Type()
)
fgVpn2TunTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunTimeout.setStatus("current")
_FgVpn2TunInOctets_Type = Counter64
_FgVpn2TunInOctets_Object = MibTableColumn
fgVpn2TunInOctets = _FgVpn2TunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 24),
    _FgVpn2TunInOctets_Type()
)
fgVpn2TunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunInOctets.setStatus("current")
_FgVpn2TunOutOctets_Type = Counter64
_FgVpn2TunOutOctets_Object = MibTableColumn
fgVpn2TunOutOctets = _FgVpn2TunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 25),
    _FgVpn2TunOutOctets_Type()
)
fgVpn2TunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunOutOctets.setStatus("current")


class _FgVpn2TunStatus_Type(Integer32):
    """Custom type fgVpn2TunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_FgVpn2TunStatus_Type.__name__ = "Integer32"
_FgVpn2TunStatus_Object = MibTableColumn
fgVpn2TunStatus = _FgVpn2TunStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 26),
    _FgVpn2TunStatus_Type()
)
fgVpn2TunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunStatus.setStatus("current")
_FgVpn2TunVdom_Type = FgVdIndex
_FgVpn2TunVdom_Object = MibTableColumn
fgVpn2TunVdom = _FgVpn2TunVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 27),
    _FgVpn2TunVdom_Type()
)
fgVpn2TunVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgVpn2TunVdom.setStatus("current")
_FgVpn2TunPhase2Index_Type = FnIndex
_FgVpn2TunPhase2Index_Object = MibTableColumn
fgVpn2TunPhase2Index = _FgVpn2TunPhase2Index_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 12, 4, 2, 1, 28),
    _FgVpn2TunPhase2Index_Type()
)
fgVpn2TunPhase2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgVpn2TunPhase2Index.setStatus("current")
_FgHighAvailability_ObjectIdentity = ObjectIdentity
fgHighAvailability = _FgHighAvailability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13)
)
_FgHaInfo_ObjectIdentity = ObjectIdentity
fgHaInfo = _FgHaInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1)
)
_FgHaSystemMode_Type = FgHaMode
_FgHaSystemMode_Object = MibScalar
fgHaSystemMode = _FgHaSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1, 1),
    _FgHaSystemMode_Type()
)
fgHaSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaSystemMode.setStatus("current")
_FgHaGroupId_Type = FnIndex
_FgHaGroupId_Object = MibScalar
fgHaGroupId = _FgHaGroupId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1, 2),
    _FgHaGroupId_Type()
)
fgHaGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaGroupId.setStatus("current")


class _FgHaPriority_Type(Integer32):
    """Custom type fgHaPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FgHaPriority_Type.__name__ = "Integer32"
_FgHaPriority_Object = MibScalar
fgHaPriority = _FgHaPriority_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1, 3),
    _FgHaPriority_Type()
)
fgHaPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaPriority.setStatus("current")
_FgHaOverride_Type = FnBoolState
_FgHaOverride_Object = MibScalar
fgHaOverride = _FgHaOverride_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1, 4),
    _FgHaOverride_Type()
)
fgHaOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaOverride.setStatus("current")
_FgHaAutoSync_Type = FnBoolState
_FgHaAutoSync_Object = MibScalar
fgHaAutoSync = _FgHaAutoSync_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1, 5),
    _FgHaAutoSync_Type()
)
fgHaAutoSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaAutoSync.setStatus("current")
_FgHaSchedule_Type = FgHaLBSchedule
_FgHaSchedule_Object = MibScalar
fgHaSchedule = _FgHaSchedule_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1, 6),
    _FgHaSchedule_Type()
)
fgHaSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaSchedule.setStatus("current")
_FgHaGroupName_Type = DisplayString
_FgHaGroupName_Object = MibScalar
fgHaGroupName = _FgHaGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 1, 7),
    _FgHaGroupName_Type()
)
fgHaGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaGroupName.setStatus("current")
_FgHaTables_ObjectIdentity = ObjectIdentity
fgHaTables = _FgHaTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2)
)
_FgHaStatsTable_Object = MibTable
fgHaStatsTable = _FgHaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1)
)
if mibBuilder.loadTexts:
    fgHaStatsTable.setStatus("current")
_FgHaStatsEntry_Object = MibTableRow
fgHaStatsEntry = _FgHaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1)
)
fgHaStatsEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgHaStatsIndex"),
)
if mibBuilder.loadTexts:
    fgHaStatsEntry.setStatus("current")
_FgHaStatsIndex_Type = FnIndex
_FgHaStatsIndex_Object = MibTableColumn
fgHaStatsIndex = _FgHaStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 1),
    _FgHaStatsIndex_Type()
)
fgHaStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgHaStatsIndex.setStatus("current")


class _FgHaStatsSerial_Type(DisplayString):
    """Custom type fgHaStatsSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgHaStatsSerial_Type.__name__ = "DisplayString"
_FgHaStatsSerial_Object = MibTableColumn
fgHaStatsSerial = _FgHaStatsSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 2),
    _FgHaStatsSerial_Type()
)
fgHaStatsSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsSerial.setStatus("current")


class _FgHaStatsCpuUsage_Type(Gauge32):
    """Custom type fgHaStatsCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgHaStatsCpuUsage_Type.__name__ = "Gauge32"
_FgHaStatsCpuUsage_Object = MibTableColumn
fgHaStatsCpuUsage = _FgHaStatsCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 3),
    _FgHaStatsCpuUsage_Type()
)
fgHaStatsCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsCpuUsage.setStatus("current")


class _FgHaStatsMemUsage_Type(Gauge32):
    """Custom type fgHaStatsMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgHaStatsMemUsage_Type.__name__ = "Gauge32"
_FgHaStatsMemUsage_Object = MibTableColumn
fgHaStatsMemUsage = _FgHaStatsMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 4),
    _FgHaStatsMemUsage_Type()
)
fgHaStatsMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsMemUsage.setStatus("current")
_FgHaStatsNetUsage_Type = Gauge32
_FgHaStatsNetUsage_Object = MibTableColumn
fgHaStatsNetUsage = _FgHaStatsNetUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 5),
    _FgHaStatsNetUsage_Type()
)
fgHaStatsNetUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsNetUsage.setStatus("current")
_FgHaStatsSesCount_Type = Gauge32
_FgHaStatsSesCount_Object = MibTableColumn
fgHaStatsSesCount = _FgHaStatsSesCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 6),
    _FgHaStatsSesCount_Type()
)
fgHaStatsSesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsSesCount.setStatus("current")
_FgHaStatsPktCount_Type = Counter32
_FgHaStatsPktCount_Object = MibTableColumn
fgHaStatsPktCount = _FgHaStatsPktCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 7),
    _FgHaStatsPktCount_Type()
)
fgHaStatsPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsPktCount.setStatus("current")
_FgHaStatsByteCount_Type = Counter32
_FgHaStatsByteCount_Object = MibTableColumn
fgHaStatsByteCount = _FgHaStatsByteCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 8),
    _FgHaStatsByteCount_Type()
)
fgHaStatsByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsByteCount.setStatus("current")
_FgHaStatsIdsCount_Type = Counter32
_FgHaStatsIdsCount_Object = MibTableColumn
fgHaStatsIdsCount = _FgHaStatsIdsCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 9),
    _FgHaStatsIdsCount_Type()
)
fgHaStatsIdsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsIdsCount.setStatus("current")
_FgHaStatsAvCount_Type = Counter32
_FgHaStatsAvCount_Object = MibTableColumn
fgHaStatsAvCount = _FgHaStatsAvCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 10),
    _FgHaStatsAvCount_Type()
)
fgHaStatsAvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsAvCount.setStatus("current")


class _FgHaStatsHostname_Type(DisplayString):
    """Custom type fgHaStatsHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FgHaStatsHostname_Type.__name__ = "DisplayString"
_FgHaStatsHostname_Object = MibTableColumn
fgHaStatsHostname = _FgHaStatsHostname_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 11),
    _FgHaStatsHostname_Type()
)
fgHaStatsHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsHostname.setStatus("current")
_FgHaStatsSyncStatus_Type = FgHaStatsSyncStatusType
_FgHaStatsSyncStatus_Object = MibTableColumn
fgHaStatsSyncStatus = _FgHaStatsSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 12),
    _FgHaStatsSyncStatus_Type()
)
fgHaStatsSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsSyncStatus.setStatus("current")
_FgHaStatsSyncDatimeSucc_Type = DateAndTime
_FgHaStatsSyncDatimeSucc_Object = MibTableColumn
fgHaStatsSyncDatimeSucc = _FgHaStatsSyncDatimeSucc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 13),
    _FgHaStatsSyncDatimeSucc_Type()
)
fgHaStatsSyncDatimeSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsSyncDatimeSucc.setStatus("current")
_FgHaStatsSyncDatimeUnsucc_Type = DateAndTime
_FgHaStatsSyncDatimeUnsucc_Object = MibTableColumn
fgHaStatsSyncDatimeUnsucc = _FgHaStatsSyncDatimeUnsucc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 14),
    _FgHaStatsSyncDatimeUnsucc_Type()
)
fgHaStatsSyncDatimeUnsucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsSyncDatimeUnsucc.setStatus("current")


class _FgHaStatsGlobalChecksum_Type(DisplayString):
    """Custom type fgHaStatsGlobalChecksum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgHaStatsGlobalChecksum_Type.__name__ = "DisplayString"
_FgHaStatsGlobalChecksum_Object = MibTableColumn
fgHaStatsGlobalChecksum = _FgHaStatsGlobalChecksum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 15),
    _FgHaStatsGlobalChecksum_Type()
)
fgHaStatsGlobalChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsGlobalChecksum.setStatus("current")


class _FgHaStatsPrimarySerial_Type(DisplayString):
    """Custom type fgHaStatsPrimarySerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgHaStatsPrimarySerial_Type.__name__ = "DisplayString"
_FgHaStatsPrimarySerial_Object = MibTableColumn
fgHaStatsPrimarySerial = _FgHaStatsPrimarySerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 16),
    _FgHaStatsPrimarySerial_Type()
)
fgHaStatsPrimarySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsPrimarySerial.setStatus("current")


class _FgHaStatsAllChecksum_Type(DisplayString):
    """Custom type fgHaStatsAllChecksum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgHaStatsAllChecksum_Type.__name__ = "DisplayString"
_FgHaStatsAllChecksum_Object = MibTableColumn
fgHaStatsAllChecksum = _FgHaStatsAllChecksum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 2, 1, 1, 17),
    _FgHaStatsAllChecksum_Type()
)
fgHaStatsAllChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHaStatsAllChecksum.setStatus("current")
_FgHaTrapObjects_ObjectIdentity = ObjectIdentity
fgHaTrapObjects = _FgHaTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 3)
)
_FgHaTrapMemberSerial_Type = DisplayString
_FgHaTrapMemberSerial_Object = MibScalar
fgHaTrapMemberSerial = _FgHaTrapMemberSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 13, 3, 1),
    _FgHaTrapMemberSerial_Type()
)
fgHaTrapMemberSerial.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgHaTrapMemberSerial.setStatus("current")
_FgWc_ObjectIdentity = ObjectIdentity
fgWc = _FgWc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14)
)
_FgWcTrapObjects_ObjectIdentity = ObjectIdentity
fgWcTrapObjects = _FgWcTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 1)
)
_FgWcApVdom_Type = FgVdIndex
_FgWcApVdom_Object = MibScalar
fgWcApVdom = _FgWcApVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 1, 1),
    _FgWcApVdom_Type()
)
fgWcApVdom.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgWcApVdom.setStatus("current")


class _FgWcApSerial_Type(DisplayString):
    """Custom type fgWcApSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgWcApSerial_Type.__name__ = "DisplayString"
_FgWcApSerial_Object = MibScalar
fgWcApSerial = _FgWcApSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 1, 2),
    _FgWcApSerial_Type()
)
fgWcApSerial.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgWcApSerial.setStatus("current")


class _FgWcApName_Type(DisplayString):
    """Custom type fgWcApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgWcApName_Type.__name__ = "DisplayString"
_FgWcApName_Object = MibScalar
fgWcApName = _FgWcApName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 1, 3),
    _FgWcApName_Type()
)
fgWcApName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgWcApName.setStatus("current")
_FgWcInfo_ObjectIdentity = ObjectIdentity
fgWcInfo = _FgWcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2)
)
_FgWcInfoName_Type = DisplayString
_FgWcInfoName_Object = MibScalar
fgWcInfoName = _FgWcInfoName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2, 1),
    _FgWcInfoName_Type()
)
fgWcInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcInfoName.setStatus("current")
_FgWcInfoLocation_Type = DisplayString
_FgWcInfoLocation_Object = MibScalar
fgWcInfoLocation = _FgWcInfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2, 2),
    _FgWcInfoLocation_Type()
)
fgWcInfoLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcInfoLocation.setStatus("current")
_FgWcInfoWtpCapacity_Type = Unsigned32
_FgWcInfoWtpCapacity_Object = MibScalar
fgWcInfoWtpCapacity = _FgWcInfoWtpCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2, 3),
    _FgWcInfoWtpCapacity_Type()
)
fgWcInfoWtpCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcInfoWtpCapacity.setStatus("current")
_FgWcInfoWtpManaged_Type = Unsigned32
_FgWcInfoWtpManaged_Object = MibScalar
fgWcInfoWtpManaged = _FgWcInfoWtpManaged_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2, 4),
    _FgWcInfoWtpManaged_Type()
)
fgWcInfoWtpManaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcInfoWtpManaged.setStatus("current")
_FgWcInfoWtpSessions_Type = Gauge32
_FgWcInfoWtpSessions_Object = MibScalar
fgWcInfoWtpSessions = _FgWcInfoWtpSessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2, 5),
    _FgWcInfoWtpSessions_Type()
)
fgWcInfoWtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcInfoWtpSessions.setStatus("current")
_FgWcInfoStationCapacity_Type = Unsigned32
_FgWcInfoStationCapacity_Object = MibScalar
fgWcInfoStationCapacity = _FgWcInfoStationCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2, 6),
    _FgWcInfoStationCapacity_Type()
)
fgWcInfoStationCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcInfoStationCapacity.setStatus("current")
_FgWcInfoStationCount_Type = Gauge32
_FgWcInfoStationCount_Object = MibScalar
fgWcInfoStationCount = _FgWcInfoStationCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 2, 7),
    _FgWcInfoStationCount_Type()
)
fgWcInfoStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcInfoStationCount.setStatus("current")
_FgWcWlanTable_Object = MibTable
fgWcWlanTable = _FgWcWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3)
)
if mibBuilder.loadTexts:
    fgWcWlanTable.setStatus("current")
_FgWcWlanEntry_Object = MibTableRow
fgWcWlanEntry = _FgWcWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1)
)
fgWcWlanEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fgWcWlanEntry.setStatus("current")


class _FgWcWlanSsid_Type(OctetString):
    """Custom type fgWcWlanSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgWcWlanSsid_Type.__name__ = "OctetString"
_FgWcWlanSsid_Object = MibTableColumn
fgWcWlanSsid = _FgWcWlanSsid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 1),
    _FgWcWlanSsid_Type()
)
fgWcWlanSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanSsid.setStatus("current")
_FgWcWlanBroadcastSsid_Type = FnBoolState
_FgWcWlanBroadcastSsid_Object = MibTableColumn
fgWcWlanBroadcastSsid = _FgWcWlanBroadcastSsid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 2),
    _FgWcWlanBroadcastSsid_Type()
)
fgWcWlanBroadcastSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanBroadcastSsid.setStatus("current")
_FgWcWlanSecurity_Type = FgWcWlanSecurityType
_FgWcWlanSecurity_Object = MibTableColumn
fgWcWlanSecurity = _FgWcWlanSecurity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 3),
    _FgWcWlanSecurity_Type()
)
fgWcWlanSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanSecurity.setStatus("current")
_FgWcWlanEncryption_Type = FgWcWlanEncryptionType
_FgWcWlanEncryption_Object = MibTableColumn
fgWcWlanEncryption = _FgWcWlanEncryption_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 4),
    _FgWcWlanEncryption_Type()
)
fgWcWlanEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanEncryption.setStatus("current")
_FgWcWlanAuthentication_Type = FgWcWlanAuthenticationType
_FgWcWlanAuthentication_Object = MibTableColumn
fgWcWlanAuthentication = _FgWcWlanAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 5),
    _FgWcWlanAuthentication_Type()
)
fgWcWlanAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanAuthentication.setStatus("current")
_FgWcWlanRadiusServer_Type = DisplayString
_FgWcWlanRadiusServer_Object = MibTableColumn
fgWcWlanRadiusServer = _FgWcWlanRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 6),
    _FgWcWlanRadiusServer_Type()
)
fgWcWlanRadiusServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanRadiusServer.setStatus("current")
_FgWcWlanUserGroup_Type = DisplayString
_FgWcWlanUserGroup_Object = MibTableColumn
fgWcWlanUserGroup = _FgWcWlanUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 7),
    _FgWcWlanUserGroup_Type()
)
fgWcWlanUserGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanUserGroup.setStatus("current")
_FgWcWlanLocalBridging_Type = FnBoolState
_FgWcWlanLocalBridging_Object = MibTableColumn
fgWcWlanLocalBridging = _FgWcWlanLocalBridging_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 8),
    _FgWcWlanLocalBridging_Type()
)
fgWcWlanLocalBridging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanLocalBridging.setStatus("current")


class _FgWcWlanVlanId_Type(Integer32):
    """Custom type fgWcWlanVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_FgWcWlanVlanId_Type.__name__ = "Integer32"
_FgWcWlanVlanId_Object = MibTableColumn
fgWcWlanVlanId = _FgWcWlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 9),
    _FgWcWlanVlanId_Type()
)
fgWcWlanVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanVlanId.setStatus("current")
_FgWcWlanMeshBackhaul_Type = FnBoolState
_FgWcWlanMeshBackhaul_Object = MibTableColumn
fgWcWlanMeshBackhaul = _FgWcWlanMeshBackhaul_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 10),
    _FgWcWlanMeshBackhaul_Type()
)
fgWcWlanMeshBackhaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanMeshBackhaul.setStatus("current")
_FgWcWlanStationCapacity_Type = Unsigned32
_FgWcWlanStationCapacity_Object = MibTableColumn
fgWcWlanStationCapacity = _FgWcWlanStationCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 11),
    _FgWcWlanStationCapacity_Type()
)
fgWcWlanStationCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanStationCapacity.setStatus("current")
_FgWcWlanStationCount_Type = Gauge32
_FgWcWlanStationCount_Object = MibTableColumn
fgWcWlanStationCount = _FgWcWlanStationCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 12),
    _FgWcWlanStationCount_Type()
)
fgWcWlanStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanStationCount.setStatus("current")
_FgWcWlanCPAuth_Type = FnBoolState
_FgWcWlanCPAuth_Object = MibTableColumn
fgWcWlanCPAuth = _FgWcWlanCPAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 3, 1, 13),
    _FgWcWlanCPAuth_Type()
)
fgWcWlanCPAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWlanCPAuth.setStatus("current")
_FgWcWtpTables_ObjectIdentity = ObjectIdentity
fgWcWtpTables = _FgWcWtpTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4)
)
_FgWcWtpProfileTable_Object = MibTable
fgWcWtpProfileTable = _FgWcWtpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 1)
)
if mibBuilder.loadTexts:
    fgWcWtpProfileTable.setStatus("current")
_FgWcWtpProfileEntry_Object = MibTableRow
fgWcWtpProfileEntry = _FgWcWtpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 1, 1)
)
fgWcWtpProfileEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpProfileName"),
)
if mibBuilder.loadTexts:
    fgWcWtpProfileEntry.setStatus("current")


class _FgWcWtpProfileName_Type(DisplayString):
    """Custom type fgWcWtpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_FgWcWtpProfileName_Type.__name__ = "DisplayString"
_FgWcWtpProfileName_Object = MibTableColumn
fgWcWtpProfileName = _FgWcWtpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 1, 1, 1),
    _FgWcWtpProfileName_Type()
)
fgWcWtpProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpProfileName.setStatus("current")
_FgWcWtpProfilePlatform_Type = DisplayString
_FgWcWtpProfilePlatform_Object = MibTableColumn
fgWcWtpProfilePlatform = _FgWcWtpProfilePlatform_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 1, 1, 2),
    _FgWcWtpProfilePlatform_Type()
)
fgWcWtpProfilePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfilePlatform.setStatus("current")


class _FgWcWtpProfileDataChannelDtlsPolicy_Type(Bits):
    """Custom type fgWcWtpProfileDataChannelDtlsPolicy based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("clear", 1),
          ("dtls", 2),
          ("ipsec", 3),
          ("ipsecsn", 4))
    )

_FgWcWtpProfileDataChannelDtlsPolicy_Type.__name__ = "Bits"
_FgWcWtpProfileDataChannelDtlsPolicy_Object = MibTableColumn
fgWcWtpProfileDataChannelDtlsPolicy = _FgWcWtpProfileDataChannelDtlsPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 1, 1, 3),
    _FgWcWtpProfileDataChannelDtlsPolicy_Type()
)
fgWcWtpProfileDataChannelDtlsPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileDataChannelDtlsPolicy.setStatus("current")
_FgWcWtpProfileCountryString_Type = FgWcCountryString
_FgWcWtpProfileCountryString_Object = MibTableColumn
fgWcWtpProfileCountryString = _FgWcWtpProfileCountryString_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 1, 1, 4),
    _FgWcWtpProfileCountryString_Type()
)
fgWcWtpProfileCountryString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileCountryString.setStatus("current")
_FgWcWtpProfileRadioTable_Object = MibTable
fgWcWtpProfileRadioTable = _FgWcWtpProfileRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2)
)
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioTable.setStatus("current")
_FgWcWtpProfileRadioEntry_Object = MibTableRow
fgWcWtpProfileRadioEntry = _FgWcWtpProfileRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1)
)
fgWcWtpProfileRadioEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioProfileName"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioRadioId"),
)
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioEntry.setStatus("current")


class _FgWcWtpProfileRadioProfileName_Type(DisplayString):
    """Custom type fgWcWtpProfileRadioProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_FgWcWtpProfileRadioProfileName_Type.__name__ = "DisplayString"
_FgWcWtpProfileRadioProfileName_Object = MibTableColumn
fgWcWtpProfileRadioProfileName = _FgWcWtpProfileRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 1),
    _FgWcWtpProfileRadioProfileName_Type()
)
fgWcWtpProfileRadioProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioProfileName.setStatus("current")
_FgWcWtpProfileRadioRadioId_Type = FgWcWtpRadioId
_FgWcWtpProfileRadioRadioId_Object = MibTableColumn
fgWcWtpProfileRadioRadioId = _FgWcWtpProfileRadioRadioId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 2),
    _FgWcWtpProfileRadioRadioId_Type()
)
fgWcWtpProfileRadioRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioRadioId.setStatus("current")
_FgWcWtpProfileRadioMode_Type = FgWcWtpRadioMode
_FgWcWtpProfileRadioMode_Object = MibTableColumn
fgWcWtpProfileRadioMode = _FgWcWtpProfileRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 3),
    _FgWcWtpProfileRadioMode_Type()
)
fgWcWtpProfileRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioMode.setStatus("current")
_FgWcWtpProfileRadioApScan_Type = FnBoolState
_FgWcWtpProfileRadioApScan_Object = MibTableColumn
fgWcWtpProfileRadioApScan = _FgWcWtpProfileRadioApScan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 4),
    _FgWcWtpProfileRadioApScan_Type()
)
fgWcWtpProfileRadioApScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioApScan.setStatus("current")
_FgWcWtpProfileRadioWidsProfile_Type = DisplayString
_FgWcWtpProfileRadioWidsProfile_Object = MibTableColumn
fgWcWtpProfileRadioWidsProfile = _FgWcWtpProfileRadioWidsProfile_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 5),
    _FgWcWtpProfileRadioWidsProfile_Type()
)
fgWcWtpProfileRadioWidsProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioWidsProfile.setStatus("current")
_FgWcWtpProfileRadioDarrp_Type = FnBoolState
_FgWcWtpProfileRadioDarrp_Object = MibTableColumn
fgWcWtpProfileRadioDarrp = _FgWcWtpProfileRadioDarrp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 6),
    _FgWcWtpProfileRadioDarrp_Type()
)
fgWcWtpProfileRadioDarrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioDarrp.setStatus("current")
_FgWcWtpProfileRadioFrequencyHandoff_Type = FnBoolState
_FgWcWtpProfileRadioFrequencyHandoff_Object = MibTableColumn
fgWcWtpProfileRadioFrequencyHandoff = _FgWcWtpProfileRadioFrequencyHandoff_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 7),
    _FgWcWtpProfileRadioFrequencyHandoff_Type()
)
fgWcWtpProfileRadioFrequencyHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioFrequencyHandoff.setStatus("current")
_FgWcWtpProfileRadioApHandoff_Type = FnBoolState
_FgWcWtpProfileRadioApHandoff_Object = MibTableColumn
fgWcWtpProfileRadioApHandoff = _FgWcWtpProfileRadioApHandoff_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 8),
    _FgWcWtpProfileRadioApHandoff_Type()
)
fgWcWtpProfileRadioApHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioApHandoff.setStatus("current")


class _FgWcWtpProfileRadioBeaconInterval_Type(Integer32):
    """Custom type fgWcWtpProfileRadioBeaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FgWcWtpProfileRadioBeaconInterval_Type.__name__ = "Integer32"
_FgWcWtpProfileRadioBeaconInterval_Object = MibTableColumn
fgWcWtpProfileRadioBeaconInterval = _FgWcWtpProfileRadioBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 9),
    _FgWcWtpProfileRadioBeaconInterval_Type()
)
fgWcWtpProfileRadioBeaconInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioBeaconInterval.setStatus("current")


class _FgWcWtpProfileRadioDtimPeriod_Type(Integer32):
    """Custom type fgWcWtpProfileRadioDtimPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FgWcWtpProfileRadioDtimPeriod_Type.__name__ = "Integer32"
_FgWcWtpProfileRadioDtimPeriod_Object = MibTableColumn
fgWcWtpProfileRadioDtimPeriod = _FgWcWtpProfileRadioDtimPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 10),
    _FgWcWtpProfileRadioDtimPeriod_Type()
)
fgWcWtpProfileRadioDtimPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioDtimPeriod.setStatus("current")
_FgWcWtpProfileRadioBand_Type = FgWcWtpRadioType
_FgWcWtpProfileRadioBand_Object = MibTableColumn
fgWcWtpProfileRadioBand = _FgWcWtpProfileRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 11),
    _FgWcWtpProfileRadioBand_Type()
)
fgWcWtpProfileRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioBand.setStatus("current")
_FgWcWtpProfileRadioChannelBonding_Type = FnBoolState
_FgWcWtpProfileRadioChannelBonding_Object = MibTableColumn
fgWcWtpProfileRadioChannelBonding = _FgWcWtpProfileRadioChannelBonding_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 12),
    _FgWcWtpProfileRadioChannelBonding_Type()
)
fgWcWtpProfileRadioChannelBonding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioChannelBonding.setStatus("current")
_FgWcWtpProfileRadioChannel_Type = DisplayString
_FgWcWtpProfileRadioChannel_Object = MibTableColumn
fgWcWtpProfileRadioChannel = _FgWcWtpProfileRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 13),
    _FgWcWtpProfileRadioChannel_Type()
)
fgWcWtpProfileRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioChannel.setStatus("current")
_FgWcWtpProfileRadioAutoTxPowerControl_Type = FnBoolState
_FgWcWtpProfileRadioAutoTxPowerControl_Object = MibTableColumn
fgWcWtpProfileRadioAutoTxPowerControl = _FgWcWtpProfileRadioAutoTxPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 14),
    _FgWcWtpProfileRadioAutoTxPowerControl_Type()
)
fgWcWtpProfileRadioAutoTxPowerControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioAutoTxPowerControl.setStatus("current")
_FgWcWtpProfileRadioAutoTxPowerLow_Type = Integer32
_FgWcWtpProfileRadioAutoTxPowerLow_Object = MibTableColumn
fgWcWtpProfileRadioAutoTxPowerLow = _FgWcWtpProfileRadioAutoTxPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 15),
    _FgWcWtpProfileRadioAutoTxPowerLow_Type()
)
fgWcWtpProfileRadioAutoTxPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioAutoTxPowerLow.setStatus("current")
_FgWcWtpProfileRadioAutoTxPowerHigh_Type = Integer32
_FgWcWtpProfileRadioAutoTxPowerHigh_Object = MibTableColumn
fgWcWtpProfileRadioAutoTxPowerHigh = _FgWcWtpProfileRadioAutoTxPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 16),
    _FgWcWtpProfileRadioAutoTxPowerHigh_Type()
)
fgWcWtpProfileRadioAutoTxPowerHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioAutoTxPowerHigh.setStatus("current")


class _FgWcWtpProfileRadioTxPowerLevel_Type(Gauge32):
    """Custom type fgWcWtpProfileRadioTxPowerLevel based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgWcWtpProfileRadioTxPowerLevel_Type.__name__ = "Gauge32"
_FgWcWtpProfileRadioTxPowerLevel_Object = MibTableColumn
fgWcWtpProfileRadioTxPowerLevel = _FgWcWtpProfileRadioTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 17),
    _FgWcWtpProfileRadioTxPowerLevel_Type()
)
fgWcWtpProfileRadioTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioTxPowerLevel.setStatus("current")
_FgWcWtpProfileRadioVaps_Type = DisplayString
_FgWcWtpProfileRadioVaps_Object = MibTableColumn
fgWcWtpProfileRadioVaps = _FgWcWtpProfileRadioVaps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 18),
    _FgWcWtpProfileRadioVaps_Type()
)
fgWcWtpProfileRadioVaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioVaps.setStatus("current")
_FgWcWtpProfileRadioStationCapacity_Type = Unsigned32
_FgWcWtpProfileRadioStationCapacity_Object = MibTableColumn
fgWcWtpProfileRadioStationCapacity = _FgWcWtpProfileRadioStationCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 19),
    _FgWcWtpProfileRadioStationCapacity_Type()
)
fgWcWtpProfileRadioStationCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioStationCapacity.setStatus("current")
_FgWcWtpProfileRadioChannelWidth_Type = FgWcWtpChannelWidthType
_FgWcWtpProfileRadioChannelWidth_Object = MibTableColumn
fgWcWtpProfileRadioChannelWidth = _FgWcWtpProfileRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 2, 1, 20),
    _FgWcWtpProfileRadioChannelWidth_Type()
)
fgWcWtpProfileRadioChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpProfileRadioChannelWidth.setStatus("current")
_FgWcWtpConfigTable_Object = MibTable
fgWcWtpConfigTable = _FgWcWtpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3)
)
if mibBuilder.loadTexts:
    fgWcWtpConfigTable.setStatus("current")
_FgWcWtpConfigEntry_Object = MibTableRow
fgWcWtpConfigEntry = _FgWcWtpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1)
)
fgWcWtpConfigEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpConfigWtpId"),
)
if mibBuilder.loadTexts:
    fgWcWtpConfigEntry.setStatus("current")


class _FgWcWtpConfigWtpId_Type(DisplayString):
    """Custom type fgWcWtpConfigWtpId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_FgWcWtpConfigWtpId_Type.__name__ = "DisplayString"
_FgWcWtpConfigWtpId_Object = MibTableColumn
fgWcWtpConfigWtpId = _FgWcWtpConfigWtpId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 1),
    _FgWcWtpConfigWtpId_Type()
)
fgWcWtpConfigWtpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpConfigWtpId.setStatus("current")


class _FgWcWtpConfigWtpAdmin_Type(Integer32):
    """Custom type fgWcWtpConfigWtpAdmin based on Integer32"""
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
        *(("other", 0),
          ("discovered", 1),
          ("disable", 2),
          ("enable", 3))
    )


_FgWcWtpConfigWtpAdmin_Type.__name__ = "Integer32"
_FgWcWtpConfigWtpAdmin_Object = MibTableColumn
fgWcWtpConfigWtpAdmin = _FgWcWtpConfigWtpAdmin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 2),
    _FgWcWtpConfigWtpAdmin_Type()
)
fgWcWtpConfigWtpAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigWtpAdmin.setStatus("current")
_FgWcWtpConfigWtpName_Type = DisplayString
_FgWcWtpConfigWtpName_Object = MibTableColumn
fgWcWtpConfigWtpName = _FgWcWtpConfigWtpName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 3),
    _FgWcWtpConfigWtpName_Type()
)
fgWcWtpConfigWtpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigWtpName.setStatus("current")
_FgWcWtpConfigWtpLocation_Type = DisplayString
_FgWcWtpConfigWtpLocation_Object = MibTableColumn
fgWcWtpConfigWtpLocation = _FgWcWtpConfigWtpLocation_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 4),
    _FgWcWtpConfigWtpLocation_Type()
)
fgWcWtpConfigWtpLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigWtpLocation.setStatus("current")
_FgWcWtpConfigWtpProfile_Type = DisplayString
_FgWcWtpConfigWtpProfile_Object = MibTableColumn
fgWcWtpConfigWtpProfile = _FgWcWtpConfigWtpProfile_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 5),
    _FgWcWtpConfigWtpProfile_Type()
)
fgWcWtpConfigWtpProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigWtpProfile.setStatus("current")
_FgWcWtpConfigRadioEnable_Type = FnBoolState
_FgWcWtpConfigRadioEnable_Object = MibTableColumn
fgWcWtpConfigRadioEnable = _FgWcWtpConfigRadioEnable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 6),
    _FgWcWtpConfigRadioEnable_Type()
)
fgWcWtpConfigRadioEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigRadioEnable.setStatus("current")
_FgWcWtpConfigRadioAutoTxPowerControl_Type = FnBoolState
_FgWcWtpConfigRadioAutoTxPowerControl_Object = MibTableColumn
fgWcWtpConfigRadioAutoTxPowerControl = _FgWcWtpConfigRadioAutoTxPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 7),
    _FgWcWtpConfigRadioAutoTxPowerControl_Type()
)
fgWcWtpConfigRadioAutoTxPowerControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigRadioAutoTxPowerControl.setStatus("current")
_FgWcWtpConfigRadioAutoTxPowerLow_Type = Integer32
_FgWcWtpConfigRadioAutoTxPowerLow_Object = MibTableColumn
fgWcWtpConfigRadioAutoTxPowerLow = _FgWcWtpConfigRadioAutoTxPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 8),
    _FgWcWtpConfigRadioAutoTxPowerLow_Type()
)
fgWcWtpConfigRadioAutoTxPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigRadioAutoTxPowerLow.setStatus("current")
_FgWcWtpConfigRadioAutoTxPowerHigh_Type = Integer32
_FgWcWtpConfigRadioAutoTxPowerHigh_Object = MibTableColumn
fgWcWtpConfigRadioAutoTxPowerHigh = _FgWcWtpConfigRadioAutoTxPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 9),
    _FgWcWtpConfigRadioAutoTxPowerHigh_Type()
)
fgWcWtpConfigRadioAutoTxPowerHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigRadioAutoTxPowerHigh.setStatus("current")


class _FgWcWtpConfigRadioTxPowerLevel_Type(Gauge32):
    """Custom type fgWcWtpConfigRadioTxPowerLevel based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgWcWtpConfigRadioTxPowerLevel_Type.__name__ = "Gauge32"
_FgWcWtpConfigRadioTxPowerLevel_Object = MibTableColumn
fgWcWtpConfigRadioTxPowerLevel = _FgWcWtpConfigRadioTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 10),
    _FgWcWtpConfigRadioTxPowerLevel_Type()
)
fgWcWtpConfigRadioTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigRadioTxPowerLevel.setStatus("current")
_FgWcWtpConfigRadioBand_Type = FgWcWtpRadioBandType
_FgWcWtpConfigRadioBand_Object = MibTableColumn
fgWcWtpConfigRadioBand = _FgWcWtpConfigRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 11),
    _FgWcWtpConfigRadioBand_Type()
)
fgWcWtpConfigRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigRadioBand.setStatus("current")
_FgWcWtpConfigRadioApScan_Type = FnBoolState
_FgWcWtpConfigRadioApScan_Object = MibTableColumn
fgWcWtpConfigRadioApScan = _FgWcWtpConfigRadioApScan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 12),
    _FgWcWtpConfigRadioApScan_Type()
)
fgWcWtpConfigRadioApScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigRadioApScan.setStatus("current")
_FgWcWtpConfigVapAll_Type = FnBoolState
_FgWcWtpConfigVapAll_Object = MibTableColumn
fgWcWtpConfigVapAll = _FgWcWtpConfigVapAll_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 13),
    _FgWcWtpConfigVapAll_Type()
)
fgWcWtpConfigVapAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigVapAll.setStatus("current")
_FgWcWtpConfigVaps_Type = DisplayString
_FgWcWtpConfigVaps_Object = MibTableColumn
fgWcWtpConfigVaps = _FgWcWtpConfigVaps_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 3, 1, 14),
    _FgWcWtpConfigVaps_Type()
)
fgWcWtpConfigVaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpConfigVaps.setStatus("current")
_FgWcWtpSessionTable_Object = MibTable
fgWcWtpSessionTable = _FgWcWtpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4)
)
if mibBuilder.loadTexts:
    fgWcWtpSessionTable.setStatus("current")
_FgWcWtpSessionEntry_Object = MibTableRow
fgWcWtpSessionEntry = _FgWcWtpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1)
)
fgWcWtpSessionEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpId"),
)
if mibBuilder.loadTexts:
    fgWcWtpSessionEntry.setStatus("current")


class _FgWcWtpSessionWtpId_Type(DisplayString):
    """Custom type fgWcWtpSessionWtpId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_FgWcWtpSessionWtpId_Type.__name__ = "DisplayString"
_FgWcWtpSessionWtpId_Object = MibTableColumn
fgWcWtpSessionWtpId = _FgWcWtpSessionWtpId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 1),
    _FgWcWtpSessionWtpId_Type()
)
fgWcWtpSessionWtpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpId.setStatus("current")
_FgWcWtpSessionWtpIpAddressType_Type = InetAddressType
_FgWcWtpSessionWtpIpAddressType_Object = MibTableColumn
fgWcWtpSessionWtpIpAddressType = _FgWcWtpSessionWtpIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 2),
    _FgWcWtpSessionWtpIpAddressType_Type()
)
fgWcWtpSessionWtpIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpIpAddressType.setStatus("current")
_FgWcWtpSessionWtpIpAddress_Type = InetAddress
_FgWcWtpSessionWtpIpAddress_Object = MibTableColumn
fgWcWtpSessionWtpIpAddress = _FgWcWtpSessionWtpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 3),
    _FgWcWtpSessionWtpIpAddress_Type()
)
fgWcWtpSessionWtpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpIpAddress.setStatus("current")
_FgWcWtpSessionWtpLocalIpAddressType_Type = InetAddressType
_FgWcWtpSessionWtpLocalIpAddressType_Object = MibTableColumn
fgWcWtpSessionWtpLocalIpAddressType = _FgWcWtpSessionWtpLocalIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 4),
    _FgWcWtpSessionWtpLocalIpAddressType_Type()
)
fgWcWtpSessionWtpLocalIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpLocalIpAddressType.setStatus("current")
_FgWcWtpSessionWtpLocalIpAddress_Type = InetAddress
_FgWcWtpSessionWtpLocalIpAddress_Object = MibTableColumn
fgWcWtpSessionWtpLocalIpAddress = _FgWcWtpSessionWtpLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 5),
    _FgWcWtpSessionWtpLocalIpAddress_Type()
)
fgWcWtpSessionWtpLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpLocalIpAddress.setStatus("current")


class _FgWcWtpSessionWtpBaseMacAddress_Type(PhysAddress):
    """Custom type fgWcWtpSessionWtpBaseMacAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_FgWcWtpSessionWtpBaseMacAddress_Type.__name__ = "PhysAddress"
_FgWcWtpSessionWtpBaseMacAddress_Object = MibTableColumn
fgWcWtpSessionWtpBaseMacAddress = _FgWcWtpSessionWtpBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 6),
    _FgWcWtpSessionWtpBaseMacAddress_Type()
)
fgWcWtpSessionWtpBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpBaseMacAddress.setStatus("current")


class _FgWcWtpSessionConnectionState_Type(Integer32):
    """Custom type fgWcWtpSessionConnectionState based on Integer32"""
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
        *(("other", 0),
          ("offLine", 1),
          ("onLine", 2),
          ("downloadingImage", 3),
          ("connectedImage", 4),
          ("standby", 5))
    )


_FgWcWtpSessionConnectionState_Type.__name__ = "Integer32"
_FgWcWtpSessionConnectionState_Object = MibTableColumn
fgWcWtpSessionConnectionState = _FgWcWtpSessionConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 7),
    _FgWcWtpSessionConnectionState_Type()
)
fgWcWtpSessionConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionConnectionState.setStatus("current")
_FgWcWtpSessionWtpUpTime_Type = TimeTicks
_FgWcWtpSessionWtpUpTime_Object = MibTableColumn
fgWcWtpSessionWtpUpTime = _FgWcWtpSessionWtpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 8),
    _FgWcWtpSessionWtpUpTime_Type()
)
fgWcWtpSessionWtpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpUpTime.setStatus("current")
_FgWcWtpSessionWtpDaemonUpTime_Type = TimeTicks
_FgWcWtpSessionWtpDaemonUpTime_Object = MibTableColumn
fgWcWtpSessionWtpDaemonUpTime = _FgWcWtpSessionWtpDaemonUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 9),
    _FgWcWtpSessionWtpDaemonUpTime_Type()
)
fgWcWtpSessionWtpDaemonUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpDaemonUpTime.setStatus("current")
_FgWcWtpSessionWtpSessionUpTime_Type = TimeTicks
_FgWcWtpSessionWtpSessionUpTime_Object = MibTableColumn
fgWcWtpSessionWtpSessionUpTime = _FgWcWtpSessionWtpSessionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 10),
    _FgWcWtpSessionWtpSessionUpTime_Type()
)
fgWcWtpSessionWtpSessionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpSessionUpTime.setStatus("current")
_FgWcWtpSessionWtpProfileName_Type = DisplayString
_FgWcWtpSessionWtpProfileName_Object = MibTableColumn
fgWcWtpSessionWtpProfileName = _FgWcWtpSessionWtpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 11),
    _FgWcWtpSessionWtpProfileName_Type()
)
fgWcWtpSessionWtpProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpProfileName.setStatus("current")
_FgWcWtpSessionWtpModelNumber_Type = DisplayString
_FgWcWtpSessionWtpModelNumber_Object = MibTableColumn
fgWcWtpSessionWtpModelNumber = _FgWcWtpSessionWtpModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 12),
    _FgWcWtpSessionWtpModelNumber_Type()
)
fgWcWtpSessionWtpModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpModelNumber.setStatus("current")
_FgWcWtpSessionWtpHwVersion_Type = DisplayString
_FgWcWtpSessionWtpHwVersion_Object = MibTableColumn
fgWcWtpSessionWtpHwVersion = _FgWcWtpSessionWtpHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 13),
    _FgWcWtpSessionWtpHwVersion_Type()
)
fgWcWtpSessionWtpHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpHwVersion.setStatus("current")
_FgWcWtpSessionWtpSwVersion_Type = DisplayString
_FgWcWtpSessionWtpSwVersion_Object = MibTableColumn
fgWcWtpSessionWtpSwVersion = _FgWcWtpSessionWtpSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 14),
    _FgWcWtpSessionWtpSwVersion_Type()
)
fgWcWtpSessionWtpSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpSwVersion.setStatus("current")
_FgWcWtpSessionWtpBootVersion_Type = DisplayString
_FgWcWtpSessionWtpBootVersion_Object = MibTableColumn
fgWcWtpSessionWtpBootVersion = _FgWcWtpSessionWtpBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 15),
    _FgWcWtpSessionWtpBootVersion_Type()
)
fgWcWtpSessionWtpBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpBootVersion.setStatus("current")
_FgWcWtpSessionWtpRegionCode_Type = DisplayString
_FgWcWtpSessionWtpRegionCode_Object = MibTableColumn
fgWcWtpSessionWtpRegionCode = _FgWcWtpSessionWtpRegionCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 16),
    _FgWcWtpSessionWtpRegionCode_Type()
)
fgWcWtpSessionWtpRegionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpRegionCode.setStatus("current")
_FgWcWtpSessionWtpStationCount_Type = Gauge32
_FgWcWtpSessionWtpStationCount_Object = MibTableColumn
fgWcWtpSessionWtpStationCount = _FgWcWtpSessionWtpStationCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 17),
    _FgWcWtpSessionWtpStationCount_Type()
)
fgWcWtpSessionWtpStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpStationCount.setStatus("current")
_FgWcWtpSessionWtpByteRxCount_Type = Counter64
_FgWcWtpSessionWtpByteRxCount_Object = MibTableColumn
fgWcWtpSessionWtpByteRxCount = _FgWcWtpSessionWtpByteRxCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 18),
    _FgWcWtpSessionWtpByteRxCount_Type()
)
fgWcWtpSessionWtpByteRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpByteRxCount.setStatus("current")
_FgWcWtpSessionWtpByteTxCount_Type = Counter64
_FgWcWtpSessionWtpByteTxCount_Object = MibTableColumn
fgWcWtpSessionWtpByteTxCount = _FgWcWtpSessionWtpByteTxCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 19),
    _FgWcWtpSessionWtpByteTxCount_Type()
)
fgWcWtpSessionWtpByteTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpByteTxCount.setStatus("current")


class _FgWcWtpSessionWtpCpuUsage_Type(Gauge32):
    """Custom type fgWcWtpSessionWtpCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgWcWtpSessionWtpCpuUsage_Type.__name__ = "Gauge32"
_FgWcWtpSessionWtpCpuUsage_Object = MibTableColumn
fgWcWtpSessionWtpCpuUsage = _FgWcWtpSessionWtpCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 20),
    _FgWcWtpSessionWtpCpuUsage_Type()
)
fgWcWtpSessionWtpCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpCpuUsage.setStatus("current")


class _FgWcWtpSessionWtpMemoryUsage_Type(Gauge32):
    """Custom type fgWcWtpSessionWtpMemoryUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgWcWtpSessionWtpMemoryUsage_Type.__name__ = "Gauge32"
_FgWcWtpSessionWtpMemoryUsage_Object = MibTableColumn
fgWcWtpSessionWtpMemoryUsage = _FgWcWtpSessionWtpMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 21),
    _FgWcWtpSessionWtpMemoryUsage_Type()
)
fgWcWtpSessionWtpMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpMemoryUsage.setStatus("current")
_FgWcWtpSessionWtpMemoryCapacity_Type = Unsigned32
_FgWcWtpSessionWtpMemoryCapacity_Object = MibTableColumn
fgWcWtpSessionWtpMemoryCapacity = _FgWcWtpSessionWtpMemoryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 4, 1, 22),
    _FgWcWtpSessionWtpMemoryCapacity_Type()
)
fgWcWtpSessionWtpMemoryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionWtpMemoryCapacity.setStatus("current")
_FgWcWtpSessionRadioTable_Object = MibTable
fgWcWtpSessionRadioTable = _FgWcWtpSessionRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5)
)
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioTable.setStatus("current")
_FgWcWtpSessionRadioEntry_Object = MibTableRow
fgWcWtpSessionRadioEntry = _FgWcWtpSessionRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1)
)
fgWcWtpSessionRadioEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioWtpId"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioRadioId"),
)
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioEntry.setStatus("current")


class _FgWcWtpSessionRadioWtpId_Type(DisplayString):
    """Custom type fgWcWtpSessionRadioWtpId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_FgWcWtpSessionRadioWtpId_Type.__name__ = "DisplayString"
_FgWcWtpSessionRadioWtpId_Object = MibTableColumn
fgWcWtpSessionRadioWtpId = _FgWcWtpSessionRadioWtpId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 1),
    _FgWcWtpSessionRadioWtpId_Type()
)
fgWcWtpSessionRadioWtpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioWtpId.setStatus("current")
_FgWcWtpSessionRadioRadioId_Type = FgWcWtpRadioId
_FgWcWtpSessionRadioRadioId_Object = MibTableColumn
fgWcWtpSessionRadioRadioId = _FgWcWtpSessionRadioRadioId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 2),
    _FgWcWtpSessionRadioRadioId_Type()
)
fgWcWtpSessionRadioRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioRadioId.setStatus("current")
_FgWcWtpSessionRadioMode_Type = FgWcWtpRadioMode
_FgWcWtpSessionRadioMode_Object = MibTableColumn
fgWcWtpSessionRadioMode = _FgWcWtpSessionRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 3),
    _FgWcWtpSessionRadioMode_Type()
)
fgWcWtpSessionRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioMode.setStatus("current")


class _FgWcWtpSessionRadioBaseBssid_Type(PhysAddress):
    """Custom type fgWcWtpSessionRadioBaseBssid based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_FgWcWtpSessionRadioBaseBssid_Type.__name__ = "PhysAddress"
_FgWcWtpSessionRadioBaseBssid_Object = MibTableColumn
fgWcWtpSessionRadioBaseBssid = _FgWcWtpSessionRadioBaseBssid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 4),
    _FgWcWtpSessionRadioBaseBssid_Type()
)
fgWcWtpSessionRadioBaseBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioBaseBssid.setStatus("current")
_FgWcWtpSessionRadioCountryString_Type = FgWcCountryString
_FgWcWtpSessionRadioCountryString_Object = MibTableColumn
fgWcWtpSessionRadioCountryString = _FgWcWtpSessionRadioCountryString_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 5),
    _FgWcWtpSessionRadioCountryString_Type()
)
fgWcWtpSessionRadioCountryString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioCountryString.setStatus("current")
_FgWcWtpSessionRadioCountryCode_Type = Integer32
_FgWcWtpSessionRadioCountryCode_Object = MibTableColumn
fgWcWtpSessionRadioCountryCode = _FgWcWtpSessionRadioCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 6),
    _FgWcWtpSessionRadioCountryCode_Type()
)
fgWcWtpSessionRadioCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioCountryCode.setStatus("current")
_FgWcWtpSessionRadioOperatingChannel_Type = FgWcWtpRadioChannelNumber
_FgWcWtpSessionRadioOperatingChannel_Object = MibTableColumn
fgWcWtpSessionRadioOperatingChannel = _FgWcWtpSessionRadioOperatingChannel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 7),
    _FgWcWtpSessionRadioOperatingChannel_Type()
)
fgWcWtpSessionRadioOperatingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioOperatingChannel.setStatus("current")
_FgWcWtpSessionRadioOperatingPower_Type = Integer32
_FgWcWtpSessionRadioOperatingPower_Object = MibTableColumn
fgWcWtpSessionRadioOperatingPower = _FgWcWtpSessionRadioOperatingPower_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 8),
    _FgWcWtpSessionRadioOperatingPower_Type()
)
fgWcWtpSessionRadioOperatingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioOperatingPower.setStatus("current")
_FgWcWtpSessionRadioStationCount_Type = Gauge32
_FgWcWtpSessionRadioStationCount_Object = MibTableColumn
fgWcWtpSessionRadioStationCount = _FgWcWtpSessionRadioStationCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 5, 1, 9),
    _FgWcWtpSessionRadioStationCount_Type()
)
fgWcWtpSessionRadioStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionRadioStationCount.setStatus("current")
_FgWcWtpSessionVapTable_Object = MibTable
fgWcWtpSessionVapTable = _FgWcWtpSessionVapTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6)
)
if mibBuilder.loadTexts:
    fgWcWtpSessionVapTable.setStatus("current")
_FgWcWtpSessionVapEntry_Object = MibTableRow
fgWcWtpSessionVapEntry = _FgWcWtpSessionVapEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6, 1)
)
fgWcWtpSessionVapEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpSessionVapWtpId"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcWtpSessionVapRadioId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fgWcWtpSessionVapEntry.setStatus("current")


class _FgWcWtpSessionVapWtpId_Type(DisplayString):
    """Custom type fgWcWtpSessionVapWtpId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_FgWcWtpSessionVapWtpId_Type.__name__ = "DisplayString"
_FgWcWtpSessionVapWtpId_Object = MibTableColumn
fgWcWtpSessionVapWtpId = _FgWcWtpSessionVapWtpId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6, 1, 1),
    _FgWcWtpSessionVapWtpId_Type()
)
fgWcWtpSessionVapWtpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpSessionVapWtpId.setStatus("current")
_FgWcWtpSessionVapRadioId_Type = FgWcWtpRadioId
_FgWcWtpSessionVapRadioId_Object = MibTableColumn
fgWcWtpSessionVapRadioId = _FgWcWtpSessionVapRadioId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6, 1, 2),
    _FgWcWtpSessionVapRadioId_Type()
)
fgWcWtpSessionVapRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcWtpSessionVapRadioId.setStatus("current")


class _FgWcWtpSessionVapSsid_Type(OctetString):
    """Custom type fgWcWtpSessionVapSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgWcWtpSessionVapSsid_Type.__name__ = "OctetString"
_FgWcWtpSessionVapSsid_Object = MibTableColumn
fgWcWtpSessionVapSsid = _FgWcWtpSessionVapSsid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6, 1, 3),
    _FgWcWtpSessionVapSsid_Type()
)
fgWcWtpSessionVapSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionVapSsid.setStatus("current")
_FgWcWtpSessionVapStationCount_Type = Gauge32
_FgWcWtpSessionVapStationCount_Object = MibTableColumn
fgWcWtpSessionVapStationCount = _FgWcWtpSessionVapStationCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6, 1, 4),
    _FgWcWtpSessionVapStationCount_Type()
)
fgWcWtpSessionVapStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionVapStationCount.setStatus("current")
_FgWcWtpSessionVapByteRxCount_Type = Counter64
_FgWcWtpSessionVapByteRxCount_Object = MibTableColumn
fgWcWtpSessionVapByteRxCount = _FgWcWtpSessionVapByteRxCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6, 1, 5),
    _FgWcWtpSessionVapByteRxCount_Type()
)
fgWcWtpSessionVapByteRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionVapByteRxCount.setStatus("current")
_FgWcWtpSessionVapByteTxCount_Type = Counter64
_FgWcWtpSessionVapByteTxCount_Object = MibTableColumn
fgWcWtpSessionVapByteTxCount = _FgWcWtpSessionVapByteTxCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 4, 6, 1, 6),
    _FgWcWtpSessionVapByteTxCount_Type()
)
fgWcWtpSessionVapByteTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcWtpSessionVapByteTxCount.setStatus("current")
_FgWcStaTable_Object = MibTable
fgWcStaTable = _FgWcStaTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5)
)
if mibBuilder.loadTexts:
    fgWcStaTable.setStatus("current")
_FgWcStaEntry_Object = MibTableRow
fgWcStaEntry = _FgWcStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1)
)
fgWcStaEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "IF-MIB", "ifIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgWcStaMacAddress"),
)
if mibBuilder.loadTexts:
    fgWcStaEntry.setStatus("current")


class _FgWcStaMacAddress_Type(PhysAddress):
    """Custom type fgWcStaMacAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_FgWcStaMacAddress_Type.__name__ = "PhysAddress"
_FgWcStaMacAddress_Object = MibTableColumn
fgWcStaMacAddress = _FgWcStaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 1),
    _FgWcStaMacAddress_Type()
)
fgWcStaMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgWcStaMacAddress.setStatus("current")
_FgWcStaWlan_Type = DisplayString
_FgWcStaWlan_Object = MibTableColumn
fgWcStaWlan = _FgWcStaWlan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 2),
    _FgWcStaWlan_Type()
)
fgWcStaWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaWlan.setStatus("current")
_FgWcStaWtpId_Type = DisplayString
_FgWcStaWtpId_Object = MibTableColumn
fgWcStaWtpId = _FgWcStaWtpId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 3),
    _FgWcStaWtpId_Type()
)
fgWcStaWtpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaWtpId.setStatus("current")
_FgWcStaRadioId_Type = FgWcWtpRadioId
_FgWcStaRadioId_Object = MibTableColumn
fgWcStaRadioId = _FgWcStaRadioId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 4),
    _FgWcStaRadioId_Type()
)
fgWcStaRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaRadioId.setStatus("current")


class _FgWcStaVlanId_Type(Integer32):
    """Custom type fgWcStaVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_FgWcStaVlanId_Type.__name__ = "Integer32"
_FgWcStaVlanId_Object = MibTableColumn
fgWcStaVlanId = _FgWcStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 5),
    _FgWcStaVlanId_Type()
)
fgWcStaVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaVlanId.setStatus("current")
_FgWcStaIpAddressType_Type = InetAddressType
_FgWcStaIpAddressType_Object = MibTableColumn
fgWcStaIpAddressType = _FgWcStaIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 6),
    _FgWcStaIpAddressType_Type()
)
fgWcStaIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaIpAddressType.setStatus("current")
_FgWcStaIpAddress_Type = InetAddress
_FgWcStaIpAddress_Object = MibTableColumn
fgWcStaIpAddress = _FgWcStaIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 7),
    _FgWcStaIpAddress_Type()
)
fgWcStaIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaIpAddress.setStatus("current")
_FgWcStaVci_Type = DisplayString
_FgWcStaVci_Object = MibTableColumn
fgWcStaVci = _FgWcStaVci_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 8),
    _FgWcStaVci_Type()
)
fgWcStaVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaVci.setStatus("current")
_FgWcStaHost_Type = DisplayString
_FgWcStaHost_Object = MibTableColumn
fgWcStaHost = _FgWcStaHost_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 9),
    _FgWcStaHost_Type()
)
fgWcStaHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaHost.setStatus("current")
_FgWcStaUser_Type = DisplayString
_FgWcStaUser_Object = MibTableColumn
fgWcStaUser = _FgWcStaUser_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 10),
    _FgWcStaUser_Type()
)
fgWcStaUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaUser.setStatus("current")
_FgWcStaGroup_Type = DisplayString
_FgWcStaGroup_Object = MibTableColumn
fgWcStaGroup = _FgWcStaGroup_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 11),
    _FgWcStaGroup_Type()
)
fgWcStaGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaGroup.setStatus("current")
_FgWcStaSignal_Type = Integer32
_FgWcStaSignal_Object = MibTableColumn
fgWcStaSignal = _FgWcStaSignal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 12),
    _FgWcStaSignal_Type()
)
fgWcStaSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaSignal.setStatus("current")
_FgWcStaNoise_Type = Integer32
_FgWcStaNoise_Object = MibTableColumn
fgWcStaNoise = _FgWcStaNoise_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 13),
    _FgWcStaNoise_Type()
)
fgWcStaNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaNoise.setStatus("current")
_FgWcStaIdle_Type = Gauge32
_FgWcStaIdle_Object = MibTableColumn
fgWcStaIdle = _FgWcStaIdle_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 14),
    _FgWcStaIdle_Type()
)
fgWcStaIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaIdle.setStatus("current")
_FgWcStaBandwidthTx_Type = Gauge32
_FgWcStaBandwidthTx_Object = MibTableColumn
fgWcStaBandwidthTx = _FgWcStaBandwidthTx_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 15),
    _FgWcStaBandwidthTx_Type()
)
fgWcStaBandwidthTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaBandwidthTx.setStatus("current")
_FgWcStaBandwidthRx_Type = Gauge32
_FgWcStaBandwidthRx_Object = MibTableColumn
fgWcStaBandwidthRx = _FgWcStaBandwidthRx_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 16),
    _FgWcStaBandwidthRx_Type()
)
fgWcStaBandwidthRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaBandwidthRx.setStatus("current")
_FgWcStaChannel_Type = FgWcWtpRadioChannelNumber
_FgWcStaChannel_Object = MibTableColumn
fgWcStaChannel = _FgWcStaChannel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 17),
    _FgWcStaChannel_Type()
)
fgWcStaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaChannel.setStatus("current")
_FgWcStaRadioType_Type = FgWcWtpRadioType
_FgWcStaRadioType_Object = MibTableColumn
fgWcStaRadioType = _FgWcStaRadioType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 18),
    _FgWcStaRadioType_Type()
)
fgWcStaRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaRadioType.setStatus("current")
_FgWcStaSecurity_Type = FgWcWlanSecurityType
_FgWcStaSecurity_Object = MibTableColumn
fgWcStaSecurity = _FgWcStaSecurity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 19),
    _FgWcStaSecurity_Type()
)
fgWcStaSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaSecurity.setStatus("current")
_FgWcStaEncrypt_Type = FgWcWlanEncryptionType
_FgWcStaEncrypt_Object = MibTableColumn
fgWcStaEncrypt = _FgWcStaEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 20),
    _FgWcStaEncrypt_Type()
)
fgWcStaEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaEncrypt.setStatus("current")


class _FgWcStaOnline_Type(Integer32):
    """Custom type fgWcStaOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_FgWcStaOnline_Type.__name__ = "Integer32"
_FgWcStaOnline_Object = MibTableColumn
fgWcStaOnline = _FgWcStaOnline_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 21),
    _FgWcStaOnline_Type()
)
fgWcStaOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaOnline.setStatus("current")
_FgWcStaCPAuth_Type = FnBoolState
_FgWcStaCPAuth_Object = MibTableColumn
fgWcStaCPAuth = _FgWcStaCPAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 14, 5, 1, 22),
    _FgWcStaCPAuth_Type()
)
fgWcStaCPAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcStaCPAuth.setStatus("current")
_FgFc_ObjectIdentity = ObjectIdentity
fgFc = _FgFc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 15)
)
_FgFcTrapObjects_ObjectIdentity = ObjectIdentity
fgFcTrapObjects = _FgFcTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 15, 1)
)
_FgFcSwVdom_Type = FgVdIndex
_FgFcSwVdom_Object = MibScalar
fgFcSwVdom = _FgFcSwVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 15, 1, 1),
    _FgFcSwVdom_Type()
)
fgFcSwVdom.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgFcSwVdom.setStatus("current")


class _FgFcSwSerial_Type(DisplayString):
    """Custom type fgFcSwSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgFcSwSerial_Type.__name__ = "DisplayString"
_FgFcSwSerial_Object = MibScalar
fgFcSwSerial = _FgFcSwSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 15, 1, 2),
    _FgFcSwSerial_Type()
)
fgFcSwSerial.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgFcSwSerial.setStatus("current")


class _FgFcSwName_Type(DisplayString):
    """Custom type fgFcSwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgFcSwName_Type.__name__ = "DisplayString"
_FgFcSwName_Object = MibScalar
fgFcSwName = _FgFcSwName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 15, 1, 3),
    _FgFcSwName_Type()
)
fgFcSwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgFcSwName.setStatus("current")
_FgServerLoadBalance_ObjectIdentity = ObjectIdentity
fgServerLoadBalance = _FgServerLoadBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 16)
)
_FgServerLoadBalanceTrapObjects_ObjectIdentity = ObjectIdentity
fgServerLoadBalanceTrapObjects = _FgServerLoadBalanceTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 16, 1)
)
_FgServerLoadBalanceRealServerAddress_Type = IpAddress
_FgServerLoadBalanceRealServerAddress_Object = MibScalar
fgServerLoadBalanceRealServerAddress = _FgServerLoadBalanceRealServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 16, 1, 1),
    _FgServerLoadBalanceRealServerAddress_Type()
)
fgServerLoadBalanceRealServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgServerLoadBalanceRealServerAddress.setStatus("current")


class _FgServerLoadBalanceVirtualServerName_Type(DisplayString):
    """Custom type fgServerLoadBalanceVirtualServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgServerLoadBalanceVirtualServerName_Type.__name__ = "DisplayString"
_FgServerLoadBalanceVirtualServerName_Object = MibScalar
fgServerLoadBalanceVirtualServerName = _FgServerLoadBalanceVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 16, 1, 2),
    _FgServerLoadBalanceVirtualServerName_Type()
)
fgServerLoadBalanceVirtualServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgServerLoadBalanceVirtualServerName.setStatus("current")
_FgServerLoadBalanceRealServerAddress6_Type = Ipv6Address
_FgServerLoadBalanceRealServerAddress6_Object = MibScalar
fgServerLoadBalanceRealServerAddress6 = _FgServerLoadBalanceRealServerAddress6_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 16, 1, 3),
    _FgServerLoadBalanceRealServerAddress6_Type()
)
fgServerLoadBalanceRealServerAddress6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgServerLoadBalanceRealServerAddress6.setStatus("current")
_FgUsbModemInfo_ObjectIdentity = ObjectIdentity
fgUsbModemInfo = _FgUsbModemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17)
)
_FgUsbModemInfoObjects_ObjectIdentity = ObjectIdentity
fgUsbModemInfoObjects = _FgUsbModemInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1)
)


class _FgUsbModemSignalStrength_Type(Integer32):
    """Custom type fgUsbModemSignalStrength based on Integer32"""
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
        *(("level0", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3),
          ("level4", 4))
    )


_FgUsbModemSignalStrength_Type.__name__ = "Integer32"
_FgUsbModemSignalStrength_Object = MibScalar
fgUsbModemSignalStrength = _FgUsbModemSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 1),
    _FgUsbModemSignalStrength_Type()
)
fgUsbModemSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemSignalStrength.setStatus("current")


class _FgUsbModemStatus_Type(Integer32):
    """Custom type fgUsbModemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connected", 1))
    )


_FgUsbModemStatus_Type.__name__ = "Integer32"
_FgUsbModemStatus_Object = MibScalar
fgUsbModemStatus = _FgUsbModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 2),
    _FgUsbModemStatus_Type()
)
fgUsbModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemStatus.setStatus("current")


class _FgUsbModemSimState_Type(Integer32):
    """Custom type fgUsbModemSimState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_FgUsbModemSimState_Type.__name__ = "Integer32"
_FgUsbModemSimState_Object = MibScalar
fgUsbModemSimState = _FgUsbModemSimState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 3),
    _FgUsbModemSimState_Type()
)
fgUsbModemSimState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemSimState.setStatus("current")


class _FgUsbModemVendor_Type(DisplayString):
    """Custom type fgUsbModemVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgUsbModemVendor_Type.__name__ = "DisplayString"
_FgUsbModemVendor_Object = MibScalar
fgUsbModemVendor = _FgUsbModemVendor_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 4),
    _FgUsbModemVendor_Type()
)
fgUsbModemVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemVendor.setStatus("current")


class _FgUsbModemProduct_Type(DisplayString):
    """Custom type fgUsbModemProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgUsbModemProduct_Type.__name__ = "DisplayString"
_FgUsbModemProduct_Object = MibScalar
fgUsbModemProduct = _FgUsbModemProduct_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 5),
    _FgUsbModemProduct_Type()
)
fgUsbModemProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemProduct.setStatus("current")


class _FgUsbModemNetwork_Type(Integer32):
    """Custom type fgUsbModemNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("network3G", 0),
          ("networkLTE", 1))
    )


_FgUsbModemNetwork_Type.__name__ = "Integer32"
_FgUsbModemNetwork_Object = MibScalar
fgUsbModemNetwork = _FgUsbModemNetwork_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 6),
    _FgUsbModemNetwork_Type()
)
fgUsbModemNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemNetwork.setStatus("current")


class _FgUsbModemId_Type(DisplayString):
    """Custom type fgUsbModemId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgUsbModemId_Type.__name__ = "DisplayString"
_FgUsbModemId_Object = MibScalar
fgUsbModemId = _FgUsbModemId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 7),
    _FgUsbModemId_Type()
)
fgUsbModemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemId.setStatus("current")


class _FgUsbModemSimId_Type(DisplayString):
    """Custom type fgUsbModemSimId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgUsbModemSimId_Type.__name__ = "DisplayString"
_FgUsbModemSimId_Object = MibScalar
fgUsbModemSimId = _FgUsbModemSimId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 17, 1, 8),
    _FgUsbModemSimId_Type()
)
fgUsbModemSimId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUsbModemSimId.setStatus("current")
_FgDevice_ObjectIdentity = ObjectIdentity
fgDevice = _FgDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 18)
)
_FgDeviceTrapObjects_ObjectIdentity = ObjectIdentity
fgDeviceTrapObjects = _FgDeviceTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 18, 1)
)


class _FgDeviceMacAddress_Type(DisplayString):
    """Custom type fgDeviceMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgDeviceMacAddress_Type.__name__ = "DisplayString"
_FgDeviceMacAddress_Object = MibScalar
fgDeviceMacAddress = _FgDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 18, 1, 1),
    _FgDeviceMacAddress_Type()
)
fgDeviceMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgDeviceMacAddress.setStatus("current")
_FgDeviceCreated_Type = Gauge32
_FgDeviceCreated_Object = MibScalar
fgDeviceCreated = _FgDeviceCreated_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 18, 1, 2),
    _FgDeviceCreated_Type()
)
fgDeviceCreated.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgDeviceCreated.setStatus("current")
_FgDeviceLastSeen_Type = Gauge32
_FgDeviceLastSeen_Object = MibScalar
fgDeviceLastSeen = _FgDeviceLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 18, 1, 3),
    _FgDeviceLastSeen_Type()
)
fgDeviceLastSeen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgDeviceLastSeen.setStatus("current")
_FgInternalLTEModemsInfo_ObjectIdentity = ObjectIdentity
fgInternalLTEModemsInfo = _FgInternalLTEModemsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19)
)
_FgMdmInfoTable_Object = MibTable
fgMdmInfoTable = _FgMdmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1)
)
if mibBuilder.loadTexts:
    fgMdmInfoTable.setStatus("current")
_FgMdmInfoEntry_Object = MibTableRow
fgMdmInfoEntry = _FgMdmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1)
)
fgMdmInfoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgMdmEntIndex"),
)
if mibBuilder.loadTexts:
    fgMdmInfoEntry.setStatus("current")
_FgMdmEntIndex_Type = FnIndex
_FgMdmEntIndex_Object = MibTableColumn
fgMdmEntIndex = _FgMdmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 1),
    _FgMdmEntIndex_Type()
)
fgMdmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgMdmEntIndex.setStatus("current")


class _FgMdmDetected_Type(Integer32):
    """Custom type fgMdmDetected based on Integer32"""
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


_FgMdmDetected_Type.__name__ = "Integer32"
_FgMdmDetected_Object = MibTableColumn
fgMdmDetected = _FgMdmDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 2),
    _FgMdmDetected_Type()
)
fgMdmDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmDetected.setStatus("current")


class _FgMdmVendor_Type(DisplayString):
    """Custom type fgMdmVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgMdmVendor_Type.__name__ = "DisplayString"
_FgMdmVendor_Object = MibTableColumn
fgMdmVendor = _FgMdmVendor_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 3),
    _FgMdmVendor_Type()
)
fgMdmVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmVendor.setStatus("current")


class _FgMdmModel_Type(DisplayString):
    """Custom type fgMdmModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgMdmModel_Type.__name__ = "DisplayString"
_FgMdmModel_Object = MibTableColumn
fgMdmModel = _FgMdmModel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 4),
    _FgMdmModel_Type()
)
fgMdmModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmModel.setStatus("current")


class _FgMdmRevision_Type(DisplayString):
    """Custom type fgMdmRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgMdmRevision_Type.__name__ = "DisplayString"
_FgMdmRevision_Object = MibTableColumn
fgMdmRevision = _FgMdmRevision_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 5),
    _FgMdmRevision_Type()
)
fgMdmRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmRevision.setStatus("current")


class _FgMdmMsisdn_Type(DisplayString):
    """Custom type fgMdmMsisdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgMdmMsisdn_Type.__name__ = "DisplayString"
_FgMdmMsisdn_Object = MibTableColumn
fgMdmMsisdn = _FgMdmMsisdn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 6),
    _FgMdmMsisdn_Type()
)
fgMdmMsisdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmMsisdn.setStatus("current")


class _FgMdmEsn_Type(DisplayString):
    """Custom type fgMdmEsn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FgMdmEsn_Type.__name__ = "DisplayString"
_FgMdmEsn_Object = MibTableColumn
fgMdmEsn = _FgMdmEsn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 7),
    _FgMdmEsn_Type()
)
fgMdmEsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmEsn.setStatus("current")


class _FgMdmImei_Type(DisplayString):
    """Custom type fgMdmImei based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgMdmImei_Type.__name__ = "DisplayString"
_FgMdmImei_Object = MibTableColumn
fgMdmImei = _FgMdmImei_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 8),
    _FgMdmImei_Type()
)
fgMdmImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmImei.setStatus("current")


class _FgMdmHwRevision_Type(DisplayString):
    """Custom type fgMdmHwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_FgMdmHwRevision_Type.__name__ = "DisplayString"
_FgMdmHwRevision_Object = MibTableColumn
fgMdmHwRevision = _FgMdmHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 9),
    _FgMdmHwRevision_Type()
)
fgMdmHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmHwRevision.setStatus("current")


class _FgMdmMeid_Type(DisplayString):
    """Custom type fgMdmMeid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgMdmMeid_Type.__name__ = "DisplayString"
_FgMdmMeid_Object = MibTableColumn
fgMdmMeid = _FgMdmMeid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 10),
    _FgMdmMeid_Type()
)
fgMdmMeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmMeid.setStatus("current")


class _FgMdmSwRev_Type(DisplayString):
    """Custom type fgMdmSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgMdmSwRev_Type.__name__ = "DisplayString"
_FgMdmSwRev_Object = MibTableColumn
fgMdmSwRev = _FgMdmSwRev_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 11),
    _FgMdmSwRev_Type()
)
fgMdmSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmSwRev.setStatus("current")


class _FgMdmSku_Type(DisplayString):
    """Custom type fgMdmSku based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgMdmSku_Type.__name__ = "DisplayString"
_FgMdmSku_Object = MibTableColumn
fgMdmSku = _FgMdmSku_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 12),
    _FgMdmSku_Type()
)
fgMdmSku.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmSku.setStatus("current")


class _FgMdmFsn_Type(DisplayString):
    """Custom type fgMdmFsn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgMdmFsn_Type.__name__ = "DisplayString"
_FgMdmFsn_Object = MibTableColumn
fgMdmFsn = _FgMdmFsn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 13),
    _FgMdmFsn_Type()
)
fgMdmFsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmFsn.setStatus("current")


class _FgMdmPrlVer_Type(DisplayString):
    """Custom type fgMdmPrlVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_FgMdmPrlVer_Type.__name__ = "DisplayString"
_FgMdmPrlVer_Object = MibTableColumn
fgMdmPrlVer = _FgMdmPrlVer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 14),
    _FgMdmPrlVer_Type()
)
fgMdmPrlVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmPrlVer.setStatus("current")


class _FgMdmFwVer_Type(DisplayString):
    """Custom type fgMdmFwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FgMdmFwVer_Type.__name__ = "DisplayString"
_FgMdmFwVer_Object = MibTableColumn
fgMdmFwVer = _FgMdmFwVer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 15),
    _FgMdmFwVer_Type()
)
fgMdmFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmFwVer.setStatus("current")


class _FgMdmPriFwVer_Type(DisplayString):
    """Custom type fgMdmPriFwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FgMdmPriFwVer_Type.__name__ = "DisplayString"
_FgMdmPriFwVer_Object = MibTableColumn
fgMdmPriFwVer = _FgMdmPriFwVer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 16),
    _FgMdmPriFwVer_Type()
)
fgMdmPriFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmPriFwVer.setStatus("current")


class _FgMdmCarrierAbbr_Type(DisplayString):
    """Custom type fgMdmCarrierAbbr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FgMdmCarrierAbbr_Type.__name__ = "DisplayString"
_FgMdmCarrierAbbr_Object = MibTableColumn
fgMdmCarrierAbbr = _FgMdmCarrierAbbr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 17),
    _FgMdmCarrierAbbr_Type()
)
fgMdmCarrierAbbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmCarrierAbbr.setStatus("current")


class _FgMdmActState_Type(Integer32):
    """Custom type fgMdmActState based on Integer32"""
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
        *(("notActivated", 0),
          ("activated", 1),
          ("connecting", 2),
          ("connected", 3),
          ("otaspAuthenticated", 4),
          ("otaspNamDownloaded", 5),
          ("otaspMdnDownloaded", 6),
          ("otaspImsiDownloaded", 7),
          ("otaspPrlDownloaded", 8),
          ("otaspSpcDownloaded", 9),
          ("otaspSettingsCmted", 10))
    )


_FgMdmActState_Type.__name__ = "Integer32"
_FgMdmActState_Object = MibTableColumn
fgMdmActState = _FgMdmActState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 18),
    _FgMdmActState_Type()
)
fgMdmActState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmActState.setStatus("current")


class _FgMdmOpMode_Type(Integer32):
    """Custom type fgMdmOpMode based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("online", 0),
          ("lowPower", 1),
          ("factoryTest", 2),
          ("offLine", 3),
          ("reset", 4),
          ("shuttingDown", 5),
          ("persistentLowPower", 6),
          ("modeOnlyLowPower", 7),
          ("unknown", 255))
    )


_FgMdmOpMode_Type.__name__ = "Integer32"
_FgMdmOpMode_Object = MibTableColumn
fgMdmOpMode = _FgMdmOpMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 19),
    _FgMdmOpMode_Type()
)
fgMdmOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmOpMode.setStatus("current")


class _FgMdmLacTac_Type(DisplayString):
    """Custom type fgMdmLacTac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FgMdmLacTac_Type.__name__ = "DisplayString"
_FgMdmLacTac_Object = MibTableColumn
fgMdmLacTac = _FgMdmLacTac_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 20),
    _FgMdmLacTac_Type()
)
fgMdmLacTac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmLacTac.setStatus("current")


class _FgMdmActBand_Type(DisplayString):
    """Custom type fgMdmActBand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FgMdmActBand_Type.__name__ = "DisplayString"
_FgMdmActBand_Object = MibTableColumn
fgMdmActBand = _FgMdmActBand_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 21),
    _FgMdmActBand_Type()
)
fgMdmActBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmActBand.setStatus("current")


class _FgMdmCellId_Type(DisplayString):
    """Custom type fgMdmCellId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FgMdmCellId_Type.__name__ = "DisplayString"
_FgMdmCellId_Object = MibTableColumn
fgMdmCellId = _FgMdmCellId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 22),
    _FgMdmCellId_Type()
)
fgMdmCellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmCellId.setStatus("current")


class _FgMdmRssi_Type(Integer32):
    """Custom type fgMdmRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_FgMdmRssi_Type.__name__ = "Integer32"
_FgMdmRssi_Object = MibTableColumn
fgMdmRssi = _FgMdmRssi_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 1, 1, 23),
    _FgMdmRssi_Type()
)
fgMdmRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgMdmRssi.setStatus("current")
_FgSimInfoTable_Object = MibTable
fgSimInfoTable = _FgSimInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 2)
)
if mibBuilder.loadTexts:
    fgSimInfoTable.setStatus("current")
_FgSimInfoEntry_Object = MibTableRow
fgSimInfoEntry = _FgSimInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 2, 1)
)
fgSimInfoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgSimEntIndex"),
)
if mibBuilder.loadTexts:
    fgSimInfoEntry.setStatus("current")
_FgSimEntIndex_Type = FnIndex
_FgSimEntIndex_Object = MibTableColumn
fgSimEntIndex = _FgSimEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 2, 1, 1),
    _FgSimEntIndex_Type()
)
fgSimEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgSimEntIndex.setStatus("current")
_FgSimMdmEntIndex_Type = FnIndex
_FgSimMdmEntIndex_Object = MibTableColumn
fgSimMdmEntIndex = _FgSimMdmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 2, 1, 2),
    _FgSimMdmEntIndex_Type()
)
fgSimMdmEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSimMdmEntIndex.setStatus("current")


class _FgSimState_Type(Integer32):
    """Custom type fgSimState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("initialized", 0),
          ("lockedOrFailed", 1),
          ("notPresent", 2),
          ("reserved", 3),
          ("unknown", 255))
    )


_FgSimState_Type.__name__ = "Integer32"
_FgSimState_Object = MibTableColumn
fgSimState = _FgSimState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 2, 1, 3),
    _FgSimState_Type()
)
fgSimState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSimState.setStatus("current")


class _FgSimIccid_Type(DisplayString):
    """Custom type fgSimIccid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgSimIccid_Type.__name__ = "DisplayString"
_FgSimIccid_Object = MibTableColumn
fgSimIccid = _FgSimIccid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 2, 1, 4),
    _FgSimIccid_Type()
)
fgSimIccid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSimIccid.setStatus("current")


class _FgSimImsi_Type(DisplayString):
    """Custom type fgSimImsi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FgSimImsi_Type.__name__ = "DisplayString"
_FgSimImsi_Object = MibTableColumn
fgSimImsi = _FgSimImsi_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 2, 1, 5),
    _FgSimImsi_Type()
)
fgSimImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSimImsi.setStatus("current")


class _FgSimCountry_Type(DisplayString):
    """Custom type fgSimCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_FgSimCountry_Type.__name__ = "DisplayString"
_FgSimCountry_Object = MibTableColumn
fgSimCountry = _FgSimCountry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 2, 1, 6),
    _FgSimCountry_Type()
)
fgSimCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSimCountry.setStatus("current")


class _FgSimNetwork_Type(DisplayString):
    """Custom type fgSimNetwork based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FgSimNetwork_Type.__name__ = "DisplayString"
_FgSimNetwork_Object = MibTableColumn
fgSimNetwork = _FgSimNetwork_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 2, 1, 7),
    _FgSimNetwork_Type()
)
fgSimNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSimNetwork.setStatus("current")
_FgSignalInfoTable_Object = MibTable
fgSignalInfoTable = _FgSignalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3)
)
if mibBuilder.loadTexts:
    fgSignalInfoTable.setStatus("current")
_FgSignalInfoEntry_Object = MibTableRow
fgSignalInfoEntry = _FgSignalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1)
)
fgSignalInfoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgSigMdmEntIndex"),
)
if mibBuilder.loadTexts:
    fgSignalInfoEntry.setStatus("current")
_FgSigMdmEntIndex_Type = FnIndex
_FgSigMdmEntIndex_Object = MibTableColumn
fgSigMdmEntIndex = _FgSigMdmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1, 1),
    _FgSigMdmEntIndex_Type()
)
fgSigMdmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgSigMdmEntIndex.setStatus("current")


class _FgCdmaRssi_Type(Integer32):
    """Custom type fgCdmaRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_FgCdmaRssi_Type.__name__ = "Integer32"
_FgCdmaRssi_Object = MibTableColumn
fgCdmaRssi = _FgCdmaRssi_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1, 2),
    _FgCdmaRssi_Type()
)
fgCdmaRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgCdmaRssi.setStatus("current")


class _FgCdmaEcio_Type(Integer32):
    """Custom type fgCdmaEcio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65536, 65535),
    )


_FgCdmaEcio_Type.__name__ = "Integer32"
_FgCdmaEcio_Object = MibTableColumn
fgCdmaEcio = _FgCdmaEcio_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1, 3),
    _FgCdmaEcio_Type()
)
fgCdmaEcio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgCdmaEcio.setStatus("current")


class _FgHdrRssi_Type(Integer32):
    """Custom type fgHdrRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_FgHdrRssi_Type.__name__ = "Integer32"
_FgHdrRssi_Object = MibTableColumn
fgHdrRssi = _FgHdrRssi_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1, 4),
    _FgHdrRssi_Type()
)
fgHdrRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHdrRssi.setStatus("current")


class _FgHdrEcio_Type(Integer32):
    """Custom type fgHdrEcio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65536, 65535),
    )


_FgHdrEcio_Type.__name__ = "Integer32"
_FgHdrEcio_Object = MibTableColumn
fgHdrEcio = _FgHdrEcio_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1, 5),
    _FgHdrEcio_Type()
)
fgHdrEcio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHdrEcio.setStatus("current")


class _FgHdrSinr_Type(Integer32):
    """Custom type fgHdrSinr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_FgHdrSinr_Type.__name__ = "Integer32"
_FgHdrSinr_Object = MibTableColumn
fgHdrSinr = _FgHdrSinr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1, 6),
    _FgHdrSinr_Type()
)
fgHdrSinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHdrSinr.setStatus("current")
_FgHdrIo_Type = Integer32
_FgHdrIo_Object = MibTableColumn
fgHdrIo = _FgHdrIo_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1, 7),
    _FgHdrIo_Type()
)
fgHdrIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgHdrIo.setStatus("current")


class _FgGsm_Type(Integer32):
    """Custom type fgGsm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_FgGsm_Type.__name__ = "Integer32"
_FgGsm_Object = MibTableColumn
fgGsm = _FgGsm_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1, 8),
    _FgGsm_Type()
)
fgGsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgGsm.setStatus("current")


class _FgWcdmaRssi_Type(Integer32):
    """Custom type fgWcdmaRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_FgWcdmaRssi_Type.__name__ = "Integer32"
_FgWcdmaRssi_Object = MibTableColumn
fgWcdmaRssi = _FgWcdmaRssi_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1, 9),
    _FgWcdmaRssi_Type()
)
fgWcdmaRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcdmaRssi.setStatus("current")


class _FgWcdmaEcio_Type(Integer32):
    """Custom type fgWcdmaEcio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65536, 65535),
    )


_FgWcdmaEcio_Type.__name__ = "Integer32"
_FgWcdmaEcio_Object = MibTableColumn
fgWcdmaEcio = _FgWcdmaEcio_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1, 10),
    _FgWcdmaEcio_Type()
)
fgWcdmaEcio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgWcdmaEcio.setStatus("current")


class _FgLteRssi_Type(Integer32):
    """Custom type fgLteRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_FgLteRssi_Type.__name__ = "Integer32"
_FgLteRssi_Object = MibTableColumn
fgLteRssi = _FgLteRssi_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1, 11),
    _FgLteRssi_Type()
)
fgLteRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLteRssi.setStatus("current")


class _FgLteRsrq_Type(Integer32):
    """Custom type fgLteRsrq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_FgLteRsrq_Type.__name__ = "Integer32"
_FgLteRsrq_Object = MibTableColumn
fgLteRsrq = _FgLteRsrq_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1, 12),
    _FgLteRsrq_Type()
)
fgLteRsrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLteRsrq.setStatus("current")


class _FgLteRsrp_Type(Integer32):
    """Custom type fgLteRsrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65536, 65535),
    )


_FgLteRsrp_Type.__name__ = "Integer32"
_FgLteRsrp_Object = MibTableColumn
fgLteRsrp = _FgLteRsrp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1, 13),
    _FgLteRsrp_Type()
)
fgLteRsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLteRsrp.setStatus("current")


class _FgLteSnr_Type(Integer32):
    """Custom type fgLteSnr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65536, 65535),
    )


_FgLteSnr_Type.__name__ = "Integer32"
_FgLteSnr_Object = MibTableColumn
fgLteSnr = _FgLteSnr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1, 14),
    _FgLteSnr_Type()
)
fgLteSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLteSnr.setStatus("current")


class _FgTdma_Type(Integer32):
    """Custom type fgTdma based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_FgTdma_Type.__name__ = "Integer32"
_FgTdma_Object = MibTableColumn
fgTdma = _FgTdma_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 3, 1, 15),
    _FgTdma_Type()
)
fgTdma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgTdma.setStatus("current")
_FgTrafficInfoTable_Object = MibTable
fgTrafficInfoTable = _FgTrafficInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 4)
)
if mibBuilder.loadTexts:
    fgTrafficInfoTable.setStatus("current")
_FgTrafficInfoEntry_Object = MibTableRow
fgTrafficInfoEntry = _FgTrafficInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 4, 1)
)
fgTrafficInfoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgTrafMdmEntIndex"),
)
if mibBuilder.loadTexts:
    fgTrafficInfoEntry.setStatus("current")
_FgTrafMdmEntIndex_Type = FnIndex
_FgTrafMdmEntIndex_Object = MibTableColumn
fgTrafMdmEntIndex = _FgTrafMdmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 4, 1, 1),
    _FgTrafMdmEntIndex_Type()
)
fgTrafMdmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgTrafMdmEntIndex.setStatus("current")
_FgTxPacksOK_Type = Counter32
_FgTxPacksOK_Object = MibTableColumn
fgTxPacksOK = _FgTxPacksOK_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 4, 1, 2),
    _FgTxPacksOK_Type()
)
fgTxPacksOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgTxPacksOK.setStatus("current")
_FgRxPacksOK_Type = Counter32
_FgRxPacksOK_Object = MibTableColumn
fgRxPacksOK = _FgRxPacksOK_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 4, 1, 3),
    _FgRxPacksOK_Type()
)
fgRxPacksOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgRxPacksOK.setStatus("current")
_FgTxPacksErr_Type = Counter32
_FgTxPacksErr_Object = MibTableColumn
fgTxPacksErr = _FgTxPacksErr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 4, 1, 4),
    _FgTxPacksErr_Type()
)
fgTxPacksErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgTxPacksErr.setStatus("current")
_FgRxPacksErr_Type = Counter32
_FgRxPacksErr_Object = MibTableColumn
fgRxPacksErr = _FgRxPacksErr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 4, 1, 5),
    _FgRxPacksErr_Type()
)
fgRxPacksErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgRxPacksErr.setStatus("current")
_FgTxPacksOverflow_Type = Counter32
_FgTxPacksOverflow_Object = MibTableColumn
fgTxPacksOverflow = _FgTxPacksOverflow_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 4, 1, 6),
    _FgTxPacksOverflow_Type()
)
fgTxPacksOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgTxPacksOverflow.setStatus("current")
_FgRxPacksOverflow_Type = Counter32
_FgRxPacksOverflow_Object = MibTableColumn
fgRxPacksOverflow = _FgRxPacksOverflow_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 4, 1, 7),
    _FgRxPacksOverflow_Type()
)
fgRxPacksOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgRxPacksOverflow.setStatus("current")
_FgTxBytesOK_Type = Counter64
_FgTxBytesOK_Object = MibTableColumn
fgTxBytesOK = _FgTxBytesOK_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 4, 1, 8),
    _FgTxBytesOK_Type()
)
fgTxBytesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgTxBytesOK.setStatus("current")
_FgRxBytesOK_Type = Counter64
_FgRxBytesOK_Object = MibTableColumn
fgRxBytesOK = _FgRxBytesOK_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 4, 1, 9),
    _FgRxBytesOK_Type()
)
fgRxBytesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgRxBytesOK.setStatus("current")
_FgLastCallTxBytesOK_Type = Counter64
_FgLastCallTxBytesOK_Object = MibTableColumn
fgLastCallTxBytesOK = _FgLastCallTxBytesOK_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 4, 1, 10),
    _FgLastCallTxBytesOK_Type()
)
fgLastCallTxBytesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLastCallTxBytesOK.setStatus("current")
_FgLastCallRxBytesOK_Type = Counter64
_FgLastCallRxBytesOK_Object = MibTableColumn
fgLastCallRxBytesOK = _FgLastCallRxBytesOK_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 4, 1, 11),
    _FgLastCallRxBytesOK_Type()
)
fgLastCallRxBytesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLastCallRxBytesOK.setStatus("current")
_FgTxPacksDrop_Type = Counter32
_FgTxPacksDrop_Object = MibTableColumn
fgTxPacksDrop = _FgTxPacksDrop_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 4, 1, 12),
    _FgTxPacksDrop_Type()
)
fgTxPacksDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgTxPacksDrop.setStatus("current")
_FgRxPacksDrop_Type = Counter32
_FgRxPacksDrop_Object = MibTableColumn
fgRxPacksDrop = _FgRxPacksDrop_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 4, 1, 13),
    _FgRxPacksDrop_Type()
)
fgRxPacksDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgRxPacksDrop.setStatus("current")
_FgSessInfoTable_Object = MibTable
fgSessInfoTable = _FgSessInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5)
)
if mibBuilder.loadTexts:
    fgSessInfoTable.setStatus("current")
_FgSessInfoEntry_Object = MibTableRow
fgSessInfoEntry = _FgSessInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1)
)
fgSessInfoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgLteSessEntIndex"),
)
if mibBuilder.loadTexts:
    fgSessInfoEntry.setStatus("current")
_FgLteSessEntIndex_Type = FnIndex
_FgLteSessEntIndex_Object = MibTableColumn
fgLteSessEntIndex = _FgLteSessEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 1),
    _FgLteSessEntIndex_Type()
)
fgLteSessEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgLteSessEntIndex.setStatus("current")
_FgSessMdmEntIndex_Type = FnIndex
_FgSessMdmEntIndex_Object = MibTableColumn
fgSessMdmEntIndex = _FgSessMdmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 2),
    _FgSessMdmEntIndex_Type()
)
fgSessMdmEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSessMdmEntIndex.setStatus("current")


class _FdLteIfName_Type(DisplayString):
    """Custom type fdLteIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FdLteIfName_Type.__name__ = "DisplayString"
_FdLteIfName_Object = MibTableColumn
fdLteIfName = _FdLteIfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 3),
    _FdLteIfName_Type()
)
fdLteIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteIfName.setStatus("current")


class _FdLteSessConnStat_Type(Integer32):
    """Custom type fdLteSessConnStat based on Integer32"""
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
        *(("unknown", 0),
          ("disconnected", 1),
          ("connected", 2),
          ("suspended", 3),
          ("authenticating", 4))
    )


_FdLteSessConnStat_Type.__name__ = "Integer32"
_FdLteSessConnStat_Object = MibTableColumn
fdLteSessConnStat = _FdLteSessConnStat_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 4),
    _FdLteSessConnStat_Type()
)
fdLteSessConnStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteSessConnStat.setStatus("current")


class _FdLteProfId_Type(Integer32):
    """Custom type fdLteProfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FdLteProfId_Type.__name__ = "Integer32"
_FdLteProfId_Object = MibTableColumn
fdLteProfId = _FdLteProfId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 5),
    _FdLteProfId_Type()
)
fdLteProfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteProfId.setStatus("current")


class _FdLteProfName_Type(DisplayString):
    """Custom type fdLteProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FdLteProfName_Type.__name__ = "DisplayString"
_FdLteProfName_Object = MibTableColumn
fdLteProfName = _FdLteProfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 6),
    _FdLteProfName_Type()
)
fdLteProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteProfName.setStatus("current")


class _FdLteProfType_Type(Integer32):
    """Custom type fdLteProfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lpt3gpp", 0),
          ("lpt3gpp2", 1))
    )


_FdLteProfType_Type.__name__ = "Integer32"
_FdLteProfType_Object = MibTableColumn
fdLteProfType = _FdLteProfType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 7),
    _FdLteProfType_Type()
)
fdLteProfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteProfType.setStatus("current")


class _FdLtePdpType_Type(Integer32):
    """Custom type fdLtePdpType based on Integer32"""
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
        *(("ipv4", 0),
          ("ppp", 1),
          ("ipv6", 2),
          ("ipv4v6", 3))
    )


_FdLtePdpType_Type.__name__ = "Integer32"
_FdLtePdpType_Object = MibTableColumn
fdLtePdpType = _FdLtePdpType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 8),
    _FdLtePdpType_Type()
)
fdLtePdpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLtePdpType.setStatus("current")


class _FdLteProfApn_Type(DisplayString):
    """Custom type fdLteProfApn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FdLteProfApn_Type.__name__ = "DisplayString"
_FdLteProfApn_Object = MibTableColumn
fdLteProfApn = _FdLteProfApn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 9),
    _FdLteProfApn_Type()
)
fdLteProfApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteProfApn.setStatus("current")


class _FdLteProfIpFamily_Type(Integer32):
    """Custom type fdLteProfIpFamily based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 4),
          ("ipv6", 6),
          ("unspecified", 8))
    )


_FdLteProfIpFamily_Type.__name__ = "Integer32"
_FdLteProfIpFamily_Object = MibTableColumn
fdLteProfIpFamily = _FdLteProfIpFamily_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 10),
    _FdLteProfIpFamily_Type()
)
fdLteProfIpFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteProfIpFamily.setStatus("current")
_FdLteIpv4Addr_Type = IpAddress
_FdLteIpv4Addr_Object = MibTableColumn
fdLteIpv4Addr = _FdLteIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 11),
    _FdLteIpv4Addr_Type()
)
fdLteIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteIpv4Addr.setStatus("current")
_FdLteIpv4GwAddr_Type = IpAddress
_FdLteIpv4GwAddr_Object = MibTableColumn
fdLteIpv4GwAddr = _FdLteIpv4GwAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 12),
    _FdLteIpv4GwAddr_Type()
)
fdLteIpv4GwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteIpv4GwAddr.setStatus("current")
_FdLteIpv4NetMask_Type = IpAddress
_FdLteIpv4NetMask_Object = MibTableColumn
fdLteIpv4NetMask = _FdLteIpv4NetMask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 13),
    _FdLteIpv4NetMask_Type()
)
fdLteIpv4NetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteIpv4NetMask.setStatus("current")
_FdLteIpv4PriDns_Type = IpAddress
_FdLteIpv4PriDns_Object = MibTableColumn
fdLteIpv4PriDns = _FdLteIpv4PriDns_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 14),
    _FdLteIpv4PriDns_Type()
)
fdLteIpv4PriDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteIpv4PriDns.setStatus("current")
_FdLteIpv4SecDns_Type = IpAddress
_FdLteIpv4SecDns_Object = MibTableColumn
fdLteIpv4SecDns = _FdLteIpv4SecDns_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 15),
    _FdLteIpv4SecDns_Type()
)
fdLteIpv4SecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteIpv4SecDns.setStatus("current")
_FdLteIpv6Addr_Type = Ipv6Address
_FdLteIpv6Addr_Object = MibTableColumn
fdLteIpv6Addr = _FdLteIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 16),
    _FdLteIpv6Addr_Type()
)
fdLteIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteIpv6Addr.setStatus("current")


class _FdLteIpv6PrefLen_Type(Integer32):
    """Custom type fdLteIpv6PrefLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_FdLteIpv6PrefLen_Type.__name__ = "Integer32"
_FdLteIpv6PrefLen_Object = MibTableColumn
fdLteIpv6PrefLen = _FdLteIpv6PrefLen_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 17),
    _FdLteIpv6PrefLen_Type()
)
fdLteIpv6PrefLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteIpv6PrefLen.setStatus("current")
_FdLteIpv6GwAddr_Type = Ipv6Address
_FdLteIpv6GwAddr_Object = MibTableColumn
fdLteIpv6GwAddr = _FdLteIpv6GwAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 18),
    _FdLteIpv6GwAddr_Type()
)
fdLteIpv6GwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteIpv6GwAddr.setStatus("current")


class _FdLteIpv6GwPrefLen_Type(Integer32):
    """Custom type fdLteIpv6GwPrefLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_FdLteIpv6GwPrefLen_Type.__name__ = "Integer32"
_FdLteIpv6GwPrefLen_Object = MibTableColumn
fdLteIpv6GwPrefLen = _FdLteIpv6GwPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 19),
    _FdLteIpv6GwPrefLen_Type()
)
fdLteIpv6GwPrefLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteIpv6GwPrefLen.setStatus("current")
_FdLteIpv6PriDns_Type = Ipv6Address
_FdLteIpv6PriDns_Object = MibTableColumn
fdLteIpv6PriDns = _FdLteIpv6PriDns_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 20),
    _FdLteIpv6PriDns_Type()
)
fdLteIpv6PriDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteIpv6PriDns.setStatus("current")
_FdLteIpv6SecDns_Type = Ipv6Address
_FdLteIpv6SecDns_Object = MibTableColumn
fdLteIpv6SecDns = _FdLteIpv6SecDns_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 21),
    _FdLteIpv6SecDns_Type()
)
fdLteIpv6SecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteIpv6SecDns.setStatus("current")
_FdLteMtu_Type = Integer32
_FdLteMtu_Object = MibTableColumn
fdLteMtu = _FdLteMtu_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 22),
    _FdLteMtu_Type()
)
fdLteMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteMtu.setStatus("current")


class _FdLteAutoConn_Type(Integer32):
    """Custom type fdLteAutoConn based on Integer32"""
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
          ("paused", 2))
    )


_FdLteAutoConn_Type.__name__ = "Integer32"
_FdLteAutoConn_Object = MibTableColumn
fdLteAutoConn = _FdLteAutoConn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 23),
    _FdLteAutoConn_Type()
)
fdLteAutoConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteAutoConn.setStatus("current")


class _FdLteNetType_Type(Integer32):
    """Custom type fdLteNetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
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
        *(("unknown", -1),
          ("cdma1x", 1),
          ("evdo", 2),
          ("gsm", 3),
          ("umts", 4),
          ("evdoReva", 5),
          ("edge", 6),
          ("hsdpa", 7),
          ("hsupa", 8),
          ("hsdpaHsupa", 9),
          ("lte", 10),
          ("ehrpd", 11),
          ("hsdpaPlus", 12),
          ("hsdpaPlusHsupa", 13),
          ("dchsdpaPlus", 14),
          ("dchspdaPlusHsupa", 15))
    )


_FdLteNetType_Type.__name__ = "Integer32"
_FdLteNetType_Object = MibTableColumn
fdLteNetType = _FdLteNetType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 24),
    _FdLteNetType_Type()
)
fdLteNetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteNetType.setStatus("current")


class _FdLteNetTypeLas_Type(Integer32):
    """Custom type fdLteNetTypeLas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
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
        *(("unknown", -1),
          ("cdma1x", 1),
          ("evdo", 2),
          ("gsm", 3),
          ("umts", 4),
          ("evdoReva", 5),
          ("edge", 6),
          ("hsdpa", 7),
          ("hsupa", 8),
          ("hsdpaHsupa", 9),
          ("lte", 10),
          ("ehrpd", 11),
          ("hsdpaPlus", 12),
          ("hsdpaPlusHsupa", 13),
          ("dchsdpaPlus", 14),
          ("dchspdaPlusHsupa", 15))
    )


_FdLteNetTypeLas_Type.__name__ = "Integer32"
_FdLteNetTypeLas_Object = MibTableColumn
fdLteNetTypeLas = _FdLteNetTypeLas_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 25),
    _FdLteNetTypeLas_Type()
)
fdLteNetTypeLas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteNetTypeLas.setStatus("current")


class _FdLteLinkProto_Type(Integer32):
    """Custom type fdLteLinkProto based on Integer32"""
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
          ("ieee8023", 1),
          ("rawIp", 2))
    )


_FdLteLinkProto_Type.__name__ = "Integer32"
_FdLteLinkProto_Object = MibTableColumn
fdLteLinkProto = _FdLteLinkProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 5, 1, 26),
    _FdLteLinkProto_Type()
)
fdLteLinkProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdLteLinkProto.setStatus("current")
_FgGpsInfoTable_Object = MibTable
fgGpsInfoTable = _FgGpsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 6)
)
if mibBuilder.loadTexts:
    fgGpsInfoTable.setStatus("current")
_FgGpsInfoEntry_Object = MibTableRow
fgGpsInfoEntry = _FgGpsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 6, 1)
)
fgGpsInfoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgGpsMdmEntIndex"),
)
if mibBuilder.loadTexts:
    fgGpsInfoEntry.setStatus("current")
_FgGpsMdmEntIndex_Type = FnIndex
_FgGpsMdmEntIndex_Object = MibTableColumn
fgGpsMdmEntIndex = _FgGpsMdmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 6, 1, 1),
    _FgGpsMdmEntIndex_Type()
)
fgGpsMdmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgGpsMdmEntIndex.setStatus("current")


class _FgGpsEnabled_Type(Integer32):
    """Custom type fgGpsEnabled based on Integer32"""
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


_FgGpsEnabled_Type.__name__ = "Integer32"
_FgGpsEnabled_Object = MibTableColumn
fgGpsEnabled = _FgGpsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 6, 1, 2),
    _FgGpsEnabled_Type()
)
fgGpsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgGpsEnabled.setStatus("current")


class _FgLatitude_Type(DisplayString):
    """Custom type fgLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FgLatitude_Type.__name__ = "DisplayString"
_FgLatitude_Object = MibTableColumn
fgLatitude = _FgLatitude_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 6, 1, 3),
    _FgLatitude_Type()
)
fgLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLatitude.setStatus("current")


class _FgLongitude_Type(DisplayString):
    """Custom type fgLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FgLongitude_Type.__name__ = "DisplayString"
_FgLongitude_Object = MibTableColumn
fgLongitude = _FgLongitude_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 6, 1, 4),
    _FgLongitude_Type()
)
fgLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLongitude.setStatus("current")


class _FgUtcTime_Type(DisplayString):
    """Custom type fgUtcTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgUtcTime_Type.__name__ = "DisplayString"
_FgUtcTime_Object = MibTableColumn
fgUtcTime = _FgUtcTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 6, 1, 5),
    _FgUtcTime_Type()
)
fgUtcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgUtcTime.setStatus("current")


class _FgLocalTime_Type(DisplayString):
    """Custom type fgLocalTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgLocalTime_Type.__name__ = "DisplayString"
_FgLocalTime_Object = MibTableColumn
fgLocalTime = _FgLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 6, 1, 6),
    _FgLocalTime_Type()
)
fgLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLocalTime.setStatus("current")
_FgDatausageInfoTable_Object = MibTable
fgDatausageInfoTable = _FgDatausageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 7)
)
if mibBuilder.loadTexts:
    fgDatausageInfoTable.setStatus("current")
_FgDatausageInfoEntry_Object = MibTableRow
fgDatausageInfoEntry = _FgDatausageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 7, 1)
)
fgDatausageInfoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgDatausageMdmEntIndex"),
)
if mibBuilder.loadTexts:
    fgDatausageInfoEntry.setStatus("current")
_FgDatausageMdmEntIndex_Type = FnIndex
_FgDatausageMdmEntIndex_Object = MibTableColumn
fgDatausageMdmEntIndex = _FgDatausageMdmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 7, 1, 1),
    _FgDatausageMdmEntIndex_Type()
)
fgDatausageMdmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgDatausageMdmEntIndex.setStatus("current")


class _FgDatausageEnabled_Type(Integer32):
    """Custom type fgDatausageEnabled based on Integer32"""
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


_FgDatausageEnabled_Type.__name__ = "Integer32"
_FgDatausageEnabled_Object = MibTableColumn
fgDatausageEnabled = _FgDatausageEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 7, 1, 2),
    _FgDatausageEnabled_Type()
)
fgDatausageEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDatausageEnabled.setStatus("current")
_FgDataOut_Type = Counter64
_FgDataOut_Object = MibTableColumn
fgDataOut = _FgDataOut_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 7, 1, 3),
    _FgDataOut_Type()
)
fgDataOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDataOut.setStatus("current")
_FgDataIn_Type = Counter64
_FgDataIn_Object = MibTableColumn
fgDataIn = _FgDataIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 19, 7, 1, 4),
    _FgDataIn_Type()
)
fgDataIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDataIn.setStatus("current")
_FgNPU_ObjectIdentity = ObjectIdentity
fgNPU = _FgNPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 20)
)
_FgNPUInfo_ObjectIdentity = ObjectIdentity
fgNPUInfo = _FgNPUInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 20, 1)
)
_FgNPUNumber_Type = Integer32
_FgNPUNumber_Object = MibScalar
fgNPUNumber = _FgNPUNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 20, 1, 1),
    _FgNPUNumber_Type()
)
fgNPUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgNPUNumber.setStatus("current")


class _FgNPUName_Type(DisplayString):
    """Custom type fgNPUName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgNPUName_Type.__name__ = "DisplayString"
_FgNPUName_Object = MibScalar
fgNPUName = _FgNPUName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 20, 1, 2),
    _FgNPUName_Type()
)
fgNPUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgNPUName.setStatus("current")
_FgNPUDrvDriftSum_Type = Integer32
_FgNPUDrvDriftSum_Object = MibScalar
fgNPUDrvDriftSum = _FgNPUDrvDriftSum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 20, 1, 3),
    _FgNPUDrvDriftSum_Type()
)
fgNPUDrvDriftSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgNPUDrvDriftSum.setStatus("current")
_FgNPUTables_ObjectIdentity = ObjectIdentity
fgNPUTables = _FgNPUTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 20, 2)
)
_FgNPUTable_Object = MibTable
fgNPUTable = _FgNPUTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 20, 2, 1)
)
if mibBuilder.loadTexts:
    fgNPUTable.setStatus("current")
_FgNPUEntry_Object = MibTableRow
fgNPUEntry = _FgNPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 20, 2, 1, 1)
)
fgNPUEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgNPUEntIndex"),
)
if mibBuilder.loadTexts:
    fgNPUEntry.setStatus("current")


class _FgNPUEntIndex_Type(FgNPUIndex):
    """Custom type fgNPUEntIndex based on FgNPUIndex"""
    subtypeSpec = FgNPUIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FgNPUEntIndex_Type.__name__ = "FgNPUIndex"
_FgNPUEntIndex_Object = MibTableColumn
fgNPUEntIndex = _FgNPUEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 20, 2, 1, 1, 1),
    _FgNPUEntIndex_Type()
)
fgNPUEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgNPUEntIndex.setStatus("current")
_FgNPUSessionTblSize_Type = Gauge32
_FgNPUSessionTblSize_Object = MibTableColumn
fgNPUSessionTblSize = _FgNPUSessionTblSize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 20, 2, 1, 1, 2),
    _FgNPUSessionTblSize_Type()
)
fgNPUSessionTblSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgNPUSessionTblSize.setStatus("current")
_FgNPUSessionCount_Type = Gauge32
_FgNPUSessionCount_Object = MibTableColumn
fgNPUSessionCount = _FgNPUSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 20, 2, 1, 1, 3),
    _FgNPUSessionCount_Type()
)
fgNPUSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgNPUSessionCount.setStatus("current")
_FgNPUDrvDrift_Type = Integer32
_FgNPUDrvDrift_Object = MibTableColumn
fgNPUDrvDrift = _FgNPUDrvDrift_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 20, 2, 1, 1, 4),
    _FgNPUDrvDrift_Type()
)
fgNPUDrvDrift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgNPUDrvDrift.setStatus("current")
_FgLog_ObjectIdentity = ObjectIdentity
fgLog = _FgLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 21)
)
_FgLogInfo_ObjectIdentity = ObjectIdentity
fgLogInfo = _FgLogInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 21, 1)
)
_FgLogDeviceNumber_Type = Integer32
_FgLogDeviceNumber_Object = MibScalar
fgLogDeviceNumber = _FgLogDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 21, 1, 1),
    _FgLogDeviceNumber_Type()
)
fgLogDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLogDeviceNumber.setStatus("current")
_FgLogDevices_ObjectIdentity = ObjectIdentity
fgLogDevices = _FgLogDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 21, 2)
)
_FgLogDeviceTable_Object = MibTable
fgLogDeviceTable = _FgLogDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 21, 2, 1)
)
if mibBuilder.loadTexts:
    fgLogDeviceTable.setStatus("current")
_FgLogDeviceEntry_Object = MibTableRow
fgLogDeviceEntry = _FgLogDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 21, 2, 1, 1)
)
fgLogDeviceEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgLogDeviceEntryIndex"),
)
if mibBuilder.loadTexts:
    fgLogDeviceEntry.setStatus("current")


class _FgLogDeviceEntryIndex_Type(FgLogDeviceIndex):
    """Custom type fgLogDeviceEntryIndex based on FgLogDeviceIndex"""
    subtypeSpec = FgLogDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FgLogDeviceEntryIndex_Type.__name__ = "FgLogDeviceIndex"
_FgLogDeviceEntryIndex_Object = MibTableColumn
fgLogDeviceEntryIndex = _FgLogDeviceEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 21, 2, 1, 1, 1),
    _FgLogDeviceEntryIndex_Type()
)
fgLogDeviceEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgLogDeviceEntryIndex.setStatus("current")
_FgLogDeviceEnabled_Type = Integer32
_FgLogDeviceEnabled_Object = MibTableColumn
fgLogDeviceEnabled = _FgLogDeviceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 21, 2, 1, 1, 2),
    _FgLogDeviceEnabled_Type()
)
fgLogDeviceEnabled.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgLogDeviceEnabled.setStatus("current")


class _FgLogDeviceName_Type(DisplayString):
    """Custom type fgLogDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FgLogDeviceName_Type.__name__ = "DisplayString"
_FgLogDeviceName_Object = MibTableColumn
fgLogDeviceName = _FgLogDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 21, 2, 1, 1, 3),
    _FgLogDeviceName_Type()
)
fgLogDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLogDeviceName.setStatus("current")
_FgLogDeviceSentCount_Type = Counter32
_FgLogDeviceSentCount_Object = MibTableColumn
fgLogDeviceSentCount = _FgLogDeviceSentCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 21, 2, 1, 1, 4),
    _FgLogDeviceSentCount_Type()
)
fgLogDeviceSentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLogDeviceSentCount.setStatus("current")
_FgLogDeviceRelayedCount_Type = Counter32
_FgLogDeviceRelayedCount_Object = MibTableColumn
fgLogDeviceRelayedCount = _FgLogDeviceRelayedCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 21, 2, 1, 1, 5),
    _FgLogDeviceRelayedCount_Type()
)
fgLogDeviceRelayedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLogDeviceRelayedCount.setStatus("current")
_FgLogDeviceCachedCount_Type = Gauge32
_FgLogDeviceCachedCount_Object = MibTableColumn
fgLogDeviceCachedCount = _FgLogDeviceCachedCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 21, 2, 1, 1, 6),
    _FgLogDeviceCachedCount_Type()
)
fgLogDeviceCachedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLogDeviceCachedCount.setStatus("current")
_FgLogDeviceFailedCount_Type = Counter32
_FgLogDeviceFailedCount_Object = MibTableColumn
fgLogDeviceFailedCount = _FgLogDeviceFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 21, 2, 1, 1, 7),
    _FgLogDeviceFailedCount_Type()
)
fgLogDeviceFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLogDeviceFailedCount.setStatus("current")
_FgLogDeviceDroppedCount_Type = Counter32
_FgLogDeviceDroppedCount_Object = MibTableColumn
fgLogDeviceDroppedCount = _FgLogDeviceDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 21, 2, 1, 1, 8),
    _FgLogDeviceDroppedCount_Type()
)
fgLogDeviceDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgLogDeviceDroppedCount.setStatus("current")
_FgConfig_ObjectIdentity = ObjectIdentity
fgConfig = _FgConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 22)
)
_FgConfigStatus_ObjectIdentity = ObjectIdentity
fgConfigStatus = _FgConfigStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 22, 1)
)
_FgConfigSerial_Type = Counter32
_FgConfigSerial_Object = MibScalar
fgConfigSerial = _FgConfigSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 22, 1, 1),
    _FgConfigSerial_Type()
)
fgConfigSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgConfigSerial.setStatus("current")
_FgConfigChecksum_Type = OctetString
_FgConfigChecksum_Object = MibScalar
fgConfigChecksum = _FgConfigChecksum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 22, 1, 2),
    _FgConfigChecksum_Type()
)
fgConfigChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgConfigChecksum.setStatus("current")
_FgConfigLastChangeTime_Type = TimeStamp
_FgConfigLastChangeTime_Object = MibScalar
fgConfigLastChangeTime = _FgConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 22, 1, 3),
    _FgConfigLastChangeTime_Type()
)
fgConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgConfigLastChangeTime.setStatus("current")
_FgDhcp_ObjectIdentity = ObjectIdentity
fgDhcp = _FgDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 23)
)
_FgDhcpInfo_ObjectIdentity = ObjectIdentity
fgDhcpInfo = _FgDhcpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 23, 1)
)
_FgDhcpServerNumber_Type = Integer32
_FgDhcpServerNumber_Object = MibScalar
fgDhcpServerNumber = _FgDhcpServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 23, 1, 1),
    _FgDhcpServerNumber_Type()
)
fgDhcpServerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDhcpServerNumber.setStatus("current")
_FgDhcpTables_ObjectIdentity = ObjectIdentity
fgDhcpTables = _FgDhcpTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 23, 2)
)
_FgDhcpTable_Object = MibTable
fgDhcpTable = _FgDhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 23, 2, 1)
)
if mibBuilder.loadTexts:
    fgDhcpTable.setStatus("current")
_FgDhcpEntry_Object = MibTableRow
fgDhcpEntry = _FgDhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 23, 2, 1, 1)
)
fgDhcpEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgDhcpEntry.setStatus("current")
_FgDhcpLeaseUsage_Type = Integer32
_FgDhcpLeaseUsage_Object = MibTableColumn
fgDhcpLeaseUsage = _FgDhcpLeaseUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 23, 2, 1, 1, 2),
    _FgDhcpLeaseUsage_Type()
)
fgDhcpLeaseUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgDhcpLeaseUsage.setStatus("current")
_FgDhcpTrapObjects_ObjectIdentity = ObjectIdentity
fgDhcpTrapObjects = _FgDhcpTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 23, 3)
)


class _FgDhcpTrapType_Type(Integer32):
    """Custom type fgDhcpTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("runOutOfIPPool", 1),
          ("conflictIP", 2),
          ("receivedNAK", 3))
    )


_FgDhcpTrapType_Type.__name__ = "Integer32"
_FgDhcpTrapType_Object = MibScalar
fgDhcpTrapType = _FgDhcpTrapType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 23, 3, 1),
    _FgDhcpTrapType_Type()
)
fgDhcpTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgDhcpTrapType.setStatus("current")
_FgDhcpTrapMessage_Type = DisplayString
_FgDhcpTrapMessage_Object = MibScalar
fgDhcpTrapMessage = _FgDhcpTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 23, 3, 2),
    _FgDhcpTrapMessage_Type()
)
fgDhcpTrapMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgDhcpTrapMessage.setStatus("current")
_FgDhcpServerId_Type = FnIndex
_FgDhcpServerId_Object = MibScalar
fgDhcpServerId = _FgDhcpServerId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 23, 3, 3),
    _FgDhcpServerId_Type()
)
fgDhcpServerId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgDhcpServerId.setStatus("current")
_FgSw_ObjectIdentity = ObjectIdentity
fgSw = _FgSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24)
)
_FgSwDeviceInfo_ObjectIdentity = ObjectIdentity
fgSwDeviceInfo = _FgSwDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1)
)
_FgSwDeviceTable_Object = MibTable
fgSwDeviceTable = _FgSwDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1, 1)
)
if mibBuilder.loadTexts:
    fgSwDeviceTable.setStatus("current")
_FgSwDeviceEntry_Object = MibTableRow
fgSwDeviceEntry = _FgSwDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1, 1, 1)
)
fgSwDeviceEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgSwDevicePlatform"),
    (0, "FORTINET-FORTIGATE-MIB", "fgSwDeviceId"),
)
if mibBuilder.loadTexts:
    fgSwDeviceEntry.setStatus("current")
_FgSwDevicePlatform_Type = FnIndex
_FgSwDevicePlatform_Object = MibTableColumn
fgSwDevicePlatform = _FgSwDevicePlatform_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1, 1, 1, 1),
    _FgSwDevicePlatform_Type()
)
fgSwDevicePlatform.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgSwDevicePlatform.setStatus("current")
_FgSwDeviceId_Type = FnIndex
_FgSwDeviceId_Object = MibTableColumn
fgSwDeviceId = _FgSwDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1, 1, 1, 2),
    _FgSwDeviceId_Type()
)
fgSwDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgSwDeviceId.setStatus("current")
_FgSwDeviceSerialNum_Type = DisplayString
_FgSwDeviceSerialNum_Object = MibTableColumn
fgSwDeviceSerialNum = _FgSwDeviceSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1, 1, 1, 3),
    _FgSwDeviceSerialNum_Type()
)
fgSwDeviceSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwDeviceSerialNum.setStatus("current")
_FgSwDeviceName_Type = DisplayString
_FgSwDeviceName_Object = MibTableColumn
fgSwDeviceName = _FgSwDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1, 1, 1, 4),
    _FgSwDeviceName_Type()
)
fgSwDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwDeviceName.setStatus("current")
_FgSwDeviceVersion_Type = DisplayString
_FgSwDeviceVersion_Object = MibTableColumn
fgSwDeviceVersion = _FgSwDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1, 1, 1, 5),
    _FgSwDeviceVersion_Type()
)
fgSwDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwDeviceVersion.setStatus("current")


class _FgSwDeviceAuthorized_Type(Integer32):
    """Custom type fgSwDeviceAuthorized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discovered", 0),
          ("disabled", 1),
          ("authorized", 2))
    )


_FgSwDeviceAuthorized_Type.__name__ = "Integer32"
_FgSwDeviceAuthorized_Object = MibTableColumn
fgSwDeviceAuthorized = _FgSwDeviceAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1, 1, 1, 6),
    _FgSwDeviceAuthorized_Type()
)
fgSwDeviceAuthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwDeviceAuthorized.setStatus("current")


class _FgSwDeviceStatus_Type(Integer32):
    """Custom type fgSwDeviceStatus based on Integer32"""
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


_FgSwDeviceStatus_Type.__name__ = "Integer32"
_FgSwDeviceStatus_Object = MibTableColumn
fgSwDeviceStatus = _FgSwDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1, 1, 1, 7),
    _FgSwDeviceStatus_Type()
)
fgSwDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwDeviceStatus.setStatus("current")
_FgSwDeviceJoinTime_Type = Gauge32
_FgSwDeviceJoinTime_Object = MibTableColumn
fgSwDeviceJoinTime = _FgSwDeviceJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1, 1, 1, 8),
    _FgSwDeviceJoinTime_Type()
)
fgSwDeviceJoinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwDeviceJoinTime.setStatus("current")
_FgSwDeviceIp_Type = IpAddress
_FgSwDeviceIp_Object = MibTableColumn
fgSwDeviceIp = _FgSwDeviceIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1, 1, 1, 9),
    _FgSwDeviceIp_Type()
)
fgSwDeviceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwDeviceIp.setStatus("current")
_FgSwDeviceFlag_Type = DisplayString
_FgSwDeviceFlag_Object = MibTableColumn
fgSwDeviceFlag = _FgSwDeviceFlag_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1, 1, 1, 10),
    _FgSwDeviceFlag_Type()
)
fgSwDeviceFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwDeviceFlag.setStatus("current")


class _FgSwCpu_Type(Integer32):
    """Custom type fgSwCpu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgSwCpu_Type.__name__ = "Integer32"
_FgSwCpu_Object = MibTableColumn
fgSwCpu = _FgSwCpu_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1, 1, 1, 11),
    _FgSwCpu_Type()
)
fgSwCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwCpu.setStatus("current")


class _FgSwMemory_Type(Integer32):
    """Custom type fgSwMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgSwMemory_Type.__name__ = "Integer32"
_FgSwMemory_Object = MibTableColumn
fgSwMemory = _FgSwMemory_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1, 1, 1, 12),
    _FgSwMemory_Type()
)
fgSwMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwMemory.setStatus("current")
_FgSwDeviceIpv6_Type = Ipv6Address
_FgSwDeviceIpv6_Object = MibTableColumn
fgSwDeviceIpv6 = _FgSwDeviceIpv6_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 1, 1, 1, 13),
    _FgSwDeviceIpv6_Type()
)
fgSwDeviceIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwDeviceIpv6.setStatus("current")
_FgSwPortInfo_ObjectIdentity = ObjectIdentity
fgSwPortInfo = _FgSwPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2)
)
_FgSwPortTable_Object = MibTable
fgSwPortTable = _FgSwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1)
)
if mibBuilder.loadTexts:
    fgSwPortTable.setStatus("current")
_FgSwPortEntry_Object = MibTableRow
fgSwPortEntry = _FgSwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1, 1)
)
fgSwPortEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgSwPortSwitchPlatform"),
    (0, "FORTINET-FORTIGATE-MIB", "fgSwPortSwitchId"),
    (0, "FORTINET-FORTIGATE-MIB", "fgSwPortNum"),
)
if mibBuilder.loadTexts:
    fgSwPortEntry.setStatus("current")
_FgSwPortSwitchPlatform_Type = FnIndex
_FgSwPortSwitchPlatform_Object = MibTableColumn
fgSwPortSwitchPlatform = _FgSwPortSwitchPlatform_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1, 1, 1),
    _FgSwPortSwitchPlatform_Type()
)
fgSwPortSwitchPlatform.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgSwPortSwitchPlatform.setStatus("current")
_FgSwPortSwitchId_Type = FnIndex
_FgSwPortSwitchId_Object = MibTableColumn
fgSwPortSwitchId = _FgSwPortSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1, 1, 2),
    _FgSwPortSwitchId_Type()
)
fgSwPortSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgSwPortSwitchId.setStatus("current")
_FgSwPortNum_Type = FnIndex
_FgSwPortNum_Object = MibTableColumn
fgSwPortNum = _FgSwPortNum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1, 1, 3),
    _FgSwPortNum_Type()
)
fgSwPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgSwPortNum.setStatus("current")
_FgSwPortSwitchSerialNum_Type = DisplayString
_FgSwPortSwitchSerialNum_Object = MibTableColumn
fgSwPortSwitchSerialNum = _FgSwPortSwitchSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1, 1, 4),
    _FgSwPortSwitchSerialNum_Type()
)
fgSwPortSwitchSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwPortSwitchSerialNum.setStatus("current")
_FgSwPortName_Type = DisplayString
_FgSwPortName_Object = MibTableColumn
fgSwPortName = _FgSwPortName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1, 1, 5),
    _FgSwPortName_Type()
)
fgSwPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwPortName.setStatus("current")


class _FgSwPortStatus_Type(Integer32):
    """Custom type fgSwPortStatus based on Integer32"""
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


_FgSwPortStatus_Type.__name__ = "Integer32"
_FgSwPortStatus_Object = MibTableColumn
fgSwPortStatus = _FgSwPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1, 1, 6),
    _FgSwPortStatus_Type()
)
fgSwPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwPortStatus.setStatus("current")
_FgSwPortSpeedDuplex_Type = DisplayString
_FgSwPortSpeedDuplex_Object = MibTableColumn
fgSwPortSpeedDuplex = _FgSwPortSpeedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1, 1, 7),
    _FgSwPortSpeedDuplex_Type()
)
fgSwPortSpeedDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwPortSpeedDuplex.setStatus("current")
_FgSwPortNativeVlan_Type = Integer32
_FgSwPortNativeVlan_Object = MibTableColumn
fgSwPortNativeVlan = _FgSwPortNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1, 1, 8),
    _FgSwPortNativeVlan_Type()
)
fgSwPortNativeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwPortNativeVlan.setStatus("current")
_FgSwPortAllowedVlan_Type = DisplayString
_FgSwPortAllowedVlan_Object = MibTableColumn
fgSwPortAllowedVlan = _FgSwPortAllowedVlan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1, 1, 9),
    _FgSwPortAllowedVlan_Type()
)
fgSwPortAllowedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwPortAllowedVlan.setStatus("current")
_FgSwPortUntaggedVlan_Type = DisplayString
_FgSwPortUntaggedVlan_Object = MibTableColumn
fgSwPortUntaggedVlan = _FgSwPortUntaggedVlan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1, 1, 10),
    _FgSwPortUntaggedVlan_Type()
)
fgSwPortUntaggedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwPortUntaggedVlan.setStatus("current")


class _FgSwPortPOE_Type(Integer32):
    """Custom type fgSwPortPOE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notcapable", 0),
          ("capable", 1))
    )


_FgSwPortPOE_Type.__name__ = "Integer32"
_FgSwPortPOE_Object = MibTableColumn
fgSwPortPOE = _FgSwPortPOE_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1, 1, 11),
    _FgSwPortPOE_Type()
)
fgSwPortPOE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwPortPOE.setStatus("current")


class _FgSwPortPOEStatus_Type(Integer32):
    """Custom type fgSwPortPOEStatus based on Integer32"""
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


_FgSwPortPOEStatus_Type.__name__ = "Integer32"
_FgSwPortPOEStatus_Object = MibTableColumn
fgSwPortPOEStatus = _FgSwPortPOEStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1, 1, 12),
    _FgSwPortPOEStatus_Type()
)
fgSwPortPOEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwPortPOEStatus.setStatus("current")
_FgSwPortPOEState_Type = DisplayString
_FgSwPortPOEState_Object = MibTableColumn
fgSwPortPOEState = _FgSwPortPOEState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1, 1, 13),
    _FgSwPortPOEState_Type()
)
fgSwPortPOEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwPortPOEState.setStatus("current")
_FgSwPortPOEPower_Type = DisplayString
_FgSwPortPOEPower_Object = MibTableColumn
fgSwPortPOEPower = _FgSwPortPOEPower_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 24, 2, 1, 1, 14),
    _FgSwPortPOEPower_Type()
)
fgSwPortPOEPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSwPortPOEPower.setStatus("current")
_FgChassis_ObjectIdentity = ObjectIdentity
fgChassis = _FgChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 25)
)
_FgChassisInfo_ObjectIdentity = ObjectIdentity
fgChassisInfo = _FgChassisInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 25, 1)
)
_FgChassisVersion_Type = DisplayString
_FgChassisVersion_Object = MibScalar
fgChassisVersion = _FgChassisVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 25, 1, 1),
    _FgChassisVersion_Type()
)
fgChassisVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgChassisVersion.setStatus("current")
_FgChassisTrapObjects_ObjectIdentity = ObjectIdentity
fgChassisTrapObjects = _FgChassisTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 25, 2)
)
_FgChassisSlotId_Type = Integer32
_FgChassisSlotId_Object = MibScalar
fgChassisSlotId = _FgChassisSlotId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 25, 2, 1),
    _FgChassisSlotId_Type()
)
fgChassisSlotId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgChassisSlotId.setStatus("current")
_FgChassisTrapMessage_Type = DisplayString
_FgChassisTrapMessage_Object = MibScalar
fgChassisTrapMessage = _FgChassisTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 25, 2, 2),
    _FgChassisTrapMessage_Type()
)
fgChassisTrapMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fgChassisTrapMessage.setStatus("current")
_FgServiceGroupWorkerBlades_ObjectIdentity = ObjectIdentity
fgServiceGroupWorkerBlades = _FgServiceGroupWorkerBlades_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26)
)
_FgSgWbTables_ObjectIdentity = ObjectIdentity
fgSgWbTables = _FgSgWbTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1)
)
_FgSgWorkerBladeTable_Object = MibTable
fgSgWorkerBladeTable = _FgSgWorkerBladeTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1)
)
if mibBuilder.loadTexts:
    fgSgWorkerBladeTable.setStatus("current")
_FgSgWorkerBladeEntry_Object = MibTableRow
fgSgWorkerBladeEntry = _FgSgWorkerBladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1)
)
fgSgWorkerBladeEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgSgWbEntIndex"),
)
if mibBuilder.loadTexts:
    fgSgWorkerBladeEntry.setStatus("current")
_FgSgWbEntIndex_Type = FgSgWorkerBladeIndex
_FgSgWbEntIndex_Object = MibTableColumn
fgSgWbEntIndex = _FgSgWbEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 1),
    _FgSgWbEntIndex_Type()
)
fgSgWbEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgSgWbEntIndex.setStatus("current")
_FgSgWbServiceGroupID_Type = Integer32
_FgSgWbServiceGroupID_Object = MibTableColumn
fgSgWbServiceGroupID = _FgSgWbServiceGroupID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 2),
    _FgSgWbServiceGroupID_Type()
)
fgSgWbServiceGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSgWbServiceGroupID.setStatus("current")
_FgSgWbChassisID_Type = Integer32
_FgSgWbChassisID_Object = MibTableColumn
fgSgWbChassisID = _FgSgWbChassisID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 3),
    _FgSgWbChassisID_Type()
)
fgSgWbChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSgWbChassisID.setStatus("current")
_FgSgWbSlotID_Type = Integer32
_FgSgWbSlotID_Object = MibTableColumn
fgSgWbSlotID = _FgSgWbSlotID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 4),
    _FgSgWbSlotID_Type()
)
fgSgWbSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSgWbSlotID.setStatus("current")
_FgSgWbState_Type = FgSgWorkerBladeState
_FgSgWbState_Object = MibTableColumn
fgSgWbState = _FgSgWbState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 5),
    _FgSgWbState_Type()
)
fgSgWbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSgWbState.setStatus("current")


class _FgSgWbStatusMsg_Type(DisplayString):
    """Custom type fgSgWbStatusMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgSgWbStatusMsg_Type.__name__ = "DisplayString"
_FgSgWbStatusMsg_Object = MibTableColumn
fgSgWbStatusMsg = _FgSgWbStatusMsg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 6),
    _FgSgWbStatusMsg_Type()
)
fgSgWbStatusMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSgWbStatusMsg.setStatus("current")


class _FgSgWbMaster_Type(Integer32):
    """Custom type fgSgWbMaster based on Integer32"""
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


_FgSgWbMaster_Type.__name__ = "Integer32"
_FgSgWbMaster_Object = MibTableColumn
fgSgWbMaster = _FgSgWbMaster_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 7),
    _FgSgWbMaster_Type()
)
fgSgWbMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSgWbMaster.setStatus("current")


class _FgSgWbSysVersion_Type(DisplayString):
    """Custom type fgSgWbSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgSgWbSysVersion_Type.__name__ = "DisplayString"
_FgSgWbSysVersion_Object = MibTableColumn
fgSgWbSysVersion = _FgSgWbSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 8),
    _FgSgWbSysVersion_Type()
)
fgSgWbSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSgWbSysVersion.setStatus("current")


class _FgSgWbSysSerial_Type(DisplayString):
    """Custom type fgSgWbSysSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FgSgWbSysSerial_Type.__name__ = "DisplayString"
_FgSgWbSysSerial_Object = MibTableColumn
fgSgWbSysSerial = _FgSgWbSysSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 9),
    _FgSgWbSysSerial_Type()
)
fgSgWbSysSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSgWbSysSerial.setStatus("current")
_FgSgWbSysUpTime_Type = TimeTicks
_FgSgWbSysUpTime_Object = MibTableColumn
fgSgWbSysUpTime = _FgSgWbSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 10),
    _FgSgWbSysUpTime_Type()
)
fgSgWbSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSgWbSysUpTime.setStatus("current")


class _FgSgWbSysCpuUsage_Type(Gauge32):
    """Custom type fgSgWbSysCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgSgWbSysCpuUsage_Type.__name__ = "Gauge32"
_FgSgWbSysCpuUsage_Object = MibTableColumn
fgSgWbSysCpuUsage = _FgSgWbSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 11),
    _FgSgWbSysCpuUsage_Type()
)
fgSgWbSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSgWbSysCpuUsage.setStatus("current")
if mibBuilder.loadTexts:
    fgSgWbSysCpuUsage.setUnits("%")


class _FgSgWbSysMemUsage_Type(Gauge32):
    """Custom type fgSgWbSysMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FgSgWbSysMemUsage_Type.__name__ = "Gauge32"
_FgSgWbSysMemUsage_Object = MibTableColumn
fgSgWbSysMemUsage = _FgSgWbSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 12),
    _FgSgWbSysMemUsage_Type()
)
fgSgWbSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSgWbSysMemUsage.setStatus("current")
if mibBuilder.loadTexts:
    fgSgWbSysMemUsage.setUnits("%")


class _FgSgWbBaseLink_Type(DisplayString):
    """Custom type fgSgWbBaseLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgSgWbBaseLink_Type.__name__ = "DisplayString"
_FgSgWbBaseLink_Object = MibTableColumn
fgSgWbBaseLink = _FgSgWbBaseLink_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 13),
    _FgSgWbBaseLink_Type()
)
fgSgWbBaseLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSgWbBaseLink.setStatus("current")


class _FgSgWbFabricLink_Type(DisplayString):
    """Custom type fgSgWbFabricLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgSgWbFabricLink_Type.__name__ = "DisplayString"
_FgSgWbFabricLink_Object = MibTableColumn
fgSgWbFabricLink = _FgSgWbFabricLink_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 14),
    _FgSgWbFabricLink_Type()
)
fgSgWbFabricLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSgWbFabricLink.setStatus("current")


class _FgSgWbDataHb_Type(DisplayString):
    """Custom type fgSgWbDataHb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgSgWbDataHb_Type.__name__ = "DisplayString"
_FgSgWbDataHb_Object = MibTableColumn
fgSgWbDataHb = _FgSgWbDataHb_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 15),
    _FgSgWbDataHb_Type()
)
fgSgWbDataHb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSgWbDataHb.setStatus("current")


class _FgSgWbMgmtHb_Type(DisplayString):
    """Custom type fgSgWbMgmtHb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FgSgWbMgmtHb_Type.__name__ = "DisplayString"
_FgSgWbMgmtHb_Object = MibTableColumn
fgSgWbMgmtHb = _FgSgWbMgmtHb_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 26, 1, 1, 1, 16),
    _FgSgWbMgmtHb_Type()
)
fgSgWbMgmtHb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgSgWbMgmtHb.setStatus("current")
_FgEms_ObjectIdentity = ObjectIdentity
fgEms = _FgEms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27)
)
_FgEmsTables_ObjectIdentity = ObjectIdentity
fgEmsTables = _FgEmsTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2)
)
_FgEmsGlobalTable_Object = MibTable
fgEmsGlobalTable = _FgEmsGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 1)
)
if mibBuilder.loadTexts:
    fgEmsGlobalTable.setStatus("current")
_FgEmsGlobalEntry_Object = MibTableRow
fgEmsGlobalEntry = _FgEmsGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 1, 1)
)
fgEmsGlobalEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgEmsGlobalEntIndex"),
)
if mibBuilder.loadTexts:
    fgEmsGlobalEntry.setStatus("current")
_FgEmsGlobalEntIndex_Type = FnIndex
_FgEmsGlobalEntIndex_Object = MibTableColumn
fgEmsGlobalEntIndex = _FgEmsGlobalEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 1, 1, 1),
    _FgEmsGlobalEntIndex_Type()
)
fgEmsGlobalEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgEmsGlobalEntIndex.setStatus("current")
_FgEmsGlobalEntStatus_Type = FnBoolState
_FgEmsGlobalEntStatus_Object = MibTableColumn
fgEmsGlobalEntStatus = _FgEmsGlobalEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 1, 1, 2),
    _FgEmsGlobalEntStatus_Type()
)
fgEmsGlobalEntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgEmsGlobalEntStatus.setStatus("current")
_FgEmsGlobalEntConnectionName_Type = DisplayString
_FgEmsGlobalEntConnectionName_Object = MibTableColumn
fgEmsGlobalEntConnectionName = _FgEmsGlobalEntConnectionName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 1, 1, 3),
    _FgEmsGlobalEntConnectionName_Type()
)
fgEmsGlobalEntConnectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgEmsGlobalEntConnectionName.setStatus("current")


class _FgEmsGlobalEntConnectionStatus_Type(Integer32):
    """Custom type fgEmsGlobalEntConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connecting", 1),
          ("connected", 2))
    )


_FgEmsGlobalEntConnectionStatus_Type.__name__ = "Integer32"
_FgEmsGlobalEntConnectionStatus_Object = MibTableColumn
fgEmsGlobalEntConnectionStatus = _FgEmsGlobalEntConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 1, 1, 4),
    _FgEmsGlobalEntConnectionStatus_Type()
)
fgEmsGlobalEntConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgEmsGlobalEntConnectionStatus.setStatus("current")
_FgEmsGlobalEntLastCloseReason_Type = Integer32
_FgEmsGlobalEntLastCloseReason_Object = MibTableColumn
fgEmsGlobalEntLastCloseReason = _FgEmsGlobalEntLastCloseReason_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 1, 1, 5),
    _FgEmsGlobalEntLastCloseReason_Type()
)
fgEmsGlobalEntLastCloseReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgEmsGlobalEntLastCloseReason.setStatus("current")
_FgEmsGlobalEntLastCloseReasonDesc_Type = DisplayString
_FgEmsGlobalEntLastCloseReasonDesc_Object = MibTableColumn
fgEmsGlobalEntLastCloseReasonDesc = _FgEmsGlobalEntLastCloseReasonDesc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 1, 1, 6),
    _FgEmsGlobalEntLastCloseReasonDesc_Type()
)
fgEmsGlobalEntLastCloseReasonDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgEmsGlobalEntLastCloseReasonDesc.setStatus("current")
_FgEmsGlobalEntLastCloseTime_Type = TimeTicks
_FgEmsGlobalEntLastCloseTime_Object = MibTableColumn
fgEmsGlobalEntLastCloseTime = _FgEmsGlobalEntLastCloseTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 1, 1, 7),
    _FgEmsGlobalEntLastCloseTime_Type()
)
fgEmsGlobalEntLastCloseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgEmsGlobalEntLastCloseTime.setStatus("current")
_FgEmsVdTable_Object = MibTable
fgEmsVdTable = _FgEmsVdTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 2)
)
if mibBuilder.loadTexts:
    fgEmsVdTable.setStatus("current")
_FgEmsVdEntry_Object = MibTableRow
fgEmsVdEntry = _FgEmsVdEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 2, 1)
)
fgEmsVdEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
    (0, "FORTINET-FORTIGATE-MIB", "fgEmsVdEntIndex"),
)
if mibBuilder.loadTexts:
    fgEmsVdEntry.setStatus("current")
_FgEmsVdEntIndex_Type = FnIndex
_FgEmsVdEntIndex_Object = MibTableColumn
fgEmsVdEntIndex = _FgEmsVdEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 2, 1, 1),
    _FgEmsVdEntIndex_Type()
)
fgEmsVdEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fgEmsVdEntIndex.setStatus("current")
_FgEmsVdEntStatus_Type = FnBoolState
_FgEmsVdEntStatus_Object = MibTableColumn
fgEmsVdEntStatus = _FgEmsVdEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 2, 1, 2),
    _FgEmsVdEntStatus_Type()
)
fgEmsVdEntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgEmsVdEntStatus.setStatus("current")
_FgEmsVdEntConnectionName_Type = DisplayString
_FgEmsVdEntConnectionName_Object = MibTableColumn
fgEmsVdEntConnectionName = _FgEmsVdEntConnectionName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 2, 1, 3),
    _FgEmsVdEntConnectionName_Type()
)
fgEmsVdEntConnectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgEmsVdEntConnectionName.setStatus("current")


class _FgEmsVdEntConnectionStatus_Type(Integer32):
    """Custom type fgEmsVdEntConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connecting", 1),
          ("connected", 2))
    )


_FgEmsVdEntConnectionStatus_Type.__name__ = "Integer32"
_FgEmsVdEntConnectionStatus_Object = MibTableColumn
fgEmsVdEntConnectionStatus = _FgEmsVdEntConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 2, 1, 4),
    _FgEmsVdEntConnectionStatus_Type()
)
fgEmsVdEntConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgEmsVdEntConnectionStatus.setStatus("current")
_FgEmsVdEntLastCloseReason_Type = Integer32
_FgEmsVdEntLastCloseReason_Object = MibTableColumn
fgEmsVdEntLastCloseReason = _FgEmsVdEntLastCloseReason_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 2, 1, 5),
    _FgEmsVdEntLastCloseReason_Type()
)
fgEmsVdEntLastCloseReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgEmsVdEntLastCloseReason.setStatus("current")
_FgEmsVdEntLastCloseReasonDesc_Type = DisplayString
_FgEmsVdEntLastCloseReasonDesc_Object = MibTableColumn
fgEmsVdEntLastCloseReasonDesc = _FgEmsVdEntLastCloseReasonDesc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 2, 1, 6),
    _FgEmsVdEntLastCloseReasonDesc_Type()
)
fgEmsVdEntLastCloseReasonDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgEmsVdEntLastCloseReasonDesc.setStatus("current")
_FgEmsVdEntLastCloseTime_Type = TimeTicks
_FgEmsVdEntLastCloseTime_Object = MibTableColumn
fgEmsVdEntLastCloseTime = _FgEmsVdEntLastCloseTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 27, 2, 2, 1, 7),
    _FgEmsVdEntLastCloseTime_Type()
)
fgEmsVdEntLastCloseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fgEmsVdEntLastCloseTime.setStatus("current")
_FgInternal5GModemsInfo_ObjectIdentity = ObjectIdentity
fgInternal5GModemsInfo = _FgInternal5GModemsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28)
)
_Fg5gMdmInfo_ObjectIdentity = ObjectIdentity
fg5gMdmInfo = _Fg5gMdmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 1)
)
_Fg5gModemNumber_Type = Integer32
_Fg5gModemNumber_Object = MibScalar
fg5gModemNumber = _Fg5gModemNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 1, 1),
    _Fg5gModemNumber_Type()
)
fg5gModemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gModemNumber.setStatus("current")
_Fg5gMdmInfoTable_Object = MibTable
fg5gMdmInfoTable = _Fg5gMdmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2)
)
if mibBuilder.loadTexts:
    fg5gMdmInfoTable.setStatus("current")
_Fg5gMdmInfoEntry_Object = MibTableRow
fg5gMdmInfoEntry = _Fg5gMdmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2, 1)
)
fg5gMdmInfoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fg5gMdmEntIndex"),
)
if mibBuilder.loadTexts:
    fg5gMdmInfoEntry.setStatus("current")
_Fg5gMdmEntIndex_Type = FnIndex
_Fg5gMdmEntIndex_Object = MibTableColumn
fg5gMdmEntIndex = _Fg5gMdmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2, 1, 1),
    _Fg5gMdmEntIndex_Type()
)
fg5gMdmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fg5gMdmEntIndex.setStatus("current")


class _Fg5gMdmDetected_Type(Integer32):
    """Custom type fg5gMdmDetected based on Integer32"""
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


_Fg5gMdmDetected_Type.__name__ = "Integer32"
_Fg5gMdmDetected_Object = MibTableColumn
fg5gMdmDetected = _Fg5gMdmDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2, 1, 2),
    _Fg5gMdmDetected_Type()
)
fg5gMdmDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gMdmDetected.setStatus("current")


class _Fg5gMdmVendor_Type(DisplayString):
    """Custom type fg5gMdmVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Fg5gMdmVendor_Type.__name__ = "DisplayString"
_Fg5gMdmVendor_Object = MibTableColumn
fg5gMdmVendor = _Fg5gMdmVendor_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2, 1, 3),
    _Fg5gMdmVendor_Type()
)
fg5gMdmVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gMdmVendor.setStatus("current")


class _Fg5gMdmModel_Type(DisplayString):
    """Custom type fg5gMdmModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Fg5gMdmModel_Type.__name__ = "DisplayString"
_Fg5gMdmModel_Object = MibTableColumn
fg5gMdmModel = _Fg5gMdmModel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2, 1, 4),
    _Fg5gMdmModel_Type()
)
fg5gMdmModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gMdmModel.setStatus("current")


class _Fg5gMdmRevision_Type(DisplayString):
    """Custom type fg5gMdmRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Fg5gMdmRevision_Type.__name__ = "DisplayString"
_Fg5gMdmRevision_Object = MibTableColumn
fg5gMdmRevision = _Fg5gMdmRevision_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2, 1, 5),
    _Fg5gMdmRevision_Type()
)
fg5gMdmRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gMdmRevision.setStatus("current")


class _Fg5gMdmImei_Type(DisplayString):
    """Custom type fg5gMdmImei based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Fg5gMdmImei_Type.__name__ = "DisplayString"
_Fg5gMdmImei_Object = MibTableColumn
fg5gMdmImei = _Fg5gMdmImei_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2, 1, 6),
    _Fg5gMdmImei_Type()
)
fg5gMdmImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gMdmImei.setStatus("current")


class _Fg5gMdmHwRevision_Type(DisplayString):
    """Custom type fg5gMdmHwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Fg5gMdmHwRevision_Type.__name__ = "DisplayString"
_Fg5gMdmHwRevision_Object = MibTableColumn
fg5gMdmHwRevision = _Fg5gMdmHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2, 1, 7),
    _Fg5gMdmHwRevision_Type()
)
fg5gMdmHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gMdmHwRevision.setStatus("current")


class _Fg5gMdmMeid_Type(DisplayString):
    """Custom type fg5gMdmMeid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Fg5gMdmMeid_Type.__name__ = "DisplayString"
_Fg5gMdmMeid_Object = MibTableColumn
fg5gMdmMeid = _Fg5gMdmMeid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2, 1, 8),
    _Fg5gMdmMeid_Type()
)
fg5gMdmMeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gMdmMeid.setStatus("current")


class _Fg5gMdmSwRev_Type(DisplayString):
    """Custom type fg5gMdmSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Fg5gMdmSwRev_Type.__name__ = "DisplayString"
_Fg5gMdmSwRev_Object = MibTableColumn
fg5gMdmSwRev = _Fg5gMdmSwRev_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2, 1, 9),
    _Fg5gMdmSwRev_Type()
)
fg5gMdmSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gMdmSwRev.setStatus("current")


class _Fg5gMdmPriFwVer_Type(DisplayString):
    """Custom type fg5gMdmPriFwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fg5gMdmPriFwVer_Type.__name__ = "DisplayString"
_Fg5gMdmPriFwVer_Object = MibTableColumn
fg5gMdmPriFwVer = _Fg5gMdmPriFwVer_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2, 1, 10),
    _Fg5gMdmPriFwVer_Type()
)
fg5gMdmPriFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gMdmPriFwVer.setStatus("current")


class _Fg5gMdmFwName_Type(DisplayString):
    """Custom type fg5gMdmFwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fg5gMdmFwName_Type.__name__ = "DisplayString"
_Fg5gMdmFwName_Object = MibTableColumn
fg5gMdmFwName = _Fg5gMdmFwName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2, 1, 11),
    _Fg5gMdmFwName_Type()
)
fg5gMdmFwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gMdmFwName.setStatus("current")


class _Fg5gMdmOpMode_Type(Integer32):
    """Custom type fg5gMdmOpMode based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("online", 0),
          ("lowPower", 1),
          ("factoryTest", 2),
          ("offLine", 3),
          ("reset", 4),
          ("shuttingDown", 5),
          ("persistentLowPower", 6),
          ("modeOnlyLowPower", 7),
          ("unknown", 255))
    )


_Fg5gMdmOpMode_Type.__name__ = "Integer32"
_Fg5gMdmOpMode_Object = MibTableColumn
fg5gMdmOpMode = _Fg5gMdmOpMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2, 1, 12),
    _Fg5gMdmOpMode_Type()
)
fg5gMdmOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gMdmOpMode.setStatus("current")


class _Fg5gMdmTemperature_Type(Integer32):
    """Custom type fg5gMdmTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Fg5gMdmTemperature_Type.__name__ = "Integer32"
_Fg5gMdmTemperature_Object = MibTableColumn
fg5gMdmTemperature = _Fg5gMdmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2, 1, 13),
    _Fg5gMdmTemperature_Type()
)
fg5gMdmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gMdmTemperature.setStatus("current")


class _Fg5gNetworkMode_Type(DisplayString):
    """Custom type fg5gNetworkMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fg5gNetworkMode_Type.__name__ = "DisplayString"
_Fg5gNetworkMode_Object = MibTableColumn
fg5gNetworkMode = _Fg5gNetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 2, 1, 14),
    _Fg5gNetworkMode_Type()
)
fg5gNetworkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gNetworkMode.setStatus("current")
_Fg5gSimInfoTable_Object = MibTable
fg5gSimInfoTable = _Fg5gSimInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 3)
)
if mibBuilder.loadTexts:
    fg5gSimInfoTable.setStatus("current")
_Fg5gSimInfoEntry_Object = MibTableRow
fg5gSimInfoEntry = _Fg5gSimInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 3, 1)
)
fg5gSimInfoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fg5gSimMdmEntIndex"),
)
if mibBuilder.loadTexts:
    fg5gSimInfoEntry.setStatus("current")
_Fg5gSimMdmEntIndex_Type = FnIndex
_Fg5gSimMdmEntIndex_Object = MibTableColumn
fg5gSimMdmEntIndex = _Fg5gSimMdmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 3, 1, 1),
    _Fg5gSimMdmEntIndex_Type()
)
fg5gSimMdmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fg5gSimMdmEntIndex.setStatus("current")


class _Fg5gIdleSimState_Type(DisplayString):
    """Custom type fg5gIdleSimState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Fg5gIdleSimState_Type.__name__ = "DisplayString"
_Fg5gIdleSimState_Object = MibTableColumn
fg5gIdleSimState = _Fg5gIdleSimState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 3, 1, 2),
    _Fg5gIdleSimState_Type()
)
fg5gIdleSimState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIdleSimState.setStatus("current")


class _Fg5gIdleSimIccid_Type(DisplayString):
    """Custom type fg5gIdleSimIccid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Fg5gIdleSimIccid_Type.__name__ = "DisplayString"
_Fg5gIdleSimIccid_Object = MibTableColumn
fg5gIdleSimIccid = _Fg5gIdleSimIccid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 3, 1, 3),
    _Fg5gIdleSimIccid_Type()
)
fg5gIdleSimIccid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIdleSimIccid.setStatus("current")


class _Fg5gActiveSimState_Type(DisplayString):
    """Custom type fg5gActiveSimState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Fg5gActiveSimState_Type.__name__ = "DisplayString"
_Fg5gActiveSimState_Object = MibTableColumn
fg5gActiveSimState = _Fg5gActiveSimState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 3, 1, 4),
    _Fg5gActiveSimState_Type()
)
fg5gActiveSimState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gActiveSimState.setStatus("current")


class _Fg5gActiveSimIccid_Type(DisplayString):
    """Custom type fg5gActiveSimIccid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Fg5gActiveSimIccid_Type.__name__ = "DisplayString"
_Fg5gActiveSimIccid_Object = MibTableColumn
fg5gActiveSimIccid = _Fg5gActiveSimIccid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 3, 1, 5),
    _Fg5gActiveSimIccid_Type()
)
fg5gActiveSimIccid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gActiveSimIccid.setStatus("current")


class _Fg5gActiveSimMsisdn_Type(DisplayString):
    """Custom type fg5gActiveSimMsisdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Fg5gActiveSimMsisdn_Type.__name__ = "DisplayString"
_Fg5gActiveSimMsisdn_Object = MibTableColumn
fg5gActiveSimMsisdn = _Fg5gActiveSimMsisdn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 3, 1, 6),
    _Fg5gActiveSimMsisdn_Type()
)
fg5gActiveSimMsisdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gActiveSimMsisdn.setStatus("current")


class _Fg5gActiveSimImsi_Type(DisplayString):
    """Custom type fg5gActiveSimImsi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Fg5gActiveSimImsi_Type.__name__ = "DisplayString"
_Fg5gActiveSimImsi_Object = MibTableColumn
fg5gActiveSimImsi = _Fg5gActiveSimImsi_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 3, 1, 7),
    _Fg5gActiveSimImsi_Type()
)
fg5gActiveSimImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gActiveSimImsi.setStatus("current")


class _Fg5gActiveSimCountry_Type(DisplayString):
    """Custom type fg5gActiveSimCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Fg5gActiveSimCountry_Type.__name__ = "DisplayString"
_Fg5gActiveSimCountry_Object = MibTableColumn
fg5gActiveSimCountry = _Fg5gActiveSimCountry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 3, 1, 8),
    _Fg5gActiveSimCountry_Type()
)
fg5gActiveSimCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gActiveSimCountry.setStatus("current")


class _Fg5gActiveSimNetwork_Type(DisplayString):
    """Custom type fg5gActiveSimNetwork based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fg5gActiveSimNetwork_Type.__name__ = "DisplayString"
_Fg5gActiveSimNetwork_Object = MibTableColumn
fg5gActiveSimNetwork = _Fg5gActiveSimNetwork_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 3, 1, 9),
    _Fg5gActiveSimNetwork_Type()
)
fg5gActiveSimNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gActiveSimNetwork.setStatus("current")


class _Fg5gActiveSimPinState_Type(DisplayString):
    """Custom type fg5gActiveSimPinState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fg5gActiveSimPinState_Type.__name__ = "DisplayString"
_Fg5gActiveSimPinState_Object = MibTableColumn
fg5gActiveSimPinState = _Fg5gActiveSimPinState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 3, 1, 10),
    _Fg5gActiveSimPinState_Type()
)
fg5gActiveSimPinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gActiveSimPinState.setStatus("current")
_Fg5gSignalInfoTable_Object = MibTable
fg5gSignalInfoTable = _Fg5gSignalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 4)
)
if mibBuilder.loadTexts:
    fg5gSignalInfoTable.setStatus("current")
_Fg5gSignalInfoEntry_Object = MibTableRow
fg5gSignalInfoEntry = _Fg5gSignalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 4, 1)
)
fg5gSignalInfoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fg5gSigMdmEntIndex"),
)
if mibBuilder.loadTexts:
    fg5gSignalInfoEntry.setStatus("current")
_Fg5gSigMdmEntIndex_Type = FnIndex
_Fg5gSigMdmEntIndex_Object = MibTableColumn
fg5gSigMdmEntIndex = _Fg5gSigMdmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 4, 1, 1),
    _Fg5gSigMdmEntIndex_Type()
)
fg5gSigMdmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fg5gSigMdmEntIndex.setStatus("current")


class _Fg5gSigWcdmaRssi_Type(Integer32):
    """Custom type fg5gSigWcdmaRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Fg5gSigWcdmaRssi_Type.__name__ = "Integer32"
_Fg5gSigWcdmaRssi_Object = MibTableColumn
fg5gSigWcdmaRssi = _Fg5gSigWcdmaRssi_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 4, 1, 2),
    _Fg5gSigWcdmaRssi_Type()
)
fg5gSigWcdmaRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gSigWcdmaRssi.setStatus("current")


class _Fg5gSigWcdmaEcio_Type(Integer32):
    """Custom type fg5gSigWcdmaEcio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65536, 65535),
    )


_Fg5gSigWcdmaEcio_Type.__name__ = "Integer32"
_Fg5gSigWcdmaEcio_Object = MibTableColumn
fg5gSigWcdmaEcio = _Fg5gSigWcdmaEcio_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 4, 1, 3),
    _Fg5gSigWcdmaEcio_Type()
)
fg5gSigWcdmaEcio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gSigWcdmaEcio.setStatus("current")


class _Fg5gSigLteRssi_Type(Integer32):
    """Custom type fg5gSigLteRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Fg5gSigLteRssi_Type.__name__ = "Integer32"
_Fg5gSigLteRssi_Object = MibTableColumn
fg5gSigLteRssi = _Fg5gSigLteRssi_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 4, 1, 4),
    _Fg5gSigLteRssi_Type()
)
fg5gSigLteRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gSigLteRssi.setStatus("current")


class _Fg5gSigLteRsrq_Type(Integer32):
    """Custom type fg5gSigLteRsrq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_Fg5gSigLteRsrq_Type.__name__ = "Integer32"
_Fg5gSigLteRsrq_Object = MibTableColumn
fg5gSigLteRsrq = _Fg5gSigLteRsrq_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 4, 1, 5),
    _Fg5gSigLteRsrq_Type()
)
fg5gSigLteRsrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gSigLteRsrq.setStatus("current")


class _Fg5gSigLteRsrp_Type(Integer32):
    """Custom type fg5gSigLteRsrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65536, 65535),
    )


_Fg5gSigLteRsrp_Type.__name__ = "Integer32"
_Fg5gSigLteRsrp_Object = MibTableColumn
fg5gSigLteRsrp = _Fg5gSigLteRsrp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 4, 1, 6),
    _Fg5gSigLteRsrp_Type()
)
fg5gSigLteRsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gSigLteRsrp.setStatus("current")


class _Fg5gSigLteSnr_Type(Integer32):
    """Custom type fg5gSigLteSnr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65536, 65535),
    )


_Fg5gSigLteSnr_Type.__name__ = "Integer32"
_Fg5gSigLteSnr_Object = MibTableColumn
fg5gSigLteSnr = _Fg5gSigLteSnr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 4, 1, 7),
    _Fg5gSigLteSnr_Type()
)
fg5gSigLteSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gSigLteSnr.setStatus("current")


class _Fg5gSig5gRsrp_Type(Integer32):
    """Custom type fg5gSig5gRsrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65536, 65535),
    )


_Fg5gSig5gRsrp_Type.__name__ = "Integer32"
_Fg5gSig5gRsrp_Object = MibTableColumn
fg5gSig5gRsrp = _Fg5gSig5gRsrp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 4, 1, 8),
    _Fg5gSig5gRsrp_Type()
)
fg5gSig5gRsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gSig5gRsrp.setStatus("current")


class _Fg5gSig5gSnr_Type(Integer32):
    """Custom type fg5gSig5gSnr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-65536, 65535),
    )


_Fg5gSig5gSnr_Type.__name__ = "Integer32"
_Fg5gSig5gSnr_Object = MibTableColumn
fg5gSig5gSnr = _Fg5gSig5gSnr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 4, 1, 9),
    _Fg5gSig5gSnr_Type()
)
fg5gSig5gSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gSig5gSnr.setStatus("current")
_Fg5gTrafficInfoTable_Object = MibTable
fg5gTrafficInfoTable = _Fg5gTrafficInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5)
)
if mibBuilder.loadTexts:
    fg5gTrafficInfoTable.setStatus("current")
_Fg5gTrafficInfoEntry_Object = MibTableRow
fg5gTrafficInfoEntry = _Fg5gTrafficInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1)
)
fg5gTrafficInfoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fg5gTrafMdmEntIndex"),
)
if mibBuilder.loadTexts:
    fg5gTrafficInfoEntry.setStatus("current")
_Fg5gTrafMdmEntIndex_Type = FnIndex
_Fg5gTrafMdmEntIndex_Object = MibTableColumn
fg5gTrafMdmEntIndex = _Fg5gTrafMdmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 1),
    _Fg5gTrafMdmEntIndex_Type()
)
fg5gTrafMdmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fg5gTrafMdmEntIndex.setStatus("current")
_Fg5gIpv4TxPacksOK_Type = Counter32
_Fg5gIpv4TxPacksOK_Object = MibTableColumn
fg5gIpv4TxPacksOK = _Fg5gIpv4TxPacksOK_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 2),
    _Fg5gIpv4TxPacksOK_Type()
)
fg5gIpv4TxPacksOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4TxPacksOK.setStatus("current")
_Fg5gIpv4RxPacksOK_Type = Counter32
_Fg5gIpv4RxPacksOK_Object = MibTableColumn
fg5gIpv4RxPacksOK = _Fg5gIpv4RxPacksOK_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 3),
    _Fg5gIpv4RxPacksOK_Type()
)
fg5gIpv4RxPacksOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4RxPacksOK.setStatus("current")
_Fg5gIpv4TxPacksErr_Type = Counter32
_Fg5gIpv4TxPacksErr_Object = MibTableColumn
fg5gIpv4TxPacksErr = _Fg5gIpv4TxPacksErr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 4),
    _Fg5gIpv4TxPacksErr_Type()
)
fg5gIpv4TxPacksErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4TxPacksErr.setStatus("current")
_Fg5gIpv4RxPacksErr_Type = Counter32
_Fg5gIpv4RxPacksErr_Object = MibTableColumn
fg5gIpv4RxPacksErr = _Fg5gIpv4RxPacksErr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 5),
    _Fg5gIpv4RxPacksErr_Type()
)
fg5gIpv4RxPacksErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4RxPacksErr.setStatus("current")
_Fg5gIpv4TxPacksOverflow_Type = Counter32
_Fg5gIpv4TxPacksOverflow_Object = MibTableColumn
fg5gIpv4TxPacksOverflow = _Fg5gIpv4TxPacksOverflow_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 6),
    _Fg5gIpv4TxPacksOverflow_Type()
)
fg5gIpv4TxPacksOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4TxPacksOverflow.setStatus("current")
_Fg5gIpv4RxPacksOverflow_Type = Counter32
_Fg5gIpv4RxPacksOverflow_Object = MibTableColumn
fg5gIpv4RxPacksOverflow = _Fg5gIpv4RxPacksOverflow_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 7),
    _Fg5gIpv4RxPacksOverflow_Type()
)
fg5gIpv4RxPacksOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4RxPacksOverflow.setStatus("current")
_Fg5gIpv4TxBytesOK_Type = Counter64
_Fg5gIpv4TxBytesOK_Object = MibTableColumn
fg5gIpv4TxBytesOK = _Fg5gIpv4TxBytesOK_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 8),
    _Fg5gIpv4TxBytesOK_Type()
)
fg5gIpv4TxBytesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4TxBytesOK.setStatus("current")
_Fg5gIpv4RxBytesOK_Type = Counter64
_Fg5gIpv4RxBytesOK_Object = MibTableColumn
fg5gIpv4RxBytesOK = _Fg5gIpv4RxBytesOK_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 9),
    _Fg5gIpv4RxBytesOK_Type()
)
fg5gIpv4RxBytesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4RxBytesOK.setStatus("current")
_Fg5gIpv4TxPacksDrop_Type = Counter32
_Fg5gIpv4TxPacksDrop_Object = MibTableColumn
fg5gIpv4TxPacksDrop = _Fg5gIpv4TxPacksDrop_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 10),
    _Fg5gIpv4TxPacksDrop_Type()
)
fg5gIpv4TxPacksDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4TxPacksDrop.setStatus("current")
_Fg5gIpv4RxPacksDrop_Type = Counter32
_Fg5gIpv4RxPacksDrop_Object = MibTableColumn
fg5gIpv4RxPacksDrop = _Fg5gIpv4RxPacksDrop_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 11),
    _Fg5gIpv4RxPacksDrop_Type()
)
fg5gIpv4RxPacksDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4RxPacksDrop.setStatus("current")
_Fg5gIpv6TxPacksOK_Type = Counter32
_Fg5gIpv6TxPacksOK_Object = MibTableColumn
fg5gIpv6TxPacksOK = _Fg5gIpv6TxPacksOK_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 12),
    _Fg5gIpv6TxPacksOK_Type()
)
fg5gIpv6TxPacksOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6TxPacksOK.setStatus("current")
_Fg5gIpv6RxPacksOK_Type = Counter32
_Fg5gIpv6RxPacksOK_Object = MibTableColumn
fg5gIpv6RxPacksOK = _Fg5gIpv6RxPacksOK_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 13),
    _Fg5gIpv6RxPacksOK_Type()
)
fg5gIpv6RxPacksOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6RxPacksOK.setStatus("current")
_Fg5gIpv6TxPacksErr_Type = Counter32
_Fg5gIpv6TxPacksErr_Object = MibTableColumn
fg5gIpv6TxPacksErr = _Fg5gIpv6TxPacksErr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 14),
    _Fg5gIpv6TxPacksErr_Type()
)
fg5gIpv6TxPacksErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6TxPacksErr.setStatus("current")
_Fg5gIpv6RxPacksErr_Type = Counter32
_Fg5gIpv6RxPacksErr_Object = MibTableColumn
fg5gIpv6RxPacksErr = _Fg5gIpv6RxPacksErr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 15),
    _Fg5gIpv6RxPacksErr_Type()
)
fg5gIpv6RxPacksErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6RxPacksErr.setStatus("current")
_Fg5gIpv6TxPacksOverflow_Type = Counter32
_Fg5gIpv6TxPacksOverflow_Object = MibTableColumn
fg5gIpv6TxPacksOverflow = _Fg5gIpv6TxPacksOverflow_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 16),
    _Fg5gIpv6TxPacksOverflow_Type()
)
fg5gIpv6TxPacksOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6TxPacksOverflow.setStatus("current")
_Fg5gIpv6RxPacksOverflow_Type = Counter32
_Fg5gIpv6RxPacksOverflow_Object = MibTableColumn
fg5gIpv6RxPacksOverflow = _Fg5gIpv6RxPacksOverflow_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 17),
    _Fg5gIpv6RxPacksOverflow_Type()
)
fg5gIpv6RxPacksOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6RxPacksOverflow.setStatus("current")
_Fg5gIpv6TxBytesOK_Type = Counter64
_Fg5gIpv6TxBytesOK_Object = MibTableColumn
fg5gIpv6TxBytesOK = _Fg5gIpv6TxBytesOK_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 18),
    _Fg5gIpv6TxBytesOK_Type()
)
fg5gIpv6TxBytesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6TxBytesOK.setStatus("current")
_Fg5gIpv6RxBytesOK_Type = Counter64
_Fg5gIpv6RxBytesOK_Object = MibTableColumn
fg5gIpv6RxBytesOK = _Fg5gIpv6RxBytesOK_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 19),
    _Fg5gIpv6RxBytesOK_Type()
)
fg5gIpv6RxBytesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6RxBytesOK.setStatus("current")
_Fg5gIpv6TxPacksDrop_Type = Counter32
_Fg5gIpv6TxPacksDrop_Object = MibTableColumn
fg5gIpv6TxPacksDrop = _Fg5gIpv6TxPacksDrop_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 20),
    _Fg5gIpv6TxPacksDrop_Type()
)
fg5gIpv6TxPacksDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6TxPacksDrop.setStatus("current")
_Fg5gIpv6RxPacksDrop_Type = Counter32
_Fg5gIpv6RxPacksDrop_Object = MibTableColumn
fg5gIpv6RxPacksDrop = _Fg5gIpv6RxPacksDrop_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 5, 1, 21),
    _Fg5gIpv6RxPacksDrop_Type()
)
fg5gIpv6RxPacksDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6RxPacksDrop.setStatus("current")
_Fg5gSessInfoTable_Object = MibTable
fg5gSessInfoTable = _Fg5gSessInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6)
)
if mibBuilder.loadTexts:
    fg5gSessInfoTable.setStatus("current")
_Fg5gSessInfoEntry_Object = MibTableRow
fg5gSessInfoEntry = _Fg5gSessInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1)
)
fg5gSessInfoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fg5gSessMdmEntIndex"),
)
if mibBuilder.loadTexts:
    fg5gSessInfoEntry.setStatus("current")
_Fg5gSessMdmEntIndex_Type = FnIndex
_Fg5gSessMdmEntIndex_Object = MibTableColumn
fg5gSessMdmEntIndex = _Fg5gSessMdmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 1),
    _Fg5gSessMdmEntIndex_Type()
)
fg5gSessMdmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fg5gSessMdmEntIndex.setStatus("current")


class _Fg5gIfName_Type(DisplayString):
    """Custom type fg5gIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fg5gIfName_Type.__name__ = "DisplayString"
_Fg5gIfName_Object = MibTableColumn
fg5gIfName = _Fg5gIfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 2),
    _Fg5gIfName_Type()
)
fg5gIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIfName.setStatus("current")
_Fg5gMtu_Type = Integer32
_Fg5gMtu_Object = MibTableColumn
fg5gMtu = _Fg5gMtu_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 3),
    _Fg5gMtu_Type()
)
fg5gMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gMtu.setStatus("current")


class _Fg5gProfId_Type(Integer32):
    """Custom type fg5gProfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fg5gProfId_Type.__name__ = "Integer32"
_Fg5gProfId_Object = MibTableColumn
fg5gProfId = _Fg5gProfId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 4),
    _Fg5gProfId_Type()
)
fg5gProfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gProfId.setStatus("current")


class _Fg5gProfName_Type(DisplayString):
    """Custom type fg5gProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Fg5gProfName_Type.__name__ = "DisplayString"
_Fg5gProfName_Object = MibTableColumn
fg5gProfName = _Fg5gProfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 5),
    _Fg5gProfName_Type()
)
fg5gProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gProfName.setStatus("current")


class _Fg5gPdpType_Type(Integer32):
    """Custom type fg5gPdpType based on Integer32"""
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
        *(("ipv4", 0),
          ("ppp", 1),
          ("ipv6", 2),
          ("ipv4v6", 3))
    )


_Fg5gPdpType_Type.__name__ = "Integer32"
_Fg5gPdpType_Object = MibTableColumn
fg5gPdpType = _Fg5gPdpType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 6),
    _Fg5gPdpType_Type()
)
fg5gPdpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gPdpType.setStatus("current")


class _Fg5gProfApn_Type(DisplayString):
    """Custom type fg5gProfApn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Fg5gProfApn_Type.__name__ = "DisplayString"
_Fg5gProfApn_Object = MibTableColumn
fg5gProfApn = _Fg5gProfApn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 7),
    _Fg5gProfApn_Type()
)
fg5gProfApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gProfApn.setStatus("current")


class _Fg5gIpv4SessionStatus_Type(Integer32):
    """Custom type fg5gIpv4SessionStatus based on Integer32"""
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
        *(("unknown", 0),
          ("disconnected", 1),
          ("connected", 2),
          ("suspended", 3),
          ("authenticating", 4))
    )


_Fg5gIpv4SessionStatus_Type.__name__ = "Integer32"
_Fg5gIpv4SessionStatus_Object = MibTableColumn
fg5gIpv4SessionStatus = _Fg5gIpv4SessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 8),
    _Fg5gIpv4SessionStatus_Type()
)
fg5gIpv4SessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4SessionStatus.setStatus("current")
_Fg5gIpv4Addr_Type = IpAddress
_Fg5gIpv4Addr_Object = MibTableColumn
fg5gIpv4Addr = _Fg5gIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 9),
    _Fg5gIpv4Addr_Type()
)
fg5gIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4Addr.setStatus("current")
_Fg5gIpv4GwAddr_Type = IpAddress
_Fg5gIpv4GwAddr_Object = MibTableColumn
fg5gIpv4GwAddr = _Fg5gIpv4GwAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 10),
    _Fg5gIpv4GwAddr_Type()
)
fg5gIpv4GwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4GwAddr.setStatus("current")
_Fg5gIpv4NetMask_Type = IpAddress
_Fg5gIpv4NetMask_Object = MibTableColumn
fg5gIpv4NetMask = _Fg5gIpv4NetMask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 11),
    _Fg5gIpv4NetMask_Type()
)
fg5gIpv4NetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4NetMask.setStatus("current")
_Fg5gIpv4PriDns_Type = IpAddress
_Fg5gIpv4PriDns_Object = MibTableColumn
fg5gIpv4PriDns = _Fg5gIpv4PriDns_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 12),
    _Fg5gIpv4PriDns_Type()
)
fg5gIpv4PriDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4PriDns.setStatus("current")
_Fg5gIpv4SecDns_Type = IpAddress
_Fg5gIpv4SecDns_Object = MibTableColumn
fg5gIpv4SecDns = _Fg5gIpv4SecDns_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 13),
    _Fg5gIpv4SecDns_Type()
)
fg5gIpv4SecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv4SecDns.setStatus("current")


class _Fg5gIpv6SessionStatus_Type(Integer32):
    """Custom type fg5gIpv6SessionStatus based on Integer32"""
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
        *(("unknown", 0),
          ("disconnected", 1),
          ("connected", 2),
          ("suspended", 3),
          ("authenticating", 4))
    )


_Fg5gIpv6SessionStatus_Type.__name__ = "Integer32"
_Fg5gIpv6SessionStatus_Object = MibTableColumn
fg5gIpv6SessionStatus = _Fg5gIpv6SessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 14),
    _Fg5gIpv6SessionStatus_Type()
)
fg5gIpv6SessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6SessionStatus.setStatus("current")
_Fg5gIpv6Addr_Type = Ipv6Address
_Fg5gIpv6Addr_Object = MibTableColumn
fg5gIpv6Addr = _Fg5gIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 15),
    _Fg5gIpv6Addr_Type()
)
fg5gIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6Addr.setStatus("current")


class _Fg5gIpv6PrefLen_Type(Integer32):
    """Custom type fg5gIpv6PrefLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Fg5gIpv6PrefLen_Type.__name__ = "Integer32"
_Fg5gIpv6PrefLen_Object = MibTableColumn
fg5gIpv6PrefLen = _Fg5gIpv6PrefLen_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 16),
    _Fg5gIpv6PrefLen_Type()
)
fg5gIpv6PrefLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6PrefLen.setStatus("current")
_Fg5gIpv6GwAddr_Type = Ipv6Address
_Fg5gIpv6GwAddr_Object = MibTableColumn
fg5gIpv6GwAddr = _Fg5gIpv6GwAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 17),
    _Fg5gIpv6GwAddr_Type()
)
fg5gIpv6GwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6GwAddr.setStatus("current")


class _Fg5gIpv6GwPrefLen_Type(Integer32):
    """Custom type fg5gIpv6GwPrefLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Fg5gIpv6GwPrefLen_Type.__name__ = "Integer32"
_Fg5gIpv6GwPrefLen_Object = MibTableColumn
fg5gIpv6GwPrefLen = _Fg5gIpv6GwPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 18),
    _Fg5gIpv6GwPrefLen_Type()
)
fg5gIpv6GwPrefLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6GwPrefLen.setStatus("current")
_Fg5gIpv6PriDns_Type = Ipv6Address
_Fg5gIpv6PriDns_Object = MibTableColumn
fg5gIpv6PriDns = _Fg5gIpv6PriDns_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 19),
    _Fg5gIpv6PriDns_Type()
)
fg5gIpv6PriDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6PriDns.setStatus("current")
_Fg5gIpv6SecDns_Type = Ipv6Address
_Fg5gIpv6SecDns_Object = MibTableColumn
fg5gIpv6SecDns = _Fg5gIpv6SecDns_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 6, 1, 20),
    _Fg5gIpv6SecDns_Type()
)
fg5gIpv6SecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gIpv6SecDns.setStatus("current")
_Fg5gGpsInfoTable_Object = MibTable
fg5gGpsInfoTable = _Fg5gGpsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 7)
)
if mibBuilder.loadTexts:
    fg5gGpsInfoTable.setStatus("current")
_Fg5gGpsInfoEntry_Object = MibTableRow
fg5gGpsInfoEntry = _Fg5gGpsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 7, 1)
)
fg5gGpsInfoEntry.setIndexNames(
    (0, "FORTINET-FORTIGATE-MIB", "fg5gGpsMdmEntIndex"),
)
if mibBuilder.loadTexts:
    fg5gGpsInfoEntry.setStatus("current")
_Fg5gGpsMdmEntIndex_Type = FnIndex
_Fg5gGpsMdmEntIndex_Object = MibTableColumn
fg5gGpsMdmEntIndex = _Fg5gGpsMdmEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 7, 1, 1),
    _Fg5gGpsMdmEntIndex_Type()
)
fg5gGpsMdmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fg5gGpsMdmEntIndex.setStatus("current")


class _Fg5gGpsEnabled_Type(Integer32):
    """Custom type fg5gGpsEnabled based on Integer32"""
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


_Fg5gGpsEnabled_Type.__name__ = "Integer32"
_Fg5gGpsEnabled_Object = MibTableColumn
fg5gGpsEnabled = _Fg5gGpsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 7, 1, 2),
    _Fg5gGpsEnabled_Type()
)
fg5gGpsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gGpsEnabled.setStatus("current")


class _Fg5gLatitude_Type(DisplayString):
    """Custom type fg5gLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fg5gLatitude_Type.__name__ = "DisplayString"
_Fg5gLatitude_Object = MibTableColumn
fg5gLatitude = _Fg5gLatitude_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 7, 1, 3),
    _Fg5gLatitude_Type()
)
fg5gLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gLatitude.setStatus("current")


class _Fg5gLongitude_Type(DisplayString):
    """Custom type fg5gLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fg5gLongitude_Type.__name__ = "DisplayString"
_Fg5gLongitude_Object = MibTableColumn
fg5gLongitude = _Fg5gLongitude_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 7, 1, 4),
    _Fg5gLongitude_Type()
)
fg5gLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gLongitude.setStatus("current")


class _Fg5gUtcTime_Type(DisplayString):
    """Custom type fg5gUtcTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Fg5gUtcTime_Type.__name__ = "DisplayString"
_Fg5gUtcTime_Object = MibTableColumn
fg5gUtcTime = _Fg5gUtcTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 7, 1, 5),
    _Fg5gUtcTime_Type()
)
fg5gUtcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gUtcTime.setStatus("current")


class _Fg5gLocalTime_Type(DisplayString):
    """Custom type fg5gLocalTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Fg5gLocalTime_Type.__name__ = "DisplayString"
_Fg5gLocalTime_Object = MibTableColumn
fg5gLocalTime = _Fg5gLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 101, 28, 7, 1, 6),
    _Fg5gLocalTime_Type()
)
fg5gLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fg5gLocalTime.setStatus("current")
_FgMibConformance_ObjectIdentity = ObjectIdentity
fgMibConformance = _FgMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100)
)
fnAdminEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgAdminEntry")
)
fgAdminEntry.setIndexNames(*fnAdminEntry.getIndexNames())
ifEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgIntfEntry")
)
fgIntfEntry.setIndexNames(*ifEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgAvStatsEntry")
)
fgAvStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgIpsStatsEntry")
)
fgIpsStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgWebfilterStatsEntry")
)
fgWebfilterStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgFortiGuardStatsEntry")
)
fgFortiGuardStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApHTTPStatsEntry")
)
fgApHTTPStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApSMTPStatsEntry")
)
fgApSMTPStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApPOP3StatsEntry")
)
fgApPOP3StatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApIMAPStatsEntry")
)
fgApIMAPStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApNNTPStatsEntry")
)
fgApNNTPStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApIMStatsEntry")
)
fgApIMStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApSIPStatsEntry")
)
fgApSIPStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgAppVoIPStatsEntry")
)
fgAppVoIPStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgAppP2PStatsEntry")
)
fgAppP2PStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgAppIMStatsEntry")
)
fgAppIMStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgApFTPStatsEntry")
)
fgApFTPStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgIpSessStatsEntry")
)
fgIpSessStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgIp6SessStatsEntry")
)
fgIp6SessStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())
fgVdEntry.registerAugmentions(
    ("FORTINET-FORTIGATE-MIB",
     "fgVpnSslStatsEntry")
)
fgVpnSslStatsEntry.setIndexNames(*fgVdEntry.getIndexNames())

# Managed Objects groups

fgFmTrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 2)
)
fgFmTrapObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgManIfIp"),
        ("FORTINET-FORTIGATE-MIB", "fgManIfMask"),
        ("FORTINET-FORTIGATE-MIB", "fgManIfIp6"),
        ("FORTINET-FORTIGATE-MIB", "fgFazTrapType"))
)
if mibBuilder.loadTexts:
    fgFmTrapObjectGroup.setStatus("current")

fgAdminObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 3)
)
fgAdminObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgAdminIdleTimeout"),
        ("FORTINET-FORTIGATE-MIB", "fgAdminLcdProtection"))
)
if mibBuilder.loadTexts:
    fgAdminObjectGroup.setStatus("current")

fgSystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 4)
)
fgSystemObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgSysVersion"),
        ("FORTINET-FORTIGATE-MIB", "fgSysCpuUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgSysMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgSysMemCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgSysFreeMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgSysFreeableMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgSysDiskUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgSysDiskCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSesCount"),
        ("FORTINET-FORTIGATE-MIB", "fgSysLowMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgSysLowMemCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSesRate1"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSesRate10"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSesRate30"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSesRate60"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSes6Count"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSes6Rate1"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSes6Rate10"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSes6Rate30"),
        ("FORTINET-FORTIGATE-MIB", "fgSysSes6Rate60"),
        ("FORTINET-FORTIGATE-MIB", "fgSysUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgDataSecurityLevel"),
        ("FORTINET-FORTIGATE-MIB", "fgSysNeedLogPartitionScan"),
        ("FORTINET-FORTIGATE-MIB", "fgSysUpTimeDetail"),
        ("FORTINET-FORTIGATE-MIB", "fgSysNpuSesCount"),
        ("FORTINET-FORTIGATE-MIB", "fgSysNpuSesRate1"),
        ("FORTINET-FORTIGATE-MIB", "fgSysNpuSesRate10"),
        ("FORTINET-FORTIGATE-MIB", "fgSysNpuSesRate30"),
        ("FORTINET-FORTIGATE-MIB", "fgSysNpuSesRate60"),
        ("FORTINET-FORTIGATE-MIB", "fgSysNpuSes6Count"),
        ("FORTINET-FORTIGATE-MIB", "fgSysNpuSes6Rate1"),
        ("FORTINET-FORTIGATE-MIB", "fgSysNpuSes6Rate10"),
        ("FORTINET-FORTIGATE-MIB", "fgSysNpuSes6Rate30"),
        ("FORTINET-FORTIGATE-MIB", "fgSysNpuSes6Rate60"),
        ("FORTINET-FORTIGATE-MIB", "fgSysNeedLogPartitionScan"),
        ("FORTINET-FORTIGATE-MIB", "fgSysUpTimeDetail"),
        ("FORTINET-FORTIGATE-MIB", "fgSysRebootReason"),
        ("FORTINET-FORTIGATE-MIB", "fgDataCpuUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgDataMemUsage"))
)
if mibBuilder.loadTexts:
    fgSystemObjectGroup.setStatus("current")

fgSoftwareObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 5)
)
fgSoftwareObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgSysVersionAv"),
        ("FORTINET-FORTIGATE-MIB", "fgSysVersionIps"),
        ("FORTINET-FORTIGATE-MIB", "fgSysVersionAvEt"),
        ("FORTINET-FORTIGATE-MIB", "fgSysVersionIpsEt"))
)
if mibBuilder.loadTexts:
    fgSoftwareObjectGroup.setStatus("current")

fgHwSensorsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 6)
)
fgHwSensorsObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgHwSensorCount"),
        ("FORTINET-FORTIGATE-MIB", "fgHwSensorEntName"),
        ("FORTINET-FORTIGATE-MIB", "fgHwSensorEntValue"),
        ("FORTINET-FORTIGATE-MIB", "fgHwSensorEntAlarmStatus"))
)
if mibBuilder.loadTexts:
    fgHwSensorsObjectGroup.setStatus("current")

fgHighAvailabilityObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 7)
)
fgHighAvailabilityObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgHaSystemMode"),
        ("FORTINET-FORTIGATE-MIB", "fgHaGroupId"),
        ("FORTINET-FORTIGATE-MIB", "fgHaPriority"),
        ("FORTINET-FORTIGATE-MIB", "fgHaOverride"),
        ("FORTINET-FORTIGATE-MIB", "fgHaAutoSync"),
        ("FORTINET-FORTIGATE-MIB", "fgHaSchedule"),
        ("FORTINET-FORTIGATE-MIB", "fgHaGroupName"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsCpuUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsNetUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsSesCount"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsPktCount"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsByteCount"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsIdsCount"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsAvCount"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsHostname"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsSyncStatus"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsSyncDatimeSucc"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsSyncDatimeUnsucc"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsGlobalChecksum"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsPrimarySerial"),
        ("FORTINET-FORTIGATE-MIB", "fgHaStatsAllChecksum"),
        ("FORTINET-FORTIGATE-MIB", "fgHaTrapMemberSerial"))
)
if mibBuilder.loadTexts:
    fgHighAvailabilityObjectGroup.setStatus("current")

fgVpnObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 8)
)
fgVpnObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgVpnDialupGateway"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupLifetime"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupTimeout"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupSrcBegin"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupSrcEnd"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupDstAddr"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupInOctets"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnDialupOutOctets"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntPhase1Name"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntPhase2Name"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntRemGwyIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntRemGwyPort"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntLocGwyIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntLocGwyPort"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntSelectorSrcBeginIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntSelectorSrcEndIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntSelectorSrcPort"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntSelectorDstBeginIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntSelectorDstEndIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntSelectorDstPort"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntSelectorProto"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntLifeSecs"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntLifeBytes"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntTimeout"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntInOctets"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntOutOctets"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntStatus"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunEntVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslState"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslStatsLoginUsers"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslStatsMaxUsers"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslStatsActiveWebSessions"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslStatsMaxWebSessions"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslStatsActiveTunnels"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslStatsMaxTunnels"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelUserName"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelSrcIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelBytesIn"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnSslTunnelBytesOut"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapLocalGateway"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapRemoteGateway"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapPhase1Name"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTunnelUpCount"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupGatewayType"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupGateway"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupLifetime"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupTimeout"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupSrcBeginType"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupSrcBegin"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupSrcEndType"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupSrcEnd"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupDstBeginType"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupDstBegin"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupDstEndType"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupDstEnd"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupInOctets"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupOutOctets"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupPhase1Name"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2DialupVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunPhase1Name"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunPhase2Name"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunRemGwyIpType"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunRemGwyIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunRemGwyPort"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunLocGwyIpType"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunLocGwyIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunLocGwyPort"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunSelSrcBeginIpType"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunSelSrcBeginIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunSelSrcEndIpType"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunSelSrcEndIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunSelDstBeginIpType"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunSelDstBeginIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunSelDstEndIpType"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunSelDstEndIp"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunSelSrcPort"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunSelDstPort"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunSelProto"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunLifeSecs"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunLifeBytes"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunTimeout"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunInOctets"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunOutOctets"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunStatus"),
        ("FORTINET-FORTIGATE-MIB", "fgVpn2TunVdom"))
)
if mibBuilder.loadTexts:
    fgVpnObjectGroup.setStatus("current")

fgFirewallObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 9)
)
fgFirewallObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgFwPolPktCount"),
        ("FORTINET-FORTIGATE-MIB", "fgFwPolByteCount"),
        ("FORTINET-FORTIGATE-MIB", "fgFwUserNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgFwPolPktCountHc"),
        ("FORTINET-FORTIGATE-MIB", "fgFwPolByteCountHc"),
        ("FORTINET-FORTIGATE-MIB", "fgFwUserAuthTimeout"),
        ("FORTINET-FORTIGATE-MIB", "fgFwUserName"),
        ("FORTINET-FORTIGATE-MIB", "fgFwUserAuth"),
        ("FORTINET-FORTIGATE-MIB", "fgFwUserState"),
        ("FORTINET-FORTIGATE-MIB", "fgFwUserVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessProto"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessFromAddr"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessFromPort"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessToAddr"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessToPort"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessExp"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgIpSessNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgIp6SessNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgFwPolLastUsed"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsName"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsType"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsTotalSessions"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsTcpSessions"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsUdpSessions"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsOtherSessions"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsTotalPBAs"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsInusePBAs"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsExpiringPBAs"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsFreePBAs"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsFlags"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsGroupName"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsBlockSize"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsPortStart"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsPortEnd"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsStartClientIP"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsEndClientIP"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsRscTCP"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsRscUDP"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsUsedRscTCP"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsUsedRscUDP"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsPercentageTCP"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsPercentageUDP"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppTrapType"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppTrapPoolProto"),
        ("FORTINET-FORTIGATE-MIB", "fgFwTrapPoolUtilization"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsRequest"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsEchoRequest"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsTunnel"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsTunnelV0"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsPath"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsBearer"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsFteid"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsProfile"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsImsi"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsApn"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsApnShaper"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsTunnelLimiter"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsAdvPolicies"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsIeRemovePolicies"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsIpPolicy"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsNoipPolicy"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsIeWlEntry"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsClash"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpStatsDrop"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCForwarded"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCRejected"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped0"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped1"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped2"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped3"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped4"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped5"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped6"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped7"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped8"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped9"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped10"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped11"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped12"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped13"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped14"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped15"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped16"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped17"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped18"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped19"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped20"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped21"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped22"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsCDropped23"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsDForwarded"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsDDroppedSanity"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsDDroppedMalMsg"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsDDroppedNoState"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsDDroppedMalIe"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsDDroppedGtpInGtp"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsDDroppedSpoof"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsDDroppedIpPol"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsDDroppedMsgFilter"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsDDroppedMsgRateLimit"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsDDroppedUnknownVersion"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsBForwarded"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsBDroppedSanity"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsBDroppedMalMsg"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsBDroppedMalIe"),
        ("FORTINET-FORTIGATE-MIB", "fgFwGtpRtStatsBDroppedMsgFilter"),
        ("FORTINET-FORTIGATE-MIB", "fgFwAddrDynEmsName"),
        ("FORTINET-FORTIGATE-MIB", "fgFwAddrDynEmsAddresses"),
        ("FORTINET-FORTIGATE-MIB", "fgFwAuthIpv4UserNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgFwAuthIpv6UserNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgFwAuthIpv4UserVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgFwAuthIpv4UserName"),
        ("FORTINET-FORTIGATE-MIB", "fgFwAuthIpv4UserType"),
        ("FORTINET-FORTIGATE-MIB", "fgFwAuthIpv4UserAddr"),
        ("FORTINET-FORTIGATE-MIB", "fgFwAuthIpv6UserVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgFwAuthIpv6UserName"),
        ("FORTINET-FORTIGATE-MIB", "fgFwAuthIpv6UserType"),
        ("FORTINET-FORTIGATE-MIB", "fgFwAuthIpv6UserAddr"),
        ("FORTINET-FORTIGATE-MIB", "fgFwHsPolPktCount"),
        ("FORTINET-FORTIGATE-MIB", "fgFwHsPolByteCount"),
        ("FORTINET-FORTIGATE-MIB", "fgFwHsPolLastUsed"))
)
if mibBuilder.loadTexts:
    fgFirewallObjectGroup.setStatus("current")

fgAppServicesObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 10)
)
fgAppServicesObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgApHTTPReqProcessed"),
        ("FORTINET-FORTIGATE-MIB", "fgApSMTPReqProcessed"),
        ("FORTINET-FORTIGATE-MIB", "fgApSMTPSpamDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgApPOP3ReqProcessed"),
        ("FORTINET-FORTIGATE-MIB", "fgApPOP3SpamDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMAPReqProcessed"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMAPSpamDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgApNNTPReqProcessed"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMReqProcessed"),
        ("FORTINET-FORTIGATE-MIB", "fgApSIPUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApSIPMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgApSIPClientReg"),
        ("FORTINET-FORTIGATE-MIB", "fgApSIPCallHandling"),
        ("FORTINET-FORTIGATE-MIB", "fgApSIPServices"),
        ("FORTINET-FORTIGATE-MIB", "fgApSIPOtherReq"),
        ("FORTINET-FORTIGATE-MIB", "fgAppSuNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgAppSuFileScanned"),
        ("FORTINET-FORTIGATE-MIB", "fgAppVoIPConn"),
        ("FORTINET-FORTIGATE-MIB", "fgAppVoIPCallBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAppP2PConnBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAppP2PProtEntBytes"),
        ("FORTINET-FORTIGATE-MIB", "fgAppP2PProtoEntLastReset"),
        ("FORTINET-FORTIGATE-MIB", "fgAppIMMessages"),
        ("FORTINET-FORTIGATE-MIB", "fgAppIMFileTransfered"),
        ("FORTINET-FORTIGATE-MIB", "fgAppIMFileTxBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAppIMConnBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAppFnbamStatsTotalAuthReqs"),
        ("FORTINET-FORTIGATE-MIB", "fgAppFnbamStatsTotalEagainErrs"),
        ("FORTINET-FORTIGATE-MIB", "fgAppFnbamStatsTotalLdapFails"),
        ("FORTINET-FORTIGATE-MIB", "fgApFTPReqProcessed"),
        ("FORTINET-FORTIGATE-MIB", "fgApHTTPConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApFTPConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApSMTPConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApPOP3Connections"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMAPConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApNNTPConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApHTTPMaxConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApFTPMaxConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApSMTPMaxConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApPOP3MaxConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMAPMaxConnections"),
        ("FORTINET-FORTIGATE-MIB", "fgApNNTPMaxConnections"))
)
if mibBuilder.loadTexts:
    fgAppServicesObjectGroup.setStatus("current")

fgAntivirusObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 11)
)
fgAntivirusObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgAvVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvHTTPVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvHTTPVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvSMTPVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvSMTPVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvPOP3VirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvPOP3VirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvIMAPVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvIMAPVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvFTPVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvFTPVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvIMVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvIMVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvNNTPVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvNNTPVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvOversizedDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvOversizedBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvMAPIVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvMAPIVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvSMBVirusDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgAvSMBVirusBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgAvTrapVirName"))
)
if mibBuilder.loadTexts:
    fgAntivirusObjectGroup.setStatus("current")

fgIntrusionPrevtObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 12)
)
fgIntrusionPrevtObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgIpsTrapSigId"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSrcIp"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSigMsg"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsIntrusionsDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsIntrusionsBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsCritSevDetections"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsHighSevDetections"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsMedSevDetections"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsLowSevDetections"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsInfoSevDetections"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsSignatureDetections"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsAnomalyDetections"))
)
if mibBuilder.loadTexts:
    fgIntrusionPrevtObjectGroup.setStatus("current")

fgWebFilterObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 13)
)
fgWebFilterObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgWfHTTPBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgWfHTTPSBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgWfHTTPURLBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgWfHTTPSURLBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgWfActiveXBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgWfCookieBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgWfAppletBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPExamined"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPSExamined"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPAllowed"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPSAllowed"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPSBlocked"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPLogged"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPSLogged"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPOverridden"),
        ("FORTINET-FORTIGATE-MIB", "fgFgWfHTTPSOverridden"))
)
if mibBuilder.loadTexts:
    fgWebFilterObjectGroup.setStatus("current")

fgVirtualDomainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 14)
)
fgVirtualDomainObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgVdNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgVdMaxVdoms"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEnabled"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntName"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntOpMode"),
        ("FORTINET-FORTIGATE-MIB", "fgVdTpMgmtAddrType"),
        ("FORTINET-FORTIGATE-MIB", "fgVdTpMgmtAddr"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntCpuUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntSesCount"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntSesRate"),
        ("FORTINET-FORTIGATE-MIB", "fgVdTpMgmtMask"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntHaState"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntChecksum"))
)
if mibBuilder.loadTexts:
    fgVirtualDomainObjectGroup.setStatus("current")

fgAdministrationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 15)
)
fgAdministrationObjectGroup.setObjects(
    ("FORTINET-FORTIGATE-MIB", "fgAdminVdom")
)
if mibBuilder.loadTexts:
    fgAdministrationObjectGroup.setStatus("current")

fgIntfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 16)
)
fgIntfObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgIntfEntVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfEntEstUpBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfEntEstDownBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfEntMeaUpBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfEntMeaDownBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVlanName"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVlanID"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVlanPhyName"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVrrpCount"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVrrpEntVrId"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVrrpEntGrpId"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVrrpEntIfName"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVrrpEntState"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVrrpEntVrIp"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVlanHbCount"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVlanHbEntIfName"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVlanHbEntSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfVlanHbEntState"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgIfName"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgIfEgressSProfile"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgIfIngressSProfile"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgIfEstUpBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgIfEstDownBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgIfInBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgIfOutBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSproName"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSproType"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSproDefaultClassId"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSproClassNum"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSentClassName"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSentGuaranteedBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSentMaxBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSpolSrcaddr"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSpolDstaddr"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSpolSvr"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSpolComment"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCfgSpolClassName"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcAllocatedBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcGuaranteedBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcMaxBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcCurrentBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcBytes"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcDrops"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcInAllocatedBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcInGuaranteedBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcInMaxBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcInCurrentBandwidth"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcInBytes"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcInDrops"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcQPackets"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcQBytes"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcQPDrops"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfBcQBDrops"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfTrapType"))
)
if mibBuilder.loadTexts:
    fgIntfObjectGroup.setStatus("current")

fgProcessorsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 17)
)
fgProcessorsObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgProcessorCount"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorUsage5sec"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorType"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorContainedIn"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorPktRxCount"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorPktTxCount"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorPktDroppedCount"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorUserUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorSysUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorPktTxDroppedCount"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorModuleCount"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModType"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModName"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModDescr"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModProcessorCount"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModMemCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgPerCpuHighDetails"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModSessionCount"),
        ("FORTINET-FORTIGATE-MIB", "fgProcModSACount"))
)
if mibBuilder.loadTexts:
    fgProcessorsObjectGroup.setStatus("current")

fgExplicitProxyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 20)
)
fgExplicitProxyObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgExplicitProxyUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyRequests"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyUsers"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxySessions"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyVirus"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyBannedWords"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyPolicy"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyOversized"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyArchNest"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyArchSize"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyArchEncrypted"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyArchMultiPart"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyArchUnsupported"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyArchBomb"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyArchCorrupt"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyFilteredApplets"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyFilteredActiveX"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyFilteredJScript"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyFilteredJS"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyFilteredVBS"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyFilteredOthScript"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyBlockedDLP"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyBlockedConType"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyExaminedURLs"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyAllowedURLs"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyBlockedURLs"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyLoggedURLs"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyOverriddenURLs"))
)
if mibBuilder.loadTexts:
    fgExplicitProxyObjectGroup.setStatus("current")

fgWebCacheObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 21)
)
fgWebCacheObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgWebCacheUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheRAMLimit"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheRAMUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheRAMHits"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheRAMMisses"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheRequests"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheBypass"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheDiskLimit"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheDiskUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheDiskHits"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheDiskMisses"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheDiskFailure"))
)
if mibBuilder.loadTexts:
    fgWebCacheObjectGroup.setStatus("current")

fgWanOptObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 22)
)
fgWanOptObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgMemCacheLimit"),
        ("FORTINET-FORTIGATE-MIB", "fgMemCacheUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgMemCacheHits"),
        ("FORTINET-FORTIGATE-MIB", "fgMemCacheMisses"),
        ("FORTINET-FORTIGATE-MIB", "fgByteCacheRAMLimit"),
        ("FORTINET-FORTIGATE-MIB", "fgByteCacheRAMUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptReductionRate"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptLanTraffic"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptWanTraffic"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptLanInTraffic"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptLanOutTraffic"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptWanInTraffic"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptWanOutTraffic"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptTunnels"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptLANBytesIn"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptLANBytesOut"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptWANBytesIn"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptWANBytesOut"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptDiskLimit"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptDiskUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptDiskHits"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptDiskMisses"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptDiskFailure"))
)
if mibBuilder.loadTexts:
    fgWanOptObjectGroup.setStatus("current")

fgObsoleteAppServicesObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 23)
)
fgObsoleteAppServicesObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgApHTTPUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApHTTPMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgApSMTPUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApSMTPMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgApPOP3UpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApPOP3MemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMAPUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApIMAPMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgApNNTPUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApNNTPMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgApFTPUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgApFTPMemUsage"))
)
if mibBuilder.loadTexts:
    fgObsoleteAppServicesObjectGroup.setStatus("deprecated")

fgSystemAdvancedObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 24)
)
fgSystemAdvancedObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgSIAdvMemPageCache"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvMemCacheActive"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvMemCacheInactive"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvMemBuffer"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvMemEnterKerConsThrsh"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvMemLeaveKerConsThrsh"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvMemEnterProxyConsThrsh"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvMemLeaveProxyConsThrsh"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvSesEphemeralCount"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvSesEphemeralLimit"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvSesClashCount"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvSesExpCount"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvSesSyncQFCount"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvSesAcceptQFCount"),
        ("FORTINET-FORTIGATE-MIB", "fgSIAdvSesNoListenerCount"),
        ("FORTINET-FORTIGATE-MIB", "fgLicContractCount"),
        ("FORTINET-FORTIGATE-MIB", "fgLicVersionCount"),
        ("FORTINET-FORTIGATE-MIB", "fgLicContractDesc"),
        ("FORTINET-FORTIGATE-MIB", "fgLicContractExpiry"),
        ("FORTINET-FORTIGATE-MIB", "fgLicVersionDesc"),
        ("FORTINET-FORTIGATE-MIB", "fgLicVersionExpiry"),
        ("FORTINET-FORTIGATE-MIB", "fgLicVersionNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgLicVersionUpdTime"),
        ("FORTINET-FORTIGATE-MIB", "fgLicVersionUpdMethod"),
        ("FORTINET-FORTIGATE-MIB", "fgLicVersionTryTime"),
        ("FORTINET-FORTIGATE-MIB", "fgLicVersionTryResult"),
        ("FORTINET-FORTIGATE-MIB", "fgLicAlContractCount"),
        ("FORTINET-FORTIGATE-MIB", "fgLicAlContractDesc"),
        ("FORTINET-FORTIGATE-MIB", "fgLicAlContractExpiry"))
)
if mibBuilder.loadTexts:
    fgSystemAdvancedObjectGroup.setStatus("current")

fgWcObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 25)
)
fgWcObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgWcApVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApName"),
        ("FORTINET-FORTIGATE-MIB", "fgWcInfoName"),
        ("FORTINET-FORTIGATE-MIB", "fgWcInfoLocation"),
        ("FORTINET-FORTIGATE-MIB", "fgWcInfoWtpCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgWcInfoWtpManaged"),
        ("FORTINET-FORTIGATE-MIB", "fgWcInfoWtpSessions"),
        ("FORTINET-FORTIGATE-MIB", "fgWcInfoStationCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgWcInfoStationCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanSsid"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanBroadcastSsid"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanSecurity"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanEncryption"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanAuthentication"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanRadiusServer"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanUserGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanLocalBridging"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanVlanId"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanMeshBackhaul"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanStationCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanStationCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWlanCPAuth"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfilePlatform"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileDataChannelDtlsPolicy"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileCountryString"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioMode"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioApScan"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioWidsProfile"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioDarrp"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioFrequencyHandoff"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioApHandoff"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioBeaconInterval"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioDtimPeriod"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioBand"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioChannelBonding"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioChannel"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioAutoTxPowerControl"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioAutoTxPowerLow"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioAutoTxPowerHigh"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioTxPowerLevel"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioVaps"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioStationCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpProfileRadioChannelWidth"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigWtpAdmin"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigWtpName"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigWtpLocation"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigWtpProfile"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigRadioEnable"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigRadioAutoTxPowerControl"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigRadioAutoTxPowerLow"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigRadioAutoTxPowerHigh"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigRadioTxPowerLevel"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigRadioBand"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigRadioApScan"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigVapAll"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpConfigVaps"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpIpAddressType"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpIpAddress"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpLocalIpAddressType"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpLocalIpAddress"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpBaseMacAddress"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionConnectionState"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpDaemonUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpSessionUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpProfileName"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpModelNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpHwVersion"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpSwVersion"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpBootVersion"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpRegionCode"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpStationCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpByteRxCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpByteTxCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpCpuUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpMemoryUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionWtpMemoryCapacity"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioMode"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioBaseBssid"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioCountryString"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioCountryCode"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioOperatingChannel"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioOperatingPower"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionRadioStationCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionVapSsid"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionVapStationCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionVapByteRxCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcWtpSessionVapByteTxCount"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaWlan"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaWtpId"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaRadioId"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaVlanId"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaIpAddressType"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaIpAddress"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaVci"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaHost"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaUser"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaSignal"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaNoise"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaIdle"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaBandwidthTx"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaBandwidthRx"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaChannel"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaRadioType"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaSecurity"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaEncrypt"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaOnline"),
        ("FORTINET-FORTIGATE-MIB", "fgWcStaCPAuth"))
)
if mibBuilder.loadTexts:
    fgWcObjectGroup.setStatus("current")

fgFcObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 26)
)
fgFcObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgFcSwVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwName"))
)
if mibBuilder.loadTexts:
    fgFcObjectGroup.setStatus("current")

fgServerLoadBalanceObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 27)
)
fgServerLoadBalanceObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgServerLoadBalanceRealServerAddress"),
        ("FORTINET-FORTIGATE-MIB", "fgServerLoadBalanceVirtualServerName"),
        ("FORTINET-FORTIGATE-MIB", "fgServerLoadBalanceRealServerAddress6"))
)
if mibBuilder.loadTexts:
    fgServerLoadBalanceObjectGroup.setStatus("current")

fgUsbportsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 28)
)
fgUsbportsObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgUsbportCount"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportPlugged"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportVersion"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportClass"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportVendId"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportProdId"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportRevision"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportManufacturer"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportProduct"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportSerial"))
)
if mibBuilder.loadTexts:
    fgUsbportsObjectGroup.setStatus("current")

fgUsbModemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 29)
)
fgUsbModemInfoGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgUsbModemSignalStrength"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbModemStatus"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbModemSimState"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbModemVendor"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbModemProduct"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbModemNetwork"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbModemId"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbModemSimId"))
)
if mibBuilder.loadTexts:
    fgUsbModemInfoGroup.setStatus("current")

fgDeviceObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 30)
)
fgDeviceObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgDeviceMacAddress"),
        ("FORTINET-FORTIGATE-MIB", "fgDeviceCreated"),
        ("FORTINET-FORTIGATE-MIB", "fgDeviceLastSeen"))
)
if mibBuilder.loadTexts:
    fgDeviceObjectGroup.setStatus("current")

fgLinkMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 31)
)
fgLinkMonitorGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgLinkMonitorNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorName"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorState"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorLatency"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorJitter"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorPacketSend"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorPacketRecv"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorPacketLoss"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorBandwidthIn"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorBandwidthOut"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorBandwidthBi"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorOutofSeq"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorServer"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorProtocol"))
)
if mibBuilder.loadTexts:
    fgLinkMonitorGroup.setStatus("current")

fgInternalModemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 32)
)
fgInternalModemInfoGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgMdmDetected"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmVendor"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmModel"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmRevision"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmMsisdn"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmEsn"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmImei"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmHwRevision"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmMeid"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmSwRev"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmSku"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmFsn"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmPrlVer"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmFwVer"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmPriFwVer"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmCarrierAbbr"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmActState"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmOpMode"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmLacTac"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmActBand"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmCellId"),
        ("FORTINET-FORTIGATE-MIB", "fgMdmRssi"))
)
if mibBuilder.loadTexts:
    fgInternalModemInfoGroup.setStatus("current")

fgInternalModemSIMInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 33)
)
fgInternalModemSIMInfoGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgSimMdmEntIndex"),
        ("FORTINET-FORTIGATE-MIB", "fgSimState"),
        ("FORTINET-FORTIGATE-MIB", "fgSimIccid"),
        ("FORTINET-FORTIGATE-MIB", "fgSimImsi"),
        ("FORTINET-FORTIGATE-MIB", "fgSimCountry"),
        ("FORTINET-FORTIGATE-MIB", "fgSimNetwork"))
)
if mibBuilder.loadTexts:
    fgInternalModemSIMInfoGroup.setStatus("current")

fgInternalModemSigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 34)
)
fgInternalModemSigInfoGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgCdmaRssi"),
        ("FORTINET-FORTIGATE-MIB", "fgCdmaEcio"),
        ("FORTINET-FORTIGATE-MIB", "fgHdrRssi"),
        ("FORTINET-FORTIGATE-MIB", "fgHdrEcio"),
        ("FORTINET-FORTIGATE-MIB", "fgHdrSinr"),
        ("FORTINET-FORTIGATE-MIB", "fgHdrIo"),
        ("FORTINET-FORTIGATE-MIB", "fgGsm"),
        ("FORTINET-FORTIGATE-MIB", "fgWcdmaRssi"),
        ("FORTINET-FORTIGATE-MIB", "fgWcdmaEcio"),
        ("FORTINET-FORTIGATE-MIB", "fgLteRssi"),
        ("FORTINET-FORTIGATE-MIB", "fgLteRsrq"),
        ("FORTINET-FORTIGATE-MIB", "fgLteRsrp"),
        ("FORTINET-FORTIGATE-MIB", "fgLteSnr"),
        ("FORTINET-FORTIGATE-MIB", "fgTdma"))
)
if mibBuilder.loadTexts:
    fgInternalModemSigInfoGroup.setStatus("current")

fgInternalModemTrafficInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 35)
)
fgInternalModemTrafficInfoGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgTxPacksOK"),
        ("FORTINET-FORTIGATE-MIB", "fgRxPacksOK"),
        ("FORTINET-FORTIGATE-MIB", "fgTxPacksErr"),
        ("FORTINET-FORTIGATE-MIB", "fgRxPacksErr"),
        ("FORTINET-FORTIGATE-MIB", "fgTxPacksOverflow"),
        ("FORTINET-FORTIGATE-MIB", "fgRxPacksOverflow"),
        ("FORTINET-FORTIGATE-MIB", "fgTxBytesOK"),
        ("FORTINET-FORTIGATE-MIB", "fgRxBytesOK"),
        ("FORTINET-FORTIGATE-MIB", "fgLastCallTxBytesOK"),
        ("FORTINET-FORTIGATE-MIB", "fgLastCallRxBytesOK"),
        ("FORTINET-FORTIGATE-MIB", "fgTxPacksDrop"),
        ("FORTINET-FORTIGATE-MIB", "fgRxPacksDrop"))
)
if mibBuilder.loadTexts:
    fgInternalModemTrafficInfoGroup.setStatus("current")

fgInternalModemSessInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 36)
)
fgInternalModemSessInfoGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgSessMdmEntIndex"),
        ("FORTINET-FORTIGATE-MIB", "fdLteIfName"),
        ("FORTINET-FORTIGATE-MIB", "fdLteSessConnStat"),
        ("FORTINET-FORTIGATE-MIB", "fdLteProfId"),
        ("FORTINET-FORTIGATE-MIB", "fdLteProfName"),
        ("FORTINET-FORTIGATE-MIB", "fdLteProfType"),
        ("FORTINET-FORTIGATE-MIB", "fdLtePdpType"),
        ("FORTINET-FORTIGATE-MIB", "fdLteProfApn"),
        ("FORTINET-FORTIGATE-MIB", "fdLteProfIpFamily"),
        ("FORTINET-FORTIGATE-MIB", "fdLteIpv4Addr"),
        ("FORTINET-FORTIGATE-MIB", "fdLteIpv4GwAddr"),
        ("FORTINET-FORTIGATE-MIB", "fdLteIpv4NetMask"),
        ("FORTINET-FORTIGATE-MIB", "fdLteIpv4PriDns"),
        ("FORTINET-FORTIGATE-MIB", "fdLteIpv4SecDns"),
        ("FORTINET-FORTIGATE-MIB", "fdLteIpv6Addr"),
        ("FORTINET-FORTIGATE-MIB", "fdLteIpv6PrefLen"),
        ("FORTINET-FORTIGATE-MIB", "fdLteIpv6GwAddr"),
        ("FORTINET-FORTIGATE-MIB", "fdLteIpv6GwPrefLen"),
        ("FORTINET-FORTIGATE-MIB", "fdLteIpv6PriDns"),
        ("FORTINET-FORTIGATE-MIB", "fdLteIpv6SecDns"),
        ("FORTINET-FORTIGATE-MIB", "fdLteMtu"),
        ("FORTINET-FORTIGATE-MIB", "fdLteAutoConn"),
        ("FORTINET-FORTIGATE-MIB", "fdLteNetType"),
        ("FORTINET-FORTIGATE-MIB", "fdLteNetTypeLas"),
        ("FORTINET-FORTIGATE-MIB", "fdLteLinkProto"))
)
if mibBuilder.loadTexts:
    fgInternalModemSessInfoGroup.setStatus("current")

fgInternalModemGpsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 37)
)
fgInternalModemGpsInfoGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgGpsEnabled"),
        ("FORTINET-FORTIGATE-MIB", "fgLatitude"),
        ("FORTINET-FORTIGATE-MIB", "fgLongitude"),
        ("FORTINET-FORTIGATE-MIB", "fgUtcTime"),
        ("FORTINET-FORTIGATE-MIB", "fgLocalTime"))
)
if mibBuilder.loadTexts:
    fgInternalModemGpsInfoGroup.setStatus("current")

fgInternalModemDatausageInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 38)
)
fgInternalModemDatausageInfoGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgDatausageEnabled"),
        ("FORTINET-FORTIGATE-MIB", "fgDataOut"),
        ("FORTINET-FORTIGATE-MIB", "fgDataIn"))
)
if mibBuilder.loadTexts:
    fgInternalModemDatausageInfoGroup.setStatus("current")

fgVWLHealthCheckLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 39)
)
fgVWLHealthCheckLinkGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkName"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkSeq"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkState"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkLatency"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkJitter"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkPacketSend"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkPacketRecv"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkPacketLoss"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkBandwidthIn"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkBandwidthOut"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkBandwidthBi"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkIfName"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkUsedBandwidthIn"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkUsedBandwidthOut"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkUsedBandwidthBi"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkMOSCodec"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkMOS"))
)
if mibBuilder.loadTexts:
    fgVWLHealthCheckLinkGroup.setStatus("current")

fgDisksObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 40)
)
fgDisksObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgDiskCount"),
        ("FORTINET-FORTIGATE-MIB", "fgDiskName"),
        ("FORTINET-FORTIGATE-MIB", "fgDiskFsMountName"),
        ("FORTINET-FORTIGATE-MIB", "fgDiskFsMountMountPoint"),
        ("FORTINET-FORTIGATE-MIB", "fgDiskFsMountType"),
        ("FORTINET-FORTIGATE-MIB", "fgDiskFsMountOptions"),
        ("FORTINET-FORTIGATE-MIB", "fgDiskFsMountFreq"),
        ("FORTINET-FORTIGATE-MIB", "fgDiskFsMountPassNo"),
        ("FORTINET-FORTIGATE-MIB", "fgDiskFsMountOptionsVal"),
        ("FORTINET-FORTIGATE-MIB", "fgDiskPartitionsMajor"),
        ("FORTINET-FORTIGATE-MIB", "fgDiskPartitionsMinor"),
        ("FORTINET-FORTIGATE-MIB", "fgDiskPartitionsBlockNum"),
        ("FORTINET-FORTIGATE-MIB", "fgDiskPartitionsName"))
)
if mibBuilder.loadTexts:
    fgDisksObjectGroup.setStatus("current")

fgNPUGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 41)
)
fgNPUGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgNPUNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgNPUName"),
        ("FORTINET-FORTIGATE-MIB", "fgNPUDrvDriftSum"),
        ("FORTINET-FORTIGATE-MIB", "fgNPUSessionTblSize"),
        ("FORTINET-FORTIGATE-MIB", "fgNPUSessionCount"),
        ("FORTINET-FORTIGATE-MIB", "fgNPUDrvDrift"))
)
if mibBuilder.loadTexts:
    fgNPUGroup.setStatus("current")

fgSlaProbeClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 42)
)
fgSlaProbeClientGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientIP"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientState"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientAvgLatency"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientAvgLatencySD"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientAvgLatencyDS"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientMinLatency"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientMinLatencySD"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientMinLatencyDS"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientMaxLatency"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientMaxLatencySD"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientMaxLatencyDS"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientAvgJitter"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientAvgJitterSD"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientAvgJitterDS"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientMinJitter"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientMinJitterSD"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientMinJitterDS"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientMaxJitter"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientMaxJitterSD"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientMaxJitterDS"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientPktloss"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientPktlossSD"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientPktlossDS"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientOutofSeq"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientOutofSeqSD"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientOutofSeqDS"))
)
if mibBuilder.loadTexts:
    fgSlaProbeClientGroup.setStatus("current")

fgDNSProxyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 43)
)
fgDNSProxyObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgDNSProxyStatsUdpCacheHit"),
        ("FORTINET-FORTIGATE-MIB", "fgDNSProxyStatsUdpRatingCacheHit"),
        ("FORTINET-FORTIGATE-MIB", "fgDNSProxyStatsUdpReq"),
        ("FORTINET-FORTIGATE-MIB", "fgDNSProxyStatsUdpRes"),
        ("FORTINET-FORTIGATE-MIB", "fgDNSProxyStatsUdpFwd"),
        ("FORTINET-FORTIGATE-MIB", "fgDNSProxyStatsUdpRetrans"),
        ("FORTINET-FORTIGATE-MIB", "fgDNSProxyStatsUdpTo"),
        ("FORTINET-FORTIGATE-MIB", "fgDNSProxyStatsUdpFtgRes"),
        ("FORTINET-FORTIGATE-MIB", "fgDNSProxyStatsUdpFtgFwd"),
        ("FORTINET-FORTIGATE-MIB", "fgDNSProxyStatsUdpFtgRetrans"))
)
if mibBuilder.loadTexts:
    fgDNSProxyObjectGroup.setStatus("current")

fgLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 44)
)
fgLogGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgLogDeviceNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgLogDeviceName"),
        ("FORTINET-FORTIGATE-MIB", "fgLogDeviceSentCount"),
        ("FORTINET-FORTIGATE-MIB", "fgLogDeviceRelayedCount"),
        ("FORTINET-FORTIGATE-MIB", "fgLogDeviceCachedCount"),
        ("FORTINET-FORTIGATE-MIB", "fgLogDeviceFailedCount"),
        ("FORTINET-FORTIGATE-MIB", "fgLogDeviceDroppedCount"))
)
if mibBuilder.loadTexts:
    fgLogGroup.setStatus("current")

fgConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 45)
)
fgConfigGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgConfigSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgConfigChecksum"),
        ("FORTINET-FORTIGATE-MIB", "fgConfigLastChangeTime"))
)
if mibBuilder.loadTexts:
    fgConfigGroup.setStatus("current")

fgDhcpObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 46)
)
fgDhcpObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgDhcpServerNumber"),
        ("FORTINET-FORTIGATE-MIB", "fgDhcpLeaseUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgDhcpServerId"),
        ("FORTINET-FORTIGATE-MIB", "fgDhcpTrapType"),
        ("FORTINET-FORTIGATE-MIB", "fgDhcpTrapMessage"))
)
if mibBuilder.loadTexts:
    fgDhcpObjectGroup.setStatus("current")

fgDpdkEngsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 47)
)
fgDpdkEngsObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgDpdkEngCount"),
        ("FORTINET-FORTIGATE-MIB", "fgDpdkEngRxUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgDpdkEngVnpUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgDpdkEngIpsUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgDpdkEngTxUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgDpdkEngIdle"),
        ("FORTINET-FORTIGATE-MIB", "fgDpdkEngToCpu"))
)
if mibBuilder.loadTexts:
    fgDpdkEngsObjectGroup.setStatus("current")

fgSwitchDeviceObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 48)
)
fgSwitchDeviceObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgSwDeviceSerialNum"),
        ("FORTINET-FORTIGATE-MIB", "fgSwDeviceName"),
        ("FORTINET-FORTIGATE-MIB", "fgSwDeviceVersion"),
        ("FORTINET-FORTIGATE-MIB", "fgSwDeviceAuthorized"),
        ("FORTINET-FORTIGATE-MIB", "fgSwDeviceStatus"),
        ("FORTINET-FORTIGATE-MIB", "fgSwDeviceJoinTime"),
        ("FORTINET-FORTIGATE-MIB", "fgSwDeviceIp"),
        ("FORTINET-FORTIGATE-MIB", "fgSwDeviceFlag"),
        ("FORTINET-FORTIGATE-MIB", "fgSwCpu"),
        ("FORTINET-FORTIGATE-MIB", "fgSwMemory"),
        ("FORTINET-FORTIGATE-MIB", "fgSwDeviceIpv6"))
)
if mibBuilder.loadTexts:
    fgSwitchDeviceObjectGroup.setStatus("current")

fgSwitchPortObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 49)
)
fgSwitchPortObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgSwPortSwitchSerialNum"),
        ("FORTINET-FORTIGATE-MIB", "fgSwPortName"),
        ("FORTINET-FORTIGATE-MIB", "fgSwPortStatus"),
        ("FORTINET-FORTIGATE-MIB", "fgSwPortSpeedDuplex"),
        ("FORTINET-FORTIGATE-MIB", "fgSwPortNativeVlan"),
        ("FORTINET-FORTIGATE-MIB", "fgSwPortAllowedVlan"),
        ("FORTINET-FORTIGATE-MIB", "fgSwPortUntaggedVlan"),
        ("FORTINET-FORTIGATE-MIB", "fgSwPortPOE"),
        ("FORTINET-FORTIGATE-MIB", "fgSwPortPOEStatus"),
        ("FORTINET-FORTIGATE-MIB", "fgSwPortPOEState"),
        ("FORTINET-FORTIGATE-MIB", "fgSwPortPOEPower"))
)
if mibBuilder.loadTexts:
    fgSwitchPortObjectGroup.setStatus("current")

fgChassisObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 50)
)
fgChassisObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgChassisVersion"),
        ("FORTINET-FORTIGATE-MIB", "fgChassisSlotId"),
        ("FORTINET-FORTIGATE-MIB", "fgChassisTrapMessage"))
)
if mibBuilder.loadTexts:
    fgChassisObjectGroup.setStatus("current")

fgServiceGroupWorkerBladesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 51)
)
fgServiceGroupWorkerBladesGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgSgWbServiceGroupID"),
        ("FORTINET-FORTIGATE-MIB", "fgSgWbChassisID"),
        ("FORTINET-FORTIGATE-MIB", "fgSgWbSlotID"),
        ("FORTINET-FORTIGATE-MIB", "fgSgWbState"),
        ("FORTINET-FORTIGATE-MIB", "fgSgWbStatusMsg"),
        ("FORTINET-FORTIGATE-MIB", "fgSgWbMaster"),
        ("FORTINET-FORTIGATE-MIB", "fgSgWbSysVersion"),
        ("FORTINET-FORTIGATE-MIB", "fgSgWbSysSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgSgWbSysUpTime"),
        ("FORTINET-FORTIGATE-MIB", "fgSgWbSysCpuUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgSgWbSysMemUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgSgWbBaseLink"),
        ("FORTINET-FORTIGATE-MIB", "fgSgWbFabricLink"),
        ("FORTINET-FORTIGATE-MIB", "fgSgWbDataHb"),
        ("FORTINET-FORTIGATE-MIB", "fgSgWbMgmtHb"))
)
if mibBuilder.loadTexts:
    fgServiceGroupWorkerBladesGroup.setStatus("current")

fgEmsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 52)
)
fgEmsObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgEmsGlobalEntStatus"),
        ("FORTINET-FORTIGATE-MIB", "fgEmsGlobalEntConnectionName"),
        ("FORTINET-FORTIGATE-MIB", "fgEmsGlobalEntConnectionStatus"),
        ("FORTINET-FORTIGATE-MIB", "fgEmsGlobalEntLastCloseReason"),
        ("FORTINET-FORTIGATE-MIB", "fgEmsGlobalEntLastCloseReasonDesc"),
        ("FORTINET-FORTIGATE-MIB", "fgEmsGlobalEntLastCloseTime"),
        ("FORTINET-FORTIGATE-MIB", "fgEmsVdEntStatus"),
        ("FORTINET-FORTIGATE-MIB", "fgEmsVdEntConnectionName"),
        ("FORTINET-FORTIGATE-MIB", "fgEmsVdEntConnectionStatus"),
        ("FORTINET-FORTIGATE-MIB", "fgEmsVdEntLastCloseReason"),
        ("FORTINET-FORTIGATE-MIB", "fgEmsVdEntLastCloseReasonDesc"),
        ("FORTINET-FORTIGATE-MIB", "fgEmsVdEntLastCloseTime"))
)
if mibBuilder.loadTexts:
    fgEmsObjectGroup.setStatus("current")

fgDioObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 53)
)
fgDioObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgDioEntName"),
        ("FORTINET-FORTIGATE-MIB", "fgDioEntStatusMsg"),
        ("FORTINET-FORTIGATE-MIB", "fgDioTrapType"))
)
if mibBuilder.loadTexts:
    fgDioObjectGroup.setStatus("current")

fgInternal5GModemsInfoObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 54)
)
fgInternal5GModemsInfoObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fg5gModemNumber"),
        ("FORTINET-FORTIGATE-MIB", "fg5gMdmDetected"),
        ("FORTINET-FORTIGATE-MIB", "fg5gMdmVendor"),
        ("FORTINET-FORTIGATE-MIB", "fg5gMdmModel"),
        ("FORTINET-FORTIGATE-MIB", "fg5gMdmRevision"),
        ("FORTINET-FORTIGATE-MIB", "fg5gMdmImei"),
        ("FORTINET-FORTIGATE-MIB", "fg5gMdmHwRevision"),
        ("FORTINET-FORTIGATE-MIB", "fg5gMdmMeid"),
        ("FORTINET-FORTIGATE-MIB", "fg5gMdmSwRev"),
        ("FORTINET-FORTIGATE-MIB", "fg5gMdmPriFwVer"),
        ("FORTINET-FORTIGATE-MIB", "fg5gMdmFwName"),
        ("FORTINET-FORTIGATE-MIB", "fg5gMdmOpMode"),
        ("FORTINET-FORTIGATE-MIB", "fg5gMdmTemperature"),
        ("FORTINET-FORTIGATE-MIB", "fg5gNetworkMode"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIdleSimState"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIdleSimIccid"),
        ("FORTINET-FORTIGATE-MIB", "fg5gActiveSimState"),
        ("FORTINET-FORTIGATE-MIB", "fg5gActiveSimIccid"),
        ("FORTINET-FORTIGATE-MIB", "fg5gActiveSimMsisdn"),
        ("FORTINET-FORTIGATE-MIB", "fg5gActiveSimImsi"),
        ("FORTINET-FORTIGATE-MIB", "fg5gActiveSimCountry"),
        ("FORTINET-FORTIGATE-MIB", "fg5gActiveSimNetwork"),
        ("FORTINET-FORTIGATE-MIB", "fg5gActiveSimPinState"),
        ("FORTINET-FORTIGATE-MIB", "fg5gSigWcdmaRssi"),
        ("FORTINET-FORTIGATE-MIB", "fg5gSigWcdmaEcio"),
        ("FORTINET-FORTIGATE-MIB", "fg5gSigLteRssi"),
        ("FORTINET-FORTIGATE-MIB", "fg5gSigLteRsrq"),
        ("FORTINET-FORTIGATE-MIB", "fg5gSigLteRsrp"),
        ("FORTINET-FORTIGATE-MIB", "fg5gSigLteSnr"),
        ("FORTINET-FORTIGATE-MIB", "fg5gSig5gRsrp"),
        ("FORTINET-FORTIGATE-MIB", "fg5gSig5gSnr"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4TxPacksOK"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4RxPacksOK"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4TxPacksErr"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4RxPacksErr"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4TxPacksOverflow"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4RxPacksOverflow"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4TxBytesOK"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4RxBytesOK"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4TxPacksDrop"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4RxPacksDrop"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6TxPacksOK"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6RxPacksOK"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6TxPacksErr"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6RxPacksErr"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6TxPacksOverflow"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6RxPacksOverflow"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6TxBytesOK"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6RxBytesOK"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6TxPacksDrop"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6RxPacksDrop"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIfName"),
        ("FORTINET-FORTIGATE-MIB", "fg5gMtu"),
        ("FORTINET-FORTIGATE-MIB", "fg5gProfId"),
        ("FORTINET-FORTIGATE-MIB", "fg5gProfName"),
        ("FORTINET-FORTIGATE-MIB", "fg5gPdpType"),
        ("FORTINET-FORTIGATE-MIB", "fg5gProfApn"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4SessionStatus"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4Addr"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4GwAddr"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4NetMask"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4PriDns"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv4SecDns"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6SessionStatus"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6Addr"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6PrefLen"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6GwAddr"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6GwPrefLen"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6PriDns"),
        ("FORTINET-FORTIGATE-MIB", "fg5gIpv6SecDns"),
        ("FORTINET-FORTIGATE-MIB", "fg5gGpsEnabled"),
        ("FORTINET-FORTIGATE-MIB", "fg5gLatitude"),
        ("FORTINET-FORTIGATE-MIB", "fg5gLongitude"),
        ("FORTINET-FORTIGATE-MIB", "fg5gUtcTime"),
        ("FORTINET-FORTIGATE-MIB", "fg5gLocalTime"))
)
if mibBuilder.loadTexts:
    fgInternal5GModemsInfoObjectGroup.setStatus("current")

fgChassisSensorsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 55)
)
fgChassisSensorsObjectGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgChassisSensorCount"),
        ("FORTINET-FORTIGATE-MIB", "fgChassisSensorEntName"),
        ("FORTINET-FORTIGATE-MIB", "fgChassisSensorEntValue"),
        ("FORTINET-FORTIGATE-MIB", "fgChassisSensorEntAlarmStatus"))
)
if mibBuilder.loadTexts:
    fgChassisSensorsObjectGroup.setStatus("current")


# Notification objects

fgTrapVpnTunUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 301)
)
fgTrapVpnTunUp.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapLocalGateway"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapRemoteGateway"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapPhase1Name"))
)
if mibBuilder.loadTexts:
    fgTrapVpnTunUp.setStatus(
        "current"
    )

fgTrapVpnTunDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 302)
)
fgTrapVpnTunDown.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapLocalGateway"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapRemoteGateway"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnTrapPhase1Name"))
)
if mibBuilder.loadTexts:
    fgTrapVpnTunDown.setStatus(
        "current"
    )

fgTrapHaSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 401)
)
fgTrapHaSwitch.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapHaSwitch.setStatus(
        "current"
    )

fgTrapHaStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 402)
)
fgTrapHaStateChange.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgTrapHaStateChange.setStatus(
        "deprecated"
    )

fgTrapHaHBFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 403)
)
fgTrapHaHBFail.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgTrapHaHBFail.setStatus(
        "current"
    )

fgTrapHaMemberDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 404)
)
fgTrapHaMemberDown.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgTrapHaMemberDown.setStatus(
        "current"
    )

fgTrapHaMemberUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 405)
)
fgTrapHaMemberUp.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgTrapHaMemberUp.setStatus(
        "current"
    )

fgTrapIpsSignature = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 503)
)
fgTrapIpsSignature.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSigId"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSrcIp"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSigMsg"))
)
if mibBuilder.loadTexts:
    fgTrapIpsSignature.setStatus(
        "current"
    )

fgTrapIpsAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 504)
)
fgTrapIpsAnomaly.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSigId"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSrcIp"),
        ("FORTINET-FORTIGATE-MIB", "fgIpsTrapSigMsg"))
)
if mibBuilder.loadTexts:
    fgTrapIpsAnomaly.setStatus(
        "current"
    )

fgTrapIpsPkgUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 505)
)
fgTrapIpsPkgUpdate.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapIpsPkgUpdate.setStatus(
        "current"
    )

fgTrapIpsFailOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 506)
)
fgTrapIpsFailOpen.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapIpsFailOpen.setStatus(
        "current"
    )

fgTrapAvVirus = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 601)
)
fgTrapAvVirus.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgAvTrapVirName"))
)
if mibBuilder.loadTexts:
    fgTrapAvVirus.setStatus(
        "current"
    )

fgTrapAvOversize = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 602)
)
fgTrapAvOversize.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapAvOversize.setStatus(
        "current"
    )

fgTrapAvPattern = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 603)
)
fgTrapAvPattern.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapAvPattern.setStatus(
        "current"
    )

fgTrapAvFragmented = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 604)
)
fgTrapAvFragmented.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapAvFragmented.setStatus(
        "current"
    )

fgTrapAvEnterConserve = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 605)
)
fgTrapAvEnterConserve.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapAvEnterConserve.setStatus(
        "current"
    )

fgTrapAvBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 606)
)
fgTrapAvBypass.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapAvBypass.setStatus(
        "current"
    )

fgTrapAvOversizePass = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 607)
)
fgTrapAvOversizePass.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapAvOversizePass.setStatus(
        "current"
    )

fgTrapAvOversizeBlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 608)
)
fgTrapAvOversizeBlock.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fgTrapAvOversizeBlock.setStatus(
        "current"
    )

fgTrapFazDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 701)
)
fgTrapFazDisconnect.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgTrapFazDisconnect.setStatus(
        "current"
    )

fgTrapFaz = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 702)
)
fgTrapFaz.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgFazTrapType"))
)
if mibBuilder.loadTexts:
    fgTrapFaz.setStatus(
        "current"
    )

fgTrapWcApUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 801)
)
fgTrapWcApUp.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApName"))
)
if mibBuilder.loadTexts:
    fgTrapWcApUp.setStatus(
        "current"
    )

fgTrapWcApDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 802)
)
fgTrapWcApDown.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgWcApName"))
)
if mibBuilder.loadTexts:
    fgTrapWcApDown.setStatus(
        "current"
    )

fgTrapFcSwUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 901)
)
fgTrapFcSwUp.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwName"))
)
if mibBuilder.loadTexts:
    fgTrapFcSwUp.setStatus(
        "current"
    )

fgTrapFcSwDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 902)
)
fgTrapFcSwDown.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwVdom"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwSerial"),
        ("FORTINET-FORTIGATE-MIB", "fgFcSwName"))
)
if mibBuilder.loadTexts:
    fgTrapFcSwDown.setStatus(
        "current"
    )

fgTrapServerLoadBalanceRealServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 1101)
)
fgTrapServerLoadBalanceRealServerDown.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgServerLoadBalanceRealServerAddress"),
        ("FORTINET-FORTIGATE-MIB", "fgServerLoadBalanceVirtualServerName"),
        ("FORTINET-FORTIGATE-MIB", "fgServerLoadBalanceRealServerAddress6"))
)
if mibBuilder.loadTexts:
    fgTrapServerLoadBalanceRealServerDown.setStatus(
        "current"
    )

fgTrapPerCpuHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 1102)
)
fgTrapPerCpuHigh.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgPerCpuHighDetails"))
)
if mibBuilder.loadTexts:
    fgTrapPerCpuHigh.setStatus(
        "current"
    )

fgTrapDeviceNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 1201)
)
fgTrapDeviceNew.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntIndex"),
        ("FORTINET-FORTIGATE-MIB", "fgDeviceCreated"),
        ("FORTINET-FORTIGATE-MIB", "fgDeviceLastSeen"),
        ("FORTINET-FORTIGATE-MIB", "fgDeviceMacAddress"))
)
if mibBuilder.loadTexts:
    fgTrapDeviceNew.setStatus(
        "current"
    )

fgTrapDhcp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 1301)
)
fgTrapDhcp.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifName"),
        ("FORTINET-FORTIGATE-MIB", "fgVdEntName"),
        ("FORTINET-FORTIGATE-MIB", "fgDhcpServerId"),
        ("FORTINET-FORTIGATE-MIB", "fgDhcpTrapType"),
        ("FORTINET-FORTIGATE-MIB", "fgDhcpTrapMessage"))
)
if mibBuilder.loadTexts:
    fgTrapDhcp.setStatus(
        "current"
    )

fgTrapPoolUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 1401)
)
fgTrapPoolUsage.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppTrapType"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsName"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppStatsGroupName"),
        ("FORTINET-FORTIGATE-MIB", "fgFwTrapPoolUtilization"),
        ("FORTINET-FORTIGATE-MIB", "fgFwIppTrapPoolProto"))
)
if mibBuilder.loadTexts:
    fgTrapPoolUsage.setStatus(
        "current"
    )

fgTrapSlbc = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 1501)
)
fgTrapSlbc.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgChassisSlotId"),
        ("FORTINET-FORTIGATE-MIB", "fgChassisTrapMessage"))
)
if mibBuilder.loadTexts:
    fgTrapSlbc.setStatus(
        "current"
    )

fgTrapInterface = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 1601)
)
fgTrapInterface.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfTrapType"),
        ("IF-MIB", "ifName"),
        ("FORTINET-CORE-MIB", "fnGenTrapMsg"))
)
if mibBuilder.loadTexts:
    fgTrapInterface.setStatus(
        "current"
    )

fgTrapDio = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 2, 0, 1701)
)
fgTrapDio.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIGATE-MIB", "fgDioTrapType"),
        ("FORTINET-FORTIGATE-MIB", "fgDioEntName"),
        ("FORTINET-CORE-MIB", "fnGenTrapMsg"))
)
if mibBuilder.loadTexts:
    fgTrapDio.setStatus(
        "current"
    )

fgFmTrapDeployComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 0, 1000)
)
fgFmTrapDeployComplete.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgFmTrapDeployComplete.setStatus(
        "current"
    )

fgFmTrapDeployInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 0, 1002)
)
fgFmTrapDeployInProgress.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgFmTrapDeployInProgress.setStatus(
        "current"
    )

fgFmTrapConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 0, 1003)
)
fgFmTrapConfChange.setObjects(
    ("FORTINET-CORE-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fgFmTrapConfChange.setStatus(
        "current"
    )

fgFmTrapIfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 101, 6, 0, 1004)
)
fgFmTrapIfChange.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("IF-MIB", "ifName"),
        ("FORTINET-FORTIGATE-MIB", "fgManIfIp"),
        ("FORTINET-FORTIGATE-MIB", "fgManIfMask"),
        ("FORTINET-FORTIGATE-MIB", "fgManIfIp6"))
)
if mibBuilder.loadTexts:
    fgFmTrapIfChange.setStatus(
        "current"
    )


# Notifications groups

fgFmTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 1)
)
fgFmTrapGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgFmTrapDeployComplete"),
        ("FORTINET-FORTIGATE-MIB", "fgFmTrapDeployInProgress"),
        ("FORTINET-FORTIGATE-MIB", "fgFmTrapConfChange"),
        ("FORTINET-FORTIGATE-MIB", "fgFmTrapIfChange"))
)
if mibBuilder.loadTexts:
    fgFmTrapGroup.setStatus(
        "current"
    )

fgNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 18)
)
fgNotificationGroup.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgTrapVpnTunUp"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapVpnTunDown"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapHaSwitch"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapHaHBFail"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapHaMemberDown"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapHaMemberUp"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapIpsSignature"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapIpsAnomaly"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapIpsPkgUpdate"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapIpsFailOpen"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvVirus"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvOversize"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvPattern"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvFragmented"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvEnterConserve"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvBypass"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvOversizePass"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapAvOversizeBlock"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapFazDisconnect"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapFaz"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapWcApUp"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapWcApDown"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapDeviceNew"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapPerCpuHigh"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapDhcp"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapPoolUsage"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapInterface"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapDio"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapFcSwUp"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapFcSwDown"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapServerLoadBalanceRealServerDown"),
        ("FORTINET-FORTIGATE-MIB", "fgTrapSlbc"))
)
if mibBuilder.loadTexts:
    fgNotificationGroup.setStatus(
        "current"
    )

fgObsoleteNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 19)
)
fgObsoleteNotificationsGroup.setObjects(
    ("FORTINET-FORTIGATE-MIB", "fgTrapHaStateChange")
)
if mibBuilder.loadTexts:
    fgObsoleteNotificationsGroup.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance

fgMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 100)
)
fgMIBCompliance.setObjects(
      *(("FORTINET-FORTIGATE-MIB", "fgFmTrapGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgNotificationGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgFmTrapObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgAdminObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgSystemObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgSoftwareObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgHwSensorsObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgHighAvailabilityObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgVpnObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgFirewallObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgAppServicesObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgAntivirusObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgIntrusionPrevtObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgWebFilterObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgVirtualDomainObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgAdministrationObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgIntfObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgProcessorsObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgExplicitProxyObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgWebCacheObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgWanOptObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgSystemAdvancedObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgWcObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgFcObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgServerLoadBalanceObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbportsObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgUsbModemInfoGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgDeviceObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgLinkMonitorGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgInternalModemInfoGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgInternalModemSIMInfoGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgInternalModemSigInfoGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgInternalModemTrafficInfoGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgInternalModemSessInfoGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgInternalModemGpsInfoGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgInternalModemDatausageInfoGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgVWLHealthCheckLinkGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgDisksObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgNPUGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgSlaProbeClientGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgDNSProxyObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgLogGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgConfigGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgDhcpObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgDpdkEngsObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgChassisSensorsObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgSwitchDeviceObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgSwitchPortObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgChassisObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgServiceGroupWorkerBladesGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgEmsObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgDioObjectGroup"),
        ("FORTINET-FORTIGATE-MIB", "fgInternal5GModemsInfoObjectGroup"))
)
if mibBuilder.loadTexts:
    fgMIBCompliance.setStatus(
        "current"
    )

fg300MibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 101)
)
fg300MibCompliance.setObjects(
    ("FORTINET-FORTIGATE-MIB", "fgObsoleteNotificationsGroup")
)
if mibBuilder.loadTexts:
    fg300MibCompliance.setStatus(
        "deprecated"
    )

fgObsolteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 101, 100, 102)
)
fgObsolteMIBCompliance.setObjects(
    ("FORTINET-FORTIGATE-MIB", "fgObsoleteAppServicesObjectGroup")
)
if mibBuilder.loadTexts:
    fgObsolteMIBCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTIGATE-MIB",
    **{"FgVdIndex": FgVdIndex,
       "FgOpMode": FgOpMode,
       "FgHaMode": FgHaMode,
       "FgHaState": FgHaState,
       "FgSgWorkerBladeIndex": FgSgWorkerBladeIndex,
       "FgSgWorkerBladeState": FgSgWorkerBladeState,
       "FgHaLBSchedule": FgHaLBSchedule,
       "FgAdminPermLevel": FgAdminPermLevel,
       "FgFwUserAuthType": FgFwUserAuthType,
       "FgFwAuthUserType": FgFwAuthUserType,
       "FgSessProto": FgSessProto,
       "FgP2PProto": FgP2PProto,
       "FgScanAvDisposition": FgScanAvDisposition,
       "FgWanOptProtocols": FgWanOptProtocols,
       "FgWanOptHistPeriods": FgWanOptHistPeriods,
       "FgHaStatsSyncStatusType": FgHaStatsSyncStatusType,
       "FgWcWlanSecurityType": FgWcWlanSecurityType,
       "FgWcWlanAuthenticationType": FgWcWlanAuthenticationType,
       "FgWcWlanEncryptionType": FgWcWlanEncryptionType,
       "FgWcWtpRadioId": FgWcWtpRadioId,
       "FgWcWtpRadioType": FgWcWtpRadioType,
       "FgWcWtpChannelWidthType": FgWcWtpChannelWidthType,
       "FgWcWtpRadioBandType": FgWcWtpRadioBandType,
       "FgWcWtpRadioChannelNumber": FgWcWtpRadioChannelNumber,
       "FgWcWtpRadioMode": FgWcWtpRadioMode,
       "FgWcCountryString": FgWcCountryString,
       "FgNPUIndex": FgNPUIndex,
       "FgLogDeviceIndex": FgLogDeviceIndex,
       "fnFortiGateMib": fnFortiGateMib,
       "fgModel": fgModel,
       "fgtVM64": fgtVM64,
       "fgtVM64XEN": fgtVM64XEN,
       "fgtVM64AWS": fgtVM64AWS,
       "fgtVM64FGCAWS": fgtVM64FGCAWS,
       "fgtVM64OPC": fgtVM64OPC,
       "fgtVM64KVm": fgtVM64KVm,
       "fgtVM64FGCKVM": fgtVM64FGCKVM,
       "fgtVM64GCP": fgtVM64GCP,
       "fgtARM64KVM": fgtARM64KVM,
       "fgtVM64HV": fgtVM64HV,
       "fgt40F": fgt40F,
       "fgt41F": fgt41F,
       "fg40FI": fg40FI,
       "fg41FI": fg41FI,
       "fwf40F": fwf40F,
       "fwf41F": fwf41F,
       "fw40FI": fw40FI,
       "fw41FI": fw41FI,
       "fgt50G": fgt50G,
       "fg50G5": fg50G5,
       "fg50GD": fg50GD,
       "fg51G5": fg51G5,
       "fw50G5": fw50G5,
       "fwf50G": fwf50G,
       "fwf51G": fwf51G,
       "fwf50GD": fwf50GD,
       "fw51G5": fw51G5,
       "fgt51G": fgt51G,
       "fg50GP": fg50GP,
       "fgt51GP": fgt51GP,
       "fw50GS": fw50GS,
       "fg50GS": fg50GS,
       "fwf60E": fwf60E,
       "fgt61E": fgt61E,
       "fgt60E": fgt60E,
       "fgt60EPOE": fgt60EPOE,
       "fgr60F": fgr60F,
       "fgt60F": fgt60F,
       "fgt61F": fgt61F,
       "fwf60F": fwf60F,
       "fwf61F": fwf61F,
       "fgr60FI": fgr60FI,
       "fwf61E": fwf61E,
       "fgt60EJ": fgt60EJ,
       "fwf60EJ": fwf60EJ,
       "fgt60EV": fgt60EV,
       "fwf60EV": fwf60EV,
       "fgt70F": fgt70F,
       "fgt71F": fgt71F,
       "fr70FB": fr70FB,
       "fr70FM": fr70FM,
       "fw80FS": fw80FS,
       "fw81FS": fw81FS,
       "fgt80EPOE": fgt80EPOE,
       "fgt80E": fgt80E,
       "fgt81E": fgt81E,
       "fgt81EPOE": fgt81EPOE,
       "fgt80F": fgt80F,
       "fgt81F": fgt81F,
       "fgt80FBP": fgt80FBP,
       "fwf80F": fwf80F,
       "fwf81F": fwf81F,
       "fgt80FPOE": fgt80FPOE,
       "fgt81FPOE": fgt81FPOE,
       "fw81FD": fw81FD,
       "fw81FP": fw81FP,
       "fgt80FDSL": fgt80FDSL,
       "fg900D": fg900D,
       "fgt90E": fgt90E,
       "fgt91E": fgt91E,
       "fgt90g": fgt90g,
       "fgt91g": fgt91g,
       "fwf90G": fwf90G,
       "fwf91G": fwf91G,
       "fgt100F": fgt100F,
       "fgt101F": fgt101F,
       "fgt140E": fgt140E,
       "fgt140EP": fgt140EP,
       "fgt100E": fgt100E,
       "fgt100EF": fgt100EF,
       "fgt101E": fgt101E,
       "fgt120g": fgt120g,
       "fgt121g": fgt121g,
       "fgt200E": fgt200E,
       "fgt201E": fgt201E,
       "fgt200F": fgt200F,
       "fgt201F": fgt201F,
       "fgt200G": fgt200G,
       "fgt201G": fgt201G,
       "fgt3HD": fgt3HD,
       "fgt300E": fgt300E,
       "fgt301E": fgt301E,
       "fgt400D": fgt400D,
       "fgt400E": fgt400E,
       "fgt401E": fgt401E,
       "fgt400EBP": fgt400EBP,
       "fgt400F": fgt400F,
       "fgt401F": fgt401F,
       "fgt500D": fgt500D,
       "fgt500E": fgt500E,
       "fgt501E": fgt501E,
       "fgt600D": fgt600D,
       "fgt600E": fgt600E,
       "fgt601E": fgt601E,
       "fgt600F": fgt600F,
       "fgt601F": fgt601F,
       "fgt800D": fgt800D,
       "fgt900G": fgt900G,
       "fgt901G": fgt901G,
       "fgt1000D": fgt1000D,
       "fgt1100E": fgt1100E,
       "fgt1101E": fgt1101E,
       "fgt1000F": fgt1000F,
       "fgt1001F": fgt1001F,
       "fgt1200D": fgt1200D,
       "fgt1500D": fgt1500D,
       "fgt1500DT": fgt1500DT,
       "fgt1801F": fgt1801F,
       "fgt1800F": fgt1800F,
       "ffw1801F": ffw1801F,
       "fgt2200E": fgt2200E,
       "fgt2201E": fgt2201E,
       "fgt2000E": fgt2000E,
       "fgt2500E": fgt2500E,
       "fgt2600F": fgt2600F,
       "fgt2601F": fgt2601F,
       "ffw2600F": ffw2600F,
       "fgt3000D": fgt3000D,
       "fgt3300E": fgt3300E,
       "fgt3301E": fgt3301E,
       "fgt3000F": fgt3000F,
       "fgt3001F": fgt3001F,
       "ffw3001F": ffw3001F,
       "fgt3100D": fgt3100D,
       "fgt3200D": fgt3200D,
       "fgt3200F": fgt3200F,
       "fgt3201F": fgt3201F,
       "fgt3400E": fgt3400E,
       "fgt3401E": fgt3401E,
       "fgt3500F": fgt3500F,
       "fgt3501F": fgt3501F,
       "ffw3501F": ffw3501F,
       "fgt3600E": fgt3600E,
       "fgt3601E": fgt3601E,
       "fgt3700D": fgt3700D,
       "fgt3700F": fgt3700F,
       "fgt3701F": fgt3701F,
       "fgt3800D": fgt3800D,
       "fgt4200F": fgt4200F,
       "ffw4200F": ffw4200F,
       "fgt3810D": fgt3810D,
       "fgt3815D": fgt3815D,
       "fgt4400F": fgt4400F,
       "ffw4400F": ffw4400F,
       "fgt3960E": fgt3960E,
       "fgt3980E": fgt3980E,
       "ffw3980E": ffw3980E,
       "fgt4201F": fgt4201F,
       "fgt4401F": fgt4401F,
       "ffw4401F": ffw4401F,
       "fgt4800F": fgt4800F,
       "fgt4801F": fgt4801F,
       "ffw4801F": ffw4801F,
       "fgt5001D": fgt5001D,
       "fgt5001E": fgt5001E,
       "fgt5001E1": fgt5001E1,
       "fgt6000F": fgt6000F,
       "fgt7000E": fgt7000E,
       "fgt7000F": fgt7000F,
       "ffvmev": ffvmev,
       "fgvmev": fgvmev,
       "fgvmxx": fgvmxx,
       "fgtvmx": fgtvmx,
       "fgvm00": fgvm00,
       "fgvm01": fgvm01,
       "fgvm02": fgvm02,
       "fgvm04": fgvm04,
       "fgvm08": fgvm08,
       "fgvm16": fgvm16,
       "fgvm32": fgvm32,
       "fgvm1v": fgvm1v,
       "fgvm2v": fgvm2v,
       "fgvm4v": fgvm4v,
       "fgvm8v": fgvm8v,
       "fgv16v": fgv16v,
       "fgv32v": fgv32v,
       "fgvulv": fgvulv,
       "fgvmul": fgvmul,
       "fgvmsl": fgvmsl,
       "fgvmsb": fgvmsb,
       "fgvmel": fgvmel,
       "fgvmml": fgvmml,
       "ffvmbb": ffvmbb,
       "fgvmpg": fgvmpg,
       "fgtARM64AWS": fgtARM64AWS,
       "fgtARM64XEN": fgtARM64XEN,
       "fgtVM64ALI": fgtVM64ALI,
       "fgtVM64RAXONDEMAND": fgtVM64RAXONDEMAND,
       "fgtVM64IBM": fgtVM64IBM,
       "fgtARM64OCI": fgtARM64OCI,
       "fgtARM64GCP": fgtARM64GCP,
       "fgtARM64AZURE": fgtARM64AZURE,
       "ffwVM64": ffwVM64,
       "ffwVM64KVm": ffwVM64KVm,
       "fgtVM64AZURE": fgtVM64AZURE,
       "fgTraps": fgTraps,
       "fgTrapPrefix": fgTrapPrefix,
       "fgTrapVpnTunUp": fgTrapVpnTunUp,
       "fgTrapVpnTunDown": fgTrapVpnTunDown,
       "fgTrapHaSwitch": fgTrapHaSwitch,
       "fgTrapHaStateChange": fgTrapHaStateChange,
       "fgTrapHaHBFail": fgTrapHaHBFail,
       "fgTrapHaMemberDown": fgTrapHaMemberDown,
       "fgTrapHaMemberUp": fgTrapHaMemberUp,
       "fgTrapIpsSignature": fgTrapIpsSignature,
       "fgTrapIpsAnomaly": fgTrapIpsAnomaly,
       "fgTrapIpsPkgUpdate": fgTrapIpsPkgUpdate,
       "fgTrapIpsFailOpen": fgTrapIpsFailOpen,
       "fgTrapAvVirus": fgTrapAvVirus,
       "fgTrapAvOversize": fgTrapAvOversize,
       "fgTrapAvPattern": fgTrapAvPattern,
       "fgTrapAvFragmented": fgTrapAvFragmented,
       "fgTrapAvEnterConserve": fgTrapAvEnterConserve,
       "fgTrapAvBypass": fgTrapAvBypass,
       "fgTrapAvOversizePass": fgTrapAvOversizePass,
       "fgTrapAvOversizeBlock": fgTrapAvOversizeBlock,
       "fgTrapFazDisconnect": fgTrapFazDisconnect,
       "fgTrapFaz": fgTrapFaz,
       "fgTrapWcApUp": fgTrapWcApUp,
       "fgTrapWcApDown": fgTrapWcApDown,
       "fgTrapFcSwUp": fgTrapFcSwUp,
       "fgTrapFcSwDown": fgTrapFcSwDown,
       "fgTrapServerLoadBalanceRealServerDown": fgTrapServerLoadBalanceRealServerDown,
       "fgTrapPerCpuHigh": fgTrapPerCpuHigh,
       "fgTrapDeviceNew": fgTrapDeviceNew,
       "fgTrapDhcp": fgTrapDhcp,
       "fgTrapPoolUsage": fgTrapPoolUsage,
       "fgTrapSlbc": fgTrapSlbc,
       "fgTrapInterface": fgTrapInterface,
       "fgTrapDio": fgTrapDio,
       "fgVirtualDomain": fgVirtualDomain,
       "fgVdInfo": fgVdInfo,
       "fgVdNumber": fgVdNumber,
       "fgVdMaxVdoms": fgVdMaxVdoms,
       "fgVdEnabled": fgVdEnabled,
       "fgVdTables": fgVdTables,
       "fgVdTable": fgVdTable,
       "fgVdEntry": fgVdEntry,
       "fgVdEntIndex": fgVdEntIndex,
       "fgVdEntName": fgVdEntName,
       "fgVdEntOpMode": fgVdEntOpMode,
       "fgVdEntHaState": fgVdEntHaState,
       "fgVdEntCpuUsage": fgVdEntCpuUsage,
       "fgVdEntMemUsage": fgVdEntMemUsage,
       "fgVdEntSesCount": fgVdEntSesCount,
       "fgVdEntSesRate": fgVdEntSesRate,
       "fgVdEntChecksum": fgVdEntChecksum,
       "fgVdTpTable": fgVdTpTable,
       "fgVdTpEntry": fgVdTpEntry,
       "fgVdTpMgmtAddrType": fgVdTpMgmtAddrType,
       "fgVdTpMgmtAddr": fgVdTpMgmtAddr,
       "fgVdTpMgmtMask": fgVdTpMgmtMask,
       "fgSystem": fgSystem,
       "fgSystemInfo": fgSystemInfo,
       "fgSysVersion": fgSysVersion,
       "fgSysMgmtVdom": fgSysMgmtVdom,
       "fgSysCpuUsage": fgSysCpuUsage,
       "fgSysMemUsage": fgSysMemUsage,
       "fgSysMemCapacity": fgSysMemCapacity,
       "fgSysDiskUsage": fgSysDiskUsage,
       "fgSysDiskCapacity": fgSysDiskCapacity,
       "fgSysSesCount": fgSysSesCount,
       "fgSysLowMemUsage": fgSysLowMemUsage,
       "fgSysLowMemCapacity": fgSysLowMemCapacity,
       "fgSysSesRate1": fgSysSesRate1,
       "fgSysSesRate10": fgSysSesRate10,
       "fgSysSesRate30": fgSysSesRate30,
       "fgSysSesRate60": fgSysSesRate60,
       "fgSysSes6Count": fgSysSes6Count,
       "fgSysSes6Rate1": fgSysSes6Rate1,
       "fgSysSes6Rate10": fgSysSes6Rate10,
       "fgSysSes6Rate30": fgSysSes6Rate30,
       "fgSysSes6Rate60": fgSysSes6Rate60,
       "fgSysUpTime": fgSysUpTime,
       "fgSysNeedLogPartitionScan": fgSysNeedLogPartitionScan,
       "fgSysUpTimeDetail": fgSysUpTimeDetail,
       "fgSysRebootReason": fgSysRebootReason,
       "fgSysNpuSesCount": fgSysNpuSesCount,
       "fgSysNpuSesRate1": fgSysNpuSesRate1,
       "fgSysNpuSesRate10": fgSysNpuSesRate10,
       "fgSysNpuSesRate30": fgSysNpuSesRate30,
       "fgSysNpuSesRate60": fgSysNpuSesRate60,
       "fgSysNpuSes6Count": fgSysNpuSes6Count,
       "fgSysNpuSes6Rate1": fgSysNpuSes6Rate1,
       "fgSysNpuSes6Rate10": fgSysNpuSes6Rate10,
       "fgSysNpuSes6Rate30": fgSysNpuSes6Rate30,
       "fgSysNpuSes6Rate60": fgSysNpuSes6Rate60,
       "fgDataCpuUsage": fgDataCpuUsage,
       "fgDataMemUsage": fgDataMemUsage,
       "fgSysFreeMemUsage": fgSysFreeMemUsage,
       "fgSysFreeableMemUsage": fgSysFreeableMemUsage,
       "fgDataSecurityLevel": fgDataSecurityLevel,
       "fgSoftware": fgSoftware,
       "fgSysVersionAv": fgSysVersionAv,
       "fgSysVersionIps": fgSysVersionIps,
       "fgSysVersionAvEt": fgSysVersionAvEt,
       "fgSysVersionIpsEt": fgSysVersionIpsEt,
       "fgHwSensors": fgHwSensors,
       "fgHwSensorCount": fgHwSensorCount,
       "fgHwSensorTable": fgHwSensorTable,
       "fgHwSensorEntry": fgHwSensorEntry,
       "fgHwSensorEntIndex": fgHwSensorEntIndex,
       "fgHwSensorEntName": fgHwSensorEntName,
       "fgHwSensorEntValue": fgHwSensorEntValue,
       "fgHwSensorEntAlarmStatus": fgHwSensorEntAlarmStatus,
       "fgProcessors": fgProcessors,
       "fgProcessorCount": fgProcessorCount,
       "fgProcessorTable": fgProcessorTable,
       "fgProcessorEntry": fgProcessorEntry,
       "fgProcessorEntIndex": fgProcessorEntIndex,
       "fgProcessorUsage": fgProcessorUsage,
       "fgProcessorUsage5sec": fgProcessorUsage5sec,
       "fgProcessorType": fgProcessorType,
       "fgProcessorContainedIn": fgProcessorContainedIn,
       "fgProcessorPktRxCount": fgProcessorPktRxCount,
       "fgProcessorPktTxCount": fgProcessorPktTxCount,
       "fgProcessorPktDroppedCount": fgProcessorPktDroppedCount,
       "fgProcessorUserUsage": fgProcessorUserUsage,
       "fgProcessorSysUsage": fgProcessorSysUsage,
       "fgProcessorPktTxDroppedCount": fgProcessorPktTxDroppedCount,
       "fgProcessorTypes": fgProcessorTypes,
       "fgProcessorOther": fgProcessorOther,
       "fgProcessorIntel": fgProcessorIntel,
       "fgProcessorAMD": fgProcessorAMD,
       "fgProcessorXlr": fgProcessorXlr,
       "fgProcessorFnSoc": fgProcessorFnSoc,
       "fgProcessorFnNP2": fgProcessorFnNP2,
       "fgProcessorFnNP4": fgProcessorFnNP4,
       "fgProcessorFnNP6": fgProcessorFnNP6,
       "fgProcessorFnNP6LITE": fgProcessorFnNP6LITE,
       "fgProcessorFnNP7": fgProcessorFnNP7,
       "fgProcessorFnNP6XLITE": fgProcessorFnNP6XLITE,
       "fgProcessorFnNP7LITE": fgProcessorFnNP7LITE,
       "fgProcessorsTrapObjects": fgProcessorsTrapObjects,
       "fgPerCpuHighDetails": fgPerCpuHighDetails,
       "fgProcessorModules": fgProcessorModules,
       "fgProcessorModuleTypes": fgProcessorModuleTypes,
       "fgProcModOther": fgProcModOther,
       "fgProcModIntegrated": fgProcModIntegrated,
       "fgProcModIntegratedNPU": fgProcModIntegratedNPU,
       "fgProcessorModuleCount": fgProcessorModuleCount,
       "fgProcessorModuleTable": fgProcessorModuleTable,
       "fgProcessorModuleEntry": fgProcessorModuleEntry,
       "fgProcModIndex": fgProcModIndex,
       "fgProcModType": fgProcModType,
       "fgProcModName": fgProcModName,
       "fgProcModDescr": fgProcModDescr,
       "fgProcModProcessorCount": fgProcModProcessorCount,
       "fgProcModMemCapacity": fgProcModMemCapacity,
       "fgProcModMemUsage": fgProcModMemUsage,
       "fgProcModSessionCount": fgProcModSessionCount,
       "fgProcModSACount": fgProcModSACount,
       "fgSystemInfoAdvanced": fgSystemInfoAdvanced,
       "fgSysInfoAdvMem": fgSysInfoAdvMem,
       "fgSIAdvMemPageCache": fgSIAdvMemPageCache,
       "fgSIAdvMemCacheActive": fgSIAdvMemCacheActive,
       "fgSIAdvMemCacheInactive": fgSIAdvMemCacheInactive,
       "fgSIAdvMemBuffer": fgSIAdvMemBuffer,
       "fgSIAdvMemEnterKerConsThrsh": fgSIAdvMemEnterKerConsThrsh,
       "fgSIAdvMemLeaveKerConsThrsh": fgSIAdvMemLeaveKerConsThrsh,
       "fgSIAdvMemEnterProxyConsThrsh": fgSIAdvMemEnterProxyConsThrsh,
       "fgSIAdvMemLeaveProxyConsThrsh": fgSIAdvMemLeaveProxyConsThrsh,
       "fgSysInfoAdvSessions": fgSysInfoAdvSessions,
       "fgSIAdvSesEphemeralCount": fgSIAdvSesEphemeralCount,
       "fgSIAdvSesEphemeralLimit": fgSIAdvSesEphemeralLimit,
       "fgSIAdvSesClashCount": fgSIAdvSesClashCount,
       "fgSIAdvSesExpCount": fgSIAdvSesExpCount,
       "fgSIAdvSesSyncQFCount": fgSIAdvSesSyncQFCount,
       "fgSIAdvSesAcceptQFCount": fgSIAdvSesAcceptQFCount,
       "fgSIAdvSesNoListenerCount": fgSIAdvSesNoListenerCount,
       "fgSIAdvLicenseDetails": fgSIAdvLicenseDetails,
       "fgLicContracts": fgLicContracts,
       "fgLicContractCount": fgLicContractCount,
       "fgLicContractTable": fgLicContractTable,
       "fgLicContractEntry": fgLicContractEntry,
       "fgLicContractDesc": fgLicContractDesc,
       "fgLicContractExpiry": fgLicContractExpiry,
       "fgLicVersions": fgLicVersions,
       "fgLicVersionCount": fgLicVersionCount,
       "fgLicVersionTable": fgLicVersionTable,
       "fgLicVersionEntry": fgLicVersionEntry,
       "fgLicVersionDesc": fgLicVersionDesc,
       "fgLicVersionExpiry": fgLicVersionExpiry,
       "fgLicVersionNumber": fgLicVersionNumber,
       "fgLicVersionUpdTime": fgLicVersionUpdTime,
       "fgLicVersionUpdMethod": fgLicVersionUpdMethod,
       "fgLicVersionTryTime": fgLicVersionTryTime,
       "fgLicVersionTryResult": fgLicVersionTryResult,
       "fgLicAlContracts": fgLicAlContracts,
       "fgLicAlContractCount": fgLicAlContractCount,
       "fgLicAlContractTable": fgLicAlContractTable,
       "fgLicAlContractEntry": fgLicAlContractEntry,
       "fgLicAlContractDesc": fgLicAlContractDesc,
       "fgLicAlContractExpiry": fgLicAlContractExpiry,
       "fgUsbports": fgUsbports,
       "fgUsbportCount": fgUsbportCount,
       "fgUsbportTable": fgUsbportTable,
       "fgUsbportEntry": fgUsbportEntry,
       "fgUsbportEntIndex": fgUsbportEntIndex,
       "fgUsbportPlugged": fgUsbportPlugged,
       "fgUsbportVersion": fgUsbportVersion,
       "fgUsbportClass": fgUsbportClass,
       "fgUsbportVendId": fgUsbportVendId,
       "fgUsbportProdId": fgUsbportProdId,
       "fgUsbportRevision": fgUsbportRevision,
       "fgUsbportManufacturer": fgUsbportManufacturer,
       "fgUsbportProduct": fgUsbportProduct,
       "fgUsbportSerial": fgUsbportSerial,
       "fgLinkMonitor": fgLinkMonitor,
       "fgLinkMonitorNumber": fgLinkMonitorNumber,
       "fgLinkMonitorTable": fgLinkMonitorTable,
       "fgLinkMonitorEntry": fgLinkMonitorEntry,
       "fgLinkMonitorID": fgLinkMonitorID,
       "fgLinkMonitorName": fgLinkMonitorName,
       "fgLinkMonitorState": fgLinkMonitorState,
       "fgLinkMonitorLatency": fgLinkMonitorLatency,
       "fgLinkMonitorJitter": fgLinkMonitorJitter,
       "fgLinkMonitorPacketSend": fgLinkMonitorPacketSend,
       "fgLinkMonitorPacketRecv": fgLinkMonitorPacketRecv,
       "fgLinkMonitorPacketLoss": fgLinkMonitorPacketLoss,
       "fgLinkMonitorVdom": fgLinkMonitorVdom,
       "fgLinkMonitorBandwidthIn": fgLinkMonitorBandwidthIn,
       "fgLinkMonitorBandwidthOut": fgLinkMonitorBandwidthOut,
       "fgLinkMonitorBandwidthBi": fgLinkMonitorBandwidthBi,
       "fgLinkMonitorOutofSeq": fgLinkMonitorOutofSeq,
       "fgLinkMonitorServer": fgLinkMonitorServer,
       "fgLinkMonitorProtocol": fgLinkMonitorProtocol,
       "fgVWLHealthCheckLink": fgVWLHealthCheckLink,
       "fgVWLHealthCheckLinkNumber": fgVWLHealthCheckLinkNumber,
       "fgVWLHealthCheckLinkTable": fgVWLHealthCheckLinkTable,
       "fgVWLHealthCheckLinkEntry": fgVWLHealthCheckLinkEntry,
       "fgVWLHealthCheckLinkID": fgVWLHealthCheckLinkID,
       "fgVWLHealthCheckLinkName": fgVWLHealthCheckLinkName,
       "fgVWLHealthCheckLinkSeq": fgVWLHealthCheckLinkSeq,
       "fgVWLHealthCheckLinkState": fgVWLHealthCheckLinkState,
       "fgVWLHealthCheckLinkLatency": fgVWLHealthCheckLinkLatency,
       "fgVWLHealthCheckLinkJitter": fgVWLHealthCheckLinkJitter,
       "fgVWLHealthCheckLinkPacketSend": fgVWLHealthCheckLinkPacketSend,
       "fgVWLHealthCheckLinkPacketRecv": fgVWLHealthCheckLinkPacketRecv,
       "fgVWLHealthCheckLinkPacketLoss": fgVWLHealthCheckLinkPacketLoss,
       "fgVWLHealthCheckLinkVdom": fgVWLHealthCheckLinkVdom,
       "fgVWLHealthCheckLinkBandwidthIn": fgVWLHealthCheckLinkBandwidthIn,
       "fgVWLHealthCheckLinkBandwidthOut": fgVWLHealthCheckLinkBandwidthOut,
       "fgVWLHealthCheckLinkBandwidthBi": fgVWLHealthCheckLinkBandwidthBi,
       "fgVWLHealthCheckLinkIfName": fgVWLHealthCheckLinkIfName,
       "fgVWLHealthCheckLinkUsedBandwidthIn": fgVWLHealthCheckLinkUsedBandwidthIn,
       "fgVWLHealthCheckLinkUsedBandwidthOut": fgVWLHealthCheckLinkUsedBandwidthOut,
       "fgVWLHealthCheckLinkUsedBandwidthBi": fgVWLHealthCheckLinkUsedBandwidthBi,
       "fgVWLHealthCheckLinkMOSCodec": fgVWLHealthCheckLinkMOSCodec,
       "fgVWLHealthCheckLinkMOS": fgVWLHealthCheckLinkMOS,
       "fgDisks": fgDisks,
       "fgDiskCount": fgDiskCount,
       "fgDiskTable": fgDiskTable,
       "fgDiskEntry": fgDiskEntry,
       "fgDiskIndex": fgDiskIndex,
       "fgDiskName": fgDiskName,
       "fgDiskFsMountsTable": fgDiskFsMountsTable,
       "fgDiskFsMountsEntry": fgDiskFsMountsEntry,
       "fgDiskFsMountDevIdx": fgDiskFsMountDevIdx,
       "fgDiskFsMountName": fgDiskFsMountName,
       "fgDiskFsMountMountPoint": fgDiskFsMountMountPoint,
       "fgDiskFsMountType": fgDiskFsMountType,
       "fgDiskFsMountOptions": fgDiskFsMountOptions,
       "fgDiskFsMountFreq": fgDiskFsMountFreq,
       "fgDiskFsMountPassNo": fgDiskFsMountPassNo,
       "fgDiskFsMountOptionsVal": fgDiskFsMountOptionsVal,
       "fgDiskPartitionsTable": fgDiskPartitionsTable,
       "fgDiskPartitionsEntry": fgDiskPartitionsEntry,
       "fgDiskPartitionIdx": fgDiskPartitionIdx,
       "fgDiskPartitionsMajor": fgDiskPartitionsMajor,
       "fgDiskPartitionsMinor": fgDiskPartitionsMinor,
       "fgDiskPartitionsBlockNum": fgDiskPartitionsBlockNum,
       "fgDiskPartitionsName": fgDiskPartitionsName,
       "fgSlaProbeClient": fgSlaProbeClient,
       "fgSlaProbeClientNumber": fgSlaProbeClientNumber,
       "fgSlaProbeClientTable": fgSlaProbeClientTable,
       "fgSlaProbeClientEntry": fgSlaProbeClientEntry,
       "fgSlaProbeClientID": fgSlaProbeClientID,
       "fgSlaProbeClientIP": fgSlaProbeClientIP,
       "fgSlaProbeClientState": fgSlaProbeClientState,
       "fgSlaProbeClientAvgLatency": fgSlaProbeClientAvgLatency,
       "fgSlaProbeClientAvgLatencySD": fgSlaProbeClientAvgLatencySD,
       "fgSlaProbeClientAvgLatencyDS": fgSlaProbeClientAvgLatencyDS,
       "fgSlaProbeClientMinLatency": fgSlaProbeClientMinLatency,
       "fgSlaProbeClientMinLatencySD": fgSlaProbeClientMinLatencySD,
       "fgSlaProbeClientMinLatencyDS": fgSlaProbeClientMinLatencyDS,
       "fgSlaProbeClientMaxLatency": fgSlaProbeClientMaxLatency,
       "fgSlaProbeClientMaxLatencySD": fgSlaProbeClientMaxLatencySD,
       "fgSlaProbeClientMaxLatencyDS": fgSlaProbeClientMaxLatencyDS,
       "fgSlaProbeClientAvgJitter": fgSlaProbeClientAvgJitter,
       "fgSlaProbeClientAvgJitterSD": fgSlaProbeClientAvgJitterSD,
       "fgSlaProbeClientAvgJitterDS": fgSlaProbeClientAvgJitterDS,
       "fgSlaProbeClientMinJitter": fgSlaProbeClientMinJitter,
       "fgSlaProbeClientMinJitterSD": fgSlaProbeClientMinJitterSD,
       "fgSlaProbeClientMinJitterDS": fgSlaProbeClientMinJitterDS,
       "fgSlaProbeClientMaxJitter": fgSlaProbeClientMaxJitter,
       "fgSlaProbeClientMaxJitterSD": fgSlaProbeClientMaxJitterSD,
       "fgSlaProbeClientMaxJitterDS": fgSlaProbeClientMaxJitterDS,
       "fgSlaProbeClientPktloss": fgSlaProbeClientPktloss,
       "fgSlaProbeClientPktlossSD": fgSlaProbeClientPktlossSD,
       "fgSlaProbeClientPktlossDS": fgSlaProbeClientPktlossDS,
       "fgSlaProbeClientOutofSeq": fgSlaProbeClientOutofSeq,
       "fgSlaProbeClientOutofSeqSD": fgSlaProbeClientOutofSeqSD,
       "fgSlaProbeClientOutofSeqDS": fgSlaProbeClientOutofSeqDS,
       "fgDpdkEngs": fgDpdkEngs,
       "fgDpdkEngCount": fgDpdkEngCount,
       "fgDpdkEngTable": fgDpdkEngTable,
       "fgDpdkEngEntry": fgDpdkEngEntry,
       "fgDpdkEngEntIndex": fgDpdkEngEntIndex,
       "fgDpdkEngRxUsage": fgDpdkEngRxUsage,
       "fgDpdkEngVnpUsage": fgDpdkEngVnpUsage,
       "fgDpdkEngIpsUsage": fgDpdkEngIpsUsage,
       "fgDpdkEngTxUsage": fgDpdkEngTxUsage,
       "fgDpdkEngIdle": fgDpdkEngIdle,
       "fgDpdkEngToCpu": fgDpdkEngToCpu,
       "fgDigitalIO": fgDigitalIO,
       "fgDioInfo": fgDioInfo,
       "fgDioTables": fgDioTables,
       "fgDioTable": fgDioTable,
       "fgDioEntry": fgDioEntry,
       "fgDioEntIndex": fgDioEntIndex,
       "fgDioEntName": fgDioEntName,
       "fgDioEntStatusMsg": fgDioEntStatusMsg,
       "fgDioTrapObjects": fgDioTrapObjects,
       "fgDioTrapType": fgDioTrapType,
       "fgChassisSensors": fgChassisSensors,
       "fgChassisSensorCount": fgChassisSensorCount,
       "fgChassisSensorTable": fgChassisSensorTable,
       "fgChassisSensorEntry": fgChassisSensorEntry,
       "fgChassisSensorEntIndex": fgChassisSensorEntIndex,
       "fgChassisSensorEntName": fgChassisSensorEntName,
       "fgChassisSensorEntValue": fgChassisSensorEntValue,
       "fgChassisSensorEntAlarmStatus": fgChassisSensorEntAlarmStatus,
       "fgFirewall": fgFirewall,
       "fgFwPolicies": fgFwPolicies,
       "fgFwPolInfo": fgFwPolInfo,
       "fgFwPolTables": fgFwPolTables,
       "fgFwPolStatsTable": fgFwPolStatsTable,
       "fgFwPolStatsEntry": fgFwPolStatsEntry,
       "fgFwPolID": fgFwPolID,
       "fgFwPolPktCount": fgFwPolPktCount,
       "fgFwPolByteCount": fgFwPolByteCount,
       "fgFwPolLastUsed": fgFwPolLastUsed,
       "fgFwPolPktCountHc": fgFwPolPktCountHc,
       "fgFwPolByteCountHc": fgFwPolByteCountHc,
       "fgFwHsPolStatsTable": fgFwHsPolStatsTable,
       "fgFwHsPolStatsEntry": fgFwHsPolStatsEntry,
       "fgFwHsPolID": fgFwHsPolID,
       "fgFwHsPolPktCount": fgFwHsPolPktCount,
       "fgFwHsPolByteCount": fgFwHsPolByteCount,
       "fgFwHsPolLastUsed": fgFwHsPolLastUsed,
       "fgFwUsers": fgFwUsers,
       "fgFwUserInfo": fgFwUserInfo,
       "fgFwUserNumber": fgFwUserNumber,
       "fgFwUserAuthTimeout": fgFwUserAuthTimeout,
       "fgFwUserTables": fgFwUserTables,
       "fgFwUserTable": fgFwUserTable,
       "fgFwUserEntry": fgFwUserEntry,
       "fgFwUserIndex": fgFwUserIndex,
       "fgFwUserName": fgFwUserName,
       "fgFwUserAuth": fgFwUserAuth,
       "fgFwUserState": fgFwUserState,
       "fgFwUserVdom": fgFwUserVdom,
       "fgFwAuthUserTables": fgFwAuthUserTables,
       "fgFwAuthUserInfoTable": fgFwAuthUserInfoTable,
       "fgFwAuthUserInfoEntry": fgFwAuthUserInfoEntry,
       "fgFwAuthUserInfoVdom": fgFwAuthUserInfoVdom,
       "fgFwAuthIpv4UserNumber": fgFwAuthIpv4UserNumber,
       "fgFwAuthIpv6UserNumber": fgFwAuthIpv6UserNumber,
       "fgFwAuthIpv4UserTable": fgFwAuthIpv4UserTable,
       "fgFwAuthIpv4UserEntry": fgFwAuthIpv4UserEntry,
       "fgFwAuthIpv4UserIndex": fgFwAuthIpv4UserIndex,
       "fgFwAuthIpv4UserVdom": fgFwAuthIpv4UserVdom,
       "fgFwAuthIpv4UserName": fgFwAuthIpv4UserName,
       "fgFwAuthIpv4UserType": fgFwAuthIpv4UserType,
       "fgFwAuthIpv4UserAddr": fgFwAuthIpv4UserAddr,
       "fgFwAuthIpv6UserTable": fgFwAuthIpv6UserTable,
       "fgFwAuthIpv6UserEntry": fgFwAuthIpv6UserEntry,
       "fgFwAuthIpv6UserIndex": fgFwAuthIpv6UserIndex,
       "fgFwAuthIpv6UserVdom": fgFwAuthIpv6UserVdom,
       "fgFwAuthIpv6UserName": fgFwAuthIpv6UserName,
       "fgFwAuthIpv6UserType": fgFwAuthIpv6UserType,
       "fgFwAuthIpv6UserAddr": fgFwAuthIpv6UserAddr,
       "fgFwIppools": fgFwIppools,
       "fgFwIppTables": fgFwIppTables,
       "fgFwIppStatsTable": fgFwIppStatsTable,
       "fgFwIppStatsEntry": fgFwIppStatsEntry,
       "fgFwIppStatsName": fgFwIppStatsName,
       "fgFwIppStatsType": fgFwIppStatsType,
       "fgFwIppStatsStartIp": fgFwIppStatsStartIp,
       "fgFwIppStatsEndIp": fgFwIppStatsEndIp,
       "fgFwIppStatsTotalSessions": fgFwIppStatsTotalSessions,
       "fgFwIppStatsTcpSessions": fgFwIppStatsTcpSessions,
       "fgFwIppStatsUdpSessions": fgFwIppStatsUdpSessions,
       "fgFwIppStatsOtherSessions": fgFwIppStatsOtherSessions,
       "fgFwIppStatsTotalPBAs": fgFwIppStatsTotalPBAs,
       "fgFwIppStatsInusePBAs": fgFwIppStatsInusePBAs,
       "fgFwIppStatsExpiringPBAs": fgFwIppStatsExpiringPBAs,
       "fgFwIppStatsFreePBAs": fgFwIppStatsFreePBAs,
       "fgFwIppStatsFlags": fgFwIppStatsFlags,
       "fgFwIppStatsGroupName": fgFwIppStatsGroupName,
       "fgFwIppStatsBlockSize": fgFwIppStatsBlockSize,
       "fgFwIppStatsPortStart": fgFwIppStatsPortStart,
       "fgFwIppStatsPortEnd": fgFwIppStatsPortEnd,
       "fgFwIppStatsStartClientIP": fgFwIppStatsStartClientIP,
       "fgFwIppStatsEndClientIP": fgFwIppStatsEndClientIP,
       "fgFwIppStatsRscTCP": fgFwIppStatsRscTCP,
       "fgFwIppStatsRscUDP": fgFwIppStatsRscUDP,
       "fgFwIppStatsUsedRscTCP": fgFwIppStatsUsedRscTCP,
       "fgFwIppStatsUsedRscUDP": fgFwIppStatsUsedRscUDP,
       "fgFwIppStatsPercentageTCP": fgFwIppStatsPercentageTCP,
       "fgFwIppStatsPercentageUDP": fgFwIppStatsPercentageUDP,
       "fgFwIppTrapObjects": fgFwIppTrapObjects,
       "fgFwIppTrapType": fgFwIppTrapType,
       "fgFwTrapPoolUtilization": fgFwTrapPoolUtilization,
       "fgFwIppTrapPoolProto": fgFwIppTrapPoolProto,
       "fgFwGtp": fgFwGtp,
       "fgFwGtpStats": fgFwGtpStats,
       "fgFwGtpStatsRequest": fgFwGtpStatsRequest,
       "fgFwGtpStatsEchoRequest": fgFwGtpStatsEchoRequest,
       "fgFwGtpStatsTunnel": fgFwGtpStatsTunnel,
       "fgFwGtpStatsTunnelV0": fgFwGtpStatsTunnelV0,
       "fgFwGtpStatsPath": fgFwGtpStatsPath,
       "fgFwGtpStatsBearer": fgFwGtpStatsBearer,
       "fgFwGtpStatsFteid": fgFwGtpStatsFteid,
       "fgFwGtpStatsProfile": fgFwGtpStatsProfile,
       "fgFwGtpStatsImsi": fgFwGtpStatsImsi,
       "fgFwGtpStatsApn": fgFwGtpStatsApn,
       "fgFwGtpStatsApnShaper": fgFwGtpStatsApnShaper,
       "fgFwGtpStatsTunnelLimiter": fgFwGtpStatsTunnelLimiter,
       "fgFwGtpStatsAdvPolicies": fgFwGtpStatsAdvPolicies,
       "fgFwGtpStatsIeRemovePolicies": fgFwGtpStatsIeRemovePolicies,
       "fgFwGtpStatsIpPolicy": fgFwGtpStatsIpPolicy,
       "fgFwGtpStatsNoipPolicy": fgFwGtpStatsNoipPolicy,
       "fgFwGtpStatsIeWlEntry": fgFwGtpStatsIeWlEntry,
       "fgFwGtpStatsClash": fgFwGtpStatsClash,
       "fgFwGtpStatsDrop": fgFwGtpStatsDrop,
       "fgFwGtpRtStats": fgFwGtpRtStats,
       "fgFwGtpRtStatsCPkts": fgFwGtpRtStatsCPkts,
       "fgFwGtpRtStatsCForwarded": fgFwGtpRtStatsCForwarded,
       "fgFwGtpRtStatsCRejected": fgFwGtpRtStatsCRejected,
       "fgFwGtpRtStatsCDropped0": fgFwGtpRtStatsCDropped0,
       "fgFwGtpRtStatsCDropped1": fgFwGtpRtStatsCDropped1,
       "fgFwGtpRtStatsCDropped2": fgFwGtpRtStatsCDropped2,
       "fgFwGtpRtStatsCDropped3": fgFwGtpRtStatsCDropped3,
       "fgFwGtpRtStatsCDropped4": fgFwGtpRtStatsCDropped4,
       "fgFwGtpRtStatsCDropped5": fgFwGtpRtStatsCDropped5,
       "fgFwGtpRtStatsCDropped6": fgFwGtpRtStatsCDropped6,
       "fgFwGtpRtStatsCDropped7": fgFwGtpRtStatsCDropped7,
       "fgFwGtpRtStatsCDropped8": fgFwGtpRtStatsCDropped8,
       "fgFwGtpRtStatsCDropped9": fgFwGtpRtStatsCDropped9,
       "fgFwGtpRtStatsCDropped10": fgFwGtpRtStatsCDropped10,
       "fgFwGtpRtStatsCDropped11": fgFwGtpRtStatsCDropped11,
       "fgFwGtpRtStatsCDropped12": fgFwGtpRtStatsCDropped12,
       "fgFwGtpRtStatsCDropped13": fgFwGtpRtStatsCDropped13,
       "fgFwGtpRtStatsCDropped14": fgFwGtpRtStatsCDropped14,
       "fgFwGtpRtStatsCDropped15": fgFwGtpRtStatsCDropped15,
       "fgFwGtpRtStatsCDropped16": fgFwGtpRtStatsCDropped16,
       "fgFwGtpRtStatsCDropped17": fgFwGtpRtStatsCDropped17,
       "fgFwGtpRtStatsCDropped18": fgFwGtpRtStatsCDropped18,
       "fgFwGtpRtStatsCDropped19": fgFwGtpRtStatsCDropped19,
       "fgFwGtpRtStatsCDropped20": fgFwGtpRtStatsCDropped20,
       "fgFwGtpRtStatsCDropped21": fgFwGtpRtStatsCDropped21,
       "fgFwGtpRtStatsCDropped22": fgFwGtpRtStatsCDropped22,
       "fgFwGtpRtStatsCDropped23": fgFwGtpRtStatsCDropped23,
       "fgFwGtpRtStatsDPkts": fgFwGtpRtStatsDPkts,
       "fgFwGtpRtStatsDForwarded": fgFwGtpRtStatsDForwarded,
       "fgFwGtpRtStatsDDroppedSanity": fgFwGtpRtStatsDDroppedSanity,
       "fgFwGtpRtStatsDDroppedMalMsg": fgFwGtpRtStatsDDroppedMalMsg,
       "fgFwGtpRtStatsDDroppedNoState": fgFwGtpRtStatsDDroppedNoState,
       "fgFwGtpRtStatsDDroppedMalIe": fgFwGtpRtStatsDDroppedMalIe,
       "fgFwGtpRtStatsDDroppedGtpInGtp": fgFwGtpRtStatsDDroppedGtpInGtp,
       "fgFwGtpRtStatsDDroppedSpoof": fgFwGtpRtStatsDDroppedSpoof,
       "fgFwGtpRtStatsDDroppedIpPol": fgFwGtpRtStatsDDroppedIpPol,
       "fgFwGtpRtStatsDDroppedMsgFilter": fgFwGtpRtStatsDDroppedMsgFilter,
       "fgFwGtpRtStatsDDroppedMsgRateLimit": fgFwGtpRtStatsDDroppedMsgRateLimit,
       "fgFwGtpRtStatsDDroppedUnknownVersion": fgFwGtpRtStatsDDroppedUnknownVersion,
       "fgFwGtpRtStatsBPkts": fgFwGtpRtStatsBPkts,
       "fgFwGtpRtStatsBForwarded": fgFwGtpRtStatsBForwarded,
       "fgFwGtpRtStatsBDroppedSanity": fgFwGtpRtStatsBDroppedSanity,
       "fgFwGtpRtStatsBDroppedMalMsg": fgFwGtpRtStatsBDroppedMalMsg,
       "fgFwGtpRtStatsBDroppedMalIe": fgFwGtpRtStatsBDroppedMalIe,
       "fgFwGtpRtStatsBDroppedMsgFilter": fgFwGtpRtStatsBDroppedMsgFilter,
       "fgFwAddresses": fgFwAddresses,
       "fgFwAddrTables": fgFwAddrTables,
       "fgFwAddrDynEmsTable": fgFwAddrDynEmsTable,
       "fgFwAddrDynEmsEntry": fgFwAddrDynEmsEntry,
       "fgFwAddrDynEmsID": fgFwAddrDynEmsID,
       "fgFwAddrDynEmsName": fgFwAddrDynEmsName,
       "fgFwAddrDynEmsAddresses": fgFwAddrDynEmsAddresses,
       "fgMgmt": fgMgmt,
       "fgFmTrapPrefix": fgFmTrapPrefix,
       "fgFmTrapDeployComplete": fgFmTrapDeployComplete,
       "fgFmTrapDeployInProgress": fgFmTrapDeployInProgress,
       "fgFmTrapConfChange": fgFmTrapConfChange,
       "fgFmTrapIfChange": fgFmTrapIfChange,
       "fgAdmin": fgAdmin,
       "fgAdminOptions": fgAdminOptions,
       "fgAdminIdleTimeout": fgAdminIdleTimeout,
       "fgAdminLcdProtection": fgAdminLcdProtection,
       "fgAdminTables": fgAdminTables,
       "fgAdminTable": fgAdminTable,
       "fgAdminEntry": fgAdminEntry,
       "fgAdminVdom": fgAdminVdom,
       "fgMgmtTrapObjects": fgMgmtTrapObjects,
       "fgManIfIp": fgManIfIp,
       "fgManIfMask": fgManIfMask,
       "fgManIfIp6": fgManIfIp6,
       "fgFazTrapType": fgFazTrapType,
       "fgIntf": fgIntf,
       "fgIntfInfo": fgIntfInfo,
       "fgIntfTables": fgIntfTables,
       "fgIntfTable": fgIntfTable,
       "fgIntfEntry": fgIntfEntry,
       "fgIntfEntVdom": fgIntfEntVdom,
       "fgIntfEntEstUpBandwidth": fgIntfEntEstUpBandwidth,
       "fgIntfEntEstDownBandwidth": fgIntfEntEstDownBandwidth,
       "fgIntfEntMeaUpBandwidth": fgIntfEntMeaUpBandwidth,
       "fgIntfEntMeaDownBandwidth": fgIntfEntMeaDownBandwidth,
       "fgIntfVlanTable": fgIntfVlanTable,
       "fgIntfVlanEntry": fgIntfVlanEntry,
       "fgIntfVlanName": fgIntfVlanName,
       "fgIntfVlanID": fgIntfVlanID,
       "fgIntfVlanPhyName": fgIntfVlanPhyName,
       "fgIntfVrrps": fgIntfVrrps,
       "fgIntfVrrpCount": fgIntfVrrpCount,
       "fgIntfVrrpTable": fgIntfVrrpTable,
       "fgIntfVrrpEntry": fgIntfVrrpEntry,
       "fgIntfVrrpEntIndex": fgIntfVrrpEntIndex,
       "fgIntfVrrpEntVrId": fgIntfVrrpEntVrId,
       "fgIntfVrrpEntGrpId": fgIntfVrrpEntGrpId,
       "fgIntfVrrpEntIfName": fgIntfVrrpEntIfName,
       "fgIntfVrrpEntState": fgIntfVrrpEntState,
       "fgIntfVrrpEntVrIp": fgIntfVrrpEntVrIp,
       "fgIntfVlanHbs": fgIntfVlanHbs,
       "fgIntfVlanHbCount": fgIntfVlanHbCount,
       "fgIntfVlanHbTable": fgIntfVlanHbTable,
       "fgIntfVlanHbEntry": fgIntfVlanHbEntry,
       "fgIntfVlanHbEntIndex": fgIntfVlanHbEntIndex,
       "fgIntfVlanHbEntIfName": fgIntfVlanHbEntIfName,
       "fgIntfVlanHbEntSerial": fgIntfVlanHbEntSerial,
       "fgIntfVlanHbEntState": fgIntfVlanHbEntState,
       "fgIntfBcs": fgIntfBcs,
       "fgIntfBcTable": fgIntfBcTable,
       "fgIntfBcEntry": fgIntfBcEntry,
       "fgIntfBcAllocatedBandwidth": fgIntfBcAllocatedBandwidth,
       "fgIntfBcGuaranteedBandwidth": fgIntfBcGuaranteedBandwidth,
       "fgIntfBcMaxBandwidth": fgIntfBcMaxBandwidth,
       "fgIntfBcCurrentBandwidth": fgIntfBcCurrentBandwidth,
       "fgIntfBcBytes": fgIntfBcBytes,
       "fgIntfBcDrops": fgIntfBcDrops,
       "fgIntfBcInTable": fgIntfBcInTable,
       "fgIntfBcInEntry": fgIntfBcInEntry,
       "fgIntfBcInAllocatedBandwidth": fgIntfBcInAllocatedBandwidth,
       "fgIntfBcInGuaranteedBandwidth": fgIntfBcInGuaranteedBandwidth,
       "fgIntfBcInMaxBandwidth": fgIntfBcInMaxBandwidth,
       "fgIntfBcInCurrentBandwidth": fgIntfBcInCurrentBandwidth,
       "fgIntfBcInBytes": fgIntfBcInBytes,
       "fgIntfBcInDrops": fgIntfBcInDrops,
       "fgIntfBcQTable": fgIntfBcQTable,
       "fgIntfBcQEntry": fgIntfBcQEntry,
       "fgIntfBcQPackets": fgIntfBcQPackets,
       "fgIntfBcQBytes": fgIntfBcQBytes,
       "fgIntfBcQPDrops": fgIntfBcQPDrops,
       "fgIntfBcQBDrops": fgIntfBcQBDrops,
       "fgIntfBcCfgTables": fgIntfBcCfgTables,
       "fgIntfBcCfgIfTable": fgIntfBcCfgIfTable,
       "fgIntfBcCfgIfEntry": fgIntfBcCfgIfEntry,
       "fgIntfBcCfgIfName": fgIntfBcCfgIfName,
       "fgIntfBcCfgIfEgressSProfile": fgIntfBcCfgIfEgressSProfile,
       "fgIntfBcCfgIfIngressSProfile": fgIntfBcCfgIfIngressSProfile,
       "fgIntfBcCfgIfEstUpBandwidth": fgIntfBcCfgIfEstUpBandwidth,
       "fgIntfBcCfgIfEstDownBandwidth": fgIntfBcCfgIfEstDownBandwidth,
       "fgIntfBcCfgIfInBandwidth": fgIntfBcCfgIfInBandwidth,
       "fgIntfBcCfgIfOutBandwidth": fgIntfBcCfgIfOutBandwidth,
       "fgIntfBcCfgSproTable": fgIntfBcCfgSproTable,
       "fgIntfBcCfgSproEntry": fgIntfBcCfgSproEntry,
       "fgIntfBcCfgSproID": fgIntfBcCfgSproID,
       "fgIntfBcCfgSproName": fgIntfBcCfgSproName,
       "fgIntfBcCfgSproType": fgIntfBcCfgSproType,
       "fgIntfBcCfgSproDefaultClassId": fgIntfBcCfgSproDefaultClassId,
       "fgIntfBcCfgSproClassNum": fgIntfBcCfgSproClassNum,
       "fgIntfBcCfgSentTable": fgIntfBcCfgSentTable,
       "fgIntfBcCfgSentEntry": fgIntfBcCfgSentEntry,
       "fgIntfBcCfgSentClassID": fgIntfBcCfgSentClassID,
       "fgIntfBcCfgSentClassName": fgIntfBcCfgSentClassName,
       "fgIntfBcCfgSentGuaranteedBandwidth": fgIntfBcCfgSentGuaranteedBandwidth,
       "fgIntfBcCfgSentMaxBandwidth": fgIntfBcCfgSentMaxBandwidth,
       "fgIntfBcCfgSpolTable": fgIntfBcCfgSpolTable,
       "fgIntfBcCfgSpolEntry": fgIntfBcCfgSpolEntry,
       "fgIntfBcCfgSpolID": fgIntfBcCfgSpolID,
       "fgIntfBcCfgSpolSrcaddr": fgIntfBcCfgSpolSrcaddr,
       "fgIntfBcCfgSpolDstaddr": fgIntfBcCfgSpolDstaddr,
       "fgIntfBcCfgSpolSvr": fgIntfBcCfgSpolSvr,
       "fgIntfBcCfgSpolComment": fgIntfBcCfgSpolComment,
       "fgIntfBcCfgSpolClassName": fgIntfBcCfgSpolClassName,
       "fgIntfTrapObjects": fgIntfTrapObjects,
       "fgIntfTrapType": fgIntfTrapType,
       "fgAntivirus": fgAntivirus,
       "fgAvInfo": fgAvInfo,
       "fgAvTables": fgAvTables,
       "fgAvStatsTable": fgAvStatsTable,
       "fgAvStatsEntry": fgAvStatsEntry,
       "fgAvVirusDetected": fgAvVirusDetected,
       "fgAvVirusBlocked": fgAvVirusBlocked,
       "fgAvHTTPVirusDetected": fgAvHTTPVirusDetected,
       "fgAvHTTPVirusBlocked": fgAvHTTPVirusBlocked,
       "fgAvSMTPVirusDetected": fgAvSMTPVirusDetected,
       "fgAvSMTPVirusBlocked": fgAvSMTPVirusBlocked,
       "fgAvPOP3VirusDetected": fgAvPOP3VirusDetected,
       "fgAvPOP3VirusBlocked": fgAvPOP3VirusBlocked,
       "fgAvIMAPVirusDetected": fgAvIMAPVirusDetected,
       "fgAvIMAPVirusBlocked": fgAvIMAPVirusBlocked,
       "fgAvFTPVirusDetected": fgAvFTPVirusDetected,
       "fgAvFTPVirusBlocked": fgAvFTPVirusBlocked,
       "fgAvIMVirusDetected": fgAvIMVirusDetected,
       "fgAvIMVirusBlocked": fgAvIMVirusBlocked,
       "fgAvNNTPVirusDetected": fgAvNNTPVirusDetected,
       "fgAvNNTPVirusBlocked": fgAvNNTPVirusBlocked,
       "fgAvOversizedDetected": fgAvOversizedDetected,
       "fgAvOversizedBlocked": fgAvOversizedBlocked,
       "fgAvMAPIVirusDetected": fgAvMAPIVirusDetected,
       "fgAvMAPIVirusBlocked": fgAvMAPIVirusBlocked,
       "fgAvSMBVirusDetected": fgAvSMBVirusDetected,
       "fgAvSMBVirusBlocked": fgAvSMBVirusBlocked,
       "fgAvTrapObjects": fgAvTrapObjects,
       "fgAvTrapVirName": fgAvTrapVirName,
       "fgIps": fgIps,
       "fgIpsInfo": fgIpsInfo,
       "fgIpsTables": fgIpsTables,
       "fgIpsStatsTable": fgIpsStatsTable,
       "fgIpsStatsEntry": fgIpsStatsEntry,
       "fgIpsIntrusionsDetected": fgIpsIntrusionsDetected,
       "fgIpsIntrusionsBlocked": fgIpsIntrusionsBlocked,
       "fgIpsCritSevDetections": fgIpsCritSevDetections,
       "fgIpsHighSevDetections": fgIpsHighSevDetections,
       "fgIpsMedSevDetections": fgIpsMedSevDetections,
       "fgIpsLowSevDetections": fgIpsLowSevDetections,
       "fgIpsInfoSevDetections": fgIpsInfoSevDetections,
       "fgIpsSignatureDetections": fgIpsSignatureDetections,
       "fgIpsAnomalyDetections": fgIpsAnomalyDetections,
       "fgIpsTrapObjects": fgIpsTrapObjects,
       "fgIpsTrapSigId": fgIpsTrapSigId,
       "fgIpsTrapSrcIp": fgIpsTrapSrcIp,
       "fgIpsTrapSigMsg": fgIpsTrapSigMsg,
       "fgApplications": fgApplications,
       "fgWebfilter": fgWebfilter,
       "fgWebfilterInfo": fgWebfilterInfo,
       "fgWebfilterTables": fgWebfilterTables,
       "fgWebfilterStatsTable": fgWebfilterStatsTable,
       "fgWebfilterStatsEntry": fgWebfilterStatsEntry,
       "fgWfHTTPBlocked": fgWfHTTPBlocked,
       "fgWfHTTPSBlocked": fgWfHTTPSBlocked,
       "fgWfHTTPURLBlocked": fgWfHTTPURLBlocked,
       "fgWfHTTPSURLBlocked": fgWfHTTPSURLBlocked,
       "fgWfActiveXBlocked": fgWfActiveXBlocked,
       "fgWfCookieBlocked": fgWfCookieBlocked,
       "fgWfAppletBlocked": fgWfAppletBlocked,
       "fgFortiGuardStatsTable": fgFortiGuardStatsTable,
       "fgFortiGuardStatsEntry": fgFortiGuardStatsEntry,
       "fgFgWfHTTPExamined": fgFgWfHTTPExamined,
       "fgFgWfHTTPSExamined": fgFgWfHTTPSExamined,
       "fgFgWfHTTPAllowed": fgFgWfHTTPAllowed,
       "fgFgWfHTTPSAllowed": fgFgWfHTTPSAllowed,
       "fgFgWfHTTPBlocked": fgFgWfHTTPBlocked,
       "fgFgWfHTTPSBlocked": fgFgWfHTTPSBlocked,
       "fgFgWfHTTPLogged": fgFgWfHTTPLogged,
       "fgFgWfHTTPSLogged": fgFgWfHTTPSLogged,
       "fgFgWfHTTPOverridden": fgFgWfHTTPOverridden,
       "fgFgWfHTTPSOverridden": fgFgWfHTTPSOverridden,
       "fgAppProxyHTTP": fgAppProxyHTTP,
       "fgApHTTPUpTime": fgApHTTPUpTime,
       "fgApHTTPMemUsage": fgApHTTPMemUsage,
       "fgApHTTPStatsTable": fgApHTTPStatsTable,
       "fgApHTTPStatsEntry": fgApHTTPStatsEntry,
       "fgApHTTPReqProcessed": fgApHTTPReqProcessed,
       "fgApHTTPConnections": fgApHTTPConnections,
       "fgApHTTPMaxConnections": fgApHTTPMaxConnections,
       "fgAppProxySMTP": fgAppProxySMTP,
       "fgApSMTPUpTime": fgApSMTPUpTime,
       "fgApSMTPMemUsage": fgApSMTPMemUsage,
       "fgApSMTPStatsTable": fgApSMTPStatsTable,
       "fgApSMTPStatsEntry": fgApSMTPStatsEntry,
       "fgApSMTPReqProcessed": fgApSMTPReqProcessed,
       "fgApSMTPSpamDetected": fgApSMTPSpamDetected,
       "fgApSMTPConnections": fgApSMTPConnections,
       "fgApSMTPMaxConnections": fgApSMTPMaxConnections,
       "fgAppProxyPOP3": fgAppProxyPOP3,
       "fgApPOP3UpTime": fgApPOP3UpTime,
       "fgApPOP3MemUsage": fgApPOP3MemUsage,
       "fgApPOP3StatsTable": fgApPOP3StatsTable,
       "fgApPOP3StatsEntry": fgApPOP3StatsEntry,
       "fgApPOP3ReqProcessed": fgApPOP3ReqProcessed,
       "fgApPOP3SpamDetected": fgApPOP3SpamDetected,
       "fgApPOP3Connections": fgApPOP3Connections,
       "fgApPOP3MaxConnections": fgApPOP3MaxConnections,
       "fgAppProxyIMAP": fgAppProxyIMAP,
       "fgApIMAPUpTime": fgApIMAPUpTime,
       "fgApIMAPMemUsage": fgApIMAPMemUsage,
       "fgApIMAPStatsTable": fgApIMAPStatsTable,
       "fgApIMAPStatsEntry": fgApIMAPStatsEntry,
       "fgApIMAPReqProcessed": fgApIMAPReqProcessed,
       "fgApIMAPSpamDetected": fgApIMAPSpamDetected,
       "fgApIMAPConnections": fgApIMAPConnections,
       "fgApIMAPMaxConnections": fgApIMAPMaxConnections,
       "fgAppProxyNNTP": fgAppProxyNNTP,
       "fgApNNTPUpTime": fgApNNTPUpTime,
       "fgApNNTPMemUsage": fgApNNTPMemUsage,
       "fgApNNTPStatsTable": fgApNNTPStatsTable,
       "fgApNNTPStatsEntry": fgApNNTPStatsEntry,
       "fgApNNTPReqProcessed": fgApNNTPReqProcessed,
       "fgApNNTPConnections": fgApNNTPConnections,
       "fgApNNTPMaxConnections": fgApNNTPMaxConnections,
       "fgAppProxyIM": fgAppProxyIM,
       "fgApIMUpTime": fgApIMUpTime,
       "fgApIMMemUsage": fgApIMMemUsage,
       "fgApIMStatsTable": fgApIMStatsTable,
       "fgApIMStatsEntry": fgApIMStatsEntry,
       "fgApIMReqProcessed": fgApIMReqProcessed,
       "fgAppProxySIP": fgAppProxySIP,
       "fgApSIPUpTime": fgApSIPUpTime,
       "fgApSIPMemUsage": fgApSIPMemUsage,
       "fgApSIPStatsTable": fgApSIPStatsTable,
       "fgApSIPStatsEntry": fgApSIPStatsEntry,
       "fgApSIPClientReg": fgApSIPClientReg,
       "fgApSIPCallHandling": fgApSIPCallHandling,
       "fgApSIPServices": fgApSIPServices,
       "fgApSIPOtherReq": fgApSIPOtherReq,
       "fgAppScanUnit": fgAppScanUnit,
       "fgAppSuNumber": fgAppSuNumber,
       "fgAppSuStatsTable": fgAppSuStatsTable,
       "fgAppSuStatsEntry": fgAppSuStatsEntry,
       "fgAppSuIndex": fgAppSuIndex,
       "fgAppSuFileScanned": fgAppSuFileScanned,
       "fgAppVoIP": fgAppVoIP,
       "fgAppVoIPStatsTable": fgAppVoIPStatsTable,
       "fgAppVoIPStatsEntry": fgAppVoIPStatsEntry,
       "fgAppVoIPConn": fgAppVoIPConn,
       "fgAppVoIPCallBlocked": fgAppVoIPCallBlocked,
       "fgAppP2P": fgAppP2P,
       "fgAppP2PStatsTable": fgAppP2PStatsTable,
       "fgAppP2PStatsEntry": fgAppP2PStatsEntry,
       "fgAppP2PConnBlocked": fgAppP2PConnBlocked,
       "fgAppP2PProtoTable": fgAppP2PProtoTable,
       "fgAppP2PProtoEntry": fgAppP2PProtoEntry,
       "fgAppP2PProtEntProto": fgAppP2PProtEntProto,
       "fgAppP2PProtEntBytes": fgAppP2PProtEntBytes,
       "fgAppP2PProtoEntLastReset": fgAppP2PProtoEntLastReset,
       "fgAppIM": fgAppIM,
       "fgAppIMStatsTable": fgAppIMStatsTable,
       "fgAppIMStatsEntry": fgAppIMStatsEntry,
       "fgAppIMMessages": fgAppIMMessages,
       "fgAppIMFileTransfered": fgAppIMFileTransfered,
       "fgAppIMFileTxBlocked": fgAppIMFileTxBlocked,
       "fgAppIMConnBlocked": fgAppIMConnBlocked,
       "fgAppProxyFTP": fgAppProxyFTP,
       "fgApFTPUpTime": fgApFTPUpTime,
       "fgApFTPMemUsage": fgApFTPMemUsage,
       "fgApFTPStatsTable": fgApFTPStatsTable,
       "fgApFTPStatsEntry": fgApFTPStatsEntry,
       "fgApFTPReqProcessed": fgApFTPReqProcessed,
       "fgApFTPConnections": fgApFTPConnections,
       "fgApFTPMaxConnections": fgApFTPMaxConnections,
       "fgAppExplicitProxy": fgAppExplicitProxy,
       "fgExplicitProxyInfo": fgExplicitProxyInfo,
       "fgExplicitProxyUpTime": fgExplicitProxyUpTime,
       "fgExplicitProxyMemUsage": fgExplicitProxyMemUsage,
       "fgExplicitProxyRequests": fgExplicitProxyRequests,
       "fgExplicitProxyStatsTable": fgExplicitProxyStatsTable,
       "fgExplicitProxyStatsEntry": fgExplicitProxyStatsEntry,
       "fgExplicitProxyUsers": fgExplicitProxyUsers,
       "fgExplicitProxySessions": fgExplicitProxySessions,
       "fgExplicitProxyScanStatsTable": fgExplicitProxyScanStatsTable,
       "fgExplicitProxyScanStatsEntry": fgExplicitProxyScanStatsEntry,
       "fgExplicitProxyScanStatsDisp": fgExplicitProxyScanStatsDisp,
       "fgExplicitProxyVirus": fgExplicitProxyVirus,
       "fgExplicitProxyBannedWords": fgExplicitProxyBannedWords,
       "fgExplicitProxyPolicy": fgExplicitProxyPolicy,
       "fgExplicitProxyOversized": fgExplicitProxyOversized,
       "fgExplicitProxyArchNest": fgExplicitProxyArchNest,
       "fgExplicitProxyArchSize": fgExplicitProxyArchSize,
       "fgExplicitProxyArchEncrypted": fgExplicitProxyArchEncrypted,
       "fgExplicitProxyArchMultiPart": fgExplicitProxyArchMultiPart,
       "fgExplicitProxyArchUnsupported": fgExplicitProxyArchUnsupported,
       "fgExplicitProxyArchBomb": fgExplicitProxyArchBomb,
       "fgExplicitProxyArchCorrupt": fgExplicitProxyArchCorrupt,
       "fgExplicitProxyScriptStatsTable": fgExplicitProxyScriptStatsTable,
       "fgExplicitProxyScriptStatsEntry": fgExplicitProxyScriptStatsEntry,
       "fgExplicitProxyFilteredApplets": fgExplicitProxyFilteredApplets,
       "fgExplicitProxyFilteredActiveX": fgExplicitProxyFilteredActiveX,
       "fgExplicitProxyFilteredJScript": fgExplicitProxyFilteredJScript,
       "fgExplicitProxyFilteredJS": fgExplicitProxyFilteredJS,
       "fgExplicitProxyFilteredVBS": fgExplicitProxyFilteredVBS,
       "fgExplicitProxyFilteredOthScript": fgExplicitProxyFilteredOthScript,
       "fgExplicitProxyFilterStatsTable": fgExplicitProxyFilterStatsTable,
       "fgExplicitProxyFilterStatsEntry": fgExplicitProxyFilterStatsEntry,
       "fgExplicitProxyBlockedDLP": fgExplicitProxyBlockedDLP,
       "fgExplicitProxyBlockedConType": fgExplicitProxyBlockedConType,
       "fgExplicitProxyExaminedURLs": fgExplicitProxyExaminedURLs,
       "fgExplicitProxyAllowedURLs": fgExplicitProxyAllowedURLs,
       "fgExplicitProxyBlockedURLs": fgExplicitProxyBlockedURLs,
       "fgExplicitProxyLoggedURLs": fgExplicitProxyLoggedURLs,
       "fgExplicitProxyOverriddenURLs": fgExplicitProxyOverriddenURLs,
       "fgAppWebCache": fgAppWebCache,
       "fgWebCacheInfo": fgWebCacheInfo,
       "fgWebCacheRAMLimit": fgWebCacheRAMLimit,
       "fgWebCacheRAMUsage": fgWebCacheRAMUsage,
       "fgWebCacheRAMHits": fgWebCacheRAMHits,
       "fgWebCacheRAMMisses": fgWebCacheRAMMisses,
       "fgWebCacheRequests": fgWebCacheRequests,
       "fgWebCacheBypass": fgWebCacheBypass,
       "fgWebCacheUpTime": fgWebCacheUpTime,
       "fgWebCacheDiskStatsTable": fgWebCacheDiskStatsTable,
       "fgWebCacheDiskStatsEntry": fgWebCacheDiskStatsEntry,
       "fgWebCacheDisk": fgWebCacheDisk,
       "fgWebCacheDiskLimit": fgWebCacheDiskLimit,
       "fgWebCacheDiskUsage": fgWebCacheDiskUsage,
       "fgWebCacheDiskHits": fgWebCacheDiskHits,
       "fgWebCacheDiskMisses": fgWebCacheDiskMisses,
       "fgWebCacheDiskFailure": fgWebCacheDiskFailure,
       "fgAppWanOpt": fgAppWanOpt,
       "fgWanOptInfo": fgWanOptInfo,
       "fgMemCacheLimit": fgMemCacheLimit,
       "fgMemCacheUsage": fgMemCacheUsage,
       "fgMemCacheHits": fgMemCacheHits,
       "fgMemCacheMisses": fgMemCacheMisses,
       "fgByteCacheRAMLimit": fgByteCacheRAMLimit,
       "fgByteCacheRAMUsage": fgByteCacheRAMUsage,
       "fgWanOptUpTime": fgWanOptUpTime,
       "fgWanOptStatsTable": fgWanOptStatsTable,
       "fgWanOptStatsEntry": fgWanOptStatsEntry,
       "fgWanOptTunnels": fgWanOptTunnels,
       "fgWanOptLANBytesIn": fgWanOptLANBytesIn,
       "fgWanOptLANBytesOut": fgWanOptLANBytesOut,
       "fgWanOptWANBytesIn": fgWanOptWANBytesIn,
       "fgWanOptWANBytesOut": fgWanOptWANBytesOut,
       "fgWanOptHistoryStatsTable": fgWanOptHistoryStatsTable,
       "fgWanOptHistoryStatsEntry": fgWanOptHistoryStatsEntry,
       "fgWanOptHistPeriod": fgWanOptHistPeriod,
       "fgWanOptProtocol": fgWanOptProtocol,
       "fgWanOptReductionRate": fgWanOptReductionRate,
       "fgWanOptLanTraffic": fgWanOptLanTraffic,
       "fgWanOptWanTraffic": fgWanOptWanTraffic,
       "fgWanOptTrafficStatsTable": fgWanOptTrafficStatsTable,
       "fgWanOptTrafficStatsEntry": fgWanOptTrafficStatsEntry,
       "fgWanOptLanInTraffic": fgWanOptLanInTraffic,
       "fgWanOptLanOutTraffic": fgWanOptLanOutTraffic,
       "fgWanOptWanInTraffic": fgWanOptWanInTraffic,
       "fgWanOptWanOutTraffic": fgWanOptWanOutTraffic,
       "fgWanOptDiskStatsTable": fgWanOptDiskStatsTable,
       "fgWanOptDiskStatsEntry": fgWanOptDiskStatsEntry,
       "fgWanOptDisk": fgWanOptDisk,
       "fgWanOptDiskLimit": fgWanOptDiskLimit,
       "fgWanOptDiskUsage": fgWanOptDiskUsage,
       "fgWanOptDiskHits": fgWanOptDiskHits,
       "fgWanOptDiskMisses": fgWanOptDiskMisses,
       "fgWanOptDiskFailure": fgWanOptDiskFailure,
       "fgAppDNSProxy": fgAppDNSProxy,
       "fgDNSProxyStatsInfo": fgDNSProxyStatsInfo,
       "fgDNSProxyStatsUdpCacheHit": fgDNSProxyStatsUdpCacheHit,
       "fgDNSProxyStatsUdpRatingCacheHit": fgDNSProxyStatsUdpRatingCacheHit,
       "fgDNSProxyStatsUdpReq": fgDNSProxyStatsUdpReq,
       "fgDNSProxyStatsUdpRes": fgDNSProxyStatsUdpRes,
       "fgDNSProxyStatsUdpFwd": fgDNSProxyStatsUdpFwd,
       "fgDNSProxyStatsUdpRetrans": fgDNSProxyStatsUdpRetrans,
       "fgDNSProxyStatsUdpTo": fgDNSProxyStatsUdpTo,
       "fgDNSProxyStatsUdpFtgRes": fgDNSProxyStatsUdpFtgRes,
       "fgDNSProxyStatsUdpFtgFwd": fgDNSProxyStatsUdpFtgFwd,
       "fgDNSProxyStatsUdpFtgRetrans": fgDNSProxyStatsUdpFtgRetrans,
       "fgAppFnbam": fgAppFnbam,
       "fgAppFnbamStatsInfo": fgAppFnbamStatsInfo,
       "fgAppFnbamStatsTotalAuthReqs": fgAppFnbamStatsTotalAuthReqs,
       "fgAppFnbamStatsTotalEagainErrs": fgAppFnbamStatsTotalEagainErrs,
       "fgAppFnbamStatsTotalLdapFails": fgAppFnbamStatsTotalLdapFails,
       "fgInetProto": fgInetProto,
       "fgInetProtoInfo": fgInetProtoInfo,
       "fgInetProtoTables": fgInetProtoTables,
       "fgIpSessTable": fgIpSessTable,
       "fgIpSessEntry": fgIpSessEntry,
       "fgIpSessIndex": fgIpSessIndex,
       "fgIpSessProto": fgIpSessProto,
       "fgIpSessFromAddr": fgIpSessFromAddr,
       "fgIpSessFromPort": fgIpSessFromPort,
       "fgIpSessToAddr": fgIpSessToAddr,
       "fgIpSessToPort": fgIpSessToPort,
       "fgIpSessExp": fgIpSessExp,
       "fgIpSessVdom": fgIpSessVdom,
       "fgIpSessStatsTable": fgIpSessStatsTable,
       "fgIpSessStatsEntry": fgIpSessStatsEntry,
       "fgIpSessNumber": fgIpSessNumber,
       "fgIp6SessStatsTable": fgIp6SessStatsTable,
       "fgIp6SessStatsEntry": fgIp6SessStatsEntry,
       "fgIp6SessNumber": fgIp6SessNumber,
       "fgVpn": fgVpn,
       "fgVpnInfo": fgVpnInfo,
       "fgVpnTunnelUpCount": fgVpnTunnelUpCount,
       "fgVpnTables": fgVpnTables,
       "fgVpnDialupTable": fgVpnDialupTable,
       "fgVpnDialupEntry": fgVpnDialupEntry,
       "fgVpnDialupIndex": fgVpnDialupIndex,
       "fgVpnDialupGateway": fgVpnDialupGateway,
       "fgVpnDialupLifetime": fgVpnDialupLifetime,
       "fgVpnDialupTimeout": fgVpnDialupTimeout,
       "fgVpnDialupSrcBegin": fgVpnDialupSrcBegin,
       "fgVpnDialupSrcEnd": fgVpnDialupSrcEnd,
       "fgVpnDialupDstAddr": fgVpnDialupDstAddr,
       "fgVpnDialupVdom": fgVpnDialupVdom,
       "fgVpnDialupInOctets": fgVpnDialupInOctets,
       "fgVpnDialupOutOctets": fgVpnDialupOutOctets,
       "fgVpnTunTable": fgVpnTunTable,
       "fgVpnTunEntry": fgVpnTunEntry,
       "fgVpnTunEntIndex": fgVpnTunEntIndex,
       "fgVpnTunEntPhase1Name": fgVpnTunEntPhase1Name,
       "fgVpnTunEntPhase2Name": fgVpnTunEntPhase2Name,
       "fgVpnTunEntRemGwyIp": fgVpnTunEntRemGwyIp,
       "fgVpnTunEntRemGwyPort": fgVpnTunEntRemGwyPort,
       "fgVpnTunEntLocGwyIp": fgVpnTunEntLocGwyIp,
       "fgVpnTunEntLocGwyPort": fgVpnTunEntLocGwyPort,
       "fgVpnTunEntSelectorSrcBeginIp": fgVpnTunEntSelectorSrcBeginIp,
       "fgVpnTunEntSelectorSrcEndIp": fgVpnTunEntSelectorSrcEndIp,
       "fgVpnTunEntSelectorSrcPort": fgVpnTunEntSelectorSrcPort,
       "fgVpnTunEntSelectorDstBeginIp": fgVpnTunEntSelectorDstBeginIp,
       "fgVpnTunEntSelectorDstEndIp": fgVpnTunEntSelectorDstEndIp,
       "fgVpnTunEntSelectorDstPort": fgVpnTunEntSelectorDstPort,
       "fgVpnTunEntSelectorProto": fgVpnTunEntSelectorProto,
       "fgVpnTunEntLifeSecs": fgVpnTunEntLifeSecs,
       "fgVpnTunEntLifeBytes": fgVpnTunEntLifeBytes,
       "fgVpnTunEntTimeout": fgVpnTunEntTimeout,
       "fgVpnTunEntInOctets": fgVpnTunEntInOctets,
       "fgVpnTunEntOutOctets": fgVpnTunEntOutOctets,
       "fgVpnTunEntStatus": fgVpnTunEntStatus,
       "fgVpnTunEntVdom": fgVpnTunEntVdom,
       "fgVpnTunEntPhase2Index": fgVpnTunEntPhase2Index,
       "fgVpnSslStatsTable": fgVpnSslStatsTable,
       "fgVpnSslStatsEntry": fgVpnSslStatsEntry,
       "fgVpnSslState": fgVpnSslState,
       "fgVpnSslStatsLoginUsers": fgVpnSslStatsLoginUsers,
       "fgVpnSslStatsMaxUsers": fgVpnSslStatsMaxUsers,
       "fgVpnSslStatsActiveWebSessions": fgVpnSslStatsActiveWebSessions,
       "fgVpnSslStatsMaxWebSessions": fgVpnSslStatsMaxWebSessions,
       "fgVpnSslStatsActiveTunnels": fgVpnSslStatsActiveTunnels,
       "fgVpnSslStatsMaxTunnels": fgVpnSslStatsMaxTunnels,
       "fgVpnSslTunnelTable": fgVpnSslTunnelTable,
       "fgVpnSslTunnelEntry": fgVpnSslTunnelEntry,
       "fgVpnSslTunnelIndex": fgVpnSslTunnelIndex,
       "fgVpnSslTunnelVdom": fgVpnSslTunnelVdom,
       "fgVpnSslTunnelUserName": fgVpnSslTunnelUserName,
       "fgVpnSslTunnelSrcIp": fgVpnSslTunnelSrcIp,
       "fgVpnSslTunnelIp": fgVpnSslTunnelIp,
       "fgVpnSslTunnelUpTime": fgVpnSslTunnelUpTime,
       "fgVpnSslTunnelBytesIn": fgVpnSslTunnelBytesIn,
       "fgVpnSslTunnelBytesOut": fgVpnSslTunnelBytesOut,
       "fgVpnTrapObjects": fgVpnTrapObjects,
       "fgVpnTrapLocalGateway": fgVpnTrapLocalGateway,
       "fgVpnTrapRemoteGateway": fgVpnTrapRemoteGateway,
       "fgVpnTrapPhase1Name": fgVpnTrapPhase1Name,
       "fgVpn2Tables": fgVpn2Tables,
       "fgVpn2DialupTable": fgVpn2DialupTable,
       "fgVpn2DialupEntry": fgVpn2DialupEntry,
       "fgVpn2DialupIndex": fgVpn2DialupIndex,
       "fgVpn2DialupGatewayType": fgVpn2DialupGatewayType,
       "fgVpn2DialupGateway": fgVpn2DialupGateway,
       "fgVpn2DialupLifetime": fgVpn2DialupLifetime,
       "fgVpn2DialupTimeout": fgVpn2DialupTimeout,
       "fgVpn2DialupSrcBeginType": fgVpn2DialupSrcBeginType,
       "fgVpn2DialupSrcBegin": fgVpn2DialupSrcBegin,
       "fgVpn2DialupSrcEndType": fgVpn2DialupSrcEndType,
       "fgVpn2DialupSrcEnd": fgVpn2DialupSrcEnd,
       "fgVpn2DialupDstBeginType": fgVpn2DialupDstBeginType,
       "fgVpn2DialupDstBegin": fgVpn2DialupDstBegin,
       "fgVpn2DialupDstEndType": fgVpn2DialupDstEndType,
       "fgVpn2DialupDstEnd": fgVpn2DialupDstEnd,
       "fgVpn2DialupInOctets": fgVpn2DialupInOctets,
       "fgVpn2DialupOutOctets": fgVpn2DialupOutOctets,
       "fgVpn2DialupPhase1Name": fgVpn2DialupPhase1Name,
       "fgVpn2DialupVdom": fgVpn2DialupVdom,
       "fgVpn2TunTable": fgVpn2TunTable,
       "fgVpn2TunEntry": fgVpn2TunEntry,
       "fgVpn2TunIndex": fgVpn2TunIndex,
       "fgVpn2TunPhase1Name": fgVpn2TunPhase1Name,
       "fgVpn2TunPhase2Name": fgVpn2TunPhase2Name,
       "fgVpn2TunRemGwyIpType": fgVpn2TunRemGwyIpType,
       "fgVpn2TunRemGwyIp": fgVpn2TunRemGwyIp,
       "fgVpn2TunRemGwyPort": fgVpn2TunRemGwyPort,
       "fgVpn2TunLocGwyIpType": fgVpn2TunLocGwyIpType,
       "fgVpn2TunLocGwyIp": fgVpn2TunLocGwyIp,
       "fgVpn2TunLocGwyPort": fgVpn2TunLocGwyPort,
       "fgVpn2TunSelSrcBeginIpType": fgVpn2TunSelSrcBeginIpType,
       "fgVpn2TunSelSrcBeginIp": fgVpn2TunSelSrcBeginIp,
       "fgVpn2TunSelSrcEndIpType": fgVpn2TunSelSrcEndIpType,
       "fgVpn2TunSelSrcEndIp": fgVpn2TunSelSrcEndIp,
       "fgVpn2TunSelSrcPort": fgVpn2TunSelSrcPort,
       "fgVpn2TunSelDstBeginIpType": fgVpn2TunSelDstBeginIpType,
       "fgVpn2TunSelDstBeginIp": fgVpn2TunSelDstBeginIp,
       "fgVpn2TunSelDstEndIpType": fgVpn2TunSelDstEndIpType,
       "fgVpn2TunSelDstEndIp": fgVpn2TunSelDstEndIp,
       "fgVpn2TunSelDstPort": fgVpn2TunSelDstPort,
       "fgVpn2TunSelProto": fgVpn2TunSelProto,
       "fgVpn2TunLifeSecs": fgVpn2TunLifeSecs,
       "fgVpn2TunLifeBytes": fgVpn2TunLifeBytes,
       "fgVpn2TunTimeout": fgVpn2TunTimeout,
       "fgVpn2TunInOctets": fgVpn2TunInOctets,
       "fgVpn2TunOutOctets": fgVpn2TunOutOctets,
       "fgVpn2TunStatus": fgVpn2TunStatus,
       "fgVpn2TunVdom": fgVpn2TunVdom,
       "fgVpn2TunPhase2Index": fgVpn2TunPhase2Index,
       "fgHighAvailability": fgHighAvailability,
       "fgHaInfo": fgHaInfo,
       "fgHaSystemMode": fgHaSystemMode,
       "fgHaGroupId": fgHaGroupId,
       "fgHaPriority": fgHaPriority,
       "fgHaOverride": fgHaOverride,
       "fgHaAutoSync": fgHaAutoSync,
       "fgHaSchedule": fgHaSchedule,
       "fgHaGroupName": fgHaGroupName,
       "fgHaTables": fgHaTables,
       "fgHaStatsTable": fgHaStatsTable,
       "fgHaStatsEntry": fgHaStatsEntry,
       "fgHaStatsIndex": fgHaStatsIndex,
       "fgHaStatsSerial": fgHaStatsSerial,
       "fgHaStatsCpuUsage": fgHaStatsCpuUsage,
       "fgHaStatsMemUsage": fgHaStatsMemUsage,
       "fgHaStatsNetUsage": fgHaStatsNetUsage,
       "fgHaStatsSesCount": fgHaStatsSesCount,
       "fgHaStatsPktCount": fgHaStatsPktCount,
       "fgHaStatsByteCount": fgHaStatsByteCount,
       "fgHaStatsIdsCount": fgHaStatsIdsCount,
       "fgHaStatsAvCount": fgHaStatsAvCount,
       "fgHaStatsHostname": fgHaStatsHostname,
       "fgHaStatsSyncStatus": fgHaStatsSyncStatus,
       "fgHaStatsSyncDatimeSucc": fgHaStatsSyncDatimeSucc,
       "fgHaStatsSyncDatimeUnsucc": fgHaStatsSyncDatimeUnsucc,
       "fgHaStatsGlobalChecksum": fgHaStatsGlobalChecksum,
       "fgHaStatsPrimarySerial": fgHaStatsPrimarySerial,
       "fgHaStatsAllChecksum": fgHaStatsAllChecksum,
       "fgHaTrapObjects": fgHaTrapObjects,
       "fgHaTrapMemberSerial": fgHaTrapMemberSerial,
       "fgWc": fgWc,
       "fgWcTrapObjects": fgWcTrapObjects,
       "fgWcApVdom": fgWcApVdom,
       "fgWcApSerial": fgWcApSerial,
       "fgWcApName": fgWcApName,
       "fgWcInfo": fgWcInfo,
       "fgWcInfoName": fgWcInfoName,
       "fgWcInfoLocation": fgWcInfoLocation,
       "fgWcInfoWtpCapacity": fgWcInfoWtpCapacity,
       "fgWcInfoWtpManaged": fgWcInfoWtpManaged,
       "fgWcInfoWtpSessions": fgWcInfoWtpSessions,
       "fgWcInfoStationCapacity": fgWcInfoStationCapacity,
       "fgWcInfoStationCount": fgWcInfoStationCount,
       "fgWcWlanTable": fgWcWlanTable,
       "fgWcWlanEntry": fgWcWlanEntry,
       "fgWcWlanSsid": fgWcWlanSsid,
       "fgWcWlanBroadcastSsid": fgWcWlanBroadcastSsid,
       "fgWcWlanSecurity": fgWcWlanSecurity,
       "fgWcWlanEncryption": fgWcWlanEncryption,
       "fgWcWlanAuthentication": fgWcWlanAuthentication,
       "fgWcWlanRadiusServer": fgWcWlanRadiusServer,
       "fgWcWlanUserGroup": fgWcWlanUserGroup,
       "fgWcWlanLocalBridging": fgWcWlanLocalBridging,
       "fgWcWlanVlanId": fgWcWlanVlanId,
       "fgWcWlanMeshBackhaul": fgWcWlanMeshBackhaul,
       "fgWcWlanStationCapacity": fgWcWlanStationCapacity,
       "fgWcWlanStationCount": fgWcWlanStationCount,
       "fgWcWlanCPAuth": fgWcWlanCPAuth,
       "fgWcWtpTables": fgWcWtpTables,
       "fgWcWtpProfileTable": fgWcWtpProfileTable,
       "fgWcWtpProfileEntry": fgWcWtpProfileEntry,
       "fgWcWtpProfileName": fgWcWtpProfileName,
       "fgWcWtpProfilePlatform": fgWcWtpProfilePlatform,
       "fgWcWtpProfileDataChannelDtlsPolicy": fgWcWtpProfileDataChannelDtlsPolicy,
       "fgWcWtpProfileCountryString": fgWcWtpProfileCountryString,
       "fgWcWtpProfileRadioTable": fgWcWtpProfileRadioTable,
       "fgWcWtpProfileRadioEntry": fgWcWtpProfileRadioEntry,
       "fgWcWtpProfileRadioProfileName": fgWcWtpProfileRadioProfileName,
       "fgWcWtpProfileRadioRadioId": fgWcWtpProfileRadioRadioId,
       "fgWcWtpProfileRadioMode": fgWcWtpProfileRadioMode,
       "fgWcWtpProfileRadioApScan": fgWcWtpProfileRadioApScan,
       "fgWcWtpProfileRadioWidsProfile": fgWcWtpProfileRadioWidsProfile,
       "fgWcWtpProfileRadioDarrp": fgWcWtpProfileRadioDarrp,
       "fgWcWtpProfileRadioFrequencyHandoff": fgWcWtpProfileRadioFrequencyHandoff,
       "fgWcWtpProfileRadioApHandoff": fgWcWtpProfileRadioApHandoff,
       "fgWcWtpProfileRadioBeaconInterval": fgWcWtpProfileRadioBeaconInterval,
       "fgWcWtpProfileRadioDtimPeriod": fgWcWtpProfileRadioDtimPeriod,
       "fgWcWtpProfileRadioBand": fgWcWtpProfileRadioBand,
       "fgWcWtpProfileRadioChannelBonding": fgWcWtpProfileRadioChannelBonding,
       "fgWcWtpProfileRadioChannel": fgWcWtpProfileRadioChannel,
       "fgWcWtpProfileRadioAutoTxPowerControl": fgWcWtpProfileRadioAutoTxPowerControl,
       "fgWcWtpProfileRadioAutoTxPowerLow": fgWcWtpProfileRadioAutoTxPowerLow,
       "fgWcWtpProfileRadioAutoTxPowerHigh": fgWcWtpProfileRadioAutoTxPowerHigh,
       "fgWcWtpProfileRadioTxPowerLevel": fgWcWtpProfileRadioTxPowerLevel,
       "fgWcWtpProfileRadioVaps": fgWcWtpProfileRadioVaps,
       "fgWcWtpProfileRadioStationCapacity": fgWcWtpProfileRadioStationCapacity,
       "fgWcWtpProfileRadioChannelWidth": fgWcWtpProfileRadioChannelWidth,
       "fgWcWtpConfigTable": fgWcWtpConfigTable,
       "fgWcWtpConfigEntry": fgWcWtpConfigEntry,
       "fgWcWtpConfigWtpId": fgWcWtpConfigWtpId,
       "fgWcWtpConfigWtpAdmin": fgWcWtpConfigWtpAdmin,
       "fgWcWtpConfigWtpName": fgWcWtpConfigWtpName,
       "fgWcWtpConfigWtpLocation": fgWcWtpConfigWtpLocation,
       "fgWcWtpConfigWtpProfile": fgWcWtpConfigWtpProfile,
       "fgWcWtpConfigRadioEnable": fgWcWtpConfigRadioEnable,
       "fgWcWtpConfigRadioAutoTxPowerControl": fgWcWtpConfigRadioAutoTxPowerControl,
       "fgWcWtpConfigRadioAutoTxPowerLow": fgWcWtpConfigRadioAutoTxPowerLow,
       "fgWcWtpConfigRadioAutoTxPowerHigh": fgWcWtpConfigRadioAutoTxPowerHigh,
       "fgWcWtpConfigRadioTxPowerLevel": fgWcWtpConfigRadioTxPowerLevel,
       "fgWcWtpConfigRadioBand": fgWcWtpConfigRadioBand,
       "fgWcWtpConfigRadioApScan": fgWcWtpConfigRadioApScan,
       "fgWcWtpConfigVapAll": fgWcWtpConfigVapAll,
       "fgWcWtpConfigVaps": fgWcWtpConfigVaps,
       "fgWcWtpSessionTable": fgWcWtpSessionTable,
       "fgWcWtpSessionEntry": fgWcWtpSessionEntry,
       "fgWcWtpSessionWtpId": fgWcWtpSessionWtpId,
       "fgWcWtpSessionWtpIpAddressType": fgWcWtpSessionWtpIpAddressType,
       "fgWcWtpSessionWtpIpAddress": fgWcWtpSessionWtpIpAddress,
       "fgWcWtpSessionWtpLocalIpAddressType": fgWcWtpSessionWtpLocalIpAddressType,
       "fgWcWtpSessionWtpLocalIpAddress": fgWcWtpSessionWtpLocalIpAddress,
       "fgWcWtpSessionWtpBaseMacAddress": fgWcWtpSessionWtpBaseMacAddress,
       "fgWcWtpSessionConnectionState": fgWcWtpSessionConnectionState,
       "fgWcWtpSessionWtpUpTime": fgWcWtpSessionWtpUpTime,
       "fgWcWtpSessionWtpDaemonUpTime": fgWcWtpSessionWtpDaemonUpTime,
       "fgWcWtpSessionWtpSessionUpTime": fgWcWtpSessionWtpSessionUpTime,
       "fgWcWtpSessionWtpProfileName": fgWcWtpSessionWtpProfileName,
       "fgWcWtpSessionWtpModelNumber": fgWcWtpSessionWtpModelNumber,
       "fgWcWtpSessionWtpHwVersion": fgWcWtpSessionWtpHwVersion,
       "fgWcWtpSessionWtpSwVersion": fgWcWtpSessionWtpSwVersion,
       "fgWcWtpSessionWtpBootVersion": fgWcWtpSessionWtpBootVersion,
       "fgWcWtpSessionWtpRegionCode": fgWcWtpSessionWtpRegionCode,
       "fgWcWtpSessionWtpStationCount": fgWcWtpSessionWtpStationCount,
       "fgWcWtpSessionWtpByteRxCount": fgWcWtpSessionWtpByteRxCount,
       "fgWcWtpSessionWtpByteTxCount": fgWcWtpSessionWtpByteTxCount,
       "fgWcWtpSessionWtpCpuUsage": fgWcWtpSessionWtpCpuUsage,
       "fgWcWtpSessionWtpMemoryUsage": fgWcWtpSessionWtpMemoryUsage,
       "fgWcWtpSessionWtpMemoryCapacity": fgWcWtpSessionWtpMemoryCapacity,
       "fgWcWtpSessionRadioTable": fgWcWtpSessionRadioTable,
       "fgWcWtpSessionRadioEntry": fgWcWtpSessionRadioEntry,
       "fgWcWtpSessionRadioWtpId": fgWcWtpSessionRadioWtpId,
       "fgWcWtpSessionRadioRadioId": fgWcWtpSessionRadioRadioId,
       "fgWcWtpSessionRadioMode": fgWcWtpSessionRadioMode,
       "fgWcWtpSessionRadioBaseBssid": fgWcWtpSessionRadioBaseBssid,
       "fgWcWtpSessionRadioCountryString": fgWcWtpSessionRadioCountryString,
       "fgWcWtpSessionRadioCountryCode": fgWcWtpSessionRadioCountryCode,
       "fgWcWtpSessionRadioOperatingChannel": fgWcWtpSessionRadioOperatingChannel,
       "fgWcWtpSessionRadioOperatingPower": fgWcWtpSessionRadioOperatingPower,
       "fgWcWtpSessionRadioStationCount": fgWcWtpSessionRadioStationCount,
       "fgWcWtpSessionVapTable": fgWcWtpSessionVapTable,
       "fgWcWtpSessionVapEntry": fgWcWtpSessionVapEntry,
       "fgWcWtpSessionVapWtpId": fgWcWtpSessionVapWtpId,
       "fgWcWtpSessionVapRadioId": fgWcWtpSessionVapRadioId,
       "fgWcWtpSessionVapSsid": fgWcWtpSessionVapSsid,
       "fgWcWtpSessionVapStationCount": fgWcWtpSessionVapStationCount,
       "fgWcWtpSessionVapByteRxCount": fgWcWtpSessionVapByteRxCount,
       "fgWcWtpSessionVapByteTxCount": fgWcWtpSessionVapByteTxCount,
       "fgWcStaTable": fgWcStaTable,
       "fgWcStaEntry": fgWcStaEntry,
       "fgWcStaMacAddress": fgWcStaMacAddress,
       "fgWcStaWlan": fgWcStaWlan,
       "fgWcStaWtpId": fgWcStaWtpId,
       "fgWcStaRadioId": fgWcStaRadioId,
       "fgWcStaVlanId": fgWcStaVlanId,
       "fgWcStaIpAddressType": fgWcStaIpAddressType,
       "fgWcStaIpAddress": fgWcStaIpAddress,
       "fgWcStaVci": fgWcStaVci,
       "fgWcStaHost": fgWcStaHost,
       "fgWcStaUser": fgWcStaUser,
       "fgWcStaGroup": fgWcStaGroup,
       "fgWcStaSignal": fgWcStaSignal,
       "fgWcStaNoise": fgWcStaNoise,
       "fgWcStaIdle": fgWcStaIdle,
       "fgWcStaBandwidthTx": fgWcStaBandwidthTx,
       "fgWcStaBandwidthRx": fgWcStaBandwidthRx,
       "fgWcStaChannel": fgWcStaChannel,
       "fgWcStaRadioType": fgWcStaRadioType,
       "fgWcStaSecurity": fgWcStaSecurity,
       "fgWcStaEncrypt": fgWcStaEncrypt,
       "fgWcStaOnline": fgWcStaOnline,
       "fgWcStaCPAuth": fgWcStaCPAuth,
       "fgFc": fgFc,
       "fgFcTrapObjects": fgFcTrapObjects,
       "fgFcSwVdom": fgFcSwVdom,
       "fgFcSwSerial": fgFcSwSerial,
       "fgFcSwName": fgFcSwName,
       "fgServerLoadBalance": fgServerLoadBalance,
       "fgServerLoadBalanceTrapObjects": fgServerLoadBalanceTrapObjects,
       "fgServerLoadBalanceRealServerAddress": fgServerLoadBalanceRealServerAddress,
       "fgServerLoadBalanceVirtualServerName": fgServerLoadBalanceVirtualServerName,
       "fgServerLoadBalanceRealServerAddress6": fgServerLoadBalanceRealServerAddress6,
       "fgUsbModemInfo": fgUsbModemInfo,
       "fgUsbModemInfoObjects": fgUsbModemInfoObjects,
       "fgUsbModemSignalStrength": fgUsbModemSignalStrength,
       "fgUsbModemStatus": fgUsbModemStatus,
       "fgUsbModemSimState": fgUsbModemSimState,
       "fgUsbModemVendor": fgUsbModemVendor,
       "fgUsbModemProduct": fgUsbModemProduct,
       "fgUsbModemNetwork": fgUsbModemNetwork,
       "fgUsbModemId": fgUsbModemId,
       "fgUsbModemSimId": fgUsbModemSimId,
       "fgDevice": fgDevice,
       "fgDeviceTrapObjects": fgDeviceTrapObjects,
       "fgDeviceMacAddress": fgDeviceMacAddress,
       "fgDeviceCreated": fgDeviceCreated,
       "fgDeviceLastSeen": fgDeviceLastSeen,
       "fgInternalLTEModemsInfo": fgInternalLTEModemsInfo,
       "fgMdmInfoTable": fgMdmInfoTable,
       "fgMdmInfoEntry": fgMdmInfoEntry,
       "fgMdmEntIndex": fgMdmEntIndex,
       "fgMdmDetected": fgMdmDetected,
       "fgMdmVendor": fgMdmVendor,
       "fgMdmModel": fgMdmModel,
       "fgMdmRevision": fgMdmRevision,
       "fgMdmMsisdn": fgMdmMsisdn,
       "fgMdmEsn": fgMdmEsn,
       "fgMdmImei": fgMdmImei,
       "fgMdmHwRevision": fgMdmHwRevision,
       "fgMdmMeid": fgMdmMeid,
       "fgMdmSwRev": fgMdmSwRev,
       "fgMdmSku": fgMdmSku,
       "fgMdmFsn": fgMdmFsn,
       "fgMdmPrlVer": fgMdmPrlVer,
       "fgMdmFwVer": fgMdmFwVer,
       "fgMdmPriFwVer": fgMdmPriFwVer,
       "fgMdmCarrierAbbr": fgMdmCarrierAbbr,
       "fgMdmActState": fgMdmActState,
       "fgMdmOpMode": fgMdmOpMode,
       "fgMdmLacTac": fgMdmLacTac,
       "fgMdmActBand": fgMdmActBand,
       "fgMdmCellId": fgMdmCellId,
       "fgMdmRssi": fgMdmRssi,
       "fgSimInfoTable": fgSimInfoTable,
       "fgSimInfoEntry": fgSimInfoEntry,
       "fgSimEntIndex": fgSimEntIndex,
       "fgSimMdmEntIndex": fgSimMdmEntIndex,
       "fgSimState": fgSimState,
       "fgSimIccid": fgSimIccid,
       "fgSimImsi": fgSimImsi,
       "fgSimCountry": fgSimCountry,
       "fgSimNetwork": fgSimNetwork,
       "fgSignalInfoTable": fgSignalInfoTable,
       "fgSignalInfoEntry": fgSignalInfoEntry,
       "fgSigMdmEntIndex": fgSigMdmEntIndex,
       "fgCdmaRssi": fgCdmaRssi,
       "fgCdmaEcio": fgCdmaEcio,
       "fgHdrRssi": fgHdrRssi,
       "fgHdrEcio": fgHdrEcio,
       "fgHdrSinr": fgHdrSinr,
       "fgHdrIo": fgHdrIo,
       "fgGsm": fgGsm,
       "fgWcdmaRssi": fgWcdmaRssi,
       "fgWcdmaEcio": fgWcdmaEcio,
       "fgLteRssi": fgLteRssi,
       "fgLteRsrq": fgLteRsrq,
       "fgLteRsrp": fgLteRsrp,
       "fgLteSnr": fgLteSnr,
       "fgTdma": fgTdma,
       "fgTrafficInfoTable": fgTrafficInfoTable,
       "fgTrafficInfoEntry": fgTrafficInfoEntry,
       "fgTrafMdmEntIndex": fgTrafMdmEntIndex,
       "fgTxPacksOK": fgTxPacksOK,
       "fgRxPacksOK": fgRxPacksOK,
       "fgTxPacksErr": fgTxPacksErr,
       "fgRxPacksErr": fgRxPacksErr,
       "fgTxPacksOverflow": fgTxPacksOverflow,
       "fgRxPacksOverflow": fgRxPacksOverflow,
       "fgTxBytesOK": fgTxBytesOK,
       "fgRxBytesOK": fgRxBytesOK,
       "fgLastCallTxBytesOK": fgLastCallTxBytesOK,
       "fgLastCallRxBytesOK": fgLastCallRxBytesOK,
       "fgTxPacksDrop": fgTxPacksDrop,
       "fgRxPacksDrop": fgRxPacksDrop,
       "fgSessInfoTable": fgSessInfoTable,
       "fgSessInfoEntry": fgSessInfoEntry,
       "fgLteSessEntIndex": fgLteSessEntIndex,
       "fgSessMdmEntIndex": fgSessMdmEntIndex,
       "fdLteIfName": fdLteIfName,
       "fdLteSessConnStat": fdLteSessConnStat,
       "fdLteProfId": fdLteProfId,
       "fdLteProfName": fdLteProfName,
       "fdLteProfType": fdLteProfType,
       "fdLtePdpType": fdLtePdpType,
       "fdLteProfApn": fdLteProfApn,
       "fdLteProfIpFamily": fdLteProfIpFamily,
       "fdLteIpv4Addr": fdLteIpv4Addr,
       "fdLteIpv4GwAddr": fdLteIpv4GwAddr,
       "fdLteIpv4NetMask": fdLteIpv4NetMask,
       "fdLteIpv4PriDns": fdLteIpv4PriDns,
       "fdLteIpv4SecDns": fdLteIpv4SecDns,
       "fdLteIpv6Addr": fdLteIpv6Addr,
       "fdLteIpv6PrefLen": fdLteIpv6PrefLen,
       "fdLteIpv6GwAddr": fdLteIpv6GwAddr,
       "fdLteIpv6GwPrefLen": fdLteIpv6GwPrefLen,
       "fdLteIpv6PriDns": fdLteIpv6PriDns,
       "fdLteIpv6SecDns": fdLteIpv6SecDns,
       "fdLteMtu": fdLteMtu,
       "fdLteAutoConn": fdLteAutoConn,
       "fdLteNetType": fdLteNetType,
       "fdLteNetTypeLas": fdLteNetTypeLas,
       "fdLteLinkProto": fdLteLinkProto,
       "fgGpsInfoTable": fgGpsInfoTable,
       "fgGpsInfoEntry": fgGpsInfoEntry,
       "fgGpsMdmEntIndex": fgGpsMdmEntIndex,
       "fgGpsEnabled": fgGpsEnabled,
       "fgLatitude": fgLatitude,
       "fgLongitude": fgLongitude,
       "fgUtcTime": fgUtcTime,
       "fgLocalTime": fgLocalTime,
       "fgDatausageInfoTable": fgDatausageInfoTable,
       "fgDatausageInfoEntry": fgDatausageInfoEntry,
       "fgDatausageMdmEntIndex": fgDatausageMdmEntIndex,
       "fgDatausageEnabled": fgDatausageEnabled,
       "fgDataOut": fgDataOut,
       "fgDataIn": fgDataIn,
       "fgNPU": fgNPU,
       "fgNPUInfo": fgNPUInfo,
       "fgNPUNumber": fgNPUNumber,
       "fgNPUName": fgNPUName,
       "fgNPUDrvDriftSum": fgNPUDrvDriftSum,
       "fgNPUTables": fgNPUTables,
       "fgNPUTable": fgNPUTable,
       "fgNPUEntry": fgNPUEntry,
       "fgNPUEntIndex": fgNPUEntIndex,
       "fgNPUSessionTblSize": fgNPUSessionTblSize,
       "fgNPUSessionCount": fgNPUSessionCount,
       "fgNPUDrvDrift": fgNPUDrvDrift,
       "fgLog": fgLog,
       "fgLogInfo": fgLogInfo,
       "fgLogDeviceNumber": fgLogDeviceNumber,
       "fgLogDevices": fgLogDevices,
       "fgLogDeviceTable": fgLogDeviceTable,
       "fgLogDeviceEntry": fgLogDeviceEntry,
       "fgLogDeviceEntryIndex": fgLogDeviceEntryIndex,
       "fgLogDeviceEnabled": fgLogDeviceEnabled,
       "fgLogDeviceName": fgLogDeviceName,
       "fgLogDeviceSentCount": fgLogDeviceSentCount,
       "fgLogDeviceRelayedCount": fgLogDeviceRelayedCount,
       "fgLogDeviceCachedCount": fgLogDeviceCachedCount,
       "fgLogDeviceFailedCount": fgLogDeviceFailedCount,
       "fgLogDeviceDroppedCount": fgLogDeviceDroppedCount,
       "fgConfig": fgConfig,
       "fgConfigStatus": fgConfigStatus,
       "fgConfigSerial": fgConfigSerial,
       "fgConfigChecksum": fgConfigChecksum,
       "fgConfigLastChangeTime": fgConfigLastChangeTime,
       "fgDhcp": fgDhcp,
       "fgDhcpInfo": fgDhcpInfo,
       "fgDhcpServerNumber": fgDhcpServerNumber,
       "fgDhcpTables": fgDhcpTables,
       "fgDhcpTable": fgDhcpTable,
       "fgDhcpEntry": fgDhcpEntry,
       "fgDhcpLeaseUsage": fgDhcpLeaseUsage,
       "fgDhcpTrapObjects": fgDhcpTrapObjects,
       "fgDhcpTrapType": fgDhcpTrapType,
       "fgDhcpTrapMessage": fgDhcpTrapMessage,
       "fgDhcpServerId": fgDhcpServerId,
       "fgSw": fgSw,
       "fgSwDeviceInfo": fgSwDeviceInfo,
       "fgSwDeviceTable": fgSwDeviceTable,
       "fgSwDeviceEntry": fgSwDeviceEntry,
       "fgSwDevicePlatform": fgSwDevicePlatform,
       "fgSwDeviceId": fgSwDeviceId,
       "fgSwDeviceSerialNum": fgSwDeviceSerialNum,
       "fgSwDeviceName": fgSwDeviceName,
       "fgSwDeviceVersion": fgSwDeviceVersion,
       "fgSwDeviceAuthorized": fgSwDeviceAuthorized,
       "fgSwDeviceStatus": fgSwDeviceStatus,
       "fgSwDeviceJoinTime": fgSwDeviceJoinTime,
       "fgSwDeviceIp": fgSwDeviceIp,
       "fgSwDeviceFlag": fgSwDeviceFlag,
       "fgSwCpu": fgSwCpu,
       "fgSwMemory": fgSwMemory,
       "fgSwDeviceIpv6": fgSwDeviceIpv6,
       "fgSwPortInfo": fgSwPortInfo,
       "fgSwPortTable": fgSwPortTable,
       "fgSwPortEntry": fgSwPortEntry,
       "fgSwPortSwitchPlatform": fgSwPortSwitchPlatform,
       "fgSwPortSwitchId": fgSwPortSwitchId,
       "fgSwPortNum": fgSwPortNum,
       "fgSwPortSwitchSerialNum": fgSwPortSwitchSerialNum,
       "fgSwPortName": fgSwPortName,
       "fgSwPortStatus": fgSwPortStatus,
       "fgSwPortSpeedDuplex": fgSwPortSpeedDuplex,
       "fgSwPortNativeVlan": fgSwPortNativeVlan,
       "fgSwPortAllowedVlan": fgSwPortAllowedVlan,
       "fgSwPortUntaggedVlan": fgSwPortUntaggedVlan,
       "fgSwPortPOE": fgSwPortPOE,
       "fgSwPortPOEStatus": fgSwPortPOEStatus,
       "fgSwPortPOEState": fgSwPortPOEState,
       "fgSwPortPOEPower": fgSwPortPOEPower,
       "fgChassis": fgChassis,
       "fgChassisInfo": fgChassisInfo,
       "fgChassisVersion": fgChassisVersion,
       "fgChassisTrapObjects": fgChassisTrapObjects,
       "fgChassisSlotId": fgChassisSlotId,
       "fgChassisTrapMessage": fgChassisTrapMessage,
       "fgServiceGroupWorkerBlades": fgServiceGroupWorkerBlades,
       "fgSgWbTables": fgSgWbTables,
       "fgSgWorkerBladeTable": fgSgWorkerBladeTable,
       "fgSgWorkerBladeEntry": fgSgWorkerBladeEntry,
       "fgSgWbEntIndex": fgSgWbEntIndex,
       "fgSgWbServiceGroupID": fgSgWbServiceGroupID,
       "fgSgWbChassisID": fgSgWbChassisID,
       "fgSgWbSlotID": fgSgWbSlotID,
       "fgSgWbState": fgSgWbState,
       "fgSgWbStatusMsg": fgSgWbStatusMsg,
       "fgSgWbMaster": fgSgWbMaster,
       "fgSgWbSysVersion": fgSgWbSysVersion,
       "fgSgWbSysSerial": fgSgWbSysSerial,
       "fgSgWbSysUpTime": fgSgWbSysUpTime,
       "fgSgWbSysCpuUsage": fgSgWbSysCpuUsage,
       "fgSgWbSysMemUsage": fgSgWbSysMemUsage,
       "fgSgWbBaseLink": fgSgWbBaseLink,
       "fgSgWbFabricLink": fgSgWbFabricLink,
       "fgSgWbDataHb": fgSgWbDataHb,
       "fgSgWbMgmtHb": fgSgWbMgmtHb,
       "fgEms": fgEms,
       "fgEmsTables": fgEmsTables,
       "fgEmsGlobalTable": fgEmsGlobalTable,
       "fgEmsGlobalEntry": fgEmsGlobalEntry,
       "fgEmsGlobalEntIndex": fgEmsGlobalEntIndex,
       "fgEmsGlobalEntStatus": fgEmsGlobalEntStatus,
       "fgEmsGlobalEntConnectionName": fgEmsGlobalEntConnectionName,
       "fgEmsGlobalEntConnectionStatus": fgEmsGlobalEntConnectionStatus,
       "fgEmsGlobalEntLastCloseReason": fgEmsGlobalEntLastCloseReason,
       "fgEmsGlobalEntLastCloseReasonDesc": fgEmsGlobalEntLastCloseReasonDesc,
       "fgEmsGlobalEntLastCloseTime": fgEmsGlobalEntLastCloseTime,
       "fgEmsVdTable": fgEmsVdTable,
       "fgEmsVdEntry": fgEmsVdEntry,
       "fgEmsVdEntIndex": fgEmsVdEntIndex,
       "fgEmsVdEntStatus": fgEmsVdEntStatus,
       "fgEmsVdEntConnectionName": fgEmsVdEntConnectionName,
       "fgEmsVdEntConnectionStatus": fgEmsVdEntConnectionStatus,
       "fgEmsVdEntLastCloseReason": fgEmsVdEntLastCloseReason,
       "fgEmsVdEntLastCloseReasonDesc": fgEmsVdEntLastCloseReasonDesc,
       "fgEmsVdEntLastCloseTime": fgEmsVdEntLastCloseTime,
       "fgInternal5GModemsInfo": fgInternal5GModemsInfo,
       "fg5gMdmInfo": fg5gMdmInfo,
       "fg5gModemNumber": fg5gModemNumber,
       "fg5gMdmInfoTable": fg5gMdmInfoTable,
       "fg5gMdmInfoEntry": fg5gMdmInfoEntry,
       "fg5gMdmEntIndex": fg5gMdmEntIndex,
       "fg5gMdmDetected": fg5gMdmDetected,
       "fg5gMdmVendor": fg5gMdmVendor,
       "fg5gMdmModel": fg5gMdmModel,
       "fg5gMdmRevision": fg5gMdmRevision,
       "fg5gMdmImei": fg5gMdmImei,
       "fg5gMdmHwRevision": fg5gMdmHwRevision,
       "fg5gMdmMeid": fg5gMdmMeid,
       "fg5gMdmSwRev": fg5gMdmSwRev,
       "fg5gMdmPriFwVer": fg5gMdmPriFwVer,
       "fg5gMdmFwName": fg5gMdmFwName,
       "fg5gMdmOpMode": fg5gMdmOpMode,
       "fg5gMdmTemperature": fg5gMdmTemperature,
       "fg5gNetworkMode": fg5gNetworkMode,
       "fg5gSimInfoTable": fg5gSimInfoTable,
       "fg5gSimInfoEntry": fg5gSimInfoEntry,
       "fg5gSimMdmEntIndex": fg5gSimMdmEntIndex,
       "fg5gIdleSimState": fg5gIdleSimState,
       "fg5gIdleSimIccid": fg5gIdleSimIccid,
       "fg5gActiveSimState": fg5gActiveSimState,
       "fg5gActiveSimIccid": fg5gActiveSimIccid,
       "fg5gActiveSimMsisdn": fg5gActiveSimMsisdn,
       "fg5gActiveSimImsi": fg5gActiveSimImsi,
       "fg5gActiveSimCountry": fg5gActiveSimCountry,
       "fg5gActiveSimNetwork": fg5gActiveSimNetwork,
       "fg5gActiveSimPinState": fg5gActiveSimPinState,
       "fg5gSignalInfoTable": fg5gSignalInfoTable,
       "fg5gSignalInfoEntry": fg5gSignalInfoEntry,
       "fg5gSigMdmEntIndex": fg5gSigMdmEntIndex,
       "fg5gSigWcdmaRssi": fg5gSigWcdmaRssi,
       "fg5gSigWcdmaEcio": fg5gSigWcdmaEcio,
       "fg5gSigLteRssi": fg5gSigLteRssi,
       "fg5gSigLteRsrq": fg5gSigLteRsrq,
       "fg5gSigLteRsrp": fg5gSigLteRsrp,
       "fg5gSigLteSnr": fg5gSigLteSnr,
       "fg5gSig5gRsrp": fg5gSig5gRsrp,
       "fg5gSig5gSnr": fg5gSig5gSnr,
       "fg5gTrafficInfoTable": fg5gTrafficInfoTable,
       "fg5gTrafficInfoEntry": fg5gTrafficInfoEntry,
       "fg5gTrafMdmEntIndex": fg5gTrafMdmEntIndex,
       "fg5gIpv4TxPacksOK": fg5gIpv4TxPacksOK,
       "fg5gIpv4RxPacksOK": fg5gIpv4RxPacksOK,
       "fg5gIpv4TxPacksErr": fg5gIpv4TxPacksErr,
       "fg5gIpv4RxPacksErr": fg5gIpv4RxPacksErr,
       "fg5gIpv4TxPacksOverflow": fg5gIpv4TxPacksOverflow,
       "fg5gIpv4RxPacksOverflow": fg5gIpv4RxPacksOverflow,
       "fg5gIpv4TxBytesOK": fg5gIpv4TxBytesOK,
       "fg5gIpv4RxBytesOK": fg5gIpv4RxBytesOK,
       "fg5gIpv4TxPacksDrop": fg5gIpv4TxPacksDrop,
       "fg5gIpv4RxPacksDrop": fg5gIpv4RxPacksDrop,
       "fg5gIpv6TxPacksOK": fg5gIpv6TxPacksOK,
       "fg5gIpv6RxPacksOK": fg5gIpv6RxPacksOK,
       "fg5gIpv6TxPacksErr": fg5gIpv6TxPacksErr,
       "fg5gIpv6RxPacksErr": fg5gIpv6RxPacksErr,
       "fg5gIpv6TxPacksOverflow": fg5gIpv6TxPacksOverflow,
       "fg5gIpv6RxPacksOverflow": fg5gIpv6RxPacksOverflow,
       "fg5gIpv6TxBytesOK": fg5gIpv6TxBytesOK,
       "fg5gIpv6RxBytesOK": fg5gIpv6RxBytesOK,
       "fg5gIpv6TxPacksDrop": fg5gIpv6TxPacksDrop,
       "fg5gIpv6RxPacksDrop": fg5gIpv6RxPacksDrop,
       "fg5gSessInfoTable": fg5gSessInfoTable,
       "fg5gSessInfoEntry": fg5gSessInfoEntry,
       "fg5gSessMdmEntIndex": fg5gSessMdmEntIndex,
       "fg5gIfName": fg5gIfName,
       "fg5gMtu": fg5gMtu,
       "fg5gProfId": fg5gProfId,
       "fg5gProfName": fg5gProfName,
       "fg5gPdpType": fg5gPdpType,
       "fg5gProfApn": fg5gProfApn,
       "fg5gIpv4SessionStatus": fg5gIpv4SessionStatus,
       "fg5gIpv4Addr": fg5gIpv4Addr,
       "fg5gIpv4GwAddr": fg5gIpv4GwAddr,
       "fg5gIpv4NetMask": fg5gIpv4NetMask,
       "fg5gIpv4PriDns": fg5gIpv4PriDns,
       "fg5gIpv4SecDns": fg5gIpv4SecDns,
       "fg5gIpv6SessionStatus": fg5gIpv6SessionStatus,
       "fg5gIpv6Addr": fg5gIpv6Addr,
       "fg5gIpv6PrefLen": fg5gIpv6PrefLen,
       "fg5gIpv6GwAddr": fg5gIpv6GwAddr,
       "fg5gIpv6GwPrefLen": fg5gIpv6GwPrefLen,
       "fg5gIpv6PriDns": fg5gIpv6PriDns,
       "fg5gIpv6SecDns": fg5gIpv6SecDns,
       "fg5gGpsInfoTable": fg5gGpsInfoTable,
       "fg5gGpsInfoEntry": fg5gGpsInfoEntry,
       "fg5gGpsMdmEntIndex": fg5gGpsMdmEntIndex,
       "fg5gGpsEnabled": fg5gGpsEnabled,
       "fg5gLatitude": fg5gLatitude,
       "fg5gLongitude": fg5gLongitude,
       "fg5gUtcTime": fg5gUtcTime,
       "fg5gLocalTime": fg5gLocalTime,
       "fgMibConformance": fgMibConformance,
       "fgFmTrapGroup": fgFmTrapGroup,
       "fgFmTrapObjectGroup": fgFmTrapObjectGroup,
       "fgAdminObjectGroup": fgAdminObjectGroup,
       "fgSystemObjectGroup": fgSystemObjectGroup,
       "fgSoftwareObjectGroup": fgSoftwareObjectGroup,
       "fgHwSensorsObjectGroup": fgHwSensorsObjectGroup,
       "fgHighAvailabilityObjectGroup": fgHighAvailabilityObjectGroup,
       "fgVpnObjectGroup": fgVpnObjectGroup,
       "fgFirewallObjectGroup": fgFirewallObjectGroup,
       "fgAppServicesObjectGroup": fgAppServicesObjectGroup,
       "fgAntivirusObjectGroup": fgAntivirusObjectGroup,
       "fgIntrusionPrevtObjectGroup": fgIntrusionPrevtObjectGroup,
       "fgWebFilterObjectGroup": fgWebFilterObjectGroup,
       "fgVirtualDomainObjectGroup": fgVirtualDomainObjectGroup,
       "fgAdministrationObjectGroup": fgAdministrationObjectGroup,
       "fgIntfObjectGroup": fgIntfObjectGroup,
       "fgProcessorsObjectGroup": fgProcessorsObjectGroup,
       "fgNotificationGroup": fgNotificationGroup,
       "fgObsoleteNotificationsGroup": fgObsoleteNotificationsGroup,
       "fgExplicitProxyObjectGroup": fgExplicitProxyObjectGroup,
       "fgWebCacheObjectGroup": fgWebCacheObjectGroup,
       "fgWanOptObjectGroup": fgWanOptObjectGroup,
       "fgObsoleteAppServicesObjectGroup": fgObsoleteAppServicesObjectGroup,
       "fgSystemAdvancedObjectGroup": fgSystemAdvancedObjectGroup,
       "fgWcObjectGroup": fgWcObjectGroup,
       "fgFcObjectGroup": fgFcObjectGroup,
       "fgServerLoadBalanceObjectGroup": fgServerLoadBalanceObjectGroup,
       "fgUsbportsObjectGroup": fgUsbportsObjectGroup,
       "fgUsbModemInfoGroup": fgUsbModemInfoGroup,
       "fgDeviceObjectGroup": fgDeviceObjectGroup,
       "fgLinkMonitorGroup": fgLinkMonitorGroup,
       "fgInternalModemInfoGroup": fgInternalModemInfoGroup,
       "fgInternalModemSIMInfoGroup": fgInternalModemSIMInfoGroup,
       "fgInternalModemSigInfoGroup": fgInternalModemSigInfoGroup,
       "fgInternalModemTrafficInfoGroup": fgInternalModemTrafficInfoGroup,
       "fgInternalModemSessInfoGroup": fgInternalModemSessInfoGroup,
       "fgInternalModemGpsInfoGroup": fgInternalModemGpsInfoGroup,
       "fgInternalModemDatausageInfoGroup": fgInternalModemDatausageInfoGroup,
       "fgVWLHealthCheckLinkGroup": fgVWLHealthCheckLinkGroup,
       "fgDisksObjectGroup": fgDisksObjectGroup,
       "fgNPUGroup": fgNPUGroup,
       "fgSlaProbeClientGroup": fgSlaProbeClientGroup,
       "fgDNSProxyObjectGroup": fgDNSProxyObjectGroup,
       "fgLogGroup": fgLogGroup,
       "fgConfigGroup": fgConfigGroup,
       "fgDhcpObjectGroup": fgDhcpObjectGroup,
       "fgDpdkEngsObjectGroup": fgDpdkEngsObjectGroup,
       "fgSwitchDeviceObjectGroup": fgSwitchDeviceObjectGroup,
       "fgSwitchPortObjectGroup": fgSwitchPortObjectGroup,
       "fgChassisObjectGroup": fgChassisObjectGroup,
       "fgServiceGroupWorkerBladesGroup": fgServiceGroupWorkerBladesGroup,
       "fgEmsObjectGroup": fgEmsObjectGroup,
       "fgDioObjectGroup": fgDioObjectGroup,
       "fgInternal5GModemsInfoObjectGroup": fgInternal5GModemsInfoObjectGroup,
       "fgChassisSensorsObjectGroup": fgChassisSensorsObjectGroup,
       "fgMIBCompliance": fgMIBCompliance,
       "fg300MibCompliance": fg300MibCompliance,
       "fgObsolteMIBCompliance": fgObsolteMIBCompliance}
)
