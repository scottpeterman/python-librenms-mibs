# SNMP MIB module (CIENA-WS-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-LICENSE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:06 2025
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

(StringMaxl128,
 StringMaxl16,
 StringMaxl32,
 StringMaxl64) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "StringMaxl128",
    "StringMaxl16",
    "StringMaxl32",
    "StringMaxl64")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaWsLicenseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25)
)
if mibBuilder.loadTexts:
    cienaWsLicenseMIB.setRevisions(
        ("2017-07-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LicenseComplianceState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notCompliant", 0),
          ("compliant", 1))
    )



class LicenseSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("preInstall", 0),
          ("local", 1))
    )



class LicenseStatus(TextualConvention, Integer32):
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
        *(("valid", 0),
          ("invalid", 1),
          ("expired", 2))
    )



class LicenseType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trial", 0),
          ("served", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CienaWsLicenseObjects_ObjectIdentity = ObjectIdentity
cienaWsLicenseObjects = _CienaWsLicenseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 1)
)
_CienaWsLicenseConformance_ObjectIdentity = ObjectIdentity
cienaWsLicenseConformance = _CienaWsLicenseConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 2)
)
_CienaWsLicenseGroups_ObjectIdentity = ObjectIdentity
cienaWsLicenseGroups = _CienaWsLicenseGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 2, 1)
)
_CienaWsLicenseCompliances_ObjectIdentity = ObjectIdentity
cienaWsLicenseCompliances = _CienaWsLicenseCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 2, 2)
)
_CwsLicenseClientIdTable_Object = MibTable
cwsLicenseClientIdTable = _CwsLicenseClientIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 4)
)
if mibBuilder.loadTexts:
    cwsLicenseClientIdTable.setStatus("current")
_CwsLicenseClientIdEntry_Object = MibTableRow
cwsLicenseClientIdEntry = _CwsLicenseClientIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 4, 1)
)
cwsLicenseClientIdEntry.setIndexNames(
    (0, "CIENA-WS-LICENSE-MIB", "cwsLicenseClientIdTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsLicenseClientIdEntry.setStatus("current")


class _CwsLicenseClientIdTableSnmpKey_Type(Integer32):
    """Custom type cwsLicenseClientIdTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsLicenseClientIdTableSnmpKey_Type.__name__ = "Integer32"
_CwsLicenseClientIdTableSnmpKey_Object = MibTableColumn
cwsLicenseClientIdTableSnmpKey = _CwsLicenseClientIdTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 4, 1, 1),
    _CwsLicenseClientIdTableSnmpKey_Type()
)
cwsLicenseClientIdTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsLicenseClientIdTableSnmpKey.setStatus("current")
_CwsLicenseClientIdRegistrationId_Type = StringMaxl64
_CwsLicenseClientIdRegistrationId_Object = MibTableColumn
cwsLicenseClientIdRegistrationId = _CwsLicenseClientIdRegistrationId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 4, 1, 2),
    _CwsLicenseClientIdRegistrationId_Type()
)
cwsLicenseClientIdRegistrationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseClientIdRegistrationId.setStatus("current")
_CwsLicenseClientStateTable_Object = MibTable
cwsLicenseClientStateTable = _CwsLicenseClientStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 5)
)
if mibBuilder.loadTexts:
    cwsLicenseClientStateTable.setStatus("current")
_CwsLicenseClientStateEntry_Object = MibTableRow
cwsLicenseClientStateEntry = _CwsLicenseClientStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 5, 1)
)
cwsLicenseClientStateEntry.setIndexNames(
    (0, "CIENA-WS-LICENSE-MIB", "cwsLicenseClientStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsLicenseClientStateEntry.setStatus("current")


class _CwsLicenseClientStateTableSnmpKey_Type(Integer32):
    """Custom type cwsLicenseClientStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsLicenseClientStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsLicenseClientStateTableSnmpKey_Object = MibTableColumn
cwsLicenseClientStateTableSnmpKey = _CwsLicenseClientStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 5, 1, 1),
    _CwsLicenseClientStateTableSnmpKey_Type()
)
cwsLicenseClientStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsLicenseClientStateTableSnmpKey.setStatus("current")
_CwsLicenseClientStateComplianceState_Type = LicenseComplianceState
_CwsLicenseClientStateComplianceState_Object = MibTableColumn
cwsLicenseClientStateComplianceState = _CwsLicenseClientStateComplianceState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 5, 1, 2),
    _CwsLicenseClientStateComplianceState_Type()
)
cwsLicenseClientStateComplianceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseClientStateComplianceState.setStatus("current")
_CwsLicenseLicenseslistTable_Object = MibTable
cwsLicenseLicenseslistTable = _CwsLicenseLicenseslistTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7)
)
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistTable.setStatus("current")
_CwsLicenseLicenseslistEntry_Object = MibTableRow
cwsLicenseLicenseslistEntry = _CwsLicenseLicenseslistEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1)
)
cwsLicenseLicenseslistEntry.setIndexNames(
    (0, "CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistLicenseIndex"),
)
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistEntry.setStatus("current")


class _CwsLicenseLicenseslistLicenseIndex_Type(Integer32):
    """Custom type cwsLicenseLicenseslistLicenseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsLicenseLicenseslistLicenseIndex_Type.__name__ = "Integer32"
_CwsLicenseLicenseslistLicenseIndex_Object = MibTableColumn
cwsLicenseLicenseslistLicenseIndex = _CwsLicenseLicenseslistLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 1),
    _CwsLicenseLicenseslistLicenseIndex_Type()
)
cwsLicenseLicenseslistLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistLicenseIndex.setStatus("current")
_CwsLicenseLicenseslistName_Type = StringMaxl128
_CwsLicenseLicenseslistName_Object = MibTableColumn
cwsLicenseLicenseslistName = _CwsLicenseLicenseslistName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 2),
    _CwsLicenseLicenseslistName_Type()
)
cwsLicenseLicenseslistName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistName.setStatus("current")
_CwsLicenseLicenseslistDescription_Type = StringMaxl128
_CwsLicenseLicenseslistDescription_Object = MibTableColumn
cwsLicenseLicenseslistDescription = _CwsLicenseLicenseslistDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 3),
    _CwsLicenseLicenseslistDescription_Type()
)
cwsLicenseLicenseslistDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistDescription.setStatus("current")
_CwsLicenseLicenseslistVersion_Type = StringMaxl16
_CwsLicenseLicenseslistVersion_Object = MibTableColumn
cwsLicenseLicenseslistVersion = _CwsLicenseLicenseslistVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 4),
    _CwsLicenseLicenseslistVersion_Type()
)
cwsLicenseLicenseslistVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistVersion.setStatus("current")
_CwsLicenseLicenseslistStatus_Type = LicenseStatus
_CwsLicenseLicenseslistStatus_Object = MibTableColumn
cwsLicenseLicenseslistStatus = _CwsLicenseLicenseslistStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 5),
    _CwsLicenseLicenseslistStatus_Type()
)
cwsLicenseLicenseslistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistStatus.setStatus("current")
_CwsLicenseLicenseslistSource_Type = LicenseSource
_CwsLicenseLicenseslistSource_Object = MibTableColumn
cwsLicenseLicenseslistSource = _CwsLicenseLicenseslistSource_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 6),
    _CwsLicenseLicenseslistSource_Type()
)
cwsLicenseLicenseslistSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistSource.setStatus("current")
_CwsLicenseLicenseslistIssuerName_Type = StringMaxl128
_CwsLicenseLicenseslistIssuerName_Object = MibTableColumn
cwsLicenseLicenseslistIssuerName = _CwsLicenseLicenseslistIssuerName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 7),
    _CwsLicenseLicenseslistIssuerName_Type()
)
cwsLicenseLicenseslistIssuerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistIssuerName.setStatus("current")
_CwsLicenseLicenseslistIssuedDate_Type = StringMaxl128
_CwsLicenseLicenseslistIssuedDate_Object = MibTableColumn
cwsLicenseLicenseslistIssuedDate = _CwsLicenseLicenseslistIssuedDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 8),
    _CwsLicenseLicenseslistIssuedDate_Type()
)
cwsLicenseLicenseslistIssuedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistIssuedDate.setStatus("current")
_CwsLicenseLicenseslistType_Type = LicenseType
_CwsLicenseLicenseslistType_Object = MibTableColumn
cwsLicenseLicenseslistType = _CwsLicenseLicenseslistType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 9),
    _CwsLicenseLicenseslistType_Type()
)
cwsLicenseLicenseslistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistType.setStatus("current")
_CwsLicenseLicenseslistHostId_Type = StringMaxl128
_CwsLicenseLicenseslistHostId_Object = MibTableColumn
cwsLicenseLicenseslistHostId = _CwsLicenseLicenseslistHostId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 10),
    _CwsLicenseLicenseslistHostId_Type()
)
cwsLicenseLicenseslistHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistHostId.setStatus("current")
_CwsLicenseLicenseslistCount_Type = StringMaxl16
_CwsLicenseLicenseslistCount_Object = MibTableColumn
cwsLicenseLicenseslistCount = _CwsLicenseLicenseslistCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 11),
    _CwsLicenseLicenseslistCount_Type()
)
cwsLicenseLicenseslistCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistCount.setStatus("current")
_CwsLicenseLicenseslistCheckedOutCount_Type = StringMaxl16
_CwsLicenseLicenseslistCheckedOutCount_Object = MibTableColumn
cwsLicenseLicenseslistCheckedOutCount = _CwsLicenseLicenseslistCheckedOutCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 12),
    _CwsLicenseLicenseslistCheckedOutCount_Type()
)
cwsLicenseLicenseslistCheckedOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistCheckedOutCount.setStatus("current")
_CwsLicenseLicenseslistExpiryDate_Type = StringMaxl32
_CwsLicenseLicenseslistExpiryDate_Object = MibTableColumn
cwsLicenseLicenseslistExpiryDate = _CwsLicenseLicenseslistExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 13),
    _CwsLicenseLicenseslistExpiryDate_Type()
)
cwsLicenseLicenseslistExpiryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistExpiryDate.setStatus("current")
_CwsLicenseLicenseslistNotice_Type = StringMaxl128
_CwsLicenseLicenseslistNotice_Object = MibTableColumn
cwsLicenseLicenseslistNotice = _CwsLicenseLicenseslistNotice_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 7, 1, 14),
    _CwsLicenseLicenseslistNotice_Type()
)
cwsLicenseLicenseslistNotice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseLicenseslistNotice.setStatus("current")
_CwsLicenseServerTable_Object = MibTable
cwsLicenseServerTable = _CwsLicenseServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 8)
)
if mibBuilder.loadTexts:
    cwsLicenseServerTable.setStatus("current")
_CwsLicenseServerEntry_Object = MibTableRow
cwsLicenseServerEntry = _CwsLicenseServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 8, 1)
)
cwsLicenseServerEntry.setIndexNames(
    (0, "CIENA-WS-LICENSE-MIB", "cwsLicenseServerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsLicenseServerEntry.setStatus("current")


class _CwsLicenseServerTableSnmpKey_Type(Integer32):
    """Custom type cwsLicenseServerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsLicenseServerTableSnmpKey_Type.__name__ = "Integer32"
_CwsLicenseServerTableSnmpKey_Object = MibTableColumn
cwsLicenseServerTableSnmpKey = _CwsLicenseServerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 8, 1, 1),
    _CwsLicenseServerTableSnmpKey_Type()
)
cwsLicenseServerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsLicenseServerTableSnmpKey.setStatus("current")


class _CwsLicenseServerHostAddress_Type(OctetString):
    """Custom type cwsLicenseServerHostAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CwsLicenseServerHostAddress_Type.__name__ = "OctetString"
_CwsLicenseServerHostAddress_Object = MibTableColumn
cwsLicenseServerHostAddress = _CwsLicenseServerHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 8, 1, 2),
    _CwsLicenseServerHostAddress_Type()
)
cwsLicenseServerHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsLicenseServerHostAddress.setStatus("current")
_CwsLicenseServerNumLicenseServers_Type = Unsigned32
_CwsLicenseServerNumLicenseServers_Object = MibTableColumn
cwsLicenseServerNumLicenseServers = _CwsLicenseServerNumLicenseServers_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 8, 1, 3),
    _CwsLicenseServerNumLicenseServers_Type()
)
cwsLicenseServerNumLicenseServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsLicenseServerNumLicenseServers.setStatus("current")

# Managed Objects groups

cienaWsLicenseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 2, 1, 1)
)
cienaWsLicenseGroup.setObjects(
      *(("CIENA-WS-LICENSE-MIB", "cwsLicenseClientIdRegistrationId"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseClientStateComplianceState"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistName"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistDescription"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistVersion"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistStatus"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistSource"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistIssuerName"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistIssuedDate"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistType"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistHostId"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistCount"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistCheckedOutCount"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistExpiryDate"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseLicenseslistNotice"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseServerHostAddress"),
        ("CIENA-WS-LICENSE-MIB", "cwsLicenseServerNumLicenseServers"))
)
if mibBuilder.loadTexts:
    cienaWsLicenseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsLicenseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 25, 2, 2, 1)
)
cienaWsLicenseCompliance.setObjects(
    ("CIENA-WS-LICENSE-MIB", "cienaWsLicenseGroup")
)
if mibBuilder.loadTexts:
    cienaWsLicenseCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-LICENSE-MIB",
    **{"LicenseComplianceState": LicenseComplianceState,
       "LicenseSource": LicenseSource,
       "LicenseStatus": LicenseStatus,
       "LicenseType": LicenseType,
       "cienaWsLicenseMIB": cienaWsLicenseMIB,
       "cienaWsLicenseObjects": cienaWsLicenseObjects,
       "cienaWsLicenseConformance": cienaWsLicenseConformance,
       "cienaWsLicenseGroups": cienaWsLicenseGroups,
       "cienaWsLicenseGroup": cienaWsLicenseGroup,
       "cienaWsLicenseCompliances": cienaWsLicenseCompliances,
       "cienaWsLicenseCompliance": cienaWsLicenseCompliance,
       "cwsLicenseClientIdTable": cwsLicenseClientIdTable,
       "cwsLicenseClientIdEntry": cwsLicenseClientIdEntry,
       "cwsLicenseClientIdTableSnmpKey": cwsLicenseClientIdTableSnmpKey,
       "cwsLicenseClientIdRegistrationId": cwsLicenseClientIdRegistrationId,
       "cwsLicenseClientStateTable": cwsLicenseClientStateTable,
       "cwsLicenseClientStateEntry": cwsLicenseClientStateEntry,
       "cwsLicenseClientStateTableSnmpKey": cwsLicenseClientStateTableSnmpKey,
       "cwsLicenseClientStateComplianceState": cwsLicenseClientStateComplianceState,
       "cwsLicenseLicenseslistTable": cwsLicenseLicenseslistTable,
       "cwsLicenseLicenseslistEntry": cwsLicenseLicenseslistEntry,
       "cwsLicenseLicenseslistLicenseIndex": cwsLicenseLicenseslistLicenseIndex,
       "cwsLicenseLicenseslistName": cwsLicenseLicenseslistName,
       "cwsLicenseLicenseslistDescription": cwsLicenseLicenseslistDescription,
       "cwsLicenseLicenseslistVersion": cwsLicenseLicenseslistVersion,
       "cwsLicenseLicenseslistStatus": cwsLicenseLicenseslistStatus,
       "cwsLicenseLicenseslistSource": cwsLicenseLicenseslistSource,
       "cwsLicenseLicenseslistIssuerName": cwsLicenseLicenseslistIssuerName,
       "cwsLicenseLicenseslistIssuedDate": cwsLicenseLicenseslistIssuedDate,
       "cwsLicenseLicenseslistType": cwsLicenseLicenseslistType,
       "cwsLicenseLicenseslistHostId": cwsLicenseLicenseslistHostId,
       "cwsLicenseLicenseslistCount": cwsLicenseLicenseslistCount,
       "cwsLicenseLicenseslistCheckedOutCount": cwsLicenseLicenseslistCheckedOutCount,
       "cwsLicenseLicenseslistExpiryDate": cwsLicenseLicenseslistExpiryDate,
       "cwsLicenseLicenseslistNotice": cwsLicenseLicenseslistNotice,
       "cwsLicenseServerTable": cwsLicenseServerTable,
       "cwsLicenseServerEntry": cwsLicenseServerEntry,
       "cwsLicenseServerTableSnmpKey": cwsLicenseServerTableSnmpKey,
       "cwsLicenseServerHostAddress": cwsLicenseServerHostAddress,
       "cwsLicenseServerNumLicenseServers": cwsLicenseServerNumLicenseServers}
)
