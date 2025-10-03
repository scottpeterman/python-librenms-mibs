# SNMP MIB module (DOCS-BPI2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\DOCS-BPI2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:37 2025
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

(docsIfMib,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfMib")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

docsBpi2MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 6)
)
if mibBuilder.loadTexts:
    docsBpi2MIB.setRevisions(
        ("2001-04-17 00:00",
         "2000-11-17 19:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class X509Certificate(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )



# MIB Managed Objects in the order of their OIDs

_DocsBpi2MIBObjects_ObjectIdentity = ObjectIdentity
docsBpi2MIBObjects = _DocsBpi2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1)
)
_DocsBpi2CmObjects_ObjectIdentity = ObjectIdentity
docsBpi2CmObjects = _DocsBpi2CmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1)
)
_DocsBpi2CmBaseTable_Object = MibTable
docsBpi2CmBaseTable = _DocsBpi2CmBaseTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    docsBpi2CmBaseTable.setStatus("current")
_DocsBpi2CmBaseEntry_Object = MibTableRow
docsBpi2CmBaseEntry = _DocsBpi2CmBaseEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1)
)
docsBpi2CmBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsBpi2CmBaseEntry.setStatus("current")
_DocsBpi2CmPrivacyEnable_Type = TruthValue
_DocsBpi2CmPrivacyEnable_Object = MibTableColumn
docsBpi2CmPrivacyEnable = _DocsBpi2CmPrivacyEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 1),
    _DocsBpi2CmPrivacyEnable_Type()
)
docsBpi2CmPrivacyEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmPrivacyEnable.setStatus("current")


class _DocsBpi2CmPublicKey_Type(OctetString):
    """Custom type docsBpi2CmPublicKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(74, 74),
        ValueSizeConstraint(106, 106),
        ValueSizeConstraint(140, 140),
        ValueSizeConstraint(204, 204),
        ValueSizeConstraint(270, 270),
    )


_DocsBpi2CmPublicKey_Type.__name__ = "OctetString"
_DocsBpi2CmPublicKey_Object = MibTableColumn
docsBpi2CmPublicKey = _DocsBpi2CmPublicKey_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 2),
    _DocsBpi2CmPublicKey_Type()
)
docsBpi2CmPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmPublicKey.setStatus("current")


class _DocsBpi2CmAuthState_Type(Integer32):
    """Custom type docsBpi2CmAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("authWait", 2),
          ("authorized", 3),
          ("reauthWait", 4),
          ("authRejectWait", 5),
          ("silent", 6))
    )


_DocsBpi2CmAuthState_Type.__name__ = "Integer32"
_DocsBpi2CmAuthState_Object = MibTableColumn
docsBpi2CmAuthState = _DocsBpi2CmAuthState_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 3),
    _DocsBpi2CmAuthState_Type()
)
docsBpi2CmAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthState.setStatus("current")


class _DocsBpi2CmAuthKeySequenceNumber_Type(Integer32):
    """Custom type docsBpi2CmAuthKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DocsBpi2CmAuthKeySequenceNumber_Type.__name__ = "Integer32"
_DocsBpi2CmAuthKeySequenceNumber_Object = MibTableColumn
docsBpi2CmAuthKeySequenceNumber = _DocsBpi2CmAuthKeySequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 4),
    _DocsBpi2CmAuthKeySequenceNumber_Type()
)
docsBpi2CmAuthKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthKeySequenceNumber.setStatus("current")
_DocsBpi2CmAuthExpiresOld_Type = DateAndTime
_DocsBpi2CmAuthExpiresOld_Object = MibTableColumn
docsBpi2CmAuthExpiresOld = _DocsBpi2CmAuthExpiresOld_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 5),
    _DocsBpi2CmAuthExpiresOld_Type()
)
docsBpi2CmAuthExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthExpiresOld.setStatus("current")
_DocsBpi2CmAuthExpiresNew_Type = DateAndTime
_DocsBpi2CmAuthExpiresNew_Object = MibTableColumn
docsBpi2CmAuthExpiresNew = _DocsBpi2CmAuthExpiresNew_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 6),
    _DocsBpi2CmAuthExpiresNew_Type()
)
docsBpi2CmAuthExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthExpiresNew.setStatus("current")
_DocsBpi2CmAuthReset_Type = TruthValue
_DocsBpi2CmAuthReset_Object = MibTableColumn
docsBpi2CmAuthReset = _DocsBpi2CmAuthReset_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 7),
    _DocsBpi2CmAuthReset_Type()
)
docsBpi2CmAuthReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpi2CmAuthReset.setStatus("current")


class _DocsBpi2CmAuthGraceTime_Type(Integer32):
    """Custom type docsBpi2CmAuthGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6047999),
    )


_DocsBpi2CmAuthGraceTime_Type.__name__ = "Integer32"
_DocsBpi2CmAuthGraceTime_Object = MibTableColumn
docsBpi2CmAuthGraceTime = _DocsBpi2CmAuthGraceTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 8),
    _DocsBpi2CmAuthGraceTime_Type()
)
docsBpi2CmAuthGraceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    docsBpi2CmAuthGraceTime.setUnits("seconds")


class _DocsBpi2CmTEKGraceTime_Type(Integer32):
    """Custom type docsBpi2CmTEKGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 302399),
    )


_DocsBpi2CmTEKGraceTime_Type.__name__ = "Integer32"
_DocsBpi2CmTEKGraceTime_Object = MibTableColumn
docsBpi2CmTEKGraceTime = _DocsBpi2CmTEKGraceTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 9),
    _DocsBpi2CmTEKGraceTime_Type()
)
docsBpi2CmTEKGraceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    docsBpi2CmTEKGraceTime.setUnits("seconds")


class _DocsBpi2CmAuthWaitTimeout_Type(Integer32):
    """Custom type docsBpi2CmAuthWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_DocsBpi2CmAuthWaitTimeout_Type.__name__ = "Integer32"
_DocsBpi2CmAuthWaitTimeout_Object = MibTableColumn
docsBpi2CmAuthWaitTimeout = _DocsBpi2CmAuthWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 10),
    _DocsBpi2CmAuthWaitTimeout_Type()
)
docsBpi2CmAuthWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsBpi2CmAuthWaitTimeout.setUnits("seconds")


class _DocsBpi2CmReauthWaitTimeout_Type(Integer32):
    """Custom type docsBpi2CmReauthWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_DocsBpi2CmReauthWaitTimeout_Type.__name__ = "Integer32"
_DocsBpi2CmReauthWaitTimeout_Object = MibTableColumn
docsBpi2CmReauthWaitTimeout = _DocsBpi2CmReauthWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 11),
    _DocsBpi2CmReauthWaitTimeout_Type()
)
docsBpi2CmReauthWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmReauthWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsBpi2CmReauthWaitTimeout.setUnits("seconds")


class _DocsBpi2CmOpWaitTimeout_Type(Integer32):
    """Custom type docsBpi2CmOpWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DocsBpi2CmOpWaitTimeout_Type.__name__ = "Integer32"
_DocsBpi2CmOpWaitTimeout_Object = MibTableColumn
docsBpi2CmOpWaitTimeout = _DocsBpi2CmOpWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 12),
    _DocsBpi2CmOpWaitTimeout_Type()
)
docsBpi2CmOpWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmOpWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsBpi2CmOpWaitTimeout.setUnits("seconds")


class _DocsBpi2CmRekeyWaitTimeout_Type(Integer32):
    """Custom type docsBpi2CmRekeyWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DocsBpi2CmRekeyWaitTimeout_Type.__name__ = "Integer32"
_DocsBpi2CmRekeyWaitTimeout_Object = MibTableColumn
docsBpi2CmRekeyWaitTimeout = _DocsBpi2CmRekeyWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 13),
    _DocsBpi2CmRekeyWaitTimeout_Type()
)
docsBpi2CmRekeyWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmRekeyWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsBpi2CmRekeyWaitTimeout.setUnits("seconds")


class _DocsBpi2CmAuthRejectWaitTimeout_Type(Integer32):
    """Custom type docsBpi2CmAuthRejectWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_DocsBpi2CmAuthRejectWaitTimeout_Type.__name__ = "Integer32"
_DocsBpi2CmAuthRejectWaitTimeout_Object = MibTableColumn
docsBpi2CmAuthRejectWaitTimeout = _DocsBpi2CmAuthRejectWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 14),
    _DocsBpi2CmAuthRejectWaitTimeout_Type()
)
docsBpi2CmAuthRejectWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthRejectWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsBpi2CmAuthRejectWaitTimeout.setUnits("seconds")


class _DocsBpi2CmSAMapWaitTimeout_Type(Integer32):
    """Custom type docsBpi2CmSAMapWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DocsBpi2CmSAMapWaitTimeout_Type.__name__ = "Integer32"
_DocsBpi2CmSAMapWaitTimeout_Object = MibTableColumn
docsBpi2CmSAMapWaitTimeout = _DocsBpi2CmSAMapWaitTimeout_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 15),
    _DocsBpi2CmSAMapWaitTimeout_Type()
)
docsBpi2CmSAMapWaitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmSAMapWaitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsBpi2CmSAMapWaitTimeout.setUnits("seconds")


class _DocsBpi2CmSAMapMaxRetries_Type(Integer32):
    """Custom type docsBpi2CmSAMapMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DocsBpi2CmSAMapMaxRetries_Type.__name__ = "Integer32"
_DocsBpi2CmSAMapMaxRetries_Object = MibTableColumn
docsBpi2CmSAMapMaxRetries = _DocsBpi2CmSAMapMaxRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 16),
    _DocsBpi2CmSAMapMaxRetries_Type()
)
docsBpi2CmSAMapMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmSAMapMaxRetries.setStatus("current")
if mibBuilder.loadTexts:
    docsBpi2CmSAMapMaxRetries.setUnits("count")
_DocsBpi2CmAuthentInfos_Type = Counter32
_DocsBpi2CmAuthentInfos_Object = MibTableColumn
docsBpi2CmAuthentInfos = _DocsBpi2CmAuthentInfos_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 17),
    _DocsBpi2CmAuthentInfos_Type()
)
docsBpi2CmAuthentInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthentInfos.setStatus("current")
_DocsBpi2CmAuthRequests_Type = Counter32
_DocsBpi2CmAuthRequests_Object = MibTableColumn
docsBpi2CmAuthRequests = _DocsBpi2CmAuthRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 18),
    _DocsBpi2CmAuthRequests_Type()
)
docsBpi2CmAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthRequests.setStatus("current")
_DocsBpi2CmAuthReplies_Type = Counter32
_DocsBpi2CmAuthReplies_Object = MibTableColumn
docsBpi2CmAuthReplies = _DocsBpi2CmAuthReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 19),
    _DocsBpi2CmAuthReplies_Type()
)
docsBpi2CmAuthReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthReplies.setStatus("current")
_DocsBpi2CmAuthRejects_Type = Counter32
_DocsBpi2CmAuthRejects_Object = MibTableColumn
docsBpi2CmAuthRejects = _DocsBpi2CmAuthRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 20),
    _DocsBpi2CmAuthRejects_Type()
)
docsBpi2CmAuthRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthRejects.setStatus("current")
_DocsBpi2CmAuthInvalids_Type = Counter32
_DocsBpi2CmAuthInvalids_Object = MibTableColumn
docsBpi2CmAuthInvalids = _DocsBpi2CmAuthInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 21),
    _DocsBpi2CmAuthInvalids_Type()
)
docsBpi2CmAuthInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthInvalids.setStatus("current")


class _DocsBpi2CmAuthRejectErrorCode_Type(Integer32):
    """Custom type docsBpi2CmAuthRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              11)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("unauthorizedCm", 3),
          ("unauthorizedSaid", 4),
          ("permanentAuthorizationFailure", 8),
          ("timeOfDayNotAcquired", 11))
    )


_DocsBpi2CmAuthRejectErrorCode_Type.__name__ = "Integer32"
_DocsBpi2CmAuthRejectErrorCode_Object = MibTableColumn
docsBpi2CmAuthRejectErrorCode = _DocsBpi2CmAuthRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 22),
    _DocsBpi2CmAuthRejectErrorCode_Type()
)
docsBpi2CmAuthRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthRejectErrorCode.setStatus("current")


class _DocsBpi2CmAuthRejectErrorString_Type(SnmpAdminString):
    """Custom type docsBpi2CmAuthRejectErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpi2CmAuthRejectErrorString_Type.__name__ = "SnmpAdminString"
_DocsBpi2CmAuthRejectErrorString_Object = MibTableColumn
docsBpi2CmAuthRejectErrorString = _DocsBpi2CmAuthRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 23),
    _DocsBpi2CmAuthRejectErrorString_Type()
)
docsBpi2CmAuthRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthRejectErrorString.setStatus("current")


class _DocsBpi2CmAuthInvalidErrorCode_Type(Integer32):
    """Custom type docsBpi2CmAuthInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("unauthorizedCm", 3),
          ("unsolicited", 5),
          ("invalidKeySequence", 6),
          ("keyRequestAuthenticationFailure", 7))
    )


_DocsBpi2CmAuthInvalidErrorCode_Type.__name__ = "Integer32"
_DocsBpi2CmAuthInvalidErrorCode_Object = MibTableColumn
docsBpi2CmAuthInvalidErrorCode = _DocsBpi2CmAuthInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 24),
    _DocsBpi2CmAuthInvalidErrorCode_Type()
)
docsBpi2CmAuthInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthInvalidErrorCode.setStatus("current")


class _DocsBpi2CmAuthInvalidErrorString_Type(SnmpAdminString):
    """Custom type docsBpi2CmAuthInvalidErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpi2CmAuthInvalidErrorString_Type.__name__ = "SnmpAdminString"
_DocsBpi2CmAuthInvalidErrorString_Object = MibTableColumn
docsBpi2CmAuthInvalidErrorString = _DocsBpi2CmAuthInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 1, 1, 25),
    _DocsBpi2CmAuthInvalidErrorString_Type()
)
docsBpi2CmAuthInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmAuthInvalidErrorString.setStatus("current")
_DocsBpi2CmTEKTable_Object = MibTable
docsBpi2CmTEKTable = _DocsBpi2CmTEKTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    docsBpi2CmTEKTable.setStatus("current")
_DocsBpi2CmTEKEntry_Object = MibTableRow
docsBpi2CmTEKEntry = _DocsBpi2CmTEKEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1)
)
docsBpi2CmTEKEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-BPI2-MIB", "docsBpi2CmTEKSAId"),
)
if mibBuilder.loadTexts:
    docsBpi2CmTEKEntry.setStatus("current")


class _DocsBpi2CmTEKSAId_Type(Integer32):
    """Custom type docsBpi2CmTEKSAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_DocsBpi2CmTEKSAId_Type.__name__ = "Integer32"
_DocsBpi2CmTEKSAId_Object = MibTableColumn
docsBpi2CmTEKSAId = _DocsBpi2CmTEKSAId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 1),
    _DocsBpi2CmTEKSAId_Type()
)
docsBpi2CmTEKSAId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsBpi2CmTEKSAId.setStatus("current")


class _DocsBpi2CmTEKSAType_Type(Integer32):
    """Custom type docsBpi2CmTEKSAType based on Integer32"""
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
          ("primary", 1),
          ("static", 2),
          ("dynamic", 3))
    )


_DocsBpi2CmTEKSAType_Type.__name__ = "Integer32"
_DocsBpi2CmTEKSAType_Object = MibTableColumn
docsBpi2CmTEKSAType = _DocsBpi2CmTEKSAType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 2),
    _DocsBpi2CmTEKSAType_Type()
)
docsBpi2CmTEKSAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKSAType.setStatus("current")


class _DocsBpi2CmTEKDataEncryptAlg_Type(Integer32):
    """Custom type docsBpi2CmTEKDataEncryptAlg based on Integer32"""
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
          ("des56CbcMode", 1),
          ("des40CbcMode", 2))
    )


_DocsBpi2CmTEKDataEncryptAlg_Type.__name__ = "Integer32"
_DocsBpi2CmTEKDataEncryptAlg_Object = MibTableColumn
docsBpi2CmTEKDataEncryptAlg = _DocsBpi2CmTEKDataEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 3),
    _DocsBpi2CmTEKDataEncryptAlg_Type()
)
docsBpi2CmTEKDataEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKDataEncryptAlg.setStatus("current")


class _DocsBpi2CmTEKDataAuthentAlg_Type(Integer32):
    """Custom type docsBpi2CmTEKDataAuthentAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_DocsBpi2CmTEKDataAuthentAlg_Type.__name__ = "Integer32"
_DocsBpi2CmTEKDataAuthentAlg_Object = MibTableColumn
docsBpi2CmTEKDataAuthentAlg = _DocsBpi2CmTEKDataAuthentAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 4),
    _DocsBpi2CmTEKDataAuthentAlg_Type()
)
docsBpi2CmTEKDataAuthentAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKDataAuthentAlg.setStatus("current")


class _DocsBpi2CmTEKState_Type(Integer32):
    """Custom type docsBpi2CmTEKState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("opWait", 2),
          ("opReauthWait", 3),
          ("operational", 4),
          ("rekeyWait", 5),
          ("rekeyReauthWait", 6))
    )


_DocsBpi2CmTEKState_Type.__name__ = "Integer32"
_DocsBpi2CmTEKState_Object = MibTableColumn
docsBpi2CmTEKState = _DocsBpi2CmTEKState_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 5),
    _DocsBpi2CmTEKState_Type()
)
docsBpi2CmTEKState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKState.setStatus("current")


class _DocsBpi2CmTEKKeySequenceNumber_Type(Integer32):
    """Custom type docsBpi2CmTEKKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DocsBpi2CmTEKKeySequenceNumber_Type.__name__ = "Integer32"
_DocsBpi2CmTEKKeySequenceNumber_Object = MibTableColumn
docsBpi2CmTEKKeySequenceNumber = _DocsBpi2CmTEKKeySequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 6),
    _DocsBpi2CmTEKKeySequenceNumber_Type()
)
docsBpi2CmTEKKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKKeySequenceNumber.setStatus("current")
_DocsBpi2CmTEKExpiresOld_Type = DateAndTime
_DocsBpi2CmTEKExpiresOld_Object = MibTableColumn
docsBpi2CmTEKExpiresOld = _DocsBpi2CmTEKExpiresOld_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 7),
    _DocsBpi2CmTEKExpiresOld_Type()
)
docsBpi2CmTEKExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKExpiresOld.setStatus("current")
_DocsBpi2CmTEKExpiresNew_Type = DateAndTime
_DocsBpi2CmTEKExpiresNew_Object = MibTableColumn
docsBpi2CmTEKExpiresNew = _DocsBpi2CmTEKExpiresNew_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 8),
    _DocsBpi2CmTEKExpiresNew_Type()
)
docsBpi2CmTEKExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKExpiresNew.setStatus("current")
_DocsBpi2CmTEKKeyRequests_Type = Counter32
_DocsBpi2CmTEKKeyRequests_Object = MibTableColumn
docsBpi2CmTEKKeyRequests = _DocsBpi2CmTEKKeyRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 9),
    _DocsBpi2CmTEKKeyRequests_Type()
)
docsBpi2CmTEKKeyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKKeyRequests.setStatus("current")
_DocsBpi2CmTEKKeyReplies_Type = Counter32
_DocsBpi2CmTEKKeyReplies_Object = MibTableColumn
docsBpi2CmTEKKeyReplies = _DocsBpi2CmTEKKeyReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 10),
    _DocsBpi2CmTEKKeyReplies_Type()
)
docsBpi2CmTEKKeyReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKKeyReplies.setStatus("current")
_DocsBpi2CmTEKKeyRejects_Type = Counter32
_DocsBpi2CmTEKKeyRejects_Object = MibTableColumn
docsBpi2CmTEKKeyRejects = _DocsBpi2CmTEKKeyRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 11),
    _DocsBpi2CmTEKKeyRejects_Type()
)
docsBpi2CmTEKKeyRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKKeyRejects.setStatus("current")
_DocsBpi2CmTEKInvalids_Type = Counter32
_DocsBpi2CmTEKInvalids_Object = MibTableColumn
docsBpi2CmTEKInvalids = _DocsBpi2CmTEKInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 12),
    _DocsBpi2CmTEKInvalids_Type()
)
docsBpi2CmTEKInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKInvalids.setStatus("current")
_DocsBpi2CmTEKAuthPends_Type = Counter32
_DocsBpi2CmTEKAuthPends_Object = MibTableColumn
docsBpi2CmTEKAuthPends = _DocsBpi2CmTEKAuthPends_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 13),
    _DocsBpi2CmTEKAuthPends_Type()
)
docsBpi2CmTEKAuthPends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKAuthPends.setStatus("current")


class _DocsBpi2CmTEKKeyRejectErrorCode_Type(Integer32):
    """Custom type docsBpi2CmTEKKeyRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("unauthorizedSaid", 4))
    )


_DocsBpi2CmTEKKeyRejectErrorCode_Type.__name__ = "Integer32"
_DocsBpi2CmTEKKeyRejectErrorCode_Object = MibTableColumn
docsBpi2CmTEKKeyRejectErrorCode = _DocsBpi2CmTEKKeyRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 14),
    _DocsBpi2CmTEKKeyRejectErrorCode_Type()
)
docsBpi2CmTEKKeyRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKKeyRejectErrorCode.setStatus("current")


class _DocsBpi2CmTEKKeyRejectErrorString_Type(SnmpAdminString):
    """Custom type docsBpi2CmTEKKeyRejectErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpi2CmTEKKeyRejectErrorString_Type.__name__ = "SnmpAdminString"
_DocsBpi2CmTEKKeyRejectErrorString_Object = MibTableColumn
docsBpi2CmTEKKeyRejectErrorString = _DocsBpi2CmTEKKeyRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 15),
    _DocsBpi2CmTEKKeyRejectErrorString_Type()
)
docsBpi2CmTEKKeyRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKKeyRejectErrorString.setStatus("current")


class _DocsBpi2CmTEKInvalidErrorCode_Type(Integer32):
    """Custom type docsBpi2CmTEKInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("invalidKeySequence", 6))
    )


_DocsBpi2CmTEKInvalidErrorCode_Type.__name__ = "Integer32"
_DocsBpi2CmTEKInvalidErrorCode_Object = MibTableColumn
docsBpi2CmTEKInvalidErrorCode = _DocsBpi2CmTEKInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 16),
    _DocsBpi2CmTEKInvalidErrorCode_Type()
)
docsBpi2CmTEKInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKInvalidErrorCode.setStatus("current")


class _DocsBpi2CmTEKInvalidErrorString_Type(SnmpAdminString):
    """Custom type docsBpi2CmTEKInvalidErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpi2CmTEKInvalidErrorString_Type.__name__ = "SnmpAdminString"
_DocsBpi2CmTEKInvalidErrorString_Object = MibTableColumn
docsBpi2CmTEKInvalidErrorString = _DocsBpi2CmTEKInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 2, 1, 17),
    _DocsBpi2CmTEKInvalidErrorString_Type()
)
docsBpi2CmTEKInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmTEKInvalidErrorString.setStatus("current")
_DocsBpi2CmMulticastObjects_ObjectIdentity = ObjectIdentity
docsBpi2CmMulticastObjects = _DocsBpi2CmMulticastObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 3)
)
_DocsBpi2CmIpMulticastMapTable_Object = MibTable
docsBpi2CmIpMulticastMapTable = _DocsBpi2CmIpMulticastMapTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    docsBpi2CmIpMulticastMapTable.setStatus("current")
_DocsBpi2CmIpMulticastMapEntry_Object = MibTableRow
docsBpi2CmIpMulticastMapEntry = _DocsBpi2CmIpMulticastMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 3, 1, 1)
)
docsBpi2CmIpMulticastMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-BPI2-MIB", "docsBpi2CmIpMulticastIndex"),
)
if mibBuilder.loadTexts:
    docsBpi2CmIpMulticastMapEntry.setStatus("current")


class _DocsBpi2CmIpMulticastIndex_Type(Integer32):
    """Custom type docsBpi2CmIpMulticastIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_DocsBpi2CmIpMulticastIndex_Type.__name__ = "Integer32"
_DocsBpi2CmIpMulticastIndex_Object = MibTableColumn
docsBpi2CmIpMulticastIndex = _DocsBpi2CmIpMulticastIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 3, 1, 1, 1),
    _DocsBpi2CmIpMulticastIndex_Type()
)
docsBpi2CmIpMulticastIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsBpi2CmIpMulticastIndex.setStatus("current")
_DocsBpi2CmIpMulticastAddressType_Type = InetAddressType
_DocsBpi2CmIpMulticastAddressType_Object = MibTableColumn
docsBpi2CmIpMulticastAddressType = _DocsBpi2CmIpMulticastAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 3, 1, 1, 2),
    _DocsBpi2CmIpMulticastAddressType_Type()
)
docsBpi2CmIpMulticastAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmIpMulticastAddressType.setStatus("current")
_DocsBpi2CmIpMulticastAddress_Type = InetAddress
_DocsBpi2CmIpMulticastAddress_Object = MibTableColumn
docsBpi2CmIpMulticastAddress = _DocsBpi2CmIpMulticastAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 3, 1, 1, 3),
    _DocsBpi2CmIpMulticastAddress_Type()
)
docsBpi2CmIpMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmIpMulticastAddress.setStatus("current")


class _DocsBpi2CmIpMulticastSAId_Type(Integer32):
    """Custom type docsBpi2CmIpMulticastSAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_DocsBpi2CmIpMulticastSAId_Type.__name__ = "Integer32"
_DocsBpi2CmIpMulticastSAId_Object = MibTableColumn
docsBpi2CmIpMulticastSAId = _DocsBpi2CmIpMulticastSAId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 3, 1, 1, 4),
    _DocsBpi2CmIpMulticastSAId_Type()
)
docsBpi2CmIpMulticastSAId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmIpMulticastSAId.setStatus("current")


class _DocsBpi2CmIpMulticastSAMapState_Type(Integer32):
    """Custom type docsBpi2CmIpMulticastSAMapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("mapWait", 2),
          ("mapped", 3))
    )


_DocsBpi2CmIpMulticastSAMapState_Type.__name__ = "Integer32"
_DocsBpi2CmIpMulticastSAMapState_Object = MibTableColumn
docsBpi2CmIpMulticastSAMapState = _DocsBpi2CmIpMulticastSAMapState_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 3, 1, 1, 5),
    _DocsBpi2CmIpMulticastSAMapState_Type()
)
docsBpi2CmIpMulticastSAMapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmIpMulticastSAMapState.setStatus("current")
_DocsBpi2CmIpMulticastSAMapRequests_Type = Counter32
_DocsBpi2CmIpMulticastSAMapRequests_Object = MibTableColumn
docsBpi2CmIpMulticastSAMapRequests = _DocsBpi2CmIpMulticastSAMapRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 3, 1, 1, 6),
    _DocsBpi2CmIpMulticastSAMapRequests_Type()
)
docsBpi2CmIpMulticastSAMapRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmIpMulticastSAMapRequests.setStatus("current")
_DocsBpi2CmIpMulticastSAMapReplies_Type = Counter32
_DocsBpi2CmIpMulticastSAMapReplies_Object = MibTableColumn
docsBpi2CmIpMulticastSAMapReplies = _DocsBpi2CmIpMulticastSAMapReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 3, 1, 1, 7),
    _DocsBpi2CmIpMulticastSAMapReplies_Type()
)
docsBpi2CmIpMulticastSAMapReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmIpMulticastSAMapReplies.setStatus("current")
_DocsBpi2CmIpMulticastSAMapRejects_Type = Counter32
_DocsBpi2CmIpMulticastSAMapRejects_Object = MibTableColumn
docsBpi2CmIpMulticastSAMapRejects = _DocsBpi2CmIpMulticastSAMapRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 3, 1, 1, 8),
    _DocsBpi2CmIpMulticastSAMapRejects_Type()
)
docsBpi2CmIpMulticastSAMapRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmIpMulticastSAMapRejects.setStatus("current")


class _DocsBpi2CmIpMulticastSAMapRejectErrorCode_Type(Integer32):
    """Custom type docsBpi2CmIpMulticastSAMapRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("noAuthForRequestedDSFlow", 9),
          ("dsFlowNotMappedToSA", 10))
    )


_DocsBpi2CmIpMulticastSAMapRejectErrorCode_Type.__name__ = "Integer32"
_DocsBpi2CmIpMulticastSAMapRejectErrorCode_Object = MibTableColumn
docsBpi2CmIpMulticastSAMapRejectErrorCode = _DocsBpi2CmIpMulticastSAMapRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 3, 1, 1, 9),
    _DocsBpi2CmIpMulticastSAMapRejectErrorCode_Type()
)
docsBpi2CmIpMulticastSAMapRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmIpMulticastSAMapRejectErrorCode.setStatus("current")


class _DocsBpi2CmIpMulticastSAMapRejectErrorString_Type(SnmpAdminString):
    """Custom type docsBpi2CmIpMulticastSAMapRejectErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpi2CmIpMulticastSAMapRejectErrorString_Type.__name__ = "SnmpAdminString"
_DocsBpi2CmIpMulticastSAMapRejectErrorString_Object = MibTableColumn
docsBpi2CmIpMulticastSAMapRejectErrorString = _DocsBpi2CmIpMulticastSAMapRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 3, 1, 1, 10),
    _DocsBpi2CmIpMulticastSAMapRejectErrorString_Type()
)
docsBpi2CmIpMulticastSAMapRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmIpMulticastSAMapRejectErrorString.setStatus("current")
_DocsBpi2CmCertObjects_ObjectIdentity = ObjectIdentity
docsBpi2CmCertObjects = _DocsBpi2CmCertObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 4)
)
_DocsBpi2CmDeviceCertTable_Object = MibTable
docsBpi2CmDeviceCertTable = _DocsBpi2CmDeviceCertTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    docsBpi2CmDeviceCertTable.setStatus("current")
_DocsBpi2CmDeviceCertEntry_Object = MibTableRow
docsBpi2CmDeviceCertEntry = _DocsBpi2CmDeviceCertEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 4, 1, 1)
)
docsBpi2CmDeviceCertEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsBpi2CmDeviceCertEntry.setStatus("current")
_DocsBpi2CmDeviceCmCert_Type = X509Certificate
_DocsBpi2CmDeviceCmCert_Object = MibTableColumn
docsBpi2CmDeviceCmCert = _DocsBpi2CmDeviceCmCert_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 4, 1, 1, 1),
    _DocsBpi2CmDeviceCmCert_Type()
)
docsBpi2CmDeviceCmCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpi2CmDeviceCmCert.setStatus("current")
_DocsBpi2CmDeviceManufCert_Type = X509Certificate
_DocsBpi2CmDeviceManufCert_Object = MibTableColumn
docsBpi2CmDeviceManufCert = _DocsBpi2CmDeviceManufCert_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 4, 1, 1, 2),
    _DocsBpi2CmDeviceManufCert_Type()
)
docsBpi2CmDeviceManufCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmDeviceManufCert.setStatus("current")
_DocsBpi2CmCryptoSuiteTable_Object = MibTable
docsBpi2CmCryptoSuiteTable = _DocsBpi2CmCryptoSuiteTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 5)
)
if mibBuilder.loadTexts:
    docsBpi2CmCryptoSuiteTable.setStatus("current")
_DocsBpi2CmCryptoSuiteEntry_Object = MibTableRow
docsBpi2CmCryptoSuiteEntry = _DocsBpi2CmCryptoSuiteEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 5, 1)
)
docsBpi2CmCryptoSuiteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-BPI2-MIB", "docsBpi2CmCryptoSuiteIndex"),
)
if mibBuilder.loadTexts:
    docsBpi2CmCryptoSuiteEntry.setStatus("current")


class _DocsBpi2CmCryptoSuiteIndex_Type(Integer32):
    """Custom type docsBpi2CmCryptoSuiteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_DocsBpi2CmCryptoSuiteIndex_Type.__name__ = "Integer32"
_DocsBpi2CmCryptoSuiteIndex_Object = MibTableColumn
docsBpi2CmCryptoSuiteIndex = _DocsBpi2CmCryptoSuiteIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 5, 1, 1),
    _DocsBpi2CmCryptoSuiteIndex_Type()
)
docsBpi2CmCryptoSuiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsBpi2CmCryptoSuiteIndex.setStatus("current")


class _DocsBpi2CmCryptoSuiteDataEncryptAlg_Type(Integer32):
    """Custom type docsBpi2CmCryptoSuiteDataEncryptAlg based on Integer32"""
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
          ("des56CbcMode", 1),
          ("des40CbcMode", 2))
    )


_DocsBpi2CmCryptoSuiteDataEncryptAlg_Type.__name__ = "Integer32"
_DocsBpi2CmCryptoSuiteDataEncryptAlg_Object = MibTableColumn
docsBpi2CmCryptoSuiteDataEncryptAlg = _DocsBpi2CmCryptoSuiteDataEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 5, 1, 2),
    _DocsBpi2CmCryptoSuiteDataEncryptAlg_Type()
)
docsBpi2CmCryptoSuiteDataEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmCryptoSuiteDataEncryptAlg.setStatus("current")


class _DocsBpi2CmCryptoSuiteDataAuthentAlg_Type(Integer32):
    """Custom type docsBpi2CmCryptoSuiteDataAuthentAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_DocsBpi2CmCryptoSuiteDataAuthentAlg_Type.__name__ = "Integer32"
_DocsBpi2CmCryptoSuiteDataAuthentAlg_Object = MibTableColumn
docsBpi2CmCryptoSuiteDataAuthentAlg = _DocsBpi2CmCryptoSuiteDataAuthentAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 1, 5, 1, 3),
    _DocsBpi2CmCryptoSuiteDataAuthentAlg_Type()
)
docsBpi2CmCryptoSuiteDataAuthentAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmCryptoSuiteDataAuthentAlg.setStatus("current")
_DocsBpi2CmtsObjects_ObjectIdentity = ObjectIdentity
docsBpi2CmtsObjects = _DocsBpi2CmtsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2)
)
_DocsBpi2CmtsBaseTable_Object = MibTable
docsBpi2CmtsBaseTable = _DocsBpi2CmtsBaseTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    docsBpi2CmtsBaseTable.setStatus("current")
_DocsBpi2CmtsBaseEntry_Object = MibTableRow
docsBpi2CmtsBaseEntry = _DocsBpi2CmtsBaseEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 1, 1)
)
docsBpi2CmtsBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsBpi2CmtsBaseEntry.setStatus("current")


class _DocsBpi2CmtsDefaultAuthLifetime_Type(Integer32):
    """Custom type docsBpi2CmtsDefaultAuthLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6048000),
    )


_DocsBpi2CmtsDefaultAuthLifetime_Type.__name__ = "Integer32"
_DocsBpi2CmtsDefaultAuthLifetime_Object = MibTableColumn
docsBpi2CmtsDefaultAuthLifetime = _DocsBpi2CmtsDefaultAuthLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 1, 1, 1),
    _DocsBpi2CmtsDefaultAuthLifetime_Type()
)
docsBpi2CmtsDefaultAuthLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpi2CmtsDefaultAuthLifetime.setStatus("current")
if mibBuilder.loadTexts:
    docsBpi2CmtsDefaultAuthLifetime.setUnits("seconds")


class _DocsBpi2CmtsDefaultTEKLifetime_Type(Integer32):
    """Custom type docsBpi2CmtsDefaultTEKLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_DocsBpi2CmtsDefaultTEKLifetime_Type.__name__ = "Integer32"
_DocsBpi2CmtsDefaultTEKLifetime_Object = MibTableColumn
docsBpi2CmtsDefaultTEKLifetime = _DocsBpi2CmtsDefaultTEKLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 1, 1, 2),
    _DocsBpi2CmtsDefaultTEKLifetime_Type()
)
docsBpi2CmtsDefaultTEKLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpi2CmtsDefaultTEKLifetime.setStatus("current")
if mibBuilder.loadTexts:
    docsBpi2CmtsDefaultTEKLifetime.setUnits("seconds")


class _DocsBpi2CmtsDefaultSelfSignedManufCertTrust_Type(Integer32):
    """Custom type docsBpi2CmtsDefaultSelfSignedManufCertTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_DocsBpi2CmtsDefaultSelfSignedManufCertTrust_Type.__name__ = "Integer32"
_DocsBpi2CmtsDefaultSelfSignedManufCertTrust_Object = MibTableColumn
docsBpi2CmtsDefaultSelfSignedManufCertTrust = _DocsBpi2CmtsDefaultSelfSignedManufCertTrust_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 1, 1, 3),
    _DocsBpi2CmtsDefaultSelfSignedManufCertTrust_Type()
)
docsBpi2CmtsDefaultSelfSignedManufCertTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpi2CmtsDefaultSelfSignedManufCertTrust.setStatus("current")
_DocsBpi2CmtsCheckCertValidityPeriods_Type = TruthValue
_DocsBpi2CmtsCheckCertValidityPeriods_Object = MibTableColumn
docsBpi2CmtsCheckCertValidityPeriods = _DocsBpi2CmtsCheckCertValidityPeriods_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 1, 1, 4),
    _DocsBpi2CmtsCheckCertValidityPeriods_Type()
)
docsBpi2CmtsCheckCertValidityPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpi2CmtsCheckCertValidityPeriods.setStatus("current")
_DocsBpi2CmtsAuthentInfos_Type = Counter32
_DocsBpi2CmtsAuthentInfos_Object = MibTableColumn
docsBpi2CmtsAuthentInfos = _DocsBpi2CmtsAuthentInfos_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 1, 1, 5),
    _DocsBpi2CmtsAuthentInfos_Type()
)
docsBpi2CmtsAuthentInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthentInfos.setStatus("current")
_DocsBpi2CmtsAuthRequests_Type = Counter32
_DocsBpi2CmtsAuthRequests_Object = MibTableColumn
docsBpi2CmtsAuthRequests = _DocsBpi2CmtsAuthRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 1, 1, 6),
    _DocsBpi2CmtsAuthRequests_Type()
)
docsBpi2CmtsAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthRequests.setStatus("current")
_DocsBpi2CmtsAuthReplies_Type = Counter32
_DocsBpi2CmtsAuthReplies_Object = MibTableColumn
docsBpi2CmtsAuthReplies = _DocsBpi2CmtsAuthReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 1, 1, 7),
    _DocsBpi2CmtsAuthReplies_Type()
)
docsBpi2CmtsAuthReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthReplies.setStatus("current")
_DocsBpi2CmtsAuthRejects_Type = Counter32
_DocsBpi2CmtsAuthRejects_Object = MibTableColumn
docsBpi2CmtsAuthRejects = _DocsBpi2CmtsAuthRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 1, 1, 8),
    _DocsBpi2CmtsAuthRejects_Type()
)
docsBpi2CmtsAuthRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthRejects.setStatus("current")
_DocsBpi2CmtsAuthInvalids_Type = Counter32
_DocsBpi2CmtsAuthInvalids_Object = MibTableColumn
docsBpi2CmtsAuthInvalids = _DocsBpi2CmtsAuthInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 1, 1, 9),
    _DocsBpi2CmtsAuthInvalids_Type()
)
docsBpi2CmtsAuthInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthInvalids.setStatus("current")
_DocsBpi2CmtsSAMapRequests_Type = Counter32
_DocsBpi2CmtsSAMapRequests_Object = MibTableColumn
docsBpi2CmtsSAMapRequests = _DocsBpi2CmtsSAMapRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 1, 1, 10),
    _DocsBpi2CmtsSAMapRequests_Type()
)
docsBpi2CmtsSAMapRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsSAMapRequests.setStatus("current")
_DocsBpi2CmtsSAMapReplies_Type = Counter32
_DocsBpi2CmtsSAMapReplies_Object = MibTableColumn
docsBpi2CmtsSAMapReplies = _DocsBpi2CmtsSAMapReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 1, 1, 11),
    _DocsBpi2CmtsSAMapReplies_Type()
)
docsBpi2CmtsSAMapReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsSAMapReplies.setStatus("current")
_DocsBpi2CmtsSAMapRejects_Type = Counter32
_DocsBpi2CmtsSAMapRejects_Object = MibTableColumn
docsBpi2CmtsSAMapRejects = _DocsBpi2CmtsSAMapRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 1, 1, 12),
    _DocsBpi2CmtsSAMapRejects_Type()
)
docsBpi2CmtsSAMapRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsSAMapRejects.setStatus("current")
_DocsBpi2CmtsAuthTable_Object = MibTable
docsBpi2CmtsAuthTable = _DocsBpi2CmtsAuthTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthTable.setStatus("current")
_DocsBpi2CmtsAuthEntry_Object = MibTableRow
docsBpi2CmtsAuthEntry = _DocsBpi2CmtsAuthEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1)
)
docsBpi2CmtsAuthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-BPI2-MIB", "docsBpi2CmtsAuthCmMacAddress"),
)
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthEntry.setStatus("current")
_DocsBpi2CmtsAuthCmMacAddress_Type = MacAddress
_DocsBpi2CmtsAuthCmMacAddress_Object = MibTableColumn
docsBpi2CmtsAuthCmMacAddress = _DocsBpi2CmtsAuthCmMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 1),
    _DocsBpi2CmtsAuthCmMacAddress_Type()
)
docsBpi2CmtsAuthCmMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmMacAddress.setStatus("current")


class _DocsBpi2CmtsAuthCmBpiVersion_Type(Integer32):
    """Custom type docsBpi2CmtsAuthCmBpiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bpi", 0),
          ("bpiPlus", 1))
    )


_DocsBpi2CmtsAuthCmBpiVersion_Type.__name__ = "Integer32"
_DocsBpi2CmtsAuthCmBpiVersion_Object = MibTableColumn
docsBpi2CmtsAuthCmBpiVersion = _DocsBpi2CmtsAuthCmBpiVersion_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 2),
    _DocsBpi2CmtsAuthCmBpiVersion_Type()
)
docsBpi2CmtsAuthCmBpiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmBpiVersion.setStatus("current")


class _DocsBpi2CmtsAuthCmPublicKey_Type(OctetString):
    """Custom type docsBpi2CmtsAuthCmPublicKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(74, 74),
        ValueSizeConstraint(106, 106),
        ValueSizeConstraint(140, 140),
        ValueSizeConstraint(204, 204),
        ValueSizeConstraint(270, 270),
    )


_DocsBpi2CmtsAuthCmPublicKey_Type.__name__ = "OctetString"
_DocsBpi2CmtsAuthCmPublicKey_Object = MibTableColumn
docsBpi2CmtsAuthCmPublicKey = _DocsBpi2CmtsAuthCmPublicKey_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 3),
    _DocsBpi2CmtsAuthCmPublicKey_Type()
)
docsBpi2CmtsAuthCmPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmPublicKey.setStatus("current")


class _DocsBpi2CmtsAuthCmKeySequenceNumber_Type(Integer32):
    """Custom type docsBpi2CmtsAuthCmKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DocsBpi2CmtsAuthCmKeySequenceNumber_Type.__name__ = "Integer32"
_DocsBpi2CmtsAuthCmKeySequenceNumber_Object = MibTableColumn
docsBpi2CmtsAuthCmKeySequenceNumber = _DocsBpi2CmtsAuthCmKeySequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 4),
    _DocsBpi2CmtsAuthCmKeySequenceNumber_Type()
)
docsBpi2CmtsAuthCmKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmKeySequenceNumber.setStatus("current")
_DocsBpi2CmtsAuthCmExpiresOld_Type = DateAndTime
_DocsBpi2CmtsAuthCmExpiresOld_Object = MibTableColumn
docsBpi2CmtsAuthCmExpiresOld = _DocsBpi2CmtsAuthCmExpiresOld_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 5),
    _DocsBpi2CmtsAuthCmExpiresOld_Type()
)
docsBpi2CmtsAuthCmExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmExpiresOld.setStatus("current")
_DocsBpi2CmtsAuthCmExpiresNew_Type = DateAndTime
_DocsBpi2CmtsAuthCmExpiresNew_Object = MibTableColumn
docsBpi2CmtsAuthCmExpiresNew = _DocsBpi2CmtsAuthCmExpiresNew_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 6),
    _DocsBpi2CmtsAuthCmExpiresNew_Type()
)
docsBpi2CmtsAuthCmExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmExpiresNew.setStatus("current")


class _DocsBpi2CmtsAuthCmLifetime_Type(Integer32):
    """Custom type docsBpi2CmtsAuthCmLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6048000),
    )


_DocsBpi2CmtsAuthCmLifetime_Type.__name__ = "Integer32"
_DocsBpi2CmtsAuthCmLifetime_Object = MibTableColumn
docsBpi2CmtsAuthCmLifetime = _DocsBpi2CmtsAuthCmLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 7),
    _DocsBpi2CmtsAuthCmLifetime_Type()
)
docsBpi2CmtsAuthCmLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmLifetime.setStatus("current")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmLifetime.setUnits("seconds")


class _DocsBpi2CmtsAuthCmGraceTime_Type(Integer32):
    """Custom type docsBpi2CmtsAuthCmGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6047999),
    )


_DocsBpi2CmtsAuthCmGraceTime_Type.__name__ = "Integer32"
_DocsBpi2CmtsAuthCmGraceTime_Object = MibTableColumn
docsBpi2CmtsAuthCmGraceTime = _DocsBpi2CmtsAuthCmGraceTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 8),
    _DocsBpi2CmtsAuthCmGraceTime_Type()
)
docsBpi2CmtsAuthCmGraceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmGraceTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmGraceTime.setUnits("seconds")


class _DocsBpi2CmtsAuthCmReset_Type(Integer32):
    """Custom type docsBpi2CmtsAuthCmReset based on Integer32"""
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
        *(("noResetRequested", 1),
          ("invalidateAuth", 2),
          ("sendAuthInvalid", 3),
          ("invalidateTeks", 4))
    )


_DocsBpi2CmtsAuthCmReset_Type.__name__ = "Integer32"
_DocsBpi2CmtsAuthCmReset_Object = MibTableColumn
docsBpi2CmtsAuthCmReset = _DocsBpi2CmtsAuthCmReset_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 9),
    _DocsBpi2CmtsAuthCmReset_Type()
)
docsBpi2CmtsAuthCmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmReset.setStatus("current")
_DocsBpi2CmtsAuthCmInfos_Type = Counter32
_DocsBpi2CmtsAuthCmInfos_Object = MibTableColumn
docsBpi2CmtsAuthCmInfos = _DocsBpi2CmtsAuthCmInfos_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 10),
    _DocsBpi2CmtsAuthCmInfos_Type()
)
docsBpi2CmtsAuthCmInfos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmInfos.setStatus("current")
_DocsBpi2CmtsAuthCmRequests_Type = Counter32
_DocsBpi2CmtsAuthCmRequests_Object = MibTableColumn
docsBpi2CmtsAuthCmRequests = _DocsBpi2CmtsAuthCmRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 11),
    _DocsBpi2CmtsAuthCmRequests_Type()
)
docsBpi2CmtsAuthCmRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmRequests.setStatus("current")
_DocsBpi2CmtsAuthCmReplies_Type = Counter32
_DocsBpi2CmtsAuthCmReplies_Object = MibTableColumn
docsBpi2CmtsAuthCmReplies = _DocsBpi2CmtsAuthCmReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 12),
    _DocsBpi2CmtsAuthCmReplies_Type()
)
docsBpi2CmtsAuthCmReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmReplies.setStatus("current")
_DocsBpi2CmtsAuthCmRejects_Type = Counter32
_DocsBpi2CmtsAuthCmRejects_Object = MibTableColumn
docsBpi2CmtsAuthCmRejects = _DocsBpi2CmtsAuthCmRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 13),
    _DocsBpi2CmtsAuthCmRejects_Type()
)
docsBpi2CmtsAuthCmRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmRejects.setStatus("current")
_DocsBpi2CmtsAuthCmInvalids_Type = Counter32
_DocsBpi2CmtsAuthCmInvalids_Object = MibTableColumn
docsBpi2CmtsAuthCmInvalids = _DocsBpi2CmtsAuthCmInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 14),
    _DocsBpi2CmtsAuthCmInvalids_Type()
)
docsBpi2CmtsAuthCmInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthCmInvalids.setStatus("current")


class _DocsBpi2CmtsAuthRejectErrorCode_Type(Integer32):
    """Custom type docsBpi2CmtsAuthRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              11)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("unauthorizedCm", 3),
          ("unauthorizedSaid", 4),
          ("permanentAuthorizationFailure", 8),
          ("timeOfDayNotAcquired", 11))
    )


_DocsBpi2CmtsAuthRejectErrorCode_Type.__name__ = "Integer32"
_DocsBpi2CmtsAuthRejectErrorCode_Object = MibTableColumn
docsBpi2CmtsAuthRejectErrorCode = _DocsBpi2CmtsAuthRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 15),
    _DocsBpi2CmtsAuthRejectErrorCode_Type()
)
docsBpi2CmtsAuthRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthRejectErrorCode.setStatus("current")


class _DocsBpi2CmtsAuthRejectErrorString_Type(SnmpAdminString):
    """Custom type docsBpi2CmtsAuthRejectErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpi2CmtsAuthRejectErrorString_Type.__name__ = "SnmpAdminString"
_DocsBpi2CmtsAuthRejectErrorString_Object = MibTableColumn
docsBpi2CmtsAuthRejectErrorString = _DocsBpi2CmtsAuthRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 16),
    _DocsBpi2CmtsAuthRejectErrorString_Type()
)
docsBpi2CmtsAuthRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthRejectErrorString.setStatus("current")


class _DocsBpi2CmtsAuthInvalidErrorCode_Type(Integer32):
    """Custom type docsBpi2CmtsAuthInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("unauthorizedCm", 3),
          ("unsolicited", 5),
          ("invalidKeySequence", 6),
          ("keyRequestAuthenticationFailure", 7))
    )


_DocsBpi2CmtsAuthInvalidErrorCode_Type.__name__ = "Integer32"
_DocsBpi2CmtsAuthInvalidErrorCode_Object = MibTableColumn
docsBpi2CmtsAuthInvalidErrorCode = _DocsBpi2CmtsAuthInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 17),
    _DocsBpi2CmtsAuthInvalidErrorCode_Type()
)
docsBpi2CmtsAuthInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthInvalidErrorCode.setStatus("current")


class _DocsBpi2CmtsAuthInvalidErrorString_Type(SnmpAdminString):
    """Custom type docsBpi2CmtsAuthInvalidErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpi2CmtsAuthInvalidErrorString_Type.__name__ = "SnmpAdminString"
_DocsBpi2CmtsAuthInvalidErrorString_Object = MibTableColumn
docsBpi2CmtsAuthInvalidErrorString = _DocsBpi2CmtsAuthInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 18),
    _DocsBpi2CmtsAuthInvalidErrorString_Type()
)
docsBpi2CmtsAuthInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthInvalidErrorString.setStatus("current")


class _DocsBpi2CmtsAuthPrimarySAId_Type(Integer32):
    """Custom type docsBpi2CmtsAuthPrimarySAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_DocsBpi2CmtsAuthPrimarySAId_Type.__name__ = "Integer32"
_DocsBpi2CmtsAuthPrimarySAId_Object = MibTableColumn
docsBpi2CmtsAuthPrimarySAId = _DocsBpi2CmtsAuthPrimarySAId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 19),
    _DocsBpi2CmtsAuthPrimarySAId_Type()
)
docsBpi2CmtsAuthPrimarySAId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthPrimarySAId.setStatus("current")


class _DocsBpi2CmtsAuthBpkmCmCertValid_Type(Integer32):
    """Custom type docsBpi2CmtsAuthBpkmCmCertValid based on Integer32"""
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
        *(("unknown", 0),
          ("validCmChained", 1),
          ("validCmTrusted", 2),
          ("invalidCmUntrusted", 3),
          ("invalidCAUntrusted", 4),
          ("invalidCmOther", 5),
          ("invalidCAOther", 6))
    )


_DocsBpi2CmtsAuthBpkmCmCertValid_Type.__name__ = "Integer32"
_DocsBpi2CmtsAuthBpkmCmCertValid_Object = MibTableColumn
docsBpi2CmtsAuthBpkmCmCertValid = _DocsBpi2CmtsAuthBpkmCmCertValid_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 20),
    _DocsBpi2CmtsAuthBpkmCmCertValid_Type()
)
docsBpi2CmtsAuthBpkmCmCertValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthBpkmCmCertValid.setStatus("current")
_DocsBpi2CmtsAuthBpkmCmCert_Type = X509Certificate
_DocsBpi2CmtsAuthBpkmCmCert_Object = MibTableColumn
docsBpi2CmtsAuthBpkmCmCert = _DocsBpi2CmtsAuthBpkmCmCert_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 2, 1, 21),
    _DocsBpi2CmtsAuthBpkmCmCert_Type()
)
docsBpi2CmtsAuthBpkmCmCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsAuthBpkmCmCert.setStatus("current")
_DocsBpi2CmtsTEKTable_Object = MibTable
docsBpi2CmtsTEKTable = _DocsBpi2CmtsTEKTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3)
)
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKTable.setStatus("current")
_DocsBpi2CmtsTEKEntry_Object = MibTableRow
docsBpi2CmtsTEKEntry = _DocsBpi2CmtsTEKEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1)
)
docsBpi2CmtsTEKEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-BPI2-MIB", "docsBpi2CmtsTEKSAId"),
)
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKEntry.setStatus("current")


class _DocsBpi2CmtsTEKSAId_Type(Integer32):
    """Custom type docsBpi2CmtsTEKSAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_DocsBpi2CmtsTEKSAId_Type.__name__ = "Integer32"
_DocsBpi2CmtsTEKSAId_Object = MibTableColumn
docsBpi2CmtsTEKSAId = _DocsBpi2CmtsTEKSAId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 1),
    _DocsBpi2CmtsTEKSAId_Type()
)
docsBpi2CmtsTEKSAId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKSAId.setStatus("current")


class _DocsBpi2CmtsTEKSAType_Type(Integer32):
    """Custom type docsBpi2CmtsTEKSAType based on Integer32"""
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
          ("primary", 1),
          ("static", 2),
          ("dynamic", 3))
    )


_DocsBpi2CmtsTEKSAType_Type.__name__ = "Integer32"
_DocsBpi2CmtsTEKSAType_Object = MibTableColumn
docsBpi2CmtsTEKSAType = _DocsBpi2CmtsTEKSAType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 2),
    _DocsBpi2CmtsTEKSAType_Type()
)
docsBpi2CmtsTEKSAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKSAType.setStatus("current")


class _DocsBpi2CmtsTEKDataEncryptAlg_Type(Integer32):
    """Custom type docsBpi2CmtsTEKDataEncryptAlg based on Integer32"""
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
          ("des56CbcMode", 1),
          ("des40CbcMode", 2))
    )


_DocsBpi2CmtsTEKDataEncryptAlg_Type.__name__ = "Integer32"
_DocsBpi2CmtsTEKDataEncryptAlg_Object = MibTableColumn
docsBpi2CmtsTEKDataEncryptAlg = _DocsBpi2CmtsTEKDataEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 3),
    _DocsBpi2CmtsTEKDataEncryptAlg_Type()
)
docsBpi2CmtsTEKDataEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKDataEncryptAlg.setStatus("current")


class _DocsBpi2CmtsTEKDataAuthentAlg_Type(Integer32):
    """Custom type docsBpi2CmtsTEKDataAuthentAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_DocsBpi2CmtsTEKDataAuthentAlg_Type.__name__ = "Integer32"
_DocsBpi2CmtsTEKDataAuthentAlg_Object = MibTableColumn
docsBpi2CmtsTEKDataAuthentAlg = _DocsBpi2CmtsTEKDataAuthentAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 4),
    _DocsBpi2CmtsTEKDataAuthentAlg_Type()
)
docsBpi2CmtsTEKDataAuthentAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKDataAuthentAlg.setStatus("current")


class _DocsBpi2CmtsTEKLifetime_Type(Integer32):
    """Custom type docsBpi2CmtsTEKLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_DocsBpi2CmtsTEKLifetime_Type.__name__ = "Integer32"
_DocsBpi2CmtsTEKLifetime_Object = MibTableColumn
docsBpi2CmtsTEKLifetime = _DocsBpi2CmtsTEKLifetime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 5),
    _DocsBpi2CmtsTEKLifetime_Type()
)
docsBpi2CmtsTEKLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKLifetime.setStatus("current")
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKLifetime.setUnits("seconds")


class _DocsBpi2CmtsTEKGraceTime_Type(Integer32):
    """Custom type docsBpi2CmtsTEKGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 302399),
    )


_DocsBpi2CmtsTEKGraceTime_Type.__name__ = "Integer32"
_DocsBpi2CmtsTEKGraceTime_Object = MibTableColumn
docsBpi2CmtsTEKGraceTime = _DocsBpi2CmtsTEKGraceTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 6),
    _DocsBpi2CmtsTEKGraceTime_Type()
)
docsBpi2CmtsTEKGraceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKGraceTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKGraceTime.setUnits("seconds")


class _DocsBpi2CmtsTEKKeySequenceNumber_Type(Integer32):
    """Custom type docsBpi2CmtsTEKKeySequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DocsBpi2CmtsTEKKeySequenceNumber_Type.__name__ = "Integer32"
_DocsBpi2CmtsTEKKeySequenceNumber_Object = MibTableColumn
docsBpi2CmtsTEKKeySequenceNumber = _DocsBpi2CmtsTEKKeySequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 7),
    _DocsBpi2CmtsTEKKeySequenceNumber_Type()
)
docsBpi2CmtsTEKKeySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKKeySequenceNumber.setStatus("current")
_DocsBpi2CmtsTEKExpiresOld_Type = DateAndTime
_DocsBpi2CmtsTEKExpiresOld_Object = MibTableColumn
docsBpi2CmtsTEKExpiresOld = _DocsBpi2CmtsTEKExpiresOld_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 8),
    _DocsBpi2CmtsTEKExpiresOld_Type()
)
docsBpi2CmtsTEKExpiresOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKExpiresOld.setStatus("current")
_DocsBpi2CmtsTEKExpiresNew_Type = DateAndTime
_DocsBpi2CmtsTEKExpiresNew_Object = MibTableColumn
docsBpi2CmtsTEKExpiresNew = _DocsBpi2CmtsTEKExpiresNew_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 9),
    _DocsBpi2CmtsTEKExpiresNew_Type()
)
docsBpi2CmtsTEKExpiresNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKExpiresNew.setStatus("current")
_DocsBpi2CmtsTEKReset_Type = TruthValue
_DocsBpi2CmtsTEKReset_Object = MibTableColumn
docsBpi2CmtsTEKReset = _DocsBpi2CmtsTEKReset_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 10),
    _DocsBpi2CmtsTEKReset_Type()
)
docsBpi2CmtsTEKReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKReset.setStatus("current")
_DocsBpi2CmtsKeyRequests_Type = Counter32
_DocsBpi2CmtsKeyRequests_Object = MibTableColumn
docsBpi2CmtsKeyRequests = _DocsBpi2CmtsKeyRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 11),
    _DocsBpi2CmtsKeyRequests_Type()
)
docsBpi2CmtsKeyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsKeyRequests.setStatus("current")
_DocsBpi2CmtsKeyReplies_Type = Counter32
_DocsBpi2CmtsKeyReplies_Object = MibTableColumn
docsBpi2CmtsKeyReplies = _DocsBpi2CmtsKeyReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 12),
    _DocsBpi2CmtsKeyReplies_Type()
)
docsBpi2CmtsKeyReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsKeyReplies.setStatus("current")
_DocsBpi2CmtsKeyRejects_Type = Counter32
_DocsBpi2CmtsKeyRejects_Object = MibTableColumn
docsBpi2CmtsKeyRejects = _DocsBpi2CmtsKeyRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 13),
    _DocsBpi2CmtsKeyRejects_Type()
)
docsBpi2CmtsKeyRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsKeyRejects.setStatus("current")
_DocsBpi2CmtsTEKInvalids_Type = Counter32
_DocsBpi2CmtsTEKInvalids_Object = MibTableColumn
docsBpi2CmtsTEKInvalids = _DocsBpi2CmtsTEKInvalids_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 14),
    _DocsBpi2CmtsTEKInvalids_Type()
)
docsBpi2CmtsTEKInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKInvalids.setStatus("current")


class _DocsBpi2CmtsKeyRejectErrorCode_Type(Integer32):
    """Custom type docsBpi2CmtsKeyRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("unauthorizedSaid", 4))
    )


_DocsBpi2CmtsKeyRejectErrorCode_Type.__name__ = "Integer32"
_DocsBpi2CmtsKeyRejectErrorCode_Object = MibTableColumn
docsBpi2CmtsKeyRejectErrorCode = _DocsBpi2CmtsKeyRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 15),
    _DocsBpi2CmtsKeyRejectErrorCode_Type()
)
docsBpi2CmtsKeyRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsKeyRejectErrorCode.setStatus("current")


class _DocsBpi2CmtsKeyRejectErrorString_Type(SnmpAdminString):
    """Custom type docsBpi2CmtsKeyRejectErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpi2CmtsKeyRejectErrorString_Type.__name__ = "SnmpAdminString"
_DocsBpi2CmtsKeyRejectErrorString_Object = MibTableColumn
docsBpi2CmtsKeyRejectErrorString = _DocsBpi2CmtsKeyRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 16),
    _DocsBpi2CmtsKeyRejectErrorString_Type()
)
docsBpi2CmtsKeyRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsKeyRejectErrorString.setStatus("current")


class _DocsBpi2CmtsTEKInvalidErrorCode_Type(Integer32):
    """Custom type docsBpi2CmtsTEKInvalidErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("invalidKeySequence", 6))
    )


_DocsBpi2CmtsTEKInvalidErrorCode_Type.__name__ = "Integer32"
_DocsBpi2CmtsTEKInvalidErrorCode_Object = MibTableColumn
docsBpi2CmtsTEKInvalidErrorCode = _DocsBpi2CmtsTEKInvalidErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 17),
    _DocsBpi2CmtsTEKInvalidErrorCode_Type()
)
docsBpi2CmtsTEKInvalidErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKInvalidErrorCode.setStatus("current")


class _DocsBpi2CmtsTEKInvalidErrorString_Type(SnmpAdminString):
    """Custom type docsBpi2CmtsTEKInvalidErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpi2CmtsTEKInvalidErrorString_Type.__name__ = "SnmpAdminString"
_DocsBpi2CmtsTEKInvalidErrorString_Object = MibTableColumn
docsBpi2CmtsTEKInvalidErrorString = _DocsBpi2CmtsTEKInvalidErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 3, 1, 18),
    _DocsBpi2CmtsTEKInvalidErrorString_Type()
)
docsBpi2CmtsTEKInvalidErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsTEKInvalidErrorString.setStatus("current")
_DocsBpi2CmtsMulticastObjects_ObjectIdentity = ObjectIdentity
docsBpi2CmtsMulticastObjects = _DocsBpi2CmtsMulticastObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4)
)
_DocsBpi2CmtsIpMulticastMapTable_Object = MibTable
docsBpi2CmtsIpMulticastMapTable = _DocsBpi2CmtsIpMulticastMapTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastMapTable.setStatus("current")
_DocsBpi2CmtsIpMulticastMapEntry_Object = MibTableRow
docsBpi2CmtsIpMulticastMapEntry = _DocsBpi2CmtsIpMulticastMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1)
)
docsBpi2CmtsIpMulticastMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-BPI2-MIB", "docsBpi2CmtsIpMulticastIndex"),
)
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastMapEntry.setStatus("current")


class _DocsBpi2CmtsIpMulticastIndex_Type(Integer32):
    """Custom type docsBpi2CmtsIpMulticastIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_DocsBpi2CmtsIpMulticastIndex_Type.__name__ = "Integer32"
_DocsBpi2CmtsIpMulticastIndex_Object = MibTableColumn
docsBpi2CmtsIpMulticastIndex = _DocsBpi2CmtsIpMulticastIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1, 1),
    _DocsBpi2CmtsIpMulticastIndex_Type()
)
docsBpi2CmtsIpMulticastIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastIndex.setStatus("current")


class _DocsBpi2CmtsIpMulticastAddressType_Type(InetAddressType):
    """Custom type docsBpi2CmtsIpMulticastAddressType based on InetAddressType"""
    defaultValue = 1


_DocsBpi2CmtsIpMulticastAddressType_Type.__name__ = "InetAddressType"
_DocsBpi2CmtsIpMulticastAddressType_Object = MibTableColumn
docsBpi2CmtsIpMulticastAddressType = _DocsBpi2CmtsIpMulticastAddressType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1, 2),
    _DocsBpi2CmtsIpMulticastAddressType_Type()
)
docsBpi2CmtsIpMulticastAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastAddressType.setStatus("current")
_DocsBpi2CmtsIpMulticastAddress_Type = InetAddress
_DocsBpi2CmtsIpMulticastAddress_Object = MibTableColumn
docsBpi2CmtsIpMulticastAddress = _DocsBpi2CmtsIpMulticastAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1, 3),
    _DocsBpi2CmtsIpMulticastAddress_Type()
)
docsBpi2CmtsIpMulticastAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastAddress.setStatus("current")


class _DocsBpi2CmtsIpMulticastMaskType_Type(InetAddressType):
    """Custom type docsBpi2CmtsIpMulticastMaskType based on InetAddressType"""
    defaultValue = 1


_DocsBpi2CmtsIpMulticastMaskType_Type.__name__ = "InetAddressType"
_DocsBpi2CmtsIpMulticastMaskType_Object = MibTableColumn
docsBpi2CmtsIpMulticastMaskType = _DocsBpi2CmtsIpMulticastMaskType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1, 4),
    _DocsBpi2CmtsIpMulticastMaskType_Type()
)
docsBpi2CmtsIpMulticastMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastMaskType.setStatus("current")
_DocsBpi2CmtsIpMulticastMask_Type = InetAddress
_DocsBpi2CmtsIpMulticastMask_Object = MibTableColumn
docsBpi2CmtsIpMulticastMask = _DocsBpi2CmtsIpMulticastMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1, 5),
    _DocsBpi2CmtsIpMulticastMask_Type()
)
docsBpi2CmtsIpMulticastMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastMask.setStatus("current")


class _DocsBpi2CmtsIpMulticastSAId_Type(Integer32):
    """Custom type docsBpi2CmtsIpMulticastSAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_DocsBpi2CmtsIpMulticastSAId_Type.__name__ = "Integer32"
_DocsBpi2CmtsIpMulticastSAId_Object = MibTableColumn
docsBpi2CmtsIpMulticastSAId = _DocsBpi2CmtsIpMulticastSAId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1, 6),
    _DocsBpi2CmtsIpMulticastSAId_Type()
)
docsBpi2CmtsIpMulticastSAId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastSAId.setStatus("current")


class _DocsBpi2CmtsIpMulticastSAType_Type(Integer32):
    """Custom type docsBpi2CmtsIpMulticastSAType based on Integer32"""
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
          ("primary", 1),
          ("static", 2),
          ("dynamic", 3))
    )


_DocsBpi2CmtsIpMulticastSAType_Type.__name__ = "Integer32"
_DocsBpi2CmtsIpMulticastSAType_Object = MibTableColumn
docsBpi2CmtsIpMulticastSAType = _DocsBpi2CmtsIpMulticastSAType_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1, 7),
    _DocsBpi2CmtsIpMulticastSAType_Type()
)
docsBpi2CmtsIpMulticastSAType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastSAType.setStatus("current")


class _DocsBpi2CmtsIpMulticastDataEncryptAlg_Type(Integer32):
    """Custom type docsBpi2CmtsIpMulticastDataEncryptAlg based on Integer32"""
    defaultValue = 1

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
          ("des56CbcMode", 1),
          ("des40CbcMode", 2))
    )


_DocsBpi2CmtsIpMulticastDataEncryptAlg_Type.__name__ = "Integer32"
_DocsBpi2CmtsIpMulticastDataEncryptAlg_Object = MibTableColumn
docsBpi2CmtsIpMulticastDataEncryptAlg = _DocsBpi2CmtsIpMulticastDataEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1, 8),
    _DocsBpi2CmtsIpMulticastDataEncryptAlg_Type()
)
docsBpi2CmtsIpMulticastDataEncryptAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastDataEncryptAlg.setStatus("current")


class _DocsBpi2CmtsIpMulticastDataAuthentAlg_Type(Integer32):
    """Custom type docsBpi2CmtsIpMulticastDataAuthentAlg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_DocsBpi2CmtsIpMulticastDataAuthentAlg_Type.__name__ = "Integer32"
_DocsBpi2CmtsIpMulticastDataAuthentAlg_Object = MibTableColumn
docsBpi2CmtsIpMulticastDataAuthentAlg = _DocsBpi2CmtsIpMulticastDataAuthentAlg_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1, 9),
    _DocsBpi2CmtsIpMulticastDataAuthentAlg_Type()
)
docsBpi2CmtsIpMulticastDataAuthentAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastDataAuthentAlg.setStatus("current")
_DocsBpi2CmtsIpMulticastSAMapRequests_Type = Counter32
_DocsBpi2CmtsIpMulticastSAMapRequests_Object = MibTableColumn
docsBpi2CmtsIpMulticastSAMapRequests = _DocsBpi2CmtsIpMulticastSAMapRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1, 10),
    _DocsBpi2CmtsIpMulticastSAMapRequests_Type()
)
docsBpi2CmtsIpMulticastSAMapRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastSAMapRequests.setStatus("current")
_DocsBpi2CmtsIpMulticastSAMapReplies_Type = Counter32
_DocsBpi2CmtsIpMulticastSAMapReplies_Object = MibTableColumn
docsBpi2CmtsIpMulticastSAMapReplies = _DocsBpi2CmtsIpMulticastSAMapReplies_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1, 11),
    _DocsBpi2CmtsIpMulticastSAMapReplies_Type()
)
docsBpi2CmtsIpMulticastSAMapReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastSAMapReplies.setStatus("current")
_DocsBpi2CmtsIpMulticastSAMapRejects_Type = Counter32
_DocsBpi2CmtsIpMulticastSAMapRejects_Object = MibTableColumn
docsBpi2CmtsIpMulticastSAMapRejects = _DocsBpi2CmtsIpMulticastSAMapRejects_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1, 12),
    _DocsBpi2CmtsIpMulticastSAMapRejects_Type()
)
docsBpi2CmtsIpMulticastSAMapRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastSAMapRejects.setStatus("current")


class _DocsBpi2CmtsIpMulticastSAMapRejectErrorCode_Type(Integer32):
    """Custom type docsBpi2CmtsIpMulticastSAMapRejectErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unknown", 2),
          ("noAuthForRequestedDSFlow", 9),
          ("dsFlowNotMappedToSA", 10))
    )


_DocsBpi2CmtsIpMulticastSAMapRejectErrorCode_Type.__name__ = "Integer32"
_DocsBpi2CmtsIpMulticastSAMapRejectErrorCode_Object = MibTableColumn
docsBpi2CmtsIpMulticastSAMapRejectErrorCode = _DocsBpi2CmtsIpMulticastSAMapRejectErrorCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1, 13),
    _DocsBpi2CmtsIpMulticastSAMapRejectErrorCode_Type()
)
docsBpi2CmtsIpMulticastSAMapRejectErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastSAMapRejectErrorCode.setStatus("current")


class _DocsBpi2CmtsIpMulticastSAMapRejectErrorString_Type(SnmpAdminString):
    """Custom type docsBpi2CmtsIpMulticastSAMapRejectErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DocsBpi2CmtsIpMulticastSAMapRejectErrorString_Type.__name__ = "SnmpAdminString"
_DocsBpi2CmtsIpMulticastSAMapRejectErrorString_Object = MibTableColumn
docsBpi2CmtsIpMulticastSAMapRejectErrorString = _DocsBpi2CmtsIpMulticastSAMapRejectErrorString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1, 14),
    _DocsBpi2CmtsIpMulticastSAMapRejectErrorString_Type()
)
docsBpi2CmtsIpMulticastSAMapRejectErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastSAMapRejectErrorString.setStatus("current")
_DocsBpi2CmtsIpMulticastMapControl_Type = RowStatus
_DocsBpi2CmtsIpMulticastMapControl_Object = MibTableColumn
docsBpi2CmtsIpMulticastMapControl = _DocsBpi2CmtsIpMulticastMapControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 1, 1, 15),
    _DocsBpi2CmtsIpMulticastMapControl_Type()
)
docsBpi2CmtsIpMulticastMapControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsIpMulticastMapControl.setStatus("current")
_DocsBpi2CmtsMulticastAuthTable_Object = MibTable
docsBpi2CmtsMulticastAuthTable = _DocsBpi2CmtsMulticastAuthTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    docsBpi2CmtsMulticastAuthTable.setStatus("current")
_DocsBpi2CmtsMulticastAuthEntry_Object = MibTableRow
docsBpi2CmtsMulticastAuthEntry = _DocsBpi2CmtsMulticastAuthEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 2, 1)
)
docsBpi2CmtsMulticastAuthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-BPI2-MIB", "docsBpi2CmtsMulticastAuthSAId"),
    (0, "DOCS-BPI2-MIB", "docsBpi2CmtsMulticastAuthCmMacAddress"),
)
if mibBuilder.loadTexts:
    docsBpi2CmtsMulticastAuthEntry.setStatus("current")


class _DocsBpi2CmtsMulticastAuthSAId_Type(Integer32):
    """Custom type docsBpi2CmtsMulticastAuthSAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_DocsBpi2CmtsMulticastAuthSAId_Type.__name__ = "Integer32"
_DocsBpi2CmtsMulticastAuthSAId_Object = MibTableColumn
docsBpi2CmtsMulticastAuthSAId = _DocsBpi2CmtsMulticastAuthSAId_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 2, 1, 1),
    _DocsBpi2CmtsMulticastAuthSAId_Type()
)
docsBpi2CmtsMulticastAuthSAId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsBpi2CmtsMulticastAuthSAId.setStatus("current")
_DocsBpi2CmtsMulticastAuthCmMacAddress_Type = MacAddress
_DocsBpi2CmtsMulticastAuthCmMacAddress_Object = MibTableColumn
docsBpi2CmtsMulticastAuthCmMacAddress = _DocsBpi2CmtsMulticastAuthCmMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 2, 1, 2),
    _DocsBpi2CmtsMulticastAuthCmMacAddress_Type()
)
docsBpi2CmtsMulticastAuthCmMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsBpi2CmtsMulticastAuthCmMacAddress.setStatus("current")
_DocsBpi2CmtsMulticastAuthControl_Type = RowStatus
_DocsBpi2CmtsMulticastAuthControl_Object = MibTableColumn
docsBpi2CmtsMulticastAuthControl = _DocsBpi2CmtsMulticastAuthControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 4, 2, 1, 3),
    _DocsBpi2CmtsMulticastAuthControl_Type()
)
docsBpi2CmtsMulticastAuthControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsMulticastAuthControl.setStatus("current")
_DocsBpi2CmtsCertObjects_ObjectIdentity = ObjectIdentity
docsBpi2CmtsCertObjects = _DocsBpi2CmtsCertObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5)
)
_DocsBpi2CmtsProvisionedCmCertTable_Object = MibTable
docsBpi2CmtsProvisionedCmCertTable = _DocsBpi2CmtsProvisionedCmCertTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    docsBpi2CmtsProvisionedCmCertTable.setStatus("current")
_DocsBpi2CmtsProvisionedCmCertEntry_Object = MibTableRow
docsBpi2CmtsProvisionedCmCertEntry = _DocsBpi2CmtsProvisionedCmCertEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 1, 1)
)
docsBpi2CmtsProvisionedCmCertEntry.setIndexNames(
    (0, "DOCS-BPI2-MIB", "docsBpi2CmtsProvisionedCmCertMacAddress"),
)
if mibBuilder.loadTexts:
    docsBpi2CmtsProvisionedCmCertEntry.setStatus("current")
_DocsBpi2CmtsProvisionedCmCertMacAddress_Type = MacAddress
_DocsBpi2CmtsProvisionedCmCertMacAddress_Object = MibTableColumn
docsBpi2CmtsProvisionedCmCertMacAddress = _DocsBpi2CmtsProvisionedCmCertMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 1, 1, 1),
    _DocsBpi2CmtsProvisionedCmCertMacAddress_Type()
)
docsBpi2CmtsProvisionedCmCertMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsBpi2CmtsProvisionedCmCertMacAddress.setStatus("current")


class _DocsBpi2CmtsProvisionedCmCertTrust_Type(Integer32):
    """Custom type docsBpi2CmtsProvisionedCmCertTrust based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_DocsBpi2CmtsProvisionedCmCertTrust_Type.__name__ = "Integer32"
_DocsBpi2CmtsProvisionedCmCertTrust_Object = MibTableColumn
docsBpi2CmtsProvisionedCmCertTrust = _DocsBpi2CmtsProvisionedCmCertTrust_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 1, 1, 2),
    _DocsBpi2CmtsProvisionedCmCertTrust_Type()
)
docsBpi2CmtsProvisionedCmCertTrust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsProvisionedCmCertTrust.setStatus("current")


class _DocsBpi2CmtsProvisionedCmCertSource_Type(Integer32):
    """Custom type docsBpi2CmtsProvisionedCmCertSource based on Integer32"""
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
        *(("snmp", 1),
          ("configurationFile", 2),
          ("externalDatabase", 3),
          ("other", 4))
    )


_DocsBpi2CmtsProvisionedCmCertSource_Type.__name__ = "Integer32"
_DocsBpi2CmtsProvisionedCmCertSource_Object = MibTableColumn
docsBpi2CmtsProvisionedCmCertSource = _DocsBpi2CmtsProvisionedCmCertSource_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 1, 1, 3),
    _DocsBpi2CmtsProvisionedCmCertSource_Type()
)
docsBpi2CmtsProvisionedCmCertSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsProvisionedCmCertSource.setStatus("current")
_DocsBpi2CmtsProvisionedCmCertStatus_Type = RowStatus
_DocsBpi2CmtsProvisionedCmCertStatus_Object = MibTableColumn
docsBpi2CmtsProvisionedCmCertStatus = _DocsBpi2CmtsProvisionedCmCertStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 1, 1, 4),
    _DocsBpi2CmtsProvisionedCmCertStatus_Type()
)
docsBpi2CmtsProvisionedCmCertStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsProvisionedCmCertStatus.setStatus("current")
_DocsBpi2CmtsProvisionedCmCert_Type = X509Certificate
_DocsBpi2CmtsProvisionedCmCert_Object = MibTableColumn
docsBpi2CmtsProvisionedCmCert = _DocsBpi2CmtsProvisionedCmCert_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 1, 1, 5),
    _DocsBpi2CmtsProvisionedCmCert_Type()
)
docsBpi2CmtsProvisionedCmCert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsProvisionedCmCert.setStatus("current")
_DocsBpi2CmtsCACertTable_Object = MibTable
docsBpi2CmtsCACertTable = _DocsBpi2CmtsCACertTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    docsBpi2CmtsCACertTable.setStatus("current")
_DocsBpi2CmtsCACertEntry_Object = MibTableRow
docsBpi2CmtsCACertEntry = _DocsBpi2CmtsCACertEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 2, 1)
)
docsBpi2CmtsCACertEntry.setIndexNames(
    (0, "DOCS-BPI2-MIB", "docsBpi2CmtsCACertIndex"),
)
if mibBuilder.loadTexts:
    docsBpi2CmtsCACertEntry.setStatus("current")


class _DocsBpi2CmtsCACertIndex_Type(Integer32):
    """Custom type docsBpi2CmtsCACertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_DocsBpi2CmtsCACertIndex_Type.__name__ = "Integer32"
_DocsBpi2CmtsCACertIndex_Object = MibTableColumn
docsBpi2CmtsCACertIndex = _DocsBpi2CmtsCACertIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 2, 1, 1),
    _DocsBpi2CmtsCACertIndex_Type()
)
docsBpi2CmtsCACertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsBpi2CmtsCACertIndex.setStatus("current")
_DocsBpi2CmtsCACertSubject_Type = SnmpAdminString
_DocsBpi2CmtsCACertSubject_Object = MibTableColumn
docsBpi2CmtsCACertSubject = _DocsBpi2CmtsCACertSubject_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 2, 1, 2),
    _DocsBpi2CmtsCACertSubject_Type()
)
docsBpi2CmtsCACertSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsCACertSubject.setStatus("current")
_DocsBpi2CmtsCACertIssuer_Type = SnmpAdminString
_DocsBpi2CmtsCACertIssuer_Object = MibTableColumn
docsBpi2CmtsCACertIssuer = _DocsBpi2CmtsCACertIssuer_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 2, 1, 3),
    _DocsBpi2CmtsCACertIssuer_Type()
)
docsBpi2CmtsCACertIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsCACertIssuer.setStatus("current")


class _DocsBpi2CmtsCACertSerialNumber_Type(OctetString):
    """Custom type docsBpi2CmtsCACertSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DocsBpi2CmtsCACertSerialNumber_Type.__name__ = "OctetString"
_DocsBpi2CmtsCACertSerialNumber_Object = MibTableColumn
docsBpi2CmtsCACertSerialNumber = _DocsBpi2CmtsCACertSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 2, 1, 4),
    _DocsBpi2CmtsCACertSerialNumber_Type()
)
docsBpi2CmtsCACertSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsCACertSerialNumber.setStatus("current")


class _DocsBpi2CmtsCACertTrust_Type(Integer32):
    """Custom type docsBpi2CmtsCACertTrust based on Integer32"""
    defaultValue = 3

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
        *(("trusted", 1),
          ("untrusted", 2),
          ("chained", 3),
          ("root", 4))
    )


_DocsBpi2CmtsCACertTrust_Type.__name__ = "Integer32"
_DocsBpi2CmtsCACertTrust_Object = MibTableColumn
docsBpi2CmtsCACertTrust = _DocsBpi2CmtsCACertTrust_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 2, 1, 5),
    _DocsBpi2CmtsCACertTrust_Type()
)
docsBpi2CmtsCACertTrust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsCACertTrust.setStatus("current")


class _DocsBpi2CmtsCACertSource_Type(Integer32):
    """Custom type docsBpi2CmtsCACertSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("snmp", 1),
          ("configurationFile", 2),
          ("externalDatabase", 3),
          ("other", 4),
          ("authentInfo", 5),
          ("compiledIntoCode", 6))
    )


_DocsBpi2CmtsCACertSource_Type.__name__ = "Integer32"
_DocsBpi2CmtsCACertSource_Object = MibTableColumn
docsBpi2CmtsCACertSource = _DocsBpi2CmtsCACertSource_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 2, 1, 6),
    _DocsBpi2CmtsCACertSource_Type()
)
docsBpi2CmtsCACertSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsCACertSource.setStatus("current")
_DocsBpi2CmtsCACertStatus_Type = RowStatus
_DocsBpi2CmtsCACertStatus_Object = MibTableColumn
docsBpi2CmtsCACertStatus = _DocsBpi2CmtsCACertStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 2, 1, 7),
    _DocsBpi2CmtsCACertStatus_Type()
)
docsBpi2CmtsCACertStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsCACertStatus.setStatus("current")
_DocsBpi2CmtsCACert_Type = X509Certificate
_DocsBpi2CmtsCACert_Object = MibTableColumn
docsBpi2CmtsCACert = _DocsBpi2CmtsCACert_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 2, 1, 8),
    _DocsBpi2CmtsCACert_Type()
)
docsBpi2CmtsCACert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsBpi2CmtsCACert.setStatus("current")


class _DocsBpi2CmtsCACertThumbprint_Type(OctetString):
    """Custom type docsBpi2CmtsCACertThumbprint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_DocsBpi2CmtsCACertThumbprint_Type.__name__ = "OctetString"
_DocsBpi2CmtsCACertThumbprint_Object = MibTableColumn
docsBpi2CmtsCACertThumbprint = _DocsBpi2CmtsCACertThumbprint_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 2, 5, 2, 1, 9),
    _DocsBpi2CmtsCACertThumbprint_Type()
)
docsBpi2CmtsCACertThumbprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CmtsCACertThumbprint.setStatus("current")
_DocsBpi2CodeDownloadControl_ObjectIdentity = ObjectIdentity
docsBpi2CodeDownloadControl = _DocsBpi2CodeDownloadControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 4)
)


class _DocsBpi2CodeDownloadStatusCode_Type(Integer32):
    """Custom type docsBpi2CodeDownloadStatusCode based on Integer32"""
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
        *(("configFileCvcVerified", 1),
          ("configFileCvcRejected", 2),
          ("snmpCvcVerified", 3),
          ("snmpCvcRejected", 4),
          ("codeFileVerified", 5),
          ("codeFileRejected", 6),
          ("other", 7))
    )


_DocsBpi2CodeDownloadStatusCode_Type.__name__ = "Integer32"
_DocsBpi2CodeDownloadStatusCode_Object = MibScalar
docsBpi2CodeDownloadStatusCode = _DocsBpi2CodeDownloadStatusCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 4, 1),
    _DocsBpi2CodeDownloadStatusCode_Type()
)
docsBpi2CodeDownloadStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CodeDownloadStatusCode.setStatus("current")
_DocsBpi2CodeDownloadStatusString_Type = SnmpAdminString
_DocsBpi2CodeDownloadStatusString_Object = MibScalar
docsBpi2CodeDownloadStatusString = _DocsBpi2CodeDownloadStatusString_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 4, 2),
    _DocsBpi2CodeDownloadStatusString_Type()
)
docsBpi2CodeDownloadStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CodeDownloadStatusString.setStatus("current")
_DocsBpi2CodeMfgOrgName_Type = SnmpAdminString
_DocsBpi2CodeMfgOrgName_Object = MibScalar
docsBpi2CodeMfgOrgName = _DocsBpi2CodeMfgOrgName_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 4, 3),
    _DocsBpi2CodeMfgOrgName_Type()
)
docsBpi2CodeMfgOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CodeMfgOrgName.setStatus("current")
_DocsBpi2CodeMfgCodeAccessStart_Type = DateAndTime
_DocsBpi2CodeMfgCodeAccessStart_Object = MibScalar
docsBpi2CodeMfgCodeAccessStart = _DocsBpi2CodeMfgCodeAccessStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 4, 4),
    _DocsBpi2CodeMfgCodeAccessStart_Type()
)
docsBpi2CodeMfgCodeAccessStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CodeMfgCodeAccessStart.setStatus("current")
_DocsBpi2CodeMfgCvcAccessStart_Type = DateAndTime
_DocsBpi2CodeMfgCvcAccessStart_Object = MibScalar
docsBpi2CodeMfgCvcAccessStart = _DocsBpi2CodeMfgCvcAccessStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 4, 5),
    _DocsBpi2CodeMfgCvcAccessStart_Type()
)
docsBpi2CodeMfgCvcAccessStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CodeMfgCvcAccessStart.setStatus("current")
_DocsBpi2CodeCoSignerOrgName_Type = SnmpAdminString
_DocsBpi2CodeCoSignerOrgName_Object = MibScalar
docsBpi2CodeCoSignerOrgName = _DocsBpi2CodeCoSignerOrgName_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 4, 6),
    _DocsBpi2CodeCoSignerOrgName_Type()
)
docsBpi2CodeCoSignerOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CodeCoSignerOrgName.setStatus("current")
_DocsBpi2CodeCoSignerCodeAccessStart_Type = DateAndTime
_DocsBpi2CodeCoSignerCodeAccessStart_Object = MibScalar
docsBpi2CodeCoSignerCodeAccessStart = _DocsBpi2CodeCoSignerCodeAccessStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 4, 7),
    _DocsBpi2CodeCoSignerCodeAccessStart_Type()
)
docsBpi2CodeCoSignerCodeAccessStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CodeCoSignerCodeAccessStart.setStatus("current")
_DocsBpi2CodeCoSignerCvcAccessStart_Type = DateAndTime
_DocsBpi2CodeCoSignerCvcAccessStart_Object = MibScalar
docsBpi2CodeCoSignerCvcAccessStart = _DocsBpi2CodeCoSignerCvcAccessStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 4, 8),
    _DocsBpi2CodeCoSignerCvcAccessStart_Type()
)
docsBpi2CodeCoSignerCvcAccessStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsBpi2CodeCoSignerCvcAccessStart.setStatus("current")
_DocsBpi2CodeCvcUpdate_Type = X509Certificate
_DocsBpi2CodeCvcUpdate_Object = MibScalar
docsBpi2CodeCvcUpdate = _DocsBpi2CodeCvcUpdate_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 1, 4, 9),
    _DocsBpi2CodeCvcUpdate_Type()
)
docsBpi2CodeCvcUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsBpi2CodeCvcUpdate.setStatus("current")
_DocsBpi2Notification_ObjectIdentity = ObjectIdentity
docsBpi2Notification = _DocsBpi2Notification_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 2)
)
_DocsBpi2Conformance_ObjectIdentity = ObjectIdentity
docsBpi2Conformance = _DocsBpi2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 3)
)
_DocsBpi2Compliances_ObjectIdentity = ObjectIdentity
docsBpi2Compliances = _DocsBpi2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 3, 1)
)
_DocsBpi2Groups_ObjectIdentity = ObjectIdentity
docsBpi2Groups = _DocsBpi2Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 3, 2)
)

# Managed Objects groups

docsBpi2CmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 3, 2, 1)
)
docsBpi2CmGroup.setObjects(
      *(("DOCS-BPI2-MIB", "docsBpi2CmPrivacyEnable"),
        ("DOCS-BPI2-MIB", "docsBpi2CmPublicKey"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthState"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthKeySequenceNumber"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthExpiresOld"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthExpiresNew"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthReset"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthGraceTime"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKGraceTime"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthWaitTimeout"),
        ("DOCS-BPI2-MIB", "docsBpi2CmReauthWaitTimeout"),
        ("DOCS-BPI2-MIB", "docsBpi2CmOpWaitTimeout"),
        ("DOCS-BPI2-MIB", "docsBpi2CmRekeyWaitTimeout"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthRejectWaitTimeout"),
        ("DOCS-BPI2-MIB", "docsBpi2CmSAMapWaitTimeout"),
        ("DOCS-BPI2-MIB", "docsBpi2CmSAMapMaxRetries"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthentInfos"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthRequests"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthReplies"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthRejects"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthInvalids"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthRejectErrorCode"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthRejectErrorString"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthInvalidErrorCode"),
        ("DOCS-BPI2-MIB", "docsBpi2CmAuthInvalidErrorString"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKSAType"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKDataEncryptAlg"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKDataAuthentAlg"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKState"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKKeySequenceNumber"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKExpiresOld"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKExpiresNew"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKKeyRequests"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKKeyReplies"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKKeyRejects"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKInvalids"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKAuthPends"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKKeyRejectErrorCode"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKKeyRejectErrorString"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKInvalidErrorCode"),
        ("DOCS-BPI2-MIB", "docsBpi2CmTEKInvalidErrorString"),
        ("DOCS-BPI2-MIB", "docsBpi2CmIpMulticastAddressType"),
        ("DOCS-BPI2-MIB", "docsBpi2CmIpMulticastAddress"),
        ("DOCS-BPI2-MIB", "docsBpi2CmIpMulticastSAId"),
        ("DOCS-BPI2-MIB", "docsBpi2CmIpMulticastSAMapState"),
        ("DOCS-BPI2-MIB", "docsBpi2CmIpMulticastSAMapRequests"),
        ("DOCS-BPI2-MIB", "docsBpi2CmIpMulticastSAMapReplies"),
        ("DOCS-BPI2-MIB", "docsBpi2CmIpMulticastSAMapRejects"),
        ("DOCS-BPI2-MIB", "docsBpi2CmIpMulticastSAMapRejectErrorCode"),
        ("DOCS-BPI2-MIB", "docsBpi2CmIpMulticastSAMapRejectErrorString"),
        ("DOCS-BPI2-MIB", "docsBpi2CmDeviceCmCert"),
        ("DOCS-BPI2-MIB", "docsBpi2CmDeviceManufCert"),
        ("DOCS-BPI2-MIB", "docsBpi2CmCryptoSuiteDataEncryptAlg"),
        ("DOCS-BPI2-MIB", "docsBpi2CmCryptoSuiteDataAuthentAlg"))
)
if mibBuilder.loadTexts:
    docsBpi2CmGroup.setStatus("current")

docsBpi2CmtsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 3, 2, 2)
)
docsBpi2CmtsGroup.setObjects(
      *(("DOCS-BPI2-MIB", "docsBpi2CmtsDefaultAuthLifetime"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsDefaultTEKLifetime"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsDefaultSelfSignedManufCertTrust"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsCheckCertValidityPeriods"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthentInfos"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthRequests"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthReplies"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthRejects"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthInvalids"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsSAMapRequests"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsSAMapReplies"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsSAMapRejects"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthCmBpiVersion"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthCmPublicKey"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthCmKeySequenceNumber"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthCmExpiresOld"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthCmExpiresNew"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthCmLifetime"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthCmReset"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthCmInfos"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthCmRequests"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthCmReplies"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthCmRejects"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthCmInvalids"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthRejectErrorCode"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthRejectErrorString"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthInvalidErrorCode"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthInvalidErrorString"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthPrimarySAId"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthBpkmCmCertValid"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsAuthBpkmCmCert"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsTEKSAType"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsTEKDataEncryptAlg"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsTEKDataAuthentAlg"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsTEKLifetime"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsTEKKeySequenceNumber"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsTEKExpiresOld"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsTEKExpiresNew"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsTEKReset"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsKeyRequests"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsKeyReplies"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsKeyRejects"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsTEKInvalids"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsKeyRejectErrorCode"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsKeyRejectErrorString"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsTEKInvalidErrorCode"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsTEKInvalidErrorString"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsIpMulticastAddressType"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsIpMulticastAddress"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsIpMulticastMaskType"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsIpMulticastMask"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsIpMulticastSAId"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsIpMulticastSAType"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsIpMulticastDataEncryptAlg"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsIpMulticastDataAuthentAlg"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsIpMulticastSAMapRequests"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsIpMulticastSAMapReplies"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsIpMulticastSAMapRejects"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsIpMulticastSAMapRejectErrorCode"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsIpMulticastSAMapRejectErrorString"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsIpMulticastMapControl"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsMulticastAuthControl"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsProvisionedCmCertTrust"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsProvisionedCmCertSource"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsProvisionedCmCertStatus"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsProvisionedCmCert"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsCACertSubject"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsCACertIssuer"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsCACertSerialNumber"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsCACertTrust"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsCACertSource"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsCACertStatus"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsCACert"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsCACertThumbprint"))
)
if mibBuilder.loadTexts:
    docsBpi2CmtsGroup.setStatus("current")

docsBpi2CodeDownloadGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 3, 2, 3)
)
docsBpi2CodeDownloadGroup.setObjects(
      *(("DOCS-BPI2-MIB", "docsBpi2CodeDownloadStatusCode"),
        ("DOCS-BPI2-MIB", "docsBpi2CodeDownloadStatusString"),
        ("DOCS-BPI2-MIB", "docsBpi2CodeMfgOrgName"),
        ("DOCS-BPI2-MIB", "docsBpi2CodeMfgCodeAccessStart"),
        ("DOCS-BPI2-MIB", "docsBpi2CodeMfgCvcAccessStart"),
        ("DOCS-BPI2-MIB", "docsBpi2CodeCoSignerOrgName"),
        ("DOCS-BPI2-MIB", "docsBpi2CodeCoSignerCodeAccessStart"),
        ("DOCS-BPI2-MIB", "docsBpi2CodeCoSignerCvcAccessStart"),
        ("DOCS-BPI2-MIB", "docsBpi2CodeCvcUpdate"))
)
if mibBuilder.loadTexts:
    docsBpi2CodeDownloadGroup.setStatus("current")

docsBpi2ObsoleteObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 3, 2, 4)
)
docsBpi2ObsoleteObjectsGroup.setObjects(
      *(("DOCS-BPI2-MIB", "docsBpi2CmtsAuthCmGraceTime"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsTEKGraceTime"))
)
if mibBuilder.loadTexts:
    docsBpi2ObsoleteObjectsGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsBpi2BasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 127, 6, 3, 1, 1)
)
docsBpi2BasicCompliance.setObjects(
      *(("DOCS-BPI2-MIB", "docsBpi2CmGroup"),
        ("DOCS-BPI2-MIB", "docsBpi2CmtsGroup"),
        ("DOCS-BPI2-MIB", "docsBpi2CodeDownloadGroup"))
)
if mibBuilder.loadTexts:
    docsBpi2BasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-BPI2-MIB",
    **{"X509Certificate": X509Certificate,
       "docsBpi2MIB": docsBpi2MIB,
       "docsBpi2MIBObjects": docsBpi2MIBObjects,
       "docsBpi2CmObjects": docsBpi2CmObjects,
       "docsBpi2CmBaseTable": docsBpi2CmBaseTable,
       "docsBpi2CmBaseEntry": docsBpi2CmBaseEntry,
       "docsBpi2CmPrivacyEnable": docsBpi2CmPrivacyEnable,
       "docsBpi2CmPublicKey": docsBpi2CmPublicKey,
       "docsBpi2CmAuthState": docsBpi2CmAuthState,
       "docsBpi2CmAuthKeySequenceNumber": docsBpi2CmAuthKeySequenceNumber,
       "docsBpi2CmAuthExpiresOld": docsBpi2CmAuthExpiresOld,
       "docsBpi2CmAuthExpiresNew": docsBpi2CmAuthExpiresNew,
       "docsBpi2CmAuthReset": docsBpi2CmAuthReset,
       "docsBpi2CmAuthGraceTime": docsBpi2CmAuthGraceTime,
       "docsBpi2CmTEKGraceTime": docsBpi2CmTEKGraceTime,
       "docsBpi2CmAuthWaitTimeout": docsBpi2CmAuthWaitTimeout,
       "docsBpi2CmReauthWaitTimeout": docsBpi2CmReauthWaitTimeout,
       "docsBpi2CmOpWaitTimeout": docsBpi2CmOpWaitTimeout,
       "docsBpi2CmRekeyWaitTimeout": docsBpi2CmRekeyWaitTimeout,
       "docsBpi2CmAuthRejectWaitTimeout": docsBpi2CmAuthRejectWaitTimeout,
       "docsBpi2CmSAMapWaitTimeout": docsBpi2CmSAMapWaitTimeout,
       "docsBpi2CmSAMapMaxRetries": docsBpi2CmSAMapMaxRetries,
       "docsBpi2CmAuthentInfos": docsBpi2CmAuthentInfos,
       "docsBpi2CmAuthRequests": docsBpi2CmAuthRequests,
       "docsBpi2CmAuthReplies": docsBpi2CmAuthReplies,
       "docsBpi2CmAuthRejects": docsBpi2CmAuthRejects,
       "docsBpi2CmAuthInvalids": docsBpi2CmAuthInvalids,
       "docsBpi2CmAuthRejectErrorCode": docsBpi2CmAuthRejectErrorCode,
       "docsBpi2CmAuthRejectErrorString": docsBpi2CmAuthRejectErrorString,
       "docsBpi2CmAuthInvalidErrorCode": docsBpi2CmAuthInvalidErrorCode,
       "docsBpi2CmAuthInvalidErrorString": docsBpi2CmAuthInvalidErrorString,
       "docsBpi2CmTEKTable": docsBpi2CmTEKTable,
       "docsBpi2CmTEKEntry": docsBpi2CmTEKEntry,
       "docsBpi2CmTEKSAId": docsBpi2CmTEKSAId,
       "docsBpi2CmTEKSAType": docsBpi2CmTEKSAType,
       "docsBpi2CmTEKDataEncryptAlg": docsBpi2CmTEKDataEncryptAlg,
       "docsBpi2CmTEKDataAuthentAlg": docsBpi2CmTEKDataAuthentAlg,
       "docsBpi2CmTEKState": docsBpi2CmTEKState,
       "docsBpi2CmTEKKeySequenceNumber": docsBpi2CmTEKKeySequenceNumber,
       "docsBpi2CmTEKExpiresOld": docsBpi2CmTEKExpiresOld,
       "docsBpi2CmTEKExpiresNew": docsBpi2CmTEKExpiresNew,
       "docsBpi2CmTEKKeyRequests": docsBpi2CmTEKKeyRequests,
       "docsBpi2CmTEKKeyReplies": docsBpi2CmTEKKeyReplies,
       "docsBpi2CmTEKKeyRejects": docsBpi2CmTEKKeyRejects,
       "docsBpi2CmTEKInvalids": docsBpi2CmTEKInvalids,
       "docsBpi2CmTEKAuthPends": docsBpi2CmTEKAuthPends,
       "docsBpi2CmTEKKeyRejectErrorCode": docsBpi2CmTEKKeyRejectErrorCode,
       "docsBpi2CmTEKKeyRejectErrorString": docsBpi2CmTEKKeyRejectErrorString,
       "docsBpi2CmTEKInvalidErrorCode": docsBpi2CmTEKInvalidErrorCode,
       "docsBpi2CmTEKInvalidErrorString": docsBpi2CmTEKInvalidErrorString,
       "docsBpi2CmMulticastObjects": docsBpi2CmMulticastObjects,
       "docsBpi2CmIpMulticastMapTable": docsBpi2CmIpMulticastMapTable,
       "docsBpi2CmIpMulticastMapEntry": docsBpi2CmIpMulticastMapEntry,
       "docsBpi2CmIpMulticastIndex": docsBpi2CmIpMulticastIndex,
       "docsBpi2CmIpMulticastAddressType": docsBpi2CmIpMulticastAddressType,
       "docsBpi2CmIpMulticastAddress": docsBpi2CmIpMulticastAddress,
       "docsBpi2CmIpMulticastSAId": docsBpi2CmIpMulticastSAId,
       "docsBpi2CmIpMulticastSAMapState": docsBpi2CmIpMulticastSAMapState,
       "docsBpi2CmIpMulticastSAMapRequests": docsBpi2CmIpMulticastSAMapRequests,
       "docsBpi2CmIpMulticastSAMapReplies": docsBpi2CmIpMulticastSAMapReplies,
       "docsBpi2CmIpMulticastSAMapRejects": docsBpi2CmIpMulticastSAMapRejects,
       "docsBpi2CmIpMulticastSAMapRejectErrorCode": docsBpi2CmIpMulticastSAMapRejectErrorCode,
       "docsBpi2CmIpMulticastSAMapRejectErrorString": docsBpi2CmIpMulticastSAMapRejectErrorString,
       "docsBpi2CmCertObjects": docsBpi2CmCertObjects,
       "docsBpi2CmDeviceCertTable": docsBpi2CmDeviceCertTable,
       "docsBpi2CmDeviceCertEntry": docsBpi2CmDeviceCertEntry,
       "docsBpi2CmDeviceCmCert": docsBpi2CmDeviceCmCert,
       "docsBpi2CmDeviceManufCert": docsBpi2CmDeviceManufCert,
       "docsBpi2CmCryptoSuiteTable": docsBpi2CmCryptoSuiteTable,
       "docsBpi2CmCryptoSuiteEntry": docsBpi2CmCryptoSuiteEntry,
       "docsBpi2CmCryptoSuiteIndex": docsBpi2CmCryptoSuiteIndex,
       "docsBpi2CmCryptoSuiteDataEncryptAlg": docsBpi2CmCryptoSuiteDataEncryptAlg,
       "docsBpi2CmCryptoSuiteDataAuthentAlg": docsBpi2CmCryptoSuiteDataAuthentAlg,
       "docsBpi2CmtsObjects": docsBpi2CmtsObjects,
       "docsBpi2CmtsBaseTable": docsBpi2CmtsBaseTable,
       "docsBpi2CmtsBaseEntry": docsBpi2CmtsBaseEntry,
       "docsBpi2CmtsDefaultAuthLifetime": docsBpi2CmtsDefaultAuthLifetime,
       "docsBpi2CmtsDefaultTEKLifetime": docsBpi2CmtsDefaultTEKLifetime,
       "docsBpi2CmtsDefaultSelfSignedManufCertTrust": docsBpi2CmtsDefaultSelfSignedManufCertTrust,
       "docsBpi2CmtsCheckCertValidityPeriods": docsBpi2CmtsCheckCertValidityPeriods,
       "docsBpi2CmtsAuthentInfos": docsBpi2CmtsAuthentInfos,
       "docsBpi2CmtsAuthRequests": docsBpi2CmtsAuthRequests,
       "docsBpi2CmtsAuthReplies": docsBpi2CmtsAuthReplies,
       "docsBpi2CmtsAuthRejects": docsBpi2CmtsAuthRejects,
       "docsBpi2CmtsAuthInvalids": docsBpi2CmtsAuthInvalids,
       "docsBpi2CmtsSAMapRequests": docsBpi2CmtsSAMapRequests,
       "docsBpi2CmtsSAMapReplies": docsBpi2CmtsSAMapReplies,
       "docsBpi2CmtsSAMapRejects": docsBpi2CmtsSAMapRejects,
       "docsBpi2CmtsAuthTable": docsBpi2CmtsAuthTable,
       "docsBpi2CmtsAuthEntry": docsBpi2CmtsAuthEntry,
       "docsBpi2CmtsAuthCmMacAddress": docsBpi2CmtsAuthCmMacAddress,
       "docsBpi2CmtsAuthCmBpiVersion": docsBpi2CmtsAuthCmBpiVersion,
       "docsBpi2CmtsAuthCmPublicKey": docsBpi2CmtsAuthCmPublicKey,
       "docsBpi2CmtsAuthCmKeySequenceNumber": docsBpi2CmtsAuthCmKeySequenceNumber,
       "docsBpi2CmtsAuthCmExpiresOld": docsBpi2CmtsAuthCmExpiresOld,
       "docsBpi2CmtsAuthCmExpiresNew": docsBpi2CmtsAuthCmExpiresNew,
       "docsBpi2CmtsAuthCmLifetime": docsBpi2CmtsAuthCmLifetime,
       "docsBpi2CmtsAuthCmGraceTime": docsBpi2CmtsAuthCmGraceTime,
       "docsBpi2CmtsAuthCmReset": docsBpi2CmtsAuthCmReset,
       "docsBpi2CmtsAuthCmInfos": docsBpi2CmtsAuthCmInfos,
       "docsBpi2CmtsAuthCmRequests": docsBpi2CmtsAuthCmRequests,
       "docsBpi2CmtsAuthCmReplies": docsBpi2CmtsAuthCmReplies,
       "docsBpi2CmtsAuthCmRejects": docsBpi2CmtsAuthCmRejects,
       "docsBpi2CmtsAuthCmInvalids": docsBpi2CmtsAuthCmInvalids,
       "docsBpi2CmtsAuthRejectErrorCode": docsBpi2CmtsAuthRejectErrorCode,
       "docsBpi2CmtsAuthRejectErrorString": docsBpi2CmtsAuthRejectErrorString,
       "docsBpi2CmtsAuthInvalidErrorCode": docsBpi2CmtsAuthInvalidErrorCode,
       "docsBpi2CmtsAuthInvalidErrorString": docsBpi2CmtsAuthInvalidErrorString,
       "docsBpi2CmtsAuthPrimarySAId": docsBpi2CmtsAuthPrimarySAId,
       "docsBpi2CmtsAuthBpkmCmCertValid": docsBpi2CmtsAuthBpkmCmCertValid,
       "docsBpi2CmtsAuthBpkmCmCert": docsBpi2CmtsAuthBpkmCmCert,
       "docsBpi2CmtsTEKTable": docsBpi2CmtsTEKTable,
       "docsBpi2CmtsTEKEntry": docsBpi2CmtsTEKEntry,
       "docsBpi2CmtsTEKSAId": docsBpi2CmtsTEKSAId,
       "docsBpi2CmtsTEKSAType": docsBpi2CmtsTEKSAType,
       "docsBpi2CmtsTEKDataEncryptAlg": docsBpi2CmtsTEKDataEncryptAlg,
       "docsBpi2CmtsTEKDataAuthentAlg": docsBpi2CmtsTEKDataAuthentAlg,
       "docsBpi2CmtsTEKLifetime": docsBpi2CmtsTEKLifetime,
       "docsBpi2CmtsTEKGraceTime": docsBpi2CmtsTEKGraceTime,
       "docsBpi2CmtsTEKKeySequenceNumber": docsBpi2CmtsTEKKeySequenceNumber,
       "docsBpi2CmtsTEKExpiresOld": docsBpi2CmtsTEKExpiresOld,
       "docsBpi2CmtsTEKExpiresNew": docsBpi2CmtsTEKExpiresNew,
       "docsBpi2CmtsTEKReset": docsBpi2CmtsTEKReset,
       "docsBpi2CmtsKeyRequests": docsBpi2CmtsKeyRequests,
       "docsBpi2CmtsKeyReplies": docsBpi2CmtsKeyReplies,
       "docsBpi2CmtsKeyRejects": docsBpi2CmtsKeyRejects,
       "docsBpi2CmtsTEKInvalids": docsBpi2CmtsTEKInvalids,
       "docsBpi2CmtsKeyRejectErrorCode": docsBpi2CmtsKeyRejectErrorCode,
       "docsBpi2CmtsKeyRejectErrorString": docsBpi2CmtsKeyRejectErrorString,
       "docsBpi2CmtsTEKInvalidErrorCode": docsBpi2CmtsTEKInvalidErrorCode,
       "docsBpi2CmtsTEKInvalidErrorString": docsBpi2CmtsTEKInvalidErrorString,
       "docsBpi2CmtsMulticastObjects": docsBpi2CmtsMulticastObjects,
       "docsBpi2CmtsIpMulticastMapTable": docsBpi2CmtsIpMulticastMapTable,
       "docsBpi2CmtsIpMulticastMapEntry": docsBpi2CmtsIpMulticastMapEntry,
       "docsBpi2CmtsIpMulticastIndex": docsBpi2CmtsIpMulticastIndex,
       "docsBpi2CmtsIpMulticastAddressType": docsBpi2CmtsIpMulticastAddressType,
       "docsBpi2CmtsIpMulticastAddress": docsBpi2CmtsIpMulticastAddress,
       "docsBpi2CmtsIpMulticastMaskType": docsBpi2CmtsIpMulticastMaskType,
       "docsBpi2CmtsIpMulticastMask": docsBpi2CmtsIpMulticastMask,
       "docsBpi2CmtsIpMulticastSAId": docsBpi2CmtsIpMulticastSAId,
       "docsBpi2CmtsIpMulticastSAType": docsBpi2CmtsIpMulticastSAType,
       "docsBpi2CmtsIpMulticastDataEncryptAlg": docsBpi2CmtsIpMulticastDataEncryptAlg,
       "docsBpi2CmtsIpMulticastDataAuthentAlg": docsBpi2CmtsIpMulticastDataAuthentAlg,
       "docsBpi2CmtsIpMulticastSAMapRequests": docsBpi2CmtsIpMulticastSAMapRequests,
       "docsBpi2CmtsIpMulticastSAMapReplies": docsBpi2CmtsIpMulticastSAMapReplies,
       "docsBpi2CmtsIpMulticastSAMapRejects": docsBpi2CmtsIpMulticastSAMapRejects,
       "docsBpi2CmtsIpMulticastSAMapRejectErrorCode": docsBpi2CmtsIpMulticastSAMapRejectErrorCode,
       "docsBpi2CmtsIpMulticastSAMapRejectErrorString": docsBpi2CmtsIpMulticastSAMapRejectErrorString,
       "docsBpi2CmtsIpMulticastMapControl": docsBpi2CmtsIpMulticastMapControl,
       "docsBpi2CmtsMulticastAuthTable": docsBpi2CmtsMulticastAuthTable,
       "docsBpi2CmtsMulticastAuthEntry": docsBpi2CmtsMulticastAuthEntry,
       "docsBpi2CmtsMulticastAuthSAId": docsBpi2CmtsMulticastAuthSAId,
       "docsBpi2CmtsMulticastAuthCmMacAddress": docsBpi2CmtsMulticastAuthCmMacAddress,
       "docsBpi2CmtsMulticastAuthControl": docsBpi2CmtsMulticastAuthControl,
       "docsBpi2CmtsCertObjects": docsBpi2CmtsCertObjects,
       "docsBpi2CmtsProvisionedCmCertTable": docsBpi2CmtsProvisionedCmCertTable,
       "docsBpi2CmtsProvisionedCmCertEntry": docsBpi2CmtsProvisionedCmCertEntry,
       "docsBpi2CmtsProvisionedCmCertMacAddress": docsBpi2CmtsProvisionedCmCertMacAddress,
       "docsBpi2CmtsProvisionedCmCertTrust": docsBpi2CmtsProvisionedCmCertTrust,
       "docsBpi2CmtsProvisionedCmCertSource": docsBpi2CmtsProvisionedCmCertSource,
       "docsBpi2CmtsProvisionedCmCertStatus": docsBpi2CmtsProvisionedCmCertStatus,
       "docsBpi2CmtsProvisionedCmCert": docsBpi2CmtsProvisionedCmCert,
       "docsBpi2CmtsCACertTable": docsBpi2CmtsCACertTable,
       "docsBpi2CmtsCACertEntry": docsBpi2CmtsCACertEntry,
       "docsBpi2CmtsCACertIndex": docsBpi2CmtsCACertIndex,
       "docsBpi2CmtsCACertSubject": docsBpi2CmtsCACertSubject,
       "docsBpi2CmtsCACertIssuer": docsBpi2CmtsCACertIssuer,
       "docsBpi2CmtsCACertSerialNumber": docsBpi2CmtsCACertSerialNumber,
       "docsBpi2CmtsCACertTrust": docsBpi2CmtsCACertTrust,
       "docsBpi2CmtsCACertSource": docsBpi2CmtsCACertSource,
       "docsBpi2CmtsCACertStatus": docsBpi2CmtsCACertStatus,
       "docsBpi2CmtsCACert": docsBpi2CmtsCACert,
       "docsBpi2CmtsCACertThumbprint": docsBpi2CmtsCACertThumbprint,
       "docsBpi2CodeDownloadControl": docsBpi2CodeDownloadControl,
       "docsBpi2CodeDownloadStatusCode": docsBpi2CodeDownloadStatusCode,
       "docsBpi2CodeDownloadStatusString": docsBpi2CodeDownloadStatusString,
       "docsBpi2CodeMfgOrgName": docsBpi2CodeMfgOrgName,
       "docsBpi2CodeMfgCodeAccessStart": docsBpi2CodeMfgCodeAccessStart,
       "docsBpi2CodeMfgCvcAccessStart": docsBpi2CodeMfgCvcAccessStart,
       "docsBpi2CodeCoSignerOrgName": docsBpi2CodeCoSignerOrgName,
       "docsBpi2CodeCoSignerCodeAccessStart": docsBpi2CodeCoSignerCodeAccessStart,
       "docsBpi2CodeCoSignerCvcAccessStart": docsBpi2CodeCoSignerCvcAccessStart,
       "docsBpi2CodeCvcUpdate": docsBpi2CodeCvcUpdate,
       "docsBpi2Notification": docsBpi2Notification,
       "docsBpi2Conformance": docsBpi2Conformance,
       "docsBpi2Compliances": docsBpi2Compliances,
       "docsBpi2BasicCompliance": docsBpi2BasicCompliance,
       "docsBpi2Groups": docsBpi2Groups,
       "docsBpi2CmGroup": docsBpi2CmGroup,
       "docsBpi2CmtsGroup": docsBpi2CmtsGroup,
       "docsBpi2CodeDownloadGroup": docsBpi2CodeDownloadGroup,
       "docsBpi2ObsoleteObjectsGroup": docsBpi2ObsoleteObjectsGroup}
)
