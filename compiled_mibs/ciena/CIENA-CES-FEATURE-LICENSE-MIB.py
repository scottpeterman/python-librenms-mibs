# SNMP MIB module (CIENA-CES-FEATURE-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-FEATURE-LICENSE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:35 2025
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

(cienaCesModuleChassisIndx,
 cienaCesModuleShelfIndx,
 cienaCesModuleSlotIndx) = mibBuilder.importSymbols(
    "CIENA-CES-MODULE-MIB",
    "cienaCesModuleChassisIndx",
    "cienaCesModuleShelfIndx",
    "cienaCesModuleSlotIndx")

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaCesFeatureLicenseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11)
)
if mibBuilder.loadTexts:
    cienaCesFeatureLicenseMIB.setRevisions(
        ("2017-06-07 00:00",
         "2013-11-04 00:00",
         "2011-02-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesFeatureLicenseMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesFeatureLicenseMIBObjects = _CienaCesFeatureLicenseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1)
)
_CienaCesPremiumFeatureLicense_ObjectIdentity = ObjectIdentity
cienaCesPremiumFeatureLicense = _CienaCesPremiumFeatureLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1)
)
_CienaCesPremiumFeatureStatusTable_Object = MibTable
cienaCesPremiumFeatureStatusTable = _CienaCesPremiumFeatureStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureStatusTable.setStatus("current")
_CienaCesPremiumFeatureStatusEntry_Object = MibTableRow
cienaCesPremiumFeatureStatusEntry = _CienaCesPremiumFeatureStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 1, 1)
)
cienaCesPremiumFeatureStatusEntry.setIndexNames(
    (0, "CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureId"),
)
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureStatusEntry.setStatus("current")
_CienaCesPremiumFeatureId_Type = Integer32
_CienaCesPremiumFeatureId_Object = MibTableColumn
cienaCesPremiumFeatureId = _CienaCesPremiumFeatureId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 1, 1, 1),
    _CienaCesPremiumFeatureId_Type()
)
cienaCesPremiumFeatureId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureId.setStatus("current")
_CienaCesPremiumFeatureName_Type = DisplayString
_CienaCesPremiumFeatureName_Object = MibTableColumn
cienaCesPremiumFeatureName = _CienaCesPremiumFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 1, 1, 2),
    _CienaCesPremiumFeatureName_Type()
)
cienaCesPremiumFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureName.setStatus("current")


class _CienaCesPremiumFeatureOperStatus_Type(Integer32):
    """Custom type cienaCesPremiumFeatureOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("disabled", 1),
          ("restrictedUse", 2),
          ("fullyActive", 3),
          ("someLicenseKeyMissing", 4),
          ("licenseViolation", 5))
    )


_CienaCesPremiumFeatureOperStatus_Type.__name__ = "Integer32"
_CienaCesPremiumFeatureOperStatus_Object = MibTableColumn
cienaCesPremiumFeatureOperStatus = _CienaCesPremiumFeatureOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 1, 1, 3),
    _CienaCesPremiumFeatureOperStatus_Type()
)
cienaCesPremiumFeatureOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureOperStatus.setStatus("current")
_CienaCesPremiumFeatureLicenseStatusTable_Object = MibTable
cienaCesPremiumFeatureLicenseStatusTable = _CienaCesPremiumFeatureLicenseStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseStatusTable.setStatus("current")
_CienaCesPremiumFeatureLicenseStatusEntry_Object = MibTableRow
cienaCesPremiumFeatureLicenseStatusEntry = _CienaCesPremiumFeatureLicenseStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 2, 1)
)
cienaCesPremiumFeatureLicenseStatusEntry.setIndexNames(
    (0, "CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicenseIndex"),
)
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseStatusEntry.setStatus("current")
_CienaCesPremiumFeatureLicenseIndex_Type = Unsigned32
_CienaCesPremiumFeatureLicenseIndex_Object = MibTableColumn
cienaCesPremiumFeatureLicenseIndex = _CienaCesPremiumFeatureLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 2, 1, 1),
    _CienaCesPremiumFeatureLicenseIndex_Type()
)
cienaCesPremiumFeatureLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseIndex.setStatus("current")
_CienaCesPremiumFeatureLicenseName_Type = DisplayString
_CienaCesPremiumFeatureLicenseName_Object = MibTableColumn
cienaCesPremiumFeatureLicenseName = _CienaCesPremiumFeatureLicenseName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 2, 1, 2),
    _CienaCesPremiumFeatureLicenseName_Type()
)
cienaCesPremiumFeatureLicenseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseName.setStatus("current")
_CienaCesPremiumFeatureLicenseDomainName_Type = DisplayString
_CienaCesPremiumFeatureLicenseDomainName_Object = MibTableColumn
cienaCesPremiumFeatureLicenseDomainName = _CienaCesPremiumFeatureLicenseDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 2, 1, 3),
    _CienaCesPremiumFeatureLicenseDomainName_Type()
)
cienaCesPremiumFeatureLicenseDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseDomainName.setStatus("current")


class _CienaCesPremiumFeatureLicenseOperStatus_Type(Integer32):
    """Custom type cienaCesPremiumFeatureLicenseOperStatus based on Integer32"""
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
        *(("infoNotAvailable", 1),
          ("notInstalled", 2),
          ("installed", 3),
          ("partial", 4),
          ("noBaseLic", 5))
    )


_CienaCesPremiumFeatureLicenseOperStatus_Type.__name__ = "Integer32"
_CienaCesPremiumFeatureLicenseOperStatus_Object = MibTableColumn
cienaCesPremiumFeatureLicenseOperStatus = _CienaCesPremiumFeatureLicenseOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 2, 1, 4),
    _CienaCesPremiumFeatureLicenseOperStatus_Type()
)
cienaCesPremiumFeatureLicenseOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseOperStatus.setStatus("current")
_CienaCesPremiumFeatureLicenseSystemTable_Object = MibTable
cienaCesPremiumFeatureLicenseSystemTable = _CienaCesPremiumFeatureLicenseSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseSystemTable.setStatus("current")
_CienaCesPremiumFeatureLicenseSystemEntry_Object = MibTableRow
cienaCesPremiumFeatureLicenseSystemEntry = _CienaCesPremiumFeatureLicenseSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 3, 1)
)
cienaCesPremiumFeatureLicenseSystemEntry.setIndexNames(
    (0, "CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicenseSystemIndex"),
)
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseSystemEntry.setStatus("current")
_CienaCesPremiumFeatureLicenseSystemIndex_Type = Unsigned32
_CienaCesPremiumFeatureLicenseSystemIndex_Object = MibTableColumn
cienaCesPremiumFeatureLicenseSystemIndex = _CienaCesPremiumFeatureLicenseSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 3, 1, 1),
    _CienaCesPremiumFeatureLicenseSystemIndex_Type()
)
cienaCesPremiumFeatureLicenseSystemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseSystemIndex.setStatus("current")
_CienaCesPremiumFeatureLicenseSystemLicenseName_Type = DisplayString
_CienaCesPremiumFeatureLicenseSystemLicenseName_Object = MibTableColumn
cienaCesPremiumFeatureLicenseSystemLicenseName = _CienaCesPremiumFeatureLicenseSystemLicenseName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 3, 1, 2),
    _CienaCesPremiumFeatureLicenseSystemLicenseName_Type()
)
cienaCesPremiumFeatureLicenseSystemLicenseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseSystemLicenseName.setStatus("current")
_CienaCesPremiumFeatureLicenseSystemDomainName_Type = DisplayString
_CienaCesPremiumFeatureLicenseSystemDomainName_Object = MibTableColumn
cienaCesPremiumFeatureLicenseSystemDomainName = _CienaCesPremiumFeatureLicenseSystemDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 3, 1, 3),
    _CienaCesPremiumFeatureLicenseSystemDomainName_Type()
)
cienaCesPremiumFeatureLicenseSystemDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseSystemDomainName.setStatus("current")
_CienaCesPremiumFeatureLicenseSystemAdminId_Type = Integer32
_CienaCesPremiumFeatureLicenseSystemAdminId_Object = MibTableColumn
cienaCesPremiumFeatureLicenseSystemAdminId = _CienaCesPremiumFeatureLicenseSystemAdminId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 3, 1, 4),
    _CienaCesPremiumFeatureLicenseSystemAdminId_Type()
)
cienaCesPremiumFeatureLicenseSystemAdminId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseSystemAdminId.setStatus("current")
_CienaCesPremiumFeatureLicenseSystemSequenceNumber_Type = Unsigned32
_CienaCesPremiumFeatureLicenseSystemSequenceNumber_Object = MibTableColumn
cienaCesPremiumFeatureLicenseSystemSequenceNumber = _CienaCesPremiumFeatureLicenseSystemSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 3, 1, 5),
    _CienaCesPremiumFeatureLicenseSystemSequenceNumber_Type()
)
cienaCesPremiumFeatureLicenseSystemSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseSystemSequenceNumber.setStatus("current")
_CienaCesPremiumFeatureLicenseSystemDaysRemaining_Type = Integer32
_CienaCesPremiumFeatureLicenseSystemDaysRemaining_Object = MibTableColumn
cienaCesPremiumFeatureLicenseSystemDaysRemaining = _CienaCesPremiumFeatureLicenseSystemDaysRemaining_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 3, 1, 6),
    _CienaCesPremiumFeatureLicenseSystemDaysRemaining_Type()
)
cienaCesPremiumFeatureLicenseSystemDaysRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseSystemDaysRemaining.setStatus("current")
_CienaCesPremiumFeatureLicenseSystemLicenseKey_Type = DisplayString
_CienaCesPremiumFeatureLicenseSystemLicenseKey_Object = MibTableColumn
cienaCesPremiumFeatureLicenseSystemLicenseKey = _CienaCesPremiumFeatureLicenseSystemLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 3, 1, 7),
    _CienaCesPremiumFeatureLicenseSystemLicenseKey_Type()
)
cienaCesPremiumFeatureLicenseSystemLicenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseSystemLicenseKey.setStatus("current")
_CienaCesPremiumFeatureLicensePoolTable_Object = MibTable
cienaCesPremiumFeatureLicensePoolTable = _CienaCesPremiumFeatureLicensePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicensePoolTable.setStatus("current")
_CienaCesPremiumFeatureLicensePoolEntry_Object = MibTableRow
cienaCesPremiumFeatureLicensePoolEntry = _CienaCesPremiumFeatureLicensePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 4, 1)
)
cienaCesPremiumFeatureLicensePoolEntry.setIndexNames(
    (0, "CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicensePoolIndex"),
)
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicensePoolEntry.setStatus("current")
_CienaCesPremiumFeatureLicensePoolIndex_Type = Integer32
_CienaCesPremiumFeatureLicensePoolIndex_Object = MibTableColumn
cienaCesPremiumFeatureLicensePoolIndex = _CienaCesPremiumFeatureLicensePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 4, 1, 1),
    _CienaCesPremiumFeatureLicensePoolIndex_Type()
)
cienaCesPremiumFeatureLicensePoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicensePoolIndex.setStatus("current")
_CienaCesPremiumFeatureLicensePoolLicenseName_Type = DisplayString
_CienaCesPremiumFeatureLicensePoolLicenseName_Object = MibTableColumn
cienaCesPremiumFeatureLicensePoolLicenseName = _CienaCesPremiumFeatureLicensePoolLicenseName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 4, 1, 2),
    _CienaCesPremiumFeatureLicensePoolLicenseName_Type()
)
cienaCesPremiumFeatureLicensePoolLicenseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicensePoolLicenseName.setStatus("current")
_CienaCesPremiumFeatureLicensePoolDomainName_Type = DisplayString
_CienaCesPremiumFeatureLicensePoolDomainName_Object = MibTableColumn
cienaCesPremiumFeatureLicensePoolDomainName = _CienaCesPremiumFeatureLicensePoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 4, 1, 3),
    _CienaCesPremiumFeatureLicensePoolDomainName_Type()
)
cienaCesPremiumFeatureLicensePoolDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicensePoolDomainName.setStatus("current")
_CienaCesPremiumFeatureLicensePoolAdminId_Type = Integer32
_CienaCesPremiumFeatureLicensePoolAdminId_Object = MibTableColumn
cienaCesPremiumFeatureLicensePoolAdminId = _CienaCesPremiumFeatureLicensePoolAdminId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 4, 1, 4),
    _CienaCesPremiumFeatureLicensePoolAdminId_Type()
)
cienaCesPremiumFeatureLicensePoolAdminId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicensePoolAdminId.setStatus("current")
_CienaCesPremiumFeatureLicensePoolSequenceNumber_Type = Unsigned32
_CienaCesPremiumFeatureLicensePoolSequenceNumber_Object = MibTableColumn
cienaCesPremiumFeatureLicensePoolSequenceNumber = _CienaCesPremiumFeatureLicensePoolSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 4, 1, 5),
    _CienaCesPremiumFeatureLicensePoolSequenceNumber_Type()
)
cienaCesPremiumFeatureLicensePoolSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicensePoolSequenceNumber.setStatus("current")
_CienaCesPremiumFeatureLicensePoolDaysRemaining_Type = Integer32
_CienaCesPremiumFeatureLicensePoolDaysRemaining_Object = MibTableColumn
cienaCesPremiumFeatureLicensePoolDaysRemaining = _CienaCesPremiumFeatureLicensePoolDaysRemaining_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 4, 1, 6),
    _CienaCesPremiumFeatureLicensePoolDaysRemaining_Type()
)
cienaCesPremiumFeatureLicensePoolDaysRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicensePoolDaysRemaining.setStatus("current")
_CienaCesPremiumFeatureLicensePoolLicenseKey_Type = DisplayString
_CienaCesPremiumFeatureLicensePoolLicenseKey_Object = MibTableColumn
cienaCesPremiumFeatureLicensePoolLicenseKey = _CienaCesPremiumFeatureLicensePoolLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 1, 4, 1, 7),
    _CienaCesPremiumFeatureLicensePoolLicenseKey_Type()
)
cienaCesPremiumFeatureLicensePoolLicenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicensePoolLicenseKey.setStatus("current")
_CienaCesPremiumFeatureLicenseNotifAttrs_ObjectIdentity = ObjectIdentity
cienaCesPremiumFeatureLicenseNotifAttrs = _CienaCesPremiumFeatureLicenseNotifAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 2)
)
_CienaCesPremiumFeatureLicenseInstallUnsuccessfulReason_Type = DisplayString
_CienaCesPremiumFeatureLicenseInstallUnsuccessfulReason_Object = MibScalar
cienaCesPremiumFeatureLicenseInstallUnsuccessfulReason = _CienaCesPremiumFeatureLicenseInstallUnsuccessfulReason_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 1, 2, 1),
    _CienaCesPremiumFeatureLicenseInstallUnsuccessfulReason_Type()
)
cienaCesPremiumFeatureLicenseInstallUnsuccessfulReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseInstallUnsuccessfulReason.setStatus("current")
_CienaCesFeatureLicenseMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesFeatureLicenseMIBConformance = _CienaCesFeatureLicenseMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 3)
)
_CienaCesFeatureLicenseMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesFeatureLicenseMIBCompliances = _CienaCesFeatureLicenseMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 3, 1)
)
_CienaCesFeatureLicenseMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesFeatureLicenseMIBGroups = _CienaCesFeatureLicenseMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 11, 3, 2)
)
_CienaCesFeatureLicenseMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesFeatureLicenseMIBNotificationPrefix = _CienaCesFeatureLicenseMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 11)
)
_CienaCesFeatureLicenseMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesFeatureLicenseMIBNotifications = _CienaCesFeatureLicenseMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 11, 0)
)

# Managed Objects groups


# Notification objects

cienaCesPremiumFeatureLicenseNotInstalledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 11, 0, 1)
)
cienaCesPremiumFeatureLicenseNotInstalledNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicenseName"),
        ("CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicenseOperStatus"),
        ("CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicenseDomainName"))
)
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseNotInstalledNotification.setStatus(
        "current"
    )

cienaCesPremiumFeatureLicensePartialStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 11, 0, 2)
)
cienaCesPremiumFeatureLicensePartialStatusNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicenseName"),
        ("CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicenseOperStatus"),
        ("CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicenseDomainName"))
)
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicensePartialStatusNotification.setStatus(
        "current"
    )

cienaCesPremiumFeatureLicenseInstallErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 11, 0, 3)
)
cienaCesPremiumFeatureLicenseInstallErrorNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleChassisIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleShelfIndx"),
        ("CIENA-CES-MODULE-MIB", "cienaCesModuleSlotIndx"),
        ("CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicenseInstallUnsuccessfulReason"))
)
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseInstallErrorNotification.setStatus(
        "current"
    )

cienaCesPremiumFeatureLicenseInstalledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 11, 0, 4)
)
cienaCesPremiumFeatureLicenseInstalledNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicenseName"),
        ("CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicenseOperStatus"),
        ("CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicenseDomainName"))
)
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseInstalledNotification.setStatus(
        "current"
    )

cienaCesPremiumFeatureLicenseUsageViolationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 11, 0, 5)
)
cienaCesPremiumFeatureLicenseUsageViolationNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicenseName"),
        ("CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicenseOperStatus"),
        ("CIENA-CES-FEATURE-LICENSE-MIB", "cienaCesPremiumFeatureLicenseDomainName"))
)
if mibBuilder.loadTexts:
    cienaCesPremiumFeatureLicenseUsageViolationNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-FEATURE-LICENSE-MIB",
    **{"cienaCesFeatureLicenseMIB": cienaCesFeatureLicenseMIB,
       "cienaCesFeatureLicenseMIBObjects": cienaCesFeatureLicenseMIBObjects,
       "cienaCesPremiumFeatureLicense": cienaCesPremiumFeatureLicense,
       "cienaCesPremiumFeatureStatusTable": cienaCesPremiumFeatureStatusTable,
       "cienaCesPremiumFeatureStatusEntry": cienaCesPremiumFeatureStatusEntry,
       "cienaCesPremiumFeatureId": cienaCesPremiumFeatureId,
       "cienaCesPremiumFeatureName": cienaCesPremiumFeatureName,
       "cienaCesPremiumFeatureOperStatus": cienaCesPremiumFeatureOperStatus,
       "cienaCesPremiumFeatureLicenseStatusTable": cienaCesPremiumFeatureLicenseStatusTable,
       "cienaCesPremiumFeatureLicenseStatusEntry": cienaCesPremiumFeatureLicenseStatusEntry,
       "cienaCesPremiumFeatureLicenseIndex": cienaCesPremiumFeatureLicenseIndex,
       "cienaCesPremiumFeatureLicenseName": cienaCesPremiumFeatureLicenseName,
       "cienaCesPremiumFeatureLicenseDomainName": cienaCesPremiumFeatureLicenseDomainName,
       "cienaCesPremiumFeatureLicenseOperStatus": cienaCesPremiumFeatureLicenseOperStatus,
       "cienaCesPremiumFeatureLicenseSystemTable": cienaCesPremiumFeatureLicenseSystemTable,
       "cienaCesPremiumFeatureLicenseSystemEntry": cienaCesPremiumFeatureLicenseSystemEntry,
       "cienaCesPremiumFeatureLicenseSystemIndex": cienaCesPremiumFeatureLicenseSystemIndex,
       "cienaCesPremiumFeatureLicenseSystemLicenseName": cienaCesPremiumFeatureLicenseSystemLicenseName,
       "cienaCesPremiumFeatureLicenseSystemDomainName": cienaCesPremiumFeatureLicenseSystemDomainName,
       "cienaCesPremiumFeatureLicenseSystemAdminId": cienaCesPremiumFeatureLicenseSystemAdminId,
       "cienaCesPremiumFeatureLicenseSystemSequenceNumber": cienaCesPremiumFeatureLicenseSystemSequenceNumber,
       "cienaCesPremiumFeatureLicenseSystemDaysRemaining": cienaCesPremiumFeatureLicenseSystemDaysRemaining,
       "cienaCesPremiumFeatureLicenseSystemLicenseKey": cienaCesPremiumFeatureLicenseSystemLicenseKey,
       "cienaCesPremiumFeatureLicensePoolTable": cienaCesPremiumFeatureLicensePoolTable,
       "cienaCesPremiumFeatureLicensePoolEntry": cienaCesPremiumFeatureLicensePoolEntry,
       "cienaCesPremiumFeatureLicensePoolIndex": cienaCesPremiumFeatureLicensePoolIndex,
       "cienaCesPremiumFeatureLicensePoolLicenseName": cienaCesPremiumFeatureLicensePoolLicenseName,
       "cienaCesPremiumFeatureLicensePoolDomainName": cienaCesPremiumFeatureLicensePoolDomainName,
       "cienaCesPremiumFeatureLicensePoolAdminId": cienaCesPremiumFeatureLicensePoolAdminId,
       "cienaCesPremiumFeatureLicensePoolSequenceNumber": cienaCesPremiumFeatureLicensePoolSequenceNumber,
       "cienaCesPremiumFeatureLicensePoolDaysRemaining": cienaCesPremiumFeatureLicensePoolDaysRemaining,
       "cienaCesPremiumFeatureLicensePoolLicenseKey": cienaCesPremiumFeatureLicensePoolLicenseKey,
       "cienaCesPremiumFeatureLicenseNotifAttrs": cienaCesPremiumFeatureLicenseNotifAttrs,
       "cienaCesPremiumFeatureLicenseInstallUnsuccessfulReason": cienaCesPremiumFeatureLicenseInstallUnsuccessfulReason,
       "cienaCesFeatureLicenseMIBConformance": cienaCesFeatureLicenseMIBConformance,
       "cienaCesFeatureLicenseMIBCompliances": cienaCesFeatureLicenseMIBCompliances,
       "cienaCesFeatureLicenseMIBGroups": cienaCesFeatureLicenseMIBGroups,
       "cienaCesFeatureLicenseMIBNotificationPrefix": cienaCesFeatureLicenseMIBNotificationPrefix,
       "cienaCesFeatureLicenseMIBNotifications": cienaCesFeatureLicenseMIBNotifications,
       "cienaCesPremiumFeatureLicenseNotInstalledNotification": cienaCesPremiumFeatureLicenseNotInstalledNotification,
       "cienaCesPremiumFeatureLicensePartialStatusNotification": cienaCesPremiumFeatureLicensePartialStatusNotification,
       "cienaCesPremiumFeatureLicenseInstallErrorNotification": cienaCesPremiumFeatureLicenseInstallErrorNotification,
       "cienaCesPremiumFeatureLicenseInstalledNotification": cienaCesPremiumFeatureLicenseInstalledNotification,
       "cienaCesPremiumFeatureLicenseUsageViolationNotification": cienaCesPremiumFeatureLicenseUsageViolationNotification}
)
