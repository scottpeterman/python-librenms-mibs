# SNMP MIB module (IPSEC-ISAKMP-IKE-DOI-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\watchguard\IPSEC-ISAKMP-IKE-DOI-TC
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:48 2025
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
 experimental,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "experimental",
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(watchguard,) = mibBuilder.importSymbols(
    "WATCHGUARD-MIB",
    "watchguard")


# MODULE-IDENTITY

ipsecIsakmpIkeDoiTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 100)
)
if mibBuilder.loadTexts:
    ipsecIsakmpIkeDoiTC.setRevisions(
        ("1999-02-18 17:05",
         "1999-03-05 15:45",
         "1999-07-13 21:45",
         "1999-10-05 17:05",
         "1999-10-15 19:50")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IpsecDoiSituation(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class IpsecDoiSecProtocolId(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
        *(("reserved", 0),
          ("protoIsakmp", 1),
          ("protoIpsecAh", 2),
          ("protoIpsecEsp", 3),
          ("protoIpcomp", 4))
    )



class IpsecDoiTransformIdent(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("keyIke", 1))
    )



class IpsecDoiAhTransform(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
        *(("reserved", 0),
          ("reserved1", 1),
          ("ahMd5", 2),
          ("ahSha", 3),
          ("ahDes", 4))
    )



class IpsecDoiEspTransform(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("espDesIv64", 1),
          ("espDes", 2),
          ("esp3Des", 3),
          ("espRc5", 4),
          ("espIdea", 5),
          ("espCast", 6),
          ("espBlowfish", 7),
          ("esp3Idea", 8),
          ("espDesIv32", 9),
          ("espRc4", 10),
          ("espNull", 11))
    )



class IpsecDoiAuthAlgorithm(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
        *(("reserved", 0),
          ("hmacMd5", 1),
          ("hmacSha", 2),
          ("desMac", 3),
          ("kpdk", 4))
    )



class IpsecDoiIpcompTransform(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
        *(("reserved", 0),
          ("ipcompOui", 1),
          ("ipcompDeflate", 2),
          ("ipcompLzs", 3))
    )



class IpsecDoiEncapsulationMode(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("tunnel", 1),
          ("transport", 2))
    )



class IpsecDoiIdentType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("idIpv4Addr", 1),
          ("idFqdn", 2),
          ("idUserFqdn", 3),
          ("idIpv4AddrSubnet", 4),
          ("idIpv6Addr", 5),
          ("idIpv6AddrSubnet", 6),
          ("idIpv4AddrRange", 7),
          ("idIpv6AddrRange", 8),
          ("idDerAsn1Dn", 9),
          ("idDerAsn1Gn", 10),
          ("idKeyId", 11))
    )



class IsakmpDOI(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("isakmp", 0),
          ("ipsecDOI", 1))
    )



class IsakmpCertificateEncoding(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("pkcs7", 1),
          ("pgp", 2),
          ("dnsSignedKey", 3),
          ("x509Signature", 4),
          ("x509KeyExchange", 5),
          ("kerberosTokens", 6),
          ("crl", 7),
          ("arl", 8),
          ("spki", 9),
          ("x509Attribute", 10))
    )



class IsakmpExchangeType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
        *(("reserved", 0),
          ("base", 1),
          ("identityProtect", 2),
          ("authOnly", 3),
          ("aggressive", 4),
          ("informational", 5))
    )



class IsakmpNotifyMessageType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
              30)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("invalidPayloadType", 1),
          ("doiNotSupported", 2),
          ("situationNotSupported", 3),
          ("invalidCookie", 4),
          ("invalidMajorVersion", 5),
          ("invalidMinorVersion", 6),
          ("invalidExchangeType", 7),
          ("invalidFlags", 8),
          ("invalidMessageId", 9),
          ("invalidProtocolId", 10),
          ("invalidSpi", 11),
          ("invalidTransformId", 12),
          ("attributesNotSupported", 13),
          ("noProposalChosen", 14),
          ("badProposalSyntax", 15),
          ("payloadMalformed", 16),
          ("invalidKeyInformation", 17),
          ("invalidIdInformation", 18),
          ("invalidCertEncoding", 19),
          ("invalidCertificate", 20),
          ("certTypeUnsupported", 21),
          ("invalidCertAuthority", 22),
          ("invalidHashInformation", 23),
          ("authenticationFailed", 24),
          ("invalidSignature", 25),
          ("addressNotification", 26),
          ("notifySaLifetime", 27),
          ("certificateUnavailable", 28),
          ("unsupportedExchangeType", 29),
          ("unequalPayloadLengths", 30))
    )



class IkeExchangeType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("base", 1),
          ("mainMode", 2),
          ("authOnly", 3),
          ("aggressive", 4),
          ("informational", 5),
          ("quickMode", 32),
          ("newGroupMode", 33),
          ("acknowledgedInfo", 34))
    )



class IkeEncryptionAlgorithm(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
        *(("reserved", 0),
          ("desCbc", 1),
          ("ideaCbc", 2),
          ("blowfishCbc", 3),
          ("rc5R16B64Cbc", 4),
          ("tripleDesCbc", 5),
          ("castCbc", 6))
    )



class IkeHashAlgorithm(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
        *(("reserved", 0),
          ("md5", 1),
          ("sha", 2),
          ("tiger", 3))
    )



class IkeAuthMethod(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
        *(("reserved", 0),
          ("preSharedKey", 1),
          ("dssSignatures", 2),
          ("rsaSignatures", 3),
          ("encryptionWithRsa", 4),
          ("revisedEncryptionWithRsa", 5),
          ("encryptionWithElGamal", 6),
          ("revisedEncryptionWithElGamal", 7))
    )



class IkeGroupDescription(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
        *(("reserved", 0),
          ("modp768", 1),
          ("modp1024", 2),
          ("ec2nGalois2P155", 3),
          ("ec2nGalois2P185", 4),
          ("modp1536", 5))
    )



class IkeGroupType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
        *(("reserved", 0),
          ("modp", 1),
          ("ecp", 2),
          ("ec2n", 3))
    )



class IkePrf(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IkeNotifyMessageType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
              24576,
              24577,
              24578)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("invalidPayloadType", 1),
          ("doiNotSupported", 2),
          ("situationNotSupported", 3),
          ("invalidCookie", 4),
          ("invalidMajorVersion", 5),
          ("invalidMinorVersion", 6),
          ("invalidExchangeType", 7),
          ("invalidFlags", 8),
          ("invalidMessageId", 9),
          ("invalidProtocolId", 10),
          ("invalidSpi", 11),
          ("invalidTransformId", 12),
          ("attributesNotSupported", 13),
          ("noProposalChosen", 14),
          ("badProposalSyntax", 15),
          ("payloadMalformed", 16),
          ("invalidKeyInformation", 17),
          ("invalidIdInformation", 18),
          ("invalidCertEncoding", 19),
          ("invalidCertificate", 20),
          ("certTypeUnsupported", 21),
          ("invalidCertAuthority", 22),
          ("invalidHashInformation", 23),
          ("authenticationFailed", 24),
          ("invalidSignature", 25),
          ("addressNotification", 26),
          ("notifySaLifetime", 27),
          ("certificateUnavailable", 28),
          ("unsupportedExchangeType", 29),
          ("unequalPayloadLengths", 30),
          ("responderLifetime", 24576),
          ("replayStatus", 24577),
          ("initialContact", 24578))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPSEC-ISAKMP-IKE-DOI-TC",
    **{"IpsecDoiSituation": IpsecDoiSituation,
       "IpsecDoiSecProtocolId": IpsecDoiSecProtocolId,
       "IpsecDoiTransformIdent": IpsecDoiTransformIdent,
       "IpsecDoiAhTransform": IpsecDoiAhTransform,
       "IpsecDoiEspTransform": IpsecDoiEspTransform,
       "IpsecDoiAuthAlgorithm": IpsecDoiAuthAlgorithm,
       "IpsecDoiIpcompTransform": IpsecDoiIpcompTransform,
       "IpsecDoiEncapsulationMode": IpsecDoiEncapsulationMode,
       "IpsecDoiIdentType": IpsecDoiIdentType,
       "IsakmpDOI": IsakmpDOI,
       "IsakmpCertificateEncoding": IsakmpCertificateEncoding,
       "IsakmpExchangeType": IsakmpExchangeType,
       "IsakmpNotifyMessageType": IsakmpNotifyMessageType,
       "IkeExchangeType": IkeExchangeType,
       "IkeEncryptionAlgorithm": IkeEncryptionAlgorithm,
       "IkeHashAlgorithm": IkeHashAlgorithm,
       "IkeAuthMethod": IkeAuthMethod,
       "IkeGroupDescription": IkeGroupDescription,
       "IkeGroupType": IkeGroupType,
       "IkePrf": IkePrf,
       "IkeNotifyMessageType": IkeNotifyMessageType,
       "ipsecIsakmpIkeDoiTC": ipsecIsakmpIkeDoiTC}
)
