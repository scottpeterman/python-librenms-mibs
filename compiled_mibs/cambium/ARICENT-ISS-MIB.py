# SNMP MIB module (ARICENT-ISS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cambium\cnmatrix\ARICENT-ISS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:34 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

iss = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81)
)
if mibBuilder.loadTexts:
    iss.setRevisions(
        ("2022-03-31 00:00",
         "2022-01-21 00:00",
         "2022-01-12 00:00",
         "2012-09-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_IssNotifications_ObjectIdentity = ObjectIdentity
issNotifications = _IssNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 0)
)
_IssSystem_ObjectIdentity = ObjectIdentity
issSystem = _IssSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1)
)


class _IssSwitchName_Type(DisplayString):
    """Custom type issSwitchName based on DisplayString"""
    defaultValue = OctetString("ISS")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_IssSwitchName_Type.__name__ = "DisplayString"
_IssSwitchName_Object = MibScalar
issSwitchName = _IssSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 1),
    _IssSwitchName_Type()
)
issSwitchName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issSwitchName.setStatus("current")


class _IssHardwareVersion_Type(DisplayString):
    """Custom type issHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_IssHardwareVersion_Type.__name__ = "DisplayString"
_IssHardwareVersion_Object = MibScalar
issHardwareVersion = _IssHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 2),
    _IssHardwareVersion_Type()
)
issHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issHardwareVersion.setStatus("current")


class _IssFirmwareVersion_Type(DisplayString):
    """Custom type issFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_IssFirmwareVersion_Type.__name__ = "DisplayString"
_IssFirmwareVersion_Object = MibScalar
issFirmwareVersion = _IssFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 3),
    _IssFirmwareVersion_Type()
)
issFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issFirmwareVersion.setStatus("current")


class _IssDefaultIpAddrCfgMode_Type(Integer32):
    """Custom type issDefaultIpAddrCfgMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("dynamic", 2))
    )


_IssDefaultIpAddrCfgMode_Type.__name__ = "Integer32"
_IssDefaultIpAddrCfgMode_Object = MibScalar
issDefaultIpAddrCfgMode = _IssDefaultIpAddrCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 4),
    _IssDefaultIpAddrCfgMode_Type()
)
issDefaultIpAddrCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDefaultIpAddrCfgMode.setStatus("current")
_IssDefaultIpAddr_Type = IpAddress
_IssDefaultIpAddr_Object = MibScalar
issDefaultIpAddr = _IssDefaultIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 5),
    _IssDefaultIpAddr_Type()
)
issDefaultIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDefaultIpAddr.setStatus("current")
_IssDefaultIpSubnetMask_Type = IpAddress
_IssDefaultIpSubnetMask_Object = MibScalar
issDefaultIpSubnetMask = _IssDefaultIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 6),
    _IssDefaultIpSubnetMask_Type()
)
issDefaultIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDefaultIpSubnetMask.setStatus("current")
_IssEffectiveIpAddr_Type = IpAddress
_IssEffectiveIpAddr_Object = MibScalar
issEffectiveIpAddr = _IssEffectiveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 7),
    _IssEffectiveIpAddr_Type()
)
issEffectiveIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issEffectiveIpAddr.setStatus("deprecated")


class _IssDefaultInterface_Type(DisplayString):
    """Custom type issDefaultInterface based on DisplayString"""
    defaultValue = OctetString("eth0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_IssDefaultInterface_Type.__name__ = "DisplayString"
_IssDefaultInterface_Object = MibScalar
issDefaultInterface = _IssDefaultInterface_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 8),
    _IssDefaultInterface_Type()
)
issDefaultInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDefaultInterface.setStatus("current")


class _IssRestart_Type(TruthValue):
    """Custom type issRestart based on TruthValue"""
    defaultValue = 2


_IssRestart_Type.__name__ = "TruthValue"
_IssRestart_Object = MibScalar
issRestart = _IssRestart_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 9),
    _IssRestart_Type()
)
issRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issRestart.setStatus("current")


class _IssConfigSaveOption_Type(Integer32):
    """Custom type issConfigSaveOption based on Integer32"""
    defaultValue = 1

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
        *(("noSave", 1),
          ("flashSave", 2),
          ("remoteSave", 3),
          ("startupConfig", 4))
    )


_IssConfigSaveOption_Type.__name__ = "Integer32"
_IssConfigSaveOption_Object = MibScalar
issConfigSaveOption = _IssConfigSaveOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 10),
    _IssConfigSaveOption_Type()
)
issConfigSaveOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigSaveOption.setStatus("current")
_IssConfigSaveIpAddr_Type = IpAddress
_IssConfigSaveIpAddr_Object = MibScalar
issConfigSaveIpAddr = _IssConfigSaveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 11),
    _IssConfigSaveIpAddr_Type()
)
issConfigSaveIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigSaveIpAddr.setStatus("deprecated")


class _IssConfigSaveFileName_Type(DisplayString):
    """Custom type issConfigSaveFileName based on DisplayString"""
    defaultValue = OctetString("iss.conf")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_IssConfigSaveFileName_Type.__name__ = "DisplayString"
_IssConfigSaveFileName_Object = MibScalar
issConfigSaveFileName = _IssConfigSaveFileName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 12),
    _IssConfigSaveFileName_Type()
)
issConfigSaveFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigSaveFileName.setStatus("current")


class _IssInitiateConfigSave_Type(TruthValue):
    """Custom type issInitiateConfigSave based on TruthValue"""
    defaultValue = 2


_IssInitiateConfigSave_Type.__name__ = "TruthValue"
_IssInitiateConfigSave_Object = MibScalar
issInitiateConfigSave = _IssInitiateConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 13),
    _IssInitiateConfigSave_Type()
)
issInitiateConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issInitiateConfigSave.setStatus("current")


class _IssConfigSaveStatus_Type(Integer32):
    """Custom type issConfigSaveStatus based on Integer32"""
    defaultValue = 4

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
        *(("saveInProgress", 1),
          ("saveSuccessful", 2),
          ("saveFailed", 3),
          ("notInitiated", 4))
    )


_IssConfigSaveStatus_Type.__name__ = "Integer32"
_IssConfigSaveStatus_Object = MibScalar
issConfigSaveStatus = _IssConfigSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 14),
    _IssConfigSaveStatus_Type()
)
issConfigSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issConfigSaveStatus.setStatus("current")


class _IssConfigRestoreOption_Type(Integer32):
    """Custom type issConfigRestoreOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRestore", 1),
          ("restore", 2))
    )


_IssConfigRestoreOption_Type.__name__ = "Integer32"
_IssConfigRestoreOption_Object = MibScalar
issConfigRestoreOption = _IssConfigRestoreOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 15),
    _IssConfigRestoreOption_Type()
)
issConfigRestoreOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigRestoreOption.setStatus("current")
_IssConfigRestoreIpAddr_Type = IpAddress
_IssConfigRestoreIpAddr_Object = MibScalar
issConfigRestoreIpAddr = _IssConfigRestoreIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 16),
    _IssConfigRestoreIpAddr_Type()
)
issConfigRestoreIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigRestoreIpAddr.setStatus("deprecated")


class _IssConfigRestoreFileName_Type(DisplayString):
    """Custom type issConfigRestoreFileName based on DisplayString"""
    defaultValue = OctetString("iss.conf")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_IssConfigRestoreFileName_Type.__name__ = "DisplayString"
_IssConfigRestoreFileName_Object = MibScalar
issConfigRestoreFileName = _IssConfigRestoreFileName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 17),
    _IssConfigRestoreFileName_Type()
)
issConfigRestoreFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigRestoreFileName.setStatus("current")


class _IssInitiateConfigRestore_Type(TruthValue):
    """Custom type issInitiateConfigRestore based on TruthValue"""
    defaultValue = 2


_IssInitiateConfigRestore_Type.__name__ = "TruthValue"
_IssInitiateConfigRestore_Object = MibScalar
issInitiateConfigRestore = _IssInitiateConfigRestore_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 18),
    _IssInitiateConfigRestore_Type()
)
issInitiateConfigRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issInitiateConfigRestore.setStatus("current")


class _IssConfigRestoreStatus_Type(Integer32):
    """Custom type issConfigRestoreStatus based on Integer32"""
    defaultValue = 4

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
        *(("restoreInprogress", 1),
          ("restoreSuccessful", 2),
          ("restoreFailed", 3),
          ("notInitiated", 4))
    )


_IssConfigRestoreStatus_Type.__name__ = "Integer32"
_IssConfigRestoreStatus_Object = MibScalar
issConfigRestoreStatus = _IssConfigRestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 19),
    _IssConfigRestoreStatus_Type()
)
issConfigRestoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issConfigRestoreStatus.setStatus("current")
_IssDlImageFromIp_Type = IpAddress
_IssDlImageFromIp_Object = MibScalar
issDlImageFromIp = _IssDlImageFromIp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 20),
    _IssDlImageFromIp_Type()
)
issDlImageFromIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDlImageFromIp.setStatus("deprecated")


class _IssDlImageName_Type(DisplayString):
    """Custom type issDlImageName based on DisplayString"""
    defaultValue = OctetString("iss.exe")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_IssDlImageName_Type.__name__ = "DisplayString"
_IssDlImageName_Object = MibScalar
issDlImageName = _IssDlImageName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 21),
    _IssDlImageName_Type()
)
issDlImageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDlImageName.setStatus("current")
_IssInitiateDlImage_Type = TruthValue
_IssInitiateDlImage_Object = MibScalar
issInitiateDlImage = _IssInitiateDlImage_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 22),
    _IssInitiateDlImage_Type()
)
issInitiateDlImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issInitiateDlImage.setStatus("current")


class _IssLoggingOption_Type(Integer32):
    """Custom type issLoggingOption based on Integer32"""
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
        *(("console", 1),
          ("file", 2),
          ("flash", 3))
    )


_IssLoggingOption_Type.__name__ = "Integer32"
_IssLoggingOption_Object = MibScalar
issLoggingOption = _IssLoggingOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 23),
    _IssLoggingOption_Type()
)
issLoggingOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issLoggingOption.setStatus("current")
_IssUploadLogFileToIp_Type = IpAddress
_IssUploadLogFileToIp_Object = MibScalar
issUploadLogFileToIp = _IssUploadLogFileToIp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 24),
    _IssUploadLogFileToIp_Type()
)
issUploadLogFileToIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issUploadLogFileToIp.setStatus("deprecated")


class _IssLogFileName_Type(DisplayString):
    """Custom type issLogFileName based on DisplayString"""
    defaultValue = OctetString("iss.log")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_IssLogFileName_Type.__name__ = "DisplayString"
_IssLogFileName_Object = MibScalar
issLogFileName = _IssLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 25),
    _IssLogFileName_Type()
)
issLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issLogFileName.setStatus("current")
_IssInitiateUlLogFile_Type = TruthValue
_IssInitiateUlLogFile_Object = MibScalar
issInitiateUlLogFile = _IssInitiateUlLogFile_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 26),
    _IssInitiateUlLogFile_Type()
)
issInitiateUlLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issInitiateUlLogFile.setStatus("current")


class _IssRemoteSaveStatus_Type(Integer32):
    """Custom type issRemoteSaveStatus based on Integer32"""
    defaultValue = 4

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
        *(("inprogress", 1),
          ("successful", 2),
          ("failed", 3),
          ("notInitiated", 4))
    )


_IssRemoteSaveStatus_Type.__name__ = "Integer32"
_IssRemoteSaveStatus_Object = MibScalar
issRemoteSaveStatus = _IssRemoteSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 27),
    _IssRemoteSaveStatus_Type()
)
issRemoteSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issRemoteSaveStatus.setStatus("current")


class _IssDownloadStatus_Type(Integer32):
    """Custom type issDownloadStatus based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("inprogress", 1),
          ("successful", 2),
          ("failed", 3),
          ("configDefaultNeeded", 4),
          ("configDefaultInProgress", 5),
          ("configDeafultAborted", 6),
          ("notInitiated", 7))
    )


_IssDownloadStatus_Type.__name__ = "Integer32"
_IssDownloadStatus_Object = MibScalar
issDownloadStatus = _IssDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 28),
    _IssDownloadStatus_Type()
)
issDownloadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDownloadStatus.setStatus("current")


class _IssSysContact_Type(DisplayString):
    """Custom type issSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_IssSysContact_Type.__name__ = "DisplayString"
_IssSysContact_Object = MibScalar
issSysContact = _IssSysContact_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 29),
    _IssSysContact_Type()
)
issSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issSysContact.setStatus("deprecated")


class _IssSysLocation_Type(DisplayString):
    """Custom type issSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_IssSysLocation_Type.__name__ = "DisplayString"
_IssSysLocation_Object = MibScalar
issSysLocation = _IssSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 30),
    _IssSysLocation_Type()
)
issSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issSysLocation.setStatus("deprecated")


class _IssLoginAuthentication_Type(Integer32):
    """Custom type issLoginAuthentication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remoteRadius", 2),
          ("remoteTacacs", 3),
          ("radiusFallbackToLocal", 4),
          ("tacacsFallbackToLocal", 5),
          ("ldap", 6))
    )


_IssLoginAuthentication_Type.__name__ = "Integer32"
_IssLoginAuthentication_Object = MibScalar
issLoginAuthentication = _IssLoginAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 31),
    _IssLoginAuthentication_Type()
)
issLoginAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issLoginAuthentication.setStatus("current")


class _IssSwitchBaseMacAddress_Type(MacAddress):
    """Custom type issSwitchBaseMacAddress based on MacAddress"""
    defaultHexValue = "000102030405"


_IssSwitchBaseMacAddress_Type.__name__ = "MacAddress"
_IssSwitchBaseMacAddress_Object = MibScalar
issSwitchBaseMacAddress = _IssSwitchBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 32),
    _IssSwitchBaseMacAddress_Type()
)
issSwitchBaseMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issSwitchBaseMacAddress.setStatus("current")
_IssOOBInterface_Type = TruthValue
_IssOOBInterface_Object = MibScalar
issOOBInterface = _IssOOBInterface_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 33),
    _IssOOBInterface_Type()
)
issOOBInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issOOBInterface.setStatus("current")


class _IssSwitchDate_Type(DisplayString):
    """Custom type issSwitchDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_IssSwitchDate_Type.__name__ = "DisplayString"
_IssSwitchDate_Object = MibScalar
issSwitchDate = _IssSwitchDate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 34),
    _IssSwitchDate_Type()
)
issSwitchDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issSwitchDate.setStatus("current")
_IssNoCliConsole_Type = TruthValue
_IssNoCliConsole_Object = MibScalar
issNoCliConsole = _IssNoCliConsole_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 35),
    _IssNoCliConsole_Type()
)
issNoCliConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issNoCliConsole.setStatus("current")


class _IssDefaultIpAddrAllocProtocol_Type(Integer32):
    """Custom type issDefaultIpAddrAllocProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rarp", 1),
          ("dhcp", 2),
          ("bootp", 3))
    )


_IssDefaultIpAddrAllocProtocol_Type.__name__ = "Integer32"
_IssDefaultIpAddrAllocProtocol_Object = MibScalar
issDefaultIpAddrAllocProtocol = _IssDefaultIpAddrAllocProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 36),
    _IssDefaultIpAddrAllocProtocol_Type()
)
issDefaultIpAddrAllocProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDefaultIpAddrAllocProtocol.setStatus("current")


class _IssHttpPort_Type(Integer32):
    """Custom type issHttpPort based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IssHttpPort_Type.__name__ = "Integer32"
_IssHttpPort_Object = MibScalar
issHttpPort = _IssHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 37),
    _IssHttpPort_Type()
)
issHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issHttpPort.setStatus("current")


class _IssHttpStatus_Type(Integer32):
    """Custom type issHttpStatus based on Integer32"""
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


_IssHttpStatus_Type.__name__ = "Integer32"
_IssHttpStatus_Object = MibScalar
issHttpStatus = _IssHttpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 38),
    _IssHttpStatus_Type()
)
issHttpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issHttpStatus.setStatus("current")


class _IssConfigRestoreFileVersion_Type(DisplayString):
    """Custom type issConfigRestoreFileVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_IssConfigRestoreFileVersion_Type.__name__ = "DisplayString"
_IssConfigRestoreFileVersion_Object = MibScalar
issConfigRestoreFileVersion = _IssConfigRestoreFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 39),
    _IssConfigRestoreFileVersion_Type()
)
issConfigRestoreFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issConfigRestoreFileVersion.setStatus("current")


class _IssDefaultRmIfName_Type(DisplayString):
    """Custom type issDefaultRmIfName based on DisplayString"""
    defaultValue = OctetString("NONE")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_IssDefaultRmIfName_Type.__name__ = "DisplayString"
_IssDefaultRmIfName_Object = MibScalar
issDefaultRmIfName = _IssDefaultRmIfName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 40),
    _IssDefaultRmIfName_Type()
)
issDefaultRmIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDefaultRmIfName.setStatus("current")


class _IssDefaultVlanId_Type(Integer32):
    """Custom type issDefaultVlanId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IssDefaultVlanId_Type.__name__ = "Integer32"
_IssDefaultVlanId_Object = MibScalar
issDefaultVlanId = _IssDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 41),
    _IssDefaultVlanId_Type()
)
issDefaultVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDefaultVlanId.setStatus("current")


class _IssNpapiMode_Type(DisplayString):
    """Custom type issNpapiMode based on DisplayString"""
    defaultValue = OctetString("Synchronous")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_IssNpapiMode_Type.__name__ = "DisplayString"
_IssNpapiMode_Object = MibScalar
issNpapiMode = _IssNpapiMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 42),
    _IssNpapiMode_Type()
)
issNpapiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issNpapiMode.setStatus("current")


class _IssConfigAutoSaveTrigger_Type(TruthValue):
    """Custom type issConfigAutoSaveTrigger based on TruthValue"""
    defaultValue = 2


_IssConfigAutoSaveTrigger_Type.__name__ = "TruthValue"
_IssConfigAutoSaveTrigger_Object = MibScalar
issConfigAutoSaveTrigger = _IssConfigAutoSaveTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 43),
    _IssConfigAutoSaveTrigger_Type()
)
issConfigAutoSaveTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigAutoSaveTrigger.setStatus("current")


class _IssConfigIncrSaveFlag_Type(TruthValue):
    """Custom type issConfigIncrSaveFlag based on TruthValue"""
    defaultValue = 2


_IssConfigIncrSaveFlag_Type.__name__ = "TruthValue"
_IssConfigIncrSaveFlag_Object = MibScalar
issConfigIncrSaveFlag = _IssConfigIncrSaveFlag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 44),
    _IssConfigIncrSaveFlag_Type()
)
issConfigIncrSaveFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigIncrSaveFlag.setStatus("current")


class _IssConfigRollbackFlag_Type(Integer32):
    """Custom type issConfigRollbackFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IssConfigRollbackFlag_Type.__name__ = "Integer32"
_IssConfigRollbackFlag_Object = MibScalar
issConfigRollbackFlag = _IssConfigRollbackFlag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 45),
    _IssConfigRollbackFlag_Type()
)
issConfigRollbackFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigRollbackFlag.setStatus("current")


class _IssConfigSyncUpOperation_Type(Integer32):
    """Custom type issConfigSyncUpOperation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("syncup", 1)
    )


_IssConfigSyncUpOperation_Type.__name__ = "Integer32"
_IssConfigSyncUpOperation_Object = MibScalar
issConfigSyncUpOperation = _IssConfigSyncUpOperation_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 46),
    _IssConfigSyncUpOperation_Type()
)
issConfigSyncUpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigSyncUpOperation.setStatus("current")
_IssFrontPanelPortCount_Type = Integer32
_IssFrontPanelPortCount_Object = MibScalar
issFrontPanelPortCount = _IssFrontPanelPortCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 47),
    _IssFrontPanelPortCount_Type()
)
issFrontPanelPortCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issFrontPanelPortCount.setStatus("current")


class _IssAuditLogStatus_Type(Integer32):
    """Custom type issAuditLogStatus based on Integer32"""
    defaultValue = 2

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


_IssAuditLogStatus_Type.__name__ = "Integer32"
_IssAuditLogStatus_Object = MibScalar
issAuditLogStatus = _IssAuditLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 48),
    _IssAuditLogStatus_Type()
)
issAuditLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issAuditLogStatus.setStatus("current")


class _IssAuditLogFileName_Type(DisplayString):
    """Custom type issAuditLogFileName based on DisplayString"""
    defaultValue = OctetString("config.txt")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_IssAuditLogFileName_Type.__name__ = "DisplayString"
_IssAuditLogFileName_Object = MibScalar
issAuditLogFileName = _IssAuditLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 49),
    _IssAuditLogFileName_Type()
)
issAuditLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issAuditLogFileName.setStatus("current")


class _IssAuditLogFileSize_Type(Unsigned32):
    """Custom type issAuditLogFileSize based on Unsigned32"""
    defaultValue = 1048576

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 1048576),
    )


_IssAuditLogFileSize_Type.__name__ = "Unsigned32"
_IssAuditLogFileSize_Object = MibScalar
issAuditLogFileSize = _IssAuditLogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 50),
    _IssAuditLogFileSize_Type()
)
issAuditLogFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issAuditLogFileSize.setStatus("current")


class _IssAuditLogReset_Type(TruthValue):
    """Custom type issAuditLogReset based on TruthValue"""
    defaultValue = 2


_IssAuditLogReset_Type.__name__ = "TruthValue"
_IssAuditLogReset_Object = MibScalar
issAuditLogReset = _IssAuditLogReset_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 51),
    _IssAuditLogReset_Type()
)
issAuditLogReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issAuditLogReset.setStatus("current")
_IssAuditLogRemoteIpAddr_Type = IpAddress
_IssAuditLogRemoteIpAddr_Object = MibScalar
issAuditLogRemoteIpAddr = _IssAuditLogRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 52),
    _IssAuditLogRemoteIpAddr_Type()
)
issAuditLogRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issAuditLogRemoteIpAddr.setStatus("deprecated")


class _IssAuditLogInitiateTransfer_Type(TruthValue):
    """Custom type issAuditLogInitiateTransfer based on TruthValue"""
    defaultValue = 2


_IssAuditLogInitiateTransfer_Type.__name__ = "TruthValue"
_IssAuditLogInitiateTransfer_Object = MibScalar
issAuditLogInitiateTransfer = _IssAuditLogInitiateTransfer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 53),
    _IssAuditLogInitiateTransfer_Type()
)
issAuditLogInitiateTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issAuditLogInitiateTransfer.setStatus("current")


class _IssAuditTransferFileName_Type(DisplayString):
    """Custom type issAuditTransferFileName based on DisplayString"""
    defaultValue = OctetString("config.txt")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_IssAuditTransferFileName_Type.__name__ = "DisplayString"
_IssAuditTransferFileName_Object = MibScalar
issAuditTransferFileName = _IssAuditTransferFileName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 54),
    _IssAuditTransferFileName_Type()
)
issAuditTransferFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issAuditTransferFileName.setStatus("current")


class _IssDownLoadTransferMode_Type(Integer32):
    """Custom type issDownLoadTransferMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("sftp", 2))
    )


_IssDownLoadTransferMode_Type.__name__ = "Integer32"
_IssDownLoadTransferMode_Object = MibScalar
issDownLoadTransferMode = _IssDownLoadTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 55),
    _IssDownLoadTransferMode_Type()
)
issDownLoadTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDownLoadTransferMode.setStatus("current")


class _IssDownLoadUserName_Type(DisplayString):
    """Custom type issDownLoadUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IssDownLoadUserName_Type.__name__ = "DisplayString"
_IssDownLoadUserName_Object = MibScalar
issDownLoadUserName = _IssDownLoadUserName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 56),
    _IssDownLoadUserName_Type()
)
issDownLoadUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDownLoadUserName.setStatus("current")


class _IssDownLoadPassword_Type(DisplayString):
    """Custom type issDownLoadPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IssDownLoadPassword_Type.__name__ = "DisplayString"
_IssDownLoadPassword_Object = MibScalar
issDownLoadPassword = _IssDownLoadPassword_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 57),
    _IssDownLoadPassword_Type()
)
issDownLoadPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDownLoadPassword.setStatus("current")


class _IssUploadLogTransferMode_Type(Integer32):
    """Custom type issUploadLogTransferMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("sftp", 2))
    )


_IssUploadLogTransferMode_Type.__name__ = "Integer32"
_IssUploadLogTransferMode_Object = MibScalar
issUploadLogTransferMode = _IssUploadLogTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 58),
    _IssUploadLogTransferMode_Type()
)
issUploadLogTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issUploadLogTransferMode.setStatus("current")


class _IssUploadLogUserName_Type(DisplayString):
    """Custom type issUploadLogUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IssUploadLogUserName_Type.__name__ = "DisplayString"
_IssUploadLogUserName_Object = MibScalar
issUploadLogUserName = _IssUploadLogUserName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 59),
    _IssUploadLogUserName_Type()
)
issUploadLogUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issUploadLogUserName.setStatus("current")


class _IssUploadLogPasswd_Type(DisplayString):
    """Custom type issUploadLogPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IssUploadLogPasswd_Type.__name__ = "DisplayString"
_IssUploadLogPasswd_Object = MibScalar
issUploadLogPasswd = _IssUploadLogPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 60),
    _IssUploadLogPasswd_Type()
)
issUploadLogPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issUploadLogPasswd.setStatus("current")


class _IssConfigSaveTransferMode_Type(Integer32):
    """Custom type issConfigSaveTransferMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("sftp", 2))
    )


_IssConfigSaveTransferMode_Type.__name__ = "Integer32"
_IssConfigSaveTransferMode_Object = MibScalar
issConfigSaveTransferMode = _IssConfigSaveTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 61),
    _IssConfigSaveTransferMode_Type()
)
issConfigSaveTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigSaveTransferMode.setStatus("current")


class _IssConfigSaveUserName_Type(DisplayString):
    """Custom type issConfigSaveUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IssConfigSaveUserName_Type.__name__ = "DisplayString"
_IssConfigSaveUserName_Object = MibScalar
issConfigSaveUserName = _IssConfigSaveUserName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 62),
    _IssConfigSaveUserName_Type()
)
issConfigSaveUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigSaveUserName.setStatus("current")


class _IssConfigSavePassword_Type(DisplayString):
    """Custom type issConfigSavePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IssConfigSavePassword_Type.__name__ = "DisplayString"
_IssConfigSavePassword_Object = MibScalar
issConfigSavePassword = _IssConfigSavePassword_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 63),
    _IssConfigSavePassword_Type()
)
issConfigSavePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigSavePassword.setStatus("current")


class _IssSwitchMinThresholdTemperature_Type(Integer32):
    """Custom type issSwitchMinThresholdTemperature based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 30),
    )


_IssSwitchMinThresholdTemperature_Type.__name__ = "Integer32"
_IssSwitchMinThresholdTemperature_Object = MibScalar
issSwitchMinThresholdTemperature = _IssSwitchMinThresholdTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 64),
    _IssSwitchMinThresholdTemperature_Type()
)
issSwitchMinThresholdTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issSwitchMinThresholdTemperature.setStatus("current")


class _IssSwitchMaxThresholdTemperature_Type(Integer32):
    """Custom type issSwitchMaxThresholdTemperature based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(35, 40),
    )


_IssSwitchMaxThresholdTemperature_Type.__name__ = "Integer32"
_IssSwitchMaxThresholdTemperature_Object = MibScalar
issSwitchMaxThresholdTemperature = _IssSwitchMaxThresholdTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 65),
    _IssSwitchMaxThresholdTemperature_Type()
)
issSwitchMaxThresholdTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issSwitchMaxThresholdTemperature.setStatus("current")
_IssSwitchCurrentTemperature_Type = Integer32
_IssSwitchCurrentTemperature_Object = MibScalar
issSwitchCurrentTemperature = _IssSwitchCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 66),
    _IssSwitchCurrentTemperature_Type()
)
issSwitchCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issSwitchCurrentTemperature.setStatus("current")


class _IssSwitchMaxCPUThreshold_Type(Integer32):
    """Custom type issSwitchMaxCPUThreshold based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IssSwitchMaxCPUThreshold_Type.__name__ = "Integer32"
_IssSwitchMaxCPUThreshold_Object = MibScalar
issSwitchMaxCPUThreshold = _IssSwitchMaxCPUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 67),
    _IssSwitchMaxCPUThreshold_Type()
)
issSwitchMaxCPUThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issSwitchMaxCPUThreshold.setStatus("current")
_IssSwitchCurrentCPUThreshold_Type = Integer32
_IssSwitchCurrentCPUThreshold_Object = MibScalar
issSwitchCurrentCPUThreshold = _IssSwitchCurrentCPUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 68),
    _IssSwitchCurrentCPUThreshold_Type()
)
issSwitchCurrentCPUThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issSwitchCurrentCPUThreshold.setStatus("current")


class _IssSwitchPowerSurge_Type(Integer32):
    """Custom type issSwitchPowerSurge based on Integer32"""
    defaultValue = 230

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IssSwitchPowerSurge_Type.__name__ = "Integer32"
_IssSwitchPowerSurge_Object = MibScalar
issSwitchPowerSurge = _IssSwitchPowerSurge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 69),
    _IssSwitchPowerSurge_Type()
)
issSwitchPowerSurge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issSwitchPowerSurge.setStatus("current")


class _IssSwitchPowerFailure_Type(Integer32):
    """Custom type issSwitchPowerFailure based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IssSwitchPowerFailure_Type.__name__ = "Integer32"
_IssSwitchPowerFailure_Object = MibScalar
issSwitchPowerFailure = _IssSwitchPowerFailure_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 70),
    _IssSwitchPowerFailure_Type()
)
issSwitchPowerFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issSwitchPowerFailure.setStatus("current")
_IssSwitchCurrentPowerSupply_Type = Integer32
_IssSwitchCurrentPowerSupply_Object = MibScalar
issSwitchCurrentPowerSupply = _IssSwitchCurrentPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 71),
    _IssSwitchCurrentPowerSupply_Type()
)
issSwitchCurrentPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issSwitchCurrentPowerSupply.setStatus("current")


class _IssSwitchMaxRAMUsage_Type(Integer32):
    """Custom type issSwitchMaxRAMUsage based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IssSwitchMaxRAMUsage_Type.__name__ = "Integer32"
_IssSwitchMaxRAMUsage_Object = MibScalar
issSwitchMaxRAMUsage = _IssSwitchMaxRAMUsage_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 72),
    _IssSwitchMaxRAMUsage_Type()
)
issSwitchMaxRAMUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issSwitchMaxRAMUsage.setStatus("current")
_IssSwitchCurrentRAMUsage_Type = Integer32
_IssSwitchCurrentRAMUsage_Object = MibScalar
issSwitchCurrentRAMUsage = _IssSwitchCurrentRAMUsage_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 73),
    _IssSwitchCurrentRAMUsage_Type()
)
issSwitchCurrentRAMUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issSwitchCurrentRAMUsage.setStatus("current")


class _IssSwitchMaxFlashUsage_Type(Integer32):
    """Custom type issSwitchMaxFlashUsage based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IssSwitchMaxFlashUsage_Type.__name__ = "Integer32"
_IssSwitchMaxFlashUsage_Object = MibScalar
issSwitchMaxFlashUsage = _IssSwitchMaxFlashUsage_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 74),
    _IssSwitchMaxFlashUsage_Type()
)
issSwitchMaxFlashUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issSwitchMaxFlashUsage.setStatus("current")
_IssSwitchCurrentFlashUsage_Type = Integer32
_IssSwitchCurrentFlashUsage_Object = MibScalar
issSwitchCurrentFlashUsage = _IssSwitchCurrentFlashUsage_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 75),
    _IssSwitchCurrentFlashUsage_Type()
)
issSwitchCurrentFlashUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issSwitchCurrentFlashUsage.setStatus("current")


class _IssConfigRestoreFileFormatVersion_Type(DisplayString):
    """Custom type issConfigRestoreFileFormatVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_IssConfigRestoreFileFormatVersion_Type.__name__ = "DisplayString"
_IssConfigRestoreFileFormatVersion_Object = MibScalar
issConfigRestoreFileFormatVersion = _IssConfigRestoreFileFormatVersion_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 76),
    _IssConfigRestoreFileFormatVersion_Type()
)
issConfigRestoreFileFormatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issConfigRestoreFileFormatVersion.setStatus("current")


class _IssDebugOption_Type(DisplayString):
    """Custom type issDebugOption based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 288),
    )


_IssDebugOption_Type.__name__ = "DisplayString"
_IssDebugOption_Object = MibScalar
issDebugOption = _IssDebugOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 77),
    _IssDebugOption_Type()
)
issDebugOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDebugOption.setStatus("current")


class _IssConfigDefaultValueSaveOption_Type(Integer32):
    """Custom type issConfigDefaultValueSaveOption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IssConfigDefaultValueSaveOption_Type.__name__ = "Integer32"
_IssConfigDefaultValueSaveOption_Object = MibScalar
issConfigDefaultValueSaveOption = _IssConfigDefaultValueSaveOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 78),
    _IssConfigDefaultValueSaveOption_Type()
)
issConfigDefaultValueSaveOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigDefaultValueSaveOption.setStatus("current")
_IssConfigSaveIpAddrType_Type = InetAddressType
_IssConfigSaveIpAddrType_Object = MibScalar
issConfigSaveIpAddrType = _IssConfigSaveIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 79),
    _IssConfigSaveIpAddrType_Type()
)
issConfigSaveIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigSaveIpAddrType.setStatus("current")
_IssConfigSaveIpvxAddr_Type = InetAddress
_IssConfigSaveIpvxAddr_Object = MibScalar
issConfigSaveIpvxAddr = _IssConfigSaveIpvxAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 80),
    _IssConfigSaveIpvxAddr_Type()
)
issConfigSaveIpvxAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigSaveIpvxAddr.setStatus("current")
_IssConfigRestoreIpAddrType_Type = InetAddressType
_IssConfigRestoreIpAddrType_Object = MibScalar
issConfigRestoreIpAddrType = _IssConfigRestoreIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 81),
    _IssConfigRestoreIpAddrType_Type()
)
issConfigRestoreIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigRestoreIpAddrType.setStatus("current")
_IssConfigRestoreIpvxAddr_Type = InetAddress
_IssConfigRestoreIpvxAddr_Object = MibScalar
issConfigRestoreIpvxAddr = _IssConfigRestoreIpvxAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 82),
    _IssConfigRestoreIpvxAddr_Type()
)
issConfigRestoreIpvxAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigRestoreIpvxAddr.setStatus("current")
_IssDlImageFromIpAddrType_Type = InetAddressType
_IssDlImageFromIpAddrType_Object = MibScalar
issDlImageFromIpAddrType = _IssDlImageFromIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 83),
    _IssDlImageFromIpAddrType_Type()
)
issDlImageFromIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDlImageFromIpAddrType.setStatus("current")
_IssDlImageFromIpvx_Type = InetAddress
_IssDlImageFromIpvx_Object = MibScalar
issDlImageFromIpvx = _IssDlImageFromIpvx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 84),
    _IssDlImageFromIpvx_Type()
)
issDlImageFromIpvx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDlImageFromIpvx.setStatus("current")
_IssUploadLogFileToIpAddrType_Type = InetAddressType
_IssUploadLogFileToIpAddrType_Object = MibScalar
issUploadLogFileToIpAddrType = _IssUploadLogFileToIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 85),
    _IssUploadLogFileToIpAddrType_Type()
)
issUploadLogFileToIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issUploadLogFileToIpAddrType.setStatus("current")
_IssUploadLogFileToIpvx_Type = InetAddress
_IssUploadLogFileToIpvx_Object = MibScalar
issUploadLogFileToIpvx = _IssUploadLogFileToIpvx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 86),
    _IssUploadLogFileToIpvx_Type()
)
issUploadLogFileToIpvx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issUploadLogFileToIpvx.setStatus("current")
_IssAuditLogRemoteIpAddrType_Type = InetAddressType
_IssAuditLogRemoteIpAddrType_Object = MibScalar
issAuditLogRemoteIpAddrType = _IssAuditLogRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 87),
    _IssAuditLogRemoteIpAddrType_Type()
)
issAuditLogRemoteIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issAuditLogRemoteIpAddrType.setStatus("current")
_IssAuditLogRemoteIpvxAddr_Type = InetAddress
_IssAuditLogRemoteIpvxAddr_Object = MibScalar
issAuditLogRemoteIpvxAddr = _IssAuditLogRemoteIpvxAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 88),
    _IssAuditLogRemoteIpvxAddr_Type()
)
issAuditLogRemoteIpvxAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issAuditLogRemoteIpvxAddr.setStatus("current")


class _IssSystemTimerSpeed_Type(Unsigned32):
    """Custom type issSystemTimerSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_IssSystemTimerSpeed_Type.__name__ = "Unsigned32"
_IssSystemTimerSpeed_Object = MibScalar
issSystemTimerSpeed = _IssSystemTimerSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 89),
    _IssSystemTimerSpeed_Type()
)
issSystemTimerSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issSystemTimerSpeed.setStatus("current")


class _IssMgmtInterfaceRouting_Type(Integer32):
    """Custom type issMgmtInterfaceRouting based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IssMgmtInterfaceRouting_Type.__name__ = "Integer32"
_IssMgmtInterfaceRouting_Object = MibScalar
issMgmtInterfaceRouting = _IssMgmtInterfaceRouting_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 90),
    _IssMgmtInterfaceRouting_Type()
)
issMgmtInterfaceRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMgmtInterfaceRouting.setStatus("current")


class _IssMacLearnRateLimit_Type(Integer32):
    """Custom type issMacLearnRateLimit based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IssMacLearnRateLimit_Type.__name__ = "Integer32"
_IssMacLearnRateLimit_Object = MibScalar
issMacLearnRateLimit = _IssMacLearnRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 91),
    _IssMacLearnRateLimit_Type()
)
issMacLearnRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMacLearnRateLimit.setStatus("current")


class _IssMacLearnRateLimitInterval_Type(Unsigned32):
    """Custom type issMacLearnRateLimitInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_IssMacLearnRateLimitInterval_Type.__name__ = "Unsigned32"
_IssMacLearnRateLimitInterval_Object = MibScalar
issMacLearnRateLimitInterval = _IssMacLearnRateLimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 92),
    _IssMacLearnRateLimitInterval_Type()
)
issMacLearnRateLimitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMacLearnRateLimitInterval.setStatus("current")
if mibBuilder.loadTexts:
    issMacLearnRateLimitInterval.setUnits("milliseconds")


class _IssVrfUnqMacFlag_Type(Integer32):
    """Custom type issVrfUnqMacFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IssVrfUnqMacFlag_Type.__name__ = "Integer32"
_IssVrfUnqMacFlag_Object = MibScalar
issVrfUnqMacFlag = _IssVrfUnqMacFlag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 93),
    _IssVrfUnqMacFlag_Type()
)
issVrfUnqMacFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issVrfUnqMacFlag.setStatus("current")


class _IssLoginAttempts_Type(Integer32):
    """Custom type issLoginAttempts based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IssLoginAttempts_Type.__name__ = "Integer32"
_IssLoginAttempts_Object = MibScalar
issLoginAttempts = _IssLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 94),
    _IssLoginAttempts_Type()
)
issLoginAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issLoginAttempts.setStatus("current")


class _IssLoginLockTime_Type(Integer32):
    """Custom type issLoginLockTime based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 900),
    )


_IssLoginLockTime_Type.__name__ = "Integer32"
_IssLoginLockTime_Object = MibScalar
issLoginLockTime = _IssLoginLockTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 95),
    _IssLoginLockTime_Type()
)
issLoginLockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issLoginLockTime.setStatus("current")


class _IssAuditLogSizeThreshold_Type(Unsigned32):
    """Custom type issAuditLogSizeThreshold based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_IssAuditLogSizeThreshold_Type.__name__ = "Unsigned32"
_IssAuditLogSizeThreshold_Object = MibScalar
issAuditLogSizeThreshold = _IssAuditLogSizeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 96),
    _IssAuditLogSizeThreshold_Type()
)
issAuditLogSizeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issAuditLogSizeThreshold.setStatus("current")


class _IssTelnetStatus_Type(Integer32):
    """Custom type issTelnetStatus based on Integer32"""
    defaultValue = 1

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
        *(("enable", 1),
          ("disable", 2),
          ("enableInProgress", 3),
          ("disableInProgress", 4))
    )


_IssTelnetStatus_Type.__name__ = "Integer32"
_IssTelnetStatus_Object = MibScalar
issTelnetStatus = _IssTelnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 97),
    _IssTelnetStatus_Type()
)
issTelnetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issTelnetStatus.setStatus("current")


class _IssWebSessionTimeOut_Type(Integer32):
    """Custom type issWebSessionTimeOut based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_IssWebSessionTimeOut_Type.__name__ = "Integer32"
_IssWebSessionTimeOut_Object = MibScalar
issWebSessionTimeOut = _IssWebSessionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 98),
    _IssWebSessionTimeOut_Type()
)
issWebSessionTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issWebSessionTimeOut.setStatus("current")


class _IssWebSessionMaxUsers_Type(Integer32):
    """Custom type issWebSessionMaxUsers based on Integer32"""
    defaultValue = 7


_IssWebSessionMaxUsers_Type.__name__ = "Integer32"
_IssWebSessionMaxUsers_Object = MibScalar
issWebSessionMaxUsers = _IssWebSessionMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 99),
    _IssWebSessionMaxUsers_Type()
)
issWebSessionMaxUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issWebSessionMaxUsers.setStatus("current")


class _IssHeartBeatMode_Type(Integer32):
    """Custom type issHeartBeatMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_IssHeartBeatMode_Type.__name__ = "Integer32"
_IssHeartBeatMode_Object = MibScalar
issHeartBeatMode = _IssHeartBeatMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 100),
    _IssHeartBeatMode_Type()
)
issHeartBeatMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issHeartBeatMode.setStatus("current")


class _IssRmRType_Type(Integer32):
    """Custom type issRmRType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hot", 1),
          ("cold", 2))
    )


_IssRmRType_Type.__name__ = "Integer32"
_IssRmRType_Object = MibScalar
issRmRType = _IssRmRType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 101),
    _IssRmRType_Type()
)
issRmRType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issRmRType.setStatus("current")


class _IssRmDType_Type(Integer32):
    """Custom type issRmDType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shared", 1),
          ("separate", 2))
    )


_IssRmDType_Type.__name__ = "Integer32"
_IssRmDType_Object = MibScalar
issRmDType = _IssRmDType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 102),
    _IssRmDType_Type()
)
issRmDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issRmDType.setStatus("current")


class _IssClearConfig_Type(TruthValue):
    """Custom type issClearConfig based on TruthValue"""
    defaultValue = 2


_IssClearConfig_Type.__name__ = "TruthValue"
_IssClearConfig_Object = MibScalar
issClearConfig = _IssClearConfig_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 103),
    _IssClearConfig_Type()
)
issClearConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issClearConfig.setStatus("current")


class _IssClearConfigFileName_Type(DisplayString):
    """Custom type issClearConfigFileName based on DisplayString"""
    defaultValue = OctetString("clear.conf")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_IssClearConfigFileName_Type.__name__ = "DisplayString"
_IssClearConfigFileName_Object = MibScalar
issClearConfigFileName = _IssClearConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 104),
    _IssClearConfigFileName_Type()
)
issClearConfigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issClearConfigFileName.setStatus("current")


class _IssTelnetClientStatus_Type(Integer32):
    """Custom type issTelnetClientStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IssTelnetClientStatus_Type.__name__ = "Integer32"
_IssTelnetClientStatus_Object = MibScalar
issTelnetClientStatus = _IssTelnetClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 105),
    _IssTelnetClientStatus_Type()
)
issTelnetClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issTelnetClientStatus.setStatus("current")


class _IssSshClientStatus_Type(Integer32):
    """Custom type issSshClientStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IssSshClientStatus_Type.__name__ = "Integer32"
_IssSshClientStatus_Object = MibScalar
issSshClientStatus = _IssSshClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 106),
    _IssSshClientStatus_Type()
)
issSshClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issSshClientStatus.setStatus("current")
_IssActiveTelnetClientSessions_Type = Integer32
_IssActiveTelnetClientSessions_Object = MibScalar
issActiveTelnetClientSessions = _IssActiveTelnetClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 107),
    _IssActiveTelnetClientSessions_Type()
)
issActiveTelnetClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issActiveTelnetClientSessions.setStatus("current")
_IssActiveSshClientSessions_Type = Integer32
_IssActiveSshClientSessions_Object = MibScalar
issActiveSshClientSessions = _IssActiveSshClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 108),
    _IssActiveSshClientSessions_Type()
)
issActiveSshClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issActiveSshClientSessions.setStatus("current")


class _IssLogFileSize_Type(Unsigned32):
    """Custom type issLogFileSize based on Unsigned32"""
    defaultValue = 1048576


_IssLogFileSize_Type.__name__ = "Unsigned32"
_IssLogFileSize_Object = MibScalar
issLogFileSize = _IssLogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 109),
    _IssLogFileSize_Type()
)
issLogFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issLogFileSize.setStatus("current")


class _IssLogReset_Type(TruthValue):
    """Custom type issLogReset based on TruthValue"""
    defaultValue = 2


_IssLogReset_Type.__name__ = "TruthValue"
_IssLogReset_Object = MibScalar
issLogReset = _IssLogReset_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 110),
    _IssLogReset_Type()
)
issLogReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issLogReset.setStatus("current")


class _IssLogSizeThreshold_Type(Unsigned32):
    """Custom type issLogSizeThreshold based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_IssLogSizeThreshold_Type.__name__ = "Unsigned32"
_IssLogSizeThreshold_Object = MibScalar
issLogSizeThreshold = _IssLogSizeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 111),
    _IssLogSizeThreshold_Type()
)
issLogSizeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issLogSizeThreshold.setStatus("current")


class _IssAutomaticPortCreate_Type(Integer32):
    """Custom type issAutomaticPortCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IssAutomaticPortCreate_Type.__name__ = "Integer32"
_IssAutomaticPortCreate_Object = MibScalar
issAutomaticPortCreate = _IssAutomaticPortCreate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 112),
    _IssAutomaticPortCreate_Type()
)
issAutomaticPortCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issAutomaticPortCreate.setStatus("current")


class _IssUlRemoteLogFileName_Type(DisplayString):
    """Custom type issUlRemoteLogFileName based on DisplayString"""
    defaultValue = OctetString("iss.log")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_IssUlRemoteLogFileName_Type.__name__ = "DisplayString"
_IssUlRemoteLogFileName_Object = MibScalar
issUlRemoteLogFileName = _IssUlRemoteLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 113),
    _IssUlRemoteLogFileName_Type()
)
issUlRemoteLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issUlRemoteLogFileName.setStatus("current")
_IssDefaultExecTimeOut_Type = Unsigned32
_IssDefaultExecTimeOut_Object = MibScalar
issDefaultExecTimeOut = _IssDefaultExecTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 114),
    _IssDefaultExecTimeOut_Type()
)
issDefaultExecTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDefaultExecTimeOut.setStatus("current")


class _IssRmStackingInterfaceType_Type(Integer32):
    """Custom type issRmStackingInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oob", 1),
          ("inband", 2))
    )


_IssRmStackingInterfaceType_Type.__name__ = "Integer32"
_IssRmStackingInterfaceType_Object = MibScalar
issRmStackingInterfaceType = _IssRmStackingInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 115),
    _IssRmStackingInterfaceType_Type()
)
issRmStackingInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issRmStackingInterfaceType.setStatus("current")


class _IssPeerLoggingOption_Type(Integer32):
    """Custom type issPeerLoggingOption based on Integer32"""
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
        *(("console", 1),
          ("file", 2),
          ("flash", 3))
    )


_IssPeerLoggingOption_Type.__name__ = "Integer32"
_IssPeerLoggingOption_Object = MibScalar
issPeerLoggingOption = _IssPeerLoggingOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 116),
    _IssPeerLoggingOption_Type()
)
issPeerLoggingOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPeerLoggingOption.setStatus("current")


class _IssStandbyRestart_Type(TruthValue):
    """Custom type issStandbyRestart based on TruthValue"""
    defaultValue = 2


_IssStandbyRestart_Type.__name__ = "TruthValue"
_IssStandbyRestart_Object = MibScalar
issStandbyRestart = _IssStandbyRestart_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 117),
    _IssStandbyRestart_Type()
)
issStandbyRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issStandbyRestart.setStatus("current")


class _IssRestoreType_Type(Integer32):
    """Custom type issRestoreType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("msr", 1),
          ("csr", 2))
    )


_IssRestoreType_Type.__name__ = "Integer32"
_IssRestoreType_Object = MibScalar
issRestoreType = _IssRestoreType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 118),
    _IssRestoreType_Type()
)
issRestoreType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issRestoreType.setStatus("current")


class _IssSwitchModeType_Type(Integer32):
    """Custom type issSwitchModeType based on Integer32"""
    defaultValue = 2

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
        *(("cutThroughSameSpeed", 1),
          ("storeForward", 2),
          ("cutThroughSlowToFast", 3),
          ("cutThroughFastToSlow", 4))
    )


_IssSwitchModeType_Type.__name__ = "Integer32"
_IssSwitchModeType_Object = MibScalar
issSwitchModeType = _IssSwitchModeType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 119),
    _IssSwitchModeType_Type()
)
issSwitchModeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issSwitchModeType.setStatus("current")


class _IssConfigRestoreRetries_Type(Integer32):
    """Custom type issConfigRestoreRetries based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IssConfigRestoreRetries_Type.__name__ = "Integer32"
_IssConfigRestoreRetries_Object = MibScalar
issConfigRestoreRetries = _IssConfigRestoreRetries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 120),
    _IssConfigRestoreRetries_Type()
)
issConfigRestoreRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigRestoreRetries.setStatus("current")


class _IssPauseFloodSamplingInterval_Type(Unsigned32):
    """Custom type issPauseFloodSamplingInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_IssPauseFloodSamplingInterval_Type.__name__ = "Unsigned32"
_IssPauseFloodSamplingInterval_Object = MibScalar
issPauseFloodSamplingInterval = _IssPauseFloodSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 121),
    _IssPauseFloodSamplingInterval_Type()
)
issPauseFloodSamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPauseFloodSamplingInterval.setStatus("current")
if mibBuilder.loadTexts:
    issPauseFloodSamplingInterval.setUnits("seconds")


class _IssPauseFloodProtect_Type(Integer32):
    """Custom type issPauseFloodProtect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IssPauseFloodProtect_Type.__name__ = "Integer32"
_IssPauseFloodProtect_Object = MibScalar
issPauseFloodProtect = _IssPauseFloodProtect_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 122),
    _IssPauseFloodProtect_Type()
)
issPauseFloodProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPauseFloodProtect.setStatus("current")


class _IssPauseFloodMode_Type(Integer32):
    """Custom type issPauseFloodMode based on Integer32"""
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
        *(("disabled", 1),
          ("detectionOnly", 2),
          ("enabled", 3))
    )


_IssPauseFloodMode_Type.__name__ = "Integer32"
_IssPauseFloodMode_Object = MibScalar
issPauseFloodMode = _IssPauseFloodMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 123),
    _IssPauseFloodMode_Type()
)
issPauseFloodMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPauseFloodMode.setStatus("current")


class _IssPauseFloodReset_Type(TruthValue):
    """Custom type issPauseFloodReset based on TruthValue"""
    defaultValue = 2


_IssPauseFloodReset_Type.__name__ = "TruthValue"
_IssPauseFloodReset_Object = MibScalar
issPauseFloodReset = _IssPauseFloodReset_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 124),
    _IssPauseFloodReset_Type()
)
issPauseFloodReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPauseFloodReset.setStatus("current")


class _IssPauseFloodTraceSeverityLevel_Type(Integer32):
    """Custom type issPauseFloodTraceSeverityLevel based on Integer32"""
    defaultValue = 4

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
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("informational", 6),
          ("debug", 7))
    )


_IssPauseFloodTraceSeverityLevel_Type.__name__ = "Integer32"
_IssPauseFloodTraceSeverityLevel_Object = MibScalar
issPauseFloodTraceSeverityLevel = _IssPauseFloodTraceSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 125),
    _IssPauseFloodTraceSeverityLevel_Type()
)
issPauseFloodTraceSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPauseFloodTraceSeverityLevel.setStatus("current")


class _IssPauseFloodTraceOption_Type(Integer32):
    """Custom type issPauseFloodTraceOption based on Integer32"""
    defaultValue = 0


_IssPauseFloodTraceOption_Type.__name__ = "Integer32"
_IssPauseFloodTraceOption_Object = MibScalar
issPauseFloodTraceOption = _IssPauseFloodTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 126),
    _IssPauseFloodTraceOption_Type()
)
issPauseFloodTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPauseFloodTraceOption.setStatus("current")
_IssPortsSwitchingModeStatus_Type = PortList
_IssPortsSwitchingModeStatus_Object = MibScalar
issPortsSwitchingModeStatus = _IssPortsSwitchingModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 127),
    _IssPortsSwitchingModeStatus_Type()
)
issPortsSwitchingModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issPortsSwitchingModeStatus.setStatus("current")


class _IssDebugTimeStampOption_Type(Integer32):
    """Custom type issDebugTimeStampOption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IssDebugTimeStampOption_Type.__name__ = "Integer32"
_IssDebugTimeStampOption_Object = MibScalar
issDebugTimeStampOption = _IssDebugTimeStampOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 128),
    _IssDebugTimeStampOption_Type()
)
issDebugTimeStampOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDebugTimeStampOption.setStatus("current")


class _IssLdapLoginPrivilege_Type(Integer32):
    """Custom type issLdapLoginPrivilege based on Integer32"""
    defaultValue = 0


_IssLdapLoginPrivilege_Type.__name__ = "Integer32"
_IssLdapLoginPrivilege_Object = MibScalar
issLdapLoginPrivilege = _IssLdapLoginPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 129),
    _IssLdapLoginPrivilege_Type()
)
issLdapLoginPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issLdapLoginPrivilege.setStatus("current")


class _IssLdapAttributeName_Type(OctetString):
    """Custom type issLdapAttributeName based on OctetString"""
    defaultValue = OctetString("")


_IssLdapAttributeName_Type.__name__ = "OctetString"
_IssLdapAttributeName_Object = MibScalar
issLdapAttributeName = _IssLdapAttributeName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 130),
    _IssLdapAttributeName_Type()
)
issLdapAttributeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issLdapAttributeName.setStatus("current")


class _IssConfigRestoreFileSkuManifest_Type(OctetString):
    """Custom type issConfigRestoreFileSkuManifest based on OctetString"""
    defaultValue = OctetString("")


_IssConfigRestoreFileSkuManifest_Type.__name__ = "OctetString"
_IssConfigRestoreFileSkuManifest_Object = MibScalar
issConfigRestoreFileSkuManifest = _IssConfigRestoreFileSkuManifest_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 131),
    _IssConfigRestoreFileSkuManifest_Type()
)
issConfigRestoreFileSkuManifest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issConfigRestoreFileSkuManifest.setStatus("current")


class _IssDlImageType_Type(Integer32):
    """Custom type issDlImageType based on Integer32"""
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
        *(("agent", 1),
          ("diagnostic", 2),
          ("firmware-cpld", 3))
    )


_IssDlImageType_Type.__name__ = "Integer32"
_IssDlImageType_Object = MibScalar
issDlImageType = _IssDlImageType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 132),
    _IssDlImageType_Type()
)
issDlImageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issDlImageType.setStatus("current")


class _IssFirmwareCpldVersion_Type(OctetString):
    """Custom type issFirmwareCpldVersion based on OctetString"""
    defaultValue = OctetString("")


_IssFirmwareCpldVersion_Type.__name__ = "OctetString"
_IssFirmwareCpldVersion_Object = MibScalar
issFirmwareCpldVersion = _IssFirmwareCpldVersion_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 133),
    _IssFirmwareCpldVersion_Type()
)
issFirmwareCpldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issFirmwareCpldVersion.setStatus("current")


class _IssHttpMaxSessions_Type(Integer32):
    """Custom type issHttpMaxSessions based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IssHttpMaxSessions_Type.__name__ = "Integer32"
_IssHttpMaxSessions_Object = MibScalar
issHttpMaxSessions = _IssHttpMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 1, 134),
    _IssHttpMaxSessions_Type()
)
issHttpMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issHttpMaxSessions.setStatus("current")
_IssConfigControl_ObjectIdentity = ObjectIdentity
issConfigControl = _IssConfigControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2)
)
_IssConfigCtrlTable_Object = MibTable
issConfigCtrlTable = _IssConfigCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 1)
)
if mibBuilder.loadTexts:
    issConfigCtrlTable.setStatus("current")
_IssConfigCtrlEntry_Object = MibTableRow
issConfigCtrlEntry = _IssConfigCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 1, 1)
)
issConfigCtrlEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issConfigCtrlIndex"),
)
if mibBuilder.loadTexts:
    issConfigCtrlEntry.setStatus("current")


class _IssConfigCtrlIndex_Type(Integer32):
    """Custom type issConfigCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IssConfigCtrlIndex_Type.__name__ = "Integer32"
_IssConfigCtrlIndex_Object = MibTableColumn
issConfigCtrlIndex = _IssConfigCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 1, 1, 1),
    _IssConfigCtrlIndex_Type()
)
issConfigCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issConfigCtrlIndex.setStatus("current")


class _IssConfigCtrlEgressStatus_Type(Integer32):
    """Custom type issConfigCtrlEgressStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IssConfigCtrlEgressStatus_Type.__name__ = "Integer32"
_IssConfigCtrlEgressStatus_Object = MibTableColumn
issConfigCtrlEgressStatus = _IssConfigCtrlEgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 1, 1, 2),
    _IssConfigCtrlEgressStatus_Type()
)
issConfigCtrlEgressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigCtrlEgressStatus.setStatus("current")


class _IssConfigCtrlStatsCollection_Type(Integer32):
    """Custom type issConfigCtrlStatsCollection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IssConfigCtrlStatsCollection_Type.__name__ = "Integer32"
_IssConfigCtrlStatsCollection_Object = MibTableColumn
issConfigCtrlStatsCollection = _IssConfigCtrlStatsCollection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 1, 1, 3),
    _IssConfigCtrlStatsCollection_Type()
)
issConfigCtrlStatsCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigCtrlStatsCollection.setStatus("current")


class _IssConfigCtrlStatus_Type(Integer32):
    """Custom type issConfigCtrlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_IssConfigCtrlStatus_Type.__name__ = "Integer32"
_IssConfigCtrlStatus_Object = MibTableColumn
issConfigCtrlStatus = _IssConfigCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 1, 1, 4),
    _IssConfigCtrlStatus_Type()
)
issConfigCtrlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issConfigCtrlStatus.setStatus("current")
_IssPortCtrlTable_Object = MibTable
issPortCtrlTable = _IssPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2)
)
if mibBuilder.loadTexts:
    issPortCtrlTable.setStatus("current")
_IssPortCtrlEntry_Object = MibTableRow
issPortCtrlEntry = _IssPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1)
)
issPortCtrlEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issPortCtrlIndex"),
)
if mibBuilder.loadTexts:
    issPortCtrlEntry.setStatus("current")


class _IssPortCtrlIndex_Type(Integer32):
    """Custom type issPortCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IssPortCtrlIndex_Type.__name__ = "Integer32"
_IssPortCtrlIndex_Object = MibTableColumn
issPortCtrlIndex = _IssPortCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 1),
    _IssPortCtrlIndex_Type()
)
issPortCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issPortCtrlIndex.setStatus("current")


class _IssPortCtrlMode_Type(Integer32):
    """Custom type issPortCtrlMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("noNegotiation", 2))
    )


_IssPortCtrlMode_Type.__name__ = "Integer32"
_IssPortCtrlMode_Object = MibTableColumn
issPortCtrlMode = _IssPortCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 2),
    _IssPortCtrlMode_Type()
)
issPortCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlMode.setStatus("current")


class _IssPortCtrlDuplex_Type(Integer32):
    """Custom type issPortCtrlDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_IssPortCtrlDuplex_Type.__name__ = "Integer32"
_IssPortCtrlDuplex_Object = MibTableColumn
issPortCtrlDuplex = _IssPortCtrlDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 3),
    _IssPortCtrlDuplex_Type()
)
issPortCtrlDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlDuplex.setStatus("current")


class _IssPortCtrlSpeed_Type(Integer32):
    """Custom type issPortCtrlSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("tenMBPS", 1),
          ("hundredMBPS", 2),
          ("oneGB", 3),
          ("tenGB", 4),
          ("fortyGB", 5),
          ("fiftyGB", 6),
          ("twothousandfivehundredMBPS", 7),
          ("twentyfiveGB", 8),
          ("onehundredGB", 9))
    )


_IssPortCtrlSpeed_Type.__name__ = "Integer32"
_IssPortCtrlSpeed_Object = MibTableColumn
issPortCtrlSpeed = _IssPortCtrlSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 4),
    _IssPortCtrlSpeed_Type()
)
issPortCtrlSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlSpeed.setStatus("current")


class _IssPortCtrlFlowControl_Type(Integer32):
    """Custom type issPortCtrlFlowControl based on Integer32"""
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


_IssPortCtrlFlowControl_Type.__name__ = "Integer32"
_IssPortCtrlFlowControl_Object = MibTableColumn
issPortCtrlFlowControl = _IssPortCtrlFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 5),
    _IssPortCtrlFlowControl_Type()
)
issPortCtrlFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlFlowControl.setStatus("deprecated")


class _IssPortCtrlRenegotiate_Type(TruthValue):
    """Custom type issPortCtrlRenegotiate based on TruthValue"""
    defaultValue = 2


_IssPortCtrlRenegotiate_Type.__name__ = "TruthValue"
_IssPortCtrlRenegotiate_Object = MibTableColumn
issPortCtrlRenegotiate = _IssPortCtrlRenegotiate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 6),
    _IssPortCtrlRenegotiate_Type()
)
issPortCtrlRenegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlRenegotiate.setStatus("current")
_IssPortCtrlMaxMacAddr_Type = Integer32
_IssPortCtrlMaxMacAddr_Object = MibTableColumn
issPortCtrlMaxMacAddr = _IssPortCtrlMaxMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 7),
    _IssPortCtrlMaxMacAddr_Type()
)
issPortCtrlMaxMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlMaxMacAddr.setStatus("current")


class _IssPortCtrlMaxMacAction_Type(Integer32):
    """Custom type issPortCtrlMaxMacAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("purgeLRU", 2))
    )


_IssPortCtrlMaxMacAction_Type.__name__ = "Integer32"
_IssPortCtrlMaxMacAction_Object = MibTableColumn
issPortCtrlMaxMacAction = _IssPortCtrlMaxMacAction_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 8),
    _IssPortCtrlMaxMacAction_Type()
)
issPortCtrlMaxMacAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlMaxMacAction.setStatus("current")


class _IssPortHOLBlockPrevention_Type(Integer32):
    """Custom type issPortHOLBlockPrevention based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IssPortHOLBlockPrevention_Type.__name__ = "Integer32"
_IssPortHOLBlockPrevention_Object = MibTableColumn
issPortHOLBlockPrevention = _IssPortHOLBlockPrevention_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 9),
    _IssPortHOLBlockPrevention_Type()
)
issPortHOLBlockPrevention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortHOLBlockPrevention.setStatus("current")
_IssPortAutoNegAdvtCapBits_Type = OctetString
_IssPortAutoNegAdvtCapBits_Object = MibTableColumn
issPortAutoNegAdvtCapBits = _IssPortAutoNegAdvtCapBits_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 10),
    _IssPortAutoNegAdvtCapBits_Type()
)
issPortAutoNegAdvtCapBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortAutoNegAdvtCapBits.setStatus("current")


class _IssPortCpuControlledLearning_Type(Integer32):
    """Custom type issPortCpuControlledLearning based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IssPortCpuControlledLearning_Type.__name__ = "Integer32"
_IssPortCpuControlledLearning_Object = MibTableColumn
issPortCpuControlledLearning = _IssPortCpuControlledLearning_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 11),
    _IssPortCpuControlledLearning_Type()
)
issPortCpuControlledLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCpuControlledLearning.setStatus("current")


class _IssPortMdiOrMdixCap_Type(Integer32):
    """Custom type issPortMdiOrMdixCap based on Integer32"""
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
        *(("auto", 1),
          ("mdi", 2),
          ("mdix", 3))
    )


_IssPortMdiOrMdixCap_Type.__name__ = "Integer32"
_IssPortMdiOrMdixCap_Object = MibTableColumn
issPortMdiOrMdixCap = _IssPortMdiOrMdixCap_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 12),
    _IssPortMdiOrMdixCap_Type()
)
issPortMdiOrMdixCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortMdiOrMdixCap.setStatus("current")


class _IssPortCtrlFlowControlMaxRate_Type(Integer32):
    """Custom type issPortCtrlFlowControlMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80000000),
    )


_IssPortCtrlFlowControlMaxRate_Type.__name__ = "Integer32"
_IssPortCtrlFlowControlMaxRate_Object = MibTableColumn
issPortCtrlFlowControlMaxRate = _IssPortCtrlFlowControlMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 13),
    _IssPortCtrlFlowControlMaxRate_Type()
)
issPortCtrlFlowControlMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlFlowControlMaxRate.setStatus("current")


class _IssPortCtrlFlowControlMinRate_Type(Integer32):
    """Custom type issPortCtrlFlowControlMinRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80000000),
    )


_IssPortCtrlFlowControlMinRate_Type.__name__ = "Integer32"
_IssPortCtrlFlowControlMinRate_Object = MibTableColumn
issPortCtrlFlowControlMinRate = _IssPortCtrlFlowControlMinRate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 14),
    _IssPortCtrlFlowControlMinRate_Type()
)
issPortCtrlFlowControlMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlFlowControlMinRate.setStatus("current")


class _IssPortCtrlPauseFloodProtect_Type(Integer32):
    """Custom type issPortCtrlPauseFloodProtect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IssPortCtrlPauseFloodProtect_Type.__name__ = "Integer32"
_IssPortCtrlPauseFloodProtect_Object = MibTableColumn
issPortCtrlPauseFloodProtect = _IssPortCtrlPauseFloodProtect_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 15),
    _IssPortCtrlPauseFloodProtect_Type()
)
issPortCtrlPauseFloodProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlPauseFloodProtect.setStatus("current")


class _IssPortCtrlPauseFloodMode_Type(Integer32):
    """Custom type issPortCtrlPauseFloodMode based on Integer32"""
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
        *(("disabled", 1),
          ("detectionOnly", 2),
          ("enabled", 3))
    )


_IssPortCtrlPauseFloodMode_Type.__name__ = "Integer32"
_IssPortCtrlPauseFloodMode_Object = MibTableColumn
issPortCtrlPauseFloodMode = _IssPortCtrlPauseFloodMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 16),
    _IssPortCtrlPauseFloodMode_Type()
)
issPortCtrlPauseFloodMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlPauseFloodMode.setStatus("current")


class _IssPortCtrlPauseFloodStatus_Type(Integer32):
    """Custom type issPortCtrlPauseFloodStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("detected", 2),
          ("blocked", 3))
    )


_IssPortCtrlPauseFloodStatus_Type.__name__ = "Integer32"
_IssPortCtrlPauseFloodStatus_Object = MibTableColumn
issPortCtrlPauseFloodStatus = _IssPortCtrlPauseFloodStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 17),
    _IssPortCtrlPauseFloodStatus_Type()
)
issPortCtrlPauseFloodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issPortCtrlPauseFloodStatus.setStatus("current")


class _IssPortCtrlPauseFloodReset_Type(TruthValue):
    """Custom type issPortCtrlPauseFloodReset based on TruthValue"""
    defaultValue = 2


_IssPortCtrlPauseFloodReset_Type.__name__ = "TruthValue"
_IssPortCtrlPauseFloodReset_Object = MibTableColumn
issPortCtrlPauseFloodReset = _IssPortCtrlPauseFloodReset_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 18),
    _IssPortCtrlPauseFloodReset_Type()
)
issPortCtrlPauseFloodReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlPauseFloodReset.setStatus("current")
_IssPortCtrlPauseFloodStats_Type = Unsigned32
_IssPortCtrlPauseFloodStats_Object = MibTableColumn
issPortCtrlPauseFloodStats = _IssPortCtrlPauseFloodStats_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 19),
    _IssPortCtrlPauseFloodStats_Type()
)
issPortCtrlPauseFloodStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issPortCtrlPauseFloodStats.setStatus("current")


class _IssPortCtrlPauseFloodStatsClear_Type(TruthValue):
    """Custom type issPortCtrlPauseFloodStatsClear based on TruthValue"""
    defaultValue = 2


_IssPortCtrlPauseFloodStatsClear_Type.__name__ = "TruthValue"
_IssPortCtrlPauseFloodStatsClear_Object = MibTableColumn
issPortCtrlPauseFloodStatsClear = _IssPortCtrlPauseFloodStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 20),
    _IssPortCtrlPauseFloodStatsClear_Type()
)
issPortCtrlPauseFloodStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlPauseFloodStatsClear.setStatus("current")


class _IssPortCtrlPauseFloodTraceOption_Type(Integer32):
    """Custom type issPortCtrlPauseFloodTraceOption based on Integer32"""
    defaultValue = 0


_IssPortCtrlPauseFloodTraceOption_Type.__name__ = "Integer32"
_IssPortCtrlPauseFloodTraceOption_Object = MibTableColumn
issPortCtrlPauseFloodTraceOption = _IssPortCtrlPauseFloodTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 21),
    _IssPortCtrlPauseFloodTraceOption_Type()
)
issPortCtrlPauseFloodTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlPauseFloodTraceOption.setStatus("current")


class _IssPortCtrlSwitchModeType_Type(Integer32):
    """Custom type issPortCtrlSwitchModeType based on Integer32"""
    defaultValue = 2

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
        *(("cutThroughSameSpeed", 1),
          ("storeForward", 2),
          ("cutThroughSlowToFast", 3),
          ("cutThroughFastToSlow", 4))
    )


_IssPortCtrlSwitchModeType_Type.__name__ = "Integer32"
_IssPortCtrlSwitchModeType_Object = MibTableColumn
issPortCtrlSwitchModeType = _IssPortCtrlSwitchModeType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 22),
    _IssPortCtrlSwitchModeType_Type()
)
issPortCtrlSwitchModeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlSwitchModeType.setStatus("current")


class _IssPortCtrlSwitchModeStatus_Type(Integer32):
    """Custom type issPortCtrlSwitchModeStatus based on Integer32"""
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
        *(("cutThroughSameSpeed", 1),
          ("storeForward", 2),
          ("cutThroughSlowToFast", 3),
          ("cutThroughFastToSlow", 4))
    )


_IssPortCtrlSwitchModeStatus_Type.__name__ = "Integer32"
_IssPortCtrlSwitchModeStatus_Object = MibTableColumn
issPortCtrlSwitchModeStatus = _IssPortCtrlSwitchModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 23),
    _IssPortCtrlSwitchModeStatus_Type()
)
issPortCtrlSwitchModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issPortCtrlSwitchModeStatus.setStatus("current")


class _IssPortCtrlInbandAutoNeg_Type(Integer32):
    """Custom type issPortCtrlInbandAutoNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_IssPortCtrlInbandAutoNeg_Type.__name__ = "Integer32"
_IssPortCtrlInbandAutoNeg_Object = MibTableColumn
issPortCtrlInbandAutoNeg = _IssPortCtrlInbandAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 24),
    _IssPortCtrlInbandAutoNeg_Type()
)
issPortCtrlInbandAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlInbandAutoNeg.setStatus("current")


class _IssPortCtrlBypassInbandAutoNeg_Type(Integer32):
    """Custom type issPortCtrlBypassInbandAutoNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_IssPortCtrlBypassInbandAutoNeg_Type.__name__ = "Integer32"
_IssPortCtrlBypassInbandAutoNeg_Object = MibTableColumn
issPortCtrlBypassInbandAutoNeg = _IssPortCtrlBypassInbandAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 25),
    _IssPortCtrlBypassInbandAutoNeg_Type()
)
issPortCtrlBypassInbandAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlBypassInbandAutoNeg.setStatus("current")


class _IssPortCtrlForceSpeed_Type(Integer32):
    """Custom type issPortCtrlForceSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_IssPortCtrlForceSpeed_Type.__name__ = "Integer32"
_IssPortCtrlForceSpeed_Object = MibTableColumn
issPortCtrlForceSpeed = _IssPortCtrlForceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 2, 1, 26),
    _IssPortCtrlForceSpeed_Type()
)
issPortCtrlForceSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issPortCtrlForceSpeed.setStatus("current")
_IssPortIsolationTable_Object = MibTable
issPortIsolationTable = _IssPortIsolationTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 3)
)
if mibBuilder.loadTexts:
    issPortIsolationTable.setStatus("current")
_IssPortIsolationEntry_Object = MibTableRow
issPortIsolationEntry = _IssPortIsolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 3, 1)
)
issPortIsolationEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issPortIsolationIngressPort"),
    (0, "ARICENT-ISS-MIB", "issPortIsolationInVlanId"),
    (0, "ARICENT-ISS-MIB", "issPortIsolationEgressPort"),
)
if mibBuilder.loadTexts:
    issPortIsolationEntry.setStatus("current")
_IssPortIsolationIngressPort_Type = InterfaceIndex
_IssPortIsolationIngressPort_Object = MibTableColumn
issPortIsolationIngressPort = _IssPortIsolationIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 3, 1, 1),
    _IssPortIsolationIngressPort_Type()
)
issPortIsolationIngressPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issPortIsolationIngressPort.setStatus("current")


class _IssPortIsolationInVlanId_Type(Integer32):
    """Custom type issPortIsolationInVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_IssPortIsolationInVlanId_Type.__name__ = "Integer32"
_IssPortIsolationInVlanId_Object = MibTableColumn
issPortIsolationInVlanId = _IssPortIsolationInVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 3, 1, 2),
    _IssPortIsolationInVlanId_Type()
)
issPortIsolationInVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issPortIsolationInVlanId.setStatus("current")
_IssPortIsolationEgressPort_Type = InterfaceIndex
_IssPortIsolationEgressPort_Object = MibTableColumn
issPortIsolationEgressPort = _IssPortIsolationEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 3, 1, 3),
    _IssPortIsolationEgressPort_Type()
)
issPortIsolationEgressPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issPortIsolationEgressPort.setStatus("current")
_IssPortIsolationStorageType_Type = StorageType
_IssPortIsolationStorageType_Object = MibTableColumn
issPortIsolationStorageType = _IssPortIsolationStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 3, 1, 4),
    _IssPortIsolationStorageType_Type()
)
issPortIsolationStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issPortIsolationStorageType.setStatus("current")
_IssPortIsolationRowStatus_Type = RowStatus
_IssPortIsolationRowStatus_Object = MibTableColumn
issPortIsolationRowStatus = _IssPortIsolationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 2, 3, 1, 5),
    _IssPortIsolationRowStatus_Type()
)
issPortIsolationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issPortIsolationRowStatus.setStatus("current")
_IssMirror_ObjectIdentity = ObjectIdentity
issMirror = _IssMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3)
)


class _IssMirrorStatus_Type(Integer32):
    """Custom type issMirrorStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IssMirrorStatus_Type.__name__ = "Integer32"
_IssMirrorStatus_Object = MibScalar
issMirrorStatus = _IssMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 1),
    _IssMirrorStatus_Type()
)
issMirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMirrorStatus.setStatus("current")
_IssMirrorToPort_Type = Integer32
_IssMirrorToPort_Object = MibScalar
issMirrorToPort = _IssMirrorToPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 2),
    _IssMirrorToPort_Type()
)
issMirrorToPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMirrorToPort.setStatus("current")
_IssMirrorCtrlTable_Object = MibTable
issMirrorCtrlTable = _IssMirrorCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 3)
)
if mibBuilder.loadTexts:
    issMirrorCtrlTable.setStatus("current")
_IssMirrorCtrlEntry_Object = MibTableRow
issMirrorCtrlEntry = _IssMirrorCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 3, 1)
)
issMirrorCtrlEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issMirrorCtrlIndex"),
)
if mibBuilder.loadTexts:
    issMirrorCtrlEntry.setStatus("current")


class _IssMirrorCtrlIndex_Type(Integer32):
    """Custom type issMirrorCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IssMirrorCtrlIndex_Type.__name__ = "Integer32"
_IssMirrorCtrlIndex_Object = MibTableColumn
issMirrorCtrlIndex = _IssMirrorCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 3, 1, 1),
    _IssMirrorCtrlIndex_Type()
)
issMirrorCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issMirrorCtrlIndex.setStatus("current")


class _IssMirrorCtrlIngressMirroring_Type(Integer32):
    """Custom type issMirrorCtrlIngressMirroring based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IssMirrorCtrlIngressMirroring_Type.__name__ = "Integer32"
_IssMirrorCtrlIngressMirroring_Object = MibTableColumn
issMirrorCtrlIngressMirroring = _IssMirrorCtrlIngressMirroring_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 3, 1, 2),
    _IssMirrorCtrlIngressMirroring_Type()
)
issMirrorCtrlIngressMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMirrorCtrlIngressMirroring.setStatus("current")


class _IssMirrorCtrlEgressMirroring_Type(Integer32):
    """Custom type issMirrorCtrlEgressMirroring based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IssMirrorCtrlEgressMirroring_Type.__name__ = "Integer32"
_IssMirrorCtrlEgressMirroring_Object = MibTableColumn
issMirrorCtrlEgressMirroring = _IssMirrorCtrlEgressMirroring_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 3, 1, 3),
    _IssMirrorCtrlEgressMirroring_Type()
)
issMirrorCtrlEgressMirroring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMirrorCtrlEgressMirroring.setStatus("current")


class _IssMirrorCtrlStatus_Type(Integer32):
    """Custom type issMirrorCtrlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_IssMirrorCtrlStatus_Type.__name__ = "Integer32"
_IssMirrorCtrlStatus_Object = MibTableColumn
issMirrorCtrlStatus = _IssMirrorCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 3, 1, 4),
    _IssMirrorCtrlStatus_Type()
)
issMirrorCtrlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMirrorCtrlStatus.setStatus("current")
_IssMirrorCtrlRemainingSrcRcrds_Type = Integer32
_IssMirrorCtrlRemainingSrcRcrds_Object = MibScalar
issMirrorCtrlRemainingSrcRcrds = _IssMirrorCtrlRemainingSrcRcrds_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 4),
    _IssMirrorCtrlRemainingSrcRcrds_Type()
)
issMirrorCtrlRemainingSrcRcrds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issMirrorCtrlRemainingSrcRcrds.setStatus("current")
_IssMirrorCtrlRemainingDestRcrds_Type = Integer32
_IssMirrorCtrlRemainingDestRcrds_Object = MibScalar
issMirrorCtrlRemainingDestRcrds = _IssMirrorCtrlRemainingDestRcrds_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 5),
    _IssMirrorCtrlRemainingDestRcrds_Type()
)
issMirrorCtrlRemainingDestRcrds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issMirrorCtrlRemainingDestRcrds.setStatus("current")
_IssMirrorCtrlExtnTable_Object = MibTable
issMirrorCtrlExtnTable = _IssMirrorCtrlExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 6)
)
if mibBuilder.loadTexts:
    issMirrorCtrlExtnTable.setStatus("current")
_IssMirrorCtrlExtnEntry_Object = MibTableRow
issMirrorCtrlExtnEntry = _IssMirrorCtrlExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 6, 1)
)
issMirrorCtrlExtnEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issMirrorCtrlExtnSessionIndex"),
)
if mibBuilder.loadTexts:
    issMirrorCtrlExtnEntry.setStatus("current")


class _IssMirrorCtrlExtnSessionIndex_Type(Integer32):
    """Custom type issMirrorCtrlExtnSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_IssMirrorCtrlExtnSessionIndex_Type.__name__ = "Integer32"
_IssMirrorCtrlExtnSessionIndex_Object = MibTableColumn
issMirrorCtrlExtnSessionIndex = _IssMirrorCtrlExtnSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 6, 1, 1),
    _IssMirrorCtrlExtnSessionIndex_Type()
)
issMirrorCtrlExtnSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issMirrorCtrlExtnSessionIndex.setStatus("current")


class _IssMirrorCtrlExtnMirrType_Type(Integer32):
    """Custom type issMirrorCtrlExtnMirrType based on Integer32"""
    defaultValue = 4

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
        *(("portBased", 1),
          ("macflowBased", 2),
          ("vlanBased", 3),
          ("invalid", 4),
          ("ipflowBased", 5))
    )


_IssMirrorCtrlExtnMirrType_Type.__name__ = "Integer32"
_IssMirrorCtrlExtnMirrType_Object = MibTableColumn
issMirrorCtrlExtnMirrType = _IssMirrorCtrlExtnMirrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 6, 1, 2),
    _IssMirrorCtrlExtnMirrType_Type()
)
issMirrorCtrlExtnMirrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMirrorCtrlExtnMirrType.setStatus("current")


class _IssMirrorCtrlExtnRSpanStatus_Type(Integer32):
    """Custom type issMirrorCtrlExtnRSpanStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sourceRSpanVlan", 1),
          ("destinationRSpanVlan", 2),
          ("disabled", 3))
    )


_IssMirrorCtrlExtnRSpanStatus_Type.__name__ = "Integer32"
_IssMirrorCtrlExtnRSpanStatus_Object = MibTableColumn
issMirrorCtrlExtnRSpanStatus = _IssMirrorCtrlExtnRSpanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 6, 1, 3),
    _IssMirrorCtrlExtnRSpanStatus_Type()
)
issMirrorCtrlExtnRSpanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMirrorCtrlExtnRSpanStatus.setStatus("current")


class _IssMirrorCtrlExtnRSpanVlanId_Type(Integer32):
    """Custom type issMirrorCtrlExtnRSpanVlanId based on Integer32"""
    defaultValue = 0


_IssMirrorCtrlExtnRSpanVlanId_Type.__name__ = "Integer32"
_IssMirrorCtrlExtnRSpanVlanId_Object = MibTableColumn
issMirrorCtrlExtnRSpanVlanId = _IssMirrorCtrlExtnRSpanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 6, 1, 4),
    _IssMirrorCtrlExtnRSpanVlanId_Type()
)
issMirrorCtrlExtnRSpanVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMirrorCtrlExtnRSpanVlanId.setStatus("current")


class _IssMirrorCtrlExtnRSpanContext_Type(Integer32):
    """Custom type issMirrorCtrlExtnRSpanContext based on Integer32"""
    defaultValue = 0


_IssMirrorCtrlExtnRSpanContext_Type.__name__ = "Integer32"
_IssMirrorCtrlExtnRSpanContext_Object = MibTableColumn
issMirrorCtrlExtnRSpanContext = _IssMirrorCtrlExtnRSpanContext_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 6, 1, 5),
    _IssMirrorCtrlExtnRSpanContext_Type()
)
issMirrorCtrlExtnRSpanContext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMirrorCtrlExtnRSpanContext.setStatus("current")
_IssMirrorCtrlExtnStatus_Type = RowStatus
_IssMirrorCtrlExtnStatus_Object = MibTableColumn
issMirrorCtrlExtnStatus = _IssMirrorCtrlExtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 6, 1, 6),
    _IssMirrorCtrlExtnStatus_Type()
)
issMirrorCtrlExtnStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issMirrorCtrlExtnStatus.setStatus("current")
_IssMirrorCtrlExtnSrcTable_Object = MibTable
issMirrorCtrlExtnSrcTable = _IssMirrorCtrlExtnSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 7)
)
if mibBuilder.loadTexts:
    issMirrorCtrlExtnSrcTable.setStatus("current")
_IssMirrorCtrlExtnSrcEntry_Object = MibTableRow
issMirrorCtrlExtnSrcEntry = _IssMirrorCtrlExtnSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 7, 1)
)
issMirrorCtrlExtnSrcEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issMirrorCtrlExtnSessionIndex"),
    (0, "ARICENT-ISS-MIB", "issMirrorCtrlExtnSrcId"),
)
if mibBuilder.loadTexts:
    issMirrorCtrlExtnSrcEntry.setStatus("current")


class _IssMirrorCtrlExtnSrcId_Type(Integer32):
    """Custom type issMirrorCtrlExtnSrcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IssMirrorCtrlExtnSrcId_Type.__name__ = "Integer32"
_IssMirrorCtrlExtnSrcId_Object = MibTableColumn
issMirrorCtrlExtnSrcId = _IssMirrorCtrlExtnSrcId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 7, 1, 1),
    _IssMirrorCtrlExtnSrcId_Type()
)
issMirrorCtrlExtnSrcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issMirrorCtrlExtnSrcId.setStatus("current")


class _IssMirrorCtrlExtnSrcCfg_Type(Integer32):
    """Custom type issMirrorCtrlExtnSrcCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_IssMirrorCtrlExtnSrcCfg_Type.__name__ = "Integer32"
_IssMirrorCtrlExtnSrcCfg_Object = MibTableColumn
issMirrorCtrlExtnSrcCfg = _IssMirrorCtrlExtnSrcCfg_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 7, 1, 2),
    _IssMirrorCtrlExtnSrcCfg_Type()
)
issMirrorCtrlExtnSrcCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMirrorCtrlExtnSrcCfg.setStatus("current")


class _IssMirrorCtrlExtnSrcMode_Type(Integer32):
    """Custom type issMirrorCtrlExtnSrcMode based on Integer32"""
    defaultValue = 3

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
        *(("ingress", 1),
          ("egress", 2),
          ("both", 3),
          ("disable", 4))
    )


_IssMirrorCtrlExtnSrcMode_Type.__name__ = "Integer32"
_IssMirrorCtrlExtnSrcMode_Object = MibTableColumn
issMirrorCtrlExtnSrcMode = _IssMirrorCtrlExtnSrcMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 7, 1, 3),
    _IssMirrorCtrlExtnSrcMode_Type()
)
issMirrorCtrlExtnSrcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMirrorCtrlExtnSrcMode.setStatus("current")
_IssMirrorCtrlExtnSrcVlanTable_Object = MibTable
issMirrorCtrlExtnSrcVlanTable = _IssMirrorCtrlExtnSrcVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 8)
)
if mibBuilder.loadTexts:
    issMirrorCtrlExtnSrcVlanTable.setStatus("current")
_IssMirrorCtrlExtnSrcVlanEntry_Object = MibTableRow
issMirrorCtrlExtnSrcVlanEntry = _IssMirrorCtrlExtnSrcVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 8, 1)
)
issMirrorCtrlExtnSrcVlanEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issMirrorCtrlExtnSessionIndex"),
    (0, "ARICENT-ISS-MIB", "issMirrorCtrlExtnSrcVlanContext"),
    (0, "ARICENT-ISS-MIB", "issMirrorCtrlExtnSrcVlanId"),
)
if mibBuilder.loadTexts:
    issMirrorCtrlExtnSrcVlanEntry.setStatus("current")


class _IssMirrorCtrlExtnSrcVlanContext_Type(Integer32):
    """Custom type issMirrorCtrlExtnSrcVlanContext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_IssMirrorCtrlExtnSrcVlanContext_Type.__name__ = "Integer32"
_IssMirrorCtrlExtnSrcVlanContext_Object = MibTableColumn
issMirrorCtrlExtnSrcVlanContext = _IssMirrorCtrlExtnSrcVlanContext_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 8, 1, 1),
    _IssMirrorCtrlExtnSrcVlanContext_Type()
)
issMirrorCtrlExtnSrcVlanContext.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issMirrorCtrlExtnSrcVlanContext.setStatus("current")


class _IssMirrorCtrlExtnSrcVlanId_Type(Integer32):
    """Custom type issMirrorCtrlExtnSrcVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IssMirrorCtrlExtnSrcVlanId_Type.__name__ = "Integer32"
_IssMirrorCtrlExtnSrcVlanId_Object = MibTableColumn
issMirrorCtrlExtnSrcVlanId = _IssMirrorCtrlExtnSrcVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 8, 1, 2),
    _IssMirrorCtrlExtnSrcVlanId_Type()
)
issMirrorCtrlExtnSrcVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issMirrorCtrlExtnSrcVlanId.setStatus("current")


class _IssMirrorCtrlExtnSrcVlanCfg_Type(Integer32):
    """Custom type issMirrorCtrlExtnSrcVlanCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_IssMirrorCtrlExtnSrcVlanCfg_Type.__name__ = "Integer32"
_IssMirrorCtrlExtnSrcVlanCfg_Object = MibTableColumn
issMirrorCtrlExtnSrcVlanCfg = _IssMirrorCtrlExtnSrcVlanCfg_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 8, 1, 3),
    _IssMirrorCtrlExtnSrcVlanCfg_Type()
)
issMirrorCtrlExtnSrcVlanCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMirrorCtrlExtnSrcVlanCfg.setStatus("current")


class _IssMirrorCtrlExtnSrcVlanMode_Type(Integer32):
    """Custom type issMirrorCtrlExtnSrcVlanMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2),
          ("both", 3))
    )


_IssMirrorCtrlExtnSrcVlanMode_Type.__name__ = "Integer32"
_IssMirrorCtrlExtnSrcVlanMode_Object = MibTableColumn
issMirrorCtrlExtnSrcVlanMode = _IssMirrorCtrlExtnSrcVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 8, 1, 4),
    _IssMirrorCtrlExtnSrcVlanMode_Type()
)
issMirrorCtrlExtnSrcVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMirrorCtrlExtnSrcVlanMode.setStatus("current")
_IssMirrorCtrlExtnDestinationTable_Object = MibTable
issMirrorCtrlExtnDestinationTable = _IssMirrorCtrlExtnDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 9)
)
if mibBuilder.loadTexts:
    issMirrorCtrlExtnDestinationTable.setStatus("current")
_IssMirrorCtrlExtnDestinationEntry_Object = MibTableRow
issMirrorCtrlExtnDestinationEntry = _IssMirrorCtrlExtnDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 9, 1)
)
issMirrorCtrlExtnDestinationEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issMirrorCtrlExtnSessionIndex"),
    (0, "ARICENT-ISS-MIB", "issMirrorCtrlExtnDestination"),
)
if mibBuilder.loadTexts:
    issMirrorCtrlExtnDestinationEntry.setStatus("current")


class _IssMirrorCtrlExtnDestination_Type(Integer32):
    """Custom type issMirrorCtrlExtnDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IssMirrorCtrlExtnDestination_Type.__name__ = "Integer32"
_IssMirrorCtrlExtnDestination_Object = MibTableColumn
issMirrorCtrlExtnDestination = _IssMirrorCtrlExtnDestination_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 9, 1, 1),
    _IssMirrorCtrlExtnDestination_Type()
)
issMirrorCtrlExtnDestination.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issMirrorCtrlExtnDestination.setStatus("current")


class _IssMirrorCtrlExtnDestCfg_Type(Integer32):
    """Custom type issMirrorCtrlExtnDestCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_IssMirrorCtrlExtnDestCfg_Type.__name__ = "Integer32"
_IssMirrorCtrlExtnDestCfg_Object = MibTableColumn
issMirrorCtrlExtnDestCfg = _IssMirrorCtrlExtnDestCfg_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 9, 1, 2),
    _IssMirrorCtrlExtnDestCfg_Type()
)
issMirrorCtrlExtnDestCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMirrorCtrlExtnDestCfg.setStatus("current")


class _IssCpuMirrorType_Type(Integer32):
    """Custom type issCpuMirrorType based on Integer32"""
    defaultValue = 4

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
        *(("ingress", 1),
          ("egress", 2),
          ("both", 3),
          ("disable", 4))
    )


_IssCpuMirrorType_Type.__name__ = "Integer32"
_IssCpuMirrorType_Object = MibScalar
issCpuMirrorType = _IssCpuMirrorType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 10),
    _IssCpuMirrorType_Type()
)
issCpuMirrorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issCpuMirrorType.setStatus("current")


class _IssCpuMirrorToPort_Type(Integer32):
    """Custom type issCpuMirrorToPort based on Integer32"""
    defaultValue = 0


_IssCpuMirrorToPort_Type.__name__ = "Integer32"
_IssCpuMirrorToPort_Object = MibScalar
issCpuMirrorToPort = _IssCpuMirrorToPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 3, 11),
    _IssCpuMirrorToPort_Type()
)
issCpuMirrorToPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issCpuMirrorToPort.setStatus("current")
_IssRateControl_ObjectIdentity = ObjectIdentity
issRateControl = _IssRateControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 4)
)
_IssRateCtrlTable_Object = MibTable
issRateCtrlTable = _IssRateCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 4, 1)
)
if mibBuilder.loadTexts:
    issRateCtrlTable.setStatus("deprecated")
_IssRateCtrlEntry_Object = MibTableRow
issRateCtrlEntry = _IssRateCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 4, 1, 1)
)
issRateCtrlEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issRateCtrlIndex"),
)
if mibBuilder.loadTexts:
    issRateCtrlEntry.setStatus("deprecated")


class _IssRateCtrlIndex_Type(Integer32):
    """Custom type issRateCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IssRateCtrlIndex_Type.__name__ = "Integer32"
_IssRateCtrlIndex_Object = MibTableColumn
issRateCtrlIndex = _IssRateCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 4, 1, 1, 1),
    _IssRateCtrlIndex_Type()
)
issRateCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issRateCtrlIndex.setStatus("deprecated")


class _IssRateCtrlDLFLimitValue_Type(Integer32):
    """Custom type issRateCtrlDLFLimitValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IssRateCtrlDLFLimitValue_Type.__name__ = "Integer32"
_IssRateCtrlDLFLimitValue_Object = MibTableColumn
issRateCtrlDLFLimitValue = _IssRateCtrlDLFLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 4, 1, 1, 2),
    _IssRateCtrlDLFLimitValue_Type()
)
issRateCtrlDLFLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issRateCtrlDLFLimitValue.setStatus("deprecated")


class _IssRateCtrlBCASTLimitValue_Type(Integer32):
    """Custom type issRateCtrlBCASTLimitValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IssRateCtrlBCASTLimitValue_Type.__name__ = "Integer32"
_IssRateCtrlBCASTLimitValue_Object = MibTableColumn
issRateCtrlBCASTLimitValue = _IssRateCtrlBCASTLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 4, 1, 1, 3),
    _IssRateCtrlBCASTLimitValue_Type()
)
issRateCtrlBCASTLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issRateCtrlBCASTLimitValue.setStatus("deprecated")


class _IssRateCtrlMCASTLimitValue_Type(Integer32):
    """Custom type issRateCtrlMCASTLimitValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IssRateCtrlMCASTLimitValue_Type.__name__ = "Integer32"
_IssRateCtrlMCASTLimitValue_Object = MibTableColumn
issRateCtrlMCASTLimitValue = _IssRateCtrlMCASTLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 4, 1, 1, 4),
    _IssRateCtrlMCASTLimitValue_Type()
)
issRateCtrlMCASTLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issRateCtrlMCASTLimitValue.setStatus("deprecated")


class _IssRateCtrlPortRateLimit_Type(Integer32):
    """Custom type issRateCtrlPortRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80000000),
    )


_IssRateCtrlPortRateLimit_Type.__name__ = "Integer32"
_IssRateCtrlPortRateLimit_Object = MibTableColumn
issRateCtrlPortRateLimit = _IssRateCtrlPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 4, 1, 1, 5),
    _IssRateCtrlPortRateLimit_Type()
)
issRateCtrlPortRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issRateCtrlPortRateLimit.setStatus("deprecated")


class _IssRateCtrlPortBurstSize_Type(Integer32):
    """Custom type issRateCtrlPortBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80000000),
    )


_IssRateCtrlPortBurstSize_Type.__name__ = "Integer32"
_IssRateCtrlPortBurstSize_Object = MibTableColumn
issRateCtrlPortBurstSize = _IssRateCtrlPortBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 4, 1, 1, 6),
    _IssRateCtrlPortBurstSize_Type()
)
issRateCtrlPortBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issRateCtrlPortBurstSize.setStatus("deprecated")
_IssL2Filter_ObjectIdentity = ObjectIdentity
issL2Filter = _IssL2Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5)
)
_IssL2FilterTable_Object = MibTable
issL2FilterTable = _IssL2FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5, 1)
)
if mibBuilder.loadTexts:
    issL2FilterTable.setStatus("deprecated")
_IssL2FilterEntry_Object = MibTableRow
issL2FilterEntry = _IssL2FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5, 1, 1)
)
issL2FilterEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issL2FilterNo"),
)
if mibBuilder.loadTexts:
    issL2FilterEntry.setStatus("deprecated")


class _IssL2FilterNo_Type(Integer32):
    """Custom type issL2FilterNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IssL2FilterNo_Type.__name__ = "Integer32"
_IssL2FilterNo_Object = MibTableColumn
issL2FilterNo = _IssL2FilterNo_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5, 1, 1, 1),
    _IssL2FilterNo_Type()
)
issL2FilterNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issL2FilterNo.setStatus("current")


class _IssL2FilterPriority_Type(Integer32):
    """Custom type issL2FilterPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IssL2FilterPriority_Type.__name__ = "Integer32"
_IssL2FilterPriority_Object = MibTableColumn
issL2FilterPriority = _IssL2FilterPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5, 1, 1, 2),
    _IssL2FilterPriority_Type()
)
issL2FilterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL2FilterPriority.setStatus("current")


class _IssL2FilterEtherType_Type(Integer32):
    """Custom type issL2FilterEtherType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IssL2FilterEtherType_Type.__name__ = "Integer32"
_IssL2FilterEtherType_Object = MibTableColumn
issL2FilterEtherType = _IssL2FilterEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5, 1, 1, 3),
    _IssL2FilterEtherType_Type()
)
issL2FilterEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL2FilterEtherType.setStatus("deprecated")


class _IssL2FilterProtocolType_Type(Unsigned32):
    """Custom type issL2FilterProtocolType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IssL2FilterProtocolType_Type.__name__ = "Unsigned32"
_IssL2FilterProtocolType_Object = MibTableColumn
issL2FilterProtocolType = _IssL2FilterProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5, 1, 1, 4),
    _IssL2FilterProtocolType_Type()
)
issL2FilterProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL2FilterProtocolType.setStatus("deprecated")
_IssL2FilterDstMacAddr_Type = MacAddress
_IssL2FilterDstMacAddr_Object = MibTableColumn
issL2FilterDstMacAddr = _IssL2FilterDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5, 1, 1, 5),
    _IssL2FilterDstMacAddr_Type()
)
issL2FilterDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL2FilterDstMacAddr.setStatus("deprecated")
_IssL2FilterSrcMacAddr_Type = MacAddress
_IssL2FilterSrcMacAddr_Object = MibTableColumn
issL2FilterSrcMacAddr = _IssL2FilterSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5, 1, 1, 6),
    _IssL2FilterSrcMacAddr_Type()
)
issL2FilterSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL2FilterSrcMacAddr.setStatus("deprecated")


class _IssL2FilterVlanId_Type(Integer32):
    """Custom type issL2FilterVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_IssL2FilterVlanId_Type.__name__ = "Integer32"
_IssL2FilterVlanId_Object = MibTableColumn
issL2FilterVlanId = _IssL2FilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5, 1, 1, 7),
    _IssL2FilterVlanId_Type()
)
issL2FilterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL2FilterVlanId.setStatus("deprecated")
_IssL2FilterInPortList_Type = PortList
_IssL2FilterInPortList_Object = MibTableColumn
issL2FilterInPortList = _IssL2FilterInPortList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5, 1, 1, 8),
    _IssL2FilterInPortList_Type()
)
issL2FilterInPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL2FilterInPortList.setStatus("deprecated")


class _IssL2FilterAction_Type(Integer32):
    """Custom type issL2FilterAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2))
    )


_IssL2FilterAction_Type.__name__ = "Integer32"
_IssL2FilterAction_Object = MibTableColumn
issL2FilterAction = _IssL2FilterAction_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5, 1, 1, 9),
    _IssL2FilterAction_Type()
)
issL2FilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL2FilterAction.setStatus("deprecated")
_IssL2FilterMatchCount_Type = Counter32
_IssL2FilterMatchCount_Object = MibTableColumn
issL2FilterMatchCount = _IssL2FilterMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5, 1, 1, 10),
    _IssL2FilterMatchCount_Type()
)
issL2FilterMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issL2FilterMatchCount.setStatus("deprecated")
_IssL2FilterStatus_Type = RowStatus
_IssL2FilterStatus_Object = MibTableColumn
issL2FilterStatus = _IssL2FilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5, 1, 1, 11),
    _IssL2FilterStatus_Type()
)
issL2FilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issL2FilterStatus.setStatus("deprecated")
_IssL2FilterOutPortList_Type = PortList
_IssL2FilterOutPortList_Object = MibTableColumn
issL2FilterOutPortList = _IssL2FilterOutPortList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5, 1, 1, 12),
    _IssL2FilterOutPortList_Type()
)
issL2FilterOutPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL2FilterOutPortList.setStatus("deprecated")


class _IssL2FilterDirection_Type(Integer32):
    """Custom type issL2FilterDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_IssL2FilterDirection_Type.__name__ = "Integer32"
_IssL2FilterDirection_Object = MibTableColumn
issL2FilterDirection = _IssL2FilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 5, 1, 1, 13),
    _IssL2FilterDirection_Type()
)
issL2FilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL2FilterDirection.setStatus("deprecated")
_IssL3Filter_ObjectIdentity = ObjectIdentity
issL3Filter = _IssL3Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6)
)
_IssL3FilterTable_Object = MibTable
issL3FilterTable = _IssL3FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1)
)
if mibBuilder.loadTexts:
    issL3FilterTable.setStatus("deprecated")
_IssL3FilterEntry_Object = MibTableRow
issL3FilterEntry = _IssL3FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1)
)
issL3FilterEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issL3FilterNo"),
)
if mibBuilder.loadTexts:
    issL3FilterEntry.setStatus("deprecated")


class _IssL3FilterNo_Type(Integer32):
    """Custom type issL3FilterNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IssL3FilterNo_Type.__name__ = "Integer32"
_IssL3FilterNo_Object = MibTableColumn
issL3FilterNo = _IssL3FilterNo_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 1),
    _IssL3FilterNo_Type()
)
issL3FilterNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issL3FilterNo.setStatus("deprecated")


class _IssL3FilterPriority_Type(Integer32):
    """Custom type issL3FilterPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IssL3FilterPriority_Type.__name__ = "Integer32"
_IssL3FilterPriority_Object = MibTableColumn
issL3FilterPriority = _IssL3FilterPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 2),
    _IssL3FilterPriority_Type()
)
issL3FilterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterPriority.setStatus("deprecated")


class _IssL3FilterProtocol_Type(Integer32):
    """Custom type issL3FilterProtocol based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IssL3FilterProtocol_Type.__name__ = "Integer32"
_IssL3FilterProtocol_Object = MibTableColumn
issL3FilterProtocol = _IssL3FilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 3),
    _IssL3FilterProtocol_Type()
)
issL3FilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterProtocol.setStatus("deprecated")


class _IssL3FilterMessageType_Type(Integer32):
    """Custom type issL3FilterMessageType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IssL3FilterMessageType_Type.__name__ = "Integer32"
_IssL3FilterMessageType_Object = MibTableColumn
issL3FilterMessageType = _IssL3FilterMessageType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 4),
    _IssL3FilterMessageType_Type()
)
issL3FilterMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterMessageType.setStatus("deprecated")


class _IssL3FilterMessageCode_Type(Integer32):
    """Custom type issL3FilterMessageCode based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IssL3FilterMessageCode_Type.__name__ = "Integer32"
_IssL3FilterMessageCode_Object = MibTableColumn
issL3FilterMessageCode = _IssL3FilterMessageCode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 5),
    _IssL3FilterMessageCode_Type()
)
issL3FilterMessageCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterMessageCode.setStatus("deprecated")


class _IssL3FilterDstIpAddr_Type(IpAddress):
    """Custom type issL3FilterDstIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IssL3FilterDstIpAddr_Type.__name__ = "IpAddress"
_IssL3FilterDstIpAddr_Object = MibTableColumn
issL3FilterDstIpAddr = _IssL3FilterDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 6),
    _IssL3FilterDstIpAddr_Type()
)
issL3FilterDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterDstIpAddr.setStatus("deprecated")


class _IssL3FilterSrcIpAddr_Type(IpAddress):
    """Custom type issL3FilterSrcIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IssL3FilterSrcIpAddr_Type.__name__ = "IpAddress"
_IssL3FilterSrcIpAddr_Object = MibTableColumn
issL3FilterSrcIpAddr = _IssL3FilterSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 7),
    _IssL3FilterSrcIpAddr_Type()
)
issL3FilterSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterSrcIpAddr.setStatus("deprecated")


class _IssL3FilterDstIpAddrMask_Type(IpAddress):
    """Custom type issL3FilterDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_IssL3FilterDstIpAddrMask_Type.__name__ = "IpAddress"
_IssL3FilterDstIpAddrMask_Object = MibTableColumn
issL3FilterDstIpAddrMask = _IssL3FilterDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 8),
    _IssL3FilterDstIpAddrMask_Type()
)
issL3FilterDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterDstIpAddrMask.setStatus("deprecated")


class _IssL3FilterSrcIpAddrMask_Type(IpAddress):
    """Custom type issL3FilterSrcIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_IssL3FilterSrcIpAddrMask_Type.__name__ = "IpAddress"
_IssL3FilterSrcIpAddrMask_Object = MibTableColumn
issL3FilterSrcIpAddrMask = _IssL3FilterSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 9),
    _IssL3FilterSrcIpAddrMask_Type()
)
issL3FilterSrcIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterSrcIpAddrMask.setStatus("deprecated")


class _IssL3FilterMinDstProtPort_Type(Unsigned32):
    """Custom type issL3FilterMinDstProtPort based on Unsigned32"""
    defaultValue = 0


_IssL3FilterMinDstProtPort_Type.__name__ = "Unsigned32"
_IssL3FilterMinDstProtPort_Object = MibTableColumn
issL3FilterMinDstProtPort = _IssL3FilterMinDstProtPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 10),
    _IssL3FilterMinDstProtPort_Type()
)
issL3FilterMinDstProtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterMinDstProtPort.setStatus("deprecated")


class _IssL3FilterMaxDstProtPort_Type(Unsigned32):
    """Custom type issL3FilterMaxDstProtPort based on Unsigned32"""
    defaultValue = 65535


_IssL3FilterMaxDstProtPort_Type.__name__ = "Unsigned32"
_IssL3FilterMaxDstProtPort_Object = MibTableColumn
issL3FilterMaxDstProtPort = _IssL3FilterMaxDstProtPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 11),
    _IssL3FilterMaxDstProtPort_Type()
)
issL3FilterMaxDstProtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterMaxDstProtPort.setStatus("deprecated")


class _IssL3FilterMinSrcProtPort_Type(Unsigned32):
    """Custom type issL3FilterMinSrcProtPort based on Unsigned32"""
    defaultValue = 0


_IssL3FilterMinSrcProtPort_Type.__name__ = "Unsigned32"
_IssL3FilterMinSrcProtPort_Object = MibTableColumn
issL3FilterMinSrcProtPort = _IssL3FilterMinSrcProtPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 12),
    _IssL3FilterMinSrcProtPort_Type()
)
issL3FilterMinSrcProtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterMinSrcProtPort.setStatus("deprecated")


class _IssL3FilterMaxSrcProtPort_Type(Unsigned32):
    """Custom type issL3FilterMaxSrcProtPort based on Unsigned32"""
    defaultValue = 65535


_IssL3FilterMaxSrcProtPort_Type.__name__ = "Unsigned32"
_IssL3FilterMaxSrcProtPort_Object = MibTableColumn
issL3FilterMaxSrcProtPort = _IssL3FilterMaxSrcProtPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 13),
    _IssL3FilterMaxSrcProtPort_Type()
)
issL3FilterMaxSrcProtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterMaxSrcProtPort.setStatus("deprecated")
_IssL3FilterInPortList_Type = PortList
_IssL3FilterInPortList_Object = MibTableColumn
issL3FilterInPortList = _IssL3FilterInPortList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 14),
    _IssL3FilterInPortList_Type()
)
issL3FilterInPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterInPortList.setStatus("deprecated")
_IssL3FilterOutPortList_Type = PortList
_IssL3FilterOutPortList_Object = MibTableColumn
issL3FilterOutPortList = _IssL3FilterOutPortList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 15),
    _IssL3FilterOutPortList_Type()
)
issL3FilterOutPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterOutPortList.setStatus("deprecated")


class _IssL3FilterAckBit_Type(Integer32):
    """Custom type issL3FilterAckBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("establish", 1),
          ("notEstablish", 2),
          ("any", 3))
    )


_IssL3FilterAckBit_Type.__name__ = "Integer32"
_IssL3FilterAckBit_Object = MibTableColumn
issL3FilterAckBit = _IssL3FilterAckBit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 16),
    _IssL3FilterAckBit_Type()
)
issL3FilterAckBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issL3FilterAckBit.setStatus("deprecated")


class _IssL3FilterRstBit_Type(Integer32):
    """Custom type issL3FilterRstBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("notSet", 2),
          ("any", 3))
    )


_IssL3FilterRstBit_Type.__name__ = "Integer32"
_IssL3FilterRstBit_Object = MibTableColumn
issL3FilterRstBit = _IssL3FilterRstBit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 17),
    _IssL3FilterRstBit_Type()
)
issL3FilterRstBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issL3FilterRstBit.setStatus("deprecated")


class _IssL3FilterTos_Type(Integer32):
    """Custom type issL3FilterTos based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_IssL3FilterTos_Type.__name__ = "Integer32"
_IssL3FilterTos_Object = MibTableColumn
issL3FilterTos = _IssL3FilterTos_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 18),
    _IssL3FilterTos_Type()
)
issL3FilterTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issL3FilterTos.setStatus("deprecated")


class _IssL3FilterDscp_Type(Integer32):
    """Custom type issL3FilterDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_IssL3FilterDscp_Type.__name__ = "Integer32"
_IssL3FilterDscp_Object = MibTableColumn
issL3FilterDscp = _IssL3FilterDscp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 19),
    _IssL3FilterDscp_Type()
)
issL3FilterDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issL3FilterDscp.setStatus("deprecated")


class _IssL3FilterDirection_Type(Integer32):
    """Custom type issL3FilterDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_IssL3FilterDirection_Type.__name__ = "Integer32"
_IssL3FilterDirection_Object = MibTableColumn
issL3FilterDirection = _IssL3FilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 20),
    _IssL3FilterDirection_Type()
)
issL3FilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterDirection.setStatus("deprecated")


class _IssL3FilterAction_Type(Integer32):
    """Custom type issL3FilterAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2))
    )


_IssL3FilterAction_Type.__name__ = "Integer32"
_IssL3FilterAction_Object = MibTableColumn
issL3FilterAction = _IssL3FilterAction_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 21),
    _IssL3FilterAction_Type()
)
issL3FilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL3FilterAction.setStatus("deprecated")
_IssL3FilterMatchCount_Type = Counter32
_IssL3FilterMatchCount_Object = MibTableColumn
issL3FilterMatchCount = _IssL3FilterMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 22),
    _IssL3FilterMatchCount_Type()
)
issL3FilterMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issL3FilterMatchCount.setStatus("deprecated")
_IssL3FilterStatus_Type = RowStatus
_IssL3FilterStatus_Object = MibTableColumn
issL3FilterStatus = _IssL3FilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 6, 1, 1, 23),
    _IssL3FilterStatus_Type()
)
issL3FilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issL3FilterStatus.setStatus("deprecated")
_IssIpAuthMgr_ObjectIdentity = ObjectIdentity
issIpAuthMgr = _IssIpAuthMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 7)
)
_IssIpAuthMgrTable_Object = MibTable
issIpAuthMgrTable = _IssIpAuthMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 7, 1)
)
if mibBuilder.loadTexts:
    issIpAuthMgrTable.setStatus("current")
_IssIpAuthMgrEntry_Object = MibTableRow
issIpAuthMgrEntry = _IssIpAuthMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 7, 1, 1)
)
issIpAuthMgrEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issIpAuthMgrIpAddr"),
    (0, "ARICENT-ISS-MIB", "issIpAuthMgrIpMask"),
)
if mibBuilder.loadTexts:
    issIpAuthMgrEntry.setStatus("current")
_IssIpAuthMgrIpAddr_Type = IpAddress
_IssIpAuthMgrIpAddr_Object = MibTableColumn
issIpAuthMgrIpAddr = _IssIpAuthMgrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 7, 1, 1, 1),
    _IssIpAuthMgrIpAddr_Type()
)
issIpAuthMgrIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issIpAuthMgrIpAddr.setStatus("current")
_IssIpAuthMgrIpMask_Type = IpAddress
_IssIpAuthMgrIpMask_Object = MibTableColumn
issIpAuthMgrIpMask = _IssIpAuthMgrIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 7, 1, 1, 2),
    _IssIpAuthMgrIpMask_Type()
)
issIpAuthMgrIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issIpAuthMgrIpMask.setStatus("current")
_IssIpAuthMgrPortList_Type = PortList
_IssIpAuthMgrPortList_Object = MibTableColumn
issIpAuthMgrPortList = _IssIpAuthMgrPortList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 7, 1, 1, 3),
    _IssIpAuthMgrPortList_Type()
)
issIpAuthMgrPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issIpAuthMgrPortList.setStatus("current")
_IssIpAuthMgrVlanList_Type = OctetString
_IssIpAuthMgrVlanList_Object = MibTableColumn
issIpAuthMgrVlanList = _IssIpAuthMgrVlanList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 7, 1, 1, 4),
    _IssIpAuthMgrVlanList_Type()
)
issIpAuthMgrVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issIpAuthMgrVlanList.setStatus("current")


class _IssIpAuthMgrOOBPort_Type(TruthValue):
    """Custom type issIpAuthMgrOOBPort based on TruthValue"""
    defaultValue = 2


_IssIpAuthMgrOOBPort_Type.__name__ = "TruthValue"
_IssIpAuthMgrOOBPort_Object = MibTableColumn
issIpAuthMgrOOBPort = _IssIpAuthMgrOOBPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 7, 1, 1, 5),
    _IssIpAuthMgrOOBPort_Type()
)
issIpAuthMgrOOBPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issIpAuthMgrOOBPort.setStatus("current")


class _IssIpAuthMgrAllowedServices_Type(Integer32):
    """Custom type issIpAuthMgrAllowedServices based on Integer32"""
    defaultValue = 31


_IssIpAuthMgrAllowedServices_Type.__name__ = "Integer32"
_IssIpAuthMgrAllowedServices_Object = MibTableColumn
issIpAuthMgrAllowedServices = _IssIpAuthMgrAllowedServices_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 7, 1, 1, 6),
    _IssIpAuthMgrAllowedServices_Type()
)
issIpAuthMgrAllowedServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issIpAuthMgrAllowedServices.setStatus("current")
_IssIpAuthMgrRowStatus_Type = RowStatus
_IssIpAuthMgrRowStatus_Object = MibTableColumn
issIpAuthMgrRowStatus = _IssIpAuthMgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 7, 1, 1, 7),
    _IssIpAuthMgrRowStatus_Type()
)
issIpAuthMgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issIpAuthMgrRowStatus.setStatus("current")
_IssExt_ObjectIdentity = ObjectIdentity
issExt = _IssExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8)
)
_IssL4Switching_ObjectIdentity = ObjectIdentity
issL4Switching = _IssL4Switching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 9)
)
_IssL4SwitchingFilterTable_Object = MibTable
issL4SwitchingFilterTable = _IssL4SwitchingFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 9, 1)
)
if mibBuilder.loadTexts:
    issL4SwitchingFilterTable.setStatus("current")
_IssL4SwitchingFilterEntry_Object = MibTableRow
issL4SwitchingFilterEntry = _IssL4SwitchingFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 9, 1, 1)
)
issL4SwitchingFilterEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issL4SwitchingFilterNo"),
)
if mibBuilder.loadTexts:
    issL4SwitchingFilterEntry.setStatus("current")


class _IssL4SwitchingFilterNo_Type(Integer32):
    """Custom type issL4SwitchingFilterNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IssL4SwitchingFilterNo_Type.__name__ = "Integer32"
_IssL4SwitchingFilterNo_Object = MibTableColumn
issL4SwitchingFilterNo = _IssL4SwitchingFilterNo_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 9, 1, 1, 1),
    _IssL4SwitchingFilterNo_Type()
)
issL4SwitchingFilterNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issL4SwitchingFilterNo.setStatus("current")


class _IssL4SwitchingProtocol_Type(Integer32):
    """Custom type issL4SwitchingProtocol based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IssL4SwitchingProtocol_Type.__name__ = "Integer32"
_IssL4SwitchingProtocol_Object = MibTableColumn
issL4SwitchingProtocol = _IssL4SwitchingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 9, 1, 1, 2),
    _IssL4SwitchingProtocol_Type()
)
issL4SwitchingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL4SwitchingProtocol.setStatus("current")


class _IssL4SwitchingPortNo_Type(Unsigned32):
    """Custom type issL4SwitchingPortNo based on Unsigned32"""
    defaultValue = 0


_IssL4SwitchingPortNo_Type.__name__ = "Unsigned32"
_IssL4SwitchingPortNo_Object = MibTableColumn
issL4SwitchingPortNo = _IssL4SwitchingPortNo_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 9, 1, 1, 3),
    _IssL4SwitchingPortNo_Type()
)
issL4SwitchingPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL4SwitchingPortNo.setStatus("current")


class _IssL4SwitchingCopyToPort_Type(Integer32):
    """Custom type issL4SwitchingCopyToPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IssL4SwitchingCopyToPort_Type.__name__ = "Integer32"
_IssL4SwitchingCopyToPort_Object = MibTableColumn
issL4SwitchingCopyToPort = _IssL4SwitchingCopyToPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 9, 1, 1, 4),
    _IssL4SwitchingCopyToPort_Type()
)
issL4SwitchingCopyToPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issL4SwitchingCopyToPort.setStatus("current")
_IssL4SwitchingFilterStatus_Type = RowStatus
_IssL4SwitchingFilterStatus_Object = MibTableColumn
issL4SwitchingFilterStatus = _IssL4SwitchingFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 9, 1, 1, 5),
    _IssL4SwitchingFilterStatus_Type()
)
issL4SwitchingFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issL4SwitchingFilterStatus.setStatus("current")
_IssSystemTrap_ObjectIdentity = ObjectIdentity
issSystemTrap = _IssSystemTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 10)
)
_IssMsrFailedOid_Type = ObjectIdentifier
_IssMsrFailedOid_Object = MibScalar
issMsrFailedOid = _IssMsrFailedOid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 10, 1),
    _IssMsrFailedOid_Type()
)
issMsrFailedOid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    issMsrFailedOid.setStatus("current")
_IssMsrFailedValue_Type = DisplayString
_IssMsrFailedValue_Object = MibScalar
issMsrFailedValue = _IssMsrFailedValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 10, 2),
    _IssMsrFailedValue_Type()
)
issMsrFailedValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    issMsrFailedValue.setStatus("current")
_IssAuditTrap_ObjectIdentity = ObjectIdentity
issAuditTrap = _IssAuditTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 11)
)


class _IssAuditTrapEvent_Type(Integer32):
    """Custom type issAuditTrapEvent based on Integer32"""
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
        *(("openFailed", 1),
          ("writeFailed", 2),
          ("sizeExceeded", 3),
          ("sizeThresholdHit", 4))
    )


_IssAuditTrapEvent_Type.__name__ = "Integer32"
_IssAuditTrapEvent_Object = MibScalar
issAuditTrapEvent = _IssAuditTrapEvent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 11, 1),
    _IssAuditTrapEvent_Type()
)
issAuditTrapEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    issAuditTrapEvent.setStatus("current")


class _IssAuditTrapEventTime_Type(DisplayString):
    """Custom type issAuditTrapEventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )
    fixed_length = 24


_IssAuditTrapEventTime_Type.__name__ = "DisplayString"
_IssAuditTrapEventTime_Object = MibScalar
issAuditTrapEventTime = _IssAuditTrapEventTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 11, 2),
    _IssAuditTrapEventTime_Type()
)
issAuditTrapEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    issAuditTrapEventTime.setStatus("current")


class _IssAuditTrapFileName_Type(DisplayString):
    """Custom type issAuditTrapFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_IssAuditTrapFileName_Type.__name__ = "DisplayString"
_IssAuditTrapFileName_Object = MibScalar
issAuditTrapFileName = _IssAuditTrapFileName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 11, 3),
    _IssAuditTrapFileName_Type()
)
issAuditTrapFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issAuditTrapFileName.setStatus("current")
_IssModule_ObjectIdentity = ObjectIdentity
issModule = _IssModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 12)
)
_IssModuleTable_Object = MibTable
issModuleTable = _IssModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 12, 1)
)
if mibBuilder.loadTexts:
    issModuleTable.setStatus("current")
_IssModuleEntry_Object = MibTableRow
issModuleEntry = _IssModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 12, 1, 1)
)
issModuleEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issModuleId"),
)
if mibBuilder.loadTexts:
    issModuleEntry.setStatus("current")


class _IssModuleId_Type(Integer32):
    """Custom type issModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IssModuleId_Type.__name__ = "Integer32"
_IssModuleId_Object = MibTableColumn
issModuleId = _IssModuleId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 12, 1, 1, 1),
    _IssModuleId_Type()
)
issModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issModuleId.setStatus("current")


class _IssModuleSystemControl_Type(Integer32):
    """Custom type issModuleSystemControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("shutdown", 1),
          ("start", 2))
    )


_IssModuleSystemControl_Type.__name__ = "Integer32"
_IssModuleSystemControl_Object = MibTableColumn
issModuleSystemControl = _IssModuleSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 12, 1, 1, 2),
    _IssModuleSystemControl_Type()
)
issModuleSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issModuleSystemControl.setStatus("current")
_IssSwitchFan_ObjectIdentity = ObjectIdentity
issSwitchFan = _IssSwitchFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 13)
)
_IssSwitchFanTable_Object = MibTable
issSwitchFanTable = _IssSwitchFanTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 13, 1)
)
if mibBuilder.loadTexts:
    issSwitchFanTable.setStatus("current")
_IssSwitchFanEntry_Object = MibTableRow
issSwitchFanEntry = _IssSwitchFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 13, 1, 1)
)
issSwitchFanEntry.setIndexNames(
    (0, "ARICENT-ISS-MIB", "issSwitchFanIndex"),
)
if mibBuilder.loadTexts:
    issSwitchFanEntry.setStatus("current")


class _IssSwitchFanIndex_Type(Integer32):
    """Custom type issSwitchFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IssSwitchFanIndex_Type.__name__ = "Integer32"
_IssSwitchFanIndex_Object = MibTableColumn
issSwitchFanIndex = _IssSwitchFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 13, 1, 1, 1),
    _IssSwitchFanIndex_Type()
)
issSwitchFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issSwitchFanIndex.setStatus("current")


class _IssSwitchFanStatus_Type(Integer32):
    """Custom type issSwitchFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_IssSwitchFanStatus_Type.__name__ = "Integer32"
_IssSwitchFanStatus_Object = MibTableColumn
issSwitchFanStatus = _IssSwitchFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 13, 1, 1, 2),
    _IssSwitchFanStatus_Type()
)
issSwitchFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issSwitchFanStatus.setStatus("current")
_IssAclNp_ObjectIdentity = ObjectIdentity
issAclNp = _IssAclNp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 14)
)


class _IssAclProvisionMode_Type(Integer32):
    """Custom type issAclProvisionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 1),
          ("consolidated", 2))
    )


_IssAclProvisionMode_Type.__name__ = "Integer32"
_IssAclProvisionMode_Object = MibScalar
issAclProvisionMode = _IssAclProvisionMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 14, 1),
    _IssAclProvisionMode_Type()
)
issAclProvisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issAclProvisionMode.setStatus("current")


class _IssAclTriggerCommit_Type(Integer32):
    """Custom type issAclTriggerCommit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IssAclTriggerCommit_Type.__name__ = "Integer32"
_IssAclTriggerCommit_Object = MibScalar
issAclTriggerCommit = _IssAclTriggerCommit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 14, 2),
    _IssAclTriggerCommit_Type()
)
issAclTriggerCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issAclTriggerCommit.setStatus("current")
_IssAclTrafficControl_ObjectIdentity = ObjectIdentity
issAclTrafficControl = _IssAclTrafficControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 15)
)


class _IssAclTrafficSeperationCtrl_Type(Integer32):
    """Custom type issAclTrafficSeperationCtrl based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("systemdefault", 1),
          ("userconfig", 2),
          ("none", 3))
    )


_IssAclTrafficSeperationCtrl_Type.__name__ = "Integer32"
_IssAclTrafficSeperationCtrl_Object = MibScalar
issAclTrafficSeperationCtrl = _IssAclTrafficSeperationCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 15, 1),
    _IssAclTrafficSeperationCtrl_Type()
)
issAclTrafficSeperationCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issAclTrafficSeperationCtrl.setStatus("current")
_IssLogTrap_ObjectIdentity = ObjectIdentity
issLogTrap = _IssLogTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 16)
)


class _IssLogTrapEvent_Type(Integer32):
    """Custom type issLogTrapEvent based on Integer32"""
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
        *(("openFailed", 1),
          ("writeFailed", 2),
          ("sizeExceeded", 3),
          ("sizeThresholdHit", 4))
    )


_IssLogTrapEvent_Type.__name__ = "Integer32"
_IssLogTrapEvent_Object = MibScalar
issLogTrapEvent = _IssLogTrapEvent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 16, 1),
    _IssLogTrapEvent_Type()
)
issLogTrapEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    issLogTrapEvent.setStatus("current")


class _IssLogTrapEventTime_Type(DisplayString):
    """Custom type issLogTrapEventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )
    fixed_length = 24


_IssLogTrapEventTime_Type.__name__ = "DisplayString"
_IssLogTrapEventTime_Object = MibScalar
issLogTrapEventTime = _IssLogTrapEventTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 16, 2),
    _IssLogTrapEventTime_Type()
)
issLogTrapEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    issLogTrapEventTime.setStatus("current")


class _IssLogTrapFileName_Type(DisplayString):
    """Custom type issLogTrapFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_IssLogTrapFileName_Type.__name__ = "DisplayString"
_IssLogTrapFileName_Object = MibScalar
issLogTrapFileName = _IssLogTrapFileName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 16, 3),
    _IssLogTrapFileName_Type()
)
issLogTrapFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issLogTrapFileName.setStatus("current")
_IssHealthCheckGroup_ObjectIdentity = ObjectIdentity
issHealthCheckGroup = _IssHealthCheckGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 17)
)


class _IssHealthChkStatus_Type(Integer32):
    """Custom type issHealthChkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("upAndRunning", 1),
          ("downNonRecoverableErr", 2),
          ("upRecoverableRuntimeErr", 3))
    )


_IssHealthChkStatus_Type.__name__ = "Integer32"
_IssHealthChkStatus_Object = MibScalar
issHealthChkStatus = _IssHealthChkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 17, 1),
    _IssHealthChkStatus_Type()
)
issHealthChkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issHealthChkStatus.setStatus("current")


class _IssHealthChkErrorReason_Type(Integer32):
    """Custom type issHealthChkErrorReason based on Integer32"""
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
        *(("nonRecovTaskInitializationFailure", 1),
          ("nonRecovInsufficientStartupMemory", 2),
          ("recovCruBuffExhausted", 3),
          ("recovConfigRestoreFailed", 4),
          ("recovProtocolMemPoolExhausted", 5))
    )


_IssHealthChkErrorReason_Type.__name__ = "Integer32"
_IssHealthChkErrorReason_Object = MibScalar
issHealthChkErrorReason = _IssHealthChkErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 17, 2),
    _IssHealthChkErrorReason_Type()
)
issHealthChkErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issHealthChkErrorReason.setStatus("current")
_IssHealthChkMemAllocErrPoolId_Type = Integer32
_IssHealthChkMemAllocErrPoolId_Object = MibScalar
issHealthChkMemAllocErrPoolId = _IssHealthChkMemAllocErrPoolId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 17, 3),
    _IssHealthChkMemAllocErrPoolId_Type()
)
issHealthChkMemAllocErrPoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issHealthChkMemAllocErrPoolId.setStatus("current")


class _IssHealthChkConfigRestoreStatus_Type(Integer32):
    """Custom type issHealthChkConfigRestoreStatus based on Integer32"""
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
        *(("configRestoreSuccess", 1),
          ("configRestoreFailed", 2),
          ("configRestoreInProgress", 3),
          ("configRestoreDefault", 4))
    )


_IssHealthChkConfigRestoreStatus_Type.__name__ = "Integer32"
_IssHealthChkConfigRestoreStatus_Object = MibScalar
issHealthChkConfigRestoreStatus = _IssHealthChkConfigRestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 17, 4),
    _IssHealthChkConfigRestoreStatus_Type()
)
issHealthChkConfigRestoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issHealthChkConfigRestoreStatus.setStatus("current")


class _IssHealthChkClearCtr_Type(Bits):
    """Custom type issHealthChkClearCtr based on Bits"""
    namedValues = NamedValues(
        *(("bgp", 1),
          ("ospf", 2),
          ("rip", 3),
          ("rip6", 4),
          ("ospf3", 5),
          ("ipv4", 6),
          ("ipv6", 7))
    )

_IssHealthChkClearCtr_Type.__name__ = "Bits"
_IssHealthChkClearCtr_Object = MibScalar
issHealthChkClearCtr = _IssHealthChkClearCtr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 17, 5),
    _IssHealthChkClearCtr_Type()
)
issHealthChkClearCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issHealthChkClearCtr.setStatus("current")

# Managed Objects groups


# Notification objects

issTrapConfigRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 81, 0, 1)
)
issTrapConfigRestore.setObjects(
    ("ARICENT-ISS-MIB", "issConfigRestoreStatus")
)
if mibBuilder.loadTexts:
    issTrapConfigRestore.setStatus(
        "current"
    )

issMsrUpdateEventFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 81, 0, 2)
)
issMsrUpdateEventFail.setObjects(
      *(("ARICENT-ISS-MIB", "issMsrFailedOid"),
        ("ARICENT-ISS-MIB", "issMsrFailedValue"))
)
if mibBuilder.loadTexts:
    issMsrUpdateEventFail.setStatus(
        "current"
    )

issAuditTrapMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 81, 0, 3)
)
issAuditTrapMessage.setObjects(
      *(("ARICENT-ISS-MIB", "issAuditTrapEvent"),
        ("ARICENT-ISS-MIB", "issAuditTrapEventTime"),
        ("ARICENT-ISS-MIB", "issAuditTrapFileName"))
)
if mibBuilder.loadTexts:
    issAuditTrapMessage.setStatus(
        "current"
    )

issTrapTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 81, 0, 4)
)
issTrapTemperature.setObjects(
      *(("ARICENT-ISS-MIB", "issSwitchMinThresholdTemperature"),
        ("ARICENT-ISS-MIB", "issSwitchMaxThresholdTemperature"),
        ("ARICENT-ISS-MIB", "issSwitchCurrentTemperature"))
)
if mibBuilder.loadTexts:
    issTrapTemperature.setStatus(
        "current"
    )

issTrapCPUThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 81, 0, 5)
)
issTrapCPUThreshold.setObjects(
      *(("ARICENT-ISS-MIB", "issSwitchMaxCPUThreshold"),
        ("ARICENT-ISS-MIB", "issSwitchCurrentCPUThreshold"))
)
if mibBuilder.loadTexts:
    issTrapCPUThreshold.setStatus(
        "current"
    )

issTrapPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 81, 0, 6)
)
issTrapPowerSupply.setObjects(
      *(("ARICENT-ISS-MIB", "issSwitchPowerSurge"),
        ("ARICENT-ISS-MIB", "issSwitchPowerFailure"),
        ("ARICENT-ISS-MIB", "issSwitchCurrentPowerSupply"))
)
if mibBuilder.loadTexts:
    issTrapPowerSupply.setStatus(
        "current"
    )

issTrapRAMUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 81, 0, 7)
)
issTrapRAMUsage.setObjects(
      *(("ARICENT-ISS-MIB", "issSwitchMaxRAMUsage"),
        ("ARICENT-ISS-MIB", "issSwitchCurrentRAMUsage"))
)
if mibBuilder.loadTexts:
    issTrapRAMUsage.setStatus(
        "current"
    )

issTrapFlashUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 81, 0, 8)
)
issTrapFlashUsage.setObjects(
      *(("ARICENT-ISS-MIB", "issSwitchMaxFlashUsage"),
        ("ARICENT-ISS-MIB", "issSwitchCurrentFlashUsage"))
)
if mibBuilder.loadTexts:
    issTrapFlashUsage.setStatus(
        "current"
    )

issTrapFanStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 81, 0, 9)
)
issTrapFanStatus.setObjects(
      *(("ARICENT-ISS-MIB", "issSwitchFanIndex"),
        ("ARICENT-ISS-MIB", "issSwitchFanStatus"))
)
if mibBuilder.loadTexts:
    issTrapFanStatus.setStatus(
        "current"
    )

issLogTrapMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 81, 0, 10)
)
issLogTrapMessage.setObjects(
      *(("ARICENT-ISS-MIB", "issLogTrapEvent"),
        ("ARICENT-ISS-MIB", "issLogTrapEventTime"),
        ("ARICENT-ISS-MIB", "issLogTrapFileName"))
)
if mibBuilder.loadTexts:
    issLogTrapMessage.setStatus(
        "current"
    )

issPauseFloodSnmpTrapMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 81, 0, 11)
)
issPauseFloodSnmpTrapMessage.setObjects(
    ("ARICENT-ISS-MIB", "issPortCtrlPauseFloodStatus")
)
if mibBuilder.loadTexts:
    issPauseFloodSnmpTrapMessage.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-ISS-MIB",
    **{"PortList": PortList,
       "iss": iss,
       "issNotifications": issNotifications,
       "issTrapConfigRestore": issTrapConfigRestore,
       "issMsrUpdateEventFail": issMsrUpdateEventFail,
       "issAuditTrapMessage": issAuditTrapMessage,
       "issTrapTemperature": issTrapTemperature,
       "issTrapCPUThreshold": issTrapCPUThreshold,
       "issTrapPowerSupply": issTrapPowerSupply,
       "issTrapRAMUsage": issTrapRAMUsage,
       "issTrapFlashUsage": issTrapFlashUsage,
       "issTrapFanStatus": issTrapFanStatus,
       "issLogTrapMessage": issLogTrapMessage,
       "issPauseFloodSnmpTrapMessage": issPauseFloodSnmpTrapMessage,
       "issSystem": issSystem,
       "issSwitchName": issSwitchName,
       "issHardwareVersion": issHardwareVersion,
       "issFirmwareVersion": issFirmwareVersion,
       "issDefaultIpAddrCfgMode": issDefaultIpAddrCfgMode,
       "issDefaultIpAddr": issDefaultIpAddr,
       "issDefaultIpSubnetMask": issDefaultIpSubnetMask,
       "issEffectiveIpAddr": issEffectiveIpAddr,
       "issDefaultInterface": issDefaultInterface,
       "issRestart": issRestart,
       "issConfigSaveOption": issConfigSaveOption,
       "issConfigSaveIpAddr": issConfigSaveIpAddr,
       "issConfigSaveFileName": issConfigSaveFileName,
       "issInitiateConfigSave": issInitiateConfigSave,
       "issConfigSaveStatus": issConfigSaveStatus,
       "issConfigRestoreOption": issConfigRestoreOption,
       "issConfigRestoreIpAddr": issConfigRestoreIpAddr,
       "issConfigRestoreFileName": issConfigRestoreFileName,
       "issInitiateConfigRestore": issInitiateConfigRestore,
       "issConfigRestoreStatus": issConfigRestoreStatus,
       "issDlImageFromIp": issDlImageFromIp,
       "issDlImageName": issDlImageName,
       "issInitiateDlImage": issInitiateDlImage,
       "issLoggingOption": issLoggingOption,
       "issUploadLogFileToIp": issUploadLogFileToIp,
       "issLogFileName": issLogFileName,
       "issInitiateUlLogFile": issInitiateUlLogFile,
       "issRemoteSaveStatus": issRemoteSaveStatus,
       "issDownloadStatus": issDownloadStatus,
       "issSysContact": issSysContact,
       "issSysLocation": issSysLocation,
       "issLoginAuthentication": issLoginAuthentication,
       "issSwitchBaseMacAddress": issSwitchBaseMacAddress,
       "issOOBInterface": issOOBInterface,
       "issSwitchDate": issSwitchDate,
       "issNoCliConsole": issNoCliConsole,
       "issDefaultIpAddrAllocProtocol": issDefaultIpAddrAllocProtocol,
       "issHttpPort": issHttpPort,
       "issHttpStatus": issHttpStatus,
       "issConfigRestoreFileVersion": issConfigRestoreFileVersion,
       "issDefaultRmIfName": issDefaultRmIfName,
       "issDefaultVlanId": issDefaultVlanId,
       "issNpapiMode": issNpapiMode,
       "issConfigAutoSaveTrigger": issConfigAutoSaveTrigger,
       "issConfigIncrSaveFlag": issConfigIncrSaveFlag,
       "issConfigRollbackFlag": issConfigRollbackFlag,
       "issConfigSyncUpOperation": issConfigSyncUpOperation,
       "issFrontPanelPortCount": issFrontPanelPortCount,
       "issAuditLogStatus": issAuditLogStatus,
       "issAuditLogFileName": issAuditLogFileName,
       "issAuditLogFileSize": issAuditLogFileSize,
       "issAuditLogReset": issAuditLogReset,
       "issAuditLogRemoteIpAddr": issAuditLogRemoteIpAddr,
       "issAuditLogInitiateTransfer": issAuditLogInitiateTransfer,
       "issAuditTransferFileName": issAuditTransferFileName,
       "issDownLoadTransferMode": issDownLoadTransferMode,
       "issDownLoadUserName": issDownLoadUserName,
       "issDownLoadPassword": issDownLoadPassword,
       "issUploadLogTransferMode": issUploadLogTransferMode,
       "issUploadLogUserName": issUploadLogUserName,
       "issUploadLogPasswd": issUploadLogPasswd,
       "issConfigSaveTransferMode": issConfigSaveTransferMode,
       "issConfigSaveUserName": issConfigSaveUserName,
       "issConfigSavePassword": issConfigSavePassword,
       "issSwitchMinThresholdTemperature": issSwitchMinThresholdTemperature,
       "issSwitchMaxThresholdTemperature": issSwitchMaxThresholdTemperature,
       "issSwitchCurrentTemperature": issSwitchCurrentTemperature,
       "issSwitchMaxCPUThreshold": issSwitchMaxCPUThreshold,
       "issSwitchCurrentCPUThreshold": issSwitchCurrentCPUThreshold,
       "issSwitchPowerSurge": issSwitchPowerSurge,
       "issSwitchPowerFailure": issSwitchPowerFailure,
       "issSwitchCurrentPowerSupply": issSwitchCurrentPowerSupply,
       "issSwitchMaxRAMUsage": issSwitchMaxRAMUsage,
       "issSwitchCurrentRAMUsage": issSwitchCurrentRAMUsage,
       "issSwitchMaxFlashUsage": issSwitchMaxFlashUsage,
       "issSwitchCurrentFlashUsage": issSwitchCurrentFlashUsage,
       "issConfigRestoreFileFormatVersion": issConfigRestoreFileFormatVersion,
       "issDebugOption": issDebugOption,
       "issConfigDefaultValueSaveOption": issConfigDefaultValueSaveOption,
       "issConfigSaveIpAddrType": issConfigSaveIpAddrType,
       "issConfigSaveIpvxAddr": issConfigSaveIpvxAddr,
       "issConfigRestoreIpAddrType": issConfigRestoreIpAddrType,
       "issConfigRestoreIpvxAddr": issConfigRestoreIpvxAddr,
       "issDlImageFromIpAddrType": issDlImageFromIpAddrType,
       "issDlImageFromIpvx": issDlImageFromIpvx,
       "issUploadLogFileToIpAddrType": issUploadLogFileToIpAddrType,
       "issUploadLogFileToIpvx": issUploadLogFileToIpvx,
       "issAuditLogRemoteIpAddrType": issAuditLogRemoteIpAddrType,
       "issAuditLogRemoteIpvxAddr": issAuditLogRemoteIpvxAddr,
       "issSystemTimerSpeed": issSystemTimerSpeed,
       "issMgmtInterfaceRouting": issMgmtInterfaceRouting,
       "issMacLearnRateLimit": issMacLearnRateLimit,
       "issMacLearnRateLimitInterval": issMacLearnRateLimitInterval,
       "issVrfUnqMacFlag": issVrfUnqMacFlag,
       "issLoginAttempts": issLoginAttempts,
       "issLoginLockTime": issLoginLockTime,
       "issAuditLogSizeThreshold": issAuditLogSizeThreshold,
       "issTelnetStatus": issTelnetStatus,
       "issWebSessionTimeOut": issWebSessionTimeOut,
       "issWebSessionMaxUsers": issWebSessionMaxUsers,
       "issHeartBeatMode": issHeartBeatMode,
       "issRmRType": issRmRType,
       "issRmDType": issRmDType,
       "issClearConfig": issClearConfig,
       "issClearConfigFileName": issClearConfigFileName,
       "issTelnetClientStatus": issTelnetClientStatus,
       "issSshClientStatus": issSshClientStatus,
       "issActiveTelnetClientSessions": issActiveTelnetClientSessions,
       "issActiveSshClientSessions": issActiveSshClientSessions,
       "issLogFileSize": issLogFileSize,
       "issLogReset": issLogReset,
       "issLogSizeThreshold": issLogSizeThreshold,
       "issAutomaticPortCreate": issAutomaticPortCreate,
       "issUlRemoteLogFileName": issUlRemoteLogFileName,
       "issDefaultExecTimeOut": issDefaultExecTimeOut,
       "issRmStackingInterfaceType": issRmStackingInterfaceType,
       "issPeerLoggingOption": issPeerLoggingOption,
       "issStandbyRestart": issStandbyRestart,
       "issRestoreType": issRestoreType,
       "issSwitchModeType": issSwitchModeType,
       "issConfigRestoreRetries": issConfigRestoreRetries,
       "issPauseFloodSamplingInterval": issPauseFloodSamplingInterval,
       "issPauseFloodProtect": issPauseFloodProtect,
       "issPauseFloodMode": issPauseFloodMode,
       "issPauseFloodReset": issPauseFloodReset,
       "issPauseFloodTraceSeverityLevel": issPauseFloodTraceSeverityLevel,
       "issPauseFloodTraceOption": issPauseFloodTraceOption,
       "issPortsSwitchingModeStatus": issPortsSwitchingModeStatus,
       "issDebugTimeStampOption": issDebugTimeStampOption,
       "issLdapLoginPrivilege": issLdapLoginPrivilege,
       "issLdapAttributeName": issLdapAttributeName,
       "issConfigRestoreFileSkuManifest": issConfigRestoreFileSkuManifest,
       "issDlImageType": issDlImageType,
       "issFirmwareCpldVersion": issFirmwareCpldVersion,
       "issHttpMaxSessions": issHttpMaxSessions,
       "issConfigControl": issConfigControl,
       "issConfigCtrlTable": issConfigCtrlTable,
       "issConfigCtrlEntry": issConfigCtrlEntry,
       "issConfigCtrlIndex": issConfigCtrlIndex,
       "issConfigCtrlEgressStatus": issConfigCtrlEgressStatus,
       "issConfigCtrlStatsCollection": issConfigCtrlStatsCollection,
       "issConfigCtrlStatus": issConfigCtrlStatus,
       "issPortCtrlTable": issPortCtrlTable,
       "issPortCtrlEntry": issPortCtrlEntry,
       "issPortCtrlIndex": issPortCtrlIndex,
       "issPortCtrlMode": issPortCtrlMode,
       "issPortCtrlDuplex": issPortCtrlDuplex,
       "issPortCtrlSpeed": issPortCtrlSpeed,
       "issPortCtrlFlowControl": issPortCtrlFlowControl,
       "issPortCtrlRenegotiate": issPortCtrlRenegotiate,
       "issPortCtrlMaxMacAddr": issPortCtrlMaxMacAddr,
       "issPortCtrlMaxMacAction": issPortCtrlMaxMacAction,
       "issPortHOLBlockPrevention": issPortHOLBlockPrevention,
       "issPortAutoNegAdvtCapBits": issPortAutoNegAdvtCapBits,
       "issPortCpuControlledLearning": issPortCpuControlledLearning,
       "issPortMdiOrMdixCap": issPortMdiOrMdixCap,
       "issPortCtrlFlowControlMaxRate": issPortCtrlFlowControlMaxRate,
       "issPortCtrlFlowControlMinRate": issPortCtrlFlowControlMinRate,
       "issPortCtrlPauseFloodProtect": issPortCtrlPauseFloodProtect,
       "issPortCtrlPauseFloodMode": issPortCtrlPauseFloodMode,
       "issPortCtrlPauseFloodStatus": issPortCtrlPauseFloodStatus,
       "issPortCtrlPauseFloodReset": issPortCtrlPauseFloodReset,
       "issPortCtrlPauseFloodStats": issPortCtrlPauseFloodStats,
       "issPortCtrlPauseFloodStatsClear": issPortCtrlPauseFloodStatsClear,
       "issPortCtrlPauseFloodTraceOption": issPortCtrlPauseFloodTraceOption,
       "issPortCtrlSwitchModeType": issPortCtrlSwitchModeType,
       "issPortCtrlSwitchModeStatus": issPortCtrlSwitchModeStatus,
       "issPortCtrlInbandAutoNeg": issPortCtrlInbandAutoNeg,
       "issPortCtrlBypassInbandAutoNeg": issPortCtrlBypassInbandAutoNeg,
       "issPortCtrlForceSpeed": issPortCtrlForceSpeed,
       "issPortIsolationTable": issPortIsolationTable,
       "issPortIsolationEntry": issPortIsolationEntry,
       "issPortIsolationIngressPort": issPortIsolationIngressPort,
       "issPortIsolationInVlanId": issPortIsolationInVlanId,
       "issPortIsolationEgressPort": issPortIsolationEgressPort,
       "issPortIsolationStorageType": issPortIsolationStorageType,
       "issPortIsolationRowStatus": issPortIsolationRowStatus,
       "issMirror": issMirror,
       "issMirrorStatus": issMirrorStatus,
       "issMirrorToPort": issMirrorToPort,
       "issMirrorCtrlTable": issMirrorCtrlTable,
       "issMirrorCtrlEntry": issMirrorCtrlEntry,
       "issMirrorCtrlIndex": issMirrorCtrlIndex,
       "issMirrorCtrlIngressMirroring": issMirrorCtrlIngressMirroring,
       "issMirrorCtrlEgressMirroring": issMirrorCtrlEgressMirroring,
       "issMirrorCtrlStatus": issMirrorCtrlStatus,
       "issMirrorCtrlRemainingSrcRcrds": issMirrorCtrlRemainingSrcRcrds,
       "issMirrorCtrlRemainingDestRcrds": issMirrorCtrlRemainingDestRcrds,
       "issMirrorCtrlExtnTable": issMirrorCtrlExtnTable,
       "issMirrorCtrlExtnEntry": issMirrorCtrlExtnEntry,
       "issMirrorCtrlExtnSessionIndex": issMirrorCtrlExtnSessionIndex,
       "issMirrorCtrlExtnMirrType": issMirrorCtrlExtnMirrType,
       "issMirrorCtrlExtnRSpanStatus": issMirrorCtrlExtnRSpanStatus,
       "issMirrorCtrlExtnRSpanVlanId": issMirrorCtrlExtnRSpanVlanId,
       "issMirrorCtrlExtnRSpanContext": issMirrorCtrlExtnRSpanContext,
       "issMirrorCtrlExtnStatus": issMirrorCtrlExtnStatus,
       "issMirrorCtrlExtnSrcTable": issMirrorCtrlExtnSrcTable,
       "issMirrorCtrlExtnSrcEntry": issMirrorCtrlExtnSrcEntry,
       "issMirrorCtrlExtnSrcId": issMirrorCtrlExtnSrcId,
       "issMirrorCtrlExtnSrcCfg": issMirrorCtrlExtnSrcCfg,
       "issMirrorCtrlExtnSrcMode": issMirrorCtrlExtnSrcMode,
       "issMirrorCtrlExtnSrcVlanTable": issMirrorCtrlExtnSrcVlanTable,
       "issMirrorCtrlExtnSrcVlanEntry": issMirrorCtrlExtnSrcVlanEntry,
       "issMirrorCtrlExtnSrcVlanContext": issMirrorCtrlExtnSrcVlanContext,
       "issMirrorCtrlExtnSrcVlanId": issMirrorCtrlExtnSrcVlanId,
       "issMirrorCtrlExtnSrcVlanCfg": issMirrorCtrlExtnSrcVlanCfg,
       "issMirrorCtrlExtnSrcVlanMode": issMirrorCtrlExtnSrcVlanMode,
       "issMirrorCtrlExtnDestinationTable": issMirrorCtrlExtnDestinationTable,
       "issMirrorCtrlExtnDestinationEntry": issMirrorCtrlExtnDestinationEntry,
       "issMirrorCtrlExtnDestination": issMirrorCtrlExtnDestination,
       "issMirrorCtrlExtnDestCfg": issMirrorCtrlExtnDestCfg,
       "issCpuMirrorType": issCpuMirrorType,
       "issCpuMirrorToPort": issCpuMirrorToPort,
       "issRateControl": issRateControl,
       "issRateCtrlTable": issRateCtrlTable,
       "issRateCtrlEntry": issRateCtrlEntry,
       "issRateCtrlIndex": issRateCtrlIndex,
       "issRateCtrlDLFLimitValue": issRateCtrlDLFLimitValue,
       "issRateCtrlBCASTLimitValue": issRateCtrlBCASTLimitValue,
       "issRateCtrlMCASTLimitValue": issRateCtrlMCASTLimitValue,
       "issRateCtrlPortRateLimit": issRateCtrlPortRateLimit,
       "issRateCtrlPortBurstSize": issRateCtrlPortBurstSize,
       "issL2Filter": issL2Filter,
       "issL2FilterTable": issL2FilterTable,
       "issL2FilterEntry": issL2FilterEntry,
       "issL2FilterNo": issL2FilterNo,
       "issL2FilterPriority": issL2FilterPriority,
       "issL2FilterEtherType": issL2FilterEtherType,
       "issL2FilterProtocolType": issL2FilterProtocolType,
       "issL2FilterDstMacAddr": issL2FilterDstMacAddr,
       "issL2FilterSrcMacAddr": issL2FilterSrcMacAddr,
       "issL2FilterVlanId": issL2FilterVlanId,
       "issL2FilterInPortList": issL2FilterInPortList,
       "issL2FilterAction": issL2FilterAction,
       "issL2FilterMatchCount": issL2FilterMatchCount,
       "issL2FilterStatus": issL2FilterStatus,
       "issL2FilterOutPortList": issL2FilterOutPortList,
       "issL2FilterDirection": issL2FilterDirection,
       "issL3Filter": issL3Filter,
       "issL3FilterTable": issL3FilterTable,
       "issL3FilterEntry": issL3FilterEntry,
       "issL3FilterNo": issL3FilterNo,
       "issL3FilterPriority": issL3FilterPriority,
       "issL3FilterProtocol": issL3FilterProtocol,
       "issL3FilterMessageType": issL3FilterMessageType,
       "issL3FilterMessageCode": issL3FilterMessageCode,
       "issL3FilterDstIpAddr": issL3FilterDstIpAddr,
       "issL3FilterSrcIpAddr": issL3FilterSrcIpAddr,
       "issL3FilterDstIpAddrMask": issL3FilterDstIpAddrMask,
       "issL3FilterSrcIpAddrMask": issL3FilterSrcIpAddrMask,
       "issL3FilterMinDstProtPort": issL3FilterMinDstProtPort,
       "issL3FilterMaxDstProtPort": issL3FilterMaxDstProtPort,
       "issL3FilterMinSrcProtPort": issL3FilterMinSrcProtPort,
       "issL3FilterMaxSrcProtPort": issL3FilterMaxSrcProtPort,
       "issL3FilterInPortList": issL3FilterInPortList,
       "issL3FilterOutPortList": issL3FilterOutPortList,
       "issL3FilterAckBit": issL3FilterAckBit,
       "issL3FilterRstBit": issL3FilterRstBit,
       "issL3FilterTos": issL3FilterTos,
       "issL3FilterDscp": issL3FilterDscp,
       "issL3FilterDirection": issL3FilterDirection,
       "issL3FilterAction": issL3FilterAction,
       "issL3FilterMatchCount": issL3FilterMatchCount,
       "issL3FilterStatus": issL3FilterStatus,
       "issIpAuthMgr": issIpAuthMgr,
       "issIpAuthMgrTable": issIpAuthMgrTable,
       "issIpAuthMgrEntry": issIpAuthMgrEntry,
       "issIpAuthMgrIpAddr": issIpAuthMgrIpAddr,
       "issIpAuthMgrIpMask": issIpAuthMgrIpMask,
       "issIpAuthMgrPortList": issIpAuthMgrPortList,
       "issIpAuthMgrVlanList": issIpAuthMgrVlanList,
       "issIpAuthMgrOOBPort": issIpAuthMgrOOBPort,
       "issIpAuthMgrAllowedServices": issIpAuthMgrAllowedServices,
       "issIpAuthMgrRowStatus": issIpAuthMgrRowStatus,
       "issExt": issExt,
       "issL4Switching": issL4Switching,
       "issL4SwitchingFilterTable": issL4SwitchingFilterTable,
       "issL4SwitchingFilterEntry": issL4SwitchingFilterEntry,
       "issL4SwitchingFilterNo": issL4SwitchingFilterNo,
       "issL4SwitchingProtocol": issL4SwitchingProtocol,
       "issL4SwitchingPortNo": issL4SwitchingPortNo,
       "issL4SwitchingCopyToPort": issL4SwitchingCopyToPort,
       "issL4SwitchingFilterStatus": issL4SwitchingFilterStatus,
       "issSystemTrap": issSystemTrap,
       "issMsrFailedOid": issMsrFailedOid,
       "issMsrFailedValue": issMsrFailedValue,
       "issAuditTrap": issAuditTrap,
       "issAuditTrapEvent": issAuditTrapEvent,
       "issAuditTrapEventTime": issAuditTrapEventTime,
       "issAuditTrapFileName": issAuditTrapFileName,
       "issModule": issModule,
       "issModuleTable": issModuleTable,
       "issModuleEntry": issModuleEntry,
       "issModuleId": issModuleId,
       "issModuleSystemControl": issModuleSystemControl,
       "issSwitchFan": issSwitchFan,
       "issSwitchFanTable": issSwitchFanTable,
       "issSwitchFanEntry": issSwitchFanEntry,
       "issSwitchFanIndex": issSwitchFanIndex,
       "issSwitchFanStatus": issSwitchFanStatus,
       "issAclNp": issAclNp,
       "issAclProvisionMode": issAclProvisionMode,
       "issAclTriggerCommit": issAclTriggerCommit,
       "issAclTrafficControl": issAclTrafficControl,
       "issAclTrafficSeperationCtrl": issAclTrafficSeperationCtrl,
       "issLogTrap": issLogTrap,
       "issLogTrapEvent": issLogTrapEvent,
       "issLogTrapEventTime": issLogTrapEventTime,
       "issLogTrapFileName": issLogTrapFileName,
       "issHealthCheckGroup": issHealthCheckGroup,
       "issHealthChkStatus": issHealthChkStatus,
       "issHealthChkErrorReason": issHealthChkErrorReason,
       "issHealthChkMemAllocErrPoolId": issHealthChkMemAllocErrPoolId,
       "issHealthChkConfigRestoreStatus": issHealthChkConfigRestoreStatus,
       "issHealthChkClearCtr": issHealthChkClearCtr}
)
