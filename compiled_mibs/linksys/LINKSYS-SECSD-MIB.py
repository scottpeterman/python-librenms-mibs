# SNMP MIB module (LINKSYS-SECSD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\linksys\LINKSYS-SECSD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:08:53 2025
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

(rnd,) = mibBuilder.importSymbols(
    "LINKSYS-MIB",
    "rnd")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlSecSd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209)
)
if mibBuilder.loadTexts:
    rlSecSd.setRevisions(
        ("2011-08-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlSecSdRuleUserType(TextualConvention, Integer32):
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
        *(("user-name", 1),
          ("default-user", 2),
          ("level-15-users", 3),
          ("all-users", 4))
    )



class RlSecSdChannelType(TextualConvention, Integer32):
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
        *(("secure-xml-snmp", 1),
          ("secure", 2),
          ("insecure", 3),
          ("insecure-xml-snmp", 4))
    )



class RlSecSdAccessType(TextualConvention, Integer32):
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
        *(("exclude", 1),
          ("include-encrypted", 2),
          ("include-decrypted", 3))
    )



class RlSecSdPermitAccessType(TextualConvention, Integer32):
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
        *(("exclude", 1),
          ("include-encrypted", 2),
          ("include-decrypted", 3),
          ("include-all", 4))
    )



class RlSecSdSessionAccessType(TextualConvention, Integer32):
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
        *(("exclude", 1),
          ("include-encrypted", 2),
          ("include-decrypted", 3),
          ("default", 4))
    )



class RlSecSdRuleOwnerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("user", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RlSecSdRulesTable_Object = MibTable
rlSecSdRulesTable = _RlSecSdRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 1)
)
if mibBuilder.loadTexts:
    rlSecSdRulesTable.setStatus("current")
_RlSecSdRulesEntry_Object = MibTableRow
rlSecSdRulesEntry = _RlSecSdRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 1, 1)
)
rlSecSdRulesEntry.setIndexNames(
    (0, "LINKSYS-SECSD-MIB", "rlSecSdRuleUser"),
    (0, "LINKSYS-SECSD-MIB", "rlSecSdRuleUserName"),
    (0, "LINKSYS-SECSD-MIB", "rlSecSdRuleChannel"),
)
if mibBuilder.loadTexts:
    rlSecSdRulesEntry.setStatus("current")
_RlSecSdRuleUser_Type = RlSecSdRuleUserType
_RlSecSdRuleUser_Object = MibTableColumn
rlSecSdRuleUser = _RlSecSdRuleUser_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 1, 1, 1),
    _RlSecSdRuleUser_Type()
)
rlSecSdRuleUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecSdRuleUser.setStatus("current")


class _RlSecSdRuleUserName_Type(DisplayString):
    """Custom type rlSecSdRuleUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_RlSecSdRuleUserName_Type.__name__ = "DisplayString"
_RlSecSdRuleUserName_Object = MibTableColumn
rlSecSdRuleUserName = _RlSecSdRuleUserName_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 1, 1, 2),
    _RlSecSdRuleUserName_Type()
)
rlSecSdRuleUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecSdRuleUserName.setStatus("current")
_RlSecSdRuleChannel_Type = RlSecSdChannelType
_RlSecSdRuleChannel_Object = MibTableColumn
rlSecSdRuleChannel = _RlSecSdRuleChannel_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 1, 1, 3),
    _RlSecSdRuleChannel_Type()
)
rlSecSdRuleChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecSdRuleChannel.setStatus("current")
_RlSecSdRuleRead_Type = RlSecSdAccessType
_RlSecSdRuleRead_Object = MibTableColumn
rlSecSdRuleRead = _RlSecSdRuleRead_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 1, 1, 4),
    _RlSecSdRuleRead_Type()
)
rlSecSdRuleRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecSdRuleRead.setStatus("current")
_RlSecSdRulePermitRead_Type = RlSecSdPermitAccessType
_RlSecSdRulePermitRead_Object = MibTableColumn
rlSecSdRulePermitRead = _RlSecSdRulePermitRead_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 1, 1, 5),
    _RlSecSdRulePermitRead_Type()
)
rlSecSdRulePermitRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecSdRulePermitRead.setStatus("current")
_RlSecSdRuleIsDefault_Type = TruthValue
_RlSecSdRuleIsDefault_Object = MibTableColumn
rlSecSdRuleIsDefault = _RlSecSdRuleIsDefault_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 1, 1, 6),
    _RlSecSdRuleIsDefault_Type()
)
rlSecSdRuleIsDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSecSdRuleIsDefault.setStatus("current")
_RlSecSdRuleOwner_Type = RlSecSdRuleOwnerType
_RlSecSdRuleOwner_Object = MibTableColumn
rlSecSdRuleOwner = _RlSecSdRuleOwner_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 1, 1, 7),
    _RlSecSdRuleOwner_Type()
)
rlSecSdRuleOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecSdRuleOwner.setStatus("current")
_RlSecSdRuleStatus_Type = RowStatus
_RlSecSdRuleStatus_Object = MibTableColumn
rlSecSdRuleStatus = _RlSecSdRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 1, 1, 8),
    _RlSecSdRuleStatus_Type()
)
rlSecSdRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecSdRuleStatus.setStatus("current")
_RlSecSdMngSessionsTable_Object = MibTable
rlSecSdMngSessionsTable = _RlSecSdMngSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 2)
)
if mibBuilder.loadTexts:
    rlSecSdMngSessionsTable.setStatus("current")
_RlSecSdMngSessionsEntry_Object = MibTableRow
rlSecSdMngSessionsEntry = _RlSecSdMngSessionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 2, 2)
)
rlSecSdMngSessionsEntry.setIndexNames(
    (0, "LINKSYS-SECSD-MIB", "rlSecSdMngSessionId"),
)
if mibBuilder.loadTexts:
    rlSecSdMngSessionsEntry.setStatus("current")
_RlSecSdMngSessionId_Type = Integer32
_RlSecSdMngSessionId_Object = MibTableColumn
rlSecSdMngSessionId = _RlSecSdMngSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 2, 2, 1),
    _RlSecSdMngSessionId_Type()
)
rlSecSdMngSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSecSdMngSessionId.setStatus("current")
_RlSecSdMngSessionUserLevel_Type = Integer32
_RlSecSdMngSessionUserLevel_Object = MibTableColumn
rlSecSdMngSessionUserLevel = _RlSecSdMngSessionUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 2, 2, 2),
    _RlSecSdMngSessionUserLevel_Type()
)
rlSecSdMngSessionUserLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSecSdMngSessionUserLevel.setStatus("current")


class _RlSecSdMngSessionUserName_Type(DisplayString):
    """Custom type rlSecSdMngSessionUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSecSdMngSessionUserName_Type.__name__ = "DisplayString"
_RlSecSdMngSessionUserName_Object = MibTableColumn
rlSecSdMngSessionUserName = _RlSecSdMngSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 2, 2, 3),
    _RlSecSdMngSessionUserName_Type()
)
rlSecSdMngSessionUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecSdMngSessionUserName.setStatus("current")
_RlSecSdMngSessionChannel_Type = RlSecSdChannelType
_RlSecSdMngSessionChannel_Object = MibTableColumn
rlSecSdMngSessionChannel = _RlSecSdMngSessionChannel_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 2, 2, 4),
    _RlSecSdMngSessionChannel_Type()
)
rlSecSdMngSessionChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSecSdMngSessionChannel.setStatus("current")
_RlSecSdSessionControl_Type = RlSecSdSessionAccessType
_RlSecSdSessionControl_Object = MibScalar
rlSecSdSessionControl = _RlSecSdSessionControl_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 3),
    _RlSecSdSessionControl_Type()
)
rlSecSdSessionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecSdSessionControl.setStatus("current")
_RlSecSdCurrentSessionId_Type = Integer32
_RlSecSdCurrentSessionId_Object = MibScalar
rlSecSdCurrentSessionId = _RlSecSdCurrentSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 4),
    _RlSecSdCurrentSessionId_Type()
)
rlSecSdCurrentSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSecSdCurrentSessionId.setStatus("current")


class _RlSecSdPassPhrase_Type(DisplayString):
    """Custom type rlSecSdPassPhrase based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSecSdPassPhrase_Type.__name__ = "DisplayString"
_RlSecSdPassPhrase_Object = MibScalar
rlSecSdPassPhrase = _RlSecSdPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 5),
    _RlSecSdPassPhrase_Type()
)
rlSecSdPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecSdPassPhrase.setStatus("current")


class _RlSecSdFilePassphraseControl_Type(Integer32):
    """Custom type rlSecSdFilePassphraseControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restricted", 1),
          ("unrestricted", 2))
    )


_RlSecSdFilePassphraseControl_Type.__name__ = "Integer32"
_RlSecSdFilePassphraseControl_Object = MibScalar
rlSecSdFilePassphraseControl = _RlSecSdFilePassphraseControl_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 6),
    _RlSecSdFilePassphraseControl_Type()
)
rlSecSdFilePassphraseControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecSdFilePassphraseControl.setStatus("current")


class _RlSecSdFileIntegrityControl_Type(Integer32):
    """Custom type rlSecSdFileIntegrityControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RlSecSdFileIntegrityControl_Type.__name__ = "Integer32"
_RlSecSdFileIntegrityControl_Object = MibScalar
rlSecSdFileIntegrityControl = _RlSecSdFileIntegrityControl_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 7),
    _RlSecSdFileIntegrityControl_Type()
)
rlSecSdFileIntegrityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecSdFileIntegrityControl.setStatus("current")


class _RlSecSdConfigurationFileSsdDigest_Type(DisplayString):
    """Custom type rlSecSdConfigurationFileSsdDigest based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSecSdConfigurationFileSsdDigest_Type.__name__ = "DisplayString"
_RlSecSdConfigurationFileSsdDigest_Object = MibScalar
rlSecSdConfigurationFileSsdDigest = _RlSecSdConfigurationFileSsdDigest_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 8),
    _RlSecSdConfigurationFileSsdDigest_Type()
)
rlSecSdConfigurationFileSsdDigest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecSdConfigurationFileSsdDigest.setStatus("current")


class _RlSecSdConfigurationFileDigest_Type(DisplayString):
    """Custom type rlSecSdConfigurationFileDigest based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlSecSdConfigurationFileDigest_Type.__name__ = "DisplayString"
_RlSecSdConfigurationFileDigest_Object = MibScalar
rlSecSdConfigurationFileDigest = _RlSecSdConfigurationFileDigest_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 9),
    _RlSecSdConfigurationFileDigest_Type()
)
rlSecSdConfigurationFileDigest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecSdConfigurationFileDigest.setStatus("current")


class _RlSecSdFileIndicator_Type(DisplayString):
    """Custom type rlSecSdFileIndicator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_RlSecSdFileIndicator_Type.__name__ = "DisplayString"
_RlSecSdFileIndicator_Object = MibScalar
rlSecSdFileIndicator = _RlSecSdFileIndicator_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 209, 10),
    _RlSecSdFileIndicator_Type()
)
rlSecSdFileIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecSdFileIndicator.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINKSYS-SECSD-MIB",
    **{"RlSecSdRuleUserType": RlSecSdRuleUserType,
       "RlSecSdChannelType": RlSecSdChannelType,
       "RlSecSdAccessType": RlSecSdAccessType,
       "RlSecSdPermitAccessType": RlSecSdPermitAccessType,
       "RlSecSdSessionAccessType": RlSecSdSessionAccessType,
       "RlSecSdRuleOwnerType": RlSecSdRuleOwnerType,
       "rlSecSd": rlSecSd,
       "rlSecSdRulesTable": rlSecSdRulesTable,
       "rlSecSdRulesEntry": rlSecSdRulesEntry,
       "rlSecSdRuleUser": rlSecSdRuleUser,
       "rlSecSdRuleUserName": rlSecSdRuleUserName,
       "rlSecSdRuleChannel": rlSecSdRuleChannel,
       "rlSecSdRuleRead": rlSecSdRuleRead,
       "rlSecSdRulePermitRead": rlSecSdRulePermitRead,
       "rlSecSdRuleIsDefault": rlSecSdRuleIsDefault,
       "rlSecSdRuleOwner": rlSecSdRuleOwner,
       "rlSecSdRuleStatus": rlSecSdRuleStatus,
       "rlSecSdMngSessionsTable": rlSecSdMngSessionsTable,
       "rlSecSdMngSessionsEntry": rlSecSdMngSessionsEntry,
       "rlSecSdMngSessionId": rlSecSdMngSessionId,
       "rlSecSdMngSessionUserLevel": rlSecSdMngSessionUserLevel,
       "rlSecSdMngSessionUserName": rlSecSdMngSessionUserName,
       "rlSecSdMngSessionChannel": rlSecSdMngSessionChannel,
       "rlSecSdSessionControl": rlSecSdSessionControl,
       "rlSecSdCurrentSessionId": rlSecSdCurrentSessionId,
       "rlSecSdPassPhrase": rlSecSdPassPhrase,
       "rlSecSdFilePassphraseControl": rlSecSdFilePassphraseControl,
       "rlSecSdFileIntegrityControl": rlSecSdFileIntegrityControl,
       "rlSecSdConfigurationFileSsdDigest": rlSecSdConfigurationFileSsdDigest,
       "rlSecSdConfigurationFileDigest": rlSecSdConfigurationFileDigest,
       "rlSecSdFileIndicator": rlSecSdFileIndicator}
)
