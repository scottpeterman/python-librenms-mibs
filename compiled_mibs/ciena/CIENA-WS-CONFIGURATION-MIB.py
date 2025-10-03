# SNMP MIB module (CIENA-WS-CONFIGURATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-CONFIGURATION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:04 2025
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

(EnabledDisabledEnum,
 StringMaxl128,
 StringMaxl254) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "EnabledDisabledEnum",
    "StringMaxl128",
    "StringMaxl254")

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

cienaWsConfigurationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19)
)
if mibBuilder.loadTexts:
    cienaWsConfigurationMIB.setRevisions(
        ("2017-04-05 00:00",
         "2017-03-02 00:00",
         "2016-12-12 00:00",
         "2016-06-15 00:00",
         "2015-09-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ZtpError(TextualConvention, Integer32):
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("none", 1),
          ("bootFileDownloadFailed", 2),
          ("bootFileParseError", 3),
          ("ftpConfigError", 4),
          ("ftpLicenseFileError", 5),
          ("ftpSoftwareLoadFileError", 6),
          ("sshKeyError", 7),
          ("licenseIdError", 8),
          ("licenseDownloadError", 9),
          ("licenseInstallError", 10),
          ("licenseHostIdMismatchError", 11),
          ("licenseWarmRebootRequired", 12),
          ("licenseUnsupportedFileType", 13),
          ("expiredLicenseFile", 14),
          ("systemTimeNotSet", 15),
          ("loginBannerError", 16),
          ("welcomeBannerError", 17),
          ("configFileDownloadFailed", 18),
          ("configFileApplyFailed", 19),
          ("softwareUpgradeFailed", 20),
          ("softwareServerSetFailed", 21),
          ("softwareDownloadFailed", 22),
          ("softwareRepositoryRemountFailed", 23),
          ("softwareUnzipFailed", 24),
          ("softwareAlreadyRunning", 25),
          ("scriptFileDownloadFailed", 26),
          ("scriptFileApplyFailed", 27))
    )



class ZtpOperationalState(TextualConvention, Integer32):
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("idle", 1),
          ("start", 2),
          ("restarting", 3),
          ("waitingForDhcpLease", 4),
          ("downloadingBootFile", 5),
          ("parsingBootFile", 6),
          ("processingBootFile", 7),
          ("processingFtpConfigFile", 8),
          ("processingFtpLicenseFile", 9),
          ("processingFtpSoftwareLoadFile", 10),
          ("processingSshKeys", 11),
          ("processingLicenseId", 12),
          ("installingLicenses", 13),
          ("downloadingLoginBanner", 14),
          ("downloadingWelcomeBanner", 15),
          ("downloadingConfigFile", 16),
          ("applyingConfigFile", 17),
          ("processingConfigFile", 18),
          ("processingSoftwarePackage", 19),
          ("requestingReboot", 20),
          ("upgradingSoftware", 21),
          ("booting", 22),
          ("completed", 23),
          ("failed", 24),
          ("downloadingScriptFile", 25),
          ("downloadingLicenses", 26))
    )



# MIB Managed Objects in the order of their OIDs

_CienaWsConfigurationObjects_ObjectIdentity = ObjectIdentity
cienaWsConfigurationObjects = _CienaWsConfigurationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 1)
)
_CienaWsConfigurationConformance_ObjectIdentity = ObjectIdentity
cienaWsConfigurationConformance = _CienaWsConfigurationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 2)
)
_CienaWsConfigurationGroups_ObjectIdentity = ObjectIdentity
cienaWsConfigurationGroups = _CienaWsConfigurationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 2, 1)
)
_CienaWsConfigurationCompliances_ObjectIdentity = ObjectIdentity
cienaWsConfigurationCompliances = _CienaWsConfigurationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 2, 2)
)
_CwsConfigurationFileListTable_Object = MibTable
cwsConfigurationFileListTable = _CwsConfigurationFileListTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 3)
)
if mibBuilder.loadTexts:
    cwsConfigurationFileListTable.setStatus("current")
_CwsConfigurationFileListEntry_Object = MibTableRow
cwsConfigurationFileListEntry = _CwsConfigurationFileListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 3, 1)
)
cwsConfigurationFileListEntry.setIndexNames(
    (0, "CIENA-WS-CONFIGURATION-MIB", "cwsConfigurationConfigurationFilesTableSnmpKey"),
    (0, "CIENA-WS-CONFIGURATION-MIB", "cwsConfigurationFileListTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsConfigurationFileListEntry.setStatus("current")


class _CwsConfigurationFileListTableSnmpKey_Type(Integer32):
    """Custom type cwsConfigurationFileListTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsConfigurationFileListTableSnmpKey_Type.__name__ = "Integer32"
_CwsConfigurationFileListTableSnmpKey_Object = MibTableColumn
cwsConfigurationFileListTableSnmpKey = _CwsConfigurationFileListTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 3, 1, 1),
    _CwsConfigurationFileListTableSnmpKey_Type()
)
cwsConfigurationFileListTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsConfigurationFileListTableSnmpKey.setStatus("current")
_CwsConfigurationFileList_Type = StringMaxl254
_CwsConfigurationFileList_Object = MibTableColumn
cwsConfigurationFileList = _CwsConfigurationFileList_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 3, 1, 2),
    _CwsConfigurationFileList_Type()
)
cwsConfigurationFileList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsConfigurationFileList.setStatus("current")
_CwsConfigurationConfigurationFilesTable_Object = MibTable
cwsConfigurationConfigurationFilesTable = _CwsConfigurationConfigurationFilesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 4)
)
if mibBuilder.loadTexts:
    cwsConfigurationConfigurationFilesTable.setStatus("current")
_CwsConfigurationConfigurationFilesEntry_Object = MibTableRow
cwsConfigurationConfigurationFilesEntry = _CwsConfigurationConfigurationFilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 4, 1)
)
cwsConfigurationConfigurationFilesEntry.setIndexNames(
    (0, "CIENA-WS-CONFIGURATION-MIB", "cwsConfigurationConfigurationFilesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsConfigurationConfigurationFilesEntry.setStatus("current")


class _CwsConfigurationConfigurationFilesTableSnmpKey_Type(Integer32):
    """Custom type cwsConfigurationConfigurationFilesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsConfigurationConfigurationFilesTableSnmpKey_Type.__name__ = "Integer32"
_CwsConfigurationConfigurationFilesTableSnmpKey_Object = MibTableColumn
cwsConfigurationConfigurationFilesTableSnmpKey = _CwsConfigurationConfigurationFilesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 4, 1, 1),
    _CwsConfigurationConfigurationFilesTableSnmpKey_Type()
)
cwsConfigurationConfigurationFilesTableSnmpKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsConfigurationConfigurationFilesTableSnmpKey.setStatus("current")
_CwsConfigurationDefaultFilesTable_Object = MibTable
cwsConfigurationDefaultFilesTable = _CwsConfigurationDefaultFilesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 5)
)
if mibBuilder.loadTexts:
    cwsConfigurationDefaultFilesTable.setStatus("current")
_CwsConfigurationDefaultFilesEntry_Object = MibTableRow
cwsConfigurationDefaultFilesEntry = _CwsConfigurationDefaultFilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 5, 1)
)
cwsConfigurationDefaultFilesEntry.setIndexNames(
    (0, "CIENA-WS-CONFIGURATION-MIB", "cwsConfigurationDefaultFilesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsConfigurationDefaultFilesEntry.setStatus("current")


class _CwsConfigurationDefaultFilesTableSnmpKey_Type(Integer32):
    """Custom type cwsConfigurationDefaultFilesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsConfigurationDefaultFilesTableSnmpKey_Type.__name__ = "Integer32"
_CwsConfigurationDefaultFilesTableSnmpKey_Object = MibTableColumn
cwsConfigurationDefaultFilesTableSnmpKey = _CwsConfigurationDefaultFilesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 5, 1, 1),
    _CwsConfigurationDefaultFilesTableSnmpKey_Type()
)
cwsConfigurationDefaultFilesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsConfigurationDefaultFilesTableSnmpKey.setStatus("current")
_CwsConfigurationDefaultFilesSaveFilename_Type = StringMaxl254
_CwsConfigurationDefaultFilesSaveFilename_Object = MibTableColumn
cwsConfigurationDefaultFilesSaveFilename = _CwsConfigurationDefaultFilesSaveFilename_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 5, 1, 2),
    _CwsConfigurationDefaultFilesSaveFilename_Type()
)
cwsConfigurationDefaultFilesSaveFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsConfigurationDefaultFilesSaveFilename.setStatus("current")
_CwsConfigurationDefaultFilesLoadFilename_Type = StringMaxl254
_CwsConfigurationDefaultFilesLoadFilename_Object = MibTableColumn
cwsConfigurationDefaultFilesLoadFilename = _CwsConfigurationDefaultFilesLoadFilename_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 5, 1, 3),
    _CwsConfigurationDefaultFilesLoadFilename_Type()
)
cwsConfigurationDefaultFilesLoadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsConfigurationDefaultFilesLoadFilename.setStatus("current")
_CwsConfigurationDefaultFilesBackupLoadFilename_Type = StringMaxl254
_CwsConfigurationDefaultFilesBackupLoadFilename_Object = MibTableColumn
cwsConfigurationDefaultFilesBackupLoadFilename = _CwsConfigurationDefaultFilesBackupLoadFilename_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 5, 1, 4),
    _CwsConfigurationDefaultFilesBackupLoadFilename_Type()
)
cwsConfigurationDefaultFilesBackupLoadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsConfigurationDefaultFilesBackupLoadFilename.setStatus("current")
_CwsConfigurationZtpStateTable_Object = MibTable
cwsConfigurationZtpStateTable = _CwsConfigurationZtpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 7)
)
if mibBuilder.loadTexts:
    cwsConfigurationZtpStateTable.setStatus("current")
_CwsConfigurationZtpStateEntry_Object = MibTableRow
cwsConfigurationZtpStateEntry = _CwsConfigurationZtpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 7, 1)
)
cwsConfigurationZtpStateEntry.setIndexNames(
    (0, "CIENA-WS-CONFIGURATION-MIB", "cwsConfigurationZtpStateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsConfigurationZtpStateEntry.setStatus("current")


class _CwsConfigurationZtpStateTableSnmpKey_Type(Integer32):
    """Custom type cwsConfigurationZtpStateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsConfigurationZtpStateTableSnmpKey_Type.__name__ = "Integer32"
_CwsConfigurationZtpStateTableSnmpKey_Object = MibTableColumn
cwsConfigurationZtpStateTableSnmpKey = _CwsConfigurationZtpStateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 7, 1, 1),
    _CwsConfigurationZtpStateTableSnmpKey_Type()
)
cwsConfigurationZtpStateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsConfigurationZtpStateTableSnmpKey.setStatus("current")
_CwsConfigurationZtpStateAdminState_Type = EnabledDisabledEnum
_CwsConfigurationZtpStateAdminState_Object = MibTableColumn
cwsConfigurationZtpStateAdminState = _CwsConfigurationZtpStateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 7, 1, 2),
    _CwsConfigurationZtpStateAdminState_Type()
)
cwsConfigurationZtpStateAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsConfigurationZtpStateAdminState.setStatus("current")
_CwsConfigurationZtpStateOperationalState_Type = ZtpOperationalState
_CwsConfigurationZtpStateOperationalState_Object = MibTableColumn
cwsConfigurationZtpStateOperationalState = _CwsConfigurationZtpStateOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 7, 1, 3),
    _CwsConfigurationZtpStateOperationalState_Type()
)
cwsConfigurationZtpStateOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsConfigurationZtpStateOperationalState.setStatus("current")
_CwsConfigurationZtpStateLastFailure_Type = ZtpError
_CwsConfigurationZtpStateLastFailure_Object = MibTableColumn
cwsConfigurationZtpStateLastFailure = _CwsConfigurationZtpStateLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 7, 1, 4),
    _CwsConfigurationZtpStateLastFailure_Type()
)
cwsConfigurationZtpStateLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsConfigurationZtpStateLastFailure.setStatus("current")
_CwsConfigurationZtpStateLastCommandFile_Type = StringMaxl128
_CwsConfigurationZtpStateLastCommandFile_Object = MibTableColumn
cwsConfigurationZtpStateLastCommandFile = _CwsConfigurationZtpStateLastCommandFile_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 7, 1, 5),
    _CwsConfigurationZtpStateLastCommandFile_Type()
)
cwsConfigurationZtpStateLastCommandFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsConfigurationZtpStateLastCommandFile.setStatus("current")
_CwsConfigurationZtpStateLastConfigFile_Type = StringMaxl128
_CwsConfigurationZtpStateLastConfigFile_Object = MibTableColumn
cwsConfigurationZtpStateLastConfigFile = _CwsConfigurationZtpStateLastConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 7, 1, 6),
    _CwsConfigurationZtpStateLastConfigFile_Type()
)
cwsConfigurationZtpStateLastConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsConfigurationZtpStateLastConfigFile.setStatus("current")

# Managed Objects groups

cienaWsConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 2, 1, 1)
)
cienaWsConfigurationGroup.setObjects(
      *(("CIENA-WS-CONFIGURATION-MIB", "cwsConfigurationDefaultFilesSaveFilename"),
        ("CIENA-WS-CONFIGURATION-MIB", "cwsConfigurationDefaultFilesLoadFilename"),
        ("CIENA-WS-CONFIGURATION-MIB", "cwsConfigurationDefaultFilesBackupLoadFilename"),
        ("CIENA-WS-CONFIGURATION-MIB", "cwsConfigurationZtpStateAdminState"),
        ("CIENA-WS-CONFIGURATION-MIB", "cwsConfigurationZtpStateOperationalState"),
        ("CIENA-WS-CONFIGURATION-MIB", "cwsConfigurationZtpStateLastFailure"),
        ("CIENA-WS-CONFIGURATION-MIB", "cwsConfigurationZtpStateLastCommandFile"),
        ("CIENA-WS-CONFIGURATION-MIB", "cwsConfigurationZtpStateLastConfigFile"))
)
if mibBuilder.loadTexts:
    cienaWsConfigurationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsConfigurationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 19, 2, 2, 1)
)
cienaWsConfigurationCompliance.setObjects(
    ("CIENA-WS-CONFIGURATION-MIB", "cienaWsConfigurationGroup")
)
if mibBuilder.loadTexts:
    cienaWsConfigurationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-CONFIGURATION-MIB",
    **{"ZtpError": ZtpError,
       "ZtpOperationalState": ZtpOperationalState,
       "cienaWsConfigurationMIB": cienaWsConfigurationMIB,
       "cienaWsConfigurationObjects": cienaWsConfigurationObjects,
       "cienaWsConfigurationConformance": cienaWsConfigurationConformance,
       "cienaWsConfigurationGroups": cienaWsConfigurationGroups,
       "cienaWsConfigurationGroup": cienaWsConfigurationGroup,
       "cienaWsConfigurationCompliances": cienaWsConfigurationCompliances,
       "cienaWsConfigurationCompliance": cienaWsConfigurationCompliance,
       "cwsConfigurationFileListTable": cwsConfigurationFileListTable,
       "cwsConfigurationFileListEntry": cwsConfigurationFileListEntry,
       "cwsConfigurationFileListTableSnmpKey": cwsConfigurationFileListTableSnmpKey,
       "cwsConfigurationFileList": cwsConfigurationFileList,
       "cwsConfigurationConfigurationFilesTable": cwsConfigurationConfigurationFilesTable,
       "cwsConfigurationConfigurationFilesEntry": cwsConfigurationConfigurationFilesEntry,
       "cwsConfigurationConfigurationFilesTableSnmpKey": cwsConfigurationConfigurationFilesTableSnmpKey,
       "cwsConfigurationDefaultFilesTable": cwsConfigurationDefaultFilesTable,
       "cwsConfigurationDefaultFilesEntry": cwsConfigurationDefaultFilesEntry,
       "cwsConfigurationDefaultFilesTableSnmpKey": cwsConfigurationDefaultFilesTableSnmpKey,
       "cwsConfigurationDefaultFilesSaveFilename": cwsConfigurationDefaultFilesSaveFilename,
       "cwsConfigurationDefaultFilesLoadFilename": cwsConfigurationDefaultFilesLoadFilename,
       "cwsConfigurationDefaultFilesBackupLoadFilename": cwsConfigurationDefaultFilesBackupLoadFilename,
       "cwsConfigurationZtpStateTable": cwsConfigurationZtpStateTable,
       "cwsConfigurationZtpStateEntry": cwsConfigurationZtpStateEntry,
       "cwsConfigurationZtpStateTableSnmpKey": cwsConfigurationZtpStateTableSnmpKey,
       "cwsConfigurationZtpStateAdminState": cwsConfigurationZtpStateAdminState,
       "cwsConfigurationZtpStateOperationalState": cwsConfigurationZtpStateOperationalState,
       "cwsConfigurationZtpStateLastFailure": cwsConfigurationZtpStateLastFailure,
       "cwsConfigurationZtpStateLastCommandFile": cwsConfigurationZtpStateLastCommandFile,
       "cwsConfigurationZtpStateLastConfigFile": cwsConfigurationZtpStateLastConfigFile}
)
