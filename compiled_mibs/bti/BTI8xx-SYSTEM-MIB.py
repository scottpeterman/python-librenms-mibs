# SNMP MIB module (BTI8xx-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bti\BTI8xx-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:22:40 2025
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

(mainSystem,) = mibBuilder.importSymbols(
    "BTI8xx-TC-MIB",
    "mainSystem")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

systemConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1)
)
if mibBuilder.loadTexts:
    systemConfig.setRevisions(
        ("2015-11-30 12:00",
         "2015-11-20 12:00",
         "2015-09-07 13:00",
         "2014-10-29 12:00",
         "2014-08-11 12:00",
         "2014-07-15 12:00",
         "2014-06-18 12:00",
         "2013-12-27 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SystemManagement_ObjectIdentity = ObjectIdentity
systemManagement = _SystemManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1)
)
_SystemInfo_ObjectIdentity = ObjectIdentity
systemInfo = _SystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 1)
)


class _SystemName_Type(OctetString):
    """Custom type systemName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SystemName_Type.__name__ = "OctetString"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 1, 1),
    _SystemName_Type()
)
systemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemName.setStatus("current")


class _AutoLogoutTime_Type(Integer32):
    """Custom type autoLogoutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35791),
    )


_AutoLogoutTime_Type.__name__ = "Integer32"
_AutoLogoutTime_Object = MibScalar
autoLogoutTime = _AutoLogoutTime_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 1, 2),
    _AutoLogoutTime_Type()
)
autoLogoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoLogoutTime.setStatus("current")
_SystemUpTime_Type = TimeTicks
_SystemUpTime_Object = MibScalar
systemUpTime = _SystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 1, 3),
    _SystemUpTime_Type()
)
systemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpTime.setStatus("current")


class _SystemHWVersion_Type(OctetString):
    """Custom type systemHWVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SystemHWVersion_Type.__name__ = "OctetString"
_SystemHWVersion_Object = MibScalar
systemHWVersion = _SystemHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 1, 4),
    _SystemHWVersion_Type()
)
systemHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHWVersion.setStatus("current")


class _SystemSWVersion_Type(OctetString):
    """Custom type systemSWVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SystemSWVersion_Type.__name__ = "OctetString"
_SystemSWVersion_Object = MibScalar
systemSWVersion = _SystemSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 1, 5),
    _SystemSWVersion_Type()
)
systemSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSWVersion.setStatus("current")


class _SystemSWDateAndTime_Type(OctetString):
    """Custom type systemSWDateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SystemSWDateAndTime_Type.__name__ = "OctetString"
_SystemSWDateAndTime_Object = MibScalar
systemSWDateAndTime = _SystemSWDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 1, 6),
    _SystemSWDateAndTime_Type()
)
systemSWDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSWDateAndTime.setStatus("current")


class _SystemTemperature_Type(Integer32):
    """Custom type systemTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SystemTemperature_Type.__name__ = "Integer32"
_SystemTemperature_Object = MibScalar
systemTemperature = _SystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 1, 7),
    _SystemTemperature_Type()
)
systemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperature.setStatus("current")


class _SystemProductName_Type(OctetString):
    """Custom type systemProductName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SystemProductName_Type.__name__ = "OctetString"
_SystemProductName_Object = MibScalar
systemProductName = _SystemProductName_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 1, 8),
    _SystemProductName_Type()
)
systemProductName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemProductName.setStatus("current")
_ConfigAndImageMgmt_ObjectIdentity = ObjectIdentity
configAndImageMgmt = _ConfigAndImageMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2)
)
_ServerConfig_ObjectIdentity = ObjectIdentity
serverConfig = _ServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 1)
)
_ServerIpAddr_Type = IpAddress
_ServerIpAddr_Object = MibScalar
serverIpAddr = _ServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 1, 1),
    _ServerIpAddr_Type()
)
serverIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverIpAddr.setStatus("current")


class _FtpUserName_Type(OctetString):
    """Custom type ftpUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FtpUserName_Type.__name__ = "OctetString"
_FtpUserName_Object = MibScalar
ftpUserName = _FtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 1, 2),
    _FtpUserName_Type()
)
ftpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpUserName.setStatus("current")


class _FtpUserPasswd_Type(OctetString):
    """Custom type ftpUserPasswd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FtpUserPasswd_Type.__name__ = "OctetString"
_FtpUserPasswd_Object = MibScalar
ftpUserPasswd = _FtpUserPasswd_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 1, 3),
    _FtpUserPasswd_Type()
)
ftpUserPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpUserPasswd.setStatus("current")


class _ServerInterfaceType_Type(Integer32):
    """Custom type serverInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oob", 0),
          ("inBand", 1))
    )


_ServerInterfaceType_Type.__name__ = "Integer32"
_ServerInterfaceType_Object = MibScalar
serverInterfaceType = _ServerInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 1, 4),
    _ServerInterfaceType_Type()
)
serverInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverInterfaceType.setStatus("current")
_ConfigMgmt_ObjectIdentity = ObjectIdentity
configMgmt = _ConfigMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 2)
)


class _CfgFileName_Type(OctetString):
    """Custom type cfgFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CfgFileName_Type.__name__ = "OctetString"
_CfgFileName_Object = MibScalar
cfgFileName = _CfgFileName_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 2, 1),
    _CfgFileName_Type()
)
cfgFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFileName.setStatus("current")


class _CfgFileControl_Type(Integer32):
    """Custom type cfgFileControl based on Integer32"""
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
        *(("none", 0),
          ("backUpByFtp", 1),
          ("restoreByFtp", 2),
          ("backupByTftp", 3),
          ("restoreByTftp", 4))
    )


_CfgFileControl_Type.__name__ = "Integer32"
_CfgFileControl_Object = MibScalar
cfgFileControl = _CfgFileControl_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 2, 2),
    _CfgFileControl_Type()
)
cfgFileControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFileControl.setStatus("current")


class _CfgFileStatus_Type(Integer32):
    """Custom type cfgFileStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("backupSuccess", 1),
          ("restoreSuccess", 2),
          ("inProgress", 3),
          ("fileNotFound", 4),
          ("connnectionFail", 5),
          ("logInFail", 6),
          ("diskFull", 7),
          ("otherError", 8))
    )


_CfgFileStatus_Type.__name__ = "Integer32"
_CfgFileStatus_Object = MibScalar
cfgFileStatus = _CfgFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 2, 3),
    _CfgFileStatus_Type()
)
cfgFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgFileStatus.setStatus("current")
_ImageMgmt_ObjectIdentity = ObjectIdentity
imageMgmt = _ImageMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 3)
)


class _UpgradeImageSWFileName_Type(OctetString):
    """Custom type upgradeImageSWFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_UpgradeImageSWFileName_Type.__name__ = "OctetString"
_UpgradeImageSWFileName_Object = MibScalar
upgradeImageSWFileName = _UpgradeImageSWFileName_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 3, 1),
    _UpgradeImageSWFileName_Type()
)
upgradeImageSWFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeImageSWFileName.setStatus("current")


class _UpgradeImageSW_Type(Integer32):
    """Custom type upgradeImageSW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("updateImageFile", 1),
          ("upgradeImage", 2))
    )


_UpgradeImageSW_Type.__name__ = "Integer32"
_UpgradeImageSW_Object = MibScalar
upgradeImageSW = _UpgradeImageSW_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 3, 3),
    _UpgradeImageSW_Type()
)
upgradeImageSW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgradeImageSW.setStatus("current")


class _UpgradeImageSWStatus_Type(Integer32):
    """Custom type upgradeImageSWStatus based on Integer32"""
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
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("success", 1),
          ("inProgress", 2),
          ("diskIsFull", 3),
          ("fileSizeError", 4),
          ("fileOpenError", 5),
          ("fileCRCError", 6),
          ("flashEraseError", 7),
          ("flashWriteError", 8),
          ("unknownError", 9),
          ("upgradeDeliveryInProgress", 101),
          ("upgradeDeliveryFailed", 102),
          ("upgradeDeliverySuccess", 103),
          ("upgradeCheckInProgress", 104),
          ("upgradeCheckFailed", 105),
          ("upgradeCheckSuccess", 106),
          ("upgradeLoadInProgress", 107),
          ("upgradeLoadFailed", 108),
          ("upgradeLoadSuccess1stDone", 109),
          ("upgradeInvokeInProgress", 110),
          ("upgradeInvokeFailed", 111),
          ("upgradeInvokeSuccess2ndDone", 112),
          ("upgradeCommitInProgress", 113),
          ("upgradeCommitFailed", 114),
          ("upgradeImagelatestVersion", 115))
    )


_UpgradeImageSWStatus_Type.__name__ = "Integer32"
_UpgradeImageSWStatus_Object = MibScalar
upgradeImageSWStatus = _UpgradeImageSWStatus_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 3, 4),
    _UpgradeImageSWStatus_Type()
)
upgradeImageSWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeImageSWStatus.setStatus("current")


class _UpgradeImageSWDateAndTime_Type(OctetString):
    """Custom type upgradeImageSWDateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UpgradeImageSWDateAndTime_Type.__name__ = "OctetString"
_UpgradeImageSWDateAndTime_Object = MibScalar
upgradeImageSWDateAndTime = _UpgradeImageSWDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 3, 5),
    _UpgradeImageSWDateAndTime_Type()
)
upgradeImageSWDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgradeImageSWDateAndTime.setStatus("current")
_ImageInfoTable_Object = MibTable
imageInfoTable = _ImageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 3, 10)
)
if mibBuilder.loadTexts:
    imageInfoTable.setStatus("current")
_ImageInfoEntry_Object = MibTableRow
imageInfoEntry = _ImageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 3, 10, 1)
)
imageInfoEntry.setIndexNames(
    (0, "BTI8xx-SYSTEM-MIB", "imageInfoIndex"),
)
if mibBuilder.loadTexts:
    imageInfoEntry.setStatus("current")


class _ImageInfoIndex_Type(Integer32):
    """Custom type imageInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ImageInfoIndex_Type.__name__ = "Integer32"
_ImageInfoIndex_Object = MibTableColumn
imageInfoIndex = _ImageInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 3, 10, 1, 1),
    _ImageInfoIndex_Type()
)
imageInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageInfoIndex.setStatus("current")


class _ImageInfoVersion_Type(OctetString):
    """Custom type imageInfoVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ImageInfoVersion_Type.__name__ = "OctetString"
_ImageInfoVersion_Object = MibTableColumn
imageInfoVersion = _ImageInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 3, 10, 1, 2),
    _ImageInfoVersion_Type()
)
imageInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageInfoVersion.setStatus("current")


class _ImageInfoCreated_Type(OctetString):
    """Custom type imageInfoCreated based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ImageInfoCreated_Type.__name__ = "OctetString"
_ImageInfoCreated_Object = MibTableColumn
imageInfoCreated = _ImageInfoCreated_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 3, 10, 1, 3),
    _ImageInfoCreated_Type()
)
imageInfoCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageInfoCreated.setStatus("current")


class _ImageInfoSize_Type(Integer32):
    """Custom type imageInfoSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ImageInfoSize_Type.__name__ = "Integer32"
_ImageInfoSize_Object = MibTableColumn
imageInfoSize = _ImageInfoSize_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 3, 10, 1, 4),
    _ImageInfoSize_Type()
)
imageInfoSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageInfoSize.setStatus("current")


class _ImageInfoCurrent_Type(Integer32):
    """Custom type imageInfoCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("active", 1))
    )


_ImageInfoCurrent_Type.__name__ = "Integer32"
_ImageInfoCurrent_Object = MibTableColumn
imageInfoCurrent = _ImageInfoCurrent_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 2, 3, 10, 1, 5),
    _ImageInfoCurrent_Type()
)
imageInfoCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageInfoCurrent.setStatus("current")
_Miscellaneous_ObjectIdentity = ObjectIdentity
miscellaneous = _Miscellaneous_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3)
)


class _Reboot_Type(Integer32):
    """Custom type reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reboot", 1))
    )


_Reboot_Type.__name__ = "Integer32"
_Reboot_Object = MibScalar
reboot = _Reboot_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3, 1),
    _Reboot_Type()
)
reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reboot.setStatus("current")


class _Save_Type(Integer32):
    """Custom type save based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("save", 1))
    )


_Save_Type.__name__ = "Integer32"
_Save_Object = MibScalar
save = _Save_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3, 2),
    _Save_Type()
)
save.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    save.setStatus("current")
_LastSaveTime_Type = DisplayString
_LastSaveTime_Object = MibScalar
lastSaveTime = _LastSaveTime_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3, 3),
    _LastSaveTime_Type()
)
lastSaveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSaveTime.setStatus("current")


class _Timezone_Type(OctetString):
    """Custom type timezone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Timezone_Type.__name__ = "OctetString"
_Timezone_Object = MibScalar
timezone = _Timezone_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3, 4),
    _Timezone_Type()
)
timezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timezone.setStatus("current")


class _SystemTime_Type(OctetString):
    """Custom type systemTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemTime_Type.__name__ = "OctetString"
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3, 5),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")


class _LastCommand_Type(OctetString):
    """Custom type lastCommand based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_LastCommand_Type.__name__ = "OctetString"
_LastCommand_Object = MibScalar
lastCommand = _LastCommand_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3, 6),
    _LastCommand_Type()
)
lastCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastCommand.setStatus("current")


class _FanCtrlStartTemp_Type(Integer32):
    """Custom type fanCtrlStartTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FanCtrlStartTemp_Type.__name__ = "Integer32"
_FanCtrlStartTemp_Object = MibScalar
fanCtrlStartTemp = _FanCtrlStartTemp_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3, 7),
    _FanCtrlStartTemp_Type()
)
fanCtrlStartTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanCtrlStartTemp.setStatus("current")


class _FanCtrlStopTemp_Type(Integer32):
    """Custom type fanCtrlStopTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 30),
    )


_FanCtrlStopTemp_Type.__name__ = "Integer32"
_FanCtrlStopTemp_Object = MibScalar
fanCtrlStopTemp = _FanCtrlStopTemp_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3, 8),
    _FanCtrlStopTemp_Type()
)
fanCtrlStopTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanCtrlStopTemp.setStatus("current")


class _FanRpmConfig_Type(Integer32):
    """Custom type fanRpmConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 20000),
    )


_FanRpmConfig_Type.__name__ = "Integer32"
_FanRpmConfig_Object = MibScalar
fanRpmConfig = _FanRpmConfig_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3, 9),
    _FanRpmConfig_Type()
)
fanRpmConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmConfig.setStatus("current")


class _FanLowTolerance_Type(Integer32):
    """Custom type fanLowTolerance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 80),
    )


_FanLowTolerance_Type.__name__ = "Integer32"
_FanLowTolerance_Object = MibScalar
fanLowTolerance = _FanLowTolerance_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3, 10),
    _FanLowTolerance_Type()
)
fanLowTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanLowTolerance.setStatus("current")
_FanLowToleranceValue_Type = Integer32
_FanLowToleranceValue_Object = MibScalar
fanLowToleranceValue = _FanLowToleranceValue_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3, 11),
    _FanLowToleranceValue_Type()
)
fanLowToleranceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanLowToleranceValue.setStatus("current")


class _FanHighTolerance_Type(Integer32):
    """Custom type fanHighTolerance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 80),
    )


_FanHighTolerance_Type.__name__ = "Integer32"
_FanHighTolerance_Object = MibScalar
fanHighTolerance = _FanHighTolerance_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3, 12),
    _FanHighTolerance_Type()
)
fanHighTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanHighTolerance.setStatus("current")
_FanHighToleranceValue_Type = Integer32
_FanHighToleranceValue_Object = MibScalar
fanHighToleranceValue = _FanHighToleranceValue_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3, 13),
    _FanHighToleranceValue_Type()
)
fanHighToleranceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanHighToleranceValue.setStatus("current")


class _TempHighThreshold_Type(Integer32):
    """Custom type tempHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TempHighThreshold_Type.__name__ = "Integer32"
_TempHighThreshold_Object = MibScalar
tempHighThreshold = _TempHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3, 14),
    _TempHighThreshold_Type()
)
tempHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHighThreshold.setStatus("current")


class _TempLowThreshold_Type(Integer32):
    """Custom type tempLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, -1),
    )


_TempLowThreshold_Type.__name__ = "Integer32"
_TempLowThreshold_Object = MibScalar
tempLowThreshold = _TempLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 3, 15),
    _TempLowThreshold_Type()
)
tempLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowThreshold.setStatus("current")
_MgmtVlanConfig_ObjectIdentity = ObjectIdentity
mgmtVlanConfig = _MgmtVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 5)
)


class _MgmtOuterVlan_Type(Integer32):
    """Custom type mgmtOuterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MgmtOuterVlan_Type.__name__ = "Integer32"
_MgmtOuterVlan_Object = MibScalar
mgmtOuterVlan = _MgmtOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 5, 1),
    _MgmtOuterVlan_Type()
)
mgmtOuterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtOuterVlan.setStatus("current")


class _MgmtOuterVlanPriority_Type(Integer32):
    """Custom type mgmtOuterVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MgmtOuterVlanPriority_Type.__name__ = "Integer32"
_MgmtOuterVlanPriority_Object = MibScalar
mgmtOuterVlanPriority = _MgmtOuterVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 5, 2),
    _MgmtOuterVlanPriority_Type()
)
mgmtOuterVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtOuterVlanPriority.setStatus("current")


class _MgmtInnerVlan_Type(Integer32):
    """Custom type mgmtInnerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MgmtInnerVlan_Type.__name__ = "Integer32"
_MgmtInnerVlan_Object = MibScalar
mgmtInnerVlan = _MgmtInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 5, 3),
    _MgmtInnerVlan_Type()
)
mgmtInnerVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtInnerVlan.setStatus("current")


class _MgmtInnerVlanPriority_Type(Integer32):
    """Custom type mgmtInnerVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MgmtInnerVlanPriority_Type.__name__ = "Integer32"
_MgmtInnerVlanPriority_Object = MibScalar
mgmtInnerVlanPriority = _MgmtInnerVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 1, 5, 4),
    _MgmtInnerVlanPriority_Type()
)
mgmtInnerVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtInnerVlanPriority.setStatus("current")
_AccessInfo_ObjectIdentity = ObjectIdentity
accessInfo = _AccessInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 2)
)
_PInbandIPAddress_Type = IpAddress
_PInbandIPAddress_Object = MibScalar
pInbandIPAddress = _PInbandIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 2, 1),
    _PInbandIPAddress_Type()
)
pInbandIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pInbandIPAddress.setStatus("current")
_PInbandNetMask_Type = IpAddress
_PInbandNetMask_Object = MibScalar
pInbandNetMask = _PInbandNetMask_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 2, 2),
    _PInbandNetMask_Type()
)
pInbandNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pInbandNetMask.setStatus("current")
_PInbandNetworkAddress_Type = IpAddress
_PInbandNetworkAddress_Object = MibScalar
pInbandNetworkAddress = _PInbandNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 2, 3),
    _PInbandNetworkAddress_Type()
)
pInbandNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pInbandNetworkAddress.setStatus("current")
_PInbandMACAddress_Type = MacAddress
_PInbandMACAddress_Object = MibScalar
pInbandMACAddress = _PInbandMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 2, 4),
    _PInbandMACAddress_Type()
)
pInbandMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pInbandMACAddress.setStatus("current")
_POOBIPAddress_Type = IpAddress
_POOBIPAddress_Object = MibScalar
pOOBIPAddress = _POOBIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 2, 5),
    _POOBIPAddress_Type()
)
pOOBIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pOOBIPAddress.setStatus("current")
_POOBNetMask_Type = IpAddress
_POOBNetMask_Object = MibScalar
pOOBNetMask = _POOBNetMask_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 2, 6),
    _POOBNetMask_Type()
)
pOOBNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pOOBNetMask.setStatus("current")
_POOBNetworkAddress_Type = IpAddress
_POOBNetworkAddress_Object = MibScalar
pOOBNetworkAddress = _POOBNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 2, 7),
    _POOBNetworkAddress_Type()
)
pOOBNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pOOBNetworkAddress.setStatus("current")
_POOBMACAddress_Type = MacAddress
_POOBMACAddress_Object = MibScalar
pOOBMACAddress = _POOBMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 2, 8),
    _POOBMACAddress_Type()
)
pOOBMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pOOBMACAddress.setStatus("current")
_PDefaultGateway_Type = IpAddress
_PDefaultGateway_Object = MibScalar
pDefaultGateway = _PDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 2, 9),
    _PDefaultGateway_Type()
)
pDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pDefaultGateway.setStatus("current")
_ConsoleInformation_ObjectIdentity = ObjectIdentity
consoleInformation = _ConsoleInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 3)
)


class _ConsoleBaudRate_Type(Integer32):
    """Custom type consoleBaudRate based on Integer32"""
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
        *(("bps9600", 1),
          ("bps19200", 2),
          ("bps38400", 3),
          ("bps57600", 4),
          ("bps115200", 5))
    )


_ConsoleBaudRate_Type.__name__ = "Integer32"
_ConsoleBaudRate_Object = MibScalar
consoleBaudRate = _ConsoleBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 3, 1),
    _ConsoleBaudRate_Type()
)
consoleBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleBaudRate.setStatus("current")


class _ConsoleCharSize_Type(Integer32):
    """Custom type consoleCharSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("sevenBits", 7),
          ("eightBits", 8))
    )


_ConsoleCharSize_Type.__name__ = "Integer32"
_ConsoleCharSize_Object = MibScalar
consoleCharSize = _ConsoleCharSize_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 3, 2),
    _ConsoleCharSize_Type()
)
consoleCharSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleCharSize.setStatus("current")


class _ConsoleParityBits_Type(Integer32):
    """Custom type consoleParityBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noParity", 1),
          ("evenParity", 2),
          ("oddParity", 3))
    )


_ConsoleParityBits_Type.__name__ = "Integer32"
_ConsoleParityBits_Object = MibScalar
consoleParityBits = _ConsoleParityBits_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 3, 3),
    _ConsoleParityBits_Type()
)
consoleParityBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleParityBits.setStatus("current")


class _ConsoleStopBits_Type(Integer32):
    """Custom type consoleStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_ConsoleStopBits_Type.__name__ = "Integer32"
_ConsoleStopBits_Object = MibScalar
consoleStopBits = _ConsoleStopBits_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 3, 4),
    _ConsoleStopBits_Type()
)
consoleStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleStopBits.setStatus("current")


class _ConsoleFlowControl_Type(Integer32):
    """Custom type consoleFlowControl based on Integer32"""
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
          ("hardware", 2),
          ("xonXoff", 3))
    )


_ConsoleFlowControl_Type.__name__ = "Integer32"
_ConsoleFlowControl_Object = MibScalar
consoleFlowControl = _ConsoleFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2, 1, 3, 5),
    _ConsoleFlowControl_Type()
)
consoleFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleFlowControl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BTI8xx-SYSTEM-MIB",
    **{"systemConfig": systemConfig,
       "systemManagement": systemManagement,
       "systemInfo": systemInfo,
       "systemName": systemName,
       "autoLogoutTime": autoLogoutTime,
       "systemUpTime": systemUpTime,
       "systemHWVersion": systemHWVersion,
       "systemSWVersion": systemSWVersion,
       "systemSWDateAndTime": systemSWDateAndTime,
       "systemTemperature": systemTemperature,
       "systemProductName": systemProductName,
       "configAndImageMgmt": configAndImageMgmt,
       "serverConfig": serverConfig,
       "serverIpAddr": serverIpAddr,
       "ftpUserName": ftpUserName,
       "ftpUserPasswd": ftpUserPasswd,
       "serverInterfaceType": serverInterfaceType,
       "configMgmt": configMgmt,
       "cfgFileName": cfgFileName,
       "cfgFileControl": cfgFileControl,
       "cfgFileStatus": cfgFileStatus,
       "imageMgmt": imageMgmt,
       "upgradeImageSWFileName": upgradeImageSWFileName,
       "upgradeImageSW": upgradeImageSW,
       "upgradeImageSWStatus": upgradeImageSWStatus,
       "upgradeImageSWDateAndTime": upgradeImageSWDateAndTime,
       "imageInfoTable": imageInfoTable,
       "imageInfoEntry": imageInfoEntry,
       "imageInfoIndex": imageInfoIndex,
       "imageInfoVersion": imageInfoVersion,
       "imageInfoCreated": imageInfoCreated,
       "imageInfoSize": imageInfoSize,
       "imageInfoCurrent": imageInfoCurrent,
       "miscellaneous": miscellaneous,
       "reboot": reboot,
       "save": save,
       "lastSaveTime": lastSaveTime,
       "timezone": timezone,
       "systemTime": systemTime,
       "lastCommand": lastCommand,
       "fanCtrlStartTemp": fanCtrlStartTemp,
       "fanCtrlStopTemp": fanCtrlStopTemp,
       "fanRpmConfig": fanRpmConfig,
       "fanLowTolerance": fanLowTolerance,
       "fanLowToleranceValue": fanLowToleranceValue,
       "fanHighTolerance": fanHighTolerance,
       "fanHighToleranceValue": fanHighToleranceValue,
       "tempHighThreshold": tempHighThreshold,
       "tempLowThreshold": tempLowThreshold,
       "mgmtVlanConfig": mgmtVlanConfig,
       "mgmtOuterVlan": mgmtOuterVlan,
       "mgmtOuterVlanPriority": mgmtOuterVlanPriority,
       "mgmtInnerVlan": mgmtInnerVlan,
       "mgmtInnerVlanPriority": mgmtInnerVlanPriority,
       "accessInfo": accessInfo,
       "pInbandIPAddress": pInbandIPAddress,
       "pInbandNetMask": pInbandNetMask,
       "pInbandNetworkAddress": pInbandNetworkAddress,
       "pInbandMACAddress": pInbandMACAddress,
       "pOOBIPAddress": pOOBIPAddress,
       "pOOBNetMask": pOOBNetMask,
       "pOOBNetworkAddress": pOOBNetworkAddress,
       "pOOBMACAddress": pOOBMACAddress,
       "pDefaultGateway": pDefaultGateway,
       "consoleInformation": consoleInformation,
       "consoleBaudRate": consoleBaudRate,
       "consoleCharSize": consoleCharSize,
       "consoleParityBits": consoleParityBits,
       "consoleStopBits": consoleStopBits,
       "consoleFlowControl": consoleFlowControl}
)
