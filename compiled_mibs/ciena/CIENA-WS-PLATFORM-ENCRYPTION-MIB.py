# SNMP MIB module (CIENA-WS-PLATFORM-ENCRYPTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-PLATFORM-ENCRYPTION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:08 2025
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

(cienaWsPlatformConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsPlatformConfig")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

cienaWsPlatformEncryptionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23)
)
if mibBuilder.loadTexts:
    cienaWsPlatformEncryptionMIB.setRevisions(
        ("2018-08-22 00:00",
         "2018-07-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AuthenticationMaterialType(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("preSharedKey", 1),
          ("certificateECC", 2))
    )



class WarmRestartType(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("fips", 1),
          ("nonFIPS", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CienaWsEncryptionObjects_ObjectIdentity = ObjectIdentity
cienaWsEncryptionObjects = _CienaWsEncryptionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 1)
)
_CienaWsEncryptionConformance_ObjectIdentity = ObjectIdentity
cienaWsEncryptionConformance = _CienaWsEncryptionConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 2)
)
_CienaWsEncryptionGroups_ObjectIdentity = ObjectIdentity
cienaWsEncryptionGroups = _CienaWsEncryptionGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 2, 1)
)
_CienaWsEncryptionCompliances_ObjectIdentity = ObjectIdentity
cienaWsEncryptionCompliances = _CienaWsEncryptionCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 2, 2)
)
_ChannelEncryptionTable_Object = MibTable
channelEncryptionTable = _ChannelEncryptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 3)
)
if mibBuilder.loadTexts:
    channelEncryptionTable.setStatus("current")
_ChannelEncryptionEntry_Object = MibTableRow
channelEncryptionEntry = _ChannelEncryptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 3, 1)
)
channelEncryptionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    channelEncryptionEntry.setStatus("current")
_ChannelDescr_Type = DisplayString
_ChannelDescr_Object = MibTableColumn
channelDescr = _ChannelDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 3, 1, 1),
    _ChannelDescr_Type()
)
channelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelDescr.setStatus("current")


class _PeerAuthenticationStatus_Type(Integer32):
    """Custom type peerAuthenticationStatus based on Integer32"""
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


_PeerAuthenticationStatus_Type.__name__ = "Integer32"
_PeerAuthenticationStatus_Object = MibTableColumn
peerAuthenticationStatus = _PeerAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 3, 1, 2),
    _PeerAuthenticationStatus_Type()
)
peerAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerAuthenticationStatus.setStatus("current")
_PeerAuthenticationStatusUpdateTime_Type = DisplayString
_PeerAuthenticationStatusUpdateTime_Object = MibTableColumn
peerAuthenticationStatusUpdateTime = _PeerAuthenticationStatusUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 3, 1, 3),
    _PeerAuthenticationStatusUpdateTime_Type()
)
peerAuthenticationStatusUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerAuthenticationStatusUpdateTime.setStatus("current")
_EncryptionPreSharedKeyTable_Object = MibTable
encryptionPreSharedKeyTable = _EncryptionPreSharedKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 4)
)
if mibBuilder.loadTexts:
    encryptionPreSharedKeyTable.setStatus("current")
_EncryptionPreSharedKeyEntry_Object = MibTableRow
encryptionPreSharedKeyEntry = _EncryptionPreSharedKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 4, 1)
)
encryptionPreSharedKeyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    encryptionPreSharedKeyEntry.setStatus("current")
_EncryptionPreSharedChannelDescr_Type = DisplayString
_EncryptionPreSharedChannelDescr_Object = MibTableColumn
encryptionPreSharedChannelDescr = _EncryptionPreSharedChannelDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 4, 1, 1),
    _EncryptionPreSharedChannelDescr_Type()
)
encryptionPreSharedChannelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionPreSharedChannelDescr.setStatus("current")
_EncryptionPreSharedKeyFingerprint_Type = DisplayString
_EncryptionPreSharedKeyFingerprint_Object = MibTableColumn
encryptionPreSharedKeyFingerprint = _EncryptionPreSharedKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 4, 1, 2),
    _EncryptionPreSharedKeyFingerprint_Type()
)
encryptionPreSharedKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionPreSharedKeyFingerprint.setStatus("current")
_EncryptionPreSharedKeyStatus_Type = TruthValue
_EncryptionPreSharedKeyStatus_Object = MibTableColumn
encryptionPreSharedKeyStatus = _EncryptionPreSharedKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 4, 1, 3),
    _EncryptionPreSharedKeyStatus_Type()
)
encryptionPreSharedKeyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionPreSharedKeyStatus.setStatus("current")
_EncryptionPreSharedKeyDescription_Type = DisplayString
_EncryptionPreSharedKeyDescription_Object = MibTableColumn
encryptionPreSharedKeyDescription = _EncryptionPreSharedKeyDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 4, 1, 4),
    _EncryptionPreSharedKeyDescription_Type()
)
encryptionPreSharedKeyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encryptionPreSharedKeyDescription.setStatus("current")
_SystemEncryptionTable_Object = MibTable
systemEncryptionTable = _SystemEncryptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 5)
)
if mibBuilder.loadTexts:
    systemEncryptionTable.setStatus("current")
_SystemEncryptionEntry_Object = MibTableRow
systemEncryptionEntry = _SystemEncryptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 5, 1)
)
systemEncryptionEntry.setIndexNames(
    (0, "CIENA-WS-PLATFORM-ENCRYPTION-MIB", "systemEncryptionTableSnmpKey"),
)
if mibBuilder.loadTexts:
    systemEncryptionEntry.setStatus("current")


class _SystemEncryptionTableSnmpKey_Type(Integer32):
    """Custom type systemEncryptionTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SystemEncryptionTableSnmpKey_Type.__name__ = "Integer32"
_SystemEncryptionTableSnmpKey_Object = MibTableColumn
systemEncryptionTableSnmpKey = _SystemEncryptionTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 5, 1, 1),
    _SystemEncryptionTableSnmpKey_Type()
)
systemEncryptionTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemEncryptionTableSnmpKey.setStatus("current")
_AuthenticationMaterialType_Type = AuthenticationMaterialType
_AuthenticationMaterialType_Object = MibTableColumn
authenticationMaterialType = _AuthenticationMaterialType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 5, 1, 2),
    _AuthenticationMaterialType_Type()
)
authenticationMaterialType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticationMaterialType.setStatus("current")
_WarmRestartType_Type = WarmRestartType
_WarmRestartType_Object = MibTableColumn
warmRestartType = _WarmRestartType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 5, 1, 3),
    _WarmRestartType_Type()
)
warmRestartType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    warmRestartType.setStatus("current")
_SigningCACertificate_Type = DisplayString
_SigningCACertificate_Object = MibTableColumn
signingCACertificate = _SigningCACertificate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 5, 1, 4),
    _SigningCACertificate_Type()
)
signingCACertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signingCACertificate.setStatus("current")
_EntityCertificate_Type = DisplayString
_EntityCertificate_Object = MibTableColumn
entityCertificate = _EntityCertificate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 5, 1, 5),
    _EntityCertificate_Type()
)
entityCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityCertificate.setStatus("current")

# Managed Objects groups

cienaWsEncryptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 2, 1, 1)
)
cienaWsEncryptionGroup.setObjects(
      *(("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "channelDescr"),
        ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "peerAuthenticationStatus"),
        ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "peerAuthenticationStatusUpdateTime"),
        ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "encryptionPreSharedChannelDescr"),
        ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "encryptionPreSharedKeyFingerprint"),
        ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "encryptionPreSharedKeyStatus"),
        ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "encryptionPreSharedKeyDescription"),
        ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "authenticationMaterialType"),
        ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "warmRestartType"),
        ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "signingCACertificate"),
        ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "entityCertificate"))
)
if mibBuilder.loadTexts:
    cienaWsEncryptionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsEncryptionCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 2, 2, 1)
)
cienaWsEncryptionCompliance.setObjects(
    ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "cienaWsEncryptionGroup")
)
if mibBuilder.loadTexts:
    cienaWsEncryptionCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-PLATFORM-ENCRYPTION-MIB",
    **{"AuthenticationMaterialType": AuthenticationMaterialType,
       "WarmRestartType": WarmRestartType,
       "cienaWsPlatformEncryptionMIB": cienaWsPlatformEncryptionMIB,
       "cienaWsEncryptionObjects": cienaWsEncryptionObjects,
       "cienaWsEncryptionConformance": cienaWsEncryptionConformance,
       "cienaWsEncryptionGroups": cienaWsEncryptionGroups,
       "cienaWsEncryptionGroup": cienaWsEncryptionGroup,
       "cienaWsEncryptionCompliances": cienaWsEncryptionCompliances,
       "cienaWsEncryptionCompliance": cienaWsEncryptionCompliance,
       "channelEncryptionTable": channelEncryptionTable,
       "channelEncryptionEntry": channelEncryptionEntry,
       "channelDescr": channelDescr,
       "peerAuthenticationStatus": peerAuthenticationStatus,
       "peerAuthenticationStatusUpdateTime": peerAuthenticationStatusUpdateTime,
       "encryptionPreSharedKeyTable": encryptionPreSharedKeyTable,
       "encryptionPreSharedKeyEntry": encryptionPreSharedKeyEntry,
       "encryptionPreSharedChannelDescr": encryptionPreSharedChannelDescr,
       "encryptionPreSharedKeyFingerprint": encryptionPreSharedKeyFingerprint,
       "encryptionPreSharedKeyStatus": encryptionPreSharedKeyStatus,
       "encryptionPreSharedKeyDescription": encryptionPreSharedKeyDescription,
       "systemEncryptionTable": systemEncryptionTable,
       "systemEncryptionEntry": systemEncryptionEntry,
       "systemEncryptionTableSnmpKey": systemEncryptionTableSnmpKey,
       "authenticationMaterialType": authenticationMaterialType,
       "warmRestartType": warmRestartType,
       "signingCACertificate": signingCACertificate,
       "entityCertificate": entityCertificate}
)
