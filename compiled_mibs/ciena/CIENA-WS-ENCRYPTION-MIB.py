# SNMP MIB module (CIENA-WS-ENCRYPTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-ENCRYPTION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:05 2025
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

(cienaWsConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsConfig")

(PortId,
 StringMaxl32) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "PortId",
    "StringMaxl32")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaWsEncryptionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23)
)
if mibBuilder.loadTexts:
    cienaWsEncryptionMIB.setRevisions(
        ("2017-03-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaWsEncryptionObjects_ObjectIdentity = ObjectIdentity
cienaWsEncryptionObjects = _CienaWsEncryptionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 1)
)
_CienaWsEncryptionConformance_ObjectIdentity = ObjectIdentity
cienaWsEncryptionConformance = _CienaWsEncryptionConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 2)
)
_CienaWsEncryptionGroups_ObjectIdentity = ObjectIdentity
cienaWsEncryptionGroups = _CienaWsEncryptionGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 2, 1)
)
_CienaWsEncryptionCompliances_ObjectIdentity = ObjectIdentity
cienaWsEncryptionCompliances = _CienaWsEncryptionCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 2, 2)
)
_CwsEncryptionPortEncryptionTable_Object = MibTable
cwsEncryptionPortEncryptionTable = _CwsEncryptionPortEncryptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 3)
)
if mibBuilder.loadTexts:
    cwsEncryptionPortEncryptionTable.setStatus("current")
_CwsEncryptionPortEncryptionEntry_Object = MibTableRow
cwsEncryptionPortEncryptionEntry = _CwsEncryptionPortEncryptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 3, 1)
)
cwsEncryptionPortEncryptionEntry.setIndexNames(
    (0, "CIENA-WS-ENCRYPTION-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-ENCRYPTION-MIB", "cwsEncryptionPortEncryptionTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsEncryptionPortEncryptionEntry.setStatus("current")


class _CwsEncryptionPortEncryptionTableSnmpKey_Type(Integer32):
    """Custom type cwsEncryptionPortEncryptionTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsEncryptionPortEncryptionTableSnmpKey_Type.__name__ = "Integer32"
_CwsEncryptionPortEncryptionTableSnmpKey_Object = MibTableColumn
cwsEncryptionPortEncryptionTableSnmpKey = _CwsEncryptionPortEncryptionTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 3, 1, 1),
    _CwsEncryptionPortEncryptionTableSnmpKey_Type()
)
cwsEncryptionPortEncryptionTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsEncryptionPortEncryptionTableSnmpKey.setStatus("current")


class _CwsEncryptionPortEncryptionPeerAuthenticationStatus_Type(Integer32):
    """Custom type cwsEncryptionPortEncryptionPeerAuthenticationStatus based on Integer32"""
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
          ("pass", 1),
          ("fail", 2))
    )


_CwsEncryptionPortEncryptionPeerAuthenticationStatus_Type.__name__ = "Integer32"
_CwsEncryptionPortEncryptionPeerAuthenticationStatus_Object = MibTableColumn
cwsEncryptionPortEncryptionPeerAuthenticationStatus = _CwsEncryptionPortEncryptionPeerAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 3, 1, 2),
    _CwsEncryptionPortEncryptionPeerAuthenticationStatus_Type()
)
cwsEncryptionPortEncryptionPeerAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsEncryptionPortEncryptionPeerAuthenticationStatus.setStatus("current")
_CwsEncryptionPreSharedKeyTable_Object = MibTable
cwsEncryptionPreSharedKeyTable = _CwsEncryptionPreSharedKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 4)
)
if mibBuilder.loadTexts:
    cwsEncryptionPreSharedKeyTable.setStatus("current")
_CwsEncryptionPreSharedKeyEntry_Object = MibTableRow
cwsEncryptionPreSharedKeyEntry = _CwsEncryptionPreSharedKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 4, 1)
)
cwsEncryptionPreSharedKeyEntry.setIndexNames(
    (0, "CIENA-WS-ENCRYPTION-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-ENCRYPTION-MIB", "cwsEncryptionPreSharedKeyTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsEncryptionPreSharedKeyEntry.setStatus("current")


class _CwsEncryptionPreSharedKeyTableSnmpKey_Type(Integer32):
    """Custom type cwsEncryptionPreSharedKeyTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsEncryptionPreSharedKeyTableSnmpKey_Type.__name__ = "Integer32"
_CwsEncryptionPreSharedKeyTableSnmpKey_Object = MibTableColumn
cwsEncryptionPreSharedKeyTableSnmpKey = _CwsEncryptionPreSharedKeyTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 4, 1, 1),
    _CwsEncryptionPreSharedKeyTableSnmpKey_Type()
)
cwsEncryptionPreSharedKeyTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsEncryptionPreSharedKeyTableSnmpKey.setStatus("current")


class _CwsEncryptionPreSharedKeyValue_Type(OctetString):
    """Custom type cwsEncryptionPreSharedKeyValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CwsEncryptionPreSharedKeyValue_Type.__name__ = "OctetString"
_CwsEncryptionPreSharedKeyValue_Object = MibTableColumn
cwsEncryptionPreSharedKeyValue = _CwsEncryptionPreSharedKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 4, 1, 2),
    _CwsEncryptionPreSharedKeyValue_Type()
)
cwsEncryptionPreSharedKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsEncryptionPreSharedKeyValue.setStatus("current")
_CwsEncryptionPreSharedKeyFingerprint_Type = StringMaxl32
_CwsEncryptionPreSharedKeyFingerprint_Object = MibTableColumn
cwsEncryptionPreSharedKeyFingerprint = _CwsEncryptionPreSharedKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 4, 1, 3),
    _CwsEncryptionPreSharedKeyFingerprint_Type()
)
cwsEncryptionPreSharedKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsEncryptionPreSharedKeyFingerprint.setStatus("current")
_CwsEncryptionPreSharedKeyStatus_Type = TruthValue
_CwsEncryptionPreSharedKeyStatus_Object = MibTableColumn
cwsEncryptionPreSharedKeyStatus = _CwsEncryptionPreSharedKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 4, 1, 4),
    _CwsEncryptionPreSharedKeyStatus_Type()
)
cwsEncryptionPreSharedKeyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsEncryptionPreSharedKeyStatus.setStatus("current")


class _CwsEncryptionPreSharedKeyDescription_Type(OctetString):
    """Custom type cwsEncryptionPreSharedKeyDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_CwsEncryptionPreSharedKeyDescription_Type.__name__ = "OctetString"
_CwsEncryptionPreSharedKeyDescription_Object = MibTableColumn
cwsEncryptionPreSharedKeyDescription = _CwsEncryptionPreSharedKeyDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 4, 1, 5),
    _CwsEncryptionPreSharedKeyDescription_Type()
)
cwsEncryptionPreSharedKeyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsEncryptionPreSharedKeyDescription.setStatus("current")
_CwsEncryptionReAuthenticationTable_Object = MibTable
cwsEncryptionReAuthenticationTable = _CwsEncryptionReAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 5)
)
if mibBuilder.loadTexts:
    cwsEncryptionReAuthenticationTable.setStatus("current")
_CwsEncryptionReAuthenticationEntry_Object = MibTableRow
cwsEncryptionReAuthenticationEntry = _CwsEncryptionReAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 5, 1)
)
cwsEncryptionReAuthenticationEntry.setIndexNames(
    (0, "CIENA-WS-ENCRYPTION-MIB", "cwsPortPortsPortId"),
    (0, "CIENA-WS-ENCRYPTION-MIB", "cwsEncryptionReAuthenticationTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsEncryptionReAuthenticationEntry.setStatus("current")


class _CwsEncryptionReAuthenticationTableSnmpKey_Type(Integer32):
    """Custom type cwsEncryptionReAuthenticationTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsEncryptionReAuthenticationTableSnmpKey_Type.__name__ = "Integer32"
_CwsEncryptionReAuthenticationTableSnmpKey_Object = MibTableColumn
cwsEncryptionReAuthenticationTableSnmpKey = _CwsEncryptionReAuthenticationTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 5, 1, 1),
    _CwsEncryptionReAuthenticationTableSnmpKey_Type()
)
cwsEncryptionReAuthenticationTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsEncryptionReAuthenticationTableSnmpKey.setStatus("current")
_CwsEncryptionReAuthenticationPeriod_Type = Unsigned32
_CwsEncryptionReAuthenticationPeriod_Object = MibTableColumn
cwsEncryptionReAuthenticationPeriod = _CwsEncryptionReAuthenticationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 5, 1, 2),
    _CwsEncryptionReAuthenticationPeriod_Type()
)
cwsEncryptionReAuthenticationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsEncryptionReAuthenticationPeriod.setStatus("current")


class _CwsEncryptionReAuthenticationFailureMode_Type(Integer32):
    """Custom type cwsEncryptionReAuthenticationFailureMode based on Integer32"""
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
          ("drop", 1),
          ("allow", 2))
    )


_CwsEncryptionReAuthenticationFailureMode_Type.__name__ = "Integer32"
_CwsEncryptionReAuthenticationFailureMode_Object = MibTableColumn
cwsEncryptionReAuthenticationFailureMode = _CwsEncryptionReAuthenticationFailureMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 5, 1, 3),
    _CwsEncryptionReAuthenticationFailureMode_Type()
)
cwsEncryptionReAuthenticationFailureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsEncryptionReAuthenticationFailureMode.setStatus("current")
_CwsEncryptionEncryptionStateTable_Object = MibTable
cwsEncryptionEncryptionStateTable = _CwsEncryptionEncryptionStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 6)
)
if mibBuilder.loadTexts:
    cwsEncryptionEncryptionStateTable.setStatus("current")
_CwsEncryptionEncryptionStateEntry_Object = MibTableRow
cwsEncryptionEncryptionStateEntry = _CwsEncryptionEncryptionStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 6, 1)
)
cwsEncryptionEncryptionStateEntry.setIndexNames(
    (0, "CIENA-WS-ENCRYPTION-MIB", "cwsEncryptionEncryptionStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsEncryptionEncryptionStateEntry.setStatus("current")


class _CwsEncryptionEncryptionStateTableSnmpKey_Type(Integer32):
    """Custom type cwsEncryptionEncryptionStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsEncryptionEncryptionStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsEncryptionEncryptionStateTableSnmpKey_Object = MibTableColumn
cwsEncryptionEncryptionStateTableSnmpKey = _CwsEncryptionEncryptionStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 6, 1, 1),
    _CwsEncryptionEncryptionStateTableSnmpKey_Type()
)
cwsEncryptionEncryptionStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsEncryptionEncryptionStateTableSnmpKey.setStatus("current")


class _CwsEncryptionEncryptionStateLicenseState_Type(Integer32):
    """Custom type cwsEncryptionEncryptionStateLicenseState based on Integer32"""
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
        *(("missing", 0),
          ("available", 1),
          ("held", 2),
          ("na", 3))
    )


_CwsEncryptionEncryptionStateLicenseState_Type.__name__ = "Integer32"
_CwsEncryptionEncryptionStateLicenseState_Object = MibTableColumn
cwsEncryptionEncryptionStateLicenseState = _CwsEncryptionEncryptionStateLicenseState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 6, 1, 2),
    _CwsEncryptionEncryptionStateLicenseState_Type()
)
cwsEncryptionEncryptionStateLicenseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsEncryptionEncryptionStateLicenseState.setStatus("current")


class _CwsEncryptionEncryptionStateFeatureState_Type(Integer32):
    """Custom type cwsEncryptionEncryptionStateFeatureState based on Integer32"""
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
        *(("notSupported", 0),
          ("notReady", 1),
          ("ready", 2),
          ("na", 3))
    )


_CwsEncryptionEncryptionStateFeatureState_Type.__name__ = "Integer32"
_CwsEncryptionEncryptionStateFeatureState_Object = MibTableColumn
cwsEncryptionEncryptionStateFeatureState = _CwsEncryptionEncryptionStateFeatureState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 6, 1, 3),
    _CwsEncryptionEncryptionStateFeatureState_Type()
)
cwsEncryptionEncryptionStateFeatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsEncryptionEncryptionStateFeatureState.setStatus("current")

# Managed Objects groups

cienaWsEncryptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 2, 1, 1)
)
cienaWsEncryptionGroup.setObjects(
      *(("CIENA-WS-ENCRYPTION-MIB", "cwsEncryptionPortEncryptionPeerAuthenticationStatus"),
        ("CIENA-WS-ENCRYPTION-MIB", "cwsEncryptionPreSharedKeyValue"),
        ("CIENA-WS-ENCRYPTION-MIB", "cwsEncryptionPreSharedKeyFingerprint"),
        ("CIENA-WS-ENCRYPTION-MIB", "cwsEncryptionPreSharedKeyStatus"),
        ("CIENA-WS-ENCRYPTION-MIB", "cwsEncryptionPreSharedKeyDescription"),
        ("CIENA-WS-ENCRYPTION-MIB", "cwsEncryptionReAuthenticationPeriod"),
        ("CIENA-WS-ENCRYPTION-MIB", "cwsEncryptionReAuthenticationFailureMode"),
        ("CIENA-WS-ENCRYPTION-MIB", "cwsEncryptionEncryptionStateLicenseState"),
        ("CIENA-WS-ENCRYPTION-MIB", "cwsEncryptionEncryptionStateFeatureState"))
)
if mibBuilder.loadTexts:
    cienaWsEncryptionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsEncryptionCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 23, 2, 2, 1)
)
cienaWsEncryptionCompliance.setObjects(
    ("CIENA-WS-ENCRYPTION-MIB", "cienaWsEncryptionGroup")
)
if mibBuilder.loadTexts:
    cienaWsEncryptionCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-ENCRYPTION-MIB",
    **{"cienaWsEncryptionMIB": cienaWsEncryptionMIB,
       "cienaWsEncryptionObjects": cienaWsEncryptionObjects,
       "cienaWsEncryptionConformance": cienaWsEncryptionConformance,
       "cienaWsEncryptionGroups": cienaWsEncryptionGroups,
       "cienaWsEncryptionGroup": cienaWsEncryptionGroup,
       "cienaWsEncryptionCompliances": cienaWsEncryptionCompliances,
       "cienaWsEncryptionCompliance": cienaWsEncryptionCompliance,
       "cwsEncryptionPortEncryptionTable": cwsEncryptionPortEncryptionTable,
       "cwsEncryptionPortEncryptionEntry": cwsEncryptionPortEncryptionEntry,
       "cwsEncryptionPortEncryptionTableSnmpKey": cwsEncryptionPortEncryptionTableSnmpKey,
       "cwsEncryptionPortEncryptionPeerAuthenticationStatus": cwsEncryptionPortEncryptionPeerAuthenticationStatus,
       "cwsEncryptionPreSharedKeyTable": cwsEncryptionPreSharedKeyTable,
       "cwsEncryptionPreSharedKeyEntry": cwsEncryptionPreSharedKeyEntry,
       "cwsEncryptionPreSharedKeyTableSnmpKey": cwsEncryptionPreSharedKeyTableSnmpKey,
       "cwsEncryptionPreSharedKeyValue": cwsEncryptionPreSharedKeyValue,
       "cwsEncryptionPreSharedKeyFingerprint": cwsEncryptionPreSharedKeyFingerprint,
       "cwsEncryptionPreSharedKeyStatus": cwsEncryptionPreSharedKeyStatus,
       "cwsEncryptionPreSharedKeyDescription": cwsEncryptionPreSharedKeyDescription,
       "cwsEncryptionReAuthenticationTable": cwsEncryptionReAuthenticationTable,
       "cwsEncryptionReAuthenticationEntry": cwsEncryptionReAuthenticationEntry,
       "cwsEncryptionReAuthenticationTableSnmpKey": cwsEncryptionReAuthenticationTableSnmpKey,
       "cwsEncryptionReAuthenticationPeriod": cwsEncryptionReAuthenticationPeriod,
       "cwsEncryptionReAuthenticationFailureMode": cwsEncryptionReAuthenticationFailureMode,
       "cwsEncryptionEncryptionStateTable": cwsEncryptionEncryptionStateTable,
       "cwsEncryptionEncryptionStateEntry": cwsEncryptionEncryptionStateEntry,
       "cwsEncryptionEncryptionStateTableSnmpKey": cwsEncryptionEncryptionStateTableSnmpKey,
       "cwsEncryptionEncryptionStateLicenseState": cwsEncryptionEncryptionStateLicenseState,
       "cwsEncryptionEncryptionStateFeatureState": cwsEncryptionEncryptionStateFeatureState}
)
