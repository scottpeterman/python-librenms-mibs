# SNMP MIB module (CM-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\CM-SECURITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:32 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(IpVersion,
 UserInterfaceType) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "IpVersion",
    "UserInterfaceType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(usmUserEntry,) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "usmUserEntry")

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
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

cmSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10)
)
if mibBuilder.loadTexts:
    cmSecurityMIB.setRevisions(
        ("2021-01-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SecuritySelfTestResult(TextualConvention, Integer32):
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
        *(("notApplicable", 0),
          ("fail", 1),
          ("success", 2))
    )



class SecuritySelfTestStatus(TextualConvention, Integer32):
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
        *(("notApplicable", 0),
          ("notStarted", 1),
          ("inprogress", 2),
          ("complete", 3))
    )



class CmRemoteAuthProtocol(TextualConvention, Integer32):
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
          ("radius", 2),
          ("tacacs", 3))
    )



class CmSecurityAccessOrder(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )



class CmSecurityAuthType(TextualConvention, Integer32):
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
        *(("pap", 1),
          ("chap", 2),
          ("ascii", 3))
    )



class CmSecurityPrivLevel(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("retrieve", 1),
          ("maintenance", 2),
          ("provisioning", 3),
          ("superuser", 4),
          ("testuser", 5),
          ("cryptouser", 6),
          ("netconf", 7))
    )



class CmRemoteAuthOrder(TextualConvention, Integer32):
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
        *(("first", 1),
          ("second", 2),
          ("third", 3))
    )



class CmSecurityPolicyStrength(TextualConvention, Integer32):
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
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )



class UsmUserAccessType(TextualConvention, Integer32):
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
        *(("read-only", 1),
          ("read-write", 2),
          ("trap-only", 3))
    )



class SecurityUserAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("remove-lockout", 1))
    )



class SnmpSecurityTrapType(TextualConvention, Integer32):
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
        *(("all", 1),
          ("loginFailed", 2),
          ("disabled", 3))
    )



class PrivilegeRequestAction(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("none", 1),
          ("approve", 2),
          ("deny", 3),
          ("cancel", 4))
    )



class PrivilegeRequestState(TextualConvention, Integer32):
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
          ("requestSent", 2),
          ("requestCanceled", 3),
          ("requestApproved", 4),
          ("requestDenied", 5),
          ("requestTimeout", 6),
          ("accessExpired", 7),
          ("accessCanceled", 8))
    )



class RsaKeyLengthType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rsaKeyLength2048", 1),
          ("rsaKeyLength4096", 2))
    )



class ZeroizeKeysAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("ZeroizeKeys", 1))
    )



class RunSelfTestAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("RunSelfTest", 1))
    )



class SslCertificateAction(TextualConvention, Integer32):
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
        *(("notApplicable", 0),
          ("deleteSslKeyPair", 1),
          ("setHttpsSslKeyPair", 2),
          ("addRsaPrivateKey", 3))
    )



class RsaKeyPairAction(TextualConvention, Integer32):
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
        *(("notApplicable", 0),
          ("genRsaKeyPair", 1),
          ("delRsaKeyPair", 2))
    )



class CsrAction(TextualConvention, Integer32):
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
        *(("notApplicable", 0),
          ("genCsr", 1),
          ("delCsr", 2))
    )



class NasIpAddressType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("userDefined", 1),
          ("packetSourceIp", 2))
    )



class CertificateEnrollmentProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("scep", 1)
    )



class CaAction(TextualConvention, Integer32):
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
        *(("none", 1),
          ("updateCACertificates", 2),
          ("startAutoEnrollment", 3),
          ("getCACertificates", 4))
    )



class SslCertificatePrivateKeyPairAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("trustRootCACertificate", 2))
    )



class CertificateType(TextualConvention, Integer32):
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
        *(("root", 1),
          ("intermediate", 2),
          ("device", 3))
    )



class CertificateStatus(TextualConvention, Integer32):
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
        *(("trusted", 1),
          ("untrusted", 2),
          ("valid", 3),
          ("invalid", 4))
    )



class AutoEnrollmentStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 1),
          ("failure", 2),
          ("success", 3),
          ("pending", 4),
          ("aborted", 5),
          ("timedout", 6))
    )



class CaRootCertStatus(TextualConvention, Integer32):
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
        *(("pending", 1),
          ("active", 2),
          ("failed", 3),
          ("renewing", 4),
          ("renewalFailed", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CmSecurityObjects_ObjectIdentity = ObjectIdentity
cmSecurityObjects = _CmSecurityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1)
)
_CmAuthProtocol_Type = CmRemoteAuthProtocol
_CmAuthProtocol_Object = MibScalar
cmAuthProtocol = _CmAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 1),
    _CmAuthProtocol_Type()
)
cmAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAuthProtocol.setStatus("current")
_CmAccessOrder_Type = CmSecurityAccessOrder
_CmAccessOrder_Object = MibScalar
cmAccessOrder = _CmAccessOrder_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 2),
    _CmAccessOrder_Type()
)
cmAccessOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAccessOrder.setStatus("current")
_CmAuthType_Type = CmSecurityAuthType
_CmAuthType_Object = MibScalar
cmAuthType = _CmAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 3),
    _CmAuthType_Type()
)
cmAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAuthType.setStatus("current")
_CmNASIpAddress_Type = IpAddress
_CmNASIpAddress_Object = MibScalar
cmNASIpAddress = _CmNASIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 4),
    _CmNASIpAddress_Type()
)
cmNASIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmNASIpAddress.setStatus("current")
_CmSecurityUserTable_Object = MibTable
cmSecurityUserTable = _CmSecurityUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5)
)
if mibBuilder.loadTexts:
    cmSecurityUserTable.setStatus("current")
_CmSecurityUserEntry_Object = MibTableRow
cmSecurityUserEntry = _CmSecurityUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1)
)
cmSecurityUserEntry.setIndexNames(
    (0, "CM-SECURITY-MIB", "cmSecurityUserName"),
    (0, "CM-SECURITY-MIB", "cmSecurityUserRemoteUser"),
)
if mibBuilder.loadTexts:
    cmSecurityUserEntry.setStatus("current")


class _CmSecurityUserName_Type(DisplayString):
    """Custom type cmSecurityUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CmSecurityUserName_Type.__name__ = "DisplayString"
_CmSecurityUserName_Object = MibTableColumn
cmSecurityUserName = _CmSecurityUserName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 1),
    _CmSecurityUserName_Type()
)
cmSecurityUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserName.setStatus("current")


class _CmSecurityUserComment_Type(DisplayString):
    """Custom type cmSecurityUserComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CmSecurityUserComment_Type.__name__ = "DisplayString"
_CmSecurityUserComment_Object = MibTableColumn
cmSecurityUserComment = _CmSecurityUserComment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 2),
    _CmSecurityUserComment_Type()
)
cmSecurityUserComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserComment.setStatus("current")
_CmSecurityUserPrivLevel_Type = CmSecurityPrivLevel
_CmSecurityUserPrivLevel_Object = MibTableColumn
cmSecurityUserPrivLevel = _CmSecurityUserPrivLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 3),
    _CmSecurityUserPrivLevel_Type()
)
cmSecurityUserPrivLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserPrivLevel.setStatus("current")
_CmSecurityUserLoginTimeout_Type = Integer32
_CmSecurityUserLoginTimeout_Object = MibTableColumn
cmSecurityUserLoginTimeout = _CmSecurityUserLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 4),
    _CmSecurityUserLoginTimeout_Type()
)
cmSecurityUserLoginTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserLoginTimeout.setStatus("current")
_CmSecurityUserNumFailedLoginAttempts_Type = Integer32
_CmSecurityUserNumFailedLoginAttempts_Object = MibTableColumn
cmSecurityUserNumFailedLoginAttempts = _CmSecurityUserNumFailedLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 5),
    _CmSecurityUserNumFailedLoginAttempts_Type()
)
cmSecurityUserNumFailedLoginAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSecurityUserNumFailedLoginAttempts.setStatus("current")
_CmSecurityUserLastLoginTime_Type = DateAndTime
_CmSecurityUserLastLoginTime_Object = MibTableColumn
cmSecurityUserLastLoginTime = _CmSecurityUserLastLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 6),
    _CmSecurityUserLastLoginTime_Type()
)
cmSecurityUserLastLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSecurityUserLastLoginTime.setStatus("current")
_CmSecurityUserLockedout_Type = TruthValue
_CmSecurityUserLockedout_Object = MibTableColumn
cmSecurityUserLockedout = _CmSecurityUserLockedout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 7),
    _CmSecurityUserLockedout_Type()
)
cmSecurityUserLockedout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSecurityUserLockedout.setStatus("current")
_CmSecurityUserLastLockedoutTime_Type = DateAndTime
_CmSecurityUserLastLockedoutTime_Object = MibTableColumn
cmSecurityUserLastLockedoutTime = _CmSecurityUserLastLockedoutTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 8),
    _CmSecurityUserLastLockedoutTime_Type()
)
cmSecurityUserLastLockedoutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSecurityUserLastLockedoutTime.setStatus("current")
_CmSecurityUserCliPagingEnable_Type = TruthValue
_CmSecurityUserCliPagingEnable_Object = MibTableColumn
cmSecurityUserCliPagingEnable = _CmSecurityUserCliPagingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 9),
    _CmSecurityUserCliPagingEnable_Type()
)
cmSecurityUserCliPagingEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserCliPagingEnable.setStatus("current")
_CmSecurityUserRemoteUser_Type = TruthValue
_CmSecurityUserRemoteUser_Object = MibTableColumn
cmSecurityUserRemoteUser = _CmSecurityUserRemoteUser_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 10),
    _CmSecurityUserRemoteUser_Type()
)
cmSecurityUserRemoteUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSecurityUserRemoteUser.setStatus("current")


class _CmSecurityUserPassword_Type(DisplayString):
    """Custom type cmSecurityUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmSecurityUserPassword_Type.__name__ = "DisplayString"
_CmSecurityUserPassword_Object = MibTableColumn
cmSecurityUserPassword = _CmSecurityUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 11),
    _CmSecurityUserPassword_Type()
)
cmSecurityUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserPassword.setStatus("current")
_CmSecurityUserStorageType_Type = StorageType
_CmSecurityUserStorageType_Object = MibTableColumn
cmSecurityUserStorageType = _CmSecurityUserStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 12),
    _CmSecurityUserStorageType_Type()
)
cmSecurityUserStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserStorageType.setStatus("current")
_CmSecurityUserRowStatus_Type = RowStatus
_CmSecurityUserRowStatus_Object = MibTableColumn
cmSecurityUserRowStatus = _CmSecurityUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 13),
    _CmSecurityUserRowStatus_Type()
)
cmSecurityUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserRowStatus.setStatus("current")
_CmSecurityUserAction_Type = SecurityUserAction
_CmSecurityUserAction_Object = MibTableColumn
cmSecurityUserAction = _CmSecurityUserAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 14),
    _CmSecurityUserAction_Type()
)
cmSecurityUserAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSecurityUserAction.setStatus("current")


class _CmSecurityCryptoPassword_Type(DisplayString):
    """Custom type cmSecurityCryptoPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmSecurityCryptoPassword_Type.__name__ = "DisplayString"
_CmSecurityCryptoPassword_Object = MibTableColumn
cmSecurityCryptoPassword = _CmSecurityCryptoPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 15),
    _CmSecurityCryptoPassword_Type()
)
cmSecurityCryptoPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityCryptoPassword.setStatus("current")
_CmSecurityUserRemoteCryptoUser_Type = TruthValue
_CmSecurityUserRemoteCryptoUser_Object = MibTableColumn
cmSecurityUserRemoteCryptoUser = _CmSecurityUserRemoteCryptoUser_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 16),
    _CmSecurityUserRemoteCryptoUser_Type()
)
cmSecurityUserRemoteCryptoUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserRemoteCryptoUser.setStatus("current")
_CmSecurityUserSso2fa_Type = TruthValue
_CmSecurityUserSso2fa_Object = MibTableColumn
cmSecurityUserSso2fa = _CmSecurityUserSso2fa_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 17),
    _CmSecurityUserSso2fa_Type()
)
cmSecurityUserSso2fa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserSso2fa.setStatus("current")
_CmRemoteAuthServerTable_Object = MibTable
cmRemoteAuthServerTable = _CmRemoteAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6)
)
if mibBuilder.loadTexts:
    cmRemoteAuthServerTable.setStatus("current")
_CmRemoteAuthServerEntry_Object = MibTableRow
cmRemoteAuthServerEntry = _CmRemoteAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1)
)
cmRemoteAuthServerEntry.setIndexNames(
    (0, "CM-SECURITY-MIB", "cmRemoteAuthServerIndex"),
)
if mibBuilder.loadTexts:
    cmRemoteAuthServerEntry.setStatus("current")
_CmRemoteAuthServerIndex_Type = Integer32
_CmRemoteAuthServerIndex_Object = MibTableColumn
cmRemoteAuthServerIndex = _CmRemoteAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 1),
    _CmRemoteAuthServerIndex_Type()
)
cmRemoteAuthServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRemoteAuthServerIndex.setStatus("current")
_CmRemoteAuthServerEnabled_Type = TruthValue
_CmRemoteAuthServerEnabled_Object = MibTableColumn
cmRemoteAuthServerEnabled = _CmRemoteAuthServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 2),
    _CmRemoteAuthServerEnabled_Type()
)
cmRemoteAuthServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerEnabled.setStatus("current")
_CmRemoteAuthServerOrder_Type = CmRemoteAuthOrder
_CmRemoteAuthServerOrder_Object = MibTableColumn
cmRemoteAuthServerOrder = _CmRemoteAuthServerOrder_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 3),
    _CmRemoteAuthServerOrder_Type()
)
cmRemoteAuthServerOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerOrder.setStatus("current")
_CmRemoteAuthServerIpAddress_Type = IpAddress
_CmRemoteAuthServerIpAddress_Object = MibTableColumn
cmRemoteAuthServerIpAddress = _CmRemoteAuthServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 4),
    _CmRemoteAuthServerIpAddress_Type()
)
cmRemoteAuthServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerIpAddress.setStatus("current")
_CmRemoteAuthServerPort_Type = Integer32
_CmRemoteAuthServerPort_Object = MibTableColumn
cmRemoteAuthServerPort = _CmRemoteAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 5),
    _CmRemoteAuthServerPort_Type()
)
cmRemoteAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerPort.setStatus("current")
_CmRemoteAuthServerNumRetries_Type = Integer32
_CmRemoteAuthServerNumRetries_Object = MibTableColumn
cmRemoteAuthServerNumRetries = _CmRemoteAuthServerNumRetries_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 6),
    _CmRemoteAuthServerNumRetries_Type()
)
cmRemoteAuthServerNumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerNumRetries.setStatus("current")
_CmRemoteAuthServerTimeout_Type = Integer32
_CmRemoteAuthServerTimeout_Object = MibTableColumn
cmRemoteAuthServerTimeout = _CmRemoteAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 7),
    _CmRemoteAuthServerTimeout_Type()
)
cmRemoteAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerTimeout.setStatus("current")


class _CmRemoteAuthServerSecret_Type(DisplayString):
    """Custom type cmRemoteAuthServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CmRemoteAuthServerSecret_Type.__name__ = "DisplayString"
_CmRemoteAuthServerSecret_Object = MibTableColumn
cmRemoteAuthServerSecret = _CmRemoteAuthServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 8),
    _CmRemoteAuthServerSecret_Type()
)
cmRemoteAuthServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerSecret.setStatus("current")
_CmRemoteAuthServerAccountingPort_Type = Integer32
_CmRemoteAuthServerAccountingPort_Object = MibTableColumn
cmRemoteAuthServerAccountingPort = _CmRemoteAuthServerAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 9),
    _CmRemoteAuthServerAccountingPort_Type()
)
cmRemoteAuthServerAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerAccountingPort.setStatus("current")
_CmRemoteAuthServerIpVersion_Type = IpVersion
_CmRemoteAuthServerIpVersion_Object = MibTableColumn
cmRemoteAuthServerIpVersion = _CmRemoteAuthServerIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 10),
    _CmRemoteAuthServerIpVersion_Type()
)
cmRemoteAuthServerIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerIpVersion.setStatus("current")
_CmRemoteAuthServerIpv6Addr_Type = Ipv6Address
_CmRemoteAuthServerIpv6Addr_Object = MibTableColumn
cmRemoteAuthServerIpv6Addr = _CmRemoteAuthServerIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 11),
    _CmRemoteAuthServerIpv6Addr_Type()
)
cmRemoteAuthServerIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerIpv6Addr.setStatus("current")
_CmSecurityPolicyStrength_Type = CmSecurityPolicyStrength
_CmSecurityPolicyStrength_Object = MibScalar
cmSecurityPolicyStrength = _CmSecurityPolicyStrength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 7),
    _CmSecurityPolicyStrength_Type()
)
cmSecurityPolicyStrength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSecurityPolicyStrength.setStatus("current")
_CmRemoteAuthServerAccountingEnabled_Type = TruthValue
_CmRemoteAuthServerAccountingEnabled_Object = MibScalar
cmRemoteAuthServerAccountingEnabled = _CmRemoteAuthServerAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 8),
    _CmRemoteAuthServerAccountingEnabled_Type()
)
cmRemoteAuthServerAccountingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerAccountingEnabled.setStatus("current")
_F3UsmUserTable_Object = MibTable
f3UsmUserTable = _F3UsmUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 9)
)
if mibBuilder.loadTexts:
    f3UsmUserTable.setStatus("current")
_F3UsmUserEntry_Object = MibTableRow
f3UsmUserEntry = _F3UsmUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 9, 1)
)
if mibBuilder.loadTexts:
    f3UsmUserEntry.setStatus("current")
_F3UsmUserAccessType_Type = UsmUserAccessType
_F3UsmUserAccessType_Object = MibTableColumn
f3UsmUserAccessType = _F3UsmUserAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 9, 1, 1),
    _F3UsmUserAccessType_Type()
)
f3UsmUserAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsmUserAccessType.setStatus("current")
_F3TacacsPrivLevelControlEnabled_Type = TruthValue
_F3TacacsPrivLevelControlEnabled_Object = MibScalar
f3TacacsPrivLevelControlEnabled = _F3TacacsPrivLevelControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 10),
    _F3TacacsPrivLevelControlEnabled_Type()
)
f3TacacsPrivLevelControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TacacsPrivLevelControlEnabled.setStatus("current")
_F3TacacsDefaultPrivLevel_Type = CmSecurityPrivLevel
_F3TacacsDefaultPrivLevel_Object = MibScalar
f3TacacsDefaultPrivLevel = _F3TacacsDefaultPrivLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 11),
    _F3TacacsDefaultPrivLevel_Type()
)
f3TacacsDefaultPrivLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TacacsDefaultPrivLevel.setStatus("current")
_F3NasIpv6Addr_Type = Ipv6Address
_F3NasIpv6Addr_Object = MibScalar
f3NasIpv6Addr = _F3NasIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 12),
    _F3NasIpv6Addr_Type()
)
f3NasIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NasIpv6Addr.setStatus("current")
_F3SecurityTrapType_Type = SnmpSecurityTrapType
_F3SecurityTrapType_Object = MibScalar
f3SecurityTrapType = _F3SecurityTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 13),
    _F3SecurityTrapType_Type()
)
f3SecurityTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SecurityTrapType.setStatus("current")
_F3SecurityTrapInfo_Type = DisplayString
_F3SecurityTrapInfo_Object = MibScalar
f3SecurityTrapInfo = _F3SecurityTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 14),
    _F3SecurityTrapInfo_Type()
)
f3SecurityTrapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SecurityTrapInfo.setStatus("current")
_F3PrivilegeChangeTable_Object = MibTable
f3PrivilegeChangeTable = _F3PrivilegeChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15)
)
if mibBuilder.loadTexts:
    f3PrivilegeChangeTable.setStatus("current")
_F3PrivilegeChangeEntry_Object = MibTableRow
f3PrivilegeChangeEntry = _F3PrivilegeChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1)
)
f3PrivilegeChangeEntry.setIndexNames(
    (0, "CM-SECURITY-MIB", "f3PrivilegeChangeId"),
)
if mibBuilder.loadTexts:
    f3PrivilegeChangeEntry.setStatus("current")


class _F3PrivilegeChangeId_Type(Unsigned32):
    """Custom type f3PrivilegeChangeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_F3PrivilegeChangeId_Type.__name__ = "Unsigned32"
_F3PrivilegeChangeId_Object = MibTableColumn
f3PrivilegeChangeId = _F3PrivilegeChangeId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 1),
    _F3PrivilegeChangeId_Type()
)
f3PrivilegeChangeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PrivilegeChangeId.setStatus("current")
_F3PrivilegeChangeUserName_Type = SnmpAdminString
_F3PrivilegeChangeUserName_Object = MibTableColumn
f3PrivilegeChangeUserName = _F3PrivilegeChangeUserName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 2),
    _F3PrivilegeChangeUserName_Type()
)
f3PrivilegeChangeUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeUserName.setStatus("current")
_F3PrivilegeChangeIpv4Address_Type = IpAddress
_F3PrivilegeChangeIpv4Address_Object = MibTableColumn
f3PrivilegeChangeIpv4Address = _F3PrivilegeChangeIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 3),
    _F3PrivilegeChangeIpv4Address_Type()
)
f3PrivilegeChangeIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeIpv4Address.setStatus("current")
_F3PrivilegeChangeIpv6Address_Type = Ipv6Address
_F3PrivilegeChangeIpv6Address_Object = MibTableColumn
f3PrivilegeChangeIpv6Address = _F3PrivilegeChangeIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 4),
    _F3PrivilegeChangeIpv6Address_Type()
)
f3PrivilegeChangeIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeIpv6Address.setStatus("current")
_F3PrivilegeChangeTerminalIpv4Address_Type = IpAddress
_F3PrivilegeChangeTerminalIpv4Address_Object = MibTableColumn
f3PrivilegeChangeTerminalIpv4Address = _F3PrivilegeChangeTerminalIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 5),
    _F3PrivilegeChangeTerminalIpv4Address_Type()
)
f3PrivilegeChangeTerminalIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeTerminalIpv4Address.setStatus("current")
_F3PrivilegeChangeTerminalIpv6Address_Type = Ipv6Address
_F3PrivilegeChangeTerminalIpv6Address_Object = MibTableColumn
f3PrivilegeChangeTerminalIpv6Address = _F3PrivilegeChangeTerminalIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 6),
    _F3PrivilegeChangeTerminalIpv6Address_Type()
)
f3PrivilegeChangeTerminalIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeTerminalIpv6Address.setStatus("current")
_F3PrivilegeChangeInterface_Type = UserInterfaceType
_F3PrivilegeChangeInterface_Object = MibTableColumn
f3PrivilegeChangeInterface = _F3PrivilegeChangeInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 7),
    _F3PrivilegeChangeInterface_Type()
)
f3PrivilegeChangeInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeInterface.setStatus("current")
_F3PrivilegeChangeCurrentPrivilege_Type = CmSecurityPrivLevel
_F3PrivilegeChangeCurrentPrivilege_Object = MibTableColumn
f3PrivilegeChangeCurrentPrivilege = _F3PrivilegeChangeCurrentPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 8),
    _F3PrivilegeChangeCurrentPrivilege_Type()
)
f3PrivilegeChangeCurrentPrivilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeCurrentPrivilege.setStatus("current")
_F3PrivilegeChangeRequestedPrivilege_Type = CmSecurityPrivLevel
_F3PrivilegeChangeRequestedPrivilege_Object = MibTableColumn
f3PrivilegeChangeRequestedPrivilege = _F3PrivilegeChangeRequestedPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 9),
    _F3PrivilegeChangeRequestedPrivilege_Type()
)
f3PrivilegeChangeRequestedPrivilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeRequestedPrivilege.setStatus("current")


class _F3PrivilegeChangeDuration_Type(Unsigned32):
    """Custom type f3PrivilegeChangeDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 480),
    )


_F3PrivilegeChangeDuration_Type.__name__ = "Unsigned32"
_F3PrivilegeChangeDuration_Object = MibTableColumn
f3PrivilegeChangeDuration = _F3PrivilegeChangeDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 10),
    _F3PrivilegeChangeDuration_Type()
)
f3PrivilegeChangeDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeDuration.setStatus("current")
if mibBuilder.loadTexts:
    f3PrivilegeChangeDuration.setUnits("minutes")
_F3PrivilegeChangeAction_Type = PrivilegeRequestAction
_F3PrivilegeChangeAction_Object = MibTableColumn
f3PrivilegeChangeAction = _F3PrivilegeChangeAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 11),
    _F3PrivilegeChangeAction_Type()
)
f3PrivilegeChangeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PrivilegeChangeAction.setStatus("current")
_F3PrivilegeChangeState_Type = PrivilegeRequestState
_F3PrivilegeChangeState_Object = MibTableColumn
f3PrivilegeChangeState = _F3PrivilegeChangeState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 12),
    _F3PrivilegeChangeState_Type()
)
f3PrivilegeChangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeState.setStatus("current")
_F3PrivilegeChangeRemainingTime_Type = Unsigned32
_F3PrivilegeChangeRemainingTime_Object = MibTableColumn
f3PrivilegeChangeRemainingTime = _F3PrivilegeChangeRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 13),
    _F3PrivilegeChangeRemainingTime_Type()
)
f3PrivilegeChangeRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeRemainingTime.setStatus("current")
if mibBuilder.loadTexts:
    f3PrivilegeChangeRemainingTime.setUnits("seconds")
_F3PrivilegeChangeRemoteName_Type = SnmpAdminString
_F3PrivilegeChangeRemoteName_Object = MibTableColumn
f3PrivilegeChangeRemoteName = _F3PrivilegeChangeRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 14),
    _F3PrivilegeChangeRemoteName_Type()
)
f3PrivilegeChangeRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeRemoteName.setStatus("current")
_F3UserPrivMgmtControl_Type = TruthValue
_F3UserPrivMgmtControl_Object = MibScalar
f3UserPrivMgmtControl = _F3UserPrivMgmtControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 16),
    _F3UserPrivMgmtControl_Type()
)
f3UserPrivMgmtControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3UserPrivMgmtControl.setStatus("current")


class _F3UserPrivRspTimeout_Type(Integer32):
    """Custom type f3UserPrivRspTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_F3UserPrivRspTimeout_Type.__name__ = "Integer32"
_F3UserPrivRspTimeout_Object = MibScalar
f3UserPrivRspTimeout = _F3UserPrivRspTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 17),
    _F3UserPrivRspTimeout_Type()
)
f3UserPrivRspTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3UserPrivRspTimeout.setStatus("current")
if mibBuilder.loadTexts:
    f3UserPrivRspTimeout.setUnits("minutes")
_F3RadiusSendVendorAvpEnabled_Type = TruthValue
_F3RadiusSendVendorAvpEnabled_Object = MibScalar
f3RadiusSendVendorAvpEnabled = _F3RadiusSendVendorAvpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 18),
    _F3RadiusSendVendorAvpEnabled_Type()
)
f3RadiusSendVendorAvpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3RadiusSendVendorAvpEnabled.setStatus("current")
_F3RadiusRealm_Type = DisplayString
_F3RadiusRealm_Object = MibScalar
f3RadiusRealm = _F3RadiusRealm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 19),
    _F3RadiusRealm_Type()
)
f3RadiusRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3RadiusRealm.setStatus("current")
_CmIcmpV4Objects_ObjectIdentity = ObjectIdentity
cmIcmpV4Objects = _CmIcmpV4Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 20)
)


class _IcmpV4Filter_Type(Integer32):
    """Custom type icmpV4Filter based on Integer32"""
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


_IcmpV4Filter_Type.__name__ = "Integer32"
_IcmpV4Filter_Object = MibScalar
icmpV4Filter = _IcmpV4Filter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 20, 1),
    _IcmpV4Filter_Type()
)
icmpV4Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpV4Filter.setStatus("current")


class _IcmpV4DropEchoRequests_Type(Integer32):
    """Custom type icmpV4DropEchoRequests based on Integer32"""
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


_IcmpV4DropEchoRequests_Type.__name__ = "Integer32"
_IcmpV4DropEchoRequests_Object = MibScalar
icmpV4DropEchoRequests = _IcmpV4DropEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 20, 2),
    _IcmpV4DropEchoRequests_Type()
)
icmpV4DropEchoRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpV4DropEchoRequests.setStatus("current")
_CmIcmpV6Objects_ObjectIdentity = ObjectIdentity
cmIcmpV6Objects = _CmIcmpV6Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 21)
)


class _IcmpV6Filter_Type(Integer32):
    """Custom type icmpV6Filter based on Integer32"""
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


_IcmpV6Filter_Type.__name__ = "Integer32"
_IcmpV6Filter_Object = MibScalar
icmpV6Filter = _IcmpV6Filter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 21, 1),
    _IcmpV6Filter_Type()
)
icmpV6Filter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpV6Filter.setStatus("current")


class _IcmpV6DropEchoRequests_Type(Integer32):
    """Custom type icmpV6DropEchoRequests based on Integer32"""
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


_IcmpV6DropEchoRequests_Type.__name__ = "Integer32"
_IcmpV6DropEchoRequests_Object = MibScalar
icmpV6DropEchoRequests = _IcmpV6DropEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 21, 2),
    _IcmpV6DropEchoRequests_Type()
)
icmpV6DropEchoRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpV6DropEchoRequests.setStatus("current")


class _IcmpV6DropNeighborSolicitation_Type(Integer32):
    """Custom type icmpV6DropNeighborSolicitation based on Integer32"""
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


_IcmpV6DropNeighborSolicitation_Type.__name__ = "Integer32"
_IcmpV6DropNeighborSolicitation_Object = MibScalar
icmpV6DropNeighborSolicitation = _IcmpV6DropNeighborSolicitation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 21, 3),
    _IcmpV6DropNeighborSolicitation_Type()
)
icmpV6DropNeighborSolicitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpV6DropNeighborSolicitation.setStatus("current")


class _IcmpV6DropRouterAdvertisement_Type(Integer32):
    """Custom type icmpV6DropRouterAdvertisement based on Integer32"""
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


_IcmpV6DropRouterAdvertisement_Type.__name__ = "Integer32"
_IcmpV6DropRouterAdvertisement_Object = MibScalar
icmpV6DropRouterAdvertisement = _IcmpV6DropRouterAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 21, 4),
    _IcmpV6DropRouterAdvertisement_Type()
)
icmpV6DropRouterAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpV6DropRouterAdvertisement.setStatus("current")


class _IcmpV6DropNeighborAdvertisement_Type(Integer32):
    """Custom type icmpV6DropNeighborAdvertisement based on Integer32"""
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


_IcmpV6DropNeighborAdvertisement_Type.__name__ = "Integer32"
_IcmpV6DropNeighborAdvertisement_Object = MibScalar
icmpV6DropNeighborAdvertisement = _IcmpV6DropNeighborAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 21, 5),
    _IcmpV6DropNeighborAdvertisement_Type()
)
icmpV6DropNeighborAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpV6DropNeighborAdvertisement.setStatus("current")


class _IcmpV6DropRouterSolicitation_Type(Integer32):
    """Custom type icmpV6DropRouterSolicitation based on Integer32"""
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


_IcmpV6DropRouterSolicitation_Type.__name__ = "Integer32"
_IcmpV6DropRouterSolicitation_Object = MibScalar
icmpV6DropRouterSolicitation = _IcmpV6DropRouterSolicitation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 21, 6),
    _IcmpV6DropRouterSolicitation_Type()
)
icmpV6DropRouterSolicitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpV6DropRouterSolicitation.setStatus("current")


class _CmAnonymizeLogTimeInDays_Type(Integer32):
    """Custom type cmAnonymizeLogTimeInDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1096),
    )


_CmAnonymizeLogTimeInDays_Type.__name__ = "Integer32"
_CmAnonymizeLogTimeInDays_Object = MibScalar
cmAnonymizeLogTimeInDays = _CmAnonymizeLogTimeInDays_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 22),
    _CmAnonymizeLogTimeInDays_Type()
)
cmAnonymizeLogTimeInDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAnonymizeLogTimeInDays.setStatus("current")
_F3FipsObjects_ObjectIdentity = ObjectIdentity
f3FipsObjects = _F3FipsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 23)
)
_F3FipsOperationMode_Type = TruthValue
_F3FipsOperationMode_Object = MibScalar
f3FipsOperationMode = _F3FipsOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 23, 1),
    _F3FipsOperationMode_Type()
)
f3FipsOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FipsOperationMode.setStatus("current")
_F3FipsSecuritySelfTestFailureCount_Type = Unsigned32
_F3FipsSecuritySelfTestFailureCount_Object = MibScalar
f3FipsSecuritySelfTestFailureCount = _F3FipsSecuritySelfTestFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 23, 2),
    _F3FipsSecuritySelfTestFailureCount_Type()
)
f3FipsSecuritySelfTestFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FipsSecuritySelfTestFailureCount.setStatus("current")
_F3FipsSecuritySelfTestResult_Type = SecuritySelfTestResult
_F3FipsSecuritySelfTestResult_Object = MibScalar
f3FipsSecuritySelfTestResult = _F3FipsSecuritySelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 23, 3),
    _F3FipsSecuritySelfTestResult_Type()
)
f3FipsSecuritySelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FipsSecuritySelfTestResult.setStatus("current")
_F3FipsSecuritySelfTestStatus_Type = SecuritySelfTestStatus
_F3FipsSecuritySelfTestStatus_Object = MibScalar
f3FipsSecuritySelfTestStatus = _F3FipsSecuritySelfTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 23, 4),
    _F3FipsSecuritySelfTestStatus_Type()
)
f3FipsSecuritySelfTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FipsSecuritySelfTestStatus.setStatus("current")


class _F3FipsAction_Type(Integer32):
    """Custom type f3FipsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("zeroize", 1),
          ("startSecSelfTest", 2))
    )


_F3FipsAction_Type.__name__ = "Integer32"
_F3FipsAction_Object = MibScalar
f3FipsAction = _F3FipsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 23, 5),
    _F3FipsAction_Type()
)
f3FipsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FipsAction.setStatus("current")
_F3Sso2faControl_Type = TruthValue
_F3Sso2faControl_Object = MibScalar
f3Sso2faControl = _F3Sso2faControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 24),
    _F3Sso2faControl_Type()
)
f3Sso2faControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Sso2faControl.setStatus("current")
_F3SslCertificateObjects_ObjectIdentity = ObjectIdentity
f3SslCertificateObjects = _F3SslCertificateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 25)
)


class _F3HttpsSslCertExpNotifPeriod_Type(Unsigned32):
    """Custom type f3HttpsSslCertExpNotifPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_F3HttpsSslCertExpNotifPeriod_Type.__name__ = "Unsigned32"
_F3HttpsSslCertExpNotifPeriod_Object = MibScalar
f3HttpsSslCertExpNotifPeriod = _F3HttpsSslCertExpNotifPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 25, 1),
    _F3HttpsSslCertExpNotifPeriod_Type()
)
f3HttpsSslCertExpNotifPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3HttpsSslCertExpNotifPeriod.setStatus("current")


class _F3HttpsSslKeyPair_Type(DisplayString):
    """Custom type f3HttpsSslKeyPair based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_F3HttpsSslKeyPair_Type.__name__ = "DisplayString"
_F3HttpsSslKeyPair_Object = MibScalar
f3HttpsSslKeyPair = _F3HttpsSslKeyPair_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 25, 2),
    _F3HttpsSslKeyPair_Type()
)
f3HttpsSslKeyPair.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3HttpsSslKeyPair.setStatus("current")
_F3SslCertificateAction_Type = SslCertificateAction
_F3SslCertificateAction_Object = MibScalar
f3SslCertificateAction = _F3SslCertificateAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 25, 3),
    _F3SslCertificateAction_Type()
)
f3SslCertificateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SslCertificateAction.setStatus("current")


class _F3SslCertificateActionPairName_Type(DisplayString):
    """Custom type f3SslCertificateActionPairName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3SslCertificateActionPairName_Type.__name__ = "DisplayString"
_F3SslCertificateActionPairName_Object = MibScalar
f3SslCertificateActionPairName = _F3SslCertificateActionPairName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 25, 4),
    _F3SslCertificateActionPairName_Type()
)
f3SslCertificateActionPairName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SslCertificateActionPairName.setStatus("current")
_F3SslCertificatePrivateKeyPairTable_Object = MibTable
f3SslCertificatePrivateKeyPairTable = _F3SslCertificatePrivateKeyPairTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 25, 5)
)
if mibBuilder.loadTexts:
    f3SslCertificatePrivateKeyPairTable.setStatus("current")
_F3SslCertificatePrivateKeyPairEntry_Object = MibTableRow
f3SslCertificatePrivateKeyPairEntry = _F3SslCertificatePrivateKeyPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 25, 5, 1)
)
f3SslCertificatePrivateKeyPairEntry.setIndexNames(
    (0, "CM-SECURITY-MIB", "f3SslCertificatePrivateKeyPairName"),
)
if mibBuilder.loadTexts:
    f3SslCertificatePrivateKeyPairEntry.setStatus("current")


class _F3SslCertificatePrivateKeyPairName_Type(DisplayString):
    """Custom type f3SslCertificatePrivateKeyPairName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_F3SslCertificatePrivateKeyPairName_Type.__name__ = "DisplayString"
_F3SslCertificatePrivateKeyPairName_Object = MibTableColumn
f3SslCertificatePrivateKeyPairName = _F3SslCertificatePrivateKeyPairName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 25, 5, 1, 1),
    _F3SslCertificatePrivateKeyPairName_Type()
)
f3SslCertificatePrivateKeyPairName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3SslCertificatePrivateKeyPairName.setStatus("current")


class _F3SslCertificatePrivateKeyPairSslCertificate_Type(DisplayString):
    """Custom type f3SslCertificatePrivateKeyPairSslCertificate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_F3SslCertificatePrivateKeyPairSslCertificate_Type.__name__ = "DisplayString"
_F3SslCertificatePrivateKeyPairSslCertificate_Object = MibTableColumn
f3SslCertificatePrivateKeyPairSslCertificate = _F3SslCertificatePrivateKeyPairSslCertificate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 25, 5, 1, 2),
    _F3SslCertificatePrivateKeyPairSslCertificate_Type()
)
f3SslCertificatePrivateKeyPairSslCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SslCertificatePrivateKeyPairSslCertificate.setStatus("current")
_F3SslCertificatePrivateKeyPairPrivateKeyPresent_Type = TruthValue
_F3SslCertificatePrivateKeyPairPrivateKeyPresent_Object = MibTableColumn
f3SslCertificatePrivateKeyPairPrivateKeyPresent = _F3SslCertificatePrivateKeyPairPrivateKeyPresent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 25, 5, 1, 3),
    _F3SslCertificatePrivateKeyPairPrivateKeyPresent_Type()
)
f3SslCertificatePrivateKeyPairPrivateKeyPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SslCertificatePrivateKeyPairPrivateKeyPresent.setStatus("current")


class _F3SslCertificatePrivateKeyPairRsaKeyPairName_Type(DisplayString):
    """Custom type f3SslCertificatePrivateKeyPairRsaKeyPairName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3SslCertificatePrivateKeyPairRsaKeyPairName_Type.__name__ = "DisplayString"
_F3SslCertificatePrivateKeyPairRsaKeyPairName_Object = MibTableColumn
f3SslCertificatePrivateKeyPairRsaKeyPairName = _F3SslCertificatePrivateKeyPairRsaKeyPairName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 25, 5, 1, 4),
    _F3SslCertificatePrivateKeyPairRsaKeyPairName_Type()
)
f3SslCertificatePrivateKeyPairRsaKeyPairName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SslCertificatePrivateKeyPairRsaKeyPairName.setStatus("current")
_F3SslCertificatePrivateKeyPairCertificateType_Type = CertificateType
_F3SslCertificatePrivateKeyPairCertificateType_Object = MibTableColumn
f3SslCertificatePrivateKeyPairCertificateType = _F3SslCertificatePrivateKeyPairCertificateType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 25, 5, 1, 5),
    _F3SslCertificatePrivateKeyPairCertificateType_Type()
)
f3SslCertificatePrivateKeyPairCertificateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SslCertificatePrivateKeyPairCertificateType.setStatus("current")
_F3SslCertificatePrivateKeyPairCertificateStatus_Type = CertificateStatus
_F3SslCertificatePrivateKeyPairCertificateStatus_Object = MibTableColumn
f3SslCertificatePrivateKeyPairCertificateStatus = _F3SslCertificatePrivateKeyPairCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 25, 5, 1, 6),
    _F3SslCertificatePrivateKeyPairCertificateStatus_Type()
)
f3SslCertificatePrivateKeyPairCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SslCertificatePrivateKeyPairCertificateStatus.setStatus("current")
_F3SslCertificatePrivateKeyPairAction_Type = SslCertificatePrivateKeyPairAction
_F3SslCertificatePrivateKeyPairAction_Object = MibTableColumn
f3SslCertificatePrivateKeyPairAction = _F3SslCertificatePrivateKeyPairAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 25, 5, 1, 7),
    _F3SslCertificatePrivateKeyPairAction_Type()
)
f3SslCertificatePrivateKeyPairAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SslCertificatePrivateKeyPairAction.setStatus("current")


class _F3SslCertificateActionKeyName_Type(DisplayString):
    """Custom type f3SslCertificateActionKeyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3SslCertificateActionKeyName_Type.__name__ = "DisplayString"
_F3SslCertificateActionKeyName_Object = MibScalar
f3SslCertificateActionKeyName = _F3SslCertificateActionKeyName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 25, 6),
    _F3SslCertificateActionKeyName_Type()
)
f3SslCertificateActionKeyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SslCertificateActionKeyName.setStatus("current")
_F3RsaKeyPairObjects_ObjectIdentity = ObjectIdentity
f3RsaKeyPairObjects = _F3RsaKeyPairObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 26)
)
_F3RsaKeyPairAction_Type = RsaKeyPairAction
_F3RsaKeyPairAction_Object = MibScalar
f3RsaKeyPairAction = _F3RsaKeyPairAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 26, 1),
    _F3RsaKeyPairAction_Type()
)
f3RsaKeyPairAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3RsaKeyPairAction.setStatus("current")


class _F3RsaKeyPairActionName_Type(DisplayString):
    """Custom type f3RsaKeyPairActionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3RsaKeyPairActionName_Type.__name__ = "DisplayString"
_F3RsaKeyPairActionName_Object = MibScalar
f3RsaKeyPairActionName = _F3RsaKeyPairActionName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 26, 2),
    _F3RsaKeyPairActionName_Type()
)
f3RsaKeyPairActionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3RsaKeyPairActionName.setStatus("current")
_F3RsaKeyPairActionLength_Type = RsaKeyLengthType
_F3RsaKeyPairActionLength_Object = MibScalar
f3RsaKeyPairActionLength = _F3RsaKeyPairActionLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 26, 3),
    _F3RsaKeyPairActionLength_Type()
)
f3RsaKeyPairActionLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3RsaKeyPairActionLength.setStatus("current")
_F3RsaKeyPairTable_Object = MibTable
f3RsaKeyPairTable = _F3RsaKeyPairTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 26, 4)
)
if mibBuilder.loadTexts:
    f3RsaKeyPairTable.setStatus("current")
_F3RsaKeyPairEntry_Object = MibTableRow
f3RsaKeyPairEntry = _F3RsaKeyPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 26, 4, 1)
)
f3RsaKeyPairEntry.setIndexNames(
    (0, "CM-SECURITY-MIB", "f3RsaKeyPairName"),
)
if mibBuilder.loadTexts:
    f3RsaKeyPairEntry.setStatus("current")


class _F3RsaKeyPairName_Type(DisplayString):
    """Custom type f3RsaKeyPairName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_F3RsaKeyPairName_Type.__name__ = "DisplayString"
_F3RsaKeyPairName_Object = MibTableColumn
f3RsaKeyPairName = _F3RsaKeyPairName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 26, 4, 1, 1),
    _F3RsaKeyPairName_Type()
)
f3RsaKeyPairName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3RsaKeyPairName.setStatus("current")


class _F3RsaKeyPairPublicKey_Type(DisplayString):
    """Custom type f3RsaKeyPairPublicKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_F3RsaKeyPairPublicKey_Type.__name__ = "DisplayString"
_F3RsaKeyPairPublicKey_Object = MibTableColumn
f3RsaKeyPairPublicKey = _F3RsaKeyPairPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 26, 4, 1, 2),
    _F3RsaKeyPairPublicKey_Type()
)
f3RsaKeyPairPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3RsaKeyPairPublicKey.setStatus("current")
_F3CertSigningRequestObjects_ObjectIdentity = ObjectIdentity
f3CertSigningRequestObjects = _F3CertSigningRequestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27)
)
_F3CsrAction_Type = CsrAction
_F3CsrAction_Object = MibScalar
f3CsrAction = _F3CsrAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 1),
    _F3CsrAction_Type()
)
f3CsrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CsrAction.setStatus("current")


class _F3CsrActionCsrName_Type(DisplayString):
    """Custom type f3CsrActionCsrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3CsrActionCsrName_Type.__name__ = "DisplayString"
_F3CsrActionCsrName_Object = MibScalar
f3CsrActionCsrName = _F3CsrActionCsrName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 2),
    _F3CsrActionCsrName_Type()
)
f3CsrActionCsrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CsrActionCsrName.setStatus("current")


class _F3CsrActionRsaKeyName_Type(DisplayString):
    """Custom type f3CsrActionRsaKeyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3CsrActionRsaKeyName_Type.__name__ = "DisplayString"
_F3CsrActionRsaKeyName_Object = MibScalar
f3CsrActionRsaKeyName = _F3CsrActionRsaKeyName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 3),
    _F3CsrActionRsaKeyName_Type()
)
f3CsrActionRsaKeyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CsrActionRsaKeyName.setStatus("current")


class _F3CsrActionCountry_Type(DisplayString):
    """Custom type f3CsrActionCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3CsrActionCountry_Type.__name__ = "DisplayString"
_F3CsrActionCountry_Object = MibScalar
f3CsrActionCountry = _F3CsrActionCountry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 4),
    _F3CsrActionCountry_Type()
)
f3CsrActionCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CsrActionCountry.setStatus("current")


class _F3CsrActionState_Type(DisplayString):
    """Custom type f3CsrActionState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3CsrActionState_Type.__name__ = "DisplayString"
_F3CsrActionState_Object = MibScalar
f3CsrActionState = _F3CsrActionState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 5),
    _F3CsrActionState_Type()
)
f3CsrActionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CsrActionState.setStatus("current")


class _F3CsrActionLocality_Type(DisplayString):
    """Custom type f3CsrActionLocality based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3CsrActionLocality_Type.__name__ = "DisplayString"
_F3CsrActionLocality_Object = MibScalar
f3CsrActionLocality = _F3CsrActionLocality_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 6),
    _F3CsrActionLocality_Type()
)
f3CsrActionLocality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CsrActionLocality.setStatus("current")


class _F3CsrActionOrganization_Type(DisplayString):
    """Custom type f3CsrActionOrganization based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3CsrActionOrganization_Type.__name__ = "DisplayString"
_F3CsrActionOrganization_Object = MibScalar
f3CsrActionOrganization = _F3CsrActionOrganization_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 7),
    _F3CsrActionOrganization_Type()
)
f3CsrActionOrganization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CsrActionOrganization.setStatus("current")


class _F3CsrActionOrganizationUnit_Type(DisplayString):
    """Custom type f3CsrActionOrganizationUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3CsrActionOrganizationUnit_Type.__name__ = "DisplayString"
_F3CsrActionOrganizationUnit_Object = MibScalar
f3CsrActionOrganizationUnit = _F3CsrActionOrganizationUnit_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 8),
    _F3CsrActionOrganizationUnit_Type()
)
f3CsrActionOrganizationUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CsrActionOrganizationUnit.setStatus("current")


class _F3CsrActionCommonName_Type(DisplayString):
    """Custom type f3CsrActionCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3CsrActionCommonName_Type.__name__ = "DisplayString"
_F3CsrActionCommonName_Object = MibScalar
f3CsrActionCommonName = _F3CsrActionCommonName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 9),
    _F3CsrActionCommonName_Type()
)
f3CsrActionCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CsrActionCommonName.setStatus("current")


class _F3CsrActionEmail_Type(DisplayString):
    """Custom type f3CsrActionEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3CsrActionEmail_Type.__name__ = "DisplayString"
_F3CsrActionEmail_Object = MibScalar
f3CsrActionEmail = _F3CsrActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 10),
    _F3CsrActionEmail_Type()
)
f3CsrActionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CsrActionEmail.setStatus("current")


class _F3CsrActionSerialNumber_Type(DisplayString):
    """Custom type f3CsrActionSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3CsrActionSerialNumber_Type.__name__ = "DisplayString"
_F3CsrActionSerialNumber_Object = MibScalar
f3CsrActionSerialNumber = _F3CsrActionSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 11),
    _F3CsrActionSerialNumber_Type()
)
f3CsrActionSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CsrActionSerialNumber.setStatus("current")


class _F3CsrActionAlternativeName_Type(DisplayString):
    """Custom type f3CsrActionAlternativeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3CsrActionAlternativeName_Type.__name__ = "DisplayString"
_F3CsrActionAlternativeName_Object = MibScalar
f3CsrActionAlternativeName = _F3CsrActionAlternativeName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 12),
    _F3CsrActionAlternativeName_Type()
)
f3CsrActionAlternativeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CsrActionAlternativeName.setStatus("current")
_F3CertSigningRequestTable_Object = MibTable
f3CertSigningRequestTable = _F3CertSigningRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 13)
)
if mibBuilder.loadTexts:
    f3CertSigningRequestTable.setStatus("current")
_F3CertSigningRequestEntry_Object = MibTableRow
f3CertSigningRequestEntry = _F3CertSigningRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 13, 1)
)
f3CertSigningRequestEntry.setIndexNames(
    (0, "CM-SECURITY-MIB", "f3CertSigningRequestName"),
)
if mibBuilder.loadTexts:
    f3CertSigningRequestEntry.setStatus("current")


class _F3CertSigningRequestName_Type(DisplayString):
    """Custom type f3CertSigningRequestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_F3CertSigningRequestName_Type.__name__ = "DisplayString"
_F3CertSigningRequestName_Object = MibTableColumn
f3CertSigningRequestName = _F3CertSigningRequestName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 13, 1, 1),
    _F3CertSigningRequestName_Type()
)
f3CertSigningRequestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3CertSigningRequestName.setStatus("current")


class _F3CertSigningRequestRsaKeyPairName_Type(DisplayString):
    """Custom type f3CertSigningRequestRsaKeyPairName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_F3CertSigningRequestRsaKeyPairName_Type.__name__ = "DisplayString"
_F3CertSigningRequestRsaKeyPairName_Object = MibTableColumn
f3CertSigningRequestRsaKeyPairName = _F3CertSigningRequestRsaKeyPairName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 13, 1, 2),
    _F3CertSigningRequestRsaKeyPairName_Type()
)
f3CertSigningRequestRsaKeyPairName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CertSigningRequestRsaKeyPairName.setStatus("current")


class _F3CertSigningRequestCsrData_Type(DisplayString):
    """Custom type f3CertSigningRequestCsrData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_F3CertSigningRequestCsrData_Type.__name__ = "DisplayString"
_F3CertSigningRequestCsrData_Object = MibTableColumn
f3CertSigningRequestCsrData = _F3CertSigningRequestCsrData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 13, 1, 3),
    _F3CertSigningRequestCsrData_Type()
)
f3CertSigningRequestCsrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CertSigningRequestCsrData.setStatus("current")
_F3CertSigningRequestAutoEnrollmentStatus_Type = AutoEnrollmentStatus
_F3CertSigningRequestAutoEnrollmentStatus_Object = MibTableColumn
f3CertSigningRequestAutoEnrollmentStatus = _F3CertSigningRequestAutoEnrollmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 27, 13, 1, 4),
    _F3CertSigningRequestAutoEnrollmentStatus_Type()
)
f3CertSigningRequestAutoEnrollmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CertSigningRequestAutoEnrollmentStatus.setStatus("current")
_F3NasIpAddressType_Type = NasIpAddressType
_F3NasIpAddressType_Object = MibScalar
f3NasIpAddressType = _F3NasIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 28),
    _F3NasIpAddressType_Type()
)
f3NasIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NasIpAddressType.setStatus("current")
_F3CaProfileTable_Object = MibTable
f3CaProfileTable = _F3CaProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 29)
)
if mibBuilder.loadTexts:
    f3CaProfileTable.setStatus("current")
_F3CaProfileEntry_Object = MibTableRow
f3CaProfileEntry = _F3CaProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 29, 1)
)
f3CaProfileEntry.setIndexNames(
    (0, "CM-SECURITY-MIB", "f3CaProfileIndex"),
)
if mibBuilder.loadTexts:
    f3CaProfileEntry.setStatus("current")


class _F3CaProfileIndex_Type(Unsigned32):
    """Custom type f3CaProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3CaProfileIndex_Type.__name__ = "Unsigned32"
_F3CaProfileIndex_Object = MibTableColumn
f3CaProfileIndex = _F3CaProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 29, 1, 1),
    _F3CaProfileIndex_Type()
)
f3CaProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3CaProfileIndex.setStatus("current")


class _F3CaProfileName_Type(DisplayString):
    """Custom type f3CaProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3CaProfileName_Type.__name__ = "DisplayString"
_F3CaProfileName_Object = MibTableColumn
f3CaProfileName = _F3CaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 29, 1, 2),
    _F3CaProfileName_Type()
)
f3CaProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3CaProfileName.setStatus("current")


class _F3CaProfileEnrollmentProtocol_Type(CertificateEnrollmentProtocol):
    """Custom type f3CaProfileEnrollmentProtocol based on CertificateEnrollmentProtocol"""
    defaultValue = 1


_F3CaProfileEnrollmentProtocol_Type.__name__ = "CertificateEnrollmentProtocol"
_F3CaProfileEnrollmentProtocol_Object = MibTableColumn
f3CaProfileEnrollmentProtocol = _F3CaProfileEnrollmentProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 29, 1, 3),
    _F3CaProfileEnrollmentProtocol_Type()
)
f3CaProfileEnrollmentProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3CaProfileEnrollmentProtocol.setStatus("current")


class _F3CaProfileHttpPort_Type(Unsigned32):
    """Custom type f3CaProfileHttpPort based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3CaProfileHttpPort_Type.__name__ = "Unsigned32"
_F3CaProfileHttpPort_Object = MibTableColumn
f3CaProfileHttpPort = _F3CaProfileHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 29, 1, 4),
    _F3CaProfileHttpPort_Type()
)
f3CaProfileHttpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3CaProfileHttpPort.setStatus("current")


class _F3CaProfileAutoRenewalControl_Type(TruthValue):
    """Custom type f3CaProfileAutoRenewalControl based on TruthValue"""
    defaultValue = 1


_F3CaProfileAutoRenewalControl_Type.__name__ = "TruthValue"
_F3CaProfileAutoRenewalControl_Object = MibTableColumn
f3CaProfileAutoRenewalControl = _F3CaProfileAutoRenewalControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 29, 1, 5),
    _F3CaProfileAutoRenewalControl_Type()
)
f3CaProfileAutoRenewalControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3CaProfileAutoRenewalControl.setStatus("current")


class _F3CaProfileRenewalPercentLifetime_Type(Unsigned32):
    """Custom type f3CaProfileRenewalPercentLifetime based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_F3CaProfileRenewalPercentLifetime_Type.__name__ = "Unsigned32"
_F3CaProfileRenewalPercentLifetime_Object = MibTableColumn
f3CaProfileRenewalPercentLifetime = _F3CaProfileRenewalPercentLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 29, 1, 6),
    _F3CaProfileRenewalPercentLifetime_Type()
)
f3CaProfileRenewalPercentLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3CaProfileRenewalPercentLifetime.setStatus("current")


class _F3CaProfileRenewalNewKeyPairGenControl_Type(TruthValue):
    """Custom type f3CaProfileRenewalNewKeyPairGenControl based on TruthValue"""
    defaultValue = 2


_F3CaProfileRenewalNewKeyPairGenControl_Type.__name__ = "TruthValue"
_F3CaProfileRenewalNewKeyPairGenControl_Object = MibTableColumn
f3CaProfileRenewalNewKeyPairGenControl = _F3CaProfileRenewalNewKeyPairGenControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 29, 1, 7),
    _F3CaProfileRenewalNewKeyPairGenControl_Type()
)
f3CaProfileRenewalNewKeyPairGenControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3CaProfileRenewalNewKeyPairGenControl.setStatus("current")
_F3CaProfileStorageType_Type = StorageType
_F3CaProfileStorageType_Object = MibTableColumn
f3CaProfileStorageType = _F3CaProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 29, 1, 8),
    _F3CaProfileStorageType_Type()
)
f3CaProfileStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3CaProfileStorageType.setStatus("current")
_F3CaProfileRowStatus_Type = RowStatus
_F3CaProfileRowStatus_Object = MibTableColumn
f3CaProfileRowStatus = _F3CaProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 29, 1, 9),
    _F3CaProfileRowStatus_Type()
)
f3CaProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3CaProfileRowStatus.setStatus("current")
_F3CaTable_Object = MibTable
f3CaTable = _F3CaTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 30)
)
if mibBuilder.loadTexts:
    f3CaTable.setStatus("current")
_F3CaEntry_Object = MibTableRow
f3CaEntry = _F3CaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 30, 1)
)
f3CaEntry.setIndexNames(
    (0, "CM-SECURITY-MIB", "f3CaName"),
)
if mibBuilder.loadTexts:
    f3CaEntry.setStatus("current")


class _F3CaName_Type(DisplayString):
    """Custom type f3CaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_F3CaName_Type.__name__ = "DisplayString"
_F3CaName_Object = MibTableColumn
f3CaName = _F3CaName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 30, 1, 1),
    _F3CaName_Type()
)
f3CaName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3CaName.setStatus("current")
_F3CaProfile_Type = VariablePointer
_F3CaProfile_Object = MibTableColumn
f3CaProfile = _F3CaProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 30, 1, 2),
    _F3CaProfile_Type()
)
f3CaProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3CaProfile.setStatus("current")


class _F3CaUrl_Type(DisplayString):
    """Custom type f3CaUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_F3CaUrl_Type.__name__ = "DisplayString"
_F3CaUrl_Object = MibTableColumn
f3CaUrl = _F3CaUrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 30, 1, 3),
    _F3CaUrl_Type()
)
f3CaUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3CaUrl.setStatus("current")


class _F3CaScepQueryMessage_Type(DisplayString):
    """Custom type f3CaScepQueryMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_F3CaScepQueryMessage_Type.__name__ = "DisplayString"
_F3CaScepQueryMessage_Object = MibScalar
f3CaScepQueryMessage = _F3CaScepQueryMessage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 30, 1, 4),
    _F3CaScepQueryMessage_Type()
)
f3CaScepQueryMessage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3CaScepQueryMessage.setStatus("current")


class _F3CaCertList_Type(DisplayString):
    """Custom type f3CaCertList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3CaCertList_Type.__name__ = "DisplayString"
_F3CaCertList_Object = MibTableColumn
f3CaCertList = _F3CaCertList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 30, 1, 5),
    _F3CaCertList_Type()
)
f3CaCertList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CaCertList.setStatus("current")
_F3CaRootCertStatus_Type = CaRootCertStatus
_F3CaRootCertStatus_Object = MibTableColumn
f3CaRootCertStatus = _F3CaRootCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 30, 1, 6),
    _F3CaRootCertStatus_Type()
)
f3CaRootCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CaRootCertStatus.setStatus("current")


class _F3CaLastCsr_Type(DisplayString):
    """Custom type f3CaLastCsr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3CaLastCsr_Type.__name__ = "DisplayString"
_F3CaLastCsr_Object = MibTableColumn
f3CaLastCsr = _F3CaLastCsr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 30, 1, 7),
    _F3CaLastCsr_Type()
)
f3CaLastCsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CaLastCsr.setStatus("current")
_F3CaAction_Type = CaAction
_F3CaAction_Object = MibTableColumn
f3CaAction = _F3CaAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 30, 1, 8),
    _F3CaAction_Type()
)
f3CaAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CaAction.setStatus("current")


class _F3CaActionCsrName_Type(DisplayString):
    """Custom type f3CaActionCsrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_F3CaActionCsrName_Type.__name__ = "DisplayString"
_F3CaActionCsrName_Object = MibTableColumn
f3CaActionCsrName = _F3CaActionCsrName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 30, 1, 9),
    _F3CaActionCsrName_Type()
)
f3CaActionCsrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CaActionCsrName.setStatus("current")


class _F3CaActionChallengePassword_Type(DisplayString):
    """Custom type f3CaActionChallengePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3CaActionChallengePassword_Type.__name__ = "DisplayString"
_F3CaActionChallengePassword_Object = MibTableColumn
f3CaActionChallengePassword = _F3CaActionChallengePassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 30, 1, 10),
    _F3CaActionChallengePassword_Type()
)
f3CaActionChallengePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CaActionChallengePassword.setStatus("current")
_F3CaStorageType_Type = StorageType
_F3CaStorageType_Object = MibTableColumn
f3CaStorageType = _F3CaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 30, 1, 11),
    _F3CaStorageType_Type()
)
f3CaStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3CaStorageType.setStatus("current")
_F3CaRowStatus_Type = RowStatus
_F3CaRowStatus_Object = MibTableColumn
f3CaRowStatus = _F3CaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 30, 1, 12),
    _F3CaRowStatus_Type()
)
f3CaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3CaRowStatus.setStatus("current")
_F3SshCipherStrengthHighControl_Type = TruthValue
_F3SshCipherStrengthHighControl_Object = MibScalar
f3SshCipherStrengthHighControl = _F3SshCipherStrengthHighControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 31),
    _F3SshCipherStrengthHighControl_Type()
)
f3SshCipherStrengthHighControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SshCipherStrengthHighControl.setStatus("current")
_CmSecurityConformance_ObjectIdentity = ObjectIdentity
cmSecurityConformance = _CmSecurityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 2)
)
_CmSecurityCompliances_ObjectIdentity = ObjectIdentity
cmSecurityCompliances = _CmSecurityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 2, 1)
)
_CmSecurityGroups_ObjectIdentity = ObjectIdentity
cmSecurityGroups = _CmSecurityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 2, 2)
)
_CmSecurityNotifications_ObjectIdentity = ObjectIdentity
cmSecurityNotifications = _CmSecurityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 3)
)
usmUserEntry.registerAugmentions(
    ("CM-SECURITY-MIB",
     "f3UsmUserEntry")
)
f3UsmUserEntry.setIndexNames(*usmUserEntry.getIndexNames())

# Managed Objects groups

cmSecurityObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 2, 2, 1)
)
cmSecurityObjectGroup.setObjects(
      *(("CM-SECURITY-MIB", "cmAuthProtocol"),
        ("CM-SECURITY-MIB", "cmAccessOrder"),
        ("CM-SECURITY-MIB", "cmAuthType"),
        ("CM-SECURITY-MIB", "cmNASIpAddress"),
        ("CM-SECURITY-MIB", "cmSecurityPolicyStrength"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerAccountingEnabled"),
        ("CM-SECURITY-MIB", "cmAnonymizeLogTimeInDays"),
        ("CM-SECURITY-MIB", "f3Sso2faControl"),
        ("CM-SECURITY-MIB", "f3NasIpAddressType"),
        ("CM-SECURITY-MIB", "f3SshCipherStrengthHighControl"),
        ("CM-SECURITY-MIB", "f3TacacsPrivLevelControlEnabled"),
        ("CM-SECURITY-MIB", "f3TacacsDefaultPrivLevel"),
        ("CM-SECURITY-MIB", "f3NasIpv6Addr"),
        ("CM-SECURITY-MIB", "f3SecurityTrapType"),
        ("CM-SECURITY-MIB", "f3SecurityTrapInfo"),
        ("CM-SECURITY-MIB", "cmSecurityUserName"),
        ("CM-SECURITY-MIB", "cmSecurityUserComment"),
        ("CM-SECURITY-MIB", "cmSecurityUserPrivLevel"),
        ("CM-SECURITY-MIB", "cmSecurityUserLoginTimeout"),
        ("CM-SECURITY-MIB", "cmSecurityUserNumFailedLoginAttempts"),
        ("CM-SECURITY-MIB", "cmSecurityUserLastLoginTime"),
        ("CM-SECURITY-MIB", "cmSecurityUserLockedout"),
        ("CM-SECURITY-MIB", "cmSecurityUserLastLockedoutTime"),
        ("CM-SECURITY-MIB", "cmSecurityUserCliPagingEnable"),
        ("CM-SECURITY-MIB", "cmSecurityUserRemoteUser"),
        ("CM-SECURITY-MIB", "cmSecurityUserPassword"),
        ("CM-SECURITY-MIB", "cmSecurityUserStorageType"),
        ("CM-SECURITY-MIB", "cmSecurityUserRowStatus"),
        ("CM-SECURITY-MIB", "cmSecurityUserAction"),
        ("CM-SECURITY-MIB", "cmSecurityCryptoPassword"),
        ("CM-SECURITY-MIB", "cmSecurityUserRemoteCryptoUser"),
        ("CM-SECURITY-MIB", "cmSecurityUserSso2fa"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerIndex"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerEnabled"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerOrder"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerIpAddress"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerPort"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerNumRetries"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerTimeout"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerSecret"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerAccountingPort"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerIpVersion"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerIpv6Addr"),
        ("CM-SECURITY-MIB", "f3UsmUserAccessType"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeUserName"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeIpv4Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeIpv6Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeTerminalIpv4Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeTerminalIpv6Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeInterface"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeCurrentPrivilege"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeRequestedPrivilege"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeDuration"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeAction"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeState"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeRemainingTime"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeRemoteName"),
        ("CM-SECURITY-MIB", "f3RadiusSendVendorAvpEnabled"),
        ("CM-SECURITY-MIB", "f3RadiusRealm"),
        ("CM-SECURITY-MIB", "icmpV4Filter"),
        ("CM-SECURITY-MIB", "icmpV4DropEchoRequests"),
        ("CM-SECURITY-MIB", "icmpV6Filter"),
        ("CM-SECURITY-MIB", "icmpV6DropEchoRequests"),
        ("CM-SECURITY-MIB", "icmpV6DropNeighborSolicitation"),
        ("CM-SECURITY-MIB", "icmpV6DropRouterAdvertisement"),
        ("CM-SECURITY-MIB", "icmpV6DropNeighborAdvertisement"),
        ("CM-SECURITY-MIB", "icmpV6DropRouterSolicitation"),
        ("CM-SECURITY-MIB", "f3FipsOperationMode"),
        ("CM-SECURITY-MIB", "f3FipsSecuritySelfTestFailureCount"),
        ("CM-SECURITY-MIB", "f3FipsSecuritySelfTestResult"),
        ("CM-SECURITY-MIB", "f3FipsSecuritySelfTestStatus"),
        ("CM-SECURITY-MIB", "f3FipsAction"),
        ("CM-SECURITY-MIB", "f3HttpsSslCertExpNotifPeriod"),
        ("CM-SECURITY-MIB", "f3HttpsSslKeyPair"),
        ("CM-SECURITY-MIB", "f3SslCertificateAction"),
        ("CM-SECURITY-MIB", "f3SslCertificateActionPairName"),
        ("CM-SECURITY-MIB", "f3SslCertificatePrivateKeyPairName"),
        ("CM-SECURITY-MIB", "f3SslCertificatePrivateKeyPairSslCertificate"),
        ("CM-SECURITY-MIB", "f3SslCertificatePrivateKeyPairPrivateKeyPresent"),
        ("CM-SECURITY-MIB", "f3RsaKeyPairName"),
        ("CM-SECURITY-MIB", "f3RsaKeyPairPublicKey"),
        ("CM-SECURITY-MIB", "f3RsaKeyPairAction"),
        ("CM-SECURITY-MIB", "f3RsaKeyPairActionName"),
        ("CM-SECURITY-MIB", "f3RsaKeyPairActionLength"),
        ("CM-SECURITY-MIB", "f3CsrAction"),
        ("CM-SECURITY-MIB", "f3CsrActionCsrName"),
        ("CM-SECURITY-MIB", "f3CsrActionRsaKeyName"),
        ("CM-SECURITY-MIB", "f3CsrActionCountry"),
        ("CM-SECURITY-MIB", "f3CsrActionState"),
        ("CM-SECURITY-MIB", "f3CsrActionLocality"),
        ("CM-SECURITY-MIB", "f3CsrActionOrganization"),
        ("CM-SECURITY-MIB", "f3CsrActionOrganizationUnit"),
        ("CM-SECURITY-MIB", "f3CsrActionCommonName"),
        ("CM-SECURITY-MIB", "f3CsrActionEmail"),
        ("CM-SECURITY-MIB", "f3CsrActionSerialNumber"),
        ("CM-SECURITY-MIB", "f3CsrActionAlternativeName"),
        ("CM-SECURITY-MIB", "f3CertSigningRequestName"),
        ("CM-SECURITY-MIB", "f3CertSigningRequestRsaKeyPairName"),
        ("CM-SECURITY-MIB", "f3CertSigningRequestCsrData"),
        ("CM-SECURITY-MIB", "f3CertSigningRequestAutoEnrollmentStatus"),
        ("CM-SECURITY-MIB", "f3SslCertificatePrivateKeyPairRsaKeyPairName"),
        ("CM-SECURITY-MIB", "f3SslCertificatePrivateKeyPairCertificateType"),
        ("CM-SECURITY-MIB", "f3SslCertificatePrivateKeyPairCertificateStatus"),
        ("CM-SECURITY-MIB", "f3SslCertificatePrivateKeyPairAction"),
        ("CM-SECURITY-MIB", "f3SslCertificateActionKeyName"),
        ("CM-SECURITY-MIB", "f3CaProfileName"),
        ("CM-SECURITY-MIB", "f3CaProfileEnrollmentProtocol"),
        ("CM-SECURITY-MIB", "f3CaProfileHttpPort"),
        ("CM-SECURITY-MIB", "f3CaProfileAutoRenewalControl"),
        ("CM-SECURITY-MIB", "f3CaProfileRenewalPercentLifetime"),
        ("CM-SECURITY-MIB", "f3CaProfileRenewalNewKeyPairGenControl"),
        ("CM-SECURITY-MIB", "f3CaProfileStorageType"),
        ("CM-SECURITY-MIB", "f3CaProfileRowStatus"),
        ("CM-SECURITY-MIB", "f3CaProfile"),
        ("CM-SECURITY-MIB", "f3CaScepQueryMessage"),
        ("CM-SECURITY-MIB", "f3CaUrl"),
        ("CM-SECURITY-MIB", "f3CaCertList"),
        ("CM-SECURITY-MIB", "f3CaRootCertStatus"),
        ("CM-SECURITY-MIB", "f3CaLastCsr"),
        ("CM-SECURITY-MIB", "f3CaAction"),
        ("CM-SECURITY-MIB", "f3CaActionCsrName"),
        ("CM-SECURITY-MIB", "f3CaActionChallengePassword"),
        ("CM-SECURITY-MIB", "f3CaStorageType"),
        ("CM-SECURITY-MIB", "f3CaRowStatus"))
)
if mibBuilder.loadTexts:
    cmSecurityObjectGroup.setStatus("current")


# Notification objects

f3SecurityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 3, 1)
)
if mibBuilder.loadTexts:
    f3SecurityTrap.setStatus(
        "current"
    )

f3PrivilegeChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 3, 2)
)
f3PrivilegeChangeTrap.setObjects(
      *(("CM-SECURITY-MIB", "f3PrivilegeChangeState"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeUserName"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeIpv4Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeIpv6Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeTerminalIpv4Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeTerminalIpv6Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeInterface"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeCurrentPrivilege"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeRequestedPrivilege"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeDuration"))
)
if mibBuilder.loadTexts:
    f3PrivilegeChangeTrap.setStatus(
        "current"
    )


# Notifications groups

cmSecurityNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 2, 2, 2)
)
cmSecurityNotifGroup.setObjects(
    ("CM-SECURITY-MIB", "f3SecurityTrap")
)
if mibBuilder.loadTexts:
    cmSecurityNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cmSecurityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 2, 1, 1)
)
cmSecurityCompliance.setObjects(
    ("CM-SECURITY-MIB", "cmSecurityObjectGroup")
)
if mibBuilder.loadTexts:
    cmSecurityCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-SECURITY-MIB",
    **{"SecuritySelfTestResult": SecuritySelfTestResult,
       "SecuritySelfTestStatus": SecuritySelfTestStatus,
       "CmRemoteAuthProtocol": CmRemoteAuthProtocol,
       "CmSecurityAccessOrder": CmSecurityAccessOrder,
       "CmSecurityAuthType": CmSecurityAuthType,
       "CmSecurityPrivLevel": CmSecurityPrivLevel,
       "CmRemoteAuthOrder": CmRemoteAuthOrder,
       "CmSecurityPolicyStrength": CmSecurityPolicyStrength,
       "UsmUserAccessType": UsmUserAccessType,
       "SecurityUserAction": SecurityUserAction,
       "SnmpSecurityTrapType": SnmpSecurityTrapType,
       "PrivilegeRequestAction": PrivilegeRequestAction,
       "PrivilegeRequestState": PrivilegeRequestState,
       "RsaKeyLengthType": RsaKeyLengthType,
       "ZeroizeKeysAction": ZeroizeKeysAction,
       "RunSelfTestAction": RunSelfTestAction,
       "SslCertificateAction": SslCertificateAction,
       "RsaKeyPairAction": RsaKeyPairAction,
       "CsrAction": CsrAction,
       "NasIpAddressType": NasIpAddressType,
       "CertificateEnrollmentProtocol": CertificateEnrollmentProtocol,
       "CaAction": CaAction,
       "SslCertificatePrivateKeyPairAction": SslCertificatePrivateKeyPairAction,
       "CertificateType": CertificateType,
       "CertificateStatus": CertificateStatus,
       "AutoEnrollmentStatus": AutoEnrollmentStatus,
       "CaRootCertStatus": CaRootCertStatus,
       "cmSecurityMIB": cmSecurityMIB,
       "cmSecurityObjects": cmSecurityObjects,
       "cmAuthProtocol": cmAuthProtocol,
       "cmAccessOrder": cmAccessOrder,
       "cmAuthType": cmAuthType,
       "cmNASIpAddress": cmNASIpAddress,
       "cmSecurityUserTable": cmSecurityUserTable,
       "cmSecurityUserEntry": cmSecurityUserEntry,
       "cmSecurityUserName": cmSecurityUserName,
       "cmSecurityUserComment": cmSecurityUserComment,
       "cmSecurityUserPrivLevel": cmSecurityUserPrivLevel,
       "cmSecurityUserLoginTimeout": cmSecurityUserLoginTimeout,
       "cmSecurityUserNumFailedLoginAttempts": cmSecurityUserNumFailedLoginAttempts,
       "cmSecurityUserLastLoginTime": cmSecurityUserLastLoginTime,
       "cmSecurityUserLockedout": cmSecurityUserLockedout,
       "cmSecurityUserLastLockedoutTime": cmSecurityUserLastLockedoutTime,
       "cmSecurityUserCliPagingEnable": cmSecurityUserCliPagingEnable,
       "cmSecurityUserRemoteUser": cmSecurityUserRemoteUser,
       "cmSecurityUserPassword": cmSecurityUserPassword,
       "cmSecurityUserStorageType": cmSecurityUserStorageType,
       "cmSecurityUserRowStatus": cmSecurityUserRowStatus,
       "cmSecurityUserAction": cmSecurityUserAction,
       "cmSecurityCryptoPassword": cmSecurityCryptoPassword,
       "cmSecurityUserRemoteCryptoUser": cmSecurityUserRemoteCryptoUser,
       "cmSecurityUserSso2fa": cmSecurityUserSso2fa,
       "cmRemoteAuthServerTable": cmRemoteAuthServerTable,
       "cmRemoteAuthServerEntry": cmRemoteAuthServerEntry,
       "cmRemoteAuthServerIndex": cmRemoteAuthServerIndex,
       "cmRemoteAuthServerEnabled": cmRemoteAuthServerEnabled,
       "cmRemoteAuthServerOrder": cmRemoteAuthServerOrder,
       "cmRemoteAuthServerIpAddress": cmRemoteAuthServerIpAddress,
       "cmRemoteAuthServerPort": cmRemoteAuthServerPort,
       "cmRemoteAuthServerNumRetries": cmRemoteAuthServerNumRetries,
       "cmRemoteAuthServerTimeout": cmRemoteAuthServerTimeout,
       "cmRemoteAuthServerSecret": cmRemoteAuthServerSecret,
       "cmRemoteAuthServerAccountingPort": cmRemoteAuthServerAccountingPort,
       "cmRemoteAuthServerIpVersion": cmRemoteAuthServerIpVersion,
       "cmRemoteAuthServerIpv6Addr": cmRemoteAuthServerIpv6Addr,
       "cmSecurityPolicyStrength": cmSecurityPolicyStrength,
       "cmRemoteAuthServerAccountingEnabled": cmRemoteAuthServerAccountingEnabled,
       "f3UsmUserTable": f3UsmUserTable,
       "f3UsmUserEntry": f3UsmUserEntry,
       "f3UsmUserAccessType": f3UsmUserAccessType,
       "f3TacacsPrivLevelControlEnabled": f3TacacsPrivLevelControlEnabled,
       "f3TacacsDefaultPrivLevel": f3TacacsDefaultPrivLevel,
       "f3NasIpv6Addr": f3NasIpv6Addr,
       "f3SecurityTrapType": f3SecurityTrapType,
       "f3SecurityTrapInfo": f3SecurityTrapInfo,
       "f3PrivilegeChangeTable": f3PrivilegeChangeTable,
       "f3PrivilegeChangeEntry": f3PrivilegeChangeEntry,
       "f3PrivilegeChangeId": f3PrivilegeChangeId,
       "f3PrivilegeChangeUserName": f3PrivilegeChangeUserName,
       "f3PrivilegeChangeIpv4Address": f3PrivilegeChangeIpv4Address,
       "f3PrivilegeChangeIpv6Address": f3PrivilegeChangeIpv6Address,
       "f3PrivilegeChangeTerminalIpv4Address": f3PrivilegeChangeTerminalIpv4Address,
       "f3PrivilegeChangeTerminalIpv6Address": f3PrivilegeChangeTerminalIpv6Address,
       "f3PrivilegeChangeInterface": f3PrivilegeChangeInterface,
       "f3PrivilegeChangeCurrentPrivilege": f3PrivilegeChangeCurrentPrivilege,
       "f3PrivilegeChangeRequestedPrivilege": f3PrivilegeChangeRequestedPrivilege,
       "f3PrivilegeChangeDuration": f3PrivilegeChangeDuration,
       "f3PrivilegeChangeAction": f3PrivilegeChangeAction,
       "f3PrivilegeChangeState": f3PrivilegeChangeState,
       "f3PrivilegeChangeRemainingTime": f3PrivilegeChangeRemainingTime,
       "f3PrivilegeChangeRemoteName": f3PrivilegeChangeRemoteName,
       "f3UserPrivMgmtControl": f3UserPrivMgmtControl,
       "f3UserPrivRspTimeout": f3UserPrivRspTimeout,
       "f3RadiusSendVendorAvpEnabled": f3RadiusSendVendorAvpEnabled,
       "f3RadiusRealm": f3RadiusRealm,
       "cmIcmpV4Objects": cmIcmpV4Objects,
       "icmpV4Filter": icmpV4Filter,
       "icmpV4DropEchoRequests": icmpV4DropEchoRequests,
       "cmIcmpV6Objects": cmIcmpV6Objects,
       "icmpV6Filter": icmpV6Filter,
       "icmpV6DropEchoRequests": icmpV6DropEchoRequests,
       "icmpV6DropNeighborSolicitation": icmpV6DropNeighborSolicitation,
       "icmpV6DropRouterAdvertisement": icmpV6DropRouterAdvertisement,
       "icmpV6DropNeighborAdvertisement": icmpV6DropNeighborAdvertisement,
       "icmpV6DropRouterSolicitation": icmpV6DropRouterSolicitation,
       "cmAnonymizeLogTimeInDays": cmAnonymizeLogTimeInDays,
       "f3FipsObjects": f3FipsObjects,
       "f3FipsOperationMode": f3FipsOperationMode,
       "f3FipsSecuritySelfTestFailureCount": f3FipsSecuritySelfTestFailureCount,
       "f3FipsSecuritySelfTestResult": f3FipsSecuritySelfTestResult,
       "f3FipsSecuritySelfTestStatus": f3FipsSecuritySelfTestStatus,
       "f3FipsAction": f3FipsAction,
       "f3Sso2faControl": f3Sso2faControl,
       "f3SslCertificateObjects": f3SslCertificateObjects,
       "f3HttpsSslCertExpNotifPeriod": f3HttpsSslCertExpNotifPeriod,
       "f3HttpsSslKeyPair": f3HttpsSslKeyPair,
       "f3SslCertificateAction": f3SslCertificateAction,
       "f3SslCertificateActionPairName": f3SslCertificateActionPairName,
       "f3SslCertificatePrivateKeyPairTable": f3SslCertificatePrivateKeyPairTable,
       "f3SslCertificatePrivateKeyPairEntry": f3SslCertificatePrivateKeyPairEntry,
       "f3SslCertificatePrivateKeyPairName": f3SslCertificatePrivateKeyPairName,
       "f3SslCertificatePrivateKeyPairSslCertificate": f3SslCertificatePrivateKeyPairSslCertificate,
       "f3SslCertificatePrivateKeyPairPrivateKeyPresent": f3SslCertificatePrivateKeyPairPrivateKeyPresent,
       "f3SslCertificatePrivateKeyPairRsaKeyPairName": f3SslCertificatePrivateKeyPairRsaKeyPairName,
       "f3SslCertificatePrivateKeyPairCertificateType": f3SslCertificatePrivateKeyPairCertificateType,
       "f3SslCertificatePrivateKeyPairCertificateStatus": f3SslCertificatePrivateKeyPairCertificateStatus,
       "f3SslCertificatePrivateKeyPairAction": f3SslCertificatePrivateKeyPairAction,
       "f3SslCertificateActionKeyName": f3SslCertificateActionKeyName,
       "f3RsaKeyPairObjects": f3RsaKeyPairObjects,
       "f3RsaKeyPairAction": f3RsaKeyPairAction,
       "f3RsaKeyPairActionName": f3RsaKeyPairActionName,
       "f3RsaKeyPairActionLength": f3RsaKeyPairActionLength,
       "f3RsaKeyPairTable": f3RsaKeyPairTable,
       "f3RsaKeyPairEntry": f3RsaKeyPairEntry,
       "f3RsaKeyPairName": f3RsaKeyPairName,
       "f3RsaKeyPairPublicKey": f3RsaKeyPairPublicKey,
       "f3CertSigningRequestObjects": f3CertSigningRequestObjects,
       "f3CsrAction": f3CsrAction,
       "f3CsrActionCsrName": f3CsrActionCsrName,
       "f3CsrActionRsaKeyName": f3CsrActionRsaKeyName,
       "f3CsrActionCountry": f3CsrActionCountry,
       "f3CsrActionState": f3CsrActionState,
       "f3CsrActionLocality": f3CsrActionLocality,
       "f3CsrActionOrganization": f3CsrActionOrganization,
       "f3CsrActionOrganizationUnit": f3CsrActionOrganizationUnit,
       "f3CsrActionCommonName": f3CsrActionCommonName,
       "f3CsrActionEmail": f3CsrActionEmail,
       "f3CsrActionSerialNumber": f3CsrActionSerialNumber,
       "f3CsrActionAlternativeName": f3CsrActionAlternativeName,
       "f3CertSigningRequestTable": f3CertSigningRequestTable,
       "f3CertSigningRequestEntry": f3CertSigningRequestEntry,
       "f3CertSigningRequestName": f3CertSigningRequestName,
       "f3CertSigningRequestRsaKeyPairName": f3CertSigningRequestRsaKeyPairName,
       "f3CertSigningRequestCsrData": f3CertSigningRequestCsrData,
       "f3CertSigningRequestAutoEnrollmentStatus": f3CertSigningRequestAutoEnrollmentStatus,
       "f3NasIpAddressType": f3NasIpAddressType,
       "f3CaProfileTable": f3CaProfileTable,
       "f3CaProfileEntry": f3CaProfileEntry,
       "f3CaProfileIndex": f3CaProfileIndex,
       "f3CaProfileName": f3CaProfileName,
       "f3CaProfileEnrollmentProtocol": f3CaProfileEnrollmentProtocol,
       "f3CaProfileHttpPort": f3CaProfileHttpPort,
       "f3CaProfileAutoRenewalControl": f3CaProfileAutoRenewalControl,
       "f3CaProfileRenewalPercentLifetime": f3CaProfileRenewalPercentLifetime,
       "f3CaProfileRenewalNewKeyPairGenControl": f3CaProfileRenewalNewKeyPairGenControl,
       "f3CaProfileStorageType": f3CaProfileStorageType,
       "f3CaProfileRowStatus": f3CaProfileRowStatus,
       "f3CaTable": f3CaTable,
       "f3CaEntry": f3CaEntry,
       "f3CaName": f3CaName,
       "f3CaProfile": f3CaProfile,
       "f3CaUrl": f3CaUrl,
       "f3CaScepQueryMessage": f3CaScepQueryMessage,
       "f3CaCertList": f3CaCertList,
       "f3CaRootCertStatus": f3CaRootCertStatus,
       "f3CaLastCsr": f3CaLastCsr,
       "f3CaAction": f3CaAction,
       "f3CaActionCsrName": f3CaActionCsrName,
       "f3CaActionChallengePassword": f3CaActionChallengePassword,
       "f3CaStorageType": f3CaStorageType,
       "f3CaRowStatus": f3CaRowStatus,
       "f3SshCipherStrengthHighControl": f3SshCipherStrengthHighControl,
       "cmSecurityConformance": cmSecurityConformance,
       "cmSecurityCompliances": cmSecurityCompliances,
       "cmSecurityCompliance": cmSecurityCompliance,
       "cmSecurityGroups": cmSecurityGroups,
       "cmSecurityObjectGroup": cmSecurityObjectGroup,
       "cmSecurityNotifGroup": cmSecurityNotifGroup,
       "cmSecurityNotifications": cmSecurityNotifications,
       "f3SecurityTrap": f3SecurityTrap,
       "f3PrivilegeChangeTrap": f3PrivilegeChangeTrap}
)
