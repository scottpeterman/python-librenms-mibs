# SNMP MIB module (ALCATEL-IND1-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-IPSEC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:34 2025
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

(softentIND1IPsec,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1IPsec")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1IPsecMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1IPsecMIB.setRevisions(
        ("2007-07-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IPsecName(TextualConvention, OctetString):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



class IPsecDescription(TextualConvention, OctetString):
    status = "current"
    displayHint = "200a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )



class IPsecPortNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IPsecPrefixLength(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )



class IPsecULProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class IPsecAdminState(TextualConvention, Integer32):
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



class IPsecSAType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ah", 2),
          ("esp", 3))
    )



class IPsecESPAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("descbc", 2),
          ("des3cbc", 3),
          ("null", 11),
          ("aescbc", 12),
          ("aesctr", 13))
    )



class IPsecAHAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("hmacmd5", 2),
          ("hmacsha1", 3),
          ("aesxcbcmac", 9))
    )



class IPsecOperationalState(TextualConvention, Integer32):
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
        *(("enabled", 1),
          ("disabled", 2),
          ("dnspending", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1IPsecMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1IPsecMIBObjects = _AlcatelIND1IPsecMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1)
)
_AlaIPsecConfig_ObjectIdentity = ObjectIdentity
alaIPsecConfig = _AlaIPsecConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1)
)
_AlaIPsecSecurityKeyTable_Object = MibTable
alaIPsecSecurityKeyTable = _AlaIPsecSecurityKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaIPsecSecurityKeyTable.setStatus("current")
_AlaIPsecSecurityKeyEntry_Object = MibTableRow
alaIPsecSecurityKeyEntry = _AlaIPsecSecurityKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 1, 1)
)
alaIPsecSecurityKeyEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityKeyID"),
)
if mibBuilder.loadTexts:
    alaIPsecSecurityKeyEntry.setStatus("current")
_AlaIPsecSecurityKeyID_Type = Unsigned32
_AlaIPsecSecurityKeyID_Object = MibTableColumn
alaIPsecSecurityKeyID = _AlaIPsecSecurityKeyID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 1, 1, 1),
    _AlaIPsecSecurityKeyID_Type()
)
alaIPsecSecurityKeyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPsecSecurityKeyID.setStatus("current")


class _AlaIPsecSecurityKeyCurrent_Type(OctetString):
    """Custom type alaIPsecSecurityKeyCurrent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_AlaIPsecSecurityKeyCurrent_Type.__name__ = "OctetString"
_AlaIPsecSecurityKeyCurrent_Object = MibTableColumn
alaIPsecSecurityKeyCurrent = _AlaIPsecSecurityKeyCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 1, 1, 2),
    _AlaIPsecSecurityKeyCurrent_Type()
)
alaIPsecSecurityKeyCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIPsecSecurityKeyCurrent.setStatus("current")


class _AlaIPsecSecurityKeyNew_Type(OctetString):
    """Custom type alaIPsecSecurityKeyNew based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_AlaIPsecSecurityKeyNew_Type.__name__ = "OctetString"
_AlaIPsecSecurityKeyNew_Object = MibTableColumn
alaIPsecSecurityKeyNew = _AlaIPsecSecurityKeyNew_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 1, 1, 3),
    _AlaIPsecSecurityKeyNew_Type()
)
alaIPsecSecurityKeyNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIPsecSecurityKeyNew.setStatus("current")
_AlaIPsecStatisticsTable_Object = MibTable
alaIPsecStatisticsTable = _AlaIPsecStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaIPsecStatisticsTable.setStatus("current")
_AlaIPsecStatisticsEntry_Object = MibTableRow
alaIPsecStatisticsEntry = _AlaIPsecStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1)
)
alaIPsecStatisticsEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsProtocol"),
)
if mibBuilder.loadTexts:
    alaIPsecStatisticsEntry.setStatus("current")


class _AlaIPsecStatisticsProtocol_Type(Integer32):
    """Custom type alaIPsecStatisticsProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            6
        )
    )
    namedValues = NamedValues(
        ("ipv6", 6)
    )


_AlaIPsecStatisticsProtocol_Type.__name__ = "Integer32"
_AlaIPsecStatisticsProtocol_Object = MibTableColumn
alaIPsecStatisticsProtocol = _AlaIPsecStatisticsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 1),
    _AlaIPsecStatisticsProtocol_Type()
)
alaIPsecStatisticsProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPsecStatisticsProtocol.setStatus("current")
_AlaIPsecStatisticsInSuccessful_Type = Counter32
_AlaIPsecStatisticsInSuccessful_Object = MibTableColumn
alaIPsecStatisticsInSuccessful = _AlaIPsecStatisticsInSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 2),
    _AlaIPsecStatisticsInSuccessful_Type()
)
alaIPsecStatisticsInSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsInSuccessful.setStatus("current")
_AlaIPsecStatisticsInPolicyViolation_Type = Counter32
_AlaIPsecStatisticsInPolicyViolation_Object = MibTableColumn
alaIPsecStatisticsInPolicyViolation = _AlaIPsecStatisticsInPolicyViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 3),
    _AlaIPsecStatisticsInPolicyViolation_Type()
)
alaIPsecStatisticsInPolicyViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsInPolicyViolation.setStatus("current")
_AlaIPsecStatisticsInNoSA_Type = Counter32
_AlaIPsecStatisticsInNoSA_Object = MibTableColumn
alaIPsecStatisticsInNoSA = _AlaIPsecStatisticsInNoSA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 4),
    _AlaIPsecStatisticsInNoSA_Type()
)
alaIPsecStatisticsInNoSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsInNoSA.setStatus("current")
_AlaIPsecStatisticsInUnknownSPI_Type = Counter32
_AlaIPsecStatisticsInUnknownSPI_Object = MibTableColumn
alaIPsecStatisticsInUnknownSPI = _AlaIPsecStatisticsInUnknownSPI_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 5),
    _AlaIPsecStatisticsInUnknownSPI_Type()
)
alaIPsecStatisticsInUnknownSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsInUnknownSPI.setStatus("current")
_AlaIPsecStatisticsInAHReplay_Type = Counter32
_AlaIPsecStatisticsInAHReplay_Object = MibTableColumn
alaIPsecStatisticsInAHReplay = _AlaIPsecStatisticsInAHReplay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 6),
    _AlaIPsecStatisticsInAHReplay_Type()
)
alaIPsecStatisticsInAHReplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsInAHReplay.setStatus("current")
_AlaIPsecStatisticsInESPReplay_Type = Counter32
_AlaIPsecStatisticsInESPReplay_Object = MibTableColumn
alaIPsecStatisticsInESPReplay = _AlaIPsecStatisticsInESPReplay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 7),
    _AlaIPsecStatisticsInESPReplay_Type()
)
alaIPsecStatisticsInESPReplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsInESPReplay.setStatus("current")
_AlaIPsecStatisticsInAHAuthenticationSuccess_Type = Counter32
_AlaIPsecStatisticsInAHAuthenticationSuccess_Object = MibTableColumn
alaIPsecStatisticsInAHAuthenticationSuccess = _AlaIPsecStatisticsInAHAuthenticationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 8),
    _AlaIPsecStatisticsInAHAuthenticationSuccess_Type()
)
alaIPsecStatisticsInAHAuthenticationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsInAHAuthenticationSuccess.setStatus("current")
_AlaIPsecStatisticsInAHAuthenticationFail_Type = Counter32
_AlaIPsecStatisticsInAHAuthenticationFail_Object = MibTableColumn
alaIPsecStatisticsInAHAuthenticationFail = _AlaIPsecStatisticsInAHAuthenticationFail_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 9),
    _AlaIPsecStatisticsInAHAuthenticationFail_Type()
)
alaIPsecStatisticsInAHAuthenticationFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsInAHAuthenticationFail.setStatus("current")
_AlaIPsecStatisticsInESPAuthenticationSuccess_Type = Counter32
_AlaIPsecStatisticsInESPAuthenticationSuccess_Object = MibTableColumn
alaIPsecStatisticsInESPAuthenticationSuccess = _AlaIPsecStatisticsInESPAuthenticationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 10),
    _AlaIPsecStatisticsInESPAuthenticationSuccess_Type()
)
alaIPsecStatisticsInESPAuthenticationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsInESPAuthenticationSuccess.setStatus("current")
_AlaIPsecStatisticsInESPAuthenticationFail_Type = Counter32
_AlaIPsecStatisticsInESPAuthenticationFail_Object = MibTableColumn
alaIPsecStatisticsInESPAuthenticationFail = _AlaIPsecStatisticsInESPAuthenticationFail_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 11),
    _AlaIPsecStatisticsInESPAuthenticationFail_Type()
)
alaIPsecStatisticsInESPAuthenticationFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsInESPAuthenticationFail.setStatus("current")
_AlaIPsecStatisticsInBadPacket_Type = Counter32
_AlaIPsecStatisticsInBadPacket_Object = MibTableColumn
alaIPsecStatisticsInBadPacket = _AlaIPsecStatisticsInBadPacket_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 12),
    _AlaIPsecStatisticsInBadPacket_Type()
)
alaIPsecStatisticsInBadPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsInBadPacket.setStatus("current")
_AlaIPsecStatisticsInNoMemory_Type = Counter32
_AlaIPsecStatisticsInNoMemory_Object = MibTableColumn
alaIPsecStatisticsInNoMemory = _AlaIPsecStatisticsInNoMemory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 13),
    _AlaIPsecStatisticsInNoMemory_Type()
)
alaIPsecStatisticsInNoMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsInNoMemory.setStatus("current")
_AlaIPsecStatisticsOutSuccessful_Type = Counter32
_AlaIPsecStatisticsOutSuccessful_Object = MibTableColumn
alaIPsecStatisticsOutSuccessful = _AlaIPsecStatisticsOutSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 14),
    _AlaIPsecStatisticsOutSuccessful_Type()
)
alaIPsecStatisticsOutSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsOutSuccessful.setStatus("current")
_AlaIPsecStatisticsOutPolicyViolation_Type = Counter32
_AlaIPsecStatisticsOutPolicyViolation_Object = MibTableColumn
alaIPsecStatisticsOutPolicyViolation = _AlaIPsecStatisticsOutPolicyViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 15),
    _AlaIPsecStatisticsOutPolicyViolation_Type()
)
alaIPsecStatisticsOutPolicyViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsOutPolicyViolation.setStatus("current")
_AlaIPsecStatisticsOutNoSA_Type = Counter32
_AlaIPsecStatisticsOutNoSA_Object = MibTableColumn
alaIPsecStatisticsOutNoSA = _AlaIPsecStatisticsOutNoSA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 16),
    _AlaIPsecStatisticsOutNoSA_Type()
)
alaIPsecStatisticsOutNoSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsOutNoSA.setStatus("current")
_AlaIPsecStatisticsOutBadPacket_Type = Counter32
_AlaIPsecStatisticsOutBadPacket_Object = MibTableColumn
alaIPsecStatisticsOutBadPacket = _AlaIPsecStatisticsOutBadPacket_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 17),
    _AlaIPsecStatisticsOutBadPacket_Type()
)
alaIPsecStatisticsOutBadPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsOutBadPacket.setStatus("current")
_AlaIPsecStatisticsOutNoMemory_Type = Counter32
_AlaIPsecStatisticsOutNoMemory_Object = MibTableColumn
alaIPsecStatisticsOutNoMemory = _AlaIPsecStatisticsOutNoMemory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 18),
    _AlaIPsecStatisticsOutNoMemory_Type()
)
alaIPsecStatisticsOutNoMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsOutNoMemory.setStatus("current")
_AlaIPsecStatisticsInDiscarded_Type = Counter32
_AlaIPsecStatisticsInDiscarded_Object = MibTableColumn
alaIPsecStatisticsInDiscarded = _AlaIPsecStatisticsInDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 19),
    _AlaIPsecStatisticsInDiscarded_Type()
)
alaIPsecStatisticsInDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsInDiscarded.setStatus("current")
_AlaIPsecStatisticsOutDiscarded_Type = Counter32
_AlaIPsecStatisticsOutDiscarded_Object = MibTableColumn
alaIPsecStatisticsOutDiscarded = _AlaIPsecStatisticsOutDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 1, 2, 1, 20),
    _AlaIPsecStatisticsOutDiscarded_Type()
)
alaIPsecStatisticsOutDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecStatisticsOutDiscarded.setStatus("current")
_AlaIPsecSecurityPolicyTable_Object = MibTable
alaIPsecSecurityPolicyTable = _AlaIPsecSecurityPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyTable.setStatus("current")
_AlaIPsecSecurityPolicyEntry_Object = MibTableRow
alaIPsecSecurityPolicyEntry = _AlaIPsecSecurityPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1)
)
alaIPsecSecurityPolicyEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyID"),
)
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyEntry.setStatus("current")
_AlaIPsecSecurityPolicyID_Type = Unsigned32
_AlaIPsecSecurityPolicyID_Object = MibTableColumn
alaIPsecSecurityPolicyID = _AlaIPsecSecurityPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 1),
    _AlaIPsecSecurityPolicyID_Type()
)
alaIPsecSecurityPolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyID.setStatus("current")
_AlaIPsecSecurityPolicySourceType_Type = InetAddressType
_AlaIPsecSecurityPolicySourceType_Object = MibTableColumn
alaIPsecSecurityPolicySourceType = _AlaIPsecSecurityPolicySourceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 2),
    _AlaIPsecSecurityPolicySourceType_Type()
)
alaIPsecSecurityPolicySourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicySourceType.setStatus("current")
_AlaIPsecSecurityPolicySource_Type = InetAddress
_AlaIPsecSecurityPolicySource_Object = MibTableColumn
alaIPsecSecurityPolicySource = _AlaIPsecSecurityPolicySource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 3),
    _AlaIPsecSecurityPolicySource_Type()
)
alaIPsecSecurityPolicySource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicySource.setStatus("current")
_AlaIPsecSecurityPolicySourcePrefixLength_Type = IPsecPrefixLength
_AlaIPsecSecurityPolicySourcePrefixLength_Object = MibTableColumn
alaIPsecSecurityPolicySourcePrefixLength = _AlaIPsecSecurityPolicySourcePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 4),
    _AlaIPsecSecurityPolicySourcePrefixLength_Type()
)
alaIPsecSecurityPolicySourcePrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicySourcePrefixLength.setStatus("current")


class _AlaIPsecSecurityPolicySourcePort_Type(IPsecPortNumber):
    """Custom type alaIPsecSecurityPolicySourcePort based on IPsecPortNumber"""
    defaultValue = 0


_AlaIPsecSecurityPolicySourcePort_Type.__name__ = "IPsecPortNumber"
_AlaIPsecSecurityPolicySourcePort_Object = MibTableColumn
alaIPsecSecurityPolicySourcePort = _AlaIPsecSecurityPolicySourcePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 5),
    _AlaIPsecSecurityPolicySourcePort_Type()
)
alaIPsecSecurityPolicySourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicySourcePort.setStatus("current")
_AlaIPsecSecurityPolicyDestinationType_Type = InetAddressType
_AlaIPsecSecurityPolicyDestinationType_Object = MibTableColumn
alaIPsecSecurityPolicyDestinationType = _AlaIPsecSecurityPolicyDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 6),
    _AlaIPsecSecurityPolicyDestinationType_Type()
)
alaIPsecSecurityPolicyDestinationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyDestinationType.setStatus("current")
_AlaIPsecSecurityPolicyDestination_Type = InetAddress
_AlaIPsecSecurityPolicyDestination_Object = MibTableColumn
alaIPsecSecurityPolicyDestination = _AlaIPsecSecurityPolicyDestination_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 7),
    _AlaIPsecSecurityPolicyDestination_Type()
)
alaIPsecSecurityPolicyDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyDestination.setStatus("current")
_AlaIPsecSecurityPolicyDestinationPrefixLength_Type = IPsecPrefixLength
_AlaIPsecSecurityPolicyDestinationPrefixLength_Object = MibTableColumn
alaIPsecSecurityPolicyDestinationPrefixLength = _AlaIPsecSecurityPolicyDestinationPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 8),
    _AlaIPsecSecurityPolicyDestinationPrefixLength_Type()
)
alaIPsecSecurityPolicyDestinationPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyDestinationPrefixLength.setStatus("current")


class _AlaIPsecSecurityPolicyDestinationPort_Type(IPsecPortNumber):
    """Custom type alaIPsecSecurityPolicyDestinationPort based on IPsecPortNumber"""
    defaultValue = 0


_AlaIPsecSecurityPolicyDestinationPort_Type.__name__ = "IPsecPortNumber"
_AlaIPsecSecurityPolicyDestinationPort_Object = MibTableColumn
alaIPsecSecurityPolicyDestinationPort = _AlaIPsecSecurityPolicyDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 9),
    _AlaIPsecSecurityPolicyDestinationPort_Type()
)
alaIPsecSecurityPolicyDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyDestinationPort.setStatus("current")


class _AlaIPsecSecurityPolicyULProtocol_Type(IPsecULProtocol):
    """Custom type alaIPsecSecurityPolicyULProtocol based on IPsecULProtocol"""
    defaultValue = 255


_AlaIPsecSecurityPolicyULProtocol_Type.__name__ = "IPsecULProtocol"
_AlaIPsecSecurityPolicyULProtocol_Object = MibTableColumn
alaIPsecSecurityPolicyULProtocol = _AlaIPsecSecurityPolicyULProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 10),
    _AlaIPsecSecurityPolicyULProtocol_Type()
)
alaIPsecSecurityPolicyULProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyULProtocol.setStatus("current")


class _AlaIPsecSecurityPolicyICMPv6Type_Type(Integer32):
    """Custom type alaIPsecSecurityPolicyICMPv6Type based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaIPsecSecurityPolicyICMPv6Type_Type.__name__ = "Integer32"
_AlaIPsecSecurityPolicyICMPv6Type_Object = MibTableColumn
alaIPsecSecurityPolicyICMPv6Type = _AlaIPsecSecurityPolicyICMPv6Type_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 11),
    _AlaIPsecSecurityPolicyICMPv6Type_Type()
)
alaIPsecSecurityPolicyICMPv6Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyICMPv6Type.setStatus("current")


class _AlaIPsecSecurityPolicyDirection_Type(Integer32):
    """Custom type alaIPsecSecurityPolicyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_AlaIPsecSecurityPolicyDirection_Type.__name__ = "Integer32"
_AlaIPsecSecurityPolicyDirection_Object = MibTableColumn
alaIPsecSecurityPolicyDirection = _AlaIPsecSecurityPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 12),
    _AlaIPsecSecurityPolicyDirection_Type()
)
alaIPsecSecurityPolicyDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyDirection.setStatus("current")
_AlaIPsecSecurityPolicyName_Type = IPsecName
_AlaIPsecSecurityPolicyName_Object = MibTableColumn
alaIPsecSecurityPolicyName = _AlaIPsecSecurityPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 13),
    _AlaIPsecSecurityPolicyName_Type()
)
alaIPsecSecurityPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyName.setStatus("current")


class _AlaIPsecSecurityPolicyDescription_Type(IPsecDescription):
    """Custom type alaIPsecSecurityPolicyDescription based on IPsecDescription"""
    defaultValue = OctetString("")


_AlaIPsecSecurityPolicyDescription_Type.__name__ = "IPsecDescription"
_AlaIPsecSecurityPolicyDescription_Object = MibTableColumn
alaIPsecSecurityPolicyDescription = _AlaIPsecSecurityPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 14),
    _AlaIPsecSecurityPolicyDescription_Type()
)
alaIPsecSecurityPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyDescription.setStatus("current")


class _AlaIPsecSecurityPolicyAction_Type(Integer32):
    """Custom type alaIPsecSecurityPolicyAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("none", 1),
          ("ipsec", 2))
    )


_AlaIPsecSecurityPolicyAction_Type.__name__ = "Integer32"
_AlaIPsecSecurityPolicyAction_Object = MibTableColumn
alaIPsecSecurityPolicyAction = _AlaIPsecSecurityPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 15),
    _AlaIPsecSecurityPolicyAction_Type()
)
alaIPsecSecurityPolicyAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyAction.setStatus("current")


class _AlaIPsecSecurityPolicyAdminState_Type(IPsecAdminState):
    """Custom type alaIPsecSecurityPolicyAdminState based on IPsecAdminState"""
    defaultValue = 1


_AlaIPsecSecurityPolicyAdminState_Type.__name__ = "IPsecAdminState"
_AlaIPsecSecurityPolicyAdminState_Object = MibTableColumn
alaIPsecSecurityPolicyAdminState = _AlaIPsecSecurityPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 16),
    _AlaIPsecSecurityPolicyAdminState_Type()
)
alaIPsecSecurityPolicyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyAdminState.setStatus("current")
_AlaIPsecSecurityPolicyOperationalState_Type = IPsecOperationalState
_AlaIPsecSecurityPolicyOperationalState_Object = MibTableColumn
alaIPsecSecurityPolicyOperationalState = _AlaIPsecSecurityPolicyOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 17),
    _AlaIPsecSecurityPolicyOperationalState_Type()
)
alaIPsecSecurityPolicyOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyOperationalState.setStatus("current")


class _AlaIPsecSecurityPolicyPriority_Type(Integer32):
    """Custom type alaIPsecSecurityPolicyPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AlaIPsecSecurityPolicyPriority_Type.__name__ = "Integer32"
_AlaIPsecSecurityPolicyPriority_Object = MibTableColumn
alaIPsecSecurityPolicyPriority = _AlaIPsecSecurityPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 18),
    _AlaIPsecSecurityPolicyPriority_Type()
)
alaIPsecSecurityPolicyPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyPriority.setStatus("current")
_AlaIPsecSecurityPolicyRowStatus_Type = RowStatus
_AlaIPsecSecurityPolicyRowStatus_Object = MibTableColumn
alaIPsecSecurityPolicyRowStatus = _AlaIPsecSecurityPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 2, 1, 19),
    _AlaIPsecSecurityPolicyRowStatus_Type()
)
alaIPsecSecurityPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyRowStatus.setStatus("current")
_AlaIPsecSecurityPolicyRuleTable_Object = MibTable
alaIPsecSecurityPolicyRuleTable = _AlaIPsecSecurityPolicyRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyRuleTable.setStatus("current")
_AlaIPsecSecurityPolicyRuleEntry_Object = MibTableRow
alaIPsecSecurityPolicyRuleEntry = _AlaIPsecSecurityPolicyRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 3, 1)
)
alaIPsecSecurityPolicyRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyID"),
    (0, "ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyRuleIndex"),
)
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyRuleEntry.setStatus("current")


class _AlaIPsecSecurityPolicyRuleIndex_Type(Unsigned32):
    """Custom type alaIPsecSecurityPolicyRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AlaIPsecSecurityPolicyRuleIndex_Type.__name__ = "Unsigned32"
_AlaIPsecSecurityPolicyRuleIndex_Object = MibTableColumn
alaIPsecSecurityPolicyRuleIndex = _AlaIPsecSecurityPolicyRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 3, 1, 1),
    _AlaIPsecSecurityPolicyRuleIndex_Type()
)
alaIPsecSecurityPolicyRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyRuleIndex.setStatus("current")


class _AlaIPsecSecurityPolicyRuleProtocol_Type(Integer32):
    """Custom type alaIPsecSecurityPolicyRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ah", 1),
          ("esp", 2))
    )


_AlaIPsecSecurityPolicyRuleProtocol_Type.__name__ = "Integer32"
_AlaIPsecSecurityPolicyRuleProtocol_Object = MibTableColumn
alaIPsecSecurityPolicyRuleProtocol = _AlaIPsecSecurityPolicyRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 3, 1, 2),
    _AlaIPsecSecurityPolicyRuleProtocol_Type()
)
alaIPsecSecurityPolicyRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyRuleProtocol.setStatus("current")


class _AlaIPsecSecurityPolicyRuleMode_Type(Integer32):
    """Custom type alaIPsecSecurityPolicyRuleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("transport", 1)
    )


_AlaIPsecSecurityPolicyRuleMode_Type.__name__ = "Integer32"
_AlaIPsecSecurityPolicyRuleMode_Object = MibTableColumn
alaIPsecSecurityPolicyRuleMode = _AlaIPsecSecurityPolicyRuleMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 3, 1, 3),
    _AlaIPsecSecurityPolicyRuleMode_Type()
)
alaIPsecSecurityPolicyRuleMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyRuleMode.setStatus("current")
_AlaIPsecSecurityPolicyRuleRowStatus_Type = RowStatus
_AlaIPsecSecurityPolicyRuleRowStatus_Object = MibTableColumn
alaIPsecSecurityPolicyRuleRowStatus = _AlaIPsecSecurityPolicyRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 3, 1, 4),
    _AlaIPsecSecurityPolicyRuleRowStatus_Type()
)
alaIPsecSecurityPolicyRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyRuleRowStatus.setStatus("current")
_AlaIPsecSAConfigTable_Object = MibTable
alaIPsecSAConfigTable = _AlaIPsecSAConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaIPsecSAConfigTable.setStatus("current")
_AlaIPsecSAConfigEntry_Object = MibTableRow
alaIPsecSAConfigEntry = _AlaIPsecSAConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1)
)
alaIPsecSAConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigID"),
)
if mibBuilder.loadTexts:
    alaIPsecSAConfigEntry.setStatus("current")
_AlaIPsecSAConfigID_Type = Unsigned32
_AlaIPsecSAConfigID_Object = MibTableColumn
alaIPsecSAConfigID = _AlaIPsecSAConfigID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1, 1),
    _AlaIPsecSAConfigID_Type()
)
alaIPsecSAConfigID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPsecSAConfigID.setStatus("current")
_AlaIPsecSAConfigType_Type = IPsecSAType
_AlaIPsecSAConfigType_Object = MibTableColumn
alaIPsecSAConfigType = _AlaIPsecSAConfigType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1, 2),
    _AlaIPsecSAConfigType_Type()
)
alaIPsecSAConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSAConfigType.setStatus("current")
_AlaIPsecSAConfigSourceType_Type = InetAddressType
_AlaIPsecSAConfigSourceType_Object = MibTableColumn
alaIPsecSAConfigSourceType = _AlaIPsecSAConfigSourceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1, 3),
    _AlaIPsecSAConfigSourceType_Type()
)
alaIPsecSAConfigSourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSAConfigSourceType.setStatus("current")
_AlaIPsecSAConfigSource_Type = InetAddress
_AlaIPsecSAConfigSource_Object = MibTableColumn
alaIPsecSAConfigSource = _AlaIPsecSAConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1, 4),
    _AlaIPsecSAConfigSource_Type()
)
alaIPsecSAConfigSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSAConfigSource.setStatus("current")
_AlaIPsecSAConfigDestinationType_Type = InetAddressType
_AlaIPsecSAConfigDestinationType_Object = MibTableColumn
alaIPsecSAConfigDestinationType = _AlaIPsecSAConfigDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1, 5),
    _AlaIPsecSAConfigDestinationType_Type()
)
alaIPsecSAConfigDestinationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSAConfigDestinationType.setStatus("current")
_AlaIPsecSAConfigDestination_Type = InetAddress
_AlaIPsecSAConfigDestination_Object = MibTableColumn
alaIPsecSAConfigDestination = _AlaIPsecSAConfigDestination_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1, 6),
    _AlaIPsecSAConfigDestination_Type()
)
alaIPsecSAConfigDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSAConfigDestination.setStatus("current")
_AlaIPsecSAConfigSPI_Type = Unsigned32
_AlaIPsecSAConfigSPI_Object = MibTableColumn
alaIPsecSAConfigSPI = _AlaIPsecSAConfigSPI_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1, 7),
    _AlaIPsecSAConfigSPI_Type()
)
alaIPsecSAConfigSPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSAConfigSPI.setStatus("current")
_AlaIPsecSAConfigName_Type = IPsecName
_AlaIPsecSAConfigName_Object = MibTableColumn
alaIPsecSAConfigName = _AlaIPsecSAConfigName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1, 8),
    _AlaIPsecSAConfigName_Type()
)
alaIPsecSAConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSAConfigName.setStatus("current")


class _AlaIPsecSAConfigDescription_Type(IPsecDescription):
    """Custom type alaIPsecSAConfigDescription based on IPsecDescription"""
    defaultValue = OctetString("")


_AlaIPsecSAConfigDescription_Type.__name__ = "IPsecDescription"
_AlaIPsecSAConfigDescription_Object = MibTableColumn
alaIPsecSAConfigDescription = _AlaIPsecSAConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1, 9),
    _AlaIPsecSAConfigDescription_Type()
)
alaIPsecSAConfigDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSAConfigDescription.setStatus("current")


class _AlaIPsecSAConfigEncryptionAlgorithm_Type(IPsecESPAlgorithm):
    """Custom type alaIPsecSAConfigEncryptionAlgorithm based on IPsecESPAlgorithm"""
    defaultValue = 0


_AlaIPsecSAConfigEncryptionAlgorithm_Type.__name__ = "IPsecESPAlgorithm"
_AlaIPsecSAConfigEncryptionAlgorithm_Object = MibTableColumn
alaIPsecSAConfigEncryptionAlgorithm = _AlaIPsecSAConfigEncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1, 10),
    _AlaIPsecSAConfigEncryptionAlgorithm_Type()
)
alaIPsecSAConfigEncryptionAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSAConfigEncryptionAlgorithm.setStatus("current")


class _AlaIPsecSAConfigEncryptionKeyLength_Type(Unsigned32):
    """Custom type alaIPsecSAConfigEncryptionKeyLength based on Unsigned32"""
    defaultValue = 0


_AlaIPsecSAConfigEncryptionKeyLength_Type.__name__ = "Unsigned32"
_AlaIPsecSAConfigEncryptionKeyLength_Object = MibTableColumn
alaIPsecSAConfigEncryptionKeyLength = _AlaIPsecSAConfigEncryptionKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1, 11),
    _AlaIPsecSAConfigEncryptionKeyLength_Type()
)
alaIPsecSAConfigEncryptionKeyLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSAConfigEncryptionKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    alaIPsecSAConfigEncryptionKeyLength.setUnits("bits")


class _AlaIPsecSAConfigAuthenticationAlgorithm_Type(IPsecAHAlgorithm):
    """Custom type alaIPsecSAConfigAuthenticationAlgorithm based on IPsecAHAlgorithm"""
    defaultValue = 0


_AlaIPsecSAConfigAuthenticationAlgorithm_Type.__name__ = "IPsecAHAlgorithm"
_AlaIPsecSAConfigAuthenticationAlgorithm_Object = MibTableColumn
alaIPsecSAConfigAuthenticationAlgorithm = _AlaIPsecSAConfigAuthenticationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1, 12),
    _AlaIPsecSAConfigAuthenticationAlgorithm_Type()
)
alaIPsecSAConfigAuthenticationAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSAConfigAuthenticationAlgorithm.setStatus("current")


class _AlaIPsecSAConfigAdminState_Type(IPsecAdminState):
    """Custom type alaIPsecSAConfigAdminState based on IPsecAdminState"""
    defaultValue = 1


_AlaIPsecSAConfigAdminState_Type.__name__ = "IPsecAdminState"
_AlaIPsecSAConfigAdminState_Object = MibTableColumn
alaIPsecSAConfigAdminState = _AlaIPsecSAConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1, 13),
    _AlaIPsecSAConfigAdminState_Type()
)
alaIPsecSAConfigAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSAConfigAdminState.setStatus("current")
_AlaIPsecSAConfigOperationalState_Type = IPsecOperationalState
_AlaIPsecSAConfigOperationalState_Object = MibTableColumn
alaIPsecSAConfigOperationalState = _AlaIPsecSAConfigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1, 14),
    _AlaIPsecSAConfigOperationalState_Type()
)
alaIPsecSAConfigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIPsecSAConfigOperationalState.setStatus("current")
_AlaIPsecSAConfigRowStatus_Type = RowStatus
_AlaIPsecSAConfigRowStatus_Object = MibTableColumn
alaIPsecSAConfigRowStatus = _AlaIPsecSAConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 4, 1, 15),
    _AlaIPsecSAConfigRowStatus_Type()
)
alaIPsecSAConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecSAConfigRowStatus.setStatus("current")
_AlaIPsecKeyTable_Object = MibTable
alaIPsecKeyTable = _AlaIPsecKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaIPsecKeyTable.setStatus("current")
_AlaIPsecKeyEntry_Object = MibTableRow
alaIPsecKeyEntry = _AlaIPsecKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 5, 1)
)
alaIPsecKeyEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPSEC-MIB", "alaIPsecKeyID"),
)
if mibBuilder.loadTexts:
    alaIPsecKeyEntry.setStatus("current")
_AlaIPsecKeyID_Type = Unsigned32
_AlaIPsecKeyID_Object = MibTableColumn
alaIPsecKeyID = _AlaIPsecKeyID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 5, 1, 1),
    _AlaIPsecKeyID_Type()
)
alaIPsecKeyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIPsecKeyID.setStatus("current")


class _AlaIPsecKeyType_Type(Integer32):
    """Custom type alaIPsecKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("saAuthentication", 1),
          ("saEncryption", 2))
    )


_AlaIPsecKeyType_Type.__name__ = "Integer32"
_AlaIPsecKeyType_Object = MibTableColumn
alaIPsecKeyType = _AlaIPsecKeyType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 5, 1, 2),
    _AlaIPsecKeyType_Type()
)
alaIPsecKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecKeyType.setStatus("current")


class _AlaIPsecKeyName_Type(OctetString):
    """Custom type alaIPsecKeyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AlaIPsecKeyName_Type.__name__ = "OctetString"
_AlaIPsecKeyName_Object = MibTableColumn
alaIPsecKeyName = _AlaIPsecKeyName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 5, 1, 3),
    _AlaIPsecKeyName_Type()
)
alaIPsecKeyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecKeyName.setStatus("current")
_AlaIPsecKey_Type = OctetString
_AlaIPsecKey_Object = MibTableColumn
alaIPsecKey = _AlaIPsecKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 5, 1, 4),
    _AlaIPsecKey_Type()
)
alaIPsecKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecKey.setStatus("current")


class _AlaIPsecKeyEncrypted_Type(TruthValue):
    """Custom type alaIPsecKeyEncrypted based on TruthValue"""
    defaultValue = 2


_AlaIPsecKeyEncrypted_Type.__name__ = "TruthValue"
_AlaIPsecKeyEncrypted_Object = MibTableColumn
alaIPsecKeyEncrypted = _AlaIPsecKeyEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 5, 1, 5),
    _AlaIPsecKeyEncrypted_Type()
)
alaIPsecKeyEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecKeyEncrypted.setStatus("current")
_AlaIPsecKeyRowStatus_Type = RowStatus
_AlaIPsecKeyRowStatus_Object = MibTableColumn
alaIPsecKeyRowStatus = _AlaIPsecKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 1, 5, 1, 6),
    _AlaIPsecKeyRowStatus_Type()
)
alaIPsecKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIPsecKeyRowStatus.setStatus("current")
_AlcatelIND1IPsecMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1IPsecMIBConformance = _AlcatelIND1IPsecMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 2)
)
_AlcatelIND1IPsecMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1IPsecMIBCompliances = _AlcatelIND1IPsecMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 2, 1)
)
_AlcatelIND1IPsecMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1IPsecMIBGroups = _AlcatelIND1IPsecMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 2, 2)
)

# Managed Objects groups

alaIPsecConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 2, 2, 1)
)
alaIPsecConfigGroup.setObjects(
      *(("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityKeyCurrent"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityKeyNew"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInSuccessful"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInPolicyViolation"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInNoSA"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInUnknownSPI"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInAHReplay"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInESPReplay"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInAHAuthenticationSuccess"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInAHAuthenticationFail"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInESPAuthenticationSuccess"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInESPAuthenticationFail"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInBadPacket"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInNoMemory"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsOutSuccessful"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsOutPolicyViolation"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsOutNoSA"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsOutBadPacket"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsOutNoMemory"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsInDiscarded"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecStatisticsOutDiscarded"))
)
if mibBuilder.loadTexts:
    alaIPsecConfigGroup.setStatus("current")

alaIPsecSecurityPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 2, 2, 2)
)
alaIPsecSecurityPolicyGroup.setObjects(
      *(("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicySource"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicySourceType"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicySourcePrefixLength"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicySourcePort"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyDestination"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyDestinationType"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyDestinationPrefixLength"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyDestinationPort"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyULProtocol"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyICMPv6Type"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyDirection"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyName"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyDescription"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyAction"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyAdminState"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyOperationalState"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyPriority"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyRowStatus"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyRuleProtocol"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyRuleMode"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyRuleRowStatus"))
)
if mibBuilder.loadTexts:
    alaIPsecSecurityPolicyGroup.setStatus("current")

alaIPsecSAConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 2, 2, 3)
)
alaIPsecSAConfigGroup.setObjects(
      *(("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigType"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigSource"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigSourceType"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigDestination"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigDestinationType"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigSPI"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigName"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigDescription"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigEncryptionAlgorithm"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigEncryptionKeyLength"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigAuthenticationAlgorithm"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigAdminState"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigOperationalState"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigRowStatus"))
)
if mibBuilder.loadTexts:
    alaIPsecSAConfigGroup.setStatus("current")

alaIPsecKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 2, 2, 4)
)
alaIPsecKeyGroup.setObjects(
      *(("ALCATEL-IND1-IPSEC-MIB", "alaIPsecKeyType"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecKeyName"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecKey"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecKeyEncrypted"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecKeyRowStatus"))
)
if mibBuilder.loadTexts:
    alaIPsecKeyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaIPsecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 43, 1, 2, 1, 1)
)
alaIPsecCompliance.setObjects(
      *(("ALCATEL-IND1-IPSEC-MIB", "alaIPsecConfigGroup"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSecurityPolicyGroup"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecSAConfigGroup"),
        ("ALCATEL-IND1-IPSEC-MIB", "alaIPsecKeyGroup"))
)
if mibBuilder.loadTexts:
    alaIPsecCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-IPSEC-MIB",
    **{"IPsecName": IPsecName,
       "IPsecDescription": IPsecDescription,
       "IPsecPortNumber": IPsecPortNumber,
       "IPsecPrefixLength": IPsecPrefixLength,
       "IPsecULProtocol": IPsecULProtocol,
       "IPsecAdminState": IPsecAdminState,
       "IPsecSAType": IPsecSAType,
       "IPsecESPAlgorithm": IPsecESPAlgorithm,
       "IPsecAHAlgorithm": IPsecAHAlgorithm,
       "IPsecOperationalState": IPsecOperationalState,
       "alcatelIND1IPsecMIB": alcatelIND1IPsecMIB,
       "alcatelIND1IPsecMIBObjects": alcatelIND1IPsecMIBObjects,
       "alaIPsecConfig": alaIPsecConfig,
       "alaIPsecSecurityKeyTable": alaIPsecSecurityKeyTable,
       "alaIPsecSecurityKeyEntry": alaIPsecSecurityKeyEntry,
       "alaIPsecSecurityKeyID": alaIPsecSecurityKeyID,
       "alaIPsecSecurityKeyCurrent": alaIPsecSecurityKeyCurrent,
       "alaIPsecSecurityKeyNew": alaIPsecSecurityKeyNew,
       "alaIPsecStatisticsTable": alaIPsecStatisticsTable,
       "alaIPsecStatisticsEntry": alaIPsecStatisticsEntry,
       "alaIPsecStatisticsProtocol": alaIPsecStatisticsProtocol,
       "alaIPsecStatisticsInSuccessful": alaIPsecStatisticsInSuccessful,
       "alaIPsecStatisticsInPolicyViolation": alaIPsecStatisticsInPolicyViolation,
       "alaIPsecStatisticsInNoSA": alaIPsecStatisticsInNoSA,
       "alaIPsecStatisticsInUnknownSPI": alaIPsecStatisticsInUnknownSPI,
       "alaIPsecStatisticsInAHReplay": alaIPsecStatisticsInAHReplay,
       "alaIPsecStatisticsInESPReplay": alaIPsecStatisticsInESPReplay,
       "alaIPsecStatisticsInAHAuthenticationSuccess": alaIPsecStatisticsInAHAuthenticationSuccess,
       "alaIPsecStatisticsInAHAuthenticationFail": alaIPsecStatisticsInAHAuthenticationFail,
       "alaIPsecStatisticsInESPAuthenticationSuccess": alaIPsecStatisticsInESPAuthenticationSuccess,
       "alaIPsecStatisticsInESPAuthenticationFail": alaIPsecStatisticsInESPAuthenticationFail,
       "alaIPsecStatisticsInBadPacket": alaIPsecStatisticsInBadPacket,
       "alaIPsecStatisticsInNoMemory": alaIPsecStatisticsInNoMemory,
       "alaIPsecStatisticsOutSuccessful": alaIPsecStatisticsOutSuccessful,
       "alaIPsecStatisticsOutPolicyViolation": alaIPsecStatisticsOutPolicyViolation,
       "alaIPsecStatisticsOutNoSA": alaIPsecStatisticsOutNoSA,
       "alaIPsecStatisticsOutBadPacket": alaIPsecStatisticsOutBadPacket,
       "alaIPsecStatisticsOutNoMemory": alaIPsecStatisticsOutNoMemory,
       "alaIPsecStatisticsInDiscarded": alaIPsecStatisticsInDiscarded,
       "alaIPsecStatisticsOutDiscarded": alaIPsecStatisticsOutDiscarded,
       "alaIPsecSecurityPolicyTable": alaIPsecSecurityPolicyTable,
       "alaIPsecSecurityPolicyEntry": alaIPsecSecurityPolicyEntry,
       "alaIPsecSecurityPolicyID": alaIPsecSecurityPolicyID,
       "alaIPsecSecurityPolicySourceType": alaIPsecSecurityPolicySourceType,
       "alaIPsecSecurityPolicySource": alaIPsecSecurityPolicySource,
       "alaIPsecSecurityPolicySourcePrefixLength": alaIPsecSecurityPolicySourcePrefixLength,
       "alaIPsecSecurityPolicySourcePort": alaIPsecSecurityPolicySourcePort,
       "alaIPsecSecurityPolicyDestinationType": alaIPsecSecurityPolicyDestinationType,
       "alaIPsecSecurityPolicyDestination": alaIPsecSecurityPolicyDestination,
       "alaIPsecSecurityPolicyDestinationPrefixLength": alaIPsecSecurityPolicyDestinationPrefixLength,
       "alaIPsecSecurityPolicyDestinationPort": alaIPsecSecurityPolicyDestinationPort,
       "alaIPsecSecurityPolicyULProtocol": alaIPsecSecurityPolicyULProtocol,
       "alaIPsecSecurityPolicyICMPv6Type": alaIPsecSecurityPolicyICMPv6Type,
       "alaIPsecSecurityPolicyDirection": alaIPsecSecurityPolicyDirection,
       "alaIPsecSecurityPolicyName": alaIPsecSecurityPolicyName,
       "alaIPsecSecurityPolicyDescription": alaIPsecSecurityPolicyDescription,
       "alaIPsecSecurityPolicyAction": alaIPsecSecurityPolicyAction,
       "alaIPsecSecurityPolicyAdminState": alaIPsecSecurityPolicyAdminState,
       "alaIPsecSecurityPolicyOperationalState": alaIPsecSecurityPolicyOperationalState,
       "alaIPsecSecurityPolicyPriority": alaIPsecSecurityPolicyPriority,
       "alaIPsecSecurityPolicyRowStatus": alaIPsecSecurityPolicyRowStatus,
       "alaIPsecSecurityPolicyRuleTable": alaIPsecSecurityPolicyRuleTable,
       "alaIPsecSecurityPolicyRuleEntry": alaIPsecSecurityPolicyRuleEntry,
       "alaIPsecSecurityPolicyRuleIndex": alaIPsecSecurityPolicyRuleIndex,
       "alaIPsecSecurityPolicyRuleProtocol": alaIPsecSecurityPolicyRuleProtocol,
       "alaIPsecSecurityPolicyRuleMode": alaIPsecSecurityPolicyRuleMode,
       "alaIPsecSecurityPolicyRuleRowStatus": alaIPsecSecurityPolicyRuleRowStatus,
       "alaIPsecSAConfigTable": alaIPsecSAConfigTable,
       "alaIPsecSAConfigEntry": alaIPsecSAConfigEntry,
       "alaIPsecSAConfigID": alaIPsecSAConfigID,
       "alaIPsecSAConfigType": alaIPsecSAConfigType,
       "alaIPsecSAConfigSourceType": alaIPsecSAConfigSourceType,
       "alaIPsecSAConfigSource": alaIPsecSAConfigSource,
       "alaIPsecSAConfigDestinationType": alaIPsecSAConfigDestinationType,
       "alaIPsecSAConfigDestination": alaIPsecSAConfigDestination,
       "alaIPsecSAConfigSPI": alaIPsecSAConfigSPI,
       "alaIPsecSAConfigName": alaIPsecSAConfigName,
       "alaIPsecSAConfigDescription": alaIPsecSAConfigDescription,
       "alaIPsecSAConfigEncryptionAlgorithm": alaIPsecSAConfigEncryptionAlgorithm,
       "alaIPsecSAConfigEncryptionKeyLength": alaIPsecSAConfigEncryptionKeyLength,
       "alaIPsecSAConfigAuthenticationAlgorithm": alaIPsecSAConfigAuthenticationAlgorithm,
       "alaIPsecSAConfigAdminState": alaIPsecSAConfigAdminState,
       "alaIPsecSAConfigOperationalState": alaIPsecSAConfigOperationalState,
       "alaIPsecSAConfigRowStatus": alaIPsecSAConfigRowStatus,
       "alaIPsecKeyTable": alaIPsecKeyTable,
       "alaIPsecKeyEntry": alaIPsecKeyEntry,
       "alaIPsecKeyID": alaIPsecKeyID,
       "alaIPsecKeyType": alaIPsecKeyType,
       "alaIPsecKeyName": alaIPsecKeyName,
       "alaIPsecKey": alaIPsecKey,
       "alaIPsecKeyEncrypted": alaIPsecKeyEncrypted,
       "alaIPsecKeyRowStatus": alaIPsecKeyRowStatus,
       "alcatelIND1IPsecMIBConformance": alcatelIND1IPsecMIBConformance,
       "alcatelIND1IPsecMIBCompliances": alcatelIND1IPsecMIBCompliances,
       "alaIPsecCompliance": alaIPsecCompliance,
       "alcatelIND1IPsecMIBGroups": alcatelIND1IPsecMIBGroups,
       "alaIPsecConfigGroup": alaIPsecConfigGroup,
       "alaIPsecSecurityPolicyGroup": alaIPsecSecurityPolicyGroup,
       "alaIPsecSAConfigGroup": alaIPsecSAConfigGroup,
       "alaIPsecKeyGroup": alaIPsecKeyGroup}
)
