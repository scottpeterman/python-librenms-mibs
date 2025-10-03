# SNMP MIB module (AI-AP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos\AI-AP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:41 2025
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

(aiEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "aiEnterpriseMibModules")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

aiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    aiMIB.setRevisions(
        ("2020-08-14 17:45",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ArubaEnableValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



class ArubaFrameType(TextualConvention, Integer32):
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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("associateRequest", 0),
          ("associateResponse", 1),
          ("reassociateRequest", 2),
          ("reassociateResponse", 3),
          ("probeRequest", 4),
          ("probeResponse", 5),
          ("beacon", 8),
          ("atim", 9),
          ("disassociate", 10),
          ("auth", 11),
          ("deauth", 12))
    )



class ArubaPhyType(TextualConvention, Integer32):
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
        *(("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 3),
          ("dot11ag", 4),
          ("wired", 5))
    )



class ArubaHTMode(TextualConvention, Integer32):
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
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ht20", 2),
          ("ht40", 3),
          ("vht20", 4),
          ("vht40", 5),
          ("vht80", 6),
          ("vht160", 7),
          ("vht80plus80", 8),
          ("he20", 9),
          ("he40", 10),
          ("he80", 11),
          ("he160", 12),
          ("he80plus80", 13))
    )



class ArubaHTExtChannel(TextualConvention, Integer32):
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
        *(("none", 1),
          ("above", 2),
          ("below", 3))
    )



class ArubaMonEncryptionType(TextualConvention, Integer32):
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
        *(("open", 0),
          ("wep", 1),
          ("wpa", 2),
          ("wpa2", 3),
          ("wpa3", 4))
    )



class ArubaMonEncryptionCipher(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("wep40", 1),
          ("wep104", 2),
          ("tkip", 3),
          ("aesccmp", 4),
          ("other", 5),
          ("gcm256", 6))
    )



class ArubaMonAuthAlgorithm(TextualConvention, Integer32):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("psk", 1),
          ("dot1x", 2),
          ("ft8021x", 3),
          ("ftpsk", 4),
          ("dot1x256", 5),
          ("psk256", 6),
          ("tdls", 7),
          ("sae", 8),
          ("ftsae", 9),
          ("other", 10),
          ("suiteb", 11),
          ("owe", 12))
    )



class ArubaSwitchRole(TextualConvention, Integer32):
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
        *(("master", 1),
          ("local", 2),
          ("backupmaster", 3))
    )



class ArubaSupportStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("supported", 2))
    )



class ArubaActiveState(TextualConvention, Integer32):
    status = "current"
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



class ArubaACLDomain(TextualConvention, Integer32):
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
        *(("alias", 1),
          ("any", 2),
          ("user", 3),
          ("host", 4),
          ("network", 5))
    )



class ArubaACLNetworkServiceType(TextualConvention, Integer32):
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
        *(("alias", 1),
          ("any", 2),
          ("tcp", 3),
          ("udp", 4),
          ("protocol", 5))
    )



class ArubaACLAction(TextualConvention, Integer32):
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
        *(("deny", 1),
          ("permit", 2),
          ("srcNAT", 3),
          ("dstNAT", 4),
          ("redirect", 5))
    )



class ArubaDaysOfWeek(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("sun", 1),
          ("mon", 2),
          ("tue", 3),
          ("wed", 4),
          ("thu", 5),
          ("fri", 6),
          ("sat", 7))
    )



class ArubaAuthenticationMethods(TextualConvention, Integer32):
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
              7,
              15,
              16,
              17,
              28,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("web", 1),
          ("mac", 2),
          ("vpn", 3),
          ("dot1x", 4),
          ("kerberos", 5),
          ("secureId", 7),
          ("pubcookie", 15),
          ("xSec", 16),
          ("xSecMachine", 17),
          ("via-vpn", 28),
          ("other", 255))
    )



class ArubaSubAuthenticationMethods(TextualConvention, Integer32):
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("authPAP", 1),
          ("authCHAP", 2),
          ("authMSCHAP", 3),
          ("authMSCHAPv2", 4),
          ("eapTLS", 5),
          ("eapTTLS", 6),
          ("eapLEAP", 7),
          ("eapMD5", 8),
          ("eapPEAP", 9))
    )



class ArubaEncryptionType(TextualConvention, Integer32):
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
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("static-wep", 1),
          ("dynamic-wep", 2),
          ("wpa-psk-tkip", 3),
          ("wpa-tkip", 4),
          ("wpa-psk-aes", 5),
          ("wpa-aes", 6),
          ("wpa2-psk-tkip", 7),
          ("wpa2-tkip", 8),
          ("wpa2-psk-aes", 9),
          ("wpa2-aes", 10),
          ("xSec", 11),
          ("bSec-128", 12),
          ("bSec-256", 13),
          ("aes-128-cmac", 14),
          ("unknown", 15),
          ("ft-psk", 16),
          ("ft-8021x", 17),
          ("wpa3-cnsa", 18),
          ("owe-aes", 20),
          ("wpa3-sae-aes", 21),
          ("wpa3-aes-gcmp-256", 22))
    )



class ArubaUserForwardMode(TextualConvention, Integer32):
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
        *(("tunnel-encrypted", 0),
          ("bridge", 1),
          ("tunnel-decrypted", 2),
          ("split-tunnel", 3))
    )



class ArubaRogueApType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("interfering", 2),
          ("unsecure", 3),
          ("dos", 4),
          ("unknown", 5),
          ("knownInterfering", 6),
          ("suspectedUnsecure", 7))
    )



class ArubaAPMatchType(TextualConvention, Integer32):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("configuredWiredMac", 1),
          ("ethernetWiredMac", 2),
          ("apWiredMac", 3),
          ("externalWiredMac", 4),
          ("manual", 5),
          ("baseBSSIDOverride", 6),
          ("mms", 7),
          ("ethernetGatewayWiredMac", 8),
          ("classificationDisabled", 9),
          ("apBSSID", 10),
          ("propagatedEthernetWiredMac", 11),
          ("apRule", 12),
          ("systemWiredMac", 13),
          ("systemGatewayMac", 14))
    )



class ArubaAPMatchMethod(TextualConvention, Integer32):
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
        *(("notApplicable", 0),
          ("exactMatch", 1),
          ("plusOneMatch", 2),
          ("minusOneMatch", 3),
          ("ouiMatch", 4))
    )



class ArubaStationType(TextualConvention, Integer32):
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
        *(("valid", 1),
          ("interfering", 2),
          ("dos", 3))
    )



class ArubaEncryptionMethods(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("disabled", 0),
          ("static-wep", 1),
          ("dynamic-wep", 2),
          ("static-wpa", 3),
          ("dynamic-wpa", 4),
          ("wpa2-psk-aes", 5),
          ("wpa2-8021x-aes", 6),
          ("wpa2PreAuth", 7),
          ("xsec", 8),
          ("wpa-psk-aes", 9),
          ("wpa-aes", 10),
          ("wpa2-psk-tkip", 11),
          ("wpa2-8021x-tkip", 12),
          ("bSec-128", 13),
          ("bSec-256", 14),
          ("owe-aes", 16),
          ("wpa3-sae-aes", 17),
          ("wpa3-cnsa", 18),
          ("wpa3-aes-ccm-128", 19),
          ("mpsk-aes", 21),
          ("wpa3-aes-gcm-256", 22))
    )


class ArubaHashAlgorithms(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )



class ArubaVlanValidRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )



class ArubaPortMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("dot1q", 2))
    )



class ArubaDot1dState(TextualConvention, Integer32):
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
        *(("disabled", 1),
          ("blocked", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5))
    )



class ArubaPoeState(TextualConvention, Integer32):
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
        *(("disabled", 1),
          ("enabled", 2),
          ("enabledCisco", 3),
          ("notAvailable", 4))
    )



class ArubaCardType(TextualConvention, Integer32):
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
        *(("lc1", 1),
          ("lc2", 2),
          ("sc1", 3),
          ("sc2", 4),
          ("sw2400", 5),
          ("sw800", 6),
          ("sw200", 7),
          ("m3mk1", 8),
          ("sw3200", 9),
          ("sw3400", 10),
          ("sw3600", 11),
          ("sw650", 12),
          ("sw651", 13),
          ("reserved1", 14),
          ("reserved2", 15),
          ("sw620", 16))
    )



class ArubaESIServerMode(TextualConvention, Integer32):
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
        *(("bridged", 1),
          ("routed", 2),
          ("nat", 3))
    )



class ArubaESIServerStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )



class ArubaIfType(TextualConvention, Integer32):
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
        *(("port", 1),
          ("vlan", 2),
          ("tunnel", 3),
          ("loopback", 4))
    )



class ArubaVoipProtocolType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("sccp", 1),
          ("svp", 2),
          ("vocera", 3),
          ("sip", 4),
          ("unknown", 10))
    )



class ArubaAccessPointMode(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("airMonitor", 1),
          ("accessPoint", 2),
          ("accessPointAndMonitor", 3),
          ("meshPortal", 4),
          ("meshPoint", 5),
          ("rfprotectSensor", 6),
          ("spectrumSensor", 7))
    )



class ArubaAuthServerType(TextualConvention, Integer32):
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
        *(("internaldb", 1),
          ("radius", 2),
          ("ldap", 3),
          ("kerberos", 4),
          ("tacacs", 5))
    )



class ArubaAddressType(TextualConvention, Integer32):
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
        *(("srcAddress", 1),
          ("dstAddress", 2),
          ("bssid", 3))
    )



class ArubaBlackListReason(TextualConvention, Integer32):
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
              8,
              9,
              100)
        )
    )
    namedValues = NamedValues(
        *(("userDefined", 1),
          ("mitmAttack", 2),
          ("authFailure", 3),
          ("pingFlood", 4),
          ("sessionFlood", 5),
          ("synFlood", 6),
          ("sessionBlacklist", 7),
          ("ipSpoofing", 8),
          ("esiBlacklist", 9),
          ("other", 100))
    )



class ArubaDBType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mssql", 1),
          ("mysql", 2))
    )



class ArubaVrrpState(TextualConvention, Integer32):
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
        *(("initialize", 1),
          ("backup", 2),
          ("master", 3))
    )



class ArubaOperStateValue(TextualConvention, Integer32):
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )



class ArubaAntennaSetting(TextualConvention, Integer32):
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
        *(("notPresent", 1),
          ("enabled", 2),
          ("disabled", 3))
    )



class ArubaAPStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )



class ArubaPortSpeed(TextualConvention, Integer32):
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
        *(("speed10Mbps", 1),
          ("speed100Mbps", 2),
          ("speed1000Mbps", 3),
          ("speedAuto", 4),
          ("speed10Gbps", 5))
    )



class ArubaPortDuplex(TextualConvention, Integer32):
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
        *(("half", 1),
          ("full", 2),
          ("auto", 3))
    )



class ArubaPortType(TextualConvention, Integer32):
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
        *(("fastethernet", 1),
          ("gigabitethernet", 2),
          ("xgigabitethernet", 3))
    )



class ArubaEnet1Mode(TextualConvention, Integer32):
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
        *(("activeStandby", 1),
          ("tunnel", 2),
          ("bridge", 3),
          ("notApplicable", 4),
          ("split", 5))
    )



class ArubaUnprovisionedStatus(TextualConvention, Integer32):
    status = "current"
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



class ArubaMonitorMode(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("all", 1),
          ("none", 2),
          ("mixed", 3))
    )



class ArubaConfigurationState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("error", 2))
    )



class ArubaConfigurationChangeType(TextualConvention, Integer32):
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
        *(("create", 1),
          ("delete", 2),
          ("modify", 3))
    )



class ArubaCallStates(TextualConvention, Integer32):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("initiated", 1),
          ("connecting", 2),
          ("delivered", 3),
          ("connected", 4),
          ("offered", 5),
          ("alerting", 6),
          ("releasing", 7),
          ("cancelling", 8),
          ("challenging", 9),
          ("transient", 10),
          ("blockwait", 11),
          ("succ", 12),
          ("fail", 13),
          ("aborted", 14),
          ("blocked", 15))
    )



class ArubaVoipProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("sccp", 1),
          ("svp", 2),
          ("vocera", 3),
          ("sip", 9),
          ("ua", 11))
    )



class ArubaVoipRegState(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("registering", 1),
          ("unregistering", 2),
          ("challenge", 3),
          ("registered", 4),
          ("unregistered", 5))
    )



class ArubaVoiceCdrDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("og", 0),
          ("ic", 1))
    )



class ArubaVoiceCacBit(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("cacActiveLoadBalancing", 0),
          ("cacHighCapThresholdReached", 1),
          ("cacHandRsrvThresholdReached", 2),
          ("cacPeakCapacityReached", 3))
    )


class ArubaMeshRole(TextualConvention, Integer32):
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
        *(("nonmesh", 0),
          ("point", 1),
          ("portal", 2))
    )



class ArubaHTRate(TextualConvention, Integer32):
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
              34)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ht6dot5", 1),
          ("ht13", 2),
          ("ht13dot5", 3),
          ("ht15", 4),
          ("ht19dot5", 5),
          ("ht26", 6),
          ("ht27", 7),
          ("ht30", 8),
          ("ht39", 9),
          ("ht40dot5", 10),
          ("ht45", 11),
          ("ht52", 12),
          ("ht54", 13),
          ("ht58dot5", 14),
          ("ht60", 15),
          ("ht65", 16),
          ("ht78", 17),
          ("ht81", 18),
          ("ht90", 19),
          ("ht104", 20),
          ("ht108", 21),
          ("ht117", 22),
          ("ht120", 23),
          ("ht121dot5", 24),
          ("ht130", 25),
          ("ht135", 26),
          ("ht150", 27),
          ("ht162", 28),
          ("ht180", 29),
          ("ht216", 30),
          ("ht240", 31),
          ("ht243", 32),
          ("ht270", 33),
          ("ht300", 34))
    )



class ArubaUSBStatus(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("notPresent", 1),
          ("inactive", 2),
          ("active", 3))
    )



class ArubaARMChangeReason(TextualConvention, Integer32):
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("radarDetected", 1),
          ("radarCleared", 2),
          ("txHang", 3),
          ("txHangClear", 4),
          ("fortyMhzIntol", 5),
          ("cancel40mhzIntol", 6),
          ("fortyMhzAlign", 7),
          ("armInterference", 8),
          ("armInvalidCh", 9),
          ("armErrorThresh", 10),
          ("armNoiseThresh", 11),
          ("armEmptyCh", 12),
          ("armRogueCont", 13),
          ("armDecreasePower", 14),
          ("armIncreasePower", 15),
          ("armTurnOffRadio", 16),
          ("armTurnOnRadio", 17))
    )



class ArubaAPMasterStatus(TextualConvention, Integer32):
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
        *(("up", 1),
          ("down", 2),
          ("move", 3))
    )



class ArubaAPUplinkType(TextualConvention, Integer32):
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
        *(("ethernet", 1),
          ("usb", 2),
          ("pppoe", 3),
          ("wifi", 4))
    )



class ArubaAPUplinkChangeReason(TextualConvention, Integer32):
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
        *(("linkFailure", 1),
          ("vpnFailure", 2),
          ("preemption", 3),
          ("internetFailover", 4))
    )



class ArubaPortalServerDownReason(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("connectFail", 1)
    )



# MIB Managed Objects in the order of their OIDs

_AiInfoGroup_ObjectIdentity = ObjectIdentity
aiInfoGroup = _AiInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1)
)
_AiVirtualControllerKey_Type = DisplayString
_AiVirtualControllerKey_Object = MibScalar
aiVirtualControllerKey = _AiVirtualControllerKey_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 1),
    _AiVirtualControllerKey_Type()
)
aiVirtualControllerKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiVirtualControllerKey.setStatus("current")
_AiVirtualControllerName_Type = DisplayString
_AiVirtualControllerName_Object = MibScalar
aiVirtualControllerName = _AiVirtualControllerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 2),
    _AiVirtualControllerName_Type()
)
aiVirtualControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiVirtualControllerName.setStatus("current")
_AiVirtualControllerOrganization_Type = DisplayString
_AiVirtualControllerOrganization_Object = MibScalar
aiVirtualControllerOrganization = _AiVirtualControllerOrganization_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 3),
    _AiVirtualControllerOrganization_Type()
)
aiVirtualControllerOrganization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiVirtualControllerOrganization.setStatus("current")
_AiVirtualControllerVersion_Type = DisplayString
_AiVirtualControllerVersion_Object = MibScalar
aiVirtualControllerVersion = _AiVirtualControllerVersion_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 4),
    _AiVirtualControllerVersion_Type()
)
aiVirtualControllerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiVirtualControllerVersion.setStatus("current")
_AiVirtualControllerIPAddress_Type = IpAddress
_AiVirtualControllerIPAddress_Object = MibScalar
aiVirtualControllerIPAddress = _AiVirtualControllerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 5),
    _AiVirtualControllerIPAddress_Type()
)
aiVirtualControllerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiVirtualControllerIPAddress.setStatus("current")
_AiMasterIPAddress_Type = IpAddress
_AiMasterIPAddress_Object = MibScalar
aiMasterIPAddress = _AiMasterIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 6),
    _AiMasterIPAddress_Type()
)
aiMasterIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiMasterIPAddress.setStatus("current")
_AiWlanSSIDTable_Object = MibTable
aiWlanSSIDTable = _AiWlanSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    aiWlanSSIDTable.setStatus("current")
_AiWlanSSIDEntry_Object = MibTableRow
aiWlanSSIDEntry = _AiWlanSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 7, 1)
)
aiWlanSSIDEntry.setIndexNames(
    (0, "AI-AP-MIB", "aiSSIDIndex"),
)
if mibBuilder.loadTexts:
    aiWlanSSIDEntry.setStatus("current")
_AiSSIDIndex_Type = Integer32
_AiSSIDIndex_Object = MibTableColumn
aiSSIDIndex = _AiSSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 7, 1, 1),
    _AiSSIDIndex_Type()
)
aiSSIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSSIDIndex.setStatus("current")


class _AiSSID_Type(OctetString):
    """Custom type aiSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AiSSID_Type.__name__ = "OctetString"
_AiSSID_Object = MibTableColumn
aiSSID = _AiSSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 7, 1, 2),
    _AiSSID_Type()
)
aiSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSSID.setStatus("current")


class _AiSSIDStatus_Type(Integer32):
    """Custom type aiSSIDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_AiSSIDStatus_Type.__name__ = "Integer32"
_AiSSIDStatus_Object = MibTableColumn
aiSSIDStatus = _AiSSIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 7, 1, 3),
    _AiSSIDStatus_Type()
)
aiSSIDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSSIDStatus.setStatus("current")
_AiSSIDClientNum_Type = Integer32
_AiSSIDClientNum_Object = MibTableColumn
aiSSIDClientNum = _AiSSIDClientNum_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 7, 1, 4),
    _AiSSIDClientNum_Type()
)
aiSSIDClientNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSSIDClientNum.setStatus("current")


class _AiSSIDHide_Type(Integer32):
    """Custom type aiSSIDHide based on Integer32"""
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


_AiSSIDHide_Type.__name__ = "Integer32"
_AiSSIDHide_Object = MibTableColumn
aiSSIDHide = _AiSSIDHide_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 7, 1, 5),
    _AiSSIDHide_Type()
)
aiSSIDHide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiSSIDHide.setStatus("current")
_AiInterferAccessPointTable_Object = MibTable
aiInterferAccessPointTable = _AiInterferAccessPointTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    aiInterferAccessPointTable.setStatus("current")
_AiInterferAccessPointEntry_Object = MibTableRow
aiInterferAccessPointEntry = _AiInterferAccessPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 8, 1)
)
aiInterferAccessPointEntry.setIndexNames(
    (0, "AI-AP-MIB", "aiInterferAPIndex"),
)
if mibBuilder.loadTexts:
    aiInterferAccessPointEntry.setStatus("current")
_AiInterferAPIndex_Type = Integer32
_AiInterferAPIndex_Object = MibTableColumn
aiInterferAPIndex = _AiInterferAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 8, 1, 1),
    _AiInterferAPIndex_Type()
)
aiInterferAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiInterferAPIndex.setStatus("current")
_AiInterferAPBSSID_Type = MacAddress
_AiInterferAPBSSID_Object = MibTableColumn
aiInterferAPBSSID = _AiInterferAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 8, 1, 2),
    _AiInterferAPBSSID_Type()
)
aiInterferAPBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiInterferAPBSSID.setStatus("current")


class _AiInterferAPESSID_Type(OctetString):
    """Custom type aiInterferAPESSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AiInterferAPESSID_Type.__name__ = "OctetString"
_AiInterferAPESSID_Object = MibTableColumn
aiInterferAPESSID = _AiInterferAPESSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 8, 1, 3),
    _AiInterferAPESSID_Type()
)
aiInterferAPESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiInterferAPESSID.setStatus("current")
_AiInterferAPChannel_Type = DisplayString
_AiInterferAPChannel_Object = MibTableColumn
aiInterferAPChannel = _AiInterferAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 8, 1, 4),
    _AiInterferAPChannel_Type()
)
aiInterferAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiInterferAPChannel.setStatus("current")
_AiInterferAPPhyType_Type = DisplayString
_AiInterferAPPhyType_Object = MibTableColumn
aiInterferAPPhyType = _AiInterferAPPhyType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 8, 1, 5),
    _AiInterferAPPhyType_Type()
)
aiInterferAPPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiInterferAPPhyType.setStatus("current")
_AiInterferAPEncr_Type = DisplayString
_AiInterferAPEncr_Object = MibTableColumn
aiInterferAPEncr = _AiInterferAPEncr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 8, 1, 6),
    _AiInterferAPEncr_Type()
)
aiInterferAPEncr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiInterferAPEncr.setStatus("current")
_AiInterferAPAvgSnr_Type = Integer32
_AiInterferAPAvgSnr_Object = MibTableColumn
aiInterferAPAvgSnr = _AiInterferAPAvgSnr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 8, 1, 7),
    _AiInterferAPAvgSnr_Type()
)
aiInterferAPAvgSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiInterferAPAvgSnr.setStatus("current")
_AiInterferAPType_Type = DisplayString
_AiInterferAPType_Object = MibTableColumn
aiInterferAPType = _AiInterferAPType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 8, 1, 8),
    _AiInterferAPType_Type()
)
aiInterferAPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiInterferAPType.setStatus("current")
_AiMeshTable_Object = MibTable
aiMeshTable = _AiMeshTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 15)
)
if mibBuilder.loadTexts:
    aiMeshTable.setStatus("current")
_AiMeshEntry_Object = MibTableRow
aiMeshEntry = _AiMeshEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 15, 1)
)
aiMeshEntry.setIndexNames(
    (0, "AI-AP-MIB", "aiMeshIndex"),
)
if mibBuilder.loadTexts:
    aiMeshEntry.setStatus("current")
_AiMeshIndex_Type = Integer32
_AiMeshIndex_Object = MibTableColumn
aiMeshIndex = _AiMeshIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 15, 1, 1),
    _AiMeshIndex_Type()
)
aiMeshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiMeshIndex.setStatus("current")
_AiMeshPointMac_Type = MacAddress
_AiMeshPointMac_Object = MibTableColumn
aiMeshPointMac = _AiMeshPointMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 15, 1, 2),
    _AiMeshPointMac_Type()
)
aiMeshPointMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiMeshPointMac.setStatus("current")
_AiMeshPortalMac_Type = DisplayString
_AiMeshPortalMac_Object = MibTableColumn
aiMeshPortalMac = _AiMeshPortalMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 15, 1, 3),
    _AiMeshPortalMac_Type()
)
aiMeshPortalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiMeshPortalMac.setStatus("current")
_AiMeshChannel_Type = DisplayString
_AiMeshChannel_Object = MibTableColumn
aiMeshChannel = _AiMeshChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 15, 1, 4),
    _AiMeshChannel_Type()
)
aiMeshChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiMeshChannel.setStatus("current")
_AiMeshAvgRssi_Type = Integer32
_AiMeshAvgRssi_Object = MibTableColumn
aiMeshAvgRssi = _AiMeshAvgRssi_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 15, 1, 5),
    _AiMeshAvgRssi_Type()
)
aiMeshAvgRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiMeshAvgRssi.setStatus("current")
_AiMeshHops_Type = Integer32
_AiMeshHops_Object = MibTableColumn
aiMeshHops = _AiMeshHops_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 15, 1, 6),
    _AiMeshHops_Type()
)
aiMeshHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiMeshHops.setStatus("current")
_AiMeshAge_Type = Integer32
_AiMeshAge_Object = MibTableColumn
aiMeshAge = _AiMeshAge_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 15, 1, 7),
    _AiMeshAge_Type()
)
aiMeshAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiMeshAge.setStatus("current")
_AiMeshCost_Type = DisplayString
_AiMeshCost_Object = MibTableColumn
aiMeshCost = _AiMeshCost_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 15, 1, 8),
    _AiMeshCost_Type()
)
aiMeshCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiMeshCost.setStatus("current")
_AiMeshRelation_Type = DisplayString
_AiMeshRelation_Object = MibTableColumn
aiMeshRelation = _AiMeshRelation_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 1, 15, 1, 9),
    _AiMeshRelation_Type()
)
aiMeshRelation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiMeshRelation.setStatus("current")
_AiStateGroup_ObjectIdentity = ObjectIdentity
aiStateGroup = _AiStateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2)
)
_AiAccessPointTable_Object = MibTable
aiAccessPointTable = _AiAccessPointTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aiAccessPointTable.setStatus("current")
_AiAccessPointEntry_Object = MibTableRow
aiAccessPointEntry = _AiAccessPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 1, 1)
)
aiAccessPointEntry.setIndexNames(
    (0, "AI-AP-MIB", "aiAPMACAddress"),
)
if mibBuilder.loadTexts:
    aiAccessPointEntry.setStatus("current")
_AiAPMACAddress_Type = MacAddress
_AiAPMACAddress_Object = MibTableColumn
aiAPMACAddress = _AiAPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 1, 1, 1),
    _AiAPMACAddress_Type()
)
aiAPMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiAPMACAddress.setStatus("current")


class _AiAPName_Type(DisplayString):
    """Custom type aiAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AiAPName_Type.__name__ = "DisplayString"
_AiAPName_Object = MibTableColumn
aiAPName = _AiAPName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 1, 1, 2),
    _AiAPName_Type()
)
aiAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiAPName.setStatus("current")
_AiAPIPAddress_Type = IpAddress
_AiAPIPAddress_Object = MibTableColumn
aiAPIPAddress = _AiAPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 1, 1, 3),
    _AiAPIPAddress_Type()
)
aiAPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiAPIPAddress.setStatus("current")


class _AiAPSerialNum_Type(DisplayString):
    """Custom type aiAPSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AiAPSerialNum_Type.__name__ = "DisplayString"
_AiAPSerialNum_Object = MibTableColumn
aiAPSerialNum = _AiAPSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 1, 1, 4),
    _AiAPSerialNum_Type()
)
aiAPSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiAPSerialNum.setStatus("current")
_AiAPModel_Type = ObjectIdentifier
_AiAPModel_Object = MibTableColumn
aiAPModel = _AiAPModel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 1, 1, 5),
    _AiAPModel_Type()
)
aiAPModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiAPModel.setStatus("current")


class _AiAPModelName_Type(DisplayString):
    """Custom type aiAPModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AiAPModelName_Type.__name__ = "DisplayString"
_AiAPModelName_Object = MibTableColumn
aiAPModelName = _AiAPModelName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 1, 1, 6),
    _AiAPModelName_Type()
)
aiAPModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiAPModelName.setStatus("current")
_AiAPCPUUtilization_Type = Integer32
_AiAPCPUUtilization_Object = MibTableColumn
aiAPCPUUtilization = _AiAPCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 1, 1, 7),
    _AiAPCPUUtilization_Type()
)
aiAPCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiAPCPUUtilization.setStatus("current")
_AiAPMemoryFree_Type = Integer32
_AiAPMemoryFree_Object = MibTableColumn
aiAPMemoryFree = _AiAPMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 1, 1, 8),
    _AiAPMemoryFree_Type()
)
aiAPMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiAPMemoryFree.setStatus("current")
_AiAPUptime_Type = TimeTicks
_AiAPUptime_Object = MibTableColumn
aiAPUptime = _AiAPUptime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 1, 1, 9),
    _AiAPUptime_Type()
)
aiAPUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiAPUptime.setStatus("current")
_AiAPTotalMemory_Type = Integer32
_AiAPTotalMemory_Object = MibTableColumn
aiAPTotalMemory = _AiAPTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 1, 1, 10),
    _AiAPTotalMemory_Type()
)
aiAPTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiAPTotalMemory.setStatus("current")


class _AiAPStatus_Type(Integer32):
    """Custom type aiAPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AiAPStatus_Type.__name__ = "Integer32"
_AiAPStatus_Object = MibTableColumn
aiAPStatus = _AiAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 1, 1, 11),
    _AiAPStatus_Type()
)
aiAPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiAPStatus.setStatus("current")


class _AiAPHwopmode_Type(Integer32):
    """Custom type aiAPHwopmode based on Integer32"""
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
        *(("default", 0),
          ("rsdbsplit", 1),
          ("rsdb5g", 2),
          ("rsdb2g", 3),
          ("dual5gon", 4),
          ("dual5goff", 5),
          ("split5goff", 6),
          ("split5gon", 7))
    )


_AiAPHwopmode_Type.__name__ = "Integer32"
_AiAPHwopmode_Object = MibTableColumn
aiAPHwopmode = _AiAPHwopmode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 1, 1, 12),
    _AiAPHwopmode_Type()
)
aiAPHwopmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiAPHwopmode.setStatus("current")
_AiAPRole_Type = DisplayString
_AiAPRole_Object = MibTableColumn
aiAPRole = _AiAPRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 1, 1, 13),
    _AiAPRole_Type()
)
aiAPRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiAPRole.setStatus("current")
_AiRadioTable_Object = MibTable
aiRadioTable = _AiRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    aiRadioTable.setStatus("current")
_AiRadioEntry_Object = MibTableRow
aiRadioEntry = _AiRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1)
)
aiRadioEntry.setIndexNames(
    (0, "AI-AP-MIB", "aiRadioAPMACAddress"),
    (0, "AI-AP-MIB", "aiRadioIndex"),
)
if mibBuilder.loadTexts:
    aiRadioEntry.setStatus("current")
_AiRadioAPMACAddress_Type = MacAddress
_AiRadioAPMACAddress_Object = MibTableColumn
aiRadioAPMACAddress = _AiRadioAPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 1),
    _AiRadioAPMACAddress_Type()
)
aiRadioAPMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioAPMACAddress.setStatus("current")
_AiRadioIndex_Type = Integer32
_AiRadioIndex_Object = MibTableColumn
aiRadioIndex = _AiRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 2),
    _AiRadioIndex_Type()
)
aiRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioIndex.setStatus("current")
_AiRadioMACAddress_Type = MacAddress
_AiRadioMACAddress_Object = MibTableColumn
aiRadioMACAddress = _AiRadioMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 3),
    _AiRadioMACAddress_Type()
)
aiRadioMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioMACAddress.setStatus("current")
_AiRadioChannel_Type = DisplayString
_AiRadioChannel_Object = MibTableColumn
aiRadioChannel = _AiRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 4),
    _AiRadioChannel_Type()
)
aiRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioChannel.setStatus("current")
_AiRadioTransmitPower_Type = Integer32
_AiRadioTransmitPower_Object = MibTableColumn
aiRadioTransmitPower = _AiRadioTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 5),
    _AiRadioTransmitPower_Type()
)
aiRadioTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioTransmitPower.setStatus("current")
_AiRadioNoiseFloor_Type = Integer32
_AiRadioNoiseFloor_Object = MibTableColumn
aiRadioNoiseFloor = _AiRadioNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 6),
    _AiRadioNoiseFloor_Type()
)
aiRadioNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioNoiseFloor.setStatus("current")
_AiRadioUtilization4_Type = Integer32
_AiRadioUtilization4_Object = MibTableColumn
aiRadioUtilization4 = _AiRadioUtilization4_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 7),
    _AiRadioUtilization4_Type()
)
aiRadioUtilization4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioUtilization4.setStatus("current")
_AiRadioUtilization64_Type = Integer32
_AiRadioUtilization64_Object = MibTableColumn
aiRadioUtilization64 = _AiRadioUtilization64_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 8),
    _AiRadioUtilization64_Type()
)
aiRadioUtilization64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioUtilization64.setStatus("current")
_AiRadioTxTotalFrames_Type = Counter32
_AiRadioTxTotalFrames_Object = MibTableColumn
aiRadioTxTotalFrames = _AiRadioTxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 9),
    _AiRadioTxTotalFrames_Type()
)
aiRadioTxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioTxTotalFrames.setStatus("current")
_AiRadioTxMgmtFrames_Type = Counter32
_AiRadioTxMgmtFrames_Object = MibTableColumn
aiRadioTxMgmtFrames = _AiRadioTxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 10),
    _AiRadioTxMgmtFrames_Type()
)
aiRadioTxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioTxMgmtFrames.setStatus("current")
_AiRadioTxDataFrames_Type = Counter32
_AiRadioTxDataFrames_Object = MibTableColumn
aiRadioTxDataFrames = _AiRadioTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 11),
    _AiRadioTxDataFrames_Type()
)
aiRadioTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioTxDataFrames.setStatus("current")
_AiRadioTxDataBytes_Type = Counter32
_AiRadioTxDataBytes_Object = MibTableColumn
aiRadioTxDataBytes = _AiRadioTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 12),
    _AiRadioTxDataBytes_Type()
)
aiRadioTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioTxDataBytes.setStatus("current")
_AiRadioTxDrops_Type = Counter32
_AiRadioTxDrops_Object = MibTableColumn
aiRadioTxDrops = _AiRadioTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 13),
    _AiRadioTxDrops_Type()
)
aiRadioTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioTxDrops.setStatus("current")
_AiRadioRxTotalFrames_Type = Counter32
_AiRadioRxTotalFrames_Object = MibTableColumn
aiRadioRxTotalFrames = _AiRadioRxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 14),
    _AiRadioRxTotalFrames_Type()
)
aiRadioRxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioRxTotalFrames.setStatus("current")
_AiRadioRxDataFrames_Type = Counter32
_AiRadioRxDataFrames_Object = MibTableColumn
aiRadioRxDataFrames = _AiRadioRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 15),
    _AiRadioRxDataFrames_Type()
)
aiRadioRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioRxDataFrames.setStatus("current")
_AiRadioRxDataBytes_Type = Counter32
_AiRadioRxDataBytes_Object = MibTableColumn
aiRadioRxDataBytes = _AiRadioRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 16),
    _AiRadioRxDataBytes_Type()
)
aiRadioRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioRxDataBytes.setStatus("current")
_AiRadioRxMgmtFrames_Type = Counter32
_AiRadioRxMgmtFrames_Object = MibTableColumn
aiRadioRxMgmtFrames = _AiRadioRxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 17),
    _AiRadioRxMgmtFrames_Type()
)
aiRadioRxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioRxMgmtFrames.setStatus("current")
_AiRadioRxBad_Type = Counter32
_AiRadioRxBad_Object = MibTableColumn
aiRadioRxBad = _AiRadioRxBad_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 18),
    _AiRadioRxBad_Type()
)
aiRadioRxBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioRxBad.setStatus("current")
_AiRadioPhyEvents_Type = Counter32
_AiRadioPhyEvents_Object = MibTableColumn
aiRadioPhyEvents = _AiRadioPhyEvents_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 19),
    _AiRadioPhyEvents_Type()
)
aiRadioPhyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioPhyEvents.setStatus("current")


class _AiRadioStatus_Type(Integer32):
    """Custom type aiRadioStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AiRadioStatus_Type.__name__ = "Integer32"
_AiRadioStatus_Object = MibTableColumn
aiRadioStatus = _AiRadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 20),
    _AiRadioStatus_Type()
)
aiRadioStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioStatus.setStatus("current")
_AiRadioClientNum_Type = Integer32
_AiRadioClientNum_Object = MibTableColumn
aiRadioClientNum = _AiRadioClientNum_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 21),
    _AiRadioClientNum_Type()
)
aiRadioClientNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioClientNum.setStatus("current")
_AiRadioMode_Type = DisplayString
_AiRadioMode_Object = MibTableColumn
aiRadioMode = _AiRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 2, 1, 22),
    _AiRadioMode_Type()
)
aiRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiRadioMode.setStatus("current")
_AiWlanTable_Object = MibTable
aiWlanTable = _AiWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    aiWlanTable.setStatus("current")
_AiWlanEntry_Object = MibTableRow
aiWlanEntry = _AiWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 3, 1)
)
aiWlanEntry.setIndexNames(
    (0, "AI-AP-MIB", "aiWlanAPMACAddress"),
    (0, "AI-AP-MIB", "aiWlanIndex"),
)
if mibBuilder.loadTexts:
    aiWlanEntry.setStatus("current")
_AiWlanAPMACAddress_Type = MacAddress
_AiWlanAPMACAddress_Object = MibTableColumn
aiWlanAPMACAddress = _AiWlanAPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 3, 1, 1),
    _AiWlanAPMACAddress_Type()
)
aiWlanAPMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiWlanAPMACAddress.setStatus("current")
_AiWlanIndex_Type = Integer32
_AiWlanIndex_Object = MibTableColumn
aiWlanIndex = _AiWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 3, 1, 2),
    _AiWlanIndex_Type()
)
aiWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiWlanIndex.setStatus("current")
_AiWlanESSID_Type = DisplayString
_AiWlanESSID_Object = MibTableColumn
aiWlanESSID = _AiWlanESSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 3, 1, 3),
    _AiWlanESSID_Type()
)
aiWlanESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiWlanESSID.setStatus("current")
_AiWlanMACAddress_Type = MacAddress
_AiWlanMACAddress_Object = MibTableColumn
aiWlanMACAddress = _AiWlanMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 3, 1, 4),
    _AiWlanMACAddress_Type()
)
aiWlanMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiWlanMACAddress.setStatus("current")
_AiWlanTxTotalFrames_Type = Counter32
_AiWlanTxTotalFrames_Object = MibTableColumn
aiWlanTxTotalFrames = _AiWlanTxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 3, 1, 5),
    _AiWlanTxTotalFrames_Type()
)
aiWlanTxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiWlanTxTotalFrames.setStatus("current")
_AiWlanTxDataFrames_Type = Counter32
_AiWlanTxDataFrames_Object = MibTableColumn
aiWlanTxDataFrames = _AiWlanTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 3, 1, 6),
    _AiWlanTxDataFrames_Type()
)
aiWlanTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiWlanTxDataFrames.setStatus("current")
_AiWlanTxDataBytes_Type = Counter32
_AiWlanTxDataBytes_Object = MibTableColumn
aiWlanTxDataBytes = _AiWlanTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 3, 1, 7),
    _AiWlanTxDataBytes_Type()
)
aiWlanTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiWlanTxDataBytes.setStatus("current")
_AiWlanRxTotalFrames_Type = Counter32
_AiWlanRxTotalFrames_Object = MibTableColumn
aiWlanRxTotalFrames = _AiWlanRxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 3, 1, 8),
    _AiWlanRxTotalFrames_Type()
)
aiWlanRxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiWlanRxTotalFrames.setStatus("current")
_AiWlanRxDataFrames_Type = Counter32
_AiWlanRxDataFrames_Object = MibTableColumn
aiWlanRxDataFrames = _AiWlanRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 3, 1, 9),
    _AiWlanRxDataFrames_Type()
)
aiWlanRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiWlanRxDataFrames.setStatus("current")
_AiWlanRxDataBytes_Type = Counter32
_AiWlanRxDataBytes_Object = MibTableColumn
aiWlanRxDataBytes = _AiWlanRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 3, 1, 10),
    _AiWlanRxDataBytes_Type()
)
aiWlanRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiWlanRxDataBytes.setStatus("current")
_AiClientTable_Object = MibTable
aiClientTable = _AiClientTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    aiClientTable.setStatus("current")
_AiClientEntry_Object = MibTableRow
aiClientEntry = _AiClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1)
)
aiClientEntry.setIndexNames(
    (0, "AI-AP-MIB", "aiClientMACAddress"),
)
if mibBuilder.loadTexts:
    aiClientEntry.setStatus("current")
_AiClientMACAddress_Type = MacAddress
_AiClientMACAddress_Object = MibTableColumn
aiClientMACAddress = _AiClientMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 1),
    _AiClientMACAddress_Type()
)
aiClientMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientMACAddress.setStatus("current")
_AiClientWlanMACAddress_Type = MacAddress
_AiClientWlanMACAddress_Object = MibTableColumn
aiClientWlanMACAddress = _AiClientWlanMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 2),
    _AiClientWlanMACAddress_Type()
)
aiClientWlanMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientWlanMACAddress.setStatus("current")
_AiClientIPAddress_Type = IpAddress
_AiClientIPAddress_Object = MibTableColumn
aiClientIPAddress = _AiClientIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 3),
    _AiClientIPAddress_Type()
)
aiClientIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientIPAddress.setStatus("current")
_AiClientAPIPAddress_Type = IpAddress
_AiClientAPIPAddress_Object = MibTableColumn
aiClientAPIPAddress = _AiClientAPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 4),
    _AiClientAPIPAddress_Type()
)
aiClientAPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientAPIPAddress.setStatus("current")
_AiClientName_Type = DisplayString
_AiClientName_Object = MibTableColumn
aiClientName = _AiClientName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 5),
    _AiClientName_Type()
)
aiClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientName.setStatus("current")
_AiClientOperatingSystem_Type = DisplayString
_AiClientOperatingSystem_Object = MibTableColumn
aiClientOperatingSystem = _AiClientOperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 6),
    _AiClientOperatingSystem_Type()
)
aiClientOperatingSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientOperatingSystem.setStatus("current")
_AiClientSNR_Type = Integer32
_AiClientSNR_Object = MibTableColumn
aiClientSNR = _AiClientSNR_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 7),
    _AiClientSNR_Type()
)
aiClientSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientSNR.setStatus("current")
_AiClientTxDataFrames_Type = Counter32
_AiClientTxDataFrames_Object = MibTableColumn
aiClientTxDataFrames = _AiClientTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 8),
    _AiClientTxDataFrames_Type()
)
aiClientTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientTxDataFrames.setStatus("current")
_AiClientTxDataBytes_Type = Counter32
_AiClientTxDataBytes_Object = MibTableColumn
aiClientTxDataBytes = _AiClientTxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 9),
    _AiClientTxDataBytes_Type()
)
aiClientTxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientTxDataBytes.setStatus("current")
_AiClientTxRetries_Type = Counter32
_AiClientTxRetries_Object = MibTableColumn
aiClientTxRetries = _AiClientTxRetries_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 10),
    _AiClientTxRetries_Type()
)
aiClientTxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientTxRetries.setStatus("current")
_AiClientTxRate_Type = Integer32
_AiClientTxRate_Object = MibTableColumn
aiClientTxRate = _AiClientTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 11),
    _AiClientTxRate_Type()
)
aiClientTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientTxRate.setStatus("current")
_AiClientRxDataFrames_Type = Counter32
_AiClientRxDataFrames_Object = MibTableColumn
aiClientRxDataFrames = _AiClientRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 12),
    _AiClientRxDataFrames_Type()
)
aiClientRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientRxDataFrames.setStatus("current")
_AiClientRxDataBytes_Type = Counter32
_AiClientRxDataBytes_Object = MibTableColumn
aiClientRxDataBytes = _AiClientRxDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 13),
    _AiClientRxDataBytes_Type()
)
aiClientRxDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientRxDataBytes.setStatus("current")
_AiClientRxRetries_Type = Counter32
_AiClientRxRetries_Object = MibTableColumn
aiClientRxRetries = _AiClientRxRetries_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 14),
    _AiClientRxRetries_Type()
)
aiClientRxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientRxRetries.setStatus("current")
_AiClientRxRate_Type = Integer32
_AiClientRxRate_Object = MibTableColumn
aiClientRxRate = _AiClientRxRate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 15),
    _AiClientRxRate_Type()
)
aiClientRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientRxRate.setStatus("current")
_AiClientUptime_Type = TimeTicks
_AiClientUptime_Object = MibTableColumn
aiClientUptime = _AiClientUptime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 16),
    _AiClientUptime_Type()
)
aiClientUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientUptime.setStatus("current")
_AiClientPhyType_Type = ArubaPhyType
_AiClientPhyType_Object = MibTableColumn
aiClientPhyType = _AiClientPhyType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 17),
    _AiClientPhyType_Type()
)
aiClientPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientPhyType.setStatus("current")
_AiClientHtMode_Type = ArubaHTMode
_AiClientHtMode_Object = MibTableColumn
aiClientHtMode = _AiClientHtMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 4, 1, 18),
    _AiClientHtMode_Type()
)
aiClientHtMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientHtMode.setStatus("current")
_AiVoiceClientTable_Object = MibTable
aiVoiceClientTable = _AiVoiceClientTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 5)
)
if mibBuilder.loadTexts:
    aiVoiceClientTable.setStatus("current")
_AiVoiceClientEntry_Object = MibTableRow
aiVoiceClientEntry = _AiVoiceClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 5, 1)
)
aiVoiceClientEntry.setIndexNames(
    (0, "AI-AP-MIB", "aiClientMac"),
)
if mibBuilder.loadTexts:
    aiVoiceClientEntry.setStatus("current")
_AiClientMac_Type = MacAddress
_AiClientMac_Object = MibTableColumn
aiClientMac = _AiClientMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 5, 1, 1),
    _AiClientMac_Type()
)
aiClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientMac.setStatus("current")
_AiClientIP_Type = IpAddress
_AiClientIP_Object = MibTableColumn
aiClientIP = _AiClientIP_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 5, 1, 2),
    _AiClientIP_Type()
)
aiClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientIP.setStatus("current")
_AiClientAPMac_Type = MacAddress
_AiClientAPMac_Object = MibTableColumn
aiClientAPMac = _AiClientAPMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 5, 1, 3),
    _AiClientAPMac_Type()
)
aiClientAPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientAPMac.setStatus("current")
_AiClientAPName_Type = DisplayString
_AiClientAPName_Object = MibTableColumn
aiClientAPName = _AiClientAPName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 2, 5, 1, 4),
    _AiClientAPName_Type()
)
aiClientAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiClientAPName.setStatus("current")
_AiManagedInfoGroup_ObjectIdentity = ObjectIdentity
aiManagedInfoGroup = _AiManagedInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 3)
)
_AiManagedModeSinceLastSync_Type = DisplayString
_AiManagedModeSinceLastSync_Object = MibScalar
aiManagedModeSinceLastSync = _AiManagedModeSinceLastSync_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 3, 1),
    _AiManagedModeSinceLastSync_Type()
)
aiManagedModeSinceLastSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiManagedModeSinceLastSync.setStatus("current")
_AiTrapsGroup_ObjectIdentity = ObjectIdentity
aiTrapsGroup = _AiTrapsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200)
)
_AiTrapObjectsGroup_ObjectIdentity = ObjectIdentity
aiTrapObjectsGroup = _AiTrapObjectsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1)
)
_WlsxTrapAPMacAddress_Type = MacAddress
_WlsxTrapAPMacAddress_Object = MibScalar
wlsxTrapAPMacAddress = _WlsxTrapAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 1),
    _WlsxTrapAPMacAddress_Type()
)
wlsxTrapAPMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPMacAddress.setStatus("current")
_WlsxTrapAPIpAddress_Type = IpAddress
_WlsxTrapAPIpAddress_Object = MibScalar
wlsxTrapAPIpAddress = _WlsxTrapAPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 2),
    _WlsxTrapAPIpAddress_Type()
)
wlsxTrapAPIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPIpAddress.setStatus("current")
_WlsxTrapAPBSSID_Type = MacAddress
_WlsxTrapAPBSSID_Object = MibScalar
wlsxTrapAPBSSID = _WlsxTrapAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 3),
    _WlsxTrapAPBSSID_Type()
)
wlsxTrapAPBSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPBSSID.setStatus("current")


class _WlsxTrapEssid_Type(DisplayString):
    """Custom type wlsxTrapEssid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapEssid_Type.__name__ = "DisplayString"
_WlsxTrapEssid_Object = MibScalar
wlsxTrapEssid = _WlsxTrapEssid_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 4),
    _WlsxTrapEssid_Type()
)
wlsxTrapEssid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapEssid.setStatus("current")
_WlsxTrapTargetAPBSSID_Type = MacAddress
_WlsxTrapTargetAPBSSID_Object = MibScalar
wlsxTrapTargetAPBSSID = _WlsxTrapTargetAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 5),
    _WlsxTrapTargetAPBSSID_Type()
)
wlsxTrapTargetAPBSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTargetAPBSSID.setStatus("current")


class _WlsxTrapTargetAPSSID_Type(DisplayString):
    """Custom type wlsxTrapTargetAPSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapTargetAPSSID_Type.__name__ = "DisplayString"
_WlsxTrapTargetAPSSID_Object = MibScalar
wlsxTrapTargetAPSSID = _WlsxTrapTargetAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 6),
    _WlsxTrapTargetAPSSID_Type()
)
wlsxTrapTargetAPSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTargetAPSSID.setStatus("current")
_WlsxTrapTargetAPChannel_Type = Integer32
_WlsxTrapTargetAPChannel_Object = MibScalar
wlsxTrapTargetAPChannel = _WlsxTrapTargetAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 7),
    _WlsxTrapTargetAPChannel_Type()
)
wlsxTrapTargetAPChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTargetAPChannel.setStatus("current")
_WlsxTrapNodeMac_Type = MacAddress
_WlsxTrapNodeMac_Object = MibScalar
wlsxTrapNodeMac = _WlsxTrapNodeMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 8),
    _WlsxTrapNodeMac_Type()
)
wlsxTrapNodeMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapNodeMac.setStatus("current")
_WlsxTrapSourceMac_Type = MacAddress
_WlsxTrapSourceMac_Object = MibScalar
wlsxTrapSourceMac = _WlsxTrapSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 9),
    _WlsxTrapSourceMac_Type()
)
wlsxTrapSourceMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSourceMac.setStatus("current")
_WlsxReceiverMac_Type = MacAddress
_WlsxReceiverMac_Object = MibScalar
wlsxReceiverMac = _WlsxReceiverMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 10),
    _WlsxReceiverMac_Type()
)
wlsxReceiverMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxReceiverMac.setStatus("current")
_WlsxTrapTransmitterMac_Type = MacAddress
_WlsxTrapTransmitterMac_Object = MibScalar
wlsxTrapTransmitterMac = _WlsxTrapTransmitterMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 11),
    _WlsxTrapTransmitterMac_Type()
)
wlsxTrapTransmitterMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTransmitterMac.setStatus("current")
_WlsxTrapReceiverMac_Type = MacAddress
_WlsxTrapReceiverMac_Object = MibScalar
wlsxTrapReceiverMac = _WlsxTrapReceiverMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 12),
    _WlsxTrapReceiverMac_Type()
)
wlsxTrapReceiverMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapReceiverMac.setStatus("current")
_WlsxTrapSnr_Type = Integer32
_WlsxTrapSnr_Object = MibScalar
wlsxTrapSnr = _WlsxTrapSnr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 13),
    _WlsxTrapSnr_Type()
)
wlsxTrapSnr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSnr.setStatus("current")


class _WlsxTrapSignatureName_Type(DisplayString):
    """Custom type wlsxTrapSignatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapSignatureName_Type.__name__ = "DisplayString"
_WlsxTrapSignatureName_Object = MibScalar
wlsxTrapSignatureName = _WlsxTrapSignatureName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 14),
    _WlsxTrapSignatureName_Type()
)
wlsxTrapSignatureName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSignatureName.setStatus("current")
_WlsxTrapFrameType_Type = ArubaFrameType
_WlsxTrapFrameType_Object = MibScalar
wlsxTrapFrameType = _WlsxTrapFrameType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 15),
    _WlsxTrapFrameType_Type()
)
wlsxTrapFrameType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapFrameType.setStatus("current")
_WlsxTrapAddressType_Type = ArubaAddressType
_WlsxTrapAddressType_Object = MibScalar
wlsxTrapAddressType = _WlsxTrapAddressType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 16),
    _WlsxTrapAddressType_Type()
)
wlsxTrapAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAddressType.setStatus("current")


class _WlsxTrapAPLocation_Type(DisplayString):
    """Custom type wlsxTrapAPLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WlsxTrapAPLocation_Type.__name__ = "DisplayString"
_WlsxTrapAPLocation_Object = MibScalar
wlsxTrapAPLocation = _WlsxTrapAPLocation_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 17),
    _WlsxTrapAPLocation_Type()
)
wlsxTrapAPLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPLocation.setStatus("current")
_WlsxTrapAPChannel_Type = Integer32
_WlsxTrapAPChannel_Object = MibScalar
wlsxTrapAPChannel = _WlsxTrapAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 18),
    _WlsxTrapAPChannel_Type()
)
wlsxTrapAPChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPChannel.setStatus("current")
_WlsxTrapAPTxPower_Type = Integer32
_WlsxTrapAPTxPower_Object = MibScalar
wlsxTrapAPTxPower = _WlsxTrapAPTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 19),
    _WlsxTrapAPTxPower_Type()
)
wlsxTrapAPTxPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPTxPower.setStatus("current")
_WlsxTrapMatchedMac_Type = MacAddress
_WlsxTrapMatchedMac_Object = MibScalar
wlsxTrapMatchedMac = _WlsxTrapMatchedMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 20),
    _WlsxTrapMatchedMac_Type()
)
wlsxTrapMatchedMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapMatchedMac.setStatus("current")
_WlsxTrapMatchedIp_Type = IpAddress
_WlsxTrapMatchedIp_Object = MibScalar
wlsxTrapMatchedIp = _WlsxTrapMatchedIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 21),
    _WlsxTrapMatchedIp_Type()
)
wlsxTrapMatchedIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapMatchedIp.setStatus("current")


class _WlsxTrapRogueIfoURL_Type(DisplayString):
    """Custom type wlsxTrapRogueIfoURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapRogueIfoURL_Type.__name__ = "DisplayString"
_WlsxTrapRogueIfoURL_Object = MibScalar
wlsxTrapRogueIfoURL = _WlsxTrapRogueIfoURL_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 22),
    _WlsxTrapRogueIfoURL_Type()
)
wlsxTrapRogueIfoURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapRogueIfoURL.setStatus("current")
_WlsxTrapVlanId_Type = Integer32
_WlsxTrapVlanId_Object = MibScalar
wlsxTrapVlanId = _WlsxTrapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 23),
    _WlsxTrapVlanId_Type()
)
wlsxTrapVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVlanId.setStatus("current")
_WlsxTrapAdminStatus_Type = ArubaEnableValue
_WlsxTrapAdminStatus_Object = MibScalar
wlsxTrapAdminStatus = _WlsxTrapAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 24),
    _WlsxTrapAdminStatus_Type()
)
wlsxTrapAdminStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAdminStatus.setStatus("current")
_WlsxTrapOperStatus_Type = ArubaOperStateValue
_WlsxTrapOperStatus_Object = MibScalar
wlsxTrapOperStatus = _WlsxTrapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 25),
    _WlsxTrapOperStatus_Type()
)
wlsxTrapOperStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapOperStatus.setStatus("current")


class _WlsxTrapAuthServerName_Type(DisplayString):
    """Custom type wlsxTrapAuthServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapAuthServerName_Type.__name__ = "DisplayString"
_WlsxTrapAuthServerName_Object = MibScalar
wlsxTrapAuthServerName = _WlsxTrapAuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 26),
    _WlsxTrapAuthServerName_Type()
)
wlsxTrapAuthServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAuthServerName.setStatus("current")
_WlsxTrapAuthServerTimeout_Type = Integer32
_WlsxTrapAuthServerTimeout_Object = MibScalar
wlsxTrapAuthServerTimeout = _WlsxTrapAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 27),
    _WlsxTrapAuthServerTimeout_Type()
)
wlsxTrapAuthServerTimeout.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAuthServerTimeout.setStatus("current")
_WlsxTrapCardSlot_Type = Integer32
_WlsxTrapCardSlot_Object = MibScalar
wlsxTrapCardSlot = _WlsxTrapCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 28),
    _WlsxTrapCardSlot_Type()
)
wlsxTrapCardSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapCardSlot.setStatus("current")


class _WlsxTrapTemperatureValue_Type(DisplayString):
    """Custom type wlsxTrapTemperatureValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapTemperatureValue_Type.__name__ = "DisplayString"
_WlsxTrapTemperatureValue_Object = MibScalar
wlsxTrapTemperatureValue = _WlsxTrapTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 29),
    _WlsxTrapTemperatureValue_Type()
)
wlsxTrapTemperatureValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTemperatureValue.setStatus("current")


class _WlsxTrapProcessName_Type(DisplayString):
    """Custom type wlsxTrapProcessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapProcessName_Type.__name__ = "DisplayString"
_WlsxTrapProcessName_Object = MibScalar
wlsxTrapProcessName = _WlsxTrapProcessName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 30),
    _WlsxTrapProcessName_Type()
)
wlsxTrapProcessName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapProcessName.setStatus("current")
_WlsxTrapFanNumber_Type = Integer32
_WlsxTrapFanNumber_Object = MibScalar
wlsxTrapFanNumber = _WlsxTrapFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 31),
    _WlsxTrapFanNumber_Type()
)
wlsxTrapFanNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapFanNumber.setStatus("current")


class _WlsxTrapVoltageType_Type(DisplayString):
    """Custom type wlsxTrapVoltageType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapVoltageType_Type.__name__ = "DisplayString"
_WlsxTrapVoltageType_Object = MibScalar
wlsxTrapVoltageType = _WlsxTrapVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 32),
    _WlsxTrapVoltageType_Type()
)
wlsxTrapVoltageType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVoltageType.setStatus("current")


class _WlsxTrapVoltageValue_Type(DisplayString):
    """Custom type wlsxTrapVoltageValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapVoltageValue_Type.__name__ = "DisplayString"
_WlsxTrapVoltageValue_Object = MibScalar
wlsxTrapVoltageValue = _WlsxTrapVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 33),
    _WlsxTrapVoltageValue_Type()
)
wlsxTrapVoltageValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVoltageValue.setStatus("current")
_WlsxTrapStationBlackListReason_Type = ArubaBlackListReason
_WlsxTrapStationBlackListReason_Object = MibScalar
wlsxTrapStationBlackListReason = _WlsxTrapStationBlackListReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 34),
    _WlsxTrapStationBlackListReason_Type()
)
wlsxTrapStationBlackListReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapStationBlackListReason.setStatus("current")
_WlsxTrapSpoofedIpAddress_Type = IpAddress
_WlsxTrapSpoofedIpAddress_Object = MibScalar
wlsxTrapSpoofedIpAddress = _WlsxTrapSpoofedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 35),
    _WlsxTrapSpoofedIpAddress_Type()
)
wlsxTrapSpoofedIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSpoofedIpAddress.setStatus("current")
_WlsxTrapSpoofedOldPhyAddress_Type = MacAddress
_WlsxTrapSpoofedOldPhyAddress_Object = MibScalar
wlsxTrapSpoofedOldPhyAddress = _WlsxTrapSpoofedOldPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 36),
    _WlsxTrapSpoofedOldPhyAddress_Type()
)
wlsxTrapSpoofedOldPhyAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSpoofedOldPhyAddress.setStatus("current")
_WlsxTrapSpoofedNewPhyAddress_Type = MacAddress
_WlsxTrapSpoofedNewPhyAddress_Object = MibScalar
wlsxTrapSpoofedNewPhyAddress = _WlsxTrapSpoofedNewPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 37),
    _WlsxTrapSpoofedNewPhyAddress_Type()
)
wlsxTrapSpoofedNewPhyAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSpoofedNewPhyAddress.setStatus("current")


class _WlsxTrapDBName_Type(DisplayString):
    """Custom type wlsxTrapDBName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapDBName_Type.__name__ = "DisplayString"
_WlsxTrapDBName_Object = MibScalar
wlsxTrapDBName = _WlsxTrapDBName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 38),
    _WlsxTrapDBName_Type()
)
wlsxTrapDBName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapDBName.setStatus("current")


class _WlsxTrapDBUserName_Type(DisplayString):
    """Custom type wlsxTrapDBUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapDBUserName_Type.__name__ = "DisplayString"
_WlsxTrapDBUserName_Object = MibScalar
wlsxTrapDBUserName = _WlsxTrapDBUserName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 39),
    _WlsxTrapDBUserName_Type()
)
wlsxTrapDBUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapDBUserName.setStatus("current")


class _WlsxTrapDBIpAddress_Type(DisplayString):
    """Custom type wlsxTrapDBIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapDBIpAddress_Type.__name__ = "DisplayString"
_WlsxTrapDBIpAddress_Object = MibScalar
wlsxTrapDBIpAddress = _WlsxTrapDBIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 40),
    _WlsxTrapDBIpAddress_Type()
)
wlsxTrapDBIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapDBIpAddress.setStatus("current")
_WlsxTrapDBType_Type = ArubaDBType
_WlsxTrapDBType_Object = MibScalar
wlsxTrapDBType = _WlsxTrapDBType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 41),
    _WlsxTrapDBType_Type()
)
wlsxTrapDBType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapDBType.setStatus("current")
_WlsxTrapVrrpID_Type = Integer32
_WlsxTrapVrrpID_Object = MibScalar
wlsxTrapVrrpID = _WlsxTrapVrrpID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 42),
    _WlsxTrapVrrpID_Type()
)
wlsxTrapVrrpID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVrrpID.setStatus("current")
_WlsxTrapVrrpMasterIp_Type = IpAddress
_WlsxTrapVrrpMasterIp_Object = MibScalar
wlsxTrapVrrpMasterIp = _WlsxTrapVrrpMasterIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 43),
    _WlsxTrapVrrpMasterIp_Type()
)
wlsxTrapVrrpMasterIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVrrpMasterIp.setStatus("current")
_WlsxTrapVrrpOperState_Type = ArubaVrrpState
_WlsxTrapVrrpOperState_Object = MibScalar
wlsxTrapVrrpOperState = _WlsxTrapVrrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 44),
    _WlsxTrapVrrpOperState_Type()
)
wlsxTrapVrrpOperState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVrrpOperState.setStatus("current")


class _WlsxTrapESIServerGrpName_Type(DisplayString):
    """Custom type wlsxTrapESIServerGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapESIServerGrpName_Type.__name__ = "DisplayString"
_WlsxTrapESIServerGrpName_Object = MibScalar
wlsxTrapESIServerGrpName = _WlsxTrapESIServerGrpName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 45),
    _WlsxTrapESIServerGrpName_Type()
)
wlsxTrapESIServerGrpName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapESIServerGrpName.setStatus("current")


class _WlsxTrapESIServerName_Type(DisplayString):
    """Custom type wlsxTrapESIServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapESIServerName_Type.__name__ = "DisplayString"
_WlsxTrapESIServerName_Object = MibScalar
wlsxTrapESIServerName = _WlsxTrapESIServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 46),
    _WlsxTrapESIServerName_Type()
)
wlsxTrapESIServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapESIServerName.setStatus("current")
_WlsxTrapESIServerIpAddress_Type = IpAddress
_WlsxTrapESIServerIpAddress_Object = MibScalar
wlsxTrapESIServerIpAddress = _WlsxTrapESIServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 47),
    _WlsxTrapESIServerIpAddress_Type()
)
wlsxTrapESIServerIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapESIServerIpAddress.setStatus("current")
_WlsxTrapLicenseDaysRemaining_Type = Integer32
_WlsxTrapLicenseDaysRemaining_Object = MibScalar
wlsxTrapLicenseDaysRemaining = _WlsxTrapLicenseDaysRemaining_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 48),
    _WlsxTrapLicenseDaysRemaining_Type()
)
wlsxTrapLicenseDaysRemaining.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapLicenseDaysRemaining.setStatus("current")
_WlsxTrapSwitchIp_Type = IpAddress
_WlsxTrapSwitchIp_Object = MibScalar
wlsxTrapSwitchIp = _WlsxTrapSwitchIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 49),
    _WlsxTrapSwitchIp_Type()
)
wlsxTrapSwitchIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSwitchIp.setStatus("current")
_WlsxTrapSwitchRole_Type = ArubaSwitchRole
_WlsxTrapSwitchRole_Object = MibScalar
wlsxTrapSwitchRole = _WlsxTrapSwitchRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 50),
    _WlsxTrapSwitchRole_Type()
)
wlsxTrapSwitchRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSwitchRole.setStatus("current")
_WlsxTrapUserIpAddress_Type = IpAddress
_WlsxTrapUserIpAddress_Object = MibScalar
wlsxTrapUserIpAddress = _WlsxTrapUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 51),
    _WlsxTrapUserIpAddress_Type()
)
wlsxTrapUserIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUserIpAddress.setStatus("current")
_WlsxTrapUserPhyAddress_Type = MacAddress
_WlsxTrapUserPhyAddress_Object = MibScalar
wlsxTrapUserPhyAddress = _WlsxTrapUserPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 52),
    _WlsxTrapUserPhyAddress_Type()
)
wlsxTrapUserPhyAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUserPhyAddress.setStatus("current")


class _WlsxTrapUserName_Type(DisplayString):
    """Custom type wlsxTrapUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapUserName_Type.__name__ = "DisplayString"
_WlsxTrapUserName_Object = MibScalar
wlsxTrapUserName = _WlsxTrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 53),
    _WlsxTrapUserName_Type()
)
wlsxTrapUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUserName.setStatus("current")


class _WlsxTrapUserRole_Type(DisplayString):
    """Custom type wlsxTrapUserRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapUserRole_Type.__name__ = "DisplayString"
_WlsxTrapUserRole_Object = MibScalar
wlsxTrapUserRole = _WlsxTrapUserRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 54),
    _WlsxTrapUserRole_Type()
)
wlsxTrapUserRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUserRole.setStatus("current")
_WlsxTrapUserAuthenticationMethod_Type = ArubaAuthenticationMethods
_WlsxTrapUserAuthenticationMethod_Object = MibScalar
wlsxTrapUserAuthenticationMethod = _WlsxTrapUserAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 55),
    _WlsxTrapUserAuthenticationMethod_Type()
)
wlsxTrapUserAuthenticationMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUserAuthenticationMethod.setStatus("current")
_WlsxTrapAPRadioNumber_Type = Integer32
_WlsxTrapAPRadioNumber_Object = MibScalar
wlsxTrapAPRadioNumber = _WlsxTrapAPRadioNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 56),
    _WlsxTrapAPRadioNumber_Type()
)
wlsxTrapAPRadioNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPRadioNumber.setStatus("current")


class _WlsxTrapRogueInfoURL_Type(DisplayString):
    """Custom type wlsxTrapRogueInfoURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapRogueInfoURL_Type.__name__ = "DisplayString"
_WlsxTrapRogueInfoURL_Object = MibScalar
wlsxTrapRogueInfoURL = _WlsxTrapRogueInfoURL_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 57),
    _WlsxTrapRogueInfoURL_Type()
)
wlsxTrapRogueInfoURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapRogueInfoURL.setStatus("current")


class _WlsxTrapInterferingAPInfoURL_Type(DisplayString):
    """Custom type wlsxTrapInterferingAPInfoURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapInterferingAPInfoURL_Type.__name__ = "DisplayString"
_WlsxTrapInterferingAPInfoURL_Object = MibScalar
wlsxTrapInterferingAPInfoURL = _WlsxTrapInterferingAPInfoURL_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 58),
    _WlsxTrapInterferingAPInfoURL_Type()
)
wlsxTrapInterferingAPInfoURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapInterferingAPInfoURL.setStatus("current")
_WlsxTrapPortNumber_Type = Integer32
_WlsxTrapPortNumber_Object = MibScalar
wlsxTrapPortNumber = _WlsxTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 59),
    _WlsxTrapPortNumber_Type()
)
wlsxTrapPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapPortNumber.setStatus("current")
_WlsxTrapTime_Type = DateAndTime
_WlsxTrapTime_Object = MibScalar
wlsxTrapTime = _WlsxTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 60),
    _WlsxTrapTime_Type()
)
wlsxTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTime.setStatus("current")
_WlsxTrapHostIp_Type = IpAddress
_WlsxTrapHostIp_Object = MibScalar
wlsxTrapHostIp = _WlsxTrapHostIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 61),
    _WlsxTrapHostIp_Type()
)
wlsxTrapHostIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapHostIp.setStatus("current")
_WlsxTrapHostPort_Type = Integer32
_WlsxTrapHostPort_Object = MibScalar
wlsxTrapHostPort = _WlsxTrapHostPort_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 62),
    _WlsxTrapHostPort_Type()
)
wlsxTrapHostPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapHostPort.setStatus("current")
_WlsxTrapConfigurationId_Type = Integer32
_WlsxTrapConfigurationId_Object = MibScalar
wlsxTrapConfigurationId = _WlsxTrapConfigurationId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 63),
    _WlsxTrapConfigurationId_Type()
)
wlsxTrapConfigurationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapConfigurationId.setStatus("current")


class _WlsxTrapCTSURL_Type(DisplayString):
    """Custom type wlsxTrapCTSURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapCTSURL_Type.__name__ = "DisplayString"
_WlsxTrapCTSURL_Object = MibScalar
wlsxTrapCTSURL = _WlsxTrapCTSURL_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 64),
    _WlsxTrapCTSURL_Type()
)
wlsxTrapCTSURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapCTSURL.setStatus("current")


class _WlsxTrapCTSTransferType_Type(DisplayString):
    """Custom type wlsxTrapCTSTransferType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapCTSTransferType_Type.__name__ = "DisplayString"
_WlsxTrapCTSTransferType_Object = MibScalar
wlsxTrapCTSTransferType = _WlsxTrapCTSTransferType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 65),
    _WlsxTrapCTSTransferType_Type()
)
wlsxTrapCTSTransferType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapCTSTransferType.setStatus("current")
_WlsxTrapConfigurationState_Type = ArubaConfigurationState
_WlsxTrapConfigurationState_Object = MibScalar
wlsxTrapConfigurationState = _WlsxTrapConfigurationState_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 66),
    _WlsxTrapConfigurationState_Type()
)
wlsxTrapConfigurationState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapConfigurationState.setStatus("current")


class _WlsxTrapUpdateFailureReason_Type(DisplayString):
    """Custom type wlsxTrapUpdateFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapUpdateFailureReason_Type.__name__ = "DisplayString"
_WlsxTrapUpdateFailureReason_Object = MibScalar
wlsxTrapUpdateFailureReason = _WlsxTrapUpdateFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 67),
    _WlsxTrapUpdateFailureReason_Type()
)
wlsxTrapUpdateFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUpdateFailureReason.setStatus("current")


class _WlsxTrapUpdateFailedObj_Type(DisplayString):
    """Custom type wlsxTrapUpdateFailedObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapUpdateFailedObj_Type.__name__ = "DisplayString"
_WlsxTrapUpdateFailedObj_Object = MibScalar
wlsxTrapUpdateFailedObj = _WlsxTrapUpdateFailedObj_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 68),
    _WlsxTrapUpdateFailedObj_Type()
)
wlsxTrapUpdateFailedObj.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUpdateFailedObj.setStatus("current")
_WlsxTrapTableEntryChangeType_Type = ArubaConfigurationChangeType
_WlsxTrapTableEntryChangeType_Object = MibScalar
wlsxTrapTableEntryChangeType = _WlsxTrapTableEntryChangeType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 69),
    _WlsxTrapTableEntryChangeType_Type()
)
wlsxTrapTableEntryChangeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTableEntryChangeType.setStatus("current")


class _WlsxTrapGlobalConfigObj_Type(DisplayString):
    """Custom type wlsxTrapGlobalConfigObj based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapGlobalConfigObj_Type.__name__ = "DisplayString"
_WlsxTrapGlobalConfigObj_Object = MibScalar
wlsxTrapGlobalConfigObj = _WlsxTrapGlobalConfigObj_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 70),
    _WlsxTrapGlobalConfigObj_Type()
)
wlsxTrapGlobalConfigObj.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapGlobalConfigObj.setStatus("current")
_WlsxTrapTableGenNumber_Type = Integer32
_WlsxTrapTableGenNumber_Object = MibScalar
wlsxTrapTableGenNumber = _WlsxTrapTableGenNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 71),
    _WlsxTrapTableGenNumber_Type()
)
wlsxTrapTableGenNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTableGenNumber.setStatus("current")
_WlsxTrapLicenseId_Type = Integer32
_WlsxTrapLicenseId_Object = MibScalar
wlsxTrapLicenseId = _WlsxTrapLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 72),
    _WlsxTrapLicenseId_Type()
)
wlsxTrapLicenseId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapLicenseId.setStatus("current")
_WlsxTrapConfidenceLevel_Type = Integer32
_WlsxTrapConfidenceLevel_Object = MibScalar
wlsxTrapConfidenceLevel = _WlsxTrapConfidenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 73),
    _WlsxTrapConfidenceLevel_Type()
)
wlsxTrapConfidenceLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapConfidenceLevel.setStatus("current")


class _WlsxTrapMissingLicenses_Type(DisplayString):
    """Custom type wlsxTrapMissingLicenses based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapMissingLicenses_Type.__name__ = "DisplayString"
_WlsxTrapMissingLicenses_Object = MibScalar
wlsxTrapMissingLicenses = _WlsxTrapMissingLicenses_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 74),
    _WlsxTrapMissingLicenses_Type()
)
wlsxTrapMissingLicenses.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapMissingLicenses.setStatus("current")
_WlsxVoiceCurrentNumCdr_Type = Integer32
_WlsxVoiceCurrentNumCdr_Object = MibScalar
wlsxVoiceCurrentNumCdr = _WlsxVoiceCurrentNumCdr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 75),
    _WlsxVoiceCurrentNumCdr_Type()
)
wlsxVoiceCurrentNumCdr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxVoiceCurrentNumCdr.setStatus("current")
_WlsxTrapTunnelId_Type = Integer32
_WlsxTrapTunnelId_Object = MibScalar
wlsxTrapTunnelId = _WlsxTrapTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 76),
    _WlsxTrapTunnelId_Type()
)
wlsxTrapTunnelId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTunnelId.setStatus("current")
_WlsxTrapTunnelStatus_Type = Integer32
_WlsxTrapTunnelStatus_Object = MibScalar
wlsxTrapTunnelStatus = _WlsxTrapTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 77),
    _WlsxTrapTunnelStatus_Type()
)
wlsxTrapTunnelStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTunnelStatus.setStatus("current")


class _WlsxTrapTunnelUpReason_Type(DisplayString):
    """Custom type wlsxTrapTunnelUpReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapTunnelUpReason_Type.__name__ = "DisplayString"
_WlsxTrapTunnelUpReason_Object = MibScalar
wlsxTrapTunnelUpReason = _WlsxTrapTunnelUpReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 78),
    _WlsxTrapTunnelUpReason_Type()
)
wlsxTrapTunnelUpReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTunnelUpReason.setStatus("current")


class _WlsxTrapTunnelDownReason_Type(DisplayString):
    """Custom type wlsxTrapTunnelDownReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapTunnelDownReason_Type.__name__ = "DisplayString"
_WlsxTrapTunnelDownReason_Object = MibScalar
wlsxTrapTunnelDownReason = _WlsxTrapTunnelDownReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 79),
    _WlsxTrapTunnelDownReason_Type()
)
wlsxTrapTunnelDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTunnelDownReason.setStatus("current")


class _WlsxTrapApSerialNumber_Type(DisplayString):
    """Custom type wlsxTrapApSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapApSerialNumber_Type.__name__ = "DisplayString"
_WlsxTrapApSerialNumber_Object = MibScalar
wlsxTrapApSerialNumber = _WlsxTrapApSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 80),
    _WlsxTrapApSerialNumber_Type()
)
wlsxTrapApSerialNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapApSerialNumber.setStatus("current")


class _WlsxTrapTimeStr_Type(DisplayString):
    """Custom type wlsxTrapTimeStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapTimeStr_Type.__name__ = "DisplayString"
_WlsxTrapTimeStr_Object = MibScalar
wlsxTrapTimeStr = _WlsxTrapTimeStr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 81),
    _WlsxTrapTimeStr_Type()
)
wlsxTrapTimeStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapTimeStr.setStatus("current")
_WlsxTrapMasterIp_Type = IpAddress
_WlsxTrapMasterIp_Object = MibScalar
wlsxTrapMasterIp = _WlsxTrapMasterIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 82),
    _WlsxTrapMasterIp_Type()
)
wlsxTrapMasterIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapMasterIp.setStatus("current")
_WlsxTrapLocalIp_Type = IpAddress
_WlsxTrapLocalIp_Object = MibScalar
wlsxTrapLocalIp = _WlsxTrapLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 83),
    _WlsxTrapLocalIp_Type()
)
wlsxTrapLocalIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapLocalIp.setStatus("current")


class _WlsxTrapMasterName_Type(DisplayString):
    """Custom type wlsxTrapMasterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapMasterName_Type.__name__ = "DisplayString"
_WlsxTrapMasterName_Object = MibScalar
wlsxTrapMasterName = _WlsxTrapMasterName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 84),
    _WlsxTrapMasterName_Type()
)
wlsxTrapMasterName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapMasterName.setStatus("current")


class _WlsxTrapLocalName_Type(DisplayString):
    """Custom type wlsxTrapLocalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapLocalName_Type.__name__ = "DisplayString"
_WlsxTrapLocalName_Object = MibScalar
wlsxTrapLocalName = _WlsxTrapLocalName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 85),
    _WlsxTrapLocalName_Type()
)
wlsxTrapLocalName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapLocalName.setStatus("current")
_WlsxTrapPrimaryControllerIp_Type = IpAddress
_WlsxTrapPrimaryControllerIp_Object = MibScalar
wlsxTrapPrimaryControllerIp = _WlsxTrapPrimaryControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 86),
    _WlsxTrapPrimaryControllerIp_Type()
)
wlsxTrapPrimaryControllerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapPrimaryControllerIp.setStatus("current")
_WlsxTrapBackupControllerIp_Type = IpAddress
_WlsxTrapBackupControllerIp_Object = MibScalar
wlsxTrapBackupControllerIp = _WlsxTrapBackupControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 87),
    _WlsxTrapBackupControllerIp_Type()
)
wlsxTrapBackupControllerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapBackupControllerIp.setStatus("current")


class _WlsxTrapSpoofedFrameType_Type(DisplayString):
    """Custom type wlsxTrapSpoofedFrameType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapSpoofedFrameType_Type.__name__ = "DisplayString"
_WlsxTrapSpoofedFrameType_Object = MibScalar
wlsxTrapSpoofedFrameType = _WlsxTrapSpoofedFrameType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 88),
    _WlsxTrapSpoofedFrameType_Type()
)
wlsxTrapSpoofedFrameType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapSpoofedFrameType.setStatus("current")


class _WlsxTrapAssociationType_Type(DisplayString):
    """Custom type wlsxTrapAssociationType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapAssociationType_Type.__name__ = "DisplayString"
_WlsxTrapAssociationType_Object = MibScalar
wlsxTrapAssociationType = _WlsxTrapAssociationType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 89),
    _WlsxTrapAssociationType_Type()
)
wlsxTrapAssociationType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAssociationType.setStatus("current")
_WlsxTrapDeviceIpAddress_Type = IpAddress
_WlsxTrapDeviceIpAddress_Object = MibScalar
wlsxTrapDeviceIpAddress = _WlsxTrapDeviceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 90),
    _WlsxTrapDeviceIpAddress_Type()
)
wlsxTrapDeviceIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapDeviceIpAddress.setStatus("current")
_WlsxTrapDeviceMac_Type = MacAddress
_WlsxTrapDeviceMac_Object = MibScalar
wlsxTrapDeviceMac = _WlsxTrapDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 91),
    _WlsxTrapDeviceMac_Type()
)
wlsxTrapDeviceMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapDeviceMac.setStatus("current")
_WlsxTrapVcIpAddress_Type = IpAddress
_WlsxTrapVcIpAddress_Object = MibScalar
wlsxTrapVcIpAddress = _WlsxTrapVcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 92),
    _WlsxTrapVcIpAddress_Type()
)
wlsxTrapVcIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVcIpAddress.setStatus("current")
_WlsxTrapVcMacAddress_Type = MacAddress
_WlsxTrapVcMacAddress_Object = MibScalar
wlsxTrapVcMacAddress = _WlsxTrapVcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 93),
    _WlsxTrapVcMacAddress_Type()
)
wlsxTrapVcMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapVcMacAddress.setStatus("current")


class _WlsxTrapAPName_Type(DisplayString):
    """Custom type wlsxTrapAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WlsxTrapAPName_Type.__name__ = "DisplayString"
_WlsxTrapAPName_Object = MibScalar
wlsxTrapAPName = _WlsxTrapAPName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 94),
    _WlsxTrapAPName_Type()
)
wlsxTrapAPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPName.setStatus("current")
_WlsxTrapApMode_Type = Integer32
_WlsxTrapApMode_Object = MibScalar
wlsxTrapApMode = _WlsxTrapApMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 95),
    _WlsxTrapApMode_Type()
)
wlsxTrapApMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapApMode.setStatus("current")
_WlsxTrapAPPrevChannel_Type = Integer32
_WlsxTrapAPPrevChannel_Object = MibScalar
wlsxTrapAPPrevChannel = _WlsxTrapAPPrevChannel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 96),
    _WlsxTrapAPPrevChannel_Type()
)
wlsxTrapAPPrevChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPPrevChannel.setStatus("current")
_WlsxTrapAPPrevChannelSec_Type = ArubaHTExtChannel
_WlsxTrapAPPrevChannelSec_Object = MibScalar
wlsxTrapAPPrevChannelSec = _WlsxTrapAPPrevChannelSec_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 97),
    _WlsxTrapAPPrevChannelSec_Type()
)
wlsxTrapAPPrevChannelSec.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPPrevChannelSec.setStatus("current")
_WlsxTrapAPPrevTxPower_Type = Integer32
_WlsxTrapAPPrevTxPower_Object = MibScalar
wlsxTrapAPPrevTxPower = _WlsxTrapAPPrevTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 98),
    _WlsxTrapAPPrevTxPower_Type()
)
wlsxTrapAPPrevTxPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPPrevTxPower.setStatus("current")
_WlsxTrapAPCurMode_Type = ArubaAccessPointMode
_WlsxTrapAPCurMode_Object = MibScalar
wlsxTrapAPCurMode = _WlsxTrapAPCurMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 99),
    _WlsxTrapAPCurMode_Type()
)
wlsxTrapAPCurMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPCurMode.setStatus("current")
_WlsxTrapAPPrevMode_Type = ArubaAccessPointMode
_WlsxTrapAPPrevMode_Object = MibScalar
wlsxTrapAPPrevMode = _WlsxTrapAPPrevMode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 100),
    _WlsxTrapAPPrevMode_Type()
)
wlsxTrapAPPrevMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPPrevMode.setStatus("current")
_WlsxTrapAPARMChangeReason_Type = ArubaARMChangeReason
_WlsxTrapAPARMChangeReason_Object = MibScalar
wlsxTrapAPARMChangeReason = _WlsxTrapAPARMChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 101),
    _WlsxTrapAPARMChangeReason_Type()
)
wlsxTrapAPARMChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPARMChangeReason.setStatus("current")
_WlsxTrapAPChannelSec_Type = ArubaHTExtChannel
_WlsxTrapAPChannelSec_Object = MibScalar
wlsxTrapAPChannelSec = _WlsxTrapAPChannelSec_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 102),
    _WlsxTrapAPChannelSec_Type()
)
wlsxTrapAPChannelSec.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPChannelSec.setStatus("current")
_WlsxTrapUserAttributeChangeType_Type = ArubaConfigurationChangeType
_WlsxTrapUserAttributeChangeType_Object = MibScalar
wlsxTrapUserAttributeChangeType = _WlsxTrapUserAttributeChangeType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 103),
    _WlsxTrapUserAttributeChangeType_Type()
)
wlsxTrapUserAttributeChangeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUserAttributeChangeType.setStatus("current")
_WlsxTrapApControllerIp_Type = IpAddress
_WlsxTrapApControllerIp_Object = MibScalar
wlsxTrapApControllerIp = _WlsxTrapApControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 104),
    _WlsxTrapApControllerIp_Type()
)
wlsxTrapApControllerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapApControllerIp.setStatus("current")
_WlsxTrapApMasterStatus_Type = ArubaAPMasterStatus
_WlsxTrapApMasterStatus_Object = MibScalar
wlsxTrapApMasterStatus = _WlsxTrapApMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 105),
    _WlsxTrapApMasterStatus_Type()
)
wlsxTrapApMasterStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapApMasterStatus.setStatus("current")


class _WlsxTrapCaName_Type(DisplayString):
    """Custom type wlsxTrapCaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapCaName_Type.__name__ = "DisplayString"
_WlsxTrapCaName_Object = MibScalar
wlsxTrapCaName = _WlsxTrapCaName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 106),
    _WlsxTrapCaName_Type()
)
wlsxTrapCaName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapCaName.setStatus("current")


class _WlsxTrapCrlName_Type(DisplayString):
    """Custom type wlsxTrapCrlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapCrlName_Type.__name__ = "DisplayString"
_WlsxTrapCrlName_Object = MibScalar
wlsxTrapCrlName = _WlsxTrapCrlName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 107),
    _WlsxTrapCrlName_Type()
)
wlsxTrapCrlName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapCrlName.setStatus("current")
_WlsxTrapCount_Type = Integer32
_WlsxTrapCount_Object = MibScalar
wlsxTrapCount = _WlsxTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 108),
    _WlsxTrapCount_Type()
)
wlsxTrapCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapCount.setStatus("current")
_WlsxTrapAPPreviousUplinkType_Type = ArubaAPUplinkType
_WlsxTrapAPPreviousUplinkType_Object = MibScalar
wlsxTrapAPPreviousUplinkType = _WlsxTrapAPPreviousUplinkType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 130),
    _WlsxTrapAPPreviousUplinkType_Type()
)
wlsxTrapAPPreviousUplinkType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPPreviousUplinkType.setStatus("current")
_WlsxTrapAPPreviousUplinkActiveTime_Type = TimeTicks
_WlsxTrapAPPreviousUplinkActiveTime_Object = MibScalar
wlsxTrapAPPreviousUplinkActiveTime = _WlsxTrapAPPreviousUplinkActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 131),
    _WlsxTrapAPPreviousUplinkActiveTime_Type()
)
wlsxTrapAPPreviousUplinkActiveTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPPreviousUplinkActiveTime.setStatus("current")
_WlsxTrapAPActiveUplinkType_Type = ArubaAPUplinkType
_WlsxTrapAPActiveUplinkType_Object = MibScalar
wlsxTrapAPActiveUplinkType = _WlsxTrapAPActiveUplinkType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 132),
    _WlsxTrapAPActiveUplinkType_Type()
)
wlsxTrapAPActiveUplinkType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPActiveUplinkType.setStatus("current")
_WlsxTrapAPUplinkChangeReason_Type = ArubaAPUplinkChangeReason
_WlsxTrapAPUplinkChangeReason_Object = MibScalar
wlsxTrapAPUplinkChangeReason = _WlsxTrapAPUplinkChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 133),
    _WlsxTrapAPUplinkChangeReason_Type()
)
wlsxTrapAPUplinkChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPUplinkChangeReason.setStatus("current")


class _WlsxTrapAPManagedModeConfigFailure_Type(DisplayString):
    """Custom type wlsxTrapAPManagedModeConfigFailure based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapAPManagedModeConfigFailure_Type.__name__ = "DisplayString"
_WlsxTrapAPManagedModeConfigFailure_Object = MibScalar
wlsxTrapAPManagedModeConfigFailure = _WlsxTrapAPManagedModeConfigFailure_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 138),
    _WlsxTrapAPManagedModeConfigFailure_Type()
)
wlsxTrapAPManagedModeConfigFailure.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPManagedModeConfigFailure.setStatus("current")
_WlsxTrapAuthServerAddress_Type = IpAddress
_WlsxTrapAuthServerAddress_Object = MibScalar
wlsxTrapAuthServerAddress = _WlsxTrapAuthServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 139),
    _WlsxTrapAuthServerAddress_Type()
)
wlsxTrapAuthServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAuthServerAddress.setStatus("current")


class _WlsxTrapPortalServerName_Type(DisplayString):
    """Custom type wlsxTrapPortalServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapPortalServerName_Type.__name__ = "DisplayString"
_WlsxTrapPortalServerName_Object = MibScalar
wlsxTrapPortalServerName = _WlsxTrapPortalServerName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 140),
    _WlsxTrapPortalServerName_Type()
)
wlsxTrapPortalServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapPortalServerName.setStatus("current")


class _WlsxTrapPortalServerAddress_Type(DisplayString):
    """Custom type wlsxTrapPortalServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapPortalServerAddress_Type.__name__ = "DisplayString"
_WlsxTrapPortalServerAddress_Object = MibScalar
wlsxTrapPortalServerAddress = _WlsxTrapPortalServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 141),
    _WlsxTrapPortalServerAddress_Type()
)
wlsxTrapPortalServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapPortalServerAddress.setStatus("current")
_WlsxTrapPortalServerDownReason_Type = ArubaPortalServerDownReason
_WlsxTrapPortalServerDownReason_Object = MibScalar
wlsxTrapPortalServerDownReason = _WlsxTrapPortalServerDownReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 142),
    _WlsxTrapPortalServerDownReason_Type()
)
wlsxTrapPortalServerDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapPortalServerDownReason.setStatus("current")


class _WlsxTrapStationBlackListReasonStr_Type(DisplayString):
    """Custom type wlsxTrapStationBlackListReasonStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlsxTrapStationBlackListReasonStr_Type.__name__ = "DisplayString"
_WlsxTrapStationBlackListReasonStr_Object = MibScalar
wlsxTrapStationBlackListReasonStr = _WlsxTrapStationBlackListReasonStr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 144),
    _WlsxTrapStationBlackListReasonStr_Type()
)
wlsxTrapStationBlackListReasonStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapStationBlackListReasonStr.setStatus("current")


class _WlsxTrapAPUSBStatus_Type(DisplayString):
    """Custom type wlsxTrapAPUSBStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlsxTrapAPUSBStatus_Type.__name__ = "DisplayString"
_WlsxTrapAPUSBStatus_Object = MibScalar
wlsxTrapAPUSBStatus = _WlsxTrapAPUSBStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 147),
    _WlsxTrapAPUSBStatus_Type()
)
wlsxTrapAPUSBStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAPUSBStatus.setStatus("current")


class _WlsxTrapUSBVendorProductID_Type(DisplayString):
    """Custom type wlsxTrapUSBVendorProductID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlsxTrapUSBVendorProductID_Type.__name__ = "DisplayString"
_WlsxTrapUSBVendorProductID_Object = MibScalar
wlsxTrapUSBVendorProductID = _WlsxTrapUSBVendorProductID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 148),
    _WlsxTrapUSBVendorProductID_Type()
)
wlsxTrapUSBVendorProductID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapUSBVendorProductID.setStatus("current")


class _WlsxTrapAuthFailureReason_Type(DisplayString):
    """Custom type wlsxTrapAuthFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxTrapAuthFailureReason_Type.__name__ = "DisplayString"
_WlsxTrapAuthFailureReason_Object = MibScalar
wlsxTrapAuthFailureReason = _WlsxTrapAuthFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 1, 155),
    _WlsxTrapAuthFailureReason_Type()
)
wlsxTrapAuthFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wlsxTrapAuthFailureReason.setStatus("current")
_AiTrapDefinitionsGroup_ObjectIdentity = ObjectIdentity
aiTrapDefinitionsGroup = _AiTrapDefinitionsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2)
)

# Managed Objects groups


# Notification objects

wlsxNodeRateAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1003)
)
wlsxNodeRateAnomaly.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapFrameType"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxNodeRateAnomaly.setStatus(
        "current"
    )

wlsxNUserEntryCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1014)
)
wlsxNUserEntryCreated.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapUserIpAddress"),
        ("AI-AP-MIB", "wlsxTrapUserPhyAddress"))
)
if mibBuilder.loadTexts:
    wlsxNUserEntryCreated.setStatus(
        "current"
    )

wlsxNUserEntryDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1015)
)
wlsxNUserEntryDeleted.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapUserIpAddress"),
        ("AI-AP-MIB", "wlsxTrapUserPhyAddress"))
)
if mibBuilder.loadTexts:
    wlsxNUserEntryDeleted.setStatus(
        "current"
    )

wlsxNUserEntryAuthenticated = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1016)
)
wlsxNUserEntryAuthenticated.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapUserIpAddress"),
        ("AI-AP-MIB", "wlsxTrapUserPhyAddress"),
        ("AI-AP-MIB", "wlsxTrapUserName"),
        ("AI-AP-MIB", "wlsxTrapUserAuthenticationMethod"),
        ("AI-AP-MIB", "wlsxTrapUserRole"))
)
if mibBuilder.loadTexts:
    wlsxNUserEntryAuthenticated.setStatus(
        "current"
    )

wlsxNUserEntryDeAuthenticated = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1017)
)
wlsxNUserEntryDeAuthenticated.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapUserIpAddress"),
        ("AI-AP-MIB", "wlsxTrapUserPhyAddress"))
)
if mibBuilder.loadTexts:
    wlsxNUserEntryDeAuthenticated.setStatus(
        "current"
    )

wlsxNUserAuthenticationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1018)
)
wlsxNUserAuthenticationFailed.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapUserName"),
        ("AI-AP-MIB", "wlsxTrapUserIpAddress"),
        ("AI-AP-MIB", "wlsxTrapUserPhyAddress"),
        ("AI-AP-MIB", "wlsxTrapAuthServerName"),
        ("AI-AP-MIB", "wlsxTrapAuthServerAddress"),
        ("AI-AP-MIB", "wlsxTrapAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPName"))
)
if mibBuilder.loadTexts:
    wlsxNUserAuthenticationFailed.setStatus(
        "current"
    )

wlsxNAuthServerReqTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1019)
)
wlsxNAuthServerReqTimedOut.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapUserName"),
        ("AI-AP-MIB", "wlsxTrapUserIpAddress"),
        ("AI-AP-MIB", "wlsxTrapUserPhyAddress"),
        ("AI-AP-MIB", "wlsxTrapAuthServerName"),
        ("AI-AP-MIB", "wlsxTrapAuthServerAddress"),
        ("AI-AP-MIB", "wlsxTrapAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPName"))
)
if mibBuilder.loadTexts:
    wlsxNAuthServerReqTimedOut.setStatus(
        "current"
    )

wlsxNAuthServerTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1020)
)
wlsxNAuthServerTimedOut.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAuthServerName"),
        ("AI-AP-MIB", "wlsxTrapAuthServerTimeout"))
)
if mibBuilder.loadTexts:
    wlsxNAuthServerTimedOut.setStatus(
        "current"
    )

wlsxNAuthServerIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1021)
)
wlsxNAuthServerIsUp.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAuthServerName"),
        ("AI-AP-MIB", "wlsxTrapAuthServerAddress"))
)
if mibBuilder.loadTexts:
    wlsxNAuthServerIsUp.setStatus(
        "current"
    )

wlsxNAccessPointIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1040)
)
wlsxNAccessPointIsUp.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    wlsxNAccessPointIsUp.setStatus(
        "current"
    )

wlsxNAccessPointIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1041)
)
wlsxNAccessPointIsDown.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    wlsxNAccessPointIsDown.setStatus(
        "current"
    )

wlsxNChannelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1043)
)
wlsxNChannelChanged.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNChannelChanged.setStatus(
        "current"
    )

wlsxNStationAddedToBlackList = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1044)
)
wlsxNStationAddedToBlackList.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapStationBlackListReason"),
        ("AI-AP-MIB", "wlsxTrapStationBlackListReasonStr"))
)
if mibBuilder.loadTexts:
    wlsxNStationAddedToBlackList.setStatus(
        "current"
    )

wlsxNStationRemovedFromBlackList = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1045)
)
wlsxNStationRemovedFromBlackList.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"))
)
if mibBuilder.loadTexts:
    wlsxNStationRemovedFromBlackList.setStatus(
        "current"
    )

wlsxNRadioAttributesChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1049)
)
wlsxNRadioAttributesChanged.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPIpAddress"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapAPTxPower"))
)
if mibBuilder.loadTexts:
    wlsxNRadioAttributesChanged.setStatus(
        "current"
    )

wlsxUnsecureAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1053)
)
wlsxUnsecureAPDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapMatchedMac"),
        ("AI-AP-MIB", "wlsxTrapMatchedIp"),
        ("AI-AP-MIB", "wlsxTrapRogueInfoURL"))
)
if mibBuilder.loadTexts:
    wlsxUnsecureAPDetected.setStatus(
        "current"
    )

wlsxUnsecureAPResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1054)
)
wlsxUnsecureAPResolved.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxUnsecureAPResolved.setStatus(
        "current"
    )

wlsxStaImpersonation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1055)
)
wlsxStaImpersonation.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxStaImpersonation.setStatus(
        "current"
    )

wlsxReservedChannelViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1056)
)
wlsxReservedChannelViolation.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxReservedChannelViolation.setStatus(
        "current"
    )

wlsxValidSSIDViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1057)
)
wlsxValidSSIDViolation.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxValidSSIDViolation.setStatus(
        "current"
    )

wlsxChannelMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1058)
)
wlsxChannelMisconfiguration.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxChannelMisconfiguration.setStatus(
        "current"
    )

wlsxOUIMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1059)
)
wlsxOUIMisconfiguration.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxOUIMisconfiguration.setStatus(
        "current"
    )

wlsxSSIDMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1060)
)
wlsxSSIDMisconfiguration.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxSSIDMisconfiguration.setStatus(
        "current"
    )

wlsxShortPreableMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1061)
)
wlsxShortPreableMisconfiguration.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxShortPreableMisconfiguration.setStatus(
        "current"
    )

wlsxWPAMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1062)
)
wlsxWPAMisconfiguration.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxWPAMisconfiguration.setStatus(
        "current"
    )

wlsxAdhocNetworkDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1063)
)
wlsxAdhocNetworkDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAdhocNetworkDetected.setStatus(
        "current"
    )

wlsxAdhocNetworkRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1064)
)
wlsxAdhocNetworkRemoved.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAdhocNetworkRemoved.setStatus(
        "current"
    )

wlsxStaPolicyViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1065)
)
wlsxStaPolicyViolation.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxStaPolicyViolation.setStatus(
        "current"
    )

wlsxRepeatWEPIVViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1066)
)
wlsxRepeatWEPIVViolation.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxRepeatWEPIVViolation.setStatus(
        "current"
    )

wlsxWeakWEPIVViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1067)
)
wlsxWeakWEPIVViolation.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxWeakWEPIVViolation.setStatus(
        "current"
    )

wlsxChannelInterferenceDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1068)
)
wlsxChannelInterferenceDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxChannelInterferenceDetected.setStatus(
        "current"
    )

wlsxChannelInterferenceCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1069)
)
wlsxChannelInterferenceCleared.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxChannelInterferenceCleared.setStatus(
        "current"
    )

wlsxAPInterferenceDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1070)
)
wlsxAPInterferenceDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAPInterferenceDetected.setStatus(
        "current"
    )

wlsxAPInterferenceCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1071)
)
wlsxAPInterferenceCleared.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAPInterferenceCleared.setStatus(
        "current"
    )

wlsxStaInterferenceDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1072)
)
wlsxStaInterferenceDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxStaInterferenceDetected.setStatus(
        "current"
    )

wlsxStaInterferenceCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1073)
)
wlsxStaInterferenceCleared.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxStaInterferenceCleared.setStatus(
        "current"
    )

wlsxFrameRetryRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1074)
)
wlsxFrameRetryRateExceeded.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxFrameRetryRateExceeded.setStatus(
        "current"
    )

wlsxFrameReceiveErrorRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1075)
)
wlsxFrameReceiveErrorRateExceeded.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapTargetAPChannel"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxFrameReceiveErrorRateExceeded.setStatus(
        "current"
    )

wlsxFrameFragmentationRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1076)
)
wlsxFrameFragmentationRateExceeded.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapTargetAPChannel"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxFrameFragmentationRateExceeded.setStatus(
        "current"
    )

wlsxFrameBandWidthRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1077)
)
wlsxFrameBandWidthRateExceeded.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxFrameBandWidthRateExceeded.setStatus(
        "current"
    )

wlsxFrameLowSpeedRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1078)
)
wlsxFrameLowSpeedRateExceeded.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxFrameLowSpeedRateExceeded.setStatus(
        "current"
    )

wlsxFrameNonUnicastRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1079)
)
wlsxFrameNonUnicastRateExceeded.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxFrameNonUnicastRateExceeded.setStatus(
        "current"
    )

wlsxLoadbalancingEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1080)
)
wlsxLoadbalancingEnabled.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxLoadbalancingEnabled.setStatus(
        "current"
    )

wlsxLoadbalancingDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1081)
)
wlsxLoadbalancingDisabled.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxLoadbalancingDisabled.setStatus(
        "current"
    )

wlsxChannelFrameRetryRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1082)
)
wlsxChannelFrameRetryRateExceeded.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxChannelFrameRetryRateExceeded.setStatus(
        "current"
    )

wlsxChannelFrameFragmentationRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1083)
)
wlsxChannelFrameFragmentationRateExceeded.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxChannelFrameFragmentationRateExceeded.setStatus(
        "current"
    )

wlsxChannelFrameErrorRateExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1084)
)
wlsxChannelFrameErrorRateExceeded.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxChannelFrameErrorRateExceeded.setStatus(
        "current"
    )

wlsxSignatureMatchAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1085)
)
wlsxSignatureMatchAP.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignatureMatchAP.setStatus(
        "current"
    )

wlsxSignatureMatchSta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1086)
)
wlsxSignatureMatchSta.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignatureMatchSta.setStatus(
        "current"
    )

wlsxChannelRateAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1087)
)
wlsxChannelRateAnomaly.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapFrameType"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxChannelRateAnomaly.setStatus(
        "current"
    )

wlsxNodeRateAnomalyAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1088)
)
wlsxNodeRateAnomalyAP.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapFrameType"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxNodeRateAnomalyAP.setStatus(
        "current"
    )

wlsxNodeRateAnomalySta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1089)
)
wlsxNodeRateAnomalySta.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapFrameType"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxNodeRateAnomalySta.setStatus(
        "current"
    )

wlsxEAPRateAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1090)
)
wlsxEAPRateAnomaly.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxEAPRateAnomaly.setStatus(
        "current"
    )

wlsxSignalAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1091)
)
wlsxSignalAnomaly.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxSignalAnomaly.setStatus(
        "current"
    )

wlsxSequenceNumberAnomalyAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1092)
)
wlsxSequenceNumberAnomalyAP.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSequenceNumberAnomalyAP.setStatus(
        "current"
    )

wlsxSequenceNumberAnomalySta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1093)
)
wlsxSequenceNumberAnomalySta.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSequenceNumberAnomalySta.setStatus(
        "current"
    )

wlsxDisconnectStationAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1094)
)
wlsxDisconnectStationAttack.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapFrameType"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxDisconnectStationAttack.setStatus(
        "current"
    )

wlsxApFloodAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1095)
)
wlsxApFloodAttack.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxApFloodAttack.setStatus(
        "current"
    )

wlsxAdhocNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1096)
)
wlsxAdhocNetwork.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxAdhocNetwork.setStatus(
        "current"
    )

wlsxWirelessBridge = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1097)
)
wlsxWirelessBridge.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTransmitterMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxWirelessBridge.setStatus(
        "current"
    )

wlsxInvalidMacOUIAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1098)
)
wlsxInvalidMacOUIAP.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAddressType"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxInvalidMacOUIAP.setStatus(
        "current"
    )

wlsxInvalidMacOUISta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1099)
)
wlsxInvalidMacOUISta.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAddressType"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxInvalidMacOUISta.setStatus(
        "current"
    )

wlsxWEPMisconfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1100)
)
wlsxWEPMisconfiguration.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxWEPMisconfiguration.setStatus(
        "current"
    )

wlsxStaRepeatWEPIVViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1101)
)
wlsxStaRepeatWEPIVViolation.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxStaRepeatWEPIVViolation.setStatus(
        "current"
    )

wlsxStaWeakWEPIVViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1102)
)
wlsxStaWeakWEPIVViolation.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxStaWeakWEPIVViolation.setStatus(
        "current"
    )

wlsxStaAssociatedToUnsecureAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1103)
)
wlsxStaAssociatedToUnsecureAP.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapRogueInfoURL"))
)
if mibBuilder.loadTexts:
    wlsxStaAssociatedToUnsecureAP.setStatus(
        "current"
    )

wlsxStaUnAssociatedFromUnsecureAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1104)
)
wlsxStaUnAssociatedFromUnsecureAP.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"))
)
if mibBuilder.loadTexts:
    wlsxStaUnAssociatedFromUnsecureAP.setStatus(
        "current"
    )

wlsxAdhocNetworkBridgeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1105)
)
wlsxAdhocNetworkBridgeDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAdhocNetworkBridgeDetected.setStatus(
        "current"
    )

wlsxInterferingApDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1106)
)
wlsxInterferingApDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapInterferingAPInfoURL"))
)
if mibBuilder.loadTexts:
    wlsxInterferingApDetected.setStatus(
        "current"
    )

wlsxColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1111)
)
wlsxColdStart.setObjects(
    ("AI-AP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxColdStart.setStatus(
        "current"
    )

wlsxWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1112)
)
wlsxWarmStart.setObjects(
    ("AI-AP-MIB", "wlsxTrapTime")
)
if mibBuilder.loadTexts:
    wlsxWarmStart.setStatus(
        "current"
    )

wlsxAPImpersonation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1113)
)
wlsxAPImpersonation.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAPImpersonation.setStatus(
        "current"
    )

wlsxNAuthServerIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1115)
)
wlsxNAuthServerIsDown.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAuthServerName"),
        ("AI-AP-MIB", "wlsxTrapAuthServerAddress"))
)
if mibBuilder.loadTexts:
    wlsxNAuthServerIsDown.setStatus(
        "current"
    )

wlsxWindowsBridgeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1129)
)
wlsxWindowsBridgeDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxWindowsBridgeDetected.setStatus(
        "current"
    )

wlsxSignAPNetstumbler = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1134)
)
wlsxSignAPNetstumbler.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignAPNetstumbler.setStatus(
        "current"
    )

wlsxSignStaNetstumbler = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1135)
)
wlsxSignStaNetstumbler.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignStaNetstumbler.setStatus(
        "current"
    )

wlsxSignAPAsleap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1136)
)
wlsxSignAPAsleap.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignAPAsleap.setStatus(
        "current"
    )

wlsxSignStaAsleap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1137)
)
wlsxSignStaAsleap.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignStaAsleap.setStatus(
        "current"
    )

wlsxSignAPAirjack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1138)
)
wlsxSignAPAirjack.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignAPAirjack.setStatus(
        "current"
    )

wlsxSignStaAirjack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1139)
)
wlsxSignStaAirjack.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignStaAirjack.setStatus(
        "current"
    )

wlsxSignAPNullProbeResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1140)
)
wlsxSignAPNullProbeResp.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignAPNullProbeResp.setStatus(
        "current"
    )

wlsxSignStaNullProbeResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1141)
)
wlsxSignStaNullProbeResp.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignStaNullProbeResp.setStatus(
        "current"
    )

wlsxSignAPDeauthBcast = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1142)
)
wlsxSignAPDeauthBcast.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignAPDeauthBcast.setStatus(
        "current"
    )

wlsxSignStaDeauthBcast = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1143)
)
wlsxSignStaDeauthBcast.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxSignStaDeauthBcast.setStatus(
        "current"
    )

wlsxWindowsBridgeDetectedAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1144)
)
wlsxWindowsBridgeDetectedAP.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxWindowsBridgeDetectedAP.setStatus(
        "current"
    )

wlsxWindowsBridgeDetectedSta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1145)
)
wlsxWindowsBridgeDetectedSta.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxWindowsBridgeDetectedSta.setStatus(
        "current"
    )

wlsxAdhocNetworkBridgeDetectedAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1146)
)
wlsxAdhocNetworkBridgeDetectedAP.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAdhocNetworkBridgeDetectedAP.setStatus(
        "current"
    )

wlsxAdhocNetworkBridgeDetectedSta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1147)
)
wlsxAdhocNetworkBridgeDetectedSta.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAdhocNetworkBridgeDetectedSta.setStatus(
        "current"
    )

wlsxDisconnectStationAttackAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1148)
)
wlsxDisconnectStationAttackAP.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapFrameType"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxDisconnectStationAttackAP.setStatus(
        "current"
    )

wlsxDisconnectStationAttackSta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1149)
)
wlsxDisconnectStationAttackSta.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapFrameType"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxDisconnectStationAttackSta.setStatus(
        "current"
    )

wlsxSuspectUnsecureAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1150)
)
wlsxSuspectUnsecureAPDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapMatchedMac"),
        ("AI-AP-MIB", "wlsxTrapMatchedIp"),
        ("AI-AP-MIB", "wlsxTrapConfidenceLevel"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapRogueInfoURL"))
)
if mibBuilder.loadTexts:
    wlsxSuspectUnsecureAPDetected.setStatus(
        "current"
    )

wlsxSuspectUnsecureAPResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1151)
)
wlsxSuspectUnsecureAPResolved.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"))
)
if mibBuilder.loadTexts:
    wlsxSuspectUnsecureAPResolved.setStatus(
        "current"
    )

wlsxHtGreenfieldSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1157)
)
wlsxHtGreenfieldSupported.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxHtGreenfieldSupported.setStatus(
        "current"
    )

wlsxHT40MHzIntoleranceAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1158)
)
wlsxHT40MHzIntoleranceAP.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxHT40MHzIntoleranceAP.setStatus(
        "current"
    )

wlsxHT40MHzIntoleranceSta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1159)
)
wlsxHT40MHzIntoleranceSta.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapFrameType"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxHT40MHzIntoleranceSta.setStatus(
        "current"
    )

wlsxNAuthServerAllInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1160)
)
wlsxNAuthServerAllInService.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapESIServerGrpName"))
)
if mibBuilder.loadTexts:
    wlsxNAuthServerAllInService.setStatus(
        "current"
    )

wlsxNAdhocNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1161)
)
wlsxNAdhocNetwork.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNAdhocNetwork.setStatus(
        "current"
    )

wlsxNAdhocNetworkBridgeDetectedAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1162)
)
wlsxNAdhocNetworkBridgeDetectedAP.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNAdhocNetworkBridgeDetectedAP.setStatus(
        "current"
    )

wlsxNAdhocNetworkBridgeDetectedSta = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1163)
)
wlsxNAdhocNetworkBridgeDetectedSta.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNAdhocNetworkBridgeDetectedSta.setStatus(
        "current"
    )

wlsxClientFloodAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1170)
)
wlsxClientFloodAttack.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxClientFloodAttack.setStatus(
        "current"
    )

wlsxValidClientNotUsingEncryption = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1171)
)
wlsxValidClientNotUsingEncryption.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxValidClientNotUsingEncryption.setStatus(
        "current"
    )

wlsxAdhocUsingValidSSID = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1172)
)
wlsxAdhocUsingValidSSID.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAdhocUsingValidSSID.setStatus(
        "current"
    )

wlsxAPSpoofingDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1173)
)
wlsxAPSpoofingDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapSpoofedFrameType"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxAPSpoofingDetected.setStatus(
        "current"
    )

wlsxClientAssociatingOnWrongChannel = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1174)
)
wlsxClientAssociatingOnWrongChannel.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapSpoofedFrameType"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxClientAssociatingOnWrongChannel.setStatus(
        "current"
    )

wlsxNDisconnectStationAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1175)
)
wlsxNDisconnectStationAttack.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNDisconnectStationAttack.setStatus(
        "current"
    )

wlsxNStaUnAssociatedFromUnsecureAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1176)
)
wlsxNStaUnAssociatedFromUnsecureAP.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNStaUnAssociatedFromUnsecureAP.setStatus(
        "current"
    )

wlsxOmertaAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1177)
)
wlsxOmertaAttack.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxOmertaAttack.setStatus(
        "current"
    )

wlsxTKIPReplayAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1178)
)
wlsxTKIPReplayAttack.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxTKIPReplayAttack.setStatus(
        "current"
    )

wlsxChopChopAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1179)
)
wlsxChopChopAttack.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxChopChopAttack.setStatus(
        "current"
    )

wlsxFataJackAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1180)
)
wlsxFataJackAttack.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxFataJackAttack.setStatus(
        "current"
    )

wlsxInvalidAddressCombination = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1181)
)
wlsxInvalidAddressCombination.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxInvalidAddressCombination.setStatus(
        "current"
    )

wlsxValidClientMisassociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1182)
)
wlsxValidClientMisassociation.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapAssociationType"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxValidClientMisassociation.setStatus(
        "current"
    )

wlsxMalformedHTIEDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1183)
)
wlsxMalformedHTIEDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxMalformedHTIEDetected.setStatus(
        "current"
    )

wlsxMalformedAssocReqDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1184)
)
wlsxMalformedAssocReqDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxMalformedAssocReqDetected.setStatus(
        "current"
    )

wlsxOverflowIEDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1185)
)
wlsxOverflowIEDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxOverflowIEDetected.setStatus(
        "current"
    )

wlsxOverflowEAPOLKeyDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1186)
)
wlsxOverflowEAPOLKeyDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxOverflowEAPOLKeyDetected.setStatus(
        "current"
    )

wlsxMalformedFrameLargeDurationDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1187)
)
wlsxMalformedFrameLargeDurationDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxMalformedFrameLargeDurationDetected.setStatus(
        "current"
    )

wlsxMalformedFrameWrongChannelDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1188)
)
wlsxMalformedFrameWrongChannelDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPChannel"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxMalformedFrameWrongChannelDetected.setStatus(
        "current"
    )

wlsxMalformedAuthFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1189)
)
wlsxMalformedAuthFrame.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxMalformedAuthFrame.setStatus(
        "current"
    )

wlsxCTSRateAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1190)
)
wlsxCTSRateAnomaly.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxCTSRateAnomaly.setStatus(
        "current"
    )

wlsxRTSRateAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1191)
)
wlsxRTSRateAnomaly.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxRTSRateAnomaly.setStatus(
        "current"
    )

wlsxNRogueAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1192)
)
wlsxNRogueAPDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNRogueAPDetected.setStatus(
        "current"
    )

wlsxNRogueAPResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1193)
)
wlsxNRogueAPResolved.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNRogueAPResolved.setStatus(
        "current"
    )

wlsxNeighborAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1194)
)
wlsxNeighborAPDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNeighborAPDetected.setStatus(
        "current"
    )

wlsxNInterferingAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1195)
)
wlsxNInterferingAPDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNInterferingAPDetected.setStatus(
        "current"
    )

wlsxNSuspectRogueAPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1196)
)
wlsxNSuspectRogueAPDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapConfidenceLevel"))
)
if mibBuilder.loadTexts:
    wlsxNSuspectRogueAPDetected.setStatus(
        "current"
    )

wlsxNSuspectRogueAPResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1197)
)
wlsxNSuspectRogueAPResolved.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSuspectRogueAPResolved.setStatus(
        "current"
    )

wlsxBlockAckAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1198)
)
wlsxBlockAckAttackDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxBlockAckAttackDetected.setStatus(
        "current"
    )

wlsxHotspotterAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1199)
)
wlsxHotspotterAttackDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"))
)
if mibBuilder.loadTexts:
    wlsxHotspotterAttackDetected.setStatus(
        "current"
    )

wlsxNSignatureMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1200)
)
wlsxNSignatureMatch.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTransmitterMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatch.setStatus(
        "current"
    )

wlsxNSignatureMatchNetstumbler = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1201)
)
wlsxNSignatureMatchNetstumbler.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTransmitterMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatchNetstumbler.setStatus(
        "current"
    )

wlsxNSignatureMatchAsleap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1202)
)
wlsxNSignatureMatchAsleap.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTransmitterMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatchAsleap.setStatus(
        "current"
    )

wlsxNSignatureMatchAirjack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1203)
)
wlsxNSignatureMatchAirjack.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTransmitterMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatchAirjack.setStatus(
        "current"
    )

wlsxNSignatureMatchNullProbeResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1204)
)
wlsxNSignatureMatchNullProbeResp.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTransmitterMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatchNullProbeResp.setStatus(
        "current"
    )

wlsxNSignatureMatchDeauthBcast = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1205)
)
wlsxNSignatureMatchDeauthBcast.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTransmitterMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatchDeauthBcast.setStatus(
        "current"
    )

wlsxNSignatureMatchDisassocBcast = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1206)
)
wlsxNSignatureMatchDisassocBcast.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTransmitterMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatchDisassocBcast.setStatus(
        "current"
    )

wlsxNSignatureMatchWellenreiter = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1207)
)
wlsxNSignatureMatchWellenreiter.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTransmitterMac"),
        ("AI-AP-MIB", "wlsxTrapReceiverMac"),
        ("AI-AP-MIB", "wlsxTrapSignatureName"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNSignatureMatchWellenreiter.setStatus(
        "current"
    )

wlsxAPDeauthContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1208)
)
wlsxAPDeauthContainment.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxAPDeauthContainment.setStatus(
        "current"
    )

wlsxClientDeauthContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1209)
)
wlsxClientDeauthContainment.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxClientDeauthContainment.setStatus(
        "current"
    )

wlsxAPWiredContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1210)
)
wlsxAPWiredContainment.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapDeviceIpAddress"),
        ("AI-AP-MIB", "wlsxTrapDeviceMac"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxAPWiredContainment.setStatus(
        "current"
    )

wlsxClientWiredContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1211)
)
wlsxClientWiredContainment.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapDeviceIpAddress"),
        ("AI-AP-MIB", "wlsxTrapDeviceMac"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxClientWiredContainment.setStatus(
        "current"
    )

wlsxAPTaggedWiredContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1212)
)
wlsxAPTaggedWiredContainment.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapDeviceIpAddress"),
        ("AI-AP-MIB", "wlsxTrapDeviceMac"),
        ("AI-AP-MIB", "wlsxTrapVlanId"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxAPTaggedWiredContainment.setStatus(
        "current"
    )

wlsxClientTaggedWiredContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1213)
)
wlsxClientTaggedWiredContainment.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapDeviceIpAddress"),
        ("AI-AP-MIB", "wlsxTrapDeviceMac"),
        ("AI-AP-MIB", "wlsxTrapVlanId"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxClientTaggedWiredContainment.setStatus(
        "current"
    )

wlsxTarpitContainment = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1214)
)
wlsxTarpitContainment.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapTargetAPChannel"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxTarpitContainment.setStatus(
        "current"
    )

wlsxAPChannelChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1216)
)
wlsxAPChannelChange.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapAPChannelSec"),
        ("AI-AP-MIB", "wlsxTrapAPPrevChannel"),
        ("AI-AP-MIB", "wlsxTrapAPPrevChannelSec"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPARMChangeReason"))
)
if mibBuilder.loadTexts:
    wlsxAPChannelChange.setStatus(
        "current"
    )

wlsxAPPowerChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1217)
)
wlsxAPPowerChange.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPTxPower"),
        ("AI-AP-MIB", "wlsxTrapAPPrevTxPower"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxAPPowerChange.setStatus(
        "current"
    )

wlsxAPModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1218)
)
wlsxAPModeChange.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPCurMode"),
        ("AI-AP-MIB", "wlsxTrapAPPrevMode"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"))
)
if mibBuilder.loadTexts:
    wlsxAPModeChange.setStatus(
        "current"
    )

wlsxUserEntryAttributesChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1219)
)
wlsxUserEntryAttributesChanged.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapUserIpAddress"),
        ("AI-AP-MIB", "wlsxTrapUserPhyAddress"),
        ("AI-AP-MIB", "wlsxTrapAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPName"),
        ("AI-AP-MIB", "wlsxTrapCardSlot"),
        ("AI-AP-MIB", "wlsxTrapPortNumber"),
        ("AI-AP-MIB", "wlsxTrapUserAttributeChangeType"))
)
if mibBuilder.loadTexts:
    wlsxUserEntryAttributesChanged.setStatus(
        "current"
    )

wlsxPowerSaveDosAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1220)
)
wlsxPowerSaveDosAttack.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxPowerSaveDosAttack.setStatus(
        "current"
    )

wlsxNAPMasterStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1221)
)
wlsxNAPMasterStatusChange.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapApControllerIp"),
        ("AI-AP-MIB", "wlsxTrapApMasterStatus"))
)
if mibBuilder.loadTexts:
    wlsxNAPMasterStatusChange.setStatus(
        "current"
    )

wlsxNAdhocUsingValidSSID = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1222)
)
wlsxNAdhocUsingValidSSID.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapTargetAPSSID"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapSnr"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"))
)
if mibBuilder.loadTexts:
    wlsxNAdhocUsingValidSSID.setStatus(
        "current"
    )

wlsxMgmtUserAuthenticationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1224)
)
wlsxMgmtUserAuthenticationFailed.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapUserName"),
        ("AI-AP-MIB", "wlsxTrapUserIpAddress"),
        ("AI-AP-MIB", "wlsxTrapUserPhyAddress"),
        ("AI-AP-MIB", "wlsxTrapAuthServerName"),
        ("AI-AP-MIB", "wlsxTrapAuthServerAddress"))
)
if mibBuilder.loadTexts:
    wlsxMgmtUserAuthenticationFailed.setStatus(
        "current"
    )

wlsxAPActiveUplinkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1252)
)
wlsxAPActiveUplinkChanged.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPPreviousUplinkType"),
        ("AI-AP-MIB", "wlsxTrapAPPreviousUplinkActiveTime"),
        ("AI-AP-MIB", "wlsxTrapAPActiveUplinkType"),
        ("AI-AP-MIB", "wlsxTrapAPUplinkChangeReason"))
)
if mibBuilder.loadTexts:
    wlsxAPActiveUplinkChanged.setStatus(
        "current"
    )

wlsxAPManagedModeConfigFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1255)
)
wlsxAPManagedModeConfigFailureTrap.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPManagedModeConfigFailure"))
)
if mibBuilder.loadTexts:
    wlsxAPManagedModeConfigFailureTrap.setStatus(
        "current"
    )

wlsxNAuthServerAcctTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1256)
)
wlsxNAuthServerAcctTimedOut.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapUserName"),
        ("AI-AP-MIB", "wlsxTrapUserIpAddress"),
        ("AI-AP-MIB", "wlsxTrapUserPhyAddress"),
        ("AI-AP-MIB", "wlsxTrapAuthServerName"),
        ("AI-AP-MIB", "wlsxTrapAuthServerAddress"),
        ("AI-AP-MIB", "wlsxTrapAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPName"))
)
if mibBuilder.loadTexts:
    wlsxNAuthServerAcctTimedOut.setStatus(
        "current"
    )

wlsxPortalServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1259)
)
wlsxPortalServerDown.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapPortalServerName"),
        ("AI-AP-MIB", "wlsxTrapPortalServerAddress"),
        ("AI-AP-MIB", "wlsxTrapAPName"),
        ("AI-AP-MIB", "wlsxTrapPortalServerDownReason"))
)
if mibBuilder.loadTexts:
    wlsxPortalServerDown.setStatus(
        "current"
    )

wlsxPortalServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1260)
)
wlsxPortalServerUp.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapPortalServerName"),
        ("AI-AP-MIB", "wlsxTrapPortalServerAddress"),
        ("AI-AP-MIB", "wlsxTrapAPName"))
)
if mibBuilder.loadTexts:
    wlsxPortalServerUp.setStatus(
        "current"
    )

wlsxIAPVoiceClientLocationUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1262)
)
wlsxIAPVoiceClientLocationUpdate.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapVcIpAddress"),
        ("AI-AP-MIB", "wlsxTrapVcMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPName"))
)
if mibBuilder.loadTexts:
    wlsxIAPVoiceClientLocationUpdate.setStatus(
        "current"
    )

wlsxWPAFTAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1267)
)
wlsxWPAFTAttack.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapNodeMac"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"))
)
if mibBuilder.loadTexts:
    wlsxWPAFTAttack.setStatus(
        "current"
    )

wlsxMitMDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1268)
)
wlsxMitMDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPLocation"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPRadioNumber"),
        ("AI-AP-MIB", "wlsxTrapSourceMac"),
        ("AI-AP-MIB", "wlsxTrapTargetAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPChannel"),
        ("AI-AP-MIB", "wlsxTrapSnr"))
)
if mibBuilder.loadTexts:
    wlsxMitMDetected.setStatus(
        "current"
    )

wlsxAPLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1271)
)
wlsxAPLoopDetected.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPName"),
        ("AI-AP-MIB", "wlsxTrapPortNumber"))
)
if mibBuilder.loadTexts:
    wlsxAPLoopDetected.setStatus(
        "current"
    )

wlsxAPBROADCASTSTORM = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1272)
)
wlsxAPBROADCASTSTORM.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPName"),
        ("AI-AP-MIB", "wlsxTrapPortNumber"))
)
if mibBuilder.loadTexts:
    wlsxAPBROADCASTSTORM.setStatus(
        "current"
    )

wlsxCLEARPASSSERVERINVALID = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1274)
)
wlsxCLEARPASSSERVERINVALID.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAuthServerName"))
)
if mibBuilder.loadTexts:
    wlsxCLEARPASSSERVERINVALID.setStatus(
        "current"
    )

wlsxAPUSBPLUGALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1277)
)
wlsxAPUSBPLUGALARM.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPName"),
        ("AI-AP-MIB", "wlsxTrapUSBVendorProductID"),
        ("AI-AP-MIB", "wlsxTrapUSBVendorProductID"),
        ("AI-AP-MIB", "wlsxTrapAPUSBStatus"))
)
if mibBuilder.loadTexts:
    wlsxAPUSBPLUGALARM.setStatus(
        "current"
    )

wlsxClientRejectedByMaxClientCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1284)
)
wlsxClientRejectedByMaxClientCount.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapUserPhyAddress"),
        ("AI-AP-MIB", "wlsxTrapAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPName"),
        ("AI-AP-MIB", "wlsxTrapEssid"))
)
if mibBuilder.loadTexts:
    wlsxClientRejectedByMaxClientCount.setStatus(
        "current"
    )

wlsxClientPskAuthenticationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 14823, 2, 3, 3, 1, 200, 2, 1285)
)
wlsxClientPskAuthenticationFailed.setObjects(
      *(("AI-AP-MIB", "wlsxTrapTime"),
        ("AI-AP-MIB", "wlsxTrapUserPhyAddress"),
        ("AI-AP-MIB", "wlsxTrapAuthFailureReason"),
        ("AI-AP-MIB", "wlsxTrapAPBSSID"),
        ("AI-AP-MIB", "wlsxTrapAPMacAddress"),
        ("AI-AP-MIB", "wlsxTrapAPName"),
        ("AI-AP-MIB", "wlsxTrapEssid"))
)
if mibBuilder.loadTexts:
    wlsxClientPskAuthenticationFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AI-AP-MIB",
    **{"ArubaEnableValue": ArubaEnableValue,
       "ArubaFrameType": ArubaFrameType,
       "ArubaPhyType": ArubaPhyType,
       "ArubaHTMode": ArubaHTMode,
       "ArubaHTExtChannel": ArubaHTExtChannel,
       "ArubaMonEncryptionType": ArubaMonEncryptionType,
       "ArubaMonEncryptionCipher": ArubaMonEncryptionCipher,
       "ArubaMonAuthAlgorithm": ArubaMonAuthAlgorithm,
       "ArubaSwitchRole": ArubaSwitchRole,
       "ArubaSupportStatus": ArubaSupportStatus,
       "ArubaActiveState": ArubaActiveState,
       "ArubaACLDomain": ArubaACLDomain,
       "ArubaACLNetworkServiceType": ArubaACLNetworkServiceType,
       "ArubaACLAction": ArubaACLAction,
       "ArubaDaysOfWeek": ArubaDaysOfWeek,
       "ArubaAuthenticationMethods": ArubaAuthenticationMethods,
       "ArubaSubAuthenticationMethods": ArubaSubAuthenticationMethods,
       "ArubaEncryptionType": ArubaEncryptionType,
       "ArubaUserForwardMode": ArubaUserForwardMode,
       "ArubaRogueApType": ArubaRogueApType,
       "ArubaAPMatchType": ArubaAPMatchType,
       "ArubaAPMatchMethod": ArubaAPMatchMethod,
       "ArubaStationType": ArubaStationType,
       "ArubaEncryptionMethods": ArubaEncryptionMethods,
       "ArubaHashAlgorithms": ArubaHashAlgorithms,
       "ArubaVlanValidRange": ArubaVlanValidRange,
       "ArubaPortMode": ArubaPortMode,
       "ArubaDot1dState": ArubaDot1dState,
       "ArubaPoeState": ArubaPoeState,
       "ArubaCardType": ArubaCardType,
       "ArubaESIServerMode": ArubaESIServerMode,
       "ArubaESIServerStatus": ArubaESIServerStatus,
       "ArubaIfType": ArubaIfType,
       "ArubaVoipProtocolType": ArubaVoipProtocolType,
       "ArubaAccessPointMode": ArubaAccessPointMode,
       "ArubaAuthServerType": ArubaAuthServerType,
       "ArubaAddressType": ArubaAddressType,
       "ArubaBlackListReason": ArubaBlackListReason,
       "ArubaDBType": ArubaDBType,
       "ArubaVrrpState": ArubaVrrpState,
       "ArubaOperStateValue": ArubaOperStateValue,
       "ArubaAntennaSetting": ArubaAntennaSetting,
       "ArubaAPStatus": ArubaAPStatus,
       "ArubaPortSpeed": ArubaPortSpeed,
       "ArubaPortDuplex": ArubaPortDuplex,
       "ArubaPortType": ArubaPortType,
       "ArubaEnet1Mode": ArubaEnet1Mode,
       "ArubaUnprovisionedStatus": ArubaUnprovisionedStatus,
       "ArubaMonitorMode": ArubaMonitorMode,
       "ArubaConfigurationState": ArubaConfigurationState,
       "ArubaConfigurationChangeType": ArubaConfigurationChangeType,
       "ArubaCallStates": ArubaCallStates,
       "ArubaVoipProtocol": ArubaVoipProtocol,
       "ArubaVoipRegState": ArubaVoipRegState,
       "ArubaVoiceCdrDirection": ArubaVoiceCdrDirection,
       "ArubaVoiceCacBit": ArubaVoiceCacBit,
       "ArubaMeshRole": ArubaMeshRole,
       "ArubaHTRate": ArubaHTRate,
       "ArubaUSBStatus": ArubaUSBStatus,
       "ArubaARMChangeReason": ArubaARMChangeReason,
       "ArubaAPMasterStatus": ArubaAPMasterStatus,
       "ArubaAPUplinkType": ArubaAPUplinkType,
       "ArubaAPUplinkChangeReason": ArubaAPUplinkChangeReason,
       "ArubaPortalServerDownReason": ArubaPortalServerDownReason,
       "aiMIB": aiMIB,
       "aiInfoGroup": aiInfoGroup,
       "aiVirtualControllerKey": aiVirtualControllerKey,
       "aiVirtualControllerName": aiVirtualControllerName,
       "aiVirtualControllerOrganization": aiVirtualControllerOrganization,
       "aiVirtualControllerVersion": aiVirtualControllerVersion,
       "aiVirtualControllerIPAddress": aiVirtualControllerIPAddress,
       "aiMasterIPAddress": aiMasterIPAddress,
       "aiWlanSSIDTable": aiWlanSSIDTable,
       "aiWlanSSIDEntry": aiWlanSSIDEntry,
       "aiSSIDIndex": aiSSIDIndex,
       "aiSSID": aiSSID,
       "aiSSIDStatus": aiSSIDStatus,
       "aiSSIDClientNum": aiSSIDClientNum,
       "aiSSIDHide": aiSSIDHide,
       "aiInterferAccessPointTable": aiInterferAccessPointTable,
       "aiInterferAccessPointEntry": aiInterferAccessPointEntry,
       "aiInterferAPIndex": aiInterferAPIndex,
       "aiInterferAPBSSID": aiInterferAPBSSID,
       "aiInterferAPESSID": aiInterferAPESSID,
       "aiInterferAPChannel": aiInterferAPChannel,
       "aiInterferAPPhyType": aiInterferAPPhyType,
       "aiInterferAPEncr": aiInterferAPEncr,
       "aiInterferAPAvgSnr": aiInterferAPAvgSnr,
       "aiInterferAPType": aiInterferAPType,
       "aiMeshTable": aiMeshTable,
       "aiMeshEntry": aiMeshEntry,
       "aiMeshIndex": aiMeshIndex,
       "aiMeshPointMac": aiMeshPointMac,
       "aiMeshPortalMac": aiMeshPortalMac,
       "aiMeshChannel": aiMeshChannel,
       "aiMeshAvgRssi": aiMeshAvgRssi,
       "aiMeshHops": aiMeshHops,
       "aiMeshAge": aiMeshAge,
       "aiMeshCost": aiMeshCost,
       "aiMeshRelation": aiMeshRelation,
       "aiStateGroup": aiStateGroup,
       "aiAccessPointTable": aiAccessPointTable,
       "aiAccessPointEntry": aiAccessPointEntry,
       "aiAPMACAddress": aiAPMACAddress,
       "aiAPName": aiAPName,
       "aiAPIPAddress": aiAPIPAddress,
       "aiAPSerialNum": aiAPSerialNum,
       "aiAPModel": aiAPModel,
       "aiAPModelName": aiAPModelName,
       "aiAPCPUUtilization": aiAPCPUUtilization,
       "aiAPMemoryFree": aiAPMemoryFree,
       "aiAPUptime": aiAPUptime,
       "aiAPTotalMemory": aiAPTotalMemory,
       "aiAPStatus": aiAPStatus,
       "aiAPHwopmode": aiAPHwopmode,
       "aiAPRole": aiAPRole,
       "aiRadioTable": aiRadioTable,
       "aiRadioEntry": aiRadioEntry,
       "aiRadioAPMACAddress": aiRadioAPMACAddress,
       "aiRadioIndex": aiRadioIndex,
       "aiRadioMACAddress": aiRadioMACAddress,
       "aiRadioChannel": aiRadioChannel,
       "aiRadioTransmitPower": aiRadioTransmitPower,
       "aiRadioNoiseFloor": aiRadioNoiseFloor,
       "aiRadioUtilization4": aiRadioUtilization4,
       "aiRadioUtilization64": aiRadioUtilization64,
       "aiRadioTxTotalFrames": aiRadioTxTotalFrames,
       "aiRadioTxMgmtFrames": aiRadioTxMgmtFrames,
       "aiRadioTxDataFrames": aiRadioTxDataFrames,
       "aiRadioTxDataBytes": aiRadioTxDataBytes,
       "aiRadioTxDrops": aiRadioTxDrops,
       "aiRadioRxTotalFrames": aiRadioRxTotalFrames,
       "aiRadioRxDataFrames": aiRadioRxDataFrames,
       "aiRadioRxDataBytes": aiRadioRxDataBytes,
       "aiRadioRxMgmtFrames": aiRadioRxMgmtFrames,
       "aiRadioRxBad": aiRadioRxBad,
       "aiRadioPhyEvents": aiRadioPhyEvents,
       "aiRadioStatus": aiRadioStatus,
       "aiRadioClientNum": aiRadioClientNum,
       "aiRadioMode": aiRadioMode,
       "aiWlanTable": aiWlanTable,
       "aiWlanEntry": aiWlanEntry,
       "aiWlanAPMACAddress": aiWlanAPMACAddress,
       "aiWlanIndex": aiWlanIndex,
       "aiWlanESSID": aiWlanESSID,
       "aiWlanMACAddress": aiWlanMACAddress,
       "aiWlanTxTotalFrames": aiWlanTxTotalFrames,
       "aiWlanTxDataFrames": aiWlanTxDataFrames,
       "aiWlanTxDataBytes": aiWlanTxDataBytes,
       "aiWlanRxTotalFrames": aiWlanRxTotalFrames,
       "aiWlanRxDataFrames": aiWlanRxDataFrames,
       "aiWlanRxDataBytes": aiWlanRxDataBytes,
       "aiClientTable": aiClientTable,
       "aiClientEntry": aiClientEntry,
       "aiClientMACAddress": aiClientMACAddress,
       "aiClientWlanMACAddress": aiClientWlanMACAddress,
       "aiClientIPAddress": aiClientIPAddress,
       "aiClientAPIPAddress": aiClientAPIPAddress,
       "aiClientName": aiClientName,
       "aiClientOperatingSystem": aiClientOperatingSystem,
       "aiClientSNR": aiClientSNR,
       "aiClientTxDataFrames": aiClientTxDataFrames,
       "aiClientTxDataBytes": aiClientTxDataBytes,
       "aiClientTxRetries": aiClientTxRetries,
       "aiClientTxRate": aiClientTxRate,
       "aiClientRxDataFrames": aiClientRxDataFrames,
       "aiClientRxDataBytes": aiClientRxDataBytes,
       "aiClientRxRetries": aiClientRxRetries,
       "aiClientRxRate": aiClientRxRate,
       "aiClientUptime": aiClientUptime,
       "aiClientPhyType": aiClientPhyType,
       "aiClientHtMode": aiClientHtMode,
       "aiVoiceClientTable": aiVoiceClientTable,
       "aiVoiceClientEntry": aiVoiceClientEntry,
       "aiClientMac": aiClientMac,
       "aiClientIP": aiClientIP,
       "aiClientAPMac": aiClientAPMac,
       "aiClientAPName": aiClientAPName,
       "aiManagedInfoGroup": aiManagedInfoGroup,
       "aiManagedModeSinceLastSync": aiManagedModeSinceLastSync,
       "aiTrapsGroup": aiTrapsGroup,
       "aiTrapObjectsGroup": aiTrapObjectsGroup,
       "wlsxTrapAPMacAddress": wlsxTrapAPMacAddress,
       "wlsxTrapAPIpAddress": wlsxTrapAPIpAddress,
       "wlsxTrapAPBSSID": wlsxTrapAPBSSID,
       "wlsxTrapEssid": wlsxTrapEssid,
       "wlsxTrapTargetAPBSSID": wlsxTrapTargetAPBSSID,
       "wlsxTrapTargetAPSSID": wlsxTrapTargetAPSSID,
       "wlsxTrapTargetAPChannel": wlsxTrapTargetAPChannel,
       "wlsxTrapNodeMac": wlsxTrapNodeMac,
       "wlsxTrapSourceMac": wlsxTrapSourceMac,
       "wlsxReceiverMac": wlsxReceiverMac,
       "wlsxTrapTransmitterMac": wlsxTrapTransmitterMac,
       "wlsxTrapReceiverMac": wlsxTrapReceiverMac,
       "wlsxTrapSnr": wlsxTrapSnr,
       "wlsxTrapSignatureName": wlsxTrapSignatureName,
       "wlsxTrapFrameType": wlsxTrapFrameType,
       "wlsxTrapAddressType": wlsxTrapAddressType,
       "wlsxTrapAPLocation": wlsxTrapAPLocation,
       "wlsxTrapAPChannel": wlsxTrapAPChannel,
       "wlsxTrapAPTxPower": wlsxTrapAPTxPower,
       "wlsxTrapMatchedMac": wlsxTrapMatchedMac,
       "wlsxTrapMatchedIp": wlsxTrapMatchedIp,
       "wlsxTrapRogueIfoURL": wlsxTrapRogueIfoURL,
       "wlsxTrapVlanId": wlsxTrapVlanId,
       "wlsxTrapAdminStatus": wlsxTrapAdminStatus,
       "wlsxTrapOperStatus": wlsxTrapOperStatus,
       "wlsxTrapAuthServerName": wlsxTrapAuthServerName,
       "wlsxTrapAuthServerTimeout": wlsxTrapAuthServerTimeout,
       "wlsxTrapCardSlot": wlsxTrapCardSlot,
       "wlsxTrapTemperatureValue": wlsxTrapTemperatureValue,
       "wlsxTrapProcessName": wlsxTrapProcessName,
       "wlsxTrapFanNumber": wlsxTrapFanNumber,
       "wlsxTrapVoltageType": wlsxTrapVoltageType,
       "wlsxTrapVoltageValue": wlsxTrapVoltageValue,
       "wlsxTrapStationBlackListReason": wlsxTrapStationBlackListReason,
       "wlsxTrapSpoofedIpAddress": wlsxTrapSpoofedIpAddress,
       "wlsxTrapSpoofedOldPhyAddress": wlsxTrapSpoofedOldPhyAddress,
       "wlsxTrapSpoofedNewPhyAddress": wlsxTrapSpoofedNewPhyAddress,
       "wlsxTrapDBName": wlsxTrapDBName,
       "wlsxTrapDBUserName": wlsxTrapDBUserName,
       "wlsxTrapDBIpAddress": wlsxTrapDBIpAddress,
       "wlsxTrapDBType": wlsxTrapDBType,
       "wlsxTrapVrrpID": wlsxTrapVrrpID,
       "wlsxTrapVrrpMasterIp": wlsxTrapVrrpMasterIp,
       "wlsxTrapVrrpOperState": wlsxTrapVrrpOperState,
       "wlsxTrapESIServerGrpName": wlsxTrapESIServerGrpName,
       "wlsxTrapESIServerName": wlsxTrapESIServerName,
       "wlsxTrapESIServerIpAddress": wlsxTrapESIServerIpAddress,
       "wlsxTrapLicenseDaysRemaining": wlsxTrapLicenseDaysRemaining,
       "wlsxTrapSwitchIp": wlsxTrapSwitchIp,
       "wlsxTrapSwitchRole": wlsxTrapSwitchRole,
       "wlsxTrapUserIpAddress": wlsxTrapUserIpAddress,
       "wlsxTrapUserPhyAddress": wlsxTrapUserPhyAddress,
       "wlsxTrapUserName": wlsxTrapUserName,
       "wlsxTrapUserRole": wlsxTrapUserRole,
       "wlsxTrapUserAuthenticationMethod": wlsxTrapUserAuthenticationMethod,
       "wlsxTrapAPRadioNumber": wlsxTrapAPRadioNumber,
       "wlsxTrapRogueInfoURL": wlsxTrapRogueInfoURL,
       "wlsxTrapInterferingAPInfoURL": wlsxTrapInterferingAPInfoURL,
       "wlsxTrapPortNumber": wlsxTrapPortNumber,
       "wlsxTrapTime": wlsxTrapTime,
       "wlsxTrapHostIp": wlsxTrapHostIp,
       "wlsxTrapHostPort": wlsxTrapHostPort,
       "wlsxTrapConfigurationId": wlsxTrapConfigurationId,
       "wlsxTrapCTSURL": wlsxTrapCTSURL,
       "wlsxTrapCTSTransferType": wlsxTrapCTSTransferType,
       "wlsxTrapConfigurationState": wlsxTrapConfigurationState,
       "wlsxTrapUpdateFailureReason": wlsxTrapUpdateFailureReason,
       "wlsxTrapUpdateFailedObj": wlsxTrapUpdateFailedObj,
       "wlsxTrapTableEntryChangeType": wlsxTrapTableEntryChangeType,
       "wlsxTrapGlobalConfigObj": wlsxTrapGlobalConfigObj,
       "wlsxTrapTableGenNumber": wlsxTrapTableGenNumber,
       "wlsxTrapLicenseId": wlsxTrapLicenseId,
       "wlsxTrapConfidenceLevel": wlsxTrapConfidenceLevel,
       "wlsxTrapMissingLicenses": wlsxTrapMissingLicenses,
       "wlsxVoiceCurrentNumCdr": wlsxVoiceCurrentNumCdr,
       "wlsxTrapTunnelId": wlsxTrapTunnelId,
       "wlsxTrapTunnelStatus": wlsxTrapTunnelStatus,
       "wlsxTrapTunnelUpReason": wlsxTrapTunnelUpReason,
       "wlsxTrapTunnelDownReason": wlsxTrapTunnelDownReason,
       "wlsxTrapApSerialNumber": wlsxTrapApSerialNumber,
       "wlsxTrapTimeStr": wlsxTrapTimeStr,
       "wlsxTrapMasterIp": wlsxTrapMasterIp,
       "wlsxTrapLocalIp": wlsxTrapLocalIp,
       "wlsxTrapMasterName": wlsxTrapMasterName,
       "wlsxTrapLocalName": wlsxTrapLocalName,
       "wlsxTrapPrimaryControllerIp": wlsxTrapPrimaryControllerIp,
       "wlsxTrapBackupControllerIp": wlsxTrapBackupControllerIp,
       "wlsxTrapSpoofedFrameType": wlsxTrapSpoofedFrameType,
       "wlsxTrapAssociationType": wlsxTrapAssociationType,
       "wlsxTrapDeviceIpAddress": wlsxTrapDeviceIpAddress,
       "wlsxTrapDeviceMac": wlsxTrapDeviceMac,
       "wlsxTrapVcIpAddress": wlsxTrapVcIpAddress,
       "wlsxTrapVcMacAddress": wlsxTrapVcMacAddress,
       "wlsxTrapAPName": wlsxTrapAPName,
       "wlsxTrapApMode": wlsxTrapApMode,
       "wlsxTrapAPPrevChannel": wlsxTrapAPPrevChannel,
       "wlsxTrapAPPrevChannelSec": wlsxTrapAPPrevChannelSec,
       "wlsxTrapAPPrevTxPower": wlsxTrapAPPrevTxPower,
       "wlsxTrapAPCurMode": wlsxTrapAPCurMode,
       "wlsxTrapAPPrevMode": wlsxTrapAPPrevMode,
       "wlsxTrapAPARMChangeReason": wlsxTrapAPARMChangeReason,
       "wlsxTrapAPChannelSec": wlsxTrapAPChannelSec,
       "wlsxTrapUserAttributeChangeType": wlsxTrapUserAttributeChangeType,
       "wlsxTrapApControllerIp": wlsxTrapApControllerIp,
       "wlsxTrapApMasterStatus": wlsxTrapApMasterStatus,
       "wlsxTrapCaName": wlsxTrapCaName,
       "wlsxTrapCrlName": wlsxTrapCrlName,
       "wlsxTrapCount": wlsxTrapCount,
       "wlsxTrapAPPreviousUplinkType": wlsxTrapAPPreviousUplinkType,
       "wlsxTrapAPPreviousUplinkActiveTime": wlsxTrapAPPreviousUplinkActiveTime,
       "wlsxTrapAPActiveUplinkType": wlsxTrapAPActiveUplinkType,
       "wlsxTrapAPUplinkChangeReason": wlsxTrapAPUplinkChangeReason,
       "wlsxTrapAPManagedModeConfigFailure": wlsxTrapAPManagedModeConfigFailure,
       "wlsxTrapAuthServerAddress": wlsxTrapAuthServerAddress,
       "wlsxTrapPortalServerName": wlsxTrapPortalServerName,
       "wlsxTrapPortalServerAddress": wlsxTrapPortalServerAddress,
       "wlsxTrapPortalServerDownReason": wlsxTrapPortalServerDownReason,
       "wlsxTrapStationBlackListReasonStr": wlsxTrapStationBlackListReasonStr,
       "wlsxTrapAPUSBStatus": wlsxTrapAPUSBStatus,
       "wlsxTrapUSBVendorProductID": wlsxTrapUSBVendorProductID,
       "wlsxTrapAuthFailureReason": wlsxTrapAuthFailureReason,
       "aiTrapDefinitionsGroup": aiTrapDefinitionsGroup,
       "wlsxNodeRateAnomaly": wlsxNodeRateAnomaly,
       "wlsxNUserEntryCreated": wlsxNUserEntryCreated,
       "wlsxNUserEntryDeleted": wlsxNUserEntryDeleted,
       "wlsxNUserEntryAuthenticated": wlsxNUserEntryAuthenticated,
       "wlsxNUserEntryDeAuthenticated": wlsxNUserEntryDeAuthenticated,
       "wlsxNUserAuthenticationFailed": wlsxNUserAuthenticationFailed,
       "wlsxNAuthServerReqTimedOut": wlsxNAuthServerReqTimedOut,
       "wlsxNAuthServerTimedOut": wlsxNAuthServerTimedOut,
       "wlsxNAuthServerIsUp": wlsxNAuthServerIsUp,
       "wlsxNAccessPointIsUp": wlsxNAccessPointIsUp,
       "wlsxNAccessPointIsDown": wlsxNAccessPointIsDown,
       "wlsxNChannelChanged": wlsxNChannelChanged,
       "wlsxNStationAddedToBlackList": wlsxNStationAddedToBlackList,
       "wlsxNStationRemovedFromBlackList": wlsxNStationRemovedFromBlackList,
       "wlsxNRadioAttributesChanged": wlsxNRadioAttributesChanged,
       "wlsxUnsecureAPDetected": wlsxUnsecureAPDetected,
       "wlsxUnsecureAPResolved": wlsxUnsecureAPResolved,
       "wlsxStaImpersonation": wlsxStaImpersonation,
       "wlsxReservedChannelViolation": wlsxReservedChannelViolation,
       "wlsxValidSSIDViolation": wlsxValidSSIDViolation,
       "wlsxChannelMisconfiguration": wlsxChannelMisconfiguration,
       "wlsxOUIMisconfiguration": wlsxOUIMisconfiguration,
       "wlsxSSIDMisconfiguration": wlsxSSIDMisconfiguration,
       "wlsxShortPreableMisconfiguration": wlsxShortPreableMisconfiguration,
       "wlsxWPAMisconfiguration": wlsxWPAMisconfiguration,
       "wlsxAdhocNetworkDetected": wlsxAdhocNetworkDetected,
       "wlsxAdhocNetworkRemoved": wlsxAdhocNetworkRemoved,
       "wlsxStaPolicyViolation": wlsxStaPolicyViolation,
       "wlsxRepeatWEPIVViolation": wlsxRepeatWEPIVViolation,
       "wlsxWeakWEPIVViolation": wlsxWeakWEPIVViolation,
       "wlsxChannelInterferenceDetected": wlsxChannelInterferenceDetected,
       "wlsxChannelInterferenceCleared": wlsxChannelInterferenceCleared,
       "wlsxAPInterferenceDetected": wlsxAPInterferenceDetected,
       "wlsxAPInterferenceCleared": wlsxAPInterferenceCleared,
       "wlsxStaInterferenceDetected": wlsxStaInterferenceDetected,
       "wlsxStaInterferenceCleared": wlsxStaInterferenceCleared,
       "wlsxFrameRetryRateExceeded": wlsxFrameRetryRateExceeded,
       "wlsxFrameReceiveErrorRateExceeded": wlsxFrameReceiveErrorRateExceeded,
       "wlsxFrameFragmentationRateExceeded": wlsxFrameFragmentationRateExceeded,
       "wlsxFrameBandWidthRateExceeded": wlsxFrameBandWidthRateExceeded,
       "wlsxFrameLowSpeedRateExceeded": wlsxFrameLowSpeedRateExceeded,
       "wlsxFrameNonUnicastRateExceeded": wlsxFrameNonUnicastRateExceeded,
       "wlsxLoadbalancingEnabled": wlsxLoadbalancingEnabled,
       "wlsxLoadbalancingDisabled": wlsxLoadbalancingDisabled,
       "wlsxChannelFrameRetryRateExceeded": wlsxChannelFrameRetryRateExceeded,
       "wlsxChannelFrameFragmentationRateExceeded": wlsxChannelFrameFragmentationRateExceeded,
       "wlsxChannelFrameErrorRateExceeded": wlsxChannelFrameErrorRateExceeded,
       "wlsxSignatureMatchAP": wlsxSignatureMatchAP,
       "wlsxSignatureMatchSta": wlsxSignatureMatchSta,
       "wlsxChannelRateAnomaly": wlsxChannelRateAnomaly,
       "wlsxNodeRateAnomalyAP": wlsxNodeRateAnomalyAP,
       "wlsxNodeRateAnomalySta": wlsxNodeRateAnomalySta,
       "wlsxEAPRateAnomaly": wlsxEAPRateAnomaly,
       "wlsxSignalAnomaly": wlsxSignalAnomaly,
       "wlsxSequenceNumberAnomalyAP": wlsxSequenceNumberAnomalyAP,
       "wlsxSequenceNumberAnomalySta": wlsxSequenceNumberAnomalySta,
       "wlsxDisconnectStationAttack": wlsxDisconnectStationAttack,
       "wlsxApFloodAttack": wlsxApFloodAttack,
       "wlsxAdhocNetwork": wlsxAdhocNetwork,
       "wlsxWirelessBridge": wlsxWirelessBridge,
       "wlsxInvalidMacOUIAP": wlsxInvalidMacOUIAP,
       "wlsxInvalidMacOUISta": wlsxInvalidMacOUISta,
       "wlsxWEPMisconfiguration": wlsxWEPMisconfiguration,
       "wlsxStaRepeatWEPIVViolation": wlsxStaRepeatWEPIVViolation,
       "wlsxStaWeakWEPIVViolation": wlsxStaWeakWEPIVViolation,
       "wlsxStaAssociatedToUnsecureAP": wlsxStaAssociatedToUnsecureAP,
       "wlsxStaUnAssociatedFromUnsecureAP": wlsxStaUnAssociatedFromUnsecureAP,
       "wlsxAdhocNetworkBridgeDetected": wlsxAdhocNetworkBridgeDetected,
       "wlsxInterferingApDetected": wlsxInterferingApDetected,
       "wlsxColdStart": wlsxColdStart,
       "wlsxWarmStart": wlsxWarmStart,
       "wlsxAPImpersonation": wlsxAPImpersonation,
       "wlsxNAuthServerIsDown": wlsxNAuthServerIsDown,
       "wlsxWindowsBridgeDetected": wlsxWindowsBridgeDetected,
       "wlsxSignAPNetstumbler": wlsxSignAPNetstumbler,
       "wlsxSignStaNetstumbler": wlsxSignStaNetstumbler,
       "wlsxSignAPAsleap": wlsxSignAPAsleap,
       "wlsxSignStaAsleap": wlsxSignStaAsleap,
       "wlsxSignAPAirjack": wlsxSignAPAirjack,
       "wlsxSignStaAirjack": wlsxSignStaAirjack,
       "wlsxSignAPNullProbeResp": wlsxSignAPNullProbeResp,
       "wlsxSignStaNullProbeResp": wlsxSignStaNullProbeResp,
       "wlsxSignAPDeauthBcast": wlsxSignAPDeauthBcast,
       "wlsxSignStaDeauthBcast": wlsxSignStaDeauthBcast,
       "wlsxWindowsBridgeDetectedAP": wlsxWindowsBridgeDetectedAP,
       "wlsxWindowsBridgeDetectedSta": wlsxWindowsBridgeDetectedSta,
       "wlsxAdhocNetworkBridgeDetectedAP": wlsxAdhocNetworkBridgeDetectedAP,
       "wlsxAdhocNetworkBridgeDetectedSta": wlsxAdhocNetworkBridgeDetectedSta,
       "wlsxDisconnectStationAttackAP": wlsxDisconnectStationAttackAP,
       "wlsxDisconnectStationAttackSta": wlsxDisconnectStationAttackSta,
       "wlsxSuspectUnsecureAPDetected": wlsxSuspectUnsecureAPDetected,
       "wlsxSuspectUnsecureAPResolved": wlsxSuspectUnsecureAPResolved,
       "wlsxHtGreenfieldSupported": wlsxHtGreenfieldSupported,
       "wlsxHT40MHzIntoleranceAP": wlsxHT40MHzIntoleranceAP,
       "wlsxHT40MHzIntoleranceSta": wlsxHT40MHzIntoleranceSta,
       "wlsxNAuthServerAllInService": wlsxNAuthServerAllInService,
       "wlsxNAdhocNetwork": wlsxNAdhocNetwork,
       "wlsxNAdhocNetworkBridgeDetectedAP": wlsxNAdhocNetworkBridgeDetectedAP,
       "wlsxNAdhocNetworkBridgeDetectedSta": wlsxNAdhocNetworkBridgeDetectedSta,
       "wlsxClientFloodAttack": wlsxClientFloodAttack,
       "wlsxValidClientNotUsingEncryption": wlsxValidClientNotUsingEncryption,
       "wlsxAdhocUsingValidSSID": wlsxAdhocUsingValidSSID,
       "wlsxAPSpoofingDetected": wlsxAPSpoofingDetected,
       "wlsxClientAssociatingOnWrongChannel": wlsxClientAssociatingOnWrongChannel,
       "wlsxNDisconnectStationAttack": wlsxNDisconnectStationAttack,
       "wlsxNStaUnAssociatedFromUnsecureAP": wlsxNStaUnAssociatedFromUnsecureAP,
       "wlsxOmertaAttack": wlsxOmertaAttack,
       "wlsxTKIPReplayAttack": wlsxTKIPReplayAttack,
       "wlsxChopChopAttack": wlsxChopChopAttack,
       "wlsxFataJackAttack": wlsxFataJackAttack,
       "wlsxInvalidAddressCombination": wlsxInvalidAddressCombination,
       "wlsxValidClientMisassociation": wlsxValidClientMisassociation,
       "wlsxMalformedHTIEDetected": wlsxMalformedHTIEDetected,
       "wlsxMalformedAssocReqDetected": wlsxMalformedAssocReqDetected,
       "wlsxOverflowIEDetected": wlsxOverflowIEDetected,
       "wlsxOverflowEAPOLKeyDetected": wlsxOverflowEAPOLKeyDetected,
       "wlsxMalformedFrameLargeDurationDetected": wlsxMalformedFrameLargeDurationDetected,
       "wlsxMalformedFrameWrongChannelDetected": wlsxMalformedFrameWrongChannelDetected,
       "wlsxMalformedAuthFrame": wlsxMalformedAuthFrame,
       "wlsxCTSRateAnomaly": wlsxCTSRateAnomaly,
       "wlsxRTSRateAnomaly": wlsxRTSRateAnomaly,
       "wlsxNRogueAPDetected": wlsxNRogueAPDetected,
       "wlsxNRogueAPResolved": wlsxNRogueAPResolved,
       "wlsxNeighborAPDetected": wlsxNeighborAPDetected,
       "wlsxNInterferingAPDetected": wlsxNInterferingAPDetected,
       "wlsxNSuspectRogueAPDetected": wlsxNSuspectRogueAPDetected,
       "wlsxNSuspectRogueAPResolved": wlsxNSuspectRogueAPResolved,
       "wlsxBlockAckAttackDetected": wlsxBlockAckAttackDetected,
       "wlsxHotspotterAttackDetected": wlsxHotspotterAttackDetected,
       "wlsxNSignatureMatch": wlsxNSignatureMatch,
       "wlsxNSignatureMatchNetstumbler": wlsxNSignatureMatchNetstumbler,
       "wlsxNSignatureMatchAsleap": wlsxNSignatureMatchAsleap,
       "wlsxNSignatureMatchAirjack": wlsxNSignatureMatchAirjack,
       "wlsxNSignatureMatchNullProbeResp": wlsxNSignatureMatchNullProbeResp,
       "wlsxNSignatureMatchDeauthBcast": wlsxNSignatureMatchDeauthBcast,
       "wlsxNSignatureMatchDisassocBcast": wlsxNSignatureMatchDisassocBcast,
       "wlsxNSignatureMatchWellenreiter": wlsxNSignatureMatchWellenreiter,
       "wlsxAPDeauthContainment": wlsxAPDeauthContainment,
       "wlsxClientDeauthContainment": wlsxClientDeauthContainment,
       "wlsxAPWiredContainment": wlsxAPWiredContainment,
       "wlsxClientWiredContainment": wlsxClientWiredContainment,
       "wlsxAPTaggedWiredContainment": wlsxAPTaggedWiredContainment,
       "wlsxClientTaggedWiredContainment": wlsxClientTaggedWiredContainment,
       "wlsxTarpitContainment": wlsxTarpitContainment,
       "wlsxAPChannelChange": wlsxAPChannelChange,
       "wlsxAPPowerChange": wlsxAPPowerChange,
       "wlsxAPModeChange": wlsxAPModeChange,
       "wlsxUserEntryAttributesChanged": wlsxUserEntryAttributesChanged,
       "wlsxPowerSaveDosAttack": wlsxPowerSaveDosAttack,
       "wlsxNAPMasterStatusChange": wlsxNAPMasterStatusChange,
       "wlsxNAdhocUsingValidSSID": wlsxNAdhocUsingValidSSID,
       "wlsxMgmtUserAuthenticationFailed": wlsxMgmtUserAuthenticationFailed,
       "wlsxAPActiveUplinkChanged": wlsxAPActiveUplinkChanged,
       "wlsxAPManagedModeConfigFailureTrap": wlsxAPManagedModeConfigFailureTrap,
       "wlsxNAuthServerAcctTimedOut": wlsxNAuthServerAcctTimedOut,
       "wlsxPortalServerDown": wlsxPortalServerDown,
       "wlsxPortalServerUp": wlsxPortalServerUp,
       "wlsxIAPVoiceClientLocationUpdate": wlsxIAPVoiceClientLocationUpdate,
       "wlsxWPAFTAttack": wlsxWPAFTAttack,
       "wlsxMitMDetected": wlsxMitMDetected,
       "wlsxAPLoopDetected": wlsxAPLoopDetected,
       "wlsxAPBROADCASTSTORM": wlsxAPBROADCASTSTORM,
       "wlsxCLEARPASSSERVERINVALID": wlsxCLEARPASSSERVERINVALID,
       "wlsxAPUSBPLUGALARM": wlsxAPUSBPLUGALARM,
       "wlsxClientRejectedByMaxClientCount": wlsxClientRejectedByMaxClientCount,
       "wlsxClientPskAuthenticationFailed": wlsxClientPskAuthenticationFailed}
)
