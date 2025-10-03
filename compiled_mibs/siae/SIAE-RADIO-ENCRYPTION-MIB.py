# SNMP MIB module (SIAE-RADIO-ENCRYPTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-RADIO-ENCRYPTION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:29 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(AlarmSeverityCode,
 AlarmStatus) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "AlarmSeverityCode",
    "AlarmStatus")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

radioEncrypt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 96)
)
if mibBuilder.loadTexts:
    radioEncrypt.setRevisions(
        ("2015-07-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RdEncryptMibVersion_Type(Integer32):
    """Custom type rdEncryptMibVersion based on Integer32"""
    defaultValue = 1


_RdEncryptMibVersion_Type.__name__ = "Integer32"
_RdEncryptMibVersion_Object = MibScalar
rdEncryptMibVersion = _RdEncryptMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 96, 1),
    _RdEncryptMibVersion_Type()
)
rdEncryptMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdEncryptMibVersion.setStatus("current")
_RdEncryptTable_Object = MibTable
rdEncryptTable = _RdEncryptTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2)
)
if mibBuilder.loadTexts:
    rdEncryptTable.setStatus("current")
_RdEncryptTableEntry_Object = MibTableRow
rdEncryptTableEntry = _RdEncryptTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1)
)
rdEncryptTableEntry.setIndexNames(
    (0, "SIAE-RADIO-ENCRYPTION-MIB", "rdEncryptIfIndex"),
)
if mibBuilder.loadTexts:
    rdEncryptTableEntry.setStatus("current")
_RdEncryptIfIndex_Type = InterfaceIndex
_RdEncryptIfIndex_Object = MibTableColumn
rdEncryptIfIndex = _RdEncryptIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 1),
    _RdEncryptIfIndex_Type()
)
rdEncryptIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdEncryptIfIndex.setStatus("current")
_RdEncryptRowStatus_Type = RowStatus
_RdEncryptRowStatus_Object = MibTableColumn
rdEncryptRowStatus = _RdEncryptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 2),
    _RdEncryptRowStatus_Type()
)
rdEncryptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdEncryptRowStatus.setStatus("current")


class _RdEncryptAdminStatus_Type(Integer32):
    """Custom type rdEncryptAdminStatus based on Integer32"""
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


_RdEncryptAdminStatus_Type.__name__ = "Integer32"
_RdEncryptAdminStatus_Object = MibTableColumn
rdEncryptAdminStatus = _RdEncryptAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 3),
    _RdEncryptAdminStatus_Type()
)
rdEncryptAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdEncryptAdminStatus.setStatus("current")


class _RdEncryptAlgo_Type(Integer32):
    """Custom type rdEncryptAlgo based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes128", 1),
          ("aes256", 2))
    )


_RdEncryptAlgo_Type.__name__ = "Integer32"
_RdEncryptAlgo_Object = MibTableColumn
rdEncryptAlgo = _RdEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 4),
    _RdEncryptAlgo_Type()
)
rdEncryptAlgo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdEncryptAlgo.setStatus("current")


class _RdEncryptAlgoMode_Type(Integer32):
    """Custom type rdEncryptAlgoMode based on Integer32"""
    defaultValue = 5

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
        *(("aesModeElectronicCodebook", 1),
          ("aesModeCipherBlockChaining", 2),
          ("aesModeCipherFeedback", 3),
          ("aesModeOutputFeedback", 4),
          ("aesModeCounter", 5))
    )


_RdEncryptAlgoMode_Type.__name__ = "Integer32"
_RdEncryptAlgoMode_Object = MibTableColumn
rdEncryptAlgoMode = _RdEncryptAlgoMode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 5),
    _RdEncryptAlgoMode_Type()
)
rdEncryptAlgoMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdEncryptAlgoMode.setStatus("current")


class _RdEncryptKeyMode_Type(Integer32):
    """Custom type rdEncryptKeyMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manualEnteredKey", 1),
          ("automaticKeyGeneration", 2))
    )


_RdEncryptKeyMode_Type.__name__ = "Integer32"
_RdEncryptKeyMode_Object = MibTableColumn
rdEncryptKeyMode = _RdEncryptKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 6),
    _RdEncryptKeyMode_Type()
)
rdEncryptKeyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdEncryptKeyMode.setStatus("current")


class _RdEncryptKey_Type(OctetString):
    """Custom type rdEncryptKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(32, 32),
    )


_RdEncryptKey_Type.__name__ = "OctetString"
_RdEncryptKey_Object = MibTableColumn
rdEncryptKey = _RdEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 7),
    _RdEncryptKey_Type()
)
rdEncryptKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdEncryptKey.setStatus("current")


class _RdEncryptKeyLifeTime_Type(Integer32):
    """Custom type rdEncryptKeyLifeTime based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1096),
    )


_RdEncryptKeyLifeTime_Type.__name__ = "Integer32"
_RdEncryptKeyLifeTime_Object = MibTableColumn
rdEncryptKeyLifeTime = _RdEncryptKeyLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 8),
    _RdEncryptKeyLifeTime_Type()
)
rdEncryptKeyLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdEncryptKeyLifeTime.setStatus("current")
_RdEncryptMismatchAlarm_Type = AlarmStatus
_RdEncryptMismatchAlarm_Object = MibTableColumn
rdEncryptMismatchAlarm = _RdEncryptMismatchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 9),
    _RdEncryptMismatchAlarm_Type()
)
rdEncryptMismatchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdEncryptMismatchAlarm.setStatus("current")


class _RdEncryptSystemControl_Type(Integer32):
    """Custom type rdEncryptSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_RdEncryptSystemControl_Type.__name__ = "Integer32"
_RdEncryptSystemControl_Object = MibScalar
rdEncryptSystemControl = _RdEncryptSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 96, 3),
    _RdEncryptSystemControl_Type()
)
rdEncryptSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdEncryptSystemControl.setStatus("current")


class _RdEncryptMismatchAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type rdEncryptMismatchAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_RdEncryptMismatchAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_RdEncryptMismatchAlarmSeverityCode_Object = MibScalar
rdEncryptMismatchAlarmSeverityCode = _RdEncryptMismatchAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 96, 4),
    _RdEncryptMismatchAlarmSeverityCode_Type()
)
rdEncryptMismatchAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdEncryptMismatchAlarmSeverityCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-RADIO-ENCRYPTION-MIB",
    **{"radioEncrypt": radioEncrypt,
       "rdEncryptMibVersion": rdEncryptMibVersion,
       "rdEncryptTable": rdEncryptTable,
       "rdEncryptTableEntry": rdEncryptTableEntry,
       "rdEncryptIfIndex": rdEncryptIfIndex,
       "rdEncryptRowStatus": rdEncryptRowStatus,
       "rdEncryptAdminStatus": rdEncryptAdminStatus,
       "rdEncryptAlgo": rdEncryptAlgo,
       "rdEncryptAlgoMode": rdEncryptAlgoMode,
       "rdEncryptKeyMode": rdEncryptKeyMode,
       "rdEncryptKey": rdEncryptKey,
       "rdEncryptKeyLifeTime": rdEncryptKeyLifeTime,
       "rdEncryptMismatchAlarm": rdEncryptMismatchAlarm,
       "rdEncryptSystemControl": rdEncryptSystemControl,
       "rdEncryptMismatchAlarmSeverityCode": rdEncryptMismatchAlarmSeverityCode}
)
