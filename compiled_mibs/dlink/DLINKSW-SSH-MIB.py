# SNMP MIB module (DLINKSW-SSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-SSH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:37:52 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwSshMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 17)
)
if mibBuilder.loadTexts:
    dlinkSwSshMIB.setRevisions(
        ("2013-07-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DSshNotifications_ObjectIdentity = ObjectIdentity
dSshNotifications = _DSshNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 0)
)
_DSshObjects_ObjectIdentity = ObjectIdentity
dSshObjects = _DSshObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1)
)
_DSshGeneral_ObjectIdentity = ObjectIdentity
dSshGeneral = _DSshGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 1)
)


class _DSshEnabled_Type(TruthValue):
    """Custom type dSshEnabled based on TruthValue"""
    defaultValue = 2


_DSshEnabled_Type.__name__ = "TruthValue"
_DSshEnabled_Object = MibScalar
dSshEnabled = _DSshEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 1, 1),
    _DSshEnabled_Type()
)
dSshEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSshEnabled.setStatus("current")


class _DSshVersion_Type(Integer32):
    """Custom type dSshVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v1v2", 3))
    )


_DSshVersion_Type.__name__ = "Integer32"
_DSshVersion_Object = MibScalar
dSshVersion = _DSshVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 1, 2),
    _DSshVersion_Type()
)
dSshVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSshVersion.setStatus("current")


class _DSshTimeout_Type(Integer32):
    """Custom type dSshTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_DSshTimeout_Type.__name__ = "Integer32"
_DSshTimeout_Object = MibScalar
dSshTimeout = _DSshTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 1, 3),
    _DSshTimeout_Type()
)
dSshTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSshTimeout.setStatus("current")
if mibBuilder.loadTexts:
    dSshTimeout.setUnits("seconds")


class _DSshAuthenticationRetries_Type(Integer32):
    """Custom type dSshAuthenticationRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DSshAuthenticationRetries_Type.__name__ = "Integer32"
_DSshAuthenticationRetries_Object = MibScalar
dSshAuthenticationRetries = _DSshAuthenticationRetries_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 1, 4),
    _DSshAuthenticationRetries_Type()
)
dSshAuthenticationRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSshAuthenticationRetries.setStatus("current")


class _DSshServicePort_Type(Unsigned32):
    """Custom type dSshServicePort based on Unsigned32"""
    defaultValue = 22


_DSshServicePort_Type.__name__ = "Unsigned32"
_DSshServicePort_Object = MibScalar
dSshServicePort = _DSshServicePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 1, 5),
    _DSshServicePort_Type()
)
dSshServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSshServicePort.setStatus("current")


class _DSshSrcIfIndex_Type(InterfaceIndexOrZero):
    """Custom type dSshSrcIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_DSshSrcIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_DSshSrcIfIndex_Object = MibScalar
dSshSrcIfIndex = _DSshSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 1, 6),
    _DSshSrcIfIndex_Type()
)
dSshSrcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSshSrcIfIndex.setStatus("current")
_DSshKeyConfiguration_ObjectIdentity = ObjectIdentity
dSshKeyConfiguration = _DSshKeyConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 2)
)
_DSshCryptoKeyPairTable_Object = MibTable
dSshCryptoKeyPairTable = _DSshCryptoKeyPairTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dSshCryptoKeyPairTable.setStatus("current")
_DSshCryptoKeyPairEntry_Object = MibTableRow
dSshCryptoKeyPairEntry = _DSshCryptoKeyPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 2, 1, 1)
)
dSshCryptoKeyPairEntry.setIndexNames(
    (0, "DLINKSW-SSH-MIB", "dSshCryptoKeyPairIndex"),
)
if mibBuilder.loadTexts:
    dSshCryptoKeyPairEntry.setStatus("current")


class _DSshCryptoKeyPairIndex_Type(Integer32):
    """Custom type dSshCryptoKeyPairIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rsa", 1),
          ("dsa", 2))
    )


_DSshCryptoKeyPairIndex_Type.__name__ = "Integer32"
_DSshCryptoKeyPairIndex_Object = MibTableColumn
dSshCryptoKeyPairIndex = _DSshCryptoKeyPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 2, 1, 1, 1),
    _DSshCryptoKeyPairIndex_Type()
)
dSshCryptoKeyPairIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSshCryptoKeyPairIndex.setStatus("current")


class _DSshCryptoKeyPairNBits_Type(Integer32):
    """Custom type dSshCryptoKeyPairNBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(360, 360),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(768, 768),
        ValueRangeConstraint(1024, 1024),
        ValueRangeConstraint(2048, 2048),
    )


_DSshCryptoKeyPairNBits_Type.__name__ = "Integer32"
_DSshCryptoKeyPairNBits_Object = MibTableColumn
dSshCryptoKeyPairNBits = _DSshCryptoKeyPairNBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 2, 1, 1, 2),
    _DSshCryptoKeyPairNBits_Type()
)
dSshCryptoKeyPairNBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSshCryptoKeyPairNBits.setStatus("current")
_DSshCryptoKeyPairReplace_Type = TruthValue
_DSshCryptoKeyPairReplace_Object = MibTableColumn
dSshCryptoKeyPairReplace = _DSshCryptoKeyPairReplace_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 2, 1, 1, 3),
    _DSshCryptoKeyPairReplace_Type()
)
dSshCryptoKeyPairReplace.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSshCryptoKeyPairReplace.setStatus("current")
_DSshCryptoKeyPairLastCreateTime_Type = TimeStamp
_DSshCryptoKeyPairLastCreateTime_Object = MibTableColumn
dSshCryptoKeyPairLastCreateTime = _DSshCryptoKeyPairLastCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 2, 1, 1, 4),
    _DSshCryptoKeyPairLastCreateTime_Type()
)
dSshCryptoKeyPairLastCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSshCryptoKeyPairLastCreateTime.setStatus("current")


class _DSshCryptoKeyPairString_Type(DisplayString):
    """Custom type dSshCryptoKeyPairString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DSshCryptoKeyPairString_Type.__name__ = "DisplayString"
_DSshCryptoKeyPairString_Object = MibTableColumn
dSshCryptoKeyPairString = _DSshCryptoKeyPairString_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 2, 1, 1, 6),
    _DSshCryptoKeyPairString_Type()
)
dSshCryptoKeyPairString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSshCryptoKeyPairString.setStatus("current")
_DSshCryptoKeyPairRowStatus_Type = RowStatus
_DSshCryptoKeyPairRowStatus_Object = MibTableColumn
dSshCryptoKeyPairRowStatus = _DSshCryptoKeyPairRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 2, 1, 1, 99),
    _DSshCryptoKeyPairRowStatus_Type()
)
dSshCryptoKeyPairRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSshCryptoKeyPairRowStatus.setStatus("current")


class _DSshCryptoKeyGenerationStatus_Type(Integer32):
    """Custom type dSshCryptoKeyGenerationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("successful", 2),
          ("failed", 3))
    )


_DSshCryptoKeyGenerationStatus_Type.__name__ = "Integer32"
_DSshCryptoKeyGenerationStatus_Object = MibScalar
dSshCryptoKeyGenerationStatus = _DSshCryptoKeyGenerationStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 2, 2),
    _DSshCryptoKeyGenerationStatus_Type()
)
dSshCryptoKeyGenerationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSshCryptoKeyGenerationStatus.setStatus("current")
_DSshConnectionTable_Object = MibTable
dSshConnectionTable = _DSshConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 3)
)
if mibBuilder.loadTexts:
    dSshConnectionTable.setStatus("current")
_DSshConnectionEntry_Object = MibTableRow
dSshConnectionEntry = _DSshConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 3, 1)
)
dSshConnectionEntry.setIndexNames(
    (0, "DLINKSW-SSH-MIB", "dSshConnectionSID"),
)
if mibBuilder.loadTexts:
    dSshConnectionEntry.setStatus("current")


class _DSshConnectionSID_Type(Integer32):
    """Custom type dSshConnectionSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DSshConnectionSID_Type.__name__ = "Integer32"
_DSshConnectionSID_Object = MibTableColumn
dSshConnectionSID = _DSshConnectionSID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 3, 1, 1),
    _DSshConnectionSID_Type()
)
dSshConnectionSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSshConnectionSID.setStatus("current")


class _DSshConnectionVersion_Type(Integer32):
    """Custom type dSshConnectionVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v1v2", 3))
    )


_DSshConnectionVersion_Type.__name__ = "Integer32"
_DSshConnectionVersion_Object = MibTableColumn
dSshConnectionVersion = _DSshConnectionVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 3, 1, 2),
    _DSshConnectionVersion_Type()
)
dSshConnectionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSshConnectionVersion.setStatus("current")
_DSshConnectionCipher_Type = DisplayString
_DSshConnectionCipher_Object = MibTableColumn
dSshConnectionCipher = _DSshConnectionCipher_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 3, 1, 3),
    _DSshConnectionCipher_Type()
)
dSshConnectionCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSshConnectionCipher.setStatus("current")
_DSshConnectionUserID_Type = DisplayString
_DSshConnectionUserID_Object = MibTableColumn
dSshConnectionUserID = _DSshConnectionUserID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 3, 1, 4),
    _DSshConnectionUserID_Type()
)
dSshConnectionUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSshConnectionUserID.setStatus("current")
_DSshConnectionHostAddrType_Type = InetAddressType
_DSshConnectionHostAddrType_Object = MibTableColumn
dSshConnectionHostAddrType = _DSshConnectionHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 3, 1, 5),
    _DSshConnectionHostAddrType_Type()
)
dSshConnectionHostAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSshConnectionHostAddrType.setStatus("current")
_DSshConnectionHostAddr_Type = InetAddress
_DSshConnectionHostAddr_Object = MibTableColumn
dSshConnectionHostAddr = _DSshConnectionHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 3, 1, 6),
    _DSshConnectionHostAddr_Type()
)
dSshConnectionHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSshConnectionHostAddr.setStatus("current")
_DSshUserTable_Object = MibTable
dSshUserTable = _DSshUserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 4)
)
if mibBuilder.loadTexts:
    dSshUserTable.setStatus("current")
_DSshUserEntry_Object = MibTableRow
dSshUserEntry = _DSshUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 4, 1)
)
dSshUserEntry.setIndexNames(
    (0, "DLINKSW-SSH-MIB", "dSshUserName"),
)
if mibBuilder.loadTexts:
    dSshUserEntry.setStatus("current")


class _DSshUserName_Type(SnmpAdminString):
    """Custom type dSshUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DSshUserName_Type.__name__ = "SnmpAdminString"
_DSshUserName_Object = MibTableColumn
dSshUserName = _DSshUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 4, 1, 1),
    _DSshUserName_Type()
)
dSshUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSshUserName.setStatus("current")


class _DSshUserAuthMethod_Type(Integer32):
    """Custom type dSshUserAuthMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("password", 1),
          ("publickey", 2),
          ("hostbased", 3))
    )


_DSshUserAuthMethod_Type.__name__ = "Integer32"
_DSshUserAuthMethod_Object = MibTableColumn
dSshUserAuthMethod = _DSshUserAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 4, 1, 2),
    _DSshUserAuthMethod_Type()
)
dSshUserAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSshUserAuthMethod.setStatus("current")


class _DSshUserKeyFilename_Type(SnmpAdminString):
    """Custom type dSshUserKeyFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DSshUserKeyFilename_Type.__name__ = "SnmpAdminString"
_DSshUserKeyFilename_Object = MibTableColumn
dSshUserKeyFilename = _DSshUserKeyFilename_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 4, 1, 3),
    _DSshUserKeyFilename_Type()
)
dSshUserKeyFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSshUserKeyFilename.setStatus("current")


class _DSshUserHostName_Type(DisplayString):
    """Custom type dSshUserHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DSshUserHostName_Type.__name__ = "DisplayString"
_DSshUserHostName_Object = MibTableColumn
dSshUserHostName = _DSshUserHostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 4, 1, 4),
    _DSshUserHostName_Type()
)
dSshUserHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSshUserHostName.setStatus("current")
_DSshUserHostAddrType_Type = InetAddressType
_DSshUserHostAddrType_Object = MibTableColumn
dSshUserHostAddrType = _DSshUserHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 4, 1, 5),
    _DSshUserHostAddrType_Type()
)
dSshUserHostAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSshUserHostAddrType.setStatus("current")
_DSshUserHostAddr_Type = InetAddress
_DSshUserHostAddr_Object = MibTableColumn
dSshUserHostAddr = _DSshUserHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 4, 1, 6),
    _DSshUserHostAddr_Type()
)
dSshUserHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSshUserHostAddr.setStatus("current")
_DSshUserRowStatus_Type = RowStatus
_DSshUserRowStatus_Object = MibTableColumn
dSshUserRowStatus = _DSshUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 1, 4, 1, 99),
    _DSshUserRowStatus_Type()
)
dSshUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSshUserRowStatus.setStatus("current")
_DSshConformance_ObjectIdentity = ObjectIdentity
dSshConformance = _DSshConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 2)
)
_DSshCompliances_ObjectIdentity = ObjectIdentity
dSshCompliances = _DSshCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 2, 1)
)
_DSshGroups_ObjectIdentity = ObjectIdentity
dSshGroups = _DSshGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 2, 2)
)

# Managed Objects groups

dSshConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 2, 2, 1)
)
dSshConfigGroup.setObjects(
      *(("DLINKSW-SSH-MIB", "dSshEnabled"),
        ("DLINKSW-SSH-MIB", "dSshVersion"),
        ("DLINKSW-SSH-MIB", "dSshTimeout"),
        ("DLINKSW-SSH-MIB", "dSshAuthenticationRetries"),
        ("DLINKSW-SSH-MIB", "dSshServicePort"),
        ("DLINKSW-SSH-MIB", "dSshSrcIfIndex"),
        ("DLINKSW-SSH-MIB", "dSshCryptoKeyPairNBits"),
        ("DLINKSW-SSH-MIB", "dSshCryptoKeyPairReplace"),
        ("DLINKSW-SSH-MIB", "dSshCryptoKeyPairLastCreateTime"),
        ("DLINKSW-SSH-MIB", "dSshCryptoKeyPairRowStatus"),
        ("DLINKSW-SSH-MIB", "dSshCryptoKeyPairString"),
        ("DLINKSW-SSH-MIB", "dSshCryptoKeyGenerationStatus"))
)
if mibBuilder.loadTexts:
    dSshConfigGroup.setStatus("current")

dSshConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 2, 2, 2)
)
dSshConnectionGroup.setObjects(
      *(("DLINKSW-SSH-MIB", "dSshConnectionVersion"),
        ("DLINKSW-SSH-MIB", "dSshConnectionCipher"),
        ("DLINKSW-SSH-MIB", "dSshConnectionUserID"),
        ("DLINKSW-SSH-MIB", "dSshConnectionHostAddrType"),
        ("DLINKSW-SSH-MIB", "dSshConnectionHostAddr"))
)
if mibBuilder.loadTexts:
    dSshConnectionGroup.setStatus("current")

dSshUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 2, 2, 3)
)
dSshUserGroup.setObjects(
      *(("DLINKSW-SSH-MIB", "dSshUserAuthMethod"),
        ("DLINKSW-SSH-MIB", "dSshUserKeyFilename"),
        ("DLINKSW-SSH-MIB", "dSshUserHostName"),
        ("DLINKSW-SSH-MIB", "dSshUserHostAddrType"),
        ("DLINKSW-SSH-MIB", "dSshUserHostAddr"))
)
if mibBuilder.loadTexts:
    dSshUserGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dSshCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 17, 2, 1, 1)
)
dSshCompliance.setObjects(
    ("DLINKSW-SSH-MIB", "dSshConfigGroup")
)
if mibBuilder.loadTexts:
    dSshCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-SSH-MIB",
    **{"dlinkSwSshMIB": dlinkSwSshMIB,
       "dSshNotifications": dSshNotifications,
       "dSshObjects": dSshObjects,
       "dSshGeneral": dSshGeneral,
       "dSshEnabled": dSshEnabled,
       "dSshVersion": dSshVersion,
       "dSshTimeout": dSshTimeout,
       "dSshAuthenticationRetries": dSshAuthenticationRetries,
       "dSshServicePort": dSshServicePort,
       "dSshSrcIfIndex": dSshSrcIfIndex,
       "dSshKeyConfiguration": dSshKeyConfiguration,
       "dSshCryptoKeyPairTable": dSshCryptoKeyPairTable,
       "dSshCryptoKeyPairEntry": dSshCryptoKeyPairEntry,
       "dSshCryptoKeyPairIndex": dSshCryptoKeyPairIndex,
       "dSshCryptoKeyPairNBits": dSshCryptoKeyPairNBits,
       "dSshCryptoKeyPairReplace": dSshCryptoKeyPairReplace,
       "dSshCryptoKeyPairLastCreateTime": dSshCryptoKeyPairLastCreateTime,
       "dSshCryptoKeyPairString": dSshCryptoKeyPairString,
       "dSshCryptoKeyPairRowStatus": dSshCryptoKeyPairRowStatus,
       "dSshCryptoKeyGenerationStatus": dSshCryptoKeyGenerationStatus,
       "dSshConnectionTable": dSshConnectionTable,
       "dSshConnectionEntry": dSshConnectionEntry,
       "dSshConnectionSID": dSshConnectionSID,
       "dSshConnectionVersion": dSshConnectionVersion,
       "dSshConnectionCipher": dSshConnectionCipher,
       "dSshConnectionUserID": dSshConnectionUserID,
       "dSshConnectionHostAddrType": dSshConnectionHostAddrType,
       "dSshConnectionHostAddr": dSshConnectionHostAddr,
       "dSshUserTable": dSshUserTable,
       "dSshUserEntry": dSshUserEntry,
       "dSshUserName": dSshUserName,
       "dSshUserAuthMethod": dSshUserAuthMethod,
       "dSshUserKeyFilename": dSshUserKeyFilename,
       "dSshUserHostName": dSshUserHostName,
       "dSshUserHostAddrType": dSshUserHostAddrType,
       "dSshUserHostAddr": dSshUserHostAddr,
       "dSshUserRowStatus": dSshUserRowStatus,
       "dSshConformance": dSshConformance,
       "dSshCompliances": dSshCompliances,
       "dSshCompliance": dSshCompliance,
       "dSshGroups": dSshGroups,
       "dSshConfigGroup": dSshConfigGroup,
       "dSshConnectionGroup": dSshConnectionGroup,
       "dSshUserGroup": dSshUserGroup}
)
