# SNMP MIB module (SIAE-USER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-USER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:34 2025
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

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

accessControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5)
)
if mibBuilder.loadTexts:
    accessControl.setRevisions(
        ("2016-09-17 00:00",
         "2014-04-08 00:00",
         "2014-02-03 00:00",
         "2013-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AccessControlMibVersion_Type(Integer32):
    """Custom type accessControlMibVersion based on Integer32"""
    defaultValue = 1


_AccessControlMibVersion_Type.__name__ = "Integer32"
_AccessControlMibVersion_Object = MibScalar
accessControlMibVersion = _AccessControlMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 1),
    _AccessControlMibVersion_Type()
)
accessControlMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessControlMibVersion.setStatus("current")
_AccessControlGroupTable_Object = MibTable
accessControlGroupTable = _AccessControlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2)
)
if mibBuilder.loadTexts:
    accessControlGroupTable.setStatus("current")
_AccessControlGroupRecord_Object = MibTableRow
accessControlGroupRecord = _AccessControlGroupRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1)
)
accessControlGroupRecord.setIndexNames(
    (0, "SIAE-USER-MIB", "accessControlGroupName"),
)
if mibBuilder.loadTexts:
    accessControlGroupRecord.setStatus("current")


class _AccessControlGroupName_Type(SnmpAdminString):
    """Custom type accessControlGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AccessControlGroupName_Type.__name__ = "SnmpAdminString"
_AccessControlGroupName_Object = MibTableColumn
accessControlGroupName = _AccessControlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 1),
    _AccessControlGroupName_Type()
)
accessControlGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlGroupName.setStatus("current")


class _AccessControlGroupProfile_Type(Integer32):
    """Custom type accessControlGroupProfile based on Integer32"""
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
        *(("admin", 1),
          ("readwrite", 2),
          ("maintenance", 3),
          ("readonly", 4))
    )


_AccessControlGroupProfile_Type.__name__ = "Integer32"
_AccessControlGroupProfile_Object = MibTableColumn
accessControlGroupProfile = _AccessControlGroupProfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 2),
    _AccessControlGroupProfile_Type()
)
accessControlGroupProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlGroupProfile.setStatus("current")


class _AccessControlGroupHttp_Type(Integer32):
    """Custom type accessControlGroupHttp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("allow", 2))
    )


_AccessControlGroupHttp_Type.__name__ = "Integer32"
_AccessControlGroupHttp_Object = MibTableColumn
accessControlGroupHttp = _AccessControlGroupHttp_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 3),
    _AccessControlGroupHttp_Type()
)
accessControlGroupHttp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlGroupHttp.setStatus("current")


class _AccessControlGroupHttps_Type(Integer32):
    """Custom type accessControlGroupHttps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("allow", 2))
    )


_AccessControlGroupHttps_Type.__name__ = "Integer32"
_AccessControlGroupHttps_Object = MibTableColumn
accessControlGroupHttps = _AccessControlGroupHttps_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 4),
    _AccessControlGroupHttps_Type()
)
accessControlGroupHttps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlGroupHttps.setStatus("current")


class _AccessControlGroupSnmp_Type(Integer32):
    """Custom type accessControlGroupSnmp based on Integer32"""
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
        *(("deny", 1),
          ("allowV1", 2),
          ("allowV2c", 3),
          ("allowV3", 4))
    )


_AccessControlGroupSnmp_Type.__name__ = "Integer32"
_AccessControlGroupSnmp_Object = MibTableColumn
accessControlGroupSnmp = _AccessControlGroupSnmp_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 5),
    _AccessControlGroupSnmp_Type()
)
accessControlGroupSnmp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlGroupSnmp.setStatus("current")


class _AccessControlGroupFtp_Type(Integer32):
    """Custom type accessControlGroupFtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("allow", 2))
    )


_AccessControlGroupFtp_Type.__name__ = "Integer32"
_AccessControlGroupFtp_Object = MibTableColumn
accessControlGroupFtp = _AccessControlGroupFtp_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 6),
    _AccessControlGroupFtp_Type()
)
accessControlGroupFtp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlGroupFtp.setStatus("current")


class _AccessControlGroupSftp_Type(Integer32):
    """Custom type accessControlGroupSftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("allow", 2))
    )


_AccessControlGroupSftp_Type.__name__ = "Integer32"
_AccessControlGroupSftp_Object = MibTableColumn
accessControlGroupSftp = _AccessControlGroupSftp_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 7),
    _AccessControlGroupSftp_Type()
)
accessControlGroupSftp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlGroupSftp.setStatus("current")


class _AccessControlGroupSsh_Type(Integer32):
    """Custom type accessControlGroupSsh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("allow", 2))
    )


_AccessControlGroupSsh_Type.__name__ = "Integer32"
_AccessControlGroupSsh_Object = MibTableColumn
accessControlGroupSsh = _AccessControlGroupSsh_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 8),
    _AccessControlGroupSsh_Type()
)
accessControlGroupSsh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlGroupSsh.setStatus("current")
_AccessControlGroupRowStatus_Type = RowStatus
_AccessControlGroupRowStatus_Object = MibTableColumn
accessControlGroupRowStatus = _AccessControlGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 9),
    _AccessControlGroupRowStatus_Type()
)
accessControlGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlGroupRowStatus.setStatus("current")


class _AccessControlGroupCli_Type(Integer32):
    """Custom type accessControlGroupCli based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("allow", 2))
    )


_AccessControlGroupCli_Type.__name__ = "Integer32"
_AccessControlGroupCli_Object = MibTableColumn
accessControlGroupCli = _AccessControlGroupCli_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 10),
    _AccessControlGroupCli_Type()
)
accessControlGroupCli.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessControlGroupCli.setStatus("current")
_AccessControlUserTable_Object = MibTable
accessControlUserTable = _AccessControlUserTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3)
)
if mibBuilder.loadTexts:
    accessControlUserTable.setStatus("current")
_AccessControlUserRecord_Object = MibTableRow
accessControlUserRecord = _AccessControlUserRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1)
)
accessControlUserRecord.setIndexNames(
    (0, "SIAE-USER-MIB", "accessControlUserName"),
)
if mibBuilder.loadTexts:
    accessControlUserRecord.setStatus("current")


class _AccessControlUserName_Type(SnmpAdminString):
    """Custom type accessControlUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AccessControlUserName_Type.__name__ = "SnmpAdminString"
_AccessControlUserName_Object = MibTableColumn
accessControlUserName = _AccessControlUserName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 1),
    _AccessControlUserName_Type()
)
accessControlUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlUserName.setStatus("current")


class _AccessControlUserGroupName_Type(SnmpAdminString):
    """Custom type accessControlUserGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AccessControlUserGroupName_Type.__name__ = "SnmpAdminString"
_AccessControlUserGroupName_Object = MibTableColumn
accessControlUserGroupName = _AccessControlUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 2),
    _AccessControlUserGroupName_Type()
)
accessControlUserGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlUserGroupName.setStatus("current")


class _AccessControlUserPwd_Type(DisplayString):
    """Custom type accessControlUserPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AccessControlUserPwd_Type.__name__ = "DisplayString"
_AccessControlUserPwd_Object = MibTableColumn
accessControlUserPwd = _AccessControlUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 3),
    _AccessControlUserPwd_Type()
)
accessControlUserPwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlUserPwd.setStatus("current")


class _AccessControlUserSnmpAuthProt_Type(Integer32):
    """Custom type accessControlUserSnmpAuthProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("md5", 2),
          ("sha", 3))
    )


_AccessControlUserSnmpAuthProt_Type.__name__ = "Integer32"
_AccessControlUserSnmpAuthProt_Object = MibTableColumn
accessControlUserSnmpAuthProt = _AccessControlUserSnmpAuthProt_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 4),
    _AccessControlUserSnmpAuthProt_Type()
)
accessControlUserSnmpAuthProt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlUserSnmpAuthProt.setStatus("current")
_AccessControlUserSnmpAuthKey_Type = OctetString
_AccessControlUserSnmpAuthKey_Object = MibTableColumn
accessControlUserSnmpAuthKey = _AccessControlUserSnmpAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 5),
    _AccessControlUserSnmpAuthKey_Type()
)
accessControlUserSnmpAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlUserSnmpAuthKey.setStatus("current")


class _AccessControlUserSnmpPrivProt_Type(Integer32):
    """Custom type accessControlUserSnmpPrivProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noPriv", 1),
          ("des", 2),
          ("aes", 3))
    )


_AccessControlUserSnmpPrivProt_Type.__name__ = "Integer32"
_AccessControlUserSnmpPrivProt_Object = MibTableColumn
accessControlUserSnmpPrivProt = _AccessControlUserSnmpPrivProt_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 6),
    _AccessControlUserSnmpPrivProt_Type()
)
accessControlUserSnmpPrivProt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlUserSnmpPrivProt.setStatus("current")


class _AccessControlUserSnmpPrivKey_Type(OctetString):
    """Custom type accessControlUserSnmpPrivKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AccessControlUserSnmpPrivKey_Type.__name__ = "OctetString"
_AccessControlUserSnmpPrivKey_Object = MibTableColumn
accessControlUserSnmpPrivKey = _AccessControlUserSnmpPrivKey_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 7),
    _AccessControlUserSnmpPrivKey_Type()
)
accessControlUserSnmpPrivKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlUserSnmpPrivKey.setStatus("current")


class _AccessControlUserTimeout_Type(Integer32):
    """Custom type accessControlUserTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AccessControlUserTimeout_Type.__name__ = "Integer32"
_AccessControlUserTimeout_Object = MibTableColumn
accessControlUserTimeout = _AccessControlUserTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 8),
    _AccessControlUserTimeout_Type()
)
accessControlUserTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlUserTimeout.setStatus("current")
_AccessControlUserRowStatus_Type = RowStatus
_AccessControlUserRowStatus_Object = MibTableColumn
accessControlUserRowStatus = _AccessControlUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 9),
    _AccessControlUserRowStatus_Type()
)
accessControlUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlUserRowStatus.setStatus("current")
_AccessControlLoginTable_Object = MibTable
accessControlLoginTable = _AccessControlLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4)
)
if mibBuilder.loadTexts:
    accessControlLoginTable.setStatus("current")
_AccessControlLoginRecord_Object = MibTableRow
accessControlLoginRecord = _AccessControlLoginRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1)
)
accessControlLoginRecord.setIndexNames(
    (0, "SIAE-USER-MIB", "accessControlLoginIpAddress"),
    (0, "SIAE-USER-MIB", "accessControlLoginUserName"),
    (0, "SIAE-USER-MIB", "accessControlLoginType"),
)
if mibBuilder.loadTexts:
    accessControlLoginRecord.setStatus("current")


class _AccessControlLoginUserName_Type(SnmpAdminString):
    """Custom type accessControlLoginUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AccessControlLoginUserName_Type.__name__ = "SnmpAdminString"
_AccessControlLoginUserName_Object = MibTableColumn
accessControlLoginUserName = _AccessControlLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 1),
    _AccessControlLoginUserName_Type()
)
accessControlLoginUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessControlLoginUserName.setStatus("current")
_AccessControlLoginIpAddress_Type = IpAddress
_AccessControlLoginIpAddress_Object = MibTableColumn
accessControlLoginIpAddress = _AccessControlLoginIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 2),
    _AccessControlLoginIpAddress_Type()
)
accessControlLoginIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessControlLoginIpAddress.setStatus("current")


class _AccessControlLoginRequest_Type(Integer32):
    """Custom type accessControlLoginRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("logout", 2),
          ("forcelogout", 3))
    )


_AccessControlLoginRequest_Type.__name__ = "Integer32"
_AccessControlLoginRequest_Object = MibTableColumn
accessControlLoginRequest = _AccessControlLoginRequest_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 3),
    _AccessControlLoginRequest_Type()
)
accessControlLoginRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlLoginRequest.setStatus("current")


class _AccessControlLoginTrapEnable_Type(Integer32):
    """Custom type accessControlLoginTrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AccessControlLoginTrapEnable_Type.__name__ = "Integer32"
_AccessControlLoginTrapEnable_Object = MibTableColumn
accessControlLoginTrapEnable = _AccessControlLoginTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 4),
    _AccessControlLoginTrapEnable_Type()
)
accessControlLoginTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlLoginTrapEnable.setStatus("current")


class _AccessControlLoginType_Type(Integer32):
    """Custom type accessControlLoginType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("web", 1),
          ("snmp", 2),
          ("cli", 3))
    )


_AccessControlLoginType_Type.__name__ = "Integer32"
_AccessControlLoginType_Object = MibTableColumn
accessControlLoginType = _AccessControlLoginType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 5),
    _AccessControlLoginType_Type()
)
accessControlLoginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessControlLoginType.setStatus("current")


class _AccessControlLoginPwd_Type(OctetString):
    """Custom type accessControlLoginPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AccessControlLoginPwd_Type.__name__ = "OctetString"
_AccessControlLoginPwd_Object = MibTableColumn
accessControlLoginPwd = _AccessControlLoginPwd_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 6),
    _AccessControlLoginPwd_Type()
)
accessControlLoginPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlLoginPwd.setStatus("current")


class _AccessControlLoginPolling_Type(Integer32):
    """Custom type accessControlLoginPolling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("polling", 1)
    )


_AccessControlLoginPolling_Type.__name__ = "Integer32"
_AccessControlLoginPolling_Object = MibTableColumn
accessControlLoginPolling = _AccessControlLoginPolling_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 7),
    _AccessControlLoginPolling_Type()
)
accessControlLoginPolling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessControlLoginPolling.setStatus("current")
_AccessControlClientTable_Object = MibTable
accessControlClientTable = _AccessControlClientTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5)
)
if mibBuilder.loadTexts:
    accessControlClientTable.setStatus("current")
_AccessControlClientRecord_Object = MibTableRow
accessControlClientRecord = _AccessControlClientRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1)
)
accessControlClientRecord.setIndexNames(
    (0, "SIAE-USER-MIB", "accessControlClientService"),
)
if mibBuilder.loadTexts:
    accessControlClientRecord.setStatus("current")


class _AccessControlClientService_Type(Integer32):
    """Custom type accessControlClientService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 2))
    )


_AccessControlClientService_Type.__name__ = "Integer32"
_AccessControlClientService_Object = MibTableColumn
accessControlClientService = _AccessControlClientService_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 1),
    _AccessControlClientService_Type()
)
accessControlClientService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlClientService.setStatus("current")


class _AccessControlClientServiceStatus_Type(Integer32):
    """Custom type accessControlClientServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AccessControlClientServiceStatus_Type.__name__ = "Integer32"
_AccessControlClientServiceStatus_Object = MibTableColumn
accessControlClientServiceStatus = _AccessControlClientServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 2),
    _AccessControlClientServiceStatus_Type()
)
accessControlClientServiceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlClientServiceStatus.setStatus("current")


class _AccessControlClientName_Type(SnmpAdminString):
    """Custom type accessControlClientName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AccessControlClientName_Type.__name__ = "SnmpAdminString"
_AccessControlClientName_Object = MibTableColumn
accessControlClientName = _AccessControlClientName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 3),
    _AccessControlClientName_Type()
)
accessControlClientName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlClientName.setStatus("current")


class _AccessControlClientPwd_Type(SnmpAdminString):
    """Custom type accessControlClientPwd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AccessControlClientPwd_Type.__name__ = "SnmpAdminString"
_AccessControlClientPwd_Object = MibTableColumn
accessControlClientPwd = _AccessControlClientPwd_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 4),
    _AccessControlClientPwd_Type()
)
accessControlClientPwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlClientPwd.setStatus("current")


class _AccessControlClientStorageType_Type(StorageType):
    """Custom type accessControlClientStorageType based on StorageType"""
    defaultValue = 3


_AccessControlClientStorageType_Type.__name__ = "StorageType"
_AccessControlClientStorageType_Object = MibTableColumn
accessControlClientStorageType = _AccessControlClientStorageType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 5),
    _AccessControlClientStorageType_Type()
)
accessControlClientStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlClientStorageType.setStatus("current")
_AccessControlClientRowStatus_Type = RowStatus
_AccessControlClientRowStatus_Object = MibTableColumn
accessControlClientRowStatus = _AccessControlClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 6),
    _AccessControlClientRowStatus_Type()
)
accessControlClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessControlClientRowStatus.setStatus("current")
_AccessControlExtLoginTable_Object = MibTable
accessControlExtLoginTable = _AccessControlExtLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 6)
)
if mibBuilder.loadTexts:
    accessControlExtLoginTable.setStatus("current")
_AccessControlExtLoginRecord_Object = MibTableRow
accessControlExtLoginRecord = _AccessControlExtLoginRecord_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 6, 1)
)
if mibBuilder.loadTexts:
    accessControlExtLoginRecord.setStatus("current")


class _AccessControlExtLoginProfile_Type(Integer32):
    """Custom type accessControlExtLoginProfile based on Integer32"""
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
        *(("admin", 1),
          ("readwrite", 2),
          ("maintenance", 3),
          ("readonly", 4))
    )


_AccessControlExtLoginProfile_Type.__name__ = "Integer32"
_AccessControlExtLoginProfile_Object = MibTableColumn
accessControlExtLoginProfile = _AccessControlExtLoginProfile_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 6, 1, 1),
    _AccessControlExtLoginProfile_Type()
)
accessControlExtLoginProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessControlExtLoginProfile.setStatus("current")


class _AccessControlExtLoginAuthMode_Type(Integer32):
    """Custom type accessControlExtLoginAuthMode based on Integer32"""
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


_AccessControlExtLoginAuthMode_Type.__name__ = "Integer32"
_AccessControlExtLoginAuthMode_Object = MibTableColumn
accessControlExtLoginAuthMode = _AccessControlExtLoginAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 5, 6, 1, 2),
    _AccessControlExtLoginAuthMode_Type()
)
accessControlExtLoginAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessControlExtLoginAuthMode.setStatus("current")
accessControlLoginRecord.registerAugmentions(
    ("SIAE-USER-MIB",
     "accessControlExtLoginRecord")
)
accessControlExtLoginRecord.setIndexNames(*accessControlLoginRecord.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-USER-MIB",
    **{"accessControl": accessControl,
       "accessControlMibVersion": accessControlMibVersion,
       "accessControlGroupTable": accessControlGroupTable,
       "accessControlGroupRecord": accessControlGroupRecord,
       "accessControlGroupName": accessControlGroupName,
       "accessControlGroupProfile": accessControlGroupProfile,
       "accessControlGroupHttp": accessControlGroupHttp,
       "accessControlGroupHttps": accessControlGroupHttps,
       "accessControlGroupSnmp": accessControlGroupSnmp,
       "accessControlGroupFtp": accessControlGroupFtp,
       "accessControlGroupSftp": accessControlGroupSftp,
       "accessControlGroupSsh": accessControlGroupSsh,
       "accessControlGroupRowStatus": accessControlGroupRowStatus,
       "accessControlGroupCli": accessControlGroupCli,
       "accessControlUserTable": accessControlUserTable,
       "accessControlUserRecord": accessControlUserRecord,
       "accessControlUserName": accessControlUserName,
       "accessControlUserGroupName": accessControlUserGroupName,
       "accessControlUserPwd": accessControlUserPwd,
       "accessControlUserSnmpAuthProt": accessControlUserSnmpAuthProt,
       "accessControlUserSnmpAuthKey": accessControlUserSnmpAuthKey,
       "accessControlUserSnmpPrivProt": accessControlUserSnmpPrivProt,
       "accessControlUserSnmpPrivKey": accessControlUserSnmpPrivKey,
       "accessControlUserTimeout": accessControlUserTimeout,
       "accessControlUserRowStatus": accessControlUserRowStatus,
       "accessControlLoginTable": accessControlLoginTable,
       "accessControlLoginRecord": accessControlLoginRecord,
       "accessControlLoginUserName": accessControlLoginUserName,
       "accessControlLoginIpAddress": accessControlLoginIpAddress,
       "accessControlLoginRequest": accessControlLoginRequest,
       "accessControlLoginTrapEnable": accessControlLoginTrapEnable,
       "accessControlLoginType": accessControlLoginType,
       "accessControlLoginPwd": accessControlLoginPwd,
       "accessControlLoginPolling": accessControlLoginPolling,
       "accessControlClientTable": accessControlClientTable,
       "accessControlClientRecord": accessControlClientRecord,
       "accessControlClientService": accessControlClientService,
       "accessControlClientServiceStatus": accessControlClientServiceStatus,
       "accessControlClientName": accessControlClientName,
       "accessControlClientPwd": accessControlClientPwd,
       "accessControlClientStorageType": accessControlClientStorageType,
       "accessControlClientRowStatus": accessControlClientRowStatus,
       "accessControlExtLoginTable": accessControlExtLoginTable,
       "accessControlExtLoginRecord": accessControlExtLoginRecord,
       "accessControlExtLoginProfile": accessControlExtLoginProfile,
       "accessControlExtLoginAuthMode": accessControlExtLoginAuthMode}
)
